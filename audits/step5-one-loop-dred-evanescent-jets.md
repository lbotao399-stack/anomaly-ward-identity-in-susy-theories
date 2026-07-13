# Step 5 Project-5A DRED evanescent local jets

## 0. Status

$$
\boxed{
\mathsf{M}_{\rm DRED\_EVANESCENT\_JETS}
=\texttt{FAIL\_EXPLICIT\_FULL\_DRED\_QUADRATIC\_JET\_KERNEL}
}
$$

$$
\boxed{
0\ne\mathscr E\in
\ker\!\left(\ell_2\big|_{\mathcal V^{J^1}_{\rm DRED,raw}}\right),
\qquad
q_{4d}(\mathscr E)=0.
}
$$

$$
N_{\tau,{\rm raw}}=229,
\qquad
N_{\tau,N=3}=1,
\qquad
\operatorname{rank}\mathcal M_{\tau,{\rm EOM/IBP/BV}}
=\texttt{BLOCKED}.
$$

No loop or anomaly coefficient is computed.

## 1. Typed carrier

$$
[\mathscr O]=\frac92,
\qquad
(j_L,j_R)=\left(\frac32,0\right),
\qquad
|\mathscr O|=1,
\qquad
r_{\rm f}(\mathscr O)=-1.
$$

The Project $U(1)_R$ certificate fixes

$$
r_{\rm P}(W,\widetilde W,\nabla,\bar\nabla,\mathcal D)
=(+1,-1,-1,+1,0),
$$

so $r_{\rm f}=r_{\rm P}$ on this complete pure-gauge letter set.

$$
J_{(AB)}=J_{(BA)},
\qquad |J|=1,
\qquad |J\mathscr O|=0.
$$

The source has no Lorentz index.  Its exact ordered projector is

$$
P_{\rm Sym^2}
=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
P_{\rm Sym^2}^2=P_{\rm Sym^2},
\qquad
\operatorname{rank}P_{\rm Sym^2}=1.
$$

The raw Project letter census gives

$$
N_{\rm skeleton}=18,
\qquad
(N_0,N_1,N_2,N_3)=(40,20,6,0),
\qquad
N_{(3/2,0)}=66.
$$

All counts are per symbolic generator of $\operatorname{Sym}^2(\mathrm{Adj})$.

## 2. Scalar and traceless metric channels

$$
\delta_{(4)}^{mn}
=\widehat\delta^{mn}+\widetilde\delta^{mn},
\qquad
\widehat\delta\widetilde\delta=0,
\qquad
\operatorname{tr}\widetilde\delta=2\epsilon.
$$

Define

$$
\tau^{mn}
:=\widetilde\delta^{mn}
-\frac{\epsilon}{2}\delta_{(4)}^{mn}.
$$

Then

$$
\delta_{(4)mn}\tau^{mn}
=2\epsilon-\frac{\epsilon}{2}4=0,
$$

$$
\widetilde\delta^{mn}
=\frac{\epsilon}{2}\delta_{(4)}^{mn}+\tau^{mn},
\qquad
\tau\in(1,1).
$$

Using $\widetilde\delta^2=\widetilde\delta$,

$$
\begin{aligned}
\tau_{mn}\tau^{mn}
&=\widetilde\delta_{mn}\widetilde\delta^{mn}
-\epsilon\widetilde\delta_m{}^m
+\frac{\epsilon^2}{4}\delta_{(4)m}{}^m\\
&=2\epsilon-2\epsilon^2+\epsilon^2\\
&=2\epsilon-\epsilon^2.
\end{aligned}
$$

If $\tau=\epsilon X$ for a regular tensor $X$ over
$R=\mathbb Q[\epsilon]$, then
$\tau_{mn}\tau^{mn}\in(\epsilon^2)R$.  But

$$
2\epsilon-\epsilon^2\notin(\epsilon^2)R.
$$

Therefore $\tau$ is an independent evanescent tensor generator; it is not an
$\epsilon$ coefficient multiplying $\delta_{(4)}$.

## 3. External-momentum channel

Every external derivative momentum obeys

$$
v^m=\widehat\delta^m{}_nv^n.
$$

Hence the full insertion vanishes:

$$
\widetilde\delta^m{}_nv^n
=\widetilde\delta^m{}_n\widehat\delta^n{}_rv^r
=0.
$$

The split pieces cancel:

$$
\tau^m{}_nv^n=-\frac{\epsilon}{2}v^m,
\qquad
\frac{\epsilon}{2}\delta_{(4)}^m{}_nv^n
=+\frac{\epsilon}{2}v^m.
$$

Thus external support removes only the channel in which at least one
$\widetilde\delta$ endpoint reaches an external derivative momentum.

## 4. Closed sigma channels

$$
\begin{aligned}
\widetilde\delta_{mn}
(\sigma_E^m\bar\sigma_E^n)
&=2\epsilon\,\mathbf1_L,\\
\widetilde\delta_{mn}
(\bar\sigma_E^m\sigma_E^n)
&=2\epsilon\,\mathbf1_R,\\
\widetilde\delta_{mn}
(\sigma_E^m)_{a\dot a}(\sigma_E^n)_b{}^{\dot a}
&=-2\epsilon\,\epsilon_{ab},\\
\widetilde\delta_{mn}
(\bar\sigma_E^m)^{\dot a a}
(\bar\sigma_E^n)^{\dot b}{}_a
&=-2\epsilon\,\epsilon^{\dot a\dot b}.
\end{aligned}
$$

The executable component check evaluates $4\times64=256$ exact entries.

$$
\widetilde\delta_{mn}\sigma_E^{mn}=0,
\qquad
\widetilde\delta_{mn}\bar\sigma_E^{mn}=0.
$$

These equations classify the closed trace and antisymmetric channels.  They do
not remove the open symmetric-traceless bispinor

$$
\tau_{ab\dot a\dot b}
:=\tau_{mn}
(\sigma_E^m)_{(a(\dot a}
(\sigma_E^n)_{b)\dot b)},
\qquad
\tau_{ab\dot a\dot b}\in(1,1).
$$

The complete single-insertion channel partition is

$$
\begin{array}{c|c}
\text{channel}&\text{result}\\ \hline
\text{external hatted momentum}&0\\
\text{closed scalar sigma trace}&2\epsilon\times\text{existing jet}\\
\text{closed antisymmetric sigma}&0\\
\text{open symmetric-traceless sigma}&\tau\text{ target candidate}\\
\text{free vector endpoint}&\text{wrong target type}
\end{array}
$$

## 5. Exact traceless-spurion multiplicity census

For a skeleton with $L$ left and $R$ right fundamental spinor slots, let
$m_L(j)$ and $m_R(j)$ be the exact $SU(2)$ tensor-product multiplicities.
Since

$$
\frac12\otimes1\supset\frac32,
\qquad
\frac32\otimes1\supset\frac32,
\qquad
\frac52\otimes1\supset\frac32,
\qquad
1\otimes1\supset0,
$$

the raw multiplicity is

$$
m_\tau
=m_R(1)
\left[m_L\left(\frac12\right)
+m_L\left(\frac32\right)
+m_L\left(\frac52\right)\right].
$$

The complete 18-skeleton census gives

$$
\begin{array}{c|rrrr|r}
N&0&1&2&3&\text{total}\\ \hline
m_{\rm physical}&40&20&6&0&66\\
m_\tau&150&66&12&1&229
\end{array}
$$

Three independent decomposition checks are

$$
\begin{aligned}
(L,R)=(5,4):\quad
m_\tau&=3(5+4+1)=30,\\
(L,R)=(3,2):\quad
m_\tau&=1(2+1+0)=3,\\
(L,R)=(1,2):\quad
m_\tau&=1(1+0+0)=1.
\end{aligned}
$$

The representation multiplicity is exhaustive.  The 229 explicit open-index
placement projectors and their EOM/IBP/BV relations are not built.

## 6. Explicit full-DRED quadratic-jet kernel

For $N=3$, the only skeleton is

$$
W\widetilde W\widetilde W,
\qquad
n_{\mathcal D}=0.
$$

Its physical target multiplicity is zero, while its $\tau$-extended target
multiplicity is one.  In Project notation define

$$
\mathscr E_{abc}^{AB}
:=
K^{AB}{}_{C[DE]}
\tau_{(ab|\dot c\dot d|}
W_{c)}^C
\widetilde W^{D\dot c}
\widetilde W^{E\dot d}.
$$

$$
K^{AB}{}_{C[DE]}
:=\delta^A{}_C c_{DE}{}^B
+\delta^B{}_C c_{DE}{}^A,
\qquad
K^{AB}{}_{C[DE]}=K^{BA}{}_{C[DE]},
\qquad
K^{AB}{}_{C[ED]}=-K^{AB}{}_{C[DE]}.
$$

For the exact $SU(2)$ adjoint realization

$$
\kappa_{AB}=\delta_{AB},
\qquad
c_{ABC}=\varepsilon_{ABC},
$$

the exhaustive component sum gives

$$
\begin{aligned}
0={}&c_{XA}{}^F K_{FB;CDE}
+c_{XB}{}^F K_{AF;CDE}
+c_{XC}{}^F K_{AB;FDE}\\
&+c_{XD}{}^F K_{AB;CFE}
+c_{XE}{}^F K_{AB;CDF},
\end{aligned}
$$

$$
\#\left\{(X,A,B,C,D,E)\right\}=3^6=729,
\qquad
\max|\delta_XK|=0,
$$

$$
\#\left\{(A,B,C,D,E):K^{AB}{}_{CDE}\ne0\right\}=30,
\qquad
K^{00}{}_{0[12]}=2.
$$

Thus $K$ is nonzero and adjoint-equivariant.

Set

$$
B^{DE}
:=\tau_{\dot c\dot d}
\widetilde W^{D\dot c}
\widetilde W^{E\dot d}.
$$

The exact Grassmann exchange is

$$
\begin{aligned}
B^{ED}
&=\tau_{\dot c\dot d}
\widetilde W^{E\dot c}
\widetilde W^{D\dot d}\\
&=-\tau_{\dot c\dot d}
\widetilde W^{D\dot d}
\widetilde W^{E\dot c}\\
&=-\tau_{\dot d\dot c}
\widetilde W^{D\dot c}
\widetilde W^{E\dot d}\\
&=-B^{DE}.
\end{aligned}
$$

Therefore

$$
K^{AB}{}_{C[ED]}B^{ED}
=(-1)(-1)K^{AB}{}_{C[DE]}B^{DE}
=K^{AB}{}_{C[DE]}B^{DE}\ne0.
$$

For the displayed $SU(2)$ component,

$$
K^{00}{}_{0[DE]}B^{DE}
=2B^{12}+(-2)B^{21}
=2B^{12}+2B^{12}
=4B^{12}\ne0.
$$

Direct counting gives

$$
[\mathscr E]=3\left(\frac32\right)=\frac92,
\qquad
r_{\rm f}(\mathscr E)=1-1-1=-1,
\qquad
|\mathscr E|=1+1+1=1\pmod2.
$$

There is no external momentum on which $\widetilde\delta$ can vanish.  Each
field strength has minimum background-connection degree one.  Hence

$$
\mathscr E(t\mathcal B)=t^3\mathscr E_{(3)}(\mathcal B)
+\sum_{n\ge4}t^n\mathscr E_{(n)}(\mathcal B),
$$

$$
\ell_2(\mathscr E)
:=\frac12\left.\frac{d^2}{dt^2}\right|_{t=0}
\mathscr E(t\mathcal B)=0,
\qquad
\left.\frac{d^3}{dt^3}\right|_{t=0}t^3=6.
$$

Thus

$$
0\ne\mathscr E\in
\ker\!\left(\ell_2\big|_{\mathcal V^{J^1}_{\rm DRED,raw}}\right).
$$

The adjoint-equivariance of $K$ places the same witness in the
background-CE-covariant submodule.  Therefore injectivity fails in both raw
modules.

The physical-$4d$ quotient is different:

$$
q_{4d}(\tau)=0,
\qquad
q_{4d}(\mathscr E)=0.
$$

This witness does not refute injectivity after $q_{4d}$.  Its class after
EOM/IBP and in the full quantum BV complex remains open.

## 7. Certified contracted subledger

$$
\begin{array}{c|r}
\text{class}&\text{rows}\\ \hline
\text{closed sigma masters}&264\\
\text{closed antisymmetric sigma}&132\\
\text{one external endpoint}&420\\
\text{two external endpoints}&92\\ \hline
\text{total}&908
\end{array}
$$

The 908 rows exhaust only external-support, closed-trace, and antisymmetric
placements.  They do not contain the open $\tau$ sector.

The corresponding sparse presentation is

$$
M_{\rm contracted}
\in\operatorname{Mat}_{710\times776}(R),
\qquad
\operatorname{rank}_R M_{\rm contracted}=710.
$$

It proves no new direction in that contracted submodule only.

## 8. Multiple insertions

For every integer $n\ge1$,

$$
(\widetilde\delta^n)^m{}_n
=\widetilde\delta^m{}_n,
\qquad
\operatorname{tr}(\widetilde\delta^n)=2\epsilon.
$$

The induction is

$$
\widetilde\delta^{n+1}
=\widetilde\delta^n\widetilde\delta
=\widetilde\delta\widetilde\delta
=\widetilde\delta.
$$

A connected component touching an external momentum is zero.  A closed
component gives $2\epsilon$.  For $c$ disconnected closed components,

$$
(2\epsilon)^c\in(\epsilon)R,
\qquad c\ge1.
$$

A fully closed network is coefficient-ring mixing.  An open network can retain
$\tau$; idempotence does not convert $\tau$ into an $\epsilon$ multiple.

$\mathcal M_{\rm phys}$ is $\epsilon$-torsion-free.  The scalar-trace
quotient

$$
\frac{\mathcal M_{\rm phys}}{(2\epsilon)\mathcal M_{\rm phys}}
=
\left(\frac{\mathbb Q[\epsilon]}{(\epsilon)}\right)^{66}
\otimes\operatorname{Sym}^2(\mathrm{Adj})
$$

is $\epsilon$-torsion.  Pole mixing remains possible:

$$
\epsilon^{-1}(2\epsilon P_i)=2P_i.
$$

This is coefficient-ring mixing, not an independent evanescent tensor.

The $\tau$ sector is an independent tensor sector before the missing quotient
matrix is applied.

## 9. Gap audit

$$
\begin{array}{c|c|c|c}
\text{gap}&\text{type}&\text{finding}&\text{status}\\ \hline
G1&\mathrm{G\!\!-PROJ}&\widetilde\delta
=\frac\epsilon2\delta_{(4)}+\tau&\texttt{REPAIRED}\\
G2&\mathrm{G\!\!-IDX}&229\text{ open }\tau\text{ projectors}&\texttt{OPEN\ P0}\\
G3&\mathrm{G\!\!-COLOR}&K^{AB}{}_{C[DE]}
\text{ exact }SU(2)\text{ equivariance}&\texttt{CLOSED}\\
G4&\mathrm{G\!\!-ALG}&\tau\text{ versus }(\epsilon)R
\text{ separated}&\texttt{REPAIRED}\\
G5&\mathrm{G\!\!-BV}&\text{EOM/IBP and full BV-ST class}
&\texttt{OPEN\ P1}
\end{array}
$$

$$
\boxed{
\texttt{PASS_EXACT_EXPLICIT_FULL_DRED_KERNEL_PHYSICAL4D_UNTOUCHED}
\qquad
63/63.
}
$$

Project $U(1)_R$, background-CE source covariance, the ordinary
$\operatorname{Sym}^2(\mathrm{Adj})$ split monomorphism, and the explicit
$SU(2)$ rank-five color witness pass.  Full-DRED raw quadratic-jet injectivity
fails.  The exhaustive $\tau$ quotient matrix and the full quantum BV-ST class
remain open; physical-$4d$ injectivity is untouched by this counterexample.
