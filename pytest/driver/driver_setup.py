# ─────────────────────────────────────────────
# driver/driver_setup.py  –  Appium driver factory
# ─────────────────────────────────────────────
# Responsible ONLY for creating and destroying the
# WebDriver session against a physical iOS device.

import logging
import os
import subprocess
import time
from typing import Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import urlopen

from appium import webdriver
from appium.options.ios import XCUITestOptions

import config

logger = logging.getLogger(__name__)

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_START_WDA_SCRIPT = os.path.join(_PROJECT_ROOT, "scripts", "start_wda.sh")

WDA_READY_ATTEMPTS = 3
WDA_READY_REQUEST_TIMEOUT_SECONDS = 15
WDA_READY_RETRY_DELAY_SECONDS = 1
WDA_TUNNEL_START_TIMEOUT_SECONDS = 90


def _wda_responds(status_url: str) -> bool:
    """True when the local WDA tunnel answers /status with a 2xx."""
    try:
        with urlopen(status_url, timeout=WDA_READY_REQUEST_TIMEOUT_SECONDS) as response:
            return 200 <= response.status < 300
    except (HTTPError, URLError, OSError, ValueError) as exc:
        logger.debug("WDA probe failed at %s: %s", status_url, exc)
        return False


def ensure_wda_tunnel(capabilities: Mapping[str, object] | None = None) -> None:
    """Make sure the local WDA tunnel answers before a session is created.

    `appium:webDriverAgentUrl` points at an iproxy tunnel on this Mac, not at
    device-side WDA. The tunnel dies with the shell that created it, so the
    Phase 2 healing replay — a separate pytest process started after the main
    run's shell is gone — kept finding port 8100 dead and failed every test
    with "Could not proxy command to the remote server".

    scripts/start_wda.sh reuses a healthy tunnel for the same UDID and only
    ever manages the local iproxy process, never device-side WDA.

    Raises:
        RuntimeError: if the tunnel cannot be brought up (most often because
            device-side WDA itself is not running, which only Xcode can fix).
    """
    caps = dict(capabilities or config.IOS_CAPABILITIES)
    wda_url = str(caps.get("appium:webDriverAgentUrl", "")).rstrip("/")
    if not wda_url:
        # No externally managed WDA: Appium builds and launches its own.
        return

    status_url = f"{wda_url}/status"
    if _wda_responds(status_url):
        logger.info("WDA tunnel is ready: %s", status_url)
        return

    logger.warning("WDA tunnel is down at %s - restarting it", status_url)

    udid = caps.get("appium:udid")
    if not udid:
        raise RuntimeError("appium:udid is required to restart the WDA tunnel")
    if not os.path.exists(_START_WDA_SCRIPT):
        raise RuntimeError(f"WDA tunnel is down and {_START_WDA_SCRIPT} is missing")

    env = {
        **os.environ,
        "WDA_UDID": str(udid),
        "WDA_LOCAL_PORT": str(urlparse(wda_url).port or 8100),
    }
    # start_new_session detaches iproxy from this pytest run's process group so
    # the tunnel outlives the run — otherwise the next replay would have to
    # rebuild it all over again.
    result = subprocess.run(
        ["bash", _START_WDA_SCRIPT],
        env=env,
        capture_output=True,
        text=True,
        timeout=WDA_TUNNEL_START_TIMEOUT_SECONDS,
        start_new_session=True,
    )
    for line in (result.stdout or "").splitlines():
        logger.info("%s", line)

    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(f"Could not restart the WDA tunnel for {udid}: {detail}")

    for attempt in range(1, WDA_READY_ATTEMPTS + 1):
        if _wda_responds(status_url):
            logger.info("WDA tunnel restarted: %s", status_url)
            return
        if attempt < WDA_READY_ATTEMPTS:
            time.sleep(WDA_READY_RETRY_DELAY_SECONDS)

    raise RuntimeError(
        f"The WDA tunnel for {udid} was restarted but still does not answer {status_url}"
    )


def build_options(capabilities: Mapping[str, object] | None = None) -> XCUITestOptions:
    """Convert the capability dict in config.py into an XCUITestOptions object."""
    caps = dict(capabilities or config.IOS_CAPABILITIES)
    options = XCUITestOptions()

    options.platform_name        = caps["platformName"]
    options.automation_name      = caps["appium:automationName"]
    options.udid                 = caps["appium:udid"]
    options.device_name          = caps["appium:deviceName"]
    bundle_id = caps.get("appium:bundleId")
    if bundle_id:
        options.bundle_id = bundle_id
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


def create_driver(capabilities: Mapping[str, object] | None = None) -> webdriver.Remote:
    """
    Start a new Appium session and return the driver.

    Raises:
        RuntimeError: if the WDA tunnel cannot be brought up, the Appium server
            is unreachable, or session creation fails.
    """
    ensure_wda_tunnel(capabilities)
    options = build_options(capabilities)
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
