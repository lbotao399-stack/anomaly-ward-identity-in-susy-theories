# GPT Pro Gate 15 response — final one-loop / HT settlement

Status: `NON_AUTHORITY_PRO_REVIEW__FINAL_ONE_LOOP_HT_SETTLEMENT_ACCEPTED`.

Browser thread: `https://chatgpt.com/c/6a56dd0d-b678-83e8-87cd-38e71b372ec6`

This file preserves the returned mathematical content with browser display
fractions and subscripts normalized to TeX.

## 1. Universal DRED identity

External momenta have no evanescent components, so

$$
\bar r_e^2-r_{e,d}^2
=\bar\ell^2-\ell_d^2
=\mu_\ell^2.
$$

Since

$$
D_e=r_{e,d}^2,
\qquad
D_0D_1D_2=D_e\prod_{j\ne e}D_j,
$$

one has

$$
\begin{aligned}
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
&=\frac{D_e+\mu_\ell^2}{D_0D_1D_2}
-\frac{D_e}{D_0D_1D_2}\\
&=\frac{\mu_\ell^2}{D_0D_1D_2}.
\end{aligned}
$$

Replacing the numerator by the full square gives

$$
\frac{D_e}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{D_e}{D_0D_1D_2}
-\frac{D_e}{D_0D_1D_2}
=0.
$$

Thus every bare anomaly family is an occurrence-resolved cutting failure;
there is no additional $4-d$ multiplier.

## 2. Exact physical census

The nine letters give

$$
9^2=81
$$

ordered pairs.  The nonzero rows split as

$$
1_{A>A}
+6_{A>B_r,,B_r>A}
+6_{A>C_r,,C_r>A}
+6_{B_r>B_s,,r\ne s}
+6_{B_r>C_r,,C_r>B_r}
+4_{A>D_{\dot a},,D_{\dot a}>A}
=29.
$$

Therefore

$$
81-29=52.
$$

The nonzero output-word count is

$$
8+6\cdot4+6\cdot2+6\cdot2+6\cdot1+4\cdot2=70.
$$

The flavor, ordered-output, and zero/nonzero census contains no arithmetic
conflict.

## 3. Common-TD quotient

For $G_1$,

$$
T_{DB}=X_{DB}+E_{DB}
\quad\Longrightarrow\quad
E_{DB}=T_{DB}-X_{DB},
$$

$$
2X_{DB}+2E_{DB}
=2X_{DB}+2(T_{DB}-X_{DB})
=2T_{DB}.
$$

Hence

$$
(2,2)_{(X,E)}\longmapsto(0,2)_{(X,T)},
\qquad [G_1]_{\rm TD}=0.
$$

For $G_2$,

$$
T_{BD}=-X_{BD}+E_{BD}
\quad\Longrightarrow\quad
E_{BD}=T_{BD}+X_{BD},
$$

$$
-\frac13X_{BD}+\frac43E_{BD}
=-\frac13X_{BD}+\frac43(T_{BD}+X_{BD})
=X_{BD}+\frac43T_{BD}.
$$

Hence

$$
\left(-\frac13,\frac43\right)_{(X,E)}
\longmapsto
\left(1,\frac43\right)_{(X,T)},
\qquad [G_2]_{\rm TD}=1.
$$

Therefore

$$
v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2).
$$

Its Ward defect is

$$
M_qv_{\rm TD}=(-1,-2i\sqrt2,+2i\sqrt2)^T.
$$

The finite normal-product shift satisfies

$$
\delta v_{\rm fin}=(1,0,+i\sqrt2,-i\sqrt2),
$$

$$
M_q\delta v_{\rm fin}=(1,+2i\sqrt2,-2i\sqrt2)^T.
$$

Consequently,

$$
M_q(v_{\rm TD}+\delta v_{\rm fin})=0,
$$

$$
v_{\rm ren}
=(0,1,-2i\sqrt2,+2i\sqrt2)
+(1,0,+i\sqrt2,-i\sqrt2)
=(1,1,-i\sqrt2,+i\sqrt2),
$$

$$
M_qv_{\rm ren}=0.
$$

## 4. AA-fixed scale

For a Ward-compatible ray

$$
v(t)=t(1,1,-i\sqrt2,+i\sqrt2),
\qquad
\Delta_t(A,B_r)=t\mathscr Y_r,
$$

one has

$$
q_s\Delta_t(A,B_r)=it\delta_{sr}\mathscr Z.
$$

The independently normalized AA seed gives

$$
\Delta(A,A)=\mathscr Z,
\qquad
q_s\mathscr Y_r=i\delta_{sr}\mathscr Z.
$$

Therefore

$$
it\delta_{sr}\mathscr Z=i\delta_{sr}\mathscr Z
\quad\Longrightarrow\quad
t=1.
$$

No HT coefficient is used in this scale fixing.  The finite normal-product
term and the bare $\mu_\ell^2$ graph residues remain distinct layers.

## 5. Holomorphic-twist kernel

At $m=n=k=\ell=0$,

$$
T^{HT,\mathrm{printed}}_{0,0;0,0}=\frac12,
\qquad
K^P_{0,0;0,0}=1,
$$

so

$$
K^P_{0,0;0,0}
=2T^{HT,\mathrm{printed}}_{0,0;0,0}
=T^{HT,\mathrm{corrected}}_{0,0;0,0}.
$$

On the full domain,

$$
2T^{HT,\mathrm{printed}}_{m,n;k,\ell}
=\frac{2\binom mk\binom n\ell}
{(m+n+2)(k+\ell+1)}
=K^P_{m,n;k,\ell}.
$$

The exact rectangle count is

$$
\sum_{m=0}^{8}\sum_{n=0}^{8}(m+1)(n+1)
=\left(\sum_{j=1}^{9}j\right)^2
=45^2
=2025.
$$

For 70 nonzero base-output words,

$$
2025\cdot70=141750.
$$

The executable totals and the closed-form all-jet identity are consistent.

## 6. Final scope check

The machine result

$$
33/33\ {\rm PASS},
\qquad
0\ {\rm FAIL}
$$

agrees with the preceding algebra.  The accepted physical scope does not
assert the excluded general BV, formal-$U/Q_0$, general reductive-color, or
raw-graph-functor theorems.

Finally,

$$
32768\left(\frac14\right)\left(\frac12\right)=4096,
$$

$$
65536\left(\frac14\right)\left(\frac14\right)=4096.
$$

The correlated cycles cancel the outer $1/2$ and leave no normalization fork.

Verdict: `FINAL_ONE_LOOP_HT_SETTLEMENT_ACCEPTED`.
