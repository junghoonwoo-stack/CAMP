# CAMP Diagnostic Playbook

## Evidence 원칙

한 명의 Power User, Demo 하나, Pilot 하나만으로 조직 Stage를 높이지 않습니다.

- **Anecdotal:** 한 명/한 프로젝트
- **Repeated:** 여러 사용자/팀에서 반복
- **Operationalized:** Owner, Process, Metric이 있고 정식 운영
- **Institutionalized:** 회사의 기본 업무방식

계획/제안 중인 것은 현재 Capability로 계산하지 않습니다. Stage는 반복성·일반화·운영화된 상태를 중심으로 판정합니다.

## AX 과제 분류

- AI-made IT
- AI-enabled Application
- Agent
- Agent Enabler: RAG/MCP/API/Permission/Runtime/Search
- Knowledge & Skill: Skill/Session/Memory/Context Compounding
- Organization Transformation
- AI Operations
- Model / Sovereign Infrastructure

각 과제에 대해 다음을 평가합니다.

1. 현재 CAMP Stage를 실제로 높이는가?
2. Agent Test를 통과하는가?
3. 개인의 생산성 향상을 조직 전체에 복제하는가?
4. 업무에서 생긴 지식이 다음 Agent에 남는가?
5. Role/Handoff를 줄이는가?
6. 운영·비용·품질·보안을 측정할 수 있는가?

판정은 `Continue / Refocus / Merge / Stop` 중 하나로 제시합니다.

## AI Operations

**Visibility** — `User → Agent → Model → Tool/MCP → Result` End-to-End Trace, latency, retry, failure, tool call, user/session을 봅니다.

**Cost** — User/Team/Agent/Model별 Token, Cost, Cache, Latency를 봅니다. 모델 선택은 **Quality × Cost × Latency**로 판단합니다.

**Quality** — Groundedness, relevance, hallucination, task success, correction rate를 가능하면 Dataset 기반으로 평가하고 Skill/Prompt/Model 변경 전후를 비교합니다.

**Security** — Prompt Injection 탐지만으로 충분하지 않습니다. DB 조회, PII Export, Email Send, ERP Write 같은 Action 직전에 identity, permission, policy, data sensitivity, human approval을 확인해야 합니다.

> **보이지 않는 AI는 운영할 수 없습니다.**

## Sovereign AI

Sovereignty는 CAMP Stage와 별도의 Supporting Capability입니다.

- **API:** 외부 SaaS/API 중심
- **Portfolio:** 여러 모델을 업무별 성능/비용/보안에 따라 선택/라우팅
- **Private:** Open-weight, 자체 GPU, VPC/On-prem/Local inference
- **Post-trained:** LoRA/Fine-tuning/Distillation/Domain adaptation
- **Foundation:** Pre-training부터 자체 수행

자체 모델이 없어도 높은 CAMP Stage가 가능하며, Foundation Model이 있어도 조직의 Agent 활용이 낮으면 CAMP Stage는 낮을 수 있습니다.

## 흔한 Q&A

### Higgsfield 같은 전문 AI를 쓰면 AI를 쓰는 것인가?
네. Stage 1의 중요한 출발점입니다. 다만 목표는 AI App 개수가 아니라 모든 개인이 General Agent에게 전체 업무를 점점 더 많이 위임하는 방향입니다.

### 전문 AI Tool은 필요 없어지는가?
아닙니다. `General Agent → 전문 Tool API/CLI → 결과 → 다음 업무`처럼 Agent가 Tool을 직접 사용하는 방향이 더 강합니다.

### Dashboard에 Chatbot이 있으면 Agent인가?
대부분 Smart Dashboard / AI-enabled Application에 가깝습니다. Agent Test 두 질문으로 판정합니다.

### SKILL.md가 꼭 필요한가?
항상은 아닙니다. 단순·일회성 업무는 Prompt로 충분할 수 있습니다. 복잡하고 반복되며 여러 사람에게 복제할 업무일수록 Skill이 중요합니다. 핵심은 파일 형식이 아니라 업무 노하우를 AI-readable하고 reusable하게 만드는 것입니다.

### RAG는 Agent 시대에 뒤처진 기술인가?
아닙니다. RAG는 Agent가 회사 지식을 사용하는 핵심 Context Infrastructure입니다. 다음 단계는 `RAG → 판단 → Tool → Action`입니다.

### 내부 MCP Server는 중요한가?
중요합니다. AI가 회사의 Data/System을 실제 Tool로 사용할 수 있게 만드는 Interface입니다. 실제 운영 중인 MCP/API는 Stage 3의 강한 Evidence입니다.

### Data Lake는 Agent 시대에도 가치가 있는가?
매우 큽니다. Pipeline, Metadata, Governance, Access Control이 이미 있으면 Agent Context 연결이 훨씬 쉬워집니다.

### Vibe Coding은 AX가 아닌가?
Vibe Coding은 중요한 생산성 변화입니다. 다만 사람이 사용할 App/Dashboard를 더 많이 만드는 것과 Agent가 더 잘 일하도록 Tool을 만드는 것은 구분해야 합니다.

> 이 Software는 사람의 UI를 늘리는가, Agent의 실행능력을 늘리는가?
