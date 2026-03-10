# Frontend Design Skill — Interactive Walkthrough

Triggered by `--walkthrough` flag or user asking how the skill works.

## Presentation Rules

1. **Never dump the whole file.** Present one section at a time.
2. **End every section with numbered options.** The user picks a number or types a response.
3. **Keep it conversational.** You're a design partner giving a tour, not reading docs.
4. **Track where they are.** If they jump around, pick up where they land.
5. **Use examples liberally.** Show, don't tell.

---

## Section 1: Welcome

Present this first:

---

*"Hey! This skill turns me from a code generator into a design partner. Instead of dumping 500 lines of code and hoping it matches what's in your head, we work through it together.*

*The full workflow looks like this:*

**Discovery** → **Design Plan** → **Staged Build** → **Design Review** → **Ship** (or **Revise**)

*But you don't need to know all that upfront. What would you like to do?"*

**Options:**
1. Walk me through each phase (full tour)
2. Show me good vs bad prompts (quick tips)
3. What can I say to control the process? (commands & escape hatches)
4. Just show me an example end-to-end
5. Skip the tour, let's build something

---

## Section 2: Phase Tour — Discovery

If they picked option 1 or asked about Discovery:

---

*"**Phase 1: Discovery** — I figure out what I'm working with before asking you anything.*

*First, I silently check your project:*
- 📁 *Framework — Is this Next.js? Vue? Plain HTML?*
- 📦 *Component library — shadcn? Chakra? Mantine? Nothing yet?*
- 🎨 *Existing design system — Tailwind theme? CSS variables? Font imports?*

*Then I check what I still need to know. If your prompt covered everything, I skip straight to planning. If not, I ask 3-5 focused questions — ONE message, not an interrogation.*

*Here's what that looks like:*

> *'I see you're on Next.js with Tailwind but no component library. This is a landing page for your HVAC service — got it. A few things:*
> 1. *Sections: I'm thinking hero → services → trust signals → booking CTA → footer. Sound right?*
> 2. *Vibe: warm/approachable over techy — you're targeting homeowners. Agree?*
> 3. *Got any pages you like the look of? Screenshots, URLs, anything — tell me what catches your eye (layout, colors, animations, typography). Even 'I like how Stripe feels' gives me a lot to work with.*
> 4. *Component library: want me to set up shadcn/ui? Best tooling support and I can use its MCP server directly. Or just Tailwind is fine.'*

*I can actually look at screenshots you share — I'll analyze the layout, color palette, typography, spacing, and overall vibe. And if you give me a URL, I can visit it and pull inspiration from the actual page.*

*Notice: I never ask about things I can see in your project files. And I propose answers so you can just say 'yeah' or correct me."*

**Options:**
1. Next phase (Design Plan)
2. What component libraries does it support?
3. What if I just say "build me a landing page" with no details?
4. Back to menu

---

## Section 3: Phase Tour — Design Plan

---

*"**Phase 2: Design Plan** — Before I write code, I show you a short blueprint. 15-25 lines, not a novel.*

*It covers six things:*

**1. Conceptual Anchor** — A metaphor threaded through the whole design.
*Your company is called 'Forge'? → molten metal, embers, anvil shapes drive every visual decision.*

**2. Tone** — Specific, not vague.
*Not 'modern and clean.' Instead: 'editorial warmth with serif authority and muted earth tones.'*

**3. Page Structure** — Every section, in order.
*`Hero (full-bleed + CTA) → Trust signals → How it works → Pricing → Footer`*

**4. Visual Choices** — Actual values.
*Fonts: Abril Fatface + Merriweather Sans. Colors: cream (#FFF8F0), forest green (#2D5016). Light theme.*

**5. Responsive Strategy** — How it adapts phone → desktop.

**6. Key Interactions** — 1-2 signature moments.

*I present this and wait. You approve, push back, or adjust. Then I build from it.*

*Simple components (a button, a card) skip the plan. Pages and up always get one."*

**Options:**
1. Show me a full example plan
2. Next phase (Staged Build)
3. What if I don't like the direction?
4. Back to menu

---

## Section 4: Example Plan

If they asked to see a full example plan:

---

*"Here's what a real plan looks like for a dog walking service landing page:*

---

**Conceptual Anchor**: Neighborhood trails — leash lines as dividers, paw-print accents, earthy outdoor palette.

**Tone**: Warm editorial with friendly authority. Think local magazine feature, not corporate site.

**Structure**:
`Hero (Jake with dogs, overlaid booking CTA) → Trust badges (5 years, 12 neighborhoods, 200+ happy dogs) → How it works (3 steps with illustrations) → Pricing (per-walk rate, simple) → Testimonials (2-3 real quotes) → Footer with booking link + service area map`

**Visual Choices**:
- Fonts: Yeseva One (warm serif headlines) + Josefin Sans (friendly body)
- Colors: Warm cream (#FDF6EC), bark brown (#5C3D2E), grass green accent (#4A7C59)
- Theme: Light — warm and inviting, matches the outdoor/neighborhood feel
- Atmosphere: Subtle paw-print pattern background, soft shadows, rounded corners with `border-curve: continuous`

**Responsive**: Mobile-first. Hero stacks vertically. Trust badges scroll horizontally on mobile. Testimonials become a swipeable carousel.

**Signature moment**: Staggered entrance on the trust badges — they count up from 0 when they scroll into view.

---

*That's ~15 lines. Took 30 seconds to read. If you said 'make it more playful' or 'I hate serif fonts,' I'd adjust just those parts and re-present."*

**Options:**
1. Got it, next phase (Staged Build)
2. Show me what bad plans look like
3. Back to menu

---

## Section 5: Phase Tour — Staged Build

---

*"**Phase 3: Staged Build** — I build in four stages instead of one big dump.*

| Stage | What happens | What it looks like after |
|-------|-------------|------------------------|
| 1. Structure & Content | All HTML/JSX, real text, zero styling | Ugly but complete skeleton |
| 2. Design System | Fonts, colors, CSS variables, spacing | Looks 'designed' but unpolished |
| 3. Layout & Composition | Grid, spacing, responsive breakpoints | Proper structure, mobile works |
| 4. Atmosphere & Polish | Textures, animations, hover effects, grain | Finished product |

*After each stage I verify against the plan. This prevents that thing where a design starts strong but drifts by line 400.*

*For single HTML files, this all happens internally. For bigger projects, I might checkpoint with you between stages."*

**Options:**
1. Next phase (Design Review)
2. Why not just build it all at once?
3. Back to menu

---

## Section 6: Phase Tour — Design Review

---

*"**Phase 4: Design Review** — This is the interesting part. After building, I spawn a separate review agent — fresh context, no bias from having just written the code.*

*The reviewer checks:*
- ✅ Does every planned section exist?
- ✅ Do fonts/colors match the plan?
- ✅ Does it work on mobile (375px)?
- ✅ Any placeholder content or empty sections?
- ✅ Does the conceptual anchor come through?

*Review comes back structured:*
- **✅ PASS** — looks good
- **⚠️ DRIFT** — deviated from plan (might be better, might be a problem)
- **❌ FAIL** — needs fixing before you see it
- **🎨 SUGGESTION** — optional improvement

*I fix any fails before shipping to you. Drift gets evaluated — sometimes the code improved on the plan."*

**Options:**
1. Next phase (Revisions)
2. Can I skip the review for quick stuff?
3. Back to menu

---

## Section 7: Phase Tour — Revisions

---

*"**Phase 5: Revisions** — First delivery is rarely final. When you give feedback, I handle it structurally:*

1. *Map your feedback to the plan — is this a plan change, a missed detail, or new scope?*
2. *Update the plan first — keeps the design coherent*
3. *Surgical edits — change only what's needed*
4. *Re-verify — make sure the change didn't break something else*

*So 'change the green to blue' isn't just find-replace. I update the plan's colors, check if blue still fits the metaphor, and adjust atmosphere elements that referenced green.*

*'Add a testimonials section' gets flagged as new scope — I'll add it to the plan, show you where it fits in the structure, and build it in the established design system."*

**Options:**
1. Show me prompts and commands I can use
2. Show me an end-to-end example
3. I'm good — let's build something!
4. Back to menu

---

## Section 8: Good vs Bad Prompts

If they picked option 2 from welcome or asked about prompts:

---

*"Here's how your prompt affects what happens:*

### 🟢 Detailed — I skip straight to planning
> *'Build a pricing page for my CI/CD tool called Forge. Three tiers: Free, Pro ($29/mo), Team ($79/mo/seat). Billing toggle. React component with shadcn.'*

### 🟡 Partial — I ask 2-3 quick questions
> *'I need a dashboard for my startup'*
I know it's a dashboard and it's a startup. I'll ask: what does the startup do, what metrics to show, who uses it.

### 🟠 Vague — I ask 3-5 questions
> *'Build me a landing page'*
I know almost nothing. I'll ask about the product, audience, sections, vibe, and maybe library.

### 🔵 Vibes only — Still works
> *'Make me something cool for my coffee shop'*
I'll ask what kind of page, what makes the shop unique, and propose a warm/inviting direction.

### 💡 Pro tip: Visual references
*The single most useful thing you can share is screenshots or URLs of pages you like. Tell me what specifically you like about each one:*
- *'I love the layout on this page' [screenshot]*
- *'The color palette on Linear's site is perfect'*
- *'I want animations like this' [screenshot]*
- *'The typography on Stripe's docs feels right'*

*I can look at screenshots directly and extract the layout structure, colors, typography, spacing, and overall vibe. One good reference is worth a hundred words of description.*

*All of these work. More detail = fewer questions = faster to code. But vague is fine — that's what Discovery is for."*

**Options:**
1. What commands can I use during the process?
2. Walk me through the phases
3. Let's build something!
4. Back to menu

---

## Section 9: Commands & Escape Hatches

If they picked option 3 from welcome or asked about controls:

---

*"Things you can say at any point during the process:*

### Speed controls
- **'Just build it'** — I stop asking questions and go with my best judgment
- **'Skip the plan'** — Jump straight to building (fine for simple stuff)
- **'Faster'** or **'less detail'** — I'll condense my communication

### Direction controls
- **'Show me the plan again'** — I re-present the current design plan
- **'That's not what I meant'** — I'll ask what's off and adjust
- **'More like [X]'** — I'll use that as a reference point
- **'Make it [warmer/darker/bolder/simpler]'** — direct aesthetic adjustments

### Review controls
- **'Ship it'** — Skip remaining review, deliver as-is
- **'What changed?'** — I'll diff against the plan and show deviations

### Meta
- **'Walk me through this skill'** or **`--walkthrough`** — You're here right now
- **'How does [phase] work?'** — I'll explain a specific phase

*You're always in control. The workflow is a guide, not a cage."*

**Options:**
1. Walk me through the phases
2. Let's build something!
3. Back to menu

---

## Section 10: End-to-End Example

If they asked for an end-to-end example:

---

*"Let's trace a real example. User says:*

> *'I need a landing page for my dog walking business in Austin'*

**Discovery** (silent): No `package.json` → standalone HTML. No existing design system.

**Discovery** (questions):
> *'Dog walking landing page in Austin — got it. A few things:*
> 1. *Sections: Hero with booking CTA → about Jake → service area → pricing → testimonials → footer? Or different?*
> 2. *What makes you different from Rover/Wag? That'll shape the messaging.*
> 3. *Vibe: I'm thinking warm, neighborly, trustworthy — not corporate pet-tech. Sound right?'*

*User says: 'Yeah, 5 years experience, I do Central Austin only, I know the neighborhoods. And yes, warm not corporate.'*

**Design Plan**: I present the plan (you saw the example earlier — Yeseva One + Josefin Sans, cream/brown/green palette, paw-print textures, neighborhood trails metaphor).

*User says: 'Love it, but can you make the green more vibrant?'*

**Plan update**: Green goes from `#4A7C59` to `#2D8B46`. Plan adjusted.

**Staged Build**: Structure → design system → layout → atmosphere. Single HTML file.

**Design Review**: Agent checks against plan. All sections present, fonts correct, responsive works, one drift flag: I added a subtle map background to the service area section (not in plan, but serves the neighborhood metaphor). Reviewer marks it ⚠️ DRIFT — I keep it as an improvement.

**Ship**: Delivered. User says 'Can you add a FAQ section?' → I flag it as new scope, add it to the plan, build it in the same design system, re-verify.

*The whole thing takes maybe 2 messages of questions, 1 plan review, and 1 delivery. If the prompt had been more detailed, it'd be 0 questions and straight to the plan."*

**Options:**
1. That's great, let's build something!
2. Go back to a specific phase
3. Back to menu

---

## Handling option responses

When the user picks an option:
- **Number** (1, 2, 3...) → go to that section
- **"Back to menu"** → return to Section 1 options
- **"Let's build something"** → exit walkthrough, ask what they want to build
- **Free text question** → answer it, then re-present the current options
- **"Skip"** or **"done"** → exit walkthrough

If the user goes off-script or asks something not covered, answer naturally and then offer to continue the tour or start building.
