"use strict";

// ── State ──────────────────────────────────────────────────────────────────────
let unitTestMode = false;
let unitTestEntryCount = 0;
let wdaUrl = "http://localhost:8100";
let deviceW = 390, deviceH = 844;
let isConnected = false;
let isRecording = false;
let steps = [];
let _treeElements = []; // cached from last /api/tree fetch
let ws = null;let fingerMode = "single";  // "single" | "two" | "multi"
let gestureMode = "normal"; // "normal" | "pinch" | "rotate"
let dragMode    = "scroll"; // "scroll" | "swipe" | "drag" | "paint"
let pollPauseUntil = 0; // timestamp(ms): pause status/tree polling during heavy gestures
let awaitingScrollTarget = false;
let awaitingSwipeTarget  = false;
let typeTextTarget = { x: 0, y: 0 }; // device coords of last single tap (text target, non-recording fallback)
let awaitingTypeTarget = false;       // true while waiting for user to click the type target element
let typeTextSelectedTarget = null;    // resolved target element { x, y, type, value, bounds, selector_quality }

// Verify state
let verifyMode  = null; // null|"visible"|"not_visible"|"get_text"|"screenshot_gt"|"screenshot_diff"
let verifyPhase = 0;    // 0 = picking target, 1 = process (for not_visible / screenshot_diff)
let verifyTarget = null; // { x, y, type, value, bounds }
let _screenshotDiffCtx = null; // { x, y, bounds } — saved while screenshot_diff PROCESS is active
let _diffExpectedCb    = null; // callback waiting for The Same / Not The Same choice
let _rightDblCtx = { count: 0, timer: null }; // tracks consecutive right-clicks during drag

// Pinch/Rotate overlay state
const PGST_INIT_R           = 70;               // display px — initial finger radius
const PGST_INIT_ANGLE       = Math.PI / 4;      // pinch: 45° diagonal
const PGST_ROTATE_INIT_ANGLE = -Math.PI / 2;    // rotate: vertical (dots top/bottom) = 0°
let pgst = null;           // { cx, cy, r, angle, initAngle }
let activeDotIdx = null;   // null | 0 | 1 — which side dot is being dragged
// ── DOM refs ───────────────────────────────────────────────────────────────────
const urlInput      = document.getElementById("urlInput");
const connectBtn    = document.getElementById("connectBtn");
const dot           = document.getElementById("dot");
const screenWrap    = document.getElementById("screenWrap");
const screenImg     = document.getElementById("screenImg");
const gestureSvg    = document.getElementById("gestureSvg");
const clickLayer    = document.getElementById("clickLayer");
const offlineMsg    = document.getElementById("offlineMsg");
const screenMeta    = document.getElementById("screenMeta");
const recBtn        = document.getElementById("recBtn");
const versionBadge  = document.getElementById("versionBadge");
const clearBtn   = document.getElementById("clearBtn");
const exportBtn      = document.getElementById("exportBtn");
const caseNameInput  = document.getElementById("caseNameInput");
const stepsList  = document.getElementById("stepsList");
const stepCount  = document.getElementById("stepCount");
const fingerBtns = document.querySelectorAll(".finger-btn[data-finger]");
const pinchBtn      = document.getElementById("pinchBtn");
const rotateBtn     = document.getElementById("rotateBtn");
const pgstSvg       = document.getElementById("pgstSvg");
const pgstAutoExit  = document.getElementById("pgstAutoExit");
const dragModeBtns  = document.querySelectorAll(".drag-mode-btn[data-drag]");
const typeBtn           = document.getElementById("typeBtn");
const textInputOverlay  = document.getElementById("textInputOverlay");
const textInputField    = document.getElementById("textInputField");
const textInputHint     = document.getElementById("textInputHint");
const textCancelBtn     = document.getElementById("textCancelBtn");
const textSendBtn       = document.getElementById("textSendBtn");
const homeBtn           = document.getElementById("homeBtn");
const launchAppBtn      = document.getElementById("launchAppBtn");
const terminateAppBtn   = document.getElementById("terminateAppBtn");
const appPickerModal    = document.getElementById("appPickerModal");
const appPickerList     = document.getElementById("appPickerList");
const appPickerClose    = document.getElementById("appPickerClose");
const verifyBtns        = document.querySelectorAll(".verify-btn[data-verify]");
const verifySvg         = document.getElementById("verifySvg");
const verifyPhaseSidebar = document.getElementById("verifyPhaseSidebar");
const verifyContextBadge = document.getElementById("verifyContextBadge");
const verifyPhaseLabel  = document.getElementById("verifyPhaseLabel");
const verifyDoneBtn     = document.getElementById("verifyDoneBtn");
const verifyTextModal       = document.getElementById("verifyTextModal");
const verifyTextExpected    = document.getElementById("verifyTextExpected");
const verifyTextClose       = document.getElementById("verifyTextClose");
const verifyTextCancel      = document.getElementById("verifyTextCancel");
const verifyTextConfirm     = document.getElementById("verifyTextConfirm");
const verifyScreenshotGtModal = document.getElementById("verifyScreenshotGtModal");
const verifyGtNameInput     = document.getElementById("verifyGtNameInput");
const verifyGtClose         = document.getElementById("verifyGtClose");
const verifyGtCancel        = document.getElementById("verifyGtCancel");
const verifyGtConfirm       = document.getElementById("verifyGtConfirm");
const hoverBboxRect         = document.getElementById("hoverBboxRect");
const hoverLoadingMark      = document.getElementById("hoverLoadingMark");
const hoverLoadingH         = document.getElementById("hoverLoadingH");
const hoverLoadingV         = document.getElementById("hoverLoadingV");
const screenLoadingText     = document.getElementById("screenLoadingText");
const unitTestBadge         = document.getElementById("unitTestBadge");
const unitTestPanel         = document.getElementById("unitTestPanel");
const exportUnitTestBtn     = document.getElementById("exportUnitTestBtn");
const unitTestCountEl       = document.getElementById("unitTestCount");
const unitTestResultModal   = document.getElementById("unitTestResultModal");
const unitTestResultClose   = document.getElementById("unitTestResultClose");
const unitTestResultPaths   = document.getElementById("unitTestResultPaths");

if (screenWrap) {
  ["pointerdown", "pointerup", "click", "contextmenu"].forEach(type => {
    screenWrap.addEventListener(type, e => {
      if (!isScreenLoadingActive()) return;
      e.preventDefault();
      e.stopImmediatePropagation();
    }, true);
  });
}

// ── Boot ───────────────────────────────────────────────────────────────────────
window.addEventListener("load", async () => {
  const cfg = await api("GET", "/api/config").catch(() => null);
  if (cfg?.wda_url) { wdaUrl = cfg.wda_url; urlInput.value = wdaUrl; }
  // Show version badge
  const ver = await api("GET", "/api/version").catch(() => null);
  if (ver?.version && versionBadge) versionBadge.textContent = `v${ver.version}`;
  // Unit test capture mode
  const utStatus = await api("GET", "/api/unit_test/status").catch(() => null);
  if (utStatus?.enabled) {
    unitTestMode = true;
    unitTestBadge.style.display = "";
    unitTestPanel.style.display = "";
    unitTestEntryCount = utStatus.entry_count;
    _updateUnitTestCount();
  }
  await checkStatus();
  if (isConnected) refreshElementTree();
  setInterval(() => {
    if (isPollPaused()) return;
    checkStatus();
  }, 2000);
  setInterval(pollSteps, 800);
  if (unitTestMode) {
    setInterval(() => {
      if (isPollPaused()) return;
      pollUnitTestStatus();
    }, 1500);
  }
  // Keep element tree warm for instant hover hit-test
  setInterval(refreshElementTree, 2000);
});

function pausePolling(ms) {
  pollPauseUntil = Math.max(pollPauseUntil, Date.now() + Math.max(0, ms));
}

function isPollPaused() {
  return Date.now() < pollPauseUntil;
}

function rememberScreenPoint(fx, fy) {
  _lastScreenPoint = { fx, fy };
}

async function refreshElementTree(force = false) {
  if (!force && (isPollPaused() || !isConnected)) return;
  const data = await api("GET", force ? "/api/tree?fresh=1" : "/api/tree").catch(() => null);
  if (data?.elements) _treeElements = data.elements;
  return !!data?.elements;
}
// ── Finger mode ─────────────────────────────────────────────────────────
fingerBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    fingerMode = btn.dataset.finger;
    fingerBtns.forEach(b => b.classList.toggle("active", b === btn));
  });
});

// ── Gesture mode (Pinch / Rotate) ───────────────────────────────────────
function enterGestureMode(mode) {
  gestureMode = mode;
  clearPgstOverlay();
  clearTimeout(tapSeq.timer);
  tapSeq = { count: 0, x: 0, y: 0, timer: null };
  pinchBtn.classList.toggle("active",  mode === "pinch");
  rotateBtn.classList.toggle("active", mode === "rotate");
  clickLayer.style.cursor = "cell";
}
function exitGestureMode() {
  gestureMode = "normal";
  clearPgstOverlay();
  pinchBtn.classList.remove("active");
  rotateBtn.classList.remove("active");
  clickLayer.style.cursor = "crosshair";
}
pinchBtn.addEventListener("click",  () => gestureMode === "pinch"  ? exitGestureMode() : enterGestureMode("pinch"));
rotateBtn.addEventListener("click", () => gestureMode === "rotate" ? exitGestureMode() : enterGestureMode("rotate"));

// ── Drag mode ───────────────────────────────────────────────────────
function sendScrollTarget(x, y) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: "update_scroll_target", x, y }));
    return;
  }
  api("POST", "/api/record/scroll_target", { x, y });
}

function sendSwipeTarget(x, y) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: "update_swipe_target", x, y }));
    return;
  }
  api("POST", "/api/record/swipe_target", { x, y });
}

dragModeBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    dragMode = btn.dataset.drag;
    dragModeBtns.forEach(b => b.classList.toggle("active", b === btn));
  });
});

const DRAG_MODE_CYCLE = ["scroll", "drag", "swipe", "paint"];

function cycleDragMode() {
  const idx = DRAG_MODE_CYCLE.indexOf(dragMode);
  dragMode = DRAG_MODE_CYCLE[(idx + 1) % DRAG_MODE_CYCLE.length];
  dragModeBtns.forEach(b => b.classList.toggle("active", b.dataset.drag === dragMode));
  showDragModeToast(dragMode);
}

function showDragModeToast(mode) {
  const label = mode.charAt(0).toUpperCase() + mode.slice(1);
  let toast = document.getElementById("dragModeToast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "dragModeToast";
    Object.assign(toast.style, {
      position: "absolute", top: "50%", left: "50%",
      transform: "translate(-50%, -50%)",
      background: "rgba(0,0,0,0.72)", color: "#fff",
      padding: "7px 20px", borderRadius: "8px",
      fontSize: "15px", fontWeight: "bold",
      pointerEvents: "none", zIndex: "999",
      transition: "opacity 0.3s",
    });
    clickLayer.parentElement.appendChild(toast);
  }
  toast.textContent = "⇄ " + label;
  toast.style.opacity = "1";
  clearTimeout(toast._hideTimer);
  toast._hideTimer = setTimeout(() => { toast.style.opacity = "0"; }, 900);
}

// pgstSvg interaction ———————————————————————————————————————
// All drag events route through pgstSvg (pointer-captured on side circles)
pgstSvg.addEventListener("pointermove", e => {
  // Show hover highlight while hovering over the overlay without dragging a dot
  const rect = pgstSvg.getBoundingClientRect();
  rememberScreenPoint(e.clientX - rect.left, e.clientY - rect.top);
  if (activeDotIdx === null) {
    updateHoverHighlight(e.clientX - rect.left, e.clientY - rect.top);
  }
  if (activeDotIdx === null || !pgst) return;
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;
  const dx = mx - pgst.cx, dy = my - pgst.cy;
  if (gestureMode === "pinch") {
    pgst.r = Math.max(20, Math.hypot(dx, dy));
  } else {
    const newAngle = activeDotIdx === 0
      ? Math.atan2(dy, dx) - Math.PI
      : Math.atan2(dy, dx);
    // Accumulate delta normalised to [-π, π] to avoid atan2 wrap discontinuity.
    // This lets the user drag past ±180° without any 360° jump.
    let delta = newAngle - pgst.lastDragAngle;
    if (delta >  Math.PI) delta -= 2 * Math.PI;
    if (delta < -Math.PI) delta += 2 * Math.PI;
    pgst.totalRotation += delta;
    pgst.lastDragAngle  = newAngle;
    pgst.angle = pgst.initAngle + pgst.totalRotation;
  }
  renderPgstOverlay();
});
pgstSvg.addEventListener("pointerup", () => {
  if (activeDotIdx === null) return;
  activeDotIdx = null;
  executePgst();
});
pgstSvg.addEventListener("pointercancel", () => { activeDotIdx = null; });
pgstSvg.addEventListener("pointerleave", () => { if (activeDotIdx === null) clearHoverHighlight(); });

function clearPgstOverlay() {
  pgstSvg.innerHTML = "";
  pgst = null;
  activeDotIdx = null;
}

function renderPgstOverlay() {
  pgstSvg.innerHTML = "";
  if (!pgst) return;
  const { cx, cy, r, angle } = pgst;
  const ax = cx + r * Math.cos(angle + Math.PI);
  const ay = cy + r * Math.sin(angle + Math.PI);
  const bx = cx + r * Math.cos(angle);
  const by = cy + r * Math.sin(angle);
  const ns = "http://www.w3.org/2000/svg";

  // Connecting line
  const line = document.createElementNS(ns, "line");
  Object.entries({ x1: ax, y1: ay, x2: bx, y2: by,
    stroke: "rgba(255,184,108,0.55)", "stroke-width": "1.5",
    "stroke-dasharray": "5,3", "pointer-events": "none" })
    .forEach(([k, v]) => line.setAttribute(k, v));
  pgstSvg.appendChild(line);

  // Center circle (orange, non-draggable)
  addSvgCircle(cx, cy, 11, "rgba(255,184,108,0.3)", "#ffb86c", 2.5, "pointer-events", "none");

  // Side circle A (blue, draggable) — idx 0
  addSvgSideDot(ax, ay, 0);
  // Side circle B (blue, draggable) — idx 1
  addSvgSideDot(bx, by, 1);

  // Info label — white pill background + large text
  let labelText;
  if (gestureMode === "pinch") {
    const s = r / PGST_INIT_R;
    labelText = `×${s.toFixed(2)}`;
  } else {
    const deg = Math.round((angle - pgst.initAngle) * 180 / Math.PI);
    labelText = `${deg > 0 ? "+" : ""}${deg}°`;
  }

  // Measure approximate text width (monospace ~9px/char at font-size 15)
  const charW = 9, padX = 8, padY = 5, fSize = 15;
  const tw = labelText.length * charW;
  const rx = cx + 14, ry = cy - 30;

  const bg = document.createElementNS(ns, "rect");
  Object.entries({
    x: rx - padX, y: ry - fSize - padY + 2,
    width: tw + padX * 2, height: fSize + padY * 2,
    rx: 5, ry: 5,
    fill: "rgba(255,255,255,0.92)", "pointer-events": "none"
  }).forEach(([k, v]) => bg.setAttribute(k, v));
  pgstSvg.appendChild(bg);

  const text = document.createElementNS(ns, "text");
  text.setAttribute("x", rx); text.setAttribute("y", ry);
  text.setAttribute("fill", "#1a1a1a"); text.setAttribute("font-size", fSize);
  text.setAttribute("font-family", "monospace"); text.setAttribute("font-weight", "700");
  text.setAttribute("pointer-events", "none");
  text.textContent = labelText;
  pgstSvg.appendChild(text);
}

function addSvgCircle(cx, cy, r, fill, stroke, sw, ...extraAttrs) {
  const ns = "http://www.w3.org/2000/svg";
  const c = document.createElementNS(ns, "circle");
  Object.entries({ cx, cy, r, fill, stroke, "stroke-width": sw })
    .forEach(([k, v]) => c.setAttribute(k, v));
  for (let i = 0; i < extraAttrs.length; i += 2) c.setAttribute(extraAttrs[i], extraAttrs[i + 1]);
  pgstSvg.appendChild(c);
  return c;
}

function addSvgSideDot(cx, cy, idx) {
  const ns = "http://www.w3.org/2000/svg";
  const c = document.createElementNS(ns, "circle");
  Object.entries({ cx, cy, r: 8, fill: "rgba(74,158,255,0.55)", stroke: "#4a9eff",
    "stroke-width": 2, "pointer-events": "all", cursor: "grab" })
    .forEach(([k, v]) => c.setAttribute(k, v));
  c.addEventListener("pointerdown", e => {
    e.stopPropagation();
    e.preventDefault();
    activeDotIdx = idx;
    pgst.dragStartTime = Date.now();
    // Seed the accumulator with the angle at drag-start using the same formula
    // as pointermove, so the first delta is always 0 (no jump on grab).
    pgst.lastDragAngle = pgst.angle;
    pgstSvg.setPointerCapture(e.pointerId);
  });
  pgstSvg.appendChild(c);
}

function executePgst() {
  if (!pgst) return;
  const rect = clickLayer.getBoundingClientRect();
  const scaleX = deviceW / rect.width;
  const center = toDevice(pgst.cx, pgst.cy);
  if (gestureMode === "pinch") {
    const scale    = parseFloat((pgst.r / PGST_INIT_R).toFixed(3));
    const spread   = Math.round(PGST_INIT_R * scaleX);
    const duration = pgst.dragStartTime ? Math.max(100, Date.now() - pgst.dragStartTime) : 500;
    sendGesture("pinch", { x: center.x, y: center.y, scale, spread, duration });
  } else {
    const rotation = parseFloat(((pgst.angle - pgst.initAngle) * 180 / Math.PI).toFixed(1));
    const spread   = Math.round(pgst.r * scaleX);
    const duration = pgst.dragStartTime ? Math.max(100, Date.now() - pgst.dragStartTime) : 600;
    sendGesture("rotate", { x: center.x, y: center.y, rotation, spread, duration });
  }
  // Reset back to initial position
  pgst.r             = PGST_INIT_R;
  pgst.angle         = pgst.initAngle;
  pgst.totalRotation = 0;
  pgst.lastDragAngle = null;
  if (pgstAutoExit.checked) {
    exitGestureMode();
  } else {
    renderPgstOverlay();
  }
}
// ── Steps info popup ───────────────────────────────────────────────────────────
const stepsInfoBtn   = document.getElementById("stepsInfoBtn");
const stepsInfoPopup = document.getElementById("stepsInfoPopup");
stepsInfoBtn.addEventListener("click", e => {
  e.stopPropagation();
  const visible = stepsInfoPopup.style.display !== "none";
  stepsInfoPopup.style.display = visible ? "none" : "block";
});
document.addEventListener("click", () => { stepsInfoPopup.style.display = "none"; });

// ── Connection ─────────────────────────────────────────────────────────────────
connectBtn.addEventListener("click", doConnect);
urlInput.addEventListener("keydown", e => { if (e.key === "Enter") doConnect(); });

async function doConnect() {
  const url = urlInput.value.trim();
  if (!url) return;
  setDot("connecting");
  const ok = await api("POST", "/api/config", { wda_url: url }).catch(() => null);
  if (!ok) { setDot(""); return; }
  wdaUrl = url;
  connectWS();
  await checkStatus();
}

async function checkStatus() {
  const data = await api("GET", "/api/status").catch(() => null);
  if (data?.connected) {
    isConnected = true;
    setDot("connected");
    offlineMsg.style.display = "none";
    if (data.screen_size?.width) {
      const { width, height } = data.screen_size;
      if (width !== deviceW || height !== deviceH) {
        deviceW = width; deviceH = height;
        screenMeta.textContent = `${deviceW} × ${deviceH} pts`;
      }
    }
    if (data.mjpeg_url && screenImg.dataset.mjpeg !== data.mjpeg_url) {
      screenImg.dataset.mjpeg = data.mjpeg_url;
      loadStream(data.mjpeg_url);
    }
  } else {
    isConnected = false;
    if (!isScreenLoadingActive()) setScreenLoading(false);
    setDot("");
  }
  return !!data?.connected;
}

function setDot(state) { dot.className = "dot" + (state ? " " + state : ""); }

function loadStream(mjpegUrl) {
  // Always route through the server-side proxy (/api/stream) so the browser
  // never needs a direct connection to the device IP/port.
  screenImg.onerror = null;
  screenImg.src = `/api/stream?t=${Date.now()}`;
  screenImg.onerror = () => {
    setTimeout(() => loadStream(mjpegUrl), 1500);
  };
}

// ── WebSocket ──────────────────────────────────────────────────────────────────
function connectWS() {
  if (ws) { try { ws.close(); } catch (_) {} ws = null; }
  const proto = location.protocol === "https:" ? "wss" : "ws";
  ws = new WebSocket(`${proto}://${location.host}/ws/tap`);
  ws.onclose = ws.onerror = () => { ws = null; };
}

// ── Coordinate helpers ─────────────────────────────────────────────────────────
function toDevice(displayX, displayY) {
  const r = clickLayer.getBoundingClientRect();
  return {
    x: Math.round((displayX / r.width)  * deviceW),
    y: Math.round((displayY / r.height) * deviceH),
  };
}

function deviceToDisplay(deviceX, deviceY) {
  const r = clickLayer.getBoundingClientRect();
  return {
    x: deviceW ? (Number(deviceX) / deviceW) * r.width : 0,
    y: deviceH ? (Number(deviceY) / deviceH) * r.height : 0,
  };
}

// ── Gesture detection ──────────────────────────────────────────────────────────
const MOVE_THRESHOLD = 10;   // px display — below = tap
const LONG_PRESS_MS  = 500;  // ms hold without move → long press
const LONG_PRESS_DRAG_MS = 1000; // ms hold before moving → long press drag
const DBL_TAP_MS     = 400;  // ms window to accumulate taps
const DBL_TAP_DIST   = 30;   // px display
const PAINT_MIN_DIST  = 4.0; // px display — ignore jitter between paint samples
const PAINT_MIN_GAP   = 28;  // ms between paint samples
const PAINT_KEEP_TURN_DEG = 16; // keep points on meaningful direction changes
const PAINT_MAX_POINTS = 600;
const PAINT_TARGET_SEND_POINTS = 48; // final payload target for recording/replay

let gst = null;   // active gesture state
let tapSeq = { count: 0, x: 0, y: 0, timer: null };

clickLayer.addEventListener("pointerdown", e => {
  e.preventDefault();
  rememberScreenPoint(e.offsetX, e.offsetY);
  if (isScreenLoadingActive()) {
    e.stopPropagation();
    return;
  }
  clearHoverHighlight();

  if (e.button !== 0) return; // ignore right-click / middle-click

  // In pinch/rotate mode: click places the three-dot overlay
  if (gestureMode !== "normal") {
    const initAngle = gestureMode === "rotate" ? PGST_ROTATE_INIT_ANGLE : PGST_INIT_ANGLE;
    pgst = { cx: e.offsetX, cy: e.offsetY, r: PGST_INIT_R, angle: initAngle, initAngle,
             totalRotation: 0, lastDragAngle: null };
    renderPgstOverlay();
    return;
  }

  clickLayer.setPointerCapture(e.pointerId);

  gst = {
    sx: e.offsetX, sy: e.offsetY,
    t0: Date.now(),
    moved: false,
    longPressed: false,
    moveStartTime: null,
    points: [{ x: e.offsetX, y: e.offsetY, t: 0 }],
    lastPointTs: Date.now(),
    prevVecX: null,
    prevVecY: null,
    longTimer: setTimeout(() => {
      if (gst && !gst.moved) {
        gst.longPressed = true;
        if (dragMode === "drag") showLongRing(gst.sx, gst.sy);
      }
    }, dragMode === "drag" ? LONG_PRESS_DRAG_MS : LONG_PRESS_MS),
  };
});

clickLayer.addEventListener("pointermove", e => {
  rememberScreenPoint(e.offsetX, e.offsetY);
  if (isScreenLoadingActive() && !gst) return;
  // Hover element highlight: synchronous hit-test, rAF-batched DOM write
  if (!gst && gestureMode === "normal") {
    updateHoverHighlight(e.offsetX, e.offsetY);
  }
  // In pinch/rotate mode, show hover highlight before the overlay is placed
  if (gestureMode !== "normal" && !pgst) {
    updateHoverHighlight(e.offsetX, e.offsetY);
  }

  // Live hover bbox for screenshot verify modes (phase 0 = picking target)
  if ((verifyMode === "screenshot_gt" || verifyMode === "screenshot_diff") && verifyPhase === 0) {
    hoverVerifyBbox(e.offsetX, e.offsetY);
  }

  if (!gst) return;
  const dx = e.offsetX - gst.sx, dy = e.offsetY - gst.sy;
  if (!gst.moved && Math.hypot(dx, dy) > MOVE_THRESHOLD) {
    gst.moved = true;
    gst.moveStartTime = Date.now();
    clearTimeout(gst.longTimer);
    clearGestureOverlay();
  }
  if (gst.moved) {
    if (dragMode === "paint") {
      maybeAddPaintPoint(gst, e.offsetX, e.offsetY);
      drawPaintPreview(gst.points, e.offsetX, e.offsetY);
    } else {
      const snapped = (dragMode === "scroll" || dragMode === "swipe")
        ? snapCardinal(gst.sx, gst.sy, e.offsetX, e.offsetY)
        : { ex: e.offsetX, ey: e.offsetY };
      const previewMode = (dragMode === "drag" && gst.longPressed) ? "long_press_drag" : dragMode;
      drawSwipePreview(gst.sx, gst.sy, snapped.ex, snapped.ey, previewMode);
    }
  }
});

clickLayer.addEventListener("pointerup", e => {
  rememberScreenPoint(e.offsetX, e.offsetY);
  if (!gst) return;
  if (e.button !== 0) return; // ignore right-click release
  clearTimeout(gst.longTimer);
  clearGestureOverlay();

  const ex = e.offsetX, ey = e.offsetY;
  const elapsed = Date.now() - gst.t0;
  const { sx, sy, moved, longPressed, moveStartTime, points, t0 } = gst;
  gst = null;

  if (!moved) {
    if (longPressed || elapsed >= LONG_PRESS_MS) {
      onLongPress(sx, sy);
    } else {
      onTap(sx, sy);
    }
  } else {
    // Any drag motion uses the current dragMode
    const dur = Math.min(Math.max(elapsed, 200), 1500);
    if (dragMode === "scroll")     onScroll(sx, sy, ex, ey, dur);
    else if (dragMode === "drag")  onDrag(sx, sy, ex, ey, longPressed, elapsed, moveStartTime ? moveStartTime - t0 : elapsed);
    else if (dragMode === "swipe") onSwipe(sx, sy, ex, ey, dur);
    else                            onPaint(sx, sy, ex, ey, elapsed, points, t0);
  }
});

clickLayer.addEventListener("contextmenu", e => {
  e.preventDefault(); // always suppress browser context menu

  if (!gst || !gst.moved) return; // only act during an active drag

  _rightDblCtx.count++;
  if (_rightDblCtx.count === 1) {
    // Start timer — if no second right-click arrives, do nothing
    _rightDblCtx.timer = setTimeout(() => {
      _rightDblCtx = { count: 0, timer: null };
    }, 350);
  } else {
    // Second right-click within 350 ms → cycle drag mode
    clearTimeout(_rightDblCtx.timer);
    _rightDblCtx = { count: 0, timer: null };
    cycleDragMode();
  }
});

clickLayer.addEventListener("pointercancel", () => {
  if (gst) { clearTimeout(gst.longTimer); clearGestureOverlay(); gst = null; }
});

// Escape cancels an in-progress drag/scroll/swipe
document.addEventListener("keydown", e => {
  if (e.key === "Escape" && gst) {
    clearTimeout(gst.longTimer);
    clearGestureOverlay();
    gst = null;
  }
});

// ── Gesture handlers ───────────────────────────────────────────────────────────
function onTap(dx, dy) {
  clearTimeout(tapSeq.timer);
  tapSeq.timer = null;

  const sameSite = tapSeq.count > 0 &&
    Math.hypot(dx - tapSeq.x, dy - tapSeq.y) < DBL_TAP_DIST;

  if (sameSite) {
    tapSeq.count = Math.min(tapSeq.count + 1, 5);
  } else {
    // New location — start fresh (discard any unfinished streak from elsewhere)
    tapSeq.count = 1;
    tapSeq.x = dx;
    tapSeq.y = dy;
  }

  // Always defer: wait for DBL_TAP_MS silence before dispatching
  const cnt = tapSeq.count, fx = tapSeq.x, fy = tapSeq.y;
  tapSeq.timer = setTimeout(() => {
    tapSeq = { count: 0, x: 0, y: 0, timer: null };
    dispatchTap(cnt, fx, fy);
  }, DBL_TAP_MS);
}

function dispatchTap(cnt, fx, fy) {
  // ── Verify mode intercept (phase 0: select target, no tap sent) ───────────
  if (verifyMode !== null && verifyPhase === 0) {
    handleVerifyTargetPick(fx, fy);
    return;
  }

  // ── Type target pick intercept (pick phase: no tap sent to device) ──────────
  if (awaitingTypeTarget) {
    handleTypeTargetPick(fx, fy);
    return;
  }

  // Enrich last scroll step with this tap's element as the scroll target
  if (awaitingScrollTarget) {
    awaitingScrollTarget = false;
    if (isRecording) {
      const { x, y } = toDevice(fx, fy);
      sendScrollTarget(x, y);
    }
  }
  // Enrich last swipe step with this tap's element as the swipe_until target
  if (awaitingSwipeTarget) {
    awaitingSwipeTarget = false;
    if (isRecording) {
      const { x, y } = toDevice(fx, fy);
      sendSwipeTarget(x, y);
    }
  }

  const coords = toDevice(fx, fy);

  // Track last single-tap position for "Type" overlay
  if (fingerMode === "single" && cnt === 1) typeTextTarget = coords;

  if (fingerMode === "two") {
    showRipple(fx - 16, fy); showRipple(fx + 16, fy);
    sendGesture("two_finger_tap", coords);
    return;
  }
  if (fingerMode === "multi") {
    showRipple(fx - 24, fy); showRipple(fx, fy); showRipple(fx + 24, fy);
    sendGesture("multi_finger_tap", { ...coords, fingers: 3 });
    return;
  }

  // single-finger mode — respect tap count
  if (cnt >= 5) {
    showRipple(fx, fy); showRipple(fx, fy); showRipple(fx, fy); showRipple(fx, fy); showRipple(fx, fy);
    sendGesture("five_tap", coords);
  } else if (cnt >= 3) {
    showRipple(fx, fy); showRipple(fx, fy); showRipple(fx, fy);
    sendGesture("triple_tap", coords);
  } else if (cnt >= 2) {
    showRipple(fx, fy); showRipple(fx, fy);
    sendGesture("double_tap", coords);
  } else {
    showRipple(fx, fy);
    sendGesture("tap", coords);
  }
}

function onLongPress(dx, dy) {
  // Cancel any pending tap sequence so it doesn't fire after long press
  clearTimeout(tapSeq.timer);
  tapSeq = { count: 0, x: 0, y: 0, timer: null };
  showRipple(dx, dy);
  sendGesture("long_press", { ...toDevice(dx, dy), duration: 1000 });
}

function snapCardinal(sx, sy, ex, ey) {
  const dx = ex - sx, dy = ey - sy;
  if (Math.abs(dx) >= Math.abs(dy)) {
    return { ex, ey: sy };  // horizontal — lock Y
  } else {
    return { ex: sx, ey };  // vertical — lock X
  }
}

function onSwipe(sx, sy, ex, ey, elapsed) {
  const snapped = snapCardinal(sx, sy, ex, ey);
  ex = snapped.ex; ey = snapped.ey;
  showGestureTrail(sx, sy, ex, ey);
  const duration = Math.min(Math.max(elapsed, 200), 1500);
  const s = toDevice(sx, sy), e2 = toDevice(ex, ey);
  const dx = ex - sx, dy = ey - sy;
  const dir = Math.abs(dx) >= Math.abs(dy) ? (dx > 0 ? "right" : "left") : (dy > 0 ? "down" : "up");
  sendGesture("swipe", { x1: s.x, y1: s.y, x2: e2.x, y2: e2.y, duration, direction: dir });
  if (isRecording) awaitingSwipeTarget = true;
}

function onScroll(sx, sy, ex, ey, elapsed) {
  const snapped = snapCardinal(sx, sy, ex, ey);
  ex = snapped.ex; ey = snapped.ey;
  showGestureTrail(sx, sy, ex, ey);
  const duration = Math.min(Math.max(elapsed, 300), 1500);
  const s = toDevice(sx, sy), e2 = toDevice(ex, ey);
  sendGesture("scroll", { x1: s.x, y1: s.y, x2: e2.x, y2: e2.y, duration });
  if (isRecording) awaitingScrollTarget = true;
}

function onDrag(sx, sy, ex, ey, longPressed = false, elapsed = 1000, pressDuration = 0) {
  const actionType = longPressed ? "long_press_drag" : "drag";
  showGestureTrail(sx, sy, ex, ey, actionType);
  const s = toDevice(sx, sy), e2 = toDevice(ex, ey);
  if (longPressed) {
    const holdMs = Math.min(Math.max(pressDuration, LONG_PRESS_DRAG_MS), 3000);
    const moveMs = Math.min(Math.max(elapsed - holdMs, 200), 1500);
    sendGesture("long_press_drag", {
      x1: s.x, y1: s.y, x2: e2.x, y2: e2.y,
      duration: moveMs,
      press_duration: holdMs,
    });
  } else {
    sendGesture("drag", { x1: s.x, y1: s.y, x2: e2.x, y2: e2.y, duration: 1000 });
  }
}

function simplifyPaintPointsForSend(points, maxPoints = PAINT_TARGET_SEND_POINTS) {
  if (!Array.isArray(points) || points.length <= maxPoints) return points.slice();

  function perpDist(p, a, b) {
    const dx = b.x - a.x;
    const dy = b.y - a.y;
    if (dx === 0 && dy === 0) return Math.hypot(p.x - a.x, p.y - a.y);
    const t = ((p.x - a.x) * dx + (p.y - a.y) * dy) / (dx * dx + dy * dy);
    const px = a.x + t * dx;
    const py = a.y + t * dy;
    return Math.hypot(p.x - px, p.y - py);
  }

  function rdp(pts, eps) {
    if (pts.length < 3) return pts;
    let maxD = -1;
    let idx = -1;
    for (let i = 1; i < pts.length - 1; i++) {
      const d = perpDist(pts[i], pts[0], pts[pts.length - 1]);
      if (d > maxD) {
        maxD = d;
        idx = i;
      }
    }
    if (maxD > eps && idx > 0) {
      const left = rdp(pts.slice(0, idx + 1), eps);
      const right = rdp(pts.slice(idx), eps);
      return left.slice(0, -1).concat(right);
    }
    return [pts[0], pts[pts.length - 1]];
  }

  let eps = 1.0;
  let simplified = points;
  for (let i = 0; i < 8; i++) {
    const cand = rdp(points, eps);
    simplified = cand;
    if (cand.length <= maxPoints) break;
    eps *= 1.6;
  }

  if (simplified.length > maxPoints) {
    const stride = Math.max(1, Math.ceil((simplified.length - 1) / (maxPoints - 1)));
    const sampled = [];
    for (let i = 0; i < simplified.length; i += stride) sampled.push(simplified[i]);
    if (sampled[sampled.length - 1] !== simplified[simplified.length - 1]) {
      sampled.push(simplified[simplified.length - 1]);
    }
    simplified = sampled;
  }

  return simplified;
}

function onPaint(sx, sy, ex, ey, elapsed, points, t0) {
  const duration = Math.min(Math.max(elapsed, 200), 5000);
  // Reduce WDA contention while paint executes.
  pausePolling(Math.max(6000, duration + 3000));
  const sampled = Array.isArray(points) && points.length ? points.slice() : [{ x: sx, y: sy, t: 0 }];
  const endT = Math.max(0, Date.now() - t0);
  const last = sampled[sampled.length - 1];
  if (!last || Math.hypot(last.x - ex, last.y - ey) >= 1.0) {
    sampled.push({ x: ex, y: ey, t: endT });
  }
  const simplified = simplifyPaintPointsForSend(sampled, PAINT_TARGET_SEND_POINTS);
  const compact = simplified.slice(0, PAINT_MAX_POINTS).map((pt) => {
    const p = toDevice(pt.x, pt.y);
    return { x: p.x, y: p.y, t: Math.max(0, Math.round(pt.t || 0)) };
  });
  drawPaintPreview(sampled, ex, ey);
  showGestureTrail(sx, sy, ex, ey);
  sendGesture("paint", {
    start_x: compact[0]?.x ?? toDevice(sx, sy).x,
    start_y: compact[0]?.y ?? toDevice(sx, sy).y,
    points: compact,
    duration,
  });
}

function maybeAddPaintPoint(state, x, y) {
  if (!state || !Array.isArray(state.points) || state.points.length >= PAINT_MAX_POINTS) return;
  const now = Date.now();
  const last = state.points[state.points.length - 1];
  const vx = x - last.x;
  const vy = y - last.y;
  const dist = Math.hypot(vx, vy);
  const dt = now - state.lastPointTs;

  let keepForTurn = false;
  if (state.prevVecX !== null && state.prevVecY !== null) {
    const prevMag = Math.hypot(state.prevVecX, state.prevVecY);
    const currMag = Math.hypot(vx, vy);
    if (prevMag > 0.01 && currMag > 0.01) {
      const cos = Math.max(-1, Math.min(1, (state.prevVecX * vx + state.prevVecY * vy) / (prevMag * currMag)));
      const turnDeg = Math.acos(cos) * 180 / Math.PI;
      keepForTurn = turnDeg >= PAINT_KEEP_TURN_DEG;
    }
  }

  if (!keepForTurn && dist < PAINT_MIN_DIST && dt < PAINT_MIN_GAP) return;
  state.points.push({ x, y, t: now - state.t0 });
  state.lastPointTs = now;
  state.prevVecX = vx;
  state.prevVecY = vy;
}

// ── Send gesture ───────────────────────────────────────────────────────────────
function sendGesture(type, data) {
  const record = isRecording;

  // HTTP fallback.
  const execEp = { tap: "/api/tap", double_tap: "/api/double_tap", triple_tap: "/api/triple_tap", five_tap: "/api/five_tap", long_press: "/api/long_press", two_finger_tap: "/api/two_finger_tap", multi_finger_tap: "/api/multi_finger_tap", pinch: "/api/pinch", rotate: "/api/rotate", scroll: "/api/scroll", swipe: "/api/swipe", drag: "/api/drag", long_press_drag: "/api/long_press_drag", paint: "/api/paint" };
  const recEp  = { tap: "/api/record", double_tap: "/api/record/double_tap", triple_tap: "/api/record/triple_tap", five_tap: "/api/record/five_tap", long_press: "/api/record/long_press", two_finger_tap: "/api/record/two_finger_tap", multi_finger_tap: "/api/record/multi_finger_tap", pinch: "/api/record/pinch", rotate: "/api/record/rotate", scroll: "/api/record/scroll", swipe: "/api/record/swipe", drag: "/api/record/drag", long_press_drag: "/api/record/long_press_drag", paint: "/api/record/paint" };

  trackActionLoading(type, data, () => {
    if (record) {
      showSentCoordsOverlay(type, data);
      return api("POST", recEp[type], data);
    }
    return api("POST", execEp[type], data);
  });
}

// ── Type Text overlay ─────────────────────────────────────────────────────────
function openTypeOverlay() {
  textInputField.value = "";
  const t = typeTextSelectedTarget;
  if (t && t.type !== "coordinate") {
    textInputHint.textContent = `value to element: ${t.value}`;
  } else {
    textInputHint.textContent = "Press Enter or click outside to send";
  }
  textInputOverlay.style.display = "flex";
  textInputField.focus();
}

function closeTypeOverlay() {
  textInputOverlay.style.display = "none";
  textInputField.value = "";
  typeTextSelectedTarget = null;
  awaitingTypeTarget = false;
  typeBtn.classList.remove("active");
  clearVerifyBbox();
}

function submitTypeText() {
  const text = textInputField.value.trim();
  closeTypeOverlay();
  if (!text) return;
  sendTypeText(text, typeTextTarget.x, typeTextTarget.y);
}

function sendTypeText(text, tx, ty) {
  const record = isRecording;
  const t = typeTextSelectedTarget;
  const data = {
    text,
    target_x: t?.x ?? tx,
    target_y: t?.y ?? ty,
    ...(t && t.type !== "coordinate" ? {
      target_type: t.type,
      target_value: t.value,
      target_bounds: t.bounds ?? null,
      target_selector_quality: t.selector_quality ?? null,
    } : {}),
  };
  trackActionLoading("type_text", data, () => {
    if (record) return api("POST", "/api/record/type_text", data);
    return api("POST", "/api/type_text", { text });
  });
}

typeBtn.addEventListener("click", () => {
  if (isRecording) {
    if (awaitingTypeTarget) {
      // Toggle off — cancel target picking
      awaitingTypeTarget = false;
      typeTextSelectedTarget = null;
      typeBtn.classList.remove("active");
      hideVerifyPhaseLabel();
      clearVerifyBbox();
      return;
    }
    awaitingTypeTarget = true;
    typeTextSelectedTarget = null;
    typeBtn.classList.add("active");
    verifyPhaseLabel.innerHTML = '<span class="vpl-mode">⌨️ TYPE</span><span class="vpl-phase">TARGET</span>';
    verifyPhaseSidebar.style.display = "flex";
    verifyDoneBtn.style.display = "none";
    verifyContextBadge.style.display = "none";
  } else {
    openTypeOverlay();
  }
});
textCancelBtn.addEventListener("click", () => closeTypeOverlay());
textSendBtn.addEventListener("click", () => submitTypeText());
textInputField.addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); submitTypeText(); }
  if (e.key === "Escape") closeTypeOverlay();
});
textInputOverlay.addEventListener("click", e => {
  if (e.target === textInputOverlay) closeTypeOverlay();
});

// ── Home button ───────────────────────────────────────────────────────────────
homeBtn.addEventListener("click", () => {
  const record = isRecording;
  trackActionLoading("home", {}, () => {
    if (record) return api("POST", "/api/record/home");
    return api("POST", "/api/home");
  });
});

// ── App Picker ────────────────────────────────────────────────────────────────
let _appList = [];

async function openAppPicker(onSelect = sendLaunchApp) {
  if (!_appList.length) {
    _appList = await api("GET", "/api/apps").catch(() => []);
  }
  if (!_appList.length) {
    appPickerList.innerHTML = '<div class="modal-empty">No apps configured.<br>Edit <code>apps.json</code> to add entries.</div>';
  } else {
    appPickerList.innerHTML = _appList.map((a, i) => `
      <div class="modal-app-item" data-idx="${i}">
        <div>
          <div class="modal-app-name">${esc(a.name)}</div>
          <div class="modal-app-bundle">${esc(a.bundle_id)}</div>
        </div>
      </div>`).join("");
    appPickerList.querySelectorAll(".modal-app-item").forEach(el => {
      el.addEventListener("click", () => {
        const app = _appList[+el.dataset.idx];
        closeAppPicker();
        onSelect(app.bundle_id);
      });
    });
  }
  appPickerModal.style.display = "flex";
}

function closeAppPicker() {
  appPickerModal.style.display = "none";
}

function sendLaunchApp(bundleId) {
  const record = isRecording;
  trackActionLoading("launch_app", { bundle_id: bundleId }, () => {
    if (record) return api("POST", "/api/record/launch_app", { bundle_id: bundleId });
    return api("POST", "/api/launch_app", { bundle_id: bundleId });
  });
}

function sendTerminateApp(bundleId) {
  const record = isRecording;
  trackActionLoading("terminate_app", { bundle_id: bundleId }, () => {
    if (record) return api("POST", "/api/record/terminate_app", { bundle_id: bundleId });
    return api("POST", "/api/terminate_app", { bundle_id: bundleId });
  });
}

launchAppBtn.addEventListener("click", () => openAppPicker());
terminateAppBtn.addEventListener("click", () => openAppPicker(sendTerminateApp));
appPickerClose.addEventListener("click", () => closeAppPicker());
appPickerModal.addEventListener("click", e => {
  if (e.target === appPickerModal) closeAppPicker();
});

// ── Verify mode ───────────────────────────────────────────────────────────────
verifyBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    const mode = btn.dataset.verify;
    if (verifyMode === mode) {
      // toggle off
      exitVerifyMode();
    } else {
      enterVerifyMode(mode);
    }
  });
});

function enterVerifyMode(mode) {
  if (_screenshotDiffCtx !== null) {
    // Sub-verify during screenshot_diff PROCESS — switch mode without clearing context
    verifyMode  = mode;
    verifyPhase = 0;
    verifyTarget = null;
    verifyBtns.forEach(b => b.classList.toggle("active", b.dataset.verify === mode));
    showVerifyPhaseLabel("TARGET"); // will show context badge automatically
    return;
  }
  exitVerifyMode();
  verifyMode  = mode;
  verifyPhase = 0;
  verifyTarget = null;
  verifyBtns.forEach(b => b.classList.toggle("active", b.dataset.verify === mode));
  showVerifyPhaseLabel("TARGET");
}

function exitVerifyMode() {
  verifyMode  = null;
  verifyPhase = 0;
  verifyTarget = null;
  verifyBtns.forEach(b => b.classList.remove("active"));
  if (_screenshotDiffCtx !== null) {
    // Restore PROCESS state for ongoing screenshot_diff
    showVerifyPhaseLabel("PROCESS", "screenshot_diff");
    showVerifyDoneBtn("screenshot_diff");
    clearVerifyBbox();
    _hoverBboxLast = null;
    return;
  }
  hideVerifyPhaseLabel();
  hideVerifyDoneBtn();
  clearVerifyBbox();
  clearTimeout(_hoverBboxTimer);
  _hoverBboxLast = null;
}

const MODE_LABELS = {
  visible:          "👁 VISIBLE",
  not_visible:      "🚫 NOT VISIBLE",
  get_text:         "📝 TEXT",
  screenshot_gt:    "📸 SCR GT",
  screenshot_diff:  "🔀 SCR DIFF",
};

function showVerifyPhaseLabel(phase, mode) {
  const m = mode ?? verifyMode;
  const modeLabel = MODE_LABELS[m] || "";
  verifyPhaseLabel.innerHTML = modeLabel
    ? `<span class="vpl-mode">${modeLabel}</span><span class="vpl-phase">${phase}</span>`
    : `<span class="vpl-phase">${phase}</span>`;
  verifyPhaseSidebar.style.display = "flex";
  verifyDoneBtn.style.display = "none";
  // Show outer context badge if screenshot_diff PROCESS is running in background
  if (_screenshotDiffCtx !== null && m !== "screenshot_diff") {
    verifyContextBadge.textContent = "🔀 SCR DIFF · PROCESS";
    verifyContextBadge.style.display = "block";
  } else {
    verifyContextBadge.style.display = "none";
  }
}

function hideVerifyPhaseLabel() {
  verifyPhaseSidebar.style.display = "none";
  verifyContextBadge.style.display = "none";
}

function showVerifyDoneBtn(mode) {
  const m = mode ?? verifyMode;
  const modeLabel = MODE_LABELS[m] || "";
  verifyPhaseLabel.innerHTML = modeLabel
    ? `<span class="vpl-mode">${modeLabel}</span><span class="vpl-phase">PROCESS</span>`
    : `<span class="vpl-phase">PROCESS</span>`;
  verifyPhaseSidebar.style.display = "flex";
  verifyDoneBtn.style.display = "block";
  verifyContextBadge.style.display = "none";
}

function hideVerifyDoneBtn() {
  verifyDoneBtn.style.display = "none";
}

function drawVerifyBbox(bounds) {
  // bounds in device coords → convert to display %
  clearVerifyBbox();
  if (!bounds) return;
  const rect = clickLayer.getBoundingClientRect();
  const scaleX = rect.width  / deviceW;
  const scaleY = rect.height / deviceH;
  const ns = "http://www.w3.org/2000/svg";
  const r = document.createElementNS(ns, "rect");
  r.setAttribute("id", "verifyBboxRect");
  r.setAttribute("x",      bounds.x * scaleX);
  r.setAttribute("y",      bounds.y * scaleY);
  r.setAttribute("width",  bounds.w * scaleX);
  r.setAttribute("height", bounds.h * scaleY);
  r.setAttribute("fill",   "rgba(255,200,0,0.12)");
  r.setAttribute("stroke", "#ffc800");
  r.setAttribute("stroke-width", "2");
  r.setAttribute("rx", "4");
  r.setAttribute("pointer-events", "none");
  verifySvg.appendChild(r);
}

function clearVerifyBbox() {
  const existing = document.getElementById("verifyBboxRect");
  if (existing) existing.remove();
}

// ── Hover element highlight ──────────────────────────────────────────────────
// Uses backend /api/element_info (same hit_test logic as recording) so the
// highlighted element always matches what will actually be recorded.
// While the hierarchy cache is warming up after a page navigation
// (cache_ready=false), a pulsing crosshair is shown immediately at the cursor
// position and the fetch is retried every 250 ms until the cache is ready.
let _hoverLastKey    = null;
let _hoverRafId      = null;
let _hoverTimer      = null;
let _hoverRetryTimer = null;
let _hoverCoord      = null;
let _screenLoadingActive = false;
let _actionFlowSeq = 0;
let _lastScreenPoint = null;

function isScreenLoadingActive() {
  return _screenLoadingActive;
}

function setScreenLoading(active, text = "Getting APP Information") {
  _screenLoadingActive = active;
  if (!screenWrap) return;
  screenWrap.classList.toggle("is-screen-loading", active);
  screenWrap.setAttribute("aria-busy", active ? "true" : "false");
  if (active && screenLoadingText) screenLoadingText.textContent = text;
}

function beginActionLoading() {
  const flow = { id: ++_actionFlowSeq, startedAt: Date.now() };
  clearVisibleBbox();
  setScreenLoading(true, "Sending Action");
  return flow;
}

function completeActionSend(flow, type, data) {
  if (!flow || flow.id !== _actionFlowSeq) return;
  setTimeout(() => startAppInfoRefresh(flow), getActionVisualSettleMs(type, data));
}

async function startAppInfoRefresh(flow) {
  if (!flow || flow.id !== _actionFlowSeq) {
    if (flow?.id === _actionFlowSeq) setScreenLoading(false);
    return;
  }

  setScreenLoading(true, "Getting APP Information");
  const deadline = Date.now() + 30000;
  while (flow.id === _actionFlowSeq && Date.now() < deadline) {
    if (await refreshElementTree(true)) {
      const drewBbox = await drawActionBboxAtLastPoint();
      if (drewBbox) {
        await waitForCommittedFrame();
        if (flow.id === _actionFlowSeq) setScreenLoading(false);
        return;
      }
    }
    await delay(250);
  }
  if (flow.id === _actionFlowSeq) setScreenLoading(false);
}

function failActionLoading(flow) {
  if (flow?.id === _actionFlowSeq) setScreenLoading(false);
}

function trackActionLoading(type, data, sendFn) {
  const flow = beginActionLoading();
  try {
    Promise.resolve(sendFn())
      .then(() => completeActionSend(flow, type, data))
      .catch(() => failActionLoading(flow));
  } catch (_) {
    failActionLoading(flow);
  }
}

function getActionVisualSettleMs(type, data = {}) {
  const defaults = {
    tap: 450,
    double_tap: 520,
    triple_tap: 620,
    five_tap: 760,
    two_finger_tap: 450,
    multi_finger_tap: 500,
    long_press: 350,
    scroll: 180,
    swipe: 180,
    drag: 220,
    long_press_drag: 260,
    paint: 220,
    pinch: 220,
    rotate: 220,
    type_text: 450,
    home: 900,
    launch_app: 1200,
    terminate_app: 800,
  };
  return defaults[type] ?? 450;
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function waitForCommittedFrame() {
  return new Promise(resolve => {
    requestAnimationFrame(() => requestAnimationFrame(resolve));
  });
}

async function drawActionBboxAtLastPoint() {
  if (!_lastScreenPoint) return false;
  const { fx, fy } = _lastScreenPoint;
  const { x, y } = toDevice(fx, fy);

  let info = null;
  try { info = await api("GET", `/api/element_info?x=${x}&y=${y}`); } catch (_) {}
  if (info?.cache_ready === false) return false;
  if (info?.found && info.bounds) return applyVisibleBbox(info.bounds);

  if (_treeElements.length) {
    const el = _clientHitTest(x, y);
    if (el?.rect) return applyVisibleBbox(el.rect);
  }
  return false;
}

function applyHoverInfo(info, fx, fy) {
  if (!info?.found || !info.bounds) {
    clearHoverHighlight();
    return Promise.resolve(false);
  }
  const b = info.bounds;
  if (!b.w || !b.h) {
    clearHoverHighlight();
    return Promise.resolve(false);
  }
  const rectKey = `${b.x},${b.y},${b.w},${b.h}`;
  cancelAnimationFrame(_hoverRafId);
  return new Promise(resolve => {
    _hoverRafId = requestAnimationFrame(() => {
      _hideHoverLoading();
      if (rectKey !== _hoverLastKey || hoverBboxRect.getAttribute("visibility") !== "visible") {
        _hoverLastKey = rectKey;
        setBboxRectAttrs(hoverBboxRect, b);
      }
      resolve(true);
    });
  });
}

function applyVisibleBbox(bounds) {
  if (!bounds?.w || !bounds?.h) return Promise.resolve(false);
  return new Promise(resolve => {
    requestAnimationFrame(() => {
      setBboxRectAttrs(hoverBboxRect, bounds);
      resolve(true);
    });
  });
}

function setBboxRectAttrs(rectEl, bounds) {
  const r  = clickLayer.getBoundingClientRect();
  const sx = r.width  / deviceW;
  const sy = r.height / deviceH;
  rectEl.setAttribute("x",          bounds.x * sx);
  rectEl.setAttribute("y",          bounds.y * sy);
  rectEl.setAttribute("width",      bounds.w * sx);
  rectEl.setAttribute("height",     bounds.h * sy);
  rectEl.setAttribute("visibility", "visible");
}

function clearVisibleBbox() {
  hoverBboxRect.setAttribute("visibility", "hidden");
}

function updateHoverHighlight(fx, fy) {
  const { x, y } = toDevice(fx, fy);
  const coordKey = `${x},${y}`;
  if (coordKey === _hoverCoord) return;
  _hoverCoord = coordKey;

  clearTimeout(_hoverTimer);
  clearTimeout(_hoverRetryTimer);
  _showHoverLoading(fx, fy);
  _hoverTimer = setTimeout(() => _fetchHoverAt(x, y, fx, fy, coordKey), 60);
}

async function _fetchHoverAt(x, y, fx, fy, coordKey) {
  if (coordKey !== _hoverCoord) return;
  let info = null;
  try { info = await api("GET", `/api/element_info?x=${x}&y=${y}`); } catch (_) {}
  if (coordKey !== _hoverCoord) return;

  if (info?.cache_ready === false) {
    // Hierarchy still loading — keep crosshair, retry shortly
    _hoverRetryTimer = setTimeout(() => _fetchHoverAt(x, y, fx, fy, coordKey), 250);
    return;
  }
  await applyHoverInfo(info, fx, fy);
}

function _showHoverLoading(fx, fy) {
  const sz = 10;
  hoverLoadingH.setAttribute("x1", fx - sz); hoverLoadingH.setAttribute("y1", fy);
  hoverLoadingH.setAttribute("x2", fx + sz); hoverLoadingH.setAttribute("y2", fy);
  hoverLoadingV.setAttribute("x1", fx);       hoverLoadingV.setAttribute("y1", fy - sz);
  hoverLoadingV.setAttribute("x2", fx);       hoverLoadingV.setAttribute("y2", fy + sz);
  hoverLoadingMark.setAttribute("visibility", "visible");
}

function _hideHoverLoading() {
  hoverLoadingMark.setAttribute("visibility", "hidden");
}

function clearHoverHighlight() {
  _hoverCoord   = null;
  _hoverLastKey = null;
  clearTimeout(_hoverTimer);
  clearTimeout(_hoverRetryTimer);
  cancelAnimationFrame(_hoverRafId);
  if (!isScreenLoadingActive()) clearVisibleBbox();
  _hideHoverLoading();
}

clickLayer.addEventListener("pointerleave", clearHoverHighlight);

let _hoverBboxTimer = null;
let _hoverBboxLast  = null; // "x,y" to skip identical positions

// Client-side hit-test: smallest bounding area wins.
// _treeElements is in post-order (children before parents), so on equal area
// the child is already `best` and the strict < never replaces it with the parent.
function _clientHitTest(dx, dy) {
  const candidates = _treeElements.filter(el => {
    const r = el.rect;
    return r && dx >= r.x && dx <= r.x + r.w && dy >= r.y && dy <= r.y + r.h;
  });
  if (!candidates.length) return null;
  return candidates.reduce((best, el) =>
    el.rect.w * el.rect.h < best.rect.w * best.rect.h ? el : best
  );
}

function hoverVerifyBbox(fx, fy) {
  const { x, y } = toDevice(fx, fy);
  const key = `${Math.round(x)},${Math.round(y)}`;
  if (key === _hoverBboxLast) return;
  _hoverBboxLast = key;

  // Fast path: synchronous client-side hit-test when tree is cached
  if (_treeElements.length) {
    const el = _clientHitTest(x, y);
    if ((verifyMode === "screenshot_gt" || verifyMode === "screenshot_diff") && verifyPhase === 0) {
      drawVerifyBbox(el ? el.rect : null);
    }
    return;
  }

  // Fallback: ask backend (no tree cached yet)
  clearTimeout(_hoverBboxTimer);
  _hoverBboxTimer = setTimeout(async () => {
    let info = { found: false };
    try { info = await api("GET", `/api/element_info?x=${x}&y=${y}`); } catch (_) {}
    if ((verifyMode === "screenshot_gt" || verifyMode === "screenshot_diff") && verifyPhase === 0) {
      drawVerifyBbox(info.found ? info.bounds : null);
    }
  }, 80);
}

async function handleVerifyTargetPick(fx, fy) {
  const { x, y } = toDevice(fx, fy);
  showRipple(fx, fy);

  // Fetch element info from backend
  let info = { found: false };
  try {
    info = await api("GET", `/api/element_info?x=${x}&y=${y}`);
  } catch (_) {}

  verifyTarget = {
    x, y,
    type:             info.found ? info.type             : "coordinate",
    value:            info.found ? info.value            : null,
    text:             info.found ? info.text             : "",
    bounds:           info.found ? info.bounds           : null,
    selector_quality: info.found ? info.selector_quality : null,
  };

  switch (verifyMode) {
    case "visible":
      // Record immediately and exit
      sendVerify("verify_visible", { target_x: x, target_y: y, not_visible: false });
      exitVerifyMode();
      break;

    case "not_visible":
      // Enter process phase: user does actions, then clicks Done
      verifyPhase = 1;
      showVerifyPhaseLabel("PROCESS");
      showVerifyDoneBtn("not_visible");
      break;

    case "get_text":
      openVerifyTextDialog(x, y, verifyTarget.text);
      break;

    case "screenshot_gt":
      // bbox already shown by hover; open dialog
      openVerifyGtDialog(x, y, verifyTarget.bounds);
      break;

    case "screenshot_diff":
      // bbox already shown by hover; record before + enter process phase
      sendVerify("verify_screenshot_diff", { target_x: x, target_y: y, bounds: verifyTarget.bounds ?? {}, phase: "before" });
      // Save context so sub-verifications can run during PROCESS
      _screenshotDiffCtx = { x, y, bounds: verifyTarget.bounds ?? {} };
      console.debug("[screenshot_diff] set _screenshotDiffCtx=", _screenshotDiffCtx);
      verifyMode  = null; // free up verifyMode for sub-verifications
      verifyPhase = 1;
      verifyBtns.forEach(b => b.classList.remove("active"));
      showVerifyPhaseLabel("PROCESS", "screenshot_diff");
      showVerifyDoneBtn("screenshot_diff");
      break;
  }
}

async function handleTypeTargetPick(fx, fy) {
  const { x, y } = toDevice(fx, fy);
  showRipple(fx, fy);
  let info = { found: false };
  try { info = await api("GET", `/api/element_info?x=${x}&y=${y}`); } catch (_) {}
  typeTextSelectedTarget = info.found
    ? { x, y, type: info.type, value: info.value, bounds: info.bounds ?? null, selector_quality: info.selector_quality ?? null }
    : { x, y, type: "coordinate" };
  if (info.found && info.bounds) drawVerifyBbox(info.bounds);
  awaitingTypeTarget = false;
  typeBtn.classList.remove("active");
  verifyPhaseSidebar.style.display = "none";
  verifyContextBadge.style.display = "none";
  openTypeOverlay();
}

verifyDoneBtn.addEventListener("click", () => {
  console.debug("[Done] _screenshotDiffCtx=", _screenshotDiffCtx, "verifyMode=", verifyMode, "verifyPhase=", verifyPhase, "verifyTarget=", verifyTarget);
  if (_screenshotDiffCtx !== null) {
    // Capture AFTER, then ask user for expected result before fully exiting
    const { x, y, bounds } = _screenshotDiffCtx;
    _screenshotDiffCtx = null;
    openVerifyDiffExpectedDialog((expectedResult) => {
      sendVerify("verify_screenshot_diff", { target_x: x, target_y: y, bounds, phase: "after", expected_result: expectedResult });
      exitVerifyMode();
    });
    return;
  }
  if (!verifyTarget) { exitVerifyMode(); return; }
  const { x, y, bounds } = verifyTarget;
  if (verifyMode === "not_visible") {
    sendVerify("verify_visible", {
      target_x: x, target_y: y, not_visible: true,
      target_type:             verifyTarget.type,
      target_value:            verifyTarget.value,
      target_bounds:           verifyTarget.bounds,
      target_selector_quality: verifyTarget.selector_quality,
    });
  }
  exitVerifyMode();
});

function sendVerify(type, data) {
  const record = isRecording;
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type, ...data, record }));
    return;
  }
  if (record) {
    const epMap = {
      verify_visible:        "/api/record/verify_visible",
      verify_get_text:       "/api/record/verify_get_text",
      verify_screenshot_gt:  "/api/record/verify_screenshot_gt",
      verify_screenshot_diff:"/api/record/verify_screenshot_diff",
    };
    if (epMap[type]) api("POST", epMap[type], data);
  }
}

// ── Verify: Get Text dialog ────────────────────────────────────────────────────
function openVerifyTextDialog(x, y, fetchedText) {
  verifyTextExpected.value = fetchedText || "";
  verifyTextModal.style.display = "flex";
  verifyTextExpected.focus();
  verifyTextExpected.select();

  // Store coords for confirm handler
  verifyTextConfirm._x = x;
  verifyTextConfirm._y = y;
}

function closeVerifyTextDialog() {
  verifyTextModal.style.display = "none";
  exitVerifyMode();
}

verifyTextClose.addEventListener("click",   () => closeVerifyTextDialog());
verifyTextCancel.addEventListener("click",  () => closeVerifyTextDialog());
verifyTextModal.addEventListener("click", e => { if (e.target === verifyTextModal) closeVerifyTextDialog(); });
verifyTextExpected.addEventListener("keydown", e => {
  if (e.key === "Enter") { e.preventDefault(); verifyTextConfirm.click(); }
  if (e.key === "Escape") closeVerifyTextDialog();
});
verifyTextConfirm.addEventListener("click", () => {
  const expected = verifyTextExpected.value.trim();
  const x = verifyTextConfirm._x, y = verifyTextConfirm._y;
  verifyTextModal.style.display = "none";
  sendVerify("verify_get_text", { target_x: x, target_y: y, expected_text: expected });
  exitVerifyMode();
});

// ── Verify: Screenshot Diff expected-result dialog ──────────────────────────
const verifyDiffExpectedModal = document.getElementById("verifyDiffExpectedModal");
const diffExpectedSameBtn     = document.getElementById("diffExpectedSame");
const diffExpectedDiffBtn     = document.getElementById("diffExpectedDiff");

function openVerifyDiffExpectedDialog(cb) {
  _diffExpectedCb = cb;
  verifyDiffExpectedModal.style.display = "flex";
}

function closeDiffExpectedDialog(expectedResult) {
  verifyDiffExpectedModal.style.display = "none";
  if (_diffExpectedCb) { _diffExpectedCb(expectedResult); _diffExpectedCb = null; }
}

diffExpectedSameBtn.addEventListener("click", () => { if (verifyDiffExpectedModal.style.display !== "none") closeDiffExpectedDialog("same"); });
diffExpectedDiffBtn.addEventListener("click", () => { if (verifyDiffExpectedModal.style.display !== "none") closeDiffExpectedDialog("different"); });

// ── Verify: Screenshot GT dialog ──────────────────────────────────────────────
function openVerifyGtDialog(x, y, bounds) {
  const caseName = caseNameInput.value.trim() || "screenshot";
  const stepIdx  = steps.length + 1;
  verifyGtNameInput.value = `${caseName}_Step${String(stepIdx).padStart(2, "0")}`;
  verifyScreenshotGtModal.style.display = "flex";
  verifyGtNameInput.focus();
  verifyGtNameInput.select();

  verifyGtConfirm._x = x;
  verifyGtConfirm._y = y;
  verifyGtConfirm._bounds = bounds;
}

function closeVerifyGtDialog() {
  verifyScreenshotGtModal.style.display = "none";
  exitVerifyMode();
}

verifyGtClose.addEventListener("click",  () => closeVerifyGtDialog());
verifyGtCancel.addEventListener("click", () => closeVerifyGtDialog());
verifyScreenshotGtModal.addEventListener("click", e => { if (e.target === verifyScreenshotGtModal) closeVerifyGtDialog(); });
verifyGtNameInput.addEventListener("keydown", e => {
  if (e.key === "Enter") { e.preventDefault(); verifyGtConfirm.click(); }
  if (e.key === "Escape") closeVerifyGtDialog();
});
verifyGtConfirm.addEventListener("click", () => {
  const name   = verifyGtNameInput.value.trim().replace(/[^a-zA-Z0-9_\-]/g, "_") || "screenshot";
  const x      = verifyGtConfirm._x;
  const y      = verifyGtConfirm._y;
  const bounds = verifyGtConfirm._bounds ?? {};
  verifyScreenshotGtModal.style.display = "none";
  sendVerify("verify_screenshot_gt", { target_x: x, target_y: y, screenshot_name: name, bounds });
  exitVerifyMode();
});

// ── Visual feedback ────────────────────────────────────────────────────────────
function showRipple(x, y) {
  const el = document.createElement("div");
  el.className = "ripple";
  el.style.cssText = `left:${x}px;top:${y}px`;
  clickLayer.appendChild(el);
  setTimeout(() => el.remove(), 600);
}

let longRingEl = null;
function showLongRing(x, y) {
  longRingEl = document.createElement("div");
  longRingEl.className = "long-ring";
  longRingEl.style.cssText = `left:${x}px;top:${y}px`;
  clickLayer.appendChild(longRingEl);
}

function clearGestureOverlay() {
  gestureSvg.innerHTML = "";
  if (longRingEl) { longRingEl.remove(); longRingEl = null; }
}

function drawSwipePreview(x1, y1, x2, y2, mode = dragMode) {
  const modeColors = { scroll: "#50fa7b", swipe: "#4a9eff", drag: "#ffb86c", long_press_drag: "#ff79c6", paint: "#ff79c6" };
  const color = modeColors[mode] || "#4a9eff";
  const dashArr = (mode === "drag" || mode === "long_press_drag") ? "5,3" : "8,4";
  const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
  const label = mode === "long_press_drag" ? "LONG DRAG" : mode.toUpperCase();
  const tw = label.length * 8 + 16;
  gestureSvg.innerHTML = `
    <defs><marker id="arr" markerWidth="6" markerHeight="4" refX="6" refY="2" orient="auto">
      <polygon points="0 0,6 2,0 4" fill="${color}"/>
    </marker></defs>
    <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}"
      stroke="${color}" stroke-width="2.5" stroke-dasharray="${dashArr}"
      marker-end="url(#arr)" opacity=".85"/>
    <circle cx="${x1}" cy="${y1}" r="5" fill="${color}" opacity=".7"/>
    <rect x="${mx - tw / 2}" y="${my - 19}" width="${tw}" height="20" rx="4"
      fill="rgba(255,255,255,0.93)" pointer-events="none"/>
    <text x="${mx}" y="${my - 4}" text-anchor="middle" fill="#1a1a1a"
      font-size="11" font-weight="700" font-family="monospace" pointer-events="none">${label}</text>`;
}

function drawPaintPreview(points, cursorX, cursorY) {
  if (!Array.isArray(points) || !points.length) return;
  const color = "#ff79c6";
  const tmp = points.slice();
  const last = tmp[tmp.length - 1];
  if (!last || Math.hypot(last.x - cursorX, last.y - cursorY) > 0.5) {
    tmp.push({ x: cursorX, y: cursorY });
  }
  const pts = tmp.map(p => `${p.x},${p.y}`).join(" ");
  gestureSvg.innerHTML = `
    <polyline points="${pts}" fill="none" stroke="${color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.95" />
    <circle cx="${tmp[0].x}" cy="${tmp[0].y}" r="4" fill="${color}" opacity="0.8"/>
    <circle cx="${tmp[tmp.length - 1].x}" cy="${tmp[tmp.length - 1].y}" r="3" fill="${color}" opacity="0.9"/>
  `;
}

function showGestureTrail(x1, y1, x2, y2, mode = dragMode) {
  const modeColors = { scroll: "#50fa7b", swipe: "#4a9eff", drag: "#ffb86c", long_press_drag: "#ff79c6", paint: "#ff79c6" };
  const color = modeColors[mode] || "#4a9eff";
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.style.cssText = "position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible";
  svg.innerHTML = `
    <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}"
      stroke="${color}" stroke-width="2" opacity="1"
      style="animation:gesture-fade .7s ease-out forwards"/>`;
  clickLayer.appendChild(svg);
  setTimeout(() => svg.remove(), 800);
}

function finiteNumber(value) {
  const n = Number(value);
  return Number.isFinite(n) ? n : null;
}

function sentCoordActionLabel(type) {
  const labels = {
    tap: "TAP",
    double_tap: "DOUBLE TAP",
    triple_tap: "TRIPLE TAP",
    five_tap: "FIVE TAP",
    two_finger_tap: "TWO FINGER TAP",
    multi_finger_tap: "MULTI FINGER TAP",
    long_press: "LONG PRESS",
    scroll: "SCROLL",
    swipe: "SWIPE",
    drag: "DRAG",
    long_press_drag: "LONG DRAG",
    paint: "PAINT",
    pinch: "PINCH",
    rotate: "ROTATE",
  };
  return labels[type] || String(type || "GESTURE").replace(/_/g, " ").toUpperCase();
}

function sentCoordColor(type) {
  const colors = {
    long_press_drag: "#ff79c6",
    drag: "#ffb86c",
    scroll: "#50fa7b",
    swipe: "#4a9eff",
    paint: "#ff79c6",
    long_press: "#ffd166",
    pinch: "#bd93f9",
    rotate: "#bd93f9",
  };
  return colors[type] || "#4a9eff";
}

function sentCoordPayloadPoints(type, data) {
  if (!data || typeof data !== "object") return [];

  const x1 = finiteNumber(data.x1), y1 = finiteNumber(data.y1);
  const x2 = finiteNumber(data.x2), y2 = finiteNumber(data.y2);
  if (x1 !== null && y1 !== null && x2 !== null && y2 !== null) {
    return [
      { role: "START", x: x1, y: y1 },
      { role: "END", x: x2, y: y2 },
    ];
  }

  const x = finiteNumber(data.x), y = finiteNumber(data.y);
  if (x !== null && y !== null) {
    return [{ role: sentCoordActionLabel(type), x, y }];
  }

  const startX = finiteNumber(data.start_x), startY = finiteNumber(data.start_y);
  if (startX !== null && startY !== null) {
    const points = Array.isArray(data.points) ? data.points : [];
    const last = [...points].reverse().find((pt) =>
      finiteNumber(pt?.x) !== null && finiteNumber(pt?.y) !== null
    );
    if (last) {
      return [
        { role: "START", x: startX, y: startY },
        { role: "END", x: Number(last.x), y: Number(last.y) },
      ];
    }
    return [{ role: "START", x: startX, y: startY }];
  }

  return [];
}

function svgNode(tag, attrs = {}) {
  const node = document.createElementNS("http://www.w3.org/2000/svg", tag);
  Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value));
  return node;
}

function addSentCoordLabel(svg, x, y, lines, width, height) {
  const cleanLines = lines.filter(Boolean);
  if (!cleanLines.length) return;

  const lineH = 13;
  const padX = 7;
  const rectW = Math.max(56, Math.min(width - 8, Math.max(...cleanLines.map((line) => line.length)) * 7 + padX * 2));
  const rectH = cleanLines.length * lineH + 7;
  const rectX = Math.max(4, Math.min(width - rectW - 4, x - rectW / 2));
  let rectY = y - rectH - 13;
  if (rectY < 4) rectY = y + 13;
  if (rectY + rectH > height - 4) rectY = Math.max(4, height - rectH - 4);

  svg.appendChild(svgNode("rect", {
    x: rectX,
    y: rectY,
    width: rectW,
    height: rectH,
    rx: 4,
    fill: "rgba(5,8,14,0.9)",
    stroke: "rgba(255,255,255,0.78)",
    "stroke-width": 1,
  }));

  cleanLines.forEach((line, idx) => {
    const text = svgNode("text", {
      x: rectX + rectW / 2,
      y: rectY + 15 + idx * lineH,
      "text-anchor": "middle",
      fill: "#ffffff",
      "font-size": 11,
      "font-weight": 800,
      "font-family": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
      "pointer-events": "none",
    });
    text.textContent = line;
    svg.appendChild(text);
  });
}

function addSentCoordCrosshair(svg, point, color, width, height) {
  const raw = deviceToDisplay(point.x, point.y);
  const x = Math.max(0, Math.min(width, raw.x));
  const y = Math.max(0, Math.min(height, raw.y));
  const offscreen = Math.abs(x - raw.x) > 0.5 || Math.abs(y - raw.y) > 0.5;

  svg.appendChild(svgNode("circle", {
    cx: x,
    cy: y,
    r: 10,
    fill: "rgba(0,0,0,0.18)",
    stroke: "rgba(0,0,0,0.72)",
    "stroke-width": 4,
  }));
  svg.appendChild(svgNode("circle", {
    cx: x,
    cy: y,
    r: 10,
    fill: "rgba(255,255,255,0.16)",
    stroke: color,
    "stroke-width": 2.5,
  }));
  svg.appendChild(svgNode("line", { x1: x - 14, y1: y, x2: x + 14, y2: y, stroke: "#ffffff", "stroke-width": 1.5, "stroke-linecap": "round" }));
  svg.appendChild(svgNode("line", { x1: x, y1: y - 14, x2: x, y2: y + 14, stroke: "#ffffff", "stroke-width": 1.5, "stroke-linecap": "round" }));

  const coord = `${Math.round(point.x)},${Math.round(point.y)}`;
  addSentCoordLabel(svg, x, y, [`${point.role} ${coord}`, offscreen ? "OFFSCREEN" : ""], width, height);
  return { x, y };
}

function showSentCoordsOverlay(type, data) {
  const points = sentCoordPayloadPoints(type, data);
  if (!points.length) return;

  const rect = clickLayer.getBoundingClientRect();
  const width = rect.width;
  const height = rect.height;
  if (!width || !height) return;

  clickLayer.querySelectorAll(".sent-coords-overlay").forEach((el) => el.remove());

  const color = sentCoordColor(type);
  const svg = svgNode("svg", {
    class: "sent-coords-overlay",
    viewBox: `0 0 ${width} ${height}`,
    preserveAspectRatio: "none",
  });

  let displayPoints = [];
  if (points.length >= 2) {
    displayPoints = points.map((point) => {
      const raw = deviceToDisplay(point.x, point.y);
      return {
        x: Math.max(0, Math.min(width, raw.x)),
        y: Math.max(0, Math.min(height, raw.y)),
      };
    });

    svg.appendChild(svgNode("line", {
      x1: displayPoints[0].x,
      y1: displayPoints[0].y,
      x2: displayPoints[displayPoints.length - 1].x,
      y2: displayPoints[displayPoints.length - 1].y,
      stroke: "rgba(0,0,0,0.72)",
      "stroke-width": 6,
      "stroke-linecap": "round",
    }));
    svg.appendChild(svgNode("line", {
      x1: displayPoints[0].x,
      y1: displayPoints[0].y,
      x2: displayPoints[displayPoints.length - 1].x,
      y2: displayPoints[displayPoints.length - 1].y,
      stroke: color,
      "stroke-width": 3,
      "stroke-linecap": "round",
      "stroke-dasharray": type === "long_press_drag" || type === "drag" ? "7,4" : "",
    }));
  }

  const marks = points.map((point) => addSentCoordCrosshair(svg, point, color, width, height));
  if (marks.length >= 2) {
    const midX = (marks[0].x + marks[marks.length - 1].x) / 2;
    const midY = (marks[0].y + marks[marks.length - 1].y) / 2;
    const pressDuration = finiteNumber(data?.press_duration);
    const hold = type === "long_press_drag" && pressDuration !== null ? `hold ${Math.round(pressDuration)}ms` : "";
    addSentCoordLabel(svg, midX, midY, [`SENT ${sentCoordActionLabel(type)}`, hold], width, height);
  }

  clickLayer.appendChild(svg);
  setTimeout(() => svg.remove(), 3400);
}

// ── Unit Test Capture ──────────────────────────────────────────────────────────
async function pollUnitTestStatus() {
  const data = await api("GET", "/api/unit_test/status").catch(() => null);
  if (!data) return;
  unitTestEntryCount = data.entry_count;
  _updateUnitTestCount();
  _updateUnitTestBtn();
}

function _updateUnitTestCount() {
  unitTestCountEl.textContent = `${unitTestEntryCount} entr${unitTestEntryCount === 1 ? "y" : "ies"} captured`;
}

function _updateUnitTestBtn() {
  const hasName = caseNameInput.value.trim().length > 0;
  exportUnitTestBtn.disabled = !hasName || unitTestEntryCount === 0;
}

unitTestResultClose.addEventListener("click", () => { unitTestResultModal.style.display = "none"; });
unitTestResultModal.addEventListener("click", e => { if (e.target === unitTestResultModal) unitTestResultModal.style.display = "none"; });

exportUnitTestBtn.addEventListener("click", async () => {
  const caseName = caseNameInput.value.trim();
  const data = await api("POST", "/api/unit_test/save", { case_name: caseName }).catch(() => null);
  if (!data?.ok) return;
  unitTestResultPaths.innerHTML = (data.saved_paths || [])
    .map(p => `<li style="font-family:monospace;font-size:13px;word-break:break-all;">${p}</li>`)
    .join("");
  unitTestResultModal.style.display = "flex";
  unitTestEntryCount = 0;
  _updateUnitTestCount();
  _updateUnitTestBtn();
});

// ── Case name gate ─────────────────────────────────────────────────────────────
function updateActionBtns() {
  const hasName = caseNameInput.value.trim().length > 0;
  const hint = "Please enter a case name first";
  [recBtn, clearBtn, exportBtn].forEach(btn => {
    btn.disabled = !hasName;
    if (hasName) btn.removeAttribute("title");
    else btn.title = hint;
  });
  if (unitTestMode) _updateUnitTestBtn();
}
caseNameInput.addEventListener("input", updateActionBtns);

// ── Recording controls ─────────────────────────────────────────────────────────
recBtn.addEventListener("click", () => {
  isRecording = !isRecording;
  recBtn.textContent = isRecording ? "⏹ Stop" : "⏺ Record";
  recBtn.classList.toggle("on", isRecording);
});

clearBtn.addEventListener("click", async () => {
  await api("DELETE", "/api/steps");
  steps = [];
  renderSteps();
  if (unitTestMode) {
    unitTestEntryCount = 0;
    _updateUnitTestCount();
    _updateUnitTestBtn();
  }
});

// ── Export result modal ───────────────────────────────────────────────────────
const exportResultModal = document.getElementById("exportResultModal");
const exportResultClose = document.getElementById("exportResultClose");
const exportResultPaths = document.getElementById("exportResultPaths");
exportResultClose.addEventListener("click", () => { exportResultModal.style.display = "none"; });
exportResultModal.addEventListener("click", e => { if (e.target === exportResultModal) exportResultModal.style.display = "none"; });

exportBtn.addEventListener("click", async () => {
  const caseName = caseNameInput.value.trim();
  const data = await api("POST", "/api/export", { case_name: caseName }).catch(() => null);
  if (!data?.script) return;
  // Show export result dialog
  exportResultPaths.innerHTML = (data.saved_paths || [data.filename])
    .map(p => `<li style="font-family:monospace;font-size:13px;word-break:break-all;">${p}</li>`)
    .join("");
  exportResultModal.style.display = "flex";
});

// ── Steps polling ──────────────────────────────────────────────────────────────
async function pollSteps() {
  const data = await api("GET", "/api/steps").catch(() => null);
  if (!data?.steps) return;
  const changed = JSON.stringify(data.steps) !== JSON.stringify(steps);
  if (changed) { steps = data.steps; renderSteps(); }
}

function renderSteps() {
  stepCount.textContent = steps.length;
  if (!steps.length) {
    stepsList.innerHTML = '<div class="empty">No steps recorded yet</div>';
    return;
  }
  stepsList.innerHTML = steps.map((s, i) => {
    let cls, typeStr, valStr;
    const c = s.coords;

    if (s.action === "swipe" || s.action === "drag" || s.action === "long_press_drag") {
      const st = s.start_target;
      const qCls = (st && st.type !== "coordinate") ? qualityClass(st) : "";
      cls = (qCls ? qCls + " " : "") + "is-gesture";
      typeStr = s.action === "long_press_drag" ? "long press drag" : s.action === "drag" ? "drag" : "swipe";
      if (s.action === "swipe" && s.swipe_target && s.swipe_target.type !== "coordinate") {
        const dir = s.direction || "?";
        valStr = `${dir} until: ${s.swipe_target.type}: ${s.swipe_target.value}`;
      } else if (s.action === "swipe" && s.start_target && s.start_target.type !== "coordinate") {
        const dir = s.direction || "?";
        const dur = s.duration != null ? `${s.duration}ms` : null;
        const vel = s.velocity != null ? `${Math.round(s.velocity)}px/s` : null;
        const meta = [dur, vel].filter(Boolean).join(" · ");
        valStr = `${dir} on ${s.start_target.value}` + (meta ? ` · ${meta}` : "");
      } else if (s.action === "drag" || s.action === "long_press_drag") {
        const st = s.start_target, et = s.end_target;
        const hasStart = st && st.type !== "coordinate";
        const hasEnd   = et && et.type !== "coordinate";
        const hold = s.action === "long_press_drag" && s.press_duration != null ? ` · hold ${s.press_duration}ms` : "";
        if (hasStart && hasEnd) {
          const sp = st.offset_pct ?? { x: "?", y: "?" };
          const ep = et.offset_pct ?? { x: "?", y: "?" };
          valStr = `${st.value} (${sp.x}%,${sp.y}%) → ${et.value} (${ep.x}%,${ep.y}%)${hold}`;
        } else if (hasStart) {
          const sp = st.offset_pct ?? { x: "?", y: "?" };
          valStr = `${st.value} (${sp.x}%,${sp.y}%) → (${c.x2},${c.y2})${hold}`;
        } else {
          valStr = `(${c.x1},${c.y1}) → (${c.x2},${c.y2})${hold}`;
        }
      } else {
        valStr = `(${c.x1},${c.y1}) → (${c.x2},${c.y2})`;
      }
    } else if (s.action === "scroll") {
      const sc = s.scroll_container;
      const qCls = (sc && sc.type !== "coordinate") ? qualityClass(sc) : "";
      cls = (qCls ? qCls + " " : "") + "is-scroll";
      typeStr = "scroll";
      if (s.scroll_target && s.scroll_target.type !== "coordinate") {
        valStr = `→ ${s.scroll_target.type}: ${s.scroll_target.value}`;
      } else {
        valStr = `(${c.x1},${c.y1}) → (${c.x2},${c.y2})`;
      }
    } else if (s.action === "pinch") {
      const pt = s.target;
      const qCls = (pt && pt.type !== "coordinate") ? qualityClass(pt) : "";
      cls = (qCls ? qCls + " " : "") + "is-gesture";
      typeStr = "pinch";
      const pEl = pt && pt.type !== "coordinate" ? `${pt.type}: ${pt.value}` : null;
      valStr = pEl
        ? `×${(s.scale ?? 1).toFixed(2)} on ${pEl}`
        : `×${(s.scale ?? 1).toFixed(2)} @ (${c.x},${c.y})`;
    } else if (s.action === "rotate") {
      const rt = s.target;
      const qCls = (rt && rt.type !== "coordinate") ? qualityClass(rt) : "";
      cls = (qCls ? qCls + " " : "") + "is-gesture";
      typeStr = "rotate";
      const rEl = rt && rt.type !== "coordinate" ? `${rt.type}: ${rt.value}` : null;
      valStr = rEl
        ? `${(s.rotation ?? 0).toFixed(1)}° on ${rEl}`
        : `${(s.rotation ?? 0).toFixed(1)}° @ (${c.x},${c.y})`;
    } else if (s.action === "type_text") {
      cls = "t-name";
      const t = s.target;
      const txt = s.text ?? "";
      if (t && t.type !== "coordinate") {
        typeStr = "value to selected element";
        valStr = `"${txt}" → ${t.value}`;
      } else {
        typeStr = "type";
        valStr = `"${txt}"`;
      }
    } else if (s.action === "home") {
      cls = "t-gesture";
      typeStr = "home";
      valStr = "press home";
    } else if (s.action === "launch_app") {
      cls = "t-name";
      typeStr = "launch";
      valStr = s.app_name ?? s.bundle_id ?? "";
    } else if (s.action === "terminate_app") {
      cls = "t-name";
      typeStr = "kill";
      valStr = s.app_name ?? s.bundle_id ?? "";
    } else if (s.action === "verify_visible") {
      const t = s.target;
      cls = (t && t.type !== "coordinate") ? qualityClass(t) : "t-coord";
      typeStr = "assert visible";
      valStr = t && t.type !== "coordinate" ? `${t.type}: ${t.value}` : `(${s.coords?.x},${s.coords?.y})`;
    } else if (s.action === "verify_not_visible") {
      const t = s.target;
      cls = (t && t.type !== "coordinate") ? qualityClass(t) : "t-coord";
      typeStr = "assert not visible";
      valStr = t && t.type !== "coordinate" ? `${t.type}: ${t.value}` : `(${s.coords?.x},${s.coords?.y})`;
    } else if (s.action === "verify_get_text") {
      const t = s.target;
      cls = (t && t.type !== "coordinate") ? qualityClass(t) : "t-coord";
      typeStr = "assert text";
      valStr = `"${s.expected_text ?? ""}" — ${t && t.type !== "coordinate" ? `${t.type}: ${t.value}` : "coord"}`;
    } else if (s.action === "verify_screenshot_gt") {
      const t = s.target;
      cls = (t && t.type !== "coordinate") ? qualityClass(t) : "t-coord";
      typeStr = "screenshot GT";
      const elInfo = t && t.type !== "coordinate" ? ` — ${t.type}: ${t.value}` : "";
      valStr = (s.screenshot_name ?? "") + elInfo;
    } else if (s.action === "verify_screenshot_diff") {
      const t = s.target;
      cls = (t && t.type !== "coordinate") ? qualityClass(t) : "t-coord";
      const phase = s.phase ?? "before";
      const expected = s.expected_result;
      const badge = expected === "same" ? " ✅" : expected === "different" ? " 🔄" : "";
      typeStr = phase === "after" ? `scr diff after${badge}` : "scr diff before";
      const elPart = t && t.type !== "coordinate" ? ` — ${t.type}: ${t.value}` : ` — (${s.coords?.x},${s.coords?.y})`;
      valStr = (s.screenshot_name ?? "") + elPart;
    } else {
      const t = s.target;
      if (!t || t.type === "coordinate") {
        cls = "t-coord"; typeStr = s.action;
        valStr = t ? `(${t.x},${t.y})` : `(${c?.x},${c?.y})`;
      } else {
        cls = qualityClass(t);
        const labelMap = { tap: "tap", double_tap: "2×tap", triple_tap: "3×tap", five_tap: "5×tap", long_press: "long press", two_finger_tap: "2 finger tap", multi_finger_tap: `${s.fingers ?? 3} finger tap` };
        typeStr = `${labelMap[s.action] ?? s.action}: ${t.type}`;
        valStr = t.value;
      }
    }
    return `<div class="step ${cls}" data-step-idx="${i}">
      <span class="step-n">#${i + 1}</span>
      <span class="step-type">${esc(typeStr)}</span>
      <span class="step-val">${esc(valStr)}</span>
    </div>`;
  }).join("");
  stepsList.scrollTop = stepsList.scrollHeight;
}

// ── Step deletion (7 consecutive clicks) ────────────────────────────────────
const _stepClickCounters = new Map(); // "idx" -> { count, timer }

stepsList.addEventListener("click", e => {
  const stepEl = e.target.closest(".step[data-step-idx]");
  if (!stepEl) return;
  const idx = parseInt(stepEl.dataset.stepIdx, 10);
  const key = String(idx);

  let entry = _stepClickCounters.get(key);
  if (!entry) {
    entry = { count: 0, timer: null };
    _stepClickCounters.set(key, entry);
  }

  clearTimeout(entry.timer);
  entry.count++;

  if (entry.count >= 7) {
    _stepClickCounters.delete(key);
    _deleteStep(idx);
    return;
  }

  entry.timer = setTimeout(() => {
    _stepClickCounters.delete(key);
  }, 1500);
});

async function _deleteStep(idx) {
  await api("DELETE", `/api/steps/${idx}`);
  steps.splice(idx, 1);
  renderSteps();
}

function typeClass(type) {
  if (type === "accessibility id") return "t-acc";
  if (type === "name") return "t-name";
  if (type === "coordinate") return "t-coord";
  return "t-xpath";
}

// Returns a CSS class based on selector_quality when available, else falls back to typeClass.
function qualityClass(target) {
  if (!target || target.type === "coordinate") return "t-coord";
  const q = target.selector_quality;
  if (q === "id")           return "q-id";
  if (q === "id_indexed")   return "q-id-indexed";
  if (q === "id_eq_label")  return "q-id-eq-label";
  if (q === "label_only")   return "q-label-only";
  if (q === "xpath_only")   return "q-xpath-only";
  // Fallback for steps recorded before this feature
  return typeClass(target.type);
}

// ── Helpers ────────────────────────────────────────────────────────────────────
function esc(s) {
  return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}

async function api(method, path, body) {
  const opts = { method, headers: {} };
  if (body) { opts.headers["Content-Type"] = "application/json"; opts.body = JSON.stringify(body); }
  const r = await fetch(path, opts);
  if (!r.ok) throw new Error(`${r.status}`);
  return r.json();
}
