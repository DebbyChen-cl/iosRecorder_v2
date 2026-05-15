"""
conftest.py — shared fixtures for both integration and unit tests.

Integration fixtures (client, clear_steps, warm_tree):
  - Require the recorder server running on BASE_URL
  - Require WDA connected to a real iOS device
  - Tests must be marked @pytest.mark.integration

Unit fixtures (fixture_xml, fixture_root, unit_client):
  - No device or server needed
  - Tests must be marked @pytest.mark.unit (set via pytestmark per file)
"""

import asyncio
import xml.etree.ElementTree as ET
from unittest.mock import AsyncMock, patch

import httpx
import pytest

BASE_URL = "http://localhost:8888"

# ── Shared fixture XML ─────────────────────────────────────────────────────────
#
# Minimal but realistic hierarchy covering all selector quality levels:
#   SaveButton  → id        (name != label)
#   Effects     → id_eq_label (name == label)
#   SearchField → id        (name != label)
#   Item1       → id        (name != label)
#   Label Only  → label_only (no name attr)
#   XCUIElementTypeOther (no id/label) → xpath_only
#   Cell-3      → id_indexed (name ends with -N)
#
# Coordinates summary (x, y → element):
#   (140, 222) → SaveButton
#   (240, 222) → Effects
#   (190, 318) → SearchField
#   (195, 390) → Item1  (inside MainScroll)
#   (195, 460) → "Label Only" button
#   (50,  530) → XCUIElementTypeOther (no id/label)
#   (195, 600) → Cell-3
#   (500, 500) → None  (outside all elements)

FIXTURE_XML = """\
<AppiumAUT>
  <XCUIElementTypeApplication name="PhotoDirector" label="PhotoDirector"
      enabled="true" x="0" y="0" width="390" height="844">
    <XCUIElementTypeWindow enabled="true" x="0" y="0" width="390" height="844">
      <XCUIElementTypeOther enabled="true" x="0" y="0" width="390" height="844">
        <XCUIElementTypeButton name="SaveButton" label="Save"
            enabled="true" x="100" y="200" width="80" height="44"/>
        <XCUIElementTypeButton name="Effects" label="Effects"
            enabled="true" x="200" y="200" width="80" height="44"/>
        <XCUIElementTypeTextField name="SearchField" label="Search here"
            enabled="true" x="50" y="300" width="280" height="36"/>
        <XCUIElementTypeScrollView name="MainScroll" label="Main Scroll"
            enabled="true" x="0" y="350" width="390" height="494">
          <XCUIElementTypeButton name="Item1" label="Item 1"
              enabled="true" x="10" y="360" width="370" height="60"/>
          <XCUIElementTypeButton label="Label Only"
              enabled="true" x="10" y="430" width="370" height="60"/>
          <XCUIElementTypeOther
              enabled="true" x="10" y="500" width="100" height="60"/>
          <XCUIElementTypeCell name="Cell-3" label="Cell 3"
              enabled="true" x="10" y="570" width="370" height="60"/>
        </XCUIElementTypeScrollView>
      </XCUIElementTypeOther>
    </XCUIElementTypeWindow>
  </XCUIElementTypeApplication>
</AppiumAUT>
"""


@pytest.fixture(scope="session")
def fixture_xml():
    return FIXTURE_XML


@pytest.fixture(scope="session")
def fixture_root(fixture_xml):
    return ET.fromstring(fixture_xml)


# ── Unit test client (no real server / device needed) ─────────────────────────

@pytest.fixture
def unit_client(fixture_root):
    """FastAPI TestClient with WDA and background tasks mocked out.

    Populates _cache["root"] with the fixture hierarchy so record endpoints
    can run hit_test without a real device.
    """
    import app.main as m
    from fastapi.testclient import TestClient

    async def _noop():
        pass

    m._steps.clear()
    m._cache["root"] = fixture_root

    with (
        patch("app.main.wda.connect", new_callable=AsyncMock),
        patch("app.main.wda.close", new_callable=AsyncMock),
        patch("app.main.wda.get_screenshot", new_callable=AsyncMock, return_value=None),
        patch("app.main._wda_heartbeat", side_effect=_noop),
        patch("app.main._mjpeg_frame_reader", side_effect=_noop),
        patch("app.main._hierarchy_loop", side_effect=_noop),
    ):
        with TestClient(m.app) as client:
            yield client

    m._steps.clear()
    m._cache["root"] = None


# ── Integration fixtures (require live server + device) ───────────────────────

@pytest.fixture(scope="session")
def client():
    """Synchronous httpx client shared across all integration tests."""
    with httpx.Client(base_url=BASE_URL, timeout=30.0) as c:
        yield c


@pytest.fixture(autouse=True)
def clear_steps(request):
    """Clear recorded steps before every test.

    For unit tests (marked @pytest.mark.unit): no-op — unit_client fixture
    already resets _steps.
    For integration tests: DELETE /api/steps via live server.
    """
    if request.node.get_closest_marker("unit"):
        yield
        return
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as c:
        c.delete("/api/steps")
    yield


@pytest.fixture()
def warm_tree(client):
    """Force-fetch the WDA element tree so _cache is populated."""
    resp = client.get("/api/tree")
    assert resp.status_code == 200, f"WDA unreachable: {resp.text}"
    return resp.json()
