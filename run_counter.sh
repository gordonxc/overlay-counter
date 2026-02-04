#!/bin/bash
#
# Run Key Counter Overlay
# Checks environment and launches the counter
#

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
COUNTER_SCRIPT="$SCRIPT_DIR/key_counter_overlay.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=== Key Counter Overlay ==="
echo

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    # Check if 'python' is Python 3
    PY_VERSION=$(python -c 'import sys; print(sys.version_info[0])' 2>/dev/null)
    if [ "$PY_VERSION" = "3" ]; then
        PYTHON_CMD="python"
    else
        echo -e "${RED}Error: Python 3 is required but only Python 2 was found.${NC}"
        exit 1
    fi
else
    echo -e "${RED}Error: Python is not installed.${NC}"
    echo "Please install Python 3:"
    echo "  macOS:   brew install python3"
    echo "  Ubuntu:  sudo apt install python3 python3-tk"
    echo "  Windows: https://www.python.org/downloads/"
    exit 1
fi

echo -e "${GREEN}✓${NC} Python found: $($PYTHON_CMD --version)"

# Check if tkinter is available
if ! $PYTHON_CMD -c "import tkinter" &> /dev/null; then
    echo -e "${YELLOW}tkinter not found. Attempting to install...${NC}"

    # Detect OS and install
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install python-tk
        else
            echo -e "${RED}Error: Homebrew not found. Please install tkinter manually:${NC}"
            echo "  brew install python-tk"
            exit 1
        fi
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]] || [[ "$(uname -s)" == MINGW* ]] || [[ "$(uname -s)" == CYGWIN* ]]; then
        # Windows (Git Bash, MSYS2, Cygwin)
        if command -v choco &> /dev/null; then
            echo "Installing Python with tkinter via Chocolatey..."
            choco install python -y
        elif command -v winget &> /dev/null; then
            echo "Installing Python with tkinter via winget..."
            winget install Python.Python.3 --accept-source-agreements --accept-package-agreements
        else
            echo -e "${RED}Error: tkinter is missing.${NC}"
            echo "On Windows, tkinter comes bundled with Python."
            echo "Please reinstall Python from https://www.python.org/downloads/"
            echo "During installation, ensure 'tcl/tk and IDLE' is checked."
            exit 1
        fi
    elif command -v apt &> /dev/null; then
        # Debian/Ubuntu
        sudo apt update && sudo apt install -y python3-tk
    elif command -v dnf &> /dev/null; then
        # Fedora
        sudo dnf install -y python3-tkinter
    elif command -v pacman &> /dev/null; then
        # Arch
        sudo pacman -S --noconfirm tk
    else
        echo -e "${RED}Error: Could not detect package manager.${NC}"
        echo "Please install tkinter manually."
        exit 1
    fi

    # Verify installation
    if ! $PYTHON_CMD -c "import tkinter" &> /dev/null; then
        echo -e "${RED}Error: tkinter installation failed.${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓${NC} tkinter installed successfully"
else
    echo -e "${GREEN}✓${NC} tkinter available"
fi

# Check if the counter script exists
if [ ! -f "$COUNTER_SCRIPT" ]; then
    echo -e "${RED}Error: key_counter_overlay.py not found at:${NC}"
    echo "  $COUNTER_SCRIPT"
    exit 1
fi

echo -e "${GREEN}✓${NC} Counter script found"
echo
echo -e "${YELLOW}Launching counter...${NC}"
echo "  Left-click to count"
echo "  Right-click for menu (Reset/Exit)"
echo

# Run the counter
exec $PYTHON_CMD "$COUNTER_SCRIPT"
