# CAMP Score Contract

This is the canonical scoring boundary for **CAMP 1.x**. Question wording and evidence probes may evolve; the score shape must not drift silently.

## Fixed structure

CAMP 1.x has five scored dimensions, each worth 20 points:

| Dimension | What it measures |
|---|---|
| **AI Access** | How broadly people in the assessed scope repeatedly use approved AI for real work. |
| **AI Delegation** | How much real work people can delegate to AI, from assistance to agent-first execution. |
| **Enterprise Connection** | How reliably AI can use governed company context, data, tools, and systems. |
| **Knowledge Compounding** | Whether useful instructions, decisions, sessions, corrections, and outcomes become reusable organizational assets. |
| **Role Transformation** | Whether AI augments/replicates capable people, reduces handoffs, and changes responsibility or organization design. |

Each dimension uses only `0 / 5 / 10 / 15 / 20`. Total is always **CAMP Score /100**.

한국어로는 각각 **AI 사용범위 / AI 업무위임 / 회사 Data·System 연결 / 지식·업무방식 재사용 / 역할·조직 변화**를 의미하며, 동일하게 각 20점·총 100점임.

## Evidence probes are not score buckets

Questions may be added, removed, or refined as enterprise AI changes. A probe only helps decide which existing anchor is supported; it never creates additional points.

Examples:
- metadata and data-mart operations → **Enterprise Connection** evidence;
- MCP, plugin, API, tool distribution and lifecycle ownership → **Enterprise Connection** evidence;
- replication of a strong employee’s way of working → **Knowledge Compounding** and **Role Transformation** evidence;
- a human-facing dashboard may be useful IT, but does not by itself increase Agent maturity unless it also makes context, tools, permissions, or execution available to AI.

## AI Operations is separate from /100

AI Operations is reported as `Weak / Developing / Strong`; it is not a sixth score dimension. It covers:

- **Observability & cost** — user → agent → model → tool/MCP → result, usage, latency, cost;
- **Quality & eval** — risk-tiered checks appropriate to the consequence of failure;
- **Runtime security** — identity, least privilege, data sensitivity, approval, workspace/filesystem controls, computer use, and action policy;
- **Operating ownership** — clear teams/processes for data/metadata, MCP/plugin/tool lifecycle, AI runtime, security review, and incident response.

Low-risk assistants do not all need heavy evals. Core value-chain, customer-risk, safety, regulated, or materially consequential workflows do need appropriate repeatable quality and runtime controls. Weak controls on such workflows reduce confidence in a Stage 4–5 diagnosis.

## AI-facing transformation rule

CAMP distinguishes systems built mainly for people to use from capabilities that let AI work.

Stronger AX evidence makes the company more **legible or executable to AI**: governed data/metadata, searchable context, APIs/MCP/plugins/tools, permissions, action paths, reusable skills, memory, evals, and runtime controls.

Use three checks:
1. Does the investment increase what AI can understand, decide, or do?
2. Would a better model naturally make the capability more useful?
3. Is the organization building reusable context/harness rather than only another screen or workflow for a person?

If all three are No, classify it as valuable IT or AI-made IT rather than core Agent Transformation.

## Versioning rule

Within **CAMP 1.x**:
- the five dimension names and 20-point weights remain fixed;
- total remains `/100`;
- historical benchmark records remain comparable at the dimension level;
- wording, examples, probes, and Stage evidence requirements may become more precise;
- changing a dimension definition or weight requires a new major score contract and benchmark cohort separation.

Never silently recalculate historical submissions under a materially different score contract.
