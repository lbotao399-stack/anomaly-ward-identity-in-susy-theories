## 记号

$$
\alpha:=\frac{\sqrt2g}{\hbar},
\qquad
P^I:=\bar\varphi_1^I,
\qquad
E^J:=\bar\varphi_2^J,
\qquad
X^K:=\bar\varphi_3^K.
$$

这里 $P$ 是连接 source–$H$ edge $r_2$ 的 potential，$E$ 是连接 $M$–$H$ edge $r_1$ 的 Euler potential，$X$ 是剩余 explicit potential。

定义 dotted-spinor wedge

$$
W(a,b):=a_{+\dot\alpha}b_+{}^{\dot\alpha},
\qquad
W_{ij}:=W(r_i,r_j).
$$

因此

$$
W_{ji}=-W_{ij},
\qquad
W_{ii}=0.
$$

又因

$$
p=r_0-r_1,
$$

故

$$
\boxed{
W_{p0}:=W(p,r_0)
=W(r_0-r_1,r_0)
=W_{01}.
}
$$

所有 $P,E,X$ 都是 Grassmann-even。Odd left derivative 满足 graded Leibniz rule；对于 even functional variable，left/right functional derivatives 没有转换符号。

---

# 1. Antichiral cubic 的 exact ordered differentiation

固定 flavor set $(1,2,3)$：

$$
\begin{aligned}
V_{H_-}^{123}
=-\frac{\alpha}{6}\int_-
c_{ABC}\Big(
&P^AE^BX^C
-P^AX^BE^C\\
&-E^AP^BX^C
+E^AX^BP^C\\
&+X^AP^BE^C
-X^AE^BP^C
\Big).
\end{aligned}
$$

六个 permutation 的符号为

$$
\begin{array}{c|cccccc}
\pi&123&132&213&231&312&321\\ \hline
\operatorname{sgn}_{\rm flavor}(\pi)
&+&-&-&+&+&-\\
\operatorname{sgn}_{\rm color}(\pi)
&+&-&-&+&+&-\\
\operatorname{sgn}_{\rm flavor}
\operatorname{sgn}_{\rm color}
&+&+&+&+&+&+
\end{array}
$$

而 field Koszul sign 全部为 $+1$。所以

$$
\frac1{3!}\sum_{\pi\in S_3}
\operatorname{sgn}_{\rm flavor}(\pi)
\operatorname{sgn}_{\rm color}(\pi)
=\frac16(6)=1.
$$

对 source-linked $P^I$ 作 left functional derivative：

$$
\boxed{
\frac{\vec\delta V_{H_-}^{123}}
{\delta P^I}
=
-\alpha\,c_{IJK}E^JX^K.
}
$$

不存在剩余 $1/2$。

---

## 1.1 PE Hessian

保持 ordered derivative slots $(P,E;X)$：

$$
\begin{aligned}
V_{PE}^{IJ}
&:=
\frac{\vec\delta}{\delta E^J}
\frac{\vec\delta V_{H_-}^{123}}{\delta P^I}\\
&=
\frac{\vec\delta}{\delta E^J}
\left(-\alpha c_{ILK}E^LX^K\right)\\
&=
\boxed{-\alpha c_{IJK}X^K}.
\end{aligned}
$$

这给出 supplied scalar sign

$$
\boxed{\mathrm{PE}:\ -128}.
$$

---

## 1.2 PX Hessian

保持 ordered derivative slots $(P,X;E)$：

$$
\begin{aligned}
V_{PX}^{IK}
&:=
\frac{\vec\delta}{\delta X^K}
\frac{\vec\delta V_{H_-}^{123}}{\delta P^I}\\
&=
\frac{\vec\delta}{\delta X^K}
\left(-\alpha c_{IJL}E^JX^L\right)\\
&=
-\alpha c_{IJK}E^J.
\end{aligned}
$$

为了将 derivative indices 按 $(P,X,E)=(I,K,J)$ 排列，

$$
c_{IJK}=-c_{IKJ},
$$

所以

$$
\boxed{
V_{PX}^{IK}
=
+\alpha c_{IKJ}E^J.
}
$$

这给出 supplied scalar sign

$$
\boxed{\mathrm{PX}:\ +128}.
$$

由于 $P,E,X$ 都是 even，

$$
\boxed{
\sigma_{\rm functional\;Koszul}^{PE}
=
\sigma_{\rm functional\;Koszul}^{PX}
=+1,
}
$$

并且

$$
\boxed{
\frac{\overleftarrow\delta}{\delta P}
=
\frac{\vec\delta}{\delta P},
\quad
\frac{\overleftarrow\delta}{\delta E}
=
\frac{\vec\delta}{\delta E},
\quad
\frac{\overleftarrow\delta}{\delta X}
=
\frac{\vec\delta}{\delta X}.
}
$$

---

# 2. Collapsed edge

原始 D-word 中，$P$-slot 只通过

$$
\mathcal B_-
=
D_-D_+\bar D^2D^2\delta_{SH}
$$

连接 source $S$ 与 antichiral vertex $H$。

因此 PE 与 PX 虽然具有不同的 second Hessian slot，但它们共享同一个 first derivative $P$。Schwinger inverse kernel 总是作用在

$$
S\longleftrightarrow H
$$

propagator 上，即

$$
\boxed{
e_{PE}=e_{PX}=2.
}
$$

第二个 derivative slot $E$ 或 $X$ 只决定 $M$–$H$ endpoint 的 ordered routing；它不产生第二个 propagator collapse。

所以两项 collapse 后都留下

$$
\boxed{
\frac1{D_0D_1}.
}
$$

---

# 3. Berezin、endpoint 与 Koszul signs

由

$$
|\mathcal A|=0,
\qquad
|\mathcal B|=1,
\qquad
|\mathcal B_-|=0,
\qquad
|\mathcal P_{MH}|=0,
$$

endpoint transfer 给出

$$
D_-^{(S)}\delta_{SH}
=
-D_-^{(H)}\delta_{SH}.
$$

因此先产生

$$
\sigma_{\rm endpoint}=-1.
$$

对于 odd $D_-^{(H)}$ 和 odd $\mathcal B$，

$$
0
=
\int_H D_-^{(H)}(\mathcal B F)
=
\int_H(D_-^{(H)}\mathcal B)F
-\int_H\mathcal B(D_-^{(H)}F).
$$

所以

$$
\int_H(D_-^{(H)}\mathcal B)F
=
\int_H\mathcal B(D_-^{(H)}F).
$$

即 Berezin integration-by-parts 本身给出

$$
\sigma_{\rm IBP}=+1.
$$

连同 endpoint transfer：

$$
\boxed{
\sigma_{\rm endpoint}\sigma_{\rm IBP}=-1.
}
$$

由于被越过的 potential 是 even，

$$
(-1)^{|D_-P||X|}
=
(-1)^{1\cdot0}
=+1,
$$

$$
(-1)^{|P||D_-X|}
=
(-1)^{0\cdot1}
=+1.
$$

所以 PE/PX 都没有额外 potential-Koszul sign：

$$
\boxed{
\sigma_{\rm Koszul}^{PE}
=
\sigma_{\rm Koszul}^{PX}
=+1.
}
$$

---

# 4. Route-sensitive D-algebra

Antichiral endpoint 满足

$$
D_+Y=0.
$$

Project Euclidean algebra为

$$
\{D_+,\bar D_{\dot\alpha}\}
=
2r_{+\dot\alpha}.
$$

故

$$
\begin{aligned}
D_+\bar D_{\dot\alpha}Y
&=
-\bar D_{\dot\alpha}D_+Y
+2r_{+\dot\alpha}Y\\
&=
2r_{+\dot\alpha}Y.
\end{aligned}
$$

这就是每个 contact row 中不能删除的 exact factor $2$。

---

## 4.1 PE routing

PE ordered Hessian 是

$$
(P,E;X).
$$

Collapse $e_2$ 后，source–$M$ D-word 位于左侧，$M$–$H$ Euler endpoint 位于右侧。因此 free dotted-index contraction 顺序为

$$
(r_0,r_1).
$$

Route-sensitive numerator：

$$
\begin{aligned}
W_{PE}
&=
(\sigma_{\rm endpoint}\sigma_{\rm IBP})
(\sigma_{\rm Koszul})
(2)\,
W(r_0,r_1)\\
&=
(-1)(+1)(2)W_{01}\\
&=
\boxed{-2W_{01}}\\
&=
\boxed{-2W_{p0}}.
\end{aligned}
$$

---

## 4.2 PX routing

PX ordered Hessian 是

$$
(P,X;E).
$$

Canonical left differentiation leaves the $M$–$H$ endpoint on the opposite side of the free dotted contraction，因此顺序为

$$
(r_1,r_0).
$$

于是

$$
\begin{aligned}
W_{PX}
&=
(\sigma_{\rm endpoint}\sigma_{\rm IBP})
(\sigma_{\rm Koszul})
(2)\,
W(r_1,r_0)\\
&=
(-1)(+1)(2)W_{10}\\
&=
-2(-W_{01})\\
&=
\boxed{+2W_{01}}\\
&=
\boxed{+2W_{p0}}.
\end{aligned}
$$

完整 sign ledger：

$$
\begin{array}{c|cc}
&PE&PX\\ \hline
\text{ordered Hessian coefficient}&-128&+128\\
e&2&2\\
\text{left/right derivative sign}&+1&+1\\
\text{endpoint transfer}&-1&-1\\
\text{Berezin IBP}&+1&+1\\
\text{potential Koszul}&+1&+1\\
\text{mixed }D\bar D\text{ factor}&2&2\\
\text{wedge order}&W_{01}&W_{10}\\
W_{\rm routed}&-2W_{p0}&+2W_{p0}
\end{array}
$$

---

# 5. Exact PE/PX identity

由于

$$
e_{PE}=e_{PX}=2,
$$

有

$$
\begin{aligned}
-D_{e_{PE}}W_{PE}
+D_{e_{PX}}W_{PX}
&=
-D_2(-2W_{p0})
+D_2(+2W_{p0})\\
&=
2D_2W_{p0}+2D_2W_{p0}\\
&=
\boxed{4D_2W_{p0}}.
\end{aligned}
$$

所以题中 displayed identity **exactly correct**：

$$
\boxed{
-D_{e_{PE}}W_{PE}
+D_{e_{PX}}W_{PX}
=
4D_2W_{p0}.
}
$$

Pointwise untagged cancellation 是错误的，因为

$$
\begin{aligned}
(-128)W_{PE}+(+128)W_{PX}
&=
(-128)(-2W_{p0})
+(+128)(+2W_{p0})\\
&=
256W_{p0}+256W_{p0}\\
&=
\boxed{512W_{p0}}.
\end{aligned}
$$

---

# 6. Full-$d$ B-contact

PE：

$$
\begin{aligned}
C_{PE,d}
&=
-128\frac{W_{PE}}{D_0D_1}\\
&=
-128\frac{-2W_{p0}}{D_0D_1}\\
&=
\boxed{
+256\frac{W_{p0}}{D_0D_1}.
}
\end{aligned}
$$

PX：

$$
\begin{aligned}
C_{PX,d}
&=
+128\frac{W_{PX}}{D_0D_1}\\
&=
+128\frac{+2W_{p0}}{D_0D_1}\\
&=
\boxed{
+256\frac{W_{p0}}{D_0D_1}.
}
\end{aligned}
$$

因此

$$
\boxed{
C_{B,d}
=
C_{PE,d}+C_{PX,d}
=
+512\frac{W_{p0}}{D_0D_1}.
}
$$

等价地，

$$
\boxed{
C_{B,d}
=
+512
\frac{D_2W_{p0}}{D_0D_1D_2}.
}
$$

---

# 7. Full-$d$ Schwinger cancellation

Parent 是

$$
P_{B,E2}
=
-512
\frac{\bar r_2^2W_{p0}}{D_0D_1D_2}.
$$

在 strictly full-$d$ projection 中

$$
\bar r_2^2\longrightarrow r_{2,d}^2=D_2.
$$

所以

$$
\begin{aligned}
P_{B,E2}\big|_{\mu_\ell^2=0}
&=
-512
\frac{D_2W_{p0}}{D_0D_1D_2}\\
&=
-512\frac{W_{p0}}{D_0D_1}.
\end{aligned}
$$

加上 contact：

$$
\begin{aligned}
P_{B,E2}\big|_{\mu_\ell^2=0}
+C_{B,d}
&=
-512\frac{W_{p0}}{D_0D_1}
+512\frac{W_{p0}}{D_0D_1}\\
&=
\boxed{0}.
\end{aligned}
$$

这正是 regulated Schwinger–Dyson integration-by-parts identity 的 occurrence-resolved realization。

---

# 8. Unique finite remainder

先写

$$
\bar r_2^2=D_2+\mu_\ell^2.
$$

于是

$$
\begin{aligned}
P_{B,E2}+C_{B,d}
={}&
-512
\frac{(D_2+\mu_\ell^2)W_{p0}}
{D_0D_1D_2}
+
512
\frac{D_2W_{p0}}
{D_0D_1D_2}\\
={}&
-512
\frac{D_2W_{p0}}
{D_0D_1D_2}
-512
\frac{\mu_\ell^2W_{p0}}
{D_0D_1D_2}\\
&+
512
\frac{D_2W_{p0}}
{D_0D_1D_2}\\
={}&
\boxed{
-512
\frac{\mu_\ell^2W_{p0}}
{D_0D_1D_2}.
}
\end{aligned}
$$

PE/PX collapse 后只剩 $D_0D_1$，其 numerator 不再含任何 $\bar r_f^2$。因此没有 secondary marked square：

$$
\boxed{
R_{B,\mathrm{fin}}
=
-512
\frac{\mu_\ell^2W_{p0}}
{D_0D_1D_2}
}
$$

是 B-occurrence 的唯一 finite remainder。

---

# 9. Rank-one simplex integral

取

$$
x+y+z=1,
\qquad x,y,z\geq0,
$$

其中 $x,y,z$ 分别乘 $D_0,D_1,D_2$。则

$$
\begin{aligned}
xD_0+yD_1+zD_2
={}&
x\ell^2+y(\ell-p)^2+z(\ell-p-q)^2.
\end{aligned}
$$

令

$$
\ell=k+(y+z)p+zq.
$$

因为

$$
W_{p0}=W(p,\ell),
$$

所以

$$
\begin{aligned}
W_{p0}
&=
W\bigl(p,k+(y+z)p+zq\bigr)\\
&=
W(p,k)+(y+z)W(p,p)+zW(p,q)\\
&=
W(p,k)+zW(p,q).
\end{aligned}
$$

Odd $k$ integral 为零：

$$
\int d^dk\,
\frac{\mu_k^2W(p,k)}
{(k^2+\Delta)^3}
=0.
$$

而

$$
\begin{aligned}
2\int_{\Sigma_2}z
&=
2\int_0^1dy\int_0^{1-y}dz\,z\\
&=
2\int_0^1dy\,
\frac{(1-y)^2}{2}\\
&=
\int_0^1(1-2y+y^2)\,dy\\
&=
1-1+\frac13\\
&=
\boxed{\frac13}.
\end{aligned}
$$

因此

$$
\boxed{
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2W_{p0}}{D_0D_1D_2}
=
\frac{W(p,q)}{96\pi^2}.
}
$$

---

# 10. Absolute $G_{3,2}$ B-branch

注意：

- $-512$
- $-2048$

两者不能再次相乘。

使用

$$
C_{\rm preD}^{32}
=
-\frac{\sqrt2\hbar g^4}{1024},
$$

$$
C_D=-2048,
\qquad
2\int_{\Sigma_2}z=\frac13,
\qquad
I_{\mu^2}=\frac1{32\pi^2},
$$

以及 external map $g^{-2}$ 和 color $+i$：

$$
\begin{aligned}
G_{3,2}^{B}
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
\boxed{
\frac13i\sqrt2\,\lambda_1.
}
\end{aligned}
$$

Gate 6 已闭合的另外两个 occurrence 为

$$
G_{3,2}^{A,E0}
=
\frac13i\sqrt2\,\lambda_1,
$$

$$
G_{3,2}^{A,L1}
=
\frac13i\sqrt2\,\lambda_1.
$$

因此

$$
\begin{aligned}
G_{3,2}^{AB}
&=
G_{3,2}^{A,E0}
+
G_{3,2}^{A,L1}
+
G_{3,2}^{B,E2}\\
&=
\left(
\frac13+\frac13+\frac13
\right)
i\sqrt2\,\lambda_1\\
&=
\boxed{
+i\sqrt2\,\lambda_1.
}
\end{aligned}
$$

---

# 11. Reflected $BA$ orientation

Reflection 取

$$
(p,q,\ell)
\longmapsto
(q,p,\widetilde\ell),
\qquad
\widetilde\ell=p+q-\ell.
$$

于是

$$
\widetilde r_0
=
\widetilde\ell
=
-r_2,
$$

$$
\widetilde r_1
=
\widetilde\ell-q
=
-r_1,
$$

$$
\widetilde r_2
=
\widetilde\ell-q-p
=
-r_0.
$$

所以

$$
D_0\longleftrightarrow D_2,
\qquad
D_1\longmapsto D_1,
\qquad
\mu_\ell^2\longmapsto\mu_\ell^2.
$$

AB 的 $e_2$ PE/PX proof 映为 BA 的 $e_0$ proof：

$$
-D_0\widetilde W_{PE}
+D_0\widetilde W_{PX}
=
4D_0\widetilde W.
$$

Simplex relabeling $z\leftrightarrow x$ 不改变 moment：

$$
2\int_{\Sigma_2}x
=
\frac13.
$$

Source factors 的 parity 是

$$
|A|=0,
\qquad
|B_1|=1,
$$

故 source reflection Koszul sign 为

$$
(-1)^{|A||B_1|}
=
(-1)^{0\cdot1}
=
+1.
$$

Flavor/color simultaneous reflection 给出 $+1$，ordered external color reflection 给出 $-1$。因此

$$
C_{\rm preD}^{33}
=
-C_{\rm preD}^{32}
=
+\frac{\sqrt2\hbar g^4}{1024}.
$$

每个 reflected branch：

$$
\begin{aligned}
G_{3,3}^{(e)}
&=
\left(
+\frac{\sqrt2\hbar g^4}{1024}
\right)
(-2048)
\left(\frac13\right)
\left(\frac1{32\pi^2}\right)
g^{-2}(+i)\\
&=
-2\sqrt2\hbar g^4
\left(\frac1{96\pi^2}\right)
g^{-2}(+i)\\
&=
-\frac{i\sqrt2\hbar g^2}{48\pi^2}\\
&=
\boxed{
-\frac13i\sqrt2\,\lambda_1.
}
\end{aligned}
$$

三条 reflected occurrence 相加：

$$
\boxed{
G_{3,3}^{BA}
=
-\,i\sqrt2\,\lambda_1.
}
$$

---

# Closed target-blind result

$$
\boxed{
\left(
G_{3,2}^{AB},
G_{3,3}^{BA}
\right)
=
\left(
+i\sqrt2\,\lambda_1,
-i\sqrt2\,\lambda_1
\right).
}
$$

其中 B-occurrence 已完全闭合：

$$
\boxed{
e_{PE}=e_{PX}=2,
\qquad
W_{PE}=-2W_{p0},
\qquad
W_{PX}=+2W_{p0},
}
$$

$$
\boxed{
C_{B,d}
=
+512\frac{W_{p0}}{D_0D_1},
}
$$

$$
\boxed{
P_{B,E2}\big|_{\mu_\ell^2=0}
+C_{B,d}=0,
}
$$

$$
\boxed{
P_{B,E2}+C_{B,d}
=
-512
\frac{\mu_\ell^2W_{p0}}
{D_0D_1D_2}.
}
$$
