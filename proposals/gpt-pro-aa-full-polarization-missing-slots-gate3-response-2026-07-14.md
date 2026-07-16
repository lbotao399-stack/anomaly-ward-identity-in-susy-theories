## 记号 / Notation

$$
\mathsf r:=-i\sigma_E\!\cdot r
=
\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
\bar r^{\,2}:=-\det\mathsf r,
\qquad
D_e:=r_{e,d}^{\,2}.
$$

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

最终 ordered basis 为

$$
\mathcal B_{AA}
=
(\mathcal T_p,\mathcal T_q,
\widetilde{\mathcal T}_p,\widetilde{\mathcal T}_q).
$$

Color tensor：

$$
\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E},
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

以下 $N_{\mathrm{full},e},R_e,L_e$ 采用题中 exact component-engine normalization：relative raw-action coefficients、corrected source coefficient、Berezin saturation 与 endpoint transport 已经包含在 $N,R,L$ 中；共同的两个 exponent vertices、三条 propagators、color tensor 与 loop measure 留在外面。

---

# 1. Full polarized cubic action

由 (5A.52)，在 Euclidean parity-even sector

$$
\eta_E=-1,
\qquad
f_{AB}=\widetilde f_{AB}=g^{-2}\kappa_{AB},
\qquad
V=\sqrt2g\,u,
$$

令

$$
a_g:=\frac{\sqrt2g}{256}.
$$

原始 chiral cubic words 为

$$
\begin{array}{c|c|c}
(p,q,r,s)&\text{word}&\text{coefficient}\\ \hline
(1,0,0,0)&
[\bar D^2(uD^au)]^A[\bar D^2D_au]^B
&+a_g\kappa_{AB}\\[1mm]
(0,1,0,0)&
[\bar D^2(D^au\,u)]^A[\bar D^2D_au]^B
&-a_g\kappa_{AB}\\[1mm]
(0,0,1,0)&
[\bar D^2D^au]^A[\bar D^2(uD_au)]^B
&+a_g\kappa_{AB}\\[1mm]
(0,0,0,1)&
[\bar D^2D^au]^A[\bar D^2(D_au\,u)]^B
&-a_g\kappa_{AB}.
\end{array}
$$

Antichiral words 为

$$
\begin{array}{c|c|c}
(p,q,r,s)&\text{word}&\text{coefficient}\\ \hline
(1,0,0,0)&
[D^2(u\bar D_{\dot a}u)]^A[D^2\bar D^{\dot a}u]^B
&-a_g\kappa_{AB}\\[1mm]
(0,1,0,0)&
[D^2(\bar D_{\dot a}u\,u)]^A[D^2\bar D^{\dot a}u]^B
&+a_g\kappa_{AB}\\[1mm]
(0,0,1,0)&
[D^2\bar D_{\dot a}u]^A[D^2(u\bar D^{\dot a}u)]^B
&-a_g\kappa_{AB}\\[1mm]
(0,0,0,1)&
[D^2\bar D_{\dot a}u]^A[D^2(\bar D^{\dot a}u\,u)]^B
&+a_g\kappa_{AB}.
\end{array}
$$

这些 coefficients 直接来自 authority convolution。

经过 chiral/full-superspace conversion，得到

$$
S_+^{(3)}
=
-\frac{ig}{4}
c_{UCE}
\int d^8z\,
W^{Ea}(D_au^U)u^C,
$$

$$
S_-^{(3)}
=
+\frac{ig}{4}
c_{UCD}
\int d^8z\,
\widetilde W_{\dot a}^{D}
(\bar D^{\dot a}u^U)u^C.
$$

Field strengths 的 projector normalization 为

$$
W_a=-\frac1{4\sqrt2}\bar D^2D_au,
\qquad
\widetilde W_{\dot a}
=-\frac1{4\sqrt2}D^2\bar D_{\dot a}u,
$$

与 locked superfield definitions 一致。

---

## 1.1 Chiral three-position polarization

对三个独立 labeled fields $u^U,u^C,u^E$，完整 polarization 为

$$
\begin{aligned}
\operatorname{Pol}S_+^{(3)}
=
-\frac{ig}{4}c_{UCE}\int d^8z\,
\Big\{&
W^E(Du^U)u^C
-W^C(Du^U)u^E\\
&-W^E(Du^C)u^U
+W^U(Du^C)u^E\\
&+W^C(Du^E)u^U
-W^U(Du^E)u^C
\Big\}.
\end{aligned}
$$

按 external $u^E$ 所在位置分成：

### Family $F_+$：linear field-strength slot

$$
\boxed{
\mathscr P_{F,+}
=
W^E\Big[(Du^U)u^C-(Du^C)u^U\Big].
}
$$

### Family $\partial_+$：differentiated commutator slot

$$
\boxed{
\mathscr P_{\partial,+}
=
W^C(Du^E)u^U-W^U(Du^E)u^C.
}
$$

### Family $0_+$：undifferentiated commutator slot

$$
\boxed{
\mathscr P_{0,+}
=
\Big[W^U(Du^C)-W^C(Du^U)\Big]u^E.
}
$$

每一 family 的 action coefficient 都是

$$
-\frac{ig}{4}c_{UCE}.
$$

Exponent vertex coefficient 则是

$$
+\frac{ig}{4\hbar}c_{UCE}.
$$

---

## 1.2 Antichiral three-position polarization

同理，

$$
\begin{aligned}
\operatorname{Pol}S_-^{(3)}
=
+\frac{ig}{4}c_{UCD}\int d^8z\,
\Big\{&
\widetilde W^D(\bar Du^U)u^C
-\widetilde W^C(\bar Du^U)u^D\\
&-\widetilde W^D(\bar Du^C)u^U
+\widetilde W^U(\bar Du^C)u^D\\
&+\widetilde W^C(\bar Du^D)u^U
-\widetilde W^U(\bar Du^D)u^C
\Big\}.
\end{aligned}
$$

三组为

$$
\boxed{
\mathscr P_{F,-}
=
\widetilde W^D
\Big[(\bar Du^U)u^C-(\bar Du^C)u^U\Big],
}
$$

$$
\boxed{
\mathscr P_{\partial,-}
=
\widetilde W^C(\bar Du^D)u^U
-\widetilde W^U(\bar Du^D)u^C,
}
$$

$$
\boxed{
\mathscr P_{0,-}
=
\Big[
\widetilde W^U(\bar Du^C)
-\widetilde W^C(\bar Du^U)
\Big]u^D.
}
$$

每一 family 的 action coefficient 是

$$
+\frac{ig}{4}c_{UCD},
$$

其 exponent coefficient 是

$$
-\frac{ig}{4\hbar}c_{UCD}.
$$

---

## 1.3 为什么 Gate 2Y 只证明第一 family

Gate 2Y 先把 background 固定在 $W$ 或 $\widetilde W$ slot，然后只对余下两个 quantum $u$-ports 作 second variation。因此它计算的是

$$
\delta_U\delta_C
\left[
W^E(Du^U)u^C
\right],
$$

而不是

$$
\delta_U\delta_C\delta_E S^{(3)}.
$$

所以它只能看到

$$
\mathscr P_{F,+},
\qquad
\mathscr P_{F,-},
$$

完全看不到

$$
\mathscr P_{\partial,\pm},
\qquad
\mathscr P_{0,\pm}.
$$

每组有

$$
4\ \text{endpoint rows}
\times 2\ \text{source tags}
\times 2\ \text{action orderings}
=16
$$

个 raw rows。因此

$$
\boxed{16+16+16=48}
$$

而不是乘上 $72$。

---

## 1.4 Exact component counterexample

在 locked component choice

$$
p=e_0,\qquad q=e_1,\qquad
\varepsilon=e_3,\qquad
\ell=(2,-1,1,3),
$$

完整 component sum 为

$$
\boxed{
N_{\rm full}
=
N_F+N_\partial+N_0
=
6-\frac{19}{2}i.
}
$$

固定 field-strength family 为

$$
\boxed{N_F=-5.}
$$

因此 omitted families 的总和为

$$
\begin{aligned}
N_\partial+N_0
&=
N_{\rm full}-N_F\\
&=
6-\frac{19}{2}i+5\\
&=
\boxed{
11-\frac{19}{2}i}.
\end{aligned}
$$

所以

$$
N_{\rm full}\neq m\,N_F
$$

对任何 real route multiplicity $m$ 都不成立：实部要求 $m=-6/5$，虚部则要求 $19/2=0$。

题中没有分别给出 $N_\partial$ 与 $N_0$ 的 component-engine outputs；严格可重放的数据只决定它们的和。写成

$$
N_\partial=\xi,
\qquad
N_0=11-\frac{19}{2}i-\xi,
$$

其中 $\xi$ 不进入后面的 DRED remainder，因为两组的 longitudinal part 被同一 induced contact 消去。

---

# 2. Occurrence-resolved numerators

$$
T_0=I0\_{\rm DminusA1}[A]*A1[B],
\qquad
T_2=I0\_{A1}[A]*{\rm DminusA1}[B].
$$

Corrected source coefficient 为

$$
(-D_-)A_c^{(1)}
=
+\frac1{4\sqrt2}D_-D_+\bar D^2D_+u,
$$

$$
A_c^{(1)}
=
-\frac1{4\sqrt2}D_+\bar D^2D_+u,
$$

所以 primitive source product 是

$$
\boxed{
\left(+\frac1{4\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
=
-\frac1{32}.
}
$$

等价地，用 $D_-D_+=\frac12D^2$，

$$
-\frac1{32}D_-D_+
=
-\frac1{64}D^2.
$$

该 source scalar 已经包含在题中 $N_{S,e}=\bar r_e^2R_e$；不能再次乘入。

---

## 2.1 $T_0$

$$
N_{\rm full,0}=34-8i,
$$

$$
R_0(\ell)=
-\frac12+2i
+\left(1-\frac32i\right)\ell_0
+\left(-\frac12-2i\right)\ell_1
-\frac i2\ell_2-\frac i2\ell_3.
$$

在 $\ell=(2,-1,1,3)$：

$$
\begin{aligned}
R_0
={}&-\frac12+2i
+2\left(1-\frac32i\right)
-\left(-\frac12-2i\right)
-\frac i2-\frac{3i}{2}\\
={}&
-\frac12+2+\frac12
+i\left(2-3+2-\frac12-\frac32\right)\\
={}&
\boxed{2-i}.
\end{aligned}
$$

$$
\bar r_0^2
=
2^2+(-1)^2+1^2+3^2
=
15.
$$

因此

$$
\boxed{
N_{S,0}
=
15(2-i)
=
30-15i.
}
$$

Longitudinal numerator：

$$
\begin{aligned}
L_0
&=
N_{\rm full,0}-N_{S,0}\\
&=
(34-8i)-(30-15i)\\
&=
\boxed{4+7i}.
\end{aligned}
$$

---

## 2.2 $T_2$

$$
N_{\rm full,2}
=
-28-\frac32i,
$$

$$
R_2(\ell)
=
\frac i2
+\left(-1-\frac i2\right)\ell_0
+\frac12\ell_1
-\frac i2\ell_2
-\frac i2\ell_3.
$$

在同一点：

$$
\begin{aligned}
R_2
={}&
\frac i2
+2\left(-1-\frac i2\right)
-\frac12
-\frac i2
-\frac{3i}{2}\\
={}&
-\frac52
+i\left(
\frac12-1-\frac12-\frac32
\right)\\
={}&
\boxed{-\frac52(1+i)}.
\end{aligned}
$$

$$
r_2
=
\ell-p-q
=
(1,-2,1,3),
$$

$$
\bar r_2^2
=
1+4+1+9
=
15.
$$

故

$$
\boxed{
N_{S,2}
=
15\left[-\frac52(1+i)\right]
=
-\frac{75}{2}(1+i).
}
$$

Longitudinal part：

$$
\begin{aligned}
L_2
&=
-28-\frac32i
+\frac{75}{2}(1+i)\\
&=
-\frac{56}{2}+\frac{75}{2}
+i\left(-\frac32+\frac{75}{2}\right)\\
&=
\boxed{\frac{19}{2}+36i}.
\end{aligned}
$$

总和检查：

$$
\begin{aligned}
N_{\rm full,0}+N_{\rm full,2}
&=
34-8i-28-\frac32i\\
&=
\boxed{6-\frac{19}{2}i}.
\end{aligned}
$$

---

## 2.3 Independent affine-quotient checks

这些 checks 不使用 aggregate harmonic trace。

### $\ell^{(1)}=(1,0,0,0)$

$$
\bar r_0^2=1,\qquad
\bar r_2^2=1.
$$

$$
\begin{aligned}
R_0(\ell^{(1)})
&=
-\frac12+2i+1-\frac32i\\
&=
\frac12+\frac i2,
\\
R_2(\ell^{(1)})
&=
\frac i2-1-\frac i2\\
&=-1.
\end{aligned}
$$

所以

$$
N_{S,0}=\frac12+\frac i2,
\qquad
N_{S,2}=-1.
$$

### $\ell^{(2)}=(0,1,0,0)$

$$
\bar r_0^2=1,\qquad
\bar r_2^2=1.
$$

$$
R_0(\ell^{(2)})
=
-\frac12+2i-\frac12-2i
=
-1,
$$

$$
R_2(\ell^{(2)})
=
\frac i2+\frac12
=
\frac12+\frac i2.
$$

因此

$$
N_{S,0}=-1,
\qquad
N_{S,2}=\frac12+\frac i2.
$$

### $\ell^{(3)}=(1,1,1,0)$

$$
\bar r_0^2=3,
\qquad
r_2=(0,0,1,0),
\qquad
\bar r_2^2=1.
$$

$$
\begin{aligned}
R_0(\ell^{(3)})
&=
-\frac12+2i
+1-\frac32i
-\frac12-2i
-\frac i2\\
&=-2i,
\\
R_2(\ell^{(3)})
&=
\frac i2-1-\frac i2+\frac12-\frac i2\\
&=-\frac12-\frac i2.
\end{aligned}
$$

所以

$$
N_{S,0}=-6i,
\qquad
N_{S,2}=-\frac12-\frac i2.
$$

要在这些额外点分别数值检查 $N_{\rm full,e}$ 与 $L_e$，还需要 component engine 输出完整 polynomial $N_{\rm full,e}(\ell)$；题中只提供了其在 $(2,-1,1,3)$ 的值。这里不虚构未给出的 polynomial。

---

# 3. Induced Schwinger contacts

固定 occurrence $e$，对同一 full action 作 functional integration by parts：

$$
0
=
\int Du\,
\frac{\delta}{\delta u_e}
\left[
\mathcal X_e[u]\,
e^{-(S_2+S_3)/\hbar}
\right].
$$

在目标 order，$\delta/\delta u_e$ 对两个 cubic actions 的作用为

$$
\delta_e(S_-^{(3)}S_+^{(3)})
=
(\delta_eS_-^{(3)})S_+^{(3)}
+
S_-^{(3)}(\delta_eS_+^{(3)}),
$$

因为两个 cubic actions 都是 Grassmann-even，不产生额外 Koszul sign。

对该 occurrence，$d$-dimensional parent numerator 是

$$
N_{\mathrm{parent},e}^{(d)}
=
r_{e,d}^2R_e+L_e.
$$

同一 functional derivative 产生的 contact 必须是其负值：

$$
\boxed{
C_{e,d}
=
-r_{e,d}^2R_e-L_e.
}
$$

这不是额外独立计算的 source bubble。

---

## 3.1 Row identity

$$
\begin{aligned}
N_{\rm full,e}+C_{e,d}
&=
\bar r_e^2R_e+L_e
-L_e-r_{e,d}^2R_e\\
&=
(\bar r_e^2-r_{e,d}^2)R_e\\
&=
\boxed{\mu_\ell^2R_e}.
\end{aligned}
$$

若把 four-dimensional spin numerator $\bar r_e^2$ 全部替换成 $r_{e,d}^2$，则

$$
\begin{aligned}
N_{\rm full,e}^{(d)}+C_{e,d}
&=
r_{e,d}^2R_e+L_e
-L_e-r_{e,d}^2R_e\\
&=
\boxed{0}.
\end{aligned}
$$

因此唯一 DRED defect 是

$$
\boxed{
\frac{\mu_\ell^2R_e}{D_0D_1D_2}.
}
$$

没有额外 $4-d$。

---

## 3.2 Contact decomposition

利用

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
=
\frac1{\prod_{j\neq e}D_j},
$$

contact integrand 为

$$
\begin{aligned}
\frac{C_{e,d}}{D_0D_1D_2}
&=
-\frac{L_e}{D_0D_1D_2}
-\frac{r_{e,d}^2R_e}{D_0D_1D_2}\\
&=
\boxed{
-\frac{L_e}{D_0D_1D_2}
-\frac{R_e}{\prod_{j\neq e}D_j}}.
\end{aligned}
$$

第二项是 affine two-denominator contact。因为 $R_e$ 是非零 affine polynomial，它不能被删除。

---

## 3.3 Sample contacts

### Edge $0$

$$
C_{0,d}
=
-(4+7i)-r_{0,d}^2(2-i).
$$

在严格 four-dimensional replacement $r_{0,d}^2=15$：

$$
\begin{aligned}
C_{0,4}
&=
-4-7i-30+15i\\
&=
\boxed{-34+8i}.
\end{aligned}
$$

$$
N_{\rm full,0}+C_{0,4}
=
34-8i-34+8i
=
0.
$$

### Edge $2$

$$
C_{2,d}
=
-\left(\frac{19}{2}+36i\right)
+\frac52r_{2,d}^2(1+i).
$$

在 $r_{2,d}^2=15$：

$$
\begin{aligned}
C_{2,4}
&=
-\frac{19}{2}-36i
+\frac{75}{2}
+\frac{75}{2}i\\
&=
28+\frac32i.
\end{aligned}
$$

$$
N_{\rm full,2}+C_{2,4}
=
-28-\frac32i
+28+\frac32i
=
0.
$$

---

# 4. Rank-one integration

Locked routing：

$$
r_0=\ell,
\qquad
r_1=\ell-q,
\qquad
r_2=\ell-p-q.
$$

Feynman parameters $x+y+z=1$ give

$$
xD_0+yD_1+zD_2
=
\left[\ell-yq-z(p+q)\right]^2+\Delta.
$$

设

$$
L:=\ell-yq-z(p+q).
$$

则

$$
\ell=L+yq+z(p+q).
$$

Simplex moments：

$$
\int_{\Delta_2}1=\frac12,
\qquad
\int_{\Delta_2}y=\frac16,
\qquad
\int_{\Delta_2}z=\frac16.
$$

Normalized rank-one moment：

$$
\begin{aligned}
\langle\ell\rangle
&=
\frac{
q\int y+(p+q)\int z
}{
\int1
}\\
&=
\frac{
q/6+(p+q)/6
}{
1/2
}\\
&=
\boxed{\frac{p+2q}{3}}.
\end{aligned}
$$

---

## 4.1 Integrated $R_0$

$$
\langle\ell_0\rangle=\frac13,
\qquad
\langle\ell_1\rangle=\frac23,
\qquad
\langle\ell_2\rangle
=
\langle\ell_3\rangle
=0.
$$

$$
\begin{aligned}
\langle R_0\rangle
={}&
-\frac12+2i
+\frac13\left(1-\frac32i\right)
+\frac23\left(-\frac12-2i\right)\\
={}&
-\frac12
+\frac13-\frac13\\
&\quad
+i\left(
2-\frac12-\frac43
\right)\\
={}&
\boxed{-\frac12+\frac i6}.
\end{aligned}
$$

## 4.2 Integrated $R_2$

$$
\begin{aligned}
\langle R_2\rangle
={}&
\frac i2
+\frac13\left(-1-\frac i2\right)
+\frac23\left(\frac12\right)\\
={}&
-\frac13+\frac13
+i\left(\frac12-\frac16\right)\\
={}&
\boxed{\frac i3}.
\end{aligned}
$$

总 quotient：

$$
\boxed{
\langle R_0+R_2\rangle
=
-\frac12+\frac i2}.
$$

因此

$$
\begin{aligned}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2(R_0+R_2)}
{D_0D_1D_2}
&=
\frac1{32\pi^2}
\left(-\frac12+\frac i2\right)\\
&=
\boxed{\frac{-1+i}{64\pi^2}}.
\end{aligned}
$$

---

## 4.3 Typed reconstruction

Locked matrices

$$
\sigma_E=(-i\sigma^1,-i\sigma^2,-i\sigma^3,\mathbf1)
$$

imply

$$
\mathsf p=-i\sigma_E\!\cdot e_0=-\sigma^1
=
\begin{pmatrix}
0&-1\\-1&0
\end{pmatrix},
$$

$$
\mathsf q=-i\sigma_E\!\cdot e_1=-\sigma^2
=
\begin{pmatrix}
0&i\\-i&0
\end{pmatrix}.
$$

这些 sigma conventions 由 Step 1 锁定。

在 $\dot\alpha=0$ component normalization 中，

$$
\mathcal T_p\longmapsto-1,
\qquad
\mathcal T_q\longmapsto+i.
$$

故

$$
-\frac12+\frac i2
=
\frac12(-1)+\frac12(i)
$$

唯一重建为

$$
\boxed{
\langle R_0+R_2\rangle
=
\frac12\mathcal T_p
+
\frac12\mathcal T_q.
}
$$

所以 DA orientation 的 integrated kinematic remainder 是

$$
\boxed{
\frac1{64\pi^2}
\left(
\mathcal T_p+\mathcal T_q
\right)}.
$$

---

# 5. Complete normalization ledger

两个 exponent vertices：

$$
\left(
-\frac{ig}{4\hbar}
\right)_{\!-\text{ chirality}}
\left(
+\frac{ig}{4\hbar}
\right)_{\!+\text{ chirality}}
=
\frac{g^2}{16\hbar^2}.
$$

三条 locked propagators：

$$
(-\hbar)^3=-\hbar^3.
$$

因此共同 action–propagator factor：

$$
\boxed{
\mathcal C_{\rm AP}
=
-\frac{\hbar g^2}{16}.
}
$$

Action ordering：

$$
\frac1{2!}
\left(
S_-^{(3)}S_+^{(3)}
+
S_+^{(3)}S_-^{(3)}
\right)
=
S_-^{(3)}S_+^{(3)},
$$

故

$$
w_{\rm Wick}=1.
$$

Corrected source coefficient、Berezin saturation、48-row relative action sum 已经包含在 $R_0,R_2$，不再重乘。

于是

$$
\begin{aligned}
\Gamma_{DA}^{AB}
&=
-\frac{\hbar g^2}{16}
\frac1{64\pi^2}
\mathbb F^{AB}{}_{DE}
\left(
\mathcal T_p^{DE}
+
\mathcal T_q^{DE}
\right)\\
&=
-\frac{\hbar g^2}{1024\pi^2}
\mathbb F^{AB}{}_{DE}
\left(
\mathcal T_p^{DE}
+
\mathcal T_q^{DE}
\right)\\
&=
\boxed{
-\frac{\lambda_1}{64}
\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^{D}(q)p^{\dot\alpha}A^E(p)
+
D_{\dot\alpha}^{D}(q)q^{\dot\alpha}A^E(p)
\right]}.
\end{aligned}
$$

没有 $72$，没有额外 source scalar，没有额外 endpoint sum。

---

# 6. Reflected AD orientation

## 6.1 Ordered functional derivative

所有被 functional-differentiated 的 $u$-fields 都是 even，因此

$$
\frac{\delta^3S^{(3)}}
{\delta u_A\delta u_B\delta u_E}
=
\frac{\delta^3S^{(3)}}
{\delta u_B\delta u_A\delta u_E}.
$$

反射交换：

$$
T_0\leftrightarrow T_2,
\qquad
A\leftrightarrow B,
\qquad
D\leftrightarrow E,
$$

不产生 functional-derivative Koszul sign。

Color：

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
\boxed{\mathbb F^{AB}{}_{DE}}.
\end{aligned}
$$

---

## 6.2 Natural reflected spinor word

Independent reflected derivative gives

$$
\frac12
\left[
(p^{\dot\alpha}A^D)D_{\dot\alpha}^E
+
(q^{\dot\alpha}A^D)D_{\dot\alpha}^E
\right].
$$

现在只执行 epsilon lowering。由

$$
X^{\dot\alpha}
=
\epsilon^{\dot\alpha\dot\beta}X_{\dot\beta},
$$

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

所以 reflected kinematic remainder 是

$$
-\frac12
\left(
\widetilde{\mathcal T}_p
+
\widetilde{\mathcal T}_q
\right).
$$

乘同一个 $\mathcal C_{\rm AP}$：

$$
\boxed{
\Gamma_{AD}^{AB}
=
+\frac{\lambda_1}{64}
\mathbb F^{AB}{}_{DE}
\left[
(p_{\dot\alpha}A^D)D^{E\dot\alpha}
+
(q_{\dot\alpha}A^D)D^{E\dot\alpha}
\right]}.
$$

这里的 plus 不是从一个固定 $SU(2)$ color component 猜出的；它来自：

$$
(-\hbar g^2/16)
\times
(-1/2\ \text{epsilon sign})
=
+\hbar g^2/32,
$$

再乘 loop master。

---

# 7. Complete target-blind ordered AA vector

合并 DA 与 AD：

$$
\boxed{
\begin{aligned}
\Gamma_{AA,G}^{AB}
={}&
-\frac{\lambda_1}{64}
\mathbb F^{AB}{}_{DE}
\Big[
D_{\dot\alpha}^{D}(q)
(p+q)^{\dot\alpha}A^E(p)\\
&\hspace{32mm}
-
\big((p+q)_{\dot\alpha}A^D(p)\big)
D^{E\dot\alpha}(q)
\Big].
\end{aligned}}
$$

因此在 basis $\mathcal B_{AA}$ 中：

$$
\boxed{
\vec C_{AA,G}^{\rm Project}
=
\frac{\lambda_1}{64}
(-1,-1,+1,+1)
=
-\frac{\lambda_1}{64}
(1,1,-1,-1).
}
$$

这是 full polarized gauge-cubic result。关键变化是

$$
\boxed{p-q\quad\longrightarrow\quad p+q},
$$

其来源是 omitted $32$ rows 与 induced occurrence contacts，而不是 multiplicity。

---

# 8. Holomorphic-twist comparison

HT gauge-sector AA word 为

$$
D(q)(p+q)A(p)
-
((p+q)A(p))D(q),
$$

即 ordered structural vector

$$
(1,1,-1,-1).
$$

因此：

$$
\boxed{
\text{relative derivative structure and reflected sign now agree exactly}.
}
$$

若采用之前 later-comparison branch 的 coefficient

$$
\vec C_{AA,G}^{HT}
=
+\frac{\lambda_1}{8}
(1,1,-1,-1),
$$

则

$$
\frac{
C_{\rm Project}
}{
C_{HT}
}
=
\frac{-1/64}{1/8}
=
\boxed{-\frac18},
$$

且

$$
\boxed{
\vec C_{\rm Project}
-
\vec C_{HT}
=
-\frac{9\lambda_1}{64}
(1,1,-1,-1).
}
$$

第一处剩余 mismatch 已不在：

- polarized vertex；
- $p\pm q$
- reflection epsilon sign；
- Schwinger contact；
- route multiplicity。

它出现在共同 overall normalization/sign：

$$
\boxed{
-\frac{\lambda_1}{64}
\quad\text{versus}\quad
+\frac{\lambda_1}{8}.
}
$$

不过 HT source 自身仍存在

$$
-\frac14
\quad\text{versus}\quad
-\kappa_H^2
$$

以及 zero-shift factor-two conflict，因此该 absolute mismatch 不能用 HT target 反向修补。

唯一未能由题中给定 numerical data 单独重放的是

$$
N_\partial,\qquad N_0
$$

各自的 sample value，以及 $N_{\rm full,e}(\ell)$ 的完整 affine/quadratic polynomial；已给数据只确定

$$
N_\partial+N_0
=
11-\frac{19}{2}i.
$$

这不影响上面的 contact cancellation、$\mu_\ell^2R_e$ remainder 或最终 ordered vector。
