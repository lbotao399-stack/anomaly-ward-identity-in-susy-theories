# GPT Pro round 6 response — full-N=4 one-loop gap review

Conversation: https://chatgpt.com/c/6a5519c3-70a4-83e8-8862-39f8df68d4dd

Role: advisory gap review only; no coefficient authority.

## 1. Gaussian word expansion

Write

$$
H_B=H_1+H_2+O(B^3),
\qquad
I_B=I_0+I_1+I_2+O(B^3).
$$

Then

$$
G_B
=G_0-G_0H_1G_0-G_0H_2G_0
+G_0H_1G_0H_1G_0+O(B^3).
$$

Hence

$$
\begin{aligned}
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}\Big[&
+I_0G_0H_1[1]G_0H_1[2]G_0
+I_0G_0H_1[2]G_0H_1[1]G_0\\
&-I_0G_0H_2[1,2]G_0
-I_1[1]G_0H_1[2]G_0\\
&-I_1[2]G_0H_1[1]G_0
+I_2[1,2]G_0\Big]+\mathrm{CT}_2.
\end{aligned}
$$

There are six words, one global factor $1/2$, and signs

$$
+,+,-,-,-,+.
$$

## 2. Topology translation

The two notational layers are related by

$$
I_2\leftrightarrow I_0,
\qquad
I_3\leftrightarrow I_1,
\qquad
I_4\leftrightarrow I_2,
$$

$$
S_3\leftrightarrow H_1,
\qquad
S_4\leftrightarrow H_2.
$$

## 3. Contact gate

The isolated triangle does not close the coefficient.  The required cut
relation is

$$
R_{\rm cut}a_{\rm metric}+b_{\rm native}=0.
$$

Until both terms and the transport $R_{\rm cut}$ are exact, the contact gate
is open.

## 4. Background covariance

For $L\in\{X,Y,Z,T\}$,

$$
\delta_RL=[R,L].
$$

This action preserves the intrinsic letter type.  It does not map $X$ into
$Y$, $Z$, or $T$ and therefore does not equate their loop coefficients.

## 5. DRED ordering

The admissible order is

$$
\sum_{\mathfrak g}\Gamma_{\mathfrak g}
\longrightarrow\text{contact closure}
\longrightarrow d\text{-dimensional tensor reduction}
\longrightarrow\operatorname{Loc}_{\rm UV}^{\rm DRED}
\longrightarrow\text{evanescent mixing}
\longrightarrow q_{4d}.
$$

In particular, $q_{4d}$ cannot be applied before pole extraction and
evanescent mixing because

$$
\frac1\epsilon\left(\epsilon\mathscr O\right)=\mathscr O.
$$

## 6. Matter-sector qualification

The abstract inference

$$
\text{source Hessian has }VV\text{ ports}
\Longrightarrow
\text{no matter carrier loop}
$$

is too strong.  Port type and internal carrier type are distinct data.  The
complete $I_3/I_4$ Euler matter blocks must be checked by the Project vertex
grammar.

## 7. Coefficient status

The old value

$$
\frac{g^2}{64\pi^2}
$$

is a row-aggregate hypothesis.  It is not an accepted one-loop anomaly
coefficient.
