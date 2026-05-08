# ─────────────────────────────────────────────
# pages/base_page.py  –  Shared page-level helpers
# ─────────────────────────────────────────────
# Every specific page object (LoginPage, HomePage, …) extends BasePage.
# BasePage holds helpers that are useful across ALL pages so they don't
# need to be duplicated inside every test or page class.

import logging
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from driver.driver_actions import DriverActions

# ── ReportPortal step decorator (no-op fallback when RP is not installed) ─────
try:
    from reportportal_client import step
except ImportError:
    def step(title=None, **_):  # type: ignore[misc]
        """No-op: works as @step, @step("title"), or with step("title")."""
        class _Noop:
            def __call__(self, fn): return fn
            def __enter__(self): return self
            def __exit__(self, *a): pass
        if callable(title):
            return title
        return _Noop()
# ──────────────────────────────────────────────────────────────────

logger = logging.getLogger(__name__)

# Shared locator constants used app-wide
LOADING_SPINNER = (AppiumBy.ACCESSIBILITY_ID, "ActivityIndicator")
ALERT_OK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "OK")
BACK_BUTTON     = (AppiumBy.ACCESSIBILITY_ID, "Back")


class BasePage:
    """
    Base class inherited by every page object.

    Provides:
    - Shorthand wrappers around DriverActions so subclasses don't always
      need to call self.actions.<method>
    - Cross-page utilities (wait for load, handle alerts, screenshot on
      failure, navigation helpers)
    """

    def __init__(self, driver, actions: DriverActions):
        self.driver  = driver
        self.actions = actions

    # ──────────────────────────────────────────
    # Loading / readiness
    # ──────────────────────────────────────────

    @step("Wait for page load")
    def wait_for_page_load(self, timeout: int = 15) -> None:
        """
        Wait until the loading spinner (if any) disappears.
        Override in subclasses that have a more specific readiness signal.
        """
        try:
            self.actions.wait_for_invisible(*LOADING_SPINNER, timeout=timeout)
        except TimeoutException:
            logger.warning("Loading spinner still visible after %ds", timeout)

    def is_current_page(self) -> bool:
        """
        Override in each subclass to assert a unique element that identifies
        the page. Default implementation always returns True.
        """
        return True

    # ──────────────────────────────────────────
    # Navigation
    # ──────────────────────────────────────────

    @step("Go back")
    def go_back(self) -> None:
        """Tap the native iOS back button."""
        self.actions.tap_by_locator(*BACK_BUTTON)

    @step("Navigate to URL")
    def navigate_to(self, url: str) -> None:
        """
        Deep-link or URL scheme navigation (if the app supports it).
        Example: navigate_to("myapp://home")
        """
        self.driver.get(url)

    # ──────────────────────────────────────────
    # Alert handling
    # ──────────────────────────────────────────

    @step("Accept alert")
    def accept_alert(self, timeout: int = 5) -> bool:
        """
        Accept a native iOS alert if one appears within *timeout* seconds.
        Returns True if an alert was accepted, False otherwise.
        """
        try:
            WebDriverWait_import()  # deferred import to keep top-level clean
            alert = self.driver.switch_to.alert
            alert.accept()
            logger.info("Alert accepted.")
            return True
        except Exception:
            return False

    @step("Dismiss permission popup")
    def dismiss_permission_popup(self, allow: bool = True) -> bool:
        """
        Handle iOS permission prompts ('Allow' / 'Don't Allow').
        Returns True if a popup was found and handled.
        """
        button_label = "Allow" if allow else "Don't Allow"
        if self.actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, button_label, timeout=4):
            self.actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, button_label)
            logger.info("Permission popup dismissed (allow=%s).", allow)
            return True
        return False

    # ──────────────────────────────────────────
    # Assertions / state queries
    # ──────────────────────────────────────────

    def is_visible(self, by: str, value: str, timeout: int = 5) -> bool:
        """Return True if the element is visible within *timeout* seconds."""
        return self.actions.is_element_present(by, value, timeout=timeout)

    def get_text(self, by: str, value: str, timeout: int = 10) -> str:
        """Return the text / label of an element."""
        element = self.actions.wait_for_visible(by, value, timeout)
        return element.text

    def get_attribute(self, by: str, value: str, attribute: str, timeout: int = 10) -> str:
        """Return an attribute value of an element."""
        element = self.actions.find_element(by, value, timeout)
        return element.get_attribute(attribute)

    # ──────────────────────────────────────────
    # Screenshot helper
    # ──────────────────────────────────────────

    @step("Take page screenshot")
    def screenshot(self, name: str, folder: str = "screenshots") -> str:
        """
        Save a screenshot into *folder*/<name>.png and return the path.
        The folder is created automatically if it does not exist.
        """
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{name}.png")
        self.actions.take_screenshot(path)
        return path

    # ──────────────────────────────────────────
    # Convenience wrappers (so subclasses stay clean)
    # ──────────────────────────────────────────

    @step("Tap element")
    def tap(self, by: str, value: str, timeout: int = 10) -> None:
        self.actions.tap_by_locator(by, value, timeout)

    @step("Type text")
    def type_text(self, by: str, value: str, text: str, timeout: int = 10) -> None:
        self.actions.type_text_by_locator(by, value, text, timeout=timeout)

    @step("Scroll down")
    def scroll_down(self) -> None:
        self.actions.scroll("down")

    @step("Scroll up")
    def scroll_up(self) -> None:
        self.actions.scroll("up")

    @step("Scroll to element")
    def scroll_to(self, by: str, value: str) -> None:
        self.actions.scroll_to_element(by, value)


def WebDriverWait_import():
    """Lazy import guard (avoids circular-import issues in some configurations)."""
    from selenium.webdriver.support.ui import WebDriverWait  # noqa: F401
