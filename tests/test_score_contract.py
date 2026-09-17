import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ScoreContractTests(unittest.TestCase):
    def test_five_dimensions_and_100_point_total_remain_stable(self):
        contract = (ROOT / "references" / "SCORE_CONTRACT.md").read_text(encoding="utf-8")
        schema = json.loads((ROOT / "benchmark" / "submission.schema.json").read_text(encoding="utf-8"))

        self.assertIn("five scored dimensions", contract)
        self.assertIn("AI Access", contract)
        self.assertIn("AI Delegation", contract)
        self.assertIn("Enterprise Connection", contract)
        self.assertIn("Knowledge Compounding", contract)
        self.assertIn("Role Transformation", contract)
        self.assertIn("CAMP Score /100", contract)

        dims = schema["properties"]["dimensions"]
        self.assertEqual(
            dims["required"],
            ["access", "delegation", "connection", "compounding", "transformation"],
        )
        for key in dims["required"]:
            self.assertEqual(dims["properties"][key]["enum"], [0, 5, 10, 15, 20])
        self.assertEqual(schema["properties"]["total_score"]["maximum"], 100)

    def test_new_probes_do_not_create_extra_score_buckets(self):
        guide = (ROOT / "references" / "QUESTION_GUIDE.md").read_text(encoding="utf-8")
        contract = (ROOT / "references" / "SCORE_CONTRACT.md").read_text(encoding="utf-8")

        self.assertIn("evidence probes, not extra score buckets", guide)
        self.assertIn("Same-card probes never create additional points", guide)
        self.assertIn("total remains **/100**", guide)
        self.assertIn("metadata and data-mart operations", contract)
        self.assertIn("MCP, plugin, API, tool distribution", contract)
        self.assertIn("workspace/filesystem controls", contract)
        self.assertIn("human-facing dashboard", contract)

    def test_operations_are_supporting_but_gate_high_stage_confidence(self):
        playbook = (ROOT / "references" / "PLAYBOOK.md").read_text(encoding="utf-8")
        stages = (ROOT / "references" / "STAGES.md").read_text(encoding="utf-8")

        self.assertIn("supporting capability, not a sixth score dimension", playbook)
        self.assertIn("Observability & cost", playbook)
        self.assertIn("Quality & eval", playbook)
        self.assertIn("Runtime security", playbook)
        self.assertIn("Operating ownership", playbook)
        self.assertIn("Stage 4–5 should not receive High confidence", stages)


if __name__ == "__main__":
    unittest.main()
