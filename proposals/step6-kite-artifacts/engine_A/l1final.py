"""Level-1 gate: compare engine totals to seed structure ON THE CONSTRAINED
letter subspace (W chiral, Wt antichiral)."""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import structure, MOM, M_p, M_q
from constraints import constraint_subst, gp_apply_subst
from util_solve import solve_structures
import pickle

XI1, XI2 = 16, 17
agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]

# constraints: Wt_ad antichiral with momentum q ; W^a chiral with momentum p
subst = {}
subst.update(constraint_subst("wt0", M_q, "antichiral", XI1))
subst.update(constraint_subst("wt1", M_q, "antichiral", XI1))
subst.update(constraint_subst("wp", M_p, "chiral", XI2))
subst.update(constraint_subst("wm", M_p, "chiral", XI2))
print("substitution entries:", len(subst))

ML1 = pmat({'k': 2, 'q': 1}); ML2 = pmat({'k': 2, 'p': 1, 'q': 2})
Sc = gp_apply_subst(structure(ML1, ML2), subst)

for nm, agg in (("a", agg_a), ("b", agg_b)):
    R = gp_apply_subst(agg.get(target, gp_zero()), subst)
    sol = solve_structures(R, {"S": Sc})
    print("term %s: constrained total == z*S(L1,L2)?  z =" % nm, sol)

# per-assignment 8-row table on constrained subspace
structs = {}
for i in range(3):
    for j in range(3):
        structs[("r%d" % i, "r%d" % j)] = gp_apply_subst(structure(MOM[i], MOM[j]), subst)
print("\n8-row endpoint table (constrained):")
for term, per in (("a", per_a), ("b", per_b)):
    for (asg1, asg2), (canon, tot) in sorted(per.items()):
        totc = gp_apply_subst(tot, subst)
        sol = solve_structures(totc, structs)
        if sol is None:
            print("  term %s Y1:%s Y2:%s -> NOT in span" % (term, asg1, asg2))
        else:
            pretty = ", ".join("%s.%s: (%s,%s)" % (k[0], k[1], v[0], v[1]) for k, v in sorted(sol.items()))
            print("  term %s Y1:%s Y2:%s %s -> %s" % (term, asg1, asg2, color_str(canon), pretty))
