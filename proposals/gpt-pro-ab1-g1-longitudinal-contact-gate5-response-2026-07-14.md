## 记号

$$
\kappa:=\frac{\eta}{512}.
$$

$T_i$ 表示第 $i$ 个 labeled gauge field 的 color generator；$(T_iT_j)^A$ 是矩阵乘积 $T_iT_j$ 在基 $T_A$ 上的分量。定义 invariant color $3$-form

$$
C_{ijk}:=
f_{AB}\Big[(T_iT_j)^A-(T_jT_i)^A\Big](T_k)^B
=
f_{AB}(T_i)^A\Big[(T_jT_k)^B-(T_kT_j)^B\Big].
$$

由 $f$ 的 ad-invariance，

$$
C_{\pi1\,\pi2\,\pi3}=\operatorname{sgn}(\pi)C_{123}.
$$

定义 chiral differential words

$$
Q^+_{ij}:=\bar D^2(u_iD^au_j),\qquad
L^+_k:=\bar D^2D_au_k,
$$

其中 Lorentz/spinor index $a$ 在乘积中收缩。Antichiral words 记作

$$
Q^-_{ij}:=(Q^+_{ij})^\dagger,\qquad
L^-_k:=(L^+_k)^\dagger,
$$

并保持 Hermitian conjugation 所确定的 operator order。

$\rho=(\chi,\pi,w)$ 表示一个 row，其中 $\chi=\pm$ 是 chirality，$\pi\in S_3$，$w\in\{QL,LQ\}$。

对 homogeneous polynomial $P$，其 labeled polarization 定义为

$$
\operatorname{Pol}_nP[u_1,\ldots,u_n]
:=
\left.
\frac{\partial^n}{\partial t_1\cdots\partial t_n}
P\!\left(\sum_{i=1}^nt_iu_i\right)
\right|_{t_i=0}.
$$

后面 source 展开使用

$$
X_i:=Du_i,\qquad
H_i:=\bar D^2X_i,\qquad
K_i:=D\bar D^2X_i,\qquad
P:=D\phi_1 .
$$

为避免与 resolvent $R_1,\ldots,R_4$ 混淆，edgewise numerator 写成 $\mathcal R_{\alpha,e}$。

---

# 1. 四个 raw cubic gauge words

条件 $p+q+r+s=1$ 只有四种可能。各项 denominator 逐项为

$$
\begin{array}{c|c|c|c}
(p,q,r,s)&(-1)^{p+r}&(p+q+1)(r+s+1)&\text{coefficient}\\
\hline
(1,0,0,0)&-1&2&-\eta/512\\
(0,1,0,0)&+1&2&+\eta/512\\
(0,0,1,0)&-1&2&-\eta/512\\
(0,0,0,1)&+1&2&+\eta/512
\end{array}
$$

因此

$$
\boxed{
\begin{aligned}
W_p^+
&=-\kappa f_{AB}\int_+
 [\bar D^2(VD^aV)]^A[\bar D^2D_aV]^B,\\
W_q^+
&=+\kappa f_{AB}\int_+
 [\bar D^2(D^aVV)]^A[\bar D^2D_aV]^B,\\
W_r^+
&=-\kappa f_{AB}\int_+
 [\bar D^2D^aV]^A[\bar D^2(VD_aV)]^B,\\
W_s^+
&=+\kappa f_{AB}\int_+
 [\bar D^2D^aV]^A[\bar D^2(D_aVV)]^B.
\end{aligned}}
$$

Antichiral sector 是逐项的 exact conjugate：

$$
W_\bullet^-:=(W_\bullet^+)^\dagger,\qquad
\kappa^-:=\kappa^\dagger .
$$

## Labeled differentiation：尚未使用 color antisymmetry

对每个 $\pi\in S_3$：

$$
\begin{aligned}
\operatorname{Pol}_3W_p^+
&=
-\kappa
\sum_{\pi}
f_{AB}(T_{\pi1}T_{\pi2})^A(T_{\pi3})^B
Q^+_{\pi1\pi2}L^+_{\pi3},\\
\operatorname{Pol}_3W_q^+
&=
+\kappa
\sum_{\pi}
f_{AB}(T_{\pi2}T_{\pi1})^A(T_{\pi3})^B
Q^+_{\pi1\pi2}L^+_{\pi3},\\
\operatorname{Pol}_3W_r^+
&=
-\kappa
\sum_{\pi}
f_{AB}(T_{\pi1})^A(T_{\pi2}T_{\pi3})^B
L^+_{\pi1}Q^+_{\pi2\pi3},\\
\operatorname{Pol}_3W_s^+
&=
+\kappa
\sum_{\pi}
f_{AB}(T_{\pi1})^A(T_{\pi3}T_{\pi2})^B
L^+_{\pi1}Q^+_{\pi2\pi3}.
\end{aligned}
$$

现在分别合并 $p,q$ 与 $r,s$：

$$
\begin{aligned}
\operatorname{Pol}_3(W_p^++W_q^+)
&=
-\kappa\sum_{\pi}
C_{\pi1\pi2\pi3}
Q^+_{\pi1\pi2}L^+_{\pi3},\\
\operatorname{Pol}_3(W_r^++W_s^+)
&=
-\kappa\sum_{\pi}
C_{\pi1\pi2\pi3}
L^+_{\pi1}Q^+_{\pi2\pi3}.
\end{aligned}
$$

故

$$
\boxed{
\mathcal V_{VVV}^+
=
\sum_{\pi\in S_3}c^+_{\pi1\pi2\pi3}
\left[
Q^+_{\pi1\pi2}L^+_{\pi3}
+
L^+_{\pi1}Q^+_{\pi2\pi3}
\right],
}
$$

其中

$$
\boxed{
c^+_{ijk}=-\frac{\eta}{512}C_{ijk}.
}
$$

Antichiral sector：

$$
\boxed{
\mathcal V_{VVV}^-=(\mathcal V_{VVV}^+)^\dagger,\qquad
c^-_{ijk}:=(c^+_{ijk})^\dagger .
}
$$

这正是每 chirality 的

$$
6\times\{QL,LQ\}=12
$$

个 labeled rows。

---

# 2. 全部 $24$ rows：$A$-mark、$B$-mark、$L_A$ 分离

定义

$$
c_\chi:=c^\chi_{123},
\qquad
L_{A,\rho}:=
-\frac12D_+\bar D^2D^2(\mathcal V_\rho),
$$

其中 $\mathcal V_\rho$ 包括该 row 的 color coefficient。

## Chiral $+$ sector

| $\rho$ | $\pi$ | word | coefficient | $F_{A,\rho}$ | $F_{B,\rho}$ |
| --- | --- | --- | --- | --- | --- |
| 1 | 123 | $Q^+_{12}L^+_3$ | $+c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 2 | 123 | $L^+_1Q^+_{23}$ | $+c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 3 | 132 | $Q^+_{13}L^+_2$ | $-c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 4 | 132 | $L^+_1Q^+_{32}$ | $-c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 5 | 213 | $Q^+_{21}L^+_3$ | $-c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 6 | 213 | $L^+_2Q^+_{13}$ | $-c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 7 | 231 | $Q^+_{23}L^+_1$ | $+c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 8 | 231 | $L^+_2Q^+_{31}$ | $+c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 9 | 312 | $Q^+_{31}L^+_2$ | $+c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 10 | 312 | $L^+_3Q^+_{12}$ | $+c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 11 | 321 | $Q^+_{32}L^+_1$ | $-c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 12 | 321 | $L^+_3Q^+_{21}$ | $-c_+$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |

## Antichiral $-$ sector

| $\rho$ | $\pi$ | word | coefficient | $F_{A,\rho}$ | $F_{B,\rho}$ |
| --- | --- | --- | --- | --- | --- |
| 13 | 123 | $Q^-_{12}L^-_3$ | $+c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 14 | 123 | $L^-_1Q^-_{23}$ | $+c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 15 | 132 | $Q^-_{13}L^-_2$ | $-c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 16 | 132 | $L^-_1Q^-_{32}$ | $-c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 17 | 213 | $Q^-_{21}L^-_3$ | $-c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 18 | 213 | $L^-_2Q^-_{13}$ | $-c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 19 | 231 | $Q^-_{23}L^-_1$ | $+c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 20 | 231 | $L^-_2Q^-_{31}$ | $+c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 21 | 312 | $Q^-_{31}L^-_2$ | $+c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 22 | 312 | $L^-_3Q^-_{12}$ | $+c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 23 | 321 | $Q^-_{32}L^-_1$ | $-c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |
| 24 | 321 | $L^-_3Q^-_{21}$ | $-c_-$ | $L_{A,\rho}-8\bar r_2^2\mathcal R_{A,\rho}$ | $-8\bar r_0^2\mathcal R_{B,\rho}$ |

因此逐 row：

$$
\boxed{
F_{A,\rho}-L_{A,\rho}
=-8\bar r_2^2\mathcal R_{A,\rho},
\qquad
F_{B,\rho}
=-8\bar r_0^2\mathcal R_{B,\rho}.
}
$$

在给定测试点，

$$
r_0=(2,1,-1,3),\quad
r_1=(1,1,-1,3),\quad
r_2=(1,1,-1,2),
$$

所以

$$
\bar r_0^2=4+1+1+9=15,
$$

$$
\bar r_1^2=1+1+1+9=12,
$$

$$
\bar r_2^2=1+1+1+4=7.
$$

故所有 nonzero $A$-marked rows 满足

$$
\boxed{
\frac{F_{A,\rho}-L_{A,\rho}}
{\mathcal R_{A,\rho}}
=-8\cdot7=-56.
}
$$

相应 nonzero $B$-marked rows 满足

$$
\boxed{
\frac{F_{B,\rho}}{\mathcal R_{B,\rho}}
=-8\cdot15=-120.
}
$$

---

# 3. Source Hessian grading 与全部可导出的 local words

令 source functional

$$
\mathcal J^{AB}=g^2A\,B_1.
$$

首先

$$
g^2A_1B_{11}
=
-\frac{g^2\sqrt2}{8}
D\bar D^2(Du)\,D\phi_1
=
-\frac{g^2}{4\sqrt2}
D\bar D^2(Du)\,D\phi_1,
$$

正好是所给 physical insertion。

## 3.1 Resolvent grading 强制确定 $I_{[n]}$ 的含义

由

$$
\mathscr G
=
\left(
\mathscr G_0^{-1}
+V_{[1]}+V_{[2]}+\cdots
\right)^{-1},
$$

二阶 background degree 为

$$
\begin{aligned}
(\mathscr GI)_{[2]}
={}&
\mathscr G_0I_{[2]}
-\mathscr G_0V_{[1]}\mathscr G_0I_{[1]}\\
&-\mathscr G_0V_{[2]}\mathscr G_0I_{[0]}
+\mathscr G_0V_{[1]}\mathscr G_0V_{[1]}
 \mathscr G_0I_{[0]}.
\end{aligned}
$$

所以 bracket index 必须是 background Taylor degree。于是

$$
\boxed{
\begin{aligned}
\mathcal J_{(2)}^{AB}
&=g^2A_1B_{11},\\
\mathcal J_{(3)}^{AB}
&=g^2(A_2B_{11}+A_1B_{12}),\\
\mathcal J_{(4)}^{AB}
&=g^2(A_3B_{11}+A_2B_{12}+A_1B_{13}).
\end{aligned}}
$$

相应地，

$$
I_{[0]}\longleftarrow\mathcal J_{(2)},\qquad
I_{[1]}\longleftarrow\mathcal J_{(3)},\qquad
I_{[2]}\longleftarrow\mathcal J_{(4)}.
$$

这已经显示：由给定 $A_1,A_2,B_{11},B_{12}$ 可完整得到 $I_{[0]},I_{[1]}$，但只能得到 $I_{[2]}$ 的 $A_2B_{12}$ sector。

---

## 3.2 $A_2$ 的 exact two-label polarization

$$
\boxed{
\begin{aligned}
A_2[u_1,u_2]
={}&-\frac18D\bar D^2
\Big(
X_1u_2+X_2u_1-u_1X_2-u_2X_1
\Big)\\
&-\frac14
\Big(
X_1H_2+X_2H_1+H_1X_2+H_2X_1
\Big).
\end{aligned}}
$$

它满足

$$
A_2[u,u]_{\rm polarized}=2A_2[u].
$$

因此完整 trilinear source polarization 为

$$
\boxed{
\begin{aligned}
\mathcal J_{(3)}^{AB}[u_1,u_2,\phi_1]
=g^2\Big[
&A_2[u_1,u_2]P\\
&+A_1[u_1]B_{12}[u_2,\phi_1]
+A_1[u_2]B_{12}[u_1,\phi_1]
\Big].
\end{aligned}}
$$

---

## 3.3 十二个 $I_{[1]}$ local source words

表中 $a_k$ 是 source local coefficient；$R_2$ 的 overall sign 为 $-1$，故 resolvent coefficient 为 $-a_k$。Marked inverse-kernel orientation sign 尚未包含在这一列。

| $k$ | $a_k$ | $AB$ local word | $BA$ local word | $AB$ edge | $BA$ reflected edge |
| --- | --- | --- | --- | --- | --- |
| 1 | $-1/8$ | $D\bar D^2(X_1u_2)P$ | $P\,D\bar D^2(X_1u_2)$ | $r_2$ | $r_0$ |
| 2 | $-1/8$ | $D\bar D^2(X_2u_1)P$ | $P\,D\bar D^2(X_2u_1)$ | $r_2$ | $r_0$ |
| 3 | $+1/8$ | $D\bar D^2(u_1X_2)P$ | $P\,D\bar D^2(u_1X_2)$ | $r_2$ | $r_0$ |
| 4 | $+1/8$ | $D\bar D^2(u_2X_1)P$ | $P\,D\bar D^2(u_2X_1)$ | $r_2$ | $r_0$ |
| 5 | $-1/4$ | $X_1H_2P$ | $P\,X_1H_2$ | $r_2$ | $r_0$ |
| 6 | $-1/4$ | $X_2H_1P$ | $P\,X_2H_1$ | $r_2$ | $r_0$ |
| 7 | $-1/4$ | $H_1X_2P$ | $P\,H_1X_2$ | $r_2$ | $r_0$ |
| 8 | $-1/4$ | $H_2X_1P$ | $P\,H_2X_1$ | $r_2$ | $r_0$ |
| 9 | $-1/4$ | $K_1X_2\phi_1$ | $X_2\phi_1K_1$ | $r_0$ | $r_2$ |
| 10 | $+1/4$ | $K_1\phi_1X_2$ | $\phi_1X_2K_1$ | $r_0$ | $r_2$ |
| 11 | $-1/4$ | $K_2X_1\phi_1$ | $X_1\phi_1K_2$ | $r_0$ | $r_2$ |
| 12 | $+1/4$ | $K_2\phi_1X_1$ | $\phi_1X_1K_2$ | $r_0$ | $r_2$ |

因此 AB orientation 的 $R_2$ contact classes 为

$$
\boxed{
\begin{aligned}
\mathcal C^{AB}_{A,k}
&:
\quad k=1,\ldots,8,\quad
e=2,\quad
\text{local coefficient}=-a_k,\\
\mathcal C^{AB}_{B,k}
&:
\quad k=9,\ldots,12,\quad
e=0,\quad
\text{local coefficient}=-a_k.
\end{aligned}}
$$

其 triangle-side numerator 必须具有 tagged form

$$
\bar r_2^2\mathcal R_{A,k}
\quad\text{或}\quad
\bar r_0^2\mathcal R_{B,k}.
$$

BA orientation 独立地给出 reversed words；geometric reflection 交换 source-adjacent edges：

$$
r_0\longleftrightarrow r_2.
$$

---

## 3.4 $R_3$ 所需的 raw $V_{[2]}$

定义

$$
W_{pqrs}:=
[\bar D^2(V^pD^aVV^q)]^A
[\bar D^2(V^rD_aVV^s)]^B .
$$

$p+q+r+s=2$ 的全部十个 raw terms 为

$$
S^{{\rm g}}_{+,4}
=
\frac{\eta f_{AB}}{256}\int_+
\sum_{p+q+r+s=2}
\beta_{pqrs}W_{pqrs},
$$

其中

| $(p,q,r,s)$ | $\beta_{pqrs}$ | raw word |
| --- | --- | --- |
| $(2,0,0,0)$ | $+1/6$ | $\bar D^2(V^2D^aV)\,\bar D^2D_aV$ |
| $(0,2,0,0)$ | $+1/6$ | $\bar D^2(D^aVV^2)\,\bar D^2D_aV$ |
| $(0,0,2,0)$ | $+1/6$ | $\bar D^2D^aV\,\bar D^2(V^2D_aV)$ |
| $(0,0,0,2)$ | $+1/6$ | $\bar D^2D^aV\,\bar D^2(D_aVV^2)$ |
| $(1,1,0,0)$ | $-1/3$ | $\bar D^2(VD^aVV)\,\bar D^2D_aV$ |
| $(0,0,1,1)$ | $-1/3$ | $\bar D^2D^aV\,\bar D^2(VD_aVV)$ |
| $(1,0,1,0)$ | $+1/4$ | $\bar D^2(VD^aV)\,\bar D^2(VD_aV)$ |
| $(1,0,0,1)$ | $-1/4$ | $\bar D^2(VD^aV)\,\bar D^2(D_aVV)$ |
| $(0,1,1,0)$ | $-1/4$ | $\bar D^2(D^aVV)\,\bar D^2(VD_aV)$ |
| $(0,1,0,1)$ | $+1/4$ | $\bar D^2(D^aVV)\,\bar D^2(D_aVV)$ |

每个 raw word 的 labeled polarization 由 $\pi\in S_4$ 填充其四个 ordered $V$-slots，故在使用 color relations 前共有

$$
10\times24=240
$$

个 raw labeled words per chirality。

它们对应内部 action-action contact：

$$
\boxed{
R_3:
\qquad
e=1,\qquad
\text{resolvent sign}=-1,\qquad
\text{pre-contact numerator}
=\bar r_1^2\mathcal R_{pqrs,\pi}.
}
$$

---

## 3.5 可确定的 $R_1$ mixed sector

由给定 source words 能确定

$$
\boxed{
\begin{aligned}
\mathcal J^{AB}_{(4),{\rm mix}}
[u_1,u_2,u_3,\phi_1]
={}&g^2
\sum_{\{i,j\}\sqcup\{k\}=\{1,2,3\}}
A_2[u_i,u_j]\,
\sqrt2(X_k\phi_1-\phi_1X_k),\\
\mathcal J^{BA}_{(4),{\rm mix}}
[u_1,u_2,u_3,\phi_1]
={}&g^2
\sum_{\{i,j\}\sqcup\{k\}=\{1,2,3\}}
\sqrt2(X_k\phi_1-\phi_1X_k)\,
A_2[u_i,u_j].
\end{aligned}}
$$

令 $W_m(i,j)$, $m=1,\ldots,8$，依次表示 $A_2[u_i,u_j]$ 中表 3.3 的前八个 differential words，系数为

$$
(a_1,\ldots,a_8)
=
\left(
-\frac18,-\frac18,
+\frac18,+\frac18,
-\frac14,-\frac14,-\frac14,-\frac14
\right).
$$

则全部 $48$ 个 known $AB$ quartic words 为

$$
\boxed{
\begin{aligned}
W_m(i,j)X_k\phi_1
&\quad\text{with coefficient}\quad
+\sqrt2\,a_m,\\
W_m(i,j)\phi_1X_k
&\quad\text{with coefficient}\quad
-\sqrt2\,a_m,
\end{aligned}}
$$

其中有 $3$ 种 partition $\{i,j\}\sqcup\{k\}$，故

$$
3\times8\times2=48.
$$

BA words 是完全独立的 reversed products：

$$
X_k\phi_1W_m(i,j),
\qquad
\phi_1X_kW_m(i,j).
$$

Labeled backgrounds $u_1,u_2$ 时没有额外 $1/2$。在 diagonal Taylor expansion 中，

$$
I_{[2]}[\bar u,\bar u]
=
\frac12
\operatorname{Pol}_2I[\bar u,\bar u].
$$

因此两个 ordered transport paths

$$
(2\rightarrow0),\qquad(0\rightarrow2)
$$

共同组成同一个 diagonal $A_2B_{12}$ Taylor coefficient。

---

# 4. Edgewise Schwinger subtraction：逐 edge 的 exact identity

对任意 occurrence $\alpha$ 和其 tagged edge $e$，有

$$
D_e=r_{e,d}^2.
$$

因此

$$
\frac{\mathcal R_{\alpha,e}}
{\prod_{j\neq e}D_j}
=
\frac{D_e\mathcal R_{\alpha,e}}
{D_0D_1D_2}
=
\frac{r_{e,d}^2\mathcal R_{\alpha,e}}
{D_0D_1D_2}.
$$

故

$$
\boxed{
\frac{r_{e,d}^2\mathcal R_{\alpha,e}}
{D_0D_1D_2}
-
\frac{\mathcal R_{\alpha,e}}
{\prod_{j\neq e}D_j}
=0.
}
$$

三个 edge 分别为

$$
\frac{r_{0,d}^2\mathcal R_{\alpha,0}}{D_0D_1D_2}
-\frac{\mathcal R_{\alpha,0}}{D_1D_2}=0,
$$

$$
\frac{r_{1,d}^2\mathcal R_{\alpha,1}}{D_0D_1D_2}
-\frac{\mathcal R_{\alpha,1}}{D_0D_2}=0,
$$

$$
\frac{r_{2,d}^2\mathcal R_{\alpha,2}}{D_0D_1D_2}
-\frac{\mathcal R_{\alpha,2}}{D_0D_1}=0.
$$

只有在这个 edgewise contact subtraction 完成后，才作

$$
\bar r_e^2-r_{e,d}^2=\mu_\ell^2.
$$

于是

$$
\boxed{
\frac{\bar r_e^2\mathcal R_{\alpha,e}}
{D_0D_1D_2}
-
\frac{\mathcal R_{\alpha,e}}
{\prod_{j\neq e}D_j}
=
\frac{\mu_\ell^2\mathcal R_{\alpha,e}}
{D_0D_1D_2}.
}
$$

由于 $p,q$ 没有 evanescent components，

$$
\mu_{r_0}^2=\mu_{r_1}^2=\mu_{r_2}^2=\mu_\ell^2.
$$

没有使用 global four-dimensional metric trace。

---

# 5. 若 contact 后仍有 inverse-kernel square

若一个已 collapse 的 marked numerator 仍含 $\bar r_f^2$，保持新的 edge tag $f$。对当前 active denominator set $E$：

$$
\boxed{
\frac{\bar r_f^2\mathcal N}
{\prod_{j\in E}D_j}
-
\frac{\mathcal N}
{\prod_{j\in E\setminus\{f\}}D_j}
=
\frac{\mu_\ell^2\mathcal N}
{\prod_{j\in E}D_j}.
}
$$

这里第二项只能由同一个 oriented inverse-kernel block 的 Schwinger contact 给出；不能把 $\bar r_f^2$ 替换成无标记的 tensor trace。

---

# 6. Final residue integrals 与 rank-one simplex moments

给定

$$
I_0:=
\lim_{\epsilon\to0}
\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2}{D_0D_1D_2}
=
\frac1{32\pi^2}.
$$

使用 Feynman parameters

$$
x_0+x_1+x_2=1,\qquad x_i\ge0,
$$

有

$$
\frac1{D_0D_1D_2}
=
2\int_{\Delta_2}
\frac{dx_1dx_2}
{\big[(\ell-P_x)^2+\Delta(x)\big]^3},
$$

其中

$$
P_x=x_1p+x_2(p+q),
$$

$$
\Delta(x)
=x_0x_1p^2+x_1x_2q^2+x_0x_2(p+q)^2.
$$

Simplex moments 为

$$
\int_{\Delta_2}dx_1dx_2=\frac12,
$$

$$
\int_{\Delta_2}x_0\,dx_1dx_2
=
\int_{\Delta_2}x_1\,dx_1dx_2
=
\int_{\Delta_2}x_2\,dx_1dx_2
=
\frac16.
$$

因此 normalized moments 为

$$
\langle x_0\rangle
=\langle x_1\rangle
=\langle x_2\rangle
=\frac13.
$$

令 $\ell=k+P_x$。Odd $k^\mu$ integral 为零，于是

$$
\boxed{
\lim_{\epsilon\to0}
\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2\,\bar\ell^\mu}{D_0D_1D_2}
=
\frac{2p^\mu+q^\mu}{96\pi^2}.
}
$$

进而

$$
\boxed{
\begin{aligned}
\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2\,\bar r_0^\mu}{D_0D_1D_2}
\Bigg|_{\epsilon\to0}
&=
\frac{2p^\mu+q^\mu}{96\pi^2},\\[2mm]
\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2\,\bar r_1^\mu}{D_0D_1D_2}
\Bigg|_{\epsilon\to0}
&=
\frac{q^\mu-p^\mu}{96\pi^2},\\[2mm]
\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2\,\bar r_2^\mu}{D_0D_1D_2}
\Bigg|_{\epsilon\to0}
&=
-\frac{p^\mu+2q^\mu}{96\pi^2}.
\end{aligned}}
$$

因此对于 affine rank-one numerator

$$
\mathcal R_{\alpha,e}
=
a_{\alpha,e}
+b_{\alpha,e,\mu}\bar r_e^\mu,
$$

其 residue 为

$$
\boxed{
\begin{aligned}
e=0:\quad&
\frac{a_{\alpha,0}}{32\pi^2}
+
\frac{b_{\alpha,0}\cdot(2p+q)}{96\pi^2},\\
e=1:\quad&
\frac{a_{\alpha,1}}{32\pi^2}
+
\frac{b_{\alpha,1}\cdot(q-p)}{96\pi^2},\\
e=2:\quad&
\frac{a_{\alpha,2}}{32\pi^2}
-
\frac{b_{\alpha,2}\cdot(p+2q)}{96\pi^2}.
\end{aligned}}
$$

---

# 7. 第一个缺失的 local object；ordered coefficients 的状态

要把

$$
L_A=-\frac12D_+\bar D^2D^2(\mathcal V_{VVV})
$$

真正 integrate by parts 成为上述 $R_2/R_3/R_1$ local kernels，首先需要的、但未给出的 object 是 **marked oriented free inverse-kernel contact identity**

$$
\boxed{
\left(D_+\bar D^2D^2\right)_z
\mathscr G_{0,\chi}^{XY}(z,z';r_e)
=
\sigma_{\chi,XY,e}\,
N_{\chi,XY}\,
r_{e,d}^2\,
\mathcal P_{\chi,XY}
\delta^4(\theta-\theta').
}
$$

还必须给出其 right-acting counterpart。这里必须明确：

$$
(X,Y),\quad
\chi,\quad
e,\quad
\sigma_{\chi,XY,e},\quad
N_{\chi,XY},\quad
\mathcal P_{\chi,XY}.
$$

没有这个 kernel，不能决定：

$$
\text{IBP sign},\qquad
\text{left/right contact},\qquad
\text{field-block contraction},\qquad
\mathcal R_{\alpha,e}.
$$

即使该 inverse-kernel identity 被补充，$R_1$ 仍不完整，因为

$$
\boxed{
I_{[2]}
\ \text{还需要}\
A_3B_{11}+A_1B_{13}.
}
$$

确切地，任取一个 local cubic deformation $\Delta A_3$，它不改变题中给出的

$$
A_1,\ A_2,\ B_{11},\ B_{12},
$$

也不改变上面的 $24$ 个 cubic gauge rows，但它改变

$$
\Delta I_{[2]}
=
\delta^2\!\left[g^2\Delta A_3B_{11}\right]_{[2]},
$$

从而改变

$$
\Delta R_1
=
\mathscr G_0\Delta I_{[2]}.
$$

同理，任意 $\Delta B_{13}$ 也改变 $R_1$。

因此当前输入唯一确定的是：

$$
\boxed{
\begin{gathered}
\text{四个 raw cubic words},\\
12+12\text{ labeled gauge rows},\\
A_2B_{11}\text{ 与 }A_1B_{12}\text{ 的全部 }R_2\text{ local words},\\
V_{[2]}\text{ 的十个 raw }R_3\text{ sectors},\\
A_2B_{12}\text{ 的 }48\text{ 个 known }R_1\text{ mixed words},\\
\text{edgewise }\mu_\ell^2\text{ residues and exact rank-one moments}.
\end{gathered}}
$$

但两个 ordered integrated coefficients

$$
\boxed{
C^{AB}_{G_1},
\qquad
C^{BA}_{G_1}
}
$$

不能由当前 displayed input 唯一确定；因此不能在此阶段封闭，也不能进行 HT comparison。
