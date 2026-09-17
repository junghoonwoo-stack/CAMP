import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InterviewContractTests(unittest.TestCase):
    def test_profile_progress_and_scope_rules_are_required(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        guide = (ROOT / "references" / "QUESTION_GUIDE.md").read_text(encoding="utf-8")

        self.assertIn("13 cards", skill)
        self.assertIn("Never silently infer or skip the profile", skill)
        self.assertIn("CAMP · Progress n/13", skill)
        self.assertIn("capability existence", skill)

        # Localized participant-facing copy belongs in QUESTION_GUIDE.
        self.assertIn("CAMP · 진행 n/13", guide)
        self.assertIn("## 한국어 질문", guide)

    def test_agent_first_submission_and_missing_profile_gate_are_required(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        submission = (ROOT / "references" / "SUBMISSION.md").read_text(encoding="utf-8")

        self.assertIn("Submission readiness", skill)
        self.assertIn("explain the CAMP Bench benefit", skill)
        self.assertIn("local agent", skill.lower())
        self.assertIn("official browser submission page", skill)
        self.assertIn("CAMP Bench 제출 페이지", readme)
        self.assertNotIn("python3", readme.lower())
        self.assertNotIn("python3", skill.lower())
        self.assertNotIn("python3", submission.lower())


if __name__ == "__main__":
    unittest.main()
