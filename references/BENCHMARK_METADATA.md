# CAMP Benchmark Metadata

## English

The public repository documents the **schema**, not the raw benchmark dataset.

### Anonymized assessment schema

| Field | Meaning | Example |
|---|---|---|
| `submission_id` | Unique assessment record | `2026-001` |
| `date` | Assessment date | `2026-09-13` |
| `org_group_id` | Stable anonymous organization key | `ORG-KR-A1B2` |
| `scope_id` | Anonymous company/unit/team scope | `S01` |
| `respondent_id` | Anonymous respondent key | `R03` |
| `respondent_role` | Broad role perspective; no personal identity | `Manager / team leader` |
| `assessment_method` | self_report / interview / evidence_assessment / expert_evidence | `self_report` |
| `evidence_level` | Anecdotal / Repeated / Operationalized / Institutionalized | `Repeated` |
| `confidence` | Low / Medium / High | `High` |
| `benchmark_status` | eligible / provisional / reference_only | `eligible` |
| `country` | Country | `South Korea` |
| `industry` | Broad industry | `Manufacturing` |
| `industry_segment` | Broad peer segment | `Home Appliances` |
| `scope` | Company / business unit / team / new org | `Business unit / division` |
| `headcount` | Assessed population band | `1001-5000` |
| `function` | Primary function | `R&D / Engineering` |
| `stage` | CAMP Stage | `Stage 3 - Connected AI` |
| `total_score` | CAMP Score /100 | `60` |
| `access` | AI Access /20 | `15` |
| `delegation` | AI Delegation /20 | `15` |
| `connection` | Enterprise Connection /20 | `15` |
| `compounding` | Knowledge Compounding /20 | `10` |
| `transformation` | Role Transformation /20 | `5` |
| `operations` | AI Operations | `Strong` |
| `sovereignty` | Sovereign AI level | `Portfolio` |

### Private identity data

Real organization identity is stored outside the public repository. The private store maintains at minimum:
- `org_group_id`
- real `company_name`
- country / industry / industry segment
- private scope labels linked to `scope_id`
- raw assessment records linked only through anonymous IDs
- evidence/provenance and longitudinal history

Personal respondent names and emails are not required by default.

Use the role labels from the interview guide: `New joiner / early career (0-2 years)`, `Junior / practitioner (3-7 years)`, `Senior / expert (8+ years)`, `Manager / team leader`, `Executive / C-level`, or `Other / prefer not to say`.

The participant may see their own company name in a private report. Other organizations remain anonymous. Public/shared benchmark output uses only aggregate or anonymized data.

---

## 한국어

Public Repository에는 Raw Benchmark Dataset이 아니라 **Schema만 공개**합니다.

### 익명 진단 Schema

| Field | 의미 | 예시 |
|---|---|---|
| `submission_id` | 진단 Record 고유 ID | `2026-001` |
| `date` | 진단일 | `2026-09-13` |
| `org_group_id` | 안정적인 익명 조직 Key | `ORG-KR-A1B2` |
| `scope_id` | 회사/사업부/팀 익명 Scope | `S01` |
| `respondent_id` | 익명 응답자 Key | `R03` |
| `respondent_role` | 개인식별정보가 없는 넓은 역할 관점 | `Manager / team leader` |
| `assessment_method` | self_report / interview / evidence_assessment / expert_evidence | `self_report` |
| `evidence_level` | Anecdotal / Repeated / Operationalized / Institutionalized | `Repeated` |
| `confidence` | Low / Medium / High | `High` |
| `benchmark_status` | eligible / provisional / reference_only | `eligible` |
| `country` | 국가 | `South Korea` |
| `industry` | 대분류 업종 | `Manufacturing` |
| `industry_segment` | Peer Segment | `Home Appliances` |
| `scope` | 회사/사업부/팀/신설조직 | `Business unit / division` |
| `headcount` | 진단 대상 인원 구간 | `1001-5000` |
| `function` | 주요 Function | `R&D / Engineering` |
| `stage` | CAMP Stage | `Stage 3 - Connected AI` |
| `total_score` | CAMP Score /100 | `60` |
| `access` | AI Access /20 | `15` |
| `delegation` | AI Delegation /20 | `15` |
| `connection` | Enterprise Connection /20 | `15` |
| `compounding` | Knowledge Compounding /20 | `10` |
| `transformation` | Role Transformation /20 | `5` |
| `operations` | AI Operations | `Strong` |
| `sovereignty` | Sovereign AI 수준 | `Portfolio` |

### Private Identity Data

실제 회사 identity는 Public Repository 밖에서 관리합니다. Private Store에는 최소한 다음을 둡니다.
- `org_group_id`
- 실제 `company_name`
- 국가 / 업종 / Industry Segment
- `scope_id`와 연결되는 Private Scope Label
- 익명 ID로만 연결되는 원본 Assessment Record
- Evidence/Provenance와 시계열 이력

개인 응답자의 이름과 이메일은 기본적으로 수집하지 않습니다.

역할 Label은 인터뷰 가이드에 따라 `신입·초기 경력(0–2년)`, `주니어·실무자(3–7년)`, `시니어·전문가(8년 이상)`, `매니저·팀장`, `임원·경영진`, `기타·응답하지 않음`을 사용합니다.

참여자는 Private Report에서 자기 회사명을 볼 수 있지만 다른 회사는 익명화합니다. 외부 공유 Benchmark는 Aggregate 또는 익명 데이터만 사용합니다.
