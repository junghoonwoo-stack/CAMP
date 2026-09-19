# CAMP Score Contract

This is the canonical scoring boundary for **CAMP 1.x**. Question wording and evidence probes may evolve; the score shape and anchor meaning must not drift silently.

## Fixed structure and anchors

CAMP 1.x has five scored dimensions, each worth 20 points. Each dimension uses only `0 / 5 / 10 / 15 / 20`; total is always **CAMP Score /100**.

| Dimension | 0 | 5 | 10 | 15 | 20 |
|---|---|---|---|---|---|
| **AI Access** | <5% recurring users | 5–20% | 21–50% | 51–80% | 81%+ |
| **AI Delegation** | Search/Q&A/summary | Draft/partial task | Meaningful result for human review | Connected multi-step work with context/tools | AI-first delegation is normal; people review/approve/handle exceptions |
| **Enterprise Connection** | External/general info only | Company files/docs/search | Managed internal datasets or everyday work tools | Live business data/systems with managed recurring connection | Controlled read + write/action with permissions, approvals, logs |
| **Knowledge Compounding** | Disappears after sessions | Personal prompts/notes/examples | Shared reusable instructions/examples/methods | Owner + versioning + checks/evals + distribution | Sessions/decisions/corrections/outcomes systematically improve future people/agents |
| **Role Transformation** | Little change | Same role, faster | Adjacent work previously requiring another specialist | Capable methods replicated through AI + fewer handoffs | R&R/team/workforce design changes around work delegated to AI |

한국어로는 각각 **AI 사용범위 / AI 업무위임 / 회사 Data·System 연결 / 지식·업무방식 재사용 / 역할·조직 변화**를 의미하며, 위 Anchor 의미를 그대로 사용함.

## Evidence probes are not score buckets

Questions may be added, removed, or refined as enterprise AI changes. A probe only helps decide which existing anchor is supported; it never creates additional points.

Examples:
- metadata and data-mart operations → **Enterprise Connection** evidence;
- MCP, plugin, API, tool distribution and lifecycle ownership → **Enterprise Connection** evidence;
- replication of a strong employee’s way of working → **Knowledge Compounding** and **Role Transformation** evidence;
- a human-facing dashboard may be useful IT, but does not by itself increase Agent maturity unless it also makes context, tools, permissions, or execution available to AI.

Upper anchors require credible recurring evidence. A personal script, one-off connector, demo, or future plan does not establish an operational capability.

## AI Operations is separate from /100

AI Operations is reported as `Weak / Developing / Strong`; it is not a sixth score dimension. It covers:

- **Observability & cost** — user → agent → model → tool/MCP → result, usage, latency, cost;
- **Quality & eval** — risk-tiered checks appropriate to the consequence of failure;
- **Runtime security** — identity, least privilege, data sensitivity, approval, workspace/filesystem controls, computer use, and action policy;
- **Operating ownership** — clear teams/processes for data/metadata, MCP/plugin/tool lifecycle, AI runtime, security review, and incident response.

Low-risk assistants do not all need heavy evals. Core value-chain, customer-risk, safety, regulated, or materially consequential workflows do need appropriate repeatable quality and runtime controls. Weak controls on such workflows reduce confidence in a Stage 4–5 diagnosis.

## AI-driven transformation rule

**AI-driven is an evidence interpretation lens, not a new score bucket or Stage.** It means the model itself performs meaningful work, and improvements in model capability can translate into better outcomes because the organization has reusable context and harness around the model.

CAMP distinguishes systems built mainly for people to use from capabilities that let AI work. Stronger AX evidence makes the company more **legible or executable to AI**: governed data/metadata, searchable context, APIs/MCP/plugins/tools, permissions, action paths, reusable skills, memory, evals, and runtime controls.

Use three checks:
1. Does the AI model itself understand, decide, create, or act as part of the real workflow?
2. Would a materially better model make the workflow more capable without rebuilding the core surrounding IT?
3. Is the organization building reusable context/harness rather than only another screen or workflow for a person?

These checks interpret evidence inside the existing five anchors; they never add points. If all three are No, classify it as valuable IT or AI-made IT rather than core Agent Transformation.

## Versioning rule

Within **CAMP 1.x**:
- the five dimension names, anchor meanings, and 20-point weights remain fixed;
- total remains `/100`;
- historical benchmark records remain comparable at the dimension level;
- wording, examples, probes, and Stage evidence requirements may become more precise without changing anchor meaning;
- changing a dimension definition, anchor meaning, or weight requires a new major score contract and benchmark cohort separation.

Never silently recalculate historical submissions under a materially different score contract.
