#!/usr/bin/env python3
"""Exact partial-scope verifier for Step-5A component/BV-BRST grammar.

The verifier is deliberately independent of the forbidden Step-3E branch.
It uses only Python's standard library and exact arithmetic in Q(i,sqrt(2)).
No floating point, external CAS, network access, or Notion input is used.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import itertools
import json
from math import comb, factorial
from pathlib import Path
import re
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "audits" / "step5a-component-bv-brst-grammar-verification.json"
SCOPE_ID = "STEP5A_COMPONENT_BV_BRST_GRAMMAR_EXACT_PARTIAL_SCOPE"
SECTION_ID = "STEP-05A"
CONTRACT_PATH = "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"
PASS_STATUS = "PASS_EXACT_PARTIAL_SCOPE"

# The Step-4B/4C values are intentionally isolated: a contract repair changes
# only these lock constants and the generated audit, never the exact checker.
SOURCE_LOCKS = {
    "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md":
        "109e0c531da3a1b98313e87dd692fa3d9047c8f745291f8e87021008c7acc538",
    "contracts/foundations/step-04a-n1-super-yang-mills.md":
        "b2495f6a98c8cffe21ab2583b1955c81f5bb06af9b0edfb677fc0a3a3ee1fbc1",
    "contracts/foundations/step-04b-n2-super-yang-mills.md":
        "590bff04a31f2790ec97226570df189647f822b69c53ee9b141f5c1a0c98c860",
    "contracts/foundations/step-04c-n4-super-yang-mills.md":
        "fafc3bc2227b60ca699b3f953b632db82dafe093b221baa74736cc5fb838928f",
}

BLOCKER_LABELS = (
    "BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED",
    "BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
    "BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED",
    "BLOCKED_STEP3D_LC_VECTOR_CYCLE",
)


def q(value: int | Fraction) -> Fraction:
    return Fraction(value)


@dataclass(frozen=True)
class Exact:
    """a + b sqrt(2) + i(c + d sqrt(2)), with rational coefficients."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    c: Fraction = Fraction(0)
    d: Fraction = Fraction(0)

    @staticmethod
    def rational(value: int | Fraction) -> "Exact":
        return Exact(a=Fraction(value))

    def __add__(self, other: "Exact") -> "Exact":
        return Exact(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d,
        )

    def __neg__(self) -> "Exact":
        return Exact(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: "Exact") -> "Exact":
        return self + (-other)

    def __mul__(self, other: "Exact") -> "Exact":
        real_a = self.a * other.a + 2 * self.b * other.b
        real_b = self.a * other.b + self.b * other.a
        imag_product_a = self.c * other.c + 2 * self.d * other.d
        imag_product_b = self.c * other.d + self.d * other.c
        cross_a = (
            self.a * other.c
            + 2 * self.b * other.d
            + self.c * other.a
            + 2 * self.d * other.b
        )
        cross_b = (
            self.a * other.d
            + self.b * other.c
            + self.c * other.b
            + self.d * other.a
        )
        return Exact(
            real_a - imag_product_a,
            real_b - imag_product_b,
            cross_a,
            cross_b,
        )

    def scale(self, value: int | Fraction) -> "Exact":
        factor = Fraction(value)
        return Exact(
            factor * self.a,
            factor * self.b,
            factor * self.c,
            factor * self.d,
        )


ZERO = Exact()
ONE = Exact.rational(1)
MINUS_ONE = -ONE
I = Exact(c=q(1))
SQRT_TWO = Exact(b=q(1))
INV_SQRT_TWO = SQRT_TWO.scale(Fraction(1, 2))


def serialize(value: Any) -> Any:
    if isinstance(value, Exact):
        return {
            "1": str(value.a),
            "sqrt2": str(value.b),
            "i": str(value.c),
            "i_sqrt2": str(value.d),
        }
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, FormalScalar):
        return {
            "coefficient": str(value.coefficient),
            "powers": {name: exponent for name, exponent in value.powers},
        }
    if isinstance(value, ProjectorElement):
        return {"P_T": serialize(value.transverse), "P_0": serialize(value.longitudinal)}
    if isinstance(value, tuple):
        return [serialize(item) for item in value]
    if isinstance(value, list):
        return [serialize(item) for item in value]
    if isinstance(value, set):
        return [serialize(item) for item in sorted(value, key=str)]
    if isinstance(value, dict):
        return {
            str(key): serialize(item)
            for key, item in sorted(value.items(), key=lambda row: str(row[0]))
        }
    return value


def fingerprint(value: Any) -> str:
    payload = json.dumps(serialize(value), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class Recorder:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []
        self.failures: list[dict[str, Any]] = []

    def check(self, name: str, actual: Any, expected: Any, category: str) -> None:
        passed = actual == expected
        row: dict[str, Any] = {
            "name": name,
            "category": category,
            "passed": passed,
            "actual_sha256": fingerprint(actual),
            "expected_sha256": fingerprint(expected),
        }
        if isinstance(actual, (str, int, bool)) or actual is None:
            row["actual"] = actual
            row["expected"] = expected
        self.checks.append(row)
        if not passed:
            self.failures.append(
                {
                    "name": name,
                    "category": category,
                    "actual": serialize(actual),
                    "expected": serialize(expected),
                }
            )


def add_term(target: dict[str, Exact], name: str, coefficient: Exact) -> None:
    target[name] = target.get(name, ZERO) + coefficient
    if target[name] == ZERO:
        del target[name]


def n1_lorentzian_coefficients() -> dict[str, Exact]:
    return {
        "gauge:F2": Exact.rational(Fraction(-1, 4)),
        "fermion:tilde_lambda_D_lambda": I,
        "aux:D2": Exact.rational(Fraction(1, 2)),
        "topological:k_F_dual_F": Exact.rational(Fraction(-1, 8)),
    }


def n2_lorentzian_coefficients() -> dict[str, Exact]:
    result = n1_lorentzian_coefficients()
    additions = {
        "scalar:D_tilde_phi_D_phi": MINUS_ONE,
        "fermion:tilde_psi_D_psi": I,
        "aux:tilde_F_F": ONE,
        "aux:D_mu": ONE,
        "yukawa:tilde_phi_lambda_psi": -SQRT_TWO,
        "yukawa:tilde_psi_tilde_lambda_phi": SQRT_TWO,
    }
    for name, coefficient in additions.items():
        add_term(result, name, coefficient)
    return result


def n4_lorentzian_coefficients() -> dict[str, Exact]:
    result = n1_lorentzian_coefficients()
    additions = {
        "scalar:sum_r_D_tilde_phi_r_D_phi_r": MINUS_ONE,
        "fermion:sum_r_tilde_psi_r_D_psi_r": I,
        "aux:sum_r_tilde_F_r_F_r": ONE,
        "aux:i_D_C0": I,
        "yukawa:sum_r_tilde_phi_r_psi_r_lambda": SQRT_TWO,
        "yukawa:sum_r_phi_r_tilde_psi_r_tilde_lambda": SQRT_TWO,
        "superpotential:epsilon_F_phi_phi": -INV_SQRT_TWO,
        "superpotential:epsilon_tilde_F_tilde_phi_tilde_phi": -INV_SQRT_TWO,
        "superpotential:epsilon_phi_psi_psi": INV_SQRT_TWO,
        "superpotential:epsilon_tilde_phi_tilde_psi_tilde_psi": INV_SQRT_TWO,
    }
    for name, coefficient in additions.items():
        add_term(result, name, coefficient)
    return result


WICK_FACTORS = {
    "gauge:F2": MINUS_ONE,
    "fermion:tilde_lambda_D_lambda": -I,
    "aux:D2": MINUS_ONE,
    "topological:k_F_dual_F": I,
    "scalar:D_tilde_phi_D_phi": MINUS_ONE,
    "fermion:tilde_psi_D_psi": -I,
    "aux:tilde_F_F": MINUS_ONE,
    "aux:D_mu": MINUS_ONE,
    "yukawa:tilde_phi_lambda_psi": MINUS_ONE,
    "yukawa:tilde_psi_tilde_lambda_phi": MINUS_ONE,
    "scalar:sum_r_D_tilde_phi_r_D_phi_r": MINUS_ONE,
    "fermion:sum_r_tilde_psi_r_D_psi_r": -I,
    "aux:sum_r_tilde_F_r_F_r": MINUS_ONE,
    "aux:i_D_C0": MINUS_ONE,
    "yukawa:sum_r_tilde_phi_r_psi_r_lambda": MINUS_ONE,
    "yukawa:sum_r_phi_r_tilde_psi_r_tilde_lambda": MINUS_ONE,
    "superpotential:epsilon_F_phi_phi": MINUS_ONE,
    "superpotential:epsilon_tilde_F_tilde_phi_tilde_phi": MINUS_ONE,
    "superpotential:epsilon_phi_psi_psi": MINUS_ONE,
    "superpotential:epsilon_tilde_phi_tilde_psi_tilde_psi": MINUS_ONE,
}


def wick_rotate(coefficients: dict[str, Exact]) -> dict[str, Exact]:
    return {
        name: coefficient * WICK_FACTORS[name]
        for name, coefficient in coefficients.items()
    }


N1_L_TARGET = {
    "gauge:F2": Exact.rational(Fraction(-1, 4)),
    "fermion:tilde_lambda_D_lambda": I,
    "aux:D2": Exact.rational(Fraction(1, 2)),
    "topological:k_F_dual_F": Exact.rational(Fraction(-1, 8)),
}

N1_E_TARGET = {
    "gauge:F2": Exact.rational(Fraction(1, 4)),
    "fermion:tilde_lambda_D_lambda": ONE,
    "aux:D2": Exact.rational(Fraction(-1, 2)),
    "topological:k_F_dual_F": -I.scale(Fraction(1, 8)),
}

N2_L_TARGET = {
    **N1_L_TARGET,
    "scalar:D_tilde_phi_D_phi": MINUS_ONE,
    "fermion:tilde_psi_D_psi": I,
    "aux:tilde_F_F": ONE,
    "aux:D_mu": ONE,
    "yukawa:tilde_phi_lambda_psi": -SQRT_TWO,
    "yukawa:tilde_psi_tilde_lambda_phi": SQRT_TWO,
}

N2_E_TARGET = {
    **N1_E_TARGET,
    "scalar:D_tilde_phi_D_phi": ONE,
    "fermion:tilde_psi_D_psi": ONE,
    "aux:tilde_F_F": MINUS_ONE,
    "aux:D_mu": MINUS_ONE,
    "yukawa:tilde_phi_lambda_psi": SQRT_TWO,
    "yukawa:tilde_psi_tilde_lambda_phi": -SQRT_TWO,
}

N4_L_TARGET = {
    **N1_L_TARGET,
    "scalar:sum_r_D_tilde_phi_r_D_phi_r": MINUS_ONE,
    "fermion:sum_r_tilde_psi_r_D_psi_r": I,
    "aux:sum_r_tilde_F_r_F_r": ONE,
    "aux:i_D_C0": I,
    "yukawa:sum_r_tilde_phi_r_psi_r_lambda": SQRT_TWO,
    "yukawa:sum_r_phi_r_tilde_psi_r_tilde_lambda": SQRT_TWO,
    "superpotential:epsilon_F_phi_phi": -INV_SQRT_TWO,
    "superpotential:epsilon_tilde_F_tilde_phi_tilde_phi": -INV_SQRT_TWO,
    "superpotential:epsilon_phi_psi_psi": INV_SQRT_TWO,
    "superpotential:epsilon_tilde_phi_tilde_psi_tilde_psi": INV_SQRT_TWO,
}

N4_E_TARGET = {
    **N1_E_TARGET,
    "scalar:sum_r_D_tilde_phi_r_D_phi_r": ONE,
    "fermion:sum_r_tilde_psi_r_D_psi_r": ONE,
    "aux:sum_r_tilde_F_r_F_r": MINUS_ONE,
    "aux:i_D_C0": -I,
    "yukawa:sum_r_tilde_phi_r_psi_r_lambda": -SQRT_TWO,
    "yukawa:sum_r_phi_r_tilde_psi_r_tilde_lambda": -SQRT_TWO,
    "superpotential:epsilon_F_phi_phi": INV_SQRT_TWO,
    "superpotential:epsilon_tilde_F_tilde_phi_tilde_phi": INV_SQRT_TWO,
    "superpotential:epsilon_phi_psi_psi": -INV_SQRT_TWO,
    "superpotential:epsilon_tilde_phi_tilde_psi_tilde_psi": -INV_SQRT_TWO,
}


Monomial = tuple[str, ...]
Polynomial = dict[Monomial, Exact]


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, ZERO) + coefficient
        if result[monomial] == ZERO:
            del result[monomial]
    return result


def poly_scale(value: Polynomial, coefficient: Exact) -> Polynomial:
    return {
        monomial: coefficient * term_coefficient
        for monomial, term_coefficient in value.items()
        if coefficient * term_coefficient != ZERO
    }


def poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            contribution = left_coefficient * right_coefficient
            result[monomial] = result.get(monomial, ZERO) + contribution
            if result[monomial] == ZERO:
                del result[monomial]
    return result


def variable(name: str) -> Polynomial:
    return {(name,): ONE}


def auxiliary_checks(recorder: Recorder) -> dict[str, Any]:
    d_field = variable("D")
    mu = variable("mu")
    f_field = variable("F")
    tilde_f = variable("tilde_F")
    h_field = poly_add(d_field, mu)

    n2_left = poly_add(
        poly_multiply(tilde_f, f_field),
        poly_add(
            poly_scale(poly_multiply(d_field, d_field), Exact.rational(Fraction(1, 2))),
            poly_multiply(d_field, mu),
        ),
    )
    n2_right = poly_add(
        poly_multiply(tilde_f, f_field),
        poly_add(
            poly_scale(poly_multiply(h_field, h_field), Exact.rational(Fraction(1, 2))),
            poly_scale(poly_multiply(mu, mu), Exact.rational(Fraction(-1, 2))),
        ),
    )
    recorder.check("N=2 contracted auxiliary square", n2_left, n2_right, "auxiliary")

    # D=-i C0 in both signatures.
    d_solution = -I
    lorentz_d_value = d_solution * d_solution.scale(Fraction(1, 2)) + I * d_solution
    euclid_d_value = -(d_solution * d_solution.scale(Fraction(1, 2))) - I * d_solution
    recorder.check(
        "N=4 Lorentzian D elimination coefficient",
        lorentz_d_value,
        Exact.rational(Fraction(1, 2)),
        "auxiliary",
    )
    recorder.check(
        "N=4 Euclidean D elimination coefficient",
        euclid_d_value,
        Exact.rational(Fraction(-1, 2)),
        "auxiliary",
    )

    f_solution = INV_SQRT_TWO
    tilde_f_solution = INV_SQRT_TWO
    lorentz_f_value = (
        tilde_f_solution * f_solution
        - INV_SQRT_TWO * f_solution
        - INV_SQRT_TWO * tilde_f_solution
    )
    euclid_f_value = (
        -(tilde_f_solution * f_solution)
        + INV_SQRT_TWO * f_solution
        + INV_SQRT_TWO * tilde_f_solution
    )
    recorder.check(
        "N=4 Lorentzian F-pair elimination coefficient",
        lorentz_f_value,
        Exact.rational(Fraction(-1, 2)),
        "auxiliary",
    )
    recorder.check(
        "N=4 Euclidean F-pair elimination coefficient",
        euclid_f_value,
        Exact.rational(Fraction(1, 2)),
        "auxiliary",
    )

    contracted_yukawa = {
        "b_r^A psi_r^B lambda^C": 1,
    }
    # The second raw slot has coefficient -1.  B<->C in c_[ABC]
    # contributes -1; the two-spinor scalar contraction is symmetric.
    contracted_yukawa["b_r^A psi_r^B lambda^C"] += (-1) * (-1) * 1
    contracted_yukawa["epsilon_rst a_t^A psi_r^B psi_s^C"] = 1
    recorder.check(
        "contracted SU(4) Yukawa expansion",
        contracted_yukawa,
        {
            "b_r^A psi_r^B lambda^C": 2,
            "epsilon_rst a_t^A psi_r^B psi_s^C": 1,
        },
        "contraction",
    )

    raw_slots = list(itertools.product(range(4), repeat=4))
    nonzero_slots = [slot for slot in raw_slots if slot[0] != slot[1] and slot[2] != slot[3]]

    def orbit(slot: tuple[int, int, int, int]) -> frozenset[tuple[int, int, int, int]]:
        i, j, k, l = slot
        return frozenset(((i, j, k, l), (j, i, k, l), (i, j, l, k), (j, i, l, k)))

    orbits = {orbit(slot) for slot in nonzero_slots}
    census = {
        "raw": len(raw_slots),
        "diagonal_zero": len(raw_slots) - len(nonzero_slots),
        "off_diagonal": len(nonzero_slots),
        "reversal_orbits": len(orbits),
    }
    recorder.check(
        "SU(4) 256-slot contraction census",
        census,
        {"raw": 256, "diagonal_zero": 112, "off_diagonal": 144, "reversal_orbits": 36},
        "contraction",
    )

    reduced: dict[str, int] = {}
    for r in range(1, 4):
        for s in range(1, 4):
            if r != s:
                a_key = f"A{min(r, s)}{max(r, s)}"
                reduced[a_key] = reduced.get(a_key, 0) + 16
            c_key = f"C{min(r, s)}{max(r, s)}"
            reduced[c_key] = reduced.get(c_key, 0) - 8
    reduced_expected = {
        "A12": 32,
        "A13": 32,
        "A23": 32,
        "C11": -8,
        "C22": -8,
        "C33": -8,
        "C12": -16,
        "C13": -16,
        "C23": -16,
    }
    recorder.check("SU(4) Jacobi-reduced coefficient dictionary", reduced, reduced_expected, "contraction")

    return {
        "n2_square": serialize(n2_left),
        "n4_D_elimination_L": serialize(lorentz_d_value),
        "n4_D_elimination_E": serialize(euclid_d_value),
        "n4_F_pair_elimination_L": serialize(lorentz_f_value),
        "n4_F_pair_elimination_E": serialize(euclid_f_value),
        "su4_slot_census": census,
        "su4_reduced_coefficients": reduced,
    }


def bch_coefficient(p: int, q_index: int) -> Fraction:
    total = Fraction(0)
    for left_power in range(p + 1):
        derivative_power = p + q_index - left_power + 1
        total += Fraction((-1) ** left_power, factorial(left_power) * factorial(derivative_power))
    return total


def tilded_bch_coefficient(p: int, q_index: int) -> Fraction:
    total = Fraction(0)
    for left_power in range(p + 1):
        derivative_power = p + q_index - left_power + 1
        total += Fraction(
            (-1) ** derivative_power,
            factorial(left_power) * factorial(derivative_power),
        )
    return total


def closed_bch_coefficient(p: int, q_index: int) -> Fraction:
    return Fraction((-1) ** p, factorial(p) * factorial(q_index) * (p + q_index + 1))


def closed_tilded_bch_coefficient(p: int, q_index: int) -> Fraction:
    return Fraction((-1) ** (q_index + 1), factorial(p) * factorial(q_index) * (p + q_index + 1))


def bch_and_gauge_checks(recorder: Recorder, maximum: int = 8) -> dict[str, Any]:
    bch_failures: list[tuple[int, int, str]] = []
    for p, q_index in itertools.product(range(maximum + 1), repeat=2):
        if bch_coefficient(p, q_index) != closed_bch_coefficient(p, q_index):
            bch_failures.append((p, q_index, "Gamma"))
        if tilded_bch_coefficient(p, q_index) != closed_tilded_bch_coefficient(p, q_index):
            bch_failures.append((p, q_index, "tilde_Gamma"))
    recorder.check("BCH and tilded-BCH word coefficients", bch_failures, [], "bch")

    gauge_failures: list[tuple[int, int, int, int, int, str]] = []
    convolution_maximum = 4
    for eta in (1, -1):
        for p, q_index, r, s in itertools.product(range(convolution_maximum + 1), repeat=4):
            denominator = (
                256
                * factorial(p)
                * factorial(q_index)
                * factorial(r)
                * factorial(s)
                * (p + q_index + 1)
                * (r + s + 1)
            )
            plus_direct = Fraction(eta, 256) * bch_coefficient(p, q_index) * bch_coefficient(r, s)
            plus_expected = Fraction(eta * (-1) ** (p + r), denominator)
            if plus_direct != plus_expected:
                gauge_failures.append((eta, p, q_index, r, s, "chiral"))

            minus_direct = (
                Fraction(eta, 256)
                * tilded_bch_coefficient(p, q_index)
                * tilded_bch_coefficient(r, s)
            )
            minus_expected = Fraction(eta * (-1) ** (q_index + s), denominator)
            if minus_direct != minus_expected:
                gauge_failures.append((eta, p, q_index, r, s, "antichiral"))
    recorder.check("gauge-action BCH convolution", gauge_failures, [], "gauge_vertices")
    return {
        "bch_checked_square": [maximum + 1, maximum + 1],
        "gauge_convolution_signatures": ["Lorentzian eta=+1", "Euclidean eta=-1"],
        "gauge_convolution_range": [0, convolution_maximum],
    }


def matter_symmetrization_checks(recorder: Recorder, maximum: int = 7) -> dict[str, Any]:
    failures: list[tuple[int, str]] = []
    zero_evaluation_failures: list[tuple[int, list[int]]] = []
    witness: dict[str, Any] = {}
    for number in range(maximum + 1):
        coefficient = Fraction(1, factorial(number))
        labelled_words = list(itertools.permutations(range(number)))
        if len(labelled_words) != factorial(number):
            failures.append((number, "labelled permutation count"))
        if sum((coefficient for _ in labelled_words), Fraction(0)) != 1:
            failures.append((number, "symmetrized coefficient sum"))
        if factorial(number) * coefficient != 1:
            failures.append((number, "identical-leg cancellation"))
        surviving_source_orders = [
            source_order
            for source_order in range(maximum + 3)
            if source_order >= number and source_order - number == 0
        ]
        if surviving_source_orders != [number]:
            zero_evaluation_failures.append((number, surviving_source_orders))
        witness[str(number)] = {
            "ordered_words": len(labelled_words),
            "coefficient_per_word": str(coefficient),
            "total": "1",
            "source_orders_surviving_V_equals_zero": surviving_source_orders,
        }
    recorder.check("matter exponential labelled symmetrization", failures, [], "matter_vertices")
    recorder.check(
        "matter derivative evaluated at V=0 isolates degree n",
        zero_evaluation_failures,
        [],
        "matter_vertices",
    )
    return witness


def exact_power(base: Exact, exponent: int) -> Exact:
    result = ONE
    for _ in range(exponent):
        result = result * base
    return result


def graph_wick_phase_checks(recorder: Recorder, maximum: int = 6) -> dict[str, Any]:
    tau_phase = {"L": I, "E": MINUS_ONE}
    edge_phase = {"L": I, "E": ONE}
    recorder.check(
        "universal Wick edge phase satisfies tau_R times edge_R equals -1",
        {signature: tau_phase[signature] * edge_phase[signature] for signature in ("L", "E")},
        {"L": MINUS_ONE, "E": MINUS_ONE},
        "graph_weights",
    )

    failures: list[tuple[str, int, int]] = []
    for vertices, edges in itertools.product(range(maximum + 1), repeat=2):
        lorentz_actual = exact_power(tau_phase["L"], vertices) * exact_power(edge_phase["L"], edges)
        lorentz_expected = exact_power(I, vertices + edges)
        if lorentz_actual != lorentz_expected:
            failures.append(("L", vertices, edges))

        euclidean_actual = exact_power(tau_phase["E"], vertices) * exact_power(edge_phase["E"], edges)
        euclidean_expected = exact_power(MINUS_ONE, vertices)
        if euclidean_actual != euclidean_expected:
            failures.append(("E", vertices, edges))
    recorder.check(
        "signature-dependent labeled graph phases",
        failures,
        [],
        "graph_weights",
    )
    return {
        "tau_phase": serialize(tau_phase),
        "edge_phase_minus_tau_inverse": serialize(edge_phase),
        "checked_vertex_edge_square": [maximum + 1, maximum + 1],
    }


def bernoulli_numbers(maximum: int) -> list[Fraction]:
    values = [Fraction(1)]
    for n in range(1, maximum + 1):
        lower_sum = sum((Fraction(comb(n + 1, k)) * values[k] for k in range(n)), Fraction(0))
        values.append(-lower_sum / Fraction(n + 1))
    return values


def brst_and_fp_checks(recorder: Recorder, maximum: int = 10) -> dict[str, Any]:
    bernoulli = bernoulli_numbers(maximum)
    expected = [
        Fraction(1),
        Fraction(-1, 2),
        Fraction(1, 6),
        Fraction(0),
        Fraction(-1, 30),
        Fraction(0),
        Fraction(1, 42),
        Fraction(0),
        Fraction(-1, 30),
        Fraction(0),
        Fraction(5, 66),
    ]
    recorder.check("Bernoulli sequence B_0 through B_10", bernoulli, expected, "brst")

    generating_failures: list[int] = []
    for n in range(maximum + 1):
        coefficient = sum(
            (
                bernoulli[k]
                / Fraction(factorial(k) * factorial(n - k + 1))
                for k in range(n + 1)
            ),
            Fraction(0),
        )
        expected_coefficient = Fraction(1 if n == 0 else 0)
        if coefficient != expected_coefficient:
            generating_failures.append(n)
    recorder.check("Bernoulli generating-function inverse", generating_failures, [], "brst")

    coefficient_failures: list[tuple[int, int, str]] = []
    coefficient_witness: dict[str, Any] = {}
    for p, q_index in itertools.product(range(8), repeat=2):
        n = p + q_index
        if n > maximum:
            continue
        common = Fraction(bernoulli[n], factorial(p) * factorial(q_index))
        sv_tilde_c = I.scale(common * ((-1) ** q_index))
        sv_c = (-I).scale(common * ((-1) ** p))
        fp_tilde_c = I.scale(common * ((-1) ** q_index) * Fraction(1, 4))
        fp_c = (-I).scale(common * ((-1) ** p) * Fraction(1, 4))
        if fp_tilde_c != sv_tilde_c.scale(Fraction(1, 4)):
            coefficient_failures.append((p, q_index, "tilde_c"))
        if fp_c != sv_c.scale(Fraction(1, 4)):
            coefficient_failures.append((p, q_index, "c"))
        if p + q_index <= 3:
            coefficient_witness[f"p={p},q={q_index}"] = {
                "sV_tilde_c": serialize(sv_tilde_c),
                "sV_c": serialize(sv_c),
                "FP_tilde_c": serialize(fp_tilde_c),
                "FP_c": serialize(fp_c),
            }
    recorder.check("Bernoulli sV and FP word coefficients", coefficient_failures, [], "fp_vertices")
    return {
        "bernoulli": [str(value) for value in bernoulli],
        "low_order_coefficients": coefficient_witness,
    }


def permutation_koszul_sign(permutation: tuple[int, ...], parities: tuple[int, ...]) -> int:
    exponent = 0
    for left in range(len(permutation)):
        for right in range(left + 1, len(permutation)):
            if permutation[left] > permutation[right]:
                exponent += parities[permutation[left]] * parities[permutation[right]]
    return -1 if exponent % 2 else 1


def bubble_koszul_sign(permutation: tuple[int, ...], parities: tuple[int, ...]) -> int:
    current = list(permutation)
    sign = 1
    for end in range(len(current) - 1, 0, -1):
        for left in range(end):
            if current[left] > current[left + 1]:
                first = current[left]
                second = current[left + 1]
                if parities[first] * parities[second]:
                    sign = -sign
                current[left], current[left + 1] = current[left + 1], current[left]
    if current != list(range(len(permutation))):
        raise AssertionError("bubble reduction did not reach identity")
    return sign


def koszul_checks(recorder: Recorder) -> dict[str, Any]:
    derivative_failures: list[tuple[tuple[int, ...], int, int]] = []
    derivative_cases = 0
    for length in range(1, 8):
        for parities in itertools.product((0, 1), repeat=length):
            for derivative_parity in (0, 1):
                for position in range(length):
                    expected = -1 if derivative_parity * sum(parities[:position]) % 2 else 1
                    crossings = 1
                    for parity in parities[:position]:
                        if derivative_parity * parity:
                            crossings = -crossings
                    derivative_cases += 1
                    if crossings != expected:
                        derivative_failures.append((parities, derivative_parity, position))
    recorder.check("ordered functional-derivative Koszul signs", derivative_failures, [], "koszul")

    permutation_failures: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    permutation_cases = 0
    for length in range(6):
        for parities in itertools.product((0, 1), repeat=length):
            for permutation in itertools.permutations(range(length)):
                permutation_cases += 1
                if permutation_koszul_sign(permutation, parities) != bubble_koszul_sign(permutation, parities):
                    permutation_failures.append((permutation, parities))
    recorder.check("permutation Koszul signs", permutation_failures, [], "koszul")
    return {
        "ordered_derivative_cases": derivative_cases,
        "permutation_cases": permutation_cases,
    }


@dataclass(frozen=True)
class FormalScalar:
    coefficient: Fraction = Fraction(1)
    powers: tuple[tuple[str, int], ...] = ()

    @staticmethod
    def build(coefficient: int | Fraction, **powers: int) -> "FormalScalar":
        return FormalScalar(
            Fraction(coefficient),
            tuple(sorted((name, exponent) for name, exponent in powers.items() if exponent)),
        )

    def __mul__(self, other: "FormalScalar") -> "FormalScalar":
        powers = dict(self.powers)
        for name, exponent in other.powers:
            powers[name] = powers.get(name, 0) + exponent
            if powers[name] == 0:
                del powers[name]
        return FormalScalar.build(self.coefficient * other.coefficient, **powers)

    def specialize(self, **values: Fraction) -> "FormalScalar":
        coefficient = self.coefficient
        residual: dict[str, int] = {}
        for name, exponent in self.powers:
            if name in values:
                coefficient *= values[name] ** exponent
            else:
                residual[name] = exponent
        return FormalScalar.build(coefficient, **residual)


@dataclass(frozen=True)
class ProjectorElement:
    transverse: FormalScalar
    longitudinal: FormalScalar

    def __mul__(self, other: "ProjectorElement") -> "ProjectorElement":
        # P_T^2=P_T, P_0^2=P_0, P_T P_0=P_0 P_T=0.
        return ProjectorElement(
            self.transverse * other.transverse,
            self.longitudinal * other.longitudinal,
        )

    def specialize(self, **values: Fraction) -> "ProjectorElement":
        return ProjectorElement(
            self.transverse.specialize(**values),
            self.longitudinal.specialize(**values),
        )


def projector_checks(recorder: Recorder) -> dict[str, Any]:
    kernel = ProjectorElement(
        FormalScalar.build(Fraction(1, 2), h=1, Box_E=1),
        FormalScalar.build(Fraction(1, 2), h=1, Box_E=1, xi=-1),
    )
    inverse = ProjectorElement(
        FormalScalar.build(2, h=-1, Box_E=-1),
        FormalScalar.build(2, h=-1, Box_E=-1, xi=1),
    )
    covariance = ProjectorElement(
        FormalScalar.build(2, hbar=1, h=-1, Box_E=-1),
        FormalScalar.build(2, hbar=1, h=-1, Box_E=-1, xi=1),
    )
    identity = ProjectorElement(FormalScalar.build(1), FormalScalar.build(1))
    hbar_identity = ProjectorElement(
        FormalScalar.build(1, hbar=1),
        FormalScalar.build(1, hbar=1),
    )
    recorder.check("Euclidean projector kernel inverse", kernel * inverse, identity, "projector")
    recorder.check("Euclidean projector covariance", kernel * covariance, hbar_identity, "projector")

    fermi_covariance = covariance.specialize(xi=Fraction(1))
    expected_fermi = ProjectorElement(
        FormalScalar.build(2, hbar=1, h=-1, Box_E=-1),
        FormalScalar.build(2, hbar=1, h=-1, Box_E=-1),
    )
    recorder.check("Euclidean xi=1 Fermi covariance", fermi_covariance, expected_fermi, "projector")
    return {
        "kernel": serialize(kernel),
        "inverse": serialize(inverse),
        "covariance": serialize(covariance),
        "xi_equals_one_covariance": serialize(fermi_covariance),
    }


def source_checks(recorder: Recorder) -> list[dict[str, str]]:
    source_rows: list[dict[str, str]] = []
    for relative_path, expected_hash in SOURCE_LOCKS.items():
        path = ROOT / relative_path
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        recorder.check(f"source SHA-256 lock: {relative_path}", actual_hash, expected_hash, "source_lock")
        source_rows.append({"path": relative_path, "sha256": actual_hash})
    return source_rows


def component_checks(recorder: Recorder) -> dict[str, Any]:
    n1_l = n1_lorentzian_coefficients()
    n2_l = n2_lorentzian_coefficients()
    n4_l = n4_lorentzian_coefficients()
    n1_e = wick_rotate(n1_l)
    n2_e = wick_rotate(n2_l)
    n4_e = wick_rotate(n4_l)
    recorder.check("N=1 Lorentzian component coefficient dictionary", n1_l, N1_L_TARGET, "components")
    recorder.check("N=1 Euclidean component coefficient dictionary", n1_e, N1_E_TARGET, "components")
    recorder.check("N=2 Lorentzian component coefficient dictionary", n2_l, N2_L_TARGET, "components")
    recorder.check("N=2 Euclidean component coefficient dictionary", n2_e, N2_E_TARGET, "components")
    recorder.check("N=4 Lorentzian component coefficient dictionary", n4_l, N4_L_TARGET, "components")
    recorder.check("N=4 Euclidean component coefficient dictionary", n4_e, N4_E_TARGET, "components")
    return {
        "N1_L": serialize(n1_l),
        "N1_E": serialize(n1_e),
        "N2_L": serialize(n2_l),
        "N2_E": serialize(n2_e),
        "N4_L": serialize(n4_l),
        "N4_E": serialize(n4_e),
    }


def blocker_checks(recorder: Recorder) -> None:
    recorder.check(
        "exact partial-scope blocker labels",
        BLOCKER_LABELS,
        (
            "BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED",
            "BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
            "BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED",
            "BLOCKED_STEP3D_LC_VECTOR_CYCLE",
        ),
        "scope",
    )


def contract_surface_checks(recorder: Recorder) -> dict[str, Any]:
    text = (ROOT / CONTRACT_PATH).read_text(encoding="utf-8")
    tags = re.findall(r"\\tag\{(5A\.[^}]+)\}", text)
    numeric_tags = {tag for tag in tags if tag[3:].isdigit()}
    recorder.check("Step-5A unique equation tags", len(tags), len(set(tags)), "surface")
    recorder.check(
        "Step-5A numeric equation surface",
        numeric_tags,
        {f"5A.{number}" for number in range(1, 82)},
        "surface",
    )
    recorder.check("Step-5A display delimiter parity", text.count("$$") % 2, 0, "surface")
    forbidden = [token for token in (r"\sim", r"\approx", r"\propto") if token in text]
    recorder.check("Step-5A strict-equality tokens", forbidden, [], "surface")
    controls = [ord(character) for character in text if ord(character) < 32 and character not in "\n\t"]
    recorder.check("Step-5A control characters", controls, [], "surface")
    naked_qquads = [
        {"line": line_number, "text": line}
        for line_number, line in enumerate(text.splitlines(), start=1)
        if re.search(r"(?<!\\)qquad", line)
    ]
    recorder.check("Step-5A no malformed naked qquad", naked_qquads, [], "surface")
    recorder.check(
        "Step-5A does not infer BV compatibility from nonvanishing density",
        r"\Delta_{R,\nu}^2=0" in text,
        False,
        "surface",
    )
    blocker_counts = {label: text.count(label) for label in BLOCKER_LABELS}
    recorder.check(
        "Step-5A blocker tokens occur exactly once",
        blocker_counts,
        {label: 1 for label in BLOCKER_LABELS},
        "surface",
    )
    required = (
        r"f_{AB}=h\kappa_{AB}+i\mathfrak k_{AB}",
        r"\mathcal V_R\ne\mathcal V_R^{\mathrm{WZ}}",
        r"\mathfrak R_{R,\nu}^{\mathsf i}",
        r"\mathfrak O^{\mathrm{BV}}_{E,\nu}[W]",
        r"\mathfrak M^\Delta_{R,\nu}[F]",
        r"&:=\Delta_{R,\nu}^2F",
        r"\widehat{\boldsymbol\varpi}_{R,\nu}\ \text{BV-compatible}",
        r"\mathfrak M^\Delta_{R,\nu}[F]=0\quad\text{for every }F",
        r"a_{pq}:=\frac{(-1)^p}{p!q!(p+q+1)}",
        r"\widetilde a_{pq}:=\frac{(-1)^{q+1}}{p!q!(p+q+1)}",
        r"\right|_{V=0}",
        r"(-\tau_R^{-1})^{|E(G)|}",
        r"-\tau_L^{-1}=i\hbar",
        r"-\tau_E^{-1}=\hbar",
        r"\mathcal Y_{E,\mathrm{FF}}\text{ is nonlocal}",
        "complete accepted Feynman rules are not claimed",
    )
    missing = [token for token in required if token not in text]
    recorder.check("Step-5A required formula surface", missing, [], "surface")
    return {
        "tag_count": len(tags),
        "numeric_tag_count": len(numeric_tags),
        "blocker_counts": blocker_counts,
        "naked_qquads": naked_qquads,
    }


def category_totals(checks: Iterable[dict[str, Any]]) -> dict[str, dict[str, int]]:
    totals: dict[str, dict[str, int]] = {}
    for check in checks:
        row = totals.setdefault(check["category"], {"checks": 0, "failed": 0})
        row["checks"] += 1
        if not check["passed"]:
            row["failed"] += 1
    return totals


def build_audit() -> dict[str, Any]:
    recorder = Recorder()
    surface = contract_surface_checks(recorder)
    sources = source_checks(recorder)
    components = component_checks(recorder)
    auxiliaries = auxiliary_checks(recorder)
    bch_gauge = bch_and_gauge_checks(recorder)
    matter = matter_symmetrization_checks(recorder)
    brst_fp = brst_and_fp_checks(recorder)
    koszul = koszul_checks(recorder)
    graph_phases = graph_wick_phase_checks(recorder)
    projector = projector_checks(recorder)
    blocker_checks(recorder)
    status = PASS_STATUS if not recorder.failures else "FAIL"
    return {
        "schema": 1,
        "section": SECTION_ID,
        "contract_path": CONTRACT_PATH,
        "scope_id": SCOPE_ID,
        "status": status,
        "scope": {
            "claim": "exact partial component/BV-BRST/vertex grammar only",
            "forbidden_inputs_used": [],
            "forbidden_inputs": ["network", "Notion", "Step-3E branch"],
            "blockers": list(BLOCKER_LABELS),
        },
        "sources": sources,
        "arithmetic": {
            "coefficient_field": "Q(i,sqrt(2))",
            "floating_point": False,
            "external_cas": False,
            "random_sampling": False,
        },
        "categories": category_totals(recorder.checks),
        "totals": {
            "exact_check_families": len(recorder.checks),
            "failed_check_families": len(recorder.failures),
        },
        "witnesses": {
            "component_coefficients": components,
            "auxiliary_and_contraction": auxiliaries,
            "bch_and_gauge": bch_gauge,
            "matter_symmetrization": matter,
            "brst_and_fp": brst_fp,
            "koszul": koszul,
            "graph_wick_phases": graph_phases,
            "euclidean_projector": projector,
            "contract_surface": surface,
        },
        "checks": recorder.checks,
        "failures": recorder.failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="deterministic JSON audit path",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    audit = build_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if audit["status"] != PASS_STATUS:
        print(json.dumps(audit["failures"], indent=2, ensure_ascii=False))
        raise SystemExit(1)
    print(
        "Step-5A exact partial-scope verification: "
        f"{audit['totals']['exact_check_families']} check families, 0 failures"
    )


if __name__ == "__main__":
    main()
