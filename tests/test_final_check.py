"""Tests for scripts/final_check.py, the measurement the Editor runs last.

Run with `python3 -m unittest discover tests` (stdlib only).
"""
import importlib.util
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "final_check", Path(__file__).resolve().parent.parent / "scripts" / "final_check.py")
fc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fc)


def kinds(text, source=None):
    return [k for k, _, _ in fc.check(text, source)]


class FinalCheckTest(unittest.TestCase):
    def test_clean_text_has_no_hits(self):
        self.assertEqual(kinds("We worked with 30 clients. The plan is not final. We review it Monday.",
                               "30 clients"), [])

    def test_cursed_list_is_read_from_skill_md(self):
        words = fc.cursed_words()
        self.assertIn("leverage", words)
        self.assertIn("streamline", words)

    def test_dashes_but_not_the_signature_line(self):
        self.assertEqual(kinds("A point — an aside.\nAnother -- aside.\n--\nPat"), ["DASH", "DASH"])

    def test_contrast_forms(self):
        for s in ["The work is not a deck, it is a habit.", "It's not about tools, it's about habits.",
                  "This isn't a pilot, it's a program.", "Not just faster but better.",
                  "These are not pilots. This is the work.", "What: Not a new policy.",
                  "This is a sequencing decision, not a build."]:
            self.assertIn("CONTRAST", kinds(s), s)

    def test_numbers_missing_from_source(self):
        self.assertEqual(kinds("35 companies at $20,000 each", "We have 35 clients."), ["NUMBER"])

    def test_no_source_skips_numbers(self):
        self.assertEqual(kinds("35 companies"), [])


if __name__ == "__main__":
    unittest.main()
