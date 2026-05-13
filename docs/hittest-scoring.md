# Hit-Test 評分邏輯說明

> 對應檔案：`app/hittest.py`

---

## 概覽

每次點擊時，`_collect(x, y)` 會收集所有包含該座標的元素，
再由 `_score()` 為每個元素計算分數，**分數最小的元素勝出**（Python `min()`）。

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

```python
(int(is_container), -int(has_stable_id), -int(is_interactive), area, -int(has_id), int(has_children))
```

數值越小越優先（`min()` 取勝）。

### 各欄位說明

| 優先順序 | 欄位 | 數值 | 說明 |
|:---:|---|---|---|
| 1 | `is_container` | 0 / 1 | **非容器優先**：CollectionView、ScrollView 等結構容器排最後 |
| 2 | `-has_stable_id` | -1 / 0 | **穩定 ID 葉節點優先**：`quality == "id"` 或 `"id_eq_label"`，**且無子元素**才算；有子元素的容器（如 ViewController 根 View）不享有此加分 |
| 3 | `-is_interactive` | -1 / 0 | **互動元素次優先**：Button、TextField 等（同 ID 品質下的加分） |
| 4 | `area` | 浮點數 | **面積越小越具體**：像素面積 (width × height) |
| 5 | `-has_id` | -1 / 0 | **有任何識別符優於純 xpath** |
| 6 | `has_children` | 0 / 1 | **葉節點優先於有子元素的容器** |

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

```python
(-int(is_interactive), int(is_generic), area)
```

Swipe 目標是「被滑動的容器」，邏輯與 tap 不同：
1. 互動元素優先
2. Generic 容器（Other、Application 等）降優先
3. 面積最小者勝
