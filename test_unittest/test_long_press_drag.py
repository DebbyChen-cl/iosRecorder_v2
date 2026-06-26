import asyncio
import xml.etree.ElementTree as ET

import app.main as m
import pytest
from app.codegen import generate_script
from app.hittest import hit_test, hit_test_drop_target, hit_test_long_press_drag_source

pytestmark = pytest.mark.unit

_TIMELINE_XML = """\
<AppiumAUT>
  <XCUIElementTypeApplication x="0" y="0" width="320" height="640">
    <XCUIElementTypeOther name="EditPage.UIView.timelineBackgroundView" x="0" y="400" width="320" height="200">
      <XCUIElementTypeImage name="thumbnailContentCell.UIImageView.opacity" x="0" y="430" width="80" height="60"/>
      <XCUIElementTypeImage name="thumbnailContentCell.UIImageView.opacity" x="90" y="430" width="80" height="60"/>
      <XCUIElementTypeImage name="thumbnailContentCell.UIImageView.opacity" x="180" y="430" width="80" height="60"/>
    </XCUIElementTypeOther>
  </XCUIElementTypeApplication>
</AppiumAUT>
"""

_PIP_TRACK_XML = """\
<AppiumAUT>
  <XCUIElementTypeApplication x="0" y="0" width="320" height="693">
    <XCUIElementTypeOther name="dragDropInteraction.UIView.validArea" x="0" y="427" width="320" height="175">
      <XCUIElementTypeImage x="0" y="427" width="320" height="175">
        <XCUIElementTypeOther name="timelineVC.UIView.trackTableContainer" x="0" y="488" width="320" height="114">
          <XCUIElementTypeTable name="multipleTrack.UITableView.tracks" x="0" y="488" width="320" height="114">
            <XCUIElementTypeCell name="multipleTrackViewController.MultipleTrackCell.cell" x="0" y="491" width="320" height="19">
              <XCUIElementTypeImage name="pipTrackCell.UIImageView.clipType" x="164" y="496" width="9" height="9"/>
            </XCUIElementTypeCell>
            <XCUIElementTypeCell name="multipleTrackViewController.MultipleTrackCell.cell" x="0" y="509" width="320" height="19"/>
          </XCUIElementTypeTable>
        </XCUIElementTypeOther>
      </XCUIElementTypeImage>
    </XCUIElementTypeOther>
  </XCUIElementTypeApplication>
</AppiumAUT>
"""


def test_codegen_emits_long_press_drag_function():
    step = {
        "action": "long_press_drag",
        "coords": {"x1": 10, "y1": 20, "x2": 90, "y2": 120},
        "duration": 700,
        "press_duration": 1250,
        "start_target": {
            "type": "accessibility id",
            "value": "source",
            "offset_pct": {"x": 25.0, "y": 50.0},
        },
        "end_target": {
            "type": "accessibility id",
            "value": "target",
            "offset_pct": {"x": 75.0, "y": 55.0},
        },
    }

    code = generate_script([step], "long_press_drag")

    assert "Long press drag source" in code
    assert "actions.long_press_drag_within_elements(" in code
    assert "duration=0.7, press_duration=1.25" in code


def test_codegen_clamps_long_press_drag_press_duration_to_one_second():
    step = {
        "action": "long_press_drag",
        "coords": {"x1": 10, "y1": 20, "x2": 90, "y2": 120},
        "duration": 700,
        "press_duration": 611,
        "start_target": {
            "type": "accessibility id",
            "value": "source",
            "offset_pct": {"x": 25.0, "y": 50.0},
        },
        "end_target": {
            "type": "accessibility id",
            "value": "target",
            "offset_pct": {"x": 75.0, "y": 55.0},
        },
    }

    code = generate_script([step], "long_press_drag")

    assert "duration=0.7, press_duration=1.0" in code


def test_record_long_press_drag_keeps_press_duration():
    m._steps.clear()

    asyncio.run(
        m._record_drag(
            10,
            20,
            90,
            120,
            700,
            snapshot=ET.Element("App"),
            action="long_press_drag",
            press_duration=1250,
        )
    )

    step = m._steps.pop()
    assert step["action"] == "long_press_drag"
    assert step["duration"] == 700
    assert step["press_duration"] == 1250


def test_long_press_drag_source_prefers_multiple_track_cell_over_valid_area():
    root = ET.fromstring(_PIP_TRACK_XML)

    target = hit_test_long_press_drag_source(170, 500, root)

    assert target is not None
    assert target.tag == "XCUIElementTypeCell"
    assert target.attrib["name"] == "multipleTrackViewController.MultipleTrackCell.cell"


def test_record_long_press_drag_source_uses_indexed_track_cell_xpath():
    m._steps.clear()
    root = ET.fromstring(_PIP_TRACK_XML)

    asyncio.run(
        m._record_drag(
            170,
            500,
            263,
            466,
            1452,
            snapshot=root,
            action="long_press_drag",
            press_duration=2460,
        )
    )

    step = m._steps.pop()
    assert step["start_target"]["type"] == "xpath"
    assert step["start_target"]["value"] == '(//XCUIElementTypeCell[@name="multipleTrackViewController.MultipleTrackCell.cell"])[1]'
    assert step["start_target"]["offset_pct"] == {"x": 53.1, "y": 47.4}


def test_drop_target_prefers_timeline_container_over_thumbnail_leaf():
    root = ET.fromstring(_TIMELINE_XML)
    source = hit_test(220, 460, root)
    assert source is not None
    assert source.tag == "XCUIElementTypeImage"

    target = hit_test_drop_target(40, 460, root, source)

    assert target is not None
    assert target.attrib["name"] == "EditPage.UIView.timelineBackgroundView"


def test_drop_target_keeps_timeline_container_when_source_is_same_container():
    root = ET.fromstring(_TIMELINE_XML)
    source = hit_test(300, 560, root)
    assert source is not None
    assert source.attrib["name"] == "EditPage.UIView.timelineBackgroundView"

    target = hit_test_drop_target(40, 460, root, source)

    assert target is source
