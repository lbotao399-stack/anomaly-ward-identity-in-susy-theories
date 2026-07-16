# GPT Pro Gate 2Y: AA raw gauge convolution versus compact Hessian

Work target-blind. Do not use the holomorphic-twist coefficient until the final comparison.

The previous Gate 2W unit result is rejected because it multiplied the already evaluated sparse row polynomial by the same source scalar, Berezin saturation, and endpoint sum a second time. Gate 2X correctly leaves the complete coefficient undefined.

Locked conventions:

$$
V=\sqrt2g\,u,
\qquad
\langle u^A u^B\rangle=-\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_{12}),
\qquad
A_c^{(1)}=-\frac1{4\sqrt2}D_+\bar D^2D_+u.
$$

For external lower $W_+$, the chiral cubic endpoint is

$$
W^\gamma D_\gamma\big|_{W_+}=W^-D_-=-W_+D_-.
$$

The corrected exact sparse selected rows are

$$
G_{01,S}=(-b_2\det r_0,+b_2\det r_0,+b_2\det r_0,+b_2\det r_0),
$$

$$
G_{02,S}=(+b_0\det r_2,-b_0\det r_2,+b_0\det r_2,+b_0\det r_2).
$$

The exact longitudinal sums are

$$
\sum_jG_{01,L}^{(j)}=-2d_0(a_0b_2-b_0a_2),
\qquad
\sum_jG_{02,L}^{(j)}=0.
$$

With $r_2=r_0+P$, the full parent sum is

$$
G_{\rm full}=2b_0\left[a_2(d_0+d_2)-b_2(c_0+c_2)\right].
$$

Using the locked Euclidean matrix $\mathsf r=-i\sigma_E\cdot r$, do not identify the aggregate scalar projection with the occurrence-tagged cut.  Writing $b_2=b+B$, direct four-dimensional harmonic projection gives

$$
\mathcal P_{\rm scalar}(G_{\rm selected})=(-4b-3B)\bar\ell^2,
$$

$$
\mathcal P_{\rm scalar}(G_{\rm full})=(-4b-2B)\bar\ell^2,
$$

$$
\mathcal P_{\rm scalar}(G_{\rm longitudinal})=+B\bar\ell^2.
$$

Indeed,

$$
G_{\rm full}=4b\det\ell+2b[aD-bC+2Ad-2Bc+(AD-BC)],
$$

and the loop Laplacian of its quadratic part is $-16B$, whereas the selected quadratic part has loop Laplacian $-24B$; use $\Delta_\ell\bar\ell^2=8$.  Therefore edge-tagging is necessary.

The structural raw census has three position-labeled $u$ ports at every gauge cubic. For AA it emits $72$ split-source TGG routes: $6$ source/bridge/external assignments at each cubic times two chiral orderings. This count is structural and is not automatically a multiplicity.

Start from the authority all-order gauge convolution (5A.52):

$$
S_{R,+}^{\rm g}=\sum_{p,q,r,s\ge0}
\frac{\eta_R(-1)^{p+r}f_{AB}}
{256p!q!r!s!(p+q+1)(r+s+1)}
\int_{R,+}
[\bar D^2(V^pD^aV V^q)]^A
[\bar D^2(V^rD_aV V^s)]^B,
$$

and the analogous antichiral line with $(-1)^{q+s}$.

Required exact replay:

1. Set $p+q+r+s=1$. Write all four cubic words per chirality with their rational signs and denominators. Expand their labeled functional derivatives into every ordered assignment of source port, bridge port, and external port. Do not collapse by cyclicity before displaying this table.

2. Insert $V=\sqrt2g\,u$, $h=g^{-2}$ and the locked $f_{AB},\widetilde f_{AB},\eta_R$. Derive the coefficient of every raw port row from (5A.52). Sum them and prove or disprove the compact Hessians

$$
\mathfrak V_W=-\frac{ig}{4\hbar}c_{UCE}W_c^{E\gamma}(D_{C\gamma}-D_{U\gamma}),
\qquad
\mathfrak V_{\widetilde W}=+\frac{ig}{4\hbar}c_{UCD}\widetilde W_{c\dot\gamma}^{D}(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).
$$

Explicitly state which of the $72$ structural routes cancel, combine, or are already contained in these Hessians. No route count may be multiplied after the action sum.

3. Re-evaluate one fixed DA orientation with the corrected $-D_-$ endpoint and the complete raw action-word sum. For every surviving raw row show: action coefficient, source coefficient, three propagators, Grassmann polynomial, selected edge, full-$d$ cut, and sole $\mu_\ell^2$ remainder.

4. Use only

$$
\frac{r_{e,d}^2}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}=0,
\qquad
\bar r_e^2-r_{e,d}^2=\mu_\ell^2,
$$

and

$$
\int\frac{d^d\ell}{(2\pi)^d}\frac{\mu_\ell^2}{D_0D_1D_2}=\frac1{32\pi^2}.
$$

Compute the rank-one simplex moments explicitly. Keep the independent typed structures $D(q)pA(p)$ and $D(q)qA(p)$ separate.

5. Derive the reflected AD orientation independently, including epsilon-index signs. Give the final target-blind ordered vector. If it remains undefined, identify the first missing equality. If it disagrees with the later HT comparison, locate the first exact mismatch; do not repair by inserting the target.

Forbidden: using the old $D_+$ word, reusing the old rank-two $L_1^mL_2^n/\epsilon$ pole, multiplying sparse rows by $16(-1/4)$ again, or multiplying by $72$ without the raw action coefficients.
