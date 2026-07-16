# Step 5 no-descendant ordered pairs

Status: `TARGET_BLIND_EXACT_ZERO__NO_OUTER_DESCENDANT__NO_CUTTING_FAILURE_WORD`.

## 1. Exact outer identity

Let

$$
\mathbb L_0=(C_1,C_2,C_3,D_{\dot1},D_{\dot2}),
$$

with

$$
\nabla_-C_r=0,
\qquad
\nabla_-D_{\dot a}=0.
$$

For every ordered pair \((X,Y)\in\mathbb L_0^2\),

$$
\begin{aligned}
\nabla_-(XY)
&=(\nabla_-X)Y+(-1)^{|X|}X(\nabla_-Y)\\
&=0\cdot Y+(-1)^{|X|}X\cdot0\\
&=0.
\end{aligned}
$$

Hence

$$
N_{\mathrm{marked\ inverse\ kernels}}(X,Y)=0.
$$

## 2. DRED anomaly sector

The finite cutting failure requires a marked word

$$
\frac{\bar r_e^2-r_{e,d}^2}{D_0D_1D_2}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

Here no marked edge exists. Therefore, for all 25 ordered pairs,

$$
\boxed{\Gamma_{XY}^{\mathrm{ev}}=0},
\qquad
(X,Y)\in\mathbb L_0^2.
$$

The exact rows are

$$
(C_r,C_s),\ (C_r,D_{\dot a}),\ (D_{\dot a},C_r),\
(D_{\dot a},D_{\dot b}).
$$

Verification:

```text
python scripts/step5_no_descendant_pairs_exact_audit.py --check
```
