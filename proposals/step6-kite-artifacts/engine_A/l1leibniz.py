"""Check: R_a + R_b = D_-^{(theta0, p(P))} T,  T = triangle with K+ on both legs."""
from fractions import Fraction as Fr
from galg import *
from model import *
import calib1
from calib1 import M_r0_inO, M_r0_inY1, M_r1_inY1, M_r1_inY2, M_r2_inY2, M_r2_inO
import pickle

XI1, XI2 = 16, 17
W_KP = ((Fr(-1, 2), Fr(0)), [('D', 0), ('Db', 0), ('Db', 1), ('D', 0)])  # K+ = -1/4 D+ Db^2 D+

def run(wleg1, wleg2):
    per = {}
    for asg1 in ('C_T1', 'C_T2'):
        for asg2 in ('C_T2', 'C_T3'):
            total = gp_zero()
            for ad in range(2):
                Cw1 = vertex_realizations('-')[ad][1]
                wt_ext = ext_superfield(1, "wt%d" % ad, XI1, 1)
                for a in range(2):
                    Cw2 = vertex_realizations('+')[a][1]
                    w_ext = ext_superfield(2, "wp" if a == 0 else "wm", XI2, 1)
                    f0 = Factor(0, word=wleg1, pt=0)
                    f1 = Factor(1, word=wleg2, pt=0)
                    f2 = Factor(2, ext_poly=wt_ext, parity=1)
                    f3 = Factor(3, word=Cw1, pt=1)
                    f4 = Factor(4, word=W_ID, pt=1)
                    f5 = Factor(5, ext_poly=w_ext, parity=1)
                    f6 = Factor(6, word=Cw2, pt=2)
                    f7 = Factor(7, word=W_ID, pt=2)
                    facs = [f0, f1, f2, f3, f4, f5, f6, f7]
                    y1_T1 = 3 if asg1 == 'C_T1' else 4
                    y1_T2 = 4 if asg1 == 'C_T1' else 3
                    y2_T2 = 6 if asg2 == 'C_T2' else 7
                    y2_T3 = 7 if asg2 == 'C_T2' else 6
                    lines = [
                        (0, y1_T1, M_r0_inO, M_r0_inY1, "-r0", "+r0"),
                        (y1_T2, y2_T2, M_r1_inY1, M_r1_inY2, "-r1", "+r1"),
                        (1, y2_T3, M_r2_inO, M_r2_inY2, "+r2", "-r2"),
                    ]
                    R = eval_contraction(facs, lines, (1, 2),
                                         line_key_extra="LB%s%s%s%d%d" % (str(wleg1), asg1, asg2, ad, a))
                    total = gp_add(total, R)
            c1 = ('A' if asg1 == 'C_T1' else 'm', 'm' if asg1 == 'C_T1' else 'A', 'D')
            c2 = ('m' if asg2 == 'C_T2' else 'B', 'B' if asg2 == 'C_T2' else 'm', 'E')
            csign, canon = color_canon([c1, c2])
            pref = cmul((Fr(0), Fr(-1, 2)), (Fr(0), Fr(1, 2)))
            if csign < 0: pref = cneg(pref)
            per[(asg1, asg2)] = (canon, gp_scale(total, pref))
    agg = {}
    for k, (canon, tot) in per.items():
        agg[canon] = gp_add(agg.get(canon, gp_zero()), tot)
    return agg

agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))
target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]

aggT = run(W_KP, W_KP)
T = aggT.get(target, gp_zero())
MP = pmat({'k': 0, 'p': 1, 'q': 1})   # P = p + q  (total incoming at O)
DT = apply_letter(T, ('D', 1, 0, MP))
LHS = gp_add(agg_a.get(target, gp_zero()), agg_b.get(target, gp_zero()))
print("R_a + R_b == D_-^{(0,P)} T :", gp_eq(LHS, DT))
print("R_a + R_b == -D_-^{(0,P)} T :", gp_eq(LHS, gp_scale(DT, (Fr(-1), Fr(0)))))
