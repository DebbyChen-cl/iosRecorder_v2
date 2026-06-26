import asyncio
import xml.etree.ElementTree as ET

import pytest

import app.main as m
import app.selector as selector
from app.hittest import hit_test
from app.selector import build_indexed_xpath_if_duplicate, build_xpath

pytestmark = pytest.mark.unit


def _timeline_switch_root() -> ET.Element:
    return ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeOther name="EditPage.UIView.timelineBackgroundView"
              enabled="true" visible="true" x="0" y="427" width="320" height="266" />
          <XCUIElementTypeSwitch value="1"
              enabled="true" visible="true" x="220" y="500" width="51" height="31" />
          <XCUIElementTypeSwitch value="1"
              enabled="true" visible="true" x="20" y="500" width="51" height="31" />
        </AppiumAUT>
        """
    )


def test_hit_test_prefers_switch_over_named_timeline_background():
    root = _timeline_switch_root()

    el = hit_test(234, 513, root)

    assert el is not None
    assert el.tag == "XCUIElementTypeSwitch"
    assert el.attrib["value"] == "1"


def test_hit_test_prefers_visible_track_cell_over_hidden_timeline_background(monkeypatch):
    root = ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeOther name="EditPage.UIView.timelineBackgroundView"
              enabled="true" visible="false" x="0" y="427" width="320" height="266" />
          <XCUIElementTypeOther name="dragDropInteraction.UIView.validArea"
              enabled="true" visible="true" x="0" y="427" width="320" height="175">
            <XCUIElementTypeImage enabled="true" visible="true" x="0" y="427" width="320" height="175">
              <XCUIElementTypeOther name="timelineVC.UIView.trackTableContainer"
                  enabled="true" visible="true" x="0" y="488" width="320" height="114">
                <XCUIElementTypeTable name="multipleTrack.UITableView.tracks"
                    enabled="true" visible="true" x="0" y="488" width="320" height="114">
                  <XCUIElementTypeCell name="multipleTrackViewController.MultipleTrackCell.cell"
                      enabled="true" visible="true" x="0" y="491" width="320" height="19" />
                  <XCUIElementTypeCell name="multipleTrackViewController.MultipleTrackCell.cell"
                      enabled="true" visible="true" x="0" y="509" width="320" height="19" />
                </XCUIElementTypeTable>
              </XCUIElementTypeOther>
            </XCUIElementTypeImage>
          </XCUIElementTypeOther>
        </AppiumAUT>
        """
    )
    monkeypatch.setattr(selector, "_XPATH_ONLY_MODE", True)

    el = hit_test(234, 513, root)

    assert el is not None
    assert el.tag == "XCUIElementTypeCell"
    assert el.attrib["name"] == "multipleTrackViewController.MultipleTrackCell.cell"

    target = m._build_target(234, 513, el, root, structural_log=False)
    assert target["type"] == "xpath"
    assert (
        target["value"]
        == '(//XCUIElementTypeCell[@name="multipleTrackViewController.MultipleTrackCell.cell"])[2]'
    )


def test_hit_test_prefers_add_button_with_children_over_overlapping_thumbnail():
    root = ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeOther name="timelineVC.UIView.masterTrackContainer"
              enabled="true" visible="true" x="0" y="447" width="320" height="42">
            <XCUIElementTypeCollectionView
                enabled="true" visible="true" x="0" y="447" width="320" height="42">
              <XCUIElementTypeImage name="thumbnailContentCell.UIImageView.opacity"
                  enabled="true" visible="false" accessible="true"
                  x="255" y="450" width="68" height="39" />
            </XCUIElementTypeCollectionView>
            <XCUIElementTypeButton name="masterTrackViewController.button.add"
                enabled="true" visible="true" accessible="true"
                x="269" y="453" width="29" height="30">
              <XCUIElementTypeStaticText
                  enabled="true" visible="false" x="269" y="453" width="1" height="1" />
              <XCUIElementTypeStaticText name="maskButton.UILabel.label"
                  enabled="true" visible="false" x="269" y="475" width="29" height="0" />
            </XCUIElementTypeButton>
          </XCUIElementTypeOther>
        </AppiumAUT>
        """
    )

    el = hit_test(289, 473, root)

    assert el is not None
    assert el.tag == "XCUIElementTypeButton"
    assert el.attrib["name"] == "masterTrackViewController.button.add"
    assert build_xpath(el) == "//XCUIElementTypeButton[@name='masterTrackViewController.button.add']"


def test_value_only_switch_xpath_is_indexed_when_duplicates_exist():
    root = _timeline_switch_root()
    switch = root[1]

    assert build_xpath(switch) == '//XCUIElementTypeSwitch[@value="1"]'
    assert (
        build_indexed_xpath_if_duplicate(switch, root)
        == '(//XCUIElementTypeSwitch[@value="1"])[1]'
    )

    target = m._build_target(234, 513, switch, root, structural_log=False)
    assert target["type"] == "xpath"
    assert target["value"] == '(//XCUIElementTypeSwitch[@value="1"])[1]'
    assert target["xpath"] == '(//XCUIElementTypeSwitch[@value="1"])[1]'
    assert target["selector_quality"] == "xpath_only"


def test_scroll_target_uses_indexed_xpath_for_duplicate_menu_image(monkeypatch):
    root = ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeCollectionView name="toolMenuCollectionViewController.UICollectionView.collectionView"
              enabled="true" visible="true" x="0" y="600" width="320" height="54">
            <XCUIElementTypeImage name="MenuImageCell.UIImageView.buttonImage"
                enabled="true" visible="true" x="10" y="612" width="22" height="22" />
            <XCUIElementTypeImage name="MenuImageCell.UIImageView.buttonImage"
                enabled="true" visible="true" x="70" y="612" width="22" height="22" />
            <XCUIElementTypeImage name="MenuImageCell.UIImageView.buttonImage"
                enabled="true" visible="true" x="130" y="612" width="22" height="22" />
            <XCUIElementTypeImage name="MenuImageCell.UIImageView.buttonImage"
                enabled="true" visible="true" x="190" y="612" width="22" height="22" />
            <XCUIElementTypeImage name="MenuImageCell.UIImageView.buttonImage"
                enabled="true" visible="true" x="250" y="612" width="22" height="22" />
          </XCUIElementTypeCollectionView>
        </AppiumAUT>
        """
    )
    monkeypatch.setattr(selector, "_XPATH_ONLY_MODE", True)
    old_steps = m._steps
    m._steps = [{"action": "scroll", "coords": {"x1": 260, "y1": 626, "x2": 80, "y2": 626}}]

    try:
        asyncio.run(m._record_scroll_target(261, 623, snapshot=root))

        assert m._steps[0]["scroll_target"]["type"] == "xpath"
        assert (
            m._steps[0]["scroll_target"]["value"]
            == '(//XCUIElementTypeImage[@name="MenuImageCell.UIImageView.buttonImage"])[5]'
        )
        assert (
            m._steps[0]["scroll_target"]["xpath"]
            == '(//XCUIElementTypeImage[@name="MenuImageCell.UIImageView.buttonImage"])[5]'
        )
    finally:
        m._steps = old_steps
