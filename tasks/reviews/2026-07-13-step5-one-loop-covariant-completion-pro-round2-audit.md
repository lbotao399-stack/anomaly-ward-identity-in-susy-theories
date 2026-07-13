# Step 5 one-loop covariant-completion review — round 2 audit

Status: `EXTERNAL_GAP_REVIEW_AUDITED`

## Admitted after independent Project derivation

$$
\mathscr I^{AB}=\mathscr I^{BA},
\qquad
\mathscr O_-^{AB}=-\mathscr O_-^{BA}.
$$

Hence

$$
P_{\operatorname{Sym}^2(\mathrm{Adj})}\mathscr O_-=0.
$$

The fixed quadratic jet is the relevant linear map:

$$
\bar\ell_2:H_{\mathrm{phys}}\longrightarrow\mathcal T_2/B_2,
$$

$$
\ker\bar\ell_2=0
\iff
\{v\in\ker C:\ell_2v\in B_2\}=\operatorname{im}[E\ Q].
$$

For an odd source \\(J\\), the labeled two-background Hessian family is

$$
\Gamma^{(1)}_{J;12}
=\frac12\operatorname{STr}\!\left[
I_{12}G_0
-I_1G_0H_2G_0
-I_2G_0H_1G_0
-I_0G_0H_{12}G_0
+I_0G_0H_1G_0H_2G_0
+I_0G_0H_2G_0H_1G_0
\right]
+\mathrm{CT}_{12}+\mathrm{Jac}_{12}.
$$

Raw Hessians transform by congruence; the paired endomorphism inside the
regulated supertrace transforms by similarity.

## Rejected translations

The response used

$$
r(\bar\nabla_{\dot a})=+1
$$

as a physical \\(U(1)_R\\) charge.  The Project currently has only the formal
filtration \\(r_{\mathrm f}\\); `PROJECT_R_WEIGHT_BINDING` remains open.

The response used the withdrawn sector

$$
(j_L,j_R)=\left(\frac12,0\right).
$$

The exact Project sector is

$$
(j_L,j_R)=\left(\frac32,0\right),
\qquad
U_{-;++++}=-\frac45t_{+++}.
$$

The statement

$$
[\mathscr I]_{\mathrm{EOM}}=0
$$

is not admitted as the full \(\mathcal N=4\) source-completed quotient.  The
pure-\(\mathcal N=1\) identity

$$
\mathscr I^{AB}
=-(\nabla_+E^A)X^B-X^A(\nabla_+E^B)
$$

is retained only as an explicit EOM-carrier relation until the matter terms,
antifields, contact descendants, and hidden-supersymmetry source multiplet are
included.

The response's monomial counts are not imported: they used the wrong spin
sector and an unbound charge.  The executable Project census is authoritative.

## Open gates

$$
\ker\bar\ell_2,
\qquad
\mathrm{CT}_{12}+\mathrm{Jac}_{12},
\qquad
\Delta_{\mathrm{cyc}},
\qquad
\frac{\delta}{\delta J}\log\operatorname{Ber}S_R,
\qquad
\text{full }\mathcal N=4\text{ EOM/source complex}
$$

remain unproved.  No coefficient and no one-loop exactness theorem are
accepted from this review.
