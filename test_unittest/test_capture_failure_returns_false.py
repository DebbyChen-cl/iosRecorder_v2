"""Behaviour tests for the capture failure contract.

`capture_for_gt()` used to return its path unconditionally: when the device
produced no image the path was still queued and still truthy, so
`assert actions.capture_for_gt(...)` passed and the missing file only surfaced
much later inside `run_screenshot_comparisons()`.

It now returns the saved path on success (truthy — callers feed it into
`compare_with_gt(compare_path=...)`) and `False` when nothing was written, and
skips queueing in that case.

Runs against a stub driver — no device, no Appium server.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pytest"))

from driver.driver_actions import DriverActions  # noqa: E402

pytestmark = pytest.mark.unit

PNG_1x1 = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01"
    b"\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
)


class _StubDriver:
    """Minimal driver double: `writes` controls whether a file appears."""

    def __init__(self, writes=True, raises=False):
        self.writes = writes
        self.raises = raises
        self.capabilities = {}

    def save_screenshot(self, path):
        if self.raises:
            raise RuntimeError("WDA screenshot channel died")
        if self.writes:
            Path(path).write_bytes(PNG_1x1)
            return True
        return False

    def get_window_size(self):
        return {"width": 390, "height": 844}


@pytest.fixture
def actions_factory(tmp_path, monkeypatch):
    def make(**kw):
        a = DriverActions(_StubDriver(**kw))
        a.stability_check = False
        # Keep the WDA/MJPEG side channels out of play so the full-screen
        # fallback is the only path that can produce a file.
        monkeypatch.setattr(a, "_fetch_wda_screenshot_png", lambda: None)
        return a
    return make


def test_capture_for_gt_returns_path_and_queues_on_success(actions_factory, tmp_path):
    actions = actions_factory(writes=True)
    result = actions.capture_for_gt("shot.png", compare_folder=str(tmp_path))

    assert result, "a successful capture must be truthy so `assert` passes"
    assert Path(result).exists()
    assert len(actions._gt_compare_queue) == 1
    assert actions._gt_compare_queue[0][1] == result


def test_capture_for_gt_returns_false_when_nothing_written(actions_factory, tmp_path):
    actions = actions_factory(writes=False)
    result = actions.capture_for_gt("shot.png", compare_folder=str(tmp_path))

    assert result is False, "a failed capture must be falsy so `assert` catches it"
    assert actions._gt_compare_queue == [], (
        "a capture that produced no file must not be queued — otherwise "
        "run_screenshot_comparisons() later trips over a missing path"
    )


def test_capture_for_gt_returns_false_when_driver_raises(actions_factory, tmp_path):
    actions = actions_factory(raises=True)
    result = actions.capture_for_gt("shot.png", compare_folder=str(tmp_path))

    assert result is False
    assert actions._gt_compare_queue == []


def test_capture_for_gt_returns_false_on_empty_file(actions_factory, tmp_path):
    """A zero-byte file is a failed capture, not a successful one."""
    actions = actions_factory(writes=True)
    actions.driver.save_screenshot = lambda path: Path(path).write_bytes(b"") or True

    result = actions.capture_for_gt("shot.png", compare_folder=str(tmp_path))

    assert result is False
    assert actions._gt_compare_queue == []


def test_take_screenshot_reports_failure(actions_factory, tmp_path):
    ok = actions_factory(writes=True).take_screenshot(str(tmp_path / "ok.png"))
    bad = actions_factory(writes=False).take_screenshot(str(tmp_path / "bad.png"))

    assert ok is True
    assert bad is False
