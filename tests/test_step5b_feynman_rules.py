"""Step 5B -- exact symbolic verification of the superspace Feynman-rule identities.

Everything is verified over an exact Grassmann exterior algebra with sympy
scalar coefficients; no numerics.  The memo equations checked by each test are
cited in its docstring ("Checks (5B.n), ...").

Locked conventions (from the repository contracts, contracts/foundations):

  * eps^{12} = eps^{1.2.} = +1, eps_{12} = eps_{1.2.} = -1;
    psi^a = eps^{ab} psi_b, psi_a = eps_{ab} psi^b (same for dotted), so
    x^1 = x_2 and x^2 = -x_1.
  * sigma_L^mu = (1, sigma^i)_{a b.}; (bar-sigma_L^mu)^{a.a} = (1, -sigma^i);
    eta = diag(-1,+1,+1,+1).
    sigma_E^m = (-i sigma^1, -i sigma^2, -i sigma^3, 1)_{a a.};
    (bar-sigma_E^m)^{a.a} = (+i sigma^1, +i sigma^2, +i sigma^3, 1).
    sigma^{mu nu} = (1/4)[sigma^mu bar-sigma^nu - sigma^nu bar-sigma^mu],
    bar-sigma^{mu nu} = (1/4)[bar-sigma^mu sigma^nu - bar-sigma^nu sigma^mu].
  * Grassmann generators per superspace point, canonical exterior order
    t1 < t2 < b1 < b2 for (theta^1, theta^2, thetabar_{1.}, thetabar_{2.});
    the barred coordinate carries a LOWER dotted index as the fundamental
    variable; thetabar^{a.} := eps^{a.b.} thetabar_{b.}.
  * Left derivatives: {d_a, theta^b} = delta_a^b;
    {dbar^{a.}, thetabar_{b.}} = delta^{a.}_{b.};
    dbar_{a.} := eps_{a.b.} dbar^{b.}  (hence {dbar_{a.}, thetabar^{b.}} = -delta).
  * Momentum representation with plane wave e^{i p.x}: d_mu -> i p_mu.
      D_a^L      = d_a     - i (sigma_L^mu)_{a b.} thetabar^{b.} (i p_mu)
      Dbar_{a.}^L = dbar_{a.} + i theta^b (sigma_L^mu)_{b a.} (i p_mu)
      D_a^E      = d_a     + (sigma_E^m)_{a b.} thetabar^{b.} (i p_m)
      Dbar_{a.}^E = dbar_{a.} - theta^b (sigma_E^m)_{b a.} (i p_m)
  * D^2 := D^a D_a = eps^{ab} D_b D_a; Dbar^2 := Dbar_{a.} Dbar^{a.}
    = eps^{a.b.} Dbar_{a.} Dbar_{b.};
    theta^2 = -2 theta^1 theta^2, thetabar^2 = +2 thetabar_{1.} thetabar_{2.}.
  * [X]_F := -(1/4) D^2 X|;  [Y]_D := (1/16) D^2 Dbar^2 Y| (Dbar^2 acts FIRST).
    Box -> -p^2 with p_L^2 := eta^{mu nu} p_mu p_nu, p_E^2 := sum_m p_m^2.
  * Berezin measure fixed by [theta^2 thetabar^2]_D = 1:
    theta^2 thetabar^2 = -4 t1 t2 b1 b2, hence
      int d^4theta (t1 t2 b1 b2) = -1/4.
    For int d^4theta_2 the point-2 block (4 generators, an EVEN block) is
    extracted with Koszul sign +1 -- moving a block of four generators past
    anything costs (-1)^{4k} = +1; the residual global sign convention is
    validated by the reproducing property in T9.

DISCREPANCIES FOUND: none.  Every identity below holds exactly as stated in
the memo with the locked conventions.
"""

from __future__ import annotations

import unittest
from typing import Callable, Dict, Optional, Tuple

import sympy as sp
from sympy import I, Rational

Key = Tuple[int, ...]


# --------------------------------------------------------------------------
# Grassmann exterior-algebra engine over sympy scalar coefficients.
# --------------------------------------------------------------------------

def _merge_sign(ka: Key, kb: Key) -> Tuple[int, Optional[Key]]:
    """Merge two strictly increasing generator tuples.

    Returns (koszul_sign, merged_tuple), or (0, None) if a generator repeats
    (in which case the exterior product vanishes).
    """
    if not ka:
        return 1, kb
    if not kb:
        return 1, ka
    i = j = 0
    sign = 1
    la, lb = len(ka), len(kb)
    out = []
    while i < la and j < lb:
        a, b = ka[i], kb[j]
        if a == b:
            return 0, None
        if a < b:
            out.append(a)
            i += 1
        else:
            # kb[j] jumps over the remaining la - i generators of ka
            out.append(b)
            j += 1
            if (la - i) & 1:
                sign = -sign
    out.extend(ka[i:])
    out.extend(kb[j:])
    return sign, tuple(out)


class G:
    """Element of the exterior algebra: dict {ordered generator tuple: coeff}."""

    __slots__ = ("d",)

    def __init__(self, d: Optional[Dict[Key, object]] = None):
        self.d: Dict[Key, object] = {}
        if d:
            for k, v in d.items():
                if v == 0:
                    continue
                self.d[tuple(k)] = v

    def __add__(self, other: "G") -> "G":
        out = dict(self.d)
        for k, v in other.d.items():
            out[k] = out.get(k, sp.Integer(0)) + v
        return G(out)

    def __sub__(self, other: "G") -> "G":
        return self + (-1) * other

    def __neg__(self) -> "G":
        return (-1) * self

    def __rmul__(self, scalar) -> "G":
        return G({k: scalar * v for k, v in self.d.items()})

    def __mul__(self, other):
        if isinstance(other, G):
            out: Dict[Key, object] = {}
            for ka, va in self.d.items():
                for kb, vb in other.d.items():
                    sgn, km = _merge_sign(ka, kb)
                    if sgn:
                        out[km] = out.get(km, sp.Integer(0)) + sgn * va * vb
            return G(out)
        return G({k: v * other for k, v in self.d.items()})

    def coeff(self, key) -> object:
        return self.d.get(tuple(key), sp.Integer(0))

    def body(self) -> object:
        return self.d.get((), sp.Integer(0))

    def is_zero(self) -> bool:
        return all(sp.expand(v) == 0 for v in self.d.values())


def gen(i: int) -> G:
    return G({(i,): sp.Integer(1)})


def geq(x: G, y: G) -> bool:
    return (x - y).is_zero()


def deriv(x: G, g: int) -> G:
    """Left derivative with respect to generator g: {deriv_g, gen(g)*} = 1."""
    out: Dict[Key, object] = {}
    for k, v in x.d.items():
        if g in k:
            pos = k.index(g)
            nk = k[:pos] + k[pos + 1:]
            out[nk] = out.get(nk, sp.Integer(0)) + (v if pos % 2 == 0 else -v)
    return G(out)


# --------------------------------------------------------------------------
# Locked spinor / sigma-matrix data.
# --------------------------------------------------------------------------

S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -I], [I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
ID2 = sp.eye(2)
SIGMAS = {1: S1, 2: S2, 3: S3}

# (sigma^mu)_{a b.} indexed [mu][a-1, b.-1]; (bar-sigma^mu)^{a. a} indexed
# [mu][a.-1, a-1].  Euclidean list position m-1 holds sigma_E^m, m = 1..4.
SIG = {"L": [ID2, S1, S2, S3], "E": [-I * S1, -I * S2, -I * S3, ID2]}
SIGBAR = {"L": [ID2, -S1, -S2, -S3], "E": [I * S1, I * S2, I * S3, ID2]}
ETA = sp.diag(-1, 1, 1, 1)

EPS_UP = {(1, 2): sp.Integer(1), (2, 1): sp.Integer(-1)}   # eps^{12} = +1
EPS_LO = {(1, 2): sp.Integer(-1), (2, 1): sp.Integer(1)}   # eps_{12} = -1


def smunu(sig: str, mu: int, nu: int) -> sp.Matrix:
    """(sigma^{mu nu})_a{}^b = (1/4)[sigma^mu bar-sigma^nu - (mu <-> nu)]."""
    return (SIG[sig][mu] * SIGBAR[sig][nu] - SIG[sig][nu] * SIGBAR[sig][mu]) / 4


def sbmunu(sig: str, mu: int, nu: int) -> sp.Matrix:
    """(bar-sigma^{mu nu})^{a.}{}_{b.} = (1/4)[bar-sigma^mu sigma^nu - (mu <-> nu)]."""
    return (SIGBAR[sig][mu] * SIG[sig][nu] - SIGBAR[sig][nu] * SIG[sig][mu]) / 4


# --------------------------------------------------------------------------
# One superspace point: generators, covariant derivatives, projections.
# --------------------------------------------------------------------------

class Point:
    """A superspace point: 4 Grassmann generators at `offset`, plus a momentum.

    Generator indices: offset+0 = theta^1, offset+1 = theta^2,
    offset+2 = thetabar_{1.}, offset+3 = thetabar_{2.} (canonical order
    t1 < t2 < b1 < b2).  `p` are the 4 momentum components: for sig "L" the
    LOWER components (p_0, p_1, p_2, p_3); for sig "E" (p_1, ..., p_4).
    """

    def __init__(self, offset: int, sig: str, p):
        self.o = offset
        self.sig = sig
        self.p = list(p)

    # generator indices
    def t(self, a: int) -> int:
        return self.o + a - 1

    def b(self, ad: int) -> int:
        return self.o + 2 + ad - 1

    # coordinate elements
    def theta_up(self, a: int) -> G:
        return gen(self.t(a))

    def thetabar_lo(self, ad: int) -> G:
        return gen(self.b(ad))

    def thetabar_up(self, ad: int) -> G:
        out = G()
        for bd in (1, 2):
            e = EPS_UP.get((ad, bd))
            if e is not None:
                out = out + e * gen(self.b(bd))
        return out

    @property
    def B(self):
        """Box -> -p^2 in this signature."""
        p = self.p
        if self.sig == "L":
            return -(-p[0] ** 2 + p[1] ** 2 + p[2] ** 2 + p[3] ** 2)
        return -(p[0] ** 2 + p[1] ** 2 + p[2] ** 2 + p[3] ** 2)

    # covariant derivatives (momentum representation, literal locked formulas)
    def D(self, a: int) -> Callable[[G], G]:
        def op(x: G) -> G:
            res = deriv(x, self.t(a))
            for bd in (1, 2):
                c = sp.Integer(0)
                for mu in range(4):
                    if self.sig == "L":
                        # D_a^L = d_a - i (sigma_L^mu)_{a b.} thetabar^{b.} (i p_mu)
                        c += -I * SIG["L"][mu][a - 1, bd - 1] * (I * self.p[mu])
                    else:
                        # D_a^E = d_a + (sigma_E^m)_{a b.} thetabar^{b.} (i p_m)
                        c += SIG["E"][mu][a - 1, bd - 1] * (I * self.p[mu])
                if c != 0:
                    res = res + c * (self.thetabar_up(bd) * x)
            return res
        return op

    def Dbar(self, ad: int) -> Callable[[G], G]:
        def op(x: G) -> G:
            # dbar_{a.} = eps_{a.b.} dbar^{b.}, dbar^{b.} = d/d thetabar_{b.}
            res = G()
            for bd in (1, 2):
                e = EPS_LO.get((ad, bd))
                if e is not None:
                    res = res + e * deriv(x, self.b(bd))
            for b_ in (1, 2):
                c = sp.Integer(0)
                for mu in range(4):
                    if self.sig == "L":
                        # Dbar_{a.}^L = dbar_{a.} + i theta^b (sigma_L^mu)_{b a.} (i p_mu)
                        c += I * SIG["L"][mu][b_ - 1, ad - 1] * (I * self.p[mu])
                    else:
                        # Dbar_{a.}^E = dbar_{a.} - theta^b (sigma_E^m)_{b a.} (i p_m)
                        c += -SIG["E"][mu][b_ - 1, ad - 1] * (I * self.p[mu])
                if c != 0:
                    res = res + c * (self.theta_up(b_) * x)
            return res
        return op

    def Dup(self, a: int) -> Callable[[G], G]:
        """D^a := eps^{ab} D_b."""
        def op(x: G) -> G:
            out = G()
            for b_ in (1, 2):
                e = EPS_UP.get((a, b_))
                if e is not None:
                    out = out + e * self.D(b_)(x)
            return out
        return op

    def D2(self, x: G) -> G:
        """D^2 = D^a D_a = eps^{ab} D_b D_a."""
        out = G()
        for (a, b_), e in EPS_UP.items():
            out = out + e * self.D(b_)(self.D(a)(x))
        return out

    def Dbar2(self, x: G) -> G:
        """Dbar^2 = Dbar_{a.} Dbar^{a.} = eps^{a.b.} Dbar_{a.} Dbar_{b.}."""
        out = G()
        for (ad, bd), e in EPS_UP.items():
            out = out + e * self.Dbar(ad)(self.Dbar(bd)(x))
        return out


# --------------------------------------------------------------------------
# Spinor squares, delta function, projections, Berezin measure.
# --------------------------------------------------------------------------

def spinor_sq_up(psi: Dict[int, G]) -> G:
    """psi^2 := psi^a psi_a = eps_{ab} psi^a psi^b for an upper-index spinor."""
    out = G()
    for (a, b_), e in EPS_LO.items():
        out = out + e * (psi[a] * psi[b_])
    return out


def spinor_sq_lo(psib: Dict[int, G]) -> G:
    """psibar^2 := psibar_{a.} psibar^{a.} = eps^{a.b.} psibar_{a.} psibar_{b.}."""
    out = G()
    for (ad, bd), e in EPS_UP.items():
        out = out + e * (psib[ad] * psib[bd])
    return out


def theta2(P: Point) -> G:
    return spinor_sq_up({a: P.theta_up(a) for a in (1, 2)})


def thetabar2(P: Point) -> G:
    return spinor_sq_lo({ad: P.thetabar_lo(ad) for ad in (1, 2)})


def delta4(Pi: Point, Pj: Point) -> G:
    """delta^4(theta_ij) := (theta_i - theta_j)^2 (thetabar_i - thetabar_j)^2."""
    dth = {a: Pi.theta_up(a) - Pj.theta_up(a) for a in (1, 2)}
    dbr = {ad: Pi.thetabar_lo(ad) - Pj.thetabar_lo(ad) for ad in (1, 2)}
    return spinor_sq_up(dth) * spinor_sq_lo(dbr)


def F_proj(P: Point, x: G):
    """[X]_F := -(1/4) D^2 X|_{theta = thetabar = 0}."""
    return Rational(-1, 4) * P.D2(x).body()


def D_proj(P: Point, x: G):
    """[Y]_D := (1/16) D^2 Dbar^2 Y| (Dbar^2 acts first)."""
    return Rational(1, 16) * P.D2(P.Dbar2(x)).body()


def berezin(x: G, P: Point) -> G:
    """int d^4theta_P: extract the point-P top block with weight -1/4.

    Normalization from [theta^2 thetabar^2]_D = 1:
    theta^2 thetabar^2 = -4 t1 t2 b1 b2 => int d^4theta (t1 t2 b1 b2) = -1/4.
    The point block is 4 generators (even), so factoring it out of any
    canonically ordered monomial carries Koszul sign +1 (validated by T9).
    """
    blk = {P.t(1), P.t(2), P.b(1), P.b(2)}
    out: Dict[Key, object] = {}
    for k, v in x.d.items():
        if blk <= set(k):
            nk = tuple(g for g in k if g not in blk)
            out[nk] = out.get(nk, sp.Integer(0)) + Rational(-1, 4) * v
    return G(out)


def generic_superfield(P: Point, prefix: str) -> G:
    """Generic superfield: 16 arbitrary sympy symbols on the 16 basis monomials."""
    gens4 = (P.t(1), P.t(2), P.b(1), P.b(2))
    d: Dict[Key, object] = {}
    for mask in range(16):
        key = tuple(g for i, g in enumerate(gens4) if mask >> i & 1)
        d[key] = sp.Symbol(f"{prefix}{mask}")
    return G(d)


def momenta(sig: str, base: str = "p"):
    if sig == "L":
        return list(sp.symbols(f"{base}0:4", real=True))
    return list(sp.symbols(f"{base}1:5", real=True))


SIGS = ("L", "E")


# --------------------------------------------------------------------------
# Tests.
# --------------------------------------------------------------------------

class Step5BFeynmanRulesTest(unittest.TestCase):
    def assertGZero(self, x: G, msg: str = "") -> None:
        bad = {k: sp.expand(v) for k, v in x.d.items() if sp.expand(v) != 0}
        self.assertEqual(bad, {}, msg)

    def assertGEqual(self, x: G, y: G, msg: str = "") -> None:
        self.assertGZero(x - y, msg)

    # -- T0 ---------------------------------------------------------------

    def test_T0_engine_selftests(self):
        """Checks (5B.7) prerequisites: the Grassmann-derivative conventions
        {d_a, theta^b} = delta_a^b, {dbar^{a.}, thetabar_{b.}} = delta^{a.}_{b.},
        {dbar_{a.}, thetabar^{b.}} = -delta_{a.}^{b.}, plus engine associativity
        and Koszul signs of the exterior product."""
        P = Point(0, "L", momenta("L"))
        X = generic_superfield(P, "x")

        # {d_a, theta^b .} = delta_a^b as operators
        for a in (1, 2):
            for b_ in (1, 2):
                thb = P.theta_up(b_)
                anti = deriv(thb * X, P.t(a)) + thb * deriv(X, P.t(a))
                expected = (sp.Integer(1) if a == b_ else sp.Integer(0)) * X
                self.assertGEqual(anti, expected, f"{{d_{a}, theta^{b_}}}")

        # {dbar^{a.}, thetabar_{b.} .} = delta^{a.}_{b.}
        for ad in (1, 2):
            for bd in (1, 2):
                tbl = P.thetabar_lo(bd)
                anti = deriv(tbl * X, P.b(ad)) + tbl * deriv(X, P.b(ad))
                expected = (sp.Integer(1) if ad == bd else sp.Integer(0)) * X
                self.assertGEqual(anti, expected, f"{{dbar^{ad}, thetabar_{bd}}}")

        # {dbar_{a.}, thetabar^{b.} .} = -delta_{a.}^{b.}  (the locked minus sign)
        def dbar_lo(ad, y):
            out = G()
            for cd in (1, 2):
                e = EPS_LO.get((ad, cd))
                if e is not None:
                    out = out + e * deriv(y, P.b(cd))
            return out

        for ad in (1, 2):
            for bd in (1, 2):
                tbu = P.thetabar_up(bd)
                anti = dbar_lo(ad, tbu * X) + tbu * dbar_lo(ad, X)
                expected = (sp.Integer(-1) if ad == bd else sp.Integer(0)) * X
                self.assertGEqual(anti, expected, f"{{dbar_{ad}, thetabar^{bd}}}")

        # theta^2 = -2 theta^1 theta^2 and thetabar^2 = 2 thetabar_1. thetabar_2.
        self.assertGEqual(theta2(P), G({(P.t(1), P.t(2)): sp.Integer(-2)}))
        self.assertGEqual(thetabar2(P), G({(P.b(1), P.b(2)): sp.Integer(2)}))

        # Koszul signs: g_i g_j = -g_j g_i, g_i^2 = 0, and a reorder example
        for i in range(4):
            self.assertGZero(gen(i) * gen(i))
            for j in range(4):
                if i != j:
                    self.assertGZero(gen(i) * gen(j) + gen(j) * gen(i))
        # (t2 b1)(t1 b2): the permutation (1,2,0,3) has 2 inversions -> +t1t2b1b2
        lhs = (gen(1) * gen(2)) * (gen(0) * gen(3))
        self.assertGEqual(lhs, G({(0, 1, 2, 3): sp.Integer(1)}))

        # associativity on elements with symbolic coefficients
        c = sp.symbols("c0:6")
        A = G({(0,): c[0], (1, 2): c[1], (): c[2]})
        Bm = G({(3,): c[3], (0, 2): c[4]})
        Cm = G({(1,): c[5], (2, 3): sp.Integer(2), (): sp.Integer(1)})
        self.assertGEqual((A * Bm) * Cm, A * (Bm * Cm))

    # -- T1 ---------------------------------------------------------------

    def test_T1_clifford_algebra(self):
        """Checks (5B.4), (1.12), (1.13), (1.54): sigma_L^mu bar-sigma_L^nu +
        sigma_L^nu bar-sigma_L^mu = -2 eta^{mu nu}, its bar-sigma sigma version,
        and the Euclidean Clifford algebra with +2 delta^{mn}."""
        for mu in range(4):
            for nu in range(4):
                lhs = SIG["L"][mu] * SIGBAR["L"][nu] + SIG["L"][nu] * SIGBAR["L"][mu]
                self.assertEqual(sp.expand(lhs + 2 * ETA[mu, nu] * ID2),
                                 sp.zeros(2, 2), f"L sigma sbar mu={mu} nu={nu}")
                lhs = SIGBAR["L"][mu] * SIG["L"][nu] + SIGBAR["L"][nu] * SIG["L"][mu]
                self.assertEqual(sp.expand(lhs + 2 * ETA[mu, nu] * ID2),
                                 sp.zeros(2, 2), f"L sbar sigma mu={mu} nu={nu}")
                delta = sp.Integer(1) if mu == nu else sp.Integer(0)
                lhs = SIG["E"][mu] * SIGBAR["E"][nu] + SIG["E"][nu] * SIGBAR["E"][mu]
                self.assertEqual(sp.expand(lhs - 2 * delta * ID2),
                                 sp.zeros(2, 2), f"E sigma sbar m={mu+1} n={nu+1}")
                lhs = SIGBAR["E"][mu] * SIG["E"][nu] + SIGBAR["E"][nu] * SIG["E"][mu]
                self.assertEqual(sp.expand(lhs - 2 * delta * ID2),
                                 sp.zeros(2, 2), f"E sbar sigma m={mu+1} n={nu+1}")

    # -- T2 ---------------------------------------------------------------

    def test_T2_sigma_munu_components(self):
        """Checks (5B.5), (1.16), (1.57): sigma_L^{0i} = -sigma^i/2,
        bar-sigma_L^{0i} = +sigma^i/2, sigma_L^{ij} = bar-sigma_L^{ij}
        = -(i/2) eps^{ijk} sigma^k; sigma_E^{ij} = +(i/2) eps^{ijk} sigma^k,
        sigma_E^{4i} = (i/2) sigma^i, bar-sigma_E^{4i} = -(i/2) sigma^i."""
        for i in (1, 2, 3):
            self.assertEqual(sp.expand(smunu("L", 0, i) + SIGMAS[i] / 2),
                             sp.zeros(2, 2), f"sigma_L^0{i}")
            self.assertEqual(sp.expand(sbmunu("L", 0, i) - SIGMAS[i] / 2),
                             sp.zeros(2, 2), f"bar-sigma_L^0{i}")
            self.assertEqual(sp.expand(smunu("E", 3, i - 1) - I * SIGMAS[i] / 2),
                             sp.zeros(2, 2), f"sigma_E^4{i}")
            self.assertEqual(sp.expand(sbmunu("E", 3, i - 1) + I * SIGMAS[i] / 2),
                             sp.zeros(2, 2), f"bar-sigma_E^4{i}")
            for j in (1, 2, 3):
                epsk = sum((sp.LeviCivita(i, j, k) * SIGMAS[k] for k in (1, 2, 3)),
                           start=sp.zeros(2, 2))
                self.assertEqual(sp.expand(smunu("L", i, j) + I * epsk / 2),
                                 sp.zeros(2, 2), f"sigma_L^{i}{j}")
                self.assertEqual(sp.expand(sbmunu("L", i, j) + I * epsk / 2),
                                 sp.zeros(2, 2), f"bar-sigma_L^{i}{j}")
                self.assertEqual(sp.expand(smunu("E", i - 1, j - 1) - I * epsk / 2),
                                 sp.zeros(2, 2), f"sigma_E^{i}{j}")

    # -- T3 ---------------------------------------------------------------

    def test_T3_covariant_derivative_anticommutators(self):
        """Checks (5B.7), (2A.29), (2A.42): {D_a^L, Dbar_{b.}^L}
        = 2i (sigma_L^mu)_{a b.} (i p_mu), {D, D} = {Dbar, Dbar} = 0, and
        {D_a^E, Dbar_{b.}^E} = -2 (sigma_E^m)_{a b.} (i p_m), as operators on
        the full 16-dimensional Grassmann module with symbolic momentum."""
        for sig in SIGS:
            P = Point(0, sig, momenta(sig))
            X = generic_superfield(P, "x")
            for a in (1, 2):
                for bd in (1, 2):
                    anti = P.D(a)(P.Dbar(bd)(X)) + P.Dbar(bd)(P.D(a)(X))
                    c = sp.Integer(0)
                    for mu in range(4):
                        if sig == "L":
                            c += 2 * I * SIG["L"][mu][a - 1, bd - 1] * (I * P.p[mu])
                        else:
                            c += -2 * SIG["E"][mu][a - 1, bd - 1] * (I * P.p[mu])
                    self.assertGEqual(anti, c * X, f"{sig} {{D_{a}, Dbar_{bd}}}")
            for a in (1, 2):
                for b_ in (1, 2):
                    self.assertGZero(P.D(a)(P.D(b_)(X)) + P.D(b_)(P.D(a)(X)),
                                     f"{sig} {{D_{a}, D_{b_}}}")
                    self.assertGZero(P.Dbar(a)(P.Dbar(b_)(X)) + P.Dbar(b_)(P.Dbar(a)(X)),
                                     f"{sig} {{Dbar_{a}, Dbar_{b_}}}")

    # -- T4 ---------------------------------------------------------------

    def test_T4_squares_and_D_term_normalization(self):
        """Checks (5B.8), (3A.12), (3B.4): the scalar (theta-independent) part
        of D^2 theta^2 is -4 and of Dbar^2 thetabar^2 is -4 at arbitrary
        symbolic momentum, and [theta^2 thetabar^2]_D = 1."""
        for sig in SIGS:
            P = Point(0, sig, momenta(sig))
            self.assertEqual(sp.expand(P.D2(theta2(P)).body() + 4), 0,
                             f"{sig} D^2 theta^2 body")
            self.assertEqual(sp.expand(P.Dbar2(thetabar2(P)).body() + 4), 0,
                             f"{sig} Dbar^2 thetabar^2 body")
            self.assertEqual(sp.expand(D_proj(P, theta2(P) * thetabar2(P)) - 1), 0,
                             f"{sig} [theta^2 thetabar^2]_D")

    # -- T5 ---------------------------------------------------------------

    def test_T5_D_algebra_workhorse_identities(self):
        """Checks (5B.9): Dbar^2 D^2 Dbar^2 = 16 Box Dbar^2,
        D^2 Dbar^2 D^2 = 16 Box D^2, and -D^a Dbar^2 D_a
        = 8 Box - (1/2){D^2, Dbar^2}, as operator identities on the full
        module with Box -> -p^2, in both signatures."""
        for sig in SIGS:
            P = Point(0, sig, momenta(sig))
            X = generic_superfield(P, "x")
            B = P.B
            self.assertGEqual(P.Dbar2(P.D2(P.Dbar2(X))), 16 * B * P.Dbar2(X),
                              f"{sig} Dbar2 D2 Dbar2")
            self.assertGEqual(P.D2(P.Dbar2(P.D2(X))), 16 * B * P.D2(X),
                              f"{sig} D2 Dbar2 D2")
            lhs = G()
            for a in (1, 2):
                lhs = lhs + P.Dup(a)(P.Dbar2(P.D(a)(X)))
            lhs = -lhs
            rhs = 8 * B * X - Rational(1, 2) * (P.D2(P.Dbar2(X)) + P.Dbar2(P.D2(X)))
            self.assertGEqual(lhs, rhs, f"{sig} -D^a Dbar2 D_a")

    # -- T6 ---------------------------------------------------------------

    def test_T6_projector_algebra(self):
        """Checks (5B.10), (5A.66): P_+ = Dbar^2 D^2/(16 Box),
        P_- = D^2 Dbar^2/(16 Box), P_T = -D^a Dbar^2 D_a/(8 Box) with
        Box -> -p^2 satisfy P_i P_j = delta_ij P_i and P_T + P_+ + P_- = 1 as
        operators, in both signatures.  Division by p^2 is avoided by
        verifying the Box-scaled polynomial forms (e.g. A_+ A_+ = 16 Box A_+
        with A_+ := Dbar^2 D^2, which is P_+^2 = P_+ times (16 Box)^2)."""
        for sig in SIGS:
            P = Point(0, sig, momenta(sig))
            X = generic_superfield(P, "x")
            B = P.B

            def Ap(y: G) -> G:
                return P.Dbar2(P.D2(y))

            def Am(y: G) -> G:
                return P.D2(P.Dbar2(y))

            def At(y: G) -> G:
                out = G()
                for a in (1, 2):
                    out = out + P.Dup(a)(P.Dbar2(P.D(a)(y)))
                return -out

            # idempotence (scaled): A_i A_i = (norm_i) B A_i
            self.assertGEqual(Ap(Ap(X)), 16 * B * Ap(X), f"{sig} P+ P+")
            self.assertGEqual(Am(Am(X)), 16 * B * Am(X), f"{sig} P- P-")
            self.assertGEqual(At(At(X)), 8 * B * At(X), f"{sig} PT PT")
            # orthogonality: A_i A_j = 0 for i != j
            self.assertGZero(Ap(Am(X)), f"{sig} P+ P-")
            self.assertGZero(Am(Ap(X)), f"{sig} P- P+")
            self.assertGZero(Ap(At(X)), f"{sig} P+ PT")
            self.assertGZero(At(Ap(X)), f"{sig} PT P+")
            self.assertGZero(Am(At(X)), f"{sig} P- PT")
            self.assertGZero(At(Am(X)), f"{sig} PT P-")
            # completeness: A_+/(16B) + A_-/(16B) + A_T/(8B) = 1
            self.assertGEqual(Ap(X) + Am(X) + 2 * At(X), 16 * B * X,
                              f"{sig} completeness")

    # -- T7 ---------------------------------------------------------------

    def test_T7_vector_kernel_inversion(self):
        """Checks (5B.14), (5A.68), (5A.69): K_E^V = (h/2) Box_E against
        G_E = 2 g^2 Box_E^{-1} and K_L^V = -(h/2) Box_L against
        G_L = -2 g^2 Box_L^{-1} give the identity once h g^2 = 1."""
        h, g_, BoxE, BoxL = sp.symbols("h g BoxE BoxL")
        KE = (h / 2) * BoxE
        GE = 2 * g_ ** 2 / BoxE
        self.assertEqual(sp.simplify((KE * GE).subs(h, 1 / g_ ** 2) - 1), 0)
        KL = -(h / 2) * BoxL
        GL = -2 * g_ ** 2 / BoxL
        self.assertEqual(sp.simplify((KL * GL).subs(h, 1 / g_ ** 2) - 1), 0)

    # -- T8 ---------------------------------------------------------------

    def test_T8_chiral_kernel_inversion(self):
        """Checks (5B.16), (5A.72), (5A.73): with one_plus(i,j)
        := (Dbar_i^2 D_i^2/(16 Box)) delta^4(theta_ij) and Box -> -p^2, the
        convolution int d^4theta_2 one_plus(1,2) one_plus(2,3)
        = one_plus(1,3); equivalently, the kernel K = -h one_plus inverts the
        propagator G = -g^2 one_plus on the constrained (chiral-projected)
        space once h g^2 = 1.  Verified in Box-scaled polynomial form
        (A := Dbar^2 D^2 delta^4; int A A = 16 Box A) in both signatures."""
        for sig in SIGS:
            p = momenta(sig)
            P1 = Point(0, sig, p)
            P2 = Point(4, sig, p)
            P3 = Point(8, sig, p)
            A12 = P1.Dbar2(P1.D2(delta4(P1, P2)))
            A23 = P2.Dbar2(P2.D2(delta4(P2, P3)))
            A13 = P1.Dbar2(P1.D2(delta4(P1, P3)))
            conv = berezin(A12 * A23, P2)
            self.assertGEqual(conv, 16 * P1.B * A13, f"{sig} one_plus convolution")
        # prefactor bookkeeping: K G = (-h)(-g^2) (one_plus o one_plus)
        # = h g^2 one_plus -> one_plus once h g^2 = 1.
        h, g_ = sp.symbols("h g")
        self.assertEqual(sp.simplify(((-h) * (-g_ ** 2)).subs(h, 1 / g_ ** 2) - 1), 0)

    # -- T9 ---------------------------------------------------------------

    def test_T9_delta4_reproducing_property(self):
        """Checks (5B.18): delta^4(theta_12) := (theta_1 - theta_2)^2
        (thetabar_1 - thetabar_2)^2 satisfies
        int d^4theta_2 delta^4(theta_12) X(theta_2) = X(theta_1) for a generic
        superfield X with 16 arbitrary coefficients (this fixes the Berezin
        measure sign: int d^4theta (t1 t2 b1 b2) = -1/4)."""
        p = momenta("L")
        P1 = Point(0, "L", p)
        P2 = Point(4, "L", p)
        X2 = generic_superfield(P2, "x")
        res = berezin(delta4(P1, P2) * X2, P2)
        X1 = G({tuple(g - 4 for g in k): v for k, v in X2.d.items()})
        self.assertGEqual(res, X1)

    # -- T10 --------------------------------------------------------------

    def test_T10_loop_saturation(self):
        """Checks (5B.19): delta^4(theta_12) [D_1^2 Dbar_1^2 delta^4(theta_12)]
        = 16 delta^4(theta_12) and delta^4 [Dbar_1^2 D_1^2 delta^4]
        = 16 delta^4 (momentum-dependent terms cancel exactly), while
        delta^4 delta^4 = delta^4 [D_1^2 delta^4] = delta^4 [Dbar_1^2 delta^4]
        = delta^4 [D_1^a Dbar_1^2 delta^4] = 0 componentwise.
        Both signatures."""
        for sig in SIGS:
            p = momenta(sig)
            P1 = Point(0, sig, p)
            P2 = Point(4, sig, p)
            d12 = delta4(P1, P2)
            self.assertGEqual(d12 * P1.D2(P1.Dbar2(d12)), 16 * d12,
                              f"{sig} delta D2 Dbar2 delta")
            self.assertGEqual(d12 * P1.Dbar2(P1.D2(d12)), 16 * d12,
                              f"{sig} delta Dbar2 D2 delta")
            self.assertGZero(d12 * d12, f"{sig} delta delta")
            self.assertGZero(d12 * P1.D2(d12), f"{sig} delta D2 delta")
            self.assertGZero(d12 * P1.Dbar2(d12), f"{sig} delta Dbar2 delta")
            for a in (1, 2):
                self.assertGZero(d12 * P1.Dup(a)(P1.Dbar2(d12)),
                                 f"{sig} delta D^{a} Dbar2 delta")

    # -- T11 --------------------------------------------------------------

    def test_T11_vector_component_normalization(self):
        """Checks (5B.15), (5A.71): with V_E = -2i (theta sigma_E^m thetabar) A_m
        and Box_E V_E represented by -2i (theta sigma_E^m thetabar) B_m,
        [V_E (Box_E V_E)]_D = -2 delta^{mn} A_m B_n; Lorentzian analogue with
        V_L = -2 (theta sigma_L^mu thetabar) A_mu gives
        [V_L (Box_L V_L)]_D = -2 eta^{mu nu} A_mu B_nu."""
        def bilinear(P: Point, sig: str, mu: int) -> G:
            # theta sigma^mu thetabar := theta^a (sigma^mu)_{a b.} thetabar^{b.}
            out = G()
            for a in (1, 2):
                for bd in (1, 2):
                    c = SIG[sig][mu][a - 1, bd - 1]
                    if c != 0:
                        out = out + c * (P.theta_up(a) * P.thetabar_up(bd))
            return out

        Avec = sp.symbols("A0:4")
        Bvec = sp.symbols("Bb0:4")

        PE = Point(0, "E", momenta("E"))
        VE = G()
        VBE = G()
        for m in range(4):
            VE = VE + (-2 * I) * Avec[m] * bilinear(PE, "E", m)
            VBE = VBE + (-2 * I) * Bvec[m] * bilinear(PE, "E", m)
        got = D_proj(PE, VE * VBE)
        want = -2 * sum(Avec[m] * Bvec[m] for m in range(4))
        self.assertEqual(sp.expand(got - want), 0, "E: [V Box V]_D")

        PL = Point(0, "L", momenta("L"))
        VL = G()
        VBL = G()
        for mu in range(4):
            VL = VL + (-2) * Avec[mu] * bilinear(PL, "L", mu)
            VBL = VBL + (-2) * Bvec[mu] * bilinear(PL, "L", mu)
        got = D_proj(PL, VL * VBL)
        want = -2 * sum(ETA[mu, nu] * Avec[mu] * Bvec[nu]
                        for mu in range(4) for nu in range(4))
        self.assertEqual(sp.expand(got - want), 0, "L: [V Box V]_D")

    # -- T12 --------------------------------------------------------------

    def test_T12_ghost_measure_F_D_conversion(self):
        """Checks (5B.20): the F <-> D conversion lemma behind the chiral
        ghost measure: for U := Dbar^2(q) W (exactly chiral, Dbar^3 = 0) and
        generic W, Z, with the outer projections taken at the product momentum
        s = q + r, [U Z]_D = [U (-(1/4) Dbar^2(r) Z)]_F, in both signatures."""
        for sig in SIGS:
            q = momenta(sig, "q")
            r = momenta(sig, "r")
            s = [qi + ri for qi, ri in zip(q, r)]
            Pq = Point(0, sig, q)
            Pr = Point(0, sig, r)
            Ps = Point(0, sig, s)
            W = generic_superfield(Pq, "w")
            Z = generic_superfield(Pr, "z")
            U = Pq.Dbar2(W)
            # chirality of U at momentum q
            for ad in (1, 2):
                self.assertGZero(Pq.Dbar(ad)(U), f"{sig} Dbar_{ad} U")
            lhs = D_proj(Ps, U * Z)
            rhs = F_proj(Ps, U * (Rational(-1, 4) * Pr.Dbar2(Z)))
            self.assertEqual(sp.expand(lhs - rhs), 0, f"{sig} F<->D conversion")

    # -- T13 --------------------------------------------------------------

    def test_T13_topological_term_total_derivative(self):
        """Checks (5B.13): the quadratic-in-V part of the topological density
        is a total derivative -- eps_L^{mu nu rho sigma} p_mu p_rho
        A_nu(p) A_sigma(-p) = 0 by antisymmetry of eps in mu <-> rho."""
        p = momenta("L")
        Avec = sp.symbols("A0:4")
        Bvec = sp.symbols("At0:4")  # A(-p)
        total = sum(sp.LeviCivita(mu, nu, rho, si)
                    * p[mu] * p[rho] * Avec[nu] * Bvec[si]
                    for mu in range(4) for nu in range(4)
                    for rho in range(4) for si in range(4))
        self.assertEqual(sp.expand(total), 0)


if __name__ == "__main__":
    unittest.main()
