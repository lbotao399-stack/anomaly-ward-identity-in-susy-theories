#!/usr/bin/env python3
"""Exact exploratory verifier for the Step-2B Lorentzian chiral chart."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
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
        return C(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, C) and self.r == other.r and self.i == other.i

    def __repr__(self) -> str:
        return f"C({self.r},{self.i})"

    def zero(self) -> bool:
        return self.r == 0 and self.i == 0


Z, O, M, I, MI, TWO, MTWO, HALF = C(), C(1), C(-1), C(0, 1), C(0, -1), C(2), C(-2), C(Fraction(1, 2))
ETA = (-1, 1, 1, 1)
Key = tuple[int, int, int, int, int]
Poly = dict[Key, C]
Op = object


def norm(p: Poly) -> Poly:
    return {k: v for k, v in p.items() if not v.zero()}


def add(*values: Poly) -> Poly:
    out: Poly = {}
    for p in values:
        for key, coefficient in p.items():
            out[key] = out.get(key, Z) + coefficient
    return norm(out)


def scale(c: C, p: Poly) -> Poly:
    return norm({key: c * value for key, value in p.items()})


def basis(mask: int, exponents: tuple[int, int, int, int]) -> Poly:
    return {(mask, *exponents): O}


def mul_y(mu: int, p: Poly) -> Poly:
    out: Poly = {}
    for key, coefficient in p.items():
        values = list(key)
        values[1 + mu] += 1
        new = tuple(values)
        out[new] = out.get(new, Z) + coefficient
    return norm(out)


def dy(mu: int, p: Poly) -> Poly:
    out: Poly = {}
    for key, coefficient in p.items():
        power = key[1 + mu]
        if not power:
            continue
        values = list(key)
        values[1 + mu] -= 1
        new = tuple(values)
        out[new] = out.get(new, Z) + C(power) * coefficient
    return norm(out)


def mul_t(a: int, p: Poly) -> Poly:
    bit = 1 << a
    out: Poly = {}
    for key, coefficient in p.items():
        mask = key[0]
        if mask & bit:
            continue
        sign = M if (mask & (bit - 1)).bit_count() % 2 else O
        new = (mask | bit, *key[1:])
        out[new] = out.get(new, Z) + sign * coefficient
    return norm(out)


def dt(a: int, p: Poly) -> Poly:
    bit = 1 << a
    out: Poly = {}
    for key, coefficient in p.items():
        mask = key[0]
        if not mask & bit:
            continue
        sign = M if (mask & (bit - 1)).bit_count() % 2 else O
        new = (mask ^ bit, *key[1:])
        out[new] = out.get(new, Z) + sign * coefficient
    return norm(out)


def mm(a: tuple[tuple[C, C], tuple[C, C]], b: tuple[tuple[C, C], tuple[C, C]]) -> tuple[tuple[C, C], tuple[C, C]]:
    return tuple(tuple(sum_c((a[r][k] * b[k][c] for k in range(2))) for c in range(2)) for r in range(2))  # type: ignore[return-value]


def sum_c(values) -> C:
    out = Z
    for value in values:
        out = out + value
    return out


def msub(a, b):
    return tuple(tuple(a[r][c] - b[r][c] for c in range(2)) for r in range(2))


def mscale(c: C, a):
    return tuple(tuple(c * a[r][s] for s in range(2)) for r in range(2))


SID = ((O, Z), (Z, O))
S1 = ((Z, O), (O, Z))
S2 = ((Z, MI), (I, Z))
S3 = ((O, Z), (Z, M))
SIG = (SID, S1, S2, S3)
BSIG = (SID, mscale(M, S1), mscale(M, S2), mscale(M, S3))
SIG_LOWER = tuple(mscale(C(ETA[mu]), SIG[mu]) for mu in range(4))
BSIG_LOWER = tuple(mscale(C(ETA[mu]), BSIG[mu]) for mu in range(4))
SIGMN = {}
BARMN = {}
for mu in range(4):
    for nu in range(4):
        SIGMN[mu, nu] = mscale(C(Fraction(1, 4)), msub(mm(SIG[mu], BSIG[nu]), mm(SIG[nu], BSIG[mu])))
        BARMN[mu, nu] = mscale(C(Fraction(1, 4)), msub(mm(BSIG[mu], SIG[nu]), mm(BSIG[nu], SIG[mu])))


def op_sum(*ops):
    return lambda p: add(*(op(p) for op in ops))


def op_scale(c: C, op):
    return lambda p: scale(c, op(p))


def compose(left, right):
    return lambda p: left(right(p))


def comm(left, right):
    return lambda p: add(left(right(p)), scale(M, right(left(p))))


def anti(left, right):
    return lambda p: add(left(right(p)), right(left(p)))


def zero(_: Poly) -> Poly:
    return {}


def y_then_d(mu: int, nu: int):
    return lambda p: mul_y(mu, dy(nu, p))


def t_then_d(a: int, b: int):
    return lambda p: mul_t(a, dt(b, p))


P = tuple(op_scale(MI, lambda p, mu=mu: dy(mu, p)) for mu in range(4))
Q = tuple(op_scale(MI, lambda p, a=a: dt(a, p)) for a in range(2))


def bar_q(dot: int):
    terms = []
    for a in range(2):
        for mu in range(4):
            terms.append(op_scale(MTWO * SIG[mu][a][dot], lambda p, a=a, mu=mu: mul_t(a, dy(mu, p))))
    return op_sum(*terms)


BQ = tuple(bar_q(dot) for dot in range(2))


E = op_sum(*(y_then_d(mu, mu) for mu in range(4)))
N = op_sum(*(t_then_d(a, a) for a in range(2)))
DIL = op_scale(MI, op_sum(E, op_scale(HALF, N)))
R = N


def lorentz(mu: int, nu: int):
    orbital = op_scale(MI, op_sum(op_scale(C(ETA[mu]), y_then_d(mu, nu)), op_scale(C(-ETA[nu]), y_then_d(nu, mu))))
    spin_terms = []
    sigma_lower = mscale(C(ETA[mu] * ETA[nu]), SIGMN[mu, nu])
    for a in range(2):
        for b in range(2):
            spin_terms.append(op_scale(I * sigma_lower[a][b], t_then_d(a, b)))
    return op_sum(orbital, *spin_terms)


J = {(mu, nu): lorentz(mu, nu) for mu in range(4) for nu in range(4)}


def y_squared_then_d(mu: int):
    terms = []
    for rho in range(4):
        terms.append(op_scale(C(ETA[rho]), lambda p, rho=rho, mu=mu: mul_y(rho, mul_y(rho, dy(mu, p)))))
    return op_sum(*terms)


def tilde_y_entry(dot: int, a: int, p: Poly) -> Poly:
    terms = []
    for nu in range(4):
        terms.append(scale(C(ETA[nu]) * BSIG[nu][dot][a], mul_y(nu, p)))
    return add(*terms)


def k_op(mu: int):
    terms = [y_squared_then_d(mu), op_scale(C(-2 * ETA[mu]), lambda p, mu=mu: mul_y(mu, E(p)))]
    matrix_terms = []
    for b in range(2):
        for a in range(2):
            for dot in range(2):
                coefficient = SIG_LOWER[mu][b][dot]
                matrix_terms.append(
                    op_scale(
                        coefficient,
                        lambda p, b=b, a=a, dot=dot: mul_t(b, tilde_y_entry(dot, a, dt(a, p))),
                    )
                )
    return op_scale(MI, op_sum(*terms, *matrix_terms))


K = tuple(k_op(mu) for mu in range(4))


def bar_s(dot: int):
    return op_sum(*(lambda p, dot=dot, a=a: tilde_y_entry(dot, a, dt(a, p)) for a in range(2)))


BS = tuple(bar_s(dot) for dot in range(2))
EPS_UP = ((Z, O), (M, Z))


def theta_squared(p: Poly) -> Poly:
    # theta^a theta_a = -2 theta^1 theta^2 in the Step-1 epsilon convention.
    return scale(MTWO, mul_t(0, mul_t(1, p)))


def s_op(up: int):
    terms = []
    for b in range(2):
        for mu in range(4):
            for dot in range(2):
                coefficient = C(0, 2) * SIG[mu][b][dot]
                terms.append(
                    op_scale(
                        coefficient,
                        lambda p, b=b, mu=mu, dot=dot, up=up: mul_t(
                            b, tilde_y_entry(dot, up, dy(mu, p))
                        ),
                    )
                )
    for b in range(2):
        terms.append(
            op_scale(
                C(0, -2) * EPS_UP[up][b],
                lambda p, b=b: theta_squared(dt(b, p)),
            )
        )
    return op_sum(*terms)


S = tuple(s_op(a) for a in range(2))


def linear(terms):
    return op_sum(*(op_scale(c, op) for c, op in terms))


def test_inputs():
    exponents = []
    for values in product(range(3), repeat=4):
        if sum(values) <= 2:
            exponents.append(values)
    return tuple(basis(mask, values) for mask in range(4) for values in exponents)


CASES = test_inputs()
failures: list[str] = []
checks = 0


def check(label: str, left, right=zero):
    global checks
    checks += 1
    for index, value in enumerate(CASES):
        if norm(left(value)) != norm(right(value)):
            failures.append(f"{label}:case={index}:left={left(value)}:right={right(value)}")
            return


for a in range(2):
    for dot in range(2):
        check(
            f"QQbar[{a},{dot}]",
            anti(Q[a], BQ[dot]),
            linear((MTWO * SIG[mu][a][dot], P[mu]) for mu in range(4)),
        )
        check(f"QbarS[{a},{dot}]", anti(Q[a], BS[dot]))
        check(f"barQS[{dot},{a}]", anti(BQ[dot], S[a]))
        check(
            f"SbarS[{a},{dot}]",
            anti(S[a], BS[dot]),
            linear((MTWO * BSIG[mu][dot][a], K[mu]) for mu in range(4)),
        )

for a in range(2):
    check(f"DQ[{a}]", comm(DIL, Q[a]), op_scale(C(0, Fraction(1, 2)), Q[a]))
    check(f"RQ[{a}]", comm(R, Q[a]), op_scale(M, Q[a]))
    check(f"DS[{a}]", comm(DIL, S[a]), op_scale(C(0, Fraction(-1, 2)), S[a]))
    check(f"RS[{a}]", comm(R, S[a]), S[a])
    for mu in range(4):
        check(
            f"KQ[{mu},{a}]",
            comm(K[mu], Q[a]),
            linear((SIG_LOWER[mu][a][dot], BS[dot]) for dot in range(2)),
        )
        check(
            f"PS[{mu},{a}]",
            comm(P[mu], S[a]),
            linear((-BSIG_LOWER[mu][dot][a], BQ[dot]) for dot in range(2)),
        )
    for b in range(2):
        rhs_terms = [(C(0, -2) if a == b else Z, DIL), (C(3) if a == b else Z, R)]
        for mu in range(4):
            for nu in range(4):
                rhs_terms.append((C(0, -2) * SIGMN[mu, nu][a][b], J[mu, nu]))
        check(f"QS[{a},{b}]", anti(Q[a], S[b]), linear(rhs_terms))

for dot in range(2):
    check(f"DbarQ[{dot}]", comm(DIL, BQ[dot]), op_scale(C(0, Fraction(1, 2)), BQ[dot]))
    check(f"RbarQ[{dot}]", comm(R, BQ[dot]), BQ[dot])
    check(f"DbarS[{dot}]", comm(DIL, BS[dot]), op_scale(C(0, Fraction(-1, 2)), BS[dot]))
    check(f"RbarS[{dot}]", comm(R, BS[dot]), op_scale(M, BS[dot]))
    for mu in range(4):
        check(
            f"PbarS[{mu},{dot}]",
            comm(P[mu], BS[dot]),
            linear((BSIG_LOWER[mu][dot][a], Q[a]) for a in range(2)),
        )
        check(
            f"KbarQ[{mu},{dot}]",
            comm(K[mu], BQ[dot]),
            linear((-SIG_LOWER[mu][a][dot], S[a]) for a in range(2)),
        )
    for other in range(2):
        rhs_terms = [(C(0, 2) if dot == other else Z, DIL), (C(3) if dot == other else Z, R)]
        for mu in range(4):
            for nu in range(4):
                rhs_terms.append((C(0, -2) * BARMN[mu, nu][other][dot], J[mu, nu]))
        check(f"barQbarS[{dot},{other}]", anti(BQ[dot], BS[other]), linear(rhs_terms))

for mu in range(4):
    check(f"DP[{mu}]", comm(DIL, P[mu]), op_scale(I, P[mu]))
    check(f"DK[{mu}]", comm(DIL, K[mu]), op_scale(MI, K[mu]))
    for nu in range(4):
        rhs = linear(((C(0, 2 * ETA[mu]) if mu == nu else Z, DIL), (C(0, -2), J[mu, nu])))
        check(f"PK[{mu},{nu}]", comm(P[mu], K[nu]), rhs)

# Same-chirality odd brackets.
for a in range(2):
    for b in range(2):
        check(f"QQ[{a},{b}]", anti(Q[a], Q[b]))
        check(f"SS[{a},{b}]", anti(S[a], S[b]))
for dot in range(2):
    for other in range(2):
        check(f"barQbarQ[{dot},{other}]", anti(BQ[dot], BQ[other]))
        check(f"barSbarS[{dot},{other}]", anti(BS[dot], BS[other]))

# Translation/special-conformal sectors and their odd stabilizers.
for mu in range(4):
    check(f"RP[{mu}]", comm(R, P[mu]))
    check(f"RK[{mu}]", comm(R, K[mu]))
    for nu in range(4):
        check(f"PP[{mu},{nu}]", comm(P[mu], P[nu]))
        check(f"KK[{mu},{nu}]", comm(K[mu], K[nu]))
    for a in range(2):
        check(f"PQ[{mu},{a}]", comm(P[mu], Q[a]))
        check(f"KS[{mu},{a}]", comm(K[mu], S[a]))
    for dot in range(2):
        check(f"PbarQ[{mu},{dot}]", comm(P[mu], BQ[dot]))
        check(f"KbarS[{mu},{dot}]", comm(K[mu], BS[dot]))

check("DR", comm(DIL, R))

# Lorentz action on every generator.
for mu in range(4):
    for nu in range(4):
        sigma_lower = mscale(C(ETA[mu] * ETA[nu]), SIGMN[mu, nu])
        barsigma_lower = mscale(C(ETA[mu] * ETA[nu]), BARMN[mu, nu])
        check(f"DJ[{mu},{nu}]", comm(DIL, J[mu, nu]))
        check(f"RJ[{mu},{nu}]", comm(R, J[mu, nu]))
        for a in range(2):
            check(
                f"JQ[{mu},{nu},{a}]",
                comm(J[mu, nu], Q[a]),
                linear((MI * sigma_lower[a][b], Q[b]) for b in range(2)),
            )
            check(
                f"JS[{mu},{nu},{a}]",
                comm(J[mu, nu], S[a]),
                linear((I * sigma_lower[b][a], S[b]) for b in range(2)),
            )
        for dot in range(2):
            check(
                f"JbarQ[{mu},{nu},{dot}]",
                comm(J[mu, nu], BQ[dot]),
                linear((I * barsigma_lower[other][dot], BQ[other]) for other in range(2)),
            )
            check(
                f"JbarS[{mu},{nu},{dot}]",
                comm(J[mu, nu], BS[dot]),
                linear((MI * barsigma_lower[dot][other], BS[other]) for other in range(2)),
            )
        for rho in range(4):
            check(
                f"JP[{mu},{nu},{rho}]",
                comm(J[mu, nu], P[rho]),
                linear(
                    (
                        (C(0, ETA[mu]) if rho == mu else Z, P[nu]),
                        (C(0, -ETA[nu]) if rho == nu else Z, P[mu]),
                    )
                ),
            )
            check(
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
                check(
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

# Scalar chiral-primary modules.  Closure fixes r=-2 Delta/3.
IDENTITY = lambda p: p
for delta in (Fraction(-1), Fraction(1, 2), Fraction(3, 2), Fraction(2)):
    delta_c = C(delta)
    r_c = C(Fraction(-2, 3) * delta)
    d_delta = op_sum(DIL, op_scale(MI * delta_c, IDENTITY))
    r_delta = op_sum(R, op_scale(r_c, IDENTITY))
    k_delta = tuple(
        op_sum(
            K[mu],
            op_scale(C(0, 2 * ETA[mu]) * delta_c, lambda p, mu=mu: mul_y(mu, p)),
        )
        for mu in range(4)
    )
    s_delta = tuple(
        op_sum(S[a], op_scale(C(0, -4) * delta_c, lambda p, a=a: mul_t(a, p)))
        for a in range(2)
    )
    label_delta = str(delta)
    for a in range(2):
        check(f"weighted:DQ[{label_delta},{a}]", comm(d_delta, Q[a]), op_scale(C(0, Fraction(1, 2)), Q[a]))
        check(f"weighted:DS[{label_delta},{a}]", comm(d_delta, s_delta[a]), op_scale(C(0, Fraction(-1, 2)), s_delta[a]))
        check(f"weighted:RQ[{label_delta},{a}]", comm(r_delta, Q[a]), op_scale(M, Q[a]))
        check(f"weighted:RS[{label_delta},{a}]", comm(r_delta, s_delta[a]), s_delta[a])
        for b in range(2):
            rhs_terms = [(C(0, -2) if a == b else Z, d_delta), (C(3) if a == b else Z, r_delta)]
            for mu in range(4):
                for nu in range(4):
                    rhs_terms.append((C(0, -2) * SIGMN[mu, nu][a][b], J[mu, nu]))
            check(f"weighted:QS[{label_delta},{a},{b}]", anti(Q[a], s_delta[b]), linear(rhs_terms))
        for dot in range(2):
            check(
                f"weighted:SbarS[{label_delta},{a},{dot}]",
                anti(s_delta[a], BS[dot]),
                linear((MTWO * BSIG[mu][dot][a], k_delta[mu]) for mu in range(4)),
            )
    for dot in range(2):
        for other in range(2):
            rhs_terms = [(C(0, 2) if dot == other else Z, d_delta), (C(3) if dot == other else Z, r_delta)]
            for mu in range(4):
                for nu in range(4):
                    rhs_terms.append((C(0, -2) * BARMN[mu, nu][other][dot], J[mu, nu]))
            check(
                f"weighted:barQbarS[{label_delta},{dot},{other}]",
                anti(BQ[dot], BS[other]),
                linear(rhs_terms),
            )
    for mu in range(4):
        for nu in range(4):
            rhs = linear(((C(0, 2 * ETA[mu]) if mu == nu else Z, d_delta), (C(0, -2), J[mu, nu])))
            check(f"weighted:PK[{label_delta},{mu},{nu}]", comm(P[mu], k_delta[nu]), rhs)
        for dot in range(2):
            check(
                f"weighted:KbarQ[{label_delta},{mu},{dot}]",
                comm(k_delta[mu], BQ[dot]),
                linear((-SIG_LOWER[mu][a][dot], s_delta[a]) for a in range(2)),
            )

audit = {
    "schema": 1,
    "task_id": "CONTRACT-STEP-02B-SUPERCONFORMAL-001",
    "signature": "Lorentzian",
    "chart": "chiral (y^mu,vartheta^a)",
    "arithmetic": "Q(i) polynomial coefficients and exact exterior algebra; no floating point; no CAS",
    "basis": {
        "grassmann_monomials": 4,
        "bosonic_monomials_total_degree_at_most_2": len(CASES) // 4,
        "total_inputs": len(CASES),
    },
    "superinversion_phase": "the explicit plus/minus i convention declared in contract equation 2B.32",
    "weighted_chiral_modules": {
        "tested_Delta": ["-1", "1/2", "3/2", "2"],
        "closure_relation": "r=-2 Delta/3",
    },
    "operator_identities": checks,
    "input_cases": checks * len(CASES),
    "failed_cases": len(failures),
    "failures": failures,
    "status": "PASS" if not failures else "FAIL",
}
root = Path(__file__).resolve().parents[1]
path = root / "audits" / "step2b-lorentzian-superconformal-verification.json"
rendered = json.dumps(audit, indent=2, sort_keys=True) + "\n"
path.write_text(rendered, encoding="utf-8")
print(rendered, end="")
raise SystemExit(1 if failures else 0)
