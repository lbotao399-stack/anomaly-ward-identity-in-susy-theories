STATUS: PARTIAL_ACCEPT__EDGEWISE_O05_O06_AND_FP_ZERO__ABSOLUTE_SOURCE_HESSIAN_NORMALIZATION_OPEN

## 记号 / Notation

$$
Q:=p+q,\qquad
P_3:=D_0D_1D_2,\qquad
P_{\widehat e}:=\prod_{j\neq e}D_j .
$$

$$
\bar r_e^{\,2}:=\det_4(r_e),\qquad
\mu_\ell^2:=\bar r_e^{\,2}-r_{e,d}^{\,2}.
$$

$\mathscr Q_{\omega e}$ 表示 occurrence $\omega$ 在 edge $e$ 上、冻结的 source identity 中乘 $D_+$ 的剩余有序 $D$-word；定义

$$
\mathscr H_{\omega e}:=
D_+\bar D^2D^2\big|_{\omega,e}.
$$

线性 antichiral field-strength projector 记为

$$
\Pi_{\dot\alpha}^{(-)}:=-\frac14D^2\bar D_{\dot\alpha}.
$$

共同 color tensor 记为

$$
\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}.
$$

---

# Gate verdict

$$
\boxed{\texttt{FAIL\_CLOSED}}
$$

Gauge-fixing/contact quotient 可以 edgewise 闭合到给定的 $N_{AD}^{\rm ev},N_{DA}^{\rm ev}$；FP Schwinger family 的净贡献严格为零；NK 在此 conditional slice 中不出现。

但是，给定数据没有锁定 ordered bilocal source 的 occurrence-resolved two-vector Hessian。因此不能把下面算出的 target-blind route vector 提升为一个绝对的 $\lambda_1$-normalized AD/DA coefficient vector。

第一个缺失 operator 是

$$
\boxed{
\mathbb H^{\,o;MN}_{J,-;\dot1\dot2}
:=
\left.
\Pi_{\dot1}^{(-),L}\Pi_{\dot2}^{(-),R}
\frac{\vec\delta^{\,2}}{\delta V^M\,\delta V^N}
\left[
D_-\frac{\delta S_J}{\delta J_o}
\right]
\right|_{V=0},
\qquad o\in\{AD,DA\}.}
$$

它固定：

$$
\text{O05/O06 occurrence coefficient},\quad
\text{source sign},\quad
\text{common graph normalization},\quad
\text{background/quantum port map}.
$$

当前 proposal 自身也承认 ordered bilocal source、background/quantum port grammar 和完整 contact/longitudinal orbit 尚未锁定；其 Schwinger cut sign 仍是 recorded primitive。

---

# 1. Edgewise longitudinal–gauge-fixing–contact identity

由

$$
\mathcal P_0
=
\frac{\bar D^2D^2+D^2\bar D^2}{16\Box},
$$

有

$$
\begin{aligned}
8D_+\Box\mathcal P_0
&=
8D_+\frac{\bar D^2D^2+D^2\bar D^2}{16}\\
&=
\frac12D_+\bar D^2D^2
+\frac12D_+D^2\bar D^2.
\end{aligned}
$$

因为

$$
D_+D^2=0,
$$

所以

$$
\boxed{
8D_+\Box\mathcal P_0
=
\frac12D_+\bar D^2D^2.}
$$

这正好抵消 frozen source identity 的第二项：

$$
\begin{aligned}
\mathscr L_{\omega e}
&=
-8\mathscr Q_{\omega e}
\frac{\bar r_e^{\,2}}{P_3}
-\frac12\mathscr H_{\omega e}\frac1{P_3},\\[1mm]
\mathscr G_{\omega e}
&=
+\frac12\mathscr H_{\omega e}\frac1{P_3}.
\end{aligned}
$$

因此

$$
\mathscr L_{\omega e}+\mathscr G_{\omega e}
=
-8\mathscr Q_{\omega e}
\frac{\bar r_e^{\,2}}{P_3}.
$$

O05/O06 inverse-kernel contact 是

$$
\mathscr C_{\omega e}
=
+8\mathscr Q_{\omega e}\frac1{P_{\widehat e}}.
$$

在合并不同 denominator 之前保留两项：

$$
\boxed{
\mathscr L_{\omega e}
+\mathscr G_{\omega e}
+\mathscr C_{\omega e}
=
-8\mathscr Q_{\omega e}
\frac{\bar r_e^{\,2}}{P_3}
+
8\mathscr Q_{\omega e}
\frac1{P_{\widehat e}}.}
$$

随后才使用

$$
\frac{\bar r_e^{\,2}}{P_3}
-
\frac1{P_{\widehat e}}
=
\frac{\mu_\ell^2}{P_3},
$$

得到

$$
\boxed{
\mathscr L_{\omega e}
+\mathscr G_{\omega e}
+\mathscr C_{\omega e}
=
-8\mathscr Q_{\omega e}
\frac{\mu_\ell^2}{P_3}.}
$$

相应的 full-$d$ inverse-kernel row 是

$$
-8\mathscr Q_{\omega e}
\frac{r_{e,d}^{\,2}}{P_3}
+
8\mathscr Q_{\omega e}
\frac1{P_{\widehat e}}
=0.
$$

$\Box\mathcal P_0$ 是 Step 5A.70 的 gauge-fixing quadratic row，而 projectors 及其 $D$-identities 只在 conditional Fermi–Feynman section 内成立。

## 三个 inverse-kernel edges

### $e=0$

$$
\boxed{
\frac{r_{0,d}^2}{D_0D_1D_2}
-\frac1{D_1D_2}=0,}
$$

$$
\boxed{
\frac{\bar r_0^2}{D_0D_1D_2}
-\frac1{D_1D_2}
=
\frac{\mu_\ell^2}{D_0D_1D_2}.}
$$

### $e=1$

$$
\boxed{
\frac{r_{1,d}^2}{D_0D_1D_2}
-\frac1{D_0D_2}=0,}
$$

$$
\boxed{
\frac{\bar r_1^2}{D_0D_1D_2}
-\frac1{D_0D_2}
=
\frac{\mu_\ell^2}{D_0D_1D_2}.}
$$

### $e=2$

$$
\boxed{
\frac{r_{2,d}^2}{D_0D_1D_2}
-\frac1{D_0D_1}=0,}
$$

$$
\boxed{
\frac{\bar r_2^2}{D_0D_1D_2}
-\frac1{D_0D_1}
=
\frac{\mu_\ell^2}{D_0D_1D_2}.}
$$

## Contact fractions：不跨 denominator 相消

$$
\boxed{
\mathcal C_{AD}
=
\frac{7i\,q_+}{D_1D_2}
+
\frac{2i\,q_+}{D_0D_1}
+
\frac{0}{D_0D_2}.}
$$

$$
\boxed{
\mathcal C_{DA}
=
-\frac{i\,q_+}{2D_1D_2}
+
\frac{iQ_+}{D_0D_1}
+
\frac{iQ_+}{D_0D_2}.}
$$

其中顺序严格是

$$
\begin{array}{c|c}
O05,e=0&D_1D_2\\
O05,e=2&D_0D_1\\
O06,e=1&D_0D_2.
\end{array}
$$

这些 contact 是上述 inverse-kernel brackets 的 two-denominator members；不能在形成 $N^{\rm ev}$ 后再作为新的 finite diagrams 加一次。

---

# 2. FP Euler bubble

## 2.1 从 Step 5A.57 导出 $sV$

保留 $V^0,V^1$。

$p=q=0$ 给出

$$
sV^{(0)}=i(\widetilde c-c).
$$

$p=1,q=0$：

$$
iB_1\left(V\widetilde c+Vc\right)
=
-\frac i2\left(V\widetilde c+Vc\right).
$$

$p=0,q=1$：

$$
iB_1\left(-\widetilde cV-cV\right)
=
+\frac i2\left(\widetilde cV+cV\right).
$$

所以

$$
\boxed{
sV
=
i(\widetilde c-c)
+
\frac i2
\left(
\widetilde cV+cV-V\widetilde c-Vc
\right)
+O(V^2).}
$$

Step 5A.57–5A.60 给出的 exact BRST series、FP action、ghost-word coefficients 和 free term 正是这些公式的 authority source。

## 2.2 Free kernels 与 ordered propagators

由

$$
S_{\rm FP}^{(2)}
=
\frac i4\int_+c'_+\bar D^2\widetilde c
-\frac i4\int_-\widetilde c'_-D^2c,
$$

定义

$$
K_+:=\frac i4\bar D^2,\qquad
K_-:=-\frac i4D^2.
$$

其 constrained inverses 是

$$
K_+^{-1}
=
-\frac i4\frac{D^2}{\Box},
\qquad
K_-^{-1}
=
+\frac i4\frac{\bar D^2}{\Box},
$$

因为

$$
\begin{aligned}
K_+K_+^{-1}
&=
\left(\frac i4\bar D^2\right)
\left(-\frac i4\frac{D^2}{\Box}\right)\\
&=
\frac{\bar D^2D^2}{16\Box}
=\mathcal P_+,
\end{aligned}
$$

$$
\begin{aligned}
K_-K_-^{-1}
&=
\left(-\frac i4D^2\right)
\left(+\frac i4\frac{\bar D^2}{\Box}\right)\\
&=
\frac{D^2\bar D^2}{16\Box}
=\mathcal P_-.
\end{aligned}
$$

故 ordered ghost propagators 为

$$
\boxed{
\left\langle
\widetilde c^A(1)c_+^{\prime B}(2)
\right\rangle_0
=
-\frac{i\hbar}{4}\kappa^{AB}
\frac{D_1^2}{\Box_1}\delta^8_{12},}
$$

$$
\boxed{
\left\langle
c^A(1)\widetilde c_-^{\prime B}(2)
\right\rangle_0
=
+\frac{i\hbar}{4}\kappa^{AB}
\frac{\bar D_1^2}{\Box_1}\delta^8_{12}.}
$$

反向 ordered contraction 带 odd transpose sign：

$$
G_{c'\widetilde c}(2,1)
=
-G_{\widetilde c c'}(1,2)^T,
$$

$$
G_{\widetilde c'c}(2,1)
=
-G_{c\widetilde c'}(1,2)^T.
$$

## 2.3 Cubic vertex

$$
\boxed{
S_{\rm FP}^{(3)}
=
\frac i8\int_+
c'_+\bar D^2
\left(
[\widetilde c,V]+[c,V]
\right)
+
\frac i8\int_-
\widetilde c'_-
D^2
\left(
[\widetilde c,V]+[c,V]
\right).}
$$

一个 connected two-vertex ghost loop 只能选择

$$
\boxed{
\mathcal V_+
=
\frac i8\int_+
c'_+\bar D^2[c,V],}
$$

$$
\boxed{
\mathcal V_-
=
\frac i8\int_-
\widetilde c'_-
D^2[\widetilde c,V].}
$$

其余选择在每个 vertex 内形成 tadpole，而不是连接两个 vertices 的 bubble。

采用

$$
[T_B,T_M]=ic_{BM}{}^CT_C,
$$

component vertex 为

$$
\boxed{
(\mathcal V_+)_{ABM}
=
-\frac18\kappa_{AC}c_{BM}{}^C\,\bar D^2,}
$$

$$
\boxed{
(\mathcal V_-)_{ABM}
=
-\frac18\kappa_{AC}c_{BM}{}^C\,D^2.}
$$

Color word：

$$
\boxed{
\mathcal C_{\rm FP}^{MN}
=
\operatorname{Tr}_{\rm ad}
(\operatorname{ad}_{T_M}\operatorname{ad}_{T_N})
=
-c_{MB}{}^A c_{NA}{}^B.}
$$

两个 component vertices 给出

$$
\left(-\frac18\right)^2=\frac1{64}.
$$

closed Grassmann loop 给出

$$
\boxed{s_{\rm loop}^{\rm FP}=-1.}
$$

故 stripped primitive sign 是

$$
\boxed{-\frac1{64}\mathcal C_{\rm FP}^{MN}.}
$$

## 2.4 $D$-word 与 full-$d$ cut

以循环起点不同只作 cyclic rotation。一个非零 representative word 是

$$
\boxed{
\mathscr W_{\rm FP}^{DD}
=
\Pi_{\dot1}^{(-)}
\operatorname{Tr}_{D}
\left[
\bar D^2\,\operatorname{ad}_{V_L}\,
\frac{\bar D^2}{\Box_{s_0}}\,
D^2\,\operatorname{ad}_{V_R}\,
\frac{D^2}{\Box_{s_1}}
\right]
\Pi_{\dot2}^{(-)}.}
$$

这里 multiplication operators $\operatorname{ad}_{V_L},\operatorname{ad}_{V_R}$ 把相邻的相同 $D$-powers 隔开，因此 uncut word 不是 nilpotency zero：

$$
\boxed{\mathcal B_{\rm FP}^{DD}\neq0}
$$

对于 generic nonabelian color。

但 Euler cut 在每条 ghost edge 上先局部形成

$$
\bar D^2D^2\bar D^2
=
16\Box\,\bar D^2,
$$

或

$$
D^2\bar D^2D^2
=
16\Box\,D^2.
$$

取 bubble routing

$$
s_0=\ell,\qquad s_1=\ell+K,
$$

full-$d$ inverse-kernel cuts 分别是

$$
\boxed{
\frac{s_{0,d}^2}{s_0^2s_1^2}
-\frac1{s_1^2}=0,}
$$

$$
\boxed{
\frac{s_{1,d}^2}{s_0^2s_1^2}
-\frac1{s_0^2}=0.}
$$

这里 FP quadratic kernel 是 $\Box$-kernel，不是 frozen source 的 $\det_4$-kernel。因此不能把

$$
s_{e,d}^2
$$

替换成

$$
\bar s_e^2
$$

来制造 ghost $\mu_\ell^2$ residue。

于是

$$
\boxed{
\Gamma_{\rm FP,Euler}^{DD}
=
\mathcal B_{\rm FP}^{DD}\neq0,}
$$

$$
\boxed{
\Gamma_{\rm FP,cut}^{DD}
=
-\mathcal B_{\rm FP}^{DD},}
$$

$$
\boxed{
\Gamma_{\rm FP,full\ Schwinger\ family}^{DD}=0,}
$$

$$
\boxed{
R_{\rm FP}^{\mu_\ell^2}=0.}
$$

这是 operator-level inverse-kernel cancellation，不是 verbal gauge-independence argument。

---

# 3. Nielsen–Kallosh branch

Step 5A 明确写出：由 5A.43–5A.48 选择的 gauge-fixing construction **不选择 separated Nielsen–Kallosh factor**。

所以在本 conditional slice 内：

$$
\boxed{\Gamma_{\rm NK}\ \text{is absent from the selected graph set}.}
$$

这不等于

$$
\Gamma_{\rm NK}=0
$$

作为一个独立 determinant 的陈述；也不能给它猜测 multiplicity 或 guessed weight。

---

# 4. AD 与 DA 独立重算

## 4.1 Color

AD color：

$$
\mathbb F_{AD}^{AB}{}_{DE}
=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}.
$$

反向 ordering：

$$
\mathbb F_{DA}^{BA}{}_{ED}
=
\kappa^{BU}\kappa^{AV}\kappa^{CC'}
c_{UCE}c_{VC'D}.
$$

作 dummy relabeling

$$
U\leftrightarrow V,\qquad C\leftrightarrow C',
$$

得到

$$
\begin{aligned}
\mathbb F_{DA}^{BA}{}_{ED}
&=
\kappa^{BV}\kappa^{AU}\kappa^{C'C}
c_{VC'E}c_{UCD}\\
&=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}\\
&=
\boxed{\mathbb F_{AD}^{AB}{}_{DE}}.
\end{aligned}
$$

没有 reflection multiplicity。

## 4.2 Koszul

$$
|A|=0,\qquad |D|=1,\qquad |D_-|=1.
$$

AD：

$$
D_-(AD)
=
(D_-A)D+A(D_-D)
=
(D_-A)D.
$$

DA：

$$
D_-(DA)
=
(D_-D)A-D(D_-A)
=
-D(D_-A).
$$

将 DA 输出改写到同一 canonical odd-field order 时再产生一个负号：

$$
-D_{\dot2}^E(D_-A)_{\dot1}^D
=
+(D_-A)_{\dot1}^DD_{\dot2}^E.
$$

所以

$$
\boxed{
(-1)_{\rm Leibniz}
(-1)_{\rm odd\ output\ swap}
=+1.}
$$

AD、DA 具有同一 overall Koszul sign；剩余 relative sign 已包含在给定的 $N_{AD}^{\rm ev},N_{DA}^{\rm ev}$ 中。

## 4.3 Dotted raising/lowering

采用

$$
\epsilon^{\dot1\dot2}=1,
\qquad
\epsilon^{\dot2\dot1}=-1,
$$

则

$$
Y^{\dot1}=Y_{\dot2},
\qquad
Y^{\dot2}=-Y_{\dot1}.
$$

因此

$$
X_{\dot\alpha}Y^{\dot\alpha}
=
X_{\dot1}Y_{\dot2}
-
X_{\dot2}Y_{\dot1}.
$$

固定 external order

$$
\text{left }\dot1,\qquad \text{right }\dot2
$$

选择的是第一项，其 coefficient 是

$$
\boxed{+1}.
$$

source dotted label 与 raised external dotted index 不能再作同一 index identification。

---

## 4.4 Rank-one triangle integral

取

$$
x+y+z=1,\qquad x,y,z\geq0,
$$

$$
\frac1{D_0D_1D_2}
=
2\int_{\Delta_2}
\frac{dx\,dy\,dz\,\delta(1-x-y-z)}
{(L^2+\Delta)^3},
$$

其中

$$
L
=
\ell+(y+z)p+zq,
$$

$$
\Delta
=
xy\,p^2+xz\,Q^2+yz\,q^2.
$$

simplex moments：

$$
\int_{\Delta_2}1=\frac12,
\qquad
\int_{\Delta_2}x
=
\int_{\Delta_2}y
=
\int_{\Delta_2}z
=
\frac16.
$$

### $\mu_\ell^2$ scalar integral

定义

$$
J_2(\Delta)
:=
\int_L\frac1{(L^2+\Delta)^2},
$$

$$
J_3(\Delta)
:=
\int_L\frac1{(L^2+\Delta)^3}.
$$

有

$$
\Delta J_3=\frac\epsilon2J_2.
$$

由 rotational split，

$$
\begin{aligned}
\int_L
\frac{\mu_L^2}{(L^2+\Delta)^3}
&=
\frac{2\epsilon}{4-2\epsilon}
\int_L
\frac{L^2}{(L^2+\Delta)^3}\\
&=
\frac{2\epsilon}{4-2\epsilon}
\left(J_2-\Delta J_3\right)\\
&=
\frac{2\epsilon}{4-2\epsilon}
\left(1-\frac\epsilon2\right)J_2\\
&=
\frac{\epsilon}{2}J_2.
\end{aligned}
$$

因为

$$
\operatorname{Res}_{\epsilon=0}J_2
=
\frac1{16\pi^2},
$$

所以

$$
\operatorname{Fin}_{\epsilon=0}
\int_L\frac{\mu_L^2}{(L^2+\Delta)^3}
=
\frac1{32\pi^2}.
$$

完整 constant triangle：

$$
2\int_{\Delta_2}\frac1{32\pi^2}
=
2\left(\frac12\right)\frac1{32\pi^2}
=
\boxed{\frac1{32\pi^2}}.
$$

---

## 4.5 AD

$$
N_{AD}^{\rm ev}
=
\frac{i}{16}\mu_\ell^2
\left(\ell+p+\frac12q\right)_{+\dot1}.
$$

由

$$
\ell=L-(y+z)p-zq,
$$

得

$$
\begin{aligned}
\ell+p+\frac12q
&=
L-(y+z)p-zq+p+\frac12q\\
&=
L+xp+\left(\frac12-z\right)q.
\end{aligned}
$$

odd $L$ integral 为零。于是

$$
2\int_{\Delta_2}x
=
2\left(\frac16\right)
=
\frac13,
$$

$$
\begin{aligned}
2\int_{\Delta_2}
\left(\frac12-z\right)
&=
2\left[
\frac12\left(\frac12\right)-\frac16
\right]\\
&=
2\left(\frac14-\frac16\right)\\
&=
\frac16.
\end{aligned}
$$

因此

$$
\boxed{
\int_\ell
\frac{N_{AD}^{\rm ev}}{D_0D_1D_2}
=
\frac{i}{512\pi^2}
\left(
\frac13p+\frac16q
\right)_{+\dot1}.}
$$

又因为 $Q=p+q$，

$$
\frac13p+\frac16q
=
\frac13Q-\frac16q.
$$

AD 的 ordered external placements 是

$$
(k_L,k_R)=(q,-Q),
$$

故

$$
\boxed{
\frac13p+\frac16q
=
-\frac12
\left[
\frac13k_L+\frac23k_R
\right].}
$$

---

## 4.6 DA

$$
N_{DA}^{\rm ev}
=
-\frac{i}{16}\mu_\ell^2\ell_{+\dot1}.
$$

$$
-\ell
=
-L+(y+z)p+zq.
$$

$$
2\int_{\Delta_2}(y+z)
=
2\left(\frac16+\frac16\right)
=
\frac23,
$$

$$
2\int_{\Delta_2}z
=
\frac13.
$$

所以

$$
\boxed{
\int_\ell
\frac{N_{DA}^{\rm ev}}{D_0D_1D_2}
=
\frac{i}{512\pi^2}
\left(
\frac23p+\frac13q
\right)_{+\dot1}.}
$$

并且

$$
\frac23p+\frac13q
=
\frac23Q-\frac13q.
$$

DA 的 ordered placements 是

$$
(k_L,k_R)=(-Q,q),
$$

所以

$$
\boxed{
\frac23p+\frac13q
=
-\left[
\frac23k_L+\frac13k_R
\right].}
$$

因此，给定 route sums 独立产生

$$
AD:\quad
-\frac12\left(\frac13,\frac23\right)_{(q,-Q)},
$$

$$
DA:\quad
-\left(\frac23,\frac13\right)_{(-Q,q)}.
$$

共同 Fourier/operator sign 抽出以后，绝对可靠的 relative ordering 是

$$
\boxed{AD:DA=1:2.}
$$

---

# 5. Finite occurrence ledger

| family / occurrence | $AD$ | $DA$ | one-loop 1PI status |
| --- | --- | --- | --- |
| $O05,e=0$ | $\dfrac{7iq_+}{D_1D_2}$ | $-\dfrac{iq_+}{2D_1D_2}$ | inverse-kernel contact member |
| $O05,e=2$ | $\dfrac{2iq_+}{D_0D_1}$ | $\dfrac{iQ_+}{D_0D_1}$ | inverse-kernel contact member |
| $O06,e=1$ | $0$ | $\dfrac{iQ_+}{D_0D_2}$ | chiral + antichiral quartic sum |
| longitudinal + GF + O05/O06 | $\dfrac{i}{512\pi^2}(\frac13p+\frac16q)_+$ | $\dfrac{i}{512\pi^2}(\frac23p+\frac13q)_+$ | supplied $N^{\rm ev}$ normalization |
| FP Euler bubble | $+\mathcal B_{\rm FP}^{DD}$ | $+\mathcal B_{\rm FP}^{DD}$ | individually nonzero |
| FP full-$d$ cut | $-\mathcal B_{\rm FP}^{DD}$ | $-\mathcal B_{\rm FP}^{DD}$ | separate Schwinger member |
| FP $\mu_\ell^2$ remainder | $0$ | $0$ | exact |
| separated NK | not selected | not selected | no assigned weight |
| sampled $O07$ | $0$ | $0$ | exact tadpole zero |
| matter Euler/current | $+\mathcal M_d$ | $+\mathcal M_d$ | retain separately |
| matter explicit contact | $-\mathcal M_d$ | $-\mathcal M_d$ | retain separately |
| matter family sum | $0$ | $0$ | exact before regulation |
| 42 spectators | connected, 1PR | connected, 1PR | zero in the 1PI quotient |
| spectator control $F_{01;10}$ | $0$ | $0$ | exact color control |

---

# Target-blind ordered vector

在给定 $N^{\rm ev}$ normalization 中，

$$
\boxed{
\vec{\mathcal V}_{AD/DA}^{\,\mathrm{cert}}
=
\frac{i}{512\pi^2}
\begin{pmatrix}
\left(\dfrac13p+\dfrac16q\right)_{+\dot1}\\[2mm]
\left(\dfrac23p+\dfrac13q\right)_{+\dot1}
\end{pmatrix}.}
$$

恢复共同 color：

$$
\boxed{
\vec{\Gamma}_{AD/DA}^{\,\mathrm{cert}}
=
\mathcal N_J\,
\mathbb F^{AB}{}_{DE}\,
\frac{i}{512\pi^2}
\begin{pmatrix}
\left(\dfrac13p+\dfrac16q\right)_{+\dot1}\\[2mm]
\left(\dfrac23p+\dfrac13q\right)_{+\dot1}
\end{pmatrix}
D_{\dot1}^DD_{\dot2}^E.}
$$

其中 $\mathcal N_J$ 必须由缺失的 source Hessian

$\mathbb H_{J,-;\dot1\dot2}^{o;MN}$ 固定，不能从 target 填入。

因此唯一 absolute-normalization-independent 的 ordered vector 是

$$
\boxed{
\vec v_{AD/DA}^{\,\mathrm{relative}}=(1,2).}
$$

不能仅凭“sum-to-one”将它改写为

$$
\left(\frac13,\frac23\right),
$$

因为这会人为引入未锁定的 common normalization。

---

# 当前 local derivation 的第一个 invalid assumption

`intrinsic_d_pair_outputs()` 在任何 graph construction、edgewise contact quotient、FP calculation 之前，就把

$$
A>D_{\dot a}:\quad
\left(\frac13,\frac23\right),
$$

$$
D_{\dot a}>A:\quad
\left(\frac23,\frac13\right)
$$

直接写入 ledger，并把它们解释为 simplex endpoint integrals。

随后 `physical_graph_engine` 直接读取这些 Project-side outputs，作为每个 graph 的 `physical_taylor_expansion`，并把 triangle/contact 标记为 proved；同一个 IR 又明确记录 `GAUGE_FIXING_FP_NK_MEASURE = PENDING_CLEAN_AUDIT`。

因此第一个 invalid assumption 是

$$
\boxed{
\text{“commuting-translation simplex moments”
}
=
\text{“regulated ordered 1PI supergraph coefficients”.}}
$$

Simplex moments 只能分配一个**已经锁定 normalization 的 kernel**；它们不能决定缺失的 ordered source Hessian、occurrence coefficient、FP quotient 或 source-port normalization。Step 5A 自身也明确规定：primitive graph weight 只有在所有 inverse kernels 和 integration cycles 锁定后才能成为 numerical Feynman rule。
