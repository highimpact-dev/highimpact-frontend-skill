# Phase 2: Design Plan (Plan Mode)

**When to read**: After Discovery, before writing code.
**Also read**: `aesthetics.md` (for typography, color, composition guidelines), `learnings.md` (for cross-project patterns)
**Mode**: This phase runs inside Plan Mode. Enter plan mode at the start. Do not exit until the user approves the wireframes.

---

## Phase 2: Design Plan

After Discovery, this phase transitions into **Plan Mode** — a read-only, design-only environment where no code can be written. This is intentional. The model cannot skip ahead to building. Every design decision gets user approval through visual wireframes before a single line of code exists.

### Entering Plan Mode

Call `EnterPlanMode` immediately after Discovery completes. Then follow the steps below **in order, one step per message**. Do not combine steps. Do not skip ahead.

---

### Step 1: Conceptual Anchor

**Present. Don't ask.**

State the metaphor that will drive every design decision. One sentence, bold and specific. The anchor is a decision-making framework — when you're unsure about any detail later, ask: "What would the metaphor do?"

> *"The anchor: **Nashville recording studio** — warm wood tones, analog dials, velvet acoustics, the glow of a tube amp in a dim room."*

Then immediately state what this means for the design direction in 2-3 lines:

> *"This means warm earth palette, not cool tech blues. Serif authority for headlines. Textured backgrounds — grain and warmth, not flat minimalism. Motion should feel analog — smooth easing, not snappy digital."*

**Wait for reaction.** If the user pushes back on the anchor, adjust before continuing. If they say nothing or give a thumbs up, proceed.

---

### Step 2: Visual Direction

**Present the specific visual choices derived from the anchor.** This is not a mood board — it's concrete values.

Format exactly like this:

```
VISUAL DIRECTION
────────────────
Fonts:     [Display font] + [Body font] (from font selector — run it before entering plan mode)
           Why: [one line connecting the pairing to the anchor]
Colors:    Primary [#hex name] · Accent [#hex name] · Background [#hex name] · Text [#hex name] · Surface [#hex name] · Muted [#hex name]
Theme:     [Light / Dark / Warm / Split] — [why, connected to the anchor]
Atmosphere:[Textures, gradients, grain, depth — what creates mood beyond flat rectangles]
```

**Ask one specific question:**
> *"This is the visual foundation. Anything feel wrong — fonts, colors, overall mood? I'd rather adjust now than after 500 lines of code."*

**Wait for the user to respond.** Do not proceed until they react.

---

### Step 3: Page Structure

**Present the ordered list of sections with one-line descriptions:**

```
PAGE STRUCTURE
──────────────
1. Nav         — Sticky, logo left, links right, glass effect
2. Hero        — Full-bleed image left, headline + CTA right
3. Trust       — Logo strip, "trusted by" social proof
4. Features    — 3-column cards with icons, staggered entrance
5. Testimonial — Large quote, photo, asymmetric layout
6. Pricing     — 3-tier cards, popular tier highlighted
7. CTA         — Final conversion section, bold headline
8. Footer      — Links, social, newsletter signup
```

**Do not ask for approval yet.** This list feeds directly into the wireframe in the next step.

---

### Step 4: Desktop Wireframe (MANDATORY)

**This is the centerpiece of plan mode. Do not skip this. Do not summarize it. Draw it.**

Present a full ASCII wireframe of the desktop layout (1280px viewport). Every section from Step 3 must appear. Label everything. Show spatial relationships — what's next to what, relative sizing, alignment.

**Wireframe format rules:**
- Use box-drawing characters: `┌ ┐ └ ┘ ├ ┤ ┬ ┴ ─ │ ┼`
- Label every section and element
- Show relative proportions (a hero takes more vertical space than a nav)
- Indicate interactive elements with `[ brackets ]`
- Show images/media as labeled boxes
- Annotate key design notes in parentheses where helpful

**Example quality standard:**

```
┌──────────────────────────────────────────────────────┐
│  LOGO                          [About] [Work] [▤ Menu]│
├──────────────────────────────────────────────────────┤
│                                                      │
│  ┌─────────────────────┐  We build things that       │
│  │                     │  matter.                     │
│  │      HERO IMAGE     │  ───────────────────         │
│  │                     │  Subtext about the product   │
│  │                     │  and what makes it different  │
│  │                     │                              │
│  └─────────────────────┘  [ Get Started ]             │
│                                                      │
│  (asymmetric: image 55%, copy 45%, left-weighted)    │
├──────────────────────────────────────────────────────┤
│          ★★★★★  "Trusted by 2,000+ teams"            │
│  [logo] [logo] [logo] [logo] [logo] [logo]          │
├──────────────────────────────────────────────────────┤
│                                                      │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│   │   icon   │   │   icon   │   │   icon   │        │
│   │          │   │          │   │          │        │
│   │ Feature  │   │ Feature  │   │ Feature  │        │
│   │ Title    │   │ Title    │   │ Title    │        │
│   │          │   │          │   │          │        │
│   │ Short    │   │ Short    │   │ Short    │        │
│   │ desc     │   │ desc     │   │ desc     │        │
│   └──────────┘   └──────────┘   └──────────┘        │
│                                                      │
│   (3-col grid, staggered entrance animation)         │
├──────────────────────────────────────────────────────┤
│                                                      │
│   "The best tool we've ever          ┌────────────┐  │
│    used for our workflow.            │            │  │
│    Changed everything."              │   PHOTO    │  │
│                                      │            │  │
│    — Sarah Chen, VP Engineering      └────────────┘  │
│                                                      │
│   (asymmetric: quote 60%, photo 40%)                 │
├──────────────────────────────────────────────────────┤
│              PRICING SECTION                         │
│   ┌──────────┐  ┌═══════════╗  ┌──────────┐        │
│   │  Starter │  ║  Popular  ║  │  Enterprise│        │
│   │  $29/mo  │  ║  $79/mo   ║  │  Custom   │        │
│   │  ······  │  ║  ·······  ║  │  ······   │        │
│   │  ······  │  ║  ·······  ║  │  ······   │        │
│   │ [Choose] │  ║ [Choose]  ║  │ [Contact] │        │
│   └──────────┘  ╚═══════════╝  └──────────┘        │
│                                                      │
│   (middle tier highlighted with double border)       │
├──────────────────────────────────────────────────────┤
│                                                      │
│        Ready to get started?                         │
│        [ Start your free trial ]                     │
│                                                      │
├──────────────────────────────────────────────────────┤
│  LOGO   [About] [Blog] [Careers]    [tw] [gh] [li]  │
│          © 2026 Company Name                         │
└──────────────────────────────────────────────────────┘
```

**After presenting the wireframe, ask:**
> *"This is the desktop layout. Look at the spatial relationships — what's next to what, how much space each section gets, where the eye flows. Want anything moved, resized, added, or cut?"*

**Stay in this step until the user approves the desktop layout.** If they request changes, redraw the affected sections (or the full wireframe if the change is structural). Do not move to mobile until desktop is approved.

---

### Step 5: Mobile Wireframe (MANDATORY)

**Show how the desktop layout adapts to 375px.** This is not optional. Mobile is half the traffic.

Draw the mobile wireframe. Show what stacks, what reorders, what hides, and what changes size. The mobile layout should feel **designed**, not collapsed.

**Example:**

```
┌──────────────────────┐
│  LOGO          [▤]   │
├──────────────────────┤
│                      │
│  We build things     │
│  that matter.        │
│  ─────────────       │
│  Subtext here        │
│                      │
│  [ Get Started ]     │
│                      │
│  ┌────────────────┐  │
│  │   HERO IMAGE   │  │
│  │                │  │
│  └────────────────┘  │
│                      │
│  (image moves below  │
│   copy on mobile)    │
├──────────────────────┤
│  ★★★★★ Trusted by   │
│  2,000+ teams        │
│  [logo] [logo]       │
│  [logo] [logo]       │
├──────────────────────┤
│  ┌────────────────┐  │
│  │ icon  Feature  │  │
│  │       Title    │  │
│  │       desc     │  │
│  └────────────────┘  │
│  ┌────────────────┐  │
│  │ icon  Feature  │  │
│  │       Title    │  │
│  │       desc     │  │
│  └────────────────┘  │
│  ┌────────────────┐  │
│  │ icon  Feature  │  │
│  │       Title    │  │
│  │       desc     │  │
│  └────────────────┘  │
│                      │
│  (cards stack, icon  │
│   moves to inline)   │
├──────────────────────┤
│        ...           │
└──────────────────────┘
```

**Ask:**
> *"Here's how it stacks on mobile. Does the order feel right? Anything that should be prioritized differently on a small screen?"*

**Stay here until mobile is approved.**

---

### Step 6: Interaction Callouts

**Annotate 1-2 signature animation moments.** Not a laundry list — the key moments that give the page life.

Present as annotations referencing the wireframe:

```
INTERACTIONS
────────────
1. Hero entrance: Headline slides in from left (300ms ease-out),
   image fades in from right (400ms, 100ms delay). Feels like
   a curtain opening.

2. Feature cards: Staggered entrance as they scroll into view.
   Each card fades up with 100ms delay between them. Subtle
   but creates rhythm.

3. Testimonial quote: Typewriter reveal on the quote text when
   section enters viewport. Matches the "analog" anchor.
```

**Ask:**
> *"These are the signature moments — where the page comes alive. Right amount of motion? Too much? Want a different kind of entrance?"*

---

### Step 7: Lock the Plan and Exit

When the user has approved:
- Conceptual anchor
- Visual direction
- Desktop wireframe
- Mobile wireframe
- Interactions

**Write the complete Design Plan to the plan file.** Include all of the above — the anchor, visual direction block, page structure, both wireframes, and interaction callouts. This plan file becomes the contract passed to every subagent.

**Then call `ExitPlanMode`** with allowed prompts for the build phases:
- Bash: "run font selector script"
- Bash: "start local dev server"
- Bash: "run build commands"

**Do not exit plan mode until you have explicit approval on at least the desktop wireframe.** Silence after presenting the wireframe is not approval — ask again.

---

### Scope Gating

Not everything needs the full wireframe treatment:

| Scope | Plan mode? | Wireframe? |
|-------|-----------|------------|
| Simple component (button, card, nav) | No | No — just build it |
| Single section or small component | No | No — describe and build |
| Single page with 3+ sections | **Yes** | **Yes** — desktop + mobile |
| Multi-page app | **Yes** | **Yes** — wireframe each page |

---

### Plan Mode Rules (NON-NEGOTIABLE)

1. **One step per message.** Do not dump the anchor, visual direction, and wireframe in one wall of text. The user needs space to react to each piece.
2. **Wait for the user between steps.** If they haven't responded, do not proceed. Ask again if needed.
3. **Wireframes are mandatory for pages.** No exceptions. No "I'll describe the layout instead." Draw it.
4. **Both desktop AND mobile wireframes.** Desktop alone is half a design.
5. **Stay in plan mode until wireframes are approved.** The exit gate is explicit user approval.
6. **If the user says "just build it" mid-planning** — present the wireframe anyway, but compress steps 1-6 into a single message. They can approve or redirect in one shot. Respect their urgency, but don't skip the spatial checkpoint.
7. **Never exit plan mode silently.** Always confirm: "Plan locked — building now."

### Font Selector Timing

The font selector script requires Bash, which is blocked in plan mode. **Run it during Discovery (Phase 1) before entering plan mode.** Present the font recommendation as part of Step 2's visual direction.

If fonts weren't selected during Discovery, note the gap and present placeholder font direction. After exiting plan mode, run the selector and update the plan before passing it to the builder.

---

### Planning Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "The user just wants code fast" | A wireframe takes 30 seconds to scan. A wrong-direction rebuild takes 10 minutes. The wireframe IS the fast path. |
| "I already know what to build" | Then the wireframe takes 10 seconds to draw. If you can't draw it, you don't know the layout. |
| "Planning kills creative flow" | Planning IS creative work. The wireframe is where layout decisions happen. Code is just implementation. |
| "This is simple enough to skip" | If it has more than 2 sections, wireframe it. "Simple" pages with wrong layouts still need rebuilding. |
| "I'll describe the layout in words" | Words are ambiguous. "Hero with image on the right" could be 40/60, 50/50, 30/70, overlapping, or inset. The wireframe removes ambiguity. |
| "The user didn't ask for a wireframe" | They didn't ask for a wrong layout either. The wireframe prevents the thing they'd actually complain about. |
| "ASCII art looks unprofessional" | It looks like a design process. Users know wireframes. It's how real designers work before mockups. |
| "I can't draw complex layouts in ASCII" | You can. Box-drawing characters, labels, and annotations communicate any layout. If the layout is too complex to wireframe, it's too complex to build without one. |
| "Mobile is basically the same but stacked" | Mobile is a different design. Stacking is the lazy default. Show how the hierarchy changes, what reorders, what hides. |
| "I'll just show the desktop wireframe" | No. Mobile is mandatory. Half the traffic, different constraints, different design. |
