# Step 5A primitive WW seed

Legacy specialized WW ledger; not a certificate from the generic typed $D$-compiler.

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

In this specialized ledger, two placements and four endpoint assignments give

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

Aggregate Schwinger--Dyson metric representative; the explicit contact basis is open:

$$
\left.\Gamma_{C,\mathrm{pole}}^{A|B}\right|_{\mathrm{aggregate\ SD}}=-\frac{g^2}{128\pi^2\epsilon}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)
(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}\delta^{(4)}_{mr}.
$$

$$
\left.\Gamma_{\triangle+C,\mathrm{pole}}^{A|B}\right|_{\mathrm{aggregate\ SD}}=\frac{g^2}{128\pi^2\epsilon}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)
(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}(\widehat\delta-\delta_{(4)})_{mr}.
$$

$$
\widehat\delta-\delta_{(4)}=-\widetilde\delta,\qquad p^n\widetilde\delta^{mr}(\sigma_m\bar\sigma_n\sigma_r)_+{}^{\dot\alpha}=-2\epsilon p_+{}^{\dot\alpha}.
$$

$$
\left.\Gamma_{\mathrm{candidate}}^{A|B}\right|_{\mathrm{CONDITIONAL\_ON\_CONTACT\_ORBIT\_SUM}}=\frac{g^2}{64\pi^2}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip_+{}^{\dot\alpha})X^E(p).
$$

$$
\left.\Gamma_{\mathrm{candidate}}^{B|A}\right|_{\mathrm{CONDITIONAL\_ON\_CONTACT\_ORBIT\_SUM}}=-\frac{g^2}{64\pi^2}c_{BCD}c_{ACE}\widetilde W^D_{\dot\alpha}(q)(ip_+{}^{\dot\alpha})X^E(p).
$$

In the reflected term relabel $D\leftrightarrow E$; since $|X|=0$:

$$
\left.\Gamma_{\mathrm{candidate}}^{A|B}+\Gamma_{\mathrm{candidate}}^{B|A}\right|_{\mathrm{CONDITIONAL\_ON\_CONTACT\_ORBIT\_SUM}}
=\frac{g^2}{64\pi^2}c_{ACD}c_{BCE}(ip_+{}^{\dot\alpha})
\left[\widetilde W^D_{\dot\alpha}X^E-X^D\widetilde W^E_{\dot\alpha}\right].
$$

Pre-$D$ action leg: $W_+^E$. Post-$D$ operator: $X^E=\nabla_+W_+^E$.

## DIRECT

| trace | $D_-$ | $\bar D$ edge | $D$ edge | endpoint sign | external Koszul sign | numerator | triangle pole | aggregate SD contact pole |
|---|---|---|---|---:|---:|---|---|---|
| DA-D-001 | LEFT_LETTER | e0 | e1 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-D-002 | LEFT_LETTER | e0 | e2 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-D-003 | LEFT_LETTER | e1 | e1 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-D-004 | LEFT_LETTER | e1 | e2 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-D-005 | RIGHT_LETTER | e0 | e1 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-D-006 | RIGHT_LETTER | e0 | e2 | 1 | 1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-D-007 | RIGHT_LETTER | e1 | e1 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-D-008 | RIGHT_LETTER | e1 | e2 | 1 | 1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `-g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |

## REFLECTED

| trace | $D_-$ | $\bar D$ edge | $D$ edge | endpoint sign | external Koszul sign | numerator | triangle pole | aggregate SD contact pole |
|---|---|---|---|---:|---:|---|---|---|
| DA-R-001 | LEFT_LETTER | e0 | e1 | 1 | -1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-R-002 | LEFT_LETTER | e0 | e2 | 1 | -1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-R-003 | LEFT_LETTER | e1 | e1 | 1 | -1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-R-004 | LEFT_LETTER | e1 | e2 | 1 | -1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-R-005 | RIGHT_LETTER | e0 | e1 | 1 | -1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-R-006 | RIGHT_LETTER | e0 | e2 | 1 | -1 | `(r0)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-R-007 | RIGHT_LETTER | e1 | e1 | 1 | -1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r1)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
| DA-R-008 | RIGHT_LETTER | e1 | e2 | 1 | -1 | `(r1)_+^dot_beta * (i*p)_a_dot_beta * (r2)^a_dot_alpha` | `-g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)` | `+g^2/(1024*pi^2*epsilon)*delta4^(mu nu)` |
