---
schema: 1
artifact_kind: mechanically_generated_visible_transcript
generated_from: authenticated-visible.json
generated_from_sha256: 0eba2b4e454b9ffe97f139b28bd94efc01643f55460dde6792fd05e2fcbcac7f
source_kind: AUTHENTICATED_CONVERSATION
source_url: https://chatgpt.com/c/6a51b2b1-5870-83e8-ad8f-b1f8496be0fc
captured_url: https://chatgpt.com/c/6a51b2b1-5870-83e8-ad8f-b1f8496be0fc
acquired_at: 2026-07-12T20:07:20.076Z
acquisition_boundary: VISIBLE_DOM_ONLY_NO_HIDDEN_REASONING
body_field: text_with_tex
interpretation_status: NOT_PERFORMED
translation_status: NOT_PERFORMED
---

# Authenticated visible conversation transcript

## Message 1 — user

- message_id: `0b973267-f5e1-4a08-bd5c-548b91c646ea`
- conversation_turn: `conversation-turn-1`
- authenticated_order: `0`
- content_sha256_without_capture_order: `02428ee89da008985daf1bad6666a3e4362820409b904cc00f5f4cfa195f2620`

<!-- BEGIN EXACT text_with_tex -->

计算\nabla_-(\nabla_+ W_+^A \nabla_+ W_+^B)的1-loop result in Euclidean 4d N=1 SYM.
(classically, it is zero,but at one loop, it will be non zero)
introduce two interacting vertexes,form a triangular diagram, and use dimensional reduction regularization
First build the notation
do not claim and copy from any other result (especially do not see my notion and memory about calculating the same object)

<!-- END EXACT text_with_tex -->

## Message 2 — assistant

- message_id: `7af98f88-eda4-426f-b85d-eece9477a4af`
- conversation_turn: `conversation-turn-2`
- authenticated_order: `1`
- content_sha256_without_capture_order: `ae54e7509dfd4f00b37b3fc1c63a18db4069e58b2aa9208e8b477b233cffccaf`

<!-- BEGIN EXACT text_with_tex -->

1. Notation / conventions

Euclidean rotation group：

$$
\mathrm{Spin}(4)=SU(2)_L\times SU(2)_R,
\qquad
\alpha,\beta=\pm ,
\qquad
\dot\alpha,\dot\beta=\dot\pm .
$$

Spinor metric：

$$
\epsilon^{+-}=\epsilon^{\dot+\dot-}=1,
\qquad
\epsilon_{+-}=\epsilon_{\dot+\dot-}=-1,
$$

$$
\psi^\alpha=\epsilon^{\alpha\beta}\psi_\beta,
\qquad
\bar\psi^{\dot\alpha}
=\epsilon^{\dot\alpha\dot\beta}\bar\psi_{\dot\beta}.
$$

因此

$$
\nabla^+=\nabla_-,
\qquad
\nabla^-=-\nabla_+ .
$$

Gauge generators 取 Hermitian convention：

$$
[T^A,T^B]=if^{ABC}T^C,
\qquad
\operatorname{tr}(T^AT^B)=\frac12\delta^{AB},
$$

$$
f^{ACD}f^{BCD}=C_A\delta^{AB}.
$$

Superspace algebra：

$$
\{\nabla_\alpha,\nabla_\beta\}=0,
\qquad
\{\bar\nabla_{\dot\alpha},\bar\nabla_{\dot\beta}\}=0,
$$

$$
\{\nabla_\alpha,\bar\nabla_{\dot\alpha}\}
=-2i\nabla_{\alpha\dot\alpha}.
$$

定义 vector derivative

$$
\nabla_{\alpha\dot\alpha}
=\sigma^\mu_{\alpha\dot\alpha}\nabla_\mu,
\qquad
\nabla_+{}^{\dot\alpha}
=\epsilon^{\dot\alpha\dot\beta}\nabla_{+\dot\beta}.
$$

Chirality 与 Bianchi identity：

$$
\bar\nabla_{\dot\alpha}W_\beta=0,
\qquad
\nabla_\alpha\bar W_{\dot\beta}=0,
$$

$$
\nabla^\alpha W_\alpha
=
\bar\nabla_{\dot\alpha}\bar W^{\dot\alpha}.
$$

引入

$$
X^A\equiv(\nabla_+W_+)^A,
\qquad
\mathcal E^A\equiv(\nabla^\alpha W_\alpha)^A.
$$

其中

$$
|W_\alpha|=|\bar W_{\dot\alpha}|=1,
\qquad
|X|=0.
$$

Canonically normalized vector superfield

$$
W_\alpha
=
-\frac{1}{8g_0}\bar D^2
\left(e^{-2g_0V}D_\alpha e^{2g_0V}\right),
$$

$$
\bar W_{\dot\alpha}
=
\frac{1}{8g_0}D^2
\left(e^{2g_0V}\bar D_{\dot\alpha}e^{-2g_0V}\right),
$$

$$
S_E
=
\frac12\int d^dx\,d^2\theta\,
\operatorname{tr}(W^\alpha W_\alpha)
+
\frac12\int d^dx\,d^2\bar\theta\,
\operatorname{tr}(\bar W_{\dot\alpha}\bar W^{\dot\alpha})
+S_{\rm gf}+S_{\rm gh}.
$$

Euclidean theory 中 $W_\alpha$ 与 $\bar W_{\dot\alpha}$ 作为 independent superfields。

DRED

$$
d=4-2\epsilon,
\qquad
g_0=\mu^\epsilon g,
$$

$$
g_{\mu\nu}^{(4)}
=
\widehat g_{\mu\nu}
+
\widetilde g_{\mu\nu},
$$

$$
\widehat g^\mu{}_\mu=d,
\qquad
\widetilde g^\mu{}_\mu=4-d=2\epsilon.
$$

Loop momentum 属于 $\widehat g$-subspace，而 spin/gauge algebra 保留 quasi-four-dimensional structure。下面只使用 Clifford/projector identities，不使用 four-dimensional Fierz identities；这是 consistent DRED 所要求的处理。ar5iv+1

$$
[X^AX^B]_{\overline{\rm DR}}
$$

表示 adjoint point-split、parallel-transported composite operator，减去 $\overline{\rm DR}$ poles，并且不加入额外 finite local counterterm。

2. Classical result

由

$$
\mathcal E
=
\nabla^\alpha W_\alpha
=
\nabla_-W_+-\nabla_+W_-,
$$

得到

$$
\nabla_-W_+
=
\mathcal E+\nabla_+W_-.
$$

于是

$$
\begin{aligned}
\nabla_-X
&=
\nabla_-\nabla_+W_+
\\
&=
-\nabla_+\nabla_-W_+
\\
&=
-\nabla_+\left(\mathcal E+\nabla_+W_-\right)
\\
&=
-\nabla_+\mathcal E-\nabla_+^2W_-
\\
&=
-\nabla_+\mathcal E .
\end{aligned}
$$

由于 $X$ 是 Grassmann-even，

$$
\begin{aligned}
\nabla_-(X^AX^B)
&=
(\nabla_-X^A)X^B
+
X^A(\nabla_-X^B)
\\
&=
-(\nabla_+\mathcal E^A)X^B
-
X^A(\nabla_+\mathcal E^B).
\end{aligned}
$$

因此 classical on-shell：

$$
\boxed{
\left.\nabla_-(X^AX^B)\right|_{\mathcal E=0}=0
}.
$$

3. Cubic interaction vertices

使用 Baker–Campbell–Hausdorff expansion：

$$
\begin{aligned}
e^{-2g_0V}D_\alpha e^{2g_0V}
&=
2g_0D_\alpha V
+\frac12[2g_0D_\alpha V,2g_0V]
+\cdots
\\
&=
2g_0D_\alpha V
+
2g_0^2[D_\alpha V,V]
+\cdots .
\end{aligned}
$$

所以

$$
W_\alpha
=
W_\alpha^{(1)}+W_\alpha^{(2)}+\cdots ,
$$

$$
W_\alpha^{(1)}
=
-\frac14\bar D^2D_\alpha V,
$$

$$
\begin{aligned}
W_\alpha^{(2)}
&=
-\frac{g_0}{4}\bar D^2[D_\alpha V,V]
\\
&=
\frac{g_0}{4}\bar D^2[V,D_\alpha V].
\end{aligned}
$$

利用

$$
\int d^2\theta\,A\,\bar D^2B
=
-4\int d^4\theta\,AB,
$$

以及

$$
\operatorname{tr}\left(T^A[T^B,T^C]\right)
=
\frac{i}{2}f^{BCA},
$$

chiral cubic vertex 为

$$
\boxed{
S_{3,c}
=
\frac{ig_0}{8}f^{ABC}
\int d^dx\,d^4\theta\,
(\bar D^2D^\alpha V^A)V^B D_\alpha V^C
}.
$$

同理，

$$
e^{2g_0V}\bar D_{\dot\alpha}e^{-2g_0V}
=
-2g_0\bar D_{\dot\alpha}V
-
2g_0^2[V,\bar D_{\dot\alpha}V]
+\cdots ,
$$

得到 anti-chiral vertex

$$
\boxed{
S_{3,\bar c}
=
-\frac{ig_0}{8}f^{ABC}
\int d^dx\,d^4\theta\,
(D^2\bar D_{\dot\alpha}V^A)V^B\bar D^{\dot\alpha}V^C
}.
$$

Background Feynman gauge propagator：

$$
\boxed{
\langle
V^A(k,\theta_1)V^B(-k,\theta_2)
\rangle_0
=
\frac{\delta^{AB}}{k^2}
\delta^4(\theta_1-\theta_2)
}.
$$

Composite insertion 的 linearized leg：

$$
\boxed{
X^{A(1)}
=
-\frac14D_+\bar D^2D_+V^A
}.
$$

Interaction expansion：

$$
\frac12
\left(S_{3,c}+S_{3,\bar c}\right)^2
\supset
S_{3,c}S_{3,\bar c},
$$

因为

$$
\frac12\left(
S_{3,c}S_{3,\bar c}
+
S_{3,\bar c}S_{3,c}
\right)
=
S_{3,c}S_{3,\bar c}.
$$

两个 insertion legs 分别连接两个 cubic vertices；vertices 之间有第三条 propagator，剩余两条 legs 给出 external $\bar W^D_{\dot\alpha}$ 和 $X^E$。

Color factor：

$$
( if^{ACD})(-if^{BCE})
=
f^{ACD}f^{BCE}.
$$

4. Triangle $D$-algebra

取 external momenta：

$$
\bar W^D(p),\qquad X^E(q),
\qquad
P=p+q.
$$

Loop denominator：

$$
\Delta_\triangle
=
k^2(k+p)^2(k-q)^2.
$$

Momentum-space superspace identity：

$$
D_\alpha\bar D_{\dot\alpha}
=
-\bar D_{\dot\alpha}D_\alpha
+
2k_{\alpha\dot\alpha},
$$

以及

$$
D^2\bar D^2D^2
=
16k^2D^2,
\qquad
\bar D^2D^2\bar D^2
=
16k^2\bar D^2.
$$

完成所有 internal $\theta$-integrals 后，含一个 external vector momentum $r_\nu$ 的 non-EOM terms 只有两条 derivative chains：

$$
\mathcal N^{(a)}_{+\dot\alpha}(k;r)
=
\frac{k^2}{2}
\left(
\widehat\sigma^\mu
\bar\sigma^\nu
\widehat\sigma_\mu
\right)_{+\dot\alpha}r_\nu ,
$$

$$
\mathcal N^{(b)}_{+\dot\alpha}(k;r)
=
k^2(\sigma^\nu)_{+\dot\alpha}r_\nu .
$$

第一项来自 three-$\sigma$ chain，第二项来自

$$
D^2\bar D^2D^2
$$

collapse。其余 terms 含有

$$
\bar\nabla_{\dot\alpha}W_\beta,
\qquad
\nabla_\alpha\bar W_{\dot\beta},
\qquad
\nabla_+^2,
\qquad
\nabla_+\mathcal E,
$$

分别由 chirality、nilpotency 或 EOM 消失。

总 numerator：

$$
\mathcal N_{+\dot\alpha}
=
\frac{k^2}{2}
\left[
\widehat\sigma^\mu\bar\sigma^\nu\widehat\sigma_\mu
+
2\sigma^\nu
\right]_{+\dot\alpha}r_\nu .
$$

现在严格计算 DRED spinor contraction：

$$
\begin{aligned}
\widehat\sigma^\mu
\bar\sigma^\nu
\widehat\sigma_\mu
&=
\widehat\sigma^\mu
\left(
2\widehat g^\nu{}_\mu
-
\bar\sigma_\mu\sigma^\nu
\right)
\\
&=
2\widehat\sigma^\nu
-
\left(
\widehat\sigma^\mu\bar\sigma_\mu
\right)\sigma^\nu
\\
&=
2\sigma^\nu
-
d\,\sigma^\nu
\\
&=
(2-d)\sigma^\nu .
\end{aligned}
$$

因此

$$
\begin{aligned}
\mathcal N_{+\dot\alpha}
&=
\frac{k^2}{2}
\left[(2-d)+2\right]
(\sigma^\nu)_{+\dot\alpha}r_\nu
\\
&=
\frac{4-d}{2}
k^2r_{+\dot\alpha}
\\
&=
\epsilon k^2r_{+\dot\alpha}.
\end{aligned}
$$

这正是 evanescent numerator：

$$
\boxed{
\mathcal N_{+\dot\alpha}
=
\epsilon k^2r_{+\dot\alpha}
}.
$$

在严格 $d=4$ 时，

$$
\mathcal N_{+\dot\alpha}=0,
$$

但在 DRED 中该 $\epsilon$ 将乘以 logarithmic UV pole。

5. Triangle integral

第一种 external-leg assignment 给出

$$
\begin{aligned}
\mathcal A_I^{AB}(p,q)
&=
g_0^2f^{ACD}f^{BCE}
\int\frac{d^dk}{(2\pi)^d}
\frac{
\epsilon k^2
}{
k^2(k+p)^2(k-q)^2
}
\\
&\qquad\qquad\times
\bar W^D_{\dot\alpha}(p)
\left(iq_+{}^{\dot\alpha}\right)
X^E(q).
\end{aligned}
$$

消去 $k^2$，令

$$
\ell=k+p,
\qquad
P=p+q,
$$

则

$$
(k-q)^2=(\ell-P)^2.
$$

使用 $g_0^2=\mu^{2\epsilon}g^2$：

$$
\mathcal A_I^{AB}
=
g^2f^{ACD}f^{BCE}
\epsilon J(P^2)
\bar W^D_{\dot\alpha}(p)
\left(iq_+{}^{\dot\alpha}\right)
X^E(q),
$$

其中

$$
J(P^2)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{\ell^2(\ell-P)^2}.
$$

Feynman parameter：

$$
\frac1{\ell^2(\ell-P)^2}
=
\int_0^1dx\,
\frac1{
\left[
(\ell-(1-x)P)^2+x(1-x)P^2
\right]^2
}.
$$

令

$$
L=\ell-(1-x)P,
\qquad
\Delta=x(1-x)P^2.
$$

于是

$$
J(P^2)
=
\mu^{2\epsilon}
\int_0^1dx
\int\frac{d^dL}{(2\pi)^d}
\frac1{(L^2+\Delta)^2}.
$$

Euclidean integral：

$$
\int\frac{d^dL}{(2\pi)^d}
\frac1{(L^2+\Delta)^2}
=
\frac1{(4\pi)^{d/2}}
\Gamma\left(2-\frac d2\right)
\Delta^{d/2-2}.
$$

代入

$$
d=4-2\epsilon,
\qquad
2-\frac d2=\epsilon,
\qquad
\frac d2-2=-\epsilon,
$$

得到

$$
J(P^2)
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)
(P^2)^{-\epsilon}
\int_0^1dx\,
[x(1-x)]^{-\epsilon}.
$$

Beta integral：

$$
\int_0^1dx\,
x^{-\epsilon}(1-x)^{-\epsilon}
=
\frac{\Gamma(1-\epsilon)^2}
{\Gamma(2-2\epsilon)}.
$$

因此

$$
\boxed{
J(P^2)
=
\frac1{16\pi^2}
\left(
\frac{4\pi\mu^2}{P^2}
\right)^\epsilon
\Gamma(\epsilon)
\frac{\Gamma(1-\epsilon)^2}
{\Gamma(2-2\epsilon)}
}.
$$

现在取 finite limit：

$$
\epsilon\Gamma(\epsilon)
=
\Gamma(1+\epsilon),
$$

所以

$$
\begin{aligned}
\lim_{\epsilon\rightarrow0}\epsilon J(P^2)
&=
\frac1{16\pi^2}
\lim_{\epsilon\rightarrow0}
\left[
\left(
\frac{4\pi\mu^2}{P^2}
\right)^\epsilon
\Gamma(1+\epsilon)
\frac{\Gamma(1-\epsilon)^2}
{\Gamma(2-2\epsilon)}
\right]
\\
&=
\boxed{\frac1{16\pi^2}}.
\end{aligned}
$$

故

$$
\boxed{
\mathcal A_I^{AB}(p,q)
=
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\bar W^D_{\dot\alpha}(p)
\left(iq_+{}^{\dot\alpha}\right)
X^E(q)
}.
$$

第二种 assignment：

$$
\boxed{
\mathcal A_{II}^{AB}(p,q)
=
-\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\left(ip_{+\dot\alpha}\right)
X^D(p)\,
\bar W^{E\dot\alpha}(q)
}.
$$

6. Position-space one-loop result

恢复 gauge-covariant derivatives：

$$
\boxed{
\begin{aligned}
\left.
\nabla_-
[X^AX^B]_{\overline{\rm DR}}
\right|_{\text{1-loop},\,\mathcal E=0}
&=
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\\
&\quad\times
\left[
\bar W^D_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^E
-
(\nabla_{+\dot\alpha}X^D)
\bar W^{E\dot\alpha}
\right].
\end{aligned}
}
$$

即

$$
\boxed{
\begin{aligned}
&
\left.
\nabla_-
\left[
(\nabla_+W_+)^A
(\nabla_+W_+)^B
\right]_{\overline{\rm DR}}
\right|_{\text{1-loop},\,\mathcal E=0}
\\[2mm]
&\qquad=
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\Big[
\bar W^D_{\dot\alpha}
\nabla_+{}^{\dot\alpha}
(\nabla_+W_+)^E
\\
&\hspace{62mm}
-
\nabla_{+\dot\alpha}
(\nabla_+W_+)^D\,
\bar W^{E\dot\alpha}
\Big].
\end{aligned}
}
$$

利用

$$
\begin{aligned}
(\nabla_{+\dot\alpha}X^D)\bar W^{E\dot\alpha}
&=
(\nabla_{+\dot\alpha}X^D)
\epsilon^{\dot\alpha\dot\beta}
\bar W^E_{\dot\beta}
\\
&=
-\bar W^E_{\dot\beta}
\epsilon^{\dot\beta\dot\alpha}
\nabla_{+\dot\alpha}X^D
\\
&=
-\bar W^E_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^D ,
\end{aligned}
$$

也可写成 manifestly $D\leftrightarrow E$ symmetric form：

$$
\boxed{
\begin{aligned}
\left.
\nabla_-[X^AX^B]_{\overline{\rm DR}}
\right|_{\text{1-loop},\,\mathcal E=0}
&=
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\\
&\quad\times
\left[
\bar W^D_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^E
+
\bar W^E_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^D
\right].
\end{aligned}
}
$$

包含 classical EOM term 的完整 tree + one-loop operator equation 是

$$
\boxed{
\begin{aligned}
\nabla_-[X^AX^B]_{\overline{\rm DR}}
={}&
-(\nabla_+\mathcal E^A)X^B
-
X^A(\nabla_+\mathcal E^B)
\\
&+
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\left[
\bar W^D_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^E
-
(\nabla_{+\dot\alpha}X^D)
\bar W^{E\dot\alpha}
\right].
\end{aligned}
}
$$

7. Gauge-invariant trace

定义

$$
\mathcal O_2
=
\operatorname{tr}(X^2)
=
\frac12\delta^{AB}X^AX^B.
$$

使用

$$
\delta^{AB}f^{ACD}f^{BCE}
=
C_A\delta^{DE},
$$

以及

$$
\bar W^D_{\dot\alpha}\nabla_+{}^{\dot\alpha}X^D
-
(\nabla_{+\dot\alpha}X^D)\bar W^{D\dot\alpha}
=
2\bar W^D_{\dot\alpha}\nabla_+{}^{\dot\alpha}X^D,
$$

得到

$$
\boxed{
\left.
\nabla_-
\operatorname{tr}
\left[(\nabla_+W_+)^2\right]_{\overline{\rm DR}}
\right|_{\text{1-loop},\,\mathcal E=0}
=
\frac{g^2C_A}{16\pi^2}
\bar W^A_{\dot\alpha}
\nabla_+{}^{\dot\alpha}
(\nabla_+W_+)^A
}.
$$

关键 finite mechanism 为

$$
\boxed{
\frac{4-d}{2}\times
\left(\frac1{\epsilon}\right)
=
\epsilon\times\left(\frac1{\epsilon}\right)
=1
},
$$

即 four-dimensional cancellation 在 DRED 中留下一个 finite local anomaly。

<!-- END EXACT text_with_tex -->

## Message 3 — assistant

- message_id: `85f1987d-2b98-4202-b4ad-c35ae39a41ee`
- conversation_turn: `conversation-turn-8`
- authenticated_order: `2`
- content_sha256_without_capture_order: `64dbcb1d4821cf4858c1c84c277f8025303c212a83ca9268caea3891761d8f24`

<!-- BEGIN EXACT text_with_tex -->

0. Notation 与计算对象

$$
d=4-2\epsilon ,
\qquad
\frac1{\bar\epsilon}
\equiv
\frac1\epsilon-\gamma_E+\ln4\pi .
$$

$$
g_{(4)}^{\mu\nu}
=
\widehat g^{\mu\nu}
+
\widetilde g^{\mu\nu},
$$

$$
\widehat g^\mu{}_\mu=d,
\qquad
\widetilde g^\mu{}_\mu=4-d=2\epsilon .
$$

Loop momentum 满足

$$
k^\mu=\widehat g^\mu{}_\nu k^\nu,
\qquad
\widetilde g^\mu{}_\nu k^\nu=0.
$$

Spinor algebra 始终 four-dimensional：

$$
\sigma^\mu\bar\sigma^\nu+\sigma^\nu\bar\sigma^\mu
=
2g_{(4)}^{\mu\nu}.
$$

定义

$$
X^A=(\nabla_+W_+)^A,
$$

以及 three-$\sigma$ tensor

$$
T_{\mu\rho\nu,+}{}^{\dot\alpha}
\equiv
(\sigma_\mu\bar\sigma_\rho\sigma_\nu)_+{}^{\dot\alpha}.
$$

我们计算固定 color orientation 的 amputated form factor：

$$
\Gamma^{AB;DE}_{\dot\alpha}(p,q)
=
\left\langle
\bar W^D_{\dot\alpha}(q)\,
X^E(p)\,
\nabla_-
\right\rangle_{\rm 1PI},
$$

$$
P=p+q,
\qquad
p^2,q^2,P^2>0,
$$

从而避免 IR poles。

1. 你的判断是正确的

我上一版写出的 tensor combination

$$
g_{(4)}^{\mu\nu}
\int\frac{d^d\ell}{(\ell^2+\Delta)^2}
-
4
\int\frac{d^d\ell\,\ell^\mu\ell^\nu}
{(\ell^2+\Delta)^3}
$$

不是 triangle graph 本身。

正确分类是

$$
\boxed{
\text{triangle three-denominator part}
\;+\;
\text{letter/contact two-denominator parts}.
}
$$

Triangle 单独具有 ordinary UV divergence：

$$
\boxed{
\Gamma_\triangle\Big|_{\rm UV}
\neq 0.
}
$$

不能在 triangle numerator 中预先写入一个 $\epsilon$。正确顺序是

$$
\boxed{
\begin{aligned}
&\text{先分别计算 triangle 和 bubble/contact 的 }1/\epsilon\text{ poles},
\\
&\text{再相消 physical }\widehat g^{\mu\nu}\text{ part},
\\
&\text{最后剩下 }
g_{(4)}^{\mu\nu}-\widehat g^{\mu\nu}
=
\widetilde g^{\mu\nu}.
\end{aligned}
}
$$

所以我撤回上一版“triangle numerator 已经等于 $\epsilon k^2p$”的说法。

2. Bare operator 与 action 的完整 $g$-expansion

采用

$$
W_\alpha
=
-\frac1{8g}\bar D^2
\left(
e^{-2gV}D_\alpha e^{2gV}
\right).
$$

Baker–Campbell–Hausdorff expansion：

$$
\begin{aligned}
e^{-2gV}D_\alpha e^{2gV}
={}&
2gD_\alpha V
+
2g^2[D_\alpha V,V]
\\
&+
\frac43g^3[[D_\alpha V,V],V]
+
O(g^4).
\end{aligned}
$$

写成

$$
W_\alpha
=
W_{(1)\alpha}
+
gW_{(2)\alpha}
+
g^2W_{(3)\alpha}
+
O(g^3),
$$

则

$$
W_{(1)\alpha}
=
-\frac14\bar D^2D_\alpha V,
$$

$$
W_{(2)\alpha}
=
-\frac14\bar D^2[D_\alpha V,V],
$$

$$
W_{(3)\alpha}
=
-\frac16\bar D^2[[D_\alpha V,V],V].
$$

Spinor connection 为

$$
\Gamma_\alpha
=
e^{-2gV}D_\alpha e^{2gV}
=
2gD_\alpha V
+
2g^2[D_\alpha V,V]
+
O(g^3).
$$

于是

$$
X=\nabla_+W_+
=
D_+W_+
+
[\Gamma_+,W_+]
$$

可展开为

$$
X=X_{(1)}+gX_{(2)}+O(g^2),
$$

$$
\boxed{
X_{(1)}
=
-\frac14D_+\bar D^2D_+V
\equiv K_+V
}
$$

以及

$$
\boxed{
\begin{aligned}
X_{(2)}
={}&
-\frac14D_+\bar D^2[D_+V,V]
\\
&-
\frac12[D_+V,\bar D^2D_+V].
\end{aligned}
}
$$

外层 covariant derivative：

$$
\nabla_-Y
=
D_-Y+[\Gamma_-,Y],
$$

$$
\Gamma_-^{(1)}=2gD_-V.
$$

因此

$$
\mathscr I^{AB}
\equiv
\nabla_-(X^AX^B)
=
\mathscr I_{(2)}^{AB}
+
g\mathscr I_{(3)}^{AB}
+
g^2\mathscr I_{(4)}^{AB}
+\cdots ,
$$

其中

$$
\boxed{
\mathscr I_{(2)}^{AB}
=
D_-\left(X_{(1)}^AX_{(1)}^B\right)
}
$$

并且

$$
\boxed{
\begin{aligned}
\mathscr I_{(3)}^{AB}
={}&
D_-
\left(
X_{(1)}^AX_{(2)}^B
+
X_{(2)}^AX_{(1)}^B
\right)
\\
&+
2[D_-V,X_{(1)}]^A X_{(1)}^B
\\
&+
2X_{(1)}^A[D_-V,X_{(1)}]^B .
\end{aligned}
}
$$

这就是此前缺失的 letter interaction insertion。

Action expansion

写成

$$
S=S_{(2)}+gS_{(3)}+g^2S_{(4)}+\cdots .
$$

Cubic vertices：

$$
S_{(3),c}
=
\frac{i}{8}f^{ABC}
\int d^dx\,d^4\theta\,
(\bar D^2D^\alpha V^A)V^B D_\alpha V^C,
$$

$$
S_{(3),\bar c}
=
-\frac{i}{8}f^{ABC}
\int d^dx\,d^4\theta\,
(D^2\bar D_{\dot\alpha}V^A)
V^B\bar D^{\dot\alpha}V^C.
$$

Quartic action 可以无歧义地写为

$$
\boxed{
S_{(4),c}
=
\int d^dx\,d^2\theta\,
\operatorname{tr}
\left(
W_{(1)}^\alpha W_{(3)\alpha}
+
\frac12W_{(2)}^\alpha W_{(2)\alpha}
\right)
}
$$

以及 anti-chiral conjugate。

3. One-loop 必须包含的完整 graph set

由

$$
e^{-S_{\rm int}}
=
1-gS_{(3)}
+
g^2\left(
\frac12S_{(3)}^2-S_{(4)}
\right)
+
O(g^3),
$$

order-$g^2$ two-external-field amplitude 为

$$
\boxed{
\begin{aligned}
\Gamma^{(1)}
={}&
\frac12
\left\langle
\mathscr I_{(2)}S_{(3)}^2
\right\rangle_{0,c}
\\
&-
\left\langle
\mathscr I_{(3)}S_{(3)}
\right\rangle_{0,c}
\\
&-
\left\langle
\mathscr I_{(2)}S_{(4)}
\right\rangle_{0,c}
\\
&+
\left\langle
\mathscr I_{(4)}
\right\rangle_{0,c}
+
\Gamma_{\rm wf/ct}.
\end{aligned}
}
$$

它们对应：

contributiontopologydenominator
$\frac12\langle\mathscr I_{(2)}S_{(3)}^2\rangle$triangle$D_0D_1D_2$
$-\langle\mathscr I_{(3)}S_{(3)}\rangle$nonlinear-letter bubble$D_0D_1$
$-\langle\mathscr I_{(2)}S_{(4)}\rangle$quartic/contact bubble$D_0D_1$
collapsed terms from triangle $D$-algebralower bubble$D_0D_1$
$\langle\mathscr I_{(4)}\rangle$tadpolescaleless
$\Gamma_{\rm wf/ct}$letter self-energy or $Z_X$scheme-dependent representation

在 DRED 中，最后的 massless tadpole 满足

$$
\int\frac{d^dk}{(2\pi)^d}(k^2)^n=0,
$$

所以

$$
\left\langle\mathscr I_{(4)}\right\rangle_{0,c}=0.
$$

如果计算 renormalized amputated 1PI vertex，则 external self-energy bubble 由 $Z_X$ 表示；不能同时再加入同一 external bubble，否则 double counting。

4. Triangle graph：完整 momentum routing

固定 orientation：

                         color C
                     momentum k+q
          \bar W^D(q) ●──────────────● W^E(p)
                      ╲              ╱
                       ╲            ╱
          color A       ╲          ╱       color B
          momentum k     ╲        ╱        momentum k+P
                          ●
                 insertion I_(2)^{AB}

定义

$$
r_0=k,
\qquad
r_1=k+q,
\qquad
r_2=k+P,
\qquad
P=p+q.
$$

三条 propagators：

$$
G_0(r_i;\theta_a,\theta_b)
=
\frac{\delta^4(\theta_a-\theta_b)}{r_i^2}.
$$

所以

$$
D_0=k^2,
\qquad
D_1=(k+q)^2,
\qquad
D_2=(k+P)^2.
$$

Triangle denominator 必然为

$$
\boxed{
\frac1{D_0D_1D_2}
=
\frac1{k^2(k+q)^2(k+P)^2}.
}
$$

4.1 Background-field cubic Feynman rules

从 $S_{(3)}$ amputate 一个 external field-strength leg，得到

$$
\boxed{
\mathcal V_W^{E;BC}
=
-\frac{ig}{2}
f^{BCE}
W^{E\alpha}
\left(
D_\alpha^{(C)}-D_\alpha^{(B)}
\right)
}
$$

以及

$$
\boxed{
\mathcal V_{\bar W}^{D;AC}
=
\frac{ig}{2}
f^{ACD}
\bar W^D_{\dot\alpha}
\left(
\bar D^{\dot\alpha(C)}
-
\bar D^{\dot\alpha(A)}
\right).
}
$$

Color factor：

$$
\boxed{
f^{ACD}f^{BCE}.
}
$$

在 $\bar W$-vertex，两个 incoming internal momenta 是

$$
r_0=k,
\qquad
-r_1=-(k+q).
$$

Derivative difference 因此产生

$$
L_1^\mu
=
r_0^\mu+r_1^\mu
=
2k^\mu+q^\mu.
$$

在 $W$-vertex，两个 incoming momenta 是

$$
r_1=k+q,
\qquad
-r_2=-(k+P),
$$

所以

$$
L_2^\nu
=
r_1^\nu+r_2^\nu
=
2k^\nu+q^\nu+P^\nu
=
2k^\nu+2q^\nu+p^\nu.
$$

5. Triangle 的 $D$-algebra

定义

$$
K_+=-\frac14D_+\bar D^2D_+.
$$

固定 $D_-$ 作用在 $A$-letter：

$$
D_-K_+
=
-\frac14D_-D_+\bar D^2D_+
=
-\frac18D^2\bar D^2D_+.
$$

使用

$$
D_i\delta_{ij}=-D_j\delta_{ij},
\qquad
\bar D_i\delta_{ij}=-\bar D_j\delta_{ij}.
$$

只保留最终 external tensor

$$
\bar W^D_{\dot\alpha}(q)\,
p_\rho\,
X^E(p).
$$

所有 spinor derivatives 移到 outer layer 后，相关 closed $D$-chain 可写为

$$
\boxed{
\begin{aligned}
\mathscr D_\triangle^{\dot\alpha}
={}&
\frac1{32}
\left[
D^2\bar D^2\delta^4(\theta)
\right]_{\theta=0}
\\
&\times
\left\{
-D_+,
\bar{\mathscr D}_{\bar W}^{\dot\beta}
\right\}
p_\gamma{}_{\dot\beta}
\left\{
\mathscr D_W^\gamma,
-\bar D^{\dot\alpha}
\right\}.
\end{aligned}
}
$$

这里

$$
p_{\gamma\dot\beta}
\equiv
-\frac12
\left\{
D_\gamma,\bar D_{\dot\beta}
\right\}_{\rm external}.
$$

Closed Grassmann loop：

$$
\left[
D^2\bar D^2\delta^4(\theta)
\right]_{\theta=0}
=
16.
$$

两个 internal mixed anticommutators：

$$
\left\{
-D_+,
\bar{\mathscr D}_{\bar W}^{\dot\beta}
\right\}
=
2(L_1)_+{}^{\dot\beta},
$$

$$
\left\{
\mathscr D_W^\gamma,
-\bar D^{\dot\alpha}
\right\}
=
2(L_2)^\gamma{}^{\dot\alpha}.
$$

因此

$$
\begin{aligned}
\mathscr D_\triangle^{\dot\alpha}
&=
\frac1{32}
\cdot16\cdot2\cdot2\,
(L_1)_+{}^{\dot\beta}
p_\gamma{}_{\dot\beta}
(L_2)^\gamma{}^{\dot\alpha}
\\
&=
2
(L_1)_+{}^{\dot\beta}
p_\gamma{}_{\dot\beta}
(L_2)^\gamma{}^{\dot\alpha}.
\end{aligned}
$$

利用

$$
(L_1)_+{}^{\dot\beta}
p_\gamma{}_{\dot\beta}
(L_2)^\gamma{}^{\dot\alpha}
=
T_{\mu\rho\nu,+}{}^{\dot\alpha}
L_1^\mu p^\rho L_2^\nu,
$$

以及 vertex product

$$
\left(-\frac{ig}{2}\right)
\left(\frac{ig}{2}\right)
=
\frac{g^2}{4},
$$

得到 three-denominator triangle：

$$
\boxed{
\begin{aligned}
\Gamma_{\triangle,3}^{A|B}
={}&
\frac{g^2}{2}
f^{ACD}f^{BCE}
\bar W^D_{\dot\alpha}(q)
p^\rho X^E(p)
\\
&\times
T_{\mu\rho\nu,+}{}^{\dot\alpha}
\int\frac{d^dk}{(2\pi)^d}
\frac{
L_1^\mu L_2^\nu
}{
D_0D_1D_2
}
\\
&+
\Gamma_{\triangle,\mathrm{coll}}
+
\Gamma_{\rm EOM}.
\end{aligned}
}
$$

这里：

$\Gamma_{\triangle,\mathrm{coll}}$：由 $D^2\bar D^2D^2=16\Box D^2$ cancel 一个 propagator 得到的 two-denominator terms；

$\Gamma_{\rm EOM}$：含 $D_+\mathcal E$、$D_\alpha\bar W_{\dot\alpha}$、$\bar D_{\dot\alpha}W_\alpha$ 的 terms。

这些 collapsed terms 不能丢掉。

6. Triangle 的完整 Feynman parameter integral

使用

$$
\frac1{D_0D_1D_2}
=
2
\int_{\substack{x,y,z\geq0\\x+y+z=1}}
dx\,dy\,dz\,
\frac1{(\ell^2+\Delta)^3},
$$

其中

$$
\ell=k+yq+zP,
$$

$$
\Delta
=
xy\,q^2+xz\,P^2+yz\,p^2.
$$

两个 numerator vectors：

$$
L_1=2k+q
=
2\ell+A,
$$

$$
L_2=2k+q+P
=
2\ell+B,
$$

其中

$$
A^\mu
=
(1-2y)q^\mu-2zP^\mu,
$$

$$
B^\nu
=
(1-2y)q^\nu+(1-2z)P^\nu.
$$

所以

$$
L_1^\mu L_2^\nu
=
4\ell^\mu\ell^\nu
+
2\ell^\mu B^\nu
+
2A^\mu\ell^\nu
+
A^\mu B^\nu.
$$

Odd integrals 为零：

$$
\int d^d\ell\,
\frac{\ell^\mu}{(\ell^2+\Delta)^3}
=
0.
$$

定义

$$
J_2(\Delta)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell^2+\Delta)^2},
$$

$$
I_3^{\mu\nu}(\Delta)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^\mu\ell^\nu}
{(\ell^2+\Delta)^3},
$$

$$
I_0(\Delta)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell^2+\Delta)^3}.
$$

于是

$$
\boxed{
\begin{aligned}
\int\frac{d^dk}{(2\pi)^d}
\frac{L_1^\mu L_2^\nu}{D_0D_1D_2}
=
2\int_\triangle
\left[
4I_3^{\mu\nu}(\Delta)
+
A^\mu B^\nu I_0(\Delta)
\right].
\end{aligned}
}
$$

其中

$$
I_0(\Delta)
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\frac{\Gamma(1+\epsilon)}2
\Delta^{-1-\epsilon}.
$$

$I_0$ 没有 UV pole。Triangle 的全部 UV divergence 来自 $I_3^{\mu\nu}$。

6.1 Tensor reduction

由于 loop momentum 只在 $\widehat g$-subspace：

$$
I_3^{\mu\nu}
=
\frac{\widehat g^{\mu\nu}}d
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^2}{(\ell^2+\Delta)^3}.
$$

Integration by parts：

$$
0
=
\int d^d\ell\,
\frac{\partial}{\partial\ell^\lambda}
\left[
\frac{\ell^\lambda}{(\ell^2+\Delta)^2}
\right].
$$

展开：

$$
0
=
dJ_2(\Delta)
-
4
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^2}{(\ell^2+\Delta)^3}.
$$

所以

$$
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^2}{(\ell^2+\Delta)^3}
=
\frac d4J_2(\Delta),
$$

从而

$$
\boxed{
4I_3^{\mu\nu}(\Delta)
=
\widehat g^{\mu\nu}J_2(\Delta).
}
$$

并且

$$
J_2(\Delta)
=
\frac1{16\pi^2}
\left[
\frac1{\bar\epsilon}
+
\ln\frac{\mu^2}{\Delta}
\right]
+
O(\epsilon).
$$

因为

$$
2\int_\triangle dx\,dy\,dz\,\delta(1-x-y-z)=1,
$$

triangle 的 pole 为

$$
\boxed{
\begin{aligned}
\left[
\Gamma_{\triangle,3}^{A|B}
\right]_{\rm pole}
={}&
\frac{g^2}{32\pi^2\bar\epsilon}
f^{ACD}f^{BCE}
\\
&\times
\bar W^D_{\dot\alpha}
p^\rho X^E
T_{\mu\rho\nu,+}{}^{\dot\alpha}
\widehat g^{\mu\nu}.
\end{aligned}
}
$$

这就是此前缺失的 ordinary UV divergence。

7. Letter interaction 与 lower bubble

在 ordinary prepotential expansion 中，所有 two-denominator terms 来自：

$$
-\left\langle\mathscr I_{(3)}S_{(3)}\right\rangle,
$$

$$
-\left\langle\mathscr I_{(2)}S_{(4)}\right\rangle,
$$

以及 triangle $D$-algebra 中由

$$
D^2\bar D^2D^2=16\Box D^2
$$

cancel 一个 propagator 的 terms。

这些 terms 的单独划分依赖 integration by parts 与 vertex symmetrization；但它们的 sum 是唯一的 background-covariant contact kernel。

在固定 orientation 中，这个 kernel 可整理为

$$
\boxed{
\mathscr I_{\rm contact}^{A|B}
=
g f^{BCE}X^E
\left[
(D_-K_+V^A)V^C
-
(K_+V^A)D_-V^C
\right]
+
\mathscr I_{\rm EOM}.
}
$$

它与 $\bar W$-vertex 形成 bubble：

               \bar W^D(q)
                    ●
                   ╱ ╲
                  ╱   ╲
                 ╲     ╱
                  ╲   ╱
                    ●
        contact insertion containing X^E(p)

Denominator：

$$
\boxed{
\frac1{k^2(k+Q)^2},
}
$$

其中固定 orientation 可取 $Q=q$。其 UV pole 与具体 $Q$ 无关。

7.1 Contact bubble 的 $D$-algebra

Derivative-difference structure 为

$$
(D_-^{(A)}-D_-^{(C)})
K_+
(\bar D^{\dot\alpha(C)}-\bar D^{\dot\alpha(A)}).
$$

作用在两条 propagator delta-functions 上：

$$
D^{(C)}\delta_{AC}=-D^{(A)}\delta_{AC},
$$

$$
\bar D^{(C)}\delta_{AC}
=
-\bar D^{(A)}\delta_{AC}.
$$

因此

$$
D_-^{(A)}-D_-^{(C)}
=
2D_-^{(A)},
$$

$$
\bar D^{\dot\alpha(C)}
-
\bar D^{\dot\alpha(A)}
=
-2\bar D^{\dot\alpha(A)}.
$$

插入 $K_+$：

$$
\begin{aligned}
&-\frac14
(2D_-)
D_+\bar D^2D_+
(-2\bar D^{\dot\alpha})
\\
&=
D_-D_+\bar D^2D_+\bar D^{\dot\alpha}
\\
&=
\frac12D^2\bar D^2D_+\bar D^{\dot\alpha}.
\end{aligned}
$$

对于 external $X$：

$$
D_+X=D_+^2W_+=0.
$$

因此

$$
D_+\bar D^{\dot\alpha}X
=
\{D_+,\bar D^{\dot\alpha}\}X
=
-2p_+{}^{\dot\alpha}X.
$$

所以 contact $D$-algebra 直接给出

$$
p_+{}^{\dot\alpha}X.
$$

为了与 triangle 使用同一 tensor basis，利用 four-dimensional identity

$$
g_{(4)}^{\mu\nu}
T_{\mu\rho\nu,+}{}^{\dot\alpha}
p^\rho
=
-2p_+{}^{\dot\alpha}.
$$

故 contact/bubble sum 为

$$
\boxed{
\begin{aligned}
\Gamma_{\rm contact}^{A|B}
={}&
-\frac{g^2}{2}
f^{ACD}f^{BCE}
\bar W^D_{\dot\alpha}
p^\rho X^E
\\
&\times
T_{\mu\rho\nu,+}{}^{\dot\alpha}
g_{(4)}^{\mu\nu}
B_0(Q^2)
+
\Gamma_{\rm EOM},
\end{aligned}
}
$$

其中

$$
B_0(Q^2)
=
\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}
\frac1{k^2(k+Q)^2}.
$$

Feynman parameter：

$$
B_0(Q^2)
=
\int_0^1du\,
J_2\!\left(u(1-u)Q^2\right).
$$

所以

$$
B_0(Q^2)
=
\frac1{16\pi^2}
\left[
\frac1{\bar\epsilon}
+
\ln\frac{\mu^2}{Q^2}
+
2
\right]
+
O(\epsilon).
$$

其 pole 为

$$
\boxed{
\begin{aligned}
\left[
\Gamma_{\rm contact}^{A|B}
\right]_{\rm pole}
={}&
-\frac{g^2}{32\pi^2\bar\epsilon}
f^{ACD}f^{BCE}
\\
&\times
\bar W^D_{\dot\alpha}
p^\rho X^E
T_{\mu\rho\nu,+}{}^{\dot\alpha}
g_{(4)}^{\mu\nu}.
\end{aligned}
}
$$

8. UV pole 的显式 cancellation

Triangle：

$$
\left[
\Gamma_{\triangle,3}
\right]_{\rm pole}
=
\frac{g^2}{32\pi^2\bar\epsilon}
ff\,
T_{\mu\rho\nu}
\widehat g^{\mu\nu}.
$$

Contact/bubble：

$$
\left[
\Gamma_{\rm contact}
\right]_{\rm pole}
=
-\frac{g^2}{32\pi^2\bar\epsilon}
ff\,
T_{\mu\rho\nu}
g_{(4)}^{\mu\nu}.
$$

相加：

$$
\boxed{
\begin{aligned}
\Gamma_{\triangle,3}
+
\Gamma_{\rm contact}
\Big|_{\rm local}
={}&
-\frac{g^2}{32\pi^2}
ff\,
T_{\mu\rho\nu}
\widetilde g^{\mu\nu}
\\
&\times
\left[
\frac1{\bar\epsilon}
+\text{finite scalar integrals}
\right].
\end{aligned}
}
$$

这里

$$
\widehat g^{\mu\nu}
-
g_{(4)}^{\mu\nu}
=
-\widetilde g^{\mu\nu}.
$$

Ordinary $\widehat g$-part 的 pole 完全相消：

$$
\boxed{
\left[
\Gamma_{\triangle,3}
+
\Gamma_{\rm contact}
\right]_{1/\epsilon,\;\widehat g}
=
0.
}
$$

9. 只有相消之后才出现 evanescent factor

严格 four-dimensional sigma identity：

$$
\sigma_\mu\bar\sigma_\rho\sigma_\nu
=
g_{(4)\mu\rho}\sigma_\nu
+
g_{(4)\rho\nu}\sigma_\mu
-
g_{(4)\mu\nu}\sigma_\rho
+
(\mu,\nu)\text{-antisymmetric}.
$$

由于 $\widetilde g^{\mu\nu}$ symmetric：

$$
\begin{aligned}
p^\rho
\widetilde g^{\mu\nu}
T_{\mu\rho\nu}
&=
p^\rho
\left[
2\widetilde g_\rho{}^\nu\sigma_\nu
-
\widetilde g^\mu{}_\mu\sigma_\rho
\right]
\\
&=
-(4-d)p^\rho\sigma_\rho
\\
&=
-2\epsilon\,p^\rho\sigma_\rho .
\end{aligned}
$$

因此

$$
\begin{aligned}
&
-\frac{g^2}{32\pi^2}
\left(
-2\epsilon
\right)
\left(
\frac1{\bar\epsilon}
\right)
\\
&=
\frac{g^2}{16\pi^2}
\frac{\epsilon}{\bar\epsilon}.
\end{aligned}
$$

并且

$$
\lim_{\epsilon\to0}
\frac{\epsilon}{\bar\epsilon}
=
1.
$$

所以固定 orientation 的 finite local remainder 是

$$
\boxed{
\left[
\Gamma^{A|B}
\right]_{\rm anomaly}
=
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\bar W^D_{\dot\alpha}
p_+{}^{\dot\alpha}
X^E.
}
$$

重点是：

$$
\boxed{
\epsilon
\text{ 并不在 bare triangle numerator 中。}
}
$$

它只在

$$
\boxed{
\Gamma_\triangle^{\rm UV}
+
\Gamma_{\rm contact}^{\rm UV}
}
$$

相加后，由

$$
g_{(4)}-\widehat g
$$

产生。

10. Graph-by-graph 展开可直接看出 pole cancellation

使用

$$
\widehat g^{\mu\nu}
T_{\mu\rho\nu}p^\rho
=
-2(1-\epsilon)p\!\cdot\!\sigma,
$$

$$
g_{(4)}^{\mu\nu}
T_{\mu\rho\nu}p^\rho
=
-2p\!\cdot\!\sigma,
$$

triangle local part 给出

$$
\begin{aligned}
\Gamma_\triangle^{\rm local}
={}&
-\frac{g^2}{16\pi^2}
ff\,
\left[
\frac1{\bar\epsilon}
+
F_\triangle
-
1
\right]
\bar W_{\dot\alpha}p_+{}^{\dot\alpha}X,
\end{aligned}
$$

其中 $F_\triangle$ 是 finite nonlocal Feynman-parameter integral。

Contact/bubble 给出

$$
\Gamma_{\rm contact}^{\rm local}
=
\frac{g^2}{16\pi^2}
ff\,
\left[
\frac1{\bar\epsilon}
+
F_{\rm contact}
\right]
\bar W_{\dot\alpha}p_+{}^{\dot\alpha}X.
$$

因此

$$
-\frac{g^2}{16\pi^2\bar\epsilon}
+
\frac{g^2}{16\pi^2\bar\epsilon}
=
0,
$$

而 triangle 中

$$
(1-\epsilon)\frac1{\bar\epsilon}
=
\frac1{\bar\epsilon}-1+O(\epsilon)
$$

留下 finite rational term：

$$
\boxed{
\frac{g^2}{16\pi^2}
ff\,
\bar W_{\dot\alpha}p_+{}^{\dot\alpha}X.
}
$$

$F_\triangle$ 与 $F_{\rm contact}$ 属于 full off-shell nonlocal form factor；它们与 EOM structures、wave-function graphs 和 operator counterterms 一起处理，不属于 local anomaly coefficient。

11. 修正后的 operator channel

固定 orientation：

$$
\boxed{
\left.
\nabla_-[X^AX^B]_{\overline{\rm DR}}
\right|_{\bar W^D\nabla X^E}
=
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\bar W^D_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^E.
}
$$

加入 reflected orientation：

$$
\boxed{
\begin{aligned}
\left.
\nabla_-[X^AX^B]_{\overline{\rm DR}}
\right|_{\rm anomaly}
={}&
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\\
&\times
\left[
\bar W^D_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^E
-
(\nabla_{+\dot\alpha}X^D)
\bar W^{E\dot\alpha}
\right].
\end{aligned}
}
$$

这里的 coefficient 不再来自“triangle 自带 $\epsilon$”；它来自

$$
\boxed{
\underbrace{
\Gamma_\triangle^{1/\epsilon}
}_{\text{ordinary UV divergent}}
+
\underbrace{
\Gamma_{\rm letter/bubble}^{1/\epsilon}
}_{\text{cancels physical pole}}
\quad\Longrightarrow\quad
\underbrace{
(g_{(4)}-\widehat g)\frac1\epsilon
}_{\text{finite chiral remainder}}.
}
$$

因此，你提出的 physical interpretation 是正确的：anomaly 是 gauge-complete renormalized graph set 的 finite remainder，不是 isolated triangle 的直接结果。

<!-- END EXACT text_with_tex -->

## Message 4 — user

- message_id: `1064c3f5-5760-4e0a-b400-311a968dd191`
- conversation_turn: `conversation-turn-9`
- authenticated_order: `3`
- content_sha256_without_capture_order: `81682659eca08f253160e8e015b6f0946d37007fe0c21345c3f768688d905252`

<!-- BEGIN EXACT text_with_tex -->

一个稍微更复杂一点的对象,还是 nabla minus x_a,x_b,但是呢,现在在 x_a,x_b中间,形式上我们插入一个导数的生成函数,exponential w,nabla。w是一个只有上 plus.alpha的一个某种意义上类光,或者说全纯的一个辅助常数量。nabla就是普通的斜变导数。同样计算这个单圈三角图的这个 anomaly部分。你最后的结果应该可以形式上保留 Feynman parameter的积分。
除此之外,我想说的是,你的计算,我希望整个回答流程主要focus在关于哪些图啊,还有这个dalgebra怎么做的呀,尤其是这个分子的代数啊,这部分,包括怎么识别出哪些部分是anomaly的这个的样的部分。至于已经处理好分子后，那个动量的积分,Feynman parameter的积分,这些计算都是非常常规且熟悉的,那些部分你可以不放做重点。

<!-- END EXACT text_with_tex -->

## Message 5 — assistant

- message_id: `d54b7adf-15f1-472b-9518-6347ee4b77aa`
- conversation_turn: `conversation-turn-10`
- authenticated_order: `4`
- content_sha256_without_capture_order: `5d7a7c3943174b07906682dba94ed1567bc0b8959a44cd60ecb03d8de6849c08`

<!-- BEGIN EXACT text_with_tex -->

0. Notation 与对象定义

我把你说的 generator 精确定义为 right-acting null covariant translation

$$
\boxed{
\mathcal O_w^{AB}(z)
=
X^A(z)\,\mathcal T_1X^B(z),
\qquad
X^A=(\nabla_+W_+)^A
}
$$

其中

$$
\mathcal T_s\equiv e^{s\mathbb D_w},
\qquad
\mathbb D_w\equiv w^{+\dot\alpha}\nabla_{+\dot\alpha}.
$$

辅助量 $w$ 满足

$$
w^{-\dot\alpha}=0,
\qquad
w^{+\dot\alpha}\neq0,
$$

因此

$$
w^{\alpha\dot\alpha}
=
\xi^\alpha\bar\omega^{\dot\alpha},
\qquad
\xi^\alpha=(1,0),
$$

并且

$$
w^2
=
\frac12w^{\alpha\dot\alpha}w_{\alpha\dot\alpha}
=0.
$$

Euclidean signature 中 $w$ 是 complex null auxiliary vector，不是 real Euclidean vector。

DRED prescription：

$$
d=4-2\epsilon,
\qquad
g_{(4)}^{\mu\nu}
=
\widehat g^{\mu\nu}
+
\widetilde g^{\mu\nu},
$$

$$
\widehat g^\mu{}_\mu=d,
\qquad
\widetilde g^\mu{}_\mu=4-d=2\epsilon,
$$

并取

$$
\widetilde g^\mu{}_\nu w^\nu=0,
\qquad
\widetilde g^\mu{}_\nu p^\nu
=
\widetilde g^\mu{}_\nu q^\nu=0.
$$

Four-dimensional spinor algebra：

$$
\sigma^\mu\bar\sigma^\nu+\sigma^\nu\bar\sigma^\mu
=
2g_{(4)}^{\mu\nu}.
$$

定义

$$
T_{\mu\rho\nu,+}{}^{\dot\alpha}
\equiv
(\sigma_\mu\bar\sigma_\rho\sigma_\nu)_+{}^{\dot\alpha}.
$$

Fourier convention：

$$
F(x)
=
\int\frac{d^dp}{(2\pi)^d}e^{ipx}F(p),
\qquad
\nabla_\mu F(p)\longrightarrow ip_\mu F(p).
$$

1. 首先分离 classical transport term

因为

$$
[\nabla_\alpha,\nabla_{\beta\dot\beta}]
=
2i\epsilon_{\alpha\beta}\,
\operatorname{ad}(\bar W_{\dot\beta}),
$$

所以

$$
[\nabla_-,\mathbb D_w]
=
2i\,w^{+\dot\alpha}
\operatorname{ad}(\bar W_{\dot\alpha}).
$$

Duhamel identity：

$$
[\nabla_-,e^{\mathbb D_w}]
=
\int_0^1ds\,
e^{s\mathbb D_w}
[\nabla_-,\mathbb D_w]
e^{(1-s)\mathbb D_w}.
$$

因此即使使用 classical EOM，

$$
\nabla_-X=-\nabla_+\mathcal E,
\qquad
\mathcal E=\nabla^\alpha W_\alpha,
$$

$\nabla_-\mathcal O_w$ 也不再严格为零：

$$
\begin{aligned}
\nabla_-
\left(
X^A\mathcal T_1X^B
\right)
={}&
-(\nabla_+\mathcal E^A)\mathcal T_1X^B
-
X^A\mathcal T_1(\nabla_+\mathcal E^B)
\\
&+
X^A
\int_0^1ds\,
\mathcal T_s
[\nabla_-,\mathbb D_w]
\mathcal T_{1-s}X^B.
\end{aligned}
$$

下面的 anomaly 指从 renormalized one-loop equation 中减去上述 classical transport term 和 EOM terms 后的 finite local remainder：

$$
\boxed{
\mathcal A_w^{AB}
\equiv
\left[
\nabla_-
\left(
X^A\mathcal T_1X^B
\right)
\right]_{\text{1-loop}}
\Big|_{\text{non-EOM, anomaly}}.
}
$$

2. Order $g^2$ 的完整 graph set

先展开 covariant translation。写成

$$
\mathbb D_w
=
\mathbb d_w
+
g\mathbb A_w^{(1)}
+
g^2\mathbb A_w^{(2)}
+\cdots ,
$$

其中

$$
\mathbb d_w=w\cdot\partial,
\qquad
\mathbb A_w^{(1)}
=
\operatorname{ad}(w\cdot\Gamma^{(1)}).
$$

则

$$
\mathcal T_1^{(0)}
=
e^{\mathbb d_w},
$$

$$
\boxed{
\mathcal T_1^{(1)}
=
\int_0^1ds\,
e^{s\mathbb d_w}
\mathbb A_w^{(1)}
e^{(1-s)\mathbb d_w}
}
$$

以及

$$
\boxed{
\begin{aligned}
\mathcal T_1^{(2)}
={}&
\int_0^1ds\,
e^{s\mathbb d_w}
\mathbb A_w^{(2)}
e^{(1-s)\mathbb d_w}
\\
&+
\int_{0\le a\le b\le1}
da\,db\,
e^{a\mathbb d_w}
\mathbb A_w^{(1)}
e^{(b-a)\mathbb d_w}
\mathbb A_w^{(1)}
e^{(1-b)\mathbb d_w}.
\end{aligned}
}
$$

因此 one-loop order $g^2$ 不能只保留 triangle。

graphoperator/action origintopologyrole
$T$$\frac12\langle\mathcal I_{w,(2)}S_3^2\rangle$triangle产生 $\widehat g^{\mu\nu}$ UV pole
$B_X$$-\langle\mathcal I_{X,w,(3)}S_3\rangle$nonlinear-letter bubblecancel endpoint pieces
$B_{\mathcal T}$$-\langle\mathcal I_{\mathcal T,w,(3)}S_3\rangle$Wilson-line/link bubblecancel $w^\mu$-longitudinal pieces
$C$$-\langle\mathcal I_{w,(2)}S_4\rangle$quartic/contact bubblemetric contact term
$C_{\rm coll}$collapsed terms inside triangle $D$-algebrabubblemetric contact term
$C_{\mathcal T^2}$$\langle\mathcal I_{\mathcal T,w,(4)}\rangle$link seagulldouble-eikonal completion

其中

$$
\mathcal I_{w,(2)}^{AB}
=
D_-
\left[
(K_+v^A)e^{w\cdot\partial}(K_+v^B)
\right],
$$

$$
K_+
=
-\frac14D_+\bar D^2D_+.
$$

真正产生 anomaly 的 sector 是

$$
\boxed{
T_{\text{metric pole}}
+
C_{\text{metric pole}}.
}
$$

其余 $w$-dependent poles 是 ordinary gauge-covariant renormalization；它们由 $B_X,B_{\mathcal T},C_{\mathcal T^2}$ 等相消。

3. Triangle topology 与 momentum routing

固定 orientation：

$A$-letter 连接到 $\bar W^D(q)$ vertex；

translated $B$-letter 连接到 $W_+^E(p)$ vertex；

$P=p+q$。

                         r1 = k+q
              \bar W^D ●────────────● W_+^E
                       ╲            ╱
                        ╲          ╱
             r0 = k      ╲        ╱      r2 = k+P
                          ●
                 X^A e^{w·∇} X^B

定义

$$
r_0=k,
\qquad
r_1=k+q,
\qquad
r_2=k+P.
$$

三条 propagators：

$$
\Pi_0=\frac{\delta^4(\theta_0-\theta_1)}{D_0},
\qquad
D_0=k^2,
$$

$$
\Pi_1=\frac{\delta^4(\theta_1-\theta_2)}{D_1},
\qquad
D_1=(k+q)^2,
$$

$$
\Pi_2=\frac{\delta^4(\theta_2-\theta_0)}{D_2},
\qquad
D_2=(k+P)^2.
$$

因为 exponential 作用在 $B$-letter 上：

$$
e^{w\cdot\partial}(K_+v^B)(r_2)
=
e^{iw\cdot r_2}(K_+v^B)(r_2).
$$

所以 triangle 的原始 denominator 和 phase 为

$$
\boxed{
\frac{e^{iw\cdot r_2}}
{k^2(k+q)^2(k+P)^2}.
}
$$

4. Cubic vertices 与未做 $D$-algebra 的 amplitude

使用

$$
\{D_\alpha,\bar D_{\dot\alpha}\}
=
2p_{\alpha\dot\alpha}
$$

的 momentum-space convention。

Background field-strength vertices：

$$
\mathcal V_{\bar W}
=
\frac{ig}{2}
f^{ACD}\,
\bar W^D_{\dot\alpha}
\left(
\bar D_C^{\dot\alpha}
-
\bar D_A^{\dot\alpha}
\right),
$$

$$
\mathcal V_W
=
-\frac{ig}{2}
f^{BCE}\,
W^{E\gamma}
\left(
D_{C\gamma}
-
D_{B\gamma}
\right).
$$

Vertex product：

$$
\left(\frac{ig}{2}\right)
\left(-\frac{ig}{2}\right)
=
\frac{g^2}{4}.
$$

固定 orientation 的 supergraph 为

$$
\begin{aligned}
\Gamma_{T}^{A|B}(w)
={}&
\frac{g^2}{4}
f^{ACD}f^{BCE}
\int\frac{d^dk}{(2\pi)^d}
e^{iw\cdot r_2}
\\
&\times
\int d^4\theta_0d^4\theta_1d^4\theta_2\,
\bar W^D_{\dot\alpha}(\theta_1)
W_+^E(\theta_2)
\\
&\times
\Big[
D_{0-}^{[01]}K_{0+}^{[01]}K_{0+}^{[02]}
+
K_{0+}^{[01]}D_{0-}^{[02]}K_{0+}^{[02]}
\Big]
\\
&\times
\Big[
\bar D_1^{\dot\alpha[12]}
-
\bar D_1^{\dot\alpha[10]}
\Big]
\\
&\times
\Big[
D_{2\gamma}^{[21]}
-
D_{2\gamma}^{[20]}
\Big]
\\
&\times
\Pi_0\Pi_1\Pi_2 .
\end{aligned}
$$

符号 $[ij]$ 表示 derivative 只作用在连接 $i,j$ 的 propagator 上。

5. Triangle 的完整 $D$-algebra 核心

5.1 Insertion factor

$$
K_+
=
-\frac14D_+\bar D^2D_+.
$$

当 $D_-$ 作用在相应 insertion leg 时：

$$
\begin{aligned}
D_-K_+
&=
-\frac14D_-D_+\bar D^2D_+
\\
&=
-\frac18D^2\bar D^2D_+.
\end{aligned}
$$

两个 $K_+$ 与一个 $D_-$ 因此给出

$$
\frac1{16}\times\frac12
=
\frac1{32}.
$$

Closed Grassmann loop：

$$
\left[
D^2\bar D^2\delta^4(\theta)
\right]_{\theta=0}
=
16.
$$

5.2 四个 endpoint terms

在 $\bar W$-vertex，$\bar D$ 可以作用于 $r_0$ 或 $r_1$ line。

在 $W$-vertex，$D$ 可以作用于 $r_1$ 或 $r_2$ line。

使用

$$
D_i\delta_{ij}=-D_j\delta_{ij},
\qquad
\bar D_i\delta_{ij}=-\bar D_j\delta_{ij},
$$

vertex 中原来的 minus sign 与 endpoint transfer 的 minus sign相消。四项在 momentum numerator 中全部以 plus sign 出现：

$$
\begin{array}{c|c|c}
\bar D\text{ endpoint}
&
D\text{ endpoint}
&
\text{numerator}
\\ \hline
r_0&r_1&
(r_0)_{+\dot\beta}
p^{\dot\beta\gamma}
(r_1)_\gamma{}^{\dot\alpha}
\\
r_0&r_2&
(r_0)_{+\dot\beta}
p^{\dot\beta\gamma}
(r_2)_\gamma{}^{\dot\alpha}
\\
r_1&r_1&
(r_1)_{+\dot\beta}
p^{\dot\beta\gamma}
(r_1)_\gamma{}^{\dot\alpha}
\\
r_1&r_2&
(r_1)_{+\dot\beta}
p^{\dot\beta\gamma}
(r_2)_\gamma{}^{\dot\alpha}
\end{array}
$$

相加：

$$
\begin{aligned}
&\left[
(r_0)_{+\dot\beta}
+
(r_1)_{+\dot\beta}
\right]
p^{\dot\beta\gamma}
\left[
(r_1)_\gamma{}^{\dot\alpha}
+
(r_2)_\gamma{}^{\dot\alpha}
\right]
\\
&=
(L_1)_{+\dot\beta}
p^{\dot\beta\gamma}
(L_2)_\gamma{}^{\dot\alpha},
\end{aligned}
$$

其中

$$
\boxed{
L_1=r_0+r_1=2k+q,
}
$$

$$
\boxed{
L_2=r_1+r_2=2k+q+P=2k+p+2q.
}
$$

5.3 Spinor chain

利用

$$
(L_1)_{+\dot\beta}
=
L_1^\mu(\sigma_\mu)_{+\dot\beta},
$$

$$
p^{\dot\beta\gamma}
=
p^\rho(\bar\sigma_\rho)^{\dot\beta\gamma},
$$

$$
(L_2)_\gamma{}^{\dot\alpha}
=
L_2^\nu(\sigma_\nu)_\gamma{}^{\dot\alpha},
$$

得到

$$
\boxed{
(L_1)_{+\dot\beta}
p^{\dot\beta\gamma}
(L_2)_\gamma{}^{\dot\alpha}
=
T_{\mu\rho\nu,+}{}^{\dot\alpha}
L_1^\mu p^\rho L_2^\nu.
}
$$

Numerical $D$-factor：

$$
\frac1{32}
\times16
\times2
\times2
=
2.
$$

其中两个 $2$ 来自两个 internal mixed anticommutators。

乘以 vertex product $g^2/4$：

$$
\frac{g^2}{4}\times2
=
\frac{g^2}{2}.
$$

因此 three-propagator triangle 为

$$
\boxed{
\begin{aligned}
\Gamma_T^{A|B}(w)
={}&
\frac{g^2}{2}
f^{ACD}f^{BCE}
\bar W^D_{\dot\alpha}(q)
(ip^\rho)
X^E(p)
\\
&\times
T_{\mu\rho\nu,+}{}^{\dot\alpha}
\int\frac{d^dk}{(2\pi)^d}
\frac{
e^{iw\cdot r_2}
L_1^\mu L_2^\nu
}{
D_0D_1D_2
}
\\
&+
\Gamma_{\rm coll}
+
\Gamma_{\rm EOM}.
\end{aligned}
}
$$

这是进行 Feynman parameterization 之前的完整 triangle amplitude。

6. Feynman parameters：phase 与 numerator 的精确分离

使用

$$
\frac1{D_0D_1D_2}
=
2
\int_{\substack{x,y,z\ge0\\x+y+z=1}}
dx\,dy\,dz\,
\frac1{(\ell^2+\Delta)^3},
$$

其中

$$
\ell=k+yq+zP,
$$

$$
\Delta
=
xy\,q^2+xz\,P^2+yz\,p^2.
$$

定义

$$
a=x,
\qquad
b=x+y,
$$

则

$$
0\le a\le b\le1,
\qquad
y=b-a,
\qquad
z=1-b.
$$

Translated-leg momentum：

$$
\begin{aligned}
r_2
&=
k+P
\\
&=
\ell-yq-zP+P
\\
&=
\ell+(1-z)P-yq
\\
&=
\ell+b(p+q)-(b-a)q
\\
&=
\boxed{
\ell+bp+aq
}.
\end{aligned}
$$

所以 phase 分解为

$$
\boxed{
e^{iw\cdot r_2}
=
e^{iw\cdot\ell}
e^{iw\cdot(bp+aq)}.
}
$$

并且

$$
L_1=2\ell+A,
\qquad
L_2=2\ell+B,
$$

其中

$$
\boxed{
A=(1-2y)q-2zP,
}
$$

$$
\boxed{
B=(1-2y)q+(1-2z)P.
}
$$

因此

$$
\boxed{
L_1^\mu L_2^\nu
=
4\ell^\mu\ell^\nu
+
2\ell^\mu B^\nu
+
2A^\mu\ell^\nu
+
A^\mu B^\nu.
}
$$

7. 含 null exponential 的 loop-momentum moments

定义

$$
J_n(\Delta)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{e^{iw\cdot\ell}}
{(\ell^2+\Delta)^n}.
$$

因为

$$
w^2=0,
\qquad
\widetilde g^\mu{}_\nu w^\nu=0,
$$

Schwinger Gaussian 中

$$
e^{-w^2/(4s)}=1.
$$

因此

$$
J_n(\Delta)
=
\frac{\mu^{2\epsilon}}
{(4\pi)^{d/2}}
\frac{\Gamma(n-d/2)}
{\Gamma(n)}
\Delta^{d/2-n}.
$$

特别地，

$$
J_1
=
\frac{\mu^{2\epsilon}}
{(4\pi)^{2-\epsilon}}
\Gamma(-1+\epsilon)\Delta^{1-\epsilon},
$$

$$
J_2
=
\frac{\mu^{2\epsilon}}
{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\Delta^{-\epsilon},
$$

$$
J_3
=
\frac{\mu^{2\epsilon}}
{(4\pi)^{2-\epsilon}}
\frac{\Gamma(1+\epsilon)}{2}
\Delta^{-1-\epsilon}.
$$

精确的 first moment：

$$
\boxed{
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^\mu e^{iw\cdot\ell}}
{(\ell^2+\Delta)^3}
=
\frac{i}{4}w^\mu J_2(\Delta).
}
$$

精确的 second moment：

$$
\boxed{
4\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^\mu\ell^\nu e^{iw\cdot\ell}}
{(\ell^2+\Delta)^3}
=
\widehat g^{\mu\nu}J_2(\Delta)
-
\frac12w^\mu w^\nu J_1(\Delta).
}
$$

所以整个 numerator integral 为

$$
\boxed{
\begin{aligned}
\mathfrak N^{\mu\nu}(a,b)
\equiv{}&
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{
e^{iw\cdot\ell}
(2\ell+A)^\mu(2\ell+B)^\nu
}
{(\ell^2+\Delta)^3}
\\[1mm]
={}&
\widehat g^{\mu\nu}J_2
\\
&+
\frac{i}{2}
\left(
w^\mu B^\nu
+
A^\mu w^\nu
\right)J_2
\\
&-
\frac12w^\mu w^\nu J_1
\\
&+
A^\mu B^\nu J_3.
\end{aligned}
}
$$

这是识别 anomaly 最重要的 decomposition。

8. 哪些 numerator pieces 是 anomaly candidate

逐项分类：

$$
\boxed{
\widehat g^{\mu\nu}J_2
}
$$

是 logarithmic tensor pole：

$$
J_2
=
\frac1{16\pi^2}
\left(
\frac1{\bar\epsilon}
+
\ln\frac{\mu^2}{\Delta}
\right)
+
O(\epsilon).
$$

它与 contact graph 的

$$
-g_{(4)}^{\mu\nu}J_2
$$

相加后产生

$$
-\widetilde g^{\mu\nu}J_2.
$$

这才是 anomaly sector。

第二项

$$
\frac{i}{2}w^\mu B^\nu J_2
$$

在当前 holomorphic projection 中直接为零，因为

$$
w^\mu
T_{\mu\rho\nu,+}{}^{\dot\alpha}
=
w_{+\dot\beta}
(\bar\sigma_\rho\sigma_\nu)^{\dot\beta\dot\alpha},
$$

而

$$
w^{-\dot\alpha}=0
\quad\Longrightarrow\quad
w_{+\dot\alpha}=0.
$$

故

$$
\boxed{
w^\mu
T_{\mu\rho\nu,+}{}^{\dot\alpha}
=0.
}
$$

因此

$$
T_{\mu\rho\nu,+}{}^{\dot\alpha}
w^\mu B^\nu
=
0.
$$

同样，

$$
T_{\mu\rho\nu,+}{}^{\dot\alpha}
w^\mu w^\nu
=
0.
$$

所以 $J_1$ power-contact term 在该 projection 中也不进入最终 amplitude。

剩余 mixed pole：

$$
\frac{i}{2}A^\mu w^\nu J_2
$$

一般不为零，但它是 Wilson-line longitudinal term，由 $\mathcal T^{(1)}$ insertion bubble 抵消。

其 cancellation 使用精确 eikonal identity：

$$
\boxed{
iw\cdot(r-r')
\int_0^1ds\,
e^{isw\cdot r}
e^{i(1-s)w\cdot r'}
=
e^{iw\cdot r}
-
e^{iw\cdot r'}.
}
$$

Triangle 中 $A^\mu w^\nu$ piece 可写成相邻 propagator phases 的 difference；这些 boundary phases 正好由：

$$
B_{\mathcal T},
\qquad
B_X,
\qquad
C_{\rm coll}
$$

抵消。

最后

$$
A^\mu B^\nu J_3
$$

是 UV finite：

$$
J_3
=
\frac1{32\pi^2\Delta}
+
O(\epsilon).
$$

它属于完整 nonlocal triangle form factor，不属于 anomaly。

因此：

$$
\boxed{
\mathfrak N^{\mu\nu}_{\rm anomaly\ candidate}
=
\widehat g^{\mu\nu}J_2.
}
$$

9. Contact graphs 的 metric $D$-algebra

所有 nonlinear-letter、quartic、collapsed-propagator contact graphs 的 metric part 可整理为同一个 two-propagator kernel。

其 spinor derivative chain 为

$$
(D_-^{(1)}-D_-^{(2)})
K_+
(\bar D^{\dot\alpha(2)}-\bar D^{\dot\alpha(1)}).
$$

在两条 propagator delta-functions 上：

$$
D_-^{(1)}-D_-^{(2)}
=
2D_-^{(1)},
$$

$$
\bar D^{\dot\alpha(2)}
-
\bar D^{\dot\alpha(1)}
=
-2\bar D^{\dot\alpha(1)}.
$$

所以

$$
\begin{aligned}
&
-\frac14
(2D_-)
D_+\bar D^2D_+
(-2\bar D^{\dot\alpha})
\\
&=
D_-D_+\bar D^2D_+\bar D^{\dot\alpha}
\\
&=
\frac12D^2\bar D^2D_+\bar D^{\dot\alpha}.
\end{aligned}
$$

作用在 external $X$ 上：

$$
D_+X
=
D_+^2W_+
=
0.
$$

于是

$$
\begin{aligned}
D_+\bar D^{\dot\alpha}X
&=
\{D_+,\bar D^{\dot\alpha}\}X
-
\bar D^{\dot\alpha}D_+X
\\
&=
2p_+{}^{\dot\alpha}X.
\end{aligned}
$$

使用 four-dimensional identity：

$$
\boxed{
g_{(4)}^{\mu\nu}
T_{\mu\rho\nu,+}{}^{\dot\alpha}
p^\rho
=
-2p_+{}^{\dot\alpha}.
}
$$

因此 contact graph 的 metric tensor 必然是

$$
\boxed{
-g_{(4)}^{\mu\nu}J_2.
}
$$

这里的 $g_{(4)}^{\mu\nu}$ 来自 four-dimensional $D$-algebra，而不是 loop tensor reduction。

10. Ordered Feynman-parameter kernel

Triangle 的 Feynman parameters 给出

$$
a=x,
\qquad
b=x+y,
\qquad
0\le a\le b\le1,
$$

以及 external phase

$$
e^{iw\cdot(aq+bp)}.
$$

定义 normalized ordered kernel：

$$
\boxed{
\mathcal K_w[F(q),G(p)]
=
2
\int_0^1db
\int_0^bda\,
e^{iw\cdot(aq+bp)}
F(q)G(p).
}
$$

因为

$$
2\int_0^1db\int_0^bda
=
2\cdot\frac12
=
1,
$$

所以

$$
\mathcal K_{w=0}[F,G]=FG.
$$

在 position space 中：

$$
\boxed{
\mathcal K_w[F,G]
=
2
\int_0^1db
\int_0^bda\,
(\mathcal T_aF)(\mathcal T_bG).
}
$$

Contact graphs 的 full finite denominators 与 triangle 不同；但其 UV-local pole kernel 由 Duhamel ordering 和 eikonal Ward identity 精确地整理成同一个 ordered kernel。

11. Triangle pole 与 contact pole

固定 orientation 的 triangle metric pole：

$$
\boxed{
\begin{aligned}
\Gamma_{T,\rm pole}^{A|B}
={}&
\frac{g^2}{32\pi^2\bar\epsilon}
f^{ACD}f^{BCE}
\\
&\times
\mathcal K_w
\left[
\bar W^D_{\dot\alpha},
\,
p^\rho X^E
\right]
T_{\mu\rho\nu,+}{}^{\dot\alpha}
\widehat g^{\mu\nu}.
\end{aligned}
}
$$

Gauge-completing contact pole：

$$
\boxed{
\begin{aligned}
\Gamma_{C,\rm pole}^{A|B}
={}&
-\frac{g^2}{32\pi^2\bar\epsilon}
f^{ACD}f^{BCE}
\\
&\times
\mathcal K_w
\left[
\bar W^D_{\dot\alpha},
\,
p^\rho X^E
\right]
T_{\mu\rho\nu,+}{}^{\dot\alpha}
g_{(4)}^{\mu\nu}.
\end{aligned}
}
$$

相加：

$$
\begin{aligned}
\Gamma_{T+C,\rm pole}^{A|B}
={}&
-\frac{g^2}{32\pi^2\bar\epsilon}
f^{ACD}f^{BCE}
\\
&\times
\mathcal K_w
\left[
\bar W^D_{\dot\alpha},
p^\rho X^E
\right]
T_{\mu\rho\nu,+}{}^{\dot\alpha}
\widetilde g^{\mu\nu}.
\end{aligned}
$$

12. Evanescent contraction

严格 four-dimensional identity：

$$
\sigma_\mu\bar\sigma_\rho\sigma_\nu
=
g_{(4)\mu\rho}\sigma_\nu
+
g_{(4)\rho\nu}\sigma_\mu
-
g_{(4)\mu\nu}\sigma_\rho
+
(\mu,\nu)\text{-antisymmetric}.
$$

由于 $\widetilde g^{\mu\nu}$ symmetric：

$$
\begin{aligned}
\widetilde g^{\mu\nu}
\sigma_\mu\bar\sigma_\rho\sigma_\nu
&=
2\widetilde g_\rho{}^\lambda\sigma_\lambda
-
\widetilde g^\mu{}_\mu\sigma_\rho.
\end{aligned}
$$

External momentum 无 evanescent component：

$$
\widetilde g_\rho{}^\lambda p^\rho=0.
$$

因此

$$
\begin{aligned}
p^\rho\widetilde g^{\mu\nu}
T_{\mu\rho\nu,+}{}^{\dot\alpha}
&=
-(4-d)p^\rho(\sigma_\rho)_+{}^{\dot\alpha}
\\
&=
-2\epsilon\,p_+{}^{\dot\alpha}.
\end{aligned}
$$

所以

$$
-\frac{1}{32\pi^2\bar\epsilon}
\left(-2\epsilon\right)
=
\frac1{16\pi^2}.
$$

13. Fixed-orientation anomaly

Momentum-space result：

$$
\boxed{
\begin{aligned}
\mathcal A_{w,A|B}^{AB}
(p,q)
={}&
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\\
&\times
2\int_0^1db
\int_0^bda\,
e^{iw\cdot(aq+bp)}
\\
&\times
\bar W^D_{\dot\alpha}(q)
(ip_+{}^{\dot\alpha})
X^E(p).
\end{aligned}
}
$$

它的关键结构是：

$$
\boxed{
0\le a\le b\le1.
}
$$

$\bar W$ 位于 ordered ray parameter $a$，而 $X$ 位于更靠近 translated endpoint 的 $b$。

14. 加入 reflected orientation

Reflected graph 中：

$X^D(p)$ 位于较早位置 $a$；

$\bar W^E(q)$ 位于较晚位置 $b$。

因此

$$
\boxed{
\begin{aligned}
\mathcal A_w^{AB}
={}&
\frac{g^2}{8\pi^2}
f^{ACD}f^{BCE}
\int_0^1db
\int_0^bda
\\
&\times
\Big[
(\mathcal T_a\bar W^D_{\dot\alpha})
\,
\mathcal T_b(\nabla_+{}^{\dot\alpha}X^E)
\\
&\hspace{15mm}
-
\mathcal T_a(\nabla_{+\dot\alpha}X^D)
\,
(\mathcal T_b\bar W^{E\dot\alpha})
\Big].
\end{aligned}
}
$$

等价地，使用 normalized kernel：

$$
\boxed{
\begin{aligned}
\mathcal A_w^{AB}
={}&
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\,
\mathcal K_w
\Big[
\bar W^D_{\dot\alpha},
\nabla_+{}^{\dot\alpha}X^E
\Big]
\\
&-
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\,
\mathcal K_w
\Big[
\nabla_{+\dot\alpha}X^D,
\bar W^{E\dot\alpha}
\Big].
\end{aligned}
}
$$

恢复

$$
X^A=(\nabla_+W_+)^A,
$$

得到

$$
\boxed{
\begin{aligned}
\mathcal A_w^{AB}
={}&
\frac{g^2}{8\pi^2}
f^{ACD}f^{BCE}
\int_0^1db
\int_0^bda
\\
&\times
\Big[
\mathcal T_a(\bar W^D_{\dot\alpha})
\,
\mathcal T_b
\left(
\nabla_+{}^{\dot\alpha}\nabla_+W_+^E
\right)
\\
&\hspace{13mm}
-
\mathcal T_a
\left(
\nabla_{+\dot\alpha}\nabla_+W_+^D
\right)
\,
\mathcal T_b(\bar W^{E\dot\alpha})
\Big].
\end{aligned}
}
$$

15. 两个 nontrivial checks

$w=0$

$$
2\int_0^1db\int_0^bda=1.
$$

所以

$$
\begin{aligned}
\mathcal A_{0}^{AB}
={}&
\frac{g^2}{16\pi^2}
f^{ACD}f^{BCE}
\\
&\times
\left[
\bar W^D_{\dot\alpha}
\nabla_+{}^{\dot\alpha}X^E
-
(\nabla_{+\dot\alpha}X^D)
\bar W^{E\dot\alpha}
\right].
\end{aligned}
$$

严格恢复无 derivative generator 的结果。

Descendant expansion

定义

$$
\mathbb D_w=w\cdot\nabla.
$$

则

$$
\begin{aligned}
\mathcal K_w[F,G]
&=
2\int_0^1db\int_0^bda\,
e^{a\mathbb D_w}F\,
e^{b\mathbb D_w}G
\\
&=
2
\sum_{m,n\ge0}
\frac{
(\mathbb D_w^mF)
(\mathbb D_w^nG)
}{
m!\,n!
}
\int_0^1db\int_0^bda\,
a^m b^n.
\end{aligned}
$$

参数积分：

$$
\begin{aligned}
\int_0^1db\int_0^bda\,
a^m b^n
&=
\int_0^1db\,
\frac{b^{m+1}}{m+1}
b^n
\\
&=
\frac1{m+1}
\int_0^1db\,
b^{m+n+1}
\\
&=
\frac1{(m+1)(m+n+2)}.
\end{aligned}
$$

所以

$$
\boxed{
\mathcal K_w[F,G]
=
2
\sum_{m,n\ge0}
\frac{
(\mathbb D_w^mF)
(\mathbb D_w^nG)
}{
m!\,n!\,
(m+1)(m+n+2)
}.
}
$$

例如一次 derivative：

$$
\mathcal K_w[F,G]
=
FG
+
\frac13(\mathbb D_wF)G
+
\frac23F(\mathbb D_wG)
+
O(w^2).
$$

这与原始 derivative 插在右侧 letter 上的 ordering 一致：生成的 anomaly 中，derivative weight 更偏向 right descendant。

<!-- END EXACT text_with_tex -->

## Message 6 — user

- message_id: `0f6acae0-bd68-4fa5-874c-60dc2fb5fdbb`
- conversation_turn: `conversation-turn-11`
- authenticated_order: `5`
- content_sha256_without_capture_order: `d18b0781c9a5c1f5edc2f87420b2102046fdd3006083b88e997952f6d57a0f5e`

<!-- BEGIN EXACT text_with_tex -->

漂亮,你这一段从计算到论证都相当的不错。我现在的要求是,我将会利用Codex进行一个比较自动化的,完整的,且比较好让他人可读的,尤其是这些Feynman图我希望能很好地渲染出来,画出来的方式工作。我希望你帮我写一段提示词,我希望你帮我整理一段,首先把我的这个计算逻辑非常清楚地讲明白,使得可以直接作为提示词给Codex（现有工作流见github）。其次,再来一段提示词,专门focus在如何生成这些Feynman diagram,无论是这些,对,super Feynman diagrams,以及让它们渲染,并从这些图中获取我们的amplitude,或者说这个mil contract的外球作为留存的算法。这套理论的逻辑,我希望你把这个逻辑表述得非常清楚,包括我们的正规化方案,这个计算的逻辑。
我这的方法,我认为真正的精妙之处或者说本质之处在于,就是我们可以假设,如果这种化不会破坏这个那种equation of motion与一个letters contract形成那种delta函数（即Schwinger-Dyson equation),如果不会有这种破坏的话,那么斯文格-戴森 equation将会严格地永远成立。那样的话,我们将不会有任何的anomaly term。所以说,我们真正要focus的向全部来自于这种由于正规化导致的这个可以称之为cutting rules的失效。
此即我的superspace工作route。

<!-- END EXACT text_with_tex -->

## Message 7 — assistant

- message_id: `e0aef8be-dd6b-4be5-88c4-113bb38fe8d8`
- conversation_turn: `conversation-turn-12`
- authenticated_order: `6`
- content_sha256_without_capture_order: `98e9ae45f33531adf9ac6f77d569af5cd94a7211d2ef823a4830fcf0a39351c6`

<!-- BEGIN EXACT text_with_tex -->

核心理论逻辑

你的 superspace route 可以压缩成一个非常清楚的 statement：

$$
\boxed{
\text{Anomaly 是 regularization 与 Schwinger–Dyson cutting operation 不对易的有限余项。}
}
$$

定义

$$
X^A=(\nabla_+W_+)^A,
\qquad
\mathbb D_w=w^{+\dot\alpha}\nabla_{+\dot\alpha},
\qquad
\mathcal T_s=e^{s\mathbb D_w},
$$

$$
\mathcal O_w^{AB}
=
X^A\mathcal T_1X^B.
$$

未正规化 path integral 中，

$$
0=
\int\mathcal Dv\,
\frac{\delta}{\delta v^C(z)}
\left[
\mathcal F[v]e^{-S[v]}
\right]
$$

给出严格 Schwinger–Dyson equation：

$$
\boxed{
\left\langle
\frac{\delta S}{\delta v^C(z)}
\mathcal F[v]
\right\rangle
=
\left\langle
\frac{\delta\mathcal F[v]}{\delta v^C(z)}
\right\rangle.
}
$$

Graphically：

$$
\frac{\delta S}{\delta v}
\quad\text{attached to}\quad
\frac1{\Box}
$$

应当严格 cut/collapse：

$$
\Box\frac1{\Box}
=
\delta.
$$

因此，若 regulator 同时保持：

$$
\frac{\delta S}{\delta v}
\leftrightarrow
\frac{\delta}{\delta v},
\qquad
\Box\frac1{\Box}=\delta,
\qquad
\text{four-dimensional }D\text{-algebra},
$$

则 triangle 与它的 Schwinger–Dyson cut descendants——nonlinear-letter bubbles、contact graphs、collapsed-propagator graphs、link graphs——应严格相消，不会留下 anomaly。

令

$$
\mathcal C_{\rm SD}
$$

表示 graph cutting operation，令

$$
R_\epsilon
$$

表示 DRED regularization。则 anomaly 的本质定义是

$$
\boxed{
\mathcal A
=
\lim_{\epsilon\to0}
\left[
\mathcal C_{\rm SD},R_\epsilon
\right]
\Gamma_{\rm parent}.
}
$$

在 DRED 中：

$$
\text{spinor and }D\text{-algebra use }g_{(4)}^{\mu\nu},
$$

而 loop tensor reduction 使用

$$
\widehat g^{\mu\nu},
\qquad
\widehat g^\mu{}_\mu=4-2\epsilon.
$$

因此 SD-related graphs 的 ordinary UV poles 相消后留下

$$
\widehat g^{\mu\nu}-g_{(4)}^{\mu\nu}
=
-\widetilde g^{\mu\nu},
$$

$$
\widetilde g^\mu{}_\mu=2\epsilon.
$$

于是

$$
\widetilde g^{\mu\nu}\times
\frac1\epsilon
$$

形成 finite remainder。不能在 isolated triangle numerator 中预先插入 $\epsilon$；必须先计算完整 SD graph family，再由其 mismatch 得到 anomaly。

Prompt A：完整计算、GitHub workflow 与可读推导

下面整段可以直接交给 Codex。

You are working inside the current GitHub repository. Your task is to implement,
verify, and document a complete one-loop superspace calculation in Euclidean
4d N=1 pure SYM.

Do not import or copy a final coefficient from the literature or from prior
notes. Derive every sign, symmetry factor, color factor, D-algebra factor, and
loop numerator from the action and composite operator conventions used in this
repository. Any expected final formula mentioned below is only a regression
test, never an input to the derivation.

Before editing anything:

1. Inspect AGENTS.md, README files, CONTRIBUTING files, existing symbolic
   notebooks, LaTeX conventions, build scripts, CI workflows, and generated-file
   policies.
2. Identify the repository's existing language, CAS, testing framework, and
   document-generation workflow.
3. Reuse the existing architecture. Do not introduce a parallel build system
   unless strictly necessary.
4. Produce a brief implementation plan listing the files that will be created
   or modified.

======================================================================
I. OBJECT OF THE CALCULATION
======================================================================

Work with

    X^A = (nabla_+ W_+)^A

and the right-acting covariant translation operator

    D_w = w^{+\dot alpha} nabla_{+\dot alpha},
    T_s = exp(s D_w).

The operator is

    O_w^{AB} = X^A T_1 X^B,

and the quantity of interest is

    nabla_- [ X^A T_1 X^B ].

The auxiliary vector w has only an upper undotted plus component:

    w^{-\dot alpha} = 0,
    w^{+\dot alpha} != 0.

Treat w as a complex null auxiliary vector in Euclidean signature:

    w^2 = 0.

The exponential acts on the right letter. Preserve this ordering throughout
the calculation.

Separate the following three sectors:

1. classical EOM terms;
2. the classical transport term generated by [nabla_-, T_1];
3. the genuine one-loop anomalous remainder.

Do not include the first two sectors in the anomaly.

Use the Duhamel identity

    [nabla_-, exp(D_w)]
      = integral_0^1 ds
          exp(s D_w) [nabla_-, D_w] exp((1-s) D_w)

to display the classical transport contribution explicitly.

======================================================================
II. CENTRAL SCHWINGER-DYSON / CUTTING-RULE PRINCIPLE
======================================================================

The conceptual center of the calculation is the exact unregularized
Schwinger-Dyson identity

    0 = integral Dv delta/delta v^C(z) [ F[v] exp(-S[v]) ],

hence

    < (delta S / delta v^C(z)) F[v] >
      =
    < delta F[v] / delta v^C(z) >.

Interpret this graphically as a cutting rule:

    an equation-of-motion insertion attached to a propagator
    collapses that propagator into a superspace delta function.

Introduce an abstract operation C_SD acting on a parent supergraph by cutting
the propagator adjacent to an EOM insertion and generating the corresponding
letter/contact descendant graphs.

The central hypothesis to test is:

    If regularization commuted with C_SD, then the complete SD graph family
    would cancel exactly and there would be no anomaly.

Define the anomaly as the finite obstruction

    A = lim_{epsilon -> 0}
        [ C_SD R_epsilon - R_epsilon C_SD ] Gamma_parent,

up to the overall sign fixed by the repository's Euclidean path-integral
conventions.

The calculation must therefore be organized around an SD-complete family of
graphs, not around an isolated triangle.

======================================================================
III. DRED CONVENTIONS
======================================================================

Use dimensional reduction with

    d = 4 - 2 epsilon,

    g_(4)^{mu nu}
      = ghat^{mu nu} + gtilde^{mu nu},

    tr ghat = d,
    tr gtilde = 4 - d = 2 epsilon.

Non-negotiable rule:

    all spinor algebra, sigma-matrix algebra, chirality identities,
    and superspace D-algebra remain four-dimensional.

Only loop momenta and rotational tensor integrals are d-dimensional.

Do not introduce a separate evanescent sigma-matrix algebra.
Do not replace the four-dimensional Clifford relation by a d-dimensional one.

Loop momenta satisfy

    k^mu = ghat^mu_nu k^nu,
    gtilde^mu_nu k^nu = 0.

External momenta and the auxiliary null vector w are taken in the physical
momentum subspace:

    gtilde^mu_nu p^nu = 0,
    gtilde^mu_nu q^nu = 0,
    gtilde^mu_nu w^nu = 0.

Keep p^2, q^2, and (p+q)^2 nonzero during the calculation so that UV and IR
singularities cannot be confused.

Never insert an epsilon factor into the bare triangle numerator. The
evanescent factor may appear only after summing the SD-related UV poles.

======================================================================
IV. CONVENTION LEDGER
======================================================================

Create a convention ledger at the start of the derivation containing:

- Euclidean Fourier-transform convention;
- normalization of T^A and f^{ABC};
- normalization of the vector prepotential;
- definition of W_alpha;
- background-field gauge choice;
- vector-superfield propagator;
- chiral and antichiral cubic vertices;
- quartic action vertices;
- spinor-index raising and lowering;
- signs in {D_alpha, Dbar_dot alpha};
- definitions of D^2 and Dbar^2;
- normalization of superspace delta functions;
- definition and orientation of all external and loop momenta.

Every later sign and factor must reference this ledger.

======================================================================
V. ACTION AND OPERATOR EXPANSION
======================================================================

Expand the action and operator systematically:

    S = S_(2) + g S_(3) + g^2 S_(4) + ...

    X = X_(1) + g X_(2) + g^2 X_(3) + ...

    T_1 = T_1^(0) + g T_1^(1) + g^2 T_1^(2) + ...

Use the Duhamel expansion

    T_1^(1)
      =
    integral_0^1 ds
      exp(s d_w) A_w^(1) exp((1-s) d_w),

and

    T_1^(2)
      =
    integral_0^1 ds
      exp(s d_w) A_w^(2) exp((1-s) d_w)

    + integral_{0 <= a <= b <= 1} da db
      exp(a d_w) A_w^(1)
      exp((b-a) d_w) A_w^(1)
      exp((1-b) d_w),

where

    d_w = w dot partial.

Write the explicit prepotential expressions for X_(1), X_(2), and all pieces
of the insertion needed through order g^2.

Do not summarize these expansions by saying "plus interaction terms."
Display them.

======================================================================
VI. COMPLETE ONE-LOOP GRAPH FAMILY
======================================================================

At order g^2, organize the amplitude as

    Gamma^(1)
      =
      1/2 < I_(2) S_(3)^2 >_connected
      -   < I_(3) S_(3) >_connected
      -   < I_(2) S_(4) >_connected
      +   < I_(4) >_connected
      +   counterterm / wave-function contributions,

with signs verified from the Euclidean interaction expansion.

The graph family must include at least:

A. Parent triangle graphs
   - both color/orientation choices;
   - two placements of nabla_- on the two letters;
   - all derivative endpoint choices at both cubic vertices.

B. Nonlinear-letter bubbles
   - terms from X_(2);
   - terms from the outer covariant nabla_- connection.

C. Covariant-translation/link graphs
   - one-link vertices from T_1^(1);
   - two-link and seagull terms from T_1^(2);
   - both endpoint and interior link insertions.

D. Quartic/contact bubbles
   - contributions from S_(4).

E. Collapsed-propagator graphs
   - every term generated during triangle D-algebra when a Box cancels one
     propagator.

F. Tadpoles and counterterms
   - identify scaleless DRED tadpoles explicitly;
   - distinguish external-field renormalization from genuine composite-
     operator mixing;
   - avoid double counting.

For every graph, record:

- graph ID;
- source term in the action/operator expansion;
- symmetry factor;
- Wick-contraction multiplicity;
- Grassmann sign;
- color factor;
- momentum routing;
- denominator;
- translation phase;
- external tensor structure;
- relation to its SD parent or descendant.

======================================================================
VII. TRIANGLE MOMENTUM ROUTING
======================================================================

For one fixed orientation use

    r_0 = k,
    r_1 = k + q,
    r_2 = k + P,
    P = p + q.

The external antichiral field carries q.
The external X field carries p.
The translated insertion leg carries r_2.

The three propagators must produce

    1 / [ k^2 (k+q)^2 (k+P)^2 ].

The right-acting translation produces

    exp(i w dot r_2).

At the two cubic vertices derive, rather than assume, the derivative-difference
momenta. The canonical checkpoint is

    L_1 = r_0 + r_1 = 2k + q,

    L_2 = r_1 + r_2 = 2k + p + 2q.

The noncollapsed triangle numerator should reduce to a three-sigma chain of
the form

    T_{mu rho nu,+}^{dot alpha}
    L_1^mu p^rho L_2^nu,

where

    T_{mu rho nu,+}^{dot alpha}
      =
    (sigma_mu barsigma_rho sigma_nu)_+^{dot alpha}.

Derive the overall coefficient independently. Do not insert it from an
expected result.

======================================================================
VIII. D-ALGEBRA PROCEDURE
======================================================================

The D-algebra is the main deliverable. Do not hide any part behind phrases such
as "after D-algebra" or "after straightforward algebra."

Use edge-tagged derivatives. For example,

    D_i^[ij]

means D at endpoint i acting only on the propagator joining i and j.

Required procedure:

1. Expand both derivative-difference cubic vertices into their endpoint terms.
2. Expand both possible placements of nabla_- on the two insertion letters.
3. Produce an explicit contraction table. For the triangle there should be
   four endpoint combinations times two nabla_- placements before further
   reductions.
4. For every row, display:
   - the original derivative word;
   - all endpoint-transfer signs;
   - use of D_i delta_ij = -D_j delta_ij;
   - mixed anticommutators;
   - closed Grassmann-loop saturation;
   - whether a Box cancels a propagator;
   - whether the term is EOM, chiral-zero, longitudinal, finite, or anomalous.
5. Never use D_+^2 = 0 across derivatives that are still tagged to different
   propagators.
6. Move derivatives to external fields only after their edge assignment and
   Grassmann signs are fixed.
7. Apply chirality and EOM identities only after the derivative path is
   explicit.
8. Keep the sigma-matrix order. Do not prematurely use a Fierz identity that
   erases the distinction between g_(4) and ghat.

Split the result into:

    Gamma_triangle
      =
    Gamma_3-denominator
    + Gamma_collapsed
    + Gamma_EOM
    + Gamma_longitudinal.

The collapsed part belongs to the SD contact family and must not be discarded.

======================================================================
IX. FEYNMAN PARAMETERS AND THE ORDERED KERNEL
======================================================================

Once the numerator has been completely derived, parameterize

    1 / (D_0 D_1 D_2)

with simplex variables x,y,z, x+y+z=1.

Then change variables to ordered parameters

    a = x,
    b = x + y,

so that

    0 <= a <= b <= 1.

After shifting the loop momentum, verify

    r_2 = ell + b p + a q,

and hence

    exp(i w dot r_2)
      =
    exp(i w dot ell)
    exp(i w dot (a q + b p)).

Keep the final ordered Feynman-parameter integral unevaluated where useful.

Define the ordered kernel

    K_w[F(q),G(p)]
      =
    2 integral_0^1 db integral_0^b da
      exp(i w dot (a q + b p))
      F(q) G(p).

In position-space notation this becomes

    K_w[F,G]
      =
    2 integral_0^1 db integral_0^b da
      (T_a F)(T_b G).

======================================================================
X. LOOP-NUMERATOR DECOMPOSITION
======================================================================

After the shift write

    L_1 = 2 ell + A,
    L_2 = 2 ell + B.

Derive the moments with exp(i w dot ell) using Schwinger parameters. Do not
assume them.

Decompose the numerator integral into the independent tensor sectors

    ghat^{mu nu} J_2,

    w^mu B^nu J_2,

    A^mu w^nu J_2,

    w^mu w^nu J_1,

    A^mu B^nu J_3.

Classify them as follows, verifying every claim:

1. ghat^{mu nu} J_2:
   the logarithmic metric pole and the only candidate for the chiral anomaly.

2. w-longitudinal J_2 terms:
   ordinary covariant-link renormalization. Show their cancellation against
   T_1^(1) and related link/contact graphs using the eikonal identity

       i w dot (r-r')
       integral_0^1 ds
         exp(i s w dot r)
         exp(i (1-s) w dot r')
       =
       exp(i w dot r) - exp(i w dot r').

3. w^mu w^nu J_1:
   power/contact sector. Determine explicitly whether it vanishes under the
   chosen holomorphic spinor projection or is cancelled by link seagulls.

4. A^mu B^nu J_3:
   UV-finite nonlocal form factor, not part of the anomaly.

Do not discard a term merely because it is not anomalous. Record where it goes.

======================================================================
XI. SCHWINGER-DYSON CANCELLATION
======================================================================

Compute the ordinary UV pole of the isolated triangle.

It must be displayed before any cancellation.

The tensor reduction of the loop momentum gives a pole proportional to

    ghat^{mu nu} J_2.

Independently derive the sum of nonlinear-letter, quartic, collapsed, and link
contact graphs. Their four-dimensional D-algebra metric structure must be
displayed explicitly and should give the corresponding pole proportional to

    -g_(4)^{mu nu} J_2,

plus longitudinal and EOM sectors.

Then show graph by graph that the ordinary physical UV pole cancels:

    ghat^{mu nu} J_2 - g_(4)^{mu nu} J_2
      =
    -gtilde^{mu nu} J_2.

Only at this stage perform the four-dimensional sigma contraction

    gtilde^{mu nu}
    (sigma_mu barsigma_rho sigma_nu)
    p^rho.

Use

    tr gtilde = 2 epsilon

and

    J_2 |_pole = 1 / (16 pi^2 epsilon)

in the repository's normalization.

This finite evanescent remainder is the anomaly.

The calculation must explicitly demonstrate:

    isolated triangle = UV divergent;

    complete SD graph family = ordinary UV finite;

    finite anomaly = failure of the regularized cutting rule.

======================================================================
XII. FINAL RESULT FORMAT
======================================================================

Give both fixed-orientation and reflected-orientation answers.

The final anomaly should be written in an ordered Feynman-parameter form

    A_w^{AB}
      =
    c g^2 f^{ACD} f^{BCE}
    integral_0^1 db integral_0^b da
    [
      (T_a bar W^D_dot alpha)
      (T_b nabla_+^{dot alpha} X^E)

      -

      (T_a nabla_{+ dot alpha} X^D)
      (T_b bar W^{E dot alpha})
    ],

where c must be derived from the graph calculation.

As a regression check only, in the current convention set the expected value
is

    c = 1 / (8 pi^2).

Do not use this value to determine any intermediate normalization.

Also provide the momentum-space form with

    exp(i w dot (a q + b p)).

======================================================================
XIII. REQUIRED CHECKS
======================================================================

Implement and document these checks:

1. w -> 0 reproduces the corresponding local two-letter anomaly.
2. The ordered kernel satisfies

       2 integral_0^1 db integral_0^b da = 1.

3. Expanding in descendants gives

       K_w[F,G]
         =
       2 sum_{m,n >= 0}
         (D_w^m F)(D_w^n G)
         /
         [m! n! (m+1)(m+n+2)].

4. All ordinary 1/epsilon poles cancel in the SD-complete graph family.
5. No epsilon factor occurs in the bare triangle numerator.
6. The only finite rational anomaly originates from

       (g_(4) - ghat) / epsilon.

7. The final result is background-gauge covariant.
8. EOM, total-derivative, scheme-dependent contact, and genuinely anomalous
   structures are reported separately.
9. The reflected orientation has the correct color and Grassmann signs.
10. Every diagram in the document has a machine-readable graph ID matching
    its amplitude and D-algebra trace.

======================================================================
XIV. DELIVERABLES
======================================================================

Adapt paths to the repository conventions, but produce the equivalents of:

- a convention ledger;
- a publication-readable LaTeX derivation;
- a concise Markdown overview;
- machine-readable graph definitions;
- a table of every Wick contraction;
- a complete D-algebra trace for every graph;
- symbolic expressions for all numerators;
- Feynman-parameter forms of all amplitudes;
- rendered diagrams in PDF and SVG;
- unit tests for signs, symmetry factors, denominators, phases, color factors,
  and limiting cases;
- a script or notebook that regenerates all formulas and figures;
- a final report listing commands run and their results.

Generated formulas and figures must be reproducible. Do not leave any result
that depends on manual editing.

Prompt B：Supergraph renderer、Wick-contraction skeleton 与 graph-to-amplitude compiler

这一段专门让 Codex 构造图形系统、生成 super Feynman diagrams，并将图自动转化成 amplitude。

Build a reproducible supergraph representation, renderer, and graph-to-amplitude
pipeline for the one-loop N=1 SYM calculation already defined in this
repository.

This is not merely a request for pretty diagrams. The diagram must be the
machine-readable source of:

- momentum routing;
- propagator denominators;
- color contractions;
- Wick-contraction multiplicities;
- derivative endpoint assignments;
- Grassmann signs;
- translation phases;
- D-algebra words;
- collapsed-propagator descendants;
- Schwinger-Dyson cutting relations;
- final tensor numerators.

The same graph ID must connect the rendered figure, Wick-contraction table,
D-algebra trace, and amplitude.

======================================================================
I. INSPECT AND INTEGRATE
======================================================================

First inspect the current repository:

- AGENTS.md;
- diagram-generation tools;
- LaTeX/TikZ setup;
- Python/Julia/Mathematica/SymPy infrastructure;
- CI;
- generated-artifact policy;
- existing notation.

Use the existing workflow wherever possible.

Prefer a deterministic text-based source format and publication-quality vector
output. TikZ-Feynman or a custom TikZ layer is preferred for the publication
figures. SVG output must also be available.

Do not require manual repositioning after generation.

======================================================================
II. GRAPH INTERMEDIATE REPRESENTATION
======================================================================

Create a typed, machine-readable graph IR.

A graph must contain at least:

Graph:
    id
    perturbative_order
    orientation
    source_expression
    symmetry_factor
    wick_multiplicity
    global_grassmann_sign
    color_factor
    insertion_phase
    sd_parent
    sd_descendants
    nodes
    ports
    edges
    external_legs
    metadata

Node:
    id
    type
    superspace_coordinate
    vertex_rule
    color_indices
    spinor_indices
    position_hint
    source_term

Required node types:

- composite insertion I_(2);
- nonlinear-letter insertion I_(3);
- cubic chiral vertex;
- cubic antichiral vertex;
- quartic action vertex;
- collapsed/contact vertex;
- one-link translation vertex;
- two-link/seagull translation vertex;
- external W;
- external bar W;
- external X.

Port:
    id
    node_id
    field_type
    color_index
    spinor_index
    grassmann_parity
    derivative_word
    derivative_target
    incoming_or_outgoing

Edge:
    id
    endpoint_ports
    field_type
    momentum_symbol
    momentum_orientation
    propagator_denominator
    theta_delta
    color_delta
    translated
    phase
    cuttable

Derivatives must remain edge-tagged. For example:

    D(alpha, endpoint=i, edge=e_01)

and

    Dbar(dot_alpha, endpoint=j, edge=e_12).

Do not represent D-operators as commuting symbols.

======================================================================
III. GRAPH CATALOGUE
======================================================================

Generate the complete order-g^2 graph catalogue.

At minimum include:

1. Triangle T_A|B
   - A-letter connected to the antichiral vertex;
   - translated B-letter connected to the chiral vertex.

2. Reflected triangle T_B|A.

3. Both placements of nabla_- on the insertion letters.

4. All four derivative endpoint assignments at the two cubic vertices.

5. Nonlinear-letter bubble graphs from X_(2).

6. Outer-covariant-derivative connection graphs.

7. Quartic/contact bubbles from S_(4).

8. Every collapsed-propagator graph generated by triangle D-algebra.

9. One-link graphs from the first Duhamel term of exp(w dot nabla).

10. Two-link/link-seagull graphs from the second Duhamel term.

11. Reflected versions of all non-self-reflected graphs.

12. Tadpoles and counterterm graphs, even when later shown to vanish.

Do not identify graphs solely by topology. Two supergraphs with the same
ordinary topology but different derivative ports are distinct until D-algebra
proves them equivalent.

======================================================================
IV. REQUIRED TRIANGLE FIGURE
======================================================================

Render the fixed-orientation triangle with:

- the composite insertion at the bottom;
- bar W^D_dot alpha(q) at the upper-left vertex;
- W_+^E(p) at the upper-right vertex;
- internal line labels

      r_0 = k,
      r_1 = k + q,
      r_2 = k + p + q;

- color labels A, B, C, D, E;
- the translated insertion leg visibly marked by

      exp(i w dot r_2);

- the cubic derivative rules displayed near the vertices:

      Dbar_C - Dbar_A,

      D_C - D_B;

- the composite insertion operator

      D_- [ K_+ v^A exp(w dot partial) K_+ v^B ];

- the color factor

      f^{ACD} f^{BCE};

- a stable graph ID such as T-Abar-BW-01.

Produce two versions:

1. a clean publication version;
2. an annotated audit version showing ports, derivative directions, and
   endpoint IDs.

======================================================================
V. WICK-CONTRACTION ENUMERATOR
======================================================================

Implement a port-preserving Wick-contraction enumerator.

For each graph:

1. Match compatible quantum-field ports.
2. Apply color deltas.
3. retain the orientation of each propagator;
4. compute the Wick multiplicity;
5. compute Grassmann signs from the actual permutation;
6. avoid quotienting by graph isomorphism before port labels and derivative
   assignments are included;
7. canonicalize only after all physical labels are retained.

For the fixed triangle, explicitly generate the four endpoint combinations

    (r_0,r_1),
    (r_0,r_2),
    (r_1,r_1),
    (r_1,r_2),

and multiply these by the two possible placements of D_-.

Export the resulting eight-term table in:

- machine-readable JSON;
- CSV;
- Markdown;
- LaTeX.

Each row must contain:

    contraction ID,
    D_- placement,
    Dbar endpoint,
    D endpoint,
    raw derivative word,
    sign,
    momentum numerator,
    collapsed edge if any,
    classification.

======================================================================
VI. SYMBOLIC D-ALGEBRA ENGINE
======================================================================

Implement a small exact noncommutative D-algebra engine, or extend the
repository's existing symbolic engine.

Required symbolic objects:

- D_alpha;
- Dbar_dot alpha;
- D^2;
- Dbar^2;
- theta delta functions;
- edge momenta p_{alpha dot alpha};
- Box(edge);
- sigma and barsigma chains;
- external superfields with chirality properties;
- EOM markers;
- color tensors;
- covariant-translation phases.

Required rules:

1. Endpoint transfer:

       D_i delta_ij = -D_j delta_ij,

       Dbar_i delta_ij = -Dbar_j delta_ij.

2. Anticommutation of same-chirality derivatives.

3. Mixed anticommutator:

       {D_alpha, Dbar_dot alpha}
         =
       convention-dependent momentum operator.

4. Closed-loop saturation, with the normalization taken from the convention
   ledger.

5. Identities such as

       D^2 Dbar^2 D^2 = 16 Box D^2,

   with all signs derived from the selected convention.

6. Propagator collapse:

       Box(edge) / momentum(edge)^2 -> 1,

   producing a new contact graph rather than silently deleting the factor.

7. External chirality rules.

8. EOM classification.

9. Nilpotency only after edge tags permit it.

10. Exact rational arithmetic for all numerical factors.

The engine must emit a step-by-step trace, not merely a simplified result.

A trace must look schematically like:

    initial derivative word
      -> transfer D from endpoint 1 to endpoint 2
      -> sign -1
      -> commute Dbar past D
      -> mixed anticommutator gives r_1
      -> closed D-loop gives factor 16
      -> Box(r_0) cancels propagator e_01
      -> classify as collapsed contact graph C-coll-01.

======================================================================
VII. GRAPH-TO-AMPLITUDE COMPILER
======================================================================

For each graph, generate its amplitude by the following deterministic
algorithm:

1. Solve momentum conservation from the oriented incidence matrix.
2. Assign one independent loop momentum per loop.
3. Multiply propagators.
4. Multiply vertex factors.
5. multiply the composite-insertion factor;
6. multiply translation phases;
7. contract color indices;
8. enumerate Wick contractions;
9. perform edge-tagged D-algebra;
10. separate noncollapsed and collapsed terms;
11. convert mixed D-Dbar anticommutators into momentum bispinors;
12. preserve sigma-matrix order;
13. classify the resulting terms;
14. output both bispinor and Lorentz-tensor forms.

For the fixed triangle, the pipeline must derive the checkpoint

    denominator:
      k^2 (k+q)^2 (k+p+q)^2;

    phase:
      exp(i w dot (k+p+q));

    vertex momenta:
      L_1 = 2k + q,
      L_2 = 2k + p + 2q;

    spinor chain:
      (sigma_mu barsigma_rho sigma_nu)_+^{dot alpha}
      L_1^mu p^rho L_2^nu.

The overall coefficient must be computed by the pipeline from:

- interaction-expansion coefficient;
- symmetry factor;
- Wick multiplicity;
- insertion factors;
- closed D-loop factor;
- vertex factors.

Do not hard-code the overall coefficient.

======================================================================
VIII. CUTTING-RULE OPERATOR
======================================================================

Implement an explicit Schwinger-Dyson cutting operation C_SD on the graph IR.

C_SD must:

1. identify an EOM/inverse-propagator insertion adjacent to a propagator;
2. replace the inverse kinetic operator times propagator by a superspace delta;
3. remove the cut edge;
4. merge or reconnect the appropriate superspace endpoints;
5. transfer remaining derivative operators;
6. preserve color and Grassmann signs;
7. generate the corresponding nonlinear-letter/contact graph;
8. record the parent-child relation.

The graph database should therefore contain SD orbits:

    parent triangle
        -> collapsed triangle descendants
        -> nonlinear-letter bubbles
        -> quartic/contact completions
        -> link/contact completions.

Render the following noncommuting-square diagram:

          Gamma_parent  -- C_SD -->  Gamma_cut
              |                         |
          R_epsilon                 R_epsilon
              |                         |
              v                         v
       R_epsilon Gamma_parent  --?--> R_epsilon Gamma_cut

Label the failure of the square to commute by

    A = [C_SD, R_epsilon] Gamma_parent.

This diagram is conceptually as important as the Feynman diagrams.

======================================================================
IX. DRED-AWARE TENSOR REDUCTION
======================================================================

Represent separately:

    g4(mu,nu),
    ghat(mu,nu),
    gtilde(mu,nu).

Never simplify them into one metric.

The D-algebra engine produces g4.
The d-dimensional loop tensor integral produces ghat.

For example, the tensor reduction must retain

    integral d^d ell
      ell^mu ell^nu / (ell^2 + Delta)^3
      =
    ghat^{mu nu} times scalar integral.

The contact graph produced by four-dimensional D-algebra must retain
g4^{mu nu}.

Only after summing the SD graph family may the system form

    ghat^{mu nu} - g4^{mu nu}
      =
    -gtilde^{mu nu}.

The sigma contraction with gtilde must be performed using the four-dimensional
sigma identity. There is no independent evanescent sigma algebra.

Generate an audit message if any code path replaces g4 by ghat before the
graph-family sum.

======================================================================
X. TRANSLATION/LINK SECTOR
======================================================================

Represent exp(w dot nabla) through ordered Duhamel vertices.

The graph IR must store ordered parameters a,b,... for link insertions.

Implement the identity

    i w dot (r-r')
    integral_0^1 ds
      exp(i s w dot r)
      exp(i (1-s) w dot r')
      =
    exp(i w dot r) - exp(i w dot r').

Use it to match the w-longitudinal parts of the triangle numerator to
one-link and endpoint graphs.

The code must not simply delete w-longitudinal terms. It must identify the
specific graph or graph sum that cancels each term.

For two ordered parameters, use

    0 <= a <= b <= 1.

After Feynman parameterization, verify that the translated line phase becomes

    exp(i w dot ell)
    exp(i w dot (a q + b p)).

Keep the external ordered phase in the final amplitude.

======================================================================
XI. TERM CLASSIFICATION
======================================================================

Every output term must have exactly one primary classification:

- ANOMALY_CANDIDATE_METRIC_POLE;
- ORDINARY_UV_POLE;
- W_LONGITUDINAL;
- LINK_WARD_CANCELLATION;
- COLLAPSED_CONTACT;
- EOM;
- CHIRAL_ZERO;
- NILPOTENT_ZERO;
- UV_FINITE_NONLOCAL;
- SCHEME_DEPENDENT_CONTACT;
- TADPOLE_SCALELESS;
- COUNTERTERM;
- UNCLASSIFIED.

Fail the test suite if an order-g^2 term remains UNCLASSIFIED.

The anomaly candidate is not the isolated metric pole. It becomes an anomaly
only after the SD-complete pole cancellation leaves

    (ghat - g4) J_2.

======================================================================
XII. RENDERING SPECIFICATION
======================================================================

Produce deterministic publication-quality diagrams in:

- TikZ source;
- PDF;
- SVG.

Use consistent visual semantics:

- composite insertion: double circle or diamond;
- cubic chiral vertex: filled circle labelled W;
- cubic antichiral vertex: filled circle labelled bar W;
- quartic/contact vertex: square;
- collapsed vertex: crossed or fused node;
- translation/link vertex: small open circle on the translated line;
- translated propagator: double line or line carrying an exp(i w dot r) label;
- cut propagator: dashed line with a cut marker;
- external fields: clearly labelled;
- momentum direction: arrow plus momentum label;
- derivative endpoint: small D or Dbar marker near the relevant port;
- graph ID: printed below each figure.

Do not use layout-dependent edge crossing when a planar routing exists.

Create multi-panel figures for:

1. the two triangle orientations;
2. the eight derivative/Wick assignments;
3. the nonlinear-letter and quartic contact bubbles;
4. the collapsed-propagator descendants;
5. the one-link and two-link graphs;
6. the complete SD orbit;
7. the noncommuting cutting/regularization square.

======================================================================
XIII. PERSISTENT WICK-CONTRACTION SKELETON
======================================================================

For long-term reproducibility, preserve the Wick-contraction skeleton as a
first-class artifact.

For every rendered graph store:

- the original operator/action terms;
- port pairings;
- contraction order;
- derivative endpoint assignments;
- color contractions;
- momentum equations;
- symmetry factor;
- Grassmann sign;
- D-algebra trace;
- amplitude before loop integration;
- amplitude after tensor reduction;
- SD parent and descendants.

Use stable IDs and deterministic serialization so that changes can be reviewed
with ordinary Git diffs.

Generated LaTeX equations must cite these graph and contraction IDs.

Example:

    Equation (T.17) was generated from
      graph T-Abar-BW-01,
      contractions WC-001 through WC-008,
      D-algebra traces DA-001 through DA-008.

======================================================================
XIV. TESTS
======================================================================

Add tests for:

1. graph count at order g^2;
2. expected number of triangle endpoint assignments;
3. momentum conservation on every node;
4. triangle denominator;
5. translated-line phase;
6. color factor f^{ACD} f^{BCE};
7. reflected-orientation signs;
8. exact symmetry factors;
9. D-transfer signs;
10. propagator-collapse descendants;
11. absence of premature D_+^2 simplification;
12. separation of g4, ghat, and gtilde;
13. cancellation of ordinary UV poles;
14. cancellation of w-longitudinal terms by link graphs;
15. w -> 0 reduction;
16. ordered-domain normalization;
17. reproducibility of SVG/PDF/TikZ outputs;
18. no unclassified terms.

Use golden tests for the final pre-integration amplitudes and for the
machine-readable contraction tables.

======================================================================
XV. DELIVERABLES
======================================================================

Adapt names to repository conventions, but produce equivalents of:

    graph_ir/
    graph_catalogue/
    contraction_tables/
    d_algebra_traces/
    amplitudes/
    figures/tikz/
    figures/pdf/
    figures/svg/
    tests/
    docs/

Include a single regeneration command that:

1. rebuilds the graph catalogue;
2. enumerates Wick contractions;
3. performs D-algebra;
4. generates amplitudes;
5. renders diagrams;
6. compiles the derivation document;
7. runs all tests.

End with a report containing:

- files changed;
- commands run;
- generated graph count;
- contraction count;
- all failed or unresolved checks;
- the explicit SD graph families;
- the derived anomaly coefficient;
- confirmation that no epsilon was inserted into the bare triangle.

建议的执行顺序

先运行 Prompt A，让 Codex 固定 conventions、action/operator expansion 和 SD-complete graph inventory；再运行 Prompt B，将该 inventory 编译成 diagram IR、Wick-contraction skeleton、$D$-algebra trace 与 publication figures。这样整个工程的逻辑不是“先画图再猜 amplitude”，而是

$$
\boxed{
\text{operator/action}
\rightarrow
\text{Wick contractions}
\rightarrow
\text{supergraphs}
\rightarrow
D\text{-algebra}
\rightarrow
\text{SD cuts}
\rightarrow
\text{regulated mismatch}
\rightarrow
\text{anomaly}.
}
$$

<!-- END EXACT text_with_tex -->
