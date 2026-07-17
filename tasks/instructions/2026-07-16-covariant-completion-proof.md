# Codex work order: prove the covariant completion theorem (Step-6 obligation)

Owner-issued 2026-07-16. Source memo:
`proposals/covariant-completion-theorem-memo-2026-07-16.md` (equations (T.1)–(T.9);
markings [PROVED-HERE]/[MACHINE-CHECK-k]/[OPEN]). Read `AGENTS.md` (Derivation-first law)
and `AUTHORITY.md` first. Everything below is an honest-loop-computation mandate: no
coefficient may be imported from the memo's predictions, from HT, or from literature;
memo predictions are regression targets only, compared after your derivation is sealed.

## Goal

Prove, at contract grade, that every one-loop supergraph with the letter-pair insertion and
$n\ge4$ legs contributes exactly the gauge-covariant dressing of the settled triangle
bracket (T.1) — converting graph-census completeness into a symmetry theorem. Deliverable:
ONE derivation memo promoted to `contracts/foundations/step-06-covariant-completion.md`,
at most ten exact checks (check budget law), a paper update in the same PR, and PR bodies
that state formulas, not check counts.

## Phase 0 (run first, loop-integral-free): the consistency condition

Verify (T.9), $\{Q_0,Q_1\}=0$, on all 81 settled rows: apply the tree descendants
(settlement §3: $\boldsymbol\nabla_-A=-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times C_s)$,
$\boldsymbol\nabla_-B_r=-2\mathscr E_{\widetilde r}-\sqrt2\varepsilon(C\times C)$,
$\boldsymbol\nabla_-C=\boldsymbol\nabla_-D=0$) and the residual supercharges $q_r$
(settlement §6) to each ledger output $\Delta(L_i,L_j)$, expand with the Koszul rules
(5A.61–5A.62), and confirm closure. This is exact letter algebra — sympy over the
9-letter free superalgebra with $SU(3)$ and color indices symbolic. Failure of any row is a
P0 finding against the settled ledger; report immediately.

## Phase 1 (the decisive computation): the transverse box coefficient

Object: the order-$g^3$ one-loop family for $\boldsymbol\nabla_-(A^AA^B)$ with two
uncontracted outputs and ONE additional external background leg (momentum $k$, color $F$,
connection component $\Gamma_{+\dot a}$).

1. Build the graph family target-blind from the locked words: vertices (5A.49–5A.63),
   propagators (5A.68–5A.74), occurrence-resolved rows exactly as the settlement §4–§5 did
   for the triangle. Include: soft leg on each of the three internal lines, on each cubic
   vertex, and on the insertion words (letter-dressing class). No topology may be dropped
   without citing which memo lemma kills it.
2. Apply the cut identity per marked line (settlement §2), then the threshold filter: every
   numerator sector below loop-degree $2(n-3)$ is discarded citing (T.2)/Lemma 1 with its
   $(n,a)$; every super-threshold sector is either shown to cancel or classified EOM/TD
   citing Lemma 3 — this is [MACHINE-CHECK-1].
3. The sub-eikonal parts of the new vertex must be *derived* to fall below threshold
   ([MACHINE-CHECK-3]): produce the edge-tagged D-algebra degree table for the 5A.52 cubic
   word attached to a soft external leg. If any sub-eikonal sector survives, it is a
   finding, not an inconvenience — evaluate it.
4. Evaluate surviving sectors with the masters: $M_n^{(n-3)}\to\tfrac1{32\pi^2}$ (T.3) and
   the doubled-line $\tfrac{\widehat\delta^{mn}}4\cdot\tfrac1{32\pi^2}$ (T.8). Assemble the
   transverse output in the basis $(t_1,t_2,t_W)$ of memo §6:
   slot-1 commutator, slot-2 commutator, and the field-strength primitive
   $\mathcal W_+$-insertion structure.
5. Longitudinal check: reproduce the telescoping result of memo §5 mechanically (it is
   already proved; your derivation must agree line by line).
6. Only after your $(t_1,t_2,t_W)$ is computed and committed, compare against the
   prediction $(-i\lambda_1,-i\lambda_1,0)$. Agreement: CCT box level established.
   Disagreement in $t_W$: a genuine invisible primitive — P0, stop and report with the full
   trace.

Historical method reference (optional): Bardeen, Phys. Rev. 184 (1969) 1848 evaluated the
non-abelian AVVV box and AVVVV pentagon and showed they complete $\partial A\partial A$
into $F\widetilde F$; Adler–Bardeen (1969) and Wess–Zumino (1971) fixed the structure
cohomologically. If you want the paper as a working reference, vendor it first through a
`REFERENCE_IMPORT` task with every claim classified `EXTERNAL_METHOD_PRECEDENT`; adopt the
method skeleton only, never a coefficient.

## Phase 2: uniqueness (S3) as $Q_0$-cohomology

Classify covariant local operators at the anomaly's quantum numbers that vanish at
$V_{\rm B}=0$ (candidates: single-$\mathcal W_+$ insertions at output dimension
$\tfrac92+1$; for pentagons also $\mathcal W^2$ and $\boldsymbol\nabla\mathcal W$ at $+2$).
Then impose (T.9): keep only $Q_0$-cocycles, and quotient by coboundaries (removable by
normal-product redefinition). Machine-enumerate the finite basis ([MACHINE-CHECK-2]). CCT
needs this cohomology to be empty (or exactly matched by Phase-1 output).

## Phase 3: covariance of the generating trace (S2 re-host)

State and prove as a contract lemma: (a) the one-loop pair-insertion functional is
$\tfrac12\operatorname{STr}[\mathcal I G_0(1+HG_0)^{-1}]$ whose $H$-expansion members are
the $n$-gons; (b) conjugation invariance of STr under background gauge transformations —
two lines; (c) Loc$_{\mu^2}$ (the threshold extraction) commutes with the covariance, using
Lemmas 1–3. Cross-cite, do not import, the closed PR #46 rooted-trace material and the
#71-admitted heat-kernel lemma.

## Phase 4: the induction $n\ge5$

Prove: given box-level CCT, background-gauge covariance recursively determines every
$n\ge5$ transverse coefficient from level $n-1$ (the $R$-conjugation Ward identity of the
trace). One clean lemma; no new integrals.

## Phase 5 (independent): ghost typed-absence rows

Transcribe as a target-blind typed row ([MACHINE-CHECK-6]): from the FP words 5A.58–5A.60,
(i) ghost-vertex spectator legs are never letters; (ii) closing a ghost loop at $g^2$
consumes all insertion ports leaving no letter-bilinear output; (iii) ghost self-energy
dressings are $g^4$. Same for the NK external measure (field-independent in slice D1).
This closes the ghost bucket of the seventeen open census candidates.

## Acceptance (state-machine honest)

- Phase 0 passes on 81/81 rows (or reports a P0);
- Phase 1's $(t_1,t_2,t_W)$ derived target-blind, sealed before comparison, with every
  discarded sector citing its lemma and $(n,a)$;
- Phase 2's cohomology list machine-enumerated and either empty or reconciled;
- Phases 3–4 as contract lemmas with proofs a physicist can read start to finish;
- Phase 5 rows recorded;
- exactly one derivation memo, at most ten exact checks, paper updated in the same PR,
  PR body states the derived formulas.

## Honesty rules (binding)

No coefficient from memo predictions, HT, or literature enters any derivation. Every
dropped graph or sector cites the lemma that kills it. If any computation contradicts the
memo, the computation wins — report the discrepancy as a finding rather than adjusting
either side. Check counts are not results.
