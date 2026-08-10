"""Guard test for the DriverActions return-value contract.

Generated tests wrap nearly every call in `assert actions.<method>(...)`, so a
public method that falls through and returns ``None`` turns into an
``AssertionError: assert None`` even when the gesture succeeded on the device.
That is exactly how ``test_00006_main_03_01_06_2_1`` failed: it asserted
``type_text_by_locator``, which typed the text correctly but returned ``None``.

The contract
------------
Every public ``DriverActions`` method returns a **truthy** value on success and
**raises** on failure.  Return something meaningful where one exists (the
``WebElement``, the saved path, a real bool); fall back to ``True`` only when
the method genuinely has nothing to hand back.

Methods that deliberately return ``Optional[...]`` opt out via
``OPTIONAL_RETURN_METHODS`` below — a decision that must be explicit, because a
silent ``None`` breaks callers that branch on the result.

The check is pure AST parsing of the source file, so it needs neither Appium nor
a device.
"""

import ast
from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

DRIVER_ACTIONS = (
    Path(__file__).resolve().parents[1] / "pytest" / "driver" / "driver_actions.py"
)

# Public methods allowed to return None, with the reason they need to.
OPTIONAL_RETURN_METHODS = {
    "get_element": (
        "Non-throwing lookup; tests branch on `if actions.get_element(...)` and "
        "on `is not None`, so absence must stay falsy."
    ),
}


# ── AST helpers ────────────────────────────────────────────────────────────────

def _is_none_literal(node) -> bool:
    return node is None or (isinstance(node, ast.Constant) and node.value is None)


def _always_returns(body) -> bool:
    """True when every path through *body* ends in `return <value>` or `raise`."""
    for stmt in body:
        if isinstance(stmt, ast.Return):
            return not _is_none_literal(stmt.value)
        if isinstance(stmt, ast.Raise):
            return True
        if isinstance(stmt, ast.If):
            if stmt.orelse and _always_returns(stmt.body) and _always_returns(stmt.orelse):
                return True
        elif isinstance(stmt, ast.Try):
            if stmt.finalbody and _always_returns(stmt.finalbody):
                return True
            main = _always_returns(stmt.orelse) if stmt.orelse else _always_returns(stmt.body)
            if main and stmt.handlers and all(_always_returns(h.body) for h in stmt.handlers):
                return True
        elif isinstance(stmt, ast.With):
            if _always_returns(stmt.body):
                return True
        elif isinstance(stmt, ast.While):
            # `while True:` with no break can only be left via return/raise.
            if isinstance(stmt.test, ast.Constant) and stmt.test.value is True:
                if not any(isinstance(n, ast.Break) for n in ast.walk(stmt)):
                    return True
    return False


def _bare_return_lines(fn) -> list:
    """Lines holding a `return` / `return None` inside *fn*."""
    return [
        node.lineno
        for node in ast.walk(fn)
        if isinstance(node, ast.Return) and _is_none_literal(node.value)
    ]


def _public_methods():
    tree = ast.parse(DRIVER_ACTIONS.read_text())
    cls = next(
        n for n in tree.body
        if isinstance(n, ast.ClassDef) and n.name == "DriverActions"
    )
    return [
        fn for fn in cls.body
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not fn.name.startswith("_")
    ]


# ── Tests ──────────────────────────────────────────────────────────────────────

def test_public_methods_never_return_none():
    """No public method may hand `None` back to `assert actions.<method>(...)`."""
    offenders = []
    for fn in _public_methods():
        if fn.name in OPTIONAL_RETURN_METHODS:
            continue
        reasons = []
        if not _always_returns(fn.body):
            reasons.append("falls through without returning a value")
        bare = _bare_return_lines(fn)
        if bare:
            reasons.append(f"bare `return` at line(s) {', '.join(map(str, bare))}")
        if reasons:
            offenders.append(f"  {fn.name} (line {fn.lineno}): {'; '.join(reasons)}")

    assert not offenders, (
        "These DriverActions methods can return None, so "
        "`assert actions.<method>(...)` fails even when the action succeeded.\n"
        "Return a meaningful truthy value (element / path / bool), or `True` when "
        "there is nothing to return.\n"
        "If None is genuinely part of the contract, add the method to "
        "OPTIONAL_RETURN_METHODS with a reason.\n\n" + "\n".join(offenders)
    )


def test_public_methods_are_not_annotated_none():
    """`-> None` on a public method contradicts the contract."""
    offenders = [
        f"  {fn.name} (line {fn.lineno})"
        for fn in _public_methods()
        if fn.name not in OPTIONAL_RETURN_METHODS
        and fn.returns is not None
        and _is_none_literal(fn.returns)
    ]
    assert not offenders, (
        "These public DriverActions methods are annotated `-> None` but must "
        "return a truthy value:\n" + "\n".join(offenders)
    )


def test_optional_return_allowlist_is_accurate():
    """Every allowlisted name must exist and must actually be able to return None."""
    by_name = {fn.name: fn for fn in _public_methods()}
    for name, reason in OPTIONAL_RETURN_METHODS.items():
        assert name in by_name, (
            f"OPTIONAL_RETURN_METHODS lists {name!r}, which is not a public "
            f"DriverActions method — remove the stale entry."
        )
        fn = by_name[name]
        can_be_none = not _always_returns(fn.body) or bool(_bare_return_lines(fn))
        assert can_be_none, (
            f"{name} no longer returns None, so it should be removed from "
            f"OPTIONAL_RETURN_METHODS."
        )
        assert reason.strip(), f"{name} needs a reason in OPTIONAL_RETURN_METHODS."
