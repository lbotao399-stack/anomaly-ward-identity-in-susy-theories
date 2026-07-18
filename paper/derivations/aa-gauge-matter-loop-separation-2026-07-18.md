# AA seed: gauge-loop / matter-loop separation, endpoint-row numerator sums, and the external-slot Wick computation

**Provenance.** Synthesis note prepared 2026-07-18 by Kimi (Moonshot AI) working with the repo owner, from the locked artifacts cited inline (`audits/step5-all-letter-pairs-triangle-census.md`, `audits/step5-aa-gauge-*`, `audits/step5-aa-matter-*`, `audits/step5-aa-external-slot-decomposition-exact.md`, `audits/step5-aa-standard-feynman-strictification.md`, `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`, `…/step-05a-….md`). **This note is a derivation/synthesis layer, not a machine-verified audit; it duplicates no authority — the cited contracts and audits remain the legal layer.** Two presentation-level corrections relative to the owner's earlier reading aid are recorded explicitly in §4–§5: (i) the triangle numerator is the **line-sum** $L_1=r_0+r_1$, $L_2=r_1+r_2$ (UV-leading $2\ell$ each), not a single line momentum; (ii) the gauge family's per-occurrence value $-\lambda_1/8$ and the accepted sector value $(1,-1)$ are **two independent bookkeepings** (selected directed occurrence vs 48-row target-blind replay), not related by route-count multiplication.

Status: `SYNTHESIS_NOTE__NOT_MACHINE_VERIFIED__PENDING_OWNER_REVIEW`.

---

## 1. Graph census: the (A,A) channel is two loop families

Parent skeleton vertex classes (`step5-all-letter-pairs-triangle-census.md`; the file's own status is `BLOCKED_RAW_ALL_PAIR_TRIANGLE_AND_DESCENDANT_ORBITS` — parent classes are the skeleton-level input; the 81-row acceptance rests on `step5-global-81-target-blind-orbit-ledger.json` and the strictification seal):

$$
G:=\mathcal V_{VVV},\qquad
M_r:=\mathcal V_{\widetilde\Phi_rV\Phi_r},\qquad
H_{\widetilde\Phi^3}:=\mathcal V_{\widetilde\Phi_1\widetilde\Phi_2\widetilde\Phi_3},
$$

$$
T_{GG}=(I_{XY},G,G),\quad
T_{GM}=(I_{XY},G,M_r),\quad
T_{MM}=(I_{XY},M_r,M_s),\quad
T_{MH}=(I_{XY},M_r,H_{\widetilde\Phi^3}).
$$

$$
\boxed{(A,A)=T_{GG}+\sum_{r=1}^{3}T_{MM}^{(r,r)}}
$$

- **Gauge loop** $T_{GG}$: two cubic gauge vertices (one chiral $S_+^{g,(3)}$, one antichiral $S_-^{g,(3)}$), three vector lines. Produces the field-strength output sector $\langle D,A\rangle-\langle A,D\rangle$.
- **Matter loops** $T_{MM}^{(r,r)}$ ($r=1,2,3$): two matter-gauge vertices $M_r$, **two vector source edges + one internal chiral matter edge**. Produces the matter-letter sector $\sum_r(\langle B_r,C_r\rangle-\langle C_r,B_r\rangle)$. The three flavors are three typed output rows, **not** a $\times3$ multiplicity.

Route counts (`step5-aa-gauge-full-source-sd-orbit-exact.json`, route_coverage; exhaustiveness only, `"coefficient_inference_from_census": false`):

$$
N_{AA}=42,\qquad N_{GG}=36,\qquad N_{M_rM_r}=2\times3=6,\qquad N_{AA}^{\rm marked}=2(42)=84 .
$$

(The gauge-only $2\times36=72$ marked occurrences and the census's global all-pair marked count $72$ are two different $72$s.)

## 2. Gauge loop $T_{GG}$: vertex words with the difference structure

Cubic vertex words (from (5A.49)–(5A.52), measure identity $\int d^2\vartheta\,\bar D^2Y=-4\int d^4\vartheta\,Y$):

$$
S_+^{g,(3)}=-\frac{ih}{64}c_{ABC}\int d^4\vartheta\,D^aV^A\,\bar D^2(D_aV^BV^C),
\qquad
S_-^{g,(3)}=+\frac{i\widetilde h}{64}c_{ABC}\int d^4\vartheta\,\bar D^{\dot a}V^A\,D^2(\bar D_{\dot a}V^BV^C).
$$

Ordered action Hessians (`step5-aa-gauge-canonical-normalization-ledger.md` §4) — each vertex distributes its spinor derivative as a **difference over its two internal incident lines**:

$$
\mathfrak V_W=-\frac{ig}{4\hbar}c_{UCE}W^{E\gamma}(D_{C\gamma}-D_{U\gamma}),
\qquad
\mathfrak V_{\widetilde W}=+\frac{ig}{4\hbar}c_{UCD}\widetilde W^D_{\dot\gamma}(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}),
$$

with $\delta_1\delta_2[Du,u]=[Du_1,u_2]+[Du_2,u_1]$ already inside the Hessian (no remaining $2!$).

## 3. The numerator is a line-sum: endpoint rows and the factor 4

Each derivative endpoint converts via the anticommutator ($\{D_a,\bar D_{\dot a}\}=-2i\sigma^m_{a\dot a}\partial_m$, $\{\bar D_{\dot a},D_a\}=+2i\bar\sigma^m_{\dot a a}\partial_m$) acting on that line's plane wave; per placement the four endpoint rows (sign table of `step5-canonical-superfield-ww-seed.md` §6: $(r_0,r_1):(-1)(-1)$, $(r_0,r_2):(+1)(+1)$, $(r_1,r_1):(+1)(+1)$, $(r_1,r_2):(-1)(-1)$) sum to

$$
\big[(r_0)_{+\dot\beta}+(r_1)_{+\dot\beta}\big]\mathsf p^{\dot\beta\gamma}
\big[(r_1)_\gamma{}^{\dot\alpha}+(r_2)_\gamma{}^{\dot\alpha}\big].
$$

Hence (routing $r_0=\ell$, $r_1=\ell+p$, $r_2=\ell+p+q$):

$$
L_1=r_0+r_1=2\ell+p,\qquad
L_2=r_1+r_2=2\ell+2p+q,\qquad
L_1^mL_2^n=4\,\ell^m\ell^n+(\text{linear/constant}),
$$

$$
T_{m\rho n}:=\sigma_m\bar\sigma_\rho\sigma_n .
$$

The factor $4=2\times2$ comes from the two vertices' line-sums (the two mixed anticommutators, i.e. the content of the ledger's $w_D=\frac1{32}\cdot16\cdot2\cdot2$). Shift $r=\ell+yp+z(p+q)$:

$$
L_1=2r+\underbrace{((1-2y)p-2z(p+q))}_{a'},\qquad
L_2=2r+\underbrace{((2-2y-2z)p+(1-2z)q)}_{b'},
$$

pole sector: odd terms vanish by $r\to-r$; constant terms multiply $J_3$ ($\Gamma(3-d/2)=\Gamma(1+\epsilon)$, no pole); hence

$$
\int_\ell^{\rm DRED}\frac{4r_mr_n}{(r^2+\Delta)^3}
=4\,\frac{\widehat\delta_{mn}}d(J_2-\Delta J_3)
=\widehat\delta_{mn}J_2,
\qquad
\operatorname*{Pole}_{\epsilon=0}\int_\ell^{\rm DRED}\frac{L_1^mL_2^n}{D_0D_1D_2}
=\frac{\widehat\delta^{mn}}{16\pi^2\epsilon}
$$

(tensor residue multiplier $2_{\Gamma(3)}\times4_{\rm numerator}\times\frac14_{\rm reduction}\times\frac12_{\rm simplex}=1$). With the prefactor $\frac{\hbar g^2}{2}$ (its exact factor equation: $\frac{(+i)(-i)h^2}{64^2}\cdot\hbar^{-2}\cdot(-4)^2\cdot(-\frac18)^2\cdot(2\hbar g^2)^3\cdot16\cdot16\cdot2\cdot2\cdot(\frac{16}{16})^2\cdot1=\frac{\hbar g^2}{2}$, numerically $\frac{131072}{262144}$):

$$
\Gamma_T=\frac{\hbar g^2}{32\pi^2\epsilon}\,\mathbb F^{AB}{}_{DE}\,\widehat\delta^{mn}T_{m\rho n}p^\rho,
\qquad
\Gamma_C=-\frac{\hbar g^2}{32\pi^2\epsilon}\,\mathbb F^{AB}{}_{DE}\,\delta_4^{mn}T_{m\rho n}p^\rho,
$$

$$
\Gamma_T+\Gamma_C
=-\frac{\hbar g^2}{32\pi^2\epsilon}\,\mathbb F\,\breve\delta^{mn}T_{m\rho n}p^\rho
=\frac{\hbar g^2}{16\pi^2}\,\mathbb F^{AB}{}_{DE}\,\sigma\!\cdot\!p
=\lambda_1\,\mathbb F^{AB}{}_{DE}\,\sigma\!\cdot\!p,
$$

using $p^\rho\breve\delta^{mn}\sigma_m\bar\sigma_\rho\sigma_n=-2\epsilon\,\sigma\!\cdot\!p$.

## 4. Matter loops $T_{MM}^{(r,r)}$

Vertices and propagators ((5A.53) $n=1,2$; canonical $u=V/(\sqrt2g)$, $\Phi_c=g^{-1}\Phi$; note the same bilinear differs by $g^2$ between canonical and physical letters, $\mathcal O_{\rm phys}=g^2\mathcal O_c$):

$$
S_{m3}=-h\sum_r\int d^8z\,\kappa_{DU}\widetilde\Phi_r^D V^A(T_A)^U{}_E\Phi_r^E,
\qquad
\langle\Phi_{c,r}\widetilde\Phi_{c,s}\rangle
=\delta_{rs}\frac{\hbar\kappa}{16p^2}\bar D_1^2D_1^2\delta^4_{12}.
$$

Resolvent census (only the last term is nonzero): $\langle\mathcal I_2\rangle_{BC}=0$ (two-loop), $\langle\mathcal I_1S_{m3}\rangle=0$ (scaleless), $\langle\mathcal I_0S_{m4}\rangle=0$ (seagull), $(2\hbar^2)^{-1}\langle\mathcal I_0S_{m3}S_{m3}\rangle$ = directed matter triangle.

Triangle data (`step5-aa-matter-full-placements-independent.md`): routing $r_0=k$, $r_1=k-q$, $r_2=k-p-q$; endpoints $v_1:C^D(q)$, $v_2:B^E(p)$; source words $\mathcal A(r)=D_+\bar D^2D_+$, $\mathcal M(r)=D_-\mathcal A(r)$; internal chiral edge $\frac1{16D_1}\bar D_1^2D_1^2\delta^4_{12}$. Grassmann words:

$$
\mathcal G_0=-16384\,\mathcal S_{012},\qquad
\mathcal G_2=-16384\,\mathcal T_{012},
$$

$$
\mathcal S_{012}=(\det r_0)W_{12}-(\det r_1)W_{02},\qquad
\mathcal T_{012}=W_{01}(u_2\wedge v_1),\qquad
\mathcal T_{012}=-\mathcal S_{012}+W_{12}(u_0\wedge q_-).
$$

Prefactor: $\frac{h^2}{\hbar^2}(-2\hbar g^2)^2(\frac{\hbar g^2}{16})=\frac{\hbar g^2}{4}$; source factors $(-\frac18)^2$ (from $A^{(1)}=-\frac18D_+\bar D^2D_+V$), two Berezin measures $(-\frac14)^2$, raw Grassmann $16384$: product $16$; normalized parent word $4\eta_{\rm src}\hbar g^2$ with $\eta_{\rm src}=+1$ (fixed in `step5-aa-external-slot-decomposition-exact.md` §8).

DRED defects: $\Delta_0=\mu_\ell^2(W_{12}-W_{02})$; second-mark split $D_-D_+\bar D^2D_+=-8(\det r_2)D_+-\frac12D_+\bar D^2D^2$ with graded transport $D_{0+}\bar D_0^2D_0^2\delta^4_{02}=-D_2^2\bar D_2^2D_{2+}\delta^4_{02}$ and $D_2^2(-r_1)\bar D_2^2(-r_1)D_2^2(-r_1)=-16(\det r_1)D_2^2(-r_1)$; $\Delta_2^{\rm full}=(\frac12-z)\mu_\ell^2(p_+\wedge q_+)$ (repaired truncation $(y-z)+(\frac12-y)=\frac12-z$). Simplex moments: $2\int_{\Sigma_2}x=2\int y=2\int z=\frac13$, $2\int(\frac12-z)=\frac16$. Endpoint coefficients:

$$
c_0=4\hbar g^2\Big(-\frac23\Big)\frac1{32\pi^2}=-\frac43\lambda_1,\qquad
c_2=4\hbar g^2\Big(\frac16\Big)\frac1{32\pi^2}=+\frac13\lambda_1,\qquad
-\frac43\lambda_1+\frac13\lambda_1=-\lambda_1,
$$

per directed attachment (raw orientation, output $C^D(q)>B^E(p)$); rows $(F_1,F_2,X_1,X_2)=(-\frac43,+\frac13,+\frac13,-\frac43)\lambda_1$ on the respective wedge bases; $|\operatorname{Aut}|=1$.

## 5. External letters from Wick contraction (external-slot decomposition)

External legs are computed, not assumed (`step5-aa-external-slot-decomposition-exact.md`, $269/269$, 0 failure):

- **Three placements per chirality** ($H^W$ field-strength leg, $H^{\partial C}$ derivative-commutator, $H^C$ plain-commutator): $H^{\rm full}=H^W+H^{\partial C}+H^C$; every sparse row obeys $H^W+H^{\partial C}+H^C-H^{\rm full}=0$; $N_W=N_{\partial C}=N_C=8$, $N_{\rm full}=24_\chi$, Hessian groups $=2\cdot4\cdot3=24$; the old $H^W$-only probe kept 16 rows and omitted 32.
- **By-parts transport modifies the external letters**: $D_{0+}\bar D_0^2D_0^2\delta^4_{02}=-D_2^2\bar D_2^2D_{2+}\delta^4_{02}$ (signs $(-1)^5=-1$, $(-1)^{10}=+1$); $P_+$ at one endpoint transfers to $P_-$ at the other endpoint, never to a second $P_+$; the longitudinal word must be transported (the discarded-longitudinal error: only originally tagged inverse kernels entering the SD orbit is false).
- **Typed quotient**: $(DA_p,DA_q,AD_p,AD_q)\mapsto(DA_p,0,AD_p,0)$ (the $q$-rows are EOM/divergence carriers); reflection $p_{+\dot\alpha}AD^{\dot\alpha}=-D_{\dot\alpha}p_+^{\dot\alpha}A$; no extra edge factor 2, no global metric-trace factor $d$ or $4$.
- **Residual letters**: gauge loop → $(\widetilde W^D_{\dot\alpha}(q),D_+W_+^E(p))=(D^D,A^E)$; matter loop → $(C_r^D(q),B_r^E(p))$.
- External-line vector branch (per leg): $\bar D_A^2D_A^2(\frac12\{D_{A+},\bar D_{A\dot a}\})\delta^4_{A1}=-16p^2\sigma^\rho_{+\dot a}p_\rho\delta^4_{A1}$; amputation strips $1/p^2$; the chiral projector $\mathcal P_+=\bar D^2D^2/16\Box$ supplies $1/16$ canceling the external sandwich's $16$; net per leg $-\sigma^\rho_{+\dot a}p_\rho\times(\text{letter})$.

## 6. Two independent bookkeepings (do not cross-multiply)

- **Selected directed occurrence (canonical normalization)**: $\big(\frac1{64}\big)(16)(2)(2)\big[(-\frac{ig}{4\hbar})(+\frac{ig}{4\hbar})(-\hbar)^3\big](-1)(-4)\frac1{32\pi^2}=-\frac{\hbar g^2}{128\pi^2}=-\frac{\lambda_1}{8}$ (`step5-aa-gauge-full-source-sd-orbit-exact.json`: directed triangle $-\lambda_1/8$, remaining resolvent rows $=0$, `"coefficient_in_lambda1_units":"-1/8"`, conditional on the FF slice).
- **Accepted full sector**: the $(1,-1)$ on each family's letter sector comes from the independent 48-row target-blind replay (3 placements × 4 chirality pairs × 2 marks + typed EOM quotient + Fourier map $-i$; `step5-aa-external-slot-decomposition-exact.md` §7, `step5-aa-standard-feynman-strictification.md` §11.2), **not** from summing $-\lambda_1/8$ over routes (`"coefficient_inference_from_census": false`). The difference between the two is exactly the placement content ($H^W$ 16 rows vs $H^W+H^{\partial C}+H^C$ 48 rows).

## 7. Assembly

$$
\boxed{
\Gamma_{AA}^{(1)}
=\lambda_1\mathbb F^{AB}{}_{DE}\Big[
\underbrace{\langle D^D,A^E\rangle-\langle A^D,D^E\rangle}_{\text{gauge loop }T_{GG},\ (1,-1)}
+\underbrace{\sum_{r=1}^{3}\big(\langle B_r^D,C_r^E\rangle-\langle C_r^D,B_r^E\rangle\big)}_{\text{matter loops }\sum_rT_{MM}^{(r,r)},\ (1,-1)\text{ per flavor}}\Big]
=\lambda_1\,\mathbb F^{AB}{}_{DE}\,\mathscr Z^{DE}}
$$

with $\lambda_1:=\hbar g^2/(16\pi^2)$, $\mathbb F^{AB}{}_{DE}:=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E}$; HT check-only seal $\Gamma_{AA,\rm one\ loop}^{(1)}-\Gamma_{AA,\rm HT}^{(1)}=0$; $N_{\rm total}=9216$, $N_{\rm sparse}=2048$, 0 equality failure.

Caveats retained: gauge ledger `MINUS_ONE_EIGHT_GENUINE_ON_CONDITIONAL_SLICE`; auxiliary/ghost/Nielsen–Kallosh/counterterm gauge census is a named open gate; the old $v_{\rm old}=u/\sqrt2$ unit-propagator treatment omits $(\frac12)^3=\frac18$ and inflates by $2^3=8$ — all exact coefficients here are in canonical normalization.
