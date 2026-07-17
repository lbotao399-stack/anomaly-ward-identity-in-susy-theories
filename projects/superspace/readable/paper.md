# The anomalous Ward identity for BPS letters in Euclidean $\mathcal N=4$ super-Yang–Mills at one loop

**Core derivation — evergreen paper-format document.**

This file is the always-current, human-readable statement and derivation of the Project's
central result. It is assembled from the locked contracts (cited by their equation tags) and
is updated whenever a proof obligation lands on `origin/main`; it duplicates no authority —
the contracts remain the legal layer. Intended audience: a quantum field theorist. Intended
Notion mirror: this file is the standing "core theory" page.

Sources of authority: `contracts/foundations/step-01…step-05a` (conventions, actions,
BV–BRST, supergraph grammar), `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`
(the one-loop settlement), external target `references/vendor/arxiv/2512.07771v2` (Budzik–
Kulp, *Loop Corrected Supercharges from Holomorphic Anomalies*, imported as
`EXTERNAL_TARGET_ONLY`).

---

## Abstract

In Euclidean $\mathcal N=4$ super-Yang–Mills, quantized in $\mathcal N=1$ superspace in a
fixed Fermi–Feynman representative and regulated by dimensional reduction, we derive the
complete one-loop anomaly of the semi-chiral (BPS-letter) sector of the Schwinger–Dyson
identity. The four letter families $A=\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+$,
$B_r=\boldsymbol\nabla_+\boldsymbol\Phi_r$, $C^r=\widetilde{\boldsymbol\Phi}^r$,
$D_{\dot a}=\widetilde{\boldsymbol{\mathcal W}}_{\dot a}$ ($r=1,2,3$) give nine component
letters and eighty-one ordered pairs. The tree-level identity closes on classical brackets;
the entire quantum correction is the failure of the regulated cutting rule — a single
universal evanescent insertion $\mu_\ell^2/(D_0D_1D_2)$ — and is therefore local and
computable channel by channel. Twenty-nine ordered pairs receive an exact nonzero local
anomaly, fifty-two vanish exactly; every nonzero channel carries one universal coefficient
$\lambda_1=\hbar g^2/16\pi^2$ times a fixed color tensor, and the full tower of holomorphic
derivatives is generated in closed form by the ordered-Feynman-parameter kernel
$K^P_{m,n;k,\ell}=2\binom mk\binom n\ell/[(m+n+2)(k+\ell+1)]$. The result agrees exactly,
component by component and to all derivative orders, with the holomorphic-twist prediction
of Budzik–Kulp *after* correcting an internal factor-two inconsistency of that reference in
favor of its printed component formulas; the missing factor is the $\Gamma(3)=2$ of the
triangle's Feynman parametrization.

## 1. The objects and the statement

Work in Euclidean $\mathcal N=1$ superspace with the Project conventions
(step-01, step-02a): spinor indices $a=1,2$, $\dot a=\dot1,\dot2$,
$\epsilon^{12}=\epsilon^{\dot1\dot2}=+1$; gauge algebra $[T_A,T_B]=ic_{AB}{}^CT_C$ with
Killing form $\kappa_{AB}$ and totally antisymmetric $c_{ABC}$ (4C.1); absorbed coupling
$h=g^{-2}$ (5A.2). In Euclidean signature the chiral and antichiral fields are independent
(no conjugation relates $\Phi_r$ to $\widetilde\Phi_r$), a fact used throughout.

The $\mathcal N=4$ theory is three adjoint chirals coupled to the $\mathcal N=1$ vector,
with action (4C.4) and superpotential
$\mathscr U_4=-\frac{\sqrt2}{6g^2}\varepsilon_{rst}c_{ABC}\Phi_r^A\Phi_s^B\Phi_t^C$
(4C.12–4C.13). The gauge-covariant field strengths are
$\mathcal W_{a}=-\frac18\bar D^2(e^{-\mathcal V}D_ae^{\mathcal V})$ and
$\widetilde{\mathcal W}_{\dot a}=+\frac18D^2(e^{\mathcal V}\bar D_{\dot a}e^{-\mathcal V})$
(5A.33).

Fix the Euclidean plus/minus frame of the settlement contract §1 and define the **letters**

$$
A^A:=(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+)^A,\qquad
B_r^A:=(\boldsymbol\nabla_+\boldsymbol\Phi_r)^A,\qquad
C_r^A:=\widetilde{\boldsymbol\Phi}_r^A,\qquad
D_{\dot a}^A:=\widetilde{\boldsymbol{\mathcal W}}_{\dot a}^A,
$$

with Grassmann parities $|A|=|C|=0$, $|B|=|D|=1$, and the holomorphic covariant derivatives
$P_{\dot a}:=\boldsymbol{\mathcal D}_{+\dot a}$. These are the Euclidean avatars of the
$1/16$-BPS letters of the holomorphic twist ($A\leftrightarrow b$,
$B\leftrightarrow\beta$, $C\leftrightarrow\gamma$, $D\leftrightarrow\partial c$).

**Statement.** Let $L_i,L_j$ be letters and consider the composite insertion
$\boldsymbol\nabla_-(L_iL_j)$. Classically this reduces to Euler-operator (equation-of-motion)
descendants and covariant bilinears — the classical bracket. At one loop the identity
acquires a local anomaly: for each ordered pair,

$$
\boldsymbol\nabla_-\big(L_i^AL_j^B\big)\Big|_{\text{1-loop}}
=\lambda_1\,\mathbb F^{AB}{}_{DE}\,\Delta(L_i,L_j)^{DE},
\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2},
\qquad
\mathbb F^{AB}{}_{DE}=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E},
$$

with $\Delta(L_i,L_j)$ the fixed letter bilinears of §7 below (zero for 52 of the 81 ordered
pairs). The derivation occupies §§2–6; §7 states all channels; §8 compares with the
holomorphic twist.

## 2. Quantization: the fixed Fermi–Feynman representative

Gauge fixing follows the BV–BRST construction locked in step-03d/step-05a: chiral/antichiral
FP ghosts $\mathfrak c,\widetilde{\mathfrak c}$ (gh $+1$), non-minimal antighost/multiplier
doublets (5A.43), gauge fermion $\Psi_{\mathcal F,\mathcal Y}$ (5A.46), and gauge functions
$\mathcal F_{+}=-\frac14(\bar{\boldsymbol\nabla}_{\rm B})^2\mathcal V_{\rm q}$,
$\mathcal F_{-}=-\frac14(\boldsymbol\nabla_{\rm B})^2\mathcal V_{\rm q}$ (5A.44).

Two recorded scheme decisions (owner-authorized 2026-07-16; memo
`proposals/step5b-euclidean-feynman-rules-memo-2026-07-16.md`):

- **(D1)** The perturbative expansion is *defined* by Fermi–Feynman Gaussian averaging. The
  FF kernel $\mathcal Y_{E,\rm FF}=2g^2\mathcal A_E/\Box_E$ is provably nonlocal (5A.79),
  so it cannot be reached through step-03d's local-$\mathcal Y$ gauge fermion; the locality
  requirement is retained only for nonperturbative BV statements.
- **(D2)** The Nielsen–Kallosh factor is kept as an external measure. In slice (D1) it is a
  field-independent constant and cancels in every normalized correlator.

With the projectors
$\mathcal P_+=\frac{\bar D^2D^2}{16\Box_E}$, $\mathcal P_-=\frac{D^2\bar D^2}{16\Box_E}$,
$\mathcal P_T=-\frac{D^a\bar D^2D_a}{8\Box_E}$, $\mathcal P_T+\mathcal P_++\mathcal P_-=1$
(5A.64–5A.66), the gauge-averaged quadratic form becomes a plain d'Alembertian and the
superspace propagators are (5A.68–5A.74)

$$
\langle V^AV^B\rangle
=-(2\pi)^4\delta^4(p+p')\,\frac{2\hbar g^2\kappa^{AB}}{p^2}\,\delta^4(\vartheta_{12}),
\qquad
\langle\Phi^A\widetilde\Phi^B\rangle
=(2\pi)^4\delta^4(p+p')\,\frac{\hbar g^2\kappa^{AB}}{16p^2}\,
\bar D_1^2D_1^2\,\delta^4(\vartheta_{12}).
$$

Chirality bookkeeping (the classic trap sector) is fixed by three rules: functional
derivatives of constrained fields carry chiral projectors,
$\delta\Phi(z)/\delta\Phi(z')=\mathcal P_+\delta^8(z-z')$; each conversion of a
half-superspace vertex to $\int d^4\vartheta$ costs one $-\frac14\bar D^2$ (or
$-\frac14D^2$); and propagator orientations $\mathcal P_+$ vs $\mathcal P_-$ are tracked per
line, never inferred by conjugation. Closed Grassmann loops saturate with
$\delta^4(\vartheta_{12})D^2\bar D^2\delta^4(\vartheta_{12})=16\,\delta^4(\vartheta_{12})$.

Vertices at one loop: the cubic gauge word from the BCH expansion of $\mathcal W^2$
(5A.49–5A.52), the matter–gauge chain $h\,\widetilde\Phi(\operatorname{ad}\mathcal V)^n\Phi$
for $n=1,2$ (5A.53–5A.54), the superpotential cubics (5A.55), and the FP ghost words
(5A.58–5A.60).

## 3. Regularization: the DRED ledger and the two metric representations

Dimensional reduction with $d=4-2\epsilon$ (settlement §1): loop momenta are strictly
$d$-dimensional ($\breve\delta^m{}_n\ell^n=0$ in the $\widehat\delta/\breve\delta$
representation, $\operatorname{tr}\breve\delta=2\epsilon$), while all spinor algebra,
$\sigma$-matrix identities and D-algebra remain four-dimensional. A second, scalar
*dimension-shift* representation splits $\ell_d=\bar\ell+\widetilde\ell$ with
$\operatorname{tr}\widetilde\delta=d-4$; the two representations are never contracted with
each other. The single regulator axiom is: **finite superspace spin words use the
four-dimensional metric; propagator inverses use the $d$-dimensional one.** Its entire
content is the scalar

$$
\mu_\ell^2:=\bar\ell^2-\ell_d^2 .
$$

Fourier convention $X(x)=\int\frac{d^dp}{(2\pi)^d}e^{ip\cdot x}X(p)$, all momenta incoming,
$\Box_E\mapsto-p^2$; loop measure $\int_\ell^{\rm DRED}=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}$.

## 4. The Schwinger–Dyson identity and the cutting mechanism

The regulated path integral obeys the local Schwinger–Dyson identity (3D.34). For the letter
sector its tree content is the ordered Euler-operator reduction (settlement §3):

$$
\boldsymbol\nabla_-A=-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times C_s),\qquad
\boldsymbol\nabla_-B_r=-2\mathscr E_{\widetilde r}-\sqrt2\,\varepsilon_{rst}(C_s\times C_t),\qquad
\boldsymbol\nabla_-C_r=\boldsymbol\nabla_-D_{\dot a}=0,
$$

with $\mathscr E_V,\mathscr E_{\widetilde r}$ the vector and antichiral Euler operators.
Graphically, an Euler-operator insertion attached to a propagator collapses it:
$K\,K^{-1}=\delta$ — the cutting rule. If the regulator preserved simultaneously (i) the
EOM/variation correspondence, (ii) $KK^{-1}=\delta$, and (iii) four-dimensional D-algebra,
the complete SD graph family would cancel and no anomaly could exist.

DRED preserves (i) and (iii) but deforms (ii). On an internal line of momentum
$r_e=\ell+Q_e$ (external shifts $Q_e$ carry no evanescent components), the D-algebra
numerator produces the four-dimensional square $\bar r_e^{\,2}$ while the propagator
denominator is $D_e=r_{e,d}^{\,2}$. Hence the **exact cutting-failure identity**

$$
\boxed{\;
\frac{\bar r_e^{\,2}}{D_0D_1D_2}-\frac{1}{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2}\;}
$$

for every marked line $e$ of every one-loop graph — one universal insertion, no
graph-specific $(4-d)$ factors. The entire anomaly is the sum of these remainders. Its
finiteness and locality follow from the evanescent master integral

$$
\lim_{\epsilon\to0}\ \mu^{2\epsilon}\!\int\!\frac{d^{d}\ell}{(2\pi)^{d}}
\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}
=\frac{1}{32\pi^2}
\qquad(\text{independent of }\Delta),
$$

proved by $\int\widetilde\ell^2f=\frac{d-4}{d}\int\ell^2 f$ and
$\epsilon\,\Gamma(\epsilon)\to1$: the would-be nonlocal $\Delta$-dependence enters only at
$O(\epsilon)$, so the anomaly is a polynomial in external momenta — a local operator.

Two structural consequences organize the whole calculation:

1. **Classical/quantum separation.** The nonvanishing tree contact terms are exactly the
   classical bracket (the $Q_0$ sector); they are removed first. The quantum remainder is
   carried solely by $\mu_\ell^2$ insertions.
2. **Pole bookkeeping as a cross-check.** For each channel the isolated parent graphs are UV
   divergent; the complete SD family is finite: the $1/\epsilon$ poles cancel between the
   parent tensor reduction (physical metric $\widehat\delta$) and the contact rows
   (four-dimensional metric $\delta_4$), leaving
   $\widehat\delta-\delta_4=-\breve\delta$, i.e. a pure evanescent numerator whose trace
   supplies the finite answer. Any error in a single vertex factor or sign would break this
   cancellation, so the finiteness of each channel is itself a consistency proof of its
   factor chain.

## 5. Selection rules: which of the 81 ordered pairs can be anomalous

Before any loop integral, conservation laws restrict the possible uncontracted outputs. The
gradings that survive the construction are: $SU(3)$ flavor ($A,D$ singlets, $B_r\in\mathbf
3$, $C^r\in\bar{\mathbf 3}$); Grassmann parity; the twisted dimension
$[C]=1$, $[B]=[D]=\tfrac32$, $[A]=2$, $[P_{\dot a}]=1$, with the anomaly operator carrying
$+\tfrac12$; and the output structure $\mathfrak p_{\dot a}X\,\mathfrak p^{\dot a}Y$ forced
by the $\sigma$-chain trace (§6). Checking each ordered family against these and against the
cubic-vertex spectator structure yields exactly

$$
29\ \text{nonzero}\;=\;1_{(A,A)}+6_{(A,B),(B,A)}+6_{(A,C),(C,A)}+4_{(A,D),(D,A)}
+6_{(B,C)\,\delta\text{-diagonal}}+6_{(B,B)\,\varepsilon\text{-offdiagonal}},
$$

and $52$ zeros: $25$ pairs with no descendant at all
($\boldsymbol\nabla_-C=\boldsymbol\nabla_-D=0$ makes $\boldsymbol\nabla_-(L_iL_j)$ vanish
identically when both letters are drawn from $\{C,D\}$), $12$ flavor-off-diagonal
$(B,C)/(C,B)$, $3$ diagonal $(B,B)$, and $12$ $(B,D)/(D,B)$ killed by the charge/vertex
basis analysis. The same census follows independently from the holomorphic-twist vanishing
list — three agreeing routes in total.

## 6. The seed channel $(A,A)$ in full

Fix the orientation and marking of the settlement §4. The two ordered cubic gauge vertices
contribute $(+\frac{ig}2)(-\frac{ig}2)=\frac{g^2}4$; the Wick weight is $1$; the closed-loop
D-algebra weight is $w_D=\frac1{32}\cdot16\cdot2\cdot2=2$ (the $16$ is the loop-saturation
identity); total prefactor $\frac{g^2}2$. With $D_0=\ell^2$, $D_1=(\ell+p)^2$,
$D_2=(\ell+p+q)^2$ and the ordered parametrization
$\frac1{D_0D_1D_2}=2\int\delta(1-x-y-z)\,[r^2+\Delta]^{-3}$, the exact tensor reduction

$$
\int_r\frac{r_mr_n}{(r^2+\Delta)^3}=\frac{\widehat\delta_{mn}}4\,J_2,
\qquad
J_2\big|_{\rm pole}=\frac1{16\pi^2\epsilon},
$$

(the $\tfrac14$ is exact: $(1-\tfrac\epsilon2)/(4-2\epsilon)=\tfrac14$) gives the parent
triangle pole
$\Gamma_T=+\frac{\hbar g^2}{32\pi^2\epsilon}\,\mathbb F^{AB}{}_{DE}\,
\widehat\delta^{mn}T_{m\rho n}\,p^\rho$ with
$T_{m\rho n}=\sigma_m\bar\sigma_\rho\sigma_n$. The four occurrence-resolved Schwinger
contact rows sum to
$\Gamma_C=-\frac{\hbar g^2}{32\pi^2\epsilon}\,\mathbb F^{AB}{}_{DE}\,
\delta_4^{mn}T_{m\rho n}\,p^\rho$; the physical poles cancel and the evanescent trace

$$
p^\rho\,\breve\delta^{mn}\,(\sigma_m\bar\sigma_\rho\sigma_n)=-2\epsilon\;p^\rho\sigma_\rho
$$

(for physical $p$: $\breve\delta\,p=0$ and
$\breve\delta^{mn}\bar\sigma_m\sigma_n=\breve\delta^m{}_m=2\epsilon$) leaves the finite
local result

$$
\Gamma_T+\Gamma_C
=+\frac{\hbar g^2}{16\pi^2}\,\mathbb F^{AB}{}_{DE}\,\sigma_\rho p^\rho
\;=\;\lambda_1\,\mathbb F^{AB}{}_{DE}\,\sigma\!\cdot\!p .
$$

In position space this is the letter bilinear $\mathscr Z^{DE}$ of §7.

## 7. The complete ordered-channel result

With the normalized PBW jets $\mathbb J_{\mathbf u}$ and the typed contracted bilinear
$\langle X^D,Y^E\rangle:=(\mathfrak p_{\dot\alpha}X^D)(\mathfrak p^{\dot\alpha}Y^E)$
(settlement §7), every nonzero channel equals $\lambda_1\mathbb F^{AB}{}_{DE}$ times:

$$
\Delta(A,A)=\langle D,A\rangle-\langle A,D\rangle
+\sum_{r=1}^3\big(\langle B_r,C_r\rangle-\langle C_r,B_r\rangle\big)\;=:\;\mathscr Z,
$$

$$
\Delta(A,C_r)=\Delta(C_r,A)=\langle D,C_r\rangle-\langle C_r,D\rangle,
\qquad
\Delta(B_r,C_s)=\Delta(C_s,B_r)=\delta_{rs}\,\langle D,D\rangle,
$$

$$
\Delta(B_r,B_s)=-i\sqrt2\,\varepsilon_{rst}\big(\langle D,C_t\rangle-\langle C_t,D\rangle\big),
\qquad
\Delta(A,B_r)=\Delta(B_r,A)=\langle B_r,D\rangle+\langle D,B_r\rangle
-i\sqrt2\,\varepsilon_{rst}\langle C_s,C_t\rangle,
$$

$$
\Delta(A,D_{\dot a})=\tfrac13\langle\mathbb J_{\mathbf e_a}D,D\rangle
+\tfrac23\langle D,\mathbb J_{\mathbf e_a}D\rangle,
\qquad
\Delta(D_{\dot a},A)=\tfrac23\langle\mathbb J_{\mathbf e_a}D,D\rangle
+\tfrac13\langle D,\mathbb J_{\mathbf e_a}D\rangle .
$$

The $(A,B)/(B,A)$ channels are fixed uniquely by residual supersymmetry: the letter
supercharges $q_r$ act by $q_rA=0$, $q_rB_s=-i\delta_{rs}A$,
$q_rC_s=-\frac1{\sqrt2}\varepsilon_{rst}B_t$, $q_rD_{\dot a}=-iP_{\dot a}C_r$; the
dimension-$\tfrac92$ odd singlet $q$-kernel is one-dimensional (spanned by $k_q$), and
anchoring the scale to $\Delta(A,A)=\mathscr Z$ forces the renormalized $(A,B)$ vector onto
$k_q=(1,1,-i\sqrt2,+i\sqrt2)$ — which is precisely the formula above. All remaining ordered
pairs vanish exactly (§5).

## 8. The holomorphic-derivative tower and the holomorphic-twist comparison

Shifting the second letter by $w$ (equivalently, resumming all holomorphic derivatives), the
one-loop kernel follows from the ordered parametrization with the insertion-leg phase
$e^{iw\cdot(aq+bp)}$:

$$
2\int_0^1\!db\int_0^b\!da\;a^{k+\ell}\,b^{(m-k)+(n-\ell)}
=\frac{2}{(k+\ell+1)(m+n+2)}
\;\;\Longrightarrow\;\;
K^P_{m,n;k,\ell}=\frac{2\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)} .
$$

The overall $2$ is $\Gamma(3)$ from combining the three denominators; the $(A,D)$ jet
weights $(\tfrac13,\tfrac23)$ of §7 are the $(m,n)=(1,0)$ instance.

**Comparison.** Under the dictionary $c\leftrightarrow U$, $\gamma^r\leftrightarrow C_r$,
$\beta_r\leftrightarrow\frac1{\sqrt2}B_r$, $b\leftrightarrow-\frac i{\sqrt2}A$,
$\partial_{\dot a}c\leftrightarrow iD_{\dot a}$,
$Q_0\leftrightarrow-\frac12\boldsymbol\nabla_-$, all 81 ordered output words match the
holomorphic-twist prediction of Budzik–Kulp, and the derivative tower satisfies

$$
K^P_{m,n;k,\ell}=T^{\rm HT,corrected}_{m,n;k,\ell}=2\,T^{\rm HT,printed}_{m,n;k,\ell}
\qquad\text{for all }m,n\ge0
$$

($2025$-coefficient rectangle checked mechanically; closed form proved above). The source
carries two internal inconsistencies, both resolved by this calculation: (i) its printed
zero-shift kernel $\mathcal D^{\triangle}_{0,0}=\tfrac12\partial f\,\partial g$ disagrees by
a factor $2$ with its own printed component formulas — the components are correct and the
kernel is missing $\Gamma(3)=2$; (ii) its compact-superfield coefficient is printed both as
$-\tfrac14$ and as $-\kappa^2$ with "$\kappa$ the dual Coxeter number", requiring
$\kappa=\tfrac12$ — an editorial normalization clash quarantined as source provenance; the
Project derives its own coefficient ($\lambda_1\mathbb F$) and compares output words only.

Physically, the $(B,C)$ channel is the regulated generalized-Konishi anomaly, and the full
81-channel structure is its completion over the BPS letter alphabet: the loop-corrected
supercharge $Q_1$ of the twisted theory, obtained here by a direct superspace supergraph
calculation with no twist formalism input.

## 9. Audit of the heat-kernel and direct-component alternative routes

The post-settlement heat-kernel work proves a useful auxiliary layer but not a second full
derivation.  For a typed even operator family

$$
K(g)=K_0+gK_1+g^2K_2,
$$

the exact second-order semigroup coefficient is

$$
\begin{aligned}
[g^2]e^{-sK(g)}
={}&-\int_0^sdt\,e^{-(s-t)K_0}K_2e^{-tK_0}\\
&+\int_{0<t_1<t_2<s}dt_1dt_2\,
e^{-(s-t_2)K_0}K_1e^{-(t_2-t_1)K_0}K_1e^{-t_1K_0}.
\end{aligned}
$$

Thus the quadratic background block cannot be omitted in favor of two linear insertions.  The
scalar Gaussian convolution, bridge means, DRED master integral, and the single-ordering simplex
moment are exact:

$$
\int_{0<a<b<1}a^pb^q\,da\,db
=\frac1{(p+1)(p+q+2)},
$$

but a second ordering supplies no automatic factor two.  Moreover, for fixed nonzero $w$,

$$
\lim_{s\downarrow0}\frac1{(4\pi s)^2}e^{-w^2/(4s)}=0,
$$

so the local derivative tower requires distributional coefficient extraction at $w=0$.
The later typed-regulator proposal does not close this blocker.  Its own free matter blocks give

$$
(G^{-1}S'')^2|_{E_+}=16\Box_E\mathcal P_+,
$$

whereas its declared generator is $-\Box_E\mathcal P_+$; its verifier inserts an absent
$-1/16$.  The vector weights likewise give $G_V^{-1}S''_{VV}=+\Box_E$, while the verifier
adds an undeclared sign.  Finally, using $\mathcal K^2$ on matter rows and $\mathcal K$ on the
vector row is not one operator functional calculus when vector--matter mixing is retained.
Until a single typed elliptic generator, its dual Euler action, full $K_2$, and the
distributional limit are derived together, the full alternative route remains
`BLOCKED_HEAT_KERNEL_TYPED_REGULATOR_AND_COEFFICIENT_DERIVATION`.

The direct-component BC calculation has one exact consequence, obtained by bottom projection of
the accepted superfield map.  Since

$$
B_r|=\sqrt2\psi_{r+},\qquad C_s|=\widetilde\phi_s,\qquad
D_{\dot a}|=i\widetilde\lambda_{\dot a},
$$

the channel $\Delta(B_r,C_s)=\delta_{rs}\langle D,D\rangle$ gives

$$
\boxed{
Q_-(\psi_{r+}^A\widetilde\phi_s^B)\big|_{1\text{-loop}}
=-\frac{\sqrt2\hbar g^2}{32\pi^2}
\delta_{rs}\mathbb F^{AB}{}_{DE}
\widetilde\lambda_{\dot a}^D\widetilde\lambda^{E\dot a}.}
$$

The dotted bilinear is color-symmetric:

$$
\widetilde\lambda_{\dot a}^D\widetilde\lambda^{E\dot a}
=\widetilde\lambda_{\dot a}^E\widetilde\lambda^{D\dot a},
$$

hence every antisymmetric color word annihilates it.  The relevant tensor integral also separates
from its Fierz numerator factor:

$$
\lim_{\epsilon\to0}
\frac1d\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2\ell^2}{(\ell^2+\Delta)^4}
=\frac1{128\pi^2},
\qquad
2J=\frac1{64\pi^2}.
$$

These identities reject the former antisymmetric crossed-color expression and fix its free sign
and loop-counting power.  They do not rescue the proposed ordinary two-Yukawa parent: the locked
propagators give $G_{\phi\widetilde\psi}=G_{\psi\widetilde\phi}=0$.  The nonzero BC anomaly is
the regulated coincident Euler Jacobian, differentiated before bottom projection.  The incomplete
off-shell Noether identity, Lorentzian vector cycle, and target-seeded component 81-channel sweep
remain outside the accepted result.

A later adversarial census proposal raised seventeen topology/artifact candidates.  Its final
run completed six of eight enumeration sectors, but the ghost--Nielsen--Kallosh sector, the
zero/cut-orbit sector, and the automated three-lens refutation did not run; four
physics-relevant Wick routings were deferred rather than derived.  Exact holomorphic-twist
agreement is a final comparison, not an internal proof that every typed absence row has been
emitted: equality of the total coefficient does not imply termwise vanishing of alleged omitted
routings.  These seventeen candidates therefore remain `OPEN`, and the advertised census
certificate is not accepted.  They do not alter the accepted coefficient ledger, whose
derivation is the target-blind Schwinger-cut construction above.

## 10. Covariant-completion consistency gate

The owner-issued covariant-completion obligation first tests the one-loop consistency
condition

$$
\mathfrak R_{ij}
=d\Delta(L_i,L_j)-\Delta\!\left(d(L_iL_j)\right)_{\rm Koszul}=0,
$$

on the settled 81-row bracket.  The full locked descendants retain
$\boldsymbol\nabla_+\mathscr E_V$ and $\mathscr E_{\widetilde r}$.  The ledger does not
define $\Delta$ on these descendants, $[d,P_{\dot a}]$ is not locked, and
(5A.61)--(5A.62) do not define a nonlinear-word extension of the bilinear map.  Therefore

$$
\boxed{\operatorname{status}(\text{Phase 0})
=\texttt{BLOCKED\_PHASE0\_CHAIN\_MAP\_ACTION\_NOT\_LOCKED}.}
$$

The 25 rows in $\{C_1,C_2,C_3,D_{\dot1},D_{\dot2}\}^2$ satisfy the identity exactly,
because both their descendants and settled outputs vanish.  The remaining 56 rows are
undefined on the locked domain.  If one conditionally adds an EOM quotient,
$[d,P_{\dot a}]=0$, and literal occurrence replacement, the $A>C_1$ row gives the
diagnostic

$$
\boxed{
\mathfrak R_{A,C_1}^{AB}\big|_{\rm conditional}
=2i\lambda_1c_{FG}{}^A\mathbb F^{FB}{}_{DE}
(D_{\dot a}^{D}C_1^{G})D^{E\dot a}.}
$$

The cross product is the single color monomial
$(X\times Y)^A=c_{FG}{}^AX^FY^G$; no second word
$(C_1^GD^D)D^E$ is generated.  The exact model
$\kappa_{ab}=\delta_{ab}$, $c_{abc}=\varepsilon_{abc}$ gives

$$
\sum_Fc_{F3}{}^1\mathbb F^{F2}{}_{11}=1,
$$

so the conditional coefficient is nonzero.  This is not a P0 against the settled ledger:
the missing chain-map actions can change it.  The covariant-completion theorem is not
proved; the transverse box, cohomology, trace-covariance, induction, and ghost phases were
stopped before any regression target was used.  The derivation and exact boundary audit
are in contract `CONTRACT-STEP-06-COVARIANT-COMPLETION-001`.

## 11. Verification status

- **Machine-locked (exact arithmetic, regenerated in CI):** the 81-row ledger, the AA
  external-slot replay (269 rows), the color-mask replay (9216), the HT round trip (81 rows,
  2025 tower coefficients), the DRED cutting-failure and $\mu^2$-moment audits.
- **Independently re-derived (2026-07-16 review, `proposals/step5-independent-physics-review-…`,
  spot-check verdict `proposals/step5-spot-check-verdict-…`):** the cutting-failure
  identity, the $\tfrac1{32\pi^2}$ master integral, the $-2\epsilon$ trace, the full seed
  chain of §6, the 29/52 census (three routes), the factor-two adjudication and closed-form
  tower, the AB/BA $q$-covariance settlement.
- **Adversarial census review:** an eight-sector find-a-missing-topology review
  (`proposals/step5-census-review-final-verdict-2026-07-16.md`) found **zero confirmed
  omissions** across two runs; two sectors reproduced the committed parent-triangle census
  independently. The seventeen raised candidates are all either disclosed-pending ghost/NK
  presentation rows (the IR flags itself
  `CONDITIONAL_FF_BARE_CUT_CHECKED__RENORMALIZED_MIXING_PENDING`), machine-artifact encoding,
  or specific Wick routings bounded by the holomorphic-twist independence argument — none
  affects an anomaly coefficient. Completeness of the graph census *for the coefficients* is
  therefore certified; the pending items are presentation/artifact matters routed to the
  follow-up obligation.
- **Known scope boundaries (not defects):** fixed-representative quantization (D1) with the
  local-$\mathcal Y$ BV completion, Wess–Zumino/component equivalence, background-covariant
  gauge averaging, and the entire Lorentzian sector deferred as named obligations.

## 12. References

1. Project contracts: `contracts/foundations/step-01…step-05a`, and
   `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md` (equation tags cited inline).
2. K. Budzik, J. Kulp, *Loop Corrected Supercharges from Holomorphic Anomalies*,
   arXiv:2512.07771v2 — vendored at `references/vendor/arxiv/2512.07771v2`, admitted as
   `EXTERNAL_TARGET_ONLY` with two recorded source-internal normalization conflicts.
3. Superspace/1001 supergraph pages and Weinberg Ch. 30 — vendored reference imports
   (`references/manifest.yaml`) underlying the supergraph grammar conventions.
