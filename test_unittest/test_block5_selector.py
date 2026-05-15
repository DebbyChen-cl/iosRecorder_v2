"""
Block 5 — Selector (standalone)

Tests the selector priority rules and quality classification independently.
Input: ET.Element with various combinations of name/label attributes.
Output: (selector_type, value) and quality string.
No device or server needed.
"""

import xml.etree.ElementTree as ET

import pytest

pytestmark = pytest.mark.unit

from app.selector import build_selector, build_xpath, get_selector_quality


def _el(tag="XCUIElementTypeButton", **attribs) -> ET.Element:
    el = ET.Element(tag)
    el.attrib.update(attribs)
    return el


# ── build_selector — priority ──────────────────────────────────────────────────

def test_selector_prefers_accessibility_id():
    el = _el(name="SaveButton", label="Save")
    sel_type, sel_val = build_selector(el)
    assert sel_type == "accessibility id"
    assert sel_val == "SaveButton"


def test_selector_falls_back_to_label():
    el = _el(label="Save")
    sel_type, sel_val = build_selector(el)
    assert sel_type == "name"
    assert sel_val == "Save"


def test_selector_xpath_when_no_id_or_label():
    el = _el()
    sel_type, sel_val = build_selector(el)
    assert sel_type == "xpath"
    assert "XCUIElementTypeButton" in sel_val


def test_selector_skips_hex_pointer_name():
    el = _el(name="0x1a2b3c4d", label="Save")
    sel_type, sel_val = build_selector(el)
    assert sel_type == "name"
    assert sel_val == "Save"


def test_selector_skips_path_name():
    el = _el(name="/private/var/something", label="Save")
    sel_type, sel_val = build_selector(el)
    assert sel_type == "name"
    assert sel_val == "Save"


def test_selector_strips_whitespace():
    el = _el(name="  SaveButton  ")
    sel_type, sel_val = build_selector(el)
    assert sel_type == "accessibility id"
    assert sel_val == "SaveButton"


# ── get_selector_quality ───────────────────────────────────────────────────────

def test_quality_id_when_name_differs_from_label():
    el = _el(name="SaveButton", label="Save")
    assert get_selector_quality(el) == "id"


def test_quality_id_eq_label_when_equal():
    el = _el(name="Effects", label="Effects")
    assert get_selector_quality(el) == "id_eq_label"


def test_quality_id_indexed_when_name_ends_with_number():
    el = _el(name="Cell-3", label="Cell 3")
    assert get_selector_quality(el) == "id_indexed"


def test_quality_label_only_when_no_name():
    el = _el(label="Label Only")
    assert get_selector_quality(el) == "label_only"


def test_quality_xpath_only_when_nothing():
    el = _el()
    assert get_selector_quality(el) == "xpath_only"


def test_quality_xpath_only_for_hex_name():
    el = _el(name="0xdeadbeef")
    assert get_selector_quality(el) == "xpath_only"


# ── build_xpath ────────────────────────────────────────────────────────────────

def test_xpath_with_name():
    el = _el(name="SaveButton")
    xpath = build_xpath(el)
    assert xpath == "//XCUIElementTypeButton[@name='SaveButton']"


def test_xpath_with_label_only():
    el = _el(label="Save")
    xpath = build_xpath(el)
    assert xpath == "//XCUIElementTypeButton[@label='Save']"


def test_xpath_bare_tag_fallback():
    el = _el()
    xpath = build_xpath(el)
    assert xpath == "//XCUIElementTypeButton"


def test_xpath_skips_hex_name():
    el = _el(name="0x1234", label="Save")
    xpath = build_xpath(el)
    assert "@label='Save'" in xpath


# ── fixture-based selector quality ────────────────────────────────────────────

def test_fixture_save_button_quality_is_id(fixture_root):
    from app.hittest import hit_test
    el = hit_test(140, 222, fixture_root)
    assert get_selector_quality(el) == "id"


def test_fixture_effects_quality_is_id_eq_label(fixture_root):
    from app.hittest import hit_test
    el = hit_test(240, 222, fixture_root)
    assert get_selector_quality(el) == "id_eq_label"


def test_fixture_label_only_quality(fixture_root):
    from app.hittest import hit_test
    el = hit_test(195, 460, fixture_root)
    assert get_selector_quality(el) == "label_only"


def test_fixture_xpath_only_quality(fixture_root):
    from app.hittest import hit_test
    el = hit_test(50, 530, fixture_root)
    assert get_selector_quality(el) == "xpath_only"


def test_fixture_cell3_quality_is_id_indexed(fixture_root):
    from app.hittest import hit_test
    el = hit_test(195, 600, fixture_root)
    assert get_selector_quality(el) == "id_indexed"
