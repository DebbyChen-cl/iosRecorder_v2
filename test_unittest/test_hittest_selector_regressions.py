import asyncio
import xml.etree.ElementTree as ET

import pytest

import app.main as m
import app.selector as selector
from app.hittest import HIT_SLOP, hit_test
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


def _occluded_wait_view_root() -> ET.Element:
    """ArtisticAvatarResultViewController — a full-size accessible imageView is
    stacked above waitView, so WDA's hit-test based `visible` reports the whole
    wait subtree as invisible even though it is what the user sees on screen.

    navView is included as the contrast case: it is genuinely hidden (replaced
    by resultTopView, a *container* with children), so it must stay penalised.
    """
    return ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeOther name="photodirector.ArtisticAvatarResultViewController"
              enabled="true" visible="true" accessible="false" x="0" y="0" width="430" height="932">
            <XCUIElementTypeOther name="navView" enabled="true" visible="false" accessible="false"
                x="0" y="59" width="430" height="60">
              <XCUIElementTypeStaticText name="navDescriptionLabel" enabled="true" visible="false"
                  accessible="false" x="116" y="69" width="131" height="40" />
            </XCUIElementTypeOther>
            <XCUIElementTypeOther name="resultTopView" enabled="true" visible="true" accessible="false"
                x="0" y="59" width="430" height="60">
              <XCUIElementTypeButton name="btnBack" enabled="false" visible="true" accessible="true"
                  x="18" y="76" width="26" height="26" />
            </XCUIElementTypeOther>
            <XCUIElementTypeOther name="contentView" enabled="true" visible="true" accessible="false"
                x="0" y="119" width="430" height="813">
              <XCUIElementTypeOther name="waitView" enabled="true" visible="false" accessible="false"
                  x="0" y="119" width="430" height="542">
                <XCUIElementTypeActivityIndicator value="1" name="waitIndicator" label="In progress"
                    enabled="true" visible="false" accessible="true" x="195" y="351" width="40" height="39" />
                <XCUIElementTypeStaticText value="Creating Your AI Image" name="waitLabel"
                    label="Creating Your AI Image" enabled="true" visible="false" accessible="true"
                    x="0" y="399" width="430" height="27" />
                <XCUIElementTypeStaticText value="Waiting time: about 1 minute" name="waitTimeLabel"
                    label="Waiting time: about 1 minute" enabled="true" visible="false" accessible="true"
                    x="0" y="434" width="430" height="22" />
              </XCUIElementTypeOther>
              <XCUIElementTypeImage name="imageView" enabled="true" visible="true" accessible="true"
                  x="0" y="119" width="430" height="542" />
            </XCUIElementTypeOther>
          </XCUIElementTypeOther>
        </AppiumAUT>
        """
    )


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (215, 370, "waitIndicator"),
        (215, 412, "waitLabel"),
        (215, 445, "waitTimeLabel"),
    ],
)
def test_hit_test_picks_wait_elements_occluded_by_full_size_image(x, y, expected):
    el = hit_test(x, y, _occluded_wait_view_root())

    assert el is not None
    assert el.attrib["name"] == expected


def test_hit_test_keeps_image_where_wait_subtree_has_no_element():
    """Points inside imageView but outside every wait child still resolve to imageView."""
    el = hit_test(215, 200, _occluded_wait_view_root())

    assert el is not None
    assert el.attrib["name"] == "imageView"


def test_hit_test_still_ignores_genuinely_hidden_nav_bar():
    """navView is covered by resultTopView, a container with children — not a
    bare accessible leaf — so its hidden children stay deprioritised."""
    el = hit_test(150, 88, _occluded_wait_view_root())

    assert el is not None
    assert el.attrib["name"] == "resultTopView"


def _pack_selection_cell_root() -> ET.Element:
    """AIStudioAIArtworkShortTaskPackSelection — every cell carries a full-size
    ``selectCheckBoxOverlay`` (visible="true" **accessible="false"**) drawn above
    its content, so WDA reports the whole ``statusOverlay`` subtree invisible
    even though "Processing…" is what the user sees.

    Cell-1 is the contrast case: nothing is hidden underneath the overlay, so
    the overlay itself must stay the answer.
    """
    return ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeCollectionView name="imageCollectionView"
              enabled="true" visible="true" accessible="false" x="26" y="230" width="378" height="668">
            <XCUIElementTypeCell name="AIArtworkPackSelectionCell-0"
                enabled="true" visible="true" accessible="false" x="26" y="230" width="180" height="180">
              <XCUIElementTypeOther enabled="true" visible="true" accessible="false"
                  x="26" y="230" width="180" height="180">
                <XCUIElementTypeImage enabled="true" visible="false" accessible="false"
                    x="26" y="230" width="180" height="180" />
                <XCUIElementTypeOther name="statusOverlay" enabled="true" visible="false" accessible="false"
                    x="26" y="230" width="180" height="180">
                  <XCUIElementTypeActivityIndicator value="1" name="activityIndicator" label="In progress"
                      enabled="true" visible="false" accessible="true" x="94" y="285" width="44" height="44" />
                  <XCUIElementTypeStaticText value="Processing..." name="statusLabel" label="Processing..."
                      enabled="true" visible="false" accessible="true" x="35" y="338" width="162" height="18" />
                </XCUIElementTypeOther>
                <XCUIElementTypeOther name="selectCheckBoxOverlay" enabled="true" visible="true"
                    accessible="false" x="26" y="230" width="180" height="180" />
              </XCUIElementTypeOther>
            </XCUIElementTypeCell>
            <XCUIElementTypeCell name="AIArtworkPackSelectionCell-1"
                enabled="true" visible="true" accessible="false" x="224" y="230" width="180" height="180">
              <XCUIElementTypeOther enabled="true" visible="true" accessible="false"
                  x="224" y="230" width="180" height="180">
                <XCUIElementTypeImage enabled="true" visible="false" accessible="false"
                    x="224" y="230" width="180" height="180" />
                <XCUIElementTypeOther name="selectCheckBoxOverlay" enabled="true" visible="true"
                    accessible="false" x="224" y="230" width="180" height="180" />
              </XCUIElementTypeOther>
            </XCUIElementTypeCell>
          </XCUIElementTypeCollectionView>
        </AppiumAUT>
        """
    )


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (116, 347, "statusLabel"),
        (116, 307, "activityIndicator"),
    ],
)
def test_hit_test_picks_status_elements_under_inaccessible_overlay(x, y, expected):
    """The covering overlay is accessible="false" — it still swallows the
    hit-test, so the elements below it must count as visible."""
    el = hit_test(x, y, _pack_selection_cell_root())

    assert el is not None
    assert el.attrib["name"] == expected


@pytest.mark.parametrize("x,y", [(116, 250), (314, 320)])
def test_hit_test_keeps_overlay_where_no_status_element_sits_below(x, y):
    """Inside the overlay but outside every status child (cell-0), and anywhere
    in a cell that has no status overlay at all (cell-1)."""
    el = hit_test(x, y, _pack_selection_cell_root())

    assert el is not None
    assert el.attrib["name"] == "selectCheckBoxOverlay"


def _image_to_video_history_root() -> ET.Element:
    """ImageToVideoHistoryBrowseViewController — while a clip is still rendering
    the cell stacks a not-yet-loaded ``thumbnailImageView`` (visible="false") and
    the "Processing..." ``processingLabel`` on the **exact same rect**.

    The label covers the image, so ``_visibility_exemptions`` exempts the image
    too — leaving both with an identical score until document order broke the
    tie in favour of the image nobody can see. Cell-2 is the contrast case: the
    render finished, the label is gone and the image is genuinely visible.
    """
    return ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeCollectionView name="packCollectionView"
              enabled="true" visible="true" accessible="false" x="18" y="230" width="394" height="668">
            <XCUIElementTypeCell name="AIArtworkImageToVideoCell-0"
                enabled="true" visible="true" accessible="false" x="18" y="230" width="394" height="165">
              <XCUIElementTypeOther name="imageContainerView" enabled="true" visible="true"
                  accessible="false" x="18" y="230" width="165" height="165">
                <XCUIElementTypeImage name="thumbnailImageView" enabled="true" visible="false"
                    accessible="true" x="18" y="230" width="165" height="165" />
                <XCUIElementTypeStaticText value="Processing..." name="processingLabel"
                    label="Processing..." enabled="true" visible="true" accessible="true"
                    x="18" y="230" width="165" height="165" />
              </XCUIElementTypeOther>
            </XCUIElementTypeCell>
            <XCUIElementTypeCell name="AIArtworkImageToVideoCell-2"
                enabled="true" visible="true" accessible="false" x="18" y="580" width="394" height="165">
              <XCUIElementTypeOther name="imageContainerView" enabled="true" visible="true"
                  accessible="false" x="18" y="580" width="165" height="165">
                <XCUIElementTypeImage name="thumbnailImageView" enabled="true" visible="true"
                    accessible="true" x="18" y="580" width="165" height="165" />
              </XCUIElementTypeOther>
            </XCUIElementTypeCell>
          </XCUIElementTypeCollectionView>
        </AppiumAUT>
        """
    )


def test_hit_test_prefers_processing_label_over_same_rect_hidden_thumbnail():
    el = hit_test(100, 312, _image_to_video_history_root())

    assert el is not None
    assert el.attrib["name"] == "processingLabel"


def test_hit_test_keeps_thumbnail_where_no_processing_label_covers_it():
    el = hit_test(100, 662, _image_to_video_history_root())

    assert el is not None
    assert el.attrib["name"] == "thumbnailImageView"


def _thin_compare_bar_root() -> ET.Element:
    """AIExpandViewController: a 302x1 compare bar over a full-screen anchor view."""
    return ET.fromstring(
        """
        <AppiumAUT>
          <XCUIElementTypeOther name="photodirector.AIExpandViewController"
              enabled="true" visible="true" x="0" y="0" width="430" height="932">
            <XCUIElementTypeOther name="editAnchorView"
                enabled="true" visible="true" x="0" y="0" width="430" height="932">
              <XCUIElementTypeOther enabled="true" visible="true" x="64" y="254" width="302" height="201">
                <XCUIElementTypeImage enabled="true" visible="true" x="64" y="254" width="302" height="201" />
              </XCUIElementTypeOther>
              <XCUIElementTypeImage name="barImageView"
                  enabled="true" visible="true" x="64" y="454" width="302" height="1" />
            </XCUIElementTypeOther>
            <XCUIElementTypeButton name="generateButton"
                enabled="true" visible="true" x="18" y="779" width="394" height="61" />
            <XCUIElementTypeImage name="panelDivider"
                enabled="true" visible="true" x="0" y="778" width="430" height="1" />
          </XCUIElementTypeOther>
        </AppiumAUT>
        """
    )


# barImageView is at y=454 with h=1, so its centre — and the centre of the
# HIT_SLOP window around it — sits at 454.5. Offsets are expressed relative to
# HIT_SLOP so the cases follow the constant instead of hard-coding its value.
_BAR_CENTER_Y = 454.5
_INSIDE_SLOP = HIT_SLOP / 2 - 1
_OUTSIDE_SLOP = HIT_SLOP / 2 + 1


@pytest.mark.parametrize("dy", [0, -_INSIDE_SLOP, _INSIDE_SLOP])
def test_hit_test_reaches_one_point_tall_compare_bar(dy):
    """A 1 pt element is unreachable by an exact rect test — HIT_SLOP grows the
    hit region so the bar can be recorded at all."""
    el = hit_test(200, _BAR_CENTER_Y + dy, _thin_compare_bar_root())

    assert el is not None
    assert el.attrib["name"] == "barImageView"


@pytest.mark.parametrize("dy", [-_OUTSIDE_SLOP, _OUTSIDE_SLOP, 60])
def test_hit_test_slop_does_not_leak_past_the_threshold(dy):
    """Outside the HIT_SLOP window the thin bar must not be picked up."""
    el = hit_test(200, _BAR_CENTER_Y + dy, _thin_compare_bar_root())

    assert el is not None
    assert el.attrib.get("name") != "barImageView"


def test_hit_test_prefers_button_over_adjacent_thin_divider():
    """A slop-only hit never steals the tap from an element genuinely under the
    finger: y=780 is inside generateButton and within panelDivider's slop."""
    el = hit_test(200, 780, _thin_compare_bar_root())

    assert el is not None
    assert el.attrib["name"] == "generateButton"
