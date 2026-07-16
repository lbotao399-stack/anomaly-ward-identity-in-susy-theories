# HT \(I=1\) epsilon canonicalization and G3 factor-two audit

Status: PASS_HT_EPSILON_ORDERED_AND_CANONICAL_BASES_EXACT__RAW_G32_G33_REMAIN_FACTOR_TWO__NO_HESSIAN_RESCALING.

## 1. Ordered basis

$$
X_{st}^{DE}:=(P_{\dot a}C_s^D)(P^{\dot a}C_t^E),
\qquad
X_{32}^{DE}=-X_{23}^{ED}.
$$

$$
\sum_{J,K}\varepsilon_{1JK}X_{JK}^{DE}
=X_{23}^{DE}-X_{32}^{DE}.
$$

In the basis

$$
\left(\mathbb F^{AB}{}_{DE}X_{23}^{DE},
\mathbb F^{AB}{}_{DE}X_{32}^{DE}\right),
$$

$$
v_{HT}=(-i\sqrt2,+i\sqrt2),
\qquad
v_{raw}=(-2i\sqrt2,+2i\sqrt2)=2v_{HT}.
$$

## 2. Canonical single monomial

$$
\mathbb F^{AB}{}_{ED}=\mathbb F^{BA}{}_{DE},
$$

so

$$
\mathbb F^{AB}{}_{DE}
\left(X_{23}^{DE}-X_{32}^{DE}\right)
=\left(\mathbb F^{AB}{}_{DE}
+\mathbb F^{BA}{}_{DE}\right)X_{23}^{DE}.
$$

In

$$
\left(\mathbb F^{AB}X_{23},\mathbb F^{BA}X_{23}\right),
$$

$$
v_{HT}^{can}=(-i\sqrt2,-i\sqrt2),
\qquad
v_{raw}^{can}=(-2i\sqrt2,-2i\sqrt2).
$$

For \(\mathbb F_+=\mathbb F^{AB}+\mathbb F^{BA}\),

$$
c_{HT,+}=-i\sqrt2,\qquad c_{raw,+}=-2i\sqrt2.
$$

For

$$
\mathbb F_{(AB)}=\frac12
\left(\mathbb F^{AB}+\mathbb F^{BA}\right),
$$

$$
c_{HT,(AB)}=-2i\sqrt2,\qquad c_{raw,(AB)}=-4i\sqrt2.
$$

The ratio is \(2\) in every common basis.  The numerical equality
\(c_{raw,ordered}=-2i\sqrt2=c_{HT,(AB)}\) compares coordinates of
different tensors \(\mathbb F^{AB}\) and \(\mathbb F_{(AB)}\).

In the locked \(SU(2)\) frame,

$$
\mathbb F^{01}{}_{10}=-2,\qquad
\mathbb F^{10}{}_{10}=0.
$$

## 3. Ordered external Hessian

$$
T_{u\phi}=T_{\phi u}=T,
$$

$$
\frac1{2!}\left(T_{u\phi}+T_{\phi u}\right)
=\frac12(T+T)=T.
$$

The raw primitive already contains \(\frac12(1+1)=1\).  Another factor
\(1/2\) would divide the same ordered Hessian orbit twice.

## 4. First false equality

$$
\boxed{\mathbb F^{AB}{}_{ED}
\ne\mathbb F^{AB}{}_{DE}},
\qquad
\boxed{\mathbb F^{AB}{}_{ED}
=\mathbb F^{BA}{}_{DE}}.
$$

Thus raw \(G_{32},G_{33}\) remain exactly twice HT after
canonicalization.

Checks: 42/42 PASS.
