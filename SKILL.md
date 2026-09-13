---
name: camp
description: CAMP (Company Agent Maturity Profile) assesses how agent-native an organization is using a short interview or supplied evidence. It returns a CAMP Stage, CAMP Score, dimension analysis, bottleneck, 90-day actions, recommended projects, and optional CAMP Bench comparison.
---

# CAMP — Company Agent Maturity Profile

## English

CAMP is a ~10-minute assessment.

Start with:

> CAMP takes about **10 minutes**. I’ll ask a few multiple-choice or short questions. You’ll receive your **CAMP Stage, CAMP Score /100, five-dimension analysis, biggest bottleneck, top 3 actions for the next 90 days, and practical projects to start now**. If you contribute the result to **CAMP Bench**, you can also receive benchmark comparisons when enough data exists.

Use clickable choices when available. Otherwise use A/B/C/D/E. Ask one question at a time.

### Profile

**P0. Company / organization name** — required for CAMP Bench identity matching. Explain: stored privately; never shown in public benchmark output or the anonymized report.  
**P1. Scope** — A Company / B Business unit / C Team / D New AI-native organization  
**P2. Country** — short answer  
**P3. Industry** — A Manufacturing / B Finance / C IT-SaaS / D Retail / E Professional services / F Healthcare / G Public-Education / H Media / I Construction-Energy / J Other  
**P3b. Broad industry segment** — for peer grouping  
**P4. Headcount** — A 1–10 / B 11–50 / C 51–200 / D 201–1,000 / E 1,001–5,000 / F 5,000+  
**P5. Function** — A Company-wide / B Strategy / C R&D / D Software-IT / E Data-AI-DX / F Sales-Marketing / G SCM-Manufacturing / H Finance-HR-Legal / I Customer Service / J Other  
**P6. Team / business-unit label** — short answer when scope is below company level; keep it private and use an anonymous Scope ID in reports.  
**P7. Multiple respondents?** — A No / B Yes / C Not sure

If the private CAMP Bench store is available, resolve the company name to a stable `org_group_id`. Reuse the same organization ID for all respondents from that company. Never expose the real company name in the report or public benchmark.

If prior assessments from the same company exist, include them in organization-level analysis. Do not invent prior records when the private benchmark store is unavailable.

### Core questions

**Q1. AI Access** — A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+  
**Q2. AI Delegation** — A Questions / B Drafts / C Real work / D Repeated end-to-end work / E Agent-first  
**Q3. Enterprise Connection** — A External only / B Files-RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + write + triggers  
**Q4. Knowledge Compounding** — A Disappears / B Personal notes / C Shared repository / D Owner-version-eval / E Session knowledge reused  
**Q5. Role Transformation** — A None / B Productivity only / C Adjacent work / D Handoffs shrink / E AI-first roles and org  
**Q6. AI Operations** — A Little visibility / B Some usage-cost / C User-agent-model usage-cost / D Trace + eval / E Trace + cost + quality + runtime security  
**Q7. Sovereign AI** — A External API / B Multi-model / C Private-local-open model / D Post-training / E Foundation model

Ask follow-ups only when they may change the result.

### Score and Stage

Q1–Q5: `A/B/C/D/E = 0/5/10/15/20`. Total = 100. Q6–Q7 are supporting capabilities.

- Stage 0 — No AI
- Stage 1 — AI Access
- Stage 2 — AI Workforce
- Stage 3 — Connected AI
- Stage 4 — Compounding AI
- Stage 5 — AI-Native Company

Do not raise a Stage from one user, demo, pilot, or future plan.

### Agent Test

> **Agent = Model + Context + Harness**

1. Does it improve as the model improves?
2. Is development helping AI work better through context, tools, skills, permissions, or runtime?

If both are No, it is usually **IT built faster with AI**, not core Agent Transformation.

### Report

Always return an **anonymized report**. Use `Your organization`, an anonymous Organization Group ID, and anonymous Scope IDs instead of the real company/team name.

Include:
- CAMP Stage + Confidence
- **CAMP Score /100**
- all five dimension scores
- strongest dimensions and why
- weakest dimensions and why
- gaps between dimensions
- one-line diagnosis
- biggest bottleneck
- next 90 days: Top 3
- recommended projects
- Stop Doing
- AI Operations
- Sovereign AI

For multiple respondents from the same company, also show:
- organization mean and median
- score distribution / range
- team or function differences
- dimensions with the largest disagreement
- whether leadership and frontline perceptions diverge, when role metadata supports it

### CAMP Bench — Give to Get

Assessment, Stage, Score, and recommendations are free. **CAMP Bench analysis requires contributing the assessment.**

After the report ask:

> Would you like to contribute this assessment to **CAMP Bench**? Your real company name is stored privately only for identity matching. Benchmark outputs remain anonymized. Contributors can receive **Overall, Industry, Peer Group, and same-company multi-response analysis** when enough data exists.

- A Yes
- B No
- C Show exactly what will be stored and returned

No contribution → no percentile or peer benchmark.

CAMP Bench outputs may include:
- Overall percentile
- Industry percentile
- Peer Group percentile
- benchmark distribution with `Your organization` highlighted
- five-dimension comparison against each cohort
- strengths / weaknesses relative to peers
- prior-period movement
- same-company respondent distribution and team/function differences

Use the narrowest cohort with sufficient N. If N < 10, broaden the cohort or report insufficient sample size.

Never reveal another confidential participant’s company identity or individual score. Named competitor analysis may use only public information or data explicitly authorized for named disclosure.

### Optional AX support / marketplace

Benchmark participation is **not** consent for sales outreach. After all benchmark choices, optionally ask:

> Would you like help improving one of the diagnosed areas?

- A No
- B Yes — show relevant types of AX specialists / partners anonymously
- C Yes — I am open to an introduction

Only option C can authorize identity-based introductions, and separate explicit consent is required before sharing organization identity with any consultant or partner.

---

## 한국어

CAMP는 약 10분짜리 조직 AX / Agent-native 진단입니다.

다음과 같이 시작합니다.

> CAMP 진단은 약 **10분** 정도 걸립니다. 몇 가지 객관식/짧은 질문에 답해주시면 **CAMP Stage, CAMP Score /100, 5개 영역 분석, 가장 큰 병목, 향후 90일 Top 3 Action, 바로 시도할 과제**를 드립니다. 결과를 **CAMP Bench**에 제공하면 표본이 충분할 때 다른 조직과의 비교도 받을 수 있습니다.

가능하면 클릭형 선택지를 쓰고, 아니면 A/B/C/D/E로 답하게 합니다. 한 번에 한 질문만 하고 존댓말을 사용합니다.

### 조직 정보

**P0. 실제 회사 / 조직명** — CAMP Bench에서 동일 회사 응답을 연결하기 위해 사용. 실제 이름은 Private Store에만 저장하며 Public Benchmark와 익명 Report에는 표시하지 않는다고 안내  
**P1. 범위** — A 회사 전체 / B 사업부 / C 팀 / D 신설 AI-native 조직  
**P2. 국가** — 짧게 입력  
**P3. 업종** — A 제조 / B 금융 / C IT-SaaS / D 유통 / E 전문서비스 / F 헬스케어 / G 공공-교육 / H 미디어 / I 건설-에너지 / J 기타  
**P3b. 넓은 Industry Segment** — Peer Group 구성용  
**P4. 인원** — A 1–10 / B 11–50 / C 51–200 / D 201–1,000 / E 1,001–5,000 / F 5,000+  
**P5. Function** — A 전사 / B 전략 / C R&D / D Software-IT / E Data-AI-DX / F 영업-마케팅 / G SCM-생산 / H Finance-HR-Legal / I Customer Service / J 기타  
**P6. 팀 / 사업부명** — 회사 전체가 아닌 경우 짧게 입력. Private Store에서만 사용하고 Report에는 익명 Scope ID 사용  
**P7. 같은 조직에서 여러 명이 응답하나요?** — A 아니요 / B 예 / C 아직 모름

Private CAMP Bench Store에 접근할 수 있으면 실제 회사명을 안정적인 `org_group_id`에 매핑합니다. 같은 회사의 모든 응답자는 같은 Organization Group ID를 사용합니다. 실제 회사명은 Report나 Public Benchmark에 노출하지 않습니다.

같은 회사의 과거 응답이 있으면 함께 분석합니다. Private Benchmark Store에 접근할 수 없는 환경에서는 기존 응답이 있다고 추정하거나 만들어내지 않습니다.

### 핵심 질문

**Q1. AI Access** — A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+  
**Q2. AI Delegation** — A 질문 / B 초안 / C 실제 업무 / D 반복 End-to-End 업무 / E Agent-first  
**Q3. Enterprise Connection** — A 외부만 / B 파일-RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + Write + Trigger  
**Q4. Knowledge Compounding** — A 사라짐 / B 개인 저장 / C 공용 저장소 / D Owner-Version-Eval / E Session 지식 재사용  
**Q5. Role Transformation** — A 없음 / B 생산성만 / C 인접업무 / D Handoff 감소 / E AI-first 역할-조직  
**Q6. AI Operations** — A 거의 안 보임 / B Usage-Cost 일부 / C User-Agent-Model별 사용-비용 / D Trace + Eval / E Trace + Cost + Quality + Runtime Security  
**Q7. Sovereign AI** — A 외부 API / B Multi-model / C Private-Local-Open Model / D Post-training / E Foundation Model

결과가 달라질 때만 추가 질문합니다.

### 점수와 Stage

Q1–Q5는 `A/B/C/D/E = 0/5/10/15/20`, 총 100점입니다. Q6–Q7은 Supporting Capability입니다.

- Stage 0 — No AI
- Stage 1 — AI Access
- Stage 2 — AI Workforce
- Stage 3 — Connected AI
- Stage 4 — Compounding AI
- Stage 5 — AI-Native Company

한 사람, Demo, Pilot, 향후 계획만으로 Stage를 올리지 않습니다.

### Agent Test

> **Agent = Model + Context + Harness**

1. 모델이 좋아질수록 시스템도 좋아지는가?
2. Context, Tool, Skill, Permission, Runtime을 통해 AI가 더 잘 일하게 하는가?

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**이며 핵심 Agent Transformation과 구분합니다.

### 최종 Report

Report는 항상 **익명화**합니다. 실제 회사/팀 이름 대신 `Your organization`, 익명 Organization Group ID, 익명 Scope ID를 사용합니다.

반드시 포함합니다.
- CAMP Stage + Confidence
- **CAMP 총점 /100**
- 5개 영역별 점수
- 가장 강한 영역과 이유
- 가장 약한 영역과 이유
- 영역 간 불균형 / Gap
- 한 줄 진단
- 가장 큰 병목
- 다음 90일 Top 3
- 추천 과제
- Stop Doing
- AI Operations
- Sovereign AI

같은 회사의 여러 응답자가 있으면 추가로 보여줍니다.
- 조직 평균 / 중앙값
- 점수 분포 / 범위
- 팀·Function별 차이
- 응답자 간 의견 차이가 가장 큰 영역
- 역할 정보가 있으면 경영진과 현업의 인식 차이

### CAMP Bench — Give to Get

진단, Stage, Score, 추천 Action은 무료입니다. **CAMP Bench 분석은 자신의 진단 결과를 제공한 경우에만 받을 수 있습니다.**

Report 이후 묻습니다.

> 이 결과를 **CAMP Bench**에 제공하시겠습니까? 실제 회사명은 동일 회사 Matching을 위해 Private Store에만 저장하고 Benchmark 결과는 익명화합니다. 참여하면 표본이 충분할 때 **전체 / 업종 / Peer Group / 같은 회사의 다중 응답 비교**를 받을 수 있습니다.

- A 예
- B 아니요
- C 저장되는 정보와 반환되는 정보를 먼저 보여주세요

**데이터 기여 없음 = Percentile / Peer Benchmark 없음.**

CAMP Bench 결과에는 다음이 포함될 수 있습니다.
- 전체 Percentile
- Industry Percentile
- Peer Group Percentile
- 분포 그래프에서 `Your organization` 위치 표시
- 5개 영역별 Cohort 비교
- Peer 대비 상대적 강점 / 약점
- 과거 대비 변화
- 같은 회사 응답자 분포와 팀·Function 차이

표본이 충분한 범위에서 가장 좁은 Cohort를 사용합니다. N < 10이면 더 넓은 Cohort로 비교하거나 표본 부족으로 표시합니다.

다른 참여기업의 회사명이나 개별 점수는 공개하지 않습니다. 특정 경쟁사 이름을 붙인 분석은 공개정보이거나 해당 조직이 명시적으로 허용한 데이터만 사용합니다.

### 선택형 AX 지원 / Marketplace

Benchmark 참여는 영업 연락에 대한 동의가 아닙니다. 모든 Benchmark 선택이 끝난 뒤 필요하면 별도로 묻습니다.

> 진단에서 발견된 약한 영역을 개선하는 데 외부 도움이 필요하신가요?

- A 아니요
- B 예 — 적합한 AX 전문가/파트너 유형을 익명으로 추천
- C 예 — 실제 소개를 받아볼 의향 있음

C를 선택한 경우에도 실제 회사 identity를 Consultant/Partner에게 전달하기 전 별도 명시적 동의를 받아야 합니다.
