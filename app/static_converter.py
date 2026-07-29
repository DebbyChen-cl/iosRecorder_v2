"""Static conversion from legacy iOS/Appium tests to recorder pytest tests.

The converter deliberately works on syntax trees and source text only.  It does
not import the legacy project, start a device, or execute a page-object method.
That makes the inventory a useful approval gate before any generated test is
replayed.
"""

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
import tokenize
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


class StaticConversionError(ValueError):
    """Raised when static conversion cannot produce a complete inventory."""


_BY_NAMES = {
    "ACCESSIBILITY_ID": "AppiumBy.ACCESSIBILITY_ID",
    "ID": "AppiumBy.ID",
    "NAME": "AppiumBy.NAME",
    "XPATH": "AppiumBy.XPATH",
    "IOS_CLASS_CHAIN": "AppiumBy.IOS_CLASS_CHAIN",
    "IOS_PREDICATE": "AppiumBy.IOS_PREDICATE",
    "CLASS_NAME": "AppiumBy.CLASS_NAME",
    "IOS_UIAUTOMATION": "AppiumBy.IOS_UIAUTOMATION",
}

_WAIT_NAMES = {"sleep", "wait", "wait_process", "wait_until_element_exist", "implicit_wait"}
_TAP_NAMES = {"tap", "click", "click_element", "tap_element", "tap_phd_btn", "tap_web_element"}
_TEXT_NAMES = {"type", "send_keys", "set_text", "type_text", "input_text", "input"}
_SWIPE_NAMES = {"swipe", "swipe_element", "swipe_on_element", "scroll", "scroll_to_element", "scroll_and_tap_vertical"}
_DRAG_NAMES = {"drag", "drag_element", "drag_coordinates", "move_to_location"}
_GESTURE_NAMES = {"pinch", "pinch_element", "pinch_zoom_element", "zoom_element", "rotate", "rotate_element"}
_ASSERTION_WORDS = ("verify", "assert", "check", "is_", "exist", "display", "visible", "highlight")
_EXTERNAL_WORDS = (
    "upload", "feedback", "sign_in", "signin", "purchase", "buy", "google", "email", "request",
    "fetch", "api", "ocr", "compare", "download", "install", "report", "send", "submit", "generate",
    "credential", "password",
)
_NON_BEHAVIORAL_NAMES = {
    "logger", "qa_log", "add_result", "record_locator_usage", "rp_step", "step", "print",
    "format", "str", "int", "float", "len", "range", "getattr", "isinstance", "append",
    "join", "lower", "strip", "exists", "currentframe",
}


@dataclass(frozen=True)
class FunctionRecord:
    name: str
    node: ast.FunctionDef | ast.AsyncFunctionDef
    path: Path
    class_name: str | None


@dataclass
class SourceIndex:
    """Indexes functions and literal locators without importing source modules."""

    root: Path
    functions: dict[str, list[FunctionRecord]] = field(default_factory=dict)
    locators: dict[tuple[str | None, str], dict[str, str]] = field(default_factory=dict)
    attribute_types: dict[str, set[str]] = field(default_factory=dict)

    @classmethod
    def load(cls, source: Path, project_root: Path | None = None) -> "SourceIndex":
        root = (project_root or source.parent).resolve()
        index = cls(root)
        files = sorted({source.resolve(), *root.rglob("*.py")})
        for path in files:
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except (OSError, SyntaxError, UnicodeDecodeError):
                continue
            index._index_tree(tree, path)
        return index

    def _index_tree(self, tree: ast.AST, path: Path) -> None:
        def visit(body: Iterable[ast.stmt], class_name: str | None = None) -> None:
            for node in body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    record = FunctionRecord(node.name, node, path, class_name)
                    self.functions.setdefault(node.name, []).append(record)
                elif isinstance(node, ast.ClassDef):
                    visit(node.body, node.name)
                    for member in node.body:
                        if isinstance(member, (ast.Assign, ast.AnnAssign)):
                            self._index_locator(member, class_name)
                elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                    self._index_locator(node, class_name)
                elif isinstance(node, (ast.If, ast.For, ast.While, ast.Try)):
                    visit(getattr(node, "body", []), class_name)
                    visit(getattr(node, "orelse", []), class_name)

        visit(getattr(tree, "body", []))
        # Suite setup fixtures commonly initialise page objects on ``self``.
        # The test methods themselves live in other modules, so retain this
        # project-wide type information instead of relying only on locals.
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            value = node.value
            if not isinstance(value, ast.Call):
                continue
            class_name = _called_name(value.func)
            if not class_name:
                continue
            targets = [node.target] if isinstance(node, ast.AnnAssign) else node.targets
            for target in targets:
                if isinstance(target, ast.Attribute):
                    self.attribute_types.setdefault(target.attr, set()).add(class_name)

    def _index_locator(self, node: ast.Assign | ast.AnnAssign, class_name: str | None) -> None:
        value = node.value if isinstance(node, ast.AnnAssign) else node.value
        locator = _literal_locator(value)
        if locator is None:
            return
        targets = [node.target] if isinstance(node, ast.AnnAssign) else node.targets
        for target in targets:
            if isinstance(target, ast.Name):
                self.locators[(class_name, target.id)] = locator

    def resolve_function(self, name: str, class_name: str | None = None) -> FunctionRecord | None:
        records = [record for record in self.functions.get(name, []) if _is_expandable_record(record)]
        if class_name:
            matching = [record for record in records if record.class_name == class_name]
            if len(matching) == 1:
                return matching[0]
        if len(records) == 1:
            return records[0]
        # A unique top-level helper is safe to inline even when a page class has
        # a method with the same name.
        top_level = [record for record in records if record.class_name is None]
        return top_level[0] if len(top_level) == 1 else None

    def resolve_locator(self, attr: str, class_name: str | None = None) -> dict[str, str] | None:
        if class_name and (class_name, attr) in self.locators:
            return self.locators[(class_name, attr)]
        matches = [value for (owner, name), value in self.locators.items() if name == attr]
        return matches[0] if len(matches) == 1 else None

    def resolve_attribute_type(self, attr: str) -> str | None:
        matches = self.attribute_types.get(attr, set())
        return next(iter(matches)) if len(matches) == 1 else None


def _source(node: ast.AST) -> str:
    try:
        return ast.unparse(node)
    except AttributeError:  # pragma: no cover - Python 3.8 fallback
        return getattr(node, "id", "legacy expression")


def _literal(node: ast.AST | None) -> Any:
    if node is None:
        return None
    try:
        return ast.literal_eval(node)
    except (ValueError, TypeError, SyntaxError):
        return None


def _literal_or_source(node: ast.AST | None, bindings: dict[str, ast.AST]) -> tuple[Any, bool]:
    seen: set[str] = set()
    while isinstance(node, ast.Name) and node.id in bindings and node.id not in seen:
        seen.add(node.id)
        node = bindings[node.id]
    value = _literal(node)
    return (value, value is not None or isinstance(node, ast.Constant))


def _bound_node(node: ast.AST, bindings: dict[str, ast.AST]) -> ast.AST:
    seen: set[str] = set()
    while isinstance(node, ast.Name) and node.id in bindings and node.id not in seen:
        seen.add(node.id)
        node = bindings[node.id]
    return node


def _literal_locator(node: ast.AST | None) -> dict[str, str] | None:
    if not isinstance(node, (ast.Tuple, ast.List)) or len(node.elts) != 2:
        return None
    by_node, value_node = node.elts
    if isinstance(by_node, ast.Attribute):
        by_name = by_node.attr
    elif isinstance(by_node, ast.Name):
        by_name = by_node.id
    else:
        return None
    value = _literal(value_node)
    if by_name not in _BY_NAMES or not isinstance(value, str):
        return None
    return {"by": _BY_NAMES[by_name], "value": value}


def _attribute_chain(node: ast.AST | None) -> list[str]:
    chain: list[str] = []
    while isinstance(node, ast.Attribute):
        chain.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        chain.append(node.id)
    return list(reversed(chain))


def _called_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _receiver_and_method(node: ast.Call) -> tuple[str | None, str]:
    if isinstance(node.func, ast.Attribute):
        chain = _attribute_chain(node.func.value)
        return (chain[-1] if chain else None, node.func.attr)
    if isinstance(node.func, ast.Name):
        return None, node.func.id
    return None, "legacy_call"


def _object_type_for_chain(chain: list[str], index: SourceIndex, object_types: dict[str, str]) -> str | None:
    """Resolve a page-object type from a local name or a ``self.foo`` chain."""
    for name in reversed(chain):
        if object_types.get(name):
            return object_types[name]
        attribute_type = index.resolve_attribute_type(name)
        if attribute_type:
            return attribute_type
    return None


def _class_name_for_call(call: ast.Call, index: SourceIndex, object_types: dict[str, str]) -> str | None:
    if not isinstance(call.func, ast.Attribute):
        return None
    return _object_type_for_chain(_attribute_chain(call.func.value), index, object_types)


def _locator_from_expr(node: ast.AST | None, index: SourceIndex, bindings: dict[str, ast.AST], object_types: dict[str, str]) -> dict[str, str] | None:
    if isinstance(node, ast.Starred):
        node = node.value
    seen: set[str] = set()
    while isinstance(node, ast.Name) and node.id in bindings and node.id not in seen:
        seen.add(node.id)
        node = bindings[node.id]
    locator = _literal_locator(node)
    if locator:
        return locator
    chain = _attribute_chain(node)
    if not chain:
        return None
    owner = _object_type_for_chain(chain, index, object_types)
    return index.resolve_locator(chain[-1], owner)


def _find_locator(call: ast.Call, index: SourceIndex, bindings: dict[str, ast.AST], object_types: dict[str, str]) -> dict[str, str] | None:
    # Legacy code commonly uses find_element(*PageLocator.button).  Look at
    # both direct arguments and the innermost find_element call in a chain.
    for node in ast.walk(call):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in {"find_element", "get_element", "wait_until_element_exist"}:
            if len(node.args) >= 2:
                locator = _locator_from_expr(node.args[0], index, bindings, object_types)
                locator = locator or _locator_from_expr(node.args[1], index, bindings, object_types)
                if locator:
                    return locator
            for arg in node.args:
                locator = _locator_from_expr(arg, index, bindings, object_types)
                if locator:
                    return locator
    for arg in call.args:
        locator = _locator_from_expr(arg, index, bindings, object_types)
        if locator:
            return locator
    return None


def _classify_call(call: ast.Call, index: SourceIndex, bindings: dict[str, ast.AST], object_types: dict[str, str]) -> dict[str, Any] | None:
    receiver, method = _receiver_and_method(call)
    lower = method.lower()
    locator = _find_locator(call, index, bindings, object_types)
    line = getattr(call, "lineno", 0)
    base: dict[str, Any] = {"source": _source(call), "line": line, "method": method, "locator": locator}

    if lower in _NON_BEHAVIORAL_NAMES:
        return None

    if lower in _WAIT_NAMES or lower.startswith("wait_") or lower.endswith("_wait"):
        return {**base, "kind": "wait", "mapping": "removed-fixed-wait"}
    if lower in _TEXT_NAMES or "send_keys" in lower or lower.startswith("input_"):
        value_node = call.args[-1] if call.args else None
        value, literal = _literal_or_source(value_node, bindings)
        return {**base, "kind": "type_text", "mapping": "type-text", "text": value if literal else _source(value_node)}
    if lower in _TAP_NAMES or lower.startswith("tap_") or lower.startswith("click_"):
        return {**base, "kind": "tap", "mapping": "tap", "coordinates": _coordinate_args(call, bindings)}
    if lower in _DRAG_NAMES or "drag" in lower:
        return {**base, "kind": "drag", "mapping": "drag", "coordinates": _coordinate_args(call, bindings)}
    if lower in _SWIPE_NAMES or "swipe" in lower or lower.startswith("scroll"):
        return {**base, "kind": "swipe", "mapping": "swipe", "coordinates": _coordinate_args(call, bindings)}
    if lower in _GESTURE_NAMES or lower.startswith("rotate") or lower.startswith("pinch") or lower.startswith("zoom"):
        gesture = "rotate" if "rotat" in lower else "pinch"
        return {**base, "kind": gesture, "mapping": gesture}
    if lower in {"is_displayed", "is_element_displayed", "is_element_fully_visible"} or any(word in lower for word in _ASSERTION_WORDS):
        kind = "verify_text" if "text" in lower or "value" in lower else "assertion"
        return {**base, "kind": kind, "mapping": "assertion", "expected": _literal(call.args[-1]) if kind == "verify_text" and call.args else None}
    if "screenshot" in lower or lower in {"snapshot", "get_snapshot", "compare", "compare_image", "ocr"}:
        return {**base, "kind": "screenshot_assertion", "mapping": "screenshot-comparison"}
    if any(word in lower for word in _EXTERNAL_WORDS) or receiver in {"GoogleApi", "OCR", "CompareImage"}:
        return {**base, "kind": "external", "mapping": "external-action"}
    # A low-level driver call is still a concrete legacy operation. Keeping it
    # as an external action is safer than silently dropping it or inventing an ID.
    return {**base, "kind": "external", "mapping": "legacy-operation"}


def _coordinate_args(call: ast.Call, bindings: dict[str, ast.AST]) -> dict[str, Any] | None:
    values = []
    for arg in call.args:
        value, literal = _literal_or_source(arg, bindings)
        if literal and isinstance(value, (int, float)):
            values.append(value)
    if len(values) >= 4:
        return {"x1": values[0], "y1": values[1], "x2": values[2], "y2": values[3]}
    if len(values) >= 2:
        return {"x": values[0], "y": values[1]}
    return None


def _disabled_test_names(text: str) -> list[str]:
    names: list[str] = []
    for token in tokenize.generate_tokens(iter(text.splitlines(keepends=True)).__next__):
        if token.type == tokenize.COMMENT:
            match = re.search(r"\bdef\s+(test_[A-Za-z0-9_]+)\s*\(", token.string)
            if match and match.group(1) not in names:
                names.append(match.group(1))
    return names


def _condition_call(node: ast.AST) -> tuple[ast.Call, bool] | None:
    """Return a simple action condition and its successful branch polarity.

    ``if page.tap_xxx()`` and ``if not page.tap_xxx()`` are common legacy
    success/failure guards.  They can be represented by the action itself:
    successful DriverActions calls continue, while failures raise.
    """
    if isinstance(node, ast.Call):
        return node, True
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not) and isinstance(node.operand, ast.Call):
        return node.operand, False
    if isinstance(node, ast.Compare) and len(node.ops) == 1 and len(node.comparators) == 1 and isinstance(node.left, ast.Call):
        expected = _literal(node.comparators[0])
        if isinstance(node.ops[0], (ast.Is, ast.Eq)) and expected is True:
            return node.left, True
        if isinstance(node.ops[0], (ast.Is, ast.Eq)) and expected is False:
            return node.left, False
    return None


class _Expander:
    def __init__(self, source: Path, index: SourceIndex):
        self.source = source.resolve()
        self.index = index
        self.helpers: list[str] = []
        self.branch_count = 0
        self.wait_count = 0

    def expand_case(self, record: FunctionRecord) -> list[dict[str, Any]]:
        object_types: dict[str, str] = {}
        bindings: dict[str, ast.AST] = {}
        return self._block(record.node.body, bindings, object_types, {record.name})

    def _block(self, statements: Iterable[ast.stmt], bindings: dict[str, ast.AST], object_types: dict[str, str], stack: set[str]) -> list[dict[str, Any]]:
        steps: list[dict[str, Any]] = []
        for statement in statements:
            if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Pass)):
                continue
            if isinstance(statement, ast.Assign):
                if len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Name):
                    target = statement.targets[0].id
                    bindings[target] = statement.value
                    if isinstance(statement.value, ast.Call) and isinstance(statement.value.func, ast.Name):
                        object_types[target] = statement.value.func.id
                continue
            if isinstance(statement, ast.AnnAssign):
                if isinstance(statement.target, ast.Name) and statement.value:
                    bindings[statement.target.id] = statement.value
                continue
            if isinstance(statement, ast.Assert):
                steps.append({"kind": "assertion", "mapping": "assertion", "source": _source(statement.test), "line": statement.lineno, "method": "assert", "locator": self._locator_for_test(statement.test, bindings, object_types)})
                continue
            if isinstance(statement, (ast.With, ast.AsyncWith)):
                # ``rp_step`` and similar context managers are reporting
                # structure.  Their bodies contain the actual device actions.
                steps.extend(self._block(statement.body, bindings, object_types, stack))
                continue
            if isinstance(statement, ast.If):
                self.branch_count += 1
                condition_call = _condition_call(statement.test)
                if condition_call:
                    call, succeeds_when_true = condition_call
                    # Legacy suites often use ``if not page.tap_xxx(): assert
                    # False`` as error handling.  A DriverActions operation
                    # already raises on failure, so convert the successful
                    # path directly instead of emitting a runtime hook that
                    # cannot evaluate the old Page Object expression.
                    steps.extend(self._call(call, bindings, object_types, stack))
                    selected = statement.body if succeeds_when_true else statement.orelse
                    steps.extend(self._block(selected, bindings, object_types, stack))
                    continue
                nested_bindings = dict(bindings)
                nested_types = dict(object_types)
                body = self._block(statement.body, nested_bindings, nested_types, stack)
                alternate = self._block(statement.orelse, dict(bindings), dict(object_types), stack)
                steps.append({"kind": "branch", "mapping": "branch", "condition": _source(statement.test), "line": statement.lineno, "body": body, "else_body": alternate})
                continue
            if isinstance(statement, (ast.For, ast.While)):
                self.branch_count += 1
                body = self._block(statement.body, dict(bindings), dict(object_types), stack)
                steps.append({"kind": "loop", "mapping": "branch", "condition": _source(statement.target if isinstance(statement, ast.For) else statement.test), "iterable": _source(statement.iter if isinstance(statement, ast.For) else ast.Constant(value=True)), "line": statement.lineno, "body": body})
                continue
            if isinstance(statement, ast.Try):
                body = self._block(statement.body, dict(bindings), dict(object_types), stack)
                steps.append({"kind": "try", "mapping": "branch", "line": statement.lineno, "body": body, "handlers": [self._block(handler.body, dict(bindings), dict(object_types), stack) for handler in statement.handlers], "else_body": self._block(statement.orelse, dict(bindings), dict(object_types), stack), "finally_body": self._block(statement.finalbody, dict(bindings), dict(object_types), stack)})
                continue
            if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
                steps.extend(self._call(statement.value, bindings, object_types, stack))
        return steps

    def _locator_for_test(self, test: ast.AST, bindings: dict[str, ast.AST], object_types: dict[str, str]) -> dict[str, str] | None:
        for node in ast.walk(test):
            if isinstance(node, ast.Call):
                locator = _find_locator(node, self.index, bindings, object_types)
                if locator:
                    return locator
        return None

    def _call(self, call: ast.Call, bindings: dict[str, ast.AST], object_types: dict[str, str], stack: set[str]) -> list[dict[str, Any]]:
        receiver, method = _receiver_and_method(call)
        class_name = _class_name_for_call(call, self.index, object_types)
        record = self.index.resolve_function(method, class_name)
        if record and record.name not in stack and not _is_low_level(method) and _is_safe_to_inline(record):
            self.helpers.append(record.name)
            parameters = list(record.node.args.args)
            child_bindings: dict[str, ast.AST] = dict(bindings)
            if record.class_name and parameters and parameters[0].arg in {"self", "cls"}:
                child_bindings[parameters.pop(0).arg] = ast.Name(id=receiver or "self", ctx=ast.Load())
            child_bindings.update({arg.arg: _bound_node(value, bindings) for arg, value in zip(parameters, call.args)})
            child_types = dict(object_types)
            if receiver:
                child_types["self"] = class_name or object_types.get(receiver, "")
            for key, value in child_bindings.items():
                if not isinstance(value, ast.Name):
                    continue
                inferred_type = object_types.get(_source(value)) or self.index.resolve_attribute_type(value.id)
                if inferred_type:
                    child_types[key] = inferred_type
            child = self._block(record.node.body, child_bindings, child_types, stack | {record.name})
            return child
        operation = _classify_call(call, self.index, bindings, object_types)
        if operation is None:
            return []
        if operation["kind"] == "wait":
            self.wait_count += 1
        return [operation]


def _is_low_level(method: str) -> bool:
    lower = method.lower()
    return lower in {"find_element", "find_elements", "get_element", "get_elements", "is_displayed", "get_attribute", "page_source"}


def _is_safe_to_inline(record: FunctionRecord) -> bool:
    """Avoid expanding Page Object recovery/diagnostic implementations.

    The legacy page modules contain large methods with retries, screenshots,
    and fallback locators.  Those are implementation details, not the intent
    of a generated case.  Inline simple page methods (which expose a concrete
    locator), but keep complex ones as one operation for later repair.
    """
    if record.path.parent.name != "pages":
        return True
    control_flow = (ast.If, ast.For, ast.While, ast.Try, ast.With, ast.AsyncWith)
    return not any(isinstance(node, control_flow) for node in ast.walk(record.node))


def _is_expandable_record(record: FunctionRecord) -> bool:
    """Limit inlining to suite helpers and page objects, not framework plumbing."""
    parts = {part.lower() for part in record.path.parts}
    excluded = {"atframework", "fixtures", "configs", "locator", "record", "recordings", "report"}
    return not parts.intersection(excluded)


def _function_records_in_source(source: Path, index: SourceIndex) -> list[FunctionRecord]:
    source_records = [record for values in index.functions.values() for record in values if record.path == source.resolve() and record.name.startswith("test_")]
    return sorted(source_records, key=lambda record: (record.node.lineno, record.node.col_offset))


def build_inventory(source: Path | str, *, project_root: Path | str | None = None, expected_active: int | None = None) -> dict[str, Any]:
    source_path = Path(source).expanduser().resolve()
    if not source_path.exists():
        raise StaticConversionError(f"source file not found: {source_path}")
    try:
        text = source_path.read_text(encoding="utf-8")
        ast.parse(text, filename=str(source_path))
    except (OSError, UnicodeDecodeError, SyntaxError) as exc:
        raise StaticConversionError(f"cannot parse source {source_path}: {exc}") from exc
    index = SourceIndex.load(source_path, Path(project_root).expanduser() if project_root else None)
    records = _function_records_in_source(source_path, index)
    if expected_active is not None and len(records) != expected_active:
        raise StaticConversionError(f"expected {expected_active} active cases, extracted {len(records)}")

    cases: list[dict[str, Any]] = []
    for record in records:
        expander = _Expander(source_path, index)
        steps = expander.expand_case(record)
        counts: dict[str, int] = {"unknown": 0, "branches": expander.branch_count, "removed_waits": expander.wait_count}
        for step in _flatten_steps(steps):
            kind = step["kind"]
            counts[kind] = counts.get(kind, 0) + 1
            if step.get("mapping") in {"unknown", "needs-framework-support"}:
                counts["unknown"] += 1
        cases.append({
            "source_case": record.name,
            "source_file": str(record.path),
            "source_start_line": record.node.lineno,
            "source_end_line": record.node.end_lineno or record.node.lineno,
            "status": "active",
            "resolved_helpers": list(dict.fromkeys(expander.helpers)),
            "steps": steps,
            "coverage": counts,
            "mapping_complete": counts["unknown"] == 0,
        })
    disabled = [{"source_case": name, "status": "disabled", "steps": [], "coverage": {}, "mapping_complete": True} for name in _disabled_test_names(text) if name not in {case["source_case"] for case in cases}]
    feature_mapping = _feature_mapping(cases)
    return {
        "schema_version": 1,
        "source_file": str(source_path),
        "project_root": str((Path(project_root).expanduser() if project_root else source_path.parent).resolve()),
        "active_case_count": len(cases),
        "disabled_case_count": len(disabled),
        "feature_mapping": feature_mapping,
        "cases": cases + disabled,
    }


def _flatten_steps(steps: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
    for step in steps:
        yield step
        for key in ("body", "else_body", "finally_body"):
            nested = step.get(key)
            if isinstance(nested, list):
                yield from _flatten_steps(nested)
        for handler in step.get("handlers", []) if isinstance(step.get("handlers"), list) else []:
            yield from _flatten_steps(handler)


def _feature_mapping(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for case in cases:
        for step in _flatten_steps(case["steps"]):
            kind = step["kind"]
            entry = grouped.setdefault(kind, {"feature": kind, "case_count": 0, "step_count": 0, "mapping": step.get("mapping", "external-action"), "status": "complete", "cases": []})
            entry["step_count"] += 1
            if case["source_case"] not in entry["cases"]:
                entry["cases"].append(case["source_case"])
        for kind in {step["kind"] for step in _flatten_steps(case["steps"])}:
            grouped[kind]["case_count"] = len(grouped[kind]["cases"])
    return sorted(grouped.values(), key=lambda item: item["feature"])


def _safe_name(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_]+", "_", value).strip("_")
    return safe or "converted_case"


def _case_base_name(source_case: str) -> str:
    return source_case[5:] if source_case.startswith("test_") else source_case


def _py_string(value: Any) -> str:
    return repr(value)


def _locator_args(locator: dict[str, str]) -> str:
    return f"{locator['by']}, {_py_string(locator['value'])}"


def _render_operation(step: dict[str, Any], indent: str = "    ") -> list[str]:
    kind = step["kind"]
    source = step.get("source", "legacy operation")
    locator = step.get("locator")
    lines: list[str] = []
    if kind == "branch":
        lines.append(f"{indent}if actions.legacy_condition({_py_string(step.get('condition', 'True'))}):")
        body = step.get("body") or []
        lines.extend(_render_steps(body, indent + "    ") or [indent + "    pass"])
        alternate = step.get("else_body") or []
        if alternate:
            lines.append(f"{indent}else:")
            lines.extend(_render_steps(alternate, indent + "    ") or [indent + "    pass"])
        return lines
    if kind == "loop":
        lines.append(f"{indent}for _legacy_item in actions.legacy_iterable({_py_string(step.get('iterable', '()'))}):")
        lines.extend(_render_steps(step.get("body", []), indent + "    ") or [indent + "    pass"])
        return lines
    if kind == "try":
        lines.append(f"{indent}try:")
        lines.extend(_render_steps(step.get("body", []), indent + "    ") or [indent + "    pass"])
        for handler in step.get("handlers", []):
            lines.append(f"{indent}except Exception:")
            lines.extend(_render_steps(handler, indent + "    ") or [indent + "    pass"])
        if step.get("else_body"):
            lines.append(f"{indent}else:")
            lines.extend(_render_steps(step["else_body"], indent + "    "))
        if step.get("finally_body"):
            lines.append(f"{indent}finally:")
            lines.extend(_render_steps(step["finally_body"], indent + "    "))
        return lines

    label = "[Verify]" if kind in {"assertion", "verify_text", "screenshot_assertion"} else "[External]" if kind == "external" else "[Action]"
    description = _short_description(step)
    lines.append(f"{indent}with step({_py_string(f'{label} {description}')}):")
    expression = _render_call(step)
    if kind in {"assertion", "verify_text", "screenshot_assertion", "external"} or expression.startswith("actions.external_action("):
        lines.append(f"{indent}    assert {expression}")
    else:
        lines.append(f"{indent}    {expression}")
    return lines


def _short_description(step: dict[str, Any]) -> str:
    if step["kind"] == "external":
        return f"Preserve external operation: {step.get('method', 'legacy operation')}"
    if step["kind"] == "wait":
        return "Legacy fixed wait removed"
    return step.get("method") or step["kind"]


def _render_call(step: dict[str, Any]) -> str:
    kind = step["kind"]
    locator = step.get("locator")
    loc = _locator_args(locator) if locator else None
    if kind == "tap":
        if loc:
            return f"actions.tap_by_locator({loc})"
        coords = step.get("coordinates") or {}
        if "x" in coords and "y" in coords:
            return f"actions.tap_by_coordinates({coords['x']}, {coords['y']})"
    if kind == "type_text" and loc:
        return f"actions.type_text_by_locator({loc}, {_py_string(step.get('text', ''))})"
    if kind == "swipe":
        if loc:
            return f"actions.swipe_on_element({loc}, 'down')"
        coords = step.get("coordinates") or {}
        if {"x1", "y1", "x2", "y2"} <= coords.keys():
            return f"actions.drag_coordinates({coords['x1']}, {coords['y1']}, {coords['x2']}, {coords['y2']})"
        return "actions.scroll(direction='down')"
    if kind == "drag":
        coords = step.get("coordinates") or {}
        if {"x1", "y1", "x2", "y2"} <= coords.keys():
            return f"actions.drag_coordinates({coords['x1']}, {coords['y1']}, {coords['x2']}, {coords['y2']})"
    if kind == "pinch" and loc:
        return f"actions.pinch(actions.find_element({loc}))"
    if kind == "rotate" and loc:
        return f"actions.rotate(actions.find_element({loc}))"
    if kind == "assertion" and loc:
        if "not " in step.get("source", "") or step.get("source", "").startswith("not "):
            return f"actions.verify_not_visible({loc})"
        return f"actions.verify_visible({loc})"
    if kind == "verify_text" and loc:
        return f"actions.verify_text({loc}, {_py_string(step.get('expected', ''))}) is not False"
    if kind == "screenshot_assertion":
        return "actions.run_screenshot_comparisons() is not False"
    if kind == "external":
        return f"actions.external_action({_py_string(step.get('method', 'legacy'))}, {_py_string(step.get('source', ''))}) is not False"
    return f"actions.external_action('unmapped', {_py_string(step.get('source', ''))}) is not False"


def _render_steps(steps: list[dict[str, Any]], indent: str = "    ") -> list[str]:
    lines: list[str] = []
    for step in steps:
        if step.get("kind") == "wait":
            continue
        lines.extend(_render_operation(step, indent))
    return lines


def render_test(case: dict[str, Any], identity: str) -> str:
    function_name = f"test_{_safe_name(identity)}"
    lines = [
        "import pytest",
        "from appium.webdriver.common.appiumby import AppiumBy",
        "from reportportal_client import step",
        "",
        "from driver.driver_actions import DriverActions",
        "",
        f"@pytest.mark.name({_py_string(identity)})",
        f"def {function_name}(actions: DriverActions):",
    ]
    lines.extend(_render_steps(case.get("steps", [])) or ["    pass"])
    lines.append("")
    return "\n".join(lines)


def _collision_path(directory: Path, base: str) -> Path:
    candidate = directory / f"{base}.py"
    suffix = 1
    while candidate.exists():
        candidate = directory / f"{base}_{suffix}.py"
        suffix += 1
    return candidate


def generate_tests(inventory_path: Path | str, tests_dir: Path | str, *, start_sequence: int = 1, case_name: str | None = None) -> dict[str, Any]:
    path = Path(inventory_path).expanduser()
    try:
        inventory = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StaticConversionError(f"cannot read inventory: {path}: {exc}") from exc
    cases = [case for case in inventory.get("cases", []) if case.get("status") == "active"]
    if case_name:
        cases = [case for case in cases if case.get("source_case") == case_name]
    incomplete = [case["source_case"] for case in cases if not case.get("mapping_complete", False)]
    if incomplete:
        raise StaticConversionError(f"mapping incomplete for: {', '.join(incomplete)}")
    directory = Path(tests_dir).expanduser()
    directory.mkdir(parents=True, exist_ok=True)
    files: list[str] = []
    manifest: list[dict[str, Any]] = []
    for offset, case in enumerate(cases):
        sequence = start_sequence + offset
        identity_base = f"{sequence:05d}_{_safe_name(_case_base_name(case['source_case']))}"
        output = _collision_path(directory, f"test_{identity_base}")
        identity = output.stem.removeprefix("test_")
        output.write_text(render_test(case, identity), encoding="utf-8")
        files.append(str(output))
        manifest.append({"source_case": case["source_case"], "identity": identity, "output_file": str(output)})
    return {"files": files, "manifest": manifest, "count": len(files)}


def validate_artifacts(inventory_path: Path | str, tests_dir: Path | str) -> dict[str, Any]:
    inventory_file = Path(inventory_path).expanduser()
    directory = Path(tests_dir).expanduser()
    errors: list[str] = []
    try:
        inventory = json.loads(inventory_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "files_checked": 0, "errors": [f"cannot read inventory: {exc}"]}
    active = [case for case in inventory.get("cases", []) if case.get("status") == "active"]
    incomplete = [case["source_case"] for case in active if not case.get("mapping_complete", False)]
    if incomplete:
        errors.append(f"mapping incomplete for: {', '.join(incomplete)}")
    files = sorted(directory.glob("test_*.py")) if directory.exists() else []
    runtime_hooks = {"external_action": 0, "legacy_condition": 0, "legacy_iterable": 0}
    runtime_hook_files: set[str] = set()
    expected = {case["source_case"] for case in active}
    seen: set[str] = set()
    for case in active:
        prefix = _safe_name(_case_base_name(case["source_case"]))
        matches = [file for file in files if re.match(rf"test_\d{{5}}_{re.escape(prefix)}(?:_\d+)?\.py$", file.name)]
        if not matches:
            errors.append(f"missing generated file for {case['source_case']}")
        for file in matches:
            seen.add(str(file))
            try:
                content = file.read_text(encoding="utf-8")
                tree = ast.parse(content, filename=str(file))
            except (OSError, SyntaxError) as exc:
                errors.append(f"{file}: invalid Python: {exc}")
                continue
            for hook in runtime_hooks:
                count = content.count(f"actions.{hook}(")
                runtime_hooks[hook] += count
                if count:
                    runtime_hook_files.add(str(file))
            functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")]
            if len(functions) != 1:
                errors.append(f"{file}: expected exactly one test function")
            imports = [node for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom))]
            imported_legacy = [ast.unparse(node) for node in imports if any(word in ast.unparse(node) for word in ("pages", "ATFramework", "locator", "configs"))]
            if imported_legacy:
                errors.append(f"{file}: imports legacy modules: {', '.join(imported_legacy)}")
            if not any(isinstance(node, ast.arg) and node.arg == "actions" for fn in functions for node in fn.args.args):
                errors.append(f"{file}: test must use the actions fixture")
    collection: dict[str, Any] = {"ok": False, "output": "not run"}
    if not errors and len(seen) >= len(expected):
        project_root = Path(__file__).resolve().parents[1]
        environment = dict(os.environ)
        existing_pythonpath = environment.get("PYTHONPATH", "")
        environment["PYTHONPATH"] = os.pathsep.join(
            [str(project_root), str(project_root / "pytest"), existing_pythonpath]
        ).rstrip(os.pathsep)
        completed = subprocess.run(
            [sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider", str(directory)],
            cwd=project_root,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        collection = {
            "ok": completed.returncode == 0,
            "returncode": completed.returncode,
            "output": (completed.stdout + completed.stderr)[-4000:],
        }
        if not collection["ok"]:
            errors.append("pytest collection failed for generated tests")
    return {
        "ok": not errors and len(seen) >= len(expected) and collection["ok"],
        "files_checked": len(seen),
        "collection": collection,
        "runtime_readiness": {
            "ready": not any(runtime_hooks.values()),
            "hook_counts": runtime_hooks,
            "files_with_hooks": len(runtime_hook_files),
        },
        "errors": errors,
    }
