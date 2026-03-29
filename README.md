# 🧠 Multi-Agent Memory (MAM)

> Persistent knowledge system for multi-agent development. One `/memory` directory, shared by every AI.

[![Agent Skills Spec](https://img.shields.io/badge/agent--skills-v1.0-blue)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Install with npx](https://img.shields.io/badge/npx-skills%20add-black)](https://skills.sh)

**MAM** solves the **Context Amnesia** problem — the loss of critical design decisions, architecture choices, and business rules that happens when multiple AI agents (Claude, Gemini, Cursor, Codex, etc.) work asynchronously on the same codebase.

It creates a `/memory` directory in your project that serves as the **shared source of truth** for any AI agent.

---

## Install the Skill

### One-command install (recommended)

```bash
# Auto-detects your agents and installs for all of them
npx skills add pedrollcs/multi-agent-memory
```

### Antigravity

```bash
npx skills add pedrollcs/multi-agent-memory -a antigravity
```

Or manually:

```bash
git clone https://github.com/pedrollcs/multi-agent-memory.git
cp -r multi-agent-memory/multi-agent-memory/ ~/.antigravity/skills/multi-agent-memory/
```

### Claude Code

```bash
# Project-level (shared via git)
npx skills add pedrollcs/multi-agent-memory -a claude-code

# Global (all your projects)
npx skills add pedrollcs/multi-agent-memory -a claude-code -g
```

Or manually:

```bash
# Project-level
cp -r multi-agent-memory/ .claude/skills/multi-agent-memory/

# Global
cp -r multi-agent-memory/ ~/.claude/skills/multi-agent-memory/
```

### Other Agents

The skill follows the [Agent Skills spec](https://agentskills.io) — it works with any compatible agent:

```bash
# Codex
npx skills add pedrollcs/multi-agent-memory -a codex

# Cursor
npx skills add pedrollcs/multi-agent-memory -a cursor

# GitHub Copilot
npx skills add pedrollcs/multi-agent-memory -a github-copilot

# All agents at once
npx skills add pedrollcs/multi-agent-memory --agent '*'
```

---

## Initialize Memory in Your Project

After installing the skill, create the `/memory` directory in your project:

```bash
# Using the mam CLI
mam init

# Or using the script directly
python3 multi-agent-memory/scripts/init_memory.py .
```

Then fill in your project context:
1. Edit `memory/project/context.md` — product, stack, conventions
2. Edit `memory/project/arch.md` — folder structure, architecture
3. Edit `memory/project/design.md` — design tokens, UI rules
4. Remove the example features (`auth.md`, `proposals.md`)
5. Instruct your agents to check `/memory` at the start of every session

---

## How It Works

```
                    ┌─────────────┐
                    │  /memory    │
                    │  (Source of │
                    │   Truth)    │
                    └──────┬──────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
      ┌─────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐
      │  Claude   │ │Antigravity│ │  Codex    │
      │           │ │           │ │           │
      │ CHECK-IN  │ │ CHECK-IN  │ │ CHECK-IN  │
      │ (read)    │ │ (read)    │ │ (read)    │
      │           │ │           │ │           │
      │ EXECUTE   │ │ EXECUTE   │ │ EXECUTE   │
      │           │ │           │ │           │
      │ CHECK-OUT │ │ CHECK-OUT │ │ CHECK-OUT │
      │ (write)   │ │ (write)   │ │ (write)   │
      └───────────┘ └───────────┘ └───────────┘
```

Every agent follows the **Check-in / Check-out Protocol**:

1. **🟢 CHECK-IN:** Read `index.md` → load only relevant memory files → understand context
2. **🟡 EXECUTE:** Build the feature, tracking decisions made along the way
3. **🔴 CHECK-OUT:** Update or create memory files → update index → persist knowledge

---

## Memory Structure

```
/memory
├── readme.md          # Protocol rules for AI agents
├── index.md           # Context router — agents read this FIRST
├── /project           # Structural context (rarely changes)
│   ├── context.md     # Business overview, tech stack, conventions
│   ├── arch.md        # Architecture, folder structure, deploy
│   └── design.md      # Design system: tokens, components, UI rules
└── /features          # Granular context per feature (changes often)
    ├── auth.md        # Authentication & authorization history
    ├── billing.md     # Payment system decisions and state
    └── ...
```

The system follows **progressive disclosure** — agents load only what they need:

| Level | When | What |
|---|---|---|
| Router | Always first | `index.md` — which files matter for this task |
| Structural | First interaction | `project/*.md` — loaded once per session |
| Feature | On demand | `features/*.md` — only when relevant |

---

## MAM CLI

The `mam` command wraps the utility scripts into a clean interface.

### Setup

```bash
# Option 1: Symlink (recommended)
chmod +x bin/mam
sudo ln -sf "$(pwd)/bin/mam" /usr/local/bin/mam

# Option 2: Shell alias
echo 'alias mam="/path/to/multi-agent-memory/bin/mam"' >> ~/.bashrc
source ~/.bashrc

# Option 3: Add to PATH
export PATH="$PATH:/path/to/multi-agent-memory/bin"
```

### Commands

```bash
mam init [path]       # Initialize /memory in a project (default: current dir)
mam validate [path]   # Check consistency (links, quality, security)
mam regen [path]      # Regenerate index.md from existing files
mam status [path]     # Quick overview of all features and their status
mam help              # Show help
```

### Examples

```bash
# Start a new project with memory
cd ~/my-project
mam init

# Check if everything is consistent
mam validate

# After adding new features manually, rebuild the index
mam regen

# Quick look at what's documented
mam status
```

`mam validate` checks 5 dimensions:
- **Structure** — required files and directories exist
- **Consistency** — all index.md links point to real files, all features are indexed
- **Quality** — feature files contain required sections (Status, Resumo, Decisões)
- **Size** — no file exceeds the 500-line recommendation
- **Security** — no credentials or API keys leaked in memory files

---

## Skill Structure

```
multi-agent-memory/
├── SKILL.md                          # Skill instructions (loaded when triggered)
├── references/
│   └── writing-guide.md              # How to write good memories (loaded on demand)
├── scripts/
│   ├── init_memory.py                # Initialize /memory in a project
│   ├── validate.py                   # Validate memory consistency
│   └── regen_index.py                # Regenerate index.md
└── assets/templates/                 # Templates copied during init
    ├── readme.md                     # Protocol rules for agents
    ├── index.md                      # Context router template
    ├── project/{context,arch,design}.md
    └── features/{_template,auth,proposals}.md
```

---

## Spec Compliance

This skill follows the [Agent Skills specification](https://agentskills.io) (Anthropic, December 2025).

| Requirement | Status |
|---|---|
| YAML frontmatter (name, description) | ✅ |
| Progressive disclosure (3-level loading) | ✅ |
| SKILL.md body < 500 lines | ✅ (157 lines) |
| Description in third person | ✅ |
| Positive + negative triggers | ✅ |
| `scripts/` directory | ✅ |
| `references/` directory | ✅ |
| Cross-platform (Antigravity, Claude Code, Codex, Cursor, Copilot) | ✅ |

---

## License

MIT — see [LICENSE](LICENSE).

---

*Built to orchestrate knowledge in the age of AI-assisted software engineering.*
