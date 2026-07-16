# Step-5B memo — N=4 SYM BRST + BV quantization and complete Feynman rules, Lorentzian ∥ Euclidean

Status: `NON_AUTHORITY_PROPOSAL` (supersedes and completes the Step-5B seed memo
`proposals/step5b-euclidean-feynman-rules-memo-2026-07-16.md`; nothing here settles a
project formula until a reviewed merge with green `verify`). Numbered equations are
(5B.$n$). Every project-locked input is cited by its contract tag. Equation-anchored
exact checks live in `tests/test_step5b_feynman_rules.py`; each test names the (5B.$n$)
it verifies (§12).

Owner instructions implemented (2026-07-16): *review and complete the BRST + BV
quantization of N=4 SYM and the full Feynman rules on the existing notation system, built
in parallel for the Lorentzian and Euclidean signatures* ("把Feynman rules等的建立平行
Lorentz以及Euclidean").

---

## 0. Review of the seed memo, and what this memo adds

Verdicts on the seed memo (`F.n` equations), each checked against the locked contracts:

| seed item | verdict |
|---|---|
| (F.1) projector algebra | exact restatement of (5A.64)–(5A.66); confirmed |
| (F.2)–(F.3) vector kernel | exact restatement of (5A.67)–(5A.68); confirmed, and now *derived* from (5A.34) in §6 |
| (F.4) vector propagator | exact restatement of (5A.69), (5A.74); confirmed |
| (F.5) chiral kernel/propagator | exact restatement of (5A.72)–(5A.74); confirmed |
| (F.6) loop saturation | **correct but previously underived**: no merged contract defines $\delta^4(\vartheta)$ or $\delta^8(z-z')$ at all (checked: 2A, 3A, 3B, 3C, 3D, 4, 4A–4C, 5A). Defined and derived here, (5B.17)–(5B.19) |
| seed §2 decision (D1) | adopted; extended to both signatures, (5B.D1) |
| seed §5 decision (D2) + NK lemma | adopted; lemma completed for both signatures, §5.3 |
| seed §4 ghost sector | "chiral-pair analogue" was asserted without derivation; ghost propagators now derived, §6.5 |
| seed §7 regulator ledger | cites the unmerged settlement contract; out of scope here — only the 4-dimensional Fourier ledger is fixed below, (5B.D3); the DRED ledger remains with the settlement obligation |

Gaps closed by this memo: (i) the entire **Lorentzian** propagator layer (absent from 5A,
whose §5A.10 is Euclidean-only and conditional); (ii) ghost propagators, both signatures;
(iii) the Grassmann delta ledger and the loop-saturation identity; (iv) an explicit
derivation of the quadratic forms from the locked action (5A.34) rather than a quotation;
(v) the momentum-space rule table in both signatures; (vi) the decision ledger, including
the new required Lorentzian-cycle decision (5B.D3), which is the resolution path for the
standing blocker `BLOCKED_STEP3D_LC_VECTOR_CYCLE` of (5A.80).

## 1. Conventions and locked inputs

### 1.1 Imported without change

Spinors and sigma matrices: $\epsilon^{12}=\epsilon^{\dot1\dot2}=+1$,
$\epsilon_{12}=\epsilon_{\dot1\dot2}=-1$, raising $\psi^a=\epsilon^{ab}\psi_b$ (1.3)–(1.5);
contractions $\xi\chi:=\xi^a\chi_a$, $\bar\xi\bar\chi:=\bar\xi_{\dot a}\bar\chi^{\dot a}$
(1.6)–(1.8); $\eta_{\mu\nu}=\mathrm{diag}(-1,+1,+1,+1)$, $\delta_{mn}$ (1.2), (4.1);
$(\sigma_L^\mu)_{a\dot b}=(\mathbf 1,\sigma^i)$, $(\bar\sigma_L^\mu)^{\dot ab}=(\mathbf
1,-\sigma^i)$ (1.10)–(1.11); $(\sigma_E^m)_{a\dot b}=(-i\sigma^i,\mathbf 1)$,
$(\bar\sigma_E^m)^{\dot ab}=(+i\sigma^i,\mathbf 1)$ (1.51)–(1.52); generators
(1.14)–(1.16), (1.55)–(1.57).

Superspace: coordinates (2A.1); derivatives $\partial_a$, $\bar\partial^{\dot a}$,
$\bar\partial_{\dot a}=\epsilon_{\dot a\dot b}\bar\partial^{\dot b}$ and the
anticommutators including $\{\bar\partial_{\dot a},\bar\vartheta^{\dot b}\}
=-\delta_{\dot a}{}^{\dot b}$ (2A.4), (2A.6); supercovariant derivatives (2A.28) [L],
(2A.41) [E]; algebra (2A.29)–(2A.30), (2A.42)–(2A.43).

Grassmann squares, measures, projections: $\vartheta^2=\vartheta^a\vartheta_a
=-2\vartheta^1\vartheta^2$, $\bar\vartheta^2=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a}
=2\bar\vartheta_{\dot1}\bar\vartheta_{\dot2}$ (3A.9); $D_R^2:=D_R^aD_{Ra}$,
$\bar D_R^2:=\bar D_{R\dot a}\bar D_R^{\dot a}$ (3A.10); $D_R^2\vartheta^2=-4$,
$\bar D_R^2\bar\vartheta^2=-4$ (3A.12); $[X]_F=-\tfrac14D_R^2X|$,
$[\widetilde X]_{\widetilde F}=-\tfrac14\bar D_R^2\widetilde X|$,
$[Y]_D=\tfrac1{16}D_R^2\bar D_R^2Y|$ ($\bar D^2$ first) (3A.13)–(3A.14);
$\int d^4x_R\,d^4\vartheta\,Y:=\int d^4x_R[Y]_D$ (3A.16); exterior order
$\vartheta^1<\vartheta^2<\bar\vartheta_{\dot1}<\bar\vartheta_{\dot2}$ (3A.104).

Adjoint algebra and couplings: (4.5)–(4.11); $h=g^{-2}$, $c_{ABC}=c_{[ABC]}$ (4C.1);
$f_{AB}=h\kappa_{AB}+i\mathfrak k_{AB}$, $\widetilde f_{AB}=h\kappa_{AB}-i\mathfrak
k_{AB}$, $\mathfrak h_{AB}=\tfrac12(f+\widetilde f)_{AB}=h\kappa_{AB}$ (5A.2), (4A.3).

Path integral: $\tau_L=i/\hbar$, $\tau_E=-1/\hbar$, $\upsilon_L=+1$, $\upsilon_E=-1$
(3D.6); weights (3D.24)–(3D.27); action signs $\eta_L=+1$, $\eta_E=-1$ (5A.2);
Euclidean tilded/untilded independence (3A.91), (4C.53), (3D.26).

### 1.2 Superspace integral notation (review finding, now fixed)

**Review finding R-5B.1.** The symbols $\int_{R,8}$, $\int_{R,\pm}$ are used throughout
3D and 5A but never defined in a merged contract. This memo fixes them (they are the
unique definitions compatible with (3D.5) lines 63–75 of 3D and with every 5A usage):

$$
\int_{R,8}Y:=\int d^4x_R\,[Y]_D,\qquad
\int_{R,+}X:=\int d^4x_R\,[X]_F,\qquad
\int_{R,-}\widetilde X:=\int d^4x_R\,[\widetilde X]_{\widetilde F}.
\tag{5B.1}
$$

**Lemma (D-exactness integrates to zero).** For any superfield $Z$ decaying at spatial
infinity,

$$
\int_{R,8}D_{Ra}Z=\int_{R,8}\bar D_{R\dot a}Z=0,
\tag{5B.2}
$$

because $D$, $\bar D$ are $\partial_\vartheta$ plus an $x$-derivative term
((2A.28)/(2A.41)): the Berezin part is killed by one missing $\vartheta$ in $[\,\cdot\,]_D$
after the four derivatives are saturated, and the $x$-part is a total derivative.
Consequently the full-superspace integration by parts

$$
\int_{R,8}(D^aU)W=-(-1)^{\epsilon_U}\int_{R,8}U\,D^aW
\tag{5B.3}
$$

holds with the Koszul sign of (5A.61).

**Conversion lemma.** For any $W,Z$,

$$
\big[(\bar D_R^2W)\,Z\big]_D=\Big[(\bar D_R^2W)\Big(-\tfrac14\bar D_R^2Z\Big)\Big]_F,
\qquad\text{i.e.}\qquad
\int_{R,+}\!\big(-\tfrac14\bar D_R^2Y\big)=\int_{R,8}Y ,
\tag{5B.3a}
$$

and its mirror with $D^2$, $[\,\cdot\,]_{\widetilde F}$, $\int_{R,-}$. [Checked: T12.]

### 1.3 Clifford and generator identities used below

$$
\sigma_L^\mu\bar\sigma_L^\nu+\sigma_L^\nu\bar\sigma_L^\mu=-2\eta^{\mu\nu}\mathbf 1,
\qquad
\sigma_E^m\bar\sigma_E^n+\sigma_E^n\bar\sigma_E^m=+2\delta^{mn}\mathbf 1,
\tag{5B.4}
$$

$$
\sigma_L^{0i}=-\tfrac12\sigma^i,\quad
\sigma_L^{ij}=\bar\sigma_L^{ij}=-\tfrac i2\epsilon^{ijk}\sigma^k,\quad
\sigma_E^{ij}=+\tfrac i2\epsilon^{ijk}\sigma^k,\quad
\sigma_E^{4i}=\tfrac i2\sigma^i=-(\bar\sigma_E^{4i}).
\tag{5B.5}
$$

[(1.12)–(1.16), (1.54)–(1.57); checked: T1, T2.]

### 1.4 Fourier ledger — decision (5B.D3), both signatures

No merged contract fixes a Fourier convention (checked: 2A, 3A, 3D report none). We fix,
as the third convention decision of the Step-5 program (the first two are D1, D2 of §5):

> **(5B.D3)** Plane waves are $e^{ip\cdot x_R}$ with $p\cdot x_L:=\eta^{\mu\nu}p_\mu
> x_\nu$, $p\cdot x_E:=\delta^{mn}p_mx_n$; **all momenta incoming** at every vertex and
> insertion. Consequently $\partial_M\mapsto ip_M$ on an incoming line,
>
> $$
> \Box_L:=\eta^{\mu\nu}\partial_\mu\partial_\nu\mapsto-p_L^2,\qquad
> \Box_E:=\delta^{mn}\partial_m\partial_n\mapsto-p_E^2,\qquad
> p_L^2:=\eta^{\mu\nu}p_\mu p_\nu,\quad p_E^2:=\delta^{mn}p_mp_n .
> \tag{5B.6}
> $$
>
> **Lorentzian cycle**: the $\epsilon$-damped weight (3D.24) with a positive quadratic
> $\mathscr Q_{L,\nu}$ selects the Feynman representative
> $\Box_L^{-1}\mapsto-1/(p_L^2-i\varepsilon)$, $\varepsilon\downarrow0$.
> This is a **proposed** resolution of `BLOCKED_STEP3D_LC_VECTOR_CYCLE` (5A.80) and
> requires owner authorization; every Lorentzian momentum-space rule below carries it.
> The Euclidean rules are cycle-free at this order and match the conditional (5A.74).

## 2. Field content, action, gauge structure

Fields: $\mathcal V_R=\mathcal V_R^AT_A$ unrestricted (5A.31); three adjoint chiral pairs
$(\Phi^A_r,\widetilde\Phi^A_r)$, $r=1,2,3$, with $\bar D_{R\dot a}\Phi_r=0$,
$D_{Ra}\widetilde\Phi_r=0$ ((3C.53) via (3C.52)); Lorentzian contour
$\widetilde\Phi_L=\bar\Phi_L$ (3B.17a), Euclidean pairs independent (4C.53).

The locked action, both signatures at once (5A.34) with $N=4$, $m_4=3$,
$\delta_{N4}=1$:

$$
\boxed{
\begin{aligned}
S_R^{(4)}=\eta_R\Bigg\{&
h\kappa_{AB}\sum_{r=1}^{3}
\int_{R,8}\widetilde\Phi_r^A(e^{\mathcal V_{R,\mathrm{ad}}})^B{}_C\Phi_r^C
+\frac14f_{AB}\int_{R,+}\mathcal W_R^{Aa}\mathcal W_{Ra}^B
+\frac14\widetilde f_{AB}\int_{R,-}
\widetilde{\mathcal W}_{R\dot a}^A\widetilde{\mathcal W}_R^{B\dot a}\\
&-\frac{\sqrt2h}{6}\varepsilon_{rst}c_{ABC}
\left(\int_{R,+}\Phi_r^A\Phi_s^B\Phi_t^C
+\int_{R,-}\widetilde\Phi_r^A\widetilde\Phi_s^B\widetilde\Phi_t^C\right)\Bigg\},
\end{aligned}}
\tag{5B.7$'$}
$$

with $\mathcal W_{Ra}=-\frac18\bar D_R^2(e^{-\mathcal V_R}D_{Ra}e^{\mathcal V_R})$,
$\widetilde{\mathcal W}_{R\dot a}=+\frac18D_R^2(e^{\mathcal V_R}\bar D_{R\dot
a}e^{-\mathcal V_R})$ (5A.33), superpotential coefficient $u=-\sqrt2$ locked by
(4C.12)–(4C.13). On the Lorentzian contour $\widetilde f_{AB}=\bar f_{AB}$ (4A.4);
$S_L^{(4)}$, $S_E^{(4)}$ are (4C.3), (4C.4). Gauge transformations (3A.31)–(3A.32):
$\mathcal E_R'=\bar h\,\mathcal E_Rh^{-1}$, $\Phi'=h\Phi$,
$\widetilde\Phi'=\widetilde\Phi\bar h^{-1}$, $h=e^{i\Lambda}$,
$\bar h=e^{i\bar\Lambda}$, $\bar D\Lambda=0=D\bar\Lambda$.

The flat derivative algebra needed everywhere below ((2A.29), (2A.42); checked T3):

$$
\{D_a^L,\bar D_{\dot b}^L\}=+2i(\sigma_L^\mu)_{a\dot b}\partial_\mu^L,\qquad
\{D_a^E,\bar D_{\dot b}^E\}=-2(\sigma_E^m)_{a\dot b}\partial_m^E,\qquad
\{D,D\}=\{\bar D,\bar D\}=0 .
\tag{5B.7}
$$

## 3. BRST layer (identical form in both signatures)

Ghosts $\mathfrak c_R$ (chiral), $\widetilde{\mathfrak c}_R$ (antichiral), odd, ghost
number $+1$ (5A.35)/(3D.43). The locked classical BRST operator (5A.36)–(5A.39):

$$
\mathbf s_R\mathcal E_R=i\widetilde{\mathfrak c}_R\mathcal E_R
-i\mathcal E_R\mathfrak c_R,\qquad
\mathbf s_R\mathfrak c_R=i\mathfrak c_R^2,\qquad
\mathbf s_R\widetilde{\mathfrak c}_R=i\widetilde{\mathfrak c}_R^2,\qquad
\mathbf s_R\Phi_R=i\mathfrak c_R\Phi_R,\qquad
\mathbf s_R\widetilde\Phi_R=-i\widetilde\Phi_R\widetilde{\mathfrak c}_R,
\tag{5B.8$'$}
$$

nilpotent and action-invariant, $\mathbf s_R^2=0$, $\mathbf s_RS_R^{(4)}=0$ (5A.37)–(5A.39),
with the closed-form word on $\mathcal V$ ((5A.56)–(5A.57), Bernoulli numbers $B_n$):

$$
\mathbf s_R\mathcal V_R
=i\sum_{p,q\ge0}\frac{B_{p+q}}{p!q!}
\left[(-1)^q\mathcal V_R^p\widetilde{\mathfrak c}_R\mathcal V_R^q
-(-1)^p\mathcal V_R^p\mathfrak c_R\mathcal V_R^q\right]
=i(\widetilde{\mathfrak c}_R-\mathfrak c_R)
-\frac i2[\mathcal V_R,\widetilde{\mathfrak c}_R+\mathfrak c_R]+O(\mathcal V^2).
\tag{5B.8$''$}
$$

Note the entire BRST layer carries **no explicit signature dependence**: L and E differ
only through the reality/cycle statements ($\widetilde{\mathfrak c}_L=\mathfrak
c_L^{\ddagger_L}$ vs. independent Euclidean pairs, (3D.49)).

## 4. BV layer

Antifield ledger (3D.51)–(3D.53): $(\mathcal V^\star;\Phi^\star_r,\widetilde\Phi^\star_r;
\mathfrak c^\star,\widetilde{\mathfrak c}^\star)$ on the domains $(8;+,-;+,-)$ with
$\epsilon_{X^\star}=\epsilon_X+1$, $\mathrm{gh}(X^\star)=-1-\mathrm{gh}(X)$,
$[X^\star]=d_{\Sigma_X}-[X]$ (3D.52). Antibracket and pinning (3D.54)–(3D.55); minimal
master action (3D.56)/(5A.41):

$$
S_{\min,R}=S_R^{(4)}
+\langle\mathcal V^\star,\mathbf s_R\mathcal V\rangle_{R,8}
+\sum_r\Big[\langle\Phi_r^\star,\mathbf s_R\Phi_r\rangle_{R,+}
+\langle\widetilde\Phi_r^\star,\mathbf s_R\widetilde\Phi_r\rangle_{R,-}\Big]
-\langle\mathfrak c^\star,\mathbf s_R\mathfrak c\rangle_{R,+}
-\langle\widetilde{\mathfrak c}^\star,\mathbf s_R\widetilde{\mathfrak c}\rangle_{R,-},
\tag{5B.9$'$}
$$

satisfying the CME $\tfrac12(S_{\min,R},S_{\min,R})_R=0$ (3D.57)/(5A.41) and generating
$\mathbf s_RF=(S_{\min,R},F)_R$ (3D.58). The **only** signature dependence of the quantum
BV layer is the QME phase ((3D.64), (3D.68a)–(3D.69), (5A.42d)–(5A.42f)):

$$
\mathfrak O^{\rm BV}_{L,\nu}[W]=\tfrac12(W,W)_{L,\nu}-i\hbar\Delta_{L,\nu}W,\qquad
\mathfrak O^{\rm BV}_{E,\nu}[W]=\tfrac12(W,W)_{E,\nu}-\hbar\Delta_{E,\nu}W,
\qquad
\mathfrak e_L^{\rm QME}=i,\ \ \mathfrak e_E^{\rm QME}=1,
\tag{5B.9$''$}
$$

with the order-by-order recursion (5A.42f) and the regulated-defect caveats
(3D.59)–(3D.60), (5A.42b)–(5A.42c) carried unchanged in both signatures.

## 5. Gauge fixing, decisions D1/D2, Nielsen–Kallosh lemma

Non-minimal doublets (3D.87)/(5A.43): $(\mathfrak c'_{R,+},\mathfrak n_{R,+})$ and
$(\widetilde{\mathfrak c}'_{R,-},\widetilde{\mathfrak n}_{R,-})$,
$\mathbf s_R\mathfrak c'=\mathfrak n$, $\mathbf s_R\mathfrak n=0$. Gauge conditions
(3D.86)/(5A.44) at trivial background:
$\mathcal F_{R,+}=-\tfrac14\bar D_R^2\mathcal V_R$,
$\mathcal F_{R,-}=-\tfrac14D_R^2\mathcal V_R$. Gauge fermion and its variation
(3D.89)–(3D.90)/(5A.46)–(5A.47); gauge-fixed action $S_{\Psi,R}=S_R^{(4)}+\mathbf
s_R\Psi_R$ at zero antifield sources (3D.77) — note $\mathbf s_R\Psi_R$ enters **without**
an extra $\eta_R$ or $\tau_R$ weight; the whole combination is weighted by
$\tau_R$ in the exponent (3D.124c).

### 5.1 Decision (5B.D1): Fermi–Feynman slice, both signatures

Step-3D requires $\mathcal Y_R$ local (3D.88a); the Fermi–Feynman kernel is provably
nonlocal (5A.79). As in the seed memo, the resolution is a scheme definition, now stated
for both signatures:

> **(5B.D1)** For the perturbative expansion in either signature, the gauge-fixed
> Gaussian weight is defined by the quadratic forms (5B.13)–(5B.14) below, equivalently by
> averaging the gauge conditions with the (nonlocal) kernels
>
> $$
> \mathcal Y_{R,\rm FF}^{-1}:=-\eta_R\frac h2\,\mathcal A_R,
> \qquad
> \mathcal A_R:=\begin{pmatrix}0&-\bar D_R^2/4\\-D_R^2/4&0\end{pmatrix},
> \qquad
> \mathcal A_R^2=\Box_R\mathbf 1 ,
> \tag{5B.10$'$}
> $$
>
> ($R=E$ reproduces (5A.75) exactly; $R=L$ is the new entry). Step-3D locality is
> retained only for the nonperturbative BV-density statements. Since $\mathcal
> Y_{R,\rm FF}$ is built from flat $D,\bar D$, one has $\mathbf s_R\mathcal
> Y_{R,\rm FF}=0$, so the standard factorized line of (3D.95b) applies.

### 5.2 Projector algebra, both signatures

Define, on the residual-free domain where $\Box_R^{-1}$ exists,

$$
\mathcal P_+:=\frac{\bar D_R^2D_R^2}{16\Box_R},\qquad
\mathcal P_-:=\frac{D_R^2\bar D_R^2}{16\Box_R},\qquad
\mathcal P_T:=-\frac{D_R^a\bar D_R^2D_{Ra}}{8\Box_R},\qquad
\mathcal P_0:=\mathcal P_++\mathcal P_- .
\tag{5B.10}
$$

**Lemma (D-algebra workhorse identities).** From (5B.7) alone, in both signatures with
the respective $\Box_R$,

$$
\bar D_R^2D_R^2\bar D_R^2=16\,\Box_R\,\bar D_R^2,\qquad
D_R^2\bar D_R^2D_R^2=16\,\Box_R\,D_R^2,\qquad
-D_R^a\bar D_R^2D_{Ra}=8\Box_R-\tfrac12\{D_R^2,\bar D_R^2\},
\tag{5B.9}
$$

$$
D_R^a\bar D_R^2D_{Ra}=\bar D_{R\dot a}D_R^2\bar D_R^{\dot a}.
\tag{5B.9a}
$$

For $R=E$ these are (5A.65); for $R=L$ they are new statements, with the sign chain
$(2i)^2(\sigma^\mu\partial_\mu)(\bar\sigma^\nu\partial_\nu)=(-4)(-\Box_L)=+4\Box_L$
matching the Euclidean $(-2)^2(+\Box_E)$. [Checked: T5.] Hence idempotence,
orthogonality, and completeness hold verbatim in both signatures:

$$
\mathcal P_i\mathcal P_j=\delta_{ij}\mathcal P_i\ (i,j\in\{T,+,-\}),\qquad
\mathcal P_T+\mathcal P_++\mathcal P_-=1 .
\tag{5B.10a}
$$

[= (5A.66) for $E$; checked: T6.]

### 5.3 Decision (5B.D2) and the Nielsen–Kallosh lemma, both signatures

> **(5B.D2)** Select the **external measure-only branch** of (3D.95b)/(3D.96b) in both
> signatures: $\mathscr R^{\rm BV}_{\rm NK}=\varnothing$, and the NK factor is kept as the
> external normalization $\mathfrak F^{\rm NK}_{R,\nu}=\mathfrak F^{\rm NK,req}_{R,\nu}$.

**Lemma (NK irrelevance in the FF slice).** In the slice (5B.D1), $\mathcal Y_{R,\rm FF}$
is built from the flat $D_R,\bar D_R$ only; it contains no quantum field, so the
admissibility condition (3D.96a),
$\vec\partial\mathcal Y_R/\partial x^{\mathsf r}_{R,\nu}=0$ and
$\vec\partial\mathfrak F^{\rm NK,req}_{R,\nu}/\partial x^{\mathsf r}_{R,\nu}=0$, holds
identically, the external branch is admissible, and $\mathfrak F^{\rm NK}_{R,\nu}$ is a
field-independent constant. By the normalized definitions (3D.125)–(3D.125a) every
normalized correlator — in particular every letter-channel correlator at any loop order —
is independent of $\mathfrak F^{\rm NK}_{R,\nu}$. $\square$

This discharges `BLOCKED_STEP5A_NK_BRANCH_UNSELECTED` at the level of a recorded,
provable decision in both signatures; background-covariant refinements (field-dependent
$\mathcal Y$) remain the deferred item of the seed memo §8(iii).

## 6. Free kernels and propagators, L ∥ E

### 6.1 Vector kernel derived from the locked action

Expanding (5B.7$'$) to second order in $\mathcal V$: $\mathcal W^{(1)}_{Ra}
=-\tfrac18\bar D_R^2D_{Ra}\mathcal V_R$, so the $(p,q,r,s)=(0,0,0,0)$ term of the locked
convolution (5A.52) is the entire quadratic $+$-part,

$$
S^{(2)}_{R,+}=\eta_R\frac{f_{AB}}{256}\int_{R,+}
(\bar D_R^2D_R^a\mathcal V^A)(\bar D_R^2D_{Ra}\mathcal V^B).
\tag{5B.11}
$$

Both factors are chiral ($\bar D^3=0$), so with the conversion lemma (5B.3a) and the
integration by parts (5B.3),

$$
S^{(2)}_{R,+}
=-\eta_R\frac{f_{AB}}{64}\int_{R,8}(D^a\mathcal V^A)(\bar D_R^2D_{Ra}\mathcal V^B)
=+\eta_R\frac{f_{AB}}{64}\int_{R,8}\mathcal V^A\,D_R^a\bar D_R^2D_{Ra}\mathcal V^B,
\tag{5B.12}
$$

and the mirror computation gives $S^{(2)}_{R,-}=+\eta_R\frac{\widetilde
f_{AB}}{64}\int_{R,8}\mathcal V^A\bar D_{R\dot a}D_R^2\bar D_R^{\dot a}\mathcal V^B$. By
(5B.9a) the two operators are equal, so the $f-\widetilde f$ (i.e. $\mathfrak k_{AB}$)
part cancels **identically at the superspace level**:

$$
S^{(2)}_{R,V,\rm inv}
=\eta_R\frac{\mathfrak h_{AB}}{32}\int_{R,8}\mathcal V^AD^a\bar D^2D_a\mathcal V^B
=-\eta_R\frac h4\int_{R,8}\mathcal V\cdot\Box_R\,\mathcal P_T\,\mathcal V .
\tag{5B.13}
$$

($R=E$: $+\frac h4\int V\Box_E\mathcal P_TV$ = (5A.70) exactly.) The component
counterpart of the $\mathfrak k$-cancellation is the total-derivative identity
$\epsilon^{\mu\nu\rho\sigma}\partial_\mu A_\nu\partial_\rho A_\sigma
=\partial_\mu(\epsilon^{\mu\nu\rho\sigma}A_\nu\partial_\rho A_\sigma)$ [checked: T13].

The FF average (5B.D1) contributes, by the R-uniform identity (5A.77)–(5A.78),

$$
S^{(2)}_{R,V,\rm gf}
=\tfrac12\langle\mathcal Y_{R,\rm FF}^{-1}\mathcal F,\mathcal F\rangle_R
=-\eta_R\frac h4\int_{R,8}\mathcal V\cdot\Box_R\,\mathcal P_0\,\mathcal V ,
\tag{5B.13a}
$$

so projectors sum to the identity and

$$
\boxed{
S^{(2)}_{R,V}=\frac12\int_{R,8}\mathcal V^AK^V_{R,AB}\mathcal V^B,\qquad
K^V_{R,AB}=-\eta_R\frac h2\kappa_{AB}\Box_R,\qquad
(K^V_R)^{-1\,AB}=-\eta_R\,2g^2\kappa^{AB}\Box_R^{-1}.}
\tag{5B.14}
$$

($R=E$: $K^V_E=+\frac h2\kappa\Box_E$ = (5A.68) exactly; $R=L$: $K^V_L=-\frac
h2\kappa\Box_L$ is the new entry.) Component check ((5A.71) and its Lorentzian
counterpart, with $\mathcal V_L|_A=-2\vartheta\sigma_L^\mu\bar\vartheta A_\mu$ (3B.27)):

$$
\big[\mathcal V_R\,\Box_R\mathcal V_R\big]_D\big|_{A^2}=-2A^M\Box_RA_M
\quad\Longrightarrow\quad
S^{(2)}_{R,V}\big|_{A^2}=\eta_R\frac h2\int d^4x_R\,A^M\Box_RA_M ,
\tag{5B.15}
$$

i.e. $+\frac h2A^\mu\Box_LA_\mu$ ($=$ Feynman-gauge Maxwell in mostly-plus signature) and
$-\frac h2A_m\Box_EA_m$ ($=$ (5A.71)). [Checked: T11.]

### 6.2 Matter kernel

$S^{(2)}_{R,\Phi}=\eta_Rh\kappa_{AB}\sum_r\int_{R,8}\widetilde\Phi_r^A\Phi_r^B$. With the
constrained identity kernels $\mathbf 1_\pm=\mathcal P_\pm\delta^8_R(z-z')$ (5A.72),
(5B.18):

$$
\boxed{
K^{\Phi\widetilde\Phi}_{R,AB}=\eta_R\,h\kappa_{AB}\,\mathbf 1_+,\qquad
(K^{\Phi\widetilde\Phi}_R)^{-1\,AB}=\eta_R\,g^2\kappa^{AB}\,\mathbf 1_+,}
\tag{5B.16}
$$

flavor-diagonal, reversed orientation with $\mathbf 1_-$. ($R=E$: $-h\kappa\mathbf 1_+$ =
(5A.73).) Functional-derivative rule (continuum form of (3D.20)–(3D.21)):
$\vec\delta\Phi(z)/\delta\Phi(z')=\mathbf 1_+(z,z')$, never $\delta^8$ — the seed memo's
three chirality rules (§3 there) are carried over verbatim, now for both signatures.

### 6.3 Propagators and momentum space

With the edge factor $-\tau_R^{-1}$ of the locked graph weight (5A.63)
($-\tau_L^{-1}=i\hbar$, $-\tau_E^{-1}=\hbar$), $G^{XY}_R:=(-\tau_R^{-1})(K_R^{XY})^{-1}$:

$$
G^{VV}_R=-\eta_R\,(-\tau_R^{-1})\,2g^2\kappa^{-1}\Box_R^{-1},\qquad
G^{\Phi\widetilde\Phi}_R=\eta_R\,(-\tau_R^{-1})\,g^2\kappa^{-1}\mathcal
P_+\delta^8_R(z-z').
\tag{5B.16a}
$$

In momentum space (5B.D3), with $\delta^8\to\delta^4(\vartheta_{12})$ on internal lines
and $\mathcal P_\pm\delta^8\mapsto-\frac1{16p^2}\bar D^2D^2\delta^4(\vartheta_{12})$
resp. $-\frac1{16p^2}D^2\bar D^2\delta^4(\vartheta_{12})$:

$$
\boxed{
\begin{array}{l|l}
R=L\ (\text{with }p^2\to p_L^2-i\varepsilon) & R=E\\ \hline
\langle\mathcal V^A\mathcal V^B\rangle_L
=+(2\pi)^4\delta^4(p+p')\dfrac{2i\hbar g^2\kappa^{AB}}{p_L^2}\,
\delta^4(\vartheta_{12})
&
\langle\mathcal V^A\mathcal V^B\rangle_E
=-(2\pi)^4\delta^4(p+p')\dfrac{2\hbar g^2\kappa^{AB}}{p_E^2}\,
\delta^4(\vartheta_{12})\\[2mm]
\langle\Phi_r^A\widetilde\Phi_s^B\rangle_L
=-(2\pi)^4\delta^4(p+p')\,\delta_{rs}\dfrac{i\hbar g^2\kappa^{AB}}{16\,p_L^2}\,
\bar D_1^2D_1^2\delta^4(\vartheta_{12})
&
\langle\Phi_r^A\widetilde\Phi_s^B\rangle_E
=+(2\pi)^4\delta^4(p+p')\,\delta_{rs}\dfrac{\hbar g^2\kappa^{AB}}{16\,p_E^2}\,
\bar D_1^2D_1^2\delta^4(\vartheta_{12})
\end{array}}
\tag{5B.17}
$$

The Euclidean column is (5A.74) verbatim. [Kernel–propagator inversion checked: T7, T8.]

### 6.4 Grassmann delta ledger (new; closes review finding of §0)

$$
\delta^4(\vartheta_{12}):=(\vartheta_1-\vartheta_2)^2\,(\bar\vartheta_1-\bar\vartheta_2)^2,
\qquad
\delta^8_R(z-z'):=\delta^4(x-x')\,\delta^4(\vartheta-\vartheta'),
\tag{5B.18}
$$

with $\vartheta^2$, $\bar\vartheta^2$ as in (3A.9). Reproducing property:
$\int d^4\vartheta_2\,\delta^4(\vartheta_{12})X(\vartheta_2)=X(\vartheta_1)$ for the
Berezin measure normalized by $[\vartheta^2\bar\vartheta^2]_D=1$ (3A.15). [Checked: T9.]

**Loop saturation lemma** (both signatures; the momentum-dependent pieces of $D^2$,
$\bar D^2$ cancel between the two deltas):

$$
\delta^4(\vartheta_{12})\,D_1^2\bar D_1^2\,\delta^4(\vartheta_{12})
=\delta^4(\vartheta_{12})\,\bar D_1^2D_1^2\,\delta^4(\vartheta_{12})
=16\,\delta^4(\vartheta_{12}),
\tag{5B.19}
$$

$$
\delta^4(\vartheta_{12})\,\mathcal O\,\delta^4(\vartheta_{12})=0
\quad\text{for }\mathcal O\in\{1,\;D_a,\;\bar D_{\dot a},\;D^2,\;\bar D^2,\;
D_a\bar D_{\dot b},\;D^a\bar D^2,\;\dots\}\ (\text{fewer than }2+2\text{ spinor
derivatives}).
\tag{5B.19a}
$$

[Checked: T10.] This derives the seed memo's (F.6) from first principles; more than the
maximal set reduces by (5B.9).

### 6.5 Ghost sector: quadratic forms and propagators (new)

From the locked free FP term (5A.60) and the conversion lemma (5B.3a),

$$
S^{(2)}_{R,\rm FP}
=\frac i4\int_{R,+}\mathfrak c'\bar D_R^2\widetilde{\mathfrak c}
-\frac i4\int_{R,-}\widetilde{\mathfrak c}'D_R^2\mathfrak c
=-i\int_{R,8}\mathfrak c'\cdot\widetilde{\mathfrak c}
+i\int_{R,8}\widetilde{\mathfrak c}'\cdot\mathfrak c ,
\tag{5B.20}
$$

**with no $\eta_R$ and no $h$**: the ghost kinetic operator is signature-blind and
coupling-free (couplings enter only through ghost–vector vertices, §7). The multiplier
pair decouples after the Gaussian completion (5A.48): the shifted
$\mathfrak n-\mathcal Y^{-1}\mathcal F$ integral is field-independent in the slice
(5B.D1) and is absorbed by (5B.D2); no $\mathfrak n$-line ever appears in a letter-channel
graph.

Inverting (5B.20) on the constrained pairs (fermionic kernels $\mp i\,\mathbf 1_\mp$-type,
inverse $\pm i$, edge factor $-\tau_R^{-1}$, ordered differentiation (5A.61)–(5A.62)):

$$
\boxed{
\begin{aligned}
\langle\widetilde{\mathfrak c}^A(1)\,\mathfrak c'^B(2)\rangle_R
&=(-\tau_R^{-1})\,i\,\kappa^{AB}\mathcal P_-\delta^8_R(z_1-z_2)
&&\xrightarrow{\ p\ }\
-(2\pi)^4\delta^4(p+p')\,(-\tau_R^{-1})\,\frac{i\,\kappa^{AB}}{16p^2}\,
D_1^2\bar D_1^2\delta^4(\vartheta_{12}),\\
\langle\mathfrak c^A(1)\,\widetilde{\mathfrak c}'^B(2)\rangle_R
&=(-\tau_R^{-1})\,(-i)\,\kappa^{AB}\mathcal P_+\delta^8_R(z_1-z_2)
&&\xrightarrow{\ p\ }\
+(2\pi)^4\delta^4(p+p')\,(-\tau_R^{-1})\,\frac{i\,\kappa^{AB}}{16p^2}\,
\bar D_1^2D_1^2\delta^4(\vartheta_{12}),
\end{aligned}}
\tag{5B.21}
$$

with $-\tau_L^{-1}=i\hbar$ (and $p^2\to p_L^2-i\varepsilon$), $-\tau_E^{-1}=\hbar$. The
overall fermionic orientation sign is fixed by the ordered rule (5A.61)–(5A.62): reversing
an orientation flips the sign (ghost loops carry the $(-1)$ of $\kappa_G$ in (5A.63)).
[Kernel inversion structure checked: T8/T12.]

## 7. Interaction vertices, L ∥ E (complete inventory)

All vertices are ordered functional derivatives (5A.61)–(5A.62) of the locked words; the
graph weight is (5A.63). The complete list, with the explicit low orders used at one
loop:

**(V1) Gauge self-interaction** — the all-order convolution (5A.52). Cubic and quartic
terms: the $(p,q,r,s)$ with $p+q+r+s=1$ resp. $2$, e.g. the cubic word

$$
S^{(3)}_{R,+}=\eta_R\frac{f_{AB}}{256}\sum_{(p,q,r,s):\,p+q+r+s=1}
\frac{(-1)^{p+r}}{(p+q+1)(r+s+1)}
\int_{R,+}[\bar D^2(V^pD^aV\,V^q)]^A[\bar D^2(V^rD_aV\,V^s)]^B ,
\tag{5B.22}
$$

plus the $-$ mirror with $\widetilde f_{AB}$, $(-1)^{q+s}$.

**(V2) Matter–gauge tower** (5A.53)–(5A.54): with $(T_A)^B{}_C=ic_{AC}{}^B$ (4.8),

$$
S^{\rm mat}_R
=\eta_Rh\kappa_{AB}\sum_{r,n}\frac1{n!}\int_{R,8}
\widetilde\Phi_r^AV^{A_1}\!\cdots V^{A_n}(T_{A_1}\!\cdots T_{A_n})^B{}_C\Phi_r^C;
\qquad
n=1:\ \ i\eta_Rh\,c_{BCA}\int_{R,8}\widetilde\Phi_r^A\mathcal V^B\Phi_r^C,
\tag{5B.23}
$$

$n=2$ with the symmetrized ordered color chain of (5A.54); only $n\le2$ enters at one
loop.

**(V3) Superpotential** (4C.13)/(5A.55): the labeled cubic primitives

$$
\mathcal V_{R,\Phi\Phi\Phi}=\mathcal V_{R,\widetilde\Phi\widetilde\Phi\widetilde\Phi}
=-\eta_R\sqrt2\,h\,\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3},
\tag{5B.24}
$$

on $\int_{R,+}$ resp. $\int_{R,-}$ (half-superspace vertices; see transfer rules §8).

**(V4) Ghost–vector words** (5A.57)–(5A.59): coefficients
$g^{\widetilde c}_{pq}=\frac i4\frac{B_{p+q}(-1)^q}{p!q!}$,
$g^c_{pq}=-\frac i4\frac{B_{p+q}(-1)^p}{p!q!}$; the cubic terms ($B_1=-\tfrac12$)
assemble into commutators,

$$
S^{(3)}_{R,\rm FP}
=\frac i8\int_{R,+}\mathfrak c'\,\bar D_R^2\big([\widetilde{\mathfrak c},\mathcal V]
+[\mathfrak c,\mathcal V]\big)
+\frac i8\int_{R,-}\widetilde{\mathfrak c}'\,D_R^2\big([\widetilde{\mathfrak c},\mathcal
V]+[\mathfrak c,\mathcal V]\big),
\tag{5B.25}
$$

signature-blind as in (5B.20); quartic and higher words from $B_2=\tfrac16$, $B_3=0$, ….

**(V5) Antifield (BRST-source) vertices** from (5B.9$'$): $\langle\mathcal V^\star,\mathbf
s_R\mathcal V\rangle$ expanded by (5B.8$''$), $\langle\Phi^\star,i\mathfrak c\Phi\rangle$,
$\langle\widetilde\Phi^\star,-i\widetilde\Phi\widetilde{\mathfrak c}\rangle$,
$-\langle\mathfrak c^\star,i\mathfrak c^2\rangle$,
$-\langle\widetilde{\mathfrak c}^\star,i\widetilde{\mathfrak c}^2\rangle$ — needed for
BV/Zinn–Justin correlators and for EOM insertions.

**Graph weight** (5A.63), both signatures:

$$
\mathfrak W_R(G)=\tau_R^{|V(G)|}(-\tau_R^{-1})^{|E(G)|}
\Big(\prod_v\mathcal C_v\Big)\Big(\prod_eK_e^{-1}\Big)(-1)^{\kappa_G},
\qquad
-\tau_L^{-1}=i\hbar,\quad-\tau_E^{-1}=\hbar,
\tag{5B.26}
$$

divided once by the automorphism group for unlabeled graphs.

## 8. Supergraph transfer rules (chirality bookkeeping), both signatures

1. **Half-superspace vertices.** A $+$-type vertex $\int_{R,+}\mathscr U$ entering a
   full-superspace Wick expansion converts by exactly one factor $-\tfrac14\bar D_R^2$
   via (5B.3a) (mirror: $-\tfrac14D_R^2$). Equivalently: each internal line leaving a
   purely chiral vertex carries one $-\tfrac14\bar D^2$ except one line per vertex whose
   factor is absorbed by the conversion. The $\frac1{16}\bar D^2D^2$ visible in (5B.17)
   is exactly two such factors acting on $\delta^4(\vartheta)/p^2$.
2. **Derivative transfer.** On $\delta^4(\vartheta_{12})e^{ip\cdot x_{12}}$ with all
   momenta incoming, $D^{(1)}_a=-D^{(2)}_a$ and $\bar D^{(1)}_{\dot a}=-\bar
   D^{(2)}_{\dot a}$ (the momentum in $D^{(2)}$ is $-p$), so derivatives may be moved
   across a line at the cost of a sign; superspace integration by parts (5B.3) is an
   oriented operation and every derivative moved onto an external leg **remains** in the
   final external-leg operator.
3. **Loop closure.** A closed $\vartheta$-loop is evaluated with (5B.19)/(5B.19a): exactly
   one $D^2$ and one $\bar D^2$ must remain on one $\delta^4$; fewer give zero, more
   reduce by (5B.9). The factor $16$ of (5B.19) is the project-normalization loop factor.
4. **Constrained derivatives.** EOM insertions contracted into chiral lines produce
   projected deltas $\mathbf 1_\pm$, never bare $\delta^8$ (§6.2) — the regulated version
   of this statement is the entire Step-5 anomaly mechanism.

## 9. Momentum-space rule table (tree-level complete, both signatures)

All momenta incoming; every vertex carries $(2\pi)^4\delta^4(\sum p)$ and its
$\vartheta$-integral $\int d^4\vartheta$ (after §8 rule 1); every loop carries $\int
d^4\ell/(2\pi)^4$ (the $d$-dimensional DRED ledger is deliberately **not** fixed here —
it belongs to the settlement obligation). Propagators: (5B.17), (5B.21). Vertices: §7
words differentiated by (5A.61)–(5A.62). Lorentzian denominators carry
$p_L^2-i\varepsilon$ by (5B.D3). External-leg operators follow §8 rule 2.

For the one-loop letter program the needed set is closed and finite: (V1) cubic+quartic,
(V2) $n=1,2$, (V3), (V4) cubic, (V5) insertions, propagators (5B.17)/(5B.21).

## 10. Decision ledger and blocker status

| decision | content | status |
|---|---|---|
| (5B.D1) | FF perturbative slice, both signatures; kernels (5B.10$'$) | extends seed (D1); owner-authorized 2026-07-16 for $E$; $L$ extension **requires authorization** |
| (5B.D2) | NK external measure-only branch + irrelevance lemma, both signatures | extends seed (D2); lemma proven §5.3 |
| (5B.D3) | Fourier ledger + Lorentzian Feynman cycle | **new; requires owner authorization**; resolves `BLOCKED_STEP3D_LC_VECTOR_CYCLE` for the perturbative slice if adopted |

Blocker book-keeping against (5A.80): `…PERTURBATIVE_SLICE_UNFIXED` → discharged by
(5B.D1) upon authorization (both signatures); `…NK_BRANCH_UNSELECTED` → discharged by
(5B.D2); `…FOURIER_DRED_LEDGER_UNFIXED` → Fourier half discharged by (5B.D3), DRED half
remains with the settlement contract; `BLOCKED_STEP3D_LC_VECTOR_CYCLE` → resolution
proposed by (5B.D3), Lorentzian nonperturbative cycle questions remain outside the slice.

## 11. What remains deferred (unchanged from the seed memo)

(i) a local-$\mathcal Y$ BV completion of the FF slice (impossible as stated, (5A.79));
(ii) Wess–Zumino/component ↔ superfield BV equivalence (used by the Step-5D component
route as an independent-route caveat, see the Step-5D memo §1); (iii) background-covariant
$\mathcal Y$ and NK field dependence; (iv) the $d$-dimensional (DRED) ledger.

## 12. Equation-anchored exact checks

`tests/test_step5b_feynman_rules.py` (runs in CI via `verify`):

| test | checks |
|---|---|
| T1, T2 | (5B.4), (5B.5) — Clifford/generator components, both signatures |
| T3 | (5B.7) — $\{D,\bar D\}$ operator identities on the full Grassmann module |
| T4 | (5B.8)$\equiv$(3A.12)+(3B.4) — $D^2\vartheta^2=-4$, $\bar D^2\bar\vartheta^2=-4$, $[\vartheta^2\bar\vartheta^2]_D=1$ |
| T5 | (5B.9) — the three workhorse identities, both signatures |
| T6 | (5B.10a) — projector idempotence/orthogonality/completeness |
| T7 | (5B.14) — vector kernel inversion |
| T8 | (5B.16) — chiral kernel inversion on the constrained space |
| T9 | (5B.18) — $\delta^4(\vartheta)$ reproducing property |
| T10 | (5B.19)/(5B.19a) — loop saturation and fewer-$D$ vanishing |
| T11 | (5B.15) — vector component normalization, both signatures |
| T12 | (5B.3a) — measure conversion lemma |
| T13 | (5B.13) footnote — $\mathfrak k$-term boundary identity |
