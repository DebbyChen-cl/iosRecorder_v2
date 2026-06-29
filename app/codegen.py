"""
codegen.py – Python test-script generator for iOS Recorder

Organized into three sections:
  1. UI setup   – imports and test function header (driver/actions via conftest fixtures)
  2. Elements   – locator helpers (selector type → AppiumBy constant)
  3. Export     – step-by-step code generation using DriverActions methods,
                  each wrapped in a reportportal `with step(...)` context
"""

import json
import math
from pathlib import Path
from typing import List, Optional


_RECORDING_RULES_FILE = Path(__file__).parent.parent / "recording_rules.json"
_COMPARE_RULE_DEFAULTS: dict = {
    "long_press_compare_keywords": ["compare"],
    "long_press_compare_selector_types": ["accessibility id", "id"],
}


def _load_recording_rules() -> dict:
    try:
        raw = json.loads(_RECORDING_RULES_FILE.read_text())
        cfg = {**_COMPARE_RULE_DEFAULTS, **raw}
        if not isinstance(cfg.get("long_press_compare_keywords"), list):
            cfg["long_press_compare_keywords"] = list(_COMPARE_RULE_DEFAULTS["long_press_compare_keywords"])
        if not isinstance(cfg.get("long_press_compare_selector_types"), list):
            cfg["long_press_compare_selector_types"] = list(_COMPARE_RULE_DEFAULTS["long_press_compare_selector_types"])
        return cfg
    except Exception:
        return dict(_COMPARE_RULE_DEFAULTS)


def _contains_compare_keyword(target: Optional[dict]) -> bool:
    if not target or target.get("type") == "coordinate":
        return False
    target_type = str(target.get("type", "") or "").strip().lower()
    value = str(target.get("value", "") or "").lower()
    if not value:
        return False
    cfg = _load_recording_rules()
    allowed_types = [str(t).strip().lower() for t in cfg.get("long_press_compare_selector_types", []) if str(t).strip()]
    if target_type not in allowed_types:
        return False
    keywords = [str(k).strip().lower() for k in cfg.get("long_press_compare_keywords", []) if str(k).strip()]
    return any(k in value for k in keywords)

# ── 1. UI Setup ────────────────────────────────────────────────────────────────

def generate_header(case_name: str = "") -> str:
    """Return the import block and @pytest.mark.name + test function signature.

    Driver and DriverActions are provided by conftest fixtures, not inlined here.
    """
    title = case_name or "recorded_test"
    fn = _safe_name(title)
    return f"""\
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("{title}")
def test_{fn}(actions: DriverActions):
"""


def _safe_name(name: str) -> str:
    """Convert a case name to a valid Python identifier."""
    safe = "".join(c if c.isalnum() or c == "_" else "_" for c in name)
    return safe.lstrip("_") or "case"


# ── 2. Elements ────────────────────────────────────────────────────────────────

_BY_MAP = {
    "accessibility id": "AppiumBy.ACCESSIBILITY_ID",
    "name":             "AppiumBy.NAME",
    "xpath":            "AppiumBy.XPATH",
    "id":               "AppiumBy.ID",
}


def _by(selector_type: str) -> str:
    """Map recorder selector type to AppiumBy constant string."""
    return _BY_MAP.get(selector_type, "AppiumBy.XPATH")


def _q(value: str) -> str:
    """Escape a string for use inside single-quoted Python string literals."""
    return (
        value
        .replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
    )


def _locator(target: dict) -> tuple[str, str]:
    """Return (by_const, escaped_value) for a step target dict."""
    return _by(target["type"]), _q(target["value"])


def _sc_kwargs(sc: Optional[dict]) -> str:
    """Build container keyword argument string from a scroll_container dict.

    Returns a string like:
        ", container_by=AppiumBy.ACCESSIBILITY_ID, container_value='Foo', container_w=390, container_h=700"
    or "" when no container info is available.
    """
    if not sc or sc.get("type") in ("coordinate", None) or not sc.get("value"):
        return ""
    sc_by  = _by(sc["type"])
    sc_val = _q(sc["value"])
    bounds = sc.get("bounds") or {}
    cw = bounds.get("w", 0)
    ch = bounds.get("h", 0)
    return f", container_by={sc_by}, container_value='{sc_val}', container_w={cw}, container_h={ch}"


def _needs_timeline_drag_nudge(*targets: Optional[dict]) -> bool:
    for target in targets:
        if not target:
            continue
        value = str(target.get("value", "") or "").lower()
        if any(token in value for token in ("timeline", "track", "multipletrack", "piptrack")):
            return True
    return False


# ── 3. Export ──────────────────────────────────────────────────────────────────

def _action_call(step: dict) -> tuple[str, list[str]]:
    """Return (step_label, [code_lines]) for one recorded step.

    step_label  – shown inside `with step("..."):`
    code_lines  – the actual actions.xxx() calls (no indentation)
    """
    action = step.get("action", "")
    t      = step.get("target")
    c      = step.get("coords", {})
    has_el = t and t.get("type") != "coordinate"

    # ── tap ───────────────────────────────────────────────────────────────────
    if action == "tap":
        if has_el:
            by, val = _locator(t)
            sc_kw = _sc_kwargs(step.get("scroll_container"))
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Tap {val} at ({px}%, {py}%)",
                        [f"actions.tap_within_element({by}, '{val}', {px}, {py}{sc_kw})"])
            return (f"[Action] Tap {val}",
                    [f"actions.tap_by_locator({by}, '{val}'{sc_kw})"])
        x, y = int(c.get("x", 0)), int(c.get("y", 0))
        return (f"[Action] Tap at ({x}, {y})",
                [f"actions.tap_by_coordinates({x}, {y})"])

    # ── double tap ────────────────────────────────────────────────────────────
    if action == "double_tap":
        if has_el:
            by, val = _locator(t)
            sc_kw = _sc_kwargs(step.get("scroll_container"))
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Double tap {val} at ({px}%, {py}%)",
                        [f"actions.double_tap_within_element({by}, '{val}', {px}, {py}{sc_kw})"])
            return (f"[Action] Double tap {val}",
                    [f"actions.double_tap(actions.find_element({by}, '{val}'{sc_kw}))"])
        return (f"[Action] Double tap at ({c.get('x')},{c.get('y')})",
                [f"# double_tap at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── five tap ──────────────────────────────────────────────────────────────
    if action == "five_tap":
        if has_el:
            by, val = _locator(t)
            sc_kw = _sc_kwargs(step.get("scroll_container"))
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Five tap {val} at ({px}%, {py}%)",
                        [f"actions.five_tap_within_element({by}, '{val}', {px}, {py}{sc_kw})"])
            return (f"[Action] Five tap {val}",
                    [f"actions.five_tap(actions.find_element({by}, '{val}'{sc_kw}))"])
        return (f"[Action] Five tap at ({c.get('x')},{c.get('y')})",
                [f"# five_tap at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── triple tap ────────────────────────────────────────────────────────────
    if action == "triple_tap":
        if has_el:
            by, val = _locator(t)
            sc_kw = _sc_kwargs(step.get("scroll_container"))
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Triple tap {val} at ({px}%, {py}%)",
                        [f"actions.triple_tap_within_element({by}, '{val}', {px}, {py}{sc_kw})"])
            return (f"[Action] Triple tap {val}",
                    [f"actions.triple_tap(actions.find_element({by}, '{val}'{sc_kw}))"])
        return (f"[Action] Triple tap at ({c.get('x')},{c.get('y')})",
                [f"# triple_tap at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── long press ────────────────────────────────────────────────────────────
    if action == "long_press":
        dur = round(step.get("duration", 1000) / 1000, 2)
        if has_el:
            by, val = _locator(t)
            sc_kw = _sc_kwargs(step.get("scroll_container"))
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Long press {val} at ({px}%, {py}%)",
                        [f"actions.long_press_within_element({by}, '{val}', {px}, {py}, duration={dur}{sc_kw})"])
            return (f"[Action] Long press {val}",
                    [f"actions.long_press(actions.find_element({by}, '{val}'{sc_kw}), duration={dur})"])
        return (f"[Action] Long press at ({c.get('x')},{c.get('y')})",
                [f"# long_press at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── two finger tap ────────────────────────────────────────────────────────
    if action == "two_finger_tap":
        if has_el:
            by, val = _locator(t)
            return (f"[Action] Two finger tap {val}",
                    [f"actions.two_finger_tap(actions.find_element({by}, '{val}'))"])
        return (f"[Action] Two finger tap at ({c.get('x')},{c.get('y')})",
                [f"# two_finger_tap at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── multi finger tap ──────────────────────────────────────────────────────
    if action == "multi_finger_tap":
        fingers = step.get("fingers", 3)
        if has_el:
            by, val = _locator(t)
            return (f"[Action] {fingers}-finger tap {val}",
                    [f"actions.multi_finger_tap(actions.find_element({by}, '{val}'), fingers={fingers})"])
        return (f"[Action] {fingers}-finger tap at ({c.get('x')},{c.get('y')})",
                [f"# multi_finger_tap at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── pinch ─────────────────────────────────────────────────────────────────
    if action == "pinch":
        scale    = round(step.get("scale", 0.5), 3)
        duration = step.get("duration", 500)  # ms
        # velocity magnitude = how fast the scale changes (scale-factor/sec), min 0.1.
        # XCUITest requires sign by direction: scale<1 => negative, scale>1 => positive.
        vel_mag = round(max(0.1, abs(scale - 1.0) / max(0.1, (duration / 1000))), 3)
        velocity = -vel_mag if scale < 1.0 else vel_mag
        if has_el:
            by, val = _locator(t)
            return (f"[Action] Pinch {val} scale={scale}",
                    [f"actions.pinch(actions.find_element({by}, '{val}'), scale={scale}, velocity={velocity})"])
        return (f"[Action] Pinch at ({c.get('x')},{c.get('y')}) scale={scale}",
                [f"# pinch at ({c.get('x')},{c.get('y')}) scale={scale} — no element matched"])

    # ── rotate ────────────────────────────────────────────────────────────────
    if action == "rotate":
        deg = round(step.get("rotation", 0), 1)
        if has_el:
            by, val = _locator(t)
            return (f"[Action] Rotate {val} {deg}°",
                    [f"actions.rotate(actions.find_element({by}, '{val}'), rotation={deg})"])
        return (f"[Action] Rotate at ({c.get('x')},{c.get('y')})",
                [f"# rotate at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── scroll ────────────────────────────────────────────────────────────────
    if action == "scroll":
        sc = step.get("scroll_container")
        st = step.get("scroll_target")
        dx = c.get("x2", 0) - c.get("x1", 0)
        dy = c.get("y2", 0) - c.get("y1", 0)
        direction = _swipe_direction(dx, dy)
        if st and st.get("type") != "coordinate":
            by, val = _locator(st)
            if sc and sc.get("type") != "coordinate":
                sc_by, sc_val = _locator(sc)
                offsets = step.get("scroll_offsets")
                if offsets:
                    os_ = f"({offsets['start_x_pct']}, {offsets['start_y_pct']})"
                    oe_ = f"({offsets['end_x_pct']}, {offsets['end_y_pct']})"
                    raw_dist = math.sqrt(dx ** 2 + dy ** 2)
                    dur_ms = step.get("duration", 600)
                    velocity = int(max(50, min(2000, raw_dist * 1000 / dur_ms))) if dur_ms > 0 else 100
                    return (f"[Action] Scroll until {val}",
                            [f"actions.scroll_until({sc_by}, '{sc_val}', {by}, '{val}', direction='{direction}', offset_start={os_}, offset_end={oe_}, velocity={velocity})"])
                return (f"[Action] Scroll until {val}",
                        [f"actions.scroll_until({sc_by}, '{sc_val}', {by}, '{val}', direction='{direction}')"])
            return (f"[Action] Scroll until {val}",
                    [f"# scroll_until: scroll_container missing — re-record this step"])
        return (f"[Action] Scroll {direction}",
                [f"actions.scroll(direction='{direction}')"])

    # ── swipe ─────────────────────────────────────────────────────────────────
    if action == "swipe":
        dur = step.get("duration", 400)
        x1, y1 = int(c.get("x1", 0)), int(c.get("y1", 0))
        x2, y2 = int(c.get("x2", 0)), int(c.get("y2", 0))
        direction = step.get("direction", _swipe_direction(x2 - x1, y2 - y1))
        sst = step.get("start_target")
        if sst and sst.get("type") != "coordinate":
            sst_by, sst_val = _by(sst["type"]), _q(sst["value"])
            pct = sst.get("offset_pct", {"x": 50.0, "y": 50.0})
            px, py = pct["x"], pct["y"]
            raw_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            velocity = round(max(50.0, min(5000.0, raw_dist * 1000 / dur)), 1) if dur > 0 else 500.0
            dist_arg = round(raw_dist, 1)
            return (f"[Action] Swipe {direction} on {sst_val}",
                    [f"actions.swipe_on_element({sst_by}, '{sst_val}', '{direction}', velocity={velocity}, from_pct_x={px}, from_pct_y={py}, distance_pts={dist_arg})"])
        return (f"[Action] Swipe {direction}",
                [f"# swipe {direction} at ({x1},{y1})→({x2},{y2}) — no element matched"])

    # ── drag / long-press drag ────────────────────────────────────────────────
    if action in ("drag", "long_press_drag"):
        is_long_press_drag = action == "long_press_drag"
        label_verb = "Long press drag" if is_long_press_drag else "Drag"
        within_fn = "long_press_drag_within_elements" if is_long_press_drag else "drag_within_elements"
        coords_fn = "long_press_drag_coordinates" if is_long_press_drag else "drag_coordinates"
        dur = round(step.get("duration", 1000) / 1000, 2)
        press_kw = ""
        if is_long_press_drag:
            press_dur = round(max(1000, step.get("press_duration", 1000)) / 1000, 2)
            press_kw = f", press_duration={press_dur}"
        x1, y1 = int(c.get("x1", 0)), int(c.get("y1", 0))
        x2, y2 = int(c.get("x2", 0)), int(c.get("y2", 0))
        st = step.get("start_target")
        et = step.get("end_target")
        has_start = st and st.get("type") != "coordinate"
        has_end   = et and et.get("type") != "coordinate"
        nudge_kw = ", activation_nudge_y=-8" if is_long_press_drag and _needs_timeline_drag_nudge(st, et) else ""
        if has_start and has_end:
            s_by, s_val = _by(st["type"]), _q(st["value"])
            e_by, e_val = _by(et["type"]), _q(et["value"])
            sp = st.get("offset_pct", {"x": 50.0, "y": 50.0})
            ep = et.get("offset_pct", {"x": 50.0, "y": 50.0})
            sx, sy = sp["x"], sp["y"]
            ex, ey = ep["x"], ep["y"]
            return (f"[Action] {label_verb} {s_val} ({sx}%,{sy}%) → {e_val} ({ex}%,{ey}%)",
                    [f"actions.{within_fn}({s_by}, '{s_val}', {sx}, {sy}, {e_by}, '{e_val}', {ex}, {ey}, duration={dur}{press_kw}{nudge_kw})"])
        if has_start:
            s_by, s_val = _by(st["type"]), _q(st["value"])
            sp = st.get("offset_pct", {"x": 50.0, "y": 50.0})
            if is_long_press_drag:
                return (f"[Action] {label_verb} {s_val} ({sp['x']}%,{sp['y']}%) → ({x2},{y2})",
                        [f"actions.long_press_drag_from_element_to_coordinates({s_by}, '{s_val}', {sp['x']}, {sp['y']}, {x2}, {y2}, duration={dur}{press_kw}{nudge_kw})"])
            return (f"[Action] {label_verb} {_q(st['value'])} ({sp['x']}%,{sp['y']}%) → ({x2},{y2})",
                    [f"actions.{coords_fn}({x1}, {y1}, {x2}, {y2}, duration={dur}{press_kw})"])
        if has_end:
            e_by, e_val = _by(et["type"]), _q(et["value"])
            ep = et.get("offset_pct", {"x": 50.0, "y": 50.0})
            if is_long_press_drag:
                return (f"[Action] {label_verb} ({x1},{y1}) → {e_val} ({ep['x']}%,{ep['y']}%)",
                        [f"actions.long_press_drag_from_coordinates_to_element({x1}, {y1}, {e_by}, '{e_val}', {ep['x']}, {ep['y']}, duration={dur}{press_kw}{nudge_kw})"])
        return (f"[Action] {label_verb} ({x1},{y1}) → ({x2},{y2})",
                [f"actions.{coords_fn}({x1}, {y1}, {x2}, {y2}, duration={dur}{press_kw}{nudge_kw})"])

    # ── paint ─────────────────────────────────────────────────────────────────
    if action == "paint":
        points = step.get("paint_points_pct") or []
        dur_ms = int(step.get("duration", 1000))
        if has_el and points:
            by, val = _locator(t)
            p_list: list[str] = []
            for p in points:
                p_list.append(f"({float(p.get('x_pct', 50.0))}, {float(p.get('y_pct', 50.0))}, {int(p.get('t_ms', 0))})")
            points_arg = "[" + ", ".join(p_list) + "]"
            return (
                f"[Action] Paint on {val} ({len(points)} points)",
                [f"actions.paint_in_element({by}, '{val}', {points_arg}, duration_ms={dur_ms})"],
            )
        if has_el:
            by, val = _locator(t)
            return (
                f"[Action] Paint on {val}",
                [f"# paint on {val} — no paint_points_pct recorded"],
            )
        return (
            f"[Action] Paint at ({int(c.get('x', 0))},{int(c.get('y', 0))})",
            [f"# paint at ({int(c.get('x', 0))},{int(c.get('y', 0))}) — no element matched"],
        )

    # ── type text ─────────────────────────────────────────────────────────────
    if action == "type_text":
        text = _q(step.get("text", ""))
        if has_el:
            by, val = _locator(t)
            return (f"[Action] Type '{step.get('text', '')}' into {val}",
                    [f"actions.type_text_by_locator({by}, '{val}', '{text}')"])
        return (f"[Action] Type '{step.get('text', '')}'",
                [f"# type_text '{text}' — no element matched"])

    # ── home ──────────────────────────────────────────────────────────────────
    if action == "home":
        return ("[Action] Press Home button",
                ["actions.press_home()"])

    # ── launch app ────────────────────────────────────────────────────────────
    if action == "launch_app":
        bundle_id = _q(step.get("bundle_id", ""))
        name = step.get("app_name") or bundle_id
        return (f"[Action] Launch {name}",
                [f"actions.launch_app('{bundle_id}')"])

    # ── terminate app ─────────────────────────────────────────────────────────
    if action == "terminate_app":
        bundle_id = _q(step.get("bundle_id", ""))
        name = step.get("app_name") or bundle_id
        return (f"[Action] Terminate {name}",
                [f"actions.terminate_app('{bundle_id}')"])

    # ── verify visible ────────────────────────────────────────────────────────
    if action == "verify_visible":
        if has_el:
            by, val = _locator(t)
            sc_kw = _sc_kwargs(step.get("scroll_container"))
            return (f"[Verify] {val} is visible",
                    [f"actions.verify_visible({by}, '{val}'{sc_kw})"])
        return (f"[Verify] element visible at ({c.get('x')},{c.get('y')})",
                [f"# verify_visible at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── verify not visible ────────────────────────────────────────────────────
    if action == "verify_not_visible":
        if has_el:
            by, val = _locator(t)
            return (f"[Verify] {val} is not visible",
                    [f"actions.verify_not_visible({by}, '{val}')"])
        return (f"[Verify] element not visible at ({c.get('x')},{c.get('y')})",
                [f"# verify_not_visible at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── verify get text ───────────────────────────────────────────────────────
    if action == "verify_get_text":
        expected = step.get("expected_text", "")
        if has_el:
            by, val = _locator(t)
            return (f"[Verify] {val} text equals '{expected}'",
                    [f"actions.verify_text({by}, '{val}', '{_q(expected)}')"])
        return (f"[Verify] text equals '{expected}'",
                [f"# verify_text '{_q(expected)}' — no element matched"])

    # ── screenshot ground truth ───────────────────────────────────────────────
    if action == "verify_screenshot_gt":
        name = _q(step.get("screenshot_name", "screenshot"))
        if has_el:
            by, val = _locator(t)
            return (f"[Verify] Capture '{name}' for GT comparison",
                    [f"actions.capture_for_gt('{name}', {by}, '{val}', threshold=0.95)"])
        return (f"[Verify] Capture '{name}' for GT comparison",
                [f"actions.capture_for_gt('{name}', threshold=0.95)"])

    # ── screenshot diff ───────────────────────────────────────────────────────
    if action == "verify_screenshot_diff":
        name = _q(step.get("screenshot_name", "screenshot"))
        phase = step.get("phase", "before")
        expected = step.get("expected_result", "same")  # only present on phase=="after"
        if has_el:
            by, val = _locator(t)
            if phase == "after":
                return (f"[Verify] Capture '{name}' {phase} screenshot",
                        [f"actions.capture_for_preview('{name}', '{phase}', {by}, '{val}', expected_result='{expected}', threshold=0.95)"])
            return (f"[Verify] Capture '{name}' {phase} screenshot",
                    [f"actions.capture_for_preview('{name}', '{phase}', {by}, '{val}')"])
        if phase == "after":
            return (f"[Verify] Capture '{name}' {phase} screenshot",
                    [f"actions.capture_for_preview('{name}', '{phase}', expected_result='{expected}', threshold=0.95)"])
        return (f"[Verify] Capture '{name}' {phase} screenshot",
                [f"actions.capture_for_preview('{name}', '{phase}')"])

    # ── long press + capture-after during hold ───────────────────────────────
    if action == "long_press_capture_after_during_hold":
        lp = step.get("long_press", {})
        press_t = lp.get("target") or {}
        capture_t = step.get("capture_target") or {}
        name = _q(step.get("screenshot_name", "screenshot"))
        expected = step.get("expected_result", "same")
        dur = round(lp.get("duration", 1000) / 1000, 2)

        if press_t.get("type") == "coordinate" or capture_t.get("type") == "coordinate":
            return (
                f"[Action] Long press and capture '{name}' during hold",
                ["# long_press_capture_after_during_hold skipped — missing element locator"],
            )

        p_by, p_val = _locator(press_t)
        c_by, c_val = _locator(capture_t)
        sc_kw = _sc_kwargs(lp.get("scroll_container"))
        pct = press_t.get("offset_pct")
        if pct:
            px, py = pct["x"], pct["y"]
            return (
                f"[Action] Long press {p_val} and capture '{name}' after during hold",
                [
                    f"actions.long_press_capture_for_preview_within_element({p_by}, '{p_val}', {px}, {py}, duration={dur}, capture_name='{name}', capture_by={c_by}, capture_value='{c_val}', expected_result='{expected}', threshold=0.95{sc_kw})"
                ],
            )
        return (
            f"[Action] Long press {p_val} and capture '{name}' after during hold",
            [
                f"actions.long_press_capture_for_preview({p_by}, '{p_val}', duration={dur}, capture_name='{name}', capture_by={c_by}, capture_value='{c_val}', expected_result='{expected}', threshold=0.95{sc_kw})"
            ],
        )

    return (f"[Action] {action}",
            [f"# [unknown action: {action}]"])


def _swipe_direction(dx: float, dy: float) -> str:
    """Derive 'up'/'down'/'left'/'right' from a coordinate delta.

    Note: a finger moving *up* (negative dy) scrolls content *down*.
    """
    if abs(dx) > abs(dy):
        return "right" if dx > 0 else "left"
    return "down" if dy < 0 else "up"


def _scroll_needs_target(scroll_step: dict) -> bool:
    """Return True if this scroll step has no usable element-based scroll_target."""
    st = scroll_step.get("scroll_target")
    return not st or st.get("type") == "coordinate"


def _merge_five_taps(steps: List[dict]) -> List[dict]:
    """Merge exactly 5 consecutive tap steps on the same element into a single five_tap step.

    Matches when: action=="tap", same target type+value across all 5 steps, and
    target is not coordinate-only.  The first step's target/coords/scroll_container
    are kept on the merged step.
    """
    out: list[dict] = []
    i = 0
    while i < len(steps):
        s = steps[i]
        if s.get("action") != "tap":
            out.append(s)
            i += 1
            continue

        t0 = s.get("target")
        if not t0 or t0.get("type") == "coordinate":
            out.append(s)
            i += 1
            continue

        run = [s]
        j = i + 1
        while j < len(steps):
            ns = steps[j]
            if ns.get("action") != "tap":
                break
            nt = ns.get("target")
            if not nt or nt.get("type") == "coordinate":
                break
            if nt.get("type") != t0.get("type") or nt.get("value") != t0.get("value"):
                break
            run.append(ns)
            j += 1

        if len(run) == 5:
            merged = dict(run[0])
            merged["action"] = "five_tap"
            out.append(merged)
            i = j
        else:
            out.extend(run[:1])
            i += 1

    return out


def _merge_scroll_tap(steps: List[dict]) -> List[dict]:
    """Merge consecutive scroll steps followed by a tap into scroll_until + tap.

    The server-side _record_scroll_target consolidates multiple scrolls and sets
    scroll_target before export.  If that failed (race condition: the tap action
    clears the WDA cache before _record_scroll_target can fetch the tree), the
    scroll steps will have no usable scroll_target.  This function repairs the
    pattern at codegen time by using the following tap's target as scroll_target.

    When the server already set a valid scroll_target, this function is a no-op
    for that group (it preserves the existing scroll_target unchanged).
    """
    out: list[dict] = []
    i = 0
    while i < len(steps):
        s = steps[i]
        if s.get("action") != "scroll":
            out.append(s)
            i += 1
            continue

        # Collect consecutive scroll steps
        run: list[dict] = [s]
        j = i + 1
        while j < len(steps) and steps[j].get("action") == "scroll":
            run.append(steps[j])
            j += 1

        # Check if the next step is a tap-type action with a valid element target
        tap_s = steps[j] if j < len(steps) else None
        if tap_s and tap_s.get("action") in ("tap", "double_tap", "triple_tap", "five_tap", "long_press"):
            tap_t = tap_s.get("target")
            if tap_t and tap_t.get("type") != "coordinate":
                # Use the last scroll step (has most recent offsets / container)
                last_scroll = dict(run[-1])
                # Patch scroll_target only when it is absent or coordinate-only
                if _scroll_needs_target(last_scroll):
                    last_scroll["scroll_target"] = tap_t
                out.append(last_scroll)
                out.append(tap_s)
                i = j + 1
                continue

        # No merge possible — emit the scroll run unchanged
        out.extend(run)
        i = j

    return out


def _merge_screenshot_diff_long_press_compare(steps: List[dict]) -> List[dict]:
        """Merge before + long_press + after pattern into one synthetic action.

        Pattern:
            verify_screenshot_diff(before) -> long_press -> verify_screenshot_diff(after)
        Conditions:
            - exactly one process step (the long_press)
            - long_press target contains configured compare keyword
        Result:
            keep BEFORE step unchanged;
            replace long_press + AFTER with one action that captures AFTER during hold,
            using AFTER target (= same as BEFORE target from recording rule).
        """
        out: list[dict] = []
        i = 0
        while i < len(steps):
                s = steps[i]
                if (
                        i + 2 < len(steps)
                        and s.get("action") == "verify_screenshot_diff"
                        and s.get("phase") == "before"
                        and steps[i + 1].get("action") == "long_press"
                        and steps[i + 2].get("action") == "verify_screenshot_diff"
                        and steps[i + 2].get("phase") == "after"
                        and _contains_compare_keyword(steps[i + 1].get("target"))
                ):
                        before_s = s
                        long_s = steps[i + 1]
                        after_s = steps[i + 2]
                        out.append(before_s)
                        out.append(
                                {
                                        "action": "long_press_capture_after_during_hold",
                                        "long_press": long_s,
                                        "capture_target": after_s.get("target") or before_s.get("target"),
                                        "screenshot_name": after_s.get("screenshot_name", "screenshot"),
                                        "expected_result": after_s.get("expected_result", "same"),
                                }
                        )
                        i += 3
                        continue
                out.append(s)
                i += 1
        return out


def generate_script(steps: List[dict], case_name: str = "") -> str:
    """
    Convert a list of recorded step dicts into a complete pytest test file
    using DriverActions methods, each wrapped in a reportportal step context.

    Screenshot steps (verify_screenshot_gt / verify_screenshot_diff) only
    capture images inline.  A single ``run_screenshot_comparisons()`` call is
    appended at the end of the test to evaluate ALL captures together (AND
    logic — every comparison runs, all failures reported at once).
    """
    steps = _merge_five_taps(steps)
    steps = _merge_scroll_tap(steps)
    steps = _merge_screenshot_diff_long_press_compare(steps)
    header = generate_header(case_name)
    body_lines: list[str] = []
    _screenshot_actions = {"verify_screenshot_gt", "verify_screenshot_diff"}
    has_screenshots = any(s.get("action") in _screenshot_actions for s in steps)
    for s in steps:
        label, code_lines = _action_call(s)
        safe_label = label.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")
        body_lines.append(f'    with step("{safe_label}"):')
        for line in code_lines:
            body_lines.append(f"        {line}")
    if has_screenshots:
        body_lines.append('    with step("[Verify] Screenshot comparisons"):')
        body_lines.append("        actions.run_screenshot_comparisons(threshold=0.95)")
    body_lines.append("    assert True")

    return header + "\n".join(body_lines) + "\n"
