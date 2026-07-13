# Step 5 one-loop covariant completion — Pro review round 5 prompt

Please act only as an adversarial theoretical-physics gap reviewer.  Do not
supply or import an anomaly coefficient.  Audit the following independently
derived Project status for

$$
\mathscr I^{AB}
=\nabla_-\left[(\nabla_+W_+)^A(\nabla_+W_+)^B\right].
$$

The proposed theorem is only about the one-loop UV-local class, not the full
nonlocal 1PI amplitude and not higher-loop vanishing.

The exact rooted one-loop functional is

$$
\Gamma_{\mathscr I}^{(1)}[B]
=\frac12\operatorname{STr}_{\rm DRED}(G_BI_B),
$$

$$
\Gamma_{\mathscr I,n}^{(1)}
=\frac12\sum_{s+\sum r_j=n}(-1)^k
\operatorname{STr}_{\rm DRED}
\left[I_sG_0H_{r_1}G_0\cdots H_{r_k}G_0\right]
+\mathrm{CT}_n.
$$

Thus triangle, box, pentagon, and contact graphs are Taylor coefficients of
one background-covariant rooted functional.  This proves Ward closure of the
sum, but by itself does not prove unique covariant completion.

The complete quadratic family is

$$
\begin{aligned}
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}\Big[&
+I_0G_0H_1[1]G_0H_1[2]G_0
+I_0G_0H_1[2]G_0H_1[1]G_0\\
&-I_0G_0H_2[1,2]G_0
-I_1[1]G_0H_1[2]G_0\\
&-I_1[2]G_0H_1[1]G_0
+I_2[1,2]G_0\Big]+\mathrm{CT}_2.
\end{aligned}
$$

The isolated triangle pole is not yet the accepted coefficient because the
post-projector contact pole is not computed.  In particular, intrinsic
chiral/antichiral sector labels do not prove $I_0H_2=0$.

The full-DRED quadratic-jet injectivity claim is false in the raw
background-CE module.  Define

$$
\widetilde\delta^{mn}
=\frac\epsilon2\delta_{(4)}^{mn}+\tau^{mn},
\qquad
\delta_{(4)mn}\tau^{mn}=0,
$$

$$
\tau_{mn}\tau^{mn}=2\epsilon-\epsilon^2.
$$

There is an explicit cubic regulator-spurion jet

$$
\mathscr E_{abc}^{AB}
=K^{AB}{}_{C[DE]}\tau_{(ab|\dot c\dot d|}
W_{c)}^C\widetilde W^{D\dot c}\widetilde W^{E\dot d},
$$

$$
K^{AB}{}_{C[DE]}
=\delta^A{}_Cc_{DE}{}^B+\delta^B{}_Cc_{DE}{}^A,
$$

with correct dimension, Spin$(4)$ weight, parity, Project $R$ weight, source
symmetry, and a nonzero exact $SU(2)$ color witness.  It obeys

$$
\ell_2(\mathscr E)=0,
\qquad
\partial_t^3\mathscr E(tB)|_{t=0}\ne0,
\qquad
q_{4d}(\mathscr E)=0.
$$

Its $n=3$ coefficient is not computed: among the $26$ polarized rooted rows,
$24$ have current kernels, while $I_0H_3$ and $I_3$ are absent because the
Project lacks $[V^5]S_{\rm gauge}$ and the valence-five insertion $I_{(5)}$.

The attempted physical-$4d$ filtered proof was rejected because it used

$$
R_{1,\rm raw}=[\mathbf1_{4866}\mid-C_{1\to2}^T],
$$

but the $4866$ columns are normal-order event/branch-path coordinates, not
independent $N=1$ generators.  The required parent-incidence matrix from the
true $N=1$ carrier and the terminal normal-order relation matrix are absent.
The current honest status is therefore

$$
\ker\bar\ell_2^{\,4d}=\texttt{FAIL\_CLOSED\_NOT\_CERTIFIED}.
$$

The vector/chiral operator bridge is exact on the fixed similarity sector,
but nonlinear Hessians obey

$$
K_C=J_q^{\rm st}K_VJ_q+E_{V,\alpha}C^\alpha{}_{ij},
$$

so full cross-frame density/Jacobian equivalence is not claimed.

Please answer only:

1. Is this bifurcation between physical-$4d$ and full-DRED logically correct?
2. Does the explicit $\tau$ word really refute raw full-DRED quadratic-jet
   injectivity, or is it excluded by a symmetry/background-space axiom that
   must be stated?
3. What is the minimal non-tautological matrix certificate needed to prove
   physical-$4d$ filtered injectivity?
4. Is any theorem stronger than the conditional local-class statement

   $$
   \ker\bar\ell_2^{\,4d}=0
   \Longrightarrow
   [\mathscr A_{{\rm loc},n}^{(1)}]
   =C_2[\mathscr O_{\star,n}]
   $$

   presently justified?
5. List every remaining P0/P1 gap, especially contact, counterterm,
   source-BRST, and vector/chiral-frame gaps.

Do not assume that covariance sets the contact family to zero.  Do not infer
the full 1PI box/pentagon amplitudes from a local cohomology theorem.
