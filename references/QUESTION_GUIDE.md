# CAMP Interview Guide

This guide defines the participant-facing wording for Interview Mode. Keep each card short: one question, one sentence explaining why it matters, and one concrete example only when it helps.

Examples are context, not scoring evidence. Do not add a famous quote for decoration, and never invent or loosely attribute a quote. Use a named-company example only when a reliable public source supports it.

## Interview structure

The normal interview has **13 cards**: 5 setup cards followed by 8 assessment cards. Show progress on every card.

```text
Progress 4/13  ██████░░░░░░░ 31%
```

A conditional follow-up, such as the name of a business unit, stays on the same card number. In Evidence Mode, show `Confirmed n/13` as evidence resolves cards.

### Setup 1/5 — Organization

**Question:** What organization are we assessing, and in which country is it based?

**Why this matters:** The real name is used only if the participant later consents to CAMP Bench. It privately links repeat assessments from the same organization; it is not stored by CAMP before consent.

Ask for the company or organization name and country. Do not silently infer or pre-fill either field; the participant must confirm them.

### Setup 2/5 — Assessment scope

**Question:** Which part of the organization should these answers describe?

- A. Entire company
- B. Business unit or division
- C. Team or department
- D. New AI-native organization

If B–D is selected, ask for the exact business-unit, division, team, or organization label on the same card.

**Why this matters:** A score for one team and a score for the entire company mean different things. Every later question refers only to this confirmed scope.

### Setup 3/5 — Industry

**Question:** Which industry and narrower segment best describe this scope?

- Manufacturing
- Finance
- IT / SaaS
- Retail / Commerce
- Professional services
- Healthcare / Bio
- Public sector / Education
- Media / Content
- Construction / Energy
- Other

Ask for a short segment such as `Home appliances`, `Commercial banking`, or `B2B SaaS`. The industry is used for anonymous peer comparison when the cohort is large enough.

### Setup 4/5 — Size and function

**Question:** About how many people are inside the assessed scope, and what function best describes it?

Headcount: `1–10 / 11–50 / 51–200 / 201–1,000 / 1,001–5,000 / 5,000+`

Function: `Company-wide / Strategy / R&D / Software-IT / Data-AI-DX / Sales-Marketing / SCM-Manufacturing / Finance-HR-Legal / Customer Service / Other`

### Setup 5/5 — Respondent perspective

**Question:** From which role perspective are you answering?

- A. New joiner or early career (0–2 years)
- B. Junior or practitioner (3–7 years)
- C. Senior or expert (8+ years)
- D. Manager or team leader
- E. Executive or C-level
- F. Other or prefer not to say

**Why this matters:** Leaders and practitioners often see adoption differently. CAMP Bench may show role-level perception gaps only as anonymous aggregates when enough people respond. It never shows an individual's identity.

## Assessment cards

Before Q1, say: **“From here on, answer only for the scope you just confirmed.”**

### Q1 — Access to AI

**Question:** In this scope, roughly what share of people repeatedly use an approved AI tool for real work?

**Why this matters:** Buying licenses is different from people actually using AI as part of their work.

- A. Less than 5%
- B. 5–20%
- C. 21–50%
- D. 51–80%
- E. More than 80%

### Q2 — Work given to AI

**Question:** What is the most advanced kind of work people in this scope regularly give to AI?

**Why this matters:** CAMP distinguishes asking for help from trusting AI with a complete piece of work.

- A. Find information, answer questions, or summarize
- B. Draft or complete part of a task
- C. Produce a complete analysis, document, design, or code output for human review
- D. Run a recurring multi-step workflow from start to finish
- E. Starting with an AI agent is the normal way to begin work

### Q3 — Connection to company data and systems

**Question:** In the strongest real production case inside this scope, what company information or systems can AI actually use?

**Why this matters:** AI becomes more useful when it can work with the organization's context and tools, not only public knowledge.

- A. Public or external knowledge only
- B. Internal files, documents, search, or RAG
- C. Everyday collaboration tools such as Microsoft 365, Google Workspace, Slack, or Drive
- D. Core databases or business systems through APIs, MCP, ERP, PLM, or CRM
- E. It can also write back, trigger steps, or take approved actions

**Scope note:** One representative production case in a core organization may establish that this capability exists, even if it has not spread across the whole company. It must be recurring, owned, and used in real work—not a showcase demo. Q1 measures how widely it has spread; Q8 measures the strength of the evidence.

**Public reference:** BP publicly described making Microsoft 365 Copilot available to support productivity and skills, while Aker BP describes employees creating agents with Copilot Studio as a foundation for scalable automation. These illustrate different levels of access and connected execution; they do not determine the participant's score. Sources: [BP](https://www.bp.com/press-releases/bp-looks-to-leverage-power-of-generative-ai-with-copilot-for-microsoft-365) and [Microsoft customer story: Aker BP](https://www.microsoft.com/en/customers/story/24604-aker-bp-microsoft-365-copilot).

### Q4 — Reusing what works

**Question:** When someone finds a good way to work with AI, how well does it survive and help the next person or the next task?

**Why this matters:** Individual gains become organizational capability only when useful methods, decisions, and results can be found, owned, improved, and reused.

- A. It mostly disappears when the chat or session ends
- B. It remains in personal prompts or notes
- C. Useful prompts or reusable instructions are shared
- D. Shared assets have an owner, versions, quality checks, and a release process
- E. Past decisions and outcomes systematically improve future AI work

### Q5 — Changes to roles and handoffs

**Question:** How much has AI changed who does the work and how work moves between people?

**Why this matters:** Faster work inside the same job is useful, but deeper change appears when people can cover adjacent work and handoffs shrink.

- A. Roles and handoffs are essentially unchanged
- B. People do the same job faster
- C. People can take on adjacent work that previously needed another specialist
- D. Repeated handoffs or role boundaries have materially shrunk
- E. Roles, responsibilities, team design, or workforce allocation are designed around AI-first work

### Q6 — Operational visibility

**Question:** How clearly can the organization see which AI did what, used which tool, cost how much, and produced what result?

**Why this matters:** Once AI can act in business systems, quality, cost, permissions, and failures must be operable—not guessed.

- A. Little or no visibility
- B. Some usage or cost reporting
- C. Usage and cost by user, agent, and model
- D. End-to-end traces plus quality evaluation
- E. Traces, cost, quality, and runtime security or policy controls

### Q7 — Model control

**Question:** How much choice and control does the organization have over the models it uses?

**Why this matters:** This is about cost, security, latency, quality, and strategic control. A higher option is not automatically better.

- A. Mostly one external product or API
- B. Several models are selected or routed by use case
- C. Private or local open-weight models and owned compute are used
- D. Models are adapted through fine-tuning, distillation, or other post-training
- E. The organization develops and operates a foundation model

### Q8 — Evidence behind the answers

**Question:** Which statement best describes the evidence behind your strongest answers?

**Why this matters:** CAMP scores what is working now, not what is planned.

- A. One person, a demo, or a pilot
- B. A recurring production case used by several people or a core team
- C. Production use with a named owner, process, and measures
- D. The default way of working across the assessed scope

A strategic flagship case can count as B or C even before company-wide rollout. It does not prove broad adoption; Q1 still captures coverage.

---

# CAMP 인터뷰 가이드

Interview Mode에서 참여자에게 보여줄 문구를 정의합니다. 각 질문 카드는 짧게 유지합니다. 질문 하나, 필요한 이유 한 문장, 이해에 도움이 될 때만 짧은 사례 하나를 사용합니다.

사례는 설명용이지 점수 근거가 아닙니다. 장식용 유명인 인용문을 넣지 말고, 출처가 확인되지 않은 문장을 인용하지 않습니다. 회사 사례는 신뢰할 수 있는 공개 출처가 있을 때만 사용합니다.

## 인터뷰 구성

기본 인터뷰는 **총 13개 카드**입니다. 조직 정보 5개 카드 뒤에 진단 질문 8개가 이어집니다. 모든 카드에 진행률을 표시합니다.

```text
진행 4/13  ██████░░░░░░░ 31%
```

사업부명 확인 같은 조건부 추가 질문은 같은 카드 번호를 유지합니다. Evidence Mode에서는 자료로 확인된 항목을 `확인 4/13`처럼 표시합니다.

### 준비 1/5 — 회사·조직

**질문:** 어느 회사 또는 조직을 진단할까요? 국가는 어디인가요?

**왜 묻나요:** 실제 이름은 참여자가 나중에 CAMP Bench 제출에 동의한 경우에만 같은 조직의 과거 진단을 연결하는 데 비공개로 사용합니다. 동의 전에는 CAMP가 영구 저장하지 않습니다.

회사·조직명과 국가를 묻습니다. 알고 있는 정보라도 조용히 추정하거나 미리 확정하지 말고 참여자가 확인하게 합니다.

### 준비 2/5 — 진단 범위

**질문:** 이번 답변은 조직의 어느 범위를 기준으로 할까요?

- A. 회사 전체
- B. 사업부 또는 본부
- C. 팀 또는 부서
- D. 새로 만든 AI 중심 조직

B–D라면 같은 카드에서 사업부·본부·팀·조직의 정확한 이름을 확인합니다.

**왜 묻나요:** 한 팀의 점수와 회사 전체의 점수는 의미가 다릅니다. 이후 모든 질문은 여기서 확정한 범위만을 대상으로 합니다.

### 준비 3/5 — 업종

**질문:** 이 조직의 업종과 세부 분야는 무엇인가요?

- 제조
- 금융
- IT / SaaS
- 유통 / 커머스
- 전문서비스
- 헬스케어 / 바이오
- 공공 / 교육
- 미디어 / 콘텐츠
- 건설 / 에너지
- 기타

세부 분야는 `생활가전`, `상업은행`, `B2B SaaS`처럼 짧게 확인합니다. 업종은 익명 동종업계 표본이 충분할 때 비교에 사용합니다.

### 준비 4/5 — 인원과 기능

**질문:** 진단 범위 안에는 약 몇 명이 있으며, 어떤 기능에 가장 가깝나요?

인원: `1–10 / 11–50 / 51–200 / 201–1,000 / 1,001–5,000 / 5,000+`

기능: `전사 / 전략 / R&D / 소프트웨어-IT / 데이터-AI-DX / 영업-마케팅 / SCM-생산 / 재무-HR-법무 / 고객서비스 / 기타`

### 준비 5/5 — 응답자 관점

**질문:** 어떤 역할의 관점에서 답하시나요?

- A. 신입·초기 경력(0–2년)
- B. 주니어·실무자(3–7년)
- C. 시니어·전문가(8년 이상)
- D. 매니저·팀장
- E. 임원·경영진
- F. 기타·응답하지 않음

**왜 묻나요:** 경영진과 실무자는 같은 조직의 AI 활용을 다르게 볼 수 있습니다. 표본이 충분하면 CAMP Bench에서 역할별 인식 차이를 익명 집계로 보여줄 수 있습니다. 개인의 신원은 표시하지 않습니다.

## 진단 질문

Q1 전에 **“이제부터는 방금 확정한 범위만 생각하고 답해주세요.”**라고 안내합니다.

### Q1 — AI를 실제로 쓰는 사람

**질문:** 이 범위에서 승인된 AI를 실제 업무에 반복해서 쓰는 사람은 대략 어느 정도인가요?

**왜 묻나요:** 라이선스를 보유한 것과 실제 업무 습관으로 사용하는 것은 다르기 때문입니다.

- A. 5% 미만
- B. 5–20%
- C. 21–50%
- D. 51–80%
- E. 80% 초과

### Q2 — AI에게 맡기는 일

**질문:** 이 범위에서 사람들이 AI에게 반복적으로 맡기는 가장 높은 수준의 일은 무엇인가요?

**왜 묻나요:** 도움을 받는 것과, 하나의 완결된 업무를 맡기는 것은 다른 단계이기 때문입니다.

- A. 정보 찾기, 질의응답, 요약
- B. 초안이나 업무 일부 작성
- C. 사람이 검토할 완결된 분석·문서·설계·코드 산출물 작성
- D. 여러 단계로 된 반복 업무를 처음부터 끝까지 실행
- E. 업무를 시작할 때 AI Agent에게 먼저 맡기는 것이 일반적

### Q3 — 회사 자료와 시스템 연결

**질문:** 이 범위 안의 가장 앞선 실제 운영 사례에서, AI는 어떤 회사 자료나 시스템까지 사용할 수 있나요?

**왜 묻나요:** AI가 공개 지식만 쓰는 것을 넘어 조직의 맥락과 도구를 사용할 때 실제 업무 수행력이 커지기 때문입니다.

- A. 공개·외부 지식만 사용
- B. 사내 파일·문서·검색·RAG 사용
- C. Microsoft 365, Google Workspace, Slack, Drive 같은 협업도구 사용
- D. API·MCP를 통해 DB·ERP·PLM·CRM 같은 핵심 시스템 사용
- E. 조회뿐 아니라 승인된 쓰기·단계 실행·후속 조치까지 수행

**범위 기준:** 핵심 조직이 주도하는 대표적인 운영 사례 하나만 있어도 해당 역량이 존재한다고 볼 수 있습니다. 다만 반복 사용되고, 담당 조직이 있으며, 실제 업무에서 돌아가야 합니다. 보여주기용 Demo는 해당하지 않습니다. 얼마나 널리 퍼졌는지는 Q1, 근거의 강도는 Q8에서 별도로 봅니다.

**공개 사례:** BP는 Microsoft 365 Copilot을 생산성과 역량 향상에 활용한다고 공개했고, Aker BP는 구성원이 Copilot Studio로 Agent를 만들어 확장 가능한 자동화 기반을 마련한 사례를 소개했습니다. 서로 다른 수준의 접근성과 연결 실행을 설명하는 예일 뿐, 참여자의 점수를 결정하는 기준은 아닙니다. 출처: [BP](https://www.bp.com/press-releases/bp-looks-to-leverage-power-of-generative-ai-with-copilot-for-microsoft-365), [Microsoft 고객 사례: Aker BP](https://www.microsoft.com/en/customers/story/24604-aker-bp-microsoft-365-copilot).

### Q4 — 잘된 방법의 재사용

**질문:** 누군가 AI로 좋은 업무 방법을 만들었을 때, 그것이 다음 사람이나 다음 업무에도 얼마나 잘 남아 활용되나요?

**왜 묻나요:** 개인의 성과가 조직 역량이 되려면 좋은 방법·판단·결과를 찾고, 관리하고, 개선하고, 다시 쓸 수 있어야 하기 때문입니다.

- A. 대화나 작업이 끝나면 대부분 사라짐
- B. 개인 Prompt나 메모에 남음
- C. 유용한 Prompt나 재사용 지침을 함께 공유함
- D. 공용 자산에 담당자·버전·품질검사·배포 절차가 있음
- E. 과거 판단과 결과가 다음 AI 업무 품질을 체계적으로 높임

### Q5 — 역할과 업무 인계의 변화

**질문:** AI가 사람의 역할과 사람 사이의 업무 인계를 얼마나 바꾸었나요?

**왜 묻나요:** 같은 일을 빨리 하는 것도 가치가 있지만, 더 깊은 변화는 한 사람이 인접 업무까지 맡고 불필요한 인계가 줄어들 때 나타나기 때문입니다.

- A. 역할과 업무 인계가 거의 그대로임
- B. 같은 역할 안에서 일이 빨라짐
- C. 과거에는 다른 전문가가 하던 인접 업무까지 맡을 수 있음
- D. 반복적인 업무 인계나 역할 경계가 실질적으로 줄어듦
- E. 역할·책임·팀 구조·인력 배치를 AI 중심 업무에 맞춰 재설계함

### Q6 — 운영 가시성

**질문:** 어떤 AI가 어떤 도구를 써서 무슨 결과를 냈고 비용이 얼마나 들었는지 조직이 어디까지 확인할 수 있나요?

**왜 묻나요:** AI가 업무시스템에서 행동하기 시작하면 품질·비용·권한·실패를 추측이 아니라 운영할 수 있어야 하기 때문입니다.

- A. 거의 확인할 수 없음
- B. 일부 사용량 또는 비용을 확인함
- C. 사용자·Agent·Model별 사용량과 비용을 확인함
- D. 처음부터 결과까지의 실행 기록과 품질평가를 함께 봄
- E. 실행 기록·비용·품질과 실시간 보안·정책 통제를 함께 운영함

### Q7 — 모델 선택과 통제

**질문:** 회사가 사용하는 AI 모델을 얼마나 선택하고 통제할 수 있나요?

**왜 묻나요:** 비용·보안·속도·품질·전략적 통제를 보기 위한 질문입니다. 높은 선택지가 항상 더 좋은 것은 아닙니다.

- A. 주로 하나의 외부 제품이나 API 사용
- B. 업무에 따라 여러 모델을 선택하거나 연결함
- C. 사설·로컬 Open-weight 모델과 자체 연산자원을 사용함
- D. Fine-tuning·Distillation 같은 방식으로 모델을 업무에 맞춤
- E. Foundation Model을 직접 개발하고 운영함

### Q8 — 답변의 실제 근거

**질문:** 앞의 높은 답변을 뒷받침하는 실제 운영 근거는 어디에 가장 가깝나요?

**왜 묻나요:** CAMP는 계획이 아니라 지금 반복해서 작동하는 상태를 평가하기 때문입니다.

- A. 한 사람, Demo 또는 Pilot
- B. 여러 사람이 쓰는 반복적인 운영 사례 또는 핵심 팀의 대표 사례
- C. 담당자·운영절차·측정지표가 있는 실제 운영
- D. 진단 범위 전체의 기본 업무방식

전략적으로 중요한 대표 사례는 전사 확산 전이라도 B나 C가 될 수 있습니다. 다만 그 사례가 넓은 보급을 의미하지는 않으며, 보급 범위는 Q1에서 별도로 판단합니다.
