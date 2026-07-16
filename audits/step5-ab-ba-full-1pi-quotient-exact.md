# AB/BA full-1PI quotient historical retraction

Status: `HISTORICAL_RETRACTION__FALSE_G3_SCALE_ONE__CORRECT_RAW_TO_COMMON_TD__FINITE_NORMAL_PRODUCT_ACCEPTED`.

This filename is retained only as a regression tombstone. It is not an accepted positive derivation.

## 1. Notation

$$
d=4-2\epsilon,
\qquad
\mu_\ell^2=\bar\ell^2-\ell_d^2=-\widehat\ell_{\rm user}^2,
\qquad
D_i=r_{i,d}^2.
$$

## 2. Exact DRED cutting failure

$$
\frac{D_e}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}=0.
$$

$$
\frac{\bar r_e^2}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}
=\frac{D_e+\mu_\ell^2}{D_0D_1D_2}-\frac{D_e}{D_0D_1D_2}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

$$
\int\frac{d^dL}{(2\pi)^d}\frac{\mu_L^2}{(L_d^2+\Delta)^3}
=\frac1{32\pi^2}.
$$

## 3. Retracted G3 normalization

Exact original/full measures give

$$
32768\left(\frac14\right)_M\left(\frac12\right)_{\bar H}
=65536\left(\frac14\right)_M\left(\frac14\right)_H
=4096.
$$

There are two correlated nonzero supertrace cycles:

$$
\frac12(C_1+C_2)=C_1,
\qquad C_2=C_1.
$$

The first false equality was

$$
\boxed{\frac12(C_1+C_2)\longrightarrow\frac12C_1},
$$

which changes

$$
4096\longrightarrow2048.
$$

Therefore

$$
\mathfrak I[1-z]=\frac23,
\qquad
\mathfrak I[z]=\frac13,
\qquad
\frac23+\frac13=1
$$

fixes only the simplex shape, not the absolute graph multiplicity. The old scale-one G3 conclusion is retracted.

## 4. Exact raw-carrier rebasing

In the basis

$$
(X_{DB},E_{DB},X_{BD},E_{BD},C_{23},C_{32}),
$$

$$
v_{\rm raw}
=\left(2,2,-\frac13,\frac43,-2i\sqrt2,2i\sqrt2\right).
$$

Using

$$
T_{DB}=X_{DB}+E_{DB},
\qquad
T_{BD}=-X_{BD}+E_{BD},
$$

$$
(2,2)_{(X,E)}=(0,2)_{(X,T)},
$$

$$
\left(-\frac13,\frac43\right)_{(X,E)}
=\left(1,\frac43\right)_{(X,T)}.
$$

Hence

$$
v_{\rm TD}=\left(0,1,-2i\sqrt2,2i\sqrt2\right).
$$

The hybrid vector

$$
\left(2,1,-2i\sqrt2,2i\sqrt2\right)
$$

mixes the G1 EOM projection with the G2 TD projection and is rejected.

## 5. Accepted finite normal product

$$
\delta_{\rm fin}
=\left(1,0,i\sqrt2,-i\sqrt2\right),
$$

$$
v_{\rm ren}
=v_{\rm TD}+\delta_{\rm fin}
=\left(1,1,-i\sqrt2,i\sqrt2\right).
$$

For

$$
M_q=
\begin{pmatrix}
1&-1&0&0\\
i\sqrt2&0&1&0\\
-i\sqrt2&0&0&1
\end{pmatrix},
$$

$$
M_qv_{\rm ren}=0.
$$

The finite term is a composite-source normal-product scheme term, not an additional anomaly graph.

## 6. Bound evidence

- `audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json`: `d8c7763353f79593ec5411d734e309edcce337592d6c0e8829d9a2709d99a17f`
- `audits/step5-ab-ba-project-ward-finite-renormalization-exact.json`: `ce8f2e2daf7dfe8571030ee3f3d207e68f7ade5f485cca51abe55989793cc8a1`
- finite Project seal: `bdeffbb34da6a8191df264769d48a50e725dfad11b97fad0f4c8cd0b15ae8547`

No holomorphic-twist artifact and no Project result engine enters this retraction derivation.

Checks: `55/55` exact PASS.
