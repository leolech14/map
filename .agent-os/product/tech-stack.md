# Technical Stack

> Last Updated: 2025-07-25
> Version: 1.0.0

## Core Technologies

### Application Framework
- **Framework:** Python (Standard Library Only)
- **Version:** Python 3.x
- **Language:** Python

### Database
- **Primary:** JSON files (for data storage)
- **Version:** N/A
- **ORM:** None (file-based storage)

## Frontend Stack

### JavaScript Framework
- **Framework:** Vanilla JavaScript
- **Version:** ES6+
- **Build Tool:** None (inline scripts)

### Import Strategy
- **Strategy:** CDN-based libraries
- **Package Manager:** None
- **Node Version:** N/A

### CSS Framework
- **Framework:** Custom CSS
- **Version:** CSS3
- **PostCSS:** No

### UI Components
- **Library:** D3.js (for visualizations)
- **Version:** v7 (via CDN)
- **Installation:** CDN links

## Assets & Media

### Fonts
- **Provider:** System fonts
- **Loading Strategy:** font-family fallbacks

### Icons
- **Library:** None (using Unicode symbols)
- **Implementation:** Direct Unicode characters

## Visualization Libraries

### D3.js
- **Purpose:** Interactive treemap and network visualizations
- **Loading:** CDN (https://d3js.org/d3.v7.min.js)

### Chart Generation
- **Method:** Canvas API + Custom JavaScript
- **Charts:** Pie charts, bar charts

## Infrastructure

### Application Hosting
- **Platform:** Local file system
- **Service:** Static HTML files
- **Region:** N/A

### Database Hosting
- **Provider:** Local file system
- **Service:** JSON outputs
- **Backups:** Timestamped file versioning

### Asset Storage
- **Provider:** Local file system
- **CDN:** External CDNs for D3.js
- **Access:** File system permissions

## Deployment

### CI/CD Pipeline
- **Platform:** None (local tool)
- **Trigger:** Manual execution
- **Tests:** None currently

### Environments
- **Production:** User's local system
- **Staging:** N/A
- **Review Apps:** N/A

## Shell Integration

### Wrapper Scripts
- **map_my_system.sh:** Bash wrapper for easy execution
- **view_map:** Quick viewer for generated maps
- **map_system:** Symlinked convenience command

### Python Execution
- **Path:** /opt/homebrew/bin/python3 (configurable)
- **Dependencies:** None (standard library only)

## Code Architecture

### Design Patterns
- **Scanner:** FileSystemScanner class for traversal
- **Processor:** DataProcessor for analysis
- **Generator:** HTMLGenerator for output
- **Pipeline:** SystemMapPipeline orchestrator

### Configuration
- **Method:** Config class with constants
- **Customization:** Direct code modification
- **AI Markers:** AI_EDIT_POINT and PURPOSE tags

## Output Format

### HTML Structure
- **Template:** Embedded in Python code
- **Styling:** Inline CSS in <style> tags
- **Scripts:** Inline JavaScript
- **Responsive:** Yes, with media queries

### Data Storage
- **Format:** JSON embedded in HTML
- **Location:** PROJECT_map/outputs/
- **Naming:** YYYY-MM-DD_HH-MM-SS_*.html

## Development Tools

### Code Style
- **Python:** PEP 8 compliant
- **Comments:** PURPOSE tags for AI understanding
- **Structure:** Class-based modular design

### Logging
- **Library:** Python logging module
- **Levels:** INFO, WARNING, ERROR
- **Output:** Console with color coding