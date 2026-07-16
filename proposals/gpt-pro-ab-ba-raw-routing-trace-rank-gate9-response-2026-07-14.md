## 记号

令

$$
P_D:=D_0D_1D_2,
\qquad
\langle f\rangle_{\Sigma_2}
:=
2\int_{\substack{x,y,z\geq0\\x+y+z=1}}f(x,y,z).
$$

对 ordered local words 定义

$$
\Pi_{DB}:=\langle D,B_1\rangle
=
D_{\dot\alpha}(P^{\dot\alpha}B_1),
$$

$$
E_{DB}:=(P^{\dot\alpha}D_{\dot\alpha})B_1,
$$

$$
\Pi_{BD}:=\langle B_1,D\rangle
=
(P_{\dot\alpha}B_1)D^{\dot\alpha},
$$

$$
E_{BD}:=B_1(P_{\dot\alpha}D^{\dot\alpha}).
$$

因为 ordinary translation $P$ 是 even derivation，

$$
T_{DB}:=P^{\dot\alpha}(D_{\dot\alpha}B_1)
=E_{DB}+\Pi_{DB},
$$

$$
T_{BD}:=P_{\dot\alpha}(B_1D^{\dot\alpha})
=\Pi_{BD}+E_{BD}.
$$

Project 的 left-Grassmann Leibniz rule 是

$$
\partial_\zeta(FG)
=(\partial_\zeta F)G+(-1)^{|F|}F(\partial_\zeta G).
$$

---

# 1. Final local phases 与右端点 momentum

Fourier convention：

$$
B_1(x)
=
\int_p e^{ipx}B_1(p),
\qquad
D_{\dot\alpha}(x)
=
\int_q e^{iqx}D_{\dot\alpha}(q).
$$

因此最终 local product 的 phase 是

$$
e^{ipx}e^{iqx}=e^{i(p+q)x}.
$$

所以：

$$
\boxed{
B_1\text{ carries phase }e^{ipx},
\qquad
D\text{ carries phase }e^{iqx}.
}
$$

source momentum 是

$$
s=-(p+q).
$$

由 routing

$$
r_0-r_1=p,
\qquad
r_1-r_2=q.
$$

左 action endpoint 的 outward momentum 是

$$
p_{\rm phys}=r_0-r_1=p.
$$

但右 endpoint 的 D-word derivative 是 inward-oriented：

$$
q_{\rm word}=r_2-r_1.
$$

所以

$$
\boxed{
q_{\rm word}=r_2-r_1=-q_{\rm phys}.
}
$$

这就是 G2 逻辑中的第一个 exact sign error：

$$
\boxed{
q_{\rm word}=q_{\rm phys}
\quad\text{是错误 equality}.
}
$$

正确 equality 是

$$
\boxed{
q_{\rm word}=-q_{\rm phys}.
}
$$

---

# 2. G2：正确 momentum typing

supplied raw expression 是

$$
G_2^{\rm displayed}
=
\frac13B_1(p)
\left(4p-q_{\rm word}\right)^{\dot\alpha}
D_{\dot\alpha}(q).
$$

使用

$$
q_{\rm word}=-q,
$$

得到 physical external-momentum expression

$$
\boxed{
G_{2,\rm raw}^{\rm mom}
=
\frac13B_1(p)
(4p+q)^{\dot\alpha}
D_{\dot\alpha}(q).
}
$$

不是

$$
\frac13B_1(4p-q_{\rm phys})D.
$$

---

## 2.1 Fourier operator map

$$
P_{\dot\alpha}B_1
\longleftrightarrow
ip_{\dot\alpha}B_1(p),
$$

$$
P^{\dot\alpha}D_{\dot\alpha}
\longleftrightarrow
iq^{\dot\alpha}D_{\dot\alpha}(q).
$$

因此，stripping the common raw phase $+i$：

$$
\frac13(4p+q)
\longleftrightarrow
\frac43\Pi_{BD}+\frac13E_{BD}.
$$

即

$$
\boxed{
G_{2,\rm typed}
=
\lambda_1
\left(
\frac43\langle B_1,D\rangle
+
\frac13B_1(P\cdot D)
\right).
}
$$

利用

$$
T_{BD}=\Pi_{BD}+E_{BD},
$$

有

$$
\begin{aligned}
\frac43\Pi_{BD}+\frac13E_{BD}
&=
\Pi_{BD}
+\frac13(\Pi_{BD}+E_{BD})\\
&=
\Pi_{BD}+\frac13T_{BD}.
\end{aligned}
$$

所以

$$
\boxed{
G_{2,\rm typed}
=
\lambda_1
\left[
\langle B_1,D\rangle
+
\frac13P_{\dot\alpha}
(B_1D^{\dot\alpha})
\right].
}
$$

在 total-derivative quotient 中，

$$
[T_{BD}]=0,
$$

故

$$
\boxed{
[G_2]
=
\lambda_1\langle B_1,D\rangle.
}
$$

因此 G2 typed coefficient 是

$$
\boxed{C_{G_2}=1}.
$$

---

## 2.2 为什么 $4/3-1/3=1$ 是正确的

在 total-derivative quotient：

$$
\Pi_{BD}+E_{BD}=0,
$$

所以

$$
E_{BD}=-\Pi_{BD}.
$$

因此

$$
\frac43\Pi_{BD}+\frac13E_{BD}
=
\left(
\frac43-\frac13
\right)\Pi_{BD}
=
\Pi_{BD}.
$$

所以旧式

$$
\boxed{
\frac43-\frac13=1
}
$$

本身是正确的，但其正确理由不是 $q=p$，也不是 $q=-p$ 的直接 substitution，而是

$$
\boxed{
B_1(P\cdot D)
\equiv
-\langle B_1,D\rangle
\quad
\bmod\ \text{total derivatives}.
}
$$

---

## 2.3 哪些项可以删除

可以删除：

$$
\boxed{
P_{\dot\alpha}(B_1D^{\dot\alpha})
}
$$

因为它是完整 local product 的 total derivative。

不能 standalone 删除：

$$
\boxed{
B_1(P\cdot D).
}
$$

它是 an EOM carrier，但在 complete SD orbit 中已有对应 derivative-of-action contact。若把它再次设为零，就重复使用了一次 EOM contact。

正确 quotient reduction 是

$$
\frac43\Pi_{BD}+\frac13E_{BD}
\longrightarrow
\Pi_{BD},
$$

而不是

$$
\frac43\Pi_{BD}+\frac13E_{BD}
\longrightarrow
\frac43\Pi_{BD}.
$$

---

# 3. G1：两 marked pieces 的真实含义

定义

$$
A=D_+\bar D^2D_+u,
\qquad
B_1=D_+\phi_1.
$$

Grassmann parities：

$$
|A|
=
1+0+1
=
0,
$$

$$
|B_1|=1.
$$

因此

$$
\nabla_-(AB_1)
=
(\nabla_-A)B_1
+
A(\nabla_-B_1),
$$

第二项没有额外 minus sign。

令 $\mathcal V_\rho$ 是任意一个 polarized VVV row。因为

$$
|AB_1|=1,
\qquad
|\mathcal V_\rho|=0,
$$

Berezin IBP 给出

$$
\begin{aligned}
0
&=
\int\nabla_-
\left[
(AB_1)\mathcal V_\rho
\right]\\
&=
\int
\left[
(\nabla_-A)B_1
+
A(\nabla_-B_1)
\right]
\mathcal V_\rho\\
&\quad
-
\int AB_1(\nabla_-\mathcal V_\rho).
\end{aligned}
$$

所以逐 row：

$$
\boxed{
\int
\left[
(\nabla_-A)B_1
+
A(\nabla_-B_1)
\right]\mathcal V_\rho
=
\int AB_1(\nabla_-\mathcal V_\rho).
}
$$

这说明：

$$
\boxed{
A\text{-mark 和 }B\text{-mark
是同一个 transported SD orbit 的两个 source-product presentations，}
}
$$

不是两个额外 Feynman graphs。

---

# 4. 为什么当前 $G_{1,A}+G_{1,B}$ 是错误的

Feynman shift：

$$
xD_0+yD_1+zD_2,
\qquad
x+y+z=1,
$$

$$
\ell
=
k+(y+z)p+zq.
$$

Normalized simplex moments：

$$
\langle y\rangle_{\Sigma_2}
=
\langle z\rangle_{\Sigma_2}
=
\frac13.
$$

所以

$$
\begin{aligned}
\langle r_0\rangle_{\Sigma_2}
&=
\langle\ell\rangle_{\Sigma_2}\\
&=
\frac23p+\frac13q,
\end{aligned}
$$

$$
\begin{aligned}
\langle r_2\rangle_{\Sigma_2}
&=
\langle\ell-p-q\rangle_{\Sigma_2}\\
&=
\frac23p+\frac13q-p-q\\
&=
-\frac13p-\frac23q.
\end{aligned}
$$

当前 reported pieces 正好是

$$
\begin{aligned}
G_{1,A}
&=
\frac43p+\frac23q\\
&=
2\langle r_0\rangle_{\Sigma_2},
\end{aligned}
$$

$$
\begin{aligned}
G_{1,B}
&=
\frac23p+\frac43q\\
&=
-2\langle r_2\rangle_{\Sigma_2}.
\end{aligned}
$$

于是

$$
\begin{aligned}
G_{1,A}+G_{1,B}
&=
2\langle r_0-r_2\rangle_{\Sigma_2}\\
&=
2(p+q).
\end{aligned}
$$

即

$$
\boxed{
G_{1,A}+G_{1,B}=2(p+q).
}
$$

而 $p+q$ 正是 local product 的 total momentum。因此

$$
\boxed{
G_{1,A}+G_{1,B}
\text{ 是 total-derivative presentation，}
}
$$

不能被读取为 physical coefficient vector

$$
(2,2).
$$

所以 G1 branch 中第一个错误 equality 是

$$
\boxed{
G_{1,\rm physical}
=
G_{1,A}+G_{1,B}.
}
$$

正确 statement 是：

$$
\boxed{
G_{1,A},G_{1,B}
\text{ 是 endpoint presentations；}
\quad
G_{1,\rm physical}
\text{ 是 transported action-Hessian orbit counted once}.
}
$$

原来 $q=-p$ 的 one-variable test 给出

$$
G_{1,A}=\frac23p,
\qquad
G_{1,B}=-\frac23p,
$$

其 sum 为零，正好验证

$$
2(p+q)\Big|_{q=-p}=0.
$$

它并没有给出 physical G1 coefficient。

---

# 5. 六个 VVV permutations 与 raw multiplicity

每 chirality：

$$
6\ \text{color permutations}
\times
2\ \{QL,LQ\}
=
12\ \text{polarized rows}.
$$

两 chiralities：

$$
12\times2=24\ \text{rows}.
$$

Outer descendant 给出两个 formal source marks，所以 displayed algebraic terms 是

$$
24\times2=48.
$$

但逐 row 的 identity

$$
(\nabla_-A)B_1
+
A(\nabla_-B_1)
\longleftrightarrow
AB_1(\nabla_-\mathcal V_\rho)
$$

把两个 marks 组成一个 SD orbit。因此 physical descendant row count 是

$$
\boxed{24},
$$

不是 $48$。

由于三条 edges 在完整 $S_3$ polarization 中对称出现，每 chirality：

$$
\boxed{
N_{e_0}=N_{e_1}=N_{e_2}=4.
}
$$

两 chiralities：

$$
\boxed{
N_{e_0}=N_{e_1}=N_{e_2}=8.
}
$$

在 color reduction 和 row summation 后，这些成为每 ordered orientation 的三个 tagged occurrence classes；不是三张附加 graph，也不是 $24$ 倍 multiplicity。

---

## 5.1 Exact row reflection

定义

$$
\pi^\vee:=(\pi_3,\pi_2,\pi_1),
$$

并取

$$
QL\longleftrightarrow LQ,
\qquad
e_0\longleftrightarrow e_2,
\qquad
e_1\longleftrightarrow e_1.
$$

六个 permutations 成对：

$$
123\longleftrightarrow321,
$$

$$
132\longleftrightarrow231,
$$

$$
213\longleftrightarrow312.
$$

Color reversal 给出一个 minus sign；QL/LQ endpoint reversal 给出第二个 minus sign：

$$
(-1)_{\rm color}
(-1)_{\rm endpoint}
=+1.
$$

对于 reflected external word，$D$ 与 $B_1$ 都是 odd：

$$
(-1)_{\rm external\ Koszul}
=-1.
$$

Ordered external color word reflection 也给出

$$
(-1)_{\rm external\ color}
=-1.
$$

所以

$$
(-1)_{\rm external\ Koszul}
(-1)_{\rm external\ color}
=+1.
$$

因此 row-by-row reflection 保持 raw scalar normalization。

这不是 HT symmetry assumption；它是 complete polarized VVV row involution。

---

# 6. G1 的正确 raw momentum polynomial

G2 corrected physical polynomial 是

$$
B_1(p)\frac{4p+q}{3}D(q).
$$

应用上述 exact row reflection：

$$
p\longleftrightarrow q,
\qquad
B_1D\longleftrightarrow DB_1,
$$

得到

$$
\boxed{
G_{1,\rm raw}^{\rm mom}
=
D_{\dot\alpha}(p)
\frac{(p+4q)^{\dot\alpha}}3
B_1(q).
}
$$

这里：

- $p$
- $q$
- $\langle D,B_1\rangle$
- $(P\cdot D)B_1$

因此

$$
\boxed{
G_{1,\rm typed}
=
\lambda_1
\left[
\frac13(P\cdot D)B_1
+
\frac43\langle D,B_1\rangle
\right].
}
$$

重新排列：

$$
\begin{aligned}
\frac13E_{DB}+\frac43\Pi_{DB}
&=
\Pi_{DB}
+\frac13(E_{DB}+\Pi_{DB})\\
&=
\Pi_{DB}+\frac13T_{DB}.
\end{aligned}
$$

所以

$$
\boxed{
G_{1,\rm typed}
=
\lambda_1
\left[
\langle D,B_1\rangle
+
\frac13P^{\dot\alpha}
(D_{\dot\alpha}B_1)
\right].
}
$$

在 total-derivative quotient：

$$
\boxed{
[G_1]
=
\lambda_1\langle D,B_1\rangle.
}
$$

因此 canonical pre-quotient coefficients 是

$$
\boxed{
\operatorname{coeff}
\bigl(
\langle D,B_1\rangle,
(P\cdot D)B_1
\bigr)
=
\left(
\frac43,\frac13
\right),
}
$$

而 quotient representative 可取

$$
\boxed{
\operatorname{coeff}_{\rm quotient}
=
(1,0).
}
$$

---

## 6.1 与 one-variable replay 的关系

在

$$
q=-p
$$

时，完整 G1 polynomial 是

$$
\frac13(p+4q)
=
\frac13(p-4p)
=
-p.
$$

但 pairing momentum 是 $q=-p$，所以

$$
-p=q.
$$

因此 pairing coefficient 为

$$
\boxed{+1}.
$$

这与 endpoint pieces

$$
+\frac23p,\qquad-\frac23p
$$

不矛盾，因为后两者只是 total-derivative endpoint pair，而不是 complete transported orbit。

---

# 7. Occurrence-wise full-$d$ SD cancellation

对每个 tagged occurrence $\alpha$，定义：

$$
\alpha\in
\{1,\ 2{\rm det},\ 2\Omega\},
$$

$$
c_1=1-z,
\qquad
c_{2{\rm det}}=z,
\qquad
c_{2\Omega}=-\frac12.
$$

令其 tagged edge 为 $e_\alpha$，其 routed external word 为 $W_\alpha$。

在题目锁定的 exact raw units 中：

$$
N_{\alpha,\rm raw}
=
c_\alpha
\frac{\bar r_{e_\alpha}^{\,2}W_\alpha}{P_D},
$$

$$
K_{\alpha,\rm raw}
=
-c_\alpha
\frac{W_\alpha}
{\prod_{j\neq e_\alpha}D_j}.
$$

Full-$d$ part：

$$
N_{\alpha,\rm raw}^{(d)}
=
c_\alpha
\frac{D_{e_\alpha}W_\alpha}{P_D}.
$$

因为

$$
P_D
=
D_{e_\alpha}
\prod_{j\neq e_\alpha}D_j,
$$

所以

$$
\begin{aligned}
N_{\alpha,\rm raw}^{(d)}
+
K_{\alpha,\rm raw}
&=
c_\alpha
\frac{D_{e_\alpha}W_\alpha}{P_D}
-
c_\alpha
\frac{W_\alpha}
{\prod_{j\neq e_\alpha}D_j}\\
&=
c_\alpha
\frac{D_{e_\alpha}W_\alpha}{P_D}
-
c_\alpha
\frac{D_{e_\alpha}W_\alpha}{P_D}\\
&=
0.
\end{aligned}
$$

即

$$
\boxed{
N_{\alpha,\rm raw}^{(d)}
+
K_{\alpha,\rm raw}
=0
\qquad
\text{for every }\alpha.
}
$$

逐项写为

$$
(1-z)
\frac{D_{e_1}W_1}{P_D}
-
(1-z)
\frac{W_1}{\prod_{j\neq e_1}D_j}
=0,
$$

$$
z
\frac{D_{e_{2{\rm det}}}W_{2{\rm det}}}{P_D}
-
z
\frac{W_{2{\rm det}}}
{\prod_{j\neq e_{2{\rm det}}}D_j}
=0,
$$

$$
-\frac12
\frac{D_{e_{2\Omega}}W_{2\Omega}}{P_D}
+
\frac12
\frac{W_{2\Omega}}
{\prod_{j\neq e_{2\Omega}}D_j}
=0.
$$

没有 $\chi$，没有额外 metric trace。

Finite remainder：

$$
\boxed{
R_{\alpha,\rm raw}
=
c_\alpha
\frac{\mu_\ell^2W_\alpha}{P_D}.
}
$$

---

## 7.1 Reflected G1 occurrences

Reflection 交换

$$
e_0\leftrightarrow e_2,
\qquad
x\leftrightarrow z.
$$

因此 G1 weights 是

$$
c_1^\vee=1-x,
\qquad
c_{2{\rm det}}^\vee=x,
\qquad
c_{2\Omega}^\vee=-\frac12.
$$

且

$$
\langle1-x\rangle_{\Sigma_2}
=
\frac23,
$$

$$
\langle x\rangle_{\Sigma_2}
=
\frac13,
$$

$$
\left\langle-\frac12\right\rangle_{\Sigma_2}
=
-\frac12.
$$

每个 reflected occurrence 同样满足

$$
\boxed{
N_{\alpha^\vee,\rm raw}^{(d)}
+
K_{\alpha^\vee,\rm raw}
=0.
}
$$

---

# 8. Full factor ledger

| factor | exact value / operation |
| --- | --- |
| source mixed-Hessian factorial | $1$ |
| outer descendant Leibniz coefficients | $+1,+1$ |
| two formal source marks | one transported SD orbit, not factor $2$ |
| action Taylor ordering | $\frac1{2!}(1+1)=1$ |
| VVV color permutations | $6$, all retained inside polarization |
| QL/LQ placements | $2$, algebraic rows, not graph multiplicity |
| chiralities | $2$, independently replayed |
| fixed ordered Wick pairing | $1$ |
| graph automorphism division | $1$ |
| $d^4\theta$ projector | $1/4$ |
| $d^2\bar\theta$ projector | $1/2$ |
| rank extraction | $-1/2$ |
| extra metric/trace factor | $1$ |
| common measure conversion | $(1/4)(1/2)(-1/2)=-1/16$ |
| Feynman simplex prefactor | $2$ |
| DRED master integral | $1/(32\pi^2)$ |
| direct ordered color phase | $+i$ |
| one ordinary momentum conversion | $p=P/i=-iP$ |
| $+i$ raw phase $\times(-i)$ Fourier conversion | $+1$ |
| G1/G2 external field-map magnitude | $1$ |
| loop coupling | $\lambda_1=\hbar g^2/(16\pi^2)$ |

The ordered Berezin projectors used here are fixed by

$$
[X]_F=-\frac14D^2X\big|,
\qquad
[Y]_D=\frac1{16}D^2\bar D^2Y\big|.
$$

No post-replay factor is allowed.

---

# 9. Fourier ledger including G3

## G1

Raw phase form：

$$
i\lambda_1
D(p)
\frac{p+4q}{3}
B_1(q).
$$

Using

$$
p=\frac{P_D}{i},
\qquad
q=\frac{P_B}{i},
$$

one factor $1/i=-i$ gives

$$
i(-i)=1.
$$

所以 typed coefficient 是 real $+1$。

## G2

Raw phase form：

$$
i\lambda_1
B_1(p)
\frac{4p+q}{3}
D(q).
$$

同样：

$$
i(-i)=1.
$$

typed coefficient 是 real $+1$。

## G3

Raw coefficients：

$$
(+i\sqrt2,-i\sqrt2).
$$

G3 contains two ordinary momentum operators：

$$
(ip)_{\dot\alpha}(iq)^{\dot\alpha}
=
-p_{\dot\alpha}q^{\dot\alpha}.
$$

因此 two Fourier conversions 给出

$$
(-i)^2=-1.
$$

所以

$$
(+i\sqrt2,-i\sqrt2)
\longmapsto
(-i\sqrt2,+i\sqrt2).
$$

---

# 10. Exact typed results

Canonical pre-total-derivative representatives：

$$
\boxed{
G_1
=
\lambda_1
\left[
\frac43\langle D,B_1\rangle
+
\frac13(P\cdot D)B_1
\right],
}
$$

$$
\boxed{
G_2
=
\lambda_1
\left[
\frac43\langle B_1,D\rangle
+
\frac13B_1(P\cdot D)
\right].
}
$$

Equivalent form：

$$
\boxed{
G_1
=
\lambda_1
\left[
\langle D,B_1\rangle
+
\frac13P\cdot(DB_1)
\right],
}
$$

$$
\boxed{
G_2
=
\lambda_1
\left[
\langle B_1,D\rangle
+
\frac13P\cdot(B_1D)
\right].
}
$$

In the local total-derivative quotient：

$$
\boxed{
[G_1]
=
\lambda_1\langle D,B_1\rangle,
}
$$

$$
\boxed{
[G_2]
=
\lambda_1\langle B_1,D\rangle.
}
$$

因此

$$
\boxed{
C_{G_1}=1,
\qquad
C_{G_2}=1.
}
$$

---

# 11. First-error ledger

## G2

First false equality：

$$
\boxed{
q_{\rm word}=q_{\rm physical}.
}
$$

Correct：

$$
\boxed{
q_{\rm word}=-q_{\rm physical}.
}
$$

所以

$$
4p-q_{\rm word}
=
4p+q_{\rm physical}.
$$

The $q$-term is $+\frac13E_{BD}$, not $-\frac13E_{BD}$.

---

## G1

First false multiplicity equality：

$$
\boxed{
G_{1,\rm physical}=G_{1,A}+G_{1,B}.
}
$$

因为

$$
G_{1,A}+G_{1,B}=2(p+q),
$$

它只是 total derivative。

正确 physical object 是：

$$
\boxed{
\text{one transported VVV SD orbit},
}
$$

whose row-reflected polynomial is

$$
\boxed{
\frac13(p+4q).
}
$$

The vector

$$
(-7/6,-4/3)
$$

不能来自完整 row involution，因为它既不 obey $p\leftrightarrow q$ reflection of the corrected G2 polynomial，也不 reproduce the complete $q=-p$ coefficient $+1$.

---

# 12. Target-blind covariance check

按 basis

$$
\left(
\langle D,B_1\rangle,
\langle B_1,D\rangle,
\langle C_2,C_3\rangle,
\langle C_3,C_2\rangle
\right),
$$

independently derived typed vector 是

$$
\boxed{
\mathbf C_{\rm typed}
=
\lambda_1
\left(
1,\,
1,\,
-i\sqrt2,\,
+i\sqrt2
\right).
}
$$

因此

$$
\mathbf C_{\rm typed}
\in
\mathbb C
\left(
1,1,-i\sqrt2,+i\sqrt2
\right),
$$

with scalar exactly

$$
\boxed{\lambda_1}.
$$

No fitted factor、no free $\chi$、no HT normalization。
