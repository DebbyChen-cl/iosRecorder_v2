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
from .hittest import hit_test, find_scroll_container, build_scroll_container_selector, serialize, _rect as _el_rect
from .selector import build_selector
from .wda import WDAClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_CONFIG_FILE = Path(__file__).parent.parent / ".wda_config.json"
_APPS_FILE   = Path(__file__).parent.parent / "apps.json"


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


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(wda.connect())
    yield
    await wda.close()


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

class RotateReq(BaseModel):
    x: float
    y: float
    rotation: float  # degrees, positive = clockwise
    spread: int = 80

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

class ConfigIn(BaseModel):
    wda_url: str


# ── Status & Config ────────────────────────────────────────────────────────────

@app.get("/api/status")
async def status():
    alive, size = await asyncio.gather(
        wda.is_alive(),
        wda.get_screen_size(),
    )
    # Auto-recover: WDA is reachable but session was lost (e.g. after pytest/Appium)
    if alive and not wda._session_id:
        asyncio.create_task(wda._ensure_session())
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
    asyncio.create_task(wda.rotate(req.x, req.y, req.rotation, req.spread))
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
    asyncio.create_task(_record_point("tap", req.x, req.y))
    return {"ok": True}


@app.post("/api/record/double_tap")
async def record_double_tap(req: Coords):
    asyncio.create_task(_record_point("double_tap", req.x, req.y))
    return {"ok": True}


@app.post("/api/record/triple_tap")
async def record_triple_tap(req: Coords):
    asyncio.create_task(_record_point("triple_tap", req.x, req.y))
    return {"ok": True}


@app.post("/api/record/long_press")
async def record_long_press(req: LongPressReq):
    asyncio.create_task(_record_long_press(req.x, req.y, req.duration))
    return {"ok": True}


@app.post("/api/record/two_finger_tap")
async def record_two_finger_tap(req: Coords):
    asyncio.create_task(_record_point("two_finger_tap", req.x, req.y))
    return {"ok": True}


@app.post("/api/record/multi_finger_tap")
async def record_multi_finger_tap(req: MultiFingerTapReq):
    asyncio.create_task(_record_multi_finger_tap(req.x, req.y, req.fingers))
    return {"ok": True}


@app.post("/api/record/pinch")
async def record_pinch(req: PinchReq):
    asyncio.create_task(_record_pinch(req.x, req.y, req.scale, req.spread))
    return {"ok": True}


@app.post("/api/record/rotate")
async def record_rotate(req: RotateReq):
    asyncio.create_task(_record_rotate(req.x, req.y, req.rotation, req.spread))
    return {"ok": True}


@app.post("/api/record/type_text")
async def record_type_text(req: TypeTextReq):
    asyncio.create_task(_record_type_text(req.text, req.target_x, req.target_y))
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
    asyncio.create_task(_record_verify_visible(req.target_x, req.target_y, req.not_visible))
    return {"ok": True}


@app.post("/api/record/verify_get_text")
async def record_verify_get_text(req: VerifyGetTextReq):
    asyncio.create_task(_record_verify_get_text(req.target_x, req.target_y, req.expected_text))
    return {"ok": True}


@app.post("/api/record/verify_screenshot_gt")
async def record_verify_screenshot_gt(req: VerifyScreenshotGtReq):
    asyncio.create_task(_record_verify_screenshot_gt(req.target_x, req.target_y, req.screenshot_name, req.bounds))
    return {"ok": True}


@app.post("/api/record/verify_screenshot_diff")
async def record_verify_screenshot_diff(req: VerifyScreenshotDiffReq):
    asyncio.create_task(_record_verify_screenshot_diff(req.target_x, req.target_y, req.bounds, req.phase))
    return {"ok": True}


@app.post("/api/record/scroll")
async def record_scroll(req: ScrollReq):
    asyncio.create_task(_record_scroll(req.x1, req.y1, req.x2, req.y2, req.duration))
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
    asyncio.create_task(_record_move("swipe", req.x1, req.y1, req.x2, req.y2, req.duration))
    return {"ok": True}


@app.post("/api/record/drag")
async def record_drag(req: DragReq):
    asyncio.create_task(_record_move("drag", req.x1, req.y1, req.x2, req.y2, req.duration))
    return {"ok": True}


# ── Recording helpers ──────────────────────────────────────────────────────────

def _build_target(x: float, y: float, el) -> dict:
    """Build step target dict with selector + offset_pct within element bounds."""
    sel_type, sel_val = build_selector(el)
    target: dict = {"type": sel_type, "value": sel_val}
    r = _el_rect(el)
    if r:
        ex, ey, ew, eh = r
        target["offset_pct"] = {
            "x": max(0.0, min(100.0, round((x - ex) / ew * 100, 1))),
            "y": max(0.0, min(100.0, round((y - ey) / eh * 100, 1))),
        }
    return target


async def _record_point(action: str, x: float, y: float, snapshot=None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": action, "coords": {"x": x, "y": y}, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        step["target"] = _build_target(x, y, el) if el is not None else {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    _steps.append(step)
    logger.info(f"Recorded {action}: {step.get('target')}")


async def _record_long_press(x: float, y: float, duration: int, snapshot=None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "long_press", "coords": {"x": x, "y": y}, "duration": duration, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        step["target"] = _build_target(x, y, el) if el is not None else {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    _steps.append(step)
    logger.info(f"Recorded long_press: {step.get('target')}")


async def _record_multi_finger_tap(x: float, y: float, fingers: int, snapshot=None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "multi_finger_tap", "coords": {"x": x, "y": y}, "fingers": fingers, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        step["target"] = _build_target(x, y, el) if el is not None else {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    _steps.append(step)
    logger.info(f"Recorded multi_finger_tap({fingers}): {step.get('target')}")


async def _record_pinch(x: float, y: float, scale: float, spread: int, snapshot=None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "pinch", "coords": {"x": x, "y": y}, "scale": scale, "spread": spread, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["target"] = {"type": sel_type, "value": sel_val}
        else:
            step["target"] = {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    _steps.append(step)
    logger.info(f"Recorded pinch (scale={scale:.2f}): {step.get('target')}")


async def _record_rotate(x: float, y: float, rotation: float, spread: int, snapshot=None):
    root = snapshot if snapshot is not None else (_cache.get("root") or await _cached_tree())
    step: dict = {"action": "rotate", "coords": {"x": x, "y": y}, "rotation": rotation, "spread": spread, "timestamp": time.time()}
    if root is not None:
        el = hit_test(x, y, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["target"] = {"type": sel_type, "value": sel_val}
        else:
            step["target"] = {"type": "coordinate", "x": x, "y": y}
    else:
        step["target"] = {"type": "coordinate", "x": x, "y": y}
    _steps.append(step)
    logger.info(f"Recorded rotate ({rotation:.1f}°): {step.get('target')}")


async def _record_scroll(x1: float, y1: float, x2: float, y2: float, duration: int):
    await asyncio.sleep(0.1)
    root = await _cached_tree()
    scroll_container: dict | None = None
    scroll_offsets: dict | None = None
    if root is not None:
        el = find_scroll_container(x1, y1, root)
        if el is not None:
            sel_type, sel_val = build_scroll_container_selector(el, root)
            scroll_container = {"type": sel_type, "value": sel_val}
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


async def _record_type_text(text: str, tx: Optional[float], ty: Optional[float]):
    await asyncio.sleep(0.1)
    step: dict = {"action": "type_text", "text": text, "timestamp": time.time()}
    if tx is not None and ty is not None:
        root = await _cached_tree()
        if root is not None:
            el = hit_test(tx, ty, root)
            if el is not None:
                sel_type, sel_val = build_selector(el)
                step["target"] = {"type": sel_type, "value": sel_val}
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


async def _record_verify_visible(tx: float, ty: float, not_visible: bool):
    await asyncio.sleep(0.1)
    action = "verify_not_visible" if not_visible else "verify_visible"
    step: dict = {"action": action, "coords": {"x": tx, "y": ty}, "timestamp": time.time()}
    root = await _cached_tree()
    if root is not None:
        el = hit_test(tx, ty, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["target"] = {"type": sel_type, "value": sel_val}
        else:
            step["target"] = {"type": "coordinate", "x": tx, "y": ty}
    _steps.append(step)
    logger.info(f"Recorded {action}")


async def _record_verify_get_text(tx: float, ty: float, expected_text: str):
    await asyncio.sleep(0.1)
    step: dict = {"action": "verify_get_text", "coords": {"x": tx, "y": ty},
                  "expected_text": expected_text, "timestamp": time.time()}
    root = await _cached_tree()
    if root is not None:
        el = hit_test(tx, ty, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["target"] = {"type": sel_type, "value": sel_val}
        else:
            step["target"] = {"type": "coordinate", "x": tx, "y": ty}
    _steps.append(step)
    logger.info(f"Recorded verify_get_text: {expected_text!r}")


async def _record_verify_screenshot_gt(tx: float, ty: float, screenshot_name: str, bounds: dict):
    await asyncio.sleep(0.1)
    step: dict = {"action": "verify_screenshot_gt", "coords": {"x": tx, "y": ty},
                  "screenshot_name": screenshot_name, "bounds": bounds, "timestamp": time.time()}
    root = await _cached_tree()
    if root is not None:
        el = hit_test(tx, ty, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["target"] = {"type": sel_type, "value": sel_val}
    _steps.append(step)
    logger.info(f"Recorded verify_screenshot_gt: {screenshot_name}")


async def _record_verify_screenshot_diff(tx: float, ty: float, bounds: dict, phase: str = "before"):
    await asyncio.sleep(0.1)
    step: dict = {"action": "verify_screenshot_diff", "phase": phase,
                  "coords": {"x": tx, "y": ty}, "bounds": bounds, "timestamp": time.time()}
    root = await _cached_tree()
    if root is not None:
        el = hit_test(tx, ty, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["target"] = {"type": sel_type, "value": sel_val}
    _steps.append(step)
    logger.info(f"Recorded verify_screenshot_diff ({phase})")


async def _record_move(action: str, x1: float, y1: float, x2: float, y2: float, duration: int, extra: dict = None):
    await asyncio.sleep(0.1)
    root = await _cached_tree()
    step: dict = {
        "action": action,
        "coords": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
        "duration": duration,
        "timestamp": time.time(),
    }
    if extra:
        step.update(extra)
    if root is not None:
        el = hit_test(x1, y1, root)
        if el is not None:
            sel_type, sel_val = build_selector(el)
            step["start_target"] = {"type": sel_type, "value": sel_val}
    _steps.append(step)
    logger.info(f"Recorded {action}: {step.get('start_target', step['coords'])}")


async def _cached_tree(force: bool = False):
    now = time.time()
    if not force and _cache["root"] and now - _cache["ts"] < CACHE_TTL:
        return _cache["root"]
    root = await wda.get_source()
    if root is not None:
        _cache["root"] = root
        _cache["ts"] = now
    return _cache.get("root")


# ── Steps ──────────────────────────────────────────────────────────────────────

@app.get("/api/steps")
async def get_steps():
    return {"steps": _steps}


@app.delete("/api/steps")
async def clear_steps():
    _steps.clear()
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
        try:
            async with httpx.AsyncClient() as c:
                async with c.stream("GET", url, timeout=None) as r:
                    async for chunk in r.aiter_bytes(4096):
                        yield chunk
        except Exception as e:
            logger.warning(f"MJPEG stream disconnected: {e!r}")
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
                asyncio.create_task(wda.tap(x, y))
                if rec: asyncio.create_task(_record_point("tap", x, y, snapshot))

            elif t == "double_tap":
                x, y = float(data["x"]), float(data["y"])
                snapshot = _cache.get("root")
                asyncio.create_task(wda.double_tap(x, y))
                if rec: asyncio.create_task(_record_point("double_tap", x, y, snapshot))

            elif t == "triple_tap":
                x, y = float(data["x"]), float(data["y"])
                snapshot = _cache.get("root")
                asyncio.create_task(wda.triple_tap(x, y))
                if rec: asyncio.create_task(_record_point("triple_tap", x, y, snapshot))

            elif t == "long_press":
                x, y = float(data["x"]), float(data["y"])
                dur = int(data.get("duration", 1000))
                snapshot = _cache.get("root")
                asyncio.create_task(wda.long_press(x, y, dur))
                if rec: asyncio.create_task(_record_long_press(x, y, dur, snapshot))

            elif t == "two_finger_tap":
                x, y = float(data["x"]), float(data["y"])
                snapshot = _cache.get("root")
                asyncio.create_task(wda.two_finger_tap(x, y))
                if rec: asyncio.create_task(_record_point("two_finger_tap", x, y, snapshot))

            elif t == "multi_finger_tap":
                x, y = float(data["x"]), float(data["y"])
                fingers = int(data.get("fingers", 3))
                snapshot = _cache.get("root")
                asyncio.create_task(wda.multi_finger_tap(x, y, fingers))
                if rec: asyncio.create_task(_record_multi_finger_tap(x, y, fingers, snapshot))

            elif t == "pinch":
                x, y = float(data["x"]), float(data["y"])
                scale = float(data.get("scale", 0.5))
                spread = int(data.get("spread", 80))
                snapshot = _cache.get("root")
                asyncio.create_task(wda.pinch(x, y, scale, spread))
                if rec: asyncio.create_task(_record_pinch(x, y, scale, spread, snapshot))

            elif t == "rotate":
                x, y = float(data["x"]), float(data["y"])
                rotation = float(data.get("rotation", 45.0))
                spread = int(data.get("spread", 80))
                snapshot = _cache.get("root")
                asyncio.create_task(wda.rotate(x, y, rotation, spread))
                if rec: asyncio.create_task(_record_rotate(x, y, rotation, spread, snapshot))

            elif t == "scroll":
                x1, y1, x2, y2 = float(data["x1"]), float(data["y1"]), float(data["x2"]), float(data["y2"])
                dur = int(data.get("duration", 600))
                asyncio.create_task(wda.scroll(x1, y1, x2, y2, dur))
                if rec: asyncio.create_task(_record_scroll(x1, y1, x2, y2, dur))

            elif t == "update_scroll_target":
                x, y = float(data["x"]), float(data["y"])
                asyncio.create_task(_record_scroll_target(x, y))

            elif t == "swipe":
                x1, y1, x2, y2 = float(data["x1"]), float(data["y1"]), float(data["x2"]), float(data["y2"])
                dur = int(data.get("duration", 400))
                direction = data.get("direction", "up")
                asyncio.create_task(wda.swipe(x1, y1, x2, y2, dur))
                if rec:
                    step_extra = {"direction": direction}
                    asyncio.create_task(_record_move("swipe", x1, y1, x2, y2, dur, extra=step_extra))

            elif t == "update_swipe_target":
                x, y = float(data["x"]), float(data["y"])
                asyncio.create_task(_record_swipe_target(x, y))

            elif t == "drag":
                x1, y1, x2, y2 = float(data["x1"]), float(data["y1"]), float(data["x2"]), float(data["y2"])
                dur = int(data.get("duration", 1000))
                asyncio.create_task(wda.drag(x1, y1, x2, y2, dur))
                if rec: asyncio.create_task(_record_move("drag", x1, y1, x2, y2, dur))

            elif t == "type_text":
                text = data.get("text", "")
                tx = data.get("target_x")
                ty = data.get("target_y")
                asyncio.create_task(wda.type_text(text))
                if rec: asyncio.create_task(_record_type_text(
                    text,
                    float(tx) if tx is not None else None,
                    float(ty) if ty is not None else None,
                ))

            elif t == "home":
                asyncio.create_task(wda.press_home())
                if rec: asyncio.create_task(_record_simple("home"))

            elif t == "launch_app":
                bundle_id = data.get("bundle_id", "")
                asyncio.create_task(wda.launch_app(bundle_id))
                if rec: asyncio.create_task(_record_launch_app(bundle_id))

            elif t == "verify_visible":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                not_vis = bool(data.get("not_visible", False))
                if rec: asyncio.create_task(_record_verify_visible(tx, ty, not_vis))

            elif t == "verify_get_text":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                expected = data.get("expected_text", "")
                if rec: asyncio.create_task(_record_verify_get_text(tx, ty, expected))

            elif t == "verify_screenshot_gt":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                name = data.get("screenshot_name", "")
                bounds = data.get("bounds", {})
                if rec: asyncio.create_task(_record_verify_screenshot_gt(tx, ty, name, bounds))

            elif t == "verify_screenshot_diff":
                tx, ty = float(data["target_x"]), float(data["target_y"])
                bounds = data.get("bounds", {})
                phase = data.get("phase", "before")
                if rec: asyncio.create_task(_record_verify_screenshot_diff(tx, ty, bounds, phase))

            await ws.send_json({"ok": True})
    except (WebSocketDisconnect, Exception):
        pass


# ── Export ─────────────────────────────────────────────────────────────────────

class ExportReq(BaseModel):
    steps: List[dict]
    case_name: str = ""

@app.post("/api/export")
async def export_script(req: ExportReq):
    script = generate_script(req.steps, req.case_name)
    safe = "".join(c if c.isalnum() or c == "_" else "_" for c in req.case_name).strip("_")
    filename = f"test_{safe or 'recorded'}.py"
    return JSONResponse({"script": script, "filename": filename})


# ── Static frontend ────────────────────────────────────────────────────────────

app.mount("/", StaticFiles(directory="static", html=True), name="static")
