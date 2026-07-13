# GPT Pro Round 1 prompt — one-loop covariant completion

- Source chat: https://chatgpt.com/c/6a5519c3-70a4-83e8-8862-39f8df68d4dd
- Role: external theory audit only
- Repository formulas remain authoritative

We need design, not yet bulk-compute, a rigorous one-loop exactness theorem for a Euclidean 4d N=1/N=4 SYM superspace anomaly-Ward-identity calculation.

Operator seed:
O^{AB}=nabla_-[(nabla_+ W_+)^A (nabla_+ W_+)^B].

Project conventions relevant here:
K_+=-(1/8)D_+ barD^2 D_+.
Use background-field Fermi-Feynman gauge and DRED, with 4d spinor/D-algebra and d=4-2epsilon loop momentum.
The primitive one-loop triangle coefficient is to be computed independently; do NOT import any known coefficient or holomorphic-twist result.

Research question:
Prove or refute the precise statement that every higher-background-leg one-loop 1PI supergraph (box, pentagon, and possibly higher V-prepotential polygons/contact graphs) is only the non-Abelian gauge-covariant completion of the primitive triangle, so that no new independent local coefficient occurs. The analogy is the ABJ triangle plus box/pentagon completion of F wedge F.

Please produce a gap audit and a minimal exact proof architecture, not a claimed result:
1. State the theorem in background-gauge/BRST language: which effective-action insertion, which Slavnov-Taylor or background Ward identity, which cohomology/uniqueness statement, and what locality/power-counting assumptions are required.
2. Decide whether the completion is finite (triangle+box+pentagon) or infinite when written in the unconstrained prepotential V. In chiral representation W_alpha=-1/4 barD^2(e^{-V}D_alpha e^V) has an infinite BCH series, so distinguish component A_mu expansion, field-strength variables, and V-supergraph expansion.
3. Give the exact bridge between chiral and vector representations, including covariant derivatives, background/quantum splitting, measures, propagator/vertex conjugation, and the similarity transformation proving equality of physical covariant kernels. Keep all operator orderings and gauge transformations explicit.
4. Derive the superspace Ward recursion relating an (n+1)-background-leg decorated polygon/contact amplitude to the n-leg amplitude. State all seagull/contact terms. Explain how the primitive transverse/cohomological form factor supplies the boundary datum.
5. Give a graph-complete one-loop census for the first nontrivial levels: primitive triangle, four-point/box plus contacts, five-point/pentagon plus contacts; say what extra families appear in V representation and whether ghosts/Nielsen-Kallosh fields can contribute.
6. Give machine-checkable acceptance gates: exact GraphIR closure under gauge variation, D-algebra identities, routing/reflection, ST recursion, representation bridge, and reconstruction of the nonlinear covariant expression order by order.
7. Identify any genuine obstruction that prevents “one triangle coefficient determines all dressings” from being true for this specific composite insertion.

Source boundary: reason from standard superspace/background-field theory only. Do not use the user's Notion, local legacy notes, prior claimed one-loop coefficient, or holomorphic-twist answer. Clearly mark every assumption and every place where an explicit calculation remains necessary.
