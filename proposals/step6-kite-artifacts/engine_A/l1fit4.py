"""Full covariant dictionary fit: chains + brackets (all X letters) + E1/E2/SC."""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import chain_poly, M_p, M_q
from constraints import constraint_subst, gp_apply_subst
from util_solve import solve_structures
import pickle, time

XI1, XI2 = 16, 17
agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl","rb"))
target = color_canon([('A','m','D'), ('B','m','E')])[1]
subst = {}
subst.update(constraint_subst("wt0", M_q, "antichiral", XI1))
subst.update(constraint_subst("wt1", M_q, "antichiral", XI1))
subst.update(constraint_subst("wp", M_p, "chiral", XI2))
subst.update(constraint_subst("wm", M_p, "chiral", XI2))
MOMB = {'k': pmat({'k':1}), 'q': pmat({'q':1}), 'p': pmat({'p':1})}
MOMS = ['k','q','p']
EPS = {(0,1):Fr(1),(1,0):Fr(-1)}
wt = [gp_apply_subst(ext_superfield(0,"wt%d"%ad, XI1,1), subst) for ad in range(2)]
wpj = gp_apply_subst(ext_superfield(0,"wp", XI2,1), subst)
wmj = gp_apply_subst(ext_superfield(0,"wm", XI2,1), subst)
def jet(F, letters, M): return gp_apply_subst(apply_word(F, CONE, letters, 0, M), subst)
Xv = {"D+W^+": jet(wpj,[('D',0)],M_p), "D+W^-": jet(wmj,[('D',0)],M_p),
      "D-W^+": jet(wpj,[('D',1)],M_p), "D-W^-": jet(wmj,[('D',1)],M_p)}
D2W = {"D2W^+": gp_scale(jet(wpj,[('D',1),('D',0)],M_p),(Fr(2),Fr(0))),
       "D2W^-": gp_scale(jet(wmj,[('D',1),('D',0)],M_p),(Fr(2),Fr(0)))}
DbWt = {(i,j): jet(wt[j],[('Db',i)],M_q) for i in range(2) for j in range(2)}
structs = {}
for x in MOMS:
    for y in MOMS:
        for z in MOMS:
            ch = chain_poly(MOMB[x], pmat_bar(MOMB[y]), MOMB[z])
            for Xn, Xp in Xv.items():
                S = gp_zero()
                for ad in range(2):
                    S = gp_add(S, gp_scale_cp(gp_mul(wt[ad], Xp), ch[ad]))
                structs[("ch",x,y,z,Xn)] = S
for xi_, x in enumerate(MOMS):
    for yi_, y in enumerate(MOMS):
        if yi_ <= xi_: continue
        br = {}
        for a in range(2):
            for b in range(2):
                s = EPS.get((a,b))
                if s: br = cp_add(br, cp_scale(cp_mul(MOMB[x][0][a], MOMB[y][0][b]), (s, Fr(0))))
        for z in MOMS:
            zWt = gp_zero()
            for cd in range(2):
                for al in range(2):
                    s = EPS.get((cd, al))
                    if s: zWt = gp_add(zWt, gp_scale_cp(wt[al], cp_scale(MOMB[z][0][cd], (s, Fr(0)))))
            for Xn, Xp in Xv.items():
                structs[("br<%s%s>"%(x,y), z, Xn)] = gp_scale_cp(gp_mul(zWt, Xp), br)
for x in MOMS:
    for y in MOMS:
        for Wn, Wp in D2W.items():
            E1 = gp_zero(); E2 = gp_zero()
            for i in range(2):
                for j in range(2):
                    E1 = gp_add(E1, gp_scale_cp(gp_mul(DbWt[(i,j)], Wp),
                                                cp_mul(MOMB[x][0][i], MOMB[y][0][j])))
                    ri = {}; rj = {}
                    for ip in range(2):
                        s = EPS.get((i, ip))
                        if s: ri = cp_add(ri, cp_scale(MOMB[x][0][ip], (s, Fr(0))))
                    for jp in range(2):
                        s = EPS.get((j, jp))
                        if s: rj = cp_add(rj, cp_scale(MOMB[y][0][jp], (s, Fr(0))))
                    E2 = gp_add(E2, gp_scale_cp(gp_mul(DbWt[(i,j)], Wp), cp_mul(ri, rj)))
            structs[("E1",x,y,Wn)] = E1
            structs[("E2",x,y,Wn)] = E2
def inv2(x, y):
    A, Bb = MOMB[x], pmat_bar(MOMB[y])
    e = {}
    for a in range(2):
        for bd in range(2):
            e = cp_add(e, cp_mul(A[a][bd], Bb[bd][a]))
    return e
DbdotWt = gp_add(DbWt[(0,1)], gp_scale(DbWt[(1,0)], (Fr(-1),Fr(0))))
for xi_, x in enumerate(MOMS):
    for yi_, y in enumerate(MOMS):
        if yi_ < xi_: continue
        iv = inv2(x, y)
        for Wn, Wp in D2W.items():
            structs[("SC",x,y,Wn)] = gp_scale_cp(gp_mul(DbdotWt, Wp), iv)
print("dict size", len(structs), flush=True)
for nm, agg in (("a", agg_a), ("b", agg_b)):
    R = gp_apply_subst(agg.get(target, gp_zero()), subst)
    t0 = time.time()
    sol = solve_structures(R, structs)
    if sol is None:
        print("term %s: NO exact fit (%.0fs)" % (nm, time.time()-t0), flush=True)
    else:
        print("term %s EXACT FIT (%.0fs):" % (nm, time.time()-t0), flush=True)
        for k, v in sorted(sol.items()):
            print("   %-32s (%s, %s)" % (str(k), v[0], v[1]), flush=True)
