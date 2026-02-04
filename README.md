# 計數器懸浮窗

一個簡約、無邊框的桌面計數器懸浮窗。

## 功能

- 左鍵點擊 +1
- 右鍵選單（重置 / 退出）
- 永遠置頂
- 自訂顯示格式

## 安裝需求

- Python 3
- tkinter（通常已內建於 Python）

## 使用方法

### macOS

雙擊 `Key Counter.command`

或於終端機執行：
```bash
./run_counter.sh
```

### Windows

雙擊 `start.bat`

### 直接執行

```bash
python3 key_counter_overlay.py
```

## 自訂顯示格式

編輯 `config.txt` 檔案，使用 `{count}` 作為數字佔位符。

**範例：**

| config.txt 內容 | 顯示效果 |
|---|---|
| `{count}` | `0`、`1`、`2`... |
| `分數：{count}` | `分數：0`、`分數：1`... |
| `死亡次數：{count}` | `死亡次數：0`、`死亡次數：1`... |

## 平台支援

| 平台 | 狀態 |
|---|---|
| macOS | ✓ 支援 |
| Windows | ✓ 支援 |
| Linux | ✓ 支援（可能需要安裝 `python3-tk`） |

## 檔案說明

| 檔案 | 說明 |
|---|---|
| `key_counter_overlay.py` | 主程式 |
| `config.txt` | 顯示格式設定 |
| `Key Counter.command` | macOS 啟動器 |
| `start.bat` | Windows 啟動器 |
| `run_counter.sh` | Shell 啟動腳本 |
