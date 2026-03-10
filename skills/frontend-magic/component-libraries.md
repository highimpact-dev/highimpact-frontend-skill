# Component Library Detection & Integration

Reference file for the frontend-magic skill. Read this during the Discovery phase.

---

## Framework Detection

Check for these files/patterns to identify the framework:

| Signal | Framework |
|--------|-----------|
| `next.config.*` or `app/layout.tsx` | Next.js |
| `nuxt.config.*` or `.nuxt/` | Nuxt (Vue) |
| `svelte.config.*` | SvelteKit |
| `astro.config.*` | Astro |
| `remix.config.*` or `app/root.tsx` with Remix imports | Remix |
| `vite.config.*` + `react` in deps | Vite + React |
| `vite.config.*` + `vue` in deps | Vite + Vue |
| `vite.config.*` + `svelte` in deps | Vite + Svelte |
| `package.json` with `react`/`react-dom` only | Plain React (CRA or custom) |
| `package.json` with `vue` only | Plain Vue |
| No `package.json` | Standalone HTML/CSS/JS |

## Component Library Detection

Check `package.json` dependencies and project files:

| Signal | Library |
|--------|---------|
| `components.json` in project root | **shadcn/ui** |
| `@shadcn/ui` in deps | **shadcn/ui** |
| `@chakra-ui/react` in deps | **Chakra UI** |
| `@mantine/core` in deps | **Mantine** |
| `@ark-ui/react` (or `/vue`, `/solid`) in deps | **Ark UI** |
| `tailwindcss` in deps, no component library | **Tailwind-only** |
| None of the above | Vanilla CSS or no project |

## Design System Detection

| Signal | What it tells you |
|--------|-------------------|
| CSS variables file (e.g., `globals.css` with `--primary:`) | Existing color/spacing tokens — use them |
| `tailwind.config.*` with custom `theme.extend` | Established design system — extend, don't override |
| shadcn preset string | Full design system (colors, theme, icons, fonts, radius) |
| Global CSS with `@import url('fonts.googleapis.com/...')` | Existing typography choices — match or ask before changing |
| `theme.ts` or `theme.js` | Centralized theme — work within it |

---

## No Framework Detected — Scaffolding Path

When Discovery finds no `package.json` and the user wants more than a standalone HTML file, offer to scaffold a project. Present options based on what they're building:

> *"No project set up here. I can either:*
> 1. ***Build a standalone HTML file** — single file, zero setup, works right away. Best for landing pages and one-off pages.*
> 2. ***Scaffold a Next.js + shadcn/ui project** — full React framework with the best component library and agent tooling. Best for apps, dashboards, multi-page sites.*
> 3. ***Scaffold a Vite + React project** — lighter than Next.js, no SSR, still gets shadcn. Good for SPAs and tools.*
> 4. ***Something else** — tell me what you want and I'll set it up."*

If user says "just build it" → default to standalone HTML.
If user picks a framework → run the scaffolding sequence below.

### Next.js + shadcn/ui Scaffolding Sequence

This is the recommended path. Run these in order:

```bash
# 1. Create Next.js project
pnpm dlx create-next-app@latest [project-name] --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"

# 2. Initialize shadcn/ui
cd [project-name]
pnpm dlx shadcn@latest init

# (If user has a preset: pnpm dlx shadcn@latest init --preset [code])
# (To choose base library: --base radix or --base base-ui)
```

After scaffolding, set up agent tooling:

```bash
# 3. shadcn MCP server (component registry access — browse, search, install)
pnpm dlx shadcn@latest mcp init --client claude

# 4. shadcn skills package (injects project config into agent context)
pnpm dlx skills add shadcn/ui

# 5. Next.js DevTools MCP (runtime diagnostics, docs search, error analysis)
claude mcp add next-devtools -- npx next-devtools-mcp@latest

# 6. Vercel MCP (deployment, docs — optional but recommended)
claude mcp add --transport http vercel https://mcp.vercel.com

# 7. Figma MCP (design-to-code — optional, only if user works with Figma)
claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp
```

**What each MCP provides:**

| MCP Server | What it does |
|------------|-------------|
| **shadcn** | Browse component registry, search components, install via natural language, view docs/examples |
| **shadcn skills** | Auto-injects project config (framework, Tailwind version, aliases, installed components, paths) into every agent interaction |
| **next-devtools** | Search Next.js docs, diagnose build/runtime/type errors, route metadata, automated upgrades |
| **vercel** | Search Vercel docs, manage deployments, analyze deploy logs |
| **figma** | Read Figma designs, extract design tokens/variables, convert frames to code context |

### ⚠️ CRITICAL: MCP Session Restart Requirement

**MCP servers installed via `claude mcp add` are NOT available in the current session.** They require a clean session restart to connect.

When you install MCP servers during scaffolding, you MUST tell the user:

> *"I've set up the project and configured the following agent tooling:*
> - *shadcn MCP — I'll be able to browse and install components directly*
> - *shadcn skills — I'll automatically know your project's config*
> - *Next.js DevTools — I'll be able to diagnose build errors and search docs*
>
> *⚠️ **These MCP servers won't be active until you start a new session.** For this session, I'll work without them — I can still build everything, I just won't have the component registry or diagnostics tooling available.*
>
> *Want me to continue building now, or start a fresh session first so I have full tooling?"*

**If user continues in current session:**
- Use `shadcn add [component]` CLI directly instead of the MCP server
- Reference shadcn docs from `llms.txt` instead of MCP browsing
- Use `pnpm dev` output for error diagnostics instead of Next.js DevTools MCP
- Everything still works, just with CLI instead of MCP tools

**If user starts a fresh session:**
- All MCP servers will be connected
- Run `/mcp` to verify they're active
- Full agent tooling available from the start

### Browser DevTools for Live Testing

For the Live Testing phase, check what browser tools are available:

**Claude-in-Chrome** (Chrome DevTools MCP — if installed):
- Real browser with full DevTools access
- Navigate to pages, read rendered content, take screenshots
- Read console messages (filter by pattern), read network requests
- Execute JavaScript in page context
- Best for: interactive testing, checking real rendering, debugging visual issues
- Tools: `mcp__claude-in-chrome__navigate`, `mcp__claude-in-chrome__read_page`, `mcp__claude-in-chrome__computer` (screenshots), `mcp__claude-in-chrome__read_console_messages`, `mcp__claude-in-chrome__read_network_requests`, `mcp__claude-in-chrome__javascript_tool`

**Playwright** (via Playwright skill — if installed):
- Headless browser automation
- Scripted screenshot capture at specific viewports
- Best for: automated multi-viewport testing, CI-style checks
- Trigger: `/playwright-skill`

**Neither available:**
- Fall back to manual verification: serve the file, tell user to open in browser, ask them to share screenshots or feedback
- Use code-level checks: validate HTML structure, check CSS for mobile breakpoints, verify font imports exist

**Present browser tooling check to user during scaffolding or first live test:**
> *"For live testing, I can render your page and take screenshots to verify it looks right. Which browser tools do you have?*
> 1. ***Chrome DevTools** (claude-in-chrome) — I'll open the page in Chrome and screenshot at different sizes*
> 2. ***Playwright** — I'll run automated headless tests*
> 3. ***Neither** — I'll serve the file and you check it in your browser, then tell me what to fix*
>
> *If you want to add either: `claude-in-chrome` is a Chrome extension + MCP, Playwright is `npx @anthropic-ai/playwright-mcp`."*

### Vite + React + shadcn Scaffolding Sequence

Lighter alternative when SSR isn't needed:

```bash
# 1. Create Vite project
pnpm create vite [project-name] --template react-ts
cd [project-name]
pnpm install

# 2. Add Tailwind CSS
pnpm add -D tailwindcss @tailwindcss/vite

# 3. Initialize shadcn
pnpm dlx shadcn@latest init

# 4. Agent tooling (same as Next.js)
pnpm dlx shadcn@latest mcp init --client claude
pnpm dlx skills add shadcn/ui
```

### Post-Scaffolding Checklist

After any scaffolding, verify before continuing to Design Plan:
- [ ] `pnpm dev` starts without errors
- [ ] `components.json` exists (shadcn initialized)
- [ ] MCP servers respond (run `/mcp` to check)
- [ ] Project structure matches expected layout

---

## Library Recommendation Template

Use this when the project has a framework but no component library detected:

> *"You've got [framework] with Tailwind but no component library set up. Want one? The top options right now:*
> - ***shadcn/ui** (my pick) — Tailwind + Radix primitives, you own the code, and I can use its MCP server to browse/install components directly*
> - ***Chakra UI** — props-driven, fast to prototype with, has MCP server for component lookup*
> - ***Mantine** — 100+ batteries-included components, good docs*
> - ***Ark UI** — headless primitives, works across React/Vue/Solid/Svelte*
> - ***Just Tailwind** — no library overhead, full control*
>
> *Or skip this — I'll go with just Tailwind and custom components."*

If user picks shadcn → also set up the MCP server and skills package:
```bash
pnpm dlx shadcn@latest init
pnpm dlx shadcn@latest mcp init --client claude
pnpm dlx skills add shadcn/ui
```

---

## Library Integration Guides

### shadcn/ui (best agent support as of March 2026)

**Agent tooling available:**
- **MCP server**: `pnpm dlx shadcn@latest mcp init --client claude` — browse components, search registries, install via natural language
- **Skills package**: `pnpm dlx skills add shadcn/ui` — injects project config (framework, Tailwind version, aliases, base library, icon library, installed components, resolved paths) into agent context on every interaction
- **CLI introspection**: `shadcn info --json` — dump full project config
- **CLI docs**: `shadcn docs [component]` — get docs/code/examples from CLI
- **Presets**: Single string encoding full design system. `shadcn init --preset [code]`
- **llms.txt**: `ui.shadcn.com/llms.txt` — AI-optimized docs with actual source code
- **CLI flags**: `--dry-run` (inspect before writing), `--diff` (check for updates), `--view` (inspect registry items)

**How to use during build:**
1. Run `shadcn info --json` first to understand the project's config
2. Check what components are already installed — don't reinstall
3. Use MCP server to browse available components when you need something
4. If a preset exists, honor its design system choices
5. Install new components via CLI (`shadcn add button`), don't copy-paste from docs
6. Use `shadcn docs [component]` to check component API before using it

### Chakra UI

**Agent tooling:**
- **MCP server**: `claude mcp add chakra-ui -- npx -y @chakra-ui/react-mcp`
  - Tools: `list_components`, `get_component_props`, `get_component_example`, `list_component_templates`, `get_component_templates`
  - Pro templates require Chakra UI Pro license + `CHAKRA_PRO_API_KEY`
- **AI rules**: Pre-built rules at `chakra-ui.com/docs/get-started/ai/rules` — can be dropped into any AI config
- **llms.txt**: `chakra-ui.com/llms.txt` and `llms-full.txt`, plus `llms-v3-migration.txt` for migration

**How to use during build:**
1. Use MCP server to look up component props and examples
2. Follow Chakra's token-based styling system (don't mix raw CSS)
3. Use their theme extension pattern for custom colors/fonts

### Mantine

**Agent tooling:**
- **llms.txt**: `mantine.dev/llms.txt` (added in v8.3)
- **Community MCP server**: `github.com/hakxel/mantine-ui-server`
  - Tools: `get_component_docs`, `search_components`, `list_components`, `generate_component`, `create_theme_config`, `create_component_theme`

**How to use during build:**
1. Reference llms.txt for component API docs
2. Use Mantine's `createTheme()` for consistent theming
3. Mantine is batteries-included — check if a component exists before building custom

### Ark UI

**Agent tooling:**
- **MCP server**: Available at `ark-ui.com/docs/ai/mcp-server`
  - Tools: `list_components`, `list_examples`, `get_example`, `styling_guide`
- **llms.txt**: Framework-specific variants at `ark-ui.com/docs/ai/llms.txt`
  - `llms-react.txt`, `llms-vue.txt`, `llms-solid.txt` for framework-specific docs

**How to use during build:**
1. Ark is headless — all styling is yours. Great for custom design systems.
2. Use the MCP server's `styling_guide` tool for recommended patterns
3. Multi-framework: works across React, Vue, Solid, Svelte

### No Library / Vanilla

**When to use:**
- Standalone HTML files (the default when no project exists)
- Marketing/landing pages where bundle size matters
- When the user wants full control with no abstractions
- Single-file deliverables

**How to build:**
- Tailwind utility classes if available, custom CSS if not
- CSS variables for design tokens
- No component library overhead
- Full creative freedom — this is where the wildest designs live
