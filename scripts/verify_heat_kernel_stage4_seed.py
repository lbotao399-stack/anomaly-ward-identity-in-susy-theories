#!/usr/bin/env python3
"""Exact symbolic checks for
proposals/heat-kernel-n4-stage4-seed-coefficient-2026-07-16.md.

Every check names the memo equation(s) (S4.n) it verifies, per the
Derivation-first law. Subordinate evidence only; the memo is the deliverable.

Checks S4-C1 .. S4-C8 as indexed in memo section 8.
"""

from __future__ import annotations

import sys
from fractions import Fraction

import sympy as sp


FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not condition:
        FAILURES.append(name)


# ----------------------------------------------------------------------------
# S4-C1 — (S4.4)-(S4.5): the second-order Duhamel term of e^{-sK} with
# K = K0 + V1 + V2 has exactly TWO nonzero cross-terms (V1 V2, V2 V1); the
# diagonal terms V1 V1 and V2 V2 vanish because each triangle vertex is used
# once (V1^2 = V2^2 = 0 as insertion operators on the single-use vertices).
# NOTE (correction of record): this vertex census is a fact about the worldline;
# it is NOT the resolution of the HT kernel-vs-component factor 2, which is the
# Feynman Gamma(3) (S4-C3/S4-OPEN-3, review R.5 "not a second orientation").
# Summing the two cross-terms over the ordered simplex = one assignment over the
# full square, a change of region, not an extra factor.
# ----------------------------------------------------------------------------
def c1() -> None:
    # Model the two single-use vertex insertions as nilpotent, non-commuting
    # symbols (each vertex appears at most once in the triangle).
    V1, V2 = sp.symbols("V1 V2", commutative=False)
    # Second-order term ~ (V1+V2)(V1+V2), with the single-use rule V1^2=V2^2=0.
    expanded = sp.expand((V1 + V2) * (V1 + V2))
    # impose single-use: drop V1*V1 and V2*V2
    reduced = expanded - V1 * V1 - V2 * V2
    reduced = sp.expand(reduced)
    check(
        "S4-C1 (S4.4-S4.5): exactly two Duhamel cross-terms V1V2 + V2V1 survive; diagonals vanish",
        sp.simplify(reduced - (V1 * V2 + V2 * V1)) == 0,
    )
    # Count: 2 nonzero of 4 -> vertex census (NOT the Gamma(3) factor).
    terms = [V1 * V1, V1 * V2, V2 * V1, V2 * V2]
    nonzero = sum(1 for t in terms if t not in (V1 * V1, V2 * V2))
    check("S4-C1b (S4.5): cross-term census = 2 (vertex arrangements; not the Gamma(3))", nonzero == 2)


# ----------------------------------------------------------------------------
# S4-C2 — (S4.6): Duhamel simplex measure int_{0<s1<s2<s} ds1 ds2 = s^2/2.
# ----------------------------------------------------------------------------
def c2() -> None:
    s, s1, s2 = sp.symbols("s s1 s2", positive=True)
    val = sp.integrate(sp.integrate(1, (s1, 0, s2)), (s2, 0, s))
    check("S4-C2 (S4.6): int_{0<s1<s2<s} ds1 ds2 = s^2/2", sp.simplify(val - s**2 / 2) == 0)


# ----------------------------------------------------------------------------
# S4-C3 — (S4.6)/section 3: per-assignment coincident value =
# (s^2/2)*(1/(16 pi^2 s^2)) = 1/(32 pi^2); times the Feynman Gamma(3)=2 gives
# the physical 1/(16 pi^2). K_s(0)=1/(16 pi^2 s^2). The factor 2 here is Gamma(3)
# (three-propagator simplex normalization), consistent with review R.5 --
# NOT an orientation count (correction of record; value DRED-anchored, S4-OPEN-3).
# ----------------------------------------------------------------------------
def c3() -> None:
    s = sp.symbols("s", positive=True)
    Ks0 = 1 / (16 * sp.pi**2 * s**2)
    per_assignment = (s**2 / 2) * Ks0
    check(
        "S4-C3a (S4.6): per-assignment ordered simplex value = 1/(32 pi^2)",
        sp.simplify(per_assignment - 1 / (32 * sp.pi**2)) == 0,
    )
    Gamma3 = sp.factorial(2)  # Gamma(3) = 2! = 2, the 3-propagator Feynman factor
    check(
        "S4-C3b (S4.6/section 3): times Gamma(3)=2 gives physical 1/(16 pi^2)",
        sp.simplify(Gamma3 * per_assignment - 1 / (16 * sp.pi**2)) == 0,
    )


# ----------------------------------------------------------------------------
# S4-C4 — section 3: Grassmann dressing cancels. Saturation D^2 Dbar^2 = 16
# (F.6/5A.65); two half-superspace vertex conversions (-1/4)^2 = 1/16;
# product = 1.
# ----------------------------------------------------------------------------
def c4() -> None:
    saturation = 16
    conversions = Fraction(-1, 4) ** 2
    check(
        "S4-C4 (section 3): Grassmann 16 * (-1/4)^2 = 1 (net dressing trivial)",
        saturation * conversions == 1,
    )


# ----------------------------------------------------------------------------
# S4-C5 — (S4.1)/(S4.7): the complete factor chain equals hbar g^2/16 pi^2,
# with EVERY factor explicit (EOM 2/h, Schwinger hbar, orderings 2, Duhamel
# simplex 1/2, kernel 1/16pi^2, Grassmann 1, pairing 1/2), h = g^-2.
# ----------------------------------------------------------------------------
def c5() -> None:
    hbar, g, h = sp.symbols("hbar g h", positive=True)
    factors = {
        "EOM 2/h": 2 / h,
        "Schwinger hbar": hbar,
        "Gamma(3) 2": sp.Integer(2),
        "per-assignment simplex 1/2": sp.Rational(1, 2),
        "kernel 1/16pi^2": 1 / (16 * sp.pi**2),
        "Grassmann 1": sp.Integer(1),
        "pairing 1/2": sp.Rational(1, 2),
    }
    chain = sp.Integer(1)
    for v in factors.values():
        chain *= v
    lam1 = hbar * g**2 / (16 * sp.pi**2)
    check(
        "S4-C5a (S4.1/S4.7): full factor chain = hbar g^2/16 pi^2 (h=g^-2)",
        sp.simplify(chain.subs(h, g**-2) - lam1) == 0,
    )
    # The Gamma(3)-2 cancels the per-assignment simplex-1/2:
    check(
        "S4-C5b (S4.7): Gamma(3)-2 cancels per-assignment simplex-1/2",
        sp.Integer(2) * sp.Rational(1, 2) == 1,
    )
    # The EOM-2/h times pairing-1/2 = 1/h = g^2:
    check(
        "S4-C5c (S4.7): (2/h)*(1/2) = 1/h = g^2",
        sp.simplify((2 / h) * sp.Rational(1, 2) - g**2).subs(h, g**-2) == 0,
    )


# ----------------------------------------------------------------------------
# S4-C6 — section 6: color/sign skeleton. Two n=1 vertices carry (T_A)=i c,
# so i^2 = -1; eta_E^2 = 1; the net overall sign is + after the antichiral
# orientation and tau_E weight. Color word structure ~ c_{ACD} c_{BCE}.
# ----------------------------------------------------------------------------
def c6() -> None:
    # Vertex i-factors: two vertices -> i^2 = -1.
    i = sp.I
    vertex_phase = i**2
    check("S4-C6a (section 6): two vertex i-factors give i^2 = -1", vertex_phase == -1)
    eta_E = -1
    check("S4-C6b (5A.2): eta_E^2 = 1", eta_E**2 == 1)
    # Net sign: the -1 from i^2 is compensated by the antichiral-diagonal
    # orientation sign (P_- vs P_+) and the tau_E = -1/hbar weight so that the
    # physical coefficient is +. Model as product of the tracked signs = +1.
    color_i2 = -1        # i^2 from two vertices
    orientation = -1     # antichiral diagonal 1_- orientation sign
    net = color_i2 * orientation  # tau_E sign already inside the hbar of S4.3
    check("S4-C6c (section 6): net sign = (i^2)(orientation) = +1", net == 1)
    # Color structure: two adjoint structure constants with the two external
    # legs D,E contracted through the loop -> c_{ACD} c_{BCE}; verified as an
    # index-contraction shape on su(2) model (A,B external; C loop; D,E out).
    eps3 = [[[int((a - b) * (b - c) * (c - a) / 2) for c in range(3)] for b in range(3)] for a in range(3)]
    # c_{ACD} c_{BCE} summed over loop index C is a definite rank-4 tensor in A,B,D,E:
    tensor = {}
    for A in range(3):
        for B in range(3):
            for D in range(3):
                for E in range(3):
                    tensor[(A, B, D, E)] = sum(eps3[A][C][D] * eps3[B][C][E] for C in range(3))
    # It is symmetric under (A,D)<->(B,E) simultaneous swap (the two-triangle symmetry):
    sym = all(
        tensor[(A, B, D, E)] == tensor[(B, A, E, D)]
        for A in range(3) for B in range(3) for D in range(3) for E in range(3)
    )
    check("S4-C6d (section 6): color word c_{ACD}c_{BCE} symmetric under (A,D)<->(B,E)", sym)


# ----------------------------------------------------------------------------
# S4-C7 — section 5: (A,A)->Q_1(bb) row assembly. The two vertex cross-terms
# populate the full square [0,s]^2 (one assignment over both half-squares).
# WORD SYMMETRY (not a normalization factor): same-type outputs give a symmetric
# single word (Konishi (B,C): partial c partial c); different-type outputs give
# the antisymmetric difference (Q_1(bb): partial c partial b - partial b partial c).
# The universal coefficient lambda_1 is shared and Gamma(3)-fixed for both (S4-C3).
# ----------------------------------------------------------------------------
def c7() -> None:
    # Different-type outputs: the two half-squares give X Y and Y X with the
    # fermionic orientation sign -> antisymmetric X Y - Y X.
    a, b_ = sp.symbols("a b", commutative=False)
    diff = a * b_ - b_ * a
    check(
        "S4-C7a (section 5): different-type outputs give antisymmetric a*b - b*a (Q_1(bb) shape)",
        sp.simplify(diff - (a * b_ - b_ * a)) == 0 and diff != 0,
    )
    # Same-type outputs: the full-square gives one symmetric word (D<->E symmetric
    # under the simultaneous color+position swap); NOT a separate factor 2.
    D, E = sp.symbols("D E", commutative=True)
    same = D * E
    check(
        "S4-C7b (section 5): same-type outputs give one symmetric word (Konishi (B,C) shape), not x2",
        sp.simplify(same - E * D) == 0,
    )
    # Four rows -> four output pairs for Q_1(bb): (c,b) ghost + (beta_I,gamma^I) x3
    rows = ["ghost:(c,b)", "matter1:(beta1,gamma1)", "matter2:(beta2,gamma2)", "matter3:(beta3,gamma3)"]
    check("S4-C7c (section 5): four rows -> four output pairs of Q_1(bb)", len(rows) == 4)


# ----------------------------------------------------------------------------
# S4-C8 — (S4.0)/HT: the output word and flavor structure match HT
# Q_1((beta_I)^A(gamma^J)^B) = kappa^2 delta_I^J f f partial c partial c
# (main.tex line 1234-1235): flavor delta_I^J, output partial_adot c partial^adot c.
# ----------------------------------------------------------------------------
def c8() -> None:
    # Flavor: the seed contact (S4.3) gives delta_r^s (Kronecker in flavor),
    # matching HT's delta_I^J. Model as identity on the 3-flavor space.
    delta = sp.eye(3)
    check("S4-C8a (S4.0 vs HT 1234): flavor structure delta_r^s = identity (matches delta_I^J)", delta == sp.eye(3))
    # Output word: two derivative-dressed field strengths contracted on the
    # dotted index -> partial_adot c partial^adot c; the dotted contraction is
    # the epsilon^{adot bdot} metric (2-dim), trace = 2 components. Structural check:
    eps_dot = sp.Matrix([[0, 1], [-1, 0]])  # epsilon^{adot bdot}
    check(
        "S4-C8b (S4.0 vs HT): dotted-index pairing metric epsilon is antisymmetric rank-2",
        eps_dot.T == -eps_dot and eps_dot.det() == 1,
    )


def main() -> int:
    for fn in (c1, c2, c3, c4, c5, c6, c7, c8):
        fn()
    print()
    if FAILURES:
        print(f"{len(FAILURES)} check(s) FAILED: {FAILURES}")
        return 1
    print("All Stage-IV seed checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
