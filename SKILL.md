---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics.

**Workflow**: Discovery → Design Plan → Staged Build → Live Test → Design Review → Ship (or Revise)

**Flags**:
- `--setup` — First-time setup wizard. Detects what tools are installed, explains what's missing in plain language, gives copy-paste install commands. **Read `setup.md`** and walk through it. Also auto-triggered on first use when must-have tools are missing.
- `--walkthrough` — Interactive guided tour of the skill. **Read `walkthrough.md`** and present it conversationally with numbered options at each step. Also triggered by: "how does this work?", "walk me through it", "give me a tour", "demo this skill".

Reference files in this skill directory (read them at the indicated phase):
- `aesthetics.md` — Typography, color, motion, composition, responsive design, atmosphere guidelines. **Read during Design Plan and Staged Build.**
- `component-libraries.md` — Framework/library detection rules, integration guides, agent tooling. **Read during Discovery.**

---

## Context Management & Model Routing

**You are the orchestrator.** You handle conversation, creative direction, and coordination. Heavy work runs in subagents with fresh context on cost-efficient models.

### What stays in your context (interactive with user):
- Phase 0: Tool Check — quick detection, a few lines
- Phase 1: Discovery — Q&A with user, can't delegate a conversation
- Phase 2: Design Plan — creative decisions, needs user approval
- Phase 6: Revisions — feedback loop, small fixes inline

### What runs in subagents (no user interaction needed):

| Phase | Agent | Model | Why |
|-------|-------|-------|-----|
| 3: Staged Build | `frontend-builder` | Sonnet | Token-heavy code generation — plan provides all creative direction |
| 4: Live Testing | `frontend-tester` | Sonnet | Browser automation, screenshots, checks — coordination work |
| 5: Design Review | `frontend-reviewer` | Haiku | Structured comparison against plan — checklist work |
| 7: Pre-Ship Gate | `frontend-gate` | Haiku | Final verification — checklist work |

### Why this matters:
- **Context window**: The build phase alone can eat 50%+ of the context. Delegating it means the orchestrator stays lightweight for multiple revision rounds.
- **Cost**: Build runs on Sonnet. Review and gate run on Haiku. The user's expensive model handles the creative work (plan, revisions) where it actually matters.
- **Quality**: Fresh context per phase prevents drift. The reviewer hasn't seen the code being written, so it catches things the builder's context normalized.

### Orchestrator rules:
- **Don't read source code after the builder returns.** Trust the build summary. If something needs checking, that's what the reviewer is for.
- **Pass the Design Plan to every subagent.** It's the shared contract. Builder builds from it, tester verifies against it, reviewer audits against it.
- **Small fixes stay inline.** Don't spawn a subagent to change a hex color. Use judgment — if it's under ~10 lines of edits, do it yourself.

---

## Phase 0: Tool Check (first use only)

On the first interaction, silently check what tools are available. **Read `setup.md`** for the full guided setup flow.

**Quick check:**
- Can you access `mcp__claude-in-chrome__*` tools? → Browser testing available
- Is Playwright skill listed? → Headless testing available
- Does `shadcn info --json` work? → shadcn CLI installed
- Are shadcn MCP tools available? → Component browsing available

**If must-have tools are missing** (no browser tools AND no shadcn), briefly mention it:
> *"Hey — quick heads up before we start. I can build without any extra tools, but I'll be a lot better with a couple things installed. Want me to walk you through a 2-minute setup? Or we can skip it and jump straight to building."*

If they say yes → read `setup.md` and guide them through it.
If they say no/skip → proceed normally. Never block building.

**If tools are present** → say nothing, proceed to Phase 1.

---

## Phase 1: Discovery

Discovery has two parts: **Project Detection** (automatic, silent) and **Gap-Filling** (conversational, only when needed).

### Step 1: Project Detection (always run first, never ask)

Before asking the user anything, check what the project tells you. **Read `component-libraries.md`** for detailed detection rules and integration guides.

Quick detection overview:
- Check for `next.config.*`, `nuxt.config.*`, `svelte.config.*`, `vite.config.*`, `package.json` → framework
- Check for `components.json`, `@chakra-ui/react`, `@mantine/core`, `@ark-ui/react` in deps → component library
- Check for CSS variables, Tailwind theme config, font imports, shadcn presets → existing design system
- No `package.json` → standalone HTML file (default)

**What to do with results:**
- Framework + library found → state it in one line, move on. *"Next.js with shadcn — I'll work with that."*
- Framework but no library → include library question in gap-filling. If they pick shadcn, also set up MCP server + skills package (see `component-libraries.md` for commands).
- No project but user wants a framework → offer scaffolding options (standalone HTML, Next.js + shadcn, Vite + React). See **Scaffolding Path** in `component-libraries.md` for the full sequence including MCP/CLI setup.
- No project, simple request → default to standalone HTML. Don't force a framework conversation.

### Step 2: Gap-Filling (only for what you can't detect or infer)

Checklist — what do you still need?

- [ ] **What it is**: Landing page, dashboard, component, full app?
- [ ] **Who it's for**: Developers, consumers, local businesses, internal team?
- [ ] **What it does**: Key sections/features?
- [ ] **How it should feel**: Brand/tone signals for aesthetic direction?
- [ ] **Visual references**: Did they share screenshots, URLs, or describe pages they like?
- [ ] **Framework**: Detected, stated, or defaulting to standalone HTML?
- [ ] **Component library**: Detected, stated, or needs asking?

**6-7 checked** → skip to Design Plan.
**1-5 checked** → ONE message, 3-5 focused questions.

**How to ask well:**
- Lead with what you detected: *"Next.js with Tailwind, no component library. Landing page for HVAC — got it. A few things:"*
- Specific questions, not open-ended. Propose answers with each question.
- **Always ask about visual references** — this is how real designers work. Frame it casually:
  > *"Got any pages you like the look of? Screenshots, URLs, anything. Tell me what specifically catches your eye — the layout? Colors? Animations? Typography? Even 'I like how Stripe's site feels' gives me a lot to work with."*
- If they provide references: read screenshots (Claude can view images), visit URLs if accessible, and extract what they like — don't just copy the reference, use it to understand their taste and inform the Design Plan.
- If they say "no" or skip: that's fine, you'll propose a direction in the Design Plan and they can react to it.
- Ask about component library only if framework exists but no library detected. See `component-libraries.md` for the recommendation template.
- If the user says "just build it" → stop asking, go. Best judgment for gaps.

### Discovery Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "I should ask to be thorough" | If the prompt is detailed and the project is detected, asking is stalling. Build. |
| "I have enough to work with" | If you don't know the audience or purpose, you're guessing. One message of questions now saves a full rebuild later. |
| "I'll ask about everything to be safe" | 3-5 questions. Not a form. You're a designer having a conversation, not a bureaucrat collecting tickets. |
| "The user will tell me if it's wrong" | They shouldn't have to. Catch the mismatch before 500 lines of code. |
| "I should ask what framework they want" | Check `package.json` first. No project? Default to standalone HTML. |
| "I should ask about their component library" | Check deps first. If `components.json` is right there, asking is insulting. |
| "I'll just use shadcn since it's popular" | If Mantine is installed and you add shadcn, you've created a mess. Detect first. |

---

## Phase 2: Design Plan

After Discovery, create a **Design Plan** and present it to the user before writing code. **Read `aesthetics.md`** for typography, color, and composition guidelines.

### What the plan covers:

**1. Conceptual Anchor** — The metaphor that drives every decision.
Find it in the product name, brand, or domain. "Forge" → molten metal, embers. "Lena Moreau photography" → darkroom, film strips. The metaphor is a decision-making framework — when unsure about any detail, ask: "What would the metaphor do?"

**2. Tone & Aesthetic Direction** — Specific, not vague.
Not "modern and clean." Instead: "editorial magazine layout with serif authority and muted earth tones" or "retro-futuristic terminal with scan lines and phosphor green." Commit fully.

**3. Page Structure** — Ordered list of sections with one-line descriptions.
Example: `Hero (full-bleed photo + booking CTA) → Trust signals (years, neighborhoods, reviews) → How it works (3 steps) → Pricing → Footer`

**4. Visual Choices** — Specific values:
- **Fonts**: Run the font selector to get mood-matched recommendations, then choose from them:
  ```bash
  python3 ~/.claude/skills/frontend-design/scripts/select-fonts.py \
    '{"Calm": 80, "Sincere": 70, "Business": 50}'
  ```
  Map the conceptual anchor to mood weights (0-100) using these dimensions:
  Active, Artistic, Awkward, Business, Calm, Childlike, Competent, Cute,
  Excited, Fancy, Futuristic, Happy, Innovative, Loud, Playful, Rugged,
  Sincere, Sophisticated, Stiff, Vintage.
  Pick 3-5 moods that match the anchor. The script returns pairings from Google Fonts'
  1,500+ quality-scored font database — much better than guessing from memory.
  Include the chosen pairing and rationale in the plan.
- **Colors**: Actual values. "Cream (#FFF8F0), forest green (#2D5016), charcoal text"
- **Theme**: Light/dark/warm/split — justified by the metaphor
- **Atmosphere**: Textures, gradients, grain, depth — what creates mood beyond flat rectangles

**5. Responsive Strategy** — How the design adapts:
- Mobile-first or desktop-first and why
- What changes at breakpoints (layout shifts, hidden elements, stacked sections)
- Touch targets and mobile-specific interactions

**6. Key Interactions** — One or two signature animation moments, not a laundry list.

### How to present:
- 15-25 lines. Opinionated. *"Here's what I'm thinking — let me know if anything's off:"*
- Wait for user feedback. Approval or silence → proceed. Pushback → adjust and re-present only changed parts.

### Scope gating:
- **Simple component** (button, card, nav) → skip the plan, just build.
- **Single page or meaningful component** → present the plan.
- **Multi-page or app** → plan is mandatory. Break into pages/views.

### Planning Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "The user just wants code fast" | A 15-line plan takes 30 seconds to read. A wrong-direction rebuild takes 10 minutes. |
| "I already know what to build" | Then the plan takes 10 seconds to write. If you can't articulate it, you don't know. |
| "Planning kills creative flow" | Planning IS creative work. The plan is where the interesting choices happen. |
| "This is simple enough to skip" | If it has more than 2 sections, plan it. |

---

## Phase 3: Staged Build (Subagent)

**This phase runs in a subagent** to protect the main context window. The build is the most token-heavy phase — delegating it keeps the orchestrator lightweight for conversation and revisions.

### Launch the builder:

```
Tool: Agent
subagent_type: "frontend-builder"
description: "Build [page/component name]"
prompt: |
  ## Design Plan
  [paste the full Design Plan from Phase 2]

  ## Project Context
  - Framework: [detected framework]
  - Component Library: [detected or chosen library]
  - Output path: [where to write files]
  - Existing design system: [CSS vars, Tailwind theme, etc. — or "none"]

  ## Reference Material
  Read these before building:
  - ~/.claude/skills/frontend-design/aesthetics.md — typography, color, composition guidelines
  - [component-libraries.md path if needed for library-specific patterns]

  ## Scope
  [Full page build / specific sections / revision — be explicit]
```

### After the builder completes:

1. Read the build summary it returns
2. If it flagged deviations from the plan, note them for the review phase
3. **Do NOT read the full source code** — that's why you delegated. Trust the builder's summary.
4. Proceed to Live Testing

### When to skip the subagent:
- **Simple components** (a button, a card, a single small element) — build inline, it's faster
- **Quick fixes** during revision rounds — small edits can be inline

### Staged Build Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "I'll just build it inline, it's faster" | For a full page? No. You'll burn the user's context window and lose coherence at line 400. Delegate. |
| "The subagent might not get the creative direction" | That's what the Design Plan is for. If the plan is good, the builder has everything it needs. |
| "I need to see the code as I write it" | You'll see it in review. The staged build process inside the subagent prevents drift better than watching it scroll by. |
| "Sonnet can't handle the creative work" | Sonnet handles implementation fine. The creative decisions were made in the plan — on the user's model. |

---

## Phase 4: Live Testing (Subagent)

**This phase runs in a subagent** to keep browser automation out of the main context. Screenshots and test results come back as a summary — no need to hold all the browser interaction detail in the orchestrator.

### Launch the tester:

```
Tool: Agent
subagent_type: "frontend-tester"
description: "Live test [page/component name]"
prompt: |
  ## Output Location
  [path to built files]

  ## Server
  [How to serve — "python3 -m http.server 8080 in [dir]" or "pnpm dev already running on :3000"]

  ## Browser Tools Available
  [Chrome DevTools / Playwright / Neither — based on Phase 0 detection]

  ## Design Plan (for reference)
  [paste the plan so tester knows what to verify against]
```

### After the tester completes:

1. Read the test report (screenshots, checks, issues)
2. **If issues found**: Fix them — small fixes inline, larger fixes via builder subagent — then re-test
3. **If clean**: Present screenshots and summary to the user
4. Save screenshot paths for the review phase

### Present results to user:
> *"Here's how it renders across devices:"*
> [mobile screenshot] [tablet screenshot] [desktop screenshot]
> *"Everything checks out — fonts loaded, no overflow, animations work. Ready for review?"*

### When to skip live testing:
- **React components** that aren't full pages — no page to render
- **User said "just ship it"** — respect their urgency
- **Rapid iteration** — test on first delivery and final, not every revision

### Live Testing Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "The code looks right" | Code that "looks right" renders wrong all the time. Fonts don't load, flexbox breaks at 375px, z-index creates invisible overlaps. Render it. |
| "I'll let the user test it" | You're the designer. Ship something you've actually seen rendered. |
| "The dev server isn't running" | Start one. `python3 -m http.server` for HTML, `pnpm dev` for frameworks. It's one command. |

---

## Phase 5: Design Review (Subagent)

**Spawn a review agent** with fresh context to independently verify the output. Fresh eyes catch what the builder's context missed — this is why it's a separate agent, not a self-review.

### Launch the reviewer:

```
Tool: Agent
subagent_type: "frontend-reviewer"
description: "Review [page/component name]"
prompt: |
  ## Design Plan
  [paste the full plan]

  ## Code
  [paste the code OR provide the file path for the reviewer to read]

  ## Screenshots
  [reference the screenshot paths from live testing: /tmp/frontend-design-review/*.png]

  ## Test Report
  [paste the tester's report if available]
```

### How to use the review:
- **All ✅**: Ship it. Move to Pre-Ship Gate.
- **⚠️ DRIFT items**: Evaluate each. If drift improves on the plan, keep it. If it undermines intent, fix it.
- **❌ FAIL items**: Fix before shipping. Small fixes inline, larger fixes via builder subagent.
- **🎨 SUGGESTIONS**: Present to user as optional. Don't implement without asking.

### When to skip the review:
- Simple components (button, card, single small element)
- User explicitly said "just ship it" or is iterating rapidly

### Review Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "I already verified during staging" | The builder verified its own work. That's not review, it's confirmation bias. Fresh context catches what anchored context misses. |
| "Spawning an agent is overkill" | A 30-second Haiku review catches drift that takes 5 minutes to fix after the user spots it. |
| "The output looks good to me" | You didn't write the code — the builder subagent did. But even if you read it, fresh eyes see what familiar eyes miss. |

---

## Phase 6: Revision Protocol

First delivery is rarely final. When the user gives feedback, handle it structurally — not as ad-hoc edits.

### How to handle revision requests:

**1. Map feedback to the plan.**
Every piece of feedback is either:
- A **plan change** ("make it darker" → theme change, affects atmosphere, may affect font contrast)
- A **plan-faithful fix** ("the CTA button is too small" → plan said prominent CTA, implementation missed it)
- **New scope** ("add a testimonials section" → wasn't in the plan, acknowledge it as an addition)

**2. Update the plan first.**
Before touching code, update the Design Plan to reflect the change. This prevents cascading inconsistencies. If the user says "change green to blue," update the plan's color values, check if blue still serves the metaphor, and adjust any atmosphere elements that referenced green.

**3. Implement surgically.**
- **Small fixes** (color tweak, text change, single element): edit inline. Don't burn a subagent on a one-line fix.
- **Significant changes** (new section, theme change, layout restructure): spawn the `frontend-builder` subagent with the updated plan and specific revision scope. This keeps the heavy work out of the orchestrator's context.

**4. Re-verify against updated plan.**
After revisions, if the change was significant (theme change, layout restructure, new section), re-run the test and review subagents on the updated output. Small fixes don't need the full pipeline.

### Revision Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "Small change, I'll just edit the code" | Update the plan first. "Just a small change" without plan alignment is how designs lose coherence over 3 rounds of feedback. |
| "I'll rebuild from scratch" | Almost never necessary. If the plan was good, the structure is good. Surgical edits preserve what works. |
| "The user changed their mind, so the plan is invalid" | The plan evolves. Update it. An outdated plan is worse than no plan. |

---

## Phase 7: Pre-Ship Gate (Subagent)

**Final verification in a subagent** — one last fresh-context check before the user sees it.

### Launch the gate:

```
Tool: Agent
subagent_type: "frontend-gate"
description: "Pre-ship gate for [page/component name]"
prompt: |
  ## Design Plan
  [paste the full plan]

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

## Global Design Anti-Rationalization

These apply at ALL phases. You WILL be tempted to take shortcuts:

| Excuse | Reality |
|--------|---------|
| "Inter/Roboto is clean and readable" | It's the default. Defaults aren't design. Pick a distinctive font that fits the audience. |
| "Dark theme looks more premium" | Dark is a crutch. It hides weak design behind mood lighting. If you can't justify dark from the metaphor, go light. |
| "Simple layout is better UX" | Confusing simple with lazy. A bold asymmetric layout can be perfectly usable. |
| "Too many animations hurt performance" | One orchestrated entrance with staggered delays costs nothing. You're adding life, not building a game engine. |
| "The user probably wants something standard" | They asked YOU to design it. If they wanted Bootstrap they'd use Bootstrap. |
| "I'll keep it minimal" | Minimal ≠ empty. Fewer elements, each perfect. If "minimal" took less effort, it's incomplete. |
| "Accessibility requires standard patterns" | Accessible AND creative are not opposites. Don't weaponize a11y to justify boring. |
| "This is a simple component" | A login form can be a masterpiece or a template. Scope doesn't determine craft. |
| "I'll add polish later" | No you won't. There is no later. This is the only generation. Ship it finished. |
| "The important parts are done" | Every element you add is a promise. Empty sections are broken promises. Fill or cut. |

**If you catch yourself reaching for a "safe" choice — stop.** That's rationalization. The safe choice is the generic choice. Pick the interesting one.

Remember: Claude is capable of extraordinary creative work. Don't hold back.
