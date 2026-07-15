#!/usr/bin/env python3
"""Exact AB1/G1 VVV D-word replay.

This script derives, rather than stores, the six polarized cubic-gauge
permutations times the two derivative placements in each Euclidean chirality.
All coefficients belong to Q(i); no floating-point operation is used.

Locked inputs encoded below:

* epsilon and Euclidean sigma matrices: Step 1, (1.3)--(1.4), (1.51);
* left Grassmann calculus and Euclidean D operators: Step 2A, (2A.4)--(2A.5),
  (2A.41);
* cubic gauge words and ordered differentiation: Step 5A, (5A.52),
  (5A.61)--(5A.62);
* conditional vector and chiral endpoint projectors: Step 5A,
  (5A.64)--(5A.74).

The output order is eta_B eta_D, i.e. (P B_1^E) D^D.  The color parity
c_{U_pi(0) U_pi(1) U_pi(2)} = sgn(pi) c_{U_0 U_1 U_2} is included in every
reported word coefficient.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, Mapping, Sequence, Tuple


def _q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


@dataclass(frozen=True)
class QI:
    """An exact element of Q(i)."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    @classmethod
    def coerce(cls, value: object) -> "QI":
        if isinstance(value, cls):
            return value
        if isinstance(value, (int, Fraction)):
            return cls(_q(value), Fraction(0))
        raise TypeError(f"cannot coerce {value!r} to QI")

    def __add__(self, other: object) -> "QI":
        rhs = self.coerce(other)
        return QI(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "QI":
        return QI(-self.re, -self.im)

    def __sub__(self, other: object) -> "QI":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "QI":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "QI":
        try:
            rhs = self.coerce(other)
        except TypeError:
            return NotImplemented
        return QI(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "QI":
        rhs = self.coerce(other)
        norm = rhs.re * rhs.re + rhs.im * rhs.im
        if norm == 0:
            raise ZeroDivisionError("division by zero in Q(i)")
        return QI(
            (self.re * rhs.re + self.im * rhs.im) / norm,
            (self.im * rhs.re - self.re * rhs.im) / norm,
        )

    def __bool__(self) -> bool:
        return self.re != 0 or self.im != 0

    def __str__(self) -> str:
        if self.im == 0:
            return _fraction_text(self.re)
        if self.re == 0:
            return f"{_fraction_text(self.im)}*i"
        sign = "+" if self.im > 0 else "-"
        return (
            f"{_fraction_text(self.re)}{sign}"
            f"{_fraction_text(abs(self.im))}*i"
        )


ZERO = QI()
ONE = QI(Fraction(1), Fraction(0))
I = QI(Fraction(0), Fraction(1))


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def exact_json(value: QI) -> dict[str, object]:
    payload: dict[str, object] = {
        "real": _fraction_text(value.re),
        "imag": _fraction_text(value.im),
        "text": str(value),
    }
    if value.im == 0 and value.re.denominator == 1:
        payload["integer"] = value.re.numerator
    return payload


class Grassmann:
    """Sparse exterior polynomial with exact Q(i) coefficients."""

    __slots__ = ("terms",)

    def __init__(self, terms: Mapping[int, QI] | None = None) -> None:
        self.terms = {mask: coeff for mask, coeff in (terms or {}).items() if coeff}

    @classmethod
    def scalar(cls, value: object) -> "Grassmann":
        coeff = QI.coerce(value)
        return cls({0: coeff}) if coeff else cls()

    @classmethod
    def generator(cls, index: int) -> "Grassmann":
        return cls({1 << index: ONE})

    def __add__(self, other: object) -> "Grassmann":
        rhs = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        terms = dict(self.terms)
        for mask, coeff in rhs.terms.items():
            value = terms.get(mask, ZERO) + coeff
            if value:
                terms[mask] = value
            elif mask in terms:
                del terms[mask]
        return Grassmann(terms)

    __radd__ = __add__

    def __neg__(self) -> "Grassmann":
        return Grassmann({mask: -coeff for mask, coeff in self.terms.items()})

    def __sub__(self, other: object) -> "Grassmann":
        rhs = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        return self + (-rhs)

    def __rsub__(self, other: object) -> "Grassmann":
        return Grassmann.scalar(other) - self

    def __mul__(self, other: object) -> "Grassmann":
        rhs = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        terms: Dict[int, QI] = {}
        for left_mask, left_coeff in self.terms.items():
            for right_mask, right_coeff in rhs.terms.items():
                if left_mask & right_mask:
                    continue
                inversions = sum(
                    (right_mask & ((1 << index) - 1)).bit_count()
                    for index in range(left_mask.bit_length())
                    if left_mask & (1 << index)
                )
                sign = -1 if inversions % 2 else 1
                mask = left_mask | right_mask
                value = terms.get(mask, ZERO) + sign * left_coeff * right_coeff
                if value:
                    terms[mask] = value
                elif mask in terms:
                    del terms[mask]
        return Grassmann(terms)

    __rmul__ = __mul__

    def left_derivative(self, index: int) -> "Grassmann":
        bit = 1 << index
        terms: Dict[int, QI] = {}
        for mask, coeff in self.terms.items():
            if not mask & bit:
                continue
            sign = -1 if (mask & (bit - 1)).bit_count() % 2 else 1
            terms[mask ^ bit] = sign * coeff
        return Grassmann(terms)

    def set_zero(self, indices: Iterable[int]) -> "Grassmann":
        forbidden = sum(1 << index for index in indices)
        return Grassmann(
            {mask: coeff for mask, coeff in self.terms.items() if not mask & forbidden}
        )

    def coefficient(self, mask: int) -> QI:
        return self.terms.get(mask, ZERO)


NODES = ("S", "M", "G")
COORDINATES = ("theta1", "theta2", "bar1", "bar2")
INDEX = {
    (node, coordinate): 4 * node_number + coordinate_number
    for node_number, node in enumerate(NODES)
    for coordinate_number, coordinate in enumerate(COORDINATES)
}
ETA_B_INDEX = 12
ETA_D_INDEX = 13
ETA_B = Grassmann.generator(ETA_B_INDEX)
ETA_D = Grassmann.generator(ETA_D_INDEX)
ETA_BD_MASK = (1 << ETA_B_INDEX) | (1 << ETA_D_INDEX)


def coordinate(node: str, name: str) -> Grassmann:
    return Grassmann.generator(INDEX[node, name])


def theta(node: str, index: int) -> Grassmann:
    return coordinate(node, "theta1" if index == 0 else "theta2")


def bar_theta_lower(node: str, index: int) -> Grassmann:
    return coordinate(node, "bar1" if index == 0 else "bar2")


EPS_UP = ((0, 1), (-1, 0))
EPS_DOWN = ((0, -1), (1, 0))

# sigma_E^m=(-i sigma^1,-i sigma^2,-i sigma^3,1), m=1,2,3,4.
SIGMA = (
    ((ZERO, -I), (-I, ZERO)),
    ((ZERO, QI.coerce(-1)), (ONE, ZERO)),
    ((-I, ZERO), (ZERO, I)),
    ((ONE, ZERO), (ZERO, ONE)),
)


def derive_bar_sigma() -> Tuple[Tuple[Tuple[QI, QI], Tuple[QI, QI]], ...]:
    matrices = []
    for m in range(4):
        matrix = []
        for dotted in range(2):
            row = []
            for undotted in range(2):
                value = ZERO
                for b in range(2):
                    for dotted_b in range(2):
                        value += (
                            EPS_UP[undotted][b]
                            * EPS_UP[dotted][dotted_b]
                            * SIGMA[m][b][dotted_b]
                        )
                row.append(value)
            matrix.append(tuple(row))
        matrices.append(tuple(matrix))
    return tuple(matrices)


BAR_SIGMA = derive_bar_sigma()
Vector = Tuple[QI, QI, QI, QI]


def vector(values: Sequence[int | Fraction | QI]) -> Vector:
    if len(values) != 4:
        raise ValueError("a Euclidean momentum must have four components")
    return tuple(QI.coerce(value) for value in values)  # type: ignore[return-value]


def vector_add(left: Vector, right: Vector) -> Vector:
    return tuple(left[m] + right[m] for m in range(4))  # type: ignore[return-value]


def vector_neg(value: Vector) -> Vector:
    return tuple(-value[m] for m in range(4))  # type: ignore[return-value]


def vector_scale(scale: int | Fraction | QI, value: Vector) -> Vector:
    return tuple(QI.coerce(scale) * value[m] for m in range(4))  # type: ignore[return-value]


ZERO_VECTOR = vector((0, 0, 0, 0))


def bar_theta_up(node: str, dotted: int) -> Grassmann:
    return sum(
        EPS_UP[dotted][lower] * bar_theta_lower(node, lower)
        for lower in range(2)
    )


def d_lower(field: Grassmann, node: str, undotted: int, momentum: Vector) -> Grassmann:
    result = field.left_derivative(INDEX[node, "theta1" if undotted == 0 else "theta2"])
    multiplier = Grassmann.scalar(0)
    for m in range(4):
        for dotted in range(2):
            multiplier += I * momentum[m] * SIGMA[m][undotted][dotted] * bar_theta_up(node, dotted)
    return result + multiplier * field


def bar_d_lower(field: Grassmann, node: str, dotted: int, momentum: Vector) -> Grassmann:
    # bar partial_dot = epsilon_dot,dot' partial / partial bar theta_dot'.
    if dotted == 0:
        result = -field.left_derivative(INDEX[node, "bar2"])
    else:
        result = field.left_derivative(INDEX[node, "bar1"])
    multiplier = Grassmann.scalar(0)
    for m in range(4):
        for undotted in range(2):
            multiplier += (
                -I
                * momentum[m]
                * SIGMA[m][undotted][dotted]
                * theta(node, undotted)
            )
    return result + multiplier * field


def d_up(field: Grassmann, node: str, undotted: int, momentum: Vector) -> Grassmann:
    return sum(
        EPS_UP[undotted][lower] * d_lower(field, node, lower, momentum)
        for lower in range(2)
    )


def bar_d_up(field: Grassmann, node: str, dotted: int, momentum: Vector) -> Grassmann:
    return sum(
        EPS_UP[dotted][lower] * bar_d_lower(field, node, lower, momentum)
        for lower in range(2)
    )


def d_squared(field: Grassmann, node: str, momentum: Vector) -> Grassmann:
    # D^a D_a = 2 D_2 D_1 in the locked epsilon convention.
    return 2 * d_lower(d_lower(field, node, 0, momentum), node, 1, momentum)


def bar_d_squared(field: Grassmann, node: str, momentum: Vector) -> Grassmann:
    # bar D_dot-a bar D^dot-a = 2 bar D_dot-1 bar D_dot-2.
    return 2 * bar_d_lower(bar_d_lower(field, node, 1, momentum), node, 0, momentum)


def theta_squared_difference(left: str, right: str | None = None) -> Grassmann:
    theta1 = theta(left, 0) - (theta(right, 0) if right else 0)
    theta2 = theta(left, 1) - (theta(right, 1) if right else 0)
    return -2 * theta1 * theta2


def bar_theta_squared_difference(left: str, right: str | None = None) -> Grassmann:
    bar1 = bar_theta_lower(left, 0) - (bar_theta_lower(right, 0) if right else 0)
    bar2 = bar_theta_lower(left, 1) - (bar_theta_lower(right, 1) if right else 0)
    return 2 * bar1 * bar2


def superspace_delta(left: str, right: str) -> Grassmann:
    return theta_squared_difference(left, right) * bar_theta_squared_difference(left, right)


def chiral_b_endpoint(node: str, momentum: Vector) -> Grassmann:
    """Polarized chiral endpoint with D_1 Phi|=eta_B."""

    exponent = Grassmann.scalar(0)
    for m in range(4):
        for undotted in range(2):
            for dotted in range(2):
                exponent += (
                    I
                    * momentum[m]
                    * SIGMA[m][undotted][dotted]
                    * theta(node, undotted)
                    * bar_theta_up(node, dotted)
                )
    return theta(node, 0) * ETA_B * (
        Grassmann.scalar(1) + exponent + Fraction(1, 2) * exponent * exponent
    )


def vector_d_endpoint(node: str, dotted: int) -> Grassmann:
    """Polarized vector endpoint with D^2 bar D_dot-a u|=eta_D."""

    if dotted == 0:
        base = Fraction(1, 4) * theta_squared_difference(node) * bar_theta_lower(node, 1)
    else:
        base = -Fraction(1, 4) * theta_squared_difference(node) * bar_theta_lower(node, 0)
    return base * ETA_D


def integrate_full(field: Grassmann, node: str) -> Grassmann:
    projected = Fraction(1, 16) * d_squared(
        bar_d_squared(field, node, ZERO_VECTOR), node, ZERO_VECTOR
    )
    return projected.set_zero(INDEX[node, name] for name in COORDINATES)


def integrate_chiral(field: Grassmann, node: str) -> Grassmann:
    projected = -Fraction(1, 4) * d_squared(field, node, ZERO_VECTOR)
    return projected.set_zero(INDEX[node, name] for name in COORDINATES)


def integrate_antichiral(field: Grassmann, node: str) -> Grassmann:
    projected = -Fraction(1, 4) * bar_d_squared(field, node, ZERO_VECTOR)
    return projected.set_zero(INDEX[node, name] for name in COORDINATES)


def permutation_sign(permutation: Tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


PERMUTATIONS = tuple(itertools.permutations((0, 1, 2)))
PLACEMENTS = ("QL", "LQ")
ROLES = ("source_vector", "matter_vector", "external_D")
WordKey = Tuple[Tuple[int, int, int], str]


def polarized_vvv_word(
    sector: str,
    placement: str,
    permutation: Tuple[int, int, int],
    endpoints: Sequence[Grassmann],
    endpoint_momenta: Sequence[Vector],
) -> Grassmann:
    """Generate one word from the polarized cubic form; no table is stored."""

    i, j, k = permutation
    ij_momentum = vector_add(endpoint_momenta[i], endpoint_momenta[j])
    jk_momentum = vector_add(endpoint_momenta[j], endpoint_momenta[k])
    word = Grassmann.scalar(0)
    if sector == "+" and placement == "QL":
        for undotted in range(2):
            word += bar_d_squared(
                endpoints[i]
                * d_up(endpoints[j], "G", undotted, endpoint_momenta[j]),
                "G",
                ij_momentum,
            ) * bar_d_squared(
                d_lower(endpoints[k], "G", undotted, endpoint_momenta[k]),
                "G",
                endpoint_momenta[k],
            )
    elif sector == "+" and placement == "LQ":
        for undotted in range(2):
            word += bar_d_squared(
                d_up(endpoints[i], "G", undotted, endpoint_momenta[i]),
                "G",
                endpoint_momenta[i],
            ) * bar_d_squared(
                endpoints[j]
                * d_lower(endpoints[k], "G", undotted, endpoint_momenta[k]),
                "G",
                jk_momentum,
            )
    elif sector == "-" and placement == "QL":
        for dotted in range(2):
            word += d_squared(
                endpoints[i]
                * bar_d_lower(endpoints[j], "G", dotted, endpoint_momenta[j]),
                "G",
                ij_momentum,
            ) * d_squared(
                bar_d_up(endpoints[k], "G", dotted, endpoint_momenta[k]),
                "G",
                endpoint_momenta[k],
            )
    elif sector == "-" and placement == "LQ":
        for dotted in range(2):
            word += d_squared(
                bar_d_lower(endpoints[i], "G", dotted, endpoint_momenta[i]),
                "G",
                endpoint_momenta[i],
            ) * d_squared(
                endpoints[j]
                * bar_d_up(endpoints[k], "G", dotted, endpoint_momenta[k]),
                "G",
                jk_momentum,
            )
    else:
        raise ValueError(f"unknown sector/placement: {sector!r}/{placement!r}")
    return word


def evaluate_words(loop: Vector, p: Vector, dotted: int, sector: str) -> Dict[WordKey, QI]:
    """Run the source transfer, matter vertex, and endpoint projections."""

    q = vector_neg(p)
    source_vector_momentum = vector_add(vector_neg(loop), vector_add(p, q))
    source_matter_momentum = loop
    endpoint_momenta = (
        vector_add(loop, vector_neg(vector_add(p, q))),
        vector_add(vector_neg(loop), p),
        q,
    )
    endpoints = (
        superspace_delta("S", "G"),
        superspace_delta("M", "G"),
        vector_d_endpoint("G", dotted),
    )

    matter_line = bar_d_squared(
        d_squared(
            superspace_delta("S", "M"), "S", source_matter_momentum
        ),
        "S",
        source_matter_momentum,
    )
    matter_source_d0 = d_lower(
        matter_line, "S", 0, source_matter_momentum
    )
    matter_source_d1d0 = d_lower(
        matter_source_d0, "S", 1, source_matter_momentum
    )
    external_b = chiral_b_endpoint("M", p)

    result: Dict[WordKey, QI] = {}
    for permutation in PERMUTATIONS:
        color_sign = permutation_sign(permutation)
        for placement in PLACEMENTS:
            vvv = polarized_vvv_word(
                sector,
                placement,
                permutation,
                endpoints,
                endpoint_momenta,
            )
            gauge_source_d0 = d_lower(vvv, "S", 0, source_vector_momentum)
            gauge_source_bar2 = bar_d_squared(
                gauge_source_d0, "S", source_vector_momentum
            )
            gauge_source_d0_bar2_d0 = d_lower(
                gauge_source_bar2, "S", 0, source_vector_momentum
            )
            gauge_source_d1d0_bar2_d0 = d_lower(
                gauge_source_d0_bar2_d0, "S", 1, source_vector_momentum
            )

            # Exact graded Leibniz output of the outer source D_2.
            transferred = color_sign * (
                gauge_source_d1d0_bar2_d0 * matter_source_d0
                + gauge_source_d0_bar2_d0 * matter_source_d1d0
            ) * external_b
            transferred = integrate_full(transferred, "M")
            transferred = (
                integrate_chiral(transferred, "G")
                if sector == "+"
                else integrate_antichiral(transferred, "G")
            )
            transferred = transferred.set_zero(
                INDEX["S", name] for name in COORDINATES
            )
            result[permutation, placement] = transferred.coefficient(ETA_BD_MASK)
    return result


def row_laplacian(
    shift: Vector, p: Vector, dotted: int, sector: str
) -> Dict[WordKey, QI]:
    """Exact central second difference, equal to the loop Hessian trace."""

    center = evaluate_words(shift, p, dotted, sector)
    result = {key: ZERO for key in center}
    for m in range(4):
        unit = [ZERO, ZERO, ZERO, ZERO]
        unit[m] = ONE
        plus = evaluate_words(vector_add(shift, tuple(unit)), p, dotted, sector)  # type: ignore[arg-type]
        minus = evaluate_words(vector_add(shift, vector_neg(tuple(unit))), p, dotted, sector)  # type: ignore[arg-type]
        for key in result:
            result[key] += plus[key] - 2 * center[key] + minus[key]
    return result


def endpoint_spinor(p: Vector, dotted: int) -> QI:
    """i bar-sigma_E^{m dot-a 2} p_m for the chosen source polarization."""

    return sum(I * BAR_SIGMA[m][dotted][1] * p[m] for m in range(4))


def word_formula(sector: str, placement: str, permutation: Tuple[int, int, int]) -> str:
    i, j, k = (ROLES[index] for index in permutation)
    if sector == "+" and placement == "QL":
        return f"barD2({i} D^a {j}) barD2(D_a {k})"
    if sector == "+" and placement == "LQ":
        return f"barD2(D^a {i}) barD2({j} D_a {k})"
    if sector == "-" and placement == "QL":
        return f"D2({i} barD_dot-a {j}) D2(barD^dot-a {k})"
    return f"D2(barD_dot-a {i}) D2({j} barD^dot-a {k})"


def replay_sample(p: Vector, dotted: int, sector: str) -> dict[str, object]:
    zero = ZERO_VECTOR
    half_p = vector_scale(Fraction(1, 2), p)
    lap_zero = row_laplacian(zero, p, dotted, sector)
    lap_half = row_laplacian(half_p, p, dotted, sector)
    lap_one = row_laplacian(p, p, dotted, sector)
    spinor = endpoint_spinor(p, dotted)
    if not spinor:
        raise AssertionError("chosen exact validation momentum has a zero endpoint spinor")

    entries = []
    normalized: Dict[WordKey, QI] = {}
    for permutation in PERMUTATIONS:
        for placement in PLACEMENTS:
            key = (permutation, placement)
            if 2 * lap_half[key] != lap_zero[key] + lap_one[key]:
                raise AssertionError(
                    f"Feynman-shift trace is not affine for {sector} {key}"
                )
            # For q=-p, l=L+y p and
            # 2 int_0^1 dy (1-y) C(y)=(2 C(0)+C(1))/3.
            # The rank-two trace projection is C=Delta_l N/8.
            simplex_trace = (2 * lap_zero[key] + lap_one[key]) / 24
            coefficient = simplex_trace / spinor
            if coefficient.im != 0:
                raise AssertionError(
                    f"non-real normalized coefficient for {sector} {key}: {coefficient}"
                )
            normalized[key] = coefficient
            entries.append(
                {
                    "permutation": list(permutation),
                    "color_permutation_sign": permutation_sign(permutation),
                    "placement": placement,
                    "polarized_word": word_formula(sector, placement, permutation),
                    "loop_hessian_trace_at_y_0": exact_json(lap_zero[key]),
                    "loop_hessian_trace_at_y_half": exact_json(lap_half[key]),
                    "loop_hessian_trace_at_y_1": exact_json(lap_one[key]),
                    "affine_midpoint_check": True,
                    "simplex_trace_before_endpoint_division": exact_json(simplex_trace),
                    "endpoint_spinor_i_barsigma_p": exact_json(spinor),
                    "normalized_coefficient": exact_json(coefficient),
                }
            )
    total = sum(normalized.values(), ZERO)
    return {
        "momentum_p": [exact_json(component) for component in p],
        "momentum_q": [exact_json(component) for component in vector_neg(p)],
        "external_dotted_index_zero_based": dotted,
        "sector": sector,
        "entries": entries,
        "normalized_total": exact_json(total),
        "normalized_map": normalized,
    }


def public_sample(sample: Mapping[str, object], include_entries: bool) -> dict[str, object]:
    payload = {
        key: value
        for key, value in sample.items()
        if key != "normalized_map" and (include_entries or key != "entries")
    }
    return payload


def table_payload(values: Mapping[WordKey, QI]) -> list[dict[str, object]]:
    return [
        {
            "permutation": list(permutation),
            "color_permutation_sign": permutation_sign(permutation),
            "QL": exact_json(values[permutation, "QL"]),
            "LQ": exact_json(values[permutation, "LQ"]),
        }
        for permutation in PERMUTATIONS
    ]


def build_artifact() -> dict[str, object]:
    validation_momenta = (
        vector((1, 2, 3, 1)),
        vector((2, -1, 1, 3)),
        vector((-1, 3, 2, 2)),
    )
    internal_samples = []
    for p in validation_momenta:
        for dotted in (0, 1):
            for sector in ("+", "-"):
                internal_samples.append(replay_sample(p, dotted, sector))

    reference_plus = internal_samples[0]["normalized_map"]
    assert isinstance(reference_plus, dict)
    reference_minus = internal_samples[1]["normalized_map"]
    assert isinstance(reference_minus, dict)

    for sample in internal_samples:
        values = sample["normalized_map"]
        assert isinstance(values, dict)
        reference = reference_plus if sample["sector"] == "+" else reference_minus
        if values != reference:
            raise AssertionError(
                "normalized table depends on exact validation momentum or dotted index"
            )

    plus_total = sum(reference_plus.values(), ZERO)
    minus_total = sum(reference_minus.values(), ZERO)
    if minus_total != -plus_total:
        raise AssertionError("the two chiral total D-word coefficients do not cancel")
    reference_trace = [
        public_sample(internal_samples[0], include_entries=True),
        public_sample(internal_samples[1], include_entries=True),
    ]
    validation = [
        {
            **public_sample(sample, include_entries=False),
            "matches_sector_reference_exactly": True,
        }
        for sample in internal_samples
    ]
    return {
        "schema": "step5-ab1-g1-vvv-dword-replay-v1",
        "arithmetic": "Q(i), exact fractions only; no floating point",
        "contract_inputs": [
            "step-01-supersymmetry-commutator.md (1.3)-(1.4), (1.51)-(1.52)",
            "step-02a-flat-superspace.md (2A.4)-(2A.5), (2A.41)",
            "step-05a-component-bv-brst-primitive-supergraph-grammar.md (5A.52), (5A.61)-(5A.62), (5A.64)-(5A.74)",
        ],
        "external_order": "eta_B eta_D = (P_dot-a B_1^E) D^{D dot-a}",
        "role_order": list(ROLES),
        "source_transfer": {
            "matter_line": "barD2 D2 delta^4(theta_S-theta_M)",
            "gauge_factor_before_outer_D2": "D_1 barD2 D_1 VVV",
            "graded_outer_source_D2": "(D_2 D_1 barD2 D_1 VVV)(D_1 matter_line) + (D_1 barD2 D_1 VVV)(D_2 D_1 matter_line)",
            "matter_endpoint": "chiral Phi with D_1 Phi|=eta_B",
            "gauge_endpoint": "vector u with D2 barD_dot-a u|=eta_D",
        },
        "tensor_and_simplex_rule": {
            "rank_two_trace": "C(y)=Delta_l N(l=y p)/8",
            "midpoint_proof": "2 Delta_l N(p/2)=Delta_l N(0)+Delta_l N(p), checked word-by-word exactly",
            "simplex": "2 int_0^1 dy (1-y) C(y)=(2 Delta_l N(0)+Delta_l N(p))/24",
            "kinematics": "q=-p after retaining P_dot-a on the external leg",
        },
        "generated_tables": {
            "plus": table_payload(reference_plus),
            "minus": table_payload(reference_minus),
            "plus_total": exact_json(plus_total),
            "minus_total": exact_json(minus_total),
        },
        "reference_word_traces": reference_trace,
        "exact_validation_samples": validation,
        "checks": {
            "six_permutations_times_two_placements_per_chirality": len(reference_plus) == 12,
            "color_parity_included_in_each_entry": True,
            "all_feynman_shift_midpoints_affine": True,
            "all_three_momenta_and_both_dotted_indices_agree": True,
            "minus_total_is_negative_plus_total": minus_total == -plus_total,
            "no_output_integer_is_used_as_an_input": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the generated JSON artifact")
    parser.add_argument("--check", type=Path, help="compare generated JSON with an existing artifact")
    arguments = parser.parse_args()

    artifact = build_artifact()
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    if arguments.check is not None:
        existing = arguments.check.read_text(encoding="utf-8")
        if existing != rendered:
            raise SystemExit(f"FAIL: stale replay artifact: {arguments.check}")
    if arguments.output is not None:
        arguments.output.write_text(rendered, encoding="utf-8")
        print(f"PASS: wrote {arguments.output}")
    elif arguments.check is None:
        print(rendered, end="")
    else:
        print(f"PASS: exact replay matches {arguments.check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
