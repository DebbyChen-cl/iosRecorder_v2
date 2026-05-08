# ─────────────────────────────────────────────
# tests/test_example.py  –  Sample test module
# ─────────────────────────────────────────────
# Demonstrates how to combine the driver, actions, and page fixtures.
# Replace with your real test cases.

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step
from driver.driver_actions import DriverActions
from pages.base_page import BasePage

@pytest.fixture(scope="module")
def home_page(driver, actions):
    """
    Provide a HomePage instance shared across all tests in this module.
    Module scope means the page object is created once per file, not once
    per test – adjust to 'function' scope if you need full isolation.
    """
    page = HomePage(driver, actions)
    page.wait_for_page_load()
    return page


@pytest.mark.name("Home page visibility")
def test_home_page_is_visible(self, home_page: HomePage):
    """The welcome label should be present when the app opens."""
    with step("[Verify] Home page is visible"):
        assert home_page.is_current_page(), "Home page did not load."

@pytest.mark.name("Welcome text content")
def test_welcome_text_not_empty(self, home_page: HomePage):
    """Welcome label should contain non-empty text."""
    with step("[Verify] Welcome text is not empty"):
        text = home_page.get_welcome_text()
        assert text, f"Expected non-empty welcome text, got: {text!r}"

@pytest.mark.name("Scroll functionality")
def test_scroll_down_and_back(self, actions: DriverActions):
    """Basic scroll smoke-test – should not raise."""
    actions.scroll("down")
    actions.scroll("up")

@pytest.mark.name("Search field input")
def test_search_field_accepts_input(self, home_page: HomePage):
    """Typing into the search field should succeed without error."""
    with step("[Verify] Search field accepts input"):
        home_page.search("pytest")

@pytest.mark.name("Search field various queries")
@pytest.mark.parametrize("query", ["login", "settings", "profile"])
def test_search_various_queries(self, home_page: HomePage, query: str):
    """Parameterised: each query should be accepted without crashing."""

    with step(f"[Action] Wait page loading"):
        home_page.wait_for_page_load()

    with step(f"[Verify] Search field accepts query: {query}"):
        home_page.search(query)

