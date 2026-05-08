# ─────────────────────────────────────────────
# driver/driver_actions.py  –  Low-level UI interactions
# ─────────────────────────────────────────────
# Wraps Appium / W3C Actions into reusable, iOS-aware helpers.
# All page objects receive an instance of this class so that
# gesture logic lives in one place.

import functools
import logging
import math
import os
import time
from typing import Optional, Tuple

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
            return title   # used as bare @step
        return _Noop()
# ──────────────────────────────────────────────────────────────────
logger = logging.getLogger(__name__)

# Default timeouts (seconds)
DEFAULT_WAIT   = 30
DEFAULT_SCROLL_DURATION = 800  # ms


def wait_for_stable_hierarchy(fn):
    """
    Decorator: after the wrapped action completes, repeatedly poll
    page_source until it stops changing (hierarchy is stable).
    Only runs when the DriverActions instance has stability_check = True.

    Tunable via the instance attributes:
        stability_interval  (float, seconds) – gap between two snapshots
        stability_timeout   (float, seconds) – give up after this long
    """
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        result = fn(self, *args, **kwargs)
        if getattr(self, "stability_check", False):
            interval = getattr(self, "stability_interval", 0.4)
            timeout  = getattr(self, "stability_timeout",  10.0)
            deadline = time.monotonic() + timeout
            prev = self.driver.page_source
            while time.monotonic() < deadline:
                time.sleep(interval)
                curr = self.driver.page_source
                if curr == prev:
                    logger.debug("[stability] hierarchy stable after action '%s'", fn.__name__)
                    break
                prev = curr
            else:
                logger.warning(
                    "[stability] hierarchy did not stabilise within %.1fs after '%s'",
                    timeout, fn.__name__,
                )
        return result
    return wrapper


class DriverActions:
    """
    Thin wrapper around the Appium driver that provides reusable
    gesture and element-interaction methods for iOS.
    """

    def __init__(self, driver):
        self.driver = driver

        # ── Hierarchy stability check ──────────────────────────────────────
        # Set to True to automatically wait for the UI hierarchy to stop
        # changing after every decorated action.
        # WARNING: page_source is slow (~0.5–2 s per call). Only enable when
        # flakiness caused by async UI updates outweighs the extra time cost.
        self.stability_check: bool = False

        # How long to wait between two page_source snapshots (seconds).
        self.stability_interval: float = 0.4

        # Maximum time to keep polling before giving up and continuing (seconds).
        self.stability_timeout: float = 10.0
        # ──────────────────────────────────────────────────────────────────

    # ──────────────────────────────────────────
    # Element look-up
    # ──────────────────────────────────────────

    def find_element(
        self,
        by: str,
        value: str,
        timeout: int = DEFAULT_WAIT,
    ) -> WebElement:
        """Wait until an element is *present* in the DOM and return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value)),
            message=f"Element not found: ({by}, {value!r})",
        )

    def find_elements(
        self,
        by: str,
        value: str,
        timeout: int = DEFAULT_WAIT,
    ) -> list[WebElement]:
        """Return all matching elements (empty list if none found within timeout)."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            return []
        return self.driver.find_elements(by, value)

    def wait_for_visible(
        self,
        by: str,
        value: str,
        timeout: int = DEFAULT_WAIT,
    ) -> WebElement:
        """Wait until an element is present (XCUITest compatible)."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value)),
            message=f"Element not found: ({by}, {value!r})",
        )

    def wait_for_invisible(
        self,
        by: str,
        value: str,
        timeout: int = DEFAULT_WAIT,
    ) -> bool:
        """Wait until an element disappears from the screen."""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((by, value))
        )

    def is_element_present(self, by: str, value: str, timeout: int = 3) -> bool:
        """Non-throwing check: returns True if element appears within *timeout*."""
        try:
            self.find_element(by, value, timeout=timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    # ──────────────────────────────────────────
    # Tap / click
    # ──────────────────────────────────────────

    @step("Tap element")
    @wait_for_stable_hierarchy
    def tap(self, element: WebElement) -> None:
        """Tap a WebElement."""
        element.click()

    @step("Tap by locator")
    def tap_by_locator(self, by: str, value: str, timeout: int = DEFAULT_WAIT) -> None:
        """Find an element then tap it."""
        self.tap(self.wait_for_visible(by, value, timeout))

    @step("Tap at coordinates")
    @wait_for_stable_hierarchy
    def tap_by_coordinates(self, x: int, y: int) -> None:
        """
        Tap at absolute screen coordinates using the iOS mobile:tap command.
        Coordinates are in points (not pixels).
        """
        self.driver.execute_script("mobile: tap", {"x": x, "y": y})
        logger.debug("Tapped at (%d, %d)", x, y)

    def _coord_at_pct(self, element: WebElement, pct_x: float, pct_y: float) -> Tuple[int, int]:
        """Compute absolute screen coordinates at (pct_x%, pct_y%) within element bounds."""
        loc  = element.location
        size = element.size
        return (
            int(loc["x"] + size["width"]  * pct_x / 100),
            int(loc["y"] + size["height"] * pct_y / 100),
        )

    @step("Tap within element")
    @wait_for_stable_hierarchy
    def tap_within_element(self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT) -> None:
        """Find element and tap at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: tap", {"x": tx, "y": ty})

    @step("Double tap within element")
    @wait_for_stable_hierarchy
    def double_tap_within_element(self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT) -> None:
        """Find element and double-tap at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: doubleTap", {"x": tx, "y": ty})

    @step("Triple tap within element")
    @wait_for_stable_hierarchy
    def triple_tap_within_element(self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT) -> None:
        """Find element and triple-tap at (pct_x%, pct_y%) within its bounds."""
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions import interaction
        from selenium.webdriver.common.actions.pointer_input import PointerInput
        el = self.wait_for_visible(by, value, timeout)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        ac = ActionChains(self.driver)
        ac.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        pa = ac.w3c_actions.pointer_action
        for i in range(3):
            pa.move_to_location(tx, ty)
            pa.pointer_down()
            pa.pause(0.05)
            pa.pointer_up()
            if i < 2:
                pa.pause(0.08)
        ac.perform()

    @step("Long press within element")
    @wait_for_stable_hierarchy
    def long_press_within_element(self, by: str, value: str, pct_x: float, pct_y: float, duration: float = 1.0, timeout: int = DEFAULT_WAIT) -> None:
        """Find element and long-press at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: touchAndHold", {"x": tx, "y": ty, "duration": duration})

    @step("Double tap")
    @wait_for_stable_hierarchy
    def double_tap(self, element: WebElement) -> None:
        """Double-tap a WebElement."""
        self.driver.execute_script("mobile: doubleTap", {"element": element.id})

    @step("Long press")
    @wait_for_stable_hierarchy
    def long_press(self, element: WebElement, duration: float = 1.0) -> None:
        """Long-press a WebElement for *duration* seconds (default 500 ms+)."""
        self.driver.execute_script(
            "mobile: touchAndHold",
            {"element": element.id, "duration": duration},
        )

    @step("Triple tap")
    @wait_for_stable_hierarchy
    def triple_tap(self, element: WebElement) -> None:
        """Triple-tap a WebElement using native XCUITest gesture."""
        self.driver.execute_script(
            "mobile: tapWithNumberOfTaps",
            {"element": element.id, "numberOfTaps": 3, "numberOfTouches": 1},
        )

    @step("Two finger tap")
    @wait_for_stable_hierarchy
    def two_finger_tap(self, element: WebElement) -> None:
        """
        Two-finger tap on *element* using XCUITest mobile: twoFingerTap.
        This is the native iOS "two-finger tap" recognised by many apps.
        """
        self.driver.execute_script(
            "mobile: twoFingerTap",
            {"element": element.id},
        )
        logger.debug("two_finger_tap on element")

    @step("Multi finger tap")
    @wait_for_stable_hierarchy
    def multi_finger_tap(
        self,
        element: WebElement,
        fingers: int = 3,
        pause_ms: int = 50,
    ) -> None:
        """
        Tap *element* with *fingers* touch points.
        Uses twoFingerTap for 2 fingers; repeated mobile:tap for 3+.
        """
        loc  = element.location
        size = element.size
        cx   = loc["x"] + size["width"] // 2
        cy   = loc["y"] + size["height"] // 2

        if fingers == 2:
            self.driver.execute_script("mobile: twoFingerTap", {"element": element.id})
        else:
            for _ in range(fingers):
                self.driver.execute_script("mobile: tap", {"x": cx, "y": cy})
                time.sleep(pause_ms / 1000)

    # ──────────────────────────────────────────
    # Swipe / Scroll
    # ──────────────────────────────────────────

    @step("Swipe")
    def swipe(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        duration: int = DEFAULT_SCROLL_DURATION,
    ) -> None:
        """
        Swipe from (start_x, start_y) to (end_x, end_y).
        *duration* is in milliseconds.
        """
        self.driver.execute_script(
            "mobile: dragFromToWithVelocity",
            {
                "startX": start_x,
                "startY": start_y,
                "endX": end_x,
                "endY": end_y,
                "velocity": max(1, 1000 - duration),  # rough velocity inversion
            },
        )
        logger.debug("Swipe (%d,%d) → (%d,%d)", start_x, start_y, end_x, end_y)

    @step("Scroll")
    def scroll(self, direction: str = "down", distance: float = 0.5) -> None:
        """
        Scroll the whole screen in *direction* ('up', 'down', 'left', 'right').
        *distance* is a fraction of the screen (0.0–1.0).
        """
        window = self.driver.get_window_size()
        width, height = window["width"], window["height"]
        center_x = width // 2
        center_y = height // 2
        offset = int(height * distance)

        directions = {
            "down":  (center_x, center_y - offset // 2, center_x, center_y + offset // 2),
            "up":    (center_x, center_y + offset // 2, center_x, center_y - offset // 2),
            "right": (center_x - offset // 2, center_y, center_x + offset // 2, center_y),
            "left":  (center_x + offset // 2, center_y, center_x - offset // 2, center_y),
        }
        if direction not in directions:
            raise ValueError(f"Unknown scroll direction: {direction!r}")

        sx, sy, ex, ey = directions[direction]
        self.driver.execute_script(
            "mobile: scroll",
            {"direction": direction},
        )
        logger.debug("Scrolled %s", direction)

    @step("Scroll to element")
    def scroll_to_element(
        self,
        by: str,
        value: str,
        direction: str = "down",
        max_scrolls: int = 8,
    ) -> WebElement:
        """
        Scroll in *direction* until the element is visible, then return it.
        Raises NoSuchElementException if not found after *max_scrolls* attempts.
        """
        for attempt in range(max_scrolls):
            if self.is_element_present(by, value, timeout=2):
                return self.find_element(by, value)
            logger.debug("Scroll attempt %d/%d looking for (%s, %r)", attempt + 1, max_scrolls, by, value)
            self.scroll(direction)
        raise NoSuchElementException(
            f"Element ({by}, {value!r}) not found after {max_scrolls} scrolls."
        )

    # ──────────────────────────────────────────
    # Text input
    # ──────────────────────────────────────────

    @step("Type text")
    @wait_for_stable_hierarchy
    def type_text(self, element: WebElement, text: str, clear_first: bool = True) -> None:
        """Type text into an input element, optionally clearing it first."""
        if clear_first:
            element.clear()
        element.send_keys(text)

    @step("Type text by locator")
    def type_text_by_locator(
        self,
        by: str,
        value: str,
        text: str,
        clear_first: bool = True,
        timeout: int = DEFAULT_WAIT,
    ) -> None:
        element = self.wait_for_visible(by, value, timeout)
        self.type_text(element, text, clear_first)

    # ──────────────────────────────────────────
    # App / keyboard utilities
    # ──────────────────────────────────────────

    @step("Hide keyboard")
    def hide_keyboard(self) -> None:
        """Dismiss the on-screen keyboard if visible."""
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass  # keyboard may already be hidden

    @step("Background app")
    def background_app(self, seconds: int = 3) -> None:
        """Send the app to the background for *seconds* then restore it."""
        self.driver.background_app(seconds)

    def get_screen_size(self) -> Tuple[int, int]:
        """Return (width, height) in points."""
        size = self.driver.get_window_size()
        return size["width"], size["height"]

    @step("Take screenshot")
    def take_screenshot(self, path: str) -> None:
        """Save a screenshot to *path* (PNG)."""
        self.driver.save_screenshot(path)
        logger.info("Screenshot saved: %s", path)

    # ──────────────────────────────────────────
    # Swipe screen (high-velocity fling)
    # ──────────────────────────────────────────

    @step("Swipe screen")
    def swipe_screen(
        self,
        direction: str = "up",
        distance: float = 0.7,
        velocity: float = 2500.0,
    ) -> None:
        """
        Fast full-screen swipe (higher velocity than scroll).
        direction : 'up' | 'down' | 'left' | 'right'
        distance  : fraction of the screen dimension to travel (0.0–1.0).
        velocity  : points/sec – higher = faster fling.
        """
        w, h = self.get_screen_size()
        cx, cy = w // 2, h // 2
        half_h = int(h * distance / 2)
        half_w = int(w * distance / 2)
        direction_map = {
            "up":    (cx, cy + half_h, cx, cy - half_h),
            "down":  (cx, cy - half_h, cx, cy + half_h),
            "left":  (cx + half_w, cy, cx - half_w, cy),
            "right": (cx - half_w, cy, cx + half_w, cy),
        }
        if direction not in direction_map:
            raise ValueError(f"Unknown swipe direction: {direction!r}")
        sx, sy, ex, ey = direction_map[direction]
        self.driver.execute_script(
            "mobile: dragFromToWithVelocity",
            {"startX": sx, "startY": sy, "endX": ex, "endY": ey, "velocity": velocity},
        )
        logger.debug("swipe_screen %s (dist=%.1f, vel=%.0f)", direction, distance, velocity)

    # ──────────────────────────────────────────
    # scroll_until / swipe_until
    # ──────────────────────────────────────────

    @step("Scroll until element found and tap")
    def scroll_until(
        self,
        scroll_by: str,
        scroll_value: str,
        target_by: str,
        target_value: str,
        direction: str = "down",
        max_attempts: int = 8,
        offset_start: Optional[Tuple[float, float]] = None,
        offset_end: Optional[Tuple[float, float]] = None,
        velocity: int = 100,
    ) -> WebElement:
        """
        Scroll within the element (scroll_by, scroll_value) in *direction*
        until (target_by, target_value) is visible, and return it.

        offset_start / offset_end: (x_pct, y_pct) fractions of the container
        rect that define the drag gesture.  Generated by the recorder from the
        original gesture; defaults to a 40 % horizontal/vertical swipe.
        """
        for attempt in range(max_attempts):
            if self.is_element_present(target_by, target_value, timeout=2):
                element = self.find_element(target_by, target_value)
                logger.debug(
                    "scroll_until: found (%s, %r) after %d scrolls",
                    target_by, target_value, attempt,
                )
                return element
            logger.debug(
                "Scroll attempt %d/%d looking for (%s, %r)",
                attempt + 1, max_attempts, target_by, target_value,
            )
            scroll_container = self.find_element(scroll_by, scroll_value)
            rect = scroll_container.rect
            rx, ry, rw, rh = rect["x"], rect["y"], rect["width"], rect["height"]

            if offset_start and offset_end:
                sx = rx + rw * offset_start[0]
                sy = ry + rh * offset_start[1]
                ex = rx + rw * offset_end[0]
                ey = ry + rh * offset_end[1]
            else:
                cx, cy = rx + rw / 2, ry + rh / 2
                h_off, v_off = rw * 0.4, rh * 0.4
                drag = {
                    "left":  (cx + h_off, cy, cx - h_off, cy),
                    "right": (cx - h_off, cy, cx + h_off, cy),
                    "up":    (cx, cy + v_off, cx, cy - v_off),
                    "down":  (cx, cy - v_off, cx, cy + v_off),
                }
                if direction not in drag:
                    raise ValueError(f"Unknown scroll direction: {direction!r}")
                sx, sy, ex, ey = drag[direction]

            self.driver.execute_script(
                "mobile: dragFromToWithVelocity",
                {
                    "fromX": sx, "fromY": sy,
                    "toX": ex,   "toY": ey,
                    "velocity": velocity,
                    "pressDuration": 0.1,
                    "holdDuration": 0.1,
                },
            )
        raise NoSuchElementException(
            f"Element ({target_by}, {target_value!r}) not found after {max_attempts} scrolls."
        )

    @step("Swipe")
    def swipe_until(
        self,
        by: str,
        value: str,
        direction: str = "up",
        max_attempts: int = 8,
        distance: float = 0.7,
    ) -> WebElement:
        """
        Fast-swipe in *direction* 
        """
        for attempt in range(max_attempts):
            if self.is_element_present(by, value, timeout=2):
                element = self.find_element(by, value)
                logger.debug(
                    "swipe_until: found (%s, %r) after %d swipes", by, value, attempt
                )
                return element
            self.swipe_screen(direction, distance=distance)
        raise NoSuchElementException(
            f"Element ({by}, {value!r}) not found after {max_attempts} swipes."
        )

    # ──────────────────────────────────────────
    # Drag
    # ──────────────────────────────────────────

    @step("Drag element to target")
    def drag_element(
        self,
        source: WebElement,
        target: WebElement,
        duration: float = 1.0,
    ) -> None:
        """
        Press-hold *source* then drag it onto *target*.
        duration: hold-press time in seconds before releasing.
        """
        src, src_sz = source.location, source.size
        tgt, tgt_sz = target.location, target.size
        self.driver.execute_script(
            "mobile: dragFromToForDuration",
            {
                "fromX": src["x"] + src_sz["width"] // 2,
                "fromY": src["y"] + src_sz["height"] // 2,
                "toX":   tgt["x"] + tgt_sz["width"] // 2,
                "toY":   tgt["y"] + tgt_sz["height"] // 2,
                "duration": duration,
            },
        )
        logger.debug("drag_element: source → target")

    @step("Drag by coordinates")
    @wait_for_stable_hierarchy
    def drag_coordinates(
        self,
        from_x: int,
        from_y: int,
        to_x: int,
        to_y: int,
        duration: float = 1.0,
    ) -> None:
        """Press-hold at (from_x, from_y) then drag to (to_x, to_y)."""
        self.driver.execute_script(
            "mobile: dragFromToForDuration",
            {
                "fromX": from_x, "fromY": from_y,
                "toX":   to_x,   "toY":   to_y,
                "duration": duration,
            },
        )
        logger.debug("drag_coordinates: (%d,%d) → (%d,%d)", from_x, from_y, to_x, to_y)

    # ──────────────────────────────────────────
    # Pinch & Rotate
    # ──────────────────────────────────────────

    @step("Pinch")
    def pinch(
        self,
        element: WebElement,
        scale: float = 0.5,
        velocity: float = -1.0,
    ) -> None:
        """
        Pinch gesture on *element* via XCUITest mobile: pinch.
        scale   < 1.0  →  pinch in  (zoom out).
        scale   > 1.0  →  pinch out (zoom in).
        velocity: pinch speed in scale-factor/sec; -1.0 = XCUITest default.
        """
        params: dict = {"element": element.id, "scale": scale}
        if velocity > 0:
            params["velocity"] = velocity
        self.driver.execute_script("mobile: pinch", params)
        logger.debug("pinch: scale=%.2f vel=%.1f", scale, velocity)

    @step("Rotate")
    def rotate(
        self,
        element: WebElement,
        rotation: float = math.pi,
        velocity: float = 1.5,
    ) -> None:
        """
        Rotate gesture on *element* via XCUITest mobile: rotateElement.
        rotation : angle in radians (positive = clockwise).
        velocity : speed in radians/sec.
        """
        self.driver.execute_script(
            "mobile: rotateElement",
            {
                "element": element.id,
                "rotation": rotation,
                "velocity": velocity,
            },
        )
        logger.debug("rotate: %.2f rad at %.1f rad/s", rotation, velocity)

    # ──────────────────────────────────────────
    # System operations
    # ──────────────────────────────────────────

    @step("Press Home button")
    def press_home(self) -> None:
        """Press the physical Home button (sends the app to the background)."""
        self.driver.execute_script("mobile: pressButton", {"name": "home"})
        logger.debug("press_home")

    @step("Launch app")
    def launch_app(self, bundle_id: str) -> None:
        """
        Launch *bundle_id*.
        - Already running → brought to foreground.
        - Terminated       → cold-started.
        """
        self.driver.execute_script("mobile: launchApp", {"bundleId": bundle_id})
        logger.info("launch_app: %s", bundle_id)

    # ──────────────────────────────────────────
    # Verify (assertions)
    # ──────────────────────────────────────────

    @step("Verify element visible")
    def verify_visible(
        self,
        by: str,
        value: str,
        timeout: int = DEFAULT_WAIT,
        msg: str = "",
    ) -> WebElement:
        """
        Assert that the element is visible on screen.
        Returns the element so callers can chain further actions.
        Raises AssertionError if not visible within *timeout* seconds.
        """
        try:
            element = self.wait_for_visible(by, value, timeout)
        except TimeoutException:
            label = msg or f"({by}, {value!r})"
            raise AssertionError(f"verify_visible FAILED – element not visible: {label}")
        return element

    @step("Verify element not visible")
    def verify_not_visible(
        self,
        by: str,
        value: str,
        timeout: int = 3,
        msg: str = "",
    ) -> None:
        """Assert that the element is NOT visible (or absent) on screen."""
        if self.is_element_present(by, value, timeout=timeout):
            label = msg or f"({by}, {value!r})"
            raise AssertionError(f"verify_not_visible FAILED – element is visible: {label}")

    @step("Verify element text")
    def verify_text(
        self,
        by: str,
        value: str,
        expected: str,
        timeout: int = DEFAULT_WAIT,
    ) -> None:
        """
        Assert that the element's text / label equals *expected*.
        Raises AssertionError with a clear diff message on mismatch.
        """
        element = self.wait_for_visible(by, value, timeout)
        actual = element.text
        assert actual == expected, (
            f"verify_text FAILED for ({by}, {value!r})\n"
            f"  expected : {expected!r}\n"
            f"  actual   : {actual!r}"
        )

    # ──────────────────────────────────────────
    # Screenshot: ground truth & visual diff
    # ──────────────────────────────────────────

    @step("Capture ground truth screenshot")
    def screenshot_gt(
        self,
        name: str,
        folder: str = "screenshots/ground_truth",
    ) -> str:
        """
        Capture the current screen and save it as the ground truth for *name*.
        File path: <folder>/<name>.png
        Re-running overwrites the previous ground truth.
        """
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{name}.png")
        self.driver.save_screenshot(path)
        logger.info("Ground truth saved: %s", path)
        return path

    @step("Compare screenshot with ground truth")
    def screenshot_diff(
        self,
        name: str,
        gt_folder: str = "screenshots/ground_truth",
        diff_folder: str = "screenshots/diffs",
        threshold: float = 0.01,
    ) -> float:
        """
        Compare the current screen against the ground truth <name>.png.

        Returns the diff ratio (0.0 = identical, 1.0 = every pixel differs).
        Saves a diff PNG to *diff_folder* whenever any difference is found.
        Raises AssertionError if diff_ratio > *threshold*.

        Requires: pip install Pillow numpy
        """
        try:
            from PIL import Image, ImageChops
            import numpy as np
        except ImportError as exc:
            raise ImportError(
                "screenshot_diff requires Pillow and numpy. "
                "Run: pip install Pillow numpy"
            ) from exc

        gt_path = os.path.join(gt_folder, f"{name}.png")
        if not os.path.exists(gt_path):
            raise FileNotFoundError(
                f"Ground truth not found: {gt_path}. "
                f"Call screenshot_gt({name!r}) first."
            )

        os.makedirs(diff_folder, exist_ok=True)
        current_path = os.path.join(diff_folder, f"{name}_current.png")
        self.driver.save_screenshot(current_path)

        gt_img      = Image.open(gt_path).convert("RGB")
        current_img = Image.open(current_path).convert("RGB")

        if gt_img.size != current_img.size:
            current_img = current_img.resize(gt_img.size, Image.LANCZOS)

        diff_img   = ImageChops.difference(gt_img, current_img)
        diff_arr   = np.array(diff_img, dtype=np.float32)
        diff_ratio = float(np.count_nonzero(diff_arr)) / diff_arr.size

        if diff_ratio > 0:
            diff_path = os.path.join(diff_folder, f"{name}_diff.png")
            diff_img.save(diff_path)
            logger.info("Diff image saved: %s (ratio=%.4f)", diff_path, diff_ratio)

        assert diff_ratio <= threshold, (
            f"screenshot_diff FAILED for {name!r}: "
            f"diff_ratio={diff_ratio:.4f} > threshold={threshold:.4f}"
        )
        logger.info("screenshot_diff PASSED for %r (diff_ratio=%.4f)", name, diff_ratio)
        return diff_ratio
