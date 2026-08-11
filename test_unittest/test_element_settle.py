"""Unit tests for the pre-action element-readiness gate.

``tap_within_element`` turns an element into an absolute coordinate and fires
``mobile: tap``, which WDA reports as success no matter what sits under that
point.  So a coordinate read while a panel is still sliding in produces a step
that passes while nothing was tapped — the failure only surfaces one step later.

``DriverActions._element_settle()`` closes that hole by waiting until the
element's rect stops moving *and* it reports ``visible=true`` before any
coordinate is derived from it.  These tests drive it with a fake element, so
they need neither Appium nor a device.
"""

import sys
from pathlib import Path

import pytest
from selenium.common.exceptions import StaleElementReferenceException

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pytest"))

from driver.driver_actions import DriverActions  # noqa: E402

pytestmark = pytest.mark.unit


class FakeElement:
    """Replays a scripted sequence of rects / visible values.

    Each ``.rect`` read advances the timeline; the last entry repeats forever.
    """

    def __init__(self, rects, visible=None, name="fakeButton"):
        self._rects = [dict(r) for r in rects]
        self._visible = list(visible) if visible is not None else None
        self._name = name
        self.rect_reads = 0
        self.visible_reads = 0

    @property
    def rect(self):
        r = self._rects[min(self.rect_reads, len(self._rects) - 1)]
        self.rect_reads += 1
        return dict(r)

    def get_attribute(self, name):
        if name == "visible":
            if self._visible is None:
                return "true"
            v = self._visible[min(self.visible_reads, len(self._visible) - 1)]
            self.visible_reads += 1
            return v
        if name == "name":
            return self._name
        return None


class FakeDriver:
    """Only what `_visible_fraction` touches."""

    def __init__(self, width=430, height=932):
        self._size = {"width": width, "height": height}

    def get_window_size(self):
        return dict(self._size)


def _actions(interval=0.001, timeout=0.5, driver=None):
    actions = DriverActions(driver=driver)
    actions.element_settle_interval = interval
    actions.element_settle_timeout = timeout
    return actions


def _rect(x, y, w=40, h=40):
    return {"x": x, "y": y, "width": w, "height": h}


def test_settles_only_after_rect_stops_moving():
    """A view still sliding in must not hand back its in-flight coordinates."""
    el = FakeElement([_rect(100, 500), _rect(100, 460), _rect(100, 420), _rect(100, 400)])
    rect = _actions()._element_settle(el)
    assert rect == _rect(100, 400)
    assert el.rect_reads >= 4


def test_waits_for_visible_even_when_rect_is_already_still():
    """A dialog is attached to the tree at frame 0 with visible=false."""
    el = FakeElement([_rect(10, 20)] * 3, visible=["false", "false", "true"])
    rect = _actions()._element_settle(el)
    assert rect == _rect(10, 20)
    # visible=false blocks release, and the quiet-round counter only starts
    # counting from the first round that is both still *and* visible.
    assert el.visible_reads >= 3


def test_timeout_returns_last_rect_without_raising():
    """Never fail a step that would have passed before — warn and act anyway."""
    el = FakeElement([_rect(x, 0) for x in range(0, 400, 10)])
    rect = _actions(timeout=0.03)._element_settle(el)
    assert rect["width"] == 40  # last rect seen, not an exception


def test_zero_sized_element_never_counts_as_settled():
    el = FakeElement([_rect(10, 20, w=0, h=0)] * 5)
    rect = _actions(timeout=0.03)._element_settle(el)
    assert rect == _rect(10, 20, w=0, h=0)
    assert el.rect_reads > 1


def test_check_can_be_disabled():
    el = FakeElement([_rect(100, 500), _rect(100, 400)])
    actions = _actions()
    actions.element_settle_check = False
    assert actions._element_settle(el) == _rect(100, 500)
    assert el.rect_reads == 1


def test_missing_visible_attribute_does_not_block():
    class NoAttrElement(FakeElement):
        def get_attribute(self, name):
            raise RuntimeError("attribute unsupported")

    el = NoAttrElement([_rect(10, 20)] * 2)
    assert _actions()._element_settle(el) == _rect(10, 20)


def test_coord_at_pct_uses_the_settled_rect():
    """The whole point: the percent offset is applied to the final position."""
    el = FakeElement([_rect(0, 500, 100, 100), _rect(0, 400, 100, 100), _rect(0, 400, 100, 100)])
    assert _actions()._coord_at_pct(el, 57.5, 58.5) == (57, 458)


def test_point_in_element_uses_the_settled_rect():
    el = FakeElement([_rect(0, 500, 100, 100), _rect(0, 400, 100, 100), _rect(0, 400, 100, 100)])
    assert _actions()._point_in_element(el, 50.0, 50.0) == (50, 450)


# ── One matching pair is not "stopped moving" ─────────────────────────────────
#
# element.rect is rounded to whole points and iOS animations ease in/out, so at
# the head of a slide-in the frame can move less than a point between two
# samples.  The element looks parked while it is about to accelerate.


def test_one_matching_rect_pair_is_not_enough():
    """Two equal samples at the start of an ease curve must not release."""
    el = FakeElement(
        [_rect(0, 500), _rect(0, 500), _rect(0, 450), _rect(0, 400), _rect(0, 400)]
    )
    assert _actions()._element_settle(el) == _rect(0, 400)


def test_required_samples_can_be_lowered():
    """The old one-pair behaviour is still reachable for a test that needs speed."""
    actions = _actions()
    actions.element_settle_required_samples = 1
    el = FakeElement(
        [_rect(0, 500), _rect(0, 500), _rect(0, 450), _rect(0, 400), _rect(0, 400)]
    )
    assert actions._element_settle(el) == _rect(0, 500)


# ── Joint settle: every coordinate of one gesture from one quiet moment ───────
#
# A drag needs two element-derived points.  Settling them one after another
# freezes the start point while the end point is still being polled, so a panel
# that is still laying out hands back a start coordinate the control has already
# left — the recorded slider drag then moves the wrong distance, or nothing.


def _drag_pair():
    """Source parks early then shifts again; target keeps moving for longer."""
    src = FakeElement([_rect(0, 500)] * 4 + [_rect(0, 480)], name="cpSlider")
    tgt = FakeElement(
        [_rect(0, 600), _rect(0, 590), _rect(0, 580), _rect(0, 570), _rect(0, 560)],
        name="slider",
    )
    return src, tgt


def test_joint_settle_returns_rects_read_in_the_same_round():
    src, tgt = _drag_pair()
    rects = _actions()._settle_rects([src, tgt])
    # Not _rect(0, 500): the source moved again while the target was settling,
    # which a per-element settle would never have noticed.
    assert rects == [_rect(0, 480), _rect(0, 560)]


def test_points_in_elements_applies_percents_to_the_joint_rects():
    src, tgt = _drag_pair()
    points = _actions()._points_in_elements([(src, 50.0, 0.0), (tgt, 100.0, 0.0)])
    assert points == [(20, 480), (40, 560)]


def test_joint_settle_honours_the_disable_switch():
    src, tgt = _drag_pair()
    actions = _actions()
    actions.element_settle_check = False
    assert actions._settle_rects([src, tgt]) == [_rect(0, 500), _rect(0, 600)]
    assert src.rect_reads == 1 and tgt.rect_reads == 1


def test_joint_settle_never_raises_on_timeout():
    src = FakeElement([_rect(x, 0) for x in range(0, 400, 10)])
    tgt = FakeElement([_rect(0, 600)])
    rects = _actions(timeout=0.03)._settle_rects([src, tgt])
    assert len(rects) == 2


def test_drag_within_elements_measures_both_ends_after_the_ui_settles():
    """The reported failure: drag points computed before the panel was ready."""
    src, tgt = _drag_pair()
    actions = _actions(driver=FakeDriver())
    actions.stability_check = False
    lookups = {("accessibility id", "cpSlider"): src, ("accessibility id", "slider"): tgt}
    actions.find_element = lambda by, value, *a, **kw: lookups[(by, value)]
    performed = []
    actions._perform_w3c_drag = lambda *args: performed.append(args)

    assert actions.drag_within_elements(
        "accessibility id", "cpSlider", 50.0, 0.0,
        "accessibility id", "slider", 100.0, 0.0,
        duration=1.0,
    )
    assert performed == [(20, 480, 40, 560, 1.0, 0.1)]


def test_drag_within_elements_re_resolves_a_stale_element_once():
    stale = FakeElement([_rect(0, 500)], name="cpSlider")

    def boom(_name):
        raise StaleElementReferenceException("gone")

    stale.get_attribute = boom
    fresh_src = FakeElement([_rect(0, 480)], name="cpSlider")
    tgt = FakeElement([_rect(0, 560)], name="slider")
    actions = _actions(driver=FakeDriver())
    actions.stability_check = False
    sources = [stale, fresh_src]
    actions.find_element = lambda by, value, *a, **kw: (
        sources.pop(0) if value == "cpSlider" else tgt
    )
    performed = []
    actions._perform_w3c_drag = lambda *args: performed.append(args)

    assert actions.drag_within_elements(
        "accessibility id", "cpSlider", 50.0, 0.0,
        "accessibility id", "slider", 100.0, 0.0,
    )
    assert not sources, "the stale source handle was never replaced"
    assert performed == [(20, 480, 40, 560, 1.0, 0.1)]


# ── _visible_fraction: clipping by the container, not just the screen ──────────
#
# A horizontal styleCollectionView is 430x84.  A cell parked at its left edge is
# clipped by the strip long before it leaves the screen — screen-only measurement
# calls that 100% visible, so scroll_until stopped early and the tap landed on the
# cut-off cell or its neighbour.

_STRIP = {"x": 0, "y": 700, "width": 430, "height": 84}


def _fraction(el_rect, clip=None, screen=(430, 932)):
    actions = _actions(driver=FakeDriver(*screen))
    return actions._visible_fraction(FakeElement([el_rect]), clip=clip)


def test_cell_fully_inside_container_is_fully_visible():
    assert _fraction(_rect(100, 710, 80, 60), clip=_STRIP) == pytest.approx(1.0)


def test_cell_half_clipped_by_container_edge():
    """Half the cell hangs off the left edge of the strip — still on screen."""
    assert _fraction(_rect(-40, 710, 80, 60), clip=_STRIP) == pytest.approx(0.5)


def test_cell_clipped_by_container_but_on_screen_is_not_visible():
    """The regression this fix targets: on screen, but outside the strip."""
    assert _fraction(_rect(100, 300, 80, 60), clip=_STRIP) == 0.0
    # …and the old screen-only measurement is exactly what called it fully visible
    assert _fraction(_rect(100, 300, 80, 60)) == pytest.approx(1.0)


def test_element_larger_than_container_is_not_penalised():
    """A wrapper overflowing its container fills the window → fully visible."""
    assert _fraction(_rect(0, 650, 430, 200), clip=_STRIP) == pytest.approx(1.0)


def test_degenerate_clip_is_ignored():
    zero = {"x": 0, "y": 700, "width": 0, "height": 0}
    assert _fraction(_rect(100, 300, 80, 60), clip=zero) == pytest.approx(1.0)


def test_offscreen_element_still_measures_zero():
    assert _fraction(_rect(500, 300, 80, 60)) == 0.0
    assert _fraction(_rect(100, 300, 80, 60), clip=_STRIP) == 0.0


def test_screen_only_semantics_unchanged_for_oversized_elements():
    """No clip → original formula, including the >screen penalty."""
    assert _fraction(_rect(0, 0, 430, 1864)) == pytest.approx(0.5)
