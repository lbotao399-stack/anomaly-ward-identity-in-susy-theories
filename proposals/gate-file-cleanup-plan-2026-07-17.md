# GPT-Pro gate-file cleanup plan — 2026-07-17

Status: `NON_AUTHORITY_PROPOSAL`. Owner-requested: which of the 67 `proposals/gpt-pro-*.md`
gate files are meaningless for producing the readable one-loop bi-letter report, and a safe
removal plan.

## For the report itself: all 67 are non-inputs

The detailed AA-seed report (action → Feynman rules → $\nabla_+W_+^A\nabla_+W_+^B$ triangle →
Wick → amplitude → D-algebra → anomaly sector → integral → result → HT dict) is produced by
reading the **accepted contracts**, not the gate files:

- action: `step-04c` (4C.4);
- Feynman rules: `step-05a` (5A.33 field strengths, 5A.64–5A.74 propagators);
- AA seed derivation: `step-05` §4–5;
- HT dictionary: `step-05` §10;
- consolidated prose: `paper/awi-n4-one-loop.md`.

The gate files are the historical GPT-Pro review ping-pong that *produced* those contracts.
None is a required input for the report. So the honest answer to "which are meaningless":
**for the report, all of them** — read the settled contracts instead.

## For repository hygiene: 56 removable, 11 keep

Reference scan across the whole repo (tests, audits, contracts, manifests, ledger, tasks,
generated, work log):

**KEEP — referenced somewhere (11):**

| File | Referenced by |
|---|---|
| `gpt-pro-workflow-draft-2026-07-10.md` | hash-pinned in `references/manifest.yaml` (the original design blueprint) |
| `gpt-pro-aa-{derivation-correction, final-settlement, standard-feynman}` | asserted to exist by `test_step5_aa_standard_feynman_strictification`; cited as evidence in the AA audit |
| `gpt-pro-ab1-{derivation-correction, final-settlement, standard-feynman}` | asserted to exist by `test_step5_ab1_standard_feynman_strictification` |
| `gpt-pro-ad-da-edgewise-gauge-fp-gate1-response` | `source` field in `audits/step5-ad-da-gauge-family-raw-exact.md` (byte-checked audit) |
| `gpt-pro-bb12-evanescent-cut-gate1-response`, `…-gate2-response` | `source` fields in `audits/step5-bb-offdiagonal-family-exact.json` (byte-checked audit) |
| `gpt-pro-final-one-loop-ht-settlement-gate15-response` | prose mention in `Current work日志.md` (not CI) |

**REMOVE — zero references, superseded by the accepted contracts (56):**

| Channel | Count | Superseded by |
|---|---|---|
| `aa-*` gate prompt/response (gate1, 2v/2w/2x/2y, 3, 4) | 17 | `step-05` §4–5, kept AA triad |
| `ab1-*` gate prompt/response | 17 | `step-05` §9, kept AB1 triad |
| `ab-ba-*` (gate8–14) | 12 | `step-05` §9 (AB/BA settlement) |
| `ac-ca-*` | 2 | `step-05` §7 |
| `ad-da-*` (prompt + full-sd-link gate2) | 3 | `step-05` §7; kept response is the audit source |
| `bb12-*` prompts | 2 | `step-06`/`step-05`; kept responses are audit sources |
| `final-*` gate15-prompt | 1 | `step-05` §10 |
| `g3-*` gate12 (measure equivalence) | 2 | `step-05` §9 |

These 56 are pure gate ping-pong: intermediate prompt/response pairs, each superseded by the
final settlement they fed into and by the accepted contract sections. The new Derivation-first
law (`AGENTS.md`) forbids this per-gate proliferation going forward.

## Plan (phased, git-reversible)

- **Phase 1 (zero-risk, this commit):** `git rm` the 56 zero-reference files. No test, audit,
  manifest, or contract references them; the `verify` gate is unaffected. Recoverable from
  Git history.
- **Phase 2 (later, one-line fixes):** remove `final-…gate15-response` after excising its
  mention in `Current work日志.md` (or delete that stray root-level work log, which is itself
  uncatalogued clutter).
- **Phase 3 (verify-then-remove, optional):** the 3 audit-`source` responses (ad-da, bb12×2).
  Their audits are byte-compared; deleting the file leaves the `source` string intact so the
  byte-check still passes, but confirm the audit *regenerator* does not stat the file before
  removing. Low value; can be left indefinitely.
- **Not removed:** the 6 test-asserted consolidated triads and the manifest-pinned blueprint —
  these are the "≤2 review files per obligation" the reformed law actually permits, held as
  the per-channel review record. A future obligation may consolidate the 6 to 2 (needs test
  edits).

Net: `proposals/` goes from 76 → 20 files, of which the gate residue is 11 (down from 67).
