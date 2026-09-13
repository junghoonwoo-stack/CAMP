# CAMP Benchmark Metadata

## English

### Public assessment fields

| Field | Meaning | Example |
|---|---|---|
| `submission_id` | Unique assessment record | `2026-001` |
| `date` | Assessment date | `2026-09-13` |
| `org_group_id` | Stable anonymous organization key | `ORG-KR-A1B2` |
| `scope_id` | Anonymous company/unit/team scope | `S01` |
| `respondent_id` | Anonymous respondent key | `R03` |
| `assessment_method` | `self_report`, `evidence_assessment`, `expert_evidence` | `self_report` |
| `confidence` | Low / Medium / High | `High` |
| `benchmark_status` | `eligible`, `provisional`, `reference_only` | `eligible` |
| `country` | Country | `South Korea` |
| `industry` | Broad industry | `Manufacturing` |
| `industry_segment` | Broad peer segment, never a company name | `Home Appliances` |
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

### Private registry fields

Keep these outside the public repository.

| Field | Meaning |
|---|---|
| `org_group_id` | Join key to benchmark data |
| `company_name` | Real organization name |
| `legal_entity` | Optional legal entity name |
| `country` | Main country |
| `industry` | Broad industry |
| `industry_segment` | Peer-group segment |
| `source_type` | direct / interview / public / expert note |
| `consent_level` | anonymous-only / private-identity / named-public |
| `first_seen` | First assessment date |
| `last_seen` | Latest assessment date |
| `notes` | Private quality notes only; never benchmark free text |

Private identity is used for deduplication, longitudinal tracking, verification, and better peer matching. Named-company scores must not be exposed externally unless the source is public or the organization explicitly permits named disclosure.

---

## 한국어

### 공개 진단 필드

| Field | 의미 | 예시 |
|---|---|---|
| `submission_id` | 진단 레코드 고유 ID | `2026-001` |
| `date` | 진단일 | `2026-09-13` |
| `org_group_id` | 조직별 안정적인 익명 Key | `ORG-KR-A1B2` |
| `scope_id` | 회사/사업부/팀 익명 Scope | `S01` |
| `respondent_id` | 익명 응답자 Key | `R03` |
| `assessment_method` | `self_report`, `evidence_assessment`, `expert_evidence` | `self_report` |
| `confidence` | Low / Medium / High | `High` |
| `benchmark_status` | `eligible`, `provisional`, `reference_only` | `eligible` |
| `country` | 국가 | `South Korea` |
| `industry` | 대분류 업종 | `Manufacturing` |
| `industry_segment` | 회사명이 아닌 넓은 Peer Segment | `Home Appliances` |
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

### 비공개 Registry 필드

공개 Repository 밖에서만 관리합니다.

| Field | 의미 |
|---|---|
| `org_group_id` | Benchmark 데이터와 연결하는 Key |
| `company_name` | 실제 회사명 |
| `legal_entity` | 필요 시 법인명 |
| `country` | 주요 국가 |
| `industry` | 대분류 업종 |
| `industry_segment` | Peer Group 분류 |
| `source_type` | direct / interview / public / expert note |
| `consent_level` | anonymous-only / private-identity / named-public |
| `first_seen` | 최초 진단일 |
| `last_seen` | 최근 진단일 |
| `notes` | 비공개 품질관리 메모; Benchmark 자유서술에는 사용하지 않음 |

비공개 회사명은 중복 제거, 시계열 추적, 검증, 정확한 Peer Matching에 사용합니다. 회사명이 붙은 개별 점수는 공개 정보이거나 해당 조직이 명시적으로 허용한 경우가 아니면 외부에 노출하지 않습니다.
