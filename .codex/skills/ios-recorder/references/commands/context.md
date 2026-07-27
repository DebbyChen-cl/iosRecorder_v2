# Load Full Project Context

You are starting a session on the **iOS Recorder v2** project. Read the following files now to build complete context before doing any work.

## Step 1 — Project Overview
Read [CLAUDE.md](../../../CLAUDE.md)

## Step 2 — Area-Specific Rules

Read all four skill files:

- [.claude/commands/recorder-ui.md](recorder-ui.md) — rules for `static/` (HTML, JS, CSS)
- [.claude/commands/recorder-select.md](recorder-select.md) — rules for `app/selector.py`, `app/hittest.py`
- [.claude/commands/recorder-codegen.md](recorder-codegen.md) — rules for `app/codegen.py`
- [.claude/commands/pytest.md](pytest.md) — rules for `pytest/` (tests, DriverActions, conftest)

## Step 3 — Confirm Understanding

After reading, confirm:
1. What the project does (1 sentence)
2. Which area the user is about to work on
3. Which "Never Do" rules apply to that area

## Reminder

When the user's task touches a specific area, re-read the relevant skill file to ensure the rules are fresh. Do not guess at conventions — always verify against the source files before generating code.
