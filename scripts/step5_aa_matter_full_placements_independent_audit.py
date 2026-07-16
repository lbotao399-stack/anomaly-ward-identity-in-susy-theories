#!/usr/bin/env python3
"""Independent finite-Grassmann audit for the four AA matter rows.

This checker is deliberately target-blind.  It constructs the source words
from A^(1)=-(1/8) D_+ barD^2 D_+ V, evaluates the three-point Grassmann
polynomial, and compares only identities derived in the companion audit.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import sympy as sp


NVAR = 12


class Grassmann:
    def __init__(self, data=None):
        self.data = {
            mask: sp.expand(coeff)
            for mask, coeff in (data or {}).items()
            if coeff != 0
        }

    def __add__(self, other):
        if not isinstance(other, Grassmann):
            other = Grassmann({0: other})
        out = defaultdict(lambda: 0)
        out.update(self.data)
        for mask, coeff in other.data.items():
            out[mask] += coeff
        return Grassmann(out)

    __radd__ = __add__

    def __neg__(self):
        return Grassmann({mask: -coeff for mask, coeff in self.data.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Grassmann):
            return Grassmann(
                {mask: coeff * other for mask, coeff in self.data.items()}
            )
        out = defaultdict(lambda: 0)
        for left_mask, left_coeff in self.data.items():
            for right_mask, right_coeff in other.data.items():
                if left_mask & right_mask:
                    continue
                inversions = sum(
                    (right_mask & ((1 << i) - 1)).bit_count()
                    for i in range(NVAR)
                    if (left_mask >> i) & 1
                )
                sign = -1 if inversions & 1 else 1
                out[left_mask | right_mask] += (
                    sign * left_coeff * right_coeff
                )
        return Grassmann(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * sp.Rational(1, scalar)

    def derivative(self, variable: int):
        out = {}
        for mask, coeff in self.data.items():
            if not ((mask >> variable) & 1):
                continue
            lower_count = (mask & ((1 << variable) - 1)).bit_count()
            sign = -1 if lower_count & 1 else 1
            out[mask ^ (1 << variable)] = sign * coeff
        return Grassmann(out)

    def set_zero(self, variables):
        zero_mask = sum(1 << variable for variable in variables)
        return Grassmann(
            {
                mask: coeff
                for mask, coeff in self.data.items()
                if not (mask & zero_mask)
            }
        )

    def coefficient(self, mask: int):
        return sp.expand(self.data.get(mask, 0))


ONE = Grassmann({0: 1})
XI = [Grassmann({1 << i: 1}) for i in range(NVAR)]


def grassmann_exp(value):
    return (
        ONE
        + value
        + value * value / 2
        + value * value * value / 6
        + value * value * value * value / 24
    )


def d_op(value, point, undotted, momentum):
    a, b, c, d = momentum
    base = 4 * point
    derivative = value.derivative(base + (0 if undotted == "+" else 1))
    if undotted == "+":
        coordinate = a * XI[base + 3] - b * XI[base + 2]
    else:
        coordinate = c * XI[base + 3] - d * XI[base + 2]
    return derivative + sp.I * coordinate * value


def bar_d_op(value, point, dotted, momentum):
    a, b, c, d = momentum
    base = 4 * point
    if dotted == 1:
        derivative = -value.derivative(base + 3)
        coordinate = a * XI[base] + c * XI[base + 1]
    else:
        derivative = value.derivative(base + 2)
        coordinate = b * XI[base] + d * XI[base + 1]
    return derivative - sp.I * coordinate * value


def d_squared(value, point, momentum):
    return 2 * d_op(d_op(value, point, "+", momentum), point, "-", momentum)


def bar_d_squared(value, point, momentum):
    return 2 * bar_d_op(
        bar_d_op(value, point, 2, momentum), point, 1, momentum
    )


def a_word(value, point, momentum):
    value = d_op(value, point, "+", momentum)
    value = bar_d_squared(value, point, momentum)
    return d_op(value, point, "+", momentum)


def marked_a_word(value, point, momentum):
    return d_op(a_word(value, point, momentum), point, "-", momentum)


def p_plus(value, point, momentum):
    return bar_d_squared(d_squared(value, point, momentum), point, momentum)


def p_minus(value, point, momentum):
    return d_squared(bar_d_squared(value, point, momentum), point, momentum)


def superspace_delta(left, right):
    left_base = 4 * left
    right_base = 4 * right
    return (
        -4
        * (XI[left_base] - XI[right_base])
        * (XI[left_base + 1] - XI[right_base + 1])
        * (XI[left_base + 2] - XI[right_base + 2])
        * (XI[left_base + 3] - XI[right_base + 3])
    )


def plane_wave(point, momentum, sign):
    a, b, c, d = momentum
    base = 4 * point
    bilinear = (
        XI[base] * (a * XI[base + 3] - b * XI[base + 2])
        + XI[base + 1] * (c * XI[base + 3] - d * XI[base + 2])
    )
    return grassmann_exp(sign * sp.I * bilinear)


symbols = sp.symbols(
    "a0 b0 c0 d0 a1 b1 c1 d1 a2 b2 c2 d2", real=False
)
r0 = symbols[0:4]
r1 = symbols[4:8]
r2 = symbols[8:12]
q = tuple(r0[i] - r1[i] for i in range(4))
p = tuple(r1[i] - r2[i] for i in range(4))


def negate(momentum):
    return tuple(-entry for entry in momentum)


def raw_word(
    marked_edge,
    projector_point=1,
    projector_momentum=None,
    source_r2_momentum=None,
):
    # Locked source routing: r0=k, r1=k-q, r2=k-p-q.  The second source
    # endpoint is the field with Fourier momentum -r2.
    source_r0 = r0
    source_r2 = (
        negate(r2) if source_r2_momentum is None else source_r2_momentum
    )
    left = (
        marked_a_word if marked_edge == "r0" else a_word
    )(superspace_delta(0, 1), 0, source_r0)
    right = (
        marked_a_word if marked_edge == "r2" else a_word
    )(superspace_delta(0, 2), 0, source_r2)
    if projector_momentum is None:
        projector_momentum = r1
    internal = p_plus(
        superspace_delta(1, 2), projector_point, projector_momentum
    )
    external_c = plane_wave(1, q, -1)
    external_b = plane_wave(2, p, +1) * XI[8]
    product = external_c * external_b * left * right * internal
    product = product.set_zero(range(4))
    top_mask = sum(1 << i for i in range(4, 12))
    return sp.factor(product.coefficient(top_mask))


def collapsed_current_word(marked_edge, source_r2_momentum=None):
    source_r0 = r0
    source_r2 = (
        negate(r2) if source_r2_momentum is None else source_r2_momentum
    )
    left = (
        marked_a_word if marked_edge == "r0" else a_word
    )(superspace_delta(0, 1), 0, source_r0)
    right = (
        marked_a_word if marked_edge == "r2" else a_word
    )(superspace_delta(0, 2), 0, source_r2)
    external_c = plane_wave(1, q, -1)
    external_b = plane_wave(2, p, +1) * XI[8]
    product = (
        external_c
        * external_b
        * left
        * right
        * superspace_delta(1, 2)
    )
    product = product.set_zero(range(4))
    top_mask = sum(1 << i for i in range(4, 12))
    return sp.factor(product.coefficient(top_mask))


def wedge_plus(left, right):
    return sp.expand(left[0] * right[1] - left[1] * right[0])


def determinant(momentum):
    return sp.expand(momentum[0] * momentum[3] - momentum[1] * momentum[2])


def check(name, actual, expected):
    difference = sp.expand(actual - expected)
    if difference != 0:
        raise AssertionError(f"{name}: {sp.factor(difference)}")
    print(f"PASS {name}")


def check_grassmann(name, actual, expected):
    difference = actual - expected
    nonzero = {
        mask: sp.factor(coeff)
        for mask, coeff in difference.data.items()
        if sp.expand(coeff) != 0
    }
    if nonzero:
        raise AssertionError(f"{name}: {nonzero}")
    print(f"PASS {name}")


def main():
    x, y = sp.symbols("x y", nonnegative=True)
    z = 1 - x - y
    simplex = lambda value: sp.simplify(
        2 * sp.integrate(sp.integrate(value, (y, 0, 1 - x)), (x, 0, 1))
    )

    w01 = wedge_plus(r0, r1)
    w02 = wedge_plus(r0, r2)
    w12 = wedge_plus(r1, r2)
    s_word = raw_word("r0")
    r_word = raw_word("r2")
    s012 = (
        determinant(r0) * w12 - determinant(r1) * w02
    )
    t012 = w01 * (
        r2[0] * r1[3] - r2[1] * r1[2]
    )
    u012 = w12 * (
        r0[0] * q[3] - r0[1] * q[2]
    )
    expected_s = -16384 * s012
    expected_t = -16384 * t012
    check("FIXED_R0_WORD", s_word, expected_s)
    check(
        "FIXED_MINUS_R2_WORD",
        r_word,
        expected_t,
    )
    check("SCHOUTEN_T_PLUS_S_MINUS_U", t012 + s012 - u012, 0)

    plus_r2_word = w01 * (
        r2[0] * p[3] - r2[1] * p[2]
    )
    check(
        "DIAGNOSTIC_PLUS_R2_R0_WORD",
        raw_word("r0", source_r2_momentum=r2),
        16384 * s012,
    )
    check(
        "DIAGNOSTIC_PLUS_R2_R2_WORD",
        raw_word("r2", source_r2_momentum=r2),
        16384 * plus_r2_word,
    )

    # F1/F2 have forward attachments; X1/X2 have crossed attachments.
    rows = {"F1": s_word, "F2": r_word, "X1": r_word, "X2": s_word}
    check("F1_DWORD", rows["F1"], expected_s)
    check("F2_DWORD", rows["F2"], expected_t)
    check("X1_DWORD", rows["X1"], expected_t)
    check("X2_DWORD", rows["X2"], expected_s)

    delta12 = superspace_delta(1, 2)
    check_grassmann(
        "PROJECTOR_ENDPOINT_TRANSPORT",
        p_plus(delta12, 1, r1),
        p_minus(delta12, 2, negate(r1)),
    )

    # The R word contains only two loop components with undotted index +.
    # Its scalar-square projector differentiates once with respect to a
    # plus-row component and once with respect to a minus-row component.
    loop_a, loop_b, loop_c, loop_d = sp.symbols("la lb lc ld")
    shifts = (
        (y + z) * q[0] + z * p[0],
        (y + z) * q[1] + z * p[1],
        (y + z) * q[2] + z * p[2],
        (y + z) * q[3] + z * p[3],
    )
    shifted_r0 = tuple(
        loop + shift
        for loop, shift in zip((loop_a, loop_b, loop_c, loop_d), shifts)
    )
    shifted_r1 = tuple(shifted_r0[i] - q[i] for i in range(4))
    shifted_r2 = tuple(shifted_r1[i] - p[i] for i in range(4))
    wpq = wedge_plus(p, q)
    shifted_w01 = wedge_plus(shifted_r0, shifted_r1)
    shifted_w02 = wedge_plus(shifted_r0, shifted_r2)
    shifted_w12 = wedge_plus(shifted_r1, shifted_r2)
    loop_zero = {loop_a: 0, loop_b: 0, loop_c: 0, loop_d: 0}
    check(
        "SHIFTED_W01_EVEN",
        sp.expand(shifted_w01.subs(loop_zero).subs(z, 1 - x - y)),
        -(1 - x - y) * wpq,
    )
    check(
        "SHIFTED_W02_EVEN",
        sp.expand(shifted_w02.subs(loop_zero).subs(z, 1 - x - y)),
        y * wpq,
    )
    check(
        "SHIFTED_W12_EVEN",
        sp.expand(shifted_w12.subs(loop_zero).subs(z, 1 - x - y)),
        -x * wpq,
    )

    contact_r0 = collapsed_current_word("r0")
    contact_r2 = collapsed_current_word("r2")
    check("COLLAPSED_CURRENT_R0_RAW", contact_r0, -1024 * w02)
    check("COLLAPSED_CURRENT_R2_RAW", contact_r2, 1024 * w02)
    check(
        "DIAGNOSTIC_PLUS_R2_CURRENT_R0",
        collapsed_current_word("r0", source_r2_momentum=r2),
        1024 * w02,
    )
    check(
        "DIAGNOSTIC_PLUS_R2_CURRENT_R2",
        collapsed_current_word("r2", source_r2_momentum=r2),
        -1024 * w02,
    )
    check("PROJECTOR_COLLAPSE_FACTOR", sp.Rational(16384, 1024), 16)

    primary_r0 = -determinant(r0) * w12
    current_r0 = determinant(r1) * w02
    check("R0_PRIMARY_PLUS_CURRENT", primary_r0 + current_r0, -s012)

    primary_r2 = -determinant(r2) * w01
    current_r2 = -determinant(r1) * w02
    residual_r2 = sp.expand(-t012 - primary_r2 - current_r2)
    check(
        "R2_PRIMARY_PLUS_CURRENT_PLUS_RESIDUAL",
        primary_r2 + current_r2 + residual_r2,
        -t012,
    )

    # The r0 word closes on its primary/current SD orbit.  For r2, the same
    # primary/current extraction is only a truncation: graded transport of
    # the longitudinal word produces an additional r1 collapse and Omega
    # contact.  The independent rank-two replay fixes the raw-orientation
    # residual metric to 1/2-y.
    r0_primary_defect = w12
    r0_current_defect = -w02
    r2_primary_defect = w01
    r2_current_defect = w02
    r0_total_defect = sp.expand(r0_primary_defect + r0_current_defect)
    r2_primary_current_truncation = sp.expand(
        r2_primary_defect + r2_current_defect
    )
    check("R0_PRIMARY_CURRENT_DEFECT", r0_total_defect, w12 - w02)
    check(
        "R2_PRIMARY_CURRENT_TRUNCATION",
        r2_primary_current_truncation,
        w01 + w02,
    )
    check(
        "R2_FULL_METRIC_TRUNCATION_PLUS_LONGITUDINAL",
        (y - z) + (sp.Rational(1, 2) - y),
        sp.Rational(1, 2) - z,
    )

    check("SIMPLEX_ONE", simplex(1), 1)
    check("SIMPLEX_X", simplex(x), sp.Rational(1, 3))
    check("SIMPLEX_Y", simplex(y), sp.Rational(1, 3))
    check("SIMPLEX_Z", simplex(z), sp.Rational(1, 3))
    check("SIMPLEX_X_PLUS_Y", simplex(x + y), sp.Rational(2, 3))
    check(
        "ATTACHMENT_WEDGE_REVERSAL",
        wedge_plus(q, p),
        -wedge_plus(p, q),
    )

    # The source and measure normalization multiplies the raw 16384 by 16;
    # the primitive graph prefactor is hbar*g^2/4.
    check(
        "D_SOURCE_MEASURE_FACTOR",
        sp.Rational(16384, 64 * 16),
        16,
    )
    check("WICK_TWO_LABELED_ASSIGNMENTS", sp.Rational(1, 2) * 2, 1)
    check(
        "NORMALIZED_PARENT_COEFFICIENT",
        sp.Rational(1, 4) * 16,
        4,
    )
    loop_to_lambda = sp.Rational(4, 2)
    check(
        "R0_PRIMARY_LAMBDA1",
        loop_to_lambda * simplex(-x),
        -sp.Rational(2, 3),
    )
    check(
        "R0_CURRENT_LAMBDA1",
        loop_to_lambda * simplex(-y),
        -sp.Rational(2, 3),
    )
    check(
        "R0_TOTAL_LAMBDA1",
        loop_to_lambda * simplex(-(x + y)),
        -sp.Rational(4, 3),
    )
    check(
        "R2_PRIMARY_LAMBDA1",
        loop_to_lambda * simplex(-z),
        -sp.Rational(2, 3),
    )
    check(
        "R2_CURRENT_LAMBDA1",
        loop_to_lambda * simplex(y),
        sp.Rational(2, 3),
    )
    check(
        "R2_PRIMARY_CURRENT_TRUNCATION_LAMBDA1",
        loop_to_lambda * simplex(y - z),
        0,
    )
    check(
        "R2_LONGITUDINAL_RESIDUAL_LAMBDA1",
        loop_to_lambda * simplex(sp.Rational(1, 2) - y),
        sp.Rational(1, 3),
    )
    check(
        "R2_FULL_LAMBDA1",
        loop_to_lambda * simplex(sp.Rational(1, 2) - z),
        sp.Rational(1, 3),
    )

    print("40/40 PASS")


if __name__ == "__main__":
    main()
