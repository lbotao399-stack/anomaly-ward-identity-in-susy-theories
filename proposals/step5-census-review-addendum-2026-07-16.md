# Step-5 adversarial census review — status addendum (2026-07-16)

Status: `NON_AUTHORITY_PROPOSAL`, review evidence. Companion to
`proposals/step5-spot-check-verdict-2026-07-16.md` (S1–S5) and the merged settlement.

## What ran

An eight-sector adversarial "name a missing topology" review (independent per-sector
enumeration of every order-$g^2$ topology from the locked vertex/insertion words, diffed
against the committed census, with three-lens refutation of candidates). Four sectors
completed; four aborted on external session limits before running, as did the refutation
stage. The review is therefore **partially complete**; a resumed run is scheduled and its
verdict supersedes this addendum.

## Affirmative results (completed sectors)

- **AA pure-gauge sector**: both triangle orientations verified as distinct ordered outputs
  with no reflection double count; of the four (source-attachment × mark) rows exactly two
  are anomaly-bearing by the rank-two loop-numerator criterion, matching
  `audits/step5-aa-gauge-marked-occurrence-recount.md`.
- **Insertion-expansion sector (AA)**: the full resolvent
  $\langle I_2\rangle-\langle I_1S_3\rangle-\langle I_0S_4\rangle+\tfrac12\langle
  I_0S_3^2\rangle$ is enumerated with per-term disposal; no omission found.
- **AB/BA and BB**: independent port-matching enumeration reproduces exactly the 9 directed
  parent triangles (6 TGM + 1 TMM + 2 TMH) of the committed audits; census confirmed for the
  anomaly-bearing 1PI sector.
- **AC/CA and BC/CB**: the BC occurrence orbit {E-KIN, E-POT, X-POT} proven complete — an
  X-KIN row is *correctly absent* because the explicit descendant term of
  $\boldsymbol\nabla_-B_r$ is purely potential after the Euler rewrite; an X-KIN row would
  double-count.

## Open candidates (recorded, unadjudicated)

Twelve candidate omissions were raised and **not yet refuted or confirmed** (the refutation
stage never ran). By class: (i) ghost/FP/NK typed absence rows for the A-marked channels
(the settlement proves the physical result but does not everywhere display the ghost-sector
disposal as typed rows); (ii) machine-census encoding honesty (an allegation that
`generated/step5/physical-graph-ir.json` graph objects are template-stamped from the WW
seed; note `generated/step5/graph-census.json` does carry per-channel kernels — the
allegation is specifically about the IR artifact); (iii) three specific Wick routings
(BC-TMG-TAIL, AC-SOURCE-CYCLE-TAIL, BB unsplit source-double-bridge with vertex tail) and a
mixed-chirality superpotential triangle class, alleged missing as *rows* from the committed
artifacts.

## Why the merge proceeded before closure

1. CI green (165 tests) plus the S1–S5 independent verification of every load-bearing
   identity and the seed chain.
2. **The independence argument**: all 81 ordered channels, including 2025 derivative-tower
   coefficients, agree exactly with an external calculation performed in a *different*
   regulator and formalism (holomorphic point-splitting vs DRED supergraphs). A contributing
   topology missing from the Project census would generically break this agreement; the
   residual scenario — both calculations omitting the same contribution — is not credible
   for regulator-dependent graph accounting.
3. Every candidate therefore concerns, at most, absence-proof *presentation* (typed rows)
   or machine-artifact honesty, not the physical coefficients.

## Disposition

The resumed review adjudicates all twelve candidates. Any survivor becomes a finding of the
follow-up obligation (`proposals/workflow-slim-obligation-spec-2026-07-16.md`), with
expected impact limited to additional typed-zero/ghost-disposal rows and artifact repair.
