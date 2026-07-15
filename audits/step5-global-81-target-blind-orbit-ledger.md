# Step 5 target-blind global 9x9 representative-orbit ledger

Status: `LOCAL_PROPOSAL__81_COMPLETE_EXACT__0_OPEN__NO_TARGET_FILL`.

Authority: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66` is the frozen authority base; this dirty-worktree ledger is not authoritative.

## 1. Definitions

$$
\mathbb L=(A,B_1,B_2,B_3,C_1,C_2,C_3,D_{\dot1},D_{\dot2}),
\qquad
|A|=|C_r|=0,\quad |B_r|=|D_{\dot a}|=1.
$$

$$
\nabla_-(L_iL_j)=(\nabla_-L_i)L_j+(-1)^{|L_i|}L_i(\nabla_-L_j).
$$

$$
\mu_\ell^2:=\bar\ell^2-\ell_d^2,\qquad
J_{\mu^2}=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}=\frac1{32\pi^2}.
$$

Coefficient policy: only completed target-blind representative audits may populate a result. Every incomplete pair has `result=null` and `final_state=OPEN`.

Forbidden inputs: `generated/step5/project-result-ledger.json` and `generated/step5/ht_ordered_pair_targets.json`.

## 2. Symmetry and transport maps

| map | letter/index transport | Koszul/sign | color transport | inference rule |
|---|---|---|---|---|
| `FLAVOR` | `B_r->B_pi(r)`, `C_r->C_pi(r)`; `epsilon_123->epsilon_pi(1)pi(2)pi(3)`; `delta_rs->delta_pi(r)pi(s)` | `+1`; source slots fixed; `epsilon` component supplies `sgn(pi)` | `(A,B,D,E)` fixed; `F^(AB)_(DE)` fixed | allowed only for a completed flavor-covariant representative |
| `DOTTED` | `D_dota->S_dota^dotb D_dotb` | `+1`; source slots fixed; scalar coefficient fixed | `(A,B,D,E)` fixed | allowed only for a completed dotted-spinor representative |
| `ORDER_REBASE` | `(L_i^A,L_j^B)->(L_j^B,L_i^A)` | source exchange `(-1)^(|L_i||L_j|)`; right descendant sign `(-1)^|L_i|` | `(A,B,D,E)->(B,A,E,D)` | recorded only; never used here to infer a reverse coefficient |

Completed `AC/CA` and `BC/CB` reverse orders are independently routed in their audits. Completed reverse off-diagonal `BB` rows come from fixed-slot flavor transport, not source-slot reversal.

## 3. Representative gates

| family | maturity | final | proved local subresult | blocker |
|---|---|---|---|---|
| `AA` | `COMPLETED` | `COMPLETE_EXACT` | `full gauge-plus-three-flavor matter ordered vector (1,-1,1,-1,1,-1,1,-1)` | `null` |
| `AB/BA` | `COMPLETED` | `COMPLETE_EXACT` | `six flavor-covariant ordered rows on the Project-Ward-renormalized vector (1,1,-i*sqrt(2),+i*sqrt(2))` | `null` |
| `AC/CA` | `COMPLETED` | `COMPLETE_EXACT` | `full order-g^2 orbit` | `null` |
| `AD/DA` | `COMPLETED` | `COMPLETE_EXACT` | `four dotted ordered pairs with raw contact multiplicity one and finite W-link longitudinal zero` | `null` |
| `BB off-diagonal` | `COMPLETED` | `COMPLETE_EXACT` | `six ordered epsilon_rst components` | `null` |
| `BB diagonal` | `COMPLETED` | `COMPLETE_EXACT` | `three exact zeros; TMM D-words zero and epsilon repeated-index H routes zero` | `null` |
| `BC/CB` | `COMPLETED` | `COMPLETE_EXACT` | `all eighteen delta_rs components` | `null` |
| `BD/DB` | `COMPLETED` | `COMPLETE_EXACT` | `twelve exact zeros; 399 typed routes and 117 symbolic D-word checks` | `null` |
| `CC/CD/DC/DD` | `COMPLETED` | `COMPLETE_EXACT` | `twenty-five no-descendant exact zeros` | `null` |

## 4. Exact completed formulas

$$
\Delta(A,A)=\lambda_1\mathbb F^{AB}{}_{DE}\Big[
\langle D^D,A^E\rangle-\langle A^D,D^E\rangle
+\sum_{r=1}^3(\langle B_r^D,C_r^E\rangle-\langle C_r^D,B_r^E\rangle)\Big].
$$

$$
\Delta(A,B_r)=\Delta(B_r,A)
=\lambda_1\mathbb F^{AB}{}_{DE}\left[
\langle D^D,B_r^E\rangle+\langle B_r^D,D^E\rangle
-i\sqrt2\,\epsilon_{rst}\langle C_s^D,C_t^E\rangle\right].
$$

$$
\Delta(A,C_r)=\Delta(C_r,A)
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[D_{\dot a}^D(P^{\dot a}C_r)^E-(P_{\dot a}C_r)^D D^{E\dot a}\right].
$$

$$
\Delta(B_r,B_s)_{r\ne s}
=\epsilon_{rst}\lambda_1\mathbb F^{AB}{}_{DE}
\left[-i\sqrt2\langle D^D,C_t^E\rangle+i\sqrt2\langle C_t^D,D^E\rangle\right].
$$

$$
\Delta(B_r,C_s)=\Delta(C_s,B_r)
=\delta_{rs}\lambda_1\mathbb F^{AB}{}_{DE}\langle D^D,D^E\rangle.
$$

$$
\Delta(A,D_{\dot a})=\lambda_1\mathbb F^{AB}{}_{DE}
\left[\frac13\langle P_{\dot a}D^D,D^E\rangle
+\frac23\langle D^D,P_{\dot a}D^E\rangle\right].
$$

$$
\Delta(D_{\dot a},A)=\lambda_1\mathbb F^{AB}{}_{DE}
\left[\frac23\langle P_{\dot a}D^D,D^E\rangle
+\frac13\langle D^D,P_{\dot a}D^E\rangle\right].
$$

$$
\Delta(B_r,B_r)=\Delta(B_r,D_{\dot a})=\Delta(D_{\dot a},B_r)=0.
$$

$$
\Delta(X,Y)=0,\qquad X,Y\in\{C_1,C_2,C_3,D_{\dot1},D_{\dot2}\}.
$$

## 5. All 81 ordered pairs

`result` lists the coefficient vector divided by `lambda1`; `null` is not a zero.

| # | pair | marks `(side,sign)` | orbit / representative | transport | maturity | final / resolution | result | blocker/evidence |
|---:|---|---|---|---|---|---|---|---|
| 001 | `A__A` | `L:+1,R:+1` | `AA_FULL_TARGET_BLIND` / `A__A` | `identity; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1,-1,1,-1,1,-1,1,-1]` | `audits/step5-aa-standard-feynman-strictification.md,audits/step5-aa-external-slot-decomposition-exact.json` |
| 002 | `A__B1` | `L:+1,R:+1` | `AB_BA_PROJECT_WARD_RENORMALIZED::A>B` / `A__B1` | `flavor pi:(1,2,3)->(1, 2, 3); B1->B1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1,1,-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-ab-ba-project-ward-finite-renormalization-exact.json,audits/step5-ab-ba-vector-frame-missing-orbit-exact.json,audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json,audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json,audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json` |
| 003 | `A__B2` | `L:+1,R:+1` | `AB_BA_PROJECT_WARD_RENORMALIZED::A>B` / `A__B1` | `flavor pi:(1,2,3)->(2, 3, 1); B1->B2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1,1,-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-ab-ba-project-ward-finite-renormalization-exact.json,audits/step5-ab-ba-vector-frame-missing-orbit-exact.json,audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json,audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json,audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json` |
| 004 | `A__B3` | `L:+1,R:+1` | `AB_BA_PROJECT_WARD_RENORMALIZED::A>B` / `A__B1` | `flavor pi:(1,2,3)->(3, 1, 2); B1->B3; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1,1,-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-ab-ba-project-ward-finite-renormalization-exact.json,audits/step5-ab-ba-vector-frame-missing-orbit-exact.json,audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json,audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json,audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json` |
| 005 | `A__C1` | `L:+1` | `AC_CA::A>C` / `A__C1` | `flavor pi:(1,2,3)->(1, 2, 3); C1->C1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-1,+1]` | `audits/step5-ac-ca-family-exact.json` |
| 006 | `A__C2` | `L:+1` | `AC_CA::A>C` / `A__C1` | `flavor pi:(1,2,3)->(2, 3, 1); C1->C2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-1,+1]` | `audits/step5-ac-ca-family-exact.json` |
| 007 | `A__C3` | `L:+1` | `AC_CA::A>C` / `A__C1` | `flavor pi:(1,2,3)->(3, 1, 2); C1->C3; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-1,+1]` | `audits/step5-ac-ca-family-exact.json` |
| 008 | `A__Ddot1` | `L:+1` | `AD_DA_FULL::A>D` / `A__Ddot1` | `dotted S:dot1->dot1; Ddot1->Ddot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1/3,2/3]` | `audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json,audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.json,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.md` |
| 009 | `A__Ddot2` | `L:+1` | `AD_DA_FULL::A>D` / `A__Ddot1` | `dotted S:dot1->dot2; Ddot1->Ddot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1/3,2/3]` | `audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json,audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.json,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.md` |
| 010 | `B1__A` | `L:+1,R:-1` | `AB_BA_PROJECT_WARD_RENORMALIZED::B>A` / `B1__A` | `flavor pi:(1,2,3)->(1, 2, 3); B1->B1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1,1,-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-ab-ba-project-ward-finite-renormalization-exact.json,audits/step5-ab-ba-vector-frame-missing-orbit-exact.json,audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json,audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json,audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json` |
| 011 | `B1__B1` | `L:+1,R:-1` | `BB_DIAGONAL_EXACT_ZERO` / `B1__B1` | `flavor pi:(1,2,3)->(1, 2, 3); B1->B1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 012 | `B1__B2` | `L:+1,R:-1` | `BB_OFFDIAGONAL` / `B1__B2` | `flavor pi:(1,2,3)->(1, 2, 3); (B1,B2,C3)->(B1,B2,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=epsilon_123=1; Koszul source-order sign not used` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-bb-offdiagonal-family-exact.json` |
| 013 | `B1__B3` | `L:+1,R:-1` | `BB_OFFDIAGONAL` / `B1__B2` | `flavor pi:(1,2,3)->(1, 3, 2); (B1,B2,C3)->(B1,B3,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=epsilon_132=-1; Koszul source-order sign not used` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[sqrt(2)*I,-sqrt(2)*I]` | `audits/step5-bb-offdiagonal-family-exact.json` |
| 014 | `B1__C1` | `L:+1` | `BC_CB::B>C::delta=1` / `B1__C1` | `diagonal flavor pi:(1,2,3)->(1, 2, 3); (B1,C1)->(B1,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 015 | `B1__C2` | `L:+1` | `BC_CB::B>C::delta=0` / `B1__C2` | `off-diagonal flavor pi:(1,2,3)->(1, 2, 3); (B1,C2)->(B1,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 016 | `B1__C3` | `L:+1` | `BC_CB::B>C::delta=0` / `B1__C2` | `off-diagonal flavor pi:(1,2,3)->(1, 3, 2); (B1,C2)->(B1,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 017 | `B1__Ddot1` | `L:+1` | `BD_DB_EXACT_ZERO::B>D` / `B1__Ddot1` | `flavor pi:(1,2,3)->(1, 2, 3); B1->B1; dotted S:dot1->dot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 018 | `B1__Ddot2` | `L:+1` | `BD_DB_EXACT_ZERO::B>D` / `B1__Ddot1` | `flavor pi:(1,2,3)->(1, 2, 3); B1->B1; dotted S:dot1->dot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 019 | `B2__A` | `L:+1,R:-1` | `AB_BA_PROJECT_WARD_RENORMALIZED::B>A` / `B1__A` | `flavor pi:(1,2,3)->(2, 3, 1); B1->B2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1,1,-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-ab-ba-project-ward-finite-renormalization-exact.json,audits/step5-ab-ba-vector-frame-missing-orbit-exact.json,audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json,audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json,audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json` |
| 020 | `B2__B1` | `L:+1,R:-1` | `BB_OFFDIAGONAL` / `B1__B2` | `flavor pi:(1,2,3)->(2, 1, 3); (B1,B2,C3)->(B2,B1,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=epsilon_213=-1; Koszul source-order sign not used` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[sqrt(2)*I,-sqrt(2)*I]` | `audits/step5-bb-offdiagonal-family-exact.json` |
| 021 | `B2__B2` | `L:+1,R:-1` | `BB_DIAGONAL_EXACT_ZERO` / `B1__B1` | `flavor pi:(1,2,3)->(2, 3, 1); B1->B2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 022 | `B2__B3` | `L:+1,R:-1` | `BB_OFFDIAGONAL` / `B1__B2` | `flavor pi:(1,2,3)->(2, 3, 1); (B1,B2,C3)->(B2,B3,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=epsilon_231=1; Koszul source-order sign not used` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-bb-offdiagonal-family-exact.json` |
| 023 | `B2__C1` | `L:+1` | `BC_CB::B>C::delta=0` / `B1__C2` | `off-diagonal flavor pi:(1,2,3)->(2, 1, 3); (B1,C2)->(B2,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 024 | `B2__C2` | `L:+1` | `BC_CB::B>C::delta=1` / `B1__C1` | `diagonal flavor pi:(1,2,3)->(2, 3, 1); (B1,C1)->(B2,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 025 | `B2__C3` | `L:+1` | `BC_CB::B>C::delta=0` / `B1__C2` | `off-diagonal flavor pi:(1,2,3)->(2, 3, 1); (B1,C2)->(B2,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 026 | `B2__Ddot1` | `L:+1` | `BD_DB_EXACT_ZERO::B>D` / `B1__Ddot1` | `flavor pi:(1,2,3)->(2, 3, 1); B1->B2; dotted S:dot1->dot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 027 | `B2__Ddot2` | `L:+1` | `BD_DB_EXACT_ZERO::B>D` / `B1__Ddot1` | `flavor pi:(1,2,3)->(2, 3, 1); B1->B2; dotted S:dot1->dot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 028 | `B3__A` | `L:+1,R:-1` | `AB_BA_PROJECT_WARD_RENORMALIZED::B>A` / `B1__A` | `flavor pi:(1,2,3)->(3, 1, 2); B1->B3; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1,1,-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-ab-ba-project-ward-finite-renormalization-exact.json,audits/step5-ab-ba-vector-frame-missing-orbit-exact.json,audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json,audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json,audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json` |
| 029 | `B3__B1` | `L:+1,R:-1` | `BB_OFFDIAGONAL` / `B1__B2` | `flavor pi:(1,2,3)->(3, 1, 2); (B1,B2,C3)->(B3,B1,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=epsilon_312=1; Koszul source-order sign not used` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-sqrt(2)*I,sqrt(2)*I]` | `audits/step5-bb-offdiagonal-family-exact.json` |
| 030 | `B3__B2` | `L:+1,R:-1` | `BB_OFFDIAGONAL` / `B1__B2` | `flavor pi:(1,2,3)->(3, 2, 1); (B1,B2,C3)->(B3,B2,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=epsilon_321=-1; Koszul source-order sign not used` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[sqrt(2)*I,-sqrt(2)*I]` | `audits/step5-bb-offdiagonal-family-exact.json` |
| 031 | `B3__B3` | `L:+1,R:-1` | `BB_DIAGONAL_EXACT_ZERO` / `B1__B1` | `flavor pi:(1,2,3)->(3, 1, 2); B1->B3; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 032 | `B3__C1` | `L:+1` | `BC_CB::B>C::delta=0` / `B1__C2` | `off-diagonal flavor pi:(1,2,3)->(3, 1, 2); (B1,C2)->(B3,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 033 | `B3__C2` | `L:+1` | `BC_CB::B>C::delta=0` / `B1__C2` | `off-diagonal flavor pi:(1,2,3)->(3, 2, 1); (B1,C2)->(B3,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 034 | `B3__C3` | `L:+1` | `BC_CB::B>C::delta=1` / `B1__C1` | `diagonal flavor pi:(1,2,3)->(3, 1, 2); (B1,C1)->(B3,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 035 | `B3__Ddot1` | `L:+1` | `BD_DB_EXACT_ZERO::B>D` / `B1__Ddot1` | `flavor pi:(1,2,3)->(3, 1, 2); B1->B3; dotted S:dot1->dot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 036 | `B3__Ddot2` | `L:+1` | `BD_DB_EXACT_ZERO::B>D` / `B1__Ddot1` | `flavor pi:(1,2,3)->(3, 1, 2); B1->B3; dotted S:dot1->dot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 037 | `C1__A` | `R:+1` | `AC_CA::C>A` / `C1__A` | `flavor pi:(1,2,3)->(1, 2, 3); C1->C1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-1,+1]` | `audits/step5-ac-ca-family-exact.json` |
| 038 | `C1__B1` | `R:+1` | `BC_CB::C>B::delta=1` / `C1__B1` | `diagonal flavor pi:(1,2,3)->(1, 2, 3); (B1,C1)->(B1,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 039 | `C1__B2` | `R:+1` | `BC_CB::C>B::delta=0` / `C2__B1` | `off-diagonal flavor pi:(1,2,3)->(2, 1, 3); (B1,C2)->(B2,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 040 | `C1__B3` | `R:+1` | `BC_CB::C>B::delta=0` / `C2__B1` | `off-diagonal flavor pi:(1,2,3)->(3, 1, 2); (B1,C2)->(B3,C1); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 041 | `C1__C1` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 042 | `C1__C2` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 043 | `C1__C3` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 044 | `C1__Ddot1` | `none` | `NO_DESCENDANT::C>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 045 | `C1__Ddot2` | `none` | `NO_DESCENDANT::C>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 046 | `C2__A` | `R:+1` | `AC_CA::C>A` / `C1__A` | `flavor pi:(1,2,3)->(2, 3, 1); C1->C2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-1,+1]` | `audits/step5-ac-ca-family-exact.json` |
| 047 | `C2__B1` | `R:+1` | `BC_CB::C>B::delta=0` / `C2__B1` | `off-diagonal flavor pi:(1,2,3)->(1, 2, 3); (B1,C2)->(B1,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 048 | `C2__B2` | `R:+1` | `BC_CB::C>B::delta=1` / `C1__B1` | `diagonal flavor pi:(1,2,3)->(2, 3, 1); (B1,C1)->(B2,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 049 | `C2__B3` | `R:+1` | `BC_CB::C>B::delta=0` / `C2__B1` | `off-diagonal flavor pi:(1,2,3)->(3, 2, 1); (B1,C2)->(B3,C2); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 050 | `C2__C1` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 051 | `C2__C2` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 052 | `C2__C3` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 053 | `C2__Ddot1` | `none` | `NO_DESCENDANT::C>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 054 | `C2__Ddot2` | `none` | `NO_DESCENDANT::C>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 055 | `C3__A` | `R:+1` | `AC_CA::C>A` / `C1__A` | `flavor pi:(1,2,3)->(3, 1, 2); C1->C3; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[-1,+1]` | `audits/step5-ac-ca-family-exact.json` |
| 056 | `C3__B1` | `R:+1` | `BC_CB::C>B::delta=0` / `C2__B1` | `off-diagonal flavor pi:(1,2,3)->(1, 3, 2); (B1,C2)->(B1,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 057 | `C3__B2` | `R:+1` | `BC_CB::C>B::delta=0` / `C2__B1` | `off-diagonal flavor pi:(1,2,3)->(2, 3, 1); (B1,C2)->(B2,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 058 | `C3__B3` | `R:+1` | `BC_CB::C>B::delta=1` / `C1__B1` | `diagonal flavor pi:(1,2,3)->(3, 1, 2); (B1,C1)->(B3,C3); K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[1]` | `audits/step5-bc-full-family-raw-projection-exact.json` |
| 059 | `C3__C1` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 060 | `C3__C2` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 061 | `C3__C3` | `none` | `NO_DESCENDANT::C>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 062 | `C3__Ddot1` | `none` | `NO_DESCENDANT::C>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 063 | `C3__Ddot2` | `none` | `NO_DESCENDANT::C>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 064 | `Ddot1__A` | `R:-1` | `AD_DA_FULL::D>A` / `Ddot1__A` | `dotted S:dot1->dot1; Ddot1->Ddot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[2/3,1/3]` | `audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json,audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.json,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.md` |
| 065 | `Ddot1__B1` | `R:-1` | `BD_DB_EXACT_ZERO::D>B` / `Ddot1__B1` | `flavor pi:(1,2,3)->(1, 2, 3); B1->B1; dotted S:dot1->dot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 066 | `Ddot1__B2` | `R:-1` | `BD_DB_EXACT_ZERO::D>B` / `Ddot1__B1` | `flavor pi:(1,2,3)->(2, 3, 1); B1->B2; dotted S:dot1->dot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 067 | `Ddot1__B3` | `R:-1` | `BD_DB_EXACT_ZERO::D>B` / `Ddot1__B1` | `flavor pi:(1,2,3)->(3, 1, 2); B1->B3; dotted S:dot1->dot1; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 068 | `Ddot1__C1` | `none` | `NO_DESCENDANT::D>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 069 | `Ddot1__C2` | `none` | `NO_DESCENDANT::D>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 070 | `Ddot1__C3` | `none` | `NO_DESCENDANT::D>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 071 | `Ddot1__Ddot1` | `none` | `NO_DESCENDANT::D>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 072 | `Ddot1__Ddot2` | `none` | `NO_DESCENDANT::D>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 073 | `Ddot2__A` | `R:-1` | `AD_DA_FULL::D>A` / `Ddot1__A` | `dotted S:dot1->dot2; Ddot1->Ddot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_NONZERO` | `[2/3,1/3]` | `audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json,audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.json,audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.md` |
| 074 | `Ddot2__B1` | `R:-1` | `BD_DB_EXACT_ZERO::D>B` / `Ddot1__B1` | `flavor pi:(1,2,3)->(1, 2, 3); B1->B1; dotted S:dot1->dot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 075 | `Ddot2__B2` | `R:-1` | `BD_DB_EXACT_ZERO::D>B` / `Ddot1__B1` | `flavor pi:(1,2,3)->(2, 3, 1); B1->B2; dotted S:dot1->dot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 076 | `Ddot2__B3` | `R:-1` | `BD_DB_EXACT_ZERO::D>B` / `Ddot1__B1` | `flavor pi:(1,2,3)->(3, 1, 2); B1->B3; dotted S:dot1->dot2; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-bbdiagonal-bd-db-exact-zero.json` |
| 077 | `Ddot2__C1` | `none` | `NO_DESCENDANT::D>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 078 | `Ddot2__C2` | `none` | `NO_DESCENDANT::D>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 079 | `Ddot2__C3` | `none` | `NO_DESCENDANT::D>C` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 080 | `Ddot2__Ddot1` | `none` | `NO_DESCENDANT::D>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |
| 081 | `Ddot2__Ddot2` | `none` | `NO_DESCENDANT::D>D` / `(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2` | `DIRECT_UNIVERSAL_LEMMA; no coefficient transport; K=+1 (no source-slot exchange); color=(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged; sign=+1` | `COMPLETED` | `COMPLETE_EXACT` / `EXACT_ZERO` | `[0]` | `audits/step5-no-descendant-pairs-exact.json` |

## 6. Deterministic counts

$$
81=81_{\mathrm{COMPLETE\_EXACT}}+0_{\mathrm{OPEN}}.
$$

$$
81=29_{\mathrm{EXACT\_NONZERO}}+52_{\mathrm{EXACT\_ZERO}}.
$$

$$
81=81_{\mathrm{COMPLETED}}+0_{\mathrm{UNRESOLVED}}.
$$

Structural census: `56` marked pairs, `25` no-descendant pairs, `1365` directed parent routes.

Verification:

```text
python scripts/step5_global_81_target_blind_orbit_ledger_audit.py --check
python -m unittest tests.test_step5_global_81_target_blind_orbit_ledger
```
