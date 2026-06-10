"""
One-time migration: add hierarchy_file_xpath entries to all existing fixtures,
then regenerate test_gen3b_xpath_variant.py for each fixture.

Run from the project root:
    python test_unittest/migrate_xpath_variants.py
"""
import copy
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.hittest import _unwrap as _ht_unwrap, _rect as _el_rect
from app.unit_test_gen import generate_unit_tests

_FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _make_xpath_variant_xml(root: ET.Element, output: dict):
    """Strip name/label from the target element; return modified XML string or None."""
    target = output.get("target") or output.get("start_target")
    if not target or target.get("type") in ("coordinate", None):
        return None
    if target.get("selector_quality") == "xpath_only":
        return None
    bounds = target.get("bounds")
    if not bounds:
        return None
    bx, by, bw, bh = bounds["x"], bounds["y"], bounds["w"], bounds["h"]
    root_copy = copy.deepcopy(root)
    for node in _ht_unwrap(root_copy).iter():
        r = _el_rect(node)
        if r and int(r[0]) == bx and int(r[1]) == by and int(r[2]) == bw and int(r[3]) == bh:
            node.attrib.pop("name", None)
            node.attrib.pop("label", None)
            break
    return ET.tostring(root_copy, encoding="unicode")


def migrate_fixture(fixture_dir: Path) -> int:
    capture_file = fixture_dir / "capture.json"
    if not capture_file.exists():
        return 0

    payload = json.loads(capture_file.read_text(encoding="utf-8"))
    entries = payload.get("entries", [])
    added = 0

    for i, entry in enumerate(entries):
        if entry.get("hierarchy_file_xpath"):
            continue
        hfile = entry.get("hierarchy_file")
        if not hfile:
            continue
        xml_path = fixture_dir / hfile
        if not xml_path.exists():
            continue
        output = entry.get("output", {})
        root = ET.fromstring(xml_path.read_text(encoding="utf-8"))
        xpath_xml = _make_xpath_variant_xml(root, output)
        if xpath_xml:
            xml_name_xpath = f"hierarchy_{i:03d}_xpath.xml"
            (fixture_dir / xml_name_xpath).write_text(xpath_xml, encoding="utf-8")
            entry["hierarchy_file_xpath"] = xml_name_xpath
            added += 1
            print(f"  [{i:03d}] created {xml_name_xpath}")

    if added:
        capture_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        generate_unit_tests(fixture_dir.name, len(entries))
        print(f"  → {fixture_dir.name}: {added} xpath variant(s) added, tests regenerated")

    return added


def main():
    if not _FIXTURES_DIR.exists():
        print(f"Fixtures dir not found: {_FIXTURES_DIR}")
        return
    dirs = sorted(d for d in _FIXTURES_DIR.iterdir() if d.is_dir())
    print(f"Processing {len(dirs)} fixtures...\n")
    total = 0
    for d in dirs:
        n = migrate_fixture(d)
        total += n
    print(f"\nDone. {total} xpath-variant hierarchies added across {len(dirs)} fixtures.")


if __name__ == "__main__":
    main()
