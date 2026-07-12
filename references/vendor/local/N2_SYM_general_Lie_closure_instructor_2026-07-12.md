## Notation / 记号

[
\begin{gathered}
\delta_r:=\delta(\varepsilon_r,\bar\varepsilon_r,\eta_r,\bar\eta_r),
\qquad
\Delta_{12}:=[\delta_1,\delta_2]
=\delta_1\delta_2-\delta_2\delta_1,\
\llbracket X,Y\rrbracket^A
:=i,c_{BC}{}^A X^B Y^C,
\qquad
\mathcal D_\mu X
:=\partial_\mu X-i\llbracket A_\mu,X\rrbracket,\
[\mathcal D_\mu,\mathcal D_\nu]X
=-i\llbracket F_{\mu\nu},X\rrbracket,\
\mu:=\llbracket\phi,\widetilde\phi\rrbracket,
\qquad
H:=\mathscr D+\mu .
\end{gathered}
]

其中 (\mathscr D) 是 (N=1) vector multiplet 的 real auxiliary field；(\mathcal D_\mu) 是 gauge-covariant derivative。所有 supersymmetry transformations 都采用 **global parameter-left order**，即 odd parameter 放在 odd dynamical field 左边。Project 对 gauge bracket、covariant derivative、(SU(2)_R) doublet 与 auxiliary triplet 的定义已锁定。

---

# 1. PR #37 当前实际状态

PR #37 现在是：

[
\boxed{
\text{open}+\text{draft}+\text{mergeable=true},
\qquad
\text{head}=39405c716a4b17b55c0a29490d551157e8551ee2 .
}
]

GitHub Actions run `29191010014` 的 `repository-policy` job 已成功。

但这里必须区分三个不同层次：

| Layer                         | 当前状态                                |
| ----------------------------- | ----------------------------------- |
| Git mergeability              | PASS：没有 merge conflict              |
| Repository consistency / CI   | PASS：文件、hash、声明 scope、tests 相互一致    |
| Mathematical proof obligation | **P1 仍开放**：`N2_GENERAL_LIE_CLOSURE` |

Independent audit 明确给出：relative metric、全部 component slots、free closure、(SU(2))-color covariant-jet closure、coefficient uniqueness 与 currents 均通过；只有 arbitrary Lie algebra 的 simultaneous closure 尚未 machine-verified。

所以：

[
\boxed{\text{green CI}\neq\text{theorem fully machine-certified}.}
]

当前 task 仍是 `SPECIFIED`，而 acceptance policy 要求没有 unresolved P0/P1 才能 merge 并进入 Git-to-Notion mirror。

---

# 2. GitHub 上 (N=2) SYM 的完整建立流程

## Stage A — Convention lock

首先固定：

[
\eta_{\mu\nu}=(-,+,+,+),\qquad
[T_A,T_B]=ic_{AB}{}^CT_C,
]

以及 invariant metric

[
c_{CA}{}^D\kappa_{DB}
+c_{CB}{}^D\kappa_{AD}=0.
]

同时固定：

[
\chi_1=\psi,\qquad
\chi_2=-\lambda,
]

[
Y_{11}=-\sqrt2F,\qquad
Y_{22}=-\sqrt2\widetilde F,\qquad
Y_{12}=Y_{21}=iH.
]

这是整个 calculation 的 type system：Lorentzian conjugation、Euclidean independence、Grassmann order、(SU(2)_R) index raising 均在此阶段锁定。

---

## Stage B — 从 (N=1) superspace 构造

采用

[
\mathbb V_{\mathcal N=2}
=\mathbb V\oplus\Phi_{\rm adj},
]

其中

[
\mathbb V=(A_\mu,\lambda,\widetilde\lambda,\mathscr D),
\qquad
\Phi=(\phi,\psi,F).
]

最初令 adjoint-chiral kinetic metric (q_{AB}) 未定：

[
S^{(2)}
=======

\int d^4x\left{
[q_{AB}\widetilde\Phi^A e^V\Phi^B]*D
+\frac14[f*{AB}W^AW^B]_F
+\text{conjugate}
\right}.
]

然后在 Abelian linearized sector 写第二个 supersymmetry：

[
\delta_2\Phi=C,\eta W,
]

[
\delta_2W_a
=A\eta_a\bar D^2\widetilde\Phi
+B(\sigma^\mu)*{a\dot b}\bar\eta^{\dot b}\partial*\mu\Phi.
]

三个独立条件为

[
CB=-2i,
]

[
f^{(R)}*{AB}B=\sqrt2q*{AB},
]

[
4f^{(R)}*{AB}A=Cq*{AB}.
]

再由 scalar normalization

[
C=-i\sqrt2
]

得到

[
\boxed{
B=\sqrt2,\qquad
A=-\frac{i}{2\sqrt2},\qquad
q_{AB}=f^{(R)}*{AB}=h\kappa*{AB}.
}
]

因此第二 supersymmetry 不只是附加 symmetry；它严格固定了 vector 与 adjoint-chiral multiplet 的 relative kinetic normalization。

---

## Stage C — Lorentzian / Euclidean component projection

Lorentzian off-shell action 被逐项投影为

[
\begin{aligned}
\mathcal L^{(2)}*{\rm off}
=h\operatorname{tr}*\kappa\Big[
&-\frac14F_{\mu\nu}F^{\mu\nu}
-\mathcal D_\mu\widetilde\phi\mathcal D^\mu\phi\
&+i\bar\lambda\bar\sigma^\mu\mathcal D_\mu\lambda
+i\widetilde\psi\bar\sigma^\mu\mathcal D_\mu\psi\
&+\widetilde FF+\frac12\mathscr D^2+\mathscr D\mu
+\text{Yukawa}
\Big].
\end{aligned}
]

利用

[
\widetilde FF+\frac12\mathscr D^2+\mathscr D\mu
===============================================

\widetilde FF+\frac12H^2-\frac12\mu^2
]

可写成

[
\boxed{
\mathcal L_{\rm aux}
====================

\frac h4\operatorname{tr}*\kappa(Y^{ij}Y*{ij})
-\frac h2\operatorname{tr}_\kappa(\mu^2).
}
]

Auxiliary equations 是

[
F=\widetilde F=H=0,\qquad
\mathscr D=-\mu.
]

Euclidean action 则独立 component multiplication 后再与 Wick map 比较，而不是直接把 Lorentzian conjugation 强加给 Euclidean fields。

---

## Stage D — Manifest 与 hidden supersymmetry

Manifest (N=1) rules 来自 ordinary (N=1) vector/chiral superfields。

Hidden supersymmetry 的核心 component rules 是

[
\begin{aligned}
\delta_2\phi&=-\sqrt2\eta\lambda,\
\delta_2\lambda
&=-\sqrt2\eta\widetilde F
+i\sqrt2\sigma^\mu\bar\eta,\mathcal D_\mu\phi,\
\delta_2\psi
&=-\sigma^{\mu\nu}\eta F_{\mu\nu}
-i\eta\mathscr D-2i\eta\mu,\
\delta_2A_\mu
&=i\eta\sigma_\mu\widetilde\psi
+i\bar\eta\bar\sigma_\mu\psi.
\end{aligned}
]

同时导出 (F,\widetilde F,\mathscr D) 的 top-slot transformations，并加入 Wess–Zumino-gauge compensator

[
\Lambda_{2,L}^{\rm comp}
=2\sqrt2,\vartheta\eta,\widetilde\phi.
]

这一步产生所有 nonlinear commutator terms。

---

## Stage E — (SU(2)_R) packaging 与旧 obstruction 修复

PR #37 已经证明旧的

[
\gamma c=-is,\qquad
\gamma c=+is
]

并不是 physical obstruction，而是混用了 parameter-left 与 field-left coefficients。

Canonical solution 是

[
\boxed{
(u_F,u_{\widetilde F},u_H,\rho_\chi,
\gamma,\beta,\mathsf A_{\rm PL},\mathsf A_{\rm FL})
===================================================

(-\sqrt2,-\sqrt2,i,-1,1,-i,-2i,+2i).
}
]

对应

[
\boxed{
\begin{aligned}
\delta\chi_{ia}
={}&-\varepsilon_{ij}
(\sigma^{\mu\nu})*a{}^b\zeta_b^jF*{\mu\nu}
+i\sqrt2(\sigma^\mu)*{a\dot b}
\bar\zeta_i^{\dot b}\mathcal D*\mu\phi\
&+Y_{ij}\zeta_a^j
-i\mu\varepsilon_{ij}\zeta_a^j.
\end{aligned}}
]

因此 finite off-shell auxiliary triplet 确实存在。

---

## Stage F — Closure target

Project 声明的 general closure law 是

[
\boxed{
\Delta_{12}A_\mu
=v^\nu F_{\nu\mu}+\mathcal D_\mu\Omega_{12},
}
]

[
\boxed{
\Delta_{12}X
=v^\mu\mathcal D_\mu X
+i\llbracket\Omega_{12},X\rrbracket,
}
]

其中

[
\begin{aligned}
v^\mu=2i\Big(
&\varepsilon_1\sigma^\mu\bar\varepsilon_2
-\varepsilon_2\sigma^\mu\bar\varepsilon_1\
&+\eta_1\sigma^\mu\bar\eta_2
-\eta_2\sigma^\mu\bar\eta_1
\Big),
\end{aligned}
]

[
\Omega_{12}
=2\sqrt2\Big[
(\varepsilon_1\eta_2-\varepsilon_2\eta_1)\widetilde\phi
+
(\bar\varepsilon_1\bar\eta_2-\bar\varepsilon_2\bar\eta_1)\phi
\Big].
]

这里 (X) 包括 scalars、fermions、所有 auxiliaries、(H) 与 (Y_{ij})。

---

# 3. P1 障碍具体在哪里

当前 verifier 分成两个互补但不重叠的 sector：

[
\mathscr S_{\rm free}:
\qquad
c_{AB}{}^C=0,\qquad
p_\mu\neq0,
]

所以它完整看到 arbitrary derivatives，但看不到 non-Abelian brackets、Jacobi 与 curvature commutators。

另一个是

[
\mathscr S_{\rm int}:
\qquad
c_{AB}{}^C=\epsilon_{AB}{}^C,
\qquad
A_\mu=\partial_\mu X=0.
]

它保留

[
\delta(\mathcal D_\mu X)
=(\delta A_\mu)\times X,
]

所以没有错误地把 covariant jet quotient 当成 supersymmetry-invariant；但背景上仍有

[
\mathcal D_\mu X=0,\qquad F_{\mu\nu}=0,
]

并且 color algebra 固定为 (\mathfrak{su}(2))。

因此它没有在同一次 calculation 中看到：

[
\boxed{
\mathcal D_\mu X\neq0,\qquad
F_{\mu\nu}\neq0,\qquad
c_{[AB}{}^Ec_{C]E}{}^D=0.
}
]

而且仅测试 (\mathfrak{su}(2)) 不足以证明 arbitrary Lie algebra，因为

[
\epsilon_{ABE}\epsilon_{CDE}
=\delta_{AC}\delta_{BD}-\delta_{AD}\delta_{BC}
]

是 (\mathfrak{su}(2)) 的额外 low-dimensional identity；一个 residual 可能因为该 identity 消失，却不由 Jacobi 普遍消失。

所以这个 P1 的真正含义是：

[
\boxed{
\text{缺少 universal symbolic Lie-algebra certificate，}
\quad
\text{不是发现了 closure failure。}
}
]

---

# 4. 直接理论推导：先固定 (v^\mu) 与 (\Omega_{12})

## 4.1 Scalar closure

使用

[
\delta\phi=-\sqrt2(\varepsilon\psi+\eta\lambda),
]

[
\begin{aligned}
\delta\psi={}&
-\sqrt2\varepsilon F
+i\sqrt2\sigma^\mu\bar\varepsilon\mathcal D_\mu\phi
-\sigma^{\mu\nu}\eta F_{\mu\nu}
-i\eta\mathscr D-2i\eta\mu,\
\delta\lambda={}&
\sigma^{\mu\nu}\varepsilon F_{\mu\nu}
-i\varepsilon\mathscr D
-\sqrt2\eta\widetilde F
+i\sqrt2\sigma^\mu\bar\eta\mathcal D_\mu\phi .
\end{aligned}
]

逐项展开：

[
\begin{aligned}
\Delta_{12}\phi
={}&-\sqrt2\Big[
\varepsilon_2\delta_1\psi+\eta_2\delta_1\lambda
-\varepsilon_1\delta_2\psi-\eta_1\delta_2\lambda
\Big][1mm]
={}&
2(\varepsilon_2\varepsilon_1-\varepsilon_1\varepsilon_2)F\
&+2(\eta_2\eta_1-\eta_1\eta_2)\widetilde F\
&-2i\Big[
\varepsilon_2\sigma^\mu\bar\varepsilon_1
-\varepsilon_1\sigma^\mu\bar\varepsilon_2
+\eta_2\sigma^\mu\bar\eta_1
-\eta_1\sigma^\mu\bar\eta_2
\Big]\mathcal D_\mu\phi\
&+\sqrt2\Big[
\varepsilon_2\sigma^{\mu\nu}\eta_1
-\eta_2\sigma^{\mu\nu}\varepsilon_1
-\varepsilon_1\sigma^{\mu\nu}\eta_2
+\eta_1\sigma^{\mu\nu}\varepsilon_2
\Big]F_{\mu\nu}\
&+i\sqrt2\Big[
\varepsilon_2\eta_1+\eta_2\varepsilon_1
-\varepsilon_1\eta_2-\eta_1\varepsilon_2
\Big]\mathscr D\
&+2i\sqrt2
(\varepsilon_2\eta_1-\varepsilon_1\eta_2)\mu .
\end{aligned}
]

Grassmann-odd Weyl spinors 满足

[
\xi\chi=\chi\xi,
\qquad
\xi\sigma^{\mu\nu}\chi
=-\chi\sigma^{\mu\nu}\xi.
]

于是

[
\varepsilon_2\varepsilon_1-\varepsilon_1\varepsilon_2=0,
]

[
\eta_2\eta_1-\eta_1\eta_2=0,
]

[
\begin{aligned}
&\varepsilon_2\sigma^{\mu\nu}\eta_1
-\eta_2\sigma^{\mu\nu}\varepsilon_1
-\varepsilon_1\sigma^{\mu\nu}\eta_2
+\eta_1\sigma^{\mu\nu}\varepsilon_2\
&=
\varepsilon_2\sigma^{\mu\nu}\eta_1
+\varepsilon_1\sigma^{\mu\nu}\eta_2
-\varepsilon_1\sigma^{\mu\nu}\eta_2
-\varepsilon_2\sigma^{\mu\nu}\eta_1
=0,
\end{aligned}
]

[
\begin{aligned}
&\varepsilon_2\eta_1+\eta_2\varepsilon_1
-\varepsilon_1\eta_2-\eta_1\varepsilon_2\
&=
\varepsilon_2\eta_1+\varepsilon_1\eta_2
-\varepsilon_1\eta_2-\varepsilon_2\eta_1
=0.
\end{aligned}
]

因此

[
\Delta_{12}\phi
===============

v^\mu\mathcal D_\mu\phi
+2i\sqrt2
(\varepsilon_2\eta_1-\varepsilon_1\eta_2)\mu.
]

令

[
K:=\varepsilon_1\eta_2-\varepsilon_2\eta_1.
]

由于

[
\mu=\llbracket\phi,\widetilde\phi\rrbracket,
]

有

[
\begin{aligned}
i\llbracket 2\sqrt2K\widetilde\phi,\phi\rrbracket
&=2i\sqrt2K
\llbracket\widetilde\phi,\phi\rrbracket\
&=-2i\sqrt2K
\llbracket\phi,\widetilde\phi\rrbracket\
&=2i\sqrt2
(\varepsilon_2\eta_1-\varepsilon_1\eta_2)\mu.
\end{aligned}
]

所以

[
\boxed{
\Delta_{12}\phi
=v^\mu\mathcal D_\mu\phi
+i\llbracket\Omega_{12},\phi\rrbracket.
}
]

---

## 4.2 Gauge field 的 mixed (\varepsilon\eta) sector

取 unbarred parameters：

[
\delta A_\mu
=-i\varepsilon\sigma_\mu\bar\lambda
+i\eta\sigma_\mu\bar\psi,
]

[
\delta_\eta\bar\lambda_{\dot a}
=-i\sqrt2\eta^b
(\sigma^\nu)*{b\dot a}\mathcal D*\nu\widetilde\phi,
]

[
\delta_\varepsilon\bar\psi_{\dot a}
=-i\sqrt2\varepsilon^b
(\sigma^\nu)*{b\dot a}\mathcal D*\nu\widetilde\phi.
]

定义

[
S_{\mu}{}^{\nu}{}*{ab}
:=
(\sigma*\mu)_{a\dot a}
(\sigma^\nu)_b{}^{\dot a}.
]

Locked sigma matrices 给出

[
S_{\mu}{}^{\nu}{}*{ab}
-S*{\mu}{}^{\nu}{}_{ba}
=======================

2\epsilon_{ab}\delta_\mu{}^\nu.
]

于是

[
\begin{aligned}
\left.\Delta_{12}A_\mu\right|*{\varepsilon\eta}
={}&
\sqrt2
(\varepsilon_1^a\eta_2^b-\varepsilon_2^a\eta_1^b)
\left(
S*{\mu}{}^\nu{}*{ab}
-S*{\mu}{}^\nu{}*{ba}
\right)
\mathcal D*\nu\widetilde\phi\
={}&
2\sqrt2
(\varepsilon_1\eta_2-\varepsilon_2\eta_1)
\mathcal D_\mu\widetilde\phi\
={}&
\mathcal D_\mu
\left[
2\sqrt2
(\varepsilon_1\eta_2-\varepsilon_2\eta_1)
\widetilde\phi
\right].
\end{aligned}
]

Dotted sector 同理：

[
\left.\Delta_{12}A_\mu\right|_{\bar\varepsilon\bar\eta}
=======================================================

\mathcal D_\mu
\left[
2\sqrt2
(\bar\varepsilon_1\bar\eta_2-\bar\varepsilon_2\bar\eta_1)
\phi
\right].
]

而 (\varepsilon\bar\varepsilon) sector 是 manifest (N=1) closure，(\eta\bar\eta) sector 是其 (SU(2)_R) image：

[
\left.\Delta_{12}A_\mu\right|*{\varepsilon\bar\varepsilon+
\eta\bar\eta}
=v^\nu F*{\nu\mu}.
]

Manifest (N=1) closure 已经 off-shell 使用 Bianchi identity 严格证明。

因此

[
\boxed{
\Delta_{12}A_\mu
=v^\nu F_{\nu\mu}
+\mathcal D_\mu\Omega_{12}.
}
]

---

# 5. Missing Check I：同时非零的 (\mathcal D_\mu X)

任意 even variation (\delta) 都满足

[
\boxed{
\delta(\mathcal D_\mu X)
========================

\mathcal D_\mu(\delta X)
-i\llbracket\delta A_\mu,X\rrbracket .
}
]

现在假定 fundamental field 已满足

[
\Delta X
=v^\nu\mathcal D_\nu X
+i\llbracket\Omega,X\rrbracket,
]

[
\Delta A_\mu
=v^\nu F_{\nu\mu}
+\mathcal D_\mu\Omega.
]

则

[
\begin{aligned}
\Delta(\mathcal D_\mu X)
={}&
\mathcal D_\mu(\Delta X)
-i\llbracket\Delta A_\mu,X\rrbracket\
={}&
\mathcal D_\mu
\left(
v^\nu\mathcal D_\nu X
+i\llbracket\Omega,X\rrbracket
\right)\
&-i\llbracket
v^\nu F_{\nu\mu}
+\mathcal D_\mu\Omega,
X
\rrbracket\
={}&
v^\nu\mathcal D_\mu\mathcal D_\nu X
+i\llbracket\mathcal D_\mu\Omega,X\rrbracket
+i\llbracket\Omega,\mathcal D_\mu X\rrbracket\
&-iv^\nu\llbracket F_{\nu\mu},X\rrbracket
-i\llbracket\mathcal D_\mu\Omega,X\rrbracket\
={}&
v^\nu\mathcal D_\mu\mathcal D_\nu X
+i\llbracket\Omega,\mathcal D_\mu X\rrbracket
+iv^\nu\llbracket F_{\mu\nu},X\rrbracket.
\end{aligned}
]

再使用

[
\mathcal D_\mu\mathcal D_\nu X
==============================

\mathcal D_\nu\mathcal D_\mu X
-i\llbracket F_{\mu\nu},X\rrbracket,
]

得到

[
\begin{aligned}
\Delta(\mathcal D_\mu X)
={}&
v^\nu\mathcal D_\nu\mathcal D_\mu X
-iv^\nu\llbracket F_{\mu\nu},X\rrbracket\
&+i\llbracket\Omega,\mathcal D_\mu X\rrbracket
+iv^\nu\llbracket F_{\mu\nu},X\rrbracket\
={}&
v^\nu\mathcal D_\nu(\mathcal D_\mu X)
+i\llbracket\Omega,\mathcal D_\mu X\rrbracket.
\end{aligned}
]

所以

[
\boxed{
\Delta(\mathcal D_\mu X)
========================

v^\nu\mathcal D_\nu(\mathcal D_\mu X)
+i\llbracket\Omega,\mathcal D_\mu X\rrbracket.
}
]

这里两个 curvature terms 是严格相消：

[
-iv^\nu\llbracket F_{\mu\nu},X\rrbracket
+
iv^\nu\llbracket F_{\mu\nu},X\rrbracket
=0.
]

这正是当前两个 separated gates 没有同时看到的 mixed term。

---

# 6. Missing Check II：非零 (F_{\mu\nu})

任意 variation 满足

[
\delta F_{\mu\nu}
=================

\mathcal D_\mu\delta A_\nu
-\mathcal D_\nu\delta A_\mu.
]

所以

[
\begin{aligned}
\Delta F_{\mu\nu}
={}&
\mathcal D_\mu(\Delta A_\nu)
-\mathcal D_\nu(\Delta A_\mu)\
={}&
\mathcal D_\mu
\left(v^\rho F_{\rho\nu}+\mathcal D_\nu\Omega\right)
-\mathcal D_\nu
\left(v^\rho F_{\rho\mu}+\mathcal D_\mu\Omega\right)\
={}&
v^\rho
\left(
\mathcal D_\mu F_{\rho\nu}
-\mathcal D_\nu F_{\rho\mu}
\right)
+
[\mathcal D_\mu,\mathcal D_\nu]\Omega.
\end{aligned}
]

Bianchi identity

[
\mathcal D_\mu F_{\rho\nu}
-\mathcal D_\nu F_{\rho\mu}
===========================

\mathcal D_\rho F_{\mu\nu}
]

给出

[
v^\rho
\left(
\mathcal D_\mu F_{\rho\nu}
-\mathcal D_\nu F_{\rho\mu}
\right)
=======

v^\rho\mathcal D_\rho F_{\mu\nu}.
]

同时

[
[\mathcal D_\mu,\mathcal D_\nu]\Omega
=-i\llbracket F_{\mu\nu},\Omega\rrbracket
=+i\llbracket\Omega,F_{\mu\nu}\rrbracket.
]

因此

[
\boxed{
\Delta F_{\mu\nu}
=================

v^\rho\mathcal D_\rho F_{\mu\nu}
+i\llbracket\Omega,F_{\mu\nu}\rrbracket.
}
]

这里没有设

[
F_{\mu\nu}=0,
]

也没有使用 equations of motion。唯一使用的是 exact non-Abelian Bianchi identity。

---

# 7. Missing Check III：arbitrary Lie algebra 的 Jacobi reductions

因为 (\Delta) 是包含 Grassmann-odd parameter 的 **even transformation**，

[
\Delta\llbracket U,V\rrbracket
==============================

\llbracket\Delta U,V\rrbracket
+
\llbracket U,\Delta V\rrbracket.
]

若

[
\Delta U=v^\mu\mathcal D_\mu U
+i\llbracket\Omega,U\rrbracket,
]

[
\Delta V=v^\mu\mathcal D_\mu V
+i\llbracket\Omega,V\rrbracket,
]

则

[
\begin{aligned}
\Delta\llbracket U,V\rrbracket
={}&
v^\mu\llbracket\mathcal D_\mu U,V\rrbracket
+v^\mu\llbracket U,\mathcal D_\mu V\rrbracket\
&+i\llbracket\llbracket\Omega,U\rrbracket,V\rrbracket
+i\llbracket U,\llbracket\Omega,V\rrbracket\rrbracket\
={}&
v^\mu\mathcal D_\mu\llbracket U,V\rrbracket\
&+i\left[
\llbracket\llbracket\Omega,U\rrbracket,V\rrbracket
+\llbracket U,\llbracket\Omega,V\rrbracket\rrbracket
\right].
\end{aligned}
]

因为 (\Omega) 是 bosonic，graded Jacobi 简化为

[
\llbracket\Omega,\llbracket U,V\rrbracket\rrbracket
===================================================

\llbracket\llbracket\Omega,U\rrbracket,V\rrbracket
+
\llbracket U,\llbracket\Omega,V\rrbracket\rrbracket.
]

所以

[
\boxed{
\Delta\llbracket U,V\rrbracket
==============================

v^\mu\mathcal D_\mu\llbracket U,V\rrbracket
+i\llbracket\Omega,\llbracket U,V\rrbracket\rrbracket.
}
]

## Structure-constant level

上面的 Jacobi reduction 等价于

[
\begin{aligned}
0={}&
\Big(
\llbracket\Omega,\llbracket U,V\rrbracket\rrbracket
-\llbracket\llbracket\Omega,U\rrbracket,V\rrbracket
-\llbracket U,\llbracket\Omega,V\rrbracket\rrbracket
\Big)^A\
={}&-
\Big(
c_{DE}{}^A c_{BC}{}^E
-c_{EC}{}^A c_{DB}{}^E
-c_{BE}{}^A c_{DC}{}^E
\Big)
\Omega^DU^BV^C.
\end{aligned}
]

因此所需条件严格是

[
\boxed{
c_{DE}{}^A c_{BC}{}^E
-c_{EC}{}^A c_{DB}{}^E
-c_{BE}{}^A c_{DC}{}^E
=0,
}
]

即 ordinary Lie-algebra Jacobi identity；没有使用

[
c_{AB}{}^C=\epsilon_{AB}{}^C
]

或任何 (\mathfrak{su}(2))-specific tensor identity。

Project 在 current-divergence calculation 中已经采用相同的 general graded Jacobi identity；只是 closure verifier 尚未把它编码为 symbolic normal form。

---

## 对 moment map 的直接检查

由于

[
\mu=\llbracket\phi,\widetilde\phi\rrbracket,
]

有

[
\begin{aligned}
\Delta\mu
={}&
\llbracket\Delta\phi,\widetilde\phi\rrbracket
+\llbracket\phi,\Delta\widetilde\phi\rrbracket\
={}&
\llbracket
v^\mu\mathcal D_\mu\phi
+i\llbracket\Omega,\phi\rrbracket,
\widetilde\phi
\rrbracket\
&+
\llbracket
\phi,
v^\mu\mathcal D_\mu\widetilde\phi
+i\llbracket\Omega,\widetilde\phi\rrbracket
\rrbracket\
={}&
v^\mu\left[
\llbracket\mathcal D_\mu\phi,\widetilde\phi\rrbracket
+\llbracket\phi,\mathcal D_\mu\widetilde\phi\rrbracket
\right]\
&+i\left[
\llbracket\llbracket\Omega,\phi\rrbracket,\widetilde\phi\rrbracket
+\llbracket\phi,\llbracket\Omega,\widetilde\phi\rrbracket\rrbracket
\right]\
={}&
v^\mu\mathcal D_\mu\mu
+i\llbracket\Omega,\mu\rrbracket.
\end{aligned}
]

所以

[
\boxed{
\Delta\mu
=v^\mu\mathcal D_\mu\mu
+i\llbracket\Omega,\mu\rrbracket.
}
]

进而

[
H=\mathscr D+\mu
]

满足

[
\boxed{
\Delta H
=v^\mu\mathcal D_\mu H
+i\llbracket\Omega,H\rrbracket,
}
]

而 (Y_{ij}) 是 (F,\widetilde F,H) 的 linear invertible combination，因此同样 closure。

---

# 8. 为什么这三个计算已经覆盖全部 component fields

Displayed transformations 的 algebraic grammar 只有：

[
\delta A,\delta\phi
\in{\chi,\bar\chi},
]

[
\delta\chi
\in
{F_{\mu\nu},\mathcal D_\mu\phi,Y,\mu},
]

[
\delta Y
\in
{\mathcal D_\mu\chi,
\llbracket\chi,\widetilde\phi\rrbracket,
\llbracket\bar\chi,\phi\rrbracket}.
]

也就是说，计算第二次 variation 时，只可能新产生三类 operation：

[
\boxed{
\mathcal D_\mu X,\qquad
F_{\mu\nu},\qquad
\llbracket X,Y\rrbracket.
}
]

不存在第四种独立 color/jet structure。Component laws 的这一结构可直接从 (\delta\chi_i) 与 (\delta Y_{ij}) 看出。

定义 closure residual

[
\mathscr R_{A_\mu}
:=
\Delta A_\mu-v^\nu F_{\nu\mu}-\mathcal D_\mu\Omega,
]

[
\mathscr R_X
:=
\Delta X-v^\nu\mathcal D_\nu X
-i\llbracket\Omega,X\rrbracket.
]

上面的三个直接计算等价于 exact recursion：

[
\boxed{
\mathscr R_{\mathcal D_\mu X}
=============================

\mathcal D_\mu\mathscr R_X
-i\llbracket\mathscr R_{A_\mu},X\rrbracket,
}
]

[
\boxed{
\mathscr R_{F_{\mu\nu}}
=======================

\mathcal D_\mu\mathscr R_{A_\nu}
-\mathcal D_\nu\mathscr R_{A_\mu},
}
]

[
\boxed{
\mathscr R_{\llbracket X,Y\rrbracket}
=====================================

\llbracket\mathscr R_X,Y\rrbracket
+\llbracket X,\mathscr R_Y\rrbracket.
}
]

因此一旦 primitive component coefficients 已锁定并且

[
\mathscr R_{A_\mu}
=\mathscr R_{\phi}
=\mathscr R_{\widetilde\phi}
=\mathscr R_{\chi_i}
=\mathscr R_{\bar\chi^i}
=\mathscr R_{Y_{ij}}
=0,
]

所有 covariant jets、field strengths、moment maps 和 nested commutators 自动满足

[
\mathscr R=0.
]

这正是从现有 separated gates 到 arbitrary-Lie simultaneous gate 的 universal lift。

---

# 9. 理论结论与 repository 结论

## Mathematical conclusion

对任意满足 graded antisymmetry 与 Jacobi identity 的 Lie algebra (\mathfrak g)，当前 PR #37 中 coefficient-locked (N=2) transformations 满足

[
\boxed{
\begin{aligned}
\Delta_{12}A_\mu
&=v^\nu F_{\nu\mu}
+\mathcal D_\mu\Omega_{12},\
\Delta_{12}X
&=v^\mu\mathcal D_\mu X
+i\llbracket\Omega_{12},X\rrbracket,
\end{aligned}}
]

且没有使用 equations of motion：

[
\boxed{\text{off-shell closure holds.}}
]

Closure 本身只需要 Jacobi；action invariance 另外需要 (\kappa_{AB}) 的 ad-invariance。

同一证明适用于 Euclidean signature，因为

[
\delta(\mathcal D X),\quad
[\mathcal D,\mathcal D]X,\quad
\mathcal D_{[\mu}F_{\nu\rho]}=0,\quad
\text{Jacobi}
]

全部是 signature-independent identities；只需把 (v_L^\mu) 换成 (v_E^m)。当前 Euclidean free all-field gate 已通过。

## Repository conclusion

[
\boxed{
\texttt{N2_GENERAL_LIE_CLOSURE}
\text{ 是 machine-proof gap，不是 theory obstruction。}
}
]

PR 仍应保持 draft，直到把上述证明编码成 exact symbolic gate。需要的 verifier 不应再取

[
c_{AB}{}^C=\epsilon_{AB}{}^C,
]

而应使用：

1. graded free-Lie bracket trees；
2. antisymmetry + Jacobi canonicalizer，例如 Hall/Lyndon basis；
3. independent nonzero jets
   [
   X,\ \mathcal D_\mu X,\
   \mathcal D_{(\mu}\mathcal D_{\nu)}X,
   F_{\mu\nu},
   \mathcal D_\rho F_{\mu\nu};
   ]
4. rewrite rules
   [
   \mathcal D_\mu\mathcal D_\nu X
   ==============================

   \mathcal D_{(\mu}\mathcal D_{\nu)}X
   -\frac i2\llbracket F_{\mu\nu},X\rrbracket,
   ]
   [
   \mathcal D_\mu F_{\rho\nu}
   -\mathcal D_\nu F_{\rho\mu}
   ===========================

   \mathcal D_\rho F_{\mu\nu};
   ]
5. 对 (A_\mu,\phi,\widetilde\phi,\chi_i,\bar\chi^i,Y_{ij}) 及 derived fields 全部输出 exact zero residual。

该 gate 通过后，audit 才应从

[
\texttt{BLOCKED_GENERAL_LIE_CLOSURE_VERIFICATION}
]

改为

[
\boxed{\texttt{PASS_EXACT_GENERAL_LIE_CLOSURE}}.
]
