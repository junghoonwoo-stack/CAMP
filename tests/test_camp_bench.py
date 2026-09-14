import importlib.util
import json
import os
import tempfile
import threading
import unittest
from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import StringIO
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "camp_bench.py"
SPEC = importlib.util.spec_from_file_location("camp_bench", MODULE_PATH)
camp_bench = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(camp_bench)


EXAMPLE = Path(__file__).resolve().parents[1] / "benchmark" / "submission.example.json"


class ReceiptHandler(BaseHTTPRequestHandler):
    seen_headers = {}
    seen_payload = {}

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        type(self).seen_headers = dict(self.headers)
        type(self).seen_payload = json.loads(self.rfile.read(length))
        body = json.dumps({"status": "accepted", "receipt_id": "CB-TEST-001", "benchmark_status": "provisional"}).encode()
        self.send_response(202)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        receipt_id = self.path.rsplit("/", 1)[-1]
        body = json.dumps({
            "receipt_id": receipt_id,
            "status": "processed",
            "processing_status": "processed",
            "report_status": "ready",
            "benchmark_report": {
                "benchmark_date": "2026-09-14",
                "benchmark_type": "preliminary",
                "overall": {
                    "available": True,
                    "organization_count": 12,
                    "percentile": 67,
                    "distribution": [
                        {"range": "0-20", "count": 1, "percent": 8.3},
                        {"range": "21-40", "count": 2, "percent": 16.7},
                    ],
                },
                "industry": {"available": False, "organization_count": 6},
                "dimensions": [{
                    "key": "transformation",
                    "label": {"en": "Role Transformation", "ko": "역할 전환"},
                    "score": 5,
                    "overall_median": 10,
                    "gap": -5,
                }],
                "messages": {
                    "en": {
                        "overall": "You are ahead of the overall median.",
                        "industry": "Industry sample is insufficient.",
                        "priority_gap": "Role Transformation is the largest gap.",
                        "sample_note": "Preliminary benchmark.",
                    },
                    "ko": {
                        "overall": "전체 중앙값보다 앞서 있습니다.",
                        "industry": "동종업계 표본이 부족합니다.",
                        "priority_gap": "역할 전환이 가장 부족합니다.",
                        "sample_note": "예비 Benchmark입니다.",
                    },
                },
            },
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        return


class CampBenchTests(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_example_is_valid(self):
        camp_bench.validate(self.payload)

    def test_score_mismatch_fails(self):
        self.payload["total_score"] = 99
        with self.assertRaisesRegex(camp_bench.SubmissionError, "dimension sum"):
            camp_bench.validate(self.payload)

    def test_missing_consent_fails(self):
        self.payload["consent_to_benchmark"] = False
        with self.assertRaisesRegex(camp_bench.SubmissionError, "consent_to_benchmark"):
            camp_bench.validate(self.payload)

    def test_personal_identity_field_fails(self):
        self.payload["email"] = "person@example.com"
        with self.assertRaisesRegex(camp_bench.SubmissionError, "personal respondent fields"):
            camp_bench.validate(self.payload)

    def test_non_https_remote_endpoint_fails(self):
        with self.assertRaisesRegex(camp_bench.SubmissionError, "HTTPS"):
            camp_bench.assert_safe_endpoint("http://example.com/submit")

    def test_endpoint_with_query_fails(self):
        with self.assertRaisesRegex(camp_bench.SubmissionError, "plain HTTPS URL"):
            camp_bench.assert_safe_endpoint("https://example.com/submit?token=secret")

    def test_local_submission_returns_receipt_and_idempotency_key(self):
        server = HTTPServer(("127.0.0.1", 0), ReceiptHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            receipt = camp_bench.submit(self.payload, f"http://127.0.0.1:{server.server_port}/v1/submissions")
        finally:
            server.shutdown()
            thread.join()
            server.server_close()
        self.assertEqual(receipt["receipt_id"], "CB-TEST-001")
        self.assertEqual(ReceiptHandler.seen_payload, self.payload)
        self.assertEqual(ReceiptHandler.seen_headers["Idempotency-Key"], camp_bench.idempotency_key(self.payload))

    def test_optional_beta_token_is_sent_as_bearer(self):
        server = HTTPServer(("127.0.0.1", 0), ReceiptHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        previous = os.environ.get("CAMP_BENCH_TOKEN")
        os.environ["CAMP_BENCH_TOKEN"] = "beta-secret"
        try:
            camp_bench.submit(self.payload, f"http://127.0.0.1:{server.server_port}/v1/submissions")
        finally:
            if previous is None:
                os.environ.pop("CAMP_BENCH_TOKEN", None)
            else:
                os.environ["CAMP_BENCH_TOKEN"] = previous
            server.shutdown()
            thread.join()
            server.server_close()
        self.assertEqual(ReceiptHandler.seen_headers["Authorization"], "Bearer beta-secret")

    def test_fetches_and_prints_bilingual_anonymous_report(self):
        server = HTTPServer(("127.0.0.1", 0), ReceiptHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        receipt_id = "CB-20260914-ABCDEF123456"
        try:
            status = camp_bench.fetch_status(
                f"http://127.0.0.1:{server.server_port}/v1/submissions",
                receipt_id,
            )
        finally:
            server.shutdown()
            thread.join()
            server.server_close()

        output = StringIO()
        with redirect_stdout(output):
            rendered = camp_bench.print_report(status, "My Company", "both")
        text = output.getvalue()
        self.assertTrue(rendered)
        self.assertIn("My Company", text)
        self.assertIn("전체 중앙값보다 앞서 있습니다.", text)
        self.assertIn("You are ahead of the overall median.", text)
        self.assertIn("전체 점수 분포 / Overall score distribution", text)
        self.assertNotIn("Private Company", text)

    def test_waits_until_report_is_ready(self):
        responses = iter([
            {"receipt_id": "CB-20260914-ABCDEF123456", "status": "queued", "report_status": "processing"},
            {"receipt_id": "CB-20260914-ABCDEF123456", "status": "processed", "report_status": "ready", "benchmark_report": {}},
        ])
        sleeps = []

        status = camp_bench.wait_for_report(
            "https://example.com/v1/submissions",
            "CB-20260914-ABCDEF123456",
            fetcher=lambda *_: next(responses),
            sleeper=sleeps.append,
            clock=lambda: 0,
        )
        self.assertEqual(status["report_status"], "ready")
        self.assertEqual(sleeps, [15.0])

    def test_auto_language_supports_korean(self):
        previous = os.environ.get("LANG")
        os.environ["LANG"] = "ko_KR.UTF-8"
        try:
            self.assertEqual(camp_bench.selected_language("auto"), "ko")
            self.assertEqual(camp_bench.selected_language("both"), "both")
        finally:
            if previous is None:
                os.environ.pop("LANG", None)
            else:
                os.environ["LANG"] = previous

    def test_validation_mode_never_sends(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "submission.json"
            path.write_text(json.dumps(self.payload), encoding="utf-8")
            self.assertEqual(camp_bench.main([str(path)]), 0)


if __name__ == "__main__":
    unittest.main()
