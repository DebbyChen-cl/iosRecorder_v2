"""
conftest.py — shared fixtures for recording pipeline integration tests.

Prerequisites:
  - The recorder server must be running on BASE_URL (default: http://localhost:8888)
  - WDA must be connected to a real iOS device
  - App must already be open at the correct screen before each test

Run:
  cd /Users/rdqe/iosRecorder_v2
  pytest unittest/ -v
"""

import httpx
import pytest

BASE_URL = "http://localhost:8888"


@pytest.fixture(scope="session")
def client():
    """Synchronous httpx client shared across all tests in the session."""
    with httpx.Client(base_url=BASE_URL, timeout=30.0) as c:
        yield c


@pytest.fixture(autouse=True)
def clear_steps(client):
    """Clear recorded steps before every test to avoid state pollution."""
    client.delete("/api/steps")
    yield


@pytest.fixture()
def warm_tree(client):
    """Force-fetch the WDA element tree so hit_test has data to work with.

    Call this fixture in tests that record coordinate-based actions (tap,
    long_press, verify_visible, etc.) to ensure _cache["root"] is populated
    before the first record call.
    """
    resp = client.get("/api/tree")
    assert resp.status_code == 200, f"WDA unreachable: {resp.text}"
    return resp.json()
