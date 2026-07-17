"""Broad structure hunt for the Level-1 total."""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import chain_poly, M_p, M_q
from util_solve import solve_structures
import pickle

XI1, XI2 = 16, 17
agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
target = color_canon([('A', 'm', 'D'), ('B', 'E', 'm')])[1]
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]
Ra = agg_a.get(target, gp_zero())

MOMB = {'k': pmat({'k': 1}), 'q': pmat({'q': 1}), 'p': pmat({'p': 1})}

wt = [ext_superfield(0, "wt%d" % ad, XI1, 1) for ad in range(2)]
wpj = ext_superfield(0, "wp", XI2, 1)
wmj = ext_superfield(0, "wm", XI2, 1)
# X-letter candidates: D_a W^b at th0 (momentum p)
Xcand = {}
for a, an in ((0, "D+"), (1, "D-")):
    for wnm, wj in (("W^+", wpj), ("W^-", wmj)):
        Xcand["%s%s" % (an, wnm)] = apply_word(wj, CONE, [('D', a)], 0, M_p)
# also underived letters
Xcand["W^+"] = wpj
Xcand["W^-"] = wmj
# Wt-letter candidates: underived W̃_ad and D̄_bd W̃_ad
Wtcand = {}
for ad in range(2):
    Wtcand["Wt_%d" % (ad + 1)] = wt[ad]

structs = {}
for x in ('k', 'q', 'p'):
    for y in ('k', 'q', 'p'):
        for z in ('k', 'q', 'p'):
            ch = chain_poly(MOMB[x], pmat_bar(MOMB[y]), MOMB[z])
            for Xn, Xp in Xcand.items():
                if Xn in ("W^+", "W^-"):  # degree would need extra momenta; skip bare
                    continue
                # sum_ad ch[ad] * Wt_ad * X   and X * Wt order
                S1 = gp_zero(); S2 = gp_zero()
                for ad in range(2):
                    S1 = gp_add(S1, gp_scale_cp(gp_mul(wt[ad], Xp), ch[ad]))
                    S2 = gp_add(S2, gp_scale_cp(gp_mul(Xp, wt[ad]), ch[ad]))
                structs[("ch[%s,%s,%s]" % (x, y, z), Xn, "WtX")] = S1
                structs[("ch[%s,%s,%s]" % (x, y, z), Xn, "XWt")] = S2

print("structures:", len(structs))
sol = solve_structures(Ra, structs)
if sol is None:
    print("STILL NO MATCH in broad chain x letter-jet dictionary")
else:
    for k, v in sorted(sol.items()):
        print("  %-40s  %s + %s i" % (str(k), v[0], v[1]))
