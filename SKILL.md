---
name: camp
description: CAMP (Company Agent Maturity Profile) assesses how agent-native an organization is using a short interview or supplied evidence. It returns a CAMP Stage, CAMP Score, biggest bottleneck, 90-day actions, recommended projects, and optional benchmark comparison.
---

# CAMP — Company Agent Maturity Profile

Created by **Junghoon Woo**

CAMP is a ~10-minute assessment of how agent-native an organization is and what it should do next.

Start with:

> CAMP takes about **10 minutes**. I’ll ask a few multiple-choice or short questions. You’ll receive your **CAMP Stage, CAMP Score /100, biggest bottleneck, top 3 actions for the next 90 days, recommended projects, and a short report**. If you provide files, I’ll read them first and skip questions already answered.

Use clickable choices when available. Otherwise use A/B/C/D/E. Ask one question at a time.

If several people from one organization participate, use the same anonymous **Organization Group ID**, a **Scope ID**, and different **Respondent IDs**. Never require company or personal names.

## Profile

**P1. Scope** — A Company / B Business unit / C Team / D New AI-native organization  
**P2. Country** — short answer  
**P3. Industry** — A Manufacturing / B Finance / C IT-SaaS / D Retail / E Professional services / F Healthcare / G Public-Education / H Media / I Construction-Energy / J Other  
**P4. Headcount** — A 1–10 / B 11–50 / C 51–200 / D 201–1,000 / E 1,001–5,000 / F 5,000+  
**P5. Function** — A Company-wide / B Strategy / C R&D / D Software-IT / E Data-AI-DX / F Sales-Marketing / G SCM-Manufacturing / H Finance-HR-Legal / I Customer Service / J Other  
**P6. Multiple respondents?** — A No / B Yes / C Not sure

## Core questions

**Q1. AI Access — share of people repeatedly using their own AI for work**  
A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+

**Q2. AI Delegation**  
A Search/questions / B Drafts or isolated tasks / C Real work / D Repeated end-to-end work with tools / E Agent-first for most people

**Q3. Enterprise Connection**  
A External knowledge / B Internal files or RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + write + triggers/schedulers

**Q4. Knowledge Compounding**  
A Mostly disappears / B Personal notes / C Shared prompt-skill repository / D Owner-version-eval-distribution / E Sessions systematically produce reusable knowledge

**Q5. Role Transformation**  
A None / B Productivity inside current roles / C Adjacent functions expand / D Handoffs and role boundaries shrink / E Roles and organization are AI-first

**Q6. AI Operations**  
A Little visibility / B Some usage-cost / C User-agent-model usage and cost / D End-to-end trace + quality eval / E Visibility + cost + quality + runtime security

**Q7. Sovereign AI**  
A External API / B Multi-model routing / C Private-local-open model or own GPU serving / D Post-training / E Foundation model

Ask follow-ups only if they change the result: production vs pilot, repeated use, number of teams, write permissions, evaluation, or active AX projects.

If files are provided, extract evidence first and ask only what remains unknown.

## Score and Stage

Q1–Q5: `A/B/C/D/E = 0/5/10/15/20`. Total = 100.  
Q6 and Q7 are supporting capabilities.

Stage requires repeated or operational evidence:
- Stage 0 — No AI
- Stage 1 — AI Access
- Stage 2 — AI Workforce
- Stage 3 — Connected AI
- Stage 4 — Compounding AI
- Stage 5 — AI-Native Company

Do not raise a Stage from one user, demo, pilot, or future plan. A company may skip stages if its real operating model supports it.

## Agent Test

> **Agent = Model + Context + Harness**

For each AX project ask:
1. Does it naturally improve as the model improves?
2. Is it helping AI work better through context, tools, skills, permissions, or runtime?

If both are No, it is usually **IT built faster with AI**, not core Agent Transformation.

## Report

Always return:
- organization profile
- CAMP Stage + Confidence
- CAMP Score and five dimension scores
- one-line diagnosis
- evidence-backed strengths
- biggest bottleneck
- next 90 days: Top 3
- recommended projects
- Stop Doing
- AI Operations
- Sovereign AI

For multiple respondents, also show organization mean/median, score spread, and largest areas of disagreement.

After the report ask separately whether the user wants to opt into the anonymized CAMP Benchmark. Never submit without explicit consent.

---

# CAMP — Company Agent Maturity Profile

Creator: **Junghoon Woo**

CAMP는 약 10분 동안 조직이 얼마나 Agent-native한지, 다음에 무엇을 해야 하는지 진단합니다.

다음 안내로 시작합니다.

> CAMP 진단은 약 **10분** 정도 걸립니다. 몇 가지 객관식/짧은 질문에 답해주시면 **CAMP Stage, CAMP Score /100, 가장 큰 병목, 향후 90일 Top 3 Action, 추천 과제, 짧은 Report**를 드립니다. 자료가 있으면 먼저 읽고 이미 확인된 질문은 건너뜁니다.

가능하면 클릭형 선택지를 쓰고, 아니면 A/B/C/D/E로 답하게 합니다. 한 번에 한 질문만 하고 존댓말을 사용합니다.

같은 조직에서 여러 명이 참여하면 같은 익명 **Organization Group ID**, **Scope ID**, 서로 다른 **Respondent ID**를 사용합니다. 회사명과 개인 이름은 요구하지 않습니다.

## 조직 정보

**P1. 범위** — A 회사 전체 / B 사업부 / C 팀 / D 신설 AI-native 조직  
**P2. 국가** — 짧게 입력  
**P3. 업종** — A 제조 / B 금융 / C IT-SaaS / D 유통 / E 전문서비스 / F 헬스케어 / G 공공-교육 / H 미디어 / I 건설-에너지 / J 기타  
**P4. 인원** — A 1–10 / B 11–50 / C 51–200 / D 201–1,000 / E 1,001–5,000 / F 5,000+  
**P5. Function** — A 전사 / B 전략 / C R&D / D Software-IT / E Data-AI-DX / F 영업-마케팅 / G SCM-생산 / H Finance-HR-Legal / I Customer Service / J 기타  
**P6. 같은 조직에서 여러 명이 응답하나요?** — A 아니요 / B 예 / C 아직 모름

## 핵심 질문

**Q1. AI Access — 자기 전용 AI를 반복 사용하는 비율**  
A <5% / B 5–20% / C 21–50% / D 51–80% / E 81%+

**Q2. AI Delegation**  
A 검색-질문 / B 초안-일부 Task / C 실제 업무 / D 여러 Tool을 활용한 반복 End-to-End 업무 / E 대부분 Agent-first

**Q3. Enterprise Connection**  
A 외부지식 / B 내부파일-RAG / C M365-Google-Slack-Drive / D MCP-API-DB-ERP-PLM-CRM / E Read + Write + Trigger-Scheduler

**Q4. Knowledge Compounding**  
A 거의 사라짐 / B 개인 저장 / C 공용 Prompt-Skill 저장소 / D Owner-Version-Eval-배포 / E Session 지식이 다른 Agent에 체계적으로 재사용

**Q5. Role Transformation**  
A 없음 / B 기존 직무 생산성 / C 인접 업무 확장 / D Handoff와 역할경계 감소 / E R&R과 조직을 AI 기준으로 재설계

**Q6. AI Operations**  
A 거의 안 보임 / B Usage-Cost 일부 / C User-Agent-Model별 사용-비용 / D End-to-End Trace + Quality Eval / E Visibility + Cost + Quality + Runtime Security

**Q7. Sovereign AI**  
A 외부 API / B Multi-model Routing / C Private-Local-Open Model 또는 자체 GPU / D Post-training / E Foundation Model

결과가 달라질 때만 추가 질문합니다: 실제 운영인지 Pilot인지, 반복 사용 범위, 팀 수, Write Permission, Eval, 현재 AX 과제 등.

파일이 있으면 Evidence를 먼저 추출하고 모르는 것만 질문합니다.

## 점수와 Stage

Q1–Q5는 `A/B/C/D/E = 0/5/10/15/20`, 총 100점입니다.  
Q6·Q7은 Supporting Capability입니다.

Stage는 반복적·운영화된 상태를 기준으로 합니다.
- Stage 0 — No AI
- Stage 1 — AI Access
- Stage 2 — AI Workforce
- Stage 3 — Connected AI
- Stage 4 — Compounding AI
- Stage 5 — AI-Native Company

한 사람, Demo, Pilot, 향후 계획만으로 Stage를 올리지 않습니다. 실제 Operating Model이 뒷받침하면 Stage를 건너뛸 수 있습니다.

## Agent Test

> **Agent = Model + Context + Harness**

AX 과제마다 묻습니다.
1. 모델이 좋아질수록 시스템도 자연스럽게 좋아지는가?
2. Context, Tool, Skill, Permission, Runtime을 통해 AI가 더 잘 일하게 하는가?

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**이며 핵심 Agent Transformation과 구분합니다.

## 최종 Report

항상 제공합니다.
- 조직 정보
- CAMP Stage + Confidence
- CAMP Score와 5개 영역 점수
- 한 줄 진단
- Evidence 기반 강점
- 가장 큰 병목
- 다음 90일 Top 3
- 추천 과제
- Stop Doing
- AI Operations
- Sovereign AI

여러 응답자가 같은 Organization Group ID를 쓰면 조직 평균/중앙값, 점수 분산, 인식 차이가 가장 큰 영역도 보여줍니다.

Report 이후 익명 CAMP Benchmark 공유 여부를 별도로 묻습니다. 명시적 동의 없이는 제출하지 않습니다.
