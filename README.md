# High Impact Frontend Design

**A Claude Code plugin that makes AI-generated frontends actually look designed.**

Every AI coding tool produces the same output: Inter font, grey cards, flat rectangles, zero atmosphere. This plugin fixes that — systematically.

---

## The Problem

Ask any AI to "build me a landing page" and you'll get:
- **Inter or Roboto** (every time)
- Grey-on-white cards with rounded corners
- "Welcome to [Product]. We help you achieve your goals." as the headline
- No visual personality, no atmosphere, no design point of view
- Output that screams "AI made this"

The model isn't incapable of good design. It just defaults to safe, generic choices because nothing pushes it to commit.

## The Fix

This plugin adds a structured design workflow that forces real design decisions before a single line of code is written:

1. **A conceptual anchor** — not "modern and clean" but "editorial magazine layout with serif authority and muted earth tones"
2. **Data-driven font selection** — 1,500+ Google Fonts scored across 20 mood dimensions, with popularity weighting so the agent trusts and uses what's recommended
3. **A dedicated copywriter** — writes every headline, CTA, and paragraph before the builder touches code. Banned patterns block the usual AI filler. The builder uses the copy verbatim.
4. **A design plan** — fonts, colors, layout, atmosphere, responsive strategy — all decided and approved before building starts
5. **A refinement loop** — iterate until you're happy, with every revision agent getting the full ruleset
6. **Project memory** — learns your preferences per project so the next build starts smarter
7. **Anti-rationalization enforcement** — every shortcut the model might take has a pre-written counter-argument

The result: distinctive output that looks like a human designer and copywriter made intentional choices.

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

### 3. Copywriting
A dedicated copywriter agent writes every headline, body paragraph, CTA, and piece of microcopy — before the builder sees any of it. No more "Welcome to [Product]. We help you achieve your goals."

The copy is written to match the design plan's conceptual anchor and tone. A banned patterns list blocks the usual AI filler: "Transform your X," "Seamless," "Cutting-edge," "Solutions." The builder receives the copy as a build input and uses it verbatim.

### 4. Staged Build
A subagent builds in 4 verified stages:

| Stage | What | Verified Against |
|---|---|---|
| Structure | Semantic HTML, copywriter's content placed | Plan's page structure + Content Map |
| Typography | Font imports, CSS variables, color palette | Plan's visual choices |
| Layout | Grid/flex, responsive breakpoints, mobile-first | Plan's responsive strategy |
| Atmosphere | Gradients, textures, animations, polish | Plan's conceptual anchor |

### 5. Live Testing
Renders in a real browser (if Chrome DevTools or Playwright available). Screenshots at mobile (375px), tablet (768px), and desktop (1280px). Checks for overflow, font loading, console errors, and interaction behavior.

### 6. Design Review & Ship
A review agent compares the output against the plan — including copy fidelity checks to catch any generic replacements the builder might have slipped in. A quality gate runs final checks. You decide when it ships.

### 7. Refinement Loop
First delivery is rarely final. After seeing the output, you iterate: adjust the copy, tweak colors, restructure a section, change the tone. The skill stays in a feedback loop until you say "ship it."

Every revision agent gets the full ruleset — the same design guidelines, copy rules, and anti-rationalization tables that drove the first build. Quality doesn't degrade on round 3 the way it does when you're just chatting with a bare model.

### 8. Project Memory
The skill creates a `.frontend-design-memory.md` in your project directory after the first build. It captures your preferences, revision patterns, approved directions, and brand notes — so the next build in that project starts from what it already learned about your taste, not from zero.

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
├── Orchestrator (SKILL.md)          ← Creative direction, user conversation, refinement loop
├── Font Selector (select-fonts.mjs) ← Data-driven font recommendations
├── Copywriter Agent (Sonnet)        ← Headlines, body, CTAs, microcopy
├── Builder Agent (Sonnet)           ← 4-stage code generation
├── Tester Agent (Sonnet)            ← Browser rendering + screenshots
├── Reviewer Agent (Haiku)           ← Plan + copy fidelity check
├── Gate Agent (Haiku)               ← Pre-ship quality verification
└── Project Memory (.md)             ← Per-project learned preferences
```

The orchestrator stays in your conversation context for creative decisions and the refinement loop. Heavy work (copywriting, building, testing, reviewing) runs in subagents on cost-efficient models with fresh context.

---

## Anti-Rationalization

The highest-leverage pattern in this skill. AI models are excellent at justifying shortcuts. Every escape route has a pre-written counter:

| The Model Says | The Skill Says |
|---|---|
| "Inter is clean and readable" | It's the default. Defaults aren't design. |
| "I'll simplify the responsive strategy" | Build what was planned. Mobile-first, every breakpoint. |
| "This animation is too complex" | The signature moment is what makes it screenshot-worthy. |
| "I'll skip the texture/grain/atmosphere" | That's what separates designed from generic. |
| "Welcome to [Product]. We help you achieve your goals." | A copywriter wrote specific copy. Use it verbatim. |
| "I'll tighten up the copy a bit" | You're a builder, not an editor. The Content Map is a build input. |
| "The user just wants code fast" | A 15-line plan takes 30 seconds to read. A wrong-direction rebuild takes 10 minutes. |

---

## Requirements

- **Claude Code** — the CLI tool from Anthropic
- **Node.js** — for the font selector (already required by Claude Code)
- **Optional**: Chrome DevTools MCP or Playwright for live browser testing

## License

See LICENSE.txt for complete terms.
