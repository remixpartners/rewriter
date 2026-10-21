#!/usr/bin/env python3
"""Final check for a rewrite: lists what the Editor must fix or justify.

Measurements only; the judgment stays with the Editor. Run it on the final text,
after the Voice stage, with the raw input as --source:

    python3 scripts/final_check.py out.md --source input.md

Reports, one line per hit:
  DASH      em dashes, en dashes, and double hyphens (a line that is exactly "--",
            which opens an email signature block, is not counted)
  CURSED    the Scrub's cursed vocabulary, read from SKILL.md so the list lives once
  CONTRAST  "not X, it's Y" style negative parallelisms
  NUMBER    numbers in the output that never appear in the source (needs --source)

Then a summary line: "final_check: CLEAN" or "final_check: N hits". Exit 0 when
clean, 1 when there are hits, 2 on a usage error. Standard library only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"

CONTRAST = [
    r"\bnot (?:just|only|merely|simply)\b",
    r"\b(?:is|are|was|were|'s|'re) not\b[^.!?\n]{1,80}?[,;:]\s*(?:it|this|that|they|we)(?:'s|'re| is| are| was| were)\b",
    r"\b(?:isn't|aren't|wasn't)\b[^.!?\n]{1,80}?[,;:]\s*(?:it|this|that|they)(?:'s| is| are|'re)\b",
    r"\bnot\b[^.!?\n]{1,60}?,\s*but\b",
    # fragments: "Not a new policy." and "a sequencing decision, not a build."
    r"(?:^|[.!?:]\s+)not (?:a|an|the|just)\b",
    r",\s*not (?:a|an|the)\b",
    # the two-sentence form: "These are not pilots. This is the work."
    r"\b(?:is|are|was|were) not\b[^.!?\n]{1,80}?\.\s+(?:this|it|that|they)(?:'s|'re| is| are)\b",
]


def cursed_words() -> list[str]:
    m = re.search(r"Cursed vocabulary\. The words (.+?)\. Replace", SKILL_MD.read_text())
    if not m:
        sys.exit("final_check: cannot find the cursed-vocabulary line in SKILL.md")
    return [w.strip() for w in re.split(r",\s*(?:and\s+)?|\s+and\s+", m.group(1)) if w.strip()]


def numbers(text: str) -> set[str]:
    return {re.sub(r"[,$%]", "", n) for n in re.findall(r"\$?\d[\d,]*(?:\.\d+)?%?", text)
            if re.sub(r"[,$%.]", "", n)}


def check(text: str, source: str | None) -> list[tuple[str, int, str]]:
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip() == "--":
            continue
        for m in re.finditer(r"—|–|(?<!-)--(?!-)", line):
            hits.append(("DASH", i, line[max(0, m.start() - 30):m.end() + 30]))
        low = line.lower()
        for w in cursed_words():
            for m in re.finditer(rf"\b{re.escape(w.lower())}\w*", low):
                hits.append(("CURSED", i, line[max(0, m.start() - 20):m.end() + 20]))
        for pat in CONTRAST:
            for m in re.finditer(pat, low):
                hits.append(("CONTRAST", i, line[m.start():m.end() + 20]))
    if source is not None:
        known = numbers(source)
        for i, line in enumerate(text.splitlines(), 1):
            for n in sorted(numbers(line) - known):
                hits.append(("NUMBER", i, f"{n} (not in the source)"))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("output", help="the final rewrite")
    ap.add_argument("--source", action="append", default=[], help="raw input file (repeatable)")
    args = ap.parse_args()
    try:
        text = Path(args.output).read_text()
        source = "\n".join(Path(s).read_text() for s in args.source) if args.source else None
    except OSError as e:
        print(f"final_check: {e}", file=sys.stderr)
        return 2
    hits = check(text, source)
    for kind, line, excerpt in hits:
        print(f"{kind} line {line}: {excerpt.strip()}")
    print("final_check: CLEAN" if not hits else f"final_check: {len(hits)} hits"
          + ("" if source is not None else " (no --source given, so numbers were not checked)"))
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
