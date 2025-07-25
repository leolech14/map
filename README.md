# 🗺️ PROJECT_map - System File Visualization Tool

> A powerful, AI-friendly file system mapping and visualization tool that creates beautiful, interactive HTML reports of your directory structure.

## 📁 Project Structure

```
PROJECT_map/
├── README.md                    # This file
├── SYSTEM_MAP_README.md        # Detailed documentation
├── system_map.py               # Main Python pipeline
├── map_my_system.sh           # Convenient shell wrapper
├── outputs/                    # Generated maps saved here
│   └── YYYY-MM-DD_HH-MM-SS_*.html  # Timestamped scan files
└── examples/                   # Example outputs
    ├── test_system_map.html    # Example scan of development_hub
    ├── file_system_complete_visualization.html  # Full system visualization
    └── file_system_map.md      # Markdown format example

Note: Symlinks are stored in `~/development_hub/.maps/` (hidden directory)
```

## 🚀 Quick Start

### Easy Mode (Shell Script)

```bash
# From anywhere in development_hub
./map_system                     # Map entire home directory (default)
./map_system --full --open       # Deep scan of home with auto-open
./map_system ~/projects          # Map specific directory
./map_system . --quick           # Quick scan current directory
```

**Note**: By default, running `./map_system` without any arguments will scan your entire home directory!

### Direct Python Usage

```bash
# Basic usage
python3 system_map.py /path/to/scan

# With options
python3 system_map.py ~ --output ~/Desktop/my_map.html --depth 4 --open
```

## 🎯 Features

- **🔍 Intelligent Scanning**: Automatically categorizes directories (projects, tools, knowledge, etc.)
- **📊 Multiple Visualizations**: 
  - Storage distribution pie charts
  - Top directories bar charts
  - Interactive D3 treemap
  - Network relationship graph
- **🎨 Beautiful Dark Theme**: Professional dark theme with pastel accent colors
- **🤖 AI-Optimized Code**: Clear purpose tags and modular structure for easy AI modification
- **⚡ Performance**: Configurable scanning depth and smart exclusion patterns
- **📱 Responsive Design**: Works on all screen sizes

## 📊 Visualization Types

### 1. Overview Tab
- **Pie Chart**: Shows storage distribution by category
- **Bar Chart**: Displays largest directories
- **Statistics**: Total size, file count, scan date

### 2. Treemap Tab
- **Interactive**: Click any box to zoom in
- **Dual Views**: Toggle between size and file count
- **Tooltips**: Hover for detailed information

### 3. Network Tab
- **Relationship Graph**: Shows connections between directories
- **Draggable Nodes**: Rearrange for better viewing
- **Size Visualization**: Node size represents storage usage

## 🛠️ Customization

### For Developers/AI Agents

The code includes special markers for easy customization:

- **`AI_EDIT_POINT`**: Safe areas to modify
- **`PURPOSE`**: Explains what each section does
- **`AI_CONTEXT`**: Additional context for AI agents

### Common Customizations

1. **Change Colors**: Edit `Config.COLORS` in `system_map.py`
2. **Add Categories**: Modify `Config.CATEGORY_PATTERNS`
3. **Exclude Directories**: Add to `Config.EXCLUDE_DIRS`
4. **Adjust Styling**: Modify HTML template in `HTMLGenerator`

## 📋 Command Reference

### Shell Script Options
- `--full`: Deep scan (depth 4)
- `--quick`: Quick scan (depth 2)
- `--open`: Auto-open in browser
- `--help`: Show usage

### Python Script Options
- `path`: Directory to scan (required)
- `--output, -o`: Output file path
- `--depth, -d`: Max scan depth (default: 3)
- `--open`: Open in browser
- `--verbose, -v`: Detailed logging

## 🎨 Example Use Cases

1. **Regular System Monitoring**
   ```bash
   # Weekly full system scan
   ./map_my_system.sh ~ --full
   ```

2. **Project Documentation**
   ```bash
   # Document project structure
   python3 system_map.py ~/my-project --output ./docs/structure.html
   ```

3. **Quick Directory Analysis**
   ```bash
   # Fast scan for large directories
   ./map_my_system.sh /Users/lech/Downloads --quick --open
   ```

## 🔧 Troubleshooting

- **Permission Errors**: The scanner handles these gracefully
- **Large Directories**: Use `--quick` or reduce depth
- **Missing Visualizations**: Requires internet for CDN libraries

## 📚 More Information

See `SYSTEM_MAP_README.md` for:
- Detailed architecture documentation
- AI modification guide
- Advanced customization
- Module explanations

## 🌟 Tips

1. Generated files include timestamps for history tracking
2. Symlinks in `.maps/` directory point to latest scans
3. Use `--verbose` to debug any issues
4. Regular scans help track directory growth over time
5. Access latest scan with `./view_map` command

---

*Created by Leonardo Lech | AI-Friendly Design | Dark Theme with Style*