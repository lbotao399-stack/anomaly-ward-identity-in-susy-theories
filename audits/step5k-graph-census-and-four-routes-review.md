# Step 5K: seventeen candidates and four deferred Wick routes

Status: `TARGET_BLIND_17_ROWS_TYPED__4_DEFERRED_ROUTES_CLOSED`.
Authority base: `origin/main@06601a0ed4e6060e2d872980509e1b949e61506c`.
Primary-memo equation map: `(K.97)--(K.121)` in `audits/step5k-strict-supergraph-completion.md`.
The handle `0983774045f276ad4869fc6623d8069e5f74c25a` supplies grouped question
names only; no proposed verdict or HT coefficient enters this audit.
## 1. Typed meaning of the census
For a connected internal multigraph,

$$
L_G=E_G-V_G+1,
\qquad
\mathcal P_{\rm1PI}G=0
\iff G\text{ has an internal bridge}.
\tag{K17.1}
$$

DRED and the graph anomaly projector are

$$
\bar r^2=r_d^2+\mu_r^2,
\qquad
\mu_q^2=\bar q^2-q_d^2=0
\quad(q\text{ external}),
\tag{K17.2}
$$

$$
\mathcal P_{\rm anom}^{\rm graph}
=\mathcal P_{\mu^2}\mathcal P_{\rm1PI}\mathcal P_{L=1}.
\tag{K17.3}
$$

The proposal retained grouped labels, not a historical machine-readable
seventeen-row list.  Step-5K fixes the typed refinement

$$
3_{AA\,{\rm FP/NK/measure}}
+1_{\rm ghost\ spectator}
+2_{AB/BA\,{\rm FP}}
+2_{AC/CA\,{\rm FP}}
+1_{{\rm FP}_4}
+1_{S_4\,{\rm tadpole}}
+3_{\rm artifact}
+4_{\rm deferred}
=17.
\tag{K17.4}
$$

The actual deferred four are

$$
\boxed{
\mathrm{BC\!-\!TMG\!-\!TAIL},\quad
\mathrm{AC\!-\!SOURCE\!-\!CYCLE\!-\!TAIL},\quad
\mathrm{ADDA}\ I_0S_{m4},\quad
T_{H_+H_-}.}
\tag{K17.5}
$$

They are not the accepted $AA$-matter occurrence rows

$$
\{F_1,F_2,X_1,X_2\}.
\tag{K17.6}
$$
## 2. Seventeen-row topology/port/$D$-word verdict

The letters and source contain no FP port.  A closed FP cycle with $m$
FP vertices, $m$ oriented ghost edges, and $a$ vector attachments to
the physical source has

$$
V_G=m+1,
\qquad E_G=m+a,
\qquad L_G=a.
\tag{K17.7}
$$

For $a=1$, the sole vector attachment is a bridge.  For $a\ge2$,
$L_G\ge2$.  Hence

$$
\boxed{
\mathcal P_{\rm1PI}\mathcal P_{L=1}
G_{\rm FP\ attached\ to\ physical\ source}=0.}
\tag{K17.8}
$$

A local massless self-edge reduces to

$$
J_m:=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}(k_d^2)^{m-1}.
\tag{K17.9}
$$

For $k=\rho^{-1}k'$,

$$
J_m=\rho^{-(d+2m-2)}J_m,
\qquad d+2m-2=2+2m-2\epsilon\ne0,
\qquad J_m=0.
\tag{K17.10}
$$

The full row table is:

| id | field/Wick word | $(V,E,L)$; 1PI | source-port and $D$-word test | verdict |
|---|---|---|---|---|
| C01 | $I_{AA}(V,V)+\mathrm{FP}_3+\mathrm{FP}_3$: two $V$ and two ghost edges | $(3,4,2)$ | closed-FP sign exists, but no one-loop word | `EXACT_ZERO` |
| C02 | $I_{AA}$, NK | no NK graph | selected branch has no NK field, vertex, or port | `EXACT_ZERO` |
| C03 | $I_{AA}$, $\varpi_E=\varpi_0$ | no graph | $\varpi_0^{-1}\delta\varpi_0/\delta q=0$ | `EXACT_ZERO` |
| C04 | source--$\mathrm{FP}_3$, two ghost edges to a second $\mathrm{FP}_3$ | $(3,3,1)$; bridge | ordinary FP self-energy only | `EXACT_ZERO` |
| C05 | $I_{AB}+\mathrm{FP}$ | one attachment 1PR; two give $L=2$ | source has no ghost port | `EXACT_ZERO` |
| C06 | ordered $BA$ reflection | same | same port obstruction | `EXACT_ZERO` |
| C07 | $I_{AC}$--$\mathrm{FP}_3$, two ghost-cycle edges | $(3,3,1)$; bridge | AC external-leg FP self-energy | `EXACT_ZERO` |
| C08 | ordered $CA$ reflection | $(3,3,1)$; bridge | reflected self-energy word | `EXACT_ZERO` |
| C09 | $I(V,V)+\mathrm{FP}_4(V,V,c,c')$ | $(2,3,2)$ | two $V$ edges plus ghost self-edge | `EXACT_ZERO` |
| C10 | one $V$ bridge plus $\mathrm{FP}_4$ ghost tadpole | $(2,2,1)$; bridge | $J_m=0$, marked bridge has $\mu_q^2=0$ | `EXACT_ZERO` |
| C11 | old template-stamped graph object | artifact, not graph | repaired by sector-typed Step-5K IR | `EVALUATED` |
| C12 | matter triangle cloned as gauge triangle | $(3,3,1)$; 1PI | repaired to two $V$ edges plus one chiral-projector edge | `EVALUATED` |
| C13 | $I_2,I_1S_{m3},I_0S_{m4},I_0S_{m3}^2/2$ | meta-row | first three zero; last is the matter triangle | `EVALUATED` |
| C14 | $I_0^{E\text{-KIN}}S_{m3}S_{g3}$ | $(3,3,1)$; bridge | possible cycle $\mu^2$ word remains 1PR | `EXACT_ZERO` |
| C15 | $I_{0,AC}S_{m3}S_{m3}$ source-cycle-tail | $(3,3,1)$; bridge | $64q_{(4)}^2\ne0$, but $\mu_q^2=0$ | `EXACT_ZERO` |
| C16 | $I_{0,AD/DA}(V,V)S_{m4}(V,V,\Phi,\widetilde\Phi)$ | $L=2$, or $L=1$ bridge | matter self-edge is $J_m=0$ | `EXACT_ZERO` |
| C17 | $I_{0,BC}H_+H_-$ | $L=1$ bridge, or $L=2$ | $4096q_{(4)}^2\ne0$; no $D,D$ ports | `EXACT_ZERO` |

The C13 resolvent disposal used in the table is exact:

$$
\Gamma_{g^2,\rm mat}^{(1)}
=\langle I_2\rangle
-\hbar^{-1}\langle I_1S_{m3}\rangle_c
-\hbar^{-1}\langle I_0S_{m4}\rangle_c
+(2\hbar^2)^{-1}\langle I_0S_{m3}S_{m3}\rangle_c.
\tag{K17.11}
$$

Here $I_2$ has no $BC$ matter ports and has $L=2$ when paired;
$I_1S_{m3}$ contains a source self-edge and Eq. K17.10;
$I_0S_{m4}$ has shifted numerator

$$
W_{02}
=(L_++xP_+)\wedge(L_+-(1-x)P_+)
=-L_+\wedge P_+,
\tag{K17.12}
$$

so its even-denominator integral is zero.  Only
$I_0S_{m3}S_{m3}$ is the one-loop 1PI matter parent.
## 3. $F_1,F_2,X_1,X_2$: separate accepted matter occurrences

Their field word is

$$
I_{AA}(u_A,u_B)S_{m3}^{(1)}(\widetilde\Phi_1,u_1,\Phi_1)
S_{m3}^{(2)}(\widetilde\Phi_2,u_2,\Phi_2),
\qquad \frac1{2!}(1+1)=1.
\tag{K17.13}
$$

Forward attachment contracts $u_A\leftrightarrow u_1$,
$u_B\leftrightarrow u_2$, $\Phi_1\leftrightarrow\widetilde\Phi_2$ and
leaves $C_r^D,B_r^E$; crossed attachment exchanges the source-vector
endpoints.  For $r_0=k,r_1=k-q,r_2=k-p-q$, the accepted finite words are

$$
\mathcal G_0=-16384\mathcal S_{012},\qquad
\mathcal G_2=-16384\mathcal T_{012},\qquad \mathcal S_2:=\mathcal T_{012},\qquad
D_{0+}\bar D_0^2D_0^2\delta_{02}
=-D_2^2\bar D_2^2D_{2+}\delta_{02}.
\tag{K17.14}
$$

With $\lambda_1=\hbar g^2/(16\pi^2)$, their coefficients are

$$
\begin{array}{c|c}
\texttt{MW-F1}&-\frac43\lambda_1\\
\texttt{MW-F2}&+\frac13\lambda_1\\
\texttt{MW-X1}&+\frac13\lambda_1\\
\texttt{MW-X2}&-\frac43\lambda_1
\end{array}
\tag{K17.15}
$$

in the forward $\mathbb F^{AB}{}_{DE}(p_+\wedge q_+)$ and crossed
$\mathbb F^{AB}{}_{ED}(q_+\wedge p_+)$ bases.  They are four
nonzero occurrence rows, not the deferred Bucket-3 routes.
## 4. C14: BC--TMG--TAIL

The field word and selected Wick pairs are

$$
I_{0,E\text{-kin}}
=\frac12(D^2\Phi_r^A)\widetilde\Phi_s^B,
\quad
S_{m3}=\widetilde\Phi_t^U V^L\Phi_t^X,
\quad
S_{g3}=V^MV^NV^P,
\tag{K17.19}
$$

$$
D^2\Phi_r^A\leftrightarrow\widetilde\Phi_t^U,
\qquad
\widetilde\Phi_s^B\leftrightarrow\Phi_t^X,
\qquad
V^L\leftrightarrow V^M.
\tag{K17.20}
$$

Wick contraction becomes

$$
\begin{aligned}
\mathfrak W_{14}={}&
\delta_{rt}\delta_{st}\kappa^{AU}\kappa^{BX}
D_0^2G_+(r_0;0,1)G_-(r_1;0,1)G_V^{LM}(Q;1,2)\\
&\times[V^N(2)V^P(2)]_{\rm residual},
\qquad
\delta_{rt}\delta_{st}=\delta_{rs}\delta_{st}.
\end{aligned}
\tag{K17.21}
$$

The residual pair projects to

$$
[V^NV^P]_{\rm residual}
\longrightarrow D_{\dot a}^DD^{E\dot a}.
\tag{K17.22}
$$

The marked matter-edge word is

$$
\begin{aligned}
D^2P_+(r_0)\delta^4
&=\frac{D^2\bar D^2D^2}{16r_{0,d}^2}\delta^4
=\frac{\bar r_0^2}{r_{0,d}^2}D^2\delta^4\\
&=D^2\delta^4
+\frac{\mu_\ell^2}{r_{0,d}^2}D^2\delta^4.
\end{aligned}
\tag{K17.23}
$$

The first term is the contact; the second is the possible cycle anomaly.
Both retain the vector edge $e_V=(S_{m3},S_{g3})$.  The graph has two
matter edges $e_1=e_2=(I_0,S_{m3})$ and

$$
(V_G,E_G,L_G)=(3,3,1),
\qquad
G_{14}\setminus e_V
=\{I_0,S_{m3};e_1,e_2\}\sqcup\{S_{g3};D,D\}.
\tag{K17.24}
$$

Therefore

$$
\boxed{\mathcal P_{\rm1PI}G_{14}=0,
\qquad \mathcal P_{\rm anom}^{\rm graph}\mathfrak W_{14}=0.}
\tag{K17.25}
$$
## 5. C15: AC--SOURCE--CYCLE--TAIL

The word and Wick pairs are

$$
I_{0,AC}[V_I,\widetilde\Phi_{r,I}]
S_{m3}^{(1)}[\widetilde\Phi_1,V_1,\Phi_1]
S_{m3}^{(2)}[\widetilde\Phi_2,V_2,\Phi_2],
\tag{K17.26}
$$

$$
V_I\leftrightarrow V_1,
\qquad
\Phi_1\leftrightarrow\widetilde\Phi_2,
\qquad
\Phi_2\leftrightarrow\widetilde\Phi_1.
\tag{K17.27}
$$

Hence

$$
\mathfrak W_{15}
=G_V(I,1)G_+(1,2)G_-(2,1)
[\widetilde\Phi_{r,I}]_{\rm residual}[V_2]_{\rm residual}
\times(\text{typed color/flavor chain}).
\tag{K17.28}
$$

The residual operator is the ordered $C_r,D$ pair and its derivative
projections.  The ordinary cycle word is explicitly nonzero:

$$
\operatorname{Coeff}\mathfrak D_{MM}=1024q_{(4)}^2,
\quad
\mathfrak D_{MM}^{\rm collapsed}=256q_{(4)}^2,
\quad
\mathfrak D_{MM}^{\rm two\ measures}=64q_{(4)}^2.
\tag{K17.29}
$$

With $e_0=(I_0,S_{m3}^{(1)})_V$ and
$e_1=e_2=(S_{m3}^{(1)},S_{m3}^{(2)})_{\rm matter}$,

$$
(V_G,E_G,L_G)=(3,3,1),
\qquad
G_{15}\setminus e_0
=\{I_0;C_r\}\sqcup\{S_{m3}^{(1)},S_{m3}^{(2)};D\}.
\tag{K17.30}
$$

The occurrence mark is on the external-momentum bridge $e_0$, so

$$
\boxed{
\mathcal P_{\rm1PI}G_{15}=0,
\qquad \mu_{e_0}^2=\mu_q^2=0,
\qquad \mathcal P_{\rm anom}^{\rm graph}\mathfrak W_{15}=0.}
\tag{K17.31}
$$
## 6. C16: AD/DA $I_0S_{m4}$

The field word is

$$
I_{0,AD/DA}[V_I^{(1)},V_I^{(2)}]
S_{m4}[\widetilde\Phi,V_4^{(1)},V_4^{(2)},\Phi].
\tag{K17.32}
$$

No residual matter is allowed in the $D,D$ output, so

$$
\Phi(4)\leftrightarrow\widetilde\Phi(4)
\longmapsto G_+(k;4,4).
\tag{K17.33}
$$

With both vector pairs contracted,

$$
\mathfrak W_{16}^{(2)}=G_V(I,4)G_V(I,4)G_+(4,4),
\qquad (V_G,E_G,L_G)=(2,3,2).
\tag{K17.34}
$$

With one vector pair contracted,

$$
\mathfrak W_{16}^{(1)}=G_V(I,4)G_+(4,4)
[V_I]_{\rm residual}[V_4]_{\rm residual},
\qquad (V_G,E_G,L_G)=(2,2,1),
\tag{K17.35}
$$

and the sole $V$ edge is a bridge.  The residual vectors can project to
$D,D$, but remain 1PR.

The coincident chiral projector gives a finite polynomial trace,

$$
\operatorname{Tr}_\vartheta
\left[\mathcal Q(D,\bar D)
\frac{\bar D^2D^2}{16k_d^2}\delta^4(0)\right]
=\sum_{m=0}^{M}a_m(k_d^2)^{m-1}.
\tag{K17.36}
$$

No external momentum enters this self-edge; Eq. K17.10 gives

$$
\boxed{
\int_k\operatorname{Tr}_\vartheta[\cdots]=\sum_ma_mJ_m=0,
\quad
\mathcal P_{\rm anom}^{\rm graph}\mathfrak W_{16}^{(2)}
=\mathcal P_{\rm anom}^{\rm graph}\mathfrak W_{16}^{(1)}=0.}
\tag{K17.37}
$$
## 7. C17: $T_{H_+H_-}$

With $\Phi=g\Phi_c$ and $\widetilde\Phi=g\widetilde\Phi_c$, the labeled
canonical vertex words are

$$
H_+=+\sqrt2g\,\varepsilon_{abc}c_{ABC}
\Phi_{c,a}^A\Phi_{c,b}^B\Phi_{c,c}^C,
\qquad
H_-=+\sqrt2g\,\varepsilon_{abc}c_{ABC}
\widetilde\Phi_{c,a}^A\widetilde\Phi_{c,b}^B\widetilde\Phi_{c,c}^C.
\tag{K17.38}
$$

Suppressing the canonical subscript on Wick fields, the $+\!-$ orientation selects

$$
\widetilde\Phi_{s,I}\leftrightarrow\Phi_s(+),
\qquad
\Phi_t(+)\leftrightarrow\widetilde\Phi_t(-),
\qquad
\Phi_u(+)\leftrightarrow\widetilde\Phi_u(-).
\tag{K17.39}
$$

Then

$$
\mathfrak W_{17}^{+-}
=G_+(+,I)G_+(+,-)G_+(+,-)
[\Phi_{r,I}]_{\rm residual}[\widetilde\Phi_v(-)]_{\rm residual}
\times(\varepsilon\varepsilon\,cc).
\tag{K17.40}
$$

The reverse orientation reverses every chiral edge.  The two exact ordinary
words are

$$
\mathfrak D_{H_+H_-}=4096q_{(4)}^2,
\qquad
\mathfrak D_{H_-H_+}=4096q_{(4)}^2.
\tag{K17.41}
$$

Thus the zero is not a vanishing-$D$-word claim.  With
$e_0=(I_0,H_\pm)$ and $e_1=e_2=(H_+,H_-)$,

$$
(V_G,E_G,L_G)=(3,3,1),
\qquad e_0\text{ is a bridge},
\qquad \mu_{e_0}^2=\mu_q^2=0.
\tag{K17.42}
$$

The residual fields in Eq. K17.40 form a matter self-energy output.  Since
$H_\pm$ have no vector ports,

$$
\frac{\delta^2(H_+H_-)}
{\delta D_{\dot a}^D\delta D^{E\dot a}}=0.
\tag{K17.43}
$$

Contracting both source legs gives four internal edges and

$$
(V_G,E_G,L_G)=(3,4,2).
\tag{K17.44}
$$

The Euler-potential and explicit-potential contacts also cancel before
integration:

$$
\mathcal R_\epsilon I_{E,\rm pot}
+\mathcal R_\epsilon I_{X,\rm pot}
=+\sqrt2K_{\rm pot}-\sqrt2K_{\rm pot}=0.
\tag{K17.45}
$$

Therefore

$$
\boxed{
\mathcal P_{\rm anom}^{\rm graph}\mathfrak W_{17}^{+-}
=\mathcal P_{\rm anom}^{\rm graph}\mathfrak W_{17}^{-+}=0.}
\tag{K17.46}
$$
## 8. Closure

$$
N_{\rm rows}=17,
\qquad
N_{\rm artifact\ repairs}=3,
\qquad
N_{\rm exact\ zero\ physical}=14,
\qquad
N_{\rm unresolved}=0.
\tag{K17.47}
$$

$$
\boxed{
\mathcal P_{\rm anom}^{\rm graph}
(G_{14}+G_{15}+G_{16}+G_{17})=0}
\tag{K17.48}
$$

holds route by route, without using target agreement.

HT target used to decide a route: no
