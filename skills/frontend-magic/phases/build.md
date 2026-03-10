# Phase 4: Staged Build

**When to read**: After Copywriting, before Live Testing.
**Runs in subagent**: `frontend-builder` (Sonnet)

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
