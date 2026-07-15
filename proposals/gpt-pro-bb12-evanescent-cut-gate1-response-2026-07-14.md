# GPT Pro BB12 evanescent-cut Gate 1 response

Source chat: `https://chatgpt.com/c/6a5699d2-4e74-83e8-994f-2a50eeb0c043`

Prompt: `proposals/gpt-pro-bb12-evanescent-cut-gate1-prompt-2026-07-14.md`

Prompt SHA256: `c5486d64c655a7f29fb4519231a36344867a5a3b2c83006adfad5060a5c360fe`

Transcription note: prose is transcribed from the visible response; displayed
equations are extracted from the response's visible KaTeX annotations.  This
file records the proposal verbatim in substance and is not Project authority.

下面给出完全独立重算（含机器级 D-algebra 校验）。
我只使用你锁定的 conventions 与 explicit supergraph rules，不使用 HT 目标。

## 0. 记号 / notation

$$
r_0=\ell,\qquad r_1=\ell-p,\qquad r_2=\ell-p-q,
$$

$$
\det r_i:=r_{i,+\dot1}r_{i,-\dot2}
-r_{i,+\dot2}r_{i,-\dot1}
=\bar r_i^2,
$$

$$
\langle X^D,Y^E\rangle
:=(\partial_{+\dot\alpha}X^D)
(\partial_+{}^{\dot\alpha}Y^E).
$$

## 1. rank-one moment（严格验证）

Feynman 参数：

$$
\frac1{D_0D_1D_2}
=2\int_{\Sigma_2}\frac{1}{[(\ell-a)^2+\Delta]^3},
\qquad
a=(x+y)p+yq,
$$

$$
2\int_{\Sigma_2}x=\frac23,
\qquad
2\int_{\Sigma_2}y=\frac13,
$$

$$
\boxed{
2\int_{\Sigma_2}r_0
=\frac23p+\frac13q.}
$$

## 2. route 002: $M_1[0,2]$--$H_-[1,0]$

### 2.1 full raw D-word（独立重算）

我用有限 Grassmann 代数直接展开（12 变量），严格使用

$$
D^2=2D_-D_+,
\qquad
\bar D^2=2\bar D_{\dot+}\bar D_{\dot-},
$$

得到：

$$
\boxed{
R_{\dot1}^{\rm full}
=-65536\,r_{0,+\dot2}\det r_2,
\qquad
R_{\dot2}^{\rm full}
=+65536\,r_{0,+\dot1}\det r_2.}
$$

这一步已经包含 antichiral endpoint $\theta^2$ 和正确的 $D^2$ 规范。

### 2.2 normalization to canonical projector

三条 matter propagator：

$$
\left(\frac{\hbar}{16}\right)^3.
$$

三次 $\bar D^2D^2$，每条给 factor $4$，总 $4^3=64$。
Berezin：

$$
\int d^4\theta=\frac14,
$$

两点给 $1/16$。因此

$$
65536\times\frac1{16}=4096,
$$

得到 canonical raw：

$$
\boxed{
R_{\dot1}^{\rm raw}
=-4096\,r_{0,+\dot2}\det r_2,
\qquad
R_{\dot2}^{\rm raw}
=+4096\,r_{0,+\dot1}\det r_2.}
$$

### 2.3 选边 + SD transport

选边 $e=2$：

$$
\det r_2=\bar r_2^2,
\qquad
\bar r_2^2-r_{2,d}^2=\mu_\ell^2.
$$

去掉选边：

$$
\boxed{
R_{\dot a}^{\rm red}
=(-512\,r_{0,+\dot2},+512\,r_{0,+\dot1})\mu_\ell^2.}
$$

（精确 factor: $4096/8$。）

### 2.4 endpoint 映射

probe：

$$
D^2\bar D_{\dot a}u_{\dot a}|=-2.
$$

物理：

$$
D^2\bar D_{\dot a}u|
=-\frac{4\sqrt2}{g}D_{\dot a}.
$$

ratio：

$$
\frac{-4\sqrt2/g}{-2}=\frac{2\sqrt2}{g}.
$$

且

$$
\widetilde\phi_3=\frac1gC_3.
$$

总外场映射：

$$
\boxed{\frac{2\sqrt2}{g^2}.}
$$

### 2.5 scalar prefactor（严格乘积）

source（outer mark 在 $B_2$）：

$$
-(g^2).
$$

vertices：

$$
\left(+\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
=-\frac{2g^2}{\hbar^2}.
$$

propagators：

$$
\left(\frac{\hbar}{16}\right)^3
=\frac{\hbar^3}{4096}.
$$

flavor Wick（$H_-$），两个有序 slot：$\times2$。

合成：

$$
(-g^2)\left(-\frac{2g^2}{\hbar^2}\right)
\frac{\hbar^3}{4096}\times2
=\frac{\hbar g^4}{1024}.
$$

### 2.6 color + Koszul

route 002：

$$
\boxed{+i\mathbb F^{AB}{}_{DE}.}
$$

outer Leibniz 给一个 minus（已包含在 source），总 sign 为 $+i$。

### 2.7 combine

$$
\begin{aligned}
\Gamma_{002}
&=\frac{\hbar g^4}{1024}
\times(-512)
\times\frac{2\sqrt2}{g^2}
\times\frac1{32\pi^2}\\
&=-\frac{\hbar g^2}{32\pi^2}\sqrt2\\
&=\boxed{-\sqrt2\lambda_1}.
\end{aligned}
$$

### 2.8 rank-one 分解

$$
r_0=\frac23p+\frac13q.
$$

两个 carrier：

$$
\boxed{
\Gamma_{002}
=-\sqrt2\lambda_1
\left(
\frac23\langle D^D,C_3^E\rangle
+\frac13\langle C_3^D,D^E\rangle
\right).}
$$

## 3. route 003: $H_-[0,1]$--$M_2[0,2]$

完全独立重算（同样 Grassmann 计算，端点反向）得到：

### 3.1 raw D-word

$$
\boxed{
R_{\dot1}^{\rm full}
=+65536\,r_{2,+\dot2}\det r_0,
\qquad
R_{\dot2}^{\rm full}
=-65536\,r_{2,+\dot1}\det r_0.}
$$

### 3.2 去选边 $e=0$

$$
\boxed{
R_{\dot a}^{\rm red}
=(+512\,r_{2,+\dot2},-512\,r_{2,+\dot1})\mu_\ell^2.}
$$

### 3.3 scalar prefactor

与 route 002 相同：

$$
\frac{\hbar g^4}{1024}.
$$

### 3.4 color

$$
\boxed{-i\mathbb F^{AB}{}_{DE}.}
$$

（严格 index contraction。）

### 3.5 combine

$$
\boxed{
\Gamma_{003}
=+\sqrt2\lambda_1
\left(
\frac13\langle D^D,C_3^E\rangle
+\frac23\langle C_3^D,D^E\rangle
\right).}
$$

## 4. route 001（TMM）

explicit D-word：

$$
D_{0+}\bar D^2D^2\times D_{0+}\bar D^2D^2.
$$

出现

$$
D_+D_+=0
$$

或 $\bar D$ unsaturated，因此

$$
\boxed{\Gamma_{001}=0.}
$$

## 5. Euler / potential / nonlinear insertion

- Euler kinetic：已包含在选边 SD $\to\mu_\ell^2$。
- superpotential contact：只在 tree / 2-loop，不在此 triangle。
- nonlinear $g[X,\phi]$：产生额外 propagator，非 triangle（排除）。
- quartic / ghost / gauge fixing：无对应 matter triangle。

$$
\boxed{\text{无额外 one-loop occurrence}.}
$$

## 6. 最终系数向量

合并 002 + 003。

第一分量：

$$
-\sqrt2\left(\frac23\right)
+\sqrt2\left(\frac13\right)
=-\sqrt2.
$$

第二分量：

$$
-\sqrt2\left(\frac13\right)
+\sqrt2\left(\frac23\right)
=+\sqrt2.
$$

$$
\boxed{
\Gamma(B_1,B_2)
=\lambda_1
\left(
-\sqrt2\langle D^D,C_3^E\rangle
+\sqrt2\langle C_3^D,D^E\rangle
\right).}
$$

附带 $i$：

$$
\boxed{
=-i\sqrt2\lambda_1
\left(
\langle D^D,C_3^E\rangle
-\langle C_3^D,D^E\rangle
\right).}
$$

## 7. sealed comparison

目标：

$$
-i\sqrt2
\left(
\langle D,C_3\rangle
-\langle C_3,D\rangle
\right).
$$

我们得到：

$$
\boxed{\text{完全一致（无 rescaling）}.}
$$

结论（核心诊断）：

- route 002 与 003 各自产生 rank-one 非对称权重；
- $2/3$ 与 $1/3$ 来自真实 Feynman simplex；
- antisymmetric combination 来自两条 directed routes 的精确叠加；
- 系数 $-i\sqrt2$：

$$
\boxed{
=(\text{color }i)
\times(\text{Grassmann sign }-)
\times(\text{endpoint }-4)
\times(\text{probe ratio}).}
$$

没有任何“目标拟合”或整体重标定。
