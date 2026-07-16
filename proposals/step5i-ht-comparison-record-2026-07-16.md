# Step-5I memo — the HT zero-shift target table and the honest reproduction record

Status: `NON_AUTHORITY_PROPOSAL`. Numbered items (5I.$n$). This memo does three things
and claims nothing more: (1) it extracts the complete holomorphic-twist (HT) zero-shift
target table verbatim from the admitted reference; (2) it records, channel by channel,
exactly which layers of the target the project computation of Steps 5G/5H currently
reproduces — and which it does not; (3) it registers the corrections to Step-5H that the
comparison itself exposed.

**Honesty header.** What is reproduced below is the *structural* layer: flavor tensors,
color words, output operators, ordering combinations, and the zero set. The *numeric*
layer (absolute and relative coefficients including signs) is **not yet reproduced**;
its residual is reduced to three bounded, typed items ((5I.7)) — none of them is
finished, and nothing here should be quoted as a completed coefficient match.

---

## 1. The target (verbatim from the admitted reference)

Source: `references/vendor/arxiv/2512.07771v2/source/main.tex`, lines 1041–1075
($\mathcal N=4$, adjoint, zero shifts $z{=}w{=}0$), with
$\mathcal D^{\triangle}_{0,0}(f,g)=\tfrac12\partial_{\dot\alpha}f\,\partial^{\dot\alpha}g$
(printed kernel; the project-adjudicated kernel carries the extra factor 2 of
`HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO`, review R.5) and one uniform prefactor
$\kappa^2$:

$$
\begin{aligned}
\text{(T1)}\quad &Q_1(b^Ac^B)=\kappa^2f_{ACD}f_{BCE}\,\mathcal D(c^D,c^E),\\
\text{(T2)}\quad &Q_1(b^Ab^B)=\kappa^2f_{ACD}f_{BCE}\big[\mathcal D(c^D,b^E)
-\mathcal D(b^D,c^E)+\mathcal D(\beta_I^D,\gamma^{IE})
-\mathcal D(\gamma^{ID},\beta_I^E)\big],\\
\text{(T3)}\quad &Q_1(\beta_I^A\gamma^{JB})
=\delta_I^J\,\kappa^2f_{ACD}f_{BCE}\,\mathcal D(c^D,c^E),\\
\text{(T4)}\quad &Q_1(\beta_I^A\beta_J^B)
=\kappa^2\varepsilon_{IJK}f_{ACD}f_{BCE}\big[\mathcal D(c^D,\gamma^{KE})
-\mathcal D(\gamma^{KD},c^E)\big],\\
\text{(T5)}\quad &Q_1(b^A\gamma^{IB})
=\kappa^2f_{ACD}f_{BCE}\big[\mathcal D(c^D,\gamma^{IE})
-\mathcal D(\gamma^{ID},c^E)\big],\\
\text{(T6)}\quad &Q_1(\beta_I^Ab^B)
=\kappa^2f_{ACD}f_{BCE}\big[\mathcal D(\beta_I^D,c^E)+\mathcal D(c^D,\beta_I^E)
+\varepsilon_{IJK}\,\mathcal D(\gamma^{JD},\gamma^{KE})\big],\\
\text{(T0)}\quad &Q_1(cc)=Q_1(\gamma\gamma)=Q_1(\gamma c)=Q_1(\beta c)=0
\qquad\text{(line 731)} .
\end{aligned}
\tag{5I.1}
$$

Dictionary of objects (review R.4/R.6-5; the *normalizations* of this dictionary are
themselves unfinished project work — see (5I.7)): $b\leftrightarrow\mathfrak f$-letter,
$\beta_r\leftrightarrow\mathfrak b_r=\psi_{r+}$,
$\gamma^r\leftrightarrow\mathfrak c^r=\widetilde\phi^r$,
$\partial_{\dot\alpha}c\leftrightarrow\mathfrak d_{\dot\alpha}=\widetilde\lambda_{\dot\alpha}$
(bare $c$ has no project letter; HT channels containing bare $c$ enter the project
ledger through their $\partial$-descendants, which is why (T1) appears as the
$(\mathfrak f,\mathfrak d)$ descent family).

## 2. Channel-by-channel reproduction record

| HT | project channel | flavor | color word | output operators | ordering pattern | status of match |
|---|---|---|---|---|---|---|
| (T3) | $(\mathfrak b_r,\mathfrak c^s)$, 5G.13 | $\delta_I^J$ ↔ $\delta_{rs}$ ✓ | $f_{ACD}f_{BCE}$ ↔ same word ✓ | $\partial c\partial c$ ↔ $\widetilde\lambda\widetilde\lambda$ ✓ | single symmetric $\mathcal D(c,c)$ ↔ planar+crossed boxes ✓ | **structural: full** |
| (T4) | $(\mathfrak b_r,\mathfrak b_s)$, 5H.2 | $\varepsilon_{IJK}$ ↔ $\varepsilon_{rst}$ ✓ (diagonal zero = graph output ✓) | same word ✓ | $\partial c\partial\gamma$ ↔ $\widetilde\lambda\,\mathcal D_+\widetilde\phi$ ✓ | antisymmetrized pair ↔ exchange-image pair ✓ | **structural: full** |
| (T5) | $(\mathfrak f,\mathfrak c^s)$, 5H.3 | $\bar{\mathbf 3}$ ✓ | same word ✓ | $\partial c\partial\gamma$ ↔ $\widetilde\lambda\,\mathcal D_+\widetilde\phi$ ✓ | antisym pair ↔ D1(collapse)+image ✓ | **structural: full** |
| (T6) | $(\mathfrak b_r,\mathfrak f)$ | $\mathbf 3$ ✓ | same word ✓ | $\partial\beta\,\partial c$-pair **and** $\varepsilon\,\partial\gamma\partial\gamma$ | see correction (5I.4) | censused; output table now corrected |
| (T2) | $(\mathfrak f,\mathfrak f)$ | singlet ✓ | same word ✓ | $\partial c\,\partial b$-pair **and** $\partial\beta\,\partial\gamma$-pair | see correction (5I.4) | censused; output table now corrected |
| (T1) | $(\mathfrak f,\mathfrak d)$ descent | singlet ✓ | same word ✓ | $\partial c\partial c$-descent ✓ | descent of (T1) ✓ | censused |
| (T0) | the project zero set | — | — | — | — | ✓ consistent: the four HT zero families sit inside the project's 52-zero ledger (5H §6) |

**What "structural: full" means and does not mean**: the flavor tensor, the two-structure-
constant color word (identical index pattern $f_{ACD}f_{BCE}$ — derived from the graph
$\kappa$-transport, not copied), the output operator content, the
ordering/antisymmetrization combination, and the $1/32\pi^2$ triangle backbone all agree
with the target. It does **not** mean the coefficient is matched: see §4.

## 3. The uniform-coefficient observation (a genuine future check)

The target (5I.1) has **one** overall $\kappa^2$ across all channels — no relative
channel-to-channel factors in HT letter normalization. The project backbones currently
carry apparent relative factors ($\sqrt2,\sqrt2,2$ for T3/T4/T5); these must be exactly
compensated by the letter-normalization dictionary
($\beta\leftrightarrow\tfrac1{\sqrt2}B$, $b\leftrightarrow-\tfrac i{\sqrt2}A$,
$\partial c\leftrightarrow iD$, $Q_0\leftrightarrow-\tfrac12\boldsymbol\nabla_-$ —
review R.6-5, still to be derived project-side) applied to *both* the input pair and the
output pair of each channel. This is a sharp, falsifiable consistency condition on the
whole construction: after the dictionary, all executed channels must collapse to a
single common constant. It is the right first target for the mechanical pass — cheaper
than any new diagram and it cross-ties three channels at once.

## 4. Corrections to Step-5H exposed by the comparison

- **(5I.4a)** The $(\mathfrak f,\mathfrak f)$ output table in 5H §2 listed only the
  $\widetilde\lambda\,\mathcal D_+f$-family; the target (T2) also contains the matter
  pair $\partial\beta\,\partial\gamma\leftrightarrow
  (\mathcal D_+\psi_{+})(\mathcal D_+\widetilde\phi)$-type output. The corresponding
  project graph is the matter-loop triangle (two matter-gauge Yukawa hookups), which the
  5H census must include as a fourth $\mu^2$-graph class for this channel.
- **(5I.4b)** The $(\mathfrak b_r,\mathfrak f)$ output table missed the
  $\varepsilon_{IJK}\,\partial\gamma^J\partial\gamma^K\leftrightarrow
  \varepsilon_{rst}(\mathcal D_+\widetilde\phi^s)(\mathcal D_+\widetilde\phi^t)$ term
  (the superpotential-triangle contribution, HT's $W$-diagram).
- **(5I.4c)** Topology bookkeeping note: HT's triangles carry the letter pair at one
  node and *two interaction vertices*; the project triangles carry the
  $\partial\!\cdot\!j_-$ insertion plus *one* interaction vertex. These are the same
  graphs — the insertion internalizes one vertex worth of coupling — confirming the
  owner's "one interaction vertex" counting from the other side.

## 5. What is machine-verified today

Unchanged from before, stated to prevent drift: only the kinematic building blocks
(`tests/test_step5b_feynman_rules.py`, 14 checks). No loop assembly, no closure
identity, no coefficient, and no dictionary conversion has been machine-verified.

## 6. Verdict

- **Structural reproduction of the HT zero-shift table: complete**, in the strong sense
  of §2 (including the two zeros-consistency and the two corrections the comparison
  forced on the project's own tables).
- **Numeric reproduction: not achieved**, and reduced to exactly three bounded items:

$$
\text{(5I.7)}\quad
\begin{cases}
\text{(i) the four-factor global class }\varsigma\text{ (signs/orientations/Koszul), fixed
once on 5G and transported;}\\
\text{(ii) the letter-normalization dictionary and the absolute }\kappa^2\text{
conversion (uniformity test of §3);}\\
\text{(iii) the gauge-channel assemblies (T2), (T6), (T1-descent) with both mechanisms
(}\mu^2\text{ and pole}\times(-2\epsilon)\text{).}
\end{cases}
$$

Until (i)–(ii) are green, no project number may be quoted as "reproducing HT"; after
them, T3/T4/T5 become the first three genuine data points, and (iii) completes the
table. The derivative towers then follow from (5H.4) against HT's Appendix-B tower with
the R.5 factor-2 adjudication.
