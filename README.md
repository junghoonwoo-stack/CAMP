# CAMP

**Company Agent Maturity Profile**

A ~10-minute assessment for one question: **How agent-native is your organization, and what should you do next?**

CAMP returns:
- CAMP Stage
- CAMP Score /100
- biggest bottleneck
- top 3 actions for the next 90 days
- recommended AX / AI-native projects
- optional benchmark percentile

It works in two modes:
- **Interview:** answer a short guided survey.
- **Evidence:** add AX proposals, agent specs, RAG/MCP architecture, usage data, or related files; CAMP reads them first and asks only what is missing.

Multiple people from the same organization can assess separately. Use the same anonymous **Organization Group ID** and different **Respondent IDs**. CAMP can show both individual results and an aggregated organization view.

## Quick start

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
```

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude "Read SKILL.md and run the CAMP assessment."
```

### Codex CLI

```bash
npm install -g @openai/codex
codex --login
codex
```

Then enter:

```text
Read SKILL.md and run the CAMP assessment.
```

### ChatGPT

Either connect GitHub and ask:

```text
Use junghoonwoo-stack/CAMP. Read SKILL.md and run the CAMP assessment.
```

or upload `SKILL.md` and the Markdown files under `references/`, then use the same prompt.

---

# CAMP

**Company Agent Maturity Profile**

약 10분 동안 **우리 조직이 얼마나 Agent-native한지, 다음에 무엇을 해야 하는지** 진단합니다.

결과로 다음을 제공합니다.
- CAMP Stage
- CAMP Score /100
- 가장 큰 병목
- 향후 90일 Top 3 Action
- 추천 AX / AI-native 과제
- 선택형 Benchmark 순위

두 방식으로 사용할 수 있습니다.
- **Interview:** 짧은 설문에 답합니다.
- **Evidence:** AX 제안서, Agent 문서, RAG/MCP 아키텍처, 사용 데이터 등을 넣으면 먼저 읽고 부족한 부분만 질문합니다.

한 회사에서 여러 명이 각각 진단할 수도 있습니다. 같은 익명 **Organization Group ID**를 쓰고, 사람마다 다른 **Respondent ID**를 사용하면 개인 결과와 조직 종합 결과를 함께 볼 수 있습니다.

## 빠른 시작

```bash
git clone https://github.com/junghoonwoo-stack/CAMP.git
cd CAMP
```

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude "Read SKILL.md and run the CAMP assessment."
```

### Codex CLI

```bash
npm install -g @openai/codex
codex --login
codex
```

실행 후 입력합니다.

```text
Read SKILL.md and run the CAMP assessment.
```

### ChatGPT

GitHub를 연결한 뒤 다음과 같이 요청합니다.

```text
Use junghoonwoo-stack/CAMP. Read SKILL.md and run the CAMP assessment.
```

또는 `SKILL.md`와 `references/` 아래 Markdown 파일을 업로드한 뒤 같은 문장을 입력합니다.
