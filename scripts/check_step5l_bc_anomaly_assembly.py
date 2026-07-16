#!/usr/bin/env python3
"""Step-5L mechanical assembly of the (b,c)-channel one-loop anomaly coefficient.

Derives, with NO hand-fed signs, every bookkeeping factor of the mu^2-branch of the
two boxes B_par/B_cross for  Q_-(psi_{r+}^A phitilde_s^B) -> lambdatilde lambdatilde
(Euclidean N=4 SYM, DRED), plus the tree contact and the T-a/1-branch cancellation
certificate.  Inputs used (all project records, cited in the 5L memo):

  * epsilon values (1.3)-(1.5):  eps_{12}=-1, eps^{12}=+1  (same for dotted);
  * sigma_E^m = (-i sigma^i, 1), sbar_E^m = (+i sigma^i, 1)  (1.51)-(1.52);
  * frame (5D.D4):  + := 1, - := 2   (python: PLUS=0, MINUS=1);
  * Euclidean action (4C.42a): weight e^{-S/hbar};
      S  >  h[ psit sbar.D psi ]  (fermion kinetic, no i),
      S  > -sqrt2 h c_ABC phi^A psit^B_ad eps^{ad bd} lamt^C_bd   (V2 Yukawa),
      S  >  h (D phit)(D phi)     (scalar kinetic);
  * insertion (5D.4)/(5C.16) at a=-, with Euler operators by LEFT derivative
      (odd Euler coefficients to the right of the varied field, (5C.13));
  * DRED axiom (5G.5):  Sum_{m=1..4} l_m l_m  =  l_d^2 + mu^2  on a collapse line;
  * masters (5G.6):  int mu^2 l_d^2 / D^4 = 1/32pi^2 + O(eps);  int mu^2/D^4 = O(eps);
  * rotational average:  l_m l_n -> delta_mn l_d^2 / d.

Everything else (propagator constants incl. their phases, SD collapse constants
chi_L/chi_R, Koszul pairing signs, momentum routing, epsilon chains, color words,
operator matching combinatorics) is DERIVED below by explicit Berezin integration
and explicit index summation.  Gauge group su(2): c_ABC = eps_ABC, kappa = delta
(rank-independence of the derivation is argued in the memo; this certifies the
su(2) instance exactly).

Run:  python3 scripts/check_step5l_bc_anomaly_assembly.py
"""

import itertools
from fractions import Fraction
from sympy import I, Rational, sqrt, symbols, simplify, expand, S, Symbol, nsimplify

# ----------------------------------------------------------------------------
# Section 0: exact tensors and kinematic identities
# ----------------------------------------------------------------------------
PLUS, MINUS = 0, 1          # frame (5D.D4): + := index value 1, - := index value 2

eps_lo = [[0, -1], [1, 0]]  # eps_{ab}:  eps_{12} = -1  (1.3)-(1.5)
eps_up = [[0, 1], [-1, 0]]  # eps^{ab}:  eps^{12} = +1
# dotted epsilons carry the same numeric values.

pauli = [
    [[0, 1], [1, 0]],
    [[0, -I], [I, 0]],
    [[1, 0], [0, -1]],
]
ID2 = [[1, 0], [0, 1]]

# (1.51)-(1.52): sigma_E^m = (-i sigma^i, 1);  sbar_E^m = (+i sigma^i, 1)
sig = [[[(-I) * pauli[m][a][b] for b in range(2)] for a in range(2)] for m in range(3)]
sig.append([[S(ID2[a][b]) for b in range(2)] for a in range(2)])
sbar = [[[(I) * pauli[m][a][b] for b in range(2)] for a in range(2)] for m in range(3)]
sbar.append([[S(ID2[a][b]) for b in range(2)] for a in range(2)])
# index structure: sig[m][a][ad] = (sigma^m)_{a ad};  sbar[m][ad][a] = (sbar^m)^{ad a}

l1, l2, l3, l4 = symbols('l1 l2 l3 l4')
LV = [l1, l2, l3, l4]

# A1: (sigma.k)(sbar.k) = k^2 * Id   and   (sbar.k)(sigma.k) = k^2 * Id
for a in range(2):
    for b in range(2):
        s1v = expand(sum(sig[m][a][ad] * LV[m] * sbar[n][ad][b] * LV[n]
                         for m in range(4) for n in range(4) for ad in range(2)))
        s2v = expand(sum(sbar[m][a][ad] * LV[m] * sig[n][ad][b] * LV[n]
                         for m in range(4) for n in range(4) for ad in range(2)))
        tgt = expand((l1**2 + l2**2 + l3**2 + l4**2) * (1 if a == b else 0))
        assert s1v == tgt and s2v == tgt, "A1 Clifford check failed"

# A2: Euclidean Fierz  sum_m (sigma^m)_{a ad}(sigma^m)_{b bd} = 2 eps_{ab} eps_{ad bd}
for a in range(2):
    for b in range(2):
        for ad in range(2):
            for bd in range(2):
                lhs = sum(sig[m][a][ad] * sig[m][b][bd] for m in range(4))
                rhs = 2 * eps_lo[a][b] * eps_lo[ad][bd]
                assert simplify(lhs - rhs) == 0, "A2 Fierz check failed"

# A3: the averaged spinor kernel used in the boxes:
#   T_ave[X][Y] := sum_m sig[m][MINUS][X] * sig[m][PLUS][Y]  = 2 eps_{-+} eps_{XY}
T_ave = [[sum(sig[m][MINUS][X] * sig[m][PLUS][Y] for m in range(4))
          for Y in range(2)] for X in range(2)]
for X in range(2):
    for Y in range(2):
        assert simplify(T_ave[X][Y] - 2 * eps_lo[MINUS][PLUS] * eps_lo[X][Y]) == 0
assert eps_lo[MINUS][PLUS] == 1   # eps_{-+} = eps_{21} = +1

print("Section 0: Clifford, Fierz, averaged-kernel identities  ... OK")

# ----------------------------------------------------------------------------
# Section 1: Grassmann polynomial mini-engine (exact, ordered generators)
# ----------------------------------------------------------------------------
class GP:
    """Grassmann polynomial: dict {ordered-id-tuple: sympy coeff}. Ids are ints;
    monomials stored sorted ascending with sign absorbed into the coefficient."""

    def __init__(self, d=None):
        self.d = dict(d) if d else {}

    @staticmethod
    def scalar(c):
        return GP({(): S(c)})

    @staticmethod
    def gen(i, c=1):
        return GP({(i,): S(c)})

    def add(self, o):
        r = dict(self.d)
        for k, v in o.d.items():
            r[k] = r.get(k, S(0)) + v
            if r[k] == 0:
                del r[k]
        return GP(r)

    def scale(self, c):
        return GP({k: v * c for k, v in self.d.items()})

    def mul(self, o):
        r = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                if set(k1) & set(k2):
                    continue
                merged = list(k1) + list(k2)
                # merge sign: count inversions between the two sorted blocks
                sign = 1
                for x in k1:
                    for y in k2:
                        if x > y:
                            sign = -sign
                key = tuple(sorted(merged))
                c = sign * v1 * v2
                r[key] = r.get(key, S(0)) + c
                if r[key] == 0:
                    del r[key]
        return GP(r)

    def dleft(self, g):
        """left derivative d_L/d theta_g"""
        r = {}
        for k, v in self.d.items():
            if g in k:
                pos = k.index(g)
                key = tuple(x for x in k if x != g)
                r[key] = r.get(key, S(0)) + ((-1) ** pos) * v
        return GP(r)

    def top(self, ids):
        return self.d.get(tuple(sorted(ids)), S(0))


def gp_exp(x, nmax):
    r = GP.scalar(1)
    t = GP.scalar(1)
    for k in range(1, nmax + 1):
        t = t.mul(x).scale(Rational(1, k))
        r = r.add(t)
    return r

# ----------------------------------------------------------------------------
# Section 2: Berezin toy -- propagator constants and SD collapse constants
# ----------------------------------------------------------------------------
hbar, g = symbols('hbar g', positive=True)
h = 1 / g**2

# modes: u+_b = psi_b(+p), u-_b = psi_b(-p), v+_ad = psit_ad(+p), v-_ad = psit_ad(-p)
UP = [0, 1]; UM = [2, 3]; VP = [4, 5]; VM = [6, 7]
ALL = list(range(8))
pnum = [S(1), S(2), S(3), S(5)]   # generic Euclidean momentum
p2 = sum(x**2 for x in pnum)
sbp = [[sum(sbar[m][ad][b] * pnum[m] for m in range(4)) for b in range(2)]
       for ad in range(2)]        # (sbar.p)^{ad b}
sgp = [[sum(sig[m][a][ad] * pnum[m] for m in range(4)) for ad in range(2)]
       for a in range(2)]         # (sigma.p)_{a ad}

# S2 = h * psit sbar.d psi  ->  modes:  i h [ v-(sbar.p)u+  +  v+(sbar.(-p))u- ]
Stoy = GP()
for ad in range(2):
    for b in range(2):
        Stoy = Stoy.add(GP.gen(VM[ad]).mul(GP.gen(UP[b])).scale(I * h * sbp[ad][b]))
        Stoy = Stoy.add(GP.gen(VP[ad]).mul(GP.gen(UM[b])).scale(I * h * (-sbp[ad][b])))

W = gp_exp(Stoy.scale(-1 / hbar), 4)
Z = W.top(ALL)
assert simplify(Z) != 0


def vev(x):
    return simplify(x.mul(W).top(ALL) / Z)

# propagator <psi_b(p) psit_ad(-p)>  =: c_psi * hbar g^2 (sigma.p)_{b ad} / p^2
c_psi = None
for b in range(2):
    for ad in range(2):
        val = vev(GP.gen(UP[b]).mul(GP.gen(VM[ad])))
        ref = hbar * g**2 * sgp[b][ad] / p2
        if c_psi is None and ref != 0:
            c_psi = simplify(val / ref)
for b in range(2):
    for ad in range(2):
        val = vev(GP.gen(UP[b]).mul(GP.gen(VM[ad])))
        assert simplify(val - c_psi * hbar * g**2 * sgp[b][ad] / p2) == 0
        # reversed order = minus
        val2 = vev(GP.gen(VM[ad]).mul(GP.gen(UP[b])))
        assert simplify(val2 + val) == 0
        # minus-momentum sector: <psi_b(-p) psit_ad(+p)> = c_psi hbar g^2 (sigma.(-p))/p^2
        val3 = vev(GP.gen(UM[b]).mul(GP.gen(VP[ad])))
        assert simplify(val3 + c_psi * hbar * g**2 * sgp[b][ad] / p2) == 0
assert c_psi in (I, -I), f"c_psi = {c_psi}"

# SD collapse constants.
# chi_R:  <E_psit^ad(+p) psit_bd(-p)> = chi_R hbar delta^ad_bd,
#         E_psit^ad(+p) = i h (sbar.p)^{ad b} psi_b(+p)   [= d_L Stoy / d v-_ad]
chi_R = None
for ad in range(2):
    for bd in range(2):
        E = GP()
        for b in range(2):
            E = E.add(GP.gen(UP[b], I * h * sbp[ad][b]))
        # check E == d_L S / d v-_ad  (left-derivative convention of (5C.13))
        dS = Stoy.dleft(VM[ad])
        diff = E.add(dS.scale(-1))
        assert all(simplify(v) == 0 for v in diff.d.values())
        val = vev(E.mul(GP.gen(VM[bd])))
        if ad == bd:
            if chi_R is None:
                chi_R = simplify(val / hbar)
            assert simplify(val - chi_R * hbar) == 0
        else:
            assert simplify(val) == 0
assert chi_R in (1, -1), f"chi_R = {chi_R}"
assert simplify(chi_R - I * c_psi) == 0   # collapse reality: chi = i c_psi

# chi_L:  <E_psi^a(+p) psi_b(-p)> = chi_L hbar delta^a_b,
#         E_psi^a(+p) = i h (sbar.p)^{bd a} psit_bd(+p)
chi_L = None
for a in range(2):
    for b in range(2):
        E = GP()
        for bd in range(2):
            E = E.add(GP.gen(VP[bd], I * h * sbp[bd][a]))
        val = vev(E.mul(GP.gen(UM[b])))
        if a == b:
            if chi_L is None:
                chi_L = simplify(val / hbar)
            assert simplify(val - chi_L * hbar) == 0
        else:
            assert simplify(val) == 0
assert chi_L in (1, -1) and chi_L == chi_R
chi = chi_R

# collapse lemma with symbolic momentum (the DRED mu^2 split):
#   i h (sbar.l)^{ad b} * P[psi_b psit_bd](l)  =  chi hbar (Sum l^2 / L2) delta^ad_bd
L2, MU2, dd = symbols('L2 MU2 d_dim', positive=True)
for ad in range(2):
    for bd in range(2):
        val = expand(sum(I * h * sbar[n][ad][b] * LV[n]
                         * c_psi * hbar * g**2
                         * sum(sig[m][b][bd] * LV[m] for m in range(4)) / L2
                         for n in range(4) for b in range(2)))
        tgt = expand(chi * hbar * (l1**2 + l2**2 + l3**2 + l4**2) / L2
                     * (1 if ad == bd else 0))
        assert simplify(val - tgt) == 0
# on the collapse line the DRED axiom (5G.5) reads  Sum l^2 -> L2 + MU2, i.e.
#   blob = chi hbar (1 + MU2/L2) delta   -- '1'-branch and mu^2-branch.

print(f"Section 2: Berezin toy: c_psi = {c_psi}, chi_L = chi_R = {chi}  ... OK")

# ----------------------------------------------------------------------------
# Section 3: Wick pairing signs
# ----------------------------------------------------------------------------
def pairing_sign(n_odd, pairs):
    """Sign to rearrange an ordered sequence of n_odd Grassmann objects into
    (contracted pairs, in given order)(remaining objects, original order).
    Standard nested rule: process pairs sorted by first index; each pair (i,j)
    contributes (-1)^{# not-yet-consumed odd elements strictly between i and j}."""
    consumed = set()
    sign = 1
    for (i, j) in sorted(pairs):
        between = [k for k in range(i + 1, j) if k not in consumed]
        sign *= (-1) ** len(between)
        consumed.add(i); consumed.add(j)
    return sign

# ----------------------------------------------------------------------------
# Section 4: the two boxes -- mu^2 branch assembly
# ----------------------------------------------------------------------------
# gauge group su(2): c_ABC = eps_ABC; kappa = delta
NC = 3
def eps3(i, j, k):
    if len({i, j, k}) < 3:
        return 0
    perm = [(0,1,2),(1,2,0),(2,0,1)]
    return 1 if (i,j,k) in perm else -1
cAB = [[[eps3(A, B, C) for C in range(NC)] for B in range(NC)] for A in range(NC)]

NF = 3   # flavor su(3) index r,s,t = 1..3

# Odd-field canonical sequence for the boxes (construction order of the correlator):
#   [ psi_x ] [ psi_y ] [ psit_w1, LAM1 ] [ psit_w2, LAM2 ]
# positions:    0         1        2   3       4    5
LAM1, LAM2 = 100, 101   # Grassmann source ids (LAM1 < LAM2 canonical)

# pairing patterns (fermion lines) + scalar contractions; connectivity hand-checked
# in the 5K census and re-verified here by explicit node bookkeeping:
#   B_par  : (psi_x,psit_w1),(psi_y,psit_w2); scalars (phit_x,phi_w2),(phit_y,phi_w1)
#   B_cross: (psi_x,psit_w2),(psi_y,psit_w1); scalars (phit_x,phi_w1),(phit_y,phi_w2)
patterns = {
    'B_par':   {'psi_pairs': [(0, 2), (1, 4)], 'phit_x_to': 'w2', 'phit_y_to': 'w1'},
    'B_cross': {'psi_pairs': [(0, 4), (1, 2)], 'phit_x_to': 'w1', 'phit_y_to': 'w2'},
}

# momentum routing at zero external momenta: solve for line orientations.
# lines: F1 = psi_x line (collapse line), F2 = psi_y line, S1 = phit_x line,
#        S2 = phit_y line.  k(line) = o * l, with o = +1 meaning "incoming at the
#        FIRST field's node" = +l.  Node set {x, y, w1, w2}; conservation checked
#        with incoming(+k at first-field node, -k at second-field node).
def route(pattern):
    pat = patterns[pattern]
    # first fields: psi_x at x; psi_y at y; phit_x at x; phit_y at y
    lines = {
        'F1': ('x', 'w1' if pat['psi_pairs'][0][1] == 2 else 'w2'),
        'F2': ('y', 'w2' if pat['psi_pairs'][1][1] == 4 else 'w1'),
        'S1': ('x', pat['phit_x_to']),
        'S2': ('y', pat['phit_y_to']),
    }
    sols = []
    for os_ in itertools.product((1, -1), repeat=4):
        o = dict(zip(('F1', 'F2', 'S1', 'S2'), os_))
        if o['F1'] != 1:
            continue  # fix overall loop orientation
        ok = True
        for node in ('x', 'y', 'w1', 'w2'):
            inc = 0
            for ln, (n1, n2) in lines.items():
                if n1 == node:
                    inc += o[ln]
                if n2 == node:
                    inc -= o[ln]
            if inc != 0:
                ok = False
                break
        if ok:
            sols.append(o)
    assert len(sols) == 1, f"routing not unique for {pattern}: {sols}"
    return sols[0]

# scalar propagator value: <phi phit> = hbar g^2 / k^2  (orientation-blind)
PROP_S = hbar * g**2 / L2

sq2 = sqrt(2)

def assemble_boxes(branch):
    """branch = 'mu2' or '1'.  Returns dict amp[(r,s,A,B,D,E,cd,dd_)] = coeff of the
    ordered source monomial LAM1*LAM2, where LAM1 = lamt^E_{ddot} at w1 and
    LAM2 = lamt^D_{cdot} at w2.  For branch='mu2' the spectator l l average has
    already been performed (factor T_ave * L2/d_dim); for branch='1' the value is
    kept as an explicit symbolic-l integrand (no average), returned instead as
    amp[(...)][expression]."""
    out = {}
    for pname, pat in patterns.items():
        o = route(pname)
        ksign = pairing_sign(6, pat['psi_pairs'])       # sources LAM1, LAM2 remain
        # source order after contraction: positions 3,5 -> (LAM1, LAM2): canonical.
        w1_gets_psix = (pat['psi_pairs'][0][1] == 2)    # collapse blob tied to w1?
        for r in range(NF):
            for s in range(NF):
                for t in range(NF):
                    # flavor deltas: x-fields flavor t; w1 vertex flavor u; w2 vertex flavor v
                    for u in range(NF):
                        for v in range(NF):
                            # scalar line S1: phit_x(t) -- phi at w2 or w1
                            fS1 = (v if pat['phit_x_to'] == 'w2' else u)
                            if fS1 != t:
                                continue
                            # scalar line S2: phit_y(s) -- phi at w1 or w2
                            fS2 = (u if pat['phit_y_to'] == 'w1' else v)
                            if fS2 != s:
                                continue
                            # fermion line F1: psi_x(t) -- psit at w1/w2
                            fF1 = (u if w1_gets_psix else v)
                            if fF1 != t:
                                continue
                            # fermion line F2: psi_y(r) -- psit at the other vertex
                            fF2 = (v if w1_gets_psix else u)
                            if fF2 != r:
                                continue
                            for A in range(NC):
                                for B in range(NC):
                                    for D in range(NC):
                                        for E in range(NC):
                                            val = box_core(pname, pat, o, ksign, branch,
                                                           A, B, D, E)
                                            if val is None:
                                                continue
                                            for (cd, ddot), x in val.items():
                                                key = (r, s, A, B, D, E, cd, ddot)
                                                out[key] = out.get(key, S(0)) + x
    return out


def box_core(pname, pat, o, ksign, branch, A, B, D, E):
    """Color + spinor + scalar-factor core for one box pattern at fixed externals.
    Returns dict {(cdot, ddot): value} or None."""
    w1_gets_psix = (pat['psi_pairs'][0][1] == 2)
    # The collapse-blob delta ties the insertion index adot(=X) to the psit index of
    # the vertex on the collapse line:
    #   w1_gets_psix: X meets eps_up[X][ddot] at w1; spectator F2 index Y meets
    #                 eps_up[Y][cd] at w2;
    #   else        : X meets eps_up[X][cd] at w2;  Y meets eps_up[Y][ddot] at w1.
    res = {}
    for cd in range(2):
        for ddot in range(2):
            acc = S(0)
            for X in range(2):
                for Y in range(2):
                    if w1_gets_psix:
                        eps_chain = eps_up[X][ddot] * eps_up[Y][cd]
                    else:
                        eps_chain = eps_up[X][cd] * eps_up[Y][ddot]
                    if eps_chain == 0:
                        continue
                    ctot = 0
                    for A1 in range(NC):
                        for A2 in range(NC):
                            for B2 in range(NC):
                                for A3 in range(NC):
                                    for B3 in range(NC):
                                        if pat['phit_x_to'] == 'w2':
                                            if A3 != A1: continue
                                        else:
                                            if A2 != A1: continue
                                        if pat['phit_y_to'] == 'w1':
                                            if A2 != B: continue
                                        else:
                                            if A3 != B: continue
                                        if w1_gets_psix:
                                            if B2 != A1: continue
                                            if B3 != A: continue
                                        else:
                                            if B3 != A1: continue
                                            if B2 != A: continue
                                        ctot += cAB[A2][B2][E] * cAB[A3][B3][D]
                    if ctot == 0:
                        continue
                    if branch == 'mu2':
                        spin = (I * o['S1']) * (c_psi * hbar * g**2 * o['F2'] / L2) \
                               * T_ave[X][Y] * L2 / dd
                        blob = chi * hbar * MU2 / L2
                    else:
                        spin = (I * o['S1']
                                * sum(sig[m][MINUS][X] * LV[m] for m in range(4))) \
                               * (c_psi * hbar * g**2 * o['F2'] / L2
                                  * sum(sig[m][PLUS][Y] * LV[m] for m in range(4)))
                        blob = chi * hbar
                    acc += (-sq2) * blob * spin * eps_chain * ctot \
                           * (sq2 * h / hbar) ** 2 * PROP_S * PROP_S * ksign
            if acc != 0:
                res[(cd, ddot)] = acc
    return res if res else None


amp_mu2 = assemble_boxes('mu2')

# consistency: flavor structure must be delta_{rs}
for key, valx in amp_mu2.items():
    r, s = key[0], key[1]
    if r != s:
        assert simplify(valx) == 0, f"flavor violation at {key}"
ref_rs = {k[2:]: v for k, v in amp_mu2.items() if k[0] == k[1] == 0}
for rr in range(1, NF):
    cmp_rs = {k[2:]: v for k, v in amp_mu2.items() if k[0] == k[1] == rr}
    assert all(simplify(ref_rs.get(k, S(0)) - cmp_rs.get(k, S(0))) == 0
               for k in set(ref_rs) | set(cmp_rs))

print("Section 4: boxes assembled; flavor = delta_rs  ... OK")

# ----------------------------------------------------------------------------
# Section 5: operator matching
# ----------------------------------------------------------------------------
# candidate: A_op = alpha * delta_rs * W_sym[A,B,D',E'] * lamt^{D'}_{ad} lamt^{E' ad}
# with W_sym[A,B,D,E] = sum_C ( c_ACD c_BCE + c_ACE c_BCD ) / 2  (DE-symmetric).
# Source substitution: lamt^X_{xd} -> LAM1 d[X,E] d[xd,ddot] + LAM2 d[X,D] d[xd,cd];
# canonical coefficient of LAM1*LAM2 extracted with the GP engine.
def op_amp(A, B, D, E, cd, ddot):
    tot = S(0)
    for Dp in range(NC):
        for Ep in range(NC):
            w = S(0)
            for C in range(NC):
                w += Rational(1, 2) * (cAB[A][C][Dp] * cAB[B][C][Ep]
                                       + cAB[A][C][Ep] * cAB[B][C][Dp])
            if w == 0:
                continue
            for ad in range(2):
                for bd in range(2):
                    e = eps_up[ad][bd]
                    if e == 0:
                        continue
                    # lamt^{Dp}_{ad} lamt^{Ep}_{bd} -> sources
                    poly = GP()
                    f1 = GP()
                    if Dp == E and ad == ddot:
                        f1 = f1.add(GP.gen(LAM1))
                    if Dp == D and ad == cd:
                        f1 = f1.add(GP.gen(LAM2))
                    f2 = GP()
                    if Ep == E and bd == ddot:
                        f2 = f2.add(GP.gen(LAM1))
                    if Ep == D and bd == cd:
                        f2 = f2.add(GP.gen(LAM2))
                    poly = f1.mul(f2)
                    tot += w * e * poly.d.get((LAM1, LAM2), S(0))
    return tot

# fit alpha over all components at r=s=0
alpha = None
mismatch = []
for A in range(NC):
    for B in range(NC):
        for D in range(NC):
            for E in range(NC):
                for cd in range(2):
                    for ddot in range(2):
                        lhs = amp_mu2.get((0, 0, A, B, D, E, cd, ddot), S(0))
                        rhs = op_amp(A, B, D, E, cd, ddot)
                        if rhs == 0:
                            if simplify(lhs) != 0:
                                mismatch.append((A, B, D, E, cd, ddot, lhs))
                        else:
                            a = simplify(lhs / rhs)
                            if alpha is None:
                                alpha = a
                            elif simplify(a - alpha) != 0:
                                mismatch.append((A, B, D, E, cd, ddot, a, alpha))
assert not mismatch, f"operator fit failed: {mismatch[:5]}"
alpha = simplify(alpha.subs(dd, 4))
print(f"Section 5: operator fit: A_mu2 = alpha * W_sym * lamt lamt with")
print(f"           alpha (units: master 1/32pi^2 after  MU2*L2/L2^4 -> 1) = {alpha}")

# strip the master-integral bookkeeping: the assembled coefficient multiplies
# MU2/L2^3 == MU2*L2/L2^4  -> master value 1/(32 pi^2).  Express alpha = A0 * MU2/L2**3:
A0 = simplify(alpha * L2**3 / MU2)
assert not A0.has(L2) and not A0.has(MU2), f"unexpected structure: {alpha}"
M32 = Symbol('M32')   # stands for 1/(32*pi^2)
print(f"           => A_op = ({A0}) * M32 * delta_rs * Sym[c_ACD c_BCE] lamt^D_ad lamt^E^ad,"
      f"  M32 = 1/(32 pi^2)")

# ----------------------------------------------------------------------------
# Section 6: tree contact and final normalization
# ----------------------------------------------------------------------------
# I5 term of (5D.4): +sqrt2 eps_{-b} F_r E_psi^b ; collapse on the pair's psi_{r+}:
# <E_psi^b(x) psi_{r+}(y)> = chi_L hbar delta^b_+ delta(x-y); Koszul sign +1
# (E adjacent to psi_y in the odd sequence [E, psi_y]).
tree_coeff = sq2 * eps_lo[MINUS][PLUS] * chi_L * hbar          # coefficient of F_r phit_s
# delta_- O = -sqrt2 F_r phit_s  (5D.3)  => contact = (-chi_L hbar) * delta_- O
ratio = simplify(tree_coeff / (-sq2))                          # = -chi_L * hbar
print(f"Section 6: tree contact = ({tree_coeff}) F_r phit_s = (-chi_L hbar) delta_-O; "
      f"normalization factor -chi hbar = {simplify(-chi*hbar)}")

# Ward identity:  <dj O legs> = (-chi hbar) [ delta_-O + Q1 O ]  =>
#   Q1 O = A_op / (-chi hbar)
Q1_coeff = simplify(A0 * (-1) / (chi * hbar))
print(f"           Q1(psi_r+ phit_s) = ({Q1_coeff}) * M32 * delta_rs "
      f"* Sym[c_ACD c_BCE] * lamt^D_ad lamt^E^ad")

# ----------------------------------------------------------------------------
# Section 7: certificate -- T-a cancels the '1'-branches exactly
# ----------------------------------------------------------------------------
# T-a insertion (I6-Yukawa part, derived from (5C.13) left-derivative):
#   I6Y = -2h (sigma^m)_{-ad} eps^{ad bd'} c[B1][C1][A1] (d_m phit^{A1}_t) phi^{B1}_t
#         lamt^{C1}_{bd'}    (lamt at x is an external source slot)
# graph: x -- w (V2) -- y; lines: S1: phit_x -- phi_w ; S2: phi_x -- phit_y ;
#         F: psi_y -- psit_w.  Two source-slot assignments:
#   (i) lamt_x = LAM1 (E, ddot), V2-lamt = LAM2 (D, cd)   <-> B_par '1'-branch
#  (ii) lamt_x = LAM2 (D, cd),  V2-lamt = LAM1 (E, ddot)  <-> B_cross '1'-branch
def route_Ta():
    lines = {'S1': ('x', 'w'), 'S2': ('x', 'y'), 'F': ('y', 'w')}
    sols = []
    for os_ in itertools.product((1, -1), repeat=3):
        o = dict(zip(('S1', 'S2', 'F'), os_))
        if o['S1'] != 1:
            continue
        ok = True
        for node in ('x', 'y', 'w'):
            inc = 0
            for ln, (n1, n2) in lines.items():
                if n1 == node:
                    inc += o[ln]
                if n2 == node:
                    inc -= o[ln]
            if inc != 0:
                ok = False
                break
        if ok:
            sols.append(o)
    assert len(sols) == 1
    return sols[0]

def assemble_Ta(slot_x):   # slot_x in ('LAM1','LAM2')
    o = route_Ta()
    out = {}
    # odd sequence: [lamt_x(src), psi_y, psit_w, lam_w(src)] -> pair (1,2) adjacent
    ks = pairing_sign(4, [(1, 2)])
    assert ks == 1
    for A in range(NC):
        for B in range(NC):
            for D in range(NC):
                for E in range(NC):
                    for cd in range(2):
                        for ddot in range(2):
                            acc = S(0)
                            for ad in range(2):
                                for bdp in range(2):
                                    e1 = eps_up[ad][bdp]
                                    if e1 == 0:
                                        continue
                                    # source slot at x:
                                    if slot_x == 'LAM1':
                                        C1, xd = E, ddot
                                        Cw, wd = D, cd
                                    else:
                                        C1, xd = D, cd
                                        Cw, wd = E, ddot
                                    if bdp != xd:
                                        continue
                                    for cd1 in range(2):   # psit_w index
                                        e2 = eps_up[cd1][wd]
                                        if e2 == 0:
                                            continue
                                        ctot = 0
                                        for A1 in range(NC):
                                            for B1 in range(NC):
                                                for A2 in range(NC):
                                                    for B2 in range(NC):
                                                        # S1: phit_x(A1)--phi_w(A2)
                                                        if A2 != A1: continue
                                                        # S2: phi_x(B1)--phit_y(B)
                                                        if B1 != B: continue
                                                        # F: psi_y(A)--psit_w(B2)
                                                        if B2 != A: continue
                                                        ctot += cAB[B1][C1][A1] \
                                                                * cAB[A2][B2][Cw]
                                        if ctot == 0:
                                            continue
                                        spin = sum(sig[m][MINUS][ad] * LV[m]
                                                   for m in range(4)) * (I * o['S1']) \
                                               * (c_psi * hbar * g**2 * o['F'] / L2
                                                  * sum(sig[m][PLUS][cd1] * LV[m]
                                                        for m in range(4)))
                                        acc += (-2 * h) * e1 * e2 * ctot * spin \
                                               * (sq2 * h / hbar) * PROP_S * PROP_S * ks
                            # source-order canonicalization: for slot_x = LAM2 the
                            # construction order is (LAM2, LAM1) -> sign -1
                            if slot_x == 'LAM2':
                                acc = -acc
                            if acc != 0:
                                out[(A, B, D, E, cd, ddot)] = acc
    return out

amp_1 = assemble_boxes('1')
one_par = {k[2:]: v for k, v in amp_1.items() if k[0] == k[1] == 0}
# split '1'-branch by pattern: rebuild each pattern separately for the certificate
def assemble_one_pattern(pname):
    keep = {n: patterns[n] for n in patterns}
    saved = dict(patterns)
    try:
        patterns.clear()
        patterns[pname] = saved[pname]
        res = assemble_boxes('1')
    finally:
        patterns.clear()
        patterns.update(saved)
    return {k[2:]: v for k, v in res.items() if k[0] == k[1] == 0}

one_Bpar = assemble_one_pattern('B_par')
one_Bcross = assemble_one_pattern('B_cross')
Ta_E = assemble_Ta('LAM1')
Ta_D = assemble_Ta('LAM2')

def check_cancel(t_amp, b_amp, name):
    keys = set(t_amp) | set(b_amp)
    for k in keys:
        sdiff = simplify(expand(t_amp.get(k, S(0)) + b_amp.get(k, S(0))))
        assert sdiff == 0, f"certificate {name} fails at {k}: {sdiff}"

check_cancel(Ta_E, one_Bpar, "T-a(E at x) + B_par-1branch")
check_cancel(Ta_D, one_Bcross, "T-a(D at x) + B_cross-1branch")
print("Section 7: certificate: T-a + '1'-branches = 0 identically  ... OK")

# ----------------------------------------------------------------------------
print()
print("=" * 76)
print("RESULT (su(2) instance, exact):")
print(f"  chi (SD collapse sign)        = {chi}")
print(f"  c_psi (fermion prop constant) = {c_psi}")
print(f"  Q1(psi_{{r+}}^A phit_s^B) = ({Q1_coeff}) * (1/32pi^2) * delta_rs")
print(f"      * Sym_C[c_ACD c_BCE] * lamt^D_ad lamt^{{E ad}}   + O(eps), O(g^4)")
print("  (units: hbar g^2 explicit in the printed coefficient)")
print("=" * 76)
