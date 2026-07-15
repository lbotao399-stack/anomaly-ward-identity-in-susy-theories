# AB/BA G3 trace/metric and full-d SD audit

$$
D_e=r_{e,d}^2,\qquad \bar r_e^2=D_e+\mu_\ell^2,\qquad
P_D=D_0D_1D_2.
$$

$$
W_0=W_{12},\qquad W_1=W_{P0},\qquad W_2=W_{p0}=W_{01}.
$$

The kinetic cuts and zero-square currents are different occurrences:

$$
K_0=\frac{512W_0}{D_1D_2},\qquad
K_1=-\frac{512W_1}{D_0D_2},\qquad
K_2=\frac{512W_2}{D_0D_1}.
$$

$$
JE+JX=0,\qquad PE+PX=0,
$$

and the latter pair has no independent $\mu_\ell^2$ remainder.

With an unfixed trace/metric factor $\chi$,

$$
\begin{aligned}
\mathfrak O_A(\chi)
=\frac{512}{P_D}\big[&(1-\chi)D_0W_0
+(\chi-1)D_1W_1\\
&+\chi\mu_\ell^2(-W_0+W_1)\big].
\end{aligned}
$$

The two routed words are independent before integration.  At
$\mu_\ell^2=0$,

$$
1-\chi=0,\qquad \chi-1=0,
$$

so

$$
\boxed{\chi=1.}
$$

The $B$ occurrence closes independently:

$$
-512\frac{(D_2+\mu_\ell^2)W_2}{P_D}
+\frac{512W_2}{D_0D_1}
=-512\frac{\mu_\ell^2W_2}{P_D}.
$$

This cancellation is conditional on the displayed $K_2$ normalization.  Its
raw Hessian/Taylor/Wick multiplicity has not yet been derived in the same unit
as the parent trace, so $\Delta_B$ is not closed by this artifact.

The algebraic component contraction is

$$
(P_{\dot1}C_2)(P^{\dot1}C_3)
+(P_{\dot2}C_2)(P^{\dot2}C_3)
=(P_{\dot1}C_2)(P_{\dot2}C_3)
-(P_{\dot2}C_2)(P_{\dot1}C_3),
$$

With Fourier phase $e^{ipx}$,

$$
P_{\dot a}\longmapsto ip_{\dot a},\qquad
\langle C_2,C_3\rangle_{\rm Fourier}
=-(p_{\dot1}q_{\dot2}-p_{\dot2}q_{\dot1})C_2C_3.
$$

Thus raw momentum wedge to typed pairing carries factor $-1$.

$$
32768\left(\frac14\right)\left(\frac12\right)
\left(-\frac12\right)=-2048.
$$

For each simplex branch,

$$
G_{32}^{(e)}=\frac{i\sqrt2}{3}\lambda_1,qquad
G_{33}^{(e)}=-\frac{i\sqrt2}{3}\lambda_1.
$$

Conditionally at $\chi=1$, the raw-wedge coefficients are opposite to the
typed coefficients.  Therefore

$$
\boxed{G_{32}^{\rm typed}=-i\sqrt2\lambda_1,\qquad
G_{33}^{\rm typed}=+i\sqrt2\lambda_1.}
$$

The $\chi=1$ inference itself is rejected until the raw $K_e$ multiplicities
are replayed without fitting them to the SD equation.
