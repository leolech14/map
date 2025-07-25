#!/bin/bash

echo "Pushing PROJECT_map to GitHub..."

# Ensure we're in the right directory
cd "$(dirname "$0")"

# Check git status
echo "Current git status:"
git status

# Add all changes
git add -A

# Commit with detailed message
git commit -m "Add Agent OS documentation and latest updates

- Added complete Agent OS structure (.agent-os/product/)
- Updated mission.md with product vision
- Created tech-stack.md documenting zero-dependency approach
- Added roadmap.md with 5 development phases
- Documented key decisions in decisions.md
- Added CLAUDE.md for AI agent context
- Maintained AI-friendly code structure with PURPOSE tags"

# Set remote if needed
git remote set-url origin https://github.com/lech/system_map.git 2>/dev/null || \
git remote add origin https://github.com/lech/system_map.git

# Push to main
git branch -M main
git push -u origin main

echo ""
echo "✅ PROJECT_map pushed to https://github.com/lech/system_map"