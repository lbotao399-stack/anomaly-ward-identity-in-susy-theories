"""Write engine_A_summary.md from kite_totals.pkl + calibration records."""
import sys, os, pickle, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *
from model import *
from util_solve import solve_structures
from finalize import cp_out, tht_out, symname

HERE = os.path.dirname(os.path.abspath(__file__))
KITE = os.path.dirname(HERE)

MOMB = {'l': pmat({'l': 1}), 'k': pmat({'k': 1}), 'p': pmat({'p': 1})}
MOMS = ['l', 'k', 'p']
EPS = {(0, 1): Fr(1), (1, 0): Fr(-1)}

def bracket(x, y):
    br = {}
    for a in range(2):
        for b in range(2):
            s = EPS.get((a, b))
            if s: br = cp_add(br, cp_scale(cp_mul(MOMB[x][0][a], MOMB[y][0][b]), (s, Fr(0))))
    return br

def inv2(x, y):
    A, Bb = MOMB[x], pmat_bar(MOMB[y])
    e = {}
    for a in range(2):
        for bd in range(2):
            e = cp_add(e, cp_mul(A[a][bd], Bb[bd][a]))
    return e

def chain(x, y, z):
    """[p(x) pbar(y) p(z)]_{+ cd} as [CP,CP]."""
    out = []
    Bb = pmat_bar(MOMB[y])
    for cd in range(2):
        e = {}
        for bd in range(2):
            for c in range(2):
                e = cp_add(e, cp_mul(MOMB[x][0][bd], cp_mul(Bb[bd][c], MOMB[z][c][cd])))
        out.append(e)
    return out

def fit_dotted_family(N):
    """N: dict bd -> CP (numerators of a jet family with free lower dotted index bd).
    Fit against chains, p*inv2, bracket*p."""
    structs = {}
    for x in MOMS:
        for y in MOMS:
            for z in MOMS:
                ch = chain(x, y, z)
                structs[("ch[%s|%s|%s]" % (x, y, z))] = {(0,): ch[0], (1,): ch[1]}
    for x in MOMS:
        for yi, y in enumerate(MOMS):
            for zi, z in enumerate(MOMS):
                if zi < yi: continue
                iv = inv2(y, z)
                structs["p(%s)tr(%s.%s)" % (x, y, z)] = {
                    (0,): cp_mul(MOMB[x][0][0], iv), (1,): cp_mul(MOMB[x][0][1], iv)}
    for xi, x in enumerate(MOMS):
        for yi, y in enumerate(MOMS):
            if yi <= xi: continue
            br = bracket(x, y)
            for z in MOMS:
                structs["<%s%s>p(%s)" % (x, y, z)] = {
                    (0,): cp_mul(br, MOMB[z][0][0]), (1,): cp_mul(br, MOMB[z][0][1])}
    R = {(0,): N.get(0, {}), (1,): N.get(1, {})}
    R = {k: v for k, v in R.items() if v}
    return solve_structures(R, structs)

def fit_scalar(Ncp):
    structs = {}
    for xi, x in enumerate(MOMS):
        for yi, y in enumerate(MOMS):
            if yi < xi: continue
            structs["tr(%s.%s)" % (x, y)] = {(): inv2(x, y)}
        for yi, y in enumerate(MOMS):
            if yi <= xi: continue
            structs["<%s%s>" % (x, y)] = {(): bracket(x, y)}
    # quartics
    names = list(structs)
    for n1 in names:
        for n2 in names:
            if n1 <= n2:
                structs[n1 + "*" + n2] = {(): cp_mul(structs[n1][()], structs[n2][()])}
    return solve_structures({(): Ncp}, structs)

def coeffstr(v):
    re, im = v
    if im == 0: return str(re)
    if re == 0: return "%s*i" % im
    return "(%s%+s i)" % (re, im)

if __name__ == "__main__":
    with open(os.path.join(HERE, "kite_totals.pkl"), "rb") as f:
        totals, grand, jetrows_total, sector_jetrows = pickle.load(f)

    lines = []
    A = lines.append
    A("# Engine A - two-loop kite (ri) supergraph: reduced D-algebra output\n")
    A("Engine: explicit 16-generator Grassmann polynomial engine (galg.py/model.py),")
    A("momentum-space D-operators, Berezin = coefficient extraction.")
    A("Conventions: SPEC section 1 (seed audit section 1); Level-0 anchors all PASS.\n")
    A("Global prefactor of every row: `hbar^2 g^3` (hbar^5 from 5 propagators x")
    A("(-1/hbar)^3 from 3 vertices; vertex numeric factors (+-i/2) and the insertion")
    A("leg coefficients -1/8, -1/4 are inside the row numerators). Rows divide by")
    A("D1..D5 = l^2 (p-l)^2 k^2 (l-k)^2 (p-l+k)^2 under mu^{4eps} int d^dl d^dk/(2pi)^{2d}.\n")

    A("## Surviving sectors\n")
    surv = {}
    for (term, chikey, permdesc), (canon, rows) in sector_jetrows.items():
        surv.setdefault((term, chikey), 0)
        surv[(term, chikey)] += 1
    for term in ('a', 'b'):
        for chis in itertools.product('+-', repeat=3):
            ck = "".join(chis)
            A("- term %s, chi=(%s): %d nonzero slot-assignments" % (term, ck, surv.get((term, ck), 0)))
    A("")

    A("## Grand total (a+b), jet rows per color word\n")
    for canon, rows in jetrows_total.items():
        A("### color %s\n" % color_str(canon))
        # group families
        fams = {}
        for tht, jet, cw in rows:
            fams.setdefault((tht, jet), {})
            fams[(tht, jet)] = cp_add(fams[(tht, jet)], cw)
        # dotted families
        done = set()
        for (tht, jet), cw in sorted(fams.items(), key=lambda x: (x[0][0], x[0][1])):
            if (tht, jet) in done: continue
            fam = None
            if jet.endswith("Db[1]v") or jet.endswith("Db[2]v"):
                base = jet.replace("Db[1]v", "Db[%d]v").replace("Db[2]v", "Db[%d]v")
                k0 = (tht, base % 1); k1 = (tht, base % 2)
                N = {}
                if k0 in fams: N[0] = fams[k0]
                if k1 in fams: N[1] = fams[k1]
                sol = fit_dotted_family(N)
                done.update([k0, k1])
                A("- theta0=%s, jet family %s (free dotted index):" % (tht_out(tht), base % 0 + "/[2]"))
                if sol:
                    for k, v in sorted(sol.items()):
                        A("    + %s * %s" % (coeffstr(v), k))
                else:
                    for b in (0, 1):
                        if b in N:
                            A("    [%d]: %s" % (b + 1, cp_out(N[b])))
            else:
                done.add((tht, jet))
                sol = fit_scalar(cw) if all(g < 16 for g in tht) else None
                A("- theta0=%s, outjet %s:" % (tht_out(tht), jet))
                if sol:
                    for k, v in sorted(sol.items()):
                        A("    + %s * %s" % (coeffstr(v), k))
                else:
                    A("    numerator = %s" % cp_out(cw))
        A("")
    with open(os.path.join(KITE, "engine_A_summary.md"), "w") as f:
        f.write("\n".join(lines))
    print("wrote engine_A_summary.md (%d lines)" % len(lines))
