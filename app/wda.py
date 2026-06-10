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
        self._source_task: Optional[asyncio.Task] = None
        self._action_in_progress = False
        self._last_screen_size: dict = {"width": 390, "height": 844}

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

    async def _adopt_session(self) -> bool:
        """Reconnect to an existing WDA session without ever creating a new one.

        Safe to call while Appium/pytest owns WDA — will never POST /session,
        so it cannot invalidate an externally-owned session.  Returns True only
        when an existing session was found and stored.
        """
        async with self._session_lock:
            if self._session_id:
                return True
            try:
                resp = await self._client.get(f"{self.base_url}/sessions", timeout=5.0)
                if resp.status_code == 200:
                    sessions = resp.json().get("value", [])
                    if sessions:
                        sid = sessions[0].get("id") or sessions[0].get("sessionId")
                        if sid:
                            self._session_id = sid
                            logger.info(f"WDA heartbeat adopted session: {sid}")
                            return True
            except Exception as e:
                logger.debug(f"WDA heartbeat GET /sessions failed: {e!r}")
            return False  # Never POST /session — avoids killing an Appium session

    async def _ensure_session(self) -> bool:
        """Use an existing WDA session if available, otherwise create one.

        Intentionally tries POST /session even when GET /sessions fails — WDA
        can return ReadError during startup/load but still accept a new session.
        This makes the recorder resilient to transient WDA instability.
        The heartbeat uses _adopt_session() instead (never creates) to avoid
        interfering with an Appium-owned session during pytest runs.
        """
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
                logger.debug(f"WDA GET /sessions failed: {e!r} — will try POST /session")
            try:
                # No existing session (or GET failed) — create a new one
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
        """Run W3C pointer actions, auto-recreate session on failure.

        Cancels any in-flight source fetch first so WDA can process
        the gesture immediately (WDA handles requests serially).
        """
        # Cancel in-flight source fetch to free up WDA
        if self._source_task is not None and not self._source_task.done():
            self._source_task.cancel()
            self._source_task = None
            logger.debug("Cancelled in-flight source fetch for gesture priority")
        self._action_in_progress = True
        try:
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
                    # Use adopt-only on gesture retry — never POST /session here,
                    # as Appium may own WDA and a POST would kill its session.
                    # The heartbeat will recreate a session when it is safe to do so.
                    if await self._adopt_session():
                        resp = await self._client.post(
                            f"{self.base_url}/session/{self._session_id}/actions",
                            json=payload,
                            timeout=timeout,
                        )
                        return resp.status_code == 200
            except Exception as e:
                logger.error(f"Actions failed: {e!r}")
            return False
        finally:
            self._action_in_progress = False

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

    async def five_tap(self, x: float, y: float) -> bool:
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
        """Two-finger rotation around (x, y). rotation_deg > 0 = clockwise.

        Fingers move along an arc (not a straight chord) so that the iOS
        gesture recogniser samples the correct rotation at every point.
        For large angles (≥ 30°) a single straight-line move under-reports
        the rotation because the fingers converge near the centre.
        """
        xi, yi = int(x), int(y)
        r = spread
        start = math.radians(45)
        total = math.radians(rotation_deg)

        # Number of arc steps: 1 per 15°, capped so each step ≥ 40 ms
        # Fewer steps = smaller W3C payload = faster WDA processing
        steps = max(4, int(abs(rotation_deg) / 15))
        step_dur = max(40, duration_ms // steps)
        steps = duration_ms // step_dur          # recompute to fill exactly duration_ms
        remainder = duration_ms - step_dur * steps

        def pt(angle: float):
            return round(xi + r * math.cos(angle)), round(yi + r * math.sin(angle))

        def arc_actions(finger_offset: float) -> list:
            """Build W3C action list for one finger along the arc."""
            a0 = start + finger_offset
            p0 = pt(a0)
            acts = [
                {"type": "pointerMove", "duration": 0,        "x": p0[0], "y": p0[1]},
                {"type": "pointerDown", "button": 0},
            ]
            for i in range(1, steps + 1):
                a = a0 + total * i / steps
                p = pt(a)
                dur = step_dur + (remainder if i == steps else 0)
                acts.append({"type": "pointerMove", "duration": dur, "x": p[0], "y": p[1]})
            # Brief pause at final position so iOS reads the end angle before lift-off
            acts.append({"type": "pause", "duration": 40})
            acts.append({"type": "pointerUp", "button": 0})
            return acts

        return await self._actions([
            {"type": "pointer", "id": "finger1",
             "parameters": {"pointerType": "touch"},
             "actions": arc_actions(math.pi)},
            {"type": "pointer", "id": "finger2",
             "parameters": {"pointerType": "touch"},
             "actions": arc_actions(0)},
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

    async def paint(self, points: list[dict], duration_ms: int = 1000) -> bool:
        """Draw a free-form stroke using one continuous touch path.

        points: [{"x": int|float, "y": int|float, "t": int_ms}, ...]
        """
        if not points:
            return False
        norm: list[tuple[int, int, int]] = []
        for p in points:
            norm.append((
                int(float(p.get("x", 0))),
                int(float(p.get("y", 0))),
                max(0, int(p.get("t", 0))),
            ))
        if len(norm) == 1:
            x, y, _ = norm[0]
            norm.append((x, y, max(16, int(duration_ms))))

        default_seg = max(16, int(duration_ms / max(1, len(norm) - 1)))
        touch_steps: list[dict] = [
            {"type": "pointerMove", "duration": 0, "x": norm[0][0], "y": norm[0][1]},
            {"type": "pointerDown", "button": 0},
        ]
        prev_t = norm[0][2]
        for x, y, t in norm[1:]:
            seg = t - prev_t if t > prev_t else default_seg
            touch_steps.append({"type": "pointerMove", "duration": max(8, seg), "x": x, "y": y})
            prev_t = max(prev_t, t)
        touch_steps.append({"type": "pointerUp", "button": 0})
        # Paint can contain many segments and WDA often needs extra settle time.
        # Use a larger buffer to avoid false ReadTimeout on valid long strokes.
        timeout_s = max(12.0, (max(duration_ms, prev_t) / 1000.0) + 15.0)
        return await self._actions(self._touch_actions(touch_steps), timeout=timeout_s)

    async def get_source(self) -> Optional[ET.Element]:
        """Fetch page source, coalescing concurrent calls.

        If a get_source request is already in-flight to WDA, subsequent
        callers piggyback on the same request instead of queuing a new
        one.  Skips entirely if a gesture action is in progress (WDA is
        serial — source fetch would queue behind the gesture).
        """
        # Don't start source requests while a gesture is executing
        if self._action_in_progress:
            return None
        if self._source_task is not None and not self._source_task.done():
            try:
                return await self._source_task
            except (Exception, asyncio.CancelledError):
                return None
        self._source_task = asyncio.create_task(self._get_source_impl())
        try:
            return await self._source_task
        except (Exception, asyncio.CancelledError):
            return None

    async def _get_source_impl(self) -> Optional[ET.Element]:
        if not self._client:
            return None
        if not self._session_id:
            # Use adopt-only — never POST /session here.
            # If Appium is mid-test, posting would kill its session.
            # The heartbeat or the next gesture call will recreate when safe.
            await self._adopt_session()
        if not self._session_id:
            return None
        for attempt in range(2):
            try:
                t0 = asyncio.get_event_loop().time()
                resp = await self._client.get(
                    f"{self.base_url}/session/{self._session_id}/source",
                    timeout=8.0,
                )
                elapsed = asyncio.get_event_loop().time() - t0
                if resp.status_code in (404, 500):
                    self._session_id = None
                    return None
                data = resp.json()
                xml_text = data.get("value", resp.text)
                logger.info(f"WDA source: {elapsed:.2f}s  {len(xml_text):,} chars")
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
            return self._last_screen_size
        # Skip WDA call while a gesture is executing (WDA is serial)
        if self._action_in_progress:
            return self._last_screen_size
        if self._session_id:
            try:
                resp = await self._client.get(
                    f"{self.base_url}/session/{self._session_id}/window/size",
                    timeout=3.0,
                )
                val = resp.json().get("value", {})
                if val.get("width"):
                    self._last_screen_size = {"width": val["width"], "height": val["height"]}
                    return self._last_screen_size
            except Exception:
                pass
        return self._last_screen_size

    async def is_alive(self) -> bool:
        if not self._client:
            return False
        # Skip WDA call while a gesture is executing (WDA is serial)
        if self._action_in_progress:
            return True
        try:
            resp = await self._client.get(f"{self.base_url}/status", timeout=3.0)
            return resp.status_code == 200
        except Exception:
            return False

    async def ping_session(self) -> bool:
        """Validate the WDA session and recover it if lost.

        Called every 5 s by the background heartbeat.
        Rules:
          - GET /sessions succeeds and returns sessions → adopt (never disrupt)
          - GET /sessions succeeds and returns EMPTY list → safe to POST (no Appium)
          - GET /sessions throws / non-200 → do nothing (Appium might be busy)
        This prevents the heartbeat from ever killing an Appium-owned session.
        """
        if not self._client or self._action_in_progress:
            return bool(self._session_id)
        # Check WDA process reachability
        try:
            alive_resp = await self._client.get(f"{self.base_url}/status", timeout=3.0)
            if alive_resp.status_code != 200:
                return False
        except Exception:
            return False
        # Validate the cached session ID
        if self._session_id:
            try:
                resp = await self._client.get(
                    f"{self.base_url}/session/{self._session_id}",
                    timeout=3.0,
                )
                if resp.status_code == 200:
                    return True
                logger.info("WDA session lost — will adopt or recreate")
                self._session_id = None
            except Exception:
                return bool(self._session_id)
        # No valid session — decide whether to adopt or create
        async with self._session_lock:
            if self._session_id:  # re-check after acquiring lock
                return True
            try:
                resp = await self._client.get(f"{self.base_url}/sessions", timeout=5.0)
            except Exception as e:
                logger.debug(f"WDA heartbeat GET /sessions failed: {e!r} — skip")
                return False  # unknown state; don't risk POSTing
            if resp.status_code != 200:
                return False
            sessions = resp.json().get("value", [])
            if sessions:
                # Someone (Appium/pytest) owns WDA — adopt without disrupting
                sid = sessions[0].get("id") or sessions[0].get("sessionId")
                if sid:
                    self._session_id = sid
                    logger.info(f"WDA heartbeat adopted session: {sid}")
                    return True
                return False
            # Definitively empty list → no one owns WDA → safe to create
            try:
                r = await self._client.post(
                    f"{self.base_url}/session",
                    json={"capabilities": {"alwaysMatch": {}}},
                    timeout=5.0,
                )
                data = r.json()
                sid = data.get("sessionId") or data.get("value", {}).get("sessionId")
                if sid:
                    self._session_id = sid
                    logger.info(f"WDA heartbeat created session: {sid}")
                    return True
            except Exception as e:
                logger.warning(f"WDA heartbeat create session failed: {e!r}")
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
        """Launch an app by bundle ID. Tries cold-launch first; falls back to activate."""
        if not self._session_id:
            await self._ensure_session()
        if not self._session_id or not self._client:
            return False
        # Try cold launch first (works even if app is not running)
        try:
            resp = await self._client.post(
                f"{self.base_url}/session/{self._session_id}/wda/apps/launch",
                json={"bundleId": bundle_id},
                timeout=15.0,
            )
            if resp.status_code in (200, 204):
                return True
            logger.warning(f"launch_app cold-launch {resp.status_code}: {resp.text[:300]}, falling back to activate")
        except Exception as e:
            logger.debug(f"launch_app cold-launch failed ({e}), falling back to activate")
        # Fallback: activate (bring to foreground if already running)
        try:
            resp = await self._client.post(
                f"{self.base_url}/session/{self._session_id}/wda/apps/activate",
                json={"bundleId": bundle_id},
                timeout=10.0,
            )
            if resp.status_code in (200, 204):
                return True
            logger.error(f"launch_app activate fallback {resp.status_code}: {resp.text[:300]}")
            return False
        except Exception as e:
            logger.error(f"launch_app activate fallback failed: {e}")
            return False

    async def terminate_app(self, bundle_id: str) -> bool:
        """Terminate (force-quit) an app by bundle ID."""
        if not self._session_id:
            await self._ensure_session()
        if not self._session_id or not self._client:
            return False
        try:
            resp = await self._client.post(
                f"{self.base_url}/session/{self._session_id}/wda/apps/terminate",
                json={"bundleId": bundle_id},
                timeout=10.0,
            )
            if resp.status_code in (200, 204):
                return True
            logger.error(f"terminate_app {resp.status_code}: {resp.text[:300]}")
            return False
        except Exception as e:
            logger.error(f"terminate_app failed: {e}")
            return False

    async def get_screenshot(self) -> Optional[str]:
        """Return the current screen as a base64-encoded PNG string, or None."""
        if not self._client or not self._session_id:
            return None
        try:
            resp = await self._client.get(
                f"{self.base_url}/session/{self._session_id}/screenshot",
                timeout=10.0,
            )
            if resp.status_code == 200:
                return resp.json().get("value")
        except Exception as e:
            logger.warning(f"get_screenshot failed: {e!r}")
        return None

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
