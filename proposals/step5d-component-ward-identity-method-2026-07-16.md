# Step-5D memo — the component-form Ward identity $\int\partial_\mu j^\mu\,\mathcal O\sim\delta\mathcal O$: letters, EOM insertions, and the one-loop calculational method, Lorentzian ∥ Euclidean

Status: `NON_AUTHORITY_PROPOSAL` — a **method** memo: it fixes the objects, the exact
classical identities, and the complete calculational pipeline for the component-form
anomalous Ward identity, and computes the structural layer (letter algebra, contact
terms, graph families, selection rules). It does **not** claim evaluated one-loop
coefficients; those are the settlement-scale execution of this method (§9). Numbered
equations are (5D.$n$).

Owner instructions implemented (2026-07-16): *compute the Ward identity frontally,
$\int\partial_\mu j^\mu\,\mathcal O\sim\delta\mathcal O$, in component form, as the method
for the loop corrections; letters are the standard quadratic (bilinear) insertions built
from $f_{++}$, $\psi_+$, $\bar\phi$, the derivative $D_{+\dot\alpha}$, and $\bar\lambda$;
write $\partial_\mu j^\mu_-$ in the EOM-proportional form of the Step-5C memo; expand the
Feynman diagrams — the principle parallels the existing superspace workflow; develop the
calculational method.*

---

## 1. Position of the component route

The superspace route (Step-5A/5B rules, settlement contract) and the component route
developed here compute the same anomaly. They are **independent routes**: the equivalence
of the component (Wess–Zumino-gauge) BRST system with the superfield BV system is the
known deferred item `OUT_OF_SCOPE_WZ_BV_REDUCTION` /
`OUT_OF_SCOPE_COMPONENT_TO_SUPERFIELD_BV_EQUIVALENCE` (Step-5B memo §11). That is
precisely the value of the component route: an agreement of the two routes on the
81-channel ledger is a genuine cross-check, not a tautology.

Quantization used here: the component actions (4C.14) [L] / (4C.42a) [E] in Wess–Zumino
gauge, gauge-fixed by the ordinary BV machinery of 3D applied to the **component** gauge
symmetry $\delta A_M=\mathcal D_M\alpha$, $\delta X=i\llbracket\alpha,X\rrbracket$: FP
ghosts $(c,\bar c,b)$, Lorenz–Feynman gauge $\Psi=\langle\bar c,\partial^MA_M
-\tfrac12\xi b\rangle$, $\xi=1$. This is standard textbook-free content: every formula is
derived from (3D.70)–(3D.93) applied to the component theory, with $\tau_R$, $\eta_R$,
$\upsilon_R$ from (3D.6)/(5A.2). The component Feynman rules follow from (4C.14)/(4C.42a)
plus this gauge fixing (§6); the auxiliary fields may be kept (contact propagators
$\langle\mathscr D\mathscr D\rangle$, $\langle F\widetilde F\rangle\propto$ constants) or
integrated out — the Step-5C current is auxiliary-free either way.

## 2. Spin frame and the component letter alphabet

### 2.1 Frame decision

No merged contract defines $\pm$ spin-frame components (checked: 3C, 4, 5A). We fix:

> **(5D.D4)** Frame identification $+:=1$, $-:=2$ for undotted indices and
> $\dot+:=\dot1$, $\dot-:=\dot2$ for dotted indices, with the locked epsilon values
> (1.3)–(1.5): $\epsilon_{+-}=\epsilon_{12}=-1$, $\epsilon^{+-}=+1$. Frame components
> are index evaluations, $X_+:=X_{a=1}$, $X_-:=X_{a=2}$; raising/lowering follows (1.5),
> e.g. $X^+=X_-\,\epsilon^{+-}\cdot(-1)^{\text{order}}$ handled index-explicitly, never
> by a separate rule.

### 2.2 Letters

Symmetric field-strength bispinor and its projections ((3C.72i), $\tau_L=i$,
$\tau_E=-i$ (3C.72h)):

$$
f_{ab}:=(\sigma_R^{MN})_a{}^c\epsilon_{cb}\,F_{MN}\big|_{\rm sym},
\qquad
\boldsymbol\nabla_{Ra}\boldsymbol{\mathcal W}_{Rb}\big|
=-\epsilon_{ab}\mathscr D_R+\tau_R\,(\sigma_R^{MN})_{ab}F_{RMN}.
\tag{5D.1}
$$

The component letter alphabet (Euclidean displayed; Lorentzian identical with bars for
tildes), with the superspace-alphabet identifications that make the component and
superspace ledgers the same census:

$$
\boxed{
\begin{array}{c|c|c|c}
\text{letter}&\text{component definition}&\text{superspace origin}&
\text{HT dictionary}\\ \hline
\mathfrak f:=f_{++}&(\sigma_E^{mn})_{++}F_{mn}
&\tau_E^{-1}\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+|&b\\
\mathfrak b_r:=\psi_{r+}&\psi_{ra}|_{a=+}
&\tfrac1{\sqrt2}\boldsymbol\nabla_+\boldsymbol\Phi_r|\ \ \text{(3C.65)}&\beta_r\\
\mathfrak c^r:=\widetilde\phi_r&\widetilde\phi_r
&\widetilde{\boldsymbol\Phi}_r|&\gamma^r\\
\mathfrak d_{\dot a}:=\widetilde\lambda_{\dot a}&\widetilde\lambda_{\dot a}
&-i\widetilde{\boldsymbol{\mathcal W}}_{\dot a}|\ \ \text{(3B.40)}&\partial_{\dot a}c
\text{-type}\\
\mathcal D_{+\dot a}&(\sigma_E^m)_{+\dot a}\mathcal D_m
&\boldsymbol{\mathcal D}_{a\dot a}|_{a=+}&\partial_{\dot a}
\end{array}}
\tag{5D.2}
$$

Insertions $\mathcal O$ are the **ordered bilinears** of the nine derivative-dressed
letters $\{\mathfrak f,\ \mathfrak b_r,\ \mathfrak c^r,\ \mathfrak d_{\dot a}\}$ and
their $\mathcal D_{+\dot a}$-descendants — the same $9\times9=81$ ordered channel ledger
as the superspace program, now realized on component fields.

### 2.3 Gradings and the $\delta_-$ cocycle table

The transformation relevant to the twisted supercharge is the **minus slot** of the
manifest $\mathcal N=1$ transformations (5C.2)/(5C.3): $\delta_-X:=\delta_aX|_{a=-}$
(right strip (5C.1)). From (5C.3), using $\epsilon_{-+}=\epsilon_{21}=+1$:

$$
\boxed{
\begin{aligned}
\delta_-\mathfrak c^r&=0,\qquad
\delta_-\mathfrak d_{\dot a}=0,\qquad
\delta_-(\text{any }\mathcal D_{+\dot a}\text{-descendant})
=\mathcal D_{+\dot a}(\delta_-\,\cdot\,)
+(\delta_-A\text{-terms}),\\
\delta_-\mathfrak b_{r}&=\delta_-\psi_{r+}
=-\sqrt2\,\epsilon_{-+}F_r=-\sqrt2\,F_r
\ \xrightarrow{\text{aux shell (4C.18)}}\
-\varepsilon_{rst}\,(\widetilde\phi_s\times\widetilde\phi_t)
=-\varepsilon_{rst}\,\mathfrak c^s\times\mathfrak c^t,\\
\delta_-\mathfrak f&=\tau_E^{-1}\delta_-
(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+|)
\ \propto\ \mathcal D_{+\dot a}\widetilde\lambda^{\dot a}
=\mathcal D_{+\dot a}\,\mathfrak d^{\dot a},
\end{aligned}}
\tag{5D.3}
$$

i.e. exactly the twisted classical cocycle structure: $\mathfrak c,\mathfrak d$ are
$\delta_-$-closed off shell; $\delta_-\mathfrak b\propto$ auxiliary $F$ (off shell) $\to
\mathfrak c\mathfrak c$-bracket (on the auxiliary shell); $\delta_-\mathfrak
f\propto\mathcal D_{+}\mathfrak d$. This is the component realization of the review
observation (R.0): tree-level contact terms among letters are the classical
$Q_0$-bracket, and the quantum content of the Ward identity is everything beyond (5D.3).

## 3. The insertion: $\partial_\mu j^\mu_-$ in EOM-proportional form

Set $a=-$ in the Step-5C off-shell divergence identities (5C.15)/(5C.16). Euclidean
($\epsilon_{-b}$ nonzero only for $b=+$, $\epsilon_{-+}=+1$):

$$
\boxed{
\begin{aligned}
\partial_m j^{m}_{E,-}
=\operatorname{tr}_\kappa\Big\{&
-\,\mathcal E_{E,A}^{n}\,(\sigma_{En}\widetilde\lambda)_-
+i\,\mathcal E_{E,\mathscr D}\,(\sigma_E^n\mathcal D_n\widetilde\lambda)_-
+\big[(\sigma_E^{np})_b{}^c\epsilon_{-c}F_{np}
+i\epsilon_{b-}\mathscr D\big]\,\mathcal E_{E,\lambda}^{b}\\
&+\sqrt2\,\mathcal E_{E,\phi_r}\,\psi_{r-}
+\sqrt2\,F_r\,\mathcal E_{E,\psi_r}^{+}\,\epsilon_{-+}
-\sqrt2\,(\sigma_E^m)_{-\dot a}(\mathcal D_m\widetilde\phi_r)\,
\mathcal E_{E,\widetilde\psi_r}^{\dot a}\\
&+\Big[\sqrt2\,(\sigma_E^m\mathcal D_m\widetilde\psi_r)_-
-2(\lambda_-\times\widetilde\phi_r)\Big]\,\mathcal E_{E,\widetilde F_r}
\Big\},
\end{aligned}}
\tag{5D.4}
$$

and the Lorentzian mirror from (5C.15). Every term is *(typed EOM operator)* $\times$
*(local coefficient)*; this is the exact insertion used below. Note which channels each
term feeds: the $\mathcal E_\lambda$-term carries $f_{ab}$ and $\mathscr D$ coefficients
(gauge-letter channels), the $\mathcal E_{\psi}$-term carries $F_r$ (matter
$\mathfrak b$-channels), the $\mathcal E_{\widetilde\psi}$-term carries $\mathcal
D\widetilde\phi$ ($\mathfrak c$-channels with a derivative), and the $\mathcal
E_{\widetilde F}$-term feeds the Yukawa-descendant channels.

## 4. The frontal Ward identity

Let $\mathcal O_i(y_i)$ be letter bilinears, $\mathcal O=\mathcal O_1(y_1)\mathcal
O_2(y_2)$, and let $\langle\cdot\rangle$ be the normalized gauge-fixed expectation
(3D.125a)/(3D.125b). The classical identity (5D.4) plus the Schwinger–Dyson identity
(3D.31)/(3D.34) for the gauge-fixed action $S_{\Psi,R}=S_{0,R}+\mathbf s_R\Psi_R$ (3D.77)
give the **frontal component Ward identity**

$$
\boxed{
\big\langle\partial_Mj^{M}_{R,-}(x)\,\mathcal O_1(y_1)\,\mathcal O_2(y_2)\big\rangle
=-\tau_R^{-1}\sum_{i=1,2}\delta^4(x-y_i)\,
\big\langle\cdots(\delta_-\mathcal O_i)(y_i)\cdots\big\rangle
+\mathfrak G_{R,-}(x;y_1,y_2)
+\mathfrak A_{R,-}(x;y_1,y_2),}
\tag{5D.5}
$$

with the three terms on the right produced by the three distinct mechanisms:

1. **Contact terms** ($\delta_-\mathcal O_i$): from the classical Euler operators
   $\mathcal E^{S_0}_X$ in (5D.4) written as $\mathcal E^{S_\Psi}_X-\mathcal
   E^{\mathbf s\Psi}_X$ and the SD collapse of $\mathcal E^{S_\Psi}_X(x)$ against every
   $X(y_i)$ inside $\mathcal O_i$: unregulated, $\langle\mathcal
   E^{S_\Psi}_X(x)\,X(y)\rangle$-pairings produce $-\tau_R^{-1}\delta^4(x-y)$ times the
   removal of that leg ($K\,K^{-1}=\delta$). The coefficients assemble to precisely
   $\delta_-\mathcal O_i$ — the tree/cocycle layer (5D.3).
2. **Gauge-sector remainder** $\mathfrak G_{R,-}$: the $\mathcal E^{\mathbf
   s\Psi}_X\delta_-X$ pieces (the manifest SUSY does not preserve the gauge fermion).
   These are $\mathbf s_R$-exact insertions up to ghost-EOM terms; for gauge-invariant
   letters they contribute only through ghost/gauge-fixing loop graphs, and the method
   requires them to be enumerated in every channel's census (they are the component
   mirror of the superspace program's gauge-BRST-typed terms — separately typed, never
   merged into the anomaly).
3. **Anomaly candidate** $\mathfrak A_{R,-}$: zero in any regularization satisfying
   simultaneously (i) $\delta S/\delta v\leftrightarrow\delta/\delta v$, (ii)
   $KK^{-1}=\delta$, (iii) four-dimensional spinor algebra. Under DRED, (iii) is
   four-dimensional while the propagator inverse in (ii) is $d$-dimensional, so each SD
   collapse is a *regulated* delta and fails by exactly one universal evanescent
   insertion per marked line,
   $$
   \frac{\bar r_e^{\,2}}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}
   =\frac{\mu_\ell^2}{D_0D_1D_2},
   \qquad \mu_\ell^2:=\bar\ell^2-\ell_d^2,
   \tag{5D.6}
   $$
   with no graph-specific $(4-d)$ factors. $\mathfrak A$ is therefore computed by the
   evanescent master integral
   $\lim_{\epsilon\to0}\mu^{2\epsilon}\!\int\!\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
   \frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}=\frac1{32\pi^2}$ — local (polynomial in
   external momenta) because the $\Delta$-dependence enters only at $O(\epsilon)$.
   [(5D.6) and the master integral are independently re-derived in
   `proposals/step5-independent-physics-review-2026-07-16.md` (R.1)–(R.2); the project
   settlement re-derives them as authority; this memo imports neither as authority.]

## 5. Method requirement list (the DRED ledger, component form)

Identical to the superspace program's regulator ledger, restated for component graphs:
$d=4-2\epsilon$ with loop momenta strictly $d$-dimensional; all $\sigma$-chains and
frame projections ($+,-$ indices) strictly four-dimensional; the two metric
representations never contracted with each other; the single evanescent insertion
$\mu_\ell^2$; all momenta incoming (5B.D3); Lorentzian channel carries the (5B.D3)
Feynman cycle. This ledger is a **settlement-contract lock**, not this memo's decision;
the component method consumes it unchanged.

## 6. Component Feynman rules consumed by the method

From (4C.14)/(4C.42a) + §1 gauge fixing, all derivable in one page each and consistent
with the superspace rules of the Step-5B memo under component projection:

- **Propagators** (Feynman gauge, momentum space, all incoming; L with
  $p^2\to p_L^2-i\varepsilon$): $\langle A_M^AA_N^B\rangle_R\propto
  (-\tau_R^{-1})\,g^2\kappa^{AB}\,\delta_{MN}/p^2$-type from
  $S^{(2)}=\eta_R\frac h2\int A\Box A$ (5B.15);
  $\langle\lambda^a\widetilde\lambda^{\dot b}\rangle_R$,
  $\langle\psi_r\widetilde\psi_s\rangle_R\propto\delta_{rs}$ from the kinetic terms of
  (4C.14)/(4C.42a); $\langle\phi_r\widetilde\phi_s\rangle_R\propto\delta_{rs}/p^2$;
  auxiliary contact propagators $\langle\mathscr D\mathscr D\rangle$,
  $\langle F_r\widetilde F_s\rangle\propto\delta_{rs}\times$const (no pole) if
  auxiliaries are kept; ghost propagator from $\bar c\,\Box c$.
- **Vertices**: the ordered functional derivatives of (4C.14)/(4C.42a) — gauge
  self-couplings, $A$-matter minimal couplings and seagulls, the two Yukawa families,
  the $\mathscr D$- and $F$-linear couplings ($i\mathscr D(\phi\times\widetilde\phi)$,
  superpotential $F\phi\phi$), the quartic scalars, ghost–gauge vertex — all with the
  (5A.61)–(5A.63) ordering, Koszul signs, and graph weight, which are
  representation-independent.
- **Insertion vertices**: the terms of (5D.4) — each a two- or three-field local operator
  carrying one EOM-typed leg — and the letter bilinears $\mathcal O_i$.

## 7. The pipeline (mirror of the superspace workflow)

For each ordered channel $(\mathcal O_1,\mathcal O_2)$ from the 81-ledger:

1. **Selection rules first** (the owner's rule: constrain by conserved quantities before
   drawing): $SU(3)$ flavor, Grassmann parity, twisted dimension
   ($[\mathfrak c]=1$, $[\mathfrak b]=[\mathfrak d]=\tfrac32$, $[\mathfrak f]=2$,
   $[\mathcal D_{+\dot a}]=1$), and the bilinear output structure forced by the
   $\sigma$-chain — the component transcription of review §R.4, to be re-derived
   project-side; expected census: 29 nonzero / 52 zero ordered channels.
2. **Graph census**: all one-loop topologies connecting (5D.4) to the two bilinears:
   triangles, plus the same-order contact graphs generated by (i) the multi-field terms
   of (5D.4), (ii) letter-expansion (covariant derivatives and $f_{ab}$ inside letters
   contain $A$-legs), (iii) ghost loops from $\mathfrak G_{R,-}$, (iv) seagulls. Absent
   topologies must be proved absent from the typed vertex grammar, never assumed.
3. **Collapse bookkeeping**: apply the SD collapse to every EOM-typed leg; the
   unregulated identity must close on the contact terms (tree check of (5D.5) per
   channel — an exact, finite computation).
4. **Evanescent isolation**: in the regulated graphs replace each collapse failure by the
   $\mu_\ell^2$ insertion (5D.6); tensor-reduce with four-dimensional frame algebra;
   Feynman-parametrize; only the $\mu^2$-master-integral terms survive the
   $\epsilon\to0$ limit as the local anomaly.
5. **Cross-checks per channel**: pole cancellation before the finite remainder is read;
   the $-2\epsilon$ evanescent trace mechanism
   ($p^\rho\breve\delta^{mn}(\sigma_m\bar\sigma_\rho\sigma_n)=-2\epsilon\,\sigma\!\cdot\!p$,
   review R.3) as the source of finite anomaly from $1/\epsilon\times\epsilon$;
   comparison with the superspace-route channel result (independent-route agreement).

**Seed channel** ($\mathfrak f,\mathfrak f$), the component mirror of the superspace
$(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+,\boldsymbol\nabla_+\boldsymbol{\mathcal
W}_+)$ seed: insertion terms feeding it are the $\mathcal E_\lambda\cdot f$ and
$\mathcal E_A\cdot\sigma\widetilde\lambda$ terms of (5D.4); the one-loop family is the
gaugino triangle with two $f_{++}$ letters, the $A$-leg letter-expansion contacts, and
the ghost-sector graphs of $\mathfrak G$; the expected output structure is
$\partial_{\dot a}X\,\partial^{\dot a}Y$-type with coefficient governed by the
$\tfrac1{32\pi^2}$ master integral. Executing steps 2–5 for this channel end-to-end is
the designated first computation of the settlement phase (it must reproduce the
superspace AA-seed).

## 8. Exact-check surface for this memo

The classical layer of the method is fully covered by the Step-5C checks (B1–B4): (5D.4)
is a slot restriction of (5C.15)–(5C.16). The frame/letter layer adds two finite checks
(to be included with the B-suite): (i) the $\delta_-$-cocycle table (5D.3) from
(5C.2)/(5C.3) with (5D.D4); (ii) $\epsilon_{-+}=+1$-consistency of every slot restriction
in (5D.4). The regulated layer (steps 4–5) is settlement-contract scope.

## 9. What this memo does not claim

No evaluated one-loop coefficient; no census completeness proof (that is the dedicated
adversarial-review item of the settlement, cf. review R.6-3); no adoption of the
holomorphic-twist external target normalizations (dictionary work of the settlement
task). The method above is complete in the sense that every remaining step is a bounded,
typed computation with locked inputs.
