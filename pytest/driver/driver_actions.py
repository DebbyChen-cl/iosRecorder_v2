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
import threading
import time
import json
import base64
import urllib.request
import urllib.parse
from datetime import datetime
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
                    logger.info("[stability] hierarchy stable after action '%s'", fn.__name__)
                    break
                prev = curr
            else:
                logger.warning(
                    "[stability] hierarchy did not stabilise within %.1fs after '%s'",
                    timeout, fn.__name__,
                )
        return result
    return wrapper


def _apply_stability_to_all(cls):
    """
    Class decorator: automatically wraps every public (non-dunder) method with
    wait_for_stable_hierarchy so that the ``stability_check`` instance flag
    applies uniformly to the entire class.
    Individual ``@wait_for_stable_hierarchy`` decorators are no longer needed.
    """
    for attr_name in list(vars(cls)):
        if attr_name.startswith('_'):
            continue
        method = vars(cls)[attr_name]
        if callable(method):
            setattr(cls, attr_name, wait_for_stable_hierarchy(method))
    return cls


@_apply_stability_to_all
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

        # ── Screenshot comparison queues ───────────────────────────────────
        # Populated by capture_for_gt / capture_for_preview during the test.
        # GT queue entries     : (name, compare_path, threshold_or_None)
        # Preview queue entries: (name, before_path, after_path, threshold_or_None, expected_result)
        #   expected_result = "same"      → similarity >= threshold to PASS
        #   expected_result = "different" → similarity <  threshold to PASS
        # None threshold means use the global value from run_screenshot_comparisons().
        self._gt_compare_queue: list[tuple[str, str, Optional[float]]] = []
        self._preview_compare_queue: list[tuple[str, str, str, Optional[float], str]] = []
        # Pending before-captures: name → (ts, before_path), waiting for the matching "after".
        self._preview_pending: dict[str, tuple[str, str]] = {}
        # Optional metadata captured at "before" to keep before/after crop geometry identical.
        self._preview_pending_meta: dict[str, tuple[Optional[dict], Optional[dict]]] = {}
        # ──────────────────────────────────────────────────────────────────

    # ──────────────────────────────────────────
    # Element look-up
    # ──────────────────────────────────────────

    def find_element(
        self,
        by: str,
        value: str,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
    ) -> WebElement:
        """Wait until an element is present; auto-scroll within container when not immediately visible.

        When container_by / container_value are provided and the element is absent or
        less than 50 % on-screen after a quick wait, _find_with_scroll() is called to
        probe the container axis, rewind to start, and scroll forward until the element
        is fully in view.  All other methods that take (by, value) forward these params
        here, so scroll fallback applies uniformly to every action.
        """
        if container_by and container_value:
            try:
                el = WebDriverWait(self.driver, min(5, timeout)).until(
                    EC.presence_of_element_located((by, value))
                )
                if self._visible_fraction(el) >= 0.5:
                    return el
            except TimeoutException:
                pass
            return self._find_with_scroll(
                by, value, container_by, container_value, container_w, container_h
            )
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
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
    ) -> WebElement:
        """Wait until an element is present (XCUITest compatible). Forwards to find_element."""
        return self.find_element(
            by, value, timeout, container_by, container_value, container_w, container_h
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
    def tap(self, element: WebElement) -> None:
        """Tap a WebElement."""
        element.click()

    @step("Tap by locator")
    def tap_by_locator(
        self, by: str, value: str, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> None:
        """Find an element then tap it."""
        self.tap(self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h))

    @step("Tap at coordinates")
    def tap_by_coordinates(self, x: int, y: int) -> None:
        """
        Tap at absolute screen coordinates using the iOS mobile:tap command.
        Coordinates are in points (not pixels).
        """
        self.driver.execute_script("mobile: tap", {"x": x, "y": y})
        logger.info("Tapped at (%d, %d)", x, y)

    def _visible_fraction(self, element: WebElement) -> float:
        """Return the fraction (0.0–1.0) of element that lies within the device screen."""
        r = element.rect
        el_x, el_y, el_w, el_h = r["x"], r["y"], r["width"], r["height"]
        el_area = el_w * el_h
        if el_area <= 0:
            return 0.0
        win = self.driver.get_window_size()
        ix1 = max(el_x, 0)
        iy1 = max(el_y, 0)
        ix2 = min(el_x + el_w, win["width"])
        iy2 = min(el_y + el_h, win["height"])
        if ix2 <= ix1 or iy2 <= iy1:
            return 0.0
        return (ix2 - ix1) * (iy2 - iy1) / el_area

    def _coord_at_pct(self, element: WebElement, pct_x: float, pct_y: float) -> Tuple[int, int]:
        """Compute absolute screen coordinates at (pct_x%, pct_y%) within element bounds."""
        loc  = element.location
        size = element.size
        return (
            int(loc["x"] + size["width"]  * pct_x / 100),
            int(loc["y"] + size["height"] * pct_y / 100),
        )

    @step("Tap within element")
    def tap_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> None:
        """Find element and tap at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: tap", {"x": tx, "y": ty})

    # ── private scroll helpers (not wrapped by stability decorator) ─────────

    def _scroll_container_once(
        self,
        container_by: str,
        container_value: str,
        direction: str,
        velocity: int = 300,
    ) -> None:
        """One drag gesture inside the container.

        Direction convention (same as scroll_until / dragFromToWithVelocity):
          "up"    = finger moves UP    → reveals content at bottom / end of list
          "down"  = finger moves DOWN  → reveals content at top    / start of list
          "left"  = finger moves LEFT  → reveals content at right  / end of horiz. list
          "right" = finger moves RIGHT → reveals content at left   / start of horiz. list
        """
        container = self.find_element(container_by, container_value)
        rect = container.rect
        rx, ry, rw, rh = rect["x"], rect["y"], rect["width"], rect["height"]
        cx, cy = rx + rw / 2, ry + rh / 2
        h_off = rw * 0.35
        v_off = rh * 0.35
        coords = {
            "up":    (cx, cy + v_off, cx, cy - v_off),
            "down":  (cx, cy - v_off, cx, cy + v_off),
            "left":  (cx + h_off, cy, cx - h_off, cy),
            "right": (cx - h_off, cy, cx + h_off, cy),
        }
        if direction not in coords:
            raise ValueError(f"Unknown scroll direction: {direction!r}")
        sx, sy, ex, ey = coords[direction]
        self.driver.execute_script(
            "mobile: dragFromToWithVelocity",
            {
                "fromX": sx, "fromY": sy,
                "toX":   ex, "toY":   ey,
                "velocity": velocity,
                "pressDuration": 0.05,
                "holdDuration":  0.05,
            },
        )
        logger.debug("_scroll_container_once: direction=%s", direction)

    def _find_with_scroll(
        self,
        by: str,
        value: str,
        container_by: str,
        container_value: str,
        container_w: int = 0,
        container_h: int = 0,
        max_scrolls: int = 20,
    ) -> WebElement:
        """Probe container scroll axis, rewind to start, then scroll forward until
        the element is ≥ 50 % visible.  Raises NoSuchElementException if not found.

        Direction convention:
          container_w > container_h  → try horizontal first, then vertical
          container_w <= container_h → try vertical first, then horizontal
          rewind = "down" / "right"  (scroll toward list start)
          forward = "up" / "left"    (scroll toward list end)
        """
        _AXIS_DIRS = {
            "vertical":   ("down", "up"),
            "horizontal": ("right", "left"),
        }
        if (container_w or 0) > (container_h or 0):
            probe_order = [
                ("left",  "horizontal"),
                ("right", "horizontal"),
                ("up",    "vertical"),
                ("down",  "vertical"),
            ]
        else:
            probe_order = [
                ("up",    "vertical"),
                ("down",  "vertical"),
                ("left",  "horizontal"),
                ("right", "horizontal"),
            ]

        rewind_dir: Optional[str] = None
        forward_dir: Optional[str] = None
        for probe, axis in probe_order:
            before = self.driver.page_source
            self._scroll_container_once(container_by, container_value, probe)
            after = self.driver.page_source
            if after != before:
                rewind_dir, forward_dir = _AXIS_DIRS[axis]
                logger.info("_find_with_scroll: scrollable on %s axis (probe=%s)", axis, probe)
                break

        if forward_dir is None:
            raise NoSuchElementException(
                f"Element ({by}, {value!r}) not found and container "
                f"({container_by}, {container_value!r}) does not scroll."
            )

        # Rewind to start
        prev = self.driver.page_source
        for _ in range(max_scrolls):
            self._scroll_container_once(container_by, container_value, rewind_dir)
            curr = self.driver.page_source
            if curr == prev:
                break
            prev = curr
        logger.info("_find_with_scroll: rewound to start (direction=%s)", rewind_dir)

        # Scroll forward until element ≥ 50 % visible
        for attempt in range(max_scrolls):
            if self.is_element_present(by, value, timeout=2):
                el = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((by, value))
                )
                if self._visible_fraction(el) >= 0.5:
                    logger.info(
                        "_find_with_scroll: found (%s, %r) after %d scrolls",
                        by, value, attempt,
                    )
                    return el
            self._scroll_container_once(container_by, container_value, forward_dir)

        raise NoSuchElementException(
            f"Element ({by}, {value!r}) not found after {max_scrolls} scrolls "
            f"in container ({container_by}, {container_value!r})."
        )

    @step("Double tap within element")
    def double_tap_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> None:
        """Find element and double-tap at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: doubleTap", {"x": tx, "y": ty})

    @step("Triple tap within element")
    def triple_tap_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> None:
        """Find element and triple-tap at (pct_x%, pct_y%) within its bounds."""
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions import interaction
        from selenium.webdriver.common.actions.pointer_input import PointerInput
        el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
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

    @step("Five tap within element")
    def five_tap_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> None:
        """Find element and tap 5 times at (pct_x%, pct_y%) within its bounds."""
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions import interaction
        from selenium.webdriver.common.actions.pointer_input import PointerInput
        el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        ac = ActionChains(self.driver)
        ac.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        pa = ac.w3c_actions.pointer_action
        for i in range(5):
            pa.move_to_location(tx, ty)
            pa.pointer_down()
            pa.pause(0.05)
            pa.pointer_up()
            if i < 4:
                pa.pause(0.08)
        ac.perform()

    @step("Long press within element")
    def long_press_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, duration: float = 1.0,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> None:
        """Find element and long-press at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: touchAndHold", {"x": tx, "y": ty, "duration": duration})

    @step("Double tap")
    def double_tap(self, element: WebElement) -> None:
        """Double-tap a WebElement."""
        self.driver.execute_script("mobile: doubleTap", {"element": element.id})

    @step("Long press")
    def long_press(self, element: WebElement, duration: float = 1.0) -> None:
        """Long-press a WebElement for *duration* seconds (default 500 ms+)."""
        self.driver.execute_script(
            "mobile: touchAndHold",
            {"element": element.id, "duration": duration},
        )

    @step("Long press and capture preview during hold")
    def long_press_capture_for_preview(
        self,
        press_by: str,
        press_value: str,
        duration: float,
        capture_name: str,
        capture_by: str,
        capture_value: str,
        expected_result: str = "same",
        threshold: Optional[float] = 0.95,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
        compare_folder: str = "pytest/screenshots/compare",
    ) -> None:
        """Capture preview AFTER while a long-press gesture is still holding.

        Sequence: press-down/hold starts -> capture target screenshot -> release.
        """
        el = self.wait_for_visible(
            press_by,
            press_value,
            timeout,
            container_by,
            container_value,
            container_w,
            container_h,
        )
        capture_rect = None
        try:
            capture_el = self.find_element(capture_by, capture_value, timeout=3)
            capture_rect = capture_el.rect
        except Exception as exc:
            logger.warning("Capture target lookup failed before hold (%s); fallback to full-screen", exc)
        screen_pts = self.driver.get_window_size()

        center_x = int(el.rect["x"] + el.rect["width"] / 2)
        center_y = int(el.rect["y"] + el.rect["height"] / 2)

        hold_exc: list[Exception] = []
        hold_done = threading.Event()

        def _run_hold():
            logger.info("[compare-hold] long press start (%d,%d)", center_x, center_y)
            try:
                self._perform_w3c_hold(center_x, center_y, duration)
            except Exception as exc:
                hold_exc.append(exc)
            finally:
                hold_done.set()
                logger.info("[compare-hold] long press end (%d,%d)", center_x, center_y)

        t = threading.Thread(target=_run_hold, daemon=True)
        t.start()
        # Give WDA a brief moment to enter hold state, then capture during hold.
        time.sleep(max(0.05, min(0.2, duration * 0.25)))

        captured = self._capture_preview_after_during_hold(
            name=capture_name,
            capture_rect_pts=capture_rect,
            screen_pts=screen_pts,
            compare_folder=compare_folder,
            threshold=threshold,
            expected_result=expected_result,
        )
        if not captured:
            raise AssertionError("Failed to capture AFTER screenshot during long press hold")
        logger.info("[compare-hold] after screenshot captured during hold")

        t.join(timeout=max(2.0, float(duration) + 2.0))
        if not hold_done.is_set():
            logger.warning("long_press_capture_for_preview: hold thread did not finish in expected window")
        if hold_exc:
            raise hold_exc[0]

    @step("Long press within element and capture preview during hold")
    def long_press_capture_for_preview_within_element(
        self,
        press_by: str,
        press_value: str,
        pct_x: float,
        pct_y: float,
        duration: float,
        capture_name: str,
        capture_by: str,
        capture_value: str,
        expected_result: str = "same",
        threshold: Optional[float] = 0.95,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
        compare_folder: str = "pytest/screenshots/compare",
    ) -> None:
        """Hold at an offset inside press element, capture target screenshot during hold."""
        el = self.wait_for_visible(
            press_by,
            press_value,
            timeout,
            container_by,
            container_value,
            container_w,
            container_h,
        )
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        capture_rect = None
        try:
            capture_el = self.find_element(capture_by, capture_value, timeout=3)
            capture_rect = capture_el.rect
        except Exception as exc:
            logger.warning("Capture target lookup failed before hold (%s); fallback to full-screen", exc)
        screen_pts = self.driver.get_window_size()

        hold_exc: list[Exception] = []
        hold_done = threading.Event()

        def _run_hold():
            logger.info("[compare-hold] long press start (%d,%d)", tx, ty)
            try:
                self._perform_w3c_hold(tx, ty, duration)
            except Exception as exc:
                hold_exc.append(exc)
            finally:
                hold_done.set()
                logger.info("[compare-hold] long press end (%d,%d)", tx, ty)

        t = threading.Thread(target=_run_hold, daemon=True)
        t.start()
        time.sleep(max(0.05, min(0.2, duration * 0.25)))

        captured = self._capture_preview_after_during_hold(
            name=capture_name,
            capture_rect_pts=capture_rect,
            screen_pts=screen_pts,
            compare_folder=compare_folder,
            threshold=threshold,
            expected_result=expected_result,
        )
        if not captured:
            raise AssertionError("Failed to capture AFTER screenshot during long press hold")
        logger.info("[compare-hold] after screenshot captured during hold")

        t.join(timeout=max(2.0, float(duration) + 2.0))
        if not hold_done.is_set():
            logger.warning("long_press_capture_for_preview_within_element: hold thread did not finish in expected window")
        if hold_exc:
            raise hold_exc[0]

    def _perform_w3c_hold(self, x: int, y: int, duration: float) -> None:
        """Perform touch down -> hold -> touch up in one W3C action sequence."""
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions import interaction
        from selenium.webdriver.common.actions.pointer_input import PointerInput

        ac = ActionChains(self.driver)
        ac.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        pa = ac.w3c_actions.pointer_action
        pa.move_to_location(int(x), int(y))
        pa.pointer_down()
        pa.pause(max(0.1, float(duration)))
        pa.pointer_up()
        ac.perform()

    @step("Triple tap")
    def triple_tap(self, element: WebElement) -> None:
        """Triple-tap a WebElement using native XCUITest gesture."""
        self.driver.execute_script(
            "mobile: tapWithNumberOfTaps",
            {"element": element.id, "numberOfTaps": 3, "numberOfTouches": 1},
        )

    @step("Five tap")
    def five_tap(self, element: WebElement) -> None:
        """Tap a WebElement five times using native XCUITest gesture."""
        self.driver.execute_script(
            "mobile: tapWithNumberOfTaps",
            {"element": element.id, "numberOfTaps": 5, "numberOfTouches": 1},
        )

    @step("Two finger tap")
    def two_finger_tap(self, element: WebElement) -> None:
        """
        Two-finger tap on *element* using XCUITest mobile: twoFingerTap.
        This is the native iOS "two-finger tap" recognised by many apps.
        """
        self.driver.execute_script(
            "mobile: twoFingerTap",
            {"element": element.id},
        )
        logger.info("two_finger_tap on element")

    @step("Multi finger tap")
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

    @step("Swipe on element")
    def swipe_on_element(
        self,
        by: str,
        value: str,
        direction: str,
        velocity: float = 500.0,
        from_pct_x: float = 50.0,
        from_pct_y: float = 50.0,
        distance_pts: Optional[float] = None,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
    ) -> None:
        """
        Swipe in *direction* starting from a percentage offset within an element.

        *velocity* is in pixels/second — pass the value computed from the original
        gesture (distance_px * 1000 / duration_ms) to reproduce the recorded speed.
        *from_pct_x / from_pct_y* are the start point as a percentage of the
        element's width / height (0–100, default centre = 50, 50).
        *distance_pts* is the exact swipe distance in logical points from the
        original recording. When omitted, falls back to 40 % of element dimension.
        """
        element = self.find_element(by, value, container_by=container_by, container_value=container_value, container_w=container_w, container_h=container_h)
        rect = element.rect  # {x, y, width, height}

        start_x = rect["x"] + rect["width"]  * from_pct_x / 100
        start_y = rect["y"] + rect["height"] * from_pct_y / 100

        if distance_pts is not None:
            d = distance_pts
            dx_map = {"left": -d, "right": d, "up": 0.0, "down": 0.0}
            dy_map = {"up": -d, "down": d, "left": 0.0, "right": 0.0}
        else:
            dx_map = {"left": -rect["width"] * 0.4, "right": rect["width"] * 0.4,
                      "up": 0.0, "down": 0.0}
            dy_map = {"up": -rect["height"] * 0.4, "down": rect["height"] * 0.4,
                      "left": 0.0, "right": 0.0}

        end_x = start_x + dx_map.get(direction, 0.0)
        end_y = start_y + dy_map.get(direction, 0.0)

        self.driver.execute_script(
            "mobile: dragFromToWithVelocity",
            {
                "fromX": int(start_x),
                "fromY": int(start_y),
                "toX":   int(end_x),
                "toY":   int(end_y),
                "velocity": velocity,
                "pressDuration": 0.05,
                "holdDuration":  0.05,
            },
        )
        logger.info(
            "swipe_on_element: %r direction=%s velocity=%.1f dist=%s start=(%.1f%%,%.1f%%)",
            value, direction, velocity,
            f"{distance_pts:.1f}pts" if distance_pts is not None else "40%",
            from_pct_x, from_pct_y,
        )

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
        logger.info("Scrolled %s", direction)

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
            logger.info("Scroll attempt %d/%d looking for (%s, %r)", attempt + 1, max_scrolls, by, value)
            self.scroll(direction)
        raise NoSuchElementException(
            f"Element ({by}, {value!r}) not found after {max_scrolls} scrolls."
        )

    # ──────────────────────────────────────────
    # Text input
    # ──────────────────────────────────────────

    @step("Type text")
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
    # scroll_until
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
                vis = self._visible_fraction(element)
                if vis >= 0.5:
                    logger.info(
                        "scroll_until: tapping (%s, %r) after %d scrolls (%.0f%% visible)",
                        target_by, target_value, attempt, vis * 100,
                    )
                    return element
                logger.info(
                    "scroll_until: (%s, %r) found but only %.0f%% visible — scrolling more",
                    target_by, target_value, vis * 100,
                )
            logger.info(
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
        logger.info("drag_element: source → target")

    @step("Drag by coordinates")
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
        logger.info("drag_coordinates: (%d,%d) → (%d,%d)", from_x, from_y, to_x, to_y)

    @step("Drag within elements by offset percent")
    def drag_within_elements(
        self,
        from_by: str,
        from_value: str,
        from_pct_x: float,
        from_pct_y: float,
        to_by: str,
        to_value: str,
        to_pct_x: float,
        to_pct_y: float,
        duration: float = 1.0,
    ) -> None:
        """Drag from a % offset within the source element to a % offset within the target element."""
        src = self.find_element(from_by, from_value)
        tgt = self.find_element(to_by, to_value)
        src_loc, src_sz = src.location, src.size
        tgt_loc, tgt_sz = tgt.location, tgt.size
        from_x = round(src_loc["x"] + src_sz["width"]  * from_pct_x / 100)
        from_y = round(src_loc["y"] + src_sz["height"] * from_pct_y / 100)
        to_x   = round(tgt_loc["x"] + tgt_sz["width"]  * to_pct_x   / 100)
        to_y   = round(tgt_loc["y"] + tgt_sz["height"] * to_pct_y   / 100)
        self.driver.execute_script(
            "mobile: dragFromToForDuration",
            {"fromX": from_x, "fromY": from_y, "toX": to_x, "toY": to_y, "duration": duration},
        )
        logger.info(
            "drag_within_elements: %s@(%.1f%%,%.1f%%) → %s@(%.1f%%,%.1f%%)",
            from_value, from_pct_x, from_pct_y, to_value, to_pct_x, to_pct_y,
        )

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
        # velocity is required by xcuitest-driver; use a sensible default when not specified
        effective_velocity = velocity if velocity > 0 else 1.0
        params: dict = {"element": element.id, "scale": scale, "velocity": effective_velocity}
        self.driver.execute_script("mobile: pinch", params)
        logger.info("pinch: scale=%.2f vel=%.1f", scale, velocity)

    @step("Rotate")
    def rotate(
        self,
        element: WebElement,
        rotation: float = 90.0,
        velocity: float = 1.5,
    ) -> None:
        """
        Rotate gesture on *element* via XCUITest mobile: rotateElement.
        rotation : angle in **degrees** (positive = clockwise).
        velocity : speed in radians/sec.
        """
        self.driver.execute_script(
            "mobile: rotateElement",
            {
                "element": element.id,
                "rotation": rotation * math.pi / 180,
                "velocity": velocity,
            },
        )
        logger.info("rotate: %.1f deg at %.1f rad/s", rotation, velocity)

    # ──────────────────────────────────────────
    # System operations
    # ──────────────────────────────────────────

    @step("Press Home button")
    def press_home(self) -> None:
        """Press the physical Home button (sends the app to the background)."""
        self.driver.execute_script("mobile: pressButton", {"name": "home"})
        logger.info("press_home")

    @step("Launch app")
    def launch_app(self, bundle_id: str) -> None:
        """
        Launch *bundle_id*.
        - Already running → brought to foreground.
        - Terminated       → cold-started.
        """
        self.driver.execute_script("mobile: launchApp", {"bundleId": bundle_id})
        logger.info("launch_app: %s", bundle_id)

    @step("Terminate app")
    def terminate_app(self, bundle_id: str) -> None:
        """Force-quit *bundle_id*. No-op if the app is not running."""
        self.driver.execute_script("mobile: terminateApp", {"bundleId": bundle_id})
        logger.info("terminate_app: %s", bundle_id)

    # ──────────────────────────────────────────
    # Verify (assertions)
    # ──────────────────────────────────────────

    @step("Verify element visible")
    def verify_visible(
        self,
        by: str,
        value: str,
        timeout: int = 60,
        msg: str = "",
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
    ) -> WebElement:
        """
        Assert that the element is visible on screen.
        Returns the element so callers can chain further actions.
        Raises AssertionError if not visible within *timeout* seconds.
        """
        try:
            element = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        except (TimeoutException, NoSuchElementException):
            label = msg or f"({by}, {value!r})"
            raise AssertionError(f"verify_visible FAILED – element not visible: {label}")
        return element

    @step("Verify element not visible")
    def verify_not_visible(
        self,
        by: str,
        value: str,
        timeout: int = 5,
        msg: str = "",
    ) -> bool:
        """
        Poll for up to *timeout* seconds waiting for the element to disappear.
        Returns True as soon as the element is absent.
        Raises AssertionError if element is still present after *timeout* seconds.
        """
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if not self.is_element_present(by, value, timeout=1):
                logger.info("verify_not_visible: (%s, %r) is absent", by, value)
                return True
        label = msg or f"({by}, {value!r})"
        raise AssertionError(f"verify_not_visible FAILED – element is still visible after {timeout}s: {label}")

    @step("Verify element text")
    def verify_text(
        self,
        by: str,
        value: str,
        expected: str,
        timeout: int = 5,
    ) -> None:
        """
        Assert that the element's text / label equals *expected*.
        Raises AssertionError with a clear diff message on mismatch.
        """
        element = self.wait_for_visible(by, value, timeout)
        # XCUIElementTypeTextView (and other text inputs) expose their content
        # via the `value` attribute; `element.text` maps to the accessibility
        # label which is often empty for programmatic text views.
        actual = element.text or element.get_attribute("value") or ""
        assert actual == expected, (
            f"verify_text FAILED for ({by}, {value!r})\n"
            f"  expected : {expected!r}\n"
            f"  actual   : {actual!r}"
        )
        logger.info("verify_text PASSED for (%s, %r)", by, value)

    # ──────────────────────────────────────────
    # Screenshot: capture, compare GT, compare preview
    # ──────────────────────────────────────────

    def _attach_to_rp(self, path: str, label: str) -> None:
        """Attach an image file to the active ReportPortal step via logger."""
        try:
            with open(path, "rb") as fh:
                logger.info(
                    label,
                    extra={"attachment": {"name": label, "data": fh.read(), "mime": "image/png"}},
                )
        except Exception as exc:
            logger.warning("Could not attach image to ReportPortal: %s", exc)

    def _get_wda_base_url(self) -> Optional[str]:
        """Return WDA base URL from capabilities, if present."""
        caps = self.driver.capabilities or {}
        return (
            caps.get("appium:webDriverAgentUrl")
            or caps.get("webDriverAgentUrl")
            or caps.get("wdaBaseUrl")
        )

    def _fetch_wda_screenshot_png(self) -> Optional[bytes]:
        """Fetch full-screen PNG bytes directly from WDA (outside Appium session queue)."""
        wda_base = self._get_wda_base_url()
        if not wda_base:
            return None
        url = f"{wda_base.rstrip('/')}/screenshot"
        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=5) as resp:
                raw = resp.read().decode("utf-8")
            data = json.loads(raw)
            b64 = data.get("value") if isinstance(data, dict) else None
            if not b64 and isinstance(data, str):
                b64 = data
            if not b64:
                return None
            return base64.b64decode(b64)
        except Exception as exc:
            logger.warning("WDA direct screenshot failed: %s", exc)
            return None

    def _fetch_mjpeg_frame_bytes(self, timeout_s: float = 1.2) -> Optional[bytes]:
        """Fetch one JPEG frame from WDA MJPEG stream.

        This channel is usually independent of WebDriver command queue and is
        more likely to represent the true during-hold frame.
        """
        wda_base = self._get_wda_base_url()
        if not wda_base:
            return None

        parsed = urllib.parse.urlparse(wda_base)
        host = parsed.hostname or "localhost"
        caps = self.driver.capabilities or {}
        mjpeg_port = caps.get("appium:mjpegServerPort") or caps.get("mjpegServerPort") or 9100
        url = f"http://{host}:{int(mjpeg_port)}/"

        boundary = b"--BoundaryString"
        started = time.monotonic()
        buf = b""
        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                while time.monotonic() - started < timeout_s:
                    chunk = resp.read(4096)
                    if not chunk:
                        break
                    buf += chunk

                    b_start = buf.find(boundary)
                    if b_start == -1:
                        continue
                    h_end = buf.find(b"\r\n\r\n", b_start)
                    if h_end == -1:
                        continue
                    frame_start = h_end + 4

                    cl = None
                    for line in buf[b_start:h_end].split(b"\r\n"):
                        if line.lower().startswith(b"content-length:"):
                            try:
                                cl = int(line.split(b":", 1)[1].strip())
                            except Exception:
                                cl = None
                            break

                    if cl is not None and len(buf) >= frame_start + cl:
                        return buf[frame_start:frame_start + cl]

                    next_b = buf.find(boundary, frame_start)
                    if next_b != -1:
                        frame = buf[frame_start:next_b].rstrip(b"\r\n")
                        if frame:
                            return frame
        except Exception as exc:
            logger.warning("MJPEG frame fetch failed: %s", exc)
        return None

    def _save_image_crop_by_rect(
        self,
        image_bytes: bytes,
        out_path: str,
        rect_pts: Optional[dict],
        screen_pts: Optional[dict],
    ) -> bool:
        """Save a cropped image using point-space rect; returns False if crop is unavailable."""
        if not rect_pts or not screen_pts:
            return False
        try:
            import cv2
            import numpy as np
        except Exception:
            return False

        arr = np.frombuffer(image_bytes, dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        if img is None:
            return False

        h, w = img.shape[:2]
        sw = float(screen_pts.get("width", 0) or 0)
        sh = float(screen_pts.get("height", 0) or 0)
        if sw <= 0 or sh <= 0:
            return False

        sx = w / sw
        sy = h / sh
        x = int((rect_pts.get("x", 0) or 0) * sx)
        y = int((rect_pts.get("y", 0) or 0) * sy)
        cw = int((rect_pts.get("width", 0) or 0) * sx)
        ch = int((rect_pts.get("height", 0) or 0) * sy)
        if cw <= 0 or ch <= 0:
            return False

        x1 = max(0, min(w - 1, x))
        y1 = max(0, min(h - 1, y))
        x2 = max(x1 + 1, min(w, x1 + cw))
        y2 = max(y1 + 1, min(h, y1 + ch))
        crop = img[y1:y2, x1:x2]
        return bool(cv2.imwrite(out_path, crop))

    def _resolve_capture_rect(
        self,
        by: Optional[str],
        value: Optional[str],
        timeout: int = 3,
    ) -> tuple[Optional[dict], Optional[dict]]:
        """Return (rect_pts, screen_pts) for capture target, or (None, None)."""
        if not by or not value:
            return None, None
        try:
            el = self.find_element(by, value, timeout=timeout)
            return el.rect, self.driver.get_window_size()
        except Exception:
            return None, None

    def _save_preview_image(
        self,
        out_path: str,
        rect_pts: Optional[dict],
        screen_pts: Optional[dict],
        by: Optional[str],
        value: Optional[str],
        allow_driver_fallback: bool = True,
        prefer_mjpeg: bool = False,
    ) -> bool:
        """Save preview image from direct channels first; fallback to Appium screenshot."""
        if prefer_mjpeg:
            jpeg = self._fetch_mjpeg_frame_bytes()
            if jpeg and self._save_image_crop_by_rect(jpeg, out_path, rect_pts, screen_pts):
                return True

        png = self._fetch_wda_screenshot_png()
        if png:
            if self._save_image_crop_by_rect(png, out_path, rect_pts, screen_pts):
                return True
            if rect_pts is None or screen_pts is None:
                try:
                    with open(out_path, "wb") as fh:
                        fh.write(png)
                    return True
                except Exception:
                    pass

        if not prefer_mjpeg:
            jpeg = self._fetch_mjpeg_frame_bytes()
            if jpeg and self._save_image_crop_by_rect(jpeg, out_path, rect_pts, screen_pts):
                return True

        # Final fallback for non-hold flow.
        if not allow_driver_fallback:
            return False
        if by and value:
            try:
                el = self.find_element(by, value)
                el.screenshot(out_path)
                return True
            except Exception:
                pass
        try:
            self.driver.save_screenshot(out_path)
            return True
        except Exception:
            return False

    def _capture_preview_after_during_hold(
        self,
        name: str,
        capture_rect_pts: Optional[dict],
        screen_pts: Optional[dict],
        compare_folder: str,
        threshold: Optional[float],
        expected_result: str,
    ) -> bool:
        """Capture AFTER image during hold and enqueue preview comparison."""
        os.makedirs(compare_folder, exist_ok=True)
        pending = self._preview_pending.pop(name, None)
        meta = self._preview_pending_meta.pop(name, (None, None))
        if pending:
            ts, before_path = pending
        else:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            before_path = os.path.join(compare_folder, f"{name}_before.png")
        after_path = os.path.join(compare_folder, f"{name}_{ts}_after.png")

        rect_for_after = capture_rect_pts or meta[0]
        screen_for_after = screen_pts or meta[1]
        saved = self._save_preview_image(
            after_path,
            rect_for_after,
            screen_for_after,
            None,
            None,
            allow_driver_fallback=False,
            prefer_mjpeg=True,
        )

        if not saved:
            logger.warning("Failed to capture AFTER screenshot during hold for %s", name)
            return False

        self._preview_compare_queue.append((name, before_path, after_path, threshold, expected_result))
        logger.info(
            "Captured after screenshot during hold: %s (threshold=%s, expected=%s)",
            after_path,
            threshold,
            expected_result,
        )
        return True

    @step("Capture screenshot for GT comparison")
    def capture_for_gt(
        self,
        name: str,
        by: Optional[str] = None,
        value: Optional[str] = None,
        compare_folder: str = "pytest/screenshots/compare",
        threshold: Optional[float] = None,
    ) -> str:
        """
        Capture the target element (or full screen if no locator) and save it
        to *compare_folder* as ``{name}_{ts}_compare.png`` (timestamp added to
        prevent overwrite on repeated calls).

        The name is queued for GT comparison; call ``run_screenshot_comparisons()``
        at the end of the test to evaluate all queued items.

        *threshold*: per-image SSIM threshold (0–1).  When ``None``, the global
        threshold passed to ``run_screenshot_comparisons()`` is used instead.
        """
        os.makedirs(compare_folder, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(compare_folder, f"{name}_{ts}_compare.png")
        if by and value:
            try:
                el = self.find_element(by, value)
                el.screenshot(path)
            except Exception as exc:
                logger.warning("Element screenshot failed (%s); falling back to full-screen", exc)
                self.driver.save_screenshot(path)
        else:
            self.driver.save_screenshot(path)
        self._gt_compare_queue.append((name, path, threshold))
        logger.info("Captured for GT comparison: %s (threshold=%s)", path, threshold)
        return path

    @step("Capture preview screenshot")
    def capture_for_preview(
        self,
        name: str,
        phase: str,
        by: Optional[str] = None,
        value: Optional[str] = None,
        compare_folder: str = "pytest/screenshots/compare",
        threshold: Optional[float] = None,
        expected_result: str = "same",
    ) -> str:
        """
        Capture the target element (or full screen) for before/after preview diff.

        Saves to ``{name}_{ts}_{phase}.png`` in *compare_folder* (timestamp
        shared between the "before" and "after" pair to prevent overwrite).
        When *phase* == ``"after"``, the name is queued for preview comparison;
        call ``run_screenshot_comparisons()`` at the end of the test to evaluate.

        *threshold*: per-image SSIM threshold (0–1).  When ``None``, the global
        threshold passed to ``run_screenshot_comparisons()`` is used instead.

        *expected_result*: ``"same"`` (default) — similarity ≥ threshold to PASS.
                           ``"different"`` — similarity < threshold to PASS
                           (i.e. the action was expected to visually change the screen).
        Only meaningful when *phase* == ``"after"``.
        """
        os.makedirs(compare_folder, exist_ok=True)
        if phase == "before":
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(compare_folder, f"{name}_{ts}_before.png")
            rect_pts, screen_pts = self._resolve_capture_rect(by, value)
            if not self._save_preview_image(path, rect_pts, screen_pts, by, value):
                raise AssertionError(f"Failed to capture before screenshot: {name}")
            self._preview_pending[name] = (ts, path)
            self._preview_pending_meta[name] = (rect_pts, screen_pts)
            logger.info("Captured before screenshot for preview: %s", path)
        else:
            pending = self._preview_pending.pop(name, None)
            meta = self._preview_pending_meta.pop(name, (None, None))
            if pending:
                ts, before_path = pending
            else:
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                before_path = os.path.join(compare_folder, f"{name}_before.png")  # fallback
            path = os.path.join(compare_folder, f"{name}_{ts}_after.png")
            rect_pts, screen_pts = meta
            if rect_pts is None or screen_pts is None:
                rect_pts, screen_pts = self._resolve_capture_rect(by, value)
            if not self._save_preview_image(path, rect_pts, screen_pts, by, value):
                raise AssertionError(f"Failed to capture after screenshot: {name}")
            self._preview_compare_queue.append((name, before_path, path, threshold, expected_result))
            logger.info(
                "Captured after screenshot for preview: %s (threshold=%s, expected=%s)",
                path, threshold, expected_result,
            )
        return path

    def _compare_images(
        self,
        img_a_path: str,
        img_b_path: str,
        diff_path: str,
    ) -> float:
        """
        Compare two images using SSIM.  Returns the similarity score (1.0 = identical).
        Saves an annotated side-by-side diff PNG to *diff_path* whenever differences
        are found (contour area > 5 px).

        Requires: pip install opencv-python imutils scikit-image numpy
        """
        try:
            import cv2
            import imutils
            import numpy as np
            from skimage.metrics import structural_similarity as compare_ssim
        except ImportError as exc:
            raise ImportError(
                "Screenshot comparison requires opencv-python, imutils, scikit-image, and numpy. "
                "Run: pip install opencv-python imutils scikit-image numpy"
            ) from exc

        img1 = cv2.imread(img_a_path)
        img2 = cv2.imread(img_b_path)

        if img1 is None:
            raise FileNotFoundError(f"Cannot read image: {img_a_path}")
        if img2 is None:
            raise FileNotFoundError(f"Cannot read image: {img_b_path}")

        # Resize img2 to match img1 if sizes differ
        if img1.shape != img2.shape:
            img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]), interpolation=cv2.INTER_LANCZOS4)

        img_height = img1.shape[0]

        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        similar, diff = compare_ssim(gray1, gray2, full=True)
        logger.info("SSIM similarity: %.6f", similar)

        diff = (diff * 255).astype("uint8")
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = imutils.grab_contours(
            cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        )

        for contour in contours:
            if cv2.contourArea(contour) > 5:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        separator = np.zeros((img_height, 10, 3), np.uint8)
        result = np.hstack((img1, separator, img2))
        os.makedirs(os.path.dirname(diff_path), exist_ok=True)
        cv2.imwrite(diff_path, result)
        logger.info("Diff image saved: %s", diff_path)

        return similar

    def compare_with_gt(
        self,
        name: str,
        compare_path: str = "",
        gt_folder: str = "pytest/screenshots/ground_truth",
        threshold: float = 0.99,
    ) -> tuple[bool, str]:
        """
        Compare *compare_path* against ``{name}.png`` in *gt_folder*.

        - GT missing → copy compare screenshot as new GT, log, return ``(False, msg)``.
        - GT exists  → compare via SSIM; if similarity < *threshold* save an annotated
          side-by-side diff image and upload it to ReportPortal,
          return ``(False, msg)``; otherwise return ``(True, "")``.

        *threshold* is the minimum acceptable SSIM similarity (0–1, 1 = identical).
        Does NOT raise — all failures are collected by ``run_screenshot_comparisons()``.
        """
        gt_path   = os.path.join(gt_folder, f"{name}.png")
        diff_path = os.path.splitext(compare_path)[0] + "_diff.png"

        if not os.path.exists(gt_path):
            import shutil
            os.makedirs(gt_folder, exist_ok=True)
            shutil.copy2(compare_path, gt_path)
            msg = f"GT created for '{name}' — first run; re-run to compare"
            logger.info(msg)
            return (False, msg)

        compare_name = os.path.basename(compare_path)
        gt_name      = os.path.basename(gt_path)
        similar = self._compare_images(compare_path, gt_path, diff_path)
        if similar < threshold:
            msg = (
                f"GT diff FAILED for '{name}': "
                f"similarity={similar:.6f} < threshold={threshold:.6f} "
                f"[{compare_name} vs {gt_name}]"
            )
            logger.warning(msg)
            self._attach_to_rp(diff_path, f"diff: {compare_name} vs {gt_name}")
            return (False, msg)

        logger.info("GT diff PASSED for %r (similarity=%.6f) [%s vs %s]", name, similar, compare_name, gt_name)
        return (True, "")

    def compare_preview(
        self,
        name: str,
        before_path: str = "",
        after_path: str = "",
        threshold: float = 0.99,
        expected_result: str = "same",
    ) -> tuple[bool, str]:
        """
        Compare *before_path* against *after_path*.

        *expected_result* controls the pass/fail logic:
        - ``"same"``      — PASS when similarity ≥ *threshold* (images should look alike).
        - ``"different"`` — PASS when similarity < *threshold* (action was expected to
          visually change the screen).

        On failure, saves an annotated diff image and uploads it to ReportPortal.
        Does NOT raise — all failures are collected by ``run_screenshot_comparisons()``.
        """
        diff_path    = os.path.splitext(before_path)[0] + "_diff.png"
        before_name  = os.path.basename(before_path)
        after_name   = os.path.basename(after_path)

        for p in (before_path, after_path):
            if not os.path.exists(p):
                msg = f"Preview diff: file missing for '{name}': {p}"
                logger.warning(msg)
                return (False, msg)

        similar = self._compare_images(before_path, after_path, diff_path)

        if expected_result == "different":
            # PASS when images are sufficiently different
            if similar < threshold:
                logger.info(
                    "Preview diff (expected=different) PASSED for %r (similarity=%.6f) [%s vs %s]",
                    name, similar, before_name, after_name,
                )
                return (True, "")
            msg = (
                f"Preview diff FAILED for '{name}' (expected=different): "
                f"similarity={similar:.6f} >= threshold={threshold:.6f} "
                f"[{before_name} vs {after_name}] — images look the same"
            )
            logger.warning(msg)
            self._attach_to_rp(diff_path, f"diff: {before_name} vs {after_name}")
            return (False, msg)
        else:
            # PASS when images are sufficiently similar (default: "same")
            if similar >= threshold:
                logger.info(
                    "Preview diff (expected=same) PASSED for %r (similarity=%.6f) [%s vs %s]",
                    name, similar, before_name, after_name,
                )
                return (True, "")
            msg = (
                f"Preview diff FAILED for '{name}' (expected=same): "
                f"similarity={similar:.6f} < threshold={threshold:.6f} "
                f"[{before_name} vs {after_name}]"
            )
            logger.warning(msg)
            self._attach_to_rp(diff_path, f"diff: {before_name} vs {after_name}")
            return (False, msg)

    @step("Run all screenshot comparisons")
    def run_screenshot_comparisons(
        self,
        threshold: float = 0.99,
    ) -> None:
        """
        Process every name queued by ``capture_for_gt`` and ``capture_for_preview``.

        *threshold* is the **global** minimum acceptable SSIM similarity (0–1).
        Individual captures may override this with their own threshold by passing
        ``threshold=<value>`` to ``capture_for_gt`` / ``capture_for_preview``.

        AND logic — every comparison runs regardless of previous failures.
        All failure messages are collected and raised together as a single
        ``AssertionError``.  Queues are cleared after the run.
        """
        failures: list[str] = []

        for name, compare_path, item_threshold in self._gt_compare_queue:
            t = item_threshold if item_threshold is not None else threshold
            passed, msg = self.compare_with_gt(name, compare_path=compare_path, threshold=t)
            if not passed:
                failures.append(msg)

        for name, before_path, after_path, item_threshold, expected_result in self._preview_compare_queue:
            t = item_threshold if item_threshold is not None else threshold
            passed, msg = self.compare_preview(name, before_path=before_path, after_path=after_path, threshold=t, expected_result=expected_result)
            if not passed:
                failures.append(msg)

        self._gt_compare_queue.clear()
        self._preview_compare_queue.clear()

        if failures:
            combined = "\n".join(f"  • {f}" for f in failures)
            raise AssertionError(f"Screenshot comparison failures:\n{combined}")
