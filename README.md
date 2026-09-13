# CAMP

**CAMP — Company Agent Maturity Profile**

> Diagnose how agent-native your company really is — and what to do next.

한국어: **CAMP — 우리 회사 AX 진단**  
English: **CAMP — Agent-Native Company Assessment**

CAMP는 기업이 AI를 몇 개 도입했는지보다, **AI Agent에게 실제 업무를 얼마나 맡길 수 있고, 그 능력이 회사의 데이터·도구·지식·조직 구조와 얼마나 연결되어 있는지**를 진단합니다.

## CAMP가 답하는 질문

- 우리 회사는 AX를 제대로 하고 있는가?
- 우리가 만든 것은 진짜 AI Agent인가, AI로 빨리 만든 기존 IT인가?
- 현재 CAMP Stage는 어디인가?
- 사내 RAG/MCP/Data Lake는 실제 Agent 역량에 얼마나 기여하는가?
- Skill/Session/Context가 조직 지식으로 축적되고 있는가?
- AI 사용이 개인 생산성 개선을 넘어 역할·직무·조직 구조 변화로 이어지는가?
- AI 비용·품질·보안·사용량을 운영할 수 있는가?
- Sovereign AI 관점에서 Model/Infra를 얼마나 통제하고 있는가?
- 현재 AX 과제 중 무엇을 계속하고 무엇을 줄여야 하는가?
- 다음 90일에 무엇을 해야 하는가?

## 두 가지 진단 방식

### 1. Interview Mode
자료가 없어도 됩니다. CAMP가 핵심 질문을 한 번에 하나씩 물어보고 현재 상태를 진단합니다.

### 2. Evidence Mode
AX 제안서, Agent 정의, RAG/MCP Architecture, Skill, 사용로그, 조직자료 등이 있으면 먼저 읽습니다.  
자료에서 확인되지 않는 핵심 Gap만 추가 질문합니다.

## CAMP Stage

| Stage | 이름 | 핵심 |
|---|---|---|
| 0 | No AI | 업무용 AI 접근 자체가 거의 없음 |
| 1 | AI Access | AI가 일부 사용자/기능에만 제공됨 |
| 2 | AI Workforce | 대부분의 개인이 General Agent에게 실제 일을 맡김 |
| 3 | Connected AI | Agent가 사내 RAG, Data, MCP/API, 업무시스템과 연결됨 |
| 4 | Compounding AI | Skill, Session, Context가 조직 자산으로 축적·재사용됨 |
| 5 | AI-Native Company | 역할·Handoff·조직 구조가 AI를 전제로 재설계됨 |

Stage는 반드시 순서대로 밟을 필요가 없습니다.  
AI-native startup은 설립 초기부터 높은 Stage의 Operating Model을 가질 수 있습니다.

## 핵심 원칙

> **Agent = Model + Context + Harness**

그리고 모든 AX 과제를 다음 두 질문으로 먼저 봅니다.

1. **AI 모델이 좋아질수록 이 시스템의 업무 수행 능력도 자연스럽게 좋아지는가?**
2. **현재 개발이 AI가 일을 더 잘하도록 Context, Data, Tool, Skill, Permission, Runtime 등을 강화하는가?**

둘 다 No라면 대개 **AI로 더 빨리 만든 기존 IT**입니다. 가치가 없다는 뜻은 아니지만, Agent Transformation과는 구분해야 합니다.

## Supporting Capabilities

CAMP Stage와 별도로 두 가지 역량을 봅니다.

### AI Operations
- Visibility
- Cost
- Quality
- Security

> **보이지 않는 AI는 운영할 수 없습니다.**

### Sovereign AI
- External API
- Multi-model Portfolio
- Private / Local Inference
- Post-training
- Foundation Model

자체 모델이 없어도 높은 CAMP Stage가 가능하며, Foundation Model이 있어도 조직의 Agent 활용이 낮다면 CAMP Stage는 낮을 수 있습니다.

## 결과 예시

```text
🧭 CAMP Result

현재 위치: Stage 3 — Connected AI
Confidence: High

한 줄 진단:
사내 RAG와 MCP 기반은 강하지만, 개인의 Skill과 Agent Session이 조직 자산으로 축적되지 않아 다음 단계로 넘어가지 못하고 있습니다.

잘하고 있는 것
- 사내 RAG 운영
- 내부 MCP Server 운영
- 개인 AI 사용률 높음

가장 큰 병목
- Skill / Session Knowledge의 조직적 Compounding 부재

다음 90일 Top 3
1. Top Performer 10명의 반복업무 Skill화
2. Agent Session → 조직 Memory Pilot
3. Agent Usage / Cost / Quality Trace 시작

Stop Doing
- Vibe Coding Dashboard 수를 AX 성과지표로 관리하지 말 것

AI Operations: Developing
Sovereign AI: Private / Local Inference

다음 목표: Stage 4 — Compounding AI
```

## 파일

- `SKILL.md` — AI Agent가 CAMP 진단을 수행하는 지침
- `PLAYBOOK.md` — 세부 진단 기준, Q&A, Evidence 판정, 과제 리뷰 방법
- `examples/sample-assessment.md` — 결과 예시

## 철학

> **좋은 AX는 AI 시스템을 많이 만드는 것이 아니다.**
>
> 모든 개인에게 강력한 AI를 주고, AI가 회사의 Context와 Tool을 사용할 수 있게 하고, 개인의 Skill과 Session Knowledge를 조직 전체의 Intelligence로 축적하며, 그 결과 사람의 역할과 조직 구조를 다시 설계하는 것이다.
