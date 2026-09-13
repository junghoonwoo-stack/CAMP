# CAMP Benchmark

## English

Share one anonymized assessment and get useful comparisons back.

### What participants get
When sample size is sufficient:
- Overall percentile
- Industry percentile
- Peer Group percentile
- Dimension comparison: Access, Delegation, Connection, Compounding, Transformation

Peer Group uses broad industry segment, size, country/region, scope, and function. Company names are never shown.

### Data quality
Each record includes:
- `assessment_method`: self_report / evidence_assessment / expert_evidence
- `confidence`: Low / Medium / High
- `benchmark_status`: eligible / provisional / reference_only

`eligible` records count toward standard percentiles.  
`provisional` records may be used only for an explicitly labeled **Preliminary Benchmark** while the dataset is small.  
`reference_only` records are useful cases but do not count toward ranking.

Do not convert product/vendor capability into the vendor's own CAMP maturity score unless the evidence is about that organization's internal operating model.

### Public fields
Anonymous Organization Group ID, Scope ID, Respondent ID, country, industry, broad industry segment, scope, headcount band, function, Stage, scores, AI Operations, Sovereign AI, assessment method, confidence, and benchmark status.

Never publish company names, person names, email addresses, customers, projects, systems, or confidential free text.

### Multiple respondents
Use the same Organization Group ID and different Respondent IDs. For cross-company ranking, one organization counts once using an organization-level aggregate.

### Peer Group rule
Use the narrowest cohort with enough organizations:
1. Industry
2. Industry segment
3. Industry segment + size
4. Industry segment + size + country/region
5. Add scope/function only when sample size remains sufficient

If N < 10, broaden the cohort. If the eligible dataset is still too small, show no official percentile. A Preliminary Benchmark may include provisional records only when clearly labeled with N and data quality.

---

## 한국어

익명화된 진단 결과를 공유하면 의미 있는 비교 결과를 돌려줍니다.

### 참여자가 받는 것
표본이 충분하면:
- 전체 Percentile
- Industry Percentile
- Peer Group Percentile
- 영역별 비교: Access, Delegation, Connection, Compounding, Transformation

Peer Group은 넓은 Industry Segment, 규모, 국가/지역, 진단 범위, Function을 사용합니다. 회사명은 공개하지 않습니다.

### 데이터 품질
각 데이터에는 다음을 표시합니다.
- `assessment_method`: self_report / evidence_assessment / expert_evidence
- `confidence`: Low / Medium / High
- `benchmark_status`: eligible / provisional / reference_only

`eligible`만 정식 Percentile에 사용합니다.  
`provisional`은 데이터가 적은 초기 단계에서 **Preliminary Benchmark**라고 명시할 때만 사용할 수 있습니다.  
`reference_only`는 참고 사례이며 순위 계산에서 제외합니다.

제품이나 Vendor의 기능을 그 회사 자체의 CAMP 성숙도로 계산하지 않습니다. 반드시 해당 조직의 내부 Operating Model에 대한 Evidence가 있어야 합니다.

### 공개 데이터
익명 Organization Group ID, Scope ID, Respondent ID, 국가, 업종, 넓은 Industry Segment, Scope, 인원 구간, Function, Stage/Score, AI Operations, Sovereign AI, 평가 방식, Confidence, Benchmark Status.

회사명, 개인 이름, 이메일, 고객명, 과제명, 시스템명, 자유서술형 기밀정보는 공개하지 않습니다.

### 여러 명이 응답하는 경우
같은 Organization Group ID와 서로 다른 Respondent ID를 사용합니다. 기업 간 비교에서는 조직 단위 집계값으로 한 조직을 한 번만 반영합니다.

### Peer Group 원칙
표본이 충분한 범위에서 가장 유사한 Cohort를 사용합니다.
1. Industry
2. Industry Segment
3. Industry Segment + 규모
4. Industry Segment + 규모 + 국가/지역
5. 표본이 충분할 때만 Scope/Function 추가

N < 10이면 더 넓은 그룹으로 비교합니다. eligible 데이터가 부족하면 정식 Percentile을 제공하지 않습니다. provisional 데이터를 포함할 때는 반드시 **Preliminary Benchmark**, N, 데이터 품질을 함께 표시합니다.
