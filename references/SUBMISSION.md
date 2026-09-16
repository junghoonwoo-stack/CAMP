# CAMP Bench Submission

CAMP Bench submission is an optional step after the assessment. Finishing a CAMP assessment does **not** automatically send any data.

## English

### What happens after the report

After showing the complete CAMP report, the agent automatically explains the private comparison and asks whether the participant wants to join CAMP Bench. The participant only needs to choose **Yes** or **Not now**; they do not need to request submission first.

If the participant chooses Yes, the agent must:

1. Check that the company profile and all assessment results are complete.
2. Show a short summary of exactly what will be sent.
3. Explain the private comparison the participant will receive.
4. Ask for explicit final transmission consent.
5. Submit through an available direct connection or provide the official browser handoff.
6. Show the returned **CB-** receipt and private report link.

A receipt is the only proof that the submission was accepted.

### Two submission outcomes

**Local agent or configured direct connection**

Codex, Claude Code, or another agent running on the participant's computer submits through the repository's configured receiver. The participant should not need to run a separate validation or submission command.

**Hosted chat without a direct connection**

ChatGPT, Claude, Gemini, or another hosted chat creates the exact file **camp-bench-submission.json**. The participant then:

1. Downloads the file.
2. Opens the [official CAMP Bench submission page](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=en).
3. Selects the file and reviews the preview.
4. Gives consent and presses **Submit**.
5. Keeps the returned receipt and report link.

No GitHub account, token, terminal, or software installation is required for browser submission. The file stays in the browser until the participant presses Submit.

### What is included

- Company name and optional business-unit or team label
- Country, industry, size, scope, and function
- Respondent role category
- Stage, total score, and five area scores
- Supporting capability answers, evidence level, and confidence
- An optional short evidence summary

Personal name, email, phone number, employee ID, credentials, and raw internal documents are excluded.

The company name is used privately to match repeated assessments from the same organization. The participant may see their own organization by name; every other organization remains anonymous.

### Success and failure

- **CB- receipt returned:** accepted
- **Valid receipt, report still processing:** accepted; use the same report link later
- **No receipt before any request was sent:** not submitted
- **Timeout or invalid response after a request may have been sent:** acceptance unconfirmed

Agents must keep the exact same data and duplicate-prevention key during retries. They must not create a new submission while checking the original receipt. Temporary connection errors may be retried up to three total attempts. Validation, permission, certificate, or malformed-receipt errors are not retried automatically.

Never place a real submission in a public GitHub issue, discussion, pull request, commit, URL, email, or paste service.

### Receiver contract for agent integrations

The official receiver accepts schema 1.0 JSON over HTTPS. Agent integrations may use an idempotent PUT request or the compatible POST endpoint. The receiver validates the data, stores it outside the public repository, and returns a receipt, status URL, and human-readable report URL.

A repeated request with the same data returns the original receipt instead of creating a duplicate. Detailed fields are defined in [Native submission](NATIVE_SUBMISSION.md) and the [submission schema](../benchmark/submission.schema.json).

---

## 한국어

CAMP Bench 제출은 진단이 끝난 뒤 선택하는 별도 단계입니다. CAMP 진단을 완료해도 데이터가 자동으로 전송되지는 않습니다.

### Report 이후 자동 안내

완전한 CAMP Report를 보여준 뒤 Agent가 비공개 비교 혜택을 설명하고 CAMP Bench 참여 여부를 자동으로 묻습니다. 참여자는 **예** 또는 **지금은 안 함**만 선택하면 되며, 먼저 제출을 요청할 필요가 없습니다.

참여자가 예를 선택하면 Agent는 다음 순서로 진행해야 합니다.

1. 회사 정보와 진단 결과가 모두 준비됐는지 확인
2. 실제 전송할 내용을 짧게 보여주기
3. 제출 후 받을 비공개 비교 결과 설명
4. 실제 전송에 대한 명시적인 최종 동의 확인
5. 가능한 직접 연결로 제출하거나 공식 브라우저 제출 안내
6. 반환된 **CB-** 접수번호와 비공개 리포트 링크 표시

접수번호가 있어야 제출 성공입니다.

### 두 가지 제출 결과

**로컬 Agent 또는 직접 연결이 있는 경우**

Codex, Claude Code 등 사용자의 컴퓨터에서 실행되는 Agent가 Repository에 설정된 공식 Receiver로 바로 제출합니다. 참여자가 별도의 검증 명령이나 제출 명령을 실행할 필요는 없습니다.

**직접 연결이 없는 대화형 AI**

ChatGPT, Claude, Gemini 등의 대화가 정확한 **camp-bench-submission.json** 파일을 만들어 줍니다. 참여자는 다음만 하면 됩니다.

1. 파일 다운로드
2. [공식 CAMP Bench 제출 페이지](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=ko) 열기
3. 파일 선택 후 화면의 내용 확인
4. 동의하고 **제출** 누르기
5. 접수번호와 리포트 링크 보관

브라우저 제출에는 GitHub 계정, Token, Terminal 또는 별도 설치가 필요 없습니다. 제출 버튼을 누르기 전에는 파일이 전송되지 않습니다.

### 전송되는 내용

- 실제 회사명과 선택적 사업부·팀 이름
- 국가, 업종, 규모, 진단 범위, 기능
- 응답자 역할 범주
- Stage, 총점, 다섯 영역 점수
- 보조 역량 답변, 실제 근거 수준, Confidence
- 선택적인 짧은 근거 요약

개인 이름·이메일·전화번호·사번·Credential·원문 사내자료는 제외합니다.

회사명은 같은 조직의 반복 진단을 연결하기 위해 비공개로 사용합니다. 참여자는 자기 조직을 실명으로 볼 수 있지만 다른 조직은 모두 익명입니다.

### 성공과 실패 기준

- **CB- 접수번호 반환:** 접수 성공
- **접수번호가 있고 리포트가 준비 중:** 접수 성공, 같은 링크에서 나중에 확인
- **요청을 보내기 전 실패하고 접수번호 없음:** 미제출
- **요청 후 시간 초과 또는 이상한 응답:** 접수 확인 불가

재시도할 때는 같은 데이터와 중복 방지 키를 유지합니다. 기존 접수 상태를 확인하는 동안 새 제출을 만들지 않습니다. 일시적인 연결 오류는 총 세 번까지 시도할 수 있지만 입력값·권한·인증서·잘못된 접수번호 오류는 자동 재시도하지 않습니다.

실제 제출 데이터를 Public GitHub Issue·Discussion·Pull Request·Commit·URL·Email·Paste Service에 넣지 않습니다.

### Agent 연동을 위한 Receiver 규칙

공식 Receiver는 Schema 1.0 JSON을 HTTPS로 받습니다. Agent 연동은 중복 방지 PUT 또는 호환 POST Endpoint를 사용할 수 있습니다. Receiver는 데이터를 검증해 Public Repository 밖에 저장하고 접수번호, 상태 주소, 사람이 읽는 리포트 주소를 반환합니다.

같은 데이터가 다시 들어오면 새 Record 대신 기존 접수번호를 반환합니다. 상세 항목은 [Native submission](NATIVE_SUBMISSION.md)과 [Submission Schema](../benchmark/submission.schema.json)를 참고합니다.
