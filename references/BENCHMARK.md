# CAMP Benchmark

## English

CAMP uses a **Give-to-Get** benchmark.

### Access rule
- CAMP assessment, Stage, Score, and recommendations: free.
- Benchmark percentiles and peer analysis: available only after sharing your anonymized CAMP assessment.
- No contributed assessment = no Benchmark analysis.

This keeps the benchmark useful: every comparison user also improves the dataset.

### What contributors get
When sample size is sufficient:
- Overall percentile
- Industry percentile
- Peer Group percentile
- Dimension gaps: Access, Delegation, Connection, Compounding, Transformation
- Later: trend, custom cohorts, multi-team comparison, longitudinal movement

### Data architecture
**Public repository:** framework, schema, metadata, synthetic examples. No raw Benchmark dataset.  
**Private benchmark store:** assessment records used for comparison.  
**Private identity registry:** optional real company name mapped to `org_group_id` for deduplication, verification, longitudinal tracking, and better peer matching.

Real company names are never part of the public benchmark dataset.

### Participation levels
1. **Anonymous contribution** — share anonymized assessment; receive Overall / Industry / Peer Group comparison.
2. **Private identity** — optionally provide company identity privately; receive better longitudinal tracking and peer matching. Identity stays private.
3. **Multi-respondent organization** — multiple respondents share one Organization Group ID; receive mean/median, spread, and disagreement analysis.
4. **Future premium** — historical trends, custom peer cohorts, verified benchmarks, executive reports, API/export.

Named-company scores are not sold or exposed unless they come from public sources or the organization explicitly permits named disclosure. Paid value should come from verified cohorts, trends, analytics, and private comparison—not exposing confidential submissions.

### Data quality
- `eligible`: standard benchmark
- `provisional`: preliminary benchmark only
- `reference_only`: never used for ranking

For company ranking, one organization counts once using an organization-level aggregate.

### Peer Group
Use the narrowest cohort with enough organizations:
1. Industry
2. Industry segment
3. Segment + size
4. Segment + size + country/region
5. Add scope/function only when N remains sufficient

If N < 10, broaden the cohort or show insufficient sample size.

---

## 한국어

CAMP Benchmark는 **Give-to-Get** 구조입니다.

### 접근 원칙
- CAMP 진단, Stage, Score, 추천 Action: 무료.
- Benchmark Percentile과 Peer 분석: 자신의 익명 CAMP 결과를 공유한 경우에만 제공.
- 데이터 기여 없음 = Benchmark 분석 없음.

즉 비교 결과를 받는 사람은 동시에 Benchmark 데이터도 늘리게 됩니다.

### 참여자가 받는 것
표본이 충분하면:
- 전체 Percentile
- Industry Percentile
- Peer Group Percentile
- 5개 영역별 Gap
- 향후: 추세, Custom Cohort, 여러 팀 비교, 시계열 변화

### 데이터 구조
**Public Repository:** Framework, Schema, Metadata, 가상 Example만 공개. Raw Benchmark 데이터는 공개하지 않음.  
**Private Benchmark Store:** 실제 비교 계산용 진단 데이터.  
**Private Identity Registry:** 선택적으로 실제 회사명과 `org_group_id`를 연결해 중복 제거, 검증, 시계열 추적, Peer Matching에 사용.

실제 회사명은 Public Benchmark Dataset에 포함하지 않습니다.

### 참여 수준
1. **Anonymous Contribution** — 익명 결과 공유 → 전체 / 업종 / Peer Group 비교.
2. **Private Identity** — 회사명을 비공개로 알려주면 시계열 추적과 Peer Matching 정확도 향상. 회사명은 외부 비공개.
3. **Multi-respondent Organization** — 같은 Organization Group ID로 여러 명 참여 → 평균/중앙값/분산/인식차 분석.
4. **Future Premium** — Historical Trend, Custom Peer Cohort, Verified Benchmark, Executive Report, API/Export.

회사명이 붙은 개별 점수는 공개 출처이거나 해당 조직이 명시적으로 허용한 경우가 아니면 판매하거나 공개하지 않습니다. 유료 가치는 **회사명 노출이 아니라 검증된 Cohort, 추세, 분석, 비공개 비교**에서 만듭니다.

### 데이터 품질
- `eligible`: 정식 Benchmark
- `provisional`: Preliminary Benchmark만
- `reference_only`: 순위 제외

기업 간 비교에서는 조직 단위 집계값으로 한 조직을 한 번만 반영합니다.

### Peer Group
표본이 충분한 범위에서 가장 유사한 Cohort를 사용합니다.
1. Industry
2. Industry Segment
3. Segment + 규모
4. Segment + 규모 + 국가/지역
5. N이 충분할 때만 Scope/Function 추가

N < 10이면 더 넓은 그룹으로 비교하거나 표본 부족으로 표시합니다.
