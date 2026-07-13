# Step 6 — Schwinger–Dyson cut/contact/bubble orbit

Status: `PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE`

$$
0=\int \mathcal DV\,\frac{\delta}{\delta V}
\left(\mathcal F e^{-S/\hbar}\right)
=\left\langle\frac{\delta\mathcal F}{\delta V}\right\rangle
-\hbar^{-1}\left\langle\mathcal F\frac{\delta S}{\delta V}\right\rangle.
$$

$$
K_VG_V=G_VK_V=1.
$$

| parent | orientation | rooted cuts | contacts | bubble paths |
|---|---:|---:|---:|---:|
| `G6_DIRECT_K4ME_I3_S3CUBED` | `direct` | 10 | 10 | 36 |
| `G6_DIRECT_K4ME_I3_S3CUBED` | `reflected` | 10 | 10 | 36 |
| `G6_DIRECT_K4ME_I2_S3SQ_S4` | `direct` | 10 | 10 | 36 |
| `G6_DIRECT_K4ME_I2_S3SQ_S4` | `reflected` | 10 | 10 | 36 |
| `G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4` | `direct` | 10 | 10 | 36 |
| `G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4` | `reflected` | 10 | 10 | 36 |

$$
(N_{\rm cut},N_{\rm contact},N_{\rm bubble})=(60,60,216).
$$

$$
\mathcal N_{\rm parent}+\mathcal N_{\rm contact}
+\mathcal N_{\rm bubble}:\quad
\text{BLOCKED\_EDGE\_TAGGED\_DALGEBRA\_NUMERATOR\_ABSENT}.
$$

Verification: `PASS`; 12/12 checks.
