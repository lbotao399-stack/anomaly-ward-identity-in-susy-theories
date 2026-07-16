# AB/BA G2 external-divergence and SD exact audit

Status: `G2_R2_AND_OMEGA_SD_FULL_D_ZERO__DOTTED_EPSILON_MAPS_BPD_TO_PLUS_PAIR__PAIR_COEFFICIENT_ONE`.

No HT coefficient and no residual-$q$ equation is used.

## 1. The selected (r_2) Schwinger family

The exact raw residual is

$$
\mathcal R_{\dot0}=-128r_{0,+\dot2},
\qquad
\mathcal R_{\dot1}=+128r_{0,+\dot1}.
$$

Using

$$
\det(r_2)=-\bar r_2^2=-(D_2+\mu_\ell^2),
$$

the parent and contact are

$$
\frac{8\det(r_2)\mathcal R}{D_0D_1D_2}
=-\frac{8(D_2+\mu_\ell^2)\mathcal R}{D_0D_1D_2},
$$

$$
\frac{8\mathcal R}{D_0D_1}.
$$

Therefore

$$
\left.
\left[
-\frac{8(D_2+\mu_\ell^2)\mathcal R}{D_0D_1D_2}
+\frac{8\mathcal R}{D_0D_1}
\right]
\right|_{\mu_\ell^2=0}=0,
$$

$$
-\frac{8(D_2+\mu_\ell^2)\mathcal R}{D_0D_1D_2}
+\frac{8\mathcal R}{D_0D_1}
=-\frac{8\mu_\ell^2\mathcal R}{D_0D_1D_2}.
$$

For

$$
r_0=L+yp+z(p+q),
$$

the normalized simplex moments are

$$
2\int_0^1dy\int_0^{1-y}dz\,y
=2\int_0^1dy\int_0^{1-y}dz\,z
=\frac13,
$$

so

$$
\langle r_0\rangle_\triangle
=\frac13p+\frac13(p+q)
=\frac13(2p+q).
$$

The selected (B_1>D) word is

$$
\frac23B_1(2p+q)^{\dot a}D_{\dot a}.
$$

The transported (r_1) occurrence obeys

$$
-\frac12(D_1+\mu_\ell^2)W
+\frac12D_1W
=-\frac12\mu_\ell^2W,
$$

and contributes (-B_1q^{\dot a}D_{\dot a}).  Hence

$$
\Gamma_{G_2}^{B_1>D}
=\frac13B_1(4p-q)^{\dot a}D_{\dot a}.
$$

Here (p) is the momentum of (D), while (q) is the momentum of (B_1).  Thus

$$
(c_{\rm pair},c_{\rm EOM})
=\left(-\frac13,\frac43\right).
$$

## 2. Dotted-index divergence

The locked epsilon tensors give

$$
\epsilon^{\dot a\dot b}\epsilon_{\dot a\dot c}
=-\delta^{\dot b}_{\dot c}.
$$

Therefore

$$
(P^{\dot a}B_1)D_{\dot a}
=\epsilon^{\dot a\dot b}\epsilon_{\dot a\dot c}
(P_{\dot b}B_1)D^{\dot c}
=-\langle B_1,D\rangle.
$$

Define

$$
E_{BD}:=B_1(P^{\dot a}D_{\dot a}),
\qquad
T_{BD}:=P^{\dot a}(B_1D_{\dot a}).
$$

The exact Leibniz expansion is

$$
T_{BD}
=-\langle B_1,D\rangle+E_{BD},
$$

so

$$
E_{BD}=\langle B_1,D\rangle+T_{BD}.
$$

Consequently

$$
-\frac13\langle B_1,D\rangle
+\frac43E_{BD}
=\langle B_1,D\rangle
+\frac43T_{BD}.
$$

In the exact-divergence quotient,

$$
\boxed{c_{G_2}=1.}
$$
