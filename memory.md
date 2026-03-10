# Frontend Design Memory — Template

This is the template for per-project memory files. The orchestrator creates `.frontend-design-memory.md` in the project's working directory on first use.

**The skill does NOT use this file directly.** It reads/writes the project-local copy.

---

## How It Works

1. **First build in a project**: Orchestrator creates `.frontend-design-memory.md` in the project root from this template
2. **Every build**: Orchestrator reads the project's memory file during Discovery
3. **After shipping/revisions**: Orchestrator updates the project's memory file with what it learned
4. **Users can**: edit it directly, gitignore it, or delete it to reset

## Template (copied to project on first use)

```markdown
# Frontend Design Memory

Persistent memory for this project's design preferences. Read by the frontend-design skill during Discovery, updated after shipping.

**To reset**: delete this file. A new one will be created on the next build.

---

## Brand & Identity
<!-- Project-specific brand details: colors, voice, audience, positioning -->


## Design Preferences
<!-- Visual choices that were approved or praised. What "good" looks like for this project. -->


## Voice & Copy
<!-- Tone, vocabulary, CTA style. What copy landed vs got revised. -->


## Revision Patterns
<!-- Feedback that repeated = a preference the skill missed. Captured so it doesn't repeat. -->


## Approved Directions
<!-- Design plans that were approved. Brief notes on what worked about them. -->

```
