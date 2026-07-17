#!/usr/bin/env python3
"""
Color factor of the tip-ri (kite / K4-e) graph, SPEC v1 SS4 topology.

Conventions (SPEC SS2 / seed audit SS3-4):
  [T_A, T_B] = i c_{AB}^C T_C ,   tr_kappa(T_A T_B) = kappa_{AB},
  c_{ABC} := c_{AB}^D kappa_{DC} totally antisymmetric,
  propagator carries kappa^{XY} (inverse of kappa_{AB}).

We realize su(N) by fundamental generators T_A with tr(T_A T_B) = (1/2) delta_AB
(su(2): T = sigma/2, su(3): T = lambda_GellMann/2), so kappa_{AB} = delta_AB/2
and c_{AB}^C = f_ABC (the standard real structure constants, f_ACD f_BCD = N delta_AB).

Checks:
 (1) every slot assignment's color word = (sign) x C3,   sign = eta * prod of 3 perm parities
 (2) C3^{AB}_G antisymmetric under A<->B
 (3) C3_{ABG} = (C2(adj)/2) c_{ABG};  su(N) fundamental-kappa: = N c_{ABG};
     delta-normalized identity f_{AMS1} f_{BMS2} f_{GS1S2} = (N/2) f_{ABG};
     C2(adj) = 2N (w.r.t. kappa = fundamental trace form)
 (J) Jacobi step: kappa^{MM'}(c_{AMS1}c_{BM'S2} - c_{AMS2}c_{BM'S1}) = c_{ABM} kappa^{MM'} c_{M'S1S2}
 (4) settlement F^{AB}_{DE} = kappa^{AU}kappa^{BV}kappa^{CC'}c_{UCD}c_{VC'E}:
     symmetry F^{AB}_{DE} = F^{BA}_{ED}; and C3^{AB}_G = kappa^{DD'}kappa^{EE'} F^{AB}_{DE} c_{GD'E'}.
"""
import itertools
import numpy as np

TOL = 1e-11


def su_fundamental_generators(N):
    """Generalized Gell-Mann matrices / 2 : tr(T_a T_b) = delta_ab/2."""
    gens = []
    # off-diagonal symmetric and antisymmetric
    for i in range(N):
        for j in range(i + 1, N):
            S = np.zeros((N, N), dtype=complex); S[i, j] = S[j, i] = 1.0
            A = np.zeros((N, N), dtype=complex); A[i, j] = -1j; A[j, i] = 1j
            gens.append(S / 2); gens.append(A / 2)
    # diagonal
    for k in range(1, N):
        D = np.zeros((N, N), dtype=complex)
        for i in range(k):
            D[i, i] = 1.0
        D[k, k] = -k
        D *= 1.0 / np.sqrt(2 * k * (k + 1))
        gens.append(D)
    return gens


def perm_sign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


def run(N):
    print(f"\n================ su({N}) ================")
    T = su_fundamental_generators(N)
    dim = len(T)
    assert dim == N * N - 1

    # kappa_{AB} = tr(T_A T_B)  (project tr_kappa in the fundamental)
    kappa = np.array([[np.trace(a @ b) for b in T] for a in T]).real
    assert np.max(np.abs(kappa - 0.5 * np.eye(dim))) < TOL, "kappa != delta/2"
    ki = np.linalg.inv(kappa)                      # kappa^{AB}

    # structure constants: [T_A,T_B] = i c_{AB}^C T_C  =>  c_{AB}^D kappa_{DC} = -i tr([T_A,T_B] T_C)
    c_low = np.zeros((dim, dim, dim))              # c_{ABC} (all lower, totally antisym)
    for a, b in itertools.product(range(dim), repeat=2):
        comm = T[a] @ T[b] - T[b] @ T[a]
        for cc in range(dim):
            z = -1j * np.trace(comm @ T[cc])
            assert abs(z.imag) < TOL
            c_low[a, b, cc] = z.real
    c_up = np.einsum('abd,dc->abc', c_low, ki)     # c_{AB}^C = f_ABC here
    f = c_up
    # total antisymmetry of c_{ABC}
    for p in itertools.permutations(range(3)):
        d = np.max(np.abs(np.transpose(c_low, p) - perm_sign(p) * c_low))
        assert d < TOL, "c_{ABC} not totally antisym"
    print("c_{ABC} totally antisymmetric: OK   (c_{AB}^C = f_ABC, kappa = delta/2)")

    # ---------- base contraction C3 ----------
    # C3_{ABG} = kappa^{MM'} kappa^{S1S1'} kappa^{S2S2'} c_{A M S1} c_{B M' S2} c_{G S1' S2'}
    C3 = np.einsum('ams,bnt,guv,mn,su,tv->abg', c_low, c_low, c_low, ki, ki, ki,
                   optimize=True)

    # ---------- (1) slot-assignment enumeration ----------
    # Topology: O has legs L1(->X1, index A-side), L2(->X2, B-side).
    # X1 legs (L1, L3, L4); X2 legs (L2, L3, L5); X3 legs (L4, L5, ext G).
    # A vertex slot assignment is a bijection legs->(C,U,E) slots; the vertex tensor
    # in leg order is c_low with its 3 indices permuted. Reference (identity perms):
    #   X1: (L1,L3,L4)->(1st,2nd,3rd) index, i.e. c_{A' M S1}
    #   X2: (L2,L3,L5) -> c_{B' M' S2}
    #   X3: (Gslot,L4,L5) -> c_{G S1' S2'}
    # eta: attachment of insertion legs (A on L1: eta=+1) or swapped (A on L2: eta=-1).
    nplus = nminus = 0
    ok = True
    for p1, p2, p3 in itertools.product(itertools.permutations(range(3)), repeat=3):
        V1 = np.transpose(c_low, p1)
        V2 = np.transpose(c_low, p2)
        V3 = np.transpose(c_low, p3)
        for eta_word, eta in ((('ams,bnt,guv,mn,su,tv->abg'), +1),
                              (('bms,ant,guv,mn,su,tv->abg'), -1)):
            W = np.einsum(eta_word, V1, V2, V3, ki, ki, ki, optimize=True)
            sign = eta * perm_sign(p1) * perm_sign(p2) * perm_sign(p3)
            if np.max(np.abs(W - sign * C3)) > 1e-9:
                ok = False
            if sign > 0:
                nplus += 1
            else:
                nminus += 1
    print(f"(1) all {nplus + nminus} slot words == (eta*prod parities) x C3 : {'OK' if ok else 'FAIL'}"
          f"   [{nplus} with +1, {nminus} with -1]")

    # ---------- (2) antisymmetry ----------
    d2 = np.max(np.abs(C3 + np.transpose(C3, (1, 0, 2))))
    print(f"(2) C3_(AB)G + C3_(BA)G = 0 :  max|.| = {d2:.2e}  {'OK' if d2 < 1e-10 else 'FAIL'}")

    # ---------- (J) Jacobi step ----------
    X1_ = np.einsum('ams,bnt,mn->abst', c_low, c_low, ki)
    lhsJ = X1_ - np.transpose(X1_, (0, 1, 3, 2))
    rhsJ = np.einsum('abm,mn,nst->abst', c_low, ki, c_low)
    dJ = np.max(np.abs(lhsJ - rhsJ))
    print(f"(J) kappa^MM'(c_AMS1 c_BM'S2 - (S1<->S2)) = c_ABM kappa^MM' c_M'S1S2 : "
          f"max dev {dJ:.2e}  {'OK' if dJ < 1e-10 else 'FAIL'}")

    # ---------- (3) Casimir & reduction ----------
    Cas = np.einsum('amn,bMN,mM,nN->ab', c_low, c_low, ki, ki)   # = C2(adj) kappa_{AB}
    C2 = Cas[0, 0] / kappa[0, 0]
    dCas = np.max(np.abs(Cas - C2 * kappa))
    print(f"(3a) c_AMN c_B^MN = C2 kappa_AB with C2 = {C2:.6f} (expect 2N = {2*N}); "
          f"dev {dCas:.2e}  {'OK' if dCas < 1e-9 and abs(C2 - 2*N) < 1e-9 else 'FAIL'}")

    d3 = np.max(np.abs(C3 - 0.5 * C2 * c_low))
    print(f"(3b) C3_ABG = (C2/2) c_ABG = {0.5*C2:.4f} c_ABG (expect N={N}): "
          f"max dev {d3:.2e}  {'OK' if d3 < 1e-9 else 'FAIL'}")

    fff = np.einsum('ams,bmt,gst->abg', f, f, f)                 # pure-delta contraction
    d3f = np.max(np.abs(fff - 0.5 * N * f))
    print(f"(3c) f_AMS1 f_BMS2 f_GS1S2 = (N/2) f_ABG : max dev {d3f:.2e}  "
          f"{'OK' if d3f < 1e-9 else 'FAIL'}")

    # ---------- (4) settlement F cross-check ----------
    F = np.einsum('Au,Bv,Cc,uCd,vce->ABde', ki, ki, ki, c_low, c_low)  # F^{AB}_{DE}
    d4a = np.max(np.abs(F - np.transpose(F, (1, 0, 3, 2))))
    print(f"(4a) F^AB_DE = F^BA_ED ((A,D)<->(B,E) symmetric): max dev {d4a:.2e}  "
          f"{'OK' if d4a < 1e-10 else 'FAIL'}")
    C3up = np.einsum('Aa,Bb,abg->ABg', ki, ki, C3)               # C3^{AB}_G
    C3fromF = np.einsum('ABde,dD,eE,gDE->ABg', F, ki, ki, c_low)
    d4b = np.max(np.abs(C3up - C3fromF))
    print(f"(4b) C3^AB_G = kappa^DD' kappa^EE' F^AB_DE c_GD'E' : max dev {d4b:.2e}  "
          f"{'OK' if d4b < 1e-10 else 'FAIL'}")
    # antisym-in-(D,E) part of F is the Jacobi combination (kappa-raised)
    Fanti = 0.5 * (F - np.transpose(F, (0, 1, 3, 2)))
    rhs4 = 0.5 * np.einsum('Aa,Bb,abm,mn,nde->ABde', ki, ki, c_low, ki, c_low)
    d4c = np.max(np.abs(Fanti - rhs4))
    print(f"(4c) F^AB_[DE] = (1/2) c^AB_M kappa^MM' c_M'DE : max dev {d4c:.2e}  "
          f"{'OK' if d4c < 1e-10 else 'FAIL'}")

    # sample value at the largest-|c| component
    idx = np.unravel_index(np.argmax(np.abs(c_low)), c_low.shape)
    print(f"    sample at {tuple(i+1 for i in idx)}: C3 = {C3[idx]:.6f}, "
          f"c = {c_low[idx]:.6f} (ratio {C3[idx]/c_low[idx]:.4f})")
    return True


if __name__ == "__main__":
    for N in (2, 3):
        run(N)
    print("\nAll checks executed.")
