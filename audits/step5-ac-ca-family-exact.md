# Step 5 ordered $A>C_r$ and $C_r>A$ anomaly sector

Status: `TARGET_BLIND_COMPLETE_ORDER_G2_ORBIT__HT_UNIT_MATCH`.

No holomorphic-twist coefficient enters Sections 1--7.

## 1. Definitions

$$
A_c=A_1+gA_2+g^2A_3,
\qquad
C_r=\widetilde\Phi_r,
$$

$$
N_0=D_-A_1,
$$

$$
N_1=D_-A_2+[\gamma_1,A_1],
$$

$$
N_2=D_-A_3+[\gamma_1,A_2]+[\gamma_2,A_1].
$$

The connected order-$g^2$ orbit is

$$
\Gamma_{g^2}^{(1)}
=\langle I_2\rangle_0
-\frac1\hbar\langle I_1S_3\rangle_{0,c}
-\frac1\hbar\langle I_0S_4\rangle_{0,c}
+\frac1{2\hbar^2}\langle I_0S_3S_3\rangle_{0,c}.
$$

Define

$$
d=4-2\epsilon,
\qquad
J_2:=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell_d^2}{(\ell_d^2+\Delta)^3},
$$

$$
\mu_\ell^2:=\bar\ell^2-\ell_d^2,
\qquad
J_{\mu^2}:=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}.
$$

Rotational reduction in $d$ dimensions gives

$$
\int\bar\ell^2 f(\ell_d^2)
=\frac4d\int\ell_d^2f(\ell_d^2),
$$

and therefore

$$
\boxed{J_{\mu^2}=\frac{4-d}{d}J_2=\frac1{32\pi^2}.}
$$

## 2. Exact color contraction

Use $T_A=\sigma_A/2$, $\operatorname{tr}(T_AT_B)=\delta_{AB}/2$.
For the frame

$$
(A,B,D,E)=(0,1,1,0),
$$

the two matter vertices, two matter inverse metrics, and the complete vector
covariance give

$$
\begin{aligned}
C_{\rm full}
&=(-2)(2)(2)
\sum_{X=0}^2
\operatorname{tr}\!\left(T_D[T_A,T_X]\right)
\operatorname{tr}\!\left(T_X[T_E,T_B]\right)
\\
&=-8\left(\frac{i}{2}\right)^2
\sum_X\varepsilon_{AXD}\varepsilon_{EBX}
\\
&=-2.
\end{aligned}
$$

The Project tensor in the same frame is

$$
\mathbb F^{01}{}_{10}
=2\sum_X\varepsilon_{0X1}\varepsilon_{1X0}
=-2.
$$

Hence

$$
\boxed{C_{\rm full}=+\mathbb F^{AB}{}_{DE}.}
$$

The old sign line separated the vector-covariance minus from the same color
word and then used it a second time.  The full covariance contraction above
is the sign used below.

## 3. Exact nonlinear $D$-words

Set

$$
z(k):=k_0-ik_1.
$$

The finite-Grassmann replay gives, for $A>C_r$,

$$
\left.I_1S_{m3}\right|_{A_2M_1,D>C}
=-8z(k),
$$

$$
\left.I_0S_{m4}\right|_{A_1M_2,D>C}
=+8\sqrt2\,z(k),
$$

$$
\left.I_0S_{m4}\right|_{A_1M_2,C>D}
=-16\sqrt2\,z(k).
$$

At the exact validation momentum $k=(2,-1,1,3)$,

$$
z(k)=2+i,
$$

$$
(-8z,8\sqrt2z,-16\sqrt2z)
=(-16-8i,16\sqrt2+8i\sqrt2,-32\sqrt2-16i\sqrt2).
$$

Swapping the source slots and replaying $C_r>A$ gives the same three
polynomials in the reversed ports.  No reflected coefficient is assumed.

The quartic word is obtained by differentiating

$$
[U,[U,\Phi]]
=U^2\Phi-2U\Phi U+\Phi U^2
$$

with respect to one internal and one external $U$.  Thus both ordered $U$
placements occur inside one seagull vertex; they are not two Feynman graphs.

## 4. $TMM$ metric orbit

The three-denominator triangle has the normalized metric pole

$$
\Gamma_{TMM}^{\triangle}\big|_{J_2}
=-\frac8dJ_2.
$$

The complete $I_0S_{m4}$ seagull gives

$$
\Gamma_{TMM}^{I_0S_{m4}}\big|_{J_2}
=+2J_2.
$$

Their four-dimensional pole cancels exactly:

$$
\left(-\frac84+2\right)J_2=0.
$$

In DRED,

$$
\begin{aligned}
\Gamma_{TMM}^{\rm DRED}\big|_{\rm local}
&=\left(2-\frac8d\right)J_2
\\
&=\frac{2d-8}{d}J_2
\\
&=-2\frac{4-d}{d}J_2
\\
&=-2J_{\mu^2}.
\end{aligned}
$$

Therefore

$$
\hbar g^2(-2)J_{\mu^2}
=-\frac{\hbar g^2}{16\pi^2}
=-\lambda_1.
$$

Thus $TMM$ contributes

$$
\boxed{c_{TMM}=-1.}
$$

## 5. $TGM$ metric orbit

The six gauge--matter triangle routes have total metric pole

$$
\Gamma_{TGM}^{\triangle}\big|_{J_2}
=+\frac8dJ_2.
$$

The nonlinear-source bubble and the matter seagull give separately

$$
\Gamma_{TGM}^{I_1S_{m3}}\big|_{J_2}=-J_2,
$$

$$
\Gamma_{TGM}^{I_0S_{m4}}\big|_{J_2}=-J_2.
$$

At $d=4$,

$$
\left(\frac84-1-1\right)J_2=0.
$$

In DRED,

$$
\begin{aligned}
\Gamma_{TGM}^{\rm DRED}\big|_{\rm local}
&=\left(\frac8d-2\right)J_2
\\
&=\frac{8-2d}{d}J_2
\\
&=+2\frac{4-d}{d}J_2
\\
&=+2J_{\mu^2}.
\end{aligned}
$$

Therefore

$$
\hbar g^2(+2)J_{\mu^2}
=+\frac{\hbar g^2}{16\pi^2}
=+\lambda_1,
$$

and

$$
\boxed{c_{TGM}=+1.}
$$

## 6. Remaining order-$g^2$ rows

The $A_3$ source term has one massless coincident vector tadpole:

$$
\langle I_2\rangle_0
\supset
\int\frac{d^dk}{(2\pi)^d}\frac{(k^2)^n}{k^2}=0.
$$

Both typed superpotential routes have exact projected polynomial zero:

$$
T_{MH}^{(1)}=T_{MH}^{(2)}=0.
$$

The gauge, gauge-fixing, FP, and NK rows have zero
$\mathbb F$-sector metric trace.  They contain no $J_{\mu^2}$ remainder.

The Euler-current and explicit-current occurrences remain separate until
their ports, denominators, and edge tags are matched:

$$
\begin{array}{c|c|c|c}
\text{row}&\text{coefficient}&\text{denominator}&\text{selected square}\\ \hline
E_{\rm cur}&+2i&D_0D_1&\varnothing\\
X_{\rm cur}&-2i&D_0D_1&\varnothing
\end{array}
$$

Hence

$$
(+2i-2i)K_{\rm cur}(k)=0.
$$

This zero does not produce the factor $1/2$.

## 7. First invalid line and ordered result

The old replay replaced both transported inverse-square rows independently:

$$
\bar r_0^2-r_{0,d}^2=\mu_\ell^2,
\qquad
\bar r_1^2-r_{1,d}^2=\mu_\ell^2,
$$

and promoted both rows to independent nonlinear descendants.  The exact
$I_1S_3+I_0S_4$ replay shows that these are two decompositions of one metric
pole orbit.  Consequently

$$
\left|\Gamma_{\rm old}\right|=4J_{\mu^2},
\qquad
\left|\Gamma_{\rm complete}\right|=2J_{\mu^2}.
$$

The first invalid classification is therefore

$$
\boxed{\texttt{OCCURRENCE_DECOMPOSITION_DOUBLE_COUNT}.}
$$

In the ordered basis

$$
\left((P_{\dot a}C_r)^D D^{E\dot a},
D_{\dot a}^D(P^{\dot a}C_r)^E\right),
$$

the independent results are

$$
\boxed{\mathbf c_{A>C_r}=(-1,+1),}
$$

$$
\boxed{\mathbf c_{C_r>A}=(-1,+1).}
$$

Equivalently,

$$
\boxed{
\Delta(A,C_r)=\Delta(C_r,A)
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
D_{\dot a}^D(P^{\dot a}C_r)^E
-(P_{\dot a}C_r)^D D^{E\dot a}
\right].}
$$

## 8. Holomorphic-twist after-check

Only now read the compact zero-shift row.  It gives

$$
\mathbf c_{\rm HT}=(-1,+1).
$$

Therefore

$$
\boxed{\mathbf c_{A>C_r}=\mathbf c_{C_r>A}=\mathbf c_{\rm HT}.}
$$
