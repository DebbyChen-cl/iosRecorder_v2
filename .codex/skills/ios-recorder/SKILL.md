---
name: ios-recorder
description: Project-specific guidance for iOS Recorder v2 automation, recorder CLI workflows, live device recording, UI/selector/codegen/pytest changes, and documentation sync. Use when working in this repo on app/, static/, pytest/, recorder-generated tests, Appium DriverActions, selector or hit-test logic, recorder CLI usage, live recording flows, or architecture/documentation updates.
---

# iOS Recorder

Use this skill as the entry point for iOS Recorder v2 project rules. Load only the reference file that matches the task, then read the project source files named by that reference before editing or generating code.

## Reference Map

- Full project context: read [context.md](references/commands/context.md) when starting broad work or when the user asks to load project context.
- Recorder CLI usage: read [recorder-cli-skill.md](references/commands/recorder-cli-skill.md) when using `python -m app.cli` or generating/exporting tests from recorded steps.
- Live AI recording: read [record.md](references/commands/record.md) when the user asks to record a test on a live iOS device through the recorder server.
- Web UI changes: read [recorder-ui.md](references/commands/recorder-ui.md) before editing `static/index.html`, `static/app.js`, or `static/style.css`.
- Selector and hit-test changes: read [recorder-select.md](references/commands/recorder-select.md) before editing `app/selector.py` or `app/hittest.py`.
- Code generation changes: read [recorder-codegen.md](references/commands/recorder-codegen.md) before editing `app/codegen.py` or recorder step schema behavior.
- Pytest/Appium framework changes: read [pytest.md](references/commands/pytest.md) before editing files under `pytest/`, generated test files, `DriverActions`, fixtures, or pytest config.
- Documentation synchronization: read [sync-docs.md](references/commands/sync-docs.md) after changes that affect architecture, goals, structure, public endpoints, action types, selectors, gestures, fixtures, or test conventions.

## Workflow

1. Identify the affected project area from the user's request and changed files.
2. Read the matching reference file from `references/commands/`.
3. Read the source files listed inside that reference before making changes.
4. Follow the reference's mandatory rules and "Never Do" section.
5. If the task changes project architecture, public behavior, recorder schemas, endpoints, gestures, selectors, fixtures, or test conventions, run the documentation sync procedure.

For an active user-authorized conversion run, required `python3` recorder CLI,
validation, generation, and pytest commands are directly authorized; do not ask
for per-command confirmation. This does not authorize external side effects
such as submitting feedback or uploading data, which still require explicit
replay authorization.

## Scope

This skill mirrors only Markdown files from `.claude/commands/`. Do not treat unrelated `.claude` files or other documentation as part of this skill unless the user explicitly asks to add them.
