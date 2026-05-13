import asyncio
import json
import logging
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import List, Optional

import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .codegen import generate_script
from .hittest import hit_test, hit_test_for_swipe, hit_test_excluding, hit_test_drop_target, find_scroll_container, build_scroll_container_selector, serialize, _rect as _el_rect
from .selector import build_selector, build_xpath, get_selector_quality
from .wda import WDAClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_CONFIG_FILE   = Path(__file__).parent.parent / ".wda_config.json"
_APPS_FILE     = Path(__file__).parent.parent / "apps.json"
_VERSION_FILE  = Path(__file__).parent.parent / "version.json"


def _load_wda_url() -> str:
    try:
        return json.loads(_CONFIG_FILE.read_text()).get("wda_url", "http://localhost:8100")
    except Exception:
        return "http://localhost:8100"


def _save_wda_url(url: str):
    try:
        _CONFIG_FILE.write_text(json.dumps({"wda_url": url}))
    except Exception:
        pass


def _load_apps() -> List[dict]:
    try:
        return json.loads(_APPS_FILE.read_text())
    except Exception:
        return []


wda = WDAClient(_load_wda_url())
_cache: dict = {"root": None, "ts": 0.0}
CACHE_TTL = 0.5
_steps: List[dict] = []
_last_tap_target: Optional[dict] = None
_WARN_QUALITIES = frozenset({"id_indexed", "id_eq_label", "label_only", "xpath_only"})


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(wda.connect())
    asyncio.create_task(_wda_heartbeat())
    yield
    await wda.close()


async def _wda_heartbeat():
    """Background task: validate WDA session every 5 s and recreate if lost.

    This keeps the recorder connected even while pytest/Appium temporarily
    owns the WDA session.  The check is skipped while a gesture is executing
    so it never races with in-flight actions.
    """
    while True:
        await asyncio.sleep(5)
        try:
            await wda.ping_session()
        except Exception as exc:
            logger.debug("WDA heartbeat error: %r", exc)


app = FastAPI(title="iOS Recorder", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


# ── Models ─────────────────────────────────────────────────────────────────────

class Coords(BaseModel):
    x: float
    y: float

class SwipeReq(BaseModel):
    x1: float; y1: float; x2: float; y2: float
    duration: int = 400

class DragReq(BaseModel):
    x1: float; y1: float; x2: float; y2: float
    duration: int = 1000

class LongPressReq(BaseModel):
    x: float
    y: float
    duration: int = 1000

class MultiFingerTapReq(BaseModel):
    x: float
    y: float
    fingers: int = 3

class ScrollReq(BaseModel):
    x1: float; y1: float; x2: float; y2: float
    duration: int = 600

class PinchReq(BaseModel):
    x: float
    y: float
    scale: float
    spread: int = 80
    duration: int = 500  # ms — used to derive velocity for playback

class RotateReq(BaseModel):
    x: float
    y: float
    rotation: float  # degrees, positive = clockwise
    spread: int = 80
    duration: int = 600  # ms — controls gesture speed

class TypeTextReq(BaseModel):
    text: str
    target_x: Optional[float] = None
    target_y: Optional[float] = None

class LaunchAppReq(BaseModel):
    bundle_id: str

class VerifyVisibleReq(BaseModel):
    target_x: float
    target_y: float
    not_visible: bool = False  # True → verify_not_visible

class VerifyGetTextReq(BaseModel):
    target_x: float
    target_y: float
    expected_text: str

class VerifyScreenshotGtReq(BaseModel):
    target_x: float
    target_y: float
    screenshot_name: str
    bounds: dict  # {x, y, w, h} in device coords

class VerifyScreenshotDiffReq(BaseModel):
    target_x: float
    target_y: float
    bounds: dict
    phase: str = "before"  # "before" | "after"
    expected_result: str = "same"  # "same" | "different" (only meaningful for phase=="after")

class ConfigIn(BaseModel):
    wda_url: str


# ── Status & Config ────────────────────────────────────────────────────────────

@app.get("/api/version")
async def get_version():
    try:
        data = json.loads(_VERSION_FILE.read_text())
        versions = data.get("versions", [])
        latest = versions[-1] if versions else {}
    except Exception:
        latest = {}
    return {"version": latest.get("version", ""), "date": latest.get("date", ""), "notes": latest.get("notes", "")}


@app.get("/api/status")
async def status():
    alive, size = await asyncio.gather(
        wda.is_alive(),
        wda.get_screen_size(),
    )
    # Auto-recover: WDA is reachable but session was lost.
    # Use adopt-only — never POST /session here; the heartbeat creates one
    # when GET /sessions confirms WDA is free (i.e. no Appium session running).
    if alive and not wda._session_id:
        asyncio.create_task(wda._adopt_session())
    return {
        "connected": alive,
        "wda_url": wda.base_url,
        "mjpeg_url": wda.mjpeg_url,
        "session": wda._session_id,
        "screen_size": size,
    }


@app.get("/api/config")
async def get_config():
    return {"wda_url": wda.base_url}


@app.post("/api/config")
async def set_config(req: ConfigIn):
    await wda.connect(req.wda_url)
    _save_wda_url(req.wda_url)
    return {"ok": True, "wda_url": wda.base_url}


@app.get("/api/screen_size")
async def screen_size():
    return await wda.get_screen_size()


# ── Gesture execution (fast path) ─────────────────────────────────────────────

@app.post("/api/tap")
async def api_tap(req: Coords):
    asyncio.create_task(wda.tap(req.x, req.y))
    return {"ok": True}


@app.post("/api/double_tap")
async def api_double_tap(req: Coords):
    asyncio.create_task(wda.double_tap(req.x, req.y))
    return {"ok": True}


@app.post("/api/triple_tap")
async def api_triple_tap(req: Coords):
    asyncio.create_task(wda.triple_tap(req.x, req.y))
    return {"ok": True}


@app.post("/api/long_press")
async def api_long_press(req: LongPressReq):
    asyncio.create_task(wda.long_press(req.x, req.y, req.duration))
    return {"ok": True}


@app.post("/api/two_finger_tap")
async def api_two_finger_tap(req: Coords):
    asyncio.create_task(wda.two_finger_tap(req.x, req.y))
    return {"ok": True}


@app.post("/api/multi_finger_tap")
async def api_multi_finger_tap(req: MultiFingerTapReq):
    asyncio.create_task(wda.multi_finger_tap(req.x, req.y, req.fingers))
    return {"ok": True}


@app.post("/api/scroll")
async def api_scroll(req: ScrollReq):
    asyncio.create_task(wda.scroll(req.x1, req.y1, req.x2, req.y2, req.duration))
    return {"ok": True}


@app.post("/api/pinch")
async def api_pinch(req: PinchReq):
    asyncio.create_task(wda.pinch(req.x, req.y, req.scale, req.spread))
    return {"ok": True}


@app.post("/api/rotate")
async def api_rotate(req: RotateReq):
    wda_dur = max(300, min(800, int(abs(req.rotation) / 180 * 800)))
    asyncio.create_task(wda.rotate(req.x, req.y, req.rotation, req.spread, wda_dur))
    return {"ok": True}


@app.post("/api/type_text")
async def api_type_text(req: TypeTextReq):
    asyncio.create_task(wda.type_text(req.text))
    return {"ok": True}


@app.post("/api/home")
async def api_home():
    asyncio.create_task(wda.press_home())
    return {"ok": True}


@app.post("/api/launch_app")
async def api_launch_app(req: LaunchAppReq):
    asyncio.create_task(wda.launch_app(req.bundle_id))
    return {"ok": True}


@app.get("/api/apps")
async def api_apps():
    return _load_apps()


@app.get("/api/element_info")
async def api_element_info(x: float, y: float):
    """Return selector + text + bounds of the topmost element at (x, y)."""
    root = await _cached_tree(force=True)
    if root is None:
        return {"found": False}
    from .hittest import _rect
    el = hit_test(x, y, root)
    if el is None:
        return {"found": False}
    sel_type, sel_val = build_selector(el)
    a = el.attrib
    text = a.get("value", "") or a.get("label", "") or a.get("name", "")
    r = _rect(el)
    bounds = {"x": r[0], "y": r[1], "w": r[2], "h": r[3]} if r else None
    return {"found": True, "type": sel_type, "value": sel_val, "text": text, "bounds": bounds}


@app.post("/api/swipe")
async def api_swipe(req: SwipeReq):
    asyncio.create_task(wda.swipe(req.x1, req.y1, req.x2, req.y2, req.duration))
    return {"ok": True}


@app.post("/api/drag")
async def api_drag(req: DragReq):
    asyncio.create_task(wda.drag(req.x1, req.y1, req.x2, req.y2, req.duration))
    return {"ok": True}


# ── Recording (async path) ────────────────────────────────────────────────────

@app.post("/api/record")
async def record_tap(req: Coords):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_point("tap", req.x, req.y, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/double_tap")
async def record_double_tap(req: Coords):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_point("double_tap", req.x, req.y, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/triple_tap")
async def record_triple_tap(req: Coords):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_point("triple_tap", req.x, req.y, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/long_press")
async def record_long_press(req: LongPressReq):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_long_press(req.x, req.y, req.duration, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/two_finger_tap")
async def record_two_finger_tap(req: Coords):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_point("two_finger_tap", req.x, req.y, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/multi_finger_tap")
async def record_multi_finger_tap(req: MultiFingerTapReq):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_multi_finger_tap(req.x, req.y, req.fingers, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/pinch")
async def record_pinch(req: PinchReq):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_pinch(req.x, req.y, req.scale, req.spread, duration=req.duration, snapshot=snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/rotate")
async def record_rotate(req: RotateReq):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_rotate(req.x, req.y, req.rotation, req.spread, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/type_text")
async def record_type_text(req: TypeTextReq):
    snapshot = _cache.get("root")
    asyncio.create_task(_record_type_text(req.text, req.target_x, req.target_y, snapshot))
    return {"ok": True}


@app.post("/api/record/home")
async def record_home():
    asyncio.create_task(_record_simple("home"))
    return {"ok": True}


@app.post("/api/record/launch_app")
async def record_launch_app(req: LaunchAppReq):
    asyncio.create_task(_record_launch_app(req.bundle_id))
    return {"ok": True}


@app.post("/api/record/verify_visible")
async def record_verify_visible(req: VerifyVisibleReq):
    snapshot = _cache.get("root") if req.not_visible else None
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_verify_visible(req.target_x, req.target_y, req.not_visible, snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/verify_get_text")
async def record_verify_get_text(req: VerifyGetTextReq):
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_verify_get_text(req.target_x, req.target_y, req.expected_text, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/verify_screenshot_gt")
async def record_verify_screenshot_gt(req: VerifyScreenshotGtReq):
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_verify_screenshot_gt(req.target_x, req.target_y, req.screenshot_name, req.bounds, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/verify_screenshot_diff")
async def record_verify_screenshot_diff(req: VerifyScreenshotDiffReq):
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_verify_screenshot_diff(req.target_x, req.target_y, req.bounds, req.phase, req.expected_result, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/scroll")
async def record_scroll(req: ScrollReq):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_scroll(req.x1, req.y1, req.x2, req.y2, req.duration, snapshot=snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/scroll_target")
async def record_scroll_target(req: Coords):
    asyncio.create_task(_record_scroll_target(req.x, req.y))
    return {"ok": True}


@app.post("/api/record/swipe_target")
async def record_swipe_target(req: Coords):
    asyncio.create_task(_record_swipe_target(req.x, req.y))
    return {"ok": True}


@app.post("/api/record/swipe")
async def record_swipe(req: SwipeReq):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_move("swipe", req.x1, req.y1, req.x2, req.y2, req.duration, snapshot=snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


@app.post("/api/record/drag")
async def record_drag(req: DragReq):
    snapshot = _cache.get("root")
    pre_ss = await _take_pre_gesture_screenshot()
    asyncio.create_task(_record_drag(req.x1, req.y1, req.x2, req.y2, req.duration, snapshot=snapshot, pre_screenshot=pre_ss))
    return {"ok": True}


# ── Recording helpers ──────────────────────────────────────────────────────────

def _build_target(x: float, y: float, el) -> dict:
    """Build step target dict with selector + offset_pct + quality + bounds + xpath."""
    sel_type, sel_val = build_selector(el)
    target: dict = {
        "type": sel_type,
        "value": sel_val,
        "selector_quality": get_selector_quality(el),
        "xpath": build_xpath(el),
    }
    r = _el_rect(el)
    if r:
        ex, ey, ew, eh = r
        target["offset_pct"] = {
            "x": max(0.0, min(100.0, round((x - ex) / ew * 100, 1))),
            "y": max(0.0, min(100.0, round((y - ey) / eh * 100, 1))),
        }
        target["bounds"] = {"x": int(ex), "y": int(ey), "w": int(ew), "h": int(eh)}
    return target


async def _take_pre_gesture_screenshot() -> Optional[str]:
    """Capture the current screen state BEFORE the gesture fires.

    Cancels any in-flight source-tree fetch and temporarily blocks new
    ones so WDA processes the screenshot request immediately (WDA
    handles HTTP requests serially — a queued source fetch would delay
    the screenshot by 1-5 s, during which the UI may settle into a
    different state).
    """
    # Cancel any concurrent get_source() to free up WDA
    if wda._source_task is not None and not wda._source_task.done():
        wda._source_task.cancel()
        wda._source_task = None
        logger.debug("Cancelled in-flight source fetch for screenshot priority")
    # Block new source requests while capturing
    prev_flag = wda._action_in_progress
    wda._action_in_progress = True
    try:
        b64 = await wda.get_screenshot()
        return b64.strip() if b64 else None
    finally:
        wda._action_in_progress = prev_flag


async def _record_point(action: str, x: float, y: float, snapshot=None, pre_screenshot: Optional[str] = None):
    global _last_tap_target
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": action, "coords": {"x": x, "y": y}, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        step["target"] = _build_target(x, y, el) if el is not None else {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    if action == "tap":
        _last_tap_target = step["target"]
    _steps.append(step)
    logger.info(f"Recorded {action}: {step.get('target')}")


async def _record_long_press(x: float, y: float, duration: int, snapshot=None, pre_screenshot: Optional[str] = None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "long_press", "coords": {"x": x, "y": y}, "duration": duration, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        step["target"] = _build_target(x, y, el) if el is not None else {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded long_press: {step.get('target')}")


async def _record_multi_finger_tap(x: float, y: float, fingers: int, snapshot=None, pre_screenshot: Optional[str] = None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "multi_finger_tap", "coords": {"x": x, "y": y}, "fingers": fingers, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        step["target"] = _build_target(x, y, el) if el is not None else {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded multi_finger_tap({fingers}): {step.get('target')}")


async def _record_pinch(x: float, y: float, scale: float, spread: int, duration: int = 500, snapshot=None, pre_screenshot: Optional[str] = None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "pinch", "coords": {"x": x, "y": y}, "scale": scale, "spread": spread, "duration": duration, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            t: dict = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            r = _el_rect(el)
            if r:
                t["bounds"] = {"x": int(r[0]), "y": int(r[1]), "w": int(r[2]), "h": int(r[3])}
            step["target"] = t
        else:
            step["target"] = {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded pinch (scale={scale:.2f}): {step.get('target')}")


async def _record_rotate(x: float, y: float, rotation: float, spread: int, snapshot=None, pre_screenshot: Optional[str] = None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "rotate", "coords": {"x": x, "y": y}, "rotation": rotation, "spread": spread, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            t: dict = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            r = _el_rect(el)
            if r:
                t["bounds"] = {"x": int(r[0]), "y": int(r[1]), "w": int(r[2]), "h": int(r[3])}
            step["target"] = t
        else:
            step["target"] = {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded rotate ({rotation:.1f}°): {step.get('target')}")


async def _record_scroll(x1: float, y1: float, x2: float, y2: float, duration: int, snapshot=None, pre_screenshot: Optional[str] = None):
    root = snapshot if snapshot is not None else await _cached_tree()
    scroll_container: dict | None = None
    scroll_offsets: dict | None = None
    if root is not None:
        el = find_scroll_container(x1, y1, root)
        if el is not None:
            sel_type, sel_val = build_scroll_container_selector(el, root)
            scroll_container = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            r = _el_rect(el)
            if r and r[2] > 0 and r[3] > 0:
                el_x, el_y, el_w, el_h = r
                scroll_offsets = {
                    "start_x_pct": round(max(0.0, min(1.0, (x1 - el_x) / el_w)), 3),
                    "start_y_pct": round(max(0.0, min(1.0, (y1 - el_y) / el_h)), 3),
                    "end_x_pct":   round(max(0.0, min(1.0, (x2 - el_x) / el_w)), 3),
                    "end_y_pct":   round(max(0.0, min(1.0, (y2 - el_y) / el_h)), 3),
                }

    step: dict = {
        "action": "scroll",
        "coords": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
        "duration": duration,
        "timestamp": time.time(),
    }
    if scroll_container:
        step["scroll_container"] = scroll_container
    if scroll_offsets:
        step["scroll_offsets"] = scroll_offsets
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded scroll: ({x1},{y1}) → ({x2},{y2}), container={scroll_container}")


async def _record_scroll_target(x: float, y: float):
    await asyncio.sleep(0.1)
    root = await _cached_tree()

    # Build scroll_target value
    scroll_target: dict
    if root is not None:
        el = hit_test(x, y, root)
        if el is not None:
            sel_type, sel_val = build_scroll_container_selector(el, root)
            scroll_target = {"type": sel_type, "value": sel_val}
        else:
            scroll_target = {"type": "coordinate", "x": x, "y": y}
    else:
        scroll_target = {"type": "coordinate", "x": x, "y": y}

    # Find the last scroll step index
    last_scroll_idx = None
    for i in range(len(_steps) - 1, -1, -1):
        if _steps[i].get("action") == "scroll":
            last_scroll_idx = i
            break

    if last_scroll_idx is None:
        return

    # Remove all consecutive scroll steps before the last one
    first_scroll_idx = last_scroll_idx
    while first_scroll_idx > 0 and _steps[first_scroll_idx - 1].get("action") == "scroll":
        first_scroll_idx -= 1

    if first_scroll_idx < last_scroll_idx:
        del _steps[first_scroll_idx:last_scroll_idx]
        last_scroll_idx = first_scroll_idx

    _steps[last_scroll_idx]["scroll_target"] = scroll_target
    logger.info(f"Updated last scroll target (removed {last_scroll_idx - first_scroll_idx} preceding scrolls)")


async def _record_swipe_target(x: float, y: float):
    await asyncio.sleep(0.1)
    root = await _cached_tree()
    for i in range(len(_steps) - 1, -1, -1):
        if _steps[i].get("action") == "swipe":
            if root is not None:
                el = hit_test(x, y, root)
                if el is not None:
                    sel_type, sel_val = build_selector(el)
                    _steps[i]["swipe_target"] = {"type": sel_type, "value": sel_val}
                else:
                    _steps[i]["swipe_target"] = {"type": "coordinate", "x": x, "y": y}
            break
    logger.info("Updated last swipe target")


async def _record_type_text(text: str, tx: Optional[float], ty: Optional[float], snapshot=None):
    step: dict = {"action": "type_text", "text": text, "timestamp": time.time()}
    # Prefer the last-tapped element target — avoids iOS updating the text field's
    # `name` attribute to the typed text before we can run hit_test.
    if _last_tap_target is not None and _last_tap_target.get("type") != "coordinate":
        step["target"] = _last_tap_target
    elif tx is not None and ty is not None:
        root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
        if root is not None:
            el = hit_test(tx, ty, root)
            if el is not None:
                sel_type, sel_val = build_selector(el)
                step["target"] = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            else:
                step["target"] = {"type": "coordinate", "x": tx, "y": ty}
        else:
            step["target"] = {"type": "coordinate", "x": tx, "y": ty}
    _steps.append(step)
    logger.info(f"Recorded type_text: {text!r}")


async def _record_simple(action: str):
    step: dict = {"action": action, "timestamp": time.time()}
    _steps.append(step)
    logger.info(f"Recorded {action}")


async def _record_launch_app(bundle_id: str):
    apps = _load_apps()
    name = next((a["name"] for a in apps if a["bundle_id"] == bundle_id), bundle_id)
    step: dict = {"action": "launch_app", "bundle_id": bundle_id, "app_name": name, "timestamp": time.time()}
    _steps.append(step)
    logger.info(f"Recorded launch_app: {bundle_id}")


async def _record_verify_visible(tx: float, ty: float, not_visible: bool, snapshot=None, pre_screenshot: Optional[str] = None):
    action = "verify_not_visible" if not_visible else "verify_visible"
    step: dict = {"action": action, "coords": {"x": tx, "y": ty}, "timestamp": time.time()}
    if not_visible and snapshot is not None:
        # Use pre-action snapshot so the element is captured before it disappears
        el = hit_test(tx, ty, snapshot)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            t: dict = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            r = _el_rect(el)
            if r:
                t["bounds"] = {"x": int(r[0]), "y": int(r[1]), "w": int(r[2]), "h": int(r[3])}
            step["target"] = t
        else:
            step["target"] = {"type": "coordinate", "x": tx, "y": ty}
    else:
        await asyncio.sleep(0.1)
        root = await _cached_tree()
        if root is not None:
            el = hit_test(tx, ty, root)
            if el is not None:
                sel_type, sel_val = build_selector(el)
                t2: dict = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
                r = _el_rect(el)
                if r:
                    t2["bounds"] = {"x": int(r[0]), "y": int(r[1]), "w": int(r[2]), "h": int(r[3])}
                step["target"] = t2
            else:
                step["target"] = {"type": "coordinate", "x": tx, "y": ty}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded {action}")


async def _record_verify_get_text(tx: float, ty: float, expected_text: str, pre_screenshot: Optional[str] = None):
    await asyncio.sleep(0.1)
    step: dict = {"action": "verify_get_text", "coords": {"x": tx, "y": ty},
                  "expected_text": expected_text, "timestamp": time.time()}
    root = await _cached_tree()
    if root is not None:
        el = hit_test(tx, ty, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            t: dict = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            r = _el_rect(el)
            if r:
                t["bounds"] = {"x": int(r[0]), "y": int(r[1]), "w": int(r[2]), "h": int(r[3])}
            step["target"] = t
        else:
            step["target"] = {"type": "coordinate", "x": tx, "y": ty}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded verify_get_text: {expected_text!r}")


async def _record_verify_screenshot_gt(tx: float, ty: float, screenshot_name: str, bounds: dict, pre_screenshot: Optional[str] = None):
    await asyncio.sleep(0.1)
    step: dict = {"action": "verify_screenshot_gt", "coords": {"x": tx, "y": ty},
                  "screenshot_name": screenshot_name, "bounds": bounds, "timestamp": time.time()}
    root = await _cached_tree()
    if root is not None:
        el = hit_test(tx, ty, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            t: dict = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            r = _el_rect(el)
            if r:
                t["bounds"] = {"x": int(r[0]), "y": int(r[1]), "w": int(r[2]), "h": int(r[3])}
            step["target"] = t
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded verify_screenshot_gt: {screenshot_name}")


async def _record_verify_screenshot_diff(tx: float, ty: float, bounds: dict, phase: str = "before", expected_result: str = "same", pre_screenshot: Optional[str] = None):
    await asyncio.sleep(0.1)
    step: dict = {"action": "verify_screenshot_diff", "phase": phase,
                  "coords": {"x": tx, "y": ty}, "bounds": bounds, "timestamp": time.time()}
    if phase == "after":
        step["expected_result"] = expected_result
    root = await _cached_tree()
    if root is not None:
        el = hit_test(tx, ty, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            t: dict = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
            r = _el_rect(el)
            if r:
                t["bounds"] = {"x": int(r[0]), "y": int(r[1]), "w": int(r[2]), "h": int(r[3])}
            step["target"] = t
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded verify_screenshot_diff ({phase}, expected={expected_result})")


async def _record_move(action: str, x1: float, y1: float, x2: float, y2: float, duration: int, extra: dict = None, snapshot=None, pre_screenshot: Optional[str] = None):
    root = snapshot if snapshot is not None else await _cached_tree()
    step: dict = {
        "action": action,
        "coords": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
        "duration": duration,
        "timestamp": time.time(),
    }
    if extra:
        step.update(extra)
    # Pre-compute direction and velocity for swipe so the UI and export JSON
    # show them without needing to re-derive at codegen time.
    if action == "swipe":
        dx, dy = x2 - x1, y2 - y1
        if abs(dx) > abs(dy):
            step["direction"] = "right" if dx > 0 else "left"
        else:
            step["direction"] = "down" if dy < 0 else "up"
        raw_dist = (dx ** 2 + dy ** 2) ** 0.5
        step["velocity"] = round(max(50.0, min(5000.0, raw_dist * 1000 / duration)), 1) if duration > 0 else 500.0
    if root is not None:
        el = hit_test_for_swipe(x1, y1, root) if action == "swipe" else hit_test(x1, y1, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["start_target"] = {"type": sel_type, "value": sel_val, "selector_quality": get_selector_quality(el)}
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded {action}: {step.get('start_target', step['coords'])}")


async def _record_drag(x1: float, y1: float, x2: float, y2: float, duration: int, snapshot=None, pre_screenshot: Optional[str] = None):
    root = snapshot if snapshot is not None else await _cached_tree()
    step: dict = {
        "action": "drag",
        "coords": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
        "duration": duration,
        "timestamp": time.time(),
    }
    if root is not None:
        # Find the element being dragged (source)
        start_el = hit_test(x1, y1, root)
        if start_el is not None:
            step["start_target"] = _build_target(x1, y1, start_el)
            # Find the drop target: exclude source subtree AND deprioritise
            # elements of the same tag (e.g. another image in a gallery)
            # so we land on the container/slot instead
            end_el = hit_test_drop_target(x2, y2, root, start_el)
        else:
            end_el = hit_test(x2, y2, root)
        if end_el is not None:
            step["end_target"] = _build_target(x2, y2, end_el)
    if pre_screenshot:
        step["pre_screenshot"] = pre_screenshot
        step["pre_screenshot_size"] = dict(wda._last_screen_size)
    _steps.append(step)
    logger.info(f"Recorded drag: {step.get('start_target')} → {step.get('end_target')}")


async def _cached_tree(force: bool = False):
    now = time.time()
    if not force and _cache["root"] and now - _cache["ts"] < CACHE_TTL:
        return _cache["root"]
    # Even with force, skip re-fetch if cache is very recent — avoids
    # saturating WDA with back-to-back source requests that block
    # gesture commands (tap, rotate, etc.).
    if force and _cache["root"] and now - _cache["ts"] < 4.0:
        return _cache["root"]
    root = await wda.get_source()
    if root is not None:
        _cache["root"] = root
        _cache["ts"] = now
    return _cache.get("root")


# ── Steps ──────────────────────────────────────────────────────────────────────

_STRIP_STEP_KEYS = frozenset({"pre_screenshot", "pre_screenshot_size"})


@app.get("/api/steps")
async def get_steps():
    stripped = [{k: v for k, v in s.items() if k not in _STRIP_STEP_KEYS} for s in _steps]
    return {"steps": stripped}


@app.delete("/api/steps")
async def clear_steps():
    global _last_tap_target
    _steps.clear()
    _last_tap_target = None
    return {"ok": True}


# ── UI Tree ────────────────────────────────────────────────────────────────────

@app.get("/api/tree")
async def get_tree():
    root = await _cached_tree(force=True)
    if root is None:
        return JSONResponse({"error": "Cannot reach WDA"}, status_code=503)
    return {"elements": serialize(root)}


# ── MJPEG proxy ────────────────────────────────────────────────────────────────

@app.get("/api/stream")
async def stream_proxy():
    async def gen():
        url = wda.mjpeg_url or f"{wda.base_url}/mjpeg"
        while True:
            try:
                async with httpx.AsyncClient() as c:
                    async with c.stream("GET", url, timeout=None) as r:
                        async for chunk in r.aiter_bytes(4096):
                            yield chunk
            except Exception as e:
                logger.warning(f"MJPEG stream disconnected: {e!r}")
            await asyncio.sleep(1.0)
    return StreamingResponse(gen(), media_type="multipart/x-mixed-replace; boundary=BoundaryString")


# ── WebSocket (lowest latency) ─────────────────────────────────────────────────

@app.websocket("/ws/tap")
async def ws_handler(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_json()
            t = data.get("type", "tap")
            rec = data.get("record", False)

            if t == "tap":
                x, y = float(data["x"]), float(data["y"])
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.tap(x, y)
                    asyncio.create_task(_record_point("tap", x, y, snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.tap(x, y))

            elif t == "double_tap":
                x, y = float(data["x"]), float(data["y"])
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.double_tap(x, y)
                    asyncio.create_task(_record_point("double_tap", x, y, snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.double_tap(x, y))

            elif t == "triple_tap":
                x, y = float(data["x"]), float(data["y"])
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.triple_tap(x, y)
                    asyncio.create_task(_record_point("triple_tap", x, y, snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.triple_tap(x, y))

            elif t == "long_press":
                x, y = float(data["x"]), float(data["y"])
                dur = int(data.get("duration", 1000))
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.long_press(x, y, dur)
                    asyncio.create_task(_record_long_press(x, y, dur, snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.long_press(x, y, dur))

            elif t == "two_finger_tap":
                x, y = float(data["x"]), float(data["y"])
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.two_finger_tap(x, y)
                    asyncio.create_task(_record_point("two_finger_tap", x, y, snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.two_finger_tap(x, y))

            elif t == "multi_finger_tap":
                x, y = float(data["x"]), float(data["y"])
                fingers = int(data.get("fingers", 3))
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.multi_finger_tap(x, y, fingers)
                    asyncio.create_task(_record_multi_finger_tap(x, y, fingers, snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.multi_finger_tap(x, y, fingers))

            elif t == "pinch":
                x, y = float(data["x"]), float(data["y"])
                scale = float(data.get("scale", 0.5))
                spread = int(data.get("spread", 80))
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.pinch(x, y, scale, spread)
                    asyncio.create_task(_record_pinch(x, y, scale, spread, snapshot=snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.pinch(x, y, scale, spread))

            elif t == "rotate":
                x, y = float(data["x"]), float(data["y"])
                rotation = float(data.get("rotation", 45.0))
                spread = int(data.get("spread", 80))
                snapshot = _cache.get("root")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                # Execution duration based on angle (not UI drag time): 300–800 ms
                wda_dur = max(300, min(800, int(abs(rotation) / 180 * 800)))
                if rec:
                    await wda.rotate(x, y, rotation, spread, wda_dur)
                    asyncio.create_task(_record_rotate(x, y, rotation, spread, snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.rotate(x, y, rotation, spread, wda_dur))

            elif t == "scroll":
                x1, y1, x2, y2 = float(data["x1"]), float(data["y1"]), float(data["x2"]), float(data["y2"])
                dur = int(data.get("duration", 600))
                snapshot = _cache.get("root") if rec else None
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.scroll(x1, y1, x2, y2, dur)
                    asyncio.create_task(_record_scroll(x1, y1, x2, y2, dur, snapshot=snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.scroll(x1, y1, x2, y2, dur))

            elif t == "update_scroll_target":
                x, y = float(data["x"]), float(data["y"])
                asyncio.create_task(_record_scroll_target(x, y))

            elif t == "swipe":
                x1, y1, x2, y2 = float(data["x1"]), float(data["y1"]), float(data["x2"]), float(data["y2"])
                dur = int(data.get("duration", 400))
                direction = data.get("direction", "up")
                snapshot = _cache.get("root") if rec else None
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.swipe(x1, y1, x2, y2, dur)
                    step_extra = {"direction": direction}
                    asyncio.create_task(_record_move("swipe", x1, y1, x2, y2, dur, extra=step_extra, snapshot=snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.swipe(x1, y1, x2, y2, dur))

            elif t == "update_swipe_target":
                x, y = float(data["x"]), float(data["y"])
                asyncio.create_task(_record_swipe_target(x, y))

            elif t == "drag":
                x1, y1, x2, y2 = float(data["x1"]), float(data["y1"]), float(data["x2"]), float(data["y2"])
                dur = int(data.get("duration", 1000))
                snapshot = _cache.get("root") if rec else None
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec:
                    await wda.drag(x1, y1, x2, y2, dur)
                    asyncio.create_task(_record_drag(x1, y1, x2, y2, dur, snapshot=snapshot, pre_screenshot=pre_ss))
                else:
                    asyncio.create_task(wda.drag(x1, y1, x2, y2, dur))

            elif t == "type_text":
                text = data.get("text", "")
                tx = data.get("target_x")
                ty = data.get("target_y")
                snapshot = _cache.get("root")
                if rec:
                    await wda.type_text(text)
                    asyncio.create_task(_record_type_text(
                        text,
                        float(tx) if tx is not None else None,
                        float(ty) if ty is not None else None,
                        snapshot,
                    ))
                else:
                    asyncio.create_task(wda.type_text(text))

            elif t == "home":
                if rec:
                    await wda.press_home()
                    asyncio.create_task(_record_simple("home"))
                else:
                    asyncio.create_task(wda.press_home())

            elif t == "launch_app":
                bundle_id = data.get("bundle_id", "")
                if rec:
                    await wda.launch_app(bundle_id)
                    asyncio.create_task(_record_launch_app(bundle_id))
                else:
                    asyncio.create_task(wda.launch_app(bundle_id))

            elif t == "verify_visible":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                not_vis = bool(data.get("not_visible", False))
                snapshot = _cache.get("root") if not_vis else None
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec: asyncio.create_task(_record_verify_visible(tx, ty, not_vis, snapshot, pre_screenshot=pre_ss))

            elif t == "verify_get_text":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                expected = data.get("expected_text", "")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec: asyncio.create_task(_record_verify_get_text(tx, ty, expected, pre_screenshot=pre_ss))

            elif t == "verify_screenshot_gt":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                name = data.get("screenshot_name", "")
                bounds = data.get("bounds", {})
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec: asyncio.create_task(_record_verify_screenshot_gt(tx, ty, name, bounds, pre_screenshot=pre_ss))

            elif t == "verify_screenshot_diff":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                bounds = data.get("bounds", {})
                phase = data.get("phase", "before")
                expected_result = data.get("expected_result", "same")
                pre_ss = await _take_pre_gesture_screenshot() if rec else None
                if rec: asyncio.create_task(_record_verify_screenshot_diff(tx, ty, bounds, phase, expected_result, pre_screenshot=pre_ss))

            await ws.send_json({"ok": True})
    except (WebSocketDisconnect, Exception):
        pass


# ── Export ─────────────────────────────────────────────────────────────────────

_PROJECT_ROOT   = Path(__file__).parent.parent
_EXPORT_DIR     = _PROJECT_ROOT / "export"
_PYTEST_TESTS   = _PROJECT_ROOT / "pytest" / "tests"

class ExportReq(BaseModel):
    case_name: str = ""


_QUALITY_LABELS = {
    "id":          ("ID",           "#555",    "Has proper accessibility ID (most stable)"),
    "id_indexed":  ("ID -N",        "#f1c40f", "Accessibility ID ends with -<digits> (e.g. Cell-3) — index may shift"),
    "id_eq_label": ("ID = Label",   "#4a9eff", "Accessibility ID equals label — may be fragile if label text changes"),
    "label_only":  ("Label Only",   "#ffb86c", "No stable ID; found by label attribute — fragile if text changes"),
    "xpath_only":  ("XPath Only",   "#ff5555", "No ID or label; XPath fallback — will break if UI structure changes"),
    "coordinate":  ("Coord Only",   "#888888", "No element matched — action recorded at raw coordinates"),
}


def _generate_html_report(steps: list, case_name: str) -> str:
    """Generate a self-contained HTML selector-quality report with per-step screenshots."""
    exported_at = time.strftime("%Y-%m-%dT%H:%M:%S")

    # Collect warning steps — check all possible element target keys
    warn_steps = []
    for i, s in enumerate(steps):
        primary = s.get("target") or s.get("start_target") or s.get("scroll_container")
        if not primary:
            continue
        if primary.get("type") == "coordinate":
            warn_steps.append((i + 1, s, primary, "coordinate"))
        elif primary.get("selector_quality", "") in _WARN_QUALITIES:
            warn_steps.append((i + 1, s, primary, primary.get("selector_quality", "")))

    # ── Legend rows ──────────────────────────────────────────────────────────
    legend_html = ""
    for q, (label, color, desc) in _QUALITY_LABELS.items():
        if q == "id":
            continue
        legend_html += (
            f'<div class="leg-row">'
            f'<span class="leg-dot" style="background:{color}"></span>'
            f'<strong style="color:{color}">{label}</strong>'
            f'<span class="leg-desc">{desc}</span>'
            f'</div>\n'
        )

    # ── Per-step cards ───────────────────────────────────────────────────────
    if warn_steps:
        cards_html = f'<h2>Steps with Selector Warnings ({len(warn_steps)})</h2>\n'
        for step_n, s, primary, q in warn_steps:
            label, color, _ = _QUALITY_LABELS.get(q, ("?", "#888", ""))
            bounds = primary.get("bounds")
            bounds_str = (
                f"({bounds['x']},{bounds['y']}) {bounds['w']}×{bounds['h']}"
                if bounds else "—"
            )
            pre_ss = s.get("pre_screenshot")
            ss_size = s.get("pre_screenshot_size", {})
            sw = ss_size.get("width", 390)
            sh = ss_size.get("height", 844)

            # Screenshot with bounding box / crosshair overlay
            if pre_ss and bounds:
                bx, by, bw, bh = bounds["x"], bounds["y"], bounds["w"], bounds["h"]
                img_html = f"""<div class="img-wrap">
  <img src="data:image/png;base64,{pre_ss}" style="display:block;max-width:100%;height:auto">
  <svg style="position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none"
       viewBox="0 0 {sw} {sh}" preserveAspectRatio="none">
    <rect x="{bx}" y="{by}" width="{bw}" height="{bh}"
          fill="{color}33" stroke="{color}" stroke-width="3" rx="4"/>
  </svg>
</div>"""
            elif pre_ss and q == "coordinate":
                cx_val = int(primary.get("x") or s.get("coords", {}).get("x", sw // 2))
                cy_val = int(primary.get("y") or s.get("coords", {}).get("y", sh // 2))
                img_html = f"""<div class="img-wrap">
  <img src="data:image/png;base64,{pre_ss}" style="display:block;max-width:100%;height:auto">
  <svg style="position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none"
       viewBox="0 0 {sw} {sh}" preserveAspectRatio="none">
    <circle cx="{cx_val}" cy="{cy_val}" r="20" fill="{color}33" stroke="{color}" stroke-width="3"/>
    <line x1="{cx_val-12}" y1="{cy_val}" x2="{cx_val+12}" y2="{cy_val}" stroke="{color}" stroke-width="2"/>
    <line x1="{cx_val}" y1="{cy_val-12}" x2="{cx_val}" y2="{cy_val+12}" stroke="{color}" stroke-width="2"/>
  </svg>
</div>"""
            elif pre_ss:
                img_html = f'<div class="img-wrap"><img src="data:image/png;base64,{pre_ss}" style="display:block;max-width:100%;height:auto"></div>'
            else:
                img_html = '<p class="no-img">No pre-gesture screenshot available — re-record to capture</p>'

            if q == "coordinate":
                cx_disp = int(primary.get("x") or s.get("coords", {}).get("x", 0))
                cy_disp = int(primary.get("y") or s.get("coords", {}).get("y", 0))
                sel_html = f'<span class="step-sel"><code>coordinate</code> = <code>({cx_disp},{cy_disp})</code></span>'
            else:
                sel_html = f'<span class="step-sel"><code>{primary.get("type","")}</code> = <code>{primary.get("value","")}</code></span>'

            cards_html += f"""<div class="step-card" style="border-left-color:{color}">
  <div class="step-hd">
    <span class="step-num">#{step_n}</span>
    <code class="step-action">{s['action']}</code>
    <span class="badge" style="background:{color}22;color:{color};border:1px solid {color}">{label}</span>
    {sel_html}
    <span class="step-bounds">{bounds_str}</span>
  </div>
  {img_html}
</div>
"""
    else:
        cards_html = "<p class='ok'>All steps use stable selectors.</p>"

    summary_color = "#ff5555" if warn_steps else "#50fa7b"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Selector Quality Report — {case_name}</title>
<style>
  body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
       background:#141414;color:#ddd;margin:0;padding:24px;line-height:1.5}}
  h1{{color:#4a9eff;margin-bottom:4px}}
  h2{{color:#aaa;font-size:15px;text-transform:uppercase;letter-spacing:.7px;
      margin:28px 0 10px;border-bottom:1px solid #333;padding-bottom:4px}}
  p.ok{{color:#50fa7b;font-size:14px}}
  p.no-img{{color:#555;font-size:13px;font-style:italic;margin:8px 0}}
  .meta{{color:#777;font-size:13px;margin-bottom:20px}}
  .summary{{display:inline-block;padding:6px 14px;border-radius:6px;
            font-size:13px;font-weight:700;color:{summary_color};
            background:{summary_color}22;border:1px solid {summary_color};margin-bottom:20px}}
  .leg-row{{display:flex;align-items:flex-start;gap:10px;margin-bottom:8px;font-size:14px}}
  .leg-dot{{width:14px;height:14px;border-radius:50%;flex-shrink:0;margin-top:3px}}
  .leg-desc{{color:#888;font-size:13px}}
  .step-card{{background:#1a1a1a;border:1px solid #2a2a2a;border-left:4px solid #555;
              border-radius:8px;margin-bottom:20px;overflow:hidden}}
  .step-hd{{display:flex;align-items:center;flex-wrap:wrap;gap:8px;
            padding:10px 14px;background:#1e1e1e;border-bottom:1px solid #2a2a2a}}
  .step-num{{font-weight:700;font-size:14px;color:#aaa;min-width:28px}}
  .step-action{{font-size:13px;color:#e0e0e0;background:#2a2a2a;
                padding:2px 7px;border-radius:4px}}
  .step-sel{{font-size:12px;color:#888;margin-left:4px}}
  .step-bounds{{font-size:11px;color:#555;margin-left:auto}}
  .badge{{display:inline-block;padding:2px 8px;border-radius:4px;
          font-size:12px;font-weight:700;white-space:nowrap}}
  code{{font-family:monospace;font-size:13px;color:#ccc}}
  .img-wrap{{position:relative;display:inline-block;max-width:100%;margin:14px}}
  img{{border-radius:12px;box-shadow:0 0 0 1px #333,0 8px 32px rgba(0,0,0,.6)}}
</style>
</head>
<body>
<h1>Selector Quality Report</h1>
<div class="meta">Case: <strong>{case_name}</strong> &nbsp;|&nbsp; Exported: {exported_at}</div>
<div class="summary">{len(warn_steps)} of {len(steps)} steps have selector warnings</div>

<h2>Legend</h2>
{legend_html}

{cards_html}
</body>
</html>"""


@app.post("/api/export")
async def export_script(req: ExportReq):
    ts = time.strftime("%Y%m%d_%H%M%S")
    # Append timestamp to both the display name and the safe identifier
    stamped_name = f"{req.case_name}_{ts}" if req.case_name else ts
    script = generate_script(_steps, stamped_name)
    safe = "".join(c if c.isalnum() or c == "_" else "_" for c in stamped_name).strip("_")
    safe = safe or f"recorded_{ts}"
    filename = f"test_{safe}.py"

    # Create a timestamped subfolder inside export/
    export_folder = _EXPORT_DIR / safe
    export_folder.mkdir(parents=True, exist_ok=True)
    _PYTEST_TESTS.mkdir(parents=True, exist_ok=True)

    # Write steps JSON (exclude embedded screenshot data — it inflates the file)
    json_filename = f"{safe}.json"
    steps_for_json = [{k: v for k, v in s.items() if k not in _STRIP_STEP_KEYS} for s in _steps]
    steps_payload = {
        "case_name": stamped_name,
        "exported_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "steps": steps_for_json,
    }
    (export_folder / json_filename).write_text(
        json.dumps(steps_payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Write pytest code to export subfolder and pytest/tests/
    (export_folder / filename).write_text(script, encoding="utf-8")
    (_PYTEST_TESTS / filename).write_text(script, encoding="utf-8")

    # Generate HTML report using per-step pre-gesture screenshots stored in _steps
    html_filename = f"{safe}.html"
    html_content = _generate_html_report(_steps, stamped_name)
    (export_folder / html_filename).write_text(html_content, encoding="utf-8")

    logger.info(f"Exported: {filename} → export/{safe}/ and pytest/tests/")
    return JSONResponse({
        "script": script,
        "filename": filename,
        "saved_paths": [
            f"pytest/tests/{filename}",
            f"export/{safe}/{filename}",
            f"export/{safe}/{json_filename}",
            f"export/{safe}/{html_filename}",
        ],
    })


# ── Static frontend ────────────────────────────────────────────────────────────

app.mount("/", StaticFiles(directory="static", html=True), name="static")
