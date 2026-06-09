import xml.etree.ElementTree as ET
from typing import List, Optional, Tuple

from .selector import build_selector, get_selector_quality

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
# swipe / gesture target.  Penalised in hit_test_for_swipe so that more
# specific siblings (e.g. XCUIElementTypeImage) are preferred.
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


def find_scroll_container(x: float, y: float, root: ET.Element) -> Optional[ET.Element]:
    """Return the innermost scrollable element that contains (x, y).

    Checks standard scrollable tags first; falls back to any element with
    scrollable="true" (WDA exposes this for non-standard scroll views).
    """
    actual = _unwrap(root)
    candidates: List[ET.Element] = []
    _collect(x, y, actual, candidates)
    scrollable = [el for el in candidates if el.tag in SCROLLABLE_TAGS]
    if not scrollable:
        scrollable = [el for el in candidates if el.attrib.get("scrollable") == "true"]
    if not scrollable:
        return None
    return min(scrollable, key=_area)


def build_scroll_container_selector(el: ET.Element, root: ET.Element) -> Tuple[str, str]:
    """Build the most specific selector for a scroll container element.

    Uses accessibility id / name when available; falls back to a structural
    xpath anchored on the nearest named ancestor so the selector is stable
    even for XCUIElementTypeOther containers that have no accessibility id.
    """
    sel_type, sel_val = build_selector(el)
    if sel_type in ("accessibility id", "name"):
        return sel_type, sel_val
    xpath = _structural_xpath(el, _unwrap(root))
    if xpath:
        return "xpath", xpath
    return sel_type, sel_val


def hit_test(x: float, y: float, root: ET.Element) -> Optional[ET.Element]:
    actual = _unwrap(root)
    candidates: List[ET.Element] = []
    _collect(x, y, actual, candidates)
    if not candidates:
        return None
    return min(candidates, key=_score)


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
    candidates: List[ET.Element] = []
    _collect(x, y, actual, candidates)
    if not candidates:
        return None

    def _swipe_score(el: ET.Element) -> tuple:
        r = _rect(el)
        area = (r[2] * r[3]) if r else float("inf")
        is_interactive = el.tag in INTERACTIVE_TAGS
        is_generic = el.tag in GENERIC_CONTAINER_TAGS
        # Priority: interactive first → penalise generic wrappers (Other/Application/Window)
        # → smallest area (most specific non-generic element wins)
        return (-int(is_interactive), int(is_generic), area)

    return min(candidates, key=_swipe_score)


def hit_test_excluding(x: float, y: float, root: ET.Element, exclude: ET.Element) -> Optional[ET.Element]:
    """Like hit_test but skips *exclude* and all its descendants.

    Used when finding the drop-target of a drag: excludes the element being
    dragged so we don't resolve back to the same element at the end position.
    """
    actual = _unwrap(root)
    candidates: List[ET.Element] = []
    _collect(x, y, actual, candidates)
    # Build the set of nodes to exclude (the dragged element and its subtree)
    excluded = set()
    _collect_nodes(exclude, excluded)
    filtered = [el for el in candidates if el not in excluded]
    if not filtered:
        # Fallback: if nothing else is found, accept any candidate
        return min(candidates, key=_score) if candidates else None
    return min(filtered, key=_score)


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
    candidates: List[ET.Element] = []
    _collect(x, y, actual, candidates)

    excluded = set()
    _collect_nodes(source, excluded)
    filtered = [el for el in candidates if el not in excluded]
    if not filtered:
        return min(candidates, key=_score) if candidates else None

    source_tag = source.tag

    def _drop_score(el: ET.Element) -> tuple:
        base = _score(el)
        # Add a penalty tier: same tag as source → sorted after different-tag elements
        same_tag_penalty = int(el.tag == source_tag)
        return (same_tag_penalty,) + base

    return min(filtered, key=_drop_score)


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


def _score(el: ET.Element) -> tuple:
    r = _rect(el)
    area = (r[2] * r[3]) if r else float("inf")
    is_interactive = el.tag in INTERACTIVE_TAGS
    has_id = _has_id(el)
    quality = get_selector_quality(el)
    has_children = len(list(el)) > 0
    is_container = el.tag in TAP_CONTAINER_TAGS
    # Stable ID bonus only applies to leaf elements (no children).
    # Container-level stable IDs (e.g. ViewController root views with
    # "bundleid.ClassName" names) must not override smaller child elements.
    has_stable_id = quality in ("id", "id_eq_label") and not has_children
    # Priority:
    #   1. Non-container over structural containers (CollectionView, ScrollView …)
    #   2. Stable ID leaf (non-indexed, no children) over anything without one
    #   3. Interactive (Button, TextField …) as tiebreaker within same ID quality
    #   4. Smallest area (most specific element)
    #   5. Has any identifier > pure xpath fallback
    return (int(is_container), -int(has_stable_id), -int(is_interactive), area, -int(has_id), int(has_children))


def _collect(x: float, y: float, el: ET.Element, out: List[ET.Element]):
    r = _rect(el)
    if r and r[0] <= x <= r[0] + r[2] and r[1] <= y <= r[1] + r[3]:
        out.append(el)
    for child in el:
        _collect(x, y, child, out)


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

    parts = [f'//{anchor.tag}[@name="{anchor_name}"]']
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
