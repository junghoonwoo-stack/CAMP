import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ScoreContractTests(unittest.TestCase):
    def test_five_dimensions_and_100_point_total_remain_stable(self):
        contract = (ROOT / "references" / "SCORE_CONTRACT.md").read_text(encoding="utf-8")
        schema = json.loads((ROOT / "benchmark" / "submission.schema.json").read_text(encoding="utf-8"))

        for name in [
            "AI Access",
            "AI Delegation",
            "Enterprise Connection",
            "Knowledge Compounding",
            "Role Transformation",
        ]:
            self.assertIn(name, contract)

        dims = schema["properties"]["dimensions"]
        self.assertEqual(
            dims["required"],
            ["access", "delegation", "connection", "compounding", "transformation"],
        )
        for key in dims["required"]:
            self.assertEqual(dims["properties"][key]["enum"], [0, 5, 10, 15, 20])
        self.assertEqual(schema["properties"]["total_score"]["maximum"], 100)

        # CAMP 1.x anchor meanings are intentionally stable.
        for row in [
            "| **AI Access** | <5% recurring users | 5–20% | 21–50% | 51–80% | 81%+ |",
            "| **AI Delegation** | Search/Q&A/summary | Draft/partial task | Meaningful result for human review | Connected multi-step work with context/tools | AI-first delegation is normal; people review/approve/handle exceptions |",
            "| **Enterprise Connection** | External/general info only | Company files/docs/search | Managed internal datasets or everyday work tools | Live business data/systems with managed recurring connection | Controlled read + write/action with permissions, approvals, logs |",
            "| **Knowledge Compounding** | Disappears after sessions | Personal prompts/notes/examples | Shared reusable instructions/examples/methods | Owner + versioning + checks/evals + distribution | Sessions/decisions/corrections/outcomes systematically improve future people/agents |",
            "| **Role Transformation** | Little change | Same role, faster | Adjacent work previously requiring another specialist | Capable methods replicated through AI + fewer handoffs | R&R/team/workforce design changes around work delegated to AI |",
        ]:
            self.assertIn(row, contract)

    def test_evidence_probes_do_not_create_extra_score_buckets(self):
        guide = (ROOT / "references" / "QUESTION_GUIDE.md").read_text(encoding="utf-8")
        contract = (ROOT / "references" / "SCORE_CONTRACT.md").read_text(encoding="utf-8")

        self.assertIn("evidence probes, not extra score buckets", guide)
        self.assertIn("Same-card probes never create additional points", guide)
        self.assertIn("metadata and data-mart operations", contract)
        self.assertIn("MCP, plugin, API, tool distribution", contract)
        self.assertIn("workspace/filesystem controls", contract)
        self.assertIn("human-facing dashboard", contract)

    def test_ai_driven_is_scored_inside_existing_delegation_dimension(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        contract = (ROOT / "references" / "SCORE_CONTRACT.md").read_text(encoding="utf-8")
        guide = (ROOT / "references" / "QUESTION_GUIDE.md").read_text(encoding="utf-8")
        playbook = (ROOT / "references" / "PLAYBOOK.md").read_text(encoding="utf-8")
        stages = (ROOT / "references" / "STAGES.md").read_text(encoding="utf-8")

        self.assertIn("AI-driven is scored inside the existing AI Delegation dimension", contract)
        self.assertIn("AI Delegation is capped at 10/20", contract)
        self.assertIn("AI Delegation is capped at 15/20", contract)
        self.assertIn("Model Upgrade Gate is scored evidence inside AI Delegation", skill)
        self.assertIn("Model Upgrade Gate — affects the AI Delegation score", guide)
        self.assertIn("Model Upgrade Gate", playbook)
        self.assertIn("not an additional Stage", stages)

        # AI-driven changes scoring evidence, not the score structure.
        schema = json.loads((ROOT / "benchmark" / "submission.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(
            schema["properties"]["dimensions"]["required"],
            ["access", "delegation", "connection", "compounding", "transformation"],
        )
        self.assertEqual(schema["properties"]["total_score"]["maximum"], 100)

    def test_operations_are_supporting_but_gate_high_stage_confidence(self):
        playbook = (ROOT / "references" / "PLAYBOOK.md").read_text(encoding="utf-8")
        stages = (ROOT / "references" / "STAGES.md").read_text(encoding="utf-8")

        self.assertIn("supporting capability, not a sixth score dimension", playbook)
        for phrase in ["Observability & cost", "Quality & eval", "Runtime security", "Operating ownership"]:
            self.assertIn(phrase, playbook)
        self.assertIn("Stage 4–5 should not receive High confidence", stages)

    def test_skill_is_concise_execution_master_with_canonical_owners(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        owners = [
            "references/SCORE_CONTRACT.md",
            "references/QUESTION_GUIDE.md",
            "references/PLAYBOOK.md",
            "references/STAGES.md",
            "references/REPORT_TEMPLATE.md",
            "references/BENCHMARK.md",
            "references/SUBMISSION.md",
            "references/NATIVE_SUBMISSION.md",
            "references/TRANSPORTS.md",
        ]
        for path in owners:
            self.assertIn(path, skill)
            self.assertTrue((ROOT / path).exists(), path)

        self.assertIn("Single-source rule", skill)
        self.assertIn("Change discipline", skill)
        self.assertIn("five dimensions", skill)
        self.assertIn("Data/metadata operations", skill)
        self.assertIn("Connector operations", skill)
        self.assertIn("augmentation and replication of capable people", skill)
        self.assertIn("workspaces/filesystems", skill)
        self.assertIn("Operating ownership", skill)
        self.assertIn("never create extra points", skill)

        # Localized participant copy belongs in QUESTION_GUIDE, not a second full master.
        self.assertNotIn("## 한국어", skill)
        self.assertLess(len(skill), 16000)

    def test_score_contract_is_one_compact_canonical_definition(self):
        contract = (ROOT / "references" / "SCORE_CONTRACT.md").read_text(encoding="utf-8")

        self.assertIn("canonical scoring boundary", contract)
        self.assertIn("한국어로는", contract)
        self.assertNotIn("## 한국어", contract)
        self.assertLess(len(contract), 9000)


if __name__ == "__main__":
    unittest.main()
