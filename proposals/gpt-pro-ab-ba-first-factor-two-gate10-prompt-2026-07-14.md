# Gate 10: AB/BA 唯一 residual 的 first-error localization

We have now closed G2 exactly and rejected several claims in Gate 9. Do not infer any coefficient from the holomorphic-twist target or from residual-q covariance. We need a standard raw one-loop Feynman/supergraph computation, occurrence by occurrence.

## Locked DRED rule

For every selected edge (e),

$$
\frac{\bar r_e^2}{D_0D_1D_2}-\frac{1}{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\int\frac{d^d\ell}{(2\pi)^d}\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

Replacing (\bar r_e^2) by (r_{e,d}^2) makes each parent plus induced Schwinger contact identically zero.

## What is already exact

### G2

The executable raw route is

$$
r_0-r_1=p,\qquad r_1-r_2=q,
$$

with (D=D(p)) at the M endpoint and (B_1=B_1(q)) at H. The selected (r_2) family and transported (r_1\)-Omega family give

$$
(c_{p},c_q)=\left(\frac43,-\frac13\right),
$$

and the typed basis is

$$
(c_{\langle B,D\rangle},c_{E_{BD}})
=\left(-\frac13,\frac43\right).
$$

With the repository tensors

$$
\epsilon^{\dot a\dot b}\epsilon_{\dot a\dot c}
=-\delta^{\dot b}_{\dot c},
$$

we have

$$
T_{BD}:=P^{\dot a}(B_1D_{\dot a})
=-\langle B_1,D\rangle+E_{BD},
$$

so modulo the exact divergence (T_{BD}),

$$
-\frac13\langle B_1,D\rangle+\frac43E_{BD}
=\langle B_1,D\rangle+\frac43T_{BD}.
$$

Thus (c_{G2}=1). This is 47/47 exact and target-blind. There is no momentum-carrier swap and no (q_{word}=-q_{physical}) replacement.

### Source/action multiplicity

For fixed ordered (I_0^{AB}=C_{AB}u^A\phi_1^B),

$$
\frac12\operatorname{Tr}(I''K)
=\frac12(A+A)=A.
$$

Equivalently,

$$
\frac1{2!}(S_XS_Y+S_YS_X)=S_XS_Y.
$$

For G1 and G3, the two action vertices and the internal species/roles are distinguishable, the fixed-color/flavor Wick matching is unique, and (operatorname{Aut}(G)=1). For G2, the two M1 labelings cancel (1/2!). Hence a selective G1/G3 symmetry factor (1/2) is forbidden.

### Current raw outputs

The G1 24 VVV words, their two product-rule source marks, and edgewise induced contacts give

$$
A:\left(\frac43,\frac23\right),\qquad
B:\left(\frac23,\frac43\right),\qquad
G1_{raw}=2(p+q).
$$

Do not set (p+q=0): the source insertion carries (s=-(p+q)).

The G3 original raw trace at (y=z=0) is

$$
T_\perp=-65536i,qquad p_+\wedge q_+=-i,
$$

so

$$
c=\frac{T_\perp}{2(p_+\wedge q_+)}=32768.
$$

The original Berezin measures give

$$
32768\left(\frac14\right)\left(\frac12\right)=4096.
$$

The two equivalent DRED routes are

$$
-\frac12T_\perp=-c(p_+\wedge q_+),
$$

and applying another (1/2) after extracting (c) is double-halving. The edgewise parents/cuts are

$$
P_0=-4096(D_0+\mu^2)W_0,\quad K_0=+4096D_0W_0,
$$

$$
P_1=+4096(D_1+\mu^2)W_1,\quad K_1=-4096D_1W_1,
$$

$$
P_2=-4096(D_2+\mu^2)W_2,\quad K_2=+4096D_2W_2.
$$

Each full-d sum is zero. The DRED result presently is

$$
c_{G32}=-2i\sqrt2,\qquad c_{G33}=+2i\sqrt2.
$$

The current target-blind vector is therefore

$$
(G1,G2,G32,G33)=(2,1,-2i\sqrt2,+2i\sqrt2).
$$

Only the first component violates residual-q covariance; the G1 and G3 raw channels share scale 2, while the corrected G2 is scale 1.

## Required calculation

1. Recompute G1 from its own 24 VVV D-words and two source-product-rule marks. Do not reflect G2 into G1. Track source momentum (s=-(p+q)), output-component maps, ordered odd-field signs, and every factorial/Wick multiplicity. Identify whether one mark is a transported/contact presentation of the other, or prove they are distinct. Write every parent square and its induced cut.

2. Recompute G3 directly in the original (d^4\theta_M d^2\bar\theta_H) measure. Reconcile exactly these two normalizations:

$$
T_\perp=-65536i\to c=32768\to c_{G3}=2,
$$

versus the alternative normalized replay

$$
T_\perp/32768=-2i\to c_{metric}=1.
$$

State what the divisor (32768) physically contains. Compare it term-by-term with the explicit measure factor (1/8), the primitive pre-D coefficient, the component output map, the (\Gamma(3)=2) Feynman prefactor, and the finite master. Locate the first equality where one route duplicates or omits a factor 2.

3. If an omitted triangle/contact supplies the correction, name its exact source/action Hessian, external ports, ordered Wick pairing, selected edge, parent numerator, induced full-d cut, and finite (\mu^2) remainder. A covariance argument or a target-derived counterterm is not accepted.

4. Return a target-blind final AB and BA vector only after all four entries arise from raw parent-minus-cut families and every full-d family is pointwise zero.

Do not stop at a proposal. Give a complete calculation and explicitly identify the earliest incorrect equality in Gate 9 and in the current local factor-two route.
