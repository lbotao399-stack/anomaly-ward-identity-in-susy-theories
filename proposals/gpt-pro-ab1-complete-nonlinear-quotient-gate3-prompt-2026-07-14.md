# GPT Pro Gate 3 — complete $AB_1/ B_1A$ nonlinear endpoint quotient

Recompute the remaining $AB_1$ one-loop 1PI anomaly orbit target-blind. The universal regulator rule is locked:

$$
\frac{r_{e,d}^2}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}=0,
\qquad
\frac{\bar r_e^2-r_{e,d}^2}{D_0D_1D_2}
=\frac{\mu_\ell^2}{D_0D_1D_2},
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

There is no extra $4-d$ factor. The 870 spectator-source double-bridge routes are connected but 1PR: the unique source-to-loop tree edge is an articulation edge, all quantum marks lie on it, and no marked edge lies on the loop cycle. Hence they are external-leg self energies removed by amputation and contribute zero to the 1PI anomaly. Work only with the nine $AB_1$ split-source 1PI parents and their exact descendants.

The current unquotiented ordered vector is

$$
(c_{B_1>D},c_{D>B_1},c_{C_3>C_2},c_{C_2>C_3})
=\left(\frac43,-\frac76,-2i\sqrt2,+2i\sqrt2\right).
$$

The current $G_1$ $D>B_1$ polynomial is

$$
-\frac76p-\frac43q,
$$

and the current $G_2$ $B_1>D$ polynomial is

$$
+\frac43p-\frac13q.
$$

Do not set $q=-p$ and do not quotient total derivatives until every selected edge has its own contact.

The concrete missing endpoint mechanism is the full Leibniz expansion already proved in the independent $B_1B_2$ family:

$$
D^2(\Pi_b\Pi_s)
=(D^2\Pi_b)\Pi_s+\Pi_b(D^2\Pi_s)
+2(D_-\Pi_b)(D_+\Pi_s)-2(D_+\Pi_b)(D_-\Pi_s).
$$

For a pure-antichiral $H_-$ endpoint the direct branch alone is incomplete. The surviving mixed-projector branch transports the inverse square to the neighboring edge and contributes a simplex moment $1/3$ beside the direct $2/3$ branch. In $B_1B_2$ the exact sum is $2/3+1/3=1$. Replay this full endpoint product for both $G_{3,2}$ and $G_{3,3}$ rather than multiplying a raw polynomial by an endpoint factor after contraction.

The current $G_3$ direct raw words are

$$
F_A^{\rm raw}
=-1024\det(r_0)W_{12}
+1024\det(r_1)W_{P0},
$$

$$
F_B^{\rm raw}
=-1024\det(r_2)W_{p0},
$$

with

$$
W_{12}=(1-y-z)(p_+\wedge q_+)+q_+\wedge L_+,
$$

$$
W_{P0}=-y(p_+\wedge q_+)+P_+\wedge L_+,
\qquad
W_{p0}=z(p_+\wedge q_+)+p_+\wedge L_+.
$$

Your former outer-$A$ cancellation used an incoming-routing sign change

$$
W_{P_G0}=-W_{P0}
$$

while retaining the old coefficient. That is noncovariant and rejected. Fix one outgoing routing and transform both the wedge and its coefficient together.

Required output:

1. For $G_1$, $G_2$, $G_{3,2}$, $G_{3,3}$, list every direct, transported mixed-Leibniz, nonlinear-current/potential, Euler, explicit-contact, and reflected occurrence with its selected edge.
2. For each square print the full-$d$ parent-minus-cut zero and the sole $\mu_\ell^2$ remainder.
3. Prove the occurrence quotient: distinguish a new neighboring edge of the same mark from a genuinely new mark; do not double count Euler-current summands as additional parents.
4. Compute both $AB_1$ and $B_1A$ independently, including color/Koszul/routing signs.
5. End with the sealed vector

$$
(c_{B_1>D},c_{D>B_1},c_{C_3>C_2},c_{C_2>C_3}).
$$

Only then compare with the external row

$$
(1,1,+i\sqrt2,-i\sqrt2)
$$

in the same declared ordering. If it differs, name the first exact occurrence. Do not fit a multiplicity or add a counterterm.
