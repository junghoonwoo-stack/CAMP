# CAMP Benchmark

## English

CAMP Benchmark is opt-in. Its first goal is simple: **share one anonymized assessment and get a useful comparison back.**

### What the participant gets
When sample size is sufficient, return:
- **Overall percentile** — vs all organizations
- **Industry percentile** — e.g. vs Manufacturing
- **Peer Group percentile** — vs similar organizations by broad industry segment, size, country/region, scope, and function when enough data exists
- **Dimension comparison** — Access, Delegation, Connection, Compounding, Transformation

Do not reveal competitor or company identities. “Competitor comparison” means an anonymized peer cohort, never named-company scores.

### Public data
Public benchmark data may include:
- anonymous Organization Group ID
- anonymous Scope ID and Respondent ID
- country
- industry
- broad industry segment
- scope
- headcount band
- function
- CAMP Stage and scores
- AI Operations and Sovereign AI level

**Never collect or publish company name, person name, email, customer name, project name, system name, or confidential free text.**

GitHub Issue submissions are public, so the submitter’s GitHub account may still be visible. Do not encode a company name in any anonymous ID.

### Multiple respondents from one organization
Use the same **Organization Group ID** and different **Respondent IDs**.

CAMP may show:
- individual results
- organization mean / median
- score spread
- dimensions with the largest disagreement

For external ranking, one organization counts once. Use an organization-level aggregate so organizations with many respondents do not dominate the benchmark.

### Peer Group rule
Use the narrowest cohort with enough organizations. Typical order:
1. broad industry
2. industry segment
3. industry segment + headcount band
4. industry segment + headcount + country/region
5. add scope/function only when sample size remains sufficient

If a cohort has fewer than 10 organizations, broaden the cohort instead of showing a fragile percentile.

### Privacy thresholds
- Overall N < 10: no percentile
- Segment N < 10: no segment percentile
- Never expose a single organization’s identity
- Always show N and benchmark date

---

## 한국어

CAMP Benchmark는 선택형입니다. 초기 목표는 단순합니다. **익명화된 진단 결과 하나를 공유하면 의미 있는 비교 결과를 돌려주는 것**입니다.

### 참여자가 받는 것
표본이 충분하면 다음을 제공합니다.
- **전체 Percentile** — 전체 조직 대비
- **Industry Percentile** — 예: 전체 제조업 대비
- **Peer Group Percentile** — 업종 세부군, 규모, 국가/지역, 진단 범위, Function이 유사한 조직 대비
- **영역별 비교** — Access, Delegation, Connection, Compounding, Transformation

경쟁사나 회사 이름은 공개하지 않습니다. “경쟁사 대비”는 익명 Peer Group 비교를 의미하며 특정 회사 점수를 공개하지 않습니다.

### 공개 가능한 데이터
- 익명 Organization Group ID
- 익명 Scope ID / Respondent ID
- 국가
- 업종
- 넓은 Industry Segment
- 진단 범위
- 인원 구간
- Function
- CAMP Stage / Score
- AI Operations / Sovereign AI 수준

**회사명, 개인 이름, 이메일, 고객명, 과제명, 시스템명, 자유서술형 기밀정보는 수집하거나 공개하지 않습니다.**

GitHub Issue는 공개이므로 제출자의 GitHub 계정은 보일 수 있습니다. 익명 ID에 회사명을 넣지 않습니다.

### 한 조직에서 여러 명이 응답하는 경우
같은 **Organization Group ID**와 서로 다른 **Respondent ID**를 사용합니다.

CAMP는 다음을 보여줄 수 있습니다.
- 개인별 결과
- 조직 평균 / 중앙값
- 점수 분산
- 인식 차이가 가장 큰 영역

외부 Benchmark에서는 한 조직이 한 번만 반영되도록 조직 단위 집계값을 사용합니다.

### Peer Group 원칙
표본이 충분한 범위에서 가장 유사한 Cohort를 사용합니다.
1. 전체 업종
2. Industry Segment
3. Industry Segment + 규모
4. Industry Segment + 규모 + 국가/지역
5. 표본이 충분할 때만 Scope/Function까지 추가

Cohort가 10개 조직 미만이면 억지로 순위를 보여주지 않고 더 넓은 그룹으로 비교합니다.

### Privacy 기준
- 전체 N < 10: Percentile 미제공
- 세부 그룹 N < 10: 해당 Percentile 미제공
- 특정 회사의 정체는 공개하지 않음
- N과 Benchmark 기준일을 항상 표시
