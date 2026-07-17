"""Compare canonical bilinear rows of engine total R_a vs seed structure S."""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import structure, M_p, M_q
from bilinear import build_basis, decompose_bilinear, XI1, XI2
from util_solve import solve_structures
import pickle

agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]
Ra = agg_a.get(target, gp_zero())

ML1 = pmat({'k': 2, 'q': 1}); ML2 = pmat({'k': 2, 'p': 1, 'q': 2})
S = structure(ML1, ML2)

basisA = build_basis(["wt0", "wt1"], M_q, XI1, 1)
basisB = build_basis(["wp", "wm"], M_p, XI2, 1)

def show(name, X):
    rows, res = decompose_bilinear(X, basisA, basisB, ["wt0", "wt1"], ["wp", "wm"])
    assert not res
    print("== %s : %d rows" % (name, len(rows)))
    for t, ka, kb, cw in sorted(rows, key=lambda r: (r[0], r[1], r[2])):
        t0 = "*".join(str(g) for g in t) or "-"
        print("   th0=%-8s [%s %s]x[%s %s]   %s" % (t0, ka[0], ka[1], kb[0], kb[1], cp_str(cw)))
    return {(t, ka, kb): cw for t, ka, kb, cw in rows}

ra = show("R_a (engine total)", Ra)
rs = show("S (seed structure, unit coeff)", S)

# difference pattern: which keys of ra are absent in rs and vice versa
ka = set(ra); ks = set(rs)
print("\nkeys only in R_a:", len(ka - ks))
print("keys only in S:", len(ks - ka))
print("shared keys:", len(ka & ks))
# ratio test on shared keys
import itertools
for k in sorted(ka & ks)[:20]:
    print("  shared", k[1], k[2], " R:", cp_str(ra[k]), " | S:", cp_str(rs[k]))
