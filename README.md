# CAMP

**Company Agent Maturity Profile**

CAMP is a ~10-minute assessment for one question: **How agent-native is this company or team, and what should it do next?**

A short interview or evidence review returns a CAMP Stage, a Score /100, five-dimension analysis, the biggest bottleneck, and concrete actions for the next 90 days.

## Quick Start

Install `git` and the CLI you intend to use first. The commands below do not install Claude Code or Codex.

### Claude Code

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git && cd CAMP
claude "Read SKILL.md and run the CAMP assessment."
```

### Codex

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git && cd CAMP
codex "Read SKILL.md and run the CAMP assessment."
```

### ChatGPT

Connect this repository, or upload `SKILL.md` and `references/`, then enter:

```text
Read SKILL.md and run the CAMP assessment.
```

## Choose one of two ways to run CAMP

The assessment is the same in both paths. Choose based on where the conversation is running:

| Path | Best for | CAMP Bench submission |
|---|---|---|
| **Local** | Claude Code, Codex, or a terminal on your computer/VM | Validate and send from that machine. A `receipt_id` confirms acceptance. |
| **Cloud chat** | ChatGPT, Claude, Gemini, M365 Copilot, or another hosted chat | Download the exact JSON and submit it in the official browser page. No GitHub account or installation is required. |

### Path A — Local installation

Use this when you can run commands on your own computer or VM. DNS, proxy, and firewall settings from that machine apply to the submission.

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
claude "Read SKILL.md and run the CAMP assessment."
# or: codex "Read SKILL.md and run the CAMP assessment."
```

After the report, explicitly agree to CAMP Bench and review the fields. Validate and submit from the same machine:

```bash
python3 scripts/camp_bench.py private-submissions/my-assessment.json
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --no-wait --language en
```

Only a returned `receipt_id` means the submission was accepted. Creating a JSON file is not submission, and a real file must never be committed to this public repository.

### Path B — Cloud chat (no installation)

Paste this into ChatGPT, Claude, Gemini, or another hosted chat:

```text
https://github.com/junghoonwoo-stack/CAMP

Read SKILL.md from this repository and run the CAMP assessment.
Ask the profile questions first, show progress, and ask one simple question at a time.
Use Korean unless I ask for English. Show the report when complete.
If I agree to CAMP Bench, prepare the exact private submission JSON for download.
```

For a safe dry run, add: `Run a test with synthetic Example Corp data; do not submit to CAMP Bench.`

If the cloud chat cannot make an outbound HTTPS request, it must not keep retrying. Download the unchanged `camp-bench-submission.json`, open the [official CAMP Bench submission page](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=en), choose the file, review it, and press **Submit** in the browser. Keep the returned `CB-...` receipt. Without it, the status is **NOT SUBMITTED**.

The browser sends directly to CAMP Bench, so the cloud chat does not need DNS access to the receiver. A configured native CAMP connector may submit directly; otherwise use this browser handoff. Never paste real company JSON into a public GitHub issue, discussion, pull request, or URL.

## What CAMP Measures

| Dimension | Core question |
|---|---|
| **AI Access** | How broadly can people use AI for work? |
| **AI Delegation** | How much real work is delegated to AI? |
| **Enterprise Connection** | Can AI use company context, data, tools, and systems? |
| **Knowledge Compounding** | Do skills, decisions, and session knowledge become reusable organizational assets? |
| **Role Transformation** | Are handoffs, role boundaries, and organization design changing around AI? |

Each dimension is scored 0–20 for a total **CAMP Score /100**. CAMP also reports a qualitative **Stage 0–5**. Stage and Score are intentionally separate: Stage describes the recurring operating model; Score shows how balanced the five capabilities are.

**AI Operations** and **Sovereign AI** are reported separately and do not increase the CAMP Score.

A CAMP report includes:
- Stage + confidence
- Score /100 and all five dimension scores
- strongest and weakest areas
- biggest bottleneck
- Top 3 actions for the next 90 days
- practical projects to start, refocus, merge, or stop
- AI Operations and Sovereign AI assessment

## CAMP Bench

CAMP Bench places an assessment in context.

![CAMP Bench — illustrative example](assets/camp-bench.svg)

*Illustrative example. Actual results depend on the available sample.*

When an assessment is submitted to CAMP Bench, it can be compared with:
- **Overall** — all eligible organizations for official benchmarks, or eligible and provisional organizations for an explicitly labeled preliminary benchmark
- **Industry** — organizations in the same broad industry
- **Peer Group** — similar organizations by segment, size, country/region, scope, and function
- **Five dimensions** — where the organization is relatively strong or weak

Submission now returns a private benchmark report. It tells the participant whether the organization is ahead of, in line with, or behind the overall median; shows percentile, mean, median, and the full score distribution; compares the five dimensions; and identifies the largest capability gap with a recommended next action. Industry ranking is added when that anonymous cohort contains at least 10 organizations.

Submitting the **real company name** improves the analysis because CAMP Bench can match previous assessments from the same company. If several people or teams from that company participate, the report can also show the company mean/median, score distribution, team/function differences, and dimensions with the largest internal disagreement. Repeated assessments enable longitudinal comparison.

CAMP Bench uses current operating evidence, not plans or isolated pilots. Accurate submissions make both the participant's own comparison and the aggregate benchmark more useful.

### Submit to CAMP Bench

Completing a CAMP assessment does **not** automatically submit it. After reviewing the standalone report, the participant reviews the exact fields, explicitly consents, and submits only through the configured private HTTPS receiver.

```bash
# Validate only — sends nothing
python3 scripts/camp_bench.py private-submissions/my-assessment.json

# Fast submit after consent — returns as soon as a receipt is accepted
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --no-wait --language en

# Retrieve the report again later
python3 scripts/camp_bench.py --status CB-YYYYMMDD-XXXXXXXXXXXX --language en
```

Submission acceptance and report generation are separate. A valid receipt confirms the submission immediately; the comparison report normally follows shortly. The receipt includes both `status_url` for JSON/API use and `report_url` for a bilingual, human-readable web report.

The official receiver is configured in `benchmark/submission.config.json`, so the submit command uses it automatically. A missing endpoint, network error, or response without a valid receipt still means **NOT SUBMITTED**. Never put a real submission in a public issue, discussion, pull request, or commit. See [CAMP Bench Submission](references/SUBMISSION.md).

### Privacy

The participant can see **their own company** in their private report. **Every other organization remains anonymized.** Individual respondent identities are never shown.

- The **private CAMP Bench store** contains real company identity mapping, raw assessment records, scope relationships, evidence, and history.
- The **public CAMP repository** contains only the framework, methodology, schemas, and synthetic examples.
- Public or shared benchmark views contain aggregate or anonymized results only.
- Confidential submissions are never used to expose another company's named score. Named-company comparisons require public information or explicit authorization.

Official percentiles require a sufficiently large cohort. If a cohort has fewer than 10 organizations, CAMP Bench broadens the cohort or reports that the sample is insufficient.

## Example Survey

```text
CAMP · Progress 1/13  █░░░░░░░░░░░░ 8%
Which organization are we assessing, and in which country is it based?
You: Example Corp, Korea.

CAMP · Progress 2/13  ██░░░░░░░░░░░ 15%
Should these answers describe the whole company, a business unit, or a team?
Why this matters: a team score and a company-wide score mean different things.
You: Business unit — Home Appliances.

CAMP · Progress 8/13  ████████░░░░░ 62%
In the strongest real production case, what company information or systems can AI use?
Why this matters: one core production case can prove the capability exists; Q1 separately measures how widely it has spread.
[A] External only  [B] Internal documents  [C] Work tools  [D] Core systems  [E] Can also take action
```

When the chat product supports native choice controls, the options appear as clickable choices. Otherwise the participant can answer with one letter. See the complete [interview wording and scope rule](references/QUESTION_GUIDE.md).

Example result:

```text
Stage 3 — Connected AI
CAMP Score: 40 / 100
Strongest: Enterprise Connection
Weakest: Role Transformation
Biggest bottleneck: Individual AI → Organizational Intelligence
Next target: build reusable skills and complete high-value end-to-end connections.
```

## Methodology

- [Stages and Agent definition](references/STAGES.md)
- [Diagnostic playbook and evidence rules](references/PLAYBOOK.md)
- [Participant-facing interview guide](references/QUESTION_GUIDE.md)
- [Report format](references/REPORT_TEMPLATE.md)
- [CAMP Bench methodology](references/BENCHMARK.md)
- [CAMP Bench submission](references/SUBMISSION.md)

## License

CAMP framework and documentation use **CC BY 4.0**. If you redistribute or publish the framework or an adapted version, retain a link to the canonical project.

---

# CAMP

**Company Agent Maturity Profile**

CAMP는 약 8–10분 동안 **우리 회사나 팀이 AI를 업무에 얼마나 실제로 활용하고 있으며, 다음에 무엇을 해야 하는지** 진단합니다.

짧은 질의응답이나 자료 검토를 통해 CAMP Stage, 총점 /100, 5개 영역 분석, 가장 큰 병목, 향후 90일 Action을 제공합니다.

## 바로 시작

먼저 `git`과 사용할 CLI를 설치해야 합니다. 아래 명령은 Claude Code나 Codex 자체를 설치하지 않습니다.

### Claude Code

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git && cd CAMP
claude "Read SKILL.md and run the CAMP assessment."
```

### Codex

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git && cd CAMP
codex "Read SKILL.md and run the CAMP assessment."
```

### ChatGPT

이 Repository를 연결하거나 `SKILL.md`와 `references/`를 업로드한 뒤 입력합니다.

```text
Read SKILL.md and run the CAMP assessment.
```

## CAMP를 사용하는 두 가지 표준 경로

진단 내용은 어느 환경에서든 같습니다. 대화가 어디에서 실행되는지에 따라 한 가지를 선택합니다.

| 경로 | 적합한 경우 | CAMP Bench 제출 |
|---|---|---|
| **로컬** | 내 PC·VM에서 Claude Code, Codex, 터미널을 실행할 때 | 같은 환경에서 JSON을 검증하고 전송합니다. `receipt_id`가 있어야 접수 성공입니다. |
| **클라우드 대화** | ChatGPT·Claude·Gemini·M365 Copilot 등 호스팅된 대화에서 실행할 때 | JSON 파일을 내려받아 공식 웹페이지에서 제출합니다. 설치와 GitHub 계정이 필요 없습니다. |

### 경로 A — 로컬 설치

내 PC나 VM에서 실행할 때 사용합니다. 제출 요청도 그 컴퓨터에서 나가므로 DNS·Proxy·방화벽 설정을 그대로 사용합니다.

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
claude "Read SKILL.md and run the CAMP assessment."
# 또는: codex "Read SKILL.md and run the CAMP assessment."
```

Report를 확인하고 CAMP Bench 제출에 동의한 뒤 같은 환경에서 검증·제출합니다.

```bash
python3 scripts/camp_bench.py private-submissions/my-assessment.json
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --no-wait --language ko
```

`receipt_id`가 반환되어야 접수 성공입니다. JSON 파일을 만든 것만으로 제출된 것이 아니며, 실제 파일을 Public Repository에 Commit하면 안 됩니다.

### 경로 B — 클라우드 대화 (설치 없음)

ChatGPT·Claude·Gemini 등 호스팅된 대화창에 아래 내용을 붙여 넣습니다.

```text
https://github.com/junghoonwoo-stack/CAMP

이 Repository의 SKILL.md를 읽고 CAMP 진단을 실행해줘.
먼저 조직 정보를 묻고, 진행률을 표시하며, 쉬운 질문을 한 번에 하나씩 해줘.
영어로 요청하기 전까지는 한국어로 진행해줘. 진단이 끝나면 Report를 보여줘.
CAMP Bench 제출에 동의하면 제출용 원본 JSON 파일을 다운로드할 수 있게 만들어줘.
```

안전한 테스트만 하려면 마지막에 `Synthetic Example Corp 데이터로 테스트하고 CAMP Bench에는 제출하지 마.`를 덧붙입니다.

클라우드 대화가 외부 HTTPS 요청을 보내지 못하면 반복 시도하지 않습니다. 원본 `camp-bench-submission.json`을 내려받아 [공식 CAMP Bench 제출 페이지](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=ko)를 열고, 파일을 선택·검토한 뒤 브라우저에서 **Submit**을 누릅니다. `CB-...` 접수번호가 없으면 **NOT SUBMITTED**입니다.

브라우저가 CAMP Bench로 직접 전송하므로 클라우드 대화의 DNS 권한이 없어도 됩니다. 실제 CAMP Connector가 연결된 경우에만 대화에서 직접 제출할 수 있습니다. 실제 회사 JSON을 Public GitHub Issue·Discussion·Pull Request·URL에 넣지 않습니다.

## 무엇을 측정하나

| Dimension | 핵심 질문 |
|---|---|
| **AI Access** | 얼마나 많은 사람이 업무에서 AI를 사용할 수 있는가? |
| **AI Delegation** | 실제 업무를 어느 수준까지 AI에 위임하는가? |
| **Enterprise Connection** | AI가 회사 Context, Data, Tool, System을 사용할 수 있는가? |
| **Knowledge Compounding** | Skill, 판단, Session Knowledge가 조직 자산으로 축적·재사용되는가? |
| **Role Transformation** | Handoff와 직무 경계, 조직 구조가 AI를 중심으로 바뀌고 있는가? |

각 영역은 0–20점, 총 **CAMP Score /100**입니다. 별도로 **Stage 0–5**를 제공합니다. Stage는 현재 반복되는 Operating Model을, Score는 5개 역량의 균형을 보여주므로 둘은 반드시 같이 움직이지 않습니다.

**AI Operations**와 **Sovereign AI**는 별도로 평가하며 CAMP Score에는 포함하지 않습니다.

최종 Report에는 다음이 포함됩니다.
- Stage + Confidence
- CAMP Score /100과 5개 영역 점수
- 가장 강한 영역과 약한 영역
- 가장 큰 병목
- 다음 90일 Top 3 Action
- 시작·재집중·통합·중단할 과제
- AI Operations / Sovereign AI

## CAMP Bench

CAMP Bench는 진단 결과를 다른 조직의 분포 안에서 보여줍니다.

![CAMP Bench — illustrative example](assets/camp-bench.svg)

*위 그림은 예시이며 실제 결과는 확보된 표본에 따라 달라집니다.*

CAMP Bench에 진단 결과를 제출하면 다음과 비교할 수 있습니다.
- **Overall** — 정식 Benchmark에서는 전체 적격 조직 대비, `preliminary`로 명시된 초기 Benchmark에서는 적격·잠정 조직 대비
- **Industry** — 같은 대분류 업종 대비
- **Peer Group** — Segment, 규모, 국가/지역, Scope, Function이 유사한 조직 대비
- **5개 Dimension** — 상대적으로 강한 영역과 약한 영역

제출하면 Private Benchmark Report를 돌려받습니다. 전체 중앙값보다 앞서는지, 비슷한지, 뒤처지는지와 Percentile·평균·중앙값·전체 점수 분포를 보여줍니다. 5개 Dimension을 비교해 가장 부족한 영역과 다음 Action도 알려줍니다. 동종업계 익명 표본이 10개 조직 이상이면 Industry 순위와 분포도 함께 제공합니다.

**실제 회사명**을 제출하면 같은 회사의 기존 진단을 연결할 수 있어 비교가 더 정확해집니다. 같은 회사에서 여러 사람이나 팀이 참여했다면 평균/중앙값, 점수 분포, 팀·Function별 차이, 내부 인식 차이가 큰 영역까지 볼 수 있습니다. 반복 진단은 시간에 따른 변화도 보여줍니다.

CAMP Bench는 계획이나 단일 Pilot보다 **현재 반복적으로 운영되는 상태**를 기준으로 합니다. 정확한 답변을 제출할수록 본인 회사의 비교도, 전체 Benchmark도 더 유용해집니다.

### CAMP Bench에 제출

CAMP 진단을 완료해도 자동으로 제출되지는 않습니다. Standalone Report를 확인한 뒤 실제 전송 항목을 검토하고 명시적으로 동의한 경우에만 설정된 Private HTTPS Receiver로 제출합니다.

```bash
# 검증만 수행 — 전송하지 않음
python3 scripts/camp_bench.py private-submissions/my-assessment.json

# 동의 후 빠른 제출 — Receipt가 오면 즉시 반환
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --no-wait --language ko

# 나중에 Report 다시 조회
python3 scripts/camp_bench.py --status CB-YYYYMMDD-XXXXXXXXXXXX --language ko
```

제출 접수와 리포트 생성은 별도입니다. 유효한 Receipt가 오면 제출은 즉시 완료된 것이며, 비교 리포트는 보통 잠시 뒤 준비됩니다. Receipt에는 개발·연동용 JSON `status_url`과 한·영 사용자용 웹 리포트 `report_url`이 함께 제공됩니다.

공식 Receiver는 `benchmark/submission.config.json`에 설정되어 있어 제출 명령이 자동으로 사용합니다. Endpoint 누락, Network Error, 유효한 Receipt가 없는 응답은 모두 **NOT SUBMITTED**입니다. 실제 제출 파일을 Public Issue, Discussion, Pull Request, Commit에 올리면 안 됩니다. 자세한 절차는 [CAMP Bench Submission](references/SUBMISSION.md)을 참고합니다.

### Privacy

참여자는 자신의 Private Report에서 **자기 회사**를 볼 수 있습니다. **다른 회사는 모두 익명화**됩니다. 개인 응답자의 identity는 표시하지 않습니다.

- **Private CAMP Bench Store**: 실제 회사명 Mapping, 원본 진단 Record, Scope 관계, Evidence, 시계열
- **Public CAMP Repository**: Framework, Methodology, Schema, Synthetic Example만 포함
- 외부에 공유되는 Benchmark는 Aggregate 또는 익명화 결과만 사용
- 비공개 제출 데이터를 이용해 다른 회사의 실명 점수를 노출하지 않음. Named Company 비교는 공개정보 또는 명시적 허가가 있는 경우만 사용

공식 Percentile은 충분한 표본이 있을 때만 제공합니다. Cohort가 10개 조직 미만이면 더 넓은 그룹으로 비교하거나 표본 부족으로 표시합니다.

## 설문 예시

```text
CAMP · 진행 1/13  █░░░░░░░░░░░░ 8%
어느 회사 또는 조직을 진단할까요? 국가는 어디인가요?
응답: 예시전자, 한국.

CAMP · 진행 2/13  ██░░░░░░░░░░░ 15%
회사 전체, 사업부·본부, 팀·부서 중 어느 범위를 기준으로 답할까요?
왜 묻나요: 한 팀의 점수와 회사 전체의 점수는 의미가 다릅니다.
응답: 사업본부 — 생활가전.

CAMP · 진행 8/13  ████████░░░░░ 62%
이 범위 안의 가장 앞선 실제 운영 사례에서, AI는 어떤 회사 자료나 시스템까지 사용할 수 있나요?
왜 묻나요: 핵심 운영사례 하나로 역량의 존재를 확인할 수 있고, 얼마나 널리 퍼졌는지는 Q1에서 따로 봅니다.
[A] 외부지식  [B] 사내문서  [C] 협업도구  [D] 핵심시스템  [E] 실행까지
```

대화 환경이 지원하면 선택지는 클릭형으로 표시됩니다. 지원하지 않으면 글자 하나만 답하면 됩니다. 전체 문구와 범위 기준은 [인터뷰 가이드](references/QUESTION_GUIDE.md)를 참고하세요.

예시 결과:

```text
Stage 3 — Connected AI
CAMP Score: 40 / 100
강점: Enterprise Connection
약점: Role Transformation
가장 큰 병목: Individual AI → Organizational Intelligence
다음 목표: 재사용 가능한 Skill과 핵심 업무의 End-to-End 연결 강화
```

## Methodology

- [Stage와 Agent 정의](references/STAGES.md)
- [진단 Playbook과 Evidence 기준](references/PLAYBOOK.md)
- [참여자용 인터뷰 가이드](references/QUESTION_GUIDE.md)
- [Report 형식](references/REPORT_TEMPLATE.md)
- [CAMP Bench 기준](references/BENCHMARK.md)
- [CAMP Bench 제출 절차](references/SUBMISSION.md)

## License

CAMP Framework와 문서는 **CC BY 4.0**입니다. Framework 또는 수정본을 외부에 재배포·공개할 때 canonical project 링크를 유지합니다.

### Chat cannot submit? / 대화에서 제출이 안 되나요?

Open [CAMP Bench submission](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=en), choose the submission JSON from your CAMP conversation, review it, and press Submit. No installation or GitHub account is needed. Keep the receipt and report link. This path uses your browser connection when the chat environment cannot reach the server.

[CAMP Bench 제출 페이지](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=ko)에서 대화 중 만든 제출용 JSON 파일을 선택하고, 내용을 확인한 뒤 제출하세요. 설치나 GitHub 계정은 필요 없습니다. 접수번호와 리포트 링크를 보관하세요. 대화 환경에서 전송이 막혀도 사용자 브라우저로 제출할 수 있습니다.

Survey questions are available in plain English and Korean. You can answer through everyday work examples without knowing AI technology terms.
설문은 한국어·영어 모두 실제 업무 사례를 기준으로 쉽게 답하도록 구성했습니다. AI 기술 용어를 알 필요는 없습니다.
