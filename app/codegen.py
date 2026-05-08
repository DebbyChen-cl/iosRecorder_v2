"""
codegen.py – Python test-script generator for iOS Recorder

Organized into three sections:
  1. UI setup   – imports and test function header (driver/actions via conftest fixtures)
  2. Elements   – locator helpers (selector type → AppiumBy constant)
  3. Export     – step-by-step code generation using DriverActions methods,
                  each wrapped in a reportportal `with step(...)` context
"""

import math
from typing import List

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
    return value.replace("\\", "\\\\").replace("'", "\\'")


def _locator(target: dict) -> tuple[str, str]:
    """Return (by_const, escaped_value) for a step target dict."""
    return _by(target["type"]), _q(target["value"])


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
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Tap {val} at ({px}%, {py}%)",
                        [f"actions.tap_within_element({by}, '{val}', {px}, {py})"])
            return (f"[Action] Tap {val}",
                    [f"actions.tap_by_locator({by}, '{val}')"])
        x, y = int(c.get("x", 0)), int(c.get("y", 0))
        return (f"[Action] Tap at ({x}, {y})",
                [f"actions.tap_by_coordinates({x}, {y})"])

    # ── double tap ────────────────────────────────────────────────────────────
    if action == "double_tap":
        if has_el:
            by, val = _locator(t)
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Double tap {val} at ({px}%, {py}%)",
                        [f"actions.double_tap_within_element({by}, '{val}', {px}, {py})"])
            return (f"[Action] Double tap {val}",
                    [f"actions.double_tap(actions.find_element({by}, '{val}')"])
        return (f"[Action] Double tap at ({c.get('x')},{c.get('y')})",
                [f"# double_tap at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── triple tap ────────────────────────────────────────────────────────────
    if action == "triple_tap":
        if has_el:
            by, val = _locator(t)
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Triple tap {val} at ({px}%, {py}%)",
                        [f"actions.triple_tap_within_element({by}, '{val}', {px}, {py})"])
            return (f"[Action] Triple tap {val}",
                    [f"actions.triple_tap(actions.find_element({by}, '{val}'))"])
        return (f"[Action] Triple tap at ({c.get('x')},{c.get('y')})",
                [f"# triple_tap at ({c.get('x')},{c.get('y')}) — no element matched"])

    # ── long press ────────────────────────────────────────────────────────────
    if action == "long_press":
        dur = round(step.get("duration", 1000) / 1000, 2)
        if has_el:
            by, val = _locator(t)
            pct = t.get("offset_pct")
            if pct:
                px, py = pct["x"], pct["y"]
                return (f"[Action] Long press {val} at ({px}%, {py}%)",
                        [f"actions.long_press_within_element({by}, '{val}', {px}, {py}, duration={dur})"])
            return (f"[Action] Long press {val}",
                    [f"actions.long_press(actions.find_element({by}, '{val}'), duration={dur})"])
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
        scale = round(step.get("scale", 0.5), 3)
        if has_el:
            by, val = _locator(t)
            return (f"[Action] Pinch {val} scale={scale}",
                    [f"actions.pinch(actions.find_element({by}, '{val}'), scale={scale})"])
        return (f"[Action] Pinch at ({c.get('x')},{c.get('y')}) scale={scale}",
                [f"# pinch at ({c.get('x')},{c.get('y')}) scale={scale} — no element matched"])

    # ── rotate ────────────────────────────────────────────────────────────────
    if action == "rotate":
        rad = round(step.get("rotation", 0) * math.pi / 180, 4)
        if has_el:
            by, val = _locator(t)
            return (f"[Action] Rotate {val} {round(step.get('rotation', 0), 1)}°",
                    [f"actions.rotate(actions.find_element({by}, '{val}'), rotation={rad})"])
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
        st = step.get("swipe_target")
        if st and st.get("type") != "coordinate":
            by, val = _locator(st)
            direction = step.get("direction", "up")
            return (f"[Action] Swipe until {val}",
                    [f"actions.swipe_until({by}, '{val}', direction='{direction}')"])
        dur = step.get("duration", 400)
        x1, y1 = int(c.get("x1", 0)), int(c.get("y1", 0))
        x2, y2 = int(c.get("x2", 0)), int(c.get("y2", 0))
        direction = step.get("direction", _swipe_direction(x2 - x1, y2 - y1))
        return (f"[Action] Swipe {direction}",
                [f"actions.swipe({x1}, {y1}, {x2}, {y2}, duration={dur})"])

    # ── drag ──────────────────────────────────────────────────────────────────
    if action == "drag":
        dur = round(step.get("duration", 1000) / 1000, 2)
        x1, y1 = int(c.get("x1", 0)), int(c.get("y1", 0))
        x2, y2 = int(c.get("x2", 0)), int(c.get("y2", 0))
        return (f"[Action] Drag ({x1},{y1}) → ({x2},{y2})",
                [f"actions.drag_coordinates({x1}, {y1}, {x2}, {y2}, duration={dur})"])

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

    # ── verify visible ────────────────────────────────────────────────────────
    if action == "verify_visible":
        if has_el:
            by, val = _locator(t)
            return (f"[Verify] {val} is visible",
                    [f"actions.verify_visible({by}, '{val}')"])
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
        return (f"[Verify] Save screenshot GT '{name}'",
                [f"actions.screenshot_gt('{name}')"])

    # ── screenshot diff ───────────────────────────────────────────────────────
    if action == "verify_screenshot_diff":
        name = _q(step.get("screenshot_name", "screenshot"))
        phase = step.get("phase", "before")
        if phase == "before":
            return (f"[Verify] Screenshot diff — save before state",
                    [f"actions.screenshot_gt('{name}')  # save before-state GT"])
        return (f"[Verify] Screenshot diff — compare against GT",
                [f"actions.screenshot_diff('{name}')"])

    return (f"[Action] {action}",
            [f"# [unknown action: {action}]"])


def _swipe_direction(dx: float, dy: float) -> str:
    """Derive 'up'/'down'/'left'/'right' from a coordinate delta.

    Note: a finger moving *up* (negative dy) scrolls content *down*.
    """
    if abs(dx) > abs(dy):
        return "right" if dx > 0 else "left"
    return "down" if dy < 0 else "up"


def generate_script(steps: List[dict], case_name: str = "") -> str:
    """
    Convert a list of recorded step dicts into a complete pytest test file
    using DriverActions methods, each wrapped in a reportportal step context.
    """
    header = generate_header(case_name)
    body_lines: list[str] = []
    for s in steps:
        label, code_lines = _action_call(s)
        safe_label = label.replace("\\", "\\\\").replace('"', '\\"')
        body_lines.append(f'    with step("{safe_label}"):')
        for line in code_lines:
            body_lines.append(f"        {line}")

    return header + "\n".join(body_lines) + "\n"
