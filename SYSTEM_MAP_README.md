# System Map Pipeline Documentation

## Overview

The `system_map.py` is a modular, AI-friendly file system visualization pipeline that automatically scans your directory structure and generates beautiful, interactive HTML visualizations.

## Features

- 🔍 **Intelligent Scanning**: Automatically categorizes directories based on patterns
- 📊 **Multiple Visualizations**: Pie charts, bar charts, treemaps, and network graphs
- 🎨 **Beautiful Dark Theme**: Consistent dark theme with customizable pastel colors
- 🤖 **AI-Optimized**: Clear purpose tags and modular structure for easy AI editing
- ⚡ **Performance**: Configurable depth and exclusion patterns
- 📱 **Responsive**: Works on all screen sizes

## Installation

No installation required! The script uses standard Python libraries and CDN-hosted JavaScript libraries.

## Usage

### Basic Usage

```bash
# Scan your home directory
python system_map.py ~

# Scan a specific directory
python system_map.py /Users/lech/development_hub

# Specify output location
python system_map.py ~ --output ~/Desktop/my_system_map.html

# Open automatically in browser
python system_map.py ~ --open
```

### Command Line Options

- `path`: Directory to scan (required)
- `--output, -o`: Output HTML file path (default: `path/system_map.html`)
- `--depth, -d`: Maximum directory depth to scan (default: 3)
- `--open`: Open the generated HTML in browser
- `--verbose, -v`: Enable verbose logging

### Examples

```bash
# Full system scan with custom output
python system_map.py ~ --output ~/development_hub/full_system_map.html --depth 4 --open

# Quick project scan
python system_map.py ~/01_projects --depth 2 --open

# Verbose mode for debugging
python system_map.py ~ --verbose
```

## Architecture

The pipeline consists of 5 main modules:

### 1. **Config** (AI_EDIT_POINT)
- Central configuration for all customizable parameters
- Directory exclusion patterns
- Color schemes
- Category detection patterns

### 2. **FileSystemScanner**
- Recursively scans directories
- Calculates sizes and file counts
- Applies exclusion rules
- Categorizes directories

### 3. **DataProcessor**
- Transforms raw scan data
- Aggregates by category
- Prepares visualization-specific formats
- Creates D3 and vis.js compatible data

### 4. **HTMLGenerator**
- Generates complete HTML file
- Embeds all visualization data
- Creates interactive charts
- Applies dark theme styling

### 5. **SystemMapPipeline**
- Orchestrates all modules
- Handles logging
- Manages file I/O

## Customization Guide for AI Agents

### Changing Colors (AI_EDIT_POINT)
Edit the `COLORS` dictionary in the `Config` class:
```python
COLORS = {
    'projects': '#F687B3',    # Pink
    'knowledge': '#63B3ED',   # Blue
    'tools': '#68D391',       # Green
    # Add more categories...
}
```

### Adding Category Patterns (AI_EDIT_POINT)
Edit the `CATEGORY_PATTERNS` in the `Config` class:
```python
CATEGORY_PATTERNS = {
    'projects': ['project', 'app', 'site'],
    'ml_models': ['models', 'ml', 'ai'],  # New category
    # Add more patterns...
}
```

### Excluding Directories
Add to `EXCLUDE_DIRS` in the `Config` class:
```python
EXCLUDE_DIRS = {
    '.git', 'node_modules', 'venv',
    'my_private_folder',  # Add custom exclusions
}
```

### Modifying Visualizations
Each visualization can be customized in the `_generate_html_template` method:
- Chart.js options for pie/bar charts
- D3 settings for treemap
- vis.js options for network graph

## Output

The generated HTML file includes:

### Overview Tab
- Storage distribution pie chart
- Top directories bar chart
- System statistics

### Treemap Tab
- Interactive D3 treemap
- Click to zoom functionality
- Toggle between size/file count views

### Network Tab
- Interactive network visualization
- Shows directory relationships
- Draggable nodes

## Tips

1. **Large Directories**: Use `--depth 2` for faster scans
2. **Exclude Patterns**: Customize `EXCLUDE_DIRS` for your needs
3. **Categories**: Add custom patterns for better categorization
4. **Colors**: Match your terminal or IDE theme
5. **Regular Updates**: Run periodically to track growth

## Troubleshooting

### Permission Errors
- The scanner gracefully handles permission denied errors
- Check logs with `--verbose` flag

### Large File Systems
- Reduce depth with `--depth 2`
- Add more exclusions to `Config`
- Increase `MIN_SIZE_TO_REPORT` threshold

### Browser Issues
- All visualizations use CDN libraries
- Requires internet connection for first load
- Works best in modern browsers

## AI Agent Instructions

When modifying this code:
1. Look for `AI_EDIT_POINT` comments for safe modification areas
2. Check `PURPOSE` tags to understand each section
3. Follow the modular structure - each class has a single responsibility
4. Test with small directories first
5. Use `--verbose` to debug issues

## Future Enhancements

- [ ] Add file type analysis
- [ ] Include git repository detection
- [ ] Add time-based filtering
- [ ] Export to different formats (PDF, PNG)
- [ ] Add real-time monitoring mode
- [ ] Include file content analysis