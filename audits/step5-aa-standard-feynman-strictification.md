# Step 5 ordered $AA$ standard-Feynman strictification

Status: `BLOCKED__PRO_FINAL_SETTLED__CONDITIONAL_DOWNSTREAM_ARITHMETIC_ONLY__FULL_AA_MATCH_OPEN`.

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.

GPT Pro output is `NON_AUTHORITY_PRO_REVIEW`; the three gates are archived at `proposals/gpt-pro-aa-standard-feynman-2026-07-14.md`, `proposals/gpt-pro-aa-derivation-correction-2026-07-14.md`, and `proposals/gpt-pro-aa-final-settlement-2026-07-14.md`.  Sections 1, 2, and 5 contain independently checked normalization, tensor-integral, and simplex arithmetic.  Sections 3 and 4 contain conditional downstream arithmetic only: neither the gauge nor the matter superspace $D$-word has yet been emitted as an occurrence-resolved executable trace.  The ordered source/background-port definition in Section 3 is a `LOCAL_PROPOSAL` because the verified base does not lock it.

## 1. Canonical letters and regulator

The Step-4 fields are coupling-absorbed.  Define the canonical fields and letters by

$$
u:=\frac{V}{\sqrt2g},
\qquad
\Phi_{c,r}:=g^{-1}\Phi_r,
\qquad
\widetilde\Phi_{c,r}:=g^{-1}\widetilde\Phi_r,
$$

$$
A^A:=g^{-1}(\nabla_+\mathcal W_+)^A,
\qquad
B_r^A:=g^{-1}(\nabla_+\Phi_r)^A,
$$

$$
C_r^A:=g^{-1}\widetilde\Phi_r^A,
\qquad
D_{\dot\alpha}^A:=g^{-1}\widetilde{\mathcal W}_{\dot\alpha}^A.
$$

All formulas below use these canonical letters.  Define

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2},
\qquad
\mathbb F^{AB}{}_{DE}
:=\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}.
$$

The conditional Fermi--Feynman propagators become

$$
\langle u^A(p,1)u^B(-p,2)\rangle
=-\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_1-\theta_2),
$$

$$
\langle\Phi_{c,r}^A(p,1)\widetilde\Phi_{c,s}^B(-p,2)\rangle
=\delta_{rs}\frac{\hbar\kappa^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\theta_1-\theta_2).
$$

The inconsistent old variable was

$$
v_{\rm old}:=\frac{V}{2g}=\frac{u}{\sqrt2}.
$$

Hence

$$
\langle v_{\rm old}v_{\rm old}\rangle
=-\frac{\hbar}{2p^2}\delta^4(\theta_1-\theta_2),
$$

not the unit propagator used in the former WW seed.  Let $p,q$ be physical external momenta and define $Q:=p+q$.  The dotted operator $P_{\dot\alpha}$ used below is the holomorphic translation generator acting on an external letter; it is not a loop momentum.

The DRED split is

$$
d=4-2\epsilon,
\qquad
\delta_4^{mn}=\widehat\delta^{mn}+\breve\delta^{mn},
$$

$$
\widehat\delta^m{}_m=d,
\qquad
\breve\delta^m{}_m=2\epsilon,
\qquad
\breve\delta^m{}_n\ell^n=0,
\qquad
\breve\delta^m{}_np^n
=\breve\delta^m{}_nq^n
=\breve\delta^m{}_nQ^n=0.
$$

## 2. Universal triangle tensor integral

Let

$$
r_0=k,
\qquad
r_1=k+q,
\qquad
r_2=k+p+q,
\qquad
Q=p+q.
$$

Define the standard two-simplex by

$$
\Delta_2
:=\{(x,y,z)\in\mathbb R_{\ge0}^3:x+y+z=1\}
\cong\{(a,b)\in\mathbb R_{\ge0}^2:a+b\le1\},
$$

Then

$$
\frac1{r_0^2r_1^2r_2^2}
=2\int_{\Delta_2}
\frac{dx\,dy\,dz\,\delta(1-x-y-z)}{(\ell^2+\Delta)^3},
$$

$$
\ell=k+yq+zQ,
\qquad
\Delta=xyq^2+xzQ^2+yzp^2.
$$

For

$$
L_1=2k+q,
\qquad
L_2=2k+p+2q,
$$

the shifted vectors are

$$
L_1=2\ell+(1-2y)q-2zQ,
$$

$$
L_2=2\ell+(1-2y)q+(1-2z)Q.
$$

Define the loop measure and scalar integrals by

$$
\int_k:=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d},
$$

$$
I_2(\Delta):=\int_\ell\frac1{(\ell^2+\Delta)^2},
\qquad
I_3(\Delta):=\int_\ell\frac1{(\ell^2+\Delta)^3}.
$$

The pole is

$$
I_2(\Delta)\big|_{1/\epsilon}
=\frac1{16\pi^2\epsilon}.
$$

Moreover,

$$
\int_\ell\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=\frac{\widehat\delta^{mn}}d
\left[I_2(\Delta)-\Delta I_3(\Delta)\right],
$$

$$
\Delta I_3(\Delta)=\frac\epsilon2I_2(\Delta),
$$

$$
\frac1{4-2\epsilon}\left(1-\frac\epsilon2\right)
=\frac14.
$$

Therefore

$$
\operatorname*{Pole}
\int_k\frac{L_1^mL_2^n}{r_0^2r_1^2r_2^2}
=\frac{\widehat\delta^{mn}}{16\pi^2\epsilon}.
$$

## 3. Pure-gauge triangle and its Schwinger cut

The numerical coefficient in this section has status

$$
\texttt{CONDITIONAL\_ARITHMETIC\_ON\_RECORDED\_PRIMITIVES}.
$$

The missing primitives are the noncommutative $D$-word transport signs, the locked ordered bilocal source, the background/quantum port grammar, and the complete contact/longitudinal orbit.

### 3.1 Ordered local port

The linearized insertion is

$$
K_+^c:=-\frac1{4\sqrt2}D_+\bar D^2D_+,
\qquad
A_{(1)}=K_+^cu,
$$

$$
D_-A_{(1)}
=-\frac1{8\sqrt2}D^2\bar D^2D_+u.
$$

The two exponent Hessians are

$$
\mathfrak V_W^c
=-\frac{ig}{4\hbar}c_{UCE}W^{E\gamma}
(D_{C\gamma}-D_{U\gamma}),
$$

$$
\mathfrak V_{\widetilde W}^c
=+\frac{ig}{4\hbar}c_{UCD}D_{\dot\gamma}^D
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).
$$

The magnitudes of the insertion coefficient, closed $D$-loop, and mixed anticommutators give

$$
\left(\frac1{64}\right)(16)(2)(2)=1.
$$

The signed product of the two Hessians and three vector propagators is

$$
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3
=-\frac{\hbar g^2}{16}.
$$

The recorded triangle endpoint rows assign the raw and transport signs

$$
\begin{array}{c|c}
(r_0,r_1)&(-1)(-1)\\
(r_0,r_2)&(+1)(+1)\\
(r_1,r_1)&(+1)(+1)\\
(r_1,r_2)&(-1)(-1)
\end{array}
$$

The four displayed products are $+1$.  A separate unproved global odd-$D$ transport sign is required:

$$
s_{T,\mathrm{global}}=-1.
$$

The candidate closed-word sign is therefore

$$
w_{T,\mathrm{rows}}
=s_{T,\mathrm{global}}\left(\frac1{64}\right)(16)(2)(2)
=-1.
$$

The row assignment and $s_{T,\mathrm{global}}$ are recorded primitives, not an independently emitted noncommutative $D$-algebra trace.  Conditional on them,

$$
\left(-\frac{\hbar g^2}{16}\right)w_{T,\mathrm{rows}}
=\frac{\hbar g^2}{16}.
$$

The fixed-orientation numerator is

$$
N_{G,+}{}^{\dot\alpha}
=(r_0+r_1)_{+\dot\beta}
(ip)^{\dot\beta\gamma}
(r_1+r_2)_\gamma{}^{\dot\alpha}.
$$

Define the spinor chain $T_{m\rho n,+}{}^{\dot\alpha}:=(\sigma_m\bar\sigma_\rho\sigma_n)_+{}^{\dot\alpha}$.  Thus, conditional on the recorded row assignment,

$$
\Gamma_{T,G,\mathrm{pole}}^{A|B}
=\frac{i\hbar g^2}{256\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
D_{\dot\alpha}^DA^E
p^\rho T_{m\rho n,+}{}^{\dot\alpha}
\widehat\delta^{mn}.
$$

The verified base does not lock the ordered bilocal source and the background/quantum port grammar.  The following definition is `LOCAL_PROPOSAL-AA-PORT`:

$$
S_J:=\int J_{AB}L^A(\tau_wL)^B,
\qquad
\mathcal I_-^{AB}:=\nabla_-\frac{\delta S_J}{\delta J_{AB}},
$$

with every quantum occurrence tagged and differentiated in displayed order.

For one tagged occurrence,

$$
0=\int Du\,\frac{\delta}{\delta u^I}
\left(F^I e^{-S_2/\hbar}\right)
$$

gives

$$
\langle F^IK_{0,IJ}u^J\rangle
-\hbar\left\langle\frac{\delta F^I}{\delta u^I}\right\rangle=0.
$$

The Schwinger--Dyson identity alone does not fix the sign with which the cut term enters $\mathcal I_-^{AB}$.  The local source prescription records the additional primitive $s_{C,\mathrm{source}}=-1$; it is not derived from the displayed identity.  Conditional on this sign, cutting the tagged chiral port gives

$$
\left(\frac1{4\sqrt2}\right)
\left(\frac g{4\hbar}\right)
(\hbar)(16)
=\frac g{\sqrt2}.
$$

The candidate canonical aggregate descendant is

$$
\mathfrak I_{\mathrm{agg}}^{A|B}
=\frac g{\sqrt2}c^{BCE}A^E
\left[(D_-K_+^cu^A)u^C-(K_+^cu^A)D_-u^C\right]
+\mathrm{EOM}+\mathrm{longitudinal}.
$$

For one cut word the raw expansion is

$$
\begin{aligned}
(D_A-D_C)K_+^c(\bar D_C-\bar D_A)
={}&D_AK_+^c\bar D_C-D_AK_+^c\bar D_A\\
&-D_CK_+^c\bar D_C+D_CK_+^c\bar D_A.
\end{aligned}
$$

The recorded raw signs and transport signs are

$$
s_{\mathrm{raw}}=(+1,-1,-1,+1),
\qquad
s_{\mathrm{transport}}=(-1,+1,+1,-1),
$$

$$
s_{\mathrm{raw}}s_{\mathrm{transport}}
=(-1,-1,-1,-1).
$$

The four transport signs are not yet derived from an executable ordered $D$-word.  Conditional on those primitives, each row has

$$
\left(-\frac1{4\sqrt2}\right)(-1)
\left(\frac12\right)(2)
\left(-\frac12\right)
=-\frac1{8\sqrt2}.
$$

The complete conditional cut magnitude is

$$
4\left(\frac g{\sqrt2}\right)
\left(\frac{ig}{4\hbar}\right)
(-\hbar)^2
\left(-\frac1{8\sqrt2}\right)
\left(\frac1{16\pi^2\epsilon}\right)
=-\frac{i\hbar g^2}{256\pi^2\epsilon}.
$$

Therefore

$$
\Gamma_{C,G,\mathrm{pole}}^{A|B}
=-\frac{i\hbar g^2}{256\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
D_{\dot\alpha}^DA^E
p^\rho T_{m\rho n,+}{}^{\dot\alpha}
\delta_4^{mn}.
$$

Since

$$
\breve\delta^{mn}
\sigma_m\bar\sigma_\rho\sigma_n
=-2\epsilon\sigma_\rho,
$$

the first directed term is conditionally

$$
\Gamma_{G,1}^{AB}
=\frac{\lambda_1}{8}\mathbb F^{AB}{}_{DE}
D_{\dot\alpha}^DP^{\dot\alpha}A^E.
$$

For the reflected spinor ordering,

$$
(P^{\dot\alpha}A^D)D_{\dot\alpha}^E
=-(P_{\dot\alpha}A^D)D^{E\dot\alpha}.
$$

The color tensor obeys the candidate exchange relation

$$
\mathbb F^{BA}{}_{ED}=\mathbb F^{AB}{}_{DE},
$$

but this identity and the spinor reordering do not derive the reflected graph.  The source-port exchange, loop routing, parity sign, and quantum-occurrence map are still absent.  Conditional on those maps, and after discarding the displayed $\mathrm{EOM}$ and longitudinal terms, the proposed pure-gauge expression is

$$
\boxed{
\Gamma_{AA,G}^{AB}
=\frac{\lambda_1}{8}\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^DP^{\dot\alpha}A^E
-(P_{\dot\alpha}A^D)D^{E\dot\alpha}
\right].}
$$

It is not an accepted complete gauge orbit:

$$
\boxed{
\begin{gathered}
\texttt{BLOCKED\_EXPLICIT\_WW\_D\_ALGEBRA\_WORD\_DERIVATION},\\
\texttt{BLOCKED\_STEP5A\_LOCAL\_FERMI\_FEYNMAN\_PROPER\_SLICE},\\
\texttt{BLOCKED\_LOCKED\_ORDERED\_BILOCAL\_SOURCE},\\
\texttt{BLOCKED\_LOCKED\_STEP5\_DRED\_CONTRACT},\\
\texttt{BLOCKED\_LOCKED\_BACKGROUND\_QUANTUM\_PORT\_GRAMMAR},\\
\texttt{BLOCKED\_EQUAL\_CONTACT\_AND\_LONGITUDINAL\_RESIDUES}.
\end{gathered}}
$$

Machine-readable blockers: `BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION`, `BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE`, `BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE`, `BLOCKED_LOCKED_STEP5_DRED_CONTRACT`, `BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR`, `BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES`.

The former $\lambda_1$ coefficient is larger by $8$, because it assigned a unit propagator to $v_{\rm old}=V/(2g)$.  Three incorrect propagators multiply the graph by

$$
2^3=8.
$$

## 4. Conditional two-$\widetilde\Phi V\Phi$ matter parent

### 4.1 Vertices, Wick weight, color, and flavor

The canonical $n=1$ matter action is

$$
S_{E,\mathrm{mat}}^{(1)}
=-\sqrt2g\int d^8z\,
\kappa_{AB}\widetilde\Phi_{c,r}^A
u^U(T_U)^B{}_C\Phi_{c,r}^C.
$$

The fixed directed interaction weight is

$$
\frac1{2!}(S_1S_2+S_2S_1)=S_1S_2.
$$

The candidate port prescription retains one port-preserving contraction, records no closed-matter-loop sign, and carries

$$
\delta_{rs}
$$

on the internal chiral line.  For external $C_r^D$ at the first vertex and $B_r^E$ at the second,

$$
[\kappa_{DB'}(T_U)^{B'}{}_C]
[\kappa_{C'B''}(T_V)^{B''}{}_E]
=(ic_{UCD})(ic_{VEC'})
=-c_{UCD}c_{VEC'}
=+c_{UCD}c_{VC'E}.
$$

This gives the same ordered tensor

$$
\mathbb F^{AB}{}_{DE}.
$$

The two generator factors give $i^2=-1$; this sign must not be replaced by $+1$.  The candidate ordering records a separate Koszul sign $-1$ when the odd component $B_r=D_+\Phi_r|$ is moved across the odd $D_-K_+^c$ word.  Because the port/projector word is missing, this Koszul sign remains a recorded convention.  The exponent, propagator, color-antisymmetry, and Koszul signs remain separately tagged in the matter orientation ledger; the boxes below record the current fixed-order convention and are not an accepted full-sector sign.

### 4.2 Unverified $D$-word ansatz

Use

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q.
$$

The intended marked-first-$A$ word is only schematic because the graph-specific superspace delta functions, endpoint actions $D_i(r)$ and $\bar D_i(r)$, the $\theta_0$ projection, and the letter projectors $\Pi_{B_r}$ and $\Pi_{C_r}$ are not defined in the verified base:

$$
\begin{aligned}
\mathscr D_{M,CB}^{(A)}
=\int d^4\theta_1d^4\theta_2\,
&C_r^D(q,1)\Phi_r^E(p,2)\\
&\times[D_-K_+^c\delta_{01}(r_0)]
[K_+^c\delta_{02}(-r_2)]\\
&\times\left[
\frac1{16}\bar D_1^2D_1^2\delta_{12}(r_1)
\right].
\end{aligned}
$$

No executable exterior-algebra trace currently enumerates its claimed sixteen monomials.  Let $\eta_W=\pm1$ denote the uncomputed combined sign of the ordered Berezin measure and the displayed coordinate-word normal order.  With

$$
x_+\wedge y_+
:=x_{+\dot+}y_{+\dot-}-x_{+\dot-}y_{+\dot+},
$$

and the finite two-component symbol

$$
\mathsf r_{a\dot a}:=-i(\sigma_E^m)_{a\dot a}r_m,
\qquad
\det(r):=\det\mathsf r,
$$

the hand-supplied candidate is

$$
\boxed{
N_{M,\mathrm{ansatz}}^c
=2\eta_W\left[
\det(r_0)(r_{1+}\wedge r_{2+})
-\det(r_1)(r_{0+}\wedge r_{2+})
\right].}
$$

Its status is

$$
\boxed{\texttt{UNVERIFIED\_DWORD\_ANSATZ}.}
$$

The two exponent vertices give $-2$, the conversion $c_{VEC'}=-c_{VC'E}$ gives a second minus sign, and moving the odd external $B$ through the odd insertion word gives the Koszul sign $-1$.  Let $\eta_P=\pm1$ denote their product with the propagator and external-output normal-order signs.  Before an occurrence-resolved trace, the candidate stripped prefactor is

$$
2\eta_P\hbar g^2.
$$

Neither $\eta_P$ nor $\eta_W$ has been computed by an emitted ordered-word trace.  The downstream arithmetic below imposes the trial convention

$$
\eta_P\eta_W=1.
$$

Under this convention only,

$$
(2\eta_P\hbar g^2)N_{M,\mathrm{ansatz}}^c
=\hbar g^2N_M^{\mathrm{eff}},
$$

where

$$
\boxed{
N_M^{\mathrm{eff}}
:=4\left[
\det(r_0)(r_{1+}\wedge r_{2+})
-\det(r_1)(r_{0+}\wedge r_{2+})
\right].}
$$

This is a definition of the candidate parent, not a derivation:

$$
\boxed{\texttt{CONDITIONAL\_PARENT\_DEFINITION}.}
$$

### 4.3 Rank-two DRED projection

Set

$$
\ell=k-yq-zQ,
\qquad
\Delta=xyq^2+xzQ^2+yzp^2.
$$

For a symmetric metric $H^{mn}$, define

$$
\mathcal R_M[H]
:=2\int_{\Delta_2}
\frac14H^{mn}[N_M^{\mathrm{eff}}]_{\ell_m\ell_n}.
$$

The executable check constructs $N_M^{\mathrm{eff}}$ directly as an ordinary commutative polynomial; it does not derive it from the superspace $D$-word.  It checks only the frame $p=e_1$, $q=e_4$ and diagonal $H$.  In that frame the downstream polynomial arithmetic gives

$$
\left.\mathcal R_M[\delta_4]\right|_{p=e_1,q=e_4}=0,
$$

$$
\boxed{
\left.\mathcal R_M[\widehat\delta]\right|_{p=e_1,q=e_4}
=\frac{4\epsilon}{3}(p_+\wedge q_+).}
$$

These are special-frame consequences of `CONDITIONAL_PARENT_DEFINITION`; they are neither a general tensor proof nor a derivation of the parent.

For the check $p=e_1$, $q=e_4$, and

$$
H=\operatorname{diag}(1,h_2,h_3,1),
\qquad
h_2+h_3=2-2\epsilon,
$$

the exact downstream polynomial expansion of the candidate $N_M^{\mathrm{eff}}$ gives the forward and reflected diagonal rank-two weights

$$
[N_M^{\mathrm{eff}}]_{\ell_1^2}=i(12z-4),
$$

$$
[N_M^{\mathrm{eff}}]_{\ell_2^2}
=[N_M^{\mathrm{eff}}]_{\ell_3^2}
=i(4z-4),
$$

$$
[N_M^{\mathrm{eff}}]_{\ell_4^2}=i(4z+4).
$$

Using

$$
2\cdot\frac14=\frac12,
\qquad
\int_{\Delta_2}1=\frac12,
\qquad
\int_{\Delta_2}z=\frac16,
\qquad
p_+\wedge q_+=i,
$$

one obtains

$$
w_{\rightarrow}
=\left(0,-\frac23,-\frac23,\frac43\right),
$$

$$
w_{\leftarrow}
=\left(\frac43,-\frac23,-\frac23,0\right).
$$

Their ordered/reflected symmetric representative is

$$
\frac12(w_{\rightarrow}+w_{\leftarrow})
=\left(\frac23,-\frac23,-\frac23,\frac23\right).
$$

Both directed weights give the same contraction with the displayed $H$:

the exact ratio is

$$
\frac{\mathcal R_M[H]}{p_+\wedge q_+}
=-\frac23(h_2+h_3-2)
=\frac{4\epsilon}{3}.
$$

For external letters $X^D,Y^E$, define the ordered derivative contraction by $\langle X^D,Y^E\rangle:=(P_{\dot\alpha}X^D)(P^{\dot\alpha}Y^E)$; the displayed order is part of the definition.

Conditional on the unverified parent, the trial sign convention $\eta_P\eta_W=1$, and an unproved identification of the special-frame tensor with the general external-letter projector, the isolated rank-two evanescent-pole projection would be

$$
\Gamma_{M,CB}^{\mathrm{ev.pole}}
=-\frac{4\lambda_1}{3}
\mathbb F^{AB}{}_{DE}
\langle C_r^D,B_r^E\rangle,
$$

$$
\Gamma_{M,BC}^{\mathrm{ev.pole}}
=+\frac{4\lambda_1}{3}
\mathbb F^{AB}{}_{DE}
\langle B_r^D,C_r^E\rangle.
$$

Thus the conditional trial expression is

$$
\boxed{
\Gamma_{AA,M}^{\mathrm{ev.pole}}
=\frac{4\lambda_1}{3}\mathbb F^{AB}{}_{DE}
\sum_{r=1}^3
\left[
\langle B_r^D,C_r^E\rangle
-\langle C_r^D,B_r^E\rangle
\right].}
$$

This box is neither a derived superspace amplitude nor the full regulated matter result:

$$
\boxed{
\begin{gathered}
\texttt{BLOCKED\_AA\_MATTER\_DWORD\_SIGN\_NORMALIZATION},\\
\texttt{BLOCKED\_LOCKED\_Q4S\_SPINOR\_REALIZATION},\\
\texttt{BLOCKED\_MATTER\_LETTER\_PROJECTORS}.
\end{gathered}}
$$

Machine-readable blockers: `BLOCKED_AA_MATTER_DWORD_SIGN_NORMALIZATION`, `BLOCKED_LOCKED_Q4S_SPINOR_REALIZATION`, `BLOCKED_MATTER_LETTER_PROJECTORS`.

### 4.4 Explicit zero cuts

The two algebraic cuts of the factorized candidate parent are

$$
e_0:
\frac{r_{1+}\wedge r_{2+}}{r_1^2r_2^2},
\qquad
e_1:
-\frac{r_{0+}\wedge r_{2+}}{r_0^2r_2^2}.
$$

Using

$$
B_0(Q^2):=\int_k\frac1{k^2(k-Q)^2},
$$

$$
\int_k\frac{k_m}{k^2(k-Q)^2}
=\frac{Q_m}{2}B_0(Q^2),
$$

both candidate residues vanish because

$$
Q_+\wedge Q_+=0.
$$

The candidate $n=2$ action-seagull numerator used in the downstream arithmetic is

$$
N_{\mathrm{seagull}}=4(r_{0+}\wedge r_{2+}),
$$

and its bubble also vanishes by the same identity.  This does not derive the seagull from the missing graph-specific projector and $D$-word.

A schematic bottom projection of the composite insertion sets $\theta_0=0$ and integrates only the action coordinate.  Conditional on that unproved projector, the two vector-Euler-current bubble numerators are

$$
N_{J_C}=-2(k_+\wedge p_+),
\qquad
\frac{N_{J_C}}{k^2(p-k)^2},
$$

$$
N_{J_B}=-2(k_+\wedge q_+),
\qquad
\frac{N_{J_B}}{k^2(k-q)^2}.
$$

Their exact vector integrals are

$$
\int_k\frac{N_{J_C}}{k^2(p-k)^2}
=-B_0(p^2)(p_+\wedge p_+)=0,
$$

$$
\int_k\frac{N_{J_B}}{k^2(k-q)^2}
=-B_0(q^2)(q_+\wedge q_+)=0.
$$

Conditional on the same source projector, the quadratic letter and outer-connection source term with one $n=1$ matter vertex leaves a source-point vector self-contraction; at zero shift the candidate integral is a scaleless tadpole and vanishes in dimensional regularization.

### 4.5 DRED realization fork

Two incompatible continuations must not be merged.

`NAIVE_FINITE_2X2` applies the four-dimensional Cayley--Hamilton identity to the candidate ansatz before the regulated integral:

$$
\mathsf r_{a\dot a}:=-i(\sigma_E^m)_{a\dot a}r_m,
\qquad
\det(\mathsf r_{a\dot a})
=-\delta_4^{mn}r_mr_n=-r^2.
$$

It cancels $r_0^2$ and $r_1^2$ against the denominators.  The candidate parent then reduces to the two candidate zero bubbles.  In this trial branch, the rank-two finite term is canceled by the rank-zero finite remainder of the same ansatz:

$$
\left.\Gamma_{AA,M}^{\mathrm{full}}\right|_{N_{M,\mathrm{ansatz}}^c}=0.
$$

`Q4S_NO_FIERZ` retains the quasi-four-dimensional spin algebra but forbids finite-$2\times2$ Cayley--Hamilton/Fierz reduction on a dimensionally continued loop vector.  The finite-$2\times2$ determinant ansatz has no defined inverse lift to the unreduced Q4S spinor word.  It therefore proves neither cancellation nor survival of the displayed rank-two term.

The verified base does not select a quasi-four-dimensional spinor realization strong enough to adjudicate this fork:

$$
\boxed{
\texttt{BLOCKED\_LOCKED\_Q4S\_SPINOR\_REALIZATION}.}
$$

Machine-readable status: `BLOCKED_LOCKED_Q4S_SPINOR_REALIZATION`.

$$
\boxed{
\texttt{BLOCKED\_UNREDUCED\_Q4S\_MATTER\_WORD}.}
$$

The fail-closed authority anchors are:

| authority surface | locked statement |
|---|---|
| `contracts/foundations/step-01-supersymmetry-commutator.md:475` | ordinary physical four-dimensional literal $2\times2$ Euclidean sigma matrices only |
| `contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md:1210` | `BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED` |
| `audits/step5a-gap-audit.json:47` | DRED, loop-measure, and evanescent-projector ledger not locked |
| `references/claim-map.yaml:256` | imported Q4S/no-Fierz statement is not Project authority |

No locked $\Pi_{B_r}$ or $\Pi_{C_r}$ source/letter projector occurs on `origin/main`.

The FP, Nielsen--Kallosh, gauge-fixing, source-link, counterterm, evanescent-mixing, and occurrence-resolved contact graph census is also open:

$$
\boxed{\texttt{BLOCKED\_COMPLETE\_AA\_GRAPH\_CENSUS}.}
$$

Machine-readable status: `BLOCKED_COMPLETE_AA_GRAPH_CENSUS`.

## 5. Separated shifts

In the two-coordinate chart $(a,b)$ of the simplex $\Delta_2$ defined in Section 2, define

$$
\mathcal D_{w,z}^{\triangle}(f,g)
:=\int_{\Delta_2}da\,db\,
e^{[z+a(w-z)]\cdot P}P_{\dot\alpha}f\,
e^{[w+b(z-w)]\cdot P}P^{\dot\alpha}g.
$$

The simplex moment is

$$
\int_{\Delta_2}da\,db\,a^nb^m
=\frac{n!m!}{(m+n+2)!}.
$$

Therefore

$$
\mathcal D_{w,z}^{\triangle}(f,g)
=\sum_{m,n\ge0}\frac1{(m+n+2)!}
e^{z\cdot P}((w-z)\cdot P)^nP_{\dot\alpha}f
e^{w\cdot P}((z-w)\cdot P)^mP^{\dot\alpha}g.
$$

At zero shift,

$$
\mathcal D_{0,0}^{\triangle}(f,g)
=\frac12P_{\dot\alpha}fP^{\dot\alpha}g.
$$

For $m,n\ge0$, the coefficient that distributes $k$ and $l$ derivatives onto the first output is

$$
T_{m,n;k,l}^{\mathrm{HT}}
=\frac{\binom mk\binom nl}
{(m+n+2)(k+l+1)}.
$$

The Project denominator identity contains the Feynman-parameter measure factor $\Gamma(3)=2$.  Hence the Project parameter-measure kernel is

$$
\boxed{
K_{m,n;k,l}^{P}
=2T_{m,n;k,l}^{\mathrm{HT}}
=\frac{2\binom mk\binom nl}
{(m+n+2)(k+l+1)}.}
$$

In particular,

$$
K_{0,0;0,0}^{P}=1.
$$

### 5.1 Relative-normalization obstruction

Define the conditional trial coefficients

$$
c_G^{\mathrm{trial}}:=\frac18,
\qquad
c_M^{\mathrm{trial}}:=\frac43.
$$

Write the diagonal, no-derivative trial component dictionary factors as

$$
b_H=\alpha_AA_P,
\qquad
(\partial_{\dot a}c)_H=\alpha_DD_{P,\dot a},
$$

$$
(\beta_I)_H=\alpha_BU_I{}^rB_{r,P},
\qquad
(\gamma^I)_H=\alpha_C(U^{-1})_s{}^IC_{s,P},
\qquad
\partial_{\dot a}^H=\alpha_PP_{\dot a}^P.
$$

Then

$$
U_I{}^r(U^{-1})_s{}^I=\delta^r{}_s,
$$

so neither the flavor sum nor the common loop/color/source scale changes the relative coefficient.  If both trial amplitudes and a component dictionary were derived, matching would require

$$
\boxed{
\frac{c_M^{\mathrm{trial}}}{c_G^{\mathrm{trial}}}
=\frac{\alpha_P\alpha_B\alpha_C}
{\alpha_D\alpha_A}.}
$$

For one compact-superfield rescaling

$$
\mathcal C_H(\theta_H)=s\mathcal C_P(\theta_P),
\qquad
\theta_H=t\theta_P,
\qquad
\partial_H=pP_P,
$$

the component factors are

$$
\alpha_A=\frac{s}{t^3},
\quad
\alpha_B=\frac{s}{t^2},
\quad
\alpha_C=\frac{s}{t},
\quad
\alpha_D=sp,
\quad
\alpha_P=p,
$$

and hence

$$
\frac{\alpha_P\alpha_B\alpha_C}
{\alpha_D\alpha_A}=1.
$$

The common Feynman-parameter measure factor $2$, the common loop scale, the flavor frame, and every uniform compact-superfield rescaling would leave the conditional trial ratio

$$
\frac{c_M^{\mathrm{trial}}}{c_G^{\mathrm{trial}}}
=\frac{4/3}{1/8}
=\frac{32}{3}
$$

unchanged.  Its status is `CONDITIONAL_TRIAL_RATIO`; it is not an exact Project--HT mismatch.  Absorbing this trial ratio would require an independently derived nonuniform intertwiner satisfying

$$
\alpha_P\alpha_B\alpha_C
=\frac{32}{3}\alpha_D\alpha_A.
$$

No such locked dictionary exists:

$$
\boxed{
\texttt{BLOCKED\_TOTAL\_PROJECT\_HT\_COMPONENT\_INTERTWINER}.}
$$

Machine-readable status: `BLOCKED_TOTAL_PROJECT_HT_COMPONENT_INTERTWINER`.

## 6. Current mismatch ledger

| item | recorded value | state |
|---|---:|---|
| old WW coefficient | $\lambda_1$ | `REJECTED_PROPAGATOR_NORMALIZATION__REJECTED_BY_EVIDENCE__EXACT_FACTOR_8` |
| pure-gauge candidate cut orbit | $\lambda_1/8$ per ordered output | `CONDITIONAL_ARITHMETIC_ON_RECORDED_PRIMITIVES` |
| matter candidate rank-two pole | $4\lambda_1/3$ per ordered flavor output | `CONDITIONAL_SPECIAL_FRAME_ARITHMETIC` |
| matter finite-$2\times2$ candidate parent | $0$ | `CONDITIONAL_ON_UNVERIFIED_DWORD_ANSATZ` |
| matter Q4S no-Fierz defect | undetermined | `BLOCKED_UNREDUCED_Q4S_MATTER_WORD` |
| HT shifted kernel at zero shift | $1/2$ | `SOURCE_BRANCH` |
| Project parameter-measure kernel at zero shift | $1$ | `DERIVED_PARAMETER_MEASURE_ARITHMETIC` |
| relative matter/gauge trial coefficient | $32/3$ | `CONDITIONAL_TRIAL_RATIO__BLOCKED_TOTAL_PROJECT_HT_COMPONENT_INTERTWINER` |

No final $AA$ coefficient is accepted until the matter DRED fork, the complete occurrence-resolved cut orbit, and the relative gauge/matter normalization are closed without using the HT target.

## 7. GPT Pro initial-gate adjudication

Initial prompt SHA-256:

`48314dda34aaba5c2afd433c3dc2e31b5f8fd8f41e3266fef7f4659dd2531977`.

Derivation correction prompt SHA-256:

`0814aa50d9bbe3f28897326285432b85192bda855fab6242496d7c3f889e6a33`.

| Pro claim | Project-side check | verdict |
|---|---|---|
| $V=\sqrt2gu$ and $\Phi=g\Phi_c$ | follows from the locked quadratic kernels | `ACCEPTED_WITH_LOCAL_PROOF` |
| pure-gauge coefficient $\lambda_1$ | canonical magnitudes give the conditional coefficient $\lambda_1/8$; its $D$-word sign and full orbit remain blocked | `REJECTED_NORMALIZATION__FULL_REPLACEMENT_BLOCKED` |
| matter coefficient represented by $\chi_M$ | neither the matter $D$-word parent nor its Q4S lift is derived | `BLOCKED_MISSING_DERIVATION_AND_AUTHORITY` |
| simplex coefficient $[(m+n+2)(k+l+1)]^{-1}$ | independently integrated and exhaustively checked for $0\le m,n\le4$ | `ACCEPTED_WITH_LOCAL_PROOF` |
| displayed full $AA$--HT match | both diagram sectors, the auxiliary graph census, and the component intertwiner remain open | `REJECTED_BY_EVIDENCE` |

The first incorrect line in the Pro calculation is `proposals/gpt-pro-aa-standard-feynman-2026-07-14.md:117`: after declaring canonical $u$ and the auxiliary insertion $X=\sqrt2A/g$, it retains two $ig/(2\hbar)$ Hessians.  The canonical Hessian magnitudes are $g/(4\hbar)$.  It also retains insertion magnitude $1/32$ and closed-word magnitude $2$ at lines 363--400, whereas the candidate canonical magnitudes are $1/64$ and $1$.  The promised $X\to A$ output conversion is never applied.  Hence the exact ratio between Pro's normalization and the conditional canonical normalization is

$$
\frac{\Gamma_{G,\mathrm{Pro}}^{\mathrm{norm}}}{\Gamma_{G,\mathrm{candidate}}^{\mathrm{norm}}}
=\frac{(g^2/4)(2)}{(g^2/16)(1)}
=4\cdot2
=8.
$$

This differs from the earlier WW-seed error, where assigning a unit propagator to $v_{\rm old}=V/(2g)$ also produced the numerical factor $2^3=8$ through three internal vector lines.

The Pro notation defines $D_{\dot\alpha}=P_{\dot\alpha}U$ at lines 21--25 without defining $U$ or tying it to the canonical external letter $g^{-1}\widetilde{\mathcal W}_{\dot\alpha}$.  Its matter orientation at lines 756--789 is $C_r^D\to B_r^E$, but its projector at lines 883--906 is labeled $\Pi_{B_r^DC_r^E}$; the forward/reverse output labels are interchanged.  Lines 948--980 do not evaluate the announced complete $D$-word: they introduce an unspecified tensor $\mathcal R_{mn}$ instead of deriving the Section 4.2 numerator.  Lines 983--993 then discard the rank-one and rank-zero terms solely because they have no pole, although the Section 4.5 finite-$2\times2$ branch requires the rank-zero finite term to cancel the rank-two evanescent-pole term.  Consequently the claimed contact identity at lines 1047--1064 has no displayed cut algebra and does not detect the regulator fork.  At lines 1075--1097 the opposite forward/reverse signs are definitions, not consequences of a calculated orientation ledger.

The derivation gate requires an occurrence-resolved gauge $D$-word, a derived matter parent, and closure of the ghost, Nielsen--Kallosh, gauge-fixing, source-completion, and evanescent-counterterm census before making any full-result claim.

## 8. GPT Pro derivation-gate adjudication

The completed correction is archived at `proposals/gpt-pro-aa-derivation-correction-2026-07-14.md` under prompt SHA-256

`0814aa50d9bbe3f28897326285432b85192bda855fab6242496d7c3f889e6a33`.

| corrected Pro claim | Project-side check | verdict |
|---|---|---|
| pure-gauge coefficient $\lambda_1/8$ | Sections 2--3 verify only conditional arithmetic; the global odd-$D$ sign and full orbit are not derived | `REJECTED_AS_FULL_AMPLITUDE__CONDITIONAL_ONLY` |
| initial gauge normalization was $8$ times the conditional canonical normalization | $(g^2/4)2\,/\,[(g^2/16)1]=8$ | `ACCEPTED_ARITHMETIC_ONLY` |
| finite-$2\times2$ matter parent is zero | the reduction starts from `UNVERIFIED_DWORD_ANSATZ` | `REJECTED_AS_ESTABLISHED_CHECK__CONDITIONAL_ONLY` |
| standard consistent DRED selects Q4S/no-Fierz | supported externally, but not admitted by `origin/main` | `BLOCKED_MISSING_AUTHORITY` |
| full Q4S matter coefficient is not fixed by the supplied numerator | the unreduced Q4S spinor word and pointwise rank-zero tensor are missing | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |
| $K^P=2T^{\rm HT}$ and $K^P_{0,0;0,0}=1$ | independently integrated and exhaustively checked | `ACCEPTED_WITH_LOCAL_PROOF` |
| explicit numerical Project--HT component map | no admitted component intertwiner exists | `BLOCKED_MISSING_AUTHORITY` |
| complete $AA$ occurrence census | ghost, NK, gauge-fixing, counterterm, evanescent mixing, and raw port rows remain open | `BLOCKED_MISSING_AUTHORITY` |

The correction's formal Branch-B expansion begins by polarizing an object called $\det$ before defining that object in Q4S.  It therefore cannot supply the missing Q4S numerator.  Its displayed $4\lambda_1/3$ coefficient is only the special-frame downstream arithmetic consequence of `CONDITIONAL_PARENT_DEFINITION`, not an established isolated pole and not the full regulated matter answer.

## 9. GPT Pro final-gate adjudication

The completed settlement is archived at `proposals/gpt-pro-aa-final-settlement-2026-07-14.md` under prompt SHA-256

`1efd04011130a3f64f4e57e42bc58fc1d0aa576af8bc8e7eb68b7f0eaab1f90b`.

| final Pro claim | Project-side check | verdict |
|---|---|---|
| `GAUGE ACCEPTED` with $\lambda_1/8$ | the negative Hessian--propagator product requires an unproved global odd-$D$ sign; four cut transports, the reflected port, and the contact/longitudinal orbit are not derived | `REJECTED_AS_OVERCLAIM__CONDITIONAL_ARITHMETIC_ONLY` |
| finite-$2\times2$ matter result $0$ is an established check | it follows only after applying Cayley--Hamilton to `UNVERIFIED_DWORD_ANSATZ` | `REJECTED_AS_OVERCLAIM__CONDITIONAL_PARENT_ONLY` |
| isolated Q4S rank-two pole is exactly $4\lambda_1/3$ | the parent, $\eta_W\eta_P$, general tensor identity, and Q4S inverse lift are absent | `REJECTED_AS_OVERCLAIM__SPECIAL_FRAME_ARITHMETIC_ONLY` |
| unreduced Q4S matter word is missing | the finite determinant ansatz does not define its Q4S inverse image | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |
| complete graph census is open | FP, NK, gauge-fixing, source-link, counterterm, and evanescent-mixing data are absent | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |
| Project--HT component intertwiner is missing | no admitted component extraction fixes the $\alpha$-factors | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |
| full $AA$ match is blocked | neither diagram sector nor the auxiliary census is complete | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |

## 10. Derivation-gap audit

Gap types are `G-SIGN` (sign), `G-OP` (operator ordering), `G-DEF` (missing definition), `G-PROJ` (projection), `G-NORM` (normalization), `G-ALG` (algebra), and `G-SCOPE` (unproved scope extension).  Severity `P0` blocks the claimed amplitude; `P1` blocks completion or generalization.

Equation-group check: `121/121` displayed groups were checked for dependency and claim status.  Three representative groups were independently recomputed:

| checked group | exact check | status |
|---|---|---|
| canonical vector rescaling | $v_{\rm old}=u/\sqrt2$ gives three-line factor $2^3=8$ | `PASS` |
| universal triangle tensor pole | the Feynman-parameter factor $2$ and tensor factor $1/4$ give $\widehat\delta^{mn}/(16\pi^2\epsilon)$ | `PASS` |
| simplex derivative kernel | the beta integral gives $n!m!/(m+n+2)!$ and the Project measure gives $K^P=2T^{\rm HT}$ | `PASS` |

| gap id | type | severity | exact missing derivation | state |
|---|---|---:|---|---|
| `AA-G1` | `G-SIGN/G-OP` | `P0` | triangle endpoint products are $+1$; $s_{T,\rm global}=-1$ is not derived | `OPEN` |
| `AA-G2` | `G-SIGN/G-OP` | `P1` | the four cut transport signs $(-,+,+,-)$ have no ordered-word trace | `OPEN` |
| `AA-G3` | `G-SCOPE/G-OP` | `P1` | reflected source-port map and equality of EOM/contact/longitudinal residues are absent | `OPEN` |
| `AA-G4` | `G-DEF/G-PROJ` | `P0` | $\delta_{ij}(r)$, endpoint $D_i(r),\bar D_i(r)$, $\theta_0$ projection, $\Pi_{B_r}$, and $\Pi_{C_r}$ are not defined | `OPEN` |
| `AA-G5` | `G-ALG/G-SIGN/G-NORM` | `P0` | sixteen matter monomials, $\eta_W$, $\eta_P$, and the stripped prefactor are not emitted from the superspace word | `OPEN` |
| `AA-G6` | `G-PROJ/G-SCOPE` | `P1` | the frame $p=e_1,q=e_4$ with diagonal $H$ is not promoted to a general tensor identity | `OPEN` |
| `AA-G7` | `G-SCOPE` | `P0` | the finite-$2\times2$ parent has no defined inverse lift to an unreduced Q4S word | `OPEN` |
| `AA-G8` | `G-SCOPE/G-OP` | `P0` | FP, NK, gauge-fixing, source-link, counterterm, evanescent-mixing, and contact occurrences are not closed | `OPEN` |
| `AA-G9` | `G-DEF/G-NORM` | `P1` | Project component extraction does not determine the Project--HT $\alpha$-factors | `OPEN` |
| `AA-G10` | `G-DEF/G-SCOPE` | `P0` | proper slice, ordered bilocal source, background/quantum ports, and DRED contract are not locked | `OPEN` |

Repair queue:

1. Lock the perturbative slice, ordered source, port grammar, and DRED contract.
2. Emit graph-specific gauge and matter noncommutative $D$-word traces with every occurrence and sign.
3. Derive the unreduced Q4S matter numerator and a general external-momentum tensor projection.
4. Close the FP, NK, gauge-fixing, source-link, counterterm, evanescent-mixing, and contact graph census.
5. Derive the Project--HT component intertwiner from admitted component projectors.
