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
        assert actions.verify_visible(...)
```

### Mandatory Rules
- File path: always `pytest/tests/test_*.py`
- `@pytest.mark.name("...")` is required on every test function
- The only fixture parameter is `actions: DriverActions` (never add `driver` directly)
- Every logical step wrapped in `with step("..."):` for ReportPortal
- Step label prefix: `[Action]` for interactions, `[Verify]` for assertions
- Every `[Verify]` and `[Action/Verify]` step must contain an explicit `assert`.
  A plain `assert actions.<method>(...)` is valid for every public method — see the
  return-value contract below. Do not rely only on a helper's internal `AssertionError`.
  (The older `... is not False` form still works and does not need to be rewritten.)

---

## Return-Value Contract

**Every public `DriverActions` method returns a truthy value on success and raises on
failure.** Return something meaningful where one exists — the `WebElement`, the saved
path, a real bool — and fall back to `True` only when the method genuinely has nothing
to hand back.

This exists because generated tests wrap nearly every call in
`assert actions.<method>(...)`. A method that falls through and returns `None` produces
`AssertionError: assert None` even when the gesture succeeded on the device.

A method may return `None` only by opting out explicitly: add it to
`OPTIONAL_RETURN_METHODS` in
[test_unittest/test_driver_actions_contract.py](../../test_unittest/test_driver_actions_contract.py)
with the reason. The only current member is `get_element()`, whose non-throwing lookup
must stay falsy so `if actions.get_element(...)` works.

`test_driver_actions_contract.py` enforces this by AST-parsing `driver_actions.py` —
no device or Appium needed. It fails the build when a public method can return `None`,
or is annotated `-> None`. Run it after touching `DriverActions`:

```bash
python3 -m pytest test_unittest/test_driver_actions_contract.py -o addopts=""
```

---

## Fixture Reference (`conftest.py`)

| Fixture | Scope | Notes |
|---------|-------|-------|
| `driver` | function | Fresh Appium/WDA session per test — quits and recreates the driver before every test function. First test of the session also runs onboarding (C-1..C-5), popup close loop (D-1→D-2→D-3), and ATT/push Allow prompts; subsequent tests restart the app (terminate → crash dialog → activate → close popups). Teardown terminates app + quits driver. |
| `actions` | function | New `DriverActions` wrapper per test; uses the per-test `driver` |
| `screenshot_on_failure` | function (autouse) | Auto-attached to every test — do NOT add as parameter |
| `_failure_evidence_workspace` | function (autouse) | Auto-healing: allocates one evidence folder per test; deleted again when the test passes — do NOT add as parameter |
| `_log_auto_healing_context` | function (autouse) | Auto-healing: logs `AUTO_HEALING_CONTEXT` onto the RP item during agent replay runs — do NOT add as parameter |

---

## Auto-Healing (`auto_healing.py`)

Ported from `rdqe-ios-autotest-phdm/SFT/conftest.py`. `conftest.py` only holds thin
hook wrappers (`pytest_configure`, `pytest_collection_modifyitems`,
`pytest_runtest_protocol`, `pytest_runtest_makereport`, `pytest_sessionfinish`)
that delegate into `auto_healing.py`.

Phase 1 runs inside the pytest session:

| Piece | Behaviour |
|-------|-----------|
| Project root | Resolved in `configure()` from **pytest's own `config.rootpath`**, never hardcoded. Nodeids in `state.json`, evidence paths, and the `TEST_PROJECT` Phase 2 replays from must all share one base — a mismatch makes `replay.py` fail to find the test and every case ends as `infra_issue`. |
| Test registry | Every collected test gets a stable `IOSREC-AUTO-nnnn` id in `<healing project>/registry/test_registry_ios_recorder.json`. Ids are keyed by `case_key` (the test path relative to `pytest/` + test name), so they survive a change of rootdir — a plain nodeid would mint a new id per invocation directory. `@pytest.mark.case_id("...")` overrides the generated id. |
| Suite filter | `is_own_item()` restricts evidence, retries and registry entries to tests under `pytest/`. Launched from the repo root pytest also collects `test_unittest/`, which the agent cannot replay on a device. |
| Failure evidence | On any failed phase, saves `fail_moment.png`, `fail_moment_hierarchy.xml`, `stack_trace.txt` and `metadata.json` under `<rootdir>/Self-healing/evidence/<ts>-<test>/`. Passing tests have their folder removed at teardown. |
| `fail_step` | This suite has no runtime step tracker, so the failing step is inferred from the nearest `with step("...")` above the failing line **within the same test function**. |
| Heuristic lane (C2) | App not running / black screenshot → `app_crash`; network keywords in the stack → `network_issue`; both retry immediately while budget lasts. Everything else is deferred to Phase 2. |
| Immediate retry (C1) | Up to 3 cases per run (`AUTO_HEALING_MAX_RETRY_CASES`) are re-run once via `runtestprotocol`; the original evidence folder is preserved. |
| `state.json` | `<healing project>/runs/<run_id>/state.json` is the run ledger the agent reads. |
| Phase 2 trigger | If any case is deferred, `pytest_sessionfinish` opens a Terminal running the healing agent's `tools/orchestrator.py` and blocks up to 11 min, passing `TEST_PROJECT=<rootdir>`, `AUTO_HEALING_CREATE_BRANCH`, and the still-open ReportPortal launch id so replays report into the same launch. |

### Switches

Primary settings live in `pytest/config.py`:

| Setting | Default | Effect |
|---------|---------|--------|
| `AUTO_HEALING_ENABLED` | `True` | Master switch — `False` means no evidence, state, retry or Phase 2 |
| `AUTO_HEALING_CREATE_BRANCH` | `True` | Let Phase 2 commit + push its patches to `<branch>_YYMMDD_hhmmss`. The agent stages the **entire** working tree (`git add -A`) and leaves the repo on the new branch, so unrelated WIP gets committed too |

`config.py` also holds two device-tuning knobs, both read once at import and overridable
per `DriverActions` instance — one edit covers the whole suite instead of every generated
call site. See Slider Drags for the measurements behind them.

| Setting | Default | Effect |
|---------|---------|--------|
| `TEXT_NUMERIC_TOLERANCE` | `{"valueLabel": 3}` | element id → allowed numeric drift in `verify_text`; ids not listed stay exact string matches |
| `SLIDER_THUMB_SIZE` | `40.0` | thumb size (pt) used to place a press on a slider's thumb |

Environment variables of the same name override `config.py` per run
(`AUTO_HEALING=0`, `AUTO_HEALING_CREATE_BRANCH=0`). Env-only extras:
`AUTO_HEALING_PHASE2=0` (evidence + state only), `AUTO_HEALING_PROJECT_PATH`,
`AUTO_HEALING_REGISTRY_PATH`, `AUTO_HEALING_APP_VERSION`,
`AUTO_HEALING_PHASE2_TIMEOUT`, `AUTO_HEALING_MAX_RETRY_CASES`.
Set by the agent itself: `AUTO_HEALING_REPLAY=1`, `AUTO_HEALING_CONTEXT`,
`AUTO_HEALING_NOT_HEALED_REASON`, `AUTO_HEALING_RP_LAUNCH_ID`.

`AUTO_HEALING_CREATE_BRANCH` is consumed by
`iOS_auto_healing_agent/tools/orchestrator.py::_commit_and_push_healing_changes`,
which defaults to on when the variable is absent (phdm behaviour unchanged).

The `driver` fixture publishes its session via `auto_healing.set_active_driver()`
— any new driver fixture must do the same or failure evidence loses the screenshot
and hierarchy.

---

## DriverActions Method Reference

### Element Lookup
- `find_element(by, value, timeout=30)` — wait for element present, return it
- `find_elements(by, value, timeout=30)` — return all matching elements; raises when none are found
- `wait_for_visible(by, value, timeout=30)` — alias of find_element
- `wait_for_invisible(by, value, timeout=30)` — wait until element disappears
- `is_element_present(by, value, timeout=3)` — non-throwing boolean check

- `find_element(by, value, timeout=DEFAULT_WAIT, container_by=None, container_value=None, container_w=0, container_h=0)` — wait for element; when container params are provided the lookup runs **global → container-scoped → scroll**: (1) a global search returns the element immediately when it is already ≥ 50 % visible, so a stale container selector cannot break the step; (2) otherwise the container is resolved and searched internally; (3) if neither yields a ≥ 50 % visible element, `_find_with_scroll()` scrolls the container until it appears. Every one of those ≥ 50 % checks clips by the container rect as well as the screen — see Visibility Measurement. Trade-off of global-first: when the same id exists both inside and outside the container and both are on-screen, the global hit wins. All `*_by_locator`, `*_within_element`, `verify_visible`, and `swipe_on_element` forward these params here, so this order applies uniformly to every action.

### Tap Variants
- `tap(element)` — tap a WebElement
- `tap_by_locator(by, value, ..., container_by=None, container_value=None, container_w=0, container_h=0)` — find + tap; raises immediately when absent; auto-scrolls when container params given
- `tap_by_coordinates(x, y)` — tap at absolute screen points
- `tap_within_element(by, value, pct_x, pct_y, ..., container_by=None, container_value=None, container_w=0, container_h=0)` — tap at % offset within element; auto-scrolls when container params given
- `double_tap(element)` / `double_tap_within_element(by, value, pct_x, pct_y, ..., container_by=None, ...)`
- `triple_tap(element)` / `triple_tap_within_element(by, value, pct_x, pct_y, ..., container_by=None, ...)`
- `five_tap(element)` / `five_tap_within_element(by, value, pct_x, pct_y, ..., container_by=None, ...)` — tap 5 times
- `long_press(element, duration=1.0)` / `long_press_within_element(by, value, pct_x, pct_y, duration=1.0, ..., container_by=None, ...)`
- `long_press_capture_for_preview(press_by, press_value, duration, capture_name, capture_by, capture_value, expected_result="same", threshold=None, ..., container_by=None, ...)` — starts long press, captures preview AFTER during hold, then releases; `None` uses the global threshold from `run_screenshot_comparisons()`; returns `True` after success
- `long_press_capture_for_preview_within_element(press_by, press_value, pct_x, pct_y, duration, capture_name, capture_by, capture_value, expected_result="same", threshold=None, ..., container_by=None, ...)` — same as above but press point uses % offset inside element; `None` uses the global threshold from `run_screenshot_comparisons()`; returns `True` after success
- `two_finger_tap(element)`
- `multi_finger_tap(element, fingers=3)`

### Scroll / Swipe / Drag
- `scroll(direction="down", distance=0.5)` — slow content scroll
- `swipe_on_element(by, value, direction, velocity=500.0, from_pct_x=50.0, from_pct_y=50.0, distance_pts=None)` — swipe in a cardinal direction starting from a % offset within the element; `velocity` is px/s derived from recorded gesture speed (distance_px * 1000 / duration_ms); `distance_pts` is the exact swipe distance in logical points from the recording (falls back to 40 % of element dimension when omitted)
- `scroll_to_element(by, value, direction="down", max_scrolls=8)` — scroll until visible
- `scroll_until(scroll_by, scroll_value, target_by, target_value, direction="down", max_attempts=30, offset_start=None, offset_end=None, velocity=500)` — scroll within container until target is ≥ 50 % visible on screen, then **return** it. It does **not** tap: codegen emits `scroll_until(...)` followed by a separate tap step, so tapping here would fire twice. When the target is already visible enough it returns on attempt 0 without sending any gesture — "no scroll happened" is a normal outcome, not a fault. "Visible enough" = ≥ 50 % of the target inside **both the screen and the scroll container's own rect** (see Visibility Measurement), measured after the target's rect has settled, so neither a still-gliding scroll view nor a cell clipped by the container edge can be mistaken for "arrived". On giving up it raises `NoSuchElementException` reporting the best visibility it reached. `offset_start`/`offset_end` are `(x_pct, y_pct)` fractions of the container rect (generated by the recorder); `velocity` is pixels/second derived from the original gesture speed. Falls back to a 40 % center swipe when offsets are absent.
- `drag_element(source, target, duration=1.0)` — press-hold drag element to target
- `drag_coordinates(from_x, from_y, to_x, to_y, duration=1.0)` — drag by absolute coordinates
- `drag_within_elements(from_by, from_value, from_pct_x, from_pct_y, to_by, to_value, to_pct_x, to_pct_y, duration=1.0)` — drag from % offset within source element to % offset within target element (generated by recorder). When the source is an `XCUIElementTypeSlider` the press point is moved onto the thumb — see Slider Drags
- `set_slider_value(by, value, percent, timeout=30, tolerance=1.0, container_by=None, ...)` — set an `XCUIElementTypeSlider` to *percent* (0–100) through XCUITest `adjust(toNormalizedSliderPosition:)`, reading the value back and retrying up to 3× before raising. Exact where a coordinate drag is not; the outcome does not depend on the value the slider held beforehand
- `paint_in_element(by, value, points_pct, duration_ms=1000)` — replay free-form paint path on one element using sampled `(x_pct, y_pct, t_ms)` points; returns `False` when the recorded path is unusable (no points, or fewer than two distinct points) because no gesture reached the device

### Text Input
- `type_text(element, text, clear_first=True)`
- `type_text_by_locator(by, value, text, clear_first=True)`

### Gestures
- `pinch(element, scale=0.5, velocity=-1.0)` — scale < 1 = zoom out, > 1 = zoom in
- `rotate(element, rotation=90.0, velocity=1.5)` — rotation in **degrees** (positive = clockwise); converted to radians internally

### System
- `press_home()` — press Home button
- `launch_app(bundle_id)` — launch or foreground an app
- `activate_app(bundle_id)` — bring an app to the foreground without cold-launching it
- `terminate_app(bundle_id)` — force-quit an app
- `hide_keyboard()` — dismiss keyboard
- `background_app(seconds=3)` — background then restore
- `get_screen_size()` — returns `(width, height)` in points
- `take_screenshot(path)` — save PNG; returns `False` when no image was written

### Assertions
- `verify_visible(by, value, timeout=30, msg="")` — assert element visible; returns the `WebElement` so callers can chain, and raises `AssertionError` when absent
- `verify_not_visible(by, value, timeout=5, msg="")` — polls up to *timeout* s waiting for the element to disappear; returns `True` if absent, raises `AssertionError` if still present after timeout
- `wait_until_not_show(by, value, appear_timeout=5, disappear_timeout=1200, poll_interval=1.0, msg="")` — for a transient element (progress bar, rendering spinner, toast): waits for it to appear and then go away again. The two budgets are counted **separately** — `appear_timeout` (default 5 s) for it to show up, then a fresh `disappear_timeout` (default 1200 s = 20 min) for it to vanish. Returns `False` when it never appears (without spending the long budget) and `False` when it is still shown after the long budget; `True` as soon as it is gone. **Never raises** — both failures come back as `False`, so the generated `assert actions.wait_until_not_show(...)` is what fails the step. Unlike `verify_not_visible`, an element that was never there is a failure, not a pass.
- `verify_text(by, value, expected, timeout=30, tolerance=None)` — assert element text equals expected. `tolerance` switches to a **numeric** comparison accepting that many units of difference; `None` looks the element id up in `actions.text_numeric_tolerance` (seeded from `config.TEXT_NUMERIC_TOLERANCE`, currently `{"valueLabel": 3}`) and otherwise compares exactly. Non-numeric text is always compared exactly, whatever the tolerance — a tolerance can never turn a text assertion into a fuzzy one
- `capture_for_gt(name, by=None, value=None)` — capture element (or full screen) screenshot to `screenshots/compare/{name}_{ts}_compare.png`; queues `(name, path, threshold)` for GT comparison; timestamp prevents overwrite on repeated calls. Returns the saved **path** (truthy) on success — callers pass it straight to `compare_with_gt(compare_path=...)` / `compare_preview(before_path=...)`. Returns **`False`** when no image was written, and skips queueing, so a missing file fails at the capture rather than deep inside `run_screenshot_comparisons()`.
- `capture_for_preview(name, phase, by=None, value=None)` — capture element screenshot as `{name}_{ts}_{phase}.png` in compare folder. *phase* is `before` / `after`, optionally with a **pair suffix** (`before_min_ic_jaw` ↔ `after_min_ic_jaw`) so one `name` can hold several pairs at once — e.g. inside a loop over elements. The `(name, pair_suffix)` key is what pairs the halves in `_preview_pending`, and the suffix also lands in the filename so nothing overwrites. `before` saves the ts; `after` pops it to pair files and queues `(label, before_path, after_path, threshold, expected_result)` (`label` = `name:pair_suffix`, so failure messages name the exact pair). An `after` with no matching `before`, or a phase that is neither, **raises immediately at capture time** instead of queueing a made-up path that later surfaces as an opaque `file missing` failure in `run_screenshot_comparisons()`.
- `tap_then_capture_preview(capture_by, capture_value, tap_by, tap_value, wait_seconds=2.0, capture_name="tap_screenshot_diff", expected_result="same", threshold=None)` — one-shot flow: capture BEFORE, tap action element, wait N seconds, capture AFTER; `None` uses the global threshold from `run_screenshot_comparisons()`
- `tap_within_element_then_capture_preview(capture_by, capture_value, tap_by, tap_value, tap_pct_x, tap_pct_y, wait_seconds=2.0, capture_name="tap_screenshot_diff", expected_result="same", threshold=None)` — same flow but tap point uses percent offset inside action element; `None` uses the global threshold from `run_screenshot_comparisons()`
- `run_screenshot_comparisons()` — evaluate all queued GT and preview comparisons (AND logic); uploads failing pairs to ReportPortal with label showing both filenames (`diff: A vs B`); raises one `AssertionError` with all failure messages
- `compare_with_gt(name, compare_path, threshold)` — single GT comparison with explicit path; if GT missing → saves compare as GT; if diff > threshold → uploads diff to RP with `diff: compare vs gt` label; does not raise
- `compare_preview(name, before_path, after_path, threshold, expected_result)` — single before/after comparison with explicit paths; uploads diff to RP with `diff: before vs after` label on failure; does not raise

---

## Adding a New Gesture to DriverActions

1. Add method to `DriverActions` class
2. Decorate with `@step("Description text")` (required for ReportPortal)
3. Add `@wait_for_stable_hierarchy` if the gesture changes the UI state
4. Use `mobile:*` XCUITest script APIs for native iOS gestures (not raw W3C Actions)
5. Log with `logger.debug(...)`
6. **Return a truthy value on every success path** — see the Return-Value Contract above.
   `test_driver_actions_contract.py` fails the build otherwise.
7. Add the matching `action` type in `app/codegen.py → _action_call()`
8. All `mobile: dragFromToWithVelocity` calls must include `pressDuration` and `holdDuration` (required params)

```python
@step("My new gesture")
@wait_for_stable_hierarchy
def my_gesture(self, element: WebElement, param: float = 1.0) -> bool:
    self.driver.execute_script("mobile: myGesture", {"element": element.id, "param": param})
    logger.debug("my_gesture: param=%.2f", param)
    return True
```

---

## Stability Check

`DriverActions.stability_check = True` by default (on).

Stability currently uses a structural-identity signature (tree position + element type
+ child-count), and ignores content fields such as name/label/value.

Minimal safeguard is enabled: at least 1 consecutive matching signature is required
before release.

For continuously changing screens (for example, video playback), a fallback is enabled:
if structural identity keeps changing, release is allowed when element count remains
stable for a short period.

You can tune behavior per test when needed:
```python
actions.stability_check = True
actions.stability_interval = 0.4  # seconds between polls
actions.stability_timeout = 10.0  # give up after this long
actions.stability_required_samples = 1
actions.stability_count_fallback_enabled = True
actions.stability_count_fallback_after = 2.0
actions.stability_count_required_samples = 2
```

This polls `page_source` after each decorated action — expensive (~0.5–2s per call). Only enable when needed.

The helper methods `tap_then_capture_preview`, `tap_within_element_then_capture_preview`, `long_press_capture_for_preview`, and `long_press_capture_for_preview_within_element` are excluded from hierarchy-stability wrapping so capture timing remains deterministic during the gesture.

---

## Element Readiness (pre-action settle)

The hierarchy-stability check above runs **after** an action and compares structural
identity only, so a panel that is still sliding or fading in looks stable from its very
first frame — its tree is final while its frame keeps moving. Combined with
`find_element()` waiting on *presence* (not visibility), a `*_within_element` call could
read a coordinate mid-animation, fire `mobile: tap` at empty space, and still report
PASS, because WDA never hit-tests a coordinate tap. The failure then surfaced one step
later, on the next element that never appeared.

`DriverActions._settle_rects(elements)` closes that hole. Before any element is turned
into a coordinate it polls until, for `element_settle_required_samples` **consecutive**
rounds:

1. every `element.rect` is unchanged from the previous round, with non-zero width/height, **and**
2. every element reports `visible == "true"` (an unreadable/absent attribute counts as visible,
   so element types that do not publish it are never blocked)

One matching pair is deliberately *not* enough (hence the default of 2). `rect` is rounded
to whole points and iOS animations ease in and out, so at the head or tail of a slide-in the
frame can move less than a point between two samples — the element reads as parked while it
is about to accelerate, which is how a drag ends up starting from a coordinate the control
has already left.

It polls the elements themselves — a couple of cheap round-trips, not a `page_source` dump —
and **never raises on timeout**: it logs `[settle] '<name>' not settled within Ns … acting
anyway` and returns the last rects, so it can only make a flaky step less flaky, never turn
a passing step into a failure. `StaleElementReferenceException` still propagates so callers
that re-resolve (`tap_within_element`, `_drag_points`) keep working.

**A gesture with more than one element-derived point must settle them together.**
Settling the source and then the target freezes the start coordinate while the target is
still being polled, so a drag across a panel that is still laying out mixes points from two
different frames — both ends "settled", the drag still lands wrong. `_points_in_elements([(el, pct_x, pct_y), …])`
returns every point from the same quiet round; `_drag_points(from…, to…)` wraps it with the
two `find_element()` lookups and re-resolves once on a stale handle.

| Helper | Used by |
|--------|---------|
| `_coord_at_pct(el, …)` | all `*_within_element` taps / long-presses, `tap_by_locator()` |
| `_point_in_element(el, …)` | single-element point (`long_press_drag_from_element_to_coordinates`, …) |
| `_points_in_elements([…])` | `drag_element`, `long_press_drag_element` |
| `_drag_points(from…, to…)` | `drag_within_elements`, `long_press_drag_within_elements` |

```python
actions.element_settle_check = True         # False restores fire-immediately behaviour
actions.element_settle_interval = 0.15      # seconds between two rect samples
actions.element_settle_timeout = 3.0        # give up and act anyway after this long
actions.element_settle_required_samples = 2 # consecutive quiet rounds before releasing
```

Covered by `test_unittest/test_element_settle.py` (fake elements, no device needed).

---

## Slider Drags

A recorded drag on an `XCUIElementTypeSlider` carries **the thumb position at record
time**, and a UISlider ignores any touch that does not land on its thumb. Replay the
coordinate against a slider holding a different value and the press hits bare track:
the gesture does nothing at all, no error is raised, and the failure surfaces one step
later as a stale value. Measured on device — recorded press x=95 (thumb at 28 % when
recorded) against a slider sitting at 0 % left `valueLabel` at `0` instead of `50`.

`_slider_grab_point()` closes that: for a slider source it derives the thumb's current
position from the control's own `value` attribute (`"51%"`, a bare number, or a 0–1
float are all accepted) and presses there instead, logging

```
[slider] 'cpSlider' sits at 0%; pressing its thumb at (23, 668) instead of the recorded (95, 668)
```

The thumb is not published as an element, so its size comes from
`config.SLIDER_THUMB_SIZE` (capped at the control's own thickness). Vertical sliders
(height > width) are handled with 0 % at the bottom. Non-sliders pass through untouched.

**The press point has to be near the thumb's centre, not merely on the thumb.** These
sliders are *relative*: the value tracks the finger's displacement from wherever it
grabbed. Measured on device across six drags —

```
value_end = value_at_press + (end_x - press_x) / 2.70      # 310 pt control
```

— which pins the travel at 270 pt and therefore the thumb at **40 pt**, not iOS's own
31.5 pt. Pressing 4 pt left of centre with the old 32 pt estimate inflated every result
by ~1.5 units; correcting `SLIDER_THUMB_SIZE` to 40 moved the 14 slider verifies of
`test_00015_main_04_01_05` from a 3-unit worst case to 0 (×9), 1 (×3), 2 (×2).

**This makes the gesture land accurately, not exactly.** Slider readouts are therefore
verified with a numeric tolerance (`config.TEXT_NUMERIC_TOLERANCE`, 3 = measured max + 1),
not an exact string compare. When a step needs the exact value rather than a faithful
gesture, use `set_slider_value(by, value, percent)` — `adjust(toNormalizedSliderPosition:)`
hits it precisely (device-verified: `0.5` → `50`) and does not care what the slider held
before. Note `mobile: setValue` is **not implemented** by the installed Appium XCUITest
driver; `send_keys` is the working path.

---

## Visibility Measurement

`_visible_fraction(element, rect=None, clip=None)` decides every "is it ≥ 50 % visible"
question in the lookup chain.

The screen alone is the wrong boundary. A cell parked at the edge of a 430×84
`styleCollectionView` is clipped by the strip long before it leaves the screen, yet a
screen-only measurement calls it 100 % visible — so `scroll_until` stopped early and the
tap landed on the cut-off cell or its neighbour, while still reporting PASS.

Pass `clip` (the container's rect) and the fraction is measured against
**element ∩ container ∩ screen**. All four call sites now do:

| Call site | Clip source |
|-----------|-------------|
| `find_element()` stage 1 (global) | `_container_clip()` — a **no-wait** `find_elements` probe, so a stale container selector costs no timeout and just falls back to screen-only. Only run when the cheap screen-only measurement would have accepted, since clipping can only lower the fraction — an xpath container is not a free lookup |
| `find_element()` stage 2 (container-scoped) | the container it already resolved |
| `_find_with_scroll()` | the container it already resolved per attempt |
| `scroll_until()` | `_container_clip(scroll_by, scroll_value)` |

Two guards keep this from over-rejecting:
- an element **larger than the clip window** has its denominator capped at the window
  area, so filling the window counts as fully visible instead of being penalised
- a **degenerate clip** (zero/negative size) is ignored entirely

Without a `clip` the original screen-only formula is used unchanged, so any call site
that does not know a container behaves exactly as before.

**This is stricter than it used to be.** Cases that previously returned a clipped element
and silently tapped the wrong thing now keep scrolling, and can end in
`NoSuchElementException` after `max_attempts`. That is the intended trade: a loud failure
naming the best visibility reached, instead of a green step that tapped nothing.

---

### Missing Element Behavior

`DriverActions` propagates `TimeoutException` / `NoSuchElementException` when an
action cannot find its target. The pytest hook stops the suite after the current
test teardown when one of these locator failures reaches the test call.

## pytest.ini Markers

Defined in `pytest/pytest.ini`. Always use `@pytest.mark.name(...)` — it is the primary test identifier in ReportPortal.
`case_id(id)` pins a test's auto-healing case id; `auto_healing` is added automatically during agent replay runs.

---

## Never Do

- Never call `driver` directly inside test files — all interactions go through `actions`
- Never change `driver` fixture back to `scope="session"` — it must stay `"function"` for per-test WDA restart
- Never add `screenshot_on_failure` as a test parameter — it's `autouse=True`
- Never use raw `W3C Actions` for iOS gestures — use XCUITest `mobile:*` scripts instead
- Never `assert` inside test files without a `with step(...)` context — assertions need RP context
