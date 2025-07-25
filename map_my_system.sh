#!/bin/bash
# System Map Generator - Convenient wrapper script
# Purpose: Easy command to generate system maps

# Default values
DEFAULT_DEPTH=3
DEFAULT_PATH="~"  # Default to home directory
PYTHON_CMD="/opt/homebrew/bin/python3"
# Get the real directory of this script (following symlinks on macOS)
if [ -L "${BASH_SOURCE[0]}" ]; then
    # It's a symlink, resolve it
    REAL_SCRIPT="$(readlink "${BASH_SOURCE[0]}")"
    SCRIPT_DIR="$(cd "$(dirname "$REAL_SCRIPT")" && pwd)"
else
    # Not a symlink
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi
SCRIPT_PATH="$SCRIPT_DIR/system_map.py"

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to show usage
show_usage() {
    echo -e "${BLUE}System Map Generator${NC}"
    echo -e "${GREEN}Usage:${NC}"
    echo "  ./map_my_system.sh [options]          # Map entire home directory (default)"
    echo "  ./map_my_system.sh [path] [options]   # Map specific directory"
    echo ""
    echo -e "${GREEN}Examples:${NC}"
    echo "  ./map_my_system.sh                    # Map entire home directory"
    echo "  ./map_my_system.sh --full --open      # Deep scan of home with auto-open"
    echo "  ./map_my_system.sh ~/projects         # Map specific directory"
    echo "  ./map_my_system.sh . --quick          # Quick scan current directory"
    echo ""
    echo -e "${GREEN}Options:${NC}"
    echo "  --full        Deep scan (depth 4)"
    echo "  --quick       Quick scan (depth 2)"
    echo "  --open        Open in browser after generation"
    echo "  --help        Show this help"
    echo ""
    echo -e "${YELLOW}Default: Maps your entire home directory (~)${NC}"
    echo -e "${YELLOW}Output: Saved to ~/development_hub/PROJECT_map/outputs/${NC}"
    echo -e "${YELLOW}Symlinks: Created in ~/development_hub/.maps/${NC}"
}

# Parse arguments
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
    show_usage
    exit 0
fi

# Check if first argument is a path or an option
if [[ "$1" == "" ]] || [[ "$1" == --* ]]; then
    # No path specified or first arg is an option - use default home directory
    SCAN_PATH="$DEFAULT_PATH"
else
    # Path was specified
    SCAN_PATH="$1"
    shift
fi

# Default options
DEPTH=$DEFAULT_DEPTH
OPEN_FLAG=""

# Parse options
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --full)
            DEPTH=4
            echo -e "${YELLOW}Using full scan (depth 4)${NC}"
            ;;
        --quick)
            DEPTH=2
            echo -e "${YELLOW}Using quick scan (depth 2)${NC}"
            ;;
        --open)
            OPEN_FLAG="--open"
            ;;
        *)
            echo -e "${YELLOW}Unknown option: $1${NC}"
            ;;
    esac
    shift
done

# Expand path
FULL_PATH=$(cd "$SCAN_PATH" 2>/dev/null && pwd || echo "$SCAN_PATH")
FULL_PATH="${FULL_PATH/#\~/$HOME}"  # Expand ~ to home directory

# Create outputs directory if it doesn't exist
OUTPUT_DIR="$SCRIPT_DIR/outputs"
mkdir -p "$OUTPUT_DIR"

# Generate timestamp for unique filename
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Create a safe filename from the path
SAFE_PATH_NAME=$(basename "$FULL_PATH")
if [ "$FULL_PATH" == "$HOME" ]; then
    SAFE_PATH_NAME="home"
fi

OUTPUT_FILE="$OUTPUT_DIR/${TIMESTAMP}_${SAFE_PATH_NAME}.html"

# Run the system map
echo -e "${BLUE}🗺️  Generating system map...${NC}"
echo -e "${GREEN}📂 Scanning:${NC} $FULL_PATH"
echo -e "${GREEN}📊 Depth:${NC} $DEPTH"
echo -e "${GREEN}📄 Output:${NC} $OUTPUT_FILE"
echo ""

# Execute the Python script
$PYTHON_CMD "$SCRIPT_PATH" "$FULL_PATH" \
    --output "$OUTPUT_FILE" \
    --depth "$DEPTH" \
    $OPEN_FLAG

# Create symlinks in development_hub/.maps/ for easy access
if [ $? -eq 0 ]; then
    # Get development_hub directory (parent of PROJECT_map)
    DEV_HUB_DIR="$(dirname "$SCRIPT_DIR")"
    MAP_DIR="$DEV_HUB_DIR/.maps"
    
    # Create .maps directory if it doesn't exist
    mkdir -p "$MAP_DIR"
    
    # Create directory-specific latest link
    LATEST_LINK="$MAP_DIR/${SAFE_PATH_NAME}_latest.html"
    ln -sf "$OUTPUT_FILE" "$LATEST_LINK"
    echo -e "${GREEN}🔗 Latest ${SAFE_PATH_NAME} map:${NC} $LATEST_LINK"
    
    # Create general "latest" link for the most recent scan
    GENERAL_LATEST="$MAP_DIR/latest.html"
    ln -sf "$OUTPUT_FILE" "$GENERAL_LATEST"
    echo -e "${GREEN}🔗 Latest scan:${NC} $GENERAL_LATEST"
fi