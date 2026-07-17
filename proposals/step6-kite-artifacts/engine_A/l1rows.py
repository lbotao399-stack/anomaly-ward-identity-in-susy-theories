"""Canonical constrained bilinear rows of R_a, R_b and S."""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import structure, MOM, M_p, M_q
from model import _compdeg, lead_form, theta_pt, xi_pt
from constraints import constraint_subst, gp_apply_subst
import pickle

XI1, XI2 = 16, 17
agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]

subst = {}
subst.update(constraint_subst("wt0", M_q, "antichiral", XI1))
subst.update(constraint_subst("wt1", M_q, "antichiral", XI1))
subst.update(constraint_subst("wp", M_p, "chiral", XI2))
subst.update(constraint_subst("wm", M_p, "chiral", XI2))

WORDS_A = [("v", (CONE, [])), ("Db[1]v", (CONE, [('Db', 0)])), ("Db[2]v", (CONE, [('Db', 1)])),
           ("Db2v", W_Db2)]
WORDS_B = [("v", (CONE, [])), ("D[+]v", (CONE, [('D', 0)])), ("D[-]v", (CONE, [('D', 1)])),
           ("D2v", W_D2)]

def build(prefixes, words, M, xi):
    B = {}
    for pref in prefixes:
        F0 = gp_apply_subst(ext_superfield(0, pref, xi, 1), subst)
        for name, w in words:
            B[(name, pref)] = gp_apply_subst(apply_word(F0, w[0], w[1], 0, M), subst)
    return B

basisA = build(["wt0", "wt1"], WORDS_A, M_q, XI1)
basisB = build(["wp", "wm"], WORDS_B, M_p, XI2)

WLA = {n: len(w[1]) for n, w in WORDS_A}
WLB = {n: len(w[1]) for n, w in WORDS_B}

def bilinear_rows(R, label):
    leadA = {ka: lead_form(basisA[ka], ["wt0", "wt1"]) for ka in basisA}
    leadB = {kb: lead_form(basisB[kb], ["wp", "wm"]) for kb in basisB}
    diagA = {}
    for ka in basisA:
        cand = [s for s in leadA[ka] if _compdeg(s) == WLA[ka[0]]]
        assert len(cand) == 1, (ka, sorted(leadA[ka]))
        diagA[ka] = cand[0]
    diagB = {}
    for kb in basisB:
        cand = [s for s in leadB[kb] if _compdeg(s) == WLB[kb[0]]]
        assert len(cand) == 1, (kb, sorted(leadB[kb]))
        diagB[kb] = cand[0]
    prod = {}
    def pp(ka, kb):
        if (ka, kb) not in prod: prod[(ka, kb)] = gp_mul(basisA[ka], basisB[kb])
        return prod[(ka, kb)]
    rows = []
    Rw = {m: dict(c) for m, c in R.items()}
    guard = 0
    while Rw:
        guard += 1
        if guard > 400: raise RuntimeError("noconv")
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
        for degtot in range(6, -1, -1):
            for ka in basisA:
                for kb in basisB:
                    if WLA[ka[0]] + WLB[kb[0]] != degtot: continue
                    da, db = diagA[ka], diagB[kb]
                    cn = {}
                    for (xit, mono), c in list(work.items()):
                        if da in mono and db in mono:
                            rest = list(mono); rest.remove(da); rest.remove(db)
                            cn[tuple(rest)] = cadd(cn.get(tuple(rest), CZERO), c)
                    if not cn: continue
                    dc = cmul(leadA[ka][da][1][()], leadB[kb][db][1][()])
                    cw = cp_scale(cn, (Fr(1) / dc[0], Fr(0)))
                    found[(ka, kb)] = cp_add(found.get((ka, kb), {}), cw)
                    for sa, (xsa, cpa) in leadA[ka].items():
                        for sb, (xsb, cpb) in leadB[kb].items():
                            xu = tuple(sorted(xsa + xsb))
                            sub = cp_mul(cw, cp_mul(cpa, cpb))
                            for mono, c in sub.items():
                                k = (xu, tuple(sorted(mono + (sa, sb))))
                                v = cadd(work.get(k, CZERO), cneg(c))
                                if ciszero(v): work.pop(k, None)
                                else: work[k] = v
        if work:
            raise RuntimeError("residual at %s in %s: %s" % (str(t), label, list(work)[:4]))
        if not found:
            raise RuntimeError("stuck")
        for (ka, kb), cw in found.items():
            if not cw: continue
            rows.append((t, ka, kb, cw))
            TB = gp_scale_cp(pp(ka, kb), cw)
            for g in reversed(t):
                TB = gp_mulgen(TB, g)
            for m, c in TB.items():
                v = cp_add(Rw.get(m, {}), cp_scale(c, (Fr(-1), Fr(0))))
                if not v: Rw.pop(m, None)
                else: Rw[m] = v
    print("== %s: %d rows" % (label, len(rows)))
    for t, ka, kb, cw in sorted(rows, key=lambda r: (r[0], r[1], r[2])):
        t0 = "*".join(str(g) for g in t) or "-"
        print("   th0=%-6s [%s %s]x[%s %s]   %s" % (t0, ka[0], ka[1], kb[0], kb[1], cp_str(cw)))
    return rows

if __name__ == "__main__":
    ML1 = pmat({'k': 2, 'q': 1}); ML2 = pmat({'k': 2, 'p': 1, 'q': 2})
    bilinear_rows(gp_apply_subst(structure(ML1, ML2), subst), "S(L1,L2) constrained")
    bilinear_rows(gp_apply_subst(agg_a.get(target, gp_zero()), subst), "R_a constrained")
    bilinear_rows(gp_apply_subst(agg_b.get(target, gp_zero()), subst), "R_b constrained")
