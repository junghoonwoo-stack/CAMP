# CAMP Playbook

## 1. 진단의 목적

CAMP는 기업을 순위 매기기 위한 Maturity Survey가 아니다.

목적은 다음 세 가지다.

1. **현재 실제 Operating Model을 파악**
2. **다음 단계로 가는 가장 큰 병목을 식별**
3. **90일 동안 할 일과 하지 않을 일을 결정**

사용자에게 많은 숫자를 보여주지 않는다.  
핵심 결과는 **Stage 하나 + 병목 하나 + Action 3개**다.

---

## 2. Stage 판정 원칙

### Stage 0 — No AI
판정 신호:
- 외부 AI 사용 금지
- 승인된 AI 없음
- 내부 모델/서비스 없음
- 일부 개인 Shadow AI만 존재

다음 Action:
- 안전한 AI 접근권 제공
- 최소한의 사용정책 수립

### Stage 1 — AI Access
판정 신호:
- ChatGPT/Copilot/Higgsfield 등 일부 도입
- 특정 팀/Power User 위주
- 팀당 공유 계정
- 사용이 특정 Function에 고립

핵심:
> AI는 팀 공용장비가 아니라 개인 업무도구다.

다음 Action:
- 1인 1 AI
- 충분한 Token/Usage 확보
- 실제 업무 사용률 측정

### Stage 2 — AI Workforce
판정 신호:
- 개인별 General Agent
- AI가 실제 산출물을 만듦
- 파일/문서/코드/분석 업무를 위임
- AI가 없으면 생산성이 체감상 크게 감소

핵심:
> 질문하는 AI에서 일을 맡기는 AI로.

다음 Action:
- 반복업무 Skill화
- Power User 사례 복제
- 전문 AI Tool을 Agent Tool로 연결

### Stage 3 — Connected AI
판정 신호:
- Enterprise RAG/Search
- Data Lake 연결
- 내부 MCP/API
- DB/ERP/PLM/CRM Tool
- Auth/Permission
- Event/Trigger/Scheduler
- 일부 Write Action

핵심:
> AI가 회사의 Context와 Tool을 직접 사용할 수 있는가?

다음 Action:
- Search → Understand → Execute 확장
- 가장 가치 높은 System 3개 연결
- Runtime Permission 정교화

### Stage 4 — Compounding AI
판정 신호:
- Skill Repository
- Skill Eval/Version/Owner
- Session summary/trajectory/outcome 저장
- 개인 Agent 학습이 다른 Agent에 재사용
- 조직 Memory 운영

핵심:
> 한 명의 학습이 전체 조직 Agent의 품질을 높이는가?

다음 Action:
- SKILL Ops
- Session → reusable knowledge pipeline
- Outcome Diff 중심의 학습

### Stage 5 — AI-Native Company
판정 신호:
- Agent-first 업무 시작
- 업무 Context의 자동 capture
- 한 사람이 여러 Function 수행
- Handoff 감소
- Role/Process 재설계
- 사람+AI 자원배분
- AI가 필요한 Tool을 직접 만들고 사용
- 경영진/HR가 AI를 전제로 조직 설계

핵심:
> AI가 기존 조직을 더 빠르게 하는가, 조직의 모양 자체를 바꾸는가?

---

## 3. AI-native Greenfield Company

새 회사는 앞 Stage를 순서대로 밟을 필요가 없다.

다음 구조로 시작하면 초기부터 Stage 4~5 특성을 가질 수 있다.

- 모든 구성원에게 General Agent
- 회의/대화/업무맥락 자동 Capture
- Hermes/OpenClaw/Claude/Codex류 Agent-first workspace
- 반복업무 즉시 Skill화
- SaaS/API/CLI를 Agent Tool로 연결
- 없는 Tool은 Vibe Coding으로 제작
- Tool의 사용자가 사람이 아니라 Agent일 수도 있음
- Session에서 reusable knowledge 추출
- 역할을 처음부터 넓게 설계

중요:
**회사 나이, 직원 수, 투자액이 Stage를 결정하지 않는다.**

---

## 4. 흔한 Q&A

### Q. Higgsfield 같은 AI 서비스를 쓰면 AI를 쓰는 것인가?
Yes. Stage 1의 중요한 출발점이다.

다만 목표는 특정 AI App 도입 숫자가 아니다. 모든 개인이 General Agent를 가지고 자신의 전체 업무를 점점 더 많이 위임하는 방향이어야 한다.

### Q. Higgsfield는 나중에 필요 없어지는가?
아니다. 전문 Tool은 계속 중요하다.

더 강한 형태는:
`General Agent → Higgsfield API/CLI → 결과 확인 → 다음 업무`
처럼 Agent가 전문 Tool을 직접 사용하는 것이다.

### Q. Dashboard에 Chatbot이 있으면 Agent인가?
대부분 아니다. Smart Dashboard / AI-enabled Application에 가깝다.

사람이 여전히 중심이며 Chatbot은 사람이 정보를 더 편하게 소비하도록 돕는다.

Agent Test 두 질문으로 판정한다.

### Q. SKILL.md가 꼭 필요한가?
항상은 아니다.

단순·일회성 업무는 Prompt로 충분하다. 그러나 복잡하고 반복되며 여러 사람에게 복제할 업무일수록 Skill이 중요하다.

핵심은 파일 형식이 아니라 **업무 노하우를 AI-readable하고 reusable하게 만드는 것**이다.

### Q. RAG는 Agent 시대에 뒤처진 기술인가?
아니다.

Agent도 정확한 회사 Context가 필요하다. RAG는 Agent가 회사 지식을 사용하는 핵심 Context Infrastructure 중 하나다.

단, Q&A에서 끝나지 않고:
`RAG → 판단 → Tool → Action`
으로 확장하는 것이 다음 단계다.

### Q. 내부 MCP Server는 얼마나 중요한가?
중요하다.

AI가 회사의 Data/System을 실제 Tool로 사용할 수 있게 만드는 Interface다. 내부 MCP/API를 안전하게 운영할 수 있다면 Stage 3의 강한 역량이다.

### Q. 회사 지식 연결은 항상 어려운가?
아니다.

Slack + Google Drive처럼 디지털 업무환경이 단순하고 잘 정리되어 있으면 빠르게 연결할 수 있다.

반대로 Legacy, API 부재, 데이터 품질 저하, 복잡한 권한 구조가 있으면 매우 어렵다.

### Q. 대기업 Data Lake는 Agent 시대에도 가치가 있는가?
매우 크다.

이미 Pipeline, Metadata, Governance, Access Control이 있다면 Agent Context 연결이 훨씬 쉬워진다.

### Q. Vibe Coding은 AX가 아닌가?
Vibe Coding 자체는 매우 중요한 생산성 변화다.

다만 사람이 사용할 Web/App/Dashboard를 더 많이 만드는 것과 Agent가 일을 더 잘하게 Tool을 만드는 것은 방향이 다르다.

질문:
> 이 Software는 사람의 UI를 늘리는가, Agent의 실행능력을 늘리는가?

---

## 5. AI Operations Playbook

### Visibility
최소 Trace:
`User → Agent → Model → Tool/MCP → Result`

봐야 할 것:
- latency
- retry
- failure
- tool call
- model
- user/session

### Cost
요청 단위:
- input/output token
- cache
- model
- user/team
- workflow
- latency

모델 선택:
> **Quality × Cost × Latency**

### Quality
가능하면 Dataset 기반으로:
- groundedness
- relevance
- hallucination
- task success
- correction rate

Skill/Prompt/Model 변경 전후를 비교한다.

### Security
Prompt Injection 탐지만으로 충분하지 않다.

실제 Action 전에:
- identity
- permission
- policy
- data sensitivity
- human approval
를 확인한다.

예:
`고객정보 조회 → export → 외부 email`
은 각 경계에서 차단 가능해야 한다.

---

## 6. Sovereign AI Playbook

Sovereignty는 목적이 아니라 필요한 통제 수준이다.

### API
외부 Model/API 중심. 많은 기업에 합리적.

### Portfolio
여러 Model을 업무별 성능/비용/보안으로 선택.

### Private
Open-weight model, 자체 GPU, VPC/On-prem/local inference.

### Post-trained
LoRA/Fine-tuning/Distillation/Domain adaptation.

### Foundation
Pre-training부터 자체 수행.

진단 시 반드시 묻는다:
- 왜 더 높은 Sovereignty가 필요한가?
- Cost, Security, Latency, Domain Quality 중 어떤 문제를 푸는가?

---

## 7. AX 과제 Review Template

각 과제마다 아래를 기록한다.

### 과제명

**분류:**  
AI-made IT / AI-enabled App / Agent / Agent Enabler / Knowledge & Skill / Org Transformation / AI Operations / Model Infra

**Agent Test:**  
- Model leverage: Yes/Partial/No
- Agent enablement: Yes/Partial/No

**현재 Stage 기여:**  
어느 Stage를 강화하는가?

**Evidence:**  
Anecdotal / Repeated / Operationalized / Institutionalized

**판정:**  
Continue / Refocus / Merge / Stop

**이유:**  
한두 문장

**다음 조치:**  
가장 작은 다음 Action

---

## 8. Interview Questions

질문을 한 번에 다 하지 않는다.

### 시작 질문
> 현재 직원들 중 자기 전용 ChatGPT, Claude, Copilot 같은 AI를 실제 업무에서 반복적으로 쓰는 사람은 대략 몇 %인가요?

답변에 따라:

### 개인 업무
> 그분들은 AI에게 질문만 하나요, 아니면 문서·분석·코드·파일처리 같은 실제 일을 통째로 맡기나요?

### 연결
> 그 Agent가 회사의 문서, 데이터베이스, SaaS 또는 ERP/PLM 같은 시스템을 직접 사용할 수 있나요?

### 인프라
> 사내 RAG, MCP Server, API Tool, Data Lake 연결 중 실제 운영 중인 것이 있나요?

### 지식축적
> 잘하는 직원이 만든 Prompt/Skill/Agent 사용법이 다른 직원에게 자동 또는 체계적으로 배포되나요?

### Session
> Agent와 일하면서 생긴 판단·시행착오·Context가 다음 업무에서 재사용되나요?

### 구조변화
> AI 때문에 두 직무가 합쳐졌거나 Handoff가 실제로 줄어든 사례가 있나요?

### 운영
> 어떤 직원/Agent가 어떤 Model을 얼마나 쓰고, 비용·품질·위험이 어떤지 볼 수 있나요?

### Sovereign
> 외부 API 외에 Local/Open model, 자체 GPU serving, routing, tuning도 운영하나요?

---

## 9. 결과 작성 원칙

좋은 결과는 많은 점수가 아니라 명확한 방향을 준다.

반드시 포함:
1. 현재 Stage
2. Confidence
3. 가장 큰 병목
4. Top 3 Action
5. Stop Doing
6. AI Operations
7. Sovereign AI
8. 근거

과장 금지:
- Pilot 하나를 전사 역량으로 일반화하지 않는다.
- 계획 중인 것을 현재 Capability로 계산하지 않는다.
- 구축했다는 사실과 실제 사용/가치를 구분한다.
