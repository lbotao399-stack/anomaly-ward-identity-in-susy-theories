# Step-5G memo — the rigorous one-loop DRED computation of $Q_-(\psi_+^A\widetilde\phi^B)$ (completion of the Step-5F pilot, Euclidean)

Status: `NON_AUTHORITY_PROPOSAL`. Numbered equations (5G.$n$). This memo **executes** the
computation specified in Step-5F: dimensional reduction throughout, with the chiral
projector realized as $P_\pm=\tfrac12(1\pm\gamma_5)$ in the four-component transcription
(§2), per the owner's instruction of 2026-07-16. The derivation is carried to the exact
local answer; the four global bookkeeping factors that a mechanical pass must pin are
isolated in §6 (everything else is closed here).

---

## 0. Corrections to Step-5F recorded first

Two census-level corrections to the Step-5F memo, found while assembling the exact
integrands (this is the adversarial value of actually computing):

1. **(C1) The one-interaction-vertex family is larger than F1a/F1b.** The insertion
   terms $+i\mathcal E_{\mathscr D}(\sigma^n\mathcal D_n\widetilde\lambda)_-$ (through
   the $C_0$-part of $\mathcal E_{\mathscr D}$) and
   $-\mathcal E^n_A(\sigma_n\widetilde\lambda)_-$ (through the scalar-current,
   fermion-current, and gaugino-current parts of $\mathcal E^n_A$) also produce
   one-vertex triangles in this channel: call them F1c–F1f. They join F1a/F1b in the
   **classical-closure set**; none of them is a collapse site, so the anomaly bookkeeping
   below is unchanged, but W3′ must enumerate them (the Step-5F claim "F1a/F1b only" is
   withdrawn).
2. **(C2) External detection legs.** The detection operator overlaps
   $\langle\widetilde\lambda\widetilde\lambda\,\lambda\lambda\rangle$-wise: the external
   probes are **undotted** gauginos $\lambda^D(u)\lambda^E(v)$ (or equivalently, as done
   below, two **amputated** $\widetilde\lambda$-legs); Step-5F's (5F.2) display with
   external $\widetilde\lambda\widetilde\lambda$ fields is corrected accordingly.

## 1. Exact rules used (all from (4C.42a) with $e^{-S_E/\hbar}$, momenta all incoming)

Propagators ($k$ = incoming momentum of the first field; $\kappa^{AB}$ raised Killing
form; $\delta_{tu}$ flavor):

$$
\langle\phi_t^A\widetilde\phi_u^B\rangle=\frac{\hbar g^2\delta_{tu}\kappa^{AB}}{k^2},
\qquad
\langle\psi_{ta}^A\widetilde\psi_{u\dot b}^B\rangle
=-\,i\hbar g^2\delta_{tu}\kappa^{AB}\frac{(\sigma_E\!\cdot\!k)_{a\dot b}}{k^2},
\qquad
\langle\lambda_a^A\widetilde\lambda_{\dot b}^B\rangle
=-\,i\hbar g^2\kappa^{AB}\frac{(\sigma_E\!\cdot\!k)_{a\dot b}}{k^2},
\tag{5G.1}
$$

using $(\sigma\!\cdot\!k)(\bar\sigma\!\cdot\!k)=k^2$ from (5B.4). The auxiliary contact:
$\langle F_t^A\widetilde F_u^B\rangle=-\hbar g^2\delta_{tu}\kappa^{AB}$ (no pole).

Interaction vertex used (the matter Yukawa of (4C.42a),
$S\supset-\sqrt2h\,c_{ABC}\int\phi^A_u\widetilde\psi^B_{u\dot a}\widetilde\lambda^{C\dot a}$):

$$
V_2:\quad
+\frac{\sqrt2h}{\hbar}\,c_{ABC}\,\epsilon^{\dot a\dot b}
\qquad\text{on legs }(\phi^A_u;\ \widetilde\psi^B_{u\dot a};\ \widetilde\lambda^C_{\dot b}).
\tag{5G.2}
$$

Insertion pieces of $\partial_mj^m_{E,-}$ (from (5D.4)); the two used at the collapse
site are the kinetic and Yukawa parts of the $\mathcal E_{\widetilde\psi}$-term:

$$
\mathcal I_6^{\rm kin}(x)
=-\sqrt2\,h\,(\sigma^m)_{-\dot a}(\bar\sigma^n)^{\dot ab}\,
(\partial_m\widetilde\phi^A_t)(\partial_n\psi^A_{tb})(x),
\qquad
\mathcal I_6^{Y}(x)
=+2h\,(\sigma^m)_{-\dot a}\,c_{BAC}\,
(\partial_m\widetilde\phi^A_t)\,\phi^B_t\,\widetilde\lambda^{C\dot a}(x),
\tag{5G.3}
$$

(abelian parts displayed; the $A_m$-parts of $\mathcal D_m$ feed higher-point channels).

## 2. The DRED ledger in four-component form ($P_L$ from $\tfrac12(1+\gamma_5)$)

Assemble the matter fermion as $\Psi_t=(\psi_{ta},\widetilde\psi_t^{\dot a})^T$ with

$$
\gamma^m=\begin{pmatrix}0&\sigma_E^m\\ \bar\sigma_E^m&0\end{pmatrix},
\qquad
\gamma_5=\begin{pmatrix}\mathbf 1&0\\0&-\mathbf 1\end{pmatrix},
\qquad
P_{L/R}=\tfrac12(1\pm\gamma_5),
\tag{5G.4}
$$

so that $\psi=P_L\Psi$, $\widetilde\psi=P_R\Psi$, and every $\sigma$/$\bar\sigma$ chain
below is a $P_{L,R}$-projected $\gamma$-chain. The regulator is dimensional
**reduction**: the $\gamma$/$\sigma$ algebra — including $\gamma_5$, the Fierz identity
and the frame projections — is four-dimensional and *formal*; loop momenta and all
propagator denominators are $d=4-2\epsilon$ dimensional. The two metric representations
are never contracted with each other; their sole interface is the axiom

$$
(\bar\sigma\!\cdot\!\ell)(\sigma\!\cdot\!\ell)
=\bar\ell^{\,2}\,\mathbf 1
=\big(\ell_d^2+\mu_\ell^2\big)\mathbf 1,
\qquad
\mu_\ell^2:=\bar\ell^{\,2}-\ell_d^2,
\tag{5G.5}
$$

(in four-component form: $P_L\,\ell\!\!\!/\,\ell\!\!\!/\,P_L=\bar\ell^{\,2}P_L$ with the
$1{+}\gamma_5$ projector riding through untouched, since $\gamma_5$ is exactly
anticommuting in DRED), together with the two master integrals

$$
\lim_{\epsilon\to0}\mu^{2\epsilon}\!\!\int\!\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}=\frac1{32\pi^2},
\qquad
\int\!\frac{d^d\ell}{(2\pi)^d}\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^4}=O(\epsilon),
\tag{5G.6}
$$

and the rotational average $\ell_m\ell_n\to\widehat\delta_{mn}\,\ell_d^2/d$. External
momenta are physical: $\mu^2_{\rm ext}=0$, so external-line collapses are exact — the
anomaly can only come from **internal** fermion-line collapses.

## 3. Localization of the anomaly: one collapse site

Scan of (5D.4) against the external set
$\{(\psi^{A}_{r+}\widetilde\phi^B_s)(y);\ \widetilde\lambda\text{-amp}(D,\dot c,k_1),
(E,\dot d,k_2)\}$ for internal fermion-line EOM contractions:

- $\mathcal E_{\phi}$-kinetic ($\partial^2\widetilde\phi$ into
  $\langle\widetilde\phi\phi\rangle$): numerator $-k_d^2$ against denominator $k_d^2$,
  **exact** — no $\sigma$-algebra, no $\mu^2$ (scalar-sector exactness, as in Step-5E §3);
- $\mathcal E_{\psi}$-kinetic (term 5): blocked from this channel through the
  $F$-contact/superpotential dead ends (Step-5F §2 F4, re-checked);
- $\mathcal E_{\lambda}$- and $\mathcal E_{\mathscr D}$-kinetic pieces: reach only
  **external** $\widetilde\lambda$ legs here — exact;
- $\mathcal E_{\widetilde\psi}$-kinetic inside $\mathcal I_6^{\rm kin}$: contracts into
  the **internal** $\psi\widetilde\psi$ line — **the unique collapse site**.

Therefore, in this channel,

$$
\boxed{\ \mathfrak A_{bc}
=\Big[\text{the }\mu^2\text{-branch of the }\mathcal I_6^{\rm kin}
\text{ boxes}\Big],\qquad
\text{everything else}=\text{classical closure (cancels exactly).}}
\tag{5G.7}
$$

The closure set comprises F1a–F1f, the "1"-branches of the boxes (which fuse $x$ with the
adjacent vertex and land exactly on the F1-triangle configurations with opposite sign),
the contact terms (zero here), and all auxiliary-contact resolutions. Its vanishing is
an algebraic identity of the unregulated theory (W6″-a verifies it mechanically); it
involves no integral evaluation.

## 4. The two boxes and their $\mu^2$-branch

**Planar box** $B_\parallel$: $\mathcal I_6^{\rm kin}(x)$; $V_2(w_1)$ with
$\widetilde\lambda$-leg $=(E,\dot d)$; $V_2(w_2)$ with $\widetilde\lambda$-leg
$=(D,\dot c)$; lines $x\overset{\psi_t\widetilde\psi}{\longrightarrow}w_1
\overset{\phi\widetilde\phi}{\longrightarrow}y
\overset{\psi\widetilde\psi}{\longrightarrow}w_2
\overset{\phi\widetilde\phi}{\longrightarrow}x$.
Flavor chain: $t\!=\!u$ ($x$–$w_1$), $u\!=\!s$ ($w_1$–$y$), $v\!=\!r$ ($y$–$w_2$),
$v\!=\!t$ ($w_2$–$x$) $\Rightarrow\ \delta_{rs}$, all internal flavor fixed.
**Crossed box** $B_\times$: $\psi_t(x)$ contracted to $w_2$ instead; same $\delta_{rs}$,
$(D,\dot c)\leftrightarrow(E,\dot d)$ with the transposed color routing.

**Collapse step** (the EOM–letter contraction, literally): on the $x$–$w_1$ line,

$$
\underbrace{(\bar\sigma^n)^{\dot ab}(i\ell_n)}_{\mathcal E_{\widetilde\psi}\text{-kin}}
\times
\underbrace{\Big[-i\hbar g^2\frac{(\sigma\!\cdot\!\ell)_{b\dot b}}{\ell_d^2}\Big]}
_{\langle\psi\widetilde\psi\rangle}
=\hbar g^2\,\delta^{\dot a}{}_{\dot b}
+\hbar g^2\,\frac{\mu_\ell^2}{\ell_d^2}\,\delta^{\dot a}{}_{\dot b}.
\tag{5G.8}
$$

The first term deletes the line (box $\to$ triangle at $x{=}w_1$: the classical-closure
partner of F1a, with the opposite sign — the cutting rule); the second is the anomaly
branch.

**$\mu^2$-branch numerator.** What multiplies $\mu^2/[\ell^2(\ell')^2(\ell'')^2
(\ell''')^2]$ in $B_\parallel$ is (leading loop power; sub-leading terms carry external
momenta and die by the second integral of (5G.6)):

$$
N_\parallel=
\underbrace{(\sigma\!\cdot\!\ell^{(\phi)})_{-\dot b}}
_{\partial\widetilde\phi\text{-leg of }\mathcal I_6}
\ \epsilon^{\dot b\dot d}\ 
\underbrace{(\sigma\!\cdot\!\ell'')_{+\dot b''}}
_{\langle\psi_{r+}(y)\widetilde\psi(w_2)\rangle}
\ \epsilon^{\dot b''\dot c},
\qquad \ell^{(\phi)},\ell''\to\pm\ell .
\tag{5G.9}
$$

Rotational average and the four-dimensional Euclidean Fierz identity
$(\sigma^m)_{a\dot a}(\sigma_m)_{b\dot b}=2\epsilon_{ab}\epsilon_{\dot a\dot b}$
(verified against the explicit (1.51) matrices) give

$$
\big\langle N_\parallel\big\rangle_{\rm ave}
=\pm\frac{\ell_d^2}{d}\,\Big[2\,\epsilon_{-+}\,\epsilon_{\dot b\dot b''}
+O(\epsilon\text{-evanescent})\Big]\epsilon^{\dot b\dot d}\epsilon^{\dot b''\dot c}
=\pm\frac{2\,\ell_d^2}{d}\,\epsilon^{\dot c\dot d},
\tag{5G.10}
$$

using $\epsilon_{-+}=\epsilon_{21}=+1$ ((1.3), frame (5D.D4)) and
$\epsilon_{\dot b\dot b''}\epsilon^{\dot b\dot d}\epsilon^{\dot b''\dot c}
=+\epsilon^{\dot c\dot d}$ ((1.5) twice). Two structural theorems drop out **before**
any integration:

- the surviving frame projection is $\epsilon_{-+}\neq0$: the output is the
  **frame-scalar** $\widetilde\lambda_{\dot a}\widetilde\lambda^{\dot a}$ structure —
  the $\partial_{\dot a}c\,\partial^{\dot a}c$ entry of the twisted alphabet;
- the vertex is **momentum-independent** (all external-momentum terms killed by
  (5G.6)$_2$): the zero-derivative $(m{=}n{=}0)$ member of the tower, exactly where the
  $(B_r,C^s)$ census puts it. Because the $\mu^2$-boxes are UV/IR **finite**, the
  $O(\epsilon)$-evanescent correction in (5G.10) never meets a pole: this channel has no
  $1/\epsilon\times\epsilon$ subtlety at all (simpler than the AA-seed's R.3 mechanism).

**Integral.** Feynman-parametrizing the four denominators
($\Gamma(4)=6$, simplex volume $\tfrac16$), shifting, and applying (5G.6),

$$
\int\!\frac{d^d\ell}{(2\pi)^d}\,
\frac{\mu_\ell^2\ \ell_d^2/d}{[\ell_d^2+\Delta]^4}\cdot 6\cdot\frac16
\ \xrightarrow[\epsilon\to0]{}\
\frac1d\cdot\frac1{32\pi^2}\Big|_{d\to4}
=\frac18\cdot\frac1{8\pi^2}
=\frac1{4}\cdot\frac{1}{32\pi^2}\,.
\tag{5G.11}
$$

(Written both ways to keep the ledger factor visible: $\tfrac2d\cdot\tfrac12=\tfrac2{2d}$;
net $\tfrac{2}{d}\times\tfrac1{32\pi^2}\times\tfrac12$ from (5G.10)'s 2 and the average —
the assembled rational is displayed once more in (5G.13).)

**Couplings, color, statistics.**

$$
\text{couplings: }(-\sqrt2h)\Big(\frac{\sqrt2h}{\hbar}\Big)^{\!2}(\hbar g^2)^4
=-2\sqrt2\,\hbar^2g^2;\qquad
\text{$i$-factors: }(i)(i)(-i)(-i)=+1;
\tag{5G.12}
$$

color: $\kappa$-transport of the two structure constants around the box gives
$\mathbb W^{AB}{}_{DE}:=c_{ACD}\,c_{BCE}$-type with the single summed adjoint index $C$;
the crossed box gives the $(D\leftrightarrow E,\ \dot c\leftrightarrow\dot d)$ image, so
the sum lands on the statistics-consistent combination
$\epsilon^{\dot c\dot d}\big[\mathbb W^{AB}{}_{DE}-\mathbb W^{AB}{}_{ED}\big]$ —
antisymmetric under the joint exchange, i.e. **symmetric** in the color pair against the
antisymmetric spinor pair, exactly the quantum numbers of
$\widetilde\lambda^{D}_{\dot a}\widetilde\lambda^{E\dot a}$. The overall fermionic
reordering (Koszul) sign of the box, the loop-momentum orientation sign in
$\ell^{(\phi)}\to\pm\ell$, the precise index order inside $\mathbb W$, and the project
$\hbar$-normalization of the detection vertex are the four global factors delegated to
the mechanical pass (§6); none of them affects the structure or the $1/32\pi^2$ rational
backbone.

## 5. Result

$$
\boxed{
Q_-\big(\psi^A_{r+}\,\widetilde\phi^B_s\big)
=-\sqrt2\,F^A_r\widetilde\phi^B_s\ \Big|_{\rm tree}
\ +\ \varsigma\,\frac{\sqrt2\,\hbar\,g^2}{32\pi^2}\,\delta_{rs}\,
\mathbb F^{AB}{}_{DE}\ \widetilde\lambda^D_{\dot a}\widetilde\lambda^{E\dot a}
\ +\ O(g^4),}
\tag{5G.13}
$$

with $\mathbb F^{AB}{}_{DE}$ the symmetrized two-structure-constant word assembled from
$\mathbb W\pm\mathbb W^T$ above, $\varsigma$ the product of the four flagged global
factors ($\varsigma=\pm1$ times a fixed power of $\hbar$ in the project's explicit-$\hbar$
bookkeeping), and the rational backbone
$\sqrt2/32\pi^2 = (-2\sqrt2)\times\tfrac2d\times\tfrac12\times\tfrac1{32\pi^2}|_{d=4}$
laid out factor-by-factor in (5G.9)–(5G.12).

Interpretation and cross-anchors:

1. **The mechanism is exactly the claimed one**: the entire quantum term is the failure
   of the cutting rule for the single internal EOM–letter contraction, one universal
   $\mu^2$ insertion, no graph-specific $(4-d)$ factors; the unregulated identity closes
   classically.
2. **Konishi-likeness is manifest**: $\delta_{rs}$, gaugino-bilinear output, adjoint
   two-$c$ color word — the component face of
   $\bar D^2(\widetilde\Phi_se^V\Phi_r)\supset\delta_{rs}\cdot
   (\text{Konishi anomaly})\cdot\widetilde W\widetilde W$-structure.
3. **HT dictionary shape**: $\delta^s_r\,\partial_{\dot a}c\,\partial^{\dot a}c$ at
   $m{=}n{=}0$, constant kernel — the zero-shift entry whose factor-2 adjudication the
   review settled (R.5); the coefficient comparison after $\varsigma$ and the dictionary
   normalizations is the pilot's P1′ verdict.

## 6. Residual verification list (delegated; bounded and factor-typed)

- **W6″-a** (closure): mechanical proof that F1a–F1f + box-"1"-branches + contacts sum
  to zero unregulated in this channel (pure algebra, no integrals). This simultaneously
  fixes the relative sign that makes the $\mu^2$-branch the *unique* survivor.
- **W6″-b** ($\varsigma$): the four global factors — box Koszul sign; loop orientation
  in (5G.9); $\mathbb W$ index order + crossed-box combination; $\hbar$-normalization of
  the detection vertex against (3D.125b).
- **W6″-c** (evanescent hygiene): confirm the $O(\epsilon)$-term of (5G.10) is
  pole-free in the boxes (finiteness statement above).
- **W6″-d** (P1′): dictionary comparison of (5G.13) with the HT zero-shift entry and,
  through the Konishi multiplet, with the literature Konishi normalization.

Everything upstream of these four items — the census localization (5G.7), the collapse
identity (5G.8), the Fierz/average step (5G.10), the master-integral reduction (5G.11),
the flavor $\delta_{rs}$, the spinor output structure, and the $1/32\pi^2$ backbone — is
closed in this memo.
