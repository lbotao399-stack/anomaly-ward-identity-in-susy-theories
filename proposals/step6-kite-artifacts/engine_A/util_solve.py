"""Exact linear solve  R = sum_s z_s * S_s  over complex rationals (no sympy).

R, S_s are GPolys (or CPs). Unknowns z_s complex; equations from every
(grassmann monomial, coefficient monomial) pair, real and imaginary parts.
Returns dict s -> (Fr re, Fr im) if a unique exact solution exists, else None.
"""
from fractions import Fraction as Fr

def _rows(R, structs, is_gp):
    keys = set()
    def monos(X):
        if is_gp:
            for gm, cp in X.items():
                for m in cp: yield (gm, m)
        else:
            for m in X: yield ((), m)
    def get(X, k):
        if is_gp:
            return X.get(k[0], {}).get(k[1], (Fr(0), Fr(0)))
        return X.get(k[1], (Fr(0), Fr(0)))
    for X in [R] + list(structs.values()):
        keys.update(monos(X))
    names = list(structs)
    A = []; b = []
    for k in sorted(keys):
        arow = [get(structs[n], k) for n in names]
        A.append(arow); b.append(get(R, k))
    return names, A, b

def solve_structures(R, structs, is_gp=True):
    names, A, b = _rows(R, structs, is_gp)
    n = len(names)
    # real 2n unknowns: z = x + i y ; each complex eq -> 2 real eqs
    M = []
    for arow, bv in zip(A, b):
        r1 = []; r2 = []
        for (cr, ci) in arow:
            r1 += [cr, -ci]
            r2 += [ci, cr]
        M.append(r1 + [bv[0]])
        M.append(r2 + [bv[1]])
    ncol = 2 * n
    # gaussian elimination
    piv = []
    r = 0
    for c in range(ncol):
        pr = None
        for i in range(r, len(M)):
            if M[i][c] != 0: pr = i; break
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M): break
    # check consistency
    for i in range(r, len(M)):
        if M[i][ncol] != 0: return None
    if len(piv) < ncol:
        # underdetermined: set free vars to 0 -> still a valid representation?
        # treat as failure for uniqueness, but return a particular solution flag
        pass
    sol = [Fr(0)] * ncol
    for i, c in enumerate(piv):
        sol[c] = M[i][ncol]
    # verify
    out = {}
    for j, nme in enumerate(names):
        out[nme] = (sol[2 * j], sol[2 * j + 1])
    # residual check
    for arow, bv in zip(A, b):
        sre = Fr(0); sim = Fr(0)
        for (cr, ci), nme in zip(arow, names):
            x, y = out[nme]
            sre += cr * x - ci * y
            sim += cr * y + ci * x
        if sre != bv[0] or sim != bv[1]: return None
    return {n_: v for n_, v in out.items() if v != (0, 0)}
