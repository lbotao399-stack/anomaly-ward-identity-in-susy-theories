# GPT Pro Gate 4: AB/BA G1 occurrence-resolved edge map

Work target-blind. Do not use the holomorphic-twist output or the compact result kernel to assign a graph coefficient.

G2 and G3 are already directly sealed:

$$
G_2:\quad \frac43-\frac13=1,
\qquad
G_3:\quad \frac23+\frac13=1.
$$

The remaining raw graph is

$$
G_1=(I[u,\phi_1],M_1,\mathcal V_{VVV}).
$$

There are six ordered VVV routes, two outer source marks, two derivative placements, and both chiralities. The existing generic-$(p,q)$ code returns an unquotiented word

$$
D_{\dot a}\left(-\frac76p-\frac43q\right)^{\dot a}B_1,
$$

but it obtains the longitudinal part from a global transverse metric trace, not from occurrence-matched inverse-kernel cuts. The old $q=-p$ checker is also not a valid adjudicator: it uses the full loop Laplacian $\Delta_\ell/8$, so $(\ell\cdot p)^2$ tensor terms contaminate the claimed scalar square.

Required exact calculation:

1. Start from the four cubic words of (5A.52) with $p+q+r+s=1$. Display their rational signs. Differentiate their three labeled $V$ ports and map them to the six parent-port routes. Prove the relation to the QL/LQ representation; do not multiply route counts.

2. For each route, chirality, QL/LQ placement, and outer mark, retain the operator history of every $D,\bar D$ anticommutator. Split

$$
D_-D_+\bar D^2D_+
=8\bar\Box D_+-\frac12D_+\bar D^2D^2
$$

and transport the longitudinal term by graded integration by parts. Whenever a new inverse square is produced on $r_0,r_1,$ or $r_2$, tag that exact edge before simplifying the polynomial.

3. Write every anomaly-bearing occurrence in the form

$$
c_{j,e}(p,q,\ell)\left[
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac{r_{e,d}^2}{D_0D_1D_2}
\right]
=c_{j,e}\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

Show the matching Schwinger contact for the same occurrence and same edge. Terms not carrying an occurrence-tagged inverse square are not anomaly terms, even when their global four-dimensional tensor trace is nonzero.

4. Integrate the exact rank-zero/rank-one residuals over the simplex. Keep

$$
D(q)pB_1(p),
\qquad
D(q)qB_1(p)
$$

as independent typed structures until the EOM quotient is explicitly applied.

5. Repeat the reflected BA orientation independently. Give the target-blind ordered G1 vector and only then compare with the already sealed one-loop cohomology vector.

Forbidden: using the old full-Laplacian $q=-p$ projector; treating the generic global transverse trace as an occurrence cut; inserting the compact residual-$q$ coefficient as graph input; dropping transported longitudinal terms; or using HT to choose the answer.

Relevant local artifacts supplied conceptually:

- `scripts/step5_ab1_g1_vvv_dword_replay.py`
- `scripts/step5_ab1_marked_sd_orbit_exact_audit.py`
- `audits/step5-ab1-marked-sd-orbit-exact.md`
- `audits/step5-ab-ba-full-1pi-quotient-exact.md`
