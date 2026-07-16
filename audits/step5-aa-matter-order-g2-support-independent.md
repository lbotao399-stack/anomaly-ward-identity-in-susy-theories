# Step 5 AA matter: complete order-$g^2$ source/resolvent support audit

Status:
`ORDER_G2_BARE_MATTER_SUPPORT_EXHAUSTED__FULL_SD_UNIT_MAGNITUDE__CONDITIONAL_MATCH_EXACT`.

Authority base:
`origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`.

Scope: target-blind enumeration of

$$
\mathcal I_2,
\qquad
\mathcal I_1S_{m3},
\qquad
\mathcal I_0S_{m4},
\qquad
\mathcal I_0S_{m3}S_{m3}
$$

in the ordered $AA\to B_rC_r$ matter channel.  The holomorphic-twist unit is
read only in Section 10, after the Project-side result is fixed.  The
$-\lambda _1/3$ second-mark row is derived from the full transported
Schwinger--Dyson orbit before that comparison.

## 1. Notation

Let

$$
d=4-2\epsilon,
\qquad
\lambda _1:=\frac{\hbar g^2}{16\pi^2},
\qquad
h:=g^{-2}.
$$

The three adjoint matter flavors are indexed by

$$
r,s\in\{1,2,3\}.
$$

For the triangle routing define

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q,
$$

$$
q=r_0-r_1,
\qquad
p=r_1-r_2.
$$

For the undotted rows $u_i$ of the momentum bispinors set

$$
W_{ij}:=u_i\wedge u_j.
$$

The DRED evanescent square is

$$
\mu_\ell^2:=\bar\ell^2-\ell_d^2.
$$

The common unresolved source-transpose orientation sign is

$$
\eta_{\mathrm{src}}\in\{+1,-1\}.
$$

It multiplies every directed triangle row and does not alter the support
census or any magnitude below.

## 2. Homogeneous source expansion

The exact exponential derivative is

$$
\Gamma_+
=\sum_{a,b\geq0}
\frac{(-1)^a}{a!b!(a+b+1)}
V^a(D_+V)V^b.
$$

The coefficients through three vector ports are

$$
a_{00}=1,
\qquad
a_{10}=-\frac12,
\qquad
a_{01}=\frac12,
$$

$$
a_{20}=\frac16,
\qquad
a_{11}=-\frac13,
\qquad
a_{02}=\frac16.
$$

Hence

$$
\Gamma_+^{[1]}=D_+V,
$$

$$
\Gamma_+^{[2]}
=-\frac12V(D_+V)+\frac12(D_+V)V,
$$

$$
\Gamma_+^{[3]}
=\frac16V^2(D_+V)
-\frac13V(D_+V)V
+\frac16(D_+V)V^2.
$$

The linear operations $-D_+\bar D^2/8$ and $D_-$ do not change the number of
vector ports.  The outer connection terms in

$$
\nabla_-=D_-+[\Gamma_-,\ \cdot\ ]
$$

add precisely the vector port carried by $\Gamma_-$.  Therefore the complete
homogeneous source insertions obey

$$
N_V(\mathcal I_0)=2,
\qquad
N_V(\mathcal I_1)=3,
\qquad
N_V(\mathcal I_2)=4.
$$

Writing $A=A_1+gA_2+g^2A_3+O(g^3)$, the product part is

$$
\mathcal I_0=D_-(A_1A_1),
$$

$$
\mathcal I_1
=D_-(A_1A_2+A_2A_1)
+[\gamma_1,A_1]A_1
+A_1[\gamma_1,A_1],
$$

$$
\begin{aligned}
\mathcal I_2={}&
D_-(A_1A_3+A_3A_1+A_2A_2)\\
&+[\gamma_1,A_2]A_1+A_2[\gamma_1,A_1]\\
&+[\gamma_1,A_1]A_2+A_1[\gamma_1,A_2]\\
&+[\gamma_2,A_1]A_1+A_1[\gamma_2,A_1].
\end{aligned}
$$

Every displayed monomial in $\mathcal I_j$ has exactly $j+2$ vector ports
and no matter port.

## 3. Matter action and resolvent coefficient

With $\eta_E=-1$, the matter action terms with one and two vector ports are

$$
S_{m3}
=-h\sum_{r=1}^3\int d^8z\,
\kappa_{DU}\widetilde\Phi_r^D V^A(T_A)^U{}_E\Phi_r^E,
$$

$$
S_{m4}
=-\frac h2\sum_{r=1}^3\int d^8z\,
\kappa_{DU}\widetilde\Phi_r^D
V^AV^B(T_AT_B)^U{}_E\Phi_r^E.
$$

Labeled differentiation of $S_{m4}$ gives

$$
\frac12(T_AT_B+T_BT_A).
$$

The connected order-$g^2$ matter coefficient is

$$
\boxed{
\begin{aligned}
\Gamma_{g^2,\mathrm{mat}}^{(1)}={}&
\langle\mathcal I_2\rangle_{BC}
-\frac1\hbar\langle\mathcal I_1S_{m3}\rangle_{0,c;BC}\\
&-\frac1\hbar\langle\mathcal I_0S_{m4}\rangle_{0,c;BC}
+\frac1{2\hbar^2}
\langle\mathcal I_0S_{m3}S_{m3}\rangle_{0,c;BC}.
\end{aligned}}
$$

Its port-complete topology census is

| resolvent term | source vector ports | action vector ports | one-loop support | result |
|---|---:|---:|---|---:|
| $\mathcal I_2$ | $4$ | $0$ | no $BC$ ports; all-quantum contraction is two-loop | $0$ |
| $\mathcal I_1S_{m3}$ | $3$ | $1$ | one bridge plus a source self-edge | $0$ |
| $\mathcal I_0S_{m4}$ | $2$ | $2$ | matter seagull/contact bubble | $0$ |
| $\mathcal I_0S_{m3}S_{m3}$ | $2$ | $1+1$ | directed matter triangle | nonzero parent |

The first three rows are nontriangle/contact rows.  The fourth row contains
all matter triangle parents.

## 4. Exact zero of $\mathcal I_2$

The desired external functional derivative is

$$
\frac{\delta^2}{\delta\widetilde\Phi_r^D(q)\,
\delta\Phi_s^E(p)}.
$$

Since $\mathcal I_2$ contains only vector fields,

$$
\frac{\delta^2\mathcal I_2}
{\delta\widetilde\Phi_r^D(q)\,
\delta\Phi_s^E(p)}=0.
$$

If all four vector ports at the single source insertion are paired, then

$$
V_{\mathrm{graph}}=1,
\qquad
E_{\mathrm{graph}}=2,
$$

$$
L=E_{\mathrm{graph}}-V_{\mathrm{graph}}+1
=2-1+1=2.
$$

Thus this contraction is neither a one-loop graph nor a $BC$ output:

$$
\boxed{
\left.\langle\mathcal I_2\rangle_{BC}
\right|_{\text{one loop}}=0.}
$$

## 5. Exact zero of $\mathcal I_1S_{m3}$

Keep the two matter ports of $S_{m3}$ external.  Label the three source
vector ports by $s_1,s_2,s_3$ and the action vector port by $a$.  The complete
perfect-matching set is

$$
\mathfrak P_1
=\{(a,s_1),(s_2,s_3)\},
$$

$$
\mathfrak P_2
=\{(a,s_2),(s_1,s_3)\},
$$

$$
\mathfrak P_3
=\{(a,s_3),(s_1,s_2)\}.
$$

Every matching contains one source-source self-edge.  The source-to-action
bridge carries the external total momentum $P=p+q$; the self-edge carries an
independent loop momentum $k$.  The loop factor has the form

$$
J[N]
=\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}\frac{N(k)}{k^2},
$$

where $N(k)$ is a polynomial produced by the $D$-algebra.  Odd tensor powers
vanish under $k\mapsto-k$.  Every even tensor integral reduces to a linear
combination of

$$
J_m
=\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}(k^2)^{m-1},
\qquad
m\in\mathbb Z_{\geq0}.
$$

Under $k\mapsto\rho k$,

$$
J_m
=\rho^{d+2m-2}J_m
=\rho^{2+2m-2\epsilon}J_m.
$$

For $m\geq0$ and $\epsilon$ in a punctured neighborhood of zero,

$$
2+2m-2\epsilon\neq0.
$$

Analytic dimensional regularization therefore gives

$$
J_m=0.
$$

There is no dimensionless logarithmic integral in this row.  Consequently

$$
\boxed{
\langle\mathcal I_1S_{m3}\rangle_{0,c;BC}=0.}
$$

This is the full-DRED scale-free value.  A separate UV/IR split of a power
tadpole is not an additional finite cutting-failure coefficient.

## 6. Exact zero of $\mathcal I_0S_{m4}$

The two occurrence-resolved collapsed-current $D$-words are

$$
\mathcal C_0^{\mathrm{raw}}=-1024W_{02},
\qquad
\mathcal C_2^{\mathrm{raw}}=+1024W_{02}.
$$

Let

$$
P:=p+q,
\qquad
r_0=k,
\qquad
r_2=k-P.
$$

Feynman parameterization and the shift $L=k-xP$ give

$$
r_0=L+xP,
\qquad
r_2=L-(1-x)P.
$$

The numerator expands exactly as

$$
\begin{aligned}
W_{02}
&=(L_++xP_+)\wedge(L_+-(1-x)P_+)\\
&=L_+\wedge L_+
-(1-x)L_+\wedge P_+
+xP_+\wedge L_+
-x(1-x)P_+\wedge P_+\\
&=-(1-x)L_+\wedge P_+
-xL_+\wedge P_+\\
&=-L_+\wedge P_+.
\end{aligned}
$$

The shifted denominator is even in $L$.  Hence

$$
\int\frac{d^dL}{(2\pi)^d}
\frac{L_{+\alpha}}
{[L^2+x(1-x)P^2]^2}=0,
$$

and the same parity identity holds after multiplication by $\mu_L^2$.
Therefore each marked seagull row vanishes before color summation.

The independent ordered-color cancellation is

| source placement | $T_AT_B$ | $T_BT_A$ |
|---|---:|---:|
| first marked placement | $-1$ | $+1$ |
| second marked placement | $+1$ | $-1$ |

Thus

$$
-T_AT_B+T_BT_A+T_AT_B-T_BT_A=0.
$$

Both arguments give

$$
\boxed{
\langle\mathcal I_0S_{m4}\rangle_{0,c;BC}=0.}
$$

## 7. Exhaustion of $\mathcal I_0S_{m3}S_{m3}$

The matter propagator is flavor diagonal:

$$
\langle\Phi_r\widetilde\Phi_s\rangle_0
=\delta_{rs}G_{\Phi\widetilde\Phi}.
$$

Therefore $r\neq s$ has zero support.  For each fixed $r$ there are exactly
two directed external port orders,

$$
M_{r,\rightarrow}:
\Phi_r\longrightarrow\widetilde\Phi_r,
\qquad
M_{r,\leftarrow}:
\widetilde\Phi_r\longrightarrow\Phi_r.
$$

Each directed parent has two marked source-$A$ endpoints.  Hence

$$
N_{\mathrm{parent}}
=3\times2=6,
$$

$$
N_{\mathrm{marked}}
=3\times2\times2=12.
$$

For one local orientation, the two occurrence-tagged DRED defects are

$$
D_i:=r_{i,d}^2,
\qquad
\bar r_i^2=D_i+\mu_\ell^2.
$$

If the $D$-algebra supplied the full inverse kernel, the parent and its
Schwinger cut would cancel pointwise:

$$
\frac{D_i}{D_i\prod_{j\neq i}D_j}
-\frac1{\prod_{j\neq i}D_j}=0.
$$

The four-dimensional $D$-algebra square instead leaves

$$
\frac{\bar r_i^2}{D_i\prod_{j\neq i}D_j}
-\frac1{\prod_{j\neq i}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

The first marked defect and the full transported second marked defect are

$$
\Delta_0
=\mu_\ell^2(W_{12}-W_{02}),
$$

$$
\Delta_2^{\mathrm{full}}
\longmapsto
\left(\frac12-z\right)
\mu_\ell^2(p_+\wedge q_+)
$$

in the raw \(-\mathcal S_1,-\mathcal S_2\) orientation.  The second line
contains the primary/current truncation

$$
(y-z)\mu_\ell^2(p_+\wedge q_+)
$$

and the transported longitudinal residue

$$
\left(\frac12-y\right)\mu_\ell^2(p_+\wedge q_+).
$$

With

$$
\frac1{D_0D_1D_2}
=2\int_{x,y,z\geq0}dx\,dy\,dz\,
\delta(1-x-y-z)
\frac1{(L^2+\Delta)^3},
$$

the even wedge parts are

$$
W_{01}\longmapsto-z(p_+\wedge q_+),
$$

$$
W_{02}\longmapsto+y(p_+\wedge q_+),
$$

$$
W_{12}\longmapsto-x(p_+\wedge q_+).
$$

The exact simplex moments are

$$
2\int_{\Sigma_2}x
=2\int_{\Sigma_2}y
=2\int_{\Sigma_2}z
=\frac13.
$$

The evanescent master is

$$
\lim_{\epsilon\to0}
\mu^{2\epsilon}
\int\frac{d^dL}{(2\pi)^d}
\frac{\mu_L^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

Using the primitive normalization derived in Section 8, the first marked
endpoint gives

$$
\begin{aligned}
c_0
&=4\hbar g^2
\left[-2\int_{\Sigma_2}(x+y)\right]
\frac1{32\pi^2}\\
&=4\hbar g^2
\left[-\frac23\right]
\frac1{32\pi^2}\\
&=-\frac{\hbar g^2}{12\pi^2}\\
&=-\frac43\lambda_1.
\end{aligned}
$$

The second marked endpoint gives

$$
\begin{aligned}
c_2
&=4\hbar g^2
\left[
2\int_{\Sigma_2}\left(\frac12-z\right)
\right]
\frac1{32\pi^2}\\
&=4\hbar g^2
\left(\frac16\right)
\frac1{32\pi^2}\\
&=\frac{\hbar g^2}{48\pi^2}\\
&=\frac13\lambda_1.
\end{aligned}
$$

Thus every directed parent has two nonzero marked endpoints:

$$
N_{\mathrm{nonzero\ marked}}=12,
\qquad
N_{\mathrm{zero\ marked}}=0.
$$

For each fixed flavor $r$, the two directed rows are

$$
\boxed{
\begin{array}{c|c|c}
\text{parent}&\text{first marked endpoint}&\text{second marked endpoint}\\ \hline
M_{r,\rightarrow}
&-\eta_{\mathrm{src}}\dfrac43\lambda_1
\mathbb F^{AB}{}_{DE}(p_+\wedge q_+)
&+\eta_{\mathrm{src}}\dfrac13\lambda_1
\mathbb F^{AB}{}_{DE}(p_+\wedge q_+)\\[2mm]
M_{r,\leftarrow}
&-\eta_{\mathrm{src}}\dfrac43\lambda_1
\mathbb F^{AB}{}_{ED}(q_+\wedge p_+)
&+\eta_{\mathrm{src}}\dfrac13\lambda_1
\mathbb F^{AB}{}_{ED}(q_+\wedge p_+)
\end{array}}
$$

For either directed row,

$$
-\frac43\lambda_1+\frac13\lambda_1=-\lambda_1.
$$

The three values of $r$ are three typed output rows.  They do not multiply a
fixed-flavor coefficient by $3$.

## 8. Primitive triangle normalization

The order-two action exponential and the two assignments of the labeled
copies of $S_{m3}$ give

$$
w_{\mathrm{exp+Wick}}
=\frac1{2!}(2)=1.
$$

Including the powers of $\hbar$ and the two cubic matter vertices,

$$
\frac1{2!\hbar^2}(-h)^2(2)
=\frac{h^2}{\hbar^2}.
$$

The two vector propagator factors and the matter propagator with its chiral
projector are

$$
(-2\hbar g^2)^2,
\qquad
\frac{\hbar g^2}{16}.
$$

Therefore

$$
\begin{aligned}
N_{\mathrm{primitive}}^{(P_\chi\ \mathrm{in\ propagator})}
&=\frac{h^2}{\hbar^2}
(-2\hbar g^2)^2
\left(\frac{\hbar g^2}{16}\right)\\
&=\frac{g^{-4}}{\hbar^2}
(4\hbar^2g^4)
\left(\frac{\hbar g^2}{16}\right)\\
&=\frac{\hbar g^2}{4}.
\end{aligned}
$$

The two source factors, two Berezin-measure conversions, and the raw finite
Grassmann word give

$$
\left(-\frac18\right)^2
\left(-\frac14\right)^2
(16384)
=\frac{16384}{64\cdot16}
=16.
$$

Hence

$$
\boxed{
N_{\mathrm{triangle}}
=\frac{\hbar g^2}{4}(16)
=4\hbar g^2.}
$$

Move the projector factor $1/16$ from the matter propagator to the finite
$D$-word.  Then

$$
\begin{aligned}
N_{\mathrm{primitive}}^{(P_\chi\ \mathrm{in\ }D\mathrm{-word})}
&=\frac{h^2}{\hbar^2}
(-2\hbar g^2)^2(\hbar g^2)\\
&=4\hbar g^2,
\end{aligned}
$$

$$
\frac{16384}{64\cdot16\cdot16}=1,
$$

$$
N_{\mathrm{triangle}}
=(4\hbar g^2)(1)
=4\hbar g^2.
$$

The two partitions agree exactly.  There is no second projector factor.

The graph automorphism group is trivial after retaining the ordered source
letters, the marked $D_-$ endpoint, the chiral orientation of the matter
edge, and the two external endpoints:

$$
|\operatorname{Aut}(M_{r,\rightarrow})|
=|\operatorname{Aut}(M_{r,\leftarrow})|
=1.
$$

For one typed output $r$,

$$
\delta_{rr}=1.
$$

The two ordered color chains are

$$
\begin{aligned}
(T_A)^D{}_X(T_B)^X{}_E
&=(ic_{AX}{}^D)(ic_{BE}{}^X)\\
&=-c_{AX}{}^Dc_{BE}{}^X\\
&=c_{AX}{}^Dc_{BX}{}^E\\
&=\mathbb F^{AB}{}_{DE},
\end{aligned}
$$

$$
(T_B)^D{}_X(T_A)^X{}_E
=\mathbb F^{AB}{}_{ED}.
$$

Neither chain supplies a numerical factor.

The source coordinate is $L=g^{-1}A$.  Returning to the physical ordered
operator gives

$$
g^2L^AL^B
=g^2(g^{-1}A^A)(g^{-1}A^B)
=A^AA^B.
$$

Thus the source round trip also supplies no numerical factor.  In particular,
the complete numerical multipliers supplied by

$$
w_{\mathrm{exp+Wick}},
\quad
|\operatorname{Aut}|^{-1},
\quad
\delta_{rr},
\quad
\text{color orientation},
\quad
L\leftrightarrow A,
\quad
P_\chi\text{ placement}
$$

are all $1$.

## 9. Target-blind Project result

The four resolvent sectors give

$$
\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}\right|_{\mathcal I_2}=0,
$$

$$
\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}\right|_{\mathcal I_1S_{m3}}=0,
$$

$$
\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}\right|_{\mathcal I_0S_{m4}}=0,
$$

$$
\left|
\left.\Gamma_{g^2,\mathrm{mat}}^{(1)}
\right|_{\mathcal I_0S_{m3}S_{m3}}
\right|
=\lambda_1
$$

per fixed directed flavor output.  Hence

$$
\boxed{
\left|c_{AA\to B_rC_r}^{\mathrm{bare,mat}}\right|
=1.}
$$

The second-mark row is derived from the transported longitudinal word:

$$
D_{0+}\bar D_0^2D_0^2\delta^4_{02}
=-D_2^2\bar D_2^2D_{2+}\delta^4_{02},
$$

$$
D^2\bar D^2D^2=-16(\det r_1)D^2.
$$

Its coefficient is \(+\lambda_1/3\) in the raw orientation and
\(-\lambda_1/3\) in the opposite orientation.

## 10. Conditional holomorphic-twist after-check

Only now assume, as an external conditional after-check, the comparison value
for the same normalized directed row,

$$
\left|c_{AA\to B_rC_r}^{\mathrm{HT,conditional}}\right|=1.
$$

Then

$$
\begin{aligned}
\left|c_{AA\to B_rC_r}^{\mathrm{bare,mat}}\right|
-\left|c_{AA\to B_rC_r}^{\mathrm{HT,conditional}}\right|
&=1-1\\
&=0.
\end{aligned}
$$

The equality is an after-check only; no coefficient was imported from the
conditional target into the Project-side calculation.

## 11. Gap verdicts

| id | type | priority | claim | exact check | verdict |
|---|---|---:|---|---|---|
| AA-MG2-G1 | G-SCOPE | P0 | the four triangle rows alone exhaust all flavors and directions | $3$ flavors $\times$ $2$ directed ports $\times$ $2$ marks $=12$ occurrences | repaired |
| AA-MG2-G2 | G-OP | P0 | only inverse kernels tagged before transport enter the SD orbit | graded endpoint transport plus \(D^2\bar D^2D^2=-16(\det r_1)D^2\) | rejected |
| AA-MG2-G3 | G-NORM | P0 | a hidden normalization changes $4/3$ to $1$ | the new \(-1/3\) row comes from the explicit longitudinal residue, while every normalization factor remains fixed | rejected |
| AA-MG2-G4 | G-SCOPE | P1 | $\mathcal I_1S_{m3}$ contains a finite anomaly row | every matching contains a scale-free one-propagator tadpole and no logarithmic degree | rejected |
| AA-MG2-G5 | G-ALG | P1 | $\mathcal I_0S_{m4}$ leaves an even bubble numerator | $W_{02}=-L_+\wedge P_+$ after the exact shift | rejected |
| AA-MG2-G6 | G-SCOPE | P0 | the conditional target determines the bare coefficient | target is read only after the Project-side support sum | rejected |

Verification command used:

    /Users/libotao/MinerU/.venv/bin/python3 scripts/step5_aa_matter_order_g2_support_independent_audit.py

Expected result:

    68/68 PASS
