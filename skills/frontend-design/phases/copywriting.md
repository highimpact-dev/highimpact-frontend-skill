# Phase 3: Copywriting

**When to read**: After Style Guide is approved (or skipped), before Build.
**Runs in subagent**: `implementer` (Sonnet) with copywriter instructions

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
subagent_type: "implementer"
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
