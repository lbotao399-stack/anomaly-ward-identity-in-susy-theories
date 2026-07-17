#!/usr/bin/env python3
"""Build the typed Step-5K momentum-rule and gauge-dispatcher ledger."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "generated" / "step5k-momentum-rule-ledger.json"
RULE_MEMO = ROOT / "audits" / "step5k-momentum-rules-and-fp-inverse.md"
DWORD = ROOT / "generated" / "step5k-ww-gauge-dword.json"
DIAGRAM_IR = ROOT / "audits" / "step5k-diagram-ir.json"

ComplexQ = tuple[Fraction, Fraction]
LaurentMonomial = tuple[int, int]
LaurentPolynomial = dict[LaurentMonomial, Fraction]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def q(value: Fraction | int) -> list[int]:
    value = Fraction(value)
    return [value.numerator, value.denominator]


def cq(value: ComplexQ) -> dict[str, list[int]]:
    return {"real": q(value[0]), "imaginary": q(value[1])}


def complex_product(left: ComplexQ, right: ComplexQ) -> ComplexQ:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def add_poly(
    left: LaurentPolynomial,
    right: LaurentPolynomial,
) -> LaurentPolynomial:
    output = dict(left)
    for monomial, coefficient in right.items():
        output[monomial] = output.get(monomial, Fraction(0)) + coefficient
        if output[monomial] == 0:
            del output[monomial]
    return output


def multiply_poly(
    left: LaurentPolynomial,
    right: LaurentPolynomial,
) -> LaurentPolynomial:
    output: LaurentPolynomial = {}
    for (p_left, mu_left), coefficient_left in left.items():
        for (p_right, mu_right), coefficient_right in right.items():
            monomial = p_left + p_right, mu_left + mu_right
            output[monomial] = (
                output.get(monomial, Fraction(0))
                + coefficient_left * coefficient_right
            )
    return {key: value for key, value in output.items() if value != 0}


def serialize_poly(polynomial: LaurentPolynomial) -> list[dict[str, Any]]:
    return [
        {
            "coefficient": q(coefficient),
            "p_d_squared_power": p_power,
            "mu_squared_power": mu_power,
        }
        for (p_power, mu_power), coefficient in sorted(
            polynomial.items(),
            key=lambda item: (-item[0][0], item[0][1]),
        )
    ]


PD2: LaurentPolynomial = {(1, 0): Fraction(1)}
MU2: LaurentPolynomial = {(0, 1): Fraction(1)}
PD2_INVERSE: LaurentPolynomial = {(-1, 0): Fraction(1)}
BAR_P2 = add_poly(PD2, MU2)
DRED_RATIO = multiply_poly(BAR_P2, PD2_INVERSE)
DRED_IDENTITY: LaurentPolynomial = {(0, 0): Fraction(1)}
DRED_DEFECT = add_poly(DRED_RATIO, {(0, 0): Fraction(-1)})


@dataclass(frozen=True)
class TypedOperator:
    coefficient: ComplexQ
    scalar_inverse: str
    spin_word: tuple[str, ...]
    source: str
    target: str


def serialize_operator(operator: TypedOperator | None) -> dict[str, Any] | None:
    if operator is None:
        return None
    return {
        "coefficient": cq(operator.coefficient),
        "scalar_inverse": operator.scalar_inverse,
        "spin_word": list(operator.spin_word),
        "source": operator.source,
        "target": operator.target,
    }


def compose_operator(left: TypedOperator, right: TypedOperator) -> TypedOperator:
    if right.target != left.source:
        raise ValueError(
            f"typed composition failure: {right.target} != {left.source}"
        )
    scalar_factors = [
        factor
        for factor in (left.scalar_inverse, right.scalar_inverse)
        if factor != "1"
    ]
    if len(scalar_factors) > 1:
        raise ValueError(f"unsupported scalar product {scalar_factors}")
    return TypedOperator(
        coefficient=complex_product(left.coefficient, right.coefficient),
        scalar_inverse=scalar_factors[0] if scalar_factors else "1",
        spin_word=left.spin_word + right.spin_word,
        source=right.source,
        target=left.target,
    )


def matrix_product(
    left: list[list[TypedOperator | None]],
    right: list[list[TypedOperator | None]],
) -> list[list[TypedOperator | None]]:
    output: list[list[TypedOperator | None]] = [[None, None], [None, None]]
    for row in range(2):
        for column in range(2):
            terms = [
                compose_operator(left[row][inner], right[inner][column])
                for inner in range(2)
                if left[row][inner] is not None
                and right[inner][column] is not None
            ]
            if len(terms) > 1:
                raise ValueError("unexpected multi-term FP matrix entry")
            output[row][column] = terms[0] if terms else None
    return output


def reduce_projector_product(
    operator: TypedOperator,
) -> dict[str, Any]:
    if operator.coefficient != (Fraction(1, 16), Fraction(0)):
        raise ValueError(f"projector coefficient is {operator.coefficient}")
    if operator.spin_word == ("barD2", "D2"):
        chirality = "+"
        projector = "P_+^bar4"
        spin_rewrite = "barD2*D2=16*barBox_E*P_+^bar4"
    elif operator.spin_word == ("D2", "barD2"):
        chirality = "-"
        projector = "P_-^bar4"
        spin_rewrite = "D2*barD2=16*barBox_E*P_-^bar4"
    else:
        raise ValueError(f"unreduced spin word {operator.spin_word}")
    if not operator.source.endswith(chirality):
        raise ValueError(
            f"projector chirality {chirality} does not match {operator.source}"
        )
    if operator.source != operator.target:
        raise ValueError(
            f"projector does not close: {operator.source}->{operator.target}"
        )

    if operator.scalar_inverse == "barBox_E^-1":
        scalar_result = "1"
        ratio = DRED_IDENTITY
        defect: LaurentPolynomial = {}
    elif operator.scalar_inverse == "Box_d^-1":
        scalar_result = "1+mu_p^2/p_d^2"
        ratio = DRED_RATIO
        defect = DRED_DEFECT
    else:
        raise ValueError(f"unexpected scalar inverse {operator.scalar_inverse}")

    return {
        "source": operator.source,
        "target": operator.target,
        "chirality": chirality,
        "coefficient_before_spin_rewrite": cq(operator.coefficient),
        "spin_rewrite": spin_rewrite,
        "projector": projector,
        "projector_action": f"{projector}=1_{operator.source}",
        "scalar_result": scalar_result,
        "ratio_laurent_polynomial": serialize_poly(ratio),
        "defect_laurent_polynomial": serialize_poly(defect),
        "result": (
            f"1_{operator.source}"
            if scalar_result == "1"
            else f"(1+mu_p^2/p_d^2)*1_{operator.source}"
        ),
    }


def reduce_product_matrix(
    matrix: list[list[TypedOperator | None]],
) -> list[list[dict[str, Any] | None]]:
    return [
        [
            reduce_projector_product(entry) if entry is not None else None
            for entry in row
        ]
        for row in matrix
    ]


def build_fp_block() -> dict[str, Any]:
    zero = Fraction(0)
    quarter = Fraction(1, 4)
    kernel: list[list[TypedOperator | None]] = [
        [
            None,
            TypedOperator(
                (zero, quarter), "1", ("barD2",), "G-", "F+"
            ),
        ],
        [
            TypedOperator(
                (zero, -quarter), "1", ("D2",), "G+", "F-"
            ),
            None,
        ],
    ]

    def inverse(scalar_inverse: str) -> list[list[TypedOperator | None]]:
        return [
            [
                None,
                TypedOperator(
                    (zero, quarter),
                    scalar_inverse,
                    ("barD2",),
                    "F-",
                    "G+",
                ),
            ],
            [
                TypedOperator(
                    (zero, -quarter),
                    scalar_inverse,
                    ("D2",),
                    "F+",
                    "G-",
                ),
                None,
            ],
        ]

    inverse_bar4 = inverse("barBox_E^-1")
    inverse_d = inverse("Box_d^-1")
    exact_right = matrix_product(kernel, inverse_bar4)
    exact_left = matrix_product(inverse_bar4, kernel)
    dred_right = matrix_product(kernel, inverse_d)
    dred_left = matrix_product(inverse_d, kernel)

    return {
        "domain_basis": ["G+", "G-"],
        "codomain_basis": ["F+", "F-"],
        "kernel": [
            [serialize_operator(entry) for entry in row] for row in kernel
        ],
        "inverse_bar4": [
            [serialize_operator(entry) for entry in row]
            for row in inverse_bar4
        ],
        "inverse_d": [
            [serialize_operator(entry) for entry in row] for row in inverse_d
        ],
        "right_inverse_bar4": {
            "composition": "K_FP*inverse_bar4",
            "space": "F_perp",
            "raw": [
                [serialize_operator(entry) for entry in row]
                for row in exact_right
            ],
            "reduced": reduce_product_matrix(exact_right),
        },
        "left_inverse_bar4": {
            "composition": "inverse_bar4*K_FP",
            "space": "G_perp",
            "raw": [
                [serialize_operator(entry) for entry in row]
                for row in exact_left
            ],
            "reduced": reduce_product_matrix(exact_left),
        },
        "right_composition_d": {
            "composition": "K_FP*inverse_d",
            "space": "F_perp",
            "raw": [
                [serialize_operator(entry) for entry in row]
                for row in dred_right
            ],
            "reduced": reduce_product_matrix(dred_right),
        },
        "left_composition_d": {
            "composition": "inverse_d*K_FP",
            "space": "G_perp",
            "raw": [
                [serialize_operator(entry) for entry in row]
                for row in dred_left
            ],
            "reduced": reduce_product_matrix(dred_left),
        },
    }


def scalar_inverse_ledger() -> dict[str, Any]:
    ratio = serialize_poly(DRED_RATIO)
    defect = serialize_poly(DRED_DEFECT)
    return {
        "variables": {
            "bar_p_squared": "p_d^2+mu_p^2",
            "mu_p_squared": "bar_p^2-p_d^2",
        },
        "bar_p_squared_over_p_d_squared": ratio,
        "identity": serialize_poly(DRED_IDENTITY),
        "defect": defect,
        "exact_result": "bar_p^2/p_d^2=1+mu_p^2/p_d^2",
    }


def exact_and_dred_products(space: str) -> dict[str, Any]:
    return {
        "exact_left": f"1_{space}",
        "exact_right": f"1_{space}",
        "dred_left": {
            "result": f"(1+mu_p^2/p_d^2)*1_{space}",
            "ratio_laurent_polynomial": serialize_poly(DRED_RATIO),
            "defect_laurent_polynomial": serialize_poly(DRED_DEFECT),
        },
        "dred_right": {
            "result": f"(1+mu_p^2/p_d^2)*1_{space}",
            "ratio_laurent_polynomial": serialize_poly(DRED_RATIO),
            "defect_laurent_polynomial": serialize_poly(DRED_DEFECT),
        },
    }


def build_quadratic_blocks() -> dict[str, Any]:
    return {
        "scalar_inverse_ledger": scalar_inverse_ledger(),
        "vector": {
            "space": "U_bar4_perp",
            "kernel_bar4": {
                "coefficient": q(1),
                "color": "kappa_AB",
                "operator": "barBox_E",
            },
            "inverse_bar4": {
                "coefficient": q(1),
                "color": "kappa^AB",
                "operator": "barBox_E^-1",
            },
            "inverse_d": {
                "coefficient": q(1),
                "color": "kappa^AB",
                "operator": "Box_d^-1",
            },
            "products": exact_and_dred_products("U_bar4_perp"),
            "momentum_propagator": (
                "-(2*pi)^d*delta_d(p+p')*hbar*kappa^AB*"
                "delta4(theta_1-theta_2)/p_d^2"
            ),
            "memo_equations": ["K.23", "K.23a", "K.24", "K.24a"],
        },
        "matter_plus": {
            "orientation": "Phi_c_to_tildePhi_c",
            "space": "Sigma_E,+",
            "kernel_bar4": {
                "coefficient": q(-1),
                "color": "kappa_AB",
                "operator": "1_+",
            },
            "inverse_bar4": {
                "coefficient": q(-1),
                "color": "kappa^AB",
                "operator": "P_+^bar4=barD2*D2/(16*barBox_E)",
            },
            "inverse_d": {
                "coefficient": q(-1),
                "color": "kappa^AB",
                "operator": "R_+^d=barD2*D2/(16*Box_d)",
            },
            "products": exact_and_dred_products("Sigma_E,+"),
            "momentum_propagator": (
                "+(2*pi)^d*delta_d(p+p')*delta_rs*hbar*kappa^AB*"
                "barD2(p)*D2(p)*delta4(theta_1-theta_2)/(16*p_d^2)"
            ),
            "memo_equations": ["K.25", "K.26", "K.27", "K.28", "K.29"],
        },
        "matter_minus": {
            "orientation": "tildePhi_c_to_Phi_c",
            "space": "Sigma_E,-",
            "kernel_bar4": {
                "coefficient": q(-1),
                "color": "kappa_AB",
                "operator": "1_-",
            },
            "inverse_bar4": {
                "coefficient": q(-1),
                "color": "kappa^AB",
                "operator": "P_-^bar4=D2*barD2/(16*barBox_E)",
            },
            "inverse_d": {
                "coefficient": q(-1),
                "color": "kappa^AB",
                "operator": "R_-^d=D2*barD2/(16*Box_d)",
            },
            "products": exact_and_dred_products("Sigma_E,-"),
            "momentum_propagator": (
                "+(2*pi)^d*delta_d(p+p')*delta_rs*hbar*kappa^AB*"
                "D2(p)*barD2(p)*delta4(theta_1-theta_2)/(16*p_d^2)"
            ),
            "memo_equations": [
                "K.26",
                "K.27",
                "K.27a",
                "K.27b",
                "K.28",
                "K.29",
            ],
        },
        "fp": build_fp_block(),
    }


def gauge_action_coefficient(
    n: int,
    chirality: str,
    p: int,
    q_value: int,
    r: int,
    s: int,
) -> tuple[Fraction, int, int]:
    exponent = p + r if chirality == "+" else q_value + s
    denominator = (
        256
        * factorial(p)
        * factorial(q_value)
        * factorial(r)
        * factorial(s)
        * (p + q_value + 1)
        * (r + s + 1)
    )
    raw = Fraction(-((-1) ** exponent), denominator)
    rational = raw * (2 ** (n // 2))
    return rational, n % 2, n - 2


def coefficient_expression(
    rational: Fraction,
    sqrt2_power: int,
    g_power: int,
) -> str:
    sign = "+" if rational >= 0 else "-"
    absolute = abs(rational)
    factors = [str(absolute.numerator)]
    if sqrt2_power:
        factors.append("sqrt(2)")
    if g_power == 1:
        factors.append("g")
    elif g_power:
        factors.append(f"g^{g_power}")
    numerator = "*".join(factors)
    if absolute.denominator != 1:
        return f"{sign}{numerator}/{absolute.denominator}"
    return f"{sign}{numerator}"


def ordered_slots(
    p: int,
    q_value: int,
    r: int,
    s: int,
) -> list[dict[str, str | int]]:
    slots: list[dict[str, str | int]] = []
    for index in range(p):
        slots.append(
            {"id": f"L.pre.{index + 1}", "block": "left", "role": "plain_u"}
        )
    slots.append({"id": "L.D", "block": "left", "role": "distinguished_u"})
    for index in range(q_value):
        slots.append(
            {"id": f"L.post.{index + 1}", "block": "left", "role": "plain_u"}
        )
    for index in range(r):
        slots.append(
            {"id": f"R.pre.{index + 1}", "block": "right", "role": "plain_u"}
        )
    slots.append({"id": "R.D", "block": "right", "role": "distinguished_u"})
    for index in range(s):
        slots.append(
            {"id": f"R.post.{index + 1}", "block": "right", "role": "plain_u"}
        )
    return slots


def build_raw_gauge_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for n in (3, 4):
        for chirality in ("+", "-"):
            for p in range(n - 1):
                for q_value in range(n - 1 - p):
                    for r in range(n - 1 - p - q_value):
                        s = n - 2 - p - q_value - r
                        rational, sqrt2_power, g_power = gauge_action_coefficient(
                            n, chirality, p, q_value, r, s
                        )
                        monomial = f"{p}{q_value}{r}{s}"
                        slots = ordered_slots(p, q_value, r, s)
                        outer = "barD2" if chirality == "+" else "D2"
                        left_d = "D^a" if chirality == "+" else "barD_dot_a"
                        right_d = "D_a" if chirality == "+" else "barD^dot_a"
                        half_measure = "E,+" if chirality == "+" else "E,-"
                        full_conversion = (
                            "-D2/(4*barBox_E)"
                            if chirality == "+"
                            else "-barD2/(4*barBox_E)"
                        )
                        left_slots = [
                            slot["id"] for slot in slots if slot["block"] == "left"
                        ]
                        right_slots = [
                            slot["id"] for slot in slots if slot["block"] == "right"
                        ]
                        rows.append(
                            {
                                "id": f"G{n}:{chirality}:{monomial}",
                                "n": n,
                                "chirality": chirality,
                                "pqrs": [p, q_value, r, s],
                                "raw_monomial": monomial,
                                "action_coefficient_after_h_equals_g_minus2": {
                                    "rational": q(rational),
                                    "sqrt2_power": sqrt2_power,
                                    "g_power": g_power,
                                    "expression": coefficient_expression(
                                        rational, sqrt2_power, g_power
                                    ),
                                },
                                "coupling_reduction": (
                                    "(sqrt(2)*g)^n*h*kappa_AB with h=g^-2"
                                ),
                                "sign_exponent": "p+r" if chirality == "+" else "q+s",
                                "color_map": {
                                    "metric": "kappa_AB",
                                    "left_output_index": "A",
                                    "right_output_index": "B",
                                    "ordered_rule": (
                                        "kappa_AB*Coeff^A(left ordered adjoint word)*"
                                        "Coeff^B(right ordered adjoint word)"
                                    ),
                                    "left_ordered_slots": left_slots,
                                    "right_ordered_slots": right_slots,
                                },
                                "ordered_slots": slots,
                                "operator_map": {
                                    "left_outer": outer,
                                    "right_outer": outer,
                                    "left_distinguished": left_d,
                                    "right_distinguished": right_d,
                                    "left_outer_momentum": "sum of left ordered-slot momenta",
                                    "right_outer_momentum": "sum of right ordered-slot momenta",
                                    "distinguished_momentum": (
                                        "momentum of the corresponding L.D or R.D slot"
                                    ),
                                },
                                "measure": {
                                    "half_superspace": half_measure,
                                    "exact_full_measure_conversion": full_conversion,
                                },
                                "momentum_delta": (
                                    "(2*pi)^d*delta_d(p_1+...+p_n)"
                                ),
                                "ordinary_vertex_factor": "-C_E/hbar",
                                "memo_equation": "K.54" if chirality == "+" else "K.55",
                            }
                        )
    return rows


def momentum_sum(labels: list[int]) -> str:
    return "+".join(f"p_{label}" for label in labels)


def build_labeled_gauge_rows(
    raw_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for raw in raw_rows:
        n = raw["n"]
        slots = raw["ordered_slots"]
        for permutation in itertools.permutations(range(1, n + 1)):
            assignments = [
                {
                    "slot": slot["id"],
                    "block": slot["block"],
                    "role": slot["role"],
                    "label": label,
                    "color_index": f"A_{label}",
                    "momentum": f"p_{label}",
                }
                for slot, label in zip(slots, permutation, strict=True)
            ]
            left = [row for row in assignments if row["block"] == "left"]
            right = [row for row in assignments if row["block"] == "right"]
            left_d = next(row for row in left if row["role"] == "distinguished_u")
            right_d = next(row for row in right if row["role"] == "distinguished_u")
            outer = raw["operator_map"]["left_outer"]
            left_distinguished = raw["operator_map"]["left_distinguished"]
            right_distinguished = raw["operator_map"]["right_distinguished"]
            permutation_id = "".join(str(label) for label in permutation)
            rows.append(
                {
                    "id": f"{raw['id']}:P{permutation_id}",
                    "raw_row_id": raw["id"],
                    "functional_derivative_order": [
                        f"delta/delta u^(A_{label})(p_{label})"
                        for label in range(n, 0, -1)
                    ],
                    "koszul_sign": 1,
                    "ordered_slot_assignment": assignments,
                    "action_coefficient_after_h_equals_g_minus2": raw[
                        "action_coefficient_after_h_equals_g_minus2"
                    ],
                    "color_map": {
                        "metric": "kappa_AB",
                        "left_ordered_color_word": [
                            row["color_index"] for row in left
                        ],
                        "right_ordered_color_word": [
                            row["color_index"] for row in right
                        ],
                        "expression": (
                            "kappa_AB*Coeff^A(T_"
                            + "*T_".join(str(row["label"]) for row in left)
                            + ")*Coeff^B(T_"
                            + "*T_".join(str(row["label"]) for row in right)
                            + ")"
                        ),
                    },
                    "operator_momentum_map": {
                        "left_outer": f"{outer}({momentum_sum([row['label'] for row in left])})",
                        "left_distinguished": (
                            f"{left_distinguished}(p_{left_d['label']})"
                        ),
                        "right_outer": f"{outer}({momentum_sum([row['label'] for row in right])})",
                        "right_distinguished": (
                            f"{right_distinguished}(p_{right_d['label']})"
                        ),
                    },
                    "momentum_delta": (
                        "(2*pi)^d*delta_d("
                        + momentum_sum(list(range(1, n + 1)))
                        + ")"
                    ),
                    "ordinary_vertex_factor": "-C_E/hbar",
                }
            )
    return rows


def fraction_from_json(value: list[int]) -> Fraction:
    return Fraction(value[0], value[1])


def expected_cubic_coefficients(
    raw_rows: list[dict[str, Any]],
) -> dict[tuple[str, str], str]:
    return {
        (row["chirality"], row["raw_monomial"]): row[
            "action_coefficient_after_h_equals_g_minus2"
        ]["expression"]
        for row in raw_rows
        if row["n"] == 3
    }


def build_dword_cross_binding(
    raw_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    document = json.loads(DWORD.read_text(encoding="utf-8"))
    rows = document.get("full_contact_rows", [])
    observed: dict[tuple[str, str], set[str]] = {}
    for row in rows:
        key = row.get("chirality"), row.get("raw_monomial")
        observed.setdefault(key, set()).add(row.get("coefficient_canonical_u"))
    expected = expected_cubic_coefficients(raw_rows)
    if set(observed) != set(expected):
        raise ValueError(
            f"D-word cubic keys {sorted(observed)} != {sorted(expected)}"
        )
    mismatches = {
        key: {"expected": expected[key], "observed": sorted(observed[key])}
        for key in sorted(expected)
        if observed[key] != {expected[key]}
    }
    if mismatches:
        raise ValueError(f"D-word cubic coefficient mismatch: {mismatches}")
    return {
        "artifact": str(DWORD.relative_to(ROOT)),
        "artifact_sha256": sha256(DWORD),
        "full_contact_row_count": len(rows),
        "unique_cubic_raw_row_count": len(observed),
        "rows": [
            {
                "chirality": key[0],
                "raw_monomial": key[1],
                "coefficient": expected[key],
                "matched": True,
            }
            for key in sorted(expected)
        ],
        "matched": True,
    }


def build_diagram_cross_binding(
    raw_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    document = json.loads(DIAGRAM_IR.read_text(encoding="utf-8"))
    graphs = {row["id"]: row for row in document.get("graphs", [])}
    gauge = graphs.get("G-WW-GAUGE-01")
    if gauge is None:
        raise ValueError("diagram IR lacks G-WW-GAUGE-01")
    by_kind: dict[str, list[dict[str, Any]]] = {}
    for vertex in gauge.get("vertices", []):
        by_kind.setdefault(vertex.get("kind"), []).append(vertex)

    expected = {
        "GAUGE_CUBIC_CHIRAL": {
            "chirality": "+",
            "id": "VW",
            "factor": "-i*g/(4*hbar)",
            "label_tex": (
                "\\mathfrak V_W=-\\frac{ig}{4\\hbar}c_{VC'E}"
                "W_c^{E\\gamma}(D_{C'\\gamma}-D_{V\\gamma})"
            ),
            "color": "c_{VC'E}",
            "operator_difference": "D_C'-D_V",
        },
        "GAUGE_CUBIC_ANTICHIRAL": {
            "chirality": "-",
            "id": "VBAR",
            "factor": "+i*g/(4*hbar)",
            "label_tex": (
                "\\mathfrak V_{\\widetilde W}=+\\frac{ig}{4\\hbar}"
                "c_{UCD}\\widetilde W_c^D{}_{\\dot\\alpha}"
                "(\\bar D_C^{\\dot\\alpha}-\\bar D_U^{\\dot\\alpha})"
            ),
            "color": "c_{UCD}",
            "operator_difference": "barD_C-barD_U",
        },
    }
    coefficient_ledger = json.loads(DWORD.read_text(encoding="utf-8")).get(
        "coefficient_ledger", {}
    )
    ledger_factors = {
        "GAUGE_CUBIC_CHIRAL": coefficient_ledger.get("exponent_vertex_W"),
        "GAUGE_CUBIC_ANTICHIRAL": coefficient_ledger.get(
            "exponent_vertex_barW"
        ),
    }
    output_rows = []
    for kind, specification in expected.items():
        vertices = by_kind.get(kind, [])
        if len(vertices) != 1:
            raise ValueError(f"diagram IR has {len(vertices)} vertices of {kind}")
        vertex = vertices[0]
        if vertex.get("id") != specification["id"]:
            raise ValueError(f"{kind} id mismatch: {vertex.get('id')}")
        if vertex.get("label_tex") != specification["label_tex"]:
            raise ValueError(f"{kind} TeX label mismatch")
        if ledger_factors[kind] != specification["factor"]:
            raise ValueError(
                f"{kind} D-word factor {ledger_factors[kind]} != "
                f"{specification['factor']}"
            )
        source_ids = [
            row["id"]
            for row in raw_rows
            if row["n"] == 3
            and row["chirality"] == specification["chirality"]
        ]
        output_rows.append(
            {
                "kind": kind,
                "diagram_vertex_id": vertex["id"],
                "chirality": specification["chirality"],
                "polarized_factor": specification["factor"],
                "color": specification["color"],
                "operator_difference": specification["operator_difference"],
                "source_raw_row_ids": source_ids,
                "label_tex": vertex["label_tex"],
                "matched": True,
            }
        )
    return {
        "artifact": str(DIAGRAM_IR.relative_to(ROOT)),
        "artifact_sha256": sha256(DIAGRAM_IR),
        "graph_id": gauge["id"],
        "vertices": output_rows,
        "matched": True,
    }


def validate_dispatcher(
    raw_rows: list[dict[str, Any]],
    labeled_rows: list[dict[str, Any]],
) -> list[str]:
    errors: list[str] = []
    if len(raw_rows) != 28:
        errors.append(f"raw gauge row count {len(raw_rows)} != 28")
    if len({row["id"] for row in raw_rows}) != 28:
        errors.append("raw gauge row ids are not unique")
    counts = Counter((row["n"], row["chirality"]) for row in raw_rows)
    if counts != {(3, "+"): 4, (3, "-"): 4, (4, "+"): 10, (4, "-"): 10}:
        errors.append(f"raw gauge row partition mismatch: {counts}")
    if len(labeled_rows) != 528:
        errors.append(f"labeled gauge row count {len(labeled_rows)} != 528")
    if len({row["id"] for row in labeled_rows}) != 528:
        errors.append("labeled gauge row ids are not unique")

    raw_by_id = {row["id"]: row for row in raw_rows}
    labeled_counts = Counter(row["raw_row_id"] for row in labeled_rows)
    for raw_id, raw in raw_by_id.items():
        expected_count = factorial(raw["n"])
        if labeled_counts[raw_id] != expected_count:
            errors.append(
                f"{raw_id} labeled count {labeled_counts[raw_id]} != {expected_count}"
            )
    for row in labeled_rows:
        raw = raw_by_id.get(row["raw_row_id"])
        if raw is None:
            errors.append(f"unknown raw row {row['raw_row_id']}")
            continue
        if row["action_coefficient_after_h_equals_g_minus2"] != raw[
            "action_coefficient_after_h_equals_g_minus2"
        ]:
            errors.append(f"{row['id']} coefficient differs from raw row")
        labels = [item["label"] for item in row["ordered_slot_assignment"]]
        if sorted(labels) != list(range(1, raw["n"] + 1)):
            errors.append(f"{row['id']} is not a label permutation")
        if row["koszul_sign"] != 1:
            errors.append(f"{row['id']} has nontrivial even-vector Koszul sign")

    coefficient_map = {
        (row["n"], row["chirality"], tuple(row["pqrs"])): fraction_from_json(
            row["action_coefficient_after_h_equals_g_minus2"]["rational"]
        )
        for row in raw_rows
    }
    monomials_by_n = {
        n: {
            tuple(row["pqrs"])
            for row in raw_rows
            if row["n"] == n and row["chirality"] == "+"
        }
        for n in (3, 4)
    }
    for monomial in monomials_by_n[3]:
        if coefficient_map[(3, "-", monomial)] != -coefficient_map[
            (3, "+", monomial)
        ]:
            errors.append(f"cubic chirality sign relation fails at {monomial}")
    for monomial in monomials_by_n[4]:
        if coefficient_map[(4, "-", monomial)] != coefficient_map[
            (4, "+", monomial)
        ]:
            errors.append(f"quartic chirality relation fails at {monomial}")
    return errors


def validate_quadratic_blocks(blocks: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if DRED_RATIO != {(0, 0): Fraction(1), (-1, 1): Fraction(1)}:
        errors.append(f"DRED ratio polynomial mismatch: {DRED_RATIO}")
    if DRED_DEFECT != {(-1, 1): Fraction(1)}:
        errors.append(f"DRED defect polynomial mismatch: {DRED_DEFECT}")
    for sector in ("vector", "matter_plus", "matter_minus"):
        products = blocks[sector]["products"]
        if not products["exact_left"].startswith("1_"):
            errors.append(f"{sector} exact left product is not identity")
        if not products["exact_right"].startswith("1_"):
            errors.append(f"{sector} exact right product is not identity")
        for order in ("dred_left", "dred_right"):
            if products[order]["defect_laurent_polynomial"] != serialize_poly(
                DRED_DEFECT
            ):
                errors.append(f"{sector} {order} defect mismatch")

    fp = blocks["fp"]
    for key in ("right_inverse_bar4", "left_inverse_bar4"):
        reduced = fp[key]["reduced"]
        diagonal = [reduced[0][0], reduced[1][1]]
        if any(row is None or row["scalar_result"] != "1" for row in diagonal):
            errors.append(f"FP {key} is not an exact identity")
        if reduced[0][1] is not None or reduced[1][0] is not None:
            errors.append(f"FP {key} has an off-diagonal product")
    for key in ("right_composition_d", "left_composition_d"):
        reduced = fp[key]["reduced"]
        diagonal = [reduced[0][0], reduced[1][1]]
        if any(
            row is None
            or row["defect_laurent_polynomial"] != serialize_poly(DRED_DEFECT)
            for row in diagonal
        ):
            errors.append(f"FP {key} DRED defect mismatch")
        if reduced[0][1] is not None or reduced[1][0] is not None:
            errors.append(f"FP {key} has an off-diagonal product")
    return errors


def build_document() -> dict[str, Any]:
    raw_rows = build_raw_gauge_rows()
    labeled_rows = build_labeled_gauge_rows(raw_rows)
    quadratic_blocks = build_quadratic_blocks()
    errors = validate_quadratic_blocks(quadratic_blocks)
    errors.extend(validate_dispatcher(raw_rows, labeled_rows))
    if errors:
        raise ValueError("; ".join(errors))
    return {
        "schema": "step5k-momentum-rule-ledger-v1",
        "status": "DERIVED_EXACT_TYPED_RULES",
        "generated": True,
        "generator": "scripts/build_step5k_momentum_rule_ledger.py",
        "rule_memo": str(RULE_MEMO.relative_to(ROOT)),
        "rule_memo_sha256": sha256(RULE_MEMO),
        "memo_equations": {
            "vector": "K.19--K.24a",
            "matter": "K.25--K.29",
            "fp": "K.30--K.53c",
            "gauge_dispatcher": "K.54--K.56",
        },
        "coupling_branch": {
            "h": "g^-2",
            "f_AB": "h*kappa_AB",
            "tilde_f_AB": "h*kappa_AB",
            "canonical_vector": "u=V/(sqrt(2)*g)",
        },
        "typed_quadratic_blocks": quadratic_blocks,
        "gauge_dispatcher": {
            "raw_rows": raw_rows,
            "labeled_rows": labeled_rows,
            "invariants": {
                "raw_row_count": len(raw_rows),
                "raw_unique_row_id_count": len({row["id"] for row in raw_rows}),
                "cubic_raw_rows_per_chirality": 4,
                "quartic_raw_rows_per_chirality": 10,
                "labeled_row_count": len(labeled_rows),
                "labeled_unique_row_id_count": len(
                    {row["id"] for row in labeled_rows}
                ),
                "cubic_labeled_row_count": sum(
                    1
                    for row in labeled_rows
                    if raw_rows_by_id(raw_rows)[row["raw_row_id"]]["n"] == 3
                ),
                "quartic_labeled_row_count": sum(
                    1
                    for row in labeled_rows
                    if raw_rows_by_id(raw_rows)[row["raw_row_id"]]["n"] == 4
                ),
                "cubic_chirality_relation": "c_minus=-c_plus",
                "quartic_chirality_relation": "c_minus=c_plus",
                "unresolved": 0,
            },
        },
        "cross_bindings": {
            "dword_cubic_raw_rows": build_dword_cross_binding(raw_rows),
            "diagram_polarized_vertices": build_diagram_cross_binding(raw_rows),
        },
        "unresolved": [],
    }


def raw_rows_by_id(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["id"]: row for row in rows}


def rendered_document(document: dict[str, Any]) -> str:
    return json.dumps(
        document,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    try:
        document = build_document()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL STEP5K_MOMENTUM_RULE_LEDGER: {error}")
        return 1
    rendered = rendered_document(document)

    if args.write:
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        TARGET.write_text(rendered, encoding="utf-8")
        print(
            "WROTE STEP5K_MOMENTUM_RULE_LEDGER "
            "28 RAW / 528 LABELED"
        )
        return 0

    if args.check:
        if not TARGET.is_file():
            print(f"FAIL missing {TARGET}")
            return 1
        actual = TARGET.read_text(encoding="utf-8")
        if actual != rendered:
            print("FAIL stale generated/step5k-momentum-rule-ledger.json")
            return 1
        print(
            "PASS STEP5K_MOMENTUM_RULE_LEDGER "
            "28 RAW / 528 LABELED / FP+VECTOR+MATTER TYPED"
        )
        return 0

    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
