# High Impact Frontend Design

**A Claude Code plugin that makes AI-generated frontends actually look designed.**

Every AI coding tool produces the same output: Inter font, grey cards, flat rectangles, zero atmosphere. This plugin fixes that — systematically.

---

## The Problem

Ask any AI to "build me a landing page" and you'll get:
- **Inter or Roboto** (every time)
- Grey-on-white cards with rounded corners
- No visual personality, no atmosphere, no design point of view
- Output that screams "AI made this"

The model isn't incapable of good design. It just defaults to safe, generic choices because nothing pushes it to commit.

## The Fix

This plugin adds a structured design workflow that forces real design decisions before a single line of code is written:

1. **A conceptual anchor** — not "modern and clean" but "editorial magazine layout with serif authority and muted earth tones"
2. **Data-driven font selection** — 1,500+ Google Fonts scored across 20 mood dimensions, with popularity weighting so the agent trusts and uses what's recommended
3. **A design plan** — fonts, colors, layout, atmosphere, responsive strategy — all decided and approved before building starts
4. **Anti-rationalization enforcement** — every shortcut the model might take has a pre-written counter-argument

The result: distinctive output that looks like a human designer made intentional choices.

---

## Before & After

| | Without Plugin | With Plugin |
|---|---|---|
| **Fonts** | Inter + system sans | Ubuntu + Saira Condensed (mood-matched) |
| **Personality** | Generic corporate | Specific to the project's audience |
| **Atmosphere** | Flat rectangles | Gradients, textures, depth, motion |
| **Score** | 43% on design assertions | **100%** on design assertions |

*Based on 6 blind evaluations across law firms, SaaS products, conferences, fashion, kids apps, and cybersecurity.*

---

## Install

```bash
claude plugin add highimpact-dev/highimpact-frontend-skill
```

## Usage

Just ask Claude to build something. The skill triggers automatically.

```
> Build me a landing page for a Nashville law firm
> I need an event registration page for a tech conference
> Create a pricing page for my SaaS product
```

### Flags

- `--setup` — First-time setup wizard. Detects your tools, explains what's missing, gives install commands.
- `--walkthrough` — Interactive guided tour. Good for understanding what the skill does before using it.

---

## How It Works

### 1. Discovery
Detects your project: framework (Next.js, Vite, plain HTML), component library (shadcn, Radix), existing design system (CSS variables, Tailwind config). Asks only what it can't detect.

### 2. Design Plan
The creative phase. Creates a **conceptual anchor** (a metaphor that drives all visual decisions), runs the **font selector**, picks specific colors with hex values, plans the page structure, responsive strategy, and 1-2 signature interactions.

You approve the plan before any code is written.

### 3. Staged Build
A subagent builds in 4 verified stages:

| Stage | What | Verified Against |
|---|---|---|
| Structure | Semantic HTML, real content, every section | Plan's page structure |
| Typography | Font imports, CSS variables, color palette | Plan's visual choices |
| Layout | Grid/flex, responsive breakpoints, mobile-first | Plan's responsive strategy |
| Atmosphere | Gradients, textures, animations, polish | Plan's conceptual anchor |

### 4. Live Testing
Renders in a real browser (if Chrome DevTools or Playwright available). Screenshots at mobile (375px), tablet (768px), and desktop (1280px). Checks for overflow, font loading, console errors, and interaction behavior.

### 5. Design Review & Ship
A review agent compares the output against the plan. A quality gate runs final checks. You decide when it ships.

---

## Font Selector

The secret weapon. Instead of guessing fonts from training data, the skill queries **Google Fonts' own mood/personality tag dataset** — 1,502 fonts scored across 20 expressive dimensions.

```bash
node scripts/select-fonts.mjs '{"Futuristic": 80, "Competent": 70, "Active": 60}'
```

### Mood Dimensions
`Active` · `Artistic` · `Awkward` · `Business` · `Calm` · `Childlike` · `Competent` · `Cute` · `Excited` · `Fancy` · `Futuristic` · `Happy` · `Innovative` · `Loud` · `Playful` · `Rugged` · `Sincere` · `Sophisticated` · `Stiff` · `Vintage`

### How Scoring Works

Each font is scored on:
- **Mood alignment** — how well its personality tags match your project's mood profile
- **Popularity** — a percentile from Google Fonts metadata (ensures the agent recognizes and trusts the recommendation)
- **Category contrast** — pairings maximize visual contrast (serif + sans, or different structural subcategories)

### Banned Defaults
These are auto-excluded — they're not bad fonts, they're just what every AI defaults to:

Inter · Roboto · Open Sans · Poppins · Montserrat · DM Sans · Lato · Nunito · Nunito Sans · Raleway · Source Sans 3 · Work Sans · Rubik · Manrope · Plus Jakarta Sans

---

## Architecture

```
Plugin
├── Orchestrator (SKILL.md)        ← Creative direction, user conversation
├── Font Selector (select-fonts.mjs) ← Data-driven font recommendations
├── Builder Agent (Sonnet)          ← 4-stage code generation
├── Tester Agent (Sonnet)           ← Browser rendering + screenshots
├── Reviewer Agent (Haiku)          ← Plan compliance check
└── Gate Agent (Haiku)              ← Pre-ship quality verification
```

The orchestrator stays in your conversation context for creative decisions. Heavy work (building, testing, reviewing) runs in subagents on cost-efficient models with fresh context.

---

## Anti-Rationalization

The highest-leverage pattern in this skill. AI models are excellent at justifying shortcuts. Every escape route has a pre-written counter:

| The Model Says | The Skill Says |
|---|---|
| "Inter is clean and readable" | It's the default. Defaults aren't design. |
| "I'll simplify the responsive strategy" | Build what was planned. Mobile-first, every breakpoint. |
| "This animation is too complex" | The signature moment is what makes it screenshot-worthy. |
| "I'll skip the texture/grain/atmosphere" | That's what separates designed from generic. |
| "The user just wants code fast" | A 15-line plan takes 30 seconds to read. A wrong-direction rebuild takes 10 minutes. |

---

## Requirements

- **Claude Code** — the CLI tool from Anthropic
- **Node.js** — for the font selector (already required by Claude Code)
- **Optional**: Chrome DevTools MCP or Playwright for live browser testing

## License

See LICENSE.txt for complete terms.
