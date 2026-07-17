"""Bilinear covariant-jet decomposition at theta_0 for two external letters.

R is decomposed as
   R = sum  c_{t,(V1,c1),(V2,c2)}  t(theta0) * [V1 F1_c1](th0) * [V2 F2_c2](th0)
triangularly: theta0-monomials ascending, total component-degree descending.
Odd components carry xi tags (XI1 for field 1, XI2 for field 2) per ext_superfield.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *
from model import (jet_words, ext_superfield, lead_form, theta_pt, xi_pt,
                   _compdeg, apply_word)

XI1, XI2 = 16, 17

def build_basis(prefixes, MF, xi, parity):
    """for each comp prefix: dict (jetname,pref) -> GPoly."""
    B = {}
    for pref in prefixes:
        F = ext_superfield(0, pref, xi, parity)
        for name, w in jet_words():
            B[(name, pref)] = apply_word(F, w[0], w[1], 0, MF)
    return B

def decompose_bilinear(R, basisA, basisB, prefA, prefB):
    """returns rows [(t, (nameA,prefA), (nameB,prefB), CP)], residual ({} on success)."""
    wl = {n: len(w[1]) for n, w in jet_words()}
    leadA = {ka: lead_form(basisA[ka], prefA) for ka in basisA}
    leadB = {kb: lead_form(basisB[kb], prefB) for kb in basisB}
    diagA = {}
    for ka in basisA:
        cand = [s for s in leadA[ka] if _compdeg(s) == wl[ka[0]]]
        assert len(cand) == 1, (ka, cand)
        diagA[ka] = cand[0]
    diagB = {}
    for kb in basisB:
        cand = [s for s in leadB[kb] if _compdeg(s) == wl[kb[0]]]
        assert len(cand) == 1, (kb, cand)
        diagB[kb] = cand[0]
    prodcache = {}
    def prodpoly(ka, kb):
        if (ka, kb) not in prodcache:
            prodcache[(ka, kb)] = gp_mul(basisA[ka], basisB[kb])
        return prodcache[(ka, kb)]
    rows = []
    Rw = {m: dict(c) for m, c in R.items()}
    guard = 0
    while Rw:
        guard += 1
        if guard > 400: raise RuntimeError("no convergence")
        t = min((theta_pt(m) for m in Rw), key=lambda x: (len(x),) + x)
        work = {}
        for m, cp in Rw.items():
            if theta_pt(m) != t: continue
            xit = xi_pt(m)
            for mono, c in cp.items():
                k = (xit, mono)
                v = cadd(work.get(k, CZERO), c)
                if ciszero(v): work.pop(k, None)
                else: work[k] = v
        found = {}
        for degtot in range(8, -1, -1):
            for ka in basisA:
                for kb in basisB:
                    if wl[ka[0]] + wl[kb[0]] != degtot: continue
                    da, db = diagA[ka], diagB[kb]
                    xa, ca_d = leadA[ka][da]
                    xb, cb_d = leadB[kb][db]
                    cn = {}
                    for (xit, mono), c in list(work.items()):
                        if da in mono and db in mono:
                            rest = list(mono); rest.remove(da); rest.remove(db)
                            cn[tuple(rest)] = cadd(cn.get(tuple(rest), CZERO), c)
                    if not cn: continue
                    dc = cmul(ca_d[()], cb_d[()])
                    assert dc[1] == 0 and dc[0] != 0
                    cw = cp_scale(cn, (Fr(1) / dc[0], Fr(0)))
                    found[(ka, kb)] = cp_add(found.get((ka, kb), {}), cw)
                    # subtract cw * (theta-free bilinear form of A_ka*B_kb)
                    for sa, (xsa, cpa) in leadA[ka].items():
                        for sb, (xsb, cpb) in leadB[kb].items():
                            # merge xi tuples: XI1 parts < XI2 parts, disjoint -> sign +1
                            xu = tuple(sorted(xsa + xsb))
                            sub = cp_mul(cw, cp_mul(cpa, cpb))
                            for mono, c in sub.items():
                                k = (xu, tuple(sorted(mono + (sa, sb))))
                                v = cadd(work.get(k, CZERO), cneg(c))
                                if ciszero(v): work.pop(k, None)
                                else: work[k] = v
        if work:
            raise RuntimeError("bilinear residual at theta part %s (%d keys)" % (str(t), len(work)))
        if not found:
            raise RuntimeError("stuck at theta part %s" % (str(t),))
        for (ka, kb), cw in found.items():
            if not cw: continue
            rows.append((t, ka, kb, cw))
            TB = gp_scale_cp(prodpoly(ka, kb), cw)
            for g in reversed(t):
                TB = gp_mulgen(TB, g)
            for m, c in TB.items():
                v = cp_add(Rw.get(m, {}), cp_scale(c, (Fr(-1), Fr(0))))
                if not v: Rw.pop(m, None)
                else: Rw[m] = v
    return rows, Rw
