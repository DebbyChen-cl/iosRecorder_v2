# Sub-agent protocol

## Main agent responsibilities

The main agent owns:

1. tracker initialization and count validation;
2. exclusive live-device scheduling;
3. atomic case claims and worker leases;
4. output-path collision checks;
5. starting a fresh sub-agent with one case only;
6. reviewing the returned report and generated file;
7. terminal status updates and selecting the next case.

The main agent must never dispatch two workers that can reach the same WDA/recorder server concurrently. A worker that loses its session must be marked `blocked` or returned to `pending` only after the main agent verifies no artifacts are still changing.

Blocker scope is explicit:

- A case-local locator/action mismatch, unexpected app screen, or case-specific
  approval issue ends only that case attempt. The main agent must continue with
  the next independent case after reconciling the report.
- A global WDA/recorder outage, lost device session affecting all cases, or
  global safety approval pauses the scheduler and requires recovery before any
  worker is dispatched.
- A worker must not classify a single recording error as a global blocker.

## Worker model preference

When dispatching a worker, request:

```yaml
model: "GPT-5.6 Luna"
reasoning: "high"
```

This is a runtime dispatch preference, not a pytest or recorder setting. Use the product's model and reasoning controls when available. If the runtime cannot provide this exact model or reasoning level, report the unsupported configuration to the main agent and stop the dispatch; do not silently substitute another model.

## Worker prompt contract

Start each worker with a fresh session and a compact prompt like:

```text
Use $convert-code and $ios-recorder for exactly one case.
Worker model preference: GPT-5.6 Luna
Reasoning effort: High
Case: <source_case>
Worker: <worker_id>
Lease: <lease_id>
Wrapper-to-helper mapping: <outer_test_name> -> <helper_name>
Resolved helper method source: <complete_helper_text>
Sequence: <NNNN>
Output file: <output_file>
Scratchpad: <scratchpad>

Record, clean, validate, generate, and run only this case. Do not claim another
case, overwrite an existing test, clear another worker's buffer, or choose the
next case. Return JSON with status, report, generated_file, pytest_result,
attempts, fail_point, and notes.
```

The main agent must resolve the wrapper's delegated helper before dispatch. The worker payload must contain the complete helper method source and may include only the direct locator/page-object declarations needed to interpret it. Do not send only an outer `@pytest.mark.online def test_main_*` wrapper. The worker may read additional referenced helper methods and locator declarations as needed, but must not load the whole legacy suite unless a helper resolution requires it.

If execution does not finish with pytest exit code `0`, the worker must leave the generated file on disk and make its final executable step an explicit ReportPortal failure context:

```python
with step("[Verify] Conversion execution failed"):
    assert False, "<exact blocker or first failure point>"
```

Never return a non-PASS case whose generated file ends with `assert True`.

### Mandatory stop acknowledgement

The worker must never stop silently. Before returning, being interrupted, or
classifying a case as blocked/failed, it must write or update the case report
and send the main agent a compact structured result containing `status`,
`report`, `generated_file`, `pytest_result`, `attempts`, `fail_point`, and
`notes`. If it is interrupted before any artifact can be written, it must still
return that same structure with `status: "interrupted"`, null paths/results as
appropriate, and the exact last command or step. The main agent must reconcile
that acknowledgement before releasing the lease or dispatching another worker.

The runtime does not necessarily provide a user-facing transcript switch. Do
not promise direct worker-session switching. Expose progress through the main
agent by relaying status acknowledgements, tracker state, and links to the
case-local artifacts. A `wait_agent` timeout means only that no terminal result
arrived during that wait; it is not permission to reclaim the lease or spawn a
second device worker.

For a recording mismatch, the worker must not immediately mark the case
blocked. Save the failure snapshot and raw buffer, restore the case's initial
state, clear only that case's buffer, repair the target/action, and re-record
from the first affected step. Retry up to 10 attempts per case and include the
attempt history in `final_report.md`. Use `blocked` only for an external or
safety blocker that prevents this case from proceeding; use `failed` after the
allowed recording/replay repairs are exhausted.

## Worker lifecycle

```text
pending -> assigned -> recording -> validating -> generated -> running -> passed
                                      \-> blocked / failed
```

The `case_tracker.py claim` command creates the `assigned` state and a lease. The worker changes status as work progresses. The main agent treats a worker's report as untrusted until it verifies the report path, generated file, cleaned steps, validation result, and full pytest result.

## Context-window rules

- One worker session handles one case.
- Store source text, snapshots, raw/cleaned steps, generated test, logs, and the final report on disk under the case scratchpad.
- Return summaries and paths, not full snapshots or full pytest logs, to the main agent.
- Start a new worker after every terminal case; do not keep one worker alive across the suite.
- If a case is blocked by WDA, approval, or device state, preserve its artifacts and stop that worker; do not let the worker continue into another case.
- After the main agent verifies a case-local terminal report, immediately
  release that worker and continue scheduling the next non-terminal case. Do
  not stop the whole run unless the blocker is verified global.
