# AB/BA unified typed projection and residual-q covariance

For G1 the external slots are

$$
B_1(p),\qquad D(q),
$$

so

$$
(c_p,c_q)_{G_1}
=(c_{\rm pair},c_{\rm EOM})_{G_1}.
$$

The exact replay gives

$$
(c_{\rm pair},c_{\rm EOM})_{G_1}=(2,2).
$$

For G2 the raw graph has the opposite momentum assignment:

$$
D(p)\text{ at }M,
\qquad
B_1(q)\text{ at }H.
$$

Hence

$$
\binom{c_{\rm pair}}{c_{\rm EOM}}_{G_2}
=
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\binom{c_p}{c_q}_{G_2}.
$$

The D-first and B-first words are

$$
\frac13D(q-4p)B_1
=\frac13B_1(4p-q)D.
$$

Therefore

$$
(c_p,c_q)_{G_2}
=\left(\frac43,-\frac13\right),
$$

$$
\boxed{
(c_{\rm pair},c_{\rm EOM})_{G_2}
=\left(-\frac13,\frac43\right).}
$$

For the ordered (B_1>D) slot,

$$
\epsilon^{\dot a\dot b}\epsilon_{\dot a\dot c}
=-\delta^{\dot b}_{\dot c},
$$

therefore

$$
(P^{\dot a}B_1)D_{\dot a}
=-\langle B_1,D\rangle.
$$

Thus

$$
T_{BD}:=P^{\dot a}(B_1D_{\dot a})
=-\langle B_1,D\rangle+B_1(P^{\dot a}D_{\dot a}),
$$

$$
B_1(P\!\cdot D)=\langle B_1,D\rangle+T_{BD}.
$$

Consequently

$$
-\frac13\langle B_1,D\rangle
+\frac43B_1(P\!\cdot D)
=\langle B_1,D\rangle+\frac43T_{BD},
$$

and the exact-divergence quotient gives

$$
\boxed{c_{G_2}=1.}
$$

The transported $\Omega_{21}$ occurrence remains in this result:

$$
P_\Omega=-\frac12\bar L^2W,
\qquad
C_\Omega=+\frac12L_d^2W,
$$

$$
P_\Omega+C_\Omega=-\frac12\mu_\ell^2W.
$$

For G3, the two-axis trace gives the unhalved D-word magnitude $4096$, and
the locked Fourier phase gives

$$
(ip)_+\wedge(iq)_+=-(p_+\wedge q_+).
$$

Thus

$$
G_{3,2}^{\rm typed}=-2i\sqrt2\lambda_1,
\qquad
G_{3,3}^{\rm typed}=+2i\sqrt2\lambda_1.
$$

In the ordered basis

$$
(\langle D,B_1\rangle,\langle B_1,D\rangle,
\langle C_2,C_3\rangle,\langle C_3,C_2\rangle),
$$

the residual-$q$ kernel is

$$
\ker Q=\mathbb C(1,1,-i\sqrt2,+i\sqrt2).
$$

The corrected direct vector is

$$
v_{\rm direct}
=\left(2,1,-2i\sqrt2,+2i\sqrt2\right),
$$

and

$$
Qv_{\rm direct}
=\left(1,0,0\right).
$$

Its four candidate scales are

$$
2,\qquad 1,\qquad 2,\qquad 2.
$$

Thus G2 is exactly on the unit ray after the dotted-divergence quotient.
G1 and G3 retain one common factor two.
