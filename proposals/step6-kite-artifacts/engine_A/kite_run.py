"""Two-loop kite (ri / K4-e) run, SPEC sections 4-5.  (optimized)

Points: O=0, X1=1, X2=2, X3=3.
Lines (directed, momentum):
  L1: O->X1  l        L2: O->X2  p-l      L3: X1->X2  k
  L4: X1->X3 l-k      L5: X2->X3 p-l+k
External v-leg at X3, outgoing momentum p (momentum INTO X3 = -p).
Insertion term a: leg1(A)=Oalpha on L1, leg2(B)=Obeta on L2 ; term b swapped.
Prefactor bookkeeping: hbar^5 (props) x (-1/hbar)^3 (vertices; sign inside +-i/2)
 = hbar^2 ; g^3 ; numeric = prod of vertex coeffs (+-i/2) x engine signs.
Internally each line's p-matrix uses an ATOMIC symbol PLn_ab; expand to basis
l,k,p at the end via LINSUB.
"""
import sys, os, itertools, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *
from model import *

HERE = os.path.dirname(os.path.abspath(__file__))

# atomic line momenta; sign per end (into the point)
PMAT = {n: pmat({n: 1}) for n in ('L1', 'L2', 'L3', 'L4', 'L5')}
PMATN = {n: pmat_neg(PMAT[n]) for n in PMAT}
M_EXT = pmat({'p': -1})

# expansion of atomic line momenta in basis l,k,p
LINSUB = {
    'PL1': {'Pl': 1},
    'PL2': {'Pp': 1, 'Pl': -1},
    'PL3': {'Pk': 1},
    'PL4': {'Pl': 1, 'Pk': -1},
    'PL5': {'Pp': 1, 'Pl': -1, 'Pk': 1},
}

def cp_expand_lines(cp):
    out = {}
    for mono, c in cp.items():
        terms = [((), c)]
        for s in mono:
            pref = s.split("_")[0]
            if pref in LINSUB:
                tail = "_" + s.split("_")[1]
                reps = [((b + tail,), (Fr(co), Fr(0))) for b, co in LINSUB[pref].items()]
            else:
                reps = [((s,), CONE)]
            new = []
            for m0, c0 in terms:
                for mr, cr in reps:
                    new.append((tuple(sorted(m0 + mr)), cmul(c0, cr)))
            terms = new
        for m0, c0 in terms:
            v = cadd(out.get(m0, CZERO), c0)
            if ciszero(v): out.pop(m0, None)
            else: out[m0] = v
    return {m: v for m, v in out.items() if not ciszero(v)}

def gp_expand_lines(A):
    R = {}
    for m, cp in A.items():
        r = cp_expand_lines(cp)
        if r: R[m] = r
    return R

VLEGS = {1: ['L1', 'L3', 'L4'], 2: ['L2', 'L3', 'L5'], 3: ['L4', 'L5', 'EXT']}
COLORNAME = {'L1': 'A', 'L2': 'B', 'L3': 'm', 'L4': 's1', 'L5': 's2', 'EXT': 'G'}
XI_V = 18
V_EXT_POLY = ext_superfield(3, "v", XI_V, 0)

# line block cache (per process)
_blk = {}

def blk(linename, ptE, ptL, wE, wL, ME, ML):
    key = (linename, str(wE), str(wL))
    if key in _blk: return _blk[key]
    d = delta4_pair(ptE, ptL)
    r = apply_word(d, wL[0], wL[1], ptL, ML)
    r = apply_word(r, wE[0], wE[1], ptE, ME)
    _blk[key] = r
    return r

_ext_cache = {}

def ext_block(w):
    key = str(w)
    if key not in _ext_cache:
        _ext_cache[key] = apply_word(V_EXT_POLY, w[0], w[1], 3, M_EXT)
    return _ext_cache[key]

def eval_kite(term, chis, perms, idxs):
    w_leg1, w_leg2 = (W_OALPHA, W_OBETA) if term == 'a' else (W_OBETA, W_OALPHA)
    words = {}
    pars = {0: word_parity(w_leg1), 1: word_parity(w_leg2)}
    slot_fid = {}
    ctris = []
    fid = 2
    extw = None
    ext_fid = None
    for v in (1, 2, 3):
        Ew, Cw = vertex_realizations(chis[v - 1])[idxs[v - 1]]
        legE, legC, legU = perms[v]
        wmap = {legE: Ew, legC: Cw, legU: W_ID}
        for leg in (legE, legC, legU):
            w = wmap[leg]
            if leg == 'EXT':
                extw = w
                ext_fid = fid
                pars[fid] = word_parity(w)
            else:
                slot_fid[(v, leg)] = fid
                words[fid] = w
                pars[fid] = word_parity(w)
            fid += 1
        ctris.append((COLORNAME[legC], COLORNAME[legU], COLORNAME[legE]))
    f_L1 = slot_fid[(1, 'L1')]; f_L3a = slot_fid[(1, 'L3')]; f_L3b = slot_fid[(2, 'L3')]
    f_L4a = slot_fid[(1, 'L4')]; f_L4b = slot_fid[(3, 'L4')]
    f_L2 = slot_fid[(2, 'L2')]; f_L5a = slot_fid[(2, 'L5')]; f_L5b = slot_fid[(3, 'L5')]
    tgt = [0, f_L1, f_L3a, f_L3b, f_L4a, f_L4b, 1, f_L2, f_L5a, f_L5b, ext_fid]
    src_ids = sorted(pars)
    sign = koszul_sign(src_ids, pars, tgt)
    kA = (term, str(words[f_L1]), str(words[f_L3a]), str(words[f_L3b]),
          str(words[f_L4a]), str(words[f_L4b]))
    A = _Acache.get(kA, "miss")
    if A == "miss":
        g1 = blk('L1', 0, 1, w_leg1, words[f_L1], PMATN['L1'], PMAT['L1'])
        g3 = blk('L3', 1, 2, words[f_L3a], words[f_L3b], PMATN['L3'], PMAT['L3'])
        g4 = blk('L4', 1, 3, words[f_L4a], words[f_L4b], PMATN['L4'], PMAT['L4'])
        A = gp_mul(gp_mul(g1, g3), g4)
        if A: A = berezin(A, 1)
        _Acache[kA] = A
    if not A:
        return None, {}
    kB = (term, str(words[f_L2]), str(words[f_L5a]), str(words[f_L5b]))
    B = _Bcache.get(kB, "miss")
    if B == "miss":
        g2 = blk('L2', 0, 2, w_leg2, words[f_L2], PMATN['L2'], PMAT['L2'])
        g5 = blk('L5', 2, 3, words[f_L5a], words[f_L5b], PMATN['L5'], PMAT['L5'])
        B = gp_mul(g2, g5)
        _Bcache[kB] = B
    if not B:
        return None, {}
    R = gp_mul(A, B)
    if not R: return None, {}
    R = berezin(R, 2)
    if not R: return None, {}
    R = gp_mul(R, ext_block(extw))
    if not R: return None, {}
    R = berezin(R, 3)
    if not R: return None, {}
    if sign < 0:
        R = gp_scale(R, (Fr(-1), Fr(0)))
    pref = CONE
    for chi in chis:
        pref = cmul(pref, VERTEX_COEFF[chi])
    csign, canon = color_canon(ctris)
    if csign < 0: pref = cneg(pref)
    return canon, gp_scale(R, pref)

_Acache = {}
_Bcache = {}

def run_sector(args):
    term, chis = args
    out = {}
    t0 = time.time()
    for p1 in itertools.permutations(VLEGS[1]):
        for p2 in itertools.permutations(VLEGS[2]):
            for p3 in itertools.permutations(VLEGS[3]):
                perms = {1: p1, 2: p2, 3: p3}
                tot = gp_zero()
                canon0 = None
                for idxs in itertools.product(range(2), repeat=3):
                    canon, R = eval_kite(term, chis, perms, idxs)
                    if canon is not None and R:
                        canon0 = canon
                        tot = gp_add(tot, R)
                if tot:
                    permdesc = "X1(E%s,C%s,U%s)|X2(E%s,C%s,U%s)|X3(E%s,C%s,U%s)" % (p1 + p2 + p3)
                    out[(term, "".join(chis), permdesc)] = (canon0, gp_expand_lines(tot))
    return out, term, "".join(chis), time.time() - t0

if __name__ == "__main__":
    from multiprocessing import Pool
    jobs = [(term, chis) for term in ('a', 'b')
            for chis in itertools.product('+-', repeat=3)]
    results = {}
    t0 = time.time()
    with Pool(4) as pool:
        for out, term, ck, dt in pool.imap_unordered(run_sector, jobs):
            results.update(out)
            print("sector term=%s chi=%s done in %.0fs (nonzero perms: %d), total elapsed %.0fs"
                  % (term, ck, dt, len(out), time.time() - t0), flush=True)
    with open(os.path.join(HERE, "kite_raw.pkl"), "wb") as f:
        pickle.dump(results, f)
    print("saved", len(results), "nonzero (term,chi,perm) sectors")
