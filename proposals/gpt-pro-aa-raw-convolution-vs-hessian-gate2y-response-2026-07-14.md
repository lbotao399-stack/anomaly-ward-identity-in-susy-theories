## 记号 / Notation

$$
\Pi_3:=\{SBE,SEB,BSE,BES,ESB,EBS\},
$$

其中 $S,B,E$ 分别表示 source port、bridge port、external port；它们是 occurrence labels，不是 color indices。

$$
\mathsf r_e=
\begin{pmatrix}
a_e&b_e\\ c_e&d_e
\end{pmatrix}
:=-i\sigma_E\!\cdot r_e,
\qquad
\det\mathsf r_e=-\bar r_e^{\,2}.
$$

$$
D_e:=r_{e,d}^{\,2},\qquad
\bar r_e^{\,2}-r_{e,d}^{\,2}=\mu_\ell^2,
\qquad
P:=p+q.
$$

定义 color tensor

$$
\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E},
$$

以及

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

最终 ordered basis 取为

$$
\mathcal B_{AA}:=
\left(
D_{\dot\alpha}^D(q)p^{\dot\alpha}A^E(p),\;
D_{\dot\alpha}^D(q)q^{\dot\alpha}A^E(p),\;
(p_{\dot\alpha}A^D(p))D^{E\dot\alpha}(q),\;
(q_{\dot\alpha}A^D(p))D^{E\dot\alpha}(q)
\right).
$$

---

# 0. Main result

1. 在 parity-even sector

$$
f_{AB}=\widetilde f_{AB}=g^{-2}\kappa_{AB},
$$

raw convolution **严格证明**两条 compact Hessian：

$$
\boxed{
\mathfrak V_W
=
-\frac{ig}{4\hbar}
c_{UCE}W_c^{E\gamma}(D_{C\gamma}-D_{U\gamma})},
$$

$$
\boxed{
\mathfrak V_{\widetilde W}
=
+\frac{ig}{4\hbar}
c_{UCD}\widetilde W_{c\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma})}.
$$
2. $72$
3. 已给出的 edge-tagged selected rows 唯一给出

$$
\boxed{
\Gamma^{DA}_{\rm selected}
=
\frac{\lambda_1}{48}\,
\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^D(q)p^{\dot\alpha}A^E(p)
-
D_{\dot\alpha}^D(q)q^{\dot\alpha}A^E(p)
\right]}.
$$
4. **完整 DA coefficient 仍未定义。** 第一条缺失 equality 是 occurrence-resolved longitudinal lift：

$$
\boxed{
\sum_jG_{01,L}^{(j)}
=
-2d_0(a_0b_2-b_0a_2)
}
$$

$G_{01,L}^{(j)}$
5. AD 还额外缺少 reflected occurrence map。因此最终 target-blind ordered vector 不能赋予四个确定数值。

---

# 1. $p+q+r+s=1$：八个 cubic words

所有 factorial 均为 $1$，且每项

$$
(p+q+1)(r+s+1)=2.
$$

## 1.1 Chiral line

定义

$$
\begin{aligned}
P_+[X,Y,Z]
&:=
[\bar D^2(u_XD^au_Y)]^A
[\bar D^2D_au_Z]^B,\\
Q_+[X,Y,Z]
&:=
[\bar D^2(D^au_Xu_Y)]^A
[\bar D^2D_au_Z]^B,\\
R_+[X,Y,Z]
&:=
[\bar D^2D^au_X]^A
[\bar D^2(u_YD_au_Z)]^B,\\
S_+[X,Y,Z]
&:=
[\bar D^2D^au_X]^A
[\bar D^2(D_au_Yu_Z)]^B.
\end{aligned}
$$

四个 unscaled action coefficients 为

$$
\begin{array}{c|c|c}
(p,q,r,s)&\text{word}&c_{R,+}\\ \hline
(1,0,0,0)&P_+&-\dfrac{\eta_Rf_{AB}}{512}\\[2mm]
(0,1,0,0)&Q_+&+\dfrac{\eta_Rf_{AB}}{512}\\[2mm]
(0,0,1,0)&R_+&-\dfrac{\eta_Rf_{AB}}{512}\\[2mm]
(0,0,0,1)&S_+&+\dfrac{\eta_Rf_{AB}}{512}
\end{array}
$$

## 1.2 Antichiral line

定义

$$
\begin{aligned}
P_-[X,Y,Z]
&:=
[D^2(u_X\bar D_{\dot a}u_Y)]^A
[D^2\bar D^{\dot a}u_Z]^B,\\
Q_-[X,Y,Z]
&:=
[D^2(\bar D_{\dot a}u_Xu_Y)]^A
[D^2\bar D^{\dot a}u_Z]^B,\\
R_-[X,Y,Z]
&:=
[D^2\bar D_{\dot a}u_X]^A
[D^2(u_Y\bar D^{\dot a}u_Z)]^B,\\
S_-[X,Y,Z]
&:=
[D^2\bar D_{\dot a}u_X]^A
[D^2(\bar D^{\dot a}u_Yu_Z)]^B.
\end{aligned}
$$

由于 antichiral sign 为 $(-1)^{q+s}$，

$$
\begin{array}{c|c|c}
(p,q,r,s)&\text{word}&c_{R,-}\\ \hline
(1,0,0,0)&P_-&+\dfrac{\eta_R\widetilde f_{AB}}{512}\\[2mm]
(0,1,0,0)&Q_-&-\dfrac{\eta_R\widetilde f_{AB}}{512}\\[2mm]
(0,0,1,0)&R_-&+\dfrac{\eta_R\widetilde f_{AB}}{512}\\[2mm]
(0,0,0,1)&S_-&-\dfrac{\eta_R\widetilde f_{AB}}{512}
\end{array}
$$

---

# 2. 全部 ordered port assignments

每个 word 的 labeled third derivative 都是

$$
\delta_S\delta_B\delta_E\,X[u,u,u]
=
\sum_{\pi\in\Pi_3}X[\pi_1,\pi_2,\pi_3].
$$

因为 $u$ 是 Grassmann-even，functional differentiation 本身不产生 Koszul sign。

## 2.1 Chiral：$4\times6=24$ rows

$$
\begin{array}{c|cccccc}
& SBE&SEB&BSE&BES&ESB&EBS\\ \hline
P_+&
P_+[S,B,E]&P_+[S,E,B]&P_+[B,S,E]&P_+[B,E,S]&P_+[E,S,B]&P_+[E,B,S]\\
Q_+&
Q_+[S,B,E]&Q_+[S,E,B]&Q_+[B,S,E]&Q_+[B,E,S]&Q_+[E,S,B]&Q_+[E,B,S]\\
R_+&
R_+[S,B,E]&R_+[S,E,B]&R_+[B,S,E]&R_+[B,E,S]&R_+[E,S,B]&R_+[E,B,S]\\
S_+&
S_+[S,B,E]&S_+[S,E,B]&S_+[B,S,E]&S_+[B,E,S]&S_+[E,S,B]&S_+[E,B,S]
\end{array}
$$

未使用 cyclicity。

## 2.2 Antichiral：$4\times6=24$ rows

$$
\begin{array}{c|cccccc}
& SBE&SEB&BSE&BES&ESB&EBS\\ \hline
P_-&
P_-[S,B,E]&P_-[S,E,B]&P_-[B,S,E]&P_-[B,E,S]&P_-[E,S,B]&P_-[E,B,S]\\
Q_-&
Q_-[S,B,E]&Q_-[S,E,B]&Q_-[B,S,E]&Q_-[B,E,S]&Q_-[E,S,B]&Q_-[E,B,S]\\
R_-&
R_-[S,B,E]&R_-[S,E,B]&R_-[B,S,E]&R_-[B,E,S]&R_-[E,S,B]&R_-[E,B,S]\\
S_-&
S_-[S,B,E]&S_-[S,E,B]&S_-[B,S,E]&S_-[B,E,S]&S_-[E,S,B]&S_-[E,B,S]
\end{array}
$$

---

# 3. Insert $V=\sqrt2gu$, $h=g^{-2}$

Authority convention 是

$$
\eta_E=-1,\qquad
f_{AB}=g^{-2}\kappa_{AB}+i\mathfrak k_{AB},
\qquad
\widetilde f_{AB}=g^{-2}\kappa_{AB}-i\mathfrak k_{AB}.
$$

由于

$$
(\sqrt2g)^3=2\sqrt2\,g^3,
$$

定义

$$
\alpha^+_{AB}:=\frac{\sqrt2\,g^3}{256}f_{AB},
\qquad
\alpha^-_{AB}:=\frac{\sqrt2\,g^3}{256}\widetilde f_{AB}.
$$

于是每一个固定 port assignment 的 action coefficient 都是

$$
\begin{array}{c|rrrr}
& P&Q&R&S\\ \hline
+&+\alpha^+_{AB}&-\alpha^+_{AB}&+\alpha^+_{AB}&-\alpha^+_{AB}\\
-&-\alpha^-_{AB}&+\alpha^-_{AB}&-\alpha^-_{AB}&+\alpha^-_{AB}
\end{array}
$$

没有 $3!$，没有 $6$，没有 $72$。

在 parity-even sector $\mathfrak k_{AB}=0$，

$$
\alpha^+_{AB}=\alpha^-_{AB}
=\frac{\sqrt2g}{256}\kappa_{AB}
=:a_g\kappa_{AB}.
$$

---

# 4. Raw word sum $\Rightarrow$ compact chiral Hessian

令

$$
X_a:=[D_au,u].
$$

因为

$$
uD_au-D_au\,u=-X_a,
$$

得到

$$
P_+-Q_+
=
-[\bar D^2X^a]^A[\bar D^2D_au]^B,
$$

$$
R_+-S_+
=
-[\bar D^2D^au]^A[\bar D^2X_a]^B.
$$

两个 superfields 均为 odd。利用

$$
Y^aX_a
=
\epsilon^{ab}Y_b\epsilon_{ac}X^c
=
-\delta^b{}_cY_bX^c
=
X^bY_b,
$$

所以两个 cyclic blocks 相等：

$$
S_{E,+}^{(3)}
=
-2a_g\int_+
\kappa_{AB}
[\bar D^2X^a]^A[\bar D^2D_au]^B.
$$

Ordered Berezin projectors 给出

$$
\int_+\bar D^2Z=-4\int d^8z\,Z.
$$

该符号直接来自

$[X]_F=-\frac14D^2X|$ 与

$[Y]_D=\frac1{16}D^2\bar D^2Y|$。

线性 field strength 为

$$
W_{c,a}
=
-\frac1{4\sqrt2}\bar D^2D_au,
\qquad
\bar D^2D_au=-4\sqrt2W_{c,a}.
$$

这与 authority field-strength definition

$\mathcal W_a=-\frac18\bar D^2(e^{-V}De^V)$

一致。

因此

$$
\begin{aligned}
S_{E,+}^{(3)}
&=
-2a_g(-4)(-4\sqrt2)
\int d^8z\,
\kappa_{AB}X^{Aa}W_{c,a}^B\\
&=
-32\sqrt2
\frac{\sqrt2g}{256}
\int d^8z\,
\kappa_{AB}W_c^{Ba}X_a^A\\
&=
-\frac g4
\int d^8z\,
\kappa_{AB}W_c^{Aa}[D_au,u]^B.
\end{aligned}
$$

用

$$
[T_U,T_C]=ic_{UC}{}^FT_F,
\qquad
c_{UCE}:=\kappa_{EF}c_{UC}{}^F,
$$

得

$$
\boxed{
S_{E,+}^{(3)}
=
-\frac{ig}{4}
c_{UCE}
\int d^8z\,
W_c^{Ea}(D_au^U)u^C}.
$$

二阶 variation：

$$
\delta_U\delta_C
\big[c_{MNE}(D_au^M)u^N\big]
=
c_{UCE}D_{Ua}
+
c_{CUE}D_{Ca},
$$

$$
c_{CUE}=-c_{UCE},
$$

故

$$
\frac{\delta^2S_{E,+}^{(3)}}{\delta u^U\delta u^C}
=
-\frac{ig}{4}c_{UCE}(D_U-D_C)
=
+\frac{ig}{4}c_{UCE}(D_C-D_U).
$$

指数 $e^{-S/\hbar}$ 再给一个 minus：

$$
\boxed{
-\frac1\hbar
\frac{\delta^2S_{E,+}^{(3)}}{\delta u^U\delta u^C}
=
-\frac{ig}{4\hbar}
c_{UCE}W_c^{E\gamma}
(D_{C\gamma}-D_{U\gamma})}.
$$

因此 chiral compact Hessian **proved**。

---

# 5. Raw word sum $\Rightarrow$ compact antichiral Hessian

令

$$
\widetilde X_{\dot a}:=[\bar D_{\dot a}u,u].
$$

Antichiral action sum 是

$$
-a_gP_-+a_gQ_--a_gR_-+a_gS_-.
$$

其中

$$
Q_--P_-
=
[D^2\widetilde X_{\dot a}]^A
[D^2\bar D^{\dot a}u]^B,
$$

$$
S_--R_-
=
[D^2\bar D_{\dot a}u]^A
[D^2\widetilde X^{\dot a}]^B.
$$

同样由 epsilon sign 与 odd exchange，两项相等：

$$
S_{E,-}^{(3)}
=
2a_g\int_-
\kappa_{AB}
[D^2\widetilde X_{\dot a}]^A
[D^2\bar D^{\dot a}u]^B.
$$

线性 antichiral field strength：

$$
\widetilde W_{c,\dot a}
=
-\frac1{4\sqrt2}D^2\bar D_{\dot a}u,
\qquad
D^2\bar D_{\dot a}u=-4\sqrt2\widetilde W_{c,\dot a}.
$$

故

$$
\begin{aligned}
S_{E,-}^{(3)}
&=
2a_g(-4)(-4\sqrt2)
\int d^8z\,
\kappa_{AB}
\widetilde X_{\dot a}^A
\widetilde W_c^{B\dot a}\\
&=
+\frac g4
\int d^8z\,
\kappa_{AB}
\widetilde W_{c,\dot a}^A
[\bar D^{\dot a}u,u]^B\\
&=
+\frac{ig}{4}
c_{UCD}
\int d^8z\,
\widetilde W_{c,\dot a}^D
(\bar D^{\dot a}u^U)u^C.
\end{aligned}
$$

于是

$$
\frac{\delta^2S_{E,-}^{(3)}}{\delta u^U\delta u^C}
=
+\frac{ig}{4}c_{UCD}
(\bar D_U-\bar D_C)
=
-\frac{ig}{4}c_{UCD}
(\bar D_C-\bar D_U),
$$

从而

$$
\boxed{
-\frac1\hbar
\frac{\delta^2S_{E,-}^{(3)}}{\delta u^U\delta u^C}
=
+\frac{ig}{4\hbar}
c_{UCD}\widetilde W_{c\dot\gamma}^D
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma})}.
$$

Antichiral compact Hessian 亦 **proved**。

---

## 5.1 非零 $\mathfrak k_{AB}$ 时

定义

$$
c^{(f)}_{UCE}:=f_{EF}c_{UC}{}^F,
\qquad
c^{(\widetilde f)}_{UCD}
:=\widetilde f_{DF}c_{UC}{}^F.
$$

Raw convolution 实际给出

$$
\mathfrak V_W
=
-\frac{ig^3}{4\hbar}
c^{(f)}_{UCE}W^E(D_C-D_U),
$$

$$
\mathfrak V_{\widetilde W}
=
+\frac{ig^3}{4\hbar}
c^{(\widetilde f)}_{UCD}
\widetilde W^D(\bar D_C-\bar D_U).
$$

因此题中两条 Hessian 作为完整等式要求

$$
\boxed{\mathfrak k_{AB}=0}
$$

或另行证明 $\mathfrak k$-sector 是 removable topological boundary term。仅由 (5A.52) 本身不能删除它。

---

# 6. $72$ routes 的精确去向

对每个 vertex 定义完整 raw sum

$$
\mathcal V_\pm
=
\sum_{\pi\in\Pi_3}
\sum_{w=P,Q,R,S}
c_{w,\pm}\mathcal V_{w,\pi}.
$$

### Cancelled combinations

对每个固定 $\pi$：

$$
P_+[\pi]-Q_+[\pi]
$$

删除 symmetric matrix product，只保留 commutator；

$$
R_+[\pi]-S_+[\pi]
$$

执行同一操作。Antichiral 为 $Q_--P_-$ 与 $S_--R_-$。

这里 cancel 的是 symmetric-color linear combination，不是把某个 structural route 单独删掉。

### Combined combinations

$$
(P-Q)\text{ block}=(R-S)\text{ block}
$$

在 graded cyclicity 与 epsilon signs 后合并，产生 action 中已经出现的 factor $2$。

这个 $2$ 已进入

$$
-\frac g4,\qquad +\frac g4.
$$

不能再乘一次。

### Six port assignments

六个 port assignments 是 labeled functional derivative 的六项：

$$
\delta_S\delta_B\delta_E S^{(3)}
=
\sum_{\pi\in\Pi_3}S^{(3)}[\pi].
$$

它们已经进入 Hessian 的 two derivative endpoints

$$
D_C-D_U,
\qquad
\bar D_C-\bar D_U.
$$

不能再乘 $6$。

### Two chiral orderings

固定 DA orientation 时，interaction exponential 给出

$$
\frac1{2!}
\left(
\mathfrak V_{\widetilde W}\mathfrak V_W+
\mathfrak V_W\mathfrak V_{\widetilde W}
\right).
$$

每个 cubic vertex 是 even：

odd external field strength $\times$ odd spinor derivative，因此

$$
\mathfrak V_{\widetilde W}\mathfrak V_W
=
\mathfrak V_W\mathfrak V_{\widetilde W}.
$$

所以

$$
\frac12(1+1)=1.
$$

不能再乘 $2$。

### Exact census statement

$$
6\times6\times2=72
$$

是 formal route-label space。Action-word convolution 把每个 orientation 的 $36$ 个 labels 映射到 compact product 的四个 endpoint terms：

$$
(\bar D_C-\bar D_U)(D_C-D_U)
=
\bar D_CD_C-\bar D_CD_U-\bar D_UD_C+\bar D_UD_U.
$$

两个 selected edges $e=0,2$ 再把这四项展开为题中八个 $G$-rows。

因此：

$$
\boxed{\text{No factor }72,\quad\text{no factor }36,\quad\text{no factor }6.}
$$

更精确地说，$64$ 不是“逐项为零的 routes”；它们属于 raw route space 到八个 endpoint-edge representatives 的 kernel/combinations。

---

# 7. Fixed DA orientation：common coefficient ledger

Compact vertex product：

$$
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
=
\frac{g^2}{16\hbar^2}.
$$

三个 vector propagators：

$$
\prod_{e=0}^2
\left(
-\frac{\hbar\kappa^{A_eB_e}}{D_e}
\right)
=
-\frac{\hbar^3}{D_0D_1D_2}
\prod_{e=0}^2\kappa^{A_eB_e}.
$$

因此 action–propagator coefficient 为

$$
\boxed{
C_{\rm AP}
=
-\frac{\hbar g^2}{16}}.
$$

没有额外 Wick factor。

## 7.1 Corrected source coefficient

由

$$
A_c^{(1)}
=
-\frac1{4\sqrt2}
D_+\bar D^2D_+u
$$

以及

$$
W^\gamma D_\gamma\big|_{W_+}
=
-W_+D_-,
$$

得到

$$
(-D_-)A_c^{(1)}
=
+\frac1{4\sqrt2}
D_-D_+\bar D^2D_+u
=
+\frac1{8\sqrt2}
D^2\bar D^2D_+u.
$$

另一条 source leg 为

$$
A_c^{(1)}
=
-\frac1{4\sqrt2}D_+\bar D^2D_+u.
$$

所以 primitive source coefficient 是

$$
\boxed{
C_{\rm source}^{\rm primitive}
=
\left(+\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
=
-\frac1{64}}.
$$

Berezin saturation primitive 是

$$
[D^2\bar D^2\delta^4(\theta)]_{\theta=0}
=(-4)(-4)=16.
$$

但题中 $G_{01,S},G_{02,S}$ 已经是完成 source、Berezin、endpoint transfer 后的 sparse polynomials。因此：

$$
\boxed{
C_{\rm source}^{\rm effective\;outside\;}G=1}.
$$

不能再乘 $-1/64$、$16$、endpoint sum 或 $16(-1/4)$。

---

# 8. Eight edge-tagged selected rows

由

$$
\det\mathsf r_e=-\bar r_e^{\,2},
$$

写

$$
G_j=q_j\bar r_e^{\,2}.
$$

Allowed cut identity 给出

$$
\begin{aligned}
\frac{q_j\bar r_e^{\,2}}{D_0D_1D_2}
-
\frac{q_j}{\prod_{i\neq e}D_i}
&=
\frac{q_j(\bar r_e^{\,2}-r_{e,d}^{\,2})}
{D_0D_1D_2}\\
&=
\frac{q_j\mu_\ell^2}{D_0D_1D_2}.
\end{aligned}
$$

每一行共同带有

$$
C_{\rm AP}=-\frac{\hbar g^2}{16},
\qquad
C_{\rm source}^{\rm primitive}=-\frac1{64}\subset G,
\qquad
\frac{-\hbar^3}{D_0D_1D_2}\text{ 已用于 }C_{\rm AP}.
$$

## 8.1 $G_{01,S}$, edge $e=0$

$$
G_{01,S}
=
(-b_2\det r_0,\;b_2\det r_0,\;b_2\det r_0,\;b_2\det r_0).
$$

$$
\begin{array}{c|c|c|c|c}
\text{id}&G_j&q_j&e&
\text{full-}d\text{ cut and remainder}\\ \hline
01.1&
+b_2\bar r_0^2&
+b_2&0&
b_2\!\left[
\dfrac{\bar r_0^2}{D_0D_1D_2}
-\dfrac1{D_1D_2}
\right]
=
\dfrac{b_2\mu_\ell^2}{D_0D_1D_2}
\\[4mm]
01.2&
-b_2\bar r_0^2&
-b_2&0&
-b_2\!\left[
\dfrac{\bar r_0^2}{D_0D_1D_2}
-\dfrac1{D_1D_2}
\right]
=
-\dfrac{b_2\mu_\ell^2}{D_0D_1D_2}
\\[4mm]
01.3&
-b_2\bar r_0^2&
-b_2&0&
-b_2\!\left[
\dfrac{\bar r_0^2}{D_0D_1D_2}
-\dfrac1{D_1D_2}
\right]
=
-\dfrac{b_2\mu_\ell^2}{D_0D_1D_2}
\\[4mm]
01.4&
-b_2\bar r_0^2&
-b_2&0&
-b_2\!\left[
\dfrac{\bar r_0^2}{D_0D_1D_2}
-\dfrac1{D_1D_2}
\right]
=
-\dfrac{b_2\mu_\ell^2}{D_0D_1D_2}
\end{array}
$$

因此

$$
\boxed{
R_{01,S}
=
-2b_2\mu_\ell^2}.
$$

## 8.2 $G_{02,S}$, edge $e=2$

$$
G_{02,S}
=
(b_0\det r_2,\;-b_0\det r_2,\;b_0\det r_2,\;b_0\det r_2).
$$

$$
\begin{array}{c|c|c|c|c}
\text{id}&G_j&q_j&e&
\text{full-}d\text{ cut and remainder}\\ \hline
02.1&
-b_0\bar r_2^2&
-b_0&2&
-b_0\!\left[
\dfrac{\bar r_2^2}{D_0D_1D_2}
-\dfrac1{D_0D_1}
\right]
=
-\dfrac{b_0\mu_\ell^2}{D_0D_1D_2}
\\[4mm]
02.2&
+b_0\bar r_2^2&
+b_0&2&
b_0\!\left[
\dfrac{\bar r_2^2}{D_0D_1D_2}
-\dfrac1{D_0D_1}
\right]
=
+\dfrac{b_0\mu_\ell^2}{D_0D_1D_2}
\\[4mm]
02.3&
-b_0\bar r_2^2&
-b_0&2&
-b_0\!\left[
\dfrac{\bar r_2^2}{D_0D_1D_2}
-\dfrac1{D_0D_1}
\right]
=
-\dfrac{b_0\mu_\ell^2}{D_0D_1D_2}
\\[4mm]
02.4&
-b_0\bar r_2^2&
-b_0&2&
-b_0\!\left[
\dfrac{\bar r_2^2}{D_0D_1D_2}
-\dfrac1{D_0D_1}
\right]
=
-\dfrac{b_0\mu_\ell^2}{D_0D_1D_2}
\end{array}
$$

因此

$$
\boxed{
R_{02,S}
=
-2b_0\mu_\ell^2}.
$$

总 selected remainder：

$$
\boxed{
R_{DA,S}
=
-2(b_0+b_2)\mu_\ell^2}.
$$

---

# 9. Longitudinal reconstruction and the occurrence obstruction

Selected sums：

$$
\sum_jG_{01,S}^{(j)}
=
2b_2(a_0d_0-b_0c_0),
$$

$$
\sum_jG_{02,S}^{(j)}
=
2b_0(a_2d_2-b_2c_2).
$$

加入 longitudinal：

$$
\begin{aligned}
G_S+G_L
={}&
2b_2a_0d_0-2b_0b_2c_0
+2b_0a_2d_2-2b_0b_2c_2\\
&-2d_0(a_0b_2-b_0a_2)\\
={}&
2a_0b_2d_0-2b_0b_2c_0
+2b_0a_2d_2-2b_0b_2c_2\\
&-2a_0b_2d_0+2b_0a_2d_0\\
={}&
2b_0a_2(d_0+d_2)
-2b_0b_2(c_0+c_2)\\
={}&
\boxed{
2b_0[a_2(d_0+d_2)-b_2(c_0+c_2)]}\\
={}&G_{\rm full}.
\end{aligned}
$$

这个 equality 正确，但不足以执行 DRED cut。

定义 occurrence-forgetting map

$$
\pi:
\bigoplus_{e=0}^2\mathcal R[e]\longrightarrow\mathcal R,
$$

以及 edge-cut map

$$
\mathscr E
\left(
q\bar r_e^2[e]
\right)
:=
q\mu_\ell^2.
$$

关键事实是

$$
\boxed{\mathscr E\text{ 不通过 }\pi\text{ factorize}.}
$$

题中数据只给出

$$
\pi(\widetilde G_L)
=
-2d_0(a_0b_2-b_0a_2),
$$

没有给出

$$
\widetilde G_L
=
\sum_{j,e}
G_{L,e}^{(j)}[e],
$$

也没有给出每一项对应的 bubble contact。

因此不能从

$$
\mathcal P_{\rm scalar}(G_L)
=
B\bar\ell^2
$$

推出

$$
\mathscr E(\widetilde G_L)=B\mu_\ell^2,
$$

也不能推出

$$
\mathscr E(\widetilde G_L)=0.
$$

实际上，selected sector 已经直接显示两种操作不同：

$$
\mathcal P_{\rm scalar}(G_S)
=
(-4b-3B)\bar\ell^2,
$$

而 edge-tagged cut 给出的 coefficient 是

$$
-2(b_0+b_2)
=
-2[b+(b+B)]
=
-4b-2B.
$$

故

$$
\boxed{
(-4b-3B)\neq(-4b-2B)}.
$$

这正是 aggregate harmonic projection 不能代替 occurrence cut 的严格反例。

因此，完整 DA “sole $\mu_\ell^2$ remainder” 所需的第一条 missing equality 是

$$
\boxed{
\mathscr E(\widetilde G_{DA,L})=0
}
$$

或更原始地，给出所有

$$
\boxed{
\left\{
G_{01,L}^{(j)},\,
e_{01,L}^{(j)},\,
G_{01,L,\rm contact}^{(j)}
\right\}_{j}
}.
$$

当前输入没有这条 equality。

---

# 10. Rank-one simplex moments：selected sector

取

$$
r_0=k,\qquad
r_1=k+q,\qquad
r_2=k+P,\qquad P=p+q.
$$

Feynman parameters：

$$
\frac1{D_0D_1D_2}
=
2\int d\Omega\,
\frac1{(\ell^2+\Delta)^3},
$$

$$
d\Omega
:=
dx\,dy\,dz\,
\delta(1-x-y-z),
$$

$$
\ell=k+yq+zP,
\qquad
k=\ell-yq-zP.
$$

Simplex moments：

$$
\begin{aligned}
M_0
&=
\int_0^1dy\int_0^{1-y}dz
=
\int_0^1(1-y)\,dy\\
&=
1-\frac12
=
\frac12,
\end{aligned}
$$

$$
\begin{aligned}
M_y
&=
\int_0^1dy\int_0^{1-y}dz\,y\\
&=
\int_0^1y(1-y)\,dy\\
&=
\frac12-\frac13
=
\frac16,
\end{aligned}
$$

$$
M_z
=
\frac16.
$$

令

$$
J:=
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell^2+\Delta)^3}.
$$

由给定 master：

$$
2M_0J
=
\frac1{32\pi^2}.
$$

由于 $2M_0=1$，

$$
J=\frac1{32\pi^2}.
$$

于是

$$
2M_yJ
=
2\cdot\frac16\cdot\frac1{32\pi^2}
=
\frac1{96\pi^2},
$$

$$
2M_zJ
=
\frac1{96\pi^2}.
$$

设 $\beta=b(\ell)$，且 $B=b(P)=b(p)+b(q)$。则

$$
b_0
=
\beta-yb(q)-zB,
$$

$$
b_2
=
\beta-yb(q)+(1-z)B.
$$

Odd loop moment 为零：

$$
\int
\frac{\mu_\ell^2\,\beta}{D_0D_1D_2}
=0.
$$

因此

$$
\begin{aligned}
\int
\frac{\mu_\ell^2b_0}{D_0D_1D_2}
&=
-\frac{b(q)}{96\pi^2}
-\frac{B}{96\pi^2}\\
&=
-\frac{b(p)+2b(q)}{96\pi^2},
\end{aligned}
$$

以及

$$
\begin{aligned}
\int
\frac{\mu_\ell^2b_2}{D_0D_1D_2}
&=
-\frac{b(q)}{96\pi^2}
+
B\left(
\frac1{32\pi^2}-\frac1{96\pi^2}
\right)\\
&=
-\frac{b(q)}{96\pi^2}
+\frac{2B}{96\pi^2}\\
&=
\frac{2b(p)+b(q)}{96\pi^2}.
\end{aligned}
$$

故

$$
\begin{aligned}
\int
\frac{-2(b_0+b_2)\mu_\ell^2}
{D_0D_1D_2}
&=
-2
\frac{
-[b(p)+2b(q)]
+[2b(p)+b(q)]
}
{96\pi^2}\\
&=
-2
\frac{b(p)-b(q)}{96\pi^2}\\
&=
\frac{b(q)-b(p)}{48\pi^2}.
\end{aligned}
$$

乘以

$$
C_{\rm AP}
=
-\frac{\hbar g^2}{16},
$$

得到

$$
\begin{aligned}
\Gamma_{DA,S}
&=
-\frac{\hbar g^2}{16}
\frac{b(q)-b(p)}{48\pi^2}\\
&=
\frac{\hbar g^2}{768\pi^2}
[b(p)-b(q)]\\
&=
\frac{\lambda_1}{48}
[b(p)-b(q)].
\end{aligned}
$$

Covariant typed form：

$$
\boxed{
\Gamma^{DA}_{S}
=
\frac{\lambda_1}{48}
\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^D(q)p^{\dot\alpha}A^E(p)
-
D_{\dot\alpha}^D(q)q^{\dot\alpha}A^E(p)
\right]}.
$$

注意两种 typed structures 完全独立：

$$
\boxed{
c_{D(q)pA(p)}=\frac{\lambda_1}{48}},
\qquad
\boxed{
c_{D(q)qA(p)}=-\frac{\lambda_1}{48}}.
$$

这只是 selected contribution；不能把它命名为 complete DA coefficient，除非补充

$$
\mathscr E(\widetilde G_{DA,L})=0.
$$

---

# 11. Reflected AD orientation

## 11.1 Action、source、propagator coefficients

Raw action convolution 不变：

$$
C_{\rm AP}^{AD}
=
-\frac{\hbar g^2}{16}.
$$

由于 $A=D_+W_+$ 为 even，交换两个 ordered source legs 不产生 source-field Koszul sign。

Color reflection：

$$
\begin{aligned}
\mathbb F^{BA}{}_{ED}
&=
\kappa^{BU}\kappa^{AV}\kappa^{CC'}
c_{UCE}c_{VC'D}\\
&=
\kappa^{AV}\kappa^{BU}\kappa^{C'C}
c_{VC'E}c_{UCD}\\
&=
\mathbb F^{AB}{}_{DE}.
\end{aligned}
$$

## 11.2 Independent reflected routing

取

$$
\rho_0=k,\qquad
\rho_1=k+p,\qquad
\rho_2=k+P.
$$

Feynman shift：

$$
\ell'=k+yp+zP.
$$

则

$$
b'_0
=
\beta'-yb(p)-zB,
$$

$$
b'_2
=
\beta'-yb(p)+(1-z)B.
$$

同样得到

$$
\boxed{
\int
\frac{\mu_\ell^2b'_0}{D_0D_1D_2}
=
-\frac{2b(p)+b(q)}{96\pi^2}},
$$

$$
\boxed{
\int
\frac{\mu_\ell^2b'_2}{D_0D_1D_2}
=
\frac{b(p)+2b(q)}{96\pi^2}}.
$$

若 occurrence-resolved AD row sum 写为

$$
R_{AD}
=
(\alpha b'_0+\beta b'_2)\mu_\ell^2,
$$

则

$$
\int\frac{R_{AD}}{D_0D_1D_2}
=
\frac{
(-2\alpha+\beta)b(p)
+
(-\alpha+2\beta)b(q)
}
{96\pi^2}.
$$

乘 action–propagator coefficient 后，natural upper-lower contraction 为

$$
-\frac{\lambda_1}{96}
\left[
(-2\alpha+\beta)
(p^{\dot\alpha}A^D)D_{\dot\alpha}^E
+
(-\alpha+2\beta)
(q^{\dot\alpha}A^D)D_{\dot\alpha}^E
\right].
$$

## 11.3 Epsilon-index sign

由

$$
X^{\dot\alpha}
=
\epsilon^{\dot\alpha\dot\beta}X_{\dot\beta},
\qquad
D^{\dot\alpha}
=
\epsilon^{\dot\alpha\dot\beta}D_{\dot\beta},
$$

有

$$
\begin{aligned}
(X^{\dot\alpha}A)D_{\dot\alpha}
&=
\epsilon^{\dot\alpha\dot\beta}
(X_{\dot\beta}A)D_{\dot\alpha}\\
&=
-\epsilon^{\dot\alpha\dot\beta}
(X_{\dot\alpha}A)D_{\dot\beta}\\
&=
-(X_{\dot\alpha}A)D^{\dot\alpha}.
\end{aligned}
$$

因此 standard AD order 为

$$
\boxed{
\Gamma_{AD}
=
\frac{\lambda_1}{96}
\mathbb F^{AB}{}_{DE}
\left[
(-2\alpha+\beta)
(p_{\dot\alpha}A^D)D^{E\dot\alpha}
+
(-\alpha+2\beta)
(q_{\dot\alpha}A^D)D^{E\dot\alpha}
\right]}.
$$

## 11.4 缺失的 reflected equality

当前输入没有提供

$$
G_{01,S}^{AD},\qquad
G_{02,S}^{AD},\qquad
G_{01,L}^{AD},\qquad
G_{02,L}^{AD},
$$

也没有提供 occurrence reflection

$$
\boxed{
\widetilde G_{AD}
=
\mathcal R_{\rm occ,\epsilon}
\widetilde G_{DA}}.
$$

尤其缺少 reflected endpoint transfer 的 global sign。

若额外假设

$$
R_{AD,S}
=
s_{\rm refl}\,
[-2(b'_0+b'_2)]\mu_\ell^2,
\qquad
s_{\rm refl}\in\{+1,-1\},
$$

则

$$
\alpha=\beta=-2s_{\rm refl},
$$

从而

$$
\boxed{
\Gamma_{AD,S}
=
s_{\rm refl}
\frac{\lambda_1}{48}
\mathbb F^{AB}{}_{DE}
\left[
(p_{\dot\alpha}A^D)D^{E\dot\alpha}
-
(q_{\dot\alpha}A^D)D^{E\dot\alpha}
\right]}.
$$

但 $s_{\rm refl}$ 不能由 DA aggregate polynomial、cyclicity 或 epsilon lowering 决定。Epsilon lowering 只给最后一个显式 minus，不给 occurrence-reflection sign。

---

# 12. Final target-blind ordered vector

定义 longitudinal corrections

$$
\delta_p^{DA},\qquad
\delta_q^{DA},
$$

以及完整 reflected corrections

$$
\rho_p^{AD},\qquad
\rho_q^{AD}.
$$

则当前数据允许的唯一严格 ordered vector 是

$$
\boxed{
\vec C_{AA}^{\rm target\mbox{-}blind}
=
\lambda_1
\left(
\frac1{48}+\delta_p^{DA},\;
-\frac1{48}+\delta_q^{DA},\;
\rho_p^{AD},\;
\rho_q^{AD}
\right)}.
$$

其中

$$
(\delta_p^{DA},\delta_q^{DA})
$$

由 occurrence-resolved longitudinal cut 决定，而

$$
(\rho_p^{AD},\rho_q^{AD})
$$

还需要独立 AD row ledger。

因此：

$$
\boxed{\text{The complete ordered vector remains undefined.}}
$$

第一条 missing equality 不是 HT normalization，也不是 route multiplicity，而是

$$
\boxed{
\mathscr E(\widetilde G_{DA,L})
\text{ from an occurrence-tagged longitudinal lift}.
}
$$

AD reflection 是第二条 missing equality。

---

# 13. Final HT comparison

此前记录的 later comparison candidate 是

$$
\Gamma_{AA,G}^{HT\text{-candidate}}
=
\frac{\lambda_1}{8}
\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^DP^{\dot\alpha}A^E
-
(P_{\dot\alpha}A^D)D^{E\dot\alpha}
\right],
$$

即在本 ordered basis 中

$$
\vec C_{HT}
=
\frac{\lambda_1}{8}(1,0,-1,0).
$$

该式在 repository 中明确标为 non-authority review。

而 HT source 本身还有 $1/4$ 与 $\kappa_H^2$、以及 zero-shift factor-two 的 normalization conflicts。

若仅作 diagnostic，非法地设

$$
\delta_p^{DA}=\delta_q^{DA}=0
$$

并选择最有利的 antisymmetric reflection

$$
s_{\rm refl}=-1,
$$

则 selected-only vector 是

$$
\vec C_{\rm diagnostic}
=
\frac{\lambda_1}{48}(1,-1,-1,+1).
$$

与 $\vec C_{HT}$ 的差为

$$
\boxed{
\vec C_{\rm diagnostic}-\vec C_{HT}
=
\frac{\lambda_1}{48}
(-5,-1,+5,+1)}.
$$

因此 diagnostic level 上：

$$
\frac{\lambda_1}{48}
\neq
\frac{\lambda_1}{8}
$$

首先在 $D(q)pA(p)$ coefficient 处相差 factor $6$；同时出现独立的非零结构

$$
\boxed{
-\frac{\lambda_1}{48}D(q)qA(p)}
$$

而 candidate target 的该分量为零。

乘 $6$ 虽可把第一分量变成 $\lambda_1/8$，却同时产生

$$
-\frac{\lambda_1}{8}D(q)qA(p),
$$

并违反 raw action sum、$1/2!$ 与 route census。因此不能这样 repair。

最终判断是：

$$
\boxed{
\begin{gathered}
\text{compact Hessians: proved},\\
72\text{ multiplicity: disproved},\\
\Gamma_{DA,S}:\text{ fixed as }\lambda_1(1,-1)/48,\\
\Gamma_{DA,\rm full}:\text{ undefined at longitudinal occurrence lift},\\
\Gamma_{AD,\rm full}:\text{ additionally undefined at reflected occurrence map}.
\end{gathered}}
$$
