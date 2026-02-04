# Key Counter Overlay

A minimal, borderless click counter overlay with timer.

## Files

- `key_counter_overlay.py` - Main Python/tkinter application
- `config.txt` - Display format configuration
- `run_counter.sh` - Shell script launcher (auto-installs dependencies)
- `start.command` - macOS double-click launcher (hides terminal)
- `start.bat` - Windows double-click launcher (hides console)
- `README.md` - Documentation (Traditional Chinese)

## Requirements

- Python 3 (auto-installed if missing)
- tkinter (auto-installed if missing)

## Usage

**macOS:** Double-click `start.command`

**Windows:** Double-click `start.bat`

**Terminal:**
```bash
./run_counter.sh
# or
python3 key_counter_overlay.py
```

## Controls

| Action | Result |
|--------|--------|
| Left-click | +1 to counter |
| Drag | Move window |
| Right-click | Context menu |
| Ctrl+Click | Context menu (macOS) |
| Middle-click | Context menu |

## Right-click Menu

| Option | Action |
|--------|--------|
| Set Number... | Manually enter count |
| Reset | Reset counter to 0 |
| Text Color... | Change text color |
| Font Size... | Change font size (8-200) |
| Background Color... | Change background color |
| Transparency... | Window opacity (10-100%) |
| Timer → Show/Hide | Toggle timer display |
| Timer → Start | Start timer |
| Timer → Pause | Pause timer |
| Timer → Reset | Reset timer to 00:00:00 |
| Exit | Quit |

## Configuration

Edit `config.txt` to customize display format. Use `{count}` as placeholder.

Examples:
- `{count}` → `0`, `1`, `2`...
- `Score: {count}` → `Score: 0`, `Score: 1`...
- `Deaths: {count}` → `Deaths: 0`, `Deaths: 1`...

## Features

- Borderless, minimal window
- Always-on-top overlay
- Draggable window
- Auto-sizes to fit text
- Customizable text/background color
- Adjustable font size
- Adjustable transparency
- Built-in timer (start/pause/reset)
- Custom display format via config.txt
- Cross-platform (macOS, Linux, Windows)
- Auto-installs Python and tkinter if missing
- Launches without terminal/console window

## Auto-install Support

| Platform | Package Manager |
|---|---|
| macOS | Homebrew |
| Ubuntu/Debian | apt |
| Fedora | dnf |
| Arch | pacman |
| Windows | winget / Chocolatey |
