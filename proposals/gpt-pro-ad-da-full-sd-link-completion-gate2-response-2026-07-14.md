## 记号 / Notation

令

$$
A_1:=A_c^{(1)},\qquad D_{1,\dot a}:=D_{c,\dot a}^{(1)},
$$

$$
\mathscr W_{\omega,e}^{L}
:=
\text{固定 orientation }\omega\text{、固定 occurrence }e
\text{ 后，未标记端点组成的 ordered }D\text{-word}.
$$

$$
T_1[u]
:=
\int_0^1ds\;
e^{(1-s)w\cdot\partial}\,
\mathbb M_1[u]\,
e^{s w\cdot\partial},
$$

$$
\bigl(\mathbb M_1[u]\bigr)^B{}_C
:=
w^m c_{LC}{}^B\,\mathcal A_m^{L,(1)}[u].
$$

这里 $\mathcal A_m^{(1)}[u]$ 是 adjoint covariant translation 中对 $u$ 线性的 gauge connection。

---

# 1. 由 supplied data 已经闭合的 same-edge ledger

Marked split 为

$$
D_-D_+\bar D^2D_+
=
-8(\det r_e)D_+
-\frac12D_+\bar D^2D^2.
$$

因此每个 $(\omega,e)$：

$$
\boxed{
K_{\omega,e}
=
-8(\det r_e)\,
\mathscr W_{\omega,e}^{K}},
$$

$$
\boxed{
L_{\omega,e}^{\rm source}
=
-\frac12\mathscr W_{\omega,e}^{L}},
$$

$$
\boxed{
L_{\omega,e}^{\rm gf}
=
+\frac12\mathscr W_{\omega,e}^{L}},
$$

所以

$$
\boxed{
L_{\omega,e}^{\rm source}
+
L_{\omega,e}^{\rm gf}
=0}.
$$

在 reduced numerator notation 中，

$$
K_{\omega,e}^{(4)}
=
\frac{\chi R_{\omega,e}\bar r_e^2}
{D_0D_1D_2},
\qquad
C_{\omega,e}^{SD}
=
-\frac{R_{\omega,e}}
{\prod_{j\neq e}D_j}.
$$

Full-$d$ Schwinger–Dyson identity 给出

$$
\begin{aligned}
K_{\omega,e}^{(d)}+C_{\omega,e}^{SD}
&=
\frac{\chi R_{\omega,e}r_{e,d}^2}
{D_0D_1D_2}
-\frac{R_{\omega,e}}
{\prod_{j\neq e}D_j}\\
&=
\frac{(\chi-1)R_{\omega,e}}
{\prod_{j\neq e}D_j}.
\end{aligned}
$$

对 generic nonzero routed word，

$$
\boxed{\chi=1}.
$$

因此该 **two-member suborbit** 严格满足

$$
\boxed{
K_{\omega,e}^{(d)}
+
C_{\omega,e}^{SD}=0},
$$

以及

$$
\begin{aligned}
K_{\omega,e}^{(4)}
+
C_{\omega,e}^{SD}
&=
\frac{R_{\omega,e}\bar r_e^2}
{D_0D_1D_2}
-\frac{R_{\omega,e}}
{\prod_{j\neq e}D_j}\\
&=
\boxed{
\frac{\mu_\ell^2R_{\omega,e}}
{D_0D_1D_2}}.
\end{aligned}
$$

这里没有 $4-d$。

---

## O05/O06 partial contacts

在 direct routing：

$$
\begin{array}{c|ccc}
&e_0&e_1&e_2\\ \hline
O05^{AD}_e
&7i\,q_+&0&2i\,q_+\\[1mm]
O06^{DA}_e
&-\dfrac i2q_+
&i(p+q)_+
&i(p+q)_+
\end{array}
$$

Crossed routing 仅交换 ordered pair：

$$
\boxed{
O05^{AD,\rm crossed}_e
=
O06^{DA,\rm direct}_e},
$$

$$
\boxed{
O06^{DA,\rm crossed}_e
=
O05^{AD,\rm direct}_e}.
$$

这些是 partial two-denominator members，不能和已经形成的

$$
\frac{\mu_\ell^2R_{\omega,e}}{D_0D_1D_2}
$$

再次相加。

---

# 2. 第一条缺失的 named-link functional derivative

Available completion record 只给出

$$
\texttt{ONE\_LINK\_BULK}:
\qquad
L_{1,A}T_1L_{1,B},
$$

以及

$$
\texttt{TWO\_LINK\_ORDERED}:
\qquad
L_{1,A}T_2L_{1,B},
$$

作为 operator words；它没有给出 occurrence-resolved amplitude coefficient。Collapsed kernels 与 $C_{SD}$ amplitude kernels 在该记录中仍被明确标为 blocked。

对于 ordered $AD$ source，第一条尚未提供的 derivative 是 one-link bulk 的三 occurrence derivative：

$$
\boxed{
\begin{aligned}
\mathcal V^{AD,[1]}_{\dot a;\,IJK}
(z_1,z_2,z_3)
:={}&
\left.
\frac{\vec\delta}{\delta u_A^I(z_1)}
\frac{\vec\delta}{\delta u_{\rm link}^J(z_2)}
\frac{\vec\delta}{\delta u_D^K(z_3)}
\right.\\
&\left.
\qquad\times
\Big[
(\nabla_-A_1)^A(z)\,
\big(T_1[u]D_{1,\dot a}\big)^B(z)
\Big]
\right|_{u=0}.
\end{aligned}}
$$

显式地，

$$
\begin{aligned}
\big(T_1[u]D_{1,\dot a}\big)^B(z)
={}&
\int_0^1ds\,
\Big[
e^{(1-s)w\cdot\partial}
\mathbb M_1[u]
e^{sw\cdot\partial}
D_{1,\dot a}
\Big]^B(z),
\end{aligned}
$$

$$
\bigl(\mathbb M_1[u]\bigr)^B{}_C
=
w^m c_{LC}{}^B\,
\mathcal A_m^{L,(1)}[u].
$$

要完成 same-edge ledger，必须给出该 derivative 对每个 labeled assignment

$$
(u_A,u_{\rm link},u_D)
\longrightarrow
(r_i,r_j,r_k)
$$

的：

$$
\boxed{
\text{rational coefficient},
\qquad
\text{color order},
\qquad
\text{routed spinor word},
\qquad
\text{marked edge }e.
}
$$

当前 supplied data 没有这些 rows。

Phase telescoping

$$
iw\cdot(r_0-r_1)
\int_0^1ds\,
e^{iw\cdot[sr_0+(1-s)r_1]}
=
e^{iw\cdot r_0}-e^{iw\cdot r_1}
$$

只能决定 boundary signs；它不能证明 link residue 等于 O05/O06 residue。Available audit 也明确把 “same residue” 留作独立 amplitude obligation。

对应的 repository blocker 正是：必须独立计算每个 nonlinear、collapsed、one-link、two-link 与 endpoint graph 的 edge-tagged residue；phase telescoping 本身不足以证明相消。

---

# 3. 强制停止点

由于

$$
\mathcal V^{AD,[1]}_{\dot a;\,IJK}
$$

未给出，不能合法确定：

$$
O05_e+O06_e+\sum_{\nu}
L^{\rm named}_{\nu,e},
$$

因此不能判定 O05/O06 是

$$
0
$$

还是仅留下

$$
q_+\times(\text{divergence/EOM carrier}).
$$

也不能把条件算术

$$
4\left(\frac12\right)(-8)R_1
=
\left(-\frac i3,-\frac i6\right),
$$

$$
4\left(\frac12\right)(-8)R_2
=
\left(-\frac{2i}{3},-\frac i3\right)
$$

提升为 full-SD physical coefficients：这些乘法本身成立，但尚未证明其 $q_+$ entries 已由完整 same-edge orbit 消去。

故此 Gate 的严格状态是

$$
\boxed{
\texttt{BLOCKED\_AT\_ONE\_LINK\_OCCURRENCE\_DERIVATIVE}.
}
$$

在该 derivative 及其 $DA$、crossed、two-link、endpoint continuations 被逐 row 给出之前，不能 target-blindly confirm 或 refute 所提

$$
\left(\frac13,\frac23\right),
\qquad
\left(\frac23,\frac13\right)
$$

ordered physical vectors，也不进行 holomorphic-twist comparison。
