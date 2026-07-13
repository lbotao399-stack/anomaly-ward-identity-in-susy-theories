# Step 6 GPT Pro round-2 implementation audit prompt

- Role: `GAP_REVIEW_ONLY_NO_FORMULA_AUTHORITY`
- Status: `RESPONSE_CAPTURED`
- Raw response: `tasks/reviews/2026-07-12-step6-gpt-pro-round2-response.md`
- Raw response SHA-256: `48929292078bb911d25d57e989445ca794bb327990c17d955ad493476e8e6075`
- Calculation authority: none
- External target supplied: false
- Holomorphic-twist input forbidden: true

## Prompt

Second-round gap review only; no formula authority and no final anomaly coefficient. Do not use or infer any holomorphic-twist target. Audit only the independently constructed Euclidean N=4 SYM pure-gauge two-loop pipeline below.

Locked proposal facts:

1. For two background legs and one insertion (I_{(m)}),

   $$
   (m-2)+\sum_{r\geq 3}(r-2)n_r=4.
   $$

   The 12 valence families are

   $$
   \begin{aligned}
   I_2:&\ \{S_3^4,S_3^2S_4,S_4^2,S_3S_5,S_6\},\\
   I_3:&\ \{S_3^3,S_3S_4,S_5\},\\
   I_4:&\ \{S_3^2,S_4\},\\
   I_5:&\ \{S_3\},\\
   I_6:&\ \{1\}.
   \end{aligned}
   $$

   These are `VALENCE_NOT_GRAPH` until Wick-complete.

2. Literal five-edge (K_4\setminus e) direct sources are (I_3S_3^3) and (I_2S_3^2S_4). We separately retain raw marked (K_{2,3}=I_2S_3^4) as a six-edge graph; it may become a five-edge child only through a typed D-algebra/SD collapse certificate.

3. One literal routing uses (P+p_1+p_2=0) and denominators

   $$
   D_{3311}=k^2l^2(l-p_1)^2(k+l)^2(k+l+p_2)^2,
   $$

   $$
   D_{2324}=k^2(k-P)^2l^2(l-p_1)^2(k+l)^2.
   $$

   The raw (K_{2,3}) routing is

   $$
   (k,k-P,l,l-p_1,-k-l,-k-l-p_2).
   $$

4. Every graph has three simple one-loop cycles (gamma_L,gamma_R,gamma_O). Each pair overlaps non-nested; no two-cycle forest is admissible merely from topology.

5. Project BCH grammar is generated exactly through (mathcal V^5):

   $$
   \Gamma_{(n)}=\frac{(-1)^{n-1}}{n!}\operatorname{ad}_{\mathcal V}^{n-1}(D\mathcal V),
   \qquad
   W_{(n)}=-\frac18\bar D^2\Gamma_{(n)},
   $$

   with the independent tilded recursion and

   $$
   X_{(n)}=D_+W_{(n)+}
   +\sum_{r=1}^{n-1}[\Gamma_{(r)+},W_{(n-r)+}].
   $$

   It gives

   $$
   (|I_2|,|I_3|,|I_4|,|I_5|,|I_6|)=(2,10,30,70,140),
   $$

   (S_3^+,\ldots,S_6^+), independent (S_3^-,\ldots,S_6^-), (E_\Xi^{\rm gauge}) through (mathcal V^5), and (E_{\mathcal V}) through (mathcal V^5). No external-projection coefficient has yet been transported.

6. DRED:

   $$
   d=4-2\epsilon,
   \qquad
   \delta_{(4)}=\widehat\delta+\widetilde\delta,
   $$

   loop/external momenta live in the hatted space, spinor algebra uses (delta_{(4)}), the bare numerator contains no (epsilon), and

   $$
   \mu^{4\epsilon}
   \frac{d^dk}{(2\pi)^d}
   \frac{d^dl}{(2\pi)^d}
   $$

   is the two-loop measure.

Requested forensic review:

A. Enumerate the minimal physical typed-port/Wick families that instantiate the two literal (K_4\setminus e) parents. Separate all background-port distributions, chiral/antichiral sector words, external probe types, and prove every sector word that vanishes before integration from chirality/measure saturation. Do not call a valence family a graph.

B. Specify a complete first-class edge-tagged two-loop D-algebra scheduler from the Project AST: phase order, pivots, endpoint-transfer/Koszul data, critical-pair obligations, external derivative tokens, and typed propagator collapses. Give an exact combinatorial expression for row count in terms of derivative-scope branch sizes; do not reuse the one-loop eight-row number.

C. Give the exact BPHZ/minimal-subtraction forest algorithm for these overlapping cycles. For a compiled numerator (N(k,l)), state how each candidate (gamma) is tested by its own scaling degree, then write (R') and (KR') with all allowed forests. Include the outer cycle and distinguish the six-edge lift.

D. Perform a graph-theoretic two-loop FP/NK census for this insertion using typed ports (mathcal V^n c'c). State the smallest connected families, which literal (K_4\setminus e) parents can or cannot contain a ghost loop, and what higher-(n) ghost vertices are required. Do not use finite-BV cycles as a blocker.

E. Check every displayed topology, routing, coefficient recursion, and term count above; list corrections with exact equations.

F. Return a machine-oriented schema: required IR record types, invariants, acceptance gates, and P0/P1 list. Keep any possible two-loop coefficient explicitly `UNCOMPUTED`.
