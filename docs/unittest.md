# Unit Test Reference

**151 tests · 5 gen files · 7 fixtures · runs in ~4 s · no device or server required**  
**`--unit_test` mode** captures real device pairs and auto-generates 5 regression test files → see [Unit Test Capture Mode](#unit-test-capture-mode---unit_test) below.

Run all unit tests:
```bash
python3 -m pytest -m unit -v
```

Run a single gen file:
```bash
python3 -m pytest test_unittest/test_gen1_action_coords.py -v
```

---

## Generated Test Files

Five append-only files live in `test_unittest/`. Each covers a different layer of the recording pipeline:

| File | What it tests |
|------|---------------|
| `test_gen1_action_coords.py` | **Test 1** — action type + coordinates pass through the record pipeline unchanged |
| `test_gen2_hit_test.py` | **Test 2** — `hit_test(x, y, hierarchy)` returns the expected element + selector type/value |
| `test_gen3_step_json.py` | **Test 3** — full step JSON output (minus `timestamp`, `pre_screenshot`, `pre_screenshot_size`) matches ground truth |
| `test_gen4_selector_quality.py` | **Test 4** — `get_selector_quality(el)` + is-problematic flag match ground truth |
| `test_gen5_codegen.py` | **Test 5** — `generate_script([step], "test_case")` produces the expected Python code |

Each recording session appends new `def test_gen{N}_{fixture_key}_step_{i:03d}():` functions. Existing functions are never overwritten.

### Current fixtures (7)

| Fixture | Steps | Notes |
|---------|-------|-------|
| `Canva_20260604_114332` | 9 | tap, double_tap, long_press, swipe |
| `Canva_Text_20260604_114431` | 4 | type_text interactions |
| `Canva_Pinch_Rotate_20260604_114557` | 2 | pinch, rotate |
| `Swipe_20260604_114637` | 1 | swipe |
| `Home_Switch_Kill_20260604_114722` | 3 | home / launch_app / terminate_app |
| `Verify_visible_nonVsible_text_20260604_115547` | 5 | verify_visible, verify_not_visible, verify_get_text |
| `Verify_GT_Diff_20260604_143914` | 7 | verify_screenshot_gt, verify_screenshot_diff |

---

## Step filtering — which steps are generated per test

Not every step produces a test function in every file. `unit_test_gen.py` checks each entry in `capture.json` before generating, and silently skips generation when the test would always be vacuous:

| Test | Step is **not** generated when… |
|------|---------------------------------|
| Test 1 & 3 | `action` is `verify_screenshot_gt` or `verify_screenshot_diff` **and** `input` has no `bounds` field |
| Test 2 & 4 | `hierarchy_file` is `null` (action leaves the app: `home`, `launch_app`, `terminate_app`) |
| Test 5 | — (all steps generated; codegen output is always testable) |

> These steps are **not generated at all** — they do not appear as `SKIPPED` in the test run.

Concrete examples from existing fixtures:

- **`Home_Switch_Kill` steps 0-2** (home / launch_app / terminate_app): no hierarchy captured → absent from gen2 and gen4.
- **`Verify_visible` step 4** (verify_not_visible with app in background): no hierarchy → absent from gen2 and gen4.
- **`Verify_GT_Diff` steps 0, 5, 6** (screenshot compare without element bounds): no bounds → absent from gen1 and gen3.

---

## Ground-truth / answer files

Answers live in `test_unittest/answers/<fixture_key>.json`. Keys are `step_NNN_tM`.

**First run** — the answer file doesn't exist yet. `_load_or_store()` computes the result, saves it, and calls `pytest.fail()` so you see what was stored. The test fails on first run by design.

**Subsequent runs** — the stored answer is loaded and compared. If a code change produces a different result, the test fails (regression detected).

To update a ground truth after an intentional change: delete the relevant key from the `.json` file (or the whole file) and re-run the test.

---

## Unit Test Capture Mode (`--unit_test`)

Run the recorder server with the `--unit_test` flag to capture real input/output pairs from actual device interactions:

```bash
bash start.sh --unit_test
```

The server behaves identically to normal mode — every `_record_*` call also appends to an in-memory list.

### How it works

Every recorded step appends an entry with three fields:

```json
{
  "input":          { "action": "tap", "x": 140.0, "y": 222.0 },
  "output":         { "action": "tap", "coords": {"x": 140, "y": 222}, "target": { ... } },
  "hierarchy_file": "hierarchy_000.xml"
}
```

`pre_screenshot` and `pre_screenshot_size` are stripped from `output`.  
Steps where WDA hierarchy was unavailable have `"hierarchy_file": null`.

### API endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/unit_test/status` | `GET` | `{"enabled": true/false, "entry_count": N}` |
| `/api/unit_test/save` | `POST` | Saves captured entries to `test_unittest/fixtures/` |
| `/api/unit_test/entries` | `DELETE` | Clears in-memory entries without touching `_steps` |

`DELETE /api/steps` also clears entries automatically.

### Saving a capture

`POST /api/unit_test/save` with `{"case_name": "my_capture"}` creates a timestamped subfolder:

```
test_unittest/fixtures/my_capture_20260603_143510/
├── capture.json          ← step inputs, outputs, hierarchy_file refs
├── hierarchy_000.xml     ← WDA page source at step 0
├── hierarchy_001.xml     ← WDA page source at step 1
└── hierarchy_NNN.xml     ← one file per recorded step (omitted if null)
```

**`capture.json`** structure:
```json
{
  "captured_at": "2026-01-01T12:00:00",
  "case_name": "my_capture",
  "entries": [
    {
      "input":          { "action": "tap", "x": 140.0, "y": 222.0 },
      "output":         { "action": "tap", "coords": {"x": 140, "y": 222}, "target": { ... } },
      "hierarchy_file": "hierarchy_000.xml"
    },
    {
      "input":          { "action": "home" },
      "output":         { "action": "home" },
      "hierarchy_file": null
    }
  ],
  "steps": [ ... ],
  "codegen_output": "import pytest\n..."
}
```

### Folder layout after saving

```
test_unittest/
├── fixtures/
│   └── MyTest_20260603_143510/
│       ├── capture.json
│       ├── hierarchy_000.xml
│       └── hierarchy_NNN.xml
├── answers/
│   └── MyTest_20260603_143510.json   ← auto-created on first run
├── test_gen1_action_coords.py
├── test_gen2_hit_test.py
├── test_gen3_step_json.py
├── test_gen4_selector_quality.py
└── test_gen5_codegen.py
```

### Workflow

1. `bash start.sh --unit_test`
2. Record a test scenario in the UI (enter a case name, hit Record)
3. Click **⬇ Save Unit Test** in the UI
4. The modal shows the fixture files + the gen test files that were updated
5. Run tests immediately: `python3 -m pytest test_unittest/ -v`  
   — first run stores ground truth (test **fails** with the stored value shown); re-run passes
6. To add more cases: record another scenario and click Save Unit Test again — new functions are appended

---

## Markers & conftest

**Pytest markers** (registered in `test_unittest/pytest.ini`):

| Marker | Meaning |
|--------|---------|
| `unit` | No device or server needed — set via `pytestmark = pytest.mark.unit` in every gen file |
| `smoke` | Fast, high-confidence sanity checks |
| `regression` | Full regression suite |
| `slow` | Tests that take more than 30 seconds |

**`test_unittest/conftest.py` fixtures:**

| Fixture | Scope | Description |
|---------|-------|-------------|
| `FIXTURE_XML` | module constant | XML string of the shared element hierarchy (used by old block tests) |
| `fixture_xml` | session | Same string as a pytest fixture |
| `fixture_root` | session | Parsed `ET.Element` from `fixture_xml` |
| `unit_client` | function | FastAPI `TestClient` with WDA + background tasks mocked; `_cache["root"]` pre-populated |
| `client` | session | `httpx.Client` pointed at `localhost:8888` (integration only) |
| `clear_steps` | autouse | No-op for `unit` tests; `DELETE /api/steps` for integration tests |
| `warm_tree` | function | `GET /api/tree` to warm `_cache["root"]` (integration only) |
