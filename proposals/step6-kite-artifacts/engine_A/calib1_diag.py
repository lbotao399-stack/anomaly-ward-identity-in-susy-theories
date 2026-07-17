"""Level-1 diagnosis: full bilinear jet decomposition of the term-a total."""
import sys, os, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *
from model import *
from bilinear import build_basis, decompose_bilinear, XI1, XI2
from calib1 import run_term, M_p, M_q

def cpn(cp):
    return cp_str(cp)

if __name__ == "__main__":
    agg_a, per_a = run_term('a')
    target_color = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]
    basisA = build_basis(["wt0", "wt1"], M_q, XI1, 1)     # jets of Wt_ad(q) at th0
    basisB = build_basis(["wp", "wm"], M_p, XI2, 1)       # jets of W^a(p) at th0
    print("== per-assignment bilinear jet rows (term a) ==")
    for (asg1, asg2), (canon, tot) in sorted(per_a.items()):
        print("--- assignment Y1:%s Y2:%s   color %s" % (asg1, asg2, color_str(canon)))
        if not tot:
            print("    ZERO")
            continue
        rows, resid = decompose_bilinear(tot, basisA, basisB, ["wt0", "wt1"], ["wp", "wm"])
        assert not resid
        for tht, ka, kb, cw in rows:
            t0 = "*".join({0: "th0+", 1: "th0-", 2: "tb0_1", 3: "tb0_2"}[g] for g in tht) or "1"
            print("    theta0=%s  [%s %s] x [%s %s]  coeff= %s"
                  % (t0, ka[0], ka[1], kb[0], kb[1], cpn(cw)))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "calib1_agg.pkl"), "wb") as f:
        pickle.dump((agg_a, per_a), f)
