# CAMP Report Template

Use [SCORE_CONTRACT.md](SCORE_CONTRACT.md) for the stable five-dimension /100 score. A participant's **private report may show their own company and scope name**. Every other organization in CAMP Bench remains anonymous. For a public/shared report, anonymize the participant's own company by default unless they explicitly request otherwise.

## English

### Executive result
- Organization / exact assessed scope
- Respondent perspective category
- CAMP Stage + Confidence
- **CAMP Score /100**
- one-line diagnosis
- biggest bottleneck
- one-line **AI-facing direction** diagnosis: is transformation energy mainly making work easier for people to operate, or making the company easier for AI to understand and execute?

### Five dimensions

| Dimension | Score | Interpretation |
|---|---:|---|
| AI Access | /20 | |
| AI Delegation | /20 | |
| Enterprise Connection | /20 | |
| Knowledge Compounding | /20 | |
| Role Transformation | /20 | |
| **Total** | **/100** | |

Always explain:
- strongest 1–2 dimensions and why
- weakest 1–2 dimensions and why
- major gaps or imbalance
- what the pattern implies for the next CAMP Stage
- when relevant, the difference between the strongest proven core case and adoption across the full assessed scope
- whether current AX investment is mainly **human-facing IT** or **AI-facing infrastructure/capability**

### Enterprise connection evidence

Summarize what makes company knowledge and systems usable by AI:
- governed data marts/pipelines
- definitions, ownership, freshness, access control, and machine-readable metadata
- document/search/RAG context
- reusable MCP/API/plugin/connector/tool services
- read/write/action permissions and approvals
- named operating team/process for connector lifecycle

Do not require every item. Explain the bottleneck that prevents the next anchor.

### Knowledge and replication evidence

Explain whether:
- useful prompts/instructions/skills are shared and versioned
- sessions, decisions, corrections, and outcomes survive beyond one chat
- a strong employee's way of doing important work can be packaged and reused by other people or agents
- the next person/agent starts from accumulated organizational knowledge instead of from zero

### Role transformation evidence

Describe the concrete change in work:
- same role, faster
- adjacent work absorbed by one person
- fewer handoffs between teams
- strong individual capability replicated through AI
- R&R/team/workforce design changed around AI delegation

A new dashboard, portal, or workflow by itself is not Role Transformation.

### AI Operations

Report **Overall AI Operations: Weak / Developing / Strong**, then give a short breakdown:

| Area | Finding |
|---|---|
| Observability & cost | User → Agent → Model → Tool/MCP → Result visibility; usage, latency, cost where useful |
| Quality & eval | risk-tiered task success / correctness / groundedness / domain tests, especially for core value-chain or customer-risk work |
| Runtime security | identity, least privilege, sensitive-data handling, approvals, workspace/filesystem/computer-use controls, logging |
| Operating ownership | data/metadata owner, MCP/tool lifecycle owner, AI platform owner, cybersecurity review, incident response |

Not every low-risk assistant needs heavy evals. Explicitly call out critical workflows where a wrong answer/action could materially harm the business or a customer and whether the control level matches that consequence.

### Action
- next 90 days: Top 3 actions + success signals
- recommended projects
- Stop Doing
- AI Operations gaps
- Sovereign AI
- next Stage target + evidence required

Prefer actions that increase what AI can understand, decide, or do: governed data/metadata, reusable tools, permissioned action paths, skills, evals, runtime controls, and replication of strong employee workflows. Do not default to building another dashboard unless the business need is genuinely human-facing.

### Same-company analysis
If multiple assessments resolve to the same private Organization Group ID, also show:
- organization/scope mean and median
- score distribution and range
- team / scope / function differences
- dimensions with the largest disagreement
- role-level perception gaps when sample size supports them
- longitudinal movement when repeat assessments exist

Never show individual respondent identity.

### CAMP Bench
When the assessment is submitted and sample size is sufficient, show:
- Overall percentile
- Industry percentile
- Peer Group percentile
- benchmark distribution with the participant's organization highlighted
- five-dimension comparison against the selected cohorts
- relative strengths and weaknesses
- prior-period movement when available

**Peer Group** = similar anonymous organizations by broad industry segment, size, country/region, scope, and function. If N < 10 organizations, broaden the cohort or show `Insufficient sample`.

The participant may see their own company name. Other participant organizations and scores remain anonymized. Named-company comparisons may use only public evidence or data explicitly authorized for named disclosure.

---

## 한국어

[SCORE_CONTRACT.md](SCORE_CONTRACT.md)를 고정된 5개 영역 /100점 기준으로 사용함. 참여자의 **Private Report에는 본인 회사/Scope 이름을 표시할 수 있음.** CAMP Bench의 다른 회사는 모두 익명화함. 외부 공유용 Report는 사용자가 요청하지 않는 한 본인 회사도 기본 익명화함.

### 핵심 결과
- 조직 / 정확한 진단 범위
- 응답자 관점 범주
- CAMP Stage + Confidence
- **CAMP 총점 /100**
- 한 줄 진단
- 가장 큰 병목
- 한 줄 **AI-facing 방향 진단**: 혁신 에너지가 사람이 시스템을 더 잘 쓰게 만드는 쪽인지, 회사가 AI에게 더 잘 읽히고 실행되게 만드는 쪽인지

### 5개 영역 분석

| Dimension | Score | 해석 |
|---|---:|---|
| AI Access | /20 | |
| AI Delegation | /20 | |
| Enterprise Connection | /20 | |
| Knowledge Compounding | /20 | |
| Role Transformation | /20 | |
| **Total** | **/100** | |

항상 다음을 해석함.
- 가장 강한 1~2개 영역과 이유
- 가장 약한 1~2개 영역과 이유
- 영역 간 큰 Gap / 불균형
- 이 패턴이 다음 CAMP Stage에 의미하는 것
- 필요한 경우 핵심 조직의 가장 앞선 운영사례와 진단 범위 전체 보급 수준의 차이
- 현재 AX 투자가 주로 **Human-facing IT**인지 **AI-facing Infrastructure/Capability**인지

### Enterprise Connection Evidence

회사의 지식과 시스템이 AI에게 실제로 얼마나 사용 가능한지 정리함.
- 관리되는 Data Mart/Pipeline
- Definition, Owner, Freshness, Access Control, AI가 읽을 수 있는 Metadata
- 문서/Search/RAG Context
- 재사용 MCP/API/Plugin/Connector/Tool Service
- Read/Write/Action Permission과 Approval
- Connector Lifecycle을 운영하는 담당 조직/절차

모든 항목이 있어야 하는 것은 아님. 다음 점수 Anchor를 막는 병목을 설명함.

### Knowledge & Replication Evidence

다음을 설명함.
- 좋은 Prompt/Instruction/Skill이 공유·Version 관리되는가
- Session, 판단, 수정, 실제 결과가 한 번의 Chat 이후에도 남는가
- 일을 잘하는 구성원의 업무방식을 다른 사람/Agent가 재사용할 수 있게 Package할 수 있는가
- 다음 사람/Agent가 0이 아니라 축적된 조직지식에서 시작하는가

### Role Transformation Evidence

업무 자체가 어떻게 바뀌었는지 구체적으로 씀.
- 같은 Role에서 더 빠르게 일함
- 한 사람이 인접 전문업무까지 흡수함
- Team 간 Handoff가 줄어듦
- 뛰어난 개인의 Capability가 AI를 통해 복제됨
- AI 위임을 기준으로 R&R/Team/인력설계를 바꿈

새 Dashboard, Portal, Workflow만 만든 것은 Role Transformation으로 보지 않음.

### AI Operations

**Overall AI Operations: Weak / Developing / Strong**을 표시한 뒤 간단히 분해함.

| 영역 | 확인 내용 |
|---|---|
| Observability & Cost | User → Agent → Model → Tool/MCP → Result 흐름, 필요한 Usage/Latency/Cost 가시성 |
| Quality & Eval | 위험도에 맞춘 Task Success/정답성/Groundedness/Domain Test, 특히 Core Value Chain·고객위험 업무 |
| Runtime Security | Identity, Least Privilege, Sensitive Data, Approval, Workspace/File System/Computer Use Control, Logging |
| Operating Ownership | Data/Metadata Owner, MCP/Tool Lifecycle Owner, AI Platform Owner, Cybersecurity Review, Incident Response |

모든 저위험 Assistant에 강한 Eval이 필요한 것은 아님. 오답/오작동이 사업 또는 고객에 큰 피해를 줄 수 있는 핵심 Workflow를 명확히 지적하고 현재 Control이 그 위험에 맞는지 평가함.

### Action
- 향후 90일 Top 3 Action + Success Signal
- 추천 과제
- Stop Doing
- AI Operations Gap
- Sovereign AI
- 다음 Stage 목표 + 필요한 Evidence

가능하면 AI가 이해·판단·실행할 수 있는 범위를 늘리는 Action을 우선함. 예: 관리된 Data/Metadata, 재사용 Tool, Permission이 있는 Action Path, Skill, Eval, Runtime Control, 뛰어난 개인 Workflow의 복제. 실제 Business Need가 사람용 UI가 아니라면 Dashboard를 기본 처방으로 제안하지 않음.

### 같은 회사의 여러 응답
Private Organization Group ID가 같은 진단이 여러 개면 다음도 보여줌.
- 조직/Scope 평균·중앙값
- 점수 분포와 범위
- 팀 / Scope / Function별 차이
- 의견 차이가 가장 큰 영역
- 표본이 충분하면 Role Level별 인식 차이
- 반복 진단이 있으면 시계열 변화

개별 응답자 Identity는 표시하지 않음.

### CAMP Bench
진단 결과가 제출됐고 표본이 충분하면 다음을 보여줌.
- Overall Percentile
- Industry Percentile
- Peer Group Percentile
- 분포에서 본인 조직 위치 Highlight
- 선택 Cohort 대비 5개 영역 비교
- Peer 대비 상대적 강점 / 약점
- 가능하면 과거 대비 변화

**Peer Group** = Industry Segment, 규모, 국가/지역, Scope, Function이 유사한 익명 조직군임. Cohort가 10개 조직 미만이면 더 넓은 그룹으로 비교하거나 `표본 부족`으로 표시함.

참여자는 자기 회사명을 볼 수 있지만 다른 참여기업의 회사명과 개별 점수는 익명화함. Named Company 비교는 공개 Evidence 또는 명시적으로 허용된 데이터만 사용함.