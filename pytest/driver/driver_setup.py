# ─────────────────────────────────────────────
# driver/driver_setup.py  –  Appium driver factory
# ─────────────────────────────────────────────
# Responsible ONLY for creating and destroying the
# WebDriver session against a physical iOS device.

import logging
from appium import webdriver
from appium.options.ios import XCUITestOptions

import config

logger = logging.getLogger(__name__)


def build_options() -> XCUITestOptions:
    """Convert the capability dict in config.py into an XCUITestOptions object."""
    caps = config.IOS_CAPABILITIES
    options = XCUITestOptions()

    options.platform_name        = caps["platformName"]
    options.automation_name      = caps["appium:automationName"]
    options.udid                 = caps["appium:udid"]
    options.device_name          = caps["appium:deviceName"]
    options.bundle_id            = caps.get("appium:bundleId")
    options.xcode_org_id         = caps.get("appium:xcodeOrgId")
    options.xcode_signing_id     = caps.get("appium:xcodeSigningId")
    options.no_reset             = caps.get("appium:noReset", True)
    options.full_reset           = caps.get("appium:fullReset", False)
    options.new_command_timeout  = caps.get("appium:newCommandTimeout", 120)

    # Pass any remaining appium: capabilities that XCUITestOptions doesn't expose
    # as a first-class property via the generic set_capability interface.
    # (e.g. wdaLocalPort, skipServerInstallation, useNewWDA, showXcodeLog, …)
    _first_class = {
        "appium:automationName", "appium:udid", "appium:deviceName",
        "appium:bundleId", "appium:xcodeOrgId", "appium:xcodeSigningId",
        "appium:noReset", "appium:fullReset", "appium:newCommandTimeout",
    }
    for key, value in caps.items():
        if key.startswith("appium:") and key not in _first_class:
            options.set_capability(key, value)

    return options


def create_driver() -> webdriver.Remote:
    """
    Start a new Appium session and return the driver.

    Raises:
        RuntimeError: if Appium server is unreachable or session creation fails.
    """
    options = build_options()
    logger.info("Connecting to Appium at %s", config.APPIUM_SERVER_URL)
    try:
        driver = webdriver.Remote(
            command_executor=config.APPIUM_SERVER_URL,
            options=options,
        )
        logger.info("Session created: %s", driver.session_id)
        return driver
    except Exception as exc:
        raise RuntimeError(
            f"Failed to create Appium session. "
            f"Is Appium running at {config.APPIUM_SERVER_URL}? Details: {exc}"
        ) from exc


def quit_driver(driver: webdriver.Remote) -> None:
    """Gracefully close the Appium session."""
    if driver:
        try:
            driver.quit()
            logger.info("Appium session closed.")
        except Exception as exc:
            logger.warning("Error while quitting driver: %s", exc)
