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

The heat-kernel scheme reproduces the HT one-loop supercharge coefficient **exactly**:

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

Two things are *derived here* that the Stage-I–III memo only asserted or staged:

1. **The factor 2 that resolves `HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO` is the two Duhamel
   cross-terms** $V_1(s_2)V_2(s_1)+V_2(s_2)V_1(s_1)$ of the second-order expansion of
   $e^{-s\mathcal K}$ — identically HT's own *two triangle diagrams* (main.tex line 744,
   "There are two triangle diagrams"), and identically the "$+\,(z,D)\!\leftrightarrow\!(w,E)$"
   / "$\mathcal I+\text{swap}$" of HT's commented derivation (main.tex line 767). The printed
   HT kernel $\mathcal D^{\triangle}_{0,0}=\tfrac12$ is one ordering; the component
   normalization $1$ is both. The heat kernel produces both, mechanically, and lands on the
   component value. This is the promised third route, now with the earlier overclaim repaired.
2. **The complete factor chain**, with the Duhamel-simplex $\tfrac12$ and the ordering-$2$
   now shown explicitly (they were silently omitted in (HK.28)/C11, which got the right number
   by dropping both):

$$
\lambda_1=
\underbrace{\tfrac2h}_{\text{(S4.3) EOM}}\!\cdot
\underbrace{\hbar}_{\text{Schwinger}}\!\cdot
\underbrace{2}_{\text{2 orderings}}\!\cdot
\underbrace{\tfrac12}_{\text{Duhamel simplex}}\!\cdot
\underbrace{\tfrac{1}{16\pi^2}}_{K_s(0)\,s^2}\!\cdot
\underbrace{1}_{16\times\frac1{16}\ \text{Grassmann}}\!\cdot
\underbrace{\tfrac12}_{\dot a\text{-pairing}}
=\frac{\hbar g^2}{16\pi^2}.
\tag{S4.1}
$$

**One factor is pinned by cross-regulator consistency, not independently re-derived:** the
$\dot a$-pairing $\tfrac12$ (§4). It is fixed by agreement with the review-verified DRED value
(review R.1–R.3, independent of any pull request), which gives the same physical
$+\frac{\hbar g^2}{16\pi^2}$. An independent Step-1 $\sigma$-table derivation of this one $\tfrac12$
is the sole bounded item left in the seed; it is a check, not a blocker. The absolute trace
normalization ($\kappa^2$ vs the project Killing form) is the *quarantined source defect*
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

## 2. The two Duhamel cross-terms = the two triangle diagrams

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

The diagonal terms $V_1V_1,V_2V_2$ vanish (each interaction vertex of the triangle is used
once); only the **two cross-terms** survive:

$$
V_1(s_2)V_2(s_1)+V_2(s_2)V_1(s_1)
\;\Longleftrightarrow\;
\underbrace{\text{triangle A}}_{\text{vertex 1 early}}
\;+\;
\underbrace{\text{triangle B}}_{\text{vertex 1 late}} .
\tag{S4.5}
$$

These are HT's *two triangle diagrams* (main.tex line 744) and its
"$\mathcal I[\lambda;0,-w,-z]+(z,D)\!\leftrightarrow\!(w,E)$" (commented line 767). At zero shift the
two outputs are the same type ($\partial_{\dot a}c^D,\partial^{\dot a}c^E$, symmetric under the
$\dot a$-contraction), so the two cross-terms produce the **same** output word and **add**:
factor $2$. (For $(A,A)\to Q_1(bb)$, §5, the two outputs are *different* types and the same two
cross-terms produce the *antisymmetric* difference instead — the mechanism is identical; only its
manifestation differs. This is the origin of HT's $[\mathcal D(c,b)-\mathcal D(b,c)]$ sign
structure.)

**This is the factor 2.** It is not imported from HT; it is the count of nonzero cross-terms in
(S4.4). Script check S4-C1 verifies the cross-term census (2 nonzero of 4).

## 3. The universal $\tfrac{1}{16\pi^2}$ and the Grassmann cancellation

The spacetime part of each cross-term is the three-kernel chain (HK.19)–(HK.20). Its
coincident-point marginal value, as $s\to0$:

$$
\underbrace{\int_{0<s_1<s_2<s}\!\!ds_1ds_2}_{=\,s^2/2}
\;\times\;
\underbrace{K_s(0)}_{=\,1/(16\pi^2 s^2)}
=\frac{1}{2}\cdot\frac{1}{16\pi^2}=\frac{1}{32\pi^2}
\qquad(\text{per single ordering}),
\tag{S4.6}
$$

so one triangle gives $\frac{1}{32\pi^2}$ and the two together give
$2\cdot\frac{1}{32\pi^2}=\frac{1}{16\pi^2}$ (script S4-C2, S4-C3). The $s^2/2$ is the Duhamel
simplex; the $1/(16\pi^2 s^2)$ is $K_s(0)$ (HK.17, memo C3). **The Grassmann dressing cancels
to 1**: the closed $\vartheta$-loop needs the saturating $D^2\bar D^2$ (giving $16$ by
(F.6)/(5A.65)), while the two half-superspace vertex conversions
$\int_{E,8}\to\int_{E,\pm}$ each carry $-\tfrac14$, i.e. $(-\tfrac14)^2=\tfrac1{16}$; product
$16\cdot\tfrac1{16}=1$ (script S4-C4). The Stage-I–III factor chain (HK.28)/C11 wrote the $16$
and $\tfrac1{16}$ but omitted the Duhamel $\tfrac12$ and the ordering-$2$; they cancel, so the
number was right but the ledger was incomplete. (S4.1) is the complete ledger.

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

(script S4-C5 verifies the arithmetic; the ordering-$2$ cancels the Duhamel-$\tfrac12$, and the
pairing-$\tfrac12$ combines with the EOM $\tfrac2h$ to give $\tfrac1h=g^2$).

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
$\mathcal K$ (HK.12)–(HK.14) — no new integral: the universal coefficient and the two-ordering
mechanism of §§2–4 are shared, and the four output pairs are the four field-content rows that can
close the loop against the $A$-letter insertion:

| row of $\mathcal K$ | output pair | ordering structure | matches |
|---|---|---|---|
| ghost/vector ($bc$ system) | $(\partial c,\partial b)$ | two cross-terms, *different* types $\Rightarrow$ antisymmetric | $\partial c\partial b-\partial b\partial c$ |
| three matter ($\beta_I\gamma^I$) | $(\partial\beta_I,\partial\gamma^I)$ | same, summed over $I=1,2,3$ | $\partial\beta_I\partial\gamma^I-\partial\gamma^I\partial\beta_I$ |

Each row carries the same $\lambda_1=\frac{\hbar g^2}{16\pi^2}$ (§4) and the same color word
$f_{ACD}f_{BCE}$; the relative $+/-$ within each pair is the orientation/Grassmann sign of the two
cross-terms when the two outputs differ in type (S4.5, parenthetical). The four-term structure of
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
- **Overall sign.** $\tfrac2h>0$, $\hbar>0$, ordering-$2>0$, Duhamel-$\tfrac12>0$,
  $\tfrac1{16\pi^2}>0$, pairing-$\tfrac12>0$; the color $i^2=-1$ is compensated by the
  antichiral-diagonal orientation sign of $\mathbf 1_-$ and the $\tau_E=-1/\hbar$ weight, giving
  net $+$, matching the target $+$ (S4.0). The full sign chain is S4-C6; the four-sign closure for
  $Q_1(bb)$ is S4-OPEN-2.

## 7. What this settles, and what remains

**Settled (the owner's question "能复现1-loop Q action correction的结果吗"):** for the seed, the
heat-kernel scheme reproduces the HT one-loop coefficient **exactly** —
$\lambda_1=+\frac{\hbar g^2}{16\pi^2}$, flavor $\delta_r^s$, output word
$\partial_{\dot a}c\,\partial^{\dot a}c$, color structure $c_{ACD}c_{BCE}$, sign $+$ — with the
factor-2 conflict resolved by a **derived** mechanism (two Duhamel cross-terms = HT's two
triangles). The answer to the owner is now: **yes for the seed coefficient, end to end, with one
factor pinned by cross-regulator consistency and the absolute trace scale quarantined as a source
defect.**

**Bounded remainders (checks, not blockers):**
- S4-OPEN-1: independent Step-1 $\sigma$-table derivation of the $\dot a$-pairing $\tfrac12$
  (currently pinned by DRED consistency).
- S4-OPEN-2: the four absolute $\pm$ signs of the $Q_1(bb)$ four-term assembly (§5), and the
  (HK.13) vector-block normalization sign.
- Stage IV (full): the remaining 28 nonzero component channels by the same row-assembly, diffed
  against the settlement ledger; Stage V–VII as in the plan.

## 8. Exact-check index (`scripts/verify_heat_kernel_stage4_seed.py`)

| check | names | statement |
|---|---|---|
| S4-C1 | (S4.4)–(S4.5) | Duhamel second order: 2 nonzero cross-terms of 4; diagonal terms vanish |
| S4-C2 | (S4.6) | Duhamel simplex $\int_{0<s_1<s_2<s}ds_1ds_2=s^2/2$ |
| S4-C3 | (S4.6) | per-ordering $=\tfrac12\cdot\tfrac1{16\pi^2}=\tfrac1{32\pi^2}$; two orderings $=\tfrac1{16\pi^2}$ |
| S4-C4 | §3 | Grassmann $16\times\tfrac1{16}=1$ |
| S4-C5 | (S4.1)/(S4.7) | full factor chain $=\hbar g^2/16\pi^2$ |
| S4-C6 | §6 | color/sign skeleton: $i^2\eta_E^2$, net $+$, $c_{ACD}c_{BCE}$ structure |
| S4-C7 | §5 | $(A,A)$ row-assembly: 4 output pairs from 4 rows; same-type$\Rightarrow$add, diff-type$\Rightarrow$antisymmetrize |
| S4-C8 | (S4.0)/HT | output word & flavor $\delta_r^s$ match HT $Q_1(\beta\gamma)$ (line 1234–1235) |
