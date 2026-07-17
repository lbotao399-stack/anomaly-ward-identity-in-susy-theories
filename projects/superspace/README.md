# Project 1 — Superspace supergraph Feynman diagrams

The completed project. One-loop anomaly of the Schwinger–Dyson identity for BPS letters in
Euclidean $\mathcal N=4$ SYM, computed by $\mathcal N=1$ superspace supergraphs; compared to
the holomorphic twist.

**Status: one-loop accepted.** 81 ordered letter pairs (29 nonzero, 52 zero), coefficient
$\lambda_1=\hbar g^2/16\pi^2$, full derivative tower matching Budzik–Kulp after the printed
factor-2 correction. Anomaly = evanescent DRED cutting-rule failure $\mu_\ell^2/(D_0D_1D_2)$,
master $1/32\pi^2$. Open frontier: the covariant-completion theorem (all $\ge4$-gon graphs =
gauge-covariant dressing of the triangle) and the two-loop $Q_2$.

- `readable/paper.md` — the full human-readable derivation (imports `../notation/`).
- `readable/` (to add) — per-pair 11-point calculation reports (the AA seed with full Wick →
  amplitude → D-algebra → anomaly sector → integral).
- `machine/` — the isolated verifiers/audits/tests (Phase 2 relocation of the legacy
  `scripts/`, `audits/`, `tests/`, `generated/` for step-05/05a/06).

Legacy sources: `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`,
`step-05a-…md`, `step-06-covariant-completion.md`,
`proposals/covariant-completion-theorem-memo-2026-07-16.md`.
