# Step 5 ordered AA gauge first D-algebra error

Status: `AA_GAUGE_WRONG_CHIRAL_INDEX_PROVED__FULL_EDGE_ORBIT_PENDING`.

No holomorphic-twist or Project result coefficient enters this audit.

The cubic Hessian contains

$$
W^\gamma D_\gamma.
$$

For the external lower-index field $W_+$,

$$
W^-=\epsilon^{-+}W_+=-W_+.
$$

Hence the selected action derivative is

$$
\boxed{W^\gamma D_\gamma\big|_{W_+}=-W_+D_-.}
$$

The former checker instead used $D_+$.  It therefore contracted the same
undotted momentum row at both chiral endpoints and obtained the false control
word

$$
(b_0+b_1)(a_0b_2-b_0a_2),
$$

whose four-dimensional metric trace vanishes.

Write

$$
D_-A_1
=\sqrt2\,\bar r_e^2D_+u
+\frac{\sqrt2}{16}D_+\bar D^2D^2u
=:\mathcal S_e+\mathcal L_e.
$$

For

$$
r_i=
\begin{pmatrix}
a_i&b_i\\
c_i&d_i
\end{pmatrix},
\qquad
W_{02}:=a_0b_2-b_0a_2,
$$

the corrected $-D_-$ endpoint replay gives

$$
\begin{aligned}
\mathcal G_{01,\mathcal S}
={}&
\bigl(
-b_2\det r_0,
+b_2\det r_0,
+b_2\det r_0,
+b_2\det r_0
\bigr),\\
\mathcal G_{02,\mathcal S}
={}&
\bigl(
+b_0\det r_2,
-b_0\det r_2,
+b_0\det r_2,
+b_0\det r_2
\bigr).
\end{aligned}
$$

Thus

$$
\boxed{
\sum_j\mathcal G_{01,\mathcal S}^{(j)}
=2b_2\det r_0
=-2b_2\bar r_0^2,}
$$

$$
\boxed{
\sum_j\mathcal G_{02,\mathcal S}^{(j)}
=2b_0\det r_2
=-2b_0\bar r_2^2.}
$$

The longitudinal sums are

$$
\sum_j\mathcal G_{01,\mathcal L}^{(j)}
=-2d_0W_{02},
\qquad
\sum_j\mathcal G_{02,\mathcal L}^{(j)}=0,
$$

and all eight rows satisfy

$$
\mathcal G_{\rm full}
=\mathcal G_{\mathcal S}+\mathcal G_{\mathcal L}.
$$

Therefore the former statement

$$
\mathcal G_{\mathcal S}=0
$$

is rejected.  The selected inverse-kernel squares are $r_0$ and $r_2$,
respectively.  Each must be paired with its own full-dimensional Schwinger
contact:

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad e=0,2.
$$

Verification:

```text
python scripts/step5_aa_gauge_longitudinal_first_error_exact_audit.py
```
