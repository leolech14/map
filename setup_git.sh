#!/bin/bash

# Setup Git for PROJECT_map (system_map)

echo "Initializing Git repository for PROJECT_map..."

# Initialize git
git init

# Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# macOS
.DS_Store

# Project specific
outputs/*.html
.maps/

# IDE
.vscode/
.idea/
EOF

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: System file visualization tool

- Python-based file system scanner and visualizer
- Multiple visualization types (treemap, network, charts)
- AI-friendly code with PURPOSE tags
- Zero dependencies (Python standard library only)
- Beautiful dark theme with pastel accents
- Agent OS integration for structured development"

echo "Git repository initialized!"
echo ""
echo "To push to GitHub:"
echo "1. Create a new repo named 'system_map' on GitHub"
echo "2. Run: git remote add origin https://github.com/YOUR_USERNAME/system_map.git"
echo "3. Run: git branch -M main"
echo "4. Run: git push -u origin main"