# 計數器懸浮窗

一個簡約、無邊框的桌面計數器懸浮窗。

## 功能

- 左鍵點擊 +1
- 拖曳移動視窗
- 右鍵選單
- 永遠置頂
- 自訂顯示格式
- 自訂文字/背景顏色
- 可調整透明度

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

## 右鍵選單

| 選項 | 功能 |
|------|------|
| Set Number... | 手動輸入數字 |
| Reset | 重置為 0 |
| Text Color... | 更改文字顏色 |
| Background Color... | 更改背景顏色 |
| Transparency... | 調整透明度 (10-100%) |
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
