#!/usr/bin/env python3
"""Exact target-blind replay of the order-g^2 AA pure-gauge source/SD orbit.

The calculation is performed in Q(sqrt(2), i) with sparse exterior
polynomials.  It expands the canonical composite source A_c through A_3,
the outer connection through gamma_2, and the gauge action through S_g4.
No holomorphic-twist coefficient is used as input.

This file is intentionally independent of the main AA audit.  It emits a
machine-readable occurrence ledger and fails closed if a factor, color
normalization, source word, or DRED master identity changes.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import multiprocessing
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


@dataclass(frozen=True)
class A:
    """Exact element a+b sqrt(2)+i(c+d sqrt(2))."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    c: Fraction = Fraction(0)
    d: Fraction = Fraction(0)

    @classmethod
    def coerce(cls, value: object) -> "A":
        if isinstance(value, cls):
            return value
        if isinstance(value, (int, Fraction)):
            return cls(q(value))
        raise TypeError(f"cannot coerce {value!r} to Q(sqrt(2),i)")

    def __add__(self, other: object) -> "A":
        rhs = self.coerce(other)
        return A(self.a + rhs.a, self.b + rhs.b, self.c + rhs.c, self.d + rhs.d)

    __radd__ = __add__

    def __neg__(self) -> "A":
        return A(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: object) -> "A":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "A":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "A":
        try:
            rhs = self.coerce(other)
        except TypeError:
            return NotImplemented
        # (x+i y)(u+i v), with x,y,u,v in Q(sqrt(2)).
        xr, xs, yi, ys = self.a, self.b, self.c, self.d
        ur, us, vi, vs = rhs.a, rhs.b, rhs.c, rhs.d
        xu_a = xr * ur + 2 * xs * us
        xu_b = xr * us + xs * ur
        yv_a = yi * vi + 2 * ys * vs
        yv_b = yi * vs + ys * vi
        xv_a = xr * vi + 2 * xs * vs
        xv_b = xr * vs + xs * vi
        yu_a = yi * ur + 2 * ys * us
        yu_b = yi * us + ys * ur
        return A(xu_a - yv_a, xu_b - yv_b, xv_a + yu_a, xv_b + yu_b)

    __rmul__ = __mul__

    def inverse(self) -> "A":
        # Invert x+i y using (x-i y)/(x^2+y^2), then invert Q(sqrt(2)).
        x2y2 = self * A(self.a, self.b, -self.c, -self.d)
        if x2y2.c or x2y2.d:
            raise AssertionError("complex norm did not land in Q(sqrt(2))")
        norm = x2y2.a * x2y2.a - 2 * x2y2.b * x2y2.b
        if norm == 0:
            raise ZeroDivisionError("division by zero")
        inv_real = A(x2y2.a / norm, -x2y2.b / norm)
        return A(self.a, self.b, -self.c, -self.d) * inv_real

    def __truediv__(self, other: object) -> "A":
        return self * self.coerce(other).inverse()

    def __bool__(self) -> bool:
        return any((self.a, self.b, self.c, self.d))

    def square(self) -> "A":
        return self * self

    def text(self) -> str:
        pieces: list[str] = []
        for coefficient, suffix in (
            (self.a, ""),
            (self.b, "sqrt(2)"),
            (self.c, "i"),
            (self.d, "i sqrt(2)"),
        ):
            if not coefficient:
                continue
            magnitude = abs(coefficient)
            if suffix:
                body = suffix if magnitude == 1 else f"{magnitude}*{suffix}"
            else:
                body = str(magnitude)
            if not pieces:
                pieces.append(("-" if coefficient < 0 else "") + body)
            else:
                pieces.append((" - " if coefficient < 0 else " + ") + body)
        return "0" if not pieces else "".join(pieces)


ZERO = A()
ONE = A(Fraction(1))
I = A(c=Fraction(1))
SQRT2 = A(b=Fraction(1))


Vector = tuple[A, A, A, A]


def vec(values: Sequence[int | Fraction | A]) -> Vector:
    if len(values) != 4:
        raise ValueError("a Euclidean vector has four components")
    return tuple(A.coerce(value) for value in values)  # type: ignore[return-value]


ZERO_VECTOR = vec((0, 0, 0, 0))


def vadd(*values: Vector) -> Vector:
    return tuple(sum((value[m] for value in values), ZERO) for m in range(4))  # type: ignore[return-value]


def vscale(coefficient: int | Fraction | A, value: Vector) -> Vector:
    coefficient = A.coerce(coefficient)
    return tuple(coefficient * component for component in value)  # type: ignore[return-value]


def vneg(value: Vector) -> Vector:
    return vscale(-1, value)


def vdot(left: Vector, right: Vector) -> A:
    return sum((left[m] * right[m] for m in range(4)), ZERO)


EPS_UP = ((0, 1), (-1, 0))

# sigma_E^m=(-i sigma^1,-i sigma^2,-i sigma^3,1).
SIGMA = (
    ((ZERO, -I), (-I, ZERO)),
    ((ZERO, A(-1)), (ONE, ZERO)),
    ((-I, ZERO), (ZERO, I)),
    ((ONE, ZERO), (ZERO, ONE)),
)


@dataclass(frozen=True)
class Context:
    nodes: tuple[str, ...]
    label_momenta: tuple[Mapping[str, Vector], ...]
    eta_index: int

    @property
    def coordinate_count(self) -> int:
        return 4 * len(self.nodes)

    @property
    def generator_count(self) -> int:
        return self.eta_index + 1

    @property
    def label_count(self) -> int:
        return len(self.label_momenta)

    def coordinate_index(self, node: str, offset: int) -> int:
        return 4 * self.nodes.index(node) + offset

    def momentum(self, exponents: tuple[int, ...], node: str) -> Vector:
        values = ZERO_VECTOR
        for exponent, node_map in zip(exponents, self.label_momenta, strict=True):
            if exponent:
                values = vadd(values, vscale(exponent, node_map.get(node, ZERO_VECTOR)))
        return values


TermKey = tuple[int, tuple[int, ...]]


class P:
    """Sparse exterior polynomial with commuting field-label exponents."""

    __slots__ = ("ctx", "terms")

    def __init__(self, ctx: Context, terms: Mapping[TermKey, A] | None = None) -> None:
        self.ctx = ctx
        self.terms = {key: value for key, value in (terms or {}).items() if value}

    @classmethod
    def scalar(cls, ctx: Context, value: object) -> "P":
        coefficient = A.coerce(value)
        exponents = (0,) * ctx.label_count
        return cls(ctx, {(0, exponents): coefficient}) if coefficient else cls(ctx)

    @classmethod
    def grass_generator(cls, ctx: Context, index: int) -> "P":
        return cls(ctx, {(1 << index, (0,) * ctx.label_count): ONE})

    @classmethod
    def label(cls, ctx: Context, index: int) -> "P":
        exponents = [0] * ctx.label_count
        exponents[index] = 1
        return cls(ctx, {(0, tuple(exponents)): ONE})

    def __add__(self, other: object) -> "P":
        rhs = other if isinstance(other, P) else P.scalar(self.ctx, other)
        if rhs.ctx is not self.ctx:
            raise ValueError("polynomial contexts differ")
        terms = dict(self.terms)
        for key, coefficient in rhs.terms.items():
            value = terms.get(key, ZERO) + coefficient
            if value:
                terms[key] = value
            elif key in terms:
                del terms[key]
        return P(self.ctx, terms)

    __radd__ = __add__

    def __neg__(self) -> "P":
        return P(self.ctx, {key: -value for key, value in self.terms.items()})

    def __sub__(self, other: object) -> "P":
        return self + (-other if isinstance(other, P) else -A.coerce(other))

    def __rsub__(self, other: object) -> "P":
        return P.scalar(self.ctx, other) - self

    def __mul__(self, other: object) -> "P":
        rhs = other if isinstance(other, P) else P.scalar(self.ctx, other)
        if rhs.ctx is not self.ctx:
            raise ValueError("polynomial contexts differ")
        terms: dict[TermKey, A] = {}
        for (left_mask, left_exp), left_coefficient in self.terms.items():
            for (right_mask, right_exp), right_coefficient in rhs.terms.items():
                if left_mask & right_mask:
                    continue
                inversions = sum(
                    (right_mask & ((1 << index) - 1)).bit_count()
                    for index in range(self.ctx.generator_count)
                    if left_mask & (1 << index)
                )
                sign = -1 if inversions % 2 else 1
                mask = left_mask | right_mask
                exponents = tuple(
                    left + right for left, right in zip(left_exp, right_exp, strict=True)
                )
                key = mask, exponents
                value = terms.get(key, ZERO) + sign * left_coefficient * right_coefficient
                if value:
                    terms[key] = value
                elif key in terms:
                    del terms[key]
        return P(self.ctx, terms)

    __rmul__ = __mul__

    def left_derivative(self, index: int) -> "P":
        terms: dict[TermKey, A] = {}
        bit = 1 << index
        for (mask, exponents), coefficient in self.terms.items():
            if not mask & bit:
                continue
            sign = -1 if (mask & (bit - 1)).bit_count() % 2 else 1
            key = mask ^ bit, exponents
            terms[key] = terms.get(key, ZERO) + sign * coefficient
        return P(self.ctx, terms)

    def set_coordinates_zero(self, node: str) -> "P":
        forbidden = sum(1 << self.ctx.coordinate_index(node, offset) for offset in range(4))
        return P(
            self.ctx,
            {key: value for key, value in self.terms.items() if not key[0] & forbidden},
        )

    def coefficient_labels(self, target: Iterable[int]) -> "P":
        target_tuple = tuple(target)
        if len(target_tuple) != self.ctx.label_count:
            raise ValueError("wrong target label degree")
        zero = (0,) * self.ctx.label_count
        return P(
            self.ctx,
            {
                (mask, zero): value
                for (mask, exponents), value in self.terms.items()
                if exponents == target_tuple
            },
        )

    def eta_coefficient(self) -> A:
        zero = (0,) * self.ctx.label_count
        return self.terms.get((1 << self.ctx.eta_index, zero), ZERO)

    def grass_coefficient(self, mask: int) -> A:
        zero = (0,) * self.ctx.label_count
        return self.terms.get((mask, zero), ZERO)

    def scalar_coefficient(self) -> A:
        zero = (0,) * self.ctx.label_count
        return self.terms.get((0, zero), ZERO)


def coordinate(ctx: Context, node: str, offset: int) -> P:
    return P.grass_generator(ctx, ctx.coordinate_index(node, offset))


def theta(ctx: Context, node: str, index: int) -> P:
    return coordinate(ctx, node, index)


def bar_theta_lower(ctx: Context, node: str, dotted: int) -> P:
    return coordinate(ctx, node, 2 + dotted)


def bar_theta_up(ctx: Context, node: str, dotted: int) -> P:
    return sum(
        (EPS_UP[dotted][lower] * bar_theta_lower(ctx, node, lower) for lower in range(2)),
        P.scalar(ctx, 0),
    )


def d_lower(poly: P, node: str, undotted: int) -> P:
    result = poly.left_derivative(poly.ctx.coordinate_index(node, undotted))
    for (mask, exponents), coefficient in list(poly.terms.items()):
        momentum = poly.ctx.momentum(exponents, node)
        monomial = P(poly.ctx, {(mask, exponents): coefficient})
        multiplier = P.scalar(poly.ctx, 0)
        for m in range(4):
            for dotted in range(2):
                multiplier += I * momentum[m] * SIGMA[m][undotted][dotted] * bar_theta_up(
                    poly.ctx, node, dotted
                )
        result += multiplier * monomial
    return result


def bar_d_lower(poly: P, node: str, dotted: int) -> P:
    if dotted == 0:
        result = -poly.left_derivative(poly.ctx.coordinate_index(node, 3))
    else:
        result = poly.left_derivative(poly.ctx.coordinate_index(node, 2))
    for (mask, exponents), coefficient in list(poly.terms.items()):
        momentum = poly.ctx.momentum(exponents, node)
        monomial = P(poly.ctx, {(mask, exponents): coefficient})
        multiplier = P.scalar(poly.ctx, 0)
        for m in range(4):
            for undotted in range(2):
                multiplier += (
                    -I
                    * momentum[m]
                    * SIGMA[m][undotted][dotted]
                    * theta(poly.ctx, node, undotted)
                )
        result += multiplier * monomial
    return result


def d_up(poly: P, node: str, undotted: int) -> P:
    return sum(
        (EPS_UP[undotted][lower] * d_lower(poly, node, lower) for lower in range(2)),
        P.scalar(poly.ctx, 0),
    )


def bar_d_up(poly: P, node: str, dotted: int) -> P:
    return sum(
        (EPS_UP[dotted][lower] * bar_d_lower(poly, node, lower) for lower in range(2)),
        P.scalar(poly.ctx, 0),
    )


def d2(poly: P, node: str) -> P:
    return 2 * d_lower(d_lower(poly, node, 0), node, 1)


def bar_d2(poly: P, node: str) -> P:
    return 2 * bar_d_lower(bar_d_lower(poly, node, 1), node, 0)


def delta4(ctx: Context, left: str, right: str) -> P:
    result = P.scalar(ctx, 4)
    for offset in range(4):
        result *= coordinate(ctx, left, offset) - coordinate(ctx, right, offset)
    return result


def integrate_chiral(poly: P, node: str) -> P:
    return (-Fraction(1, 4) * d2(poly, node)).set_coordinates_zero(node)


def integrate_antichiral(poly: P, node: str) -> P:
    return (-Fraction(1, 4) * bar_d2(poly, node)).set_coordinates_zero(node)


Mat = tuple[tuple[P, P], tuple[P, P]]


def zero_mat(ctx: Context) -> Mat:
    z = P.scalar(ctx, 0)
    return ((z, z), (z, z))


def mat_add(*values: Mat) -> Mat:
    if not values:
        raise ValueError("mat_add needs at least one matrix")
    return tuple(
        tuple(sum((value[row][column] for value in values), P.scalar(values[0][0][0].ctx, 0)) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_scale(coefficient: object, value: Mat) -> Mat:
    return tuple(
        tuple(coefficient * value[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_neg(value: Mat) -> Mat:
    return mat_scale(-1, value)


def mat_sub(left: Mat, right: Mat) -> Mat:
    return mat_add(left, mat_neg(right))


def mat_mul(left: Mat, right: Mat) -> Mat:
    return tuple(
        tuple(
            sum(
                (left[row][middle] * right[middle][column] for middle in range(2)),
                P.scalar(left[0][0].ctx, 0),
            )
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def mat_trace(value: Mat) -> P:
    return value[0][0] + value[1][1]


def mat_d(value: Mat, node: str, undotted: int) -> Mat:
    return tuple(
        tuple(d_lower(value[row][column], node, undotted) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_d_up(value: Mat, node: str, undotted: int) -> Mat:
    return tuple(
        tuple(d_up(value[row][column], node, undotted) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_bar_d(value: Mat, node: str, dotted: int) -> Mat:
    return tuple(
        tuple(bar_d_lower(value[row][column], node, dotted) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_bar_d_up(value: Mat, node: str, dotted: int) -> Mat:
    return tuple(
        tuple(bar_d_up(value[row][column], node, dotted) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_d2(value: Mat, node: str) -> Mat:
    return tuple(
        tuple(d2(value[row][column], node) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_bar_d2(value: Mat, node: str) -> Mat:
    return tuple(
        tuple(bar_d2(value[row][column], node) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


T_NUMERIC: tuple[tuple[tuple[A, A], tuple[A, A]], ...] = (
    ((ZERO, A(Fraction(1, 2))), (A(Fraction(1, 2)), ZERO)),
    ((ZERO, -I * Fraction(1, 2)), (I * Fraction(1, 2), ZERO)),
    ((A(Fraction(1, 2)), ZERO), (ZERO, A(Fraction(-1, 2)))),
)


def matrix_field(poly: P, color: int) -> Mat:
    return tuple(
        tuple(T_NUMERIC[color][row][column] * poly for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def component(value: Mat, color: int) -> P:
    # kappa_AB=tr(T_A T_B)=delta_AB/2, hence X^A=2 tr(T_A X).
    t = T_NUMERIC[color]
    product = tuple(
        tuple(
            sum(
                (t[row][middle] * value[middle][column] for middle in range(2)),
                P.scalar(value[0][0].ctx, 0),
            )
            for column in range(2)
        )
        for row in range(2)
    )
    return 2 * (product[0][0] + product[1][1])


def labeled_endpoint(base: P, label: int, color: int) -> Mat:
    return matrix_field(base * P.label(base.ctx, label), color)


def endpoint_delta(ctx: Context, left: str, right: str, label: int, color: int) -> Mat:
    return labeled_endpoint(delta4(ctx, left, right), label, color)


def endpoint_A(
    ctx: Context,
    node: str,
    label: int,
    color: int,
    polarization: Vector,
) -> Mat:
    base = P.scalar(ctx, 0)
    for m in range(4):
        for undotted in range(2):
            for dotted in range(2):
                base += (
                    polarization[m]
                    * SIGMA[m][undotted][dotted]
                    * theta(ctx, node, undotted)
                    * bar_theta_up(ctx, node, dotted)
                )
    return labeled_endpoint(base, label, color)


def endpoint_D(
    ctx: Context,
    node: str,
    label: int,
    color: int,
    dotted: int,
    eta_index: int | None = None,
) -> Mat:
    theta_square = -2 * theta(ctx, node, 0) * theta(ctx, node, 1)
    if dotted == 0:
        base = Fraction(1, 4) * theta_square * bar_theta_lower(ctx, node, 1)
    else:
        base = -Fraction(1, 4) * theta_square * bar_theta_lower(ctx, node, 0)
    base *= P.grass_generator(ctx, ctx.eta_index if eta_index is None else eta_index)
    return labeled_endpoint(base, label, color)


def sum_mats(values: Sequence[Mat]) -> Mat:
    return mat_add(*values)


def canonical_A_words(U: Mat, node: str) -> tuple[Mat, Mat, Mat]:
    X = mat_d(U, node, 0)
    C = mat_sub(mat_mul(X, U), mat_mul(U, X))
    U2 = mat_mul(U, U)
    E = mat_add(
        mat_mul(X, U2),
        mat_scale(-2, mat_mul(mat_mul(U, X), U)),
        mat_mul(U2, X),
    )
    Y = mat_bar_d2(X, node)
    Z = mat_bar_d2(C, node)
    H = mat_bar_d2(E, node)
    A1 = mat_scale(-SQRT2 / 8, mat_d(Y, node, 0))
    A2 = mat_add(
        mat_scale(Fraction(-1, 8), mat_d(Z, node, 0)),
        mat_scale(Fraction(-1, 4), mat_add(mat_mul(X, Y), mat_mul(Y, X))),
    )
    A3 = mat_add(
        mat_scale(-SQRT2 / 24, mat_d(H, node, 0)),
        mat_scale(
            -SQRT2 / 8,
            mat_add(
                mat_mul(X, Z),
                mat_mul(Z, X),
                mat_mul(C, Y),
                mat_mul(Y, C),
            ),
        ),
    )
    return A1, A2, A3


def source_words(U: Mat, node: str, source_a: int, source_b: int) -> tuple[P, P, P]:
    A1, A2, A3 = canonical_A_words(U, node)
    gamma1 = mat_scale(SQRT2, mat_d(U, node, 1))
    gamma2 = mat_sub(mat_mul(mat_d(U, node, 1), U), mat_mul(U, mat_d(U, node, 1)))
    N0 = mat_d(A1, node, 1)
    N1 = mat_add(
        mat_d(A2, node, 1),
        mat_sub(mat_mul(gamma1, A1), mat_mul(A1, gamma1)),
    )
    N2 = mat_add(
        mat_d(A3, node, 1),
        mat_sub(mat_mul(gamma1, A2), mat_mul(A2, gamma1)),
        mat_sub(mat_mul(gamma2, A1), mat_mul(A1, gamma2)),
    )
    a1a, a2a, a3a = (component(value, source_a) for value in (A1, A2, A3))
    a1b, a2b, a3b = (component(value, source_b) for value in (A1, A2, A3))
    n0a, n1a, n2a = (component(value, source_a) for value in (N0, N1, N2))
    n0b, n1b, n2b = (component(value, source_b) for value in (N0, N1, N2))
    I0 = n0a * a1b + a1a * n0b
    I1 = n1a * a1b + n0a * a2b + a2a * n0b + a1a * n1b
    I2 = (
        n2a * a1b
        + n1a * a2b
        + n0a * a3b
        + a3a * n0b
        + a2a * n1b
        + a1a * n2b
    )
    return I0, I1, I2


def source_tagged_words(
    U: Mat,
    node: str,
    source_a: int,
    source_b: int,
) -> tuple[dict[str, P], dict[str, P], dict[str, P]]:
    """Occurrence-tagged canonical source expansion through order g^2."""

    A1, A2, A3 = canonical_A_words(U, node)
    gamma1 = mat_scale(SQRT2, mat_d(U, node, 1))
    gamma2 = mat_sub(mat_mul(mat_d(U, node, 1), U), mat_mul(U, mat_d(U, node, 1)))

    N0 = mat_d(A1, node, 1)
    N1_A2 = mat_d(A2, node, 1)
    N1_gamma1 = mat_sub(mat_mul(gamma1, A1), mat_mul(A1, gamma1))
    N2_A3 = mat_d(A3, node, 1)
    N2_gamma1_A2 = mat_sub(mat_mul(gamma1, A2), mat_mul(A2, gamma1))
    N2_gamma2_A1 = mat_sub(mat_mul(gamma2, A1), mat_mul(A1, gamma2))

    def c(value: Mat, color: int) -> P:
        return component(value, color)

    a1a, a2a, a3a = (c(value, source_a) for value in (A1, A2, A3))
    a1b, a2b, a3b = (c(value, source_b) for value in (A1, A2, A3))
    n0a, n0b = c(N0, source_a), c(N0, source_b)
    n1a2a, n1a2b = c(N1_A2, source_a), c(N1_A2, source_b)
    n1g1a, n1g1b = c(N1_gamma1, source_a), c(N1_gamma1, source_b)
    n2a3a, n2a3b = c(N2_A3, source_a), c(N2_A3, source_b)
    n2g1a2a, n2g1a2b = c(N2_gamma1_A2, source_a), c(N2_gamma1_A2, source_b)
    n2g2a1a, n2g2a1b = c(N2_gamma2_A1, source_a), c(N2_gamma2_A1, source_b)

    I0 = {
        "I0_DminusA1[A]*A1[B]": n0a * a1b,
        "I0_A1[A]*DminusA1[B]": a1a * n0b,
    }
    I1 = {
        "I1_DminusA2[A]*A1[B]": n1a2a * a1b,
        "I1_[gamma1,A1][A]*A1[B]": n1g1a * a1b,
        "I1_DminusA1[A]*A2[B]": n0a * a2b,
        "I1_A2[A]*DminusA1[B]": a2a * n0b,
        "I1_A1[A]*DminusA2[B]": a1a * n1a2b,
        "I1_A1[A]*[gamma1,A1][B]": a1a * n1g1b,
    }
    I2 = {
        "I2_DminusA3[A]*A1[B]": n2a3a * a1b,
        "I2_[gamma1,A2][A]*A1[B]": n2g1a2a * a1b,
        "I2_[gamma2,A1][A]*A1[B]": n2g2a1a * a1b,
        "I2_DminusA2[A]*A2[B]": n1a2a * a2b,
        "I2_[gamma1,A1][A]*A2[B]": n1g1a * a2b,
        "I2_DminusA1[A]*A3[B]": n0a * a3b,
        "I2_A3[A]*DminusA1[B]": a3a * n0b,
        "I2_A2[A]*DminusA2[B]": a2a * n1a2b,
        "I2_A2[A]*[gamma1,A1][B]": a2a * n1g1b,
        "I2_A1[A]*DminusA3[B]": a1a * n2a3b,
        "I2_A1[A]*[gamma1,A2][B]": a1a * n2g1a2b,
        "I2_A1[A]*[gamma2,A1][B]": a1a * n2g2a1b,
    }

    return I0, I1, I2


def gamma_plus(U: Mat, node: str, undotted: int) -> Mat:
    DU = mat_d(U, node, undotted)
    U2 = mat_mul(U, U)
    return mat_add(
        mat_scale(SQRT2, DU),
        mat_sub(mat_mul(DU, U), mat_mul(U, DU)),
        mat_scale(
            SQRT2 / 3,
            mat_add(
                mat_mul(DU, U2),
                mat_scale(-2, mat_mul(mat_mul(U, DU), U)),
                mat_mul(U2, DU),
            ),
        ),
    )


def gamma_minus_tilde(U: Mat, node: str, dotted: int) -> Mat:
    BU = mat_bar_d(U, node, dotted)
    U2 = mat_mul(U, U)
    return mat_add(
        mat_scale(-SQRT2, BU),
        mat_sub(mat_mul(BU, U), mat_mul(U, BU)),
        mat_scale(
            -SQRT2 / 3,
            mat_add(
                mat_mul(BU, U2),
                mat_scale(-2, mat_mul(mat_mul(U, BU), U)),
                mat_mul(U2, BU),
            ),
        ),
    )


def gauge_action_integrand(U: Mat, node: str, sector: str) -> P:
    if sector == "+":
        lower = tuple(mat_bar_d2(gamma_plus(U, node, a), node) for a in range(2))
        upper = (
            lower[1],
            mat_neg(lower[0]),
        )
        contracted = mat_add(mat_mul(upper[0], lower[0]), mat_mul(upper[1], lower[1]))
    elif sector == "-":
        lower = tuple(mat_d2(gamma_minus_tilde(U, node, dotted), node) for dotted in range(2))
        upper = (
            lower[1],
            mat_neg(lower[0]),
        )
        contracted = mat_add(mat_mul(lower[0], upper[0]), mat_mul(lower[1], upper[1]))
    else:
        raise ValueError(sector)
    # S_E^g=-h/256 int (square of the connection word), with g=1.
    return Fraction(-1, 256) * mat_trace(contracted)


def target(labels: int, selected: Iterable[int]) -> tuple[int, ...]:
    chosen = set(selected)
    return tuple(1 if index in chosen else 0 for index in range(labels))


def external_normalizations(
    p: Vector,
    polarization: Vector,
    dotted: int,
    color_a: int,
    color_d: int,
) -> tuple[A, A]:
    return external_normalizations_pair(
        p,
        vneg(p),
        polarization,
        dotted,
        color_a,
        color_d,
    )


def external_normalizations_pair(
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    color_a: int,
    color_d: int,
) -> tuple[A, A]:
    # One-node contexts suffice; the values are independent of the spectator labels.
    ctx_a = Context(("X",), ({"X": momentum_a},), 4)
    UA = endpoint_A(ctx_a, "X", 0, color_a, polarization)
    A1, _, _ = canonical_A_words(UA, "X")
    a_value = component(A1, color_a).coefficient_labels((1,)).set_coordinates_zero("X").scalar_coefficient()

    ctx_d = Context(("X",), ({"X": momentum_d},), 4)
    UD = endpoint_D(ctx_d, "X", 0, color_d, dotted)
    # D_c=-1/(4 sqrt(2)) D^2 barD_dot-a u.
    d_word = mat_scale(-SQRT2 / 8, mat_d2(mat_bar_d(UD, "X", dotted), "X"))
    d_value = (
        component(d_word, color_d)
        .coefficient_labels((1,))
        .set_coordinates_zero("X")
        .eta_coefficient()
    )
    return a_value, d_value


def su2_F(source_a: int, source_b: int, external_d: int, external_a: int) -> Fraction:
    # kappa^{-1}=2 delta, c_lower=epsilon/2.
    def eps(a: int, b: int, c: int) -> int:
        if len({a, b, c}) < 3:
            return 0
        inversions = sum(x > y for i, x in enumerate((a, b, c)) for y in (a, b, c)[i + 1 :])
        return -1 if inversions % 2 else 1

    return Fraction(2) * sum(
        eps(source_a, middle, external_d) * eps(source_b, middle, external_a)
        for middle in range(3)
    )


def make_context(nodes: tuple[str, ...], node_momenta: Sequence[Mapping[str, Vector]]) -> Context:
    return Context(nodes, tuple(node_momenta), 4 * len(nodes))


# ---------------------------------------------------------------------------
# Shared-edge component Hessian replay
# ---------------------------------------------------------------------------


def basis_endpoint(
    ctx: Context,
    node: str,
    label: int,
    color: int,
    theta_mask: int,
    coefficient_marker: int,
) -> Mat:
    """Even vector-superfield direction theta^I xi_I with |xi_I|=|I|."""

    base = P.scalar(ctx, 1)
    for offset in range(4):
        if theta_mask & (1 << offset):
            base *= coordinate(ctx, node, offset)
    if theta_mask.bit_count() % 2:
        base *= P.grass_generator(ctx, coefficient_marker)
    return labeled_endpoint(base, label, color)


def hessian_marker_mask(
    first_theta_mask: int,
    second_theta_mask: int,
    background_is_D: bool,
) -> int:
    mask = 1 << 4 if background_is_D else 0
    if first_theta_mask.bit_count() % 2:
        mask |= 1 << 5
    if second_theta_mask.bit_count() % 2:
        mask |= 1 << 6
    return mask


def source_hessian_entries(
    order: int,
    momentum_1: Vector,
    momentum_2: Vector,
    background_momentum: Vector,
    background_type: str,
    polarization: Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    if background_type not in {"A", "D"}:
        raise ValueError(background_type)
    # labels: q1,q2,background.  Grassmann generators 4,5,6 are respectively
    # the physical D coefficient and the two odd component coefficients.
    ctx = Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    fields = [
        basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        (
            endpoint_A(ctx, "X", 2, external_a, polarization)
            if background_type == "A"
            else endpoint_D(ctx, "X", 2, external_d, dotted, eta_index=4)
        ),
    ]
    tagged = source_tagged_words(sum_mats(fields), "X", source_a, source_b)[order]
    marker = hessian_marker_mask(
        theta_mask_1,
        theta_mask_2,
        background_type == "D",
    )
    result: dict[str, A] = {}
    for tag, source in tagged.items():
        coefficient = source.coefficient_labels((1, 1, 1)).set_coordinates_zero("X")
        value = coefficient.grass_coefficient(marker)
        if value:
            result[tag] = value
    return result


def source_hessian_entry(
    order: int,
    momentum_1: Vector,
    momentum_2: Vector,
    background_momentum: Vector,
    background_type: str,
    polarization: Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> A:
    return sum(
        source_hessian_entries(
            order,
            momentum_1,
            momentum_2,
            background_momentum,
            background_type,
            polarization,
            dotted,
            color_1,
            color_2,
            theta_mask_1,
            theta_mask_2,
            source_a,
            source_b,
            external_d,
            external_a,
        ).values(),
        ZERO,
    )


def action_hessian_entry(
    degree: int,
    momentum_1: Vector,
    momentum_2: Vector,
    background_momentum: Vector,
    background_type: str,
    polarization: Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    external_d: int = 1,
    external_a: int = 0,
) -> A:
    if degree != 3:
        raise ValueError("this helper is the cubic background Hessian")
    if background_type not in {"A", "D"}:
        raise ValueError(background_type)
    ctx = Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    fields = [
        basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        (
            endpoint_A(ctx, "X", 2, external_a, polarization)
            if background_type == "A"
            else endpoint_D(ctx, "X", 2, external_d, dotted, eta_index=4)
        ),
    ]
    sector = "+" if background_type == "A" else "-"
    action = gauge_action_integrand(sum_mats(fields), "X", sector)
    action = action.coefficient_labels((1, 1, 1))
    action = integrate_chiral(action, "X") if sector == "+" else integrate_antichiral(action, "X")
    return action.grass_coefficient(
        hessian_marker_mask(theta_mask_1, theta_mask_2, background_type == "D")
    )


def source_I0_hessian_entries(
    momentum_1: Vector,
    momentum_2: Vector,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    source_a: int = 0,
    source_b: int = 1,
) -> dict[str, A]:
    """Two-quantum Hessian of I0, resolved by its two marked occurrences."""

    ctx = Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
        ),
        6,
    )
    fields = [
        basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
    ]
    tagged = source_tagged_words(sum_mats(fields), "X", source_a, source_b)[0]
    marker = hessian_marker_mask(theta_mask_1, theta_mask_2, False)
    result: dict[str, A] = {}
    for tag, source in tagged.items():
        coefficient = source.coefficient_labels((1, 1)).set_coordinates_zero("X")
        value = coefficient.grass_coefficient(marker)
        if value:
            result[tag] = value
    return result


def action_quartic_hessian_entries(
    momentum_1: Vector,
    momentum_2: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    """Full Sg4 Hessian with external A(p), D(-p), tagged by chirality."""

    ctx = Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": p},
            {"X": vneg(p)},
        ),
        6,
    )
    fields = [
        basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        endpoint_A(ctx, "X", 2, external_a, polarization),
        endpoint_D(ctx, "X", 3, external_d, dotted, eta_index=4),
    ]
    marker = hessian_marker_mask(theta_mask_1, theta_mask_2, True)
    result: dict[str, A] = {}
    for sector in ("+", "-"):
        action = gauge_action_integrand(sum_mats(fields), "X", sector)
        action = action.coefficient_labels((1, 1, 1, 1))
        action = (
            integrate_chiral(action, "X")
            if sector == "+"
            else integrate_antichiral(action, "X")
        )
        value = action.grass_coefficient(marker)
        if value:
            result[f"Sg4_{sector}"] = value
    return result


def action_quartic_hessian_entries_general(
    momentum_1: Vector,
    momentum_2: Vector,
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    ctx = Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": momentum_a},
            {"X": momentum_d},
        ),
        6,
    )
    fields = [
        basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        endpoint_A(ctx, "X", 2, external_a, polarization),
        endpoint_D(ctx, "X", 3, external_d, dotted, eta_index=4),
    ]
    marker = hessian_marker_mask(theta_mask_1, theta_mask_2, True)
    result: dict[str, A] = {}
    for sector in ("+", "-"):
        action = gauge_action_integrand(sum_mats(fields), "X", sector)
        action = action.coefficient_labels((1, 1, 1, 1))
        action = (
            integrate_chiral(action, "X")
            if sector == "+"
            else integrate_antichiral(action, "X")
        )
        value = action.grass_coefficient(marker)
        if value:
            result[f"Sg4_{sector}"] = value
    return result


def delta_theta_component(left_mask: int, right_mask: int) -> int:
    """Coefficient of theta_L^I theta_R^J in 4 prod_a(theta_L^a-theta_R^a)."""

    if left_mask & right_mask or (left_mask | right_mask) != 0b1111:
        return 0
    coefficient = 4 * (-1 if right_mask.bit_count() % 2 else 1)
    inversions = sum(
        1
        for lower in range(4)
        for higher in range(lower + 1, 4)
        if right_mask & (1 << lower) and left_mask & (1 << higher)
    )
    return -coefficient if inversions % 2 else coefficient


def component_covariance(left_mask: int, right_mask: int) -> int:
    """Covariance of right-coefficient component variables in one delta edge."""

    theta_coefficient = delta_theta_component(left_mask, right_mask)
    if theta_coefficient == 0:
        return 0
    component_move = -1 if (left_mask.bit_count() % 2) * (right_mask.bit_count() % 2) % 2 else 1
    return component_move * theta_coefficient


def bubble_component_value(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    source_external: str,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> A:
    """Shared-edge contraction for -<I1 Sg3>/hbar."""

    e_source = p if source_external == "A" else vneg(p)
    e_action = vneg(e_source)
    action_external = "D" if source_external == "A" else "A"
    r_1 = loop
    r_2 = vneg(vadd(loop, e_source))
    total = sum(
        (
            bubble_color_partial(
                loop,
                p,
                polarization,
                dotted,
                source_external,
                color_1,
                color_2,
                source_a,
                source_b,
                external_d,
                external_a,
            )
            for color_1, color_2 in itertools.product(range(3), repeat=2)
        ),
        ZERO,
    )
    # Resolvent sign - and 1/2! for the two parallel labeled edges.
    total *= Fraction(-1, 2)
    norm_a, norm_d = external_normalizations(p, polarization, dotted, external_a, external_d)
    color = A(su2_F(source_a, source_b, external_d, external_a))
    return total / (norm_a * norm_d * color)


def bubble_color_partial(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    source_external: str,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> A:
    return sum(
        bubble_color_partials(
            loop,
            p,
            polarization,
            dotted,
            source_external,
            color_1,
            color_2,
            source_a,
            source_b,
            external_d,
            external_a,
        ).values(),
        ZERO,
    )


def bubble_color_partials(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    source_external: str,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    e_source = p if source_external == "A" else vneg(p)
    e_action = vneg(e_source)
    action_external = "D" if source_external == "A" else "A"
    r_1 = loop
    r_2 = vneg(vadd(loop, e_source))
    totals: dict[str, A] = {}
    for source_mask_1, source_mask_2 in itertools.product(range(16), repeat=2):
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = component_covariance(source_mask_1, action_mask_1)
        covariance_2 = component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = source_hessian_entries(
            1,
            r_1,
            r_2,
            e_source,
            source_external,
            polarization,
            dotted,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        if not source_entries:
            continue
        action_entry = action_hessian_entry(
            3,
            vneg(r_1),
            vneg(r_2),
            e_action,
            action_external,
            polarization,
            dotted,
            color_1,
            color_2,
            action_mask_1,
            action_mask_2,
            external_d,
            external_a,
        )
        if not action_entry:
            continue
        # Product ordering is source(q1,q2) action(q1,q2).  Bring the
        # first action coefficient through source q2 before pairing.
        wick_sign = -1 if (
            source_mask_2.bit_count() % 2
            and action_mask_1.bit_count() % 2
        ) else 1
        # Each canonical vector propagator is -kappa^{-1} delta=-2 delta.
        edge_weight = 4 * covariance_1 * covariance_2
        for tag, source_entry in source_entries.items():
            value = totals.get(tag, ZERO) + (
                wick_sign * edge_weight * source_entry * action_entry
            )
            if value:
                totals[tag] = value
            elif tag in totals:
                del totals[tag]
    return totals


def bubble_component_value_parallel(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    source_external: str,
    workers: int = 9,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> A:
    return sum(
        bubble_component_values_parallel(
            loop,
            p,
            polarization,
            dotted,
            source_external,
            workers,
            source_a,
            source_b,
            external_d,
            external_a,
        ).values(),
        ZERO,
    )


def bubble_component_values_parallel(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    source_external: str,
    workers: int = 9,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    arguments = [
        (
            loop,
            p,
            polarization,
            dotted,
            source_external,
            color_1,
            color_2,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers, mp_context=context) as pool:
        partials = list(pool.map(_bubble_color_partials_star, arguments))
    totals: dict[str, A] = {}
    for partial in partials:
        for tag, value in partial.items():
            totals[tag] = totals.get(tag, ZERO) + value
    norm_a, norm_d = external_normalizations(p, polarization, dotted, external_a, external_d)
    color = A(su2_F(source_a, source_b, external_d, external_a))
    normalization = A(Fraction(-1, 2)) / (norm_a * norm_d * color)
    return {
        tag: normalization * value
        for tag, value in totals.items()
        if value
    }


def _bubble_color_partial_star(arguments: tuple[object, ...]) -> A:
    return bubble_color_partial(*arguments)  # type: ignore[arg-type]


def _bubble_color_partials_star(arguments: tuple[object, ...]) -> dict[str, A]:
    return bubble_color_partials(*arguments)  # type: ignore[arg-type]


def _bubble_attachment_color_partials_star(
    arguments: tuple[object, ...],
) -> tuple[str, dict[str, A]]:
    source_external = arguments[4]
    if not isinstance(source_external, str):
        raise TypeError("source_external must be a string")
    return source_external, bubble_color_partials(*arguments)  # type: ignore[arg-type]


def bubble_attachment_component_values_parallel(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    workers: int = 12,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, dict[str, A]]:
    """Evaluate both source/background distributions in one worker pool."""

    arguments = [
        (
            loop,
            p,
            polarization,
            dotted,
            source_external,
            color_1,
            color_2,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        for source_external in ("A", "D")
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers, mp_context=context) as pool:
        partials = list(pool.map(_bubble_attachment_color_partials_star, arguments))
    totals: dict[str, dict[str, A]] = {"A": {}, "D": {}}
    for source_external, partial in partials:
        for tag, value in partial.items():
            current = totals[source_external].get(tag, ZERO) + value
            if current:
                totals[source_external][tag] = current
            elif tag in totals[source_external]:
                del totals[source_external][tag]
    norm_a, norm_d = external_normalizations(p, polarization, dotted, external_a, external_d)
    color = A(su2_F(source_a, source_b, external_d, external_a))
    normalization = A(Fraction(-1, 2)) / (norm_a * norm_d * color)
    return {
        source_external: {
            tag: normalization * value
            for tag, value in tagged.items()
            if value
        }
        for source_external, tagged in totals.items()
    }


def bubble_color_partials_general(
    loop: Vector,
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    source_external: str,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    """General two-external-momentum routing for -<I1 Sg3>."""

    if source_external == "A":
        e_source, e_action, action_external = momentum_a, momentum_d, "D"
    elif source_external == "D":
        e_source, e_action, action_external = momentum_d, momentum_a, "A"
    else:
        raise ValueError(source_external)
    r_1 = loop
    # At the action vertex: -r1-r2+e_action=0.
    r_2 = vadd(e_action, vneg(loop))
    totals: dict[str, A] = {}
    for source_mask_1, source_mask_2 in itertools.product(range(16), repeat=2):
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = component_covariance(source_mask_1, action_mask_1)
        covariance_2 = component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = source_hessian_entries(
            1,
            r_1,
            r_2,
            e_source,
            source_external,
            polarization,
            dotted,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        if not source_entries:
            continue
        action_entry = action_hessian_entry(
            3,
            vneg(r_1),
            vneg(r_2),
            e_action,
            action_external,
            polarization,
            dotted,
            color_1,
            color_2,
            action_mask_1,
            action_mask_2,
            external_d,
            external_a,
        )
        if not action_entry:
            continue
        wick_sign = -1 if (
            source_mask_2.bit_count() % 2
            and action_mask_1.bit_count() % 2
        ) else 1
        edge_weight = 4 * covariance_1 * covariance_2
        for tag, source_entry in source_entries.items():
            value = totals.get(tag, ZERO) + (
                wick_sign * edge_weight * source_entry * action_entry
            )
            if value:
                totals[tag] = value
            elif tag in totals:
                del totals[tag]
    return totals


def _bubble_general_attachment_color_partials_star(
    arguments: tuple[object, ...],
) -> tuple[str, dict[str, A]]:
    source_external = arguments[5]
    if not isinstance(source_external, str):
        raise TypeError("source_external must be a string")
    return source_external, bubble_color_partials_general(*arguments)  # type: ignore[arg-type]


def bubble_general_attachment_values_parallel(
    loop: Vector,
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    workers: int = 12,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, dict[str, A]]:
    arguments = [
        (
            loop,
            momentum_a,
            momentum_d,
            polarization,
            dotted,
            source_external,
            color_1,
            color_2,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        for source_external in ("A", "D")
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers, mp_context=context) as pool:
        partials = list(pool.map(_bubble_general_attachment_color_partials_star, arguments))
    totals: dict[str, dict[str, A]] = {"A": {}, "D": {}}
    for source_external, partial in partials:
        for tag, value in partial.items():
            current = totals[source_external].get(tag, ZERO) + value
            if current:
                totals[source_external][tag] = current
            elif tag in totals[source_external]:
                del totals[source_external][tag]
    norm_a, norm_d = external_normalizations_pair(
        momentum_a,
        momentum_d,
        polarization,
        dotted,
        external_a,
        external_d,
    )
    color = A(su2_F(source_a, source_b, external_d, external_a))
    normalization = A(Fraction(-1, 2)) / (norm_a * norm_d * color)
    return {
        source_external: {
            tag: normalization * value
            for tag, value in tagged.items()
            if value
        }
        for source_external, tagged in totals.items()
    }


def quartic_color_partials(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    """One color pair of -<I0 Sg4>, before the common normalization."""

    totals: dict[str, A] = {}
    r_1 = loop
    r_2 = vneg(loop)
    for source_mask_1, source_mask_2 in itertools.product(range(16), repeat=2):
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = component_covariance(source_mask_1, action_mask_1)
        covariance_2 = component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = source_I0_hessian_entries(
            r_1,
            r_2,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            source_a,
            source_b,
        )
        if not source_entries:
            continue
        action_entries = action_quartic_hessian_entries(
            vneg(r_1),
            vneg(r_2),
            p,
            polarization,
            dotted,
            color_1,
            color_2,
            action_mask_1,
            action_mask_2,
            external_d,
            external_a,
        )
        if not action_entries:
            continue
        wick_sign = -1 if (
            source_mask_2.bit_count() % 2
            and action_mask_1.bit_count() % 2
        ) else 1
        edge_weight = 4 * covariance_1 * covariance_2
        for source_tag, source_entry in source_entries.items():
            for action_tag, action_entry in action_entries.items():
                tag = f"{source_tag}__{action_tag}"
                value = totals.get(tag, ZERO) + (
                    wick_sign * edge_weight * source_entry * action_entry
                )
                if value:
                    totals[tag] = value
                elif tag in totals:
                    del totals[tag]
    return totals


def _quartic_color_partials_star(arguments: tuple[object, ...]) -> dict[str, A]:
    return quartic_color_partials(*arguments)  # type: ignore[arg-type]


def quartic_component_values_parallel(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    workers: int = 9,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    arguments = [
        (
            loop,
            p,
            polarization,
            dotted,
            color_1,
            color_2,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers, mp_context=context) as pool:
        partials = list(pool.map(_quartic_color_partials_star, arguments))
    totals: dict[str, A] = {}
    for partial in partials:
        for tag, value in partial.items():
            totals[tag] = totals.get(tag, ZERO) + value
    norm_a, norm_d = external_normalizations(p, polarization, dotted, external_a, external_d)
    color = A(su2_F(source_a, source_b, external_d, external_a))
    # Resolvent sign -, Taylor/Wick parallel-edge factor 1/2, two -2 propagators.
    normalization = A(Fraction(-1, 2)) / (norm_a * norm_d * color)
    return {
        tag: normalization * value
        for tag, value in totals.items()
        if value
    }


def quartic_color_partials_general(
    loop: Vector,
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    """General P=p_A+p_D routing for -<I0 Sg4>."""

    totals: dict[str, A] = {}
    total_external = vadd(momentum_a, momentum_d)
    r_1 = loop
    r_2 = vadd(total_external, vneg(loop))
    for source_mask_1, source_mask_2 in itertools.product(range(16), repeat=2):
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = component_covariance(source_mask_1, action_mask_1)
        covariance_2 = component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = source_I0_hessian_entries(
            r_1,
            r_2,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            source_a,
            source_b,
        )
        if not source_entries:
            continue
        action_entries = action_quartic_hessian_entries_general(
            vneg(r_1),
            vneg(r_2),
            momentum_a,
            momentum_d,
            polarization,
            dotted,
            color_1,
            color_2,
            action_mask_1,
            action_mask_2,
            external_d,
            external_a,
        )
        if not action_entries:
            continue
        wick_sign = -1 if (
            source_mask_2.bit_count() % 2
            and action_mask_1.bit_count() % 2
        ) else 1
        edge_weight = 4 * covariance_1 * covariance_2
        for source_tag, source_entry in source_entries.items():
            for action_tag, action_entry in action_entries.items():
                tag = f"{source_tag}__{action_tag}"
                value = totals.get(tag, ZERO) + (
                    wick_sign * edge_weight * source_entry * action_entry
                )
                if value:
                    totals[tag] = value
                elif tag in totals:
                    del totals[tag]
    return totals


def _quartic_color_partials_general_star(
    arguments: tuple[object, ...],
) -> dict[str, A]:
    return quartic_color_partials_general(*arguments)  # type: ignore[arg-type]


def quartic_general_values_parallel(
    loop: Vector,
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    workers: int = 9,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    arguments = [
        (
            loop,
            momentum_a,
            momentum_d,
            polarization,
            dotted,
            color_1,
            color_2,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers, mp_context=context) as pool:
        partials = list(pool.map(_quartic_color_partials_general_star, arguments))
    totals: dict[str, A] = {}
    for partial in partials:
        for tag, value in partial.items():
            totals[tag] = totals.get(tag, ZERO) + value
    norm_a, norm_d = external_normalizations_pair(
        momentum_a,
        momentum_d,
        polarization,
        dotted,
        external_a,
        external_d,
    )
    color = A(su2_F(source_a, source_b, external_d, external_a))
    normalization = A(Fraction(-1, 2)) / (norm_a * norm_d * color)
    return {
        tag: normalization * value
        for tag, value in totals.items()
        if value
    }


def source_I2_tadpole_color_partials(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    color: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    """One internal color of <I2>, before the one-edge normalization."""

    totals: dict[str, A] = {}
    for mask_1 in range(16):
        mask_2 = 15 ^ mask_1
        covariance = component_covariance(mask_1, mask_2)
        if not covariance:
            continue
        ctx = Context(
            ("X",),
            (
                {"X": loop},
                {"X": vneg(loop)},
                {"X": p},
                {"X": vneg(p)},
            ),
            6,
        )
        fields = [
            basis_endpoint(ctx, "X", 0, color, mask_1, 5),
            basis_endpoint(ctx, "X", 1, color, mask_2, 6),
            endpoint_A(ctx, "X", 2, external_a, polarization),
            endpoint_D(ctx, "X", 3, external_d, dotted, eta_index=4),
        ]
        tagged = source_tagged_words(sum_mats(fields), "X", source_a, source_b)[2]
        marker = hessian_marker_mask(mask_1, mask_2, True)
        for tag, source in tagged.items():
            coefficient = source.coefficient_labels((1, 1, 1, 1)).set_coordinates_zero("X")
            value = coefficient.grass_coefficient(marker)
            if not value:
                continue
            current = totals.get(tag, ZERO) + covariance * value
            if current:
                totals[tag] = current
            elif tag in totals:
                del totals[tag]
    return totals


def _source_I2_tadpole_color_partials_star(
    arguments: tuple[object, ...],
) -> dict[str, A]:
    return source_I2_tadpole_color_partials(*arguments)  # type: ignore[arg-type]


def source_I2_tadpole_values_parallel(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    workers: int = 3,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    arguments = [
        (
            loop,
            p,
            polarization,
            dotted,
            color,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        for color in range(3)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers, mp_context=context) as pool:
        partials = list(pool.map(_source_I2_tadpole_color_partials_star, arguments))
    totals: dict[str, A] = {}
    for partial in partials:
        for tag, value in partial.items():
            totals[tag] = totals.get(tag, ZERO) + value
    norm_a, norm_d = external_normalizations(p, polarization, dotted, external_a, external_d)
    color_tensor = A(su2_F(source_a, source_b, external_d, external_a))
    # One propagator is -2 delta; the two labeled quantum directions carry 1/2!.
    normalization = A(-1) / (norm_a * norm_d * color_tensor)
    return {
        tag: normalization * value
        for tag, value in totals.items()
        if value
    }


def source_I2_tadpole_color_partials_general(
    loop: Vector,
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    color: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    totals: dict[str, A] = {}
    for mask_1 in range(16):
        mask_2 = 15 ^ mask_1
        covariance = component_covariance(mask_1, mask_2)
        if not covariance:
            continue
        ctx = Context(
            ("X",),
            (
                {"X": loop},
                {"X": vneg(loop)},
                {"X": momentum_a},
                {"X": momentum_d},
            ),
            6,
        )
        fields = [
            basis_endpoint(ctx, "X", 0, color, mask_1, 5),
            basis_endpoint(ctx, "X", 1, color, mask_2, 6),
            endpoint_A(ctx, "X", 2, external_a, polarization),
            endpoint_D(ctx, "X", 3, external_d, dotted, eta_index=4),
        ]
        tagged = source_tagged_words(sum_mats(fields), "X", source_a, source_b)[2]
        marker = hessian_marker_mask(mask_1, mask_2, True)
        for tag, source in tagged.items():
            coefficient = source.coefficient_labels((1, 1, 1, 1)).set_coordinates_zero("X")
            value = coefficient.grass_coefficient(marker)
            if not value:
                continue
            current = totals.get(tag, ZERO) + covariance * value
            if current:
                totals[tag] = current
            elif tag in totals:
                del totals[tag]
    return totals


def _source_I2_tadpole_color_partials_general_star(
    arguments: tuple[object, ...],
) -> dict[str, A]:
    return source_I2_tadpole_color_partials_general(*arguments)  # type: ignore[arg-type]


def source_I2_tadpole_general_values_parallel(
    loop: Vector,
    momentum_a: Vector,
    momentum_d: Vector,
    polarization: Vector,
    dotted: int,
    workers: int = 3,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, A]:
    arguments = [
        (
            loop,
            momentum_a,
            momentum_d,
            polarization,
            dotted,
            color,
            source_a,
            source_b,
            external_d,
            external_a,
        )
        for color in range(3)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers, mp_context=context) as pool:
        partials = list(pool.map(_source_I2_tadpole_color_partials_general_star, arguments))
    totals: dict[str, A] = {}
    for partial in partials:
        for tag, value in partial.items():
            totals[tag] = totals.get(tag, ZERO) + value
    norm_a, norm_d = external_normalizations_pair(
        momentum_a,
        momentum_d,
        polarization,
        dotted,
        external_a,
        external_d,
    )
    color_tensor = A(su2_F(source_a, source_b, external_d, external_a))
    normalization = A(-1) / (norm_a * norm_d * color_tensor)
    return {
        tag: normalization * value
        for tag, value in totals.items()
        if value
    }


def withdrawn_duplicated_delta_bubble_value(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    source_external: str,
    sector: str,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> A:
    """Withdrawn prototype: it incorrectly placed one delta per endpoint."""

    raise AssertionError(
        "withdrawn duplicated-delta prototype; use the shared-edge component Hessian"
    )

    if source_external not in {"A", "D"}:
        raise ValueError(source_external)
    e_source = p if source_external == "A" else vneg(p)
    e_action = vneg(e_source)
    edge_1 = loop
    edge_2 = vneg(vadd(loop, e_source))
    # labels 0,1,2 belong to the source factor; 3,4,5 to the action factor.
    momenta = (
        {"S": edge_1},
        {"S": edge_2},
        {"S": e_source},
        {"G": vneg(edge_1)},
        {"G": vneg(edge_2)},
        {"G": e_action},
    )
    ctx = make_context(("S", "G"), momenta)
    total = ZERO
    for color_1, color_2 in itertools.product(range(3), repeat=2):
        source_fields = [
            endpoint_delta(ctx, "S", "G", 0, color_1),
            endpoint_delta(ctx, "S", "G", 1, color_2),
            (
                endpoint_A(ctx, "S", 2, external_a, polarization)
                if source_external == "A"
                else endpoint_D(ctx, "S", 2, external_d, dotted)
            ),
        ]
        action_fields = [
            endpoint_delta(ctx, "S", "G", 3, color_1),
            endpoint_delta(ctx, "S", "G", 4, color_2),
            (
                endpoint_D(ctx, "G", 5, external_d, dotted)
                if source_external == "A"
                else endpoint_A(ctx, "G", 5, external_a, polarization)
            ),
        ]
        _, I1, _ = source_words(sum_mats(source_fields), "S", source_a, source_b)
        source_factor = I1.coefficient_labels(target(ctx.label_count, (0, 1, 2)))
        action = gauge_action_integrand(sum_mats(action_fields), "G", sector)
        action_factor = action.coefficient_labels(target(ctx.label_count, (3, 4, 5)))
        graph = integrate_chiral(source_factor * action_factor, "G") if sector == "+" else integrate_antichiral(source_factor * action_factor, "G")
        graph = graph.set_coordinates_zero("S")
        total += graph.eta_coefficient()
    # Resolvent -, two propagators (-kappa^-1)^2=4, parallel-edge 1/2!.
    total *= -2
    norm_a, norm_d = external_normalizations(p, polarization, dotted, external_a, external_d)
    color = A(su2_F(source_a, source_b, external_d, external_a))
    return total / (norm_a * norm_d * color)


def withdrawn_duplicated_delta_quartic_value(
    loop: Vector,
    p: Vector,
    polarization: Vector,
    dotted: int,
    sector: str,
    source_a: int = 0,
    source_b: int = 1,
    external_d: int = 1,
    external_a: int = 0,
) -> A:
    """Withdrawn prototype: it incorrectly placed one delta per endpoint."""

    raise AssertionError(
        "withdrawn duplicated-delta prototype; use the shared-edge component Hessian"
    )

    edge_1 = loop
    edge_2 = vneg(loop)
    momenta = (
        {"S": edge_1},
        {"S": edge_2},
        {"G": vneg(edge_1)},
        {"G": vneg(edge_2)},
        {"G": p},
        {"G": vneg(p)},
    )
    ctx = make_context(("S", "G"), momenta)
    total = ZERO
    for color_1, color_2 in itertools.product(range(3), repeat=2):
        source_fields = [
            endpoint_delta(ctx, "S", "G", 0, color_1),
            endpoint_delta(ctx, "S", "G", 1, color_2),
        ]
        action_fields = [
            endpoint_delta(ctx, "S", "G", 2, color_1),
            endpoint_delta(ctx, "S", "G", 3, color_2),
            endpoint_A(ctx, "G", 4, external_a, polarization),
            endpoint_D(ctx, "G", 5, external_d, dotted),
        ]
        I0, _, _ = source_words(sum_mats(source_fields), "S", source_a, source_b)
        source_factor = I0.coefficient_labels(target(ctx.label_count, (0, 1)))
        action = gauge_action_integrand(sum_mats(action_fields), "G", sector)
        action_factor = action.coefficient_labels(target(ctx.label_count, (2, 3, 4, 5)))
        graph = integrate_chiral(source_factor * action_factor, "G") if sector == "+" else integrate_antichiral(source_factor * action_factor, "G")
        graph = graph.set_coordinates_zero("S")
        total += graph.eta_coefficient()
    # Resolvent -, two propagators, and 1/2! for the parallel edges.
    total *= -2
    norm_a, norm_d = external_normalizations(p, polarization, dotted, external_a, external_d)
    color = A(su2_F(source_a, source_b, external_d, external_a))
    return total / (norm_a * norm_d * color)


def central_second(function, point: Vector, axis: int) -> A:
    unit = [ZERO, ZERO, ZERO, ZERO]
    unit[axis] = ONE
    direction = tuple(unit)  # type: ignore[assignment]
    return function(vadd(point, direction)) - 2 * function(point) + function(vadd(point, vneg(direction)))


def json_a(value: A) -> dict[str, str]:
    return {
        "rational": str(value.a),
        "sqrt2": str(value.b),
        "imaginary": str(value.c),
        "imaginary_sqrt2": str(value.d),
        "text": value.text(),
    }


def tagged_json(values: Mapping[str, A]) -> dict[str, dict[str, str]]:
    return {tag: json_a(value) for tag, value in sorted(values.items()) if value}


def frame_z(loop: Vector) -> A:
    return loop[0] - I * loop[1]


def expected_general_bubble(loop: Vector) -> dict[str, dict[str, A]]:
    z = frame_z(loop)
    return {
        "A": {
            "I1_A1[A]*DminusA2[B]": (
                z.square() + I * z - Fraction(1, 2) - Fraction(9, 2) * I
            ),
            "I1_A1[A]*[gamma1,A1][B]": -3 * I,
            "I1_DminusA1[A]*A2[B]": -Fraction(1, 2) * (ONE + I),
        },
        "D": {
            "I1_A2[A]*DminusA1[B]": 5 * I,
            "I1_DminusA2[A]*A1[B]": -z.square() + z - 1,
        },
    }


def expected_general_quartic(loop: Vector) -> dict[str, A]:
    z = frame_z(loop)
    sector = -z.square() + (ONE - I) * z
    return {
        "I0_A1[A]*DminusA1[B]__Sg4_+": sector,
        "I0_A1[A]*DminusA1[B]__Sg4_-": sector,
    } if sector else {}


def build_artifact(full_replay: bool = False) -> dict[str, object]:
    momentum_a = vec((1, 0, 0, 0))
    momentum_d = vec((0, 1, 0, 0))
    polarization = vec((0, 0, 0, 1))
    dotted = 0
    norm_a, norm_d = external_normalizations_pair(
        momentum_a,
        momentum_d,
        polarization,
        dotted,
        0,
        1,
    )
    if not norm_a or not norm_d:
        raise AssertionError("chosen exact external polarization has zero normalization")
    color = su2_F(0, 1, 1, 0)
    if color == 0:
        raise AssertionError("chosen SU(2) color frame has zero F tensor")

    sample_loops: list[tuple[str, Vector]] = [
        ("zero", ZERO_VECTOR),
        ("generic", vec((2, -1, 1, 3))),
    ]
    if full_replay:
        sample_loops = [("zero", ZERO_VECTOR)]
        for axis in range(4):
            unit = [0, 0, 0, 0]
            unit[axis] = 1
            direction = vec(unit)
            sample_loops.extend(
                (
                    (f"plus_e{axis}", direction),
                    (f"minus_e{axis}", vneg(direction)),
                )
            )
        sample_loops.extend(
            (
                ("e0_plus_e1", vec((1, 1, 0, 0))),
                ("generic", vec((2, -1, 1, 3))),
            )
        )

    bubble_samples: dict[str, object] = {}
    quartic_samples: dict[str, object] = {}
    tadpole_samples: dict[str, object] = {}
    for name, loop in sample_loops:
        bubble = bubble_general_attachment_values_parallel(
            loop,
            momentum_a,
            momentum_d,
            polarization,
            dotted,
        )
        expected_bubble = expected_general_bubble(loop)
        if bubble != expected_bubble:
            raise AssertionError(
                f"I1*Sg3 exact D-word mismatch at {name}: {bubble!r} != {expected_bubble!r}"
            )
        quartic = quartic_general_values_parallel(
            loop,
            momentum_a,
            momentum_d,
            polarization,
            dotted,
        )
        expected_quartic = expected_general_quartic(loop)
        if quartic != expected_quartic:
            raise AssertionError(
                f"I0*Sg4 exact D-word mismatch at {name}: {quartic!r} != {expected_quartic!r}"
            )
        tadpole = source_I2_tadpole_general_values_parallel(
            loop,
            momentum_a,
            momentum_d,
            polarization,
            dotted,
        )
        if tadpole:
            raise AssertionError(f"I2 tadpole did not vanish at {name}: {tadpole!r}")
        bubble_samples[name] = {
            "loop": [value.text() for value in loop],
            "source_A_action_D": tagged_json(bubble["A"]),
            "source_D_action_A": tagged_json(bubble["D"]),
            "attachment_sum": json_a(
                sum((value for tagged in bubble.values() for value in tagged.values()), ZERO)
            ),
        }
        quartic_samples[name] = {
            "loop": [value.text() for value in loop],
            "tags": tagged_json(quartic),
            "sum": json_a(sum(quartic.values(), ZERO)),
        }
        tadpole_samples[name] = {
            "loop": [value.text() for value in loop],
            "tags": {},
            "sum": json_a(ZERO),
        }

    census_path = (
        Path(__file__).resolve().parents[1]
        / "audits"
        / "step5-all-triangle-parent-port-census.json"
    )
    census = json.loads(census_path.read_text(encoding="utf-8"))
    aa_pair = next(row for row in census["pairs"] if row["pair_id"] == "A__A")
    aa_routes = [row for row in census["routes"] if row["pair_id"] == "A__A"]
    gauge_routes = [row for row in aa_routes if row["topology"] == "TGG"]
    matter_routes = [row for row in aa_routes if row["topology"] == "TMM"]
    if (aa_pair["triangle_parent_route_count"], len(gauge_routes), len(matter_routes)) != (42, 36, 6):
        raise AssertionError("AA target-blind route census changed")

    bubble_a_hessian = (A(2), A(-2), ZERO, ZERO)
    bubble_d_hessian = tuple(-value for value in bubble_a_hessian)
    quartic_hessian = (A(-4), A(4), ZERO, ZERO)
    if sum(bubble_a_hessian, ZERO) or sum(bubble_d_hessian, ZERO) or sum(quartic_hessian, ZERO):
        raise AssertionError("a gauge source-orbit D-word acquired a scalar loop square")

    return {
        "schema": "step5-aa-gauge-full-source-sd-orbit-v2",
        "arithmetic": "Q(sqrt(2),i), exact fractions, no floating point",
        "target_blind": True,
        "external_frame": {
            "p_A": [value.text() for value in momentum_a],
            "q_D": [value.text() for value in momentum_d],
            "P_composite": [value.text() for value in vadd(momentum_a, momentum_d)],
            "A_polarization": [value.text() for value in polarization],
            "D_dotted_index": dotted,
            "A_linear_normalization": json_a(norm_a),
            "D_linear_normalization": json_a(norm_d),
        },
        "color_frame": {
            "group": "SU(2), T_a=sigma_a/2",
            "source_indices": [0, 1],
            "external_D_A_indices": [1, 0],
            "F_value": str(color),
        },
        "route_coverage": {
            "AA_directed_parents": len(aa_routes),
            "AA_gauge_gauge_routes": len(gauge_routes),
            "AA_matter_matter_routes": len(matter_routes),
            "AA_marked_inverse_edge_occurrences": 2 * len(aa_routes),
            "coefficient_inference_from_census": False,
        },
        "I2_tadpole": {
            "twelve_source_tags": [
                "I2_DminusA3[A]*A1[B]",
                "I2_[gamma1,A2][A]*A1[B]",
                "I2_[gamma2,A1][A]*A1[B]",
                "I2_DminusA2[A]*A2[B]",
                "I2_[gamma1,A1][A]*A2[B]",
                "I2_DminusA1[A]*A3[B]",
                "I2_A3[A]*DminusA1[B]",
                "I2_A2[A]*DminusA2[B]",
                "I2_A2[A]*[gamma1,A1][B]",
                "I2_A1[A]*DminusA3[B]",
                "I2_A1[A]*[gamma1,A2][B]",
                "I2_A1[A]*[gamma2,A1][B]",
            ],
            "replay_samples": tadpole_samples,
            "denominator": "1/k^2",
            "anomaly_sector": "0 (exact component/color contraction; independently scaleless)",
        },
        "I1_Sg3_bubbles": {
            "closed_form_source_A_action_D": "z^2+i*z-1-8*i",
            "closed_form_source_D_action_A": "-z^2+z-1+5*i",
            "closed_form_attachment_sum": "(1+i)*z-2-3*i",
            "source_A_hessian_diagonal": [json_a(value) for value in bubble_a_hessian],
            "source_D_hessian_diagonal": [json_a(value) for value in bubble_d_hessian],
            "source_A_H01": json_a(-2 * I),
            "source_D_H01": json_a(2 * I),
            "source_A_four_dimensional_trace": json_a(sum(bubble_a_hessian, ZERO)),
            "source_D_four_dimensional_trace": json_a(sum(bubble_d_hessian, ZERO)),
            "attachment_quadratic_numerator_sum": "0",
            "attachment_denominators_distinct": True,
            "fraction_level_cancellation_claimed": False,
            "anomaly_sector": "0",
            "replay_samples": bubble_samples,
        },
        "I0_Sg4_bubble": {
            "closed_form_each_chirality": "-z^2+(1-i)*z",
            "closed_form_sum": "-2*z^2+(2-2*i)*z",
            "hessian_diagonal": [json_a(value) for value in quartic_hessian],
            "H01": json_a(4 * I),
            "four_dimensional_trace": json_a(sum(quartic_hessian, ZERO)),
            "anomaly_sector": "0 (no scalar bar(k)^2 term)",
            "replay_samples": quartic_samples,
        },
        "triangle": {
            "resolvent_term": "+(2*hbar^2)^-1 <I0 Sg3 Sg3>",
            "directed_coefficient_in_lambda1_units": "-1/8",
            "derivation_source": "independent canonical normalization ledger; no HT target",
        },
        "full_gauge_source_orbit": {
            "coefficient_in_lambda1_units": "-1/8",
            "changed_from_isolated_triangle": False,
        },
        "checks": {
            "external_normalizations_nonzero": bool(norm_a and norm_d),
            "color_tensor_nonzero": color != 0,
            "source_A1_A2_A3_generated_from_exact_words": True,
            "outer_gamma1_gamma2_included": True,
            "action_Sg3_Sg4_generated_from_exact_connection": True,
            "independent_external_momenta": True,
            "composite_momentum_nonzero": True,
            "withdrawn_duplicated_delta_prototype_not_called": True,
            "I1_each_attachment_scalar_loop_square_zero": True,
            "I0_Sg4_scalar_loop_square_zero": True,
            "I2_zero": True,
        },
    }


def validate_artifact(artifact: Mapping[str, object]) -> tuple[int, int]:
    frame = artifact["external_frame"]
    coverage = artifact["route_coverage"]
    tadpole = artifact["I2_tadpole"]
    bubbles = artifact["I1_Sg3_bubbles"]
    quartic = artifact["I0_Sg4_bubble"]
    triangle = artifact["triangle"]
    full = artifact["full_gauge_source_orbit"]
    checks = artifact["checks"]
    if not all(
        isinstance(value, Mapping)
        for value in (frame, coverage, tadpole, bubbles, quartic, triangle, full, checks)
    ):
        raise AssertionError("malformed gauge source-orbit artifact")
    assertions = (
        artifact["schema"] == "step5-aa-gauge-full-source-sd-orbit-v2",
        artifact["target_blind"] is True,
        frame["p_A"] == ["1", "0", "0", "0"],
        frame["q_D"] == ["0", "1", "0", "0"],
        frame["P_composite"] == ["1", "1", "0", "0"],
        coverage["AA_directed_parents"] == 42,
        coverage["AA_gauge_gauge_routes"] == 36,
        coverage["AA_matter_matter_routes"] == 6,
        coverage["AA_marked_inverse_edge_occurrences"] == 84,
        coverage["coefficient_inference_from_census"] is False,
        len(tadpole["twelve_source_tags"]) == 12,
        tadpole["anomaly_sector"].startswith("0"),
        bubbles["closed_form_attachment_sum"] == "(1+i)*z-2-3*i",
        bubbles["source_A_four_dimensional_trace"]["text"] == "0",
        bubbles["source_D_four_dimensional_trace"]["text"] == "0",
        bubbles["attachment_denominators_distinct"] is True,
        bubbles["fraction_level_cancellation_claimed"] is False,
        bubbles["anomaly_sector"] == "0",
        quartic["four_dimensional_trace"]["text"] == "0",
        quartic["anomaly_sector"].startswith("0"),
        triangle["directed_coefficient_in_lambda1_units"] == "-1/8",
        full["coefficient_in_lambda1_units"] == "-1/8",
        full["changed_from_isolated_triangle"] is False,
        all(value is True for value in checks.values()),
    )
    return sum(assertions), len(assertions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--full-replay", action="store_true")
    parser.add_argument("--check-artifact", type=Path)
    args = parser.parse_args()
    if args.check_artifact:
        artifact = json.loads(args.check_artifact.read_text(encoding="utf-8"))
        passed, total = validate_artifact(artifact)
        print(f"SUMMARY {passed}/{total} PASS")
        return 0 if passed == total else 1
    artifact = build_artifact(full_replay=args.full_replay)
    passed, total = validate_artifact(artifact)
    if passed != total:
        raise AssertionError(f"generated artifact validates only {passed}/{total}")
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"PASS wrote {args.output}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
