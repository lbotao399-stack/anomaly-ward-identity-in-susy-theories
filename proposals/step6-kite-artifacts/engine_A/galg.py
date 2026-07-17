"""Engine A: explicit-generator Grassmann / D-algebra core.

Conventions (SPEC section 1, seed audit section 1, step-02a, step-01):
  - Undotted a in {+,-} encoded 0,1 ; dotted ad in {1.,2.} encoded 0,1.
  - eps^{+-}=1, eps_{+-}=-1 ; same numerics for dotted (eps^{12}=1, eps_{12}=-1).
  - Generators per superspace point i (points 0..3):
        gen id 4*i+0 : theta_i^+
        gen id 4*i+1 : theta_i^-
        gen id 4*i+2 : thetabar_i^{dot1}   (upper dotted index)
        gen id 4*i+3 : thetabar_i^{dot2}
    Extra odd tags: 16 = xi1 (odd external letter #1), 17 = xi2 (odd letter #2).
  - Monomials stored as ascending tuples of gen ids; coefficient = CP
    (commutative polynomial over Q(i) in string symbols).
  - theta^2 := theta^a theta_a = -2 th+ th-   (D^2 theta^2 | = -4)
  - thetabar^2 := tb_ad tb^ad = +2 tb1 tb2    (Db^2 tbar^2 | = -4)
  - delta4(theta) = theta^2 thetabar^2 = -4 th+ th- tb1 tb2 ; int d4th delta4 = 1.
  - D_a  = d/dtheta^a + P[a][bd] * tbar^bd          (P = pmat of momentum INTO the point)
  - Db_bd= d/dtbar^bd + theta^c * P[c][bd]
    => {D_a, Db_bd} = 2 P[a][bd],  P_{a bd}(q) = -i (sigma_E^m)_{a bd} q_m.
  - D^2 = 2 D_- D_+ ; Db^2 = 2 Db_1 Db_2  (both verified against anchors).
"""
from fractions import Fraction as Fr

# ---------------- complex rational ----------------
CZERO = (Fr(0), Fr(0))
CONE = (Fr(1), Fr(0))
CI = (Fr(0), Fr(1))

def cadd(x, y): return (x[0] + y[0], x[1] + y[1])
def cmul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def cneg(x): return (-x[0], -x[1])
def ciszero(x): return x[0] == 0 and x[1] == 0

# ---------------- commutative polynomial CP ----------------
# dict { tuple(sorted symbol strings, with repetition) : (Fr,Fr) }

def cp_zero(): return {}
def cp_const(c):
    if ciszero(c): return {}
    return {(): c}
def cp_sym(s, c=CONE): return {(s,): c}

def cp_add(A, B):
    R = dict(A)
    for m, c in B.items():
        v = cadd(R.get(m, CZERO), c)
        if ciszero(v): R.pop(m, None)
        else: R[m] = v
    return R

def cp_scale(A, c):
    if ciszero(c): return {}
    return {m: cmul(v, c) for m, v in A.items()}

def cp_mul(A, B):
    R = {}
    for ma, ca in A.items():
        for mb, cb in B.items():
            m = tuple(sorted(ma + mb))
            v = cadd(R.get(m, CZERO), cmul(ca, cb))
            if ciszero(v): R.pop(m, None)
            else: R[m] = v
    return R

def cp_eq(A, B):
    return cp_add(A, cp_scale(B, (Fr(-1), Fr(0)))) == {}

def cp_str(A, symmap=None):
    if not A: return "0"
    terms = []
    for m in sorted(A.keys()):
        c = A[m]
        parts = []
        re, im = c
        if im == 0: coefstr = str(re)
        elif re == 0:
            coefstr = ("i" if im == 1 else ("-i" if im == -1 else "(%s)*i" % im))
        else: coefstr = "(%s%s%si)" % (re, "+" if im >= 0 else "-", abs(im))
        parts.append(coefstr)
        for s in m:
            parts.append(symmap[s] if symmap and s in symmap else s)
        terms.append("*".join(parts))
    return " + ".join(terms)

# ---------------- Grassmann polynomial GP ----------------
# dict { tuple(ascending gen ids) : CP }

def gp_zero(): return {}
def gp_const(cp):
    if not cp: return {}
    return {(): dict(cp)}

def gp_add(A, B):
    R = dict(A)
    for m, c in B.items():
        v = cp_add(R.get(m, {}), c)
        if not v: R.pop(m, None)
        else: R[m] = v
    return R

def gp_scale_cp(A, cp):
    if not cp: return {}
    return {m: cp_mul(c, cp) for m, c in A.items()}

def gp_scale(A, c):
    if ciszero(c): return {}
    return {m: cp_scale(v, c) for m, v in A.items()}

def _merge_sign(ma, mb):
    """sign of sorting concatenation of two ascending disjoint tuples; None if overlap."""
    i = j = 0; inv = 0
    la, lb = len(ma), len(mb)
    while i < la and j < lb:
        if ma[i] == mb[j]: return None, None
        if ma[i] < mb[j]: i += 1
        else:
            inv += la - i
            j += 1
    merged = tuple(sorted(ma + mb))
    return merged, (-1) ** inv

def gp_mul(A, B):
    R = {}
    for ma, ca in A.items():
        for mb, cb in B.items():
            m, s = _merge_sign(ma, mb)
            if m is None: continue
            c = cp_mul(ca, cb)
            if s < 0: c = cp_scale(c, (Fr(-1), Fr(0)))
            v = cp_add(R.get(m, {}), c)
            if not v: R.pop(m, None)
            else: R[m] = v
    return R

def gp_deriv(A, g):
    """left derivative d/d(gen g)."""
    R = {}
    for m, c in A.items():
        if g in m:
            idx = m.index(g)
            nm = m[:idx] + m[idx+1:]
            cc = c if idx % 2 == 0 else cp_scale(c, (Fr(-1), Fr(0)))
            v = cp_add(R.get(nm, {}), cc)
            if not v: R.pop(nm, None)
            else: R[nm] = v
    return R

def gp_mulgen(A, g):
    """left multiplication by generator g."""
    R = {}
    for m, c in A.items():
        if g in m: continue
        cnt = sum(1 for x in m if x < g)
        nm = tuple(sorted(m + (g,)))
        cc = c if cnt % 2 == 0 else cp_scale(c, (Fr(-1), Fr(0)))
        v = cp_add(R.get(nm, {}), cc)
        if not v: R.pop(nm, None)
        else: R[nm] = v
    return R

def gp_eq(A, B):
    return gp_add(A, gp_scale(B, (Fr(-1), Fr(0)))) == {}

# ---------------- momentum matrices ----------------
# pmat entries: P[a][bd] = CP.  Basis momentum 'x' -> symbols 'Px_{a}{bd}'.

def pmat(combo):
    """combo: dict momname -> rational coefficient. Returns 2x2 of CP."""
    M = [[{}, {}], [{}, {}]]
    for a in range(2):
        for b in range(2):
            e = {}
            for name, co in combo.items():
                if co == 0: continue
                e = cp_add(e, cp_sym("P%s_%d%d" % (name, a, b), (Fr(co), Fr(0))))
            M[a][b] = e
    return M

def pmat_neg(M):
    return [[cp_scale(M[a][b], (Fr(-1), Fr(0))) for b in range(2)] for a in range(2)]

EPS_UP = {(0, 1): Fr(1), (1, 0): Fr(-1)}   # eps^{+-}=1 ; eps^{12}=1
EPS_DN = {(0, 1): Fr(-1), (1, 0): Fr(1)}   # eps_{+-}=-1

def pmat_bar(M):
    """Pbar^{ad a} = eps^{ad bd} eps^{a b} P_{b bd}; returns Mb[ad][a]."""
    Mb = [[{}, {}], [{}, {}]]
    for ad in range(2):
        for a in range(2):
            e = {}
            for bd in range(2):
                for b in range(2):
                    s1 = EPS_UP.get((ad, bd)); s2 = EPS_UP.get((a, b))
                    if s1 is None or s2 is None: continue
                    e = cp_add(e, cp_scale(M[b][bd], (s1 * s2, Fr(0))))
            Mb[ad][a] = e
    return Mb

# ---------------- D operators ----------------

def gen(pt, slot): return 4 * pt + slot

def apply_letter(A, letter):
    """letter = ('D', a, pt, M) or ('Db', bd, pt, M)."""
    kind, idx, pt, M = letter
    if kind == 'D':
        R = gp_deriv(A, gen(pt, idx))
        for bd in range(2):
            e = M[idx][bd]
            if e:
                R = gp_add(R, gp_scale_cp(gp_mulgen(A, gen(pt, 2 + bd)), e))
    else:
        R = gp_deriv(A, gen(pt, 2 + idx))
        for c in range(2):
            e = M[c][idx]
            if e:
                R = gp_add(R, gp_scale_cp(gp_mulgen(A, gen(pt, c)), e))
    return R

def apply_word(A, coeff, letters, pt, M):
    """letters in OPERATOR order (leftmost first); coeff complex rational."""
    R = A
    for L in reversed(letters):
        R = apply_letter(R, (L[0], L[1], pt, M))
    return gp_scale(R, coeff)

# words as (coeff, letters); letters ('D',a) / ('Db',bd)
W_D2 = ((Fr(2), Fr(0)), [('D', 1), ('D', 0)])            # D^2 = 2 D_- D_+
W_Db2 = ((Fr(2), Fr(0)), [('Db', 0), ('Db', 1)])         # Db^2 = 2 Db_1 Db_2

def word_concat(*ws):
    c = CONE; ls = []
    for co, le in ws:
        c = cmul(c, co); ls = ls + le
    return (c, ls)

# ---------------- deltas & Berezin ----------------

def delta4_single(pt):
    """delta^4(theta_pt) = -4 th+ th- tb1 tb2."""
    m = (gen(pt, 0), gen(pt, 1), gen(pt, 2), gen(pt, 3))
    return {m: cp_const((Fr(-4), Fr(0)))}

def delta4_pair(pi, pj):
    """delta^4(theta_pi - theta_pj)."""
    R = gp_const(cp_const((Fr(-4), Fr(0))))
    for slot in range(4):
        f = gp_add({(gen(pi, slot),): cp_const(CONE)},
                   {(gen(pj, slot),): cp_const((Fr(-1), Fr(0)))})
        R = gp_mul(R, f)
    return R

def berezin(A, pt):
    """int d^4 theta_pt ; normalized so int delta4 = 1 -> extract block * (-1/4)."""
    ids = {gen(pt, s) for s in range(4)}
    R = {}
    for m, c in A.items():
        present = [g for g in m if g in ids]
        if len(present) != 4: continue
        nm = tuple(g for g in m if g not in ids)
        # the 4 ids are contiguous ascending inside sorted m; block is even -> no sign
        cc = cp_scale(c, (Fr(-1, 4), Fr(0)))
        v = cp_add(R.get(nm, {}), cc)
        if not v: R.pop(nm, None)
        else: R[nm] = v
    return R

def scalar_part(A):
    return A.get((), {})

def theta_restrict(A):
    """set all theta = 0 (all points)."""
    return A.get((), {})
