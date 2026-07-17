# Step-6: the two-loop 日 (kite) supergraph for $\boldsymbol\nabla_-(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^A\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^B\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^C)$ — anomaly sector

Status: `NON_AUTHORITY_PROPOSAL` (exploratory two-loop seed, owner-authorized in the
2026-07-16/17 sessions: *"N=4 SYM 中，能有 2-loop 的修正必须是 3-letters operator …
纯 gauge sector 的 $\nabla_-(\nabla_+W_+^A\nabla_+W_+^B\nabla_+W_+^C)$，日字图 …
只 focus 在这一个图的 anomaly sector"*). Nothing here modifies the accepted one-loop
settlement. Numbered equations are (K3.$n$). Conventions, the DRED two-loop ledger
extension **[D3]**, the $\mu^2$-insertion lemma, and the length-2 vanishing baseline are
shared with the companion memo
`proposals/step6-two-loop-kite-aa-anomaly-memo-2026-07-16.md` (cited as **K.$n$**).

**External-target boundary.** The HT source (arXiv:2512.07771v2) prints no explicit
two-loop coefficient. Its sharp two-loop statements are: (i) the two-loop bracket
$Q_2=\tfrac1{3!}\{\mathcal I,\mathcal I,\mathcal I,\mathcal O\}$ is supported on the
unique two-loop Laman topology $K_4-e$ = 日 (`main.tex:539-561,648`); (ii)
$Q_1^2+\{Q_0,Q_2\}=0$ (`main.tex:220,398`); (iii) corrections on a length-$n$ word are
expected to truncate at $Q_{n-1}$ (`main.tex:222`) — so the **first nonvanishing** $Q_2$
sits on length-3 words, and the length-2 channel must vanish. The companion memo proves
the length-2 vanishing on this topology (single output letter, single external momentum
— kinematic theorem K §8, machine-enumerated). This memo computes the first genuinely
nonzero case: the pure-gauge length-3 word $A^AA^BA^C$, $A=\boldsymbol\nabla_+
\boldsymbol{\mathcal W}_+$, on the 日 graph.

---

## 1. Conventions

All of K §1 (seed-audit frame (K.1), FF propagator (K.2), saturation F.6, DRED anchor
(K.3), two-loop evanescent ledger **[D3]**). Canonical dictionary $\mathcal V_P=2gv$,
$W_{(1)a}=-\tfrac14\bar D^2D_av$, $\widetilde W_{(1)\dot a}=-\tfrac14D^2\bar D_{\dot a}v$;
cubic vertices $S_{(3),\pm}$ of (K.7).

## 2. The word

$$
\mathcal I^{ABC}_{(3)}
=D_-\big[(K_+v^A)(K_+v^B)(K_+v^C)\big],
\qquad K_+=-\tfrac14D_+\bar D^2D_+,\qquad
D_-K_+=-\tfrac18D^2\bar D^2D_+,
\tag{K3.1}
$$

three $\boldsymbol\nabla_-$-placements $\mathfrak a,\mathfrak b,\mathfrak c$ (Leibniz on
three bosonic legs). Project conversion: $\boldsymbol\nabla_-(A^AA^BA^C)_P
=g^3\,\mathcal I^{ABC}_{(3)}+O(g^4)$; two canonical output letters reconvert with $g^2$;
the graph below is $\hbar^2g^3$ canonical $=\hbar^2g^4$ in project letters — the
two-loop order.

Quantum numbers of the insertion: dimension $\tfrac{13}2$, undotted charge
$+\tfrac52$, odd Grassmann parity. Two-letter output words consistent with this
bookkeeping and with a pure-gauge routing (output jets are $v$-jets only):

$$
\mathsf p^3\text{-dressed }\langle D,A\rangle\text{-family}:\quad
\dim=\tfrac32+2+3=\tfrac{13}2,\quad
\text{charge}=0+1+\tfrac32=\tfrac52\ \checkmark
\tag{K3.2}
$$

(the $\mathsf p^4\langle B,C\rangle$ matter family cannot appear on all-vector lines).
Because the two output letters carry **independent** momenta $q_1,q_2$, the length-2
kinematic vanishing theorem (K §8) does not apply:
$\epsilon^{\dot a\dot b}\mathsf p_{+\dot a}(q_1)\mathsf p_{+\dot b}(q_2)\neq0$.
This channel is where HT's expected truncation $Q_{n-1}$ first permits — and the
consistency condition $Q_1^2+\{Q_0,Q_2\}=0$ generically demands — a nonzero $Q_2$.

## 3. The graph

$K_4-e$ with the insertion at a degree-3 corner; the missing edge is
$X_a$–$X_b$; the 日 rectangle is $O,X_a,X_{\rm mid},X_b$ with middle bar $O$–$X_{\rm mid}$:

```
            q₁ ⇐ (output letter, X_a)          (output letter, X_b) ⇒ q₂
                     ╲                              ╱
                    X_a(θ₁) ══════════════════ X_b(θ₂)      ← NO edge (K₄−e)
                     │   ╲                    ╱   │
              D₁, ℓ  │     ╲ D₄, q₁−ℓ  D₅, q₂−k ╱ │  D₂, k
                     │       ╲              ╱     │
                    O(θ₀) ─────── D₃ ────── X_mid(θ₃)
                            Q−ℓ−k  (middle bar)

   O = ∇₋(∇₊W₊ᴬ ∇₊W₊ᴮ ∇₊W₊ᶜ)(Q = q₁+q₂ incoming)
```

equivalently, as the 日 character: rectangle $O$–$X_a$–$X_b$–$X_{\rm mid}$ with the
middle bar $O$–$X_{\rm mid}$; $O$ and $X_{\rm mid}$ have degree 3, $X_a$ and $X_b$
degree 2 (one uncontracted output leg each).

$$
\begin{aligned}
&L_1:O\!\to\!X_a\ (\ell),\quad
L_2:O\!\to\!X_b\ (k),\quad
L_3:O\!\to\!X_{\rm mid}\ (Q-\ell-k),\\
&L_4:X_{\rm mid}\!\to\!X_a\ (q_1-\ell),\quad
L_5:X_{\rm mid}\!\to\!X_b\ (q_2-k),\qquad Q:=q_1+q_2,\\[2pt]
&D_1=\ell^2,\quad D_2=k^2,\quad D_3=(Q-\ell-k)^2,\quad
D_4=(q_1-\ell)^2,\quad D_5=(q_2-k)^2 .
\end{aligned}
\tag{K3.3}
$$

TikZ (paper layer):

```tex
\begin{tikzpicture}[scale=1.5, every node/.style={font=\small}]
  \coordinate (O)  at (0,0);  \coordinate (M)  at (0,-1.6);
  \coordinate (Xa) at (-1.5,-0.8); \coordinate (Xb) at (1.5,-0.8);
  \draw (O)--(Xa) node[midway,above left] {$\ell$};
  \draw (O)--(Xb) node[midway,above right] {$k$};
  \draw (O)--(M)  node[midway,right] {$Q-\ell-k$};
  \draw (M)--(Xa) node[midway,below left] {$q_1-\ell$};
  \draw (M)--(Xb) node[midway,below right] {$q_2-k$};
  \draw[dashed] (Xa)--(-2.4,-0.8) node[left] {$q_1$};
  \draw[dashed] (Xb)--(2.4,-0.8) node[right] {$q_2$};
  \filldraw (O) circle (2.2pt) node[above] {$\mathcal O=\boldsymbol\nabla_-(A^AA^BA^C)$};
  \filldraw (M) circle (1.5pt) node[below] {$X_{\rm mid}$};
  \filldraw (Xa) circle (1.5pt) node[above left] {$X_a$};
  \filldraw (Xb) circle (1.5pt) node[above right] {$X_b$};
\end{tikzpicture}
```

## 4. The amplitude read off the graph

$$
\boxed{
\begin{aligned}
\Gamma^{ABC;DE}_{\text{日}}(q_1,q_2)
={}&\hbar^2\Big(\frac{g}{2}\Big)^{3}
\sum_{\mathfrak p\in\{\mathfrak a,\mathfrak b,\mathfrak c\}}
\sum_{\pi\in S_3}\ \sum_{\chi_{\rm mid},\chi_a,\chi_b=\pm}\ \sum_{\text{slots}}
(\pm i)^3\,\mathcal K^{ABC;DE}_{\rm color}\,(-1)^{\kappa}\\[2pt]
&\times\mu^{4\epsilon}\!\!\int\!\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}\,
\frac{1}{D_1D_2D_3D_4D_5}\,
\int\!d^4\theta_1d^4\theta_2d^4\theta_3\\[2pt]
&\times\Big[\mathcal O^{(\mathfrak p,\pi)}_{1}\delta^4(\theta_{01})\Big]
\Big[\mathcal O^{(\mathfrak p,\pi)}_{2}\delta^4(\theta_{02})\Big]
\Big[\mathcal O^{(\mathfrak p,\pi)}_{3}\delta^4(\theta_{03})\Big]\\[2pt]
&\times\Big[\mathcal D^{(\rm mid)}\delta^4(\theta_{31})\,\delta^4(\theta_{32})\Big]\,
\mathcal D^{\rm out}_a v^D(q_1,\theta_1)\;
\mathcal D^{\rm out}_b v^E(q_2,\theta_2),
\end{aligned}}
\tag{K3.4}
$$

where $\pi$ assigns the color-labeled insertion legs $\{A,B,C\}$ to the lines
$\{L_1,L_2,L_3\}$; the leg hit by $\boldsymbol\nabla_-$ (placement $\mathfrak p$)
carries $-\tfrac18D^2\bar D^2D_+$ and the other two carry $-\tfrac14D_+\bar D^2D_+$;
each cubic vertex distributes $\{-\tfrac14\bar D^2D^a,\ D_a,\ 1\}$ ($\chi=+$) or
$\{-\tfrac14D^2\bar D_{\dot a},\ \bar D^{\dot a},\ 1\}$ ($\chi=-$) over its three legs
(at $X_a,X_b$ one leg is the uncontracted output);
$\mathcal K_{\rm color}$ is the ordered product $c_{\cdot\cdot\cdot}c_{\cdot\cdot\cdot}
c_{\cdot\cdot\cdot}$ contracted through the five $\kappa^{XY}$, free indices
$A,B,C$ (insertion) and $D,E$ (outputs); $(-1)^\kappa$ the Koszul sign
(5A.61)–(5A.62); vertex-label Wick weight $=1$.

Operator counting: the insertion supplies $7$ $D$'s $+\,6$ $\bar D$'s, the vertices
$6+6$; the two $\theta$-loops absorb $D^2\bar D^2$ each (F.6), the two output jets
retain up to $(2{+}1)+(2{+}2)$, and the remaining pairs convert to momenta via (K.1) —
five $\mathsf p$-factors, of which two are consumed by the $(\ell,k)$ tensor reduction
and **three** survive as external $\mathsf p(q_1),\mathsf p(q_2)$ factors dressing the
two-letter output — the $\mathsf p^3\langle D,A\rangle$ family of (K3.2).

## 5. D-algebra: reduced result

<!-- ENGINE3-RESULTS-SLOT -->

## 6. Anomaly-sector identification

Per marked edge $e\in\{1,\dots,5\}$ the occurrence-wise cutting identity (K.9) splits
each four-dimensional square $\bar r_e^{\,2}$ over the $d$-dimensional $K':=D_1\cdots
D_5$ into contact rows (Schwinger–Dyson/EOM sector) plus the cutting failure
$\mu_{r_e}^2/K'$. With line momenta (K3.3) and strictly hatted externals,

$$
\mu_{L_1}^2=\mu_\ell^2,\quad
\mu_{L_2}^2=\mu_k^2,\quad
\mu_{L_4}^2=\mu_\ell^2,\quad
\mu_{L_5}^2=\mu_k^2,\quad
\mu_{L_3}^2=\mu_\ell^2+2\mu_{\ell k}+\mu_k^2 ,
\tag{K3.5}
$$

so the middle bar is the sole source of the mixed invariant $\mu_{\ell k}$. The anomaly
sector of the graph is the total evanescent remainder

$$
\Gamma^{\rm anom}_{\text{日}}
=\mu^{4\epsilon}\!\!\int\!\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}\,
\frac{N_\ell\,\mu_\ell^2+N_k\,\mu_k^2+N_{\ell k}\,\mu_{\ell k}
+N_{\ell\ell kk}\,\mu_\ell^2\mu_k^2+\dots}{K'}
+(\text{contact daughters}),
\tag{K3.6}
$$

finite and local after assembly with the $\hat\delta-\delta_4=-\breve\delta$ metric
mismatches of the contact rows (one-loop mechanism, settlement §5, applied per
sub-loop).

## 7. The AAA-kite $\mu$-masters by Feynman parameters

Insertion lemma (K.11) unchanged. The archetype double-evanescent master factorizes by
inner-loop-first parametrization because the inner $\mu^2$-triangle is
$\Delta$-independent (K.3):

$$
N_1:=\mu^{4\epsilon}\!\!\int\!\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}
\frac{\mu_\ell^2\,\mu_k^2}{K'}
=\frac1{32\pi^2}\int_0^1\!dx\,L\big(2,x(1-x)q_1^2\big)+O(\epsilon)
=-\frac{q_1^2}{3072\,\pi^4}+O(\epsilon),
\tag{K3.7}
$$

($k$-loop first through $D_2D_3D_5$, then the $\mu_\ell^2$-bubble through $D_1D_4$);
the $\ell\leftrightarrow k$ mirror gives $-q_2^2/3072\pi^4$. Full master table:

<!-- MASTERS3-RESULTS-SLOT -->

## 8. Assembly: the final result

<!-- ASSEMBLY3-RESULTS-SLOT -->

## 9. HT comparison

1. Topology: the computed graph is exactly HT's unique two-loop Laman support.
2. Truncation pattern: length-2 dies kinematically (companion memo, K.13);
   length-3 is the first surviving channel — matching `main.tex:222`.
3. The quantitative acceptance target for the **full** channel (all routings summed;
   outside this single-graph memo) is Wess–Zumino consistency
   $\{Q_0,Q_2\}=-Q_1^2$ evaluated on $A^AA^BA^C$ with the settlement's locked one-loop
   kernels on the right-hand side. The single-graph result of §8 carries exactly the
   word basis and quantum numbers (K3.2) that this identity constrains.

## 10. Boundary and census

This memo computes one labeled graph (all-vector lines, three cubic BCH vertices,
insertion at a degree-3 corner). Same-order contributions deferred to a future full
census: ghost-line routings; quartic-vertex routings; matter/superpotential loops
(present for the AAA word through the $\Phi$-loop dressing of the vector lines only at
higher letter length — the $B,C$ output families of (K3.2) are closed here);
insertion-side nonlinear (BCH/connection) routings; normal-product/$\mathscr Z$
scheme terms. Scheme decisions **[D3]** (two-loop evanescent ledger) and **[D4]**
(canonical routing) as in the companion memo §10.

## 11. Verification artifacts

<!-- VERIFICATION3-RESULTS-SLOT -->
