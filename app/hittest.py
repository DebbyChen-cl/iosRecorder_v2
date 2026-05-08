import xml.etree.ElementTree as ET
from typing import List, Optional, Tuple

from .selector import build_selector

INTERACTIVE_TAGS = frozenset(
    {
        "XCUIElementTypeButton",
        "XCUIElementTypeTextField",
        "XCUIElementTypeSecureTextField",
        "XCUIElementTypeSwitch",
        "XCUIElementTypeLink",
        "XCUIElementTypeCell",
        "XCUIElementTypeCheckBox",
        "XCUIElementTypeSlider",
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
    return (bool(name) and not name.startswith("0x")) or bool(label)


def _score(el: ET.Element) -> tuple:
    r = _rect(el)
    area = (r[2] * r[3]) if r else float("inf")
    is_interactive = el.tag in INTERACTIVE_TAGS
    has_id = _has_id(el)
    has_children = len(list(el)) > 0
    # Priority: interactive > smallest area > has identifier > leaf
    return (-int(is_interactive), area, -int(has_id), int(has_children))


def _collect(x: float, y: float, el: ET.Element, out: List[ET.Element]):
    r = _rect(el)
    if r and r[0] <= x <= r[0] + r[2] and r[1] <= y <= r[1] + r[3]:
        out.append(el)
    for child in el:
        _collect(x, y, child, out)


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
        if name and not name.startswith("0x"):
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
    for child in el:
        _ser(child, out)
