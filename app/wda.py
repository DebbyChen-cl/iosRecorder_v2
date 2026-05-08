import asyncio
import logging
import math
import re
import xml.etree.ElementTree as ET
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

_W3C_TAP = {
    "actions": [{
        "type": "pointer",
        "id": "finger1",
        "parameters": {"pointerType": "touch"},
        "actions": [
            {"type": "pointerMove", "duration": 0, "x": 0, "y": 0},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": 50},
            {"type": "pointerUp", "button": 0},
        ],
    }]
}


def _parse_xml(text: str) -> ET.Element:
    text = re.sub(r"<!DOCTYPE[^>]*>", "", text)
    return ET.fromstring(text)


class WDAClient:
    def __init__(self, base_url: str = "http://localhost:8100"):
        self.base_url = base_url.rstrip("/")
        self.mjpeg_url: str = ""
        self._client: Optional[httpx.AsyncClient] = None
        self._session_id: Optional[str] = None
        self._session_lock = asyncio.Lock()

    async def connect(self, base_url: Optional[str] = None):
        if base_url:
            self.base_url = base_url.rstrip("/")
        if self._client:
            await self._client.aclose()
        self._client = httpx.AsyncClient(
            timeout=10.0,
            limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
        )
        self._session_id = None
        await self._ensure_session()
        self.mjpeg_url = re.sub(
            r":(\d+)$", lambda m: f":{int(m.group(1)) + 1000}", self.base_url
        ) + "/mjpeg"
        logger.info(f"MJPEG: {self.mjpeg_url} | session: {self._session_id}")

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None

    async def _ensure_session(self) -> bool:
        """Use an existing WDA session if available, otherwise create one."""
        async with self._session_lock:
            if self._session_id:
                return True
            try:
                # First: check if a session already exists (e.g. started by Appium/pytest)
                resp = await self._client.get(f"{self.base_url}/sessions", timeout=5.0)
                if resp.status_code == 200:
                    sessions = resp.json().get("value", [])
                    if sessions:
                        sid = sessions[0].get("id") or sessions[0].get("sessionId")
                        if sid:
                            self._session_id = sid
                            logger.info(f"WDA reusing existing session: {sid}")
                            return True
            except Exception as e:
                logger.debug(f"WDA GET /sessions failed: {e!r}")
            try:
                # No existing session — create a new one
                resp = await self._client.post(
                    f"{self.base_url}/session",
                    json={"capabilities": {"alwaysMatch": {}}},
                    timeout=5.0,
                )
                data = resp.json()
                sid = data.get("sessionId") or data.get("value", {}).get("sessionId")
                if sid:
                    self._session_id = sid
                    logger.info(f"WDA session created: {sid}")
                    return True
                logger.warning(f"WDA session failed: status={resp.status_code} body={resp.text[:200]}")
            except Exception as e:
                logger.warning(f"WDA session failed: {e!r}")
            return False

    async def tap(self, x: float, y: float) -> bool:
        if not self._client:
            return False
        return await self._actions(self._touch_actions([
            {"type": "pointerMove", "duration": 0, "x": int(x), "y": int(y)},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": 50},
            {"type": "pointerUp", "button": 0},
        ]))

    async def _actions(self, actions: list, timeout: float = 5.0) -> bool:
        """Run W3C pointer actions, auto-recreate session on failure."""
        if not self._session_id:
            await self._ensure_session()
        if not self._session_id:
            return False
        payload = {"actions": actions}
        try:
            resp = await self._client.post(
                f"{self.base_url}/session/{self._session_id}/actions",
                json=payload,
                timeout=timeout,
            )
            if resp.status_code == 200:
                return True
            if resp.status_code in (404, 500):
                self._session_id = None
                if await self._ensure_session():
                    resp = await self._client.post(
                        f"{self.base_url}/session/{self._session_id}/actions",
                        json=payload,
                        timeout=timeout,
                    )
                    return resp.status_code == 200
        except Exception as e:
            logger.error(f"Actions failed: {e}")
        return False

    def _touch_actions(self, steps: list) -> list:
        return [{
            "type": "pointer",
            "id": "finger1",
            "parameters": {"pointerType": "touch"},
            "actions": steps,
        }]

    async def double_tap(self, x: float, y: float) -> bool:
        return await self._actions(self._touch_actions([
            {"type": "pointerMove", "duration": 0, "x": int(x), "y": int(y)},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": 50},
            {"type": "pointerUp", "button": 0},
            {"type": "pause", "duration": 80},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": 50},
            {"type": "pointerUp", "button": 0},
        ]))

    async def triple_tap(self, x: float, y: float) -> bool:
        return await self._actions(self._touch_actions([
            {"type": "pointerMove", "duration": 0, "x": int(x), "y": int(y)},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": 50},
            {"type": "pointerUp", "button": 0},
            {"type": "pause", "duration": 80},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": 50},
            {"type": "pointerUp", "button": 0},
            {"type": "pause", "duration": 80},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": 50},
            {"type": "pointerUp", "button": 0},
        ]))

    async def long_press(self, x: float, y: float, duration_ms: int = 1000) -> bool:
        return await self._actions(
            self._touch_actions([
                {"type": "pointerMove", "duration": 0, "x": int(x), "y": int(y)},
                {"type": "pointerDown", "button": 0},
                {"type": "pause", "duration": duration_ms},
                {"type": "pointerUp", "button": 0},
            ]),
            timeout=duration_ms / 1000 + 4,
        )

    async def two_finger_tap(self, x: float, y: float, spread: int = 20) -> bool:
        xi, yi = int(x), int(y)
        return await self._actions([
            {
                "type": "pointer", "id": "finger1",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": xi - spread, "y": yi},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pause", "duration": 50},
                    {"type": "pointerUp", "button": 0},
                ],
            },
            {
                "type": "pointer", "id": "finger2",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": xi + spread, "y": yi},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pause", "duration": 50},
                    {"type": "pointerUp", "button": 0},
                ],
            },
        ])

    async def multi_finger_tap(self, x: float, y: float, fingers: int = 3, spread: int = 30) -> bool:
        xi, yi = int(x), int(y)
        half = spread * (fingers - 1) // 2
        return await self._actions([
            {
                "type": "pointer", "id": f"finger{i + 1}",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": xi - half + spread * i, "y": yi},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pause", "duration": 50},
                    {"type": "pointerUp", "button": 0},
                ],
            }
            for i in range(fingers)
        ])

    async def scroll(self, x1: float, y1: float, x2: float, y2: float, duration_ms: int = 600) -> bool:
        """Scroll gesture — slower than swipe, with initial stabilising pause."""
        return await self._actions(
            self._touch_actions([
                {"type": "pointerMove", "duration": 0, "x": int(x1), "y": int(y1)},
                {"type": "pointerDown", "button": 0},
                {"type": "pause", "duration": 100},
                {"type": "pointerMove", "duration": duration_ms, "x": int(x2), "y": int(y2)},
                {"type": "pointerUp", "button": 0},
            ]),
            timeout=duration_ms / 1000 + 4,
        )

    async def pinch(self, x: float, y: float, scale: float, spread: int = 80, duration_ms: int = 600) -> bool:
        """Two-finger pinch. scale<1 = zoom out, scale>1 = zoom in."""
        xi, yi = int(x), int(y)
        d = spread / math.sqrt(2)
        d_end = d * scale
        return await self._actions([
            {
                "type": "pointer", "id": "finger1",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": xi - int(d), "y": yi - int(d)},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pointerMove", "duration": duration_ms, "x": xi - int(d_end), "y": yi - int(d_end)},
                    {"type": "pointerUp", "button": 0},
                ],
            },
            {
                "type": "pointer", "id": "finger2",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": xi + int(d), "y": yi + int(d)},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pointerMove", "duration": duration_ms, "x": xi + int(d_end), "y": yi + int(d_end)},
                    {"type": "pointerUp", "button": 0},
                ],
            },
        ], timeout=duration_ms / 1000 + 4)

    async def rotate(self, x: float, y: float, rotation_deg: float, spread: int = 80, duration_ms: int = 600) -> bool:
        """Two-finger rotation around (x, y). rotation_deg > 0 = clockwise."""
        xi, yi = int(x), int(y)
        r = spread
        start = math.radians(45)
        end = start + math.radians(rotation_deg)

        def pt(angle: float):
            return xi + int(r * math.cos(angle)), yi + int(r * math.sin(angle))

        f1s, f1e = pt(start + math.pi), pt(end + math.pi)
        f2s, f2e = pt(start), pt(end)
        return await self._actions([
            {
                "type": "pointer", "id": "finger1",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": f1s[0], "y": f1s[1]},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pointerMove", "duration": duration_ms, "x": f1e[0], "y": f1e[1]},
                    {"type": "pointerUp", "button": 0},
                ],
            },
            {
                "type": "pointer", "id": "finger2",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": f2s[0], "y": f2s[1]},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pointerMove", "duration": duration_ms, "x": f2e[0], "y": f2e[1]},
                    {"type": "pointerUp", "button": 0},
                ],
            },
        ], timeout=duration_ms / 1000 + 4)

    async def swipe(self, x1: float, y1: float, x2: float, y2: float, duration_ms: int = 400) -> bool:
        return await self._actions(
            self._touch_actions([
                {"type": "pointerMove", "duration": 0, "x": int(x1), "y": int(y1)},
                {"type": "pointerDown", "button": 0},
                {"type": "pointerMove", "duration": duration_ms, "x": int(x2), "y": int(y2)},
                {"type": "pointerUp", "button": 0},
            ]),
            timeout=duration_ms / 1000 + 4,
        )

    async def drag(self, x1: float, y1: float, x2: float, y2: float, duration_ms: int = 1000) -> bool:
        return await self._actions(
            self._touch_actions([
                {"type": "pointerMove", "duration": 0, "x": int(x1), "y": int(y1)},
                {"type": "pointerDown", "button": 0},
                {"type": "pause", "duration": 800},
                {"type": "pointerMove", "duration": duration_ms, "x": int(x2), "y": int(y2)},
                {"type": "pointerUp", "button": 0},
            ]),
            timeout=(duration_ms + 800) / 1000 + 4,
        )

    async def get_source(self) -> Optional[ET.Element]:
        if not self._client:
            return None
        if not self._session_id:
            await self._ensure_session()
        if not self._session_id:
            return None
        for attempt in range(2):
            try:
                resp = await self._client.get(
                    f"{self.base_url}/session/{self._session_id}/source", timeout=8.0
                )
                if resp.status_code in (404, 500):
                    self._session_id = None
                    return None
                data = resp.json()
                xml_text = data.get("value", resp.text)
                return _parse_xml(xml_text)
            except (httpx.ReadError, httpx.RemoteProtocolError) as e:
                if attempt == 0:
                    # WDA dropped the connection mid-response; give it time to recover
                    logger.debug(f"Get source retry after {e!r}")
                    await asyncio.sleep(0.5)
                    continue
                logger.error(f"Get source: {e!r}")
                return None
            except Exception as e:
                logger.error(f"Get source: {e!r}")
                return None
        return None

    async def get_screen_size(self) -> dict:
        if not self._client:
            return {"width": 390, "height": 844}
        if self._session_id:
            try:
                resp = await self._client.get(
                    f"{self.base_url}/session/{self._session_id}/window/size",
                    timeout=3.0,
                )
                val = resp.json().get("value", {})
                if val.get("width"):
                    return {"width": val["width"], "height": val["height"]}
            except Exception:
                pass
        return {"width": 390, "height": 844}

    async def is_alive(self) -> bool:
        if not self._client:
            return False
        try:
            resp = await self._client.get(f"{self.base_url}/status", timeout=3.0)
            return resp.status_code == 200
        except Exception:
            return False

    async def press_home(self) -> bool:
        """Press the hardware Home button via WDA."""
        if not self._client:
            return False
        try:
            resp = await self._client.post(
                f"{self.base_url}/wda/homescreen",
                timeout=5.0,
            )
            return resp.status_code in (200, 204)
        except Exception as e:
            logger.error(f"press_home failed: {e}")
            return False

    async def launch_app(self, bundle_id: str) -> bool:
        """Activate (bring to foreground) an app by bundle ID."""
        if not self._session_id:
            await self._ensure_session()
        if not self._session_id or not self._client:
            return False
        try:
            resp = await self._client.post(
                f"{self.base_url}/session/{self._session_id}/wda/apps/activate",
                json={"bundleId": bundle_id},
                timeout=10.0,
            )
            return resp.status_code in (200, 204)
        except Exception as e:
            logger.error(f"launch_app failed: {e}")
            return False

    async def type_text(self, text: str) -> bool:
        """Type text into the currently focused element, word by word."""
        if not self._session_id:
            await self._ensure_session()
        if not self._session_id or not self._client:
            return False
        words = text.split(" ")
        for i, word in enumerate(words):
            chunk = word if i == len(words) - 1 else word + " "
            try:
                resp = await self._client.post(
                    f"{self.base_url}/session/{self._session_id}/wda/keys",
                    json={"value": list(chunk)},
                    timeout=10.0,
                )
                if resp.status_code not in (200, 204):
                    logger.warning(f"type_text chunk failed: {resp.status_code}")
                    return False
            except Exception as e:
                logger.error(f"type_text failed: {e}")
                return False
        return True
