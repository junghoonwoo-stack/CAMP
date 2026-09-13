# CAMP

**Company Agent Maturity Profile**

A ~10-minute assessment of how agent-native your company or team is — and what to do next.

CAMP returns:
- **CAMP Stage**
- **CAMP Score /100**
- scores across **5 dimensions**: AI Access, Delegation, Enterprise Connection, Knowledge Compounding, Role Transformation
- strengths and weak spots
- biggest bottleneck
- top 3 actions for the next 90 days
- practical AX / AI-native projects to start now

## CAMP Bench

If you contribute your assessment, **CAMP Bench** compares your organization with the benchmark dataset.

![CAMP Bench — illustrative example](assets/camp-bench.jpg)

*Illustrative example. Actual benchmark results depend on the available sample.*

Benchmark contributors can receive, when sample size is sufficient:
- **Overall percentile**
- **Industry percentile**
- **Peer Group percentile** by industry segment, size, country/region, scope, and function
- comparison across all 5 CAMP dimensions
- where your organization is unusually strong or weak

**Give to Get:** CAMP assessment is free. Benchmark comparison is available only when you contribute your assessment to CAMP Bench.

### Why CAMP Bench asks for your company name

For CAMP Bench, the survey asks for the **real company name**. It is used privately to:
- match multiple assessments from the same organization
- avoid counting one company several times
- track changes over time
- build more accurate peer groups
- compare different teams or functions inside the same organization

The company name is stored only in the **private identity registry**. It is **not shown in the CAMP report, benchmark charts, or public repository**.

If other people from the same company have already completed CAMP, CAMP Bench can analyze the organization together: mean/median, score distribution, team-level differences, and the dimensions where employees disagree most.

Named competitor scores are never exposed from confidential submissions. Detailed competitor analysis can use anonymous peer cohorts and, separately, named data that is public or explicitly authorized.

## Data architecture

**Public CAMP repository**
- framework and assessment logic
- schema and field definitions
- synthetic examples only
- no raw benchmark dataset
- no real company identity mapping

**Private CAMP Bench store**
- real company name ↔ anonymous Organization Group ID
- assessment history
- team / scope relationships
- benchmark metadata and data-quality controls

Reports use anonymous labels such as **Your organization**, **Industry**, and **Peer Group**.

## Future: CAMP Network

CAMP Bench can also become an opt-in AX marketplace. An organization that wants help may explicitly request support based on its diagnosed gaps. CAMP could then connect that organization with relevant AX consultants, implementation partners, or specialists.

**Benchmark participation never implies consent to be contacted or identified.** Identity is shared for an introduction only when the organization explicitly opts in.

## Quick start

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
```

### Claude Code
```bash
claude "Read SKILL.md and run the CAMP assessment."
```

### Codex CLI
```bash
codex
```
Then enter:
```text
Read SKILL.md and run the CAMP assessment.
```

### ChatGPT
Connect GitHub or upload `SKILL.md` + `references/`, then ask:
```text
Read SKILL.md and run the CAMP assessment.
```

## License

CAMP framework and documentation use **CC BY 4.0**. Running CAMP or using its results does not require attribution. If you redistribute or publish the framework or an adapted version, retain a link to the canonical project:

https://github.com/junghoonwoo-stack/CAMP

---

# CAMP

**Company Agent Maturity Profile**

약 10분 동안 **우리 회사나 팀이 얼마나 Agent-native한지, 다음에 무엇을 해야 하는지** 진단합니다.

CAMP는 다음을 제공합니다.
- **CAMP Stage**
- **CAMP Score /100**
- **5개 영역 점수**: AI Access, Delegation, Enterprise Connection, Knowledge Compounding, Role Transformation
- 강한 영역과 약한 영역
- 가장 큰 병목
- 향후 90일 Top 3 Action
- 바로 시도할 수 있는 AX / AI-native 과제

## CAMP Bench

진단 데이터를 제공하면 **CAMP Bench**가 다른 조직과 현재 위치를 비교해 줍니다.

![CAMP Bench — illustrative example](assets/camp-bench.jpg)

*위 그림은 예시이며 실제 Benchmark 결과는 확보된 표본에 따라 달라집니다.*

표본이 충분하면 다음을 제공합니다.
- **전체 조직 대비 Percentile**
- **같은 Industry 대비 Percentile**
- Industry Segment, 규모, 국가/지역, Scope, Function이 유사한 **Peer Group 대비 Percentile**
- CAMP 5개 영역별 비교
- 다른 조직 대비 특히 강한 영역과 약한 영역

**Give to Get:** CAMP 진단 자체는 무료입니다. CAMP Bench 비교는 자신의 진단 데이터를 Benchmark에 기여한 경우에만 제공합니다.

### 왜 실제 회사명을 묻나요?

CAMP Bench에서는 **실제 회사명**을 입력받습니다. 회사명은 외부 공개용이 아니라 다음을 위해 비공개로 사용합니다.
- 같은 회사의 여러 응답 연결
- 한 회사를 여러 회사처럼 중복 집계하지 않기
- 시간에 따른 변화 추적
- 더 정확한 Peer Group 구성
- 같은 회사 안의 팀·조직별 차이 분석

실제 회사명은 **Private Identity Registry에만 저장**하며 CAMP Report, Benchmark Chart, Public Repository에는 표시하지 않습니다.

같은 회사에서 이미 다른 사람이 CAMP를 수행했다면 여러 응답을 함께 분석해 **평균/중앙값, 점수 분포, 팀별 차이, 구성원 간 인식 차이가 큰 영역**도 보여줍니다.

비공개로 제공된 개별 경쟁사의 점수는 노출하지 않습니다. 상세 경쟁 비교는 익명 Peer Group을 기본으로 하고, 회사명이 붙은 분석은 공개자료 또는 명시적 허가가 있는 데이터만 사용합니다.

## 데이터 구조

**Public CAMP Repository**
- Framework와 진단 Logic
- Schema와 Field 정의
- Synthetic Example만 공개
- Raw Benchmark Dataset 없음
- 실제 회사명 Mapping 없음

**Private CAMP Bench Store**
- 실제 회사명 ↔ 익명 Organization Group ID
- 진단 이력
- Team / Scope 관계
- Benchmark Metadata와 Data Quality 관리

외부 Report에는 회사명 대신 **Your organization / Industry / Peer Group**처럼 익명화된 표현만 사용합니다.

## 향후: CAMP Network

CAMP Bench는 향후 opt-in 방식의 AX Marketplace로 확장할 수 있습니다. 진단 결과 특정 영역의 도움이 필요한 조직이 원할 경우, 해당 문제에 적합한 AX 컨설턴트·구축 파트너·전문가와 연결하는 방식입니다.

**Benchmark에 참여했다고 해서 영업 Lead가 되는 것은 아닙니다.** 조직이 별도로 연결을 요청한 경우에만 identity를 사용해 소개합니다.

## 빠른 시작

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
```

### Claude Code
```bash
claude "Read SKILL.md and run the CAMP assessment."
```

### Codex CLI
```bash
codex
```
실행 후 입력:
```text
Read SKILL.md and run the CAMP assessment.
```

### ChatGPT
GitHub를 연결하거나 `SKILL.md` + `references/`를 업로드한 뒤 입력:
```text
Read SKILL.md and run the CAMP assessment.
```

## License

CAMP Framework와 문서는 **CC BY 4.0**입니다. CAMP 실행이나 결과 사용에는 별도 출처 표기가 필요하지 않습니다. Framework 자체 또는 수정본을 재배포·공개할 때는 canonical project 링크를 유지합니다.

https://github.com/junghoonwoo-stack/CAMP
