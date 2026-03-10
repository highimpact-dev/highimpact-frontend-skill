# Phase 7: Refinement Loop

**When to read**: After first delivery, stay here until user approves.
**Key rule**: Verify every change in the browser. Screenshot or it didn't happen.

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
subagent_type: "implementer"
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

**3. Verify in the browser. Every time.**

After every code change — no matter how small — render the page and take a screenshot. The user needs to SEE the change, not trust your description of it.

**How to verify:**

Use whatever browser tooling was detected in Phase 0, in this priority order:

1. **Chrome DevTools MCP** (`mcp__claude-in-chrome__*`): Navigate to the page, take screenshots at the breakpoints that matter for this change. If the change affects layout, screenshot mobile (375px) AND desktop (1280px). If it's a color/copy tweak, one screenshot at the most relevant breakpoint is fine.

2. **Playwright** (if available as a skill): Run a quick verification script — navigate, screenshot, check for console errors.

3. **Neither available**: Serve the page (`python3 -m http.server` for HTML), tell the user to check it, and note that you couldn't visually verify.

**What to check on each iteration:**
- Did the change actually render? (fonts load, images show, no broken layout)
- Did the change break anything adjacent? (CSS cascade, flex/grid reflow, z-index)
- Does mobile still work? (if you touched layout or spacing)
- Any console errors? (check with `read_console_messages` or Playwright logs)

**Present the screenshot(s) to the user with a brief note:**
> *"Updated the hero headline and CTA. Here's how it looks now:"*
> [screenshot]
> *"Mobile still holds — no overflow. Better?"*

**4. Stay in the loop.**
After showing the verified result, **ask for more feedback**:
> *"Anything else you want to tweak?"*

Don't assume one round of feedback is the end. Don't say "ready to ship?" after every fix — let the user drive the pace.

### When to re-run the FULL pipeline (tester + reviewer subagents):

- **Theme change** (light→dark, new color palette) → full re-test at all 3 breakpoints + re-review
- **Layout restructure** (new sections, reordered sections) → full re-test + re-review
- **Voice overhaul** (full copy rewrite) → re-review (check copy fidelity)

For everything else, the orchestrator handles verification inline using the browser tools. You don't need the tester subagent for a color change — but you DO need to screenshot it.

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
| "Re-testing is overkill for this change" | You're not re-running the full pipeline. You're taking ONE screenshot. That takes 5 seconds. Do it. |
| "I'll just describe what I changed" | The user can't evaluate a design change from a description. They need to see it. Screenshot or it didn't happen. |
| "The browser tools aren't set up" | If Chrome DevTools or Playwright were available in Phase 0, they're available now. If neither is available, serve the page and tell the user to check it — but don't pretend a code diff is verification. |
| "It's just a text change, nothing visual shifted" | Text changes ARE visual changes. A longer headline can break layout. A shorter CTA can look lost in a big button. Render it. |
| "I'll verify after a few more changes" | No. Verify each change individually. Batching changes without verification means you won't know which one broke the layout when something goes wrong on the 4th edit. |
