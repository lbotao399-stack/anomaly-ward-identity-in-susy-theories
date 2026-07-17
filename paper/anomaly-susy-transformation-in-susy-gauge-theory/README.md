# Anomaly SUSY Transformation in SUSY Gauge Theory

**Core showcase paper of the AWI repository.**

- Source: `main.tex` + `sections/*.tex` (compile: `latexmk -pdf main.tex`)
- Compiled PDF: [`anomaly-susy-transformation-in-susy-gauge-theory.pdf`](anomaly-susy-transformation-in-susy-gauge-theory.pdf)

The paper presents, in a single self-contained submittable format, the one-loop
anomalous supersymmetry Ward identity of the BPS-letter sector of Euclidean
$\mathcal N=4$ super-Yang–Mills, organized as the project's five parallel work
streams:

1. **Conventions** (Sections 2–3): Lorentzian and Euclidean spinors, Weyl and
   Majorana fermions, covariant derivatives, $\theta$-expansions, chiral and
   vector representations, BV–BRST quantization, dimensional reduction.
2. **Superspace Feynman diagrams** (Section 4): the complete accepted result —
   cutting-failure identity, universal coefficient $\hbar g^2/(16\pi^2)$, all 81
   ordered channels (29 nonzero / 52 zero), the closed-form derivative-tower kernel.
3. **Component Feynman diagrams** (Section 5): the accepted bottom-projection
   channel and the named open items.
4. **Heat kernel** (Section 6): the exact semigroup lemmas and the current blocker.
5. **Holomorphic twist** (Section 7): the exact 81/81 comparison with
   Budzik–Kulp (arXiv:2512.07771) after the factor-two correction, and what the
   agreement does and does not prove.

Authority note: the legal mathematical layer remains `contracts/` and the
accepted audits on `origin/main`; this paper is a human-readable presentation
using standard physics notation, not a new authority. The evergreen
proof-format document remains `paper/awi-n4-one-loop.md`.
