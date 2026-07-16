# Step-5J memo — the letter dictionary derived from the HT source, and the tree-level cross-lock of the three channels

Status: `NON_AUTHORITY_PROPOSAL`. Numbered items (5J.$n$). This memo does the dictionary
derivation the owner requested and cross-locks the three executed channels — but at the
level the physics actually permits without a full loop recomputation, and it is explicit
about that boundary.

> **ERRATA (adversarial review, 2026-07-16 — corrections to this memo's own first draft).**
> An adversarial pass refuted two headline claims of the draft below; both are corrected
> here and the surviving result is narrowed:
> - **(E-i) The "unit-magnitude, no √2 freedom" headline is false for the
>   $\mathcal W$-multiplet letter $\mathfrak f=f_{++}$.** The √2 argument of §1 holds for
>   the **$\Phi$-multiplet** letters ($\beta,\gamma,\mathfrak d$: each is a component
>   $\psi=\tfrac1{\sqrt2}\boldsymbol\nabla_+\Phi|$ so the superfield √2 is spent), but
>   $f_{++}=\tau_E^{-1}\boldsymbol\nabla_+\mathcal W_+|$ carries **no** projection √2,
>   while the review's $b\leftrightarrow-\tfrac i{\sqrt2}\boldsymbol\nabla_+\mathcal W_+$
>   does — so $|\zeta_b|=1/\sqrt2$, **not** 1, and a residual √2 survives in every
>   $(\mathfrak f,\cdot)$ channel. The unit-dictionary claim is restricted to
>   $\{\beta,\gamma,\mathfrak d\}$; $\zeta_b$ needs the propagator/twist normalization.
> - **(E-ii) The §4 "5G box → triangle correction" is retracted.** It is not a settled
>   error but an **unresolved** box-vs-triangle question: 5G's box uses a *colorless*
>   kinetic insertion $\mathcal I_6^{\rm kin}$ with **two** vertices (building
>   $f_{ACD}f_{BCE}$ from the two vertices); 5H's triangle uses a *color-carrying*
>   insertion ($\mathcal I_6^Y,\mathcal I_7^W\propto c$) with **one** vertex. These are
>   **different graphs from different pieces of the same $\partial\!\cdot\!j$ insertion**,
>   and both may contribute to the channel. Replacing the box by a one-vertex triangle
>   *keeping the colorless collapse insertion* would give only one structure constant —
>   color-inconsistent. The correct statement: the channel's full graph set (boxes **and**
>   triangles) must be assembled together; neither 5G nor 5H alone is complete. See §4
>   (rewritten).
> - **(E-iii) $\zeta_Q=\tfrac12$ is contingent, not unconditional.** (5J.5) gives
>   $\zeta_Q=\rho_{fc}/2$; the value $\tfrac12$ holds under the identification
>   $\rho_{fc}=1$ (HT structure constant $=$ project $c$). This is *defensible* — the
>   source's **tree** $Q_0$ bracket carries no explicit $\kappa$ (the $\kappa$ appears
>   only in $W$ and at one loop) — but it is an **assumption**, not a derivation. The
>   sympy check validates the **factor-2 arithmetic** ($\sqrt2F_r=2\cdot\tfrac12\varepsilon
>   [\gamma,\gamma]$), not the inputs $\rho_{fc}=1$ or $\gamma=\widetilde\phi$.
>
> Robust surviving result: the tree bracket pins $\zeta_Q\zeta_\beta/\zeta_\gamma^2
> =\rho_{fc}/2$; with the $\Phi$-multiplet letters unit and $\rho_{fc}=1$ this gives
> $\zeta_Q=\tfrac12$, matching the review's recorded $Q_0$-factor. The rest of this memo
> is the draft, read through the errata above.

**Result in one line (corrected).** In the **component basis** the $\Phi$-multiplet
letters $\{\beta,\gamma,\mathfrak d\}$ carry a **unit** field dictionary; tree-level
bracket matching then pins $\zeta_Q=\rho_{fc}/2$, giving the differential normalization
$\zeta_Q=\tfrac12$ under $\rho_{fc}=1$ — reproducing the review's
$Q_0\leftrightarrow-\tfrac12\boldsymbol\nabla_-$ and cross-locking the **overall scale**
of the three channels. The $\mathcal W$-letter $\zeta_b$ and the **relative** channel
factors remain open (E-i, E-ii); the numeric cross-lock is **not yet passed**.

---

## 1. The dictionary is fixed by the source, not chosen (unit magnitude, component basis)

The admitted reference states its own field identification
(`main.tex` §3.4, the $\mathcal N=4$ subsection, twisting supercharge
$\mathbf Q=Q^4_-$), verbatim:

$$
\gamma^I\sim\Phi^{4I},\qquad
\beta_I\sim\Psi_{I+},\qquad
\partial_{\dot\alpha}c\sim\bar\Psi^4_{\dot\alpha},\qquad
b\sim F_{++},\qquad
\partial_{\dot\alpha}\sim D_{+\dot\alpha}.
\tag{5J.1}
$$

Matched to the project component letters (5D.2) — $\mathfrak c^r=\widetilde\phi_r$,
$\mathfrak b_r=\psi_{r+}$, $\mathfrak d_{\dot a}=\widetilde\lambda_{\dot a}$,
$\mathfrak f=f_{++}$. For the **$\Phi$-multiplet letters** each identification is a
**field-content** identity of **unit magnitude** (up to a phase/sign):
$\gamma^r\!=\!\zeta_\gamma\widetilde\phi_r$ with $|\zeta_\gamma|=1$ (the source object is
$\Phi^{4r}=\varphi^{4r}=-\phi_r$ by (4.27)–(4.29), unit coefficient; the project letter is
$\widetilde\phi_r$, and choosing $\gamma=\widetilde\phi$ rather than the source's
$\gamma\sim-\phi$ is a genuine Euclidean choice — $\phi_r,\widetilde\phi_r$ are
**independent** on the Euclidean contour (4C.53) — fixed by requiring the tree bracket
(5J.2) to close; unit magnitude either way); likewise $|\zeta_\beta|=|\zeta_d|=1$.
The **$\mathcal W$-multiplet letter is different**: $\mathfrak f=f_{++}$ carries no
projection √2 (see E-i), so $|\zeta_b|=1/\sqrt2$, not 1 — the residual √2 of the
$(\mathfrak f,\cdot)$ channels lives here and is **not** removed by this section.

**Why the review's √2's mostly reduce to projections (5J.1a).** The review R.6-5 recorded
$\beta\leftrightarrow\tfrac1{\sqrt2}B$, $b\leftrightarrow-\tfrac i{\sqrt2}A$ with
$B=\boldsymbol\nabla_+\Phi$, $A=\boldsymbol\nabla_+\mathcal W_+$ — the **superfield-letter**
basis. For $\beta$: since $\psi_{r+}=\tfrac1{\sqrt2}\boldsymbol\nabla_+\Phi_r|
=\tfrac1{\sqrt2}B|$, the √2 is exactly the superfield-to-component projection and
$\beta\leftrightarrow\psi_{r+}$ is unit in the component basis. For $b$: since
$f_{++}=\boldsymbol\nabla_+\mathcal W_+|$ has **projection coefficient 1** (no √2, unlike
$\psi$), the review's $\tfrac1{\sqrt2}$ is **not** absorbed and $|\zeta_b|=1/\sqrt2$
survives (E-i). So the component dictionary is unit for $\{\beta,\gamma,\mathfrak d\}$ but
carries a real $1/\sqrt2$ for $\mathfrak f$ — the (E-i) correction.

## 2. The tree bracket to match

Project side, $\mathbf Q=Q^4_-$ acting on the $+$-fermion (component basis, right-strip
(5C.1)), from the locked explicit-auxiliary transformation (4B.33b)/(4C.28) — the
$-\sqrt2\,\varepsilon_aF_r$ term is in the off-shell-auxiliary form (4B.33b), **not** the
auxiliary-eliminated (4C.46) — with $\epsilon_{12}=-1$ so
$\varepsilon_+=\varepsilon_{a=1}=\epsilon_{12}\varepsilon^2=-\varepsilon^-$ (this sign
convention is the one that yields $+\sqrt2F_r$; the companion memo (5D.3) strips with
$\varepsilon_{-+}=+1$ and records $-\sqrt2F_r$ — the two differ only by the overall phase
class, §5, not by magnitude):

$$
\delta\psi_{ra}=-\sqrt2\,\varepsilon_aF_r+\dots
\ \Longrightarrow\
Q_-\psi_{r+}=-\sqrt2\,\varepsilon_+F_r/\varepsilon^-
=+\sqrt2\,F_r
\overset{(4C.18)}{=}\varepsilon_{rst}(\widetilde\phi_s\times\widetilde\phi_t)
\quad\text{[ordered $s,t$ sum]},
\tag{5J.2}
$$

the last step on the auxiliary shell $F_r=\tfrac1{\sqrt2}\varepsilon_{rst}
(\widetilde\phi_s\times\widetilde\phi_t)$; the $\sqrt2$ of $\delta\psi$ and the
$1/\sqrt2$ of $F_r$ **cancel exactly** (unit — no residual √2 on the project side).

HT side, from the source $Q_0$:

$$
Q_0\beta_I=[c,\beta_I]+\tfrac12\varepsilon_{IJK}[\gamma^J,\gamma^K],
\tag{5J.3}
$$

whose letter-mixing part is $\tfrac12\varepsilon_{rst}[\gamma^s,\gamma^t]$ (the $[c,\cdot]$
is gauge transport, matched separately). Both sides carry the same $\varepsilon_{rst}$
and the same structure-constant contraction, so the comparison is a pure numeric factor.

## 3. The cross-lock: $\zeta_Q=\tfrac12$ derived, all channels' scale locked

Writing $\psi_{r+}=\zeta_\beta^{-1}\beta_r$, $\widetilde\phi=\zeta_\gamma^{-1}\gamma$,
$Q_-=\zeta_Q^{-1}Q_0$, and $[\gamma^s,\gamma^t]^A=\rho_{fc}(\gamma^s\times\gamma^t)^A$
(the HT-$f$ / project-$c$ structure-constant ratio), (5J.2)→HT variables gives

$$
Q_0\beta_r=\frac{\zeta_Q\zeta_\beta}{\zeta_\gamma^2}\,
\varepsilon_{rst}(\gamma^s\times\gamma^t)\quad\text{[ordered]},
\qquad\text{vs}\qquad
\tfrac12\varepsilon_{rst}[\gamma^s,\gamma^t]
=\tfrac{\rho_{fc}}2\varepsilon_{rst}(\gamma^s\times\gamma^t),
\tag{5J.4}
$$

so the tree relation pins the combination

$$
\boxed{\ \frac{\zeta_Q\zeta_\beta}{\zeta_\gamma^2}=\frac{\rho_{fc}}{2}\ .}
\tag{5J.5}
$$

With the $\Phi$-multiplet letters unit ($\zeta_\beta=\zeta_\gamma=1$; $\beta,\gamma$ are
the only letters in this bracket, so the $\zeta_b$ issue of E-i does **not** enter here)
and the structure-constant identification $f_{\rm HT}=c_{\rm proj}$ ($\rho_{fc}=1$),

$$
\boxed{\ \zeta_Q=\frac{\rho_{fc}}{2}\ \overset{\rho_{fc}=1}{=}\ \tfrac12\ ,}
\tag{5J.6}
$$

i.e. $Q_0\leftrightarrow\tfrac12\,Q_-$ (equivalently the review's
$Q_0\leftrightarrow-\tfrac12\boldsymbol\nabla_-$, magnitude — the sign is in the phase
class, §5). **On $\rho_{fc}=1$ (E-iii):** the identification is *defensible* — the source's
**tree** $Q_0$ bracket (main.tex) is the plain $[\gamma,\gamma]$ with no explicit
$\kappa$ (the $\kappa$ enters only in $W$ and at one loop) — but it is an assumption, not
a theorem; any structure-constant mismatch flows into $\zeta_Q$ via (5J.5). **Sympy
scope** (`scripts/check_step5j_tree_crosslock.py`, structure constants
$=\varepsilon_{ABC}$ on su(2), $\gamma=\widetilde\phi$ baked in): it validates the
**factor-2 arithmetic** — the project ordered sum $\sqrt2\,F_r$ is exactly $2\times$ the
HT $\tfrac12\varepsilon[\gamma,\gamma]$ — **not** the physics inputs $\rho_{fc}=1$ or
$\gamma=\widetilde\phi$, which are argued in prose above.

**What this locks.** $\zeta_Q$ is the **overall** differential normalization common to
every channel; (5J.6) therefore fixes the common scale $P=\kappa^2\eta_{\mathcal
D}/\zeta_Q$ of all three one-loop channels **simultaneously** from a single tree
computation — the cross-lock of the absolute scale (modulo $\rho_{fc}$, E-iii). It
addresses, up to that assumption, the review's remaining-trust-surface item R.6-5 (the
$Q_0$-normalization half of it) and is consistent with the factor-2 family of adjudications
(this
$\zeta_Q=\tfrac12$ is the **differential** normalization, distinct from the
zero-shift-kernel factor-2 of `HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO`; the two must not
be conflated).

## 4. The box-vs-triangle graph set (rewritten per E-ii)

The color word of every matter channel is $f_{ACD}f_{BCE}$ — **two** structure constants
(HT T3/T5). A one-loop graph reaches two structure constants in two distinct ways, and
**both** occur as different pieces of the same $\partial\!\cdot\!j_-$ insertion:

- **(4a) colorless-insertion box.** The *kinetic* insertion piece $\mathcal I_6^{\rm kin}$
  is a colour singlet; it builds $f_{ACD}f_{BCE}$ from **two** interaction vertices
  $V_2$ — the box of 5G §4 (nodes $x\!-\!w_1\!-\!y\!-\!w_2$, four internal lines). Its
  anomaly is the $\mu^2$-branch of the internal $\psi\widetilde\psi$-line collapse
  (5G.7–5G.11).
- **(4b) color-carrying-insertion triangle.** The *Yukawa/superpotential* insertion
  pieces $\mathcal I_6^{Y},\mathcal I_7^{W}\propto c$ carry **one** structure constant;
  combined with **one** vertex $V_2$ they give $f\!f$ on a **triangle** (three internal
  lines) — the graphs of 5H.

These are **not** the same graph, and (E-ii) retracts the first draft's claim that the
box was an "error corrected to a triangle." Neither 5G (box only) nor 5H (triangle only)
is the complete channel: the honest one-loop coefficient is the **sum** of (4a) and (4b)
(plus the classical-closure partners of each, which cancel). The owner's "one interaction
vertex / all triangles" picture is the (4b) family; whether (4a) contributes independently
or is a redundant description of the same physics (e.g. the box's collapse-"1" branch
reducing it to a triangle configuration) is the open question — it must be settled by the
full assembly, not by picking one topology. The *structure* results common to 5G/5H
(collapse localization, output tensor $\widetilde\lambda\widetilde\lambda$, flavor
$\delta_{rs}$, $1/32\pi^2$) stand; the *rational coefficient* is open until (4a)+(4b) are
assembled together.

This is the concrete instance of the honesty caveat of the previous turn, sharpened by the
adversarial pass: the backbone numbers were provisional; the dictionary derivation
narrows the freedom, and the adversarial pass shows the graph set itself was not yet
pinned.

## 5. Honest status of the cross-lock (post-adversarial)

- **Locked (rigorous, sympy-verified within its scope):** the $\Phi$-multiplet field
  dictionary is unit in the component basis (§1, restricted per E-i); the tree bracket
  pins $\zeta_Q\zeta_\beta/\zeta_\gamma^2=\rho_{fc}/2$ (5J.5), giving the differential
  normalization $\zeta_Q=\tfrac12$ under $\rho_{fc}=1$ (5J.6) — reproducing the review's
  $Q_0$-factor. The sympy check verifies the factor-2 arithmetic; $\rho_{fc}=1$ and
  $\gamma=\widetilde\phi$ are argued in prose (E-iii, A3), not machine-checked. Phases/signs
  sit in the global $\varsigma$ class.
- **Open:** (i) the $\mathcal W$-letter normalization $\zeta_b$ ($=1/\sqrt2$ per the
  review, needs the propagator/twist derivation — E-i); (ii) the *relative* one-loop
  factors $c_3\!:\!c_4\!:\!c_5$, which need the honest **full graph set** — boxes (4a) and
  triangles (4b) assembled together (E-ii), not one topology chosen; (iii) $\rho_{fc}$ vs
  the $\kappa$ normalization of the color word (E-iii, tied to the review's R.6-2). The
  numeric cross-lock is **not yet passed**.

## 6. The next bounded steps (delegated)

- **W-J0** (E-ii resolution, prerequisite): enumerate the **complete** one-loop graph set
  of the $(\mathfrak b,\mathfrak c)$ channel — the colorless-kinetic-insertion boxes (4a)
  **and** the color-carrying-insertion triangles (4b) — and settle whether they are
  independent contributions or a redundant description (the box collapse-"1" branch vs the
  triangle). Only then is the topology fixed.
- **W-J1–J3**: with the graph set of W-J0, assemble $c_3,c_4,c_5$ using the unit
  $\Phi$-dictionary, $\zeta_Q=\tfrac12$, and $\zeta_b$ from a propagator match; check
  $c_3\!:\!c_4\!:\!c_5$ collapse to a single $\kappa^2 f_{ACD}f_{BCE}$ (HT T3/T4/T5) — the
  uniformity verdict.
- **W-J4** ($\zeta_b$, E-i): derive the $\mathcal W$-letter normalization from matching
  the $\langle f_{++}f_{++}\rangle$ / $bc$ free two-point functions.
- **W-J5** ($\rho_{fc}$, E-iii): pin the HT-$f$/project-$c$ ratio and the absolute
  $\kappa$ from a channel where the color word is unambiguous.

Only when W-J0–J3 return equal coefficients is the numeric reproduction of the HT
zero-shift table achieved for the matter channels; the gauge channels (T2/T6) and the
tower then follow per Step-5H/5I.
