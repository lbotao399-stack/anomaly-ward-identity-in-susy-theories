# Step 5A physical-4d filtered covariant quotient

Status: `FAIL_CLOSED_MISSING_TRUE_N1_PARENT_INCIDENCE`

## 1. Scope

$$
[\mathscr O]=\frac92,
\qquad
(j_L,j_R)=\left(\frac32,0\right),
\qquad
|\mathscr O|=1,
\qquad
r_{\rm P}(\mathscr O)=-1.
$$

$$
\boxed{
\mathfrak H_{\rm phys}^{\rm vec,bg}
:=\mathfrak H_{\rm pure\ gauge}
\big|_{\tau=0}
}
$$

The equality $\tau=0$ is the physical four-dimensional projection.  It is
not a statement in the full DRED traceless-spurion module.

## 2. PBW relations

$$
\begin{gathered}
\{\nabla_a,\bar\nabla_{\dot b}\}
=-2\mathcal D_{a\dot b},\\
[\nabla_a,\mathcal D_{b\dot b}]
=-2\epsilon_{ab}\widetilde W_{\dot b},\\
[\bar\nabla_{\dot a},\mathcal D_{b\dot b}]
=-2\epsilon_{\dot a\dot b}W_b,\\
[\mathcal D_{a\dot a},\mathcal D_{b\dot b}]
=\epsilon_{\dot a\dot b}\nabla_{(a}W_{b)}
+\epsilon_{ab}\bar\nabla_{(\dot a}
\widetilde W_{\dot b)}.
\end{gathered}
$$

$$
\bar\nabla_{\dot a}W_b=0,
\qquad
\nabla_a\widetilde W_{\dot b}=0,
$$

$$
\nabla_a\nabla_bW_c
=-\epsilon_{ab}\nabla_cE,
\qquad
\mathcal D_a{}^{\dot a}\widetilde W_{\dot a}
=-\frac12\nabla_a\bar E,
\qquad
E=\bar E=0.
$$

The $N=0$ blocks are

$$
M_0\in\operatorname{Mat}_{40\times40}(\mathbb Q),
\qquad
\operatorname{rank}M_0=40,
$$

$$
M_{0,J}\in\operatorname{Mat}_{320\times320}(\mathbb Q),
\qquad
\operatorname{rank}M_{0,J}=320.
$$

Thus the complete $N=0$ block, including local source jets, has zero
quotient.

For the canonical $N=1$ terminal basis and its EOM carriers,

$$
M_{1,{\rm term}}\in
\operatorname{Mat}_{40\times40}(\mathbb Q),
\qquad
\operatorname{rank}M_{1,{\rm term}}=40.
$$

Let

$$
M_{1\to2}\in\operatorname{Mat}_{126\times4866}(\mathbb Q)
$$

be the indexed curvature-child matrix.  Its $4866$ columns are ordered-word
and event coordinates; they are not $4866$ independent $N=1$ parents.

The required incidence is

$$
C_1:\mathbb Q^{20}\longrightarrow\mathbb Q^{4866}.
$$

It must contain the word-order, Koszul, terminal-PBW, EOM, and source-jet
incidences.  It is not constructed.

The skeleton/copy-only map

$$
A_0:\mathbb Q^{4866}\longrightarrow\mathbb Q^{20}
$$

does not suffice.  In one fixed parent fiber,

$$
(\text{skeleton},\mu)=(W0_T1_N1_B1_D2, 0),
$$

$$
(q_{\rm PBW}M_{1\to2})_{0}
=-2,
\qquad
(q_{\rm PBW}M_{1\to2})_{6}
=0.
$$

Hence $q_{\rm PBW}M_{1\to2}$ does not factor through $A_0$.

The indexed $N=2$ carrier has

$$
\dim V_2^{\rm ind}=126.
$$

Its physical PBW normal form is

$$
C:=J_{AB}K^{AB}{}_{CD}
\widetilde W^C_{\dot a}
\mathcal D_{(a}{}^{\dot a}
\nabla_bW_{c)}^D.
$$

Only four indexed rows have nonzero image:

$$
q_{\rm PBW}(e_0)=q_{\rm PBW}(e_2)=C,
\qquad
q_{\rm PBW}(e_{13})=q_{\rm PBW}(e_{19})=-2C.
$$

All remaining rows reduce to $E$, $\bar E$, a chirality relation, or the
$W\widetilde W\widetilde W$ sector, whose physical $(3/2,0)$ multiplicity is
zero.

For the local source jet

$$
S_{\mathcal D J}
:=(\mathcal D_a{}^{\dot a}J_{AB})
K^{AB}{}_{CD}
\widetilde W^C_{\dot a}\nabla_bW_c^D,
$$

$$
C+C_{\rm split}+S_{\mathcal D J}=0,
\qquad
C_{\rm split}=0,
\qquad
S_{\mathcal D J}=-C.
$$

For this $N=2$ candidate block, the exact relation matrix is

$$
R_2^{\rm cand}\in\operatorname{Mat}_{126\times127}(\mathbb Q),
\qquad
\operatorname{rank}R_2^{\rm cand}=126,
$$

$$
\boxed{
\dim\left(
\mathbb Q^{127}/\operatorname{row}R_2^{\rm cand}
\right)=1.}
$$

This is not the total filtered quotient until $C_1$ and the terminal
normal-order relation matrix are assembled.

The source momentum remains local:

$$
p_J+p_T+p_W=0,
\qquad
p_J\ne0.
$$

## 3. Indexed-event intertwiner

$$
M_{1\to2}\in
\operatorname{Mat}_{126\times4866}(\mathbb Q),
$$

$$
q_{\rm PBW}M_{1\to2}
\in\operatorname{Mat}_{1\times4866}(\mathbb Q).
$$

$$
N_{\rm nonzero}(q_{\rm PBW}M_{1\to2})
=190.
$$

The stored sparse vector has SHA-256
`6aa93da2a9b7321341615dee96cf419f1be409f3dccf32f08f8197afd1159811`.  It contains every indexed
$[\nabla,\mathcal D]$, $[\bar\nabla,\mathcal D]$, and
$[\mathcal D,\mathcal D]$ child.

The multiplicity-space map lifts as

$$
q_{\rm PBW}\otimes\mathbf1_{(3/2,0)}:
\mathbb Q^{504}\longrightarrow\mathbb Q^4,
\qquad
\operatorname{rank}=4.
$$

## 4. Quadratic-jet boundary

For each orientation use $(u,t,s)=(p_W,p_T,p_J)$.  The exact boundary is

$$
u+t+s=0,
\qquad
t=0.
$$

For the two orientations,

$$
R_T\in\operatorname{Mat}_{4\times6}(\mathbb Q),
\qquad
\operatorname{rank}R_T=4,
\qquad
\dim T_2=2.
$$

$$
\bar\ell_2^{(N=2)}[C]
=\begin{pmatrix}1\\-1\end{pmatrix},
\qquad
\begin{pmatrix}1&0\end{pmatrix}
\bar\ell_2^{(N=2)}=1.
$$

$$
\boxed{\ker\bar\ell_2^{(N=2)}=0.}
$$

The executable $N=2$ square is

$$
\boxed{q_T\ell_2^{(N=2),{\rm raw}}
=\bar\ell_2^{(N=2)}q_2.}
$$

## 5. Simultaneous color/species exchange

$$
K_S^{AB}{}_{DE}
=\frac12\left(
f_{ARD}f_{BRE}+f_{BRD}f_{ARE}
\right),
$$

$$
K_S^{BA}{}_{ED}=K_S^{AB}{}_{DE}.
$$

Let $\tau$ exchange $D\leftrightarrow E$.  Since the two elementary quantum
letters $W$ and $\widetilde W$ are odd, the combined exchange is

$$
\mathsf X_g(u,v)=(-\tau v,-\tau u),
\qquad
P_+=\frac12(1+\mathsf X_g).
$$

For the actual reflected jet,

$$
L_K=(K_S,-\tau K_S),
$$

$$
\mathsf X_gL_K=L_K,
\qquad
\boxed{P_+L_K=L_K\ne0.}
$$

The exact $SU(2)$ witness gives

$$
\operatorname{rank}K_S=6,
\qquad
\operatorname{rank}L_K=6.
$$

For a nonabelian compact algebra,

$$
K_S^{AA}{}_{DD}
=\sum_R f_{ARD}^2>0
$$

for some $A,D$, so the fixed actual $K_S$ line is nonzero.

## 6. Boundary

$$
\boxed{
\ker\bar\ell_2
\text{ on the total physical-4d filtered quotient}
=\texttt{FAIL\_CLOSED\_MISSING\_C1}.}
$$

$$
\boxed{
\text{full DRED traceless-}\tau\text{ quotient}
=\texttt{NOT CLAIMED},
\qquad
\text{full quantum BV source cohomology}
=\texttt{NOT CLAIMED}.}
$$
