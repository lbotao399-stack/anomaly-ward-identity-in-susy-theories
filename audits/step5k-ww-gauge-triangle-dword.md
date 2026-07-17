# Step 5K ordered WW gauge-sector D-word

Status:
CANONICAL_ISOLATED_DWORD_AND_FULL_48_ROW_CONTACT_STREAM_EXACT.
Machine trace:
generated/step5k-ww-gauge-dword.json.
Quadratic blocks, momentum-space propagators, and the FP two-sided inverse are
derived separately in
audits/step5k-momentum-rules-and-fp-inverse.md.  This memo contains only the
gauge/ghost WW graph trace and its normalization.
Primary-memo equation map:
`(K.55)--(K.64)`, `(K.65)--(K.76)`, `(K.87)--(K.96)`, and `(K.122)`
in `audits/step5k-strict-supergraph-completion.md`.
## 1. Fixed ledger

Define
$$
u:=\frac{V}{\sqrt2g}, \qquad A^A:=g^{-1}(\nabla_+\mathcal W_+)^A, \qquad D_{\dot\alpha}^A:=g^{-1}\widetilde{\mathcal W}_{\dot\alpha}^A,
$$
$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2}, \qquad \mathbb F^{AB}{}_{DE} :=\kappa^{AU}\kappa^{BV}\kappa^{CC'} c_{UCD}c_{VC'E}. \tag{1.1}
$$
With the phase $e^{irx}$, the locked local identities are
$$
\{D_\alpha(r),\bar D_{\dot\beta}(s)\} =-i(r+s)_{\alpha\dot\beta}, \tag{1.3}
$$
$$
D_i(r)\Delta_{ij}(r) =-D_j(-r)\Delta_{ij}(r), \qquad \bar D_i(r)\Delta_{ij}(r) =-\bar D_j(-r)\Delta_{ij}(r), \tag{1.4}
$$
where
$$
\Delta_{ij}(r):=\delta^4(\vartheta_i-\vartheta_j).
$$
The canonical vector line is
$$
\boxed{ \langle u^A(r,1)u^B(r',2)\rangle =-(2\pi)^d\delta^{(d)}(r+r') \frac{\hbar\kappa^{AB}}{r_d^2}\Delta_{12}(r)}. \tag{1.5}
$$
The common routing is
$$
r_0=k, \qquad r_1=k+q, \qquad r_2=k+p+q, \tag{1.6}
$$
$$
D_i:=r_{i,d}^2, \qquad L_1:=r_0+r_1=2k+q, \qquad L_2:=r_1+r_2=2k+p+2q. \tag{1.7}
$$
DRED is
$$
d=4-2\epsilon, \qquad \delta_4^{mn} =\widehat\delta^{mn}+\breve\delta^{mn}, \qquad \breve\delta^m{}_m=2\epsilon, \tag{1.8}
$$
$$
\bar r_e^{\,2}=r_{e,d}^{\,2}+\mu_\ell^2, \qquad \breve\delta^m{}_nk^n =\breve\delta^m{}_np^n =\breve\delta^m{}_nq^n=0. \tag{1.9}
$$
## 2. Canonical source, vertices, and Wick word

The ordered linear letter is
$$
A_c^{(1)}=Ku, \qquad K=-\frac1{4\sqrt2}D_+\bar D^2D_+, \tag{2.1}
$$
$$
D_-K =-\frac1{8\sqrt2}D^2\bar D^2D_+. \tag{2.2}
$$
For either marked occurrence,
$$
\left(-\frac1{8\sqrt2}\right) \left(-\frac1{4\sqrt2}\right) =\frac1{64}. \tag{2.3}
$$
The canonical exponent vertices are
$$
\mathfrak V_W =-\frac{ig}{4\hbar}c_{UCE}W_c^{E\gamma} (D_{C\gamma}-D_{U\gamma}), \tag{2.4}
$$
$$
\mathfrak V_{\widetilde W} =+\frac{ig}{4\hbar}c_{UCD}D_{c\dot\gamma}^{D} (\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}). \tag{2.5}
$$
The mixed action-order weight is
$$
\frac1{2!} (S_{+,3}S_{-,3}+S_{-,3}S_{+,3})=S_{+,3}S_{-,3}. \tag{2.6}
$$
For one directed source attachment, the field Wick word is
$$
\begin{aligned}
&\left\langle
u_0^{a_0}u_0^{b_0}
u_1^{a_1}u_1^{b_1}
u_2^{a_2}u_2^{b_2}
\right\rangle_\triangle\\
&=
\langle u_0^{a_0}u_1^{a_1}\rangle
\langle u_1^{b_1}u_2^{a_2}\rangle
\langle u_2^{b_2}u_0^{b_0}\rangle\\
&=
\frac{(-\hbar)^3
\kappa^{a_0a_1}\kappa^{b_1a_2}\kappa^{b_2b_0}}
{D_0D_1D_2}
\Delta_{01}(r_0)\Delta_{12}(r_1)\Delta_{20}(-r_2).
\end{aligned}
\tag{2.7}
$$
All contracted $u$'s are even.  The Wick sign and the fixed directed
port-preserving multiplicity are both $+1$.  Color contraction gives
$\mathbb F^{AB}{}_{DE}$, with no additional metric trace.
## 3. Four edge-tagged endpoint rows

Before endpoint transport, the ordered local word is
$$
\boxed{ (D^{[e_0]}-D^{[e_1]})K (\bar D^{[e_1]}-\bar D^{[e_2]})}. \tag{3.1}
$$
Use $z_0$ as the canonical endpoint of the source edges.  Equation (1.4)
gives
$$
D_1^{[e_0]}\Delta_{01} =-D_0^{[e_0]}\Delta_{01}, \qquad \bar D_2^{[e_2]}\Delta_{20} =-\bar D_0^{[e_2]}\Delta_{20}. \tag{3.2}
$$
Since $K$ is even, it gives no Koszul sign.  Direct expansion yields

| row | raw word | raw sign | ordered endpoint transfer | transfer sign | product |
|---|---|---:|---|---:|---:|
| $R_{01}$ | $D^{[e_0]}K\bar D^{[e_1]}$ | $+1$ | $D_1^{[e_0]}\to-D_0^{[e_0]}$ | $-1$ | $-1$ |
| $R_{02}$ | $D^{[e_0]}K\bar D^{[e_2]}$ | $-1$ | $D_1^{[e_0]}\to-D_0^{[e_0]}$, $\bar D_2^{[e_2]}\to-\bar D_0^{[e_2]}$ | $+1$ | $-1$ |
| $R_{11}$ | $D^{[e_1]}K\bar D^{[e_1]}$ | $-1$ | none | $+1$ | $-1$ |
| $R_{12}$ | $D^{[e_1]}K\bar D^{[e_2]}$ | $+1$ | $\bar D_2^{[e_2]}\to-\bar D_0^{[e_2]}$ | $-1$ | $-1$ |
Thus
$$
s_{\rm raw}=(+1,-1,-1,+1), \qquad s_{\rm transfer}=(-1,+1,+1,-1), \tag{3.3}
$$
$$
\boxed{s_{\rm raw}s_{\rm transfer}=(-1,-1,-1,-1)}. \tag{3.4}
$$
The two source marks are
$$
T_0=I0_{D_-A_1[A]}A_1[B], \qquad T_2=I0_{A_1[A]}D_-A_1[B]. \tag{3.5}
$$
They do not exchange the ordered $A,B$ factors:
$$
(D_-K)^{[e_0]}K^{[e_2]} \longmapsto K^{[e_0]}(D_-K)^{[e_2]}. \tag{3.6}
$$
Therefore (3.3)--(3.4) is unchanged, while
$$
\boxed{T_0\mapsto e_0,\qquad T_2\mapsto e_2}. \tag{3.7}
$$
## 4. Complete representative noncommutative trace

Delta integration leaves
$$
\delta^4(\vartheta) D^2\bar D^2\delta^4(\vartheta) =16\delta^4(\vartheta). \tag{4.1}
$$
The remaining ordered word is
$$
\mathscr O^{\dot\alpha} =D_+(r_0)\bar D_{\dot\beta}(r_1) (ip)^{\dot\beta\gamma} D_\gamma(r_1)\bar D^{\dot\alpha}(r_2). \tag{4.2}
$$
For one edge, the locked flat-superspace algebra gives
$$
\{D_+(r_i),\bar D_{\dot\beta}(r_i)\}
=-2i(r_i)_{+\dot\beta}. \tag{4.3}
$$
$$
\sum_{i=0}^{1}\{D_+(r_i),\bar D_{\dot\beta}(r_i)\}
=-2iL_{1,+\dot\beta},\qquad
\sum_{j=1}^{2}\{D_\gamma(r_j),\bar D^{\dot\alpha}(r_j)\}
=-2iL_{2,\gamma}{}^{\dot\alpha}. \tag{4.4}
$$
After extracting the two explicit same-edge anticommutator factors, multiplication
of one normalized row in the original order gives every branch:
$$
\begin{aligned}
\mathscr O^{\dot\alpha}
={}&
\bar D_{\dot\beta}D_+
(ip)^{\dot\beta\gamma}
\bar D^{\dot\alpha}D_\gamma\\
&+i\bar D_{\dot\beta}D_+
(ip)^{\dot\beta\gamma}
L_{2,\gamma}{}^{\dot\alpha}\\
&+iL_{1,+\dot\beta}(ip)^{\dot\beta\gamma}
\bar D^{\dot\alpha}D_\gamma\\
&-L_{1,+\dot\beta}(ip)^{\dot\beta\gamma}
L_{2,\gamma}{}^{\dot\alpha}.
\end{aligned}
\tag{4.5}
$$
The first three lines are retained as longitudinal/contact or typed
$P\!\cdot D$ EOM words.  The last line is the derivative-free selected
parent.  Its sign $-1$ multiplies (3.4), giving the representative
numerator
$$
\boxed{ N_{T,+}{}^{\dot\alpha} =(r_0+r_1)_{+\dot\beta} (ip)^{\dot\beta\gamma} (r_1+r_2)_\gamma{}^{\dot\alpha}}. \tag{4.6}
$$
The residual external word is
$$
\boxed{D_{\dot\alpha}^D N_{T,+}{}^{\dot\alpha}A^E}. \tag{4.7}
$$
The closed $D$-weight is
$$
\boxed{\frac1{64}\times16\times2\times2=1}. \tag{4.8}
$$
The factors $2\times2$ are the common same-edge anticommutator
normalizations in (4.3), extracted before the endpoint sum.  The left rows
sum to $r_0+r_1=L_1$, and the right rows sum to $r_1+r_2=L_2$.
Each row has `raw_times_transport=-1`, while its selected branch is
$-4r_i(ip)r_j$; summing the four rows gives $4L_1(ip)L_2=4N_T$.
## 5. Canonical isolated directed result

The two vertices and three canonical propagators give
$$
\begin{aligned}
\mathfrak V_W\mathfrak V_{\widetilde W}
\langle uu\rangle^3
&=
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3\\
&=-\frac{\hbar g^2}{16}.
\end{aligned}
\tag{5.1}
$$
The closed source-loop odd integration-by-parts sign is
$$
s_{\rm odd\ IBP}=-1. \tag{5.2}
$$
Hence the fixed parent prefactor is
$$
\boxed{ \left(-\frac{\hbar g^2}{16}\right)(-1) =+\frac{\hbar g^2}{16}}. \tag{5.3}
$$
For the shifted UV momentum $L$,
$$
4\sigma\!\cdot\!L\,\bar\sigma\!\cdot\!p\,\sigma\!\cdot\!L =8(L\!\cdot\!p)\sigma\!\cdot\!L -4\bar L^2\sigma\!\cdot\!p. \tag{5.4}
$$
The first term is full-$d$ Schwinger exact.  Parent minus same-edge cut is
$$
-4\bar L^2\sigma\!\cdot\!p +4L_d^2\sigma\!\cdot\!p =-4\mu_L^2\sigma\!\cdot\!p. \tag{5.5}
$$
The exact integrals are
$$
2\int_{\Sigma_2}1=1, \qquad \int\frac{d^dL}{(2\pi)^d} \frac{\mu_L^2}{(L^2+\Delta)^3} =\frac1{32\pi^2}. \tag{5.6}
$$
Therefore
$$
\begin{aligned}
\Gamma_{G,\rm isolated\ directed}
&=\left(\frac{\hbar g^2}{16}\right)
(-4)\left(\frac1{32\pi^2}\right)\\
&=-\frac{\hbar g^2}{128\pi^2}
=\boxed{-\frac{\lambda_1}{8}}.
\end{aligned}
\tag{5.7}
$$
The rejected factor-eight chain was
$$
\left(\frac1{32}\right)(16)(2)(2)=2, \qquad \frac{\hbar g^2}{2}. \tag{5.8}
$$
Its verdict is REJECTED_FACTOR_8; it omitted
$(1/2)^3=1/8$ from the three vector lines.
## 6. Full 48-row generator

Rebuild/check command:
python3 scripts/build_step5k_ww_gauge_dword.py --check.
The exact full-Hessian partition is
$$
N_{\rm group} =2_{\chi}\times4_{\rm raw\ monomial} \times3_{\rm external\ placement}=24, \tag{6.1}
$$
$$
N_{\rm row}=24\times2_{SB,BS}=48. \tag{6.2}
$$
Each JSON row starts from
$$
c_\chi\operatorname{Tr} \left(W_\chi^{(1)}(X)[\mathscr D_\chi Y,Z]\right) ::(p,q,r,s), \tag{6.3}
$$
and records, in order,
$$
\begin{aligned}
{\rm POLARIZED\_SLOT\_TO\_ROLE}
&:\ (X,Y,Z)\mapsto(E,S,B),\\
{\rm KEEP\_SB}\ {\rm or}\ {\rm EVEN\_SWAP\_BS\_TO\_SB}
&:\ (S,B)\mapsto(S,B),\\
{\rm SOURCE\_ROLE\_TO\_MARKED\_EDGE}
&:\ S\mapsto
\begin{cases}e_0,&T_0,\\e_2,&T_2,\end{cases}\\
{\rm CLOSED\_GRASSMANN\_LOOP}
&:\ \Delta D^2\bar D^2\Delta\mapsto16\Delta,\\
{\rm GAUSSIAN\_SD\_SAME\_EDGE}
&:\ N_{d,\rho}\mapsto K_{{\rm raw},\rho}=-N_{d,\rho}.
\end{aligned}
\tag{6.4}
$$
Because both quantum endpoints are even,
$$
(-1)^{|u||u|}=+1 \tag{6.5}
$$
for the $BS\to SB$ ordering.  Every row terminates in
$$
N_{d,\rho}=L_\rho+Q_\rho r_{e,d}^{\,2}, \qquad K_{{\rm raw},\rho} =-L_\rho-Q_\rho r_{e,d}^{\,2}, \tag{6.6}
$$
$$
N_{d,\rho}+K_{{\rm raw},\rho}=0, \qquad N_{{\rm full},\rho}+K_{{\rm raw},\rho} =Q_\rho\mu_\ell^2. \tag{6.7}
$$
The JSON invariants are
$$
\boxed{ N_{\rm row}=48,\quad N_{\rm unique\ row}=48,\quad N_{\rm group}=24,\quad N_{\rm endpoint/group}=2,\quad N_{\rm mark}=2,\quad N_{\rm unresolved}=0}. \tag{6.8}
$$
## 7. Ghost typing and scope split

The ordered WW source has no FP or NK port.  The one-loop FP candidate is
one source-vector descendant joined to one cubic FP vertex, with a
same-vertex ghost edge:
$$
\langle u_{\rm source}u_{\rm FP}\rangle \langle C_{\rm FP}C'_{\rm FP}\rangle. \tag{7.1}
$$
It contains $\delta^{(d)}(Q)$.  On $Q=0$, its remaining DRED integral is
scaleless.  Hence
$$
\Gamma_{WW,\rm FP}^{(1)}=0. \tag{7.2}
$$
Two cubic FP vertices joined to both source ports have
$$
L=I-V+1=4-3+1=2, \tag{7.3}
$$
so they are two-loop.  FF gauge fixing is quadratic, and the D2 NK factor
is a field-independent normalized measure.  Thus
$$
\Gamma_{WW,\rm gauge\ fixing}^{(1)} =\Gamma_{WW,\rm NK}^{(1)}=0. \tag{7.4}
$$
Finally, the isolated graph and the full gauge orbit are distinct:
$$
\boxed{\Gamma_{G,\rm isolated\ directed}=-\frac{\lambda_1}{8}}, \tag{7.5}
$$
The 48 rows in Section 6 stop at the local parent/contact identities (6.7);
they do not contain a second action vertex, the three propagators, or an
integrated full-orbit coefficient.  The separately accepted target-blind
external-slot reconstruction
`audits/step5-aa-external-slot-decomposition-exact.json` has 269 exact
checks, 9216 color-mask rows, zero equality failure, and gives
$$
\frac{\Gamma_{WW,g}^{(1)}} {\lambda_1\mathbb F^{AB}{}_{DE}} =(i,2i,-i,-2i) \tag{7.6}
$$
in $(DA_p,DA_q,AD_p,AD_q)$.  The common Fourier map is $-i$, and
$$
DA_q=(P\!\cdot D)A, \qquad AD_q=A(P\!\cdot D) \tag{7.7}
$$
are EOM/divergence rows.  Therefore
$$
\boxed{ \Gamma_{WW,\rm full\ gauge\ orbit}^{(1),\rm phys} =\lambda_1\mathbb F^{AB}{}_{DE} \left[ D_{\dot\alpha}^DP^{\dot\alpha}A^E -(P_{\dot\alpha}A^D)D^{E\dot\alpha} \right]}. \tag{7.8}
$$
Equation (7.8) is not the value of the single integral (5.7).
It is also not derived by the 48-row generator; the Step-5K verifier reads
and checks the named accepted external-slot artifact separately.
