import re
import xml.etree.ElementTree as ET
from typing import Tuple

_ID_INDEXED_RE = re.compile(r'-\d+$')


def get_selector_quality(el: ET.Element) -> str:
    """Classify selector quality for UI color coding.

    Returns one of:
      "id"          – has a proper accessibility id (id != label, no trailing -N)
      "id_indexed"  – accessibility id ends with -<digits> (e.g. Cell-3) → fragile index
      "id_eq_label" – accessibility id exists but equals the label
      "label_only"  – no id, only a label attribute
      "xpath_only"  – nothing stable; xpath fallback
    """
    a = el.attrib
    name = a.get("name", "").strip()
    label = a.get("label", "").strip()
    if name and not name.startswith("0x") and not name.startswith("/"):
        if label and name == label:
            return "id_eq_label"
        if _ID_INDEXED_RE.search(name):
            return "id_indexed"
        return "id"
    if label:
        return "label_only"
    return "xpath_only"


def build_selector(el: ET.Element) -> Tuple[str, str]:
    a = el.attrib
    tag = el.tag

    # 1. Accessibility ID — most stable across app versions
    #    Skip: memory pointers (0x...) and file/bundle paths (/private/... or /)
    name = a.get("name", "").strip()
    if name and not name.startswith("0x") and not name.startswith("/"):
        return "accessibility id", name

    # 2. Accessibility label
    label = a.get("label", "").strip()
    if label:
        return "name", label

    # 3. XPath fallback
    return "xpath", f"//{tag}"


def build_xpath(el: ET.Element) -> str:
    """Return the most specific XPath expression for an element.

    Priority:
      1. //{tag}[@name='value']  — when a stable name attribute exists
      2. //{tag}[@label='value'] — when only a label is available
      3. //{tag}                 — bare tag fallback
    """
    a = el.attrib
    tag = el.tag
    name = a.get("name", "").strip()
    if name and not name.startswith("0x") and not name.startswith("/"):
        return f"//{tag}[@name='{name}']"
    label = a.get("label", "").strip()
    if label:
        return f"//{tag}[@label='{label}']"
    return f"//{tag}"
