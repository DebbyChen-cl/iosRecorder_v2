# Recorder UI — Generation Rules

You are working on the **recorder web UI** (`static/index.html`, `static/app.js`, `static/style.css`).

Read these files before making changes:
- [static/index.html](../../../static/index.html)
- [static/app.js](../../../static/app.js)
- [static/style.css](../../../static/style.css)

---

## Architecture

The UI is **pure vanilla JS** — no frameworks, no CDN dependencies. It must work completely offline.

```
index.html   → layout + DOM structure
app.js       → all event handling, state, WebSocket + REST calls
style.css    → BEM-like class naming
```

## Communication with Backend

| Channel | Used For |
|---------|----------|
| **WebSocket** `/ws/tap` | Live tap events during recording (low latency) |
| **REST** `POST /api/record/*` | All other gestures sent to recording engine (including `paint`) |
| **REST** `POST /api/terminate_app` | Force-quit an app on device (non-recording) |
| **REST** `GET/DELETE /api/steps` | Step list management |
| **REST** `POST /api/export` | Generate and download pytest code |
| **REST** `GET /api/frame` | Latest cached device frame for AI/CLI visual snapshot |
| **MJPEG** `/api/stream` | Live device screen video |

New verify endpoint used by the UI:
- `POST /api/record/verify_tap_screenshot_diff` — one-shot verify flow that captures a target region before and after a tap action with a user-defined wait.
- `POST /api/record/wait_until_not_show` — records a wait-until-gone step for the picked element, with `appear_timeout` and `disappear_timeout` seconds.

## Gesture Sidebar

- Finger mode buttons: `data-finger="single"` / `"two"` / `"multi"` — toggle `.active` class
- Gesture buttons: `#pinchBtn`, `#rotateBtn` — enter a dedicated gesture mode
- Drag mode buttons: `data-drag="scroll"` / `"drag"` / `"swipe"` / `"paint"` — control how mouse drag is interpreted

## Canvas Gesture Preview

The `<canvas>` element overlays the device screen image.
- Draw gesture arcs/paths on canvas **before** sending to backend
- Clear canvas after the gesture is sent
- Pinch preview: two circles + line between them
- Swipe/scroll/drag preview: arrow path
- Paint preview: free-form polyline path sampled from pointermove points
- **Swipe and scroll gestures are snapped to cardinal directions (0°/90°/180°/270°) in `pointermove` preview and in `onSwipe`/`onScroll` before sending** — use `snapCardinal()` helper
- Drag/Paint modes are free-angle (no snapping)
- **Pinch/rotate mode hover**: yellow element highlight is shown while hovering before the overlay is placed (`!pgst`); also shown while hovering over `pgstSvg` without dragging a dot (`activeDotIdx === null`); cleared on `pointerdown` (placement) and `pointerleave`
- **Pinch `duration`**: recorded from `pointerdown` on a side dot to `pointerup`; sent in the payload as `duration` (ms, min 100); used to derive `velocity` in codegen
- **Paint points**: frontend sends `start_x/start_y`, `duration`, and `points: [{x,y,t}]` to backend; recording stores points relative to the start element as percentages
- **Paint point simplification**: before send, frontend simplifies sampled paint points (RDP + capped sampling) to reduce payload/action size while preserving stroke shape
- **Paint HTTP fallback**: when WebSocket is unavailable and recording is on, frontend sends only `POST /api/record/paint`; backend freezes start-element snapshot, executes paint immediately, then records asynchronously
- **Paint polling pause**: while a paint gesture is being sent/executed, frontend temporarily pauses `/api/status`, warm `/api/tree`, and `/api/unit_test/status` polling to reduce WDA contention

## Adding a New Gesture Button

1. Add button HTML to the correct sidebar section in `index.html`
2. Add a click event listener in `app.js`
3. Call the appropriate `/api/record/<action>` endpoint with the correct payload
4. Add a canvas preview if the gesture has a visual path
5. The backend endpoint must already exist in `app/main.py` — check first

## Step List UI

- Steps are displayed in `#stepList` as `<div class="step-item">`
- Each item shows: action icon + description + timestamp
- DELETE calls `DELETE /api/steps` to clear all steps
- Export calls `POST /api/export` with `{ "case_name": "<name>" }` — **no browser download**; backend writes files to disk and returns `saved_paths`
- On success, `#exportResultModal` opens to show the saved file paths; dismiss with ✕ or clicking backdrop
- The backend appends a timestamp (`_YYYYMMDD_HHMMSS`) to the case name, marker, and function name automatically
- Export creates a **timestamped subfolder** inside `export/` (e.g. `export/MyTest_20260512_143022/`) containing three files: `.py`, `.json`, `.html` (selector quality report); the pytest/tests/ copy is written flat as before

## Verify Tap+Diff Flow

- Verify mode `tap_screenshot_diff` uses two pick phases:
	1. `TARGET` — user picks the screenshot compare region.
	2. `ACTION` — user picks the element to tap.
- After ACTION pick, UI opens a dialog to collect:
	- wait seconds after tap (default `2.0`)
	- expected result (`same` or `different`)
- On confirm, UI sends one payload to `POST /api/record/verify_tap_screenshot_diff` with both selectors and coordinates.

## Verify Wait-Until-Not-Show Flow

- Verify mode `wait_until_not_show` picks the element **while it is still on screen** (progress bar, spinner, toast) — no PROCESS phase, unlike `not_visible`.
- After the pick, `#verifyWaitGoneModal` collects the two independently-counted timeouts:
	- appear timeout in seconds (default `5`) — fails the step if the element never shows up
	- disappear timeout in seconds (default `1200`, i.e. 20 min) — fails the step if it is still shown
- On confirm, the UI **awaits** `POST /api/record/wait_until_not_show` with the pre-resolved selector plus both timeouts, then refreshes the step list. This one verify deliberately bypasses the WebSocket: it drives no gesture, and a `ws.send()` is fire-and-forget — a stale socket would drop the step with no feedback. (The backend still accepts a `wait_until_not_show` WebSocket message for CLI/other clients.)
- The Verify sidebar stays at **3 rows**: `Visible | Not Visible | Wait Not Show`, then `Text Value | Compare with GT | Preview Compare`, then `Play Preview Compare`.

## Client-Side Hit-Test (hover highlight)

`_clientHitTest(dx, dy)` resolves the hovered element synchronously from the cached
`_treeElements` list (post-order, children before parents) so the yellow highlight box
does not need a round-trip. Smallest real-rect area wins.

`HIT_SLOP = 14.0` (device points) and `_hitRect(r)` mirror the same names in
`app/hittest.py`: an element shorter than 14 pt on one axis (1 pt separators, compare
bars, slider tracks) gets its **hit region** grown to 14 pt around its centre, otherwise
it can never be hovered or recorded. A hit that only lands inside the grown region loses
to an exact hit of the same area. The highlight box is always drawn from the **real**
rect, never the grown one. **Keep `HIT_SLOP` in sync with `app/hittest.py`** — if the two
disagree, the box highlights one element while the backend records another.

`setBboxRectAttrs()` grows the drawn outline to `MIN_BBOX_PX = 4` display px on any axis
thinner than that, centred on the real rect. A 1 pt bar scales to well under one pixel,
so without this the element is picked but the user sees no outline at all and assumes the
hit-test failed. The grown outline is purely visual — reported bounds stay untouched.

## CSS Rules

- Use BEM-like naming: `.block`, `.block__element`, `.block--modifier`
- No inline styles in JS — add/remove CSS classes only
- Dark theme variables are in `:root` — use CSS custom properties, not hardcoded colors
- `.active` class controls selected state for all button groups

## Never Do

- Never add `<script src="https://...">` CDN dependencies
- Never use `document.write()`
- Never bypass CORS by changing fetch headers — the backend has CORS enabled for `*`
- Never add a new REST endpoint call without first confirming the endpoint exists in `app/main.py`
