# Step 6 — Project external-background projection

$$
V_i=V_{B,i}+v_i,\qquad
F(V_1,\ldots,V_t)=\sum_{\rho\in\{B,q\}^t}
F(V_{\rho_1,1},\ldots,V_{\rho_t,t}),
\qquad [F_\rho]=1.
$$

$$
\Gamma_{(1)+}[V_B]=D_+V_B,
\qquad W_{(1)+}[V_B]=-\frac18\bar D^2D_+V_B,
$$

$$
X_{(1)}[V_B]=D_+W_{(1)+}[V_B]
=-\frac18D_+\bar D^2D_+V_B=K_+V_B,
\qquad K_+:=-\frac18D_+\bar D^2D_+.
$$

$$
\widetilde\Gamma_{(1)\dot a}[V_B]=-\bar D_{\dot a}V_B,
\qquad \widetilde W_{(1)\dot a}[V_B]
=-\frac18D^2\bar D_{\dot a}V_B.
$$

| GraphIR | local radices | candidates |
|---|---:|---:|
| `G6_DIRECT_K4ME_I3_S3CUBED` | `[12, 12]` | 144 |
| `G6_DIRECT_K4ME_I2_S3SQ_S4` | `[12, 24]` | 288 |
| `G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4` | `[72]` | 72 |

$$
N_{\rm projection}=12\cdot12+12\cdot24+72=504.
$$

Nonlinear source factors remain their exact ordered AST; no linear-letter rename is made.

Linear-map AST hashes: `2dbd73f882b1dacbe191f3d3078426623c1ef0f314f48af17d6b6be75048f747`.

Quantum-edge join, propagators, Wick contractions, D-algebra, amplitudes, and graph coefficients are absent.
