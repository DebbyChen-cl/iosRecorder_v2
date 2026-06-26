import os
import re
import xml.etree.ElementTree as ET
from typing import Optional, Tuple

_ID_INDEXED_RE = re.compile(r'-\d+$')
_XPATH_ONLY_MODE = os.environ.get("RECORDER_XPATH_ONLY") == "1"


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
    if _XPATH_ONLY_MODE:
        return "xpath", build_xpath(el)

    a = el.attrib

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
    return "xpath", build_xpath(el)


def xpath_literal(value: str, prefer_double: bool = True) -> str:
    """Return an XPath 1.0 string literal for *value*."""
    if not prefer_double and "'" not in value:
        return f"'{value}'"
    if '"' not in value:
        return f'"{value}"'
    if "'" not in value:
        return f"'{value}'"
    return "concat(" + ", '\"', ".join(f'"{part}"' for part in value.split('"')) + ")"


def build_xpath(el: ET.Element, include_label: bool = False) -> str:
    """Return the most specific XPath expression for an element.

    Priority:
      1. //{tag}[@name='value' and @label='value'] - when explicitly requested
      2. //{tag}[@name='value']  - when a stable name attribute exists
      3. //{tag}[@label='value'] - when only a label is available
      4. //{tag}[@value='value'] - when only a value is available
      5. //{tag}                 - bare tag fallback
    """
    a = el.attrib
    tag = el.tag
    name = a.get("name", "").strip()
    label = a.get("label", "").strip()
    value = a.get("value", "").strip()
    if name and not name.startswith("0x") and not name.startswith("/"):
        predicates = [f"@name={xpath_literal(name, prefer_double=False)}"]
        if include_label and label and label != name:
            predicates.append(f"@label={xpath_literal(label, prefer_double=False)}")
        return f"//{tag}[{' and '.join(predicates)}]"
    if label:
        return f"//{tag}[@label={xpath_literal(label, prefer_double=False)}]"
    if value:
        return f"//{tag}[@value={xpath_literal(value)}]"
    return f"//{tag}"


def build_indexed_xpath_if_duplicate(el: ET.Element, root: ET.Element) -> Optional[str]:
    """Return a disambiguated XPath when the element's name/label/value is not unique."""
    actual = _unwrap_root(root)
    tag = el.tag
    name = el.attrib.get("name", "").strip()
    label = el.attrib.get("label", "").strip()
    value = el.attrib.get("value", "").strip()

    if name and not name.startswith("0x") and not name.startswith("/"):
        name_matches = [
            node for node in actual.iter()
            if node.tag == tag and node.attrib.get("name", "").strip() == name
        ]
        if len(name_matches) <= 1 or el not in name_matches:
            return None

        if label and label != name:
            name_label_matches = [
                node for node in name_matches
                if node.attrib.get("label", "").strip() == label
            ]
            base = (
                f"//{tag}[@name={xpath_literal(name)} "
                f"and @label={xpath_literal(label)}]"
            )
            if len(name_label_matches) == 1 and name_label_matches[0] is el:
                return base
            if len(name_label_matches) > 1 and el in name_label_matches:
                return f"({base})[{name_label_matches.index(el) + 1}]"

        base = f"//{tag}[@name={xpath_literal(name)}]"
        return f"({base})[{name_matches.index(el) + 1}]"
    elif label:
        attr = "label"
        attr_value = label
    elif value:
        attr = "value"
        attr_value = value
    else:
        return None

    matches = [
        node for node in actual.iter()
        if node.tag == tag and node.attrib.get(attr, "").strip() == attr_value
    ]
    if len(matches) <= 1 or el not in matches:
        return None

    base = f"//{tag}[@{attr}={xpath_literal(attr_value)}]"
    return f"({base})[{matches.index(el) + 1}]"


def _unwrap_root(root: ET.Element) -> ET.Element:
    if root.tag == "plist":
        aut = root.find("AppiumAUT")
        return aut if aut is not None else root
    if root.tag == "AppiumAUT":
        return root
    return root
