# STATUS: WIP DRAFT -- graded jet-polynomial engine, Parts 1-2 complete (algebra,
# derivation d_M, Koszul-ordered monomials, Euler-operator extraction); Part 3
# (Lagrangian assembly + unittest bodies for B1/B2/B3/B5) NOT yet written.
# Intended consumer: workflow items W1 of proposals/step5e-konishi-anomaly-pilot-2026-07-16.md
# and the B-suite of proposals/step5c-n4-susy-current-noether-LE-2026-07-16.md §7.
# Not collected by CI (lives in scripts/, defines no tests). Not acceptance evidence.

"""Step 5C -- exact jet-space verification of the off-shell N=1 SUSY Noether
current of N=4 SYM (auxiliary fields kept), Lorentzian and Euclidean.

Memos checked (equation tags cited in each test docstring):
  proposals/step5c-n4-susy-current-noether-LE-2026-07-16.md   (5C.1)-(5C.16)
  proposals/step5d-component-ward-identity-method-2026-07-16.md (5D.4), (5D.D4)
Locked inputs:
  contracts/foundations/step-04c-n4-super-yang-mills.md
    (4C.14)  Lorentzian off-shell Lagrangian (theta-term dropped: frak-k = 0)
    (4C.42a) Euclidean  off-shell Lagrangian (theta-term dropped: frak-k = 0)

Engine: a graded jet-polynomial algebra.  Every field component (su(2) color
A=1..3; flavor r=1..3; explicit spinor components) with a symmetrized
derivative multi-index is an interned symbol; monomials are canonically
ordered tuples of symbols with Koszul sign bookkeeping for the odd ones;
expressions are dicts {monomial: sympy coefficient}.  d_M is a formal even
derivation (d_M eps = 0); the SUSY variation delta (with the anticommuting
parameter eps^a carried inside the algebra) is an even derivation with
delta(d_M X) = d_M(delta X).

Locked conventions (from the repository contracts):
  * eps^{12} = +1, eps_{12} = -1 (same dotted); x^a = eps^{ab} x_b, so
    x^1 = x_2, x^2 = -x_1; contractions xi.chi = xi^a chi_a (NW) and
    xibar.chibar = xibar_adot chibar^adot (SW).
  * sigma_L^mu = (1, s1, s2, s3) with lower indices (a, adot);
    sigmabar_L^mu = (1, -s1, -s2, -s3) with upper (adot, a);
    eta = diag(-1,+1,+1,+1), so sigma_{L mu} = eta_{mu nu} sigma_L^nu.
    sigma_E^m = (-i s1, -i s2, -i s3, 1); sigmabar_E^m = (i s1, i s2, i s3, 1);
    Euclidean metric delta_{mn}.
    sigma_R^{MN} = (1/4)(sigma^M sigmabar^N - sigma^N sigmabar^M), mixed
    indices (a)^b.
  * color: c_{ABC} = LeviCivita(A,B,C), kappa_{AB} = delta_{AB};
    (X x Y)^A = eps_{BCA} X^B Y^C; [[X,Y]]^A = i eps_{BCA} X^B Y^C;
    tr_kappa(XY) = sum_A X^A Y^A.
  * (D_M X)^A = d_M X^A + eps_{BCA} A_M^B X^C            (4.8)
    F_{MN}^A  = d_M A_N^A - d_N A_M^A + eps_{BCA} A_M^B A_N^C.
  * Parameter stripping (5C.1): parameters stand to the RIGHT of all fields;
    in the displayed delta X of (5C.2)/(5C.3) eps stands to the LEFT and is
    moved through with Koszul signs by the engine's canonical ordering.
  * Euler operators: LEFT-derivative convention -- dL/dX is defined by moving
    the occurrence of X to the far left of each monomial with Koszul signs and
    stripping it; E_X := dL/dX - d_M (dL/d(d_M X)).  With this convention the
    computed E's reproduce the displayed (5C.13) forms of E_D, E_{F_r},
    E_{Ft_r} exactly (asserted inside test B4).

DISCREPANCIES FOUND (memo display vs computed-correct identity):
  1. (5C.15) [L] and (5C.16) [E], gaugino-Euler term: the displayed bracket
     multiplying E_lambda^b has the WRONG SIGN on its sigma^{MN} F part
     relative to the computed identity.  Displayed (L):
       - [ (sigma_L^{rho sigma})_b{}^c eps_{ac} F_{rho sigma}
           - i eps_{ab} scrD ] E_lambda^b ,
     computed-correct (L):
       - [ - (sigma_L^{rho sigma})_b{}^c eps_{ac} F_{rho sigma}
           - i eps_{ab} scrD ] E_lambda^b ,
     i.e. the F-part enters with the OPPOSITE sign to the display while the
     scrD-part is as displayed.  Equivalently the bracket is
     -(delta_a lambda_b) with delta_a lambda_b
     = (sigma^{rho sigma})_b{}^c eps_{ca} F_{rho sigma} - i eps_{ba} scrD
     (right strip of (5C.2)): the memo flipped eps_{ca} -> eps_{ac} AND
     eps_{ba} -> eps_{ab} as if both terms acquire the same sign, but only
     the product placement, not both epsilons, reorders.  Same for the
     Euclidean display (5C.16):
       displayed  + [ (sigma_E^{np})_b{}^c eps_{ac} F_{np}
                      + i eps_{ab} scrD ] E_lambda^b ,
       computed   + [ - (sigma_E^{np})_b{}^c eps_{ac} F_{np}
                      + i eps_{ab} scrD ] E_lambda^b .
  2. (5D.4) (minus slot, Euclidean): the same F_{np}-part sign flip as in
     (5C.16) (it is inherited from the slot restriction).  The scrD-part of
     (5D.4) is displayed as + i eps_{b-} scrD, which at b=+ equals
     - i scrD E_lambda^+; the computed-correct scrD-part is
     + i eps_{-b} scrD E_lambda^b = + i scrD E_lambda^+, i.e. (5D.4) ALSO has
     the scrD sub-term sign wrong (eps_{b-} should read eps_{-b}, exactly the
     a=- slot of the correct eps_{ab} of (5C.16)).
  All other terms of (5C.10), (5C.15), (5C.16), (5D.4) verify exactly as
  displayed.  B1 (5C.10) holds exactly as printed in both signatures, so the
  Lagrangians, transformations, Theta and S are mutually consistent and the
  two discrepancies above are pure display errors in the divergence
  identities' gaugino bracket.
"""

from __future__ import annotations

import unittest
from collections import defaultdict
from typing import Dict, Optional, Tuple

import sympy as sp
from sympy import I, Rational

h = sp.Symbol("h")
SQ2 = sp.sqrt(2)

COLORS = (1, 2, 3)
FLAV = (1, 2, 3)
SP2 = (1, 2)  # spinor component values (undotted and dotted)

# Levi-Civita on three values, as a dict.
LEVI: Dict[Tuple[int, int, int], int] = {
    (1, 2, 3): 1, (2, 3, 1): 1, (3, 1, 2): 1,
    (1, 3, 2): -1, (3, 2, 1): -1, (2, 1, 3): -1,
}

# Spinor metric: eps^{12} = +1, eps_{12} = -1 (same for dotted).
EPS_UP = {(1, 2): 1, (2, 1): -1}
EPS_LO = {(1, 2): -1, (2, 1): 1}

# --------------------------------------------------------------------------
# Symbol interning.  Key = (name, index tuple, sorted derivative multi-index).
# --------------------------------------------------------------------------

_SYMS: Dict[tuple, int] = {}
_KEYS: list = []
_ODDS: list = []
ODD_NAMES = frozenset({"lam", "lamt", "psi", "psit", "eps"})


def sid(name: str, idx: tuple, deriv: tuple = ()) -> int:
    key = (name, idx, tuple(sorted(deriv)))
    r = _SYMS.get(key)
    if r is None:
        r = len(_KEYS)
        _SYMS[key] = r
        _KEYS.append(key)
        _ODDS.append(name in ODD_NAMES)
    return r


# Field shortcuts (color index always LAST).
def A_(M, Ac, d=()):
    return sid("A", (M, Ac), d)


def lam_(a, Ac, d=()):
    return sid("lam", (a, Ac), d)


def lamt_(ad, Ac, d=()):
    return sid("lamt", (ad, Ac), d)


def phi_(r, Ac, d=()):
    return sid("phi", (r, Ac), d)


def phit_(r, Ac, d=()):
    return sid("phit", (r, Ac), d)


def psi_(r, a, Ac, d=()):
    return sid("psi", (r, a, Ac), d)


def psit_(r, ad, Ac, d=()):
    return sid("psit", (r, ad, Ac), d)


def sD_(Ac, d=()):
    return sid("sD", (Ac,), d)


def F_(r, Ac, d=()):
    return sid("F", (r, Ac), d)


def Ft_(r, Ac, d=()):
    return sid("Ft", (r, Ac), d)


def eps_(a):
    return sid("eps", (a,))


# --------------------------------------------------------------------------
# Monomials and expressions.
# --------------------------------------------------------------------------

def canon(seq) -> Tuple[int, Optional[tuple]]:
    """Canonicalize a symbol-id sequence: (Koszul sign, sorted tuple)."""
    odds = [s for s in seq if _ODDS[s]]
    sign = 1
    n = len(odds)
    for i in range(n):
        oi = odds[i]
        for j in range(i + 1, n):
            if odds[j] == oi:
                return 0, None
            if oi > odds[j]:
                sign = -sign
    return sign, tuple(sorted(seq))


def addin(d: dict, m: tuple, c) -> None:
    nc = d.get(m, 0) + c
    if nc == 0:
        d.pop(m, None)
    else:
        d[m] = nc


def prod(coeff, *syms) -> dict:
    """Expression consisting of one monomial, factors given in written order."""
    sign, m = canon(syms)
    if sign == 0 or coeff == 0:
        return {}
    return {m: sign * coeff}


def acc(target: dict, expr: dict, coeff=1) -> None:
    if coeff == 0:
        return
    for m, c in expr.items():
        addin(target, m, c * coeff)


def emul(a: dict, b: dict, coeff=1) -> dict:
    """Product a*b (in that written order), Koszul-canonicalized."""
    out: dict = {}
    if coeff == 0:
        return out
    for ma, ca in a.items():
        for mb, cb in b.items():
            sign, m = canon(ma + mb)
            if sign:
                addin(out, m, sign * ca * cb * coeff)
    return out


def esub(a: dict, b: dict) -> dict:
    out = dict(a)
    for m, c in b.items():
        addin(out, m, -c)
    return out


def dM(expr: dict, M) -> dict:
    """Formal total derivative d_M (even derivation; d_M eps = 0)."""
    out: dict = {}
    for m, c in expr.items():
        for i, s in enumerate(m):
            name, idx, der = _KEYS[s]
            if name == "eps":
                continue
            ns = sid(name, idx, der + (M,))
            sign, nm = canon(m[:i] + (ns,) + m[i + 1:])
            if sign:
                addin(out, nm, sign * c)
    return out


def prune(expr: dict) -> dict:
    """Drop coefficients that are exactly zero (after sympy expansion)."""
    out = {}
    for m, c in expr.items():
        cs = sp.expand(c)
        if cs != 0 and sp.simplify(cs) != 0:
            out[m] = cs
    return out


def sectors(expr: dict) -> Dict[tuple, int]:
    """Group monomials by field-content signature (name, #derivatives)."""
    g: Dict[tuple, int] = defaultdict(int)
    for m in expr:
        key = tuple(sorted((_KEYS[s][0], len(_KEYS[s][2])) for s in m))
        g[key] += 1
    return dict(g)


def sector_report(expr: dict, title: str) -> str:
    lines = [title]
    for k, n in sorted(sectors(expr).items()):
        lines.append("  %-70s x%d" % (str(k), n))
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Sigma matrices (2x2 tuples, row = first index - 1, col = second index - 1).
# --------------------------------------------------------------------------

_s1 = ((0, 1), (1, 0))
_s2 = ((0, -I), (I, 0))
_s3 = ((1, 0), (0, -1))
_id2 = ((1, 0), (0, 1))


def _msc(c, X):
    return tuple(tuple(c * X[i][j] for j in range(2)) for i in range(2))


def _mmul(X, Y):
    return tuple(
        tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def _msub(X, Y):
    return tuple(tuple(X[i][j] - Y[i][j] for j in range(2)) for i in range(2))


class Sig:
    """Signature data: index range, metric, sigma / sigmabar / sigma^{MN}."""

    def __init__(self, name, Ms, eta, sig, sigb):
        self.name = name
        self.Ms = Ms
        self.eta = eta            # diagonal metric, dict M -> +-1
        self.sig = sig            # (sigma^M)_{a adot}, M upper
        self.sigb = sigb          # (sigmabar^M)^{adot a}, M upper
        self.smn = {}             # (sigma^{MN})_a{}^b, M,N upper
        for M in Ms:
            for N in Ms:
                self.smn[(M, N)] = _msc(
                    Rational(1, 4),
                    _msub(_mmul(sig[M], sigb[N]), _mmul(sig[N], sigb[M])),
                )


SIG_L = Sig(
    "L",
    (0, 1, 2, 3),
    {0: -1, 1: 1, 2: 1, 3: 1},
    {0: _id2, 1: _s1, 2: _s2, 3: _s3},
    {0: _id2, 1: _msc(-1, _s1), 2: _msc(-1, _s2), 3: _msc(-1, _s3)},
)

SIG_E = Sig(
    "E",
    (1, 2, 3, 4),
    {1: 1, 2: 1, 3: 1, 4: 1},
    {1: _msc(-I, _s1), 2: _msc(-I, _s2), 3: _msc(-I, _s3), 4: _id2},
    {1: _msc(I, _s1), 2: _msc(I, _s2), 3: _msc(I, _s3), 4: _id2},
)

# --------------------------------------------------------------------------
# Covariant derivative and field strength (cached; cached dicts are read-only).
# --------------------------------------------------------------------------

_COVD_CACHE: dict = {}
_FSTR_CACHE: dict = {}


def covd(M, name, idx) -> dict:
    """(D_M X)^A = d_M X^A + eps_{BCA} A_M^B X^C; idx ends with color A."""
    key = (M, name, idx)
    r = _COVD_CACHE.get(key)
    if r is not None:
        return r
    Ac = idx[-1]
    pre = idx[:-1]
    out = dict(prod(1, sid(name, idx, (M,))))
    for B in COLORS:
        for C in COLORS:
            e = LEVI.get((B, C, Ac), 0)
            if e:
                acc(out, prod(e, A_(M, B), sid(name, pre + (C,))))
    _COVD_CACHE[key] = out
    return out


def fstr(M, N, Ac) -> dict:
    """F_{MN}^A = d_M A_N^A - d_N A_M^A + eps_{BCA} A_M^B A_N^C."""
    key = (M, N, Ac)
    r = _FSTR_CACHE.get(key)
    if r is not None:
        return r
    out = dict(prod(1, A_(N, Ac, (M,))))
    acc(out, prod(-1, A_(M, Ac, (N,))))
    for B in COLORS:
        for C in COLORS:
            e = LEVI.get((B, C, Ac), 0)
            if e:
                acc(out, prod(e, A_(M, B), A_(N, C)))
    _FSTR_CACHE[key] = out
    return out


# --------------------------------------------------------------------------
# The off-shell Lagrangians (4C.14) [L] / (4C.42a) [E], frak-k term dropped.
# --------------------------------------------------------------------------

def build_lagrangian(S: Sig, lor: bool) -> dict:
    L: dict = {}
    # gauge kinetic: L: -(1/4) F_{mu nu} F^{mu nu};  E: +(1/4) F_mn F_mn
    cF = -Rational(1, 4) if lor else Rational(1, 4)
    for Ac in COLORS:
        for M in S.Ms:
            for N in S.Ms:
                w = h * cF * S.eta[M] * S.eta[N]
                acc(L, emul(fstr(M, N, Ac), fstr(M, N, Ac)), w)
    # gaugino kinetic: L: + i h lamt_ad (sigmabar^M)^{ad a} (D_M lam_a);
    #                  E: +   h lamt sigmabar_E D lam
    cg = I * h if lor else h
    for Ac in COLORS:
        for ad in SP2:
            for a in SP2:
                for M in S.Ms:
                    c = S.sigb[M][ad - 1][a - 1]
                    if c:
                        acc(L, emul(prod(1, lamt_(ad, Ac)),
                                    covd(M, "lam", (a, Ac))), cg * c)
    # auxiliary scrD: L: +h/2 D D ; E: -h/2 D D
    cD = Rational(1, 2) * h * (1 if lor else -1)
    for Ac in COLORS:
        acc(L, prod(cD, sD_(Ac), sD_(Ac)))
    # scalar kinetic: L: - h (D_M phit)(D^M phi); E: + h (D_m phit)(D_m phi)
    cs = -h if lor else h
    for Ac in COLORS:
        for r in FLAV:
            for M in S.Ms:
                acc(L, emul(covd(M, "phit", (r, Ac)),
                            covd(M, "phi", (r, Ac))), cs * S.eta[M])
    # matter fermion kinetic: L: + i h psit sigmabar D psi; E: + h ...
    cm = I * h if lor else h
    for Ac in COLORS:
        for r in FLAV:
            for ad in SP2:
                for a in SP2:
                    for M in S.Ms:
                        c = S.sigb[M][ad - 1][a - 1]
                        if c:
                            acc(L, emul(prod(1, psit_(r, ad, Ac)),
                                        covd(M, "psi", (r, a, Ac))), cm * c)
    # auxiliary F: L: + h Ft F; E: - h Ft F
    ca = h if lor else -h
    for Ac in COLORS:
        for r in FLAV:
            acc(L, prod(ca, Ft_(r, Ac), F_(r, Ac)))
    # moment map: L: + i h scrD (phi x phit); E: - i h scrD (phi x phit)
    cmm = I * h if lor else -I * h
    for Ac in COLORS:
        for r in FLAV:
            for B in COLORS:
                for C in COLORS:
                    e = LEVI.get((B, C, Ac), 0)
                    if e:
                        acc(L, prod(cmm * e, sD_(Ac), phi_(r, B), phit_(r, C)))
    # Yukawas: L: + sqrt2 h c_ABC (phit_r psi_r lam + phi_r psit_r lamt);
    #          E: - sqrt2 h (...)
    cy = SQ2 * h if lor else -SQ2 * h
    for (Ac, B, C), e in LEVI.items():
        for r in FLAV:
            # phit_r^A (psi_r^{B a} lam^C_a), psi^{Ba} = eps^{ab} psi_{rb}
            for a in SP2:
                for b in SP2:
                    eu = EPS_UP.get((a, b), 0)
                    if eu:
                        acc(L, prod(cy * e * eu, phit_(r, Ac),
                                    psi_(r, b, B), lam_(a, C)))
            # phi_r^A (psit_{r ad}^B lamt^{C ad}), lamt^{ad} = eps^{ad bd} lamt_bd
            for ad in SP2:
                for bd in SP2:
                    eu = EPS_UP.get((ad, bd), 0)
                    if eu:
                        acc(L, prod(cy * e * eu, phi_(r, Ac),
                                    psit_(r, ad, B), lamt_(bd, C)))
    # superpotential F-terms:
    # L: -(sqrt2 h/2) eps_rst c_ABC (F_r phi_s phi_t + Ft_r phit_s phit_t);
    # E: +(sqrt2 h/2)(...)
    cw = (-SQ2 * h / 2) if lor else (SQ2 * h / 2)
    for (Ac, B, C), e2 in LEVI.items():
        for (r, s, t), e1 in LEVI.items():
            acc(L, prod(cw * e1 * e2, F_(r, Ac), phi_(s, B), phi_(t, C)))
            acc(L, prod(cw * e1 * e2, Ft_(r, Ac), phit_(s, B), phit_(t, C)))
    # matter Yukawa (psi psi):
    # L: +(h/sqrt2) eps_rst c_ABC (phi_t psi_r psi_s + phit_t psit_r psit_s);
    # E: -(h/sqrt2)(...)
    cp = (h / SQ2) if lor else (-h / SQ2)
    for (Ac, B, C), e2 in LEVI.items():
        for (r, s, t), e1 in LEVI.items():
            # phi_t^A psi_r^{Ba} psi^C_{sa}, psi^{Ba} = eps^{ab} psi_{rb}
            for a in SP2:
                for b in SP2:
                    eu = EPS_UP.get((a, b), 0)
                    if eu:
                        acc(L, prod(cp * e1 * e2 * eu, phi_(t, Ac),
                                    psi_(r, b, B), psi_(s, a, C)))
            # phit_t^A psit_{r ad}^B psit_s^{C ad}
            for ad in SP2:
                for bd in SP2:
                    eu = EPS_UP.get((ad, bd), 0)
                    if eu:
                        acc(L, prod(cp * e1 * e2 * eu, phit_(t, Ac),
                                    psit_(r, ad, B), psit_(s, bd, C)))
    return L


# --------------------------------------------------------------------------
# eps-slot transformations (5C.2) [L] / (5C.3) [E]; epsbar/epstilde = 0.
# --------------------------------------------------------------------------

def build_delta_table(S: Sig, lor: bool) -> dict:
    """basekey (name, idx) -> delta expression (eps carried inside)."""
    T: dict = {}
    for Ac in COLORS:
        # delta A_M = L: -i eps sigma_{LM} lamt ; E: + eps sigma_EM lamt
        for M in S.Ms:
            ex: dict = {}
            for a in SP2:
                for bd in SP2:
                    for cd in SP2:
                        w = S.sig[M][a - 1][bd - 1] * EPS_UP.get((bd, cd), 0)
                        if w:
                            c = (-I * S.eta[M] * w) if lor else w
                            acc(ex, prod(c, eps_(a), lamt_(cd, Ac)))
            T[("A", (M, Ac))] = ex
        # delta lam_a = L: +(sigma^{rho sig})_a{}^b eps_b F_{rho sig} - i eps_a D
        #               E: -(sigma_E^{np})_a{}^b eps_b F_{np}          - i eps_a D
        for a in SP2:
            ex = {}
            for Mp in S.Ms:
                for Np in S.Ms:
                    for b in SP2:
                        for c in SP2:
                            w = S.smn[(Mp, Np)][a - 1][b - 1] * \
                                EPS_LO.get((b, c), 0)
                            if w:
                                w = w if lor else -w
                                acc(ex, emul(prod(1, eps_(c)),
                                             fstr(Mp, Np, Ac)), w)
            for b in SP2:
                w = EPS_LO.get((a, b), 0)
                if w:
                    acc(ex, prod(-I * w, eps_(b), sD_(Ac)))
            T[("lam", (a, Ac))] = ex
        T[("lamt", (1, Ac))] = {}
        T[("lamt", (2, Ac))] = {}
        # delta scrD = L: - eps sigma^M (D_M lamt) ; E: - i eps sigma_E^M D lamt
        ex = {}
        for a in SP2:
            for bd in SP2:
                for cd in SP2:
                    for M in S.Ms:
                        w = S.sig[M][a - 1][bd - 1] * EPS_UP.get((bd, cd), 0)
                        if w:
                            c = -w if lor else -I * w
                            acc(ex, emul(prod(1, eps_(a)),
                                         covd(M, "lamt", (cd, Ac))), c)
        T[("sD", (Ac,))] = ex
        for r in FLAV:
            # delta phi_r = - sqrt2 eps^a psi_{ra}   (both signatures)
            ex = {}
            for a in SP2:
                acc(ex, prod(-SQ2, eps_(a), psi_(r, a, Ac)))
            T[("phi", (r, Ac))] = ex
            T[("phit", (r, Ac))] = {}
            # delta psi_{ra} = - sqrt2 eps_a F_r     (eps-slot, both)
            for a in SP2:
                ex = {}
                for b in SP2:
                    w = EPS_LO.get((a, b), 0)
                    if w:
                        acc(ex, prod(-SQ2 * w, eps_(b), F_(r, Ac)))
                T[("psi", (r, a, Ac))] = ex
            # delta psit_{r ad} = L: - i sqrt2 eps^b (sigma^M)_{b ad} D_M phit_r
            #                     E: +   sqrt2 eps^b (sigma_E^M)_{b ad} D_M phit_r
            for ad in SP2:
                ex = {}
                for b in SP2:
                    for M in S.Ms:
                        w = S.sig[M][b - 1][ad - 1]
                        if w:
                            c = (-I * SQ2 * w) if lor else (SQ2 * w)
                            acc(ex, emul(prod(1, eps_(b)),
                                         covd(M, "phit", (r, Ac))), c)
                T[("psit", (r, ad, Ac))] = ex
            T[("F", (r, Ac))] = {}
            # delta Ft_r = L: + i sqrt2 eps sigma^M D_M psit_r + 2 (eps lam x phit_r)
            #              E: -   sqrt2 eps sigma_E^M D_M psit_r + 2 (eps lam x phit_r)
            ex = {}
            for b in SP2:
                for bd in SP2:
                    for cd in SP2:
                        for M in S.Ms:
                            w = S.sig[M][b - 1][bd - 1] * EPS_UP.get((bd, cd), 0)
                            if w:
                                c = (I * SQ2 * w) if lor else (-SQ2 * w)
                                acc(ex, emul(prod(1, eps_(b)),
                                             covd(M, "psit", (r, cd, Ac))), c)
            for B in COLORS:
                for C in COLORS:
                    e = LEVI.get((B, C, Ac), 0)
                    if e:
                        for b in SP2:
                            acc(ex, prod(2 * e, eps_(b), lam_(b, B),
                                         phit_(r, C)))
            T[("Ft", (r, Ac))] = ex
    return T


def make_delta(T: dict):
    """Even derivation delta from a base table; delta(d_M X) = d_M(delta X)."""
    cache: dict = {}

    def delta_sym(s: int) -> dict:
        r = cache.get(s)
        if r is not None:
            return r
        name, idx, der = _KEYS[s]
        base = T.get((name, idx))
        if base is None:
            res: dict = {}
        else:
            res = base
            for M in der:
                res = dM(res, M)
        cache[s] = res
        return res

    def delta(expr: dict) -> dict:
        out: dict = {}
        for m, c in expr.items():
            for i, s in enumerate(m):
                ds = delta_sym(s)
                if not ds:
                    continue
                pre, post = m[:i], m[i + 1:]
                for dm_, dc in ds.items():
                    sign, nm = canon(pre + dm_ + post)
                    if sign:
                        addin(out, nm, sign * c * dc)
        return out

    return delta


# --------------------------------------------------------------------------
# Symplectic potentials Theta (5C.6), with delta inserted (eps-slot).
# --------------------------------------------------------------------------

def build_theta(S: Sig, lor: bool, T: dict) -> dict:
    """dict M -> Theta^M(delta_eps)."""
    th = {}
    for M in S.Ms:
        ex: dict = {}
        for Ac in COLORS:
            # L: - F^{MN} dA_N ; E: + F^{MN} dA_N
            for N in S.Ms:
                dA = T[("A", (N, Ac))]
                if dA:
                    w = (-S.eta[M] * S.eta[N]) if lor else 1
                    acc(ex, emul(fstr(M, N, Ac), dA), h * w)
            # L: + i lamt sigmabar^M dlam ; E: + lamt sigmabar_E^M dlam
            for ad in SP2:
                for b in SP2:
                    c = S.sigb[M][ad - 1][b - 1]
                    if c:
                        dl = T[("lam", (b, Ac))]
                        if dl:
                            acc(ex, emul(prod(1, lamt_(ad, Ac)), dl),
                                (I * h if lor else h) * c)
            for r in FLAV:
                # L: -(D^M phit_r) dphi_r ; E: +(D_M phit_r) dphi_r
                dphi = T[("phi", (r, Ac))]
                if dphi:
                    w = (-S.eta[M]) if lor else 1
                    acc(ex, emul(covd(M, "phit", (r, Ac)), dphi), h * w)
                # (D phi) dphit vanishes in the eps slot (delta phit = 0)
                # L: + i psit sigmabar^M dpsi ; E: + psit sigmabar_E^M dpsi
                for ad in SP2:
                    for b in SP2:
                        c = S.sigb[M][ad - 1][b - 1]
                        if c:
                            dp = T[("psi", (r, b, Ac))]
                            if dp:
                                acc(ex, emul(prod(1, psit_(r, ad, Ac)), dp),
                                    (I * h if lor else h) * c)
        th[M] = ex
    return th


# --------------------------------------------------------------------------
# The auxiliary-free current primitives S^M_a (5C.9), eps-slot.
# --------------------------------------------------------------------------

def build_S(S: Sig, lor: bool) -> dict:
    """dict (M, a) -> S^M_a."""
    out = {}
    for M in S.Ms:
        for a in SP2:
            ex: dict = {}
            for Ac in COLORS:
                # L: -i F_{rho sig} (sigma^{rho sig} sigma^M lamt)_a
                # E: +  F_{np}      (sigma_E^{np} sigma_E^M lamt)_a
                for Mp in S.Ms:
                    for Np in S.Ms:
                        for b in SP2:
                            for cd in SP2:
                                for dd in SP2:
                                    w = (S.smn[(Mp, Np)][a - 1][b - 1]
                                         * S.sig[M][b - 1][cd - 1]
                                         * EPS_UP.get((cd, dd), 0))
                                    if w:
                                        w = (-I * w) if lor else w
                                        acc(ex, emul(fstr(Mp, Np, Ac),
                                                     prod(1, lamt_(dd, Ac))),
                                            h * w)
                # - sqrt2 (D_N phit_r)(sigma^N sigmabar^M psi_r)_a  (both)
                for r in FLAV:
                    for N in S.Ms:
                        for bd in SP2:
                            for b in SP2:
                                w = (S.sig[N][a - 1][bd - 1]
                                     * S.sigb[M][bd - 1][b - 1])
                                if w:
                                    acc(ex, emul(covd(N, "phit", (r, Ac)),
                                                 prod(1, psi_(r, b, Ac))),
                                        -SQ2 * h * w)
                # L: - i (phi_s x phit_s)(sigma^M lamt)_a ; E: - (...)
                for s in FLAV:
                    for B in COLORS:
                        for C in COLORS:
                            e = LEVI.get((B, C, Ac), 0)
                            if e:
                                for bd in SP2:
                                    for cd in SP2:
                                        w = (S.sig[M][a - 1][bd - 1]
                                             * EPS_UP.get((bd, cd), 0))
                                        if w:
                                            w = (-I * w) if lor else -w
                                            acc(ex, prod(h * w * e,
                                                         phi_(s, B),
                                                         phit_(s, C),
                                                         lamt_(cd, Ac)))
                # L: - i eps_rst (phit_s x phit_t)(sigma^M psit_r)_a ; E: -(...)
                for (r, s, t), e1 in LEVI.items():
                    for B in COLORS:
                        for C in COLORS:
                            e2 = LEVI.get((B, C, Ac), 0)
                            if e2:
                                for bd in SP2:
                                    for cd in SP2:
                                        w = (S.sig[M][a - 1][bd - 1]
                                             * EPS_UP.get((bd, cd), 0))
                                        if w:
                                            w = (-I * w) if lor else -w
                                            acc(ex, prod(h * w * e1 * e2,
                                                         phit_(s, B),
                                                         phit_(t, C),
                                                         psit_(r, cd, Ac)))
            out[(M, a)] = ex
    return out


# --------------------------------------------------------------------------
# Euler operators by jet variation (left-derivative convention).
# --------------------------------------------------------------------------

def euler(Lexpr: dict, name: str, idx: tuple, Ms) -> dict:
    """E_X = dL/dX - d_M (dL/d(d_M X)), left derivative (X moved to the far
    left with Koszul signs before stripping)."""
    p0: dict = {}
    pM: Dict[object, dict] = {M: {} for M in Ms}
    for m, c in Lexpr.items():
        for i, s in enumerate(m):
            nm_, idx_, der = _KEYS[s]
            if nm_ != name or idx_ != idx:
                continue
            sgn = 1
            if _ODDS[s]:
                for t in m[:i]:
                    if _ODDS[t]:
                        sgn = -sgn
            rest = m[:i] + m[i + 1:]
            if der == ():
                addin(p0, rest, sgn * c)
            elif len(der) == 1:
                addin(pM[der[0]], rest, sgn * c)
            else:  # pragma: no cover - the Lagrangians are first order
                raise AssertionError("second derivative in L")
    out = p0
    for M in Ms:
        if pM[M]:
            out = esub(out, dM(pM[M], M))
    return out


# === PART 3 (identity assembly + tests) ===
