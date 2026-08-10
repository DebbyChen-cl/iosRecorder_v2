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

`find_scroll_container(x, y, root, target=None)` returns the scrollable container an action should be scoped to. Two modes:

- **Ancestor mode** (`target` given — element actions such as tap / long press): walks the **target's ancestor chain** and returns the innermost scrollable ancestor. Detection order within the chain: (1) standard scrollable tags — `XCUIElementTypeScrollView`, `XCUIElementTypeCollectionView`, `XCUIElementTypeTable`, `XCUIElementTypeWebView`, `XCUIElementTypeTextView`; (2) fallback: any ancestor with `scrollable="true"` (WDA exposes this for non-standard scroll views such as `XCUIElementTypeOther` wrappers). The target itself is excluded (`path[:-1]`). Returns `None` when no scrollable ancestor exists.
- **Coordinate mode** (`target` omitted — scroll gestures, which act on the view under the finger): same two-step detection over every element at `(x, y)`, picking the smallest-area (innermost) match. Returns `None` if none found.

**Never resolve an element action's container by coordinate.** Overlapping a scroll view's rect does not mean the element lives inside it — a button floating above a ScrollView, or a category strip driving a separate list, both overlap containers they are not part of. Attaching such a container makes the exported test scroll the wrong view, and `_find_with_scroll()` can never find the element (`NoSuchElementException: not found after 20 scrolls`).

`should_attach_scroll_container(target, container, root)` is the final guard: the container must be a true ancestor of the target. Ancestor mode already guarantees this; the check exists for any caller still resolving a container by coordinate.

`build_scroll_container_selector(el, root)` builds the most specific selector for a scroll container. In default mode, returns `accessibility id` or `name` when available; otherwise generates a **structural xpath** anchored on the deepest named ancestor — e.g. `//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/...`. In xpath-only mode, it always returns xpath. Used in `main.py::_record_scroll` instead of the plain `build_selector` to handle containers that lack accessibility IDs.

### How Scoring Works

**`_score()`** — used by `hit_test` (taps). Lower score = better. Tuple `(is_container, not_visible, is_generic_wrapper, -has_stable_id, -is_interactive, is_slop_hit, area, not_really_visible, -has_id, has_children)`. Prefers:
1. **Non-container** — `TAP_CONTAINER_TAGS` (`XCUIElementTypeCollectionView`, `ScrollView`, `Table`, `WebView`, `TextView`, `Application`, `Window`) are sorted last
2. **Visible** — elements with `visible="false"` are penalized; prevents invisible overlays (e.g. hidden subscription dialogs) from winning over visible content due to smaller area. Exception: candidates returned by `_visibility_exemptions()` are scored as visible — see **Occlusion exemption** below
3. **Non-generic wrapper** — interactive elements preferred over `XCUIElementTypeOther` / `XCUIElementTypeView`
4. **Stable-ID leaf** — `get_selector_quality()` returns `"id"` or `"id_eq_label"` **and** element has no children; containers with stable names (e.g. ViewController root views) do NOT get this bonus
5. **Interactive** (buttons, links, text fields) — tiebreaker within same ID quality
6. **Exact rect hit** over a `HIT_SLOP`-only hit — see **Thin-element hit slop** below
7. **Smallest bounding area** (most specific element)
8. **Genuinely visible** over occlusion-exempt — breaks the tie when an exempted element and the overlay covering it share the *same rect* (e.g. a not-yet-loaded `thumbnailImageView` stacked exactly under the "Processing..." `processingLabel`); ranked after `area` so the ordinary occlusion cases, where the exempt element is the smaller one, are unaffected
9. **Has any identifier** — over pure xpath fallback
10. **Leaf node** preferred over elements with children

Note: `XCUIElementTypeCell` is NOT in `INTERACTIVE_TAGS` — cells are containers, not leaf interactive elements.

### Occlusion exemption (`_visibility_exemptions` / `_is_occluded_not_hidden`)

WDA derives `visible` from an accessibility hit-test, not from what is rendered: an element drawn on screen still reports `visible="false"` whenever another accessibility element sits on top of it. `hit_test`, `hit_test_excluding` and `hit_test_drop_target` therefore call `_visibility_exemptions(candidates, root)` before scoring and pass the result into `_score`, which treats those elements as visible (including for the `has_stable_id` bonus).

A hidden candidate is exempted only when some **later sibling** on its ancestor chain (later = drawn above) is simultaneously `visible="true"`, `accessible="true"`, a **leaf**, and fully covers the candidate's rect. The leaf requirement is the discriminator: a subtree that was genuinely dismissed or replaced is covered by a structural container *with children* (or by nothing at all), never by a bare accessible leaf. This is what keeps a replaced nav bar and Canva's dismissed subscription dialog penalized while letting a wait/progress view underneath a full-size `XCUIElementTypeImage` win. The parent map is built at most once per hit-test, and only when a candidate is actually invisible.

**`_swipe_score()`** — used by `hit_test_for_swipe`. Prefers:
1. **Interactive** elements
2. **Non-generic tag** — penalises `GENERIC_CONTAINER_TAGS` (`XCUIElementTypeOther` etc.)
3. **Exact rect hit** over a `HIT_SLOP`-only hit
4. **Smallest area** among remaining candidates

### Thin-element hit slop (`HIT_SLOP` / `_hit_rect` / `_collect_hits`)

Separator lines, compare bars and slider tracks are routinely 1 pt on one axis — e.g. `barImageView` at `302x1`. A strict rect test only accepts `454 <= y <= 455`, which a pointer coordinate that went through display scaling essentially never satisfies, so such elements could not be recorded at all.

`HIT_SLOP = 14.0` (device points) fixes that: `_hit_rect(r)` grows any axis shorter than `HIT_SLOP` to `HIT_SLOP`, centred on the original rect; axes already at or above the threshold — i.e. every normal element — are returned untouched. `_collect()` tests the grown rect and records elements matched *only* via the growth into its `slop_out` set; `_collect_hits(x, y, root)` returns `(candidates, slop_hits)`.

**Only the hit region grows — `_score()` still computes `area` from the real rect**, and `slop_hits` is deprioritised at tuple position 6, so a slop-only hit never outranks an equally-qualified exact hit (a 1 pt divider hugging a button does not steal a tap on the button's edge) while still winning when nothing better is under the coordinate.

Every hit-test entry point shares `_collect_hits()`: `hit_test`, `hit_test_for_swipe` (`_swipe_score` carries the same `is_slop_hit` term before `area`), `hit_test_excluding`, `hit_test_drop_target`, `hit_test_long_press_drag_source`. `find_scroll_container`'s coordinate mode keeps plain `_collect()` — scrollable containers exceed 14 pt on both axes, so `_hit_rect()` is the identity there.

`static/app.js` mirrors the constant and the rule in `_hitRect()` / `_clientHitTest()` so the hover highlight matches what actually gets recorded. **Change `HIT_SLOP` in both files or the two will disagree.**

### `_collect(x, y, el, out, slop_out=None)`

Recursively finds ALL elements whose (slop-adjusted) bounding rect contains `(x, y)`. Returns a flat list; when `slop_out` is given, elements matched only via `HIT_SLOP` are added to it. `hit_test` then picks the highest-scored element from this list. `find_scroll_container` uses this list only in coordinate mode (scroll gestures), filtering it for scrollable types and picking the smallest area (innermost); in ancestor mode it walks `_find_path()` instead.

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
