# Workflow repair proposal — 2026-07-16

Status: `NON_AUTHORITY_PROPOSAL` (proposal surface only; adopts no formula, changes no contract).
Author: Claude (session of 2026-07-16), at the owner's request to diagnose and repair the
Codex + GPT Pro workflow.

Companion document: `proposals/step5-independent-physics-review-2026-07-16.md`
(independent verification of the central Step-5 physics claims).

---

## 1. Diagnosis: where the program is actually stuck

The mathematics is not stuck. The pipeline that turns mathematics into *authority* is stuck.
Five distinct failure points, in causal order:

### 1.1 The authority gate has never opened (review starvation)

`AUTHORITY.md` grants authority only to commits reachable from `origin/main` with a green
`verify` run. But the actual Step-5 settlement lives in **draft PR #61**
(`agent/step5-complete-one-loop-anomaly`): 366 files, ~513,000 inserted lines, of which the
human-readable derivation contract is 1,402 lines (≈0.3%). Nine draft PRs are open, three of
them stacked chains (#50→#55→#59, #46→#47/#49). The sole reviewer is the owner; a PR whose
body is check-counts ("141750 lifted checks") cannot be reviewed, so it is never merged, so
it never becomes authoritative, so the next session starts again from a `main` that still
says `SPECIFIED`. This is the loop that produces "海量奇怪的测试而推导变少" — the only
mergeable-looking unit of progress left is more scaffolding.

Evidence of the drift on `main` itself: over the last 20 non-merge commits, hand-written
derivation markdown vs. scripts+tests+audits ≈ **1 : 2.3**. On PR #61 the ratio is ≈ 1 : 365.

### 1.2 CI has never been able to pass on the settlement branch

`verify.yml` installs only `poppler-utils`. PR #61's audit scripts import `sympy`; the CI run
fails with 44 × `ModuleNotFoundError: No module named 'sympy'` (run 29395121406). The PR body's
"165 tests passed" was a local run. So even a willing reviewer could not merge: the mandatory
authority gate is red for infrastructure reasons, not mathematical ones.

**Fixed on this branch**: `verify.yml` now installs `sympy` + `PyYAML`; `pyproject.toml`
declares them. PR #61 must rebase onto (or cherry-pick) this to go green.

### 1.3 Four standing blockers are *decisions*, not derivations

`step-05a` (5A.80) records four blockers. None of them is an unsolved math problem; each is a
convention choice waiting for a one-paragraph user authorization, and they have been carried
as BLOCKED states across many sessions:

| blocker | what it actually is | recommended resolution |
|---|---|---|
| `BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED` | Step-3D demands a *local* gauge kernel `\mathcal Y_R`; the Fermi–Feynman kernel is provably nonlocal (5A.79). Contradiction between an acceptance clause and the standard scheme. | Authorize a scoped exception: for the **Euclidean perturbative slice only**, define the propagators directly by Gaussian averaging with `\mathcal Y_{E,\rm FF}` (equivalently: adopt the FF kernel `K_V^{\rm tot}=-\frac h2 p^2\mathbf 1` as the scheme definition). Keep 3D locality for the nonperturbative BV statement. This is what PR #61 de facto does ("fixed FF graph representative"). |
| `BLOCKED_STEP5A_NK_BRANCH_UNSELECTED` | Choice among the four Step-3D (3D.96b) Nielsen–Kallosh realizations. | Select the **external measure-only branch** and record the one-loop lemma that the NK factor is field-independent in the FF slice and cancels in normalized letter correlators at this order. (One page of derivation, then the blocker is closed.) |
| `BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED` | The Fourier/all-incoming/DRED/loop-measure ledger was never locked on `main`. | PR #61's contract §1 *is* this ledger (Fourier `e^{ip\cdot x}`, all-incoming, `d=4-2\epsilon`, `\widehat\delta/\breve\delta` vs `\bar\delta/\widetilde\delta` double representation, `\mu_\ell^2` axiom). Review §1 in isolation and lock it. |
| `BLOCKED_STEP3D_LC_VECTOR_CYCLE` | A **Lorentzian** temporal-line/cycle mismatch (`2\pi\hbar\,\delta(p_L^2)\mathfrak h_L^{-1}`). Irrelevant to the Euclidean N=4 target. | **Quarantine**: move to its own Lorentzian obligation; remove from the Euclidean Step-5 blocker list at the next contract change. Note `tests/test_repository_policy.py` pins the exact blocker list, so this removal must touch the test, the ledger, and 5A §5A.12 in the same reviewed commit. |

### 1.4 The task specification is a monolith and the policy test has fossilized it

`tasks/CURRENT.yaml` demands, in one obligation: notation ledger + DRED contract + total
bidirectional source dictionary + Euler operators + 16 channel classes + deterministic Wick
enumerator + graph IR + renderer + D-algebra engine + all 81 pairs + full HT round trip +
six audits. No session can move that through one state transition, so sessions emit
scaffolding instead. Worse, `test_repository_policy.py::test_step5_contract_registration`
hardcodes `len(acceptance)==16` and specific substrings — the law now enforces the monolith's
*shape*. Task redesign therefore requires a deliberate commit that changes the task, the
ledger hash, and the test together (see §3).

### 1.5 Scope creep while the gate is shut

While Step 5 sat unreviewed: PR #47 opened a **two-loop Step 6 compiler**, and PRs #50/#55/#59
opened an entire **N=1 holomorphic-twist BV program**. Each is legitimate future work; opening
them now multiplies the review debt at interest.

---

## 2. Repair actions taken on this branch

1. **CI dependency fix** (`.github/workflows/verify.yml`, `pyproject.toml`): `sympy`, `PyYAML`
   installed in the gate. This unblocks *every* pending branch's verify run.
2. **`AGENTS.md` — new "Derivation-first law"**: rebalances the rigor law so that the primary
   artifact is a human-readable derivation memo and machine checks are subordinate, bounded,
   and equation-anchored. (Text in `AGENTS.md`; rationale here.)
3. **Independent physics review** of PR #61's core claims
   (`proposals/step5-independent-physics-review-2026-07-16.md`): the cutting-failure identity,
   the `1/(32\pi^2)` evanescent master integral, the `-2\epsilon` trace identity, the 29/52
   selection-rule census, and the holomorphic-twist factor-2 adjudication are **independently
   re-derived and confirmed**; a bounded five-item spot-check list is given for the remaining
   trust surface. This converts "unreviewable 513k lines" into "five half-day checks".
4. **Deliberate non-action**: this branch does **not** touch `tasks/CURRENT.yaml`,
   `ledger/proof_obligations.json`, or any contract, because PR #61 modifies them and a
   parallel edit would force a three-way merge. Task restructuring is specified in §3 for
   execution *after* the #61 decision.

## 3. Recommended sequence for the owner

1. **Merge this branch** (CI fix + law + review memos). Everything here is
   infrastructure/proposal surface; nothing changes mathematical authority.
2. **Decide PR #61 by bounded spot-check, not line-by-line reading.** Rebase it on the fixed
   CI; run the five spot checks from the review memo (§6 there). If they pass: merge #61 as
   the Step-5 settlement — this simultaneously locks the DRED ledger (blocker c), the FF slice
   (blocker a, de facto), and archives the GPT-Pro gates as review evidence. If a spot check
   fails: the memo pinpoints which section of the 1,402-line contract is wrong; fix that
   section, not the scaffolding.
3. **Then restructure the task queue** in one commit: replace the monolithic CURRENT with the
   remaining obligations only (whatever the #61 review leaves open — e.g. NK lemma, blocker-d
   quarantine, mirror), updating `test_step5_contract_registration` and the ledger
   `task_sha256` in the same commit.
4. **Triage the PR stack** (recommendations):
   - **#61** — the candidate settlement; handle per step 2.
   - **#46 / #49** — superseded by #61 (typed-IR pipeline without results vs. completed
     results). Close with a salvage note; the reusable kernel-inversion identities already
     live in 5A §5A.10.
   - **#47 (Step-6 two-loop)** — close; reopen only after Step 5 is `ACCEPTED` (focus law).
   - **#50 / #55 / #59 (N=1 holomorphic-twist BV program)** — park as a named future program;
     close the PRs, keep the branches. Not on the Step-5 critical path.
   - **#42 (Step 3E)** — keep draft, explicitly labeled Lorentzian-only; it is quarantined
     with blocker (d) and does not block Euclidean Step 5.
   - **#27** — superseded by merged Step-4 work; verify nothing unique remains, then close.
5. **Going forward**, run the loop the Derivation-first law prescribes: one obligation at a
   time; memo first; checks anchored to memo equations; GPT-Pro review enters as *two* files
   per obligation, not seventy; a PR is sized for a human evening.

## 4. Division of labor (Codex ↔ GPT Pro ↔ owner), restated

- **GPT Pro**: derivation drafts and adversarial review of *memos* (physics reasoning). Its
  output enters the repo as vendored reference or as the two consolidated review files.
- **Codex**: turns an accepted memo into the repository artifact — the contract file, the
  *small* set of equation-anchored exact checks, the mirror payload. It does not invent
  acceptance criteria, gates, or IR layers that no memo equation requires.
- **Owner**: makes convention/scheme decisions the moment they surface (the §1.3 table is the
  current decision list), and reviews memos, never check-counts.
