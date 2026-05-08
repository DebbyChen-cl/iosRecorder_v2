# Recorder — Select Element Rules

You are working on the **element selector and hit-test logic** (`app/selector.py`, `app/hittest.py`).

Read these files before making changes:
- [app/selector.py](../../../app/selector.py)
- [app/hittest.py](../../../app/hittest.py)

---

## Selector Strategy (`app/selector.py`)

`build_selector(el: ET.Element) -> Tuple[str, str]` returns `(selector_type, selector_value)`.

### Priority Order — Never Change This

1. **`"accessibility id"`** — from `el.attrib["name"]`
   - Skip if value starts with `"0x"` (memory pointer, not a real ID)
   - This is the most stable selector across app versions
2. **`"name"`** — from `el.attrib["label"]`
   - Human-readable label set by the app
3. **`"xpath"` with `@value`** — from `el.attrib["value"]`
   - Only valid for these input types: `XCUIElementTypeTextField`, `XCUIElementTypeSecureTextField`, `XCUIElementTypeStaticText`
   - Format: `//{tag}[@value="{escaped_value}"]`
   - Use `_esc()` to escape double-quotes in the value
4. **`"xpath"` fallback** — `//{tag}`
   - Last resort; matches all elements of that XCUIElement type

### Adding a New Selector Type

1. Insert the new check **above** the xpath fallback (step 4)
2. Add a new entry to `_BY_MAP` in `app/codegen.py` so the generated code uses the right `AppiumBy.*` constant
3. Never use attribute values that could be `None` without `.strip()` and a truthiness check

## Hit-Test Strategy (`app/hittest.py`)

`hit_test(x, y, root: dict) -> dict | None` returns the single best element at screen coordinate `(x, y)`.

`find_scroll_container(x, y, root)` returns the **innermost scrollable element** that contains `(x, y)` — used during scroll recording to identify which view to scroll within. Detection order: (1) standard scrollable tags — `XCUIElementTypeScrollView`, `XCUIElementTypeCollectionView`, `XCUIElementTypeTable`, `XCUIElementTypeWebView`, `XCUIElementTypeTextView`; (2) fallback: any element with `scrollable="true"` attribute (WDA exposes this for non-standard scroll views such as `XCUIElementTypeOther` wrappers). Returns `None` if no scrollable container found at the coordinate.

`build_scroll_container_selector(el, root)` builds the most specific selector for a scroll container. Returns `accessibility id` or `name` when available; otherwise generates a **structural xpath** anchored on the deepest named ancestor — e.g. `//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/...`. Used in `main.py::_record_scroll` instead of the plain `build_selector` to handle containers that lack accessibility IDs.

### How Scoring Works (`_score()`)

Lower score = better match. The scorer prefers:
1. Elements that are **interactive** (buttons, links, text fields)
2. **Smallest bounding area** (most specific element)
3. Elements that **have an accessibility ID** (more stable)

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
