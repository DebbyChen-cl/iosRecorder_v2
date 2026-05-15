"""
Block 2 — Record Function: hittest + selector

Uses the shared fixture XML hierarchy. Verifies that hit_test() returns the
correct element at each coordinate and that find_scroll_container() finds the
right scrollable ancestor. No device or server needed.
"""

import xml.etree.ElementTree as ET

import pytest

pytestmark = pytest.mark.unit

from app.hittest import (
    find_scroll_container,
    hit_test,
    hit_test_for_swipe,
    hit_test_excluding,
)


# ── hit_test ───────────────────────────────────────────────────────────────────

def test_hit_test_finds_save_button(fixture_root):
    el = hit_test(140, 222, fixture_root)
    assert el is not None
    assert el.attrib.get("name") == "SaveButton"


def test_hit_test_finds_effects_button(fixture_root):
    el = hit_test(240, 222, fixture_root)
    assert el is not None
    assert el.attrib.get("name") == "Effects"


def test_hit_test_finds_textfield(fixture_root):
    el = hit_test(190, 318, fixture_root)
    assert el is not None
    assert el.tag == "XCUIElementTypeTextField"
    assert el.attrib.get("name") == "SearchField"


def test_hit_test_finds_list_item(fixture_root):
    el = hit_test(195, 390, fixture_root)
    assert el is not None
    assert el.attrib.get("name") == "Item1"


def test_hit_test_finds_label_only_button(fixture_root):
    el = hit_test(195, 460, fixture_root)
    assert el is not None
    assert el.attrib.get("label") == "Label Only"
    assert el.attrib.get("name", "") == ""


def test_hit_test_finds_no_id_element(fixture_root):
    el = hit_test(50, 530, fixture_root)
    assert el is not None
    assert el.tag == "XCUIElementTypeOther"


def test_hit_test_returns_none_outside_bounds(fixture_root):
    el = hit_test(500, 500, fixture_root)
    assert el is None


def test_hit_test_result_is_consistent(fixture_root):
    el1 = hit_test(140, 222, fixture_root)
    el2 = hit_test(140, 222, fixture_root)
    assert el1 is el2


# ── hit_test_for_swipe ─────────────────────────────────────────────────────────

def test_swipe_target_not_application(fixture_root):
    el = hit_test_for_swipe(195, 390, fixture_root)
    assert el is not None
    assert el.tag != "XCUIElementTypeApplication"
    assert el.tag != "XCUIElementTypeWindow"


def test_swipe_on_button_returns_button(fixture_root):
    el = hit_test_for_swipe(140, 222, fixture_root)
    assert el is not None
    assert el.tag == "XCUIElementTypeButton"


# ── find_scroll_container ──────────────────────────────────────────────────────

def test_scroll_container_found_inside_scroll(fixture_root):
    container = find_scroll_container(195, 390, fixture_root)
    assert container is not None
    assert container.tag == "XCUIElementTypeScrollView"
    assert container.attrib.get("name") == "MainScroll"


def test_scroll_container_none_outside_scroll(fixture_root):
    container = find_scroll_container(140, 222, fixture_root)
    assert container is None


def test_scroll_container_none_outside_bounds(fixture_root):
    container = find_scroll_container(500, 500, fixture_root)
    assert container is None


# ── hit_test_excluding ─────────────────────────────────────────────────────────

def test_hit_test_excluding_skips_element(fixture_root):
    save_btn = hit_test(140, 222, fixture_root)
    assert save_btn is not None

    # With save_btn excluded, at same coordinate another ancestor should win
    result = hit_test_excluding(140, 222, fixture_root, save_btn)
    assert result is not save_btn
