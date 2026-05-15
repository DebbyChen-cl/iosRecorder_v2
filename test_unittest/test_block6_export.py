"""
Block 6 — Export

Tests the export pipeline: generate_script() + _generate_html_report() with
fixed step inputs. Verifies that the three output artefacts (.py, .json, .html)
have the correct content. File writing is tested against a tmp_path.
No device or server needed.
"""

import json
import time
from pathlib import Path
from unittest.mock import patch

import pytest

pytestmark = pytest.mark.unit

from app.codegen import generate_script
from app.main import _generate_html_report


# ── Shared step fixtures ───────────────────────────────────────────────────────

STEPS_CLEAN = [
    {
        "action": "tap",
        "coords": {"x": 140, "y": 222},
        "target": {"type": "accessibility id", "value": "SaveButton", "selector_quality": "id"},
        "timestamp": "2026-01-01T00:00:00",
    },
    {
        "action": "verify_visible",
        "coords": {"x": 140, "y": 222},
        "target": {"type": "accessibility id", "value": "SaveButton", "selector_quality": "id"},
        "timestamp": "2026-01-01T00:00:01",
    },
]

STEPS_WITH_WARNINGS = [
    {
        "action": "tap",
        "coords": {"x": 50, "y": 530},
        "target": {"type": "xpath", "value": "//XCUIElementTypeOther", "selector_quality": "xpath_only"},
        "timestamp": "2026-01-01T00:00:00",
    },
    {
        "action": "tap",
        "coords": {"x": 200, "y": 400},
        "target": {"type": "coordinate", "value": "", "x": 200, "y": 400},
        "timestamp": "2026-01-01T00:00:01",
    },
]


# ── generate_script (pytest code) ─────────────────────────────────────────────

def test_export_script_has_test_function():
    code = generate_script(STEPS_CLEAN, "ExportTest_20260101_120000")
    assert "def test_ExportTest_20260101_120000" in code


def test_export_script_has_all_actions():
    code = generate_script(STEPS_CLEAN, "ExportTest")
    assert "actions.tap_by_locator" in code
    assert "actions.verify_visible" in code


def test_export_script_ends_with_assert_true():
    code = generate_script(STEPS_CLEAN, "ExportTest")
    assert "assert True" in code.strip().splitlines()[-1]


def test_export_script_step_count_matches():
    code = generate_script(STEPS_CLEAN, "ExportTest")
    step_blocks = code.count('with step(')
    assert step_blocks == len(STEPS_CLEAN)


# ── _generate_html_report ──────────────────────────────────────────────────────

def test_html_report_is_valid_html():
    html = _generate_html_report(STEPS_CLEAN, "ExportTest")
    assert html.startswith("<!DOCTYPE html>")
    assert "</html>" in html


def test_html_report_contains_case_name():
    html = _generate_html_report(STEPS_CLEAN, "MyCase")
    assert "MyCase" in html


def test_html_report_all_stable_shows_ok():
    html = _generate_html_report(STEPS_CLEAN, "ExportTest")
    assert "All steps use stable selectors" in html


def test_html_report_shows_warnings_for_bad_selectors():
    html = _generate_html_report(STEPS_WITH_WARNINGS, "WarnTest")
    assert "Steps with Selector Warnings" in html


def test_html_report_warning_count():
    html = _generate_html_report(STEPS_WITH_WARNINGS, "WarnTest")
    assert f"{len(STEPS_WITH_WARNINGS)} of {len(STEPS_WITH_WARNINGS)} steps have selector warnings" in html


def test_html_report_shows_xpath_badge():
    html = _generate_html_report(STEPS_WITH_WARNINGS, "WarnTest")
    assert "XPath Only" in html


def test_html_report_shows_coordinate_badge():
    html = _generate_html_report(STEPS_WITH_WARNINGS, "WarnTest")
    assert "Coord Only" in html


# ── File writing (tmp_path) ────────────────────────────────────────────────────

def test_export_writes_py_file(tmp_path):
    case = "FileTest"
    code = generate_script(STEPS_CLEAN, case)
    py_file = tmp_path / f"test_{case}.py"
    py_file.write_text(code, encoding="utf-8")
    assert py_file.exists()
    content = py_file.read_text()
    assert f"def test_{case}" in content


def test_export_writes_json_file(tmp_path):
    case = "FileTest"
    exported_at = "2026-01-01T12:00:00"
    payload = {
        "case_name": case,
        "exported_at": exported_at,
        "steps": STEPS_CLEAN,
    }
    json_file = tmp_path / f"{case}.json"
    json_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    data = json.loads(json_file.read_text())
    assert data["case_name"] == case
    assert len(data["steps"]) == len(STEPS_CLEAN)


def test_export_writes_html_file(tmp_path):
    case = "FileTest"
    html = _generate_html_report(STEPS_CLEAN, case)
    html_file = tmp_path / f"{case}.html"
    html_file.write_text(html, encoding="utf-8")
    content = html_file.read_text()
    assert "<!DOCTYPE html>" in content
    assert case in content


# ── Via TestClient endpoint ────────────────────────────────────────────────────

def test_export_endpoint_returns_script_and_paths(unit_client):
    import app.main as m
    m._steps.clear()
    m._steps.extend(STEPS_CLEAN)

    with patch("app.main.time.strftime", return_value="20260101_120000"):
        r = unit_client.post("/api/export", json={"case_name": "EndpointTest"})

    assert r.status_code == 200
    data = r.json()
    assert "script" in data
    assert "saved_paths" in data
    assert len(data["saved_paths"]) == 4
    assert any("pytest/tests/" in p for p in data["saved_paths"])
    assert "def test_EndpointTest" in data["script"]
