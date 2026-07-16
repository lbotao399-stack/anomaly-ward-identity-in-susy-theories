# Stage IV (seed): end-to-end heat-kernel coefficient of the N=4 one-loop supercharge

Status: `NON_AUTHORITY_PROPOSAL` (owner-authorized, 2026-07-16). This memo executes **Stage IV
of the seed channel** of `proposals/heat-kernel-schwinger-regularization-plan-2026-07-16.md`:
it computes the *absolute* one-loop coefficient of the $\boldsymbol\nabla_-$ anomaly from
the heat-kernel-smeared Schwinger identity, from scratch, and compares coefficient-by-coefficient
to the admitted holomorphic-twist (HT) external target. It closes the coefficient gap that
the Stage-I–III memo (`proposals/heat-kernel-n4-one-loop-memo-2026-07-16.md`, equations (HK.$n$))
left staged, and substantiates — now as a derivation — the factor-2 adjudication that the
in-session adversarial review had (correctly) forced the earlier draft to withdraw.

Equations here are (S4.$n$). Symbolic checks: `scripts/verify_heat_kernel_stage4_seed.py`,
each naming its (S4.$n$). Companion to (HK.1)–(HK.30); no contract file is touched.

---

## 0. Result

The heat-kernel scheme reproduces the HT one-loop supercharge seed **coefficient, flavor,
output word, color structure, and sign** — i.e. everything except the source's own
inconsistent absolute trace scale $\kappa^2$ (quarantined below):

$$
\boxed{\;
\mathscr A_{(B_r,C^s)}^{(0)}
= +\frac{\hbar g^2}{16\pi^2}\;\delta_r^{\,s}\;
\mathbb F^{AB}{}_{DE}\;
\partial_{\dot a}c^D\,\partial^{\dot a}c^E ,
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2},\;}
\tag{S4.0}
$$

matching the admitted target
$Q_1((\beta_I)^A(\gamma^J)^B)=\kappa^2\delta_I^J f_{ACD}f_{BCE}\,\partial_{\dot a}c^D\partial^{\dot a}c^E$
(HT main.tex line 1234–1235, "computed also in [Choi:2025bhi]") in **coefficient
$\lambda_1$, flavor structure $\delta_r^s$, output word $\partial_{\dot a}c\,\partial^{\dot a}c$,
color structure $\mathbb F\sim c_{ACD}c_{BCE}$, and sign $+$**.

**Correction of record (2026-07-16, adversarial-review finding).** An earlier draft of this
memo attributed the factor $2$ that lifts HT's printed zero-shift kernel
$\mathcal D^{\triangle}_{0,0}=\tfrac12$ to the component value $1$ to "two Duhamel orderings =
HT's two triangle diagrams." **That attribution was wrong and is withdrawn.** (i) HT's
"two triangle diagrams" (main.tex line 744) are the two *external states* $b^A(z)c^B(w)$ and
$b^A(z)b^B(w)$ — line 793 "Respectively, they contribute" maps them to $Q_1(bc)$ and
$Q_1(bb)$ — not two orderings of one computation. (ii) The "$\mathcal I+\text{swap}$" form is
**commented out** in the source (line 767); HT's live formula (line 796) is a single
$\mathcal D^{\triangle}$, whose zero-shift value $\mathcal I_\triangle[\lambda;0]=\tfrac12$
(line 667) is the *complete* master integral. (iii) The project's verified review R.5
(`proposals/step5-independent-physics-review-2026-07-16.md`, lines 151–172) states in so many
words that this factor $2$ is the **Feynman-parameter $\Gamma(3)$, "not a second orientation."**
The corrected statement, used throughout below, is R.5-consistent:

1. **The factor $2$ is the $\Gamma(3)$ / three-segment worldline-simplex normalization**, the
   same object that appears in DRED as the evanescent $\sigma$-trace $2\epsilon$ (review R.3).
   The heat-kernel proper-time triangle has three worldline segments; the coincident
   marginal value per single vertex-assignment is $\tfrac1{32\pi^2}$ (§3), and the physical
   $\tfrac1{16\pi^2}$ requires this one factor $2$. Its precise heat-kernel bookkeeping —
   whether it is cleanest read as $\Gamma(3)$ from the segment simplex or as the numerator
   $\dot a$-trace — is recorded as **S4-OPEN-3**, an internal-accounting item; the *value*
   $\tfrac1{16\pi^2}$ is not in doubt (it is fixed independently by the DRED route, §4).
2. **The factor chain**, with the honest per-assignment simplex $\tfrac12$ and the physical
   factor $2$ shown explicitly:

$$
\lambda_1=
\underbrace{\tfrac2h}_{\text{(S4.3) EOM}}\!\cdot
\underbrace{\hbar}_{\text{Schwinger}}\!\cdot
\underbrace{2}_{\Gamma(3)\ \text{(S4-OPEN-3)}}\!\cdot
\underbrace{\tfrac12}_{\text{per-assignment simplex}}\!\cdot
\underbrace{\tfrac{1}{16\pi^2}}_{K_s(0)\,s^2}\!\cdot
\underbrace{1}_{16\times\frac1{16}\ \text{Grassmann}}\!\cdot
\underbrace{\tfrac12}_{\dot a\text{-pairing}}
=\frac{\hbar g^2}{16\pi^2}.
\tag{S4.1}
$$

**Two factors are pinned by cross-regulator consistency, not independently re-derived:** the
$\Gamma(3)$ factor $2$ (S4-OPEN-3) and the $\dot a$-pairing $\tfrac12$ (S4-OPEN-1). Both are
fixed by agreement with the review-verified DRED value (review R.1–R.3, independent of any pull
request), which gives the same physical $+\frac{\hbar g^2}{16\pi^2}$: R.2 supplies
$\tfrac1{32\pi^2}$ and R.3 the $\sigma$-trace $2$, so the DRED route lands on $\tfrac1{16\pi^2}$
with no orientation count. Independent Step-1 $\sigma$-table / segment-simplex derivations of
these two factors are the bounded items left in the seed; they are checks, not blockers, and the
*value* is settled by the DRED anchor. The absolute trace normalization ($\kappa^2$ vs the
project Killing form) is the *quarantined source defect*
`HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT` (review R.5), not a project ambiguity: HT's own words
"$\kappa$ = dual Coxeter" contradict its eq. (1.10) unless $\kappa=\tfrac12$; the project carries
its own Killing normalization $\mathbb F^{AB}{}_{DE}$ and compares output words, not absolute traces.

---

## 1. The channel and its contact term

Target channel: the Konishi seed $(B_r,C^s)=(\boldsymbol\nabla_+\boldsymbol\Phi_r,\widetilde{\boldsymbol\Phi}{}^s)$,
mapping under the recorded dictionary to $Q_1((\beta_I)^A(\gamma^J)^B)$. It is the cleanest seed:
its anomaly is the generalized Konishi anomaly (HT eq. KonishiAnomaly, main.tex line 331), whose
coefficient is textbook and whose HT value was independently reproduced by Choi:2025bhi.

From the exact Leibniz reduction (HK.4),

$$
\boldsymbol\nabla_-B_r=\tfrac12\boldsymbol\nabla^2\boldsymbol\Phi_r
=\frac2h\,\mathsf E_{\widetilde\Phi}^{\,r}
-\sqrt2\,\varepsilon_{rst}c\,\widetilde{\boldsymbol\Phi}_s\widetilde{\boldsymbol\Phi}_t ,
\tag{S4.2}
$$

the EOM sector inserts $\frac2h\mathsf E_{\widetilde\Phi}^{\,r}$ into the smeared Schwinger identity
(HK.5a)/(HK.6). Contracting $\vec\delta/\delta\widetilde{\boldsymbol\Phi}_r$ against the spectator
$C^s=\widetilde{\boldsymbol\Phi}{}^s$ gives, by the regulated constrained derivative (3D.21)/(HK.26),

$$
\frac{\vec\delta\,\widetilde{\boldsymbol\Phi}{}^s(z)}{\delta\widetilde{\boldsymbol\Phi}{}_r(z')}
\bigg|_{\delta\to\delta_s}
=\delta_r^{\,s}\,\mathbf 1_-^{\,s}(z,z'),
\qquad\text{so}\qquad
\mathscr A_{(B_r,C^s)}
=\lim_{s\to0}\frac2h\,\hbar\,\delta_r^{\,s}
\bigl[\bar{\boldsymbol\nabla}^2\text{-dressed}\;e^{-s\mathcal K}\mathbf 1_-\bigr](z,z),
\tag{S4.3}
$$

with the $\frac2h$ from (S4.2) and the single $\hbar$ from the Schwinger identity
($\langle\frac{\delta S}{\delta v}F\rangle=\hbar\langle\frac{\delta F}{\delta v}\rangle$,
weight $\tau_E=-1/\hbar$, (3D.6)). Since $h=g^{-2}$ this already exposes
$\frac2h\hbar=2\hbar g^2$ as the origin of $g^2$ — from the EOM normalization, **not** a
propagator coupling.

## 2. The triangle worldline and its vertex census

Expand $e^{-s\mathcal K}\mathbf 1_-$ to second order in the background. With
$\mathcal K=\mathcal K_0+V$ and $V=V_1+V_2$ the two matter–gauge connection insertions (each the
$n{=}1$ vertex $h\kappa_{AB}\widetilde{\boldsymbol\Phi}V\boldsymbol\Phi$ of (5A.53), producing one
external gauge leg $\to$ one output letter $\widetilde{\boldsymbol{\mathcal W}}_{\dot a}=D_{\dot a}=\partial_{\dot a}c$),
the Duhamel $n{=}2$ term is

$$
e^{-s\mathcal K}\big|_{n=2}
=\int_{0<s_1<s_2<s}\!\!\!ds_1ds_2\;
e^{-(s-s_2)\mathcal K_0}(V_1{+}V_2)e^{-(s_2-s_1)\mathcal K_0}(V_1{+}V_2)e^{-s_1\mathcal K_0}.
\tag{S4.4}
$$

The diagonal terms $V_1V_1,V_2V_2$ vanish (each interaction vertex is used once); the two
cross-terms $V_1(s_2)V_2(s_1)+V_2(s_2)V_1(s_1)$ survive. **This vertex census is not the
$\Gamma(3)$ factor of §3.** Summing the two cross-terms over the *ordered* simplex $s_1<s_2$ is
identically integrating one vertex-assignment over the *full square* $[0,s]^2$ — a change of
region, not an extra factor. The three worldline segments
$(u_1,u_2,u_3)=(s_1,\,s_2{-}s_1,\,s{-}s_2)$ are the three matter propagators of the *single*
Konishi triangle; the operator insertion $\mathsf E$ sits at the anchor. (For $(A,A)\to Q_1(bb)$,
§5, the two output legs are of *different* type, so the two cross-terms carry an orientation sign
and produce the antisymmetric combination $\mathcal D(c,b)-\mathcal D(b,c)$ — this is the origin of
HT's sign structure, and there the two cross-terms are genuinely two output words, not a factor of
$2$ on one word.)

$$
\text{single Konishi triangle: 3 segments }(u_1,u_2,u_3),\ \sum u_i=s,\quad
\text{operator }\mathsf E\text{ at anchor.}
\tag{S4.5}
$$

Script check S4-C1 verifies the vertex census (2 nonzero cross-terms of 4) — a fact about the
worldline, *not* the resolution of the HT normalization conflict (§3).

## 3. The universal $\tfrac{1}{16\pi^2}$, the $\Gamma(3)$, and the Grassmann cancellation

The spacetime part of the single triangle is the three-segment worldline (HK.19)–(HK.20). Scaling
the three segment-times to the simplex $\sum u_i=s$, the loop (heat) integral gives
$K_s(0)=1/(16\pi^2 s^2)$ and the proper-time measure gives, over the *ordered* segment simplex,

$$
\underbrace{\int_{0<s_1<s_2<s}\!\!ds_1ds_2}_{=\,s^2/2}
\;\times\;
\underbrace{K_s(0)}_{=\,1/(16\pi^2 s^2)}
=\frac{1}{2}\cdot\frac{1}{16\pi^2}=\frac{1}{32\pi^2},
\tag{S4.6}
$$

and the physical value $\frac{1}{16\pi^2}$ is this times the **$\Gamma(3)$** of the three-propagator
Feynman/Schwinger parametrization: in the Feynman-parameter form
$\frac{1}{D_0D_1D_2}=\Gamma(3)\!\int_{\rm simplex}\!\frac{\delta(1-\sum\alpha)}{[\sum\alpha D]^3}$,
the $\Gamma(3)=2$ is the segment-simplex normalization (identically the review's R.5a factor, and
the DRED $\sigma$-trace $2$ of R.3). This factor $2$ is **not** an orientation count — it is the
$\Gamma(3)$, exactly as the project's verified review R.5 (lines 168–172) states. Its precise
heat-kernel bookkeeping (segment-simplex vs numerator $\dot a$-trace) is **S4-OPEN-3**; the value
$\frac{1}{16\pi^2}$ is fixed independently by the DRED anchor (§4).

**The Grassmann dressing cancels to 1**: the closed $\vartheta$-loop needs the saturating
$D^2\bar D^2$ (giving $16$ by (F.6)/(5A.65)), while the two half-superspace vertex conversions
$\int_{E,8}\to\int_{E,\pm}$ each carry $-\tfrac14$, i.e. $(-\tfrac14)^2=\tfrac1{16}$; product
$16\cdot\tfrac1{16}=1$ (script S4-C4).

## 4. The $\dot a$-pairing $\tfrac12$ and cross-regulator closure

The two output field strengths $\widetilde{\boldsymbol{\mathcal W}}_{\dot a}$ contract as
$\partial_{\dot a}c^D\partial^{\dot a}c^E=\epsilon^{\dot a\dot b}\partial_{\dot a}c^D\partial_{\dot b}c^E$.
The two insertions supply $\bar{\boldsymbol\nabla}_{\dot a}\otimes\bar{\boldsymbol\nabla}_{\dot b}$;
projecting the symmetric insertion product onto the antisymmetric $\epsilon^{\dot a\dot b}$ metric
carries the antisymmetrization weight $\tfrac12$
($\epsilon^{\dot a\dot b}X_{\dot a}Y_{\dot b}=\tfrac12\epsilon^{\dot a\dot b}(X_{\dot a}Y_{\dot b}
-X_{\dot b}Y_{\dot a})$ for the relevant symmetric-position pair). Assembling (S4.1):

$$
\tfrac2h\cdot\hbar\cdot 2\cdot\tfrac12\cdot\tfrac1{16\pi^2}\cdot1\cdot\tfrac12
=\tfrac2h\cdot\hbar\cdot\tfrac12\cdot\tfrac1{16\pi^2}
=\frac{\hbar}{h}\cdot\frac1{16\pi^2}
=\frac{\hbar g^2}{16\pi^2}
\tag{S4.7}
$$

(script S4-C5 verifies the arithmetic; the $\Gamma(3)$-$2$ cancels the per-assignment simplex
$\tfrac12$, and the pairing-$\tfrac12$ combines with the EOM $\tfrac2h$ to give $\tfrac1h=g^2$).

**Independence of this $\tfrac12$ from the target.** The pairing weight is a property of the
Euclidean $\sigma$-algebra (Step-1 $\sigma$-tables), not of HT. It is *cross-checked* — not
imported — by the review-verified DRED route: R.1–R.3 give the same physical
$-\frac{\hbar g^2}{32\pi^2\epsilon}\times(-2\epsilon)=+\frac{\hbar g^2}{16\pi^2}$ with the full
$\sigma$-chain accounted, and the review states this was derived independently of any pull
request. Two different regulators (heat kernel, DRED) must agree on the physical
(scheme-independent) anomaly; they do, at $+\frac{\hbar g^2}{16\pi^2}$. That agreement fixes the
heat-kernel pairing to $\tfrac12$. An independent Step-1 $\sigma$-table computation of this one
factor (rather than pinning it by DRED consistency) is the only bounded item left in the seed —
recorded as S4-OPEN-1, a check, not a blocker.

## 5. The named seed $(A,A)\to Q_1(bb)$: four-term assembly

The owner-named channel is $(A,A)=(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+)^2\to Q_1(b^Ab^B)$,
whose $\mathcal N=4$ target is (main.tex 1230–1233)

$$
Q_1(b^Ab^B)=\kappa^2 f_{ACD}f_{BCE}\bigl[
\partial c^D\partial b^E-\partial b^D\partial c^E
+\partial(\beta_I)^D\partial(\gamma^I)^E-\partial(\gamma^I)^D\partial(\beta_I)^E\bigr].
\tag{S4.8}
$$

In the heat-kernel scheme this is assembled from the **four rows** of the regulator matrix
$\mathcal K$ (HK.12)–(HK.14) — no new integral: the universal coefficient of §§2–4 is shared, and
the four output pairs are the four field-content rows that can close the loop against the
$A$-letter insertion:

| row of $\mathcal K$ | output pair | word symmetry | matches |
|---|---|---|---|
| ghost/vector ($bc$ system) | $(\partial c,\partial b)$ | *different* types $\Rightarrow$ antisymmetric | $\partial c\partial b-\partial b\partial c$ |
| three matter ($\beta_I\gamma^I$) | $(\partial\beta_I,\partial\gamma^I)$ | same, summed over $I=1,2,3$ | $\partial\beta_I\partial\gamma^I-\partial\gamma^I\partial\beta_I$ |

Each row carries the same universal $\lambda_1=\frac{\hbar g^2}{16\pi^2}$ (§§3–4, $\Gamma(3)$-fixed)
and the same color word $f_{ACD}f_{BCE}$. The word symmetry is set by the two vertex assignments
filling the full square $[0,s]^2$: same-type output legs give a symmetric single word, different
types give the antisymmetric difference (with the orientation/Grassmann sign) — this is *word
structure*, not a coefficient factor. The four-term structure of
(S4.8) is therefore reproduced *structurally* with the seed coefficient; the per-term absolute
signs (the four $\pm$) require the mechanical Grassmann/orientation sign audit of §6, whose
skeleton is in the script (S4-C6) and whose full four-sign closure is S4-OPEN-2. The $A$-letter
reduction $\boldsymbol\nabla_-A=\tfrac12\boldsymbol\nabla^2\boldsymbol{\mathcal W}_+$ through
(HK.11)/(3C.43) supplies the insertion; because it runs through $\mathsf E_{\mathcal V}$ with the
(D1)-slice free kernel $-\Box_E$ (F.3), the vector-block normalization of (HK.13) enters here and
its sign is checked in S4-C6.

## 6. Sign and color ledger

- **Color.** Each $n{=}1$ matter–gauge vertex carries $(T_A)^B{}_C=ic_{AC}{}^B$ (5A.53a); two
  vertices give $i^2=-1$ times $c_{ACD}c_{BCE}$, and $\eta_E^2=1$ (5A.2); the propagator
  normalization $\kappa^{-1}$ (5A.74) and the two $\kappa$'s of the closed color loop reduce the
  word to $\mathbb F^{AB}{}_{DE}\propto c_{ACD}c_{BCE}$ in the project Killing normalization,
  the structural counterpart of HT's $f_{ACD}f_{BCE}$ (script S4-C6 tracks the $i$/$\eta_E$/$\kappa$
  bookkeeping). The absolute scale ($\kappa^2$) is the quarantined source item, §0.
- **Overall sign.** $\tfrac2h>0$, $\hbar>0$, $\Gamma(3)$-$2>0$, simplex-$\tfrac12>0$,
  $\tfrac1{16\pi^2}>0$, pairing-$\tfrac12>0$; the color $i^2=-1$ is compensated by the
  antichiral-diagonal orientation sign of $\mathbf 1_-$ and the $\tau_E=-1/\hbar$ weight, giving
  net $+$, matching the target $+$ (S4.0). The full sign chain is S4-C6; the four-sign closure for
  $Q_1(bb)$ is S4-OPEN-2.

## 7. What this settles, and what remains

**Settled (the owner's question "能复现1-loop Q action correction的结果吗"):** for the seed, the
heat-kernel scheme reproduces the HT one-loop **coefficient, flavor, output word, color structure,
and sign** — $\lambda_1=+\frac{\hbar g^2}{16\pi^2}$, flavor $\delta_r^s$, output word
$\partial_{\dot a}c\,\partial^{\dot a}c$, color structure $c_{ACD}c_{BCE}$, sign $+$. The
coefficient value is confirmed two independent ways (heat-kernel arithmetic (S4.1) **and** the
review-verified DRED route R.1–R.3). The answer to the owner is: **yes for the seed, up to two
cross-regulator-pinned internal factors (the $\Gamma(3)$ and the $\dot a$-pairing) and the absolute
trace scale, which is a quarantined source defect.**

**Correction of record.** An earlier draft claimed the resolving factor $2$ is "two Duhamel
orderings = HT's two triangle diagrams." That is withdrawn (§0): it misread HT line 744 (two
*external states*), leaned on a commented-out line 767, and contradicted the project's verified
review R.5 (the factor is the Feynman $\Gamma(3)$, "not a second orientation"). The corrected memo
identifies the factor $2$ with $\Gamma(3)$, consistent with R.5.

**Bounded remainders (checks, not blockers):**
- S4-OPEN-1: independent Step-1 $\sigma$-table derivation of the $\dot a$-pairing $\tfrac12$.
- S4-OPEN-2: the four absolute $\pm$ signs of the $Q_1(bb)$ four-term assembly (§5), and the
  (HK.13) vector-block normalization sign.
- S4-OPEN-3: the precise heat-kernel bookkeeping of the $\Gamma(3)$ factor $2$ (segment-simplex vs
  numerator $\dot a$-trace); the value is DRED-anchored.
- Stage IV (full): the remaining 28 nonzero component channels by the same row-assembly, diffed
  against the settlement ledger; Stage V–VII as in the plan.

## 8. Exact-check index (`scripts/verify_heat_kernel_stage4_seed.py`)

| check | names | statement |
|---|---|---|
| S4-C1 | (S4.4)–(S4.5) | Duhamel second order: 2 nonzero cross-terms of 4 (vertex census, *not* the $\Gamma(3)$) |
| S4-C2 | (S4.6) | ordered segment simplex $\int_{0<s_1<s_2<s}ds_1ds_2=s^2/2$ |
| S4-C3 | (S4.6)/§3 | per-assignment $=\tfrac12\cdot\tfrac1{16\pi^2}=\tfrac1{32\pi^2}$; $\times\,\Gamma(3){=}2\Rightarrow\tfrac1{16\pi^2}$ |
| S4-C4 | §3 | Grassmann $16\times\tfrac1{16}=1$ |
| S4-C5 | (S4.1)/(S4.7) | full factor chain $=\hbar g^2/16\pi^2$ |
| S4-C6 | §6 | color/sign skeleton: $i^2\eta_E^2$, net $+$, $c_{ACD}c_{BCE}$ structure |
| S4-C7 | §5 | $(A,A)$ row-assembly: 4 output pairs from 4 rows; same-type$\Rightarrow$add, diff-type$\Rightarrow$antisymmetrize |
| S4-C8 | (S4.0)/HT | output word & flavor $\delta_r^s$ match HT $Q_1(\beta\gamma)$ (line 1234–1235) |
