---
name: camp
description: CAMP (Company Agent Maturity Profile) 진단 스킬. 기업/조직의 AX 또는 Agent-Native 수준을 약 10분의 Q&A 또는 제공된 AX 제안서, Agent 문서, RAG/MCP 아키텍처, Skill, 사용로그, 조직자료로 진단한다. 현재 CAMP Stage와 0-100 CAMP Score, 가장 큰 병목, 다음 90일 Top 3 Action, 추천 AX 과제를 도출한다. 사용자가 "우리 회사 AX 수준", "AI Native Company 진단", "Agent maturity", "AX 과제 리뷰", "이게 AI Agent인가", "MCP/RAG를 잘 하고 있는가", "다음 AX 과제는 무엇인가" 등을 묻거나 조직의 AI/AX 관련 파일을 제공하면 사용한다.
---

# CAMP — Company Agent Maturity Profile

한국어: **CAMP — 우리 회사 AX 진단**  
English: **CAMP — Agent-Native Company Assessment**

CAMP는 단순한 점수표가 아니다. 목적은 **현재 위치, 가장 큰 병목, 다음 90일의 Action과 과제**를 명확하게 만드는 것이다.

상세 질문은 `QUESTIONNAIRE.md`, 진단 기준은 `PLAYBOOK.md`, 결과 형식은 `REPORT_TEMPLATE.md`를 참고한다.

## 1. 진단을 시작할 때

반드시 먼저 다음 취지로 안내한다.

> CAMP 진단은 보통 **약 10분** 정도 걸립니다. 몇 가지 객관식/짧은 질문에 답해주시면 현재 조직의 **CAMP Stage와 CAMP Score**, 가장 큰 병목, 다음 90일의 **우선 Action 3개와 추천 AX 과제**를 드립니다. 자료가 있으면 먼저 읽고 이미 확인된 질문은 건너뜁니다.

항상 **존댓말**을 사용한다.

가능한 경우 객관식은 버튼/quick reply/선택형 UI로 제공한다. UI가 지원하지 않으면 `A/B/C/D/E`처럼 한 글자로 답할 수 있게 한다.

## 2. 먼저 조직 Profile을 파악한다

반드시 다음을 파악한다.

- 진단 범위: 회사 전체 / 사업부·본부 / 특정 팀 / 신설 AI-native 조직
- 국가
- 업종
- 진단 대상 인원 구간
- 주요 Function

회사명은 진단에 꼭 필요하지 않으면 묻지 않는다. Benchmark 기본 제출에도 회사명은 포함하지 않는다.

## 3. Agent 정의

> **Agent = Model + Context + Harness**

- Model: GPT, Claude, Gemini, open-weight, 자체 모델 등
- Context: Data, RAG, 문서, 이메일, Slack/Teams, Memory, Session, 과거 의사결정 등
- Harness: Skill/Instruction, Tool, MCP/API, Permission, Scheduler/Trigger, Runtime, Evaluation, Observability 등

### Agent Test

모든 AX 과제에 먼저 두 질문을 적용한다.

1. **AI 모델이 좋아질수록 이 시스템의 업무 수행 능력도 자연스럽게 좋아지는가?**
2. **현재 개발이 AI가 일을 더 잘하도록 Context, Data, Tool, Skill, Permission, Runtime 등을 강화하는가?**

둘 다 No라면 대개 `AI로 더 빨리 만든 기존 IT`다. 가치가 없다는 뜻은 아니지만 Agent Transformation과 구분한다.

## 4. CAMP Stage

Stage는 반드시 순서대로 밟는 교육과정이 아니다. **현재 반복적으로 작동하는 Operating Model**을 평가한다. AI-native startup은 설립 초기부터 높은 Stage가 가능하다.

- **Stage 0 — No AI:** 업무용 AI 접근 자체가 거의 없음
- **Stage 1 — AI Access:** AI가 일부 사용자/기능에만 제공됨. 핵심은 1인 1 AI
- **Stage 2 — AI Workforce:** 개인이 General Agent에게 실제 업무를 맡김
- **Stage 3 — Connected AI:** Agent가 사내 RAG, Data, MCP/API, 업무시스템과 연결됨
- **Stage 4 — Compounding AI:** Skill, Session, Context가 조직 자산으로 축적·재사용됨
- **Stage 5 — AI-Native Company:** 역할·Handoff·조직 구조가 AI를 전제로 재설계됨

Stage는 **단일 Demo가 아니라 반복·운영화된 Evidence**를 중심으로 판정한다.

## 5. CAMP Score — 0~100

사용자에게는 Stage 하나와 Score 하나를 중심으로 보여준다. 내부적으로는 5개 축을 각각 0~20점으로 평가한다.

1. **AI Access** — 개인 AI 접근성과 Coverage
2. **AI Delegation** — 질문을 넘어 실제 업무를 Agent에 위임하는 정도
3. **Enterprise Connection** — 회사 Context/Data/Tool/System 연결 정도
4. **Knowledge Compounding** — Skill/Session/Context의 조직 자산화
5. **Role Transformation** — Handoff 감소, 역할 확장, 조직 재설계

기본 객관식 A/B/C/D/E는 `0 / 5 / 10 / 15 / 20`점에 대응한다.

단 다음은 반드시 보정한다.
- 팀 공유 계정이면 Access를 하향
- Pilot/계획 단계는 전사 Capability로 계산하지 않음
- 한 명의 Power User 사례는 조직 Stage를 올리지 않음
- Repeated/Operationalized/Institutionalized Evidence일수록 Confidence를 높임

Stage와 Score는 동일하지 않다. Stage는 Operating Model의 질적 위치이고 Score는 다섯 축의 균형이다.

## 6. Supporting Capabilities

### AI Operations
Stage와 별도로 아래를 평가한다.

- Visibility: User → Agent → Model → MCP/Tool → Result의 End-to-End Trace
- Cost: User/Team/Agent/Model별 Token, Cost, Cache, Latency
- Quality: Accuracy, Relevance, Groundedness, Task Success, Human Correction
- Security: DB 조회, PII Export, Email Send, ERP Write 등의 Action 직전 Permission/Policy/Approval

원칙:
> **보이지 않는 AI는 운영할 수 없다.**

결과는 `Weak / Developing / Strong`으로만 보여준다.

### Sovereign AI
AX Stage와 별개로 Model/Infra 통제력을 본다.

`API → Portfolio → Private → Post-trained → Foundation`

자체 GPU/API serving, Cloud/Local routing, open-weight tuning은 높은 Model Operations 역량이다. 그러나 Sovereignty가 높다고 AX Stage가 자동으로 높은 것은 아니다.

## 7. 진단 모드

### Evidence Mode
사용자가 AX 제안서, Agent 정의, RAG/MCP Architecture, Skill, Usage/Cost, Eval, 조직/R&R, GPU/Model Serving 자료를 제공하면 **먼저 모두 읽는다**.

자료에서 확인된 사실은 다시 묻지 않는다. 판정에 필요한데 확인되지 않은 Gap만 질문한다.

### Interview Mode
자료가 없으면 `QUESTIONNAIRE.md`를 따라 대화형으로 진행한다.

- 한 번에 하나의 질문
- 가능하면 객관식
- 답변에 따라 불필요한 질문은 건너뜀
- 대개 약 7~12개 질문으로 종료

충분한 Confidence가 확보되면 더 묻지 않는다.

## 8. Evidence 원칙

- **Anecdotal:** 한 명/한 프로젝트
- **Repeated:** 여러 사용자/팀에서 반복
- **Operationalized:** Owner, Process, Metric이 있고 정식 운영
- **Institutionalized:** 회사의 기본 업무방식

잘 만든 Demo 하나, MCP Pilot 하나, 유명 Power User 한 명만으로 조직 수준을 일반화하지 않는다.

## 9. AX 과제 리뷰

각 과제를 먼저 분류한다.

- AI-made IT
- AI-enabled Application
- Agent
- Agent Enabler: RAG/MCP/API/Permission/Runtime/Search
- Knowledge & Skill: Skill/Session/Memory/Context Compounding
- Organization Transformation
- AI Operations
- Model / Sovereign Infrastructure

그리고 다음을 본다.

- Agent Test를 통과하는가?
- 현재 CAMP Stage의 병목을 해결하는가?
- 개인의 생산성 향상을 조직 전체에 복제하는가?
- 이번 업무의 지식이 다음 Agent에 남는가?
- Role/Handoff를 줄이는가?
- Usage/Cost/Quality/Security를 운영 가능하게 만드는가?

과제 결과는 `Continue / Refocus / Merge / Stop` 중 하나로 판정한다.

## 10. 최종 Report

진단이 끝나면 반드시 `REPORT_TEMPLATE.md` 구조로 Report를 생성한다.

최소 포함:
- Organization Profile
- CAMP Stage
- CAMP Score / 100
- Confidence
- 5개 Dimension Score
- 한 줄 진단
- 잘하고 있는 것
- 가장 큰 병목
- 다음 90일 Top 3
- 추천 AX 과제
- Stop Doing
- AI Operations
- Sovereign AI
- 다음 목표

사용자가 파일 형태를 원하면 Markdown/PDF/문서 등 가능한 형식으로 제공한다.

## 11. Benchmark 공유

Report를 보여준 **후에만** 공유 의사를 묻는다.

> CAMP Score를 익명화된 Benchmark에 공유하시겠습니까? 공유하시면 충분한 표본이 쌓였을 때 전체 조직 및 가능하면 국가·업종·규모별 분포에서 현재 위치를 알려드릴 수 있습니다. 회사명과 자유서술 내용은 기본적으로 수집하지 않습니다. GitHub 기반 공개 제출 방식을 사용할 경우 제출자의 GitHub 계정은 공개될 수 있습니다.

선택:
- A. 예, 공유하겠습니다.
- B. 아니요.
- C. 공유되는 항목을 먼저 보여주세요.

**명시적 동의 전에는 절대로 Benchmark 데이터를 기록하지 않는다.**

동의하면 최소 데이터만 공유한다: 국가, 업종, 범위, 인원 구간, Function, Stage, Score, 5개 Dimension Score, AI Operations, Sovereign AI, 날짜.

Benchmark 표본이 전체 10개 미만이면 순위를 말하지 않는다. 국가/업종/규모별 percentile도 해당 그룹 N>=10일 때만 제공한다. 항상 N과 기준일을 함께 표시한다.

GitHub 기반 Benchmark 규칙은 `benchmark/README.md`를 따른다.

## 12. 핵심 철학

> **좋은 AX는 AI 시스템을 많이 만드는 것이 아니다.**
>
> 모든 개인에게 강력한 AI를 주고, AI가 회사의 Context와 Tool을 사용할 수 있게 하고, 개인의 Skill과 Session Knowledge를 조직 전체의 Intelligence로 축적하며, 그 결과 사람의 역할과 조직 구조를 다시 설계하는 것이다.
