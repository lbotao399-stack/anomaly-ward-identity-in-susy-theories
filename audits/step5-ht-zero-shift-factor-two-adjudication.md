# Step 5 HT zero-shift factor-two adjudication

Status: `SOURCE_INTERNAL_FACTOR_TWO_PROVED__PROJECT_FEYNMAN_AND_COMPONENT_BRANCH_SELECTED`.

No Project letter-family coefficient is used.

## 1. Three integral-derived statements

The evaluated master triangle gives

$$
\mathcal I_{\rm tri}[\lambda;0]
=\frac12\lambda_1\wedge\lambda_2.
$$

The differential operator therefore obeys

$$
\mathcal D^{\rm tri}_{0,0}(f,g)
=\frac12\partial_{\dot\alpha}f\,\partial^{\dot\alpha}g.
$$

Appendix B gives

$$
m!n!C_{mn}
=\frac1{m+n+2}
\sum_{k=0}^{m}\sum_{l=0}^{n}
\frac1{k+l+1}
\binom mk\binom nl
(\lambda_1)_1^k(\lambda_1)_2^l
(\lambda_2)_1^{m-k}(\lambda_2)_2^{n-l}.
$$

At $m=n=0$,

$$
C_{00}=\frac1{2}\frac1{1}=\frac12.
$$

Hence

$$
\boxed{
\mathcal I_{\rm tri}[\lambda;0]
=\mathcal D^{\rm tri}_{0,0}
=C_{00}
=\frac12.}
$$

## 2. Conflict

The zero-shift component block and the compact-superfield block print unit
coefficients.  Therefore

$$
\frac{c_{\rm component}}{c_{\rm triangle}}
=\frac{1}{1/2}=2,
\qquad
\frac{c_{\rm compact}}{c_{\rm triangle}}
=\frac{1}{1/2}=2.
$$

The Project denominator identity is

$$
\frac1{D_0D_1D_2}
=2\int_{\Delta_2}\frac1{(L^2+\Delta)^3},
\qquad
2\int_{\Delta_2}1=1.
$$

Therefore the complete Project parameter kernel is

$$
\boxed{
\mathcal K^P_{m,n}(f^D,g^E)
=2\sum_{k=0}^{m}\sum_{l=0}^{n}
\frac{\binom mk\binom nl}
{(m+n+2)(k+l+1)}
(P_1^kP_2^lf^D)
(P_1^{m-k}P_2^{n-l}g^E).}
$$

Thus $\mathcal K^P_{0,0}=1$.  The source's zero-shift component and compact
branches have the complete-amplitude normalization.  Its master-integral,
generic shifted, and Appendix-B branches are uniformly smaller by $2$ and
must be multiplied by $2$ before comparison with the complete Project
amplitude.  This does not alter relative discrepancies among Project letter
families.
