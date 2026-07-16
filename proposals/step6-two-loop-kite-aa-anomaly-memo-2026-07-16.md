# Step-6 seed: the two-loop 日 (kite) supergraph for $\boldsymbol\nabla_-(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^A\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^B)$ — anomaly sector

Status: `NON_AUTHORITY_PROPOSAL` (exploratory two-loop seed, owner-authorized in the
2026-07-16 session: *"探索超空间的 2-loop 修正 … 只 focus 在这一个日字图的 anomaly
sector"*). Nothing here modifies the accepted one-loop settlement. Numbered equations
are (K.$n$). Every project-locked input is cited by contract tag; declared scheme
choices are labeled **[D3]**, **[D4]** and surfaced in §10 as the session decision list.

**External-target boundary (stated up front).** The HT source (arXiv:2512.07771v2,
`references/vendor/arxiv/2512.07771v2/source/main.tex`) contains **no explicit two-loop
coefficient**. Its two-loop content is structural: the loop tower $\bm Q = Q_{\rm free} +
Q_{\rm tree} + \hbar Q_1 + \hbar^2 Q_2 + \dots$ (`main.tex:150`), the consistency
condition $Q_1^2 + \{Q_0,Q_2\} = 0$ (`main.tex:220,398`), the statement that the two-loop
bracket is supported on the unique two-loop Laman graph — the 4-vertex/5-edge $K_4-e$
graph, i.e. the 日/kite topology (`main.tex:539-561,648`) — and the truncation
expectation: *"for an operator of length $n$ the possible corrections truncate at at most
$Q_{n+1}$, but based on computing explicit integrals we expect them to truncate at
$Q_{n-1}$"* (`main.tex:222`). For the length-2 word studied here the HT expectation is
therefore $Q_2(\text{length-2}) = 0$. **That expectation is what this memo reproduces
from the project's superspace/DRED side, for the canonical 日 graph:** the anomaly-sector
integrals are individually nonzero, finite and local, but the assembled local output
vanishes identically (§8), by a mechanism the one-loop settlement does not have (a
single-letter output with a single external momentum).

---

## 1. Conventions (all locked; citations only)

Operative frame = `audits/step5-canonical-superfield-ww-seed.md` §1–§3:

$$
\epsilon^{+-}=1,\quad \epsilon_{+-}=-1,\quad D^+=D_-,\quad D^-=-D_+,\quad
D^2=2D_-D_+,\quad
\{D_a,\bar D_{\dot a}\}=2\mathsf p_{a\dot a},\quad
\mathsf p_{a\dot a}=-i(\sigma_E^m)_{a\dot a}p_m,
\tag{K.1}
$$

with $\sigma_E^m=(-i\sigma^1,-i\sigma^2,-i\sigma^3,\mathbf 1)$ (1.51),
$\sigma_E^m\bar\sigma_E^n+\sigma_E^n\bar\sigma_E^m=2\delta^{mn}$ (1.54). Canonical
dictionary $\mathcal V_P=2gv$, $\mathcal W_P=gW_{\rm can}$;
$W_{(1)a}=-\tfrac14\bar D^2D_av$, $\widetilde W_{(1)\dot a}=-\tfrac14 D^2\bar D_{\dot a}v$
(from 5A.33). Fermi–Feynman propagator (seed §3, F.4):

$$
\langle v^A(p,\theta_1)\,v^B(-p,\theta_2)\rangle
=\hbar\,\frac{\kappa^{AB}}{p^2}\,\delta^4(\theta_1-\theta_2).
\tag{K.2}
$$

Loop saturation $\delta^4(\vartheta_{12})D^2\bar D^2\delta^4(\vartheta_{12})
=16\,\delta^4(\vartheta_{12})$ (F.6); fewer than the maximal $D^2\bar D^2$ on a closed
$\vartheta$ loop gives zero. DRED ledger as in the settlement §1: $d=4-2\epsilon$,
finite spin words four-dimensional, propagator inverses $d$-dimensional, single
evanescent scalar $\mu_\ell^2:=\bar\ell^2-\ell_d^2$, and the locked anchor

$$
\mu^{2\epsilon}\!\int\!\frac{d^d\ell}{(2\pi)^d}\,
\frac{\mu_\ell^2}{(\ell^2+\Delta)^3}=\frac1{32\pi^2}+O(\epsilon)
\qquad(\Delta\text{-independent}).
\tag{K.3}
$$

**[D3] Two-loop evanescent extension.** Both loop momenta split, with the three
invariants $\mu_\ell^2=-\tilde\ell^2$, $\mu_k^2=-\tilde k^2$,
$\mu_{\ell k}:=-\tilde\ell\cdot\tilde k$; external momenta are strictly hatted
($\mu_p^2=0$); evanescent angular averages use
$\langle\tilde\ell^\mu\tilde\ell^\nu\rangle=\tfrac{\tilde\ell^2}{2\epsilon}
\tilde\delta^{\mu\nu}$, and all $O(\epsilon)$ terms of sub-integrals are kept because
they can meet $1/\epsilon$ from the co-loop. This is the minimal extension of the locked
one-loop ledger; it is a scheme declaration, not a derived statement.

## 2. The word and its tree identity

The insertion is the AA letter channel of the settlement, one loop order up:
$A=\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+$, word $A^AA^B$, Ward operator
$\boldsymbol\nabla_-$. Tree descendants (settlement §3):

$$
\boldsymbol\nabla_-(A^AA^B)\Big|_{\rm tree}
=\big[-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times C_s)\big]^AA^B
+A^A\big[-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times C_s)\big]^B .
\tag{K.4}
$$

At one loop the accepted result is $\boldsymbol\nabla_-(A^AA^B)|_{1\text{-loop}}
=\lambda_1\mathbb F^{AB}{}_{DE}\,\Delta(A,A)^{DE}$ with $\lambda_1=\hbar g^2/16\pi^2$ and
$\Delta(A,A)=\langle D,A\rangle-\langle A,D\rangle+\sum_r(\langle B_r,C_r\rangle-\langle
C_r,B_r\rangle)$ — a **two-letter** output word carrying **two independent** external
momenta. This memo computes the $\hbar^2g^4$ (two-loop) correction from one fixed graph.

Canonical insertion (seed §5), total incoming momentum $-p$, insertion point
$\vartheta_0$ not integrated:

$$
\mathcal I^{AB}_{(2)}
=D_-\big[(K_+v^A)(K_+v^B)\big],
\qquad K_+=-\tfrac14 D_+\bar D^2D_+,
\qquad D_-K_+=-\tfrac18 D^2\bar D^2D_+ .
\tag{K.5}
$$

Project conversion: $\boldsymbol\nabla_-(A^AA^B)_P=g^2\,\mathcal I^{AB}_{(2)}+O(g^3)$ on
the insertion side; each canonical output letter reconverts with one factor of $g$, so
the graph below is $\hbar^2g^3$ canonical $=\hbar^2g^4$ in project letters.

## 3. The graph

The unique two-loop Laman topology is $K_4$ minus one edge (HT Figure 1, third graph):
four vertices, five edges, $E=2V-3$, loop number $2$ — the 日 graph. Canonical routing
(**the** graph of this memo): the insertion $\mathcal O=\mathcal I_{(2)}^{AB}$ at one
degree-2 corner (both $W$-legs contracted, no operator nonlinearity), three cubic gauge
vertices $X_1,X_2,X_3$; the single uncontracted leg at the opposite degree-2 corner
$X_3$ is the output letter.

```
                O = ∇₋(∇₊W₊ᴬ ∇₊W₊ᴮ)(p, θ₀)
               ╱  ╲
        ℓ  D₁ ╱    ╲ D₂  p−ℓ
             ╱      ╲
       X₁(θ₁)─ D₃ ──X₂(θ₂)          日 = K₄ − edge(O,X₃)
             ╲  k   ╱
   ℓ−k  D₄   ╲     ╱ D₅  p−ℓ+k
              ╲   ╱
               X₃(θ₃) ──── output leg  (letter jet, momentum p out)
```

$$
\begin{aligned}
&\text{lines: } L_1:O\!\to\!X_1\ (\ell),\quad L_2:O\!\to\!X_2\ (p-\ell),\quad
L_3:X_1\!\to\!X_2\ (k),\\
&\qquad\ \ L_4:X_1\!\to\!X_3\ (\ell-k),\quad L_5:X_2\!\to\!X_3\ (p-\ell+k);\\
&D_1=\ell^2,\ D_2=(p-\ell)^2,\ D_3=k^2,\ D_4=(\ell-k)^2,\ D_5=(p-\ell+k)^2 .
\end{aligned}
\tag{K.6}
$$

TikZ (for the paper layer):

```tex
\begin{tikzpicture}[scale=1.4, every node/.style={font=\small}]
  \coordinate (O)  at (0, 1.2);   \coordinate (X3) at (0,-1.2);
  \coordinate (X1) at (-1.2, 0);  \coordinate (X2) at (1.2, 0);
  \draw (O) -- (X1) node[midway, above left] {$\ell$};
  \draw (O) -- (X2) node[midway, above right] {$p-\ell$};
  \draw (X1) -- (X2) node[midway, above] {$k$};
  \draw (X1) -- (X3) node[midway, below left] {$\ell-k$};
  \draw (X2) -- (X3) node[midway, below right] {$p-\ell+k$};
  \draw[dashed] (X3) -- (0,-2.1) node[below] {output letter, $p$};
  \filldraw (X1) circle (1.5pt) node[left]  {$X_1$};
  \filldraw (X2) circle (1.5pt) node[right] {$X_2$};
  \filldraw (X3) circle (1.5pt) node[right] {$X_3$};
  \filldraw (O)  circle (2.2pt) node[above] {$\;\;\mathcal O=\boldsymbol\nabla_-(A^AA^B)$};
\end{tikzpicture}
```

## 4. The amplitude read off the graph

Vertices (seed §4, re-derived in the vertex audit, all three legs quantum here):

$$
S_{(3),+}=-\frac{ig}2\,c_{CUE}\!\int\! d^dx\,d^4\theta\,
\big(-\tfrac14\bar D^2D^av^E\big)(D_av^C)\,v^U,
\qquad
S_{(3),-}=+\frac{ig}2\,c_{CUE}\!\int\! d^dx\,d^4\theta\,
\big(-\tfrac14 D^2\bar D_{\dot a}v^E\big)(\bar D^{\dot a}v^C)\,v^U,
\tag{K.7}
$$

each entering as $(-1/\hbar)S_{(3),\chi}$ ($\tau_E=-1/\hbar$, 5A.63); vertex-label Wick
weight $=1$ (seed §5). The complete pre-D-algebra amplitude of the fixed labeled graph is

$$
\boxed{
\begin{aligned}
\Gamma^{AB;G}_{\text{日}}(p)
={}&\hbar^2\Big(\frac{g}{2}\Big)^{3}
\sum_{\mathfrak p\in\{\mathfrak a,\mathfrak b\}}\ 
\sum_{\chi_1,\chi_2,\chi_3=\pm}\ \sum_{\text{slots}}
(\pm i)^3\,
\mathcal K^{ABG}_{\rm color}(\text{slots})\,(-1)^{\kappa(\text{slots})}\\
&\times
\mu^{4\epsilon}\!\!\int\!\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}\,
\frac{1}{D_1D_2D_3D_4D_5}
\int\! d^4\theta_1d^4\theta_2d^4\theta_3\;
\Big[\mathcal O^{(\mathfrak p)}_1\delta^4(\theta_{01})\Big]
\Big[\mathcal O^{(\mathfrak p)}_2\delta^4(\theta_{02})\Big]\\
&\times
\Big[\mathcal D^{(1)}\delta^4(\theta_{12})\Big]
\Big[\mathcal D^{(2)}\delta^4(\theta_{13})\Big]
\Big[\mathcal D^{(3)}\delta^4(\theta_{23})\Big]\;
\mathcal D^{\rm out}v^G(p,\theta_3),
\end{aligned}}
\tag{K.8}
$$

where $\mathcal O^{(\mathfrak a)}_1=-\tfrac18D^2\bar D^2D_+$,
$\mathcal O^{(\mathfrak a)}_2=-\tfrac14D_+\bar D^2D_+$ (and $1\leftrightarrow2$ for
$\mathfrak b$), and per slot assignment each internal line's two ends carry the vertex
D-words $\{-\tfrac14\bar D^2D^a,\ D_a,\ 1\}$ ($\chi=+$) or
$\{-\tfrac14D^2\bar D_{\dot a},\ \bar D^{\dot a},\ 1\}$ ($\chi=-$), with
$\mathcal K_{\rm color}=$ the ordered product of $c_{C_iU_iE_i}$ contracted through the
five $\kappa^{XY}$ of (K.2), free indices $A,B$ (insertion) and $G$ (output leg), and
$(-1)^{\kappa}$ the Koszul sign of (5A.61)–(5A.62). Momentum-power counting: eleven $D$'s
and ten $\bar D$'s enter; eight saturate the two $\theta$-loops (F.6), the output jet
retains up to three, and the remaining pairs convert to momenta through (K.1) — five
$\mathsf p$-factors in the numerator, of which two are consumed by the loop tensor
reduction and three survive as external $\mathsf p(p)$-factors in the local output.

## 5. D-algebra: reduced result

<!-- ENGINE-RESULTS-SLOT -->

## 6. Anomaly-sector identification

Exactly as at one loop, the reduced numerator contains four-dimensional squares
$\bar r_e^{\,2}$ of line momenta generated by the spin-word algebra ($D^2\bar D^2$ pairs
collapsing on a line, $\sigma$-word traces), sitting over $d$-dimensional denominators.
The occurrence-wise cutting identity (settlement §5) applied per marked edge $e$ of the
kite,

$$
\frac{\bar r_e^{\,2}}{D_1D_2D_3D_4D_5}
-\frac1{\prod_{j\neq e}D_j}
=\frac{\mu_{r_e}^2}{D_1D_2D_3D_4D_5},
\tag{K.9}
$$

splits every such term into a **cut/contact row** (one denominator cancelled — the
Schwinger–Dyson/EOM sector, which participates in the tree Ward identity (K.4)) plus the
**cutting failure**. At two loops the failure terms close on the three evanescent
invariants of **[D3]**:

$$
\text{anomaly sector}
=\mu^{4\epsilon}\!\!\int\!\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}\,
\frac{N_{\ell}\,\mu_\ell^2+N_k\,\mu_k^2+N_{\ell k}\,\mu_{\ell k}
+N_{\ell\ell kk}\,\mu_\ell^2\mu_k^2+\dots}
{D_1D_2D_3D_4D_5}
\;+\;(\text{contact daughters}),
\tag{K.10}
$$

with $N_\bullet$ polynomials in $\mathsf p(\ell),\mathsf p(k),\mathsf p(p)$ carrying the
$\sigma$-words and the output jet. Single-$\mu$ terms whose co-loop is divergent (e.g.
$M_2$ of §7) are not by themselves local; they combine with the
$\hat\delta-\delta_4=-\breve\delta$ metric mismatches of the contact rows exactly as in
the one-loop settlement ($p^\rho\breve\delta^{mn}T_{m\rho n}=-2\epsilon\,\sigma\!\cdot\!p$
meeting the $1/\epsilon$), and the assembled anomaly sector is finite and local — a
polynomial in $p$ times the output jet.

## 7. The kite $\mu$-masters by Feynman parameters

**Insertion lemma** (from the locked rule $\int\mu_k^2f=((4-d)/d)\int k^2f$, HK.21, and
$J_n$, settlement §4):

$$
\boxed{\ 
L(n,\Delta):=\mu^{2\epsilon}\!\int\!\frac{d^dk}{(2\pi)^d}
\frac{\mu_k^2}{(k^2+\Delta)^n}
=\epsilon\,\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(n-1-d/2)}{\Gamma(n)}\,\Delta^{\,d/2+1-n}\ }
\tag{K.11}
$$

(verified symbolically for $n=2,3,4$; $n=3$ reproduces the anchor (K.3) exactly:
$L(3,\Delta)=\tfrac1{32\pi^2}\Gamma(1+\epsilon)\big(4\pi\mu^2/\Delta\big)^\epsilon$ —
note the $O(\epsilon)$ part is kept, per [D3]). The masters over the kite family
$K:=D_1D_2D_3D_4D_5$ of (K.6), through $O(\epsilon^0)$ at $p^2$ fixed:

<!-- MASTERS-RESULTS-SLOT -->

The pattern that matters structurally: every **double-evanescent** master
($\mu_\ell^2\mu_k^2$-type) is finite and a pure local polynomial in $p^2$ — the two-loop
analog of (K.3); the archetype, evaluated by inner-loop-first Feynman parametrization, is

$$
M_1=\mu^{4\epsilon}\!\!\int\!\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}
\frac{\mu_\ell^2\,\mu_k^2}{D_1D_2D_3D_4D_5}
=\frac1{32\pi^2}\!\int_0^1\!\!dx\,L\big(2,x(1-x)p^2\big)+O(\epsilon)
=-\frac{p^2}{3072\,\pi^4}+O(\epsilon).
\tag{K.12}
$$

## 8. Assembly and the vanishing theorem

**Theorem (single-letter kinematic vanishing).** Every local output of the graph of §3
is, after the loop integrations, a scalar word built from (i) factors
$\mathsf p_{a\dot a}(p)$ of the **single** external momentum $p$, (ii) one output jet
carrying at most one free spinor index (the irreducible fermionic jets are
$D_av,\ \bar D_{\dot a}v,\ D^2\bar D_{\dot a}v,\ \bar D^2D_av$), with total undotted
charge $+\tfrac32$, dimension $\tfrac92$, odd Grassmann parity. Every such word vanishes
identically. *Proof:* dotted contractions between two $\mathsf p(p)$'s obey
$\epsilon^{\dot a\dot b}\mathsf p_{a\dot a}\mathsf p_{b\dot b}\propto p^2\epsilon_{ab}$,
so a $(+,+)$ pair gives $p^2\epsilon_{++}=0$ and a $(+,-)$ pair strips one $+$ and one
$-$ label at the cost of $p^2$; recursively any word reduces to
$\mathsf p_{+\dot a_1}\cdots\mathsf p_{+\dot a_r}(\text{jet})$ with $r\geq2$ and at most
one jet index to absorb one $\dot a_i$; at least one $(+,+)$ dotted pair contraction is
then forced, hence zero. Charge $+\tfrac32$ forbids $r\leq1$. $\square$

<!-- ASSEMBLY-RESULTS-SLOT -->

Consequently:

$$
\boxed{\ 
\boldsymbol\nabla_-\big(A^AA^B\big)\Big|_{\text{2-loop, 日 (tip routing)}}^{\rm anomaly}
=0
\ }
\tag{K.13}
$$

— not because the anomaly-sector integrals vanish (they are individually nonzero,
(K.12)), but because the unique available output tensor structures
$\mathsf p_{+(\dot a}\mathsf p_{+\dot b}\mathsf p_{+\dot c)}\times(\text{jet})$ admit no
nonzero scalar contraction, and independently because the tip-日 color word
$\mathcal C_3{}^{AB}{}_G$ is antisymmetric under $A\leftrightarrow B$ against an
$A\leftrightarrow B$-symmetric kinematic sum. This holds for the whole derivative tower
$\boldsymbol\nabla_-[(P^{\mathbf u}A)^A(P^{\mathbf v}A)^B]$ on this routing (still one
output letter, one external momentum).

## 9. HT comparison

The HT side has no printed $Q_2$ number to compare against; the sharp statements it does
make are all reproduced by (K.13) on this graph:

1. the two-loop bracket lives on the $K_4-e$ Laman topology — the graph computed here;
2. $Q_2$ on a length-2 word is expected to vanish (truncation at $Q_{n-1}$,
   `main.tex:222`); (K.13) is the superspace/DRED image of that expectation for the AA
   word, derived rather than assumed;
3. consistency $Q_1^2+\{Q_0,Q_2\}=0$ is not violated: it constrains $Q_2$ on longer
   words, where the 日 topology has two-letter outputs and the vanishing theorem of §8
   does **not** apply (§10).

## 10. Boundary, census, and session decision list

This memo computes **one** labeled graph. At the same topology and order the full
census contains (classification in `scratchpad`/census verification artifact, to be
promoted with any future Step-6 obligation):

- ghost-line routings of the tip 日 (FP words 5A.58–5A.60) — same single-letter output,
  killed by the same §8 theorem;
- routings with one quartic vertex (BCH $V^4$, matter $(\operatorname{ad}V)^2$, ghost
  quartics) — **two-letter outputs; §8 does not kill these**; open;
- matter/superpotential triangles ($n=1$ matter words with $\mathscr U_4$) — open per
  routing class;
- insertion-side nonlinear routings ($O(g)$ BCH/connection expansion of
  $A=\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+$, insertion at a degree-3 corner) —
  **two-letter outputs; open**;
- one-loop$\times$one-loop normal-product ($\mathscr Z$-letter) insertions — scheme
  layer, open.

Decisions surfaced this session (per the derivation-first law):

- **[D3]** the two-loop evanescent ledger of §1 (minimal extension of the locked
  one-loop DRED ledger; three invariants $\mu_\ell^2,\mu_k^2,\mu_{\ell k}$; common
  evanescent subspace; keep $O(\epsilon)$ of sub-integrals);
- **[D4]** the canonical routing choice (tip insertion, all-vector lines, three cubic
  BCH vertices) as "the" 日 graph of the AA channel; all other routings quarantined to
  the census list above.

## 11. Verification artifacts

Two independent D-algebra engines (explicit 16-generator Grassmann representation vs.
sequential transfer/rewrite-rule reduction), both gated on (i) the D-algebra anchors of
§1 and (ii) exact reproduction of the locked one-loop canonical WW seed
(`audits/step5-canonical-superfield-ww-seed.md` §§5–9: the 8-row table, $w_D=2$,
$\Gamma_{T,A}$ with $L_1=2k+q$, $L_2=2k+p+2q$); a master-integral derivation with
numeric cross-checks; an independent color reduction with explicit $su(2)/su(3)$
numerics; an adversarial pass on the §8 theorem (including the
$\mu_{\ell k}^2/(2\epsilon)$ escape route); and a census critic. Artifact inventory and
outcomes:

<!-- VERIFICATION-RESULTS-SLOT -->
