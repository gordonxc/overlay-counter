# Key Counter Overlay

A minimal, portable key counter overlay for tracking key presses.

## Files

- `key_counter_overlay.py` - Main Python/tkinter application
- `run_counter.sh` - Shell script to check environment and launch

## Requirements

- Python 3
- tkinter (usually built-in with Python)

## Usage

```bash
./run_counter.sh
```

Or directly:

```bash
python3 key_counter_overlay.py
```

## Controls

| Key | Action |
|-----|--------|
| Any key | +1 to counter |
| `r` | Reset to 0 |
| `Escape` | Quit |

## Features

- Resizable window
- Always-on-top overlay
- Semi-transparent background (85% opacity)
- Cross-platform (macOS, Linux, Windows)

## Platform Notes

- **macOS**: Works out of the box with system Python
- **Linux**: May need `sudo apt install python3-tk`
- **Windows**: Install Python from python.org (includes tkinter)
