# Step 5 ordered (AA\to B_sC_s) outer-(A) gauge-current orbit

Status: `TARGET_BLIND_EXACT_PORT_AUDIT__POINTWISE_ZERO__NO_MINUS_ONE_THIRD_FROM_GAUGE_BC_CURRENT`.

## 1. Notation

Let

$$
(B_s\times C_s)^A
=c_{DE}{}^A B_s^D C_s^E,
$$

with independent external momenta

$$
B_s^D(p),
\qquad
C_s^E(q).
$$

The vector equation of motion is

$$
\mathscr E_V
=\nabla^a\mathcal W_a
-2i(\Phi_s\times C_s).
$$

The exact outer-(A) identity is

$$
\nabla_-A
=-\nabla_+\mathscr E_V
-2i(B_s\times C_s).
$$

## 2. Exact ordered (B_sC_s) ports

For the (\mathscr E_V)-current port,

$$
-D_+\bigl[-2i(\Phi_s\times C_s)\bigr]
=2i\bigl[(D_+\Phi_s)\times C_sigr]
+2i\bigl[\Phi_s\times(D_+C_s)\bigr].
$$

Using

$$
D_+\Phi_s=B_s,
\qquad
D_+C_s=0,
$$

one obtains

$$
-D_+\bigl[-2i(\Phi_s\times C_s)\bigr]
=2i(B_s\times C_s).
$$

The explicit outer-(A) contact is

$$
-2i(B_s\times C_s).
$$

Both terms have the same ordered color and momentum word:

$$
c_{DE}{}^A B_s^D(p)C_s^E(q).
$$

Therefore

$$
\boxed{
\left[2i-2i\right]
c_{DE}{}^A B_s^D(p)C_s^E(q)=0}
$$

for arbitrary independent (p,q).

## 3. Gauge-fixing and longitudinal port support

The gauge-fixing functional has only vector-superfield ports:

$$
\operatorname{Ports}(S_{\mathrm{gf}})=\{u\}.
$$

Hence

$$
\boxed{
\frac{\delta^2S_{\mathrm{gf}}}
{\delta B_s^D(p)\,\delta C_s^E(q)}=0.}
$$

The pure-gauge cubic and quartic action words also have only (u)-ports.  Adding a matter-action vertex changes the parent family to the already enumerated (M_s-M_s) matter orbit; it is not an additional pure-gauge (B_sC_s) contact.

The cancellation above occurs before any propagator or loop integration.  Thus no four-dimensional loop square is generated:

$$
N_{BC}^{\mathrm{gauge\ current}}(k)=0,
\qquad
N_{BC}^{\mathrm{gauge\ fixing}}(k)=0.
$$

Consequently

$$
\boxed{
C_{AA\to B_sC_s}^{\mathrm{outer}\ A,\mathrm{gauge\ current}}
=0.}
$$

In particular, this orbit does not produce

$$
-\frac13\lambda_1.
$$

The (\Omega_{21}) word is a residual of the (AA) matter second-mark (D)-algebra.  It is not a (B_sC_s) functional derivative of the pure-vector gauge-fixing or outer-(A) current port, and is not decided by this zero.

Verification:

```text
python scripts/step5_aa_gauge_bc_current_orbit_exact_audit.py \
  --output audits/step5-aa-gauge-bc-current-orbit-exact.json
```
