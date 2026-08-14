# ─────────────────────────────────────────────
# driver/driver_actions.py  –  Low-level UI interactions
# ─────────────────────────────────────────────
# Wraps Appium / W3C Actions into reusable, iOS-aware helpers.
# All page objects receive an instance of this class so that
# gesture logic lives in one place.

import functools
import hashlib
import logging
import math
import os
import re
import threading
import time
import xml.etree.ElementTree as ET
import json
import base64
import urllib.request
import urllib.parse
from datetime import datetime
from typing import List, Optional, Tuple, Union

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
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

# ── wait_until_not_show budgets ────────────────────────────────────────────
# The two waits are counted separately: a short one to confirm the element
# showed up at all, then a long one for the work behind it to finish.  A
# progress/rendering indicator can legitimately stay on screen for minutes,
# but if it never appears within seconds there is nothing to wait for.
DEFAULT_NOT_SHOW_APPEAR_TIMEOUT    = 5      # element must show up within this
DEFAULT_NOT_SHOW_DISAPPEAR_TIMEOUT = 1200   # 20 min for it to go away again
DEFAULT_NOT_SHOW_POLL_INTERVAL     = 1.0    # gap between presence probes

# ── Pre-action element readiness ───────────────────────────────────────────
# A tap coordinate is only as good as the instant its rect was read.  The
# hierarchy-stability check compares structural identity only (tree position +
# tag + child count), so a panel that is still sliding or fading in looks
# "stable" from its very first frame while its frame keeps moving — and iOS
# swallows touches on views that are mid-animation anyway.  Before turning an
# element into a coordinate we therefore wait until its rect stops moving and
# it reports itself visible.
DEFAULT_ELEMENT_SETTLE_INTERVAL = 0.15  # gap between two rect samples
DEFAULT_ELEMENT_SETTLE_TIMEOUT  = 3.0   # give up and act anyway after this long
# How many *consecutive* identical rect samples count as "stopped moving".
# One matching pair is not enough: element.rect is rounded to whole points and
# iOS animations ease in and out, so at the head or tail of a slide-in the frame
# can move less than a point between two samples.  The element then looks parked
# while it is about to accelerate — which is exactly how a drag ends up starting
# from a coordinate the control has already left.
DEFAULT_ELEMENT_SETTLE_SAMPLES  = 2

# ── Slider grab geometry ───────────────────────────────────────────────────
# A UISlider only reacts to a touch that lands on its **thumb**; a press on the
# bare track is ignored outright.  A recorded drag therefore carries the thumb
# position *at record time*, which is only valid while the slider still holds
# the value it had then — otherwise playback presses empty track, the value does
# not move at all, and the following verify reads the old value.  The thumb is
# not published as its own element, so its size comes from
# ``config.SLIDER_THUMB_SIZE``, capped at the control's own thickness.  Accuracy
# matters: these sliders track the finger *relative to where it grabbed*, so a
# press a few points off the thumb centre biases the resulting value — 4 pt was
# measured as ~1.5 units on a 0–100 slider.
SLIDER_TAG = "XCUIElementTypeSlider"
DEFAULT_SLIDER_THUMB_SIZE = 32.0

# ── Values read from config.py ─────────────────────────────────────────────
# One edit there covers the whole suite instead of every generated call site.
# Imported defensively: the AST/contract unit tests import this module without the
# pytest/ config on the path, and a missing config must not break them.
try:  # pragma: no cover - exercised on device, not in unit tests
    import config as _device_config
    _CONFIG_TEXT_TOLERANCE = dict(getattr(_device_config, "TEXT_NUMERIC_TOLERANCE", {}) or {})
    _CONFIG_SLIDER_THUMB = float(
        getattr(_device_config, "SLIDER_THUMB_SIZE", DEFAULT_SLIDER_THUMB_SIZE)
    )
except Exception:  # noqa: BLE001
    _CONFIG_TEXT_TOLERANCE = {}
    _CONFIG_SLIDER_THUMB = DEFAULT_SLIDER_THUMB_SIZE
DEFAULT_STABILITY_IGNORED_ATTRIBUTES = frozenset({"value", "x", "y", "width", "height", "frame"})
DEFAULT_STABILITY_DYNAMIC_TEXT_PATTERNS = (
    re.compile(r"^\s*(?:\d{1,2}:)?\d{1,2}:\d{2}(?:[.:]\d+)?(?:\s*/\s*(?:\d{1,2}:)?\d{1,2}:\d{2}(?:[.:]\d+)?)?\s*$"),
    re.compile(r"^\s*-?\d+(?:\.\d+)?\s*%\s*$"),
)
_STABILITY_SKIP_METHODS = frozenset({
    "find_element",
    "find_elements",
    "wait_for_visible",
    "wait_for_invisible",
    "is_element_present",
    "get_screen_size",
    "take_screenshot",
    "verify_visible",
    "verify_not_visible",
    "wait_until_not_show",
    "verify_text",
    "capture_for_gt",
    "capture_for_preview",
    "compare_with_gt",
    "compare_preview",
    "run_screenshot_comparisons",
    "tap_then_capture_preview",
    "tap_within_element_then_capture_preview",
    "long_press_capture_for_preview",
    "long_press_capture_for_preview_within_element",
})

# These are lookup/verification primitives.  Lookup failures must propagate
# to the action method that called them, while verify_* methods must preserve
# their assertion semantics.
_MISSING_ELEMENT_PROPAGATION_METHODS = frozenset({
    "find_element",
    "find_elements",
    "wait_for_visible",
    "wait_for_invisible",
    "is_element_present",
    "verify_visible",
    "verify_not_visible",
    "wait_until_not_show",
    "verify_text",
})


def _compile_stability_patterns(patterns):
    compiled = []
    for pattern in patterns or ():
        if hasattr(pattern, "fullmatch"):
            compiled.append(pattern)
        else:
            compiled.append(re.compile(pattern))
    return tuple(compiled)


_NUMBER_RE = re.compile(r"^[+-]?\d+(?:[.,]\d+)?$")


def _as_number(text: str) -> Optional[float]:
    """Parse a UI readout as a number, or None when it is not purely numeric.

    Tolerates a trailing unit sign ('50%', '50 %') and a decimal comma, so a
    slider readout is comparable whichever way the app formats it.
    """
    cleaned = str(text or "").strip().rstrip("%").strip()
    if not _NUMBER_RE.match(cleaned):
        return None
    try:
        return float(cleaned.replace(",", "."))
    except ValueError:
        return None


def _is_dynamic_stability_text(value: str, patterns) -> bool:
    text = (value or "").strip()
    return bool(text) and any(pattern.fullmatch(text) for pattern in patterns)


def _hierarchy_stability_signature(
    page_source: str,
    ignored_attributes=DEFAULT_STABILITY_IGNORED_ATTRIBUTES,
    dynamic_text_patterns=DEFAULT_STABILITY_DYNAMIC_TEXT_PATTERNS,
) -> str:
    """Return a hash based on structural identity only (no content fields)."""
    try:
        root = ET.fromstring(page_source)
    except ET.ParseError:
        return hashlib.md5(page_source.encode("utf-8")).hexdigest()

    parts = []

    def _walk(el: ET.Element, path: str) -> None:
        children = list(el)
        # Structural identity only: tree position + element type + child count.
        parts.append(f"{path}|{el.tag}|c={len(children)}")
        for idx, child in enumerate(children):
            _walk(child, f"{path}.{idx}")

    _walk(root, "0")
    digest = hashlib.md5("\n".join(parts).encode("utf-8")).hexdigest()
    element_count = sum(1 for _ in root.iter())
    # Keep count alongside structural digest for optional fallback handling.
    return f"n={element_count}|{digest}"


def wait_for_stable_hierarchy(fn):
    """
    Decorator: after the wrapped action completes, repeatedly poll
    page_source until its normalized structural signature stops changing
    (hierarchy is stable enough for the next UI action).
    Only runs when the DriverActions instance has stability_check = True,
    and only at the outermost call level — nested decorated calls are skipped
    so the check fires exactly once per top-level action.

    Tunable via the instance attributes:
        stability_interval  (float, seconds) – gap between two snapshots
        stability_timeout   (float, seconds) – give up after this long
        stability_min_wait  (float, seconds) – minimum settle time after action
        stability_required_samples – consecutive matching signatures required
        stability_ignored_attributes – XML attrs ignored during comparison
        stability_dynamic_text_patterns – name/label regexes treated as dynamic
    """
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        def _split_sig(sig: str) -> tuple[Optional[int], str]:
            if isinstance(sig, str) and sig.startswith("n=") and "|" in sig:
                head, tail = sig.split("|", 1)
                try:
                    return int(head[2:]), tail
                except ValueError:
                    return None, sig
            return None, sig

        # Track nesting depth so only the outermost call triggers the check.
        depth = getattr(self, "_stability_depth", 0)
        self._stability_depth = depth + 1
        try:
            result = fn(self, *args, **kwargs)
        finally:
            self._stability_depth -= 1

        if self._stability_depth == 0 and getattr(self, "stability_check", False):
            interval = getattr(self, "stability_interval", 0.4)
            timeout = getattr(self, "stability_timeout", 120.0)
            min_wait = getattr(self, "stability_min_wait", 0.8)
            # Minimal safeguard: require at least 1 consecutive stable signature.
            required_samples = max(1, int(getattr(self, "stability_required_samples", 3)))
            count_fallback_enabled = bool(getattr(self, "stability_count_fallback_enabled", True))
            count_fallback_after = float(getattr(self, "stability_count_fallback_after", 2.0))
            count_required_samples = max(2, int(getattr(self, "stability_count_required_samples", 2)))
            started_at = time.monotonic()
            deadline = time.monotonic() + timeout
            prev = None
            prev_count = prev_digest = None
            stable_samples = 0
            stable_count_samples = 0
            while time.monotonic() < deadline:
                time.sleep(interval)
                try:
                    curr = self._hierarchy_stability_signature(self.driver.page_source)
                except StaleElementReferenceException:
                    # WDA can briefly lose the accessibility root while an action
                    # hands off from the app to an external app.  Reacquire it on
                    # the next poll; the normal stability criteria still apply.
                    logger.debug(
                        "[stability] page source unavailable during app handoff after '%s'",
                        fn.__name__,
                    )
                    prev = None
                    prev_count = prev_digest = None
                    stable_samples = 0
                    stable_count_samples = 0
                    continue
                curr_count, curr_digest = _split_sig(curr)

                if prev is None:
                    prev = curr
                    prev_count = curr_count
                    prev_digest = curr_digest
                    continue

                if curr_digest == prev_digest:
                    stable_samples += 1
                    if (
                        stable_samples >= required_samples
                        and time.monotonic() - started_at >= min_wait
                    ):
                        logger.info("[stability] hierarchy stable after action '%s'", fn.__name__)
                        break
                else:
                    stable_samples = 0

                if curr_count is not None and prev_count is not None and curr_count == prev_count:
                    stable_count_samples += 1
                    if (
                        count_fallback_enabled
                        and stable_count_samples >= count_required_samples
                        and time.monotonic() - started_at >= max(min_wait, count_fallback_after)
                    ):
                        logger.info(
                            "[stability] fallback by stable element count after action '%s'",
                            fn.__name__,
                        )
                        break
                else:
                    stable_count_samples = 0

                prev = curr
                prev_count = curr_count
                prev_digest = curr_digest
            else:
                logger.warning(
                    "[stability] hierarchy did not stabilise within %.1fs after '%s'",
                    timeout, fn.__name__,
                )
        return result
    return wrapper


def allow_missing_element(fn):
    """Propagate missing-element errors from actions.

    The decorator name is kept for compatibility with the class decorator, but
    locator failures are intentionally not swallowed: a generated action must
    fail immediately when its target element is absent.
    """
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        try:
            return fn(self, *args, **kwargs)
        except (TimeoutException, NoSuchElementException) as exc:
            logger.error(
                "Action '%s' failed; element not found: %s",
                fn.__name__,
                exc,
            )
            raise

    return wrapper


def _apply_stability_to_all(cls):
    """Apply missing-element propagation and optional stability waits.

    Individual ``@wait_for_stable_hierarchy`` decorators are not needed.  The
    lookup and verify methods listed above remain responsible for propagating
    their own failures.
    """
    for attr_name in list(vars(cls)):
        if attr_name.startswith('_'):
            continue
        method = vars(cls)[attr_name]
        if not callable(method):
            continue

        # Apply missing-element propagation independently from hierarchy
        # stability, so actions that skip stability checks behave the same.
        if attr_name not in _MISSING_ELEMENT_PROPAGATION_METHODS:
            method = allow_missing_element(method)
        if attr_name not in _STABILITY_SKIP_METHODS:
            method = wait_for_stable_hierarchy(method)
        setattr(cls, attr_name, method)
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
        self.stability_check: bool = True

        # How long to wait between two page_source snapshots (seconds).
        self.stability_interval: float = 0.2

        # Maximum time to keep polling before giving up and continuing (seconds).
        self.stability_timeout: float = 120.0

        # Avoid releasing the next action during the first quiet frame of a
        # transition. Playback/progress churn is ignored by the signature, so
        # require a short settle window and several matching samples.
        self.stability_min_wait: float = 0.8
        self.stability_required_samples: int = 1
        # Fallback for continuously changing screens (e.g. playing videos):
        # if full structural identity keeps changing, allow release when
        # element count remains stable for a short period.
        self.stability_count_fallback_enabled: bool = True
        self.stability_count_fallback_after: float = 2.0
        self.stability_count_required_samples: int = 2

        # Compare a normalized hierarchy signature instead of the raw XML.
        # Playback/progress values can change forever while the tappable UI is
        # already structurally ready for the next action.
        self.stability_ignored_attributes = set(DEFAULT_STABILITY_IGNORED_ATTRIBUTES)
        self.stability_dynamic_text_patterns = DEFAULT_STABILITY_DYNAMIC_TEXT_PATTERNS
        # ──────────────────────────────────────────────────────────────────

        # ── Pre-action element readiness (rect settle + visible gate) ──────
        # Runs on the element itself, not on page_source, so it costs a couple
        # of cheap round-trips rather than a full hierarchy dump.  Set
        # element_settle_check = False to restore the old fire-immediately
        # behaviour for a test that cannot afford the extra time.
        self.element_settle_check: bool = True
        self.element_settle_interval: float = DEFAULT_ELEMENT_SETTLE_INTERVAL
        self.element_settle_timeout: float = DEFAULT_ELEMENT_SETTLE_TIMEOUT
        self.element_settle_required_samples: int = DEFAULT_ELEMENT_SETTLE_SAMPLES
        # ──────────────────────────────────────────────────────────────────

        # ── verify_text numeric tolerance per element id ───────────────────
        # Readouts driven by a replayed coordinate gesture (slider values) are not
        # reproducible to the digit; see config.TEXT_NUMERIC_TOLERANCE.  Every id
        # not listed keeps an exact string compare.
        self.text_numeric_tolerance: dict = dict(_CONFIG_TEXT_TOLERANCE)
        # Thumb size used to place a press on a slider — see config.SLIDER_THUMB_SIZE.
        self.slider_thumb_size: float = _CONFIG_SLIDER_THUMB
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
        # Pending before-captures: (name, pair_suffix) → (ts, before_path), waiting
        # for the matching "after".  The suffix lets one *name* keep several pairs
        # alive at once (e.g. phase="before_min_ic_jaw" pairs with "after_min_ic_jaw").
        self._preview_pending: dict[tuple[str, str], tuple[str, str]] = {}
        # Optional metadata captured at "before" to keep before/after crop geometry identical.
        self._preview_pending_meta: dict[tuple[str, str], tuple[Optional[dict], Optional[dict]]] = {}
        # ──────────────────────────────────────────────────────────────────

    def _hierarchy_stability_signature(self, page_source: str) -> str:
        return _hierarchy_stability_signature(
            page_source,
            ignored_attributes=getattr(
                self,
                "stability_ignored_attributes",
                DEFAULT_STABILITY_IGNORED_ATTRIBUTES,
            ),
            dynamic_text_patterns=getattr(
                self,
                "stability_dynamic_text_patterns",
                DEFAULT_STABILITY_DYNAMIC_TEXT_PATTERNS,
            ),
        )

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

        When container_by / container_value are provided the lookup runs in three stages:

          1. Global search — return the element straight away when it is already
             ≥ 50 % visible.  A stale container selector cannot break this stage,
             which is the common failure mode for recorded structural xpaths.
          2. Container-scoped search — resolve the container, then search inside it.
          3. _find_with_scroll() — probe the container axis, rewind to start, and
             scroll forward until the element is ≥ 50 % visible.

        "Visible" is measured against the container's rect as well as the screen
        (see ``_visible_fraction``), so a cell clipped by its own collection view no
        longer counts as on-screen.  When the container cannot be resolved the
        measurement falls back to screen-only rather than failing the lookup.

        All other methods that take (by, value) forward these params here, so the
        same lookup order applies uniformly to every action.
        """
        if container_by and container_value:
            # 1. Global first — cheapest path, and immune to a stale container selector
            try:
                global_el = WebDriverWait(self.driver, min(5, timeout)).until(
                    EC.presence_of_element_located((by, value))
                )
                rect = global_el.rect
                # Clipping can only lower the fraction, so the container probe is
                # only worth paying for when the cheap screen-only measurement
                # would have accepted — an xpath container is not a free lookup.
                if self._visible_fraction(global_el, rect) >= 0.5:
                    clip = self._container_clip(container_by, container_value)
                    if self._visible_fraction(global_el, rect, clip=clip) >= 0.5:
                        return global_el
                    logger.info(
                        "find_element: global hit for (%s, %r) is clipped by container "
                        "(%s, %r) — falling through to container search",
                        by, value, container_by, container_value,
                    )
            except TimeoutException:
                pass
            # 2. Not found globally (or off-screen) — search inside the container
            try:
                container_el = WebDriverWait(self.driver, min(5, timeout)).until(
                    EC.presence_of_element_located((container_by, container_value))
                )
                try:
                    clip = container_el.rect
                except Exception:
                    clip = None
                try:
                    scoped_el = container_el.find_element(by, value)
                except NoSuchElementException:
                    scoped_el = None
                if scoped_el is not None and self._visible_fraction(scoped_el, clip=clip) >= 0.5:
                    return scoped_el
            except TimeoutException:
                pass
            # 3. Still nothing visible — scroll the container until it comes into view
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
        """Return all matching elements or raise when none are found."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException as exc:
            raise NoSuchElementException(
                f"Elements not found: ({by}, {value!r})"
            ) from exc

        elements = self.driver.find_elements(by, value)
        if not elements:
            raise NoSuchElementException(f"Elements not found: ({by}, {value!r})")
        return elements

    # ── Pre-action element readiness ───────────────────────────────────────

    @staticmethod
    def _reports_visible(element: WebElement) -> bool:
        """XCUITest ``visible`` attribute as a bool.

        Returns True when the attribute is missing or unreadable, so an element
        type that does not publish it is never blocked from being acted on.
        """
        try:
            raw = element.get_attribute("visible")
        except StaleElementReferenceException:
            raise
        except Exception:
            return True
        if raw is None:
            return True
        return str(raw).strip().lower() in ("true", "1")

    @staticmethod
    def _describe_element(element: WebElement) -> str:
        """Best-effort identifier for log messages (only used on the slow path)."""
        try:
            return element.get_attribute("name") or element.tag_name or "element"
        except Exception:
            return "element"

    def _settle_rects(self, elements: List[WebElement]) -> List[dict]:
        """Wait until *every* element's rect stops moving in the **same** round.

        Returns one rect per element (``{x, y, width, height}``), all read in the
        final polling round, so a caller deriving several coordinates gets them
        from a single quiet moment.

        Settling elements one after another is not equivalent: the first
        element's rect is frozen while the second is still being polled, so a
        drag whose source and target both live on a panel that is animating in
        starts from a coordinate measured hundreds of ms — and possibly a
        different frame — before the end coordinate.  Both elements "settled",
        the drag still misses.

        Release requires ``element_settle_required_samples`` consecutive rounds
        in which no rect changed, every rect is non-degenerate, and every element
        reports ``visible``.  Never raises on timeout — it logs a warning and
        hands back the last rects it saw, so this can only make a flaky step less
        flaky, never turn a currently-passing step into a failure.
        ``StaleElementReferenceException`` still propagates: callers that know how
        to re-resolve already retry on it.
        """
        rects = [el.rect for el in elements]
        if not getattr(self, "element_settle_check", True):
            return rects
        interval = float(getattr(self, "element_settle_interval", DEFAULT_ELEMENT_SETTLE_INTERVAL))
        timeout = float(getattr(self, "element_settle_timeout", DEFAULT_ELEMENT_SETTLE_TIMEOUT))
        required = max(1, int(getattr(
            self, "element_settle_required_samples", DEFAULT_ELEMENT_SETTLE_SAMPLES
        )))
        deadline = time.monotonic() + timeout
        prev: Optional[List[dict]] = None
        matching_rounds = 0
        while True:
            still = (
                prev is not None
                and rects == prev
                and all(r.get("width", 0) > 0 and r.get("height", 0) > 0 for r in rects)
            )
            # The visible probe is another round-trip per element, so only pay for
            # it once the rects have stopped moving — a frame that is still gliding
            # is not actionable regardless of what `visible` says.
            visible = all(self._reports_visible(el) for el in elements) if still else None
            matching_rounds = matching_rounds + 1 if (still and visible) else 0
            if matching_rounds >= required:
                return rects
            if time.monotonic() >= deadline:
                logger.warning(
                    "[settle] %s not settled within %.1fs (rects=%s prev=%s visible=%s "
                    "matching_rounds=%d/%d); acting anyway",
                    ", ".join(repr(self._describe_element(el)) for el in elements),
                    timeout, rects, prev, visible, matching_rounds, required,
                )
                return rects
            prev = rects
            time.sleep(interval)
            rects = [el.rect for el in elements]

    def _element_settle(self, element: WebElement) -> dict:
        """Wait until *element*'s rect stops moving and it reports visible.

        Single-element form of :meth:`_settle_rects` — see there for the details
        and the failure mode it protects against.
        """
        return self._settle_rects([element])[0]

    @staticmethod
    def _pct_point(rect: dict, pct_x: float, pct_y: float) -> Tuple[int, int]:
        """Absolute point at (pct_x%, pct_y%) of an already-read rect."""
        x = round(float(rect["x"]) + float(rect["width"]) * float(pct_x) / 100)
        y = round(float(rect["y"]) + float(rect["height"]) * float(pct_y) / 100)
        return int(x), int(y)

    def _point_in_element(self, element: WebElement, pct_x: float = 50.0, pct_y: float = 50.0) -> Tuple[int, int]:
        return self._pct_point(self._element_settle(element), pct_x, pct_y)

    def _points_in_elements(
        self, specs: List[Tuple[WebElement, float, float]]
    ) -> List[Tuple[int, int]]:
        """Points for several elements, all derived from one quiet moment.

        *specs* is ``[(element, pct_x, pct_y), ...]``; use this instead of
        calling :meth:`_point_in_element` per element whenever one gesture needs
        more than one element-derived coordinate (every drag variant).
        """
        rects = self._settle_rects([el for el, _, _ in specs])
        return [
            self._pct_point(rect, pct_x, pct_y)
            for rect, (_, pct_x, pct_y) in zip(rects, specs)
        ]

    # ── Slider awareness ───────────────────────────────────────────────────

    def _slider_fraction(self, element: WebElement) -> Optional[float]:
        """Normalised position (0.0–1.0) of a slider, or None if not a slider.

        XCUITest publishes it as the ``value`` attribute, usually ``"51%"`` but
        occasionally a bare number or a 0–1 float depending on the control.
        """
        try:
            if element.tag_name != SLIDER_TAG:
                return None
            raw = element.get_attribute("value")
        except StaleElementReferenceException:
            raise
        except Exception:
            return None
        text = str(raw or "").strip()
        if not text:
            return None
        try:
            number = float(text.rstrip("%").strip())
        except ValueError:
            return None
        if text.endswith("%") or number > 1.0:
            number /= 100.0
        return max(0.0, min(1.0, number))

    def _slider_grab_point(
        self, element: WebElement, rect: dict, point: Tuple[int, int]
    ) -> Tuple[int, int]:
        """Move a press point onto a slider's thumb; other elements pass through.

        The recorded coordinate is where the thumb sat when the gesture was
        recorded.  Replaying it against a slider holding a different value presses
        bare track, which UISlider ignores — the gesture silently does nothing and
        the failure only surfaces at the next verify.  The thumb's current
        position is derived from the control's own ``value`` instead.
        """
        frac = self._slider_fraction(element)
        if frac is None:
            return point
        vertical = rect["height"] > rect["width"]
        span = rect["height"] if vertical else rect["width"]
        thickness = rect["width"] if vertical else rect["height"]
        thumb = min(float(thickness), float(getattr(
            self, "slider_thumb_size", DEFAULT_SLIDER_THUMB_SIZE
        )))
        travel = max(0.0, float(span) - thumb)
        # A vertical slider's 0 % end is at the bottom.
        offset = (thumb / 2) + (1.0 - frac if vertical else frac) * travel
        if vertical:
            grabbed = (point[0], int(round(rect["y"] + offset)))
        else:
            grabbed = (int(round(rect["x"] + offset)), point[1])
        if grabbed != point:
            logger.info(
                "[slider] %r sits at %.0f%%; pressing its thumb at %s instead of the "
                "recorded %s (a press on the bare track is ignored)",
                self._describe_element(element), frac * 100, grabbed, point,
            )
        return grabbed

    def _drag_points(
        self,
        from_by: str,
        from_value: str,
        from_pct_x: float,
        from_pct_y: float,
        to_by: str,
        to_value: str,
        to_pct_x: float,
        to_pct_y: float,
        timeout: int = DEFAULT_WAIT,
    ) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """Both ends of a drag, resolved and measured from one quiet moment.

        Re-resolves once on ``StaleElementReferenceException``: the panel a drag
        acts on is frequently rebuilt by the step before it, which invalidates the
        handle between the lookup and the rect read.
        """
        for attempt in range(2):
            src = self.find_element(from_by, from_value, timeout)
            tgt = self.find_element(to_by, to_value, timeout)
            try:
                src_rect, tgt_rect = self._settle_rects([src, tgt])
                start = self._slider_grab_point(
                    src, src_rect, self._pct_point(src_rect, from_pct_x, from_pct_y)
                )
                end = self._pct_point(tgt_rect, to_pct_x, to_pct_y)
                logger.info(
                    "_drag_points: %r rect=%s @(%.1f%%,%.1f%%) → %s | %r rect=%s "
                    "@(%.1f%%,%.1f%%) → %s",
                    from_value, src_rect, from_pct_x, from_pct_y, start,
                    to_value, tgt_rect, to_pct_x, to_pct_y, end,
                )
                return start, end
            except StaleElementReferenceException:
                if attempt == 1:
                    raise
                logger.debug(
                    "_drag_points: stale element for (%s, %r) → (%s, %r); re-resolving",
                    from_by, from_value, to_by, to_value,
                )
        raise RuntimeError("unreachable")  # pragma: no cover

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
    # Element state / value queries  (SFT conversion additions)
    # ──────────────────────────────────────────

    def is_element_enabled(self, by: str, value: str, timeout: int = 3) -> bool:
        """Non-throwing check: True if the element is present and enabled."""
        try:
            el = self.find_element(by, value, timeout=timeout)
            return bool(el.is_enabled())
        except (TimeoutException, NoSuchElementException):
            return False

    def is_element_highlighted(self, by: str, value: str, timeout: int = 3) -> bool:
        """Non-throwing check: True if the element reports a selected/highlighted state.

        iOS surfaces highlight/selection through the ``selected`` or ``value``
        attribute depending on the control, so both are inspected.
        """
        try:
            el = self.find_element(by, value, timeout=timeout)
        except (TimeoutException, NoSuchElementException):
            return False
        for attr in ("selected", "value"):
            try:
                v = el.get_attribute(attr)
            except Exception:
                v = None
            if str(v).lower() in ("true", "1"):
                return True
        return False

    def get_element(self, by: str, value: str, timeout: int = 3) -> Optional[WebElement]:
        """Non-throwing element fetch: returns the WebElement or None (legacy parity).

        Mirrors the legacy page-object ``get_element`` so preserved expressions like
        ``el = actions.get_element(...)`` / ``if actions.get_element(...) is not None``
        translate faithfully. Use ``find_element`` when you want a raise-on-absence fetch.
        """
        try:
            return self.find_element(by, value, timeout=timeout)
        except (TimeoutException, NoSuchElementException):
            return None

    def get_text(self, by: str, value: str, timeout: int = DEFAULT_WAIT) -> str:
        """Return the element's visible text/label; raises when the element is absent.

        Falls back to the ``label`` / ``value`` / ``name`` attribute when ``.text``
        is empty (common for iOS controls).
        """
        el = self.find_element(by, value, timeout=timeout)
        txt = el.text
        if not txt:
            for attr in ("label", "value", "name"):
                try:
                    a = el.get_attribute(attr)
                except Exception:
                    a = None
                if a:
                    txt = a
                    break
        return txt or ""

    def get_element_bounds(
        self, by: str, value: str, timeout: int = DEFAULT_WAIT
    ) -> Tuple[int, int, int, int]:
        """Return (x, y, w, h) in points for the element; raises when absent."""
        el = self.find_element(by, value, timeout=timeout)
        r = el.rect
        return int(r["x"]), int(r["y"]), int(r["width"]), int(r["height"])

    def set_slider(self, by: str, value: str, percent: float, timeout: int = DEFAULT_WAIT) -> bool:
        """Drag a horizontal slider thumb to *percent* (0–100) of the track width.

        Implemented via the drag primitive (no dedicated slider gesture in XCUITest):
        reads the slider element's on-device bounds, then drags along its horizontal
        mid-line from the current left edge to the target percentage position.
        """
        el = self.find_element(by, value, timeout=timeout)
        rect = el.rect
        x, y, w, h = (
            int(rect["x"]),
            int(rect["y"]),
            int(rect["width"]),
            int(rect["height"]),
        )
        cy = y + h // 2
        target_percent = max(0.0, min(100.0, float(percent)))
        current_value = el.get_attribute("value") or ""
        current_match = re.search(r"-?\d+(?:\.\d+)?", str(current_value))
        current_percent = float(current_match.group()) if current_match else 50.0
        current_percent = max(0.0, min(100.0, current_percent))
        start_x = x + int(w * current_percent / 100.0)
        target_x = x + int(w * target_percent / 100.0)
        self.drag_coordinates(start_x, cy, target_x, cy)
        logger.info("set_slider (%s,%r) -> %.1f%% (x=%d)", by, value, target_percent, target_x)
        return True

    def try_tap(self, by: str, value: str, timeout: int = 3) -> bool:
        """Non-throwing tap: tap the element if present, return True/False (legacy
        bool-style parity, for use in `if not actions.try_tap(...):` conditions)."""
        try:
            el = self.find_element(by, value, timeout=timeout)
        except (TimeoutException, NoSuchElementException):
            return False
        try:
            el.click(); return True
        except Exception:
            return False

    def try_tap_any(self, candidates, timeout: int = 1) -> bool:
        """Tap the first present element among (by, value) candidates; return True if any tapped."""
        for by, value in candidates:
            if self.try_tap(by, value, timeout=timeout):
                return True
        return False

    def execute_script(self, script: str, args: Optional[dict] = None):
        """Passthrough to the underlying Appium driver (e.g. ``mobile:`` commands)."""
        if args is None:
            return self.driver.execute_script(script)
        return self.driver.execute_script(script, args)

    def open_url(self, url: str) -> bool:
        """Open a URL / deep link in the current context (webview or Safari handoff)."""
        self.driver.get(url)
        return True

    # ──────────────────────────────────────────
    # Tap / click
    # ──────────────────────────────────────────

    @step("Tap element")
    def tap(self, element: WebElement) -> bool:
        """Tap a WebElement."""
        element.click()
        return True

    @step("Tap by locator")
    def tap_by_locator(
        self, by: str, value: str, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> bool:
        """Find and tap an element; raise immediately when it is absent."""
        element = self.wait_for_visible(
            by, value, timeout, container_by, container_value, container_w, container_h
        )
        self._element_settle(element)
        self.tap(element)
        return True

    @step("Tap at coordinates")
    def tap_by_coordinates(self, x: int, y: int) -> bool:
        """
        Tap at absolute screen coordinates using the iOS mobile:tap command.
        Coordinates are in points (not pixels).
        """
        self.driver.execute_script("mobile: tap", {"x": x, "y": y})
        logger.info("Tapped at (%d, %d)", x, y)
        return True

    def _visible_fraction(
        self,
        element: WebElement,
        rect: Optional[dict] = None,
        clip: Optional[dict] = None,
    ) -> float:
        """Return the fraction (0.0–1.0) of element that is actually reachable.

        Pass *rect* to reuse a rect that was already read (e.g. the one
        ``_element_settle()`` just returned) instead of paying another round-trip.

        Pass *clip* (the container's rect) whenever the element lives inside a
        scrollable container.  The screen alone is not the right boundary: a
        collection-view cell scrolled to the edge of a 430×84 strip is clipped by
        the strip long before it leaves the screen, yet a screen-only measurement
        still calls it 100 % visible — so the caller stops scrolling and taps a
        cell that is half cut off, or the neighbouring one.

        When the element is larger than the clip window (a wrapper that overflows
        its container) the denominator is capped at the window area, so filling the
        window counts as fully visible instead of being penalised for its size.
        A degenerate clip (zero/negative size) is ignored.
        """
        r = rect if rect is not None else element.rect
        el_x, el_y, el_w, el_h = r["x"], r["y"], r["width"], r["height"]
        el_area = el_w * el_h
        if el_area <= 0:
            return 0.0

        win = self.driver.get_window_size()
        bx1, by1 = 0, 0
        bx2, by2 = win["width"], win["height"]
        clipped = bool(clip) and clip.get("width", 0) > 0 and clip.get("height", 0) > 0
        if clipped:
            bx1 = max(bx1, clip["x"])
            by1 = max(by1, clip["y"])
            bx2 = min(bx2, clip["x"] + clip["width"])
            by2 = min(by2, clip["y"] + clip["height"])
        if bx2 <= bx1 or by2 <= by1:
            return 0.0

        ix1 = max(el_x, bx1)
        iy1 = max(el_y, by1)
        ix2 = min(el_x + el_w, bx2)
        iy2 = min(el_y + el_h, by2)
        if ix2 <= ix1 or iy2 <= iy1:
            return 0.0

        # Only the clipped path caps the denominator — the screen-only measurement
        # keeps its original semantics so existing call sites are unaffected.
        denom = min(el_area, (bx2 - bx1) * (by2 - by1)) if clipped else el_area
        return (ix2 - ix1) * (iy2 - iy1) / denom

    def _container_clip(self, container_by: str, container_value: str) -> Optional[dict]:
        """Container rect for visibility clipping, or None when it cannot be read.

        Uses a no-wait ``find_elements`` lookup: the global fast path in
        ``find_element()`` must never pay a locator timeout for a container that is
        stale or gone — it just falls back to screen-only clipping.
        """
        try:
            found = self.driver.find_elements(container_by, container_value)
            return found[0].rect if found else None
        except Exception:
            return None

    def _coord_at_pct(self, element: WebElement, pct_x: float, pct_y: float) -> Tuple[int, int]:
        """Compute absolute screen coordinates at (pct_x%, pct_y%) within element bounds.

        Waits for the element to stop moving and report visible first — see
        ``_element_settle()``.  Without it a percent offset read mid-animation
        lands next to the target and ``mobile: tap`` reports success anyway.
        """
        rect = self._element_settle(element)
        return (
            int(rect["x"] + rect["width"]  * pct_x / 100),
            int(rect["y"] + rect["height"] * pct_y / 100),
        )

    @step("Tap within element")
    def tap_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> bool:
        """Find element and tap at (pct_x%, pct_y%) within its bounds."""
        for attempt in range(2):
            el = self.wait_for_visible(
                by, value, timeout, container_by, container_value, container_w, container_h
            )
            try:
                tx, ty = self._coord_at_pct(el, pct_x, pct_y)
                break
            except StaleElementReferenceException:
                if attempt == 1:
                    raise
                logger.debug(
                    "tap_within_element: stale element for (%s, %r); re-resolving",
                    by,
                    value,
                )
        self.driver.execute_script("mobile: tap", {"x": tx, "y": ty})
        return True

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
            try:
                container_el = self.driver.find_element(container_by, container_value)
                el = container_el.find_element(by, value)
                # Clip by the container: a cell parked at the edge of its own
                # collection view is not reachable even though it is on screen.
                if self._visible_fraction(el, clip=container_el.rect) >= 0.5:
                    logger.info(
                        "_find_with_scroll: found (%s, %r) after %d scrolls",
                        by, value, attempt,
                    )
                    return el
            except NoSuchElementException:
                pass
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
    ) -> bool:
        """Find element and double-tap at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: doubleTap", {"x": tx, "y": ty})
        return True

    @step("Triple tap within element")
    def triple_tap_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> bool:
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
        return True

    @step("Five tap within element")
    def five_tap_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> bool:
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
        return True

    @step("Long press within element")
    def long_press_within_element(
        self, by: str, value: str, pct_x: float, pct_y: float, duration: float = 1.0,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None, container_value: Optional[str] = None,
        container_w: int = 0, container_h: int = 0,
    ) -> bool:
        """Find element and long-press at (pct_x%, pct_y%) within its bounds."""
        el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        tx, ty = self._coord_at_pct(el, pct_x, pct_y)
        self.driver.execute_script("mobile: touchAndHold", {"x": tx, "y": ty, "duration": duration})
        return True

    @step("Double tap")
    def double_tap(self, element: WebElement) -> bool:
        """Double-tap a WebElement."""
        self.driver.execute_script("mobile: doubleTap", {"element": element.id})
        return True

    @step("Long press")
    def long_press(self, element: WebElement, duration: float = 1.0) -> bool:
        """Long-press a WebElement for *duration* seconds (default 500 ms+)."""
        self.driver.execute_script(
            "mobile: touchAndHold",
            {"element": element.id, "duration": duration},
        )
        return True

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
        threshold: Optional[float] = None,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
        compare_folder: str = "pytest/screenshots/compare",
    ) -> bool:
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
        return True

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
        threshold: Optional[float] = None,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
        compare_folder: str = "pytest/screenshots/compare",
    ) -> bool:
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
        return True

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

    def _perform_w3c_drag(
        self,
        from_x: int,
        from_y: int,
        to_x: int,
        to_y: int,
        duration: float = 1.0,
        press_duration: float = 1.0,
    ) -> None:
        """Perform touch down -> hold -> move -> release with separate timings."""
        self._perform_w3c_drag_path(
            [(from_x, from_y), (to_x, to_y)],
            [max(100, int(float(duration) * 1000))],
            press_duration,
        )

    def _perform_w3c_drag_path(
        self,
        points: List[Tuple[int, int]],
        move_durations_ms: List[int],
        press_duration: float = 1.0,
        release_pause: float = 0.08,
    ) -> None:
        """Perform touch down -> hold -> multiple moves -> release."""
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions import interaction
        from selenium.webdriver.common.actions.pointer_input import PointerInput

        if len(points) < 2:
            raise ValueError("drag path needs at least two points")
        if len(move_durations_ms) != len(points) - 1:
            raise ValueError("move duration count must match path segment count")

        hold_s = max(0.0, float(press_duration))
        pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
        start_x, start_y = points[0]
        pointer.create_pointer_move(duration=0, x=int(start_x), y=int(start_y), origin="viewport")
        pointer.create_pointer_down()
        pointer.create_pause(hold_s)
        for (x, y), move_ms in zip(points[1:], move_durations_ms):
            pointer.create_pointer_move(
                duration=max(16, int(move_ms)),
                x=int(x),
                y=int(y),
                origin="viewport",
            )
        if release_pause > 0:
            pointer.create_pause(float(release_pause))
        pointer.create_pointer_up(0)
        ActionBuilder(self.driver, mouse=pointer).perform()

    @staticmethod
    def _split_duration(total_ms: int, weights: List[int]) -> List[int]:
        total_ms = max(100, int(total_ms))
        weight_sum = max(1, sum(weights))
        durations = [max(16, int(total_ms * w / weight_sum)) for w in weights]
        durations[-1] += total_ms - sum(durations)
        return durations

    def _perform_w3c_drag_with_activation_nudge(
        self,
        from_x: int,
        from_y: int,
        to_x: int,
        to_y: int,
        duration: float = 1.0,
        press_duration: float = 1.0,
        activation_nudge_y: int = 0,
    ) -> None:
        """Drag through a tiny vertical nudge before the main move."""
        move_ms = max(100, int(float(duration) * 1000))
        nudge_y = int(activation_nudge_y)

        if nudge_y:
            points = [
                (from_x, from_y),
                (from_x, from_y + nudge_y),
                (round(from_x + (to_x - from_x) * 0.45), round(from_y + nudge_y + (to_y - from_y) * 0.45)),
                (to_x, to_y + nudge_y),
                (to_x, to_y),
            ]
            durations = self._split_duration(move_ms, [1, 3, 3, 1])
        else:
            points = [
                (from_x, from_y),
                (round(from_x + (to_x - from_x) * 0.35), round(from_y + (to_y - from_y) * 0.35)),
                (round(from_x + (to_x - from_x) * 0.75), round(from_y + (to_y - from_y) * 0.75)),
                (to_x, to_y),
            ]
            durations = self._split_duration(move_ms, [2, 3, 3])

        self._perform_w3c_drag_path(
            points,
            durations,
            press_duration,
            release_pause=0.12,
        )

    @step("Triple tap")
    def triple_tap(self, element: WebElement) -> bool:
        """Triple-tap a WebElement using native XCUITest gesture."""
        self.driver.execute_script(
            "mobile: tapWithNumberOfTaps",
            {"element": element.id, "numberOfTaps": 3, "numberOfTouches": 1},
        )
        return True

    @step("Five tap")
    def five_tap(self, element: WebElement) -> bool:
        """Tap a WebElement five times using native XCUITest gesture."""
        self.driver.execute_script(
            "mobile: tapWithNumberOfTaps",
            {"element": element.id, "numberOfTaps": 5, "numberOfTouches": 1},
        )
        return True

    @step("Two finger tap")
    def two_finger_tap(self, element: WebElement) -> bool:
        """
        Two-finger tap on *element* using XCUITest mobile: twoFingerTap.
        This is the native iOS "two-finger tap" recognised by many apps.
        """
        self.driver.execute_script(
            "mobile: twoFingerTap",
            {"element": element.id},
        )
        logger.info("two_finger_tap on element")
        return True

    @step("Multi finger tap")
    def multi_finger_tap(
        self,
        element: WebElement,
        fingers: int = 3,
        pause_ms: int = 50,
    ) -> bool:
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
        return True

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
    ) -> bool:
        """
        Swipe in *direction* starting from a percentage offset within an element.

        *velocity* is in pixels/second — pass the value computed from the original
        gesture (distance_px * 1000 / duration_ms) to reproduce the recorded speed.
        *from_pct_x / from_pct_y* are the start point as a percentage of the
        element's width / height (0–100, default centre = 50, 50).
        *distance_pts* is the exact swipe distance in logical points from the
        original recording. When omitted, falls back to 40 % of element dimension.
        """
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions import interaction
        from selenium.webdriver.common.actions.pointer_input import PointerInput

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

        # Use W3C pointer actions (same as WDA during recording) so the finger
        # lifts while still in motion, preserving momentum for page-turn triggers.
        # mobile: dragFromToWithVelocity holds at the endpoint before lifting,
        # zeroing out velocity and preventing iOS scroll views from flipping pages.
        # move_to_location() hardcodes 250 ms; use create_pointer_move() directly
        # to set the exact duration derived from the recorded velocity.
        duration_ms = max(100, int(distance_pts * 1000 / velocity)) if (distance_pts and velocity > 0) else 400
        pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
        pointer.create_pointer_move(duration=0, x=int(start_x), y=int(start_y), origin="viewport")
        pointer.create_pointer_down()
        pointer.create_pointer_move(duration=duration_ms, x=int(end_x), y=int(end_y), origin="viewport")
        pointer.create_pointer_up(0)
        ActionBuilder(self.driver, mouse=pointer).perform()

        logger.info(
            "swipe_on_element: %r direction=%s velocity=%.1f dist=%s start=(%.1f%%,%.1f%%) dur=%dms",
            value, direction, velocity,
            f"{distance_pts:.1f}pts" if distance_pts is not None else "40%",
            from_pct_x, from_pct_y, duration_ms,
        )
        return True

    @step("Scroll")
    def scroll(self, direction: str = "down", distance: float = 0.5) -> bool:
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
        return True

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
    def type_text(self, element: WebElement, text: str, clear_first: bool = True) -> bool:
        """Type text into an input element, optionally clearing it first."""
        if clear_first:
            element.clear()
        element.send_keys(text)
        return True

    @step("Type text by locator")
    def type_text_by_locator(
        self,
        by: str,
        value: str,
        text: str,
        clear_first: bool = True,
        timeout: int = DEFAULT_WAIT,
    ) -> bool:
        element = self.wait_for_visible(by, value, timeout)
        self.type_text(element, text, clear_first)
        return True

    # ──────────────────────────────────────────
    # App / keyboard utilities
    # ──────────────────────────────────────────

    @step("Hide keyboard")
    def hide_keyboard(self) -> bool:
        """Dismiss the on-screen keyboard if visible."""
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass  # keyboard may already be hidden
        return True

    @step("Background app")
    def background_app(self, seconds: int = 3) -> bool:
        """Send the app to the background for *seconds* then restore it."""
        self.driver.background_app(seconds)
        return True

    def get_screen_size(self) -> Tuple[int, int]:
        """Return (width, height) in points."""
        size = self.driver.get_window_size()
        return size["width"], size["height"]

    @step("Take screenshot")
    def take_screenshot(self, path: str) -> bool:
        """Save a screenshot to *path* (PNG). Returns False when nothing was written."""
        if not self._save_full_screenshot(path):
            logger.error("take_screenshot FAILED — no image written to %s", path)
            return False
        logger.info("Screenshot saved: %s", path)
        return True

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
        max_attempts: int = 30,
        offset_start: Optional[Tuple[float, float]] = None,
        offset_end: Optional[Tuple[float, float]] = None,
        velocity: int = 100,
    ) -> WebElement:
        """
        Scroll within the element (scroll_by, scroll_value) in *direction*
        until (target_by, target_value) is visible, and **return** it.

        It does not tap: codegen emits ``scroll_until(...)`` followed by a separate
        tap step, so tapping here would fire the gesture twice.  When the target is
        already visible enough it returns on attempt 0 without sending any gesture —
        "no scroll happened" is a normal outcome.

        "Visible enough" means ≥ 50 % of the target inside both the screen *and* the
        scroll container's own rect, measured after the target's rect has settled, so
        a cell still gliding or still clipped by the container edge keeps scrolling.

        offset_start / offset_end: (x_pct, y_pct) fractions of the container
        rect that define the drag gesture.  Generated by the recorder from the
        original gesture; defaults to a 40 % horizontal/vertical swipe.
        """
        last_vis: Optional[float] = None
        for attempt in range(max_attempts):
            if self.is_element_present(target_by, target_value, timeout=2):
                element = self.find_element(target_by, target_value)
                # Settle first: a scroll view keeps gliding after the drag ends, so a
                # rect read right now measures a moving target.  Deciding "visible
                # enough" on it hands the caller an element that has already slid
                # somewhere else by the time it is tapped.
                rect = self._element_settle(element)
                # Clip by the scroll container, not just the screen — the target is
                # only reachable once it has cleared the container's own edge.
                vis = self._visible_fraction(
                    element, rect, clip=self._container_clip(scroll_by, scroll_value)
                )
                if vis >= 0.5:
                    logger.info(
                        "scroll_until: (%s, %r) ready after %d scrolls (%.0f%% visible) — "
                        "returning it, the caller does the tap",
                        target_by, target_value, attempt, vis * 100,
                    )
                    return element
                last_vis = vis
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
        reached = (
            "never found in the hierarchy"
            if last_vis is None
            else f"best visibility reached was {last_vis * 100:.0f}% (need 50% inside "
                 f"container ({scroll_by}, {scroll_value!r}) and the screen)"
        )
        raise NoSuchElementException(
            f"Element ({target_by}, {target_value!r}) not usable after {max_attempts} "
            f"scrolls — {reached}."
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
        press_duration: float = 0.1,
    ) -> bool:
        """
        Briefly press *source*, then drag it onto *target*.
        duration controls the move time; press_duration controls the initial hold.
        """
        (from_x, from_y), (to_x, to_y) = self._points_in_elements(
            [(source, 50.0, 50.0), (target, 50.0, 50.0)]
        )
        self._perform_w3c_drag(from_x, from_y, to_x, to_y, duration, press_duration)
        logger.info("drag_element: source → target")
        return True

    @step("Drag by coordinates")
    def drag_coordinates(
        self,
        from_x: int,
        from_y: int,
        to_x: int,
        to_y: int,
        duration: float = 1.0,
        press_duration: float = 0.1,
    ) -> bool:
        """Briefly press at (from_x, from_y), then drag to (to_x, to_y)."""
        self._perform_w3c_drag(from_x, from_y, to_x, to_y, duration, press_duration)
        logger.info("drag_coordinates: (%d,%d) → (%d,%d)", from_x, from_y, to_x, to_y)
        return True

    @step("Long press and drag element to target")
    def long_press_drag_element(
        self,
        source: WebElement,
        target: WebElement,
        duration: float = 1.0,
        press_duration: float = 1.0,
    ) -> bool:
        """
        Long-press *source* for press_duration seconds, then drag it onto *target*.
        duration controls the move time after the hold.
        """
        (from_x, from_y), (to_x, to_y) = self._points_in_elements(
            [(source, 50.0, 50.0), (target, 50.0, 50.0)]
        )
        self._perform_w3c_drag_with_activation_nudge(
            from_x,
            from_y,
            to_x,
            to_y,
            duration,
            max(1.0, press_duration),
        )
        logger.info("long_press_drag_element: source → target hold=%.2fs", press_duration)
        return True

    @step("Long press and drag by coordinates")
    def long_press_drag_coordinates(
        self,
        from_x: int,
        from_y: int,
        to_x: int,
        to_y: int,
        duration: float = 1.0,
        press_duration: float = 1.0,
        activation_nudge_y: int = 0,
    ) -> bool:
        """Long-press at (from_x, from_y), then drag to (to_x, to_y).

        activation_nudge_y inserts a tiny vertical move before the main drag,
        then returns to the final Y. This helps horizontally scrollable
        timelines recognise the gesture as dragging a clip instead of scrubbing.
        """
        self._perform_w3c_drag_with_activation_nudge(
            from_x,
            from_y,
            to_x,
            to_y,
            duration,
            max(1.0, press_duration),
            activation_nudge_y,
        )
        logger.info(
            "long_press_drag_coordinates: (%d,%d) → (%d,%d) hold=%.2fs nudge_y=%d",
            from_x, from_y, to_x, to_y, press_duration, activation_nudge_y,
        )
        return True

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
        press_duration: float = 0.1,
    ) -> bool:
        """Drag from a % offset within the source element to a % offset within the target element."""
        (from_x, from_y), (to_x, to_y) = self._drag_points(
            from_by, from_value, from_pct_x, from_pct_y,
            to_by, to_value, to_pct_x, to_pct_y,
        )
        self._perform_w3c_drag(from_x, from_y, to_x, to_y, duration, press_duration)
        logger.info(
            "drag_within_elements: %s@(%.1f%%,%.1f%%) → %s@(%.1f%%,%.1f%%)",
            from_value, from_pct_x, from_pct_y, to_value, to_pct_x, to_pct_y,
        )
        return True

    @step("Set slider value")
    def set_slider_value(
        self,
        by: str,
        value: str,
        percent: float,
        timeout: int = DEFAULT_WAIT,
        tolerance: float = 1.0,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
    ) -> bool:
        """Set an ``XCUIElementTypeSlider`` to *percent* (0–100) through XCUITest.

        Exact where a coordinate drag cannot be.  One unit of slider travel is
        often less than a logical point, so a replayed drag lands within ±1 of the
        recorded value at best — and does nothing at all when the press point
        misses the thumb.  ``adjust(toNormalizedSliderPosition:)`` (reached through
        ``send_keys``) sets the position itself, so the outcome does not depend on
        the value the slider happened to hold beforehand.

        *tolerance* absorbs the rounding between the position XCUITest reports and
        the value the app derives from it (a slider reading ``21%`` while its own
        label shows ``20`` is normal).  Raises when the slider will not take the
        value; returns True once it reads back within tolerance.
        """
        el = self.find_element(
            by, value, timeout, container_by, container_value, container_w, container_h
        )
        target = max(0.0, min(100.0, float(percent)))
        reached: Optional[float] = None
        for _ in range(3):
            el.send_keys(f"{target / 100:.4f}")
            frac = self._slider_fraction(el)
            if frac is None:
                logger.warning(
                    "set_slider_value: (%s, %r) publishes no slider value to read back; "
                    "assuming %g%% took", by, value, target,
                )
                return True
            reached = frac * 100
            if abs(reached - target) <= max(0.0, float(tolerance)):
                logger.info("set_slider_value: (%s, %r) → %.0f%%", by, value, reached)
                return True
        raise AssertionError(
            f"set_slider_value failed for ({by}, {value!r}): wanted {target:g}%, "
            f"slider stayed at {reached:g}%"
        )

    @step("Long press and drag within elements by offset percent")
    def long_press_drag_within_elements(
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
        press_duration: float = 1.0,
        activation_nudge_y: int = 0,
    ) -> bool:
        """Long-press at a source % offset, then drag to a target % offset.

        activation_nudge_y inserts a tiny vertical move before the main drag,
        then returns to the final Y. Use a negative value to lift upward.
        """
        (from_x, from_y), (to_x, to_y) = self._drag_points(
            from_by, from_value, from_pct_x, from_pct_y,
            to_by, to_value, to_pct_x, to_pct_y,
        )
        logger.info(
            "long_press_drag_within_elements resolved coords: (%d,%d) → (%d,%d) hold=%.2fs nudge_y=%d",
            from_x, from_y, to_x, to_y, press_duration, activation_nudge_y,
        )
        self._perform_w3c_drag_with_activation_nudge(
            from_x,
            from_y,
            to_x,
            to_y,
            duration,
            max(1.0, press_duration),
            activation_nudge_y,
        )
        logger.info(
            "long_press_drag_within_elements: %s@(%.1f%%,%.1f%%) → %s@(%.1f%%,%.1f%%) hold=%.2fs nudge_y=%d",
            from_value, from_pct_x, from_pct_y, to_value, to_pct_x, to_pct_y, press_duration, activation_nudge_y,
        )
        return True

    @step("Long press and drag from element to coordinates")
    def long_press_drag_from_element_to_coordinates(
        self,
        from_by: str,
        from_value: str,
        from_pct_x: float,
        from_pct_y: float,
        to_x: int,
        to_y: int,
        duration: float = 1.0,
        press_duration: float = 1.0,
        activation_nudge_y: int = 0,
    ) -> bool:
        """Resolve the source element point before starting the long-press drag."""
        src = self.find_element(from_by, from_value)
        from_x, from_y = self._point_in_element(src, from_pct_x, from_pct_y)
        logger.info(
            "long_press_drag_from_element_to_coordinates resolved coords: (%d,%d) → (%d,%d) hold=%.2fs nudge_y=%d",
            from_x, from_y, to_x, to_y, press_duration, activation_nudge_y,
        )
        self._perform_w3c_drag_with_activation_nudge(
            from_x,
            from_y,
            to_x,
            to_y,
            duration,
            max(1.0, press_duration),
            activation_nudge_y,
        )
        logger.info(
            "long_press_drag_from_element_to_coordinates: %s@(%.1f%%,%.1f%%) → (%d,%d) hold=%.2fs nudge_y=%d",
            from_value, from_pct_x, from_pct_y, to_x, to_y, press_duration, activation_nudge_y,
        )
        return True

    @step("Long press and drag from coordinates to element")
    def long_press_drag_from_coordinates_to_element(
        self,
        from_x: int,
        from_y: int,
        to_by: str,
        to_value: str,
        to_pct_x: float,
        to_pct_y: float,
        duration: float = 1.0,
        press_duration: float = 1.0,
        activation_nudge_y: int = 0,
    ) -> bool:
        """Resolve the target element point before starting the long-press drag."""
        tgt = self.find_element(to_by, to_value)
        to_x, to_y = self._point_in_element(tgt, to_pct_x, to_pct_y)
        logger.info(
            "long_press_drag_from_coordinates_to_element resolved coords: (%d,%d) → (%d,%d) hold=%.2fs nudge_y=%d",
            from_x, from_y, to_x, to_y, press_duration, activation_nudge_y,
        )
        self._perform_w3c_drag_with_activation_nudge(
            from_x,
            from_y,
            to_x,
            to_y,
            duration,
            max(1.0, press_duration),
            activation_nudge_y,
        )
        logger.info(
            "long_press_drag_from_coordinates_to_element: (%d,%d) → %s@(%.1f%%,%.1f%%) hold=%.2fs nudge_y=%d",
            from_x, from_y, to_value, to_pct_x, to_pct_y, press_duration, activation_nudge_y,
        )
        return True

    @step("Paint in element")
    def paint_in_element(
        self,
        by: str,
        value: str,
        points_pct: List[Tuple[float, float, int]],
        duration_ms: int = 1000,
        timeout: int = DEFAULT_WAIT,
        container_by: Optional[str] = None,
        container_value: Optional[str] = None,
        container_w: int = 0,
        container_h: int = 0,
    ) -> bool:
        """Replay a recorded paint path inside one element.

        points_pct entries are (x_pct, y_pct, t_ms) captured during recording.
        Replays as one continuous touch sequence (down once, move through all points, up once).

        Returns True once the stroke is replayed; returns False when the recorded
        path is unusable (no points, or fewer than two distinct points), since no
        paint gesture reached the device in that case.
        """
        import time
        if not points_pct:
            logger.warning("paint_in_element: no points provided")
            return False
        # Fast path: try immediate lookup first to reduce pre-stroke latency.
        # Fallback keeps previous behavior when the element is not instantly available.
        try:
            el = self.driver.find_element(by, value)
        except Exception:
            el = self.wait_for_visible(by, value, timeout, container_by, container_value, container_w, container_h)
        rect = el.rect
        ex, ey = rect["x"], rect["y"]
        ew, eh = max(1.0, rect["width"]), max(1.0, rect["height"])
        abs_points: List[Tuple[int, int, int]] = []
        for px, py, t_ms in points_pct:
            ax = round(ex + ew * float(px) / 100.0)
            ay = round(ey + eh * float(py) / 100.0)
            tt = max(0, int(t_ms))
            if abs_points and abs_points[-1][0] == ax and abs_points[-1][1] == ay:
                # Collapse consecutive identical points to shrink action payload,
                # while keeping the latest timestamp for pause duration.
                abs_points[-1] = (ax, ay, tt)
            else:
                abs_points.append((ax, ay, tt))
        if len(abs_points) < 2:
            logger.warning("paint_in_element: insufficient points (%d)", len(abs_points))
            return False

        # Replay optimization: keep recorded points intact, but execute with fewer
        # geometric control points to reduce driver/WDA action overhead.
        def _perp_dist(p: Tuple[int, int, int], a: Tuple[int, int, int], b: Tuple[int, int, int]) -> float:
            ax, ay = a[0], a[1]
            bx, by = b[0], b[1]
            px, py = p[0], p[1]
            dx, dy = bx - ax, by - ay
            if dx == 0 and dy == 0:
                return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
            t = ((px - ax) * dx + (py - ay) * dy) / float(dx * dx + dy * dy)
            proj_x = ax + t * dx
            proj_y = ay + t * dy
            return ((px - proj_x) ** 2 + (py - proj_y) ** 2) ** 0.5

        def _rdp(pts: List[Tuple[int, int, int]], eps: float) -> List[Tuple[int, int, int]]:
            if len(pts) < 3:
                return pts
            first, last = pts[0], pts[-1]
            max_d = -1.0
            max_i = -1
            for i in range(1, len(pts) - 1):
                d = _perp_dist(pts[i], first, last)
                if d > max_d:
                    max_d = d
                    max_i = i
            if max_d > eps and max_i > 0:
                left = _rdp(pts[: max_i + 1], eps)
                right = _rdp(pts[max_i:], eps)
                return left[:-1] + right
            return [first, last]

        replay_points = abs_points
        max_replay_points = 36
        if len(abs_points) > max_replay_points:
            eps = 0.8
            simplified = abs_points
            for _ in range(8):
                candidate = _rdp(abs_points, eps)
                simplified = candidate
                if len(candidate) <= max_replay_points:
                    break
                eps *= 1.5
            if len(simplified) > max_replay_points:
                step = max(1, len(simplified) // (max_replay_points - 1))
                sampled = simplified[::step]
                if sampled[-1] != simplified[-1]:
                    sampled.append(simplified[-1])
                simplified = sampled
            replay_points = simplified
        logger.info("paint_in_element: control points %d -> %d", len(abs_points), len(replay_points))

        seg_count = len(replay_points) - 1
        default_seg = max(16, int(duration_ms / max(1, seg_count)))
        raw_segs: List[int] = []
        prev_t = replay_points[0][2]
        for _, _, t in replay_points[1:]:
            raw_segs.append((t - prev_t) if t > prev_t else default_seg)
            prev_t = max(prev_t, t)


        # Cap replay duration to reduce pre-stroke delay while preserving relative rhythm.
        raw_total = sum(raw_segs)
        target_total = min(max(700, int(duration_ms)), 1800)
        if raw_total > 0:
            scale = target_total / raw_total
            seg_durations_ms = [max(8, int(round(seg * scale))) for seg in raw_segs]
        else:
            seg_durations_ms = [max(8, default_seg)] * seg_count
        touch_steps: list[dict] = [
            {"type": "pointerMove", "duration": 0, "x": replay_points[0][0], "y": replay_points[0][1]},
            {"type": "pointerDown", "button": 0},
        ]
        for (x, y, _), seg_ms in zip(replay_points[1:], seg_durations_ms):
            touch_steps.append({"type": "pointerMove", "duration": max(8, int(seg_ms)), "x": x, "y": y})
        touch_steps.append({"type": "pointerUp", "button": 0})

        payload = [{
            "type": "pointer",
            "id": "paint_finger",
            "parameters": {"pointerType": "touch"},
            "actions": touch_steps,
        }]

        try:
            # Send one continuous W3C action chain so the stroke is not split into small drags.
            self.driver.execute("actions", {"actions": payload})
            logger.info("paint_in_element: replayed %d points on %s (continuous)", len(abs_points), value)
        except Exception as exc:
            # Fallback for drivers that don't accept raw W3C payload via execute().
            logger.warning("paint_in_element: continuous action failed (%s), fallback to segmented drags", exc)
            prev_x, prev_y, prev_t2 = replay_points[0]
            for (x, y, t), seg_ms in zip(replay_points[1:], seg_durations_ms):
                seg_duration = max(0.08, min(1.6, seg_ms / 1000.0))
                self.driver.execute_script(
                    "mobile: dragFromToForDuration",
                    {
                        "fromX": prev_x,
                        "fromY": prev_y,
                        "toX": x,
                        "toY": y,
                        "duration": seg_duration,
                    },
                )
                prev_x, prev_y, prev_t2 = x, y, max(prev_t2, t)
            logger.info("paint_in_element: replayed %d points on %s (fallback)", len(abs_points), value)
        finally:
            try:
                self.driver.release_actions()
            except Exception:
                pass
        logger.info(f'execute action done: time.time()={time.time()}')
        return True

    # ──────────────────────────────────────────
    # Pinch & Rotate
    # ──────────────────────────────────────────

    @step("Pinch")
    def pinch(
        self,
        element: WebElement,
        scale: float = 0.5,
        velocity: float = -1.0,
    ) -> bool:
        """
        Pinch gesture on *element* via XCUITest mobile: pinch.
        scale   < 1.0  →  pinch in  (zoom out).
        scale   > 1.0  →  pinch out (zoom in).
        velocity: pinch speed in scale-factor/sec; -1.0 = XCUITest default.
        """
        rect = element.rect
        width = max(1, int(rect.get("width", 0) or 0))
        height = max(1, int(rect.get("height", 0) or 0))
        center_x = int(rect.get("x", 0)) + width // 2
        center_y = int(rect.get("y", 0)) + height // 2

        # XCUITest requires velocity sign to match pinch direction:
        # scale < 1 => velocity < 0, scale > 1 => velocity > 0.
        requested_speed = abs(float(velocity)) if velocity not in (0, None) else 1.8
        if abs(scale - 1.0) >= 0.3:
            requested_speed = max(1.8, requested_speed)
        if scale < 1.0:
            effective_velocity = -requested_speed
        elif scale > 1.0:
            effective_velocity = requested_speed
        else:
            effective_velocity = requested_speed

        # Timeline-style custom views often need focus before pinch is recognised.
        try:
            self.driver.execute_script("mobile: tap", {"x": center_x, "y": center_y})
        except Exception:
            pass

        params: dict = {"element": element.id, "scale": scale, "velocity": effective_velocity}
        self.driver.execute_script("mobile: pinch", params)

        try:
            name_hint = (element.get_attribute("name") or "").lower()
        except Exception:
            name_hint = ""
        if any(token in name_hint for token in ("timeline", "track", "mastertrack", "piptrack")):
            retry_speed = max(2.4, abs(effective_velocity))
            retry_velocity = -retry_speed if scale < 1.0 else retry_speed
            if abs(retry_velocity) > abs(effective_velocity):
                self.driver.execute_script("mobile: pinch", {"element": element.id, "scale": scale, "velocity": retry_velocity})
                logger.info(
                    "pinch(mobile): timeline retry scale=%.2f vel=%.2f->%.2f center=(%d,%d)",
                    scale,
                    effective_velocity,
                    retry_velocity,
                    center_x,
                    center_y,
                )
                return True

        logger.info(
            "pinch(mobile): scale=%.2f vel=%.2f center=(%d,%d) size=%dx%d",
            scale,
            effective_velocity,
            center_x,
            center_y,
            width,
            height,
        )
        return True

    @step("Rotate")
    def rotate(
        self,
        element: WebElement,
        rotation: float = 90.0,
        velocity: float = 1.5,
    ) -> bool:
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
        return True

    # ──────────────────────────────────────────
    # System operations
    # ──────────────────────────────────────────

    @step("Press Home button")
    def press_home(self) -> bool:
        """Press the physical Home button (sends the app to the background)."""
        self.driver.execute_script("mobile: pressButton", {"name": "home"})
        logger.info("press_home")
        return True

    @step("Launch app")
    def launch_app(self, bundle_id: str) -> bool:
        """
        Launch *bundle_id*.
        - Already running → brought to foreground.
        - Terminated       → cold-started.
        """
        self.driver.execute_script("mobile: launchApp", {"bundleId": bundle_id})
        logger.info("launch_app: %s", bundle_id)
        return True

    @step("Activate app")
    def activate_app(self, bundle_id: str) -> bool:
        """Bring *bundle_id* to the foreground without cold-launching it."""
        self.driver.execute_script("mobile: activateApp", {"bundleId": bundle_id})
        logger.info("activate_app: %s", bundle_id)
        return True

    @step("Terminate app")
    def terminate_app(self, bundle_id: str) -> bool:
        """Force-quit *bundle_id*. No-op if the app is not running."""
        self.driver.execute_script("mobile: terminateApp", {"bundleId": bundle_id})
        logger.info("terminate_app: %s", bundle_id)
        return True

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

    @step("Wait until element is no longer shown")
    def wait_until_not_show(
        self,
        by: str,
        value: str,
        appear_timeout: float = DEFAULT_NOT_SHOW_APPEAR_TIMEOUT,
        disappear_timeout: float = DEFAULT_NOT_SHOW_DISAPPEAR_TIMEOUT,
        poll_interval: float = DEFAULT_NOT_SHOW_POLL_INTERVAL,
        allow_already_gone: bool = False,
        msg: str = "",
    ) -> bool:
        """
        Wait for a transient element (progress bar, rendering spinner, toast) to
        appear and then go away again.

        The two budgets are counted **separately**:

        1. *appear_timeout* — the element must show up within this window.  When
           it never appears this returns ``False`` immediately rather than
           sitting out the long budget, unless *allow_already_gone* is explicitly
           set for a short-lived indicator whose completed state is already
           visible before the first lookup.
        2. *disappear_timeout* — once seen, the element gets this much time to
           disappear.  ``True`` as soon as it is gone, ``False`` when it is still
           on screen after the budget runs out.

        Never raises: both outcomes are reported through the return value, so the
        generated ``assert actions.wait_until_not_show(...)`` is what fails the
        step — with the label of the element that misbehaved.
        """
        label = msg or f"({by}, {value!r})"

        # Phase 1 — did it ever show up?  Own budget, own verdict.
        if not self.is_element_present(by, value, timeout=appear_timeout):
            if allow_already_gone:
                logger.info(
                    "wait_until_not_show: %s was already gone within %ss",
                    label, appear_timeout,
                )
                return True
            logger.warning(
                "wait_until_not_show: %s never appeared within %ss — nothing to wait for",
                label, appear_timeout,
            )
            return False
        logger.info("wait_until_not_show: %s appeared; waiting up to %ss for it to go away",
                    label, disappear_timeout)

        # Phase 2 — fresh budget for the work behind the element to finish.
        deadline = time.monotonic() + disappear_timeout
        while time.monotonic() < deadline:
            if not self.is_element_present(by, value, timeout=1):
                logger.info("wait_until_not_show: %s is gone", label)
                return True
            time.sleep(poll_interval)
        logger.error(
            "wait_until_not_show: %s is still shown after %ss", label, disappear_timeout
        )
        return False

    _TEXT_INPUT_TAGS = (
        "XCUIElementTypeTextField",
        "XCUIElementTypeTextView",
        "XCUIElementTypeSecureTextField",
    )

    @step("Verify element text")
    def verify_text(
        self,
        by: str,
        value: str,
        expected: str,
        timeout: int = 5,
        tolerance: Optional[float] = None,
    ) -> bool:
        """
        Assert that the element's text / label equals *expected*.
        Raises AssertionError with a clear diff message on mismatch.

        *tolerance* switches the comparison to a numeric one that accepts a
        difference of up to that many units — for readouts driven by a replayed
        coordinate gesture, where the exact digit is not reproducible (see
        ``config.TEXT_NUMERIC_TOLERANCE``).  ``None`` looks the element id up in
        ``self.text_numeric_tolerance`` and falls back to an exact string compare.
        Non-numeric text is always compared exactly, whatever the tolerance.
        """
        element = self.wait_for_visible(by, value, timeout)
        # Mirror recording: try value (typed content) then label.
        actual = element.get_attribute("value") or element.text or ""
        # Mirror recording: only search relatives when BOTH value and label are empty.
        if not actual:
            # Fallback 1: element is a child inside a text input — walk ancestors.
            for tag in self._TEXT_INPUT_TAGS:
                try:
                    anc = element.find_element(AppiumBy.XPATH, f"ancestor::{tag}[1]")
                    actual = anc.get_attribute("value") or ""
                    if actual:
                        break
                except Exception:
                    continue
        if not actual:
            # Fallback 2: element wraps a text input — search descendants.
            for tag in self._TEXT_INPUT_TAGS:
                for desc in element.find_elements(AppiumBy.CLASS_NAME, tag):
                    actual = desc.get_attribute("value") or ""
                    if actual:
                        break
                if actual:
                    break
        # name is the last resort — only reached when no text content was found anywhere.
        if not actual:
            actual = element.get_attribute("name") or ""
        allowed = self._text_tolerance(value) if tolerance is None else float(tolerance)
        if allowed > 0:
            actual_n, expected_n = _as_number(actual), _as_number(expected)
            if actual_n is not None and expected_n is not None:
                assert abs(actual_n - expected_n) <= allowed, (
                    f"verify_text FAILED for ({by}, {value!r})\n"
                    f"  expected : {expected!r} (±{allowed:g})\n"
                    f"  actual   : {actual!r}"
                )
                logger.info(
                    "verify_text PASSED for (%s, %r): %r vs expected %r (±%g)",
                    by, value, actual, expected, allowed,
                )
                return True
        assert actual == expected, (
            f"verify_text FAILED for ({by}, {value!r})\n"
            f"  expected : {expected!r}\n"
            f"  actual   : {actual!r}"
        )
        logger.info("verify_text PASSED for (%s, %r)", by, value)
        return True

    def _text_tolerance(self, value: str) -> float:
        """Configured numeric tolerance for the element id *value* (0 = exact)."""
        table = getattr(self, "text_numeric_tolerance", None) or {}
        try:
            return float(table.get(value, 0) or 0)
        except (TypeError, ValueError):
            return 0.0

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

    @staticmethod
    def _parse_preview_phase(phase: str) -> tuple[str, str]:
        """Split a preview *phase* into ``(kind, pair_suffix)``.

        ``"before"`` / ``"after"`` are the plain forms and yield an empty suffix.
        A phase may carry a free suffix after a separator
        (``"before_min_ic_jaw"`` → ``("before", "min_ic_jaw")``) so that a single
        capture *name* can hold several before/after pairs at the same time —
        the suffix is what pairs the two halves and it also lands in the filename.

        Raises ``ValueError`` for anything that is neither a before nor an after
        capture; a mislabelled phase used to be silently treated as "after" and
        surfaced much later as a missing-file comparison failure.
        """
        raw = (phase or "").strip()
        low = raw.lower()
        for kind in ("before", "after"):
            if low == kind:
                return kind, ""
            if low.startswith(kind) and len(low) > len(kind) and not low[len(kind)].isalnum():
                return kind, raw[len(kind) + 1:]
        raise ValueError(
            "capture_for_preview: phase must be 'before'/'after', optionally with a "
            f"pair suffix such as 'before_min_ic_jaw' — got {phase!r}"
        )

    @staticmethod
    def _preview_label(name: str, pair_suffix: str) -> str:
        """Reporting label for one before/after pair."""
        return f"{name}:{pair_suffix}" if pair_suffix else name

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
        key = (name, "")
        pending = self._preview_pending.pop(key, None)
        meta = self._preview_pending_meta.pop(key, (None, None))
        if not pending:
            logger.error(
                "No pending 'before' capture for %r — the hold flow needs a "
                "capture_for_preview(%r, 'before', ...) first", name, name,
            )
            return False
        ts, before_path = pending
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

    def _settle_hierarchy(self) -> None:
        """Block until the UI hierarchy stops changing, so that a capture taken
        immediately afterwards lands on a settled screen.  No-op unless the
        instance has ``stability_check = True`` (same tunables as the
        ``wait_for_stable_hierarchy`` decorator)."""
        if not getattr(self, "stability_check", False):
            return
        interval = getattr(self, "stability_interval", 0.4)
        timeout = getattr(self, "stability_timeout", 120.0)
        min_wait = getattr(self, "stability_min_wait", 0.8)
        required = max(1, int(getattr(self, "stability_required_samples", 3)))
        if min_wait > 0:
            time.sleep(min_wait)
        last, stable, start = None, 0, time.time()
        while time.time() - start < timeout:
            try:
                sig = self._hierarchy_stability_signature(self.driver.page_source)
            except Exception:
                return
            if sig == last:
                stable += 1
                if stable >= required:
                    return
            else:
                stable, last = 1, sig
            time.sleep(interval)

    @staticmethod
    def _screenshot_written(path: str) -> bool:
        """True when *path* exists and holds a non-empty image."""
        try:
            return os.path.getsize(path) > 0
        except OSError:
            return False

    def _save_full_screenshot(self, path: str) -> bool:
        """Full-screen screenshot to *path*; never raises — callers check the file."""
        try:
            self.driver.save_screenshot(path)
        except Exception as exc:
            logger.warning("save_screenshot failed for %s: %s", path, exc)
        return self._screenshot_written(path)

    @step("Capture screenshot for GT comparison")
    def capture_for_gt(
        self,
        name: str,
        by: Optional[str] = None,
        value: Optional[str] = None,
        compare_folder: str = "pytest/screenshots/compare",
        threshold: Optional[float] = None,
        crop_rect: Optional[Tuple[int, int, int, int]] = None,
    ) -> Union[str, bool]:
        """
        Capture the target and save it to *compare_folder* as
        ``{name}_{ts}_compare.png`` (timestamp added to prevent overwrite).

        Capture target precedence:
          1. *crop_rect* ``(x1, y1, x2, y2)`` in **points** — crop a fixed pixel
             region of the full screen (legacy ``snapshot(crop=(...))`` parity;
             scaled point→pixel via ``_save_image_crop_by_rect``).
          2. *by* / *value* — crop to that element's bounding box.
          3. neither — full screen.

        The name is queued for GT comparison; call ``run_screenshot_comparisons()``
        at the end of the test to evaluate all queued items.

        *threshold*: per-image SSIM threshold (0–1).  When ``None``, the global
        threshold passed to ``run_screenshot_comparisons()`` is used instead.

        Returns the saved path (truthy) on success, or ``False`` when no image
        could be written — in which case nothing is queued, because a queued path
        to a missing file only turns into a confusing failure later.  The path is
        returned rather than ``True`` because callers feed it straight into
        ``compare_with_gt(compare_path=...)`` / ``compare_preview(before_path=...)``.
        """
        self._settle_hierarchy()   # wait for a stable screen before capturing
        os.makedirs(compare_folder, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(compare_folder, f"{name}_{ts}_compare.png")
        if crop_rect is not None:
            x1, y1, x2, y2 = crop_rect
            rect_pts = {"x": x1, "y": y1, "width": x2 - x1, "height": y2 - y1}
            screen_pts = self.driver.get_window_size()
            png = self._fetch_wda_screenshot_png()
            if not (png and self._save_image_crop_by_rect(png, path, rect_pts, screen_pts)):
                logger.warning("crop_rect capture failed for %s; falling back to full-screen", name)
                self._save_full_screenshot(path)
        elif by and value:
            try:
                el = self.find_element(by, value)
                el.screenshot(path)
            except Exception as exc:
                logger.warning("Element screenshot failed (%s); falling back to full-screen", exc)
                self._save_full_screenshot(path)
        else:
            self._save_full_screenshot(path)
        if not self._screenshot_written(path):
            logger.error(
                "capture_for_gt FAILED for '%s' — no image written to %s; "
                "skipping GT comparison for this capture", name, path,
            )
            return False
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
        When the phase is an "after" capture, the pair is queued for comparison;
        call ``run_screenshot_comparisons()`` at the end of the test to evaluate.

        *phase* is ``"before"`` / ``"after"``, optionally followed by a pair
        suffix (``"before_min_ic_jaw"`` / ``"after_min_ic_jaw"``).  The suffix
        pairs the two halves, so one *name* can hold several pairs at once —
        typically inside a loop over elements — and it keeps every filename
        distinct.  A phase that is neither before nor after raises ``ValueError``.

        *threshold*: per-image SSIM threshold (0–1).  When ``None``, the global
        threshold passed to ``run_screenshot_comparisons()`` is used instead.

        *expected_result*: ``"same"`` (default) — similarity ≥ threshold to PASS.
                           ``"different"`` — similarity < threshold to PASS
                           (i.e. the action was expected to visually change the screen).
        Only meaningful on the "after" capture.
        """
        os.makedirs(compare_folder, exist_ok=True)
        kind, pair_suffix = self._parse_preview_phase(phase)
        key = (name, pair_suffix)
        label = self._preview_label(name, pair_suffix)
        file_phase = f"{kind}_{pair_suffix}" if pair_suffix else kind
        if kind == "before":
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(compare_folder, f"{name}_{ts}_{file_phase}.png")
            rect_pts, screen_pts = self._resolve_capture_rect(by, value)
            if not self._save_preview_image(path, rect_pts, screen_pts, by, value):
                raise AssertionError(f"Failed to capture before screenshot: {label}")
            self._preview_pending[key] = (ts, path)
            self._preview_pending_meta[key] = (rect_pts, screen_pts)
            logger.info("Captured before screenshot for preview: %s", path)
        else:
            self._settle_hierarchy()
            pending = self._preview_pending.pop(key, None)
            meta = self._preview_pending_meta.pop(key, (None, None))
            if not pending:
                # Queueing a made-up before path here only turns into an opaque
                # "file missing" failure inside run_screenshot_comparisons().
                raise AssertionError(
                    f"capture_for_preview: no pending 'before' capture for '{label}' "
                    f"(phase={phase!r}) — every after capture needs a matching before "
                    f"capture with the same name and pair suffix"
                )
            ts, before_path = pending
            path = os.path.join(compare_folder, f"{name}_{ts}_{file_phase}.png")
            rect_pts, screen_pts = meta
            if rect_pts is None or screen_pts is None:
                rect_pts, screen_pts = self._resolve_capture_rect(by, value)
            if not self._save_preview_image(path, rect_pts, screen_pts, by, value):
                raise AssertionError(f"Failed to capture after screenshot: {label}")
            self._preview_compare_queue.append((label, before_path, path, threshold, expected_result))
            logger.info(
                "Captured after screenshot for preview: %s (threshold=%s, expected=%s)",
                path, threshold, expected_result,
            )
        return path

    @step("Tap element and capture before/after preview")
    def tap_then_capture_preview(
        self,
        capture_by: str,
        capture_value: str,
        tap_by: str,
        tap_value: str,
        wait_seconds: float = 2.0,
        capture_name: str = "tap_screenshot_diff",
        expected_result: str = "same",
        threshold: Optional[float] = None,
        timeout: int = DEFAULT_WAIT,
    ) -> bool:
        """Capture target before/after a tap action without hierarchy-stability waits."""
        self.capture_for_preview(capture_name, "before", capture_by, capture_value)
        tap_el = self.wait_for_visible(tap_by, tap_value, timeout)
        tx, ty = self._point_in_element(tap_el)
        self.driver.execute_script("mobile: tap", {"x": int(tx), "y": int(ty)})
        if wait_seconds > 0:
            time.sleep(float(wait_seconds))
        self.capture_for_preview(
            capture_name,
            "after",
            capture_by,
            capture_value,
            threshold=threshold,
            expected_result=expected_result,
        )
        logger.info(
            "tap_then_capture_preview: tap=(%d,%d) wait=%.2fs capture=%s expected=%s",
            int(tx),
            int(ty),
            float(wait_seconds),
            capture_name,
            expected_result,
        )
        return True

    @step("Tap within element and capture before/after preview")
    def tap_within_element_then_capture_preview(
        self,
        capture_by: str,
        capture_value: str,
        tap_by: str,
        tap_value: str,
        tap_pct_x: float,
        tap_pct_y: float,
        wait_seconds: float = 2.0,
        capture_name: str = "tap_screenshot_diff",
        expected_result: str = "same",
        threshold: Optional[float] = None,
        timeout: int = DEFAULT_WAIT,
    ) -> bool:
        """Capture target before/after a %offset tap action without hierarchy-stability waits."""
        self.capture_for_preview(capture_name, "before", capture_by, capture_value)
        tap_el = self.wait_for_visible(tap_by, tap_value, timeout)
        tx, ty = self._coord_at_pct(tap_el, tap_pct_x, tap_pct_y)
        self.driver.execute_script("mobile: tap", {"x": int(tx), "y": int(ty)})
        if wait_seconds > 0:
            time.sleep(float(wait_seconds))
        self.capture_for_preview(
            capture_name,
            "after",
            capture_by,
            capture_value,
            threshold=threshold,
            expected_result=expected_result,
        )
        logger.info(
            "tap_within_element_then_capture_preview: tap=(%d,%d) wait=%.2fs capture=%s expected=%s",
            int(tx),
            int(ty),
            float(wait_seconds),
            capture_name,
            expected_result,
        )
        return True

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
        if not compare_path:
            queued_paths = [
                path for queued_name, path, _ in self._gt_compare_queue
                if queued_name == name and path
            ]
            if queued_paths:
                compare_path = queued_paths[-1]

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
    ) -> bool:
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
        return True
