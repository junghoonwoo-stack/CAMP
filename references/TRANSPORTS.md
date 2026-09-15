# CAMP Bench transports / 제출 방식

CAMP Bench has one receiver and several ways to reach it. A repository URL or a skill file is not a network permission. Choose the first transport that the current assistant actually has; do not infer that a named tool is installed.

| Environment | Preferred transport | User action | Success |
|---|---|---|---|
| ChatGPT with a configured CAMP Action | `submitCampAssessment` | Confirm fields and consent; approve platform confirmation | Matching `receipt_id` |
| Claude with a configured CAMP MCP connector | `camp_bench_submit` | Confirm fields and consent; approve connector call | Matching `receipt_id` |
| Gemini with a configured function/extension | CAMP submission function | Confirm fields and consent; approve function call | Matching `receipt_id` |
| M365 Copilot with a configured Power Automate/connector flow | CAMP submission flow | Confirm fields and consent; approve flow | Matching `receipt_id` |
| Installed GitHub connector with private-repository write permission | Queue exact JSON in `submissions/inbox/<receipt_id>.json` | Confirm fields and consent; approve GitHub write | Commit and processed status |
| No native connector and no network access | Browser page | Choose exact JSON, review, press Submit | Matching `receipt_id` |

The native transports are adapters around `PUT /v1/chat/submissions/{request_key}`. `POST /v1/chat/submissions` remains compatible, but PUT is easier for connectors: generate one opaque request key once and reuse that URL/body on retries; no idempotency header or client-side hash is required. They are not automatically available in every product or account. A GitHub queue must use a private repository; never use a public issue or gist.

## Decision rule

1. Confirm the complete profile, score, dimensions, evidence, and explicit benchmark consent.
2. Inspect available tools. If a native CAMP tool is actually callable, use it. Do not use Python or shell merely because the receiver URL appears in instructions.
3. If no native tool is callable, stop repeated DNS attempts. State that the current environment has no permitted transport and provide the exact browser handoff.
4. A timeout or malformed response is **acceptance unconfirmed**. Only a verified matching receipt is accepted.
5. Never send to another endpoint, public issue, gist, paste site, email address, or model provider as an improvised relay.

OpenAPI: https://camp-bench-receiver.camp-bench-jhw.workers.dev/openapi.json

## Private GitHub queue

For assistants with genuine private-repository write access, write the exact validated JSON once to `submissions/inbox/<receipt_id>.json` in `junghoonwoo-stack/CAMP-Benchmark`. The private workflow validates and ingests it. A commit alone is not the final report; poll the receipt status until `report_status=ready`.

## Browser fallback

https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit?lang=ko

The page keeps the file local until consent and Submit. It calculates the same idempotency key, sends directly to the receiver, and displays the receipt/report link.

## 한국어

CAMP 저장소 주소나 지침에 제출 URL이 적혀 있다고 해당 대화에 인터넷 전송 권한이 생기는 것은 아닙니다. ChatGPT Action, Claude MCP, Gemini 함수/확장, M365 Power Automate 연결은 각각 별도 설정이며 모든 사용자에게 자동으로 존재하지 않습니다. 연결된 도구가 없으면 DNS 재시도를 반복하지 말고, 정확한 JSON과 중복 방지 키를 보존한 뒤 브라우저 제출을 안내합니다. 시간 초과나 이상한 응답은 “접수 확인 불가”로 표시하고, 일치하는 Receipt가 있을 때만 접수 성공으로 말합니다.
