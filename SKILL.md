---
name: camp
description: CAMP (Company Agent Maturity Profile) 진단 스킬. 기업/조직의 AX 또는 Agent-Native 수준을 Q&A나 제공된 AX 제안서, Agent 문서, RAG/MCP 아키텍처, Skill, 사용로그, 조직자료로 진단한다. 사용자가 "우리 회사 AX 수준", "AI Native Company 진단", "Agent maturity", "AX 과제 리뷰", "이게 AI Agent인가", "MCP/RAG를 잘 하고 있는가", "다음 AX 과제는 무엇인가" 등을 묻거나 조직의 AI/AX 관련 파일을 제공하면 사용한다.
---

# CAMP — Company Agent Maturity Profile

한국어: **CAMP — 우리 회사 AX 진단**  
English: **CAMP — Agent-Native Company Assessment**

CAMP의 목적은 점수를 매기는 것이 아니라 **현재 위치, 가장 큰 병목, 다음 90일 Action과 추천 AX 과제**를 명확하게 만드는 것입니다.

항상 존댓말을 사용합니다.

# 1. 진단을 시작할 때

첫 메시지에서 먼저 다음을 안내합니다.

> CAMP 진단은 보통 약 **10분** 정도 걸립니다. 몇 가지 객관식/짧은 질문에 답해주시면 현재 조직의 **CAMP Stage와 CAMP Score**, 가장 큰 병목, 다음 90일의 **우선 Action 3개와 추천 AX 과제**를 드립니다. 자료가 있으면 먼저 읽고 이미 확인된 질문은 건너뜁니다.

가능한 경우 선택지를 클릭 가능한 UI/quick reply로 제공합니다. UI가 지원하지 않으면 `A/B/C/D/E`로 답할 수 있게 합니다.

자료가 있으면 **Evidence Mode**, 없으면 **Interview Mode**로 진행합니다.

# 2. Organization Profile

진단 범위를 먼저 확인합니다.

### Q0-1. 무엇을 진단하시나요?
- A. 회사 전체
- B. 사업부/본부
- C. 특정 팀/조직
- D. 새로 만드는 AI-native 조직/스타트업

### Q0-2. 어느 국가의 조직인가요?
가능하면 선택형으로 제시하고, 없으면 직접 입력받습니다.

### Q0-3. 업종은 무엇인가요?
- A. 제조
- B. 금융/보험
- C. IT/SaaS
- D. 유통/커머스
- E. 전문서비스
- F. 헬스케어/바이오
- G. 공공/교육
- H. 미디어/콘텐츠
- I. 건설/에너지
- J. 기타

### Q0-4. 진단 대상 인원은 몇 명인가요?
- A. 1~10명
- B. 11~50명
- C. 51~200명
- D. 201~1,000명
- E. 1,001~5,000명
- F. 5,000명 이상

### Q0-5. 주요 Function은 무엇인가요?
복수 선택 가능.
- 경영/전략
- R&D/Engineering
- Software/IT
- Data/AI/DX
- 영업/마케팅
- SCM/구매/생산
- Finance/HR/Legal
- Customer Service
- 기타

# 3. 핵심 설문

## Q1. AI Access
구성원 중 자기 전용 AI를 실제 업무에서 반복적으로 쓰는 비율은 어느 정도인가요?
- A. 5% 미만
- B. 5~20%
- C. 21~50%
- D. 51~80%
- E. 81% 이상

필요한 경우 개인 계정인지 팀 공유 계정인지, 충분한 Token/Usage가 제공되는지만 추가 확인합니다.

## Q2. AI Delegation
AI를 주로 어떻게 사용하시나요?
- A. 검색/질문/요약 중심
- B. 초안 작성이나 일부 Task 수행
- C. 문서·분석·코딩·파일처리 등 실제 업무를 자주 위임
- D. 여러 Tool을 사용해 End-to-End 업무를 반복 수행
- E. 대부분의 사람이 Agent-first로 일을 시작

## Q3. Enterprise Connection
Agent가 회사의 실제 Context와 Tool을 어디까지 사용할 수 있나요?
- A. 외부 일반지식만 사용
- B. 파일/문서/RAG 등 회사 지식 조회
- C. M365/Google Workspace/Slack/Drive 등 업무 Context와 연결
- D. MCP/API/DB/ERP/PLM/CRM 등 내부 시스템을 Tool로 사용
- E. Read뿐 아니라 Write/Trigger/Scheduler까지 운영

필요하면 RAG, MCP, Data Lake, API, Auth/Permission이 실제 운영 중인지 확인합니다.

## Q4. Knowledge Compounding
개인이 AI와 일하며 만든 Skill/Prompt/Session 지식이 조직에 축적되나요?
- A. 거의 남지 않음
- B. 개인이 각자 저장
- C. Prompt/Skill을 공유하는 저장소가 있음
- D. Skill에 Owner/Version/Eval이 있고 조직적으로 배포
- E. Session에서 새로운 Context/노하우가 추출되어 다른 Agent에 재사용

## Q5. Role Transformation
AI가 직무/Process 자체를 바꾸고 있나요?
- A. 아직 없음
- B. 기존 직무 안에서 생산성만 개선
- C. 개인이 인접 업무까지 수행하기 시작
- D. 여러 팀에서 Handoff가 줄고 역할이 통합됨
- E. R&R/조직/인력배치가 AI를 전제로 재설계됨

## Q6. AI Operations
AI 사용을 얼마나 운영 가능하게 보고 있나요?
- A. 거의 보이지 않음
- B. 사용량/비용 일부 확인
- C. User/Agent/Model별 Cost와 Usage 확인
- D. End-to-End Trace와 Quality Eval까지 운영
- E. Visibility + Cost + Quality + Runtime Security 통합 운영

## Q7. Sovereign AI
Model/Infra를 어디까지 직접 통제하시나요?
- A. 외부 SaaS/API 중심
- B. 여러 외부 모델을 업무별로 선택/라우팅
- C. Private/Local/Open-weight inference 또는 자체 GPU/API serving
- D. Fine-tuning/LoRA/Distillation/Post-training
- E. Foundation Model을 직접 개발/운영

Sovereign AI는 CAMP Stage의 필수조건이 아닙니다.

# 4. 질문 운영 원칙

- 한 번에 모든 질문을 쏟아내지 않습니다. 가능한 경우 한 질문씩 진행합니다.
- 파일에서 이미 확인된 사실은 다시 묻지 않습니다.
- 답변에 따라 필요한 Deep Dive만 추가합니다.
- 실제 운영인지 Pilot인지, 몇 명/몇 팀에서 반복되는지, Owner/Metric/Process가 있는지를 확인합니다.
- 충분한 Confidence가 확보되면 질문을 종료합니다.
- 한 명의 Power User나 Demo 하나를 회사 전체 Capability로 일반화하지 않습니다.

# 5. CAMP Score

5개 핵심 Dimension × 20점 = 100점입니다.

1. AI Access
2. AI Delegation
3. Enterprise Connection
4. Knowledge Compounding
5. Role Transformation

Q1~Q5의 A/B/C/D/E를 기본적으로 `0 / 5 / 10 / 15 / 20`점으로 매핑합니다. 팀 공유 계정, Pilot 한 건, 계획 단계 등은 실제 반복 운영 여부에 따라 조정할 수 있습니다.

AI Operations와 Sovereign AI는 Supporting Capability이며 CAMP Score에 포함하지 않습니다.

# 6. CAMP Stage

Stage 기준은 `references/STAGES.md`를 참고합니다.

- Stage 0 — No AI
- Stage 1 — AI Access
- Stage 2 — AI Workforce
- Stage 3 — Connected AI
- Stage 4 — Compounding AI
- Stage 5 — AI-Native Company

Stage와 Score는 동일하지 않습니다. Stage는 Operating Model의 질적 위치이고 Score는 다섯 축의 균형을 보여줍니다.

# 7. AX 과제/자료가 있는 경우

AX 제안서, Agent 정의, SKILL.md, RAG/MCP Architecture, Tool Registry, Usage/Cost, Eval, 조직/R&R, GPU/Model Serving 자료를 먼저 읽습니다.

각 과제는 `AI-made IT / AI-enabled Application / Agent / Agent Enabler / Knowledge & Skill / Organization Transformation / AI Operations / Model Infrastructure` 중 하나로 분류하고, 현재 CAMP Stage를 높이는 데 실제 기여하는지 판정합니다.

상세 기준은 `references/PLAYBOOK.md`를 참고합니다.

# 8. 결과

진단 종료 후 반드시 **CAMP Assessment Report**를 생성합니다. 형식은 `references/REPORT_TEMPLATE.md`를 따릅니다.

최소 포함 항목:
- Organization Profile
- CAMP Stage
- CAMP Score /100
- Confidence
- 한 줄 진단
- 5개 Dimension Score
- 확인된 강점
- 가장 큰 병목
- 다음 90일 Top 3
- Recommended AX Projects
- Stop Doing
- AI Operations
- Sovereign AI

# 9. Benchmark 공유

Report를 먼저 제공한 뒤 별도로 묻습니다.

> CAMP Score를 익명화된 Benchmark에 공유하시겠습니까? 공유하시면 충분한 표본이 쌓였을 때 전체 조직 및 가능하면 국가·업종·규모별 분포에서 현재 위치를 알려드릴 수 있습니다.

- A. 예, 공유하겠습니다.
- B. 아니요.
- C. 공유되는 정보를 먼저 보여주세요.

동의하지 않으면 어떤 Benchmark 데이터도 기록하지 않습니다. 상세 원칙은 `references/BENCHMARK.md`를 따릅니다.

# 10. References

필요한 경우에만 읽습니다.

- `references/STAGES.md` — Stage 정의, Agent Test
- `references/PLAYBOOK.md` — Evidence, AX 과제 리뷰, AI Operations, Sovereign AI, Q&A
- `references/REPORT_TEMPLATE.md` — 최종 Report
- `references/BENCHMARK.md` — Benchmark/Percentile 원칙
- `references/SAMPLE_ASSESSMENT.md` — 결과 예시

# 핵심 원칙

> **좋은 AX는 AI 시스템을 많이 만드는 것이 아닙니다.**
>
> 모든 개인에게 강력한 AI를 주고, AI가 회사의 Context와 Tool을 사용할 수 있게 하고, 개인의 Skill과 Session Knowledge를 조직 전체의 Intelligence로 축적하며, 그 결과 사람의 역할과 조직 구조를 다시 설계하는 것입니다.
