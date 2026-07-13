# Step 5 one-loop covariant-completion review — round 4 audit

Status: `EXTERNAL_GAP_REVIEW_AUDITED_PROJECT_DRED_COUNTEREXAMPLE_SUPERSEDES`

The response is gap review only.  No coefficient is imported.

## Admitted after independent Project derivation

The rooted functional is

$$
\Gamma_{\mathscr I}^{(1)}[\mathcal B]
=\frac12\operatorname{STr}_{\rm DRED}(G_{\mathcal B}I_{\mathcal B}).
$$

Its background-order-$n$ Taylor coefficient is

$$
\Gamma_{\mathscr I,n}^{(1)}
=\frac12
\sum_{\substack{k,s,r_j\\s+\sum_jr_j=n}}
(-1)^k\operatorname{STr}_{\rm DRED}
\left[I_sG_0H_{r_1}G_0\cdots H_{r_k}G_0\right]
+\mathrm{CT}_n.
$$

Therefore triangle, box, pentagon, seagull, and insertion-contact graphs are
Taylor coefficients of one rooted functional.  The Ward identity constrains
their sum.

The injectivity implication concerns the local quotient class:

$$
\ker\bar\ell_2=0,
\qquad
\bar\ell_2[\mathscr A_{\rm loc}^{(1)}]
=C_2\bar\ell_2[\mathscr O_\star]
$$

implies

$$
\boxed{
[\mathscr A_{{\rm loc},n}^{(1)}]
=C_2[\mathscr O_{\star,n}]
\quad\text{for every }n.}
$$

It does not imply equality with the complete nonlocal one-loop 1PI amplitude.

The complete quadratic coefficient is

$$
\begin{aligned}
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}_{\rm DRED}\Big[&
+I_0G_0H_1[1]G_0H_1[2]G_0
+I_0G_0H_1[2]G_0H_1[1]G_0\\
&-I_0G_0H_2[1,2]G_0
-I_1[1]G_0H_1[2]G_0\\
&-I_1[2]G_0H_1[1]G_0
+I_2[1,2]G_0
\Big]+\mathrm{CT}_2.
\end{aligned}
$$

Hence

$$
C_2=C_\triangle+C_{\rm contact},
$$

$$
C_2=C_\triangle
\quad\Longleftrightarrow\quad
[Q_{\rm contact}]_{T_2}=0.
$$

Background covariance alone does not prove the second equation.

The fixed-vector-frame theorem uses the already fixed Gaussian and is not
blocked by the nonlinear chiral/vector coordinate Jacobian.  The Project
bridge certificate gives

$$
\mathcal O_C=\mathcal B^{-1}\mathcal O_V\mathcal B,
$$

while a nonlinear quantum-coordinate change obeys

$$
K_C=J_q^{\rm st}K_VJ_q
+E_{V,\alpha}C^\alpha{}_{ij}.
$$

These are distinct statements.

## Project correction beyond the response: explicit DRED kernel

Define

$$
\widetilde\delta^{mn}
=\frac{\epsilon}{2}\delta_{(4)}^{mn}+\tau^{mn},
\qquad
\delta_{(4)mn}\tau^{mn}=0.
$$

The exact projector algebra gives

$$
\tau_{mn}\tau^{mn}=2\epsilon-\epsilon^2
\notin(\epsilon^2)\mathbb Q[\epsilon].
$$

Thus $\tau$ is not an $\epsilon$-multiple of the four-dimensional metric.
The Project computation constructs

$$
\mathscr E_{abc}^{AB}
=K^{AB}{}_{C[DE]}
\tau_{(ab|\dot c\dot d|}
W_{c)}^C\widetilde W^{D\dot c}\widetilde W^{E\dot d},
$$

$$
K^{AB}{}_{C[DE]}
=\delta^A{}_Cc_{DE}{}^B
+\delta^B{}_Cc_{DE}{}^A.
$$

For $SU(2)$,

$$
K^{00}{}_{0[12]}=2,
\qquad
729\text{ of }729\text{ equivariance equations vanish}.
$$

Moreover,

$$
[\mathscr E]=\frac92,
\qquad
(j_L,j_R)=\left(\frac32,0\right),
\qquad
r_{\rm P}(\mathscr E)=-1,
\qquad
|\mathscr E|=1,
$$

$$
\ell_2(\mathscr E)=0,
\qquad
\left.\frac{\partial^3}{\partial t^3}\right|_{t=0}
\mathscr E(t\mathcal B)\ne0.
$$

Therefore

$$
\boxed{
\ker\!\left(\ell_2\big|_{\rm full\ DRED\ raw}\right)\ne0.}
$$

The physical four-dimensional projection kills this witness:

$$
q_{4d}(\tau)=0,
\qquad
q_{4d}(\mathscr E)=0.
$$

Thus the full-DRED injectivity claim is false; physical-$4d$ injectivity is a
separate relation-matrix problem.

## Color/source result and remaining gates

The fixed-background source complex obeys

$$
s_B\Gamma=\Gamma^2,
\qquad
s_B\mathscr I=\Gamma\mathscr I,
\qquad
s_BJ=J\Gamma,
$$

$$
s_B^2\mathscr I=s_B^2J=s_B(J\mathscr I)=0.
$$

The local source-IBP matrix has

$$
R_{\rm loc}
=\begin{pmatrix}1&1&1\\0&1&0\end{pmatrix},
\qquad
\operatorname{rank}R_{\rm loc}=2,
\qquad
\dim Q_{\rm loc}=1.
$$

The color split map is

$$
\iota_M(m)=(m,-m),
\qquad
\pi_1\iota_M=\operatorname{id}.
$$

This does not replace the combined physical quotient in which color exchange
and field-word exchange act simultaneously.

The unresolved equalities are

$$
\ker\bar\ell_2^{\,4d}=0,
\qquad
[Q_{\rm contact}]_{T_2}=0,
\qquad
[\mathscr E]_{\rm EOM/IBP/BV}=0,
\qquad
\operatorname{Coeff}_{\mathscr E}
\mathscr A_{{\rm loc},3}^{(1)}=0.
$$

No anomaly coefficient and no one-loop exactness theorem are accepted from
the response.
