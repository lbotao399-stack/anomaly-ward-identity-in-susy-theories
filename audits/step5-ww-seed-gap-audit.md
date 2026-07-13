# Step 5A/5B primitive \(WW\) derivation-gap audit

Input: contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md,
§5A--§5C.

Checked displayed equation groups: \(24\).

| gap id | type | location | claim | missing step | repair | severity | status |
|---|---|---|---|---|---|---|---|
| G1 | G-SIGN | (5.53m) | prepotential Euler transport | transpose of every \(\operatorname{ad}_{\mathcal V}\) power | \(F_n(-1)^n=1/(n+1)!\) displayed in (5.53l)--(5.53m) | P2 | RESOLVED |
| G2 | G-SCOPE | contact basis catalogue | ordered background/quantum assignments | distinction between a port-basis term and a physical graph | every basis term is ORDERED_PORT_BASIS_TERM_NOT_GRAPH; only the \(16\) SD metric contacts and \(6\) collapsed children are GraphIR | P2 | RESOLVED |
| G3 | G-SIGN | reflected orientation | relative minus sign | odd external permutation and derivative-transfer signs | \((\mathcal W,\widetilde{\mathcal W})\to(\widetilde{\mathcal W},\mathcal W)\) gives \(-1\); IBP and graded-prefix signs multiply to \(+1\) | P2 | RESOLVED |
| G4 | G-ALG | (5.53w)--(5.53y) | the aggregate SD contact is the explicit physical contact family | Wick pairing, symmetry factor, edge-tagged \(D\)-algebra, and routed integrand for all legal \(I_{(3)}\widetilde S_{(3)}\), \(I_{(4)}\), and collapsed terms | generate basis-resolved physical GraphIR and prove (5.54B) | P1 | OPEN |

Unresolved \(P0/P1\): \(1\).

## Verification checks

### V1. Fixed-gauge inverse

$$
K_V^{\rm tot}G_V
=\left(-\frac h2p^2\right)\left(-\frac{2g^2}{p^2}\right)\mathbf1_{16}
=hg^2\mathbf1_{16}
=\mathbf1_{16}.
$$

The reverse product is identical because both factors are scalar multiples of
\(\mathbf1_{16}\).

### V2. One-row and eight-row coefficients

$$
(-2g^2)^3
\left(-\frac{ih}{8}\right)
\left(\frac{ih}{8}\right)
=-\frac{8g^6h^2}{64}
=-\frac{g^2}{8}.
$$

$$
\frac1{128}\,16\,(2i)(2i)
=\frac{16}{128}(-4)
=-\frac12.
$$

$$
C_{\rm row}
=\left(-\frac{g^2}{8}\right)\left(-\frac12\right)
=\frac{g^2}{16}.
$$

For one \(D_-\) placement the four endpoint terms give
\((r_0+r_1)p(r_1+r_2)=L_1pL_2\). Both placements give

$$
C_{\triangle}^{\rm pre-int}
=2\left(\frac{g^2}{16}\right)
=\frac{g^2}{8}.
$$

### V3. Pole mismatch and finite coefficient

$$
C_{\rm pole}
=8\left(\frac{g^2}{1024\pi^2\epsilon}\right)
=\frac{g^2}{128\pi^2\epsilon}.
$$

$$
\widehat\delta-\delta_{(4)}=-\widetilde\delta,
\qquad
p^n\widetilde\delta^{mr}T_{mnr}=-2\epsilon p_+.
$$

$$
C_{\rm pole}(-\widetilde\delta^{mr})T_{mnr}p^n
=\frac{g^2}{128\pi^2\epsilon}(2\epsilon)p_+
=\frac{g^2}{64\pi^2}p_+.
$$
