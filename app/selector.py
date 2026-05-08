import xml.etree.ElementTree as ET
from typing import Tuple

INPUT_TAGS = frozenset(
    {"XCUIElementTypeTextField", "XCUIElementTypeSecureTextField", "XCUIElementTypeStaticText"}
)


def build_selector(el: ET.Element) -> Tuple[str, str]:
    a = el.attrib
    tag = el.tag

    # 1. Accessibility ID — most stable across app versions
    name = a.get("name", "").strip()
    if name and not name.startswith("0x"):
        return "accessibility id", name

    # 2. Accessibility label
    label = a.get("label", "").strip()
    if label:
        return "name", label

    # 3. Value (inputs only)
    value = a.get("value", "").strip()
    if value and tag in INPUT_TAGS:
        return "xpath", f'//{tag}[@value="{_esc(value)}"]'

    # 4. XPath fallback
    return "xpath", f"//{tag}"


def _esc(s: str) -> str:
    return s.replace('"', '\\"')
