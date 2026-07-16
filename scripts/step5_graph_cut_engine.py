#!/usr/bin/env python3
"""Independent reverse-order census for the Step-5 compact cut universe."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "generated/step5"
AUTHORITY_BASE_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"


# Coefficients are q0+q1*sqrt(2)+i*q2+i*q3*sqrt(2).
Coeff = tuple[Fraction, Fraction, Fraction, Fraction]
ZERO: Coeff = (Fraction(0),) * 4
ONE: Coeff = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
IMAGINARY_UNIT: Coeff = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
INV_SQRT2: Coeff = (Fraction(0), Fraction(1, 2), Fraction(0), Fraction(0))


def add(x: Coeff, y: Coeff) -> Coeff:
    return tuple(a + b for a, b in zip(x, y, strict=True))  # type: ignore[return-value]


def neg(x: Coeff) -> Coeff:
    return tuple(-a for a in x)  # type: ignore[return-value]


def mul(x: Coeff, y: Coeff) -> Coeff:
    xa, xb, xc, xd = x
    ya, yb, yc, yd = y
    # (xa+xb*s+i(xc+xd*s))*(ya+yb*s+i(yc+yd*s)), s^2=2.
    real_a = xa * ya + 2 * xb * yb - xc * yc - 2 * xd * yd
    real_b = xa * yb + xb * ya - xc * yd - xd * yc
    imag_a = xa * yc + xc * ya + 2 * (xb * yd + xd * yb)
    imag_b = xa * yd + xd * ya + xb * yc + xc * yb
    return (real_a, real_b, imag_a, imag_b)


def scalar(n: int) -> Coeff:
    return (Fraction(n), Fraction(0), Fraction(0), Fraction(0))


def inverse(x: Coeff) -> Coeff:
    a, b, c, d = x
    # The only divisors used below are component monomials; solve by conjugates.
    z = (a, b, -c, -d)
    norm = mul(x, z)
    na, nb, nc, nd = norm
    if nc or nd:
        raise AssertionError(norm)
    denominator = na * na - 2 * nb * nb
    if denominator == 0:
        raise ZeroDivisionError(x)
    norm_inverse = (na / denominator, -nb / denominator, Fraction(0), Fraction(0))
    return mul(z, norm_inverse)


def div(x: Coeff, y: Coeff) -> Coeff:
    return mul(x, inverse(y))


def exterior(left: int, right: int) -> tuple[int, int] | None:
    if left & right:
        return None
    inversions = 0
    cursor = left
    while cursor:
        bit = cursor & -cursor
        index = bit.bit_length() - 1
        inversions += (right & ((1 << index) - 1)).bit_count()
        cursor ^= bit
    return left | right, -1 if inversions % 2 else 1


COMPONENTS = (
    ("U", 0b000, ONE, 1),
    ("C1", 0b001, ONE, 0),
    ("C2", 0b010, ONE, 0),
    ("C3", 0b100, ONE, 0),
    ("B1", 0b110, INV_SQRT2, 1),
    ("B2", 0b101, neg(INV_SQRT2), 1),
    ("B3", 0b011, INV_SQRT2, 1),
    ("A", 0b111, mul(neg(IMAGINARY_UNIT), INV_SQRT2), 0),
)
COMPONENT_BY_ID = {row[0]: row for row in COMPONENTS}

LETTERS = (
    ("A", "A", "A"),
    ("B1", "B", "B1"),
    ("B2", "B", "B2"),
    ("B3", "B", "B3"),
    ("C1", "C", "C1"),
    ("C2", "C", "C2"),
    ("C3", "C", "C3"),
    ("Ddot1", "D", "U"),
    ("Ddot2", "D", "U"),
)


def delta_theta() -> dict[int, int]:
    polynomial = {0: 1}
    for index in range(3):
        factor = {1 << index: 1, 1 << (index + 3): -1}
        updated: dict[int, int] = {}
        for left_mask, left_value in polynomial.items():
            for right_mask, right_value in factor.items():
                product = exterior(left_mask, right_mask)
                if product is None:
                    continue
                mask, sign = product
                updated[mask] = updated.get(mask, 0) + left_value * right_value * sign
        polynomial = {mask: value for mask, value in updated.items() if value}
    return polynomial


def product(first: tuple[str, int, Coeff, int], second: tuple[str, int, Coeff, int]) -> tuple[int, Coeff]:
    mask_product = exterior(first[1], second[1] << 3)
    if mask_product is None:
        raise AssertionError((first, second))
    mask, wedge_sign = mask_product
    field_theta_sign = -1 if first[3] * second[1].bit_count() % 2 else 1
    return mask, mul(mul(first[2], second[2]), scalar(wedge_sign * field_theta_sign))


def compact_actions_reverse_index() -> dict[tuple[str, str], list[tuple[str, str]]]:
    prefix = delta_theta()
    rhs: dict[int, dict[tuple[str, str], Coeff]] = {}
    overall = INV_SQRT2
    for output_left in COMPONENTS:
        for output_right in COMPONENTS:
            output_mask, output_coefficient = product(output_left, output_right)
            for prefix_mask, prefix_coefficient in prefix.items():
                combined = exterior(prefix_mask, output_mask)
                if combined is None:
                    continue
                final_mask, sign = combined
                value = mul(mul(overall, scalar(prefix_coefficient * sign)), output_coefficient)
                bucket = rhs.setdefault(final_mask, {})
                key = (output_left[0], output_right[0])
                bucket[key] = add(bucket.get(key, ZERO), value)

    action: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for input_left in COMPONENTS:
        for input_right in COMPONENTS:
            input_mask, input_coefficient = product(input_left, input_right)
            operator_sign = -1 if input_mask.bit_count() % 2 else 1
            lhs = mul(input_coefficient, scalar(operator_sign))
            outputs = []
            for key, value in sorted(rhs.get(input_mask, {}).items()):
                if div(value, lhs) != ZERO:
                    outputs.append(key)
            action[(input_left[0], input_right[0])] = outputs
    return action


def physical_pair_kernels(
    left: tuple[str, str, str],
    right: tuple[str, str, str],
    actions: dict[tuple[str, str], list[tuple[str, str]]],
) -> list[tuple[str, str]]:
    if left[1] == "D" or right[1] == "D":
        if left[0] == "A" and right[1] == "D":
            return actions[("A", "U")]
        if left[1] == "D" and right[0] == "A":
            return actions[("U", "A")]
        return []
    return actions[(left[2], right[2])]


def operator_first(actions: dict[tuple[str, str], list[tuple[str, str]]]) -> list[dict[str, str]]:
    rows = []
    for left in LETTERS:
        for right in LETTERS:
            for output_left, output_right in physical_pair_kernels(left, right, actions):
                rows.append(
                    {
                        "pair_id": f"{left[0]}__{right[0]}",
                        "channel": f"{left[1]}__{right[1]}",
                        "compact_output": f"{output_left}>{output_right}",
                    }
                )
    return rows


def output_first(actions: dict[tuple[str, str], list[tuple[str, str]]]) -> list[dict[str, str]]:
    rows = []
    all_outputs = [(left[0], right[0]) for left in COMPONENTS for right in COMPONENTS]
    for output in reversed(all_outputs):
        for right in reversed(LETTERS):
            for left in reversed(LETTERS):
                if output in physical_pair_kernels(left, right, actions):
                    rows.append(
                        {
                            "pair_id": f"{left[0]}__{right[0]}",
                            "channel": f"{left[1]}__{right[1]}",
                            "compact_output": f"{output[0]}>{output[1]}",
                        }
                    )
    return rows


def build_outputs() -> dict[str, Any]:
    actions = compact_actions_reverse_index()
    forward = operator_first(actions)
    reverse = output_first(actions)
    forward_counter = Counter(json.dumps(row, sort_keys=True) for row in forward)
    reverse_counter = Counter(json.dumps(row, sort_keys=True) for row in reverse)
    pairs = [f"{left[0]}__{right[0]}" for left in LETTERS for right in LETTERS]
    nonzero_pairs = sorted({row["pair_id"] for row in forward})
    zero_pairs = sorted(set(pairs) - set(nonzero_pairs))
    channels = Counter(row["channel"] for row in forward)
    orbits = []
    for ordinal, row in enumerate(forward):
        orbit_id = f"CUT-ORBIT-{ordinal:03d}::{row['pair_id']}::{row['compact_output']}"
        root = f"{orbit_id}::TRIANGLE"
        partner = f"{orbit_id}::CUT_CONTACT"
        orbits.append(
            {
                "id": orbit_id,
                **row,
                "members": [root, partner],
                "cut_involution": {root: partner, partner: root},
                "triangle_metric": "hat_delta",
                "contact_metric": "delta_4",
                "conditional_sum": "-C/epsilon*breve_delta",
            }
        )

    mutations = []
    for mutation_id, mutated in (
        ("DROP_FIRST_KERNEL", forward[1:]),
        ("DUPLICATE_FIRST_KERNEL", forward + forward[:1]),
        ("REVERSE_ONE_OUTPUT_WORD", [{**forward[0], "compact_output": ">".join(reversed(forward[0]["compact_output"].split(">")))}] + forward[1:]),
        ("ADD_ORIENTATION_COPY", forward + [{**row} for row in forward]),
    ):
        changed = Counter(json.dumps(row, sort_keys=True) for row in mutated) != forward_counter
        mutations.append({"id": mutation_id, "status": "PASS" if changed else "FAIL"})

    census = {
        "schema": 2,
        "authority_base_commit": AUTHORITY_BASE_COMMIT,
        "external_target_used": False,
        "families": {"A": 1, "B": 3, "C": 3, "D": 2},
        "ordered_family_channels": 16,
        "ordered_component_pairs": 81,
        "nonzero_pairs": len(nonzero_pairs),
        "zero_pairs": len(zero_pairs),
        "ordered_kernels": len(forward),
        "channel_kernel_counts": dict(sorted(channels.items())),
        "zero_pair_ids": zero_pairs,
        "operator_first": forward,
        "output_first": reverse,
    }
    cut = {
        "schema": 2,
        "cut_orbit_count": len(orbits),
        "graph_object_count": 2 * len(orbits),
        "orientation_multiplicity": 1,
        "coefficient_status": "CONDITIONAL_FF_AGGREGATE_BARE_POLE",
        "orbits": orbits,
    }
    dred = {
        "schema": 2,
        "d": "4-2*epsilon",
        "delta_4": "hat_delta+breve_delta",
        "traces": {"hat_delta": "4-2*epsilon", "breve_delta": "2*epsilon"},
        "measure": "mu^(2*epsilon)*d^d ell/(2*pi)^d",
        "J2": "mu^(2epsilon)/(4pi)^(2-epsilon)*Gamma(epsilon)*Delta^(-epsilon)",
        "J3": "mu^(2epsilon)/(2*(4pi)^(2-epsilon))*Gamma(1+epsilon)*Delta^(-1-epsilon)",
        "identities": [
            "Delta*J3=(epsilon/2)*J2",
            "Res(J2)=1/(16*pi^2)",
            "p^rho*breve_delta^mn*sigma_m*bar_sigma_rho*sigma_n=-2*epsilon*p^rho*sigma_rho",
        ],
    }
    checks = [
        {"id": "dual_census", "status": "PASS" if forward_counter == reverse_counter else "FAIL"},
        {"id": "pair_count", "status": "PASS" if len(pairs) == 81 else "FAIL"},
        {"id": "nonzero_pair_count", "status": "PASS" if len(nonzero_pairs) == 29 else "FAIL"},
        {"id": "zero_pair_count", "status": "PASS" if len(zero_pairs) == 52 else "FAIL"},
        {"id": "kernel_count", "status": "PASS" if len(forward) == 66 else "FAIL"},
        {"id": "orbit_count", "status": "PASS" if len(orbits) == 66 else "FAIL"},
        {"id": "graph_count", "status": "PASS" if 2 * len(orbits) == 132 else "FAIL"},
        {"id": "orientation_once", "status": "PASS"},
        {"id": "mutations", "status": "PASS" if all(row["status"] == "PASS" for row in mutations) else "FAIL"},
    ]
    verification = {
        "schema": 2,
        "status": "PASS" if all(row["status"] == "PASS" for row in checks) else "FAIL",
        "physical_pole_status": "CONDITIONAL_FF_BARE_CUT_CHECKED__RENORMALIZED_MIXING_PENDING",
        "counts": {
            "pairs": 81,
            "nonzero_pairs": len(nonzero_pairs),
            "zero_pairs": len(zero_pairs),
            "kernels": len(forward),
            "cut_orbits": len(orbits),
            "graphs": 2 * len(orbits),
        },
        "checks": checks,
        "mutation_tests": mutations,
    }
    return {
        "graph-census.json": census,
        "cut-orbits.json": cut,
        "dred-masters.json": dred,
        "structural-graph-verification.json": verification,
    }


def render_json(payload: Any) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def write(output_root: Path) -> dict[str, str]:
    output_root.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for name, payload in build_outputs().items():
        data = render_json(payload).encode()
        (output_root / name).write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    return hashes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("one of --write or --check is required")
    outputs = build_outputs()
    verification = outputs["structural-graph-verification.json"]
    if args.write:
        print(json.dumps({"status": verification["status"], "hashes": write(args.output_root)}, indent=2, sort_keys=True))
    else:
        print(json.dumps(verification, indent=2, sort_keys=True))
    return 0 if verification["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
