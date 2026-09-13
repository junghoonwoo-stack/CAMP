#!/usr/bin/env python3
"""Validate and submit a CAMP Bench assessment using only Python's stdlib.

The command never sends data unless --submit is supplied and the user confirms.
An official endpoint can be set in benchmark/submission.config.json or with the
CAMP_BENCH_ENDPOINT environment variable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT / "benchmark" / "submission.config.json"
CLIENT_VERSION = "1.0.0"
DIMENSIONS = ("access", "delegation", "connection", "compounding", "transformation")
STEP_SCORES = {0, 5, 10, 15, 20}
REQUIRED = {
    "schema_version",
    "assessment_date",
    "company_name",
    "country",
    "industry",
    "industry_segment",
    "scope",
    "headcount_band",
    "function",
    "respondent_role",
    "assessment_method",
    "stage",
    "total_score",
    "dimensions",
    "operations",
    "sovereignty",
    "evidence_level",
    "confidence",
    "consent_to_benchmark",
}
ALLOWED = REQUIRED | {"scope_label", "evidence_summary"}
ENUMS = {
    "assessment_method": {"self_report", "interview", "evidence_assessment", "expert_evidence"},
    "evidence_level": {"Anecdotal", "Repeated", "Operationalized", "Institutionalized"},
    "confidence": {"Low", "Medium", "High"},
    "operations": {"Weak", "Developing", "Strong"},
    "sovereignty": {"API", "Portfolio", "Private", "Post-trained", "Foundation", "Unknown"},
}
FORBIDDEN_PERSONAL_KEYS = {
    "email",
    "phone",
    "personal_name",
    "respondent_name",
    "employee_id",
    "ip_address",
}


class SubmissionError(ValueError):
    """A submission is invalid or cannot be sent safely."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SubmissionError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SubmissionError(f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise SubmissionError("Submission must be a JSON object.")
    return value


def validate(payload: dict[str, Any]) -> None:
    errors: list[str] = []
    missing = sorted(REQUIRED - payload.keys())
    extra = sorted(payload.keys() - ALLOWED)
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))
    if extra:
        errors.append("unknown fields: " + ", ".join(extra))

    if payload.get("schema_version") != "1.0":
        errors.append("schema_version must be '1.0'")
    try:
        date.fromisoformat(str(payload.get("assessment_date", "")))
    except ValueError:
        errors.append("assessment_date must be YYYY-MM-DD")

    for key in ("company_name", "country", "industry", "industry_segment", "scope", "headcount_band", "function", "respondent_role", "stage"):
        if not isinstance(payload.get(key), str) or not payload.get(key, "").strip():
            errors.append(f"{key} must be a non-empty string")

    for key, allowed in ENUMS.items():
        if payload.get(key) not in allowed:
            errors.append(f"{key} must be one of: {', '.join(sorted(allowed))}")

    dimensions = payload.get("dimensions")
    if not isinstance(dimensions, dict):
        errors.append("dimensions must be an object")
    else:
        if set(dimensions) != set(DIMENSIONS):
            errors.append("dimensions must contain exactly: " + ", ".join(DIMENSIONS))
        for key in DIMENSIONS:
            value = dimensions.get(key)
            if type(value) is not int or value not in STEP_SCORES:
                errors.append(f"dimensions.{key} must be one of 0, 5, 10, 15, 20")

        if all(type(dimensions.get(k)) is int for k in DIMENSIONS):
            expected = sum(dimensions[k] for k in DIMENSIONS)
            if payload.get("total_score") != expected:
                errors.append(f"total_score must equal the dimension sum ({expected})")

    if type(payload.get("total_score")) is not int or not 0 <= payload.get("total_score", -1) <= 100:
        errors.append("total_score must be an integer from 0 to 100")
    if payload.get("consent_to_benchmark") is not True:
        errors.append("consent_to_benchmark must be true")
    if isinstance(payload.get("evidence_summary"), str) and len(payload["evidence_summary"]) > 1000:
        errors.append("evidence_summary must be 1,000 characters or fewer")

    lowered_keys = {str(key).lower() for key in payload}
    found_personal = sorted(lowered_keys & FORBIDDEN_PERSONAL_KEYS)
    if found_personal:
        errors.append("personal respondent fields are not accepted: " + ", ".join(found_personal))

    if errors:
        raise SubmissionError("Validation failed:\n- " + "\n- ".join(errors))


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def idempotency_key(payload: dict[str, Any]) -> str:
    return "camp-" + hashlib.sha256(canonical_bytes(payload)).hexdigest()


def configured_endpoint(cli_endpoint: str | None = None) -> str | None:
    if cli_endpoint:
        return cli_endpoint.strip()
    if os.environ.get("CAMP_BENCH_ENDPOINT"):
        return os.environ["CAMP_BENCH_ENDPOINT"].strip()
    if CONFIG_FILE.exists():
        config = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        endpoint = config.get("endpoint")
        if isinstance(endpoint, str) and endpoint.strip():
            return endpoint.strip()
    return None


def assert_safe_endpoint(endpoint: str) -> None:
    parsed = urlparse(endpoint)
    is_local = parsed.hostname in {"localhost", "127.0.0.1", "::1"}
    if parsed.scheme != "https" and not (parsed.scheme == "http" and is_local):
        raise SubmissionError("The submission endpoint must use HTTPS (HTTP is allowed only for localhost testing).")
    if not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise SubmissionError("The submission endpoint must be a plain HTTPS URL without credentials, query parameters, or fragments.")


def redacted_preview(payload: dict[str, Any]) -> str:
    preview = dict(payload)
    company = str(payload.get("company_name", ""))
    preview["company_name"] = company if len(company) <= 2 else company[:2] + "…"
    if preview.get("scope_label"):
        preview["scope_label"] = "[private scope label included]"
    if preview.get("evidence_summary"):
        preview["evidence_summary"] = "[private evidence summary included]"
    return json.dumps(preview, ensure_ascii=False, indent=2)


def submit(payload: dict[str, Any], endpoint: str, timeout: float = 20.0) -> dict[str, Any]:
    assert_safe_endpoint(endpoint)
    request = Request(
        endpoint,
        data=canonical_bytes(payload),
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": f"camp-bench-cli/{CLIENT_VERSION}",
            "Idempotency-Key": idempotency_key(payload),
            "X-CAMP-Schema-Version": str(payload["schema_version"]),
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
            result = json.loads(body)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise SubmissionError(f"Server rejected the submission (HTTP {exc.code}): {detail}") from exc
    except URLError as exc:
        raise SubmissionError(f"Could not reach CAMP Bench: {exc.reason}") from exc
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SubmissionError("CAMP Bench returned an invalid receipt.") from exc

    if not isinstance(result, dict) or result.get("status") not in {"accepted", "duplicate"} or not result.get("receipt_id"):
        raise SubmissionError("CAMP Bench did not return a valid accepted/duplicate receipt.")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate or submit a private CAMP Bench assessment.")
    parser.add_argument("submission", type=Path, help="path to CAMP Bench submission JSON")
    parser.add_argument("--submit", action="store_true", help="send to the configured private endpoint")
    parser.add_argument("--endpoint", help="override the endpoint (normally use CAMP_BENCH_ENDPOINT)")
    parser.add_argument("--yes", action="store_true", help="skip terminal confirmation after explicit consent was already obtained")
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args(argv)

    try:
        payload = load_json(args.submission)
        validate(payload)
        print("VALID: CAMP Bench submission schema and score checks passed.")
        print(f"Idempotency key: {idempotency_key(payload)}")
        if not args.submit:
            print("NOT SUBMITTED: validation only. Add --submit to transmit after consent.")
            return 0

        endpoint = configured_endpoint(args.endpoint)
        if not endpoint:
            raise SubmissionError(
                "No official CAMP Bench endpoint is configured. Nothing was sent. "
                "Keep this file private; do not upload it to a public GitHub issue or commit."
            )
        assert_safe_endpoint(endpoint)

        print(f"\nDestination: {endpoint}")
        print("\nData preview (private text is masked in this terminal view):")
        print(redacted_preview(payload))
        if not args.yes:
            answer = input("\nType SUBMIT to send this assessment to the private CAMP Bench store: ").strip()
            if answer != "SUBMIT":
                print("CANCELLED: nothing was sent.")
                return 2

        receipt = submit(payload, endpoint, timeout=args.timeout)
        print("SUBMITTED: CAMP Bench accepted the assessment.")
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        return 0
    except SubmissionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
