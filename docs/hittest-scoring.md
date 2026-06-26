# Hit-Test 評分邏輯說明

> 對應檔案：`app/hittest.py`

---

## 概覽

每次手勢時，`_collect(x, y)` 會收集所有包含該座標的元素（iOS UI 樹是嵌套的，父元素 rect 一定涵蓋所有子元素，因此同一個座標可能命中數十個元素）。

**不同手勢走不同的評分路徑：**

| 情境 | 函式 | 邏輯目標 |
|------|------|---------|
| Tap / Long Press / Drag | `hit_test()` → `_score()` | 找最具體的**葉節點**（Button、Image 等） |
| Swipe（找滑動目標） | `hit_test_for_swipe()` → `_swipe_score()` | 找有識別符的容器，排除 generic wrapper |
| Scroll（找滾動容器） | `find_scroll_container()` | 只從 `SCROLLABLE_TAGS` 或 `scrollable="true"` 裡挑**最內層**的 |

每套函式的「容器優先 vs 葉節點優先」方向完全相反，因為手勢語意不同。

所有評分函式都以 `min()` 取勝——**分數越小越優先**。

---

## 元素分類集合

### INTERACTIVE_TAGS（互動元素）
會被視為「可直接互動的葉節點」，在評分中獲得加分：

| XCUIElement 類型 |
|---|
| XCUIElementTypeButton |
| XCUIElementTypeTextField |
| XCUIElementTypeSecureTextField |
| XCUIElementTypeSwitch |
| XCUIElementTypeLink |
| XCUIElementTypeCheckBox |
| XCUIElementTypeSlider |

> ⚠️ `XCUIElementTypeCell` 不在此集合。Cell 是容器，不是葉節點互動元素。

---

### TAP_CONTAINER_TAGS（結構容器，tap 時降優先）
包含 `SCROLLABLE_TAGS` + Application / Window：

| XCUIElement 類型 |
|---|
| XCUIElementTypeScrollView |
| XCUIElementTypeCollectionView |
| XCUIElementTypeTable |
| XCUIElementTypeWebView |
| XCUIElementTypeTextView |
| XCUIElementTypeApplication |
| XCUIElementTypeWindow |

這類元素通常是版面結構用途，點擊時若有更具體的子元素，應優先選子元素。

---

### GENERIC_CONTAINER_TAGS（滑動時降優先）
僅用於 `hit_test_for_swipe()`，不影響 tap 評分：

| XCUIElement 類型 |
|---|
| XCUIElementTypeOther |
| XCUIElementTypeApplication |
| XCUIElementTypeWindow |
| XCUIElementTypeView |

---

## Tap 評分公式（`_score`）

用於 `hit_test()`，目標是找到最具體的**葉節點**。

```python
(
    int(is_container),
    int(is_generic_wrapper),
    -int(has_stable_id),
    -int(is_interactive),
    area,
    -int(has_id),
    int(has_children),
)
```

其中 hidden 的 inactive renderer/ROI layer（目前以 `rendererViewController.*`、`rOI.*` 命名開頭辨識）不會拿 `has_stable_id` 或 `is_interactive` 加分。其他 hidden element 仍保留既有幾何/語意行為，避免破壞舊的 xpath fallback fixture。

### 各欄位說明與設計原因

| 順位 | 欄位 | 數值 | 設計原因 |
|:---:|---|---|---|
| 1 | `is_container` | 0 / 1 | **非容器優先**。`TAP_CONTAINER_TAGS`（ScrollView、CollectionView 等）是版面結構，不是點擊目標。這是最粗粒度的過濾，「根本不可能是目標」的應該最先被排到後面，不需要看後面任何條件。 |
| 2 | `is_generic_wrapper` | 0 / 1 | **互動元素優先於 generic wrapper**。只有同一批候選元素裡存在 Switch、Button、TextField、Slider 等互動元件時，`XCUIElementTypeOther` / `XCUIElementTypeView` 才會被降權；這避免背景或結構層即使有穩定 `name`，仍壓過真正被點擊的控制項。 |
| 3 | `-has_stable_id` | -1 / 0 | **穩定 ID 葉節點優先**。`quality == "id"` 或 `"id_eq_label"` **且無子元素**才算。有穩定 accessibility id 的葉節點幾乎一定是開發者刻意命名的可操作元素，是最可靠的點擊目標。加上「無子元素」限制，是因為 ViewController 根 View 也常有穩定 ID（如 `"com.app.MyVC"`）但面積極大，若不排除有子元素的情況，這類大容器反而會搶走葉節點的優先權。hidden renderer/ROI layer 例外：這些 stale frame 不應靠 stable id 搶走可見目標。容器與 generic wrapper 過濾必須先做，才輪到 ID 品質判斷。 |
| 4 | `-is_interactive` | -1 / 0 | **互動元素次優先**。Button、TextField、Slider 等語意上就是「使用者能互動的東西」。hidden renderer/ROI layer 不拿這個加分，避免 inactive renderer control 搶走可見目標。在找不到穩定 ID 葉節點的情況下，這些比匿名的 Image 或 Other 更接近使用者意圖。穩定 ID 比「元素類型是 Button」更能代表精確意圖，所以排在第 3 位之後。 |
| 5 | `area` | 浮點數 | **面積越小越具體**。iOS UI 樹是嵌套結構，子元素的 rect 一定在父元素之內，所以面積越小代表層次越深、越精確命中。面積只是幾何事實，沒有語意，所以排在語意條件之後，作為「語意相同時」的幾何 tiebreaker。 |
| 6 | `-has_id` | -1 / 0 | **有識別符優於純 xpath**。到了這一步代表前五個條件都相同（如 cell 與裡面的 image 剛好同大）。有 `name` 或 `label` 至少能生成有意義的選擇器，不會退化成 `//XCUIElementTypeOther`。 |
| 7 | `has_children` | 0 / 1 | **葉節點優先**。最後手段：以上全部相同時，無子元素的葉節點比中間層節點更「具體」，更接近實際被渲染的 UI 元件。 |

**整體設計邏輯：**
```
排掉結構容器 → 視情境排掉 generic wrapper → 找最精確命名的葉節點 → 找語意互動元素 → 找最小幾何元素 → 找有識別符的 → 找葉節點
 (語意最粗)                                                                                                      (最後手段)
```
每一層都在上一層「無法區分」時才出場，避免讓幾何數字（面積）蓋過語意判斷。

---

## Selector 品質定義（`get_selector_quality`）

| 品質等級 | 條件 | 說明 |
|---|---|---|
| `"id"` | `name` 存在，且不等於 `label`，且不以 `-數字` 結尾 | 最穩定 |
| `"id_indexed"` | `name` 存在，但以 `-<數字>` 結尾（如 `Cell-3`） | 索引可能位移，脆弱 |
| `"id_eq_label"` | `name` 存在，且與 `label` 相同 | 可能脆弱，視情況而定 |
| `"label_only"` | 無穩定 `name`，只有 `label` | 較脆弱 |
| `"xpath_only"` | 無任何識別符 | 最脆弱，用 xpath 備用 |

`has_stable_id = quality in ("id", "id_eq_label")`

---

## 實際場景驗證

### 場景 A：Cell-3 vs QuickAction_BG_W_Zoom（Image）

| 元素 | is_container | has_stable_id | is_interactive | area | 勝負 |
|---|:---:|:---:|:---:|---|:---:|
| `Cell-3`（XCUIElementTypeCell） | 0 | ❌ `id_indexed` | 0 | 大 | ❌ 輸 |
| `QuickAction_BG_W_Zoom`（Image） | 0 | ✅ `id` | 0 | 小 | ✅ 贏 |

`-has_stable_id` 這欄決定勝負（-1 < 0）。

---

### 場景 B：photoCollectionView vs photoCell-6

| 元素 | is_container | has_stable_id | is_interactive | area | 勝負 |
|---|:---:|:---:|:---:|---|:---:|
| `photoCollectionView`（CollectionView） | ✅ 1 | ✅ `id` | 0 | 極大 | ❌ 輸 |
| `photoCell-6`（Cell） | 0 | ❌ `id_indexed` | 0 | 小 | ✅ 贏 |

`is_container` 這欄決定勝負（0 < 1）。

---

### 場景 C：Button（無 ID）vs Image（有穩定 ID）

| 元素 | is_container | has_stable_id | is_interactive | area | 勝負 |
|---|:---:|:---:|:---:|---|:---:|
| `Button`（無名稱） | 0 | ❌ | ✅ | 中 | ❌ 輸 |
| `QuickAction_BG_W_Zoom`（Image） | 0 | ✅ | 0 | 小 | ✅ 贏 |

穩定 ID 優先於 interactive（第 2 欄比第 3 欄更重要）。

---

### 場景 D：Button（有穩定 ID）vs Image（有穩定 ID）

| 元素 | is_container | has_stable_id | is_interactive | area | 勝負 |
|---|:---:|:---:|:---:|---|:---:|
| `Button 'Submit'`（穩定 ID） | 0 | ✅ | ✅ | 小 | ✅ 贏（interactive 加分） |
| `Container`（穩定 ID） | 0 | ✅ | 0 | 大 | ❌ 輸 |

兩者 `has_stable_id` 相同，由 `is_interactive` + `area` 決定。

---

## Swipe 評分公式（`_swipe_score`）

用於 `hit_test_for_swipe()`。Swipe 的語意與 tap 相反——目標是「被滑動的容器」，不是最深的葉節點，因此走完全不同的評分路徑。

```python
(-int(is_interactive), int(is_generic), area)
```

| 順位 | 欄位 | 設計原因 |
|:---:|---|---|
| 1 | `-is_interactive` | 若有互動元素（Button 等）在座標上，優先選它作為滑動起點，比匿名容器更精確 |
| 2 | `is_generic` | 排除 `GENERIC_CONTAINER_TAGS`（Other、Application、Window）——這類元素是無語意的 wrapper，滑動時幾乎不會是真正的目標 |
| 3 | `area` | 面積最小者勝，取最內層、最具體的容器 |

---

## Scroll 容器選取（`find_scroll_container`）

用於 scroll 錄製，不走評分公式，而是**直接過濾**：

1. 只保留 `SCROLLABLE_TAGS`（ScrollView、CollectionView、Table、WebView、TextView）
2. 若找不到，退而找 `scrollable="true"` 屬性的元素（WDA 對非標準 scroll view 的標記）
3. 從符合條件的元素中取**面積最小**（最內層）的一個

這樣可確保 scroll 動作綁定到最精確的可滾動容器，而非外層的 Window 或 Application。
