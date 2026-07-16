# GPT Pro AB1 derivation-correction response

Status: `NON_AUTHORITY_PRO_REVIEW`

- Chat: https://chatgpt.com/c/6a56596b-5448-83e8-9284-5a6e4fc5dc65
- Gate: `derivation`
- Prompt: `/Users/libotao/.codex/procodex/2026-07-14-awi-ab1-pair-standard-feynman/derivation-correction-prompt.md`
- Prompt SHA-256: `059d7aa7bef7ac723ec8969ef1af172a983c2073233fe75dab32c198be45b3fd`
- Rendered-body SHA-256: `380487ff9e9a65579bb34441016937f963f6d0ee81ac54589ee3dc82e47e5f19`
- GPT Pro reported elapsed time: `31m 48s`

The response below is evidence for adjudication only.  It is not Project authority.

---

## New notation

$$
X(v):=D_+v,\qquad
[P,Q\}_{\rm gr}:=PQ-(-1)^{|P||Q|}QP .
$$

$$
\mathcal E_t:=e^{t\,w\cdot\partial},\qquad
\eta:=\eta_u,\qquad
\chi:=\eta_1 .
$$

$$
\Delta:=\hbar^{-1}G_{\rm Wick}.
$$

因此 boxed resolvent 中的 $G$ 必须解释为 inverse kernel $\Delta$，而不是含 $\hbar$ 的 Wick propagator；否则 $GI_{[2]}$ 会成为 $O(\hbar^2)$，与 one-loop counting 矛盾。

$$
\Pi_2=(12,21),\qquad
\Pi_3=(123,132,213,231,312,321).
$$

由于

$$
|A_cB_{1,c}|=1,
$$

source 满足

$$
|J_{AB}|=1.
$$

以下始终把 $J_{AB}$ 放在最左侧，不与 odd letter $B_{1,c}$ 交换。

当前 branch status：

```
LOCAL_PROPOSAL_AB1_ORDERED_SOURCE
```

---

# 1. `CORRECTED_EXPONENT_LEDGER`

## 1.1 Action derivative、exponent vertex、propagator

$$
Z[J]
=
\int\mathcal D\Xi\,
\exp\left[
-\frac1\hbar S_E
+\frac1\hbar J_{AB}\mathcal O^{AB}_{AB_1}
\right].
$$

三种必须区分的 quantities 是：

$$
S^{(n)}:=\frac{\delta^nS_E}{\delta\Xi^n},
\qquad
v^{(n)}:=-S^{(n)},
\qquad
G_{\rm Wick}=\hbar\,K^{-1}.
$$

Matter cubic：

$$
S_{M_r}^{(3)}
=
-\sqrt2g\int d^8z\,
\widetilde\phi_r^A u^U(T_U)^A{}_C\phi_r^C,
$$

$$
\frac{\delta^3S_E}
{\delta\widetilde\phi_r^A\delta u^U\delta\phi_r^C}
=
-\sqrt2g\,(T_U)^A{}_C,
$$

$$
\boxed{
v_{M_r}
=
+\sqrt2g\,(T_U)^A{}_C .
}
$$

Matter seagull 的两个 labeled words：

$$
\boxed{
v_{S;U_1U_2}
=
g^2(T_{U_1}T_{U_2})^A{}_C,
}
$$

$$
\boxed{
v_{S;U_2U_1}
=
g^2(T_{U_2}T_{U_1})^A{}_C.
}
$$

其和为

$$
v_S
=
g^2
\left[
T_{U_1}T_{U_2}+T_{U_2}T_{U_1}
\right]^A{}_C.
$$

Antichiral cubic：

$$
\frac{\delta^3S_E}
{\delta\widetilde\phi_{r_1}^{A_1}
 \delta\widetilde\phi_{r_2}^{A_2}
 \delta\widetilde\phi_{r_3}^{A_3}}
=
+\sqrt2g\,
\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3},
$$

$$
\boxed{
v_H
=
-\sqrt2g\,
\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
}
$$

对应 exponent factors 分别为 $v/\hbar$。

---

## 1.2 Reduced propagators

Vector：

$$
G^{AB}_{u u,\rm Wick}(1,2)
=
+\hbar\delta^{AB}
\frac{\delta^4(\theta_{12})}{p^2},
$$

$$
\boxed{
\Delta^{AB}_{u u}(1,2)
=
+\delta^{AB}
\frac{\delta^4(\theta_{12})}{p^2}.
}
$$

Forward chiral ordering：

$$
G_{\phi_r^A\widetilde\phi_s^B,\rm Wick}(1,2)
=
-\delta_{rs}
\frac{\hbar\delta^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\theta_{12}),
$$

$$
\boxed{
\Delta_{\phi_r^A\widetilde\phi_s^B}(1,2)
=
-\delta_{rs}
\frac{\delta^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\theta_{12}).
}
$$

Reverse chiral ordering：

$$
G_{\widetilde\phi_s^B\phi_r^A,\rm Wick}(1,2)
=
-\delta_{rs}
\frac{\hbar\delta^{AB}}{16p^2}
D_1^2\bar D_1^2\delta^4(\theta_{12}),
$$

$$
\boxed{
\Delta_{\widetilde\phi_s^B\phi_r^A}(1,2)
=
-\delta_{rs}
\frac{\delta^{AB}}{16p^2}
D_1^2\bar D_1^2\delta^4(\theta_{12}).
}
$$

定义 constrained projectors

$$
\Pi_+(p)
=
\frac{\bar D^2D^2}{16p^2},
\qquad
\Pi_-(p)
=
\frac{D^2\bar D^2}{16p^2}.
$$

则

$$
\Delta_{\phi\widetilde\phi}=-\Pi_+,
\qquad
\Delta_{\widetilde\phi\phi}=-\Pi_-.
$$

Quadratic matter kernel 本身也带负号，因此

$$
\boxed{
K_VG_{V,\rm Wick}=+\hbar\,\mathbf1_V,
}
$$

$$
\boxed{
K_{\widetilde\phi\phi}
G_{\phi\widetilde\phi,\rm Wick}
=+\hbar\,\mathbf1_+,
}
$$

$$
\boxed{
K_{\phi\widetilde\phi}
G_{\widetilde\phi\phi,\rm Wick}
=+\hbar\,\mathbf1_-.
}
$$

所有 admissible edge cuts 的 kernel-inverse multiplication sign 均为 $+$。

---

## 1.3 Pre-$D$-transport parent signs

把 $A_1$ 的 coefficient

$$
-\frac{\sqrt2}{8}
$$

也包括在 parent 中，但暂不移动任何 spinor derivative。

### $G_2$

$$
\begin{aligned}
C_{G_2}^{\rm preD}
&=
\frac{\hbar}{2}
\left(-\frac{\sqrt2}{8}\right)
(\sqrt2g)^2
\left(-\frac1{16}\right)^2\\
&=
-\frac{\hbar\sqrt2\,g^2}{2048}.
\end{aligned}
$$

$$
\boxed{
C_{G_2}^{\rm preD}
=
-\frac{\hbar\sqrt2\,g^2}{2048}.
}
$$

### $G_{3,r}$

$$
\begin{aligned}
C_{G_{3,r}}^{\rm preD}
&=
\frac{\hbar}{2}
\left(-\frac{\sqrt2}{8}\right)
(\sqrt2g)
\left(-\sqrt2g\,\varepsilon_{1rt}\right)
\left(-\frac1{16}\right)^2\\
&=
+\frac{\hbar\sqrt2\,g^2}{2048}
\varepsilon_{1rt}.
\end{aligned}
$$

因此

$$
\boxed{
C_{G_{3,2}}^{\rm preD}
=
+\frac{\hbar\sqrt2\,g^2}{2048},
}
$$

$$
\boxed{
C_{G_{3,3}}^{\rm preD}
=
-\frac{\hbar\sqrt2\,g^2}{2048}.
}
$$

### Matter seagull，per ordered color word

$$
\begin{aligned}
C_S^{\rm preD}
&=
\frac{\hbar}{2}
(-1)_{\,-GV_{[2]}GI_{[0]}}
\left(-\frac{\sqrt2}{8}\right)
g^2
\left(-\frac1{16}\right)\\
&=
-\frac{\hbar\sqrt2\,g^2}{256}.
\end{aligned}
$$

$$
\boxed{
C_{S;AE}^{\rm preD}
=
C_{S;EA}^{\rm preD}
=
-\frac{\hbar\sqrt2\,g^2}{256}.
}
$$

### Mixed $M_1-I_{[1]}$ bubble

$I_{[1]}$ 自带一个 $g$：

$$
\begin{aligned}
C_{M-I_1}^{\rm loop}
&=
\frac{\hbar}{2}
(-1)
(\sqrt2g)
\left(-\frac1{16}\right)
g\\
&=
+\frac{\hbar\sqrt2\,g^2}{32}.
\end{aligned}
$$

其余 numerical coefficients 已完整包含在具体 $A_2,B_{12},T_1$ word 中。

### $G_1$

令 reduced ordered $VVV$ kernel 为 $\mathcal G_{abc}$。则

$$
\begin{aligned}
C_{G_1}^{\rm preD}
&=
\frac{\hbar}{2}
\left(-\frac{\sqrt2}{8}\right)
(\sqrt2g)
\left(-\frac1{16}\right)\mathcal G_{abc}\\
&=
+\frac{\hbar g}{128}\mathcal G_{abc}.
\end{aligned}
$$

但 $\mathcal G_{abc}$ 本身尚未给定：

```
BLOCKED_VVV_ORDERED_SUPERKERNEL_UNSPECIFIED
```

---

# 2. `A_AND_B_NONLINEAR_WORDS`

所有 matrix words 以下均不交换次序。若

$$
u=u^at_a,
$$

则例如

$$
X(u_1)u_2u_3
$$

的 color chain 是

$$
t_{a_1}t_{a_2}t_{a_3}
$$

并保持该顺序。

## 2.1 Expansion of $\Gamma_+$

由

$$
\Gamma_+
=
\sum_{p,q\geq0}
\frac{(-1)^p}{p!q!(p+q+1)}
V^p(D_+V)V^q
$$

逐阶得到：

$$
\Gamma_+^{[V]}
=
D_+V,
$$

$$
\Gamma_+^{[V^2]}
=
\frac12(D_+V)V-\frac12V(D_+V),
$$

$$
\Gamma_+^{[V^3]}
=
\frac16(D_+V)V^2
-\frac13V(D_+V)V
+\frac16V^2(D_+V).
$$

令

$$
X:=D_+u,\qquad V=\sqrt2g\,u.
$$

则

$$
\boxed{
\Gamma_+
=
g\gamma_1+g^2\gamma_2+g^3\gamma_3+O(g^4),
}
$$

其中

$$
\boxed{
\gamma_1=\sqrt2X,
}
$$

$$
\boxed{
\gamma_2=Xu-uX,
}
$$

$$
\boxed{
\gamma_3
=
\frac{\sqrt2}{3}
\left(
Xu^2-2uXu+u^2X
\right).
}
$$

这些均为 odd matrix superfields。

---

## 2.2 Expansion of $\mathcal W_+$

$$
\mathcal W_+
=
-\frac18\bar D^2\Gamma_+
=
gW_1+g^2W_2+g^3W_3+O(g^4),
$$

$$
\boxed{
W_1
=
-\frac{\sqrt2}{8}\bar D^2X,
}
$$

$$
\boxed{
W_2
=
-\frac18\bar D^2(Xu-uX),
}
$$

$$
\boxed{
W_3
=
-\frac{\sqrt2}{24}
\bar D^2
\left(
Xu^2-2uXu+u^2X
\right).
}
$$

---

## 2.3 Expansion of $A_c$

由于 $\Gamma_+$ 与 $\mathcal W_+$ 都是 odd，

$$
[\Gamma_+,\mathcal W_+\}_{\rm gr}
=
\Gamma_+\mathcal W_+
+\mathcal W_+\Gamma_+.
$$

因此

$$
A_c
=
g^{-1}
\left[
D_+\mathcal W_+
+
\Gamma_+\mathcal W_+
+
\mathcal W_+\Gamma_+
\right].
$$

### Linear word

$$
\boxed{
A_1
=
-\frac{\sqrt2}{8}
D_+\bar D^2D_+u.
}
$$

### Quadratic word

$$
\boxed{
\begin{aligned}
A_2={}&
-\frac18D_+\bar D^2
\left[
(D_+u)u-u(D_+u)
\right]\\
&-\frac14
(D_+u)\bar D^2(D_+u)
-\frac14
\bar D^2(D_+u)(D_+u).
\end{aligned}
}
$$

没有交换两个 odd factors。

### Cubic word

$$
\boxed{
\begin{aligned}
A_3={}&
-\frac{\sqrt2}{24}
D_+\bar D^2
\left[
(D_+u)u^2
-2u(D_+u)u
+u^2(D_+u)
\right]\\
&-\frac{\sqrt2}{8}
(D_+u)\,
\bar D^2\!\left[(D_+u)u-u(D_+u)\right]\\
&-\frac{\sqrt2}{8}
\bar D^2\!\left[(D_+u)u-u(D_+u)\right]
(D_+u)\\
&-\frac{\sqrt2}{8}
\left[(D_+u)u-u(D_+u)\right]
\bar D^2(D_+u)\\
&-\frac{\sqrt2}{8}
\bar D^2(D_+u)
\left[(D_+u)u-u(D_+u)\right].
\end{aligned}
}
$$

因此

$$
\boxed{
A_c=A_1+gA_2+g^2A_3+O(g^3).
}
$$

---

## 2.4 Expansion of $B_{1,c}$

$$
B_{1,c}
=
D_+\phi_1+[\Gamma_+,\phi_1],
$$

其中 $\phi_1$ even，所以这里是 ordinary commutator。

$$
\boxed{
B_{11}=D_+\phi_1.
}
$$

$$
\boxed{
B_{12}
=
\sqrt2
\left[
(D_+u)\phi_1
-\phi_1(D_+u)
\right].
}
$$

$$
\boxed{
\begin{aligned}
B_{13}={}&
\left[
(D_+u)u-u(D_+u)
\right]\phi_1\\
&-\phi_1
\left[
(D_+u)u-u(D_+u)
\right].
\end{aligned}
}
$$

因此

$$
\boxed{
B_{1,c}
=
B_{11}+gB_{12}+g^2B_{13}+O(g^3).
}
$$

---

# 3. `I0_I1_I2_ORDERED_HESSIANS`

## 3.1 Ordered multilinear endpoint kernels

为区分每个 gauge slot，定义

$$
\gamma_1[u_1]
=
\sqrt2D_+u_1,
$$

$$
\gamma_2[u_1,u_2]
=
(D_+u_1)u_2-u_1(D_+u_2),
$$

$$
\gamma_3[u_1,u_2,u_3]
=
\frac{\sqrt2}{3}
\left[
(D_+u_1)u_2u_3
-2u_1(D_+u_2)u_3
+u_1u_2(D_+u_3)
\right].
$$

令

$$
w_i=-\frac18\bar D^2\gamma_i.
$$

则

$$
a_1[u_1]
=
D_+w_1[u_1],
$$

$$
\boxed{
\begin{aligned}
a_2[u_1,u_2]={}&
D_+w_2[u_1,u_2]\\
&+\gamma_1[u_1]w_1[u_2]
+w_1[u_1]\gamma_1[u_2].
\end{aligned}
}
$$

$$
\boxed{
\begin{aligned}
a_3[u_1,u_2,u_3]={}&
D_+w_3[u_1,u_2,u_3]\\
&+\gamma_1[u_1]w_2[u_2,u_3]
+w_2[u_1,u_2]\gamma_1[u_3]\\
&+\gamma_2[u_1,u_2]w_1[u_3]
+w_1[u_1]\gamma_2[u_2,u_3].
\end{aligned}
}
$$

以及

$$
b_1[\phi]=D_+\phi,
$$

$$
b_2[u;\phi]
=
\gamma_1[u]\phi-\phi\gamma_1[u],
$$

$$
b_3[u_1,u_2;\phi]
=
\gamma_2[u_1,u_2]\phi
-\phi\gamma_2[u_1,u_2].
$$

---

## 3.2 Ordered link kernels

定义单一 gauge-link port

$$
\mathbb M[u]
:=
w\cdot\mathbb A_{\rm ad}[u].
$$

$$
t_1[u;Y]
=
\int_0^1dt\,
\mathcal E_{1-t}\,
\mathbb M[u]\,
\mathcal E_tY.
$$

$$
\boxed{
\begin{aligned}
t_2[u_1,u_2;Y]
={}&
\int_{0\leq t_1\leq t_2\leq1}
dt_1dt_2\,
\mathcal E_{1-t_2}\,
\mathbb M[u_1]\\
&\qquad\times
\mathcal E_{t_2-t_1}\,
\mathbb M[u_2]\,
\mathcal E_{t_1}Y.
\end{aligned}
}
$$

这里没有 $1/2!$。

但 $\mathbb A_{\rm ad}[u]$ 的 superspace kernel、normalization 与 color convention 尚未给出。因此涉及 $t_1,t_2$ 的 port-level color/D-word 受限于

```
BLOCKED_LINK_CONNECTION_FUNCTIONAL_UNSPECIFIED
```

---

## 3.3 Six exact $g^2$ source words

定义

$$
q_1(u_1,u_2;\phi)
=
a_2[u_1,u_2]\,T_0b_1[\phi],
$$

$$
q_2(u_1,u_2;\phi)
=
a_1[u_1]\,T_0b_2[u_2;\phi],
$$

$$
q_3(u_1,u_2;\phi)
=
a_1[u_1]\,t_1[u_2;b_1[\phi]].
$$

以及

$$
r_1(u_1,u_2,u_3;\phi)
=
a_3[u_1,u_2,u_3]\,T_0b_1[\phi],
$$

$$
r_2(u_1,u_2,u_3;\phi)
=
a_2[u_1,u_2]\,T_0b_2[u_3;\phi],
$$

$$
r_3(u_1,u_2,u_3;\phi)
=
a_1[u_1]\,T_0b_3[u_2,u_3;\phi],
$$

$$
r_4(u_1,u_2,u_3;\phi)
=
a_2[u_1,u_2]\,t_1[u_3;b_1[\phi]],
$$

$$
r_5(u_1,u_2,u_3;\phi)
=
a_1[u_1]\,t_1[u_2;b_2[u_3;\phi]],
$$

$$
r_6(u_1,u_2,u_3;\phi)
=
a_1[u_1]\,t_2[u_2,u_3;b_1[\phi]].
$$

每个 product coefficient 均为 $1$。

---

## 3.4 $I_{[0]}$

$$
\boxed{
I_{[0];u\phi}(\eta,\chi)
=
J_{AB}\,
a_1^A[\eta]\,
[T_0b_1[\chi]]^B.
}
$$

Reverse Hessian ordering：

$$
\boxed{
I_{[0];\phi u}(\chi,\eta)
=
J_{AB}\,
a_1^A[\eta]\,
[T_0b_1[\chi]]^B.
}
$$

因为 $\eta,\chi$ 均为 even fundamental superfields，第二式没有额外 minus sign。Reverse propagator 仍必须使用 $D^2\bar D^2$ ordering。

---

## 3.5 $I_{[1]}$

### Quantum ports $(u,\phi_1)$，background $\bar u$

$$
\boxed{
\begin{aligned}
I_{[1];u\phi|\bar u}(\eta,\chi;\bar u)
=gJ_{AB}\Big\{&
a_2^A[\eta,\bar u]\,T_0b_1^B[\chi]\\
&+a_2^A[\bar u,\eta]\,T_0b_1^B[\chi]\\
&+a_1^A[\eta]\,T_0b_2^B[\bar u;\chi]\\
&+a_1^A[\bar u]\,T_0b_2^B[\eta;\chi]\\
&+a_1^A[\eta]\,t_1[\bar u;b_1[\chi]]^B\\
&+a_1^A[\bar u]\,t_1[\eta;b_1[\chi]]^B
\Big\}.
\end{aligned}
}
$$

$$
I_{[1];\phi u|\bar u}
$$

由交换两个 quantum derivative slots 得到，kernel 内的 ordered products 不交换，且没有 Koszul minus sign。

### Quantum ports $(u,u)$，background $\bar\phi_1$

$$
\boxed{
\begin{aligned}
I_{[1];uu|\bar\phi}(\eta_1,\eta_2;\bar\phi)
=gJ_{AB}\Big\{&
a_2^A[\eta_1,\eta_2]\,T_0b_1^B[\bar\phi]\\
&+a_2^A[\eta_2,\eta_1]\,T_0b_1^B[\bar\phi]\\
&+a_1^A[\eta_1]\,T_0b_2^B[\eta_2;\bar\phi]\\
&+a_1^A[\eta_2]\,T_0b_2^B[\eta_1;\bar\phi]\\
&+a_1^A[\eta_1]\,t_1[\eta_2;b_1[\bar\phi]]^B\\
&+a_1^A[\eta_2]\,t_1[\eta_1;b_1[\bar\phi]]^B
\Big\}.
\end{aligned}
}
$$

不存在

$$
I_{[1];\phi\widetilde\phi|\bar\phi},
\qquad
I_{[1];\phi_1\phi_2|C_2},
\qquad
I_{[1];u\widetilde\phi_r|C_s}.
$$

---

## 3.6 $I_{[2]}$

令 $\bar u_a,\bar u_b$ 是两个 labeled external background ports。

### Quantum ports $(u,\phi_1)$，backgrounds $(\bar u_a,\bar u_b)$

$$
\boxed{
\begin{aligned}
I_{[2];u\phi|\bar u_a\bar u_b}
=
g^2J_{AB}
\sum_{j=1}^{6}\Big[
&r_j(\eta,\bar u_a,\bar u_b;\chi)
+r_j(\eta,\bar u_b,\bar u_a;\chi)\\
&+r_j(\bar u_a,\eta,\bar u_b;\chi)
+r_j(\bar u_a,\bar u_b,\eta;\chi)\\
&+r_j(\bar u_b,\eta,\bar u_a;\chi)
+r_j(\bar u_b,\bar u_a,\eta;\chi)
\Big]^{AB}.
\end{aligned}
}
$$

每个 occurrence coefficient 是 $1$。

### Quantum ports $(u,u)$，backgrounds $(\bar u,\bar\phi_1)$

$$
\boxed{
\begin{aligned}
I_{[2];uu|\bar u\bar\phi}
=
g^2J_{AB}
\sum_{j=1}^{6}\Big[
&r_j(\eta_1,\eta_2,\bar u;\bar\phi)
+r_j(\eta_1,\bar u,\eta_2;\bar\phi)\\
&+r_j(\eta_2,\eta_1,\bar u;\bar\phi)
+r_j(\eta_2,\bar u,\eta_1;\bar\phi)\\
&+r_j(\bar u,\eta_1,\eta_2;\bar\phi)
+r_j(\bar u,\eta_2,\eta_1;\bar\phi)
\Big]^{AB}.
\end{aligned}
}
$$

Port support 总结：

$$
\boxed{
\operatorname{supp}I_{[0]}
=
\{u\phi,\phi u\},
}
$$

$$
\boxed{
\operatorname{supp}I_{[1]}
=
\{u\phi|\bar u,\phi u|\bar u,uu|\bar\phi\},
}
$$

$$
\boxed{
\operatorname{supp}I_{[2]}
=
\{u\phi|\bar u\bar u,\phi u|\bar u\bar u,
uu|\bar u\bar\phi\}.
}
$$

特别地，任何 $I_{[n]}$ 都没有 quantum $\widetilde\phi$ port，也没有 $C_2,C_3$ background port。

---

# 4. `FOUR_CLASS_OCCURRENCE_CENSUS`

以下均不使用 symmetry quotient。

## 4.1 $+GI_{[2]}$

只有

$$
I_{[2];uu|\bar u\bar\phi}
$$

能由单一 free propagator 闭合；$G_{u\phi}=0$，所以 $I_{[2];u\phi|\bar u\bar u}$ 不能形成 tadpole。

Exact occurrence set：

$$
\boxed{
\mathcal C_{GI_2}
=
\{
T_{j,\pi}
\mid
j=1,\ldots ,6,\ 
\pi\in\Pi_3
\}.
}
$$

总数：

$$
6\times6=36.
$$

每个 $T_{j,\pi}$ 的完整 tuple 是

$$
\boxed{
\begin{aligned}
(&\text{source ports }u_{\pi(1)},u_{\pi(2)},\\
&\text{vertex slots }r_j(U_{\pi(1)},U_{\pi(2)},U_{\pi(3)};\bar\phi),\\
&\text{edge }V,\quad k,\\
&\text{source exponent }+g^2J/\hbar,\\
&\text{propagator }+\hbar\,\delta^4(\theta_{12})/k^2,\\
&\text{Koszul }+1,\\
&\text{color/D-word exactly the displayed }r_j,\\
&\text{output }(\bar u,\bar\phi_1)).
\end{aligned}
}
$$

其中 $j=1,2,3$ 为 endpoint occurrences；$j=4,5,6$ 为 link occurrences，后者受

```
BLOCKED_LINK_CONNECTION_FUNCTIONAL_UNSPECIFIED
```

限制。

---

## 4.2 $-GV_{[1]}GI_{[1]}$

### Matter-insertion bubbles

Exact set：

$$
\boxed{
\mathcal C_{M-I_1}
=
\{
M_{j,\sigma}
\mid
j=1,2,3,\ 
\sigma\in\Pi_2
\}.
}
$$

总数：

$$
3\times2=6.
$$

每个 occurrence：

$$
\boxed{
\begin{aligned}
(&\text{source ports }u,\phi_1,\\
&\text{\(I_{[1]}\) slot }q_j(\eta,\bar u;\chi)
\text{ or }q_j(\bar u,\eta;\chi),\\
&\text{\(M_1\) slots }(u,\widetilde\phi_1),\\
&\text{edges }(V,\Phi_1),\\
&\text{routing }(k,k-p),\\
&\text{exponents }(+gJ/\hbar,\ +\sqrt2gT/\hbar),\\
&\text{propagators }
(+\hbar/k^2,\
-\hbar\bar D^2D^2/[16(k-p)^2]),\\
&\text{class sign }-1,\quad
\text{Wick Koszul }+1,\\
&\text{output }(\bar u,\phi_1)).
\end{aligned}
}
$$

### Gauge-insertion bubbles

$I_{[1];uu|\bar\phi}$ 与 cubic $VVV$ 相连。

对于每个 $q_j$、每个 $\sigma\in\Pi_2$、每个 ordered $VVV$ port triple

$$
(a,b|c)
\in
\{
(1,2|3),(2,1|3),
(1,3|2),(3,1|2),
(2,3|1),(3,2|1)
\},
$$

均有一个 labeled occurrence：

$$
3\times2\times6=36.
$$

这些 rows 不能完成，因为 ordered $\mathcal G_{abc}$ 未给出：

```
BLOCKED_VVV_ORDERED_SUPERKERNEL_UNSPECIFIED
```

---

## 4.3 $-GV_{[2]}GI_{[0]}$

唯一由已给物理 action 确定的 compatible quartic Hessian 是 matter seagull。

两个 labeled occurrences：

$$
\boxed{
S_{AE}:
\quad
(T_A T_E)^B{}_D,
}
$$

$$
\boxed{
S_{EA}:
\quad
(T_E T_A)^B{}_D.
}
$$

Port tuple：

$$
\boxed{
\begin{aligned}
(&\text{source ports }u^A,\phi_1^B,\\
&\text{seagull slots }
u^A,u^E,\widetilde\phi_1^B,\phi_1^D,\\
&\text{edges }(V,\Phi_1),\\
&\text{routing }(k,k-p),\\
&\text{exponents }(+J/\hbar,\ +g^2T_AT_E/\hbar)
\text{ or }(+g^2T_ET_A/\hbar),\\
&\text{propagators }
(+\hbar/k^2,\
-\hbar\bar D^2D^2/[16(k-p)^2]),\\
&\text{class sign }-1,\quad
\text{Koszul }+1,\\
&\text{output }(u^E,\phi_1^D)).
\end{aligned}
}
$$

### Gauge-fixing/ghost port proof

$I_{[0]}$ 的 quantum ports 是

$$
\{u,\phi_1\}.
$$

所以一个 $V_{[2]}$ vertex 若要闭合，必须含有 conjugate ports

$$
\{u,\widetilde\phi_1\}.
$$

纯 gauge、FP、NK、measure vertices 的 port sets 分别是

$$
\{u,\ldots ,u\},
\qquad
\{u,\bar c,c\},
\qquad
\{u,\bar b,b\},
$$

均没有 $\widetilde\phi_1$。因此在 standard pure-gauge ghost branch 中，它们不能与 $I_{[0]}$ 构成该 bubble。

NK action 本身尚未选择，故保留：

```
BLOCKED_STEP5A_NK_BRANCH_UNSELECTED
```

若 measure 含有 mixed matter ports，则必须另行给出；不能由当前 measure information 排除。

---

## 4.4 $+GV_{[1]}GV_{[1]}GI_{[0]}$

物理 connected one-loop occurrences 是：

$$
G_1=(I[u,\phi_1],M_1,G),
$$

$$
G_2^{DB},\qquad G_2^{BD},
$$

$$
G_{3,2},
\qquad
G_{3,3}.
$$

Ghost structural proof：

- 两个 ghost cubic vertices 无法吸收 source $\phi_1$ port；
- 一个 $M_1$ 与一个 cubic ghost vertex：source $\phi_1$ 必须接 $M_1\widetilde\phi_1$，剩余 source $u$ 与 $M_1u$ 需要 ghost vertex 提供两个 $u$ ports，但 cubic ghost vertex 只有一个 $u$ port；
- ghost 与 antighost ports 仍未饱和。

所以不存在该阶 connected FP/NK triangle。

Pure-$u$ measure cubic 加 $M_1$ 则具有与 $G_1$ 相同的 port compatibility，不能设为零。其 kernel 未给出。

---

# 5. `G1_G2_BD_DALGEBRA`

设 source 的两个 endpoint 具有相同 $\theta_s$，但 spacetime points 由 $T_0$ 分离。

定义 source derivative operator

$$
\mathscr A_s
:=
D_{s+}\bar D_s^2D_{s+}.
$$

$A_1$ 的 numerical coefficient $-\sqrt2/8$ 已计入上一节的 parent scalar。

对于有向 chiral edge $i:\phi\to j:\widetilde\phi$，定义 numerator word

$$
\mathscr P^+_{ij}
:=
\bar D_i^2D_i^2\delta^4(\theta_{ij}).
$$

反向 traversal 必须独立写为

$$
\mathscr P^-_{ji}
:=
D_j^2\bar D_j^2\delta^4(\theta_{ji}).
$$

---

## 5.1 $G_1$

取 vertex order

$$
S\longrightarrow M\longrightarrow G\longrightarrow S.
$$

Loop routing：

$$
e_{SM}:\ell,\qquad
e_{MG}:\ell-p,\qquad
e_{GS}:\ell-p-q.
$$

$M$ 输出 $B_1^D(p)$，$G$ 输出 candidate $D^E(q)$。

固定 external $VVV$ port $g_c$ 后，两个 labeled assignments 是

$$
(s_u,m_u,\mathrm{ext})
\leftrightarrow
(g_a,g_b,g_c),
$$

$$
(s_u,m_u,\mathrm{ext})
\leftrightarrow
(g_b,g_a,g_c).
$$

Color words：

$$
\boxed{
(T_U)^B{}_D\,
\mathcal C_G(A,U,E;a,b,c),
}
$$

$$
\boxed{
(T_U)^B{}_D\,
\mathcal C_G(U,A,E;b,a,c).
}
$$

Raw noncommutative $D$-words：

$$
\boxed{
\mathfrak D_{G_1}^{(a,b|c)}
=
\left[
\mathscr A_s\,
\delta^4(\theta_s-\theta_{g_a})
\right]
\left[
D_{s+}\mathscr P^+_{sM}
\right]
\delta^4(\theta_M-\theta_{g_b})
\,
\mathfrak G_{abc}.
}
$$

$$
\boxed{
\mathfrak D_{G_1}^{(b,a|c)}
=
\left[
\mathscr A_s\,
\delta^4(\theta_s-\theta_{g_b})
\right]
\left[
D_{s+}\mathscr P^+_{sM}
\right]
\delta^4(\theta_M-\theta_{g_a})
\,
\mathfrak G_{bac}.
}
$$

这里 $\mathfrak G_{abc}$ 是 $VVV$ vertex 自身的 ordered spinor-derivative word。它未被给出，所以：

- derivative transport signs；
- rank-two、rank-one、rank-zero numerators；
- $BD$ 与 $DB$ ordered kernel decomposition；

均不能计算。

```
BLOCKED_VVV_ORDERED_SUPERKERNEL_UNSPECIFIED
```

---

## 5.2 $G_2^{DB}$

令左 action vertex $M_L$ 输出 $D^E$，右 action vertex $M_R$ 输出 $B_1^D$。

Ports：

$$
s_{\phi_1}^B
\longrightarrow
(M_L)_{\widetilde\phi_1^B},
$$

$$
(M_L)_{\phi_1^X}
\longrightarrow
(M_R)_{\widetilde\phi_1^X},
$$

$$
s_u^A
\longrightarrow
(M_R)_{u^A}.
$$

Color word：

$$
\boxed{
(T_E)^B{}_X(T_A)^X{}_D
=
(T_ET_A)^B{}_D.
}
$$

Output：

$$
\boxed{
(D^E,B_1^D).
}
$$

Loop routing：

$$
e_{S L}^{\Phi_1}:\ell,
\qquad
e_{L R}^{\Phi_1}:\ell-p,
\qquad
e_{R S}^{V}:\ell-p-q.
$$

Exponent factors：

$$
+\frac{J_{AB}}{\hbar},
\qquad
+\frac{\sqrt2g}{\hbar}(T_E)^B{}_X,
\qquad
+\frac{\sqrt2g}{\hbar}(T_A)^X{}_D.
$$

Propagator factors：

$$
-\frac{\hbar}{16\ell^2}\mathscr P^+_{sL},
$$

$$
-\frac{\hbar}{16(\ell-p)^2}\mathscr P^+_{LR},
$$

$$
+\frac{\hbar}{(\ell-p-q)^2}
\delta^4(\theta_R-\theta_s).
$$

Wick Koszul sign：

$$
+1.
$$

Raw $D$-word：

$$
\boxed{
\mathfrak D_{G_2}^{DB}
=
\left[
\mathscr A_s\,
\delta^4(\theta_s-\theta_R)
\right]
\left[
D_{s+}\mathscr P^+_{sL}
\right]
\mathscr P^+_{LR}.
}
$$

Reverse trace traversal：

$$
\boxed{
\left[
D_{L}^{\,2}\bar D_L^{\,2}
\delta^4(\theta_L-\theta_s)
\right]
\left[
D_R^{\,2}\bar D_R^{\,2}
\delta^4(\theta_R-\theta_L)
\right]
\delta^4(\theta_s-\theta_R),
}
$$

不能在 derivative transport 前与 forward word 合并。

---

## 5.3 $G_2^{BD}$

交换 $L\leftrightarrow R$ 的 action roles：

$$
s_{\phi_1}^B
\longrightarrow
(M_R)_{\widetilde\phi_1^B},
$$

$$
(M_R)_{\phi_1^X}
\longrightarrow
(M_L)_{\widetilde\phi_1^X},
$$

$$
s_u^A
\longrightarrow
(M_L)_{u^A}.
$$

输出：

$$
\boxed{
(B_1^D,D^E).
}
$$

Color word 仍是

$$
\boxed{
(T_E)^B{}_X(T_A)^X{}_D.
}
$$

Raw $D$-word：

$$
\boxed{
\mathfrak D_{G_2}^{BD}
=
\left[
\mathscr A_s\,
\delta^4(\theta_s-\theta_L)
\right]
\left[
D_{s+}\mathscr P^+_{sR}
\right]
\mathscr P^+_{RL}.
}
$$

两个 $G_2$ occurrences 的 pre-$D$ scalar 相同：

$$
\boxed{
-\frac{\hbar\sqrt2\,g^2}{2048}.
}
$$

但要比较

$$
c_{DB}\quad\text{与}\quad c_{BD},
$$

必须把 $D_+,\bar D_{\dot\alpha}$ 完整 transport 到两个不同 external endpoints，并固定：

$$
\{D_\alpha,\bar D_{\dot\alpha}\},
\qquad
\partial_{\alpha\dot\alpha}\leftrightarrow p_{\alpha\dot\alpha},
\qquad
T_0\leftrightarrow e^{\pm iw\cdot p}.
$$

这些正是尚未选定的 ledger：

```
BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED
```

因此此处不能生成 rank-two pole、rank-one terms、rank-zero finite term，也不能判断 numerator 是否真正产生 $4-d$。

---

# 6. `G32_G33_CC_DALGEBRA`

## 6.1 $G_{3,2}$

Vertices：

$$
I[u,\phi_1],
\qquad
M_2,
\qquad
H_{123}.
$$

Ports：

$$
s_u^A\longrightarrow(M_2)_{u^A},
$$

$$
s_{\phi_1}^B
\longrightarrow
H_{\widetilde\phi_1^B},
$$

$$
(M_2)_{\phi_2^X}
\longrightarrow
H_{\widetilde\phi_2^X}.
$$

Outputs：

$$
(M_2)_{\widetilde\phi_2^D}=C_2^D,
\qquad
H_{\widetilde\phi_3^E}=C_3^E.
$$

Flavor factor：

$$
\varepsilon_{123}=+1.
$$

Color word：

$$
\boxed{
(T_A)^D{}_Xc_{BXE}.
}
$$

Loop routing：

$$
e_{SM}^{V}:\ell,
\qquad
e_{MH}^{\Phi_2}:\ell-p,
\qquad
e_{HS}^{\Phi_1}:\ell-p-q.
$$

Exponent factors：

$$
+\frac{J_{AB}}{\hbar},
$$

$$
+\frac{\sqrt2g}{\hbar}(T_A)^D{}_X,
$$

$$
-\frac{\sqrt2g}{\hbar}c_{BXE}.
$$

Propagators：

$$
+\frac{\hbar}{\ell^2}
\delta^4(\theta_s-\theta_M),
$$

$$
-\frac{\hbar}{16(\ell-p)^2}
\mathscr P^+_{MH},
$$

$$
-\frac{\hbar}{16(\ell-p-q)^2}
\mathscr P^+_{sH}.
$$

Raw $D$-word：

$$
\boxed{
\mathfrak D_{G_{3,2}}
=
\left[
\mathscr A_s\delta^4(\theta_s-\theta_M)
\right]
\left[
D_{s+}\mathscr P^+_{sH}
\right]
\mathscr P^+_{MH}.
}
$$

Pre-$D$ scalar：

$$
\boxed{
+\frac{\hbar\sqrt2\,g^2}{2048}.
}
$$

---

## 6.2 $G_{3,3}$

Ports：

$$
s_u^A\longrightarrow(M_3)_{u^A},
$$

$$
s_{\phi_1}^B
\longrightarrow
H_{\widetilde\phi_1^B},
$$

$$
(M_3)_{\phi_3^X}
\longrightarrow
H_{\widetilde\phi_3^X}.
$$

Outputs：

$$
(M_3)_{\widetilde\phi_3^D}=C_3^D,
\qquad
H_{\widetilde\phi_2^E}=C_2^E.
$$

Flavor factor：

$$
\varepsilon_{132}=-1.
$$

Color word：

$$
\boxed{
(T_A)^D{}_Xc_{BXE}.
}
$$

Raw $D$-word 与 $G_{3,2}$ 完全相同，仅把 flavor $2\leftrightarrow3$。

Pre-$D$ scalar：

$$
\boxed{
-\frac{\hbar\sqrt2\,g^2}{2048}.
}
$$

因此在 triangle-parent sector 中严格有

$$
\boxed{
C_{G_{3,3}}^{\rm preD}
=
-C_{G_{3,2}}^{\rm preD}.
}
$$

不存在 dynamical-field Koszul sign：$\phi_r,\widetilde\phi_r,u$ 都是 even。唯一已固定的相对 sign 是 $\varepsilon_{132}=-\varepsilon_{123}$。

Antichiral vertex 的 $d^6\widetilde z\to d^8z$ projector normalization、Euclidean $D$-algebra 与 Fourier $i$-rule 尚未给出。因此不能从以上 raw word 严格产生 target 中的 $i\sqrt2$。

```
BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED
```

---

# 7. `OCCURRENCE_RESOLVED_CUT_LEDGER`

每个 cut 都使用

$$
K_eG_{e,\rm Wick}=+\hbar\mathbf1_e.
$$

没有任何 edge cut 自身产生 minus sign。Contact orbit 的相反 sign 来自 boxed resolvent 中

$$
-GV_{[1]}GI_{[1]},
\qquad
-GV_{[2]}GI_{[0]}.
$$

---

## 7.1 $G_1$

cut edge$K_eG_e$collapsed portsrequired matching occurrencesource–$G$, $V$$+\hbar\mathbf1_V$(I_{[1]}[u,\phi_1\bar u])source–$M_1$, $\Phi_1$$+\hbar\mathbf1_+$(I_{[1]}[u,u\bar\phi_1])$M_1$–$G$, $V$$+\hbar\mathbf1_V$(V_{[2]}[u,\widetilde\phi_1\bar u,\bar\phi_1])

三种 required field supports 都存在。

但 coefficient-by-coefficient pairing 依赖：

$$
\mathcal G_{abc},
\qquad
\mathbb A_{\rm ad}[u].
$$

因此 $G_1$ orbit 未闭合。

---

## 7.2 $G_2^{DB}$

Ports 回顾：

$$
S_{\phi_1}\to M_L,\qquad
M_L\to M_R,\qquad
M_R\to S_u.
$$

cut edge$K_eG_e$collapsed field supportmatching result$S_{\phi_1}$–$M_L$, $\Phi_1$$+\hbar\mathbf1_+$(I_{[1]}[u,\phi_1\bar u])$M_L$–$M_R$, $\Phi_1$$+\hbar\mathbf1_+$(V_{[2]}[u,\widetilde\phi_1\bar u,\bar\phi_1])$M_R$–$S_u$, $V$$+\hbar\mathbf1_V$(I_{[1]}[\phi_1,\widetilde\phi_1\bar\phi_1])

严格地，

$$
I_{[1];\phi\widetilde\phi|\bar\phi}=0
$$

不是因为 graph cancellation，而是因为 $\mathcal O_{AB_1}$ 不含任何 $\widetilde\phi$。

$G_2^{BD}$ 有完全相同的缺失 cut，只需交换 $L\leftrightarrow R$。

---

## 7.3 $G_{3,2}$

cut edge$K_eG_e$collapsed support requiredsource/action supportsource–$M_2$, $V$$+\hbar\mathbf1_V$(I_{[1]}[\phi_1,\phi_2C_2])source–$H$, $\Phi_1$$+\hbar\mathbf1_+$(I_{[1]}[u,\widetilde\phi_2C_3])$M_2$–$H$, $\Phi_2$$+\hbar\mathbf1_+$(V_{[2]}[u,\widetilde\phi_1C_2,C_3])

显式地，

$$
\operatorname{supp}I_{[1]}
=
\{u\phi_1|\bar u,\ uu|\bar\phi_1\}
$$

不含以上前两个 support。

而已给 quartic matter action

$$
\widetilde\phi_r u u\phi_r
$$

只有一个 antichiral flavor $r$，不能产生

$$
u\,\widetilde\phi_1\,C_2\,C_3.
$$

---

## 7.4 $G_{3,3}$

cut edge$K_eG_e$collapsed support requiredsource/action supportsource–$M_3$, $V$$+\hbar\mathbf1_V$(I_{[1]}[\phi_1,\phi_3C_3])source–$H$, $\Phi_1$$+\hbar\mathbf1_+$(I_{[1]}[u,\widetilde\phi_3C_2])$M_3$–$H$, $\Phi_3$$+\hbar\mathbf1_+$(V_{[2]}[u,\widetilde\phi_1C_3,C_2])

因此当前 `LOCAL_PROPOSAL_AB1_ORDERED_SOURCE` 的 four-class resolvent **并不包含 $CC$ triangle 的 Schwinger-cut/contact orbit**。

缺少的不是一个 numerical factor，而是新的 Hessian field supports。它们应来自 $\nabla_-$-descendant/EOM source sector，而不是未变换的 $A_cB_{1,c}$ source。

最小 blocking token 是

```
BLOCKED_DESCENDANT_CONTACT_HESSIANS_UNSPECIFIED
```

---

## 7.5 Q4S residue status

因为 complete $D$-word 尚未 reduction，当前没有得到任何确定的 tensor numerator

$$
N^{\mu\nu}\ell_\mu\ell_\nu,
\qquad
N^\mu\ell_\mu,
\qquad
N_0.
$$

因此也没有得到

$$
g_{\mu\nu}N^{\mu\nu}
=
\widehat g_{\mu\nu}N^{\mu\nu}
+
\breve g_{\mu\nu}N^{\mu\nu}.
$$

特别地，不能声称某个 occurrence 已产生

$$
4-(4-2\epsilon)=2\epsilon.
$$

故 verified elementary factor

$$
\frac1{32\pi^2}
$$

在本 gate 中没有乘到任何 graph 上。

---

# 8. Project coefficient vector before opening HT

当前数据不能产生 numerical vector

$$
(c_{DB},c_{BD},c_{32},c_{23}).
$$

原因有三层，且第一层已经足够 blocking：

1. $G_2$ 有一个 vector-edge cut 要求
$$
I_{[1]}[\phi_1,\widetilde\phi_1|\bar\phi_1],
$$
该 Hessian 不存在。
2. $G_{3,2},G_{3,3}$ 的全部三个 cut supports 均不在当前 source/action orbit 中。
3. 即使补充这些 contacts，$G_1$ 仍缺 ordered $VVV$ superkernel，所有 sectors 仍缺 Fourier/DRED derivative ledger。

因此

$$
\boxed{
(c_{DB},c_{BD},c_{32},c_{23})_{\rm Project}
\quad\text{is not defined by the supplied gate}.
}
$$

唯一在 triangle-parent level 已严格得到的 coefficient relation 是

$$
\boxed{
c_{32}^{\rm triangle}
+
c_{23}^{\rm triangle}
=
0.
}
$$

这里按用户给定 vector ordering，

$$
c_{32}:\ (C_3,C_2),
\qquad
c_{23}:\ (C_2,C_3).
$$

其 absolute magnitude 与 Euclidean phase 未固定。

```
BLOCKED_DESCENDANT_CONTACT_HESSIANS_UNSPECIFIED
```

---

# 9. Project versus external target

现在才打开 external target：

$$
(c_{DB},c_{BD},c_{32},c_{23})_{\rm HT}
=
(1,1,i\sqrt2,-i\sqrt2).
$$

relationProject derivation gateHT targetcomparison$c_{DB}=c_{BD}$未固定true不能比较$c_{32}+c_{23}=0$triangle-parent sector 中严格成立truerelative flavor antisymmetry agrees$c_{32}=i\sqrt2$未固定$i\sqrt2$不能 target-fit$c_{23}=-i\sqrt2$未固定$-i\sqrt2$不能 target-fitcommon loop normalization未形成 $4-d$ numeratorHT 已归入 normalization$1/(32\pi^2)$ 未使用ordered $BD/DB$ towerFourier/link transport 未固定equal zero-shift coefficients未建立

因此本 correction gate 的严格结果是：

$$
\boxed{
c_{32}^{\rm triangle}
=
-c_{23}^{\rm triangle},
}
$$

而 numerical Project vector 仍被

```
BLOCKED_DESCENDANT_CONTACT_HESSIANS_UNSPECIFIED
```

阻断；用 HT vector 补入缺失 coefficients 会违反“ordinary-supergraph calculation first”的要求。

