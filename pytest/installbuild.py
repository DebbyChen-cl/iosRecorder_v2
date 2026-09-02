import argparse
import configparser
import logging
import os
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    InvalidSessionIdException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.support.ui import WebDriverWait

import config
from build_info import save_build_info
from driver.driver_actions import DriverActions
from driver.driver_setup import create_driver, quit_driver


BUNDLE_ID = "com.apple.TestFlight"
TARGET_APP_BUNDLE_ID = "com.cyberlink.photodirector"
TARGET_APP_NAME = "PhotoDirector: AI Photo Editor"
MAX_ATTEMPTS = 5
RETRY_DELAY_SECONDS = 180
WDA_READY_ATTEMPTS = 3
WDA_READY_REQUEST_TIMEOUT_SECONDS = 15
WDA_READY_RETRY_DELAY_SECONDS = 1

logger = logging.getLogger(__name__)


class BuildMismatchError(RuntimeError):
    """Raised when the located TestFlight build does not match requested version/build."""


def wait_for_wda_ready(capabilities: dict[str, object]) -> None:
    """Wait for the configured device's WDA tunnel to answer /status.

    Jenkins prepares the local tunnel for the configured UDID. The installer
    only verifies readiness, so it never manages or interrupts device-side WDA.
    """
    wda_url = str(capabilities.get("appium:webDriverAgentUrl", "")).rstrip("/")
    if not wda_url:
        raise RuntimeError("appium:webDriverAgentUrl is required for the externally managed WDA")

    status_url = f"{wda_url}/status"
    last_error = None
    for attempt in range(1, WDA_READY_ATTEMPTS + 1):
        try:
            with urlopen(status_url, timeout=WDA_READY_REQUEST_TIMEOUT_SECONDS) as response:
                if 200 <= response.status < 300:
                    logger.info("Configured device WDA is ready: %s", status_url)
                    return
                last_error = RuntimeError(f"HTTP {response.status}")
        except (HTTPError, URLError, OSError, ValueError) as exc:
            last_error = exc

        logger.warning(
            "WDA readiness probe %s/%s failed at %s: %s",
            attempt,
            WDA_READY_ATTEMPTS,
            status_url,
            last_error,
        )
        if attempt < WDA_READY_ATTEMPTS:
            time.sleep(WDA_READY_RETRY_DELAY_SECONDS)

    raise RuntimeError(
        f"Configured device WDA is not ready at {status_url}. "
        "Start WebDriverAgent for the configured device, then rerun the installer. "
        f"Last error: {last_error}"
    )


def create_ready_driver():
    """Create an Appium session that is verified against the configured WDA."""
    capabilities = dict(config.IOS_CAPABILITIES)
    capabilities["appium:bundleId"] = BUNDLE_ID
    capabilities["appium:autoLaunch"] = False
    driver = None
    for attempt in range(1, WDA_READY_ATTEMPTS + 1):
        wait_for_wda_ready(capabilities)
        try:
            driver = create_driver(capabilities)
            # Kept from update_testflight_app.py: this verifies the live
            # Appium/WDA session and also keeps it active during retries.
            driver.get_window_size()
            logger.info("TestFlight Appium/WDA session is ready")
            return driver
        except (RuntimeError, WebDriverException) as exc:
            logger.warning(
                "Appium/WDA session readiness %s/%s failed: %s",
                attempt,
                WDA_READY_ATTEMPTS,
                exc,
            )
            quit_driver(driver)
            driver = None
            if attempt == WDA_READY_ATTEMPTS:
                raise
            time.sleep(WDA_READY_RETRY_DELAY_SECONDS)

    raise RuntimeError("Could not create a ready Appium/WDA session")


class TestFlightSession:
    """Own the Appium session so a dropped WDA session can be replaced.

    WDA can drop its session while the installer works on the device - the
    target app uninstall alone is enough to do it - and every later command
    then fails with InvalidSessionIdException. Holding the driver here lets
    the installer rebuild the session instead of failing the Jenkins stage.
    """

    def __init__(self) -> None:
        self.driver = None
        self.actions = None

    def start(self) -> DriverActions:
        self.driver = create_ready_driver()
        self.actions = DriverActions(self.driver)
        return self.actions

    def restart(self) -> DriverActions:
        logger.warning("Recreating the Appium/WDA session")
        self.close()
        return self.start()

    def close(self) -> None:
        if self.driver:
            quit_driver(self.driver)
        self.driver = None
        self.actions = None

    def ensure_alive(self) -> None:
        """Recreate the session when WDA no longer answers for it."""
        if self.driver is not None:
            try:
                self.driver.get_window_size()
                return
            except WebDriverException as exc:
                logger.warning("Appium/WDA session is no longer usable: %s", exc)
        self.restart()

    def launch_testflight(self) -> None:
        """Foreground TestFlight, rebuilding the session when WDA lost it."""
        try:
            self.actions.launch_app(BUNDLE_ID)
            return
        except InvalidSessionIdException as exc:
            logger.warning("TestFlight launch hit a dead session: %s", exc)
        self.restart()
        self.actions.launch_app(BUNDLE_ID)

    def terminate_testflight(self) -> None:
        """Force quit TestFlight; a lost session is recovered on next launch."""
        try:
            self.actions.terminate_app(BUNDLE_ID)
        except WebDriverException as exc:
            logger.info("Could not terminate TestFlight: %s", exc)


def parse_jenkins_build(raw: str) -> tuple[str, str]:
    """Parse 'x.y.z.buildno' from Jenkins build string."""
    clean = raw.split(":")[-1].strip()
    last_dot = clean.rfind(".")
    if last_dot == -1:
        raise ValueError(f"Could not find separator '.' in string: {clean}")
    return clean[:last_dot], clean[last_dot + 1 :]


def _find_first_action_button(actions: DriverActions):
    """Find the first matching action button in TestFlight card/order of preference."""
    for button_id in ("Install", "Update", "Open"):
        items = actions.find_elements(AppiumBy.ACCESSIBILITY_ID, button_id, timeout=2)
        if items:
            return items[0]
    return None


def _element_text(el) -> str:
    return (el.text or el.get_attribute("name") or "").strip()


def _find_app_card(actions: DriverActions, max_scrolls: int = 4):
    """Try to find app card in TestFlight app list with small scroll fallback."""
    for _ in range(max_scrolls):
        try:
            return actions.find_element(AppiumBy.ACCESSIBILITY_ID, TARGET_APP_NAME, timeout=4)
        except TimeoutException:
            actions.scroll("down")
            time.sleep(0.8)
    raise NoSuchElementException(f"App '{TARGET_APP_NAME}' not found")


def _wait_for_open_button(driver, timeout: int = 600) -> None:
    WebDriverWait(driver, timeout).until(
        lambda d: len(d.find_elements(AppiumBy.ACCESSIBILITY_ID, "Open")) > 0
    )


def _assert_target_build_text(build_name: str, prod_ver: str, build_no: str) -> None:
    """Validate version/build tokens while tolerating TestFlight's spacing."""
    normalized = (build_name or "").strip()
    compact_name = "".join(normalized.split())
    compact_version = "".join((prod_ver or "").split())
    if compact_version not in compact_name or f"({build_no})" not in compact_name:
        raise BuildMismatchError(
            "Wrong build detected in Previous Builds: "
            f"expected version={prod_ver} build={build_no}, got='{normalized}'"
        )


def _check_main_page_build(actions: DriverActions, prod_ver: str, build_no: str) -> bool:
    """Check build on app card/main page and install/update when available."""
    target_build = f"Version {prod_ver} ({build_no})"
    logger.info("Checking main page for build: %s", target_build)

    try:
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, target_build, timeout=8)
    except TimeoutException:
        logger.info("Build %s not found on main page", target_build)
        return False

    button = _find_first_action_button(actions)
    if not button:
        raise NoSuchElementException("Could not find Install/Update/Open button")

    button_text = _element_text(button)
    logger.info("Found action button: %s", button_text or "<empty>")
    if button_text.lower() == "open":
        logger.info("Target build is already installed and openable")
        return True

    actions.tap(button)
    logger.info("Install/Update clicked, waiting for Open")
    _wait_for_open_button(actions.driver)
    logger.info("Install/Update complete")
    return True


def check_previous_builds(actions: DriverActions, prod_ver: str, build_no: str) -> bool:
    """Navigate to Previous Builds and install the exact build when available.

    TestFlight can background itself while the main-card build lookup waits.
    Always foreground it and locate a fresh card here instead of tapping an
    element retained from the earlier lookup.
    """
    try:
        logger.info("Reopening TestFlight and locating a fresh app card")
        actions.launch_app(BUNDLE_ID)
        app_element = _find_app_card(actions)

        logger.info("Opening app details page")
        actions.tap(app_element)
        time.sleep(1.5)

        previous_builds_element = None
        for _ in range(6):
            candidates = actions.find_elements(AppiumBy.ACCESSIBILITY_ID, "Previous Builds", timeout=2)
            if candidates:
                previous_builds_element = candidates[0]
                break
            actions.scroll("down")
            time.sleep(0.8)

        if not previous_builds_element:
            logger.info("'Previous Builds' not found")
            return False

        actions.tap(previous_builds_element)
        time.sleep(1.2)

        logger.info("Looking for exact version: %s", prod_ver)
        try:
            version_element = actions.find_element(AppiumBy.ACCESSIBILITY_ID, prod_ver, timeout=10)
        except TimeoutException as exc:
            raise BuildMismatchError(
                f"Requested version not found in Previous Builds: {prod_ver}"
            ) from exc
        actions.tap(version_element)
        time.sleep(1.2)

        build_pattern = f"({build_no})"
        logger.info("Looking for build entry containing: %s", build_pattern)
        build_element = actions.find_element(
            AppiumBy.XPATH,
            f"//*[contains(@name, '{build_pattern}')]",
            timeout=12,
        )
        build_name = (build_element.get_attribute("name") or "").strip()
        _assert_target_build_text(build_name, prod_ver, build_no)
        build_y = build_element.location["y"]

        candidate_buttons = []
        for button_id in ("Install", "Update", "Open"):
            candidate_buttons.extend(actions.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, button_id))

        if not candidate_buttons:
            logger.info("No action buttons found on build page")
            return False

        closest_button = min(candidate_buttons, key=lambda btn: abs(btn.location["y"] - build_y))
        min_distance = abs(closest_button.location["y"] - build_y)
        logger.info("Closest action button distance from build row: %s", min_distance)
        if min_distance > 140:
            raise BuildMismatchError(
                "Found build row but nearest action button is too far: "
                f"distance={min_distance}, version={prod_ver}, build={build_no}"
            )

        button_text = _element_text(closest_button)
        if button_text.lower() == "open":
            logger.info("Target build already installed")
            return True

        actions.tap(closest_button)
        logger.info("Install clicked in Previous Builds, waiting for Open")
        _wait_for_open_button(actions.driver)
        logger.info("Installation from Previous Builds complete")
        return True

    except (
        TimeoutException,
        NoSuchElementException,
        StaleElementReferenceException,
        WebDriverException,
    ) as exc:
        logger.info("Previous Builds flow failed: %s", exc)
        return False


def update_testflight_app(session: TestFlightSession, prod_ver: str, build_no: str) -> bool:
    """Update/install target build in TestFlight with retry and keepalive."""
    session.launch_testflight()
    last_failure_reason = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        logger.info("--- Attempt %s/%s ---", attempt, MAX_ATTEMPTS)
        # Read the actions object per attempt: a restarted session replaces it.
        actions = session.actions
        try:
            _find_app_card(actions)
            logger.info("App '%s' found", TARGET_APP_NAME)

            if _check_main_page_build(actions, prod_ver, build_no):
                session.terminate_testflight()
                return True

            logger.info("Trying Previous Builds fallback")
            if check_previous_builds(actions, prod_ver, build_no):
                session.terminate_testflight()
                return True

        except BuildMismatchError as exc:
            last_failure_reason = str(exc)
            logger.warning("Attempt %s build mismatch: %s", attempt, exc)
        except (
            TimeoutException,
            NoSuchElementException,
            StaleElementReferenceException,
            WebDriverException,
        ) as exc:
            last_failure_reason = str(exc)
            logger.info("Attempt %s failed: %s", attempt, exc)

        if attempt < MAX_ATTEMPTS:
            logger.info("Retrying in %s seconds", RETRY_DELAY_SECONDS)
            session.terminate_testflight()
            # Keep session alive to avoid WDA idle timeout during long wait.
            for _ in range(RETRY_DELAY_SECONDS // 60):
                time.sleep(60)
                try:
                    session.driver.get_window_size()
                except Exception:
                    logger.debug("keepalive ping failed once; continuing")
            session.launch_testflight()

    logger.error("Max attempts reached: %s", last_failure_reason or "target build was not found")
    return False


def remove_target_app_if_installed(session: TestFlightSession) -> None:
    """Remove PhotoDirector app before TestFlight install/update."""
    logger.info("Removing %s if installed...", TARGET_APP_BUNDLE_ID)
    try:
        if session.driver.is_app_installed(TARGET_APP_BUNDLE_ID):
            session.driver.remove_app(TARGET_APP_BUNDLE_ID)
            logger.info("Removed installed app: %s", TARGET_APP_BUNDLE_ID)
        else:
            logger.info("App not installed, skip remove: %s", TARGET_APP_BUNDLE_ID)
    except Exception as exc:
        logger.warning("Error while removing app %s: %s", TARGET_APP_BUNDLE_ID, exc)

    # The uninstall restarts SpringBoard, which regularly makes WDA drop the
    # session; get a usable one back before touching TestFlight.
    session.ensure_alive()


def write_build_config_if_exists(prod_ver: str, build_no: str, sr_code: str, tr_code: str) -> None:
    """Update fixtures/config.ini when that file exists in current environment."""
    cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "config.ini")
    if not os.path.exists(cfg_path):
        logger.info("Skip config.ini update (not found): %s", cfg_path)
        return

    cfg = configparser.ConfigParser()
    cfg.read(cfg_path)
    if not cfg.has_section("Build"):
        cfg.add_section("Build")
    cfg.set("Build", "version", prod_ver)
    cfg.set("Build", "sr", sr_code)
    cfg.set("Build", "buildnumber", build_no)
    cfg.set("Build", "tr", tr_code)
    with open(cfg_path, "w", encoding="utf-8") as file:
        cfg.write(file)
    logger.info(
        "config.ini updated: version=%s sr=%s buildnumber=%s tr=%s",
        prod_ver,
        sr_code,
        build_no,
        tr_code,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Update/install TestFlight build")
    parser.add_argument(
        "--jenkins_build",
        required=True,
        help="Raw Jenkins build string, e.g. 'PhotoDirector Mobile (iOS): 20.9.0.2512152009'",
    )
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--sr_code", required=True, help="SR code")
    parser.add_argument("--tr_code", required=True, help="TR code")
    parser.add_argument("--short_description", required=True, help="Short description")
    parser.add_argument("--build-suffix", default="(64)", help="Suffix displayed in the app About page")
    args = parser.parse_args()

    try:
        prod_ver, build_no = parse_jenkins_build(args.jenkins_build)
    except Exception as exc:
        logger.error("FAILURE: Error parsing jenkins_build string: %s", exc)
        return 1

    logger.info("Starting update check for Version=%s Build=%s", prod_ver, build_no)
    session = TestFlightSession()
    try:
        session.start()
        remove_target_app_if_installed(session)
        success = update_testflight_app(session, prod_ver, build_no)
    finally:
        session.close()

    if success:
        logger.info("SUCCESS: App updated/found")
        write_build_config_if_exists(prod_ver, build_no, args.sr_code, args.tr_code)
        saved = save_build_info(
            {
                "project": args.project,
                "sr_code": args.sr_code,
                "tr_code": args.tr_code,
                "version": prod_ver,
                "build_number": build_no,
                "build_display": f"{build_no} {args.build_suffix}".strip(),
                "short_description": args.short_description,
                "jenkins_build": args.jenkins_build,
            }
        )
        logger.info("build_info.json updated: SR=%s TR=%s", saved["sr_code"], saved["tr_code"])
        return 0

    logger.error("FAILURE: Target build not found after %s attempts", MAX_ATTEMPTS)
    return 1


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    sys.exit(main())
