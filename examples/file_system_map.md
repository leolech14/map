# Complete File System Map - Leonardo's MacBook Air

## System Overview
- **Total Home Directory Size**: ~25GB of user-controlled data
- **Organization Method**: GTD-inspired numbered system + project-based structure
- **Primary Focus**: AI/ML development, automation, knowledge management

---

## 🗺️ ROOT LEVEL DIRECTORIES (/)

### System Directories (macOS Controlled) 🔒
```
/Applications        - Installed applications
/System             - Core macOS system files
/Library            - System-wide resources
/private            - System private data
/usr                - Unix system resources
/bin, /sbin         - System binaries
/dev                - Device files
/cores              - Core dumps
/opt                - Optional software
/Volumes            - Mounted drives
```

### User-Accessible Directory 🔓
```
/Users              - User home directories
  └── /lech         - Your home directory (primary workspace)
```

---

## 📁 HOME DIRECTORY STRUCTURE (/Users/lech)

### 🎯 Main Organization System (Numbered Directories)

#### 01_projects/ (11GB) - Active Project Repository
```
01_projects/
├── active/              - Currently working projects
├── archive/             - Completed/paused projects
├── incubation/          - Ideas and early-stage projects
└── multi-agent-dashboard/ - Major active project
```

#### 02_knowledge/ (2.3GB) - Knowledge Management Hub
```
02_knowledge/
├── ai_systems/          - AI/ML related knowledge
├── kbvault/            - Knowledge base vault
├── llmfy/              - LLM integration system
├── moneyAI/            - Financial AI knowledge
├── personal_wiki/      - Personal documentation
├── software_dev/       - Development resources
├── software_engineering/ - Engineering best practices
└── specialist_system/  - Specialized knowledge systems
```

#### 03_tools/ (1.4GB) - Development Tools & Utilities
```
03_tools/
├── AssetGeneratorApp/   - Asset generation tool
├── automation_scripts/  - Automation utilities
├── axiom_guardian/      - Security/monitoring tool
├── browser-use/         - Browser automation
├── cli_tools/          - Command line utilities
├── gemini-95-macos/    - Gemini AI integration
├── n8n/                - Workflow automation
├── n8n-mcp-server/     - n8n MCP integration
├── shell-mcp-server/   - Shell MCP integration
├── system_config/      - System configurations
├── system-mapping/     - System analysis tools
└── wptkai-cytoscape/   - Visualization tools
```

#### 04_assets/ (467MB) - Media & Resources
```
04_assets/
├── documents/          - Important documents
├── images/            - Image resources
├── loyalty-programs/  - Program documentation
├── media/             - Various media files
├── templates/         - Reusable templates
└── tunnelin_money/    - Financial assets
```

#### 04_tools/ (2.3GB) - Additional Tools [DUPLICATE NUMBERING]
```
04_tools/
├── html/                    - HTML tools and editors
├── knowledge-base-system/   - KB management
├── mermaid-editor/         - Diagram creation
├── n8n-embedding-mcp/      - Advanced n8n integration
└── pipedream/              - Workflow automation
```

#### 05_communication/ (12KB) - Communication Archive
```
05_communication/
├── archive/            - Archived communications
├── drafts/            - Draft messages
└── sent/              - Sent items
```

#### 99_inbox/ - Temporary Storage & Downloads
```
99_inbox/
├── automation/         - Temporary automation files
├── data/              - Temporary data storage
├── downloads/         - Downloaded files
├── screenshots/       - Screenshot storage
├── staging/           - Files being processed
├── temp/              - Temporary files
└── workflows/         - Workflow exports
```

### 🚀 Major Project Directories

#### Active Development Projects
```
lechworld/             (444MB) - Personal brand/portfolio site
├── client/            - Frontend code
├── server/            - Backend services
├── shared/            - Shared utilities
└── dist/              - Build output

milhaslech/           (470MB) - Financial tracking project
├── backend/           - API services
├── frontend/          - UI application
├── tests/            - Test suites
└── venv/             - Python environment

tunnelin_money/       (608MB) - Financial application
├── src/              - Source code
├── public/           - Public assets
├── build/            - Build artifacts
└── supabase/         - Database integration

html/                 (171MB) - HTML projects hub
├── repos/            - HTML repositories
├── scripts/          - Utility scripts
└── src/              - Source files
```

### 🛠️ Development Workspaces

```
development_hub/       - Primary development workspace
├── .agent-os/        - Agent OS integration
├── .claude/          - Claude configurations
├── .cursor/          - Cursor IDE settings
├── inbox/            - Development inbox
├── permissions/      - Access control
├── PROJECT_html/     - HTML project workspace
└── screenshots@      - Symlink to /screenshots

development_hub2/     - Secondary workspace
└── [Similar structure to development_hub]
```

### 🔧 Configuration Directories (Hidden)

#### AI/LLM Tools
```
.claude/              - Claude AI configurations
.claude-code/         - Claude Code settings
.cursor/              - Cursor IDE
.ollama/              - Ollama LLM
.gemini/              - Google Gemini
.agent-os/            - Agent OS framework
```

#### Development Tools
```
.docker/              - Docker configurations
.n8n/                 - n8n automation
.fly/                 - Fly.io deployment
.mcp-auth/            - MCP authentication
.doppler/             - Secret management
```

#### Package Managers
```
.npm/                 - Node.js packages
.cargo/               - Rust packages
.gem/                 - Ruby gems
.bun/                 - Bun runtime
.rustup/              - Rust toolchain
```

### 📊 Special Directories

```
credential_vault/     - Secure credential storage
├── config/          - Configuration files
├── keys/            - API keys and secrets
├── scripts/         - Security scripts
└── docs/            - Documentation

Desktop/             - Traditional desktop (actively used)
├── App Icons/       - Application icons
├── Cursor Playground/ - IDE experiments
├── life-database/   - Personal database project
└── [Various screenshots and documents]

Downloads/           - Browser downloads
├── [Various project exports]
├── notion_export_temp/
└── [Temporary downloads]
```

### 🔗 Symbolic Links
```
/Users/lech/development_hub/screenshots -> /Users/lech/screenshots
```

---

## 📈 Storage Analysis

### By Size (Largest First)
1. **01_projects/** - 11GB (44% of user data)
2. **02_knowledge/** - 2.3GB (9%)
3. **04_tools/** - 2.3GB (9%)
4. **03_tools/** - 1.4GB (6%)
5. **Individual projects** - 400-600MB each
6. **Configuration dirs** - Variable (mostly small)

### By Activity
- **Most Active**: development_hub, 01_projects/active
- **Moderate**: 02_knowledge, Desktop
- **Archival**: 01_projects/archive, 05_communication

---

## 🎯 Organization Insights

### Strengths
1. **Clear GTD-based numbering** - Easy to understand priority/category
2. **Project isolation** - Each major project has its own directory
3. **Tool centralization** - Development tools organized by purpose
4. **Knowledge management** - Dedicated space for documentation

### Areas for Improvement
1. **Duplicate numbering** - Two "04" directories (tools vs assets)
2. **Desktop clutter** - Mix of active projects and screenshots
3. **Multiple dev hubs** - Could consolidate development_hub and development_hub2
4. **Inactive directories** - 05_communication barely used

### Recommendations
1. Rename one of the 04_ directories to 06_
2. Move Desktop projects to 01_projects/active
3. Create automated cleanup for 99_inbox
4. Consolidate development workspaces