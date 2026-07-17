"""Row-space fit with explicit residual: what part of R_a is outside the span?"""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import chain_poly, M_p, M_q
from constraints import gp_apply_subst
from l1rows import bilinear_rows, subst
import pickle, io, contextlib

XI1, XI2 = 16, 17
agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]
MOMB = {'k': pmat({'k': 1}), 'q': pmat({'q': 1}), 'p': pmat({'p': 1})}
MOMS = ['k', 'q', 'p']
EPS = {(0, 1): Fr(1), (1, 0): Fr(-1)}

wt = [gp_apply_subst(ext_superfield(0, "wt%d" % ad, XI1, 1), subst) for ad in range(2)]
wpj = gp_apply_subst(ext_superfield(0, "wp", XI2, 1), subst)
wmj = gp_apply_subst(ext_superfield(0, "wm", XI2, 1), subst)
def jet(F, letters, M): return gp_apply_subst(apply_word(F, CONE, letters, 0, M), subst)
Xv = {"D+W^+": jet(wpj, [('D', 0)], M_p), "D+W^-": jet(wmj, [('D', 0)], M_p),
      "D-W^+": jet(wpj, [('D', 1)], M_p), "D-W^-": jet(wmj, [('D', 1)], M_p)}
D2W = {"D2W^+": gp_scale(jet(wpj, [('D', 1), ('D', 0)], M_p), (Fr(2), Fr(0))),
       "D2W^-": gp_scale(jet(wmj, [('D', 1), ('D', 0)], M_p), (Fr(2), Fr(0)))}
DbWt = {(i, j): jet(wt[j], [('Db', i)], M_q) for i in range(2) for j in range(2)}

def rows_of(Xp):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rows = bilinear_rows(Xp, "x")
    out = {}
    for t, ka, kb, cw in rows:
        out[(t, ka, kb)] = cp_add(out.get((t, ka, kb), {}), cw)
    return out

cands = {}
for x in MOMS:
    for y in MOMS:
        for z in MOMS:
            ch = chain_poly(MOMB[x], pmat_bar(MOMB[y]), MOMB[z])
            for Xn, Xp in Xv.items():
                S = gp_zero()
                for ad in range(2):
                    S = gp_add(S, gp_scale_cp(gp_mul(wt[ad], Xp), ch[ad]))
                cands[("ch", x, y, z, Xn)] = rows_of(S)
for ix, x in enumerate(MOMS):
    for iy, y in enumerate(MOMS):
        if iy <= ix: continue
        br = {}
        for a in range(2):
            for b in range(2):
                s = EPS.get((a, b))
                if s: br = cp_add(br, cp_scale(cp_mul(MOMB[x][0][a], MOMB[y][0][b]), (s, Fr(0))))
        for z in MOMS:
            zWt = gp_zero()
            for cd in range(2):
                for al in range(2):
                    s = EPS.get((cd, al))
                    if s: zWt = gp_add(zWt, gp_scale_cp(wt[al], cp_scale(MOMB[z][0][cd], (s, Fr(0)))))
            for Xn, Xp in Xv.items():
                cands[("br", x, y, z, Xn)] = rows_of(gp_scale_cp(gp_mul(zWt, Xp), br))
for x in MOMS:
    for y in MOMS:
        for Wn, Wp in D2W.items():
            E1 = gp_zero(); E2 = gp_zero()
            for i in range(2):
                for j in range(2):
                    E1 = gp_add(E1, gp_scale_cp(gp_mul(DbWt[(i, j)], Wp),
                                                cp_mul(MOMB[x][0][i], MOMB[y][0][j])))
                    ri = {}; rj = {}
                    for ip in range(2):
                        s = EPS.get((i, ip))
                        if s: ri = cp_add(ri, cp_scale(MOMB[x][0][ip], (s, Fr(0))))
                    for jp in range(2):
                        s = EPS.get((j, jp))
                        if s: rj = cp_add(rj, cp_scale(MOMB[y][0][jp], (s, Fr(0))))
                    E2 = gp_add(E2, gp_scale_cp(gp_mul(DbWt[(i, j)], Wp), cp_mul(ri, rj)))
            cands[("E1", x, y, Wn)] = rows_of(E1)
            cands[("E2", x, y, Wn)] = rows_of(E2)

R = rows_of(gp_apply_subst(agg_a.get(target, gp_zero()), subst))

# build exact linear system over (rowkey, mono): columns = candidates (complex)
keys = set(R)
for c in cands.values(): keys |= set(c)
eqkeys = []
for k in sorted(keys, key=str):
    monos = set(R.get(k, {}))
    for c in cands.values(): monos |= set(c.get(k, {}))
    for m in sorted(monos):
        eqkeys.append((k, m))
names = sorted(cands, key=str)
# complex -> 2 real unknowns
ncol = 2 * len(names)
M = []
for (k, m) in eqkeys:
    row = []
    for n in names:
        cr, ci = cands[n].get(k, {}).get(m, (Fr(0), Fr(0)))
        row += [cr, -ci]
    bre, bim = R.get(k, {}).get(m, (Fr(0), Fr(0)))
    M.append((row, bre, (k, m), 're'))
    row2 = []
    for n in names:
        cr, ci = cands[n].get(k, {}).get(m, (Fr(0), Fr(0)))
        row2 += [ci, cr]
    M.append((row2, bim, (k, m), 'im'))

# gaussian elimination on augmented
aug = [r + [b] for (r, b, _, _) in M]
meta = [(km, p) for (_, _, km, p) in M]
rr = 0
usedrows = set()
for c in range(ncol):
    pr = None
    for i in range(rr, len(aug)):
        if aug[i][c] != 0: pr = i; break
    if pr is None: continue
    aug[rr], aug[pr] = aug[pr], aug[rr]
    meta[rr], meta[pr] = meta[pr], meta[rr]
    pv = aug[rr][c]
    aug[rr] = [x / pv for x in aug[rr]]
    for i in range(len(aug)):
        if i != rr and aug[i][c] != 0:
            f = aug[i][c]
            aug[i] = [x - f * y for x, y in zip(aug[i], aug[rr])]
    rr += 1
resid = [(meta[i], aug[i][ncol]) for i in range(rr, len(aug)) if aug[i][ncol] != 0]
print("candidates:", len(names), " equations:", len(aug), " rank:", rr)
print("residual equations (unsatisfiable):", len(resid))
seenk = {}
for ((k, m), p), val in resid[:400]:
    seenk.setdefault(str(k), []).append((m, p, val))
for k, lst in sorted(seenk.items()):
    print("ROW", k)
    for m, p, val in lst[:8]:
        print("    ", m, p, val)
