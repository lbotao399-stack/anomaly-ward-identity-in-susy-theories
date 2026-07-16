## 记号 / Notation

$$
\mathcal T_p^{DE}:=
D_{\dot\alpha}^{D}(q)\,p^{\dot\alpha}A^E(p),
\qquad
\mathcal T_q^{DE}:=
D_{\dot\alpha}^{D}(q)\,q^{\dot\alpha}A^E(p),
$$

$$
\widetilde{\mathcal T}_p^{DE}:=
(p_{\dot\alpha}A^D(p))D^{E\dot\alpha}(q),
\qquad
\widetilde{\mathcal T}_q^{DE}:=
(q_{\dot\alpha}A^D(p))D^{E\dot\alpha}(q).
$$

$$
\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E},
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

---

# 1. Explicit retraction of Gate 3

Gate 3 使用了已经撤回的 affine fits $R_0,R_2$。因此下列 Gate-3 conclusions 全部作废：

$$
2\int(R_0+R_2)=-\frac12+\frac i2,
$$

$$
R_0+R_2\longmapsto
\frac12(\mathcal T_p+\mathcal T_q),
$$

$$
\Gamma_{DA}
=
-\frac{\lambda_1}{64}
(\mathcal T_p+\mathcal T_q),
$$

以及从它推出的 reflected $AD$ term、ordered vector 和 HT mismatch。

$$
\boxed{
\text{Gate 3 的 }-\lambda_1/64
\text{ 不是已建立的 AA coefficient.}}
$$

---

# 2. Quadratic occurrence quotients

定义

$$
\zeta:=\ell_0-i\ell_1.
$$

给定的两个 quotients 可严格重写为

$$
\boxed{
Q_0
=
-\frac12\zeta^2
+\left(\frac32-i\right)\zeta
-\frac12+\frac32i,
}
$$

$$
\boxed{
Q_2
=
-\frac12\zeta^2-\frac12\zeta.
}
$$

展开第一式：

$$
\begin{aligned}
-\frac12(\ell_0-i\ell_1)^2
={}&
-\frac12\ell_0^2
+i\ell_0\ell_1
+\frac12\ell_1^2,
\end{aligned}
$$

$$
\begin{aligned}
\left(\frac32-i\right)(\ell_0-i\ell_1)
={}&
\left(\frac32-i\right)\ell_0
-\left(1+\frac32i\right)\ell_1.
\end{aligned}
$$

因此精确恢复

$$
\begin{aligned}
Q_0={}&-\frac12\ell_0^2+i\ell_0\ell_1
+\left(\frac32-i\right)\ell_0
+\frac12\ell_1^2\\
&-\left(1+\frac32i\right)\ell_1
-\frac12+\frac32i,
\end{aligned}
$$

以及

$$
Q_2=
-\frac12\ell_0^2+i\ell_0\ell_1
-\frac12\ell_0+\frac12\ell_1^2+\frac i2\ell_1.
$$

## 2.1 Harmonic check

$$
\partial_{\ell_0}^2Q_0=-1,
\qquad
\partial_{\ell_1}^2Q_0=+1,
\qquad
\partial_{\ell_2}^2Q_0
=
\partial_{\ell_3}^2Q_0=0,
$$

所以

$$
\boxed{\Delta_\ell Q_0=0.}
$$

同理，

$$
\partial_{\ell_0}^2Q_2=-1,
\qquad
\partial_{\ell_1}^2Q_2=+1,
$$

故

$$
\boxed{\Delta_\ell Q_2=0.}
$$

## 2.2 One-point check

在

$$
\ell=(2,-1,1,3)
$$

有

$$
\begin{aligned}
Q_0
={}&
-\frac12(4)+i(2)(-1)
+\left(\frac32-i\right)2
+\frac12\\
&+\left(1+\frac32i\right)
-\frac12+\frac32i\\
={}&2-i,
\end{aligned}
$$

$$
\begin{aligned}
Q_2
={}&
-2-2i-1+\frac12-\frac i2\\
={}&-\frac52(1+i).
\end{aligned}
$$

这恢复了旧 sample 上的 selected values，但现在由完整 quadratic polynomial 给出，而非 affine interpolation。

---

## 2.3 Raw-row replay boundary

每个 occurrence edge 的 row set 可写成

$$
\mathcal R_e
=
\left\{
(F,\eta,\chi),\,
(\partial,\eta,\chi),\,
(0,\eta,\chi)
\right\},
$$

其中

$$
\eta\in\{1,2\}
$$

表示两个 endpoint orderings，

$$
\chi\in\{(+,+),(+,-),(-,+),(-,-)\}
$$

表示四个 action-chirality rows。因此每个 edge 有

$$
3\times2\times4=24
$$

个 raw rows，并且

$$
Q_e=\sum_{\rho\in\mathcal R_e}q_{e,\rho}.
$$

当前 prompt 给出了最终 $Q_e$，但没有给出任何单独的 $q_{e,\rho}$。因此我不能诚实地声称已经从 raw rows 独立重放 $Q_0,Q_2$。

审计停止的第一条 row equality 是例如

$$
\boxed{
q_{0;\,F,\,1,\,(+,+)}(\ell)
=
\text{not supplied}.
}
$$

我没有发现与 $Q_0,Q_2$ 冲突的 raw row；而是没有 row-level data 可用于判定。显示的 aggregate polynomials、harmonicity、sample 和 simplex moments 均一致。

---

# 3. Exact simplex integration

Locked routing 为

$$
r_0=\ell,\qquad
r_1=\ell-q,\qquad
r_2=\ell-p-q,
$$

且

$$
p=e_0,\qquad q=e_1.
$$

写

$$
x+y+z=1,
\qquad
\ell=L+yq+z(p+q).
$$

因此

$$
\ell_0=L_0+z,
\qquad
\ell_1=L_1+y+z.
$$

由于 $Q_e$ harmonic：

- $L_\mu$
- $L_\mu L_\nu$
- 只需把

$$
\ell_0\mapsto z,\qquad
\ell_1\mapsto y+z.
$$

Simplex moments：

$$
2\int_{\Delta_2}1=1,
$$

$$
2\int_{\Delta_2}z=\frac13,
\qquad
2\int_{\Delta_2}(y+z)=\frac23,
$$

$$
2\int_{\Delta_2}z^2=\frac16,
$$

$$
2\int_{\Delta_2}z(y+z)
=
2\left(\frac1{24}+\frac1{12}\right)
=
\frac14,
$$

$$
2\int_{\Delta_2}(y+z)^2
=
2\left(
\frac1{12}+\frac2{24}+\frac1{12}
\right)
=
\frac12.
$$

## 3.1 $Q_0$

Quadratic part：

$$
-\frac12\left(\frac16\right)
+i\left(\frac14\right)
+\frac12\left(\frac12\right)
=
\frac16+\frac i4.
$$

Linear part：

$$
\begin{aligned}
&\left(\frac32-i\right)\frac13
-\left(1+\frac32i\right)\frac23\\
&=
\frac12-\frac i3
-\frac23-i\\
&=
-\frac16-\frac43i.
\end{aligned}
$$

Constant part：

$$
-\frac12+\frac32i.
$$

总和：

$$
\begin{aligned}
2\int_{\Delta_2}Q_0
&=
\left(\frac16-\frac16-\frac12\right)
+i\left(
\frac14-\frac43+\frac32
\right)\\
&=
-\frac12
+i\left(
\frac3{12}-\frac{16}{12}+\frac{18}{12}
\right)\\
&=
\boxed{-\frac12+\frac5{12}i}.
\end{aligned}
$$

## 3.2 $Q_2$

Quadratic part仍为

$$
\frac16+\frac i4.
$$

Linear part：

$$
-\frac12\frac13+\frac i2\frac23
=
-\frac16+\frac i3.
$$

所以

$$
\boxed{
2\int_{\Delta_2}Q_2
=
\frac7{12}i}.
$$

最后

$$
\boxed{
2\int_{\Delta_2}(Q_0+Q_2)
=
-\frac12+i}.
$$

---

# 4. Occurrence-preserving Schwinger contacts

对每一 raw row $\rho\in\mathcal R_e$，定义

$$
N_{S,e,\rho}=\bar r_e^2q_{e,\rho},
$$

$$
L_{e,\rho}
:=
N_{{\rm full},e,\rho}
-\bar r_e^2q_{e,\rho}.
$$

同一 full action 的 Schwinger derivative 产生

$$
\boxed{
C_{e,d,\rho}
=
-L_{e,\rho}
-r_{e,d}^2q_{e,\rho}.
}
$$

于是逐 row：

$$
\begin{aligned}
N_{{\rm full},e,\rho}+C_{e,d,\rho}
&=
\bar r_e^2q_{e,\rho}+L_{e,\rho}
-L_{e,\rho}-r_{e,d}^2q_{e,\rho}\\
&=
(\bar r_e^2-r_{e,d}^2)q_{e,\rho}\\
&=
\boxed{\mu_\ell^2q_{e,\rho}}.
\end{aligned}
$$

若 parent 本身也作 full-$d$ replacement，

$$
N_{{\rm full},e,\rho}^{(d)}
=
r_{e,d}^2q_{e,\rho}+L_{e,\rho},
$$

则

$$
\begin{aligned}
N_{{\rm full},e,\rho}^{(d)}
+C_{e,d,\rho}
&=
r_{e,d}^2q_{e,\rho}+L_{e,\rho}
-L_{e,\rho}-r_{e,d}^2q_{e,\rho}\\
&=
\boxed{0}.
\end{aligned}
$$

求和得到

$$
C_{e,d}=-L_e-r_{e,d}^2Q_e,
$$

$$
\boxed{
N_{{\rm full},e}+C_{e,d}
=
\mu_\ell^2Q_e},
$$

$$
\boxed{
N_{{\rm full},e}^{(d)}+C_{e,d}=0}.
$$

在 integrand level，

$$
\begin{aligned}
\frac{C_{e,d}}{D_0D_1D_2}
&=
-\frac{L_e}{D_0D_1D_2}
-\frac{r_{e,d}^2Q_e}{D_0D_1D_2}\\
&=
-\frac{L_e}{D_0D_1D_2}
-\frac{Q_e}{\prod_{j\neq e}D_j}.
\end{aligned}
$$

因此 affine 或 quadratic two-denominator contact 均不能删除。

$$
\boxed{
\text{不存在独立的 graph-specific }(4-d)\text{ factor}.}
$$

唯一 remainder 是

$$
\boxed{
\frac{\mu_\ell^2Q_e}{D_0D_1D_2}}.
$$

---

# 5. Primitive normalization ledger

Step 5A 锁定

$$
\eta_E=-1,\qquad h=g^{-2},
$$

以及 all-order convolution (5A.52)。

## 5.1 Source Hessian coefficient — already inside $Q_e$

$$
A_c^{(1)}
=
-\frac1{4\sqrt2}
D_+\bar D^2D_+u.
$$

对于 $T_0$：

$$
\begin{aligned}
(-D_-A_c^{(1)})A_c^{(1)}
&=
\left(
+\frac1{4\sqrt2}
D_-D_+\bar D^2D_+u
\right)
\left(
-\frac1{4\sqrt2}
D_+\bar D^2D_+u
\right)\\
&=
-\frac1{32}
\big(D_-D_+\bar D^2D_+u\big)
\big(D_+\bar D^2D_+u\big).
\end{aligned}
$$

所以在 $D_-D_+$ word basis 中：

$$
\boxed{c_{\rm source}=-\frac1{32}.}
$$

用

$$
D_-D_+=\frac12D^2
$$

改写：

$$
\boxed{c_{\rm source}^{D^2\text{-basis}}=-\frac1{64}.}
$$

这个 $-1/64$ 是 **source-word coefficient**，已经包含在 $Q_e$ 中；它不是最终 loop coefficient，不能再次乘入。

Berezin factor

$$
D^2\bar D^2\delta^4(\theta)\big|=16
$$

也已经包含在 $Q_e$。

---

## 5.2 Full polarized cubic exponent vertices

Field-strength definitions 由

$$
\mathcal W_a=-\frac18\bar D^2\big[e^{-V}(D_ae^V)\big],
\qquad
\widetilde{\mathcal W}_{\dot a}
=+\frac18D^2\big[e^V(\bar D_{\dot a}e^{-V})\big]
$$

锁定。

Full polarization 不能再写成 fixed-$W$ two-port Hessian，但每个 trilinear family 的 common exponent prefactor 仍是

$$
\boxed{
v_W=-\frac{ig}{4\hbar}},
$$

$$
\boxed{
v_{\widetilde W}=+\frac{ig}{4\hbar}}.
$$

这两个 numbers 只应各乘一次。三种 external-position families 已在 $Q_e$ 内部。

---

## 5.3 Three propagators

按 occurrence/color labels：

$$
\boxed{
P_0
=
-\frac{\hbar\kappa^{AU}}{D_0}},
$$

$$
\boxed{
P_1
=
-\frac{\hbar\kappa^{CC'}}{D_1}},
$$

$$
\boxed{
P_2
=
-\frac{\hbar\kappa^{BV}}{D_2}}.
$$

Scalar/sign product：

$$
(-\hbar)^3=-\hbar^3.
$$

Color contraction：

$$
\boxed{
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}
=
\mathbb F^{AB}{}_{DE}.}
$$

没有额外 color sign，也不作 Casimir reduction。

---

## 5.4 Taylor and labeled Wick factors

两 cubic insertions 的 Taylor factor：

$$
\boxed{t_2=\frac1{2!}=\frac12.}
$$

两个 labeled exponent orderings：

$$
S_WS_{\widetilde W},
\qquad
S_{\widetilde W}S_W.
$$

两个 cubic actions 均为 Grassmann-even，因此两项相等：

$$
\boxed{m_{\rm label}=2.}
$$

于是

$$
\boxed{t_2m_{\rm label}=1.}
$$

$Q_e$ 中的 three external families、endpoint orderings 与 four internal action-chirality rows 不是这个额外的 vertex-label exchange，不能再被当作 multiplicity。

---

## 5.5 Product before the component-to-letter map

不提前合并：

$$
\frac12,
$$

$$
2,
$$

$$
-\frac{ig}{4\hbar},
$$

$$
+\frac{ig}{4\hbar},
$$

$$
-\hbar,
\qquad
-\hbar,
\qquad
-\hbar,
$$

$$
\mathbb F^{AB}{}_{DE},
$$

$$
\frac1{32\pi^2}.
$$

逐步乘：

$$
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
=
+\frac{g^2}{16\hbar^2},
$$

$$
\frac{g^2}{16\hbar^2}
(-\hbar)^3
=
-\frac{\hbar g^2}{16},
$$

$$
\frac12(2)
\left(-\frac{\hbar g^2}{16}\right)
=
-\frac{\hbar g^2}{16},
$$

$$
-\frac{\hbar g^2}{16}
\frac1{32\pi^2}
=
-\frac{\hbar g^2}{512\pi^2}
=
\boxed{-\frac{\lambda_1}{32}}.
$$

因此 locked primitive ledger 的确切结论是：

$$
\boxed{
\Gamma_{\rm component}
=
-\frac{\lambda_1}{32}\,
\mathbb F^{AB}{}_{DE}
\left[
2\int_{\Delta_2}(Q_0+Q_2)
\right].
}
$$

在第一 frame：

$$
\boxed{
\Gamma_{\rm component}^{F_1}
=
-\frac{\lambda_1}{32}
\left(-\frac12+i\right)
\mathbb F^{AB}{}_{DE}.}
$$

即

$$
\Gamma_{\rm component}^{F_1}
=
\left(
\frac{\lambda_1}{64}
-\frac{i\lambda_1}{32}
\right)
\mathbb F^{AB}{}_{DE}.
$$

这是一个 **fixed component value**，尚不是四个 ordered tensor coefficients。

---

# 6. Gate 3 的第一个 primitive normalization error

Gate 3 的 action、propagator、Taylor、Wick product 在 component normalization 下给出的共同因子其实是

$$
-\frac{\lambda_1}{32}.
$$

Gate 3 得到额外 denominator $2$，从而写成 $-\lambda_1/64$，来自它使用了撤回的 equality

$$
2\int(R_0+R_2)
=
-\frac12+\frac i2
$$

并进一步宣称

$$
-\frac12+\frac i2
=
\frac12\operatorname{ev}_{F_1}
(\mathcal T_p+\mathcal T_q).
$$

新 quotient 给出

$$
-\frac12+i,
$$

所以该 equality 已严格失败。

即使暂时沿用 Gate 3 未证明的单-frame assignment

$$
\operatorname{ev}_{F_1}(\mathcal T_p)=-1,
\qquad
\operatorname{ev}_{F_1}(\mathcal T_q)=i,
$$

也只能得到

$$
-\frac12+i
=
\frac12\operatorname{ev}_{F_1}(\mathcal T_p)
+
1\cdot\operatorname{ev}_{F_1}(\mathcal T_q),
$$

而不是

$$
\frac12\operatorname{ev}_{F_1}
(\mathcal T_p+\mathcal T_q).
$$

所以第一处 exact mismatch 是

$$
\boxed{
(c_p,c_q)_{\rm Gate\,3}
=
\left(\frac12,\frac12\right)
\quad\longrightarrow\quad
\left(\frac12,1\right)
}
$$

在 Gate-3 自己的 one-frame normalization 下。

因此：

- $64$
- common minus sign 在 primitive ledger 中来自

$$
(-\hbar)^3,
$$

$4-d$
- $AD$

---

# 7. Two-frame reconstruction

Authority sigma matrices 为

$$
\sigma_E^m=(-i\sigma^1,-i\sigma^2,-i\sigma^3,\mathbf1),
$$

$$
\sigma_E^m\bar\sigma_E^n+\sigma_E^n\bar\sigma_E^m
=
2\delta^{mn}\mathbf1.
$$

在 component-engine ordering

$$
(e_0,e_1,e_2,e_3)
\leftrightarrow
(\sigma_E^1,\sigma_E^2,\sigma_E^3,\sigma_E^4),
$$

有

$$
-i\sigma_E\!\cdot e_0=-\sigma^1,
\qquad
-i\sigma_E\!\cdot e_1=-\sigma^2,
$$

$$
-i\sigma_E\!\cdot e_2=-\sigma^3,
\qquad
-i\sigma_E\!\cdot e_3=-i\mathbf1.
$$

## Frame $F_1$

$$
p=e_0,\qquad q=e_1,\qquad \dot\alpha=\dot+.
$$

若 canonical external components 被单位归一化，则

$$
\operatorname{ev}_{F_1}(\mathcal T_p)=-1,
\qquad
\operatorname{ev}_{F_1}(\mathcal T_q)=i.
$$

## Independent frame $F_2$

选择

$$
p=e_2,\qquad q=e_3,\qquad
\varepsilon=e_1,\qquad
\dot\alpha=\dot-.
$$

则

$$
\operatorname{ev}_{F_2}(\mathcal T_p)=+1,
\qquad
\operatorname{ev}_{F_2}(\mathcal T_q)=i.
$$

因此 DA reconstruction matrix 是

$$
M_{DA}
=
\begin{pmatrix}
-1&i\\
+1&i
\end{pmatrix},
\qquad
\det M_{DA}=-2i\neq0.
$$

若两个 engine outputs 为 $S_1,S_2$，则

$$
\begin{pmatrix}c_p\\c_q\end{pmatrix}
=
M_{DA}^{-1}
\begin{pmatrix}S_1\\S_2\end{pmatrix},
$$

即

$$
\boxed{
c_p=\frac{S_2-S_1}{2}},
$$

$$
\boxed{
c_q=\frac{S_1+S_2}{2i}}.
$$

当前只给出了

$$
S_1=-\frac12+i.
$$

没有给出 $F_2$ 的 exact component-engine result $S_2$。所以 two-frame reconstruction 尚未闭合。

此外，若 engine 的 external rows 是 raw $u$-components，而非已经 normalized 的 canonical $A_c,D_c$，还必须显式计算

$$
Z_{AD}^{(a)}
=
\operatorname{ev}_{F_a}(A_c^{(1)})
\operatorname{ev}_{F_a}(D_c^{(1)}).
$$

Gate 3 静默采用了

$$
\boxed{Z_{AD}^{(1)}=1},
$$

但没有从

$$
A_c^{(1)}
=
-\frac1{4\sqrt2}D_+\bar D^2D_+u,
$$

$$
D_{c,\dot\alpha}^{(1)}
=
-\frac1{4\sqrt2}D^2\bar D_{\dot\alpha}u
$$

推导它。这是除 affine fit 之外，第一条未证明的 primitive normalization equality。

---

## 7.1 Reflected orientation

Color identity 可独立证明：

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

但它不决定 reflected spinor/Koszul sign。

对于相同 external spinor normalization，

$$
(X^{\dot\alpha}A)D_{\dot\alpha}
=
-(X_{\dot\alpha}A)D^{\dot\alpha},
$$

只决定 epsilon-index conversion；它不能替代 ordered $AD$ functional-derivative replay。

因此还需要两个独立 reflected engine outputs

$$
\widetilde S_1,\qquad \widetilde S_2
$$

以及相应 matrix

$$
M_{AD}
$$

才能确定

$$
(\widetilde c_p,\widetilde c_q).
$$

---

# 8. Target-blind status

在当前 supplied data 下，严格确定的是：

$$
\boxed{
2\int(Q_0+Q_2)=-\frac12+i,
}
$$

$$
\boxed{
N_{{\rm full},e}+C_{e,d}=\mu_\ell^2Q_e,
}
$$

$$
\boxed{
N_{{\rm full},e}^{(d)}+C_{e,d}=0,
}
$$

$$
\boxed{
C_{\rm primitive,outside\ }Q
=
-\frac{\lambda_1}{32}.
}
$$

完整 ordered vector 必须写为

$$
\boxed{
\vec C_{AA}
=
-\frac{\lambda_1}{32}
\left(
c_p,c_q,\widetilde c_p,\widetilde c_q
\right),
}
$$

其中

$$
(c_p,c_q)
=
M_{DA}^{-1}
\begin{pmatrix}S_1\\S_2\end{pmatrix},
$$

$$
(\widetilde c_p,\widetilde c_q)
=
M_{AD}^{-1}
\begin{pmatrix}\widetilde S_1\\\widetilde S_2\end{pmatrix}.
$$

当前缺少

$$
S_2,\qquad
\widetilde S_1,\qquad
\widetilde S_2,
$$

以及 external component normalization $Z_{AD}^{(a)}$ 的 row-level certificate。

因此

$$
\boxed{
\text{complete target-blind AA ordered vector remains undefined.}
}
$$

---

# 9. HT comparison

Primitive ledger 尚未在 two-frame DA map 与 independent AD replay 处闭合。因此现在比较

$$
\Delta(A^A,A^B)
$$

会把 missing frame normalization 或 reflected sign 偷渡为 target fitting。

$$
\boxed{
\text{No valid HT coefficient comparison is made at Gate 4.}
}
$$

目前能够精确定位的最早错误链是

$$
\boxed{
\text{retracted affine quotient}
\;\longrightarrow\;
\text{false one-frame } \frac12\text{ projection}
\;\longrightarrow\;
-\lambda_1/64.
}
$$

而在 primitive normalization 层面，第一条仍需验证的 equality 是

$$
\boxed{
Q_e\text{ 的 external component normalization}
=
\text{canonical }A_cD_c\text{ normalization}.
}
$$

它必须由第二 transverse frame 和独立 reflected replay 决定，不能由 HT coefficient 反向选择。
