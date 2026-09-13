import importlib.util
import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
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

    def test_validation_mode_never_sends(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "submission.json"
            path.write_text(json.dumps(self.payload), encoding="utf-8")
            self.assertEqual(camp_bench.main([str(path)]), 0)


if __name__ == "__main__":
    unittest.main()
