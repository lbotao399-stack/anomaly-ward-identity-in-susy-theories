#!/usr/bin/env python3
"""Exact Step-2C verifier for Lorentzian full N=1 superspace.

The coefficient field is Q(i).  The polynomial module has four commuting
coordinates x^mu and the exterior generators

    theta^1, theta^2, bartheta^dot1, bartheta^dot2.

All odd derivatives are left derivatives.  Differential operators are kept
in coefficient-left, derivative-right normal order.
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
ETA = (-1, 1, 1, 1)

# key = (exterior mask, x0 power, x1 power, x2 power, x3 power)
Key = tuple[int, int, int, int, int]
Poly = dict[Key, C]
Op = object
ZERO_EXP = (0, 0, 0, 0)


def norm(p: Poly) -> Poly:
    return {key: value for key, value in p.items() if not value.zero()}


def add(*values: Poly) -> Poly:
    out: Poly = {}
    for p in values:
        for key, coefficient in p.items():
            out[key] = out.get(key, Z) + coefficient
    return norm(out)


def scale(c: C, p: Poly) -> Poly:
    if c.zero():
        return {}
    return norm({key: c * value for key, value in p.items()})


def basis(mask: int, exponents: tuple[int, int, int, int] = ZERO_EXP) -> Poly:
    return {(mask, *exponents): O}


def exterior_product_sign(left_mask: int, right_mask: int) -> C:
    inversions = 0
    for right in range(4):
        if right_mask & (1 << right):
            inversions += (left_mask >> (right + 1)).bit_count()
    return M if inversions % 2 else O


def mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for left_key, left_coefficient in left.items():
        left_mask = left_key[0]
        for right_key, right_coefficient in right.items():
            right_mask = right_key[0]
            if left_mask & right_mask:
                continue
            sign = exterior_product_sign(left_mask, right_mask)
            new_key = (
                left_mask | right_mask,
                left_key[1] + right_key[1],
                left_key[2] + right_key[2],
                left_key[3] + right_key[3],
                left_key[4] + right_key[4],
            )
            coefficient = sign * left_coefficient * right_coefficient
            out[new_key] = out.get(new_key, Z) + coefficient
    return norm(out)


def dx(mu: int, p: Poly) -> Poly:
    out: Poly = {}
    for key, coefficient in p.items():
        power = key[1 + mu]
        if not power:
            continue
        values = list(key)
        values[1 + mu] -= 1
        new_key = tuple(values)
        out[new_key] = out.get(new_key, Z) + C(power) * coefficient
    return norm(out)


def dg(index: int, p: Poly) -> Poly:
    """Left derivative by exterior generator index."""
    bit = 1 << index
    out: Poly = {}
    for key, coefficient in p.items():
        mask = key[0]
        if not mask & bit:
            continue
        lower_occupied = (mask & (bit - 1)).bit_count()
        sign = M if lower_occupied % 2 else O
        new_key = (mask ^ bit, *key[1:])
        out[new_key] = out.get(new_key, Z) + sign * coefficient
    return norm(out)


def sum_c(values) -> C:
    out = Z
    for value in values:
        out = out + value
    return out


def mm(a, b):
    return tuple(
        tuple(sum_c(a[row][k] * b[k][column] for k in range(2)) for column in range(2))
        for row in range(2)
    )


def msub(a, b):
    return tuple(tuple(a[row][column] - b[row][column] for column in range(2)) for row in range(2))


def mscale(c: C, a):
    return tuple(tuple(c * a[row][column] for column in range(2)) for row in range(2))


SID = ((O, Z), (Z, O))
S1 = ((Z, O), (O, Z))
S2 = ((Z, MI), (I, Z))
S3 = ((O, Z), (Z, M))
SIG = (SID, S1, S2, S3)
BSIG = (SID, mscale(M, S1), mscale(M, S2), mscale(M, S3))
SIG_LOWER = tuple(mscale(C(ETA[mu]), SIG[mu]) for mu in range(4))
BSIG_LOWER = tuple(mscale(C(ETA[mu]), BSIG[mu]) for mu in range(4))
EPS_UP = ((Z, O), (M, Z))
EPS_DOWN = ((Z, M), (O, Z))

SIGMN = {}
BARMN = {}
for mu in range(4):
    for nu in range(4):
        SIGMN[mu, nu] = mscale(
            C(Fraction(1, 4)),
            msub(mm(SIG[mu], BSIG[nu]), mm(SIG[nu], BSIG[mu])),
        )
        BARMN[mu, nu] = mscale(
            C(Fraction(1, 4)),
            msub(mm(BSIG[mu], SIG[nu]), mm(BSIG[nu], SIG[mu])),
        )


X = tuple(basis(0, tuple(1 if rho == mu else 0 for rho in range(4))) for mu in range(4))
THETA = (basis(1 << 0), basis(1 << 1))
BARTHETA = (basis(1 << 2), basis(1 << 3))


def bilinear_b(mu: int) -> Poly:
    terms = []
    for a in range(2):
        for dot in range(2):
            terms.append(scale(SIG[mu][a][dot], mul(THETA[a], BARTHETA[dot])))
    return add(*terms)


B = tuple(bilinear_b(mu) for mu in range(4))
Y = tuple(add(X[mu], scale(MI, B[mu])) for mu in range(4))
BAR_Y = tuple(add(X[mu], scale(I, B[mu])) for mu in range(4))
THETA_SQUARED = scale(MTWO, mul(THETA[0], THETA[1]))
BARTHETA_SQUARED = scale(TWO, mul(BARTHETA[0], BARTHETA[1]))


def tilde_matrix(vector: tuple[Poly, Poly, Poly, Poly]):
    return tuple(
        tuple(
            add(*(scale(C(ETA[mu]) * BSIG[mu][dot][a], vector[mu]) for mu in range(4)))
            for a in range(2)
        )
        for dot in range(2)
    )


TILDE_Y = tilde_matrix(Y)
TILDE_BAR_Y = tilde_matrix(BAR_Y)


def sigma_tilde_entry(sigma, tilde, row: int, column: int) -> Poly:
    return add(*(scale(sigma[row][dot], tilde[dot][column]) for dot in range(2)))


def tilde_sigma_entry(tilde, sigma, row: int, column: int) -> Poly:
    return add(*(scale(sigma[a][column], tilde[row][a]) for a in range(2)))


def vector_squared(vector: tuple[Poly, Poly, Poly, Poly]) -> Poly:
    return add(*(scale(C(ETA[rho]), mul(vector[rho], vector[rho])) for rho in range(4)))


def conformal_v(vector: tuple[Poly, Poly, Poly, Poly], mu: int, nu: int) -> Poly:
    square_term = vector_squared(vector) if mu == nu else {}
    quadratic = scale(C(-2 * ETA[mu]), mul(vector[mu], vector[nu]))
    return add(square_term, quadratic)


def apply_vector(
    p: Poly,
    bosonic: tuple[Poly, Poly, Poly, Poly],
    theta: tuple[Poly, Poly],
    bartheta: tuple[Poly, Poly],
) -> Poly:
    terms = [mul(bosonic[mu], dx(mu, p)) for mu in range(4)]
    terms.extend(mul(theta[a], dg(a, p)) for a in range(2))
    terms.extend(mul(bartheta[dot], dg(2 + dot, p)) for dot in range(2))
    return add(*terms)


def zero(_: Poly) -> Poly:
    return {}


def identity(p: Poly) -> Poly:
    return p


def op_sum(*ops):
    return lambda p: add(*(op(p) for op in ops))


def op_scale(c: C, op):
    return lambda p: scale(c, op(p))


def comm(left, right):
    return lambda p: add(left(right(p)), scale(M, right(left(p))))


def anti(left, right):
    return lambda p: add(left(right(p)), right(left(p)))


def linear(terms):
    return op_sum(*(op_scale(coefficient, op) for coefficient, op in terms))


P = tuple(op_scale(MI, lambda p, mu=mu: dx(mu, p)) for mu in range(4))


def q_op(a: int):
    def result(p: Poly) -> Poly:
        terms = [scale(MI, dg(a, p))]
        for mu in range(4):
            for dot in range(2):
                coefficient = scale(SIG[mu][a][dot], BARTHETA[dot])
                terms.append(mul(coefficient, dx(mu, p)))
        return add(*terms)

    return result


def bar_q_op(dot: int):
    def result(p: Poly) -> Poly:
        terms = [scale(I, dg(2 + dot, p))]
        for mu in range(4):
            for a in range(2):
                coefficient = scale(-SIG[mu][a][dot], THETA[a])
                terms.append(mul(coefficient, dx(mu, p)))
        return add(*terms)

    return result


Q = tuple(q_op(a) for a in range(2))
BQ = tuple(bar_q_op(dot) for dot in range(2))


DIL = lambda p: apply_vector(
    p,
    tuple(scale(MI, X[mu]) for mu in range(4)),
    tuple(scale(C(0, Fraction(-1, 2)), THETA[a]) for a in range(2)),
    tuple(scale(C(0, Fraction(-1, 2)), BARTHETA[dot]) for dot in range(2)),
)

R = lambda p: apply_vector(
    p,
    ({}, {}, {}, {}),
    THETA,
    tuple(scale(M, BARTHETA[dot]) for dot in range(2)),
)


def lorentz_op(mu: int, nu: int):
    sigma_lower = mscale(C(ETA[mu] * ETA[nu]), SIGMN[mu, nu])
    barsigma_lower = mscale(C(ETA[mu] * ETA[nu]), BARMN[mu, nu])
    bosonic = tuple(
        add(
            scale(C(0, -ETA[mu]) if rho == nu else Z, X[mu]),
            scale(C(0, ETA[nu]) if rho == mu else Z, X[nu]),
        )
        for rho in range(4)
    )
    theta = tuple(
        add(*(scale(I * sigma_lower[b][a], THETA[b]) for b in range(2)))
        for a in range(2)
    )
    bartheta = tuple(
        add(*(scale(MI * barsigma_lower[dot][other], BARTHETA[other]) for other in range(2)))
        for dot in range(2)
    )
    return lambda p: apply_vector(p, bosonic, theta, bartheta)


J = {(mu, nu): lorentz_op(mu, nu) for mu in range(4) for nu in range(4)}


def k_op(mu: int):
    bosonic = tuple(
        scale(
            C(0, Fraction(-1, 2)),
            add(conformal_v(Y, mu, nu), conformal_v(BAR_Y, mu, nu)),
        )
        for nu in range(4)
    )
    theta = tuple(
        scale(
            MI,
            add(
                *(
                    mul(THETA[b], sigma_tilde_entry(SIG_LOWER[mu], TILDE_Y, b, a))
                    for b in range(2)
                )
            ),
        )
        for a in range(2)
    )
    bartheta = tuple(
        scale(
            MI,
            add(
                *(
                    mul(
                        BARTHETA[other],
                        tilde_sigma_entry(TILDE_BAR_Y, SIG_LOWER[mu], dot, other),
                    )
                    for other in range(2)
                )
            ),
        )
        for dot in range(2)
    )
    return lambda p: apply_vector(p, bosonic, theta, bartheta)


K = tuple(k_op(mu) for mu in range(4))


def s_op(up: int):
    bosonic = tuple(
        scale(
            I,
            add(
                *(
                    mul(THETA[b], sigma_tilde_entry(SIG[mu], TILDE_Y, b, up))
                    for b in range(2)
                )
            ),
        )
        for mu in range(4)
    )
    theta = tuple(scale(C(0, -2) * EPS_UP[up][b], THETA_SQUARED) for b in range(2))
    bartheta = tuple(TILDE_BAR_Y[dot][up] for dot in range(2))
    return lambda p: apply_vector(p, bosonic, theta, bartheta)


def bar_s_op(up: int):
    bosonic = tuple(
        scale(
            I,
            add(
                *(
                    mul(
                        BARTHETA[dot],
                        tilde_sigma_entry(TILDE_BAR_Y, SIG[mu], up, dot),
                    )
                    for dot in range(2)
                )
            ),
        )
        for mu in range(4)
    )
    theta = tuple(TILDE_Y[up][b] for b in range(2))
    bartheta = tuple(scale(C(0, 2) * EPS_UP[up][dot], BARTHETA_SQUARED) for dot in range(2))
    return lambda p: apply_vector(p, bosonic, theta, bartheta)


S = tuple(s_op(a) for a in range(2))
BS = tuple(bar_s_op(dot) for dot in range(2))


def separating_inputs() -> tuple[Poly, ...]:
    bosonic = [ZERO_EXP]
    bosonic.extend(tuple(1 if mu == rho else 0 for mu in range(4)) for rho in range(4))
    return tuple(basis(mask, exponents) for mask in range(16) for exponents in bosonic)


CASES = separating_inputs()
CHIRAL_CASES = tuple(
    mul(basis(mask), factor)
    for mask in range(4)
    for factor in ({(0, 0, 0, 0, 0): O}, *Y)
)
ANTICHIRAL_CASES = tuple(
    mul(basis(mask << 2), factor)
    for mask in range(4)
    for factor in ({(0, 0, 0, 0, 0): O}, *BAR_Y)
)


failures: list[str] = []
algebra_identities = 0
algebra_input_cases = 0
restriction_identities = 0
restriction_input_cases = 0
coordinate_identities = 0


def check_algebra(label: str, left, right=zero) -> None:
    global algebra_identities, algebra_input_cases
    algebra_identities += 1
    algebra_input_cases += len(CASES)
    for index, value in enumerate(CASES):
        left_value = norm(left(value))
        right_value = norm(right(value))
        if left_value != right_value:
            failures.append(
                f"algebra:{label}:case={index}:left={left_value}:right={right_value}"
            )
            return


def check_restriction(label: str, left, right, cases: tuple[Poly, ...]) -> None:
    global restriction_identities, restriction_input_cases
    restriction_identities += 1
    restriction_input_cases += len(cases)
    for index, value in enumerate(cases):
        left_value = norm(left(value))
        right_value = norm(right(value))
        if left_value != right_value:
            failures.append(
                f"restriction:{label}:case={index}:left={left_value}:right={right_value}"
            )
            return


def check_coordinate(label: str, actual: Poly, expected: Poly) -> None:
    global coordinate_identities
    coordinate_identities += 1
    if norm(actual) != norm(expected):
        failures.append(
            f"coordinate:{label}:actual={norm(actual)}:expected={norm(expected)}"
        )


# Entire unweighted Lorentzian N=1 superconformal algebra.
for a in range(2):
    for dot in range(2):
        check_algebra(
            f"QQbar[{a},{dot}]",
            anti(Q[a], BQ[dot]),
            linear((MTWO * SIG[mu][a][dot], P[mu]) for mu in range(4)),
        )
        check_algebra(f"QbarS[{a},{dot}]", anti(Q[a], BS[dot]))
        check_algebra(f"barQS[{dot},{a}]", anti(BQ[dot], S[a]))
        check_algebra(
            f"SbarS[{a},{dot}]",
            anti(S[a], BS[dot]),
            linear((MTWO * BSIG[mu][dot][a], K[mu]) for mu in range(4)),
        )

for a in range(2):
    check_algebra(f"DQ[{a}]", comm(DIL, Q[a]), op_scale(C(0, Fraction(1, 2)), Q[a]))
    check_algebra(f"RQ[{a}]", comm(R, Q[a]), op_scale(M, Q[a]))
    check_algebra(f"DS[{a}]", comm(DIL, S[a]), op_scale(C(0, Fraction(-1, 2)), S[a]))
    check_algebra(f"RS[{a}]", comm(R, S[a]), S[a])
    for mu in range(4):
        check_algebra(
            f"KQ[{mu},{a}]",
            comm(K[mu], Q[a]),
            linear((SIG_LOWER[mu][a][dot], BS[dot]) for dot in range(2)),
        )
        check_algebra(
            f"PS[{mu},{a}]",
            comm(P[mu], S[a]),
            linear((-BSIG_LOWER[mu][dot][a], BQ[dot]) for dot in range(2)),
        )
    for b in range(2):
        rhs_terms = [(C(0, -2) if a == b else Z, DIL), (C(3) if a == b else Z, R)]
        for mu in range(4):
            for nu in range(4):
                rhs_terms.append((C(0, -2) * SIGMN[mu, nu][a][b], J[mu, nu]))
        check_algebra(f"QS[{a},{b}]", anti(Q[a], S[b]), linear(rhs_terms))

for dot in range(2):
    check_algebra(
        f"DbarQ[{dot}]",
        comm(DIL, BQ[dot]),
        op_scale(C(0, Fraction(1, 2)), BQ[dot]),
    )
    check_algebra(f"RbarQ[{dot}]", comm(R, BQ[dot]), BQ[dot])
    check_algebra(
        f"DbarS[{dot}]",
        comm(DIL, BS[dot]),
        op_scale(C(0, Fraction(-1, 2)), BS[dot]),
    )
    check_algebra(f"RbarS[{dot}]", comm(R, BS[dot]), op_scale(M, BS[dot]))
    for mu in range(4):
        check_algebra(
            f"PbarS[{mu},{dot}]",
            comm(P[mu], BS[dot]),
            linear((BSIG_LOWER[mu][dot][a], Q[a]) for a in range(2)),
        )
        check_algebra(
            f"KbarQ[{mu},{dot}]",
            comm(K[mu], BQ[dot]),
            linear((-SIG_LOWER[mu][a][dot], S[a]) for a in range(2)),
        )
    for other in range(2):
        rhs_terms = [(C(0, 2) if dot == other else Z, DIL), (C(3) if dot == other else Z, R)]
        for mu in range(4):
            for nu in range(4):
                rhs_terms.append((C(0, -2) * BARMN[mu, nu][other][dot], J[mu, nu]))
        check_algebra(
            f"barQbarS[{dot},{other}]",
            anti(BQ[dot], BS[other]),
            linear(rhs_terms),
        )

for mu in range(4):
    check_algebra(f"DP[{mu}]", comm(DIL, P[mu]), op_scale(I, P[mu]))
    check_algebra(f"DK[{mu}]", comm(DIL, K[mu]), op_scale(MI, K[mu]))
    for nu in range(4):
        rhs = linear(
            (
                (C(0, 2 * ETA[mu]) if mu == nu else Z, DIL),
                (C(0, -2), J[mu, nu]),
            )
        )
        check_algebra(f"PK[{mu},{nu}]", comm(P[mu], K[nu]), rhs)

for a in range(2):
    for b in range(2):
        check_algebra(f"QQ[{a},{b}]", anti(Q[a], Q[b]))
        check_algebra(f"SS[{a},{b}]", anti(S[a], S[b]))
for dot in range(2):
    for other in range(2):
        check_algebra(f"barQbarQ[{dot},{other}]", anti(BQ[dot], BQ[other]))
        check_algebra(f"barSbarS[{dot},{other}]", anti(BS[dot], BS[other]))

for mu in range(4):
    check_algebra(f"RP[{mu}]", comm(R, P[mu]))
    check_algebra(f"RK[{mu}]", comm(R, K[mu]))
    for nu in range(4):
        check_algebra(f"PP[{mu},{nu}]", comm(P[mu], P[nu]))
        check_algebra(f"KK[{mu},{nu}]", comm(K[mu], K[nu]))
    for a in range(2):
        check_algebra(f"PQ[{mu},{a}]", comm(P[mu], Q[a]))
        check_algebra(f"KS[{mu},{a}]", comm(K[mu], S[a]))
    for dot in range(2):
        check_algebra(f"PbarQ[{mu},{dot}]", comm(P[mu], BQ[dot]))
        check_algebra(f"KbarS[{mu},{dot}]", comm(K[mu], BS[dot]))

check_algebra("DD", comm(DIL, DIL))
check_algebra("DR", comm(DIL, R))
check_algebra("RR", comm(R, R))

for mu in range(4):
    for nu in range(4):
        sigma_lower = mscale(C(ETA[mu] * ETA[nu]), SIGMN[mu, nu])
        barsigma_lower = mscale(C(ETA[mu] * ETA[nu]), BARMN[mu, nu])
        check_algebra(f"DJ[{mu},{nu}]", comm(DIL, J[mu, nu]))
        check_algebra(f"RJ[{mu},{nu}]", comm(R, J[mu, nu]))
        for a in range(2):
            check_algebra(
                f"JQ[{mu},{nu},{a}]",
                comm(J[mu, nu], Q[a]),
                linear((MI * sigma_lower[a][b], Q[b]) for b in range(2)),
            )
            check_algebra(
                f"JS[{mu},{nu},{a}]",
                comm(J[mu, nu], S[a]),
                linear((I * sigma_lower[b][a], S[b]) for b in range(2)),
            )
        for dot in range(2):
            check_algebra(
                f"JbarQ[{mu},{nu},{dot}]",
                comm(J[mu, nu], BQ[dot]),
                linear((I * barsigma_lower[other][dot], BQ[other]) for other in range(2)),
            )
            check_algebra(
                f"JbarS[{mu},{nu},{dot}]",
                comm(J[mu, nu], BS[dot]),
                linear((MI * barsigma_lower[dot][other], BS[other]) for other in range(2)),
            )
        for rho in range(4):
            check_algebra(
                f"JP[{mu},{nu},{rho}]",
                comm(J[mu, nu], P[rho]),
                linear(
                    (
                        (C(0, ETA[mu]) if rho == mu else Z, P[nu]),
                        (C(0, -ETA[nu]) if rho == nu else Z, P[mu]),
                    )
                ),
            )
            check_algebra(
                f"JK[{mu},{nu},{rho}]",
                comm(J[mu, nu], K[rho]),
                linear(
                    (
                        (C(0, ETA[mu]) if rho == mu else Z, K[nu]),
                        (C(0, -ETA[nu]) if rho == nu else Z, K[mu]),
                    )
                ),
            )
        for rho in range(4):
            for sigma in range(4):
                check_algebra(
                    f"JJ[{mu},{nu},{rho},{sigma}]",
                    comm(J[mu, nu], J[rho, sigma]),
                    linear(
                        (
                            (C(0, ETA[mu]) if rho == mu else Z, J[nu, sigma]),
                            (C(0, -ETA[nu]) if rho == nu else Z, J[mu, sigma]),
                            (C(0, -ETA[mu]) if sigma == mu else Z, J[nu, rho]),
                            (C(0, ETA[nu]) if sigma == nu else Z, J[mu, rho]),
                        )
                    ),
                )


# Exact coordinate actions obtained by superinversion conjugation.
for mu in range(4):
    for nu in range(4):
        check_coordinate(f"K[{mu}]y[{nu}]", K[mu](Y[nu]), scale(MI, conformal_v(Y, mu, nu)))
        check_coordinate(
            f"K[{mu}]bary[{nu}]",
            K[mu](BAR_Y[nu]),
            scale(MI, conformal_v(BAR_Y, mu, nu)),
        )
    for a in range(2):
        expected = scale(
            MI,
            add(
                *(
                    mul(THETA[b], sigma_tilde_entry(SIG_LOWER[mu], TILDE_Y, b, a))
                    for b in range(2)
                )
            ),
        )
        check_coordinate(f"K[{mu}]theta[{a}]", K[mu](THETA[a]), expected)
    for dot in range(2):
        expected = scale(
            MI,
            add(
                *(
                    mul(
                        BARTHETA[other],
                        tilde_sigma_entry(TILDE_BAR_Y, SIG_LOWER[mu], dot, other),
                    )
                    for other in range(2)
                )
            ),
        )
        check_coordinate(f"K[{mu}]bartheta[{dot}]", K[mu](BARTHETA[dot]), expected)

for up in range(2):
    for mu in range(4):
        expected_s_y = scale(
            C(0, 2),
            add(
                *(
                    mul(THETA[b], sigma_tilde_entry(SIG[mu], TILDE_Y, b, up))
                    for b in range(2)
                )
            ),
        )
        check_coordinate(f"S[{up}]y[{mu}]", S[up](Y[mu]), expected_s_y)
        check_coordinate(f"S[{up}]bary[{mu}]", S[up](BAR_Y[mu]), {})
        check_coordinate(f"barS[{up}]y[{mu}]", BS[up](Y[mu]), {})
        expected_bs_bary = scale(
            C(0, 2),
            add(
                *(
                    mul(
                        BARTHETA[dot],
                        tilde_sigma_entry(TILDE_BAR_Y, SIG[mu], up, dot),
                    )
                    for dot in range(2)
                )
            ),
        )
        check_coordinate(f"barS[{up}]bary[{mu}]", BS[up](BAR_Y[mu]), expected_bs_bary)
    for b in range(2):
        check_coordinate(
            f"S[{up}]theta[{b}]",
            S[up](THETA[b]),
            scale(C(0, -2) * EPS_UP[up][b], THETA_SQUARED),
        )
        check_coordinate(f"barS[{up}]theta[{b}]", BS[up](THETA[b]), TILDE_Y[up][b])
    for dot in range(2):
        check_coordinate(
            f"S[{up}]bartheta[{dot}]",
            S[up](BARTHETA[dot]),
            TILDE_BAR_Y[dot][up],
        )
        check_coordinate(
            f"barS[{up}]bartheta[{dot}]",
            BS[up](BARTHETA[dot]),
            scale(C(0, 2) * EPS_UP[up][dot], BARTHETA_SQUARED),
        )


# Chart derivatives, with every odd derivative acting from the left.
def dtheta_at_y(a: int, p: Poly) -> Poly:
    terms = [dg(a, p)]
    for mu in range(4):
        for dot in range(2):
            terms.append(
                mul(scale(I * SIG[mu][a][dot], BARTHETA[dot]), dx(mu, p))
            )
    return add(*terms)


def dbartheta_at_bary(dot: int, p: Poly) -> Poly:
    terms = [dg(2 + dot, p)]
    for mu in range(4):
        for a in range(2):
            terms.append(mul(scale(I * SIG[mu][a][dot], THETA[a]), dx(mu, p)))
    return add(*terms)


def k_chiral(mu: int):
    def result(p: Poly) -> Poly:
        terms = [mul(scale(MI, conformal_v(Y, mu, nu)), dx(nu, p)) for nu in range(4)]
        for a in range(2):
            coefficient = scale(
                MI,
                add(
                    *(
                        mul(THETA[b], sigma_tilde_entry(SIG_LOWER[mu], TILDE_Y, b, a))
                        for b in range(2)
                    )
                ),
            )
            terms.append(mul(coefficient, dtheta_at_y(a, p)))
        return add(*terms)

    return result


def s_chiral(up: int):
    def result(p: Poly) -> Poly:
        terms = []
        for mu in range(4):
            coefficient = scale(
                C(0, 2),
                add(
                    *(
                        mul(THETA[b], sigma_tilde_entry(SIG[mu], TILDE_Y, b, up))
                        for b in range(2)
                    )
                ),
            )
            terms.append(mul(coefficient, dx(mu, p)))
        for b in range(2):
            coefficient = scale(C(0, -2) * EPS_UP[up][b], THETA_SQUARED)
            terms.append(mul(coefficient, dtheta_at_y(b, p)))
        return add(*terms)

    return result


def bar_s_chiral(up: int):
    return lambda p: add(*(mul(TILDE_Y[up][b], dtheta_at_y(b, p)) for b in range(2)))


def k_antichiral(mu: int):
    def result(p: Poly) -> Poly:
        terms = [
            mul(scale(MI, conformal_v(BAR_Y, mu, nu)), dx(nu, p))
            for nu in range(4)
        ]
        for dot in range(2):
            coefficient = scale(
                MI,
                add(
                    *(
                        mul(
                            BARTHETA[other],
                            tilde_sigma_entry(TILDE_BAR_Y, SIG_LOWER[mu], dot, other),
                        )
                        for other in range(2)
                    )
                ),
            )
            terms.append(mul(coefficient, dbartheta_at_bary(dot, p)))
        return add(*terms)

    return result


def s_antichiral(up: int):
    return lambda p: add(
        *(mul(TILDE_BAR_Y[dot][up], dbartheta_at_bary(dot, p)) for dot in range(2))
    )


def bar_s_antichiral(up: int):
    def result(p: Poly) -> Poly:
        terms = []
        for mu in range(4):
            coefficient = scale(
                C(0, 2),
                add(
                    *(
                        mul(
                            BARTHETA[dot],
                            tilde_sigma_entry(TILDE_BAR_Y, SIG[mu], up, dot),
                        )
                        for dot in range(2)
                    )
                ),
            )
            terms.append(mul(coefficient, dx(mu, p)))
        for dot in range(2):
            coefficient = scale(C(0, 2) * EPS_UP[up][dot], BARTHETA_SQUARED)
            terms.append(mul(coefficient, dbartheta_at_bary(dot, p)))
        return add(*terms)

    return result


for mu in range(4):
    check_restriction(f"K_ch[{mu}]", K[mu], k_chiral(mu), CHIRAL_CASES)
    check_restriction(f"K_ach[{mu}]", K[mu], k_antichiral(mu), ANTICHIRAL_CASES)
for up in range(2):
    check_restriction(f"S_ch[{up}]", S[up], s_chiral(up), CHIRAL_CASES)
    check_restriction(f"barS_ch[{up}]", BS[up], bar_s_chiral(up), CHIRAL_CASES)
    check_restriction(f"S_ach[{up}]", S[up], s_antichiral(up), ANTICHIRAL_CASES)
    check_restriction(f"barS_ach[{up}]", BS[up], bar_s_antichiral(up), ANTICHIRAL_CASES)


audit = {
    "schema": 1,
    "task_id": "CONTRACT-STEP-02C-COMPLETE-SUPERCONFORMAL-COVARIANCE-001",
    "signature": "Lorentzian (-,+,+,+)",
    "chart": "full superspace (x^mu,vartheta^a,barvartheta^dot_a)",
    "arithmetic": "Q(i) polynomial coefficients and exact four-generator exterior algebra; no floating point; no CAS",
    "basis": {
        "commuting_coordinates": 4,
        "grassmann_generators": 4,
        "grassmann_monomials": 16,
        "bosonic_factors": ["1", "x^0", "x^1", "x^2", "x^3"],
        "separating_inputs": len(CASES),
        "separation_proof": (
            "A coefficient-left first-order operator is determined by its action on 1 and on "
            "the eight coordinate generators; these occur in the stated basis. Tensoring each "
            "bosonic factor with all 16 exterior monomials additionally checks every left-odd-derivative sign."
        ),
        "chiral_restriction_inputs": len(CHIRAL_CASES),
        "antichiral_restriction_inputs": len(ANTICHIRAL_CASES),
    },
    "superinversion_phase": "phi=0 convention of contract equation 2B.32",
    "coverage": {
        "algebra_operator_identities": algebra_identities,
        "algebra_input_cases": algebra_input_cases,
        "coordinate_action_identities": coordinate_identities,
        "restriction_operator_identities": restriction_identities,
        "restriction_input_cases": restriction_input_cases,
        "total_exact_cases": algebra_input_cases + coordinate_identities + restriction_input_cases,
    },
    "failed_cases": len(failures),
    "failures": failures,
    "status": "PASS" if not failures else "FAIL",
}

root = Path(__file__).resolve().parents[1]
path = root / "audits" / "step2c-full-lorentz-verification.json"
rendered = json.dumps(audit, indent=2, sort_keys=True) + "\n"
path.write_text(rendered, encoding="utf-8")
print(rendered, end="")
raise SystemExit(1 if failures else 0)
