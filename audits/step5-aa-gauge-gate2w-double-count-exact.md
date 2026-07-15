# Step 5 AA gauge Gate-2W double-count audit

Status: `GATE2W_SECTION8_REJECTED__FINAL_SPARSE_ROW_RECOUNTED_BY_MINUS_FOUR`.

No external target enters this audit.

The exact sparse-Grassmann rows are coefficients of the complete words

$$
\mathcal S_0\mathbb K\mathbb B_i\mathbb C_j\Delta_\theta,
\qquad
\mathbb K\mathcal S_2\mathbb B_i\mathbb C_j\Delta_\theta,
$$

after all $D$, $\bar D$, and Berezin operations.  They are

$$
(-1,+1,+1,+1)b_2\det r_0,
$$

$$
(+1,-1,+1,+1)b_0\det r_2.
$$

Therefore

$$
f_{01}=2b_2\det r_0,
\qquad
f_{02}=2b_0\det r_2.
$$

The marked-unmarked source scalar already contained in each $f$ is

$$
s=\sqrt2\left(-\frac1{4\sqrt2}\right)=-\frac14.
$$

Consequently the remaining endpoint differential factor encoded by the exact sparse result is

$$
E_{\rm exact}=\frac{2}{-1/4}=-8,
$$

and the source-included final coefficient is

$$
sE_{\rm exact}=\left(-\frac14\right)(-8)=2.
$$

Gate 2W Section 8 instead takes the already integrated row sum $2$ as a new bare endpoint multiplicity and forms

$$
w_D^{2W}=s(16)(2)
=\left(-\frac14\right)(16)(2)
=-8.
$$

This differs from the exact source-included row coefficient by

$$
\boxed{
\frac{w_D^{2W}}{sE_{\rm exact}}
=\frac{-8}{2}
=-4.}
$$

Thus the factor $16$ and final row sum $2$ cannot both be multiplied after the sparse row has been evaluated.

The two action vertices and three propagators, with no source $D$-word included, give

$$
w_{\rm vp}
=\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3
=-\frac{\hbar g^2}{16}.
$$

For the first determinant-basis row, the exact local product is

$$
w_{\rm vp}f_{01}
=-\frac{\hbar g^2}{8}b_2\det r_0,
$$

not

$$
\frac{\hbar g^2}{2}b_2\det r_0.
$$

After the edgewise full-$d$ subtraction,

$$
f_{01}^{\rm anom}=-2(r_2)_{+\dot-}\mu_\ell^2,
\qquad
f_{02}^{\rm anom}=-2(r_0)_{+\dot-}\mu_\ell^2.
$$

Use the Gate-2W outgoing routing

$$
r_0=\ell,
\qquad
r_1=\ell+q,
\qquad
r_2=\ell+p+q,
\qquad
P=p+q.
$$

With

$$
L=\ell+yq+zP,
$$

the exact normalized simplex moments are

$$
2\int_{\Sigma_2}r_0
=-\frac{p+2q}{3},
$$

$$
2\int_{\Sigma_2}r_2
=\frac{2p+q}{3}.
$$

Hence

$$
2\int_{\Sigma_2}f_{01}^{\rm anom}
=-\frac{4p+2q}{3}_{+\dot-}\mu_\ell^2,
$$

$$
2\int_{\Sigma_2}f_{02}^{\rm anom}
=+\frac{2p+4q}{3}_{+\dot-}\mu_\ell^2.
$$

The post-cut numerator is a rank-one momentum moment multiplying $\mu_\ell^2$.  Gate 2W Section 10 replaces it by a rank-two pole word $L_1^mL_2^n$ without an operator equality.  The polynomial degrees after extracting $\mu_\ell^2$ are respectively

$$
1\ne2.
$$

Therefore the Gate-2W final vector is not derived.  A complete result still requires the external-component normalization, typed removal or retention of the $q$ contraction, and a rowwise longitudinal/contact transport map.
