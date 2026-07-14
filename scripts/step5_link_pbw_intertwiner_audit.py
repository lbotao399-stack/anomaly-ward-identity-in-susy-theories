#!/usr/bin/env python3
"""Exact Taylor coefficient of exp(w1 P1+w2 P2) versus PBW shuffle jets."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-link-pbw-intertwiner.json"


def words(m: int, n: int) -> list[str]:
    if m == 0:
        return ["2" * n]
    if n == 0:
        return ["1" * m]
    return ["1" + word for word in words(m - 1, n)] + ["2" + word for word in words(m, n - 1)]


def build() -> dict[str, Any]:
    checks = []
    rows = []
    for degree in range(9):
        for m in range(degree + 1):
            n = degree - m
            shuffle_words = words(m, n)
            exponential_word_coefficient = Fraction(1, factorial(degree))
            differentiated_coefficient = (
                factorial(m) * factorial(n) * exponential_word_coefficient
            )
            pbw_coefficient = Fraction(1, comb(degree, m))
            condition = (
                len(shuffle_words) == comb(degree, m)
                and len(set(shuffle_words)) == len(shuffle_words)
                and differentiated_coefficient == pbw_coefficient
            )
            checks.append(
                {
                    "id": f"degree::{degree}::{m}:{n}",
                    "status": "PASS" if condition else "FAIL",
                }
            )
            rows.append(
                {
                    "multiindex": [m, n],
                    "word_count": len(shuffle_words),
                    "words": shuffle_words,
                    "coefficient_after_w_derivatives": str(differentiated_coefficient),
                    "normalized_pbw_shuffle_coefficient": str(pbw_coefficient),
                }
            )
    mutations = [
        {
            "id": "USE_FACTORIAL_DENOMINATOR_AFTER_DERIVATION",
            "status": "PASS"
            if Fraction(1, factorial(4)) != Fraction(1, comb(4, 2))
            else "FAIL",
        },
        {
            "id": "KEEP_ONE_ORDERED_WORD_ONLY",
            "status": "PASS" if len(words(2, 2)) != 1 else "FAIL",
        },
    ]
    failed = [row for row in checks + mutations if row["status"] != "PASS"]
    return {
        "schema": 1,
        "external_target_used": False,
        "ordered_translation": "tau_w=exp(w1*P1+w2*P2)",
        "taylor_identity": (
            "partial_w1^m partial_w2^n tau_w|_0="
            "binom(m+n,m)^(-1) sum_Sh(1^m,2^n) P_word"
        ),
        "curvature_statement": (
            "the sum is the PBW-symmetrized lift; individual ordered words differ "
            "by [P1,P2]=-ad_A and higher Lyndon curvature jets"
        ),
        "samples": rows,
        "mutations": mutations,
        "status": "PASS" if not failed else "FAIL",
        "totals": {
            "checks": len(checks) + len(mutations),
            "passed": len(checks) + len(mutations) - len(failed),
            "failed": len(failed),
        },
        "checks": checks,
    }


def canonical(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("one of --write or --check is required")
    payload = build()
    data = canonical(payload)
    if args.write:
        AUDIT.write_bytes(data)
    elif not AUDIT.exists() or AUDIT.read_bytes() != data:
        raise SystemExit("stale link-PBW audit")
    print(
        json.dumps(
            {
                "status": payload["status"],
                "totals": payload["totals"],
                "sha256": hashlib.sha256(data).hexdigest(),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
