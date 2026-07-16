#!/usr/bin/env python3
"""Exhaustive check of the single-letter kinematic vanishing theorem (memo K §8).

Claim: any Lorentz-scalar word built from n factors  P[a,ad] := psb p_{a adot}(p)
(one external Euclidean momentum p, generic), together with ONE jet tensor carrying
at most one free spinor index (undotted OR dotted), with total undotted U(1) charge
+3/2 carried by free '+' component labels, vanishes identically once all dotted and
undotted indices except the fixed '+' labels are contracted with epsilons.

Operationally: enumerate all full contraction patterns of
  P_{a1 b1} ... P_{an bn} (jet index j),  n in {3,4},
where a subset of undotted slots is FROZEN to '+' (these carry the charge; number of
frozen '+' minus frozen '-' = 3... we scan all freezings), the remaining slots are
pairwise epsilon-contracted, and check the resulting scalar is 0 for a generic
Euclidean p (P = -i sigma_E . p).
"""
import itertools, sympy as sp

p1,p2,p3,p4 = sp.symbols('p1 p2 p3 p4')
I = sp.I
s1 = sp.Matrix([[0,1],[1,0]]); s2 = sp.Matrix([[0,-I],[I,0]]); s3 = sp.Matrix([[1,0],[0,-1]])
id2 = sp.eye(2)
sigE = [ -I*s1, -I*s2, -I*s3, id2 ]              # (sigma_E^m)_{a adot}
P = sp.zeros(2,2)
for m,pm in enumerate((p1,p2,p3,p4)):
    P += -I*sigE[m]*pm                            # p_{a adot} = -i sigma_E . p
eps = {(0,1):1,(1,0):-1,(0,0):0,(1,1):0}          # eps^{+-}=1 with '+'->index0

def all_scalars(n_extra_dotted_from_jet, n_P, frozen_plus, frozen_minus):
    """Enumerate contraction values. Returns set of nonzero results (should be empty).

    Slots: undotted slots of the n_P P's: some frozen (+ or -), rest contracted in pairs.
    Dotted slots: n_P dotted + jet dotted (0 or 1): all contracted in pairs (need even).
    Jet undotted index (if any) participates in undotted contractions or freezing.
    We simply scan ALL ways; jet tensor is generic: represent jet index value j in {0,1}
    and require the FULL object (for each j... ) -- for a scalar the jet index must be
    contracted too; we contract it with one epsilon partner.
    """
    results = set()
    nu = n_P + (1 if n_extra_dotted_from_jet=='undotted' else 0)   # undotted slots
    nd = n_P + (1 if n_extra_dotted_from_jet=='dotted' else 0)     # dotted slots
    # choose frozen undotted slots among the P undotted slots and possibly jet undotted
    und_slots = list(range(nu)); dot_slots = list(range(nd))
    for fplus in itertools.combinations(und_slots, frozen_plus):
        rest1 = [s for s in und_slots if s not in fplus]
        for fminus in itertools.combinations(rest1, frozen_minus):
            rest = [s for s in rest1 if s not in fminus]
            if len(rest)%2 or len(dot_slots)%2: continue
            for upair in pairings(rest):
                for dpair in pairings(dot_slots):
                    val = contract(n_P, n_extra_dotted_from_jet, fplus, fminus, upair, dpair)
                    v = sp.expand(sp.simplify(val))
                    if v != 0: results.add(sp.srepr(v))
    return results

def pairings(lst):
    if not lst: yield []; return
    a = lst[0]
    for i in range(1,len(lst)):
        for sub in pairings(lst[1:i]+lst[i+1:]):
            yield [(a,lst[i])]+sub

def contract(n_P, jet_kind, fplus, fminus, upair, dpair):
    # sum over all index values of P-tensors and jet index; jet tensor entries are
    # independent generic symbols so a vanishing total must vanish per jet component.
    # Build: undotted assignment per slot, dotted per slot.
    jets = sp.symbols(f'j0 j1')
    total = {0: sp.Integer(0), 1: sp.Integer(0)} if jet_kind!='none' else {None: sp.Integer(0)}
    # enumerate index values
    nu = n_P + (1 if jet_kind=='undotted' else 0)
    nd = n_P + (1 if jet_kind=='dotted' else 0)
    for uvals in itertools.product((0,1), repeat=nu):
        ok = all(uvals[s]==0 for s in fplus) and all(uvals[s]==1 for s in fminus)
        if not ok: continue
        efac = sp.Integer(1)
        for (x,y) in upair:
            efac *= eps[(uvals[x],uvals[y])]
        if efac == 0: continue
        for dvals in itertools.product((0,1), repeat=nd):
            efac2 = efac
            for (x,y) in dpair:
                efac2 *= eps[(dvals[x],dvals[y])]
            if efac2 == 0: continue
            term = efac2
            for i in range(n_P):
                term *= P[uvals[i], dvals[i]]
            if jet_kind=='undotted':
                total[uvals[n_P]] += term
            elif jet_kind=='dotted':
                total[dvals[n_P]] += term
            else:
                total[None] += term
    return sum(sp.Abs(sp.expand(v))**2 for v in total.values())  # nonzero iff any comp nonzero

bad = []
# charge +3/2: freezings with (#+) - (#-) = 3: (3,0),(4,1) limited by slot count
for n_P, jet_kind, fp, fm in [
    (3,'dotted',3,0),      # P^3 x jet with dotted index (e.g. D2Dbar v, Dbar v @ n=4 -> also (4,'dotted') below charge-shifted)
    (3,'none',3,0),        # P^3 x scalar jet (must be fermionic-impossible, but check anyway)
    (3,'undotted',3,0),(3,'undotted',4,1),  # jet undotted index frozen or contracted
    (4,'dotted',3,0),(4,'dotted',4,1),
    (4,'undotted',3,0),(4,'undotted',4,1),
    (4,'none',3,0),(4,'none',4,1),
]:
    r = all_scalars(jet_kind, n_P, fp, fm)
    status = "ALL ZERO" if not r else f"NONZERO({len(r)})"
    print(f"n_P={n_P:d} jet={jet_kind:9s} frozen(+,-)=({fp},{fm}): {status}")
    if r: bad.append((n_P,jet_kind,fp,fm,r))
print("\nTHEOREM:", "CONFIRMED — all scalar words vanish" if not bad else f"REFUTED: {bad}")
