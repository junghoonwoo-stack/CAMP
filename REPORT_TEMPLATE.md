# CAMP Report Template

진단이 끝나면 아래 형식의 Report를 생성합니다. 사용자가 파일 생성을 원하면 Markdown/PDF/Doc 형태로 내보낼 수 있습니다.

# 🧭 CAMP Assessment Report

## 1. Organization Profile
- Scope: 회사 전체 / 사업부 / 팀 / 신설 AI-native 조직
- Country:
- Industry:
- Headcount band:
- Function:
- Assessment date:
- Evidence mode: Interview / Files + Interview

## 2. Executive Result

**CAMP Stage:** `Stage N — Name`  
**CAMP Score:** `NN / 100`  
**Confidence:** High / Medium / Low

**한 줄 진단:**  
현재 Operating Model과 가장 큰 병목을 한 문장으로 설명합니다.

## 3. CAMP Score

CAMP Score는 5개 핵심 영역을 각각 0~20점으로 평가해 100점으로 계산합니다.

| Dimension | Score | 의미 |
|---|---:|---|
| AI Access | /20 | 개인 AI 접근성과 조직 Coverage |
| AI Delegation | /20 | 질문을 넘어 실제 업무를 Agent에 위임하는 정도 |
| Enterprise Connection | /20 | 회사 Context/Data/Tool/System 연결 정도 |
| Knowledge Compounding | /20 | Skill/Session/Context의 조직 자산화 정도 |
| Role Transformation | /20 | Handoff 감소, 역할 확장, 조직 재설계 정도 |
| **Total** | **/100** | |

### 기본 점수 매핑
각 핵심 질문의 A/B/C/D/E 답변은 기본적으로 `0 / 5 / 10 / 15 / 20`점입니다.

단, 다음 경우 조정할 수 있습니다.
- 개인 계정이 아니라 팀 공유 계정이면 Access를 하향
- Pilot 한 건뿐이면 해당 Capability를 전사 수준으로 계산하지 않음
- 계획/제안 단계는 현재 Capability 점수에 포함하지 않음
- 반복 사용/Operationalized evidence가 있으면 높은 점수의 Confidence를 높임

Stage와 Score는 동일하지 않습니다. Stage는 현재 Operating Model의 질적 위치이고, Score는 다섯 축의 균형을 보여줍니다.

## 4. Evidence Summary

**확인된 강점**
- 2~5개

**확인되지 않았거나 추가 증거가 필요한 부분**
- 필요한 경우에만

## 5. Biggest Bottleneck

> 다음 CAMP Stage 또는 더 높은 성과를 막고 있는 가장 중요한 한 가지

왜 이 병목이 중요한지 2~4문장으로 설명합니다.

## 6. Next 90 Days — Top 3

1. **Action 1** — 구체적 산출물과 성공조건
2. **Action 2** — 구체적 산출물과 성공조건
3. **Action 3** — 구체적 산출물과 성공조건

가능하면 Action을 실제 AX 과제 형태로 표현합니다.

## 7. Recommended AX Projects

필요하면 3~5개 과제를 제안합니다.

| Priority | Project | CAMP impact | Success signal |
|---|---|---|---|
| P0 |  |  |  |

## 8. Stop Doing

현재 자원을 소모하지만 Agent-native 전환에 낮은 기여를 하는 활동을 1~3개 제시합니다.

## 9. Supporting Capabilities

**AI Operations:** Weak / Developing / Strong  
Visibility / Cost / Quality / Security를 근거로 설명합니다.

**Sovereign AI:** API / Portfolio / Private / Post-trained / Foundation  
현재 수준과 더 높은 Sovereignty가 실제로 필요한지 설명합니다.

## 10. Benchmark

진단 마지막에 반드시 별도의 동의를 묻습니다.

> CAMP Score를 익명화된 Benchmark에 공유하시겠습니까? 공유하시면 충분한 표본이 쌓였을 때 전체 조직 및 가능하면 국가·업종·규모별 분포에서 현재 위치를 알려드릴 수 있습니다. 회사명과 자유서술 내용은 기본적으로 수집하지 않습니다. GitHub 기반 공개 제출 방식을 사용할 경우 제출자의 GitHub 계정은 공개될 수 있습니다.

선택지:
- A. 예, 익명화된 점수를 공유하겠습니다.
- B. 아니요, 공유하지 않겠습니다.
- C. 어떤 정보가 공유되는지 먼저 보여주세요.

동의하지 않으면 어떤 Benchmark 데이터도 기록하지 않습니다.

### Percentile 표시 규칙
- 전체 표본이 10개 미만이면 순위를 제시하지 않고 `표본 부족`이라고 표시합니다.
- 세부 그룹(국가/업종/규모)은 해당 그룹 표본이 10개 이상일 때만 percentile을 표시합니다.
- Percentile은 CAMP Score 기준으로 계산합니다.
- 표본 수 `N`과 기준일을 반드시 함께 표시합니다.
