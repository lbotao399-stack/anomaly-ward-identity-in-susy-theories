# Project 4 — Is the holomorphic twist legitimate

The foundational question the other three projects lean on when they "compare to HT": is the
holomorphic twist of $\mathcal N=4$ SYM a legitimate quantum operation — does the twisted
theory faithfully compute the physical BPS-sector anomaly, and under what scheme? This project
argues quantum legality rather than assuming it.

**Status: partial.** The classical twist is derived (`step-04d`); the quantum twist and its
obstructions are set up (`step-04e`, the N=1 HT BV program on the now-closed branches). The
external target (Budzik–Kulp, arXiv:2512.07771) is vendored and admitted `EXTERNAL_TARGET_ONLY`.
The open core is the quantum-legality proof: whether the twist commutes with the regulator and
BV pushforward, i.e. whether the HT $Q_1/Q_2$ equal the physical superspace result — which
Project 1 confirms at one loop for all 81 channels, giving strong evidence the twist is legal.

- `readable/` (to add) — the classical twist, the quantum-legality argument, and the
  obstruction ledger (HT-GAP-01…07).
- `machine/` — twist/BV verifiers (Phase 2).

Legacy sources: `contracts/foundations/step-04d`, `step-04e`,
`references/vendor/arxiv/2512.07771v2`, the N=1 HT reference imports.
