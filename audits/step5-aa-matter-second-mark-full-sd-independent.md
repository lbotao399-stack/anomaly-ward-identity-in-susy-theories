# Step 5 AA matter second mark: full Schwinger--Dyson orbit

Status:
`SECOND_MARK_FULL_SD_REPAIRED__DISCARDED_LONGITUDINAL_RESIDUAL_WAS_THE_ERROR__TARGET_BLIND_UNIT_MAGNITUDE`.

Scope: fixed-routing second marked source, exact finite-Grassmann (D)-word,
graded endpoint transport, post-transport (r_1) projector collapse,
(Omega_{21}) contact completion, DRED defect, and simplex integral.  No
holomorphic-twist coefficient is used.

## 1. Notation

Write

$$
\mathsf r_i=
\begin{pmatrix}
a_i&b_i\\
c_i&d_i
\end{pmatrix},
\qquad
u_i=(a_i,b_i),
\qquad
v_i=(c_i,d_i),
$$

$$
W_{ij}:=u_i\wedge u_j,
\qquad
\det\mathsf r_i:=a_id_i-b_ic_i.
$$

The locked routing is

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q,
$$

$$
q=r_0-r_1,
\qquad
p=r_1-r_2.
$$

The finite engine convention is

$$
\det\mathsf r=-\bar r^{,2},
\qquad
\bar L^2=L_d^2+\mu_L^2,
\qquad
d=4-2\epsilon.
$$

Define

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

## 2. Exact source-operator split

The second marked source contains

$$
\mathfrak M(r)
:=D_-D_+\bar D^2D_+.
$$

With

$$
D^2=2D_-D_+,
$$

the exact operator identity in the fixed momentum convention is

$$
D^2\bar D^2D_+
=-16(\det\mathsf r)D_+-D_+\bar D^2D^2.
$$

Therefore

$$
\boxed{
\mathfrak M(r)
=-8(\det\mathsf r)D_+
-\frac12D_+\bar D^2D^2.}
$$

The first term is transverse.  The second term is the longitudinal word; it
cannot be removed before its endpoint derivatives are transported.

Acting on the fixed source delta function gives the exact finite-Grassmann
equality

$$
\begin{aligned}
D_{0-}D_{0+}\bar D_0^2D_{0+}\delta^4_{02}
={}&-8(\det\mathsf r_2)D_{0+}\delta^4_{02}\\
&-\frac12D_{0+}\bar D_0^2D_0^2\delta^4_{02}.
\end{aligned}
$$

## 3. Graded endpoint transport

For every odd derivative (Qin\{D_\alpha,\bar D_{\dot\alpha}\}),

$$
Q_0\delta^4_{02}=-Q_2\delta^4_{02}.
$$

The longitudinal word contains five odd derivatives.  Endpoint replacement
contributes

$$
(-1)^5=-1.
$$

Reversing five odd operators contributes

$$
(-1)^{5\cdot4/2}=(-1)^{10}=+1.
$$

Hence

$$
\boxed{
D_{0+}\bar D_0^2D_0^2\delta^4_{02}
=-D_2^2\bar D_2^2D_{2+}\delta^4_{02}.}
$$

Including the longitudinal prefactor gives

$$
-\frac12
D_{0+}\bar D_0^2D_0^2\delta^4_{02}
=+\frac12
D_2^2\bar D_2^2D_{2+}\delta^4_{02}.
$$

The transported (D^2\bar D^2) block is even.  Its Berezin integration by
parts onto the adjacent (r_1) chiral projector therefore contributes no
additional graded sign.  The exact projector identity is

$$
\boxed{
D_2^2(-r_1)\bar D_2^2(-r_1)D_2^2(-r_1)
=-16(\det\mathsf r_1)D_2^2(-r_1).}
$$

Because

$$
\det\mathsf r_1=-\bar r_1^{,2},
$$

the same identity is

$$
D^2\bar D^2D^2=16\bar r_1^{,2}D^2.
$$

Thus the longitudinal word generates an (r_1) inverse-kernel occurrence
after transport.  It is not an untagged remainder.

## 4. Exact finite-Grassmann words

For the fixed external (C(q)), (B(p)) tests, the engine gives

$$
\mathcal G_2^{\mathrm{full}}
=-16384W_{01}(a_2d_1-b_2c_1),
$$

$$
\mathcal G_2^{\mathrm{tr}}
=-16384(\det\mathsf r_2)W_{01},
$$

$$
\mathcal G_2^{\mathrm{long}}
=-16384W_{01}
\left[a_2(d_1-d_2)-b_2(c_1-c_2)\right].
$$

Direct expansion gives

$$
\boxed{
\mathcal G_2^{\mathrm{tr}}
+\mathcal G_2^{\mathrm{long}}
=\mathcal G_2^{\mathrm{full}}.}
$$

Define

$$
M_{21}:=a_2d_1-b_2c_1,
$$

$$
\Omega_{21}
:=a_2d_1-a_1d_2-b_2c_1+b_1c_2.
$$

Then

$$
\boxed{
2M_{21}
=\det\mathsf r_1+\det\mathsf r_2-
\det(\mathsf r_1-\mathsf r_2)+\Omega_{21}.}
$$

Since (mathsf r_1-\mathsf r_2=p), the transported longitudinal word in the
raw orientation (-W_{01}M_{21}) is

$$
\boxed{
-W_{01}\left[a_2(d_1-d_2)-b_2(c_1-c_2)\right]
=\frac12W_{01}
\left(
\det\mathsf r_2-
\det\mathsf r_1+
\det p-
\Omega_{21}
\right).}
$$

The post-transport (r_1) inverse-kernel coefficient is therefore exactly

$$
\boxed{-\frac12.}
$$

## 5. Rank-two extraction independent of the target

Choose the nondegenerate Euclidean frame

$$
p=e_1,
\qquad
q=e_4,
\qquad
p_+\wedge q_+=-i,
$$

and shift

$$
k=L+yq+z(p+q),
\qquad
x=1-y-z.
$$

For

$$
\mathcal S_1
=(\det\mathsf r_0)W_{12}
-(\det\mathsf r_1)W_{02},
$$

$$
\mathcal S_2
=W_{01}M_{21},
$$

the diagonal (L_\mu^2) coefficients are

$$
\operatorname{diag}_{L^2}(\mathcal S_1)
=i(3z-1,z-1,z-1,z+1),
$$

$$
\operatorname{diag}_{L^2}(\mathcal S_2)
=i(1-3z,1-z,-z,-z).
$$

Split

$$
\mathcal S_{2,\det}
:=\frac12W_{01}
\left(
\det\mathsf r_1+
\det\mathsf r_2-
\det p
\right),
$$

$$
\mathcal S_{2,\Omega}
:=\frac12W_{01}\Omega_{21}.
$$

Their diagonal coefficients are

$$
\operatorname{diag}_{L^2}(\mathcal S_{2,\det})
=i(1-3z,-z,-z,-z),
$$

$$
\operatorname{diag}_{L^2}(\mathcal S_{2,\Omega})
=(0,i,0,0).
$$

The transverse metric coefficient is extracted without using the external
directions:

$$
c(T)
:=\frac{T_{22}+T_{33}}{2(p_+\wedge q_+)}.
$$

Therefore

$$
c(\mathcal S_1)=1-z,
$$

$$
c(\mathcal S_{2,\det})=z,
\qquad
c(\mathcal S_{2,\Omega})=-\frac12,
$$

$$
\boxed{
c(\mathcal S_2)=z-\frac12.}
$$

## 6. Full-(d) Schwinger contacts and DRED defect

The determinant parent and its (d)-dimensional SD contact are

$$
P_{\det}=z\bar L^2(p_+\wedge q_+),
$$

$$
C_{\det}=-zL_d^2(p_+\wedge q_+).
$$

Thus

$$
P_{\det}\big|_{\mu_L^2=0}+C_{\det}=0,
$$

$$
P_{\det}+C_{\det}
=z\mu_L^2(p_+\wedge q_+).
$$

The transported (Omega_{21}) parent and its mixed collapsed descendant are

$$
P_{\Omega}
=-\frac12\bar L^2(p_+\wedge q_+),
$$

$$
C_{\Omega}
=+\frac12L_d^2(p_+\wedge q_+).
$$

The descendant contains both terms in

$$
\boxed{
\frac{L_d^2}{(L_d^2+\Delta)^3}
=\frac1{(L_d^2+\Delta)^2}
-\frac{\Delta}{(L_d^2+\Delta)^3}.}
$$

The first term is the collapsed bubble.  The second is the required
rank-zero triangle completion.  Keeping only the first term does not form the
full SD orbit.

Hence

$$
P_{\Omega}\big|_{\mu_L^2=0}+C_{\Omega}=0,
$$

$$
P_{\Omega}+C_{\Omega}
=-\frac12\mu_L^2(p_+\wedge q_+).
$$

The complete second-mark defect is therefore

$$
\boxed{
\mathcal R_2^{\mathrm{full}}
=\left(z-\frac12\right)
\mu_L^2(p_+\wedge q_+).}
$$

## 7. Exact location of the previous error

In the finite-engine raw orientation (-\mathcal S_2), keeping only the
originally visible primary/current tags gave

$$
c_{\mathrm{primary+current}}=y-z.
$$

The discarded transported longitudinal residue gives

$$
c_{\mathrm{residual}}=\frac12-y.
$$

Their exact sum is

$$
\boxed{
(y-z)+\left(\frac12-y\right)
=\frac12-z
=c(-\mathcal S_2).}
$$

Thus the rule

$$
\texttt{ONLY\_ORIGINALLY\_TAGGED\_INVERSE\_KERNELS\_ENTER}
$$

is false.  The (r_1) tag is produced by graded transport and projector
collapse; discarding it is exactly the missing term.

## 8. Simplex integral and coefficient

Use

$$
\int_{\Sigma_2}f
:=\int_0^1dy\int_0^{1-y}dz\,f(y,z).
$$

Then

$$
2\int_{\Sigma_2}(1-z)=\frac23,
$$

$$
2\int_{\Sigma_2}z=\frac13,
\qquad
2\int_{\Sigma_2}\left(-\frac12\right)=-\frac12,
$$

$$
\boxed{
2\int_{\Sigma_2}\left(z-\frac12\right)=-\frac16.}
$$

For the discarded raw-orientation residue,

$$
2\int_{\Sigma_2}(y-z)=0,
$$

$$
2\int_{\Sigma_2}\left(\frac12-y\right)=\frac16,
$$

$$
2\int_{\Sigma_2}\left(\frac12-z\right)=\frac16.
$$

The evanescent master and primitive normalization are

$$
\lim_{\epsilon\to0}
\mu^{2\epsilon}
\int\frac{d^dL}{(2\pi)^d}
\frac{\mu_L^2}{D_0D_1D_2}
=\frac1{32\pi^2},
$$

$$
N_{\mathrm{parent}}=4\hbar g^2.
$$

Therefore the conversion factor is

$$
4\hbar g^2\frac1{32\pi^2}=2\lambda_1.
$$

In the (mathcal S_1,mathcal S_2) orientation,

$$
c_1=2\lambda_1\left(\frac23\right)
=\frac43\lambda_1,
$$

$$
\boxed{
c_2=2\lambda_1\left(-\frac16\right)
=-\frac13\lambda_1,}
$$

$$
\boxed{
c_1+c_2=\lambda_1.}
$$

In the finite-engine raw orientation (-\mathcal S_1,-\mathcal S_2), the
same result is

$$
-\frac43\lambda_1+\frac13\lambda_1=-\lambda_1.
$$

## 9. Verification

Command:

    /Users/libotao/MinerU/.venv/bin/python3 scripts/step5_aa_matter_second_mark_full_sd_independent_audit.py

Result:

    42/42 PASS
