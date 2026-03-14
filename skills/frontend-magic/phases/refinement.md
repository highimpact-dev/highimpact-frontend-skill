# Phase 7: Refinement Loop

**When to read**: After first delivery. **Re-read at the start of every refinement round.**
**Key rule**: Verify every change in the browser. Screenshot or it didn't happen.
**Key rule**: Significant changes go through plan mode. Quick tweaks stay inline.

---

## Phase 7: Refinement Loop

First delivery is rarely final. This phase is an **active loop** — you stay in it until the user says they're happy or explicitly says "ship it." Don't rush to the gate. The refinement loop is where good becomes great.

**IMPORTANT: Re-read this file at the start of every refinement round.** Context drift is how the skill loses its grip. If you're on round 3 and this feels unfamiliar, you drifted. Re-read and re-ground.

### How the loop works:

```
User sees first delivery (screenshots + summary)
  ↓
User gives feedback
  ↓
┌─→ Classify the feedback (see table below)
│     ↓
│   ┌─────────────────────────────────────────┐
│   │ SIGNIFICANT CHANGE?                     │
│   │  Yes → Enter Plan Mode                  │
│   │    • Update the plan                    │
│   │    • Redraw wireframe (if layout change)│
│   │    • Show user the revised direction    │
│   │    • Get approval                       │
│   │    • Exit plan mode                     │
│   │  No → Stay inline                       │
│   └─────────────────────────────────────────┘
│     ↓
│   Implement (inline or subagent)
│     ↓
│   Verify in browser → screenshot
│     ↓
│   Show result to user
│     ↓
│   "Anything else you want to tweak?"
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

---

## Feedback Classification → Plan Mode Gate

**Every piece of feedback gets classified. The classification determines whether you re-enter plan mode.**

| Feedback Type | Example | Plan Mode? | Why |
|---------------|---------|-----------|-----|
| **Layout change** | "Move testimonials above pricing" "Make the hero full-width" "Add a sidebar" | **YES** | Layout is spatial. Words are ambiguous. Redraw the wireframe so the user confirms the new arrangement before you touch code. |
| **Theme/mood change** | "Make it darker" "Warmer palette" "Less corporate, more playful" | **YES** | Theme changes cascade — colors, fonts, atmosphere, contrast. Update the visual direction and show the user the revised foundation. |
| **New scope** | "Add a testimonials section" "Can we add a pricing table?" | **YES** | New sections change the page structure. Show where they fit in the wireframe, how they affect flow. |
| **Voice/copy overhaul** | "Too formal" "Doesn't sound like us" "More conversational" | **YES** | Voice changes affect the content map across multiple sections. Update the direction, show revised copy approach, get approval. |
| **Copy tweak** | "Change the headline to X" "CTA should say 'Get a quote'" | No | Direct substitution. Just do it. |
| **Plan-faithful fix** | "CTA button is too small" "Font size is hard to read" | No | The plan was right, implementation missed. Fix inline. |
| **Color/spacing tweak** | "Make that blue darker" "More padding above the fold" | No | CSS value change. Fix, screenshot, done. |
| **Animation adjustment** | "Entrance is too fast" "Tone down the hover effect" | No | Timing/easing tweak. Fix inline. |

**The test:** If you need to update the Design Plan or redraw any part of the wireframe to communicate the change — it goes through plan mode. If you can describe it in one CSS property change — it stays inline.

---

## Plan Mode Refinement Flow

When feedback triggers plan mode, follow this exact sequence:

### Step 1: Enter Plan Mode

Call `EnterPlanMode`. State what you're re-evaluating:

> *"That's a layout change — let me rethink the structure before touching code."*

or

> *"Theme shift. Let me update the visual direction so we're aligned before I rebuild."*

### Step 2: Show What's Changing

**For layout changes — redraw the wireframe.**

Show the CURRENT wireframe with the change applied. Mark what changed with annotations:

```
REVISED DESKTOP WIREFRAME
──────────────────────────

┌──────────────────────────────────────────────────────┐
│  LOGO                          [About] [Work] [▤]   │
├──────────────────────────────────────────────────────┤
│                                                      │
│  We build things that matter.                        │
│  ───────────────────────────                         │
│  Subtext about the product                           │
│  [ Get Started ]  [ Learn More ]                     │
│                                                      │
│  (CHANGED: hero is now full-width, centered.         │
│   Was: two-column with image right)                  │
├──────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────┐ │
│  │                                                 │ │
│  │              FULL-WIDTH HERO IMAGE              │ │
│  │                                                 │ │
│  └─────────────────────────────────────────────────┘ │
│                                                      │
│  (NEW: image moved to full-bleed below headline)     │
├──────────────────────────────────────────────────────┤
│          ... rest unchanged ...                      │
└──────────────────────────────────────────────────────┘
```

You can show just the affected sections if the rest is unchanged. But if the change ripples (reordering sections, adding new ones), redraw the full wireframe.

**For theme/mood changes — update the visual direction block:**

```
REVISED VISUAL DIRECTION
────────────────────────
Colors:    Primary [#1a1a2e deep navy] · Accent [#e94560 coral] · Background [#0f0f23 near-black] · Text [#eee soft white]
           (CHANGED: was warm cream palette → now dark dramatic)
Theme:     Dark — the user wants more edge. Anchor still holds: "recording studio at night" reinforces this.
Atmosphere: Subtle noise grain, deep shadows, glow effects on interactive elements
```

**For new scope — show where it fits in the wireframe:**

```
REVISED PAGE STRUCTURE
──────────────────────
1. Nav
2. Hero
3. Trust
4. Features
5. ★ TESTIMONIALS (NEW — inserted here, before pricing,
   to build social proof before the ask)
6. Pricing
7. CTA
8. Footer
```

Then draw the new section in context with its neighbors.

**For voice changes — summarize the revised direction:**

> *"Shifting from formal/corporate to conversational/direct. Headlines become shorter, punchier. CTAs drop the soft-sell ('Get started' not 'Learn more about our solutions'). Body copy reads like talking to a smart friend, not presenting to a board."*

### Step 3: Ask for Approval

**Specific question based on what changed:**

| Change type | Question |
|-------------|----------|
| Layout | *"Here's the revised layout. Spatial relationships feel right? Anything else to adjust before I implement?"* |
| Theme/mood | *"Here's the new visual direction. This is the foundation — colors, atmosphere, everything cascades from this. Good to build on?"* |
| New scope | *"I'd put the new section here in the flow. Makes sense in the page narrative? Or should it sit somewhere else?"* |
| Voice | *"Here's the new voice direction. I'll rewrite the affected copy with this tone. Sound like what you're after?"* |

**Wait for approval. Do not exit plan mode on silence.** If the user hasn't responded, ask again. If they give partial approval ("layout's good but move the new section"), adjust and re-present the changed part.

### Step 4: Exit Plan Mode and Implement

Once approved, call `ExitPlanMode`. Then:

1. **Update the actual Design Plan document** with the approved changes (wireframes, visual direction, structure — whatever changed)
2. **Implement** — inline for small scope, builder subagent for significant scope
3. **Verify in browser** — screenshot every change
4. **Show the user** the result
5. **Ask for more feedback** — back to the top of the loop

---

## Inline Refinement Flow (No Plan Mode)

For quick tweaks that don't need plan mode:

### 1. Acknowledge and act.

> *"Darker blue on the CTA — on it."*

Don't over-explain. Don't ask for confirmation on a clear directive.

### 2. Read the code first.

You delegated the build to a subagent. You haven't seen this code. **Read the specific section being changed** before editing. Not the whole file — just the relevant section.

### 3. Edit, verify, show.

Make the change. Take a screenshot. Present it:

> *"Updated — here's how it looks now:"*
> [screenshot]
> *"Better? Anything else?"*

### 4. Update the plan.

Even for small tweaks — if a color changed, update the color in the Design Plan. The plan is the source of truth. If the plan drifts from the code, the next revision round will be incoherent.

---

## Subagent Delegation During Refinement

### When to use the builder subagent:

- New sections or layout restructures
- Changes affecting 3+ sections
- Theme overhauls (colors, fonts, atmosphere across the whole page)
- Anything that could cascade

**Give the builder the UPDATED plan and UPDATED wireframes:**

```
Tool: Agent
subagent_type: "frontend-builder"
description: "Revise [specific changes]"
prompt: |
  Read the builder instructions at the skill's agents/frontend-builder.md path.

  ## Design Plan (UPDATED)
  [paste the UPDATED plan — including revised wireframes]

  ## Content Map (UPDATED)
  [paste the UPDATED Content Map — not the original]

  ## Existing Code
  [file path to the current built output]

  ## Reference Material
  Read these before building:
  - aesthetics.md path in the skill
  - component-libraries.md (if needed)

  ## Revision Scope
  [SPECIFIC changes requested — be explicit about what to change and what to preserve]

  ## What NOT to Change
  [List sections/elements the user is happy with — the builder must preserve these]

  ## Project Context
  - Framework: [detected framework]
  - Component Library: [detected or chosen library]
```

### When to use the copywriter subagent:

- Feedback like "too formal," "too salesy," "doesn't sound like us"
- Changes affecting copy across multiple sections

```
Tool: Agent
subagent_type: "implementer"
description: "Revise copy — [voice change]"
prompt: |
  Read the copywriter instructions at the skill's agents/frontend-copywriter.md path.

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

---

## Browser Verification (Every Change, No Exceptions)

After every code change — no matter how small — render the page and take a screenshot.

**Priority order for browser tools:**

1. **Chrome DevTools MCP** (`mcp__claude-in-chrome__*`): Navigate to the page, screenshot at relevant breakpoints. Layout changes → screenshot mobile (375px) AND desktop (1280px). Color/copy tweaks → one screenshot at most relevant breakpoint.

2. **Playwright** (if available): Navigate, screenshot, check console errors.

3. **Neither available**: Serve the page (`python3 -m http.server`), tell the user to check it, note you couldn't visually verify.

**What to check:**
- Did the change actually render? (fonts, images, layout intact)
- Did it break anything adjacent? (CSS cascade, flex/grid reflow, z-index)
- Does mobile still work? (if you touched layout or spacing)
- Console errors? (check with `read_console_messages`)

**Present to user:**
> *"Updated the hero to full-width. Here's desktop and mobile:"*
> [screenshots]
> *"No overflow issues. The image scales well. Better?"*

---

## When to Re-Run the Full Pipeline

| Trigger | Action |
|---------|--------|
| Theme change (light→dark, new palette) | Full re-test at all 3 breakpoints + re-review |
| Layout restructure (new sections, reordered) | Full re-test + re-review |
| Voice overhaul (full copy rewrite) | Re-review (check copy fidelity) |
| Everything else | Orchestrator handles verification inline |

---

## Exiting the Loop

The user exits the refinement loop by saying any of:
- "Looks good" / "I'm happy with it" / "Ship it" / "Done" / "That's perfect"
- Moving on to a different task (implicit approval)

When they exit → proceed to Phase 8 (Pre-Ship Gate), then update project memory.

**Do not pre-emptively suggest shipping.** Don't say "ready to ship?" after every fix. Let the user drive the pace. Your job is to ask *"Anything else?"* — not to close the sale.

---

## Refinement Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "Small change, I'll just edit the code" | Did you update the plan? If not, the plan and code are now out of sync. Next revision round will be incoherent. |
| "This doesn't need plan mode, I'll just rebuild the section" | If it's a layout change, the user needs to see the wireframe. "I'll just rebuild it" is how you build the wrong thing faster. |
| "I don't need to re-read refinement.md, I remember the rules" | You don't. Context drift is invisible. Re-read. It takes 5 seconds. |
| "The user changed their mind, so the plan is invalid" | The plan evolves. Update it. An outdated plan is worse than no plan. |
| "I don't need to read the code for this edit" | Yes you do. You didn't write it — the builder subagent did. You can't edit what you haven't seen. |
| "The builder can figure out what to preserve" | Don't make it guess. Explicitly list what NOT to change. |
| "This is taking too many rounds" | Iteration IS the process. Three rounds is normal. Rushing to ship is how you deliver something the user doesn't love. |
| "I'll skip re-entering plan mode, the change is obvious" | If it's a layout change, it's not obvious — it's spatial. Draw it. If it's a theme change, it cascades — show the new direction. The 30 seconds in plan mode prevents a wrong-direction rebuild. |
| "The wireframe is already approved, no need to update it" | The wireframe reflects the current design. If the design changed, the wireframe is wrong. An outdated wireframe misleads the builder subagent. |
| "Re-testing is overkill for this change" | One screenshot. 5 seconds. Do it. |
| "I'll just describe what I changed" | The user can't evaluate a design change from a description. Show them. Screenshot or it didn't happen. |
| "I'll verify after a few more changes" | No. Verify each change individually. Batching hides which edit broke the layout. |
| "Plan mode is too much friction for every round" | It's not for every round. It's for layout, theme, scope, and voice changes. Quick tweaks stay inline. Read the classification table. |
| "I've been in the skill for a while, I know what I'm doing" | That's when drift is worst. You FEEL competent because the instructions have faded from context. Re-read this file. |
