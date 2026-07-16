# Step-5 independent physics review — 2026-07-16

Status: `NON_AUTHORITY_PROPOSAL` — review evidence only. Nothing here settles a project
formula; per `AUTHORITY.md` only a reviewed merge with green `verify` does that.

Object under review: the Step-5 settlement candidate on PR #61
(`agent/step5-complete-one-loop-anomaly`, head `bf9ced7`), main contract
`contracts/foundations/step-05-euclidean-n4-awi-one-loop.md` (1,402 lines), result ledger
`generated/step5/project-result-ledger.json` (81 ordered pairs: 29 exact nonzero, 52 exact
zero), HT round-trip `K^P = 2T^\mathrm{HT,printed} = T^{\rm HT,corr}`.

Method: the reviewer independently re-derived the load-bearing identities below without
consulting the PR's audit scripts, then compared. "Verified" means an independent derivation
reproduced the claim exactly; "consistent" means the claim passes structural cross-checks but
was not re-derived term by term.

---

## R.0 The physical logic (restating the owner's route precisely)

The unregularized Schwinger–Dyson identity (project form: (3D.34)) says an equation-of-motion
insertion attached to a propagator collapses it to an exact superspace delta function:
$K\,K^{-1}=\delta$. If the regulator preserved (i) $\delta S/\delta v \leftrightarrow
\delta/\delta v$, (ii) $K K^{-1}=\delta$, and (iii) four-dimensional D-algebra
simultaneously, the complete SD graph family for $\boldsymbol\nabla_-(L_iL_j)$ would cancel
exactly and no anomaly could arise. In DRED the D-algebra numerators are four-dimensional
while the propagator inverse is $d$-dimensional, so the collapse is a *regulated* delta:
the mismatch is the evanescent insertion $\mu_\ell^2$, and the entire anomaly is the finite
remainder of this cutting-rule failure.

One refinement of the owner's phrasing "the BPS letters have no contact terms": the
tree-level contact terms among letters are **not** zero — they are exactly the classical
bracket ($Q_0$-action, e.g. $Q_0 C=\frac12[C,C]$), i.e. the classical EOM/transport sectors.
The correct statement, which the PR #61 contract implements, is that these classical sectors
are separated off first, and the *quantum remainder* comes solely from the regulated-cut
mismatch. With that refinement the route is exactly right.

## R.1 The cutting-failure identity — VERIFIED

Claim (PR #61, Final Result List): with four-dimensional numerator square $\bar r_e^{\,2}$
and regulated denominators $D_j = r_{j,d}^{\,2}$,

$$
\frac{\bar r_e^{\,2}}{D_0D_1D_2}-\frac{1}{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2 .
\tag{R.1}
$$

Independent derivation: $\bar r_e^{\,2}=r_{e,d}^{\,2}+(\bar r_e^{\,2}-r_{e,d}^{\,2})
=D_e+\mu_{r_e}^2$. External momenta are physical (no evanescent components), so the
evanescent part of every line momentum equals that of the loop momentum:
$\mu_{r_e}^2=\mu_\ell^2$. Dividing by $D_0D_1D_2$ gives (R.1) exactly, for every marked line
$e$. This is precisely "EOM×propagator = regulated delta, not exact delta": the failure is
one universal insertion, with **no graph-specific $(4-d)$ factors** — confirming the PR's
"no extra graph-specific evanescent factor" rule and the owner's mechanism.

## R.2 The evanescent master integral — VERIFIED

Claim: $\displaystyle\lim_{\epsilon\to0}\mu^{2\epsilon}\!\int\!\frac{d^{4-2\epsilon}\ell}
{(2\pi)^{4-2\epsilon}}\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}=\frac{1}{32\pi^2}$.

Independent derivation. In the dimension-shift representation $\mu_\ell^2=-\widetilde\ell^2$
with $\widetilde\ell$ the formal $(d-4)$-dimensional component; rotational averaging gives
$\int d^d\ell\,\widetilde\ell^2 f(\ell^2)=\frac{d-4}{d}\int d^d\ell\,\ell^2 f(\ell^2)$, so

$$
\int\!\frac{d^d\ell}{(2\pi)^d}\frac{\mu_\ell^2}{(\ell^2+\Delta)^3}
=\frac{4-d}{d}\int\!\frac{d^d\ell}{(2\pi)^d}\frac{\ell^2}{(\ell^2+\Delta)^3}
=\frac{2\epsilon}{d}\cdot\frac{1}{(4\pi)^{d/2}}\,\frac{d}{2}\,
\frac{\Gamma(2-\tfrac d2)}{\Gamma(3)}\,\Delta^{\frac d2-2}
=\frac{\epsilon\,\Gamma(\epsilon)}{2\,(4\pi)^{d/2}}\Delta^{-\epsilon}.
\tag{R.2}
$$

As $\epsilon\to0$, $\epsilon\Gamma(\epsilon)\to1$ and the limit is
$\frac{1}{2(4\pi)^2}=\frac{1}{32\pi^2}$, independent of $\Delta$ — which is simultaneously
the proof that the anomaly is **local** (polynomial in external momenta): the would-be
nonlocal $\Delta$-dependence enters only at $O(\epsilon)$. Companion pole
$J_2|_{\rm pole}=\frac{1}{16\pi^2\epsilon}$ from
$\int\frac{d^d\ell}{(2\pi)^d}(\ell^2+\Delta)^{-2}=\frac{\Gamma(\epsilon)}{(4\pi)^{d/2}}
\Delta^{-\epsilon}$: also verified.

## R.3 The evanescent trace identity — VERIFIED

Claim (PR #61 §5): for physical (hatted) external momentum $p$,
$p^\rho\breve\delta^{mn}(\sigma_m\bar\sigma_\rho\sigma_n)=-2\epsilon\,p^\rho\sigma_\rho$.

Independent derivation: Euclidean Clifford algebra
$\sigma_m\bar\sigma_\rho=2\delta_{4,m\rho}-\sigma_\rho\bar\sigma_m$ gives
$\sigma_m\bar\sigma_\rho\sigma_n=2\delta_{4,m\rho}\sigma_n-\sigma_\rho\bar\sigma_m\sigma_n$.
Contracting: the first term is $2p^\rho\breve\delta_\rho{}^{n}\sigma_n=0$ (physical $p$ has
no evanescent components); in the second, the symmetric part of $\bar\sigma_m\sigma_n$ under
$\breve\delta^{mn}$ is $\delta_{4,mn}$, so
$\breve\delta^{mn}\bar\sigma_m\sigma_n=\breve\delta^m{}_m=2\epsilon$. Result:
$-2\epsilon\,p^\rho\sigma_\rho$. The pole arithmetic of §5,
$-\frac{\hbar g^2}{32\pi^2\epsilon}\times(-2\epsilon)=+\frac{\hbar g^2}{16\pi^2}$, is then
exact. Verified.

## R.4 Selection rules and the 29/52 census — INDEPENDENTLY REPRODUCED

This is the owner's "analyze the conserved quantities first to constrain uncontracted
external legs" step, done independently.

Alphabet (project letters ↔ twist letters): $A=(\boldsymbol\nabla_+\boldsymbol{\mathcal
W}_+)\leftrightarrow b$, $B_r=(\boldsymbol\nabla_+\boldsymbol\Phi_r)\leftrightarrow\beta_r$,
$C^r=\widetilde{\boldsymbol\Phi}^r\leftrightarrow\gamma^r$,
$D_{\dot a}=\widetilde{\boldsymbol{\mathcal W}}_{\dot a}\leftrightarrow\partial_{\dot a}c$;
nine component letters, $81$ ordered pairs.

Gradings that survive the twist and constrain the anomaly output: $SU(3)$ flavor
($A,D$ singlets; $B_r\in\mathbf 3$; $C^r\in\bar{\mathbf 3}$), Grassmann parity
($|A|=|C|=0$, $|B|=|D|=1$), twisted dimension
($[c]=\tfrac12,\ [C]=1,\ [B]=[D]=\tfrac32,\ [A]=2$, $[\partial_{\dot a}]=1$,
$[Q_{1\text{-loop}}]=\tfrac12$), and the bilinear output structure
$\partial_{\dot a}X\,\partial^{\dot a}Y$ forced by the $\sigma$-chain of R.3. Checking each
ordered family against these conservation laws and the cubic-vertex spectator structure
(vertices $b[c,c]$, $\beta[c,\gamma]$, $\varepsilon\gamma[\gamma,\gamma]$):

| family | flavor structure | count (ordered) |
|---|---|---|
| $(A,A)$ | $f f$ | 1 |
| $(A,B_r),(B_r,A)$ | $f f$ | 6 |
| $(A,C^r),(C^r,A)$ | $f f$ | 6 |
| $(A,D_{\dot a}),(D_{\dot a},A)$ | derivative descent of the $(b,c)$ seed | 4 |
| $(B_r,C^s),(C^s,B_r)$ | $\propto\delta_r^s$ only | 6 |
| $(B_r,B_s)$ | $\propto\varepsilon_{rst}$, $r\ne s$ only | 6 |

Total nonzero $=1+6+6+4+6+6=\mathbf{29}$; zeros $=(B/C,D)$ mixed $24$, $(D,D)$ $4$,
$(C,C)$ $9$, diagonal $(B,B)$ $3$, off-diagonal $(B,C)$ $12$, total $\mathbf{52}$.
Example kill: for $(C,C)$, $SU(3)$ alone would allow
$\varepsilon\,\partial B\,\partial B$, but twisted dimension
($1{+}1{+}\tfrac12=\tfrac52\ne \tfrac32+\tfrac32+2$) and the vertex census exclude every
candidate; for $(c,c)$-descendants the only closable triangle leaves a single spectator $b$
of dimension $2\ne\tfrac52$ — no admissible output exists.

**Three independent routes now agree on 29/52**: this charge/vertex analysis, the HT source's
vanishing list ($Q_1(cc)=Q_1(\gamma\gamma)=Q_1(\gamma c)=Q_1(\beta c)=0$, main.tex line 731),
and PR #61's ledger census. Reproduced.

## R.5 The holomorphic-twist factor-2 adjudication — VERIFIED

The HT source is internally inconsistent by a factor of 2
(`HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO`): its zero-shift kernel
$\mathcal D^{\triangle}_{0,0}(f,g)=\frac12\partial_{\dot a}f\,\partial^{\dot a}g$ and its
Appendix-B tower give coefficient $\kappa^2/2$ at $m{=}n{=}0$, while its printed component
formulas (3.63)–(3.68) carry $\kappa^2$. PR #61 adjudicates: the *components* are right and
the printed kernel is missing the factor $2$ from the triangle Feynman parametrization.

Independent check of the adjudicated tower. The ordered two-parameter form of the triangle,

$$
\frac{1}{D_0D_1D_2}=2\int_0^1\!db\int_0^b\!da\;\frac{1}{[\,\ell^2+\Delta(a,b)\,]^3},
\tag{R.5a}
$$

carries the explicit $\Gamma(3)=2$. The shifted insertion leg contributes
$e^{i w\cdot(a q+b p)}$, so the derivative tower of the anomaly kernel is

$$
2\int_0^1\!db\int_0^b\!da\;a^{k+\ell}\,b^{(m-k)+(n-\ell)}
=\frac{2}{(k+\ell+1)(m+n+2)},
\tag{R.5b}
$$

reproducing **exactly** the project coefficient
$K^P_{m,n;k,\ell}=\frac{2\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)}
=2\,T^\mathrm{HT,printed}_{m,n;k,\ell}$, and at $m{=}n{=}0$ giving relative weight $1$ — i.e.
agreeing with HT's own printed *components* while doubling its printed *kernel*. The factor
of $2$ is the Feynman-parameter $\Gamma(3)$, not a second orientation, exactly as PR #61
§10 states. The adjudication direction is the internally consistent branch of the source.
Verified analytically; the sealed $9{\times}9{\times}25$ rectangle check (2025 coefficients)
is then a mechanical corroboration.

On `HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT` ($-\frac14$ in eq. (1.10) vs $-\kappa^2$ in
eq. (3.69)): consistency of the two printings requires $\kappa=\frac12$, i.e.
$\operatorname{Tr} t_At_B=\frac12\delta_{AB}$ (fundamental normalization), which contradicts the source's
own words "$\kappa$ is the dual Coxeter number". This is an editorial defect *of the source*;
the project's resolution — derive its own coefficient in its own Killing-form conventions
($\lambda_1=\frac{\hbar g^2}{16\pi^2}$, $\mathbb F^{AB}{}_{DE}$) and compare output words —
is the correct procedure, and quarantining the source's absolute trace normalization as
`OUT_OF_SCOPE...SOURCE_PROVENANCE` is sound.

## R.6 What is NOT yet verified (the remaining trust surface)

The following were **not** re-derived here and constitute the entire remaining review scope:

1. the per-factor provenance of the contact-row sign chain
   $(-\tfrac14)_K(-1)_{\rm endpoint}(\tfrac12)_{D_-D_+}(2)_{\rm mixed}(2)_{\rm Wick}
   (-\tfrac12)_{p_+}=-\tfrac14$ against the 5A Koszul tables (5A.61–62);
2. the absolute color normalization ($\mathbb F^{AB}{}_{DE}$ vs the 4C Killing conventions)
   and the "$4096$" absolute-normalization/G3-retraction story in the AB/BA family;
3. the exhaustiveness of the graph census per channel (that no same-order contact,
   letter-expansion, ghost, or collapsed topology is missing) — R.1 makes each *listed*
   graph's anomaly correct, but completeness of the list is a separate combinatorial fact;
4. the individual coefficients/orderings of the 29 nonzero channels beyond the AA seed;
5. the HT dictionary's field-normalization factors
   ($\beta\leftrightarrow\frac1{\sqrt2}B$, $b\leftrightarrow-\frac i{\sqrt2}A$,
   $\partial c\leftrightarrow iD$, $Q_0\leftrightarrow-\frac12\boldsymbol\nabla_-$) against
   the project spinor conventions.

**Recommended bounded spot-check protocol** (each a half-day, human-readable memo; PR #61
already contains a GPT-Pro gate document to diff against in each case):

- (S1) re-derive the AA seed end-to-end from §§1–5 of the settlement contract using only
  R.1–R.3 above;
- (S2) audit the six factors of the contact-row sign chain against 5A;
- (S3) re-derive one matter channel, $(B_1,C^1)$, including the $\delta_r^s$ structure;
- (S4) re-derive one zero, $(C^r,C^s)$, as a charge/vertex-basis proof;
- (S5) audit the AB/BA total-derivative rebase and the $4096$ normalization retraction.

If S1–S5 pass, the settlement's remaining risk is concentrated in item 3 (census
completeness), for which the right instrument is one adversarial review session dedicated to
"name a topology not in the census", not more scripts.

## R.7 Verdict

The central mechanism of the Step-5 settlement — anomaly $=$ evanescent failure of the
regulated Schwinger–Dyson cutting rule, localized by (R.1) and computed by (R.2)/(R.3) — is
independently confirmed, as are the 29/52 census and the direction and magnitude of the
holomorphic-twist factor-2 adjudication. The owner's physical route is sound and is in fact
what the settlement implements. The remaining review scope is the bounded five-item list
above, not the 513k-line diff.
