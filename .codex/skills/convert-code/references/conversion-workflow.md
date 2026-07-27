# Legacy conversion workflow

## Source extraction

The legacy suite is a Python file containing test methods, usually nested in a test class. Extract methods with Python AST, preserving source order, `name`, start/end line numbers, and the complete method text. Begin at the method named by `--start-case`; include that method and every later test method in the file. Do not count methods before the start marker.

The source method is the checklist. Preserve:

- each report step and its order;
- direct taps, text values, waits, app switches, and helper calls;
- conditional branches as explicit normal-path actions plus a verification, when the branch is observable;
- every positive and negative assertion;
- external side effects such as submission, upload, or network calls.

If the source contains helper methods, inspect their definitions and locator declarations in the reference repository before recording. The outer `@pytest.mark.online def test_main_*` wrapper is only a dispatch map; resolve `_tc.<helper>()` and give the worker the complete helper method body as its checklist. A helper name alone, or the wrapper alone, is not a sufficient worker payload.

## Naming and collision policy

Normalize only characters that are invalid in a filename or Python identifier. Keep the source case identity after the run sequence prefix. Assign one monotonically increasing four-digit sequence number per conversion case and use the same numbered identity for the generated test function/marker. The preferred output is:

```text
pytest/tests/test_<NNNN>_<source_case_without_leading_test_>.py
```

For the resumed run, `test_main_03_01_06_2_2` is `test_0007_main_03_01_06_2_2.py`; the next cases are `0008`, `0009`, and so on. If the exact numbered path exists, do not overwrite it; append one timestamp to the filename and generated case identity:

```text
pytest/tests/test_<NNNN>_<source_case_without_leading_test_>_<YYYYMMDD_HHMMSS>.py
```

Do not modify a pre-existing file and do not append a second test to it. A file created during the current conversion request may be repaired in place before the case reaches a terminal state.

## Recorder-to-pytest mapping

Use `$ios-recorder` and its references for CLI details. Typical mappings are:

| Legacy intent | Recorded/generated form |
|---|---|
| tap/click a named control | stable accessibility ID, then XPath/class chain if needed |
| type a value | `type_text_by_locator(..., clear_first=True)` for replacement semantics |
| verify text/value | explicit `assert actions.verify_text(...) is not False` |
| verify visible | explicit `assert actions.verify_visible(...)` |
| verify absent | explicit `assert actions.verify_not_visible(...)` |
| switch app | `actions.activate_app(bundle_id)` followed by a feedback/page assertion when source verifies it |
| photo selection | direct semantic picker targets; never a stale coordinate or selected-value label |

For a compound legacy helper such as “clear then type,” it is valid to generate one `type_text_by_locator` call because `DriverActions` defaults to `clear_first=True`. Remove only focus-only exploratory taps that are not needed for replay, and record that normalization in the report.

When the sub-agent execution is not a PASS, preserve the generated pytest file but replace its terminal success sentinel with an explicit failure step:

```python
with step("[Verify] Conversion execution failed"):
    assert False, "<exact blocker or first failure point>"
```

This applies to pytest failures, fixture/WDA failures, safety stops, and blocked recordings. A non-PASS generated file must not end in `assert True`.

## Per-case report

Every case report must include:

```markdown
# Final Result Report

## Original steps
## Generated file
## Step consistency
## Pytest result
## Pytest fail point
## Attempt history
```

Use `PASS` only for a full pytest exit code `0`; use `BLOCKED` for a blocker that
prevents this case from proceeding (for example a case-specific approval or
device/app state issue), and use `FAIL` for a reproduced test failure after the
allowed repairs. Neither status stops the overall conversion run unless the
blocker is global.

## Recording recovery and run continuity

Treat a wrong target, stale coordinate, unexpected screen, or other recording
mistake as recoverable. Stop the current sequence at the first mismatch, save
the snapshot and raw buffer, restore the case's recorded initial state with
`live` actions, clear only the current case buffer, repair the locator/action,
and re-record from the first affected step. Keep each attempt in the case
scratchpad and record its first failure in the report. Allow up to 10 attempts
per case; do not mark a case `blocked` merely because one recording step failed.

When a case reaches terminal `blocked` or `failed`, the main scheduler must
reconcile its report, release the worker, and claim the next pending case. Stop
the entire run only when the same WDA/recorder/device or global approval blocker
would affect every remaining case. Never let a case-local failure or approval
requirement silently halt unrelated cases.
