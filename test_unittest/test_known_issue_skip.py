"""Unit tests for the known-issue lane in `pytest/auto_healing.py`.

A case listed in `pytest/known_issue.json` whose failure log is identical to the
previous run must not enter auto-healing: no immediate retry, no Phase 2. The
first failure — and any failure with a *different* log — still heals normally.

No device, no Appium and no pytest session: `check_known_issue()` only needs an
item-like object with `fspath`/`originalname` plus the failure report text.
"""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pytest"))

import auto_healing  # noqa: E402

pytestmark = pytest.mark.unit


class FakeItem:
    """The two attributes `check_known_issue` reads off a pytest item."""

    def __init__(self, path, name):
        self.fspath = path
        self.originalname = name
        self.name = name


LOCATOR_FAIL = """\
self = <driver.driver_actions.DriverActions object at 0x10f2c3d40>

    with step("[Action] tap Bokeh"):
>       assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, "bokehBtn")
E       selenium.common.exceptions.TimeoutException: Message: element not found: bokehBtn
E       Session ID: 4b1f2c88-9a71-4f2e-9a2f-1f0a2b3c4d5e

tests/test_00133_main_05_17_03_NeedRDLocator_BokehOnPreview.py:41: TimeoutException
"""

# Same failure, second run: different session id, different object address,
# different screenshot timestamp — all of it noise that must be normalized away.
LOCATOR_FAIL_RERUN = LOCATOR_FAIL.replace("0x10f2c3d40", "0x7fbe19c04a10").replace(
    "4b1f2c88-9a71-4f2e-9a2f-1f0a2b3c4d5e", "0c9d8e77-1234-4aaa-bbbb-556677889900"
)

DIFFERENT_FAIL = """\
    with step("[Verify] preview updated"):
>       assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "valueLabel", "50")
E       AssertionError: text mismatch: expected '50', got '0'

tests/test_00133_main_05_17_03_NeedRDLocator_BokehOnPreview.py:52: AssertionError
"""


@pytest.fixture
def known_issue_file(tmp_path, monkeypatch):
    """Point auto_healing at a throwaway known_issue.json and return its path."""
    path = tmp_path / "known_issue.json"
    path.write_text(
        json.dumps(
            [
                {
                    "file_name": "test_00133_main_05_17_03_NeedRDLocator_BokehOnPreview.py",
                    "test_name": "test_00133_main_05_17_03",
                    "error_reason": "NeedRDLocator_BokehOnPreview",
                    "bug_code": "PHD-1234",
                }
            ],
            indent=2,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(auto_healing, "KNOWN_ISSUE_PATH", str(path))
    return path


def _entry(path):
    return json.loads(path.read_text(encoding="utf-8"))[0]


def _item(name="test_00133_main_05_17_03",
          file_name="test_00133_main_05_17_03_NeedRDLocator_BokehOnPreview.py"):
    return FakeItem(f"/repo/pytest/tests/{file_name}", name)


def test_unlisted_test_is_not_a_known_issue(known_issue_file):
    assert auto_healing.check_known_issue(_item("test_00001_main_05_01_06",
                                                "test_00001_main_05_01_06.py"),
                                          LOCATOR_FAIL) is None


def test_first_failure_records_signature_but_does_not_match(known_issue_file):
    result = auto_healing.check_known_issue(_item(), LOCATOR_FAIL, run_id="20260811120000")

    assert result is not None
    assert result["matched"] is False          # nothing to compare against yet → heals
    assert result["error_reason"] == "NeedRDLocator_BokehOnPreview"
    assert result["bug_code"] == "PHD-1234"

    stored = _entry(known_issue_file)
    assert stored["last_fail"]["signature"] == result["signature"]
    assert stored["last_fail"]["run_id"] == "20260811120000"
    assert stored["last_fail"]["repeat_count"] == 1
    # The four fields the human maintains are untouched.
    assert stored["bug_code"] == "PHD-1234"
    assert stored["error_reason"] == "NeedRDLocator_BokehOnPreview"


def test_same_failure_next_run_matches_despite_session_noise(known_issue_file):
    auto_healing.check_known_issue(_item(), LOCATOR_FAIL)
    result = auto_healing.check_known_issue(_item(), LOCATOR_FAIL_RERUN)

    assert result["matched"] is True
    assert _entry(known_issue_file)["last_fail"]["repeat_count"] == 2


def test_changed_failure_does_not_match_and_replaces_signature(known_issue_file):
    first = auto_healing.check_known_issue(_item(), LOCATOR_FAIL)
    second = auto_healing.check_known_issue(_item(), DIFFERENT_FAIL)

    assert second["matched"] is False          # new symptom → heals again
    assert second["signature"] != first["signature"]
    stored = _entry(known_issue_file)
    assert stored["last_fail"]["signature"] == second["signature"]
    assert stored["last_fail"]["repeat_count"] == 1


def test_renamed_file_stops_matching(known_issue_file):
    """Dropping the error suffix from the file name retires the known issue.

    The test function keeps its name, so file-name matching is what makes the
    fixed case heal normally again instead of being skipped forever.
    """
    auto_healing.check_known_issue(_item(), LOCATOR_FAIL)
    fixed = _item(file_name="test_00133_main_05_17_03.py")

    assert auto_healing.check_known_issue(fixed, LOCATOR_FAIL_RERUN) is None


def test_empty_report_never_matches(known_issue_file):
    """An unfingerprintable failure must not compare equal to a stored one."""
    auto_healing.check_known_issue(_item(), LOCATOR_FAIL)
    result = auto_healing.check_known_issue(_item(), "")

    assert result["signature"] is None
    assert result["matched"] is False


def test_retry_recovery_rolls_the_signature_back(known_issue_file):
    """A known issue that passes on retry must not leave a stored signature.

    Otherwise the next identical crash would be skipped instead of retried, and a
    case that used to end green would end red just for being on the list.
    """
    first = auto_healing.check_known_issue(_item(), LOCATOR_FAIL)
    auto_healing.forget_known_issue_failure(_item(), first["previous_last_fail"])
    assert "last_fail" not in _entry(known_issue_file)

    # Second run of the same failure therefore still heals rather than skipping.
    assert auto_healing.check_known_issue(_item(), LOCATOR_FAIL_RERUN)["matched"] is False


def test_retry_recovery_restores_the_earlier_signature(known_issue_file):
    auto_healing.check_known_issue(_item(), LOCATOR_FAIL)
    second = auto_healing.check_known_issue(_item(), DIFFERENT_FAIL)
    auto_healing.forget_known_issue_failure(_item(), second["previous_last_fail"])

    stored = _entry(known_issue_file)["last_fail"]
    assert stored["signature"] == second["previous_signature"]


def test_broken_known_issue_file_is_survivable(tmp_path, monkeypatch):
    bad = tmp_path / "known_issue.json"
    bad.write_text("{ not json", encoding="utf-8")
    monkeypatch.setattr(auto_healing, "KNOWN_ISSUE_PATH", str(bad))

    assert auto_healing.check_known_issue(_item(), LOCATOR_FAIL) is None


def test_missing_known_issue_file_is_survivable(tmp_path, monkeypatch):
    monkeypatch.setattr(auto_healing, "KNOWN_ISSUE_PATH", str(tmp_path / "nope.json"))

    assert auto_healing.check_known_issue(_item(), LOCATOR_FAIL) is None


def test_real_known_issue_file_is_in_sync_with_the_test_files():
    """The checked-in known_issue.json must match the test file names.

    Entries are matched on file name, so a rename silently breaks the link: a
    stale entry protects nothing, and a newly suffixed file is not protected at
    all. `pytest/refresh_known_issue.py` rebuilds the list, keeping `bug_code`
    and the recorded `last_fail` signatures.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pytest"))
    import refresh_known_issue

    assert refresh_known_issue.main(["--check"]) == 0, (
        "known_issue.json is out of date — run: python3 pytest/refresh_known_issue.py"
    )
