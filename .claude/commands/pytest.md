# pytest — Test Framework Rules

You are working on the **pytest + Appium test framework** (`pytest/` directory).

Read these files before making changes:
- [pytest/conftest.py](../../../pytest/conftest.py)
- [pytest/driver/driver_actions.py](../../../pytest/driver/driver_actions.py)
- [pytest/config.py](../../../pytest/config.py)

---

## Test File Rules

Every test file must follow this exact structure:

```python
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("<Human Readable Case Name>")
def test_<safe_name>(actions: DriverActions):
    with step("[Action] <description>"):
        actions.<method>(...)
    with step("[Verify] <description>"):
        actions.<assert_method>(...)
```

### Mandatory Rules
- File path: always `pytest/tests/test_*.py`
- `@pytest.mark.name("...")` is required on every test function
- The only fixture parameter is `actions: DriverActions` (never add `driver` directly)
- Every logical step wrapped in `with step("..."):` for ReportPortal
- Step label prefix: `[Action]` for interactions, `[Verify]` for assertions

---

## Fixture Reference (`conftest.py`)

| Fixture | Scope | Notes |
|---------|-------|-------|
| `driver` | session | One Appium session for the entire test suite — never re-create |
| `actions` | function | New `DriverActions` wrapper per test; shares session `driver` |
| `screenshot_on_failure` | function (autouse) | Auto-attached to every test — do NOT add as parameter |
| `reset_app` | function (optional) | Terminates + relaunches app; use only when test needs clean state |

---

## DriverActions Method Reference

### Element Lookup
- `find_element(by, value, timeout=30)` — wait for element present, return it
- `find_elements(by, value, timeout=30)` — return all matching elements
- `wait_for_visible(by, value, timeout=30)` — alias of find_element
- `wait_for_invisible(by, value, timeout=30)` — wait until element disappears
- `is_element_present(by, value, timeout=3)` — non-throwing boolean check

### Tap Variants
- `tap(element)` — tap a WebElement
- `tap_by_locator(by, value)` — find + tap
- `tap_by_coordinates(x, y)` — tap at absolute screen points
- `tap_within_element(by, value, pct_x, pct_y)` — tap at % offset within element
- `double_tap(element)` / `double_tap_within_element(by, value, pct_x, pct_y)`
- `triple_tap(element)` / `triple_tap_within_element(by, value, pct_x, pct_y)`
- `long_press(element, duration=1.0)` / `long_press_within_element(by, value, pct_x, pct_y, duration=1.0)`
- `two_finger_tap(element)`
- `multi_finger_tap(element, fingers=3)`

### Scroll / Swipe / Drag
- `scroll(direction="down", distance=0.5)` — slow content scroll
- `swipe(x1, y1, x2, y2, duration=800)` — swipe from point to point (ms)
- `swipe_screen(direction="up", distance=0.7, velocity=2500.0)` — fast full-screen fling
- `scroll_to_element(by, value, direction="down", max_scrolls=8)` — scroll until visible
- `scroll_until(scroll_by, scroll_value, target_by, target_value, direction="down")` — scroll within container element until target visible, then tap
- `swipe_until(by, value, direction="up")` — swipe until element visible then tap
- `drag_element(source, target, duration=1.0)` — press-hold drag element to target
- `drag_coordinates(from_x, from_y, to_x, to_y, duration=1.0)` — drag by coordinates

### Text Input
- `type_text(element, text, clear_first=True)`
- `type_text_by_locator(by, value, text, clear_first=True)`

### Gestures
- `pinch(element, scale=0.5, velocity=-1.0)` — scale < 1 = zoom out, > 1 = zoom in
- `rotate(element, rotation=π, velocity=1.5)` — rotation in radians

### System
- `press_home()` — press Home button
- `launch_app(bundle_id)` — launch or foreground an app
- `hide_keyboard()` — dismiss keyboard
- `background_app(seconds=3)` — background then restore
- `get_screen_size()` — returns `(width, height)` in points
- `take_screenshot(path)` — save PNG

### Assertions
- `verify_visible(by, value, timeout=30, msg="")` — assert element visible; returns element
- `verify_not_visible(by, value, timeout=3, msg="")` — assert element absent
- `verify_text(by, value, expected, timeout=30)` — assert element text equals expected
- `screenshot_gt(name, folder="screenshots/ground_truth")` — save ground truth PNG
- `screenshot_diff(name, threshold=0.01)` — compare current screen vs ground truth

---

## Adding a New Gesture to DriverActions

1. Add method to `DriverActions` class
2. Decorate with `@step("Description text")` (required for ReportPortal)
3. Add `@wait_for_stable_hierarchy` if the gesture changes the UI state
4. Use `mobile:*` XCUITest script APIs for native iOS gestures (not raw W3C Actions)
5. Log with `logger.debug(...)` 
6. Add the matching `action` type in `app/codegen.py → _action_call()`

```python
@step("My new gesture")
@wait_for_stable_hierarchy
def my_gesture(self, element: WebElement, param: float = 1.0) -> None:
    self.driver.execute_script("mobile: myGesture", {"element": element.id, "param": param})
    logger.debug("my_gesture: param=%.2f", param)
```

---

## Stability Check

`DriverActions.stability_check = False` by default (off).

Set to `True` only when tests are flaky due to async UI animations:
```python
actions.stability_check = True
actions.stability_interval = 0.4  # seconds between polls
actions.stability_timeout = 10.0  # give up after this long
```

This polls `page_source` after each decorated action — expensive (~0.5–2s per call). Only enable when needed.

---

## pytest.ini Markers

Defined in `pytest/pytest.ini`. Always use `@pytest.mark.name(...)` — it is the primary test identifier in ReportPortal.

---

## Never Do

- Never call `driver` directly inside test files — all interactions go through `actions`
- Never use `scope="function"` for the `driver` fixture — it must stay `"session"`
- Never add `screenshot_on_failure` as a test parameter — it's `autouse=True`
- Never use raw `W3C Actions` for iOS gestures — use XCUITest `mobile:*` scripts instead
- Never `assert` inside test files without a `with step(...)` context — assertions need RP context
