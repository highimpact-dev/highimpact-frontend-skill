# Frontend Design Skill — First-Run Setup

Triggered by `--setup` flag, or automatically on first use when required tools are missing.

## Presentation Rules

1. **No jargon.** Don't say "MCP server" — say "a tool that lets me browse components" or "a plugin that gives me access to..."
2. **Copy-paste commands.** Every install step is one command they can copy.
3. **One thing at a time.** Don't dump 7 install commands. Walk through them.
4. **Explain what each tool does for THEM**, not what it does technically.
5. **Be encouraging.** This takes 2 minutes and makes everything better.

---

## Step 1: Detection

Before presenting anything, silently check what's available:

**Check for browser tools:**
- Try calling `mcp__claude-in-chrome__tabs_context_mcp` — if it responds, Chrome DevTools is available
- Check if Playwright skill is available (it's in the skill list)

**Check for component tools:**
- Try running `shadcn info --json` — if it responds, shadcn CLI is installed
- Check for `components.json` in project root — shadcn is initialized
- Check if shadcn MCP tools are available (try listing tools with "shadcn" in name)

**Check for dev tools:**
- Check if Next.js DevTools MCP responds
- Check if Vercel MCP responds
- Check if Figma MCP responds

---

## Step 2: Present Results

Based on detection, present ONE of these messages:

### If everything is set up:
> *"You're all set! I can see you have browser tools, component tools, and everything I need. Let's build something."*

Skip to the normal workflow.

### If some things are missing:

Present the setup guide below.

---

## Step 3: Setup Guide

### Opening

*"Before we start building, let me check what tools I have access to. These make a huge difference in what I can do for you — the difference between guessing and actually seeing your project.*

*Here's what I found:"*

### Present what's installed vs missing

Use a simple checklist format:

*"**What I have:**"*
- ✅ [list what's detected — e.g., "I can browse your project files", "Playwright for testing"]

*"**What I'm missing:**"*
- ❌ [list what's missing with plain-language descriptions]

---

### Must-Have Tools

Present these first. Frame them as "these make me dramatically better":

#### shadcn Component Browser
**What it does for you:** *"I'll be able to browse a library of pre-built UI components (buttons, forms, cards, dialogs — hundreds of them) and add them directly to your project. Without this, I have to build everything from scratch."*

**Install:**
*"Open a new terminal tab and run:"*
```
npx shadcn@latest mcp init --client claude
```
*"This only takes a few seconds."*

#### Chrome Browser Access
**What it does for you:** *"I'll be able to open your page in a real browser, take screenshots at phone/tablet/desktop sizes, and catch visual bugs before you even see the page. Without this, I'm shipping code I've never actually looked at."*

**Install:**
*"This one has two parts:*

*1. Install the Chrome extension — search for 'Claude in Chrome' in the Chrome Web Store and click Add to Chrome*

*2. Then in a new terminal tab, run:"*
```
claude mcp add claude-in-chrome -- npx @anthropic-ai/claude-in-chrome-mcp
```

---

### Recommended Tools

Present these as optional but valuable:

#### Project Intelligence (shadcn skills)
**What it does for you:** *"I'll automatically know your project's setup — what framework you're using, what components you already have, your color theme, everything. Without this, I have to read through your files to figure it out each time."*

**Install:**
```
npx skills add shadcn/ui
```

#### Next.js Helper (only if using Next.js)
**What it does for you:** *"I'll be able to search Next.js documentation instantly and diagnose build errors automatically. Saves a lot of back-and-forth when something breaks."*

**Install:**
```
claude mcp add next-devtools -- npx next-devtools-mcp@latest
```

#### Deployment Tools (Vercel)
**What it does for you:** *"I'll be able to check your deployments, read build logs, and help debug deploy failures."*

**Install:**
```
claude mcp add --transport http vercel https://mcp.vercel.com
```
*"After installing, you'll see a browser window pop up asking you to log in to Vercel. That's normal — just authorize it."*

#### Design Import (Figma)
**What it does for you:** *"If you design in Figma, I'll be able to read your designs directly and match them in code — colors, spacing, typography, everything."*

**Install:**
```
claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp
```

---

## Step 4: Restart Instructions

After they've selected what to install:

*"Great choices. Here's what to do:*

**1.** *Open a new terminal tab (keep this one open)*
**2.** *Run each install command above, one at a time — they're fast*
**3.** *Come back here and start a **new conversation** (type `/clear` or close and reopen Claude Code)*
**4.** *When you're back, just tell me what you want to build — I'll have full access to everything you just installed*

*The installs are one-time — you won't need to do this again.*

*Want me to list all your install commands together so you can copy them all at once?"*

### If they say yes, compile their chosen commands:

*"Here you go — run these in your terminal:"*
```bash
# Component browser (must-have)
npx shadcn@latest mcp init --client claude

# Project intelligence (recommended)
npx skills add shadcn/ui

# [include only what they selected]
```

*"See you in the new session! Just say what you want to build and I'll take it from there."*

---

## Step 5: Re-Detection on Return

When the user comes back in a new session, the skill should silently re-detect and confirm:

*"Welcome back! Quick check... ✅ Component browser is connected. ✅ Browser tools are ready. ✅ Project intelligence is active. We're good to go — what are we building?"*

If something is still missing:
*"Almost there — I can see [X] but [Y] didn't connect. Want to try installing it again, or skip it for now?"*

---

## Handling Users Who Don't Want to Install Anything

Some users will say "I don't want to install anything" or "can we just build?" That's fine.

*"No problem at all! I can build without these tools — I just won't be able to browse components or preview the design in a browser. I'll build everything from scratch and you can check it in your browser when I'm done. Let's go — what are we making?"*

Never block the user from building. Setup is recommended, not required.

---

## Handling Confusion

If the user seems confused about terminal, commands, or the process:

*"No worries — here's the simple version:*

*1. Open the Terminal app on your computer (it's in Applications → Utilities on Mac, or search for 'Terminal')*
*2. Copy this text exactly:* `[command]`
*3. Paste it in the terminal and press Enter*
*4. Wait for it to finish (usually 5-10 seconds)*
*5. Come back here and say 'done'*

*That's it! I'll walk you through each one."*
