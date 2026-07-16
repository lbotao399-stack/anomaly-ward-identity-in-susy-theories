# AB/BA G3 full resolvent census and original-measure audit

Status: `PASS_FULL_RESOLVENT_CENSUS__NO_MISSING_1PI_C2C3_FAMILY__G3_SCALE_TWO_REMAINS`.

## 1. Resolvent

$$
\Gamma_{g^2}
=I_2-I_1S_3-I_0S_4+\frac12I_0S_3S_3.
$$

The bare source supports are

$$
I_0=(u,\phi_1),\qquad
I_1=(u,u,\phi_1),\qquad
I_2=(u,u,u,\phi_1).
$$

For external $(C_2,C_3)=(\widetilde\phi_2,\widetilde\phi_3)$, exact port
matching gives

$$
N^{\rm 1PI}_{I_2}=0,qquad
N^{\rm 1PI}_{I_1S_3}=0,qquad
N^{\rm 1PI}_{I_0S_4}=0.
$$

At $I_0S_3S_3$, the only one-loop 1PI rows are

$$
(M_2,H_-),\qquad (M_3,H_-).
$$

The possible $(M_1,H_-)$ rows put both external fields at $H_-$ and leave an
articulation edge; they are 1PR external-leg attachments.

## 2. Original measure

For the canonical monomials,

$$
\int d^4\theta_M\,\theta_M^+\theta_M^-\bar\theta_M^{\dot+}\bar\theta_M^{\dot-}
=\frac14,
$$

$$
\int d^2\bar\theta_H\,
\bar\theta_H^{\dot+}\bar\theta_H^{\dot-}
=\frac12.
$$

Thus the direct original measure carries

$$
\frac14\frac12=\frac18.
$$

Evaluating the complete projectors directly gives

$$
F_A^{d^4\theta_Md^2\bar\theta_H}
=4F_A^{d^4\theta_Md^4\theta_H},
$$

$$
F_B^{d^4\theta_Md^2\bar\theta_H}
=4F_B^{d^4\theta_Md^4\theta_H}.
$$

The sign relative to the transported representation is the endpoint-transfer
sign; the magnitude is exactly the locked omitted-endpoint factor $4$.  No
factor $1/2$ occurs.

## 3. Parent--cut rows

$$
\frac{-4096(D_0+\mu^2)W_0}{D_0D_1D_2}
+\frac{4096W_0}{D_1D_2}
=-\frac{4096\mu^2W_0}{D_0D_1D_2},
$$

$$
\frac{4096(D_1+\mu^2)W_1}{D_0D_1D_2}
-\frac{4096W_1}{D_0D_2}
=\frac{4096\mu^2W_1}{D_0D_1D_2},
$$

$$
\frac{-4096(D_2+\mu^2)W_2}{D_0D_1D_2}
+\frac{4096W_2}{D_0D_1}
=-\frac{4096\mu^2W_2}{D_0D_1D_2}.
$$

At $\mu^2=0$, every row is zero.

The nonlinear rows are

$$
JE+JX=512W_0-512W_0=0,
$$

$$
PE+PX=-128W_2+128W_2=0.
$$

They contain no independent loop inverse square and no $\mu^2$ remainder.

## 4. Normalization

$$
w_0=w_1=w_2=\frac13,qquad w_0+w_1+w_2=1.
$$

For each edge,

$$
c_{32,e}=\frac23i\sqrt2.
$$

Therefore

$$
c_{32}^{\rm raw}=3\frac23i\sqrt2=2i\sqrt2,
$$

and the locked Fourier map gives

$$
\boxed{
c_{32}^{\rm typed}=-2i\sqrt2,qquad
c_{33}^{\rm typed}=+2i\sqrt2.}
$$

The full bare-source 1PI resolvent supplies no additional
$-i\sqrt2$ correction.
