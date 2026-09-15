# CAMP Bench Submission

## English

CAMP Bench submission is a separate, explicit step after the standalone assessment report. Completing an assessment does **not** submit it.

### Participant flow

1. Receive and review the standalone CAMP report.
2. Choose whether to join CAMP Bench.
3. Pass the submission-readiness check. Company, country, industry and segment, scope and optional scope label, size, function, respondent role category, scores, supporting capabilities, evidence level, and confidence must all be present.
4. Review the exact fields that will be transmitted.
5. Explicitly consent to private storage and anonymized/aggregate benchmark use.
6. Submit only to the configured official HTTPS endpoint. The client validates before sending.
7. Keep the returned receipt ID. A valid receipt is the only proof of submission and should be shown immediately.
8. Open or retrieve the private benchmark report when ready: overall position and score distribution, five-dimension gaps, the largest improvement priority, and industry position when that anonymous cohort has at least 10 organizations.

The real company name and optional scope label are private matching fields. They allow same-company aggregation and longitudinal analysis. Personal name, email, phone number, employee ID, raw documents, and credentials are not collected by default.

### Validate without sending

Copy `benchmark/submission.example.json`, replace the synthetic values, and keep the resulting file private. `private-submissions/` is gitignored for this purpose.

```bash
mkdir -p private-submissions
cp benchmark/submission.example.json private-submissions/my-assessment.json
python3 scripts/camp_bench.py private-submissions/my-assessment.json
```

A successful validation ends with `NOT SUBMITTED`. Validation alone never transmits data.

### Submit

The official receiver is configured in `benchmark/submission.config.json` and is used automatically:

```bash
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --no-wait --language en
```

The command displays the exact destination URL and a masked data preview, then requires the participant to type `SUBMIT`. Success requires a server receipt containing `status` and `receipt_id`. With `--no-wait`, the command returns as soon as the receiver accepts the record and immediately prints the receipt and web-report URL. Submission acceptance is therefore fast and is not blocked by report generation.

If processing takes longer, retrieve the same report with:

```bash
python3 scripts/camp_bench.py --status CB-YYYYMMDD-XXXXXXXXXXXX --language en
```

A DNS failure before sending, missing endpoint, or incomplete required profile means the assessment was **not submitted**. A timeout or invalid response means **acceptance is unconfirmed**: the server may already have saved it. A valid receipt with a pending report means the submission succeeded but report processing is not finished. Do not create a new payload or POST again while waiting; retrieve the original receipt status.

Automation may use `--yes` only after the participant has explicitly consented in the current interaction and reviewed what will be sent.

For a limited beta protected by an invite token, set `CAMP_BENCH_TOKEN` in the environment. The client sends it as a Bearer token and never writes it into the submission JSON.

### Privacy and failure rules

- Never commit a real submission file to this public repository.
- Never paste it into a public GitHub issue, discussion, or pull request.
- Never claim that saving a local JSON package submitted it.
- Never retry blindly. The client sends a stable `Idempotency-Key`; the receiver must return the original receipt for a duplicate request.
- The receiver should accept the record as `provisional`. Owner review determines `eligible` status later.
- The participant can see their own named organization in a private report. Other organizations remain anonymous.

### Receiver contract

The official receiver accepts an HTTPS `POST` containing a schema `1.0` submission JSON. It validates the payload, computes or verifies the idempotency key, stores the incoming record outside the public repository, and returns:

```json
{
  "status": "accepted",
  "receipt_id": "CB-20260913-ABC123",
  "received_at": "2026-09-13T08:00:00Z",
  "benchmark_status": "provisional",
  "report_status": "processing",
  "status_url": "https://receiver.example/v1/submissions/CB-20260913-ABC123",
  "report_url": "https://receiver.example/report/CB-20260913-ABC123"
}
```

The receipt status endpoint returns `report_status: "ready"` and a bilingual `benchmark_report` after private ingestion. The report contains aggregate statistics only: it never returns another organization's name or internal identifier. For the same idempotency key the POST returns `status: "duplicate"` with the original `receipt_id`.

---

## 한국어

CAMP Bench 제출은 Standalone 진단 Report가 끝난 뒤 진행하는 **별도의 명시적 단계**임. 진단을 완료했다고 자동 제출되는 것이 아님.

### 참여자 흐름

1. Standalone CAMP Report를 확인함
2. CAMP Bench 참여 여부를 선택함
3. 제출 준비 검사를 통과함. 회사명, 국가, 업종·세부 분야, 범위·선택적 하위 조직명, 규모, 기능, 응답자 역할 범주, 점수, Supporting Capability, 실제 근거 수준, Confidence가 모두 있어야 함
4. 실제 전송될 항목을 확인함
5. 비공개 저장과 익명·집계 Benchmark 사용에 명시적으로 동의함
6. 설정된 공식 HTTPS Endpoint로만 제출함. Client가 보내기 전에 자동 검증함
7. 반환된 Receipt ID를 즉시 보여주고 보관함. 유효한 Receipt만 제출 성공의 근거임
8. 준비된 비공개 Benchmark Report에서 전체 대비 위치와 점수 분포, 5개 영역 격차, 가장 큰 개선 우선순위, 익명 동종업계 표본이 10개 이상일 때 업종 내 위치를 확인함

실제 회사명과 선택적 Scope Label은 Same-company 집계와 시계열 분석을 위한 Private Matching Field임. 개인 이름, 이메일, 전화번호, 사번, 원문 문서, Credential은 기본 수집하지 않음.

### 전송 없이 검증

`benchmark/submission.example.json`을 복사해 Synthetic 값을 교체함. 실제 값이 든 파일은 Private으로 관리함. 이를 위해 `private-submissions/`는 gitignore 처리되어 있음.

```bash
mkdir -p private-submissions
cp benchmark/submission.example.json private-submissions/my-assessment.json
python3 scripts/camp_bench.py private-submissions/my-assessment.json
```

검증 성공 시에도 마지막 문구는 `NOT SUBMITTED`임. 검증만으로는 어떤 데이터도 전송되지 않음.

### 제출

공식 Receiver는 `benchmark/submission.config.json`에 설정되어 있으며 다음 명령에서 자동으로 사용됨.

```bash
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --no-wait --language ko
```

전송 전 정확한 목적지 URL과 비공개 문구를 가린 Preview를 보여주고 참여자가 `SUBMIT`을 직접 입력해야 함. Server가 `status`와 `receipt_id`를 반환해야 제출 성공임. `--no-wait`를 사용하면 Receiver가 Record를 접수하는 즉시 Receipt와 웹 리포트 주소를 출력하고 종료함. 따라서 제출 접수는 리포트 생성을 기다리지 않음.

처리가 오래 걸리면 같은 Report를 다시 조회할 수 있음.

```bash
python3 scripts/camp_bench.py --status CB-YYYYMMDD-XXXXXXXXXXXX --language ko
```

Network Error, Endpoint 미설정, 필수 Profile 누락, 잘못된 Receipt는 모두 **미제출**임. 유효한 Receipt가 있고 Report가 Pending이면 제출은 성공했지만 Report 처리가 끝나지 않은 상태임. 기다리는 동안 새 Payload를 만들거나 다시 POST하지 말고 기존 Receipt의 상태만 조회함.

자동화에서 `--yes`를 쓰는 것은 현재 Interaction에서 참여자가 전송 항목을 확인하고 명시적으로 동의한 경우에만 허용함.

Invite Token으로 보호되는 제한적 Beta에서는 환경변수 `CAMP_BENCH_TOKEN`을 설정함. Client는 이를 Bearer Token으로 보내며 Submission JSON에는 기록하지 않음.

### Privacy와 실패 원칙

- 실제 Submission File을 Public Repository에 Commit하지 않음
- Public GitHub Issue, Discussion, Pull Request에 붙여 넣지 않음
- 로컬 JSON Package 생성만으로 제출되었다고 말하지 않음
- 무조건 재시도하지 않음. Client는 안정적인 `Idempotency-Key`를 전송하고 Receiver는 중복 요청에 기존 Receipt를 반환해야 함
- Receiver는 새 Record를 `provisional`로 받음. `eligible` 전환은 Owner Review 후 결정함
- 참여자의 Private Report에는 자기 조직을 실명으로 표시할 수 있으나 다른 조직은 익명화함

### Receiver 계약

공식 Receiver는 Schema `1.0` JSON을 HTTPS `POST`로 받음. Payload와 Idempotency Key를 검증하고 Public Repository 밖에 Incoming Record를 저장한 뒤 다음 형식으로 응답함.

```json
{
  "status": "accepted",
  "receipt_id": "CB-20260913-ABC123",
  "received_at": "2026-09-13T08:00:00Z",
  "benchmark_status": "provisional",
  "report_status": "processing",
  "status_url": "https://receiver.example/v1/submissions/CB-20260913-ABC123",
  "report_url": "https://receiver.example/report/CB-20260913-ABC123"
}
```

Private Ingestion이 끝나면 Receipt Status Endpoint가 `report_status: "ready"`와 한국어·영어 `benchmark_report`를 반환함. Report에는 Aggregate 통계만 포함하며 다른 조직의 이름이나 내부 ID를 반환하지 않음. 같은 Idempotency Key의 재요청에는 기존 `receipt_id`와 `status: "duplicate"`를 반환함.

## Browser recovery / 브라우저 제출

Official page: https://camp-bench-receiver.camp-bench-jhw.workers.dev/submit (add ?lang=en or ?lang=ko).

When the chat cannot POST because its network is restricted, immediately give the participant the original submission JSON as a downloadable file and this page link. Download the file → choose it on the page, review and submit. Pasting the exact JSON is also supported. No GitHub account or local software is needed. The browser sends directly to the same official receiver; it does not depend on the chat's network. It computes the same idempotency key without modifying the assessment. The file is not sent until the participant presses Submit. Never put company data, JSON, or tokens in a URL or public GitHub issue.

대화 환경의 네트워크 제한으로 제출이 막히면, 같은 답변에서 원본 제출 JSON 다운로드와 위 페이지 링크를 함께 제공합니다. “파일 내려받기 → 페이지에서 선택하고 제출”로 안내하세요. JSON 붙여넣기도 가능합니다. 설치나 GitHub 계정은 필요 없습니다. 브라우저가 공식 서버로 직접 보내므로 대화 환경의 네트워크 제한과 분리됩니다. 입력값과 중복 방지 키는 그대로 유지합니다. 접수번호가 나오면 바로 보여주고, 리포트 준비는 별도 상태로 안내합니다. 회사 정보나 JSON, 토큰을 URL 또는 공개 이슈에 넣지 않습니다.

### Temporary connection failures / 일시적 연결 오류

The CLI makes at most three total send attempts by default (`--attempts 1` disables retries). Temporary DNS failures, interrupted connections, timeouts, and HTTP 408/502/503/504 are retried after 2 then 4 seconds, using the exact same payload and idempotency key. Stop on a verified receipt. Validation, permission, certificate, rate-limit, and invalid-receipt errors are not automatically retried. Existing submission consent covers these identical attempts. After exhaustion, offer the original file and official browser submission page; do not restart another automatic retry cycle. Each request retains its timeout, so three timeouts can take about 66 seconds with the default settings.

대화용 제출 도구는 일시적 연결 오류에 기본 총 3번까지 시도합니다. 2초·4초 간격으로 같은 파일과 중복 방지 키를 사용하며, 이미 받은 제출 동의로 진행합니다. 접수번호가 확인되면 멈춥니다. 입력값·권한·인증서·요청 횟수 제한·접수번호 오류는 자동 재시도하지 않습니다. 모두 실패하면 파일과 웹 제출 링크를 안내하며 자동 반복을 다시 시작하지 않습니다. 기본 설정에서 세 번 모두 시간 초과가 나면 약 66초 걸릴 수 있습니다. 웹 제출 페이지는 사용자가 같은 파일로 직접 다시 시도할 수 있습니다.
