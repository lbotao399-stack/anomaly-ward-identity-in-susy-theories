# Step 5 all ordered-pair triangle-parent port census

Status: `STRUCTURAL_PARENT_CENSUS_ONLY__D_ALGEBRA_AND_SD_ORBITS_PENDING`.

## 1. Linear source ports

$$
A\mapsto u,
\qquad
B_r\mapsto\phi_r,
\qquad
C_r\mapsto\widetilde\phi_r,
\qquad
D_{\dot a}\mapsto u.
$$

Only

$$
\nabla_-A\ne0,
\qquad
\nabla_-B_r\ne0
$$

can mark an inverse-kernel edge.

## 2. Cubic action ports

$$
G=(u,u,u),
$$

$$
M_r=(\widetilde\phi_r,u,\phi_r),
$$

$$
H_+=(\phi_1,\phi_2,\phi_3),
\qquad
H_-=(\widetilde\phi_1,\widetilde\phi_2,\widetilde\phi_3).
$$

The only propagator-compatible unordered field pairs are

$$
(u,u),
\qquad
(\phi_r,\widetilde\phi_r),
\qquad
(\widetilde\phi_r,\phi_r).
$$

The legacy family `SPLIT_SOURCE_SINGLE_BRIDGE` consists of

$$
I_0(L_i,L_j)
\longrightarrow V_L,
\qquad
I_0(L_i,L_j)
\longrightarrow V_R,
$$

$$
V_L\longleftrightarrow V_R,
$$

with one unused external port on each cubic vertex.  The perturbative factor is

$$
\frac1{2!}(1+1)=1.
$$

The omitted family `SPECTATOR_SOURCE_DOUBLE_BRIDGE` consists of

$$
I_0(L_i,L_j):quad L_i\ \text{external spectator},
\qquad
L_j\longrightarrow V_1,
$$

$$
V_1\mathrel{\substack{\longleftrightarrow\\[-2mm]\longleftrightarrow}}V_2,
\qquad
V_2\longrightarrow X_{\rm ext}.
$$

For both families,

$$
E=3,
\qquad
V=3,
\qquad
L=E-V+1=1.
$$

The two bridges exhaust the two unused ports of $V_1$ and two distinct ports
of $V_2$.  The remaining $V_2$ port is the second external field.

Cutting the unique source-to-$V_1$ edge disconnects the composite insertion
from the two-bridge self-energy loop.  Therefore every route in this family is

$$
\texttt{CONNECTED\_BUT\_1PR\_EXTERNAL\_LEG\_SELF\_ENERGY},
\qquad
\mathrm{1PI}=\mathrm{false}.
$$

The loop cycle contains only the two $V_1\leftrightarrow V_2$ bridges.  These
rows belong to the connected structural census, not to the amputated 1PI
triangle-parent set.  Machine classification:
`CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY`.

## 3. Exact target-blind counts

$$
N_{\mathrm{ordered\ pairs}}=81,
\qquad
N_{\mathrm{marked\ pairs}}=56,
\qquad
N_{\mathrm{no\ descendant\ pairs}}=25.
$$

The inactive set is

$$
\{C_1,C_2,C_3,D_{\dot1},D_{\dot2}\}.
$$

Hence exactly

$$
25=5\times5
$$

ordered pairs have no outer descendant.  Both enumerators return the empty
set on those pairs; $N_{\mathrm{spectator}}=870$ is the sum over the remaining
56 marked ordered pairs, not over all 81 pairs.

$$
N_{\mathrm{legacy}}=495,
\qquad
N_{\mathrm{spectator}}=870,
$$

$$
N_{\mathrm{directed\ parent\ routes}}=495+870=1365,
\qquad
N_{\mathrm{marked\ inverse\ edges}}=612+486=1098.
$$

All parent routes decompose as

$$
T_{GG}=180+612=792,
\qquad
T_{GM}=144,
\qquad
T_{MM}=87+180=267,
\qquad
T_{MH}=60,
\qquad
T_{HH}=24+78=102,
$$

$$
792+144+267+60+102=1365.
$$

The new family alone has

$$
T_{GG}^{\rm spectator}=612,
\qquad
T_{MM}^{\rm spectator}=180,
\qquad
T_{HH}^{\rm spectator}=78,
$$

$$
T_{GM}^{\rm spectator}=T_{MH}^{\rm spectator}=0.
$$

The last equality follows from ports: a $G$ vertex has two unused $u$ ports,
whereas an $M$ vertex has only one $u$ port; an $M$ vertex and an $H$ vertex
have only one mutually dual matter port after the source attachment.  Neither
mixed pair supports two compatible bridges.

Among the 1086 marked occurrences in the spectator family, 486 marks lie on
the quantum source edge and 600 marks lie on the external spectator:

$$
N_{\rm spectator,marked}=486+600=1086.
$$

No route in this census is assigned a coefficient before its actual marked
edge, full-dimensional cut, contact representative, four-dimensional
$D$-word, and $\mu_\ell^2$ remainder are replayed.

Verification command:

    python scripts/step5_all_triangle_parent_port_census_audit.py --check
