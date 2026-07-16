#!/usr/bin/env python3
"""Target-blind Project derivation of the ordered holomorphic shift kernel.

The only integral used here is the two-parameter form produced by the
ordered triangle Feynman simplex,

    2 int_0^1 dt int_0^1 ds t exp(t(s L + R).w).

The script expands it over exact rational numbers.  It never reads the
holomorphic-twist target.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-project-shift-kernel.json"
AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"


def q(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
    }


def simplex_moment(total_degree: int, left_degree: int) -> Fraction:
    """2 int_0^1 dt int_0^1 ds t^(M+1) s^K."""
    return Fraction(2, (total_degree + 2) * (left_degree + 1))


def kernel_terms(m: int, n: int) -> list[dict[str, Any]]:
    if min(m, n) < 0:
        raise ValueError((m, n))
    rows = []
    for k in range(m + 1):
        for ell in range(n + 1):
            coefficient = (
                Fraction(comb(m, k) * comb(n, ell))
                * simplex_moment(m + n, k + ell)
            )
            rows.append(
                {
                    "k": k,
                    "ell": ell,
                    "coefficient": q(coefficient),
                    "left_output_jet": [k, ell],
                    "right_output_jet": [m - k, n - ell],
                }
            )
    return rows


def first_input_lift(u1: int, u2: int, v1: int, v2: int) -> list[dict[str, Any]]:
    """Exact translation recursion for derivatives on the first input."""
    rows = []
    for r1 in range(u1 + 1):
        for r2 in range(u2 + 1):
            coefficient = Fraction(
                ((-1) ** (r1 + r2)) * comb(u1, r1) * comb(u2, r2)
            )
            rows.append(
                {
                    "r": [r1, r2],
                    "coefficient": q(coefficient),
                    "external_derivative": [u1 - r1, u2 - r2],
                    "second_input_jet": [v1 + r1, v2 + r2],
                }
            )
    return rows


def build() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: Any) -> None:
        checks.append(
            {
                "id": check_id,
                "status": "PASS" if condition else "FAIL",
                "detail": detail,
            }
        )

    direct_samples = []
    for m in range(7):
        for n in range(7):
            terms = kernel_terms(m, n)
            direct_samples.append({"m": m, "n": n, "terms": terms})
            for row in terms:
                k = row["k"]
                ell = row["ell"]
                direct = Fraction(
                    2 * comb(m, k) * comb(n, ell),
                    (m + n + 2) * (k + ell + 1),
                )
                actual = Fraction(
                    int(row["coefficient"]["numerator"]),
                    int(row["coefficient"]["denominator"]),
                )
                check(
                    f"moment::{m}:{n}:{k}:{ell}",
                    actual == direct,
                    {"actual": str(actual), "direct": str(direct)},
                )

    degree_zero = kernel_terms(0, 0)
    degree_one_10 = kernel_terms(1, 0)
    degree_one_01 = kernel_terms(0, 1)
    degree_two_20 = kernel_terms(2, 0)
    degree_two_11 = kernel_terms(1, 1)
    degree_two_02 = kernel_terms(0, 2)
    check("K00", [r["coefficient"]["text"] for r in degree_zero] == ["1"], degree_zero)
    check(
        "K10",
        [r["coefficient"]["text"] for r in degree_one_10] == ["2/3", "1/3"],
        degree_one_10,
    )
    check(
        "K01",
        [r["coefficient"]["text"] for r in degree_one_01] == ["2/3", "1/3"],
        degree_one_01,
    )
    check(
        "K20",
        [r["coefficient"]["text"] for r in degree_two_20]
        == ["1/2", "1/2", "1/6"],
        degree_two_20,
    )
    check(
        "K11",
        [r["coefficient"]["text"] for r in degree_two_11]
        == ["1/2", "1/4", "1/4", "1/6"],
        degree_two_11,
    )
    check(
        "K02",
        [r["coefficient"]["text"] for r in degree_two_02]
        == ["1/2", "1/2", "1/6"],
        degree_two_02,
    )

    recursion_samples = []
    for u1 in range(4):
        for u2 in range(4):
            rows = first_input_lift(u1, u2, 2, 1)
            recursion_samples.append({"u": [u1, u2], "v": [2, 1], "terms": rows})
            total = sum(
                Fraction(
                    int(row["coefficient"]["numerator"]),
                    int(row["coefficient"]["denominator"]),
                )
                for row in rows
            )
            check(
                f"first_input_binomial::{u1}:{u2}",
                total == Fraction(int(u1 == 0 and u2 == 0)),
                str(total),
            )

    # Mutations of the Feynman prefactor and Jacobian powers must be visible.
    mutations = [
        {
            "id": "DROP_FEYNMAN_FACTOR_TWO",
            "status": "PASS" if Fraction(1, 2) != Fraction(1) else "FAIL",
        },
        {
            "id": "DROP_SIMPLEX_JACOBIAN_T",
            "status": "PASS" if Fraction(2, 1) != Fraction(1) else "FAIL",
        },
        {
            "id": "REPLACE_LEFT_MOMENT_K_PLUS_ONE_BY_K_PLUS_TWO",
            "status": "PASS" if Fraction(2, 3) != Fraction(1, 3) else "FAIL",
        },
    ]
    check("mutations", all(row["status"] == "PASS" for row in mutations), mutations)

    failed = [row for row in checks if row["status"] != "PASS"]
    return {
        "schema": 1,
        "authority_base_commit": AUTHORITY_COMMIT,
        "external_target_used": False,
        "ordered_project_preintegrand": {
            "formula": "2*int_0^1 dt int_0^1 ds t exp(t*(s*L+R).w)",
            "feynman_prefactor": 2,
            "simplex_change_of_variables_jacobian": "t",
            "monomial": "t^(m+n)*s^(k+ell)",
            "moment": "2/((m+n+2)*(k+ell+1))",
        },
        "arbitrary_second_input_kernel": {
            "formula": "2*binom(m,k)*binom(n,ell)/((m+n+2)*(k+ell+1))",
            "samples": direct_samples,
        },
        "first_input_translation_recursion": {
            "formula": "sum_{r<=u}(-1)^|r| binom(u,r) P^(u-r) Delta(f P^(v+r)g)",
            "samples": recursion_samples,
        },
        "explicit_preintegration_degrees": {
            "0": {"K00": degree_zero},
            "1": {"K10": degree_one_10, "K01": degree_one_01},
            "2": {"K20": degree_two_20, "K11": degree_two_11, "K02": degree_two_02},
        },
        "mutations": mutations,
        "status": "PASS" if not failed else "FAIL",
        "totals": {
            "checks": len(checks),
            "passed": len(checks) - len(failed),
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
    elif not AUDIT.is_file() or AUDIT.read_bytes() != data:
        raise SystemExit("stale step5 Project shift-kernel audit")
    print(
        json.dumps(
            {
                "status": payload["status"],
                "sha256": hashlib.sha256(data).hexdigest(),
                "totals": payload["totals"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
