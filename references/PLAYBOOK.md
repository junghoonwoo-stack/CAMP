# CAMP Diagnostic Playbook

## English

### Evidence rule
Do not raise an organization’s Stage based on one power user, demo, or pilot.

- **Anecdotal:** one user/project
- **Repeated:** repeated across users/teams
- **Operationalized:** owner, process, metrics, production use
- **Institutionalized:** default way of working

Plans and proposals do not count as current capability.

### AX project types
- AI-made IT
- AI-enabled application
- Agent
- Agent enabler: RAG / MCP / API / permission / runtime / search
- Knowledge & skill: skill / session / memory / context compounding
- Organization transformation
- AI operations
- Model / sovereign infrastructure

For each project ask:
1. Does it move the organization to a higher CAMP Stage?
2. Does it pass the Agent Test?
3. Can individual productivity gains be replicated?
4. Does new knowledge survive into future agents?
5. Does it reduce role boundaries or handoffs?
6. Can cost, quality, usage, and risk be operated?

Decision: **Continue / Refocus / Merge / Stop**.

### AI Operations
- **Visibility:** `User → Agent → Model → Tool/MCP → Result`
- **Cost:** token, cache, model, user/team, latency
- **Quality:** groundedness, relevance, hallucination, task success, correction rate
- **Security:** check identity, permission, policy, data sensitivity, and approval before high-risk actions

> **You cannot operate AI you cannot see.**

### Sovereign AI
- **API:** external SaaS/API
- **Portfolio:** multi-model routing
- **Private:** open-weight, private/local inference, own GPU/API
- **Post-trained:** LoRA, fine-tuning, distillation, domain adaptation
- **Foundation:** pre-training and operating a foundation model

Sovereignty is a supporting capability, not a CAMP Stage requirement.

### Common questions
- **Specialized AI tools such as Higgsfield?** Valuable, but stronger when a general agent can call them as tools.
- **Chatbot inside a dashboard?** Usually an AI-enabled application, not an agent.
- **Is SKILL.md mandatory?** No. It matters when work becomes complex, repeatable, and worth replicating.
- **Is RAG obsolete?** No. It is context infrastructure; the next step is `RAG → reasoning → tool → action`.
- **Is an internal MCP server meaningful?** Yes. Production MCP/API is strong Stage 3 evidence.
- **Does a data lake still matter?** Yes. Existing pipelines, metadata, governance, and access control accelerate agent connectivity.
- **Is vibe coding AX?** It can improve productivity, but distinguish software for human UI from tools that expand agent execution.

## 한국어

### Evidence 원칙
Power User 한 명, Demo 하나, Pilot 하나만으로 조직 Stage를 높이지 않습니다.

- **Anecdotal:** 한 명/한 프로젝트
- **Repeated:** 여러 사용자/팀에서 반복
- **Operationalized:** Owner, Process, Metric, 운영환경 존재
- **Institutionalized:** 기본 업무방식

계획·제안 단계는 현재 Capability로 계산하지 않습니다.

### AX 과제 유형
- AI-made IT
- AI-enabled Application
- Agent
- Agent Enabler: RAG / MCP / API / Permission / Runtime / Search
- Knowledge & Skill: Skill / Session / Memory / Context Compounding
- Organization Transformation
- AI Operations
- Model / Sovereign Infrastructure

각 과제에 대해 다음을 봅니다.
1. CAMP Stage를 실제로 높이는가?
2. Agent Test를 통과하는가?
3. 개인 생산성 향상을 복제할 수 있는가?
4. 새 지식이 다음 Agent에도 남는가?
5. Role/Handoff를 줄이는가?
6. Cost, Quality, Usage, Risk를 운영할 수 있는가?

판정: **Continue / Refocus / Merge / Stop**.

### AI Operations
- **Visibility:** `User → Agent → Model → Tool/MCP → Result`
- **Cost:** Token, Cache, Model, User/Team, Latency
- **Quality:** Groundedness, Relevance, Hallucination, Task Success, Correction Rate
- **Security:** 위험 Action 직전에 Identity, Permission, Policy, Data Sensitivity, Approval 확인

> **보이지 않는 AI는 운영할 수 없습니다.**

### Sovereign AI
- **API:** 외부 SaaS/API
- **Portfolio:** Multi-model Routing
- **Private:** Open-weight, Private/Local Inference, 자체 GPU/API
- **Post-trained:** LoRA, Fine-tuning, Distillation, Domain Adaptation
- **Foundation:** Foundation Model 직접 개발·운영

Sovereignty는 Supporting Capability이며 CAMP Stage의 필수조건이 아닙니다.

### 자주 묻는 질문
- **Higgsfield 같은 전문 AI?** 중요합니다. General Agent가 Tool로 호출할 수 있으면 더 강합니다.
- **Dashboard 안 Chatbot?** 대부분 AI-enabled Application에 가깝습니다.
- **SKILL.md가 꼭 필요한가?** 아닙니다. 복잡하고 반복되며 복제 가치가 커질수록 중요합니다.
- **RAG는 낡았나?** 아닙니다. Context Infrastructure이며 다음 단계는 `RAG → 판단 → Tool → Action`입니다.
- **내부 MCP Server는 중요한가?** 네. 운영 중인 MCP/API는 강한 Stage 3 Evidence입니다.
- **Data Lake는 여전히 중요한가?** 네. 기존 Pipeline, Metadata, Governance, Access Control은 Agent 연결을 가속합니다.
- **Vibe Coding은 AX인가?** 생산성에는 중요하지만 사람용 UI 증가와 Agent 실행능력 증가는 구분해야 합니다.
