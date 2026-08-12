# iOS Recorder v2 — Project Guide

## What This Project Does

A **visual test automation recorder for iOS apps**.

1. User opens the web UI (port 8888) and connects to an iOS device via WebDriver Agent (WDA).
2. User performs gestures in the recorder UI — each action is logged as a step with intelligent element selectors.
3. User exports the recording as a ready-to-run `pytest` + Appium test file.
4. Tests run on real iOS devices via Appium / XCUITest and report results to ReportPortal.

## Architecture

```
iosRecorder_v2/
├── app/                    # FastAPI backend — recording server (port 8888)
│   ├── main.py             # All API endpoints + recording engine + WDA proxy
│   ├── codegen.py          # Converts recorded steps → pytest code
│   ├── cli.py              # JSON-first CLI for validate/codegen/export automation
│   ├── hittest.py          # Score-based element detection at a coordinate
│   ├── selector.py         # Builds the most stable selector for an element
│   ├── unit_test_gen.py    # Generates test_gen1..5 + test_gen3b pytest files from --unit_test captures
│   └── wda.py              # Async HTTP client for WebDriver Agent
├── static/                 # Vanilla JS/HTML/CSS frontend UI
│   ├── index.html          # Main recorder page
│   ├── app.js              # Frontend controller (WebSocket + REST)
│   └── style.css           # UI styling
└── pytest/                 # Appium + pytest test framework
    ├── conftest.py          # Fixtures: driver (function — fresh WDA session per test), actions (function), screenshot_on_failure (autouse), _failure_evidence_workspace (autouse), _log_auto_healing_context (autouse); auto-healing hooks
    ├── auto_healing.py      # Auto-healing integration: failure evidence, state.json, known-issue lane, retry lane, Phase 2 trigger
    ├── known_issue.json     # Cases whose failure is already understood (reason is in the test file name); a repeat of the recorded failure signature skips auto-healing
    ├── refresh_known_issue.py  # Rebuilds known_issue.json from the test file names (`--check` reports drift); keeps bug_code + recorded signatures
    ├── config.py            # Device capabilities (UDID, bundle ID, Appium URL) + auto-healing switches
    ├── driver/
    │   ├── driver_setup.py  # Creates/quits the Appium driver
    │   └── driver_actions.py  # All gesture/assertion helpers (DriverActions class)
    ├── pages/
    │   └── base_page.py     # Page object base class
    └── tests/               # Generated test files (test_*.py)
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, uvicorn, httpx (async), pydantic |
| iOS Automation | Appium, XCUITest, WebDriver Agent, iproxy |
| Frontend | Vanilla JS, HTML5 Canvas, SVG |
| Test Framework | pytest, Appium Python client |
| Reporting | ReportPortal (pytest-reportportal) |

## Key Concepts

### Step dict schema (recorded by main.py, consumed by codegen.py)
```python
{
  "action":    str,             # "tap" | "swipe" | "paint" | "long_press" | "verify_visible" | ...
  "coords":    dict,            # x, y  (single point) or x1,y1,x2,y2 (gesture)
  "target":    dict | None,     # { "type": "accessibility id"|"name"|"xpath"|"coordinate",
                                #   "value": str,
                                #   "offset_pct": {"x": float, "y": float},   ← optional
                                #   "selector_quality": "id"|"id_eq_label"|"label_only"|"xpath_only",  ← optional
                                #   "bounds": {"x":int,"y":int,"w":int,"h":int} }  ← optional (device pts)
  "timestamp": str,
  # action-specific extras:
  "duration":  int,             # ms (long_press, swipe, drag, paint)
  "scale":     float,           # pinch
  "rotation":  float,           # degrees (rotate)
  "text":      str,             # type_text
  "bundle_id": str,             # launch_app / activate_app / terminate_app
  "expected_text": str,         # verify_get_text
  "appear_timeout": float,      # wait_until_not_show: seconds for the element to show up (default 5)
  "disappear_timeout": float,   # wait_until_not_show: seconds for it to go away again (default 1200 = 20 min);
                                # the two budgets are counted separately
  "screenshot_name": str,       # verify_screenshot_*
  "wait_seconds": float,        # verify_tap_screenshot_diff: delay after tap before AFTER screenshot
  "action_target": dict,        # verify_tap_screenshot_diff: the element to tap between captures
  "action_coords": dict,        # verify_tap_screenshot_diff coordinate fallback for tap action
  "expected_result": str,       # verify_screenshot_diff / verify_tap_screenshot_diff: "same" | "different"
  "scroll_container": dict,     # tap/long_press: innermost scrollable *ancestor* of the target —
                                # never a container that merely overlaps the tap coordinate;
                                # scroll: innermost scrollable container at the gesture coordinate.
                                # (type, value, selector_quality, bounds); used by
                                # codegen to pass container_by/container_value/container_w/container_h
                                # to find_element() for auto-scroll fallback during playback
  "paint_points_pct": list,     # paint: free-form stroke points relative to target element bounds
                                # [ {"x_pct": float, "y_pct": float, "t_ms": int}, ... ]
}
```

### Device selection (start.sh)
`start.sh` always passes `iproxy -u <UDID>` — never rely on iproxy's implicit "first device" pick, which silently tunnels to the wrong device when more than one is attached (symptom: `Error connecting to device: Connection refused` in `/tmp/ios-recorder-iproxy.log` and `WDA session failed: ReadError('')` in the server log). UDID resolution order:

1. `--udid <UDID>` argument or `RECORDER_UDID` env var
2. `appium:udid` from `pytest/config.py` — if that device is attached; keeps recording and playback on the same device
3. The only attached device
4. Multiple devices, no config match — probe each one's port 8100 and pick the one answering WDA `/status`

A leftover `iproxy` already listening on 8100 is only reused after WDA `/status` answers; otherwise the script exits and tells you which pid to kill. Health probes retry with a 15s timeout because a WDA busy with a page-source fetch (routinely 4–5s) serialises requests.

### Selector priority (app/selector.py)
1. `accessibility id` — element `name` attribute (skip if starts with `0x`)
2. `name` — element `label` attribute
3. `xpath` fallback — `//{tag}`

Runtime override: when started with `bash start.sh --xpath` (`RECORDER_XPATH_ONLY=1`), selector output is forced to `xpath` for all recorded targets (including scroll containers), while `hit_test` element selection logic remains unchanged.

### Code generation output (app/codegen.py)
- Every step → a `with step("..."):` block wrapping the `actions.*()` call
- Labels: `[Action] ...` for gestures, `[Verify] ...` for assertions
- Falls back to a `# comment` when no element matched (never crashes)
- Test function name and `@pytest.mark.name` derived from case name + timestamp suffix (`_YYYYMMDD_HHMMSS`) appended at export time
- For `verify_screenshot_diff(before) -> long_press -> verify_screenshot_diff(after)` on compare-tagged element ids, codegen emits a hold-time capture flow: before capture -> start long press -> after capture -> release (`recording_rules.json` controls keyword/type matching)
- `wait_until_not_show` → `assert actions.wait_until_not_show(by, value, appear_timeout=N, disappear_timeout=M)`: waits for a transient element (progress bar, spinner) to appear and then vanish. The helper returns `False` instead of raising — never appeared (short budget) and still shown (long budget) are both reported through the generated `assert`

### Export output (POST /api/export)
- Backend appends timestamp to case name before generating code (e.g. `MyTest_20260508_143022`)
- Writes `pytest/tests/test_<name>.py` — ready-to-run test file (flat, unchanged)
- Creates a **timestamped subfolder** `export/<name>/` containing three files:
  - `test_<name>.py` — pytest code
  - `<name>.json` — full step list with locators, actions, coordinates
  - `<name>.html` — selector quality report: shows every step whose selector is `id_indexed`, `id_eq_label`, `label_only`, `xpath_only`, or `coordinate`; each card shows a **pre-gesture screenshot** (captured before the action is sent to the device for every recorded step) with either a bounding-box rect overlay (element found) or a crosshair marker (coordinate-only)
- UI shows `#exportResultModal` listing all saved paths; no browser download dialog

### CLI automation output (python -m app.cli)
- `validate-steps` validates step-list JSON and returns structured errors/warnings for agents
- `generate-test` writes a pytest file directly from step JSON (`generate_script` shared backend)
- `export-bundle` writes pytest code + steps JSON + selector quality HTML report in one command
- `server-status` / `server-set-config` manage recorder backend connectivity + WDA URL
- `server-record-action` drives backend `/api/record*` endpoints from JSON payloads
- `server-steps-get` / `server-steps-clear` control the backend step buffer for iterative recording loops
- `server-export` triggers backend `POST /api/export` from in-memory recorded steps
- `server-vision-snapshot` returns AI-readable status/tree/frame bundles
- `server-vision-execute` executes one AI-selected action in `record` or `live` mode
- `server-vision-loop` runs scripted `snapshot` + `action` plans for closed-loop automation
- CLI output is JSON-only to support deterministic AI/automation pipelines

### DriverActions (pytest/driver/driver_actions.py)
- Single class wrapping all iOS gestures
- `@step(...)` decorator on every public method (ReportPortal integration)
- `@wait_for_stable_hierarchy` on tap/drag/press methods (optional polling)
- All multi-touch uses XCUITest `mobile:*` script APIs, not raw W3C Actions
- Before any element is turned into a tap/drag coordinate, `_settle_rects()` waits for its `rect` to be unchanged for `element_settle_required_samples` consecutive polls (default 2) and for `visible == "true"` (max `element_settle_timeout`, default 3 s; warns and proceeds on timeout). Without it a coordinate read mid-animation makes `mobile: tap` miss while still reporting PASS. Gestures needing two element-derived points (every drag) read both from **one** quiet round via `_points_in_elements()` / `_drag_points()` — settling them one after another freezes the start point while the end point is still being measured
- A recorded drag on an `XCUIElementTypeSlider` carries the thumb position **at record time**, and a UISlider ignores touches on bare track — replaying it against a slider holding a different value does nothing at all and reports success. `_slider_grab_point()` presses the thumb's current position (derived from the control's `value`) instead. These sliders are *relative* — the value tracks the finger's displacement from wherever it grabbed — so the press must be near the thumb's centre; its size comes from `config.SLIDER_THUMB_SIZE` (40 pt, measured). The gesture then lands accurately but not to the digit (0–2 units measured), so slider readouts are verified numerically via `config.TEXT_NUMERIC_TOLERANCE`; `set_slider_value(by, value, percent)` sets a slider exactly when a faithful gesture is not required
- `find_element(by, value, ..., container_by, container_value, container_w, container_h)` — when container params are provided the lookup order is **global → container-scoped → `_find_with_scroll()`**: an already-visible (≥ 50 %) global hit returns immediately, so a stale container selector no longer fails the whole step; otherwise the container is resolved and searched internally; only then does auto-scroll run. "Visible" is measured as element ∩ container ∩ screen (`_visible_fraction(..., clip=...)`), so a cell clipped by its own collection view is not mistaken for reachable. All `*_by_locator`, `*_within_element`, `verify_visible`, and `swipe_on_element` forward these params here, so this order applies uniformly to every action.

### Frontend ↔ Backend communication
- **WebSocket** `/ws/tap` — low-latency tap events during live recording
- **REST** — everything else (swipe, drag, paint, scroll, verify, export, config)
- **REST** `/api/frame` — latest cached frame snapshot for AI/CLI vision workflows
- **MJPEG** `/api/stream` — live device screen video

## Dynamic Skill Loading

Skill files live in `.claude/commands/`. **Before responding to any task, decide which area it touches and read the corresponding file using the Read tool.** Do not wait to be asked.

| If the task involves… | Read this file first |
|-----------------------|----------------------|
| `static/` (HTML, JS, CSS) | `.claude/commands/recorder-ui.md` |
| `app/selector.py` or `app/hittest.py` | `.claude/commands/recorder-select.md` |
| `app/codegen.py` or adding a new action type | `.claude/commands/recorder-codegen.md` |
| `app/cli.py` | `.claude/commands/recorder-cli-skill.md` |
| `pytest/` — tests, `DriverActions`, conftest, config | `.claude/commands/pytest.md` |
| Multiple areas at once | Read all relevant files before starting |

If unsure which area a task belongs to, read all files. It is always better to read more than to miss a rule.

## Automatic Documentation Sync

After completing any task, read `.claude/commands/sync-docs.md` and check whether the change qualifies as a trigger. If it does, immediately update the affected doc files — do not wait to be asked. Minor bug fixes and refactors with no interface change do not require a sync.
