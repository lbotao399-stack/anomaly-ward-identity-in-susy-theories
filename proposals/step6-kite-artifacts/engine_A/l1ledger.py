"""Ledger comparison with the seed's 8-row table.

For each (term, assignment): canonically decompose the constrained result;
extract the row family {([v wt_j], [D[+]v wm])} (the Wt_ad x D+W_+ sector,
since W_+ = -W^-), and fit that family against the same-family rows of the
nine seed chain structures S_ij = [p(r_i) pbar(p) p(r_j) eps]_{+}{}^{ad} Wt_ad X,
X = D+W_+ = -D+W^-.
Also fit the degree-2 sector against E2-sym structures.
"""
from fractions import Fraction as Fr
from galg import *
from model import *
from calib1 import structure, MOM, M_p, M_q
from constraints import constraint_subst, gp_apply_subst
from util_solve import solve_structures
from l1rows import bilinear_rows, subst   # reuses constrained basis machinery
import pickle, io, contextlib

agg_a, per_a, agg_b, per_b = pickle.load(open("calib1_agg.pkl", "rb"))

def rows_of(X):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rows = bilinear_rows(X, "x")
    return {(ka, kb): cw for t, ka, kb, cw in rows}

# seed chains, constrained + canonical rows
Srows = {}
for i in range(3):
    for j in range(3):
        Sc = gp_apply_subst(structure(MOM[i], MOM[j]), subst)
        Srows[(i, j)] = rows_of(Sc)

CHAINKEYS = [(("v", "wt0"), ("D[+]v", "wm")), (("v", "wt1"), ("D[+]v", "wm"))]

def family_fit(rows, keys, cand):
    """fit rows restricted to `keys` against candidate row-dicts restricted the same."""
    R = {}
    for n, k in enumerate(keys):
        if k in rows: R[(n,)] = rows[k]
    structs = {}
    for cname, crows in cand.items():
        s = {}
        for n, k in enumerate(keys):
            if k in crows: s[(n,)] = crows[k]
        if s: structs[cname] = s
    return solve_structures(R, structs)

print("Seed chain S_ij canonical row check (should be only the 2 chain keys):")
for ij, rr in sorted(Srows.items()):
    extra = [k for k in rr if k not in CHAINKEYS]
    print("  S%s: rows=%d extra-family rows=%d" % (ij, len(rr), len(extra)))

print("\n=== chain-sector ledger fit per assignment ===")
print("(seed table: term a rows -> (i,j) with i=Db endpoint (r0/r1), j=D endpoint (r1/r2),")
print(" expected mapping: Y1 C_T1->r0, C_T2->r1 ; Y2 C_T2->r1, C_T3->r2 ; all final signs +1)")
for term, per in (("a", per_a), ("b", per_b)):
    for (asg1, asg2), (canon, tot) in sorted(per.items()):
        rows = rows_of(gp_apply_subst(tot, subst))
        sol = family_fit(rows, CHAINKEYS, Srows)
        if sol is None:
            print("  term %s %s %s: chain family NOT in S_ij row span" % (term, asg1, asg2))
        else:
            pretty = ", ".join("S(r%d,r%d)=(%s,%s)" % (k[0], k[1], v[0], v[1])
                               for k, v in sorted(sol.items()))
            print("  term %s %s %s: %s" % (term, asg1, asg2, pretty))

print("\n=== total chain sector ===")
for nm, agg in (("a", agg_a), ("b", agg_b)):
    target = color_canon([('A', 'm', 'D'), ('B', 'm', 'E')])[1]
    rows = rows_of(gp_apply_subst(agg.get(target, gp_zero()), subst))
    sol = family_fit(rows, CHAINKEYS, Srows)
    print("  term %s total: %s" % (nm, sorted(sol.items()) if sol else "NOT in span"))
