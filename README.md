# 🧠 Multi-Agent Memory (MAM)

> Persistent knowledge system for projects developed by multiple AI agents.

[![Agent Skills Spec](https://img.shields.io/badge/agent--skills-v1.0-blue)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/works%20with-Claude%20%7C%20Codex%20%7C%20Cursor%20%7C%20Copilot-purple)]()

**Multi-Agent Memory (MAM)** solves the **Context Amnesia** problem. When different AIs (Claude, Gemini, Cursor, ChatGPT, Codex, etc.) work asynchronously on the same project, critical design decisions, architecture choices, and business rules get lost — leading to rework, inconsistencies, and wasted tokens.

MAM creates a `/memory` directory in your project that serves as the **shared source of truth** for any AI agent.

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
      │  Claude   │ │  Cursor   │ │  Codex    │
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

## Installation

### As an Agent Skill (recommended)

Install the skill so your AI agent automatically follows the MAM protocol:

**Claude Code:**
```bash
# Project-level (shared via git)
cp -r skills/memory-manager/ .claude/skills/memory-manager/

# Personal (all projects)
cp -r skills/memory-manager/ ~/.claude/skills/memory-manager/
```

**OpenAI Codex:**
```bash
cp -r skills/memory-manager/ .codex/skills/memory-manager/
```

**GitHub Copilot / VS Code:**
```bash
cp -r skills/memory-manager/ .github/skills/memory-manager/
```

**Cursor:**
```bash
cp -r skills/memory-manager/ .cursor/skills/memory-manager/
```

**Any other agent supporting the [Agent Skills spec](https://agentskills.io):**
Copy to the agent's skill directory. The format is cross-platform.

### Initialize Memory in Your Project

After installing the skill, initialize the `/memory` directory:

```bash
# Via script
python skills/memory-manager/scripts/init_memory.py .

# Or manually
cp -r skills/memory-manager/assets/templates/ ./memory/
```

Then fill in the project context:
1. Edit `memory/project/context.md` — product info, tech stack, conventions
2. Edit `memory/project/arch.md` — folder structure, architecture patterns
3. Edit `memory/project/design.md` — design tokens, components, UI rules
4. Remove example features in `memory/features/` (auth.md, proposals.md)

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
    ├── payments.md    # Payment system decisions and state
    └── ...
```

### Progressive Disclosure

The system follows the same progressive disclosure pattern used by the Agent Skills spec:

| Level | When Loaded | What |
|---|---|---|
| Router | Always first | `index.md` — identifies which files are relevant |
| Structural | First interaction | `project/*.md` — loaded once per session |
| Feature | On demand | `features/*.md` — loaded only when relevant |

This means agents use tokens efficiently — they never read everything, only what they need.

---

## Scripts

| Script | Purpose |
|---|---|
| `scripts/init_memory.py <path>` | Initialize /memory in a project |
| `scripts/validate.py <path>` | Validate memory consistency (links, structure, quality, security) |
| `scripts/regen_index.py <path>` | Regenerate index.md from existing files |

---

## Benefits

- **Token efficiency:** Agents don't need to read the entire codebase to understand progress
- **Design continuity:** Prevents new agents from ignoring established patterns
- **Decision audit trail:** Records the "why" behind decisions — something code alone doesn't explain
- **Hybrid collaboration:** Smooth handoffs between humans and AIs
- **Cross-platform:** Works with any AI agent that supports SKILL.md (Claude, Codex, Cursor, Copilot, etc.)

---

## Spec Compliance

This skill follows the [Agent Skills specification](https://agentskills.io) published by Anthropic (December 2025). It is compatible with any platform that supports the SKILL.md format.

| Feature | Status |
|---|---|
| YAML frontmatter (name, description) | ✅ |
| Progressive disclosure (3-level loading) | ✅ |
| Scripts directory | ✅ |
| References directory | ✅ |
| Cross-platform compatibility | ✅ |
| Negative triggers in description | ✅ |
| Under 500 lines SKILL.md body | ✅ |

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

*Built to orchestrate knowledge in the age of AI-assisted software engineering.*
