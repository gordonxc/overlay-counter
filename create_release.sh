#!/bin/bash

# GitHub Release script for Key Counter Overlay
# Creates platform-specific packages and publishes to GitHub

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

APP_NAME="key-counter-overlay"
RELEASE_DIR="dist"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# Check gh CLI
command -v gh &>/dev/null || error "GitHub CLI (gh) not installed. Install with: brew install gh"
gh auth status &>/dev/null || error "Not logged in to GitHub. Run: gh auth login"

# Get version
VERSION="${1:-}"
if [ -z "$VERSION" ]; then
    echo -n "Enter version (e.g., v1.0.0): "
    read -r VERSION
fi
[[ "$VERSION" =~ ^v ]] || VERSION="v$VERSION"

echo ""
echo "=========================================="
echo "  Creating GitHub Release: $VERSION"
echo "=========================================="

# Clean and create dist directory
rm -rf "$RELEASE_DIR"
mkdir -p "$RELEASE_DIR"

# Common files
COMMON="key_counter_overlay.py config.txt README.md"

# Create macOS package
info "Building macOS package..."
PKG="$RELEASE_DIR/$APP_NAME-$VERSION-macos"
mkdir -p "$PKG"
cp $COMMON run_counter.sh start.command "$PKG/"
chmod +x "$PKG/run_counter.sh" "$PKG/start.command"
(cd "$RELEASE_DIR" && zip -r "$(basename "$PKG").zip" "$(basename "$PKG")" -x "*.DS_Store")
rm -rf "$PKG"

# Create Linux package
info "Building Linux package..."
PKG="$RELEASE_DIR/$APP_NAME-$VERSION-linux"
mkdir -p "$PKG"
cp $COMMON run_counter.sh "$PKG/"
chmod +x "$PKG/run_counter.sh"
(cd "$RELEASE_DIR" && tar -czvf "$(basename "$PKG").tar.gz" "$(basename "$PKG")")
rm -rf "$PKG"

# Create Windows package
info "Building Windows package..."
PKG="$RELEASE_DIR/$APP_NAME-$VERSION-windows"
mkdir -p "$PKG"
cp $COMMON start.bat "$PKG/"
(cd "$RELEASE_DIR" && zip -r "$(basename "$PKG").zip" "$(basename "$PKG")")
rm -rf "$PKG"

echo ""
info "Packages created:"
ls -lh "$RELEASE_DIR/"

# Create GitHub release
echo ""
info "Creating GitHub release..."

gh release create "$VERSION" \
    --title "$VERSION" \
    --generate-notes \
    "$RELEASE_DIR"/*.zip \
    "$RELEASE_DIR"/*.tar.gz

echo ""
echo "=========================================="
info "Release $VERSION published!"
info "View at: $(gh browse -n)/releases/tag/$VERSION"
echo "=========================================="
