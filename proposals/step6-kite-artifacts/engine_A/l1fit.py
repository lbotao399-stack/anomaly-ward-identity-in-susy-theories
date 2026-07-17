"""Fit constrained Level-1 totals against a covariant dictionary:
   chains  S_{x,y,z}(Xvar)  = [p(x) pbar(y) p(z)]_{+}{}^{ad} Wt_ad * Xvar
   E1_{x,y}(comb)           = p(x)_{+ad} p(y)_{+bd} (Db-jet of Wt) (D2-jet of W)
All built on the constrained subspace."""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import chain_poly, M_p, M_q
from constraints import constraint_subst, gp_apply_subst
from util_solve import solve_structures
import pickle, itertools, time

XI1, XI2 = 16, 17
agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]

subst = {}
subst.update(constraint_subst("wt0", M_q, "antichiral", XI1))
subst.update(constraint_subst("wt1", M_q, "antichiral", XI1))
subst.update(constraint_subst("wp", M_p, "chiral", XI2))
subst.update(constraint_subst("wm", M_p, "chiral", XI2))

MOMB = {'k': pmat({'k': 1}), 'q': pmat({'q': 1}), 'p': pmat({'p': 1})}

wt = [gp_apply_subst(ext_superfield(0, "wt%d" % ad, XI1, 1), subst) for ad in range(2)]
wpj = gp_apply_subst(ext_superfield(0, "wp", XI2, 1), subst)
wmj = gp_apply_subst(ext_superfield(0, "wm", XI2, 1), subst)

def jet(F, letters, M):
    return gp_apply_subst(apply_word(F, CONE, letters, 0, M), subst)

Xv = {
    "D+W^+": jet(wpj, [('D', 0)], M_p),
    "D+W^-": jet(wmj, [('D', 0)], M_p),
    "D-W^+": jet(wpj, [('D', 1)], M_p),
    "D-W^-": jet(wmj, [('D', 1)], M_p),
}
D2W = {"D2W^+": jet(wpj, [('D', 1), ('D', 0)], M_p),
       "D2W^-": jet(wmj, [('D', 1), ('D', 0)], M_p)}
for k in D2W: D2W[k] = gp_scale(D2W[k], (Fr(2), Fr(0)))   # D^2 = 2 D_- D_+
DbWt = {}
for i in range(2):
    for j in range(2):
        DbWt[(i, j)] = jet(wt[j], [('Db', i)], M_q)   # Db_i Wt_j (lower indices)

structs = {}
# chains x X variants
for x in MOMB:
    for y in MOMB:
        for z in MOMB:
            ch = chain_poly(MOMB[x], pmat_bar(MOMB[y]), MOMB[z])
            for Xn, Xp in Xv.items():
                S = gp_zero()
                for ad in range(2):
                    S = gp_add(S, gp_scale_cp(gp_mul(wt[ad], Xp), ch[ad]))
                structs[("ch", x, y, z, Xn)] = S
# E1 family: p(x)_{+ i} p(y)_{+ j} (Db_i Wt_j) (D2 W)
for x in MOMB:
    for y in MOMB:
        for Wn, Wp in D2W.items():
            E = gp_zero()
            for i in range(2):
                for j in range(2):
                    co = cp_mul(MOMB[x][0][i], MOMB[y][0][j])
                    E = gp_add(E, gp_scale_cp(gp_mul(DbWt[(i, j)], Wp), co))
            structs[("E1", x, y, Wn)] = E
            # eps-contracted variant: eps^{ij} pattern p(x)_{+i}p(y)_{+j} Db^i Wt^j handled
            # by antisymmetrized combination of x,y already in span
print("dictionary size:", len(structs), flush=True)

for nm, agg in (("a", agg_a), ("b", agg_b)):
    R = gp_apply_subst(agg.get(target, gp_zero()), subst)
    t0 = time.time()
    sol = solve_structures(R, structs)
    if sol is None:
        print("term %s: no exact fit (%.0fs)" % (nm, time.time() - t0), flush=True)
    else:
        print("term %s fit (%.0fs):" % (nm, time.time() - t0), flush=True)
        for k, v in sorted(sol.items()):
            print("   %-28s  (%s, %s)" % (str(k), v[0], v[1]), flush=True)
