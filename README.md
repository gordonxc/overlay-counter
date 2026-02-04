# 計數器懸浮窗

一個簡約、無邊框的桌面計數器懸浮窗，附帶計時器功能。

## 功能

- 左鍵點擊 +1
- 拖曳移動視窗
- 右鍵選單
- 永遠置頂
- 自訂顯示格式
- 自訂文字/背景顏色
- 可調整字體大小
- 可調整透明度
- 內建計時器

## 安裝需求

- Python 3（如缺少會自動安裝）
- tkinter（如缺少會自動安裝）

## 使用方法

### macOS

雙擊 `start.command`

### Windows

雙擊 `start.bat`

### 終端機

```bash
./run_counter.sh
# 或
python3 key_counter_overlay.py
```

## 操作方式

| 動作 | 結果 |
|------|------|
| 左鍵點擊 | +1 |
| 拖曳 | 移動視窗 |
| 右鍵點擊 | 開啟選單 |
| Ctrl+點擊 | 開啟選單（macOS）|
| 中鍵點擊 | 開啟選單 |

## 右鍵選單

| 選項 | 功能 |
|------|------|
| Set Number... | 手動輸入數字 |
| Reset | 重置計數為 0 |
| Text Color... | 更改文字顏色 |
| Font Size... | 更改字體大小 (8-200) |
| Background Color... | 更改背景顏色 |
| Transparency... | 調整透明度 (10-100%) |
| Timer → Show/Hide | 顯示/隱藏計時器 |
| Timer → Start | 開始計時 |
| Timer → Pause | 暫停計時 |
| Timer → Reset | 重置計時器為 00:00:00 |
| Exit | 退出 |

## 自訂顯示格式

編輯 `config.txt` 檔案，使用 `{count}` 作為數字佔位符。

**範例：**

| config.txt 內容 | 顯示效果 |
|---|---|
| `{count}` | `0`、`1`、`2`... |
| `分數：{count}` | `分數：0`、`分數：1`... |
| `死亡次數：{count}` | `死亡次數：0`、`死亡次數：1`... |

## 平台支援

| 平台 | 狀態 | 套件管理器 |
|------|------|-----------|
| macOS | ✓ 支援 | Homebrew |
| Windows | ✓ 支援 | winget / Chocolatey |
| Ubuntu/Debian | ✓ 支援 | apt |
| Fedora | ✓ 支援 | dnf |
| Arch | ✓ 支援 | pacman |

## 檔案說明

| 檔案 | 說明 |
|------|------|
| `key_counter_overlay.py` | 主程式 |
| `config.txt` | 顯示格式設定 |
| `start.command` | macOS 啟動器（隱藏終端機）|
| `start.bat` | Windows 啟動器（隱藏控制台）|
| `run_counter.sh` | Shell 啟動腳本（自動安裝依賴）|
