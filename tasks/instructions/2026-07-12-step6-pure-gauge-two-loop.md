# Step 6 — Euclidean pure-gauge two-loop AWI

- Status: `PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE`
- Base: Step-5 proposal commit `57b7dc2a29e6174e0501a8afd6ab259298a3bc2b`
- Derivation authority: repository contracts only
- Notion input: forbidden
- Review/holomorphic-target input: forbidden by machine firewall

## Operator

$$
\mathcal I^{AB}
=
\nabla_-\!\left[X^AX^B\right],
\qquad
X^A=(\nabla_+W_+)^A.
$$

## Scope split

$$
\mathfrak G_{mathrm{Step6}}
=
\mathfrak G_{V\text{-only}}
\sqcup
\mathfrak G_{mathrm{FP}}
\sqcup
\mathfrak G_{mathrm{NK}}
\sqcup
\mathfrak G_{mathrm{matter}}.
$$

The first calculation is $\mathfrak G_{V\text{-only}}$.  FP/NK supply the fixed-gauge completion; matter is outside the first pure-gauge sector.

## Two-loop valence gate

For insertion valence $m$, action multiplicities $n_r$, and two external backgrounds,

$$
(m-2)+\sum_{r\geq3}(r-2)n_r=4.
$$

The literal five-edge $K_4\setminus e$ source families are

$$
I_3S_3^3,
\qquad
I_2S_3^2S_4.
$$

The second source family has two distinct background-valence distributions:

$$
\begin{aligned}
(b,q)_{I_2,S_3,S_3,S_4}
&=(0,2),(1,2),(0,3),(1,3),\\
(b,q)_{I_2,S_3,S_3,S_4}
&=(0,2),(0,3),(0,3),(2,2).
\end{aligned}
$$

The exchange of the two identical $S_3$ action occurrences is retained by labeled source-term/Wick assignment; it is not a second symmetry-factor division.

## Acceptance chain

$$
\text{Project AST}
\longrightarrow
\text{external projection}
\longrightarrow
\text{typed Wick GraphIR}
\longrightarrow
\text{AmplitudeIR}
\longrightarrow
\text{DWordIR}
\longrightarrow
\text{ForestIR}
\longrightarrow
\text{IBPCertificateIR}
\longrightarrow
\text{SDOrbitProofIR}.
$$

At every earlier stage,

$$
\mathcal A^{(2)}_{mathrm{ren}}=	exttt{UNCOMPUTED},
\qquad
\mathcal C^{(2)}_{mathrm{AWI}}=	exttt{UNCOMPUTED}.
$$

The external target is compared only after the Euclidean result and its artifact hash are frozen.
