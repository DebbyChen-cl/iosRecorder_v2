---
name: convert-code
description: Convert legacy nested iOS/Appium test methods into individually recorded, locator-repaired, four-digit-sequence-numbered pytest test files. Use when converting cases from `/Users/rdqe/Desktop/rdqe-ios-autotest-phdm/SFT/test_pytest_iPHD_SFT_renew.py` or a compatible legacy suite, tracking hundreds of cases, preserving existing local files with timestamped names, and running each generated case through the iOS Recorder workflow.
---

# Convert Code

Use this skill for the long-running legacy-to-recorder conversion harness. It owns case extraction and progress tracking; `$ios-recorder` owns live-device recording, step validation, code generation, and pytest conventions.

## Required resources

Read [conversion-workflow.md](references/conversion-workflow.md) before converting cases. Run `scripts/case_tracker.py` to create or update the local To Do file; do not hand-edit progress fields.

For fresh-session orchestration, also read [subagent-protocol.md](references/subagent-protocol.md). The default worker dispatch preference is `GPT-5.6 Luna` with reasoning `High`; apply it through the runtime's model/reasoning controls when those controls are available.

The default tracker is `tmp/convert_code_todo.json`. Keep it local and resumable. Do not commit it unless the user asks.

## Initialize a conversion run

From the iOS Recorder repository root:

```bash
python3 .codex/skills/convert-code/scripts/case_tracker.py extract \
  --source /Users/rdqe/Desktop/rdqe-ios-autotest-phdm/SFT/test_pytest_iPHD_SFT_renew.py \
  --start-case test_main_03_01_06_2_1 \
  --expected-count 189 \
  --output tmp/convert_code_todo.json
```

The tracker is authoritative for the current run. If `extracted_count` differs from `expected_count`, stop before live recording and report the discrepancy; never invent, duplicate, or silently skip cases to reach the requested number.

## Convert one case at a time

1. Read the next `pending` case and its wrapper from the tracker, then resolve the delegated helper (for example `_tc.test_feedback_order_problems`) in the legacy source and inspect its locator/page-object declarations. Treat the complete helper method—not the outer `@pytest.mark.online def test_main_*` wrapper—as the worker's source-of-truth. Preserve every `with self.rp_step(...)` block, assertion, helper call, conditional, wait, and external side effect; do not infer a shorter scenario from the wrapper name.
2. Mark the case `recording` before touching the device:

   ```bash
   python3 .codex/skills/convert-code/scripts/case_tracker.py update \
     --input tmp/convert_code_todo.json --case <source_case> --status recording
   ```

3. Preflight the output path. Assign the run's next four-digit sequence number before recording and use `pytest/tests/test_<NNNN>_<safe_case>.py` (for this resumed run: `test_0007_main_03_01_06_2_2.py`, then `0008`, `0009`, ...). Pass `<NNNN>_<safe_case>` as the generated case identity so the function and marker remain consistent with the numbered artifact. Never overwrite a pre-existing local test; if the exact numbered path already exists, preserve it and use a timestamped collision path with the same numbered identity.
4. Use `$ios-recorder` live-recording rules: verify server/device state, clear only the case buffer, snapshot before every action, record one action per CLI call, snapshot after state changes, use ID > XPath > class chain > coordinates, and keep explicit assertions for every source verification.
5. Save all snapshots and intermediate JSON under `tmp/record_<output_case>/`. Fetch the recorder buffer, remove ineffective exploratory actions, repair stale targets, and check the cleaned steps against the complete source method.
6. Run `validate-steps`, then `generate-test`. Confirm the new file has one test function with only `actions: DriverActions`, a `@pytest.mark.name(...)` marker, ReportPortal step contexts, and explicit verification assertions.
7. Restore the recorded initial UI state and run the full generated file:

   ```bash
   python3 -m pytest -q -p no:cacheprovider pytest/tests/test_<NNNN>_<output_case>.py
   ```

   Repair deterministic selector/action/timing failures in the current new file or cleaned steps, restore state, and retry. Allow at most 10 attempts per case. A blocked device, missing WDA/Appium service, or safety approval is not a pass. A recording or replay error is recoverable: restore the case's initial state, clear only that case's buffer, repair the affected locator or action, and re-record/replay from the first affected step. Do not mark the case blocked after a single wrong tap, stale coordinate, or selector error.
   If the sub-agent execution does not finish with pytest exit code `0`—including a pytest assertion/selector failure, fixture/WDA failure, safety stop, or other blocked execution—preserve the generated file locally and make its final executable step an explicit ReportPortal assertion failure: `with step("[Verify] Conversion execution failed"):` followed by `assert False, "<exact fail point>"`. Do not leave a terminal non-PASS artifact ending in `assert True`.
8. If the case submits feedback, uploads an image, calls a paid/remote service, or otherwise transmits data, stop before that external side effect unless the user has explicitly authorized the replay. Do not bypass an approval block by editing out the source step or using an indirect action.
9. Write `tmp/record_<NNNN>_<output_case>/final_report.md` with source steps, numbered output file, one-to-one consistency result, pytest result, attempts, first failure point, and attempt history. Mark the tracker `passed`, `blocked`, or `failed` with the report path.

Case-local failures are terminal only for that case. After the main agent verifies
the report and artifacts, it must continue with the next non-terminal case. Pause
the whole conversion run only for a global blocker such as unavailable WDA or
recorder service, device loss affecting all cases, or a required global safety
approval. A case-specific safety approval or app-state problem must be reported
as that case's blocker while later independent cases continue.

## Main-agent / sub-agent mode

Use a new sub-agent session for each case when the runtime supports sub-agents. The main agent remains the scheduler and source of truth; the sub-agent owns only the currently claimed case. Claim atomically before assigning work:

```bash
python3 .codex/skills/convert-code/scripts/case_tracker.py claim \
  --input tmp/convert_code_todo.json \
  --case test_main_03_01_06_2_1 \
  --worker-id convert-worker-001
```

Pass the sub-agent only the claimed case name, the resolved helper method source (plus a compact wrapper-to-helper mapping for provenance), worker ID/lease ID, assigned four-digit sequence number, numbered output path, scratchpad path, and the direct references needed for that case. Do not pass only the outer `test_main_*` wrapper, and do not pass the entire 188-case source into every session. The sub-agent must use `$ios-recorder`, update the claimed case through the tracker, and return a short structured result containing status, report path, generated file, pytest result, attempts, and first failure point.

Only one sub-agent may drive the shared WDA/recorder device at a time. Do not parallelize live recording or pytest on the same device; a fresh session reduces context-window growth, not device contention. Parallelize only source inspection or non-device review when it cannot touch the recorder buffer, WDA, or shared output path.

After the sub-agent exits, the main agent must inspect the report and tracker, reconcile artifacts, release/mark the case terminal, and claim the next case. Never let a sub-agent choose the next case or modify another case's status.

### Long-running worker wait cadence

When a worker is still running and no immediate result is required, do not poll
continuously or ask the user for repeated approval/status input. Check the
worker, tracker, and relevant report using exponential backoff: **2 minutes,
4 minutes, 8 minutes, 16 minutes, 32 minutes, and so on**. Reset the cadence
only when the worker returns, the user asks for an immediate update, or a
verified global blocker requires action. During the wait, do not touch the
shared WDA/recorder buffer or dispatch another device worker.

### Worker visibility and switching

The main agent is the control plane for every worker. Keep the worker ID and
lease visible in run status, and relay each meaningful worker acknowledgement
to the user. Use the runtime worker `send_input` capability for an in-progress
status request and `wait_agent` for completion. Do not claim that the user can
switch into a worker transcript unless the runtime actually exposes that UI.
A `wait_agent` timeout is not a worker result: retain the lease, inspect the
tracker and case artifacts, and continue waiting on the prescribed cadence.

When a worker stops, interrupts, blocks, or completes, require its mandatory
stop acknowledgement before closing it or dispatching another worker. The
acknowledgement must include `status`, `report`, `generated_file`,
`pytest_result`, `attempts`, `fail_point`, and `notes`; for an interruption,
include the exact last command or step.

## Resume and inspect progress

```bash
python3 .codex/skills/convert-code/scripts/case_tracker.py next --input tmp/convert_code_todo.json
python3 .codex/skills/convert-code/scripts/case_tracker.py summary --input tmp/convert_code_todo.json
```

Resume only from the first non-terminal case. Preserve completed outputs and their reports. If a user asks to continue after a blocked case, re-check the same blocker and update that case rather than resetting the entire tracker.

## Safety and integrity rules

- For this conversion workflow, the user has directly authorized the required
  `python3` commands (including tracker, recorder CLI, validation, generation,
  and pytest commands). Do not ask for per-command confirmation. This
  authorization does not cover external side effects such as submitting
  feedback, uploading data, or calling paid/remote services; those still need
  explicit authorization before replay.
- Preserve the legacy source file; it is read-only input.
- Never overwrite a pre-existing `pytest/tests/test_*.py` file.
- Every generated conversion artifact must use the run sequence prefix `test_<NNNN>_...` with exactly four digits; preserve the source case name after the prefix and increment the prefix for each subsequent case.
- Never claim a case passed without a full pytest exit code `0`.
- For every sub-agent execution result other than PASS, the local generated test must end with `with step("[Verify] Conversion execution failed"):` and `assert False` containing the exact blocker or first failure point.
- Do not treat syntax checks, collection, generated code, or recorder validation as pytest success.
- Keep source order and source case names; record a discrepancy when the requested total and extracted total differ.
- Do not run all cases in one opaque batch. Update the local tracker after every meaningful transition so an interrupted run can resume safely.
