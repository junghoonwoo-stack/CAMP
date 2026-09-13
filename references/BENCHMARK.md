# CAMP Bench

## English

CAMP Bench compares a submitted CAMP assessment with other organizations while keeping other participants anonymous.

### Why submit an assessment
Submitting an accurate current-state assessment enables:
- Overall percentile
- Industry percentile
- anonymous Peer Group percentile
- five-dimension comparison
- same-company aggregate when earlier responses exist
- team/function dispersion when multiple scopes or respondents exist
- longitudinal movement when the organization is assessed again

The **real company name** is used privately to match previous assessments from the same organization, prevent duplicate counting, and improve peer matching.

### What the participant sees
The participant may see **their own company** in their private report. Every other company remains anonymous.

If multiple people from the same company participate, CAMP Bench may show:
- company/scope mean and median
- score distribution and range
- team/function differences
- dimensions with the largest disagreement
- role-level perception gaps when sample size supports them

Individual respondent identities are never shown.

### Peer Group
Use the narrowest cohort with enough organizations:
1. Industry
2. Industry segment
3. Segment + size
4. Segment + size + country/region
5. Add scope/function only when N remains sufficient

If cohort N < 10 organizations, broaden the cohort or report insufficient sample size.

### Data quality
- `eligible`: counts toward official percentiles
- `provisional`: preliminary analysis only
- `reference_only`: never used for ranking

One organization counts once in cross-company ranking using an organization-level aggregate, even when many respondents participate.

### Privacy and storage
**Public CAMP repository:** framework, methodology, schemas, and synthetic examples only. No raw benchmark dataset and no real company identity mapping.

**Private CAMP Bench store:** company identity registry, raw assessment records, scope relationships, evidence/provenance, and longitudinal history.

Public/shared benchmark views contain only aggregate or anonymized results. Confidential submissions must never be used to expose another company's named score. Named-company comparison may use only public evidence or data explicitly authorized for named disclosure.

### Submission
At the end of a CAMP assessment, ask whether the participant wants the assessment included in CAMP Bench.

If the connected private store is available, create or reuse the company's anonymous organization key and append a new assessment record without overwriting history.

If the private store is unavailable, do not claim that submission succeeded. Produce a structured private submission package instead. Do not direct users to post real company data in a public GitHub issue.

---

## 한국어

CAMP Bench는 제출된 CAMP 진단 결과를 다른 조직과 비교하되 **다른 참여기업의 identity는 익명화**합니다.

### 왜 진단 결과를 제출하나
현재 상태를 정확히 제출하면 다음을 볼 수 있습니다.
- Overall Percentile
- Industry Percentile
- 익명 Peer Group Percentile
- 5개 Dimension 비교
- 같은 회사의 기존 응답이 있으면 Same-company Aggregate
- 여러 팀/응답자가 있으면 팀·Function별 분포
- 재진단 시 시계열 변화

**실제 회사명**은 같은 회사의 기존 진단을 연결하고, 중복 집계를 막고, Peer Matching 정확도를 높이기 위해 Private에서만 사용합니다.

### 참여자가 보는 것
참여자의 Private Report에는 **자기 회사**를 표시할 수 있습니다. 다른 회사는 모두 익명화합니다.

같은 회사에서 여러 명이 참여하면 다음을 보여줄 수 있습니다.
- 회사/Scope 평균·중앙값
- 점수 분포와 범위
- 팀·Function별 차이
- 의견 차이가 가장 큰 영역
- 표본이 충분하면 Role Level별 인식 차이

개별 응답자의 identity는 표시하지 않습니다.

### Peer Group
표본이 충분한 범위에서 가장 좁은 Cohort를 사용합니다.
1. Industry
2. Industry Segment
3. Segment + 규모
4. Segment + 규모 + 국가/지역
5. N이 충분할 때만 Scope/Function 추가

Cohort가 10개 조직 미만이면 더 넓은 그룹으로 비교하거나 표본 부족으로 표시합니다.

### Data Quality
- `eligible`: 정식 Percentile에 포함
- `provisional`: Preliminary Analysis에만 사용
- `reference_only`: Ranking 제외

여러 명이 응답해도 기업 간 Ranking에서는 Organization-level Aggregate로 한 회사가 한 번만 반영됩니다.

### Privacy와 저장
**Public CAMP Repository:** Framework, Methodology, Schema, Synthetic Example만 저장. Raw Benchmark Dataset과 실제 회사명 Mapping은 없음.

**Private CAMP Bench Store:** 실제 회사명 Registry, 원본 진단 Record, Scope 관계, Evidence/Provenance, 시계열을 저장.

외부에 공유되는 Benchmark는 Aggregate 또는 익명화 결과만 사용합니다. 비공개 제출을 이용해 다른 회사의 실명 점수를 노출하지 않습니다. Named Company 비교는 공개 Evidence 또는 명시적으로 허용된 데이터만 사용합니다.

### 제출
CAMP 진단이 끝난 뒤 CAMP Bench에 결과를 포함할지 묻습니다.

Private Store가 연결되어 있으면 회사의 익명 Organization Key를 조회하거나 생성하고, 과거 이력을 덮어쓰지 않고 새 Assessment를 추가합니다.

Private Store에 접근할 수 없다면 제출됐다고 말하지 않습니다. 대신 Private Submission Package를 생성합니다. 실제 회사 데이터를 Public GitHub Issue에 올리도록 안내하지 않습니다.
