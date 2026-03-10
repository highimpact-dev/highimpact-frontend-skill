# Phase 0 & 1: Tool Check + Discovery

**When to read**: At the start of every new build request.
**Also read**: `component-libraries.md` (for detection rules)

---

## Phase 0: Tool Check (first use only)

On the first interaction, silently check what tools are available. **Read `setup.md`** for the full guided setup flow.

**Quick check:**
- Can you access `mcp__claude-in-chrome__*` tools? → Browser testing available
- Is Playwright skill listed? → Headless testing available
- Does `shadcn info --json` work? → shadcn CLI installed
- Are shadcn MCP tools available? → Component browsing available

**If must-have tools are missing** (no browser tools AND no shadcn), briefly mention it:
> *"Hey — quick heads up before we start. I can build without any extra tools, but I'll be a lot better with a couple things installed. Want me to walk you through a 2-minute setup? Or we can skip it and jump straight to building."*

If they say yes → read `setup.md` and guide them through it.
If they say no/skip → proceed normally. Never block building.

**If tools are present** → say nothing, proceed to Phase 1.

---

## Phase 1: Discovery

Discovery has two parts: **Project Detection** (automatic, silent) and **Gap-Filling** (conversational, only when needed).

### Step 0: Memory Check (always run first, silent)

Check for `.frontend-magic-memory.md` in the project's working directory.

**If it exists**: Read it. This project has been built with the skill before. Use stored preferences to inform your plan — don't re-learn what you already know.
- If memory has brand/identity notes → you already know the audience and voice
- If memory has revision patterns ("always asks for bolder CTAs") → get it right the first time
- If memory has approved directions → you know what "good" looks like for this project

**If it doesn't exist**: First build in this project. Create the file from the template after the build ships (see Memory Update section). Proceed normally.

### Step 1: Project Detection (always run first, never ask)

Before asking the user anything, check what the project tells you. **Read `component-libraries.md`** for detailed detection rules and integration guides.

Quick detection overview:
- Check for `next.config.*`, `nuxt.config.*`, `svelte.config.*`, `vite.config.*`, `package.json` → framework
- Check for `components.json`, `@chakra-ui/react`, `@mantine/core`, `@ark-ui/react` in deps → component library
- Check for CSS variables, Tailwind theme config, font imports, shadcn presets → existing design system
- No `package.json` → standalone HTML file (default)

**What to do with results:**
- Framework + library found → state it in one line, move on. *"Next.js with shadcn — I'll work with that."*
- Framework but no library → include library question in gap-filling. If they pick shadcn, also set up MCP server + skills package (see `component-libraries.md` for commands).
- No project but user wants a framework → offer scaffolding options (standalone HTML, Next.js + shadcn, Vite + React). See **Scaffolding Path** in `component-libraries.md` for the full sequence including MCP/CLI setup.
- No project, simple request → default to standalone HTML. Don't force a framework conversation.

### Step 2: Gap-Filling (only for what you can't detect or infer)

Checklist — what do you still need?

- [ ] **What it is**: Landing page, dashboard, component, full app?
- [ ] **Who it's for**: Developers, consumers, local businesses, internal team?
- [ ] **What it does**: Key sections/features?
- [ ] **How it should feel**: Brand/tone signals for aesthetic direction?
- [ ] **Visual references**: Did they share screenshots, URLs, or describe pages they like?
- [ ] **Framework**: Detected, stated, or defaulting to standalone HTML?
- [ ] **Component library**: Detected, stated, or needs asking?

**6-7 checked** → skip to Design Plan.
**1-5 checked** → ONE message, 3-5 focused questions.

**How to ask well:**
- Lead with what you detected: *"Next.js with Tailwind, no component library. Landing page for HVAC — got it. A few things:"*
- Specific questions, not open-ended. Propose answers with each question.
- **Always ask about visual references** — this is how real designers work. Frame it casually:
  > *"Got any pages you like the look of? Screenshots, URLs, anything. Tell me what specifically catches your eye — the layout? Colors? Animations? Typography? Even 'I like how Stripe's site feels' gives me a lot to work with."*
- If they provide references: read screenshots (Claude can view images), visit URLs if accessible, and extract what they like — don't just copy the reference, use it to understand their taste and inform the Design Plan.
- If they say "no" or skip: that's fine, you'll propose a direction in the Design Plan and they can react to it.
- Ask about component library only if framework exists but no library detected. See `component-libraries.md` for the recommendation template.
- If the user says "just build it" → stop asking, go. Best judgment for gaps.

### Discovery Anti-Rationalization

| Excuse | Reality |
|--------|---------|
| "I should ask to be thorough" | If the prompt is detailed and the project is detected, asking is stalling. Build. |
| "I have enough to work with" | If you don't know the audience or purpose, you're guessing. One message of questions now saves a full rebuild later. |
| "I'll ask about everything to be safe" | 3-5 questions. Not a form. You're a designer having a conversation, not a bureaucrat collecting tickets. |
| "The user will tell me if it's wrong" | They shouldn't have to. Catch the mismatch before 500 lines of code. |
| "I should ask what framework they want" | Check `package.json` first. No project? Default to standalone HTML. |
| "I should ask about their component library" | Check deps first. If `components.json` is right there, asking is insulting. |
| "I'll just use shadcn since it's popular" | If Mantine is installed and you add shadcn, you've created a mess. Detect first. |
