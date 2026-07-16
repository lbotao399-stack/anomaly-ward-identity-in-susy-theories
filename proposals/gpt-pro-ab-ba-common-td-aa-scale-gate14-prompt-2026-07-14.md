# GPT Pro Gate 14 — common-TD quotient and AA-fixed finite normal product

Gate 13 correctly found that the complete vector-frame bridge/link/seagull
orbit is a supertrace commutator and contributes no independent
\(\mu_\ell^2\) residue.  Its final coefficient settlement is nevertheless
invalid because it mixes quotient layers.

## Locked target-blind data

Use the six-carrier basis

$$
\mathcal B_6=
(X_{DB},E_{DB},X_{BD},E_{BD},C_{23},C_{32}),
$$

with

$$
v_{\rm raw}
=\left(2,2,-\frac13,\frac43,-2i\sqrt2,+2i\sqrt2\right).
$$

The two total-derivative identities are different:

$$
T_{DB}=X_{DB}+E_{DB},
\qquad
T_{BD}=-X_{BD}+E_{BD}.
$$

Therefore

$$
G_1:(2,2)_{(X,E)}\mapsto(0,2)_{(X,T)},
$$

$$
G_2:\left(-\frac13,\frac43\right)_{(X,E)}
\mapsto\left(1,\frac43\right)_{(X,T)}.
$$

The only common compact TD-layer vector is

$$
v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2).
$$

Thus Gate 13 equation (16)

$$
(2,1,-2i\sqrt2,+2i\sqrt2)
$$

is a hybrid: it retained \(\pi_{G_1,\rm EOM}=2\) while using
\(\pi_{G_2,\rm TD}=1\).

The complete lower-resolvent audit additionally gives

$$
\mathcal A_{R_1}=\mathcal A_{R_2}=\mathcal A_{R_3}=0.
$$

In particular,

$$
N_{R_{2,G}}=-\frac{\sqrt2}{4}S(q)
$$

contains neither \(\ell\) nor a four-dimensional inverse square;
\(R_{2,M}=R_{3,M4}=0\), and \(R_1\) is scaleless.

## Project Ward data

In the ordered basis

$$
(D>B_1,B_1>D,C_2>C_3,C_3>C_2),
$$

the target-blind residual-supersymmetry matrix is

$$
M_q=
\begin{pmatrix}
1&-1&0&0\\
i\sqrt2&0&1&0\\
-i\sqrt2&0&0&1
\end{pmatrix},
$$

$$
\ker M_q
=\mathbb C k_q,
\qquad
k_q=(1,1,-i\sqrt2,+i\sqrt2).
$$

A hypothetical missing graph is constrained by the vector-frame support
theorem to \(\delta_{23}=\delta_{32}=0\).  Under that restriction,

$$
M_q(v_{\rm TD}+\delta_{\rm graph})=0
$$

has the unique solution

$$
\delta_{\rm graph}^{\rm hyp}=(2,1,0,0),
\qquad
v_{\rm TD}+\delta_{\rm graph}^{\rm hyp}=2k_q.
$$

This is not a graph result: the exact D-algebra gives zero for that missing
orbit.  It is also not the final finite scheme because the independently
derived target-blind AA anomaly fixes scale one:

$$
\Delta(A,A)=\mathscr Z,
\qquad
q_s\mathscr Y_r=i\delta_{sr}\mathscr Z.
$$

A general finite composite-source counterterm is a local operator-basis
change and is not restricted by missing-graph external support.  Thus the
Project equations are

$$
M_q(v_{\rm TD}+\delta_{\rm fin})=0,
\qquad
v_{\rm TD}+\delta_{\rm fin}=1\cdot k_q.
$$

They give

$$
\delta_{\rm fin}
=(1,0,+i\sqrt2,-i\sqrt2),
$$

$$
v_{\rm ren}
=(1,1,-i\sqrt2,+i\sqrt2).
$$

## Required adjudication

1. Recompute both \((X,E)\to(X,T)\) maps explicitly and state whether Gate
   13 equation (16) mixed the G1 EOM projection with the G2 TD projection.
2. Compute \(M_qv_{\rm TD}\), the topology-limited hypothetical solution,
   and the unrestricted finite solution separately.
3. Use only \(\Delta(A,A)=\mathscr Z\) and
   \(q_s\mathscr Y_r=i\delta_{sr}\mathscr Z\) to fix the ray scale.  Do not
   use the holomorphic-twist target.
4. State explicitly that \(\delta_{\rm fin}\) is a finite normal-product
   scheme term, not an additional cutting-failure graph; every bare anomaly
   graph residue remains an occurrence-wise \(\mu_\ell^2\) cutting failure.
5. Identify the first false equality in Gate 13.  The incomplete leading
   chiral-frame source is not the final error because the complete bridge
   orbit cancels as a supertrace commutator.

End with exactly one verdict:

`GATE13_QUOTIENT_RETRACTED__FINITE_SCALE_ONE_ACCEPTED`

or

`FINITE_SCALE_ONE_REJECTED`, followed by the first explicit failed Project
equation.
