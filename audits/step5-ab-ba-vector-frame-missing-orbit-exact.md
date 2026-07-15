# AB/BA vector-frame missing-orbit exact audit

Status: `PASS_VECTOR_FRAME_ORBIT_HAS_ONLY_DB_BD_SUPPORT__CANNOT_SUPPLY_REQUESTED_CC_HALF`.

External target used: `false`.

## 1. Vector-frame source

The locked symmetric bridge gives

$$
\mathcal B_{\rm ad}=e^{V_{\rm ad}/2}
=1+\frac12V_{\rm ad}+\frac18V_{\rm ad}^2+O(V_{\rm ad}^3).
$$

Therefore

$$
\mathcal O_V^{AB}
=(\mathcal B_{\rm ad}A_C)^A
>(\mathcal B_{\rm ad}B_{1,C})^B.
$$

At order one the two new endpoint words have coefficients $(1/2,1/2)$.
At order two the left, crossed, and right bridge coefficients are

$$
\frac18,\qquad \frac14,\qquad \frac18.
$$

The complete source-word counts through order two are

$$
N_0=1,\qquad N_1=4,\qquad N_2=10.
$$

## 2. Same-order one-loop topology census

$$
\begin{array}{c|c|c}
\text{sector}&\text{route count}&\text{external support}\\ \hline
I_1V_1&16&(u,\phi_1),(\phi_1,u)\\
I_0V_2&2&(u,\phi_1)\\
I_2&9&(u,\phi_1)
\end{array}
$$

Thus

$$
\operatorname{supp}_{\rm ext}
(I_1V_1\oplus I_0V_2\oplus I_2)
=\{D>B_1,\ B_1>D\}.
$$

No row has external support $(\widetilde\phi_2,\widetilde\phi_3)$ or
$(\widetilde\phi_3,\widetilde\phi_2)$.  Removing an internal edge by a
Schwinger cut preserves external ports, hence

$$
\Delta_{\rm vector\ bridge}(C_2>C_3)
=\Delta_{\rm vector\ bridge}(C_3>C_2)=0.
$$

Consequently the vector-frame orbit cannot equal

$$
(-1,0,+i\sqrt2,-i\sqrt2).
$$

## 3. Exact similarity chain

For the matter endpoint/link/seagull chain,

$$
e^{V/2}e^{-V}e^{V/2}=1.
$$

At order $V^2$ the six terms are

$$
\frac18+\frac12+\frac18-\frac12+\frac14-\frac12=0.
$$

The $I_2$ one-propagator self-contractions have no injected loop momentum and
are massless scaleless tadpoles, hence their dimensional-regularization value
is exactly zero.

## 4. Claim boundary

Before any Ward comparison, both graph families must be moved to the same
total-derivative quotient.  For $G_1$,

$$
(2,2)_{(\mathrm{pair},\mathrm{EOM})}
\xrightarrow{\ T_{DB}=\mathrm{pair}+\mathrm{EOM}\ }
(0,2)_{(\mathrm{pair},T_{DB})}.
$$

For $G_2$,

$$
\left(-\frac13,\frac43\right)_{(\mathrm{pair},\mathrm{EOM})}
\xrightarrow{\ T_{BD}=-\mathrm{pair}+\mathrm{EOM}\ }
\left(1,\frac43\right)_{(\mathrm{pair},T_{BD})}.
$$

Hence the common compact TD vector is

$$
v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2).
$$

The former hybrid vector used the first coordinate before the $G_1$ TD map:

$$
\pi_{\rm EOM}^{G_1}(2,2)=2
\ne
\pi_{\rm TD}^{G_1}(2,2)=0.
$$

This is its first false equality.

With

$$
M_q=
\begin{pmatrix}
1&-1&0&0\\
i\sqrt2&0&1&0\\
-i\sqrt2&0&0&1
\end{pmatrix},
$$

the topology support theorem imposes

$$
\delta v_{\rm graph}=(\delta_{DB},\delta_{BD},0,0).
$$

If this missing-graph support alone were required to solve the Ward equation,
then

$$
M_q(v_{\rm TD}+\delta v_{\rm graph})=0
$$

would have the unique hypothetical solution

$$
\delta v_{\rm graph}^{\rm hyp}=(2,1,0,0),
$$

and therefore

$$
v_{\rm TD}+\delta v_{\rm graph}^{\rm hyp}
=2k_q,
\qquad
k_q=(1,1,-i\sqrt2,+i\sqrt2).
$$

This scale-two ray conflicts with the target-blind Project $AA$ coefficient,
whose common supermultiplet scale is one.  Hence

$$
\delta v_{\rm graph}^{\rm hyp}=(2,1,0,0)
$$

is not the final completion.

## 5. General finite composite-source settlement

A general finite composite-source counterterm is not restricted by the
external support of missing Feynman graphs.  The three exact conditions are

$$
M_qv_{\rm ren}=0,
\qquad
q_1Y_1=iZ,
\qquad
t_{AA}=1.
$$

Thus $v_{\rm ren}=k_q$ and

$$
\boxed{
\delta v_{\rm fin}
=v_{\rm ren}-v_{\rm TD}
=(1,0,+i\sqrt2,-i\sqrt2).}
$$

Equivalently,

$$
\boxed{
\delta\Gamma_{\rm fin}^{AB}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\langle D^D,B_1^E\rangle
+i\sqrt2\langle C_2^D,C_3^E\rangle
-i\sqrt2\langle C_3^D,C_2^E\rangle
\right].}
$$

The completed vector is exactly

$$
\boxed{
v_{\rm ren}
=v_{\rm TD}+\delta v_{\rm fin}
=(1,1,-i\sqrt2,+i\sqrt2)
=k_q,}
\qquad
M_qv_{\rm ren}=0.
$$

## 6. Claim boundary

The graph-support theorem proves $\delta_{CC}^{\rm graph}=0$ for the
vector-frame orbit.  It neither derives nor constrains the $CC$ entries of a
general finite composite-source counterterm.  No $Q_0$-exact preimage is
claimed by this component linear-system audit.
