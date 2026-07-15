# Step 5 AD/DA raw Schwinger contact Hessian multiplicity

Status: `PASS_RAW_LOCAL_CONTACT_MULTIPLICITY_ONE__FINITE_W_LINK_LONGITUDINAL_ZERO`.

## 1. Local contact

$$
K_{AB}=-\kappa_{AB}r_e^2,
\qquad \kappa_{AB}=\frac12\delta_{AB},
\qquad r_e^2P^A=-2P^AK_A.
$$

The parent quotient and independently generated Schwinger contact carry

$$
c_{\rm parent}=(-2)^3=-8,
$$

$$
c_{\rm contact}
=(-1)_{\rm SD}(-2)_{r^2P=-2PK}(-2)^2_{\rm uncut}=+8.
$$

For every AD/DA, direct/crossed, and chirality row,

$$
N_d+K_{\rm raw}=0.
$$

The exact multiplicity is

$$
\left(\frac1{2!}\times2_{\rm action\ order}\right)
\left(\frac1{2!}\times2_{\rm cut\ endpoint}\right)
\left(\frac1{2!}\times2_{\rm remaining\ Wick}\right)=1.
$$

Thus

$$
m_{\rm contact}=1.
$$

## 2. Finite-w one-link row

$$
a_m^{L,(1)}[u]
=\frac{i\sqrt2}8(\bar\sigma_m)^{\dot ba}
[D_a,\bar D_{\dot b}]_{\rm ord}u^L\Big|,
$$

$$
(\mathbb M_1[u])^B{}_C
=w^mc_{LC}{}^Ba_m^{L,(1)}[u].
$$

Writing $x=iw\cdot r$ and $y=iw\cdot r'$, the functional derivative of
$T_1$ has unit Duhamel coefficient and phase

$$
\int_0^1ds\,e^{sx+(1-s)y}.
$$

Therefore

$$
(x-y)\int_0^1ds\,e^{sx+(1-s)y}
=e^x-e^y,
$$

and every endpoint plus one-link row is

$$
C_{\omega,e}(e^x-e^y)
-C_{\omega,e}(e^x-e^y)=0.
$$

This cancellation holds before loop integration in arbitrary $d$; its
$\mu_\ell^2$ anomaly sector is zero.

$$
N_{\rm pass}=255,\qquad
N_{\rm fail}=0.
$$
