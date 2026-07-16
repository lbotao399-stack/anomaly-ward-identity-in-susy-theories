# GPT Pro Gate 2S correction prompt — transported longitudinal cuts

Status: `NON_AUTHORITY_PRO_PROMPT`.

The Gate-2R response is rejected.  Do not restart the full calculation and do
not use the holomorphic-twist target.  Correct only the first broken step:
the longitudinal term was discarded when its original edge tag was obscured.

Use Project conventions

$$
\lambda_1=\frac{\hbar g^2}{16\pi^2},
\qquad
\mu_\ell^2=\bar\ell^2-\ell_d^2,
\qquad
I_{\mu^2}=\frac1{32\pi^2}.
$$

The exact operator identity is

$$
D_-D_+\bar D^2D_+
=8\bar\Box D_+-\frac12D_+\bar D^2D^2.
$$

The second term is not zero.  Transport it by superspace integration by parts
through the adjacent chiral projector and use

$$
D^2\bar D^2D^2=16\Box D^2.
$$

It may therefore acquire a new, neighboring inverse-kernel tag.  The full
$d$ Schwinger identity is imposed only after this transport.

Three exact local facts must be reproduced:

1. The twelve $G_1$ selected-edge rows give

$$
\Gamma_{G_1,A}^{\rm selected}=+\frac23\lambda_1\langle D,B_1\rangle,
\qquad
\Gamma_{G_1,B}^{\rm selected}=-\frac23\lambda_1\langle D,B_1\rangle.
$$

Your $\pm\lambda_1/12$ is smaller by exactly

$$
\frac{2/3}{1/12}=8.
$$

Locate this factor $8$ in one concrete normalization row; do not merely
replace the number.

2. In the analogous ordered-$AA$ matter second mark, the complete raw word is

$$
\mathcal S_2
=W_{01}(a_{2+}b_{1-}-a_{1-}b_{2+}).
$$

The transported longitudinal part changes the tagged-only result

$$
\mathcal R_{2,\rm tagged}=(y-z)\mu_\ell^2(p_+\wedge q_+)
$$

into

$$
\mathcal R_{2,\rm full}
=\left(z-\frac12\right)\mu_\ell^2(p_+\wedge q_+),
$$

$$
2\int_{\Sigma_2}\left(z-\frac12\right)=-\frac16,
\qquad
4\hbar g^2\left(-\frac16\right)I_{\mu^2}
=-\frac13\lambda_1.
$$

This is a diagnostic of the transport rule, not an $AB_1$ input coefficient.

3. For the $G_3$ outer-$A$ word, the exact local replay has

$$
R_A=-128W_{12},
$$

and

$$
N_{\rm full}-8\det(r_0)R_A
=1024\det(r_1)\bigl((p+q)_+\wedge r_{0,+}\bigr).
$$

Thus the longitudinal word generates a neighboring $r_1$ square.  With the
current routing,

$$
2\int_{\Sigma_2}(p+q)_+\wedge r_{0,+}
=-\frac13(p_+\wedge q_+).
$$

Determine its contact sign and endpoint normalization from the D-word; do not
infer them from a desired final coefficient.

Required response:

1. For $G_1$, $G_2$, $G_{3,2}$, and $G_{3,3}$, display every discarded
   longitudinal word, the IBP transport, the newly tagged neighboring edge,
   the matching full-$d$ cut/contact, and the remaining $\mu_\ell^2$ word.
2. Give the scalar prefactor as a product of source coefficient, action
   vertices, propagators, Berezin measures, Wick factor, external-field maps,
   and color word.  End in units of $\lambda_1$.
3. Preserve the ordered output types:

$$
G_{3,2}:\ \langle C_2^D,C_3^E\rangle,
\qquad
G_{3,3}:\ \langle C_3^D,C_2^E\rangle.
$$

4. State explicitly which Gate-2R lines fail.  Do not write a proportionality
   sign and do not quote the holomorphic-twist answer.
