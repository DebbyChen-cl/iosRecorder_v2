# Hierarchy Polling

`_hierarchy_loop()` in `app/main.py` is a background task that keeps `_cache["root"]` continuously fresh with the latest WDA element tree. All recording actions read from this cache rather than blocking on a live WDA request.

---

## 三個狀態

Loop 啟動時從 **FAST** 開始，根據 hash 穩定程度自動往 SLOW → IDLE 移動。

| 狀態 | 觸發條件 | fetch 後等多久 |
|------|---------|--------------|
| **FAST** | 啟動、手勢後、hash 改變 | `fast_interval_ms`（預設 0ms，立刻再 fetch）|
| **SLOW** | 連續 `stable_threshold` 次 hash 相同 | `slow_interval_ms`（預設 5000ms）|
| **IDLE** | 連續 `idle_threshold` 次 hash 相同 | `idle_interval_ms`（預設 10000ms）|

> **注意**：sleep 的意義是「這段時間完全不發 WDA request」，不是「fetch 變慢一點」。WDA 本身每次 get_source 就需要 400ms–2s，SLOW/IDLE 節省的是在 UI 沒有變動時不要浪費這段時間。

---

## 狀態轉換規則

```
啟動
  └─► FAST

每次 fetch 完成後：
  hash 和上次不同  ─► stable_count = 0, state = FAST
  hash 和上次相同  ─► stable_count += 1
                        stable_count >= stable_threshold  ─► FAST → SLOW
                        stable_count >= idle_threshold    ─► SLOW → IDLE

手勢偵測到（_action_in_progress = True）：
  └─► 取消進行中的 source fetch
      清空 cache（root = None）
      等手勢結束
      stable_count = 0, last_hash = None, state = FAST
```

---

## 手勢中斷機制

Sleep 使用 `_interruptible_sleep(seconds)`，每 100ms 輪詢一次 `wda._action_in_progress`。當偵測到手勢開始，立刻返回，不會卡在 SLOW/IDLE 的 sleep 裡等到超時。

---

## Structural Hash 比對

不能用原始 XML string 做比較，因為 `value`、`frame` 等動態 attribute 會因動畫、捲動位置而每次都不同，導致永遠回不到 SLOW/IDLE。

`_structural_hash()` 的做法：遍歷所有 element，取出 **非忽略** 的 attribute，算 MD5。

### 預設忽略的 attributes

| Attribute | 忽略原因 |
|-----------|---------|
| `value`   | 輸入框內容、動畫數值，頻繁變動但不代表頁面結構改變 |
| `x`       | 元素座標，捲動時持續變動 |
| `y`       | 同上 |
| `width`   | 動態佈局 |
| `height`  | 同上 |
| `frame`   | `{x,y,w,h}` 的字串形式，同上 |

保留的 attribute 包括：`type`（element tag）、`name`、`label`、`enabled`、`visible` 等結構性欄位。

---

## Config

所有參數放在 `.wda_config.json` 的 `hierarchy_polling` 區塊，不用改 code：

```json
{
  "wda_url": "http://localhost:8100",
  "hierarchy_polling": {
    "fast_interval_ms": 0,
    "slow_interval_ms": 5000,
    "idle_interval_ms": 10000,
    "stable_threshold": 3,
    "idle_threshold": 5,
    "ignored_attributes": ["value", "x", "y", "width", "height", "frame"]
  }
}
```

| 欄位 | 說明 |
|------|------|
| `fast_interval_ms` | FAST 狀態 fetch 後等多久（0 = 立刻再 fetch）|
| `slow_interval_ms` | SLOW 狀態 fetch 後等多久 |
| `idle_interval_ms` | IDLE 狀態 fetch 後等多久 |
| `stable_threshold` | 連續幾次 hash 相同才切到 SLOW |
| `idle_threshold`   | 連續幾次 hash 相同才切到 IDLE（從 0 累計，不是從 stable_threshold 重算）|
| `ignored_attributes` | hash 比對時要忽略的 attribute 名稱清單 |

---

## Hierarchy 使用時機

| 呼叫點 | 說明 |
|--------|------|
| 每個手勢 API endpoint（tap / swipe / drag 等） | 在**送出手勢前**從 `_cache["root"]` 取 snapshot，用於 hit-test 和 selector 分析 |
| `GET /api/element_info` | 直接讀 `_cache["root"]`（非阻塞），用於 UI hover 顯示 selector |
| `verify_visible` / `verify_get_text` / `verify_screenshot_*` | 透過 `_cached_tree()` 取 hierarchy，cache 空時才真正 fetch |
| `_cached_tree()` fallback | cache 為空（啟動或 WDA 重連時）才呼叫 `wda.get_source()` 補一次 |

---

## Console Log 格式

Server 啟動後 terminal 會持續印出：

```
[hierarchy] 14:32:01  fetch=  1243ms  state=FAST  stable=0  sleep=0ms
[hierarchy] 14:32:02  fetch=   987ms  state=FAST  stable=1  sleep=0ms
[hierarchy] 14:32:07  fetch=   912ms  state=SLOW → SLOW  stable=3  sleep=5000ms
[hierarchy] 14:32:14  fetch=  1034ms  state=IDLE → IDLE  stable=5  sleep=10000ms
[hierarchy] 14:32:35  gesture done → FAST (reset)
[hierarchy] 14:32:36  fetch=  1201ms  state=FAST  stable=0  sleep=0ms *** HASH CHANGED
```

| 欄位 | 說明 |
|------|------|
| `fetch=` | 這次 `wda.get_source()` 花了多久 |
| `state=X → Y` | 剛發生狀態切換 |
| `stable=` | 連續幾次 hash 相同 |
| `sleep=` | 本次 fetch 後實際等多久才發下一次 |
| `*** HASH CHANGED` | 結構有變動，已重置回 FAST |
