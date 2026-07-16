# Step 5 spectator-source self-energy orbit exact audit

Status: `TARGET_BLIND_CONNECTED_1PR__AMPUTATED_1PI_ANOMALY_PROJECTOR_ZERO`.

## 1. Graph cut

For every `SPECTATOR_SOURCE_DOUBLE_BRIDGE` route, write

$$
E_{\rm int}=\{e_0,e_1,e_2\},
\qquad
e_0=(I_0,V_1),
\qquad
e_1=e_2=(V_1,V_2).
$$

The unique cycle is $\{e_1,e_2\}$.  Removing $e_0$ gives

$$
G\setminus e_0
=
\{I_0\}\sqcup\{V_1,V_2\}.
$$

Therefore

$$
\boxed{\texttt{CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY}},
\qquad
\boxed{\mathcal P_{\rm 1PI}G=0}.
$$

## 2. Exact census and the 25-pair filter

The inactive letters are

$$
\{C_1,C_2,C_3,D_{\dot1},D_{\dot2}\}.
$$

Thus

$$
N_{\rm no\ descendant}=25=5\times5.
$$

Both parent enumerators return no anomaly candidate on those 25 ordered
pairs.  The spectator count is over the complementary 56 marked pairs:

$$
N_{\rm spectator}=870,
$$

$$
(N_{TGG},N_{TMM},N_{THH},N_{TGM},N_{TMH})
=(612,180,78,0,0).
$$

The marked-occurrence decomposition is

$$
N_{\rm quantum\ cut\ edge}=486,
\qquad
N_{\rm external\ spectator}=600,
\qquad
N_{\rm marked\ cycle}=0.
$$

## 3. First nonzero D-word

Choose the first $A>C_1$ spectator route,

$$
M_1(\widetilde\phi_1,u,\phi_1)
\mathrel{\substack{\longleftrightarrow\\[-2mm]\longleftrightarrow}}
M_1(\widetilde\phi_1,u,\phi_1).
$$

With source momentum $q$, bridge momenta $\ell$ and $q-\ell$, the exact sparse
Grassmann expansion gives

$$
\operatorname{Coeff}_{\theta_M^4\theta_H^4}\mathfrak D_{MM}
=1024q_{(4)}^2,
$$

$$
\mathfrak D_{MM}^{\rm collapsed}
=\frac14(1024q_{(4)}^2)
=256q_{(4)}^2,
$$

$$
\mathfrak D_{MM}^{\rm two\ full\ measures}
=\frac1{16}(1024q_{(4)}^2)
=64q_{(4)}^2.
$$

For $q=(1,2,0,0)$,

$$
q_{(4)}^2=5,
\qquad
\mathfrak D_{MM}^{\rm collapsed}=1280,
$$

for both $\ell=(3,5,0,0)$ and $\ell=(-2,7,1,0)$.  All four
$D^2\bar D^2/\bar D^2D^2$ source/bridge orientations give the same 1280.
The two superpotential orientations give

$$
\mathfrak D_{H_+H_-}
=\mathfrak D_{H_-H_+}
=4096q_{(4)}^2
=20480.
$$

These are nonzero ordinary external-leg self-energy words.

## 4. DRED anomaly projector

The 486 quantum marks lie on $e_0$, whose momentum is the fixed external
momentum $q$, not $\ell$ or $q-\ell$.  Hence

$$
\bar q^2-q_d^2=\mu_q^2=0.
$$

The 600 spectator marks contain no quantum inverse kernel.  Since neither
cycle edge is marked,

$$
N_{\rm marked\ cycle}=0,
\qquad
\mu_\ell^2\text{ remainder}=0.
$$

Route by route,

$$
\boxed{\mathcal P_{\rm anom}\mathcal P_{\rm 1PI}=0}.
$$

## 5. Ordered channels

For $A>C_r$ and $C_r>A$,

$$
(N_{TGG},N_{TMM},N_{THH},N_{TGM},N_{TMH})=(18,4,1,0,0),
$$

$$
\boxed{(-1,+1)+(0,0)=(-1,+1)}.
$$

For $B_r>C_s$ and $C_s>B_r$ on the diagonal,

$$
(N_{TMM},N_{THH},N_{TGG},N_{TGM},N_{TMH})=(2,2,0,0,0),
$$

$$
\boxed{+\delta_{rs}+0=+\delta_{rs}}.
$$

A separately defined $Z_{\rm letter}$ insertion is not included and is not
double counted as an amputated 1PI anomaly parent.
