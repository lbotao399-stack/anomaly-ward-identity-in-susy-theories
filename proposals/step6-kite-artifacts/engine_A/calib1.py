"""Calibration Level 1: locked one-loop WW seed (audits/step5-canonical-superfield-ww-seed.md).

Triangle O(th0) - Y1(th1) - Y2(th2).
Lines: T1: O->Y1 mom r0=k ; T2: Y1->Y2 mom r1=k+q ; T3: Y2->O mom r2=k+p+q.
Y1 antichiral (chi=-), E-slot external letter Wt_ad(q).
Y2 chiral (chi=+), E-slot external letter W^a(p); seed's X := D+ W_+(p).
Insertion term a: leg1(A)=Oalpha on T1, leg2(B)=Obeta on T3.
Insertion term b: leg1(A)=Obeta on T1, leg2(B)=Oalpha on T3.
Prefactors: hbar^3 (props) * hbar^-2 (2 vertices) = hbar^1 ; g^2 ; numeric = vertex
coeffs (-i/2)(+i/2) = +1/4 times word/Koszul/color signs (engine-generated).
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *
from model import *

XI1, XI2 = 16, 17

# momentum matrices
M_r0_inO = pmat({'k': -1})
M_r0_inY1 = pmat({'k': 1})
M_r1_inY1 = pmat({'k': -1, 'q': -1})
M_r1_inY2 = pmat({'k': 1, 'q': 1})
M_r2_inY2 = pmat({'k': -1, 'p': -1, 'q': -1})
M_r2_inO = pmat({'k': 1, 'p': 1, 'q': 1})
M_p = pmat({'p': 1})
M_q = pmat({'q': 1})

def run_term(term):
    """returns dict: canonical color -> GPoly total, and per-assignment results."""
    if term == 'a':
        w_leg1, w_leg2 = W_OALPHA, W_OBETA
    else:
        w_leg1, w_leg2 = W_OBETA, W_OALPHA
    per_assign = {}
    for asg1 in ('C_T1', 'C_T2'):        # Y1: C-slot on T1 or T2 (U on the other)
        for asg2 in ('C_T2', 'C_T3'):    # Y2: C-slot on T2 or T3
            total = gp_zero()
            colkey = None
            for ad in range(2):          # Y1 contracted dotted index
                reals1 = vertex_realizations('-')[ad]
                Cw1 = reals1[1]
                wt_ext = ext_superfield(1, "wt%d" % ad, XI1, 1)
                for a in range(2):       # Y2 contracted undotted index
                    reals2 = vertex_realizations('+')[a]
                    Cw2 = reals2[1]
                    wname = "wp" if a == 0 else "wm"   # W^+ , W^-
                    w_ext = ext_superfield(2, wname, XI2, 1)
                    # factors in source order
                    f0 = Factor(0, word=w_leg1, pt=0)
                    f1 = Factor(1, word=w_leg2, pt=0)
                    f2 = Factor(2, ext_poly=wt_ext, parity=1)      # Wt_ad odd
                    f3 = Factor(3, word=Cw1, pt=1)                 # (Db^ad v^C)
                    f4 = Factor(4, word=W_ID, pt=1)                # v^U
                    f5 = Factor(5, ext_poly=w_ext, parity=1)       # W^a odd
                    f6 = Factor(6, word=Cw2, pt=2)                 # (D_a v^C)
                    f7 = Factor(7, word=W_ID, pt=2)
                    facs = [f0, f1, f2, f3, f4, f5, f6, f7]
                    # slot->line
                    y1_on_T1 = 3 if asg1 == 'C_T1' else 4
                    y1_on_T2 = 4 if asg1 == 'C_T1' else 3
                    y2_on_T2 = 6 if asg2 == 'C_T2' else 7
                    y2_on_T3 = 7 if asg2 == 'C_T2' else 6
                    lines = [
                        (0, y1_on_T1, M_r0_inO, M_r0_inY1, "-r0", "+r0"),
                        (y1_on_T2, y2_on_T2, M_r1_inY1, M_r1_inY2, "-r1", "+r1"),
                        (1, y2_on_T3, M_r2_inO, M_r2_inY2, "+r2", "-r2"),
                    ]
                    R = eval_contraction(facs, lines, (1, 2),
                                         line_key_extra="L1t%s%s%s%d%d" % (term, asg1, asg2, ad, a))
                    total = gp_add(total, R)
            # color word for this assignment (indep of ad,a)
            c1 = ('A' if asg1 == 'C_T1' else 'm',   # C1
                  'm' if asg1 == 'C_T1' else 'A',   # U1
                  'D')
            c2 = ('m' if asg2 == 'C_T2' else 'B',
                  'B' if asg2 == 'C_T2' else 'm',
                  'E')
            csign, canon = color_canon([c1, c2])
            # vertex coefficients: chi- at Y1: -i/2 ; chi+ at Y2: +i/2 -> product 1/4
            pref = cmul((Fr(0), Fr(-1, 2)), (Fr(0), Fr(1, 2)))
            if csign < 0: pref = cneg(pref)
            total = gp_scale(total, pref)
            per_assign[(asg1, asg2)] = (canon, total)
    # aggregate by canonical color
    agg = {}
    for k, (canon, tot) in per_assign.items():
        agg[canon] = gp_add(agg.get(canon, gp_zero()), tot)
    return agg, per_assign

# ---------------- predicted seed structures ----------------

def chain_poly(Mi, Mbar, Mj):
    """Mchain_{+}{}^{ad} = [Mi Mbar Mj eps]_{+}{}^{ad}: returns [CP, CP] indexed by ad."""
    out = []
    for adot in range(2):
        e = {}
        for bd in range(2):
            for gam in range(2):
                for dd in range(2):
                    s = EPS_UP.get((dd, adot))
                    if s is None: continue
                    t = cp_mul(Mi[0][bd], cp_mul(Mbar[bd][gam], Mj[gam][dd]))
                    e = cp_add(e, cp_scale(t, (s, Fr(0))))
        out.append(e)
    return out

def build_letter_jets():
    """Wtjet_ad(th0) (identity word) and Xjet = D+ W_+ = -D+ W^-(p) at th0."""
    wt = [ext_superfield(0, "wt%d" % ad, XI1, 1) for ad in range(2)]
    wm = ext_superfield(0, "wm", XI2, 1)
    X = apply_word(wm, (Fr(-1), Fr(0)), [('D', 0)], 0, M_p)
    return wt, X

def structure(Mi, Mj):
    """S_ij = sum_ad chain_{+}^{ad} * Wtjet_ad * Xjet  (product order Wt X)."""
    wt, X = build_letter_jets()
    ch = chain_poly(Mi, pmat_bar(M_p), Mj)
    S = gp_zero()
    for adot in range(2):
        S = gp_add(S, gp_scale_cp(gp_mul(wt[adot], X), ch[adot]))
    return S

MOM = {0: pmat({'k': 1}), 1: pmat({'k': 1, 'q': 1}), 2: pmat({'k': 1, 'p': 1, 'q': 1})}

def sym_solve_structures(R, structs):
    """solve R = sum c_s structs[s] exactly; returns dict or None."""
    import sympy as sp
    keys = sorted(set(R) | set().union(*[set(s) for s in structs.values()]) if structs else set(R))
    unks = {name: sp.Symbol("z_%s" % str(name).replace(" ", ""), complex=True)
            for name in structs}
    eqs = []
    allm = set(R)
    for s in structs.values(): allm |= set(s)
    def cp2sp(cp):
        e = 0
        for mono, c in cp.items():
            t = sp.Rational(c[0]) + sp.I * sp.Rational(c[1])
            for s in mono: t *= sp.Symbol(s)
            e += t
        return sp.expand(e)
    for m in allm:
        lhs = cp2sp(R.get(m, {}))
        rhs = 0
        for name, s in structs.items():
            rhs += unks[name] * cp2sp(s.get(m, {}))
        eqs.append(sp.expand(lhs - rhs))
    # collect coefficients of every commuting monomial
    syms = set()
    for e in eqs: syms |= e.free_symbols
    syms -= set(unks.values())
    polyeqs = []
    for e in eqs:
        p = sp.Poly(e, *sorted(syms, key=str)) if syms else None
        if p is None:
            polyeqs.append(e)
        else:
            polyeqs.extend(p.coeffs())
    sol = sp.linsolve(polyeqs, list(unks.values()))
    if not sol: return None
    vals = list(sol)[0]
    out = {}
    for (name, u), v in zip(unks.items(), vals):
        v = sp.nsimplify(sp.expand(v))
        if v != 0: out[name] = v
    # verify no free parameters
    for v in out.values():
        if v.free_symbols: return None
    return out

if __name__ == "__main__":
    import sympy as sp
    print("=== Level 1: term a ===")
    agg_a, per_a = run_term('a')
    print("color sectors:", [color_str(k) for k in agg_a])
    target_color = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]
    R = agg_a.get(target_color, gp_zero())
    others = {k: v for k, v in agg_a.items() if k != target_color and v}
    print("nonzero non-target color sectors:", [color_str(k) for k in others])

    # predicted: (hbar g^2/2)*z * S(L1,L2) with L1=r0+r1, L2=r1+r2
    ML1 = pmat({'k': 2, 'q': 1})
    ML2 = pmat({'k': 2, 'p': 1, 'q': 2})
    S_L1L2 = structure(ML1, ML2)
    sol = sym_solve_structures(R, {"S": S_L1L2})
    print("total_a = z * [p(L1) pbar(p) p(L2)]_{+}^{ad} Wt_ad X  with z =",
          sol["S"] if sol else "NO MATCH")
    print("  (seed requires hbar g^2/2 * T-word; T-word = -i * p pbar p word,")
    print("   so exact seed match means z = (1/2)*(-i) = -i/2 ; engine hbar,g powers: hbar^1 g^2)")

    # per-assignment endpoint table
    print()
    print("=== 8-row endpoint table (terms a=placement A, b=placement B) ===")
    for term in ('a', 'b'):
        agg, per = run_term(term)
        for (asg1, asg2), (canon, tot) in sorted(per.items()):
            structs = {}
            for i in range(3):
                for j in range(3):
                    structs[(i, j)] = structure(MOM[i], MOM[j])
            sol = sym_solve_structures(tot, structs)
            if sol is None:
                print(term, asg1, asg2, color_str(canon), "-> NOT in r_i pbar(p) r_j span")
            else:
                pretty = ", ".join("(r%d,r%d): %s" % (k[0], k[1], v) for k, v in sorted(sol.items()))
                print(term, asg1, asg2, color_str(canon), "->", pretty if pretty else "0")
