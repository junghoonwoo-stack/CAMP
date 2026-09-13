# CAMP Guided Questionnaire

CAMP는 기본적으로 약 **10분** 안에 끝나는 대화형 진단입니다.

진단을 시작할 때 반드시 다음을 먼저 안내합니다.

> CAMP 진단은 보통 약 10분 정도 걸립니다. 몇 가지 객관식/짧은 질문에 답해주시면 현재 조직의 **CAMP Stage와 CAMP Score**, 가장 큰 병목, 다음 90일의 **우선 Action 3개와 추천 AX 과제**를 드립니다. 자료가 있으면 먼저 읽고 이미 확인된 질문은 건너뜁니다.

가능한 경우 선택지를 버튼/quick reply처럼 클릭 가능하게 제시합니다. UI가 지원하지 않으면 `A/B/C/D` 또는 `1/2/3/4`로 답할 수 있게 합니다. 항상 존댓말을 사용합니다.

## 0. Organization Profile

먼저 진단 범위를 명확히 합니다.

### Q0-1. 무엇을 진단하시나요?
- A. 회사 전체
- B. 사업부/본부
- C. 특정 팀/조직
- D. 새로 만드는 AI-native 조직/스타트업

### Q0-2. 국가
가능하면 선택형으로 제시하고, 없으면 직접 입력하게 합니다.

### Q0-3. 업종
- 제조
- 금융/보험
- IT/SaaS
- 유통/커머스
- 전문서비스
- 헬스케어/바이오
- 공공/교육
- 미디어/콘텐츠
- 건설/에너지
- 기타

### Q0-4. 진단 대상 인원
- 1~10명
- 11~50명
- 51~200명
- 201~1,000명
- 1,001~5,000명
- 5,000명 이상

### Q0-5. 주요 Function
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

## 1. Access

### Q1. 구성원 중 자기 전용 AI를 실제 업무에서 반복적으로 쓰는 비율은 어느 정도인가요?
- A. 5% 미만
- B. 5~20%
- C. 21~50%
- D. 51~80%
- E. 81% 이상

추가 확인이 필요한 경우만 묻습니다.
- 개인별 계정인가, 팀 공유 계정인가?
- 충분한 Token/Usage가 제공되는가?

## 2. Delegation / AI Workforce

### Q2. AI를 주로 어떻게 사용하시나요?
- A. 검색/질문/요약 중심
- B. 초안 작성이나 일부 Task 수행
- C. 문서·분석·코딩·파일처리 등 실제 업무를 자주 위임
- D. 여러 Tool을 사용해 End-to-End 업무를 반복 수행
- E. 대부분의 사람이 Agent-first로 일을 시작

## 3. Connection

### Q3. Agent가 회사의 실제 Context와 Tool을 어디까지 사용할 수 있나요?
- A. 외부 일반지식만 사용
- B. 파일/문서/RAG 등 회사 지식 조회
- C. M365/Google Workspace/Slack/Drive 등 업무 Context와 연결
- D. MCP/API/DB/ERP/PLM/CRM 등 내부 시스템을 Tool로 사용
- E. Read뿐 아니라 Write/Trigger/Scheduler까지 운영

필요하면 RAG, MCP, Data Lake, API, Auth/Permission이 실제 운영 중인지 확인합니다.

## 4. Compounding

### Q4. 개인이 AI와 일하며 만든 Skill/Prompt/Session 지식이 조직에 축적되나요?
- A. 거의 남지 않음
- B. 개인이 각자 저장
- C. Prompt/Skill을 공유하는 저장소가 있음
- D. Skill에 Owner/Version/Eval이 있고 조직적으로 배포
- E. Session에서 새로운 Context/노하우가 자동 또는 체계적으로 추출되어 다른 Agent에 재사용

## 5. Transformation

### Q5. AI가 직무/Process 자체를 바꾸고 있나요?
- A. 아직 없음
- B. 기존 직무 안에서 생산성만 개선
- C. 개인이 인접 업무까지 수행하기 시작
- D. 여러 팀에서 Handoff가 줄고 역할이 통합됨
- E. R&R/조직/인력배치가 AI를 전제로 재설계됨

## 6. AI Operations

### Q6. AI 사용을 얼마나 운영 가능하게 보고 있나요?
- A. 거의 보이지 않음
- B. 사용량/비용 일부 확인
- C. User/Agent/Model별 Cost와 Usage 확인
- D. End-to-End Trace와 Quality Eval까지 운영
- E. Visibility + Cost + Quality + Runtime Security를 통합 운영

## 7. Sovereign AI

### Q7. Model/Infra를 어디까지 직접 통제하시나요?
- A. 외부 SaaS/API 중심
- B. 여러 외부 모델을 업무별로 선택/라우팅
- C. Private/Local/Open-weight inference 또는 자체 GPU/API serving
- D. Fine-tuning/LoRA/Distillation/Post-training
- E. Foundation Model을 직접 개발/운영

Sovereign AI는 CAMP Stage를 결정하는 필수조건이 아닙니다. 필요성은 Cost, Security, Latency, Domain Quality 관점으로 판단합니다.

## 8. Evidence Deep Dive

다음은 답에 따라 필요한 경우에만 추가 질문합니다.
- 실제 운영인지 Pilot인지
- 몇 명/몇 팀에서 반복되는지
- Owner/Metric/Process가 있는지
- AI가 실제 업무 결과를 끝까지 만드는지
- Write Action의 Permission/Approval이 있는지
- 어떤 과제들이 현재 추진 중인지

질문 수를 늘리는 것이 목적이 아닙니다. 충분한 Confidence가 확보되면 진단을 종료합니다.
