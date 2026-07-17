"""Decompose kite raw results into jet rows, write JSON + summary, run Level-2 checks."""
import sys, os, json, pickle, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *
from model import *

HERE = os.path.dirname(os.path.abspath(__file__))
KITE = os.path.dirname(HERE)

M_JET = pmat({'p': -1})   # [engine convention] jet D-words at th0 use momentum INTO the
                          # output point = -p (external leg carries outgoing p)

SLOTN = {0: "th0+", 1: "th0-", 2: "tb0_1", 3: "tb0_2"}

def symname(s):
    if s.startswith("P") and "_" in s:
        mom = s[1:s.index("_")]
        ab = s[s.index("_") + 1:]
        a = {"0": "+", "1": "-"}[ab[0]]
        b = {"0": "1d", "1": "2d"}[ab[1]]
        return "p%s[%s,%s]" % (mom, a, b)
    return s

def cp_out(cp):
    return cp_str(cp, symmap=None if not cp else {s: symname(s) for m in cp for s in m})

def tht_out(tht):
    return "*".join(SLOTN[g] for g in tht) if tht else "1"

def load():
    with open(os.path.join(HERE, "kite_raw.pkl"), "rb") as f:
        return pickle.load(f)

def cp_subst_relabel(cp):
    """Pl -> Pp - Pl ; Pk -> -Pk ; Pp -> Pp  (entrywise, exact)."""
    out = {}
    for mono, c in cp.items():
        # expand each momentum symbol
        terms = [((), c)]
        for s in mono:
            new = []
            if s.startswith("Pl_"):
                tail = s[3:]
                reps = [(("Pp_" + tail,), CONE), (("Pl_" + tail,), (Fr(-1), Fr(0)))]
            elif s.startswith("Pk_"):
                reps = [((s,), (Fr(-1), Fr(0)))]
            else:
                reps = [((s,), CONE)]
            for m0, c0 in terms:
                for mr, cr in reps:
                    new.append((tuple(sorted(m0 + mr)), cmul(c0, cr)))
            terms = new
        for m0, c0 in terms:
            v = cadd(out.get(m0, CZERO), c0)
            if ciszero(v): out.pop(m0, None)
            else: out[m0] = v
    return {m: v for m, v in out.items() if not ciszero(v)}

def gp_subst_relabel(A):
    return {m: r for m, c in A.items() if (r := cp_subst_relabel(c))}

def color_swapAB(canon):
    sw = {'A': 'B', 'B': 'A', 's1': 's2', 's2': 's1'}
    tris = [tuple(sw.get(i, i) for i in t) for t in canon]
    return color_canon(tris)

if __name__ == "__main__":
    results = load()
    basis = build_jet_basis("v", M_JET, 18, 0)

    # ---------- per-sector jet rows ----------
    all_rows = []
    sector_jetrows = {}
    for (term, chikey, permdesc), (canon, tot) in sorted(results.items()):
        rows, resid = decompose_jets(tot, basis, ["v"])
        assert not resid, (term, chikey, permdesc)
        sector_jetrows[(term, chikey, permdesc)] = (canon, rows)
        for tht, jet, cw in rows:
            all_rows.append({
                "term": term,
                "chirality": chikey,
                "slotperm": permdesc,
                "coeff": "hbar^2 * g^3  (global prefactor; numeric factors inside numerator)",
                "color": color_str(canon),
                "numerator": cp_out(cw),
                "outjet": jet,
                "theta0": tht_out(tht),
            })
    with open(os.path.join(KITE, "engine_A_rows.json"), "w") as f:
        json.dump({
            "engine": "A (explicit 16-generator Grassmann polynomials)",
            "conventions": {
                "pX[a,ad]": "entries of p_{a ad}(X) = -i (sigma_E^m)_{a ad} X_m, X in {l,k,p}",
                "outjet": "covariant D-word acting on external v at theta_0, momentum -p into jet point",
                "theta0": "explicit theta_0 monomial multiplying the jet (1 = covariant row)",
                "denominators": "every row divided by D1..D5 = l^2 (p-l)^2 k^2 (l-k)^2 (p-l+k)^2",
                "loop_integrals": "mu^{4eps} int d^dl d^dk/(2pi)^{2d} NOT performed",
            },
            "rows": all_rows,
        }, f, indent=1)
    print("wrote engine_A_rows.json with", len(all_rows), "rows")

    # ---------- chi-sector survival ----------
    chis_alive = {}
    for (term, chikey, permdesc), (canon, tot) in results.items():
        chis_alive.setdefault((term, chikey), 0)
        chis_alive[(term, chikey)] += 1
    print("\nsurviving (term, chi) sectors (count of nonzero slotperms):")
    for term in ('a', 'b'):
        for chis in itertools.product('+-', repeat=3):
            ck = "".join(chis)
            print("  term %s chi %s : %d" % (term, ck, chis_alive.get((term, ck), 0)))

    # ---------- totals per color ----------
    totals = {}   # (term, colorcanon) -> GPoly
    for (term, chikey, permdesc), (canon, tot) in results.items():
        k = (term, canon)
        totals[k] = gp_add(totals.get(k, gp_zero()), tot)
    totals = {k: v for k, v in totals.items() if v}

    # ---------- Level 2a: relabeling / A<->B exchange ----------
    print("\nLevel 2 check: relabel (l->p-l, k->-k, X1<->X2 i.e. A<->B, s1<->s2): term a -> term b?")
    ok_all = True
    for (term, canon), tot in sorted(totals.items()):
        if term != 'a': continue
        sub = gp_subst_relabel(tot)
        csign, canon2 = color_swapAB(canon)
        target = totals.get(('b', canon2), gp_zero())
        if csign < 0: sub = gp_scale(sub, (Fr(-1), Fr(0)))
        same = gp_eq(sub, target)
        anti = gp_eq(sub, gp_scale(target, (Fr(-1), Fr(0))))
        print("  color %s -> %s : equal=%s  antiequal=%s" %
              (color_str(canon), color_str(canon2), same, anti))
        if not same: ok_all = False
    print("  RELABEL MAP a->b:", "EXACT" if ok_all else "NOT EXACT (see above)")

    # ---------- grand total & jet content ----------
    grand = {}
    for (term, canon), tot in totals.items():
        grand[canon] = gp_add(grand.get(canon, gp_zero()), tot)
    grand = {k: v for k, v in grand.items() if v}
    print("\nGrand total (a+b) color sectors:", [color_str(k) for k in grand])
    jetrows_total = {}
    for canon, tot in grand.items():
        rows, resid = decompose_jets(tot, basis, ["v"])
        assert not resid
        jetrows_total[canon] = rows
        print("color %s : %d jet rows" % (color_str(canon), len(rows)))
        for tht, jet, cw in rows:
            print("   theta0=%s outjet=%s  numerator=%s" % (tht_out(tht), jet, cp_out(cw)))

    with open(os.path.join(HERE, "kite_totals.pkl"), "wb") as f:
        pickle.dump((totals, grand, jetrows_total, sector_jetrows), f)
    print("\nsaved kite_totals.pkl")
