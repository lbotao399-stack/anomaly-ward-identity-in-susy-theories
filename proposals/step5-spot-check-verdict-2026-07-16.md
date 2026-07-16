# Step-5 settlement spot-check verdict — 2026-07-16

Status: `NON_AUTHORITY_PROPOSAL` — consolidated review verdict for the Step-5 settlement
(PR #61), executing the S1–S5 protocol of
`proposals/step5-independent-physics-review-2026-07-16.md`. Owner authorization for the
review-and-merge sequence: 2026-07-16 session.

Reviewed artifact: `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md` at the
settlement head, cross-read against `contracts/foundations/step-05a-*.md` (locked grammar),
the vendored HT source (arXiv:2512.07771v2), and the archived GPT-Pro gate documents.

## S1 — AA seed end-to-end: PASS

Independently re-verified, line by line, with no reference to the audit scripts:

- §2 cut identity $\bar r_e^{\,2}/(D_0D_1D_2)-1/\prod_{j\ne e}D_j=\mu_\ell^2/(D_0D_1D_2)$
  (one-line proof; external momenta carry no evanescent components).
- §3 tree descendants $\boldsymbol\nabla_-A=-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times
  C_s)$, $\boldsymbol\nabla_-B_r=-2\mathscr E_{\widetilde r}-\sqrt2\varepsilon_{rst}
  (C_s\times C_t)$, $\boldsymbol\nabla_-C_r=\boldsymbol\nabla_-D_{\dot a}=0$ — matches the
  twisted $Q_0$ structure through the §10 dictionary (covariant $\boldsymbol\nabla_-$
  absorbing the $[c,\cdot]$ terms).
- §4 loop arithmetic: Feynman simplex ($\Gamma(3)=2$, volume $\tfrac12$),
  $J_n$ closed form, $\Delta J_3=\tfrac\epsilon2 J_2$,
  $\operatorname{Res}J_2=\tfrac1{16\pi^2}$, and the tensor reduction
  $\int_r r_mr_n/(r^2+\Delta)^3=\tfrac{\widehat\delta_{mn}}4 J_2$ — the $\tfrac14$ is exact
  because $(1-\tfrac\epsilon2)/(4-2\epsilon)=\tfrac14$ identically. Triangle pole
  $+\tfrac{\hbar g^2}{32\pi^2\epsilon}\mathbb F\,\widehat\delta^{mn}T_{m\rho n}p^\rho$
  follows from the $\tfrac{g^2}2$ prefactor exactly.
- §5 contact sum $-\tfrac{\hbar g^2}{32\pi^2\epsilon}\mathbb F\,\delta_4^{mn}T_{m\rho n}
  p^\rho$, the evanescent difference $\widehat\delta-\delta_4=-\breve\delta$, the trace
  identity $p^\rho\breve\delta^{mn}T_{m\rho n}=-2\epsilon\,\sigma\!\cdot\!p$, and the finite
  remainder $+\tfrac{\hbar g^2}{16\pi^2}\mathbb F^{AB}{}_{DE}\,\sigma_\rho p^\rho$.

## S2 — contact-row sign chain: PASS (arithmetic + structural), provenance delegated

The six-factor product $(-\tfrac14)(-1)(\tfrac12)(2)(2)(-\tfrac12)=-\tfrac14$ and the
four-row sum $4\times\tfrac1{128}=\tfrac1{32}$ are verified. The per-factor provenance
against the 5A Koszul tables was not re-traced factor by factor in this review; it is
covered structurally by the fact that any error in a single factor would break the exact
$1/\epsilon$ cancellation between §4 and §5 (the regulated Ward identity), which is
exhibited, and mechanically by the committed replay tables (269 external-slot, 9216
color-mask rows).

## S3 — matter channels: PASS (structural + jet weights)

Every §7 family formula maps onto the corresponding HT component row with the correct
symmetry and flavor structure through the §10 dictionary: $\Delta(A,A)$ four-term
antisymmetric combination ↔ $Q_1(bb)$; $\Delta(B_r,C_s)=\delta_{rs}\langle D,D\rangle$ ↔
$Q_1(\beta_I\gamma^J)\propto\delta_I^J\,\partial c\partial c$;
$\Delta(B_r,B_s)\propto\varepsilon_{rst}$ antisymmetric ↔ $Q_1(\beta\beta)$;
$\Delta(A,B_r)$ symmetric mixed terms plus $\varepsilon\langle C,C\rangle$ ↔ $Q_1(\beta b)$.
The $\Delta(A,D_{\dot a})/\Delta(D_{\dot a},A)$ jet weights $(\tfrac13,\tfrac23)$ equal the
**corrected** ($\times2$) HT tower at $(m,n)=(1,0)$, independently confirming the factor-2
adjudication at first derivative order.

## S4 — zero channels: PASS

$\boldsymbol\nabla_-C_r=\boldsymbol\nabla_-D_{\dot a}=0$ makes 25 ordered pairs vanish
identically at the operator level; flavor selection ($\delta_{rs}$, $\varepsilon_{rst}$)
kills 12 off-diagonal $(B,C)/(C,B)$ and 3 diagonal $(B,B)$; the remaining $(B,D)/(D,B)$ 12
vanish by the charge/vertex analysis. Total 52, independently reproduced together with the
29 nonzero (three agreeing routes: charge counting, HT vanishing list, settlement census).

## S5 — AB/BA rebase and normalization: PASS (logic + arithmetic), carriers delegated

Verified: kernel uniqueness ($\ker M_q=\mathbb C k_q$ with $k_q=(1,1,-i\sqrt2,+i\sqrt2)$;
all three rows annihilate $k_q$), $M_qv_{\rm TD}=(-1,-2i\sqrt2,+2i\sqrt2)^T$,
$v_{\rm ren}=v_{\rm TD}+\delta v_{\rm fin}=k_q$, and that the §7 $\Delta(A,B_r)$ row *is*
$k_q$ — i.e. residual-$q$ covariance anchored to the AA scale fixes AB/BA uniquely, landing
on the HT-matching structure. The raw quotient-map carriers $(2,2)$ and
$(-\tfrac13,\tfrac43)$ rest on the committed graph replay and were not re-derived; the
scheme/anomaly separation (finite normal product vs $\mu_\ell^2$ failure) is correctly
typed.

## Residual trust surface (explicitly not closed by this review)

1. Per-graph census completeness for each channel family (that no same-order topology is
   missing) — recommend one adversarial "name a missing topology" session as the final gate;
2. per-factor provenance of the S2 sign chain against 5A tables;
3. the absolute color normalization audit trail (G3/"4096") beyond the logic verified in S5;
4. the HT dictionary's absolute field normalizations beyond the structural and jet-weight
   confirmations above.

None of these is a defect finding; they are the bounded remainder of an
otherwise-confirmed settlement.

## Verdict

`SPOT_CHECKS_PASSED_WITH_BOUNDED_RESIDUAL_SURFACE`. The settlement's central mechanism,
seed channel, family structure, census, and HT adjudication are independently confirmed.
Recommended: merge upon green `verify`, recording the four residual items above as the
follow-up review obligation.
