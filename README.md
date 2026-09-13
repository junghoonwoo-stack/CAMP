# CAMP

**CAMP — Company Agent Maturity Profile**

> Diagnose how agent-native your organization really is — and what to do next.

한국어: **CAMP — 우리 회사 AX 진단**  
English: **CAMP — Agent-Native Company Assessment**

CAMP는 기업이 AI를 몇 개 도입했는지가 아니라, **AI Agent에게 실제 업무를 얼마나 맡길 수 있고, 그 능력이 회사의 데이터·도구·지식·조직 구조와 얼마나 연결되어 있는지**를 진단합니다.

## 10분이면 됩니다

CAMP는 보통 **약 10분**의 대화형 진단입니다.

몇 가지 객관식/짧은 질문에 답하면 다음을 받습니다.

- **CAMP Stage** — 현재 조직의 Agent-native 위치
- **CAMP Score / 100** — 다섯 핵심 축의 균형
- **가장 큰 병목** — 다음 단계로 가지 못하게 하는 한 가지
- **다음 90일 Top 3** — 우선 Action
- **추천 AX 과제** — 실제 추진할 프로젝트
- **Stop Doing** — 지금 줄이거나 중단할 것
- **AI Operations / Sovereign AI** — 운영 및 모델 통제 역량
- **CAMP Report** — 최종 진단 리포트

가능한 환경에서는 객관식 질문을 선택형 UI로 제공하며, 그렇지 않으면 `A/B/C/D/E`처럼 짧게 답할 수 있습니다.

## 먼저 조직을 이해합니다

진단 전에 다음 Profile을 확인합니다.

- 회사 전체 / 사업부·본부 / 팀 / 신설 AI-native 조직 중 무엇을 진단하는지
- 국가
- 업종
- 진단 대상 인원 구간
- 주요 Function

회사명은 꼭 필요하지 않으면 묻지 않습니다.

## 두 가지 진단 방식

### Interview Mode
자료가 없어도 됩니다. CAMP가 필요한 질문을 한 번에 하나씩 물어봅니다. 보통 7~12개 질문이면 충분합니다.

### Evidence Mode
AX 제안서, Agent 정의, RAG/MCP Architecture, Skill, 사용로그, 조직자료 등을 제공하면 먼저 읽습니다. 이미 자료에서 확인된 질문은 건너뛰고, 판정에 필요한 Gap만 추가 질문합니다.

## CAMP Stage

| Stage | 이름 | 핵심 |
|---|---|---|
| 0 | No AI | 업무용 AI 접근 자체가 거의 없음 |
| 1 | AI Access | AI가 일부 사용자/기능에만 제공됨 |
| 2 | AI Workforce | 개인이 General Agent에게 실제 일을 맡김 |
| 3 | Connected AI | Agent가 사내 RAG, Data, MCP/API, 업무시스템과 연결됨 |
| 4 | Compounding AI | Skill, Session, Context가 조직 자산으로 축적·재사용됨 |
| 5 | AI-Native Company | 역할·Handoff·조직 구조가 AI를 전제로 재설계됨 |

Stage는 반드시 순서대로 밟을 필요가 없습니다. AI-native startup은 설립 초기부터 Stage 4~5의 Operating Model을 가질 수 있습니다.

## CAMP Score — 0~100

5개 핵심 Dimension을 각각 20점으로 평가합니다.

| Dimension | 질문 |
|---|---|
| AI Access | 개인에게 AI가 얼마나 넓고 충분하게 제공되는가? |
| AI Delegation | 질문을 넘어 실제 업무를 Agent에게 얼마나 맡기는가? |
| Enterprise Connection | Agent가 회사 Context/Data/Tool/System을 사용하는가? |
| Knowledge Compounding | Skill/Session/Context가 조직 자산으로 남는가? |
| Role Transformation | AI가 Handoff, 역할, 조직 구조를 실제로 바꾸는가? |

Stage와 Score는 같은 것이 아닙니다. Stage는 Operating Model의 질적 위치이고, Score는 다섯 축의 균형을 보여줍니다.

## Agent Test

> **Agent = Model + Context + Harness**

모든 AX 과제를 두 질문으로 먼저 봅니다.

1. **AI 모델이 좋아질수록 이 시스템의 업무 수행 능력도 자연스럽게 좋아지는가?**
2. **현재 개발이 AI가 일을 더 잘하도록 Context, Data, Tool, Skill, Permission, Runtime 등을 강화하는가?**

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**입니다. 가치가 없다는 뜻은 아니지만 Agent Transformation과는 구분합니다.

## Supporting Capabilities

### AI Operations
**Visibility · Cost · Quality · Security**

> **보이지 않는 AI는 운영할 수 없습니다.**

### Sovereign AI
`External API → Multi-model Portfolio → Private/Local → Post-training → Foundation Model`

자체 모델이 없어도 높은 CAMP Stage가 가능하며, Foundation Model이 있어도 조직의 Agent 활용이 낮다면 CAMP Stage는 낮을 수 있습니다.

## Opt-in CAMP Benchmark

진단이 끝나면 CAMP Score를 Benchmark에 공유할지 **별도로 동의**를 받습니다.

동의하면 회사명이나 내부 과제명이 아니라 국가·업종·규모 구간·Function·Stage·Score 같은 최소 정보만 공유합니다. 충분한 표본이 쌓이면 전체 및 가능하면 국가·업종·규모별 percentile을 보여줍니다.

- 전체 N < 10이면 순위를 제공하지 않습니다.
- 세부 그룹도 N >= 10일 때만 percentile을 제공합니다.
- GitHub Issue 방식으로 공유하면 제출자의 GitHub 계정은 공개될 수 있습니다.
- 동의하지 않으면 Benchmark에 아무 정보도 기록하지 않습니다.

Benchmark 제출은 Repository의 **CAMP Benchmark Submission** Issue Form을 사용합니다.

## Repository 구조

- `SKILL.md` — CAMP 진단 Agent 지침
- `QUESTIONNAIRE.md` — 약 10분 대화형 질문지
- `PLAYBOOK.md` — Stage/Agent/Operations/Sovereign/과제 리뷰 기준
- `REPORT_TEMPLATE.md` — CAMP Report 및 Score 기준
- `benchmark/` — Opt-in Benchmark 규칙과 데이터 구조
- `.github/ISSUE_TEMPLATE/camp-benchmark.yml` — 선택형 Benchmark 제출 Form
- `examples/sample-assessment.md` — 결과 예시

## 철학

> **좋은 AX는 AI 시스템을 많이 만드는 것이 아닙니다.**
>
> 모든 개인에게 강력한 AI를 주고, AI가 회사의 Context와 Tool을 사용할 수 있게 하고, 개인의 Skill과 Session Knowledge를 조직 전체의 Intelligence로 축적하며, 그 결과 사람의 역할과 조직 구조를 다시 설계하는 것입니다.
