"""
Block 4 — Codegen

Verifies that generate_script() produces the correct Python test code for
each action type. Tests are snapshot-style: fixed step dict in, fixed code
string out. No device or server needed.
"""

import pytest

pytestmark = pytest.mark.unit

from app.codegen import generate_header, generate_script, _merge_scroll_tap


# ── generate_header ────────────────────────────────────────────────────────────

def test_header_contains_test_function():
    code = generate_header("MyTest")
    assert "def test_MyTest(actions: DriverActions):" in code


def test_header_contains_mark():
    code = generate_header("MyTest")
    assert '@pytest.mark.name("MyTest")' in code


def test_header_imports():
    code = generate_header("MyTest")
    assert "from appium.webdriver.common.appiumby import AppiumBy" in code
    assert "from reportportal_client import step" in code


def test_header_empty_name_falls_back():
    code = generate_header("")
    assert "def test_recorded_test" in code


def test_header_special_chars_sanitized():
    code = generate_header("My Test-Case!")
    assert "def test_My_Test_Case_" in code


# ── generate_script — tap ──────────────────────────────────────────────────────

TAP_WITH_ELEMENT = {
    "action": "tap",
    "coords": {"x": 140, "y": 222},
    "target": {"type": "accessibility id", "value": "SaveButton"},
    "timestamp": "2026-01-01T00:00:00",
}

TAP_COORDINATE_ONLY = {
    "action": "tap",
    "coords": {"x": 140, "y": 222},
    "target": {"type": "coordinate", "value": ""},
    "timestamp": "2026-01-01T00:00:00",
}


def test_tap_by_locator_generated():
    code = generate_script([TAP_WITH_ELEMENT], "Test")
    assert "actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SaveButton')" in code


def test_tap_step_label():
    code = generate_script([TAP_WITH_ELEMENT], "Test")
    assert '[Action] Tap SaveButton' in code


def test_tap_coordinate_fallback():
    code = generate_script([TAP_COORDINATE_ONLY], "Test")
    assert "actions.tap_by_coordinates(140, 222)" in code


def test_tap_with_offset_pct():
    step = {
        "action": "tap",
        "coords": {"x": 140, "y": 222},
        "target": {"type": "accessibility id", "value": "SaveButton", "offset_pct": {"x": 25.0, "y": 50.0}},
        "timestamp": "2026-01-01T00:00:00",
    }
    code = generate_script([step], "Test")
    assert "actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'SaveButton', 25.0, 50.0)" in code


# ── generate_script — verify actions ──────────────────────────────────────────

def test_verify_visible_generated():
    step = {
        "action": "verify_visible",
        "coords": {"x": 140, "y": 222},
        "target": {"type": "accessibility id", "value": "SaveButton"},
        "timestamp": "2026-01-01T00:00:00",
    }
    code = generate_script([step], "Test")
    assert "actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'SaveButton')" in code
    assert "[Verify] SaveButton is visible" in code


def test_verify_get_text_generated():
    step = {
        "action": "verify_get_text",
        "coords": {"x": 140, "y": 222},
        "target": {"type": "accessibility id", "value": "SaveButton"},
        "expected_text": "Hello",
        "timestamp": "2026-01-01T00:00:00",
    }
    code = generate_script([step], "Test")
    assert "actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'SaveButton', 'Hello')" in code


# ── generate_script — home / launch_app ───────────────────────────────────────

def test_home_generated():
    step = {"action": "home", "coords": {}, "timestamp": "2026-01-01T00:00:00"}
    code = generate_script([step], "Test")
    assert "actions.press_home()" in code


def test_launch_app_generated():
    step = {"action": "launch_app", "bundle_id": "com.example.app", "coords": {}, "timestamp": "2026-01-01T00:00:00"}
    code = generate_script([step], "Test")
    assert "actions.launch_app('com.example.app')" in code


# ── generate_script — swipe / scroll ──────────────────────────────────────────

def test_swipe_direction_label():
    step = {
        "action": "swipe",
        "coords": {"x1": 300, "y1": 400, "x2": 100, "y2": 400},
        "duration": 400,
        "timestamp": "2026-01-01T00:00:00",
    }
    code = generate_script([step], "Test")
    assert "[Action] Swipe left" in code


def test_scroll_without_target_uses_direction():
    # Finger moves from y=600 → y=200 (upward), so content scrolls "down"
    step = {
        "action": "scroll",
        "coords": {"x1": 200, "y1": 600, "x2": 200, "y2": 200},
        "duration": 600,
        "timestamp": "2026-01-01T00:00:00",
    }
    code = generate_script([step], "Test")
    assert "actions.scroll(direction='down')" in code


# ── generate_script — structure ────────────────────────────────────────────────

def test_output_has_with_step_blocks():
    code = generate_script([TAP_WITH_ELEMENT], "Test")
    assert 'with step(' in code


def test_output_ends_with_assert_true():
    code = generate_script([TAP_WITH_ELEMENT], "Test")
    assert "assert True" in code


def test_unknown_action_produces_comment():
    step = {"action": "unknown_action", "coords": {}, "timestamp": "2026-01-01T00:00:00"}
    code = generate_script([step], "Test")
    assert "# [unknown action: unknown_action]" in code


def test_screenshot_comparison_appended():
    step = {
        "action": "verify_screenshot_gt",
        "coords": {"x": 0, "y": 0},
        "target": {"type": "accessibility id", "value": "SaveButton"},
        "screenshot_name": "my_shot",
        "timestamp": "2026-01-01T00:00:00",
    }
    code = generate_script([step], "Test")
    assert "actions.run_screenshot_comparisons(threshold=0.95)" in code


# ── _merge_scroll_tap ──────────────────────────────────────────────────────────

def test_merge_scroll_tap_basic():
    scroll = {
        "action": "scroll",
        "coords": {"x1": 200, "y1": 600, "x2": 200, "y2": 200},
        "scroll_container": {"type": "accessibility id", "value": "MainScroll", "bounds": {"w": 390, "h": 494}},
        "timestamp": "2026-01-01T00:00:00",
    }
    tap = {
        "action": "tap",
        "coords": {"x": 195, "y": 390},
        "target": {"type": "accessibility id", "value": "Item1"},
        "timestamp": "2026-01-01T00:00:01",
    }
    merged = _merge_scroll_tap([scroll, tap])
    assert len(merged) == 2
    # scroll gets tap's target as scroll_target
    assert merged[0]["scroll_target"]["value"] == "Item1"


def test_merge_scroll_tap_no_merge_without_following_tap():
    scroll = {
        "action": "scroll",
        "coords": {"x1": 200, "y1": 600, "x2": 200, "y2": 200},
        "timestamp": "2026-01-01T00:00:00",
    }
    result = _merge_scroll_tap([scroll])
    assert len(result) == 1
    assert "scroll_target" not in result[0]
