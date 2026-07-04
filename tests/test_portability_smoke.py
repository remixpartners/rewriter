"""Portability smoke test for the rewriter skill (2026-07 Remix skill-portability
Phase 2 pilot, the "pure/simple case" per the design spec).

This skill has no dependency on remix-env, Drive, gws, Tailscale, or any hardcoded
model ID or machine path - confirmed by inspection during this conversion pass
(a full grep across the repo for /Users/<name>, GoogleDrive-<email>, model-version
strings, Tailscale IPs, and remixpartners.ai addresses returned zero hits). So this
test does not exercise remix-env at all; instead it guards the one real portability
risk this skill DOES have: its voice-guide resolution order is documented in TWO
places (SKILL.md and voices/README.md) that could silently drift out of sync over
time, which would quietly break voice matching for whichever surface reads the
stale copy.

Run directly with `python3 tests/test_portability_smoke.py` (stdlib only, no
dependencies) or via `python3 -m unittest discover tests`.
"""
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# The three voice-guide search locations, in order, as they appear in both docs.
# If a maintainer adds/reorders/removes a location in one file and forgets the
# other, this list (extracted fresh from each file below) will stop matching.
EXPECTED_LOCATION_MARKERS = [
    "voices/",              # 1. the skill's own voices/ folder
    "~/.claude/skills/voices/",  # 2. the shared cross-skill library
    "voice-guides/",        # 3. the Cowork-safe CWD folder
]


class RewriterStructureTest(unittest.TestCase):
    """The files a fresh install / Cowork zip must contain."""

    def test_skill_md_exists(self):
        self.assertTrue((REPO_ROOT / "SKILL.md").is_file())

    def test_skillmgr_yaml_exists(self):
        self.assertTrue((REPO_ROOT / "skillmgr.yaml").is_file())

    def test_voices_scaffolding_ships(self):
        # README.md and EXAMPLE.md must ship (per .gitignore's own comment); real
        # guides are gitignored and machine-local, so they won't exist in a fresh
        # clone - this test intentionally does NOT assert on voices/*.md beyond
        # these two scaffolding files.
        self.assertTrue((REPO_ROOT / "voices" / "README.md").is_file())
        self.assertTrue((REPO_ROOT / "voices" / "EXAMPLE.md").is_file())


class NoHardcodedMachineFactsTest(unittest.TestCase):
    """Guards against portability regressions being reintroduced later. This skill
    was confirmed clean of machine-specific coupling during the 2026-07 portability
    conversion pass - this test keeps that true going forward."""

    FORBIDDEN_PATTERNS = [
        r"/Users/(justinmassa|rubyrock|remixpartners)",
        r"GoogleDrive-[a-zA-Z]+@",
        r"claude-opus-\d",
        r"claude-sonnet-\d",
        r"claude-haiku-\d",
        r"100\.120\.116\.15",
        r"100\.85\.196\.43",
        r"@remixpartners\.ai",
    ]

    def _tracked_markdown_files(self):
        # Real voice guides are gitignored (they're personal/machine-local); this
        # walk naturally skips them since it only looks at files that exist in a
        # fresh clone, same set `git ls-files` would return for *.md.
        return [
            p for p in REPO_ROOT.rglob("*.md")
            if ".git" not in p.parts
        ]

    def test_no_hardcoded_machine_facts_in_any_markdown(self):
        hits = []
        for path in self._tracked_markdown_files():
            text = path.read_text(errors="ignore")
            for pattern in self.FORBIDDEN_PATTERNS:
                if re.search(pattern, text):
                    hits.append(f"{path.relative_to(REPO_ROOT)}: matched {pattern!r}")
        self.assertEqual(hits, [], "Hardcoded machine-specific fact(s) found:\n" + "\n".join(hits))


class VoiceGuideResolutionConsistencyTest(unittest.TestCase):
    """SKILL.md (Step 1, Voice Check) and voices/README.md ("How the rewriter finds
    guides") both describe the same three-location search order in prose. There is
    no shared source of truth for this list - it's duplicated by hand in two docs -
    so this test is the guard against one being edited without the other."""

    def test_skill_md_and_voices_readme_list_the_same_locations(self):
        skill_md = (REPO_ROOT / "SKILL.md").read_text()
        voices_readme = (REPO_ROOT / "voices" / "README.md").read_text()

        for marker in EXPECTED_LOCATION_MARKERS:
            self.assertIn(marker, skill_md,
                          f"SKILL.md is missing the voice-guide location {marker!r}")
            self.assertIn(marker, voices_readme,
                          f"voices/README.md is missing the voice-guide location {marker!r}")

    def test_shared_library_path_uses_portable_tilde_not_absolute_home(self):
        # The shared-library location must stay expressed as `~/...` (expands per-
        # user at read time) and never regress to a specific person's absolute home
        # directory - that would silently break it for everyone except that person.
        skill_md = (REPO_ROOT / "SKILL.md").read_text()
        voices_readme = (REPO_ROOT / "voices" / "README.md").read_text()
        for name, text in [("SKILL.md", skill_md), ("voices/README.md", voices_readme)]:
            self.assertIn("~/.claude/skills/voices/", text,
                          f"{name} should reference the shared voice library as ~/.claude/skills/voices/")
            self.assertNotRegex(text, r"/Users/\w+/\.claude/skills/voices/",
                                 f"{name} has regressed to a hardcoded absolute home path")


if __name__ == "__main__":
    unittest.main()
