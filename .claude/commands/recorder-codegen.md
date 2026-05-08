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
        actions.<verify_method>(...)
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
    #   "offset_pct": {"x": float, "y": float}  # 0–100, optional
    # }
  "duration":         int,    # milliseconds (long_press, swipe, drag)
  "scale":            float,  # pinch scale
  "rotation":         float,  # degrees (converted to radians in codegen)
  "text":             str,    # type_text
  "bundle_id":        str,    # launch_app
  "app_name":         str,    # launch_app display name (optional)
  "expected_text":    str,    # verify_get_text
  "screenshot_name":  str,    # verify_screenshot_*
  "phase":            str,    # verify_screenshot_diff: "before" | "after"
  "direction":        str,    # swipe direction hint
  "fingers":          int,    # multi_finger_tap
  "scroll_container": dict,   # scroll: element to scroll within (captured from starting coordinate)
  "scroll_target":    dict,   # scroll: target element to scroll until visible
  "swipe_target":     dict,   # swipe: target element if swiping until element
}
```

---

## Code Style Rules for Generated Output

- **Indentation**: always 4 spaces (function body level = 4, inside `with step` = 8)
- **String quoting**: single quotes inside generated code; use `_q()` to escape content
- **No trailing newlines** inside `with step(...)` blocks — one call per block
- **Label format**:
  - `[Action] ...` for all gesture actions (tap, swipe, drag, pinch, etc.)
  - `[Verify] ...` for all assertion actions (verify_visible, verify_text, screenshot)
- **Fallback `# comment`** when no element matched — code must always be valid Python
- **Duration**: long_press and drag convert ms → seconds: `round(ms / 1000, 2)`
- **Rotation**: degrees → radians: `round(deg * math.pi / 180, 4)`
- **Percent offsets**: pass as floats (e.g. `49.5`, not `0.495`)

---

## Never Do

- Never raise exceptions or return `None` from `_action_call()` — always return a tuple
- Never hardcode `AppiumBy.ACCESSIBILITY_ID` as a string; use `_by()` to look it up
- Never skip the `with step(...)` wrapper — ReportPortal requires it
- Never modify the import block in `generate_header()` without updating `conftest.py` fixtures
