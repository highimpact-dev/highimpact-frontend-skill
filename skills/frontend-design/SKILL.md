---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics.

**Workflow**: Discovery → Design Plan → Copywriting → Staged Build → Live Test → Design Review → Ship (or Revise)

**Flags**:
- `--setup` — First-time setup wizard. Detects what tools are installed, explains what's missing in plain language, gives copy-paste install commands. **Read `setup.md`** and walk through it. Also auto-triggered on first use when must-have tools are missing.
- `--walkthrough` — Interactive guided tour of the skill. **Read `walkthrough.md`** and present it conversationally with numbered options at each step. Also triggered by: "how does this work?", "walk me through it", "give me a tour", "demo this skill".

Reference files in this skill directory (read them at the indicated phase):
- `aesthetics.md` — Typography, color, motion, composition, responsive design, atmosphere guidelines. **Read during Design Plan and Staged Build.**
- `component-libraries.md` — Framework/library detection rules, integration guides, agent tooling. **Read during Discovery.**
- `memory.md` — Template for per-project memory files. **Do not read this file directly.** Instead, read/write `.frontend-design-memory.md` in the project's working directory. See Phase 1 Step 0 and Memory Update section.

---

## Context Management & Model Routing

**You are the orchestrator.** You handle conversation, creative direction, and coordination. Heavy work runs in subagents with fresh context on cost-efficient models.

### What stays in your context (interactive with user):
- Phase 0: Tool Check — quick detection, a few lines
- Phase 1: Discovery — Q&A with user, can't delegate a conversation
- Phase 2: Design Plan — creative decisions, needs user approval
- Phase 7: Revisions — feedback loop, small fixes inline

### What runs in subagents (no user interaction needed):

| Phase | Agent | Model | Why |
|-------|-------|-------|-----|
| 3: Copywriting | `frontend-copywriter` | Sonnet | Voice-sensitive content generation — needs nuance |
| 4: Staged Build | `frontend-builder` | Sonnet | Token-heavy code generation — plan provides all creative direction |
| 5: Live Testing | `frontend-tester` | Sonnet | Browser automation, screenshots, checks — coordination work |
| 6: Design Review | `frontend-reviewer` | Haiku | Structured comparison against plan — checklist work |
| 8: Pre-Ship Gate | `frontend-gate` | Haiku | Final verification — checklist work |

### Why this matters:
- **Context window**: The build phase alone can eat 50%+ of the context. Delegating it means the orchestrator stays lightweight for multiple revision rounds.
- **Cost**: Copy and build run on Sonnet. Review and gate run on Haiku. The user's expensive model handles the creative work (plan, revisions) where it actually matters.
- **Quality**: Fresh context per phase prevents drift. The copywriter writes without seeing code. The reviewer hasn't seen the code being written, so it catches things the builder's context normalized.

### Orchestrator rules:
- **Don't read source code after the builder returns.** Trust the build summary. If something needs checking, that's what the reviewer is for.
- **Pass the Design Plan to every subagent.** It's the shared contract. Copywriter writes from it, builder builds from it, tester verifies against it, reviewer audits against it.
- **Pass the Content Map to the builder.** The copywriter's output is a build input, not a suggestion. The builder uses it verbatim.
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

### Step 0: Memory Check (always run first, silent)

Check for `.frontend-design-memory.md` in the project's working directory.

**If it exists**: Read it. This project has been built with the skill before. Use stored preferences to inform your plan — don't re-learn what you already know.
- If memory has brand/identity notes → you already know the audience and voice
- If memory has revision patterns ("always asks for bolder CTAs") → get it right the first time
- If memory has approved directions → you know what "good" looks like for this project

**If it doesn't exist**: First build in this project. Create the file from the template after the build ships (see Memory Update section). Proceed normally.

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
  node ~/.claude/skills/frontend-design/scripts/select-fonts.mjs \
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

## Phase 3: Copywriting (Subagent)

**This phase runs in a subagent** so the copywriter works from the brief alone — no code context, no layout assumptions. Just the plan, the audience, and the words.

### When to run the copywriter:
- **Landing pages, marketing pages, multi-section pages** → always. This is where copy quality makes or breaks the output.
- **Apps and dashboards** → yes, for onboarding flows, empty states, error messages, and any marketing-facing sections.
- **Simple components** (button, card, nav) → skip. The builder can handle a few labels.
- **User provided all the copy** → skip. Don't rewrite what they gave you.

### Launch the copywriter:

```
Tool: Agent
subagent_type: "frontend-copywriter" (falls back to Sonnet implementer — read the agent file)
description: "Write copy for [page/component name]"
prompt: |
  Read ~/.claude/skills/frontend-design/agents/frontend-copywriter.md for your full instructions.

  ## Design Plan
  [paste the full Design Plan from Phase 2]

  ## Project Context
  - What it is: [product/brand/business description]
  - Who it's for: [target audience from Discovery]
  - What it does: [core value proposition]
  - Any specific messaging from the user: [quotes, taglines, facts they mentioned]

  ## Sections Needing Copy
  [list every section from the plan's Page Structure]
```

### After the copywriter completes:

1. Read the Content Map it returns
2. **Quickly scan for banned patterns** — if the copywriter slipped into "Transform your X" territory, catch it now
3. **Present a summary to the user**: share 2-3 standout headlines and the overall voice direction. Don't dump the full content map — they'll see it in context when the page is built.
4. User approves or requests changes → adjust the Content Map
5. Pass the approved Content Map to the builder in Phase 4

### Copywriting Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "The builder can write copy as it goes" | The builder writes code. When it also writes copy, you get "Welcome to [Product]. We help you achieve your goals." Every. Single. Time. |
| "Copy doesn't matter for a prototype" | It absolutely does. Generic copy makes every design look like a template, no matter how good the visuals are. Stakeholders can't evaluate a design when the words say nothing. |
| "The user will replace the copy later" | In 9 out of 10 cases, they won't. What ships in v1 becomes permanent. Write it like it's final. |
| "This adds another step and slows things down" | A Sonnet call for copy takes 15 seconds. Rewriting generic copy after seeing it in the design takes a full revision round. The math isn't close. |
| "I already wrote good copy in the Design Plan" | The plan has section descriptions, not finished copy. "Hero with booking CTA" is a plan note. "Your next HVAC tech is already in your neighborhood" is copy. |
| "The copywriter will just write marketing fluff" | That's what the banned patterns and anti-rationalization table prevent. The copywriter has stricter guardrails against cliches than any other agent. |
| "I can be the copywriter — I'm Opus" | You could, but then 500+ tokens of copy sit in the orchestrator's context forever. The subagent writes it, the builder consumes it, and your context stays clean for revisions. |

---

## Phase 4: Staged Build (Subagent)

**This phase runs in a subagent** to protect the main context window. The build is the most token-heavy phase — delegating it keeps the orchestrator lightweight for conversation and revisions.

### Launch the builder:

```
Tool: Agent
subagent_type: "frontend-builder"
description: "Build [page/component name]"
prompt: |
  ## Design Plan
  [paste the full Design Plan from Phase 2]

  ## Content Map
  [paste the full Content Map from Phase 3 — the copywriter's output]

  IMPORTANT: Use this copy VERBATIM. Do not rewrite headlines, soften CTAs, or
  replace specific copy with generic alternatives. The copy was written by a
  dedicated copywriter to match the Design Plan's voice. Your job is to build
  the design around these words, not to edit them.

  ## Project Context
  - Framework: [detected framework]
  - Component Library: [detected or chosen library]
  - Output path: [where to write files]
  - Existing design system: [CSS vars, Tailwind theme, etc. — or "none"]

  ## Reference Material
  Read these before building:
  - ~/.claude/skills/frontend-design/aesthetics.md — typography, color, composition guidelines
  - ~/.claude/skills/frontend-design/component-libraries.md (if library-specific patterns needed)

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
| "The subagent might not get the creative direction" | That's what the Design Plan + Content Map are for. If the plan and copy are good, the builder has everything it needs. |
| "I need to see the code as I write it" | You'll see it in review. The staged build process inside the subagent prevents drift better than watching it scroll by. |
| "Sonnet can't handle the creative work" | Sonnet handles implementation fine. The creative decisions were made in the plan, the copy was written by the copywriter — on the user's model. |
| "The copy doesn't quite fit the layout I'm building" | Adjust the layout, not the copy. The copy was approved. If it truly can't work, flag it in the build summary — don't silently rewrite it. |

---

## Phase 5: Live Testing (Subagent)

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

## Phase 6: Design Review (Subagent)

**Spawn a review agent** with fresh context to independently verify the output. Fresh eyes catch what the builder's context missed — this is why it's a separate agent, not a self-review.

### Launch the reviewer:

```
Tool: Agent
subagent_type: "frontend-reviewer"
description: "Review [page/component name]"
prompt: |
  ## Design Plan
  [paste the full plan]

  ## Content Map (from copywriter)
  [paste the Content Map so the reviewer can verify copy fidelity]

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

## Phase 7: Refinement Loop

First delivery is rarely final. This phase is an **active loop** — you stay in it until the user says they're happy or explicitly says "ship it." Don't rush to the gate. The refinement loop is where good becomes great.

### How the loop works:

```
User sees first delivery (screenshots + summary)
  ↓
User gives feedback
  ↓
┌─→ Orchestrator classifies feedback
│     ↓
│   Update plan / Content Map / both
│     ↓
│   Implement (inline or subagent)
│     ↓
│   Show result to user (re-test if significant)
│     ↓
│   User gives more feedback → loop back ─────┐
│                                              │
└──────────────────────────────────────────────┘
  ↓
User says "looks good" / "ship it" / "done"
  ↓
Proceed to Phase 8: Pre-Ship Gate
```

### Entering the loop:

After first delivery, **explicitly invite feedback**:
> *"Here's how it looks across devices. What do you think — anything you want to adjust? I'm here for as many rounds as you need."*

Don't present the output and immediately move to the gate. The user needs time to react, and they need to know iteration is expected and welcome.

### Classifying feedback:

Every piece of feedback is one of:
- **Plan change** ("make it darker" → theme change, affects atmosphere, may affect font contrast)
- **Copy change** ("the headline feels too aggressive" → update Content Map, then update code)
- **Plan-faithful fix** ("the CTA button is too small" → plan said prominent CTA, implementation missed it)
- **New scope** ("add a testimonials section" → wasn't in the plan, acknowledge it as an addition)

### The revision process:

**1. Update the plan and/or Content Map first.**
Before touching code, update the Design Plan and Content Map to reflect the change. This prevents cascading inconsistencies. If the user says "change green to blue," update the plan's color values, check if blue still serves the metaphor, and adjust any atmosphere elements that referenced green. If they say "the tone is too formal," update the Content Map's voice direction and rewrite affected copy.

**2. Implement — inline or via subagent.**

**Inline (orchestrator handles directly):**
- Color/spacing tweaks, single element fixes
- One headline or CTA swap
- CSS adjustments, animation timing
- Any change under ~15 lines of edits

When editing inline, **read the code first.** You delegated the build to stay lightweight, but during refinement you need to see the actual code to make precise edits. Read the specific section being changed, not the whole file.

**Via builder subagent (for significant changes):**
- New sections, layout restructures, theme overhauls
- Changes affecting 3+ sections
- Anything that could cascade

When spawning the builder for revisions, **give it full context**:

```
Tool: Agent
subagent_type: "frontend-builder"
description: "Revise [specific changes]"
prompt: |
  Read ~/.claude/skills/frontend-design/agents/frontend-builder.md for your full instructions.

  ## Design Plan (UPDATED)
  [paste the UPDATED plan — not the original]

  ## Content Map (UPDATED)
  [paste the UPDATED Content Map — not the original]

  ## Existing Code
  [file path to the current built output]

  ## Reference Material
  Read these before building:
  - ~/.claude/skills/frontend-design/aesthetics.md
  - ~/.claude/skills/frontend-design/component-libraries.md (if needed)

  ## Revision Scope
  [SPECIFIC changes requested — be explicit about what to change and what to preserve]

  ## What NOT to Change
  [List sections/elements the user is happy with — the builder must preserve these]

  ## Project Context
  - Framework: [detected framework]
  - Component Library: [detected or chosen library]
```

**Via copywriter subagent (for voice/tone changes):**
- Feedback like "too formal," "too salesy," "doesn't sound like us"
- Changes affecting copy across multiple sections
- Re-run with updated voice direction, then pass new Content Map to builder

```
Tool: Agent
subagent_type: "frontend-copywriter" (falls back to Sonnet implementer)
description: "Revise copy — [voice change]"
prompt: |
  Read ~/.claude/skills/frontend-design/agents/frontend-copywriter.md for your full instructions.

  ## Design Plan
  [paste the current plan]

  ## Previous Content Map
  [paste what was written before]

  ## Revision Request
  [what the user wants changed about the voice/copy]

  ## What Worked (preserve these)
  [copy elements the user was happy with]

  ## Sections to Revise
  [specific sections, or "all" for a voice overhaul]
```

**3. Show the result.**
After implementing, show the user what changed:
- For visual changes: re-screenshot and present the updated view
- For copy changes: quote the new text in context
- For small fixes: briefly confirm what was adjusted

> *"Updated — hero headline is now 'Find your HVAC tech in 11 minutes' and the CTA says 'Get your free quote.' Here's how it looks:"*

**4. Stay in the loop.**
After showing the result, **ask for more feedback**:
> *"Better? Anything else you want to tweak?"*

Don't assume one round of feedback is the end. Don't say "ready to ship?" after every fix — let the user drive the pace.

### When to re-run the full pipeline during refinement:

- **Theme change** (light→dark, new color palette) → re-test + re-review
- **Layout restructure** (new sections, reordered sections) → re-test + re-review
- **Voice overhaul** (full copy rewrite) → re-review (check copy fidelity)
- **Everything else** → show the result, skip the pipeline

### Exiting the loop:

The user exits the refinement loop by saying any of:
- "Looks good" / "I'm happy with it" / "Ship it" / "Done" / "That's perfect"
- Moving on to a different task (implicit approval)

When they exit → proceed to Phase 8 (Pre-Ship Gate), then update project memory.

### Refinement Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "Small change, I'll just edit the code" | Update the plan first. "Just a small change" without plan alignment is how designs lose coherence over 3 rounds of feedback. |
| "I'll rebuild from scratch" | Almost never necessary. If the plan was good, the structure is good. Surgical edits preserve what works. |
| "The user changed their mind, so the plan is invalid" | The plan evolves. Update it. An outdated plan is worse than no plan. |
| "I don't need to read the code for this edit" | Yes you do. You didn't write it — the builder subagent did. You can't edit what you haven't seen. Read the section, then edit. |
| "The builder can figure out what to preserve" | Don't make it guess. Explicitly list what NOT to change. Builders without preservation constraints will normalize things the user already approved. |
| "This is taking too many rounds" | Iteration IS the process. Three rounds of refinement is normal. Rushing to ship is how you deliver something the user doesn't love. |
| "I'll skip the aesthetics.md reference for a quick revision" | The rules don't stop applying because it's round 2. The builder still needs the full ruleset. A revision without guidelines is how dark-theme creep and generic fonts sneak back in. |
| "The user is probably done after this fix" | Don't assume. Ask. If they're done, they'll say so. If they're not, they'll appreciate that you're ready for more. |
| "Re-testing is overkill for this change" | If you changed the layout, theme, or multiple sections — re-test. A 30-second screenshot catches the regression you just introduced. |

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
