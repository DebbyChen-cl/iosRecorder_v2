"""Unit tests for verify_text's numeric tolerance.

A recorded slider drag stores a finger coordinate, and on these controls one unit
of slider travel is well under a logical point — replaying the same end
coordinate was measured on device to land on 50, 51 or 52 depending on where the
press hit the thumb.  An exact string compare of the slider readout therefore
fails at random even when the drag worked, so the ids listed in
``config.TEXT_NUMERIC_TOLERANCE`` are compared numerically instead.

Fake element / driver: no Appium, no device.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pytest"))

from driver.driver_actions import DriverActions  # noqa: E402

pytestmark = pytest.mark.unit


class FakeElement:
    def __init__(self, text):
        self._text = text
        self.text = ""

    def get_attribute(self, name):
        return self._text if name == "value" else None

    def find_element(self, *_a, **_kw):
        raise RuntimeError("no relatives")

    def find_elements(self, *_a, **_kw):
        return []


def _actions(actual, tolerance_table=None):
    actions = DriverActions(driver=None)
    actions.stability_check = False
    # Pinned rather than inherited from config.py: that number is a device-tuning
    # knob, and these tests are about the comparison logic, not its current value.
    actions.text_numeric_tolerance = (
        {"valueLabel": 2} if tolerance_table is None else tolerance_table
    )
    actions.find_element = lambda *a, **kw: FakeElement(actual)
    return actions


def _verify(actual, expected, tolerance_table=None, **kwargs):
    return _actions(actual, tolerance_table).verify_text(
        "accessibility id", "valueLabel", expected, **kwargs
    )


def test_table_tolerance_accepts_a_two_unit_drift():
    """The exact case observed on device: drag landed on 52, recorded 50."""
    assert _verify("52", "50") is True


def test_table_tolerance_still_fails_a_real_miss():
    with pytest.raises(AssertionError) as exc:
        _verify("55", "50")
    assert "±2" in str(exc.value)


def test_the_table_is_seeded_from_config():
    """Wiring check — the number itself is tuned in config.py, not asserted here."""
    assert "valueLabel" in DriverActions(driver=None).text_numeric_tolerance


def test_negative_slider_values_compare_numerically():
    assert _verify("-98", "-100") is True


def test_percent_suffix_and_decimal_comma_parse():
    assert _verify("51 %", "50") is True
    assert _verify("50,5", "50") is True


def test_an_unlisted_element_id_stays_an_exact_match():
    actions = _actions("52")
    with pytest.raises(AssertionError):
        actions.verify_text("accessibility id", "photoCount", "50")


def test_explicit_zero_tolerance_forces_an_exact_match():
    with pytest.raises(AssertionError):
        _verify("52", "50", tolerance=0)


def test_explicit_tolerance_overrides_the_table():
    assert _verify("57", "50", tolerance=10) is True


def test_non_numeric_text_is_never_compared_loosely():
    """A tolerance must not turn a text assertion into a fuzzy one."""
    with pytest.raises(AssertionError):
        _verify("Done!", "Done", tolerance=5)


def test_equal_text_passes_without_any_tolerance():
    assert _verify("50", "50", tolerance_table={}) is True
