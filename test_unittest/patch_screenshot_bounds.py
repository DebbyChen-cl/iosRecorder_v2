"""
Patch existing fixtures: add 'bounds' back into input for verify_screenshot_gt/diff entries.
Run once from project root: python3 test_unittest/patch_screenshot_bounds.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from app.unit_test_gen import generate_unit_tests

_FIXTURES_DIR = Path(__file__).parent / "fixtures"
_SCREENSHOT_ACTIONS = {"verify_screenshot_gt", "verify_screenshot_diff"}


def patch_fixture(fixture_dir: Path) -> int:
    capture_file = fixture_dir / "capture.json"
    if not capture_file.exists():
        return 0
    payload = json.loads(capture_file.read_text(encoding="utf-8"))
    entries = payload.get("entries", [])
    patched = 0
    for entry in entries:
        inp = entry.get("input", {})
        if inp.get("action") not in _SCREENSHOT_ACTIONS:
            continue
        if "bounds" in inp:
            continue
        bounds = entry.get("output", {}).get("bounds")
        if bounds:
            inp["bounds"] = bounds
            patched += 1
    if patched:
        capture_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  {fixture_dir.name}: patched {patched} entry(entries)")
    return patched


def main():
    dirs = sorted(d for d in _FIXTURES_DIR.iterdir() if d.is_dir())
    total = 0
    for d in dirs:
        total += patch_fixture(d)
    print(f"Done. {total} entries patched.")


if __name__ == "__main__":
    main()
