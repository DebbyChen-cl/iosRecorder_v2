# Recorder — Code Generation Rules

You are working on the **test script generator** (`app/codegen.py`).

Read this file before making changes:
- [app/codegen.py](../../../app/codegen.py)

---

## What It Does

`generate_script(steps, case_name)` converts a list of recorded step dicts into a complete, ready-to-run `pytest` file.

Output structure:
```python
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("<case_name>")
def test_<safe_name>(actions: DriverActions):
    with step("[Action] <description>"):
        actions.<method>(...)
    with step("[Verify] <description>"):
        if not actions.<verify_method>(...):
            assert False, '<element> is not visible'
    assert True
```

---

## Core Functions

| Function | Purpose |
|----------|---------|
| `generate_header(case_name)` | Fixed import block + marker + function signature |
| `_action_call(step)` | Maps one step dict → `(label, [code_lines])` |
| `generate_script(steps, case_name)` | Combines header + all step bodies |
| `_safe_name(name)` | Converts case name to valid Python identifier |
| `_q(value)` | Escapes backslash and single-quote for Python string literals |
| `_by(selector_type)` | Maps selector type string → `AppiumBy.*` constant string |
| `_swipe_direction(dx, dy)` | Derives direction from coordinate delta |
| `_merge_screenshot_diff_long_press_compare(steps)` | Merges `before -> long_press -> after` screenshot-diff pattern into a long-press-with-capture action when compare rules match |

## Recording Rules Config

`app/codegen.py` reads compare-related generation rules from `recording_rules.json` (project root).

Current keys:
- `long_press_compare_keywords`: list of keywords to match in element id value (default `['compare']`)
- `long_press_compare_selector_types`: allowed selector types for keyword matching (default `['accessibility id', 'id']`)

When the file is missing or invalid JSON, codegen falls back to defaults.

---

## Adding a New Action Type

1. Add a new `if action == "<new_action>":` block in `_action_call()`
2. Follow the same pattern:
   - Check `has_el = t and t.get("type") != "coordinate"` first
   - If element found → use locator-based `actions.*_by_locator()` or `actions.*_within_element()`
   - If no element → use coordinates-based call or a `# comment` fallback (never raise)
   - Return `(label, [code_lines])`
3. Add the corresponding method to `DriverActions` in `pytest/driver/driver_actions.py`
4. If a new `AppiumBy.*` constant is needed, add it to `_BY_MAP`

---

## Step Dict Schema

```python
{
  "action":           str,    # required — matches if/elif chain in _action_call
  "coords":           dict,   # {"x": int, "y": int} OR {"x1":int,"y1":int,"x2":int,"y2":int}
  "target":           dict | None,
    # {
    #   "type": "accessibility id" | "name" | "xpath" | "coordinate",
    #   "value": str,
    #   "offset_pct": {"x": float, "y": float},  # 0–100, optional
    #   "selector_quality": "id" | "id_indexed" | "id_eq_label" | "label_only" | "xpath_only",  # optional
    #   "bounds": {"x": int, "y": int, "w": int, "h": int},  # device points, optional (new)
    # }
  "duration":         int,    # milliseconds (long_press, swipe, drag, pinch)
  "scale":            float,  # pinch scale
  "rotation":         float,  # degrees — passed directly to actions.rotate() (no conversion in codegen)
  "text":             str,    # type_text
  "bundle_id":        str,    # launch_app, terminate_app
  "app_name":         str,    # launch_app / terminate_app display name (optional)
  "expected_text":    str,    # verify_get_text
  "screenshot_name":  str,    # verify_screenshot_*
  "phase":            str,    # verify_screenshot_diff: "before" | "after"
  "direction":        str,    # swipe: cardinal direction stored at record time by _record_move
  "velocity":         float,  # swipe: px/s stored at record time (max(50, min(5000, dist*1000/dur)))
  "fingers":          int,    # multi_finger_tap
  "scroll_container": dict,   # tap/long_press/scroll: innermost scrollable container at the tap coordinate
                              #   (recorded automatically; used by tap_with_scroll for scroll-fallback)
                              # scroll: also used to identify the container for scroll_until()
  "scroll_offsets":   dict,   # scroll: gesture fractions relative to scroll_container rect
    # {
    #   "start_x_pct": float,  # 0.0–1.0, start x as fraction of container width
    #   "start_y_pct": float,
    #   "end_x_pct":   float,
    #   "end_y_pct":   float,
    # }
    # Used by codegen to pass offset_start / offset_end / velocity to scroll_until().
    # velocity is computed as: int(distance_px * 1000 / duration_ms), clamped to [50, 2000].
  "scroll_target":    dict,   # scroll: target element to scroll until visible
  "start_target":     dict,   # swipe/drag: element at the gesture start point
  # ── Pre-gesture screenshot (set for every recorded step; stripped from GET /api/steps) ──
  "pre_screenshot":      str,   # base64 PNG captured before the action is sent to the device
  "pre_screenshot_size": dict,  # {"width": int, "height": int} — device screen dimensions
}
```

---

## Code Style Rules for Generated Output

- **Indentation**: always 4 spaces (function body level = 4, inside `with step` = 8)
- **String quoting**: single quotes inside generated code; use `_q()` to escape content
- **No trailing newlines** inside `with step(...)` blocks — one call per block
- **`assert True`** appended after all `with step` blocks at function body level (4 spaces indent)
- **Screenshot comparison pattern**: `verify_screenshot_gt` / `verify_screenshot_diff` steps only capture inline (`capture_for_gt` / `capture_for_preview`); a single `with step("[Verify] Screenshot comparisons"): actions.run_screenshot_comparisons()` is appended **once at the end** of the test when any screenshot steps exist — AND logic, all failures raised together
- **Long-press compare shortcut**: when the sequence is exactly `verify_screenshot_diff(before) -> long_press -> verify_screenshot_diff(after)` and the long-press target element id matches `recording_rules.json` keywords, codegen keeps `before` and replaces the remaining two steps with `long_press_capture_after_during_hold` so the AFTER image is captured during the press hold window
- **`verify_visible` pattern**: generates `if not actions.verify_visible(...): assert False, '<val> is not visible'` (two lines inside the `with step` block)
- **`verify_not_visible` pattern**: generates `actions.verify_not_visible(...)` (single line; the method raises `AssertionError` internally on failure)
- **Label format**:
  - `[Action] ...` for all gesture actions (tap, swipe, drag, pinch, etc.)
  - `[Verify] ...` for all assertion actions (verify_visible, verify_text, screenshot)
- **Fallback `# comment`** when no element matched — code must always be valid Python
- **Duration**: long_press and drag convert ms → seconds: `round(ms / 1000, 2)`
- **Pinch velocity**: `max(0.1, |scale - 1| / (duration_ms / 1000))` — derived from recorded duration
- **Swipe velocity**: stored in step dict at record time; codegen reads directly from `step["velocity"]`
- **Rotation**: degrees passed as-is; `DriverActions.rotate()` converts to radians internally
- **Percent offsets**: pass as floats (e.g. `49.5`, not `0.495`)

---

## Never Do

- Never raise exceptions or return `None` from `_action_call()` — always return a tuple
- Never hardcode `AppiumBy.ACCESSIBILITY_ID` as a string; use `_by()` to look it up
- Never skip the `with step(...)` wrapper — ReportPortal requires it
- Never modify the import block in `generate_header()` without updating `conftest.py` fixtures
