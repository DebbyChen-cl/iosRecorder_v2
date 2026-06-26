import asyncio
import xml.etree.ElementTree as ET

import app.main as m
import pytest
from app.codegen import generate_script
from app.hittest import hit_test, hit_test_drop_target, hit_test_long_press_drag_source
from app.wda import WDAClient

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


def test_codegen_adds_activation_nudge_for_timeline_long_press_drag():
    step = {
        "action": "long_press_drag",
        "coords": {"x1": 94, "y1": 505, "x2": 264, "y2": 548},
        "duration": 1300,
        "press_duration": 1830,
        "start_target": {
            "type": "xpath",
            "value": '(//XCUIElementTypeCell[@name="multipleTrackViewController.MultipleTrackCell.cell"])[1]',
            "offset_pct": {"x": 29.4, "y": 72.2},
        },
        "end_target": {
            "type": "xpath",
            "value": "//XCUIElementTypeOther[@name='timelineVC.UIView.trackTableContainer']",
            "offset_pct": {"x": 82.5, "y": 52.3},
        },
    }

    code = generate_script([step], "long_press_drag")

    assert "activation_nudge_y=-8" in code


def test_codegen_resolves_long_press_drag_start_before_coordinate_drop():
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
    }

    code = generate_script([step], "long_press_drag")

    assert "actions.long_press_drag_from_element_to_coordinates(" in code
    assert "AppiumBy.ACCESSIBILITY_ID, 'source', 25.0, 50.0, 90, 120" in code


def test_codegen_resolves_long_press_drag_end_before_coordinate_start():
    step = {
        "action": "long_press_drag",
        "coords": {"x1": 10, "y1": 20, "x2": 90, "y2": 120},
        "duration": 700,
        "press_duration": 1250,
        "end_target": {
            "type": "accessibility id",
            "value": "target",
            "offset_pct": {"x": 75.0, "y": 55.0},
        },
    }

    code = generate_script([step], "long_press_drag")

    assert "actions.long_press_drag_from_coordinates_to_element(" in code
    assert "10, 20, AppiumBy.ACCESSIBILITY_ID, 'target', 75.0, 55.0" in code


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


def test_record_long_press_drag_builds_step_before_wda(monkeypatch):
    events = []
    m._steps.clear()
    monkeypatch.setitem(m._cache, "root", ET.Element("App"))

    async def fake_pre_screenshot():
        return None

    original_build = m._build_drag_record_step

    def wrapped_build(*args, **kwargs):
        events.append("build")
        return original_build(*args, **kwargs)

    async def fake_long_press_drag(*args):
        events.append("wda")
        return True

    monkeypatch.setattr(m, "_take_pre_gesture_screenshot", fake_pre_screenshot)
    monkeypatch.setattr(m, "_build_drag_record_step", wrapped_build)
    monkeypatch.setattr(m.wda, "long_press_drag", fake_long_press_drag)

    resp = asyncio.run(
        m.record_long_press_drag(
            m.LongPressDragReq(
                x1=10,
                y1=20,
                x2=90,
                y2=120,
                duration=700,
                press_duration=1250,
            )
        )
    )

    step = m._steps.pop()
    assert resp == {"ok": True}
    assert events == ["build", "wda"]
    assert step["action"] == "long_press_drag"
    assert step["press_duration"] == 1250


def test_record_long_press_drag_passes_timeline_nudge_to_wda(monkeypatch):
    calls = []
    m._steps.clear()
    root = ET.fromstring(_PIP_TRACK_XML)
    monkeypatch.setitem(m._cache, "root", root)

    async def fake_pre_screenshot():
        return None

    async def fake_long_press_drag(*args):
        calls.append(args)
        return True

    monkeypatch.setattr(m, "_take_pre_gesture_screenshot", fake_pre_screenshot)
    monkeypatch.setattr(m.wda, "long_press_drag", fake_long_press_drag)

    resp = asyncio.run(
        m.record_long_press_drag(
            m.LongPressDragReq(
                x1=170,
                y1=500,
                x2=264,
                y2=548,
                duration=1300,
                press_duration=1830,
            )
        )
    )

    m._steps.pop()
    assert resp == {"ok": True}
    assert calls
    assert calls[0][-1] == -8


def test_wda_long_press_drag_uses_multi_segment_path(monkeypatch):
    captured = {}

    async def run_drag():
        client = WDAClient()

        async def fake_actions(actions, timeout=5.0):
            captured["actions"] = actions
            captured["timeout"] = timeout
            return True

        monkeypatch.setattr(client, "_actions", fake_actions)
        return await client.long_press_drag(10, 20, 90, 120, 700, 1250, -8)

    ok = asyncio.run(run_drag())

    touch_actions = captured["actions"][0]["actions"]
    pointer_moves = [a for a in touch_actions if a["type"] == "pointerMove"]
    assert ok is True
    assert len(pointer_moves) == 5
    assert pointer_moves[0] == {"type": "pointerMove", "duration": 0, "x": 10, "y": 20}
    assert pointer_moves[1]["x"] == 10
    assert pointer_moves[1]["y"] == 12
    assert touch_actions[-2] == {"type": "pause", "duration": 120}
    assert touch_actions[-1] == {"type": "pointerUp", "button": 0}


def test_long_press_drag_source_keeps_precise_track_leaf():
    root = ET.fromstring(_PIP_TRACK_XML)

    target = hit_test_long_press_drag_source(170, 500, root)

    assert target is not None
    assert target.tag == "XCUIElementTypeImage"
    assert target.attrib["name"] == "pipTrackCell.UIImageView.clipType"


def test_long_press_drag_source_falls_back_to_track_cell_when_no_leaf():
    root = ET.fromstring(_PIP_TRACK_XML)

    target = hit_test_long_press_drag_source(104, 502, root)

    assert target is not None
    assert target.tag == "XCUIElementTypeCell"
    assert target.attrib["name"] == "multipleTrackViewController.MultipleTrackCell.cell"


def test_record_long_press_drag_source_uses_precise_track_leaf():
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
    assert step["start_target"]["type"] == "accessibility id"
    assert step["start_target"]["value"] == "pipTrackCell.UIImageView.clipType"
    assert step["start_target"]["offset_pct"] == {"x": 66.7, "y": 44.4}


def test_record_long_press_drag_source_uses_indexed_track_cell_xpath_without_leaf():
    m._steps.clear()
    root = ET.fromstring(_PIP_TRACK_XML)

    asyncio.run(
        m._record_drag(
            104,
            502,
            263,
            500,
            1452,
            snapshot=root,
            action="long_press_drag",
            press_duration=2460,
        )
    )

    step = m._steps.pop()
    assert step["start_target"]["type"] == "xpath"
    assert step["start_target"]["value"] == '(//XCUIElementTypeCell[@name="multipleTrackViewController.MultipleTrackCell.cell"])[1]'
    assert step["start_target"]["offset_pct"] == {"x": 32.5, "y": 57.9}


def test_drop_target_prefers_track_cell_over_track_table_container():
    root = ET.fromstring(_PIP_TRACK_XML)
    source = hit_test_long_press_drag_source(104, 502, root)

    target = hit_test_drop_target(263, 500, root, source)

    assert target is not None
    assert target.tag == "XCUIElementTypeCell"
    assert target.attrib["name"] == "multipleTrackViewController.MultipleTrackCell.cell"


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
