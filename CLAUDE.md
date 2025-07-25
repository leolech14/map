# CLAUDE.md - PROJECT_map Context

## Agent OS Documentation

### Product Context
- **Mission & Vision:** @.agent-os/product/mission.md
- **Technical Architecture:** @.agent-os/product/tech-stack.md
- **Development Roadmap:** @.agent-os/product/roadmap.md
- **Decision History:** @.agent-os/product/decisions.md

### Development Standards
- **Code Style:** @~/.agent-os/standards/code-style.md
- **Best Practices:** @~/.agent-os/standards/best-practices.md

### Project Management
- **Active Specs:** @.agent-os/specs/
- **Spec Planning:** Use `@~/.agent-os/instructions/create-spec.md`
- **Tasks Execution:** Use `@~/.agent-os/instructions/execute-tasks.md`

## Workflow Instructions

When asked to work on this codebase:

1. **First**, check @.agent-os/product/roadmap.md for current priorities
2. **Then**, follow the appropriate instruction file:
   - For new features: @.agent-os/instructions/create-spec.md
   - For tasks execution: @.agent-os/instructions/execute-tasks.md
3. **Always**, adhere to the standards in the files listed above

## Important Notes

- Product-specific files in `.agent-os/product/` override any global standards
- User's specific instructions override (or amend) instructions found in `.agent-os/specs/...`
- Always adhere to established patterns, code style, and best practices documented above.

## Project-Specific Context

### Quick Commands

```bash
# Generate a system map (from development_hub)
./map_system                    # Map entire home directory
./map_system --full --open      # Deep scan with auto-open
./map_system . --quick          # Quick scan current directory

# View latest map
./view_map                      # Opens latest scan
./view_map list                 # Show available maps

# From within PROJECT_map directory
./map_my_system.sh              # Same as map_system
python3 system_map.py ~/path    # Direct Python usage
```

### Key Design Principles

1. **Zero Dependencies**: Uses only Python standard library
2. **AI-Friendly**: Code includes PURPOSE tags and AI_EDIT_POINT markers
3. **Self-Contained**: HTML outputs include all CSS/JS inline
4. **Beautiful Output**: Dark theme with pastel accents

### Code Modification Guidelines

When modifying system_map.py:
- Look for `AI_EDIT_POINT` markers for safe modification areas
- Read `PURPOSE:` comments to understand each section
- Maintain the modular class structure
- Keep all visualizations self-contained (no external dependencies)
- Test with both small and large directories

### Common Customizations

1. **Change color scheme**: Modify `Config.COLORS`
2. **Add file categories**: Update `Config.CATEGORY_PATTERNS`
3. **Exclude directories**: Add to `Config.EXCLUDE_DIRS`
4. **Adjust chart styles**: Edit methods in `HTMLGenerator`

### Testing

```bash
# Quick test on current directory
python3 system_map.py . --depth 2 --open

# Full test on home directory
python3 system_map.py ~ --depth 3 --verbose

# Test specific features
python3 system_map.py ~/Downloads --output test.html --open
```

### Output Locations

- **Generated maps**: `PROJECT_map/outputs/YYYY-MM-DD_HH-MM-SS_*.html`
- **Latest symlinks**: `~/.maps/latest.html` and `~/.maps/{dirname}_latest.html`
- **Logs**: Console output (use --verbose for details)