# GPT Pro Gate 2W — corrected chiral index, complete AA gauge orbit, exact normalization

Gate 2V used the wrong undotted action-vertex index. Recompute from the corrected local D-algebra below. Do not invoke the holomorphic-twist target.

The cubic Hessian contains

$$
W^\gamma D_\gamma.
$$

For an external lower-index $W_+$,

$$
W^-=\epsilon^{-+}W_+=-W_+,
$$

so the action derivative is $-D_-$, not $D_+$. The old checker fixed $D_+$ at both chiral action endpoints and therefore produced the false traceless word

$$
(b_0+b_1)(a_0b_2-b_0a_2).
$$

Use

$$
r_i=\begin{pmatrix}a_i&b_i\\c_i&d_i\end{pmatrix},
\qquad
W_{02}=a_0b_2-b_0a_2,
\qquad
\det r_i=a_id_i-b_ic_i=-\bar r_i^2.
$$

Split the marked source word exactly as

$$
D_-A_1=\mathcal S_e+\mathcal L_e,
\qquad
\mathcal S_e=\sqrt2\,\bar r_e^2D_+u,
\qquad
\mathcal L_e=\frac{\sqrt2}{16}D_+\bar D^2D^2u.
$$

The corrected sparse-Grassmann rows are

$$
\mathcal G_{01,\mathcal S}
=
(-b_2\det r_0,+b_2\det r_0,+b_2\det r_0,+b_2\det r_0),
$$

$$
\sum_j\mathcal G_{01,\mathcal S}^{(j)}
=2b_2\det r_0=-2b_2\bar r_0^2,
$$

$$
\mathcal G_{02,\mathcal S}
=
(+b_0\det r_2,-b_0\det r_2,+b_0\det r_2,+b_0\det r_2),
$$

$$
\sum_j\mathcal G_{02,\mathcal S}^{(j)}
=2b_0\det r_2=-2b_0\bar r_2^2.
$$

The longitudinal sums are

$$
\sum_j\mathcal G_{01,\mathcal L}^{(j)}=-2d_0W_{02},
\qquad
\sum_j\mathcal G_{02,\mathcal L}^{(j)}=0.
$$

Every one of the eight rows obeys

$$
\mathcal G_{\rm full}^{(j)}
=\mathcal G_{\mathcal S}^{(j)}+\mathcal G_{\mathcal L}^{(j)}.
$$

The old $D_+$ control has selected-square part exactly zero row by row. Thus Gate 2V's four abstract copies of `selected_square=-4` are rejected: the nonzero squares arise only after the correct $-D_-$ action endpoint and are the displayed $r_0^2,r_2^2$ determinants.

For each corrected row print:

1. the raw $-D_-$ endpoint word;
2. its selected inverse-kernel edge $r_0$ or $r_2$;
3. its exact scalar coefficient of $\bar r_e^2$;
4. the full-$d$ Schwinger identity

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}=0;
$$

5. the sole DRED remainder

$$
\frac{\bar r_e^2-r_{e,d}^2}{D_0D_1D_2}
=\frac{\mu_\ell^2}{D_0D_1D_2};
$$

6. every longitudinal, transported-edge, link, and source/contact term required for the complete Schwinger orbit. Do not discard a term by an untagged four-dimensional trace. Do not introduce an extra factor $4-d$.

Then resolve the remaining factor-eight conflict from first principles. The project locks

$$
h=g^{-2}.
$$

Derive the gauge-fixed quadratic vector action and the relevant cubic $VVV$ action in the original field $V$, including all numerical coefficients, $1/n!$, ordered-vertex multiplicities, propagator inverse, source Hessian factors, and closed Grassmann-loop factor. Perform the field changes independently:

$$
u=\frac{V}{\sqrt2g},
\qquad
v=\frac{V}{2g}=\frac{u}{\sqrt2}.
$$

Print the exact $\langle uu\rangle$, $\langle vv\rangle$, cubic vertices, and show field-redefinition invariance of the final graph. One current branch assumes

$$
\langle uu\rangle=-\frac{\hbar}{p^2}
$$

and obtains $(c_{DA},c_{AD})=(1/8,-1/8)$. The independently locked WW triangle-plus-contact pole arithmetic gives one physical anomaly unit

$$
\frac{\hbar g^2}{16\pi^2}
$$

from

$$
\Gamma_T=+\frac{\hbar g^2}{32\pi^2\epsilon}\widehat\delta^{mn}T_{m\rho n}p^\rho,
\qquad
\Gamma_C=-\frac{\hbar g^2}{32\pi^2\epsilon}\delta_4^{mn}T_{m\rho n}p^\rho,
$$

$$
p^\rho\breve\delta^{mn}\sigma_m\bar\sigma_\rho\sigma_n
=-2\epsilon\,p\!\cdot\!\sigma.
$$

Do not select either normalization by this desired unit. Locate the earliest exact wrong coefficient in the $(1/8,-1/8)$ derivation or prove that an explicit same-order completion supplies the missing factor.

End with the fully gauge-fixed, target-blind ordered vector

$$
(c_{DA},c_{AD}),
$$

and a finite list of all nonzero AA one-loop 1PI parent/contact rows. Do not stop at an undefined gauge branch.
