# Step-5J memo — the letter dictionary derived from the HT source, and the tree-level cross-lock of the three channels

Status: `NON_AUTHORITY_PROPOSAL`. Numbered items (5J.$n$). This memo does the dictionary
derivation the owner requested and cross-locks the three executed channels — but at the
level the physics actually permits without a full loop recomputation, and it is explicit
about that boundary. The central result is rigorous and sympy-verified; the honest
residual is stated in §5.

**Result in one line.** The HT source gives a **unit-magnitude field dictionary** in the
component basis (no √2 renormalization freedom); tree-level matching of the classical
brackets then *derives* the single remaining dictionary factor — the overall differential
normalization $\zeta_Q=\tfrac12$ — from first principles, reproducing the review's
recorded $Q_0\leftrightarrow-\tfrac12\boldsymbol\nabla_-$. This cross-locks the **overall
scale** of all three channels simultaneously. The **relative** factors between channels
remain a parameter-free loop test, which exposes an error in the 5G topology (§4) and is
therefore *not yet passed*.

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
$\mathfrak f=f_{++}$ — each identification is a **field-content** identity of
**unit magnitude** (up to a phase/sign): $\gamma^r\!=\!\zeta_\gamma\widetilde\phi_r$ with
$|\zeta_\gamma|=1$ ($\Phi^{4r}$ is $\pm\phi_r$/$\pm\widetilde\phi_r$ with unit coefficient
from (4.24)/(4.27)); likewise $|\zeta_\beta|=|\zeta_d|=|\zeta_b|=|\zeta_\partial|=1$.

**Why the review's √2's are not a contradiction (5J.1a).** The review R.6-5 recorded
$\beta\leftrightarrow\tfrac1{\sqrt2}B$, $b\leftrightarrow-\tfrac i{\sqrt2}A$ with
$B=\boldsymbol\nabla_+\Phi$, $A=\boldsymbol\nabla_+\mathcal W_+$ — the **superfield-letter**
basis. Since $\psi_{r+}=\tfrac1{\sqrt2}\boldsymbol\nabla_+\Phi_r|=\tfrac1{\sqrt2}B|$, the
√2 is precisely the superfield-to-component projection factor; in the **component** basis
used by the Step-5G/H computation the √2 is already spent and the dictionary is unit. So
there is **no per-letter renormalization freedom** in the component computation — a fact
that makes the cross-lock unforgiving (§3).

## 2. The tree bracket to match

Project side, $\mathbf Q=Q^4_-$ acting on the $+$-fermion (component basis, right-strip
(5C.1)), from the locked (5C.3)/(4C.46) with $\epsilon_{12}=-1$ so
$\varepsilon_+=\varepsilon_{a=1}=\epsilon_{12}\varepsilon^2=-\varepsilon^-$:

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

With the unit field dictionary of §1 ($\zeta_\beta=\zeta_\gamma=1$) and the natural
structure-constant identification $f_{\rm HT}=c_{\rm proj}$ ($\rho_{fc}=1$, the source's
"$\sim$" at unit), this **derives**

$$
\boxed{\ \zeta_Q=\tfrac12\ ,}
\tag{5J.6}
$$

i.e. $Q_0\leftrightarrow\tfrac12\,Q_-$ (equivalently the review's
$Q_0\leftrightarrow-\tfrac12\boldsymbol\nabla_-$, magnitude reproduced from first
principles — the sign is in the phase class, §5). **Sympy verification** (structure
constants $=\varepsilon_{ABC}$ on su(2), ordered sums as they appear in the locked
formulas): the project ordered sum $\sqrt2\,F_r$ is exactly $2\times$ the HT
$\tfrac12\varepsilon[\gamma,\gamma]$, giving ratio $2$ hence $\zeta_Q=1/2$ — confirmed
exactly, no residual.

**What this locks.** $\zeta_Q$ is the **overall** differential normalization common to
every channel; (5J.6) therefore fixes the common scale $P=\kappa^2\eta_{\mathcal
D}/\zeta_Q$ of all three one-loop channels **simultaneously** from a single tree
computation — the cross-lock of the absolute scale. It also settles, from first
principles, the review's remaining-trust-surface item R.6-5 (the $Q_0$-normalization
half of it) and is consistent with the factor-2 family of adjudications (this
$\zeta_Q=\tfrac12$ is the **differential** normalization, distinct from the
zero-shift-kernel factor-2 of `HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO`; the two must not
be conflated).

## 4. Correction to Step-5G exposed by taking the dictionary seriously

Because §1 removes all renormalization freedom, the relative factors between channels
must come out uniform from the **honest** loop coefficients — so any spurious relative
factor is a computational error, not a normalization to be absorbed. Re-examining the
provisional backbones under this constraint exposes:

- **(5J.4a) topology error in 5G.** Step-5G drew the $(\mathfrak b,\mathfrak c)$ graph as
  a **box** (four internal lines, insertion $+$ **two** $V_2$ vertices, nodes
  $x\!-\!w_1\!-\!y\!-\!w_2$). The correct object — matching both the owner's
  "insertion $+$ **one** interaction vertex" and the HT triangle (letter pair at one
  node, interaction data at the other two) — is a **triangle** (three internal lines,
  insertion $+$ one $V_2$). The box carried an extra $(\sqrt2h/\hbar)(\hbar g^2)$ worth
  of factors, so the 5G/5H backbone √2-powers are **unreliable** and must be recomputed
  on the triangle. The *structure* results of 5G (collapse localization, output tensor
  $\widetilde\lambda\widetilde\lambda$, flavor $\delta_{rs}$, $1/32\pi^2$) are unaffected;
  the *rational coefficient* is withdrawn pending the triangle recomputation.

This is the concrete instance of the honesty caveat of the previous turn: the backbone
numbers were provisional, and the dictionary derivation — by removing the freedom to hide
behind normalization — is exactly what makes the error visible.

## 5. Honest status of the cross-lock

- **Locked (rigorous, sympy-verified):** unit field dictionary (component basis, §1);
  overall differential normalization $\zeta_Q=\tfrac12$ (5J.6), which cross-locks the
  common scale of all three channels and reproduces the review's $Q_0$-factor from first
  principles. Phases/signs of the field ζ's (and of $\zeta_Q$) are **not** pinned by the
  magnitude computation and sit in the global $\varsigma$ class.
- **Not yet passed:** the *relative* one-loop factors ($c_3\!:\!c_4\!:\!c_5$) — the test
  that the three channels collapse to a *single* $\kappa^2$ after the common $\zeta_Q$.
  This requires the honest triangle coefficients, and the 5G box error (5J.4a) means the
  current √2-powers cannot be used. The correct statement is: with the dictionary now
  parameter-free, the relative-factor uniformity is a **clean prediction to be checked**
  by the triangle recomputation — there is no longer any normalization freedom that could
  make a mismatched computation "fit."

## 6. The next bounded step (delegated, now unambiguous)

Recompute the three executed channels' coefficients on the **triangle** topology
(insertion $+$ one $V_2$), with the unit component dictionary and $\zeta_Q=\tfrac12$:

- **W-J1**: the $(\mathfrak b_r,\mathfrak c^s)$ triangle → coefficient $c_3$; target
  $\kappa^2 f_{ACD}f_{BCE}\,\widetilde\lambda\widetilde\lambda$ (HT T3).
- **W-J2/J3**: $(\mathfrak b,\mathfrak b)$ and $(\mathfrak f,\mathfrak c)$ triangles →
  $c_4,c_5$; check $c_3=c_4=c_5=\kappa^2$ after the common $\zeta_Q$ (the uniformity /
  cross-lock verdict).
- **W-J4**: propagate the corrected topology into 5G/5H (replace box by triangle
  everywhere; the census, collapse, and tensor results stand).

Only when W-J1–J3 return equal coefficients is the numeric reproduction of the HT
zero-shift table achieved for the matter channels; the gauge channels (T2/T6) and the
tower then follow per Step-5H/5I.
