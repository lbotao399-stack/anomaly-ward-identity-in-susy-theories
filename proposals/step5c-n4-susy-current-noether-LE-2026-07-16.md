# Step-5C memo — the N=1 supersymmetry current of N=4 SYM by Noether's theorem with auxiliary fields, Lorentzian ∥ Euclidean

Status: `NON_AUTHORITY_PROPOSAL`. Numbered equations are (5C.$n$); locked inputs cited by
contract tag. Companion: the Step-5B memo (BRST/BV/Feynman rules) and the Step-5D memo
(component Ward identity), same date. Exact checks: §7.

Owner instructions implemented (2026-07-16): *using Noether's theorem — keeping the
auxiliary fields — derive the N=1 SUSY current $J^\mu_a$ of N=4 SYM; the SUSY action is
invariant only up to a total divergence, and after the divergence correction the current
becomes much cleaner: all auxiliary fields cancel. Then write $\partial_\mu J^\mu_a$
off-shell as a combination of terms proportional to the equations of motion. Everything
in parallel for Lorentzian and Euclidean.*

---

## 0. Inputs, method, and relation to locked results

Inputs: the **off-shell** component actions with independent auxiliaries
$(\mathscr D;F_r,\widetilde F_r)$ — Lorentzian (4C.14) $\equiv$ (5A.17), Euclidean
(4C.42a) $\equiv$ (5A.27); the off-shell manifest $\mathcal N=1$ transformations —
vector multiplet (4A.26)/(4A.27), adjoint chiral multiplet (4B.20), (4B.20a), (4B.20b)
[L] and (4B.33b) [E], applied per flavor $r=1,2,3$; adjoint conventions (4.5)–(4.9);
sigma algebra (1.12)–(1.17), (1.54)–(1.57), (4C.55c), (4C.71).

Method: the local-parameter (Gell-Mann–Lévy) construction already locked for pure
$\mathcal N=1$ SYM in §§4A.8–4A.10 and for the **on-shell** $SU(4)_R$-covariant theory in
§4C.11. What is new here: the same construction on the **off-shell** action with
independent auxiliary fields, in both signatures, with the auxiliary-cancellation
mechanism displayed, and the exact **off-shell** divergence identity in which the
auxiliary Euler operators appear explicitly.

Relation to locked results (consistency targets, not inputs of the derivation): the
currents obtained below must reduce to (4A.42)/(4A.55) for pure SYM, and must coincide
with the $\mathcal I{=}4$ slot of the on-shell currents (4C.59)/(4C.64b)/(4C.67)/(4C.67c)
once the auxiliary composites (4C.61) are inserted — both reductions are verified in §4.3.

Convention for parameter stripping (2A.9), (4A.35): local parameters always stand to the
**right** of all fields,

$$
\Theta^\mu_R(\delta_\varepsilon)
=:C^\mu_{R,a}\,\varepsilon^a+\bar C_R^{\mu\dot a}\,\bar\varepsilon_{\dot a},
\qquad
\delta_a X:=\frac{\partial(\delta X)}{\partial\varepsilon^a}\ \ \text{(right strip)} .
\tag{5C.1}
$$

## 1. Off-shell manifest N=1 transformations (both signatures)

Lorentzian ((4A.26); (4B.20)–(4B.20b) flavored, $\llbracket X,Y\rrbracket^A=ic_{BC}{}^AX^BY^C$):

$$
\boxed{
\begin{aligned}
\delta_LA_\mu&=-i\varepsilon\sigma_{L\mu}\bar\lambda
-i\bar\varepsilon\bar\sigma_{L\mu}\lambda,
&\delta_L\lambda_a&=(\sigma_L^{\rho\sigma})_a{}^b\varepsilon_bF_{\rho\sigma}
-i\varepsilon_a\mathscr D,\\
\delta_L\bar\lambda_{\dot a}&=
-\bar\varepsilon_{\dot b}(\bar\sigma_L^{\rho\sigma})^{\dot b}{}_{\dot a}F_{\rho\sigma}
+i\bar\varepsilon_{\dot a}\mathscr D,
&\delta_L\mathscr D&=-\varepsilon\sigma_L^\mu\mathcal D_\mu\bar\lambda
+\bar\varepsilon\bar\sigma_L^\mu\mathcal D_\mu\lambda,\\
\delta_L\phi_r&=-\sqrt2\,\varepsilon\psi_r,
&\delta_L\psi_{ra}&=-\sqrt2\,\varepsilon_aF_r
+i\sqrt2(\sigma_L^\mu)_{a\dot b}\bar\varepsilon^{\dot b}\mathcal D_\mu\phi_r,\\
\delta_L\widetilde\phi_r&=-\sqrt2\,\bar\varepsilon\widetilde\psi_r,
&\delta_L\widetilde\psi_{r\dot a}&=-\sqrt2\,\bar\varepsilon_{\dot a}\widetilde F_r
-i\sqrt2\,\varepsilon^a(\sigma_L^\mu)_{a\dot a}\mathcal D_\mu\widetilde\phi_r,\\
\delta_LF_r&=i\sqrt2\,\bar\varepsilon\bar\sigma_L^\mu\mathcal D_\mu\psi_r
-2i\llbracket\bar\varepsilon\bar\lambda,\phi_r\rrbracket,
&\delta_L\widetilde F_r&=i\sqrt2\,\varepsilon\sigma_L^\mu\mathcal D_\mu\widetilde\psi_r
-2i\llbracket\varepsilon\lambda,\widetilde\phi_r\rrbracket .
\end{aligned}}
\tag{5C.2}
$$

Euclidean ((4A.27); (4B.33b) flavored; $\widetilde\varepsilon:=\bar\varepsilon$ alias
(4.34a); all tilded fields independent, (4C.53)):

$$
\boxed{
\begin{aligned}
\delta_EA_m&=\varepsilon\sigma_{Em}\widetilde\lambda
+\widetilde\varepsilon\bar\sigma_{Em}\lambda,
&\delta_E\lambda_a&=-(\sigma_E^{np})_a{}^b\varepsilon_bF_{np}
-i\varepsilon_a\mathscr D,\\
\delta_E\widetilde\lambda_{\dot a}&=
+\widetilde\varepsilon_{\dot b}(\bar\sigma_E^{np})^{\dot b}{}_{\dot a}F_{np}
+i\widetilde\varepsilon_{\dot a}\mathscr D,
&\delta_E\mathscr D&=-i\varepsilon\sigma_E^m\mathcal D_m\widetilde\lambda
+i\widetilde\varepsilon\bar\sigma_E^m\mathcal D_m\lambda,\\
\delta_E\phi_r&=-\sqrt2\,\varepsilon\psi_r,
&\delta_E\psi_{ra}&=-\sqrt2\,\varepsilon_aF_r
-\sqrt2(\sigma_E^m)_{a\dot b}\widetilde\varepsilon^{\dot b}\mathcal D_m\phi_r,\\
\delta_E\widetilde\phi_r&=-\sqrt2\,\widetilde\varepsilon\widetilde\psi_r,
&\delta_E\widetilde\psi_{r\dot a}&=-\sqrt2\,\widetilde\varepsilon_{\dot a}\widetilde F_r
+\sqrt2\,\varepsilon^a(\sigma_E^m)_{a\dot a}\mathcal D_m\widetilde\phi_r,\\
\delta_EF_r&=\sqrt2\,\widetilde\varepsilon\bar\sigma_E^m\mathcal D_m\psi_r
-2i\llbracket\widetilde\varepsilon\widetilde\lambda,\phi_r\rrbracket,
&\delta_E\widetilde F_r&=-\sqrt2\,\varepsilon\sigma_E^m\mathcal D_m\widetilde\psi_r
-2i\llbracket\varepsilon\lambda,\widetilde\phi_r\rrbracket .
\end{aligned}}
\tag{5C.3}
$$

These close off shell on the full field set (4C.54). The Wick maps (4A.11), (4B.33b)
prose, (4C.48) send (5C.2) to (5C.3) coefficient by coefficient.

## 2. Symplectic potentials and localization coefficients

Sector split of the off-shell Lagrangians ((4C.14) L / (4C.42a) E; $\vartheta$-term kept
separate as in (4C.64)):

$$
\mathcal L_R=\mathcal L_{R,g}+\mathcal L_{R,s}+\mathcal L_{R,f}
+\mathcal L_{R,\rm aux}+\mathcal L_{R,Y}+\mathcal L_{R,W}+\mathcal L_{R,\vartheta},
\tag{5C.4}
$$

$$
\begin{aligned}
\mathcal L_{L,\rm aux}&=h\operatorname{tr}_\kappa\Big[\tfrac12\mathscr D^2
+\widetilde F_rF_r+i\mathscr D(\phi_r\times\widetilde\phi_r)\Big],
\qquad
\mathcal L_{L,W}=-\frac{\sqrt2h}{2}\varepsilon_{rst}c_{ABC}
\big(F_r^A\phi_s^B\phi_t^C+\widetilde F_r^A\widetilde\phi_s^B\widetilde\phi_t^C\big),\\
\mathcal L_{E,\rm aux}&=h\operatorname{tr}_\kappa\Big[-\tfrac12\mathscr D^2
-\widetilde F_rF_r-i\mathscr D(\phi_r\times\widetilde\phi_r)\Big],
\qquad
\mathcal L_{E,W}=+\frac{\sqrt2h}{2}\varepsilon_{rst}c_{ABC}
\big(F_r^A\phi_s^B\phi_t^C+\widetilde F_r^A\widetilde\phi_s^B\widetilde\phi_t^C\big),
\end{aligned}
\tag{5C.5}
$$

with the Yukawa sectors $\mathcal L_{L,Y}=\sqrt2hc_{ABC}(\widetilde\phi_r^A\psi_r^B\lambda^C
+\phi_r^A\widetilde\psi_r^B\widetilde\lambda^C)
+\frac h{\sqrt2}\varepsilon_{rst}c_{ABC}(\phi_t^A\psi_r^B\psi_s^C
+\widetilde\phi_t^A\widetilde\psi_r^B\widetilde\psi_s^C)$ and
$\mathcal L_{E,Y}=-\mathcal L_{L,Y}$-pattern per (4C.42a).

Only the kinetic sectors have symplectic potentials:

$$
\begin{aligned}
\Theta_L^\mu(\delta)&=h\operatorname{tr}_\kappa\Big[
-F^{\mu\nu}\delta A_\nu
+i\bar\lambda\bar\sigma_L^\mu\delta\lambda
-(\mathcal D^\mu\widetilde\phi_r)\delta\phi_r
-(\mathcal D^\mu\phi_r)\delta\widetilde\phi_r
+i\widetilde\psi_r\bar\sigma_L^\mu\delta\psi_r\Big]
+\Theta_{\vartheta,L}^\mu,\\
\Theta_E^m(\delta)&=h\operatorname{tr}_\kappa\Big[
+F^{mn}\delta A_n
+\widetilde\lambda\bar\sigma_E^m\delta\lambda
+(\mathcal D_m\widetilde\phi_r)\delta\phi_r
+(\mathcal D_m\phi_r)\delta\widetilde\phi_r
+\widetilde\psi_r\bar\sigma_E^m\delta\psi_r\Big]
+\Theta_{\vartheta,E}^m .
\end{aligned}
\tag{5C.6}
$$

Inserting (5C.2)/(5C.3) and stripping per (5C.1) gives the localization coefficients.
$\varepsilon$-slot:

$$
\boxed{
\begin{aligned}
C^\mu_{L,a}=h\operatorname{tr}_\kappa\Big[&
+iF^{\mu\nu}(\sigma_{L\nu}\bar\lambda)_a
+i\bar\lambda_{\dot b}(\bar\sigma_L^\mu)^{\dot bb}
\big((\sigma_L^{\rho\sigma})_b{}^c\epsilon_{ac}F_{\rho\sigma}
-i\epsilon_{ab}\mathscr D\big)\\
&+\sqrt2\,(\mathcal D^\mu\widetilde\phi_r)\,\psi_{ra}
-i\sqrt2\,F_r\,\widetilde\psi_{r\dot b}(\bar\sigma_L^\mu)^{\dot bb}\epsilon_{ab}
\Big]+C^{\mu}_{\vartheta,L,a},\\
C^m_{E,a}=h\operatorname{tr}_\kappa\Big[&
-F^{mn}(\sigma_{En}\widetilde\lambda)_a
+\widetilde\lambda_{\dot b}(\bar\sigma_E^m)^{\dot bb}
\big(-(\sigma_E^{np})_b{}^c\epsilon_{ac}F_{np}
-i\epsilon_{ab}\mathscr D\big)\\
&-\sqrt2\,(\mathcal D_m\widetilde\phi_r)\,\psi_{ra}
-\sqrt2\,F_r\,\widetilde\psi_{r\dot b}(\bar\sigma_E^m)^{\dot bb}\epsilon_{ab}
\Big]+C^{m}_{\vartheta,E,a},
\end{aligned}}
\tag{5C.7}
$$

(the pure-SYM parts reproduce (4A.36)/(4A.51) with $f\to h\kappa$, the $\mathfrak k$-parts
being the separated $\vartheta$-coefficients (4C.64)/(4C.66d)); the
$\bar\varepsilon$/$\widetilde\varepsilon$-slot coefficients
$\bar C^{\mu\dot a}_L$, $\widetilde C^{m\dot a}_E$ are the mirror expressions
(pure-SYM parts (4A.37)/(4A.52); matter parts with
$\widetilde\psi\to\psi$, $\phi\leftrightarrow\widetilde\phi$, $F\to\widetilde F$).
Note the **auxiliary fields enter $C$**: the $\mathscr D$-terms through
$\delta\lambda$, the $F_r$-terms through $\delta\psi_r$.

## 3. Bulk reduction and the Auxiliary Cancellation Lemma

For constant parameters, $\delta\mathcal L_R=\partial\Theta_R(\delta)+\mathscr B_R$ with
the bulk $\mathscr B_R$ collected sector by sector as in (4C.58c)/(4C.66b), now on the
off-shell action. The $\varepsilon$-slot bulk organizes into a **total derivative**,

$$
\sum_{q}\mathscr B_{R,q}\big|_{\varepsilon}
=-\partial_M\big(\mathcal S^{M}_{R,a}\,\varepsilon^a\big),
\tag{5C.8}
$$

and the essential new fact relative to the on-shell computation is:

**Auxiliary Cancellation Lemma.** *Every $\mathscr D$-, $F_r$-, $\widetilde F_r$-dependent
term of the $\varepsilon$-slot bulk cancels pairwise before (5C.8) is read off; hence
$\mathcal S^M_{R,a}$ — and with it the Noether current — contains no auxiliary field.*

Proof, Lorentzian $\varepsilon$-slot (the Euclidean case is the same pattern with the
(4A.11)/(4C.48) sign transport; the $\bar\varepsilon$-slots are mirror images):

(i) **derivative-$\mathscr D$ pair**: $\tfrac12\mathscr D^2$ contributes
$h\operatorname{tr}[\mathscr D\,\delta_\varepsilon\mathscr D]
=-h\operatorname{tr}[\mathscr D\,\varepsilon\sigma_L^\rho\mathcal D_\rho\bar\lambda]$;
the gaugino kinetic bulk contributes
$-ih\operatorname{tr}[(\mathcal D_\mu\bar\lambda)\bar\sigma_L^\mu\delta\lambda]
\supset+h\operatorname{tr}[\mathscr D\,\varepsilon\sigma_L^\mu\mathcal D_\mu\bar\lambda]$
(using $(\mathcal D\bar\lambda)\bar\sigma^\mu\varepsilon=-\varepsilon\sigma^\mu
\mathcal D\bar\lambda$). Sum: $0$.

(ii) **moment-map pair**: $i\mathscr D C_0$ contributes
$ih\operatorname{tr}[\mathscr D\,\delta C_0]|_\varepsilon
=-i\sqrt2\,h\operatorname{tr}[\mathscr D\,(\varepsilon\psi_r\times\widetilde\phi_r)]$;
the Yukawa $\sqrt2hc_{ABC}\widetilde\phi_r^A\psi_r^B\lambda^C$ contributes via
$\delta\lambda|_{\mathscr D}=-i\varepsilon\mathscr D$ exactly
$+i\sqrt2\,h\,c_{ABC}(\varepsilon\psi_r)^A\widetilde\phi_r^B\mathscr D^C$-pattern.
By $c_{[ABC]}$ and $\operatorname{tr}_\kappa$-invariance (4.9) the two cancel.

(iii) **derivative-$F$ pair**: $\widetilde F_rF_r$ contributes
$h\operatorname{tr}[(\delta\widetilde F_r)F_r]\supset
i\sqrt2h\operatorname{tr}[(\varepsilon\sigma_L^\mu\mathcal D_\mu\widetilde\psi_r)F_r]$;
the matter-fermion kinetic bulk contributes
$-ih\operatorname{tr}[(\mathcal D_\mu\widetilde\psi_r)\bar\sigma_L^\mu\delta\psi_r]
\supset-i\sqrt2h\operatorname{tr}[(\varepsilon\sigma_L^\mu\mathcal
D_\mu\widetilde\psi_r)F_r]$. Sum: $0$.

(iv) **gaugino-Yukawa-$F$ pair**: the bracket part of
$\delta\widetilde F_r$ gives
$-2ih\operatorname{tr}[\llbracket\varepsilon\lambda,\widetilde\phi_r\rrbracket F_r]$;
the Yukawa $\sqrt2hc\,\widetilde\phi_r\psi_r\lambda$ with
$\delta\psi_r|_F=-\sqrt2\varepsilon F_r$ gives
$-2h\,c_{ABC}\widetilde\phi_r^AF_r^B(\varepsilon\lambda)^C$. With
$\llbracket X,Y\rrbracket^A=ic_{BC}{}^AX^BY^C$ these are equal and opposite. Sum: $0$.

(v) **superpotential-$F$ pair**: $\mathcal L_{L,W}$ with $\delta\phi=-\sqrt2\varepsilon\psi$
gives $+2h\varepsilon_{rst}c_{ABC}\phi_t^AF_r^B(\varepsilon\psi_s)^C$ (after color
reordering); the matter-Yukawa
$\frac h{\sqrt2}\varepsilon_{rst}c\,\phi_t\psi_r\psi_s$ with
$\delta\psi|_F$ gives $-2h\varepsilon_{rst}c_{ABC}\phi_t^AF_r^B(\varepsilon\psi_s)^C$.
Sum: $0$. (This pair is the Noether-level fingerprint of the locked superpotential
normalization $u=-\sqrt2$, (4C.12): any other coefficient leaves a residue.)

No other auxiliary-dependent $\varepsilon$-slot term exists ($\delta_a\phi_r$,
$\delta_a\widetilde\psi_r$ carry no auxiliaries; $\delta_aF_r=\delta_a\widetilde\phi_r
=\delta_a\bar\lambda=0$). $\square$

The surviving bulk assembles, exactly as in the on-shell computation
(4C.58e)–(4C.58h)/(4C.66c2)–(4C.66c4) restricted to the manifest slot, into (5C.8) with
the auxiliary-free primitive

$$
\boxed{
\begin{aligned}
\mathcal S^{\mu}_{L,a}
&=h\operatorname{tr}_{\kappa}\Big[
-iF_{\rho\sigma}(\sigma_L^{\rho\sigma}\sigma_L^\mu\bar\lambda)_a
-\sqrt2\,(\mathcal D_\nu\widetilde\phi_r)(\sigma_L^\nu\bar\sigma_L^\mu\psi_r)_a
-i(\phi_s\times\widetilde\phi_s)(\sigma_L^\mu\bar\lambda)_a
-i\,\varepsilon_{rst}(\widetilde\phi_s\times\widetilde\phi_t)(\sigma_L^\mu\bar\psi_r)_a
\Big],\\
\mathcal S^{m}_{E,a}
&=h\operatorname{tr}_{\kappa}\Big[
+F_{np}(\sigma_E^{np}\sigma_E^m\widetilde\lambda)_a
-\sqrt2\,(\mathcal D_n\widetilde\phi_r)(\sigma_E^n\bar\sigma_E^m\psi_r)_a
-(\phi_s\times\widetilde\phi_s)(\sigma_E^m\widetilde\lambda)_a
-\varepsilon_{rst}(\widetilde\phi_s\times\widetilde\phi_t)(\sigma_E^m\widetilde\psi_r)_a
\Big].
\end{aligned}}
\tag{5C.9}
$$

The boundary coefficient and the exact off-shell divergence statement of the action are
then

$$
\boxed{
K^{M}_{R,a}=C^{M}_{R,a}-\mathcal S^{M}_{R,a},
\qquad
\delta_\varepsilon\mathcal L_R\big|_{\varepsilon}
=\partial_M\big(K^{M}_{R,a}\varepsilon^a\big)
\quad\text{off shell},}
\tag{5C.10}
$$

with the $\vartheta$-sector obeying $C_\vartheta=K_\vartheta$ ((4C.64), (4C.66d)):
the topological term contributes to $C$ and $K$ identically and cancels from the current.

## 4. The currents

### 4.1 Definition and auxiliary-freeness

$$
\boxed{
j^{M}_{R,a}:=C^{M}_{R,a}-K^{M}_{R,a}=\mathcal S^{M}_{R,a},}
\tag{5C.11}
$$

with (5C.9): **the divergence-corrected current is auxiliary-free**, while $C$ and $K$
separately contain identical $\mathscr D$- and $F_r$-terms (e.g. in the pure-SYM slice the
$\mathscr D$-term of (4A.36) equals, by
$\bar\lambda_{\dot c}(\bar\sigma^\mu)^{\dot cb}\epsilon_{ba}
=+(\sigma^\mu)_{a\dot d}\bar\lambda^{\dot d}$, the $\mathscr D$-term of (4A.40) exactly).
This is the precise sense of the owner's statement that the divergence correction makes
the expression cleaner: all auxiliary fields cancel between $C$ and $K$.

### 4.2 Conjugate slots

The mirror computation in the $\bar\varepsilon$ (L) and $\widetilde\varepsilon$ (E) slots
gives

$$
\boxed{
\begin{aligned}
\bar j^{\mu\dot a}_{L}
&=h\operatorname{tr}_{\kappa}\Big[
+iF_{\rho\sigma}(\bar\sigma_L^{\rho\sigma}\bar\sigma_L^\mu\lambda)^{\dot a}
-\sqrt2\,(\mathcal D_\nu\phi_r)(\bar\sigma_L^\nu\sigma_L^\mu\bar\psi_r)^{\dot a}
-i(\phi_s\times\widetilde\phi_s)(\bar\sigma_L^\mu\lambda)^{\dot a}
+i\,\varepsilon_{rst}(\phi_s\times\phi_t)(\bar\sigma_L^\mu\psi_r)^{\dot a}\Big],\\
\widetilde j^{m\dot a}_{E}
&=h\operatorname{tr}_{\kappa}\Big[
-F_{np}(\bar\sigma_E^{np}\bar\sigma_E^m\lambda)^{\dot a}
-\sqrt2\,(\mathcal D_n\phi_r)(\bar\sigma_E^n\sigma_E^m\widetilde\psi_r)^{\dot a}
-(\phi_s\times\widetilde\phi_s)(\bar\sigma_E^m\lambda)^{\dot a}
+\varepsilon_{rst}(\phi_s\times\phi_t)(\bar\sigma_E^m\psi_r)^{\dot a}\Big].
\end{aligned}}
\tag{5C.12}
$$

### 4.3 Consistency reductions

(a) **Pure SYM**: dropping matter, (5C.9)/(5C.12) reduce to the simplified form of the
locked $j=C-K$ of (4A.42)/(4A.55) — a single $F\sigma\sigma\sigma\bar\lambda$-structure —
after applying (4C.71) to combine (4A.36)–(4A.40); the auxiliary term cancels as in §4.1.

(b) **On-shell $SU(4)_R$ currents**: inserting the composites (4C.18)/(4C.61)
[$\mathscr D=-i(\phi_r\times\widetilde\phi_r)$,
$F_r=\frac1{\sqrt2}\varepsilon_{rst}(\widetilde\phi_s\times\widetilde\phi_t)$,
$\widetilde F_r=\frac1{\sqrt2}\varepsilon_{rst}(\phi_s\times\phi_t)$] into the
$\mathcal I{=}4$ slots (4C.60), (4C.64c), (4C.67)$|_{\mathcal I=4}$, (4C.67c)$|_{\mathcal
I=4}$ reproduces (5C.9)/(5C.12) term by term. In other words: **for the manifest
$\mathcal N=1$ supersymmetry of $\mathcal N=4$ SYM, the off-shell Noether current and the
on-shell Noether current are the same local expression** — the auxiliary fields drop out
rather than being replaced by their equations of motion. The Wick maps (4C.69) hold for
(5C.9)/(5C.12) unchanged.

## 5. The off-shell divergence identity: $\partial\cdot j$ as a sum of EOM terms

### 5.1 Off-shell Euler operators

Ordered variations of (4C.14)/(4C.42a) (odd Euler coefficients placed to the right of the
varied field, as in (4A.56c)); adjoint index $C$, flavor $r$:

$$
\boxed{
\begin{aligned}
&\text{L:}\quad
\mathcal E_{\mathscr D}=h\big[\mathscr D+i(\phi_r\times\widetilde\phi_r)\big],\qquad
\mathcal E_{F_r}=h\big[\widetilde F_r-\tfrac1{\sqrt2}\varepsilon_{rst}
(\phi_s\times\phi_t)\big],\qquad
\mathcal E_{\widetilde F_r}=h\big[F_r-\tfrac1{\sqrt2}\varepsilon_{rst}
(\widetilde\phi_s\times\widetilde\phi_t)\big],\\
&\mathcal E_\lambda^{a}=ih(\mathcal D_\mu\bar\lambda_{\dot b})(\bar\sigma_L^\mu)^{\dot ba}
+\sqrt2h\,(\widetilde\phi_r\times\psi_r^{a}),\qquad
\mathcal E_{\bar\lambda}^{\dot a}
=ih(\bar\sigma_L^\mu)^{\dot ab}(\mathcal D_\mu\lambda_b)
+\sqrt2h\,(\phi_r\times\widetilde\psi_r^{\dot a}),\\
&\mathcal E_{\psi_r}^{a}=ih(\mathcal D_\mu\widetilde\psi_{r\dot b})
(\bar\sigma_L^\mu)^{\dot ba}
+\sqrt2h(\widetilde\phi_r\times\lambda^{a})
+\sqrt2h\,\varepsilon_{rst}(\phi_t\times\psi_s^{a}),\\
&\mathcal E_{\widetilde\psi_r}^{\dot a}=ih(\bar\sigma_L^\mu)^{\dot ab}
(\mathcal D_\mu\psi_{rb})
+\sqrt2h(\phi_r\times\widetilde\lambda^{\dot a})
+\sqrt2h\,\varepsilon_{rst}(\widetilde\phi_t\times\widetilde\psi_s^{\dot a}),\\
&\mathcal E_{\phi_r}=h\Big[\mathcal D^\mu\mathcal D_\mu\widetilde\phi_r
+i(\mathscr D\times\widetilde\phi_r)\Big]
+\sqrt2h(\widetilde\psi_r\times\widetilde\lambda)
-\sqrt2h\,\varepsilon_{rst}(F_s\times\phi_t)
+\frac h{\sqrt2}\varepsilon_{rst}(\psi_s\times\psi_t)\cdot(\text{index order as in
(4C.14)}),\\
&\mathcal E_{\widetilde\phi_r}=\ \text{mirror},\qquad
\mathcal E_A^{\nu}=h\Big[\mathcal D_\mu F^{\mu\nu}\Big]+\ \text{matter and gaugino
covariant-current terms (as in (4A.45) extended)},
\end{aligned}}
\tag{5C.13}
$$

and the Euclidean set $\mathcal E_{E,X}$ from (4C.42a) with the sign pattern of
(4A.56c)/(4C.68)–(4C.68a); the $\mathfrak k$-terms drop by (4A.46)/(4A.56d). At this
memo's level of use the bosonic $\mathcal E_A^\nu$, $\mathcal E_{\phi}$,
$\mathcal E_{\widetilde\phi}$ enter $\partial\cdot j$ only through the displayed identity
(5C.14) and are pinned there term by term; the exact check of §7 verifies the complete
set against the action.

### 5.2 The identity

Since (5C.10) holds off shell, the standard local-parameter argument gives, with the
right-strip convention (5C.1) and all Euler coefficients ordered as in (5C.13),

$$
\boxed{
\partial_M\,j^{M}_{R,a}
=-\sum_{X}\;(\pm)_X\,\mathcal E_{R,X}\cdot\delta_aX ,
}
\tag{5C.14}
$$

expanded termwise ($\varepsilon$-slot; every term is an EOM operator times a
transformation coefficient — nothing else survives):

$$
\boxed{
\begin{aligned}
\partial_\mu j^{\mu}_{L,a}
=\operatorname{tr}_\kappa\Big\{&
+i\,\mathcal E_A^{\nu}\,(\sigma_{L\nu}\bar\lambda)_a
+\mathcal E_{\mathscr D}\,(\sigma_L^\rho\mathcal D_\rho\bar\lambda)_a
-\big[(\sigma_L^{\rho\sigma})_b{}^c\epsilon_{ac}F_{\rho\sigma}
-i\epsilon_{ab}\mathscr D\big]\,\mathcal E_\lambda^{b}\\
&+\sqrt2\,\mathcal E_{\phi_r}\,\psi_{ra}
+\sqrt2\,\epsilon_{ab}F_r\,\mathcal E_{\psi_r}^{b}
+i\sqrt2\,(\sigma_L^\mu)_{a\dot a}(\mathcal D_\mu\widetilde\phi_r)\,
\mathcal E_{\widetilde\psi_r}^{\dot a}\\
&-\Big[i\sqrt2\,(\sigma_L^\mu\mathcal D_\mu\widetilde\psi_r)_a
+2(\lambda_a\times\widetilde\phi_r)\Big]\,\mathcal E_{\widetilde F_r}
\Big\},
\end{aligned}}
\tag{5C.15}
$$

$$
\boxed{
\begin{aligned}
\partial_m j^{m}_{E,a}
=\operatorname{tr}_\kappa\Big\{&
-\,\mathcal E_{E,A}^{n}\,(\sigma_{En}\widetilde\lambda)_a
+i\,\mathcal E_{E,\mathscr D}\,(\sigma_E^n\mathcal D_n\widetilde\lambda)_a
+\big[(\sigma_E^{np})_b{}^c\epsilon_{ac}F_{np}
+i\epsilon_{ab}\mathscr D\big]\,\mathcal E_{E,\lambda}^{b}\\
&+\sqrt2\,\mathcal E_{E,\phi_r}\,\psi_{ra}
+\sqrt2\,\epsilon_{ab}F_r\,\mathcal E_{E,\psi_r}^{b}
-\sqrt2\,(\sigma_E^m)_{a\dot a}(\mathcal D_m\widetilde\phi_r)\,
\mathcal E_{E,\widetilde\psi_r}^{\dot a}\\
&+\Big[\sqrt2\,(\sigma_E^m\mathcal D_m\widetilde\psi_r)_a
-2(\lambda_a\times\widetilde\phi_r)\Big]\,\mathcal E_{E,\widetilde F_r}
\Big\},
\end{aligned}}
\tag{5C.16}
$$

with the mirror identities for $\partial\bar j_L$, $\partial\widetilde j_E$. Structural
facts, visible directly in (5C.15)–(5C.16):

1. **Which EOMs appear**: exactly those of the fields whose $\varepsilon$-slot
   transformation is nonzero — $A$, $\lambda$, $\mathscr D$, $\phi_r$, $\psi_r$,
   $\widetilde\psi_r$, $\widetilde F_r$. The operators $\mathcal E_{\bar\lambda}$,
   $\mathcal E_{\widetilde\phi}$, $\mathcal E_{F}$ are absent (their fields have
   $\delta_a X=0$); they appear instead in the conjugate-slot identities.
2. **Auxiliary EOMs appear even though the current has no auxiliaries**: the terms
   $\mathcal E_{\mathscr D}(\sigma\mathcal D\bar\lambda)$,
   $F_r\,\mathcal E_{\psi_r}$, $[\dots]\mathcal E_{\widetilde F_r}$ vanish only on the
   auxiliary shell. On that shell ($\mathcal E_{\mathscr D}=\mathcal E_{F}
   =\mathcal E_{\widetilde F}=0$, auxiliaries at (4C.18)) the identities collapse to the
   $\mathcal I{=}4$ slots of the locked on-shell divergences (4C.66)/(4C.69a).
3. **Pure-SYM truncation** reproduces (4A.47)/(4A.56e) exactly.
4. These identities are the exact classical input for the Step-5D Ward identity: every
   term on the right is a typed EOM insertion, which under the path integral collapses to
   contact terms by the Schwinger–Dyson identity (3D.31)/(3D.34) — and fails to collapse,
   under DRED, by exactly one evanescent insertion per line (the Step-5 anomaly
   mechanism).

## 6. Decision and gap ledger

No new convention decision is required by this memo: (5C.2)–(5C.3) are locked
transformations, and the Noether construction introduces no scheme choice beyond the
parameter-order convention (5C.1) ($=$ (2A.9)). Gap closed: 4B/4C recorded Noether
currents only in the on-shell / $SU(2)_R$- or $SU(4)_R$-covariant bases; the off-shell
manifest-$\mathcal N=1$ currents (5C.9)/(5C.12) and the off-shell divergence identities
(5C.15)–(5C.16) were previously absent in both signatures.

## 7. Equation-anchored exact checks

To be appended to `tests/test_step5b_feynman_rules.py` (same CI gate; jet-space engine,
su(2) structure constants $c_{ABC}=\varepsilon_{ABC}$, $\kappa_{AB}=\delta_{AB}$):

| test | checks |
|---|---|
| B1 | (5C.10) — $\delta_\varepsilon\mathcal L_R|_\varepsilon-\partial(K\varepsilon)=0$ off shell, both signatures, $\varepsilon$- and conjugate slots |
| B2 | (5C.15)/(5C.16) — $\partial\cdot j+\sum\mathcal E\cdot\delta_a=0$ off shell, both signatures |
| B3 | (5C.9)/(5C.12) — structural: the currents contain no $\mathscr D,F,\widetilde F$ |
| B4 | §4.3(b) — composite substitution reproduces the $\mathcal I{=}4$ slots of (4C.60)/(4C.64c)/(4C.67)/(4C.67c) |
