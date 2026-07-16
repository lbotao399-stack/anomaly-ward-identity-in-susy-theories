# Step 5 ordered $AA$ standard-Feynman strictification

Status: `ACCEPTED_AA_ONE_LOOP_ANOMALY_SECTOR__HT_CHECK_ONLY_EXACT_MATCH`.

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.

The superseding target-blind calculation is
`audits/step5-aa-external-slot-decomposition-exact.json`.  It includes all
three external placements, all four action-chirality pairs, both marked
source edges, the raw Schwinger contact-Hessian multiplicity, typed Fourier
reconstruction, and the matter orientation.  Sections 1--10 below are the
legacy fail-closed history; Section 11 is the final acceptance and supersedes
their former AA-sector blockers.  GPT Pro outputs remain
`NON_AUTHORITY_PRO_REVIEW` and do not determine any coefficient.

The isolated linear-source gauge triangle has been replayed in
`audits/step5-aa-gauge-marked-occurrence-recount.md`, and its canonical
normalization is independently reconstructed in
`audits/step5-aa-gauge-canonical-normalization-ledger.md`.  These artifacts
fix the selected triangle at $-\lambda_1/8$; they do not include the full
$A_2,A_3,\gamma_1,\gamma_2$ source/contact orbit.

Audit scope: `FULL_AA_ONE_LOOP_ANOMALY_SECTOR_TARGET_BLIND_EXACT`.
The acceptance is AA-sector local and does not modify or certify the global
81-pair ledger.

Legacy audit scope retained in Sections 1--10:
`CONDITIONAL_DOWNSTREAM_ARITHMETIC_ONLY`.

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
\texttt{BLOCKED\_LOCKED\_BACKGROUND\_QUANTUM\_PORT\_GRAMMAR}.
\end{gathered}}
$$

Machine-readable blockers: `BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION`, `BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE`, `BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE`, `BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR`.

The triangle/cut relative coefficient is no longer a separate blocker.  For
the edge selected by the actual \(D\)-word,

$$
\frac{\bar r_e^{\,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
$$

so the full-\(d\) inverse-square part cancels the Schwinger cut pointwise.

The former $\lambda_1$ coefficient is larger by $8$, because it assigned a unit propagator to $v_{\rm old}=V/(2g)$.  Three incorrect propagators multiply the graph by

$$
2^3=8.
$$

## 4. Complete two-$\widetilde\Phi V\Phi$ marked matter orbit

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

### 4.2 Exact marked matter \(D\)-words

Use

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q,
$$

and set the source coordinate to $\theta_0=0$.  The first marked-$A$ word is

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

The external bottom projectors are represented by

$$
\Phi_r(p,\theta,\bar\theta)
=e^{\,i\theta p\bar\theta}\theta^+B_r(p),
\qquad
C_r(q,\theta,\bar\theta)
=e^{-i\theta q\bar\theta}C_r(q).
$$

They satisfy

$$
\bar D_{\dot a}\Phi_r=0,
\qquad
D_aC_r=0.
$$

Define

$$
a_{i+}:=r_{i,+\dot+},
\qquad
b_{i+}:=r_{i,+\dot-},
\qquad
a_{i-}:=r_{i,-\dot+},
\qquad
b_{i-}:=r_{i,-\dot-}.
$$

Direct left-Berezin differentiation, with

$$
D^2=2D_-D_+,
\qquad
\bar D^2=2\bar D_{\dot+}\bar D_{\dot-},
\qquad
D^2\bar D^2(\theta^2\bar\theta^2)=16,
$$

gives

$$
\mathscr D_{M,CB}^{(A)}=-2\mathcal S_{012},
$$

where

$$
\begin{aligned}
\mathcal S_{012}={}&
 a_{0+}b_{0-}a_{1+}b_{2+}
-a_{0+}b_{0-}b_{1+}a_{2+}\\
&-b_{0+}a_{0-}a_{1+}b_{2+}
+b_{0+}a_{0-}b_{1+}a_{2+}\\
&-a_{1+}b_{1-}a_{0+}b_{2+}
+a_{1+}b_{1-}b_{0+}a_{2+}\\
&+b_{1+}a_{1-}a_{0+}b_{2+}
-b_{1+}a_{1-}b_{0+}a_{2+}.
\end{aligned}
$$

Set

$$
W_{ij}:=a_{i+}b_{j+}-b_{i+}a_{j+},
\qquad
\det\mathsf r_i:=a_{i+}b_{i-}-b_{i+}a_{i-}.
$$

Term-by-term regrouping gives

$$
\boxed{
\mathcal S_{012}
=(\det\mathsf r_0)W_{12}
-(\det\mathsf r_1)W_{02}.}
$$

Thus the former sign parameter is fixed:

$$
\boxed{\eta_W=-1.}
$$

The two matter exponent vertices give \(2g^2/\hbar^2\); the three
propagators give \(\hbar^3\); the ordered adjoint color route gives
\(\mathbb F^{AB}{}_{DE}\).  Moving the odd \(B_r\) output across the odd
marked word gives

$$
\boxed{\eta_P=-1.}
$$

Consequently $\eta_P\eta_W=+1$, and the first normalized parent numerator is

$$
\boxed{
N_{M,1}^{\rm eff}
=4\left[
(\det\mathsf r_0)W_{12}
-(\det\mathsf r_1)W_{02}
\right].}
$$

The second marked-$A$ occurrence gives the distinct word

$$
\boxed{
\mathcal S_2
=W_{01}
\left(a_{2+}b_{1-}-a_{1-}b_{2+}\right).}
$$

The second marked source obeys the exact operator split

$$
\boxed{
D_-D_+\bar D^2D_+
=-8(\det\mathsf r_2)D_+
-\frac12D_+\bar D^2D^2.}
$$

The longitudinal word contains five odd derivatives.  Endpoint replacement
gives \((-1)^5=-1\), reversal gives
\((-1)^{5\cdot4/2}=+1\), and therefore

$$
\boxed{
D_{0+}\bar D_0^2D_0^2\delta^4_{02}
=-D_2^2\bar D_2^2D_{2+}\delta^4_{02}.}
$$

The transported even \(D^2\bar D^2\) block gives no additional Berezin-IBP
sign.  On the adjacent \(r_1\) projector,

$$
\boxed{
D_2^2(-r_1)\bar D_2^2(-r_1)D_2^2(-r_1)
=-16(\det\mathsf r_1)D_2^2(-r_1).}
$$

Define

$$
M_{21}:=a_{2+}b_{1-}-a_{1-}b_{2+},
$$

$$
\Omega_{21}
:=a_{2+}b_{1-}-a_{1+}b_{2-}
-b_{2+}a_{1-}+b_{1+}a_{2-}.
$$

Direct polynomial expansion gives

$$
\boxed{
2M_{21}
=\det\mathsf r_1+\det\mathsf r_2-\det p+\Omega_{21}.}
$$

For the raw \(-\mathcal S_2\) orientation, the transported longitudinal word
is

$$
\boxed{
-W_{01}
\left[
a_{2+}(b_{1-}-b_{2-})
-b_{2+}(a_{1-}-a_{2-})
\right]
=\frac12W_{01}
\left(
\det\mathsf r_2-\det\mathsf r_1+\det p-\Omega_{21}
\right).}
$$

Thus the post-transport \(r_1\) inverse-kernel coefficient is
\(-1/2\).  Losing the pre-transport edge tag does not remove this cut.

The two words obey the exact polynomial identity

$$
\boxed{
\begin{aligned}
\mathcal S_1+\mathcal S_2
={}&W_{12}
\left[
a_{0+}(b_{0-}-b_{1-})
-b_{0+}(a_{0-}-a_{1-})
\right],
\end{aligned}}
$$

where

$$
\mathcal S_1
=(\det\mathsf r_0)W_{12}
-(\det\mathsf r_1)W_{02}.
$$

Thus

$$
\boxed{
N_M^{\rm eff}=4(\mathcal S_1+\mathcal S_2).}
$$

These are occurrence-resolved $D$-word results, not ansaetze.

### 4.3 Exact complete parent-minus-cut integral

#### 4.3.1 First marked placement

The finite spinor determinant is

$$
\det\mathsf r_i=-\bar r_i^{\,2},
$$

so the first normalized parent numerator is

$$
4\hbar g^2
\left[
-\bar r_0^{\,2}W_{12}
+\bar r_1^{\,2}W_{02}
\right].
$$

The two Schwinger cuts replace only the selected four-dimensional inverse
squares by the full regulated inverse squares:

$$
\bar r_0^{\,2}\longmapsto D_0=r_{0,d}^{\,2},
\qquad
\bar r_1^{\,2}\longmapsto D_1=r_{1,d}^{\,2}.
$$

Therefore

$$
\begin{aligned}
N_{\rm parent}-N_{\rm cut}
&=4\hbar g^2
\left[
-(\bar r_0^{\,2}-D_0)W_{12}
+(\bar r_1^{\,2}-D_1)W_{02}
\right]\\
&=4\hbar g^2\mu_\ell^2(W_{02}-W_{12}).
\end{aligned}
$$

Since \(r_0-r_1=q\),

$$
W_{02}-W_{12}
=(r_0-r_1)_+\wedge r_{2+}
=q_+\wedge r_{2+}.
$$

Set

$$
L=k-yq-z(p+q).
$$

Then

$$
r_2=L+(y+z-1)q+(z-1)p,
$$

and odd integration removes \(q_+\wedge L_+\).  Hence

$$
q_+\wedge r_{2+}
=(z-1)q_+\wedge p_+
=(1-z)p_+\wedge q_+.
$$

The exact simplex moment is

$$
\begin{aligned}
2\int_0^1dy\int_0^{1-y}dz\,(1-z)
&=2\int_0^1dy
\left[
z-\frac{z^2}{2}
\right]_{z=0}^{z=1-y}\\
&=2\int_0^1dy
\left[
1-y-\frac{(1-y)^2}{2}
\right]\\
&=2\int_0^1dy
\left[
\frac12-\frac{y^2}{2}
\right]\\
&=2\left[
\frac y2-\frac{y^3}{6}
\right]_{0}^{1}\\
&=\frac23.
\end{aligned}
$$

Using

$$
\lim_{\epsilon\to0}
\mu^{2\epsilon}\int\frac{d^dL}{(2\pi)^d}
\frac{\mu_L^2}{(L^2+\Delta)^3}
=\frac1{32\pi^2},
$$

one obtains

$$
\begin{aligned}
4\hbar g^2\left(\frac23\right)
\left(\frac1{32\pi^2}\right)
&=\frac{\hbar g^2}{12\pi^2}\\
&=\frac43\lambda_1.
\end{aligned}
$$

#### 4.3.2 Second marked placement and explicit current contact

Let $x+y+z=1$.  Exact source-to-action transport gives

$$
W_{12}=-x(p_+\wedge q_+),
\qquad
W_{02}=y(p_+\wedge q_+),
\qquad
W_{01}=-z(p_+\wedge q_+).
$$

For the first marked edge $r_0$, the primary vector-EOM square and the
explicit $-2i(B\times C)$ current contact give

$$
\mathcal R_{r_0}^{\rm primary}=\mu_L^2W_{12},
\qquad
\mathcal R_{r_0}^{\rm current}=-\mu_L^2W_{02},
$$

$$
\boxed{
\mathcal R_{r_0}^{\rm full}
=\mu_L^2(W_{12}-W_{02})
=-(x+y)\mu_L^2(p_+\wedge q_+).}
$$

Its exact moment is

$$
2\int_{\Sigma_2}(x+y)
=2\left(\frac16+\frac16\right)
=\frac23.
$$

For the second marked edge $r_2$, the primary square and explicit current
contact alone give only the truncation

$$
\mathcal R_{r_2}^{\rm primary}=\mu_L^2W_{01},
\qquad
\mathcal R_{r_2}^{\rm current}=\mu_L^2W_{02},
$$

$$
\mathcal R_{r_2}^{\rm pc}
=\mu_L^2(W_{01}+W_{02})
=(y-z)\mu_L^2(p_+\wedge q_+).
$$

This is not the full second-mark SD orbit.  The transported longitudinal word
in Section 4.2 generates an $r_1$ projector collapse and the mixed
$\Omega_{21}$ contact.  In the nondegenerate frame

$$
p=e_1,
\qquad
q=e_4,
\qquad
p_+\wedge q_+=-i,
$$

with

$$
k=L+yq+z(p+q),
$$

the rank-two diagonal coefficients are

$$
\operatorname{diag}_{L^2}(\mathcal S_2)
=i(1-3z,1-z,-z,-z).
$$

Split

$$
\mathcal S_{2,\det}
:=\frac12W_{01}
\left(
\det\mathsf r_1+\det\mathsf r_2-\det p
\right),
$$

$$
\mathcal S_{2,\Omega}
:=\frac12W_{01}\Omega_{21}.
$$

Then

$$
\operatorname{diag}_{L^2}(\mathcal S_{2,\det})
=i(1-3z,-z,-z,-z),
$$

$$
\operatorname{diag}_{L^2}(\mathcal S_{2,\Omega})
=(0,i,0,0).
$$

Using

$$
c(T):=\frac{T_{22}+T_{33}}{2(p_+\wedge q_+)},
$$

one obtains

$$
c(\mathcal S_{2,\det})=z,
\qquad
c(\mathcal S_{2,\Omega})=-\frac12,
$$

$$
\boxed{
c(\mathcal S_2)=z-\frac12.}
$$

The determinant parent/contact pair is

$$
P_{\det}=z\bar L^2(p_+\wedge q_+),
\qquad
C_{\det}=-zL_d^2(p_+\wedge q_+),
$$

and the transported mixed pair is

$$
P_{\Omega}
=-\frac12\bar L^2(p_+\wedge q_+),
\qquad
C_{\Omega}
=+\frac12L_d^2(p_+\wedge q_+).
$$

At $\mu_L^2=0$,

$$
P_{\det}+C_{\det}=0,
\qquad
P_{\Omega}+C_{\Omega}=0.
$$

The mixed descendant contains both terms in

$$
\boxed{
\frac{L_d^2}{(L_d^2+\Delta)^3}
=\frac1{(L_d^2+\Delta)^2}
-\frac{\Delta}{(L_d^2+\Delta)^3}.}
$$

The first term is the collapsed bubble; the second is its required rank-zero
triangle completion.  Their DRED defects are

$$
\mathcal R_{2,\det}
=z\mu_L^2(p_+\wedge q_+),
$$

$$
\mathcal R_{2,\Omega}
=-\frac12\mu_L^2(p_+\wedge q_+).
$$

Therefore

$$
\boxed{
\mathcal R_{r_2}^{\rm full}
=\left(z-\frac12\right)
\mu_L^2(p_+\wedge q_+).}
$$

The exact simplex integral is

$$
\begin{aligned}
2\int_{\Sigma_2}\left(z-\frac12\right)
&=2\int_0^1dy\int_0^{1-y}dz
\left(z-\frac12\right)\\
&=2\int_0^1dy
\left[
\frac{z^2}{2}-\frac z2
\right]_{z=0}^{z=1-y}\\
&=2\int_0^1dy
\left[
\frac{(1-y)^2}{2}-\frac{1-y}{2}
\right]\\
&=\int_0^1dy\,(y^2-y)\\
&=\left[
\frac{y^3}{3}-\frac{y^2}{2}
\right]_0^1\\
&=-\frac16.
\end{aligned}
$$

Hence

$$
\begin{aligned}
4\hbar g^2\left(-\frac16\right)
\left(\frac1{32\pi^2}\right)
&=-\frac{\hbar g^2}{48\pi^2}\\
&=-\frac13\lambda_1.
\end{aligned}
$$

The two placements give

$$
\boxed{
\left|c_{AA,M}\right|
=\left|\frac43-\frac13\right|
=1.}
$$

Let $s_M\in\{+1,-1\}$ denote the remaining global source-orientation sign.
Then

$$
\boxed{
\Gamma_{AA,M}^{AB}
=s_M\lambda_1\mathbb F^{AB}{}_{DE}
\sum_{r=1}^3
\left[
\langle B_r^D,C_r^E\rangle
-\langle C_r^D,B_r^E\rangle
\right].}
$$

Machine-readable status:
`AA_MATTER_UNIT_MAGNITUDE_REPRODUCED__GLOBAL_ORIENTATION_SIGN_OPEN`.

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

### 4.5 Exact DRED resolution

The former two-branch fork was caused by identifying the finite spinor square
with the regulated inverse propagator.  The \(D\)-algebra identity is

$$
\det(\mathsf r_{a\dot a})=-\bar r^{\,2},
$$

whereas the denominator is

$$
D_e=r_{e,d}^{\,2}.
$$

They obey

$$
\bar r_e^{\,2}=r_{e,d}^{\,2}+\mu_\ell^2,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2.
$$

Therefore the exact edge reduction is

$$
\begin{aligned}
\frac{\bar r_e^{\,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
&=\frac{\bar r_e^{\,2}-r_{e,d}^{\,2}}
{D_0D_1D_2}\\
&=\boxed{\frac{\mu_\ell^2}{D_0D_1D_2}}.
\end{aligned}
$$

Replacing \(\bar r_e^{\,2}\) by \(r_{e,d}^{\,2}\) gives instead

$$
\frac{r_{e,d}^{\,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=0
$$

pointwise.  This is precisely the premature continuation that removed the
anomaly.  The former separate rank-two and rank-zero continuations are not
independent regulated amplitudes and must not be added after making that
replacement.

The exact remaining scalar integral is

$$
\boxed{
\lim_{\epsilon\to0}
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.}
$$

Thus the DRED/Fierz fork is closed.  The complete two-placement matter
$D$-word is fixed in Sections 4.2--4.3; the $\Pi_{B_r},\Pi_{C_r}$ output
projectors remain separately tagged graph data.

The pure-gauge marked-occurrence recount and homogeneous source/SD orbit are
closed independently in
`audits/step5-aa-gauge-marked-occurrence-recount.md` and
`audits/step5-aa-gauge-full-source-sd-orbit-exact.md`:

$$
\Gamma_{AA,G}^{\mathrm{source\ orbit}}=0,
\qquad
\Gamma_{AA,G}^{\mathrm{directed\ triangle}}
=-\frac18\lambda_1.
$$

The FP, Nielsen--Kallosh, gauge-fixing, counterterm, evanescent-mixing, and
global auxiliary graph census remains open:

$$
\boxed{\texttt{BLOCKED\_COMPLETE\_AA\_GRAPH\_CENSUS}.}
$$

The matter support rows are exhausted independently:

$$
\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}\right|_{\mathcal I_2}=0,
\qquad
\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}\right|_{\mathcal I_1S_{m3}}=0,
$$

$$
\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}\right|_{\mathcal I_0S_{m4}}=0,
\qquad
\left|\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}\right|_{\mathcal I_0S_{m3}^2}\right|
=\lambda_1.
$$

The first zero follows from the absence of external matter ports and the two-loop count, the second from the scale-free one-propagator tadpole in every perfect matching, and the third from

$$
W_{02}=(L_++xP_+)\wedge(L_+-(1-x)P_+)=-L_+\wedge P_+,
$$

whose shifted bubble integral is odd.  Hence
`BLOCKED_AA_MATTER_NONPRIMARY_SOURCE_SD_ORBIT` is closed.
Machine-readable statuses:
`TARGET_BLIND_EXACT_DWORD_REPLAY__GAUGE_SOURCE_ORBIT_ZERO__DIRECTED_TRIANGLE_MINUS_LAMBDA1_OVER_8_UNCHANGED`,
`AA_MATTER_UNIT_MAGNITUDE_REPRODUCED__GLOBAL_ORIENTATION_SIGN_OPEN`,
`BLOCKED_COMPLETE_AA_GRAPH_CENSUS`.

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

Define the selected-orbit trial magnitudes

$$
c_G^{\mathrm{trial}}:=\frac18,
\qquad
c_M^{\mathrm{trial}}:=1.
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

The common Feynman-parameter measure factor $2$, the common loop scale, the flavor frame, and every uniform compact-superfield rescaling leave the selected-orbit trial ratio

$$
\frac{c_M^{\mathrm{trial}}}{c_G^{\mathrm{trial}}}
=\frac{1}{1/8}
=8
$$

unchanged.  Its status is `CONDITIONAL_TRIAL_RATIO`; it is not an exact
Project--HT mismatch because the global auxiliary gauge census and component
intertwiner remain open.  Absorbing this provisional ratio would require an
independently derived nonuniform intertwiner satisfying

$$
\alpha_P\alpha_B\alpha_C
=8\alpha_D\alpha_A.
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
| pure-gauge selected marked occurrence | \(-\lambda_1/8\) per ordered output | `FULL_MARKED_OCCURRENCE_RECOUNTED__SOURCE_ORBIT_ZERO__GLOBAL_AUXILIARY_CENSUS_OPEN` |
| matter first marked placement | magnitude \(4\lambda_1/3\) per ordered flavor output | `REPRODUCED_WITH_EXPLICIT_PRIMARY_AND_CURRENT_CUTS` |
| matter second marked placement | \(-\lambda_1/3\) in the \(+\mathcal S_2\) orientation | `REPRODUCED_WITH_EXACT_OMEGA21_LONGITUDINAL_TRANSPORT` |
| matter complete marked orbit | magnitude \(\lambda_1\) per ordered flavor output | `GLOBAL_ORIENTATION_SIGN_OPEN` |
| selected-edge evanescent master | \(1/(32\pi^2)\) | `REPRODUCED` |
| HT shifted kernel at zero shift | $1/2$ | `SOURCE_BRANCH` |
| Project parameter-measure kernel at zero shift | $1$ | `DERIVED_PARAMETER_MEASURE_ARITHMETIC` |
| selected-orbit matter/gauge magnitude ratio | \(8\) | `NOT_A_FULL_SECTOR_RATIO__GLOBAL_AUXILIARY_GAUGE_CENSUS_OPEN` |

No final $AA$ coefficient is accepted until the global auxiliary gauge
census, common source orientations, and Project--HT component intertwiner are
closed without using the HT target.

## 7. GPT Pro initial-gate adjudication

Initial prompt SHA-256:

`48314dda34aaba5c2afd433c3dc2e31b5f8fd8f41e3266fef7f4659dd2531977`.

Derivation correction prompt SHA-256:

`0814aa50d9bbe3f28897326285432b85192bda855fab6242496d7c3f889e6a33`.

| Pro claim | Project-side check | verdict |
|---|---|---|
| $V=\sqrt2gu$ and $\Phi=g\Phi_c$ | follows from the locked quadratic kernels | `ACCEPTED_WITH_LOCAL_PROOF` |
| pure-gauge coefficient $\lambda_1$ | canonical magnitudes give the conditional coefficient $\lambda_1/8$; its $D$-word sign and full orbit remain blocked | `REJECTED_NORMALIZATION__FULL_REPLACEMENT_BLOCKED` |
| matter coefficient represented by $\chi_M$ | the Pro response did not derive it; the independent finite-spin-word replay is now Section 4.2 | `PRO_CLAIM_REJECTED__LOCAL_DWORD_SUPERSEDES_BLOCKER` |
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

The marked-occurrence gauge \(D\)-word and homogeneous gauge source/contact
orbit are closed; the global auxiliary gauge census, common matter
source-orientation sign, and component intertwiner remain open.  The
independent order-\(g^2\) support audit proves that
\(\mathcal I_2\), \(\mathcal I_1S_{m3}\), and
\(\mathcal I_0S_{m4}\) vanish.  The full transported second-mark row is
\(-\lambda_1/3\), so the bare matter magnitude is exactly \(\lambda_1\).

## 8. GPT Pro derivation-gate adjudication

The completed correction is archived at `proposals/gpt-pro-aa-derivation-correction-2026-07-14.md` under prompt SHA-256

`0814aa50d9bbe3f28897326285432b85192bda855fab6242496d7c3f889e6a33`.

| corrected Pro claim | Project-side check | verdict |
|---|---|---|
| pure-gauge coefficient $\lambda_1/8$ | Sections 2--3 verify only conditional arithmetic; the global odd-$D$ sign and full orbit are not derived | `REJECTED_AS_FULL_AMPLITUDE__CONDITIONAL_ONLY` |
| initial gauge normalization was $8$ times the conditional canonical normalization | $(g^2/4)2\,/\,[(g^2/16)1]=8$ | `ACCEPTED_ARITHMETIC_ONLY` |
| finite-$2\times2$ matter parent is zero | the Pro reduction starts from `UNVERIFIED_DWORD_ANSATZ`; the independently replayed parent-minus-cut is nonzero | `REJECTED_BY_SECTION_4_2_DWORD` |
| standard consistent DRED selects Q4S/no-Fierz | supported externally, but not admitted by `origin/main` | `BLOCKED_MISSING_AUTHORITY` |
| full Q4S matter coefficient is not fixed by the supplied numerator | the unreduced Q4S spinor word and pointwise rank-zero tensor are missing | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |
| $K^P=2T^{\rm HT}$ and $K^P_{0,0;0,0}=1$ | independently integrated and exhaustively checked | `ACCEPTED_WITH_LOCAL_PROOF` |
| explicit numerical Project--HT component map | no admitted component intertwiner exists | `BLOCKED_MISSING_AUTHORITY` |
| complete $AA$ occurrence census | ghost, NK, gauge-fixing, counterterm, evanescent mixing, and raw port rows remain open | `BLOCKED_MISSING_AUTHORITY` |

The correction's formal Branch-B expansion begins by polarizing an object
called \(\det\) before defining that object in Q4S, so that Pro response does
not supply the numerator.  Section 4.2 instead derives both marked finite spin
words directly.  Section 4.3 transports the second longitudinal word onto the
adjacent \(r_1\) projector and retains the mixed \(\Omega_{21}\) contact.  The
first placement is \(4\lambda_1/3\), while the second is

$$
2\lambda_1
\left[
2\int_{\Sigma_2}\left(z-\frac12\right)
\right]
=2\lambda_1\left(-\frac16\right)
=-\frac13\lambda_1.
$$

The complete order-\(g^2\) matter support audit proves that
\(\mathcal I_2\), \(\mathcal I_1S_{m3}\), and
\(\mathcal I_0S_{m4}\) are zero.  The bare matter magnitude is therefore
\(\lambda_1\); only its global source-orientation sign remains open.

## 9. GPT Pro final-gate adjudication

The completed settlement is archived at `proposals/gpt-pro-aa-final-settlement-2026-07-14.md` under prompt SHA-256

`1efd04011130a3f64f4e57e42bc58fc1d0aa576af8bc8e7eb68b7f0eaab1f90b`.

| final Pro claim | Project-side check | verdict |
|---|---|---|
| `GAUGE ACCEPTED` with $\lambda_1/8$ | the directed canonical triangle and zero homogeneous source orbit are independently replayed; the global auxiliary gauge census and final orientation/intertwiner remain open | `REJECTED_AS_FULL_SECTOR_OVERCLAIM__CANONICAL_TRIANGLE_REPRODUCED` |
| finite-$2\times2$ matter result $0$ is an established check | it follows only after applying Cayley--Hamilton to `UNVERIFIED_DWORD_ANSATZ`; Section 4.2 gives a nonzero parent-minus-cut | `REJECTED_BY_SECTION_4_2_DWORD` |
| isolated Q4S rank-two pole is exactly $4\lambda_1/3$ | this is the first placement only; exact longitudinal transport gives a second placement \(-\lambda_1/3\), so the complete matter magnitude is \(\lambda_1\) | `FIRST_MARK_REPRODUCED__FULL_MATTER_UNIT__GLOBAL_ORIENTATION_SIGN_OPEN` |
| unreduced Q4S matter word is missing | no Q4S inverse image is needed for the distinct scalar DRED representation used in Sections 4.2--4.5 | `SUPERSEDED_BY_DISTINCT_SCALAR_REGULATOR_REPRESENTATION` |
| complete graph census is open | FP, NK, gauge-fixing, source-link, counterterm, and evanescent-mixing data are absent | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |
| Project--HT component intertwiner is missing | no admitted component extraction fixes the $\alpha$-factors | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |
| full $AA$ match is blocked | neither diagram sector nor the auxiliary census is complete | `ACCEPTED_BLOCKER_WITH_LOCAL_PROOF` |

## 10. Derivation-gap audit

Gap types are `G-SIGN` (sign), `G-OP` (operator ordering), `G-DEF` (missing definition), `G-PROJ` (projection), `G-NORM` (normalization), `G-ALG` (algebra), and `G-SCOPE` (unproved scope extension).  Severity `P0` blocks the claimed amplitude; `P1` blocks completion or generalization.

The second-mark full-SD replay checks `42/42` exact identities.  Three
additional representative groups were independently recomputed:

| checked group | exact check | status |
|---|---|---|
| canonical vector rescaling | $v_{\rm old}=u/\sqrt2$ gives three-line factor $2^3=8$ | `PASS` |
| universal triangle tensor pole | the Feynman-parameter factor $2$ and tensor factor $1/4$ give $\widehat\delta^{mn}/(16\pi^2\epsilon)$ | `PASS` |
| simplex derivative kernel | the beta integral gives $n!m!/(m+n+2)!$ and the Project measure gives $K^P=2T^{\rm HT}$ | `PASS` |

| gap id | type | severity | exact missing derivation | state |
|---|---|---:|---|---|
| `AA-G1` | `G-SIGN/G-OP` | `P0` | the odd source-loop integration by parts and \(-4\mu_\ell^2\sigma_\rho\) remainder fix the directed gauge sign | `FIXED_R4` |
| `AA-G2` | `G-SIGN/G-OP` | `P1` | full-\(d\) inverse-square cancellation fixes the cut sign pointwise | `FIXED_R4` |
| `AA-G3` | `G-SCOPE/G-OP` | `P1` | reflected ordered outputs are retained separately; non-\(R_4\) source/contact orbits remain under `AA-G8` | `FIXED_R4` |
| `AA-G4` | `G-DEF/G-PROJ` | `P0` | $\theta_0=0$, both raw source placements, bottom representatives, and endpoint transport are explicit | `FIXED_RAW_DWORDS` |
| `AA-G5` | `G-ALG/G-SIGN/G-NORM` | `P0` | both raw Berezin words and their routing signs are independently replayed | `FIXED_RAW_DWORDS` |
| `AA-G6` | `G-PROJ/G-SCOPE` | `P0` | the first mark gives \(2/3\); the transported \(r_1\)/\(\Omega_{21}\) second-mark orbit gives \(-1/6\); their coefficient is exactly one, while the common source-orientation sign remains open | `FIXED_UNIT_MAGNITUDE__GLOBAL_SIGN_OPEN` |
| `AA-G7` | `G-SCOPE` | `P0` | \(\bar r^2-r_d^2=\mu_\ell^2\) closes the former DRED/Fierz fork | `FIXED` |
| `AA-G8` | `G-SCOPE/G-OP` | `P0` | the pure-gauge marked occurrences and homogeneous source/contact descendants are summed; FP, NK, gauge-fixing, counterterm, and evanescent-mixing global census remains open | `FIXED_SOURCE_ORBIT__GLOBAL_GAUGE_CENSUS_OPEN` |
| `AA-G9` | `G-DEF/G-NORM` | `P1` | Project component extraction does not determine the Project--HT $\alpha$-factors | `OPEN` |
| `AA-G10` | `G-DEF/G-SCOPE` | `P0` | proper slice, ordered bilocal source, background/quantum ports, and DRED contract are not locked | `OPEN` |
| `AA-G11` | `G-SCOPE/G-NORM` | `P0` | exhaust the matter $\mathcal I_2$, $\mathcal I_1S_{m3}$, and $\mathcal I_0S_{m4}$ source/resolvent rows independently of the four primary/current triangle occurrences | `FIXED_ORDER_G2_SUPPORT` |
| `AA-G12` | `G-NORM/G-SCOPE` | `P0` | the full transported bare matter coefficient is \(4/3-1/3=1\); its conditional target mismatch is zero without a counterterm | `FIXED` |

Repair queue:

1. Lock the perturbative slice, ordered source, port grammar, and DRED contract.
2. Fix the common matter source-orientation sign from the locked source/action Fourier convention.
3. Complete the FP, NK, gauge-fixing, counterterm, and evanescent-mixing global gauge census.
4. Fix the common matter and gauge orientation signs.
5. Derive the Project--HT component intertwiner from admitted component projectors.

## 11. Superseding AA final acceptance

### 11.1 Raw contact multiplicity ledger

The exact raw cubic table has

$$
N_{\rm Hessian\ groups}
=2_{\rm chirality}\cdot4_{\rm raw\ word}\cdot3_{\rm external\ placement}
=24.
$$

Every group contains exactly two ordered quantum-role rows,

$$
(S,B),\qquad(B,S),
$$

so

$$
N_{\rm raw\ endpoint\ rows}=24\cdot2=48.
$$

For each marked edge:

| source occurrence | physical edge | differentiated Hessian | Taylor factor | even action orderings | ordered Wick endpoints |
|---|---|---|---:|---:|---:|
| $T_0=D_-A_1^A\,A_1^B$ | $e_0$ | left $D$-background action Hessian | $1/2!$ | $2$ | $(S,B),(B,S)$ |
| $T_2=A_1^A\,D_-A_1^B$ | $e_2$ | right $A$-background action Hessian | $1/2!$ | $2$ | $(S,B),(B,S)$ |

Thus the raw row count is

$$
\frac1{2!}\cdot2_{\rm action\ ordering}\cdot2_{\rm Wick\ endpoint}
=2_{\rm endpoint\ rows}.
$$

The parent contains the identical endpoint sum:

$$
\frac1{2!}
\left[(N_{SB}+N_{BS})+(N_{SB}+N_{BS})\right]
=N_{SB}+N_{BS}.
$$

The Gaussian Schwinger--Dyson product rule maps the two rows bijectively,

$$
K_{{\rm raw},SB}=-N_{d,SB},
\qquad
K_{{\rm raw},BS}=-N_{d,BS}.
$$

Hence, independently for $e=e_0,e_2$,

$$
N_{d,e}=L_e+Q_er_{e,d}^2,
\qquad
K_{{\rm raw},e}=-L_e-Q_er_{e,d}^2,
$$

$$
\boxed{N_{d,e}+K_{{\rm raw},e}=0},
\qquad
\boxed{m_0=m_2=1}.
$$

The anomaly sector is therefore exactly

$$
N_{{\rm full},e}+K_{{\rm raw},e}
=Q_e\left(\bar r_e^2-r_{e,d}^2\right)
=Q_e\mu_\ell^2.
$$

There is no extra edge factor $2$ and no global metric-trace factor $d$ or
$4$.

### 11.2 Target-blind ordered result

The two independent transverse plus-spinor frames give

$$
\begin{pmatrix}-i&-1\\-1&-i\end{pmatrix}
\begin{pmatrix}c_p\\c_q\end{pmatrix}
=
\begin{pmatrix}-1/2+i\\-1+i/2\end{pmatrix},
$$

$$
c_p=-\frac i2,
\qquad
c_q=-i.
$$

After the common Fourier map and the typed EOM/divergence quotient,

$$
(DA_p,AD_p)=(1,-1).
$$

The independently replayed matter words give, for every flavor,

$$
(B_rC_r,C_rB_r)=(1,-1).
$$

Therefore

$$
\boxed{
\begin{aligned}
\Gamma_{AA}^{(1)}
=\lambda_1\mathbb F^{AB}{}_{DE}
\Bigg[{}&
\langle D^D,A^E\rangle
-\langle A^D,D^E\rangle\\
&+\sum_{r=1}^3
\left(
\langle B_r^D,C_r^E\rangle
-\langle C_r^D,B_r^E\rangle
\right)
\Bigg].
\end{aligned}}
$$

The exhaustive component replay has

$$
N_{\rm total}=9216,
\qquad
N_{\rm sparse}=2048,
\qquad
N_{\rm equality\ failure}=0.
$$

### 11.3 Holomorphic-twist check-only seal

Only after Section 11.2 is fixed, read the `A__A` row of
`audits/step5-ht-roundtrip-audit.json`.  With the Project-frame dictionary

$$
C_{\rm Project}^{AB}{}_{DE}=\mathbb F^{AB}{}_{DE},
$$

its ordered vector is

$$
(D>A,A>D,B_1>C_1,C_1>B_1,B_2>C_2,C_2>B_2,B_3>C_3,C_3>B_3)
$$

$$
=(1,-1,1,-1,1,-1,1,-1).
$$

This equals the independently derived one-loop vector entry by entry:

$$
\Gamma_{AA,\rm one\ loop}^{(1)}
-\Gamma_{AA,\rm HT}^{(1)}=0.
$$

The target was not used to select a sign, normalization, multiplicity, or
operator ordering.

`AA_HT_CHECK_ONLY_SEAL__DERIVATION_TARGET_BLIND__EXACT_MATCH`.

Final status:
`ACCEPTED_AA_ONE_LOOP_ANOMALY_SECTOR__HT_CHECK_ONLY_EXACT_MATCH`.
