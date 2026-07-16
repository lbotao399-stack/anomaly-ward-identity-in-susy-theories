# Step 5 ordered $AB_1$ marked-edge Schwinger--Dyson orbit

Status: `AB1_NINE_DIRECTED_TRIANGLES_EIGHTEEN_MARKS_ENUMERATED__G1_G2_GENERIC_PQ_FULL_DWORDS_REBUILT__G3_TRANSPORTED_THREE_EDGE_ORBIT_REBUILT__NONLINEAR_AND_EXPLICIT_CONTACT_OCCURRENCES_SEPARATED__ORDERED_EOM_CONTACT_QUOTIENT_OPEN__TARGET_BLIND`.

No holomorphic-twist coefficient is used below.

## 1. Notation

Let

$$
A:=\nabla_+W_+,
\qquad
B_1:=\nabla_+\Phi_1,
\qquad
C_s:=\widetilde\Phi_s,
$$

$$
\mathscr E_V
=\nabla^aW_a-2i(\Phi_s\times C_s),
$$

$$
\mathscr E_{\widetilde1}
=-\frac14\nabla^2\Phi_1
-\frac1{\sqrt2}\varepsilon_{1st}(C_s\times C_t).
$$

The two actual outer-derivative occurrences are

$$
\nabla_-(AB_1)
=(\nabla_-A)B_1+A(\nabla_-B_1),
$$

$$
\nabla_-A
=-\nabla_+\mathscr E_V-2i(B_s\times C_s),
$$

$$
\nabla_-B_1
=-2\mathscr E_{\widetilde1}
-\sqrt2\varepsilon_{1st}(C_s\times C_t).
$$

For an internal edge $e$,

$$
D_e:=r_{e,d}^2,
\qquad
\bar r_e^{,2}=D_e+\mu_\ell^2,
\qquad
\bar\Box_e=-\bar r_e^{,2}.
$$

Hence a selected source kernel has the exact form

$$
8\bar\Box_e\mathcal R_e
=-8D_e\mathcal R_e-8\mu_\ell^2\mathcal R_e.
$$

Its full-$d$ Schwinger cut and contact obey

$$
\frac{-8D_e\mathcal R_e}{D_eD_jD_k}
+\frac{8\mathcal R_e}{D_jD_k}=0,
$$

whereas four-dimensional $D$-algebra leaves

$$
\boxed{
\frac{8\bar\Box_e\mathcal R_e}{D_eD_jD_k}
+\frac{8\mathcal R_e}{D_jD_k}
=-\frac{8\mu_\ell^2\mathcal R_e}{D_eD_jD_k}.}
$$

The bubble on the second term is the concrete cut. It is not added again:

$$
\boxed{\texttt{NO\_DOUBLE\_COUNT\_PARENT\_MINUS\_CUT}.}
$$

## 2. $G_1=(I[u,\phi_1],M_1,\mathcal V_{VVV})$

For each chirality, $pi\in S_3$, and $a\in\{QL,LQ\}$, define the two selected-edge residuals by

$$
D_-D_+\bar D^2D_+
=8\bar\Box_{SV}D_+
-\frac12D_+\bar D^2D^2,
$$

$$
D_-D_+\bar D^2D^2
=8\bar\Box_{S\Phi}D^2.
$$

Thus $\mathcal R^A_{\chi,\pi,a}$ retains only the first term of the first identity, while $\mathcal R^B_{\chi,\pi,a}$ is the second identity.  This defines only the source-selected subtotal.  The remaining longitudinal word must be transported by graded integration by parts and every neighboring inverse square must receive its own Schwinger cut.

With $q=-p$, $\ell=L+yp$, and output normalized by $i\bar\sigma^{m\dot a2}p_m$, exact Grassmann integration gives

$$
\begin{array}{c|rr|rr}
\pi&\mathcal R^A_{+,QL}&\mathcal R^A_{+,LQ}
&\mathcal R^B_{+,QL}&\mathcal R^B_{+,LQ}\\ \hline
(0,1,2)&0&-128/3&0&0\\
(0,2,1)&0&-128/3&128/3&0\\
(1,0,2)&0&0&0&128/3\\
(1,2,0)&-128/3&0&0&128/3\\
(2,0,1)&0&0&128/3&0\\
(2,1,0)&-128/3&0&0&0
\end{array}
$$

and

$$
\begin{array}{c|rr|rr}
\pi&\mathcal R^A_{-,QL}&\mathcal R^A_{-,LQ}
&\mathcal R^B_{-,QL}&\mathcal R^B_{-,LQ}\\ \hline
(0,1,2)&128/3&0&-128/3&0\\
(0,2,1)&0&0&0&0\\
(1,0,2)&128/3&0&-128/3&0\\
(1,2,0)&0&0&0&0\\
(2,0,1)&0&128/3&0&-128/3\\
(2,1,0)&0&128/3&0&-128/3
\end{array}.
$$

Therefore

$$
\begin{aligned}
\sum_{\pi,a}\mathcal R^A_{+,\pi,a}&=-\frac{512}{3},
&\sum_{\pi,a}\mathcal R^B_{+,\pi,a}&=+\frac{512}{3},\\
\sum_{\pi,a}\mathcal R^A_{-,\pi,a}&=+\frac{512}{3},
&\sum_{\pi,a}\mathcal R^B_{-,\pi,a}&=-\frac{512}{3}.
\end{aligned}
$$

Since the evanescent word is $-8\mu_\ell^2\mathcal R$,

$$
\begin{array}{c|rr}
&A\text{-marked}&B_1\text{-marked}\\ \hline
+&+4096/3&-4096/3\\
-&-4096/3&+4096/3
\end{array}.
$$

Using

$$
C^{\rm preD}_{G_1,+}
=-\frac{\hbar g^4}{8192\sqrt2},
\qquad
C^{\rm preD}_{G_1,-}
=+\frac{\hbar g^4}{8192\sqrt2},
$$

$$
D_+\phi_1=\frac1gB_1,
\qquad
D^2\bar D_{\dot a}u=-\frac{4\sqrt2}{g}D_{\dot a},
\qquad
I_{\mu^2}=\frac1{32\pi^2},
$$

one obtains

$$
\boxed{
\Gamma^{\rm selected}_{G_1,A\text{-marked}}
=+\frac23\lambda_1\mathbb F^{AB}{}_{DE}
\langle D^D,B_1^E\rangle,}
$$

$$
\boxed{
\Gamma^{\rm selected}_{G_1,B\text{-marked}}
=-\frac23\lambda_1\mathbb F^{AB}{}_{DE}
\langle D^D,B_1^E\rangle,}
$$

$$
\boxed{
\Gamma^{\rm selected}_{G_1,A\text{-marked}}
+\Gamma^{\rm selected}_{G_1,B\text{-marked}}=0.}
$$

This equality is not the full $G_1$ result.  Keep $p$ and $q$ independent,
with $p$ on the external $B_1$ leg and $q$ on the external $D$ leg.  Use

$$
r_0=L+yp+z(p+q),
\qquad
p=e_1,
\qquad
q=e_4.
$$

For every polarized word, let $T_{\chi,X}(y,z)$ be the sum of the $L_2^2$
and $L_3^2$ coefficients, where $X=A,B$.  The exact evanescent extraction is

$$
\mathcal R_{\chi,X}^{\rm full}
=2\int_{\Sigma_2}dy,dz
\left[-\frac12T_{\chi,X}(y,z)\right].
$$

Define $\Pi_{\dot a}(v):=i\bar\sigma_E^{m\dot a2}v_m$.  The table records

$$
\mathcal R_{\chi,X}^{\rm full}
=c_p\Pi(p)+c_q\Pi(q)
$$

after summing the QL and LQ action summands of each directed route.

The parent-port census fixes the output order before any route sum.  Put

$$
U_0=u_G^I\leftrightarrow u_s^A,
\qquad
U_1=u_G^J\leftrightarrow u_M^R,
\qquad
U_2=u_G^D.
$$

The uncontracted fields are $u_G^D$ and $\phi_M^E$ for every $G_1$ route.
Thus all six routes lie in the ordered $D>B_1$ slot:

| route | $\pi$ | raw $VVV$ color word | $s_\pi$ | external fields | ordered output |
|---|---|---|---:|---|---|
| 001 | $(0,1,2)$ | $c_{IJD}$ | $+1$ | $(u,\phi_1)$ | $D>B_1$ |
| 002 | $(0,2,1)$ | $c_{IDJ}$ | $-1$ | $(u,\phi_1)$ | $D>B_1$ |
| 003 | $(1,0,2)$ | $c_{JID}$ | $-1$ | $(u,\phi_1)$ | $D>B_1$ |
| 004 | $(1,2,0)$ | $c_{JDI}$ | $+1$ | $(u,\phi_1)$ | $D>B_1$ |
| 005 | $(2,0,1)$ | $c_{DIJ}$ | $+1$ | $(u,\phi_1)$ | $D>B_1$ |
| 006 | $(2,1,0)$ | $c_{DJI}$ | $-1$ | $(u,\phi_1)$ | $D>B_1$ |

For each row,

$$
s_\pi c_{U_{\pi(0)}U_{\pi(1)}U_{\pi(2)}}
=s_\pi^2c_{IJD}=c_{IJD},
$$

and the matter color contraction gives

$$
\kappa^{AI}\kappa^{RJ}c_{IJD}\kappa^{BP}c_{REP}
=\mathbb F^{AB}{}_{DE}.
$$

The $QL,LQ$ labels are derivative placements inside the same $VVV$ action
vertex; they do not generate a $B_1>D$ output.  The six $B_1>A$ mirror routes
in the parent census have external fields $(\phi_1,u)$ and belong to a
different ordered source.

| route | mark | $(c_p,c_q)_+$ | $(c_p,c_q)_-$ | $\lambda_1^{-1}(c_p,c_q)_{\rm ordered}$ |
|---|---|---:|---:|---:|
| 001 | $A$ | $(-2048/3,-1024/3)$ | $(-1024/3,-512/3)$ | $(-1/12,-1/24)$ |
| 001 | $B_1$ | $(0,0)$ | $(1024/3,2048/3)$ | $(-1/12,-1/6)$ |
| 002 | $A$ | $(512/3,1024/3)$ | $(1024,512)$ | $(-5/24,-1/24)$ |
| 002 | $B_1$ | $(-1024/3,-2048/3)$ | $(0,0)$ | $(-1/12,-1/6)$ |
| 003 | $A$ | $(2560/3,2048/3)$ | $(2048/3,1024/3)$ | $(1/24,1/12)$ |
| 003 | $B_1$ | $(-1024/3,-2048/3)$ | $(1024/3,2048/3)$ | $(-1/6,-1/3)$ |
| 004 | $A$ | $(-2048/3,-1024/3)$ | $(512/3,-512/3)$ | $(-5/24,-1/24)$ |
| 004 | $B_1$ | $(-1024/3,-2048/3)$ | $(0,0)$ | $(-1/12,-1/6)$ |
| 005 | $A$ | $(0,0)$ | $(-512/3,-1024/3)$ | $(1/24,1/12)$ |
| 005 | $B_1$ | $(-1024/3,-2048/3)$ | $(1024/3,2048/3)$ | $(-1/6,-1/3)$ |
| 006 | $A$ | $(-2048/3,-1024/3)$ | $(-1024/3,-512/3)$ | $(-1/12,-1/24)$ |
| 006 | $B_1$ | $(0,0)$ | $(1024/3,2048/3)$ | $(-1/12,-1/6)$ |

The last column follows without target input from

$$
\frac1{\lambda_1}
\left[
C^{\rm preD}_{G_1,+}\mathcal R_+
+C^{\rm preD}_{G_1,-}\mathcal R_-
\right]
\left(-\frac{4\sqrt2}{g^2}\right)
\frac1{32\pi^2}
=\frac{\mathcal R_+-\mathcal R_-}{4096}.
$$

Summing only the six $D>B_1$ routes, separately for the two outer marks, gives
the unquotiented differential kernels

$$
\boxed{
\Gamma_{G_1,A}^{D>B_1,\rm unquot}
=-\frac12\lambda_1\mathbb F^{AB}{}_{DE}
D_{\dot a}^D p^{\dot a}B_1^E,}
$$

$$
\boxed{
\Gamma_{G_1,B}^{D>B_1,\rm unquot}
=\lambda_1\mathbb F^{AB}{}_{DE}
D_{\dot a}^D
\left(-\frac23p-\frac43q\right)^{\dot a}B_1^E.}
$$

Therefore

$$
\boxed{
\Gamma_{G_1}^{D>B_1,\rm unquot}
=\lambda_1\mathbb F^{AB}{}_{DE}
D_{\dot a}^D
\left(-\frac76p-\frac43q\right)^{\dot a}B_1^E.}
$$

Here $p$ is carried by $B_1$ and $q$ is carried by $D$.  The typed projection
is

$$
\mathfrak p_{\dot a}D=D_{\dot a},
\qquad
\mathfrak p_{\dot a}B_1=P_{\dot a}B_1.
$$

Therefore, for exact coefficients $a,b$,

$$
D_{\dot a}^D(ap+bq)^{\dot a}B_1^E
=a\langle D^D,B_1^E\rangle
+b(P^{\dot a}D_{\dot a}^D)B_1^E.
$$

Consequently

$$
\boxed{
\Gamma_{G_1}^{D>B_1,\rm unquot}
=-\frac76\lambda_1\mathbb F^{AB}{}_{DE}
\langle D^D,B_1^E\rangle
-\frac43\lambda_1\mathbb F^{AB}{}_{DE}
(P^{\dot a}D_{\dot a}^D)B_1^E.}
$$

The first coefficient is the ordered $D>B_1$ pair coefficient.  The second
term is the retained divergence/EOM carrier.  No relation between $p$ and
$q$, total-derivative quotient, EOM quotient, or cohomology quotient has been
imposed.

For every metric term, replacing the four-dimensional loop trace by the full
$d$-dimensional trace makes its parent plus derivative-of-action contact zero.
The remainder is exactly the $-\tfrac12T_{\chi,X}\mu_\ell^2$ word integrated
above.  For the source-selected pieces,

$$
\mathcal C^A_{\chi,\pi,a}
=+8\mathcal R^A_{\chi,\pi,a},
\qquad
\mathcal C^B_{\chi,\pi,a}
=+8\mathcal R^B_{\chi,\pi,a}.
$$

$\mathcal C^A$ is the functional derivative of the cubic gauge vertex hit by
$\mathscr E_V$, and $\mathcal C^B$ is the functional derivative of $M_1$ hit
by $\mathscr E_{\widetilde1}$.  Their nonlinear-letter, outer-connection,
cubic-bubble, and quartic representations are collapsed-$K$ presentations of
the same SD contacts, not additional anomaly terms.  The pointwise current
cancellations in Section 4.3 apply before this occurrence quotient.

## 3. $G_2=(I[u,\phi_1],M_{1,L},M_{1,R})$

Use

$$
r_0:\ S\Phi_1\to L\widetilde\Phi_1,
\qquad
r_1:\ L\Phi_1\to R\widetilde\Phi_1,
\qquad
r_2:\ Ru\to Su.
$$

For route 007 the parent-port census gives external fields $(\phi_1,u)$.
Hence $p$ is carried by the left $B_1$ output, $q$ is carried by the right
$D$ output, and the native ordered slot is $B_1>D$.  Cyclically writing the
source $B_1$ edge first, the A-marked selected edge is $r_2$.  The exact
dotted projections are

$$
\boxed{
\mathcal R_{G_2,A;\dot0}=-128r_{0,+\dot2},
\qquad
\mathcal R_{G_2,A;\dot1}=+128r_{0,+\dot1}.}
$$

The parent transverse square and its DRED defect are

$$
8\det(r_2)\mathcal R_{G_2,A},
\qquad
-8\mu_\ell^2\mathcal R_{G_2,A}.
$$

The explicit source current

$$
-2ig^3(B_1\times C_1)B_1
$$

with one $M_1$ action vertex produces the one-vertex bubble

$$
\boxed{
\mathcal C_{G_2,A;\dot0}^{\rm raw}=-128r_{0,+\dot2},
\qquad
\mathcal C_{G_2,A;\dot1}^{\rm raw}=+128r_{0,+\dot1}.}
$$

The parent primary raw word is eight times this bubble.  The source/action/propagator scalar is the inverse factor:

$$
\left|C_{G_2,A\text{-contact}}^{\rm preD}\right|
=\frac{\sqrt2\hbar g^4}{128}
=8\left|C_{G_2}^{\rm preD}\right|,
$$

$$
C_{G_2}^{\rm preD}
=\frac{\sqrt2\hbar g^4}{1024}.
$$

After the oriented color contraction

$$
(T_E)^B{}_X(T_A)^X{}_D
=-\mathbb F^{AB}{}_{DE},
$$

the source-selected target-blind momentum kernel is

$$
\boxed{
\Gamma_{G_2,A}^{D\text{-first},\rm selected}
=-\frac23\lambda_1\mathbb F^{AB}{}_{DE}
D_{\dot a}^{E}(2p+q)^{\dot a}B_1^D.}
$$

Because $B_1$ and $D$ are odd,

$$
\boxed{
\Gamma_{G_2,A}^{B_1>D,\rm selected}
=+\frac23\lambda_1\mathbb F^{AB}{}_{DE}
B_1^D(2p+q)^{\dot a}D_{\dot a}^{E}.}
$$

It is not the full outer-$A$ word.  Write

$$
K:=(p+q-r_0)_+\wedge q_-=-r_{2,+}\wedge q_-.
$$

The exact unprojected replay gives

$$
\begin{aligned}
F_{G_2,A;\dot0}
&=-1024r_{0,+\dot2}\,\mathcal F,\\
F_{G_2,A;\dot1}
&=+1024r_{0,+\dot1}\,\mathcal F,
\end{aligned}
$$

$$
\begin{aligned}
F^{\rm transverse}_{G_2,A;\dot0}
&=-1024r_{0,+\dot2}\det(r_2),\\
F^{\rm transverse}_{G_2,A;\dot1}
&=+1024r_{0,+\dot1}\det(r_2),
\end{aligned}
$$

$$
\boxed{
\begin{aligned}
F^{\rm longitudinal}_{G_2,A;\dot0}
&=+1024r_{0,+\dot2}K,\\
F^{\rm longitudinal}_{G_2,A;\dot1}
&=-1024r_{0,+\dot1}K.
\end{aligned}}
$$

Thus $\mathcal F=\det(r_2)-K$.  The longitudinal tensor is nonzero even
though one dotted component has vanishing four-dimensional trace.

Use the Euclidean frame

$$
p=e_1,
\qquad
q=e_4,
\qquad
r_0=L+yp+z(p+q).
$$

The exact coefficients of $L_m^2$ in the two dotted probe components are

$$
\begin{aligned}
\operatorname{diag}F_{\dot0}^{\rm full}
&=1024i\bigl(3y+3z-2,y+z,y+z,y+z\bigr),\\
\operatorname{diag}F_{\dot1}^{\rm full}
&=1024\bigl(z,z,z-1,3z-1\bigr).
\end{aligned}
$$

The $e_2,e_3$ transverse traces are

$$
\operatorname{tr}_\perp F_{\dot0}^{\rm full}
=2048i(y+z),
\qquad
\operatorname{tr}_\perp F_{\dot1}^{\rm full}
=1024(2z-1).
$$

The exact DRED extraction is $-\tfrac12\operatorname{tr}_\perp$.  Since

$$
p^{\dot a}=(-i,0),
\qquad
q^{\dot a}=(0,-1)
$$

in this frame, the normalized simplex integral gives

$$
\boxed{
V_{G_2,A}^{\rm ev,probe}
=\frac{512}{3}(4p-q)^{\dot a}\mu_\ell^2.}
$$

The probe obeys

$$
D^2\bar D_{\dot a}u_{\rm probe}\big|=-2.
$$

Therefore the coefficient of the general $D^2\bar D_{\dot a}u$ word is

$$
\boxed{
N_{G_2,A}^{\rm ev,full}
=\frac{256}{3}(q-4p)^{\dot a}
(D^2\bar D_{\dot a}u)(D_+\phi_1)\mu_\ell^2.}
$$

The selected and longitudinal pieces are separately

$$
N_{G_2,A}^{\rm ev,selected}
=-\frac{512}{3}(2p+q)^{\dot a}
(D^2\bar D_{\dot a}u)(D_+\phi_1)\mu_\ell^2,
$$

$$
N_{G_2,A}^{\rm ev,longitudinal}
=+256q^{\dot a}
(D^2\bar D_{\dot a}u)(D_+\phi_1)\mu_\ell^2.
$$

Their sum is exactly the full word.

Both matter vertices are full $D$-term vertices, so there is no omitted
endpoint projector and the endpoint factor is $1$.  The complete scalar is

$$
\begin{aligned}
C_{G_2}^{\rm preD}
&=\left(-\frac{g^2}{4\sqrt2}\right)
\left(\frac{\sqrt2g}{\hbar}\right)^2
\left[-\hbar\left(\frac{\hbar}{16}\right)^2\right]
\left(\frac1{2!}\right)(2)\\
&=+\frac{\sqrt2\hbar g^4}{1024}.
\end{aligned}
$$

Using

$$
D^2\bar D_{\dot a}u=-\frac{4\sqrt2}{g}D_{\dot a},
\qquad
D_+\phi_1=\frac1gB_1,
$$

$$
(T_E)^B{}_X(T_A)^X{}_D=-\mathbb F^{AB}{}_{DE},
\qquad
I_{\mu^2}=\frac1{32\pi^2},
$$

one obtains

$$
\boxed{
\Gamma_{G_2,A}^{D\text{-first},\rm unquot}
=+\frac13\lambda_1\mathbb F^{AB}{}_{DE}
D_{\dot a}^{E}(q-4p)^{\dot a}B_1^D.}
$$

Equivalently,

$$
-\frac23(2p+q)+q=\frac13(q-4p).
$$

Graded reordering into the census output slot gives

$$
\boxed{
\Gamma_{G_2,A}^{B_1>D,\rm unquot}
=+\frac13\lambda_1\mathbb F^{AB}{}_{DE}
B_1^D(4p-q)^{\dot a}D_{\dot a}^{E}.}
$$

Using $\mathfrak pD=D$ and $\mathfrak pB_1=PB_1$,

$$
\boxed{
\Gamma_{G_2,A}^{B_1>D,\rm unquot}
=+\frac43\lambda_1\mathbb F^{AB}{}_{DE}
\langle B_1^D,D^E\rangle
-\frac13\lambda_1\mathbb F^{AB}{}_{DE}
B_1^D(P^{\dot a}D_{\dot a}^{E}).}
$$

The first coefficient belongs to $B_1>D$.  The second term is the retained
divergence/EOM carrier; it is not set to zero here.

The nonlinear-current and explicit-current words cancel pointwise as in
Section 4.3.  The full-$d$ metric terms pair only with their
derivative-of-action collapsed-$K$ contacts; they are not added again.

Here $p$ exits at $L$ and $q$ exits at $R$.  Reversing the attachment requires

$$
L\leftrightarrow R,
\qquad
p\leftrightarrow q,
\qquad
\mathcal P_+(L,R;r_1)longrightarrow
\mathcal P_-(R,L;-r_1).
$$

The reversed endpoint kernel belongs to the separately ordered $B_1>A$
source.  It is not a second occurrence of the $A>B_1$ route.  Therefore the
present route occurs once and receives no reflection factor.

For the B-marked source-chiral edge,

$$
\boxed{
\mathcal R_{G_2,B;\dot0}
=\mathcal R_{G_2,B;\dot1}=0.}
$$

Consequently its source-selected physical full-$d$ cut and the matching collapsed $M_1$ contact both vanish in this projection.

## 4. $G_{3,2}$ and $G_{3,3}$

Define

$$
W_{ij}:=r_{i,+\dot1}r_{j,+\dot2}
-r_{i,+\dot2}r_{j,+\dot1}.
$$

Set

$$
P:=p+q,
\qquad
W_{P0}:=P_+\wedge r_{0,+},
\qquad
W_{p0}:=p_+\wedge r_{0,+}=W_{01}.
$$

### 4.1 Full raw $D$-words

The exact two-vertex Berezin integration gives

$$
\boxed{
F_A^{\rm raw}
=-1024\det(r_0)W_{12}
+1024\det(r_1)W_{P0},}
$$

$$
\boxed{
F_B^{\rm raw}
=-1024\det(r_2)W_{p0}.}
$$

The second term in $F_A^{\rm raw}$ follows from

$$
D_-D_+\bar D^2D_+
=8\bar\Box D_+-\frac12D_+\bar D^2D^2.
$$

Define the transported bridge word

$$
\begin{aligned}
\mathcal J_{r_1}:={}&
\int d^4\theta_Md^4\theta_H\,
(D_+\bar D^2\delta_{SM})
(D_+\bar D^2\delta_{SH})
(D_M^2\delta_{MH})C_M C_H\\
={}&-128W_{P0}.
\end{aligned}
$$

Both transported $D^2$ operators are even.  Hence their two graded-IBP
signs multiply to $+1$.  Using

$$
D^2\bar D^2D^2=16\bar\Box D^2,
$$

one obtains

$$
\begin{aligned}
F_A^{\rm longitudinal,raw}
&=-\frac12
\int d^4\theta_Md^4\theta_H\,
(D_+\bar D^2\delta_{SM})
(D_+\bar D^2\delta_{SH})
(D_M^2\bar D_M^2D_M^2\delta_{MH})C_M C_H\\
&=-\frac12(16\det r_1)\mathcal J_{r_1}\\
&=-8\det(r_1)(-128W_{P0})\\
&=+1024\det(r_1)W_{P0}.
\end{aligned}
$$

### 4.2 Endpoint normalization

The antichiral measure identity is

$$
\int d^4\theta\,F
=\int d^2\bar\theta\left(-\frac14D^2F\right),
$$

therefore

$$
\int d^2\bar\theta\,D^2F
=-4\int d^4\theta\,F.
$$

The propagator scalar $1/16$ is already contained in
$C^{\rm preD}_{G_3}$.  Thus an omitted endpoint $D^2$ multiplies the raw
word by

$$
\boxed{-4,}
$$

not by $-1/64$.  Indeed

$$
\frac1{16}(-4)=-\frac14.
$$

Consequently

$$
\boxed{
N_{A,T}=+4096\det(r_0)W_{12},}
$$

$$
\boxed{
N_{A,L}=-4096\det(r_1)W_{P0},}
$$

$$
\boxed{
N_B=+4096\det(r_2)W_{p0}.}
$$

### 4.3 Three Schwinger cuts

The equal local current words below are distinct regulated occurrences.  They
are not deleted before the Schwinger orbit is assembled.  Write

$$
\mathscr E_V
=\mathscr E_V^{\rm lin}-2i(\Phi_s\times C_s),
\qquad
\nabla_+C_s=0.
$$

The two outer-$A$ source rows are

$$
\begin{aligned}
\mathcal I_{A,{\rm Euler\ current}}
&=+2i(B_s\times C_s)B_1,\\
\mathcal I_{A,{\rm explicit\ current}}
&=-2i(B_s\times C_s)B_1.
\end{aligned}
$$

Likewise the two outer-$B_1$ source rows are

$$
\begin{aligned}
\mathcal I_{B,{\rm Euler\ potential}}
&=+\sqrt2\varepsilon_{1st}(C_s\times C_t)A,\\
\mathcal I_{B,{\rm explicit\ potential}}
&=-\sqrt2\varepsilon_{1st}(C_s\times C_t)A.
\end{aligned}
$$

Their raw superspace kernels are equal and their source coefficients are
opposite, but their occurrence tags remain distinct.  Neither row has an
independent four-dimensional inverse square, so neither has a standalone
$\mu_\ell^2$ remainder.  The collapsed-$K$ contacts below are paired only
with the parent square that generated them.

Since

$$
\det(r_e)=\bar\Box_e=-\bar r_e^{,2}
=-(D_e+\mu_\ell^2),
$$

the three evanescent remainders are

$$
N_{A,T}^{\rm ev}=-4096\mu_\ell^2W_{12},
$$

$$
N_{A,L}^{\rm ev}=+4096\mu_\ell^2W_{P0},
$$

$$
N_B^{\rm ev}=-4096\mu_\ell^2W_{p0}.
$$

For the transported $r_1$ cut, the complete word multiplier is

$$
\left(-\frac12\right)(16)(-4)=+32.
$$

Thus

$$
\boxed{
N_{r_1}^{\rm contact}
=32\mathcal J_{r_1}
=-4096W_{P0}.}
$$

The Euclidean Schwinger identity

$$
0=
\left\langle\frac{\delta\mathcal O}{\delta X}\right\rangle
-\frac1\hbar
\left\langle\mathcal O\frac{\delta S_E}{\delta X}\right\rangle
$$

fixes the contact sign.  On the $r_1$ edge,

$$
\frac{+4096D_1W_{P0}}{D_0D_1D_2}
-\frac{4096W_{P0}}{D_0D_2}=0,
$$

whereas DRED leaves

$$
\frac{4096\mu_\ell^2W_{P0}}{D_0D_1D_2}.
$$

The $r_0$ derivative-of-action contact has raw word $512W_{12}$ and effective
scalar ratio $8$, giving the required $+4096W_{12}$ cut.  The $r_2$
derivative-of-action contact has raw ordered word $-128W_{p0}$.  Its two
Euler-current summands $(s,t)=(2,3),(3,2)$ each carry ratio $16$; their sum is
one collapsed-$K$ contact and gives the required $+4096W_{p0}$ cut.  They are
not two $H_-$ parents.  These are collapsed-$K$ representatives of the kinetic
SD completion, not uncancelled explicit insertion terms.  No contact is
counted twice.

### 4.4 Exact normalization ledger

The rescaled antichiral cubic action is

$$
S_{H_-}=+\frac{\sqrt2g}{3!}
\varepsilon_{rst}c_{ABC}
\int_-\widetilde\phi_r^A\widetilde\phi_s^B\widetilde\phi_t^C.
$$

Its ordered third derivative is

$$
\frac{\delta^3S_{H_-}}
{\delta\widetilde\phi_{r_1}^{A_1}
\delta\widetilde\phi_{r_2}^{A_2}
\delta\widetilde\phi_{r_3}^{A_3}}
=(3!)\frac{\sqrt2g}{3!}
\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}
=\sqrt2g\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
$$

Since $\tau_E=-1/\hbar$, its exponent coefficient is

$$
-\frac{\sqrt2g}{\hbar}
\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
$$

The $3!$ is exhausted by the ordered derivative of $1/3!$.  For fixed
$(1,2,3)$ or $(1,3,2)$ the $H_-$ parent-port multiplicity is exactly $1$.

For $G_{3,2}$,

$$
\begin{aligned}
C_{G_{3,2}}^{\rm preD}
&=\left(-\frac{g^2}{4\sqrt2}\right)
\left(+\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left[-\hbar\left(\frac{\hbar}{16}\right)
\left(\frac{\hbar}{16}\right)\right]
\left(\frac1{2!}\right)(2)\\
&=\left(-\frac{g^3}{4\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\hbar^3}{256}\right)\\
&=\left(+\frac{\sqrt2g^4}{4\hbar^2}\right)
\left(-\frac{\hbar^3}{256}\right)\\
&=-\frac{\sqrt2\hbar g^4}{1024}.
\end{aligned}
$$

For $G_{3,3}$, $\varepsilon_{132}=-1$ reverses the $H_-$ vertex sign:

$$
\boxed{
C_{G_{3,3}}^{\rm preD}
=+\frac{\sqrt2\hbar g^4}{1024}.}
$$

The two full Berezin measures send each canonical top monomial to $1/4$;
their factor $1/16$ is already included in every displayed raw $D$-word.
The remaining maps are

$$
\widetilde\phi_s^D\widetilde\phi_t^E
=\frac1{g^2}C_s^DC_t^E,
\qquad
(T_A)^D{}_Xc_{BXE}
=+i\mathbb F^{AB}{}_{DE}.
$$

### 4.5 Exact simplex integral and result

Use

$$
r_0=L+yp+z(p+q),
\qquad
0\le y\le1,
\qquad
0\le z\le1-y.
$$

Then

$$
W_{12}=(1-y-z)(p_+\wedge q_+)+q_+\wedge L_+,
$$

$$
W_{P0}=-y(p_+\wedge q_+)+P_+\wedge L_+,
$$

$$
W_{p0}=z(p_+\wedge q_+)+p_+\wedge L_+.
$$

The three odd-$L$ terms integrate to zero, and

$$
2\int_0^1dy\int_0^{1-y}dz\,(1-y-z)
=\frac13,
$$

$$
2\int_0^1dy\int_0^{1-y}dz\,y
=\frac13,
$$

$$
2\int_0^1dy\int_0^{1-y}dz\,z
=\frac13.
$$

Equivalently, before integration,

$$
\boxed{
-W_{12}+W_{P0}-W_{p0}
=-p_+\wedge q_+.}
$$

Using

$$
\int_\ell\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2},
\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2},
$$

each of the three square branches gives

$$
\Gamma_{G_{3,2},A_T}
=\Gamma_{G_{3,2},A_L}
=\Gamma_{G_{3,2},B}
=+\frac23i\sqrt2\lambda_1
\mathbb F^{AB}{}_{DE}\langle C_2^D,C_3^E\rangle,
$$

$$
\Gamma_{G_{3,3},A_T}
=\Gamma_{G_{3,3},A_L}
=\Gamma_{G_{3,3},B}
=-\frac23i\sqrt2\lambda_1
\mathbb F^{AB}{}_{DE}\langle C_3^D,C_2^E\rangle.
$$

Therefore the three-square DRED kernels, before the final ordered
EOM/contact quotient, are

$$
\boxed{
\Gamma_{G_{3,2}}^{\rm unquot}
=+2i\sqrt2\lambda_1
\mathbb F^{AB}{}_{DE}\langle C_2^D,C_3^E\rangle,}
$$

$$
\boxed{
\Gamma_{G_{3,3}}^{\rm unquot}
=-2i\sqrt2\lambda_1
\mathbb F^{AB}{}_{DE}\langle C_3^D,C_2^E\rangle.}
$$

### 4.6 Executable occurrence table

The rows below are the rows checked by
`scripts/step5_ab1_marked_sd_orbit_exact_audit.py`.  A contact row has no
standalone $\mu_\ell^2$ term; its entry in the fifth column is the remainder
of the displayed parent-minus-full-$d$-contact pair.

| id | source occurrence | raw $D$-word before scalar normalization | marked edge / contact | signed $\mu_\ell^2$ simplex word | ordered output in $\lambda_1$ units |
|---|---|---|---|---|---|
| `G2-A-E0` | outer $A$, linear Euler | $8\det(r_2)\mathcal R_2$, $\mathcal R_{2,\dot0}=-128r_{0,+\dot2}$, $\mathcal R_{2,\dot1}=+128r_{0,+\dot1}$ | $r_2$ / $8\mathcal R_2$ | $-\frac{512}{3}(2p+q)^{\dot a}(D^2\bar D_{\dot a}u)(D_+\phi_1)$ | $+\frac23B_1^D(2p+q)^{\dot a}D_{\dot a}^E$ |
| `G2-A-L` | outer $A$, longitudinal metric row | $F^L_{\dot0}=+1024r_{0,+\dot2}K$, $F^L_{\dot1}=-1024r_{0,+\dot1}K$, $K=-r_{2,+}\wedge q_-$ | no factorable single-edge square; full-$d$ metric contact | $+256q^{\dot a}(D^2\bar D_{\dot a}u)(D_+\phi_1)$ | $-B_1^Dq^{\dot a}D_{\dot a}^E$ |
| `G2-A-JE` | Euler-current source contact | common bubble kernel $\mathcal R_2$ | zero-square source row | $0$ | $0$ standalone |
| `G2-A-JX` | explicit-current source contact | the same kernel with opposite source coefficient | zero-square source row | $0$ | $0$ standalone |
| `G2-B-E` | outer $B_1$, full Euler word | $0$ in both dotted projections | none | $0$ | $0$ |
| `G3-A-E0` | outer $A$, linear Euler | $-1024\det(r_0)W_{12}$ | $r_0$ / raw contact $+512W_{12}$ with scalar ratio $8$ | $-\frac{4096}{3}(p_+\wedge q_+)$ | $+\frac23i\sqrt2\langle C_2^D,C_3^E\rangle$; flavor $3$ has the opposite sign |
| `G3-A-L1` | outer $A$, transported longitudinal | $+1024\det(r_1)W_{P0}$ | $r_1$ / core $-128W_{P0}$ with multiplier $32$ | $+4096(-\frac13)(p_+\wedge q_+)=-\frac{4096}{3}(p_+\wedge q_+)$ | $+\frac23i\sqrt2\langle C_2^D,C_3^E\rangle$; flavor $3$ has the opposite sign |
| `G3-A-JE` | Euler-current source contact | $+512W_{12}$ | zero-square source row | $0$ | $0$ standalone |
| `G3-A-JX` | explicit-current source contact | $-512W_{12}$ | zero-square source row | $0$ | $0$ standalone |
| `G3-B-E2` | outer $B_1$, kinetic Euler | $-1024\det(r_2)W_{p0}$ | $r_2$ / core $-128W_{p0}$ with signed multiplier $-32$ | $-\frac{4096}{3}(p_+\wedge q_+)$ | $+\frac23i\sqrt2\langle C_2^D,C_3^E\rangle$; flavor $3$ has the opposite sign |
| `G3-B-PE` | Euler-potential source contact | $-128W_{p0}$ | zero-square source row | $0$ | $0$ standalone |
| `G3-B-PX` | explicit-potential source contact | $+128W_{p0}$ | zero-square source row | $0$ | $0$ standalone |

Thus the exact native $G_2$ outer-$A$ sum is

$$
\frac23B_1(2p+q)D-B_1qD
=\frac13B_1(4p-q)D,
$$

and the exact $G_3$ square-word sum is

$$
-\frac{4096}{3}-\frac{4096}{3}-\frac{4096}{3}
=-4096.
$$

### 4.7 Gate-2S normalization and routing adjudication

For each constrained matter propagator,

$$
\frac1{16}\bar D^2D^2
=\left(-\frac14\bar D^2\right)
\left(-\frac14D^2\right).
$$

At the pure antichiral $H_-$ vertex one normalized endpoint factor is used on
the measure:

$$
\left(-\frac14D^2\right)\theta^2
=\left(-\frac14\right)(-4)=1.
$$

The scalar $-1/4$ is already inside the $1/16$ retained in
$C_{G_3}^{\rm preD}$, while the raw polynomial omits the corresponding
unnormalized $D^2$.  Hence the raw polynomial must still be multiplied by

$$
\boxed{D^2\theta^2=-4.}
$$

Using both $1/16$ propagator scalars and the raw integer $1024$ without this
$-4$ counts the scalar half of the endpoint factor but omits its derivative
saturation.

For fixed $(1,2,3)$ flavors, the six permutations in

$$
\frac{\sqrt2g}{3!}\varepsilon_{rst}c_{ABC}C_r^AC_s^BC_t^C
$$

all have weight

$$
\operatorname{sgn}_{\varepsilon}(\pi)
\operatorname{sgn}_{c}(\pi)=1.
$$

Therefore

$$
\frac1{3!}\sum_{\pi\in S_3}1=1,
$$

and the ordered third derivative is $\sqrt2g\varepsilon_{123}c_{BXE}$.
There is no further factor $2$ for $(2,3)$ and $(3,2)$.

Finally, the direct unsplit outer-$A$ replay gives

$$
N_A^{\rm direct}
=-1024\det(r_0)W_{12}
+1024\det(r_1)W_{P0}.
$$

Changing to incoming variables $p_G=-q$, $q_G=-p$ gives

$$
P_G=-(p+q),
\qquad
W_{P_G0}=-W_{P0},
$$

so routing covariance requires

$$
N_A^{\rm direct}
=-1024\det(r_0)W_{12}
-1024\det(r_1)W_{P_G0}.
$$

Changing $W_{P0}$ to $W_{P_G0}$ while retaining the old plus coefficient
changes the polynomial by

$$
2048\det(r_1)W_{P_G0}\ne0.
$$

That noncovariant sign change is the source of the claimed outer-$A$
simplex cancellation.  In the locked outgoing routing,

$$
2\int_{\Sigma_2}W_{12}=+\frac13(p_+\wedge q_+),
\qquad
2\int_{\Sigma_2}W_{P0}=-\frac13(p_+\wedge q_+),
$$

and the coefficients in the evanescent word are respectively $-4096$ and
$+4096$; both contributions are $-4096(p_+\wedge q_+)/3$.

The factor $2$ is the unquotiented sum of the $r_0,r_1,r_2$ square branches,
$3(2/3)=2$.  It contains neither zero-square source-current row as an anomaly
term nor a second $H_-$ parent.  The nonlinear and explicit source rows remain
separately tagged in Section 4.3, and the fixed $H_-$ parent-port multiplicity
is $1$ in Section 4.4.

The dimensions close exactly:

$$
[d^4\ell]+[\mu_\ell^2]+[p_+\wedge q_+]-3[D_e]
=4+2+2-6=2,
$$

$$
[C_sC_t]=2,
\qquad
[\Gamma_{G_3}]=2+2=4.
$$

## 5. Exact directed triangle and mark ledger

The ordered source is $A>B_1$.  Every route has source $0$, left action
vertex $1$, right action vertex $2$, source-to-left $A$ edge, left-to-right
bridge, and right-to-source $B_1$ edge.

| route | left port pair | right port pair | topology | external output order | marked inverse-edge occurrences |
|---|---|---|---|---|---|
| 001 | $G[0,1]$ | $M_1[0,1]$ | TGM | $D>B_1$ | $A$ edge, $B_1$ edge |
| 002 | $G[0,2]$ | $M_1[0,1]$ | TGM | $D>B_1$ | $A$ edge, $B_1$ edge |
| 003 | $G[1,0]$ | $M_1[0,1]$ | TGM | $D>B_1$ | $A$ edge, $B_1$ edge |
| 004 | $G[1,2]$ | $M_1[0,1]$ | TGM | $D>B_1$ | $A$ edge, $B_1$ edge |
| 005 | $G[2,0]$ | $M_1[0,1]$ | TGM | $D>B_1$ | $A$ edge, $B_1$ edge |
| 006 | $G[2,1]$ | $M_1[0,1]$ | TGM | $D>B_1$ | $A$ edge, $B_1$ edge |
| 007 | $M_1[1,0]$ | $M_1[0,2]$ | TMM | $B_1>D$ | $A$ edge, $B_1$ edge |
| 008 | $M_2[1,2]$ | $H_-[0,1]$ | TMH | $C_2>C_3$ | $A$ edge, $B_1$ edge |
| 009 | $M_3[1,2]$ | $H_-[0,2]$ | TMH | $C_3>C_2$ | $A$ edge, $B_1$ edge |

Thus

$$
\boxed{N_{\rm directed\ triangle}^{A>B_1}=9,}
$$

$$
\boxed{N_{\rm marked\ inverse\ edge}^{A>B_1}=9\cdot2=18.}
$$

For routes 008 and 009, the transported $r_1$ square belongs to the same
outer-$A$ occurrence.  It is a third cut branch, not a nineteenth mark.

## 6. Occurrence quotient

| item | classification | multiplicity rule |
|---|---|---|
| outer $D_-$ on $A$ versus on $B_1$ | `REAL_OCCURRENCE` | retain both |
| $G_2$ reversed attachment | `REVERSED_ORDERED_SOURCE` | belongs to $B_1>A$, not to this $A>B_1$ orbit |
| $G_3$ flavors $2$ and $3$ | `REAL_OCCURRENCE` | retain both with $\varepsilon_{123}=-\varepsilon_{132}$ |
| $G_3$ B-current $(2,3)$ and $(3,2)$ | `EULER_CURRENT_SUMMAND` | sum inside one collapsed-$K$ contact; no second $H_-$ parent |
| transported $G_3$ $r_1$ inverse square | `SAME_OUTER_A_OCCURRENCE_NEW_EDGE_SQUARE` | cut once; do not create a new outer mark |
| $G_1$ six label permutations and two derivative placements | `ACTION_WORD_SUMMAND` | sum all twelve per chirality; no extra $N_{VVV}$ |
| $G_1$ reverse mixed-Hessian traversal | `SAME_CLOSED_WICK_CYCLE` | removed by the supertrace $1/2$ |
| retaining the endpoint $D^2$ on either edge at the same $H_-$ vertex | `SAME_PARENT_REPRESENTATION` | count once |
| $\mathcal P_+$ at one end versus transported $\mathcal P_-$ at the other | `SAME_PARENT_REPRESENTATION` | count once |
| collapsed bubble versus abstract Schwinger cut | `SAME_CONTACT` | count once |

There is no surviving labeled automorphism that supplies an extra factor $1/2$:

$$
\frac1{2!}(1+1)=1.
$$

Verification command:

    python scripts/step5_ab1_marked_sd_orbit_exact_audit.py
