"""Chain-sector ledger fit against ALL middles + A-type brackets (row space)."""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import chain_poly, M_p, M_q
from constraints import gp_apply_subst
from util_solve import solve_structures
from l1rows import bilinear_rows, subst
import pickle, io, contextlib, itertools

XI1, XI2 = 16, 17
agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
MOMB = {'k': pmat({'k': 1}), 'q': pmat({'q': 1}), 'p': pmat({'p': 1})}
EPS = {(0, 1): Fr(1), (1, 0): Fr(-1)}

wt = [gp_apply_subst(ext_superfield(0, "wt%d" % ad, XI1, 1), subst) for ad in range(2)]
wmj = gp_apply_subst(ext_superfield(0, "wm", XI2, 1), subst)
X = gp_apply_subst(apply_word(wmj, CONE, [('D', 0)], 0, M_p), subst)  # D+W^-

def rows_of(Xp):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rows = bilinear_rows(Xp, "x")
    return {(ka, kb): cw for t, ka, kb, cw in rows}

cand = {}
for x in MOMB:
    for y in MOMB:
        for z in MOMB:
            ch = chain_poly(MOMB[x], pmat_bar(MOMB[y]), MOMB[z])
            S = gp_zero()
            for ad in range(2):
                S = gp_add(S, gp_scale_cp(gp_mul(wt[ad], X), ch[ad]))
            cand[("ch", x, y, z)] = rows_of(S)
for xi_, x in enumerate(MOMB):
    for yi_, y in enumerate(MOMB):
        if yi_ <= xi_: continue
        br = {}
        for a in range(2):
            for b in range(2):
                s = EPS.get((a, b))
                if s: br = cp_add(br, cp_scale(cp_mul(MOMB[x][0][a], MOMB[y][0][b]), (s, Fr(0))))
        for z in MOMB:
            zWt = gp_zero()
            for cd in range(2):
                for al in range(2):
                    s = EPS.get((cd, al))
                    if s: zWt = gp_add(zWt, gp_scale_cp(wt[al], cp_scale(MOMB[z][0][cd], (s, Fr(0)))))
            A = gp_scale_cp(gp_mul(zWt, X), br)
            cand[("A<%s%s>" % (x, y), z)] = rows_of(A)

CHAINKEYS = [(("v", "wt0"), ("D[+]v", "wm")), (("v", "wt1"), ("D[+]v", "wm"))]

def family_fit(rows):
    R = {}
    for n, k in enumerate(CHAINKEYS):
        if k in rows: R[(n,)] = rows[k]
    structs = {}
    for cname, crows in cand.items():
        s = {}
        for n, k in enumerate(CHAINKEYS):
            if k in crows: s[(n,)] = crows[k]
        if s: structs[cname] = s
    return solve_structures(R, structs)

for term, per in (("a", per_a), ("b", per_b)):
    for (asg1, asg2), (canon, tot) in sorted(per.items()):
        rows = rows_of(gp_apply_subst(tot, subst))
        sol = family_fit(rows)
        if sol is None:
            print("term %s %s %s: NOT in extended chain span" % (term, asg1, asg2), flush=True)
        else:
            pretty = ", ".join("%s=(%s,%s)" % ("".join(map(str, k)), v[0], v[1])
                               for k, v in sorted(sol.items()))
            print("term %s %s %s:\n    %s" % (term, asg1, asg2, pretty), flush=True)
