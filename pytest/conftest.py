# ─────────────────────────────────────────────
# conftest.py  –  pytest fixtures (setup / teardown)
# ─────────────────────────────────────────────
# This file is automatically discovered by pytest.
# All fixtures defined here are available to every test module
# without an explicit import.

import logging
import os
import time
from datetime import datetime

import pytest
from appium.webdriver.common.appiumby import AppiumBy

import config
from driver.driver_actions import DriverActions
from driver.driver_setup import create_driver, quit_driver

logger = logging.getLogger(__name__)


_ONBOARDING_TIMEOUT_SEC = 10
_ALLOW_TIMEOUT_SEC = 10
_POPUP_LOOP_MAX = 3


def _tap_if_present(actions: DriverActions, by: str, value: str, timeout: int) -> bool:
    """Tap an element when present within timeout; return True on tap."""
    try:
        if not actions.is_element_present(by, value, timeout=timeout):
            return False
        actions.tap_by_locator(by, value, timeout=timeout)
        logger.info("Tapped element (%s, %r)", by, value)
        return True
    except Exception as exc:
        logger.info("Tap skipped for (%s, %r): %s", by, value, exc)
        return False


def _run_onboarding_if_needed(actions: DriverActions) -> None:
    """Run onboarding C-1..C-5 only when C-1 is found within 10 seconds."""
    logger.info("Checking onboarding entry button C-1")
    c1_found = _tap_if_present(actions, AppiumBy.NAME, "Next", _ONBOARDING_TIMEOUT_SEC)
    if not c1_found:
        logger.info("C-1 not found within %ss; skip C-2..C-5", _ONBOARDING_TIMEOUT_SEC)
        return

    # Continue best-effort onboarding path after C-1 appears.
    _tap_if_present(actions, AppiumBy.NAME, "Start Testing", _ONBOARDING_TIMEOUT_SEC)
    _tap_if_present(actions, AppiumBy.NAME, "Next", _ONBOARDING_TIMEOUT_SEC)
    _tap_if_present(actions, AppiumBy.NAME, "Next", _ONBOARDING_TIMEOUT_SEC)
    _tap_if_present(actions, AppiumBy.NAME, "Let's go", _ONBOARDING_TIMEOUT_SEC)


def _close_in_app_popup(actions: DriverActions) -> None:
    """Try D-1 -> D-2 -> D-3 in loops; click first hit then stop."""
    candidates = [
        (AppiumBy.ACCESSIBILITY_ID, "navCloseButton", "D-1 IAP/Trial"),
        (AppiumBy.ACCESSIBILITY_ID, "wdlOfferCloseButton", "D-2 Promotion"),
        (AppiumBy.ACCESSIBILITY_ID, "btnClose", "D-3 Generic close"),
    ]

    for idx in range(_POPUP_LOOP_MAX):
        logger.info("Popup close loop %d/%d", idx + 1, _POPUP_LOOP_MAX)
        for by, value, label in candidates:
            if _tap_if_present(actions, by, value, timeout=2):
                logger.info("Closed popup via %s", label)
                return
    logger.info("No popup matched after %d loops", _POPUP_LOOP_MAX)


def _handle_ios_permission_alerts(actions: DriverActions) -> None:
    """Handle ATT and Push permission alerts by tapping Allow twice."""
    if _tap_if_present(actions, AppiumBy.NAME, "Allow", _ALLOW_TIMEOUT_SEC):
        logger.info("Allowed App Tracking Transparency")
    else:
        logger.info("ATT allow button not found within %ss", _ALLOW_TIMEOUT_SEC)

    if _tap_if_present(actions, AppiumBy.NAME, "Allow", _ALLOW_TIMEOUT_SEC):
        logger.info("Allowed Push notification")
    else:
        logger.info("Push allow button not found within %ss", _ALLOW_TIMEOUT_SEC)


def _session_setup_flow(actions: DriverActions, bundle_id: str) -> None:
    """Run the requested one-time pre-test setup flow."""
    logger.info("=== SESSION PREP: restart app ===")
    actions.terminate_app(bundle_id)
    time.sleep(1)
    actions.launch_app(bundle_id)

    logger.info("=== SESSION PREP: onboarding ===")
    _run_onboarding_if_needed(actions)

    logger.info("=== SESSION PREP: close in-app popup ===")
    _close_in_app_popup(actions)

    logger.info("=== SESSION PREP: iOS permission alerts ===")
    _handle_ios_permission_alerts(actions)


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
    actions = DriverActions(_driver)
    bundle_id = config.IOS_CAPABILITIES.get("appium:bundleId", "")
    # if bundle_id:
    #     _session_setup_flow(actions, bundle_id)
    # else:
    #     logger.warning("Bundle ID is empty; skip session app setup flow")

    yield _driver

    logger.info("=== SESSION TEARDOWN: terminate app and quit Appium driver ===")
    # if bundle_id:
    #     try:
    #         actions.terminate_app(bundle_id)
    #     except Exception as exc:
    #         logger.warning("Session terminate_app failed: %s", exc)
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
    - Saves the PNG locally under pytest/screenshots/error/
    - Attaches it to the active ReportPortal launch via a log record
      (requires pytest-reportportal; silently skipped otherwise).
    """
    yield  # run the test

    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        folder = "pytest/screenshots/error"
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
    bundle_id = config.IOS_CAPABILITIES.get("appium:bundleId", "")
    logger.info("Resetting app: %s", bundle_id)
    driver.terminate_app(bundle_id)
    driver.activate_app(bundle_id)
    yield
    # (no teardown needed – next test will reset again if required)
