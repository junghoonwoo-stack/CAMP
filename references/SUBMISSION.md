# CAMP Bench Submission

## English

CAMP Bench submission is a separate, explicit step after the standalone assessment report. Completing an assessment does **not** submit it.

### Participant flow

1. Receive and review the standalone CAMP report.
2. Choose whether to join CAMP Bench.
3. Review the exact fields that will be transmitted.
4. Explicitly consent to private storage and anonymized/aggregate benchmark use.
5. Validate the submission locally.
6. Submit only to the configured official HTTPS endpoint.
7. Keep the returned receipt ID. A valid receipt is the only proof of submission.
8. Receive the private benchmark report: overall position and score distribution, five-dimension gaps, the largest improvement priority, and industry position when that anonymous cohort has at least 10 organizations.

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
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --language en
```

The command displays the exact destination URL and a masked data preview, then requires the participant to type `SUBMIT`. Success requires a server receipt containing `status` and `receipt_id`. It then waits for the anonymous benchmark report and prints the overall percentile/median comparison, score distribution, industry result or sample-size notice, five-dimension comparison, and priority gap.

If processing takes longer, retrieve the same report with:

```bash
python3 scripts/camp_bench.py --status CB-YYYYMMDD-XXXXXXXXXXXX --language en
```

A network error, missing endpoint, or invalid receipt means the assessment was **not submitted**. A valid receipt with a pending report means the submission succeeded but report processing is not finished.

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
  "status_url": "https://receiver.example/v1/submissions/CB-20260913-ABC123"
}
```

The receipt status endpoint returns `report_status: "ready"` and a bilingual `benchmark_report` after private ingestion. The report contains aggregate statistics only: it never returns another organization's name or internal identifier. For the same idempotency key the POST returns `status: "duplicate"` with the original `receipt_id`.

---

## 한국어

CAMP Bench 제출은 Standalone 진단 Report가 끝난 뒤 진행하는 **별도의 명시적 단계**임. 진단을 완료했다고 자동 제출되는 것이 아님.

### 참여자 흐름

1. Standalone CAMP Report를 확인함
2. CAMP Bench 참여 여부를 선택함
3. 실제 전송될 항목을 확인함
4. Private 저장과 익명·Aggregate Benchmark 사용에 명시적으로 동의함
5. 로컬에서 Submission을 검증함
6. 설정된 공식 HTTPS Endpoint로만 제출함
7. 반환된 Receipt ID를 보관함. 유효한 Receipt만 제출 성공의 근거임
8. 전체 대비 위치와 점수 분포, 5개 Dimension 격차, 가장 큰 개선 Priority, 익명 동종업계 표본이 10개 이상일 때 Industry 위치가 포함된 Private Benchmark Report를 받음

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
python3 scripts/camp_bench.py private-submissions/my-assessment.json --submit --language ko
```

전송 전 정확한 목적지 URL과 Private Text를 가린 Preview를 보여주고 참여자가 `SUBMIT`을 직접 입력해야 함. Server가 `status`와 `receipt_id`를 반환해야 제출 성공임. 그다음 익명 Benchmark Report를 기다려 Overall Percentile·중앙값 비교, 전체 점수 분포, Industry 결과 또는 표본 부족 안내, 5개 Dimension 비교, Priority Gap을 출력함.

처리가 오래 걸리면 같은 Report를 다시 조회할 수 있음.

```bash
python3 scripts/camp_bench.py --status CB-YYYYMMDD-XXXXXXXXXXXX --language ko
```

Network Error, Endpoint 미설정, 잘못된 Receipt는 모두 **미제출**임. 유효한 Receipt가 있고 Report가 Pending이면 제출은 성공했지만 Report 처리가 끝나지 않은 상태임.

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
  "status_url": "https://receiver.example/v1/submissions/CB-20260913-ABC123"
}
```

Private Ingestion이 끝나면 Receipt Status Endpoint가 `report_status: "ready"`와 한국어·영어 `benchmark_report`를 반환함. Report에는 Aggregate 통계만 포함하며 다른 조직의 이름이나 내부 ID를 반환하지 않음. 같은 Idempotency Key의 재요청에는 기존 `receipt_id`와 `status: "duplicate"`를 반환함.
