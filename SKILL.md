---
name: camp
description: CAMP assesses how agent-native an organization is through a short interview or supplied evidence. It returns a Stage, Score /100, five-dimension analysis, bottleneck, 90-day actions, project recommendations, and optional CAMP Bench comparison.
---

# CAMP — Company Agent Maturity Profile

## English

CAMP diagnoses the organization’s **current recurring operating model with AI**, not AI ambition, spending, license count, or the number of AI projects.

### Authoritative files and precedence

Before running CAMP, use these files together:

1. `SKILL.md` — execution master and non-negotiable operating rules
2. `references/SCORE_CONTRACT.md` — canonical score contract; five scored dimensions × 20 points = CAMP Score /100
3. `references/QUESTION_GUIDE.md` — exact participant-facing interview wording and same-card evidence probes
4. `references/PLAYBOOK.md` — evidence interpretation, AI-facing transformation, operations, security, project review
5. `references/STAGES.md` — Stage definitions and confidence gates
6. `references/REPORT_TEMPLATE.md` — required report structure
7. `references/BENCHMARK.md`, `references/SUBMISSION.md`, `references/NATIVE_SUBMISSION.md`, `references/TRANSPORTS.md` — CAMP Bench rules and submission transport

If wording differs, preserve the **Score Contract and rules in this master**. Participant-facing questions should follow `QUESTION_GUIDE.md`. Evidence probes never create extra score buckets.

### Core CAMP principle

CAMP asks whether the company is being made **more usable by AI**, not merely whether people received more software.

- A human-facing dashboard, portal, screen, or workflow may be valuable IT, but does not by itself establish Agent Transformation.
- Data, context, metadata, tools, MCP/API/plugins, permissions, actions, memory, skills, and runtime controls that make the company more legible or executable to AI are direct AX evidence.
- The objective is not simply to build another system for a person to operate. Look for **augmentation and replication of capable people**: one person can own broader work, fewer handoffs are needed, and proven ways of working can be reproduced by other people or agents.

### Modes

Use **Interview Mode** for a short assessment. Use **Evidence Mode** when strategy, architecture, project, usage, operating, security, or governance evidence is supplied; read it first and ask only what remains uncertain.

In Interview Mode, read `references/QUESTION_GUIDE.md` before the first question.

### Start and UX contract

CAMP takes about **8–10 minutes**. The normal interview has **13 cards: five setup cards and eight assessment cards**.

Begin every card with `CAMP · Progress n/13`, a compact bar such as `███░░░░░░░░░░`, and the percentage. Use native clickable choices when available. Ask one card at a time. A same-card probe stays on the same card number.

**Never silently infer or skip the profile**, even when the organization seems obvious. If prior context supplies an answer, present it for confirmation.

Use everyday language. Technical knowledge is not required. A non-technical employee may answer by saying whether a responsible team or operating process exists. Accept “not sure”; ask one concrete follow-up, then mark unknown if still unclear.

### Required profile — cards 1–5

Collect before Q1:

- company / organization name and country
- scope: Entire company / Business unit-divison / Team-department / New AI-native organization
- scope label when below company level
- industry and industry segment
- assessed headcount band
- function
- respondent perspective category

Do not collect personal name or email by default.

Before Q1 say: **“From here on, answer only for the scope you just confirmed.”** A strategically important recurring case led by a core team may establish capability when several people actually rely on it. A one-off demo or experiment does not. Broad adoption is measured separately in Q1.

## Scored dimensions — cards 6–10

The score contract is fixed for CAMP 1.x:

- **AI Access /20**
- **AI Delegation /20**
- **Enterprise Connection /20**
- **Knowledge Compounding /20**
- **Role Transformation /20**
- **Total = CAMP Score /100**

Each dimension uses only `0 / 5 / 10 / 15 / 20`. Same-card probes validate evidence and can prevent an unsupported upper anchor; they **never add points above 100**.

### Q1 — AI Access

Share of the assessed population repeatedly using approved AI for real work:

A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+.

### Q2 — AI Delegation

Assess how much work **AI itself** completes, not how sophisticated the human-facing UI is.

- 0: search, Q&A, summary
- 5: draft or partial-task help
- 10: completes a meaningful result for human review
- 15: repeatedly carries out connected multi-step work using context/tools
- 20: work is normally delegated to AI first; people review, approve material steps, and handle exceptions

Use the same-card **direction probe** from `QUESTION_GUIDE.md`: are recent AX efforts mostly human-facing dashboards/portals/workflows, mixed, or mostly making data/context/tools/permissions/actions usable by AI? Use it in diagnosis; do not add points.

### Q3 — Enterprise Connection

Assess whether AI can reliably use the company’s internal information and execution surfaces.

- 0: external/general information only
- 5: company files/documents or basic searchable knowledge
- 10: managed internal datasets or everyday work tools; the right current information is reliably available
- 15: live business data/systems are connected and a responsible team operates the connection
- 20: read + controlled write/action, with permissions, approvals, and logs

Upper anchors require more than a personal script or one-off connector. Check two evidence areas inside the same card:

1. **Data/metadata operations** — Is there a team/process maintaining important data marts/pipelines with definition, owner, freshness, access rules, and AI-readable descriptions/metadata?
2. **Connector operations** — Is there a team/process building, approving, versioning, monitoring, and supporting reusable AI connections such as MCP servers, plugins, APIs, tools, or connectors?

These probes do not create extra points.

### Q4 — Knowledge Compounding

Assess whether good ways of working survive one chat or one employee and improve future work.

- 0: disappears after sessions
- 5: personal prompts/notes/examples
- 10: shared instructions/examples/work methods others can reuse
- 15: owner + versioning + checks/evals + distribution
- 20: past sessions, decisions, corrections, and outcomes systematically improve future people/agents

Also check **replication**: can a strong employee’s way of performing an important task be packaged so another person or agent reproduces much of that performance? This is evidence, not an extra score.

### Q5 — Role Transformation

Assess augmentation/replication of people and reduction of handoffs, not the creation of another system.

- 0: little change
- 5: same role, faster
- 10: people can take on adjacent work that previously required another specialist
- 15: capable ways of working are replicated through AI and important work crosses fewer people/teams
- 20: responsibilities, R&R, team structure, or workforce allocation are redesigned around work delegated to AI

A dashboard, portal, or workflow alone does not establish 15/20.

## Supporting capabilities — cards 11–12

Q6 and Q7 do **not** enter CAMP Score /100. They matter for Stage confidence and actions.

### Q6 — AI Operations

Assess four operating capabilities:

1. **Observability & cost** — User → Agent → Model → Tool/MCP → Result, usage, token/cache/model cost, latency
2. **Quality & eval** — repeatable quality checks, especially where a wrong result can damage a core value chain, customer, safety, compliance, or material business outcome
3. **Runtime security** — identity, least privilege, data sensitivity, workspace/filesystem controls, PC/computer-use controls, enterprise write permissions, approvals, logs, incident response
4. **Operating ownership** — named teams/processes that run AI platforms, connectors/MCP/plugins, data access, quality, and security controls

Use the participant-facing A–E choices and same-card quality/security probes in `QUESTION_GUIDE.md`. Summarize overall AI Operations as **Weak / Developing / Strong**.

Do not require heavy evals for every low-risk assistant. For **material-risk workflows**, however, strong maturity requires a defined quality owner/test/evaluation appropriate to the consequence of failure.

If AI can use a workspace/filesystem, control a PC, use computer automation, or write to an enterprise system, check whether cybersecurity/IT has reviewed the risk and converted it into explicit allow/deny/approval rules and an operating model.

For Stage 4–5, weak operations around a material-risk workflow reduce confidence. A critical write/action workflow without clear quality checks or permission controls should not receive **High confidence** merely because the agent is technically capable.

### Q7 — Sovereign AI

A External API / B Multi-model portfolio-routing / C Private-local-open-weight-own GPU / D Post-training / E Foundation model.

Sovereignty is supporting capability, not automatically higher CAMP maturity. Ask why it is needed: cost, security, latency, domain quality, or strategic control.

## Evidence basis — card 13

Q8 distinguishes capability from demonstration:

- A Anecdotal — one person, demo, isolated pilot
- B Repeated — several people/core team repeatedly use it for real work
- C Operationalized — named owner, operating steps, metrics/results/risks checked
- D Institutionalized — normal way of working across the assessed scope

Plans do not count as current capability.

Separate **capability existence** from **adoption coverage**. A strong core production case can establish that a capability exists before broad rollout. Q1 separately measures how widely AI is used.

## Stage

Stage is not the Score. Stage describes the recurring operating model; Score shows balance across the five dimensions.

- **Stage 0 — No AI:** practically no approved work AI
- **Stage 1 — AI Access:** access/adoption remains the main constraint
- **Stage 2 — AI Workforce:** people repeatedly delegate real work to general agents
- **Stage 3 — Connected AI:** agents repeatedly use internal context, data, metadata, MCP/API/tools, enterprise systems, permissions or triggers
- **Stage 4 — Compounding AI:** skills, sessions, decisions, context, corrections and outcomes are versioned/evaluated/shared/reused across people and agents
- **Stage 5 — AI-Native Company:** agent-first work is normal; individual capability is augmented/replicated, roles broaden, handoffs shrink, and organization design changes around AI

Stages are not a mandatory sequence.

## Agent definition and Agent Test

> **Agent = Model + Context + Harness**

Model = GPT/Claude/Gemini/open-weight/etc.  
Context = data, metadata, RAG, documents, email/chat, memory, sessions, past decisions.  
Harness = skills, tools, MCP/API/plugins, permissions, triggers, runtime, evals, observability.

Agent Test:
1. Does the system naturally improve as the model improves?
2. Is development helping AI work better through context, data, tools, skills, permissions, memory, or runtime?

If both are No, it is usually **IT built faster with AI**, not core Agent Transformation. It may still be valuable; classify it correctly.

## Required report

Always include:

- organization / exact assessed scope and respondent perspective
- Stage + Confidence
- **CAMP Score /100** and all five dimension scores
- strongest and weakest dimensions with reasons
- AI-facing direction: human-facing systems vs capabilities AI can use
- Data/metadata readiness
- MCP/plugin/API/tool operating model
- augmentation/replication and handoff change
- AI Operations: Observability & cost / Quality & eval / Runtime security / Operating ownership
- Sovereign AI
- one-line diagnosis and biggest bottleneck
- next 90 days: Top 3 actions + success signals
- recommended projects and Stop Doing
- next Stage target + evidence required

Use `references/REPORT_TEMPLATE.md` for structure.

## AX project review

Classify each item as **AI-made IT / AI-enabled Application / Agent / Agent Enabler / Knowledge & Skill / Organization Transformation / AI Operations / Model-Sovereign Infrastructure**.

Assess Stage advancement, Agent Test, whether it makes the company more usable by AI, replication, knowledge compounding, handoff reduction, data/metadata readiness, connector operability, quality/security operations, and business value. Verdict: **Continue / Refocus / Merge / Stop**.

## CAMP Bench

After the complete standalone report, **explain the CAMP Bench benefit** and ask whether the participant wants to participate. Never submit without consent.

If Yes, run a **Submission readiness** gate. Confirm the organization profile, Stage/Score, five dimensions, AI Operations, Sovereign AI, evidence level and confidence. Show the fields to be sent and obtain explicit consent.

After consent, let the current agent handle submission. A **local agent** should use the configured official receiver on the participant’s behalf. A hosted chat should use a real CAMP connection only when actually callable; otherwise provide the unchanged JSON file and the **official browser submission page** immediately. Do not ask the participant to run validation or submission commands. Follow `references/SUBMISSION.md`, `references/NATIVE_SUBMISSION.md`, and `references/TRANSPORTS.md` exactly. Only a valid receipt confirms submission success.

Never include personal respondent name, email, phone, employee ID, credentials, or raw confidential documents in the submission package.

---

## 한국어

CAMP는 AI 투자액·License 수·AI 과제 개수가 아니라 조직의 **현재 반복적으로 작동하는 AI 업무방식**을 진단합니다.

### 실행 시 반드시 함께 읽을 문서

1. `SKILL.md` — 실행 Master와 필수 운영규칙
2. `references/SCORE_CONTRACT.md` — 5개 점수축 × 20점 = CAMP Score /100의 고정 계약
3. `references/QUESTION_GUIDE.md` — 참여자에게 실제로 보여줄 질문과 같은 카드 Evidence Probe
4. `references/PLAYBOOK.md` — Evidence 해석, AI-facing Transformation, 운영·보안, 과제 Review
5. `references/STAGES.md` — Stage와 Confidence 기준
6. `references/REPORT_TEMPLATE.md` — Report 구조
7. `references/BENCHMARK.md`, `references/SUBMISSION.md`, `references/NATIVE_SUBMISSION.md`, `references/TRANSPORTS.md` — CAMP Bench와 제출 규칙

문구가 다를 경우 **Score Contract와 이 Master의 규칙을 우선**합니다. 화면에 보여줄 질문은 `QUESTION_GUIDE.md`를 사용합니다. Evidence Probe는 새로운 점수항목을 만들지 않습니다.

### CAMP의 핵심 관점

CAMP는 회사가 단순히 사람에게 더 많은 Software를 제공했는지가 아니라 **회사를 AI가 더 잘 읽고 실행할 수 있게 바꾸고 있는가**를 봅니다.

- 사람이 보는 Dashboard, Portal, 화면, Workflow는 필요하고 가치 있을 수 있으나 그 자체로 Agent Transformation은 아님.
- Data, Context, Metadata, Tool, MCP/API/Plugin, Permission, Action, Memory, Skill, Runtime Control을 AI가 사용할 수 있게 만드는 활동은 직접적인 AX Evidence임.
- 목표는 시스템 하나를 더 만드는 것이 아니라 **유능한 개인을 증강·복제**하는 것임. 한 사람이 더 넓은 업무를 책임지고, Handoff가 줄고, 잘하는 사람의 업무방식이 다른 사람이나 Agent에게 재현되는지를 봄.

### 실행 방식

**Interview Mode**는 짧은 진단에 사용합니다. **Evidence Mode**는 전략·Architecture·과제·Usage·운영·보안·Governance 자료를 먼저 읽고 불확실한 것만 묻습니다.

Interview Mode에서는 첫 질문 전에 `references/QUESTION_GUIDE.md`를 반드시 읽습니다.

### 시작과 UX 계약

기본 인터뷰는 **조직 정보 5개 카드 + 진단 질문 8개 카드, 총 13개**입니다. 모든 카드를 `CAMP · 진행 n/13`, `███░░░░░░░░░░` 형태의 진행 막대와 진행률로 시작합니다. 같은 카드의 확인 질문은 같은 번호를 유지합니다.

**조직을 알고 있는 것처럼 보여도 프로필을 조용히 추정하거나 건너뛰지 않습니다.** 앞선 대화에서 아는 값도 확인받습니다.

질문은 기술 배경이 없는 사람도 답할 수 있게 씁니다. 일반 구성원은 “그런 담당 조직/운영 프로세스가 있는지”로 답할 수 있습니다. “잘 모르겠음”을 허용하고 한 번의 구체적인 확인 후에도 모르면 Unknown으로 둡니다.

### 필수 조직 정보 — 1~5번 카드

Q1 전에 회사/조직명과 국가, 진단 Scope, 하위 조직명, 업종/Segment, 인원 구간, Function, 응답자 관점을 확인합니다. 개인 이름이나 이메일은 기본적으로 수집하지 않습니다.

Q1 전에 **“이제부터는 방금 확정한 범위만 생각하고 답해주세요.”**라고 안내합니다. 핵심 조직이 운영하는 중요 사례 하나라도 여러 사람이 실제 업무에서 반복 사용하면 Capability의 근거가 될 수 있습니다. Demo나 단발성 실험은 제외하며 전체 보급률은 Q1에서 따로 봅니다.

## 점수 영역 — 6~10번 카드

CAMP 1.x Score Contract는 고정입니다.

- **AI Access /20**
- **AI Delegation /20**
- **Enterprise Connection /20**
- **Knowledge Compounding /20**
- **Role Transformation /20**
- **총점 = CAMP Score /100**

각 영역은 `0 / 5 / 10 / 15 / 20`만 사용합니다. 같은 카드의 확인 질문은 상위 점수의 근거를 확인하는 Evidence Probe이며 **100점 밖의 가산점을 만들지 않습니다.**

### Q1 — AI Access

승인된 AI를 실제 업무에 반복적으로 사용하는 비율: A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+.

### Q2 — AI Delegation

사람이 보는 UI가 아니라 **AI 자체가 실제 일을 어디까지 수행하는지** 평가합니다.

- 0: 검색·Q&A·요약
- 5: 초안·부분업무 보조
- 10: 의미 있는 결과물을 완성하고 사람이 검토
- 15: Context/Tool을 사용해 연결된 여러 단계를 반복 수행
- 20: 먼저 AI에게 일을 맡기고 사람은 검토·중요 단계 승인·예외처리를 하는 것이 일반적

`QUESTION_GUIDE.md`의 같은 카드 **방향 확인 질문**으로 최근 AX 개발이 사람용 Dashboard/Portal/Workflow 중심인지, 혼합인지, Data/Context/Tool/Permission/Action을 AI가 쓰게 만드는 방향이 중심인지 확인합니다. 진단에 반영하되 가산점은 없음.

### Q3 — Enterprise Connection

AI가 회사 내부의 정보와 실행 수단을 안정적으로 사용할 수 있는지를 평가합니다.

- 0: 외부 일반정보만
- 5: 사내 File/Document 또는 기본 검색지식
- 10: 관리되는 내부 Dataset 또는 일상 업무도구, 최신 정보를 안정적으로 찾을 수 있음
- 15: 실제 Business Data/System 연결 + 이를 운영하는 책임 조직 존재
- 20: Read + 통제된 Write/Action, Permission·Approval·Log 존재

상위 점수는 개인 Script나 일회성 Connector만으로 주지 않습니다. 같은 카드에서 다음을 확인합니다.

1. **Data/Metadata 운영** — 중요 Data Mart/Pipeline의 정의, Owner, Freshness, Access Rule, AI가 이해할 설명/Metadata를 관리하는 조직·프로세스가 있는가?
2. **Connector 운영** — MCP Server, Plugin, API, Tool, Connector를 만들고 승인·Version·Monitoring·Support하는 조직·프로세스가 있는가?

둘 다 Evidence Probe이며 별도 점수는 없음.

### Q4 — Knowledge Compounding

좋은 업무방식이 한 Chat이나 한 개인에게서 끝나지 않고 다음 업무를 향상시키는지 봅니다.

- 0: Session 종료 후 사라짐
- 5: 개인 Prompt/Note/Example
- 10: 다른 사람이 찾아 쓰는 공용 Instruction/Example/업무방법
- 15: Owner + Version + Check/Eval + 배포
- 20: 과거 Session·판단·수정·Outcome이 다음 사람/Agent의 수행을 체계적으로 향상

추가로 **복제 가능성**을 확인합니다. 일을 잘하는 사람의 중요한 업무방식을 Package하여 다른 사람이나 Agent가 상당 부분 재현할 수 있는가? 이는 Evidence이지 별도 점수가 아님.

### Q5 — Role Transformation

시스템 하나를 더 만드는 것이 아니라 **사람의 증강·복제와 Handoff 감소**를 봅니다.

- 0: 거의 변화 없음
- 5: 같은 Role에서 더 빠르게 일함
- 10: 과거 다른 전문가에게 맡기던 인접업무까지 수행
- 15: 유능한 사람의 업무방식이 AI로 복제되고 중요한 업무가 더 적은 사람/팀을 거침
- 20: AI에게 위임하는 업무를 기준으로 R&R, 팀 구조, 인력배치를 재설계

Dashboard, Portal, Workflow 하나만으로 15/20을 주지 않습니다.

## Supporting Capability — 11~12번 카드

Q6–Q7은 **CAMP Score /100에는 포함하지 않습니다.** 대신 Stage Confidence와 Action에 영향을 줍니다.

### Q6 — AI Operations

다음 네 가지를 평가합니다.

1. **Observability & Cost** — User → Agent → Model → Tool/MCP → Result, Usage, Token/Cache/Model Cost, Latency
2. **Quality & Eval** — 특히 Core Value Chain, 고객위험, 안전·규제, 큰 사업손실 가능성이 있는 업무의 반복 가능한 Quality Check/Eval
3. **Runtime Security** — Identity, Least Privilege, Data Sensitivity, Workspace/File System, PC/Computer Use, 기간시스템 Write Permission, Approval, Log, Incident Response
4. **Operating Ownership** — AI Platform, Connector/MCP/Plugin, Data Access, Quality, Security를 운영하는 명시적 조직·프로세스

참여자에게는 `QUESTION_GUIDE.md`의 쉬운 A–E 선택지와 Quality/Security 확인 질문을 사용합니다. 전체 AI Operations는 **Weak / Developing / Strong**으로 요약합니다.

모든 저위험 Assistant에 강한 Eval을 요구하지는 않습니다. 하지만 **틀렸을 때 Core Value Chain, 고객, 안전, 규제, 큰 사업 결과에 영향을 주는 Workflow**에는 결과를 반복 검증할 Quality Owner/Test/Eval이 있어야 높은 성숙도로 봅니다.

AI가 Workspace/File System을 쓰거나 PC를 제어하거나 Computer Use를 하거나 기간시스템에 Write할 수 있다면 Cybersecurity/IT가 Risk를 검토하고 Allow/Deny/Approval Rule과 운영체계로 바꿨는지를 확인합니다.

Stage 4–5에서 Material-risk Workflow의 운영·품질·권한통제가 약하면 **High Confidence**를 주지 않습니다.

### Q7 — Sovereign AI

A 외부 API / B Multi-model Portfolio-Routing / C Private-Local-Open-weight-Own GPU / D Post-training / E Foundation Model.

Sovereignty가 높다고 CAMP Stage가 자동으로 높은 것은 아닙니다. Cost, Security, Latency, Domain Quality, Strategic Control 중 왜 필요한지 봅니다.

## 실제 근거 — 13번 카드

Q8은 Capability와 Demo를 구분합니다.

- A Anecdotal — 한 명, Demo, 단발 Pilot
- B Repeated — 여러 사람/핵심 팀이 실제 업무에서 반복 사용
- C Operationalized — Owner, 운영절차, Metric/Result/Risk Check 존재
- D Institutionalized — 진단 Scope 전체의 일반 업무방식

계획은 현재 Capability로 계산하지 않습니다.

**역량의 존재**와 **보급 범위**를 분리합니다. 강한 핵심 운영사례가 있으면 전사 확산 전에도 Capability 존재를 인정할 수 있으나, 전체 사용범위는 Q1에서 별도로 봅니다.

## Stage

Stage와 Score는 다릅니다.

- **Stage 0 — No AI:** 승인된 업무 AI가 사실상 없음
- **Stage 1 — AI Access:** Access/Adoption이 핵심 제약
- **Stage 2 — AI Workforce:** General Agent에게 실제 업무를 반복 위임
- **Stage 3 — Connected AI:** Agent가 사내 Context, Data, Metadata, MCP/API/Tool, 업무시스템, Permission, Trigger를 반복 사용
- **Stage 4 — Compounding AI:** Skill, Session, 판단, Context, Correction, Outcome이 Version/Eval/공유되어 다음 사람·Agent에 재사용
- **Stage 5 — AI-Native Company:** Agent-first 업무가 일반적이며 개인 역량이 증강·복제되고 Role이 넓어지고 Handoff와 조직 경계가 줄어듦

Stage는 반드시 순서대로 밟는 과정이 아닙니다.

## Agent 정의와 Agent Test

> **Agent = Model + Context + Harness**

Model = GPT/Claude/Gemini/Open-weight 등.  
Context = Data, Metadata, RAG, 문서, Email/Chat, Memory, Session, 과거 판단.  
Harness = Skill, Tool, MCP/API/Plugin, Permission, Trigger, Runtime, Eval, Observability.

Agent Test:
1. 모델이 좋아질수록 시스템도 자연스럽게 좋아지는가?
2. 현재 개발이 Context, Data, Tool, Skill, Permission, Memory, Runtime을 통해 AI가 더 잘 일하도록 만드는가?

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**이며 핵심 Agent Transformation과 구분합니다.

## 최종 Report

반드시 포함합니다.

- 조직 / 정확한 진단 Scope / 응답자 관점
- Stage + Confidence
- **Score /100**과 5개 영역 점수
- 강한 영역 / 약한 영역 / 큰 Gap
- **AI-facing 방향**: 사람용 시스템 중심인지 AI가 사용할 Capability 중심인지
- Data/Metadata Readiness
- MCP/Plugin/API/Tool 운영체계
- 개인 Capability의 증강·복제와 Handoff 변화
- AI Operations: Observability & Cost / Quality & Eval / Runtime Security / Operating Ownership
- Sovereign AI
- 한 줄 진단과 가장 큰 병목
- 다음 90일 Top 3 Action + Success Signal
- 추천 과제와 Stop Doing
- 다음 Stage 목표와 필요한 Evidence

구조는 `references/REPORT_TEMPLATE.md`를 따릅니다.

## AX 과제 Review

과제·제안서·Architecture·Hackathon 산출물을 **AI-made IT / AI-enabled Application / Agent / Agent Enabler / Knowledge & Skill / Organization Transformation / AI Operations / Model-Sovereign Infrastructure**로 분류합니다.

Stage 상승, Agent Test, 회사를 AI가 더 잘 쓰게 만드는지, 개인역량 복제, Knowledge Compounding, Handoff 감소, Data/Metadata Readiness, Connector 운영가능성, Quality/Security 운영, Business Value를 평가하고 **Continue / Refocus / Merge / Stop**으로 판정합니다.

## CAMP Bench

완전한 Standalone Report 뒤에 **CAMP Bench의 혜택을 설명하고 참여 여부를 묻습니다**. 동의 없이 제출하지 않습니다.

참여를 선택하면 **제출 준비** 검사를 합니다. 조직 Profile, Stage/Score, 5개 영역, AI Operations, Sovereign AI, Evidence Level, Confidence가 모두 있는지 확인하고 실제 전송할 내용을 보여준 뒤 명시적 동의를 받습니다.

동의 후 현재 Agent가 제출을 처리합니다. **로컬 Agent**는 참여자를 대신해 설정된 공식 Receiver를 사용합니다. 대화형 AI는 실제 CAMP 연결이 호출 가능한 경우에만 직접 제출하고, 연결이 없으면 원본 JSON 파일과 공식 CAMP Bench 제출 페이지를 즉시 제공합니다. 참여자에게 별도 검증·제출 명령을 실행하게 하지 않습니다. `references/SUBMISSION.md`, `references/NATIVE_SUBMISSION.md`, `references/TRANSPORTS.md`를 정확히 따릅니다. 유효한 접수번호만 제출 성공의 증거입니다.

개인 응답자 이름, 이메일, 전화번호, 사번, Credential, Raw Confidential Document를 Submission Package에 넣지 않습니다.
