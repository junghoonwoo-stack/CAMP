---
name: camp
description: CAMP (Company Agent Maturity Profile) assesses how agent-native an organization is using a short interview or supplied evidence. It returns a CAMP Stage, CAMP Score, biggest bottleneck, 90-day actions, recommended projects, and optional benchmark comparison.
---

# CAMP — Company Agent Maturity Profile

## English

CAMP is a ~10-minute assessment.

Start with:

> CAMP takes about **10 minutes**. I’ll ask a few multiple-choice or short questions. You’ll receive your **CAMP Stage, CAMP Score /100, biggest bottleneck, top 3 actions for the next 90 days, recommended projects, and a short report**. If you provide files, I’ll read them first and skip questions already answered.

Use clickable choices when available. Otherwise use A/B/C/D/E. Ask one question at a time.

If several people from one organization participate, use the same anonymous **Organization Group ID**, one **Scope ID**, and different **Respondent IDs**. Never require company or personal names.

### Profile

**P1. Scope** — A Company / B Business unit / C Team / D New AI-native organization  
**P2. Country** — short answer  
**P3. Industry** — A Manufacturing / B Finance / C IT-SaaS / D Retail / E Professional services / F Healthcare / G Public-Education / H Media / I Construction-Energy / J Other  
**P3b. Broad industry segment** — ask only for benchmark grouping; never ask for a company name  
**P4. Headcount** — A 1–10 / B 11–50 / C 51–200 / D 201–1,000 / E 1,001–5,000 / F 5,000+  
**P5. Function** — A Company-wide / B Strategy / C R&D / D Software-IT / E Data-AI-DX / F Sales-Marketing / G SCM-Manufacturing / H Finance-HR-Legal / I Customer Service / J Other  
**P6. Multiple respondents?** — A No / B Yes / C Not sure

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

Stage:
- 0 No AI
- 1 AI Access
- 2 AI Workforce
- 3 Connected AI
- 4 Compounding AI
- 5 AI-Native Company

Do not raise a Stage from one user, demo, pilot, or future plan.

### Agent Test

> **Agent = Model + Context + Harness**

1. Does it improve as the model improves?
2. Is development helping AI work better through context, tools, skills, permissions, or runtime?

If both are No, it is usually **IT built faster with AI**, not core Agent Transformation.

### Report

Return:
- organization profile
- CAMP Stage + Confidence
- CAMP Score + five dimensions
- one-line diagnosis
- strengths
- biggest bottleneck
- next 90 days: Top 3
- recommended projects
- Stop Doing
- AI Operations
- Sovereign AI

For multiple respondents, also show organization mean/median, spread, and largest disagreements.

### Benchmark opt-in

After the report, ask:

> Would you like to share this anonymized result with the CAMP Benchmark? If you do, CAMP can compare you with **all organizations, your industry, and an anonymous peer group** when enough data exists. Company names are not collected or shown.

- A Yes
- B No
- C Show exactly what will be shared

If the user opts in, use anonymous IDs only. Public comparison data may show country, industry, broad industry segment, size, scope, function, and scores. Never show company names or named competitors.

Benchmark outputs:
- Overall percentile
- Industry percentile
- Peer Group percentile
- Dimension comparison

Use organization-level aggregation for cross-company ranking. If a cohort has fewer than 10 organizations, broaden the cohort or say sample size is insufficient.

---

## 한국어

CAMP는 약 10분짜리 조직 AX/Agent-native 진단입니다.

다음과 같이 시작합니다.

> CAMP 진단은 약 **10분** 정도 걸립니다. 몇 가지 객관식/짧은 질문에 답해주시면 **CAMP Stage, CAMP Score /100, 가장 큰 병목, 향후 90일 Top 3 Action, 추천 과제, 짧은 Report**를 드립니다. 자료가 있으면 먼저 읽고 이미 확인된 질문은 건너뜁니다.

가능하면 클릭형 선택지를 쓰고, 아니면 A/B/C/D/E로 답하게 합니다. 한 번에 한 질문만 하고 존댓말을 사용합니다.

같은 조직에서 여러 명이 참여하면 같은 익명 **Organization Group ID**, 같은 **Scope ID**, 서로 다른 **Respondent ID**를 사용합니다. 회사명과 개인 이름은 요구하지 않습니다.

### 조직 정보

**P1. 범위** — A 회사 전체 / B 사업부 / C 팀 / D 신설 AI-native 조직  
**P2. 국가** — 짧게 입력  
**P3. 업종** — A 제조 / B 금융 / C IT-SaaS / D 유통 / E 전문서비스 / F 헬스케어 / G 공공-교육 / H 미디어 / I 건설-에너지 / J 기타  
**P3b. 넓은 Industry Segment** — Benchmark 비교용으로만 질문하며 회사명은 묻지 않음  
**P4. 인원** — A 1–10 / B 11–50 / C 51–200 / D 201–1,000 / E 1,001–5,000 / F 5,000+  
**P5. Function** — A 전사 / B 전략 / C R&D / D Software-IT / E Data-AI-DX / F 영업-마케팅 / G SCM-생산 / H Finance-HR-Legal / I Customer Service / J 기타  
**P6. 같은 조직에서 여러 명이 응답하나요?** — A 아니요 / B 예 / C 아직 모름

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

Stage:
- 0 No AI
- 1 AI Access
- 2 AI Workforce
- 3 Connected AI
- 4 Compounding AI
- 5 AI-Native Company

한 사람, Demo, Pilot, 향후 계획만으로 Stage를 올리지 않습니다.

### Agent Test

> **Agent = Model + Context + Harness**

1. 모델이 좋아질수록 시스템도 좋아지는가?
2. Context, Tool, Skill, Permission, Runtime을 통해 AI가 더 잘 일하게 하는가?

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**이며 핵심 Agent Transformation과 구분합니다.

### 최종 Report

다음을 제공합니다.
- 조직 정보
- CAMP Stage + Confidence
- CAMP Score + 5개 영역
- 한 줄 진단
- 강점
- 가장 큰 병목
- 다음 90일 Top 3
- 추천 과제
- Stop Doing
- AI Operations
- Sovereign AI

여러 응답자가 있으면 조직 평균/중앙값, 분산, 인식 차이가 큰 영역도 보여줍니다.

### Benchmark 공유

Report 이후 묻습니다.

> 익명화된 CAMP 결과를 Benchmark에 공유하시겠습니까? 공유하면 표본이 충분할 때 **전체 조직 대비, 업종 대비, 익명 Peer Group 대비** 위치를 알려드립니다. 회사명은 수집하거나 공개하지 않습니다.

- A 예
- B 아니요
- C 공유되는 정보를 먼저 보여주세요

동의하면 익명 ID만 사용합니다. 공개 비교 데이터에는 국가, 업종, 넓은 Industry Segment, 규모, 범위, Function, 점수 등이 포함될 수 있습니다. 회사명이나 특정 경쟁사 이름은 공개하지 않습니다.

Benchmark 결과:
- 전체 Percentile
- Industry Percentile
- Peer Group Percentile
- 영역별 비교

기업 간 비교는 조직 단위 집계값을 사용합니다. Cohort가 10개 조직 미만이면 더 넓은 그룹으로 비교하거나 표본 부족으로 표시합니다.
