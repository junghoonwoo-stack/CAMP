# CAMP Bench

## English

CAMP Bench compares an anonymized CAMP assessment with other organizations when enough data exists.

| Area | Comparison |
|---|---|
| Overall | All organizations |
| Industry | Same industry |
| Peer Group | Similar segment, size, country/region, scope, and function |
| 5 Dimensions | Relative strengths and weak spots |
| Same Company | Mean/median, distribution, team/function differences, disagreement |

### Identity

CAMP Bench asks for the real company / organization name to connect assessments from the same organization, avoid duplicate counting, support longitudinal tracking, and improve peer matching.

The real name is stored only in the **private identity registry** and mapped to an anonymous `org_group_id`. Reports use anonymized labels such as `Your organization`, Industry, Peer Group, Organization Group ID, and Scope ID.

### Public / Private

| Location | Contains |
|---|---|
| Public CAMP repo | Framework, schema, field definitions, synthetic examples |
| Private benchmark store | Identity mapping, assessment records, scope/team relationships, history |

Confidential company identities and named scores are not exposed. Named-company comparison requires public information or data explicitly authorized for named disclosure.

### Peer Group

Use the narrowest cohort with enough organizations: Industry → Industry Segment → Segment + Size → add Country/Region → add Scope/Function. If N < 10, broaden the cohort or report insufficient sample size.

### Data Quality

`eligible` = standard benchmark  
`provisional` = preliminary benchmark only  
`reference_only` = excluded from ranking

---

## 한국어

CAMP Bench는 표본이 충분할 때 익명화된 CAMP 진단 결과를 다른 조직과 비교합니다.

| 영역 | 비교 대상 |
|---|---|
| Overall | 전체 조직 |
| Industry | 같은 업종 |
| Peer Group | 유사 Segment, 규모, 국가/지역, Scope, Function |
| 5 Dimensions | 상대적으로 강한 영역과 약한 영역 |
| Same Company | 평균/중앙값, 분포, 팀·Function 차이, 인식 차이 |

### 회사명

CAMP Bench에서는 같은 회사의 여러 응답을 연결하고, 중복 집계를 막고, 시계열 추적과 Peer Matching 정확도를 높이기 위해 실제 회사 / 조직명을 입력받습니다.

실제 이름은 **Private Identity Registry**에만 저장하고 익명 `org_group_id`와 연결합니다. Report에는 `Your organization`, Industry, Peer Group, Organization Group ID, Scope ID 같은 익명화된 표현을 사용합니다.

### Public / Private

| 위치 | 저장 내용 |
|---|---|
| Public CAMP Repo | Framework, Schema, Field 정의, Synthetic Example |
| Private Benchmark Store | 실제 회사명 Mapping, 진단 Record, Scope/Team 관계, 이력 |

비공개 회사명과 개별 Named Score는 노출하지 않습니다. 회사명이 붙는 비교는 공개정보 또는 명시적으로 허가된 데이터만 사용합니다.

### Peer Group

표본이 충분한 범위에서 가장 좁은 Cohort를 사용합니다: Industry → Industry Segment → Segment + 규모 → 국가/지역 추가 → Scope/Function 추가. N < 10이면 더 넓은 Cohort로 비교하거나 표본 부족으로 표시합니다.

### Data Quality

`eligible` = 정식 Benchmark  
`provisional` = Preliminary Benchmark만  
`reference_only` = Ranking 제외
