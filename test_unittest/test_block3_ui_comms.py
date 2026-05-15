"""
Block 3 — UI Screen Test: Frontend → Backend coordinate passthrough

Verifies that coordinates and action types sent to record endpoints are stored
exactly as received. Uses FastAPI TestClient with WDA and background tasks
mocked out via the unit_client fixture (see conftest.py). No device needed.
"""

import pytest

pytestmark = pytest.mark.unit

import app.main as m


def get_steps(client):
    resp = client.get("/api/steps")
    assert resp.status_code == 200
    return resp.json()["steps"]


def clear(client):
    client.delete("/api/steps")


# ── tap ────────────────────────────────────────────────────────────────────────

def test_tap_coords_passthrough(unit_client):
    r = unit_client.post("/api/record", json={"x": 140, "y": 222})
    assert r.status_code == 200
    steps = get_steps(unit_client)
    assert len(steps) == 1
    s = steps[0]
    assert s["action"] == "tap"
    assert s["coords"]["x"] == 140
    assert s["coords"]["y"] == 222


def test_tap_target_present(unit_client):
    unit_client.post("/api/record", json={"x": 140, "y": 222})
    s = get_steps(unit_client)[0]
    assert "target" in s
    assert s["target"]["type"] in ("accessibility id", "name", "xpath", "coordinate")


def test_tap_resolves_known_element(unit_client):
    unit_client.post("/api/record", json={"x": 140, "y": 222})
    s = get_steps(unit_client)[0]
    assert s["target"]["value"] == "SaveButton"


# ── double_tap ─────────────────────────────────────────────────────────────────

def test_double_tap_recorded(unit_client):
    r = unit_client.post("/api/record/double_tap", json={"x": 240, "y": 222})
    assert r.status_code == 200
    s = get_steps(unit_client)[0]
    assert s["action"] == "double_tap"
    assert s["coords"]["x"] == 240
    assert s["coords"]["y"] == 222


# ── long_press ─────────────────────────────────────────────────────────────────

def test_long_press_recorded_with_duration(unit_client):
    r = unit_client.post("/api/record/long_press", json={"x": 140, "y": 222, "duration": 1500})
    assert r.status_code == 200
    s = get_steps(unit_client)[0]
    assert s["action"] == "long_press"
    assert s["duration"] == 1500


# ── home (no element needed) ───────────────────────────────────────────────────

def test_home_recorded(unit_client):
    r = unit_client.post("/api/record/home")
    assert r.status_code == 200
    s = get_steps(unit_client)[0]
    assert s["action"] == "home"


# ── launch_app / terminate_app ─────────────────────────────────────────────────

def test_launch_app_recorded(unit_client):
    r = unit_client.post("/api/record/launch_app", json={"bundle_id": "com.apple.mobilesafari"})
    assert r.status_code == 200
    s = get_steps(unit_client)[0]
    assert s["action"] == "launch_app"
    assert s["bundle_id"] == "com.apple.mobilesafari"


def test_terminate_app_recorded(unit_client):
    r = unit_client.post("/api/record/terminate_app", json={"bundle_id": "com.apple.mobilesafari"})
    assert r.status_code == 200
    s = get_steps(unit_client)[0]
    assert s["action"] == "terminate_app"
    assert s["bundle_id"] == "com.apple.mobilesafari"


# ── verify_visible ─────────────────────────────────────────────────────────────

def test_verify_visible_recorded(unit_client):
    r = unit_client.post("/api/record/verify_visible", json={"target_x": 140, "target_y": 222, "not_visible": False})
    assert r.status_code == 200
    s = get_steps(unit_client)[0]
    assert s["action"] == "verify_visible"


def test_verify_not_visible_recorded(unit_client):
    r = unit_client.post("/api/record/verify_visible", json={"target_x": 140, "target_y": 222, "not_visible": True})
    assert r.status_code == 200
    s = get_steps(unit_client)[0]
    assert s["action"] == "verify_not_visible"


# ── multi-step order preserved ─────────────────────────────────────────────────

def test_multi_step_order_preserved(unit_client):
    unit_client.post("/api/record", json={"x": 140, "y": 222})
    unit_client.post("/api/record/home")
    unit_client.post("/api/record/launch_app", json={"bundle_id": "com.example.app"})
    steps = get_steps(unit_client)
    assert len(steps) == 3
    assert steps[0]["action"] == "tap"
    assert steps[1]["action"] == "home"
    assert steps[2]["action"] == "launch_app"


# ── steps isolated between tests ──────────────────────────────────────────────

def test_steps_start_empty(unit_client):
    steps = get_steps(unit_client)
    assert steps == []
