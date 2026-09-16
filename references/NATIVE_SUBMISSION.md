# Native chat submission / 대화 안에서 제출

A repository link gives a chat instructions; it does not automatically add permission to call CAMP Bench. Direct in-chat submission works only when the chat product has a configured CAMP Action, connector, function, or equivalent integration.

Ordinary participants do not need to understand this setup. If a direct connection is unavailable, give them the unchanged submission JSON and the official browser page.

## ChatGPT owner setup

1. Create or edit a dedicated CAMP custom GPT.
2. Add the CAMP instructions and participant-facing question guide.
3. Add an Action and import:
   https://camp-bench-receiver.camp-bench-jhw.workers.dev/openapi.json
4. Use no authentication for the current public receiver. If authentication is enabled later, configure it inside the integration; never ask participants for a server token.
5. Test **submitCampAssessment** with an explicitly approved synthetic assessment.
6. Test **getCampReport** using the returned receipt.
7. Share the GPT only after the complete submission and report flow succeeds.

Publishing or sharing the GPT is a separate owner action. Provide the applicable privacy policy when the editor requests it. The platform may show its own confirmation before submission.

## Instructions for a connected chat

After the participant reviews the exact company, scope, and assessment fields and explicitly agrees:

1. Call **submitCampAssessment** with the confirmed fields.
2. Do not invent missing fields, a receipt, or success.
3. Keep the assessment date and every field unchanged on a retry.
4. Show the returned receipt and **report_url** immediately.
5. If the report is still processing, call **getCampReport** using the same receipt after the recommended interval.
6. Never submit again simply to retrieve a report.
7. If the Action is not actually available, say so and provide the unchanged JSON plus the official browser submission page.

A URL written in instructions is not a callable tool. Always respect platform confirmations and network policies.

The chat endpoint validates the same schema and consent as the local-agent and browser paths. It creates the same duplicate-prevention identity, stores the record before returning a receipt, and returns the original receipt when the same assessment is sent again.

## 한국어

CAMP Repository 주소를 대화에 넣는 것만으로 CAMP Bench 호출 권한이 생기지는 않습니다. 대화 안에서 바로 제출하려면 ChatGPT Action, Connector, Function 등 실제 CAMP 연결이 설정되어 있어야 합니다.

일반 참여자는 이 설정을 알 필요가 없습니다. 직접 연결이 없으면 대화가 원본 제출 JSON과 공식 브라우저 제출 페이지를 제공하면 됩니다.

### ChatGPT 소유자 설정

1. CAMP 전용 Custom GPT를 만들거나 수정
2. CAMP 지침과 참여자용 질문 가이드 추가
3. Action을 추가하고 다음 주소 Import  
   https://camp-bench-receiver.camp-bench-jhw.workers.dev/openapi.json
4. 현재 Public Receiver는 인증 없음으로 설정. 나중에 인증이 추가되면 Integration 안에서 안전하게 설정하고 참여자에게 Server Token을 요구하지 않음
5. 명시적으로 승인한 Synthetic Assessment로 **submitCampAssessment** 테스트
6. 반환된 접수번호로 **getCampReport** 테스트
7. 제출부터 리포트까지 전체 흐름이 성공한 뒤 GPT 공유

GPT 공개·공유는 별도 소유자 작업입니다. 편집 화면에서 요구하면 적용되는 Privacy Policy를 제공합니다. 플랫폼의 제출 확인 절차를 따릅니다.

### 연결된 대화가 따라야 할 규칙

참여자가 정확한 회사·범위·진단값을 확인하고 명시적으로 동의한 뒤:

1. 확인된 값으로 **submitCampAssessment** 호출
2. 누락값·접수번호·성공 여부를 만들어내지 않음
3. 재시도할 때 진단일과 모든 값을 그대로 유지
4. 반환된 접수번호와 **report_url**을 즉시 표시
5. 리포트가 준비 중이면 같은 접수번호로 **getCampReport** 조회
6. 리포트 조회를 위해 다시 제출하지 않음
7. Action이 실제로 없으면 원본 JSON과 공식 브라우저 제출 페이지 제공

지침에 적힌 URL은 호출 가능한 도구가 아닙니다. 플랫폼 확인 절차와 Network Policy를 항상 따릅니다.

대화용 Endpoint는 로컬 Agent·브라우저 제출과 같은 Schema와 동의를 검증합니다. 같은 중복 방지 기준을 사용하며, Record를 저장한 뒤 접수번호를 반환합니다. 같은 진단이 다시 들어오면 새 Record 대신 기존 접수번호를 반환합니다.

Official documentation: https://developers.openai.com/api/docs/actions/introduction and https://developers.openai.com/api/docs/actions/getting-started
