---
name: frontend-magic
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics.

**Workflow**: Discovery → **Design Plan (Plan Mode + Wireframes)** → Style Guide → Copywriting → Staged Build → Live Test → Design Review → **Refinement (Plan Mode for significant changes)** → Ship

**Flags**:
- `--setup` — First-time setup wizard. **Read `setup.md`** and walk through it.
- `--walkthrough` — Interactive guided tour. **Read `walkthrough.md`** and present conversationally.

---

## Phase-Scoped Loading

**Each phase has its own file.** Read the phase file when entering that phase — not before. This keeps context lean for multi-round revision conversations.

| Phase | File | When to Read |
|-------|------|-------------|
| 0+1: Tool Check + Discovery | `phases/discovery.md` | Start of every build |
| 2: Design Plan (PLAN MODE) | `phases/design-plan.md` | After Discovery — enters Plan Mode, presents ASCII wireframes |
| 2.5: Style Guide | `phases/style-guide.md` | After plan approval |
| 3: Copywriting | `phases/copywriting.md` | Before build (if page has copy) |
| 4: Staged Build | `phases/build.md` | After copy is ready |
| 5: Live Testing | `phases/testing.md` | After build completes |
| 6: Design Review | `phases/review.md` | After testing |
| 7: Refinement (PLAN MODE for significant changes) | `phases/refinement.md` | After first delivery — re-read EVERY round |
| 8: Ship + Memory + Learn | `phases/ship.md` | When user says "ship it" |

**Also read at the indicated phase:**
- `aesthetics.md` — Typography, color, motion, composition, responsive design. **Read during Design Plan and Staged Build.**
- `component-libraries.md` — Framework/library detection and integration. **Read during Discovery.**
- `assets/style-guide-template.html` — HTML template for the visual style guide. **Read during Style Guide.**
- `learnings.md` — Cross-project patterns and auto-generated anti-patterns. **Read during Design Plan** to avoid known pitfalls.

**Do not read:**
- `memory.md` — Template only. Read/write `.frontend-magic-memory.md` in the project's working directory instead.

---

## Context Management & Model Routing

**You are the orchestrator.** You handle conversation, creative direction, and coordination. Heavy work runs in subagents with fresh context on cost-efficient models.

### What stays in your context (interactive with user):
- Phase 0: Tool Check — quick detection, a few lines
- Phase 1: Discovery — Q&A with user, can't delegate a conversation
- Phase 2: Design Plan — **runs in Plan Mode**. ASCII wireframes (desktop + mobile), visual direction, user iterates on layout before code exists. No code can be written until user approves.
- Phase 2.5: Style Guide — template population, browser preview, quick iteration
- Phase 7: Revisions — feedback loop. **Significant changes (layout, theme, scope, voice) re-enter Plan Mode** with updated wireframes. Quick tweaks stay inline.

### What runs in subagents (no user interaction needed):

| Phase | Agent | Model | Why |
|-------|-------|-------|-----|
| 3: Copywriting | `implementer` | Sonnet | Voice-sensitive content generation — needs nuance |
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
- **Read the phase file on entry, not in advance.** Phase 7's refinement rules don't need to be in your context during Discovery.

---

## Cross-Project Learning

This skill evolves across projects. Two mechanisms:

### Per-Project Memory (project-specific)
`.frontend-magic-memory.md` in the project's working directory. Captures brand, preferences, revision patterns for THIS project. Read during Discovery, updated after shipping.

### Cross-Project Learnings (global)
`learnings.md` in this skill directory. Captures patterns that apply across ALL projects — common revision triggers, generated anti-patterns, design patterns that consistently work. Read during Design Plan, updated after shipping via the Learning Extraction step in `phases/ship.md`.

**The evolution loop:**
```
Build ships → Update project memory → Run Learning Extraction
                                          ↓
                               Check: does this revision pattern
                               exist across 2+ projects?
                                          ↓
                                   Yes → Add to learnings.md
                                   No  → Keep in project memory only
```

Anti-patterns are auto-generated when the same failure appears across multiple projects. They use the same format as the tables below — an excuse the model tells itself, paired with the reality.

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

**Also check `learnings.md`** — it may contain additional anti-patterns generated from real revision data across past projects.

**If you catch yourself reaching for a "safe" choice — stop.** That's rationalization. The safe choice is the generic choice. Pick the interesting one.

Remember: Claude is capable of extraordinary creative work. Don't hold back.
