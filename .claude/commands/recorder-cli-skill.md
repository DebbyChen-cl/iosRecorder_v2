# Recorder CLI Skill Guide

Use this guide when an AI agent needs deterministic, non-interactive recorder automation.

## Purpose

Translate high-level recorder tasks into stable JSON-first CLI calls.

## CLI Entry

Use module mode:

```bash
python -m app.cli <command> [flags]
```

All command outputs are JSON.

## Commands

### validate-steps

Validate step schema and selector-quality risks before generation.

```bash
python -m app.cli validate-steps --input <steps.json>
```

### generate-test

Generate one pytest file from steps.

```bash
python -m app.cli generate-test \
  --input <steps.json> \
  --case-name <CaseName> \
  --output <pytest/tests/test_case.py>
```

### export-bundle

Export pytest code + steps JSON + selector report HTML.

```bash
python -m app.cli export-bundle \
  --input <steps.json> \
  --case-name <CaseName> \
  --export-dir export \
  --tests-dir pytest/tests
```

Use `--no-append-timestamp` for deterministic output names.

### server-status

Check recorder server + WDA session status.

```bash
python -m app.cli server-status --base-url http://localhost:8888
```

### server-set-config

Set backend WDA URL.

```bash
python -m app.cli server-set-config \
  --base-url http://localhost:8888 \
  --wda-url http://localhost:8100
```

### server-steps-get / server-steps-clear

Read or clear backend recording buffer.

```bash
python -m app.cli server-steps-get --output tmp/steps.json
python -m app.cli server-steps-clear
```

### server-record-action

Call backend recording endpoints (`/api/record*`) with JSON payload.

```bash
python -m app.cli server-record-action \
  --action tap \
  --payload-json '{"x": 120, "y": 240}'
```

Supported actions include `tap`, `double_tap`, `scroll`, `swipe`, `drag`,
`long_press_drag`, `paint`, `type_text`, `verify_*`, `verify_tap_screenshot_diff`,
`scroll_target`, `swipe_target`.

### server-export

Trigger backend export from current backend step buffer.

```bash
python -m app.cli server-export --case-name DemoCase
```

### server-vision-snapshot

Capture an AI-readable snapshot bundle (status + tree + latest frame).

```bash
python -m app.cli server-vision-snapshot \
  --include-frame-data \
  --output tmp/vision_snapshot.json
```

Use `--no-include-tree` or `--no-include-frame` to reduce payload size.

### server-vision-execute

Execute one AI-selected action in either `record` mode or `live` mode.

```bash
python -m app.cli server-vision-execute \
  --action tap \
  --mode live \
  --payload-json '{"x": 120, "y": 240}'
```

### server-vision-loop

Run a scripted loop from JSON plan (`snapshot` + `action` steps).

```bash
python -m app.cli server-vision-loop \
  --plan-file tmp/vision_plan.json \
  --output tmp/vision_result.json
```

Plan format:

```json
{
  "steps": [
    {"type": "snapshot", "include_frame_data": false},
    {"type": "action", "action": "tap", "mode": "record", "payload": {"x": 100, "y": 200}}
  ]
}
```

## Agent Workflow

1. Call `validate-steps`.
2. If validation fails, repair input JSON and retry.
3. For quick output, call `generate-test`.
4. For full artifacts, call `export-bundle`.

For live-device orchestration:

1. Call `server-status` to verify connectivity.
2. Call `server-set-config` when WDA URL must change.
3. Call `server-steps-clear` to reset session buffer.
4. Call `server-record-action` repeatedly for gesture/assertion recording.
5. Call `server-steps-get` for intermediate inspection.
6. Call `server-export` to produce final test artifacts.

For visual AI control loops:

1. Call `server-vision-snapshot` to read current screen/tree context.
2. Let the AI choose the next action + payload.
3. Call `server-vision-execute` to apply that action.
4. Repeat 1-3 until goal reached, or run a prebuilt `server-vision-loop` plan.

## Error Handling

- Exit code `0`: success
- Exit code `2`: validation/command errors
- Exit code `3`: file/JSON input errors

Always parse JSON `error.code` for agent retry logic.
