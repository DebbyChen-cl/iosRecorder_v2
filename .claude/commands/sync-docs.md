# Sync Documentation

This procedure runs automatically after any change that affects project architecture, goals, or structure. Do not wait to be asked.

## Trigger Conditions

Run this procedure after completing a task that involves any of the following:

| Change type | Examples |
|-------------|---------|
| New action type | Adding a new `if action == "..."` block in `codegen.py` |
| New gesture method | Adding a method to `DriverActions` in `driver_actions.py` |
| New API endpoint | Adding a route in `app/main.py` |
| New selector strategy | Adding a new priority level in `selector.py` |
| New file or directory | New module in `app/`, `static/`, or `pytest/` |
| Changed pipeline | Recording flow, step dict schema, export format |
| Changed fixture or test pattern | New fixture in `conftest.py`, new test convention |
| Changed frontend communication | New WebSocket event, new REST endpoint called from `app.js` |

Minor changes (bug fixes, refactors with no interface change) do NOT require a doc sync.

## What to Update

For each change, update the matching skill file AND any other file that references the changed concept:

| Changed file | Update these docs |
|--------------|-------------------|
| `app/codegen.py` | `.claude/commands/recorder-codegen.md` — action type list, step dict schema |
| `app/selector.py` | `.claude/commands/recorder-select.md` — selector priority table |
| `app/hittest.py` | `.claude/commands/recorder-select.md` — scoring/serialization notes |
| `app/main.py` | `.claude/commands/recorder-ui.md` — endpoint table; `.claude/commands/recorder-codegen.md` if step schema changed |
| `static/` | `.claude/commands/recorder-ui.md` — gesture buttons, canvas, communication |
| `pytest/driver/driver_actions.py` | `.claude/commands/pytest.md` — method reference table |
| `pytest/conftest.py` | `.claude/commands/pytest.md` — fixture reference table |
| New file / new directory | `CLAUDE.md` — architecture tree; `.github/copilot-instructions.md` — directory map |
| Overall pipeline change | `CLAUDE.md` — Key Concepts section |

## How to Update

1. Read the current content of the doc file to be updated
2. Identify only the sections that are now stale — do not rewrite the whole file
3. Apply a targeted edit that reflects the actual change
4. If the change adds something new (new method, new action type), add it to the relevant table or list
5. If the change removes something, delete the corresponding entry
6. Keep the existing structure and tone — do not reorganize unless the structure itself is wrong

## After Updating

Say which doc files were updated and what specifically changed. One line per file is enough.
