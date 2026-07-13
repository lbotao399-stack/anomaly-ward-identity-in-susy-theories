# Step 6 GPT Pro two-loop forensic audit

- Status: `GAP_REVIEW_ONLY_NO_FORMULA_AUTHORITY`
- Authority read: `origin/main@9e11316c94efe37df2512a812738ff153c8e6985`
- Raw review: `tasks/reviews/2026-07-12-step6-gpt-pro-two-loop-architecture-review.md`
- Inputs excluded: web, Notion, target formula, unmerged calculation artifacts

## Topology

`PROVED_TOPOLOGY`:

$$
H=K_4\setminus e,
\qquad
(V,E,L)=(4,5,2),
\qquad
\deg H=(3,3,2,2).
$$

With one insertion, three action vertices, and two external ports, the direct source-valence families are

$$
I_{(3)}S_{(3)}^3,
\qquad
I_{(2)}S_{(3)}^2S_{(4)}.
$$

`REJECTED_AS_GRAPH_ISOMORPHISM`:

$$
I_{(2)}S_{(3)}^4:
\qquad
(V,E,L)=(5,6,2)\neq(4,5,2).
$$

The four distinct relations are

$$
\texttt{LITERAL\_GRAPH},
\quad
\texttt{MARKED\_SUBDIVISION\_LIFT},
\quad
\texttt{HOMEOMORPHIC\_CORE},
\quad
\texttt{D\_COLLAPSE/SD\_CUT}.
$$

No relation may be substituted for another without its own certificate.

## Valence census

For two outgoing ports,

$$
m+\sum_{r\ge3}rn_r=2I+2,
\qquad
L=I-\sum_{r\ge3}n_r,
$$

$$
\boxed{
(m-2)+\sum_{r\ge3}(r-2)n_r=2L=4.
}
$$

The twelve weighted-partition solutions are `PROVED_TOPOLOGY`.  Their promotion to physical graphs is `UNDERSPECIFIED` until typed ports, Wick pairings, normal ordering, external extraction, ghosts, and counterterms are instantiated.

## Exponential grade

For multiplicities $n_r$,

$$
\boxed{
C_{\exp}
=
\prod_{r\ge3}
\frac{(-1)^{n_r}}{n_r!\,\hbar^{n_r}}.
}
$$

The raw review omitted

$$
\hbar^{-\sum_rn_r}.
$$

Action-internal Taylor factorials and exponential factorials are independent fields.  A labeled Wick sum is not divided by the typed automorphism order a second time.

## Incidence and routing

For the literal five-edge graph, use the vertex-by-edge incidence matrix

$$
\partial=
\begin{pmatrix}
-1&-1&0&-1&0\\
1&0&1&0&1\\
0&1&-1&0&0\\
0&0&0&1&-1
\end{pmatrix}.
$$

With

$$
r=
\begin{pmatrix}
-k-\ell-p-q\\ k\\ k+q\\ \ell\\ \ell+p
\end{pmatrix},
\qquad
j=
\begin{pmatrix}
-(p+q)\\0\\q\\p
\end{pmatrix},
$$

the exact check is

$$
\boxed{\partial r+j=0.}
$$

The raw review wrote the transpose convention inconsistently; the routing itself passes.

## Forest census

Besides the left and right triangles, the literal graph has the proper one-loop outer cycle

$$
\boxed{
\gamma_O=\{e_1,e_2,e_3,e_4\}.
}
$$

Its UV status is fixed only after the compiled numerator and power counting.  The three candidates are pairwise overlapping; if all are divergent, the allowed elementary forests include

$$
\varnothing,
\qquad
\{\gamma_L\},
\qquad
\{\gamma_R\},
\qquad
\{\gamma_O\},
$$

and no two-element subset of these three.

The six-edge marked lift requires an independent forest census.

## DRED boundary

The raw DOM capture is not an exact metric source.  Required typed data remain:

$$
V_{(4)}=V_{\widehat d}\oplus V_{\widetilde\epsilon},
$$

with explicit embeddings, projectors, traces, orthogonality, two-loop measure, Fourier square signs, spinor contractions, rank-four tensor basis, and metric-coercion provenance.  Bare numerators contain no inserted $\epsilon$.

## External target firewall

The universal bitriangle kernel and the operator differential are distinct objects.  The only admissible external benchmark for the two-letter operator is

$$
\boxed{Q_2(b^Ab^B)=0.}
$$

Any nonzero `Q2(bb)` regression target is `REJECTED`.  The benchmark remains `EXTERNAL_TARGET_NOT_DERIVATION` and is inaccessible to the Euclidean compiler.

## Blocking corrections

- `P0`: hash-locked DRED contract on accepted `origin/main`.
- `P0`: literal/lift/core/collapse distinction in GraphIR.
- `P0`: $\gamma_O$ and six-edge-lift forest census.
- `P0`: external zero target isolated by an import firewall.
- `P1`: restore exact $\hbar$ grading.
- `P1`: fix incidence orientation and transpose type.
- `P1`: keep twelve families as valence requests until physicalized.
- `P1`: typed external extraction, DRED coercions, and ordered nested-counterterm composition.
