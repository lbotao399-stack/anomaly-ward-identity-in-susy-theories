#!/usr/bin/env python3
"""Exact background-prepotential variation and formal chiral-frame recursion.

For

    E_B = exp(V_B),
    E_B' = h_tilde E_B h^{-1},

this module solves

    ((exp(ad_V) - 1) / ad_V) delta V
        = eta_L - exp(ad_V) eta_R

as a formal power series over Q.  No graph coefficient or anomaly coefficient
enters this file.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
from itertools import combinations
import json
from math import factorial
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/background-ward-recursion.json"
AUDIT = ROOT / "audits/step5-background-ward-recursion-verification.json"
DEFAULT_ORDER = 10


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def add_series(left: Sequence[Fraction], right: Sequence[Fraction]) -> tuple[Fraction, ...]:
    order = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else Fraction())
        + (right[index] if index < len(right) else Fraction())
        for index in range(order)
    )


def scale_series(series: Sequence[Fraction], scalar: Fraction) -> tuple[Fraction, ...]:
    return tuple(Fraction(scalar) * coefficient for coefficient in series)


def multiply_series(
    left: Sequence[Fraction],
    right: Sequence[Fraction],
    order: int,
) -> tuple[Fraction, ...]:
    return tuple(
        sum(
            (
                left[index] * right[degree - index]
                for index in range(degree + 1)
                if index < len(left) and degree - index < len(right)
            ),
            Fraction(),
        )
        for degree in range(order + 1)
    )


def inverse_series(series: Sequence[Fraction], order: int) -> tuple[Fraction, ...]:
    if not series or series[0] == 0:
        raise ValueError("formal-series inversion requires a nonzero constant term")
    inverse = [Fraction(1, 1) / series[0]]
    for degree in range(1, order + 1):
        convolution = sum(
            (series[index] * inverse[degree - index] for index in range(1, degree + 1)),
            Fraction(),
        )
        inverse.append(-convolution / series[0])
    return tuple(inverse)


def exponential_series(order: int) -> tuple[Fraction, ...]:
    if order < 0:
        raise ValueError("series order must be nonnegative")
    return tuple(Fraction(1, factorial(degree)) for degree in range(order + 1))


def dexp_series(order: int) -> tuple[Fraction, ...]:
    if order < 0:
        raise ValueError("series order must be nonnegative")
    return tuple(Fraction(1, factorial(degree + 1)) for degree in range(order + 1))


def variation_coefficients(order: int) -> dict[str, tuple[Fraction, ...]]:
    """Return coefficients of ad_V^n eta_L and ad_V^n eta_R."""

    dexp = dexp_series(order)
    inverse_dexp = inverse_series(dexp, order)
    exp = exponential_series(order)
    left = inverse_dexp
    right = scale_series(multiply_series(inverse_dexp, exp, order), Fraction(-1))
    return {
        "eta_left": left,
        "eta_right": right,
    }


def exact_checks(order: int) -> dict[str, bool]:
    coefficients = variation_coefficients(order)
    dexp = dexp_series(order)
    exp = exponential_series(order)
    identity = (Fraction(1),) + (Fraction(),) * order
    reconstructed_left = multiply_series(dexp, coefficients["eta_left"], order)
    reconstructed_right = multiply_series(dexp, coefficients["eta_right"], order)
    vector_subgroup = add_series(coefficients["eta_left"], coefficients["eta_right"])
    expected_vector = (
        Fraction(),
        Fraction(-1),
        *((Fraction(),) * max(0, order - 1)),
    )[: order + 1]
    return {
        "dexp_left_equals_identity": reconstructed_left == identity,
        "dexp_right_equals_minus_exp": reconstructed_right
        == scale_series(exp, Fraction(-1)),
        "vector_subgroup_delta_v_equals_minus_ad_v_eta": vector_subgroup
        == expected_vector,
    }


def rendered_terms(coefficients: Sequence[Fraction], parameter: str) -> list[dict[str, object]]:
    return [
        {
            "degree": degree,
            "coefficient": fraction_text(coefficient),
            "word": parameter if degree == 0 else f"ad_V^{degree}({parameter})",
        }
        for degree, coefficient in enumerate(coefficients)
        if coefficient
    ]


def ward_subset_profile(level: int) -> dict[str, object]:
    if level < 0:
        raise ValueError("Ward level must be nonnegative")
    labels = tuple(range(1, level + 1))
    subsets = [
        subset
        for size in range(level + 1)
        for subset in combinations(labels, size)
    ]
    by_nonlinear_order = {
        str(size): sum(len(subset) == size for subset in subsets)
        for size in range(level + 1)
    }
    return {
        "level": level,
        "term_count": len(subsets),
        "expected_term_count": 2**level,
        "by_nonlinear_order": by_nonlinear_order,
        "seagull_contact_count": sum(len(subset) >= 2 for subset in subsets),
        "subsets": [list(subset) for subset in subsets],
    }


def vector_subgroup_profile(level: int) -> dict[str, object]:
    if level < 0:
        raise ValueError("Ward level must be nonnegative")
    return {
        "level": level,
        "same_level_commutator_terms": level,
        "output_representation_terms": 1,
        "higher_level_terms": 0,
        "identity": (
            "sum_j A_n(V_1,...,[eta,V_j],...,V_n)-rho_2(eta)A_n=0"
        ),
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload(order: int = DEFAULT_ORDER) -> dict[str, object]:
    coefficients = variation_coefficients(order)
    checks = exact_checks(order)
    return {
        "schema": "Step5BackgroundWardRecursion.v2",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "order": order,
        "source_equations": [
            "3D.80",
            "3D.81",
            "3D.82",
            "step5-one-loop-covariant-completion-gap-audit.md section 5",
        ],
        "group_equation": "E_B'=h_tilde_B*E_B*h_B^{-1}",
        "linearized_group_equation": (
            "dexp(ad_V)*delta_V=eta_L-exp(ad_V)*eta_R"
        ),
        "variation": {
            "eta_left": rendered_terms(coefficients["eta_left"], "eta_L"),
            "eta_right": rendered_terms(coefficients["eta_right"], "eta_R"),
        },
        "vector_subgroup": {
            "constraint": "eta_L=eta_R=eta",
            "result": "delta_V=-ad_V(eta)",
            "Taylor_maps": {"R_0": "0", "R_1": "[eta,V]", "R_r_ge_2": "0"},
            "level_mixing": False,
            "profiles": [vector_subgroup_profile(level) for level in range(7)],
        },
        "polarized_chiral_frame_Ward_recursion": {
            "frame": "GAUGE_CHIRAL",
            "finite_covariance": (
                "A_C[h_tilde*E*h^(-1)]=(Ad_h tensor Ad_h)A_C[E]"
            ),
            "output_representation": "rho_2(eta_R)",
            "identity": (
                "sum_(S subset [n]) A_(n-|S|+1)"
                "(R_|S|(V_S;eta_L,eta_R),V_(S^c))-rho_2(eta_R)A_n=0"
            ),
            "profiles": [ward_subset_profile(level) for level in range(7)],
            "quantum_insertion_status": (
                "FAIL_CLOSED_UNTIL_SOURCE_EXTENDED_WARD_IDENTITY_AND_"
                "RESTORATION_COUNTERTERM_ARE_PROVED"
            ),
        },
        "checks": checks,
        "external_results_imported": False,
        "graph_coefficients_present": False,
        "anomaly_coefficients_present": False,
    }


def write_artifacts(order: int = DEFAULT_ORDER) -> None:
    payload = build_payload(order)
    generated_bytes = canonical_json(payload)
    audit = {
        "schema": "Step5BackgroundWardRecursionAudit.v1",
        "status": payload["status"],
        "totals": {
            "checks": len(payload["checks"]),
            "failed": sum(not result for result in payload["checks"].values()),
        },
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "scope": (
            "formal background-prepotential variation and chiral-frame subset "
            "combinatorics only; no quantum Ward or graph acceptance"
        ),
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT.write_bytes(canonical_json(audit))


if __name__ == "__main__":
    write_artifacts()
