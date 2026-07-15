# GPT Pro Gate 10 response — AB/BA first factor-two localization

Browser thread: `https://chatgpt.com/c/6a56dd0d-b678-83e8-87cd-38e71b372ec6`

This file preserves the mathematical content returned by GPT Pro.  Display-only
subscripts from the browser DOM have been normalized to TeX.

## 1. Routing and local basis

$$
P_D=D_0D_1D_2,qquad
r_0=\ell,quad r_1=\ell-p,quad r_2=\ell-p-q.
$$

For $G_1$, $p$ is the $B_1$ momentum and $q$ is the $D$ momentum.  GPT Pro
defined

$$
\Pi_{DB}=\langle D,B_1\rangle,qquad
E_{DB}=(P^{\dot a}D_{\dot a})B_1,
$$

and asserted

$$
T_{DB}=P^{\dot a}(D_{\dot a}B_1)=E_{DB}-\Pi_{DB},qquad
T_{BD}=E_{BD}-\Pi_{BD}.
$$

## 2. Claimed complete $G_1$ orbit

The two selected endpoint parents were reported as

$$
P_A=2P_D\bar r_2^{,2}r_0^{\dot a},qquad
K_A=-2D_0D_1r_0^{\dot a},qquad
R_A=2P_D\mu_\ell^2r_0^{\dot a},
$$

$$
P_B=-2P_D\bar r_0^{,2}r_2^{\dot a},qquad
K_B=+2D_1D_2r_2^{\dot a},qquad
R_B=-2P_D\mu_\ell^2r_2^{\dot a}.
$$

The simplex moments were

$$
A=\left(\frac43,\frac23\right),qquad
B=\left(\frac23,\frac43\right).
$$

GPT Pro then introduced an additional longitudinal parent-minus-cut family,

$$
P_L=-P_D\bar r_1^{,2}(r_0-r_2)^{\dot a},qquad
K_L=+D_0D_2(r_0-r_2)^{\dot a},
$$

$$
P_L^{(d)}+K_L=0,qquad
R_L=-P_D\mu_\ell^2(p+q)^{\dot a}.
$$

It was attributed to the selected $e_1$ longitudinal
$R_4\to R_2$ presentation

$$
+G_0V^{[1]}G_0V^{[1]}G_0I^{[0]}
\longrightarrow
-G_0V^{[1]}G_0I^{[1]},
$$

with

$$
I^{[1]}_{AB}=g^2(A_2^AB_{11}^B+A_1^AB_{12}^B).
$$

The claimed corrected raw vector was therefore

$$
A+B+L
=\left(\frac43,\frac23\right)
+\left(\frac23,\frac43\right)-(1,1)
=(1,1).
$$

Using $D_-D_+=D^2/2$, GPT Pro reported

$$
G_{1,\mathrm{prequot}}
=\lambda_1\left(\frac12\Pi_{DB}+\frac12E_{DB}\right),
$$

and, after quotienting by $T_{DB}$,

$$
[G_1]=\lambda_1\Pi_{DB}.
$$

## 3. $G_2$

GPT Pro retained

$$
G_{2,\mathrm{prequot}}
=\lambda_1\left(-\frac13\Pi_{BD}+\frac43E_{BD}\right),
$$

and hence

$$
[G_2]=\lambda_1\Pi_{BD}.
$$

## 4. $G_3$ absolute normalization

For the transverse trace

$$
T_\perp=-65536i,qquad W=p_+\wedge q_+=-i,
$$

GPT Pro used

$$
T_\perp=2cW,qquad
c=\frac{T_\perp}{2W}=32768.
$$

The original Berezin measures then give

$$
32768\left(\frac14\right)_{d^4\theta_M}
\left(\frac12\right)_{d^2\bar\theta_H}=4096.
$$

It identified the Gate-9 first error as applying another rank factor $-1/2$
after the division by $2W$ had already performed the two-axis trace reduction.
Thus the $4096$ route, not the $2048$ route, was declared correct.

The three parent/cut rows were reported as

$$
\begin{array}{c|c|c|c}
e&\text{parent}&\text{full-}d\text{ cut}&\mu_\ell^2\text{ remainder}\\
0&-4096P_D(D_0+\mu_\ell^2)W_0&+4096D_1D_2W_0&-4096P_D\mu_\ell^2W_0\\
1&+4096P_D(D_1+\mu_\ell^2)W_1&-4096D_0D_2W_1&+4096P_D\mu_\ell^2W_1\\
2&-4096P_D(D_2+\mu_\ell^2)W_2&+4096D_0D_1W_2&-4096P_D\mu_\ell^2W_2
\end{array}
$$

and the typed coefficients were

$$
G_{32}=-2i\sqrt2\lambda_1,qquad
G_{33}=+2i\sqrt2\lambda_1.
$$

## 5. Target-blind result claimed by GPT Pro

In the pre-quotient basis

$$
(\Pi_{DB},E_{DB},\Pi_{BD},E_{BD},
\langle C_2,C_3\rangle,\langle C_3,C_2\rangle),
$$

the response gave

$$
\lambda_1\left(
\frac12,\frac12,-\frac13,\frac43,-2i\sqrt2,+2i\sqrt2
\right).
$$

After its stated divergence quotient, it gave

$$
(G_1,G_2,G_{32},G_{33})
=\lambda_1(1,1,-2i\sqrt2,+2i\sqrt2).
$$

## 6. Claimed first-error localization

GPT Pro identified

$$
N_{G_1,\mathrm{full}}=N_A+N_B
$$

as the first invalid equality and proposed

$$
N_{G_1,\mathrm{full}}=N_A+N_B+N_L,qquad
N_L\mapsto-(p+q).
$$

This $N_L$ claim was not accompanied by an independently executable raw
Hessian/port replay in the response and therefore remains an input to be
strictly checked against the existing 192-row exact $D$-algebra artifact.
