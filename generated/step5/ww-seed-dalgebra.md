# Step 5A primitive WW seed

Typed reflection/source/variance repair applied.

$$
r_0=k,\qquad r_1=k+q,\qquad r_2=k+p+q.
$$

$$
\frac1{128}\,16\,(2i)(2i)=-\frac12.
$$

Each endpoint row:

$$
\left(-\frac{g^2}{8}\right)\left(-\frac12\right)=\frac{g^2}{16}.
$$

Reflection parity replay:

$$
s_{\mathrm{ref}}=(-1)_{(W,\widetilde W)}(-1)_{(Q_D,Q_{\bar D})}=+1.
$$

$$
|J_{AB}|=1,\qquad |\nabla_-(X^AX^B)|=1,\qquad |J_{AB}\nabla_-(X^AX^B)|=0.
$$

$$
\widetilde W^D_{\dot\alpha},\qquad \mathcal D_+{}^{\dot\alpha}X^E,
\qquad c_{ACD}c_{BCE}\left[\widetilde W^D_{\dot\alpha}\mathcal D_+{}^{\dot\alpha}X^E+(\mathcal D_+{}^{\dot\alpha}X^D)\widetilde W^E_{\dot\alpha}\right].
$$

Direct isolated triangle:

$$
\Gamma_{\triangle}^{A|B}=\frac{g^2}{8}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)
(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}
\int\frac{d^dk}{(2\pi)^d}\frac{L_{1m}L_{2r}}{k^2(k+q)^2(k+p+q)^2},
$$

$$
L_1=2k+q,\qquad L_2=2k+p+2q.
$$

$$
\Gamma_{\triangle,\mathrm{pole}}^{A|B}=\frac{g^2}{128\pi^2\epsilon}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)
(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}\widehat g_{mr}.
$$

Reflected isolated triangle:

$$
\Gamma_{\triangle,\mathrm{pole}}^{B|A}=\frac{g^2}{128\pi^2\epsilon}c_{BCD}c_{ACE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)
(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}\widehat g_{mr}.
$$

$$
\Gamma_{C,\mathrm{pole}}:\ \texttt{INVALIDATED\_REQUIRES\_TYPED\_CONTACT\_REPLAY}.
$$

$$
\Gamma_{\mathrm{anomaly}}:\ \texttt{INVALIDATED\_NOT\_PROPAGATED\_AFTER\_TYPED\_SIGN\_REPAIR}.
$$

Pre-$D$ action leg: $W_+^E$. Post-$D$ operator: $X^E=\nabla_+W_+^E$.

## DIRECT

| trace | $D_-$ | $\bar D$ edge | $D$ edge | endpoint sign | full orientation sign | numerator | isolated triangle pole | contact status |
|---|---|---|---|---:|---:|---|---|---|
| DA-D-001 | LEFT_LETTER | e0 | e1 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-D-002 | LEFT_LETTER | e0 | e2 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-D-003 | LEFT_LETTER | e1 | e1 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-D-004 | LEFT_LETTER | e1 | e2 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-D-005 | RIGHT_LETTER | e0 | e1 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-D-006 | RIGHT_LETTER | e0 | e2 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-D-007 | RIGHT_LETTER | e1 | e1 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-D-008 | RIGHT_LETTER | e1 | e2 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |

## REFLECTED

| trace | $D_-$ | $\bar D$ edge | $D$ edge | endpoint sign | full orientation sign | numerator | isolated triangle pole | contact status |
|---|---|---|---|---:|---:|---|---|---|
| DA-R-001 | LEFT_LETTER | e0 | e1 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-R-002 | LEFT_LETTER | e0 | e2 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-R-003 | LEFT_LETTER | e1 | e1 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-R-004 | LEFT_LETTER | e1 | e2 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-R-005 | RIGHT_LETTER | e0 | e1 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-R-006 | RIGHT_LETTER | e0 | e2 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-R-007 | RIGHT_LETTER | e1 | e1 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
| DA-R-008 | RIGHT_LETTER | e1 | e2 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY` |
