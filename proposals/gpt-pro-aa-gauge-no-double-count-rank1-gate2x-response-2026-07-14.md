STATUS: ACCEPT_BLOCKER__SELECTED_RANK1_FIXED__FULL_EDGE_TAGGED_LONGITUDINAL_CONTACT_MAP_OPEN

## 记号

$$
D_i:=r_{i,d}^{\,2},\qquad
r_0=\ell,\qquad
r_1=\ell+q,\qquad
r_2=\ell+P,\qquad
P:=p+q,
$$

$$
r_i=
\begin{pmatrix}
a_i&b_i\\
c_i&d_i
\end{pmatrix},
\qquad
b_i=(r_i)_{+\dot-},
\qquad
\det r_i=-\bar r_i^{\,2}.
$$

定义两个 action-endpoint choices

$$
\mathbb B_0=-\bar D_{e_0},\qquad
\mathbb B_1=+\bar D_{e_1},
$$

$$
\mathbb C_1=-D_{e_1,-},\qquad
\mathbb C_2=+D_{e_2,-}.
$$

四个 endpoint rows 的顺序为

$$
(\mathbb B_0\mathbb C_1,\,
\mathbb B_0\mathbb C_2,\,
\mathbb B_1\mathbb C_1,\,
\mathbb B_1\mathbb C_2).
$$

---

# 1. Sparse rows 之外的唯一 common prefactor

在 $u=V/(\sqrt2g)$ coordinate，

$$
\langle u^A(p,1)u^B(-p,2)\rangle
=
-\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_{12}).
$$

这由原始 $V$-Hessian

$$
K_V=\frac h2\kappa\Box_E,\qquad
K_V^{-1}=2g^2\kappa^{-1}\Box_E^{-1}
$$

直接给出。

固定一个 labeled orientation，interaction Taylor factor 为

$$
\frac1{2!}
\left(
S_{3,W}S_{3,\widetilde W}
+
S_{3,\widetilde W}S_{3,W}
\right)
=
S_{3,W}S_{3,\widetilde W}.
$$

因此 rows 之外的 common factor 只有

$$
\begin{aligned}
\mathcal N_{\rm common}
&=
\frac1{2!}(2)
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3\\
&=
\left(\frac{g^2}{16\hbar^2}\right)(-\hbar^3)\\
&=
\boxed{-\frac{\hbar g^2}{16}}.
\end{aligned}
$$

完整 factor 为

$$
\boxed{
\mathcal P^{AB}{}_{DE}
=
-\frac{\hbar g^2}{16}\,
\mathbb F^{AB}{}_{DE}.
}
$$

这里没有再乘：

$$
-\frac14,\qquad 16,\qquad 2.
$$

原因是所给 sparse polynomials 已经包含

$$
\mathcal S_e,\qquad
\mathbb K,\qquad
\mathbb B_i,\qquad
\mathbb C_j,
$$

以及完整 Berezin extraction。原始 gauge-word convolution 中的 $1/p!q!r!s!$ 与 ordered differentiation 已经构成 action Hessian，不再产生一个额外 source-saturation factor。

---

# 2. 八个 rowwise full-$d$ subtractions

## 2.1 Mark $01$

输入 sparse rows：

$$
\mathcal G_{01,\mathcal S}
=
(-b_2\det r_0,\,
+b_2\det r_0,\,
+b_2\det r_0,\,
+b_2\det r_0).
$$

因为

$$
\det r_0=-\bar r_0^2,
$$

它们的 $\bar r_0^2$ coefficients 为

$$
\alpha=(+1,-1,-1,-1).
$$

每一行满足同一个 full-$d$ identity：

$$
\frac{r_{0,d}^2}{D_0D_1D_2}
-
\frac1{D_1D_2}
=
0.
$$

| row | raw word | full-$d$ parent-minus-cut | sole DRED remainder |
| --- | --- | --- | --- |
| $01.1$ | $\mathcal S_0\mathbb K\mathbb B_0\mathbb C_1\Delta_\theta$ | $+b_2\!\left[\dfrac{r_{0,d}^2}{D_0D_1D_2}-\dfrac1{D_1D_2}\right]=0$ | $+\dfrac{(r_2)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |
| $01.2$ | $\mathcal S_0\mathbb K\mathbb B_0\mathbb C_2\Delta_\theta$ | $-b_2\!\left[\dfrac{r_{0,d}^2}{D_0D_1D_2}-\dfrac1{D_1D_2}\right]=0$ | $-\dfrac{(r_2)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |
| $01.3$ | $\mathcal S_0\mathbb K\mathbb B_1\mathbb C_1\Delta_\theta$ | $-b_2\!\left[\dfrac{r_{0,d}^2}{D_0D_1D_2}-\dfrac1{D_1D_2}\right]=0$ | $-\dfrac{(r_2)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |
| $01.4$ | $\mathcal S_0\mathbb K\mathbb B_1\mathbb C_2\Delta_\theta$ | $-b_2\!\left[\dfrac{r_{0,d}^2}{D_0D_1D_2}-\dfrac1{D_1D_2}\right]=0$ | $-\dfrac{(r_2)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |

因此

$$
\boxed{
\sum_{j=1}^4
\mathcal R_{01}^{(j)}
=
-2\frac{(r_2)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}.
}
$$

---

## 2.2 Mark $02$

输入：

$$
\mathcal G_{02,\mathcal S}
=
(+b_0\det r_2,\,
-b_0\det r_2,\,
+b_0\det r_2,\,
+b_0\det r_2).
$$

其 $\bar r_2^2$ coefficients 为

$$
\beta=(-1,+1,-1,-1).
$$

每一行满足

$$
\frac{r_{2,d}^2}{D_0D_1D_2}
-
\frac1{D_0D_1}
=
0.
$$

| row | raw word | full-$d$ parent-minus-cut | sole DRED remainder |
| --- | --- | --- | --- |
| $02.1$ | $\mathbb K\mathcal S_2\mathbb B_0\mathbb C_1\Delta_\theta$ | $-b_0\!\left[\dfrac{r_{2,d}^2}{D_0D_1D_2}-\dfrac1{D_0D_1}\right]=0$ | $-\dfrac{(r_0)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |
| $02.2$ | $\mathbb K\mathcal S_2\mathbb B_0\mathbb C_2\Delta_\theta$ | $+b_0\!\left[\dfrac{r_{2,d}^2}{D_0D_1D_2}-\dfrac1{D_0D_1}\right]=0$ | $+\dfrac{(r_0)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |
| $02.3$ | $\mathbb K\mathcal S_2\mathbb B_1\mathbb C_1\Delta_\theta$ | $-b_0\!\left[\dfrac{r_{2,d}^2}{D_0D_1D_2}-\dfrac1{D_0D_1}\right]=0$ | $-\dfrac{(r_0)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |
| $02.4$ | $\mathbb K\mathcal S_2\mathbb B_1\mathbb C_2\Delta_\theta$ | $-b_0\!\left[\dfrac{r_{2,d}^2}{D_0D_1D_2}-\dfrac1{D_0D_1}\right]=0$ | $-\dfrac{(r_0)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}$ |

所以

$$
\boxed{
\sum_{j=1}^4
\mathcal R_{02}^{(j)}
=
-2\frac{(r_0)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}.
}
$$

没有第二个 $4-d$ factor。

---

# 3. Exact rank-one simplex moments

Feynman parametrization：

$$
\frac1{D_0D_1D_2}
=
2\int_{\Sigma_2}
\frac{dy\,dz}{(L^2+\Delta)^3},
$$

$$
L=\ell+yq+zP,
\qquad
\ell=L-yq-zP.
$$

外部 momenta 没有 breve components，因此

$$
\mu_\ell^2=\mu_L^2.
$$

并且

$$
2\int_{\Sigma_2}1=1,
\qquad
2\int_{\Sigma_2}y
=
2\int_{\Sigma_2}z
=
\frac13.
$$

## $r_2$ moment

$$
\begin{aligned}
r_2
&=\ell+P\\
&=L-yq-zP+P\\
&=L-yq+(1-z)P.
\end{aligned}
$$

Odd $L$ term vanishes：

$$
\int d^dL\,L_m\frac{\mu_L^2}{(L^2+\Delta)^3}=0.
$$

因此

$$
\begin{aligned}
2\int_{\Sigma_2}r_2
&=
-\left(2\int_{\Sigma_2}y\right)q
+
\left(
2\int_{\Sigma_2}1
-
2\int_{\Sigma_2}z
\right)P\\
&=
-\frac13q
+
\left(1-\frac13\right)(p+q)\\
&=
-\frac13q+\frac23p+\frac23q\\
&=
\boxed{\frac{2p+q}{3}}.
\end{aligned}
$$

## $r_0$ moment

$$
r_0=\ell=L-yq-zP.
$$

故

$$
\begin{aligned}
2\int_{\Sigma_2}r_0
&=
-\frac13q-\frac13P\\
&=
-\frac13q-\frac13(p+q)\\
&=
\boxed{-\frac{p+2q}{3}}.
\end{aligned}
$$

利用

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=
\frac1{32\pi^2},
$$

得到

$$
\boxed{
\int
\frac{(r_2)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}
=
\frac{(2p+q)_{+\dot-}}{96\pi^2},
}
$$

$$
\boxed{
\int
\frac{(r_0)_{+\dot-}\mu_\ell^2}{D_0D_1D_2}
=
-\frac{(p+2q)_{+\dot-}}{96\pi^2}.
}
$$

---

# 4. Rowwise integrated amplitudes

定义 direct ordered component kernel

$$
\mathcal O_{DA}[k]
:=
\mathbb F^{AB}{}_{DE}\,
D_{\dot-}^D(q)\,
k_{+\dot-}\,
A^E(p).
$$

这里：

- $A^E(p)=D_+W_+^E(p)$
- $k_{+\dot-}$
- $q$

又有

$$
\lambda_1=\frac{\hbar g^2}{16\pi^2}.
$$

## Mark $01$

$$
\mathcal P_{\rm common}
\frac{(2p+q)}{96\pi^2}
=
-\frac{\lambda_1}{96}(2p+q).
$$

| row | amplitude |
| --- | --- |
| $01.1$ | $-\dfrac{\lambda_1}{96}\mathcal O_{DA}[2p+q]$ |
| $01.2$ | $+\dfrac{\lambda_1}{96}\mathcal O_{DA}[2p+q]$ |
| $01.3$ | $+\dfrac{\lambda_1}{96}\mathcal O_{DA}[2p+q]$ |
| $01.4$ | $+\dfrac{\lambda_1}{96}\mathcal O_{DA}[2p+q]$ |

因此

$$
\boxed{
\Gamma_{01,\mathcal S}
=
\frac{\lambda_1}{48}\,
\mathcal O_{DA}[2p+q].
}
$$

## Mark $02$

由于 $r_0$-moment 自身带负号，

$$
\mathcal P_{\rm common}
\left[
-\frac{p+2q}{96\pi^2}
\right]
=
+\frac{\lambda_1}{96}(p+2q).
$$

乘以 $\beta=(-1,+1,-1,-1)$：

| row | amplitude |
| --- | --- |
| $02.1$ | $-\dfrac{\lambda_1}{96}\mathcal O_{DA}[p+2q]$ |
| $02.2$ | $+\dfrac{\lambda_1}{96}\mathcal O_{DA}[p+2q]$ |
| $02.3$ | $-\dfrac{\lambda_1}{96}\mathcal O_{DA}[p+2q]$ |
| $02.4$ | $-\dfrac{\lambda_1}{96}\mathcal O_{DA}[p+2q]$ |

故

$$
\boxed{
\Gamma_{02,\mathcal S}
=
-\frac{\lambda_1}{48}\,
\mathcal O_{DA}[p+2q].
}
$$

两种 source marks 属于同一 labeled direct orientation，而不是 $DA$ 与 $AD$ 两个独立 reflections。因此

$$
\begin{aligned}
\Gamma_{DA,\mathcal S}
&=
\Gamma_{01,\mathcal S}
+
\Gamma_{02,\mathcal S}\\
&=
\frac{\lambda_1}{48}
\left(
\mathcal O_{DA}[2p+q]
-
\mathcal O_{DA}[p+2q]
\right)\\
&=
\boxed{
\frac{\lambda_1}{48}
\mathbb F^{AB}{}_{DE}
D_{\dot-}^D(q)
(p-q)_{+\dot-}
A^E(p).
}
\end{aligned}
$$

即 sparse selected-square sector 给出两个 independent typed structures：

$$
\boxed{
\Gamma_{DA,\mathcal S}
=
\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\frac1{48}
D_{\dot-}^D(q)p_{+\dot-}A^E(p)
-
\frac1{48}
D_{\dot-}^D(q)q_{+\dot-}A^E(p)
\right].
}
$$

因此目前得到的不是单一

$$
D_{\dot\alpha}^D\,p_+{}^{\dot\alpha}A^E
$$

carrier。

---

# 5. Gate 2W Section 8 的 double count

Sparse evaluation 已经计算

$$
\mathcal S_e\mathbb K\mathbb B_i\mathbb C_j\Delta_\theta
\longmapsto
\mathcal G_{\mathcal S}^{(j)}.
$$

其中包含：

$$
\sqrt2
\left(-\frac1{4\sqrt2}\right)
=
-\frac14,
$$

以及完整 Grassmann differentiation 和 Berezin coefficient extraction。

因此

$$
(-1,+1,+1,+1)\longmapsto 2
$$

是 **algebraic coefficient of the final polynomial**，不是一个尚未乘入的 endpoint multiplicity。

Gate 2W 再乘

$$
\sqrt2
\left(-\frac1{4\sqrt2}\right)(16)(2)
=
-8
$$

重复使用了：

$$
\mathcal S_e,\qquad
\mathbb K,\qquad
\text{same Berezin saturation},\qquad
\text{same four endpoint sum}.
$$

所以

$$
\boxed{
w_D=-8
}
$$

不能在 sparse rows 之后重新引入。

正确关系是

$$
\boxed{
\Gamma
=
\mathcal N_{\rm common}
\times
\left(
\text{final sparse polynomial}
\right)
\times
\left(
\text{loop integral}
\right).
}
$$

---

# 6. Longitudinal/contact sector 不能由 aggregate cancellation 删除

已知

$$
\sum_j\mathcal G_{01,\mathcal L}^{(j)}
=
-2d_0W_{02}.
$$

但

$$
W_{02}=a_0b_2-b_0a_2,
$$

且

$$
a_0d_0=\det r_0+b_0c_0.
$$

因此

$$
\begin{aligned}
-2d_0W_{02}
&=
-2a_0d_0b_2
+
2b_0a_2d_0\\
&=
-2b_2(\det r_0+b_0c_0)
+
2b_0a_2d_0\\
&=
\boxed{
-2b_2\det r_0
+
2b_0(a_2d_0-b_2c_0).
}
\end{aligned}
$$

第一项明确包含同一个 $e_0$ determinant：

$$
-2b_2\det r_0
=
+2b_2\bar r_0^2.
$$

而 selected sector 为

$$
2b_2\det r_0
=
-2b_2\bar r_0^2.
$$

所以，若 longitudinal 第一项的 rowwise edge tag 确实为 $e_0$，它的 DRED remainder 将是

$$
+2(r_2)_{+\dot-}
\frac{\mu_\ell^2}{D_0D_1D_2},
$$

并会严格抵消

$$
-2(r_2)_{+\dot-}
\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

反之，若该 determinant 是由 full-$d$ contact、transported neighboring edge 或 link descendant 产生，则 subtraction 不同。

因此 aggregate statement

$$
L_{01}^{\rm contact}=+2d_0W_{02}
$$

不足以决定 anomaly remainder。

需要的最小 rowwise map 是

$$
\boxed{
\mathcal G_{01,\mathcal L}^{(j)}
=
\sum_{e=0}^{2}
c_{j,e}(p,q,r)\,\bar r_e^2
+
R_j,
}
$$

以及对应的 contact map

$$
\boxed{
\mathcal C_{01,\mathcal L}^{(j)}
=
\sum_{e=0}^{2}
c_{j,e}(p,q,r)\,
\frac{r_{e,d}^2}{D_0D_1D_2},
}
$$

with identical occurrence and identical selected edge $e$.

当前输入没有给出这些 $c_{j,e}$。即使

$$
\sum_j\mathcal G_{02,\mathcal L}^{(j)}=0,
$$

untagged zero 也不能证明不同-edge rank-one DRED moments 分别为零。

---

# 7. Reflected $AD$ sector

上述八行是一个 fixed labeled orientation 的两个 source marks。它们不能同时兼作 independently reflected $AD$ rows。

Exact reflection of the complete odd block has no additional global sign—the two odd exchanges multiply to $+1$.

但是要得到

$$
\langle A^D,D^E\rangle
$$

仍需重新输出 reflected sparse rows，并明确：

$$
p\leftrightarrow q\ \text{是否发生},
\qquad
e_0\leftrightarrow e_2\ \text{如何发生},
\qquad
D_{\dot-}\leftrightarrow D^{\dot\alpha}
\ \text{的 epsilon sign}.
$$

这些不能由 direct rows 的 scalar sum 自动给出。

---

# 8. 当前严格结果

已完全固定的 selected-$\mathcal S$ sector 为

$$
\boxed{
\Gamma_{DA,\mathcal S}^{AB}
=
\frac{\lambda_1}{48}
\mathbb F^{AB}{}_{DE}
D_{\dot-}^D(q)
(p-q)_{+\dot-}
A^E(p).
}
$$

其 direct momentum-basis coefficients 是

$$
\boxed{
\left(
c_{DA}^{(p)},c_{DA}^{(q)}
\right)_{\mathcal S}
=
\left(
\frac1{48},-\frac1{48}
\right).
}
$$

但完整 coefficient vector 尚不能从现有数据推出，第一 exact blocker 是

$$
\boxed{
\texttt{MISSING\_ROWWISE\_LONGITUDINAL\_TO\_CONTACT\_EDGE\_MAP}.
}
$$

第二 blocker 是

$$
\boxed{
D(q)\,(p-q)\,A(p)
\notin
\operatorname{Span}\{D(q)\,p\,A(p)\}
}
$$

unless a typed quotient removes the $q$-term or the source-momentum term $P=p+q$. 当前没有这样的 EOM、total-derivative 或 source-derivative quotient。

第三 blocker 是 independently reflected sparse trace。

因此 complete target-blind ordered vector 为

$$
\boxed{
(c_{DA},c_{AD})
=
(\mathrm{UNDEFINED},\mathrm{UNDEFINED}).
}
$$

这不是 normalization ambiguity：

$$
\boxed{
\mathcal N_{\rm common}
=
-\frac{\hbar g^2}{16}
}
$$

已经固定。未固定的是完整 edge-tagged contact orbit 与 rank-one operator projection。
