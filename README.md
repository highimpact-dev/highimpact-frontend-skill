# Frontend Design Skill

A Claude Code plugin for building distinctive, production-grade frontend interfaces.

## What it does

Guides Claude through a structured design workflow — from discovery to shipped output — that consistently produces pages you'd actually screenshot and share. Avoids the generic "AI slop" aesthetic (Inter font, grey cards, no atmosphere) by enforcing opinionated design decisions at every stage.

## Key features

- **Mood-based font selection** — Queries 1,500+ Google Fonts scored across 20 personality dimensions. Picks fonts that match your project's vibe, not whatever the model defaults to.
- **Staged build pipeline** — Structure first, then typography, then layout, then atmosphere. Each stage verifies against the design plan.
- **Anti-rationalization tables** — Closes every escape route the model uses to justify shortcuts ("Inter is clean and readable" → "It's the default. Defaults aren't design.").
- **Subagent architecture** — Orchestrator handles creative direction, builder/tester/reviewer agents handle heavy lifting on cost-efficient models.

## Install

```bash
claude plugin add highimpact-dev/highimpact-frontend-skill
```

## Usage

Just ask Claude to build something:

> "Build me a landing page for a Nashville law firm"

The skill triggers automatically when you ask to build web components, pages, or applications.

Flags:
- `--setup` — First-time setup wizard (detects tools, installs what's missing)
- `--walkthrough` — Interactive guided tour of the skill

## Workflow

1. **Discovery** — Detects your project setup (framework, component library, design system)
2. **Design Plan** — Creates a conceptual anchor, runs font selector, picks colors, plans layout
3. **Staged Build** — Subagent builds in 4 stages (structure → typography → layout → atmosphere)
4. **Live Testing** — Renders in a real browser, screenshots at 3 breakpoints
5. **Design Review** — Compares output against the plan
6. **Ship** — Final quality gate, then you decide

## Font Selector

The font selector (`scripts/select-fonts.mjs`) is the secret weapon. It scores every Google Font against your project's mood profile:

```bash
node scripts/select-fonts.mjs '{"Futuristic": 80, "Competent": 70, "Active": 60}'
```

Dimensions: Active, Artistic, Awkward, Business, Calm, Childlike, Competent, Cute, Excited, Fancy, Futuristic, Happy, Innovative, Loud, Playful, Rugged, Sincere, Sophisticated, Stiff, Vintage

Banned defaults (auto-excluded): Inter, Roboto, Open Sans, Poppins, Montserrat, DM Sans, Lato, and 8 others.

## Requirements

- Claude Code
- Node.js (for font selector — already required by Claude Code)
- Optional: Browser automation tools (Chrome DevTools MCP or Playwright) for live testing
