#!/bin/bash
# Double-click this file to launch the Key Counter Overlay

cd "$(dirname "$0")"

# Run detached from terminal
nohup python3 key_counter_overlay.py > /dev/null 2>&1 &

# Wait for app to start
sleep 0.5

# Close this terminal window (macOS)
osascript -e 'tell application "Terminal" to close front window' 2>/dev/null &
exit 0
