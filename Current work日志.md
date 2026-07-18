# Current Work

## 2026-07-17 decision list — Step-0 unified notation convention (统一记号约定)

Convention branch locks surfaced per the derivation-first law; none left as standing BLOCKED.

- **Locked branches (LOCK):** mostly-plus $\eta_L=\operatorname{diag}(-1,+1,+1,+1)$ (0A.2); single-exponent bridge $\mathcal E=e^{\mathcal V}$ (0A.83); $\mathcal W_a=-\frac18\bar D^2(\mathcal E^{-1}D_a\mathcal E)$ (0A.84); i-ful BRST $\mathbf s\mathfrak c=i\mathfrak c^2$ (0A.106); Weyl primacy with the Majorana layer conditional; R-branch $r=-2\Delta/3$ (0A.132).
- **P0 corrected pre-PR:** $\epsilon_{E,1234}=+1$ (was $-1$ in draft), derived by $\delta_E$-lowering of (0A.2); pinned by exact lowering sum in `scripts/verify_step00_unified_notation.py`.
- **F-term arbitration:** exact $\mathbb Q(i)$ Grassmann engine verdict form (A) — $i(\sigma^{\mu\nu})_a{}^b\vartheta_bF_{\mu\nu}$ of (0A.77); lowered-index form (B) rejected.
- **OUT_OF_SCOPE (nonblocking):** `OUT_OF_SCOPE_N2_N4_CLOSURE_CROSSCHECK`, `OUT_OF_SCOPE_WEINBERG_GAUGINO_PHASE`, `OUT_OF_SCOPE_DRED_MOMENTUM_LEDGER_LOR_CYCLE`, `OUT_OF_SCOPE_NK_BRANCH_TABLE`.
- Acceptance of `CONTRACT-STEP-00-UNIFIED-NOTATION-001` happens by PR review; Notion mirror is post-merge only.

## Current Difficulty

- **LATEST — `OPEN_FINAL_CENSUS_17_CANDIDATES`:** the final Claude census proposal did not run the ghost--Nielsen--Kallosh sector, the zero/cut-orbit sector, or the automated three-lens refutation, and deferred four physics-relevant Wick routings.  Holomorphic-twist agreement does not prove termwise absence.  The accepted coefficient ledger is unchanged.
- `BLOCKED_HEAT_KERNEL_TYPED_REGULATOR_AND_COEFFICIENT_DERIVATION`: the proposal's matter blocks give $16\Box_E\mathcal P_+$ and its vector block gives $+\Box_E$, not the declared $-\Box_E$ generator; the mixed blockwise prescription is not one functional calculus.
- `NOT_ACCEPTED_NOETHER_B1_B4_MISSING`: complete Euler operators and the announced B1--B4 termwise checks are absent.  The locked Lorentzian vector cycle also remains blocked.
- `VERIFIED_CONDITIONAL_STEP5J_TREE_SCALE` (`e97e5c8`): the corrected tree cross-lock derives only $\zeta_Q\zeta_\beta/\zeta_\gamma^2=\rho_{fc}/2$.  It explicitly treats $\rho_{fc}=1$ as an assumption, retracts the unconditional unit dictionary for the $\mathcal W$ letter, and retracts the claim that the box must be replaced by a triangle.  The full box-plus-triangle graph set and relative coefficients remain open; the script verifies only the factor-two arithmetic and not the phase/sign or dictionary inputs.
- **Physical one-loop anomaly sector:** no unresolved coefficient row.  The target-blind ledger has `81 COMPLETE_EXACT`, `29 EXACT_NONZERO`, `52 EXACT_ZERO`, `0 OPEN`, and `0 UNRESOLVED`.
- `OUT_OF_SCOPE`: general raw-graph $q$-equivariant functor, complete BV/Wess--Zumino/open-color evanescent-module theorem, formal $U/Q_0$ absolute intertwiner, and general reductive-color inverse.  None is used in the accepted physical result.

## Certain

- The accepted BC bottom projection is

$$
Q_-\!\left(\psi_{r+}^A\widetilde\phi_s^B\right)\Big|_{1\text{-loop}}
=-\frac{\sqrt2\hbar g^2}{32\pi^2}
\delta_{rs}\mathbb F^{AB}{}_{DE}
\widetilde\lambda_{\dot a}^D\widetilde\lambda^{E\dot a}.
$$

It is the bottom projection of the regulated superfield Euler Jacobian, not an independent ordinary two-Yukawa box.  The mixed propagators $G_{\phi\widetilde\psi}$ and $G_{\psi\widetilde\phi}$ vanish.

- The dotted-gaugino bilinear is symmetric in $D,E$; antisymmetric color words therefore vanish.  The corrected tensor integral is $J=1/(128\pi^2)$, while the explicit numerator factor gives $2J=1/(64\pi^2)$.

- Majorana matrix identities on the proposed Srednicki branch are conditional checks only.  Project quantities and phases remain Weinberg; explicit Srednicki-style index placement does not authorize a field rephasing.

- The post-cutoff task-rotation test repair is accepted: Step-5A admissibility is read from the ledger obligation's archived task packet, not from whichever unrelated obligation is currently `tasks/CURRENT.yaml`.

- Every bare graph residue is the occurrence-wise DRED cutting failure

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

- Ordered (AB_r/BA_r) is closed by

$$
v_{\rm raw}
=\left(2,2,-\frac13,\frac43,-2i\sqrt2,+2i\sqrt2\right),
$$

$$
v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2),
$$

$$
\delta v_{\rm fin}=(1,0,+i\sqrt2,-i\sqrt2),
\qquad
v_{\rm ren}=(1,1,-i\sqrt2,+i\sqrt2),
\qquad
M_qv_{\rm ren}=0.
$$

The finite shift is a composite-source normal-product scheme term, not a new anomaly graph.

- Project data were canonicalized and SHA-256 sealed before HT read.  Direct comparison gives `81/81` coefficient/output-word matches.  For every (m,n\in\mathbb Z_{\ge0}),

$$
K^P_{m,n;k,\ell}
=2T^{HT,\mathrm{printed}}_{m,n;k,\ell}
=T^{HT,\mathrm{corrected}}_{m,n;k,\ell}.
$$

The executable rectangle gives `2025/2025` exact kernel checks and `141750/141750` lifted coefficient checks.

- The obsolete full-1PI scale-one audit is retracted; the exact (G_3) full-measure normalization is

$$
32768\left(\frac14\right)\left(\frac12\right)
=65536\left(\frac14\right)\left(\frac14\right)
=4096.
$$

- Physical verifier: `ACCEPTED`, scope `PHYSICAL_ONE_LOOP_ANOMALY_SECTOR`, `33/33 PASS`.  GPT Pro Gate 15 independently returned `FINAL_ONE_LOOP_HT_SETTLEMENT_ACCEPTED`.

- Primary artifacts: `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`, `audits/step5-global-81-target-blind-orbit-ledger.md`, `audits/step5_global_81_ht_symbolic_roundtrip_exact.md`, `audits/step5-euclidean-n4-awi-verification.json`, and `proposals/gpt-pro-final-one-loop-ht-settlement-gate15-response-2026-07-14.md`.
