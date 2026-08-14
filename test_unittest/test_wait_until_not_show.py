"""Unit tests for the `wait_until_not_show` verification.

The step waits for a transient element (progress bar, rendering spinner) to
appear and then go away again, with the two waits counted **separately**:

  * appear budget (default 5 s)      — never showed up  → False, right away
  * disappear budget (default 20 min) — still shown at the end → False

Both outcomes are returned rather than raised, so the generated
``assert actions.wait_until_not_show(...)`` is what fails the step.

The driver tests script presence directly, so they need neither Appium nor a
device; the recorder test drives the endpoint through the mocked `unit_client`.
"""

import ast
import sys
import time
from pathlib import Path

import pytest
from app.codegen import generate_script

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pytest"))

from driver.driver_actions import DriverActions  # noqa: E402

pytestmark = pytest.mark.unit


class ScriptedPresence(DriverActions):
    """DriverActions whose element presence follows a scripted sequence.

    Each entry is consumed by one probe; the last entry repeats forever, so a
    trailing ``True`` means "never goes away".
    """

    def __init__(self, presence):
        super().__init__(driver=None)
        self._presence = list(presence)
        self.probes = 0

    def is_element_present(self, by, value, timeout=3):  # noqa: D102 — override
        present = self._presence[min(self.probes, len(self._presence) - 1)]
        self.probes += 1
        return present


def _fast(presence):
    return ScriptedPresence(presence)


# ── Driver behaviour ──────────────────────────────────────────────────────────

def test_returns_false_when_element_never_appears():
    """Nothing to wait for — fail on the appear budget, not the long one."""
    actions = _fast([False])
    started = time.monotonic()

    result = actions.wait_until_not_show(
        "accessibility id", "Rendering",
        appear_timeout=0.05, disappear_timeout=600, poll_interval=0.01,
    )

    assert result is False
    # The 10-minute budget must not have been touched.
    assert time.monotonic() - started < 1.0
    assert actions.probes == 1, "only the appear probe should have run"


def test_returns_true_when_element_is_already_gone_if_explicitly_allowed():
    """A completed transient operation may be observed after its OSD vanishes."""
    actions = _fast([False])

    result = actions.wait_until_not_show(
        "accessibility id", "Downloading",
        appear_timeout=0.05, disappear_timeout=600, poll_interval=0.01,
        allow_already_gone=True,
    )

    assert result is True
    assert actions.probes == 1, "do not spend the long disappearance budget"


def test_returns_true_once_the_element_disappears():
    actions = _fast([True, True, True, False])

    result = actions.wait_until_not_show(
        "accessibility id", "Rendering",
        appear_timeout=1, disappear_timeout=5, poll_interval=0.01,
    )

    assert result is True


def test_returns_false_when_element_never_disappears():
    """Still on screen when the disappear budget runs out."""
    actions = _fast([True])
    started = time.monotonic()

    result = actions.wait_until_not_show(
        "accessibility id", "Rendering",
        appear_timeout=1, disappear_timeout=0.2, poll_interval=0.01,
    )

    assert result is False
    assert time.monotonic() - started >= 0.2, "disappear budget was not waited out"
    assert actions.probes > 1, "the disappear phase should keep probing"


def test_budgets_are_counted_separately():
    """A tiny appear budget must not shorten the disappear wait."""
    actions = _fast([True, True, True, True, False])

    result = actions.wait_until_not_show(
        "accessibility id", "Rendering",
        appear_timeout=0.01, disappear_timeout=5, poll_interval=0.01,
    )

    assert result is True
    assert actions.probes == 5


def test_never_raises_so_the_generated_assert_is_what_fails():
    actions = _fast([False])
    assert actions.wait_until_not_show(
        "xpath", "//XCUIElementTypeActivityIndicator",
        appear_timeout=0.01, disappear_timeout=0.01, poll_interval=0.01,
    ) is False


# ── Codegen ───────────────────────────────────────────────────────────────────

def test_codegen_emits_asserted_call_with_both_timeouts():
    code = generate_script([{
        "action": "wait_until_not_show",
        "target": {"type": "accessibility id", "value": "Rendering"},
        "appear_timeout": 5.0,
        "disappear_timeout": 1200,
    }], "wait_gone")

    ast.parse(code)  # must stay valid Python
    assert "assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Rendering', " \
           "appear_timeout=5, disappear_timeout=1200)" in code
    assert '[Verify] Rendering disappears within 1200s' in code


def test_codegen_keeps_custom_timeouts():
    code = generate_script([{
        "action": "wait_until_not_show",
        "target": {"type": "name", "value": "Exporting…"},
        "appear_timeout": 2.5,
        "disappear_timeout": 90,
    }], "wait_gone")

    assert "appear_timeout=2.5, disappear_timeout=90" in code


def test_codegen_falls_back_to_defaults_when_timeouts_missing():
    code = generate_script([{
        "action": "wait_until_not_show",
        "target": {"type": "accessibility id", "value": "Rendering"},
    }], "wait_gone")

    assert "appear_timeout=5, disappear_timeout=1200" in code


def test_codegen_asserts_false_without_a_locator():
    code = generate_script([{
        "action": "wait_until_not_show",
        "coords": {"x": 10, "y": 20},
    }], "wait_gone")

    tree = ast.parse(code)
    assert any(
        isinstance(node, ast.Assert)
        and isinstance(node.test, ast.Constant)
        and node.test.value is False
        for node in ast.walk(tree)
    ), "a step with no locator must not silently pass"


# ── Recorder endpoint ─────────────────────────────────────────────────────────

def test_record_endpoint_stores_target_and_both_timeouts(unit_client):
    import app.main as m

    resp = unit_client.post("/api/record/wait_until_not_show", json={
        "target_x": 140, "target_y": 222,
        "appear_timeout": 5, "disappear_timeout": 1200,
    })

    assert resp.status_code == 200
    step = m._steps[-1]
    assert step["action"] == "wait_until_not_show"
    assert step["target"] == {
        "type": "accessibility id", "value": "SaveButton", "selector_quality": "id",
        "bounds": {"x": 100, "y": 200, "w": 80, "h": 44},
    }
    assert step["appear_timeout"] == 5
    assert step["disappear_timeout"] == 1200


def test_record_endpoint_prefers_frontend_resolved_selector(unit_client):
    import app.main as m

    resp = unit_client.post("/api/record/wait_until_not_show", json={
        "target_x": 999, "target_y": 999,
        "target_type": "accessibility id", "target_value": "Rendering",
        "target_selector_quality": "id",
    })

    assert resp.status_code == 200
    step = m._steps[-1]
    assert step["target"]["value"] == "Rendering"
    # Defaults come from the request model when the UI omits them.
    assert step["appear_timeout"] == 5.0
    assert step["disappear_timeout"] == 1200.0
