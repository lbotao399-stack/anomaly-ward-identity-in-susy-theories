# Step 6. Covariant completion theorem: Phase-0 chain-map gate

Status: `BLOCKED_PHASE0_CHAIN_MAP_ACTION_NOT_LOCKED__COVARIANT_COMPLETION_NOT_PROVED`

Authority base: `origin/main@06601a0ed4e6060e2d872980509e1b949e61506c`.
Owner work order: `tasks/instructions/2026-07-16-covariant-completion-proof.md`.
The source memo is `NON_AUTHORITY_PROPOSAL`; its predicted box coefficients, HT target,
and literature coefficients do not enter this audit.

## Final Result List

记

- $d:=\boldsymbol\nabla_-$：tree differential；
- $\Delta$：settled 81-row one-loop letter-pair map；
- $A,B,D,E,F,G,H$：adjoint color indices；
- $r,s,t\in\{1,2,3\}$：$SU(3)$ flavor indices；
- $P_{\dot a}$：settled output 中的 covariant dotted derivative；
- $\mathfrak R_{ij}$：Phase-0 chain-map residual。

The required identity is

$$
\boxed{
\mathfrak R_{ij}
:=d\Delta(L_i,L_j)
-\Delta\!\left(d(L_iL_j)\right)_{\rm Koszul}=0.}
\tag{6.1}
$$

The 25 ordered pairs in
$\{C_1,C_2,C_3,D_{\dot1},D_{\dot2}\}^2$ are defined: both descendants and every settled
output vanish.  Every row containing $A$ or $B_r$ requires missing action data.  Hence

$$
N_{\rm ledger}=81,
\qquad
N_{\rm PASS}=25,
\qquad
N_{\rm BLOCKED}=56.
$$

Missing inputs are the Euler-descendant action of $\Delta$, the commutator
$[d,P_{\dot a}]$, a nonlinear-word extension of the bilinear map, and a declared
$Q_1$-stable BRST/EOM quotient.  Therefore Phase 0 is
`BLOCKED_PHASE0_CHAIN_MAP_ACTION_NOT_LOCKED`, not a settled-ledger P0.  Phases 1--5 were
not run; no $(t_1,t_2,t_W)$ vector was computed and no regression target entered or was
compared with the calculation.

## 1. Locked input and the undefined terms

The color product is a single ordered monomial,

$$
(X\times Y)^A:=c_{FG}{}^A X^F Y^G,
\qquad
c_{AFG}=c_{[AFG]}.
$$

It is not the graded commutator $XY-(-1)^{|X||Y|}YX$.

The full locked descendants are

$$
\boxed{
\begin{aligned}
dA^A
&=-(\boldsymbol\nabla_+\mathscr E_V)^A
-2i\sum_{s,F,G}c_{FG}{}^A B_s^F C_s^G,\\
dB_r^A
&=-2\mathscr E_{\widetilde r}^{A}
-\sqrt2\sum_{s,t,F,G}\varepsilon_{rst}c_{FG}{}^A C_s^F C_t^G,\\
dC_r^A&=0,\\
dD_{\dot a}^A&=0.
\end{aligned}}
\tag{6.2}
$$

For $X,Y\in\{C_1,C_2,C_3,D_{\dot1},D_{\dot2}\}$, the settled ledger gives
$\Delta(X,Y)=0$ and (6.2) gives $dX=dY=0$.  Therefore

$$
\mathfrak R_{X,Y}=d(0)-\Delta(0)=0,
\qquad
5\times5=25\ \mathrm{PASS}.
$$

Hence the right side of (6.1) requires

$$
\boxed{
\begin{gathered}
\Delta(\boldsymbol\nabla_+\mathscr E_V,L),
\qquad
\Delta(L,\boldsymbol\nabla_+\mathscr E_V),\\
\Delta(\mathscr E_{\widetilde r},L),
\qquad
\Delta(L,\mathscr E_{\widetilde r}),\\
\Delta(X_1\cdots X_m,Y_1\cdots Y_n).
\end{gathered}}
\tag{6.3}
$$

The 81-row ledger defines none of the first four maps.  Equations (5A.61)--(5A.62)
define ordered left functional differentiation and labeled-leg permutation; they do not
define the last bilinear extension in (6.3).

The left side is also undefined on translated outputs such as
$D_{\dot a}(P^{\dot a}C_r)$ until $[d,P_{\dot a}]$ is fixed.  The locked covariance audit
treats even $[q_r,P]=0$ as a conditional assumption and explicitly leaves the BRST/EOM
quotient unspecified.  Setting $\mathscr E_V=\mathscr E_{\widetilde r}=0$ would therefore
add a new quotient rule; it is not licensed by the work order.

For residual-$q_r$ checks, every row containing $D_{\dot a}$ additionally requires
$\Delta(P_{\dot a}C_r,L)$ or $\Delta(L,P_{\dot a}C_r)$.  These maps are also absent.

## 2. Conditional diagnostic: $A>C_1$

This section is `CONDITIONAL_NONZERO_NOT_A_P0`.  It uses the additional rules

$$
\boxed{
\mathscr E_V=\mathscr E_{\widetilde r}=0,
\qquad
[d,P_{\dot a}]=0,
\qquad
\Delta_{\rm word}=\text{literal occurrence replacement using (5A.61)}.}
\tag{6.4}
$$

The settled rows needed for the diagnostic are

$$
\begin{aligned}
\Delta(A^A,C_1^B)
={}&\lambda_1\mathbb F^{AB}{}_{DE}
\left[
D_{\dot a}^{D}(P^{\dot a}C_1)^{E}
-(P_{\dot a}C_1)^{D}D^{E\dot a}
\right],\\
\Delta(B_s^F,C_1^B)
={}&\delta_{s1}\lambda_1\mathbb F^{FB}{}_{DE}
D_{\dot a}^{D}D^{E\dot a},\\
\Delta(C_s^G,C_1^B)={}&0.
\end{aligned}
$$

Under (6.4), $dD=dC_1=0$ gives

$$
d\Delta(A^A,C_1^B)=0.
$$

For the ordered word $B_s^F C_s^G$, the $B_s$ occurrence has sign
$(-1)^{|B_s|\cdot0}=+1$.  The $C_s$ occurrence has sign
$(-1)^{|C_s||B_s|}=+1$ but its pair map is zero.  Thus

$$
\begin{aligned}
\Delta(dA^A,C_1^B)
={}&-2i\sum_{s,F,G}c_{FG}{}^A
\Delta(B_s^FC_s^G,C_1^B)\\
={}&-2i\lambda_1c_{FG}{}^A\mathbb F^{FB}{}_{DE}
(D_{\dot a}^{D}C_1^G)D^{E\dot a}.
\end{aligned}
\tag{6.5}
$$

No term $(C_1^GD^D)D^E$ is generated.  Therefore the conditional residual is

$$
\boxed{
\mathfrak R_{A,C_1}^{AB}\Big|_{(6.4)}
=2i\lambda_1T^{AB}{}_{GDE}
(D_{\dot a}^{D}C_1^G)D^{E\dot a},
\qquad
T^{AB}{}_{GDE}:=\sum_Fc_{FG}{}^A\mathbb F^{FB}{}_{DE}.}
\tag{6.6}
$$

The symbolic color tensor is not an identity zero.  Define the exact model

$$
\kappa_{ab}=\delta_{ab},
\qquad
c_{abc}=\varepsilon_{abc},
\qquad
a,b,c\in\{1,2,3\}.
$$

Its Jacobi identity follows termwise from

$$
\sum_h\varepsilon_{abh}\varepsilon_{hcd}
=\delta_{ac}\delta_{bd}-\delta_{ad}\delta_{bc},
$$

because the cyclic sum is

$$
\begin{aligned}
&\delta_{ac}\delta_{bd}-\delta_{ad}\delta_{bc}
+\delta_{ba}\delta_{cd}-\delta_{bd}\delta_{ca}
+\delta_{cb}\delta_{ad}-\delta_{cd}\delta_{ab}=0.
\end{aligned}
$$

For $(A,B,G,D,E)=(1,2,3,1,1)$,

$$
\begin{aligned}
T^{12}{}_{3,11}
&=\sum_{F=1}^{3}\varepsilon_{F31}
\sum_{H=1}^{3}\varepsilon_{FH1}\varepsilon_{2H1}\\
&=\varepsilon_{231}
\left(\varepsilon_{231}\varepsilon_{231}\right)\\
&=1.
\end{aligned}
$$

This proves only that the residual in (6.6) is nonzero under the three extra rules (6.4).
An admissible missing map in (6.3), a nonzero $[d,P_{\dot a}]$, or a different locked
$Q_1$ extension can change or cancel it.  It is therefore not evidence against the
settled 81-row ledger.

## 3. Phase gate

Phase 0 has 25 contract-grade zero rows and 56 undefined rows.  The immediate-P0 clause
applies only after a defined row fails; it is not triggered by the conditional diagnostic.

Consequently the following are not derived:

$$
(t_1,t_2,t_W),
\qquad
H(Q_0)_{\rm invisible},
\qquad
[\operatorname{Loc}_{\mu^2},\delta_\omega],
\qquad
n\ge5\ \text{induction},
\qquad
\text{ghost/NK typed-absence rows}.
$$

## 4. Exact evidence

One checker is used:

- `scripts/verify_step6_q0_q1_consistency.py` validates the canonical 81-row ledger,
  seals the locked-input blocker, and evaluates (6.5)--(6.6) only as a conditional
  diagnostic.
- `audits/step6-q0-q1-consistency.json` is the review-sized blocker summary.
- `generated/step6/q0-q1-consistency.json` is the regenerable detailed trace.

No prediction from the source memo, holomorphic twist, or literature enters the result.
