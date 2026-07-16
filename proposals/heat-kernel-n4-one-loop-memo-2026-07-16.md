# Heat-kernel ordered-simplex cross-check for the accepted Step-5 result

Status: `VERIFIED_AUXILIARY_LEMMA`.

This memo proves only the scalar heat-kernel, ordered-simplex, and DRED master-integral identities below.  It does not define a regulator on the full N=4 fluctuation complex and does not independently derive the Step-5 anomaly coefficient.  The accepted Project coefficient remains the result of `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`.

## 1. Definitions

Let (s>0), (x\in\mathbb R^4), and

$$
K_s(x)=\frac{1}{(4\pi s)^2}\exp\!\left(-\frac{x^2}{4s}\right).
\tag{HK.1}
$$

For integers (p,q\geq0), define the single ordered-simplex moment

$$
M_{p,q}=\int_0^1db\int_0^bda\,a^p b^q.
\tag{HK.2}
$$

For integers (0\leq k\leq m) and (0\leq\ell\leq n), define

$$
T_{m,n;k,\ell}
=\binom{m}{k}\binom{n}{\ell}
M_{k+\ell,m+n-k-\ell}.
\tag{HK.3}
$$

No factor from a reversed ordering is included in these definitions.

## 2. Gaussian kernel

The one-dimensional identity

$$
\int_{-\infty}^{\infty}
\frac{dx}{\sqrt{4\pi s}}e^{-x^2/(4s)}=1
\tag{HK.4}
$$

gives, by four independent integrations,

$$
\int_{\mathbb R^4}d^4x\,K_s(x)=1,
\qquad
K_s(0)=\frac{1}{16\pi^2s^2}.
\tag{HK.5}
$$

Direct differentiation yields

$$
\partial_sK_s(x)
=K_s(x)\left(-\frac2s+\frac{x^2}{4s^2}\right),
\tag{HK.6}
$$

and

$$
\partial_{x_i}^2K_s(x)
=K_s(x)\left(-\frac1{2s}+\frac{x_i^2}{4s^2}\right).
\tag{HK.7}
$$

Summing (HK.7) over (i=1,2,3,4) proves

$$
\partial_sK_s=\Delta_{\mathbb R^4}K_s.
\tag{HK.8}
$$

For (s,t>0), completion of the square gives

$$
\frac{(x-y)^2}{4s}+\frac{y^2}{4t}
=\frac{s+t}{4st}
\left(y-\frac{t}{s+t}x\right)^2
+\frac{x^2}{4(s+t)}.
\tag{HK.9}
$$

Therefore

$$
\int_{\mathbb R^4}d^4y\,K_s(x-y)K_t(y)=K_{s+t}(x).
\tag{HK.10}
$$

## 3. Three-segment bridge

For (t_1,t_2,t_3>0), (T=t_1+t_2+t_3), and one Cartesian component, use the weight

$$
Q(x,y)
=\frac{(x-w)^2}{4t_1}
+\frac{(y-x)^2}{4t_2}
+\frac{y^2}{4t_3}.
\tag{HK.11}
$$

The stationary equations are

$$
\frac{x-w}{t_1}+\frac{x-y}{t_2}=0,
\qquad
\frac{y-x}{t_2}+\frac{y}{t_3}=0.
\tag{HK.12}
$$

Solving them exactly gives

$$
\langle x\rangle=\frac{t_2+t_3}{T}w,
\qquad
\langle y\rangle=\frac{t_3}{T}w.
\tag{HK.13}
$$

The inverse Hessian of (Q) is homogeneous of degree one under

$$
(t_1,t_2,t_3)\mapsto(\rho t_1,\rho t_2,\rho t_3),
\qquad \rho>0.
\tag{HK.14}
$$

This proves the exact bridge mean and covariance scaling.  It does not remove the endpoint factor (K_T(w)).  In particular, for fixed (w\neq0),

$$
\lim_{s\downarrow0}K_s(w)=0.
\tag{HK.15}
$$

Consequently a local (w)-tower requires distributional coefficient extraction at (w=0); it cannot be obtained by deleting (K_s(w)) before the limit.

## 4. Correct second-order Duhamel coefficient

Let (E\to M) be a fixed graded bundle, let (K_0:E\to E) be an even operator, and let (K_1,K_2:E\to E) be typed even endomorphism-valued differential operators.  Define

$$
K(g)=K_0+gK_1+g^2K_2.
\tag{HK.16}
$$

The coefficient of (g^2) in the semigroup is

$$
\begin{aligned}
[g^2]e^{-sK(g)}
={}&-\int_0^sdt\,
e^{-(s-t)K_0}K_2e^{-tK_0}
\\
&+\int_{0<t_1<t_2<s}dt_1dt_2\,
e^{-(s-t_2)K_0}K_1
e^{-(t_2-t_1)K_0}K_1e^{-t_1K_0}.
\end{aligned}
\tag{HK.17}
$$

The first line is at the same background order as the second line.  Hence a heat-kernel derivation of the physical coefficient must derive the full (K_2) seagull, connection-square, gauge, and ghost blocks; it cannot retain only two labeled (K_1) insertions.

## 5. Ordered-simplex tower

Integrating first over (a),

$$
\begin{aligned}
M_{p,q}
&=\int_0^1db\,b^q\frac{b^{p+1}}{p+1}
\\
&=\frac1{p+1}\frac1{p+q+2}.
\end{aligned}
\tag{HK.18}
$$

Substitution into (HK.3) gives the single-ordering coefficient

$$
T_{m,n;k,\ell}
=\frac{\binom{m}{k}\binom{n}{\ell}}
{(m+n+2)(k+\ell+1)}.
\tag{HK.19}
$$

A factor two may be added only after an independent ordered vertex calculation proves equality of the two orderings, including color order and Koszul sign.  The previous Stage-IV draft instead imposed (V_1^2=V_2^2=0) and hard-coded the second orientation; that draft and its verifier are removed.

The auxiliary factorial identity used in the tower is

$$
\sum_{j=0}^r
\frac{(-1)^j}{(r-j)!(k+j+2)!}
=\frac1{(r+k+2)r!(k+1)!}.
\tag{HK.20}
$$

## 6. DRED master integral

Let (d=4-2\epsilon), and split the four-dimensional metric into the (d)-dimensional loop subspace and its (2\epsilon)-dimensional complement.  Rotational invariance gives

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell^2+\Delta)^3}
=\frac{4-d}{d}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^2}{(\ell^2+\Delta)^3}.
\tag{HK.21}
$$

The radial integral is

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^2}{(\ell^2+\Delta)^3}
=\frac1{(4\pi)^{d/2}}
\frac d2\frac{\Gamma(2-d/2)}{\Gamma(3)}
\Delta^{d/2-2}.
\tag{HK.22}
$$

Using (4-d=2\epsilon), (d/2=2-\epsilon), and

$$
\lim_{\epsilon\to0}\epsilon\Gamma(\epsilon)=1,
\tag{HK.23}
$$

one obtains

$$
\lim_{\epsilon\to0}
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell^2+\Delta)^3}
=\frac1{32\pi^2}.
\tag{HK.24}
$$

This agrees with the accepted DRED master integral.  Equality of this scalar integral does not determine the N=4 operator pairing, color tensor, orientation sign, or anomaly multiplicity.

## 7. Boundary of the verified result

The following claims are not made by this memo:

1. that the Hessian maps back to its own domain without a field-space supermetric;
2. that one blockwise formula defines a single regulator in the presence of off-diagonal mixing;
3. that (K_2) or higher differential insertions vanish;
4. that a fixed nonzero (w) heat kernel produces the local derivative tower;
5. that the dotted pairing, color word, orientation sign, 29/52 census, or absolute coefficient follows from the scalar lemmas.

Thus the scalar identities are verified auxiliary evidence.  A full heat-kernel reconstruction of Step 5 remains `BLOCKED_HEAT_KERNEL_TYPED_REGULATOR_AND_COEFFICIENT_DERIVATION` and cannot replace the accepted Schwinger-cut derivation.
