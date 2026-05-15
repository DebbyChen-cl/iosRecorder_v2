"""
Block 7 — WDA Gesture Payload

Verifies that WDAClient assembles the correct W3C Actions JSON payload for
each gesture type. All HTTP requests are intercepted by a mock httpx client;
the actual payload sent to WDA is captured and asserted. No device needed.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

pytestmark = pytest.mark.unit

from app.wda import WDAClient

SESSION_ID = "test-session-abc"


def _make_mock_http():
    """Return (mock_http, captured) where captured grows with each POST."""
    captured = []
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_http = AsyncMock()

    async def _post(url, json=None, timeout=None, **kwargs):
        captured.append({"url": url, "json": json})
        return mock_resp

    mock_http.post = _post
    return mock_http, captured


def _actions_payload(captured: list) -> list:
    return captured[0]["json"]["actions"]


def _finger_actions(captured: list, finger_id: str = "finger1") -> list:
    for a in _actions_payload(captured):
        if a.get("id") == finger_id:
            return a["actions"]
    raise AssertionError(f"finger {finger_id!r} not found in payload")


# ── helpers that create WDAClient inside the event loop ───────────────────────

async def _tap(x, y):
    mock_http, captured = _make_mock_http()
    client = WDAClient("http://localhost:8100")
    client._client = mock_http
    client._session_id = SESSION_ID
    result = await client.tap(x, y)
    return result, captured


async def _swipe(x1, y1, x2, y2, duration_ms=400):
    mock_http, captured = _make_mock_http()
    client = WDAClient("http://localhost:8100")
    client._client = mock_http
    client._session_id = SESSION_ID
    await client.swipe(x1, y1, x2, y2, duration_ms=duration_ms)
    return captured


async def _long_press(x, y, duration_ms=1000):
    mock_http, captured = _make_mock_http()
    client = WDAClient("http://localhost:8100")
    client._client = mock_http
    client._session_id = SESSION_ID
    await client.long_press(x, y, duration_ms=duration_ms)
    return captured


async def _double_tap(x, y):
    mock_http, captured = _make_mock_http()
    client = WDAClient("http://localhost:8100")
    client._client = mock_http
    client._session_id = SESSION_ID
    await client.double_tap(x, y)
    return captured


async def _scroll(x1, y1, x2, y2, duration_ms=600):
    mock_http, captured = _make_mock_http()
    client = WDAClient("http://localhost:8100")
    client._client = mock_http
    client._session_id = SESSION_ID
    await client.scroll(x1, y1, x2, y2, duration_ms=duration_ms)
    return captured


async def _two_finger_tap(x, y, spread=20):
    mock_http, captured = _make_mock_http()
    client = WDAClient("http://localhost:8100")
    client._client = mock_http
    client._session_id = SESSION_ID
    await client.two_finger_tap(x, y, spread=spread)
    return captured


# ── tap ────────────────────────────────────────────────────────────────────────

def test_tap_sends_actions_endpoint():
    _, captured = asyncio.run(_tap(100, 200))
    assert len(captured) == 1
    assert f"/session/{SESSION_ID}/actions" in captured[0]["url"]


def test_tap_returns_true_on_success():
    result, _ = asyncio.run(_tap(100, 200))
    assert result is True


def test_tap_payload_coordinates():
    _, captured = asyncio.run(_tap(100, 200))
    acts = _finger_actions(captured)
    move = next(a for a in acts if a["type"] == "pointerMove")
    assert move["x"] == 100
    assert move["y"] == 200


def test_tap_payload_has_pointer_down_up():
    _, captured = asyncio.run(_tap(100, 200))
    acts = _finger_actions(captured)
    types = [a["type"] for a in acts]
    assert "pointerDown" in types
    assert "pointerUp" in types


def test_tap_uses_touch_pointer_type():
    _, captured = asyncio.run(_tap(100, 200))
    finger = _actions_payload(captured)[0]
    assert finger["parameters"]["pointerType"] == "touch"


def test_tap_coordinates_are_int():
    _, captured = asyncio.run(_tap(123.7, 456.9))
    acts = _finger_actions(captured)
    move = next(a for a in acts if a["type"] == "pointerMove")
    assert isinstance(move["x"], int)
    assert isinstance(move["y"], int)


# ── swipe ──────────────────────────────────────────────────────────────────────

def test_swipe_start_and_end_coordinates():
    captured = asyncio.run(_swipe(300, 400, 100, 400))
    acts = _finger_actions(captured)
    moves = [a for a in acts if a["type"] == "pointerMove"]
    assert moves[0]["x"] == 300
    assert moves[0]["y"] == 400
    assert moves[1]["x"] == 100
    assert moves[1]["y"] == 400


def test_swipe_move_has_duration():
    captured = asyncio.run(_swipe(300, 400, 100, 400, duration_ms=800))
    acts = _finger_actions(captured)
    moving = [a for a in acts if a["type"] == "pointerMove" and a.get("duration", 0) > 0]
    assert len(moving) == 1
    assert moving[0]["duration"] == 800


# ── long_press ─────────────────────────────────────────────────────────────────

def test_long_press_pause_duration():
    captured = asyncio.run(_long_press(100, 200, duration_ms=1500))
    acts = _finger_actions(captured)
    pause = next(a for a in acts if a["type"] == "pause")
    assert pause["duration"] == 1500


def test_long_press_coordinates():
    captured = asyncio.run(_long_press(150, 300, duration_ms=1000))
    acts = _finger_actions(captured)
    move = next(a for a in acts if a["type"] == "pointerMove")
    assert move["x"] == 150
    assert move["y"] == 300


# ── double_tap ─────────────────────────────────────────────────────────────────

def test_double_tap_has_two_down_up_pairs():
    captured = asyncio.run(_double_tap(100, 200))
    acts = _finger_actions(captured)
    downs = [a for a in acts if a["type"] == "pointerDown"]
    ups = [a for a in acts if a["type"] == "pointerUp"]
    assert len(downs) == 2
    assert len(ups) == 2


# ── scroll ─────────────────────────────────────────────────────────────────────

def test_scroll_has_initial_pause():
    captured = asyncio.run(_scroll(200, 600, 200, 200, duration_ms=600))
    acts = _finger_actions(captured)
    first_pause = next((a for a in acts if a["type"] == "pause"), None)
    assert first_pause is not None
    assert first_pause["duration"] == 100


# ── two_finger_tap ─────────────────────────────────────────────────────────────

def test_two_finger_tap_has_two_fingers():
    captured = asyncio.run(_two_finger_tap(200, 400))
    actions = _actions_payload(captured)
    assert len(actions) == 2
    ids = {a["id"] for a in actions}
    assert "finger1" in ids
    assert "finger2" in ids


def test_two_finger_tap_fingers_spread_apart():
    captured = asyncio.run(_two_finger_tap(200, 400, spread=30))
    actions = _actions_payload(captured)
    x_positions = []
    for finger in actions:
        move = next(a for a in finger["actions"] if a["type"] == "pointerMove")
        x_positions.append(move["x"])
    assert x_positions[0] != x_positions[1]


# ── no client → returns False ──────────────────────────────────────────────────

def test_tap_returns_false_without_client():
    async def _run():
        client = WDAClient("http://localhost:8100")
        return await client.tap(100, 200)

    result = asyncio.run(_run())
    assert result is False
