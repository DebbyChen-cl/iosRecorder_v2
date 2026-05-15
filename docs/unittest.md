# Unit Test Reference

**106 tests · 7 blocks · runs in ~0.34 s · no device or server required**  
**`--unit_test` mode** captures real device input/output pairs as fixture files → see [Unit Test Capture Mode](#unit-test-capture-mode---unit_test) below.

Run all unit tests:
```bash
python3 -m pytest -m unit -v
```

Run one block:
```bash
python3 -m pytest test_unittest/test_block1_wda_hierarchy.py -v
```

---

## Fixture XML Hierarchy

All tests that need element data share a single fixture defined in `test_unittest/conftest.py`.
It covers every selector quality level:

```
AppiumAUT
└── XCUIElementTypeApplication  (0,0 → 390×844)
    └── XCUIElementTypeWindow
        └── XCUIElementTypeOther
            ├── XCUIElementTypeButton  name="SaveButton" label="Save"        (100,200 → 80×44)
            ├── XCUIElementTypeButton  name="Effects"    label="Effects"      (200,200 → 80×44)
            ├── XCUIElementTypeTextField name="SearchField" label="Search here" (50,300 → 280×36)
            └── XCUIElementTypeScrollView name="MainScroll"                   (0,350 → 390×494)
                ├── XCUIElementTypeButton  name="Item1"  label="Item 1"       (10,360 → 370×60)
                ├── XCUIElementTypeButton  label="Label Only"  (no name)      (10,430 → 370×60)
                ├── XCUIElementTypeOther   (no name, no label)                (10,500 → 100×60)
                └── XCUIElementTypeCell    name="Cell-3" label="Cell 3"       (10,570 → 370×60)
```

**Coordinate → expected element:**

| (x, y) | Element | Quality |
|--------|---------|---------|
| (140, 222) | SaveButton | `id` |
| (240, 222) | Effects | `id_eq_label` |
| (190, 318) | SearchField | `id` |
| (195, 390) | Item1 | `id` |
| (195, 460) | Label Only button | `label_only` |
| (50, 530) | XCUIElementTypeOther | `xpath_only` |
| (195, 600) | Cell-3 | `id_indexed` |
| (500, 500) | — | None (outside bounds) |

---

## Block 1 — WDA Hierarchy Request

**File:** [test_block1_wda_hierarchy.py](../test_unittest/test_block1_wda_hierarchy.py)
**Covers:** `app/wda.py` → `_parse_xml()`, `WDAClient.get_source()`
**Needs device:** No — HTTP mocked with `unittest.mock.AsyncMock`

### What is tested

`_parse_xml()` strips DOCTYPE and returns a valid `ET.Element` tree.
`get_source()` fetches XML via a mocked httpx session, parses it, and handles error responses gracefully.

### Tests

| Test | Input | Expected output |
|------|-------|-----------------|
| `test_parse_xml_returns_element` | FIXTURE_XML string | `ET.Element` with tag `AppiumAUT` |
| `test_parse_xml_strips_doctype` | XML prepended with `<!DOCTYPE …>` | Same `ET.Element` — DOCTYPE removed |
| `test_parse_xml_finds_children` | FIXTURE_XML | `.//XCUIElementTypeApplication` found, name=`PhotoDirector` |
| `test_get_source_returns_element` | Mock HTTP 200 with FIXTURE_XML | `ET.Element` (not None) |
| `test_get_source_returns_none_on_404` | Mock HTTP 404 | `None` |
| `test_get_source_returns_none_on_500` | Mock HTTP 500 | `None` |
| `test_get_source_returns_none_without_session` | No session, `_adopt_session` returns False | `None` |
| `test_get_source_element_has_buttons` | Mock HTTP 200 with FIXTURE_XML | At least 4 buttons found, `SaveButton` and `Item1` present |

---

## Block 2 — Record Function (hittest + scroll container)

**File:** [test_block2_hittest.py](../test_unittest/test_block2_hittest.py)
**Covers:** `app/hittest.py` → `hit_test()`, `hit_test_for_swipe()`, `hit_test_excluding()`, `find_scroll_container()`
**Needs device:** No — uses fixture XML

### What is tested

Given a fixed element tree and a tap coordinate, the correct element is selected according to the scoring rules (`_score`). Scroll container detection finds the innermost scrollable ancestor.

### Tests

| Test | Input (x, y) | Expected output |
|------|-------------|-----------------|
| `test_hit_test_finds_save_button` | (140, 222) | element `name="SaveButton"` |
| `test_hit_test_finds_effects_button` | (240, 222) | element `name="Effects"` |
| `test_hit_test_finds_textfield` | (190, 318) | `XCUIElementTypeTextField`, `name="SearchField"` |
| `test_hit_test_finds_list_item` | (195, 390) | element `name="Item1"` |
| `test_hit_test_finds_label_only_button` | (195, 460) | element `label="Label Only"`, no name |
| `test_hit_test_finds_no_id_element` | (50, 530) | `XCUIElementTypeOther` |
| `test_hit_test_returns_none_outside_bounds` | (500, 500) | `None` |
| `test_hit_test_result_is_consistent` | (140, 222) called twice | Same object both times |
| `test_swipe_target_not_application` | (195, 390) via `hit_test_for_swipe` | Not Application, not Window |
| `test_swipe_on_button_returns_button` | (140, 222) via `hit_test_for_swipe` | `XCUIElementTypeButton` |
| `test_scroll_container_found_inside_scroll` | (195, 390) via `find_scroll_container` | `XCUIElementTypeScrollView`, `name="MainScroll"` |
| `test_scroll_container_none_outside_scroll` | (140, 222) via `find_scroll_container` | `None` |
| `test_scroll_container_none_outside_bounds` | (500, 500) via `find_scroll_container` | `None` |
| `test_hit_test_excluding_skips_element` | (140, 222), exclude SaveButton | Result is not SaveButton |

---

## Block 3 — UI Communication (Frontend → Backend)

**File:** [test_block3_ui_comms.py](../test_unittest/test_block3_ui_comms.py)
**Covers:** `app/main.py` record endpoints
**Needs device:** No — uses `unit_client` fixture (FastAPI TestClient + mocked WDA)

### What is tested

Coordinates and action metadata sent to REST record endpoints are stored exactly as received in `_steps`. Uses the `unit_client` fixture which pre-populates `_cache["root"]` with the fixture hierarchy so `hit_test` resolves elements without a real device.

### Tests

| Test | HTTP call | Expected step |
|------|-----------|---------------|
| `test_tap_coords_passthrough` | `POST /api/record {x:140, y:222}` | `action="tap"`, `coords.x=140`, `coords.y=222` |
| `test_tap_target_present` | same | `target.type` is one of `accessibility id / name / xpath / coordinate` |
| `test_tap_resolves_known_element` | same | `target.value="SaveButton"` |
| `test_double_tap_recorded` | `POST /api/record/double_tap {x:240, y:222}` | `action="double_tap"`, `coords.x=240` |
| `test_long_press_recorded_with_duration` | `POST /api/record/long_press {duration:1500}` | `action="long_press"`, `duration=1500` |
| `test_home_recorded` | `POST /api/record/home` | `action="home"` |
| `test_launch_app_recorded` | `POST /api/record/launch_app {bundle_id:…}` | `action="launch_app"`, `bundle_id` matches |
| `test_terminate_app_recorded` | `POST /api/record/terminate_app {bundle_id:…}` | `action="terminate_app"`, `bundle_id` matches |
| `test_verify_visible_recorded` | `POST /api/record/verify_visible {not_visible:false}` | `action="verify_visible"` |
| `test_verify_not_visible_recorded` | `POST /api/record/verify_visible {not_visible:true}` | `action="verify_not_visible"` |
| `test_multi_step_order_preserved` | tap + home + launch_app | 3 steps in same order |
| `test_steps_start_empty` | `GET /api/steps` (no prior action) | `steps == []` |

---

## Block 4 — Codegen

**File:** [test_block4_codegen.py](../test_unittest/test_block4_codegen.py)
**Covers:** `app/codegen.py` → `generate_header()`, `generate_script()`, `_merge_scroll_tap()`
**Needs device:** No — pure function, fixed step dicts in

### What is tested

Given a list of step dicts, `generate_script()` produces the correct pytest code string. Each action type maps to the right `DriverActions` method call. Special cases: coordinate fallback, offset_pct, scroll direction, screenshot comparison footer, unknown action comment.

### Tests

**`generate_header()`**

| Test | Input | Expected output |
|------|-------|-----------------|
| `test_header_contains_test_function` | `"MyTest"` | `def test_MyTest(actions: DriverActions):` |
| `test_header_contains_mark` | `"MyTest"` | `@pytest.mark.name("MyTest")` |
| `test_header_imports` | any name | `AppiumBy` and `step` imports present |
| `test_header_empty_name_falls_back` | `""` | `def test_recorded_test` |
| `test_header_special_chars_sanitized` | `"My Test-Case!"` | `def test_My_Test_Case_` |

**`generate_script()`**

| Test | Input step | Expected code fragment |
|------|-----------|------------------------|
| `test_tap_by_locator_generated` | tap + `accessibility id / SaveButton` | `actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SaveButton')` |
| `test_tap_step_label` | same | `[Action] Tap SaveButton` in `with step(…)` |
| `test_tap_coordinate_fallback` | tap + `coordinate` target | `actions.tap_by_coordinates(140, 222)` |
| `test_tap_with_offset_pct` | tap + `offset_pct {x:25, y:50}` | `actions.tap_within_element(…, 25.0, 50.0)` |
| `test_verify_visible_generated` | `verify_visible` | `actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'SaveButton')` |
| `test_verify_get_text_generated` | `verify_get_text`, `expected_text="Hello"` | `actions.verify_text(…, 'Hello')` |
| `test_home_generated` | `home` | `actions.press_home()` |
| `test_launch_app_generated` | `launch_app`, `bundle_id="com.example.app"` | `actions.launch_app('com.example.app')` |
| `test_swipe_direction_label` | swipe x1=300→x2=100, same y | `[Action] Swipe left` |
| `test_scroll_without_target_uses_direction` | scroll y1=600→y2=200 (finger up) | `actions.scroll(direction='down')` |
| `test_output_has_with_step_blocks` | any step | `with step(` present |
| `test_output_ends_with_assert_true` | any step | last line is `assert True` |
| `test_unknown_action_produces_comment` | `action="unknown_action"` | `# [unknown action: unknown_action]` |
| `test_screenshot_comparison_appended` | `verify_screenshot_gt` step | `actions.run_screenshot_comparisons(threshold=0.95)` appended |

**`_merge_scroll_tap()`**

| Test | Input | Expected output |
|------|-------|-----------------|
| `test_merge_scroll_tap_basic` | scroll + tap (with element target) | scroll's `scroll_target.value == "Item1"` |
| `test_merge_scroll_tap_no_merge_without_following_tap` | scroll only | Unchanged, no `scroll_target` key |

---

## Block 5 — Selector (standalone)

**File:** [test_block5_selector.py](../test_unittest/test_block5_selector.py)
**Covers:** `app/selector.py` → `build_selector()`, `get_selector_quality()`, `build_xpath()`
**Needs device:** No — pure function, `ET.Element` inputs created inline

### What is tested

Selector priority rules (accessibility id > label > xpath fallback), quality classification for all 5 levels, XPath building with various attribute combinations, and skipping of memory-pointer (`0x…`) and path (`/…`) names.

### Tests

**`build_selector()`**

| Test | Element attributes | Expected `(type, value)` |
|------|-------------------|--------------------------|
| `test_selector_prefers_accessibility_id` | `name="SaveButton" label="Save"` | `("accessibility id", "SaveButton")` |
| `test_selector_falls_back_to_label` | `label="Save"` (no name) | `("name", "Save")` |
| `test_selector_xpath_when_no_id_or_label` | — | `("xpath", "//XCUIElementTypeButton")` |
| `test_selector_skips_hex_pointer_name` | `name="0x1a2b3c4d" label="Save"` | `("name", "Save")` |
| `test_selector_skips_path_name` | `name="/private/var/…" label="Save"` | `("name", "Save")` |
| `test_selector_strips_whitespace` | `name="  SaveButton  "` | `("accessibility id", "SaveButton")` |

**`get_selector_quality()`**

| Test | Element attributes | Expected quality |
|------|-------------------|-----------------|
| `test_quality_id_when_name_differs_from_label` | `name="SaveButton" label="Save"` | `"id"` |
| `test_quality_id_eq_label_when_equal` | `name="Effects" label="Effects"` | `"id_eq_label"` |
| `test_quality_id_indexed_when_name_ends_with_number` | `name="Cell-3"` | `"id_indexed"` |
| `test_quality_label_only_when_no_name` | `label="Label Only"` | `"label_only"` |
| `test_quality_xpath_only_when_nothing` | — | `"xpath_only"` |
| `test_quality_xpath_only_for_hex_name` | `name="0xdeadbeef"` | `"xpath_only"` |

**`build_xpath()`**

| Test | Element attributes | Expected XPath |
|------|-------------------|----------------|
| `test_xpath_with_name` | `name="SaveButton"` | `//XCUIElementTypeButton[@name='SaveButton']` |
| `test_xpath_with_label_only` | `label="Save"` | `//XCUIElementTypeButton[@label='Save']` |
| `test_xpath_bare_tag_fallback` | — | `//XCUIElementTypeButton` |
| `test_xpath_skips_hex_name` | `name="0x1234" label="Save"` | `@label='Save'` used |

**Fixture-based quality check** (uses `hit_test` + fixture XML to confirm end-to-end quality resolution)

| Test | Coordinate | Expected quality |
|------|-----------|-----------------|
| `test_fixture_save_button_quality_is_id` | (140, 222) | `"id"` |
| `test_fixture_effects_quality_is_id_eq_label` | (240, 222) | `"id_eq_label"` |
| `test_fixture_label_only_quality` | (195, 460) | `"label_only"` |
| `test_fixture_xpath_only_quality` | (50, 530) | `"xpath_only"` |
| `test_fixture_cell3_quality_is_id_indexed` | (195, 600) | `"id_indexed"` |

---

## Block 6 — Export

**File:** [test_block6_export.py](../test_unittest/test_block6_export.py)
**Covers:** `app/codegen.py` → `generate_script()`; `app/main.py` → `_generate_html_report()`, `POST /api/export`
**Needs device:** No — pure functions + TestClient with mocked WDA

### What is tested

Given a fixed step list, the export pipeline produces a valid pytest `.py` file, a valid JSON steps file, and a valid HTML selector-quality report. The HTML report correctly shows warning cards for fragile selectors and an OK message for clean steps.

**Shared inputs:**
- `STEPS_CLEAN` — 2 steps, both `id` quality (no warnings expected)
- `STEPS_WITH_WARNINGS` — 2 steps: one `xpath_only`, one `coordinate` (both should appear as warning cards)

### Tests

| Test | Input | Expected output |
|------|-------|-----------------|
| `test_export_script_has_test_function` | `STEPS_CLEAN`, `case="ExportTest_20260101_120000"` | `def test_ExportTest_20260101_120000` in code |
| `test_export_script_has_all_actions` | `STEPS_CLEAN` | `tap_by_locator` and `verify_visible` both present |
| `test_export_script_ends_with_assert_true` | `STEPS_CLEAN` | Last line is `assert True` |
| `test_export_script_step_count_matches` | `STEPS_CLEAN` (2 steps) | Exactly 2 `with step(` blocks |
| `test_html_report_is_valid_html` | `STEPS_CLEAN` | Starts with `<!DOCTYPE html>`, ends with `</html>` |
| `test_html_report_contains_case_name` | `case="MyCase"` | `"MyCase"` in HTML |
| `test_html_report_all_stable_shows_ok` | `STEPS_CLEAN` | `"All steps use stable selectors"` |
| `test_html_report_shows_warnings_for_bad_selectors` | `STEPS_WITH_WARNINGS` | `"Steps with Selector Warnings"` |
| `test_html_report_warning_count` | `STEPS_WITH_WARNINGS` (2 steps) | `"2 of 2 steps have selector warnings"` |
| `test_html_report_shows_xpath_badge` | `STEPS_WITH_WARNINGS` | `"XPath Only"` badge |
| `test_html_report_shows_coordinate_badge` | `STEPS_WITH_WARNINGS` | `"Coord Only"` badge |
| `test_export_writes_py_file` | `STEPS_CLEAN`, tmp_path | `.py` file exists, contains `def test_FileTest` |
| `test_export_writes_json_file` | `STEPS_CLEAN`, tmp_path | `.json` parses correctly, `steps` count matches |
| `test_export_writes_html_file` | `STEPS_CLEAN`, tmp_path | `.html` file contains `<!DOCTYPE html>` and case name |
| `test_export_endpoint_returns_script_and_paths` | `POST /api/export {case_name:"EndpointTest"}` | `saved_paths` has 4 entries, `script` contains `def test_EndpointTest` |

---

## Block 7 — WDA Gesture Payload

**File:** [test_block7_wda_gestures.py](../test_unittest/test_block7_wda_gestures.py)
**Covers:** `app/wda.py` → `WDAClient.tap()`, `swipe()`, `long_press()`, `double_tap()`, `scroll()`, `two_finger_tap()`
**Needs device:** No — `httpx.AsyncClient` replaced with an `AsyncMock` that captures POST bodies

### What is tested

Each gesture method assembles the correct W3C Actions JSON payload and sends it to `POST /session/{id}/actions`. The captured payload is inspected for pointer type, coordinates (cast to `int`), duration values, and finger count.

### Helper

`_make_mock_http()` returns `(mock_http, captured)`. Every `POST` appends `{"url": …, "json": …}` to `captured`. The `WDAClient` is created **inside the coroutine** (required on Python 3.9 where `asyncio.Lock()` needs a running event loop).

### Tests

| Test | Gesture call | Assertion |
|------|-------------|-----------|
| `test_tap_sends_actions_endpoint` | `tap(100, 200)` | URL contains `/session/{id}/actions` |
| `test_tap_returns_true_on_success` | `tap(100, 200)` | Returns `True` |
| `test_tap_payload_coordinates` | `tap(100, 200)` | `pointerMove` has `x=100, y=200` |
| `test_tap_payload_has_pointer_down_up` | `tap(100, 200)` | `pointerDown` and `pointerUp` present |
| `test_tap_uses_touch_pointer_type` | `tap(100, 200)` | `parameters.pointerType == "touch"` |
| `test_tap_coordinates_are_int` | `tap(123.7, 456.9)` | `x` and `y` are `int` (not float) |
| `test_swipe_start_and_end_coordinates` | `swipe(300, 400, 100, 400)` | First move `(300, 400)`, second move `(100, 400)` |
| `test_swipe_move_has_duration` | `swipe(…, duration_ms=800)` | Moving `pointerMove` has `duration=800` |
| `test_long_press_pause_duration` | `long_press(100, 200, duration_ms=1500)` | `pause.duration == 1500` |
| `test_long_press_coordinates` | `long_press(150, 300, …)` | `pointerMove` has `x=150, y=300` |
| `test_double_tap_has_two_down_up_pairs` | `double_tap(100, 200)` | 2× `pointerDown`, 2× `pointerUp` |
| `test_scroll_has_initial_pause` | `scroll(200, 600, 200, 200)` | First `pause.duration == 100` |
| `test_two_finger_tap_has_two_fingers` | `two_finger_tap(200, 400)` | Payload has `finger1` and `finger2` entries |
| `test_two_finger_tap_fingers_spread_apart` | `two_finger_tap(200, 400, spread=30)` | `finger1.x != finger2.x` |
| `test_tap_returns_false_without_client` | `tap(100, 200)` with `_client=None` | Returns `False` |

---

## Unit Test Capture Mode (`--unit_test`)

Run the recorder server with the `--unit_test` flag to capture real input/output pairs from actual device interactions and save them as fixture files:

```bash
bash start.sh --unit_test
```

The server prints `[Unit Test Capture Mode] Fixture captures will be saved to test_unittest/fixtures/` at startup and behaves identically to normal mode — the only difference is that every `_record_*` call appends to an in-memory list.

### How it works

Every time a step is recorded (any gesture, verify, scroll, etc.), `_unit_test_capture()` in `app/main.py` appends an entry:

```json
{
  "input":         { "action": "tap", "x": 140.0, "y": 222.0 },
  "output":        { "action": "tap", "coords": {"x": 140, "y": 222}, "target": { ... } },
  "hierarchy_xml": "<AppiumAUT>...</AppiumAUT>"
}
```

`pre_screenshot` and `pre_screenshot_size` are stripped from `output` (same rule as the export JSON).

### API endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/unit_test/status` | `GET` | `{"enabled": true/false, "entry_count": N}` |
| `/api/unit_test/save` | `POST` | Saves captured entries to `test_unittest/fixtures/` |
| `/api/unit_test/entries` | `DELETE` | Clears in-memory entries without touching `_steps` |

`DELETE /api/steps` also clears entries automatically.

### Saving a capture

`POST /api/unit_test/save` with `{"case_name": "my_capture"}` writes two files:

**`test_unittest/fixtures/capture_<name>_<ts>.json`**
```json
{
  "captured_at": "2026-01-01T12:00:00",
  "case_name": "my_capture",
  "entries": [ ... ],
  "steps": [ ... ],
  "codegen_output": "import pytest\n..."
}
```

**`test_unittest/fixtures/hierarchy_<name>_<ts>.xml`**  
The raw WDA page source XML from the first entry that has one — paste this directly into `conftest.py` as `FIXTURE_XML` to create a frozen fixture for a new test block.

### Workflow

1. `bash start.sh --unit_test`
2. Record a test scenario in the UI
3. `curl -X POST http://localhost:8888/api/unit_test/save -H 'Content-Type: application/json' -d '{"case_name":"my_scenario"}'`
4. Open the saved `.json` — `entries[N].input` is the exact dict you pass to a record helper in a new unit test; `entries[N].output` is what you assert against
5. Copy the saved `.xml` into `conftest.py` (or load it from file) as a frozen hierarchy fixture

---

## Markers & conftest

**Pytest markers** (registered in `pytest.ini`):

| Marker | Meaning |
|--------|---------|
| `unit` | No device or server needed — set via `pytestmark = pytest.mark.unit` in every block file |
| `integration` | Requires live recorder server + WDA device |

**`test_unittest/conftest.py` fixtures:**

| Fixture | Scope | Description |
|---------|-------|-------------|
| `FIXTURE_XML` | module constant | XML string of the shared element hierarchy |
| `fixture_xml` | session | Same string as a pytest fixture |
| `fixture_root` | session | Parsed `ET.Element` from `fixture_xml` |
| `unit_client` | function | FastAPI `TestClient` with WDA + background tasks mocked; `_cache["root"]` pre-populated |
| `client` | session | `httpx.Client` pointed at `localhost:8888` (integration only) |
| `clear_steps` | autouse | No-op for `unit` tests; `DELETE /api/steps` for integration tests |
| `warm_tree` | function | `GET /api/tree` to warm `_cache["root"]` (integration only) |
