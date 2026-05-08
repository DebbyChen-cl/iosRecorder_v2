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
│   ├── hittest.py          # Score-based element detection at a coordinate
│   ├── selector.py         # Builds the most stable selector for an element
│   └── wda.py              # Async HTTP client for WebDriver Agent
├── static/                 # Vanilla JS/HTML/CSS frontend UI
│   ├── index.html          # Main recorder page
│   ├── app.js              # Frontend controller (WebSocket + REST)
│   └── style.css           # UI styling
└── pytest/                 # Appium + pytest test framework
    ├── conftest.py          # Fixtures: driver (session), actions (function), screenshot_on_failure (autouse)
    ├── config.py            # Device capabilities (UDID, bundle ID, Appium URL)
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
  "action":    str,             # "tap" | "swipe" | "long_press" | "verify_visible" | ...
  "coords":    dict,            # x, y  (single point) or x1,y1,x2,y2 (gesture)
  "target":    dict | None,     # { "type": "accessibility id"|"name"|"xpath"|"coordinate",
                                #   "value": str,
                                #   "offset_pct": {"x": float, "y": float} }  ← optional
  "timestamp": str,
  # action-specific extras:
  "duration":  int,             # ms (long_press, swipe, drag)
  "scale":     float,           # pinch
  "rotation":  float,           # degrees (rotate)
  "text":      str,             # type_text
  "bundle_id": str,             # launch_app
  "expected_text": str,         # verify_get_text
  "screenshot_name": str,       # verify_screenshot_*
}
```

### Selector priority (app/selector.py)
1. `accessibility id` — element `name` attribute (skip if starts with `0x`)
2. `name` — element `label` attribute
3. `xpath` with `@value` — only for `XCUIElementTypeTextField`, `XCUIElementTypeSecureTextField`, `XCUIElementTypeStaticText`
4. `xpath` fallback — `//{tag}`

### Code generation output (app/codegen.py)
- Every step → a `with step("..."):` block wrapping the `actions.*()` call
- Labels: `[Action] ...` for gestures, `[Verify] ...` for assertions
- Falls back to a `# comment` when no element matched (never crashes)
- Test function name derived from case name via `_safe_name()` (alnum + underscore only)

### DriverActions (pytest/driver/driver_actions.py)
- Single class wrapping all iOS gestures
- `@step(...)` decorator on every public method (ReportPortal integration)
- `@wait_for_stable_hierarchy` on tap/drag/press methods (optional polling)
- All multi-touch uses XCUITest `mobile:*` script APIs, not raw W3C Actions

### Frontend ↔ Backend communication
- **WebSocket** `/ws/tap` — low-latency tap events during live recording
- **REST** — everything else (swipe, drag, scroll, verify, export, config)
- **MJPEG** `/api/stream` — live device screen video

## Dynamic Skill Loading

Skill files live in `.claude/commands/`. **Before responding to any task, decide which area it touches and read the corresponding file using the Read tool.** Do not wait to be asked.

| If the task involves… | Read this file first |
|-----------------------|----------------------|
| `static/` (HTML, JS, CSS) | `.claude/commands/recorder-ui.md` |
| `app/selector.py` or `app/hittest.py` | `.claude/commands/recorder-select.md` |
| `app/codegen.py` or adding a new action type | `.claude/commands/recorder-codegen.md` |
| `pytest/` — tests, `DriverActions`, conftest, config | `.claude/commands/pytest.md` |
| Multiple areas at once | Read all relevant files before starting |

If unsure which area a task belongs to, read all files. It is always better to read more than to miss a rule.

## Automatic Documentation Sync

After completing any task, read `.claude/commands/sync-docs.md` and check whether the change qualifies as a trigger. If it does, immediately update the affected doc files — do not wait to be asked. Minor bug fixes and refactors with no interface change do not require a sync.
