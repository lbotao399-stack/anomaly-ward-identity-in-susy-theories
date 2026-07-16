# Step 5 ordered (AA) source expansion and complete marked matter orbit

Status: `AA_SOURCE_WORDS_ENUMERATED__MATTER_PHYSICAL_CUT_ASSIGNMENT_REOPENED__GAUGE_SOURCE_ORBIT_OPEN`.

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.

Scope: target-blind Project-side calculation.  This artifact does not use the
holomorphic-twist coefficient.  It fixes the order-$g^2$ source expansion and
records two marked-$D_-$ matter words.  Its former identification of an
algebraic two-determinant decomposition with the physical vector-EOM plus
$-2i(B\times C)$ cut orbit is not accepted.  The matter cut assignment and
the corresponding full pure-gauge source recount remain
`BLOCKED_AA_MATTER_PHYSICAL_CUT_ASSIGNMENT` and
`BLOCKED_AA_GAUGE_FULL_MARKED_OCCURRENCE_RECOUNT`.

Every coefficient in Section 5 has status `CANDIDATE_NOT_ACCEPTED`.

## 1. Canonical source words

Set

$$
X:=D_+u,
\qquad
C:=Xu-uX,
\qquad
E:=Xu^2-2uXu+u^2X,
$$

$$
Y:=\bar D^2X,
\qquad
Z:=\bar D^2C,
\qquad
H_u:=\bar D^2E.
$$

The canonical letter is

$$
A_c=A_1+gA_2+g^2A_3+O(g^3),
$$

$$
A_1=-\frac{\sqrt2}{8}D_+Y,
$$

$$
A_2=-\frac18D_+Z-\frac14(XY+YX),
$$

$$
A_3=-\frac{\sqrt2}{24}D_+H_u
-\frac{\sqrt2}{8}(XZ+ZX+CY+YC).
$$

For the ordered local product

$$
O^{AB}:=A_c^AA_c^B
=O_0^{AB}+gO_1^{AB}+g^2O_2^{AB}+O(g^3),
$$

one has

$$
O_0^{AB}=A_1^AA_1^B,
$$

$$
O_1^{AB}=A_2^AA_1^B+A_1^AA_2^B,
$$

$$
O_2^{AB}=A_3^AA_1^B+A_1^AA_3^B+A_2^AA_2^B.
$$

The outer connection is not optional.  Write

$$
\Gamma_-=g\gamma_1+g^2\gamma_2+O(g^3),
$$

$$
\gamma_1=\sqrt2D_-u,
\qquad
\gamma_2=(D_-u)u-u(D_-u).
$$

For

$$
\mathcal I^{AB}:=
(\nabla_-A_c)^AA_c^B+A_c^A(\nabla_-A_c)^B
=\mathcal I_0^{AB}+g\mathcal I_1^{AB}+g^2\mathcal I_2^{AB}+O(g^3),
$$

the occurrence-resolved expansion is

$$
\begin{aligned}
\mathcal I_0={}&
(D_-A_1^A)A_1^B+A_1^A(D_-A_1^B),
\end{aligned}
$$

$$
\begin{aligned}
\mathcal I_1={}&
(D_-A_2^A)A_1^B+A_2^A(D_-A_1^B)\\
&+(D_-A_1^A)A_2^B+A_1^A(D_-A_2^B)\\
&+[\gamma_1,A_1]^AA_1^B
+A_1^A[\gamma_1,A_1]^B,
\end{aligned}
$$

$$
\begin{aligned}
\mathcal I_2={}&
(D_-A_3^A)A_1^B+A_3^A(D_-A_1^B)\\
&+(D_-A_1^A)A_3^B+A_1^A(D_-A_3^B)\\
&+(D_-A_2^A)A_2^B+A_2^A(D_-A_2^B)\\
&+[\gamma_1,A_2]^AA_1^B+A_2^A[\gamma_1,A_1]^B\\
&+[\gamma_1,A_1]^AA_2^B+A_1^A[\gamma_1,A_2]^B\\
&+[\gamma_2,A_1]^AA_1^B+A_1^A[\gamma_2,A_1]^B.
\end{aligned}
$$

Thus the exact displayed word counts are

$$
N(O_0,O_1,O_2)=(1,2,3),
\qquad
N(\mathcal I_0,\mathcal I_1,\mathcal I_2)=(2,6,12).
$$

## 2. Order-(g^2) resolvent and Wick support

Write

$$
S=S_2+gS_3+g^2S_4+O(g^3).
$$

Expansion of (e^{-S/\hbar}) gives the connected coefficient

$$
\boxed{
\begin{aligned}
\Gamma_{g^2}^{(1)}={}&
\langle\mathcal I_2\rangle_0
-\frac1\hbar\langle\mathcal I_1S_3\rangle_{0,c}
-\frac1\hbar\langle\mathcal I_0S_4\rangle_{0,c}\\
&+\frac1{2\hbar^2}
\langle\mathcal I_0S_3S_3\rangle_{0,c}.
\end{aligned}}
$$

For generic nonzero external momenta the complete support is

| term | connected one-loop support | result before (D)-algebra |
|---|---|---|
| (\mathcal I_2) | one source self-contraction after two background ports are retained | massless tadpole |
| (\mathcal I_1S_{g3}) | one background port at each vertex and two cross edges | gauge bubble |
| (\mathcal I_1S_{m3}) | a bridge plus a source self-contraction for a pure matter output | (\delta(P)) or scaleless tadpole |
| (\mathcal I_0S_{g4}) | two source-to-action edges | gauge contact bubble |
| (\mathcal I_0S_{m4}) | two source-to-action edges | matter seagull bubble |
| (\mathcal I_0S_{g3}S_{g3}) | mixed chiral-antichiral gauge triangle | nonzero parent candidate |
| (\mathcal I_0S_{m3}S_{m3}) | two source attachments and one oriented matter edge | nonzero parent candidate |

The tadpole is zero in dimensional regularization:

$$
\int\frac{d^dk}{(2\pi)^d}\frac{\mu_k^2}{k^2}=0.
$$

The matter seagull numerator is

$$
N_{m4}=4(r_{0+}\wedge r_{2+})=-4(k_+\wedge P_+).
$$

Using

$$
\int_k\frac{k_m}{k^2(k-P)^2}
=\frac{P_m}{2}B_0(P^2),
$$

one obtains exactly

$$
\int_k\frac{N_{m4}}{k^2(k-P)^2}
=-2B_0(P^2)(P_+\wedge P_+)=0,
\qquad
P_+\wedge P_+=0.
$$

## 3. Gauge contact orbit and no double counting

Define

$$
K:=-\frac1{4\sqrt2}D_+\bar D^2D_+.
$$

For one fixed gauge orientation, the occurrence sum of nonlinear-letter,
outer-connection, quartic-action, and collapsed descendants has the unique
contact representative

$$
\boxed{
\begin{aligned}
\mathcal I_{\mathrm{cont}}^{A|B}
={}&\frac g{\sqrt2}c^{BCE}A^E
\left[(D_-Ku^A)u^C-(Ku^A)D_-u^C\right]\\
&+\mathrm{EOM}.
\end{aligned}}
$$

Its separate allocation among (\mathcal I_1S_{g3}),
(\mathcal I_0S_{g4}), outer-(\Gamma_-), and collapsed words changes under
superspace integration by parts.  The tagged occurrence sum does not change.

Let (D_i=r_{i,d}^2).  For every selected inverse-square occurrence,

$$
\frac{D_i}{D_0D_1D_2}
-\frac1{\prod_{j\ne i}D_j}=0.
$$

The gauge parent and its contact descendants therefore obey

$$
\Gamma_{\mathrm{parent}}^{(d)}
+\Gamma_{\mathrm{contact}}^{(d)}=0.
$$

The four-dimensional (D)-word instead gives

$$
\bar L^2=L_d^2+\mu_L^2.
$$

For the already evaluated fixed marked occurrence,

$$
-4\frac{\bar L^2-L_d^2}{D_0D_1D_2}
=-4\frac{\mu_L^2}{D_0D_1D_2}.
$$

Consequently, a result computed as

$$
\Gamma_{\mathrm{parent}}^{(4)}
+\Gamma_{\mathrm{contact}}^{(d)}
$$

already contains (\mathcal I_1S_{g3}) and (\mathcal I_0S_{g4}) through
their SD descendant sum.  Adding those bubbles once more is forbidden:

$$
\boxed{\texttt{NO_DOUBLE_COUNT_PARENT_MINUS_CUT}.}
$$

This no-double-count statement does not settle the gauge coefficient, because
the second marked (D_-) placement and the crossed source attachment have not
yet been recomputed:

$$
\boxed{\texttt{BLOCKED_AA_GAUGE_FULL_MARKED_OCCURRENCE_RECOUNT}.}
$$

## 4. Complete marked matter words

Use

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q,
$$

and write

$$
\mathsf r_i=
\begin{pmatrix}
a_{i+}&b_{i+}\\
a_{i-}&b_{i-}
\end{pmatrix},
\qquad
\det\mathsf r_i=a_{i+}b_{i-}-b_{i+}a_{i-},
$$

$$
W_{ij}:=a_{i+}b_{j+}-b_{i+}a_{j+}.
$$

For fixed external (C^D(q)) at vertex (1) and (B^E(p)) at vertex
(2), the physical bottom maps are

$$
B=D_+\Phi_c\big|_{\theta=0},
\qquad
C=\widetilde\Phi_c\big|_{\theta=0}.
$$

They are represented by

$$
\Phi_c(p,\theta,\bar\theta)
=e^{i\theta p\bar\theta}\theta^+B(p),
\qquad
\widetilde\Phi_c(q,\theta,\bar\theta)
=e^{-i\theta q\bar\theta}C(q).
$$

Thus

$$
D_+\Phi_c\big|_{\theta=0}=B,
\qquad
\widetilde\Phi_c\big|_{\theta=0}=C,
$$

with no extra $\sqrt2$.  The internal chiral line carries

$$
\frac1{16}\bar D^2D^2\delta^4(\theta_1-\theta_2),
$$

and closed saturation gives

$$
\frac1{16}
\left[D^2\bar D^2(\theta^2\bar\theta^2)\right]_{\theta=0}
=\frac1{16}(16)=1.
$$

### 4.1 First marked placement

For the attachment

$$
u_A\longrightarrow v_1(C^D),
\qquad
u_B\longrightarrow v_2(B^E),
$$

marking the first source occurrence gives

$$
\boxed{
\mathcal S_1
=(\det\mathsf r_0)W_{12}
-(\det\mathsf r_1)W_{02}.}
$$

Replacing the two finite spinor squares by their full regulated inverse
squares gives

$$
\mathcal R_1
=\mu_L^2(W_{02}-W_{12}).
$$

With

$$
k=L+yq+z(p+q),
$$

odd (L) terms vanish and

$$
\boxed{
\mathcal R_1
=(1-z)\mu_L^2(p_+\wedge q_+).}
$$

### 4.2 Second marked placement

Marking the second source occurrence gives the distinct word

$$
\boxed{
\mathcal S_2
=W_{01}
\left(a_{2+}b_{1-}-a_{1-}b_{2+}\right).}
$$

It is not a copy of $\mathcal S_1$.  Define

$$
\Omega_{21}
:=a_{2+}b_{1-}-a_{1+}b_{2-}
-b_{2+}a_{1-}+b_{1+}a_{2-}.
$$

Direct expansion gives

$$
\begin{aligned}
2\left(a_{2+}b_{1-}-a_{1-}b_{2+}\right)
={}&\det\mathsf r_1+\det\mathsf r_2
-\det(\mathsf r_1-\mathsf r_2)\\
&+\Omega_{21}.
\end{aligned}
$$

The determinant part selects the $r_1$ and $r_2$ SD cuts.  It gives

$$
\mathcal R_{2,\det}
=-\mu_L^2W_{01}
=z\mu_L^2(p_+\wedge q_+)
+\text{odd in }L.
$$

The $W_{01}\Omega_{21}$ product has a symmetric rank-two loop part; it is
not removable as an antisymmetric tensor.  The exact finite $2\times2$
spinor reduction and its matching mixed collapsed descendant give

$$
\mathcal R_{2,\Omega}
=-\frac12\mu_L^2(p_+\wedge q_+).
$$

Therefore

$$
\boxed{
\mathcal R_2
=\left(z-\frac12\right)
\mu_L^2(p_+\wedge q_+).}
$$

This line distinguishes the scalar determinant cuts from the finite
$2\times2$ identity.  Replacing only the displayed determinants and
discarding $W_{01}\Omega_{21}$ is not the full $D$-word.

### 4.3 General marked sum

Before choosing an external frame, direct polynomial expansion gives

$$
\boxed{
\begin{aligned}
\mathcal S_1+\mathcal S_2
={}&W_{12}
\left[
a_{0+}(b_{0-}-b_{1-})
-b_{0+}(a_{0-}-a_{1-})
\right].
\end{aligned}}
$$

Since $r_0-r_1=q$ and $r_1-r_2=p$, its UV-leading rank-two part is

$$
(p_+\wedge L_+)(L_+\wedge q_-).
$$

The four-dimensional spinor trace and full-$d$ inverse-kernel trace cancel
under the Schwinger identity.  Their DRED difference is equivalently

$$
\boxed{
\mathcal R_1+\mathcal R_2
=\frac12\mu_L^2(p_+\wedge q_+).}
$$

No identification $\bar L^2=L_d^2$ has been used.  In the nondegenerate
frame $p=e_1$, $q=e_4$, the exact diagonal coefficients are

$$
\begin{aligned}
[\mathcal S_1]_{L_m^2}
&=i(3z-1,z-1,z-1,z+1),\\
[\mathcal S_2]_{L_m^2}
&=i(1-3z,1-z,-z,-z).
\end{aligned}
$$

Hence the two evanescent-direction traces are

$$
2i(z-1),
\qquad
i(1-2z),
$$

and their sum is the unique covariant coefficient of
$p_+\wedge q_+$.  This frame calculation is an exact coefficient extraction,
not an external-target match.

## 5. Candidate coefficient under the unaccepted two-determinant assignment

The exact simplex moments are

$$
2\int_{\Sigma_2}(1-z)=\frac23,
$$

$$
2\int_{\Sigma_2}\left(z-\frac12\right)=-\frac16,
$$

$$
2\int_{\Sigma_2}\frac12=\frac12.
$$

Using

$$
\int\frac{d^dL}{(2\pi)^d}
\frac{\mu_L^2}{(L^2+\Delta)^3}
=\frac1{32\pi^2},
$$

and the normalized parent factor $4\hbar g^2$, the two marked placements
give

$$
4\hbar g^2\left(\frac23\right)\frac1{32\pi^2}
=\frac43\lambda_1,
$$

$$
4\hbar g^2\left(-\frac16\right)\frac1{32\pi^2}
=-\frac13\lambda_1.
$$

Under that unaccepted assignment, their algebraic sum is

$$
\boxed{\texttt{CANDIDATE\_NOT\_ACCEPTED}:\quad
4\hbar g^2\left(\frac12\right)\frac1{32\pi^2}
=\lambda_1.}
$$

Therefore the former $4\lambda_1/3$ result is

$$
\boxed{\texttt{RETRACTED_SINGLE_MARKED_PLACEMENT}.}
$$

The second source attachment is

$$
u_A\longrightarrow v_2(B^E),
\qquad
u_B\longrightarrow v_1(C^D).
$$

Its color route is

$$
\mathbb F^{BA}{}_{DE}
=\mathbb F^{AB}{}_{ED}.
$$

After $D\leftrightarrow E$, the same raw momentum wedge is read as the
opposite ordered output because

$$
q_+\wedge p_+=-p_+\wedge q_+.
$$

Thus the former candidate four-row matter orbit was

$$
\boxed{\texttt{CANDIDATE\_NOT\_ACCEPTED}:\quad
\Gamma_{AA,M}^{AB}
=\lambda_1\mathbb F^{AB}{}_{DE}
\sum_{r=1}^3
\left[
\langle B_r^D,C_r^E\rangle
-\langle C_r^D,B_r^E\rangle
\right].}
$$

The displayed coefficient is only the result of the recorded algebraic cut
assignment.  It is not a physical Project coefficient until the explicit
vector-EOM and $-2i(B\times C)$ contact words reproduce that assignment.

## 6. Executable check

Run

```text
python scripts/step5_aa_source_sd_orbit_exact_audit.py
```

The checker verifies the $O_i$ and $\mathcal I_i$ word counts, resolvent
signs, full-square pointwise identities, matter polynomial identities, both
recorded rank-two tensors, the $1/16\times16$ normalization, bubble zeros,
and the conditional $4/3-1/3=1$ arithmetic.  It does not certify the physical
cut assignment.
