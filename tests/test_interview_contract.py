import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InterviewContractTests(unittest.TestCase):
    def test_profile_progress_and_scope_rules_are_required(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        guide = (ROOT / "references" / "QUESTION_GUIDE.md").read_text(encoding="utf-8")

        self.assertIn("13 cards", skill)
        self.assertIn("Never silently infer or skip the profile", skill)
        self.assertIn("Progress n/13", skill)
        self.assertIn("진행 n/13", skill)
        self.assertIn("capability existence", skill)
        self.assertIn("역량의 존재", skill)

    def test_fast_submission_and_missing_profile_gate_are_required(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Submission readiness", skill)
        self.assertIn("제출 준비", skill)
        self.assertIn("--submit --yes --no-wait --language en", skill)
        self.assertIn("--submit --yes --no-wait --language ko", skill)


if __name__ == "__main__":
    unittest.main()
