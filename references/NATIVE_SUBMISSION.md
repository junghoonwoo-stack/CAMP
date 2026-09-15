# Native chat submission / 대화 안에서 제출

A repository link gives a model instructions; it does not install a network tool. Repeated DNS failures in a Python execution environment cannot be fixed by instructions or retries alone. Use a registered GPT Action to call CAMP Bench through the platform's API integration, without uploading a file or asking the participant for a GitHub account. This is an additional integration, not automatically enabled in ordinary chats.

## One-time owner setup

1. Create or edit a dedicated CAMP custom GPT in the ChatGPT GPT editor.
2. Add CAMP instructions and the question guide as its knowledge/instructions. Add the submission instructions below.
3. Add an Action, import https://camp-bench-receiver.camp-bench-jhw.workers.dev/openapi.json and choose no authentication for the current public CAMP receiver. If bearer protection is enabled later, configure the integration securely; do not ask participants for the server's token.
4. Test submitCampAssessment with an explicitly approved test assessment, then getCampReport with the returned receipt. Publishing or sharing the GPT is a separate owner action. Supply the applicable privacy policy when the editor requests it.
5. Share that GPT with participants after a successful native Action test. No GitHub access or Python execution is needed by participants. The platform may show its own action confirmation.

The new POST /v1/chat/submissions validates the same schema and consent, uses the same rate limit and private GitHub App, and derives the exact same idempotency key and receipt as the CLI and browser. It accepts no client-side hash requirement, so the model does not need to run Python just to prepare a hash. It saves durably before returning a receipt. The existing POST /v1/submissions keeps its required Idempotency-Key header.

## Instructions for the GPT

After the participant confirms the exact company, scope and assessment fields and agrees to submit, call submitCampAssessment directly with those fields. Do not generate or run a Python submission script when this Action is available. Do not invent missing fields, hashes, receipts, or success. Keep the assessment date and every field unchanged on retries. Immediately show the returned receipt and report_url. If needed, call getCampReport after at least 15 seconds; follow Retry-After on 429. Never resubmit just to get a report. If the Action is absent, explain that it is not connected; a URL in the instructions is not a callable tool. Respect platform confirmations and network policies.

## 한국어

CAMP 저장소 주소를 대화에 넣는 것만으로 제출 도구가 설치되지는 않습니다. Python 실행환경의 DNS가 계속 실패한다면, 반복 재시도만으로 해결할 수 없습니다. 전용 CAMP GPT에 공식 Action을 한 번 연결하면 대화 중 확인한 진단 JSON을 플랫폼의 API 연결로 보낼 수 있습니다. 사용자가 파일을 다시 올리거나 GitHub에 가입할 필요는 없습니다.

소유자가 GPT 편집 화면에서 Action을 추가하고 위 openapi.json 주소를 가져온 뒤, 현재 공개 제출 서버에는 인증 없음으로 설정합니다. 제출과 리포트 조회를 실제 Action으로 테스트한 후 GPT를 공유합니다. 이 등록은 서버 배포와 별개의 작업이며, 설정 전에는 일반 대화에서 자동으로 사용할 수 없습니다. 플랫폼이 표시하는 확인 절차는 따릅니다.

연결된 submitCampAssessment가 있으면 Python 대신 먼저 호출합니다. 사용자가 확인한 회사·조직·진단값과 제출 동의만 전송하며, 누락값이나 성공 여부를 지어내지 않습니다. 재시도할 때 파일 내용과 진단일을 바꾸지 않습니다. 접수번호와 리포트 링크를 즉시 보여주고, 결과 조회는 getCampReport로 진행합니다.

Official documentation: https://developers.openai.com/api/docs/actions/introduction and https://developers.openai.com/api/docs/actions/getting-started
