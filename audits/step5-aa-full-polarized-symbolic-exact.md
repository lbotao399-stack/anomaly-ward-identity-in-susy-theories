# Step 5 AA full-polarized symbolic edge/contact audit

Status: `PASS_FULL_POLARIZED_SYMBOLIC_EDGE_DIVISION_AND_INDUCED_CONTACT__TYPED_NORMALIZATION_OPEN`.

No holomorphic-twist coefficient is used.

## 1. Polynomial ring and routing

The complete component replay is evaluated in

$$
\mathbb Q(\sqrt2,i)[\ell_0,\ell_1,\ell_2,\ell_3],
$$

with

$$
p=e_0,qquad q=e_1,qquad
r_0=\ell,quad r_1=\ell-q,quad r_2=\ell-p-q.
$$

The full cubic functional derivative and the fixed-field-strength-slot
Hessian are unequal.  At

$$
\ell=(2,-1,1,3)
$$

the exact normalized components are

$$
N_{\rm full}=6-\frac{19}{2}i,
\qquad
N_{\rm fixed\ strength}=-5.
$$

The JSON artifact stores both complete polynomials and their nonzero
difference.

## 2. Exact selected-edge division

For the two source occurrences,

$$
N_{S,0}=\bar r_0^{,2}Q_0,
\qquad
N_{S,2}=\bar r_2^{,2}Q_2,
$$

with zero polynomial remainders and

$$
\begin{aligned}
Q_0={}&
-\frac12\ell_0^2+i\ell_0\ell_1
+\left(\frac32-i\right)\ell_0
+\frac12\ell_1^2
-\left(1+\frac32i\right)\ell_1
-\frac12+\frac32i,
\end{aligned}
$$

$$
Q_2=
-\frac12\ell_0^2+i\ell_0\ell_1
-\frac12\ell_0
+\frac12\ell_1^2
+\frac i2\ell_1.
$$

Thus

$$
\begin{aligned}
Q_0+Q_2={}&
-\ell_0^2+2i\ell_0\ell_1+\ell_1^2
+(1-i)\ell_0-(1+i)\ell_1
-\frac12+\frac32i,
\end{aligned}
$$

and

$$
\Delta_\ell Q_0=\Delta_\ell Q_2=0.
$$

The earlier affine fit is false as a polynomial identity.  The independent
held-out point

$$
\ell=(3,2,-2,1)
$$

gives

$$
N_{S,0}=-9+27i,
\qquad
N_{S,2}=-40+70i.
$$

## 3. Induced Schwinger contacts

Write

$$
N_{{\rm full},e}=N_{S,e}+L_e
=\bar r_e^{,2}Q_e+L_e.
$$

The same-occurrence derivative-of-action contact is

$$
C_{e,d}:=-L_e-r_{e,d}^{,2}Q_e.
$$

The expanded symbolic identities are exactly

$$
N_{{\rm full},0}+C_{0,d}
=(\bar r_0^{,2}-r_{0,d}^{,2})Q_0
=\mu_\ell^2Q_0,
$$

$$
N_{{\rm full},2}+C_{2,d}
=(\bar r_2^{,2}-r_{2,d}^{,2})Q_2
=\mu_\ell^2Q_2.
$$

Replacing every four-dimensional square by its full-$d$ inverse kernel gives

$$
N_{{\rm full},e}\big|_{\bar r_e^2=r_{e,d}^2}+C_{e,d}=0.
$$

## 4. Finite simplex moments

Use

$$
\ell=L+yq+z(p+q),
$$

$$
2\int_{\Delta_2}1=1,quad
2\int_{\Delta_2}y=2\int_{\Delta_2}z=\frac13,
$$

$$
2\int_{\Delta_2}y^2
=2\int_{\Delta_2}z^2=\frac16,qquad
2\int_{\Delta_2}yz=\frac1{12}.
$$

Since the quadratic traces vanish, the $L$-quadratic integrals cancel
exactly.  The remaining shifted moments are

$$
2\int_{\Delta_2}Q_0=-\frac12+\frac5{12}i,
$$

$$
2\int_{\Delta_2}Q_2=\frac7{12}i,
$$

$$
\boxed{
2\int_{\Delta_2}(Q_0+Q_2)=-\frac12+i.}
$$

Therefore the regulated parent/contact sum is finite and contains only

$$
\frac1{32\pi^2}left(-\frac12+i\right)
$$

in this normalized component frame, before the remaining ordered-sector,
color-reflection, and typed-operator reconstruction.

Checks: `15/15 PASS`.
