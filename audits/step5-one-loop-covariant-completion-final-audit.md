# Step 5A one-loop covariant-completion final audit

Status:
ROOTED_WARD_PROVED__PHYSICAL4D_COMPLETION_FAIL_CLOSED__FULL_DRED_RAW_INJECTIVITY_FALSE__CONTACT_OPEN

## 0. Scope and notation

Audited inputs:

- audits/step5-one-loop-covariant-completion-theorem.md;
- audits/step5-one-loop-all-order-rooted-ward.md;
- audits/step5-one-loop-background-hessian-ward.md;
- audits/step5-one-loop-filtered-covariant-quotient.md;
- audits/step5-one-loop-dred-evanescent-jets.md;
- audits/step5-one-loop-tau-cubic-projection.md;
- audits/step5-ww-contact-replay.md;
- audits/step5-one-loop-source-color-closure.md;
- audits/step5-frame-bridge-intertwiner.md.

Checked equation groups: \(13\).

$$
H_{\mathcal B}:=\text{fixed-vector quadratic Hessian},\qquad
G_{\mathcal B}:=H_{\mathcal B}^{-1},\qquad
I_{\mathcal B}:=\text{source-linear insertion Hessian}.
$$

$$
\Gamma_{\mathscr I,{\rm ren,DRED}}^{(1),{\rm reg}}
:=\Gamma_{\mathscr I,{\rm root,DRED}}^{(1),{\rm reg}}+\mathrm{CT}^{\rm reg},
\qquad
\mathscr A_{{\rm loc,DRED}}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{\rm DRED}
\Gamma_{\mathscr I,{\rm ren,DRED}}^{(1),{\rm reg}},
$$

$$
\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\Gamma_{\mathscr I,{\rm ren,DRED}}^{(1),{\rm reg}},
\qquad
q_{4d}\operatorname{Loc}_{\rm UV}^{\rm DRED}
=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\quad\texttt{NOT\_PROVED},
$$

$$
\ell_2[\mathscr O]
:=\left.\frac12\frac{d^2}{dt^2}\right|_{t=0}\mathscr O(t\mathcal B).
$$

$$
q_{4d}(\tau)=0,\qquad
\widetilde\delta^{mn}
=\frac{\epsilon}{2}\delta_{(4)}^{mn}+\tau^{mn},\qquad
\delta_{(4)mn}\tau^{mn}=0.
$$

$$
\begin{array}{c|c}
\text{statement}&\text{audit status}\\ \hline
\text{registered fixed-vector rooted one-loop functional}&\texttt{PROVED}\\
\text{registered fixed-vector rooted Ward covariance}&\texttt{PROVED}\\
\text{full }\mathcal N=4\text{ fluctuating-sector trace}&\texttt{OPEN}\\
\text{full-DRED raw/background-CE }\ker\ell_2=0&\texttt{FALSE}\\
\text{full-DRED EOM/IBP/BV quotient injectivity}&\texttt{OPEN}\\
\text{physical-4d total filtered }\ker\bar\ell_2=0&\texttt{FAIL\_CLOSED}\\
\text{physical-4d }N=2\text{ candidate subblock}&\texttt{PROVED\_ONLY\_ON\_SUBBLOCK}\\
\text{complete quadratic contact pole}&\texttt{OPEN}\\
\text{local covariant-completion theorem}&\texttt{NOT\_ACCEPTED}\\
\text{full nonlocal 1PI completion}&\texttt{NOT\_CLAIMED}\\
\text{vanishing of all loop orders }\ell\ge2&\texttt{NOT\_PROVED}
\end{array}
$$

## 1. Proved fixed-vector rooted statement

In the Step-5A reference-flat fixed-vector Gaussian,

$$
\begin{aligned}
\Gamma_{\mathscr I,\rm root}^{(1)}[\mathcal B]
&=
\left.
\frac{\vec\delta}{\delta J}
\frac12\operatorname{STr}_{\rm DRED}
\log\!\left(H_{\mathcal B}+JI_{\mathcal B}\right)
\right|_{J=0}\\
&=\frac12\operatorname{STr}_{\rm DRED}
\left(G_{\mathcal B}I_{\mathcal B}\right).
\end{aligned}
$$

For

$$
H_{\mathcal B}=H_0+\sum_{r\ge1}H_r,\qquad
I_{\mathcal B}=\sum_{s\ge0}I_s,\qquad
G_0=H_0^{-1},
$$

$$
G_{\mathcal B}
=G_0\sum_{k\ge0}
\left(-\sum_{r\ge1}H_rG_0\right)^k,
$$

and therefore

$$
\boxed{
\Gamma_{\mathscr I,\rm root,n}^{(1)}
=\frac12
\sum_{\substack{k,s,r_j\\s+\sum_jr_j=n}}
(-1)^k\operatorname{STr}_{\rm DRED}
\left[I_sG_0H_{r_1}G_0\cdots H_{r_k}G_0\right].}
$$

The renormalized coefficient is

$$
\Gamma_{\mathscr I,\rm ren,n}^{(1)}
=\Gamma_{\mathscr I,\rm root,n}^{(1)}+\mathrm{CT}_n.
$$

The rooted Taylor coefficient contains polygons and every Hessian/contact
member with the same total background degree.  It does not identify an
individual polygon with a covariant observable.

Under a finite background transformation,

$$
H'=RHR^{-1},\qquad
G'=RGR^{-1},\qquad
I'=RIR^{-1}.
$$

Since \(R\) is even,

$$
\begin{aligned}
\delta_R(GI)
&=[R,G]I+G[R,I]\\
&=RGI-GRI+GRI-GIR\\
&=[R,GI],
\end{aligned}
$$

$$
\boxed{
\delta_R\Gamma_{\mathscr I,\rm root}^{(1)}
=\frac12\operatorname{STr}_{\rm DRED}[R,GI]=0.}
$$

This proves background covariance of the graph-complete rooted sum at every
background order \(n\).  Covariance of the renormalized sum additionally
requires a background-covariant \(\mathrm{CT}_n\).  It proves neither
quadratic-jet injectivity nor a triangle-only coefficient.

## 2. Exact conditional completion theorem

Let \(\mathfrak H_{\rm reg}^{4d}\) be a specified registered-sector,
source-completed physical-\(4d\) local quotient and

$$
\bar\ell_2^{4d}:\mathfrak H_{\rm reg}^{4d}
\longrightarrow\overline T_{2,{\rm reg}}^{4d,\epsilon}
$$

its induced quadratic-jet map.  The raw-to-quotient map is

$$
\rho_2^\epsilon:T_{2,{\rm reg}}^{4d,\epsilon}
\longrightarrow\overline T_{2,{\rm reg}}^{4d,\epsilon},
\qquad
\overline T_{2,{\rm reg}}^{4d,\epsilon}
=T_{2,{\rm reg}}^{4d,\epsilon}/B_2^\epsilon.
$$

If

$$
\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}\in\mathfrak H_{\rm reg}^{4d},
\qquad
0\ne[\mathscr O_\star]\in\mathfrak H_{\rm reg}^{4d},\qquad
\ker\bar\ell_2^{4d}=0,
$$

then

$$
\bar t_\star:=\bar\ell_2^{4d}[\mathscr O_\star]\ne0,
\qquad
\overline T_{2,{\rm reg}}^{4d,\epsilon}
=\mathbb Q(\epsilon)\bar t_\star
\oplus\overline T_{2,\perp}^{4d,\epsilon},
$$

$$
\bar\pi_\star^{4d}:
\overline T_{2,{\rm reg}}^{4d,\epsilon}\longrightarrow\mathbb Q(\epsilon),
\qquad
\bar\pi_\star^{4d}(\alpha\bar t_\star+\bar t_\perp)=\alpha.
$$

If in addition the complete quadratic family obeys

$$
\bar\ell_2^{4d}[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}]
=C_{2,{\rm reg}}\bar\ell_2^{4d}[\mathscr O_\star],
$$

then

$$
\bar\ell_2^{4d}
\left[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}
-C_{2,{\rm reg}}\mathscr O_\star\right]=0,
$$

$$
\boxed{
[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}]
=C_{2,{\rm reg}}[\mathscr O_\star]
\quad\text{in }\mathfrak H_{\rm reg}^{4d}.}
$$

The implication is proved.  Its Step-5 premises are not proved.

The complete quadratic family is

$$
\begin{aligned}
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
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

$$
Q_{\triangle}^{\rm bare}
:=\frac12\operatorname{STr}_{\rm DRED}\!\left[
I_0G_0H_1[1]G_0H_1[2]G_0
+I_0G_0H_1[2]G_0H_1[1]G_0
\right].
$$

Define

$$
\begin{aligned}
Q_{\rm Hess}^{(2)}
:={}&\frac12\operatorname{STr}_{\rm DRED}\Big[
-I_0G_0H_2[1,2]G_0
-I_1[1]G_0H_1[2]G_0\\
&\hspace{36mm}
-I_1[2]G_0H_1[1]G_0
+I_2[1,2]G_0
\Big].
\end{aligned}
$$

$$
\boxed{
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm bare}
+\underbrace{\left(Q_{\rm Hess}^{(2)}+\mathrm{CT}_2\right)}_{
Q_{\rm contact,Hess}^{(2)}}.}
$$

The 48 collapse bindings require a constructed coefficient map

$$
Q_{\triangle}^{\rm cut}
:=\mathcal R_{\rm cut}Q_{\triangle}^{\rm bare},
\qquad
Q_{\triangle}^{\rm irr}
:=(1-\mathcal R_{\rm cut})Q_{\triangle}^{\rm bare},
\qquad
\mathcal R_{\rm cut}=\texttt{NOT\_CONSTRUCTED}.
$$

Only after that construction may the same functional be reorganized as

$$
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm irr}
+\underbrace{
\left(Q_{\triangle}^{\rm cut}+Q_{\rm contact,Hess}^{(2)}\right)
}_{Q_{\rm contact,eff}^{(2)}}.
$$

On one fixed registered target line,

$$
C_{2,{\rm reg}}
:=\bar\pi_\star^{4d}\!\left(
\bar\ell_2^{4d}[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}]\right),
\qquad
C_{\triangle,{\rm bare,reg}}
:=\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}Q_{\triangle}^{\rm bare}\right),
$$

$$
C_{{\rm contact,Hess},{\rm reg}}
:=\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}Q_{\rm contact,Hess}^{(2)}\right),
\qquad
\operatorname{status}\!\left(
C_{{\rm contact,Hess},{\rm reg}}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED}.
$$

$$
C_{2,{\rm reg}}
=C_{\triangle,{\rm bare,reg}}+C_{{\rm contact,Hess},{\rm reg}},
$$

$$
\boxed{
C_{2,{\rm reg}}=C_{\triangle,{\rm bare,reg}}
\quad\Longleftrightarrow\quad
\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
Q_{\rm contact,Hess}^{(2)}\right)=0.}
$$

The \(H_2\) projector \(D\)-algebra, the complete \(I_1H_1\) pole, the
coefficient transport of the \(48\) collapsed bindings, the \(I_2\)
normalization, and \(\mathrm{CT}_2\) are unresolved.  Hence neither
\(\bar\pi_\star^{4d}\rho_2^\epsilon(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
Q_{\rm contact,Hess}^{(2)})=0\) nor
\(C_{2,{\rm reg}}=C_{\triangle,{\rm bare,reg}}\) is established.  This does
not require the entire \(T_2\)-vector to vanish.  The separate cut-map gap
blocks the irreducible-triangle/effective-contact reorganization.

$$
C_2^{\mathcal N=4}
:=\sum_{\alpha\in\{V,\Phi_r,\widetilde\Phi_r,{\rm FP},{\rm NK}\}}
C_{2,\alpha},
\qquad
\operatorname{status}\!\left(C_2^{\mathcal N=4}\text{ evaluated}\right)
=\texttt{NOT\_ESTABLISHED}.
$$

## 3. Full-DRED branch

The exact projector split gives

$$
\tau_{mn}\tau^{mn}
=2\epsilon-\epsilon^2
\notin(\epsilon^2)\mathbb Q[\epsilon].
$$

Thus \(\tau\) is an independent evanescent tensor, not an
\(\epsilon\delta_{(4)}\) coefficient.  Define

$$
\mathscr E_{abc}^{AB}
=K^{AB}{}_{C[DE]}
\tau_{(ab|\dot c\dot d|}
W_{c)}^C\widetilde W^{D\dot c}\widetilde W^{E\dot d},
$$

$$
K^{AB}{}_{C[DE]}
=\delta^A{}_Cc_{DE}{}^B+\delta^B{}_Cc_{DE}{}^A.
$$

For the exact \(SU(2)\) witness,

$$
K^{00}{}_{0[12]}=2,\qquad
K^{00}{}_{0[DE]}B^{DE}=4B^{12}\ne0.
$$

Moreover,

$$
\mathscr E(t\mathcal B)
=t^3\mathscr E_{(3)}(\mathcal B)
+\sum_{n\ge4}t^n\mathscr E_{(n)}(\mathcal B),
$$

$$
\ell_2(\mathscr E)
=\left.\frac12\frac{d^2}{dt^2}\right|_{t=0}
\mathscr E(t\mathcal B)=0,
$$

$$
\left.\frac{d^3}{dt^3}\right|_{t=0}
\mathscr E(t\mathcal B)=6\mathscr E_{(3)}\ne0.
$$

Its color tensor is background-equivariant.  Therefore

$$
\boxed{
0\ne\mathscr E\in
\ker\!\left(\ell_2\big|_{\mathcal V_{\rm DRED,raw}^{J^1}}\right)
\cap\mathcal V_{\rm DRED}^{\rm CE}.}
$$

Consequently,

$$
\boxed{
\ker\!\left(\ell_2\big|_{\rm full\ DRED,raw}\right)\ne0,}
$$

and the quadratic seed cannot uniquely determine the full-DRED raw or
background-CE covariant completion.

The stronger quotient statement is not available:

$$
[\mathscr E]_{\rm EOM/IBP/BV}
=\texttt{UNDETERMINED}.
$$

Hence the explicit witness disproves raw/background-CE injectivity; it does
not prove a nonzero class in the missing EOM/IBP/BV quotient.

The actual cubic coefficient is also uncomputed:

$$
C_{\mathscr E,{\rm reg}}
:=\operatorname{Coeff}_{\mathscr E}
\mathscr A_{{\rm loc,DRED},3}^{(1),{\rm reg}},
\qquad
\operatorname{status}\!\left(C_{\mathscr E,{\rm reg}}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},
$$

because

$$
H_3=\texttt{MISSING},\qquad
I_3=\texttt{MISSING},\qquad
P_\tau=\texttt{MISSING}.
$$

Therefore the present calculation proves neither the presence nor the
cancellation of the \(\mathscr E\) dressing in the one-loop amplitude.

## 4. Physical-four-dimensional branch

The explicit DRED witness vanishes under the operator projection:

$$
q_{4d}(\tau)=0,\qquad
q_{4d}(\mathscr E)=0.
$$

This removes that witness only.  It does not prove total physical-\(4d\)
injectivity.

The indexed event map has type

$$
M_{1\to2}:\mathbb Q^{4866}\longrightarrow\mathbb Q^{126}.
$$

Its \(4866\) inputs are event carriers, not independent \(N=1\) parents.
The old relation block had the form

$$
R_{1,\rm old}
=\begin{pmatrix}\mathbf1_{4866}&-M_{1\to2}^{T}\end{pmatrix}.
$$

For every matrix \(A\in\operatorname{Mat}_{m\times n}(\mathbb Q)\),

$$
\begin{pmatrix}\mathbf1_m&-A\end{pmatrix}
\binom{z}{0}=z
\qquad
\forall z\in\mathbb Q^m,
$$

$$
\boxed{
\operatorname{rank}
\begin{pmatrix}\mathbf1_m&-A\end{pmatrix}=m}
$$

independently of \(A\).  The identity pivot therefore cannot certify a
physical parent quotient.

The missing map is

$$
C_1:\mathbb Q^{20}_{\rm parent}
\longrightarrow\mathbb Q^{4866}_{\rm event}.
$$

The actual curvature-child boundary is generated by

$$
\operatorname{im}(M_{1\to2}C_1)
\subseteq\mathbb Q^{126},
$$

not by treating all \(4866\) event columns as independent parents.  Word
order, Koszul, terminal-PBW, EOM, and source-jet incidences of \(C_1\) are
absent.  Therefore

$$
\boxed{
\operatorname{status}\!\left(\ker\bar\ell_2^{\,4d}=0\right)
=\texttt{NOT\_ESTABLISHED}.}
$$

The certified \(N=2\) candidate subblock is narrower:

$$
R_2^{\rm cand}\in\operatorname{Mat}_{126\times127}(\mathbb Q),\qquad
\operatorname{rank}R_2^{\rm cand}=126,
$$

$$
\dim\!\left(\mathbb Q^{127}/\operatorname{row}R_2^{\rm cand}\right)=1,
$$

$$
\bar\ell_2^{(N=2)}[C]
=\binom{1}{-1},\qquad
\begin{pmatrix}1&0\end{pmatrix}
\bar\ell_2^{(N=2)}=1.
$$

Thus

$$
\boxed{
\ker\bar\ell_2^{(N=2)}=0}
$$

on this one candidate subblock only.  The missing \(C_1\) prevents promotion
to the total filtered quotient.

Finally,

$$
\frac1\epsilon(2\epsilon P)=2P
$$

shows that scalar evanescent traces can feed a physical finite term.  Hence
\(q_{4d}(\mathscr E)=0\) does not by itself establish commutation of the
physical projection with DRED pole extraction and operator mixing.

## 5. Representation and cohomological scope

The proved Ward statement is fixed-vector-frame.  The operator bridge

$$
\mathcal O_C=\mathcal B^{-1}\mathcal O_V\mathcal B
$$

does not equal the nonlinear quantum-coordinate Hessian identity

$$
K_C
=J_q^{\rm st}K_VJ_q
+E_{V,\alpha}C^\alpha{}_{ij}.
$$

The full chiral/vector Jacobian, density, and EOM-contact comparison remain
open.  They do not obstruct the fixed-vector Ward theorem; they do obstruct
exporting it as a cross-frame equality.

The background source complex obeys

$$
s_B^2\mathscr I=s_B^2J=s_B(J\mathscr I)=0.
$$

The composite-source antifields and full linearized BV--Slavnov mixing matrix
are not defined.  Therefore background-CE covariance does not prove a full
BV-cohomological completion theorem.

## 6. Two meanings of one-loop exactness

All background valences of the regularized rooted functional at fixed loop
order are contained in

$$
\Gamma_{\mathscr I,\rm root}^{(1)}
=\frac12\operatorname{STr}_{\rm DRED}(G_{\mathcal B}I_{\mathcal B}).
$$

This is an all-background-order identity inside the coefficient of
\(\hbar^1\).  For

$$
\Gamma_{\mathscr I}
=\sum_{\ell\ge0}\hbar^\ell\Gamma_{\mathscr I}^{(\ell)},
$$

nothing above proves

$$
\Gamma_{\mathscr I}^{(\ell)}=0,\qquad \ell\ge2.
$$

Thus loop-order one-loop exactness is not established.  The weaker statement
that every one-loop box, pentagon, and contact term is the covariant dressing
of the complete quadratic seed is also not established because

$$
\ker\bar\ell_2^{\,4d}=0
$$

is open and full-DRED raw injectivity is false.

## 7. Gap table

| ID/type | Location and claim | Missing exact object | Severity |
|---|---|---|---|
| G1[G-THM] | physical-\(4d\) completion | \(C_1:\mathbb Q^{20}\to\mathbb Q^{4866}\) and the total relation matrix | P0 |
| G2[G-THM] | full-DRED injectivity | false on raw/background-CE modules by \(\mathscr E\) | P0 |
| G3[G-NORM] | \(C_{2,{\rm reg}}=C_{\triangle,{\rm bare,reg}}\) | \(H_2\) projector \(D\)-algebra, complete \(I_1H_1\) pole, coefficient transport for \(48\) collapsed bindings, \(I_2\) normalization, \(\mathrm{CT}_2\) | P0 |
| G4[G-PROJ] | \(\operatorname{Coeff}_{\mathscr E}\mathscr A_{{\rm loc,DRED},3}^{(1),{\rm reg}}=0\) | \(H_3,I_3,P_\tau\) and the cubic contact orbit | P0 |
| G5[G-THM] | \([\mathscr E]_{\rm EOM/IBP/BV}=0\) | full evanescent relation matrix | P1 |
| G6[G-SCOPE] | local completion equals full 1PI | nonlocal homogeneous Ward solutions lie outside \(\operatorname{Loc}_{\rm UV}\) | P0 |
| G7[G-SCOPE] | all-valence one-loop identity implies loop exactness | \(\Gamma_{\mathscr I}^{(\ell)}=0\) for every \(\ell\ge2\) | P0 |
| G8[G-SCOPE] | fixed-vector result equals chiral-frame result | nonlinear Jacobian, density, and EOM-contact bridge | P1 |
| G9[G-THM] | background CE equals BV cohomology | composite-source antifields and linearized BV--ST matrix | P1 |
| G10[G-REG] | physical projection commutes with renormalization | stability of the evanescent ideal and \(q_{4d}\operatorname{Loc}_{\rm UV}^{\rm DRED}=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}\) | P0 |
| G11[G-SCOPE] | pure-gauge rooted trace is the full \(\mathcal N=4\) trace | source-coupled chiral-matter, FP, and NK Hessian/insertion sectors | P0 |
| G12[G-REG] | local pole is separated from IR | nonexceptional external momenta, an independent IR regulator, or an exact (R^*) subtraction | P0 |

Highest-risk gaps:

$$
G1\longrightarrow
\ker\bar\ell_2^{\,4d}\text{ is unknown},
$$

$$
G2\longrightarrow
\ker\ell_2^{\rm DRED,raw}\ne0,
$$

$$
G3\longrightarrow
C_{2,{\rm reg}}=C_{\triangle,{\rm bare,reg}}\text{ is unknown}.
$$

Required dependency order:

$$
C_1
\longrightarrow
\ker\bar\ell_2^{\,4d},
$$

$$
(H_2,I_1H_1,\mathrm{CT}_2)
\longrightarrow
\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}Q_{\rm contact,Hess}^{(2)}\right),
$$

$$
(H_3,I_3,P_\tau)
\longrightarrow
\operatorname{Coeff}_{\mathscr E}
\mathscr A_{{\rm loc,DRED},3}^{(1),{\rm reg}}.
$$

## 8. Verification spot checks

### Check 1: Ward telescoping

$$
[R,G]I+G[R,I]
=RGI-GRI+GRI-GIR
=[R,GI].
$$

### Check 2: identity-pivot failure

$$
\begin{pmatrix}\mathbf1_m&-A\end{pmatrix}
\binom z0=z
\quad\Longrightarrow\quad
\operatorname{rank}
\begin{pmatrix}\mathbf1_m&-A\end{pmatrix}=m
$$

for every \(A\); the rank contains no information about \(C_1\).

### Check 3: cubic kernel

$$
\left.\frac12\frac{d^2}{dt^2}\right|_{t=0}t^3
=\left.3t\right|_{t=0}=0,
$$

$$
\left.\frac{d^3}{dt^3}\right|_{t=0}t^3=6.
$$

### Check 4: conditional theorem

$$
\bar\ell_2^{4d}[A_{4d}^{\rm reg}]
=C_{2,{\rm reg}}\bar\ell_2^{4d}[O],\qquad
\ker\bar\ell_2^{4d}=0,
$$

$$
\bar\ell_2^{4d}[A_{4d}^{\rm reg}-C_{2,{\rm reg}}O]=0
\quad\Longrightarrow\quad
[A_{4d}^{\rm reg}-C_{2,{\rm reg}}O]=0.
$$

## 9. Final verdict

$$
\boxed{
\delta_R\Gamma_{\mathscr I,\rm root}^{(1)}=0
\quad\text{for the registered fixed-vector rooted one-loop carrier}.}
$$

$$
\boxed{
\text{triangle-only covariant completion}
=\texttt{NOT\_PROVED}.}
$$

$$
\boxed{
\text{accepted anomaly coefficient}
=\texttt{NONE}.}
$$
