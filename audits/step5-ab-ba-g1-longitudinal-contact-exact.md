# AB/BA G1 longitudinal and collapsed-contact orbit: exact audit

## 1. Conventions

$$
d=4-2\epsilon,\qquad
r_0=\ell,\quad r_1=\ell-p,\quad r_2=\ell-p-q,
$$

$$
\mu_\ell^2=\bar r_e^{\,2}-r_{e,d}^{\,2}=-\widehat\ell_{\rm user}^{\,2},\qquad
P_d=r_{0,d}^2r_{1,d}^2r_{2,d}^2.
$$

No holomorphic-twist coefficient is read by this audit.

## 2. Ordered source words and Koszul signs

$$
D_-(AB_1)=(D_-A)B_1+A(D_-B_1).
$$

$$
D_-(B_1A)=(D_-B_1)A-B_1(D_-A).
$$

Because $|B_1|=|D_-A|=1$ and $|A|=|D_-B_1|=0$,

$$
-B_1(D_-A)=+(D_-A)B_1,\qquad
(D_-B_1)A=A(D_-B_1).
$$

Thus the BA mirror has the same canonical row coefficient as AB.  The three
occurrence tags are $e_2$ for the A mark, $e_0$ for the B mark, and $e_1$ for
the transported longitudinal contact.

## 3. Parent and induced Schwinger contact

For every one of the $2\times2\times6\times2=48$ rows per mark,

$$
\alpha_A=-8R_A,\qquad
F_A=\alpha_A\bar r_2^{\,2}+L_A,\qquad
L_A=-\frac12D_+\bar D^2D^2,
$$

$$
C_{A,d}=-L_A-\alpha_A r_{2,d}^{\,2},
$$

$$
F_A\big|_{\bar r_2^{\,2}=r_{2,d}^{\,2}}+C_{A,d}=0,
$$

$$
F_A+C_{A,d}=\alpha_A\mu_\ell^2=-8R_A\mu_\ell^2.
$$

For the B mark,

$$
\alpha_B=-8R_B,\qquad F_B=\alpha_B\bar r_0^{\,2},\qquad L_B=0,
$$

$$
C_{B,d}=-\alpha_Br_{0,d}^{\,2},\qquad
F_B\big|_{\bar r_0^{\,2}=r_{0,d}^{\,2}}+C_{B,d}=0,
$$

$$
F_B+C_{B,d}=\alpha_B\mu_\ell^2=-8R_B\mu_\ell^2.
$$

## 4. First nonzero rows

Longitudinal row:

$$
(+,\dot a=0,\pi=012,
QL,A):\quad
F_A=-1024-2048i,\quad R_A=0,\quad
L_A=-1024-2048i,\quad C_{A,d}=-L_A.
$$

A-square row:

$$
(+,\dot a=0,\pi=012,
LQ,A):\quad
F_A=-14336+7168i,\quad R_A=256-128i,\quad
\alpha_A=-2048+1024i,\quad \bar r_2^2=7.
$$

B-square row:

$$
(+,\dot a=0,\pi=021,
QL,B):\quad
F_B=15360-15360i,\quad R_B=-128+128i,\quad
\alpha_B=1024-1024i,\quad \bar r_0^2=15.
$$

All 192 AB/BA rows are stored in the JSON artifact.

## 5. Standalone source-resolvent presentations

At $\ell=(2,1,-1,3)$, $p=(1,0,0,0)$, $q=(0,0,0,1)$ and $\dot a=0$,
the separately drawn $I_1S_{m3}$, $I_1S_{g3}$, and $I_0S_{m4}$ bubbles are
all zero, while

$$
-F_++F_-=61440.
$$

Hence they are not independent anomaly graphs.  The correct cut is
$\delta S/\delta\Phi$ on the same marked occurrence, giving $C_{A,d}$ and
$C_{B,d}$ above.

## 6. Finite master and G1 quotient

$$
\int\frac{d^{\,d}\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{P_d}=\frac{1}{32\pi^2}.
$$

The exact simplex result in $\lambda_1$ units is

$$
A:\ \frac43p+\frac23q,\qquad
B:\ \frac23p+\frac43q.
$$

For the local product, $q=-p$:

$$
A=\frac23,\qquad B=-\frac23,\qquad A+B=0.
$$

$$
\boxed{G1_{AB}(D>B_1)=0,\qquad G1_{BA}(B_1>D)=0.}
$$
