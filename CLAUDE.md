# Key Counter Overlay

A minimal, borderless click counter overlay.

## Files

- `key_counter_overlay.py` - Main Python/tkinter application
- `config.txt` - Display format configuration
- `run_counter.sh` - Shell script launcher (auto-installs dependencies)
- `Key Counter.command` - macOS double-click launcher
- `start.bat` - Windows double-click launcher
- `README.md` - Documentation (Traditional Chinese)

## Requirements

- Python 3 (auto-installed if missing)
- tkinter (auto-installed if missing)

## Usage

**macOS:** Double-click `Key Counter.command`

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
| Right-click | Menu (Reset / Exit) |

## Configuration

Edit `config.txt` to customize display format. Use `{count}` as placeholder.

Examples:
- `{count}` → `0`, `1`, `2`...
- `Score: {count}` → `Score: 0`, `Score: 1`...
- `Deaths: {count}` → `Deaths: 0`, `Deaths: 1`...

## Features

- Borderless, minimal window
- Always-on-top overlay
- Auto-sizes to fit text
- Semi-transparent (85% opacity)
- Custom display format via config.txt
- Cross-platform (macOS, Linux, Windows)
- Auto-installs Python and tkinter if missing

## Auto-install Support

| Platform | Package Manager |
|---|---|
| macOS | Homebrew |
| Ubuntu/Debian | apt |
| Fedora | dnf |
| Arch | pacman |
| Windows | winget / Chocolatey |
