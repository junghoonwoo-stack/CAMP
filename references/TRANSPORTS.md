# CAMP Bench submission paths

The participant does not need to choose a technical path before the assessment. Ask about CAMP Bench only after the standalone report is complete.

## Simple decision

| Where CAMP is running | What happens after consent | Participant action |
|---|---|---|
| **Codex, Claude Code, or another local agent** | The agent validates and submits through the configured official receiver | Review the fields and approve |
| **Hosted chat with a real CAMP connection** | The chat submits through that connection | Review the fields and approve the platform confirmation |
| **ChatGPT, Claude, Gemini, or another hosted chat without a direct connection** | The chat creates the unchanged submission JSON | Download it and upload it on the official browser page |

Official browser page:

- [English](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=en)
- [한국어](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=ko)

No GitHub account is required. The page keeps the file local until the participant reviews it, consents, and presses Submit.

A repository URL provides instructions; it does not give a hosted chat permission to access the internet. Do not repeatedly try unavailable network methods. If direct submission is unavailable, move immediately to the browser handoff.

Only a matching **CB-** receipt confirms acceptance. A timeout after sending means acceptance is unconfirmed, because the receiver may already have stored the record. Preserve the exact file and duplicate-prevention key while checking the original receipt.

Never use a public issue, gist, paste site, email, URL parameter, or another model provider as an improvised relay.

For configured agent integrations, see [Native submission](NATIVE_SUBMISSION.md).

---

## 한국어

참여자는 진단을 시작하기 전에 기술적인 제출 방식을 선택할 필요가 없습니다. Standalone Report가 완성된 뒤 CAMP Bench 참여 여부를 확인합니다.

| CAMP 실행 환경 | 동의 후 진행 방식 | 참여자가 할 일 |
|---|---|---|
| **Codex·Claude Code 등 로컬 Agent** | Agent가 공식 Receiver로 검증하고 바로 제출 | 전송 항목 확인 후 승인 |
| **CAMP 직접 연결이 실제로 있는 대화형 AI** | 연결된 도구로 바로 제출 | 전송 항목과 플랫폼 확인 절차 승인 |
| **직접 연결이 없는 ChatGPT·Claude·Gemini 등** | 대화가 원본 제출 JSON 생성 | 파일을 내려받아 공식 웹페이지에서 제출 |

공식 제출 페이지:

- [한국어](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=ko)
- [English](https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=en)

GitHub 계정은 필요 없습니다. 참여자가 내용을 확인하고 동의한 뒤 제출 버튼을 누르기 전까지 파일은 전송되지 않습니다.

Repository 주소는 실행 지침일 뿐 대화 환경에 인터넷 권한을 주지는 않습니다. 직접 제출이 불가능하면 다른 Network 방법을 반복하지 말고 바로 브라우저 제출로 전환합니다.

일치하는 **CB-** 접수번호가 있어야 접수 성공입니다. 전송 후 시간 초과가 발생하면 이미 저장됐을 수 있으므로 접수 확인 불가로 표시합니다. 같은 파일과 중복 방지 키를 유지하면서 원래 접수 상태만 확인합니다.

Public Issue·Gist·Paste Site·Email·URL Parameter·다른 Model Provider를 임시 전송 통로로 사용하지 않습니다.

설정된 Agent 연동의 상세 규칙은 [Native submission](NATIVE_SUBMISSION.md)을 참고합니다.
