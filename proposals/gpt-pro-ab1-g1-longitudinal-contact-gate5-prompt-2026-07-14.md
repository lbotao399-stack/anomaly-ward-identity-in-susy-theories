# GPT Pro Gate 5: AB/BA $G_1$ longitudinal contact transport

Work target-blind.  Do not use a holomorphic-twist coefficient, compact-kernel coefficient, or any previously reported integrated $G_1$ coefficient.

The physical leading source insertion is

$$
\mathcal O_{\rm phys}^{(0),AB}
=-\frac{g^2}{4\sqrt2}
\bigl(D_+\bar D^2D_+u\bigr)^A
\bigl(D_+\phi_1\bigr)^B.
$$

The outer descendant is applied before source-coordinate saturation:

$$
D_-\bigl(A B_1\bigr)=(D_-A)B_1+A(D_-B_1).
$$

The cubic gauge Hessian is the raw $p+q+r+s=1$ part of

$$
\begin{aligned}
S_+^{\rm g}={}&
\sum_{p,q,r,s\ge0}
\frac{\eta(-1)^{p+r}f_{AB}}
{256p!q!r!s!(p+q+1)(r+s+1)}\\
&\quad\times\int_+
\left[\bar D^2(V^pD^aV V^q)\right]^A
\left[\bar D^2(V^rD_aV V^s)\right]^B,
\end{aligned}
$$

and its antichiral conjugate.  After labeled differentiation this is the $12$-row polarization

$$
\sum_{\pi\in S_3}c_{U_{\pi1}U_{\pi2}U_{\pi3}}
\left[
\bar D^2(u_{\pi1}D^au_{\pi2})\bar D^2D_au_{\pi3}
+\bar D^2D^au_{\pi1}\bar D^2(u_{\pi2}D_au_{\pi3})
\right]
$$

per chirality.  The triangle edges are

$$
r_0=\ell,
\qquad r_1=\ell-p,
\qquad r_2=\ell-p-q,
\qquad D_e=r_{e,d}^2.
$$

An independent sparse-Grassmann replay has now proved, row by row for both chiralities and all $S_3\times\{QL,LQ\}$ words,

$$
F_A-L_A=-8\bar r_2^2R_A,
\qquad
F_B=-8\bar r_0^2R_B,
$$

where

$$
L_A=-\frac12D_+\bar D^2D^2(\mathcal V_{VVV})
$$

is evaluated inside the complete source/matter/end-point Berezin word.  For example, at

$$
\ell=(2,1,-1,3),\quad p=(1,0,0,0),\quad q=(0,0,0,1),
$$

one has $\bar r_2^2=7$ and every nonzero row satisfies

$$
\frac{F_A-L_A}{R_A}=-56=-8\bar r_2^2.
$$

The selected $r_2$ and $r_0$ residues cancel after exact normalization.  Therefore the unresolved anomaly is precisely the transported orbit of $L_A$.  A global four-dimensional metric trace of $L_A$ is forbidden: it does not identify which Schwinger contact is being subtracted.

The nonlinear source words needed for contact matching begin with

$$
A_1=-\frac{\sqrt2}{8}D\bar D^2(Du),
$$

$$
A_2=-\frac18D\bar D^2\bigl((Du)u-u(Du)\bigr)
-\frac14\left[(Du)\bar D^2(Du)+\bar D^2(Du)(Du)\right],
$$

$$
B_{11}=D\phi_1,
\qquad
B_{12}=\sqrt2\bigl((Du)\phi_1-\phi_1(Du)\bigr).
$$

The one-loop source resolvent classes carrying the matching collapsed contacts are

$$
R_1=\mathscr G_0I_{[2]},
\qquad
R_2=-\mathscr G_0V_{[1]}\mathscr G_0I_{[1]},
\qquad
R_3=-\mathscr G_0V_{[2]}\mathscr G_0I_{[0]},
\qquad
R_4=+\mathscr G_0V_{[1]}\mathscr G_0V_{[1]}\mathscr G_0I_{[0]}.
$$

Required calculation:

1. Expand the four raw cubic gauge words before using color antisymmetry, then display their collapse to the $12$ labeled rows per chirality.
2. For each of the $24$ rows, keep $(A\hbox{-mark},B\hbox{-mark},L_A)$ separate and reproduce the two displayed edge-square identities.
3. Starting only from $A_1,A_2,B_{11},B_{12}$ and the action Hessians, integrate $L_A$ by parts and name every resulting $R_1/R_2/R_3$ contact occurrence.  Give its exact color word, propagator edge, sign, Taylor factor, and numerator.
4. For each occurrence prove

$$
\frac{r_{e,d}^2R_e}{D_0D_1D_2}
-\frac{R_e}{\prod_{j\ne e}D_j}=0,
$$

then replace only

$$
\bar r_e^2-r_{e,d}^2=\mu_\ell^2.
$$

5. If a collapsed contact still contains a four-dimensional inverse-kernel square, continue the same marked reduction.  Do not stop at an untagged tensor trace.
6. Integrate every final residue with

$$
\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2}{D_0D_1D_2}=\frac1{32\pi^2},
$$

including exact rank-one simplex moments.
7. Compute the reflected $B_1A$ orientation independently.  Seal the two ordered coefficients before any HT comparison.

Do not infer a missing term from a target mismatch.  If an input is insufficient, name the first missing local Hessian or contact kernel after completing every derivable row.
