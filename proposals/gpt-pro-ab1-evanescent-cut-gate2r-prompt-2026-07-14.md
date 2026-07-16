# GPT Pro Gate 2R prompt — corrected ordered \(\nabla_-(AB_1)\) anomaly

The previous prompt was invalid because it supplied the parent insertion
\(A^AB_1^B\) but omitted the outer Ward descendant.  Discard every previous
final coefficient and redo the standard one-loop superspace Feynman
calculation target-blindly.

This is a calculation request, not a workflow review.  Do not fit a
holomorphic-twist answer and do not answer with blockers.

Use

$$
\nabla_-(A^AB_1^B)
=(\nabla_-A^A)B_1^B+A^A(\nabla_-B_1^B),
$$

$$
\nabla_-A=-\nabla_+\mathscr E_V-2i(B_s\times C_s),
$$

$$
\nabla_-B_1=-2\mathscr E_{\widetilde1}
-\sqrt2\,\varepsilon_{1st}(C_s\times C_t).
$$

Therefore the four occurrence-tagged descendant terms are

$$
-(\nabla_+\mathscr E_V)^A B_1^B,
\qquad
-2i(B_s\times C_s)^A B_1^B,
$$

$$
-2A^A\mathscr E_{\widetilde1}^{B},
\qquad
-\sqrt2 A^A\varepsilon_{1st}(C_s\times C_t)^B.
$$

Canonical fields and propagators are

$$
V=\sqrt2g\,u,
\qquad
\Phi_r=g\phi_r,
\qquad
\widetilde\Phi_r=g\widetilde\phi_r,
$$

$$
\langle u^Au^B\rangle_E
=-\frac{\hbar\kappa^{AB}}{p_d^2}\delta^4(\theta_{12}),
$$

$$
\langle\phi_r^A\widetilde\phi_s^B\rangle_E
=\delta_{rs}\frac{\hbar\kappa^{AB}}{16p_d^2}
\bar D_1^2D_1^2\delta^4(\theta_{12}).
$$

The leading parent factors are

$$
A_c^{(0)}=-\frac{\sqrt2}{8}D_+\bar D^2D_+u,
\qquad
B_{1,c}^{(0)}=D_+\phi_1.
$$

The action vertices are obtained from the accepted connection expansion.
For the gauge cubic vertex use exactly the six label permutations and the
two displayed derivative placements per chirality; no extra \(N_{VVV}\):

$$
\begin{aligned}
C_+[u_1,u_2,u_3]
={}&\frac{i\sqrt2g}{256}
\sum_{\pi\in S_3}c_{U_{\pi1}U_{\pi2}U_{\pi3}}
\int_+\Big[
\bar D^2(u_{\pi1}D^au_{\pi2})\bar D^2D_au_{\pi3}\\
&\hspace{35mm}
+\bar D^2D^au_{\pi1}\bar D^2(u_{\pi2}D_au_{\pi3})
\Big],
\end{aligned}
$$

with the conjugate antichiral word and coefficient
\(-i\sqrt2g/256\).  The matter-gauge exponent vertex is
\(+\sqrt2gT_U/\hbar\); the antichiral superpotential exponent vertex is
\(-\sqrt2g\varepsilon_{rst}c_{ABC}/\hbar\).

The parent triangle skeletons are

$$
G_1=(I[u,\phi_1],M_1,VVV),
\qquad
G_2=(I[u,\phi_1],M_1,M_1),
$$

$$
G_{3,2}=(I[u,\phi_1],M_2,H_-),
\qquad
G_{3,3}=(I[u,\phi_1],M_3,H_-).
$$

They are not yet anomaly graphs.  For each outer marked branch, retain the
actual inverse-kernel occurrence tag and pair it with its full-dimensional
Schwinger cut and the corresponding nonlinear current/contact term.  An
algebraically visible determinant is not a cut unless it retains such an
occurrence tag.

The regulator identity is

$$
\frac{\bar r_e^{,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\mu_\ell^2=\bar\ell^2-\ell_d^2,
$$

$$
\lim_{\epsilon\to0}\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

If \(\bar r_e^2\) is replaced by \(r_{e,d}^2\), parent minus cut must be
zero pointwise.  No graph-specific \(4-d\) factor is allowed.

Independent exact replay data that your result must explain, not assume:

$$
\begin{array}{c|rrr}
&D_-A\text{ parent}&D_-B_1\text{ parent}&\text{sum}\\ \hline
+\text{ chirality}&3072&-2048&1024\\
-\text{ chirality}&-3072&2048&-1024
\end{array},
$$

which gives the uncut parent traces

$$
-\frac32\lambda_1\langle D,B_1\rangle,
\qquad
+\lambda_1\langle D,B_1\rangle.
$$

The selected-edge residuals of the same twelve words are

$$
(+):\quad R_A(y)=-512y,\quad R_B(y)=+512y,
$$

$$
(-):\quad R_A(y)=+512y,\quad R_B(y)=-512y,
$$

and

$$
2\int_0^1(1-y)y\,dy=\frac13.
$$

Recompute these facts and determine whether any additional occurrence-tagged
\(G_1\) cut/contact survives.  Then compute \(G_2,G_{3,2},G_{3,3}\) and all
Euler/nonlinear contacts in the same way.

Required output:

1. A table for every marked branch with parent \(D\)-word, selected edge,
   full-\(d\) cut, nonlinear contact, \(\mu_\ell^2\) remainder, simplex
   moment, Wick factor, color route, and physical-field conversion.
2. Separate coefficients in the ordered basis

$$
\bigl(
\langle B_1^D,D^E\rangle,
\langle D^D,B_1^E\rangle,
\langle C_3^D,C_2^E\rangle,
\langle C_2^D,C_3^E\rangle
\bigr).
$$

3. A final sum derived only from these Feynman rows.  Do not open or quote
   the holomorphic-twist target in this response.
