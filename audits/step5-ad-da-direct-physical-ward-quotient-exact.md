# Step 5 AD/DA DD-port artifact rejection

Status: `REJECTED_WRONG_EXTERNAL_VERTEX_TYPE`.

External target used: `false`.

## 1. Wrong parent

Former v1 computed

$$
S_g^-\big|_{D}\times S_g^-\big|_{D}.
$$

The generated physical graph IR fixes

$$
V_{\widetilde W}\big|_{S_g^-,D}
\times
V_W\big|_{S_g^+,A},
\qquad
\frac1{2!}(1+1)=1.
$$

Therefore the former DD TGG vector, conversions (-16,-8), O05/O06
standalone-zero inference, and compact AD/DA coefficients are rejected.

An affine contact is not an anomaly-zero criterion:

$$
\frac{\bar r_e^2R_e}{D_0D_1D_2}
-\frac{R_e}{P_{\widehat e}}
=\frac{\mu_\ell^2R_e}{D_0D_1D_2},
\qquad
\bar r_e^2=r_{e,d}^2+\mu_\ell^2.
$$

## 2. Surviving source normalization

$$
O_{AD}^{AB}=N_0^A D_1^B,
\qquad
N_0^A=\frac{\sqrt2}2,
\qquad
D_1^B=\frac{i\sqrt2}4,
\qquad
N_0^AD_1^B=\frac i4,
$$

$$
O_{DA}^{AB}=-D_1^A N_0^B,
\qquad
D_1^A=-\frac{\sqrt2}4,
\qquad
N_0^B=\frac{\sqrt2}2,
\qquad
-D_1^AN_0^B=\frac14.
$$

$$
1!\,1!=1.
$$

Only this direct ordered source Hessian remains valid.

## 3. Physical coefficient

$$
\Gamma_{AD}^{\rm anom}=\mathrm{OPEN},
\qquad
\Gamma_{DA}^{\rm anom}=\mathrm{OPEN}.
$$

Machine diagnostic checks retained under `rejected_DD_diagnostic`:

$$
N_{\rm pass}=82,\qquad
N_{\rm fail}=0.
$$
