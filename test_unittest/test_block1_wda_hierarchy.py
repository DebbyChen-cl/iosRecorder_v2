"""
Block 1 — WDA Hierarchy Request

Tests that get_source() correctly fetches XML from WDA and parses it into an
ET.Element tree. All HTTP calls are mocked; no real device is needed.

Pass condition: ET.Element returned (not None), with expected tag structure.
"""

import asyncio
import xml.etree.ElementTree as ET
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

pytestmark = pytest.mark.unit

from app.wda import WDAClient, _parse_xml
from conftest import FIXTURE_XML


# ── _parse_xml ─────────────────────────────────────────────────────────────────

def test_parse_xml_returns_element():
    root = _parse_xml(FIXTURE_XML)
    assert isinstance(root, ET.Element)
    assert root.tag == "AppiumAUT"


def test_parse_xml_strips_doctype():
    xml_with_doctype = '<!DOCTYPE plist PUBLIC "-//DTD//" "">  ' + FIXTURE_XML
    root = _parse_xml(xml_with_doctype)
    assert isinstance(root, ET.Element)


def test_parse_xml_finds_children():
    root = _parse_xml(FIXTURE_XML)
    app_el = root.find(".//XCUIElementTypeApplication")
    assert app_el is not None
    assert app_el.attrib["name"] == "PhotoDirector"


# ── get_source (mocked HTTP) ───────────────────────────────────────────────────

def _make_mock_http(xml_text: str, status_code: int = 200):
    """Return an AsyncMock httpx client that replies with the given XML."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = {"value": xml_text}
    mock_resp.text = xml_text

    mock_http = AsyncMock()
    mock_http.get = AsyncMock(return_value=mock_resp)
    return mock_http


async def _get_source_with_mock(xml_text: str, status_code: int = 200):
    client = WDAClient("http://localhost:8100")
    client._client = _make_mock_http(xml_text, status_code)
    client._session_id = "fake-session-id"
    return await client.get_source()


def test_get_source_returns_element():
    root = asyncio.run(_get_source_with_mock(FIXTURE_XML))
    assert isinstance(root, ET.Element)
    assert root.tag == "AppiumAUT"


def test_get_source_returns_none_on_404():
    root = asyncio.run(_get_source_with_mock(FIXTURE_XML, status_code=404))
    assert root is None


def test_get_source_returns_none_on_500():
    root = asyncio.run(_get_source_with_mock(FIXTURE_XML, status_code=500))
    assert root is None


def test_get_source_returns_none_without_session():
    async def _run():
        client = WDAClient("http://localhost:8100")
        client._client = _make_mock_http(FIXTURE_XML)
        # No session — _adopt_session will be called. Mock it to return False.
        client._adopt_session = AsyncMock(return_value=False)
        return await client.get_source()

    root = asyncio.run(_run())
    assert root is None


def test_get_source_element_has_buttons():
    root = asyncio.run(_get_source_with_mock(FIXTURE_XML))
    buttons = root.findall(".//XCUIElementTypeButton")
    assert len(buttons) >= 4
    names = [b.attrib.get("name", "") for b in buttons]
    assert "SaveButton" in names
    assert "Item1" in names
