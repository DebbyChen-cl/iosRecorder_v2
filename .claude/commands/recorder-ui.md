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
| **REST** `POST /api/record/*` | All other gestures sent to recording engine |
| **REST** `GET/DELETE /api/steps` | Step list management |
| **REST** `POST /api/export` | Generate and download pytest code |
| **MJPEG** `/api/stream` | Live device screen video |

## Gesture Sidebar

- Finger mode buttons: `data-finger="single"` / `"two"` / `"multi"` — toggle `.active` class
- Gesture buttons: `#pinchBtn`, `#rotateBtn` — enter a dedicated gesture mode
- Drag mode buttons: `data-drag="scroll"` / `"drag"` / `"swipe"` — control how mouse drag is interpreted

## Canvas Gesture Preview

The `<canvas>` element overlays the device screen image.
- Draw gesture arcs/paths on canvas **before** sending to backend
- Clear canvas after the gesture is sent
- Pinch preview: two circles + line between them
- Swipe/drag preview: arrow path

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
- Export calls `POST /api/export` with `{ "case_name": "<name>" }` and triggers a file download

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
