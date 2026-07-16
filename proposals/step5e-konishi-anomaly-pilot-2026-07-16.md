# Step-5E memo — Konishi-anomaly pilot: the component EOM-collapse method on its simplest target (Euclidean N=4 SYM)

Status: `NON_AUTHORITY_PROPOSAL`. Numbered equations are (5E.$n$). Companions: Step-5C
(off-shell Noether machinery), Step-5D (component Ward-identity method). This memo
executes the method of Step-5D on the **simplest anomalous channel that exists** — the
Konishi current — as the pilot/go-no-go test of the whole component route, and specifies
the verification workflow for mechanical execution (§8).

Owner instructions implemented (2026-07-16): *the immediate priority is to verify the
component Feynman-diagram method computationally: with an interaction vertex inserted,
and the anomaly viewed as the failure of the cutting rule for EOM–letter contractions
(regularized delta function), can it reproduce the Konishi anomaly? This is probably the
simplest diagram; if it passes, proceed to the other sectors. Full coefficient
verification is not required of this derivation — record the verification workflow in the
repository for mechanical execution. Focus on Euclidean N=4 SYM.*

---

## 0. Why Konishi is the right pilot

The Konishi operator of the $\mathcal N=4$ theory in $\mathcal N=1$ language is
$K=\sum_r\widetilde\Phi_r^A(e^{\mathcal V_{\rm ad}})^A{}_B\Phi_r^B$; its multiplet is the
canonical example of an anomalous multiplet, and its anomaly is produced by **exactly the
mechanism this program attributes to the supersymmetry-current AWI**: an equation-of-motion
insertion contracted into a propagator collapses to a delta function unregulated, and
fails to collapse under DRED by one evanescent insertion. For Konishi:

- the symmetry is a **flavor-blind phase rotation** — the gauge multiplet is inert, so
  the current, the EOM identity, and the graph census are drastically simpler than for
  the SUSY current (no gauge-multiplet EOM terms, no gauge-sector remainder
  $\mathfrak G$ at this order for gauge-invariant channels);
- the classical breaking (superpotential, charge $+3$) is cleanly typed and does not
  contaminate the pilot channel;
- the target is known independently in the literature (the Konishi/ABJ anomaly), giving
  an external sanity value to compare against **after** the project-side derivation —
  never as an input.

If the pilot reproduces the anomaly, the identical pipeline (Step-5D §7) applies to the
$\partial\cdot j_-$ letter channels; if it fails, the failure localizes in a
few-propagator computation.

## 1. The Konishi current and its exact off-shell divergence (Euclidean)

Konishi variation ($\alpha$ constant, all flavors equally; charges
$q_{\phi}=q_\psi=q_F=+1$, tilded $-1$, gauge multiplet $0$):

$$
\delta_K\phi_r=i\alpha\,\phi_r,\quad
\delta_K\psi_r=i\alpha\,\psi_r,\quad
\delta_KF_r=i\alpha\,F_r,\qquad
\delta_K(\widetilde\phi_r,\widetilde\psi_r,\widetilde F_r)
=-i\alpha\,(\widetilde\phi_r,\widetilde\psi_r,\widetilde F_r),
\qquad
\delta_K(\mathcal A_m,\lambda,\widetilde\lambda,\mathscr D)=0 .
\tag{5E.1}
$$

From the Euclidean off-shell action (4C.42a) and the symplectic potential (5C.6), the
Noether current is

$$
\boxed{
j^m_K=ih\operatorname{tr}_\kappa\Big[
(\mathcal D_m\widetilde\phi_r)\,\phi_r-(\mathcal D_m\phi_r)\,\widetilde\phi_r
+\widetilde\psi_r\bar\sigma_E^m\psi_r\Big].}
\tag{5E.2}
$$

Charge bookkeeping of every sector of (4C.42a): kinetic terms, both Yukawa families,
$\widetilde F_rF_r$, and $\mathscr D(\phi_r\times\widetilde\phi_r)$ are neutral; only the
superpotential sector carries charge ($\pm3$). Hence the exact off-shell divergence
identity (Noether identity, same derivation as (5C.14)):

$$
\boxed{
\begin{aligned}
\partial_mj^m_K
={}&\underbrace{\ \tfrac{3\sqrt2\,i\,h}{2}\,\varepsilon_{rst}c_{ABC}
\big(F_r^A\phi_s^B\phi_t^C-\widetilde F_r^A\widetilde\phi_s^B\widetilde\phi_t^C\big)\
}_{\text{classical breaking (superpotential, charge }\pm3)}\\
&-\,i\operatorname{tr}_\kappa\Big[
\mathcal E_{\phi_r}\phi_r-\widetilde\phi_r\,\mathcal E_{\widetilde\phi_r}
+\mathcal E_{\psi_r}\!\cdot\psi_r-\widetilde\psi_r\!\cdot\mathcal E_{\widetilde\psi_r}
+\mathcal E_{F_r}F_r-\widetilde F_r\,\mathcal E_{\widetilde F_r}\Big],
\end{aligned}}
\tag{5E.3}
$$

with the ordered Euclidean Euler operators of (4C.42a) (the matter rows of (5C.13),
$E$-signature). This is the component form of the superfield statement
$\bar D^2K=(\text{superpotential term})+(\text{EOM terms})$, before any regularization.
Every term on the right is typed: *breaking* / *EOM*. There is no gauge-multiplet EOM
term — the first structural simplification relative to $\partial\cdot j_-$.

## 2. The pilot channel and its Ward identity

Take the two-gauge-boson channel,

$$
\mathcal G^{AB}_{np}(x;y,z):=
\big\langle\,\partial_mj^m_K(x)\;A^A_n(y)\;A^B_p(z)\,\big\rangle_E ,
\tag{5E.4}
$$

at one loop (order $\hbar$, absorbed-coupling basis). The frontal Ward identity (5D.5)
specializes with three simplifications:

1. **No contact terms**: $\delta_KA=0$, so $\delta_K\mathcal O=0$ for both external legs.
2. **No classical-breaking contribution at one loop**: the breaking operator
   $\varepsilon_{rst}c\,F\phi\phi$ is cubic in charged matter with no gauge leg; connecting
   it to $AA$ requires at least two more powers of the coupling beyond one loop in this
   channel (first graph: two-loop). Typed and dropped at this order.
3. **No gauge-sector remainder at this order in this channel**: the Konishi rotation
   commutes with the gauge fixing ($\delta_K$ acts on matter only, the gauge fermion
   (Step-5B §5) contains no matter), so $\mathfrak G_K\equiv0$ **exactly** — the second
   structural simplification relative to the SUSY current, where $\mathfrak G_-\ne0$.

Hence at one loop the entire correlator is the anomaly candidate:

$$
\mathcal G^{AB}_{np}\big|_{1\text{-loop}}=\mathfrak A^{AB}_{np}(x;y,z)
=\text{(sum of regulated-collapse failures of the EOM insertions in (5E.3))}.
\tag{5E.5}
$$

## 3. Graph census of the pilot channel

Insertion (5E.3), EOM part; expand each Euler operator into its kinetic + minimal-coupling
+ Yukawa pieces and Wick-contract to two external $A$ legs at one loop. The complete
census (to be re-verified mechanically, §8 W3):

| family | content | lines | anomaly status |
|---|---|---|---|
| (a) fermion triangle | $\mathcal E_{\psi}\psi$- and $\widetilde\psi\mathcal E_{\widetilde\psi}$-insertions; two minimal vertices $h\,c_{BCA}\,\widetilde\psi\bar\sigma^n A_n\psi$-type from the covariant kinetic term | $\psi\widetilde\psi$ loop | **evanescent failure — the anomaly source** |
| (b) scalar triangle + seagull | $\mathcal E_{\phi}\phi$-type insertions; minimal scalar vertices and $AA\phi\widetilde\phi$ seagull | $\phi\widetilde\phi$ loop | collapse **exact** in DRED (§4) — zero anomaly |
| (c) auxiliary contacts | $\mathcal E_FF$, $\widetilde F\mathcal E_{\widetilde F}$ insertions | $F\widetilde F$ contact | no pole, no loop momentum — zero |
| (d) Yukawa-piece insertions | the $\sqrt2h(\widetilde\phi\times\lambda)$-type parts of $\mathcal E_\psi$ | need $\lambda$/$\phi$ legs | wrong external content for $AA$ at one loop — absent |

Family (b) exactness: the scalar EOM–propagator contraction has numerator equal to the
inverse propagator built from the **same** $d$-dimensional momenta as the denominator
(no four-dimensional spinor algebra enters), so the collapse $KK^{-1}=\delta$ is exact
under DRED; no $\mu^2$ remainder. Family (a) is the only place where a four-dimensional
$\sigma$-chain meets $d$-dimensional denominators.

## 4. The regulated collapse on the fermion triangle

Momentum space (5B.D3): all incoming, $x$-insertion momentum $q=-(k_y+k_z)$; loop
momentum $\ell$ strictly $d$-dimensional, external momenta four-dimensional; DRED ledger
of Step-5D §5.

The fermionic part of the insertion (5E.3) is
$-i\operatorname{tr}[\mathcal E_{\psi_r}\psi_r-\widetilde\psi_r\mathcal
E_{\widetilde\psi_r}]$ whose kinetic pieces read
$-ih\operatorname{tr}[(\mathcal D_m\widetilde\psi_r)\bar\sigma_E^m\psi_r
+\widetilde\psi_r\bar\sigma_E^m(\mathcal D_m\psi_r)]$. On the triangle each piece sits
adjacent to one matter-fermion propagator; the **EOM–letter contraction** is the
numerator identity

$$
(\text{4-dim }\bar\sigma\cdot r_e)\times\frac{(\text{4-dim }\sigma\cdot\bar r_e)}
{r_{e,d}^{\,2}}
=\frac{\bar r_e^{\,2}}{r_{e,d}^{\,2}}\,\mathbf 1
=\Big(1+\frac{\mu_\ell^2}{r_{e,d}^{\,2}}\Big)\mathbf 1,
\qquad \mu_\ell^2:=\bar\ell^2-\ell_d^2 ,
\tag{5E.6}
$$

by the Euclidean Clifford algebra (5B.4): the *1* is the exact cutting/collapse term
(unregulated Schwinger–Dyson: the line contracts to a point and the graph reduces to a
lower-point contact object, which vanishes here because $\delta_K\mathcal O=0$ — the
Ward identity closes classically), and the $\mu_\ell^2$ term is the **unique** failure —
one universal insertion per marked line, no graph-specific $(4-d)$ factors. This is the
component-literal version of the cutting-failure identity quoted in Step-5D (5D.6).

What survives after both orientations of the loop and both insertion pieces are summed is
the $\mu^2$-triangle with a four-dimensional open $\sigma$-chain:

$$
\mathfrak A^{AB}_{np}(q;k_y,k_z)
=\mathcal N^{AB}\cdot
\int\!\frac{d^d\ell}{(2\pi)^d}\;
\frac{\mu_\ell^2\;\;T_{np}(k_y,k_z)}
{\ell_d^2\,(\ell+k_y)_d^2\,(\ell+k_y+k_z)_d^2}
\;+\;(\text{orientation image}),
\tag{5E.7}
$$

with

- **color factor** $\mathcal N^{AB}\propto h\cdot
  c_{ACD}\,c_{BDC}\cdot n_f=-\,n_f\,h\,c_{ACD}c_{BCD}$, $n_f=3$ flavors — i.e. the
  adjoint Dynkin index; per flavor the result is the $T(\mathrm{adj})$ pattern of the
  Konishi/ABJ anomaly;
- **spin word** $T_{np}$: the four-dimensional trace
  $\operatorname{tr}[\bar\sigma_E^{m}\sigma_E^{n}\bar\sigma_E^{p}\sigma_E^{q}]
  =2(\delta^{mn}\delta^{pq}-\delta^{mp}\delta^{nq}+\delta^{mq}\delta^{np})
  \mp2\,\epsilon_E^{mnpq}$ contracted with the surviving external momenta — the
  $\delta$-terms cancel between the two orientations (they are parity-even and pair off
  against the mirrored trace), the $\epsilon_E$-term adds up: the anomaly output is
  forced into $\epsilon_E^{mnpq}k_{y\,m}k_{z\,q}$-structure. **Orientation convention
  required**: no merged contract fixes $\epsilon_E^{1234}$; this memo fixes
  $\epsilon_E^{1234}:=+1$ as decision **(5E.D5)** (a one-line convention; the physical
  anomaly is orientation-covariant);
- **master integral** (dimension-shift representation, cf. review R.2 — to be re-derived
  project-side in W5):
  $$
  \lim_{\epsilon\to0}\,\mu^{2\epsilon}\!\!
  \int\!\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
  \frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}
  =\frac{1}{32\pi^2}\,,
  \tag{5E.8}
  $$
  independent of $\Delta$ — which is simultaneously the proof that
  $\mathfrak A$ is **local** (a polynomial in $k_y,k_z$), as an anomaly must be.

Assembling (5E.7)–(5E.8) and Fourier-transforming back, the pilot's target statement is

$$
\boxed{
\partial_mj^m_K\Big|_{\rm anomaly}
=\;\mathfrak c_K\;\frac{\hbar}{32\pi^2}\;n_f\;
c_{ACD}c_{BCD}\;\epsilon_E^{mnpq}\,
\partial_mA^A_n\,\partial_pA^B_q\;+\;O(A^3),}
\tag{5E.9}
$$

with $\mathfrak c_K$ a pure rational-times-phase number produced by the chain
(insertion coefficients in (5E.3)) × (two minimal-vertex factors) × (propagator
normalizations (5B.17)-projected to components) × (orientation sum) × ($\sigma$-trace) —
the factors are enumerated one by one in §8 for mechanical verification. The $O(A^3)$
completion to $\epsilon\operatorname{tr}(F\widetilde F)$-form is fixed by gauge
covariance and checked at the box-graph level (W7).

**External sanity target** (reference-level only, never an input): the literature Konishi
anomaly for adjoint matter, $\bar D^2(\widetilde\Phi e^V\Phi)\big|_{\rm anom}\propto
T(\mathrm{adj})/(16\pi^2)\cdot\operatorname{tr}W^aW_a$, whose
$\theta$-component contains exactly the $\epsilon F F$ structure of (5E.9) with matching
Casimir; agreement of $\mathfrak c_K$ with the literature value (after the notation
dictionary) is the pilot's pass criterion **P1**.

## 5. The SUSY-partner channel (second pilot stage)

The multiplet partner check: $\langle\partial_mj^m_K(x)\;
\operatorname{tr}(\lambda\lambda)(y)\rangle$-type channels, fed by the Yukawa pieces of
the insertion (family (d) of §3 with matter legs closed by two Yukawa vertices
$\sqrt2h\,c\,\widetilde\phi\psi\lambda$ / $\sqrt2h\,c\,\phi\widetilde\psi\widetilde
\lambda$). Same mechanism, same master integral, coefficient tied to (5E.9) by the
multiplet structure. Specified as workflow stage W8; **not required for go/no-go** (the
$AA$ channel decides), but it is the first genuinely supersymmetric corroboration and the
direct warm-up for the $\partial\cdot j_-$ letter channels: the graph topology (triangle
with two Yukawas) is exactly the topology of the $(\mathfrak b,\mathfrak c)$-family
letter channels of Step-5D.

## 6. Go/no-go and the promotion path

- **PASS** (P1 holds): the EOM-collapse/cutting-failure mechanism is validated end to end
  in component form — promote the identical pipeline to the $\partial_mj^m_-$ letter
  bilinears (Step-5D §7), starting with the $(\mathfrak f,\mathfrak f)$ seed channel; the
  only new ingredients there are the $-$-slot insertion (5D.4) (richer term list) and the
  gauge-sector remainder $\mathfrak G_-$ (absent for Konishi, must be typed there).
- **FAIL**: the discrepancy localizes in the §8 factor list (a one-loop, two-vertex
  computation) — fix before touching any letter channel.

## 7. What is new in this memo vs. what is imported

New: (5E.1)–(5E.5) (Konishi current, exact off-shell divergence, channel Ward identity
and its three simplifications, graph census with the scalar-exactness and
auxiliary-contact lemmas), the assembly (5E.7)/(5E.9), decision (5E.D5). Imported with
independent re-derivation required in the workflow: the collapse identity (5E.6)
(elementary, from (5B.4)), the master integral (5E.8) (review R.2 gives the derivation
shape; W5 re-derives). Nothing is taken from the unmerged settlement branch.

## 8. Verification workflow (for mechanical execution — codex)

Each item names its target equation; every item is a bounded exact computation. Items
W1–W6 decide P1.

- **W1** [(5E.2), (5E.3)]: jet-space check (engine of `tests/test_step5b_feynman_rules.py`
  extended, or the Part-1/2 jet engine draft preserved from this session): verify
  $\partial_mj^m_K-\delta_K\mathcal L_E/(i\alpha)$-Noether identity and the typed split of
  (5E.3) off shell, su(2) instance. (Konishi version of the B1/B2 suite — *simpler than
  the SUSY-current suite; implement first*.)
- **W2** [(5E.2)→components]: derive the component matter propagators and the two minimal
  vertices from (4C.42a) in Feynman gauge (Step-5B (5B.15)/(5B.17) projected), with the
  exact $\hbar g^2\kappa$ normalizations; record each as a numbered rule.
- **W3** [§3 census]: enumerate all one-loop Wick contractions of every term of (5E.3)
  against $A_n^A(y)A_p^B(z)$; confirm the four families and **prove absences** (family
  (d) content mismatch; breaking-term order counting of §2 item 2).
- **W4** [(5E.6)]: verify the collapse identity as a $2\times2$ matrix identity with
  $\bar\ell$ four-dimensional, $\ell_d$ $d$-dimensional, using (5B.4); confirm *no*
  graph-specific $(4-d)$ factor and the scalar-sector exactness (family (b)).
- **W5** [(5E.8)]: re-derive the master integral by rotational averaging
  ($\int d^d\ell\,\widetilde\ell^2f=\frac{d-4}{d}\int d^d\ell\,\ell^2f$) and Gamma
  functions; confirm $\Delta$-independence at $\epsilon\to0$ and the companion pole
  $\int(\ell^2+\Delta)^{-2}=\Gamma(\epsilon)(4\pi)^{-d/2}\Delta^{-\epsilon}$.
- **W6** [(5E.7)→(5E.9)]: assemble $\mathfrak c_K$: (i) insertion coefficients from
  (5E.3); (ii) vertex factors from W2 with the (5A.61)–(5A.63) ordering and weight;
  (iii) both orientations (Koszul sign of the fermion loop!); (iv) the four-$\sigma$
  trace with (5E.D5), verifying the $\delta$-part cancellation between orientations;
  (v) Feynman parametrization $\Gamma(3)=2$ bookkeeping; (vi) the momentum polynomial
  $\epsilon^{mnpq}k_{y\,m}k_{z\,q}$. Output: exact $\mathfrak c_K$.
- **W7** [(5E.9) $O(A^3)$]: the box/triangle graphs with three gauge legs assemble the
  abelian result into $\epsilon\,\partial A\,\partial A+\tfrac13 c\,\epsilon\,\partial
  A\,AA$-covariant form (gauge-covariance completion).
- **W8** [§5]: the $\operatorname{tr}(\lambda\lambda)$ partner channel by the same steps
  (two-Yukawa triangle); compare with the multiplet prediction from W6.
- **W9** [P1]: build the notation dictionary to one literature convention for the Konishi
  anomaly and compare $\mathfrak c_K$; record verdict PASS/FAIL with the dictionary as a
  reference-level artifact (never authority).

Suggested implementation order: W1 (reuses this session's jet engine), W4, W5 (small,
independent), W2–W3, then W6 (the assembly), W7–W9.
