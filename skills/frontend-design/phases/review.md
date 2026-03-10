# Phase 6: Design Review

**When to read**: After Live Testing.
**Runs in subagent**: `frontend-reviewer` (Haiku)

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
