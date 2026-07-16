#!/usr/bin/env python3
"""Symbolic exact replay of the fully polarized AA gauge triangle.

The component engine in ``step5_aa_full_raw_triangle_component_probe`` is
unchanged.  Only its scalar field is lifted from Q(sqrt(2),i) to the sparse
polynomial ring Q(sqrt(2),i)[l0,l1,l2,l3].  This removes sample interpolation
from the edge-divisibility and induced-contact audit.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Mapping

import sympy as sp

import step5_aa_full_raw_triangle_component_probe as probe


aa = probe.aa
BASE_A = aa.A
MONOMIAL_ZERO = (0, 0, 0, 0)
Coefficient = tuple[Fraction, Fraction, Fraction, Fraction]
ZERO_COEFFICIENT: Coefficient = (
    Fraction(0),
    Fraction(0),
    Fraction(0),
    Fraction(0),
)


def coefficient_add(left: Coefficient, right: Coefficient) -> Coefficient:
    return tuple(left[index] + right[index] for index in range(4))


def coefficient_neg(value: Coefficient) -> Coefficient:
    return tuple(-entry for entry in value)


def coefficient_mul(left: Coefficient, right: Coefficient) -> Coefficient:
    xr, xs, yi, ys = left
    ur, us, vi, vs = right
    xu_a = xr * ur + 2 * xs * us
    xu_b = xr * us + xs * ur
    yv_a = yi * vi + 2 * ys * vs
    yv_b = yi * vs + ys * vi
    xv_a = xr * vi + 2 * xs * vs
    xv_b = xr * vs + xs * vi
    yu_a = yi * ur + 2 * ys * us
    yu_b = yi * us + ys * ur
    return xu_a - yv_a, xu_b - yv_b, xv_a + yu_a, xv_b + yu_b


def coefficient_inverse(value: Coefficient) -> Coefficient:
    a, b, c, d = value
    conjugate = (a, b, -c, -d)
    real_norm = coefficient_mul(value, conjugate)
    if real_norm[2] or real_norm[3]:
        raise AssertionError("complex norm did not land in Q(sqrt(2))")
    norm = real_norm[0] * real_norm[0] - 2 * real_norm[1] * real_norm[1]
    if norm == 0:
        raise ZeroDivisionError("division by zero")
    inverse_real = (real_norm[0] / norm, -real_norm[1] / norm, Fraction(0), Fraction(0))
    return coefficient_mul(conjugate, inverse_real)


class PolyA:
    """Sparse Q(sqrt(2),i)-valued polynomial in four loop components."""

    __slots__ = ("terms",)

    def __init__(
        self,
        a: int | Fraction = Fraction(0),
        b: int | Fraction = Fraction(0),
        c: int | Fraction = Fraction(0),
        d: int | Fraction = Fraction(0),
        *,
        terms: Mapping[tuple[int, int, int, int], Coefficient] | None = None,
    ) -> None:
        if terms is None:
            value = (Fraction(a), Fraction(b), Fraction(c), Fraction(d))
            self.terms = {MONOMIAL_ZERO: value} if any(value) else {}
        else:
            self.terms = {
                monomial: value for monomial, value in terms.items() if any(value)
            }

    @classmethod
    def variable(cls, index: int) -> "PolyA":
        monomial = [0, 0, 0, 0]
        monomial[index] = 1
        return cls(terms={tuple(monomial): (Fraction(1), Fraction(0), Fraction(0), Fraction(0))})

    @classmethod
    def from_base(cls, value: BASE_A) -> "PolyA":
        coefficient = (value.a, value.b, value.c, value.d)
        return cls(terms={MONOMIAL_ZERO: coefficient} if any(coefficient) else {})

    @classmethod
    def coerce(cls, value: object) -> "PolyA":
        if isinstance(value, cls):
            return value
        if isinstance(value, BASE_A):
            return cls.from_base(value)
        if isinstance(value, (int, Fraction)):
            return cls(value)
        raise TypeError(f"cannot coerce {value!r} to polynomial scalar")

    def __add__(self, other: object) -> "PolyA":
        rhs = self.coerce(other)
        terms = dict(self.terms)
        for monomial, coefficient in rhs.terms.items():
            value = coefficient_add(terms.get(monomial, ZERO_COEFFICIENT), coefficient)
            if any(value):
                terms[monomial] = value
            else:
                terms.pop(monomial, None)
        return PolyA(terms=terms)

    __radd__ = __add__

    def __neg__(self) -> "PolyA":
        return PolyA(
            terms={monomial: coefficient_neg(value) for monomial, value in self.terms.items()}
        )

    def __sub__(self, other: object) -> "PolyA":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "PolyA":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "PolyA":
        try:
            rhs = self.coerce(other)
        except TypeError:
            return NotImplemented
        terms: dict[tuple[int, int, int, int], Coefficient] = {}
        for left_monomial, left_value in self.terms.items():
            for right_monomial, right_value in rhs.terms.items():
                monomial = tuple(
                    left_monomial[index] + right_monomial[index]
                    for index in range(4)
                )
                value = coefficient_add(
                    terms.get(monomial, ZERO_COEFFICIENT),
                    coefficient_mul(left_value, right_value),
                )
                if any(value):
                    terms[monomial] = value
                else:
                    terms.pop(monomial, None)
        return PolyA(terms=terms)

    __rmul__ = __mul__

    def inverse(self) -> "PolyA":
        if set(self.terms) != {MONOMIAL_ZERO}:
            raise ZeroDivisionError("only nonzero polynomial constants are invertible")
        return PolyA(terms={MONOMIAL_ZERO: coefficient_inverse(self.terms[MONOMIAL_ZERO])})

    def __truediv__(self, other: object) -> "PolyA":
        return self * self.coerce(other).inverse()

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __eq__(self, other: object) -> bool:
        try:
            rhs = self.coerce(other)
        except TypeError:
            return False
        return self.terms == rhs.terms

    def square(self) -> "PolyA":
        return self * self

    @staticmethod
    def _base_expr(value: Coefficient) -> sp.Expr:
        a, b, c, d = value
        return (
            sp.Rational(a.numerator, a.denominator)
            + sp.sqrt(2) * sp.Rational(b.numerator, b.denominator)
            + sp.I * sp.Rational(c.numerator, c.denominator)
            + sp.I * sp.sqrt(2) * sp.Rational(d.numerator, d.denominator)
        )

    def as_expr(self) -> sp.Expr:
        variables = sp.symbols("l0:4")
        return sp.expand(
            sum(
                self._base_expr(value)
                * sp.prod(variables[index] ** monomial[index] for index in range(4))
                for monomial, value in self.terms.items()
            )
        )

    def text(self) -> str:
        return str(self.as_expr())


def install_polynomial_scalar() -> tuple[PolyA, PolyA, PolyA, PolyA]:
    aa.A = PolyA
    aa.ZERO = PolyA()
    aa.ONE = PolyA(1)
    aa.I = PolyA(c=1)
    aa.SQRT2 = PolyA(b=1)
    aa.ZERO_VECTOR = aa.vec((0, 0, 0, 0))
    aa.SIGMA = (
        ((aa.ZERO, -aa.I), (-aa.I, aa.ZERO)),
        ((aa.ZERO, PolyA(-1)), (aa.ONE, aa.ZERO)),
        ((-aa.I, aa.ZERO), (aa.ZERO, aa.I)),
        ((aa.ONE, aa.ZERO), (aa.ZERO, aa.ONE)),
    )
    return tuple(PolyA.variable(index) for index in range(4))


def divide_exact(numerator: PolyA, denominator: PolyA) -> sp.Expr:
    variables = sp.symbols("l0:4")
    quotient, remainder = sp.div(
        sp.Poly(numerator.as_expr(), *variables, extension=[sp.I, sp.sqrt(2)]),
        sp.Poly(denominator.as_expr(), *variables, extension=[sp.I, sp.sqrt(2)]),
    )
    if remainder.as_expr() != 0:
        raise AssertionError(
            f"nonzero polynomial remainder: {sp.expand(remainder.as_expr())}"
        )
    return sp.expand(quotient.as_expr())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--frame",
        choices=(
            "canonical",
            "alternate",
            "p_only",
            "q_only",
            "p_transverse",
            "q_transverse",
            "swapped_transverse",
        ),
        default="canonical",
    )
    args = parser.parse_args()

    loop = install_polynomial_scalar()
    if args.frame == "canonical":
        p = aa.vec((1, 0, 0, 0))
        q = aa.vec((0, 1, 0, 0))
        polarization = aa.vec((0, 0, 0, 1))
        dotted = 0
    elif args.frame == "alternate":
        p = aa.vec((0, 0, 0, 1))
        q = aa.vec((0, 0, 1, 0))
        polarization = aa.vec((1, 0, 0, 0))
        dotted = 1
    elif args.frame == "p_only":
        # For dotted=0, p=e0 has p_+^{dot0}=-i while q=e3 has
        # q_+^{dot0}=0.  This isolates the coefficient multiplying p.
        p = aa.vec((1, 0, 0, 0))
        q = aa.vec((0, 0, 0, 1))
        polarization = aa.vec((0, 0, 0, 1))
        dotted = 0
    elif args.frame == "q_only":
        # For dotted=0, p=e3 has p_+^{dot0}=0 while q=e0 has
        # q_+^{dot0}=-i.  This isolates the coefficient multiplying q.
        p = aa.vec((0, 0, 0, 1))
        q = aa.vec((1, 0, 0, 0))
        polarization = aa.vec((1, 0, 0, 0))
        dotted = 0
    elif args.frame == "p_transverse":
        # Transverse isolating frame: epsilon=e2 is orthogonal to p=e0 and
        # q=e3, while p_+^{dot0}=-i and q_+^{dot0}=0.
        p = aa.vec((1, 0, 0, 0))
        q = aa.vec((0, 0, 0, 1))
        polarization = aa.vec((0, 0, 1, 0))
        dotted = 0
    elif args.frame == "q_transverse":
        # Transverse isolating frame with the same invariants: p=e3,
        # q=e0, epsilon=e1, p_+^{dot0}=0, q_+^{dot0}=-i.  epsilon=e2
        # would annihilate the external A_c helicity normalization.
        p = aa.vec((0, 0, 0, 1))
        q = aa.vec((1, 0, 0, 0))
        polarization = aa.vec((0, 1, 0, 0))
        dotted = 0
    else:
        # Independent plus-spinor projector with the same invariants as the
        # canonical frame.  For dotted=0 both p_-^{dot0} and q_-^{dot0}
        # vanish, while (p_+^{dot0},q_+^{dot0})=(-1,-i).
        p = aa.vec((0, 1, 0, 0))
        q = aa.vec((1, 0, 0, 0))
        polarization = aa.vec((0, 0, 0, 1))
        dotted = 0
    result, table_sizes = probe.triangle_numerator(
        loop,
        args.workers,
        compare_fixed=True,
        p=p,
        q=q,
        polarization=polarization,
        dotted=dotted,
    )

    r0 = loop
    r2 = aa.vadd(loop, aa.vneg(aa.vadd(p, q)))
    r0_square = aa.vdot(r0, r0)
    r2_square = aa.vdot(r2, r2)
    tag0 = "I0_DminusA1[A]*A1[B]"
    tag2 = "I0_A1[A]*DminusA1[B]"
    selected0 = result["selected_source_tags"][(tag0, "-", "+")]
    selected2 = result["selected_source_tags"][(tag2, "-", "+")]
    full0 = result["full_source_tags"][(tag0, "-", "+")]
    full2 = result["full_source_tags"][(tag2, "-", "+")]
    longitudinal0 = result["longitudinal_source_tags"][(tag0, "-", "+")]
    longitudinal2 = result["longitudinal_source_tags"][(tag2, "-", "+")]

    variables = sp.symbols("l0:4")
    quotient0, remainder0 = sp.div(
        sp.Poly(selected0.as_expr(), *variables, extension=[sp.I, sp.sqrt(2)]),
        sp.Poly(r0_square.as_expr(), *variables, extension=[sp.I, sp.sqrt(2)]),
    )
    quotient2, remainder2 = sp.div(
        sp.Poly(selected2.as_expr(), *variables, extension=[sp.I, sp.sqrt(2)]),
        sp.Poly(r2_square.as_expr(), *variables, extension=[sp.I, sp.sqrt(2)]),
    )
    quotient0_expr = sp.expand(quotient0.as_expr())
    quotient2_expr = sp.expand(quotient2.as_expr())
    quotient_sum = sp.expand(quotient0_expr + quotient2_expr)
    trace0 = sp.expand(sum(sp.diff(quotient0_expr, variable, 2) for variable in variables))
    trace2 = sp.expand(sum(sp.diff(quotient2_expr, variable, 2) for variable in variables))

    d0, d2 = sp.symbols("r0d2 r2d2")
    contact0 = sp.expand(-longitudinal0.as_expr() - quotient0_expr * d0)
    contact2 = sp.expand(-longitudinal2.as_expr() - quotient2_expr * d2)
    contact_identity0 = sp.expand(
        full0.as_expr()
        + contact0
        - quotient0_expr * (r0_square.as_expr() - d0)
    )
    contact_identity2 = sp.expand(
        full2.as_expr()
        + contact2
        - quotient2_expr * (r2_square.as_expr() - d2)
    )

    y, z = sp.symbols("y z")
    shift = {
        variables[index]: sp.expand(
            y * q[index].as_expr() + z * (p[index] + q[index]).as_expr()
        )
        for index in range(4)
    }

    def simplex_average(expression: sp.Expr) -> sp.Expr:
        shifted = sp.expand(expression.subs(shift))
        return sp.simplify(
            2 * sp.integrate(shifted, (z, 0, 1 - y), (y, 0, 1))
        )

    average0 = simplex_average(quotient0_expr)
    average2 = simplex_average(quotient2_expr)
    average_sum = sp.simplify(average0 + average2)
    heldout = {variables[index]: value for index, value in enumerate((3, 2, -2, 1))}

    full_expr = result["full"][("-", "+")].as_expr()
    fixed_expr = result["fixed"][("-", "+")].as_expr()
    sector_pairs = (("+", "+"), ("+", "-"), ("-", "+"), ("-", "-"))
    sector_polynomial_remainders = {
        family: {
            pair[0] + pair[1]: sp.expand(
                result[family][pair].as_expr()
                - result[family][("-", "+")].as_expr()
            )
            for pair in sector_pairs
        }
        for family in ("full", "selected", "longitudinal")
    }
    source_sum_identity = sp.expand(full0.as_expr() + full2.as_expr() - full_expr)
    selected_sum_identity = sp.expand(
        selected0.as_expr()
        + selected2.as_expr()
        - result["selected"][("-", "+")].as_expr()
    )
    longitudinal_sum_identity = sp.expand(
        longitudinal0.as_expr()
        + longitudinal2.as_expr()
        - result["longitudinal"][("-", "+")].as_expr()
    )
    checks = {
        "e0_division_remainder_zero": remainder0.is_zero,
        "e2_division_remainder_zero": remainder2.is_zero,
        "source_tags_sum_to_full": source_sum_identity == 0,
        "source_tags_sum_to_selected": selected_sum_identity == 0,
        "source_tags_sum_to_longitudinal": longitudinal_sum_identity == 0,
        "full_e0_equals_selected_plus_longitudinal": sp.expand(
            full0.as_expr() - selected0.as_expr() - longitudinal0.as_expr()
        ) == 0,
        "full_e2_equals_selected_plus_longitudinal": sp.expand(
            full2.as_expr() - selected2.as_expr() - longitudinal2.as_expr()
        ) == 0,
        "full_d_contact_identity_e0": contact_identity0 == 0,
        "full_d_contact_identity_e2": contact_identity2 == 0,
        "four_dimensional_trace_q0_zero": trace0 == 0,
        "four_dimensional_trace_q2_zero": trace2 == 0,
        "full_polarization_differs_from_fixed_strength": sp.expand(
            full_expr - fixed_expr
        ) != 0,
        "all_four_sector_full_polynomials_equal": all(
            remainder == 0
            for remainder in sector_polynomial_remainders["full"].values()
        ),
        "all_four_sector_selected_polynomials_equal": all(
            remainder == 0
            for remainder in sector_polynomial_remainders["selected"].values()
        ),
        "all_four_sector_longitudinal_polynomials_equal": all(
            remainder == 0
            for remainder in sector_polynomial_remainders["longitudinal"].values()
        ),
    }
    if args.frame == "canonical":
        checks.update(
            {
                "heldout_selected_e0": sp.expand(selected0.as_expr().subs(heldout))
                == -9 + 27 * sp.I,
                "heldout_selected_e2": sp.expand(selected2.as_expr().subs(heldout))
                == -40 + 70 * sp.I,
                "simplex_average_sum": average_sum == -sp.Rational(1, 2) + sp.I,
            }
        )

    payload = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "table_sizes": table_sizes,
        "routing": {
            "frame": args.frame,
            "p": [sp.sstr(component.as_expr()) for component in p],
            "q": [sp.sstr(component.as_expr()) for component in q],
            "polarization": [
                sp.sstr(component.as_expr()) for component in polarization
            ],
            "dotted": dotted,
            "r0": "ell",
            "r1": "ell-q",
            "r2": "ell-p-q",
            "feynman_shift": "ell=L+y*q+z*(p+q)",
        },
        "full_polarization": {
            "full_numerator": sp.sstr(sp.expand(full_expr)),
            "fixed_field_strength_numerator": sp.sstr(sp.expand(fixed_expr)),
            "full_minus_fixed": sp.sstr(sp.expand(full_expr - fixed_expr)),
            "four_sector_polynomial_remainders": {
                family: {
                    pair: sp.sstr(remainder)
                    for pair, remainder in rows.items()
                }
                for family, rows in sector_polynomial_remainders.items()
            },
        },
        "selected": {
            "e0_numerator": sp.sstr(selected0.as_expr()),
            "e0_square": sp.sstr(r0_square.as_expr()),
            "e0_quotient": sp.sstr(quotient0_expr),
            "e0_remainder": sp.sstr(sp.expand(remainder0.as_expr())),
            "e2_numerator": sp.sstr(selected2.as_expr()),
            "e2_square": sp.sstr(r2_square.as_expr()),
            "e2_quotient": sp.sstr(quotient2_expr),
            "e2_remainder": sp.sstr(sp.expand(remainder2.as_expr())),
            "quotient_sum": sp.sstr(quotient_sum),
            "quadratic_trace_e0": sp.sstr(trace0),
            "quadratic_trace_e2": sp.sstr(trace2),
        },
        "longitudinal": {
            "e0": sp.sstr(longitudinal0.as_expr()),
            "e2": sp.sstr(longitudinal2.as_expr()),
        },
        "induced_contact": {
            "e0": sp.sstr(contact0),
            "e2": sp.sstr(contact2),
            "identity_e0_remainder": sp.sstr(contact_identity0),
            "identity_e2_remainder": sp.sstr(contact_identity2),
        },
        "finite_simplex": {
            "master": "1/(32*pi^2)",
            "normalized_moments": {
                "1": "1",
                "y": "1/3",
                "z": "1/3",
                "y^2": "1/6",
                "y*z": "1/12",
                "z^2": "1/6",
            },
            "average_q0": sp.sstr(average0),
            "average_q2": sp.sstr(average2),
            "average_sum": sp.sstr(average_sum),
        },
    }
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")


if __name__ == "__main__":
    main()
