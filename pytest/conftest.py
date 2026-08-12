# ─────────────────────────────────────────────
# conftest.py  –  pytest fixtures (setup / teardown)
# ─────────────────────────────────────────────
# This file is automatically discovered by pytest.
# All fixtures defined here are available to every test module
# without an explicit import.

import logging
import os
import shutil
import time
from datetime import datetime

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException

import auto_healing
import config
from driver.driver_actions import DriverActions
from driver.driver_setup import create_driver, quit_driver

logger = logging.getLogger(__name__)


_ONBOARDING_TIMEOUT_SEC = 10
_ALLOW_TIMEOUT_SEC = 10
_POPUP_LOOP_MAX = 3


_TAP_AFTER_DETECT_TIMEOUT_SEC = 3.0

# Folder every screenshot capture (capture_for_gt / capture_for_preview) writes to.
# Kept as the same relative path DriverActions uses, so both resolve against the
# same working directory.
_COMPARE_FOLDER = "pytest/screenshots/compare"


def _clean_compare_folder(folder: str = _COMPARE_FOLDER) -> None:
    """Delete everything inside the screenshot compare folder, keeping the folder."""
    if not os.path.isdir(folder):
        logger.info("Compare folder not found, nothing to clean: %s", folder)
        return

    removed = 0
    for entry in os.listdir(folder):
        path = os.path.join(folder, entry)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            removed += 1
        except OSError as exc:
            logger.warning("Failed to remove %s: %s", path, exc)

    logger.info("Cleaned %d item(s) from %s", removed, folder)


def _tap_if_present(actions: DriverActions, by: str, value: str, timeout: float) -> bool:
    """Tap an element when present within timeout; return True on tap.

    The detection timeout is deliberately short for popup sweeps, but the tap
    that follows must not reuse it: a popup caught mid fade-in can move or be
    re-created between the two lookups, and a 0.5 s re-find would silently fail.
    """
    try:
        if not actions.is_element_present(by, value, timeout=timeout):
            return False
        actions.tap_by_locator(by, value, timeout=max(timeout, _TAP_AFTER_DETECT_TIMEOUT_SEC))
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


_CRASH_DIALOG_TITLE = '“PhotoDirector: AI Photo Editor” Crashed'


def _close_crash_dialog(driver) -> bool:
    """Detect the native iOS 'app crashed' dialog and dismiss it via the Share > feedback flow."""
    logger.info("Search for crash dialog.")
    try:
        if not driver.find_elements(AppiumBy.NAME, _CRASH_DIALOG_TITLE):
            logger.info("No crash dialog present")
            return False

        logger.info("App crash detected, closing crash dialog.")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Share").click()

        feedback_field = driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Write your feedback here…"]'
        )
        feedback_field.send_keys("UI AT")
        logger.info("Entered feedback field, sending crash dialog.")

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Up")
        return True
    except Exception as exc:
        logger.warning("Crash dialog handling failed: %s", exc)
        return False


# 0.5 s is below WebDriverWait's poll interval, so it degrades into a single
# one-shot query — a popup still fading in is missed outright. Keep it long
# enough for a few polls, and sweep more rounds instead.
_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC = 2.0
_POST_LAUNCH_POPUP_LOOP_MAX = 1
_POST_LAUNCH_POPUP_LOOP_GAP_SEC = 1.0


def _case_continue_edit(actions: DriverActions) -> bool:
    """Dismiss the 'Would you like to continue editing?' dialog via Cancel."""
    if not actions.is_element_present(
        AppiumBy.NAME, "Would you like to continue editing?", timeout=_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC
    ):
        logger.info("No continue edit dialog pops up")
        return False

    if not _tap_if_present(actions, AppiumBy.ACCESSIBILITY_ID, "Cancel", timeout=3):
        logger.info("Tap cancel button fail")
        return False

    try:
        actions.wait_for_invisible(AppiumBy.NAME, "Would you like to continue editing?", timeout=5)
        logger.info("close continue_edit dialog")
        return True
    except Exception:
        logger.info("continue edit dialog still exists")
        return False


def _case_popup_close(actions: DriverActions) -> bool:
    if _tap_if_present(actions, AppiumBy.ACCESSIBILITY_ID, "closeButton", timeout=_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC):
        logger.info("close popup")
        return True
    logger.info("No popup close button")
    return False


def _case_iap_close(actions: DriverActions) -> bool:
    if _tap_if_present(actions, AppiumBy.ACCESSIBILITY_ID, "navCloseButton", timeout=_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC):
        logger.info("close IAP")
        return True
    logger.info("No IAP close button")
    return False


def _case_ai_banner(actions: DriverActions) -> bool:
    if _tap_if_present(actions, AppiumBy.ACCESSIBILITY_ID, "btnClose", timeout=_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC):
        logger.info("Closed AI Creation banner")
        return True
    logger.info("AI Creation banner not displayed on main page")
    return False


def _case_iap(actions: DriverActions) -> bool:
    if not _tap_if_present(actions, AppiumBy.ACCESSIBILITY_ID, "btnClose", timeout=_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC):
        logger.info("No IAP pops up")
        return False

    for value in ("Unlock premium features", "Start 7-Day Free Trial"):
        try:
            actions.wait_for_invisible(AppiumBy.NAME, value, timeout=2)
            logger.info("IAP closed")
            return True
        except Exception:
            continue

    logger.info("IAP still exists after tapping close")
    return False


def _case_avatar_back(actions: DriverActions) -> bool:
    if _tap_if_present(actions, AppiumBy.ACCESSIBILITY_ID, "backButton", timeout=_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC):
        logger.info("tap back button")
        return True
    logger.info("No Avatar pops up")
    return False


def _case_interstitial_new(actions: DriverActions) -> bool:
    if not _tap_if_present(
        actions, AppiumBy.ACCESSIBILITY_ID, "interstitialCloseButton", timeout=_POST_LAUNCH_POPUP_CHECK_TIMEOUT_SEC
    ):
        logger.info("No interstitial new pops up")
        return False

    try:
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, "interstitialCloseButton", timeout=2)
        logger.info("close interstitial new")
        return True
    except Exception:
        logger.info("interstitial new still exists")
        return False


_POST_LAUNCH_POPUP_CASES = [
    _case_popup_close,
    _case_iap_close,
    _case_ai_banner,
    _case_iap,
    _case_avatar_back,
    _case_interstitial_new,
]


def _close_all_pop_dialog_when_launch(actions: DriverActions) -> bool:
    """Close whichever post-launch popup (continue-edit / IAP / banner / interstitial) appears.

    Popups can chain (IAP closes, an interstitial takes its place), so every
    round runs all cases instead of stopping at the first hit, and the rounds
    are spaced out to give the next dialog time to animate in.
    """
    closed_any = False
    for i in range(_POST_LAUNCH_POPUP_LOOP_MAX):
        logger.info("Popup sweep %d/%d", i + 1, _POST_LAUNCH_POPUP_LOOP_MAX)
        if _case_continue_edit(actions):
            closed_any = True
        for case in _POST_LAUNCH_POPUP_CASES:
            if case(actions):
                logger.info("When Launch Executed for case %s", case.__name__)
                closed_any = True
        time.sleep(_POST_LAUNCH_POPUP_LOOP_GAP_SEC)

    return closed_any

def _allow_screenshot(actions: DriverActions) -> bool:
    actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 66.7, 47.1)
    actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 64.7, 69.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 59.2, 46.0)
    actions.tap_within_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]', 47.6, 48.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 65.0, 58.3)
    actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.3, 46.8)
    actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 53.6, 51.1)

    return True



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

    logger.info("=== SESSION PREP: close post-launch popup ===")
    _close_all_pop_dialog_when_launch(actions)

    logger.info('=== SESSION PREP: Allow screenshot')
    _allow_screenshot(actions)


# ──────────────────────────────────────────────────────────────
# Function-scoped driver (fresh Appium/WDA session per test)
# ──────────────────────────────────────────────────────────────

_session_first_run = True


@pytest.fixture(scope="function")
def driver():
    """
    Create a fresh Appium driver for every test function and quit it
    after the test finishes.

    First test of the session additionally runs onboarding and
    permission-alert flows; subsequent tests only restart the app.
    """
    global _session_first_run

    logger.info("=== Test Reset: Clean up compare folder ===")
    _clean_compare_folder()

    logger.info("=== TEST SETUP: creating fresh Appium driver ===")
    _driver = create_driver()
    # Publish the live session so auto-healing can grab failure evidence.
    auto_healing.set_active_driver(_driver)

    bundle_id = getattr(config, "TARGET_BUNDLE_ID", "") or config.IOS_CAPABILITIES.get("appium:bundleId", "")

    # if bundle_id:
    #     if _session_first_run:
    #         _session_setup_flow(DriverActions(_driver), bundle_id)
    #         _session_first_run = False
    #     else:
    #         logger.info("=== TEST SETUP: restarting app ===")
    #         _terminate_app_resilient(_driver, bundle_id)
    #         _close_crash_dialog(_driver)
    #         time.sleep(1)
    #         _driver.activate_app(bundle_id)
    #         time.sleep(1)
    #         _close_all_pop_dialog_when_launch(DriverActions(_driver))
            
    # else:
    #     logger.warning("Bundle ID is empty; skip app setup flow")

    yield _driver

    # logger.info("=== TEST TEARDOWN: quitting Appium driver ===")
    # if bundle_id:
    #     try:
    #         _driver.terminate_app(bundle_id)
    #     except Exception as exc:
    #         logger.warning("terminate_app failed: %s", exc)
    # quit_driver(_driver)
    # auto_healing.set_active_driver(None)


# ──────────────────────────────────────────────────────────────
# Function-scoped actions  (fresh wrapper per test)
# ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def actions(driver):
    """
    Provide a DriverActions instance wrapping the per-test driver.
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
    ``screenshot_on_failure`` fixture can read it, and collect auto-healing
    failure evidence while the Appium session is still alive.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if not auto_healing.ENABLED or not auto_healing.is_own_item(item):
        return

    if rep.failed and rep.when in ("setup", "call", "teardown"):
        try:
            auto_healing.collect_failure_evidence(item, rep, call)
        except Exception as exc:
            logger.warning("Failure evidence collection failed: %s", exc)
    if rep.when == "teardown":
        auto_healing.cleanup_passed_evidence(item)


# ──────────────────────────────────────────────────────────────
# Auto-Healing hooks  (implementation lives in auto_healing.py)
# ──────────────────────────────────────────────────────────────

# NOTE: the parameter must stay named `config` — pluggy matches hook arguments
# by name. It shadows the imported `config` module inside these two functions
# only; module-level users of `config` (the driver fixture) are unaffected.

def pytest_configure(config):
    """Record session start time and initialise the run's state.json."""
    auto_healing.configure(config)


def pytest_collection_modifyitems(config, items):
    """Bootstrap stable case ids; mark/skip items for agent-driven replay runs."""
    auto_healing.collection_modifyitems(config, items)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    """Immediate-retry protocol for crash/network failures (Lane A)."""
    return auto_healing.runtest_protocol(item, nextitem)


def pytest_sessionfinish(session, exitstatus):
    """Finalise state.json and hand deferred cases to the Phase 2 agent."""
    auto_healing.sessionfinish(session, exitstatus)


@pytest.fixture(autouse=True)
def _log_auto_healing_context():
    """Log the healing agent's current root_cause/patch summary onto this
    replay attempt's RP test item — the item closes when the test finishes,
    so this has to happen live, not after result.json is written."""
    if auto_healing.IS_REPLAY:
        context = os.environ.get("AUTO_HEALING_CONTEXT")
        if context:
            logger.info("[Auto-Healing] Context for this replay attempt:\n%s", context)
    yield


@pytest.fixture(autouse=True)
def _failure_evidence_workspace(request):
    """Provide one evidence folder path per test; keep it only when the test fails."""
    if not auto_healing.ENABLED or not auto_healing.is_own_item(request.node):
        yield
        return

    test_name = getattr(request.node, "originalname", request.node.name)
    evidence_dir = auto_healing.new_evidence_dir(test_name)
    request.node._failure_evidence_dir = evidence_dir
    request.node._failure_evidence_rel_dir = os.path.relpath(evidence_dir, auto_healing.PROJECT_ROOT)
    yield


# ──────────────────────────────────────────────────────────────
# Resilient terminate helper (used by driver fixture)
# ──────────────────────────────────────────────────────────────

_TERMINATE_MAX_RETRIES = 3
_TERMINATE_RETRY_DELAY_SEC = 1.0


def _terminate_app_resilient(driver, bundle_id: str) -> None:
    """Terminate the app, tolerating WDA proxy resets (ECONNRESET).

    ``mobile: terminateApp`` frequently returns an ECONNRESET while the app
    is actually being killed — WDA drops the connection mid-command. Retry a
    few times and treat a persistent failure as best-effort so the following
    activate_app still runs a clean cold start.
    """
    for attempt in range(1, _TERMINATE_MAX_RETRIES + 1):
        try:
            driver.terminate_app(bundle_id)
            return
        except WebDriverException as exc:
            logger.warning(
                "terminate_app attempt %d/%d failed: %s",
                attempt, _TERMINATE_MAX_RETRIES, exc,
            )
            time.sleep(_TERMINATE_RETRY_DELAY_SEC)
    logger.warning("terminate_app gave up after %d attempts; continuing", _TERMINATE_MAX_RETRIES)
