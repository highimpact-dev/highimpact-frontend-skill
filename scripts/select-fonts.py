#!/usr/bin/env python3
"""Font selector for the frontend-design skill.

Takes a mood profile (derived from the conceptual anchor) and returns
font recommendations from Google Fonts' tagged dataset.

Usage:
    python3 select-fonts.py '{"Calm": 80, "Business": 60, "Sincere": 70, "Vintage": 20}'

    # With category preference:
    python3 select-fonts.py '{"Futuristic": 90, "Competent": 70}' --display sans-serif --body serif

    # With exclusions:
    python3 select-fonts.py '{"Calm": 80}' --exclude "Inter,Roboto,Open Sans"

The mood profile keys match Google Fonts' Expressive tags:
    Active, Artistic, Awkward, Business, Calm, Childlike, Competent,
    Cute, Excited, Fancy, Futuristic, Happy, Innovative, Loud, Playful,
    Rugged, Sincere, Sophisticated, Stiff, Vintage

Each value is 0-100 (how strongly this mood applies to the project).
"""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATA_PATH = SCRIPT_DIR / "font-data.json"

# Fonts that are overused defaults — always excluded
BANNED = {
    "Inter", "Roboto", "Open Sans", "Poppins", "Montserrat", "Lato",
    "Nunito", "Nunito Sans", "DM Sans", "Raleway", "Source Sans 3",
    "Work Sans", "Rubik", "Manrope", "Plus Jakarta Sans",
}


def load_fonts():
    with open(DATA_PATH) as f:
        return json.load(f)


def score_font(font_moods: dict, target_moods: dict, popularity: float = 0) -> float:
    """Score a font against the target mood profile.

    Uses cosine-like similarity: high scores on moods we want,
    low scores on moods we don't. Popularity acts as a credibility
    bonus — fonts the agent recognizes get trusted, used, not overridden.
    """
    score = 0
    total_weight = 0

    for mood, target in target_moods.items():
        actual = font_moods.get(mood, 0)
        weight = target / 100  # higher-priority moods weigh more

        # Reward alignment, penalize divergence
        score += weight * (100 - abs(actual - target))
        total_weight += weight

    # Penalize fonts that are very high on moods we DIDN'T ask for
    # (prevents "loud" fonts sneaking in when we want "calm")
    unwanted_penalty = 0
    for mood, actual in font_moods.items():
        if mood not in target_moods and actual > 70:
            unwanted_penalty += (actual - 70) * 0.3

    if total_weight == 0:
        return 0

    mood_score = (score / total_weight) - unwanted_penalty

    # Popularity bonus: recognized fonts get used, obscure ones get overridden.
    # Scale: 0-25 points. A top-100 font (~95+ percentile) gets ~24.
    # A rank-1500 font (~20 percentile) gets ~5. Strong enough to
    # prevent pixel-art fonts from beating well-known geometric sans.
    pop_bonus = popularity * 0.25

    return mood_score + pop_bonus


def is_readable_body(font_moods: dict) -> bool:
    """Filter out novelty/gimmick fonts that shouldn't be used for body text.

    Fonts that score very high on Loud, Awkward, Excited, or Childlike
    are display-only — they're not readable at 16px body sizes.
    """
    loud = font_moods.get("Loud", 0)
    awkward = font_moods.get("Awkward", 0)
    excited = font_moods.get("Excited", 0)
    childlike = font_moods.get("Childlike", 0)

    rugged = font_moods.get("Rugged", 0)
    stiff = font_moods.get("Stiff", 0)
    business = font_moods.get("Business", 0)

    # If any novelty dimension is very high, it's not body material
    if max(loud, awkward, excited, childlike) > 70:
        return False
    # If the sum of novelty dimensions is high, also skip
    if (loud + awkward + excited + childlike) > 180:
        return False
    # Display-masquerading-as-sans: high visual intensity + low business = not body text
    if (loud + rugged + stiff) > 180 and business < 20:
        return False
    return True


def select_fonts(
    target_moods: dict,
    display_cat: str | None = None,
    body_cat: str | None = None,
    exclude: set[str] | None = None,
    n: int = 5,
) -> dict:
    """Return font recommendations grouped by role (display vs body)."""
    fonts = load_fonts()
    exclude = (exclude or set()) | BANNED

    scored = []
    for name, data in fonts.items():
        if name in exclude:
            continue
        s = score_font(data["e"], target_moods, data.get("p", 0))
        scored.append((name, s, data))

    scored.sort(key=lambda x: -x[1])

    # Display fonts: personality matters — serif, display, slab bring character
    # Body fonts: readability matters — sans-serif and serif only, no novelty
    display_candidates = []
    body_candidates = []

    for name, s, data in scored:
        cat = data["c"]
        moods = data["e"]

        # Display candidates: everything except monospace
        if cat != "monospace":
            if display_cat is None or cat == display_cat:
                bonus = 0
                # Mild boost for categories with visual personality —
                # enough to break ties, not enough to override popularity
                if cat in ("serif", "slab"):
                    bonus = 6
                elif cat == "display":
                    bonus = 5
                elif cat == "script":
                    bonus = 4
                # Sans-serif gets no bonus — earns its spot on mood + popularity
                display_candidates.append({
                    "name": name, "score": round(s + bonus, 1),
                    "category": cat, "popularity": data.get("p", 0),
                    "moods": moods, "structural": data["s"]
                })

        # Body candidates: only readable categories, filtered for novelty
        if cat in ("sans-serif", "serif", "slab"):
            if (body_cat is None or cat == body_cat) and is_readable_body(moods):
                bonus = 5 if cat == "sans-serif" else 3  # slight readability edge
                body_candidates.append({
                    "name": name, "score": round(s + bonus, 1),
                    "category": cat, "popularity": data.get("p", 0),
                    "moods": moods, "structural": data["s"]
                })

    display_candidates.sort(key=lambda x: -x["score"])
    body_candidates.sort(key=lambda x: -x["score"])

    top_display = display_candidates[:n * 2]  # wider pool for pairing
    top_body = body_candidates[:n * 2]

    # Generate pairings — prefer category contrast, allow structural contrast
    pairings = []

    for d in top_display:
        # Skip obscure fonts from pairings — the agent won't trust them
        if d.get("popularity", 0) < 40:
            continue
        for b in top_body:
            if d["name"] == b["name"]:
                continue
            if b.get("popularity", 0) < 40:
                continue

            # Category contrast (serif + sans, display + sans, etc.)
            if d["category"] != b["category"]:
                pairings.append({
                    "display": d["name"],
                    "body": b["name"],
                    "contrast": f"{d['category']} + {b['category']}",
                    "combined_score": round(d["score"] + b["score"], 1)
                })
            # Same category but different structural subcategory
            # (e.g., /Sans/Geometric display + /Sans/Humanist body)
            elif d["structural"] != b["structural"]:
                pairings.append({
                    "display": d["name"],
                    "body": b["name"],
                    "contrast": f"{d['structural'][0] if d['structural'] else d['category']} + {b['structural'][0] if b['structural'] else b['category']}",
                    "combined_score": round(d["score"] + b["score"], 1)
                })
            if len(pairings) >= 30:
                break
        if len(pairings) >= 30:
            break

    # Sort by combined score, take top 3
    pairings.sort(key=lambda x: -x["combined_score"])
    # Deduplicate: no repeated fonts, no mirror pairings (A+B and B+A)
    seen_d, seen_b = set(), set()
    seen_pairs = set()
    unique_pairings = []
    for p in pairings:
        pair_key = frozenset([p["display"], p["body"]])
        if p["display"] not in seen_d and p["body"] not in seen_b and pair_key not in seen_pairs:
            unique_pairings.append(p)
            seen_d.add(p["display"])
            seen_b.add(p["body"])
            seen_pairs.add(pair_key)
        if len(unique_pairings) >= 3:
            break

    return {
        "mood_profile": target_moods,
        "recommended_pairings": unique_pairings,
        "display_candidates": [{k: v for k, v in f.items() if k != "moods"} for f in top_display[:n]],
        "body_candidates": [{k: v for k, v in f.items() if k != "moods"} for f in top_body[:n]],
    }


def format_output(result: dict) -> str:
    """Format results as readable text for the agent."""
    lines = ["## Font Recommendations", ""]
    lines.append(f"**Mood profile:** {result['mood_profile']}")
    lines.append("")

    if result["recommended_pairings"]:
        lines.append("### Recommended Pairings")
        for i, p in enumerate(result["recommended_pairings"], 1):
            lines.append(f"{i}. **{p['display']}** (display) + **{p['body']}** (body) — {p['contrast']}")
        lines.append("")

    lines.append("### Display Font Candidates")
    for f in result["display_candidates"]:
        lines.append(f"- **{f['name']}** ({f['category']}) — score: {f['score']}")
    lines.append("")

    lines.append("### Body Font Candidates")
    for f in result["body_candidates"]:
        lines.append(f"- **{f['name']}** ({f['category']}) — score: {f['score']}")

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = json.loads(sys.argv[1])

    display_cat = None
    body_cat = None
    exclude = set()

    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--display" and i + 1 < len(args):
            display_cat = args[i + 1]
            i += 2
        elif args[i] == "--body" and i + 1 < len(args):
            body_cat = args[i + 1]
            i += 2
        elif args[i] == "--exclude" and i + 1 < len(args):
            exclude = {s.strip() for s in args[i + 1].split(",")}
            i += 2
        elif args[i] == "--json":
            i += 1
        else:
            i += 1

    result = select_fonts(target, display_cat, body_cat, exclude)

    if "--json" in sys.argv:
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))
