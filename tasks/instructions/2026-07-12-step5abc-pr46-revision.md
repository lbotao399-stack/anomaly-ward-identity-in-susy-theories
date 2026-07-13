# PR #46 Step-5A/5B/5C revision instruction

Date: 2026-07-12

Preserve the Project-normalization audit and split Step 5 into:

1. `5A.PERTURBATIVE_FF_DRED_SUPERGRAPHS`;
2. `5B.SD_COMPLETE_GRAPH_ORBIT`;
3. `5C.FINITE_BV_DENSITY_AND_CYCLES`.

Only 5C may remain blocked by the exact finite coefficient-space density,
Berezinian, FP/NK cycles, finite vector coefficient cycle, and global local
non-minimal realization.

For 5A use

$$
K_V^{\rm phys}=-\frac h2p^2\Pi_{1/2},\qquad
K_V^{\rm gf}=-\frac h2p^2\Pi_0,
$$

$$
K_V^{\rm tot}=-\frac h2p^2\mathbf1,\qquad
G_V=-\frac{2g^2}{p^2}\kappa^{-1}\mathbf1,
$$

verify both inverse orders in the exact $16\times16$ Grassmann
representation, and use the reference-flat perturbative measure

$$
\mathfrak E^{\rm measure}=0.
$$

The only seed is

$$
\nabla_-\left[(\nabla_+W_+)^A(\nabla_+W_+)^B\right],
\qquad
K_+=-\frac18D_+\bar D^2D_+.
$$

Use

$$
\mathfrak E_{\Xi}^{\mathsf C}
=h\kappa\left[
\frac12\nabla^aW_a-i(\Phi_r\times\widetilde\Phi_r)
\right].
$$

Generate the prepotential insertion series, $W_{(n)}$, $\Gamma_{(n)}$,
$X_{(n)}$, and $I_{(2)},I_{(3)},I_{(4)}$ from Project definitions.  The
requested seed transport series is

$$
E_V=E_\Xi^{\mathsf C}
-\frac12[V,E_\Xi^{\mathsf C}]
-\frac16[V,[V,E_\Xi^{\mathsf C}]]+\cdots .
$$

Its sign relation to the already-derived functional Euler series must be
audited explicitly, not silently identified.

Instantiate the parent triangle and its reflected orientation with

$$
r_0=k,\qquad r_1=k+q,\qquad r_2=k+p+q.
$$

For each orientation emit

$$
2\ D_-\text{ placements}\times4\text{ derivative endpoints}=8
$$

exact traces, retaining edge tags, endpoint-transfer signs, Koszul signs,
mixed momenta, external derivatives, propagator collapses, and typed
classifications.  Generate the nonlinear-letter, quartic, and collapsed
Schwinger--Dyson children.  Compute the isolated-triangle and complete-contact
ordinary UV poles separately, with no $\epsilon$ inserted in the bare
triangle.  Accept a coefficient only after proving

$$
P_{\triangle}^{mn}-P_{\rm contact}^{mn}
=C_{\rm pole}(\widehat\delta^{mn}-\delta_{(4)}^{mn}).
$$

For the primitive seed, prove the FP/NK one-loop census result.  Absence at this
order is `PROVED_ABSENT_AT_THIS_ORDER`, not a global blocker.  The
$\exp(w\cdot\nabla)$ extension is outside the seed gate.

The former $16\times652=10432$ objects remain valence requests, not graphs.
CI success of the old blocked scaffold is not a one-loop result.
