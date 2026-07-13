# Step 6 — typed Project-AST to two-loop Wick join

`PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE`

$$
t_v=b_v+q_v,\qquad
\mathfrak W_{G,o}=\prod_{v\in V(G)}\mathfrak W_{v,o},\qquad
|\mathfrak W_{G,o}|=\prod_{v\in V(G)}|\mathfrak W_{v,o}|.
$$

| parent | orientation | local radices | labeled Wick pairings |
|:---|:---:|:---:|---:|
| `I3__S3^3` | `direct` | `[60, 24, 24, 24]` | 829440 |
| `I3__S3^3` | `reflected` | `[60, 24, 24, 24]` | 829440 |
| `I2__S3^2__S4^1` | `direct` | `[4, 24, 24, 144]` | 331776 |
| `I2__S3^2__S4^1` | `reflected` | `[4, 24, 24, 144]` | 331776 |
| `I2__S3^2__S4^1` | `direct` | `[4, 24, 24, 144]` | 331776 |
| `I2__S3^2__S4^1` | `reflected` | `[4, 24, 24, 144]` | 331776 |

$$
F_{\exp}(\{n_{r,\sigma}\})
=\frac{(-1)^N}{\hbar^N\prod_{r,\sigma}n_{r,\sigma}!},
\qquad N=\sum_{r,\sigma}n_{r,\sigma}=3.
$$

$$
(g^2)^5h^3=(g^2)^5(g^2)^{-3}=(g^2)^2=g^4.
$$

| $n_+$ | $n_-$ | expansion factor |
|---:|---:|:---|
| 2 | 1 | `(-1)^3/(1!_[S3_MINUS]*2!_[S3_PLUS]*hbar^3)` |
| 1 | 2 | `(-1)^3/(2!_[S3_MINUS]*1!_[S3_PLUS]*hbar^3)` |
| 0 | 3 | `(-1)^3/(3!_[S3_MINUS]*hbar^3)` |
| 3 | 0 | `(-1)^3/(3!_[S3_PLUS]*hbar^3)` |

$$
F_{\exp}(S_{3,+}^2S_{4,+})=-\frac1{2!\,1!\,\hbar^3}
=-\frac1{2\hbar^3}.
$$

Chirality zero inference: `UNPROVED_NO_MEASURE_SATURATION_OR_DALGEBRA_CERTIFICATE`; discarded `0`.

External projection: `BLOCKED_MISSING_PROJECT_EXTERNAL_PROJECTION_CERTIFICATE`.

Propagator: `BLOCKED_PROJECT_VECTOR_PROPAGATOR_ATTACHMENT_NOT_COMPILED`.

D-algebra: `BLOCKED_EDGE_TAGGED_DALGEBRA_NOT_COMPILED`.

Amplitude: `BLOCKED_PROPAGATOR_AND_DALGEBRA_IR_ABSENT`.

Coefficient: `BLOCKED_RENORMALIZED_AMPLITUDE_IR_ABSENT`.

Exact checks: `24/24`.
