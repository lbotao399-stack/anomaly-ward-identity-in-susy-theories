# Step 5 one-loop covariant-completion review — GPT Pro round 2 prompt

This is an external theorem-gap audit only.  Do not import any known anomaly
coefficient, holomorphic-twist result, or prior calculation of this operator.
Do not read Notion or any local legacy result.

Use the following locked Euclidean Project sector.

$$
X^A:=(\nabla_+W_+)^A,
\qquad
\mathscr I^{AB}
:=
\nabla_-^{\operatorname{Adj}\otimes\operatorname{Adj}}
\left(X^AX^B\right),
$$

where (A,B) are open gauge-adjoint indices and (J_{AB}) is the odd dual
source.  The target source-linear density has

$$
[\mathscr I]=\frac92,
\qquad
|\mathscr I|=1,
\qquad
\operatorname{Spin}(4)=\left(\frac12,0\right),
\qquad
r(\mathscr I)=-1,
$$

with formal integer weights

$$
r(\nabla_a)=-1,
\qquad
r(W_a)=+1,
\qquad
r(\widetilde W_{\dot a})=-1,
\qquad
r(\mathcal D_{a\dot a})=0.
$$

The displayed candidate is

$$
\mathscr O_{\rm cov}^{AB}
=
c_{ACD}c_{BCE}
\left[
\widetilde W^D_{\dot\alpha}\mathcal D_+{}^{\dot\alpha}X^E
-
(\mathcal D_+{}^{\dot\alpha}X^D)
\widetilde W^E_{\dot\alpha}
\right].
$$

The regulator is DRED.  Spinor algebra is four-dimensional, loop momentum is
(d=4-2\epsilon), and evanescent source operators remain in the temporary
mixing complex until every (\epsilon\epsilon^{-1}) finite term is extracted.

Please independently calculate and audit the following.

1. Construct the complete pure-gauge local covariant monomial basis with the
   displayed dimension, parity, Spin(4), (r=-1), open
   (\operatorname{Adj}\otimes\operatorname{Adj}) type, and source degree
   (J^1).  Reduce it by graded symmetry, Bianchi identities, Jacobi,
   covariant integration by parts, EOM, and BRST-exact terms.  In particular,
   test every cubic field-strength family such as
   (W_a^C W^{D b}W_b^E) against the exact (r)-weight and spin constraints.

2. State the closed, exact, and EOM matrices required to compute the
   source-linear local BRST cohomology.  Determine whether its physical
   pure-gauge quotient has rank one.  If the Project data above are
   insufficient for an actual rank, identify the smallest missing algebraic
   datum; do not guess the rank.

3. Define the fixed quadratic jet

   $$
   \ell_2[\mathscr O]
   :=
   \left.
   \frac12
   \frac{\vec\delta}{\delta\mathcal V_1}
   \frac{\vec\delta}{\delta\mathcal V_2}
   \mathscr O[\mathcal V]
   \right|_{\mathcal V=0}.
   $$

   Compute the condition for
   (\ker\ell_2=0).  Distinguish this fixed quadratic jet from the
   class-dependent “lowest nonzero jet,” which cannot prove injectivity.

4. For an odd source (J), derive with left/right functional derivatives the
   exact graded one-loop formula from

   $$
   \Gamma^{(1)}=\frac12\operatorname{STr}\log H[J,\mathcal V],
   \qquad
   H=H_0+H_+[\mathcal V]+J I[\mathcal V].
   $$

   Fix every sign, cyclic sign, and symmetry factor.  Enumerate the complete
   two-background primitive family and check whether

   $$
   I_0H_1H_1,
   \qquad
   I_0H_2,
   \qquad
   I_1H_1,
   \qquad
   I_2,
   \qquad
   \mathrm{CT}_2
   $$

   is exhaustive after mixed Hessian blocks, source partners, gauge fixing,
   FP, and Nielsen--Kallosh fields are included.

5. Prove the precise distinction between a supersymmetry/global Ward anomaly
   with exact background gauge Ward identity and a consistent gauge anomaly.
   State exactly when a Bardeen--Zumino shift can alter box/pentagon local
   representatives in this problem.

6. Audit the representation bridge at the Hessian and insertion-kernel level:

   $$
   H_{\mathsf C}=S_RH_{\mathsf V}S_R^{-1},
   \qquad
   I_{\mathsf C}=S_RI_{\mathsf V}S_R^{-1},
   \qquad
   G_{\mathsf C}(z,z')
   =S_R(z)G_{\mathsf V}(z,z')S_R^{-1}(z').
   $$

   Identify the exact regulated-supertrace cyclicity and Jacobian conditions.

7. Check the independent-connection filtration separately for the classical
   seed and candidate anomaly:

   $$
   \deg_{\mathcal A}\mathscr I\le7,
   \qquad
   \deg_{\mathcal A}\mathscr O_{\rm cov}\le6.
   $$

   Determine whether either upper bound is reduced by mandatory identities.

8. Separate the manifest-(\mathcal N=1) proof from any claim using hidden
   (\mathcal N=4) supersymmetry.  List the exact extra sources/identities
   needed before hidden supersymmetry may be used to remove cohomology classes.

Return a formula-first gap audit.  A conditional theorem is allowed; an
unproved uniqueness claim is not.  No numerical anomaly coefficient is
requested.
