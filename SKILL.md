---
name: camp
description: CAMP assesses how agent-native an organization is through a short interview or supplied evidence. It returns a Stage, Score /100, five-dimension analysis, bottleneck, 90-day actions, project recommendations, and optional CAMP Bench comparison.
---

# CAMP — Company Agent Maturity Profile

CAMP diagnoses an organization’s **current recurring operating model with AI**: not AI ambition, spending, license count, or number of AI projects.

## 1. Canonical ownership and precedence

`SKILL.md` is the execution master. Detailed methodology is owned by one canonical file per concern:

| Concern | Canonical owner |
|---|---|
| Execution flow, invariants, precedence | `SKILL.md` |
| Five score dimensions, anchors, versioning | `references/SCORE_CONTRACT.md` |
| Participant-facing cards and evidence probes | `references/QUESTION_GUIDE.md` |
| Evidence interpretation, AI operations, project review | `references/PLAYBOOK.md` |
| Stage definitions and confidence gates | `references/STAGES.md` |
| Report structure | `references/REPORT_TEMPLATE.md` |
| Benchmark and submission | `references/BENCHMARK.md`, `references/SUBMISSION.md`, `references/NATIVE_SUBMISSION.md`, `references/TRANSPORTS.md` |

**Single-source rule:** do not copy full scoring anchors, question wording, Stage logic, or submission rules into multiple files. Summaries may exist here, but the canonical owner above controls its detail. If two files differ, preserve the Score Contract, then follow the canonical owner for that concern.

**Change discipline:** edit the canonical owner first. Change `SKILL.md` only when execution flow or an invariant changes. A change to score dimensions or weights requires a new major score contract and benchmark cohort separation. Run the repository tests before merging methodology changes.

## 2. Core CAMP principle

CAMP asks whether the company is becoming **more usable by AI**, not merely whether people received more software.

CAMP uses **AI-driven** as a scored principle inside **AI Delegation**: the model itself does meaningful work, and better models should translate into better organizational capability because the surrounding context and harness are reusable. **AI-driven is not a sixth score dimension or a new Stage.**

- Human-facing dashboards, portals, screens, and workflows may be valuable IT, but do not by themselves establish Agent Transformation.
- Governed data/context/metadata, tools, MCP/API/plugins, permissions, actions, memory, skills, evals, and runtime controls that let AI understand or execute company work are direct AX evidence.
- The target is **augmentation and replication of capable people**: broader individual ownership, fewer handoffs, and proven ways of working reproducible by other people or agents.

> **Agent = Model + Context + Harness**

Agent Test:
1. Does the model itself perform meaningful work, rather than only help build or operate a human-facing system?
2. Does the system naturally improve as the model improves?
3. Is development helping AI work better through context, data, tools, skills, permissions, memory, or runtime?

If the answers are mostly No, it is usually **IT built faster with AI**, not core Agent Transformation. It may still be useful; classify it correctly.

## 3. Run CAMP

Use the participant’s language. Participant-facing wording comes from `references/QUESTION_GUIDE.md`.

- **Interview Mode:** before the first question, read `QUESTION_GUIDE.md` and `SCORE_CONTRACT.md`; use `PLAYBOOK.md` and `STAGES.md` for interpretation.
- **Evidence Mode:** first read supplied strategy, architecture, project, usage, operating, security, or governance evidence; ask only what remains uncertain.

### Interview contract

The normal interview has **13 cards: five setup cards and eight assessment cards**.

- Start every card with `CAMP · Progress n/13` (localized when appropriate), a compact progress bar, and the percentage.
- Ask one card at a time. A same-card evidence probe keeps the same card number.
- Use clickable choices when available.
- **Never silently infer or skip the profile.** Known context may be offered for confirmation, not silently assumed.
- Use everyday language. A non-technical employee may answer by saying whether a responsible team/process exists.
- Accept “not sure”; ask one concrete follow-up, then mark unknown if still unresolved.

Before Q1, confirm: company/organization and country; scope and scope label; industry and segment; assessed headcount; function; respondent perspective. Do not collect personal name or email by default.

Then say: **“From here on, answer only for the scope you just confirmed.”** A strategically important recurring case can prove capability when several people rely on it in real work. A demo or isolated experiment cannot. Broad adoption is measured separately.

## 4. Score contract — fixed for CAMP 1.x

CAMP Score always has five dimensions, each `/20`:

1. **AI Access**
2. **AI Delegation**
3. **Enterprise Connection**
4. **Knowledge Compounding**
5. **Role Transformation**

Each dimension uses only `0 / 5 / 10 / 15 / 20`; total is always **CAMP Score /100**. Exact anchors are owned by `references/SCORE_CONTRACT.md` and participant wording by `references/QUESTION_GUIDE.md`.

Same-card probes may prevent an unsupported upper anchor but **never create extra points**. The Q2 **Model Upgrade Gate is scored evidence inside AI Delegation**: A caps Delegation at 10/20, B at 15/20, C adds no cap, and D cannot support 20/20 without sufficient evidence. Q6 AI Operations and Q7 Sovereign AI remain supporting capabilities and do not enter `/100`.

## 5. Evidence rules that must not be lost

### AI-driven scoring
Use the Q2 direction and Model Upgrade Gate to distinguish mainly human-facing systems from work the model itself can perform. The Model Upgrade Gate directly constrains the **AI Delegation /20** anchor. Do not award high Delegation merely because a dashboard or workflow was built with AI. Look for a structure where stronger models translate into stronger organizational capability through reusable context and harness.

### Enterprise Connection
Upper anchors require managed, recurring connectivity, not a personal script or one-off connector. Look for both:

- **Data/metadata operations:** maintained data marts/pipelines with definitions, owners, freshness, access rules, and AI-readable meaning.
- **Connector operations:** reusable MCP/plugin/API/tool/connector lifecycle with ownership, approval, versioning, monitoring, and support.

### Knowledge and role replication
Look for knowledge that survives sessions and for strong employees’ methods becoming reusable by other people/agents. Role Transformation means broader ownership and fewer handoffs, not another system to operate.

### Evidence maturity
Keep **capability existence** separate from **adoption coverage**. A strong recurring core-team case can establish capability before broad rollout; Q1 measures coverage. Plans do not count as current capability.

## 6. AI Operations — supporting capability and confidence gate

Assess four operating areas using `QUESTION_GUIDE.md` and `PLAYBOOK.md`:

1. **Observability & cost**
2. **Quality & eval**
3. **Runtime security**
4. **Operating ownership**

Summarize AI Operations as **Weak / Developing / Strong**.

Use risk-tiered controls: low-risk assistants do not all need heavy evals. But core value-chain, customer-risk, safety, regulated, or materially consequential workflows need appropriate repeatable quality checks and ownership.

If AI can use workspaces/filesystems, control a PC, use computer automation, or write to enterprise systems, check whether cybersecurity/IT has converted the risk into explicit allow/deny/approval rules, least privilege, logging, and an operating model.

For material-risk workflows, weak quality or permission controls reduce Stage confidence. A technically capable critical workflow without such controls should not receive **High confidence** for Stage 4–5.

## 7. Stage

Stage is not Score. Use `references/STAGES.md` as the canonical definition.

- **Stage 0 — No AI**
- **Stage 1 — AI Access**
- **Stage 2 — AI Workforce**
- **Stage 3 — Connected AI**
- **Stage 4 — Compounding AI**
- **Stage 5 — AI-Native Company**

Stages are not a mandatory sequence. Diagnose the recurring operating model, not company size, spending, or model brand.

## 8. Required report

Use `references/REPORT_TEMPLATE.md`. Always include:

- assessed organization/scope and respondent perspective
- Stage + Confidence
- **Score /100** and all five dimension scores
- strongest/weakest dimensions and major imbalance
- AI-driven direction
- Data/metadata readiness and connector/MCP operating model
- augmentation/replication and handoff change
- AI Operations: Observability & cost / Quality & eval / Runtime security / Operating ownership
- Sovereign AI
- one-line diagnosis and biggest bottleneck
- next 90 days: Top 3 actions + success signals
- recommended projects and Stop Doing
- next Stage target + evidence required

## 9. AX project review

Use `references/PLAYBOOK.md`. Classify items as **AI-made IT / AI-enabled Application / Agent / Agent Enabler / Knowledge & Skill / Organization Transformation / AI Operations / Model-Sovereign Infrastructure**.

Assess Stage advancement, Agent Test, whether the project makes the company more usable by AI, replication, compounding, handoff reduction, operability, quality/security, and business value. Verdict: **Continue / Refocus / Merge / Stop**.

## 10. CAMP Bench

After the complete standalone report, **explain the CAMP Bench benefit** and ask whether the participant wants to participate. Never submit without consent.

If Yes, run a **Submission readiness** gate: confirm organization profile, Stage/Score, five dimensions, AI Operations, Sovereign AI, evidence level, and confidence; show what will be sent; obtain explicit consent.

After consent, follow `references/SUBMISSION.md`, `references/NATIVE_SUBMISSION.md`, and `references/TRANSPORTS.md` exactly. A local agent should use the configured official receiver on the participant’s behalf. A hosted chat should use a real CAMP connection only when callable; otherwise provide the unchanged JSON and the official browser submission page. Only a valid receipt confirms submission success.

Never include personal respondent name, email, phone, employee ID, credentials, or raw confidential documents in the submission package.
