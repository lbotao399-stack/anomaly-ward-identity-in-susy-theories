# GPT Pro Gate-AC/CA: complete regulated one-loop orbit

Compute the ordered $A>C_r$ and $C_r>A$ one-loop anomaly sectors by a target-blind superspace Feynman calculation.  Do not use the holomorphic-twist coefficient to choose a normalization.

## Definitions

$$
A_c=A_1+gA_2+g^2A_3,
\qquad
C_r=\widetilde\Phi_r,
$$

$$
I_{AC}=\nabla_-(A_c^A C_r^B),
\qquad
I_{CA}=\nabla_-(C_r^A A_c^B).
$$

Because $\nabla_-C_r=0$, the outer derivative marks only $A_c$, but every nonlinear occurrence in $A_2,A_3$ and $\Gamma_-=g\gamma_1+g^2\gamma_2$ must be retained.

The complete order-$g^2$ resolvent is

$$
\Gamma_{g^2}^{(1)}
=\langle I_2\rangle_0
-\hbar^{-1}\langle I_1S_3\rangle_{0,c}
-\hbar^{-1}\langle I_0S_4\rangle_{0,c}
+(2\hbar^2)^{-1}\langle I_0S_3S_3\rangle_{0,c}.
$$

Include matter, gauge, superpotential, collapsed inverse kernels, nonlinear-source bubbles, seagulls, EOM Jacobians, gauge-fixing, FP/NK, and auxiliary rows whenever typed ports permit them.  Prove every omitted sector by its ports and its regulated word.

## Locked DRED mechanism

$$
d=4-2\epsilon,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2.
$$

For each selected edge $e$ separately,

$$
\frac{r_{e,d}^2R_e}{D_0D_1D_2}
-\frac{R_e}{\prod_{j\ne e}D_j}=0,
$$

$$
\frac{\bar r_e^2R_e}{D_0D_1D_2}
-\frac{R_e}{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2R_e}{D_0D_1D_2},
$$

$$
\int_\ell^{\rm DRED}\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

No extra graph-specific $(4-d)$ may be inserted.

## Existing target-blind linear-source replay to adjudicate

For each ordered direction the port census contains

$$
N_{TGM}=6,
\qquad
N_{TMM}=1,
\qquad
N_{TMH}=2.
$$

The two $TMH$ raw projected words vanish.  The current replay gives

$$
\Gamma_{A>C_r}^{\rm linear}
=2\lambda_1\mathbb F^{AB}{}_{DE}
\left[
(P_{\dot a}C_r)^D D^{E\dot a}
-D_{\dot a}^D(P^{\dot a}C_r)^E
\right],
$$

$$
\Gamma_{C_r>A}^{\rm linear}
=2\lambda_1\mathbb F^{AB}{}_{DE}
\left[
D_{\dot a}^D(P^{\dot a}C_r)^E
-(P_{\dot a}C_r)^D D^{E\dot a}
\right].
$$

The $TMM$ $A>C_r$ four-dimensional numerator was recorded as

$$
\mathcal F_{A>C}^{(4)}
=8(\det r_0)\mathcal R_0-8(\det r_1)\mathcal J_1,
$$

$$
\mathcal R_0=-128\,\mathfrak b(r_1),
\qquad
\mathcal J_1=-128\,\mathfrak b(r_0),
$$

giving

$$
\mathcal F_{A>C}^{\rm DRED}+\mathcal C_0^{(d)}+\mathcal C_1^{(d)}
=8\mu_\ell^2(\mathcal J_1-\mathcal R_0)
=-1024\mu_\ell^2\mathfrak b(p).
$$

The $C_r>A$ replay analogously gives a $q$ carrier.  Its canonical pre-$D$ factor was

$$
\left(-\frac1{4\sqrt2}\right)
\left(\frac{\sqrt2g}{\hbar}\right)^2
\left[-\hbar\left(\frac\hbar{16}\right)^2\right]
=\frac{\sqrt2\hbar g^2}{1024}.
$$

The conditional holomorphic-twist comparison, read only after this calculation, has the same tensors with unit rather than factor two.  Hence the existing linear replay differs by an exact factor $-2$ in the displayed ordered basis.

## Outer-$A$ current orbit

The covariant identity contains two apparently opposite rows,

$$
-\nabla_+\mathscr E_V
\supset +2i(B_s\times C_s),
$$

and the explicit term

$$
-2i(B_s\times C_s).
$$

The old calculation cancels them before integration because the displayed four-dimensional current words agree.  This is admissible only if both occurrences have the same ordered color word, source sign, denominator multiset, selected inverse edge, full-$d$ Schwinger contact, and regulator routing.  Otherwise retain their $\mu_\ell^2$ difference.

Local exploratory evidence is:

$$
K_{\dot1}=64(k_0-ik_1)
$$

for one explicit current bubble; connected $A_2$--$M_1$ and $A_1$--$M_2$ bubbles are affine in the loop momentum; the tested $A_3$ tadpole is zero in an $SU(2)$ frame.  These are diagnostics, not accepted coefficients.

## Required output

For every occurrence give

$$
(\text{id},\text{ordered source term},\text{field loop},\text{ports},
\text{vertex/Wick/Koszul factor},\text{raw D-word},r_e,
\bar r_e^2, r_{e,d}^2,\mu_\ell^2\text{ remainder},
\text{simplex moment},\text{normalized output}).
$$

Apply every vertex spinor derivative to the complete product by the Leibniz rule before assigning it to a single propagator.  In particular retain terms where a derivative acts on a nonzero-momentum external probe.

Decide the first invalid line in the factor-two replay.  Determine whether the complete nonlinear/contact orbit adds $(-1,+1)$, $(-3,+3)$, zero, or another exact vector; do not select among these by the target.  End with independent Project vectors for $A>C_r$ and $C_r>A$, then compare with the conditional target.
