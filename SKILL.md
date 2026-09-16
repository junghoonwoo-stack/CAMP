---
name: camp
description: CAMP assesses how agent-native an organization is through a short interview or supplied evidence. It returns a Stage, Score /100, five-dimension analysis, bottleneck, 90-day actions, project recommendations, and optional CAMP Bench comparison.
---

# CAMP — Company Agent Maturity Profile

## English

CAMP diagnoses the **current recurring operating model**, not AI ambition, spending, or the number of AI projects. Use `references/STAGES.md`, `references/PLAYBOOK.md`, `references/QUESTION_GUIDE.md`, `references/REPORT_TEMPLATE.md`, `references/BENCHMARK.md`, and `references/SUBMISSION.md` as the detailed methodology. In Interview Mode, read and follow `references/QUESTION_GUIDE.md` before asking the first question.

Use **Interview Mode** for a short assessment. In **Evidence Mode**, read supplied strategy, architecture, project, usage, or operating documents first and ask only what remains uncertain. For submission transport selection, read `references/TRANSPORTS.md`.

### Execution and submission path

There are two supported paths:

1. **Local path:** when a real terminal/VM and the CAMP repository are available, run the local CLI. Validate first, then submit from that same environment after explicit consent. A returned `receipt_id` is the only proof of acceptance.
2. **Cloud-chat path:** when the conversation is running in a hosted chat or sandbox, run the interview in the chat and prepare the exact private JSON package. If a native CAMP connector is actually available, use it. Otherwise stop repeated Python or shell POSTs, offer the unchanged JSON as a download, and send the participant to the official browser submission page. No GitHub account is required.

A repository URL is instructions, not a network permission. Never claim success without a valid `receipt_id`. A DNS or outbound-network error means the browser handoff should be used with the unchanged JSON and idempotency key.

### Start

> CAMP takes about **8–10 minutes**. We will first confirm the organization, assessment scope, industry, and your role perspective, then ask eight short assessment questions. You’ll receive your **CAMP Stage, CAMP Score /100, five-dimension analysis, biggest bottleneck, top 3 actions for the next 90 days, and practical projects to start now**. If you submit to **CAMP Bench**, you will also receive a private comparison showing your overall position, score distribution, five-dimension gaps, and industry position when the anonymous industry cohort is large enough.

The normal interview has **13 cards: five setup cards and eight assessment cards**. The first card must ask for the company/organization name and country. The next cards must confirm scope and scope label, industry and segment, assessed headcount and function, and respondent perspective. **Never silently infer or skip the profile, even when the organization seems obvious.**

Show `Progress n/13` and a compact visual bar on every card. A conditional follow-up stays on the same number. Use the host application's native clickable choice control for every closed question when it is available. Otherwise show compact A/B/C/D/E/F choices. Never require a long typed response to answer a closed question. Ask one question card at a time; a setup card may contain at most two tightly related fields.

Use everyday language in questions, choices, follow-ups, and reports, even for executives. Say “used regularly in real work” instead of “production level”; “someone checks the results” instead of “eval”; “fewer transfers between teams” instead of “handoff redesign”. Keep technical codes inside the submission JSON only. Never require technical background to select an answer.

Use the participant-facing wording in `references/QUESTION_GUIDE.md`. Each assessment card must contain: a natural-language question, one short sentence explaining why it matters, the choices, and only when useful a brief example. Do not add decorative or unverified quotations.

### Required profile — cards 1–5

- **P0 Company / organization name** — ask the real name. Explain that it is used only for same-company matching if the user later submits to CAMP Bench; do not persist it before submission consent.
- **P1 Scope** — A Entire company / B Business unit-divison / C Team-department / D New AI-native organization
- **P2 Country** — short answer
- **P3 Industry** — Manufacturing / Finance / IT-SaaS / Retail-Commerce / Professional Services / Healthcare-Bio / Public-Education / Media-Content / Construction-Energy / Other
- **P3b Industry segment** — short answer
- **P4 Assessed headcount** — 1–10 / 11–50 / 51–200 / 201–1,000 / 1,001–5,000 / 5,000+
- **P5 Function** — Company-wide / Strategy / R&D / Software-IT / Data-AI-DX / Sales-Marketing / SCM-Manufacturing / Finance-HR-Legal / Customer Service / Other
- **P6 Team/business-unit label** — only when scope is below company level
- **P7 Respondent perspective** — New joiner-early career (0–2 years) / Junior-practitioner (3–7 years) / Senior-expert (8+ years) / Manager-team leader / Executive-C-level / Other-prefer not

Do not collect personal name or email by default. These profile fields must be complete before Q1. If information is known from earlier context or supplied documents, present it for confirmation instead of silently assuming it.

### Assessment cards 6–13

Before Q1 say: **“From here on, answer only for the scope you just confirmed.”** Use the natural participant-facing copy and background notes in `references/QUESTION_GUIDE.md`; the compact definitions below are scoring anchors, not the preferred on-screen wording.

**Q1 AI Access** — share of the assessed population repeatedly using approved AI for work: A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+

**Q2 AI Delegation** — A Search-Q&A-summary / B Drafts-partial tasks / C Real work / D Repeated end-to-end workflows / E Agent-first is normal

**Q3 Enterprise Connection** — A External only / B Files-docs-RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + write + triggers-actions

**Q4 Knowledge Compounding** — A Disappears after sessions / B Personal notes-prompts / C Shared prompt-skill repository / D Owner-version-eval-distribution / E Session decisions and outcome knowledge systematically improve future agents

**Q5 Role Transformation** — A None / B Productivity inside current roles / C Adjacent work / D Handoffs and role boundaries shrink / E AI-first roles, R&R, organization or workforce allocation are redesigned

**Q6 AI Operations** — A Little visibility / B Some usage-cost / C User-agent-model usage-cost / D End-to-end trace + quality eval / E Trace + cost + quality + runtime security-policy controls

**Q7 Sovereign AI** — A External API / B Multi-model portfolio-routing / C Private-local-open-weight-own GPU / D Post-training / E Foundation model

**Q8 Evidence basis** — A Anecdotal: one user-demo-pilot / B Repeated: recurring production case used by several people or a core team / C Operationalized: owner-process-metrics-production / D Institutionalized: default way of working across the assessed scope

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

Do not raise Stage from one power user, showcase demo, isolated pilot, or future plan.

Separate **capability existence** from **adoption coverage**. One representative production case in a strategically important or core organization can establish that an advanced capability exists when it is recurring, has a responsible owner, and is used by several people in real work. It does not establish company-wide adoption. Score the capability in the relevant question, measure coverage separately in Q1, and describe this distinction explicitly in the report. Do not downgrade a real core production case merely because rollout is incomplete.

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

Prefer a registered `submitCampAssessment` Action after consent and use `getCampReport` for results. See `references/NATIVE_SUBMISSION.md` and `references/TRANSPORTS.md`. A tool name in these instructions does not mean it is installed. If no callable native transport is present, do not repeatedly run Python or shell POST attempts: state that the current environment has no permitted transport and provide the exact browser handoff. Respect platform confirmations.

After the standalone report, ask whether the user wants to submit the assessment to CAMP Bench. State the concrete benefit before asking for consent:

> If you submit, CAMP Bench will return a private report showing whether your organization is ahead of, in line with, or behind the overall benchmark. It includes your percentile, the overall score distribution, comparison across all five dimensions, and the largest gap with a recommended action. When at least 10 anonymous organizations are available in your industry cohort, it also includes the industry percentile and distribution. Your company may be named in your own report; every other company remains anonymous.

The real company name is used privately to deduplicate and match the participant's own organization. The participant may see their own company by name; **other companies are always anonymous**.

Benchmark rules:
- aggregate multiple respondents so one company counts once in cross-company ranking
- if cohort N < 10, broaden the cohort or report insufficient sample size
- `eligible` counts toward official percentiles; `provisional` only preliminary analysis; `reference_only` never ranking
- never expose named competitor scores from confidential submissions

If the connected private CAMP Bench store is available and the user agrees, save a new assessment without overwriting history. If it is unavailable, do **not** claim submission succeeded; prepare a structured private submission package instead. Never direct users to post real company data in a public GitHub issue.

If a registered `submitCampAssessment` Action is available, use it after consent instead of running Python; retrieve results with `getCampReport`. See `references/NATIVE_SUBMISSION.md`. Do not assume an Action is installed merely because this skill mentions it. Respect the platform's confirmation steps. Otherwise use the CLI sequence below.

Use this submission sequence exactly:

1. Deliver the complete standalone report first.
2. Ask whether the participant wants to join CAMP Bench. Do not assume consent.
3. Run a completeness gate before asking for consent. Confirm that `company_name`, `country`, `industry`, `industry_segment`, `scope`, `headcount_band`, `function`, `respondent_role`, Stage/Score, all five dimensions, AI Operations, Sovereign AI, evidence level, and confidence are present. If anything is missing, ask only for the missing fields in one compact **Submission readiness** card. Never construct or send a partial submission.
4. Summarize the fields to be sent: real company name, optional scope label, organization profile, respondent role category, Stage/Score, five dimensions, supporting capabilities, evidence level/confidence, and optional evidence summary. State that personal name/email and raw documents are excluded.
5. Ask for explicit confirmation to privately store those fields and use anonymized/aggregate results for benchmarking.
6. Only after confirmation, create the JSON under `private-submissions/`. The submit command validates it before sending; do not add a redundant validation-only run to the participant's wait.
7. Submit through the configured endpoint with the fast receipt-first mode: `--submit --yes --no-wait --language en` for an English interaction or `--submit --yes --no-wait --language ko` for a Korean interaction. A valid `receipt_id` means the submission succeeded. Immediately show the receipt and returned human-readable `report_url`; do not wait silently for report generation.
8. Treat submission acceptance and report readiness as separate states. Retrieve the report with `--status <receipt_id>` after a short interval. When ready, present the overall percentile/median position, overall score distribution, industry result or sample-size notice, five-dimension comparison, and priority gap in the interaction language. Keep `status_url` as the JSON/API endpoint. Do not rebuild the JSON, re-ask consent, or resubmit while polling.
9. If DNS/network restrictions block sending, do not stop at “NOT SUBMITTED”. In the same response provide the downloadable original JSON and [Submit in your browser](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=en): “Download this file → open the page, choose the file and submit.” If file attachment is unavailable, provide the exact JSON privately for the page's paste option. No GitHub account, terminal, token, or installation is required for the public service. Use the client's bounded retry: at most three total attempts for temporary DNS/connection errors and HTTP 408/502/503/504, with 2 then 4 seconds between attempts. Keep the exact payload, destination, and idempotency key; do not ask for consent again for these approved attempts. Stop immediately after a verified receipt. Do not retry validation errors, permission denials, certificate failures, or malformed receipts. Do not restart the retry loop manually or change environments to evade network restrictions. A known DNS failure before sending means NOT SUBMITTED; a timeout or invalid response means SUBMISSION UNCONFIRMED because the server may have saved it. Reuse the exact file and idempotency key. Only a matching receipt confirms acceptance. If an endpoint override is in use, do not redirect its data to the official service automatically.

Never include personal respondent name, email, phone, employee ID, credentials, or raw confidential documents in the submission package. Never retry a failed request blindly; preserve the idempotency key and surface the failure.

---

## 한국어

CAMP는 AI 투자액이나 AI 프로젝트 개수가 아니라 **현재 반복적으로 작동하는 업무방식**을 진단합니다. 상세 기준은 `references/STAGES.md`, `references/PLAYBOOK.md`, `references/QUESTION_GUIDE.md`, `references/REPORT_TEMPLATE.md`, `references/BENCHMARK.md`, `references/SUBMISSION.md`를 사용합니다. Interview Mode에서는 첫 질문 전에 `references/QUESTION_GUIDE.md`를 읽고 따릅니다.

**Interview Mode**에서는 아래 질문을 진행합니다. **Evidence Mode**에서는 전략자료, Architecture, 과제, Usage Data, 운영자료를 먼저 읽고 확인되지 않은 부분만 질문합니다.

### 실행과 제출 경로

지원하는 방법은 두 가지입니다.

1. **로컬 경로:** 사용자의 PC나 VM에서 CAMP Repository를 실행할 수 있으면 로컬 CLI로 진단 결과를 확인하고, 제출 동의를 받은 뒤 같은 환경에서 전송합니다. `receipt_id`가 반환되어야 접수 성공입니다.
2. **클라우드 대화 경로:** ChatGPT, Claude, Gemini, M365 Copilot 같은 호스팅 대화나 Sandbox에서는 대화를 진행하고 정확한 Private JSON 파일을 만듭니다. CAMP 전용 Connector가 실제로 연결되어 있으면 그것을 사용합니다. 연결되어 있지 않거나 외부 전송이 막히면 Python이나 Shell 명령을 반복하지 않습니다. 원본 JSON을 다운로드하게 한 뒤 공식 브라우저 제출 페이지에서 파일을 선택하고, 내용을 확인한 뒤 제출하도록 안내합니다. GitHub 계정은 필요 없습니다.

Repository 주소는 실행 지침을 제공할 뿐 인터넷 전송 권한을 만들지 않습니다. 유효한 `receipt_id`가 없으면 제출 성공이라고 말하지 않습니다. DNS 또는 외부 Network 오류가 발생하면 원본 JSON과 중복 방지 키를 그대로 유지한 채 브라우저 제출로 전환합니다.

### 시작

> CAMP 진단은 약 **8–10분** 걸립니다. 먼저 회사·진단 범위·업종·응답자 관점을 확인하고, 이어서 8개의 짧은 진단 질문을 드립니다. 완료하면 **CAMP Stage, CAMP Score /100, 5개 영역 분석, 가장 큰 병목, 향후 90일 Top 3 실행과제, 바로 시도할 과제**를 받을 수 있습니다. **CAMP Bench**에 제출하면 전체 대비 위치, 점수 분포, 5개 영역의 격차와 익명 동종업계 표본이 충분할 때 업종 내 위치까지 담은 비공개 비교 리포트도 받을 수 있습니다.

기본 인터뷰는 **조직 정보 5개 카드 + 진단 질문 8개 카드, 총 13개**입니다. 첫 카드는 반드시 회사·조직명과 국가를 묻습니다. 이어서 진단 범위와 하위 조직명, 업종과 세부 분야, 진단 대상 인원과 기능, 응답자 관점을 확인합니다. **조직을 알고 있는 것처럼 보여도 프로필을 조용히 추정하거나 건너뛰지 않습니다.**

모든 카드에 `진행 n/13`과 짧은 막대를 표시합니다. 조건부 추가 질문은 같은 번호를 유지합니다. 실행 환경이 지원하면 모든 객관식 질문에 기본 클릭형 선택지를 사용합니다. 지원하지 않으면 짧은 A/B/C/D/E/F 선택지를 보여줍니다. 객관식 답변을 긴 문장으로 입력하게 하지 않습니다. 한 번에 질문 카드 하나만 보여주며, 준비 카드에는 서로 밀접한 항목을 최대 두 개까지만 묶을 수 있습니다.

질문·선택지·추가 설명·리포트는 기술 배경이 없는 사람도 바로 이해할 일상 언어로 씁니다. “Production 수준”은 “실제 업무에서 계속 사용”, “Eval”은 “결과 확인”, “Handoff 재설계”는 “팀 사이에 일을 넘기는 단계 줄이기”로 풀어 씁니다. 임원에게도 같은 원칙을 적용하며, 제출 JSON의 내부 코드는 대화에 그대로 보여주지 않습니다.

참여자에게 보여줄 질문은 `references/QUESTION_GUIDE.md`의 자연스러운 문구를 사용합니다. 각 진단 카드에는 질문, 왜 묻는지 한 문장, 선택지를 포함하고, 이해에 도움이 될 때만 짧은 사례를 덧붙입니다. 장식용 또는 출처가 확인되지 않은 인용문은 사용하지 않습니다.

### 필수 조직 정보 — 1~5번 카드

- **P0 실제 회사/조직명** — 실제 이름을 묻되 CAMP Bench 제출에 동의할 경우 같은 회사 응답을 연결하기 위해 Private에서만 사용한다고 설명. 제출 동의 전에는 영구 저장하지 않음
- **P1 범위** — 회사 전체 / 사업부·본부 / 팀·부서 / 신설 AI-native 조직
- **P2 국가**
- **P3 업종** — 제조 / 금융 / IT-SaaS / 유통-Commerce / 전문서비스 / Healthcare-Bio / 공공-교육 / Media-Content / 건설-Energy / 기타
- **P3b Industry Segment**
- **P4 진단 대상 인원** — 1–10 / 11–50 / 51–200 / 201–1,000 / 1,001–5,000 / 5,000+
- **P5 Function** — 전사 / 전략 / R&D / Software-IT / Data-AI-DX / Sales-Marketing / SCM-생산 / Finance-HR-Legal / CS / 기타
- **P6 팀/사업부명** — 회사 전체가 아닌 경우만
- **P7 응답자 관점** — 신입·초기 경력(0–2년) / 주니어·실무자(3–7년) / 시니어·전문가(8년 이상) / 매니저·팀장 / 임원·경영진 / 기타·응답하지 않음

개인 이름이나 이메일은 기본적으로 수집하지 않습니다. 이 프로필은 Q1 전에 모두 확인해야 합니다. 앞선 대화나 자료에서 알 수 있는 값도 조용히 가정하지 말고 참여자에게 확인받습니다.

### 진단 질문 — 6~13번 카드

Q1 전에 **“이제부터는 방금 확정한 범위만 생각하고 답해주세요.”**라고 안내합니다. 아래 짧은 정의는 채점 기준이며, 화면에는 `references/QUESTION_GUIDE.md`의 자연스러운 질문과 배경설명을 사용합니다.

**Q1 AI Access** — 반복적으로 업무 AI를 쓰는 비율: A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+

**Q2 AI Delegation** — A 검색-Q&A-요약 / B 초안·부분업무 / C 실제업무 / D 반복 End-to-End Workflow / E Agent-first가 기본

**Q3 Enterprise Connection** — A 외부지식만 / B File-Document-RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + Write + Trigger-Action

**Q4 Knowledge Compounding** — A Session 후 사라짐 / B 개인 Prompt-Note / C 공용 Prompt-Skill / D Owner-Version-Eval-배포 / E Session 판단과 Outcome Knowledge가 다음 Agent를 향상

**Q5 Role Transformation** — A 없음 / B 기존 Role 내부 생산성 / C 인접업무 / D Handoff·직무경계 감소 / E AI-first Role·R&R·조직 재설계

**Q6 AI Operations** — A 거의 안 보임 / B Usage-Cost 일부 / C User-Agent-Model별 Usage-Cost / D Trace + Quality Eval / E Trace + Cost + Quality + Runtime Security

**Q7 Sovereign AI** — A 외부 API / B Multi-model / C Private-Local-Open-weight / D Post-training / E Foundation Model

**Q8 실제 근거** — A 한 명·Demo·Pilot / B 여러 사람이 쓰는 반복 운영사례 또는 핵심 팀의 대표사례 / C 담당자·운영절차·측정지표가 있는 실제 운영 / D 진단 범위 전체의 기본 업무방식

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

Power User 한 명, 보여주기용 Demo, 단발성 Pilot, 미래 계획만으로 Stage를 올리지 않습니다.

**역량의 존재**와 **보급 범위**를 분리합니다. 전략적으로 중요하거나 핵심 조직이 주도하는 대표 운영사례 하나라도, 반복적으로 실제 업무에 쓰이고 담당자가 있으며 여러 사람이 사용한다면 높은 역량이 존재한다는 근거가 될 수 있습니다. 그러나 이것이 전사 보급을 뜻하지는 않습니다. 해당 질문에서는 역량을 평가하고, 보급 범위는 Q1에서 따로 평가하며, Report에도 둘을 구분해 씁니다. 전사 확산이 덜 됐다는 이유만으로 실제 핵심 운영사례의 역량을 낮추지 않습니다.

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

등록된 `submitCampAssessment` Action이 있으면 동의 후 Python 대신 호출하고 `getCampReport`로 결과를 조회합니다. `references/NATIVE_SUBMISSION.md`와 `references/TRANSPORTS.md`를 참고합니다. 지침에 이름이 있다고 실제 도구가 연결된 것으로 가정하지 않습니다. 실제 호출 가능한 연결이 없으면 Python·shell POST를 반복하지 말고, 현재 환경에 전송 권한이 없다고 알린 뒤 정확한 브라우저 제출 경로를 제공합니다. 플랫폼 확인 절차를 따릅니다.

Standalone Report 이후 CAMP Bench 제출 여부를 묻습니다. 동의를 묻기 전에 다음과 같이 구체적인 보상을 설명합니다.

> 제출하면 귀사가 전체 Benchmark보다 앞서는지, 비슷한지, 뒤처지는지를 보여주는 Private Report를 받습니다. Percentile, 전체 점수 분포, 5개 Dimension 비교, 가장 부족한 영역과 권장 Action을 제공합니다. 같은 업종의 익명 조직이 10개 이상이면 Industry Percentile과 분포도 함께 제공합니다. 본인의 Report에는 자기 회사명을 표시할 수 있지만 다른 회사는 모두 익명입니다.

실제 회사명은 Private에서 같은 회사 응답을 연결하고 중복 제거하는 데만 사용합니다. 참여자는 자기 회사를 실명으로 볼 수 있지만 **다른 회사는 모두 익명화**됩니다.

공식 Benchmark는 한 회사를 Organization-level Aggregate로 한 번만 반영합니다. Cohort N < 10이면 범위를 넓히거나 표본 부족으로 표시합니다. `eligible`만 정식 Percentile에 사용하며 `provisional`은 Preliminary, `reference_only`는 Ranking에서 제외합니다.

Private CAMP Bench Store가 연결되어 있고 사용자가 동의하면 새 Assessment를 저장하되 과거 이력을 덮어쓰지 않습니다. Store에 접근할 수 없다면 제출됐다고 말하지 말고 Private Submission Package를 생성합니다. 실제 회사 데이터를 Public GitHub Issue에 올리도록 안내하지 않습니다.

다음 Submission Sequence를 반드시 따릅니다.

1. 먼저 완전한 Standalone Report를 제공합니다.
2. 참여자에게 CAMP Bench 참여 여부를 묻습니다. 동의를 추정하지 않습니다.
3. 동의를 묻기 전에 제출 준비 검사를 수행합니다. `company_name`, `country`, `industry`, `industry_segment`, `scope`, `headcount_band`, `function`, `respondent_role`, Stage/Score, 5개 영역, AI Operations, Sovereign AI, 실제 근거 수준, Confidence가 모두 있는지 확인합니다. 빠진 값이 있으면 하나의 짧은 **제출 준비** 카드에서 누락 항목만 묻습니다. 불완전한 JSON을 만들거나 보내지 않습니다.
4. 실제 전송 항목을 요약합니다: 실제 회사명, 선택적 하위 조직명, 조직 Profile, 응답자 역할 범주, Stage/Score, 5개 영역, Supporting Capability, 실제 근거 수준/Confidence, 선택적 Evidence Summary. 개인 이름·이메일과 원문 자료는 제외된다고 알립니다.
5. 비공개 저장과 익명·집계 Benchmark 사용에 대해 명시적으로 다시 확인합니다.
6. 확인 후에만 `private-submissions/` 아래 JSON을 만듭니다. Submit 명령이 전송 전에 자동 검증하므로 참여자를 기다리게 하는 별도의 중복 검증은 실행하지 않습니다.
7. 설정된 Endpoint에 빠른 Receipt 우선 방식으로 제출합니다. 한국어 Interaction은 `--submit --yes --no-wait --language ko`, 영어 Interaction은 `--submit --yes --no-wait --language en`을 사용합니다. 유효한 `receipt_id`가 오면 제출은 성공입니다. Receipt와 사람이 읽는 `report_url`을 즉시 보여주고, Report 생성 중에 말없이 기다리지 않습니다.
8. **제출 접수**와 **리포트 준비**를 별도 상태로 다룹니다. 잠시 뒤 `--status <receipt_id>`로 조회합니다. 준비되면 대화 언어로 전체 Percentile/Median 위치, 점수 분포, 업종 결과 또는 표본 부족 안내, 5개 영역 비교, Priority Gap을 보여줍니다. `status_url`은 JSON/API 주소로 구분합니다. 조회 중 JSON을 다시 만들거나 동의를 다시 묻거나 재제출하지 않습니다.
9. DNS나 네트워크 제한으로 전송이 막히면 “미제출” 안내로 끝내지 않습니다. 같은 답변에 원본 JSON 다운로드와 [브라우저에서 제출하기](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=ko) 링크를 함께 제공합니다. “파일 내려받기 → 위 페이지에서 파일을 선택하고 제출” 두 단계로 안내합니다. 파일 첨부가 불가능하면 해당 페이지에 붙여넣을 정확한 JSON을 비공개 대화에서 제공합니다. 공개 제출 서비스는 GitHub 계정·터미널·토큰·설치가 필요 없습니다. 일시적 DNS·연결 오류와 HTTP 408/502/503/504에는 클라이언트가 총 3번까지 시도하며, 재시도 전에 2초·4초 기다립니다. 승인받은 동일 파일·목적지·중복 방지 키를 유지하고 동의를 다시 묻지 않습니다. 정상 접수번호가 오면 즉시 멈춥니다. 입력값 오류·권한 거부·인증서 문제·잘못된 접수번호에는 자동 재시도하지 않습니다. 3번 실패 후에는 자동 반복을 다시 시작하지 말고 웹 제출을 안내합니다. 환경 제한을 우회하지 않습니다. 전송 전 DNS 실패가 확인되면 미제출, 시간 초과나 응답 오류라면 저장됐을 수도 있으므로 접수 확인 불가라고 구분합니다. 파일과 중복 방지 키는 그대로 유지하며, 일치하는 접수번호가 있어야 접수 성공입니다. 별도 제출 주소를 사용 중이면 공식 서비스로 임의 전환하지 않습니다.

개인 응답자 이름, 이메일, 전화번호, 사번, Credential, Raw Confidential Document를 Submission Package에 넣지 않습니다. 실패한 요청을 무조건 재시도하지 않으며 Idempotency Key를 유지하고 실패를 명확히 알립니다.
