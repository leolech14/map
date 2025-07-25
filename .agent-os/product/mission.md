# Product Mission

> Last Updated: 2025-07-25
> Version: 1.0.0

## Pitch

PROJECT_map is a powerful file system visualization tool that helps developers, system administrators, and AI agents understand and analyze directory structures by providing beautiful, interactive HTML reports with multiple visualization types.

## Users

### Primary Customers

- **Developers**: Need to understand complex project structures and dependencies
- **System Administrators**: Monitor disk usage and directory organization
- **AI Agents**: Require structured file system understanding for code analysis

### User Personas

**Developer Dan** (25-40 years old)
- **Role:** Software Developer
- **Context:** Working on large codebases with complex structures
- **Pain Points:** Hard to visualize project organization, difficult to find large directories
- **Goals:** Quickly understand new codebases, identify storage issues

**Admin Alice** (30-50 years old)
- **Role:** System Administrator
- **Context:** Managing multiple servers and user directories
- **Pain Points:** Manual disk usage analysis is time-consuming, hard to spot growth trends
- **Goals:** Monitor disk usage efficiently, identify problem areas quickly

**AI Assistant** (N/A)
- **Role:** Code Analysis Agent
- **Context:** Analyzing codebases for understanding and modification
- **Pain Points:** Need structured data about file systems, require clear categorization
- **Goals:** Programmatically understand directory structures, identify project types

## The Problem

### Complex Directory Navigation

Modern file systems contain thousands of files and directories, making it difficult to understand structure and relationships. Traditional tools like `tree` or `du` provide text-only output that's hard to parse visually.

**Our Solution:** Interactive HTML visualizations with multiple views (treemap, network, charts)

### Storage Analysis Blindness

Users don't know where their disk space is being consumed until it's too late. Finding large directories requires manual command-line work.

**Our Solution:** Automatic size calculations with visual representations and category analysis

### AI-Unfriendly Code

Most file system tools aren't designed for AI modification or integration. Code is often monolithic and hard to extend.

**Our Solution:** AI-optimized code with clear markers, modular design, and purposeful documentation

## Differentiators

### Beautiful Dark Theme UI

Unlike command-line tools that produce plain text, we provide a professional dark theme with pastel accents. This results in reports that are presentation-ready and easy on the eyes.

### AI-First Design

Unlike traditional utilities, our code includes AI_EDIT_POINT markers and PURPOSE tags. This results in code that AI agents can easily understand and modify.

### Zero Dependencies

Unlike tools that require complex installations, PROJECT_map uses only Python standard library. This results in easy deployment and no dependency conflicts.

## Key Features

### Core Features

- **Intelligent Scanning:** Automatic categorization of directories (projects, tools, knowledge)
- **Multiple Visualizations:** Pie charts, bar charts, interactive treemap, network graph
- **Performance Options:** Configurable depth and exclusion patterns for large systems
- **Beautiful Reports:** Professional dark theme with responsive design

### Convenience Features

- **Shell Wrapper:** Easy command-line interface with sensible defaults
- **Symlink Management:** Automatic creation of "latest" links for quick access
- **Timestamped Outputs:** Historical tracking of system changes
- **View Command:** Quick access to latest scans with `./view_map`

### AI Features

- **Code Markers:** AI_EDIT_POINT and PURPOSE tags throughout
- **Modular Design:** Clear separation of scanning, processing, and generation
- **Configuration Class:** Easy customization of colors, patterns, and behavior
- **Verbose Logging:** Detailed output for debugging and understanding