from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import run_term, structure, MOM
from util_solve import solve_structures
import pickle, time

t0 = time.time()
agg_a, per_a = run_term('a')
agg_b, per_b = run_term('b')
pickle.dump((agg_a, per_a, agg_b, per_b), open("calib1_agg.pkl", "wb"))
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]
Ra = agg_a.get(target, gp_zero())
Rb = agg_b.get(target, gp_zero())
print("non-target sectors a:", [color_str(k) for k, v in agg_a.items() if k != target and v], flush=True)
print("non-target sectors b:", [color_str(k) for k, v in agg_b.items() if k != target and v], flush=True)

ML1 = pmat({'k': 2, 'q': 1}); ML2 = pmat({'k': 2, 'p': 1, 'q': 2})
S = structure(ML1, ML2)
for nm, R in (("a", Ra), ("b", Rb)):
    sol = solve_structures(R, {"S": S})
    print("term %s: total == z*[p(L1) pbar(p) p(L2)]_{+}^{ad} Wt_ad X ; z =" % nm, sol, flush=True)

structs = {}
for i in range(3):
    for j in range(3):
        structs[("r%d" % i, "r%d" % j)] = structure(MOM[i], MOM[j])
print("\n8-row endpoint table (a = D- on leg A / b = D- on leg B):", flush=True)
for term, per in (("a", per_a), ("b", per_b)):
    for (asg1, asg2), (canon, tot) in sorted(per.items()):
        sol = solve_structures(tot, structs)
        pretty = None
        if sol is not None:
            pretty = ", ".join("%s%s: %s%s%si" % (k[0], k[1], v[0], "+" if v[1] >= 0 else "-", abs(v[1]))
                               for k, v in sorted(sol.items()))
        print("  term %s  Y1:%s Y2:%s  %s -> %s" % (term, asg1, asg2, color_str(canon), pretty), flush=True)
print("t=%.0fs" % (time.time() - t0), flush=True)
