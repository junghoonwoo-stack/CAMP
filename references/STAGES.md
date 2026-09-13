# CAMP Stages

CAMP Stage는 순차 교육과정이 아니라 현재 조직의 반복적 Operating Model을 나타냅니다.

## Stage 0 — No AI
승인된 업무용 AI가 거의 없음. 다음 Action은 안전한 AI 접근권과 최소 사용정책 확보.

## Stage 1 — AI Access
AI가 일부 사용자/특정 Function에만 있음. 팀 공유 계정보다 **1인 1 AI**가 핵심. 다음 Action은 충분한 Token/Usage와 실제 업무 사용률 확대.

## Stage 2 — AI Workforce
대부분의 개인이 General Agent에게 문서·분석·코딩·파일처리 등 실제 일을 맡김. 핵심 KPI는 한 개인의 전체 업무 중 얼마나 Agent에게 맡길 수 있는가. 다음 Action은 반복업무 Skill화와 Power User 사례 복제.

## Stage 3 — Connected AI
Agent가 사내 RAG, Data Lake, MCP/API, DB/ERP/PLM/CRM, SaaS, Auth/Permission, Trigger/Scheduler 등에 연결됨. 내부 MCP Server나 Enterprise RAG를 실제 운영하는 것은 중요한 역량임. 다음 Action은 `Search → Understand → Execute` 확장.

## Stage 4 — Compounding AI
Skill, Session, 판단과 Context가 조직 자산으로 축적되고 다른 Agent에 재사용됨. Skill에 Owner/Version/Eval이 있고 Session에서 reusable knowledge를 추출함. 핵심 질문은 **오늘 한 사람이 Agent에게 가르친 것이 내일 다른 사람의 Agent에도 남는가?**

## Stage 5 — AI-Native Company
Agent-first로 일을 시작하고 업무 Context를 자동 capture하며, 한 사람이 여러 Function을 수행하고 Handoff가 줄어듦. SaaS/API는 Agent Tool로 연결하고 없는 Tool은 필요시 Vibe Coding으로 만듦. R&R, 조직, 인력배치까지 AI를 전제로 재설계함.

## Greenfield / AI-native 조직
새 회사는 Stage를 순서대로 밟을 필요가 없음. 처음부터 모든 구성원에게 General Agent를 주고, Context capture, Skill화, Tool 연결, Session knowledge 축적, 넓은 Role 설계를 적용하면 초기부터 Stage 4~5 특성을 가질 수 있음.

## Agent 정의

> **Agent = Model + Context + Harness**

- Model: GPT, Claude, Gemini, open-weight, 자체 모델 등
- Context: Data, RAG, 문서, 이메일, Slack/Teams, Memory, Session, 과거 의사결정
- Harness: Skill/Instruction, Tool, MCP/API, Permission, Scheduler/Trigger, Runtime, Eval, Observability

## Agent Test

1. AI 모델이 좋아질수록 이 시스템의 업무 수행 능력도 자연스럽게 좋아지는가?
2. 현재 개발이 AI가 일을 더 잘하도록 Context, Data, Tool, Skill, Permission, Runtime 등을 강화하는가?

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**임. 가치가 없다는 뜻은 아니지만 Agent Transformation과 구분함.
