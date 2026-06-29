import json
from pathlib import Path

import pytest

from app.cli import run_cli

pytestmark = pytest.mark.unit


def _write_steps(path: Path, steps):
    path.write_text(json.dumps({"case_name": "DemoCase", "steps": steps}, ensure_ascii=False, indent=2), encoding="utf-8")


def test_cli_validate_steps_ok(tmp_path: Path):
    steps_file = tmp_path / "steps.json"
    _write_steps(
        steps_file,
        [
            {
                "action": "tap",
                "coords": {"x": 100, "y": 200},
                "target": {"type": "xpath", "value": "//XCUIElementTypeButton[@name='OK']", "selector_quality": "xpath_only"},
            }
        ],
    )

    code, payload = run_cli(["validate-steps", "--input", str(steps_file)])

    assert code == 0
    assert payload["ok"] is True
    assert payload["step_count"] == 1
    assert payload["warning_count"] == 1


def test_cli_validate_steps_unknown_action(tmp_path: Path):
    steps_file = tmp_path / "steps.json"
    _write_steps(steps_file, [{"action": "unknown_action"}])

    code, payload = run_cli(["validate-steps", "--input", str(steps_file)])

    assert code == 2
    assert payload["ok"] is False
    assert payload["error"]["code"] == "STEP_VALIDATION_FAILED"


def test_cli_generate_test_writes_file(tmp_path: Path):
    steps_file = tmp_path / "steps.json"
    output_file = tmp_path / "test_generated.py"
    _write_steps(steps_file, [{"action": "home"}])

    code, payload = run_cli(
        [
            "generate-test",
            "--input",
            str(steps_file),
            "--case-name",
            "MyCase",
            "--output",
            str(output_file),
        ]
    )

    assert code == 0
    assert payload["ok"] is True
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert '@pytest.mark.name("MyCase")' in content
    assert "actions.press_home()" in content


def test_cli_export_bundle_writes_artifacts(tmp_path: Path):
    steps_file = tmp_path / "steps.json"
    export_dir = tmp_path / "export"
    tests_dir = tmp_path / "pytest_tests"
    _write_steps(steps_file, [{"action": "home"}])

    code, payload = run_cli(
        [
            "export-bundle",
            "--input",
            str(steps_file),
            "--case-name",
            "BundleCase",
            "--export-dir",
            str(export_dir),
            "--tests-dir",
            str(tests_dir),
            "--no-append-timestamp",
        ]
    )

    assert code == 0
    assert payload["ok"] is True
    saved = payload["saved_paths"]
    assert len(saved) == 4
    for p in saved:
        assert Path(p).exists()


def test_cli_server_status_with_mock(monkeypatch):
    class DummyResponse:
        status_code = 200

        @staticmethod
        def json():
            return {"connected": True, "wda_url": "http://localhost:8100"}

    class DummyClient:
        def __init__(self, base_url, timeout):
            self.base_url = base_url
            self.timeout = timeout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def get(self, path):
            assert path == "/api/status"
            return DummyResponse()

    monkeypatch.setattr("app.cli.httpx.Client", DummyClient)

    code, payload = run_cli(["server-status", "--base-url", "http://localhost:9999"])
    assert code == 0
    assert payload["ok"] is True
    assert payload["response"]["connected"] is True


def test_cli_server_record_action_tap_payload_json(monkeypatch):
    calls = []

    class DummyResponse:
        status_code = 200

        @staticmethod
        def json():
            return {"ok": True}

    class DummyClient:
        def __init__(self, base_url, timeout):
            self.base_url = base_url
            self.timeout = timeout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def post(self, path, json):
            calls.append((path, json))
            return DummyResponse()

    monkeypatch.setattr("app.cli.httpx.Client", DummyClient)

    code, payload = run_cli(
        [
            "server-record-action",
            "--action",
            "tap",
            "--payload-json",
            '{"x": 120, "y": 240}',
        ]
    )

    assert code == 0
    assert payload["ok"] is True
    assert payload["endpoint"] == "/api/record"
    assert calls == [("/api/record", {"x": 120, "y": 240})]


def test_cli_server_record_action_verify_tap_screenshot_diff(monkeypatch):
    calls = []

    class DummyResponse:
        status_code = 200

        @staticmethod
        def json():
            return {"ok": True}

    class DummyClient:
        def __init__(self, base_url, timeout):
            self.base_url = base_url
            self.timeout = timeout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def post(self, path, json):
            calls.append((path, json))
            return DummyResponse()

    monkeypatch.setattr("app.cli.httpx.Client", DummyClient)

    code, payload = run_cli(
        [
            "server-record-action",
            "--action",
            "verify_tap_screenshot_diff",
            "--payload-json",
            '{"target_x": 120, "target_y": 240, "target_bounds": {"x": 100, "y": 200, "w": 80, "h": 60}, "action_x": 60, "action_y": 90, "wait_seconds": 2.0, "expected_result": "different", "screenshot_name": "Demo_TapDiff"}',
        ]
    )

    assert code == 0
    assert payload["ok"] is True
    assert payload["endpoint"] == "/api/record/verify_tap_screenshot_diff"
    assert calls[0][0] == "/api/record/verify_tap_screenshot_diff"


def test_cli_server_export_writes_response_file(monkeypatch, tmp_path: Path):
    class DummyResponse:
        status_code = 200

        @staticmethod
        def json():
            return {"saved_paths": ["pytest/tests/test_case.py"]}

    class DummyClient:
        def __init__(self, base_url, timeout):
            self.base_url = base_url
            self.timeout = timeout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def post(self, path, json):
            assert path == "/api/export"
            assert json == {"case_name": "DemoCase"}
            return DummyResponse()

    monkeypatch.setattr("app.cli.httpx.Client", DummyClient)

    out = tmp_path / "export_response.json"
    code, payload = run_cli(["server-export", "--case-name", "DemoCase", "--output", str(out)])

    assert code == 0
    assert payload["ok"] is True
    assert out.exists()
    saved = json.loads(out.read_text(encoding="utf-8"))
    assert saved["saved_paths"] == ["pytest/tests/test_case.py"]


def test_cli_server_vision_snapshot_writes_file(monkeypatch, tmp_path: Path):
    class DummyResponse:
        def __init__(self, body):
            self.status_code = 200
            self._body = body

        def json(self):
            return self._body

    class DummyClient:
        def __init__(self, base_url, timeout):
            self.base_url = base_url
            self.timeout = timeout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def get(self, path):
            if path == "/api/status":
                return DummyResponse({"connected": True})
            if path == "/api/tree":
                return DummyResponse({"elements": [{"tag": "XCUIElementTypeButton"}]})
            if path == "/api/frame?include_data=false":
                return DummyResponse({"has_frame": True, "image_base64": ""})
            raise AssertionError(f"unexpected GET path: {path}")

    monkeypatch.setattr("app.cli.httpx.Client", DummyClient)

    out = tmp_path / "snapshot.json"
    code, payload = run_cli(["server-vision-snapshot", "--output", str(out)])
    assert code == 0
    assert payload["ok"] is True
    assert payload["has_tree"] is True
    assert payload["has_frame"] is True
    assert out.exists()


def test_cli_server_vision_execute_live(monkeypatch):
    calls = []

    class DummyResponse:
        status_code = 200

        @staticmethod
        def json():
            return {"ok": True}

    class DummyClient:
        def __init__(self, base_url, timeout):
            self.base_url = base_url
            self.timeout = timeout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def post(self, path, json):
            calls.append((path, json))
            return DummyResponse()

    monkeypatch.setattr("app.cli.httpx.Client", DummyClient)

    code, payload = run_cli(
        [
            "server-vision-execute",
            "--action",
            "tap",
            "--mode",
            "live",
            "--payload-json",
            '{"x": 10, "y": 20}',
        ]
    )
    assert code == 0
    assert payload["endpoint"] == "/api/tap"
    assert calls == [("/api/tap", {"x": 10, "y": 20})]


def test_cli_server_vision_loop_plan(monkeypatch, tmp_path: Path):
    class DummyResponse:
        def __init__(self, body):
            self.status_code = 200
            self._body = body

        def json(self):
            return self._body

    class DummyClient:
        def __init__(self, base_url, timeout):
            self.base_url = base_url
            self.timeout = timeout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def get(self, path):
            if path == "/api/status":
                return DummyResponse({"connected": True})
            if path == "/api/tree":
                return DummyResponse({"elements": []})
            if path == "/api/frame?include_data=false":
                return DummyResponse({"has_frame": True, "image_base64": ""})
            raise AssertionError(f"unexpected GET path: {path}")

        def post(self, path, json):
            assert path == "/api/record"
            assert json == {"x": 1, "y": 2}
            return DummyResponse({"ok": True})

    monkeypatch.setattr("app.cli.httpx.Client", DummyClient)

    plan_file = tmp_path / "plan.json"
    plan_file.write_text(
        json.dumps(
            {
                "steps": [
                    {"type": "snapshot", "include_frame_data": False},
                    {"type": "action", "action": "tap", "mode": "record", "payload": {"x": 1, "y": 2}},
                ]
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    out = tmp_path / "loop_result.json"
    code, payload = run_cli(["server-vision-loop", "--plan-file", str(plan_file), "--output", str(out)])
    assert code == 0
    assert payload["ok"] is True
    assert payload["plan_step_count"] == 2
    assert out.exists()
