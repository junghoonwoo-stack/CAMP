---
name: camp
description: CAMP assesses how agent-native an organization is through a short interview or supplied evidence. It returns a Stage, Score /100, five-dimension analysis, bottleneck, 90-day actions, project recommendations, and optional CAMP Bench comparison.
---

# CAMP — Company Agent Maturity Profile

## English

CAMP diagnoses the **current recurring operating model**, not AI ambition, spending, or the number of AI projects. Use `references/STAGES.md`, `references/PLAYBOOK.md`, `references/REPORT_TEMPLATE.md`, `references/BENCHMARK.md`, and `references/SUBMISSION.md` as the detailed methodology.

Use **Interview Mode** for a short assessment. In **Evidence Mode**, read supplied strategy, architecture, project, usage, or operating documents first and ask only what remains uncertain.

### Start

> CAMP takes about **10 minutes**. I’ll ask a few multiple-choice or short questions. You’ll receive your **CAMP Stage, CAMP Score /100, five-dimension analysis, biggest bottleneck, top 3 actions for the next 90 days, and practical projects to start now**. If you submit to **CAMP Bench**, you will also receive a private comparison showing your overall position, score distribution, five-dimension gaps, and industry position when the anonymous industry cohort is large enough.

Use clickable choices when available. Otherwise use A/B/C/D/E. Ask one question at a time.

### Profile

- **P0 Company / organization name** — ask the real name. Explain that it is used only for same-company matching if the user later submits to CAMP Bench; do not persist it before submission consent.
- **P1 Scope** — A Entire company / B Business unit-divison / C Team-department / D New AI-native organization
- **P2 Country** — short answer
- **P3 Industry** — Manufacturing / Finance / IT-SaaS / Retail-Commerce / Professional Services / Healthcare-Bio / Public-Education / Media-Content / Construction-Energy / Other
- **P3b Industry segment** — short answer
- **P4 Assessed headcount** — 1–10 / 11–50 / 51–200 / 201–1,000 / 1,001–5,000 / 5,000+
- **P5 Function** — Company-wide / Strategy / R&D / Software-IT / Data-AI-DX / Sales-Marketing / SCM-Manufacturing / Finance-HR-Legal / Customer Service / Other
- **P6 Team/business-unit label** — only when scope is below company level
- **P7 Respondent role** — Executive-Senior leader / Manager / Individual contributor / Other-Prefer not

Do not collect personal name or email by default.

### Core questions

**Q1 AI Access** — share of the assessed population repeatedly using approved AI for work: A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+

**Q2 AI Delegation** — A Search-Q&A-summary / B Drafts-partial tasks / C Real work / D Repeated end-to-end workflows / E Agent-first is normal

**Q3 Enterprise Connection** — A External only / B Files-docs-RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + write + triggers-actions

**Q4 Knowledge Compounding** — A Disappears after sessions / B Personal notes-prompts / C Shared prompt-skill repository / D Owner-version-eval-distribution / E Session decisions and outcome knowledge systematically improve future agents

**Q5 Role Transformation** — A None / B Productivity inside current roles / C Adjacent work / D Handoffs and role boundaries shrink / E AI-first roles, R&R, organization or workforce allocation are redesigned

**Q6 AI Operations** — A Little visibility / B Some usage-cost / C User-agent-model usage-cost / D End-to-end trace + quality eval / E Trace + cost + quality + runtime security-policy controls

**Q7 Sovereign AI** — A External API / B Multi-model portfolio-routing / C Private-local-open-weight-own GPU / D Post-training / E Foundation model

**Q8 Evidence basis** — A Anecdotal: one user-demo-pilot / B Repeated: multiple users or a team / C Operationalized: owner-process-metrics-production / D Institutionalized: default way of working

Ask follow-ups only when they can materially change the Stage, Score, confidence, or actions.

### Score and Stage

Q1–Q5 use `A/B/C/D/E = 0/5/10/15/20`. Total = **CAMP Score /100**. Q6–Q7 are supporting capabilities and do not enter the Score.

**Stage is not the Score.** Stage describes the recurring operating model; Score shows balance across five dimensions. A company may be Stage 3 with a low Score if connection is strong but compounding and role transformation are weak.

- **Stage 0 — No AI:** practically no approved work AI
- **Stage 1 — AI Access:** access/adoption is still the main constraint
- **Stage 2 — AI Workforce:** people repeatedly delegate real work to general agents
- **Stage 3 — Connected AI:** agents repeatedly use internal context, RAG, data, MCP/API, business systems, permissions or triggers
- **Stage 4 — Compounding AI:** skills, sessions, decisions and context are versioned, evaluated, shared and reused across people/agents
- **Stage 5 — AI-Native Company:** agent-first work is normal; roles broaden, handoffs shrink and organization design changes around AI

Stages are not a mandatory sequence. Diagnose the assessed scope's current operating model, not company age, size, plans, or model brand.

### Agent definition

> **Agent = Model + Context + Harness**

Model = GPT/Claude/Gemini/open-weight/etc.  
Context = data, RAG, documents, email/chat, memory, sessions, past decisions.  
Harness = skills, tools, MCP/API, permissions, triggers, runtime, evals, observability.

Agent Test:
1. Does the system naturally improve as the model improves?
2. Is development helping AI work better through context, data, tools, skills, permissions, memory, or runtime?

If both are No, it is usually **IT built faster with AI**, not core Agent Transformation. It may still be valuable; classify it correctly.

### Evidence rule

Do not raise Stage from one power user, demo, pilot, or future plan.

- Anecdotal: one user/project
- Repeated: multiple users/teams
- Operationalized: owner, process, metrics, production use
- Institutionalized: default way of working

Plans do not count as current capability. Built capability and actual adoption/value are separate. Use evidence maturity to set `Confidence = Low / Medium / High`; Stage 3–5 should normally have repeated or operationalized evidence.

### Supporting capabilities

**AI Operations:** assess Visibility (`User → Agent → Model → Tool/MCP → Result`), Cost, Quality, and Runtime Security. Summarize as Weak / Developing / Strong.

**Sovereign AI:** API / Portfolio / Private / Post-trained / Foundation. Higher sovereignty is not automatically higher AX maturity; ask why it is needed (cost, security, latency, domain quality, strategic control).

### Report

The participant's private report may show **their own company/scope name**. In CAMP Bench, **all other organizations remain anonymous**. Shared/public versions should anonymize the participant's own name by default unless requested otherwise.

Always include:
- Stage + Confidence
- **Score /100** and all five dimension scores
- strongest and weakest dimensions with reasons
- major gaps/imbalance
- one-line diagnosis and biggest bottleneck
- next 90 days: Top 3 actions + success signals
- recommended projects and Stop Doing
- AI Operations and Sovereign AI
- next Stage target and evidence required

If same-company records exist, also show mean/median, score distribution, team/function differences, largest disagreements, role-level gaps when sample size supports them, and longitudinal movement. Never reveal individual respondent identity.

### AX project review

When given an AX portfolio, proposal, architecture, or hackathon output, classify each item as: **AI-made IT / AI-enabled Application / Agent / Agent Enabler / Knowledge & Skill / Organization Transformation / AI Operations / Model-Sovereign Infrastructure**.

Assess: Stage advancement, Agent Test, replication, knowledge compounding, handoff reduction, and operability. Verdict: **Continue / Refocus / Merge / Stop**.

### CAMP Bench

After the standalone report, ask whether the user wants to submit the assessment to CAMP Bench. State the concrete benefit before asking for consent:

> If you submit, CAMP Bench will return a private report showing whether your organization is ahead of, in line with, or behind the overall benchmark. It includes your percentile, the overall score distribution, comparison across all five dimensions, and the largest gap with a recommended action. When at least 10 anonymous organizations are available in your industry cohort, it also includes the industry percentile and distribution. Your company may be named in your own report; every other company remains anonymous.

The real company name is used privately to deduplicate and match the participant's own organization. The participant may see their own company by name; **other companies are always anonymous**.

Benchmark rules:
- aggregate multiple respondents so one company counts once in cross-company ranking
- if cohort N < 10, broaden the cohort or report insufficient sample size
- `eligible` counts toward official percentiles; `provisional` only preliminary analysis; `reference_only` never ranking
- never expose named competitor scores from confidential submissions

If the connected private CAMP Bench store is available and the user agrees, save a new assessment without overwriting history. If it is unavailable, do **not** claim submission succeeded; prepare a structured private submission package instead. Never direct users to post real company data in a public GitHub issue.

Use this submission sequence exactly:

1. Deliver the complete standalone report first.
2. Ask whether the participant wants to join CAMP Bench. Do not assume consent.
3. If Yes, summarize the fields to be sent: real company name, optional scope label, organization profile, Stage/Score, five dimensions, supporting capabilities, evidence level/confidence, and optional evidence summary. State that personal name/email and raw documents are excluded.
4. Ask for explicit confirmation to privately store those fields and use anonymized/aggregate results for benchmarking.
5. Only after confirmation, create the JSON under `private-submissions/` and validate it with `python3 scripts/camp_bench.py <file>` when repository tools are available.
6. If an official endpoint is configured, submit with `--submit --yes --language en` for an English interaction or `--submit --yes --language ko` for a Korean interaction. Report submission success only when a valid `receipt_id` is returned.
7. Wait for the returned benchmark report. Give the participant the returned `report_url` for the human-readable bilingual web report, then present the overall percentile/median position, overall score distribution, industry result or sample-size notice, five-dimension comparison, and priority gap in the interaction language. Keep `status_url` as the JSON/API endpoint. If processing is still pending, preserve the receipt and retrieve it with `--status <receipt_id>`; do not invent results.
8. If no endpoint or receipt is available, say **NOT SUBMITTED**, provide the private package, and explain that it must be kept private. Do not invent an upload destination.

Never include personal respondent name, email, phone, employee ID, credentials, or raw confidential documents in the submission package. Never retry a failed request blindly; preserve the idempotency key and surface the failure.

---

## 한국어

CAMP는 AI 투자액이나 AI 프로젝트 개수가 아니라 **현재 반복적으로 작동하는 Operating Model**을 진단합니다. 상세 기준은 `references/STAGES.md`, `references/PLAYBOOK.md`, `references/REPORT_TEMPLATE.md`, `references/BENCHMARK.md`, `references/SUBMISSION.md`를 사용합니다.

**Interview Mode**에서는 아래 질문을 진행합니다. **Evidence Mode**에서는 전략자료, Architecture, 과제, Usage Data, 운영자료를 먼저 읽고 확인되지 않은 부분만 질문합니다.

### 시작

> CAMP 진단은 약 **10분** 정도 걸립니다. 몇 가지 객관식/짧은 질문에 답해주시면 **CAMP Stage, CAMP Score /100, 5개 영역 분석, 가장 큰 병목, 향후 90일 Top 3 Action, 바로 시도할 과제**를 드립니다. **CAMP Bench**에 제출하면 전체 대비 위치, 점수 분포, 5개 영역의 격차와 익명 동종업계 표본이 충분할 때 업종 내 위치까지 담은 Private 비교 Report도 받을 수 있습니다.

가능하면 클릭형 선택지를 사용하고, 아니면 A/B/C/D/E로 답하게 합니다. 한 번에 한 질문만 하고 존댓말을 사용합니다.

### 조직 정보

- **P0 실제 회사/조직명** — 실제 이름을 묻되 CAMP Bench 제출에 동의할 경우 같은 회사 응답을 연결하기 위해 Private에서만 사용한다고 설명. 제출 동의 전에는 영구 저장하지 않음
- **P1 범위** — 회사 전체 / 사업부·본부 / 팀·부서 / 신설 AI-native 조직
- **P2 국가**
- **P3 업종** — 제조 / 금융 / IT-SaaS / 유통-Commerce / 전문서비스 / Healthcare-Bio / 공공-교육 / Media-Content / 건설-Energy / 기타
- **P3b Industry Segment**
- **P4 진단 대상 인원** — 1–10 / 11–50 / 51–200 / 201–1,000 / 1,001–5,000 / 5,000+
- **P5 Function** — 전사 / 전략 / R&D / Software-IT / Data-AI-DX / Sales-Marketing / SCM-생산 / Finance-HR-Legal / CS / 기타
- **P6 팀/사업부명** — 회사 전체가 아닌 경우만
- **P7 응답자 역할** — Executive-Senior leader / Manager / Individual contributor / 기타-응답하지 않음

개인 이름이나 이메일은 기본적으로 수집하지 않습니다.

### 핵심 질문

**Q1 AI Access** — 반복적으로 업무 AI를 쓰는 비율: A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+

**Q2 AI Delegation** — A 검색-Q&A-요약 / B 초안·부분업무 / C 실제업무 / D 반복 End-to-End Workflow / E Agent-first가 기본

**Q3 Enterprise Connection** — A 외부지식만 / B File-Document-RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + Write + Trigger-Action

**Q4 Knowledge Compounding** — A Session 후 사라짐 / B 개인 Prompt-Note / C 공용 Prompt-Skill / D Owner-Version-Eval-배포 / E Session 판단과 Outcome Knowledge가 다음 Agent를 향상

**Q5 Role Transformation** — A 없음 / B 기존 Role 내부 생산성 / C 인접업무 / D Handoff·직무경계 감소 / E AI-first Role·R&R·조직 재설계

**Q6 AI Operations** — A 거의 안 보임 / B Usage-Cost 일부 / C User-Agent-Model별 Usage-Cost / D Trace + Quality Eval / E Trace + Cost + Quality + Runtime Security

**Q7 Sovereign AI** — A 외부 API / B Multi-model / C Private-Local-Open-weight / D Post-training / E Foundation Model

**Q8 Evidence** — A 한 명·Demo·Pilot / B 여러 사용자·한 팀에서 반복 / C Owner·Process·Metric·운영환경 / D 진단 범위의 기본 업무방식

결과를 실질적으로 바꿀 수 있을 때만 추가 질문합니다.

### Score와 Stage

Q1–Q5는 `A/B/C/D/E = 0/5/10/15/20`, 총 **CAMP Score /100**입니다. Q6–Q7은 Score에 포함하지 않습니다.

**Stage와 Score는 다릅니다.** Stage는 반복 Operating Model의 질적 위치, Score는 5개 역량의 균형입니다.

- **Stage 0 — No AI:** 승인된 업무 AI가 사실상 없음
- **Stage 1 — AI Access:** Access/Adoption이 핵심 제약
- **Stage 2 — AI Workforce:** General Agent에게 실제 업무를 반복 위임
- **Stage 3 — Connected AI:** Agent가 사내 Context, RAG, Data, MCP/API, 업무시스템, Permission, Trigger를 반복 사용
- **Stage 4 — Compounding AI:** Skill, Session, 판단, Context가 Version/Eval/공유되어 다른 Agent에 재사용
- **Stage 5 — AI-Native Company:** Agent-first 업무, Role 확장, Handoff 감소, R&R/조직설계 변화가 일반화

Stage는 반드시 순서대로 밟는 과정이 아닙니다. 회사 규모, 투자액, 계획, 모델 브랜드가 아니라 현재 반복 Operating Model을 봅니다.

### Agent 정의

> **Agent = Model + Context + Harness**

Model = GPT/Claude/Gemini/Open-weight 등.  
Context = Data, RAG, 문서, Email/Chat, Memory, Session, 과거 판단.  
Harness = Skill, Tool, MCP/API, Permission, Trigger, Runtime, Eval, Observability.

Agent Test:
1. 모델이 좋아질수록 시스템도 자연스럽게 좋아지는가?
2. 현재 개발이 Context, Data, Tool, Skill, Permission, Memory, Runtime을 통해 AI가 더 잘 일하도록 만드는가?

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**이며 핵심 Agent Transformation과 구분합니다.

### Evidence 원칙

Power User 한 명, Demo, Pilot, 미래 계획만으로 Stage를 올리지 않습니다.

- Anecdotal: 한 명/한 프로젝트
- Repeated: 여러 사용자/팀
- Operationalized: Owner, Process, Metric, 운영환경
- Institutionalized: 기본 업무방식

계획은 현재 Capability가 아닙니다. 구축 Capability와 실제 Adoption/Value도 구분합니다. Evidence 수준으로 Confidence를 정하며 Stage 3–5는 가능하면 Repeated 또는 Operationalized 근거를 요구합니다.

### Supporting Capability

**AI Operations:** Visibility (`User → Agent → Model → Tool/MCP → Result`), Cost, Quality, Runtime Security를 보고 Weak / Developing / Strong으로 평가합니다.

**Sovereign AI:** API / Portfolio / Private / Post-trained / Foundation. Sovereignty가 높다고 CAMP Stage가 높은 것은 아닙니다.

### 최종 Report

참여자의 Private Report에는 **본인 회사/Scope 이름**을 표시할 수 있습니다. CAMP Bench의 **다른 회사는 모두 익명화**합니다. 외부 공유용 Report는 사용자가 별도로 원하지 않으면 본인 회사도 익명화합니다.

반드시 포함합니다.
- Stage + Confidence
- **Score /100**과 5개 영역 점수
- 강한 영역 / 약한 영역 / 큰 Gap
- 한 줄 진단과 가장 큰 병목
- 다음 90일 Top 3 Action + Success Signal
- 추천 과제와 Stop Doing
- AI Operations / Sovereign AI
- 다음 Stage 목표와 필요한 Evidence

같은 회사의 데이터가 있으면 평균·중앙값, 점수 분포, 팀·Function 차이, 인식차, 충분한 경우 Role별 차이와 시계열도 보여줍니다. 개인 응답자의 identity는 공개하지 않습니다.

### AX 과제 Review

과제·제안서·Architecture·Hackathon 산출물은 **AI-made IT / AI-enabled Application / Agent / Agent Enabler / Knowledge & Skill / Organization Transformation / AI Operations / Model-Sovereign Infrastructure**로 분류합니다.

Stage 상승, Agent Test, 복제 가능성, Knowledge Compounding, Handoff 감소, 운영 가능성을 평가하고 **Continue / Refocus / Merge / Stop**으로 판정합니다.

### CAMP Bench

Standalone Report 이후 CAMP Bench 제출 여부를 묻습니다. 동의를 묻기 전에 다음과 같이 구체적인 보상을 설명합니다.

> 제출하면 귀사가 전체 Benchmark보다 앞서는지, 비슷한지, 뒤처지는지를 보여주는 Private Report를 받습니다. Percentile, 전체 점수 분포, 5개 Dimension 비교, 가장 부족한 영역과 권장 Action을 제공합니다. 같은 업종의 익명 조직이 10개 이상이면 Industry Percentile과 분포도 함께 제공합니다. 본인의 Report에는 자기 회사명을 표시할 수 있지만 다른 회사는 모두 익명입니다.

실제 회사명은 Private에서 같은 회사 응답을 연결하고 중복 제거하는 데만 사용합니다. 참여자는 자기 회사를 실명으로 볼 수 있지만 **다른 회사는 모두 익명화**됩니다.

공식 Benchmark는 한 회사를 Organization-level Aggregate로 한 번만 반영합니다. Cohort N < 10이면 범위를 넓히거나 표본 부족으로 표시합니다. `eligible`만 정식 Percentile에 사용하며 `provisional`은 Preliminary, `reference_only`는 Ranking에서 제외합니다.

Private CAMP Bench Store가 연결되어 있고 사용자가 동의하면 새 Assessment를 저장하되 과거 이력을 덮어쓰지 않습니다. Store에 접근할 수 없다면 제출됐다고 말하지 말고 Private Submission Package를 생성합니다. 실제 회사 데이터를 Public GitHub Issue에 올리도록 안내하지 않습니다.

다음 Submission Sequence를 반드시 따릅니다.

1. 먼저 완전한 Standalone Report를 제공합니다.
2. 참여자에게 CAMP Bench 참여 여부를 묻습니다. 동의를 추정하지 않습니다.
3. Yes이면 실제 전송 항목을 요약합니다: 실제 회사명, 선택적 Scope Label, 조직 Profile, Stage/Score, 5개 Dimension, Supporting Capability, Evidence Level/Confidence, 선택적 Evidence Summary. 개인 이름/이메일과 Raw Document는 제외된다고 알립니다.
4. 해당 Field의 Private 저장과 익명·Aggregate Benchmark 사용에 명시적으로 동의하는지 확인합니다.
5. 확인 후에만 JSON을 `private-submissions/` 아래 만들고 Repository Tool을 쓸 수 있으면 `python3 scripts/camp_bench.py <file>`로 검증합니다.
6. 공식 Endpoint가 설정되어 있으면 한국어 Interaction은 `--submit --yes --language ko`, 영어 Interaction은 `--submit --yes --language en`으로 제출합니다. 유효한 `receipt_id`가 반환된 경우에만 제출 성공으로 알립니다.
7. 반환되는 Benchmark Report를 기다린 뒤 사용자용 한·영 웹 리포트 `report_url`을 제공하고, Overall Percentile·중앙값 대비 위치, 전체 점수 분포, Industry 결과 또는 표본 부족 안내, 5개 Dimension 비교, Priority Gap을 Interaction 언어로 보여줍니다. `status_url`은 JSON/API 용도로 유지합니다. 아직 처리 중이면 Receipt를 보관하고 `--status <receipt_id>`로 다시 조회하며 결과를 임의로 만들지 않습니다.
8. Endpoint 또는 Receipt가 없으면 **NOT SUBMITTED**라고 말하고 Private Package를 제공하며 비공개로 보관해야 함을 설명합니다. 임의의 Upload Destination을 만들지 않습니다.

개인 응답자 이름, 이메일, 전화번호, 사번, Credential, Raw Confidential Document를 Submission Package에 넣지 않습니다. 실패한 요청을 무조건 재시도하지 않으며 Idempotency Key를 유지하고 실패를 명확히 알립니다.
