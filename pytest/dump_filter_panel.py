# ─────────────────────────────────────────────
# dump_filter_panel.py  –  one-off diagnostic
# ─────────────────────────────────────────────
# Walks both collection views of the filter panel from start to end and prints
# every cell it can see, so we can tell whether "Custom Filter" exists at all,
# and if so which container actually owns it.
#
# Usage:
#   1. On the device, open the app and navigate to the filter panel manually
#      (Edit -> pick a photo -> Filter) so the look list is on screen.
#   2. python3 pytest/dump_filter_panel.py
#
# Read-only apart from the scroll gestures it performs on the two strips.

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from appium.webdriver.common.appiumby import AppiumBy

from driver.driver_setup import create_driver

CATEGORY = "cmsCategoryCollectionViewCollectionView"
LOOKS = "lookEffectCollectionViewCollectionView"
NEEDLE = "custom"          # case-insensitive substring we are hunting for
MAX_SCROLLS = 40


def _labels(container):
    """Return (name, label, x, w) for every descendant cell / static text."""
    out = []
    for tag in ("XCUIElementTypeCell", "XCUIElementTypeStaticText"):
        for el in container.find_elements(AppiumBy.CLASS_NAME, tag):
            try:
                r = el.rect
                out.append((tag.replace("XCUIElementType", ""),
                            el.get_attribute("name") or "",
                            el.get_attribute("label") or "",
                            r["x"], r["width"]))
            except Exception:
                pass
    return out


def _drag(driver, container, direction):
    r = container.rect
    cx, cy = r["x"] + r["width"] / 2, r["y"] + r["height"] / 2
    off = r["width"] * 0.35
    frm, to = (cx + off, cx - off) if direction == "left" else (cx - off, cx + off)
    driver.execute_script("mobile: dragFromToWithVelocity", {
        "fromX": frm, "fromY": cy, "toX": to, "toY": cy,
        "velocity": 300, "pressDuration": 0.05, "holdDuration": 0.05,
    })


def sweep(driver, container_id):
    print(f"\n{'=' * 78}\n{container_id}\n{'=' * 78}")
    try:
        container = driver.find_element(AppiumBy.ACCESSIBILITY_ID, container_id)
    except Exception as exc:
        print(f"  !! container not found: {exc}")
        return set()

    r = container.rect
    print(f"  rect = x={r['x']} y={r['y']} w={r['width']} h={r['height']}")

    # Rewind to the start so the sweep always begins from a known position.
    for _ in range(MAX_SCROLLS):
        before = _labels(container)
        _drag(driver, container, "right")
        if _labels(container) == before:
            break

    seen, hits = {}, []
    for i in range(MAX_SCROLLS):
        before = _labels(container)
        for tag, name, label, x, w in before:
            key = (tag, name, label)
            if key not in seen:
                seen[key] = i
                if NEEDLE in f"{name} {label}".lower():
                    hits.append((i, tag, name, label, x, w))
        _drag(driver, container, "left")
        if _labels(container) == before:
            print(f"  reached the end after {i + 1} scrolls")
            break
    else:
        print(f"  !! still moving after {MAX_SCROLLS} scrolls — list is longer than the sweep")

    print(f"  {len(seen)} distinct elements seen:")
    for (tag, name, label), step in sorted(seen.items(), key=lambda kv: kv[1]):
        shown = name or f"(label only: {label})"
        print(f"    [scroll {step:2}] {tag:11} {shown}")

    if hits:
        print(f"\n  >>> MATCHES for {NEEDLE!r}:")
        for step, tag, name, label, x, w in hits:
            print(f"    scroll {step}: {tag} name={name!r} label={label!r} x={x} w={w}")
    else:
        print(f"\n  >>> no element matching {NEEDLE!r} in this container")
    return set(seen)


def main():
    driver = create_driver()
    try:
        sweep(driver, CATEGORY)
        sweep(driver, LOOKS)
        print(f"\n{'=' * 78}\nGlobal search (whole screen, current state)\n{'=' * 78}")
        for by, val in ((AppiumBy.ACCESSIBILITY_ID, "Custom Filter"),
                        (AppiumBy.IOS_PREDICATE, "name CONTAINS[c] 'custom' OR label CONTAINS[c] 'custom'")):
            try:
                found = driver.find_elements(by, val)
                print(f"  {by} {val!r} -> {len(found)} match(es)")
                for el in found:
                    print(f"     {el.tag_name} name={el.get_attribute('name')!r} "
                          f"label={el.get_attribute('label')!r} rect={el.rect}")
            except Exception as exc:
                print(f"  {by} {val!r} -> error: {exc}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
