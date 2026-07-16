# Euclidean N=4 superspace Feynman rules and BRST foundations — reviewable memo

Status: `NON_AUTHORITY_PROPOSAL` (Step-5B seed). Purpose: consolidate, in one
human-readable derivation, the Euclidean $\mathcal N=4$ perturbative foundations that the
Step-5 settlement uses, state exactly which pieces are locked, derived, decided, or still
conditional, and give the chirality-sensitive rules explicitly. Numbered equations are
(F.$n$); every project-locked input is cited by its contract tag.

The owner's concern this memo answers (2026-07-16): *"我并不确定我 Euclidean N=4 SYM 的
记号(Feynman rules、BRST quantization)是否建立得非常坚定,尤其是涉及 chiral 的超图
Feynman 规则."*

---

## 1. Status audit: what is already solid, and where the soft spots are

| layer | where | status |
|---|---|---|
| Signature/coupling conventions ($\eta_E=-1$, $\tau_E=-1/\hbar$, $h=g^{-2}$, $c_{ABC}$ antisymmetric; Euclidean $\Phi$ vs $\widetilde\Phi$ independent) | (5A.2) | locked |
| $\mathcal N=4$ action, superpotential coefficient $u=-\sqrt2$ | (4C.4), (4C.12)–(4C.13) | locked |
| Field strengths $\mathcal W_{a}=-\frac18\bar D^2(e^{-\mathcal V}D_ae^{\mathcal V})$, $\widetilde{\mathcal W}_{\dot a}=+\frac18D^2(e^{\mathcal V}\bar D_{\dot a}e^{-\mathcal V})$ | (5A.33) | locked |
| Classical BRST algebra, minimal BV action, CME, QME recursion | (5A.35)–(5A.42f) | locked |
| Non-minimal doublets, gauge fermion $\Psi_{\mathcal F,\mathcal Y}$, Gaussian completion | (5A.43)–(5A.48) | locked |
| All-order coordinate vertex words (gauge BCH words, matter color chains, superpotential, FP ghosts, Koszul rules, graph weight) | (5A.49)–(5A.63) | locked |
| Projector algebra and Fermi–Feynman kernels/propagators | (5A.64)–(5A.74) | **conditional** |
| Local-$\mathcal Y$ BV realization of the FF slice | (5A.75)–(5A.79) | **impossible as stated** (nonlocality theorem) |
| Nielsen–Kallosh branch | (3D.95b)/(3D.96b), (5A.48) | **decided 2026-07-16, lemma to record** (§5) |
| Fourier/all-incoming/DRED ledger | settlement contract §1 | written; locked upon merge |

So the honest answer to "建立得坚定吗": the algebraic and vertex layers are firmly locked;
the *propagator layer* was left `PASS_CONDITIONAL`, and the conditionality is **not** a
gap in the derivation of the kernels — it is the mismatch between the standard
Fermi–Feynman scheme and Step-3D's locality demand on $\mathcal Y$. That mismatch is
resolved by a decision (§2), not by more computation. The remaining genuinely-deferred
items are listed in §8.

## 2. Decision record: the perturbative slice is a scheme definition

Step-3D (3D.88a) requires the gauge-averaging kernel $\mathcal Y$ to be local;
(5A.79) proves the Fermi–Feynman kernel $\mathcal Y_{E,\rm FF}=2g^2\mathcal A_E/\Box_E$ is
nonlocal. Both are correct; together they say the FF slice cannot be *reached* through the
Step-3D local-$\mathcal Y$ gauge fermion. The standard resolution — adopted here as an
owner-authorized scoped decision (2026-07-16) — is:

> **(D1)** For the Euclidean perturbative expansion, the gauge-fixed Gaussian weight is
> *defined* by the quadratic form (F.3) below (equivalently: by averaging the gauge
> conditions (5A.44) with the nonlocal FF weight). Step-3D's locality requirement is
> retained only for the nonperturbative BV-density statements, which are outside the
> perturbative slice. Every graph-level consequence in Step 5 depends only on (F.3)–(F.7).

This is exactly the "fixed FF graph representative" the settlement contract declares in its
§2; (D1) upgrades it from a per-contract declaration to a recorded convention decision.

## 3. Free kernels and propagators (vector representation, Euclidean)

All formulas below are the locked (5A.64)–(5A.74) statements; what this section adds is the
derivation logic a reviewer needs, and the chirality bookkeeping.

**Projector algebra.** With $\Box_E=\delta^{mn}\partial_m\partial_n$,

$$
\mathcal P_+=\frac{\bar D^2D^2}{16\Box_E},\qquad
\mathcal P_-=\frac{D^2\bar D^2}{16\Box_E},\qquad
\mathcal P_T=-\frac{D^a\bar D^2D_a}{8\Box_E},\qquad
\mathcal P_T+\mathcal P_++\mathcal P_-=1,
\tag{F.1}
$$

idempotent and orthogonal by the locked identities
$\bar D^2D^2\bar D^2=16\Box_E\bar D^2$, $D^2\bar D^2D^2=16\Box_ED^2$,
$-D^a\bar D^2D_a=8\Box_E-\tfrac12\{D^2,\bar D^2\}$ (5A.65)–(5A.66).

**Vector sector.** The gauge-invariant quadratic action is the $\mathcal P_T$ piece; the FF
gauge average contributes exactly the missing $\mathcal P_0=\mathcal P_++\mathcal P_-$
piece, so the projectors *sum to the identity* and the kernel becomes a plain
d'Alembertian — the entire point of Fermi–Feynman gauge:

$$
S^{(2)}_{E,V}
=\frac h4\int_{E,8}V\cdot\Box_E(\mathcal P_T+\mathcal P_0)V
=\frac12\int_{E,8}V^AK^V_{E,AB}V^B,\qquad
K^V_{E,AB}=\frac h2\kappa_{AB}\Box_E .
\tag{F.2–F.3}
$$

Inversion is now trivial on the residual-free domain, giving the superspace propagator

$$
G^{VV}_E=\hbar\,(K^V_E)^{-1}=2\hbar g^2\kappa^{-1}\Box_E^{-1}
\;\xrightarrow{\;e^{ipx},\ \Box_E\mapsto-p^2\;}\;
\langle V^AV^B\rangle_E
=-\,(2\pi)^4\delta^4(p+p')\,\frac{2\hbar g^2\kappa^{AB}}{p^2}\,
\delta^4(\vartheta_1-\vartheta_2),
\tag{F.4}
$$

(5A.68)–(5A.69), (5A.74). Component check: (5A.71) confirms the $-\frac h2A_m\Box_EA_m$
normalization.

**Chiral sector — where the standard traps live.** Chiral kinematics never uses a naive
$\delta^8$ inverse. The Euclidean matter quadratic form is $S^{(2)}_{E,\Phi}=-h\int_{E,8}
\widetilde\Phi\cdot\Phi$, and the kernel acts on the *constrained* pair
$(\Phi,\widetilde\Phi)$ with the constrained identity kernels
$\mathbf 1_\pm=\mathcal P_\pm\delta^8_E(z-z')$ (5A.72):

$$
K^{\Phi\widetilde\Phi}_{E,AB}=-h\kappa_{AB}\mathbf 1_+,\qquad
G^{\Phi\widetilde\Phi}_E=-\hbar g^2\kappa^{-1}\,\mathcal P_+\delta^8_E(z-z')
\;\xrightarrow{\;p\;}\;
+\,(2\pi)^4\delta^4(p+p')\,\frac{\hbar g^2\kappa^{AB}}{16\,p^2}\,
\bar D_1^2D_1^2\,\delta^4(\vartheta_1-\vartheta_2),
\tag{F.5}
$$

(5A.73)–(5A.74); the reversed orientation uses $\mathcal P_-$. Three rules that must never
be violated when these propagators enter a supergraph:

1. **Functional derivatives of constrained fields carry chiral projectors.** In the vector
   representation, $\delta\Phi(z)/\delta\Phi(z')=\mathbf 1_+(z,z')$, never
   $\delta^8(z-z')$. This is why an EOM insertion contracted into a chiral line produces a
   *projected* delta — the object whose regulated version drives the whole Step-5 anomaly.
2. **Chiral vertices are half-superspace integrals.** A superpotential vertex
   $\int_{E,+}\mathscr U$ entering a $\int_{E,8}$ supergraph converts via one factor
   $-\frac14\bar D^2$ ($+$-type) or $-\frac14D^2$ ($-$-type); equivalently, in the standard
   bookkeeping, each internal line leaving a purely chiral vertex carries one
   $-\frac14\bar D^2$ except one line per vertex whose factor is absorbed by the
   $\int d^2\vartheta\to\int d^4\vartheta$ conversion. The factors $\frac1{16}\bar D^2D^2$
   visible in (F.5) are exactly two such conversions acting on $\delta^4(\vartheta)/p^2$.
3. **Euclidean $\Phi$ and $\widetilde\Phi$ are independent** (5A.2, 4C.53): no complex
   conjugation relates the two propagator orientations; $\mathcal P_+$ vs $\mathcal P_-$
   orientation must be tracked per line, not inferred from conjugacy.

**Loop saturation.** The Grassmann loop closes with the standard saturation identity in
project normalization,

$$
\delta^4(\vartheta_{12})\,D^2\bar D^2\,\delta^4(\vartheta_{12})
=16\,\delta^4(\vartheta_{12}),
\tag{F.6}
$$

which is the origin of the factor $16$ inside the settlement's recorded closed-loop weight
$w_D=\frac1{32}\cdot16\cdot2\cdot2$ (settlement §4); fewer than the maximal
$D^2\bar D^2$ on a closed $\vartheta$ loop gives zero, more reduce by (5A.65).

## 4. Ghost sector

FP ghosts are the chiral/antichiral pairs $\mathfrak c,\widetilde{\mathfrak c}$ (gh $+1$)
and $\mathfrak c',\widetilde{\mathfrak c}'$ (gh $-1$) with multiplier pair $\mathfrak n$
(5A.35, 5A.43). After the Gaussian completion (5A.48) their quadratic form is the
chiral-pair analogue of (F.5) with ghost statistics; their interaction words are locked in
(5A.58)–(5A.60) (the $\coth$/Bernoulli word coefficients). No additional derivation is
needed here beyond the statistics sign in the Wick rules (5A.61)–(5A.62).

## 5. Nielsen–Kallosh decision and irrelevance lemma (one loop, letter channels)

**Decision (D2), owner-authorized 2026-07-16:** select the **external measure-only branch**
of (3D.95b)/(3D.96b): $\mathscr R^{\rm BV}_{\rm NK}=\varnothing$, the NK factor is kept as
an external functional determinant $\mathfrak F^{\rm NK}_{E}$.

**Lemma (to be recorded as an exact check).** In the slice (D1) the gauge-averaging kernel
is field-independent ($\mathcal Y_{E,\rm FF}=2g^2\mathcal A_E/\Box_E$ built from flat
$D,\bar D$), hence $\mathfrak F^{\rm NK}_E$ is a field-independent constant; it cancels in
every normalized correlator, in particular in all $81$ ordered letter channels at one loop.

*Proof sketch:* the NK determinant depends on fields only through $\mathcal Y$ and the
gauge-condition Hessian evaluated on the background; in (D1) both are background-free flat
operators, so $\mathfrak F^{\rm NK}_E=\det$-const. Background-covariant refinements (where
$\mathcal Y$ is built from $\boldsymbol\nabla$) reintroduce field dependence and are
exactly the deferred item §8(iii). $\square$

## 6. One-loop vertex inventory (what the 81 channels actually use)

From the locked words: the cubic gauge self-interaction from the $\mathcal W^2$ BCH
expansion (5A.49)–(5A.52); the matter–gauge tower
$h\,\widetilde\Phi\,(\operatorname{ad}\mathcal V)^n\Phi/n!$ from (5A.53)–(5A.54) — at one
loop only $n=1,2$ enter; the superpotential vertices
$\mathscr U_4=-\frac{\sqrt2}{6g^2}\varepsilon_{rst}c_{ABC}\Phi^A_r\Phi^B_s\Phi^C_t$ and its
independent tilde (4C.13, 5A.55); FP ghost cubic words (5A.58)–(5A.60); and the two
insertion letters with their $\boldsymbol\nabla_-$ descendants (settlement §3). The
settlement's per-channel graph lists draw only from this inventory; the census-completeness
question (which topologies from this inventory appear per channel) is the remaining
review item R.6-3 of `proposals/step5-independent-physics-review-2026-07-16.md`.

## 7. Regulator ledger

Adopted verbatim from the settlement contract §1 (locked upon its merge): Fourier
$e^{ip\cdot x}$ with all momenta incoming; $d=4-2\epsilon$; loop momenta strictly hatted
($\breve\delta\,\ell=0$); the two regulator representations
($\widehat\delta/\breve\delta$ vs $\bar\delta/\widetilde\delta$) never contracted with each
other; finite spin words four-dimensional, propagator inverses $d$-dimensional; the single
evanescent insertion $\mu_\ell^2=\bar\ell^2-\ell_d^2$. The three verified consequences
(cut identity, $\int^{\rm DRED}_\ell\mu^2_\ell/(\ell^2+\Delta)^3=\frac1{32\pi^2}$,
$p^\rho\breve\delta^{mn}T_{m\rho n}=-2\epsilon\,\sigma\!\cdot\!p$) are (R.1)–(R.3) of the
independent review.

## 8. Deferred items (known, bounded, not blocking the fixed-representative settlement)

(i) a *local-$\mathcal Y$* BV completion of the FF slice — proven impossible as stated
(5A.79); a Step-3D acceptance revision or an admissible non-FF local slice would be a new
obligation, not a Step-5 prerequisite under (D1);
(ii) Wess–Zumino/component ↔ superfield BV equivalence
(`OUT_OF_SCOPE_WZ_BV_REDUCTION`, `OUT_OF_SCOPE_COMPONENT_TO_SUPERFIELD_BV_EQUIVALENCE`);
(iii) background-covariant gauge-averaging (covariant $\mathcal Y$) and the corresponding
NK field dependence;
(iv) the Lorentzian sector in its entirety (quarantined 2026-07-16; see PR #42 note).

## 9. Recommended next exact checks (equation-anchored, per the Derivation-first law)

1. (F.1)/(F.6): a single sympy check of the projector algebra and saturation identity in
   the project's explicit $\vartheta$ basis — names (5A.64)–(5A.66), (F.6).
2. (F.5): verify $K^{\Phi\widetilde\Phi}G^{\Phi\widetilde\Phi}=\mathbf 1_+$ on the
   constrained space — names (5A.72)–(5A.73).
3. (D2) lemma: field-independence of $\mathfrak F^{\rm NK}_E$ in slice (D1) — names (5A.48).
4. The settlement's $w_D$ chain against (F.6) and the two conversion factors of §3 rule 2 —
   names settlement §4.
