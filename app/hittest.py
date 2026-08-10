import os
import xml.etree.ElementTree as ET
from typing import List, Optional, Tuple

from .selector import build_selector, build_xpath, get_selector_quality, xpath_literal

_XPATH_ONLY_MODE = os.environ.get("RECORDER_XPATH_ONLY") == "1"

INTERACTIVE_TAGS = frozenset(
    {
        "XCUIElementTypeButton",
        "XCUIElementTypeTextField",
        "XCUIElementTypeSecureTextField",
        "XCUIElementTypeSwitch",
        "XCUIElementTypeLink",
        "XCUIElementTypeCheckBox",
        "XCUIElementTypeSlider",
    }
)

# Generic wrapper types that are structurally necessary but rarely the intended
# direct target. Penalised only when an interactive candidate is available.
GENERIC_CONTAINER_TAGS = frozenset(
    {
        "XCUIElementTypeOther",
        "XCUIElementTypeApplication",
        "XCUIElementTypeWindow",
        "XCUIElementTypeView",
    }
)

SCROLLABLE_TAGS = frozenset(
    {
        "XCUIElementTypeScrollView",
        "XCUIElementTypeCollectionView",
        "XCUIElementTypeTable",
        "XCUIElementTypeWebView",
        "XCUIElementTypeTextView",
    }
)

# Structural container types that should never be the primary tap target when
# a more specific element is available at the same coordinate.
TAP_CONTAINER_TAGS = SCROLLABLE_TAGS | frozenset(
    {
        "XCUIElementTypeApplication",
        "XCUIElementTypeWindow",
    }
)

# Minimum hit-test extent, in device points, for very thin elements. Separator
# lines, compare bars and slider tracks are routinely 1 pt on one axis
# (e.g. barImageView at 302x1); a strict rect test can never be satisfied by a
# pointer coordinate that went through display scaling, so those elements were
# impossible to record. Only the *hit region* grows — _score() still uses the
# real rect, and a slop-only hit is ranked below every exact hit of the same
# calibre, so an inflated sliver never steals a tap from a real element.
#
# 14 pt is sized for the recorder panel, not for a fingertip: a 932 pt screen
# shown ~600 px tall means 8 pt is only ~5 px of mouse travel, which the 60 ms
# hover debounce swallows unless the pointer stops dead inside it. The wider
# window is safe because a slop-only hit still loses to anything genuinely under
# the pointer — it only wins where the alternative is a bare background container.
HIT_SLOP = 14.0


def find_scroll_container(
    x: float,
    y: float,
    root: ET.Element,
    target: Optional[ET.Element] = None,
) -> Optional[ET.Element]:
    """Return the scrollable container an action should be scoped to.

    When *target* is given (element actions such as tap / long press), the
    container is resolved from the **target's ancestor chain** — the innermost
    scrollable ancestor that actually owns the element. A scroll view that
    merely overlaps the tap coordinate but does not contain the target must
    never be attached: the exported test would scroll the wrong view and could
    never find the element no matter how far it scrolls (e.g. a category strip
    whose selector gets paired with the effect list it controls, or a floating
    overlay button drawn on top of an unrelated collection view).

    Without *target* (scroll gestures, which act on the view under the finger)
    fall back to the innermost scrollable element at (x, y).

    In both modes standard scrollable tags win over elements that merely carry
    scrollable="true" (WDA exposes that for non-standard scroll views).
    """
    actual = _unwrap(root)
    if target is not None:
        path = _find_path(actual, target)
        if not path:
            return None
        # path[:-1] excludes the target itself — scoping an element to itself
        # is meaningless when hit_test resolved the scroll view directly.
        ancestors = list(reversed(path[:-1]))
        for el in ancestors:
            if el.tag in SCROLLABLE_TAGS:
                return el
        for el in ancestors:
            if el.attrib.get("scrollable") == "true":
                return el
        return None
    candidates: List[ET.Element] = []
    _collect(x, y, actual, candidates)
    scrollable = [el for el in candidates if el.tag in SCROLLABLE_TAGS]
    if not scrollable:
        scrollable = [el for el in candidates if el.attrib.get("scrollable") == "true"]
    if not scrollable:
        return None
    return min(scrollable, key=_area)


def should_attach_scroll_container(
    target: Optional[ET.Element],
    container: Optional[ET.Element],
    root: ET.Element,
) -> bool:
    """Return whether an element action should be scoped to *container*.

    A container is only valid when it is a real ancestor of the target.
    ``find_scroll_container(..., target=el)`` already guarantees that, so this
    is the guard for any caller that still resolves a container by coordinate.
    """
    if target is None or container is None:
        return False
    path = _find_path(_unwrap(root), target)
    if not path:
        return False
    return container in path[:-1]


def build_scroll_container_selector(el: ET.Element, root: ET.Element) -> Tuple[str, str]:
    """Build the most specific selector for a scroll container element.

    Uses accessibility id / name when available; falls back to a structural
    xpath anchored on the nearest named ancestor so the selector is stable
    even for XCUIElementTypeOther containers that have no accessibility id.
    """
    if _XPATH_ONLY_MODE:
        xpath = _structural_xpath(el, _unwrap(root))
        if xpath:
            return "xpath", xpath
        return "xpath", build_xpath(el)

    sel_type, sel_val = build_selector(el)
    if sel_type in ("accessibility id", "name"):
        return sel_type, sel_val
    xpath = _structural_xpath(el, _unwrap(root))
    if xpath:
        return "xpath", xpath
    return sel_type, sel_val


def hit_test(x: float, y: float, root: ET.Element) -> Optional[ET.Element]:
    actual = _unwrap(root)
    candidates, slop = _collect_hits(x, y, actual)
    if not candidates:
        return None
    prefer_interactive = any(_is_interactive_target(el) for el in candidates)
    exempt = _visibility_exemptions(candidates, actual)
    return min(candidates, key=lambda el: _score(el, prefer_interactive, exempt, slop))


def hit_test_for_swipe(x: float, y: float, root: ET.Element) -> Optional[ET.Element]:
    """Select the best element to act as the swipe target at (x, y).

    For swipe gestures the goal is the *container* being swiped on, not the
    deepest leaf.  The strategy:

    1. Prefer elements that have a stable identifier (accessibility id / label)
       — pick the smallest-area one among those.
    2. If nothing has an identifier, prefer container elements (has children)
       over bare leaves — then pick the smallest container.

    This avoids recording a nameless leaf canvas when the real target is its
    parent (e.g. a photo carousel swiped across its XCUIElementTypeOther
    wrapper rather than the raw canvas child inside it).
    """
    actual = _unwrap(root)
    candidates, slop = _collect_hits(x, y, actual)
    if not candidates:
        return None

    def _swipe_score(el: ET.Element) -> tuple:
        r = _rect(el)
        area = (r[2] * r[3]) if r else float("inf")
        is_interactive = el.tag in INTERACTIVE_TAGS
        is_generic = el.tag in GENERIC_CONTAINER_TAGS
        # Priority: interactive first → penalise generic wrappers (Other/Application/Window)
        # → exact rect hit over a HIT_SLOP-only hit → smallest area (most specific
        # non-generic element wins)
        return (-int(is_interactive), int(is_generic), int(el in slop), area)

    return min(candidates, key=_swipe_score)


def hit_test_long_press_drag_source(x: float, y: float, root: ET.Element) -> Optional[ET.Element]:
    """Select the draggable source for long-press-drag gestures.

    Timeline drag/drop overlays often cover the full track region while the
    deepest hit may be a precise clip/handle element or a generic container.
    Keep stable leaf hits because their bounds make replay coordinates more
    precise; fall back to the owning track cell when the leaf is missing.
    """
    actual = _unwrap(root)
    candidates, _slop = _collect_hits(x, y, actual)
    if not candidates:
        return None

    direct = hit_test(x, y, root)
    if direct is not None and _is_precise_drag_leaf(direct):
        return direct

    track_cells = [el for el in candidates if _is_track_drag_cell(el)]
    if track_cells:
        return min(track_cells, key=_track_drag_cell_score)

    return direct


def hit_test_excluding(x: float, y: float, root: ET.Element, exclude: ET.Element) -> Optional[ET.Element]:
    """Like hit_test but skips *exclude* and all its descendants.

    Used when finding the drop-target of a drag: excludes the element being
    dragged so we don't resolve back to the same element at the end position.
    """
    actual = _unwrap(root)
    candidates, slop = _collect_hits(x, y, actual)
    # Build the set of nodes to exclude (the dragged element and its subtree)
    excluded = set()
    _collect_nodes(exclude, excluded)
    filtered = [el for el in candidates if el not in excluded]
    if not filtered:
        # Fallback: if nothing else is found, accept any candidate
        prefer_interactive = any(_is_interactive_target(el) for el in candidates)
        exempt = _visibility_exemptions(candidates, actual)
        return min(candidates, key=lambda el: _score(el, prefer_interactive, exempt, slop)) if candidates else None
    prefer_interactive = any(_is_interactive_target(el) for el in filtered)
    exempt = _visibility_exemptions(filtered, actual)
    return min(filtered, key=lambda el: _score(el, prefer_interactive, exempt, slop))


def hit_test_drop_target(
    x: float, y: float, root: ET.Element, source: ET.Element
) -> Optional[ET.Element]:
    """Find the best drop-target element at (x, y), excluding the source element.

    Unlike hit_test_excluding, this scorer also **deprioritises** elements that
    share the same tag as *source* — so a container/slot (XCUIElementTypeOther)
    is preferred over another instance of the same type as the dragged element
    (e.g. another XCUIElementTypeImage in the same list).
    """
    actual = _unwrap(root)
    candidates, slop = _collect_hits(x, y, actual)

    source_is_container_like = _is_drop_container_candidate(source) or len(list(source)) > 0
    excluded = set()
    if not source_is_container_like:
        _collect_nodes(source, excluded)
    filtered = [el for el in candidates if el not in excluded]
    if not filtered:
        prefer_interactive = any(_is_interactive_target(el) for el in candidates)
        exempt = _visibility_exemptions(candidates, actual)
        return min(candidates, key=lambda el: _score(el, prefer_interactive, exempt, slop)) if candidates else None

    track_cells = [el for el in filtered if _is_track_drag_cell(el)]
    if track_cells:
        return min(track_cells, key=_track_drag_cell_score)

    drop_containers = [el for el in filtered if _is_drop_container_candidate(el)]
    if drop_containers:
        return min(drop_containers, key=_drop_container_score)

    source_tag = source.tag
    prefer_interactive = any(_is_interactive_target(el) for el in filtered)
    exempt = _visibility_exemptions(filtered, actual)

    def _drop_score(el: ET.Element) -> tuple:
        base = _score(el, prefer_interactive, exempt, slop)
        # Add a penalty tier: same tag as source → sorted after different-tag elements
        same_tag_penalty = int(not source_is_container_like and el.tag == source_tag)
        return (same_tag_penalty,) + base

    return min(filtered, key=_drop_score)


def _is_drop_container_candidate(el: ET.Element) -> bool:
    """Return True for named timeline/drop containers that should win over child leaves."""
    if el.tag not in GENERIC_CONTAINER_TAGS and el.tag not in SCROLLABLE_TAGS:
        return False
    name = (el.attrib.get("name", "") or el.attrib.get("label", "")).strip().lower()
    if not name:
        return False
    return any(
        token in name
        for token in (
            "timeline",
            "backgroundview",
            "validarea",
            "placeholder",
            "drop",
        )
    )


def _is_track_drag_cell(el: ET.Element) -> bool:
    if el.tag != "XCUIElementTypeCell" or not _is_visible(el):
        return False
    name = el.attrib.get("name", "").strip().lower()
    if "multipletrackviewcontroller.multipletrackcell.cell" in name:
        return True
    if "trackcell" in name or "track cell" in name:
        return True
    return any(
        ("piptrackcell" in desc.attrib.get("name", "").strip().lower())
        for desc in el.iter()
    )


def _is_precise_drag_leaf(el: ET.Element) -> bool:
    if not _is_visible(el) or len(list(el)) > 0:
        return False
    if el.tag in GENERIC_CONTAINER_TAGS or el.tag in TAP_CONTAINER_TAGS:
        return False
    return _has_id(el)


def _track_drag_cell_score(el: ET.Element) -> tuple:
    r = _rect(el)
    area = (r[2] * r[3]) if r else float("inf")
    name = el.attrib.get("name", "").strip().lower()
    named_multiple_track = "multipletrackviewcontroller.multipletrackcell.cell" in name
    return (-int(named_multiple_track), area)


def _drop_container_score(el: ET.Element) -> tuple:
    r = _rect(el)
    area = (r[2] * r[3]) if r else float("inf")
    path_depth = len(list(el.iter()))
    return (area, -path_depth)


def _unwrap(root: ET.Element) -> ET.Element:
    if root.tag == "plist":
        aut = root.find("AppiumAUT")
        return aut if aut is not None else root
    if root.tag == "AppiumAUT":
        return root
    return root


def _has_id(el: ET.Element) -> bool:
    a = el.attrib
    name = a.get("name", "").strip()
    label = a.get("label", "").strip()
    return (bool(name) and not name.startswith("0x") and not name.startswith("/")) or bool(label)


def _is_visible(el: ET.Element) -> bool:
    return el.attrib.get("visible", "true") != "false"


def _is_hidden_renderer_layer(el: ET.Element) -> bool:
    if _is_visible(el):
        return False
    name = el.attrib.get("name", "")
    return name.startswith(("rendererViewController.", "rOI."))


def _covers(outer: ET.Element, inner_rect: Tuple[float, float, float, float]) -> bool:
    """Return whether *outer*'s rect fully contains *inner_rect*."""
    o = _rect(outer)
    if not o:
        return False
    ox, oy, ow, oh = o
    ix, iy, iw, ih = inner_rect
    return ox <= ix and oy <= iy and ox + ow >= ix + iw and oy + oh >= iy + ih


def _is_occluded_not_hidden(el: ET.Element, parents: dict) -> bool:
    """Return whether *el* is invisible only because an overlay swallows hit-tests.

    WDA derives `visible` from an accessibility hit-test, not from what is
    actually rendered: an element that is drawn on screen still reports
    visible="false" when some other accessibility element sits on top of it.
    A full-size ``XCUIElementTypeImage`` placed above a progress/wait view is
    the common case — the wait spinner and its labels are what the user sees,
    yet every one of them is reported invisible.

    Only a *later sibling* (drawn above), that is itself visible, is a **leaf**,
    and fully covers the element, counts as such an overlay. The leaf
    requirement is what keeps genuinely hidden subtrees penalised: a view that
    was dismissed or replaced is covered by a structural container with children
    (or by nothing at all), never by a bare leaf.

    ``accessible`` is deliberately NOT part of the test: WDA computes `visible`
    from the rendered hit-point, so any view drawn on top swallows it whether or
    not it publishes itself as an accessibility element. Requiring
    accessible="true" missed the common overlay shape of a decorative cover view
    — e.g. AIArtworkPackSelectionCell's ``selectCheckBoxOverlay``
    (visible="true" accessible="false"), which hides the ``statusOverlay`` /
    ``statusLabel`` ("Processing…") the user actually sees and wants to record.
    """
    r = _rect(el)
    if not r:
        return False
    node = el
    while node in parents:
        parent = parents[node]
        siblings = list(parent)
        idx = siblings.index(node)
        for sib in siblings[idx + 1:]:
            a = sib.attrib
            if (
                a.get("visible") == "true"
                and len(sib) == 0
                and _covers(sib, r)
            ):
                return True
        node = parent
    return False


def _visibility_exemptions(candidates: List[ET.Element], root: ET.Element) -> frozenset:
    """Candidates whose visible="false" is a WDA occlusion misjudgement.

    These are scored as visible by ``_score``. Computed per hit-test call over
    the candidate list only, so the parent map is built at most once and only
    when some candidate is actually invisible.
    """
    hidden = [el for el in candidates if not _is_visible(el)]
    if not hidden:
        return frozenset()
    parents = {child: parent for parent in root.iter() for child in parent}
    return frozenset(el for el in hidden if _is_occluded_not_hidden(el, parents))


def _is_interactive_target(el: ET.Element) -> bool:
    return el.tag in INTERACTIVE_TAGS and not _is_hidden_renderer_layer(el)


def _score(
    el: ET.Element,
    prefer_interactive_over_generic: bool = False,
    visibility_exempt: frozenset = frozenset(),
    slop_hits: frozenset = frozenset(),
) -> tuple:
    r = _rect(el)
    area = (r[2] * r[3]) if r else float("inf")
    is_hidden_renderer_layer = _is_hidden_renderer_layer(el)
    has_id = _has_id(el)
    quality = get_selector_quality(el)
    is_interactive = _is_interactive_target(el)
    has_children = len(list(el)) > 0
    is_container = el.tag in TAP_CONTAINER_TAGS
    is_generic_wrapper = (
        prefer_interactive_over_generic
        and el.tag in GENERIC_CONTAINER_TAGS
        and not is_interactive
    )
    # Stable ID bonus only applies to leaf elements (no children).
    # Container-level stable IDs (e.g. ViewController root views with
    # "bundleid.ClassName" names) must not override smaller child elements.
    # WDA can keep inactive renderer layers in the hierarchy with stale frames
    # that overlap visible controls. Do not let those hidden renderer / ROI
    # leaves win purely because they have stable accessibility IDs.
    # An element WDA reported invisible only because an overlay swallows the
    # hit-test is on screen for real — score it as visible.
    is_really_visible = _is_visible(el)
    is_visible = is_really_visible or el in visibility_exempt
    has_stable_id = (
        quality in ("id", "id_eq_label")
        and not has_children
        and not is_hidden_renderer_layer
        and is_visible
    )
    # Priority:
    #   1. Non-container over structural containers (CollectionView, ScrollView …)
    #   2. Visible over invisible (WDA keeps hidden siblings in the tree with
    #      stale frames that overlap visible content — never let them win).
    #      Elements exempted by _visibility_exemptions() count as visible.
    #   3. Interactive controls over generic XCUIElementTypeOther/View wrappers
    #   4. Visible stable ID leaf (non-indexed, no children) over anything without one
    #   5. Visible interactive element (Button, TextField …) as tiebreaker
    #   6. Exact rect hit over a HIT_SLOP-only hit — a thin element next to the
    #      real target never wins while that target is genuinely under the finger
    #   7. Smallest area (most specific element)
    #   8. Genuinely visible over occlusion-exempt — when two elements share the
    #      same rect the exemption cannot tell them apart, so document order
    #      decided the winner (e.g. a not-yet-loaded thumbnailImageView stacked
    #      exactly under the "Processing..." processingLabel that covers it).
    #      Ranked *after* area so the original occlusion cases are untouched:
    #      there the exempt element is the smaller one and already wins above.
    #   9. Has any identifier > pure xpath fallback
    return (
        int(is_container),
        int(not is_visible),
        int(is_generic_wrapper),
        -int(has_stable_id),
        -int(is_interactive),
        int(el in slop_hits),
        area,
        int(not is_really_visible),
        -int(has_id),
        int(has_children),
    )


def _hit_rect(r: Tuple[float, float, float, float]) -> Tuple[float, float, float, float]:
    """Return *r* grown to at least HIT_SLOP on each axis, centred on the original."""
    x, y, w, h = r
    if w < HIT_SLOP:
        x -= (HIT_SLOP - w) / 2
        w = HIT_SLOP
    if h < HIT_SLOP:
        y -= (HIT_SLOP - h) / 2
        h = HIT_SLOP
    return x, y, w, h


def _collect(
    x: float,
    y: float,
    el: ET.Element,
    out: List[ET.Element],
    slop_out: Optional[set] = None,
):
    r = _rect(el)
    if r:
        hx, hy, hw, hh = _hit_rect(r)
        if hx <= x <= hx + hw and hy <= y <= hy + hh:
            out.append(el)
            if slop_out is not None and not (
                r[0] <= x <= r[0] + r[2] and r[1] <= y <= r[1] + r[3]
            ):
                slop_out.add(el)
    for child in el:
        _collect(x, y, child, out, slop_out)


def _collect_hits(
    x: float, y: float, root: ET.Element
) -> Tuple[List[ET.Element], frozenset]:
    """Collect the candidates at (x, y) plus the subset matched only via HIT_SLOP."""
    out: List[ET.Element] = []
    slop: set = set()
    _collect(x, y, root, out, slop)
    return out, frozenset(slop)


def _collect_nodes(el: ET.Element, out: set):
    """Collect el and all its descendants into a set (for exclusion)."""
    out.add(el)
    for child in el:
        _collect_nodes(child, out)


def _rect(el: ET.Element) -> Optional[Tuple[float, float, float, float]]:
    a = el.attrib
    if "x" in a and "width" in a:
        try:
            return float(a["x"]), float(a["y"]), float(a["width"]), float(a["height"])
        except (ValueError, KeyError):
            pass
    return None


def _area(el: ET.Element) -> float:
    r = _rect(el)
    return (r[2] * r[3]) if r else float("inf")


def _find_path(root: ET.Element, target: ET.Element) -> Optional[List[ET.Element]]:
    if root is target:
        return [root]
    for child in root:
        sub = _find_path(child, target)
        if sub is not None:
            return [root] + sub
    return None


def _structural_xpath(target: ET.Element, root: ET.Element) -> Optional[str]:
    """Generate an xpath anchored on the deepest named ancestor of *target*."""
    path = _find_path(root, target)
    if not path:
        return None

    # Find the deepest ancestor that has a stable name attribute
    anchor_idx = 0
    for i, el in enumerate(path):
        name = el.attrib.get("name", "").strip()
        if name and not name.startswith("0x") and not name.startswith("/"):
            anchor_idx = i

    anchor = path[anchor_idx]
    anchor_name = anchor.attrib.get("name", "").strip()
    if not anchor_name:
        return None

    anchor_predicates = [f"@name={xpath_literal(anchor_name)}"]
    anchor_label = anchor.attrib.get("label", "").strip()
    if anchor_label and anchor_label != anchor_name and _has_same_name_peer(anchor, root):
        anchor_predicates.append(f"@label={xpath_literal(anchor_label)}")
    parts = [f"//{anchor.tag}[{' and '.join(anchor_predicates)}]"]
    for i in range(anchor_idx + 1, len(path)):
        el = path[i]
        parent = path[i - 1]
        same_tag_siblings = [c for c in parent if c.tag == el.tag]
        if len(same_tag_siblings) > 1:
            idx = same_tag_siblings.index(el) + 1  # xpath is 1-based
            parts.append(f"{el.tag}[{idx}]")
        else:
            parts.append(el.tag)
    return "/".join(parts)


def _has_same_name_peer(target: ET.Element, root: ET.Element) -> bool:
    name = target.attrib.get("name", "").strip()
    if not name:
        return False
    matches = 0
    for el in root.iter():
        if el.tag == target.tag and el.attrib.get("name", "").strip() == name:
            matches += 1
            if matches > 1:
                return True
    return False


def serialize(root: ET.Element) -> List[dict]:
    out: List[dict] = []
    _ser(_unwrap(root), out)
    return out


def _ser(el: ET.Element, out: List[dict]):
    # Post-order: children before parent so the frontend hit-test encounters
    # leaf (small) elements first and parents last.
    for child in el:
        _ser(child, out)
    r = _rect(el)
    if r and r[2] > 0 and r[3] > 0:
        a = el.attrib
        out.append(
            {
                "tag": el.tag.replace("XCUIElementType", ""),
                "name": a.get("name", ""),
                "label": a.get("label", ""),
                "enabled": a.get("enabled") == "true",
                "rect": {"x": r[0], "y": r[1], "w": r[2], "h": r[3]},
            }
        )
