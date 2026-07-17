# Anomaly Ward Identity in SUSY Theories

Canonical proof repository for the AWI program: the one-loop (and now two-loop) anomaly of
the Schwinger–Dyson identity for BPS letters in Euclidean $\mathcal N=4$ super-Yang–Mills,
derived in $\mathcal N=1$ superspace and compared to the holomorphic-twist result of
Budzik–Kulp (arXiv:2512.07771).

**Result (accepted, `origin/main`):** for every ordered pair of the four letter families
$A=\nabla_+\mathcal W_+$, $B_r=\nabla_+\Phi_r$, $C_r=\widetilde\Phi_r$,
$D_{\dot a}=\widetilde{\mathcal W}_{\dot a}$,

$$\nabla_-(L_i^A L_j^B)\big|_{\text{1-loop}}=\lambda_1\,\mathbb F^{AB}{}_{DE}\,\Delta(L_i,L_j)^{DE},\qquad \lambda_1=\tfrac{\hbar g^2}{16\pi^2}.$$

29 of 81 ordered pairs are nonzero, 52 vanish; the full holomorphic-derivative tower matches
the twist prediction after correcting one printed factor of 2. The anomaly is the evanescent
failure of the DRED cutting rule, $\mu_\ell^2/(D_0D_1D_2)$ with master $1/32\pi^2$.

---

## Read this first (the durable core)

Everything below is load-bearing and human-readable. Start here; the rest of the tree is
verification scaffolding or history.

| What | Where |
|---|---|
| **Paper** (evergreen, full derivation) | [`paper/awi-n4-one-loop.md`](paper/awi-n4-one-loop.md) |
| **The one-loop result** | [`contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`](contracts/foundations/step-05-euclidean-n4-awi-one-loop.md) |
| **Notation core** | [`contracts/foundations/`](contracts/foundations/) step-01, 02a, 04, 04c |
| **Weinberg–Srednicki dictionary** | [`contracts/dictionaries/`](contracts/dictionaries/) |
| **Super Feynman rules / BV–BRST** | [`contracts/foundations/step-05a-…md`](contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md) |
| **Open frontier** (2-loop / covariant completion) | [`contracts/foundations/step-06-covariant-completion.md`](contracts/foundations/step-06-covariant-completion.md), [`proposals/covariant-completion-theorem-memo-2026-07-16.md`](proposals/covariant-completion-theorem-memo-2026-07-16.md) |
| **Governance** | [`AUTHORITY.md`](AUTHORITY.md), [`AGENTS.md`](AGENTS.md) |

## Proof-obligation ledger

35 obligations in [`ledger/proof_obligations.json`](ledger/proof_obligations.json): **33
ACCEPTED, 2 open.**

State machine: `SPECIFIED → FROZEN → RULES_DERIVED → ENUMERATED → EVALUATED → CUT_COMPLETE
→ RENORMALIZED → WARD_CLOSED → COHOMOLOGY_PROJECTED → ACCEPTED`.

**Foundations, all ACCEPTED:** step-01 (SUSY commutator) · 02a (flat superspace) · 02b/02c
(superconformal) · 03a–03d (gauge–chiral action, components, vector rep, BV–BRST path
integral) · 04/04a/04b/04c (extended SYM, N=1/2/4) · 05a (component BV–BRST supergraph
grammar) · **05 (the Euclidean N=4 one-loop settlement)**.

**Open:**
- `CONTRACT-STEP-03E-N1-FEYNMAN-RULES` — blocked on a Lorentzian vector-cycle mismatch
  (`BLOCKED_STEP3D_LC_VECTOR_CYCLE`); Lorentzian-only, off the Euclidean critical path.
- `CONTRACT-STEP-06-COVARIANT-COMPLETION` — current work; Phase 0 gives 25 PASS / 56 BLOCKED
  on the chain-map action (`BLOCKED_PHASE0_CHAIN_MAP_ACTION_NOT_LOCKED`).

## Directory map

**Load-bearing:**
- `contracts/` — the derivations (15 foundations + 2 dictionaries). The legal layer.
- `paper/` — the evergreen human-readable paper.
- `ledger/` — obligation states.
- `references/` — hash-pinned vendored sources (Weinberg, Srednicki, HT arXiv, Superspace/1001);
  see [`references/manifest.yaml`](references/manifest.yaml).
- `mirror/` — write-only Notion mirror map (17 pages published).

**Scaffolding (regenerable / evidence, not primary):**
- `audits/` (201) — per-step exact-verification JSON, regenerated in CI.
- `scripts/` (141) — the exact verifiers (stdlib + sympy).
- `tests/` (88) — the `verify` gate.
- `generated/` (21) — machine artifacts (graph IR, ledgers); marked generated.
- `channels/` (4) — the ec/es/lc/ls channel stubs (unused; slated for removal).

**History (safe to ignore for new work):**
- `proposals/` (76) — design/review notes. **67 are GPT-Pro per-gate files** from the
  pre-reform workflow; the current law (`AGENTS.md`, Derivation-first) caps external review
  at two files per obligation. The load-bearing proposals are: `covariant-completion-theorem-memo`,
  `step5b-euclidean-feynman-rules-memo`, `step5-independent-physics-review`,
  `step5-spot-check-verdict`, `step5-census-review-final-verdict`, `workflow-repair`,
  `workflow-slim-obligation-spec`. The rest are archival.
- `tasks/archive/` — completed task packets.

## Known cleanup debt (see `proposals/workflow-slim-obligation-spec-2026-07-16.md`)

Policy-test slimming; CI fast/slow split; removal of the unused channel system and
dual-signature contracts; consolidation of the 67 GPT-Pro gate files; per-channel IR
provenance. None blocks the accepted result.

## Authority

Only Git objects reachable from `origin/main` with a green `verify` are authoritative. No
historical repository, Notion page, local note, chat transcript, or external file is a
computational input. Notion is a write-only human-readable mirror.
