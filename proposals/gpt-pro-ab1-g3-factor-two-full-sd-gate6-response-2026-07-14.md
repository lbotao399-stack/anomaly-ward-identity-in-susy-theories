## 0. 记号

$$
d=4-2\epsilon,\qquad
D_e:=r_{e,d}^{\,2},\qquad
r_0=\ell,\quad r_1=\ell-p,\quad r_2=\ell-p-q.
$$

$$
\bar r_e^{\,2}=r_{e,d}^{\,2}+\mu_\ell^2=D_e+\mu_\ell^2.
$$

定义 routed numerator

$$
\mathcal W_0:=W_{12},\qquad
\mathcal W_1:=W_{P0},\qquad
\mathcal W_2:=W_{p0}.
$$

这里 $\mathcal W_e$ 包括 endpoint、momentum routing 和 ordered color word；不能把三个 untagged $W$ 当作同一 polynomial。

定义 trace/metric reconstruction factor $\chi$：

$$
32768
\left(\frac14\right)
\left(\frac12\right)
\left(-\frac12\right)\chi
=-2048\chi.
$$

旧计算使用 $\chi=2$。下面不预设 $\chi$。

---

# 1. Primitive scalar normalization

## 1.1 Canonical rescaling

Project conventions 给出

$$
h=g^{-2},
$$

以及 Euclidean matter action 和 cubic superpotentials。

取 canonical quantum fields

$$
V=\sqrt2\,g\,u,\qquad
\Phi_r=g\phi_r,\qquad
\widetilde\Phi_r=g\widetilde\phi_r.
$$

### Matter vertex

$n=1$ matter term 为

$$
S_{E,M}^{(3)}
=-h\int_8\widetilde\Phi_r\,V^Y T_Y\,\Phi_r.
$$

因此

$$
\begin{aligned}
S_{E,M}^{(3)}
&=-g^{-2}(g)(\sqrt2 g)(g)
\int_8\widetilde\phi_r\,u^YT_Y\,\phi_r\\
&=-\sqrt2 g
\int_8\widetilde\phi_r\,u^YT_Y\,\phi_r .
\end{aligned}
$$

Euclidean exponent 是 $e^{-S_E/\hbar}$。  因而

$$
-\frac1\hbar S_{E,M}^{(3)}
=
+\frac{\sqrt2 g}{\hbar}
\int_8\widetilde\phi_r\,u^YT_Y\,\phi_r,
$$

所以 stripping off $T_Y=i\,c_Y$ 后，

$$
\boxed{C_M=\frac{\sqrt2 g}{\hbar}}.
$$

Matter exponential 的 $n=1$ Taylor factor 是

$$
\frac1{1!}=1,
$$

没有 $1/2$。其 all-order $1/n!$ normalization 见 Project primitive rule。

---

### Antichiral $H_-$ vertex

Euclidean antichiral cubic action 为

$$
S_{E,H_-}^{(3)}
=
+\frac{\sqrt2}{6g^2}
\int_-
\varepsilon_{rst}c_{ABC}
\widetilde\Phi_r^A\widetilde\Phi_s^B\widetilde\Phi_t^C.
$$

Canonical rescaling 后

$$
S_{E,H_-}^{(3)}
=
+\frac{\sqrt2 g}{6}
\int_-
\varepsilon_{rst}c_{ABC}
\widetilde\phi_r^A\widetilde\phi_s^B\widetilde\phi_t^C,
$$

所以 exponent vertex 是

$$
-\frac1\hbar S_{E,H_-}^{(3)}
=
-\frac{\sqrt2 g}{6\hbar}
\int_-
\varepsilon_{rst}c_{ABC}
\widetilde\phi_r^A\widetilde\phi_s^B\widetilde\phi_t^C.
$$

对三个 labeled legs differentiation：

$$
\begin{aligned}
&\frac1{3!}
\sum_{\sigma\in S_3}
\varepsilon_{r_{\sigma1}r_{\sigma2}r_{\sigma3}}
c_{A_{\sigma1}A_{\sigma2}A_{\sigma3}}
\\
&=
\frac1{6}
\sum_{\sigma\in S_3}
(\operatorname{sgn}\sigma)^2
\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}
\\
&=
\frac16(6)
\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
\end{aligned}
$$

因此

$$
\boxed{C_{H_-}=-\frac{\sqrt2 g}{\hbar}}.
$$

没有剩余 $1/3!$。Project 的 labeled cubic primitive 正是 antisymmetric flavor/color tensor。

---

## 1.2 Source mixed-Hessian factorial

令

$$
A[u]:=D_+\bar D^2D_+u,\qquad
B[\phi_1]:=D_+\phi_1.
$$

则

$$
I[tu,s\phi_1]
=
ts\,C_I\,A[u]B[\phi_1],
\qquad
C_I=-\frac{g^2}{4\sqrt2}.
$$

Mixed Taylor Hessian 是

$$
\begin{aligned}
I_{[u,\phi]}
&=
\frac1{2!}
\left(
\partial_t\partial_s+
\partial_s\partial_t
\right)
I[tu,s\phi_1]\Big|_{t=s=0}\\
&=
\frac12(C_IAB+C_IAB)\\
&=C_IAB.
\end{aligned}
$$

所以

$$
\boxed{\text{source mixed-Hessian factor}=1}.
$$

不能再插入 $1/2$。

---

## 1.3 Two-action exponential factorial

$S_M,S_H$ 都是 even integrated vertices，因此

$$
S_MS_H=S_HS_M.
$$

于是

$$
\begin{aligned}
\frac1{2!}(S_MS_H+S_HS_M)
&=\frac12(2S_MS_H)\\
&=S_MS_H.
\end{aligned}
$$

故

$$
\boxed{\text{two-action Taylor factor}=1}.
$$

---

## 1.4 Unique Wick pairing

固定 $G_{32}$ external flavors 后，internal pairings 被 field type 和 flavor 唯一固定：

$$
u_I\longleftrightarrow u_M
\quad (r_0),
$$

$$
\phi_{k,M}\longleftrightarrow\widetilde\phi_{k,H}
\quad (r_1),
$$

$$
\phi_{1,I}\longleftrightarrow\widetilde\phi_{1,H}
\quad (r_2).
$$

剩余的 $M$-leg 和 $H_-$-leg 是两个 external legs。不存在第二个 preserving-flavor、preserving-chirality pairing，也没有 graph automorphism division。

Canonical propagators 由

$$
\langle VV\rangle_E
=-\frac{2\hbar g^2}{p^2}\delta^4(\theta_1-\theta_2),
$$

$$
\langle\Phi\widetilde\Phi\rangle_E
=
\frac{\hbar g^2}{16p^2}\bar D^2D^2\delta^4(\theta_1-\theta_2)
$$

经上述 field rescaling 得到。

因此

$$
\langle uu\rangle=-\frac{\hbar}{p^2},
\qquad
\langle\phi\widetilde\phi\rangle
=\frac{\hbar}{16p^2}\bar D^2D^2\delta^4(\theta),
$$

并且

$$
\boxed{
C_{\rm prop}
=(-\hbar)
\left(\frac{\hbar}{16}\right)^2
=-\frac{\hbar^3}{256}.
}
$$

---

## 1.5 $C_{\rm preD}$

$$
\begin{aligned}
C_IC_MC_{H_-}
&=
\left(-\frac{g^2}{4\sqrt2}\right)
\left(\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)\\
&=
\frac{\sqrt2g^4}{4\hbar^2}.
\end{aligned}
$$

再乘 propagators：

$$
\begin{aligned}
C_{\rm preD}^{32}
&=
\frac{\sqrt2g^4}{4\hbar^2}
\left(-\frac{\hbar^3}{256}\right)\\
&=
\boxed{-\frac{\sqrt2\hbar g^4}{1024}}.
\end{aligned}
$$

Reflection 的 net ordered sign 是 $-1$，故

$$
\boxed{
C_{\rm preD}^{33}
=+\frac{\sqrt2\hbar g^4}{1024}.
}
$$

因此在 source Hessian、action Taylor、$H_-$ permutations、Wick pairing 和 propagators 中：

$$
\boxed{\text{没有 missing }1/2.}
$$

---

# 2. Berezin measures、rank projector 与 metric factor

## 2.1 Measures

Project normalization 是

$$
[\Theta_+]_F=1,\qquad
[\Theta_-]_{\widetilde F}=1,\qquad
[\Theta_+\Theta_-]_D=1.
$$

对于 replay 所用 ordered primitive monomials，

$$
m_8=\frac14\Theta_+\Theta_-,
\qquad
m_-=\frac12\Theta_-.
$$

所以

$$
\boxed{
[m_8]_D=\frac14,
\qquad
[m_-]_{\widetilde F}=\frac12.
}
$$

---

## 2.2 Rank extraction

由

$$
\varepsilon^{ab}\varepsilon_{ab}=-2,
$$

若

$$
T_{ab}=t\,\varepsilon_{ab},
$$

则

$$
-\frac12\varepsilon^{ab}T_{ab}
=
-\frac12t\,\varepsilon^{ab}\varepsilon_{ab}
=t.
$$

因此

$$
\boxed{\text{rank extraction}=-\frac12}
$$

是正确的。

---

## 2.3 Trace/metric ambiguity

Project vector metric 是

$$
(v,w)
=
\frac12
\varepsilon^{ab}\varepsilon^{\dot a\dot b}
v_{a\dot a}w_{b\dot b}.
$$

improved_holomorphic_twist_4d_N…

故

$$
r^2
=
\frac12
\varepsilon^{ab}\varepsilon^{\dot a\dot b}
r_{a\dot a}r_{b\dot b},
$$

而

$$
\varepsilon^{ab}\varepsilon^{\dot a\dot b}
r_{a\dot a}r_{b\dot b}
=2r^2.
$$

因此：

- $32768$
- $\varepsilon\varepsilon rr$

单独的 scalar $32768$ 不能区分二者。其 general conversion 是

$$
\begin{aligned}
C_D(\chi)
&=
32768
\left(\frac14\right)
\left(\frac12\right)
\left(-\frac12\right)\chi\\
&=
\boxed{-2048\chi}.
\end{aligned}
$$

---

# 3. Full-$d$ SD identity fixes $\chi$ target-blindly

按旧 $\chi=2$ normalization，三个 square coefficients 是 $\pm1024$。因此对任意 $\chi$：

$$
\begin{aligned}
P_{A,E0}(\chi)
&=-512\chi\,
\frac{\bar r_0^2\mathcal W_0}{D_0D_1D_2},\\
P_{A,L1}(\chi)
&=+512\chi\,
\frac{\bar r_1^2\mathcal W_1}{D_0D_1D_2},\\
P_{B,E2}(\chi)
&=-512\chi\,
\frac{\bar r_2^2\mathcal W_2}{D_0D_1D_2}.
\end{aligned}
$$

JE/JX 不含 loop metric trace，因此它们不乘 $\chi$。

A-occurrence 的 routed contacts 必须是

$$
C_{A,JE}
=
+512\frac{\mathcal W_0}{D_1D_2}
=
+512\frac{D_0\mathcal W_0}{D_0D_1D_2},
$$

$$
C_{A,JX}
=
-512\frac{\mathcal W_1}{D_0D_2}
=
-512\frac{D_1\mathcal W_1}{D_0D_1D_2}.
$$

于是完整 A-occurrence 为

$$
\begin{aligned}
\mathfrak O_A(\chi)
={}&P_{A,E0}(\chi)+P_{A,L1}(\chi)
+C_{A,JE}+C_{A,JX}\\
={}&
\frac{512}{D_0D_1D_2}
\Big[
-\chi\bar r_0^2\mathcal W_0
+\chi\bar r_1^2\mathcal W_1
+D_0\mathcal W_0-D_1\mathcal W_1
\Big].
\end{aligned}
$$

置

$$
\bar r_e^2=D_e+\mu_\ell^2
$$

后，

$$
\boxed{
\begin{aligned}
\mathfrak O_A(\chi)
={}&
\frac{512}{D_0D_1D_2}
\Big[
(1-\chi)D_0\mathcal W_0
+(\chi-1)D_1\mathcal W_1\\
&\hspace{37mm}
+\chi\mu_\ell^2(-\mathcal W_0+\mathcal W_1)
\Big].
\end{aligned}}
$$

Full-$d$ Schwinger–Dyson identity 必须在 $\mu_\ell^2=0$ 时逐 routed word 成立。Regulated SD equation 是 exact functional integration-by-parts identity。

因此

$$
1-\chi=0,
\qquad
\chi-1=0,
$$

即

$$
\boxed{\chi=1}.
$$

所以 occurrence-resolved JE/JX 各出现一次时，

$$
\boxed{
32768
\left(\frac14\right)
\left(\frac12\right)
\left(-\frac12\right)
=-2048,
}
$$

不能再乘 $2$。

等价地：

$$
\boxed{
\text{exact missing factor } \frac12
\text{ 位于旧 trace/metric reconstruction，}
\quad 2\longrightarrow1.
}
$$

这不是由 HT target 推断的，而是由 full-$d$ SD cancellation 推得。

若坚持 $\chi=2$，则必须另外补出第二份 JE 和第二份 JX：

$$
N_{JE}=N_{JX}=2.
$$

当前题设称它们为 occurrence-resolved single pair，故该 alternative 与输入不相容。

---

# 4. 三个 square parents、contacts 与 $\mu_\ell^2$ remainders

修正后：

## $G3$-A-E0

$$
P_{A,E0}
=
-512
\frac{\bar r_0^2\mathcal W_0}{D_0D_1D_2}.
$$

Full-$d$ contact：

$$
C_{A,E0}
=
+512\frac{\mathcal W_0}{D_1D_2}.
$$

因此

$$
\begin{aligned}
P_{A,E0}+C_{A,E0}
&=
-512
\frac{\bar r_0^2\mathcal W_0}{D_0D_1D_2}
+512
\frac{D_0\mathcal W_0}{D_0D_1D_2}\\
&=
\boxed{
-512
\frac{\mu_\ell^2\mathcal W_0}{D_0D_1D_2}.
}
\end{aligned}
$$

---

## $G3$-A-L1

$$
P_{A,L1}
=
+512
\frac{\bar r_1^2\mathcal W_1}{D_0D_1D_2}.
$$

Full-$d$ contact：

$$
C_{A,L1}
=
-512\frac{\mathcal W_1}{D_0D_2}.
$$

因此

$$
\begin{aligned}
P_{A,L1}+C_{A,L1}
&=
512
\frac{\bar r_1^2\mathcal W_1}{D_0D_1D_2}
-512
\frac{D_1\mathcal W_1}{D_0D_1D_2}\\
&=
\boxed{
+512
\frac{\mu_\ell^2\mathcal W_1}{D_0D_1D_2}.
}
\end{aligned}
$$

---

## $G3$-B-E2

$$
P_{B,E2}
=
-512
\frac{\bar r_2^2\mathcal W_2}{D_0D_1D_2}.
$$

其 required full-$d$ contact 必须是

$$
C_{B,E2}^{\rm req}
=
+512\frac{\mathcal W_2}{D_0D_1}.
$$

因此

$$
\boxed{
P_{B,E2}+C_{B,E2}^{\rm req}
=
-512
\frac{\mu_\ell^2\mathcal W_2}{D_0D_1D_2}.
}
$$

---

## $r_1$ 的 status

$$
\boxed{
r_1\text{ term 是同一 A-graph/SD orbit 中的第二个 marked parent term，}
}
$$

但它不是第二张 Feynman graph。

理由是：

$$
P_{A,L1}\ \text{仍含}\ D_0D_1D_2
$$

且含 $\bar r_1^2$，而 $r_0$-contact 必须删除 $D_0$：

$$
C_{e=0}\ \text{只能有}\ \frac1{D_1D_2}.
$$

所以 $r_1$ term 不是 $r_0$ collapsed contact；它是 transport 后作用在第二条 inverse-kernel edge 上的 parent square。不能给它额外 graph symmetry factor，也不能从 residue sum 中删除。

---

# 5. JE/JX 与 PE/PX

## 5.1 Matter-action Hessians

Canonical exponent vertex 是

$$
\mathscr V_M
=
C_M\int_8
\widetilde\phi_s^X
u^Y(T_Y)^X{}_Z
\phi_s^Z.
$$

其 relevant local derivatives 为

$$
\frac{\vec\delta\mathscr V_M}{\delta u^Y(z)}
=
C_M
\widetilde\phi_s^X(T_Y)^X{}_Z\phi_s^Z(z),
$$

$$
\frac{\vec\delta\mathscr V_M}{\delta\phi_s^Z(z)}
=
C_M
\widetilde\phi_s^X(u^YT_Y)^X{}_Z(z).
$$

第一项 collapse vector edge $r_0$，第二项 collapse transported matter edge $r_1$。Ordered left differentiation 的 Koszul rule 是固定的。

因此

$$
\boxed{
JE:\quad
+512\frac{\mathcal W_0}{D_1D_2},
}
$$

$$
\boxed{
JX:\quad
-512\frac{\mathcal W_1}{D_0D_2}.
}
$$

它们不是 pointwise zero。若暂时 suppress routing distinction，令 $\mathcal W_0=\mathcal W_1=\mathcal W$，则

$$
\begin{aligned}
JE+JX
&=
512\mathcal W
\left(
\frac1{D_1D_2}-\frac1{D_0D_2}
\right)\\
&=
512
\frac{D_0-D_1}{D_0D_1D_2}\mathcal W\\
&=
512
\frac{2\ell\cdot p-p^2}{D_0D_1D_2}\mathcal W.
\end{aligned}
$$

这是 affine loop-momentum contact，不是零 bubble。

---

## 5.2 Antichiral $H_-$ Hessian

Exponent functional 可写为

$$
\mathscr V_{H_-}
=
\frac{C_{H_-}}{3!}
\int_-
\varepsilon_{rst}c_{ABC}
\widetilde\phi_r^A
\widetilde\phi_s^B
\widetilde\phi_t^C.
$$

一阶 derivative：

$$
\begin{aligned}
\frac{\vec\delta\mathscr V_{H_-}}
{\delta\widetilde\phi_1^A}
&=
\frac{C_{H_-}}2
\left[
\varepsilon_{123}c_{ABC}
\widetilde\phi_2^B\widetilde\phi_3^C
+
\varepsilon_{132}c_{ACB}
\widetilde\phi_3^C\widetilde\phi_2^B
\right]\\
&=
\frac{C_{H_-}}2
\left[
c_{ABC}\widetilde\phi_2^B\widetilde\phi_3^C
+
c_{ABC}\widetilde\phi_2^B\widetilde\phi_3^C
\right]\\
&=
C_{H_-}c_{ABC}
\widetilde\phi_2^B\widetilde\phi_3^C.
\end{aligned}
$$

相应 local Hessians 是

$$
\frac{\vec\delta^2\mathscr V_{H_-}}
{\delta\widetilde\phi_2^D(z')
 \delta\widetilde\phi_1^A(z)}
=
C_{H_-}c_{ADC}\,
\widetilde\phi_3^C(z)\,
\delta_-(z,z'),
$$

$$
\frac{\vec\delta^2\mathscr V_{H_-}}
{\delta\widetilde\phi_3^D(z')
 \delta\widetilde\phi_1^A(z)}
=
C_{H_-}c_{ABD}\,
\widetilde\phi_2^B(z)\,
\delta_-(z,z').
$$

---

## 5.3 PE/PX matching equation

令 $e_{PE},e_{PX}$ 是各自 collapse 的 propagator edge，并保留完整 routed words：

$$
PE
=
-128\,
\frac{\mathcal W_{PE}}
{\prod_{j\neq e_{PE}}D_j}
=
-128\,
\frac{D_{e_{PE}}\mathcal W_{PE}}
{D_0D_1D_2},
$$

$$
PX
=
+128\,
\frac{\mathcal W_{PX}}
{\prod_{j\neq e_{PX}}D_j}
=
+128\,
\frac{D_{e_{PX}}\mathcal W_{PX}}
{D_0D_1D_2}.
$$

因此

$$
\boxed{
PE+PX
=
\frac{128}
{D_0D_1D_2}
\left[
-D_{e_{PE}}\mathcal W_{PE}
+D_{e_{PX}}\mathcal W_{PX}
\right].
}
$$

Pointwise cancellation 需要同时满足

$$
e_{PE}=e_{PX},
\qquad
\mathcal W_{PE}=\mathcal W_{PX}.
$$

题中只给出 untagged display $W_{p0}$，没有给这两个等式。

要与 $B$-parent 完成 full-$d$ SD matching，必须逐 occurrence 证明

$$
\boxed{
-D_{e_{PE}}\mathcal W_{PE}
+D_{e_{PX}}\mathcal W_{PX}
=
4D_2\mathcal W_2.
}
$$

因为随后

$$
PE+PX
=
+512\frac{D_2\mathcal W_2}{D_0D_1D_2}
=
+512\frac{\mathcal W_2}{D_0D_1}.
$$

这正是 $P_{B,E2}$ 所需的 contact。

---

## 5.4 第一个缺失的 local contact kernel

当前输入没有给出

$$
\boxed{
\mathcal K^{B}_{\alpha,e}
:=
\Pi_{\mathcal W_2}
\left[
(D_-D_+)_{z_0}
G_{0}^{\Phi_1\widetilde\Phi_1}
(z_0,z_H;r_2)
\star
\mathcal H_{1k}^{H_-}(z_H,z')
\right]_{\alpha,e},
\qquad
\alpha\in\{PE,PX\},
}
$$

其中必须显式包含：

$$
e=e_{PE},e_{PX},
$$

$$
\delta_-\text{ orientation},
$$

$$
\text{left/right derivative order},
$$

$$
\text{post-collapse loop routing},
$$

$$
\text{Hessian permutation multiplicity},
$$

$$
\mathcal W_{PE},\mathcal W_{PX}
\longrightarrow\mathcal W_2.
$$

所以 PE/PX 的 full SD equality 不能由当前 displayed coefficients 单独证明。这是完成 complete orbit 时的第一个缺失 contact kernel。

---

# 6. Exact simplex moments 与 absolute branch coefficient

Normalized triangle simplex measure 为

$$
d\Sigma
=
2\,dx\,dy,
\qquad
x\ge0,\quad y\ge0,\quad x+y\le1.
$$

Normalization：

$$
2\int_0^1dx\int_0^{1-x}dy
=
2\int_0^1(1-x)\,dx
=1.
$$

第一矩：

$$
\begin{aligned}
\int d\Sigma\,x
&=
2\int_0^1dx\int_0^{1-x}dy\,x\\
&=
2\int_0^1x(1-x)\,dx\\
&=
2\left(\frac12-\frac13\right)
=\frac13.
\end{aligned}
$$

同理

$$
\boxed{
\int d\Sigma\,x
=
\int d\Sigma\,y
=
\int d\Sigma\,(1-x-y)
=
\frac13.
}
$$

---

## $G_{32}$：single branch

使用修正后的

$$
C_D=-2048,
$$

有

$$
\begin{aligned}
\mathcal A_{32}^{(e)}
&=
C_{\rm preD}^{32}
(-2048)
\left(\frac13\right)
\left(\frac1{32\pi^2}\right)
g^{-2}(+i)\\
&=
\left(
-\frac{\sqrt2\hbar g^4}{1024}
\right)
(-2048)
\left(\frac13\right)
\left(\frac1{32\pi^2}\right)
g^{-2}(+i)\\
&=
2\sqrt2\hbar g^4
\left(\frac1{96\pi^2}\right)
g^{-2}(+i)\\
&=
\frac{i\sqrt2\hbar g^2}{48\pi^2}\\
&=
\frac{i\sqrt2}{3}
\frac{\hbar g^2}{16\pi^2}\\
&=
\boxed{\frac13i\sqrt2\,\lambda_1}.
\end{aligned}
$$

三个 marked square branches 给出

$$
\boxed{
G_{32}^{\rm marked}
=
3\left(\frac13i\sqrt2\lambda_1\right)
=
+i\sqrt2\lambda_1.
}
$$

---

## Reflected $G_{33}$：independent multiplication

$$
\begin{aligned}
\mathcal A_{33}^{(e)}
&=
C_{\rm preD}^{33}
(-2048)
\left(\frac13\right)
\left(\frac1{32\pi^2}\right)
g^{-2}(+i)\\
&=
\left(
+\frac{\sqrt2\hbar g^4}{1024}
\right)
(-2048)
\left(\frac13\right)
\left(\frac1{32\pi^2}\right)
g^{-2}(+i)\\
&=
-\frac13i\sqrt2\lambda_1.
\end{aligned}
$$

所以

$$
\boxed{
G_{33}^{\rm marked}
=
-i\sqrt2\lambda_1.
}
$$

---

# 7. AB/BA reflection sign

Source factors 的 Grassmann parity 是

$$
\epsilon(A)=
\epsilon(D_+\bar D^2D_+u)=0,
$$

$$
\epsilon(B_1)=
\epsilon(D_+\phi_1)=1.
$$

所以 source-order reflection 的 direct Koszul factor 为

$$
(-1)^{\epsilon(A)\epsilon(B_1)}
=(-1)^0
=+1.
$$

$H_-$ 的 flavor/color simultaneous reflection 不产生 sign：

$$
\varepsilon_{132}c_{ACB}
=
(-\varepsilon_{123})(-c_{ABC})
=
\varepsilon_{123}c_{ABC}.
$$

剩余 ordered external color reflection 给出

$$
\sigma_{\rm color}=-1.
$$

因此

$$
\sigma_{\rm refl}
=
\sigma_{\rm Koszul}\sigma_{\rm color}
=
(+1)(-1)
=-1,
$$

即

$$
\boxed{
G_{33}=-G_{32}.
}
$$

---

# 8. Final seal 与 HT comparison

## 已严格封闭的 target-blind residue

在以下两条由题设给出的条件下：

1. $\bar r_e^2$
2. JE/JX、PE/PX 本身不隐藏新的 four-dimensional inverse-kernel square；

则

$$
\boxed{
G_{32}^{AB}
=
+i\sqrt2\,\lambda_1,
\qquad
G_{33}^{BA}
=
-i\sqrt2\,\lambda_1.
}
$$

这两个系数来自：

$$
C_I,\ C_M,\ C_{H_-},\ C_{\rm prop},
$$

exact factorials，

$$
C_D=-2048,
$$

three exact $1/3$ moments，以及

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=
\frac1{32\pi^2}.
$$

没有使用 HT normalization。

## 尚未封闭的 SD row identity

Complete $B$-orbit 仍须补证

$$
\boxed{
-D_{e_{PE}}\mathcal W_{PE}
+D_{e_{PX}}\mathcal W_{PX}
=
4D_2\mathcal W_2.
}
$$

在该 equality 未由 occurrence-resolved kernel 重放以前，严格的完整结果应记为

$$
G_{32}^{\rm full}
=
+i\sqrt2\lambda_1+\Delta_B,
$$

$$
G_{33}^{\rm full}
=
-i\sqrt2\lambda_1-\Delta_B,
$$

其中

$$
\Delta_B=0
$$

当且仅当上述 PE/PX identity 成立且其 marked continuation 不产生新的 $\bar r_f^2$。

## 与 HT 的比较

在 $\Delta_B=0$ 时，

$$
\boxed{
(G_{32},G_{33})_{\rm Project}
=
(+i\sqrt2,-i\sqrt2)\lambda_1,
}
$$

与 physical holomorphic-twist vector 相同。

若仍保留旧 factor two，则第一个不同 equality 不是 simplex integral，也不是 $C_{\rm preD}$，而是

$$
\boxed{
32768
\left(\frac14\right)
\left(\frac12\right)
\left(-\frac12\right)
\underbrace{(2)}_{\text{old trace reconstruction}}
\neq
32768
\left(\frac14\right)
\left(\frac12\right)
\left(-\frac12\right).
}
$$

等价地，旧 $\chi=2$ 与 occurrence-resolved A-sector SD equation 冲突：

$$
-1024D_0+512D_0=-512D_0\neq0,
$$

$$
+1024D_1-512D_1=+512D_1\neq0.
$$

所以 factor-two 的 earliest exact failure 位于 **rank/trace reconstruction versus contact multiplicity**，发生在 Feynman integration 和 HT comparison 之前。
