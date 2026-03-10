# Phase 8: Pre-Ship Gate + Memory Update + Learning Extraction

**When to read**: When user says "looks good" / "ship it" / "done".
**Runs in subagent**: `frontend-gate` (Haiku)

---

## Phase 8: Pre-Ship Gate (Subagent)

**Final verification in a subagent** — one last fresh-context check before the user sees it.

### Launch the gate:

```
Tool: Agent
subagent_type: "frontend-gate"
description: "Pre-ship gate for [page/component name]"
prompt: |
  ## Design Plan
  [paste the full plan]

  ## Content Map (from copywriter)
  [paste the Content Map so the gate can verify copy fidelity]

  ## Code
  [file path to the built output]

  ## Review Results
  [paste the reviewer's report]

  ## Test Results
  [paste the tester's report]
```

### How to use the gate results:
- **SHIP**: Deliver to the user with confidence.
- **FIX FIRST**: Address the issues (inline for small, builder subagent for large), then ship.
- **NOT READY**: Something fundamental is wrong. Fix and re-run the gate.

### When to skip the gate:
- Simple components that skipped the plan
- User explicitly wants it now
- Already went through 2+ revision rounds with review passes

### Pre-Ship Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "The reviewer already approved it" | The reviewer checks plan adherence. The gate checks quality standards too. Different lens. |
| "Mobile is fine, it just stacks" | "Just stacking" is not responsive design. Mobile should feel intentional, not collapsed. |
| "Three subagents is overkill" | Three Haiku calls cost less than one round of user feedback fixing something you should have caught. |

---

## Memory Update (after shipping or significant revisions)

After the build ships (or after 2+ revision rounds), update `.frontend-design-memory.md` in the project directory. If the file doesn't exist yet, create it from the template in `memory.md`.

This is how the skill gets better for this project over time. Each project maintains its own memory — a fintech dashboard's preferences don't bleed into a band's landing page.

### What to capture:

**Brand & Identity** — project-specific context:
- Company/product name, audience, positioning
- Brand colors, fonts, voice guidelines if mentioned
- "Lead Shield: blue-collar HVAC audience, trust-first, plain language"

**Design Preferences** — choices that reveal taste:
- "Approved bold serif headlines without hesitation" → preference for editorial typography
- "Changed warm cream background to cool gray" → prefers cooler palettes
- "Asked for more whitespace twice" → likes breathing room

**Voice & Copy** — what copy style landed:
- "Approved conversational, direct CTAs" → voice preference
- "Changed 'Book now' to 'Get a free quote'" → prefers soft-commitment CTAs
- "Loved the specific stats in social proof" → respond well to data-driven copy

**Design Patterns** — what worked visually:
- "Glass morphism nav approved" → likes that aesthetic
- "Staggered entrance animation praised" → signature moments land well
- "Kept the asymmetric hero layout through 3 revision rounds" → that's a keeper

**Common Revisions** — feedback that repeats = unlearned preference:
- If the user asks for the same kind of change twice, that's a preference, not a one-off. Write it down so you don't make them ask a third time.

**Approved Directions** — what the plan looked like when it was approved:
- Brief notes on the plan's anchor, tone, key choices
- "Approved: editorial magazine layout, warm earth tones, serif headlines — shipped without major revisions"

### How to write:
- Be concise — one line per insight
- Include evidence — "preferred X (approved plan v1)" not just "likes X"
- Update existing entries rather than duplicating — if a preference strengthens, update the note
- Remove entries that turn out to be wrong — if the user contradicts a stored preference, delete it

### Memory Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "Nothing notable happened this build" | If the user approved a plan, that's a data point. If they revised anything, that's a data point. There's always something. |
| "I'll remember for next time" | You won't. No memory between sessions without the file. Write it now or lose it. |
| "This is a one-off project, memory won't help" | Even one revision round generates preferences. And if they come back to iterate in 3 months, you'll have full context instead of starting over. |
| "The memory file is getting long" | Edit it. Merge similar entries. Remove outdated ones. Curation > accumulation. |

---

## Learning Extraction (after every shipped build)

After shipping AND updating project memory, run the learning extraction to improve the skill across ALL projects.

### Step 1: Check for Cross-Project Patterns

Read `~/.claude/skills/frontend-design/learnings.md`. Then ask:

1. **Did this build surface a revision pattern that matches an existing learning?**
   - If yes → the learning is validated. Update its confidence (e.g., "3 projects" → "4 projects").

2. **Did this build surface a NEW pattern not in learnings.md?**
   - A "pattern" means: a revision the user requested that reveals a general preference or common failure, NOT a project-specific choice.
   - Examples of patterns: "users almost always want more whitespace", "serif headlines get approved more than sans-serif for editorial sites"
   - NOT patterns: "this user likes blue" (project-specific → goes in project memory only)

3. **Did the user give feedback that contradicts an existing learning?**
   - If yes → reduce confidence or remove the learning. One contradiction doesn't invalidate, but note it.

### Step 2: Check for Anti-Pattern Candidates

A revision becomes an anti-pattern candidate when:
- The same type of revision was requested in 2+ different projects
- OR the user expressed frustration about the issue (strong signal from 1 project is enough)
- OR the issue maps to a known "AI slop" pattern (generic fonts, empty "Transform your X" copy, gratuitous dark theme)

**Format for new anti-patterns:**
```
| "Excuse the model tells itself" | "The reality — why this is wrong" |
```

### Step 3: Write to Learnings File

Append new learnings to `~/.claude/skills/frontend-design/learnings.md` in the appropriate section. Update existing entries if this build provides new evidence.

**What to write:**
- One line per learning
- Include evidence count: "(seen in 2 projects)" or "(strong signal: user was frustrated)"
- Include the anti-rationalization row if it's an anti-pattern candidate

**What NOT to write:**
- Project-specific preferences (those go in project memory)
- Speculative patterns from a single build with weak signal
- Anything already covered by `aesthetics.md` or `SKILL.md`'s existing anti-rationalization tables

### Learning Extraction Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "Nothing generalizable happened" | If the user revised anything, ask: would this apply to other projects? Usually yes. |
| "The existing anti-patterns already cover this" | Check. If they do, great. If they cover the category but miss the specific pattern, add the specific one. |
| "One build isn't enough signal" | Write it with "(1 project)" confidence. It'll either get validated or removed. Low-confidence entries are better than lost observations. |
| "I'll remember for next time" | You won't. No memory between sessions. Write it now. |
