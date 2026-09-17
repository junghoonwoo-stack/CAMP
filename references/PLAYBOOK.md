# CAMP Diagnostic Playbook

Use [SCORE_CONTRACT.md](SCORE_CONTRACT.md) as the scoring boundary. CAMP 1.x keeps the same five scored dimensions and the same 100-point total; this playbook explains what evidence is strong enough to support the upper anchors.

## English

### Evidence rule
Do not raise an organization’s Stage based on one power user, demo, or pilot.

- **Anecdotal:** one user/project
- **Repeated:** repeated across users/teams
- **Operationalized:** owner, process, metrics, recurring real-work use
- **Institutionalized:** default way of working

Plans and proposals do not count as current capability.

### Scope and flagship-case rule

Confirm the assessed scope before scoring: entire company, business unit/division, team/department, or a new AI-native organization. Every answer refers to that scope.

Keep two questions separate:

- **Does the capability exist?** A strategically important, recurring case in a core organization can establish that it does, even before broad rollout.
- **How widely is it adopted?** AI Access measures coverage across the assessed population. A flagship case must not be described as company-wide adoption.

The representative case must be real work, used repeatedly by several people, and have a responsible owner. A showcase demo, isolated power user, or unowned pilot does not qualify. In the report, state both the strongest proven capability and its actual coverage.

### Five scored dimensions

The five dimensions remain fixed at 20 points each.

**AI Access**
- Count real recurring users, not licenses or accounts.
- Do not infer broad adoption from a flagship team.

**AI Delegation**
- Distinguish asking AI for information from delegating a complete piece of work.
- A person-facing dashboard, form, or workflow built faster with AI is not automatically higher delegation.
- Higher anchors require AI itself to consume context, reason, use tools, and produce or execute meaningful work.

**Enterprise Connection**
- Treat data readiness and tool connectivity as one operating capability.
- Files/RAG are useful but lower evidence than governed live data and business-system access.
- Upper anchors require recurring, managed connections to enterprise data/tools, not a personal one-off script.
- Look for data pipelines/data marts with clear definitions, metadata, ownership, freshness, access control, and machine-readable descriptions.
- Look for an organization/process that builds, approves, distributes, versions, monitors, and retires MCP servers, plugins, APIs, or agent tools.
- Read/write/action capability must respect identity, least privilege, approvals, and auditability.

**Knowledge Compounding**
- Personal prompts are not organizational compounding.
- Strong evidence includes reusable skills/instructions, versioning, owners, evaluation, distribution, session/decision capture, and feedback from outcomes.
- The key question is whether the next person or agent starts from accumulated organizational knowledge instead of from zero.

**Role Transformation**
- Productivity inside the same role is useful but is not the endpoint.
- Strong evidence means AI lets a capable person cover adjacent work, packages that person’s way of working so others can reproduce it, reduces handoffs, and eventually changes R&R or organization design.
- Building another system for a person to operate is not enough by itself. CAMP looks for augmentation and replication of people through AI.

### AI-facing vs human-facing transformation

Ask where transformation energy is going.

**Human-facing:** more dashboards, portals, workflow screens, manual review queues, or systems people must learn to operate.

**AI-facing:** governed data/metadata, searchable context, APIs/MCP/plugins/tools, permissions, reusable skills, memory, action paths, evals, and runtime controls that let AI understand or execute company work.

Human-facing systems can still be necessary. The AX distinction is whether the investment increases AI's ability to understand, decide, or act. A data mart with strong metadata exposed safely to agents can be more AX-relevant than a polished dashboard built only for people.

### AI Operations

AI Operations is a supporting capability, not a sixth score dimension. It is a Stage confidence gate and should be assessed through four lenses.

1. **Observability & cost** — Can the organization trace `User → Agent → Model → Tool/MCP → Result` and see latency, token/cache/model usage, team/user usage, and cost where useful?
2. **Quality & eval** — Are important workflows checked against task-specific success criteria? For core value chains, customer risk, regulated decisions, or material business impact, are evals strong enough to catch dangerous failure modes?
3. **Runtime security** — Before AI reads files, uses a workspace, controls a PC, invokes computer use, or writes to a system, has the risk been reviewed and translated into allow/deny/approval rules, least privilege, logging, and incident response?
4. **Operating ownership** — Is there a clear team/process for AI platform runtime, connector/MCP/plugin lifecycle, data/metadata readiness, cybersecurity review, and production support?

Not every low-risk assistant needs the same control depth. Apply controls by consequence. But high-impact workflows cannot be considered mature if the organization cannot detect failures or constrain unsafe actions.

Summarize AI Operations as:
- **Weak:** mostly ad hoc; limited visibility, quality checks, permission design, or ownership.
- **Developing:** some shared platform/owners and controls; important gaps remain or coverage is inconsistent.
- **Strong:** critical workflows have trace/cost visibility, risk-tiered evals, explicit permission/runtime controls, named owners, and incident/continuous-improvement processes.

A high-confidence Stage 4–5 diagnosis should normally require at least Developing AI Operations; for critical write/action workflows, Strong controls should exist around the risky path.

### Organization/process evidence for non-specialist respondents

A respondent does not need to know the implementation detail. Accept organizational evidence such as:
- “There is a data platform team that owns marts, definitions, metadata and access.”
- “There is a team/process to publish and operate MCP servers or agent tools.”
- “Cybersecurity reviews workspace/filesystem/computer-use permissions and defines what is allowed.”
- “The AI platform team monitors model/tool calls, cost and failures.”
- “Core workflows have a test set or quality owner before changes are released.”

When a respondent says “not sure,” ask whether such a team/process exists rather than forcing technical terminology.

### AX project types
- AI-made IT
- AI-enabled application
- Agent
- Agent enabler: data / metadata / RAG / MCP / API / permission / runtime / search
- Knowledge & skill: skill / session / memory / context compounding
- Organization transformation
- AI operations
- Model / sovereign infrastructure

For each project ask:
1. Does it move the organization to a higher CAMP Stage?
2. Does it increase what AI can understand, decide, or do?
3. Does it pass the Agent Test?
4. Can an individual’s productivity or way of working be replicated?
5. Does new knowledge survive into future agents?
6. Does it reduce role boundaries or handoffs?
7. Can cost, quality, usage, permissions, and risk be operated?

Decision: **Continue / Refocus / Merge / Stop**.

### Sovereign AI
- **API:** external SaaS/API
- **Portfolio:** multi-model routing
- **Private:** open-weight, private/local inference, own GPU/API
- **Post-trained:** LoRA, fine-tuning, distillation, domain adaptation
- **Foundation:** pre-training and operating a foundation model

Sovereignty is a supporting capability, not a CAMP Stage requirement. Judge it against cost, security, latency, domain quality, and strategic control rather than assuming more sovereignty is always better.

### Common questions
- **Specialized AI tools such as Higgsfield?** Valuable, but stronger when a general agent can call them as tools.
- **Chatbot inside a dashboard?** Usually an AI-enabled application unless it can use meaningful context/tools and complete work.
- **Is SKILL.md mandatory?** No. It matters when work becomes complex, repeatable, and worth replicating.
- **Is RAG obsolete?** No. It is context infrastructure; the next step is `RAG → reasoning → tool → action`.
- **Is an internal MCP server meaningful?** Yes. A recurring, owned MCP/API service is strong Stage 3 evidence.
- **Does a data lake still matter?** Yes. Pipelines, marts, metadata, governance, freshness, and access control can be foundational Agent infrastructure.
- **Is vibe coding AX?** It can improve productivity, but distinguish software for human UI from capabilities that expand agent execution.

---

## 한국어

[SCORE_CONTRACT.md](SCORE_CONTRACT.md)를 점수의 경계로 사용함. CAMP 1.x에서는 5개 점수영역과 100점 총점을 고정하고, 이 Playbook은 높은 점수를 인정할 수 있는 Evidence를 더 구체화함.

### Evidence 원칙
Power User 한 명, Demo 하나, Pilot 하나만으로 조직 Stage를 높이지 않음.

- **Anecdotal:** 한 명/한 프로젝트
- **Repeated:** 여러 사용자/팀에서 반복
- **Operationalized:** Owner, Process, Metric, 실제 업무 반복 운영
- **Institutionalized:** 기본 업무방식

계획·제안 단계는 현재 Capability로 계산하지 않음.

### 진단 범위와 대표사례 원칙

채점 전에 회사 전체, 사업부·본부, 팀·부서, 신설 AI 중심 조직 중 어디를 진단하는지 확정함. 이후 모든 답변은 그 범위만을 기준으로 함.

다음 두 가지를 분리해서 봄.

- **그 역량이 실제로 존재하는가?** 핵심 조직이 주도하는 전략적으로 중요한 운영사례가 반복적으로 돌아간다면 전사 확산 전이라도 역량 존재의 근거가 될 수 있음.
- **얼마나 널리 보급됐는가?** 보급률은 AI Access에서 따로 측정함. 대표사례 하나를 전사 보급으로 표현하면 안 됨.

대표사례는 여러 사람이 실제 업무에서 반복 사용하고 담당자가 있어야 함. 보여주기용 Demo, 한 명의 Power User, 담당자가 없는 Pilot은 해당하지 않음. Report에는 확인된 가장 높은 역량과 실제 보급 범위를 모두 씀.

### 5개 점수영역

5개 Dimension은 계속 각 20점으로 유지함.

**AI Access**
- License나 계정이 아니라 실제 반복 사용자 비율을 봄.
- 핵심팀 사례 하나로 전사 보급을 추정하지 않음.

**AI Delegation**
- 정보를 물어보는 것과 하나의 실제 일을 맡기는 것을 구분함.
- AI로 더 빨리 만든 Dashboard, Form, Workflow가 있다는 것만으로 Delegation 점수를 높이지 않음.
- 높은 점수는 AI 자체가 Context를 읽고 판단하고 Tool을 사용해 의미 있는 결과나 실행을 만들어내는 경우임.

**Enterprise Connection**
- Data Readiness와 Tool Connectivity를 하나의 운영역량으로 봄.
- File/RAG도 중요하지만 관리되는 Live Data와 업무시스템 연결보다 낮은 Evidence임.
- 높은 점수는 개인이 임시로 만든 Script가 아니라 반복 운영되는 관리된 연결이 필요함.
- Data Pipeline/Data Mart에 정의, Metadata, Owner, Freshness, Access Control, AI가 읽을 수 있는 설명이 있는지 봄.
- MCP Server, Plugin, API, Agent Tool을 만들고 승인·배포·Version·Monitoring·폐기하는 조직/프로세스가 있는지 봄.
- Read/Write/Action은 Identity, Least Privilege, Approval, Auditability를 전제로 함.

**Knowledge Compounding**
- 개인 Prompt 저장만으로 조직의 지식축적이라고 보지 않음.
- 재사용 Skill/Instruction, Version, Owner, Eval, Distribution, Session/판단 Capture, 결과 Feedback이 강한 Evidence임.
- 다음 사람이나 Agent가 0부터 시작하지 않는지가 핵심임.

**Role Transformation**
- 기존 Role 안에서 시간을 줄이는 것도 가치 있지만 최종 목표는 아님.
- 강한 Evidence는 AI로 인접 업무까지 수행하고, 잘하는 개인의 방식이 다른 사람/Agent에게 복제되며, Handoff가 줄고, 결국 R&R이나 조직설계가 바뀌는 것임.
- 사람이 조작할 시스템 하나를 더 만드는 것만으로는 부족함. CAMP는 AI를 통한 개인의 증강과 복제를 봄.

### AI-facing vs Human-facing Transformation

혁신 에너지가 어디로 향하는지 봄.

**Human-facing:** Dashboard, Portal, Workflow Screen, 수동 Review Queue처럼 사람이 더 잘 보고 조작하도록 만드는 것.

**AI-facing:** 관리된 Data/Metadata, 검색 가능한 Context, API/MCP/Plugin/Tool, Permission, 재사용 Skill, Memory, Action Path, Eval, Runtime Control처럼 AI가 회사를 이해하고 실행하도록 만드는 것.

Human-facing 시스템도 필요할 수 있음. AX 관점의 차이는 그 투자가 AI가 이해·판단·실행할 수 있는 범위를 늘리는지임. Metadata가 잘 관리된 Data Mart를 Agent에게 안전하게 열어주는 것이 사람만 보는 멋진 Dashboard보다 AX에 더 직접적일 수 있음.

### AI Operations

AI Operations는 여섯 번째 점수항목이 아니라 Supporting Capability이며 높은 Stage의 Confidence Gate임. 네 가지로 봄.

1. **Observability & Cost** — `User → Agent → Model → Tool/MCP → Result` 흐름과 필요한 수준의 Latency, Token/Cache/Model, User/Team 사용량, 비용을 볼 수 있는가.
2. **Quality & Eval** — 중요한 업무에 업무별 성공기준이 있는가. Core Value Chain, 고객위험, 규제판단, 사업에 큰 영향을 주는 경우 위험한 실패를 잡을 수 있는 Eval이 있는가.
3. **Runtime Security** — AI가 File을 읽고 Workspace를 쓰고 PC/Computer Use를 제어하거나 시스템에 Write하기 전에 Risk Review가 되었고, Allow/Deny/Approval, Least Privilege, Logging, Incident Response로 구현되어 있는가.
4. **Operating Ownership** — AI Platform Runtime, MCP/Plugin/Connector Lifecycle, Data/Metadata Readiness, Cybersecurity Review, 운영지원에 담당 조직과 프로세스가 있는가.

모든 저위험 Assistant에 같은 수준의 통제가 필요한 것은 아님. 결과의 위험도에 따라 적용함. 그러나 고위험 업무에서 실패를 발견하지 못하고 위험한 행동을 막지 못한다면 성숙한 운영으로 보지 않음.

AI Operations 요약:
- **Weak:** 대부분 Ad hoc이며 Visibility, 품질검증, Permission 설계, Owner가 약함.
- **Developing:** 공통 Platform/Owner/Control이 일부 있으나 Coverage나 중요한 Gap이 남아 있음.
- **Strong:** 핵심 Workflow에 Trace/Cost Visibility, Risk-tiered Eval, 명시적 Permission/Runtime Control, Owner, Incident/Continuous Improvement가 있음.

Stage 4–5를 High Confidence로 판단하려면 일반적으로 AI Operations가 최소 Developing이어야 하며, 중요한 Write/Action 경로에는 위험구간을 둘러싼 Strong Control이 있어야 함.

### 일반 구성원이 답할 때의 조직/프로세스 Evidence

응답자가 구현 상세를 알 필요는 없음. 다음과 같은 조직적 Evidence를 받아들임.
- “Data Platform 조직이 Mart, Definition, Metadata, Access를 관리함.”
- “MCP Server나 Agent Tool을 배포·운영하는 팀/절차가 있음.”
- “Cybersecurity가 Workspace/File System/Computer Use 권한을 Review하고 허용범위를 정함.”
- “AI Platform 조직이 Model/Tool 호출, 비용, 실패를 Monitoring함.”
- “핵심 업무는 Release 전에 Test Set 또는 품질 Owner가 검증함.”

응답자가 “잘 모르겠다”고 하면 기술용어를 강요하지 말고 그런 담당 조직/절차가 있는지를 물음.

### AX 과제 유형
- AI-made IT
- AI-enabled Application
- Agent
- Agent Enabler: Data / Metadata / RAG / MCP / API / Permission / Runtime / Search
- Knowledge & Skill: Skill / Session / Memory / Context Compounding
- Organization Transformation
- AI Operations
- Model / Sovereign Infrastructure

각 과제에 대해 다음을 봄.
1. CAMP Stage를 실제로 높이는가?
2. AI가 이해·판단·실행할 수 있는 범위를 넓히는가?
3. Agent Test를 통과하는가?
4. 개인 생산성 또는 일하는 방식을 다른 사람/Agent에게 복제할 수 있는가?
5. 새 지식이 다음 Agent에도 남는가?
6. Role/Handoff를 줄이는가?
7. Cost, Quality, Usage, Permission, Risk를 운영할 수 있는가?

판정: **Continue / Refocus / Merge / Stop**.

### Sovereign AI
- **API:** 외부 SaaS/API
- **Portfolio:** Multi-model Routing
- **Private:** Open-weight, Private/Local Inference, 자체 GPU/API
- **Post-trained:** LoRA, Fine-tuning, Distillation, Domain Adaptation
- **Foundation:** Foundation Model 직접 개발·운영

Sovereignty는 Supporting Capability이며 CAMP Stage의 필수조건이 아님. 높을수록 무조건 좋다고 보지 않고 Cost, Security, Latency, Domain Quality, Strategic Control과 연결해서 판단함.

### 자주 묻는 질문
- **Higgsfield 같은 전문 AI?** 중요함. General Agent가 Tool로 호출할 수 있으면 더 강함.
- **Dashboard 안 Chatbot?** 의미 있는 Context/Tool을 사용해 일을 끝내지 않는다면 대부분 AI-enabled Application에 가까움.
- **SKILL.md가 꼭 필요한가?** 아님. 복잡하고 반복되며 복제 가치가 커질수록 중요함.
- **RAG는 낡았나?** 아님. Context Infrastructure이며 다음 단계는 `RAG → 판단 → Tool → Action`임.
- **내부 MCP Server는 중요한가?** 중요함. Owner가 있고 반복 운영되는 MCP/API는 강한 Stage 3 Evidence임.
- **Data Lake는 여전히 중요한가?** 중요함. Pipeline, Mart, Metadata, Governance, Freshness, Access Control은 Agent Infrastructure가 될 수 있음.
- **Vibe Coding은 AX인가?** 생산성에는 중요하지만 사람용 UI 증가와 Agent 실행능력 증가는 구분해야 함.