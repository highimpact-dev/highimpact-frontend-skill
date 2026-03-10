#!/usr/bin/env node
/**
 * Font selector for the frontend-design skill.
 *
 * Takes a mood profile (derived from the conceptual anchor) and returns
 * font recommendations from Google Fonts' tagged dataset.
 *
 * Usage:
 *   node select-fonts.mjs '{"Calm": 80, "Business": 60, "Sincere": 70}'
 *
 *   # With category preference:
 *   node select-fonts.mjs '{"Futuristic": 90, "Competent": 70}' --display sans-serif --body serif
 *
 *   # With exclusions:
 *   node select-fonts.mjs '{"Calm": 80}' --exclude "Inter,Roboto,Open Sans"
 *
 * The mood profile keys match Google Fonts' Expressive tags:
 *   Active, Artistic, Awkward, Business, Calm, Childlike, Competent,
 *   Cute, Excited, Fancy, Futuristic, Happy, Innovative, Loud, Playful,
 *   Rugged, Sincere, Sophisticated, Stiff, Vintage
 *
 * Each value is 0-100 (how strongly this mood applies to the project).
 */

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const DATA_PATH = join(__dirname, "font-data.json");

// Fonts that are overused defaults — always excluded
const BANNED = new Set([
  "Inter", "Roboto", "Open Sans", "Poppins", "Montserrat", "Lato",
  "Nunito", "Nunito Sans", "DM Sans", "Raleway", "Source Sans 3",
  "Work Sans", "Rubik", "Manrope", "Plus Jakarta Sans",
]);

function loadFonts() {
  return JSON.parse(readFileSync(DATA_PATH, "utf-8"));
}

function scoreFont(fontMoods, targetMoods, popularity = 0) {
  let score = 0;
  let totalWeight = 0;

  for (const [mood, target] of Object.entries(targetMoods)) {
    const actual = fontMoods[mood] ?? 0;
    const weight = target / 100;
    score += weight * (100 - Math.abs(actual - target));
    totalWeight += weight;
  }

  // Penalize fonts high on moods we didn't ask for
  let unwantedPenalty = 0;
  for (const [mood, actual] of Object.entries(fontMoods)) {
    if (!(mood in targetMoods) && actual > 70) {
      unwantedPenalty += (actual - 70) * 0.3;
    }
  }

  if (totalWeight === 0) return 0;

  const moodScore = score / totalWeight - unwantedPenalty;

  // Popularity bonus: recognized fonts get used, obscure ones get overridden.
  // Scale: 0-25 points. Top-100 font (~95+ percentile) gets ~24.
  // Rank-1500 font (~20 percentile) gets ~5.
  const popBonus = popularity * 0.25;

  return moodScore + popBonus;
}

function isReadableBody(fontMoods) {
  const loud = fontMoods.Loud ?? 0;
  const awkward = fontMoods.Awkward ?? 0;
  const excited = fontMoods.Excited ?? 0;
  const childlike = fontMoods.Childlike ?? 0;
  const rugged = fontMoods.Rugged ?? 0;
  const stiff = fontMoods.Stiff ?? 0;
  const business = fontMoods.Business ?? 0;

  if (Math.max(loud, awkward, excited, childlike) > 70) return false;
  if (loud + awkward + excited + childlike > 180) return false;
  if (loud + rugged + stiff > 180 && business < 20) return false;
  return true;
}

function selectFonts(targetMoods, displayCat = null, bodyCat = null, exclude = new Set(), n = 5) {
  const fonts = loadFonts();
  const allExcluded = new Set([...exclude, ...BANNED]);

  const scored = [];
  for (const [name, data] of Object.entries(fonts)) {
    if (allExcluded.has(name)) continue;
    const s = scoreFont(data.e, targetMoods, data.p ?? 0);
    scored.push({ name, score: s, data });
  }
  scored.sort((a, b) => b.score - a.score);

  const displayCandidates = [];
  const bodyCandidates = [];

  for (const { name, score: s, data } of scored) {
    const cat = data.c;
    const moods = data.e;

    // Display candidates: everything except monospace
    if (cat !== "monospace") {
      if (displayCat === null || cat === displayCat) {
        let bonus = 0;
        if (cat === "serif" || cat === "slab") bonus = 6;
        else if (cat === "display") bonus = 5;
        else if (cat === "script") bonus = 4;

        displayCandidates.push({
          name, score: Math.round((s + bonus) * 10) / 10,
          category: cat, popularity: data.p ?? 0,
          moods, structural: data.s,
        });
      }
    }

    // Body candidates: only readable categories, filtered for novelty
    if (["sans-serif", "serif", "slab"].includes(cat)) {
      if ((bodyCat === null || cat === bodyCat) && isReadableBody(moods)) {
        const bonus = cat === "sans-serif" ? 5 : 3;
        bodyCandidates.push({
          name, score: Math.round((s + bonus) * 10) / 10,
          category: cat, popularity: data.p ?? 0,
          moods, structural: data.s,
        });
      }
    }
  }

  displayCandidates.sort((a, b) => b.score - a.score);
  bodyCandidates.sort((a, b) => b.score - a.score);

  const topDisplay = displayCandidates.slice(0, n * 2);
  const topBody = bodyCandidates.slice(0, n * 2);

  // Generate pairings — prefer category contrast, allow structural contrast
  const pairings = [];

  for (const d of topDisplay) {
    if ((d.popularity ?? 0) < 40) continue;
    for (const b of topBody) {
      if (d.name === b.name) continue;
      if ((b.popularity ?? 0) < 40) continue;

      if (d.category !== b.category) {
        pairings.push({
          display: d.name, body: b.name,
          contrast: `${d.category} + ${b.category}`,
          combined_score: Math.round((d.score + b.score) * 10) / 10,
        });
      } else if (JSON.stringify(d.structural) !== JSON.stringify(b.structural)) {
        const dLabel = d.structural?.[0] ?? d.category;
        const bLabel = b.structural?.[0] ?? b.category;
        pairings.push({
          display: d.name, body: b.name,
          contrast: `${dLabel} + ${bLabel}`,
          combined_score: Math.round((d.score + b.score) * 10) / 10,
        });
      }
      if (pairings.length >= 30) break;
    }
    if (pairings.length >= 30) break;
  }

  // Sort by combined score, deduplicate
  pairings.sort((a, b) => b.combined_score - a.combined_score);
  const seenD = new Set(), seenB = new Set(), seenPairs = new Set();
  const uniquePairings = [];
  for (const p of pairings) {
    const pairKey = [p.display, p.body].sort().join("|");
    if (!seenD.has(p.display) && !seenB.has(p.body) && !seenPairs.has(pairKey)) {
      uniquePairings.push(p);
      seenD.add(p.display);
      seenB.add(p.body);
      seenPairs.add(pairKey);
    }
    if (uniquePairings.length >= 3) break;
  }

  const stripMoods = (f) => ({ name: f.name, score: f.score, category: f.category, popularity: f.popularity, structural: f.structural });

  return {
    mood_profile: targetMoods,
    recommended_pairings: uniquePairings,
    display_candidates: topDisplay.slice(0, n).map(stripMoods),
    body_candidates: topBody.slice(0, n).map(stripMoods),
  };
}

function formatOutput(result) {
  const lines = ["## Font Recommendations", ""];
  lines.push(`**Mood profile:** ${JSON.stringify(result.mood_profile)}`);
  lines.push("");

  if (result.recommended_pairings.length > 0) {
    lines.push("### Recommended Pairings");
    result.recommended_pairings.forEach((p, i) => {
      lines.push(`${i + 1}. **${p.display}** (display) + **${p.body}** (body) — ${p.contrast}`);
    });
    lines.push("");
  }

  lines.push("### Display Font Candidates");
  for (const f of result.display_candidates) {
    lines.push(`- **${f.name}** (${f.category}) — score: ${f.score}`);
  }
  lines.push("");

  lines.push("### Body Font Candidates");
  for (const f of result.body_candidates) {
    lines.push(`- **${f.name}** (${f.category}) — score: ${f.score}`);
  }

  return lines.join("\n");
}

// CLI
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log("Usage: node select-fonts.mjs '{\"Calm\": 80, \"Business\": 60}'");
  console.log("Flags: --display <cat> --body <cat> --exclude \"Font1,Font2\" --json");
  process.exit(1);
}

const target = JSON.parse(args[0]);
let displayCat = null;
let bodyCat = null;
let exclude = new Set();
let jsonOutput = false;

for (let i = 1; i < args.length; i++) {
  if (args[i] === "--display" && args[i + 1]) { displayCat = args[++i]; }
  else if (args[i] === "--body" && args[i + 1]) { bodyCat = args[++i]; }
  else if (args[i] === "--exclude" && args[i + 1]) { exclude = new Set(args[++i].split(",").map(s => s.trim())); }
  else if (args[i] === "--json") { jsonOutput = true; }
}

const result = selectFonts(target, displayCat, bodyCat, exclude);

if (jsonOutput) {
  console.log(JSON.stringify(result, null, 2));
} else {
  console.log(formatOutput(result));
}
