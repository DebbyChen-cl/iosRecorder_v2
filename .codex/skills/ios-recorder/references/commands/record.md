# Record Test — AI-Driven Live Recording Skill

You are an AI recording agent. The user provides high-level test steps; you drive a real iOS device through the recorder CLI to record each step, then generate a ready-to-run pytest file.

**Required companion CLI guide**: follow `.codex/skills/ios-recorder/references/commands/recorder-cli-skill.md` for every recorder CLI call, validation step, and test generation/export command.

**Pre-requisite**: The device must already be launched with the app open. Do NOT load unrelated skills unless explicitly asked.

## Target Selection Contract

Before touching the device, read the user's original checklist and the companion
`.codex/skills/ios-recorder/references/commands/recorder-cli-skill.md`. Convert the checklist into an ordered source-of-truth table: step number, intended action, semantic target, and expected verification. The recorded steps must be checked against this table before any pytest run.

When choosing a target, use this stability order:

1. The explicitly selected element's stable accessibility ID (`AppiumBy.ACCESSIBILITY_ID`).
2. An element-specific XPath (`AppiumBy.XPATH`), preferably structural and anchored to a stable ancestor.
3. An iOS Class Chain (`AppiumBy.IOS_CLASS_CHAIN`) only when the first two choices are unavailable and the generated test/codegen supports it.
4. Screen position / coordinates only as a last resort. Record why no stable locator was available in the final report.

The semantic target is more important than the element currently displaying a selected value:

- For a dropdown or album picker, tap the menu opener (for example `btnAlbum`) and then tap the requested item inside the opened list. Never use the currently selected album/value label as the dropdown target; that value can change between runs.
- When a requested item can be located by ID/XPath/Class Chain, tap that item directly. Do not replace the action with “swipe to next” or another position-dependent gesture merely because the item is currently adjacent; list order is allowed to change.
- A swipe is valid only when the original checklist explicitly asks for a swipe/scroll gesture or when it is required to reveal a target that cannot yet be located. In that case target the stable scroll container, preserve its metadata, then re-snapshot and locate the requested item before tapping it.
- Never reuse a stale target from the previous UI state when the checklist names a different semantic target. Capture a fresh snapshot after navigation, expansion, or scrolling.

If a generated step violates this contract, stop at review/validation, repair the steps JSON or the newly generated test, and do not proceed to pytest.

**Output contract**:
- One step group creates one new `pytest/tests/test_<case_name>.py` file containing `test_<case_name>()`.
- Multiple step groups create multiple new files, one test case per file.
- Every case must be fully self-contained: keep that case's complete scenario steps, selectors, and verifications in its own test file. Never merge requested cases through a shared case-flow helper, parameterized test, or aggregate runner. Shared framework primitives such as `DriverActions` and pytest fixtures are allowed.
- Never overwrite or edit a test file that existed when the request started. If a planned path already exists, stop before recording and ask for a different case name.
- Files created during the current request may be repaired until their full pytest run passes.

---

## Workflow

### Phase 1 — Setup

1. **Read the source checklist and CLI guide first**. The source checklist is authoritative for order, intent, targets, and verifications.
2. **Check server**: `python3 -m app.cli server-status --base-url http://localhost:8888`
3. **Parse cases** from the request. Each case requires:
   - A unique test function name (for example `test_reshape_shape_preset`)
   - Its own ordered step list
4. Ask only for names or steps that are actually missing. For multiple groups, require an unambiguous name-to-steps mapping.
5. Normalize each name to `<case_name>` without the `test_` prefix. Plan:
   - Function: `test_<case_name>`
   - File: `pytest/tests/test_<case_name>.py`
   - Scratchpad: `tmp/record_<case_name>/`
6. **Preflight every output path before touching the device**. If any file already exists or two requested names collide, do not overwrite, append, or patch it; ask for replacement names.

### Multi-Case Orchestration

Process case groups sequentially. For each case:

1. Confirm the device is at the starting state expected by that case.
2. Clear only that case's buffer:

```bash
python3 -m app.cli server-steps-clear --base-url http://localhost:8888
```

3. Record, validate, generate, and run that case before moving to the next case. If the case reaches a terminal case-local `blocked` or `failed` result, preserve its artifacts and continue with the next case after the main agent reconciles the report.
4. Store snapshots and steps in that case's unique scratchpad; never reuse another case's JSON.
5. Do not silently use `live` actions for logical setup that the generated test also needs. Record the setup as test steps. Reserve `live` mode for environment-only interruptions or restoring the recorded initial state before pytest.

Pause all cases only for a verified global WDA, recorder-server, or device
blocker.

### Phase 2 — Record Each Step

For every step in the user's list, repeat this loop:

#### 2a. Snapshot — understand the screen

```bash
python3 -m app.cli server-vision-snapshot \
  --include-frame-data \
  --output <scratchpad>/snap_<N>.json \
  --base-url http://localhost:8888
```

- Parse the `tree.elements[]` array to find elements by `name` / `label`.
- When you cannot identify the right element from the tree alone (e.g. "select the photo with a woman"), **save and view the frame image** to decide visually.
- Use `--no-include-frame` for lightweight checks (e.g. reading a slider value after adjustment).

#### 2b. Map step → action

| User step pattern | Record action | Payload |
|---|---|---|
| Tap "\<label\>" | `tap` | `{"x": <center_x>, "y": <center_y>}` |
| Expand / Open / Select (tap-like) | `tap` | same as above |
| Adjust slider to min | `drag` | `{"x1": <thumb_x>, "y1": <thumb_y>, "x2": <slider_min_x>, "y2": <thumb_y>, "duration": 500}` |
| Adjust slider to max | `drag` | `{"x1": <thumb_x>, "y1": <thumb_y>, "x2": <slider_max_x>, "y2": <thumb_y>, "duration": 500}` |
| Swipe left/right/up/down | `swipe` | `{"x1":…, "y1":…, "x2":…, "y2":…, "duration": 500}` |
| Long press | `long_press` | `{"x":…, "y":…, "duration": 1000}` |
| Type text "\<value\>" | `type_text` | `{"text": "<value>"}` |
| Verify value = \<N\> | `verify_get_text` | `{"target_x":…, "target_y":…, "expected_text": "<N>"}` |
| Verify text "\<str\>" | `verify_get_text` | `{"target_x":…, "target_y":…, "expected_text": "<str>"}` |
| Verify element visible | `verify_visible` | `{"target_x":…, "target_y":…}` |
| Verify effect applied (different) | `verify_screenshot_diff` | `{"target_x":…, "target_y":…, "bounds": {…}, "expected_result": "different", "screenshot_name": "<name>"}` |
| Verify no effect (same) | `verify_screenshot_diff` | `{"target_x":…, "target_y":…, "bounds": {…}, "expected_result": "same", "screenshot_name": "<name>"}` |

#### 2c. Record the action

```bash
python3 -m app.cli server-record-action \
  --action <action_type> \
  --payload-json '<json>' \
  --base-url http://localhost:8888
```

#### 2d. Verify state changed

After actions that change UI state (tap, drag, swipe), take a quick snapshot to confirm:
- The expected screen appeared (check element names)
- Slider values changed to expected number
- Wait 1-2 seconds (`sleep`) before snapshot if animation is expected

#### 2e. Recover from a recording mismatch

Recording mistakes are retryable case attempts, not immediate blockers. If a
tap, coordinate, locator, or state transition does not match the checklist:

1. Stop at the first mismatch and preserve the snapshot, raw buffer, and
   failure note under the case scratchpad.
2. Do not continue from the wrong UI state and do not perform later side
   effects from that state.
3. Restore the case's recorded initial state with `live` actions, then clear
   only the current case buffer.
4. Take a fresh snapshot, repair the target/action using the Target Selection
   Contract, and re-record from the first affected step.
5. Keep the attempt history and retry up to 10 attempts for the case.

Do not mark the case `blocked` after one incorrect recorded step. Mark it
`blocked` only when an external device/service, case-specific safety approval,
or unrecoverable app state prevents continuation; mark it `failed` only after
the allowed recording/replay repairs are exhausted. A case-local blocker must
not stop unrelated cases in a multi-case conversion run.

### Phase 3 — Slider Patterns

When the step involves adjusting a slider:

1. **Identify the slider** — look for element named `cpSlider` or similar `Slider` tag
2. **Read current value** — find `valueLabel` element's label
3. **Read the slider range and requested value** — do not assume every slider's minimum is `0`; use the user's expected value and confirm it from `valueLabel`.
4. **Compute drag points**: `x(value) = slider.rect.x + (value / 100) * slider.rect.w`
5. **Drag to target** with `server-record-action --action drag`:
   - Minimum: drag from `x(current_value)` to `x(expected_min_value)`
   - Maximum: drag from `x(current_value)` to `x(100)`
   - Specific value: drag to the interpolated target point
   - Keep both start and end on `cpSlider` so codegen emits `actions.drag_within_elements(...)`.
6. **Reject generated slider swipes** — a generated `actions.swipe_on_element(..., 'cpSlider', ...)` is incorrect. Repair the current request's new pytest to use `actions.drag_within_elements(...)` with `cpSlider` as both source and target.
7. **Verify** the `valueLabel` changed to the exact expected number after the drag.
8. **Do NOT use tap or swipe** to adjust sliders; always use `drag`.

### Phase 4 — Clean Up & Generate

Complete this phase independently for each case.

1. **Get all steps**: `python3 -m app.cli server-steps-get --output <scratchpad>/final_steps.json`
2. **Review steps** — remove accidental or ineffective steps and repair incorrect targets. In particular:
   - Prefer stable accessibility IDs over text labels or coordinate-only targets.
   - Enforce the Target Selection Contract: ID > element-specific XPath > iOS Class Chain > position.
   - For dropdowns, verify the target is the menu opener, not the currently selected option/value.
   - Replace swipe-to-next/position-dependent navigation with a direct tap on the requested semantic item whenever the item has a stable locator.
   - Cross-check screenshot targets against the visible editor. Do not accept a hidden/stale `AppLogo` when the real preview is `EditingImageView_ImageView`.
   - Preserve `scroll_container` metadata so generated `DriverActions` can auto-scroll to off-screen items.
3. **Validate before generation**:

```bash
python3 -m app.cli validate-steps --input <scratchpad>/cleaned_steps.json
```

If validation fails, repair the JSON and repeat until `ok: true`. Review warnings; do not ignore warnings that indicate the selected element is wrong.

4. Re-check that the output path still does not exist, then **generate a new test file**:

```bash
python3 -m app.cli generate-test \
  --input <scratchpad>/cleaned_steps.json \
  --case-name "<case_name>" \
  --output pytest/tests/test_<case_name>.py
```

5. Confirm the generated file contains exactly `def test_<case_name>(actions: DriverActions):` and `@pytest.mark.name(...)`.
6. **Polish only the file created for the current case** — update step labels to match the user's original descriptions:
   - `[Action] Tap 'Edit'` instead of `[Action] Tap Launcher_main_edit at (48.1%, 28.0%)`
   - `[Verify] Default value = 50` instead of `[Verify] valueLabel text equals '50'`
   - Group steps by section with `# --- Section Name ---` comments when there are repeated patterns
   - Give screenshot captures meaningful names matching the context

7. **Checklist consistency gate** — compare the generated test and cleaned steps JSON one-for-one with the original checklist before executing pytest. Confirm that every original step appears exactly once in the same order, the action semantics and target match, and each requested verification is present. Extra exploratory steps, selected-value dropdown targets, swipe-to-next substitutions, coordinate-only fallbacks without a reason, and missing assertions are inconsistencies. Repair and re-run `validate-steps` until the gate passes.

### Phase 5 — Execute Pytest (Required)

Generation is not completion. Run the full test, not only syntax checks or `--collect-only`.

1. Restore the device to the same initial UI state captured before recording the case. Use `live` mode so this preparation is not appended to its completed buffer.
2. Run the new file directly. This is a maximum of 10 attempts for the case; the case is complete only after one full run exits `0`:

```bash
python3 -m pytest -q -p no:cacheprovider pytest/tests/test_<case_name>.py
```

3. After every non-zero run, record the first failing pytest node/step and failure point. Classify it as selector, action, assertion, timing, or external dependency. Repair only the current request's new file or steps JSON when appropriate, restore the recorded initial state, and rerun. Do not blindly retry an unchanged deterministic failure. Stop after attempt 10 and report the blocker exactly.
4. Do not claim success until the command exits `0`. If an external dependency blocks execution (Appium, WDA, device, app state), report the exact blocker and command output.
5. For multiple cases:
   - Run every new file individually, restoring its recorded initial state before each run.
   - After all individual runs pass, restore the expected suite start state and run all newly created files together to expose shared-session state coupling:

```bash
python3 -m pytest -q -p no:cacheprovider <new_file_1.py> <new_file_2.py> ...
```

### Phase 6 — Final Result Report (Required)

Write `<scratchpad>/final_report.md` after the consistency gate and pytest attempts. It must contain these fields, using the original user wording where possible:

```markdown
# Final Result Report

## Original steps
- 1. ...
- 2. ...

## Generated file
- `pytest/tests/test_<case_name>.py`

## Step consistency
- Result: PASS / FAIL
- Notes: one-to-one checklist mapping, target corrections, and any removed exploratory steps

## Pytest result
- Result: PASS / FAIL / BLOCKED
- Attempts: <n>/10
- Command: `python3 -m pytest -q -p no:cacheprovider ...`

## Pytest fail point
- None (when PASS), or the first failing node/step and concise root cause

## Attempt history
| Attempt | Result | First fail point |
|---:|---|---|
| 1 | PASS/FAIL | ... |
```

Never omit the fail point: use `None` only when the test passed, and use the exact external blocker when pytest could not execute.

---

## Key Rules

1. **Always snapshot before acting** — never guess coordinates; read the element tree first.
2. **View the frame image** when visual identification is needed (photo selection, icon recognition).
3. **Verify after every state-changing action** — take a snapshot to confirm the UI transitioned.
4. **Slider = drag, never tap or swipe** — record slider adjustments as `drag` and generate `actions.drag_within_elements(...)`.
5. **verify_get_text uses `target_x`/`target_y`** (not `x`/`y`).
6. **verify_screenshot_diff uses `target_x`/`target_y` + `bounds`** — target the preview image area.
7. **One action per CLI call** — never batch multiple actions into one call.
8. **Sleep 1-2s** between action and verification snapshot when animations are involved.
9. **Clean up bad steps** before generating — remove any steps that didn't produce the intended effect.
10. **Use `python3`** (not `python`) for all CLI calls.
11. **Create only new test files** — never modify a test file that predated the request.
12. **One standalone case per file** — multiple input groups produce multiple files and isolated recorder buffers; never extract their scenario flows into a shared helper or parameterized aggregate.
13. **Validate then execute** — `validate-steps` and a full passing pytest run are both mandatory.
14. **Do not treat collection as execution** — `--collect-only` cannot satisfy the pytest requirement.

---

## Common Element Patterns (PhotoDirector)

These are frequently seen elements — use as hints, always verify via snapshot:

| UI Element | Typical `name` | Location |
|---|---|---|
| Edit button (home) | `Launcher_main_edit` | Home screen |
| Album dropdown | `btnAlbum` | Photo picker |
| Album list | `albumCollectionView` | Photo picker |
| Photo grid | `photoCollectionView` | Photo picker |
| Sample photos | `PhDM_example_<N>` | Sample Photos album |
| Bottom menu tabs | `ScrollableMenuView` | Edit view |
| Feature tool bar | `EditViewControllerBottomBarCollectionView` | Edit view |
| Beautify tools | `photoEditFeatureCollectionView` | Beautify panel |
| Reshape presets | `adjustableOptionCollectionView` | Reshape panel |
| Intensity slider | `cpSlider` | Any adjustment panel |
| Slider value | `valueLabel` | Next to slider |
| Cancel | `btn_cancel_n` | Bottom left |
| Confirm | `btn_ok_n` | Bottom right |
| Undo / Redo | `ic_undo` / `ic_redo` | Bottom bar |

Always expand the photo-picker album list through `btnAlbum`. Never use the
currently selected album label (for example, `Sample Photos`) as the dropdown
target because that label changes with the previous picker state. After opening
the list, select the requested album inside `albumCollectionView`.

---

## Error Recovery

- **422 error**: check required fields — verify actions need `target_x`/`target_y`, not `x`/`y`
- **Slider didn't move or stopped at the wrong value**: use `drag`, not `tap` or `swipe`; drag between percentage points inside `cpSlider` and verify `valueLabel`
- **Wrong element tapped**: re-snapshot, recalculate coordinates from element rect center
- **Premium popup blocking**: these overlays usually don't block interaction — continue recording through them
- **Element not found in tree**: scroll or swipe to reveal it, then re-snapshot
- **Output file already exists**: stop and request a new case name; never overwrite or edit the existing file
- **Generated screenshot target is stale/hidden**: repair the steps JSON to the visible preview accessibility ID, validate again, then regenerate
- **Pytest fails after generation**: restore the recorded initial state, fix only the newly created output/steps, and rerun the full test
- **Multiple cases interfere with each other**: keep individual runs passing, then fix recorded setup/teardown or case ordering until the aggregate run also passes
