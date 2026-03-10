# Phase 5: Live Testing

**When to read**: After Build completes.
**Runs in subagent**: `frontend-tester` (Sonnet)

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
