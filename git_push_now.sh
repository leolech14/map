#!/bin/bash

# Push PROJECT_map to system_map repo

echo "Pushing PROJECT_map to system_map repository..."

# Initialize git if needed
git init

# Add all files
git add -A

# Commit
git commit -m "Add Agent OS documentation and complete project structure

Features:
- System file visualization tool with zero dependencies
- Multiple visualization types (treemap, network, charts)
- AI-friendly code with PURPOSE tags and AI_EDIT_POINT markers
- Beautiful dark theme with pastel accents
- Shell script wrappers for easy usage

Agent OS Integration:
- Complete .agent-os/product/ documentation
- mission.md - Product vision and user personas
- tech-stack.md - Zero-dependency Python architecture
- roadmap.md - 5-phase development plan
- decisions.md - Key architectural decisions
- CLAUDE.md - AI agent context and usage instructions"

# Add remote
git remote add origin https://github.com/lech/system_map.git 2>/dev/null || echo "Remote already exists"

# Push to main
git branch -M main
git push -u origin main

echo "✅ Done! Check https://github.com/lech/system_map"