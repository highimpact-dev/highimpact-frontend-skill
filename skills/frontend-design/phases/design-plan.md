# Phase 2: Design Plan

**When to read**: After Discovery, before writing code.
**Also read**: `aesthetics.md` (for typography, color, composition guidelines)

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
