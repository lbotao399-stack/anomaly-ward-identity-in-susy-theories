# GPT Pro Gate 2 prompt — exact ordered \(AB_1\) triangles

You are the derivation adversary. This is a standard one-loop superspace
Feynman calculation. Do not answer with blockers, workflow prose, or a fit to
the holomorphic-twist coefficient. Compute the four ordered triangle
families completely, and use the twist row only as an after-check.

Authority context:

- origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66;
- the local branch and your output are non-authority proposals;
- Euclidean exponent: \(Z_E=\int D\Xi\,e^{-S_E/\hbar}\) for direct normalized
  Wick expectation values;
- canonical fields:
  \[
  V=\sqrt2g\,u,\qquad
  \Phi_r=g\phi_r,\qquad
  \widetilde\Phi_r=g\widetilde\phi_r .
  \]

Use direct insertion of the physical ordered composite, so there is no
odd-source derivative ambiguity:

\[
\mathcal O_{\rm phys}^{AB}=g^2\mathcal O_{\rm str}^{AB},
\qquad
\mathcal O_{\rm str}^{AB}=A_c^A B_{1,c}^B .
\]

At zero interaction order,

\[
A_c^{(0),A}
=-\frac{\sqrt2}{8}
\bigl(D_+\bar D^2D_+u\bigr)^A,
\qquad
B_{1,c}^{(0),B}=(D_+\phi_1)^B,
\]

\[
\boxed{
\mathcal O_{\rm phys}^{(0),AB}
=-\frac{g^2}{4\sqrt2}
\bigl(D_+\bar D^2D_+u\bigr)^A
\bigl(D_+\phi_1\bigr)^B .}
\]

The conditional canonical propagators are

\[
\langle u^A u^B\rangle_E
=-\frac{\hbar\kappa^{AB}}{p_d^2}\delta^4(\theta_{12}),
\]

\[
\langle\phi_r^A\widetilde\phi_s^B\rangle_E
=\delta_{rs}
\frac{\hbar\kappa^{AB}}{16p_d^2}
\bar D_1^2D_1^2\delta^4(\theta_{12}),
\]

with the reversed chiral orientation kept as its separately ordered kernel.

The matter cubic derivative and its exponent factor are

\[
C_{M_r}
=-\sqrt2g\,T_U,
\qquad
-\frac1\hbar C_{M_r}
=+\frac{\sqrt2g}{\hbar}T_U .
\]

For adjoint indices,

\[
(T_A)^B{}_C=i\,c_{AC}{}^B .
\]

The antichiral cubic derivative and exponent factor are

\[
C_{H_-}
=+\sqrt2g\,\varepsilon_{rst}c_{ABC},
\qquad
-\frac1\hbar C_{H_-}
=-\frac{\sqrt2g}{\hbar}\varepsilon_{rst}c_{ABC}.
\]

The ordered gauge cubic vertices follow directly from the accepted
connection expansion. With \(u_i=u_i^{U_i}T_{U_i}\), their exact polarized
forms are

\[
\begin{aligned}
C_+[u_1,u_2,u_3]
={}&\frac{i\sqrt2g}{256}
\sum_{\pi\in S_3}c_{U_{\pi1}U_{\pi2}U_{\pi3}}
\int_+\Bigl[
\bar D^2(u_{\pi1}D^au_{\pi2})\,\bar D^2D_au_{\pi3}\\
&\hspace{39mm}
+\bar D^2D^au_{\pi1}\,\bar D^2(u_{\pi2}D_au_{\pi3})
\Bigr],
\end{aligned}
\]

\[
\begin{aligned}
C_-[u_1,u_2,u_3]
={}&-\frac{i\sqrt2g}{256}
\sum_{\pi\in S_3}c_{U_{\pi1}U_{\pi2}U_{\pi3}}
\int_-\Bigl[
D^2(u_{\pi1}\bar D_{\dot a}u_{\pi2})\,D^2\bar D^{\dot a}u_{\pi3}\\
&\hspace{39mm}
+D^2\bar D_{\dot a}u_{\pi1}\,D^2(u_{\pi2}\bar D^{\dot a}u_{\pi3})
\Bigr].
\end{aligned}
\]

Do not introduce an extra \(N_{VVV}\): the \(6\) label permutations and the
two displayed placements are the complete ordered Hessian.

The four Project triangle skeletons are

\[
G_1=(I[u,\phi_1],M_1,\mathcal V_{VVV}),
\qquad
G_2=(I[u,\phi_1],M_1,M_1),
\]

\[
G_{3,2}=(I[u,\phi_1],M_2,H_-),
\qquad
G_{3,3}=(I[u,\phi_1],M_3,H_-).
\]

\(G_{3,2}\) is not the second variation seagull of \(G_2\). It is the
separate flavor-\((2,3)\) triangle shown above.

The regulator identity is already independently proved. The finite
superspace \(D\)-word selects one edge \(e\) and produces
\(\bar r_e^{\,2}\), whereas the Schwinger inverse square is
\(r_{e,d}^{\,2}\):

\[
\frac{\bar r_e^{\,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2 .
\]

\[
\lim_{\epsilon\to0}
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
\]

No graph-specific \(4-d\) factor is allowed.

Required calculation:

1. Expand the direct Wick term for every labeled orientation of
   \(G_1,G_2,G_{3,2},G_{3,3}\), including the exact exponential factorial,
   propagator signs, \(1/16\) chiral projectors, and Wick multiplicities.
2. Perform every superspace \(D\)-word. Show which internal occurrence
   supplies \(\bar r_e^{\,2}\), the residual external spinor derivatives, and
   the exact numerical coefficient before the evanescent integral.
3. Reduce every color route to
   \[
   \mathbb F^{AB}{}_{DE}
   =\kappa^{AU}\kappa^{BV}\kappa^{CC'}
   c_{UCD}c_{VC'E}.
   \]
4. Convert external canonical fields to physical bottom letters
   \(B_1,D,C_2,C_3\), including every power of \(g\).
5. Give the separate graph contributions to the ordered basis
   \[
   \bigl(
   \langle B_1^D,D^E\rangle,\,
   \langle D^D,B_1^E\rangle,\,
   \langle C_3^D,C_2^E\rangle,\,
   \langle C_2^D,C_3^E\rangle
   \bigr).
   \]
6. Only after the calculation, compare with
   \[
   \lambda_1\mathbb F^{AB}{}_{DE}
   \left[
   \langle B_1^D,D^E\rangle
   +\langle D^D,B_1^E\rangle
   +i\sqrt2\langle C_3^D,C_2^E\rangle
   -i\sqrt2\langle C_2^D,C_3^E\rangle
   \right],
   \qquad
   \lambda_1=\frac{\hbar g^2}{16\pi^2}.
   \]

If a mismatch occurs, locate it at one explicit line among source
normalization, action exponent, Wick factor, propagator sign, \(D\)-algebra,
color orientation, or physical-field conversion. Do not repair it by
rescaling the final answer.
