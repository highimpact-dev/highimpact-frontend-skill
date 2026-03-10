# Phase 2.5: Style Guide

**When to read**: After Design Plan is approved.
**Also read**: `assets/style-guide-template.html` (template to populate)

---

## Phase 2.5: Style Guide

After the Design Plan is approved, generate a visual style guide so the user can **see** the fonts, colors, and atmosphere rendered in the browser before committing to a full build. This catches "I don't like that font" at the cheapest possible moment — editing a hex value in a 50-line file, not hunting through 500 lines of page code.

### How it works:

1. **Read the template** at `~/.claude/skills/frontend-design/assets/style-guide-template.html`
2. **Replace the placeholders** with values from the Design Plan:

| Placeholder | Source |
|---|---|
| `{{PROJECT_NAME}}` | Product/brand name from Discovery |
| `{{FONT_IMPORTS}}` | `<link>` tags for Google Fonts (both display + body) |
| `{{FONT_DISPLAY}}` / `{{FONT_BODY}}` | CSS font-family values from the plan |
| `{{FONT_DISPLAY_NAME}}` / `{{FONT_BODY_NAME}}` | Human-readable font names |
| `{{COLOR_BG}}`, `{{COLOR_TEXT}}`, `{{COLOR_PRIMARY}}`, `{{COLOR_ACCENT}}`, `{{COLOR_SURFACE}}`, `{{COLOR_MUTED}}` | Hex values from the plan's color palette |
| `{{SAMPLE_HEADLINE}}` | A short headline that fits the brand (3-6 words) |
| `{{PAIRING_PREVIEW_HEADLINE}}` | A realistic headline for the font pairing card |
| `{{PAIRING_PREVIEW_BODY}}` | A realistic paragraph for the font pairing card |
| `{{ANCHOR_METAPHOR}}` | The conceptual anchor as a short phrase |
| `{{ANCHOR_DESCRIPTION}}` | 1-2 sentences explaining how the metaphor drives design choices |
| `{{ATMOSPHERE_CSS}}` | Inline CSS for the atmosphere preview: `background`, gradients, colors |
| `{{ATMOSPHERE_OVERLAY_CSS}}` | Overlay effects: grain texture, noise, vignette (or empty) |
| `{{ATMOSPHERE_TEXT_COLOR}}` | Text color that works on the atmosphere background |
| `{{ATMOSPHERE_HEADLINE}}` | Short headline for the atmosphere preview |
| `{{ATMOSPHERE_DESCRIPTION}}` | Brief description of the mood/atmosphere |

3. **Write the populated file** to `/tmp/style-guide-{{project}}.html`
4. **Open it in the browser** — use Chrome DevTools MCP if available, otherwise tell the user to open it
5. **Screenshot and present** to the user with a brief note:
   > *"Here's how the visual foundation looks rendered. Fonts, colors, buttons, and atmosphere — all from the plan. Anything feel off?"*

### What the user sees:

- **Conceptual anchor** — the metaphor driving all decisions, with explanation
- **Typography scale** — H1-H4, body, small text in the actual fonts on the actual background
- **Font pairing preview** — a realistic headline + paragraph in a card, showing how they work together
- **Color palette** — swatches with hex values and WCAG contrast ratios calculated live
- **Buttons** — primary, secondary, accent, ghost states in the palette
- **Atmosphere preview** — a section showing the gradient/texture/mood from the plan
- **Sample cards** — simple components showing how the palette works in practice

### Handling feedback:

- **"Love it"** → proceed to Copywriting
- **"The body font feels too thin"** → update the plan's font choice, regenerate the style guide, re-present
- **"That accent color clashes"** → swap the hex value in the plan and style guide, re-present
- **"The atmosphere is too dark/intense"** → adjust the atmosphere CSS, re-present

Each iteration is just a find-and-replace on the template — no code to rewrite.

### When to skip:

- **Simple components** (button, card, nav) that skipped the plan
- **User said "just build it"** — respect their urgency
- **Returning project with established memory** — if `.frontend-magic-memory.md` has approved colors/fonts from a previous build, the user already knows what these look like

### Style Guide Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "The plan already describes the visual choices" | Describing "#FFF8F0 warm cream" and *seeing* it rendered are different evaluations. Users can't judge a font pairing from its name. |
| "This adds another step" | It replaces the step where the user sees the full build and says "I don't like the font." That step costs 10x more. |
| "I'll just build the page and they can iterate" | Iterating on a 50-line style guide takes seconds. Iterating on a 500-line page takes a full revision round. |
| "The user already approved the plan" | They approved the *idea*. The style guide shows them the *reality*. These are different things. |
