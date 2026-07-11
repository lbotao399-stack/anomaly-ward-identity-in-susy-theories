#!/usr/bin/env python3
"""Exact full-superspace Euclidean N=1 superconformal verifier.

The coefficient field is Q(i).  Operators act on polynomials in four
commuting Euclidean coordinates and the exterior algebra generated, in order,
by vartheta^1, vartheta^2, barvartheta^dot1, barvartheta^dot2.  The 80 test
inputs are all 16 Grassmann monomials times 1,x^1,x^2,x^3,x^4.  Because every
identity compared below is an identity of first-order differential operators,
the included subfamily 1,x^m,vartheta^a,barvartheta^dot_a determines every
zeroth- and first-order coefficient exactly.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


class C:
    __slots__ = ("r", "i")

    def __init__(self, r: int | Fraction = 0, i: int | Fraction = 0) -> None:
        self.r = Fraction(r)
        self.i = Fraction(i)

    def __add__(self, other: "C") -> "C":
        return C(self.r + other.r, self.i + other.i)

    def __sub__(self, other: "C") -> "C":
        return C(self.r - other.r, self.i - other.i)

    def __neg__(self) -> "C":
        return C(-self.r, -self.i)

    def __mul__(self, other: "C") -> "C":
        return C(
            self.r * other.r - self.i * other.i,
            self.r * other.i + self.i * other.r,
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, C) and self.r == other.r and self.i == other.i

    def __repr__(self) -> str:
        return f"C({self.r},{self.i})"

    def zero(self) -> bool:
        return self.r == 0 and self.i == 0


Z = C()
O = C(1)
M = C(-1)
I = C(0, 1)
MI = C(0, -1)
TWO = C(2)
MTWO = C(-2)
HALF = C(Fraction(1, 2))

# key=(Grassmann mask,x1 power,x2 power,x3 power,x4 power)
Key = tuple[int, int, int, int, int]
Poly = dict[Key, C]


def norm(p: Poly) -> Poly:
    return {key: coefficient for key, coefficient in p.items() if not coefficient.zero()}


def add(*values: Poly) -> Poly:
    out: Poly = {}
    for p in values:
        for key, coefficient in p.items():
            out[key] = out.get(key, Z) + coefficient
    return norm(out)


def scale(coefficient: C, p: Poly) -> Poly:
    return norm({key: coefficient * value for key, value in p.items()})


def basis(mask: int, exponents: tuple[int, int, int, int]) -> Poly:
    return {(mask, *exponents): O}


ONE = basis(0, (0, 0, 0, 0))


def mul_x(m: int, p: Poly) -> Poly:
    out: Poly = {}
    for key, coefficient in p.items():
        values = list(key)
        values[1 + m] += 1
        shifted = tuple(values)
        out[shifted] = out.get(shifted, Z) + coefficient
    return norm(out)


def dx(m: int, p: Poly) -> Poly:
    out: Poly = {}
    for key, coefficient in p.items():
        power = key[1 + m]
        if power == 0:
            continue
        values = list(key)
        values[1 + m] -= 1
        shifted = tuple(values)
        out[shifted] = out.get(shifted, Z) + C(power) * coefficient
    return norm(out)


def mul_g(index: int, p: Poly) -> Poly:
    bit = 1 << index
    out: Poly = {}
    for key, coefficient in p.items():
        mask = key[0]
        if mask & bit:
            continue
        sign = M if (mask & (bit - 1)).bit_count() % 2 else O
        shifted = (mask | bit, *key[1:])
        out[shifted] = out.get(shifted, Z) + sign * coefficient
    return norm(out)


def dg(index: int, p: Poly) -> Poly:
    bit = 1 << index
    out: Poly = {}
    for key, coefficient in p.items():
        mask = key[0]
        if not mask & bit:
            continue
        sign = M if (mask & (bit - 1)).bit_count() % 2 else O
        shifted = (mask ^ bit, *key[1:])
        out[shifted] = out.get(shifted, Z) + sign * coefficient
    return norm(out)


def mul_t(a: int, p: Poly) -> Poly:
    return mul_g(a, p)


def dt(a: int, p: Poly) -> Poly:
    return dg(a, p)


def mul_bt(dot: int, p: Poly) -> Poly:
    return mul_g(2 + dot, p)


def dbt(dot: int, p: Poly) -> Poly:
    # tildebarpartial_dot=left derivative with respect to barvartheta^dot.
    return dg(2 + dot, p)


Matrix = tuple[tuple[C, C], tuple[C, C]]


def sum_c(values) -> C:
    out = Z
    for value in values:
        out = out + value
    return out


def mm(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum_c(left[row][k] * right[k][column] for k in range(2)) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def msub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mscale(coefficient: C, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(coefficient * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


SID: Matrix = ((O, Z), (Z, O))
S1: Matrix = ((Z, O), (O, Z))
S2: Matrix = ((Z, MI), (I, Z))
S3: Matrix = ((O, Z), (Z, M))
EPS_UP: Matrix = ((Z, O), (M, Z))

# Python labels 0,1,2,3 are Euclidean labels 1,2,3,4.
SIGE = (mscale(MI, S1), mscale(MI, S2), mscale(MI, S3), SID)
BSIGE = (mscale(I, S1), mscale(I, S2), mscale(I, S3), SID)
SIGEMN: dict[tuple[int, int], Matrix] = {}
BAREMN: dict[tuple[int, int], Matrix] = {}
for m in range(4):
    for n in range(4):
        SIGEMN[m, n] = mscale(
            C(Fraction(1, 4)),
            msub(mm(SIGE[m], BSIGE[n]), mm(SIGE[n], BSIGE[m])),
        )
        BAREMN[m, n] = mscale(
            C(Fraction(1, 4)),
            msub(mm(BSIGE[m], SIGE[n]), mm(BSIGE[n], SIGE[m])),
        )


def op_sum(*ops):
    return lambda p: add(*(operator(p) for operator in ops))


def op_scale(coefficient: C, operator):
    return lambda p: scale(coefficient, operator(p))


def comm(left, right):
    return lambda p: add(left(right(p)), scale(M, right(left(p))))


def anti(left, right):
    return lambda p: add(left(right(p)), right(left(p)))


def zero(_: Poly) -> Poly:
    return {}


def linear(terms):
    return op_sum(*(op_scale(coefficient, operator) for coefficient, operator in terms))


def x_then_d(m: int, n: int):
    return lambda p: mul_x(m, dx(n, p))


def t_then_d(a: int, b: int):
    return lambda p: mul_t(a, dt(b, p))


def bt_then_d(dot: int, other: int):
    return lambda p: mul_bt(dot, dbt(other, p))


E_X = op_sum(*(x_then_d(m, m) for m in range(4)))
N_T = op_sum(*(t_then_d(a, a) for a in range(2)))
N_BT = op_sum(*(bt_then_d(dot, dot) for dot in range(2)))


def mul_b(m: int, p: Poly) -> Poly:
    return add(
        *(
            scale(
                SIGE[m][a][dot],
                mul_t(a, mul_bt(dot, p)),
            )
            for a in range(2)
            for dot in range(2)
        )
    )


def mul_y(m: int, p: Poly) -> Poly:
    return add(mul_x(m, p), mul_b(m, p))


def mul_by(m: int, p: Poly) -> Poly:
    return add(mul_x(m, p), scale(M, mul_b(m, p)))


def tilde_y_entry(dot: int, a: int, p: Poly) -> Poly:
    return add(*(scale(BSIGE[m][dot][a], mul_y(m, p)) for m in range(4)))


def tilde_by_entry(dot: int, a: int, p: Poly) -> Poly:
    return add(*(scale(BSIGE[m][dot][a], mul_by(m, p)) for m in range(4)))


def mul_y2(p: Poly) -> Poly:
    return add(*(mul_y(m, mul_y(m, p)) for m in range(4)))


def mul_by2(p: Poly) -> Poly:
    return add(*(mul_by(m, mul_by(m, p)) for m in range(4)))


def v_y_component(m: int, n: int, p: Poly) -> Poly:
    return add(
        mul_y2(p) if m == n else {},
        scale(MTWO, mul_y(m, mul_y(n, p))),
    )


def v_by_component(m: int, n: int, p: Poly) -> Poly:
    return add(
        mul_by2(p) if m == n else {},
        scale(MTWO, mul_by(m, mul_by(n, p))),
    )


def theta_squared(p: Poly) -> Poly:
    # vartheta^a vartheta_a=-2 vartheta^1 vartheta^2.
    return scale(MTWO, mul_t(0, mul_t(1, p)))


def bartheta_squared(p: Poly) -> Poly:
    # barvartheta_dot_a barvartheta^dot_a=+2 barvartheta^dot1 barvartheta^dot2.
    return scale(TWO, mul_bt(0, mul_bt(1, p)))


# Full Euclidean coordinate vector fields.
P = tuple(op_scale(M, lambda p, m=m: dx(m, p)) for m in range(4))


def q_op(a: int):
    translation = op_sum(
        *(
            op_scale(
                SIGE[m][a][dot],
                lambda p, m=m, dot=dot: mul_bt(dot, dx(m, p)),
            )
            for m in range(4)
            for dot in range(2)
        )
    )
    return op_sum(op_scale(M, lambda p, a=a: dt(a, p)), translation)


Q = tuple(q_op(a) for a in range(2))


def bar_q_op(dot: int):
    translation = op_sum(
        *(
            op_scale(
                M * SIGE[m][a][dot],
                lambda p, m=m, a=a: mul_t(a, dx(m, p)),
            )
            for m in range(4)
            for a in range(2)
        )
    )
    return op_sum(lambda p, dot=dot: dbt(dot, p), translation)


BQ = tuple(bar_q_op(dot) for dot in range(2))
DIL = op_scale(M, op_sum(E_X, op_scale(HALF, N_T), op_scale(HALF, N_BT)))
R = op_scale(MI, op_sum(N_T, op_scale(M, N_BT)))


def rotation(m: int, n: int):
    orbital = op_scale(MI, op_sum(x_then_d(m, n), op_scale(M, x_then_d(n, m))))
    theta_spin = op_sum(
        *(
            op_scale(MI * SIGEMN[m, n][a][b], t_then_d(a, b))
            for a in range(2)
            for b in range(2)
        )
    )
    bar_spin = op_sum(
        *(
            op_scale(I * BAREMN[m, n][dot][other], bt_then_d(other, dot))
            for dot in range(2)
            for other in range(2)
        )
    )
    return op_sum(orbital, theta_spin, bar_spin)


J = {(m, n): rotation(m, n) for m in range(4) for n in range(4)}


def k_op(m: int):
    vector = op_sum(
        *(
            op_scale(
                C(Fraction(-1, 2)),
                lambda p, m=m, n=n: add(
                    v_y_component(m, n, dx(n, p)),
                    v_by_component(m, n, dx(n, p)),
                ),
            )
            for n in range(4)
        )
    )
    theta_spin = op_sum(
        *(
            op_scale(
                SIGE[m][b][dot],
                lambda p, b=b, dot=dot, a=a: mul_t(
                    b, tilde_y_entry(dot, a, dt(a, p))
                ),
            )
            for b in range(2)
            for dot in range(2)
            for a in range(2)
        )
    )
    bar_spin = op_sum(
        *(
            op_scale(
                SIGE[m][c][other],
                lambda p, other=other, dot=dot, c=c: mul_bt(
                    other, tilde_by_entry(dot, c, dbt(dot, p))
                ),
            )
            for other in range(2)
            for dot in range(2)
            for c in range(2)
        )
    )
    return op_sum(vector, theta_spin, bar_spin)


K = tuple(k_op(m) for m in range(4))


def s_op(up: int):
    x_part = op_sum(
        *(
            op_scale(
                M * SIGE[m][b][dot],
                lambda p, b=b, dot=dot, up=up, m=m: mul_t(
                    b, tilde_y_entry(dot, up, dx(m, p))
                ),
            )
            for b in range(2)
            for dot in range(2)
            for m in range(4)
        )
    )
    theta_part = op_sum(
        *(
            op_scale(
                MTWO * EPS_UP[up][b],
                lambda p, b=b: theta_squared(dt(b, p)),
            )
            for b in range(2)
        )
    )
    bar_part = op_sum(
        *(lambda p, dot=dot, up=up: tilde_by_entry(dot, up, dbt(dot, p)) for dot in range(2))
    )
    return op_sum(x_part, theta_part, bar_part)


S = tuple(s_op(a) for a in range(2))


def bar_s_op(updot: int):
    x_part = op_sum(
        *(
            op_scale(
                M * SIGE[m][c][other],
                lambda p, other=other, c=c, updot=updot, m=m: mul_bt(
                    other, tilde_by_entry(updot, c, dx(m, p))
                ),
            )
            for other in range(2)
            for c in range(2)
            for m in range(4)
        )
    )
    theta_part = op_sum(
        *(lambda p, updot=updot, b=b: tilde_y_entry(updot, b, dt(b, p)) for b in range(2))
    )
    bar_part = op_sum(
        *(
            op_scale(
                TWO * EPS_UP[updot][other],
                lambda p, other=other: bartheta_squared(dbt(other, p)),
            )
            for other in range(2)
        )
    )
    return op_sum(x_part, theta_part, bar_part)


BS = tuple(bar_s_op(dot) for dot in range(2))


def test_inputs() -> tuple[Poly, ...]:
    bosonic = [(0, 0, 0, 0)]
    for m in range(4):
        exponents = [0, 0, 0, 0]
        exponents[m] = 1
        bosonic.append(tuple(exponents))
    return tuple(basis(mask, exponents) for mask in range(16) for exponents in bosonic)


CASES = test_inputs()
failures: list[str] = []
families: dict[str, dict[str, int]] = {}


def record_family(family: str) -> dict[str, int]:
    return families.setdefault(
        family,
        {"operator_identities": 0, "input_cases": 0, "failed_cases": 0},
    )


def check(family: str, label: str, left, right=zero) -> None:
    record = record_family(family)
    record["operator_identities"] += 1
    record["input_cases"] += len(CASES)
    for case_index, value in enumerate(CASES):
        left_value = norm(left(value))
        right_value = norm(right(value))
        if left_value != right_value:
            record["failed_cases"] += 1
            failures.append(
                f"{family}:{label}:case={case_index}:left={left_value}:right={right_value}"
            )


def check_value(family: str, label: str, left: Poly, right: Poly) -> None:
    record = record_family(family)
    record["operator_identities"] += 1
    record["input_cases"] += 1
    left_value = norm(left)
    right_value = norm(right)
    if left_value != right_value:
        record["failed_cases"] += 1
        failures.append(f"{family}:{label}:left={left_value}:right={right_value}")


# Complete Euclidean graded algebra.
for a in range(2):
    for dot in range(2):
        check(
            "euclidean_graded_algebra",
            f"QbarQ[{a},{dot}]",
            anti(Q[a], BQ[dot]),
            linear((MTWO * SIGE[m][a][dot], P[m]) for m in range(4)),
        )
        check("euclidean_zero_odd", f"QbarS[{a},{dot}]", anti(Q[a], BS[dot]))
        check("euclidean_zero_odd", f"barQS[{dot},{a}]", anti(BQ[dot], S[a]))
        check(
            "euclidean_graded_algebra",
            f"SbarS[{a},{dot}]",
            anti(S[a], BS[dot]),
            linear((MTWO * BSIGE[m][dot][a], K[m]) for m in range(4)),
        )

for a in range(2):
    check("euclidean_dilation_r", f"DQ[{a}]", comm(DIL, Q[a]), op_scale(HALF, Q[a]))
    check("euclidean_dilation_r", f"RQ[{a}]", comm(R, Q[a]), op_scale(I, Q[a]))
    check("euclidean_dilation_r", f"DS[{a}]", comm(DIL, S[a]), op_scale(C(Fraction(-1, 2)), S[a]))
    check("euclidean_dilation_r", f"RS[{a}]", comm(R, S[a]), op_scale(MI, S[a]))
    for m in range(4):
        check(
            "euclidean_mixed_even_odd",
            f"KQ[{m},{a}]",
            comm(K[m], Q[a]),
            linear((SIGE[m][a][dot], BS[dot]) for dot in range(2)),
        )
        check(
            "euclidean_mixed_even_odd",
            f"PS[{m},{a}]",
            comm(P[m], S[a]),
            linear((-BSIGE[m][dot][a], BQ[dot]) for dot in range(2)),
        )
    for b in range(2):
        rhs_terms = [
            (C(-2) if a == b else Z, DIL),
            (C(0, -3) if a == b else Z, R),
        ]
        for m in range(4):
            for n in range(4):
                rhs_terms.append((MI * TWO * SIGEMN[m, n][a][b], J[m, n]))
        check(
            "euclidean_graded_algebra",
            f"QS[{a},{b}]",
            anti(Q[a], S[b]),
            linear(rhs_terms),
        )

for dot in range(2):
    check("euclidean_dilation_r", f"DbarQ[{dot}]", comm(DIL, BQ[dot]), op_scale(HALF, BQ[dot]))
    check("euclidean_dilation_r", f"RbarQ[{dot}]", comm(R, BQ[dot]), op_scale(MI, BQ[dot]))
    check("euclidean_dilation_r", f"DbarS[{dot}]", comm(DIL, BS[dot]), op_scale(C(Fraction(-1, 2)), BS[dot]))
    check("euclidean_dilation_r", f"RbarS[{dot}]", comm(R, BS[dot]), op_scale(I, BS[dot]))
    for m in range(4):
        check(
            "euclidean_mixed_even_odd",
            f"PbarS[{m},{dot}]",
            comm(P[m], BS[dot]),
            linear((BSIGE[m][dot][a], Q[a]) for a in range(2)),
        )
        check(
            "euclidean_mixed_even_odd",
            f"KbarQ[{m},{dot}]",
            comm(K[m], BQ[dot]),
            linear((-SIGE[m][a][dot], S[a]) for a in range(2)),
        )
    for other in range(2):
        rhs_terms = [
            (C(2) if dot == other else Z, DIL),
            (C(0, -3) if dot == other else Z, R),
        ]
        for m in range(4):
            for n in range(4):
                rhs_terms.append((MI * TWO * BAREMN[m, n][other][dot], J[m, n]))
        check(
            "euclidean_graded_algebra",
            f"barQbarS[{dot},{other}]",
            anti(BQ[dot], BS[other]),
            linear(rhs_terms),
        )

for m in range(4):
    check("euclidean_bosonic_conformal", f"DP[{m}]", comm(DIL, P[m]), P[m])
    check("euclidean_bosonic_conformal", f"DK[{m}]", comm(DIL, K[m]), op_scale(M, K[m]))
    for n in range(4):
        check(
            "euclidean_bosonic_conformal",
            f"PK[{m},{n}]",
            comm(P[m], K[n]),
            linear(((TWO if m == n else Z, DIL), (C(0, 2), J[m, n]))),
        )

for a in range(2):
    for b in range(2):
        check("euclidean_zero_odd", f"QQ[{a},{b}]", anti(Q[a], Q[b]))
        check("euclidean_zero_odd", f"SS[{a},{b}]", anti(S[a], S[b]))
for dot in range(2):
    for other in range(2):
        check("euclidean_zero_odd", f"barQbarQ[{dot},{other}]", anti(BQ[dot], BQ[other]))
        check("euclidean_zero_odd", f"barSbarS[{dot},{other}]", anti(BS[dot], BS[other]))

for m in range(4):
    check("euclidean_zero_even_mixed", f"RP[{m}]", comm(R, P[m]))
    check("euclidean_zero_even_mixed", f"RK[{m}]", comm(R, K[m]))
    for n in range(4):
        check("euclidean_zero_even_mixed", f"PP[{m},{n}]", comm(P[m], P[n]))
        check("euclidean_zero_even_mixed", f"KK[{m},{n}]", comm(K[m], K[n]))
    for a in range(2):
        check("euclidean_zero_even_mixed", f"PQ[{m},{a}]", comm(P[m], Q[a]))
        check("euclidean_zero_even_mixed", f"KS[{m},{a}]", comm(K[m], S[a]))
    for dot in range(2):
        check("euclidean_zero_even_mixed", f"PbarQ[{m},{dot}]", comm(P[m], BQ[dot]))
        check("euclidean_zero_even_mixed", f"KbarS[{m},{dot}]", comm(K[m], BS[dot]))

check("euclidean_zero_even_mixed", "DR", comm(DIL, R))

for m in range(4):
    for n in range(4):
        check("euclidean_spin4", f"DJ[{m},{n}]", comm(DIL, J[m, n]))
        check("euclidean_spin4", f"RJ[{m},{n}]", comm(R, J[m, n]))
        for a in range(2):
            check(
                "euclidean_spin4",
                f"JQ[{m},{n},{a}]",
                comm(J[m, n], Q[a]),
                linear((I * SIGEMN[m, n][a][b], Q[b]) for b in range(2)),
            )
            check(
                "euclidean_spin4",
                f"JS[{m},{n},{a}]",
                comm(J[m, n], S[a]),
                linear((MI * SIGEMN[m, n][b][a], S[b]) for b in range(2)),
            )
        for dot in range(2):
            check(
                "euclidean_spin4",
                f"JbarQ[{m},{n},{dot}]",
                comm(J[m, n], BQ[dot]),
                linear((MI * BAREMN[m, n][other][dot], BQ[other]) for other in range(2)),
            )
            check(
                "euclidean_spin4",
                f"JbarS[{m},{n},{dot}]",
                comm(J[m, n], BS[dot]),
                linear((I * BAREMN[m, n][dot][other], BS[other]) for other in range(2)),
            )
        for r in range(4):
            check(
                "euclidean_spin4",
                f"JP[{m},{n},{r}]",
                comm(J[m, n], P[r]),
                linear(((I if r == m else Z, P[n]), (MI if r == n else Z, P[m]))),
            )
            check(
                "euclidean_spin4",
                f"JK[{m},{n},{r}]",
                comm(J[m, n], K[r]),
                linear(((I if r == m else Z, K[n]), (MI if r == n else Z, K[m]))),
            )
        for r in range(4):
            for s in range(4):
                check(
                    "euclidean_spin4",
                    f"JJ[{m},{n},{r},{s}]",
                    comm(J[m, n], J[r, s]),
                    linear(
                        (
                            (I if r == m else Z, J[n, s]),
                            (MI if r == n else Z, J[m, s]),
                            (MI if s == m else Z, J[n, r]),
                            (I if s == n else Z, J[m, r]),
                        )
                    ),
                )


# Full-coordinate action and chiral/antichiral restriction identities.
X = tuple(mul_x(m, ONE) for m in range(4))
TH = tuple(mul_t(a, ONE) for a in range(2))
BTH = tuple(mul_bt(dot, ONE) for dot in range(2))
Y = tuple(mul_y(m, ONE) for m in range(4))
BY = tuple(mul_by(m, ONE) for m in range(4))

for m in range(4):
    for n in range(4):
        check_value("full_coordinate_actions", f"P[{m}]y[{n}]", P[m](Y[n]), scale(M if m == n else Z, ONE))
        check_value("full_coordinate_actions", f"P[{m}]bary[{n}]", P[m](BY[n]), scale(M if m == n else Z, ONE))
        check_value(
            "full_coordinate_actions",
            f"K[{m}]y[{n}]",
            K[m](Y[n]),
            scale(M, v_y_component(m, n, ONE)),
        )
        check_value(
            "full_coordinate_actions",
            f"K[{m}]bary[{n}]",
            K[m](BY[n]),
            scale(M, v_by_component(m, n, ONE)),
        )
    for a in range(2):
        ktheta = add(
            *(
                scale(SIGE[m][b][dot], mul_t(b, tilde_y_entry(dot, a, ONE)))
                for b in range(2)
                for dot in range(2)
            )
        )
        check_value("full_coordinate_actions", f"K[{m}]theta[{a}]", K[m](TH[a]), ktheta)
    for dot in range(2):
        kbartheta = add(
            *(
                scale(SIGE[m][c][other], mul_bt(other, tilde_by_entry(dot, c, ONE)))
                for c in range(2)
                for other in range(2)
            )
        )
        check_value("full_coordinate_actions", f"K[{m}]bartheta[{dot}]", K[m](BTH[dot]), kbartheta)

for a in range(2):
    for m in range(4):
        sy = add(
            *(
                scale(MTWO * SIGE[m][b][dot], mul_t(b, tilde_y_entry(dot, a, ONE)))
                for b in range(2)
                for dot in range(2)
            )
        )
        check_value("full_coordinate_actions", f"S[{a}]y[{m}]", S[a](Y[m]), sy)
        check_value("full_coordinate_actions", f"S[{a}]bary[{m}]", S[a](BY[m]), {})
    for b in range(2):
        expected = scale(MTWO * EPS_UP[a][b], theta_squared(ONE))
        check_value("full_coordinate_actions", f"S[{a}]theta[{b}]", S[a](TH[b]), expected)
    for dot in range(2):
        check_value(
            "full_coordinate_actions",
            f"S[{a}]bartheta[{dot}]",
            S[a](BTH[dot]),
            tilde_by_entry(dot, a, ONE),
        )

for dot in range(2):
    for m in range(4):
        check_value("full_coordinate_actions", f"barS[{dot}]y[{m}]", BS[dot](Y[m]), {})
        sbary = add(
            *(
                scale(
                    MTWO * SIGE[m][c][other],
                    mul_bt(other, tilde_by_entry(dot, c, ONE)),
                )
                for c in range(2)
                for other in range(2)
            )
        )
        check_value("full_coordinate_actions", f"barS[{dot}]bary[{m}]", BS[dot](BY[m]), sbary)
    for b in range(2):
        check_value(
            "full_coordinate_actions",
            f"barS[{dot}]theta[{b}]",
            BS[dot](TH[b]),
            tilde_y_entry(dot, b, ONE),
        )
    for other in range(2):
        expected = scale(TWO * EPS_UP[dot][other], bartheta_squared(ONE))
        check_value(
            "full_coordinate_actions",
            f"barS[{dot}]bartheta[{other}]",
            BS[dot](BTH[other]),
            expected,
        )

for a in range(2):
    for b in range(2):
        check_value(
            "full_coordinate_actions",
            f"Q[{a}]theta[{b}]",
            Q[a](TH[b]),
            scale(M if a == b else Z, ONE),
        )
    for m in range(4):
        check_value("full_coordinate_actions", f"Q[{a}]y[{m}]", Q[a](Y[m]), {})
        qby = add(
            *(
                scale(TWO * SIGE[m][a][dot], mul_bt(dot, ONE))
                for dot in range(2)
            )
        )
        check_value("full_coordinate_actions", f"Q[{a}]bary[{m}]", Q[a](BY[m]), qby)
for dot in range(2):
    for other in range(2):
        check_value(
            "full_coordinate_actions",
            f"barQ[{dot}]bartheta[{other}]",
            BQ[dot](BTH[other]),
            scale(O if dot == other else Z, ONE),
        )
    for m in range(4):
        bqy = add(
            *(
                scale(MTWO * SIGE[m][a][dot], mul_t(a, ONE))
                for a in range(2)
            )
        )
        check_value("full_coordinate_actions", f"barQ[{dot}]y[{m}]", BQ[dot](Y[m]), bqy)
        check_value("full_coordinate_actions", f"barQ[{dot}]bary[{m}]", BQ[dot](BY[m]), {})

for m in range(4):
    check_value("full_coordinate_actions", f"D.y[{m}]", DIL(Y[m]), scale(M, Y[m]))
    check_value("full_coordinate_actions", f"D.bary[{m}]", DIL(BY[m]), scale(M, BY[m]))
    check_value("full_coordinate_actions", f"R.y[{m}]", R(Y[m]), {})
    check_value("full_coordinate_actions", f"R.bary[{m}]", R(BY[m]), {})
for a in range(2):
    check_value("full_coordinate_actions", f"D.theta[{a}]", DIL(TH[a]), scale(C(Fraction(-1, 2)), TH[a]))
    check_value("full_coordinate_actions", f"R.theta[{a}]", R(TH[a]), scale(MI, TH[a]))
for dot in range(2):
    check_value("full_coordinate_actions", f"D.bartheta[{dot}]", DIL(BTH[dot]), scale(C(Fraction(-1, 2)), BTH[dot]))
    check_value("full_coordinate_actions", f"R.bartheta[{dot}]", R(BTH[dot]), scale(I, BTH[dot]))

for m in range(4):
    for n in range(4):
        for r in range(4):
            expected_y = add(
                scale(MI if r == n else Z, Y[m]),
                scale(I if r == m else Z, Y[n]),
            )
            expected_by = add(
                scale(MI if r == n else Z, BY[m]),
                scale(I if r == m else Z, BY[n]),
            )
            check_value(
                "full_coordinate_actions",
                f"J[{m},{n}]y[{r}]",
                J[m, n](Y[r]),
                expected_y,
            )
            check_value(
                "full_coordinate_actions",
                f"J[{m},{n}]bary[{r}]",
                J[m, n](BY[r]),
                expected_by,
            )
        for a in range(2):
            expected_theta = add(
                *(
                    scale(MI * SIGEMN[m, n][b][a], TH[b])
                    for b in range(2)
                )
            )
            check_value(
                "full_coordinate_actions",
                f"J[{m},{n}]theta[{a}]",
                J[m, n](TH[a]),
                expected_theta,
            )
        for dot in range(2):
            expected_bartheta = add(
                *(
                    scale(I * BAREMN[m, n][dot][other], BTH[other])
                    for other in range(2)
                )
            )
            check_value(
                "full_coordinate_actions",
                f"J[{m},{n}]bartheta[{dot}]",
                J[m, n](BTH[dot]),
                expected_bartheta,
            )


# Locked Lorentzian full-superspace fields evaluated on the same Euclidean basis.
ETA = (-1, 1, 1, 1)
SIGL = (SID, S1, S2, S3)
BSIGL = (SID, mscale(M, S1), mscale(M, S2), mscale(M, S3))
SIGL_LOWER = tuple(mscale(C(ETA[mu]), SIGL[mu]) for mu in range(4))
SIGLMN: dict[tuple[int, int], Matrix] = {}
BARELMN: dict[tuple[int, int], Matrix] = {}
for mu in range(4):
    for nu in range(4):
        SIGLMN[mu, nu] = mscale(
            C(Fraction(1, 4)),
            msub(mm(SIGL[mu], BSIGL[nu]), mm(SIGL[nu], BSIGL[mu])),
        )
        BARELMN[mu, nu] = mscale(
            C(Fraction(1, 4)),
            msub(mm(BSIGL[mu], SIGL[nu]), mm(BSIGL[nu], SIGL[mu])),
        )


def lx(mu: int, p: Poly) -> Poly:
    return scale(MI, mul_x(3, p)) if mu == 0 else mul_x(mu - 1, p)


def ldx(mu: int, p: Poly) -> Poly:
    return scale(I, dx(3, p)) if mu == 0 else dx(mu - 1, p)


def l_b(mu: int, p: Poly) -> Poly:
    return add(
        *(
            scale(SIGL[mu][a][dot], mul_t(a, mul_bt(dot, p)))
            for a in range(2)
            for dot in range(2)
        )
    )


def ly(mu: int, p: Poly) -> Poly:
    return add(lx(mu, p), scale(MI, l_b(mu, p)))


def lby(mu: int, p: Poly) -> Poly:
    return add(lx(mu, p), scale(I, l_b(mu, p)))


def ltilde_y(dot: int, a: int, p: Poly) -> Poly:
    return add(
        *(scale(C(ETA[mu]) * BSIGL[mu][dot][a], ly(mu, p)) for mu in range(4))
    )


def ltilde_by(dot: int, a: int, p: Poly) -> Poly:
    return add(
        *(scale(C(ETA[mu]) * BSIGL[mu][dot][a], lby(mu, p)) for mu in range(4))
    )


def l_y2(p: Poly, barred: bool = False) -> Poly:
    multiply = lby if barred else ly
    return add(
        *(scale(C(ETA[mu]), multiply(mu, multiply(mu, p))) for mu in range(4))
    )


def l_v_component(mu: int, nu: int, p: Poly, barred: bool = False) -> Poly:
    multiply = lby if barred else ly
    return add(
        l_y2(p, barred) if mu == nu else {},
        scale(C(-2 * ETA[mu]), multiply(mu, multiply(nu, p))),
    )


LE = op_sum(*(lambda p, mu=mu: lx(mu, ldx(mu, p)) for mu in range(4)))
LP = tuple(op_scale(MI, lambda p, mu=mu: ldx(mu, p)) for mu in range(4))


def lq_op(a: int):
    return op_sum(
        op_scale(MI, lambda p, a=a: dt(a, p)),
        *(
            op_scale(
                SIGL[mu][a][dot],
                lambda p, mu=mu, dot=dot: mul_bt(dot, ldx(mu, p)),
            )
            for mu in range(4)
            for dot in range(2)
        ),
    )


LQ = tuple(lq_op(a) for a in range(2))


def lbq_op(dot: int):
    return op_sum(
        op_scale(I, lambda p, dot=dot: dbt(dot, p)),
        *(
            op_scale(
                M * SIGL[mu][a][dot],
                lambda p, mu=mu, a=a: mul_t(a, ldx(mu, p)),
            )
            for mu in range(4)
            for a in range(2)
        ),
    )


LBQ = tuple(lbq_op(dot) for dot in range(2))
LDIL = op_scale(MI, op_sum(LE, op_scale(HALF, N_T), op_scale(HALF, N_BT)))
LR = op_sum(N_T, op_scale(M, N_BT))


def l_rotation(mu: int, nu: int):
    orbital = op_scale(
        MI,
        op_sum(
            op_scale(C(ETA[mu]), lambda p, mu=mu, nu=nu: lx(mu, ldx(nu, p))),
            op_scale(C(-ETA[nu]), lambda p, mu=mu, nu=nu: lx(nu, ldx(mu, p))),
        ),
    )
    sigma_lower = mscale(C(ETA[mu] * ETA[nu]), SIGLMN[mu, nu])
    barsigma_lower = mscale(C(ETA[mu] * ETA[nu]), BARELMN[mu, nu])
    theta_spin = op_sum(
        *(
            op_scale(I * sigma_lower[a][b], t_then_d(a, b))
            for a in range(2)
            for b in range(2)
        )
    )
    bar_spin = op_sum(
        *(
            op_scale(MI * barsigma_lower[dot][other], bt_then_d(other, dot))
            for dot in range(2)
            for other in range(2)
        )
    )
    return op_sum(orbital, theta_spin, bar_spin)


LJ = {(mu, nu): l_rotation(mu, nu) for mu in range(4) for nu in range(4)}


def lk_op(mu: int):
    vector = op_sum(
        *(
            op_scale(
                C(0, Fraction(-1, 2)),
                lambda p, mu=mu, nu=nu: add(
                    l_v_component(mu, nu, ldx(nu, p), False),
                    l_v_component(mu, nu, ldx(nu, p), True),
                ),
            )
            for nu in range(4)
        )
    )
    theta_spin = op_sum(
        *(
            op_scale(
                MI * SIGL_LOWER[mu][b][dot],
                lambda p, b=b, dot=dot, a=a: mul_t(
                    b, ltilde_y(dot, a, dt(a, p))
                ),
            )
            for b in range(2)
            for dot in range(2)
            for a in range(2)
        )
    )
    bar_spin = op_sum(
        *(
            op_scale(
                MI * SIGL_LOWER[mu][c][other],
                lambda p, other=other, dot=dot, c=c: mul_bt(
                    other, ltilde_by(dot, c, dbt(dot, p))
                ),
            )
            for other in range(2)
            for dot in range(2)
            for c in range(2)
        )
    )
    return op_sum(vector, theta_spin, bar_spin)


LK = tuple(lk_op(mu) for mu in range(4))


def ls_op(up: int):
    x_part = op_sum(
        *(
            op_scale(
                I * SIGL[mu][b][dot],
                lambda p, b=b, dot=dot, up=up, mu=mu: mul_t(
                    b, ltilde_y(dot, up, ldx(mu, p))
                ),
            )
            for b in range(2)
            for dot in range(2)
            for mu in range(4)
        )
    )
    theta_part = op_sum(
        *(
            op_scale(
                C(0, -2) * EPS_UP[up][b],
                lambda p, b=b: theta_squared(dt(b, p)),
            )
            for b in range(2)
        )
    )
    bar_part = op_sum(
        *(lambda p, dot=dot, up=up: ltilde_by(dot, up, dbt(dot, p)) for dot in range(2))
    )
    return op_sum(x_part, theta_part, bar_part)


LS = tuple(ls_op(a) for a in range(2))


def lbs_op(updot: int):
    x_part = op_sum(
        *(
            op_scale(
                I * SIGL[mu][c][other],
                lambda p, other=other, c=c, updot=updot, mu=mu: mul_bt(
                    other, ltilde_by(updot, c, ldx(mu, p))
                ),
            )
            for other in range(2)
            for c in range(2)
            for mu in range(4)
        )
    )
    theta_part = op_sum(
        *(lambda p, updot=updot, b=b: ltilde_y(updot, b, dt(b, p)) for b in range(2))
    )
    bar_part = op_sum(
        *(
            op_scale(
                C(0, 2) * EPS_UP[updot][other],
                lambda p, other=other: bartheta_squared(dbt(other, p)),
            )
            for other in range(2)
        )
    )
    return op_sum(x_part, theta_part, bar_part)


LBS = tuple(lbs_op(dot) for dot in range(2))


# Direct coordinate and bispinor Wick identities.
for mu in range(4):
    if mu == 0:
        check("wick_coordinate_relations", "y_L[0]=-i y_E[4]", lambda p: ly(0, p), op_scale(MI, lambda p: mul_y(3, p)))
        check("wick_coordinate_relations", "bary_L[0]=-i bary_E[4]", lambda p: lby(0, p), op_scale(MI, lambda p: mul_by(3, p)))
    else:
        check("wick_coordinate_relations", f"y_L[{mu}]=y_E[{mu}]", lambda p, mu=mu: ly(mu, p), lambda p, mu=mu: mul_y(mu - 1, p))
        check("wick_coordinate_relations", f"bary_L[{mu}]=bary_E[{mu}]", lambda p, mu=mu: lby(mu, p), lambda p, mu=mu: mul_by(mu - 1, p))
for dot in range(2):
    for a in range(2):
        check("wick_coordinate_relations", f"tildeY_L[{dot},{a}]=i tildeY_E", lambda p, dot=dot, a=a: ltilde_y(dot, a, p), op_scale(I, lambda p, dot=dot, a=a: tilde_y_entry(dot, a, p)))
        check("wick_coordinate_relations", f"tildebary_L[{dot},{a}]=i tildebary_E", lambda p, dot=dot, a=a: ltilde_by(dot, a, p), op_scale(I, lambda p, dot=dot, a=a: tilde_by_entry(dot, a, p)))

vector_wick = ((0, 1, MI), (1, 2, MI), (2, 3, MI), (3, 0, M))
for m, mu, phase in vector_wick:
    check("wick_generator_phases", f"P_E[{m}]", P[m], op_scale(phase, LP[mu]))
    check("wick_generator_phases", f"K_E[{m}]", K[m], op_scale(phase, LK[mu]))
for a in range(2):
    check("wick_generator_phases", f"Q_E[{a}]", Q[a], op_scale(MI, LQ[a]))
    check("wick_generator_phases", f"S_E[{a}]", S[a], op_scale(MI, LS[a]))
for dot in range(2):
    check("wick_generator_phases", f"barQ_E[{dot}]", BQ[dot], op_scale(MI, LBQ[dot]))
    check("wick_generator_phases", f"barS_E[{dot}]", BS[dot], op_scale(MI, LBS[dot]))
check("wick_generator_phases", "D_E", DIL, op_scale(MI, LDIL))
check("wick_generator_phases", "R_E", R, op_scale(MI, LR))
for m in range(4):
    for n in range(4):
        if m == 3 and n < 3:
            mu, nu, phase = 0, n + 1, MI
        elif n == 3 and m < 3:
            mu, nu, phase = m + 1, 0, MI
        elif m < 3 and n < 3:
            mu, nu, phase = m + 1, n + 1, O
        else:
            mu, nu, phase = 0, 0, O
        check("wick_generator_phases", f"J_E[{m},{n}]", J[m, n], op_scale(phase, LJ[mu, nu]))


for record in families.values():
    record["passed_cases"] = record["input_cases"] - record["failed_cases"]

total_identities = sum(record["operator_identities"] for record in families.values())
total_input_cases = sum(record["input_cases"] for record in families.values())
total_failed_cases = sum(record["failed_cases"] for record in families.values())
audit = {
    "schema": 1,
    "task_id": "CONTRACT-STEP-02C-COMPLETE-SUPERCONFORMAL-COVARIANCE-001",
    "signature": "Euclidean",
    "chart": "full superspace (x_E^m,vartheta^a,barvartheta^dot_a)",
    "arithmetic": "Q(i) polynomial coefficients and exact exterior algebra; no floating point; no CAS",
    "basis": {
        "grassmann_generators": 4,
        "grassmann_monomials": 16,
        "bosonic_test_monomials": ["1", "x_E^1", "x_E^2", "x_E^3", "x_E^4"],
        "total_inputs": len(CASES),
        "completeness": "Every tested bracket is first order. Equality on 1 and all eight coordinate generators fixes every zeroth- and first-order coefficient; that determining subset is contained in the 80 exact inputs.",
    },
    "operator_definitions": {
        "P_m": "-partial_m",
        "Q_a": "-partial_a+sigma_E^m[a,dot] barvartheta^dot partial_m",
        "barQ_dot_a": "+tildebarpartial_dot_a-vartheta^b sigma_E^m[b,dot_a] partial_m",
        "D": "-(x_E.partial_E+N_vartheta/2+N_barvartheta/2)",
        "R": "-i(N_vartheta-N_barvartheta)",
        "J_mn": "-i(x_m partial_n-x_n partial_m)-i vartheta sigma_E_mn partial_vartheta+i barsigma_E_mn barvartheta tildebarpartial",
        "K_m": "-1/2[V_m(y)+V_m(bar y)]partial_x+vartheta sigma_E_m tildeY partial_vartheta+barvartheta tildebarY sigma_E_m tildebarpartial",
        "S^a": "-vartheta sigma_E^m tildeY^a partial_m-2 vartheta^2 epsilon^(ab)partial_b+tildebarY^(dot b a)tildebarpartial_dot b",
        "barS^dot_a": "-barvartheta tildebarY sigma_E^m partial_m+tildeY^(dot a b)partial_b+2 barvartheta^2 epsilon^(dot a dot b)tildebarpartial_dot b",
    },
    "wick_transport": {
        "coordinates": "x_L^0=-i x_E^4; x_L^i=x_E^i; vartheta_L=vartheta_E; barvartheta_L=barvartheta_E",
        "bispinors": "Y_L=iY_E; tildeY_L=i tildeY_E; barY_L=i barY_E; tildebarY_L=i tildebarY_E",
        "scalar_and_spinor_phases": "G_E=-i W(G_L) for G=D,R,Q,barQ,S,barS",
        "vector_phases": "G_Ei=-i W(G_Li) and G_E4=-W(G_L0) for G=P,K",
        "rotation_phases": "J_Eij=W(J_Lij) and J_E4i=-i W(J_L0i)",
    },
    "families": families,
    "operator_identities": total_identities,
    "input_cases": total_input_cases,
    "failed_cases": total_failed_cases,
    "failures": failures,
    "status": "PASS" if not failures else "FAIL",
}

audit_path = Path(__file__).resolve().parents[1] / "audits" / "step2c-full-euclidean-verification.json"
audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(
    {
        "operator_identities": total_identities,
        "input_cases": total_input_cases,
        "failures": total_failed_cases,
        "audit": str(audit_path),
    }
)
for failure in failures[:50]:
    print(failure)
raise SystemExit(1 if failures else 0)
