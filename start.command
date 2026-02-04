#!/bin/bash
# Double-click this file to launch the Key Counter Overlay

cd "$(dirname "$0")"

# Run in background and close terminal
python3 key_counter_overlay.py &

# Close this terminal window (macOS)
osascript -e 'tell application "Terminal" to close front window' &
exit 0
