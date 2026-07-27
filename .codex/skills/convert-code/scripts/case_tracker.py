#!/usr/bin/env python3
"""Extract legacy test methods and maintain a resumable conversion tracker."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import tempfile
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


@contextmanager
def tracker_lock(path: Path):
    """Serialize claims and updates from the main agent and workers."""
    lock_path = path.with_name(f".{path.name}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock_handle:
        try:
            import fcntl
        except ImportError:  # pragma: no cover - macOS/Linux provide fcntl
            yield
            return
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)


def safe_case(case_name: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_]+", "_", case_name).strip("_")
    return value or "recorded_case"


def extract_cases(source: Path, start_case: str) -> list[dict[str, Any]]:
    text = source.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(source))
    lines = text.splitlines(keepends=True)
    methods: list[ast.FunctionDef | ast.AsyncFunctionDef] = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test_"):
            methods.append(node)
    methods.sort(key=lambda node: (node.lineno, node.col_offset))

    start_index = next((index for index, node in enumerate(methods) if node.name == start_case), None)
    if start_index is None:
        available = ", ".join(node.name for node in methods[:10])
        raise SystemExit(f"start case not found: {start_case}; first cases: {available}")

    cases: list[dict[str, Any]] = []
    for index, node in enumerate(methods[start_index:], start=1):
        end_line = node.end_lineno or node.lineno
        source_text = "".join(lines[node.lineno - 1 : end_line])
        cases.append(
            {
                "index": index,
                "source_case": node.name,
                "source_start_line": node.lineno,
                "source_end_line": end_line,
                "source_sha256": hashlib.sha256(source_text.encode("utf-8")).hexdigest(),
                "source_text": source_text,
                "status": "pending",
                "worker_id": None,
                "lease_id": None,
                "assigned_at": None,
                "output_case": None,
                "output_file": None,
                "scratchpad": None,
                "report": None,
                "pytest": {"result": "pending", "attempts": 0, "fail_point": None},
                "notes": "",
                "updated_at": None,
            }
        )
    return cases


def cmd_extract(args: argparse.Namespace) -> None:
    source = Path(args.source).expanduser().resolve()
    cases = extract_cases(source, args.start_case)
    tracker = {
        "schema_version": 1,
        "created_at": now(),
        "updated_at": now(),
        "source_file": str(source),
        "start_case": args.start_case,
        "expected_count": args.expected_count,
        "extracted_count": len(cases),
        "count_matches": args.expected_count == len(cases),
        "count_note": None if args.expected_count == len(cases) else "Requested count differs from source extraction; stop before recording.",
        "cases": cases,
    }
    output = Path(args.output).expanduser()
    if output.exists() and not args.force:
        raise SystemExit(f"refusing to overwrite tracker: {output}; use --force only to start a new run")
    atomic_write(output, tracker)
    print(json.dumps({"ok": True, "output": str(output), "expected_count": args.expected_count, "extracted_count": len(cases), "count_matches": tracker["count_matches"]}, ensure_ascii=False, indent=2))


def find_case(tracker: dict[str, Any], name: str) -> dict[str, Any]:
    for case in tracker["cases"]:
        if case["source_case"] == name or case.get("output_case") == name:
            return case
    raise SystemExit(f"case not found: {name}")


def cmd_next(args: argparse.Namespace) -> None:
    tracker = read_json(Path(args.input).expanduser())
    pending = next((case for case in tracker["cases"] if case["status"] not in {"passed", "failed", "blocked"}), None)
    print(json.dumps(pending or {"message": "all cases are terminal"}, ensure_ascii=False, indent=2))


def cmd_claim(args: argparse.Namespace) -> None:
    path = Path(args.input).expanduser()
    with tracker_lock(path):
        tracker = read_json(path)
        if args.case:
            case = find_case(tracker, args.case)
        else:
            case = next((item for item in tracker["cases"] if item["status"] == "pending"), None)
            if case is None:
                raise SystemExit("no pending case available")
        if case["status"] != "pending":
            raise SystemExit(f"case is not pending: {case['source_case']} ({case['status']})")
        case["status"] = "assigned"
        case["worker_id"] = args.worker_id
        case["lease_id"] = uuid.uuid4().hex[:16]
        case["assigned_at"] = now()
        case["updated_at"] = now()
        tracker["updated_at"] = now()
        atomic_write(path, tracker)
    print(json.dumps({"ok": True, "case": case}, ensure_ascii=False, indent=2))


def cmd_summary(args: argparse.Namespace) -> None:
    tracker = read_json(Path(args.input).expanduser())
    counts: dict[str, int] = {}
    for case in tracker["cases"]:
        counts[case["status"]] = counts.get(case["status"], 0) + 1
    print(json.dumps({"source_file": tracker["source_file"], "expected_count": tracker["expected_count"], "extracted_count": tracker["extracted_count"], "count_matches": tracker["count_matches"], "statuses": counts}, ensure_ascii=False, indent=2))


def cmd_update(args: argparse.Namespace) -> None:
    path = Path(args.input).expanduser()
    with tracker_lock(path):
        tracker = read_json(path)
        case = find_case(tracker, args.case)
        if args.worker_id and case.get("worker_id") != args.worker_id:
            raise SystemExit(f"worker lease mismatch for {case['source_case']}")
        case["status"] = args.status
        case["updated_at"] = now()
        if args.output_case is not None:
            case["output_case"] = args.output_case
        if args.output_file is not None:
            case["output_file"] = args.output_file
        if args.scratchpad is not None:
            case["scratchpad"] = args.scratchpad
        if args.report is not None:
            case["report"] = args.report
        if args.result is not None:
            case["pytest"]["result"] = args.result
        if args.attempts is not None:
            case["pytest"]["attempts"] = args.attempts
        if args.fail_point is not None:
            case["pytest"]["fail_point"] = args.fail_point
        if args.notes is not None:
            case["notes"] = args.notes
        tracker["updated_at"] = now()
        atomic_write(path, tracker)
    print(json.dumps({"ok": True, "case": case}, ensure_ascii=False, indent=2))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)

    extract = sub.add_parser("extract")
    extract.add_argument("--source", required=True)
    extract.add_argument("--start-case", required=True)
    extract.add_argument("--expected-count", type=int, default=189)
    extract.add_argument("--output", required=True)
    extract.add_argument("--force", action="store_true")
    extract.set_defaults(func=cmd_extract)

    for name, function in (("next", cmd_next), ("summary", cmd_summary)):
        command = sub.add_parser(name)
        command.add_argument("--input", required=True)
        command.set_defaults(func=function)

    claim = sub.add_parser("claim")
    claim.add_argument("--input", required=True)
    claim.add_argument("--case")
    claim.add_argument("--worker-id", required=True)
    claim.set_defaults(func=cmd_claim)

    update = sub.add_parser("update")
    update.add_argument("--input", required=True)
    update.add_argument("--case", required=True)
    update.add_argument("--status", required=True, choices=["pending", "assigned", "recording", "validating", "generated", "running", "passed", "failed", "blocked"])
    update.add_argument("--worker-id")
    update.add_argument("--output-case")
    update.add_argument("--output-file")
    update.add_argument("--scratchpad")
    update.add_argument("--report")
    update.add_argument("--result")
    update.add_argument("--attempts", type=int)
    update.add_argument("--fail-point")
    update.add_argument("--notes")
    update.set_defaults(func=cmd_update)
    return root


if __name__ == "__main__":
    arguments = parser().parse_args()
    arguments.func(arguments)
