"""Command-line interface for AI-friendly recorder workflows.

This module intentionally keeps command I/O JSON-only so it can be safely
invoked by automation agents.

Examples:
    python -m app.cli validate-steps --input steps.json
    python -m app.cli generate-test --input steps.json --case-name Demo --output pytest/tests/test_demo.py
    python -m app.cli export-bundle --input steps.json --case-name Demo
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import httpx

from .codegen import generate_script

_WARN_QUALITIES = frozenset({"id_indexed", "id_eq_label", "label_only", "xpath_only"})
_STRIP_STEP_KEYS = frozenset({"pre_screenshot", "pre_screenshot_size"})
_KNOWN_ACTIONS = frozenset(
    {
        "tap",
        "double_tap",
        "triple_tap",
        "five_tap",
        "long_press",
        "two_finger_tap",
        "multi_finger_tap",
        "pinch",
        "rotate",
        "scroll",
        "swipe",
        "drag",
        "long_press_drag",
        "paint",
        "type_text",
        "home",
        "launch_app",
        "terminate_app",
        "verify_visible",
        "verify_not_visible",
        "verify_get_text",
        "verify_screenshot_gt",
        "verify_screenshot_diff",
        "verify_tap_screenshot_diff",
    }
)

_RECORD_ENDPOINT_BY_ACTION = {
    "tap": "/api/record",
    "double_tap": "/api/record/double_tap",
    "triple_tap": "/api/record/triple_tap",
    "five_tap": "/api/record/five_tap",
    "long_press": "/api/record/long_press",
    "two_finger_tap": "/api/record/two_finger_tap",
    "multi_finger_tap": "/api/record/multi_finger_tap",
    "pinch": "/api/record/pinch",
    "rotate": "/api/record/rotate",
    "scroll": "/api/record/scroll",
    "swipe": "/api/record/swipe",
    "drag": "/api/record/drag",
    "long_press_drag": "/api/record/long_press_drag",
    "paint": "/api/record/paint",
    "type_text": "/api/record/type_text",
    "home": "/api/record/home",
    "launch_app": "/api/record/launch_app",
    "terminate_app": "/api/record/terminate_app",
    "verify_visible": "/api/record/verify_visible",
    "verify_get_text": "/api/record/verify_get_text",
    "verify_screenshot_gt": "/api/record/verify_screenshot_gt",
    "verify_screenshot_diff": "/api/record/verify_screenshot_diff",
    "verify_tap_screenshot_diff": "/api/record/verify_tap_screenshot_diff",
    "scroll_target": "/api/record/scroll_target",
    "swipe_target": "/api/record/swipe_target",
}

_LIVE_ENDPOINT_BY_ACTION = {
    "tap": "/api/tap",
    "double_tap": "/api/double_tap",
    "triple_tap": "/api/triple_tap",
    "five_tap": "/api/five_tap",
    "long_press": "/api/long_press",
    "two_finger_tap": "/api/two_finger_tap",
    "multi_finger_tap": "/api/multi_finger_tap",
    "pinch": "/api/pinch",
    "rotate": "/api/rotate",
    "scroll": "/api/scroll",
    "swipe": "/api/swipe",
    "drag": "/api/drag",
    "long_press_drag": "/api/long_press_drag",
    "paint": "/api/paint",
    "type_text": "/api/type_text",
    "home": "/api/home",
    "launch_app": "/api/launch_app",
    "terminate_app": "/api/terminate_app",
}


def _safe_name(name: str) -> str:
    safe = "".join(c if c.isalnum() or c == "_" else "_" for c in (name or ""))
    safe = safe.strip("_")
    return safe or "recorded_case"


def _ok(command: str, **kwargs: Any) -> dict[str, Any]:
    payload = {"ok": True, "command": command}
    payload.update(kwargs)
    return payload


def _err(command: str, code: str, message: str, details: Any | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "ok": False,
        "command": command,
        "error": {"code": code, "message": message},
    }
    if details is not None:
        payload["error"]["details"] = details
    return payload


def _load_steps_input(path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return raw, {}
    if isinstance(raw, dict) and isinstance(raw.get("steps"), list):
        return raw["steps"], raw
    raise ValueError("input JSON must be a step list or an object with a 'steps' array")


def _load_json_from_args(payload_json: str, payload_file: str) -> dict[str, Any]:
    if payload_json and payload_file:
        raise ValueError("use either --payload-json or --payload-file, not both")
    if payload_json:
        data = json.loads(payload_json)
    elif payload_file:
        data = json.loads(Path(payload_file).read_text(encoding="utf-8"))
    else:
        data = {}
    if not isinstance(data, dict):
        raise ValueError("payload must be a JSON object")
    return data


def _http_json(
    *,
    base_url: str,
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
    timeout: float = 30.0,
) -> tuple[int, dict[str, Any]]:
    try:
        with httpx.Client(base_url=base_url, timeout=timeout) as client:
            if method == "GET":
                resp = client.get(path)
            elif method == "POST":
                resp = client.post(path, json=payload or {})
            elif method == "DELETE":
                resp = client.delete(path)
            else:
                return 2, _err("http", "INVALID_METHOD", f"unsupported method: {method}")
    except httpx.RequestError as exc:
        return 4, _err("http", "REQUEST_FAILED", "failed to reach recorder server", str(exc))

    try:
        body = resp.json()
    except ValueError:
        body = {"raw": resp.text}

    if resp.status_code >= 400:
        return 4, _err(
            "http",
            "HTTP_ERROR",
            f"recorder server returned status {resp.status_code}",
            {"status_code": resp.status_code, "response": body},
        )
    return 0, _ok("http", status_code=resp.status_code, response=body)


def _resolve_action_endpoint(action: str, mode: str) -> str | None:
    if mode == "record":
        return _RECORD_ENDPOINT_BY_ACTION.get(action)
    if mode == "live":
        return _LIVE_ENDPOINT_BY_ACTION.get(action)
    return None


def _run_action_request(
    *,
    base_url: str,
    timeout: float,
    action: str,
    mode: str,
    payload: dict[str, Any],
) -> tuple[int, dict[str, Any]]:
    endpoint = _resolve_action_endpoint(action, mode)
    if not endpoint:
        return 2, _err("vision", "INVALID_ACTION", f"action '{action}' is not supported in mode '{mode}'")

    code, res = _http_json(
        base_url=base_url,
        method="POST",
        path=endpoint,
        payload=payload,
        timeout=timeout,
    )
    if code != 0:
        return code, _err("vision", res["error"]["code"], res["error"]["message"], res["error"].get("details"))

    return 0, _ok(
        "vision-action",
        base_url=base_url,
        action=action,
        mode=mode,
        endpoint=endpoint,
        request_payload=payload,
        response=res["response"],
    )


def _collect_vision_snapshot(
    *,
    base_url: str,
    timeout: float,
    include_tree: bool,
    include_frame: bool,
    include_frame_data: bool,
    tree_fresh: bool,
) -> tuple[int, dict[str, Any]]:
    snapshot: dict[str, Any] = {"captured_at": time.strftime("%Y-%m-%dT%H:%M:%S")}

    code, status_payload = _http_json(base_url=base_url, method="GET", path="/api/status", timeout=timeout)
    if code != 0:
        return code, _err("server-vision-snapshot", status_payload["error"]["code"], status_payload["error"]["message"], status_payload["error"].get("details"))
    snapshot["status"] = status_payload["response"]

    if include_tree:
        tree_path = "/api/tree?fresh=true" if tree_fresh else "/api/tree"
        code, tree_payload = _http_json(base_url=base_url, method="GET", path=tree_path, timeout=timeout)
        if code != 0:
            return code, _err("server-vision-snapshot", tree_payload["error"]["code"], tree_payload["error"]["message"], tree_payload["error"].get("details"))
        snapshot["tree"] = tree_payload["response"]

    if include_frame:
        frame_path = "/api/frame" if include_frame_data else "/api/frame?include_data=false"
        code, frame_payload = _http_json(base_url=base_url, method="GET", path=frame_path, timeout=timeout)
        if code != 0:
            return code, _err("server-vision-snapshot", frame_payload["error"]["code"], frame_payload["error"]["message"], frame_payload["error"].get("details"))
        snapshot["frame"] = frame_payload["response"]

    return 0, _ok("server-vision-snapshot", base_url=base_url, snapshot=snapshot)


def _load_plan_file(path: Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("vision plan must be a JSON object")
    steps = raw.get("steps")
    if not isinstance(steps, list):
        raise ValueError("vision plan requires a 'steps' array")
    return raw


def _validate_steps(steps: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    for idx, step in enumerate(steps, start=1):
        loc = {"step": idx}
        if not isinstance(step, dict):
            errors.append({**loc, "field": "step", "message": "step must be an object"})
            continue

        action = step.get("action")
        if not isinstance(action, str) or not action.strip():
            errors.append({**loc, "field": "action", "message": "action is required"})
        elif action not in _KNOWN_ACTIONS:
            errors.append({**loc, "field": "action", "message": f"unknown action: {action}"})

        target = step.get("target")
        if target is not None:
            if not isinstance(target, dict):
                errors.append({**loc, "field": "target", "message": "target must be an object when present"})
            else:
                target_type = target.get("type")
                if not isinstance(target_type, str) or not target_type:
                    errors.append({**loc, "field": "target.type", "message": "target.type is required when target exists"})
                if target_type != "coordinate":
                    target_value = target.get("value")
                    if not isinstance(target_value, str) or not target_value:
                        errors.append({**loc, "field": "target.value", "message": "target.value is required for non-coordinate targets"})

                sq = target.get("selector_quality")
                if isinstance(sq, str) and sq in _WARN_QUALITIES:
                    warnings.append(
                        {
                            **loc,
                            "field": "target.selector_quality",
                            "message": f"fragile selector quality: {sq}",
                        }
                    )

        # Lightweight action-specific checks to keep CLI strict but practical.
        if action in {"scroll", "swipe", "drag", "long_press_drag"}:
            coords = step.get("coords")
            if not isinstance(coords, dict):
                warnings.append({**loc, "field": "coords", "message": "coords missing; codegen may use fallback behavior"})
            else:
                for key in ("x1", "y1", "x2", "y2"):
                    if key not in coords:
                        warnings.append({**loc, "field": f"coords.{key}", "message": f"{key} missing"})

        if action == "type_text" and "text" not in step:
            warnings.append({**loc, "field": "text", "message": "text missing for type_text action"})

    return errors, warnings


def _strip_step_for_json(step: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in step.items() if k not in _STRIP_STEP_KEYS}


def _render_selector_report_html(steps: list[dict[str, Any]], case_name: str, exported_at: str) -> str:
    rows: list[str] = []
    warning_count = 0
    for i, step in enumerate(steps, start=1):
        target = step.get("target") if isinstance(step, dict) else None
        quality = target.get("selector_quality") if isinstance(target, dict) else ""
        warn = isinstance(quality, str) and quality in _WARN_QUALITIES
        if warn:
            warning_count += 1
        target_type = target.get("type", "") if isinstance(target, dict) else ""
        target_value = target.get("value", "") if isinstance(target, dict) else ""
        badge = "warn" if warn else "ok"
        rows.append(
            "<tr>"
            f"<td>{i}</td>"
            f"<td>{step.get('action', '')}</td>"
            f"<td>{target_type}</td>"
            f"<td><code>{target_value}</code></td>"
            f"<td class='{badge}'>{quality or '-'}</td>"
            "</tr>"
        )

    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <title>Selector Quality Report - {case_name}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 24px; background: #121212; color: #e5e5e5; }}
    h1 {{ margin-bottom: 4px; }}
    .meta {{ color: #b3b3b3; margin-bottom: 16px; }}
    .summary {{ margin-bottom: 16px; font-weight: 600; }}
    table {{ width: 100%; border-collapse: collapse; background: #1a1a1a; }}
    th, td {{ border: 1px solid #2a2a2a; padding: 8px; text-align: left; font-size: 13px; }}
    th {{ background: #202020; }}
    .warn {{ color: #ffb020; font-weight: 700; }}
    .ok {{ color: #8ad66d; }}
    code {{ color: #b0d7ff; }}
  </style>
</head>
<body>
  <h1>Selector Quality Report</h1>
  <div class=\"meta\">Case: <strong>{case_name}</strong> | Exported: {exported_at}</div>
  <div class=\"summary\">Warnings: {warning_count} / {len(steps)}</div>
  <table>
    <thead>
      <tr><th>#</th><th>Action</th><th>Target Type</th><th>Target Value</th><th>Selector Quality</th></tr>
    </thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>
</body>
</html>
"""


def cmd_validate_steps(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    try:
        steps, payload = _load_steps_input(Path(args.input))
    except FileNotFoundError:
        return 3, _err("validate-steps", "FILE_NOT_FOUND", f"input file not found: {args.input}")
    except json.JSONDecodeError as exc:
        return 3, _err("validate-steps", "INVALID_JSON", "failed to parse input JSON", str(exc))
    except ValueError as exc:
        return 2, _err("validate-steps", "INVALID_INPUT", str(exc))

    errors, warnings = _validate_steps(steps)
    if errors:
        return 2, _err(
            "validate-steps",
            "STEP_VALIDATION_FAILED",
            "step validation failed",
            {"errors": errors, "warnings": warnings},
        )

    case_name = args.case_name or payload.get("case_name") or "recorded_case"
    return 0, _ok(
        "validate-steps",
        case_name=case_name,
        step_count=len(steps),
        warning_count=len(warnings),
        warnings=warnings,
    )


def cmd_generate_test(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    try:
        steps, payload = _load_steps_input(Path(args.input))
    except FileNotFoundError:
        return 3, _err("generate-test", "FILE_NOT_FOUND", f"input file not found: {args.input}")
    except json.JSONDecodeError as exc:
        return 3, _err("generate-test", "INVALID_JSON", "failed to parse input JSON", str(exc))
    except ValueError as exc:
        return 2, _err("generate-test", "INVALID_INPUT", str(exc))

    errors, warnings = _validate_steps(steps)
    if errors:
        return 2, _err("generate-test", "STEP_VALIDATION_FAILED", "step validation failed", {"errors": errors})

    case_name = args.case_name or payload.get("case_name") or "recorded_case"
    script = generate_script(steps, case_name)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(script, encoding="utf-8")

    return 0, _ok(
        "generate-test",
        case_name=case_name,
        output_path=str(output_path),
        step_count=len(steps),
        warning_count=len(warnings),
    )


def cmd_export_bundle(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    try:
        steps, payload = _load_steps_input(Path(args.input))
    except FileNotFoundError:
        return 3, _err("export-bundle", "FILE_NOT_FOUND", f"input file not found: {args.input}")
    except json.JSONDecodeError as exc:
        return 3, _err("export-bundle", "INVALID_JSON", "failed to parse input JSON", str(exc))
    except ValueError as exc:
        return 2, _err("export-bundle", "INVALID_INPUT", str(exc))

    errors, warnings = _validate_steps(steps)
    if errors:
        return 2, _err("export-bundle", "STEP_VALIDATION_FAILED", "step validation failed", {"errors": errors})

    base_name = args.case_name or payload.get("case_name") or "recorded_case"
    stamped_name = f"{base_name}_{time.strftime('%Y%m%d_%H%M%S')}" if args.append_timestamp else base_name
    safe = _safe_name(stamped_name)
    py_filename = f"test_{safe}.py"
    json_filename = f"{safe}.json"
    html_filename = f"{safe}.html"

    export_root = Path(args.export_dir)
    tests_root = Path(args.tests_dir)
    export_dir = export_root / safe
    export_dir.mkdir(parents=True, exist_ok=True)
    tests_root.mkdir(parents=True, exist_ok=True)

    script = generate_script(steps, stamped_name)
    exported_at = time.strftime("%Y-%m-%dT%H:%M:%S")
    steps_payload = {
        "case_name": stamped_name,
        "exported_at": exported_at,
        "steps": [_strip_step_for_json(s) for s in steps],
    }

    py_export = export_dir / py_filename
    py_tests = tests_root / py_filename
    json_export = export_dir / json_filename
    html_export = export_dir / html_filename

    py_export.write_text(script, encoding="utf-8")
    py_tests.write_text(script, encoding="utf-8")
    json_export.write_text(json.dumps(steps_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    html_export.write_text(_render_selector_report_html(steps, stamped_name, exported_at), encoding="utf-8")

    return 0, _ok(
        "export-bundle",
        case_name=stamped_name,
        step_count=len(steps),
        warning_count=len(warnings),
        saved_paths=[str(py_tests), str(py_export), str(json_export), str(html_export)],
    )


def cmd_server_status(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    code, payload = _http_json(base_url=args.base_url, method="GET", path="/api/status", timeout=args.timeout)
    if code != 0:
        return code, _err("server-status", payload["error"]["code"], payload["error"]["message"], payload["error"].get("details"))
    return 0, _ok("server-status", base_url=args.base_url, response=payload["response"])


def cmd_server_set_config(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    code, payload = _http_json(
        base_url=args.base_url,
        method="POST",
        path="/api/config",
        payload={"wda_url": args.wda_url},
        timeout=args.timeout,
    )
    if code != 0:
        return code, _err("server-set-config", payload["error"]["code"], payload["error"]["message"], payload["error"].get("details"))
    return 0, _ok("server-set-config", base_url=args.base_url, wda_url=args.wda_url, response=payload["response"])


def cmd_server_steps_get(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    code, payload = _http_json(base_url=args.base_url, method="GET", path="/api/steps", timeout=args.timeout)
    if code != 0:
        return code, _err("server-steps-get", payload["error"]["code"], payload["error"]["message"], payload["error"].get("details"))
    response = payload["response"]
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0, _ok(
        "server-steps-get",
        base_url=args.base_url,
        step_count=len(response.get("steps", [])) if isinstance(response, dict) else None,
        output_path=args.output or "",
        response=response,
    )


def cmd_server_steps_clear(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    code, payload = _http_json(base_url=args.base_url, method="DELETE", path="/api/steps", timeout=args.timeout)
    if code != 0:
        return code, _err("server-steps-clear", payload["error"]["code"], payload["error"]["message"], payload["error"].get("details"))
    return 0, _ok("server-steps-clear", base_url=args.base_url, response=payload["response"])


def cmd_server_record_action(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    try:
        payload = _load_json_from_args(args.payload_json, args.payload_file)
    except FileNotFoundError:
        return 3, _err("server-record-action", "FILE_NOT_FOUND", f"payload file not found: {args.payload_file}")
    except json.JSONDecodeError as exc:
        return 3, _err("server-record-action", "INVALID_JSON", "failed to parse payload JSON", str(exc))
    except ValueError as exc:
        return 2, _err("server-record-action", "INVALID_INPUT", str(exc))

    code, res = _run_action_request(
        base_url=args.base_url,
        timeout=args.timeout,
        action=args.action,
        mode=args.mode,
        payload=payload,
    )
    if code != 0:
        return code, _err("server-record-action", res["error"]["code"], res["error"]["message"], res["error"].get("details"))
    return 0, _ok(
        "server-record-action",
        base_url=args.base_url,
        action=args.action,
        mode=args.mode,
        endpoint=res["endpoint"],
        request_payload=payload,
        response=res["response"],
    )


def cmd_server_export(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    code, payload = _http_json(
        base_url=args.base_url,
        method="POST",
        path="/api/export",
        payload={"case_name": args.case_name},
        timeout=args.timeout,
    )
    if code != 0:
        return code, _err("server-export", payload["error"]["code"], payload["error"]["message"], payload["error"].get("details"))
    response = payload["response"]
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0, _ok(
        "server-export",
        base_url=args.base_url,
        case_name=args.case_name,
        output_path=args.output or "",
        response=response,
    )


def cmd_server_vision_snapshot(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    code, payload = _collect_vision_snapshot(
        base_url=args.base_url,
        timeout=args.timeout,
        include_tree=args.include_tree,
        include_frame=args.include_frame,
        include_frame_data=args.include_frame_data,
        tree_fresh=args.tree_fresh,
    )
    if code != 0:
        return code, payload

    snapshot = payload["snapshot"]
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    tree_count = None
    if isinstance(snapshot.get("tree"), dict):
        tree_count = len(snapshot["tree"].get("elements", []))

    return 0, _ok(
        "server-vision-snapshot",
        base_url=args.base_url,
        output_path=args.output or "",
        has_tree="tree" in snapshot,
        has_frame="frame" in snapshot,
        tree_element_count=tree_count,
        snapshot=snapshot,
    )


def cmd_server_vision_execute(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    try:
        payload = _load_json_from_args(args.payload_json, args.payload_file)
    except FileNotFoundError:
        return 3, _err("server-vision-execute", "FILE_NOT_FOUND", f"payload file not found: {args.payload_file}")
    except json.JSONDecodeError as exc:
        return 3, _err("server-vision-execute", "INVALID_JSON", "failed to parse payload JSON", str(exc))
    except ValueError as exc:
        return 2, _err("server-vision-execute", "INVALID_INPUT", str(exc))

    code, res = _run_action_request(
        base_url=args.base_url,
        timeout=args.timeout,
        action=args.action,
        mode=args.mode,
        payload=payload,
    )
    if code != 0:
        return code, _err("server-vision-execute", res["error"]["code"], res["error"]["message"], res["error"].get("details"))

    return 0, _ok(
        "server-vision-execute",
        base_url=args.base_url,
        action=args.action,
        mode=args.mode,
        endpoint=res["endpoint"],
        request_payload=payload,
        response=res["response"],
    )


def cmd_server_vision_loop(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    try:
        plan = _load_plan_file(Path(args.plan_file))
    except FileNotFoundError:
        return 3, _err("server-vision-loop", "FILE_NOT_FOUND", f"plan file not found: {args.plan_file}")
    except json.JSONDecodeError as exc:
        return 3, _err("server-vision-loop", "INVALID_JSON", "failed to parse plan JSON", str(exc))
    except ValueError as exc:
        return 2, _err("server-vision-loop", "INVALID_INPUT", str(exc))

    results: list[dict[str, Any]] = []
    steps = plan.get("steps", [])
    base_url = plan.get("base_url", args.base_url)
    timeout = float(plan.get("timeout", args.timeout))

    for i, step in enumerate(steps, start=1):
        if not isinstance(step, dict):
            return 2, _err("server-vision-loop", "INVALID_PLAN", f"step {i} must be an object")

        step_type = step.get("type")
        if step_type == "snapshot":
            code, payload = _collect_vision_snapshot(
                base_url=base_url,
                timeout=timeout,
                include_tree=bool(step.get("include_tree", True)),
                include_frame=bool(step.get("include_frame", True)),
                include_frame_data=bool(step.get("include_frame_data", False)),
                tree_fresh=bool(step.get("tree_fresh", False)),
            )
            if code != 0:
                return code, _err("server-vision-loop", payload["error"]["code"], f"step {i} snapshot failed", payload["error"].get("details"))
            results.append({"step": i, "type": "snapshot", "result": payload["snapshot"]})
            continue

        if step_type == "action":
            action = step.get("action")
            mode = step.get("mode", "record")
            payload = step.get("payload", {})
            if not isinstance(payload, dict):
                return 2, _err("server-vision-loop", "INVALID_PLAN", f"step {i} payload must be an object")

            code, res = _run_action_request(
                base_url=base_url,
                timeout=timeout,
                action=str(action),
                mode=str(mode),
                payload=payload,
            )
            if code != 0:
                return code, _err("server-vision-loop", res["error"]["code"], f"step {i} action failed", res["error"].get("details"))
            results.append(
                {
                    "step": i,
                    "type": "action",
                    "action": action,
                    "mode": mode,
                    "endpoint": res["endpoint"],
                    "response": res["response"],
                }
            )
            continue

        return 2, _err("server-vision-loop", "INVALID_PLAN", f"step {i} type must be 'snapshot' or 'action'")

    out_payload = {
        "base_url": base_url,
        "timeout": timeout,
        "plan_step_count": len(steps),
        "results": results,
    }
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(out_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    return 0, _ok("server-vision-loop", output_path=args.output or "", **out_payload)


def _add_server_common_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--base-url", default="http://localhost:8888", help="Recorder server base URL")
    parser.add_argument("--timeout", type=float, default=30.0, help="HTTP timeout in seconds")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="recorder-cli", description="AI-friendly CLI for iOS recorder pipelines")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate-steps", help="Validate step-list JSON")
    p_validate.add_argument("--input", required=True, help="Path to step JSON file")
    p_validate.add_argument("--case-name", default="", help="Override case name")

    p_gen = sub.add_parser("generate-test", help="Generate pytest test from steps")
    p_gen.add_argument("--input", required=True, help="Path to step JSON file")
    p_gen.add_argument("--case-name", required=True, help="Case name for pytest marker/function")
    p_gen.add_argument("--output", required=True, help="Output python test file path")

    p_export = sub.add_parser("export-bundle", help="Export py/json/html artifacts")
    p_export.add_argument("--input", required=True, help="Path to step JSON file")
    p_export.add_argument("--case-name", required=True, help="Base case name")
    p_export.add_argument("--export-dir", default="export", help="Export root directory")
    p_export.add_argument("--tests-dir", default="pytest/tests", help="Generated pytest tests directory")
    p_export.add_argument("--append-timestamp", action="store_true", default=True, help="Append timestamp suffix")
    p_export.add_argument("--no-append-timestamp", dest="append_timestamp", action="store_false", help="Disable timestamp suffix")

    p_server_status = sub.add_parser("server-status", help="Get recorder server/device status")
    _add_server_common_flags(p_server_status)

    p_server_cfg = sub.add_parser("server-set-config", help="Set recorder WDA URL via backend config API")
    _add_server_common_flags(p_server_cfg)
    p_server_cfg.add_argument("--wda-url", required=True, help="WDA URL to set, e.g. http://localhost:8100")

    p_steps_get = sub.add_parser("server-steps-get", help="Fetch recorded steps from backend")
    _add_server_common_flags(p_steps_get)
    p_steps_get.add_argument("--output", default="", help="Optional path to save JSON response")

    p_steps_clear = sub.add_parser("server-steps-clear", help="Clear recorded steps on backend")
    _add_server_common_flags(p_steps_clear)

    p_record = sub.add_parser("server-record-action", help="Call one /api/record* endpoint with JSON payload")
    _add_server_common_flags(p_record)
    p_record.add_argument("--action", required=True, choices=sorted(_RECORD_ENDPOINT_BY_ACTION.keys()), help="Recorder action name")
    p_record.add_argument("--mode", choices=["record", "live"], default="record", help="Execution mode: record appends steps, live executes only")
    p_record.add_argument("--payload-json", default="", help="Inline JSON payload object")
    p_record.add_argument("--payload-file", default="", help="Path to JSON payload file")

    p_server_export = sub.add_parser("server-export", help="Trigger backend export from currently recorded steps")
    _add_server_common_flags(p_server_export)
    p_server_export.add_argument("--case-name", required=True, help="Case name sent to /api/export")
    p_server_export.add_argument("--output", default="", help="Optional path to save export response JSON")

    p_vision_snapshot = sub.add_parser("server-vision-snapshot", help="Capture AI-readable snapshot: status/tree/frame")
    _add_server_common_flags(p_vision_snapshot)
    p_vision_snapshot.add_argument("--include-tree", action="store_true", default=True, help="Include /api/tree response")
    p_vision_snapshot.add_argument("--no-include-tree", dest="include_tree", action="store_false", help="Skip /api/tree response")
    p_vision_snapshot.add_argument("--include-frame", action="store_true", default=True, help="Include /api/frame response")
    p_vision_snapshot.add_argument("--no-include-frame", dest="include_frame", action="store_false", help="Skip /api/frame response")
    p_vision_snapshot.add_argument("--include-frame-data", action="store_true", default=False, help="Include frame base64 in snapshot")
    p_vision_snapshot.add_argument("--tree-fresh", action="store_true", default=False, help="Force fresh /api/tree fetch")
    p_vision_snapshot.add_argument("--output", default="", help="Optional path to save snapshot JSON")

    p_vision_exec = sub.add_parser("server-vision-execute", help="Execute one AI-selected action")
    _add_server_common_flags(p_vision_exec)
    p_vision_exec.add_argument("--action", required=True, choices=sorted(set(_RECORD_ENDPOINT_BY_ACTION) | set(_LIVE_ENDPOINT_BY_ACTION)), help="Action name")
    p_vision_exec.add_argument("--mode", choices=["record", "live"], default="record", help="Execution mode")
    p_vision_exec.add_argument("--payload-json", default="", help="Inline JSON payload object")
    p_vision_exec.add_argument("--payload-file", default="", help="Path to JSON payload file")

    p_vision_loop = sub.add_parser("server-vision-loop", help="Run scripted snapshot/action loop from a plan JSON")
    _add_server_common_flags(p_vision_loop)
    p_vision_loop.add_argument("--plan-file", required=True, help="Path to plan JSON")
    p_vision_loop.add_argument("--output", default="", help="Optional path to save loop result JSON")

    return parser


def run_cli(argv: list[str]) -> tuple[int, dict[str, Any]]:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate-steps":
        return cmd_validate_steps(args)
    if args.command == "generate-test":
        return cmd_generate_test(args)
    if args.command == "export-bundle":
        return cmd_export_bundle(args)
    if args.command == "server-status":
        return cmd_server_status(args)
    if args.command == "server-set-config":
        return cmd_server_set_config(args)
    if args.command == "server-steps-get":
        return cmd_server_steps_get(args)
    if args.command == "server-steps-clear":
        return cmd_server_steps_clear(args)
    if args.command == "server-record-action":
        return cmd_server_record_action(args)
    if args.command == "server-export":
        return cmd_server_export(args)
    if args.command == "server-vision-snapshot":
        return cmd_server_vision_snapshot(args)
    if args.command == "server-vision-execute":
        return cmd_server_vision_execute(args)
    if args.command == "server-vision-loop":
        return cmd_server_vision_loop(args)

    return 2, _err("unknown", "UNKNOWN_COMMAND", f"unsupported command: {args.command}")


def main(argv: list[str] | None = None) -> int:
    code, payload = run_cli(argv if argv is not None else sys.argv[1:])
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
