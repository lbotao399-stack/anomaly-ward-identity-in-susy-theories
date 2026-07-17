"""Evaluation-order invariance: the contraction value must not depend on the
bookkeeping order of factors (vertex blocks) or on the order line blocks are
multiplied. Rebuild one Level-1 contraction with permuted orders and compare.
"""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import (M_r0_inO, M_r0_inY1, M_r1_inY1, M_r1_inY2,
                    M_r2_inY2, M_r2_inO)

XI1, XI2 = 16, 17

def build(term_words, order, lineorder, asg1, asg2, ad, a):
    w_leg1, w_leg2 = term_words
    Cw1 = vertex_realizations('-')[ad][1]
    Cw2 = vertex_realizations('+')[a][1]
    wt_ext = ext_superfield(1, "wt%d" % ad, XI1, 1)
    w_ext = ext_superfield(2, "wp" if a == 0 else "wm", XI2, 1)
    # factor definitions keyed by name
    defs = {
        "I1": Factor(0, word=w_leg1, pt=0),
        "I2": Factor(1, word=w_leg2, pt=0),
        "Y1E": Factor(2, ext_poly=wt_ext, parity=1),
        "Y1C": Factor(3, word=Cw1, pt=1),
        "Y1U": Factor(4, word=W_ID, pt=1),
        "Y2E": Factor(5, ext_poly=w_ext, parity=1),
        "Y2C": Factor(6, word=Cw2, pt=2),
        "Y2U": Factor(7, word=W_ID, pt=2),
    }
    # renumber fids according to chosen source order
    facs = []
    for i, nm in enumerate(order):
        f = defs[nm]
        f.fid = i
        facs.append(f)
    name2fid = {nm: defs[nm].fid for nm in order}
    y1_T1 = "Y1C" if asg1 == 'C_T1' else "Y1U"
    y1_T2 = "Y1U" if asg1 == 'C_T1' else "Y1C"
    y2_T2 = "Y2C" if asg2 == 'C_T2' else "Y2U"
    y2_T3 = "Y2U" if asg2 == 'C_T2' else "Y2C"
    linedefs = {
        "T1": ("I1", y1_T1, M_r0_inO, M_r0_inY1),
        "T2": (y1_T2, y2_T2, M_r1_inY1, M_r1_inY2),
        "T3": ("I2", y2_T3, M_r2_inO, M_r2_inY2),
    }
    lines = []
    for ln in lineorder:
        n1, n2, Ma, Mb = linedefs[ln]
        f1, f2 = name2fid[n1], name2fid[n2]
        if f1 < f2:
            lines.append((f1, f2, Ma, Mb, "x", "y"))
        else:
            lines.append((f2, f1, Mb, Ma, "x", "y"))
    return eval_contraction(facs, lines, (1, 2))

BASE = ["I1", "I2", "Y1E", "Y1C", "Y1U", "Y2E", "Y2C", "Y2U"]
ALT1 = ["Y2E", "Y2C", "Y2U", "I1", "I2", "Y1E", "Y1C", "Y1U"]   # vertex blocks reordered
ALT2 = ["I2", "I1", "Y1E", "Y1C", "Y1U", "Y2E", "Y2C", "Y2U"]   # insertion legs swapped in order
LO1 = ["T1", "T2", "T3"]
LO2 = ["T3", "T1", "T2"]
LO3 = ["T2", "T3", "T1"]

ok = True
for asg1 in ('C_T1', 'C_T2'):
    for asg2 in ('C_T2', 'C_T3'):
        for ad in range(2):
            for a in range(2):
                vals = []
                for order in (BASE, ALT1, ALT2):
                    for lo in (LO1, LO2, LO3):
                        vals.append(build((W_OALPHA, W_OBETA), order, lo, asg1, asg2, ad, a))
                for v in vals[1:]:
                    if not gp_eq(v, vals[0]):
                        ok = False
                        print("ORDER DEPENDENCE at", asg1, asg2, ad, a)
print("order invariance:", "PASS" if ok else "FAIL")
