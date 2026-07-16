# AB/BA G1 and G3 raw multiplicity and transverse trace

Status: `PASS_AB_BA_G1_G3_RAW_MULTIPLICITY_ONE__NO_EXTRA_TRANSVERSE_HALF__CURRENT_MAGNITUDES_RETAINED`.

## 1. Mixed source Hessian

Let $I_{u\phi}$ and $I_{\phi u}$ be the two mixed Hessian blocks.  The two
closed traces differ only by the starting point:

$$
T_{u\phi}=T_{\phi u}=T.
$$

Therefore

$$
\frac12\operatorname{STr}\bigl[C(I_{u\phi}+I_{\phi u})\bigr]
=\frac12(T+T)=T.
$$

One retained directed representative has weight $1$, not $1/2$.

## 2. Transverse rank extraction

For $N=c\bar L^2W$,

$$
T_\perp=2cW.
$$

The two equivalent calculations are

$$
-\frac12T_\perp=-cW,
$$

$$
c=\frac{T_\perp}{2W},
\qquad
\mathcal R_{\rm DRED}=-cW.
$$

The mixed prescription

$$
-\frac12\left(\frac{T_\perp}{2W}\right)W=-\frac12cW
$$

applies the rank half twice and is rejected.

## 3. G1

The primitive multiplicity is

$$
\left[\frac12(2)_{\rm cyclic\ source}\right]
\left[\frac1{2!}(2)_{S_gS_m\ {
m orders}}\right]
\left[\frac1{3!}(6)_{VVV\ {
m labels}}\right]
\left[\frac1{3!}(6)_{u\phi\widetilde\phi}\right]
(1)_{\rm Wick}=1.
$$

$QL$ and $LQ$ are two algebraic summands of the polarized gauge Hessian;
they are not an additional graph factor.

The two product-rule marks are distinct parent occurrences:

$$
A:\ e_2,\qquad B:\ e_0.
$$

The exact generic $(p_B,q_D)$ rows are

$$
A=\left(\frac43,\frac23\right),
\qquad
B=\left(\frac23,\frac43\right),
$$

$$
\boxed{G_1=(2,2).}
$$

## 4. G3

The primitive multiplicity is

$$
\left[\frac12(2)_{\rm cyclic\ source}\right]
\left[\frac1{2!}(2)_{MH\ {
m orders}}\right]
\left[\frac1{3!}(6)_{H_-\ {
m Hessian}}\right]
(1)_{\rm Wick}=1.
$$

At $y=z=0$, one exact nonzero original-measure monomial is

$$
-32768-32768i.
$$

The exact two-axis trace and external wedge are

$$
T_\perp=-65536i,
\qquad W=-i,
\qquad
c=\frac{T_\perp}{2W}=32768.
$$

Thus

$$
c_{\rm measure}=32768\left(\frac14\right)\left(\frac12\right)=4096,
$$

$$
-\frac12T_{\perp,{\rm measure}}
=-4096W.
$$

Equivalently, after recovering $c_{\rm measure}=4096$, the DRED word is
$-c_{\rm measure}W$; no further $1/2$ is allowed.

The three parent--cut rows are

$$
-\frac{4096(D_0+\mu_\ell^2)W_0}{P_3}
+\frac{4096W_0}{D_1D_2}
=-\frac{4096\mu_\ell^2W_0}{P_3},
$$

$$
+\frac{4096(D_1+\mu_\ell^2)W_1}{P_3}
-\frac{4096W_1}{D_0D_2}
=+\frac{4096\mu_\ell^2W_1}{P_3},
$$

$$
-\frac{4096(D_2+\mu_\ell^2)W_2}{P_3}
+\frac{4096W_2}{D_0D_1}
=-\frac{4096\mu_\ell^2W_2}{P_3}.
$$

The raw-wedge coefficients are

$$
G_{32}^{\rm raw}=+2i\sqrt2,
\qquad
G_{33}^{\rm raw}=-2i\sqrt2.
$$

With the locked Fourier map, the typed coefficients are

$$
\boxed{
G_{32}^{C_2>C_3}=-2i\sqrt2,
\qquad
G_{33}^{C_3>C_2}=+2i\sqrt2.}
$$

$$
N_{\rm pass}=76,
\qquad
N_{\rm fail}=0.
$$
