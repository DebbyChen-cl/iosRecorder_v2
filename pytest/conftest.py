# ─────────────────────────────────────────────
# conftest.py  –  pytest fixtures (setup / teardown)
# ─────────────────────────────────────────────
# This file is automatically discovered by pytest.
# All fixtures defined here are available to every test module
# without an explicit import.

import logging
import os
from datetime import datetime

import pytest

from driver.driver_actions import DriverActions
from driver.driver_setup import create_driver, quit_driver

logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────
# Session-scoped driver (ONE Appium session for the whole suite)
# ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def driver():
    """
    Create the Appium driver once for the entire test session and quit it
    when all tests have finished.

    Scope: session  →  setup runs once before the first test,
                        teardown runs once after the last test.
    """
    logger.info("=== SESSION SETUP: creating Appium driver ===")
    _driver = create_driver()
    yield _driver
    logger.info("=== SESSION TEARDOWN: quitting Appium driver ===")
    quit_driver(_driver)


# ──────────────────────────────────────────────────────────────
# Function-scoped actions  (fresh wrapper per test)
# ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def actions(driver):
    """
    Provide a DriverActions instance that shares the session driver.
    Scope: function  →  a new DriverActions wrapper is created for
                        every individual test function.
    """
    return DriverActions(driver)


# ──────────────────────────────────────────────────────────────
# Automatic screenshot on failure
# ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    """
    Automatically capture a screenshot when a test FAILS.
    - Saves the PNG locally under screenshots/
    - Attaches it to the active ReportPortal launch via a log record
      (requires pytest-reportportal; silently skipped otherwise).
    """
    yield  # run the test

    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = request.node.nodeid.replace("/", "_").replace("::", "_")
        path = os.path.join(folder, f"{name}_{ts}.png")
        try:
            driver.save_screenshot(path)
            logger.info("Failure screenshot saved: %s", path)
            # ── Attach to ReportPortal via logging attachment extra ──────────
            with open(path, "rb") as fh:
                logger.info(
                    "Failure screenshot",
                    extra={
                        "attachment": {
                            "name": f"{name}.png",
                            "data": fh.read(),
                            "mime": "image/png",
                        }
                    },
                )
        except Exception as exc:
            logger.warning("Could not save failure screenshot: %s", exc)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Expose the test outcome on ``request.node.rep_call`` so that the
    ``screenshot_on_failure`` fixture can read it.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ──────────────────────────────────────────────────────────────
# Optional: reset app state between tests
# ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def reset_app(driver):
    """
    Terminate and re-launch the app before each test that uses this fixture.
    Use it selectively on tests that require a clean slate:

        def test_login(reset_app, actions):
            ...
    """
    import config
    bundle_id = config.IOS_CAPABILITIES.get("appium:bundleId", "")
    logger.info("Resetting app: %s", bundle_id)
    driver.terminate_app(bundle_id)
    driver.activate_app(bundle_id)
    yield
    # (no teardown needed – next test will reset again if required)
