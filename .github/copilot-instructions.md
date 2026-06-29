# iOS Recorder v2 — Copilot Instructions

## Project Overview

A **visual iOS test automation recorder**. The backend (FastAPI, port 8888) connects to a real iOS device via WebDriver Agent. Users record gestures in the web UI; the system generates `pytest` + Appium test scripts. Tests run on real devices via XCUITest and report to ReportPortal.

## Directory Map

```
app/          FastAPI backend (recording server)
  main.py       All API endpoints + step recording engine
  codegen.py    step-list → pytest file generator
  cli.py        JSON-first CLI for validate/codegen/export workflows
  hittest.py    Hit-test iOS element tree at a coordinate
  selector.py   Build most stable selector from an element
  wda.py        Async WDA HTTP client

static/       Vanilla JS frontend
  index.html    Recorder UI
  app.js        WebSocket + REST controller
  style.css     Styling

pytest/       Appium + pytest test framework
  conftest.py   Fixtures: driver (session), actions (function), screenshot_on_failure (autouse)
  config.py     Device capabilities
  driver/driver_actions.py  All gesture/assertion helpers
  tests/        Generated test files (test_*.py)
```

## Detailed Rules

Area-specific rules are loaded automatically from `.claude/commands/` via VS Code settings:

| File being edited | Rules loaded from |
|-------------------|-------------------|
| `static/` | `.claude/commands/recorder-ui.md` |
| `app/selector.py`, `app/hittest.py` | `.claude/commands/recorder-select.md` |
| `app/codegen.py` | `.claude/commands/recorder-codegen.md` |
| `pytest/` | `.claude/commands/pytest.md` |
