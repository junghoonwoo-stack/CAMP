---
name: camp
description: CAMP (Company Agent Maturity Profile) 진단 스킬. 기업/조직의 AX 또는 Agent-Native 수준을 Q&A나 제공된 AX 제안서, Agent 문서, RAG/MCP 아키텍처, Skill, 사용로그, 조직자료로 진단한다. 사용자가 "우리 회사 AX 수준", "AI Native Company 진단", "Agent maturity", "AX 과제 리뷰", "이게 AI Agent인가", "MCP/RAG를 잘 하고 있는가", "다음 AX 과제는 무엇인가" 등을 묻거나 조직의 AI/AX 관련 파일을 제공하면 사용한다.
---

# CAMP — Company Agent Maturity Profile

한국어에서는 **"CAMP — 우리 회사 AX 진단"**, 영어에서는 **"CAMP — Agent-Native Company Assessment"**로 표현한다.

CAMP의 목적은 점수를 매기는 것이 아니라 **현재 위치, 가장 큰 병목, 다음 단계로 가기 위한 90일 Action을 명확하게 만드는 것**이다.

상세 기준은 `PLAYBOOK.md`를 반드시 참고한다.

## 1. CAMP의 기본 철학

기업 AX의 수준은 AI App이나 Dashboard의 개수로 평가하지 않는다.

다음을 본다.

> 모든 개인이 AI를 사용할 수 있는가  
> → AI에게 실제 업무를 맡기는가  
> → AI가 회사의 Context와 Tool을 사용할 수 있는가  
> → 개인의 Skill과 Session이 조직 자산으로 축적되는가  
> → AI 때문에 역할, Handoff, 조직 구조가 바뀌는가

## 2. Agent 정의

> **Agent = Model + Context + Harness**

- **Model:** GPT, Claude, Gemini, open-weight, 자체 모델 등
- **Context:** Data, RAG, 문서, 이메일, Slack/Teams, Memory, Session, 과거 의사결정 등
- **Harness:** Skill/Instruction, Tool, MCP/API, Permission, Scheduler/Trigger, Runtime, Evaluation, Observability 등

### Agent Test

모든 AX 과제를 먼저 두 질문으로 본다.

1. **AI 모델이 좋아질수록 이 시스템의 업무 수행 능력도 자연스럽게 좋아지는가?**
2. **현재 개발이 AI가 일을 더 잘하도록 Context, Data, Tool, Skill, Permission, Runtime 등을 강화하는가?**

둘 다 No라면 보통 `AI로 더 빨리 만든 기존 IT`다.  
가치가 없다는 뜻은 아니지만 Agent Transformation과 구분한다.

## 3. CAMP Stage

Stage는 반드시 순서대로 밟는 교육과정이 아니다. **현재 반복적으로 작동하는 Operating Model**을 평가한다.

### Stage 0 — No AI
업무에 사용할 수 있는 AI 접근 자체가 거의 없다.

### Stage 1 — AI Access
AI Tool이 일부 사용자나 특정 Function에만 있다.  
팀 공용 계정 하나가 아니라 **1인 1 AI**로 가는 것이 핵심이다.

Higgsfield 같은 전문 AI를 쓰는 것도 분명 AI 활용이다. 다만 회사 전체가 General Agent를 업무 기본도구로 쓰는 단계와는 구분한다.

### Stage 2 — AI Workforce
대부분의 개인이 자신의 General Agent에게 실제 업무를 맡긴다.

핵심 KPI는:
> **한 개인의 전체 업무 중 얼마나 Agent에게 맡길 수 있는가?**

전문 Tool은 사람이 직접 여러 App을 돌아다니기보다 General Agent가 필요할 때 API/CLI/Connector로 호출하는 방향이 강하다.

### Stage 3 — Connected AI
Agent가 회사의 실제 업무환경에 연결된다.

예:
- RAG / Enterprise Search
- Data Lake
- 내부 MCP Server
- DB / ERP / PLM / CRM
- Slack / Teams / Drive / SharePoint
- SaaS Connector
- 사내 API
- Authentication / Permission
- Event / Scheduler / Write Action

내부 MCP Server나 Enterprise RAG를 실제 운영하는 것은 중요한 Enterprise AX 역량이다.

### Stage 4 — Compounding AI
개인이 Agent와 일하며 만든 Skill, Session, 판단과 Context가 조직 자산으로 축적되고 다른 Agent에게 재사용된다.

핵심 질문:
> **오늘 한 사람이 Agent에게 가르친 것이 내일 다른 사람의 Agent에도 남는가?**

SKILL.md 자체가 목적은 아니다. 업무가 복잡·반복될수록 Skill이 필요하며, 핵심은 좋은 업무방식을 조직 전체에 복제하는 **SKILL Ops**다.

### Stage 5 — AI-Native Company
사람이 과거 Web Browser를 켰듯 Agent를 켜고 일을 시작한다.

- 모든 Context를 가능한 한 자동 기록
- 반복업무는 Skill화
- SaaS/API는 Agent Tool로 연결
- 없는 Tool은 Vibe Coding으로 빠르게 제작
- 사람용 App보다 Agent가 더 싸고 빠르게 일하도록 Tool을 만들기도 함
- 한 사람이 여러 Function을 수행
- Handoff와 R&R이 줄어듦
- HR/조직/자원배분까지 AI를 전제로 재설계

AI-native startup은 설립 초기부터 Stage 4~5 특성을 가질 수 있다.

## 4. Supporting Capability

### AI Operations
Stage와 별도로 아래 4가지를 본다.

- **Visibility:** User → Agent → Model → MCP/Tool → Result의 End-to-End Trace
- **Cost:** User/Team/Agent/Model별 Token, Cost, Cache, Latency
- **Quality:** Accuracy, Relevance, Groundedness, Task Success, Human Correction
- **Security:** 실제 DB 조회, PII Export, Email Send, ERP Write 등의 Action 직전에 Permission/Policy/Approval 적용

원칙:
> **보이지 않는 AI는 운영할 수 없다.**

### Sovereign AI
AX Stage와 별개로 Model/Infra 통제력을 본다.

- External API
- Multi-model Portfolio / Routing
- Private / Local Inference
- 자체 GPU / Model API Serving
- Open-weight Fine-tuning / LoRA / Distillation / Post-training
- Foundation Model

자체 GPU/API Serving과 Cloud/Local routing을 안정적으로 운영할 수 있다면 높은 Model Operations 역량이다.

## 5. 진단 방식

### Evidence Mode
사용자가 파일이나 자료를 제공하면 먼저 읽는다.

예:
- AX 과제 제안서
- Agent 정의
- SKILL.md / Prompt / Instruction
- RAG / MCP Architecture
- Tool Registry
- Usage / Cost
- Eval
- 조직/R&R 자료
- GPU / Model Serving 자료

자료에서 이미 확인한 내용은 다시 묻지 않는다.  
**판정에 필요한데 확인되지 않은 핵심 정보만 질문한다.**

### Interview Mode
자료가 없으면 한 번에 하나씩 질문한다.

질문 우선순위:
1. 전 직원 중 자기 전용 AI를 실제 업무에 반복 사용하는 비율
2. 실제로 Agent에게 맡기는 업무
3. Agent의 회사 Data/Tool/System 접근 범위
4. RAG/MCP/API/Write Action/Trigger 여부
5. Skill 저장·공유 여부
6. Session/Context의 조직적 재사용 여부
7. Role/Handoff 변화
8. Visibility/Cost/Quality/Security 운영 여부
9. Multi-model/Local/Open model/GPU/tuning 역량

설문지처럼 15개를 한꺼번에 묻지 않는다. 답변에 따라 필요한 질문만 이어간다.

## 6. Evidence 원칙

한 명의 Power User, Demo 하나, Pilot 하나만으로 회사 Stage를 높이지 않는다.

- **Anecdotal:** 한 명/한 프로젝트
- **Repeated:** 여러 사용자/팀에서 반복
- **Operationalized:** Owner, Process, Metric이 있고 정식 운영
- **Institutionalized:** 회사의 기본 업무방식

Stage는 **반복성·일반화·운영화된 상태**를 중심으로 판단한다.

확실하지 않으면 Confidence를 낮추고 필요한 Evidence를 명시한다.

## 7. AX 과제 리뷰

각 과제를 먼저 분류한다.

- AI-made IT
- AI-enabled Application
- Agent
- Agent Enabler: RAG/MCP/API/Permission/Runtime/Search
- Knowledge & Skill: Skill/Session/Memory/Context Compounding
- Organization Transformation
- AI Operations
- Model / Sovereign Infrastructure

그리고 다음을 평가한다.

1. 이 과제가 현재 CAMP Stage를 실제로 높이는가?
2. Agent Test를 통과하는가?
3. 개인의 생산성 향상을 조직 전체에 복제하는가?
4. 업무에서 생긴 지식이 다음 Agent에 남는가?
5. Role/Handoff를 줄이는가?
6. 운영·비용·품질·보안을 측정할 수 있는가?

## 8. 출력 형식

항상 간결한 한 장 형식으로 시작한다.

### 🧭 CAMP Result

**현재 위치:** `Stage N — Name`  
**Confidence:** High / Medium / Low

**한 줄 진단:** 현재 Operating Model과 가장 큰 병목

**잘하고 있는 것**
- 근거 있는 강점 2~4개

**가장 큰 병목**
- 다음 Stage를 막는 한 가지

**다음 90일 Top 3**
1. Action
2. Action
3. Action

**Stop Doing**
- Stage 발전에 거의 기여하지 않거나 에너지를 분산시키는 것

**AI Operations:** Weak / Developing / Strong — 근거 한 줄  
**Sovereign AI:** API / Portfolio / Private / Post-trained / Foundation — 근거 한 줄

**다음 목표:** 다음 Stage 또는 가장 중요한 foundation gap

AX 과제가 주어졌다면:
`과제 | 분류 | CAMP 기여 | 판정 | 다음 조치`
표를 추가한다.

## 9. 가장 중요한 원칙

> **좋은 AX는 AI 시스템을 많이 만드는 것이 아니다.**
>
> 모든 개인에게 강력한 AI를 주고, AI가 회사의 Context와 Tool을 사용할 수 있게 하고, 개인의 Skill과 Session Knowledge를 조직 전체의 Intelligence로 축적하며, 그 결과 사람의 역할과 조직 구조를 다시 설계하는 것이다.
