# CAMP

**Company Agent Maturity Profile**

A ~10-minute assessment of how agent-native a company or team is — and what to do next.

## Start

| Tool | Run |
|---|---|
| ChatGPT | Connect this GitHub repo, or upload `SKILL.md` + `references/`, then ask: `Read SKILL.md and run the CAMP assessment.` |
| Claude Code | `claude "Read SKILL.md and run the CAMP assessment."` |
| Codex | Run `codex`, then enter: `Read SKILL.md and run the CAMP assessment.` |

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
```

## What CAMP returns

| Output | What it shows |
|---|---|
| **CAMP Stage** | Stage 0–5 maturity |
| **CAMP Score** | Overall score /100 |
| **5 Dimensions** | AI Access, Delegation, Enterprise Connection, Knowledge Compounding, Role Transformation |
| **Diagnosis** | Strengths, weak spots, and the biggest bottleneck |
| **Next 90 Days** | Top 3 actions and practical AX / AI-native projects |
| **AI Operations / Sovereign AI** | Supporting operating and model capabilities |

## CAMP Bench

When an assessment is included in **CAMP Bench**, the report can compare the organization with other assessments.

![CAMP Bench — illustrative example](assets/camp-bench.svg)

*Illustrative example. Actual results depend on the available sample.*

| Comparison | What it shows |
|---|---|
| **Overall** | Position across all organizations |
| **Industry** | Position within the same industry |
| **Peer Group** | Similar organizations by segment, size, country/region, scope, and function |
| **5 Dimensions** | Where the organization is unusually strong or weak |
| **Same Company** | Mean/median, distribution, team/function differences, and areas of disagreement when multiple responses exist |

CAMP Bench asks for the **real company name** so responses from the same organization can be matched, duplicates can be avoided, and team-level or longitudinal analysis can be performed. The company name is kept in the **private identity registry** and is not shown in benchmark reports or charts.

## Data

| Location | Contains |
|---|---|
| **Public CAMP repo** | Framework, scoring logic, schema, field definitions, synthetic examples |
| **Private benchmark store** | Company identity mapping, assessment records, team/scope relationships, history |
| **Reports** | Anonymized organization, industry, and peer-group comparisons |

Named competitor scores from private submissions are not exposed. Peer comparisons use anonymized cohorts; named-company analysis requires public or explicitly authorized data.

## License

CAMP framework and documentation use **CC BY 4.0**. If you redistribute or publish the framework or an adapted version, retain a link to the canonical project.

---

# CAMP

**Company Agent Maturity Profile**

약 10분 동안 **우리 회사나 팀이 얼마나 Agent-native한지, 다음에 무엇을 해야 하는지** 진단합니다.

## 바로 시작

| Tool | 실행 |
|---|---|
| ChatGPT | 이 GitHub repo를 연결하거나 `SKILL.md` + `references/`를 업로드한 뒤 `Read SKILL.md and run the CAMP assessment.` 입력 |
| Claude Code | `claude "Read SKILL.md and run the CAMP assessment."` |
| Codex | `codex` 실행 후 `Read SKILL.md and run the CAMP assessment.` 입력 |

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
```

## CAMP 결과

| Output | 내용 |
|---|---|
| **CAMP Stage** | Stage 0–5 현재 수준 |
| **CAMP Score** | 총점 /100 |
| **5개 Dimension** | AI Access, Delegation, Enterprise Connection, Knowledge Compounding, Role Transformation |
| **Diagnosis** | 강점, 약점, 가장 큰 병목 |
| **Next 90 Days** | Top 3 Action과 바로 시도할 AX / AI-native 과제 |
| **AI Operations / Sovereign AI** | 운영 및 모델 관련 Supporting Capability |

## CAMP Bench

진단 결과가 **CAMP Bench**에 포함되면 다른 조직과 현재 위치를 비교할 수 있습니다.

![CAMP Bench — illustrative example](assets/camp-bench.svg)

*위 그림은 예시이며 실제 결과는 확보된 표본에 따라 달라집니다.*

| 비교 | 내용 |
|---|---|
| **Overall** | 전체 조직 대비 위치 |
| **Industry** | 같은 업종 대비 위치 |
| **Peer Group** | Segment, 규모, 국가/지역, Scope, Function이 유사한 조직 대비 위치 |
| **5개 Dimension** | 다른 조직 대비 특히 강한 영역과 약한 영역 |
| **Same Company** | 여러 응답이 있으면 평균/중앙값, 분포, 팀·Function별 차이, 인식 차이가 큰 영역 |

CAMP Bench에서는 **실제 회사명**을 입력받아 같은 회사의 여러 응답을 연결하고, 중복 집계를 막고, 팀별·시계열 분석에 활용합니다. 회사명은 **Private Identity Registry에만 저장**하며 Benchmark Report나 Chart에는 표시하지 않습니다.

## 데이터

| 위치 | 저장 내용 |
|---|---|
| **Public CAMP Repo** | Framework, Scoring Logic, Schema, Field 정의, Synthetic Example |
| **Private Benchmark Store** | 실제 회사명 Mapping, 진단 Record, Team/Scope 관계, 이력 |
| **Report** | 익명화된 조직 / Industry / Peer Group 비교 |

비공개 제출에서 특정 경쟁사의 개별 점수를 노출하지 않습니다. Peer 비교는 익명 Cohort를 사용하고, 회사명이 붙는 분석은 공개자료 또는 명시적으로 허가된 데이터만 사용합니다.

## License

CAMP Framework와 문서는 **CC BY 4.0**입니다. Framework 자체 또는 수정본을 외부에 재배포·공개할 때 canonical project 링크를 유지합니다.
