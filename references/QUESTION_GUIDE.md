# CAMP Interview Guide / 참여자 질문 가이드

Use everyday work language. Technical knowledge is not required. The interview still has **13 cards: five setup cards and eight assessment cards**. Extra checks inside a card are **evidence probes, not extra score buckets**. See [SCORE_CONTRACT.md](SCORE_CONTRACT.md).

Do not show scoring shorthand in the interview. Avoid technical words such as MCP, eval, runtime, RAG, API, or metadata unless the participant already uses them. Explain the work situation first. A non-technical respondent may answer by saying whether a responsible team or process exists.

Begin every card with `CAMP · Progress n/13 / CAMP · 진행 n/13`, a compact bar such as `███░░░░░░░░░░`, and the percentage. Ask one card at a time. Use clickable choices when available. Accept “not sure / 잘 모르겠어요”; ask one concrete organizational follow-up and then mark unknown if it remains unclear.

## Score contract for the interviewer

The five scored dimensions remain fixed at 20 points each:

1. AI Access
2. AI Delegation
3. Enterprise Connection
4. Knowledge Compounding
5. Role Transformation

Each dimension uses only `0 / 5 / 10 / 15 / 20`; total remains **/100**. Q6 AI Operations and Q7 Sovereign AI remain supporting capabilities. Same-card probes validate evidence and may prevent an unsupported upper anchor; they never add points above 100.

For Stage 4–5, weak operations around a material-risk workflow reduce confidence. A critical write/action workflow without clear quality checks or permission controls should not be described as mature merely because the agent is technically capable.

## Setup / 준비 (steps 1–5)

1. **Which company or organization, and which country? / 어느 회사나 조직을 진단할까요? 국가는 어디인가요?** These details are used only for same-company matching if the participant later submits to CAMP Bench. Do not collect personal name/email.
2. **Which part should we assess? / 회사 전체를 볼까요, 특정 본부나 팀을 볼까요?** A Whole company / 회사 전체; B Business unit or division / 사업부·본부; C Team or department / 팀·부서; D New organization built around AI / AI 중심 신설 조직. For B–D ask the scope label.
3. **What industry? / 어떤 업종인가요?** Manufacturing / 제조; Finance / 금융; IT and software / IT·소프트웨어; Retail / 유통; Professional services / 전문서비스; Healthcare / 의료·바이오; Public sector and education / 공공·교육; Media / 미디어; Construction and energy / 건설·에너지; Other / 기타. Ask one short segment such as home appliances / 생활가전.
4. **How many people and what work? / 진단할 조직은 약 몇 명이며, 주로 어떤 일을 하나요?** People: 1–10 / 11–50 / 51–200 / 201–1,000 / 1,001–5,000 / More than 5,000. Work: Multiple functions / 여러 기능; Strategy / 전략; R&D / 연구개발; Software-IT / 소프트웨어·IT; Data-AI / 데이터·AI; Sales-Marketing / 영업·마케팅; SCM-Manufacturing / 공급망·생산; Finance-HR-Legal / 재무·인사·법무; Customer Service / 고객서비스; Other / 기타.
5. **Which role are you answering from? / 어떤 역할의 입장에서 답하시나요?** A New or early-career employee / 신입·초기 경력; B Junior employee / 주니어 실무자; C Senior employee or specialist / 시니어 실무자·전문가; D Manager or team leader / 매니저·팀장; E Executive or business leader / 임원·경영진; F Other or prefer not / 기타·응답하지 않음.

Before Q1 say:

> Answer only for the scope we just confirmed. For capability questions, one important recurring case led by a core team can count if several people rely on it in real work. A one-off demo or experiment does not. We ask broad adoption separately.
>
> 지금부터는 방금 정한 조직만 기준으로 답해주세요. 역량을 묻는 질문은 핵심 조직이 운영하는 중요한 실제 사례 하나를 기준으로 답해도 됩니다. 여러 사람이 반복해서 쓰는 경우여야 하며 일회성 Demo나 시험은 제외합니다. 전체 보급률은 따로 묻습니다.

---

## English questions

### Q1 — Everyday AI use (step 6/13) · AI Access

**Roughly how many people here use approved AI regularly for real work?**

Why we ask: Count actual recurring users, not people who merely have an account or license.

- A. Fewer than 5%
- B. 5–20%
- C. 21–50%
- D. 51–80%
- E. 81% or more

Score anchor: A/B/C/D/E = 0/5/10/15/20.

### Q2 — Work AI takes on (step 7/13) · AI Delegation

**In a recurring work example, how much of the job does AI itself do?**

Why we ask: A tool that helps a person see information is different from AI completing work.

- A. Finds information, answers questions, or summarizes
- B. Drafts or helps with part of a task
- C. Completes an analysis, document, code change, or other meaningful result for a person to review
- D. Carries out connected steps using context and tools, such as checking data → preparing a result → saving or handing it off
- E. Work is normally delegated to AI first; people review, approve important steps, and handle exceptions

A human approval at an important step does not disqualify D or E.

**Same-card direction probe — do not add points:**

Which better describes most recent “AI/AX” development in the assessed scope?
- A. Mostly new dashboards, portals, screens, or workflows for people to use
- B. A mix of person-facing systems and capabilities AI can use
- C. Mostly making company data, context, tools, permissions, or actions usable by AI
- D. Not sure

Use this probe in the diagnosis. A dashboard can be valuable, but it is not automatically Agent Transformation.

### Q3 — Company data and tools (step 8/13) · Enterprise Connection

**In an important recurring example, what company information and tools can AI actually use?**

Why we ask: AI can only take on company work if the company is made legible and executable to AI.

- A. Mostly general information outside the company
- B. Company files and documents that people provide or make searchable
- C. Managed internal datasets or everyday work tools; people can reliably find the right current information
- D. Live business data or systems used for sales, product development, manufacturing, finance, etc.; a responsible team operates the connection
- E. AI can also update records or start approved actions with controlled permissions, approvals, and logs

Examples: reading a product document is B; querying a maintained data mart with definitions/ownership is C–D; looking up a live order in the order system is D; changing it after approval is E.

**Same-card data-readiness probe — do not add points:**

Is there a team/process that maintains important data for AI use — for example data marts/pipelines with clear definitions, owner, freshness, access rules, and descriptions of what the data means?
- A. No / mostly ad hoc
- B. Some important datasets
- C. Yes, for many important datasets
- D. Not sure

**Same-card connector-operations probe — do not add points:**

Is there a team/process that builds and operates reusable connections between AI and company systems — for example agent tools, connectors, MCP servers, plugins, or APIs?
- A. No / mostly individual experiments
- B. Some shared connections but ownership/process is still partial
- C. Yes, with owner, approval, versioning/monitoring, and support
- D. Not sure

Scoring note: D/E should normally have recurring managed connectivity. A personal script or one-off connector is not enough for an upper anchor.

### Q4 — Reusing what worked (step 9/13) · Knowledge Compounding

**When someone finds a good way to work with AI, can another person or agent reuse it without starting from zero?**

Why we ask: Good work should become organizational capability, not disappear with one person or one chat session.

- A. It usually disappears when the conversation ends
- B. People keep personal prompts, notes, or examples
- C. Useful instructions, examples, or work methods are shared where others can find and use them
- D. Someone owns them, versions them, checks that they still work, and distributes updates
- E. Past sessions, decisions, corrections, and outcomes systematically improve how future people/agents perform the work

**Same-card replication probe — do not add points:**

Can a strong employee’s way of doing an important task be packaged so another person or agent can reproduce much of that performance?
- A. Not really
- B. In a few cases
- C. Repeatedly for important work
- D. Not sure

### Q5 — People, handoffs, and role design (step 10/13) · Role Transformation

**Has AI changed what one person can own, or how often work must pass to another person or team?**

Why we ask: CAMP looks for augmentation and replication of people, not only another system for people to operate.

- A. Very little has changed
- B. People do the same jobs faster
- C. People can take on adjacent work that previously required another specialist
- D. A capable person’s way of working is replicated through AI and important work crosses fewer people/teams
- E. Responsibilities, team structure, R&R, or workforce allocation have been redesigned around work delegated to AI

A new dashboard, portal, or workflow alone does not establish D/E. Look for changed ownership, reduced handoffs, or replicated capability.

### Q6 — Operating AI safely and reliably (step 11/13) · Supporting capability

**For important AI work, how well can the organization see problems, check quality, and control what AI is allowed to do?**

Why we ask: More capable AI creates more operational responsibility, especially when it can access files, PCs, or business systems.

- A. Mostly ad hoc; it is hard to know what happened when something goes wrong
- B. Some usage or spending is visible, but quality and permissions are mostly handled case by case
- C. Shared owners/platforms can trace important use and costs; some quality checks and access controls exist
- D. Critical workflows have end-to-end traces and explicit quality tests/checks before or during operation
- E. D plus risk-based runtime controls: identity/least privilege, approval rules, sensitive-data policy, workspace/filesystem/computer-use controls, logging, and incident response

**Same-card quality probe — do not add score points:**

For a core value-chain or customer-risk workflow, is there a defined test set, quality owner, or repeatable evaluation that would detect a materially wrong result?
- A. No
- B. In some critical workflows
- C. Yes, where consequences justify it
- D. Not sure

**Same-card security probe — do not add score points:**

If AI can use a workspace/filesystem, control a PC, use computer automation, or write to an enterprise system, has cybersecurity/IT reviewed the risk and turned it into explicit allow/deny/approval rules?
- A. No / mostly case by case
- B. Some controls exist
- C. Yes, with a repeatable review and operating model
- D. Not sure / AI does not have those capabilities

This question does not enter the /100 score. Summarize overall AI Operations as Weak / Developing / Strong. Not every low-risk assistant needs heavy evals; critical workflows do.

### Q7 — Choosing and adapting AI (step 12/13) · Sovereign AI

**How does the organization choose or adapt the AI models it uses?**

Why we ask: Different jobs may need different tools; later choices are not automatically better.

- A. Mainly uses ready-made AI services as supplied
- B. Chooses among several AI services/models depending on the job
- C. Also runs models in computing environments the company controls
- D. Further trains or adapts existing models for particular work
- E. Builds and trains a general-purpose foundation model from the beginning

Using private company data through search or tools is covered in Q3; that alone does not mean C or D here. This question does not enter the /100 score.

### Q8 — How established the examples are (step 13/13) · Evidence basis

**How firmly are the examples you described part of everyday work?**

Why we ask: This separates capability from a demonstration or future plan.

- A. Mostly one person’s experiments, demos, or trials
- B. Several people or a core team use them repeatedly for real work
- C. There are named owners, operating steps, and results/risks are checked
- D. This is the normal way of working across the assessed scope

One important core-team case can support B or C. It does not imply broad adoption; Q1 covers that separately.

---

## 한국어 질문

### Q1 — 평소 AI 사용 (6/13) · AI Access

**이 조직에서 승인된 AI를 실제 업무에 꾸준히 쓰는 사람은 대략 어느 정도인가요?**

왜 묻나요: 계정이나 License가 있는 사람이 아니라 실제 반복 사용자를 보기 위함임.

- A. 5% 미만
- B. 5–20%
- C. 21–50%
- D. 51–80%
- E. 81% 이상

점수 Anchor: A/B/C/D/E = 0/5/10/15/20.

### Q2 — AI에게 맡기는 일 (7/13) · AI Delegation

**반복해서 하는 실제 업무를 하나 떠올리면, AI 자체가 일을 어디까지 해주나요?**

왜 묻나요: 사람이 정보를 보기 편하게 하는 시스템과 AI가 실제 일을 수행하는 것은 다르기 때문임.

- A. 정보를 찾거나 질문에 답하고 요약해줌
- B. 초안을 쓰거나 일의 일부를 도와줌
- C. 분석·문서·코드 변경 등 의미 있는 결과물 하나를 완성하고 사람이 검토함
- D. Context와 Tool을 사용해 자료 확인 → 결과 작성 → 저장/전달처럼 연결된 여러 단계를 처리함
- E. 먼저 AI에게 일을 맡기고 사람은 검토·중요 단계 승인·예외처리를 하는 것이 일반적임

중요 단계에서 사람이 승인하는 것은 D/E를 방해하지 않음.

**같은 카드 확인 질문 — 가산점 없음:**

최근 이 조직의 “AI/AX 개발”은 어느 쪽에 더 가까운가요?
- A. 사람이 보는 Dashboard, Portal, 화면, Workflow를 만드는 일이 대부분임
- B. 사람용 시스템과 AI가 사용할 Capability가 섞여 있음
- C. 회사 Data, Context, Tool, Permission, Action을 AI가 사용할 수 있게 만드는 일이 중심임
- D. 잘 모르겠음

Dashboard도 가치가 있을 수 있으나 그 자체로 Agent Transformation이라고 보지는 않음.

### Q3 — 회사 Data와 Tool 연결 (8/13) · Enterprise Connection

**중요한 실제 업무 사례에서 AI는 회사 안의 어떤 정보와 Tool을 실제로 사용할 수 있나요?**

왜 묻나요: AI에게 일을 맡기려면 회사를 AI가 읽고 실행할 수 있게 만들어야 하기 때문임.

- A. 주로 회사 밖의 일반정보만 사용함
- B. 사내 File과 문서를 읽거나 검색함
- C. 관리되는 내부 Dataset 또는 일상 업무 Tool을 사용하며, 필요한 최신 정보를 비교적 안정적으로 찾을 수 있음
- D. 영업·개발·생산·재무 등 실제 업무 Data/System을 조회하며, 이 연결을 운영하는 담당 조직이 있음
- E. 조회뿐 아니라 승인된 기록 수정/다음 Action도 수행하며 Permission·Approval·Log가 통제됨

예: 제품문서를 읽으면 B, 정의와 Owner가 관리되는 Data Mart를 조회하면 C–D, 현재 주문을 기간시스템에서 조회하면 D, 승인 후 주문을 수정하면 E임.

**같은 카드 Data 준비 확인 — 가산점 없음:**

AI가 쓸 중요한 Data를 관리하는 조직/절차가 있나요? 예: Data Mart/Pipeline의 정의, Owner, 최신성, 접근권한, Data 의미를 설명하는 Metadata를 관리함.
- A. 없음 / 대부분 Ad hoc
- B. 일부 중요한 Data에 있음
- C. 주요 Data에 비교적 체계적으로 있음
- D. 잘 모르겠음

**같은 카드 연결 운영 확인 — 가산점 없음:**

AI와 회사 시스템을 연결하는 재사용 가능한 Tool/Connector/MCP/Plugin/API 등을 만들고 운영하는 조직/절차가 있나요?
- A. 없음 / 개인 실험 중심
- B. 공용 연결이 일부 있으나 Owner/운영절차가 부분적임
- C. Owner, 승인, Version/Monitoring, 지원절차까지 있음
- D. 잘 모르겠음

채점 주의: D/E는 일반적으로 반복 운영되는 관리된 연결이 필요함. 개인 Script나 일회성 Connector만으로 높은 Anchor를 주지 않음.

### Q4 — 잘된 방법과 지식의 재사용 (9/13) · Knowledge Compounding

**누군가 AI로 일을 잘하는 방법을 찾으면, 다음 사람이나 Agent가 처음부터 다시 하지 않고 재사용할 수 있나요?**

왜 묻나요: 좋은 방식이 개인/Session에서 사라지지 않고 조직 Capability가 되는지 보기 위함임.

- A. 대화가 끝나면 대부분 사라짐
- B. 개인이 Prompt, Note, Example을 저장함
- C. 좋은 지시·예시·업무방법을 다른 사람도 찾아 쓰는 곳에 공유함
- D. 담당자가 Owner가 되어 Version을 관리하고 잘 작동하는지 확인하며 Update를 배포함
- E. 과거 Session, 판단, 수정, 실제 결과가 다음 사람/Agent의 업무 방식에 체계적으로 반영됨

**같은 카드 복제 확인 — 가산점 없음:**

일을 매우 잘하는 구성원의 중요한 업무방식을 정리해 다른 사람이나 Agent가 상당 부분 재현할 수 있나요?
- A. 거의 안 됨
- B. 일부 사례에서 가능함
- C. 중요한 업무에서 반복적으로 가능함
- D. 잘 모르겠음

### Q5 — 개인의 증강·복제와 Handoff 변화 (10/13) · Role Transformation

**AI 때문에 한 사람이 맡을 수 있는 일의 범위나, 다른 사람/팀으로 일을 넘기는 과정이 실제로 달라졌나요?**

왜 묻나요: 시스템 하나를 더 만드는 것이 아니라 사람을 증강·복제하고 일의 경계를 바꾸는지를 보기 위함임.

- A. 거의 달라지지 않음
- B. 기존 역할 안에서 같은 일을 더 빨리 함
- C. 전에는 다른 전문가에게 맡기던 인접 업무도 한 사람이 수행할 수 있음
- D. 잘하는 사람의 방식이 AI를 통해 복제되고, 중요한 일이 더 적은 사람/팀을 거쳐 끝남
- E. AI가 맡는 일을 기준으로 책임, R&R, 팀 구조 또는 인력배치를 재설계함

새 Dashboard, Portal, Workflow를 만든 것만으로 D/E로 보지 않음. 실제 Ownership 확대, Handoff 감소, Capability 복제가 있어야 함.

### Q6 — AI를 안전하고 믿을 수 있게 운영 (11/13) · Supporting Capability

**중요한 AI 업무에서 문제가 생기면 원인을 볼 수 있고, 결과 품질을 확인하며, AI가 할 수 있는 행동을 통제할 수 있나요?**

왜 묻나요: AI가 File, PC, 기간시스템까지 접근할수록 IT Infrastructure와 Cybersecurity 운영역량이 중요해지기 때문임.

- A. 대부분 Ad hoc이며 문제가 생겨도 어디서 잘못됐는지 알기 어려움
- B. 일부 사용량/비용은 보지만 품질·권한은 건별로 처리함
- C. 공통 Owner/Platform이 중요한 사용·비용 흐름을 볼 수 있고 일부 품질검증·접근통제가 있음
- D. 핵심 Workflow는 End-to-End Trace가 되고 명확한 품질 Test/Eval이 있음
- E. D에 더해 Identity/Least Privilege, Approval, 민감 Data Policy, Workspace/File System/Computer Use 통제, Logging, Incident Response까지 위험도에 맞게 운영함

**같은 카드 품질 확인 — 총점 가산 없음:**

Core Value Chain이나 고객위험 업무에서 AI가 중요한 오답을 내면 잡아낼 수 있는 Test Set, 품질 Owner 또는 반복 가능한 Eval이 있나요?
- A. 없음
- B. 일부 핵심 Workflow에 있음
- C. 위험도가 큰 업무에는 체계적으로 있음
- D. 잘 모르겠음

**같은 카드 보안 확인 — 총점 가산 없음:**

AI가 Workspace/File System을 쓰거나 PC를 제어하거나 Computer Use로 업무시스템에 접근하거나 System에 Write할 수 있다면, Cybersecurity/IT가 Risk를 Review하고 Allow/Deny/Approval 규칙으로 운영하나요?
- A. 없음 / 대부분 건별 대응
- B. 일부 Control이 있음
- C. 반복 가능한 Review와 운영체계가 있음
- D. 잘 모르겠음 / 그런 Capability를 아직 사용하지 않음

이 질문은 100점 총점에 넣지 않음. AI Operations는 Weak / Developing / Strong으로 별도 정리함. 저위험 Assistant 모두에 강한 Eval이 필요한 것은 아니지만, 잘못됐을 때 사업·고객에 큰 영향을 주는 업무에는 강한 Eval과 Runtime Control이 필요함.

### Q7 — AI 선택과 맞춤 사용 (12/13) · Sovereign AI

**이 조직은 필요한 AI Model을 어떻게 고르거나 맞춰 쓰나요?**

왜 묻나요: 업무마다 필요한 Model이 다를 수 있으며 뒤의 선택지가 무조건 좋은 것은 아니기 때문임.

- A. 주로 시중 AI 서비스를 제공된 그대로 사용함
- B. 업무에 따라 여러 AI 서비스/Model 중 적합한 것을 골라 씀
- C. 회사가 관리하는 Computing Environment에서도 Model을 직접 실행함
- D. 기존 Model에 업무사례를 추가 학습하거나 Domain에 맞게 Adaptation함
- E. 범용 Foundation Model을 처음부터 직접 만들고 학습함

사내 Data를 Search/Tool로 연결하는 것은 Q3에서 봄. 그것만으로 C/D가 되지는 않음. 이 질문은 총점에 포함하지 않음.

### Q8 — 실제 업무에 자리 잡은 정도 (13/13) · Evidence basis

**지금까지 말씀한 사례는 실제 업무에 어느 정도 자리 잡았나요?**

왜 묻나요: 시험해본 Capability와 사람들이 이미 믿고 반복 사용하는 Capability를 구분하기 위함임.

- A. 주로 개인 실험·Demo·시험 단계임
- B. 여러 사람이나 핵심 팀이 실제 업무에서 반복 사용함
- C. 명확한 Owner와 운영절차가 있고 결과·위험을 확인하며 사용함
- D. 진단할 조직 전체에서 기본적인 일하는 방식으로 자리 잡음

핵심 팀의 중요한 사례 하나라도 B/C 근거가 될 수 있으나 전사 보급을 의미하지는 않음. 보급률은 Q1에서 따로 봄.

---

## Interviewer scoring notes / 채점자 주의사항

- **Same-card probes never create additional points.** They validate the existing five dimension anchors.
- For Q3, an upper anchor should have managed data/connectivity evidence: owner, recurring operation, and appropriate permissions. Metadata and connector operations matter even if the participant does not know the technical terms.
- For Q4/Q5, distinguish a tool that helps one person from a method that can be replicated across people/agents.
- For Q5, human-facing IT alone does not establish transformation. Look for wider ownership, fewer handoffs, or redesigned roles.
- Q6 does not add points, but it affects the credibility and safety of higher Stages. Critical action/write paths without quality or security controls should be highlighted as a bottleneck.
- If the participant is non-technical, ask whether a responsible **data platform team, AI platform team, MCP/tool operations team, cybersecurity review process, or quality/eval owner** exists. Do not force implementation details.

## Finish and offer CAMP Bench / 종료 및 CAMP Bench 안내

After Q8, show the complete report, explain the private CAMP Bench comparison, and ask whether the participant wants to participate. If yes, review the fields and obtain consent before sending.

Q8 이후 완전한 Report를 보여주고 CAMP Bench 비교 혜택과 참여 여부를 묻습니다. 참여를 선택하면 전송 항목을 확인하고 동의를 받은 뒤 제출합니다.