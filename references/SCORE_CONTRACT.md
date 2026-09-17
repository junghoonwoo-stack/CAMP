# CAMP Score Contract

This file defines the stable scoring boundary for CAMP 1.x. Question wording may evolve as enterprise AI evolves; the score shape must not drift silently.

## English

### 1. Fixed 100-point structure

CAMP 1.x always uses five scored dimensions, each worth 20 points:

1. **AI Access** — how broadly people in the assessed scope repeatedly use approved AI for real work.
2. **AI Delegation** — how much real work people can delegate to AI, from assistance to agent-first execution.
3. **Enterprise Connection** — how well AI can consume governed company context and use company tools/systems.
4. **Knowledge Compounding** — whether useful instructions, decisions, sessions, and outcomes become reusable organizational assets.
5. **Role Transformation** — whether AI augments and replicates capable people, reduces handoffs, and changes responsibility or organization design.

Each dimension is scored only as `0 / 5 / 10 / 15 / 20`. The total is always **CAMP Score /100**.

### 2. Questions are evidence probes, not new score buckets

The interview may add, remove, or refine short questions as technology changes. A new probe does **not** create extra points. Probes exist to decide which existing 0/5/10/15/20 anchor is actually supported.

Examples:
- metadata and data-mart operations are evidence for **Enterprise Connection**;
- MCP, plugin, API, tool distribution and lifecycle ownership are evidence for **Enterprise Connection**;
- observability, cost control, evals, permissions, workspace/filesystem controls, and computer-use policy are **AI Operations** evidence and Stage confidence gates;
- replication of a strong employee's way of working is evidence for **Knowledge Compounding** and **Role Transformation**;
- a human-facing dashboard may be valuable, but it does not by itself increase Agent maturity unless it also makes context, tools, permissions, or execution available to AI.

### 3. AI Operations is a supporting capability and a Stage gate

AI Operations does not add points above 100. It is reported separately as `Weak / Developing / Strong` and should cover:

- **Observability & cost:** user → agent → model → tool/MCP → result, plus usage, latency, and cost.
- **Quality & eval:** risk-tiered checks for task success, groundedness, correctness, correction rate, and domain-specific failure.
- **Runtime security:** identity, least privilege, data sensitivity, approval, workspace/filesystem permissions, computer use, and action policy.
- **Operating ownership:** clear teams/processes for data pipelines and metadata, MCP/plugin/tool lifecycle, AI platform runtime, security review, and incident response.

Not every low-risk AI use needs heavy evals. For a core value chain, customer-facing process, regulated decision, or action that can materially harm the business or a customer, strong eval and runtime controls are expected.

A scope should not receive a high-confidence Stage 4–5 diagnosis when critical AI workflows cannot be operated safely or their failures cannot be detected.

### 4. AI-facing transformation rule

CAMP distinguishes **systems made for people to use** from **capabilities that let AI work**.

Human-facing IT can still be necessary and valuable. But CAMP gives stronger AX credit when work makes the company more legible and executable to AI: governed data and metadata, searchable context, APIs/MCP/plugins/tools, permissions, action paths, reusable skills, memory, evals, and runtime controls.

A useful test is:

1. Does this investment increase what AI can understand, decide, or do?
2. Would a better foundation model naturally make the capability more useful?
3. Is the organization building reusable context/harness instead of only another screen or workflow for a person?

If the answer to all three is No, classify it as valuable IT or AI-made IT rather than core Agent Transformation.

### 5. Versioning rule

Within **CAMP 1.x**:

- the five dimension names and 20-point weights remain fixed;
- total score remains /100;
- existing benchmark records remain comparable at the dimension level;
- wording, examples, probes, and Stage evidence requirements may become more precise;
- any change to dimension definitions or weights requires a new major score contract and benchmark cohort separation.

Do not silently recalculate historical submissions under a materially different score contract.

---

## 한국어

### 1. 100점 구조는 고정함

CAMP 1.x의 점수는 항상 5개 영역 × 20점으로 구성함.

1. **AI Access** — 진단 범위의 구성원들이 승인된 AI를 실제 업무에 얼마나 널리 반복 사용하고 있는가.
2. **AI Delegation** — 보조 수준을 넘어 실제 일을 AI에게 어디까지 맡길 수 있는가.
3. **Enterprise Connection** — AI가 회사의 관리된 Context를 읽고 회사의 Tool/System을 사용할 수 있는가.
4. **Knowledge Compounding** — 좋은 지시, 판단, Session, 결과가 다음 사람과 Agent가 다시 쓸 수 있는 조직 자산으로 남는가.
5. **Role Transformation** — AI가 개인을 증강·복제하고 Handoff를 줄이며 책임·역할·조직 설계를 바꾸는가.

각 영역은 `0 / 5 / 10 / 15 / 20`만 사용하며 총점은 항상 **100점**임.

### 2. 질문은 점수항목이 아니라 Evidence Probe임

기술과 업무환경이 바뀌면 질문은 추가·삭제·정교화할 수 있음. 그러나 질문 하나가 새 점수를 만드는 것은 아님. 추가 질문은 기존 5개 영역에서 어느 점수 Anchor가 실제로 성립하는지를 확인하기 위한 근거임.

예를 들면:
- Data Mart, Pipeline, Metadata 운영역량은 **Enterprise Connection**의 근거임.
- MCP, Plugin, API, Tool을 만들고 배포·운영하는 조직과 Lifecycle은 **Enterprise Connection**의 근거임.
- Observability, 비용, Eval, 권한, Workspace/File System, Computer Use 통제는 **AI Operations** 근거이며 높은 Stage의 Confidence Gate임.
- 뛰어난 개인의 일하는 방식을 다른 사람/Agent가 재사용하도록 만드는 것은 **Knowledge Compounding**과 **Role Transformation**의 근거임.
- 사람이 보기 위한 Dashboard는 필요할 수 있지만, 그 자체로는 Agent Maturity를 높이지 않음. Data, Context, Tool, Permission, Execution을 AI에 열어줄 때 AX 근거가 됨.

### 3. AI Operations는 별도 역량이며 높은 Stage의 Gate임

AI Operations는 100점을 넘는 가산점이 아님. `Weak / Developing / Strong`으로 별도 보고하며 다음을 봄.

- **Observability & Cost:** User → Agent → Model → Tool/MCP → Result 흐름, 사용량, Latency, 비용을 볼 수 있는가.
- **Quality & Eval:** 업무 위험도에 따라 Task Success, 정답성, Groundedness, 수정률, Domain Failure를 확인하는가.
- **Runtime Security:** Identity, Least Privilege, Data Sensitivity, Approval, Workspace/File System 권한, Computer Use, Action Policy를 운영하는가.
- **Operating Ownership:** Data Pipeline/Metadata, MCP·Plugin·Tool Lifecycle, AI Platform Runtime, Security Review, Incident Response를 담당하는 조직과 프로세스가 있는가.

모든 저위험 AI 사용에 강한 Eval이 필요한 것은 아님. 그러나 Core Value Chain, 고객접점, 규제 대상 판단, 또는 잘못되면 사업·고객에 큰 위험을 주는 업무에는 강한 Eval과 Runtime Control이 필요함.

핵심 AI 업무의 실패를 발견할 수 없거나 안전하게 운영할 수 없다면 Stage 4–5를 높은 Confidence로 부여하지 않음.

### 4. AI-facing Transformation 원칙

CAMP는 **사람이 쓰기 위한 시스템을 하나 더 만드는 것**과 **AI가 회사에서 일을 더 잘하도록 만드는 것**을 구분함.

Human-facing IT도 필요하고 가치가 있을 수 있음. 그러나 CAMP에서 더 강한 AX 근거는 회사를 AI가 읽고 실행할 수 있게 만드는 활동임. 예: 관리된 Data/Metadata, 검색 가능한 Context, API/MCP/Plugin/Tool, Permission, Action Path, 재사용 Skill, Memory, Eval, Runtime Control.

간단한 판별 질문은 다음과 같음.

1. 이 투자가 AI가 이해·판단·실행할 수 있는 범위를 넓히는가?
2. Foundation Model이 좋아질수록 이 Capability도 자연스럽게 더 좋아지는가?
3. 사람용 화면 하나를 더 만드는 대신 재사용 가능한 Context/Harness를 만드는가?

세 질문이 모두 No라면 가치 있는 IT일 수는 있지만 Core Agent Transformation과는 구분함.

### 5. Versioning 원칙

**CAMP 1.x**에서는:

- 5개 Dimension 이름과 각 20점 Weight를 고정함.
- 총점은 항상 /100으로 유지함.
- 기존 Benchmark Record와 Dimension Level 비교 가능성을 유지함.
- 질문 문구, 예시, Probe, Stage Evidence 기준은 더 정교하게 개선할 수 있음.
- Dimension 정의나 Weight를 바꾸려면 Major Score Contract를 새로 만들고 Benchmark Cohort를 분리해야 함.

실질적으로 다른 Score Contract로 과거 Submission을 조용히 재계산하지 않음.