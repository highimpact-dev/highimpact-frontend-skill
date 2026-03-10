# Frontend Aesthetics Guidelines

Reference file for the frontend-design skill. Read this during Design Plan and Staged Build phases.

---

## Typography

Choose a font pairing that matches BOTH the aesthetic direction AND the audience context. The goal is character, not shock value.

### Use the font selector

During Phase 2 (Design Plan), run the font selector script to get mood-matched recommendations from Google Fonts' 1,500+ quality-scored database:

```bash
python3 ~/.claude/skills/frontend-design/scripts/select-fonts.py \
  '{"Calm": 80, "Sincere": 70, "Business": 50}'
```

**How to set mood weights:** Derive them from the conceptual anchor. A "warm Nashville law office" maps to Calm: 85, Sincere: 75, Business: 50, Competent: 60. A "quantum computing SaaS" maps to Futuristic: 85, Competent: 75, Innovative: 70. Pick 3-5 moods that capture the anchor's personality.

Available mood dimensions (0-100):
Active, Artistic, Awkward, Business, Calm, Childlike, Competent, Cute, Excited, Fancy, Futuristic, Happy, Innovative, Loud, Playful, Rugged, Sincere, Sophisticated, Stiff, Vintage

The script returns recommended pairings (display + body) with category contrast built in. It automatically excludes overused defaults (Inter, Roboto, Open Sans, Poppins, Montserrat, etc.) and filters novelty fonts out of body candidates.

### Font selection principles
- Max 2 fonts (one display, one body)
- Extreme contrast between them (serif + sans-serif, heavy + light, decorative + clean)
- Body font must be readable above all else — the selector enforces this
- **Match the font's personality to the product's audience.** A blackletter font says "authority" on a whiskey label but "unreadable" on a SaaS dashboard. Context determines whether a choice is bold or just wrong.
- The selector gives you candidates — you still choose. If a recommendation doesn't feel right for the project, pick another from the list or adjust the mood weights.

---

## Color & Theme

Commit to a cohesive aesthetic. Use CSS variables for consistency.

**Dominant + accent** outperforms timid, evenly-distributed palettes. Pick a strong primary, a sharp accent, and let the rest support.

**Dark theme is not the default.** Dark-on-light, light-on-dark, warm neutrals, colored backgrounds, split themes — all valid. If your instinct says "dark background," interrogate it. Is dark *right for this context*, or is it the path of least resistance?

A cream-and-charcoal editorial page, a sun-bleached pastel landing page, or a stark white brutalist layout can be just as striking as dark mode. Choose the theme that serves the metaphor, not the one that feels "safe."

### Color accessibility
- Text contrast: minimum 4.5:1 ratio (WCAG AA) for body text, 3:1 for large text
- Don't rely on color alone to convey information — use shape, text, or icons as backup
- Test your palette with a contrast checker. Beautiful AND readable is the standard.

---

## Motion & Animation

Use animations for delight and clarity, not decoration.

### Priorities
- **CSS-only** for HTML projects. `@keyframes`, `transition`, `animation-delay` for staggered reveals.
- **Motion library** (Framer Motion) for React when available.
- **One signature moment** > scattered micro-interactions. A well-orchestrated page load with staggered reveals creates more delight than random hover effects.

### High-impact patterns
- Staggered entrance animations with `animation-delay` on section elements
- Scroll-triggered reveals (IntersectionObserver or CSS `animation-timeline`)
- Hover states that surprise (scale + shadow, color shift, underline reveal)
- Smooth transitions on interactive elements (toggles, tabs, accordions)

### What to avoid
- Animation for animation's sake — every motion should have purpose
- Jarring or fast animations (ease-out, 200-400ms for most transitions)
- Layout-triggering animations (stick to `transform` and `opacity` for performance)

---

## Spatial Composition

Break predictable patterns. Not every page needs to be centered content in a max-width container.

### Techniques
- **Asymmetric layouts**: Content weighted to one side, image/decoration on the other
- **Overlap**: Elements that break out of their containers, overlapping sections
- **Diagonal flow**: Angled section dividers, rotated decorative elements
- **Grid-breaking**: Most content on a grid, one element that intentionally breaks it for emphasis
- **Generous negative space**: Let sections breathe. Cramped layouts feel cheap.
- **Controlled density**: Alternatively, intentional information density (dashboards, data-heavy pages)

### The rule
Unexpected layouts are only good if they're usable. Test mentally: can a user scan this and find what they need? If asymmetry confuses the hierarchy, it's not bold — it's broken.

---

## Responsive Design

Mobile is not an afterthought. Half your traffic is phones.

### Mobile-first approach
Start with the mobile layout. Layer complexity upward. This forces you to identify what's essential.

### Breakpoint strategy
- **375px** — Mobile (iPhone SE/mini). Single column. Stack everything. Generous touch targets.
- **768px** — Tablet. Two-column layouts emerge. Side-by-side where it helps.
- **1024px** — Small desktop. Full layout takes shape.
- **1280px+** — Large desktop. Max-width containers prevent ultra-wide stretching.

### Mobile-specific considerations
- **Touch targets**: Minimum 44x44px for interactive elements. No tiny links or buttons.
- **Font sizes**: Body text minimum 16px on mobile (prevents iOS zoom). Headlines scale down but stay readable.
- **Navigation**: Hamburger menu or bottom nav on mobile. Don't try to fit desktop nav on a phone.
- **Images**: Use responsive images (`srcset` or CSS `object-fit`). Don't send 2000px images to phones.
- **Spacing**: Reduce section padding on mobile but don't eliminate it. Cramped mobile = unusable.
- **Horizontal scroll**: Never. If something overflows horizontally on mobile, fix it.

### What changes at breakpoints
- **Layout**: Single column → multi-column
- **Typography**: Scale headings down proportionally. Body stays 16px+.
- **Navigation**: Mobile nav pattern → desktop nav
- **Images/decorations**: Simplify or hide purely decorative elements on mobile
- **Interactions**: Hover effects don't exist on touch. Replace with tap feedback.

### The test
Look at your mobile layout in isolation. Does it feel like a designed experience, or a squished desktop page? If it's the latter, redesign it — don't just shrink it.

---

## Backgrounds & Visual Atmosphere

Create depth and mood. Never default to solid-color rectangles.

### Techniques
- **Gradient meshes**: Multi-point gradients that create organic color fields
- **Noise/grain textures**: SVG filter or CSS `background-image` with a noise pattern. Adds warmth and tactility.
- **Geometric patterns**: Repeating shapes, dots, lines as subtle background texture
- **Layered transparencies**: Semi-transparent elements stacked for depth
- **Dramatic shadows**: Large, soft shadows create hierarchy and lift
- **Decorative borders**: Custom borders that serve the metaphor (dashed for blueprints, rough for organic, clean for minimal)
- **Vignettes**: Subtle darkening at edges to draw focus to center content
- **Custom cursors**: When appropriate for the aesthetic (use sparingly)

### The atmosphere test
Remove all text from your design mentally. Is there still visual interest? If you're looking at flat colored rectangles, the atmosphere is missing. Add texture, gradient, depth, or pattern.

---

## Design Quality Standards

Every output must be:
- **Complete** — Real content, real data, real interactions. No placeholders, no lorem ipsum, no empty tables, no "coming soon." Scope down before you code, not after.
- **Visually striking** — Someone should remember this page.
- **Cohesive** — Clear aesthetic point-of-view threaded through every detail.
- **Meticulously refined** — Details matter. Shadow depths, border radii, spacing consistency, color values.
- **Responsive** — Works on mobile, tablet, and desktop. Not "kinda works" — designed for each.

### Matching complexity to vision
Maximalist designs need elaborate code with extensive animations and effects. Minimalist designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well, not from adding more.

NEVER use generic AI aesthetics: overused fonts (Inter, Roboto, Arial, system fonts), cliched colors (purple gradients on white), predictable layouts, cookie-cutter design without context-specific character.
