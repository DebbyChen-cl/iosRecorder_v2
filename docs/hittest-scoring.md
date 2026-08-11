# Hit-Test 評分邏輯說明

> 對應檔案：`app/hittest.py`

---

## 概覽

每次手勢時，`_collect(x, y)` 會收集所有包含該座標的元素（iOS UI 樹是嵌套的，父元素 rect 一定涵蓋所有子元素，因此同一個座標可能命中數十個元素）。單軸小於 `HIT_SLOP` 的極薄元素會以放大後的命中區判定（見下方 [極薄元素命中容差](#極薄元素命中容差hit_slop)）。

**不同手勢走不同的評分路徑：**

| 情境 | 函式 | 邏輯目標 |
|------|------|---------|
| Tap / Long Press / Drag | `hit_test()` → `_score()` | 找最具體的**葉節點**（Button、Image 等） |
| Swipe（找滑動目標） | `hit_test_for_swipe()` → `_swipe_score()` | 找有識別符的容器，排除 generic wrapper |
| Scroll（找滾動容器） | `find_scroll_container()` | 給 `target` 時取其**祖先鏈**上最內層的可滾動元素；未給時退回座標上面積最小者 |

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
    int(not is_visible),
    int(is_generic_wrapper),
    -int(has_stable_id),
    -int(is_interactive),
    int(is_slop_hit),
    area,
    int(not is_really_visible),
    -int(has_id),
    int(has_children),
)
```

其中 hidden 的 inactive renderer/ROI layer（目前以 `rendererViewController.*`、`rOI.*` 命名開頭辨識）不會拿 `has_stable_id` 或 `is_interactive` 加分。

### 各欄位說明與設計原因

| 順位 | 欄位 | 數值 | 設計原因 |
|:---:|---|---|---|
| 1 | `is_container` | 0 / 1 | **非容器優先**。`TAP_CONTAINER_TAGS`（ScrollView、CollectionView 等）是版面結構，不是點擊目標。這是最粗粒度的過濾，「根本不可能是目標」的應該最先被排到後面，不需要看後面任何條件。 |
| 2 | `not is_visible` | 0 / 1 | **可見元素優先**。WDA 樹中隱藏的 sibling（如訂閱對話框、overlay）會帶著過期的 frame 留在樹裡，與可見內容重疊。若不先過濾，隱藏元素可能因面積較小而搶贏可見目標。可見性在容器之後、語意條件之前，確保隱藏元素不會因穩定 ID 或互動標記而搶走可見目標。**例外**：被 `_visibility_exemptions()` 判定為「僅被遮擋」的元素，此欄視為 0（見下節）。 |
| 3 | `is_generic_wrapper` | 0 / 1 | **互動元素優先於 generic wrapper**。只有同一批候選元素裡存在 Switch、Button、TextField、Slider 等互動元件時，`XCUIElementTypeOther` / `XCUIElementTypeView` 才會被降權；這避免背景或結構層即使有穩定 `name`，仍壓過真正被點擊的控制項。 |
| 4 | `-has_stable_id` | -1 / 0 | **穩定 ID 葉節點優先**。`quality == "id"` 或 `"id_eq_label"` **且無子元素**才算。有穩定 accessibility id 的葉節點幾乎一定是開發者刻意命名的可操作元素，是最可靠的點擊目標。加上「無子元素」限制，是因為 ViewController 根 View 也常有穩定 ID（如 `"com.app.MyVC"`）但面積極大，若不排除有子元素的情況，這類大容器反而會搶走葉節點的優先權。hidden renderer/ROI layer 例外：這些 stale frame 不應靠 stable id 搶走可見目標。容器與 generic wrapper 過濾必須先做，才輪到 ID 品質判斷。 |
| 5 | `-is_interactive` | -1 / 0 | **互動元素次優先**。Button、TextField、Slider 等語意上就是「使用者能互動的東西」。hidden renderer/ROI layer 不拿這個加分，避免 inactive renderer control 搶走可見目標。在找不到穩定 ID 葉節點的情況下，這些比匿名的 Image 或 Other 更接近使用者意圖。穩定 ID 比「元素類型是 Button」更能代表精確意圖，所以排在第 4 位之後。 |
| 6 | `is_slop_hit` | 0 / 1 | **精確命中優於容差命中**。座標真的落在元素 rect 內的候選，一律排在只靠 `HIT_SLOP` 放大才命中的極薄元素之前。位置刻意排在語意條件之後、`area` 之前：極薄元素往往帶穩定 ID 又面積極小，若不加這一欄，一條緊貼按鈕的 1 pt 分隔線會在使用者點按鈕邊緣時搶走目標；而當座標上沒有其他更好的候選時（例如 `barImageView` 只被全螢幕 anchor view 包住），它仍然選得到。 |
| 7 | `area` | 浮點數 | **面積越小越具體**。iOS UI 樹是嵌套結構，子元素的 rect 一定在父元素之內，所以面積越小代表層次越深、越精確命中。面積只是幾何事實，沒有語意，所以排在語意條件之後，作為「語意相同時」的幾何 tiebreaker。 |
| 8 | `not is_really_visible` | 0 / 1 | **真可見優於「僅被豁免」**。第 2 順位對被遮擋豁免的元素放行後，它與遮擋它的元素在可見性上同分；若兩者 rect 完全一樣，`area` 也分不出勝負，勝負就退化成文件順序（見場景 G）。這一欄在幾何完全打平時，讓 WDA 真的回報 `visible="true"` 的那個勝出。刻意排在 `area` **之後**：場景 F / 場景 G-2 中被豁免的元素本來就是面積較小的那個，會先在 `area` 決勝，不受影響。 |
| 9 | `-has_id` | -1 / 0 | **有識別符優於純 xpath**。到了這一步代表前面所有條件都相同（如 cell 與裡面的 image 剛好同大）。有 `name` 或 `label` 至少能生成有意義的選擇器，不會退化成 `//XCUIElementTypeOther`。 |
| 10 | `has_children` | 0 / 1 | **葉節點優先**。最後手段：以上全部相同時，無子元素的葉節點比中間層節點更「具體」，更接近實際被渲染的 UI 元件。 |

**整體設計邏輯：**
```
排掉結構容器 → 排掉隱藏元素 → 排掉 generic wrapper → 找最精確命名的葉節點 → 找語意互動元素 → 精確命中優先 → 找最小幾何元素 → 真可見優先 → 找有識別符的 → 找葉節點
 (語意最粗)                                                                                                                                                    (最後手段)
```
每一層都在上一層「無法區分」時才出場，避免讓幾何數字（面積）蓋過語意判斷。

---

## 遮擋誤判豁免（`_visibility_exemptions` / `_is_occluded_not_hidden`）

WDA 的 `visible` **不是「有沒有被渲染」，而是「hit-test 打不打得到」**。只要有另一個 view 疊在上層（不論它自己是不是 accessibility element），底下即使真的畫在螢幕上，也會被標成 `visible="false"`。若無條件套用第 2 順位的可見性懲罰，這類元素永遠選不到。

`hit_test()` 在評分前先呼叫 `_visibility_exemptions(candidates, root)`，把「只是被遮擋、其實看得到」的候選元素挑出來，`_score()` 對這些元素把 `is_visible` 視為 `True`（`has_stable_id` 的可見性條件同步放行）。

判定條件——沿 el 的祖先鏈往上找，只要任何一層的**後方 sibling**同時滿足下列全部條件，即認定為遮擋誤判：

| 條件 | 原因 |
|---|---|
| 是**後方** sibling（index 較大） | UIKit 中後面的 sibling 畫在上層，只有上層才可能遮住它 |
| `visible="true"` | 遮擋者自己必須真的在畫面上 |
| **無子元素**（leaf） | 關鍵鑑別條件。被「取代」而真正隱藏的子樹，上面蓋的是有子元素的結構容器（或根本沒東西蓋）；只有 overlay 型的裸 leaf（全幅 Image、遮罩）才會造成純粹的 hit-test 誤判 |
| frame **完整覆蓋** el 的 rect | 部分重疊不足以吃掉整個元素的 hit-test |

`_visibility_exemptions()` 只在候選中真的有隱藏元素時才建立 parent map，一次 hit-test 最多建一次。

### 場景 F：waitView 被全幅 imageView 遮擋（ArtisticAvatarResultViewController）

```
contentView
├── waitView   (index 0, visible=false) ── waitIndicator / waitLabel / waitTimeLabel 全部 visible=false
└── imageView  (index 1, visible=true, accessible=true, leaf, 與 waitView 同 frame)
```

| 元素 | not_visible（原始） | 豁免 | 實際計分 | area | 勝負 |
|---|:---:|:---:|:---:|---|:---:|
| `imageView`（visible=true） | 0 | — | 0 | 233060 | ❌ 輸 |
| `waitLabel`（visible=false） | 1 | ✅ | **0** | 11610 | ✅ 贏 |

豁免後兩者可見性同分，由 `area` 決勝。同一棵樹裡的 `navView`（真隱藏，被**有子元素的** `resultTopView` 取代）不符合 leaf 條件，`navDescriptionLabel` 仍維持降權——(150,88) 依舊選到 `resultTopView`。Canva 已關閉的訂閱對話框是最上層、後方沒有 sibling 覆蓋它，同樣不會被豁免，場景 D 的保護完全保留。

回歸測試：`test_unittest/test_hittest_selector_regressions.py::test_hit_test_picks_wait_elements_occluded_by_full_size_image` 及同組的兩個對照測試。

### 場景 G：同 rect 的 thumbnailImageView vs processingLabel（ImageToVideoHistoryBrowseViewController）

影片還在算圖時，cell 會把「還沒載入的縮圖」和「Processing...」文字疊在**完全相同的 rect** 上：

```
imageContainerView (18,230,165,165)
├── thumbnailImageView (index 0, Image,      visible=false, 165x165)
└── processingLabel    (index 1, StaticText, visible=true,  165x165, value/label="Processing...")
```

`processingLabel` 是後方 sibling、visible、leaf、且完整覆蓋縮圖，所以 `thumbnailImageView` 被豁免、視為可見。兩者接著在 `has_stable_id`、`is_interactive`、`area` **全部同分**——`min()` 於是退化成文件順序，選到使用者根本看不到的 `thumbnailImageView`。

| 元素 | not_visible（豁免後） | has_stable_id | area | `not is_really_visible` | 勝負 |
|---|:---:|:---:|---|:---:|:---:|
| `thumbnailImageView`（visible=false，豁免） | 0 | ✅ | 27225 | **1** | ❌ 輸 |
| `processingLabel`（visible=true） | 0 | ✅ | 27225 | **0** | ✅ 贏 |

第 8 順位 `not is_really_visible` 就是為這種「幾何完全打平」的情況存在。算圖完成的 cell 沒有 `processingLabel`，`thumbnailImageView` 本身 `visible="true"`，仍然正常選得到。

回歸測試：`test_hit_test_prefers_processing_label_over_same_rect_hidden_thumbnail` 與對照組 `test_hit_test_keeps_thumbnail_where_no_processing_label_covers_it`。

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

### 場景 D：隱藏的 AppLogo（小面積）vs 可見的 Image（大面積）

| 元素 | is_container | not_visible | has_stable_id | is_interactive | area | 勝負 |
|---|:---:|:---:|:---:|:---:|---|:---:|
| `AppLogo`（Image, visible=false） | 0 | ✅ 1 | ✅ `id` | 0 | 小 (9216) | ❌ 輸 |
| 匿名 Image（visible=true） | 0 | 0 | ❌ | 0 | 大 (132480) | ✅ 贏 |

`not_visible` 決定勝負（0 < 1）。即使隱藏元素有穩定 ID 且面積更小，可見性仍優先。

---

### 場景 E：Button（有穩定 ID）vs Image（有穩定 ID）

| 元素 | is_container | has_stable_id | is_interactive | area | 勝負 |
|---|:---:|:---:|:---:|---|:---:|
| `Button 'Submit'`（穩定 ID） | 0 | ✅ | ✅ | 小 | ✅ 贏（interactive 加分） |
| `Container`（穩定 ID） | 0 | ✅ | 0 | 大 | ❌ 輸 |

兩者 `has_stable_id` 相同，由 `is_interactive` + `area` 決定。

---

## 極薄元素命中容差（`HIT_SLOP`）

分隔線、比較桿、slider 軌道這類元素在 WDA 樹裡常常單軸只有 1 pt——例如 `AIExpandViewController` 的 `barImageView`（`302x1`，`y=454`）。嚴格的矩形包含判定只接受 `454 ≤ y ≤ 455`，而串流畫面座標經過顯示縮放換算後是浮點數，1 pt 在面板上大約只對應半個到一個顯示像素，實務上等於永遠點不到，這類元素完全無法被錄製。

`HIT_SLOP = 14.0`（裝置點）解決這件事：

- `_hit_rect(r)` 把單軸小於 `HIT_SLOP` 的邊長以**原中心為基準**放大到 `HIT_SLOP`；已達門檻的軸與大元素完全不受影響。
- `_collect(x, y, out, slop_out)` 以放大後的矩形判定命中，並把「只有靠放大才命中」的元素記進 `slop_out`。`_collect_hits()` 回傳 `(candidates, slop_hits)` 這一組。
- **只有命中區被放大，`_score()` 仍用真實 rect 計算 `area`**，所以放大不會讓極薄元素在幾何上看起來更大或更小。
- `slop_hits` 透過 `_score(..., slop_hits)` 的第 6 欄降權，確保容差命中永遠排在同級的精確命中之後。

適用範圍：`hit_test()`、`hit_test_for_swipe()`、`hit_test_excluding()`、`hit_test_drop_target()`、`hit_test_long_press_drag_source()` 全部共用 `_collect_hits()`。`find_scroll_container()` 的座標模式沿用 `_collect()`，但可滾動容器兩軸都遠大於 14 pt，`_hit_rect()` 對它們是恆等函式，行為不變。

前端 `static/app.js` 的 `_hitRect()` / `_clientHitTest()` 是同一組常數與規則的鏡像——hover 高亮框必須和實際錄到的元素一致，否則使用者會看到框在 A、錄到 B。前端只有 `rect` 資訊，因此排序簡化為「面積最小者勝，面積相同時精確命中勝」；高亮框畫的仍是真實 rect，不是放大後的命中區。

> ⚠️ 改動 `HIT_SLOP` 時務必同步 `app/hittest.py` 與 `static/app.js` 兩處。

---

## Swipe 評分公式（`_swipe_score`）

用於 `hit_test_for_swipe()`。Swipe 的語意與 tap 相反——目標是「被滑動的容器」，不是最深的葉節點，因此走完全不同的評分路徑。

```python
(-int(is_interactive), int(is_generic), int(is_slop_hit), area)
```

| 順位 | 欄位 | 設計原因 |
|:---:|---|---|
| 1 | `-is_interactive` | 若有互動元素（Button 等）在座標上，優先選它作為滑動起點，比匿名容器更精確 |
| 2 | `is_generic` | 排除 `GENERIC_CONTAINER_TAGS`（Other、Application、Window）——這類元素是無語意的 wrapper，滑動時幾乎不會是真正的目標 |
| 3 | `is_slop_hit` | 精確命中優於 `HIT_SLOP` 容差命中，理由同 tap 評分第 6 欄 |
| 4 | `area` | 面積最小者勝，取最內層、最具體的容器 |

---

## Scroll 容器選取（`find_scroll_container`）

不走評分公式，而是**直接過濾**。依呼叫方式分兩種模式：

### 祖先模式（`target` 有給）— tap / long_press 等元素動作

從 **target 的祖先鏈**由內往外找：

1. 先找最內層屬於 `SCROLLABLE_TAGS`（ScrollView、CollectionView、Table、WebView、TextView）的祖先
2. 都沒有時，再找最內層帶 `scrollable="true"` 的祖先
3. 祖先鏈上沒有可滾動元素 → 回傳 `None`（不附加 `scroll_container`）

比對範圍是 `path[:-1]`，**不含 target 自己** —— 當 `hit_test` 直接命中滾動容器本身時，把它綁給自己沒有意義。

**為什麼一定要用祖先鏈**：只是「座標落在滾動容器矩形內」不代表元素真的在該容器裡。浮在 ScrollView 上方的按鈕、控制另一個清單的分類列，都會與不相干的滾動容器重疊。若把這種容器寫進 `scroll_container`，匯出的測試會去捲**錯的 view**，`_find_with_scroll()` 再怎麼捲都找不到元素，最後以 `NoSuchElementException: not found after 20 scrolls` 收場。

### 座標模式（`target` 為 `None`）— scroll 手勢本身

滾動手勢作用的就是手指底下那個 view，因此維持原本的座標式選取：`_collect()` 出座標上所有元素 → 同樣的兩段式過濾 → 取**面積最小**（最內層）者。

### `should_attach_scroll_container()`

最後一道守門：container 必須是 target 的真祖先才允許附加。祖先模式已保證這點，此函式是給任何仍以座標解析容器的呼叫端用的。
