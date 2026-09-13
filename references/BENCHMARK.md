# CAMP Bench

## English

CAMP Bench is **Give to Get**: contribute your assessment to receive benchmark analysis.

### Private identity matching
CAMP Bench asks for the real company / organization name to:
- deduplicate organizations
- connect multiple respondents from the same company
- track changes over time
- improve peer-group matching
- compare teams and functions inside one organization

The real company name is stored only in a **private identity registry** and mapped to an anonymous `org_group_id`.

Reports and benchmark outputs remain anonymized. They use `Your organization`, Industry, Peer Group, Organization Group ID, and anonymous Scope IDs instead of real company/team names.

### What contributors get
When sample size is sufficient:
- Overall percentile
- Industry percentile
- Peer Group percentile
- benchmark distribution with `Your organization` highlighted
- five-dimension comparison
- relative strengths and weaknesses
- longitudinal movement
- same-company respondent distribution and team/function differences

### Same-company responses
If several people from one organization participate, connect them through the private identity registry and show:
- organization mean / median
- score distribution / range
- team or function differences
- dimensions with the largest disagreement

For cross-company ranking, each organization counts once using an organization-level aggregate.

### Privacy
The public CAMP repository contains only the framework, schema, field definitions, and synthetic examples. It does **not** contain the raw benchmark dataset or real-company identity mapping.

Never expose confidential participant company names, respondent identities, or named-company scores. Named competitor comparisons may use only public information or data explicitly authorized for named disclosure.

### Peer Group
Use the narrowest cohort with enough organizations:
1. Industry
2. Industry segment
3. Segment + size
4. Segment + size + country/region
5. Add scope/function only when N remains sufficient

If N < 10, broaden the cohort or show insufficient sample size.

### Data quality
- `eligible`: standard benchmark
- `provisional`: preliminary benchmark only
- `reference_only`: never used for ranking

---

## 한국어

CAMP Bench는 **Give to Get** 방식입니다. 자신의 진단 데이터를 제공하면 Benchmark 분석을 받을 수 있습니다.

### 실제 회사명을 받는 이유
CAMP Bench에서는 실제 회사 / 조직명을 입력받습니다.
- 동일 회사 중복 제거
- 같은 회사의 여러 응답 연결
- 시간에 따른 변화 추적
- 더 정확한 Peer Group 구성
- 같은 회사 안의 팀·Function 차이 분석

실제 회사명은 **Private Identity Registry**에만 저장하고 익명 `org_group_id`와 연결합니다.

Report와 Benchmark 출력은 익명화합니다. 실제 회사/팀 이름 대신 `Your organization`, Industry, Peer Group, 익명 Organization Group ID와 Scope ID를 사용합니다.

### 참여자가 받는 것
표본이 충분하면:
- 전체 Percentile
- Industry Percentile
- Peer Group Percentile
- 분포에서 `Your organization` 위치 Highlight
- 5개 영역 비교
- Peer 대비 상대적 강점 / 약점
- 시계열 변화
- 같은 회사 응답자 분포와 팀·Function 차이

### 같은 회사의 여러 응답
같은 조직에서 여러 명이 참여하면 Private Identity Registry를 통해 연결하고 다음을 보여줍니다.
- 조직 평균 / 중앙값
- 점수 분포 / 범위
- 팀·Function별 차이
- 의견 차이가 가장 큰 영역

기업 간 Ranking에서는 조직 단위 Aggregate를 사용해 한 회사가 한 번만 반영되게 합니다.

### Privacy
Public CAMP Repository에는 Framework, Schema, Field 정의, Synthetic Example만 있습니다. **Raw Benchmark Dataset과 실제 회사명 Mapping은 공개하지 않습니다.**

비공개 참여기업의 회사명, 응답자 identity, Named Score는 공개하지 않습니다. 특정 경쟁사 이름이 붙은 비교는 공개정보이거나 해당 조직이 명시적으로 허용한 데이터만 사용합니다.

### Peer Group
표본이 충분한 범위에서 가장 좁은 Cohort를 사용합니다.
1. Industry
2. Industry Segment
3. Segment + 규모
4. Segment + 규모 + 국가/지역
5. N이 충분할 때만 Scope/Function 추가

N < 10이면 더 넓은 Cohort로 비교하거나 표본 부족으로 표시합니다.

### Data Quality
- `eligible`: 정식 Benchmark
- `provisional`: Preliminary Benchmark만
- `reference_only`: Ranking 제외
