"""
test_recording_demo.py — Integration tests for the recording pipeline.

Each test covers one or more action types. Tests do NOT assert exact element
values (those change with app version / screen state). Instead they assert:
  - HTTP 200 from every record endpoint
  - Step count and action names are correct
  - Required fields are present in every step
  - Export produces valid saved_paths

Prerequisites (must be done manually before running):
  - Start the recorder server:   cd /Users/rdqe/iosRecorder_v2 && bash start.sh
  - Ensure WDA is connected:     GET /api/status should return "connected": true
  - Open the iOS app to a stable screen with tappable elements

Run a single test:
  pytest unittest/test_recording_demo.py::test_tap -v

Run all:
  pytest unittest/ -v
"""

import pytest


# ── Helpers ────────────────────────────────────────────────────────────────────

def assert_step(step: dict, action: str):
    """Common assertions that every recorded step must satisfy."""
    assert step["action"] == action, f"Expected action={action!r}, got {step['action']!r}"
    assert "timestamp" in step, "Step missing timestamp"


def get_steps(client):
    resp = client.get("/api/steps")
    assert resp.status_code == 200
    return resp.json()["steps"]


# ── Tap family ─────────────────────────────────────────────────────────────────

def test_tap(client, warm_tree):
    """Single tap records one step with coords and a target."""
    r = client.post("/api/record", json={"x": 200, "y": 400})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "tap")
    assert "coords" in s
    assert "target" in s
    assert s["target"]["type"] in ("accessibility id", "name", "xpath", "coordinate")


def test_double_tap(client, warm_tree):
    r = client.post("/api/record/double_tap", json={"x": 200, "y": 400})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    assert_step(steps[0], "double_tap")
    assert "target" in steps[0]


def test_triple_tap(client, warm_tree):
    r = client.post("/api/record/triple_tap", json={"x": 200, "y": 400})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    assert_step(steps[0], "triple_tap")


def test_long_press(client, warm_tree):
    r = client.post("/api/record/long_press", json={"x": 200, "y": 400, "duration": 1500})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "long_press")
    assert s["duration"] == 1500


def test_two_finger_tap(client, warm_tree):
    r = client.post("/api/record/two_finger_tap", json={"x": 200, "y": 400})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    assert_step(steps[0], "two_finger_tap")


def test_multi_finger_tap(client, warm_tree):
    r = client.post("/api/record/multi_finger_tap", json={"x": 200, "y": 400, "fingers": 3})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "multi_finger_tap")
    assert s["fingers"] == 3


# ── Gesture family ─────────────────────────────────────────────────────────────

def test_pinch(client, warm_tree):
    r = client.post("/api/record/pinch", json={"x": 200, "y": 400, "scale": 0.5, "spread": 80, "duration": 500})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "pinch")
    assert s["scale"] == 0.5


def test_rotate(client, warm_tree):
    r = client.post("/api/record/rotate", json={"x": 200, "y": 400, "rotation": 90.0, "spread": 80, "duration": 600})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "rotate")
    assert s["rotation"] == 90.0


# ── Scroll / Swipe / Drag ──────────────────────────────────────────────────────

def test_scroll(client, warm_tree):
    """Scroll up (y decreases)."""
    r = client.post("/api/record/scroll", json={"x1": 200, "y1": 600, "x2": 200, "y2": 200, "duration": 600})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "scroll")
    assert "coords" in s


def test_swipe(client, warm_tree):
    """Swipe left."""
    r = client.post("/api/record/swipe", json={"x1": 300, "y1": 400, "x2": 100, "y2": 400, "duration": 400})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "swipe")
    assert "coords" in s


def test_drag(client, warm_tree):
    """Drag from one point to another."""
    r = client.post("/api/record/drag", json={"x1": 100, "y1": 300, "x2": 300, "y2": 300, "duration": 1000})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "drag")
    assert "coords" in s


# ── Text input ─────────────────────────────────────────────────────────────────

def test_type_text(client, warm_tree):
    r = client.post("/api/record/type_text", json={"text": "hello", "target_x": 200, "target_y": 400})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "type_text")
    assert s["text"] == "hello"


# ── System actions ─────────────────────────────────────────────────────────────

def test_home(client):
    r = client.post("/api/record/home")
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    assert_step(steps[0], "home")


def test_launch_app(client):
    bundle_id = "com.apple.mobilesafari"
    r = client.post("/api/record/launch_app", json={"bundle_id": bundle_id})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "launch_app")
    assert s["bundle_id"] == bundle_id


def test_terminate_app(client):
    bundle_id = "com.apple.mobilesafari"
    r = client.post("/api/record/terminate_app", json={"bundle_id": bundle_id})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "terminate_app")
    assert s["bundle_id"] == bundle_id


# ── Assertions / Verify ────────────────────────────────────────────────────────

def test_verify_visible(client, warm_tree):
    r = client.post("/api/record/verify_visible", json={"target_x": 200, "target_y": 400, "not_visible": False})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "verify_visible")
    assert "target" in s


def test_verify_not_visible(client, warm_tree):
    r = client.post("/api/record/verify_visible", json={"target_x": 200, "target_y": 400, "not_visible": True})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    assert_step(steps[0], "verify_not_visible")


def test_verify_get_text(client, warm_tree):
    r = client.post("/api/record/verify_get_text", json={"target_x": 200, "target_y": 400, "expected_text": "Hello"})
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "verify_get_text")
    assert s["expected_text"] == "Hello"


def test_verify_screenshot_gt(client, warm_tree):
    r = client.post("/api/record/verify_screenshot_gt", json={
        "target_x": 200, "target_y": 400,
        "screenshot_name": "my_gt",
        "bounds": {"x": 100, "y": 300, "w": 200, "h": 150},
    })
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "verify_screenshot_gt")
    assert s["screenshot_name"] == "my_gt"


def test_verify_screenshot_diff(client, warm_tree):
    r = client.post("/api/record/verify_screenshot_diff", json={
        "target_x": 200, "target_y": 400,
        "bounds": {"x": 100, "y": 300, "w": 200, "h": 150},
        "phase": "before",
        "expected_result": "same",
    })
    assert r.status_code == 200

    steps = get_steps(client)
    assert len(steps) == 1
    s = steps[0]
    assert_step(s, "verify_screenshot_diff")
    assert s["phase"] == "before"


# ── Multi-step + export ────────────────────────────────────────────────────────

def test_multi_step_export(client, warm_tree):
    """Record tap + long_press + verify_visible, then export and check output."""
    client.post("/api/record", json={"x": 200, "y": 400})
    client.post("/api/record/long_press", json={"x": 200, "y": 400, "duration": 1000})
    client.post("/api/record/verify_visible", json={"target_x": 200, "target_y": 400, "not_visible": False})

    steps = get_steps(client)
    assert len(steps) == 3
    assert steps[0]["action"] == "tap"
    assert steps[1]["action"] == "long_press"
    assert steps[2]["action"] == "verify_visible"

    # Export
    export_resp = client.post("/api/export", json={"case_name": "DemoTest"})
    assert export_resp.status_code == 200
    data = export_resp.json()

    assert "saved_paths" in data
    assert len(data["saved_paths"]) == 4  # .py (tests/), .py, .json, .html

    # Verify the generated .py code looks sane
    script = data["script"]
    assert "def test_" in script
    assert "actions.tap" in script
    assert "actions.long_press" in script
    assert "actions.verify_visible" in script
    assert "with step(" in script
    assert "assert True" in script
