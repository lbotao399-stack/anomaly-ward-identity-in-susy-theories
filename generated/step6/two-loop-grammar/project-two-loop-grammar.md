# Step 6 — pure-gauge Project grammar

`PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE`

$$
\Gamma_{(n)a}=\frac{(-1)^{n-1}}{n!}\operatorname{ad}_{V}^{n-1}(D_aV),
\qquad W_{(n)a}=-\frac18\bar D^2\Gamma_{(n)a},
$$

$$
\widetilde\Gamma_{(n)\dot a}=-\frac1{n!}\operatorname{ad}_{V}^{n-1}(\bar D_{\dot a}V),
\qquad \widetilde W_{(n)\dot a}=\frac18D^2\widetilde\Gamma_{(n)\dot a}.
$$

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| $\Gamma_{(n)}$ | 1 | -1/2*i | -1/6 | 1/24*i | 1/120 |
| $W_{(n)}$ | -1/8 | 1/16*i | 1/48 | -1/192*i | -1/960 |
| $\widetilde\Gamma_{(n)}$ | -1 | -1/2*i | 1/6 | 1/24*i | -1/120 |
| $\widetilde W_{(n)}$ | -1/8 | -1/16*i | 1/48 | 1/192*i | -1/960 |

$$
X_{(n)}=D_+W_{(n)+}+\sum_{r=1}^{n-1}[\Gamma_{(r)+},W_{(n-r)+}],
\qquad |X_{(n)}|=n.
$$

| $n$ | exact ordered $X_{(n)}$ coefficients |
|---:|:---|
| 1 | -1/8 |
| 2 | 1/16*i, -1/8*i |
| 3 | 1/48, -1/16, -1/16 |
| 4 | -1/192*i, 1/48*i, 1/32*i, 1/48*i |
| 5 | -1/960, 1/192, 1/96, 1/96, 1/192 |

$$
|I_{(N)}|=2\sum_{r=1}^{N-1}|X_{(r)}||X_{(N-r)}|
+2\sum_{t=1}^{N-2}\sum_{r=1}^{N-t-1}|X_{(r)}||X_{(N-t-r)}|.
$$

| $N$ | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|
| $|I_{(N)}|$ | 2 | 10 | 30 | 70 | 140 |

$$
S_{(N)}^+=-\frac h4\sum_{r=1}^{N-1}\int_{E,+}\kappa_{AB}W_{(r)}^{Aa}W_{(N-r)a}^{B},
$$

$$
S_{(N)}^-=-\frac h4\sum_{r=1}^{N-1}\int_{E,-}\kappa_{AB}\widetilde W_{(r)\dot a}^{A}\widetilde W_{(N-r)}^{B\dot a},
\qquad N=3,4,5,6.
$$

$$
|E_{\Xi}^{\rm gauge}|=2\sum_{n=1}^{5}n=30,
\qquad |E_V|=\sum_{d=1}^{5}2d(6-d)=70.
$$

$$
V_j=(V_B)_j+v_j,\qquad t=b+q.
$$

External projection: `BLOCKED_MISSING_PROJECT_EXTERNAL_PROJECTION_CERTIFICATE`.

Exact checks: `23/23`.
