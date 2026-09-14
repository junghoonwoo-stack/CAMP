# CAMP Bench

## English

CAMP Bench compares a submitted CAMP assessment with other organizations while keeping other participants anonymous.

### Why submit an assessment
Submitting an accurate current-state assessment returns an actionable private comparison, not just a contribution to the dataset:
- whether the organization is ahead of, in line with, or behind the overall benchmark
- overall percentile, mean, median, and score distribution
- industry position when the anonymous industry cohort has at least 10 organizations
- five-dimension scores and gaps against the benchmark median
- the largest capability gap and a recommended next action
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

The report labels itself `official` only when its comparison cohort contains eligible records only. A cohort containing provisional records is labeled `preliminary`, and its eligible/provisional mix is disclosed in the report. Preliminary results are directional and must not be presented as an official market ranking.

One organization counts once in cross-company ranking using an organization-level aggregate, even when many respondents participate.

### Privacy and storage
**Public CAMP repository:** framework, methodology, schemas, and synthetic examples only. No raw benchmark dataset and no real company identity mapping.

**Private CAMP Bench store:** company identity registry, raw assessment records, scope relationships, evidence/provenance, and longitudinal history.

Public/shared benchmark views contain only aggregate or anonymized results. Confidential submissions must never be used to expose another company's named score. Named-company comparison may use only public evidence or data explicitly authorized for named disclosure.

### Submission
At the end of a CAMP assessment, ask whether the participant wants the assessment included in CAMP Bench.

The configured private receiver creates or reuses the company's anonymous organization key, appends a new assessment without overwriting history, and returns a receipt. After private ingestion, the client retrieves and displays the bilingual aggregate benchmark report. If processing is still pending, retrieve it later with the receipt ID.

If the receiver is unavailable, do not claim that submission succeeded. Do not direct users to post real company data in a public GitHub issue.

The submission UX and receiver contract are defined in [SUBMISSION.md](SUBMISSION.md). A submission is successful only when the private receiver returns a valid receipt ID. Local file creation, validation, or a network request without a valid receipt is not success.

---

## 한국어

CAMP Bench는 제출된 CAMP 진단 결과를 다른 조직과 비교하되 **다른 참여기업의 identity는 익명화**합니다.

### 왜 진단 결과를 제출하나
현재 상태를 정확히 제출하면 단순히 Dataset에 기여하는 데서 끝나지 않고, 다음을 포함한 실행 가능한 Private 비교 Report를 받습니다.
- 전체 Benchmark보다 앞서는지, 비슷한지, 뒤처지는지
- Overall Percentile, 평균, 중앙값, 전체 점수 분포
- 익명 동종업계 Cohort가 10개 조직 이상일 때 Industry 위치
- Benchmark 중앙값 대비 5개 Dimension 점수와 격차
- 가장 큰 Capability Gap과 권장 Next Action
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

비교 Cohort가 `eligible` Record로만 구성된 경우에만 Report를 `official`로 표시합니다. `provisional` Record가 하나라도 포함된 Cohort는 `preliminary`로 표시하고, Report에 eligible/provisional 구성을 공개합니다. Preliminary 결과는 방향성 참고용이며 정식 시장 Ranking으로 표현하지 않습니다.

여러 명이 응답해도 기업 간 Ranking에서는 Organization-level Aggregate로 한 회사가 한 번만 반영됩니다.

### Privacy와 저장
**Public CAMP Repository:** Framework, Methodology, Schema, Synthetic Example만 저장. Raw Benchmark Dataset과 실제 회사명 Mapping은 없음.

**Private CAMP Bench Store:** 실제 회사명 Registry, 원본 진단 Record, Scope 관계, Evidence/Provenance, 시계열을 저장.

외부에 공유되는 Benchmark는 Aggregate 또는 익명화 결과만 사용합니다. 비공개 제출을 이용해 다른 회사의 실명 점수를 노출하지 않습니다. Named Company 비교는 공개 Evidence 또는 명시적으로 허용된 데이터만 사용합니다.

### 제출
CAMP 진단이 끝난 뒤 CAMP Bench에 결과를 포함할지 묻습니다.

설정된 Private Receiver가 회사의 익명 Organization Key를 조회하거나 생성하고, 과거 이력을 덮어쓰지 않고 새 Assessment를 추가한 뒤 Receipt를 반환합니다. Private Ingestion이 끝나면 Client가 한국어·영어 Aggregate Benchmark Report를 조회해 보여줍니다. 처리가 끝나지 않았다면 Receipt ID로 나중에 다시 조회할 수 있습니다.

Receiver에 접근할 수 없다면 제출됐다고 말하지 않습니다. 실제 회사 데이터를 Public GitHub Issue에 올리도록 안내하지 않습니다.

제출 UX와 Receiver 계약은 [SUBMISSION.md](SUBMISSION.md)에 정의합니다. Private Receiver가 유효한 Receipt ID를 반환한 경우에만 제출 성공입니다. 로컬 파일 생성·검증 또는 유효한 Receipt가 없는 Network Request는 성공이 아닙니다.
