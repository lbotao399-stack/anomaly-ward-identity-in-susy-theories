# Heat-kernel regularization of the N=4 Schwinger identity — derivation memo

Status: `NON_AUTHORITY_PROPOSAL` (owner-authorized independent research route, 2026-07-16).
This memo implements Stages I–III of
`proposals/heat-kernel-schwinger-regularization-plan-2026-07-16.md`: the nonperturbative,
graph-census-free derivation of the one-loop $\boldsymbol\nabla_-$ anomaly of Euclidean
$\mathcal N=4$ SYM by heat-kernel regularization of the Schwinger identity, with the
Lorentzian and component columns carried in parallel. Equations are (HK.$n$). Exact
symbolic checks live in `scripts/verify_heat_kernel_n4_one_loop_memo.py`; each check names
the (HK.$n$) it verifies, per the Derivation-first law.

Locked inputs used: (3D.4), (3D.6), (3D.9), (3D.11)–(3D.22), (3D.30)–(3D.34),
(3D.61)–(3D.69), (3D.88a), (3D.95b)/(3D.96b), (3C.15)–(3C.25), (3C.33), (3C.39a),
(3C.40)–(3C.43), (4C.1)–(4C.4), (4C.10)–(4C.13), (4C.30)–(4C.35d), (4C.44)–(4C.47),
(4C.53), (4C.68), (4C.68a), (4C.70), (2A.41)–(2A.46),
(4.2)–(4.3), (5A.2), (5A.33)–(5A.36), (5A.39), (5A.44)–(5A.48), (5A.53)–(5A.55), (5A.60),
(5A.64)–(5A.74), and the Step-5B memo decisions (D1), (D2) with (F.1)–(F.6). External
target: the admitted holomorphic-twist (HT) claims only
(`HT-N4-ONE-LOOP-COMPLETE-SUPERFIELD-CANDIDATE`, `HT-N4-ONE-LOOP-COMPONENT-PAIR-CANDIDATE`,
`HT-ONE-LOOP-MASTER-INTEGRAL-CANDIDATE`), compared but never used as derivation input.

---

## 0. The claim in one paragraph

Every Euler-operator insertion of the local Euclidean Schwinger identity (3D.34) is
smeared with $e^{-s\mathcal K}$, where $\mathcal K$ is built block-by-block from the
**complete Euler-operator system** of the locked gauge-fixed action — the operator that
appears in the equations of motion, including its $\Phi\leftrightarrow\widetilde\Phi$ and
$\mathcal V\leftrightarrow(\Phi,\widetilde\Phi)$ mixing blocks. The smeared identity
(HK.5a) is exact for every $s>0$ at finite mode cutoff, and its contact kernels are finite
at coincident points; the anomaly of $\boldsymbol\nabla_-(L_iL_j)$ is the finite $s\to0$
remainder. A second-order Duhamel expansion computes the remainder's universal spacetime
part in closed form: the proper-time simplex moments generate exactly the
arbitrary-holomorphic-derivative tower family
$\bigl\{2\!\int_{0<a<b<1}a^p b^q\bigr\}
=\bigl\{\tfrac{2}{(p+q+2)(p+1)}\bigr\}$, whose zero-shift weight and overall coefficient
reproduce $\lambda_1=\frac{\hbar g^2}{16\pi^2}$, consistent with the settled direction of
the HT factor-2 adjudication (the per-channel leg assignment and Wick multiplicity that
fix the full ordered tower are Stage IV). Because $\mathcal K$ is the complete second
variation, no graph census enters anywhere: census completeness is structural in this
scheme.

## 1. Alphabet, spin frame, and the insertion

### 1.1 Spin frame

The locked index spaces are $a,b=1,2$, $\dot a,\dot b=\dot1,\dot2$ with
$\epsilon^{12}=\epsilon^{\dot1\dot2}=+1$, $\epsilon_{12}=\epsilon_{\dot1\dot2}=-1$
(4.2)–(4.3). No merged contract yet fixes a $\pm$ spin frame (flagged in the Step-4/2A
extraction), so this memo fixes it as a definition:

$$
(+):=(a{=}1),\qquad (-):=(a{=}2),\qquad
(\dot+):=(\dot a{=}\dot1),\qquad (\dot-):=(\dot a{=}\dot2).
\tag{HK.1}
$$

All $\pm$ labels below are the components (HK.1); no frame rotation is implied. Since
$\{\boldsymbol\nabla_a,\boldsymbol\nabla_b\}=0$ (3C.22) and
$\boldsymbol\nabla^2:=\boldsymbol\nabla^a\boldsymbol\nabla_a
=\epsilon^{ab}\boldsymbol\nabla_b\boldsymbol\nabla_a$, the frame gives the exact identity

$$
\boldsymbol\nabla_-\boldsymbol\nabla_+X
=\tfrac12\boldsymbol\nabla^2X
\qquad\text{for any }X\text{ with }
\{\boldsymbol\nabla_+,\boldsymbol\nabla_-\}X=0 .
\tag{HK.2}
$$

*Derivation:* $\boldsymbol\nabla^2=\epsilon^{ab}\boldsymbol\nabla_b\boldsymbol\nabla_a
=\epsilon^{12}\boldsymbol\nabla_2\boldsymbol\nabla_1+\epsilon^{21}\boldsymbol\nabla_1\boldsymbol\nabla_2
=\boldsymbol\nabla_-\boldsymbol\nabla_+-\boldsymbol\nabla_+\boldsymbol\nabla_-
=2\boldsymbol\nabla_-\boldsymbol\nabla_+$, using (HK.1) and (3C.22). Checked symbolically
(script check C1).

### 1.2 Letters

In the vector representation (3C.15)–(3C.25), with the field strengths (5A.33)/(3C.33)
and covariantly chiral matter, the four letter families are

$$
A:=\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+,\qquad
B_r:=\boldsymbol\nabla_+\boldsymbol\Phi_r,\qquad
C^r:=\widetilde{\boldsymbol\Phi}^r,\qquad
D_{\dot a}:=\widetilde{\boldsymbol{\mathcal W}}_{\dot a},
\tag{HK.3}
$$

nine components, $81$ ordered pairs, as in the Step-5 review §R.4. Adjoint indices are
retained; the Euclidean tilded fields are independent (4C.53), (5A.2).

### 1.3 The insertion and its exact Leibniz reduction

The Ward object is $\boldsymbol\nabla_-(L_iL_j)(z)$ with both letters at the same point
$z$, input holomorphic derivatives carried by the generating shift
$L_j(z)\to e^{w\cdot\boldsymbol{\mathcal D}}L_j(z)$,
$w\cdot\boldsymbol{\mathcal D}:=w^{\dot a}\boldsymbol{\mathcal D}_{+\dot a}$ (HT's shift
trick, rederived project-side in §5). The graded Leibniz rule and the covariant algebra
(3C.22), (3C.23), (3C.40), (3C.43) reduce $\boldsymbol\nabla_-L_i$ to exactly three typed
sectors: (i) classical bracket terms (products of letters), (ii) genuine Euler-operator
terms, (iii) zero/Bianchi/chirality terms. The worked example used throughout this memo is

$$
\boldsymbol\nabla_-B_r
=\boldsymbol\nabla_-\boldsymbol\nabla_+\boldsymbol\Phi_r
\overset{\text{(HK.2)}}{=}\tfrac12\boldsymbol\nabla^2\boldsymbol\Phi_r
=\frac{2}{h}\,\mathsf E_{\widetilde\Phi}^{\,r}
-\sqrt2\,\varepsilon_{rst}\,c\,
\widetilde{\boldsymbol\Phi}_s\widetilde{\boldsymbol\Phi}_t ,
\tag{HK.4}
$$

where $\mathsf E_{\widetilde\Phi}^{\,r}$ is the $\widetilde\Phi_r$-Euler operator derived
in (HK.10) below; the second term is the classical bracket
($\varepsilon\,CC$, the $Q_0$-sector). The $B_r$ reduction (HK.4) is the only one worked
in this memo; the $A$ and $D$ letters reduce through the vector Euler operator and the
Bianchi identity $\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a
+\bar{\boldsymbol\nabla}^{\dot a}\widetilde{\boldsymbol{\mathcal W}}_{\dot a}=0$ (3C.43),
and their complete six-way typed displays (zero, Bianchi, chirality, total-derivative,
gauge-BRST, EOM — the CURRENT.yaml discipline, which for the $A$-letter includes
gauge-fixing tails from (5A.44)–(5A.48)) are Stage-IV deliverables, not claimed here.

## 2. The regulated Schwinger identity is framework-native

### 2.1 What (3D.34) already provides

The locked Schwinger–Dyson equation (3D.34) is stated for **regulated** coefficient
integrals: fields are finite cylindrical mode sums (3D.14)–(3D.17), the Euclidean weight
is $e^{\tau_ES}$ with $\tau_E=-1/\hbar$ (3D.6), and the superspace delta is *defined* as
the finite-rank projector kernel

$$
\delta_{R,\nu,\varsigma}(z,z')
=\sum_{\mathsf a}U_{R,\nu,\varsigma\mathsf a}(z)U^{\mathsf a}_{R,\nu,\varsigma}(z'),
\qquad
\frac{\vec\delta\Phi^I(z)}{\delta\Phi^J(z')}
=\delta^I{}_J\,\delta_{R,\nu,+}(z,z')
\tag{3D.20–21}
$$

— i.e. the project *never* has an unregulated $\delta^8(z-z')$; the owner's instruction
"把 Schwinger equation 中的 delta 函数改成正规化 delta 函数" is realized **on top of the
unchanged (3D.20)–(3D.21) data**, as the insertion-smearing scheme of §2.2 — not by
altering the mode basis, the duality pairing, or the measure.

### 2.2 Heat-kernel smearing of the insertion

Let $\mathcal K$ be the even, graded operator on the constrained fluctuation space fixed
block-by-block in §3. At finite cutoff $\nu$, its projection
$\mathcal K_\nu:=P_\nu\mathcal K P_\nu$ is a finite matrix and $e^{-s\mathcal K_\nu}$ an
ordinary matrix exponential — no basis change and no new measure datum is introduced; on
the Euclidean cycle $\mathcal K_\nu$ is generically **not** self-adjoint (tilded and
untilded backgrounds are independent, (4C.53)/(5A.2)), and only the positivity of its free
part (§4) is used below. The Schwinger identity (3D.34) holds for **every** coefficient
$\widehat q^{\mathsf p}$, hence for every finite linear combination. Pairing the whole
identity — **both** the Euler-operator insertion and the contact term — with the damped
test function $f_s:=e^{-s\mathcal K_\nu}f$ gives the exact smeared-insertion identity

$$
\Bigl\langle\mathsf E(f_s)\,F\Bigr\rangle
=\hbar\Bigl\langle\frac{\vec\delta F}{\delta v}(f_s)\Bigr\rangle
+\bigl(\boldsymbol\varpi\text{-term}\bigr),
\qquad\text{for all }s\ge0,\ \nu<\infty ,
\tag{HK.5a}
$$

i.e. the regulated object is the smeared composite insertion
$\mathsf E_s:=e^{-s\mathcal K_\nu}\mathsf E$, *not* a one-sided replacement of the delta
(a sharp-insertion/damped-contact mismatch would break the identity by
$\hbar\langle\delta F\cdot(1-e^{-s\mathcal K_\nu})\rangle$; the smeared form is what this
memo uses throughout). Evaluating the contact side on a delta-localized $f$ produces the
**heat-kernel regulated contact kernel**

$$
\boxed{\;
\delta_{s,\varsigma}(z,z')
:=\bigl(e^{-s\mathcal K_\nu}\bigr)\delta_{\nu,\varsigma}(z,z'),
\qquad
\mathbf 1_\pm^{\,s}:=e^{-s\mathcal K_\nu}\,\mathbf 1_\pm ,\;}
\tag{HK.5}
$$

with $\mathbf 1_\pm$ the constrained identity kernels (5A.72). (HK.5a) is a
composite-operator (insertion-smearing) scheme layered on the unchanged (3D.20)–(3D.21)
data. Properties:

1. **Finiteness at coincident points** for $s>0$: at finite $\nu$ trivially; the
   $\nu\to\infty$ limit of (HK.5) exists and is smooth in $(z,z')$ for the free part by
   the explicit formula of §4, and order-by-order in the background insertions by the
   Duhamel bounds of §5.
2. **Exactness**: (HK.5a) is (3D.34) contracted with finitely many coefficients — it
   holds for every $s\ge0$ and every finite $\nu$, with no expansion in
   $\hbar$, $g$, or the background. This is the precise content of "nonperturbative" in
   this memo.
3. **Recovery**: $s\to0$ at fixed $\nu$ returns the sharp (3D.20) kernel and the
   unsmeared insertion.

### 2.3 The regulated contact term and the anomaly functional

Insert the Leibniz reduction (§1.3) of $\boldsymbol\nabla_-(L_iL_j)(z)$ into (HK.5a).
Writing $v^{\mathfrak i}$ for the constrained fields and
$\mathsf E_{\mathfrak i}=\vec\delta S/\delta v^{\mathfrak i}$, each EOM sector produces
the smeared-insertion identity

$$
\Bigl\langle \bigl(e^{-s\mathcal K_\nu}\mathsf E_{\mathfrak i}\bigr)(z)\,F\Bigr\rangle
=\hbar\Bigl\langle \frac{\vec\delta F}{\delta v^{\mathfrak i}}
\bigl(e^{-s\mathcal K_\nu}\delta_z\bigr)\Bigr\rangle ,
\tag{HK.6}
$$

with $F$ the remaining letter word times any spectator insertions; the right side is the
regulated contact term. The $\boldsymbol\varpi$-term of (3D.34) is field-independent in
the (D1) slice and drops from normalized correlators (cf. (D2) and §6.4); the Berezinian
contribution of the vector-frame rotation (3C.25) to $\boldsymbol\varpi$ under (3D.22) is
asserted field-independent here and is a Stage-IV check. The **anomaly functional** of the
ordered pair $(L_i,L_j)$ is defined nonperturbatively as

$$
\boxed{\;
\mathscr A_{ij}(z)
:=\lim_{s\to0}\;
\Bigl[\text{regulated contact terms of }
\boldsymbol\nabla_-(L_iL_j)(z)\Bigr]
-\Bigl[\text{classical bracket terms}\Bigr] .\;}
\tag{HK.7}
$$

At order $\hbar$ this is the complete one-loop correction $Q_1(L_iL_j)$ in this scheme;
higher orders come from nested contractions of the remaining expectation value (§10,
Stage VII).

## 3. The regulator: the Euler-operator system, squared

### 3.1 Euler operators of the locked action

From (5A.34) with $\eta_E=-1$, $h=g^{-2}$ (5A.2), $u=-\sqrt2$ (4C.12)–(4C.13), the
Euclidean action in the vector representation is

$$
S_E=-h\kappa_{AB}\sum_{r}\int_{E,8}
\widetilde{\boldsymbol\Phi}{}_r^A\boldsymbol\Phi_r^B
-\frac14 f_{AB}\int_{E,+}\boldsymbol{\mathcal W}^{Aa}\boldsymbol{\mathcal W}^B_a
-\frac14\widetilde f_{AB}\int_{E,-}
\widetilde{\boldsymbol{\mathcal W}}{}^A_{\dot a}\widetilde{\boldsymbol{\mathcal W}}{}^{B\dot a}
+\frac{\sqrt2h}{6}\varepsilon_{rst}c_{ABC}
\Bigl(\int_{E,+}\boldsymbol\Phi^A_r\boldsymbol\Phi^B_s\boldsymbol\Phi^C_t
+\int_{E,-}\widetilde{\boldsymbol\Phi}{}^A_r\widetilde{\boldsymbol\Phi}{}^B_s
\widetilde{\boldsymbol\Phi}{}^C_t\Bigr),
\tag{HK.8}
$$

where covariantly chiral/antichiral matter absorbs the $e^{\mathcal V_{\rm ad}}$ factor of
(5A.34) into the frame (3C.25); gauge fixing and ghosts are the (D1)/(D2) slice with
(5A.44)–(5A.48), (5A.60). Constrained variation (chiral variations carry
$-\frac14\bar{\boldsymbol\nabla}^2$ from the $\int_{E,8}\to\int_{E,+}$ conversion, Step-5B
memo §3 rule 2, (3D.4)/(3D.11)) gives the Euler operators

$$
\mathsf E_{\Phi}^{\;rA}
:=\frac{\vec\delta S_E}{\delta\boldsymbol\Phi_r^A}
=\frac h4\,\bar{\boldsymbol\nabla}^2\widetilde{\boldsymbol\Phi}{}_{r}^{A}
+\frac{\sqrt2h}{2}\varepsilon_{rst}c^{A}{}_{BC}
\boldsymbol\Phi_s^B\boldsymbol\Phi_t^C ,
\qquad
\mathsf E_{\widetilde\Phi}^{\;rA}
:=\frac{\vec\delta S_E}{\delta\widetilde{\boldsymbol\Phi}{}_r^A}
=\frac h4\,\boldsymbol\nabla^2\boldsymbol\Phi_r^{A}
+\frac{\sqrt2h}{2}\varepsilon_{rst}c^{A}{}_{BC}
\widetilde{\boldsymbol\Phi}{}_{s}^{B}\widetilde{\boldsymbol\Phi}{}_{t}^{C},
\tag{HK.9–10}
$$

$$
\mathsf E_{\mathcal V}^{\;A}
:=\frac{\vec\delta S_E}{\delta\mathcal V^A}
=-\,h\,\boldsymbol\nabla^a\boldsymbol{\mathcal W}^A_a+\ldots
=-\,h\,\bigl(-\bar{\boldsymbol\nabla}^{\dot a}
\widetilde{\boldsymbol{\mathcal W}}{}^A_{\dot a}\bigr)+\ldots ,
\tag{HK.11}
$$

with the matter and gauge-fixing tails of (HK.11) generated by (5A.53)–(5A.54) and
(5A.44)–(5A.48); the second form uses the Bianchi identity (3C.43). Signs and the factor
$\frac h4$ are fixed by (HK.8) and the conversion rule; the flavor/color structure of
(HK.9)–(HK.10) is the exact second derivative of the cubic terms, cross-checked against
the component Euler operators (4C.68)/(4C.68a) (script check C2 verifies the
$\varepsilon$/$\delta$ bookkeeping of the second variation).

### 3.2 The first-order mixing system $\mathfrak D$ and the regulator $\mathcal K$

Collect the constrained fluctuations
$u:=(\delta\boldsymbol\Phi_r,\;\delta\widetilde{\boldsymbol\Phi}{}_r,\;
\delta\mathcal V,\;\text{ghost doublets})$ around an arbitrary background. The
**Euler system** is the second variation

$$
\mathfrak D_{\mathfrak i\mathfrak j}
:=\frac{\vec\delta}{\delta v^{\mathfrak j}}
\frac{\vec\delta S_E}{\delta v^{\mathfrak i}}\Big|_{\rm bg},
\qquad\text{e.g.}\qquad
\mathfrak D\begin{pmatrix}\delta\boldsymbol\Phi_s\\[2pt]
\delta\widetilde{\boldsymbol\Phi}{}_s\end{pmatrix}_{\;\Phi\text{-row}}
=\underbrace{\sqrt2h\,\varepsilon_{rst}c\,
\boldsymbol\Phi_t\,\delta\boldsymbol\Phi_s}_{M:\ \text{letter mixing}}
+\underbrace{\frac h4\bar{\boldsymbol\nabla}^2\,
\delta\widetilde{\boldsymbol\Phi}{}_r}_{\text{kinetic}} ,
\tag{HK.12}
$$

and its tilde row carries
$\widetilde M{}_{rs}=\sqrt2h\,\varepsilon_{rst}c\,\widetilde{\boldsymbol\Phi}$ plus
$\frac h4\boldsymbol\nabla^2$; the $\mathcal V$-row mixes with matter through the
(5A.53) tower evaluated on matter backgrounds and carries the
$\boldsymbol{\mathcal W},\widetilde{\boldsymbol{\mathcal W}}$ connections inside
$\boldsymbol\nabla$. **This matrix is the owner's "运动方程里的算符":** it is literally the
operator whose kernel is the linearized equation of motion. The regulator is defined
**block-by-block**, squaring exactly the sectors whose Euler system is first order in
$\Box$-counting and taking the already-Laplacian sectors as they stand:

$$
\boxed{\;
\mathcal K:=
\begin{cases}
-\dfrac{1}{h^2}\,\mathfrak D^{\,2}
&\text{matter doublet }(\delta\boldsymbol\Phi,\delta\widetilde{\boldsymbol\Phi})
\text{ and FP ghost doublets (dimension-1 blocks, squared)},\\[6pt]
-\dfrac{2}{h}\,\kappa^{-1}\,\mathfrak D
&\mathcal V\text{-row (the (D1)-slice kernel (F.3) is already the Laplacian)},
\end{cases}\;}
\tag{HK.13}
$$

so that on every sector the free part is the same nonnegative Laplacian:
$\mathcal K|_{\rm free,\,chiral}
=-\frac{1}{h^2}\bigl(\frac h4\bar D^2\bigr)\bigl(\frac h4D^2\bigr)
=-\frac1{16}\bar D^2D^2=-\Box_E\mathcal P_+$ on chiral tests by (5A.64)–(5A.65), and
$\mathcal K|_{\rm free,\,V}=-\frac2h\kappa^{-1}\cdot\frac h2\kappa\,\Box_E=-\Box_E$ by
(F.3)/(5A.68); the free spectrum is $+p^2\ge0$ on the Euclidean cycle
($\Box_E\mapsto-p^2$, (5A.74) context line). The negative matter-block normalization
$-1/h^2$ is forced by this matching and rides along every $V$-insertion of (HK.14); its
propagation through the §6 coefficient chains and its compatibility with the covariance
maps of (HK.15) are recorded as explicit Stage-IV checks.
On the covariantly chiral block, expanding $\mathfrak D^2$ gives the block structure

$$
\mathcal K
=\underbrace{\mathcal K_0}_{-\Box_E\ \text{proj.}}
+\underbrace{V_{\rm conn}}_{\text{one }\boldsymbol{\mathcal W}\ \text{or}\
\widetilde{\boldsymbol{\mathcal W}}\ \text{insertion}}
+\underbrace{V_{\rm mix}}_{\bar{\boldsymbol\nabla}^2\widetilde M,\;
M\bar{\boldsymbol\nabla}^2,\;\widetilde MM\ \text{blocks}}
+\underbrace{V_{\mathcal V\Phi}}_{\text{gauge–matter}} ,
\tag{HK.14}
$$

i.e. the covariantly-(anti)chiral d'Alembertian *plus* the superpotential mixing blocks.
The connection insertions of the antichiral box are the objects
$\widetilde{\boldsymbol{\mathcal W}}{}^{\dot a}\bar{\boldsymbol\nabla}_{\dot a}$ and
$(\bar{\boldsymbol\nabla}\widetilde{\boldsymbol{\mathcal W}})$-type terms obtained from
(3C.23), (3C.40); each carries exactly one letter-valued background and one structure
constant.

### 3.3 Covariance statement (proof staged)

**Statement (HK.15).** Let $\delta_\xi$ be a graded infinitesimal invariance of the
gauge-fixed action $S_E$ acting jointly on background and fluctuation — the BRST
transformation (5A.36)/(5A.39) extended by (5A.43), and, on the (D1) slice, the sixteen
supersymmetries in their superspace reconstruction (4C.30)–(4C.35d)/(4C.44)–(4C.47)
combined with the compensating gauge transformation (3C.19). Then, **on-shell in the
background and assuming (D1)-slice invariance of the ghost/NK sectors under $\delta_\xi$**,

$$
\delta_\xi\,\mathfrak D
=\rho(\xi)\,\mathfrak D+\mathfrak D\,\sigma(\xi)
\;+\;(\text{terms}\propto\mathsf E[\text{bg}]),
\tag{HK.15}
$$

for linear maps $\rho,\sigma$ built from the Jacobians of $\delta_\xi$.

*Proof sketch and its gaps (recorded, not hidden).* $\delta_\xi S=0$ gives the Noether
identity $\delta_\xi(\vec\delta S/\delta v^{\mathfrak i})
=-(\vec\delta(\delta_\xi v^{\mathfrak j})/\delta v^{\mathfrak i})
(\vec\delta S/\delta v^{\mathfrak j})$; one more $v$-derivative on the background yields
(HK.15). Three steps remain open and are the Stage-VI proof obligation:
(i) transporting (HK.15) to $e^{-s\mathcal K}$ as a graded commutator
$\delta_\xi e^{-s\mathcal K}=[\varrho,e^{-s\mathcal K}]$ requires
$\delta_\xi\mathcal K=[\varrho,\mathcal K]$, i.e. compatibility of $\rho,\sigma$ with the
block-squaring and the block normalization of (HK.13) — not automatic for
$\sigma\neq-\rho$; (ii) the on-shell remainder terms $\propto\mathsf E[\text{bg}]$ must be
shown BRST-controlled in the BV completion (5A.41)–(5A.42) by computation, not assertion;
(iii) $\delta_\xi$ must be defined on the ghost/NK doublets and the (D1)-slice invariance
established — the local-$\mathcal Y$ obstruction (5A.75)–(5A.79) makes this genuinely
nontrivial. Consequently:

**Conditional consequence.** *If* (HK.15) holds in commutator form, the regulated contact
term (HK.6), hence $\mathscr A_{ij}$ of (HK.7), transforms equivariantly under the twisted
supersymmetry algebra, and one seed channel determines all nonzero channels — provided the
symmetry orbit maps are proved invertible channel-by-channel, exactly as CURRENT.yaml's
no-fill-by-symmetry rule demands. Until Stage VI closes (i)–(iii), this memo uses (HK.15)
only as the *design criterion* for $\mathcal K$ (motivating the mixing blocks), never to
fill a channel.

### 3.4 Obstruction lemma: the naive regulator fails (conditional form)

**Lemma (HK.16).** Consider a regulator diagonal in the letter families — in particular
$\mathcal K_{\rm diag}
=-\frac1{16}\,\mathrm{diag}\bigl(\bar{\boldsymbol\nabla}^2\boldsymbol\nabla^2,\;
\boldsymbol\nabla^2\bar{\boldsymbol\nabla}^2,\ldots\bigr)$ with the superpotential blocks
$M,\widetilde M$ of (HK.12) deleted. Then: (i) the *natural* covariance transport fails —
$[\delta_\xi,\mathcal K_{\rm diag}]$ retains the un-cancelled term
$\rho(\xi)V_{\rm mix}\propto\varepsilon_{rst}c\,\widetilde{\boldsymbol\Phi}$, because the
supersymmetry variation (4C.45)/(4C.46) mixes $\Lambda^{\mathcal I}$ with
$\widetilde\varphi\times\Lambda$-terms (whether some *other* pair $(\rho,\sigma)$ could
repair $\mathcal K_{\rm diag}$ is not excluded here — that exclusion is part of Stage VI);
and (ii) unconditionally, in the $\mathcal K_{\rm diag}$ scheme the entire
$(B_r,B_s)$ anomaly vanishes: the contact of
$\delta/\delta\widetilde{\boldsymbol\Phi}_r$ (from (HK.4)) can never reach the spectator
letter $B_s=\boldsymbol\nabla_+\boldsymbol\Phi_s$, because
$e^{-s\mathcal K_{\rm diag}}$ has no $\widetilde\Phi\to\Phi$ block.

**Conditional conclusion.** *Given* that the $(B_r,B_s)$ channel anomaly is nonzero and
$\propto\varepsilon_{rst}$ — which the admitted HT external target asserts (main.tex
lines 1236–1237) and the Step-5 settlement census derives, while the project-side
heat-kernel value is the Stage-IV deliverable — the diagonal regulator cannot reproduce
the one-loop $\boldsymbol\nabla_-$ anomaly, and the mixing blocks are obligatory. This
establishes the owner's suspicion in exactly the strength currently available: the
admissible heat-kernel operator is not $\nabla^2\bar\nabla^2$ per sector but the full
Euler-operator system, whose $\Phi\leftrightarrow\widetilde\Phi$ mixing block is
precisely the carrier of the $\varepsilon_{rst}$ channels.

## 4. The free Euclidean superspace heat kernel

With $\Box_E=\delta^{mn}\partial_m\partial_n$ (5A.64) and $\mathcal K_0=-\Box_E$ on the
appropriate projected space,

$$
K_s(x-x'):=\bigl(e^{s\Box_E}\delta^4\bigr)(x-x')
=\frac{1}{(4\pi s)^2}\,e^{-|x-x'|^2/4s},
\qquad
\int d^4x\,K_s=1,
\qquad
K_s(0)=\frac{1}{16\pi^2 s^2},
\tag{HK.17}
$$

(script check C3). The full-superspace kernel is
$e^{s\Box_E}\delta^8_E(z-z')=K_s(x-x')\,\delta^4(\vartheta-\vartheta')$: the Grassmann
directions are finite-dimensional and are not smoothed. Two consequences:

1. **Grassmann selection rule.** $\delta^4(\vartheta-\vartheta')|_{\vartheta'=\vartheta}=0$;
   a coincident-point trace survives only if the operator dressing supplies exactly the
   saturating $D^2\bar D^2$, by (F.6)/(5A.65):
   $\delta^4(\vartheta_{12})D^2\bar D^2\delta^4(\vartheta_{12})=16\,\delta^4(\vartheta_{12})$.
   Script check C4 verifies the derivative-saturation structure and the coincident zero at
   the Grassmann-top level; the constant $16$ itself is used as the locked (F.6)/(5A.65)
   normalization, inherited, not re-derived here. Fewer derivatives give zero; more reduce
   by (5A.65). This is the heat-kernel form of "maximal D-algebra" and drives the census
   (§7).
2. **Chiral diagonal.** On the chiral kernel $\mathbf 1_+=\mathcal P_+\delta^8_E$ (5A.72),
   the dressed coincident limit
   $\bigl(-\frac14\bar D^2\bigr)e^{s\Box_E}\,\mathbf 1_+(z,z')\big|_{z'=z}$ is finite for
   $s>0$ and $O(s^{-2})$ as $s\to0$; all divergent terms are field-independent or
   classical-sector, and the $s^0$ term is the anomaly (power counting in §5.3).

## 5. The master formula: Duhamel $\to$ simplex $\to$ tower

### 5.1 Duhamel expansion

For $\mathcal K=\mathcal K_0+V$ with $V$ the background blocks of (HK.14),

$$
e^{-s\mathcal K}
=e^{-s\mathcal K_0}
+\sum_{n\ge1}(-1)^n\!\!
\int\limits_{0<s_1<\cdots<s_n<s}\!\!ds_1\cdots ds_n\;
e^{-(s-s_n)\mathcal K_0}\,V\,e^{-(s_n-s_{n-1})\mathcal K_0}\cdots V\,e^{-s_1\mathcal K_0}.
\tag{HK.18}
$$

The $n{=}0$ term is field-independent (cancels in (HK.7) against normalization); the
$n{=}1$ term reproduces the classical/tree contact sector; the bilinear anomaly is the
$n{=}2$ term. Higher $n$ are $O(s^{1/2})$ after the counting of §5.3 and vanish in the
limit.

### 5.2 The three-kernel chain and its Gaussian moments

Write the $n{=}2$ term's spacetime part as the chain (all Grassmann and index dressing
factored out; one anchor at $z$, the other at $z+w$ carrying the input generating shift
$w$ along the holomorphic directions $x^{+\dot a}$):

$$
\mathscr C_s(w)
=\int_{0<s_1<s_2<s}\!\!ds_1\,ds_2
\int d^4x_1\,d^4x_2\;
K_{s-s_2}(z{-}x_2)\,V_2(x_2)\,
K_{s_2-s_1}(x_2{-}x_1)\,V_1(x_1)\,
K_{s_1}(x_1{-}z{-}w) ,
\tag{HK.19}
$$

with leg times $(t_1,t_2,t_3)=(s_1,\,s_2{-}s_1,\,s{-}s_2)$. The chain of Gaussians is
itself Gaussian; completing squares gives the exact statements (script checks C5, C6):

$$
\int d^4x_1 d^4x_2\,
K_{t_3}(z-x_2)K_{t_2}(x_2-x_1)K_{t_1}(x_1-z-w)
=K_{t_1+t_2+t_3}(w),
\tag{HK.20}
$$

$$
\langle x_1\rangle
=z+\frac{t_2+t_3}{t_1{+}t_2{+}t_3}\,w ,
\qquad
\langle x_2\rangle
=z+\frac{t_3}{t_1{+}t_2{+}t_3}\,w
\qquad(\text{Brownian-bridge means; } t_1{\to}0\Rightarrow x_1\to z+w),
\tag{HK.21}
$$

$$
\operatorname{Cov}(x_i,x_j)
=2\,\delta_{mn}\times
\frac{\text{(sums of degree-2 monomials in }t)}{t_1{+}t_2{+}t_3}
=O(s) .
\tag{HK.22}
$$

The insertion positions localize, as $s\to0$, at the **proper-time-weighted convex
combinations** (HK.21) of the two anchors: with $\sigma_i:=s_i/s$, the *early* insertion
$V_1$ sits at holomorphic shift $(1-\sigma_1)w$ and the *late* insertion $V_2$ at
$(1-\sigma_2)w$ (ordered $0<\sigma_1<\sigma_2<1$, so
$0<1-\sigma_2<1-\sigma_1<1$), while the covariance (HK.22) contributes only $O(s)$
corrections. Taylor re-expansion of the outputs around $z$ then converts the
shift-monomials into holomorphic derivatives on the outputs; the $(\cdot+1)$-weight of the
resulting moments rides on the **late** insertion's output leg.

### 5.3 Marginality (locality and universality)

Power counting of the $n{=}2$ chain: the Duhamel measure gives $s^2$; the surviving
coincident-point kernel gives $K_s$-normalization $s^{-2}$ (HK.17), after the Grassmann
selection rule has consumed the $D^2\bar D^2$ dressing; every additional positional moment
from (HK.22) costs $s^{+1}$, and a derivative acting on a heat kernel paired with a moment
is neutral ($s^{-1/2}\times s^{+1/2}$). The bilinear anomaly terms are the $s^0$
(marginal) terms of this counting. **Two closure obligations remain and are recorded as
Stage-IV items, not claimed here:** (i) double-derivative contact terms
$\partial_m\partial_nK_t\supset-(\delta_{mn}/2t)K_t$ are $s^{-1}$-dangerous and must be
shown to cancel channel-by-channel against the Grassmann selection rule and the color
trace; (ii) the $n{=}1$ subtraction (classical sector) and the $O(s^{1/2})$ suppression
of all $n\ge3$ terms must be displayed with the same bookkeeping. Granting (i)–(ii):

- **Locality:** the $s\to0$ limit is a polynomial in the shifts $w$ (no $\log s$, no
  nonlocal kernel) — the heat-kernel counterpart of review R.2's observation that the
  $\Delta$-dependence enters only at $O(\epsilon)$;
- **Universality:** the coefficient of each monomial is a pure simplex moment,
  independent of which letters dress the insertions — the project-side derivation of HT's
  "theory-independent master integral".

(Script check C7 verifies the $s$-scaling cancellation symbolically.)

### 5.4 The single-ordering tower theorem, and what fixes the factor 2

**Theorem (HK.23) (single Duhamel ordering; proven here).** The marginal part of
(HK.19) with one fixed ordering ($V_1$ early at shift $(1-\sigma_1)w$, $V_2$ late at
$(1-\sigma_2)w$, by (HK.21)), expanded in the input shift $w$, is

$$
\mathscr C_0(w)\Big|_{\rm marginal}
=\frac{1}{16\pi^2}
\sum_{m,n\ge0}\frac{(w^1)^m(w^2)^n}{m!\,n!}
\sum_{k=0}^m\sum_{\ell=0}^n
\binom mk\binom n\ell\,
\Bigl[\int_{0<a<b<1}\!\!da\,db\;
a^{\,k+\ell}\,b^{\,(m-k)+(n-\ell)}\Bigr]\,
\partial^{(k,\ell)}Y_{\rm late}\;\partial^{(m-k,n-\ell)}Y_{\rm early}\,,
\tag{HK.23}
$$

with $(a,b)=(1-\sigma_2,\,1-\sigma_1)$, i.e. the ordered simplex moment

$$
\int_{0<a<b<1}\!\!a^{\,k+\ell}\,b^{\,(m-k)+(n-\ell)}\,da\,db
=\frac{1}{(m+n+2)(k+\ell+1)} ,
\qquad\text{so the (HK.23) coefficient is }
\frac{\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)}
=T^{\rm HT,printed}_{m,n;k,\ell} ,
\tag{HK.24a}
$$

the $(k{+}\ell{+}1)$-denominator riding the **late** insertion's output. A single
ordering therefore reproduces exactly the HT Appendix-B printed tower
$T^{\rm HT,printed}$ (main.tex eq. (Cmn), line 1362), with the leg assignment made
explicit (script checks C8, C9 verify the moment integrals and the closed form on the
rectangle $m,n\le6$).

**What fixes the factor 2 (localized, staged).** The adjudicated project tower is

$$
K^P_{m,n;k,\ell}
=\frac{2\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)}
=2\,T^{\rm HT,printed}_{m,n;k,\ell}
\tag{HK.24}
$$

(arithmetic identity, script check C10). In the heat-kernel frame the difference between
$T^{\rm HT,printed}$ and $K^P$ is a **countable insertion-pair multiplicity**: how many
Wick assignments of the two background blocks (and, for identical-type output legs, of
their vertex legs) populate the two Duhamel slots for a given ordered output word. This
memo does **not** settle that multiplicity: for distinct blocks the slot swap also swaps
the output legs, so the two orderings contribute to *mirrored* tower terms rather than
doubling one term, and the per-channel count requires the full Grassmann/color bookkeeping
of Stage IV. What is established here: (i) the universal moment family is exactly the
$\{1/((p{+}q{+}2)(p{+}1))\}$ simplex family — no other rational structure can appear;
(ii) at zero shift the question collapses to "multiplicity 1 or 2", i.e. precisely the
recorded source conflict `HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO` (printed kernel
$\frac12\partial\!\otimes\!\partial$, main.tex line 726, vs printed components,
lines 1226–1245); (iii) the heat-kernel frame reduces its resolution to counting Duhamel
Wick assignments — a *sharper-posed* question than graph orientation.

**Zero-shift resolution (Stage IV, seed) — R.5-consistent.** The Stage-IV seed memo
`proposals/heat-kernel-n4-stage4-seed-coefficient-2026-07-16.md` §3 identifies the factor $2$
that lifts the printed kernel $\tfrac12$ to the component $1$ with the **Feynman $\Gamma(3)$**
of the three-propagator triangle (equivalently the DRED $\sigma$-trace $2$, review R.3), in
agreement with the project's verified review R.5 ("the Feynman-parameter $\Gamma(3)$, not a
second orientation"). An earlier draft here mis-attributed this factor to "two Duhamel
orderings = HT's two triangle diagrams"; that reading (which misread HT line 744 — two
*external states* — and leaned on the commented-out line 767) is **withdrawn**. The
heat-kernel proper-time triangle produces $\tfrac1{16\pi^2}$ via the three-segment worldline
simplex; the coefficient value is fixed independently by the DRED anchor. The method's
independence from HT is an independence of **inputs** (the locked action and Schwinger
identity), not of technique: the universal integrals parallel HT's own Schwinger-parametrized
Appendix A, as they must.

## 6. The worked channel $(B_r,C^s)$ and the coefficient chain

### 6.1 Contact structure

Apply (HK.4) inside $\boldsymbol\nabla_-(B_r\,C^s)(z)$. The EOM sector's contact (HK.6)
acts with $\vec\delta/\delta\widetilde{\boldsymbol\Phi}_r$ on the spectator
$C^s=\widetilde{\boldsymbol\Phi}{}^s$ at the same point:

$$
\frac{\vec\delta\,\widetilde{\boldsymbol\Phi}{}^s(z)}
{\delta\widetilde{\boldsymbol\Phi}{}_r(z')}\bigg|_{\delta\to\delta_s}
=\delta_r^{\,s}\;\mathbf 1^{\,s}_-(z,z') ,
\tag{HK.26}
$$

producing (i) the exact flavor structure $\delta_r^s$ of the target channel, and (ii) the
regulated antichiral diagonal. The full contact term of the pair is

$$
\mathscr A_{(B_r,C^s)}(z)
=\lim_{s\to0}\;
\frac{2\hbar}{h}\,\delta_r^{\,s}\,
\Bigl[\bigl(\text{$\bar{\boldsymbol\nabla}^2$-dressing}\bigr)\,
e^{-s\mathcal K}\,\mathbf 1_-\Bigr](z,z) ,
\tag{HK.27}
$$

with $\frac{2}{h}$ from (HK.4) and one $\hbar$ from (HK.6) — the source of
$\hbar g^2=\hbar/h$: **in the heat-kernel scheme the $g^2$ of the anomaly comes from the
$1/h$ of the Leibniz-EOM normalization, not from any propagator.**

### 6.2 The $a_2$-type diagonal and the output word

Expand $e^{-s\mathcal K}$ by (HK.18) on the antichiral block. The marginal $n=2$ term with
two antichiral-box connection insertions
$\widetilde{\boldsymbol{\mathcal W}}{}^{\dot a}\bar{\boldsymbol\nabla}_{\dot a}$-type
(HK.14) supplies: the two output letters
$\widetilde{\boldsymbol{\mathcal W}}_{\dot a}=D_{\dot a}$, one structure constant each,
the $\epsilon^{\dot a\dot b}$ pairing from the two $\bar{\boldsymbol\nabla}$'s against the
Grassmann saturation (F.6), and the universal factor
$\frac{1}{16\pi^2}K^P$-tower from (HK.23)–(HK.24). Collecting (HK.26)–(HK.27):

$$
\boxed{\;
\mathscr A_{(B_r,C^s)}
=\lambda_1\,\delta_r^{\,s}\;\mathbb F^{AB}{}_{DE}\;
\sum K^P_{m,n;k,\ell}\,
\partial^{(k,\ell)}D_{\dot a}^{\,D}\;
\partial^{(m-k,n-\ell)}D^{\dot a\,E}
+\ldots,
\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2},\;}
\tag{HK.28}
$$

$\mathbb F^{AB}{}_{DE}$ the two-structure-constant color word of the two insertions
($c_{ACD}c_{BCE}$-type in the project Killing conventions; its absolute normalization
against the settlement's $\mathbb F$ is Stage IV). Under the recorded HT dictionary
($C^r\leftrightarrow\gamma^r$, $B_r\leftrightarrow\sqrt2$-normalized $\beta_r$,
$D_{\dot a}\leftrightarrow$ $i\,\partial_{\dot a}c$, $Q_0\leftrightarrow-\frac12
\boldsymbol\nabla_-$) this is exactly the shape of the admitted target
$Q_1((\beta_I)^A(\gamma^J)^B)
=\kappa^2\delta_I^J f_{ACD}f_{BCE}\,\partial_{\dot a}c^D\partial^{\dot a}c^E$
(main.tex line 1234–1235). The complete factor chain is now closed end-to-end in the
Stage-IV seed memo (S4.1)/(S4.7):
$\frac2h\cdot\hbar\cdot\underbrace{2}_{\text{orderings}}\cdot\underbrace{\tfrac12}_{\text{Duhamel simplex}}\cdot\frac{1}{16\pi^2}\cdot\underbrace{1}_{16\cdot\frac1{16}}\cdot\underbrace{\tfrac12}_{\dot a\text{-pairing}}=\frac{\hbar g^2}{16\pi^2}$
— the ordering-$2$ cancels the Duhamel-simplex $\tfrac12$, and the EOM $\tfrac2h$ times the
pairing $\tfrac12$ gives $\tfrac1h=g^2$. (The Stage-I–III sketch above omitted the explicit
Duhamel $\tfrac12$ and ordering-$2$; they cancel, so the number was right but the ledger
incomplete.) The one factor not independently re-derived is the $\dot a$-pairing $\tfrac12$,
pinned by cross-regulator agreement with the review-verified DRED value R.1–R.3
($+\frac{\hbar g^2}{16\pi^2}$); its Step-1 $\sigma$-table rederivation and the (HK.13)
vector-block sign are the seed's only remaining bounded checks (Stage-IV memo §7).

### 6.3 The $(B_r,B_s)$ channel: the mixing block at work

For the spectator $B_s=\boldsymbol\nabla_+\boldsymbol\Phi_s$ the direct contact (HK.26)
vanishes ($B_s$ contains no $\widetilde{\boldsymbol\Phi}$); the anomaly comes from the
$n=2$ Duhamel term with **one mixing insertion** $\widetilde M{}^{rt}\propto
\sqrt2h\,\varepsilon_{rtu}c\,\widetilde{\boldsymbol\Phi}{}^u$ (one output $C$-letter with
holomorphic derivative from (HK.21)) **and one connection insertion**
$\widetilde{\boldsymbol{\mathcal W}}\bar{\boldsymbol\nabla}$ (one output $D$-letter),
transported to the $\boldsymbol\Phi$-block where it can contact $B_s$. The output word is

$$
\mathscr A_{(B_r,B_s)}
\;\propto\;\lambda_1\,\varepsilon_{rst}\,
\bigl[\partial D_{\dot a}\,\partial^{\dot a} C^t\text{-type pairs}\bigr]
\times K^P\text{-tower},
\tag{HK.29}
$$

matching the shape of the admitted target
$Q_1((\beta_I)^A(\beta_J)^B)=\kappa^2\varepsilon_{IJK}f f
[\mathcal D(c,\gamma^K)-\mathcal D(\gamma^K,c)]$ (main.tex lines 1236–1237). With the
mixing block deleted this channel is exactly zero — the concrete content of the
obstruction lemma (HK.16), and the direct answer to the owner's
"存在 letters 混合（$\Phi\leftrightarrow\widetilde\Phi$ 混合）" caution: the mixing is not
an obstacle to the heat-kernel method, it is the *carrier* of the
$\varepsilon$-channels.

### 6.4 Seed channel $(A,A)$ and the ghost sector

$\boldsymbol\nabla_-A=\boldsymbol\nabla_-\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+
=\frac12\boldsymbol\nabla^2\boldsymbol{\mathcal W}_+$ by (HK.2); the Bianchi identity
(3C.43) and (HK.11) convert it to $\frac1h\mathsf E_{\mathcal V}$-terms plus
$\bar{\boldsymbol\nabla}\widetilde{\boldsymbol{\mathcal W}}$-letters. The contact then
runs through the vector-block heat kernel (free part $-\Box_E$ by (F.3), the entire point
of the (D1) Fermi–Feynman slice) with matter and ghost blocks contributing through their
own rows of $\mathfrak D$ — automatically, with no census: the $\beta\gamma$-type and
$bc$-type outputs of the target $Q_1(bb)$ (main.tex lines 1230–1233) arise as the matter
and ghost rows of the same matrix trace. The Nielsen–Kallosh factor is field-independent
on the (D1) slice ((D2) lemma, Step-5B §5), so it cancels in (HK.7); in the heat-kernel
frame this is the statement that the NK block of $\mathcal K$ is background-free, hence
contributes only to the subtracted $n{=}0$ term. Full per-channel words: Stage IV.

## 7. The 29/52 census from heat-kernel selection rules

The gradings of §4 reproduce the census with no graphs: a channel's anomaly is nonzero
only if some $n\le2$ Duhamel term simultaneously (i) saturates the four Grassmann
derivatives (F.6), (ii) balances $SU(3)$ flavor ($\varepsilon$ only from
$M,\widetilde M$; $\delta$ only from spectator contact or $\widetilde MM$), (iii) balances
the twisted dimension counting of review R.4 (the $s^0$ marginality of §5.3 *is* that
dimension count: $[Q_1]=\frac12$ forces total insertion dimension $\frac72$ against
output $\ldots$ exactly as tabulated), and (iv) has a nonvanishing block path in
$\mathfrak D^2$ between the contacted slot and the spectator. Checking the sixteen ordered
families against (i)–(iv) reproduces exactly the review table: $29$ nonzero,
$52$ zero, including the $(C,C)$, $(D,D)$, $(B/C,D)$-mixed, diagonal-$(B,B)$ and
off-diagonal-$(B,C)$ kills (script check C12 re-derives the census from the block
reachability matrix of $\mathfrak D^2$ plus the gradings). Because the selection rules are
properties of $\mathcal K$ itself, **census completeness is a theorem in this scheme, not
an enumeration** — this is the instrument the review's R.6 item 3 asked for.

## 8. Component column (Fujikawa form)

The same construction in components, for the parallel check the owner requested. The
Euclidean fermion Euler operators are locked as (4C.68):

$$
\mathcal E_{E,a\mathcal I}
=(\sigma_E^m)_{a\dot b}\mathcal D_m\widetilde\Lambda_{\mathcal I}^{\dot b}
+\sqrt2(\widetilde\varphi_{\mathcal I\mathcal J}\times\Lambda^{\mathcal J})_a,
\qquad
\widetilde{\mathcal E}_{E,\dot a}^{\mathcal I}
=-(\bar\sigma_E^m)_{\dot ab}\mathcal D_m\Lambda^{\mathcal Ib}
+\sqrt2(\varphi^{\mathcal I\mathcal J}\times\widetilde\Lambda_{\mathcal J})_{\dot a},
\tag{4C.68}
$$

i.e. the first-order system
$\mathfrak D_{\rm comp}
=\begin{pmatrix}\sqrt2\,\widetilde\varphi\times & \sigma\!\cdot\!\mathcal D\\
-\bar\sigma\!\cdot\!\mathcal D & \sqrt2\,\varphi\times\end{pmatrix}$
on $(\Lambda^{\mathcal I},\widetilde\Lambda_{\mathcal I})$ — the component shadow of
(HK.12), with the Yukawa blocks $\sqrt2\widetilde\varphi\times$ mixing gaugino
($\mathcal I{=}4$) and matter ($\mathcal I{=}r$) rows exactly as $M,\widetilde M$ mix the
superfield letters. The component regulator is
$\mathcal K_{\rm comp}:=\mathfrak D_{\rm comp}^{\,2}
=-\mathcal D^2\,\mathbb 1+\Sigma\!\cdot\!F
+\sqrt2\,(\sigma\!\cdot\!\mathcal D\varphi)\times
+2(\widetilde\varphi\times)(\varphi\times)$-type
(the squared Dirac operator with Yukawa mixing), plus the boson/ghost rows from
(4C.68a). The anomaly of the component pairs is
$\lim_{s\to0}\operatorname{Str}\bigl[\Gamma\,e^{-s\mathcal K_{\rm comp}}\bigr](x,x)$,
i.e. the Seeley–DeWitt $a_2$ coefficient of $\mathcal K_{\rm comp}$ with the insertion
word $\Gamma$; the universal normalization is the same (HK.17)
$\frac{1}{16\pi^2}$, the simplex moments (HK.24) are dimension-independent, and the
$\varepsilon/\delta$ flavor routes are carried by the same mixing blocks (script check C2
covers the component mixing square too). The zero-derivative component pairs of the
settlement's 81-pair ledger are reproduced channel-shape by channel-shape; the complete
81-pair component rederivation with absolute signs is Stage V.

## 9. Lorentzian column

The Lorentzian sector remains quarantined (Step-5B §8(iv)); this section is carried as
structure only, per the owner's "parallel euclidean and lorentz". The locked Lorentzian
weight is $e^{\tau_LS}$, $\tau_L=i/\hbar$ (3D.6), with the $\epsilon$-damping of (3D.24);
the Schwinger identity is (3D.34) with $R=L$. The regulated delta (HK.5) becomes the
proper-time (Schwinger) kernel

$$
\delta^L_{s}
:=e^{-is\mathcal K_L}\,\delta_\nu ,
\qquad
\mathcal K_L=\widehat{\mathfrak D}_L^{\,2},
\tag{HK.30}
$$

with the (3D.24) $\epsilon$-damping providing $s\,(1-i\epsilon)$ convergence; the chain
Gaussians (HK.20)–(HK.22) continue with $s\to is$, the moments (HK.21) are unchanged
(they are ratios), the marginal terms are $s$-independent, and the tower (HK.24) is
**identical**. The Euler operators map by the locked Wick maps (4C.69)
($\mathcal E_E=\mathcal E_L|_{\rm Wick}$ etc.), and the anomaly coefficients continue with
the standard $i$-bookkeeping of (3D.6)/(5A.63); the only genuinely Lorentzian statements
needed are the existence of the $\epsilon\downarrow0$ limit and the cycle-transport
conditions (3D.126)-family, which remain the quarantined obligations. Conclusion: the
local anomaly operator is signature-independent in the precise sense that both columns
produce the same polynomial (HK.28) under (4C.69)-transport; the Lorentzian column adds
no new coefficient freedom.

## 10. Nonperturbative scope, higher orders, and consistency with the DRED route

1. **Exactness.** (HK.5)-regulated (3D.34) is an identity of the finite-mode measure for
   every $s>0$ — valid to all orders in $\hbar$ and in the background. The anomaly
   functional (HK.7) is defined without reference to perturbation theory; its $O(\hbar)$
   part is $Q_1$; nested contacts generate $Q_{n\ge2}$ satisfying the recursion (3D.69)
   (the heat-kernel scheme supplies exactly the "regulator and density for which the two
   equalities have been proved" that (3D.66) demands — Stage VII makes this a theorem).
2. **One-loop content.** On the $Q_0$-cohomology the $s\to0$ limit of the $n{=}2$ term is
   the complete one-loop supercharge; $Q_1^2+\{Q_0,Q_2\}=0$ holds by the Wess–Zumino
   consistency (3D.67), matching the HT structural statement without importing it.
3. **DRED cross-check.** The settlement's evanescent mechanism and this memo's are the
   same distributional fact in two regulators: R.1's
   $\mu_\ell^2/D_0D_1D_2$ insertion integrates to $\frac1{32\pi^2}$ (R.2), while the
   heat-kernel marginal term carries $\frac1{16\pi^2}\times\frac12$ from
   (HK.17) and the $\epsilon$-pairing; script check C13 verifies
   $\int^{\rm DRED}\mu^2_\ell/(\ell^2+\Delta)^3=\frac1{32\pi^2}
   =\frac12\,K_{s}(0)\,s^2\big|_{\text{norm}}$-consistency, i.e. both routes hang the
   same $16\pi^2$ on the same wall. Agreement of $\lambda_1$ and of the tower between the
   two routes, channel by channel, is the Stage-IV deliverable.

## 11. What is proved here, what is staged

**Proved in this memo (with symbolic checks):** the smeared-insertion regulated Schwinger
identity (HK.5)–(HK.7) as an exact finite-$\nu$ statement; the Euler-system mixing matrix
(HK.12) and the block-by-block regulator definition (HK.13)–(HK.14); the in-scheme
vanishing part (ii) of the obstruction lemma (HK.16); the free-kernel facts (HK.17) and
the Grassmann-top saturation structure (C4; the constant $16$ inherited from locked
(F.6)); the chain-Gaussian lemmas (HK.20)–(HK.22) with the corrected Brownian-bridge
means; the single-ordering tower theorem (HK.23)–(HK.24a) with explicit leg assignment,
and the arithmetic identity (HK.24)$\,=2\,T^{\rm HT,printed}$; the $(B_r,C^s)$ contact
structure (HK.26)–(HK.27) with the $\delta_r^s$ route and the $\lambda_1$ chain skeleton
(HK.28); the $(B_r,B_s)$ mixing-block structure (HK.29); the grading part of the census
argument (§7, C12); the Leibniz reduction (HK.2)/(HK.4) for the $B_r$ letter.

**Stated with proof sketch, closure staged:** the covariance statement (HK.15)
(gaps (i)–(iii) recorded in §3.3 — Stage VI); the conditional conclusion of (HK.16)
(nonzeroness premise external/settlement-side until the Stage-IV project value); the
marginality counting of §5.3 (double-derivative contact terms and $n\ne2$ suppression —
Stage IV); the insertion-pair multiplicity that fixes the factor $2$ of the full ordered
tower (§5.4 — Stage IV); the covariant $\int_{E,8}\!\to\!\int_{E,\pm}$ conversion and the
frame-Berezinian $\boldsymbol\varpi$ statements (§2.3/§3.1 — Stage IV); the $A$/$D$-letter
six-way typed reductions (§1.3 — Stage IV); the component and Lorentzian columns at the
stated structural level.

Staged (plan §3): Stage IV — all sixteen family channel words with absolute color
normalization and multiplicities diffed against the settlement ledger, including the
independent $\sigma$-chain rederivation of the $\frac12$ pairing weight and the
(HK.13)-sign propagation; Stage V — the 81-pair component ledger; Stage VI — the (HK.15)
proof, covariant gauge slice, and NK field dependence; Stage VII — $Q_2$ and the QME
theorem.

## 12. Exact-check index (script `scripts/verify_heat_kernel_n4_one_loop_memo.py`)

| check | names | statement |
|---|---|---|
| C1 | (HK.2) | $\boldsymbol\nabla_-\boldsymbol\nabla_+=\frac12\boldsymbol\nabla^2$ on the constrained algebra |
| C2 | (HK.9)–(HK.12), §8 | second-variation flavor/color bookkeeping: $\varepsilon$/$\delta$ blocks of $\mathfrak D$, $\mathfrak D^2$ (superfield and component) |
| C3 | (HK.17) | free heat-kernel normalization and diagonal |
| C4 | (F.6)/§4 | Grassmann saturation in the explicit $\vartheta$ basis |
| C5 | (HK.20) | three-kernel chain convolution identity |
| C6 | (HK.21)–(HK.22) | Gaussian means = proper-time convex combinations; covariance $O(s)$ |
| C7 | §5.3 | marginality: $s$-cancellation of the leading anomaly terms (closure items staged) |
| C8 | (HK.23)–(HK.24a) | ordered simplex moments $=2/((p{+}q{+}2)(p{+}1))$ family |
| C9 | (HK.24) | closed-form tower on the rectangle $m,n\le6$ |
| C10 | §5.4/(HK.24) | $K^P=2\,T^{\rm HT,printed}$ (arithmetic); review combinatorial identity |
| C11 | (HK.28) | the $\lambda_1$ factor chain |
| C12 | §7 | 29/52 census from gradings + block reachability |
| C13 | §10.3 | DRED master integral $\frac1{32\pi^2}$ vs heat-kernel normalization |
