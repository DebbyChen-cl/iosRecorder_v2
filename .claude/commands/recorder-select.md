# Recorder — Select Element Rules

You are working on the **element selector and hit-test logic** (`app/selector.py`, `app/hittest.py`).

Read these files before making changes:
- [app/selector.py](../../../app/selector.py)
- [app/hittest.py](../../../app/hittest.py)

---

## Selector Strategy (`app/selector.py`)

`build_selector(el: ET.Element) -> Tuple[str, str]` returns `(selector_type, selector_value)`.

`get_selector_quality(el: ET.Element) -> str` classifies the element's selector stability for UI color coding and the HTML export report. Returns one of:
- `"id"` — has a proper accessibility id that differs from the label (most stable)
- `"id_indexed"` — accessibility id ends with `-<digits>` (e.g. `Cell-3`) — index may shift (yellow)
- `"id_eq_label"` — accessibility id exists but equals the label (may be fragile) (blue)
- `"label_only"` — no stable id; matched by label attribute only (orange)
- `"xpath_only"` — no id or label; xpath fallback (most fragile) (red)

This value is stored as `selector_quality` in every target dict built by `_build_target()` or any inline target construction in `app/main.py`.

### Priority Order — Never Change This

Default mode only (`RECORDER_XPATH_ONLY!=1`).

1. **`"accessibility id"`** — from `el.attrib["name"]`
   - Skip if value starts with `"0x"` (memory pointer, not a real ID)
   - Skip if value starts with `"/"` (file/bundle path — contains app UUID, changes on reinstall)
   - This is the most stable selector across app versions
2. **`"name"`** — from `el.attrib["label"]`
   - Human-readable label set by the app
3. **`"xpath"` fallback** — `//{tag}`
   - Last resort; matches all elements of that XCUIElement type

### XPath-Only Runtime Mode

When `RECORDER_XPATH_ONLY=1` (enabled by `bash start.sh --xpath`):
- `build_selector()` always returns `("xpath", <xpath_value>)`
- hit-test element selection/scoring does not change
- `build_scroll_container_selector()` also always returns xpath (structural xpath first, then `build_xpath()` fallback)

### Adding a New Selector Type

1. Insert the new check **above** the xpath fallback (step 4)
2. Add a new entry to `_BY_MAP` in `app/codegen.py` so the generated code uses the right `AppiumBy.*` constant
3. Never use attribute values that could be `None` without `.strip()` and a truthiness check

## Hit-Test Strategy (`app/hittest.py`)

`hit_test(x, y, root: dict) -> dict | None` returns the single best element at screen coordinate `(x, y)`. Used for taps and most gestures.

`hit_test_for_swipe(x, y, root)` returns the best **swipe container** at `(x, y)`. Uses a different scorer than `hit_test`: interactive elements first → penalise `GENERIC_CONTAINER_TAGS` (`XCUIElementTypeOther`, `XCUIElementTypeApplication`, `XCUIElementTypeWindow`, `XCUIElementTypeView`) → smallest area. This avoids selecting a nameless canvas leaf or a root application wrapper when the real target is a specific element like `XCUIElementTypeImage`. Used in `main.py::_record_move` when `action == "swipe"`.

`find_scroll_container(x, y, root)` returns the **innermost scrollable element** that contains `(x, y)` — used during scroll recording to identify which view to scroll within. Detection order: (1) standard scrollable tags — `XCUIElementTypeScrollView`, `XCUIElementTypeCollectionView`, `XCUIElementTypeTable`, `XCUIElementTypeWebView`, `XCUIElementTypeTextView`; (2) fallback: any element with `scrollable="true"` attribute (WDA exposes this for non-standard scroll views such as `XCUIElementTypeOther` wrappers). Returns `None` if no scrollable container found at the coordinate.

`build_scroll_container_selector(el, root)` builds the most specific selector for a scroll container. In default mode, returns `accessibility id` or `name` when available; otherwise generates a **structural xpath** anchored on the deepest named ancestor — e.g. `//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/...`. In xpath-only mode, it always returns xpath. Used in `main.py::_record_scroll` instead of the plain `build_selector` to handle containers that lack accessibility IDs.

### How Scoring Works

**`_score()`** — used by `hit_test` (taps). Lower score = better. Tuple `(is_container, -has_stable_id, -is_interactive, area, -has_id, has_children)`. Prefers:
1. **Non-container** — `TAP_CONTAINER_TAGS` (`XCUIElementTypeCollectionView`, `ScrollView`, `Table`, `WebView`, `TextView`, `Application`, `Window`) are sorted last
2. **Stable-ID leaf** — `get_selector_quality()` returns `"id"` or `"id_eq_label"` **and** element has no children; containers with stable names (e.g. ViewController root views) do NOT get this bonus
3. **Interactive** (buttons, links, text fields) — tiebreaker within same ID quality
4. **Smallest bounding area** (most specific element)
5. **Has any identifier** — over pure xpath fallback
6. **Leaf node** preferred over elements with children

Note: `XCUIElementTypeCell` is NOT in `INTERACTIVE_TAGS` — cells are containers, not leaf interactive elements.

**`_swipe_score()`** — used by `hit_test_for_swipe`. Prefers:
1. **Interactive** elements
2. **Non-generic tag** — penalises `GENERIC_CONTAINER_TAGS` (`XCUIElementTypeOther` etc.)
3. **Smallest area** among remaining candidates

### `_collect(x, y, el)`

Recursively finds ALL elements whose bounding rect contains `(x, y)`. Returns a flat list. `hit_test` then picks the highest-scored element from this list. `find_scroll_container` filters this list for scrollable types and picks the one with the smallest area (innermost).

### `serialize(root)`

Converts the full iOS UI element tree to a JSON-friendly list of dicts for the frontend UI tree panel. Includes: `tag`, `name`, `label`, `value`, `rect` (x, y, width, height), `children`.

### Coordinates

All coordinates are in **logical points** (not pixels). The WDA screen stream and element rects use the same point-space.

### Pre-gesture Snapshot (Recording Pipeline Rule)

`hit_test` must always run against the **pre-gesture** UI tree, not the post-gesture state.

In `app/main.py`, the WebSocket handler captures `snapshot = _cache.get("root")` **before** firing the WDA gesture task, then passes it to `_record_point` / `_record_long_press` / etc. The recording helpers accept an optional `snapshot` parameter and skip any network fetch when it is provided.

**Why this matters:** If a tap causes immediate navigation (e.g. tapping a back button exits a modal in < 100 ms), a delayed `_cached_tree()` call would fetch the *new* screen's element tree. The element that was tapped no longer exists on the new screen, so `hit_test` returns the wrong element. Using the pre-gesture snapshot guarantees the correct element is recorded every time.

### Never Do

- Never call `_cached_tree()` (with or without `force=True`) inside a recording helper when a pre-gesture snapshot is available — always prefer the snapshot
- Never return an element with `type == "coordinate"` from `hit_test` — that is a sentinel type used by `codegen.py` to indicate no element was matched
- Never mutate the element tree during traversal
- Never assume an element attribute exists — always use `.attrib.get(..., "")`
