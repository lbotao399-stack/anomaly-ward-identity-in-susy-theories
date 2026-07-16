# Independent review of the Claude alternative-route branches

Status: `VERIFIED_AUDIT_WITH_EXACT_BOTTOM_PROJECTION`.

The reviewed branch is not admitted as a new component derivation.  Its useful exact consequences are retained below; the incomplete BRST, Noether, component-box, and all-pairs claims are removed from the merge surface.  The original drafts remain in Git history.

## 1. Notation

The accepted Step-5 coefficient and ordered color tensor are

$$
\lambda_1=\frac{\hbar g^2}{16\pi^2},
\qquad
\mathbb F^{AB}{}_{DE}.
\tag{CR.1}
$$

The accepted bottom letters are

$$
B_r^A\big|=\sqrt2\,\psi_{r+}^A,
\qquad
C_s^B\big|=\widetilde\phi_s^B,
\qquad
D_{\dot a}^D\big|=i\widetilde\lambda_{\dot a}^D.
\tag{CR.2}
$$

For the component cross-check define $Q_-$ to be the bottom action induced by the same locked
$\boldsymbol\nabla_-$ that acts on the Step-5 letters.  No independent rephasing is introduced.

## 2. Exact BC bottom projection

The accepted regulated Schwinger orbit is

$$
\Delta(B_r^A,C_s^B)
=\delta_{rs}\lambda_1\mathbb F^{AB}{}_{DE}
\langle D^D,D^E\rangle.
\tag{CR.3}
$$

At zero holomorphic derivative,

$$
\begin{aligned}
\langle D^D,D^E\rangle\big|
&=D_{\dot a}^DD^{E\dot a}\big|\\
&=(i\widetilde\lambda_{\dot a}^D)
(i\widetilde\lambda^{E\dot a})\\
&=-\widetilde\lambda_{\dot a}^D
\widetilde\lambda^{E\dot a}.
\end{aligned}
\tag{CR.4}
$$

The one-loop part of the left side is

$$
\Delta(B_r^A,C_s^B)\big|
=\sqrt2\,
Q_-\!\left(\psi_{r+}^A\widetilde\phi_s^B\right)\Big|_{1\text{-loop}}.
\tag{CR.5}
$$

Combining (CR.1)--(CR.5),

$$
\boxed{
Q_-\!\left(\psi_{r+}^A\widetilde\phi_s^B\right)\Big|_{1\text{-loop}}
=-\frac{\lambda_1}{\sqrt2}
\delta_{rs}\mathbb F^{AB}{}_{DE}
\widetilde\lambda_{\dot a}^D\widetilde\lambda^{E\dot a}
=-\frac{\sqrt2\hbar g^2}{32\pi^2}
\delta_{rs}\mathbb F^{AB}{}_{DE}
\widetilde\lambda_{\dot a}^D\widetilde\lambda^{E\dot a}.}
\tag{CR.6}
$$

Thus the former symbol $\varsigma$ is fixed to $-1$, and the loop order contains exactly one
power of $\hbar$.  Equation (CR.6) is an exact projection of the accepted superfield result,
not an independent component-box derivation.

## 3. Color symmetry of the dotted gaugino bilinear

Use $\epsilon^{\dot1\dot2}=+1$.  Define

$$
S^{DE}
:=\widetilde\lambda_{\dot a}^D
\widetilde\lambda^{E\dot a}
=\widetilde\lambda_{\dot1}^D
\widetilde\lambda_{\dot2}^E
-\widetilde\lambda_{\dot2}^D
\widetilde\lambda_{\dot1}^E.
\tag{CR.7}
$$

Grassmann reordering gives

$$
\begin{aligned}
S^{ED}
&=\widetilde\lambda_{\dot1}^E
\widetilde\lambda_{\dot2}^D
-\widetilde\lambda_{\dot2}^E
\widetilde\lambda_{\dot1}^D\\
&=-\widetilde\lambda_{\dot2}^D
\widetilde\lambda_{\dot1}^E
+\widetilde\lambda_{\dot1}^D
\widetilde\lambda_{\dot2}^E\\
&=S^{DE}.
\end{aligned}
\tag{CR.8}
$$

Therefore any antisymmetric color coefficient $A_{DE}=-A_{ED}$ obeys

$$
A_{DE}S^{DE}
=\frac12(A_{DE}+A_{ED})S^{DE}=0.
\tag{CR.9}
$$

The former crossed word $W_{DE}-W_{ED}$ consequently gives zero.  A nonzero BC result must carry the symmetric color projection represented by $\mathbb F^{AB}{}_{DE}S^{DE}$.

## 4. Corrected evanescent tensor integral

Let $d=4-2\epsilon$, $\Delta>0$, and define

$$
I_n(\Delta)
:=\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell^2+\Delta)^n}.
\tag{CR.10}
$$

Rotational reduction in the physical (d)-subspace gives

$$
I_n(\Delta)
=\frac{4-d}{d}
\frac1{(4\pi)^{d/2}}
\frac d2
\frac{\Gamma(n-d/2-1)}{\Gamma(n)}
\Delta^{d/2+1-n}.
\tag{CR.11}
$$

Hence

$$
\lim_{\epsilon\to0}I_3(\Delta)=\frac1{32\pi^2},
\qquad
\lim_{\epsilon\to0}\Delta I_4(\Delta)=0.
\tag{CR.12}
$$

For the integral used in the former component-box memo,

$$
\begin{aligned}
J
&:=\frac1d\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2\ell^2}{(\ell^2+\Delta)^4}\\
&=\frac1d\left[I_3(\Delta)-\Delta I_4(\Delta)\right].
\end{aligned}
\tag{CR.13}
$$

Therefore

$$
\boxed{
\lim_{\epsilon\to0}J=\frac1{128\pi^2},
\qquad
\lim_{\epsilon\to0}2J=\frac1{64\pi^2}.}
\tag{CR.14}
$$

The first number is the tensor integral; the second includes the explicit factor (2) from the four-dimensional sigma/Fierz numerator.  They cannot be identified with each other.

## 5. Regulated orbit versus ordinary box

The authoritative BC census proves

$$
G_{\phi_r\widetilde\psi_s}=0,
\qquad
G_{\psi_r\widetilde\phi_s}=0.
\tag{CR.15}
$$

Thus the proposed ordinary two-Yukawa bottom parent does not exist.  The nonzero object is instead the regulated coincident Euler occurrence

$$
\widetilde\Phi_s^B
\frac{\vec\delta}{\delta\widetilde\Phi_r^A}
\longrightarrow
\delta_{rs}K_{-,\epsilon}^{AB}(z,z)
\longrightarrow
\delta_{rs}\mathbb F^{AB}{}_{DE}\langle D^D,D^E\rangle.
\tag{CR.16}
$$

The differentiation precedes the bottom projection.  Any future component realization must prove equality to (CR.16); a nonzero ordinary box cannot be substituted for it.

## 6. Noether and BRST/BV review verdicts

### 6.1 Off-shell current

The Step-5C memo left the Euler operators as placeholders and did not implement its announced B1--B4 checks.  Its parameter-stripping rule also requires the following sign pattern for the displayed Lorentzian right strip:

$$
\begin{aligned}
\partial_\mu J^\mu_{L,a}
=\operatorname{tr}_\kappa\Big\{&
-i\mathcal E_A^\nu(\sigma_{L\nu}\bar\lambda)_a
-\mathcal E_{\mathscr D}(\sigma_L^\rho\mathcal D_\rho\bar\lambda)_a\\
&+\left[(\sigma_L^{\rho\sigma})_b{}^c\epsilon_{ca}F_{\rho\sigma}
-i\epsilon_{ba}\mathscr D\right]\mathcal E_\lambda^b
-\sqrt2\mathcal E_{\phi_r}\psi_{ra}
+\sqrt2\epsilon_{ab}F_r\mathcal E_{\psi_r}^b\\
&-i\sqrt2(\sigma_L^\mu)_{a\dot a}
(\mathcal D_\mu\widetilde\phi_r)\mathcal E_{\widetilde\psi_r}^{\dot a}
+\left[i\sqrt2(\sigma_L^\mu\mathcal D_\mu\widetilde\psi_r)_a
+2(\lambda_a\times\widetilde\phi_r)\right]\mathcal E_{\widetilde F_r}\Big\}.
\end{aligned}
\tag{CR.17}
$$

Equation (CR.17) fixes only the sign strip of the memo's own proposed identity.  Because the complete Euler operators and termwise variation were absent, the off-shell Noether current remains `NOT_ACCEPTED_NOETHER_B1_B4_MISSING`.

### 6.2 Feynman rules and Lorentzian cycle

The superspace integral symbols were already defined in Step 3D.  The proposed Step-5B document supplied primitive generating words, not a complete ordered momentum-space vertex table, and its tests did not invert the odd FP kernel.  It also attempted to close the locked Lorentzian vector-cycle blocker by declaration.  These claims remain `NOT_ACCEPTED_COMPLETE_FEYNMAN_RULES` and `BLOCKED_STEP3D_LC_VECTOR_CYCLE`.

### 6.3 All-pairs sweep

The Step-5H sweep inherited the nonexistent BC ordinary parent and classified channels using a target-shaped table.  The later Step-5I comparison memo extracted the admitted target more carefully, but its structural-match claims still depended on the invalid Step-5G/5H component parents.  Both are removed.  The authoritative all-81 result is already the target-blind Schwinger-cut ledger on `origin/main`.

### 6.4 Post-merge typed heat-kernel proposal

The continuation at proposal commit `d920487` correctly starts from a Hessian two-form
$S''[v]:E\to E^\vee$ and introduces a bilinear identification $G:E\to E^\vee$.  Its
proposed even generator is nevertheless internally inconsistent.  From its displayed free
matter blocks,

$$
G_+^{-1}S''_{+-}=-\bar{\boldsymbol\nabla}^{2},
\qquad
G_-^{-1}S''_{-+}=-\boldsymbol\nabla^2,
\tag{CR.18}
$$

one obtains

$$
\left(G^{-1}S''\right)^2\Big|_{E_+}
=\bar{\boldsymbol\nabla}^{2}\boldsymbol\nabla^2
=16\Box_E\mathcal P_+,
\tag{CR.19}
$$

not $-\Box_E\mathcal P_+$.  The verifier inserts an additional factor $-1/16$, but the
memo defines $\mathcal K_{\mathrm{ev}}=\mathcal K^2$ in the matter sector and contains no
such factor.  Similarly, the displayed vector weights give

$$
G_V^{-1}S''_{VV}
=\frac2h\frac h2\Box_E
=\Box_E,
\tag{CR.20}
$$

while the claimed generator is $-\Box_E$; the verifier adds an undeclared Euclidean sign.
Moreover, applying $\mathcal K^2$ on matter/ghost rows but $\mathcal K$ on the vector row is
not a single functional calculus of $\mathcal K$ when the same proposal retains nonzero
vector--matter mixing blocks.  The finite-mode Gram-matrix model and hard-coded block-name
list do not derive nondegeneracy of the covariantly constrained field spaces or exhaustion of
the Hessian blocks.  Therefore this continuation is
`NOT_ACCEPTED_TYPED_HEAT_KERNEL_GENERATOR`; the bounded ordered-simplex/DRED lemma remains the
only accepted heat-kernel content.

### 6.5 Majorana convention proposal

The separate proposal commit `cd132a8` is internally checked on the Srednicki branch, but its
promotion of that branch to the Project convention conflicts with the locked translation policy.
The existing dictionary gives

$$
\gamma_W^\mu=-i\gamma_S^\mu,
\qquad
\Psi_{M,W}=i\Psi_{M,S},
\qquad
\bar\Psi_{M,W}=-i\bar\Psi_{M,S}.
\tag{CR.21}
$$

The proposal instead declares $\gamma_C=\gamma_S$ and $\Psi_C=\Psi_{M,S}$ and describes the
result as opposite to Weinberg in every branch-dependent choice.  This is not an index-placement
rewrite: it changes the four-component field phase and all formulas carrying an odd number of
gamma matrices.  The Project policy is to retain Weinberg quantities and phases while making
Srednicki-style upper/lower index placement explicit; no field may be silently rephased.
Consequently the ten matrix checks establish only
`VERIFIED_CONDITIONAL_SREDNICKI_DICTIONARY`.  The canonicalization, task rotation, contract
manifest entry, and paper convention note are
`NOT_ACCEPTED_MAJORANA_CANONICALIZATION_WRONG_BRANCH` and remain outside the merge surface.

### 6.6 Partial and final adversarial census proposals

The partial addendum at proposal commit `26da421` reported four completed sectors, four aborted
sectors, and twelve unadjudicated candidates.  The later proposal at commit `0983774` raises the
candidate count to seventeen and reports six completed sectors, while the ghost--Nielsen--Kallosh
sector, the zero/cut-orbit sector, and the automated three-lens refutation still did not run.  It
also defers the four physics-relevant Wick routings to a future per-routing derivation.

Its proposed completeness certificate is exact agreement with the holomorphic-twist target.  Let
$C_{\rm enum}$ denote the coefficient obtained from the emitted Project census, let
$C_{\rm HT}$ denote the translated target coefficient, and let $c_j$ denote a contribution from
an alleged omitted routing.  The observed equality

$$
C_{\rm enum}=C_{\rm HT}
\tag{CR.22}
$$

does not imply either an empty omission set or termwise vanishing:

$$
C_{\rm complete}=C_{\rm enum}+\sum_{j\in\mathcal O}c_j,
\qquad
\sum_{j\in\mathcal O}c_j=0
\centernot\Longrightarrow
\mathcal O=\varnothing
\quad\text{or}\quad
c_j=0\ \text{for every }j.
\tag{CR.23}
$$

For example, $c_1=t$ and $c_2=-t$ with $t\ne0$ leave the total unchanged.  Equation (CR.22) is
therefore a final cross-check, not a target-blind absence proof.  Nor does a self-declared
`PENDING_CLEAN_AUDIT` turn ghost/FP/NK candidates into proved typed zero rows.  If the generated
graph objects are shared templates rather than per-channel enumerations, their provenance must
be repaired before the issue can be classified as presentation-only.

The final proposal is consequently `NOT_ACCEPTED_COEFFICIENT_CENSUS_CERTIFICATE`.  Its own
seventeen candidates remain `OPEN_FINAL_CENSUS_17_CANDIDATES` until the missing sectors and the
four deferred routings are derived from the locked action without reading the target.  This does
not retract the accepted coefficient ledger, whose acceptance rests on the independent
Project-side Schwinger-cut derivation rather than either census proposal.

## 7. Final classification

- `VERIFIED`: (CR.6), the exact bottom projection of the accepted BC map.
- `VERIFIED`: (CR.8)--(CR.9), symmetry of the dotted gaugino bilinear and annihilation of antisymmetric color words.
- `VERIFIED`: (CR.12)--(CR.14), the corrected evanescent tensor integral.
- `REJECTED`: ordinary two-Yukawa box as the BC anomaly parent.
- `NOT_ACCEPTED`: independent Step-5C Noether identity, complete Step-5B Feynman rules, and the Step-5H all-pairs sweep.
- `NOT_ACCEPTED`: the post-merge typed heat-kernel generator, because (CR.18)--(CR.20)
  contradict its declared free generator and its blockwise prescription is not a single
  operator in the presence of mixing.
- `VERIFIED_CONDITIONAL`: the Majorana matrix identities on the proposal's declared Srednicki
  branch.
- `NOT_ACCEPTED`: promoting that branch to the Project convention, because (CR.21) is a
  nontrivial phase translation and the Project retains Weinberg quantities/phases.
- `OPEN`: seventeen candidates from the final adversarial census proposal; HT agreement is not
  an internal exhaustion proof, and its advertised certificate is not accepted.

The passing result is therefore a bounded audit and exact component projection; it is not a second derivation of the one-loop anomaly.
