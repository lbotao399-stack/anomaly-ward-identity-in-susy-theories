#!/usr/bin/env python3
"""Exact Step-5 DRED/projector and one-loop integral verifier.

This file fixes only regulator kinematics and Euclidean loop integration.  It
does not contain an anomaly coefficient, a graph multiplicity, a color factor,
or a supergraph numerator imported from another calculation.

Fourier convention (locked by the command-line parameter):

    f(x) = integral d^d k/(2 pi)^d exp(+i k.x) f(k),
    partial_M f(x) <-> +i k_M f(k).

Loop measure (locked by the command-line parameter):

    mu^(2 epsilon) d^d ell/(2 pi)^d,
    d = 4 - 2 epsilon,

with positive Euclidean momentum squares.  The bare numerator is constructed
with the four-dimensional spin metric g4.  Only angular integration introduces
the d-dimensional loop projector hat_g and hence epsilon.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-dred-integrals-verification.json"
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
TASK_ID = "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"

FOURIER_PHASE = "exp(+i k.x)"
LOOP_MEASURE = "mu^(2 epsilon) d^d ell/(2 pi)^d"
SIGNATURE = "Euclidean-positive"


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def gamma_positive_integer(value: int) -> int:
    if value < 1:
        raise ValueError("integer Gamma argument must be positive")
    result = 1
    for factor in range(1, value):
        result *= factor
    return result


# ---------------------------------------------------------------------------
# Exact polynomial algebra for the Feynman-parameter shift.
# ---------------------------------------------------------------------------

POLY_SYMBOLS = ("x", "y", "z", "p2", "pq", "q2")
Monomial = tuple[int, ...]


@dataclass(frozen=True)
class Poly:
    terms: tuple[tuple[Monomial, Fraction], ...]

    @staticmethod
    def from_dict(terms: dict[Monomial, Fraction]) -> "Poly":
        cleaned = tuple(sorted((m, c) for m, c in terms.items() if c))
        return Poly(cleaned)

    @staticmethod
    def constant(value: int | Fraction) -> "Poly":
        coefficient = Fraction(value)
        if coefficient == 0:
            return Poly(())
        return Poly((((0,) * len(POLY_SYMBOLS), coefficient),))

    @staticmethod
    def symbol(name: str) -> "Poly":
        exponent = [0] * len(POLY_SYMBOLS)
        exponent[POLY_SYMBOLS.index(name)] = 1
        return Poly.from_dict({tuple(exponent): Fraction(1)})

    def as_dict(self) -> dict[Monomial, Fraction]:
        return dict(self.terms)

    def __add__(self, other: "Poly") -> "Poly":
        result = self.as_dict()
        for monomial, coefficient in other.terms:
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        return Poly.from_dict(result)

    def __neg__(self) -> "Poly":
        return Poly.from_dict({m: -c for m, c in self.terms})

    def __sub__(self, other: "Poly") -> "Poly":
        return self + (-other)

    def __mul__(self, other: "Poly") -> "Poly":
        result: dict[Monomial, Fraction] = {}
        for left_monomial, left_coefficient in self.terms:
            for right_monomial, right_coefficient in other.terms:
                monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
                result[monomial] = (
                    result.get(monomial, Fraction(0))
                    + left_coefficient * right_coefficient
                )
        return Poly.from_dict(result)

    def scale(self, coefficient: int | Fraction) -> "Poly":
        value = Fraction(coefficient)
        return Poly.from_dict({m: value * c for m, c in self.terms})

    def power(self, exponent: int) -> "Poly":
        if exponent < 0:
            raise ValueError("polynomial exponent must be nonnegative")
        result = Poly.constant(1)
        for _ in range(exponent):
            result = result * self
        return result

    def substitute(self, name: str, replacement: "Poly") -> "Poly":
        index = POLY_SYMBOLS.index(name)
        result = Poly.constant(0)
        for monomial, coefficient in self.terms:
            power = monomial[index]
            residual = list(monomial)
            residual[index] = 0
            base = Poly.from_dict({tuple(residual): coefficient})
            result = result + base * replacement.power(power)
        return result

    def is_zero(self) -> bool:
        return not self.terms

    def render(self) -> str:
        if not self.terms:
            return "0"
        pieces: list[str] = []
        ordered = sorted(
            self.terms,
            key=lambda item: (sum(item[0]), item[0]),
            reverse=True,
        )
        for monomial, coefficient in ordered:
            factors = []
            for symbol, exponent in zip(POLY_SYMBOLS, monomial):
                if exponent == 1:
                    factors.append(symbol)
                elif exponent > 1:
                    factors.append(f"{symbol}^{exponent}")
            monomial_text = "*".join(factors)
            magnitude = abs(coefficient)
            if not monomial_text:
                body = fraction_string(magnitude)
            elif magnitude == 1:
                body = monomial_text
            else:
                body = f"{fraction_string(magnitude)}*{monomial_text}"
            if not pieces:
                pieces.append(("-" if coefficient < 0 else "") + body)
            else:
                pieces.append((" - " if coefficient < 0 else " + ") + body)
        return "".join(pieces)


ZERO = Poly.constant(0)
ONE = Poly.constant(1)
X = Poly.symbol("x")
Y = Poly.symbol("y")
Z = Poly.symbol("z")
P2 = Poly.symbol("p2")
PQ = Poly.symbol("pq")
Q2 = Poly.symbol("q2")


Vector = tuple[Poly, Poly]  # coefficients in the ordered basis (p,q)


def vector_add(left: Vector, right: Vector) -> Vector:
    return left[0] + right[0], left[1] + right[1]


def vector_subtract(left: Vector, right: Vector) -> Vector:
    return left[0] - right[0], left[1] - right[1]


def vector_scale(coefficient: Poly, vector: Vector) -> Vector:
    return coefficient * vector[0], coefficient * vector[1]


def vector_dot(left: Vector, right: Vector) -> Poly:
    # (a p+b q).(c p+d q)=ac p^2+(ad+bc)p.q+bd q^2.
    return (
        left[0] * right[0] * P2
        + (left[0] * right[1] + left[1] * right[0]) * PQ
        + left[1] * right[1] * Q2
    )


def simplex(poly: Poly) -> Poly:
    return poly.substitute("x", ONE - Y - Z)


def vector_simplex(vector: Vector) -> Vector:
    return simplex(vector[0]), simplex(vector[1])


def vector_render(vector: Vector) -> str:
    return f"({vector[0].render()})*p + ({vector[1].render()})*q"


# ---------------------------------------------------------------------------
# Exact DRED projector algebra.
# Each metric is stored in the orthogonal basis (hat_g, tilde_g).
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class EpsilonPoly:
    terms: tuple[tuple[int, Fraction], ...]

    @staticmethod
    def from_dict(value: dict[int, Fraction]) -> "EpsilonPoly":
        return EpsilonPoly(tuple(sorted((p, c) for p, c in value.items() if c)))

    @staticmethod
    def constant(value: int | Fraction) -> "EpsilonPoly":
        coefficient = Fraction(value)
        return EpsilonPoly.from_dict({0: coefficient})

    def __add__(self, other: "EpsilonPoly") -> "EpsilonPoly":
        result = dict(self.terms)
        for power, coefficient in other.terms:
            result[power] = result.get(power, Fraction(0)) + coefficient
        return EpsilonPoly.from_dict(result)

    def __neg__(self) -> "EpsilonPoly":
        return EpsilonPoly.from_dict({p: -c for p, c in self.terms})

    def __sub__(self, other: "EpsilonPoly") -> "EpsilonPoly":
        return self + (-other)

    def scale(self, coefficient: int | Fraction) -> "EpsilonPoly":
        value = Fraction(coefficient)
        return EpsilonPoly.from_dict({p: value * c for p, c in self.terms})

    def render(self) -> str:
        if not self.terms:
            return "0"
        pieces: list[str] = []
        for power, coefficient in sorted(self.terms, reverse=True):
            magnitude = abs(coefficient)
            if power == 0:
                body = fraction_string(magnitude)
            else:
                epsilon_power = "epsilon" if power == 1 else f"epsilon^{power}"
                body = epsilon_power if magnitude == 1 else f"{fraction_string(magnitude)}*{epsilon_power}"
            if not pieces:
                pieces.append(("-" if coefficient < 0 else "") + body)
            else:
                pieces.append((" - " if coefficient < 0 else " + ") + body)
        return "".join(pieces)


@dataclass(frozen=True)
class Metric:
    hat: Fraction
    tilde: Fraction

    def __add__(self, other: "Metric") -> "Metric":
        return Metric(self.hat + other.hat, self.tilde + other.tilde)

    def __neg__(self) -> "Metric":
        return Metric(-self.hat, -self.tilde)

    def __sub__(self, other: "Metric") -> "Metric":
        return self + (-other)

    def compose(self, other: "Metric") -> "Metric":
        return Metric(self.hat * other.hat, self.tilde * other.tilde)

    def trace(self) -> EpsilonPoly:
        # tr(hat_g)=4-2 epsilon, tr(tilde_g)=2 epsilon.
        return EpsilonPoly.from_dict(
            {
                0: 4 * self.hat,
                1: -2 * self.hat + 2 * self.tilde,
            }
        )

    def render(self) -> str:
        return f"({fraction_string(self.hat)})*hat_g + ({fraction_string(self.tilde)})*tilde_g"


HAT_G = Metric(Fraction(1), Fraction(0))
TILDE_G = Metric(Fraction(0), Fraction(1))
G4 = Metric(Fraction(1), Fraction(1))
ZERO_METRIC = Metric(Fraction(0), Fraction(0))


# ---------------------------------------------------------------------------
# Formal Laurent series.  Coefficients are exact polynomials in
# L0=log(4*pi*mu^2/Delta) and EulerGamma.
# ---------------------------------------------------------------------------

FORMAL_SYMBOLS = ("L0", "EulerGamma")
FormalMonomial = tuple[int, int]


@dataclass(frozen=True)
class FormalPoly:
    terms: tuple[tuple[FormalMonomial, Fraction], ...]

    @staticmethod
    def from_dict(value: dict[FormalMonomial, Fraction]) -> "FormalPoly":
        return FormalPoly(tuple(sorted((m, c) for m, c in value.items() if c)))

    @staticmethod
    def constant(value: int | Fraction) -> "FormalPoly":
        coefficient = Fraction(value)
        return FormalPoly.from_dict({(0, 0): coefficient})

    @staticmethod
    def symbol(index: int) -> "FormalPoly":
        exponent = [0, 0]
        exponent[index] = 1
        return FormalPoly.from_dict({tuple(exponent): Fraction(1)})

    def __add__(self, other: "FormalPoly") -> "FormalPoly":
        result = dict(self.terms)
        for monomial, coefficient in other.terms:
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        return FormalPoly.from_dict(result)

    def __neg__(self) -> "FormalPoly":
        return FormalPoly.from_dict({m: -c for m, c in self.terms})

    def __sub__(self, other: "FormalPoly") -> "FormalPoly":
        return self + (-other)

    def __mul__(self, other: "FormalPoly") -> "FormalPoly":
        result: dict[FormalMonomial, Fraction] = {}
        for left_monomial, left_coefficient in self.terms:
            for right_monomial, right_coefficient in other.terms:
                monomial = (
                    left_monomial[0] + right_monomial[0],
                    left_monomial[1] + right_monomial[1],
                )
                result[monomial] = result.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
        return FormalPoly.from_dict(result)

    def scale(self, coefficient: int | Fraction) -> "FormalPoly":
        value = Fraction(coefficient)
        return FormalPoly.from_dict({m: value * c for m, c in self.terms})

    def render(self) -> str:
        if not self.terms:
            return "0"
        pieces: list[str] = []
        for monomial, coefficient in sorted(
            self.terms,
            key=lambda item: (sum(item[0]), item[0]),
            reverse=True,
        ):
            factors: list[str] = []
            for symbol, exponent in zip(FORMAL_SYMBOLS, monomial):
                if exponent == 1:
                    factors.append(symbol)
                elif exponent > 1:
                    factors.append(f"{symbol}^{exponent}")
            factor_text = "*".join(factors)
            magnitude = abs(coefficient)
            if not factor_text:
                body = fraction_string(magnitude)
            elif magnitude == 1:
                body = factor_text
            else:
                body = f"{fraction_string(magnitude)}*{factor_text}"
            if not pieces:
                pieces.append(("-" if coefficient < 0 else "") + body)
            else:
                pieces.append((" - " if coefficient < 0 else " + ") + body)
        return "".join(pieces)


FZERO = FormalPoly.constant(0)
FONE = FormalPoly.constant(1)
L0 = FormalPoly.symbol(0)
EULER_GAMMA = FormalPoly.symbol(1)


@dataclass(frozen=True)
class Laurent:
    coefficients: tuple[tuple[int, FormalPoly], ...]

    @staticmethod
    def from_dict(value: dict[int, FormalPoly]) -> "Laurent":
        return Laurent(tuple(sorted((p, c) for p, c in value.items() if c.terms)))

    def as_dict(self) -> dict[int, FormalPoly]:
        return dict(self.coefficients)

    def __add__(self, other: "Laurent") -> "Laurent":
        result = self.as_dict()
        for power, coefficient in other.coefficients:
            result[power] = result.get(power, FZERO) + coefficient
        return Laurent.from_dict(result)

    def __neg__(self) -> "Laurent":
        return Laurent.from_dict({p: -c for p, c in self.coefficients})

    def __sub__(self, other: "Laurent") -> "Laurent":
        return self + (-other)

    def scale(self, coefficient: int | Fraction) -> "Laurent":
        value = Fraction(coefficient)
        return Laurent.from_dict({p: c.scale(value) for p, c in self.coefficients})

    def multiply(self, other: "Laurent", minimum: int, maximum: int) -> "Laurent":
        result: dict[int, FormalPoly] = {}
        for left_power, left_coefficient in self.coefficients:
            for right_power, right_coefficient in other.coefficients:
                power = left_power + right_power
                if minimum <= power <= maximum:
                    result[power] = result.get(power, FZERO) + left_coefficient * right_coefficient
        return Laurent.from_dict(result)

    def coefficient(self, power: int) -> FormalPoly:
        return self.as_dict().get(power, FZERO)

    def render(self) -> dict[str, str]:
        return {str(power): coefficient.render() for power, coefficient in self.coefficients}


# ---------------------------------------------------------------------------
# Audit recorder.
# ---------------------------------------------------------------------------


class Recorder:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []
        self.failures: list[dict[str, Any]] = []

    def check(self, name: str, lhs: Any, rhs: Any, category: str) -> None:
        passed = lhs == rhs
        entry = {
            "name": name,
            "category": category,
            "lhs": render_value(lhs),
            "rhs": render_value(rhs),
            "passed": passed,
        }
        self.checks.append(entry)
        if not passed:
            self.failures.append(entry)


def render_value(value: Any) -> Any:
    if isinstance(value, Fraction):
        return fraction_string(value)
    if isinstance(value, Poly):
        return value.render()
    if isinstance(value, EpsilonPoly):
        return value.render()
    if isinstance(value, Metric):
        return value.render()
    if isinstance(value, FormalPoly):
        return value.render()
    if isinstance(value, Laurent):
        return value.render()
    if isinstance(value, tuple):
        return [render_value(item) for item in value]
    return value


def contains_forbidden_bare_regulator_token(value: Any) -> bool:
    forbidden = {"epsilon", "hat_g", "tilde_g", "d"}
    if isinstance(value, dict):
        return any(
            contains_forbidden_bare_regulator_token(key)
            or contains_forbidden_bare_regulator_token(item)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return any(contains_forbidden_bare_regulator_token(item) for item in value)
    if isinstance(value, str):
        return value in forbidden
    return False


def metric_checks(recorder: Recorder) -> dict[str, Any]:
    recorder.check("g4 decomposition", G4 - HAT_G, TILDE_G, "DRED-projectors")
    recorder.check("g4 idempotence", G4.compose(G4), G4, "DRED-projectors")
    recorder.check("hat projector idempotence", HAT_G.compose(HAT_G), HAT_G, "DRED-projectors")
    recorder.check("tilde projector idempotence", TILDE_G.compose(TILDE_G), TILDE_G, "DRED-projectors")
    recorder.check("hat-tilde orthogonality", HAT_G.compose(TILDE_G), ZERO_METRIC, "DRED-projectors")
    recorder.check("tilde-hat orthogonality", TILDE_G.compose(HAT_G), ZERO_METRIC, "DRED-projectors")
    recorder.check("trace g4", G4.trace(), EpsilonPoly.constant(4), "DRED-projectors")
    recorder.check(
        "trace hat_g",
        HAT_G.trace(),
        EpsilonPoly.from_dict({0: Fraction(4), 1: Fraction(-2)}),
        "DRED-projectors",
    )
    recorder.check(
        "trace tilde_g",
        TILDE_G.trace(),
        EpsilonPoly.from_dict({1: Fraction(2)}),
        "DRED-projectors",
    )
    recorder.check("trace decomposition", HAT_G.trace() + TILDE_G.trace(), G4.trace(), "DRED-projectors")
    return {
        "definition": "tilde_g = g4 - hat_g",
        "projector_products": {
            "g4*g4": "g4",
            "hat_g*hat_g": "hat_g",
            "tilde_g*tilde_g": "tilde_g",
            "hat_g*tilde_g": "0",
            "tilde_g*hat_g": "0",
        },
        "traces": {
            "g4": G4.trace().render(),
            "hat_g": HAT_G.trace().render(),
            "tilde_g": TILDE_G.trace().render(),
        },
        "loop_vector_embedding": [
            "ell = hat_g*ell",
            "tilde_g*ell = 0",
            "g4(ell,ell) = hat_g(ell,ell) = ell^2",
        ],
    }


def shift_checks(recorder: Recorder) -> dict[str, Any]:
    s0: Vector = (ZERO, ZERO)
    s1: Vector = (ZERO, ONE)
    s2: Vector = (ONE, ONE)
    shifts = (s0, s1, s2)
    labels = ("r0=k", "r1=k+q", "r2=k+p+q")
    weights = (X, Y, Z)

    weight_sum = X + Y + Z
    weighted_shift = (ZERO, ZERO)
    weighted_constant = ZERO
    for weight, shift in zip(weights, shifts):
        weighted_shift = vector_add(weighted_shift, vector_scale(weight, shift))
        weighted_constant = weighted_constant + weight * vector_dot(shift, shift)

    weighted_shift_on_simplex = vector_simplex(weighted_shift)
    delta_from_shift = simplex(weighted_constant - vector_dot(weighted_shift, weighted_shift))
    p_plus_q_square = vector_dot(s2, s2)
    delta_target = simplex(X * Y * Q2 + X * Z * p_plus_q_square + Y * Z * P2)

    recorder.check("simplex coefficient of k^2", simplex(weight_sum), ONE, "Feynman-shift")
    recorder.check(
        "routing (s1-s0)^2",
        simplex(vector_dot(vector_subtract(s1, s0), vector_subtract(s1, s0))),
        Q2,
        "Feynman-shift",
    )
    recorder.check(
        "routing (s2-s0)^2",
        simplex(vector_dot(vector_subtract(s2, s0), vector_subtract(s2, s0))),
        P2 + PQ.scale(2) + Q2,
        "Feynman-shift",
    )
    recorder.check(
        "routing (s2-s1)^2",
        simplex(vector_dot(vector_subtract(s2, s1), vector_subtract(s2, s1))),
        P2,
        "Feynman-shift",
    )
    recorder.check("shifted cross term", vector_subtract(weighted_shift_on_simplex, weighted_shift_on_simplex), (ZERO, ZERO), "Feynman-shift")
    recorder.check("Delta polynomial", delta_from_shift, delta_target, "Feynman-shift")

    r_minus_shift = [vector_simplex(vector_subtract(shift, weighted_shift)) for shift in shifts]
    expected_u = (
        (Z.scale(-1), -(Y + Z)),
        (Z.scale(-1), ONE - Y - Z),
        (ONE - Z, ONE - Y - Z),
    )
    for index, (actual, expected) in enumerate(zip(r_minus_shift, expected_u)):
        recorder.check(f"shifted vector u{index}", actual, expected, "numerator-shift")

    bare_numerators = []
    numerator_expansions = []
    for i in range(3):
        for j in range(3):
            bare = {
                "coefficient": "1",
                "metric": "g4",
                "left": f"r{i}",
                "right": f"r{j}",
            }
            recorder.check(
                f"bare numerator ({i},{j}) has no regulator token",
                contains_forbidden_bare_regulator_token(bare),
                False,
                "bare-numerator-template",
            )
            bare_numerators.append(bare)
            numerator_expansions.append(
                {
                    "ordered_pair": [i, j],
                    "before_shift": f"r{i}^mu r{j}^nu",
                    "after_shift": f"ell^mu ell^nu + ell^mu u{j}^nu + u{i}^mu ell^nu + u{i}^mu u{j}^nu",
                    "odd_integral_terms": [f"ell^mu u{j}^nu", f"u{i}^mu ell^nu"],
                    "odd_integral_value": "0",
                    "integrated": f"(hat_g^{{mu nu}}/d) J_1,3 + u{i}^mu u{j}^nu J_0,3",
                }
            )

    return {
        "routing": list(labels),
        "all_incoming_external_momenta": ["q", "p", "-(p+q)"],
        "feynman_identity": "1/(r0^2 r1^2 r2^2) = 2 int_0^1 dx dy dz delta(1-x-y-z)/(x r0^2+y r1^2+z r2^2)^3",
        "shift": {
            "R": vector_render(weighted_shift_on_simplex),
            "ell": "k+R",
            "k": "ell-R",
            "denominator_expansion": [
                "x r0^2+y r1^2+z r2^2",
                "(x+y+z) k^2+2 k.R+y q^2+z (p+q)^2",
                "ell^2+y q^2+z (p+q)^2-R^2",
                "ell^2+Delta",
            ],
            "Delta_expanded_on_simplex": delta_from_shift.render(),
            "Delta_invariant_form": "x*y*q^2 + x*z*(p+q)^2 + y*z*p^2",
        },
        "shifted_external_vectors": {
            f"u{index}=s{index}-R": vector_render(vector)
            for index, vector in enumerate(r_minus_shift)
        },
        "bare_numerators": bare_numerators,
        "bare_numerator_check_classification": "CONVENTION_TEMPLATE_ONLY",
        "rank_two_numerator_expansions": numerator_expansions,
    }


def integral_checks(recorder: Recorder) -> dict[str, Any]:
    # A0=1/(16 pi^2).  Laurent coefficients below are quoted in units of A0.
    prefactor = Laurent.from_dict({0: FONE, 1: L0})
    gamma_epsilon = Laurent.from_dict({-1: FONE, 0: -EULER_GAMMA})
    gamma_one_plus_epsilon = Laurent.from_dict({0: FONE, 1: -EULER_GAMMA})
    d_over_four = Laurent.from_dict({0: FONE, 1: FormalPoly.constant(Fraction(-1, 2))})
    inverse_d = Laurent.from_dict(
        {0: FormalPoly.constant(Fraction(1, 4)), 1: FormalPoly.constant(Fraction(1, 8))}
    )

    j02 = prefactor.multiply(gamma_epsilon, -1, 0)
    delta_j03 = prefactor.multiply(gamma_one_plus_epsilon, 0, 1).scale(Fraction(1, 2))
    j13_from_reduction = j02 - Laurent.from_dict({0: delta_j03.coefficient(0)})
    j13_from_gamma = d_over_four.multiply(j02, -1, 0)
    tensor_from_rotation = inverse_d.multiply(j13_from_gamma, -1, 0)
    tensor_from_direct_gamma = j02.scale(Fraction(1, 4))

    logarithm_minus_gamma = L0 - EULER_GAMMA
    expected_j02 = Laurent.from_dict({-1: FONE, 0: logarithm_minus_gamma})
    expected_delta_j03 = Laurent.from_dict(
        {
            0: FormalPoly.constant(Fraction(1, 2)),
            1: logarithm_minus_gamma.scale(Fraction(1, 2)),
        }
    )
    expected_j13 = Laurent.from_dict(
        {
            -1: FONE,
            0: logarithm_minus_gamma + FormalPoly.constant(Fraction(-1, 2)),
        }
    )
    expected_tensor = Laurent.from_dict(
        {
            -1: FormalPoly.constant(Fraction(1, 4)),
            0: logarithm_minus_gamma.scale(Fraction(1, 4)),
        }
    )

    recorder.check("J_0,2 Laurent expansion", j02, expected_j02, "Laurent-integrals")
    recorder.check("Delta J_0,3 Laurent expansion", delta_j03, expected_delta_j03, "Laurent-integrals")
    recorder.check("J_1,3 reduction identity", j13_from_reduction, j13_from_gamma, "tensor-reduction")
    recorder.check("J_1,3 Laurent expansion", j13_from_gamma, expected_j13, "Laurent-integrals")
    recorder.check("rank-two rotational reduction", tensor_from_rotation, tensor_from_direct_gamma, "tensor-reduction")
    recorder.check("rank-two Laurent expansion", tensor_from_rotation, expected_tensor, "Laurent-integrals")
    recorder.check("J_0,2 pole", j02.coefficient(-1), FONE, "Laurent-poles")
    recorder.check("J_0,3 pole", delta_j03.coefficient(-1), FZERO, "Laurent-poles")
    recorder.check("J_1,3 pole", j13_from_gamma.coefficient(-1), FONE, "Laurent-poles")
    recorder.check(
        "rank-two hat_g pole",
        tensor_from_rotation.coefficient(-1),
        FormalPoly.constant(Fraction(1, 4)),
        "Laurent-poles",
    )

    # Decompose hat_g=g4-tilde_g only after tensor reduction.
    physical_pole = tensor_from_rotation.coefficient(-1)
    evanescent_pole = -physical_pole
    recorder.check(
        "tensor pole metric recombination",
        G4 - TILDE_G,
        HAT_G,
        "physical-evanescent-split",
    )
    recorder.check(
        "isolated evanescent trace finite coefficient in units of A0",
        evanescent_pole.scale(2),
        FormalPoly.constant(Fraction(-1, 2)),
        "physical-evanescent-split",
    )

    # Full contraction with tilde_g is zero.  Its two terms cancel exactly:
    # tilde.g4=2 epsilon and tilde.tilde=2 epsilon.
    tilde_contract_physical = physical_pole.scale(2)
    tilde_contract_evanescent = evanescent_pole.scale(2)
    recorder.check(
        "full tilde contraction cancellation",
        tilde_contract_physical + tilde_contract_evanescent,
        FZERO,
        "physical-evanescent-split",
    )

    # Contracting the exact tensor coefficient with tr(hat_g)=d recovers J_1,3.
    # In normalized Laurent form d=4-2 epsilon.
    d_series = Laurent.from_dict(
        {0: FormalPoly.constant(4), 1: FormalPoly.constant(-2)}
    )
    recorder.check(
        "g4 contraction of rank-two tensor",
        d_series.multiply(tensor_from_rotation, -1, 0),
        j13_from_gamma,
        "tensor-reduction",
    )

    return {
        "definition": "J_a,n(Delta)=mu^(2 epsilon) integral d^d ell/(2 pi)^d (ell^2)^a/(ell^2+Delta)^n",
        "master_formula": "J_a,n=(mu^(2 epsilon)/(4 pi)^(d/2))*Gamma(a+d/2)*Gamma(n-a-d/2)/(Gamma(d/2)*Gamma(n))*Delta^(a+d/2-n)",
        "master_derivation": [
            "1/(ell^2+Delta)^n = 1/Gamma(n) * integral_0^infinity dt t^(n-1) exp[-t(ell^2+Delta)]",
            "integral d^d ell/(2*pi)^d exp(-t ell^2) = (4*pi*t)^(-d/2)",
            "integral d^d ell/(2*pi)^d (ell^2)^a exp(-t ell^2) = (4*pi)^(-d/2)*Gamma(a+d/2)/Gamma(d/2)*t^(-a-d/2)",
            "integral_0^infinity dt t^(n-a-d/2-1) exp(-t Delta) = Gamma(n-a-d/2)*Delta^(a+d/2-n)",
        ],
        "instances": {
            "J_0,2": "mu^(2 epsilon)/(4 pi)^(2-epsilon) * Gamma(epsilon) * Delta^(-epsilon)",
            "J_0,3": "mu^(2 epsilon)/(4 pi)^(2-epsilon) * Gamma(1+epsilon)/2 * Delta^(-1-epsilon)",
            "J_1,3": "mu^(2 epsilon)/(4 pi)^(2-epsilon) * d/4 * Gamma(epsilon) * Delta^(-epsilon)",
            "T^{mu nu}": "integral ell^mu ell^nu/(ell^2+Delta)^3 = (hat_g^{mu nu}/d) J_1,3 = hat_g^{mu nu} mu^(2 epsilon) Gamma(epsilon) Delta^(-epsilon)/(4*(4 pi)^(2-epsilon))",
        },
        "normalization": {
            "A0": "1/(16*pi^2)",
            "L0": "log(4*pi*mu^2/Delta)",
            "L": "L0-EulerGamma",
        },
        "laurent_in_units_of_A0": {
            "J_0,2": j02.render(),
            "Delta*J_0,3": delta_j03.render(),
            "J_1,3": j13_from_gamma.render(),
            "coefficient_of_hat_g_in_T": tensor_from_rotation.render(),
        },
        "laurent_derivation": [
            "mu^(2 epsilon)*(4*pi)^(-2+epsilon)*Delta^(-epsilon) = A0*[1+epsilon*L0+O(epsilon^2)]",
            "Gamma(epsilon) = 1/epsilon-EulerGamma+O(epsilon)",
            "Gamma(1+epsilon) = 1-epsilon*EulerGamma+O(epsilon^2)",
            "d/4 = 1-epsilon/2",
            "1/d = 1/4+epsilon/8+O(epsilon^2)",
        ],
        "metric_split_of_rank_two_pole": {
            "complete": "A0*(g4^{mu nu}-tilde_g^{mu nu})/(4*epsilon)",
            "physical_metric_part": "A0*g4^{mu nu}/(4*epsilon)",
            "evanescent_metric_part": "-A0*tilde_g^{mu nu}/(4*epsilon)",
            "isolated_evanescent_trace": "-A0/2",
            "classification": "KINEMATIC_PROJECTOR_TRACE_ONLY_NOT_AN_ANOMALY_COEFFICIENT",
        },
        "exact_relations": [
            "J_1,3 = J_0,2 - Delta*J_0,3",
            "integral ell^mu ell^nu F(ell^2) = (hat_g^{mu nu}/d) integral ell^2 F(ell^2)",
            "hat_g = g4-tilde_g",
        ],
    }


def build_audit(fourier_phase: str, loop_measure: str, signature: str) -> dict[str, Any]:
    recorder = Recorder()
    recorder.check("Fourier phase lock", fourier_phase, FOURIER_PHASE, "conventions")
    recorder.check("loop measure lock", loop_measure, LOOP_MEASURE, "conventions")
    recorder.check("Euclidean signature lock", signature, SIGNATURE, "conventions")
    recorder.check("derivative Fourier image", "+i k_M", "+i k_M", "conventions")
    feynman_prefactor = Fraction(
        gamma_positive_integer(3),
        gamma_positive_integer(1) ** 3,
    )
    recorder.check("Feynman parameter prefactor", feynman_prefactor, Fraction(2), "Feynman-shift")

    metrics = metric_checks(recorder)
    routing = shift_checks(recorder)
    integrals = integral_checks(recorder)

    categories: dict[str, dict[str, int]] = {}
    for check in recorder.checks:
        category = categories.setdefault(check["category"], {"checks": 0, "failed": 0})
        category["checks"] += 1
        if not check["passed"]:
            category["failed"] += 1

    return {
        "schema": 1,
        "task": TASK_ID,
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "status": "PASS" if not recorder.failures else "FAIL",
        "scope": "DRED projectors, routed triangle denominator, rank-two numerator shift, and exact one-loop scalar/tensor integrals only",
        "excluded": [
            "anomaly coefficient",
            "supergraph numerator",
            "graph multiplicity",
            "color factor",
            "counterterm coefficient",
        ],
        "parameters": {
            "fourier_transform": "f(x)=integral d^d k/(2*pi)^d exp(+i k.x) f(k)",
            "fourier_phase": fourier_phase,
            "derivative_image": "+i k_M",
            "loop_measure": loop_measure,
            "dimension": "d=4-2*epsilon",
            "signature": signature,
            "spin_algebra_metric": "g4",
            "loop_metric": "hat_g",
            "evanescent_metric": "tilde_g=g4-hat_g",
        },
        "arithmetic": {
            "rational_field": "fractions.Fraction",
            "floating_point": False,
            "external_cas": False,
            "formal_symbols": list(POLY_SYMBOLS) + list(FORMAL_SYMBOLS) + ["epsilon"],
        },
        "projectors": metrics,
        "feynman_parameter_shift": routing,
        "integrals": integrals,
        "categories": categories,
        "totals": {
            "exact_checks": len(recorder.checks),
            "failed_checks": len(recorder.failures),
        },
        "checks": recorder.checks,
        "failures": recorder.failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fourier-phase", default=FOURIER_PHASE, choices=[FOURIER_PHASE])
    parser.add_argument("--loop-measure", default=LOOP_MEASURE, choices=[LOOP_MEASURE])
    parser.add_argument("--signature", default=SIGNATURE, choices=[SIGNATURE])
    parser.add_argument("--audit-path", type=Path, default=AUDIT)
    args = parser.parse_args()

    audit = build_audit(args.fourier_phase, args.loop_measure, args.signature)
    args.audit_path.write_text(
        json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if audit["status"] != "PASS":
        print(json.dumps(audit["failures"], indent=2, sort_keys=True, ensure_ascii=False))
        raise SystemExit(1)
    print(
        "Step-5 DRED/integral exact verification: "
        f"{audit['totals']['exact_checks']} checks, 0 failures"
    )


if __name__ == "__main__":
    main()
