#!/usr/bin/env python3
"""Launch PhotoDirector on the iOS device through its custom URL scheme.

Standalone helper: no pytest, no conftest fixtures. It creates its own Appium
session, delivers the deep link with `mobile: deepLink`, and reports whether the
app actually came to the foreground.

    python launch_phd_deeplink.py
    python launch_phd_deeplink.py --url "clphd://uiTest?skipLaunchPopups=true"
    python launch_phd_deeplink.py --keep-session      # leave the session alive
    python launch_phd_deeplink.py --no-terminate      # don't kill the app first

Defaults come from the project's config.py when this file is run from inside the
repo; every one of them can be overridden on the command line, so the script
also works on a machine that only has this file plus Appium-Python-Client.
"""

from __future__ import annotations

import argparse
import logging
import os
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import urlopen

from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.common.exceptions import WebDriverException

logger = logging.getLogger("launch_phd")

_HERE = os.path.dirname(os.path.abspath(__file__))
_START_WDA_SCRIPT = os.path.join(_HERE, "scripts", "start_wda.sh")

# ── Fallback defaults, used only when config.py is not importable ────────────
_FALLBACK = {
    "APPIUM_SERVER_URL": "http://localhost:4723",
    "TARGET_BUNDLE_ID": "com.cyberlink.photodirector",
    "LAUNCH_DEEPLINK_URL": "clphd://uiTest?skipLaunchPopups=true",
    "IOS_CAPABILITIES": {
        "platformName": "iOS",
        "appium:automationName": "XCUITest",
        "appium:udid": "",
        "appium:deviceName": "",
        "appium:bundleId": "com.cyberlink.photodirector",
        "appium:noReset": True,
        "appium:fullReset": False,
        "appium:autoLaunch": False,
        "appium:newCommandTimeout": 600,
        "appium:waitForQuiescence": False,
        "appium:webDriverAgentUrl": "http://localhost:8100",
        "appium:wdaConnectionTimeout": 240000,
        "appium:useNewWDA": False,
        "appium:skipServerInstallation": True,
    },
}

try:  # the repo's own settings win when they are available
    sys.path.insert(0, _HERE)
    import config as _config  # type: ignore
except Exception:  # pragma: no cover - only hit outside the repo
    _config = None


def _default(name):
    if _config is not None and hasattr(_config, name):
        return getattr(_config, name)
    return _FALLBACK[name]


# ── WDA tunnel ───────────────────────────────────────────────────────────────
# `appium:webDriverAgentUrl` points at an iproxy tunnel on this Mac, not at
# device-side WDA. The tunnel dies with the shell that created it, so probe it
# and rebuild it before asking Appium for a session — same contract as
# driver/driver_setup.ensure_wda_tunnel.

def _wda_responds(status_url: str, timeout: int = 15) -> bool:
    try:
        with urlopen(status_url, timeout=timeout) as response:
            return 200 <= response.status < 300
    except (HTTPError, URLError, OSError, ValueError) as exc:
        logger.debug("WDA probe failed at %s: %s", status_url, exc)
        return False


def ensure_wda_tunnel(wda_url: str, udid: str) -> None:
    """Rebuild the local iproxy tunnel when port 8100 is dead."""
    wda_url = (wda_url or "").rstrip("/")
    if not wda_url:
        return  # Appium manages its own WDA

    status_url = f"{wda_url}/status"
    if _wda_responds(status_url):
        logger.info("WDA tunnel is ready: %s", status_url)
        return

    logger.warning("WDA tunnel is down at %s - restarting it", status_url)
    if not udid:
        raise RuntimeError("--udid is required to restart the WDA tunnel")
    if not os.path.exists(_START_WDA_SCRIPT):
        raise RuntimeError(f"WDA tunnel is down and {_START_WDA_SCRIPT} is missing")

    env = {
        **os.environ,
        "WDA_UDID": str(udid),
        "WDA_LOCAL_PORT": str(urlparse(wda_url).port or 8100),
    }
    result = subprocess.run(
        ["bash", _START_WDA_SCRIPT],
        env=env, capture_output=True, text=True, timeout=90, start_new_session=True,
    )
    for line in (result.stdout or "").splitlines():
        logger.info("%s", line)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(f"Could not restart the WDA tunnel for {udid}: {detail}")

    for attempt in range(1, 4):
        if _wda_responds(status_url):
            logger.info("WDA tunnel restarted: %s", status_url)
            return
        if attempt < 3:
            time.sleep(1)
    raise RuntimeError(f"The WDA tunnel for {udid} still does not answer {status_url}")


# ── Session ──────────────────────────────────────────────────────────────────

_FIRST_CLASS = {
    "appium:automationName", "appium:udid", "appium:deviceName", "appium:bundleId",
    "appium:xcodeOrgId", "appium:xcodeSigningId", "appium:noReset",
    "appium:fullReset", "appium:newCommandTimeout",
}


def build_options(caps: dict) -> XCUITestOptions:
    options = XCUITestOptions()
    options.platform_name       = caps["platformName"]
    options.automation_name     = caps["appium:automationName"]
    options.udid                = caps["appium:udid"]
    options.device_name         = caps.get("appium:deviceName")
    if caps.get("appium:bundleId"):
        options.bundle_id = caps["appium:bundleId"]
    options.xcode_org_id        = caps.get("appium:xcodeOrgId")
    options.xcode_signing_id    = caps.get("appium:xcodeSigningId")
    options.no_reset            = caps.get("appium:noReset", True)
    options.full_reset          = caps.get("appium:fullReset", False)
    options.new_command_timeout = caps.get("appium:newCommandTimeout", 600)
    for key, value in caps.items():
        if key.startswith("appium:") and key not in _FIRST_CLASS:
            options.set_capability(key, value)
    return options


def launch_via_deeplink(driver, url: str, bundle_id: str) -> None:
    """Cold-start the app through its custom URL scheme."""
    driver.execute_script("mobile: deepLink", {"url": url, "bundleId": bundle_id})
    logger.info("Delivered deep link to %s: %s", bundle_id, url)


# XCUITest app states: 1 not running, 2 background suspended,
# 3 background running, 4 foreground.
def _app_state(driver, bundle_id: str) -> int:
    try:
        return int(driver.query_app_state(bundle_id))
    except WebDriverException as exc:
        logger.warning("query_app_state failed: %s", exc)
        return -1


def main(argv=None) -> int:
    caps_defaults = dict(_default("IOS_CAPABILITIES"))

    parser = argparse.ArgumentParser(description="Launch PHD through its deep link.")
    parser.add_argument("--url", default=_default("LAUNCH_DEEPLINK_URL"),
                        help="deep link to open (default: %(default)s)")
    parser.add_argument("--bundle-id", default=_default("TARGET_BUNDLE_ID")
                        or caps_defaults.get("appium:bundleId"),
                        help="bundle id of the app under test")
    parser.add_argument("--udid", default=caps_defaults.get("appium:udid"),
                        help="device UDID")
    parser.add_argument("--device-name", default=caps_defaults.get("appium:deviceName"))
    parser.add_argument("--server", default=_default("APPIUM_SERVER_URL"),
                        help="Appium server URL (default: %(default)s)")
    parser.add_argument("--wda-url", default=caps_defaults.get("appium:webDriverAgentUrl"),
                        help='externally managed WDA URL; "" lets Appium build its own')
    parser.add_argument("--no-terminate", action="store_true",
                        help="skip terminating the app before the deep link")
    parser.add_argument("--keep-session", action="store_true",
                        help="leave the Appium session open instead of quitting")
    parser.add_argument("--settle", type=float, default=3.0,
                        help="seconds to wait after the deep link (default: %(default)s)")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        datefmt="%H:%M:%S",
    )

    if not args.url:
        parser.error("no deep link to open: pass --url or set LAUNCH_DEEPLINK_URL in config.py")
    if not args.bundle_id:
        parser.error("no bundle id: pass --bundle-id or set TARGET_BUNDLE_ID in config.py")
    if not args.udid:
        parser.error("no device UDID: pass --udid or set appium:udid in config.py")

    caps = {
        **caps_defaults,
        "appium:udid": args.udid,
        "appium:deviceName": args.device_name,
        "appium:bundleId": args.bundle_id,
    }
    if args.wda_url:
        caps["appium:webDriverAgentUrl"] = args.wda_url
    else:
        caps.pop("appium:webDriverAgentUrl", None)

    ensure_wda_tunnel(caps.get("appium:webDriverAgentUrl", ""), args.udid)

    logger.info("Connecting to Appium at %s", args.server)
    try:
        driver = webdriver.Remote(command_executor=args.server, options=build_options(caps))
    except Exception as exc:
        logger.error("Failed to create the Appium session. Is Appium running at %s? %s",
                     args.server, exc)
        return 2
    logger.info("Session created: %s", driver.session_id)

    try:
        if not args.no_terminate:
            try:
                driver.terminate_app(args.bundle_id)
                logger.info("Terminated %s", args.bundle_id)
                time.sleep(1)
            except WebDriverException as exc:
                logger.warning("terminate_app failed (continuing): %s", exc)

        try:
            launch_via_deeplink(driver, args.url, args.bundle_id)
        except WebDriverException as exc:
            # Older XCUITest drivers and unregistered schemes both land here;
            # a plain activate at least leaves the device in a usable state.
            logger.error("Deep link launch failed: %s", exc)
            logger.info("Falling back to a plain activate_app")
            try:
                driver.activate_app(args.bundle_id)
            except WebDriverException as fallback_exc:
                logger.error("activate_app also failed: %s", fallback_exc)
                return 1
            return 1

        if args.settle > 0:
            time.sleep(args.settle)

        state = _app_state(driver, args.bundle_id)
        if state == 4:
            logger.info("%s is in the foreground.", args.bundle_id)
            return 0
        logger.error("%s did not reach the foreground (app state = %s).",
                     args.bundle_id, state)
        return 1
    finally:
        if args.keep_session:
            logger.info("Leaving the session open: %s", driver.session_id)
        else:
            try:
                driver.quit()
                logger.info("Appium session closed.")
            except Exception as exc:
                logger.warning("Error while quitting the driver: %s", exc)


if __name__ == "__main__":
    sys.exit(main())
