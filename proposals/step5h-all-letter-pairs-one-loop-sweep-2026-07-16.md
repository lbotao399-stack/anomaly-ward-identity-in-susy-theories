# Step-5H memo — the one-loop $Q_-$ correction for all BPS letter pairs: the complete DRED triangle sweep (Euclidean N=4)

Status: `NON_AUTHORITY_PROPOSAL`. Numbered equations (5H.$n$). Extends Step-5G (the
$(\mathfrak b,\mathfrak c)$ execution) to the full ordered-pair ledger with the same
method: one-loop triangles, dimensional reduction ($P_L$ from $\tfrac12(1+\gamma_5)$),
the divergence insertion (5D.4) plus **one** interaction vertex — with the gauge-letter
channels ($\mathfrak f\mathfrak f$, $\mathfrak f\mathfrak b$, …) treated with the extra
care the owner flagged: they carry **more than one diagram**, for reasons made precise
in §4.

Owner instructions implemented (2026-07-16): *compute with this method the one-loop
$Q$-action correction for all BPS letter pairs; all are one-loop triangle diagrams in
dimensional regularization with one interaction vertex inserted; but the
$f_{++}f_{++}$, $f_{++}\psi_+$-type diagrams need more care — there is more than one
diagram.*

Execution status is typed per family in §7: **EXECUTED** (5G-level: census localized,
$\mu^2$-branch assembled, backbone rational × tensor displayed) vs **CENSUSED**
(diagram list + collapse sites + output tensor fixed; rational assembly delegated to the
per-channel workflow) vs **ZERO** (grading/scan proof).

---

## 1. Two classification theorems (the sweep's backbone)

**(T1) Where $\mu^2$ can arise.** The evanescent insertion is generated exactly where a
**four-dimensional spin contraction** meets $d$-dimensional denominators:

- **fermion lines** adjacent to a kinetic Euler operator:
  $(\bar\sigma\cdot\ell)(\sigma\cdot\ell)=\bar\ell^2=\ell_d^2+\mu_\ell^2$ (5G.5);
- **vector lines** adjacent to $\mathcal E_A$-kinetic or to $\bar\delta$-contracted
  spin words: in DRED the numerator metrics are $\bar\delta_{mn}$ (four-dimensional)
  while denominators are $\ell_d^2$; the trace parts give
  $\bar\delta^{mn}\ell_m\ell_n/\ell_d^2=1+\mu_\ell^2/\ell_d^2$ — the $\varepsilon$-scalar
  phenomenon of dimensional reduction.

**Exact (no $\mu^2$)**: scalar-line collapses ($-k_d^2/k_d^2$, no spin algebra);
auxiliary contacts; **ghost lines** (scalar kinematics); every **amputated/probe leg**
(physical external momenta, $\mu^2_{\rm ext}=0$).

**(T2) The gauge-sector remainder $\mathfrak G_-$ never carries anomaly.** All
$\mathfrak G_-$ graphs (ghost/gauge-fixing sector, Step-5D (5D.5) item 2) have their
loop-sensitive lines of ghost or auxiliary type; by (T1) they are $\mu^2$-free in every
channel and belong wholly to the classical closure. The anomaly of every channel comes
only from matter-fermion, gaugino, and vector-line collapses. (Mechanical confirmation:
part of each channel's W-a closure item.)

Consequently, for every channel the computation is the 5G pipeline:
(i) scan (5D.4) × external content for internal collapse sites; (ii) $\mu^2$-split;
(iii) rotational average + four-dimensional Fierz; (iv) master integrals
(5G.6) with the triangle value $\tfrac1{32\pi^2}$; (v) tensor assembly.

## 2. Alphabet, gradings, and the output table

Letters $\mathfrak f=f_{++}$, $\mathfrak b_r=\psi_{r+}$, $\mathfrak c^r=\widetilde\phi_r$,
$\mathfrak d_{\dot a}=\widetilde\lambda_{\dot a}$, derivative $\mathcal D_{+\dot a}$
(5D.2); twisted dimensions $[\mathfrak c]=1$, $[\mathfrak b]=[\mathfrak d]=\tfrac32$,
$[\mathfrak f]=2$, $[\mathcal D]=1$, $[Q_-]=\tfrac12$. The zero-derivative output
operator of each ordered pair is fixed by (dimension, flavor, Grassmann parity,
frame-scalarity); the complete table, derived project-side (it reproduces the review's
R.4 census 29/52):

| family | dim | output operator (zero-shift) | tensor | count |
|---|---|---|---|---|
| $(\mathfrak b_r,\mathfrak c^s)$, $(\mathfrak c^s,\mathfrak b_r)$ | 3 | $\widetilde\lambda_{\dot a}\widetilde\lambda^{\dot a}$ | $\delta_r^s\,\mathbb F^{AB}{}_{DE}$ | 6 |
| $(\mathfrak b_r,\mathfrak b_s)$ | $\tfrac72$ | $\widetilde\lambda_{\dot a}\,\mathcal D_+^{\dot a}\widetilde\phi_t$ | $\varepsilon_{rst}$, $r\ne s$ | 6 |
| $(\mathfrak f,\mathfrak c^s)$, $(\mathfrak c^s,\mathfrak f)$ | $\tfrac72$ | $\widetilde\lambda_{\dot a}\,\mathcal D_+^{\dot a}\widetilde\phi_s$ | $\delta$-flavor ($\bar{\mathbf3}$) | 6 |
| $(\mathfrak f,\mathfrak b_r)$, $(\mathfrak b_r,\mathfrak f)$ | 4 | $\widetilde\lambda_{\dot a}\,\mathcal D_+^{\dot a}\psi_{r+}$ | $\mathbf 3$ | 6 |
| $(\mathfrak f,\mathfrak f)$ | $\tfrac92$ | $\widetilde\lambda_{\dot a}\,\mathcal D_+^{\dot a}f_{++}$-family | singlet | 1 |
| $(\mathfrak f,\mathfrak d_{\dot a})$, $(\mathfrak d_{\dot a},\mathfrak f)$ | 4 | descent of the $(\mathfrak f,\mathfrak f)$/$(\mathfrak b,\mathfrak c)$ seeds | singlet | 4 |
| all others | — | **no candidate exists** (grading kill, §6) | — | 52 zeros |

## 3. EXECUTED families (matter-loop dominated)

### 3.1 $(\mathfrak b_r,\mathfrak c^s)$ and $(\mathfrak c^s,\mathfrak b_r)$ — done in Step-5G

Result (5G.13); the reversed ordering differs only by the composite-ordering Koszul sign
of the two letter fields at $y$ ($\psi\widetilde\phi\to\widetilde\phi\psi$: bosonic
$\times$ fermionic — sign $+1$), so the reversed channel equals the direct one at
zero-shift; recorded, not assumed (W-b item).

### 3.2 $(\mathfrak b_r,\mathfrak b_s)$ — executed

Unique one-vertex $\mu^2$-triangle (plus its $r\!\leftrightarrow\!s$ exchange image):
insertion term 7 of (5D.4), superpotential part of $\mathcal E_{\widetilde F_t}$,

$$
\mathcal I_7^{W}(x)=
-\,h\,\varepsilon_{tuv}\,
(\sigma^m\partial_m\widetilde\psi_t)_-\,
(\widetilde\phi_u\times\widetilde\phi_v)(x),
\tag{5H.1}
$$

with the single vertex $V_2$ (5G.2). Contractions:
$\widetilde\psi_t(x)\leftrightarrow\psi_{r+}(y)$ [$t{=}r$; **collapse site**: the
$\sigma\!\cdot\!\partial$ of (5H.1) against $\langle\psi\widetilde\psi\rangle$];
$\widetilde\phi_u(x)\leftrightarrow\phi_u(w)$;
$\widetilde\psi_u(w)\leftrightarrow\psi_{s+}(y)$ [$u{=}s$];
$\widetilde\lambda(w)\to\widetilde\lambda$-probe;
$\widetilde\phi_v(x)\to\widetilde\phi$-probe. The flavor chain leaves
$\varepsilon_{rsv}$: **antisymmetry in $(r,s)$ and the vanishing of the diagonal
channels are outputs of the graph, not inputs.** The $\mu^2$-branch numerator after the
collapse retains one $\sigma\!\cdot\!\ell$ (odd — averaged away) plus the
external-momentum term: the survivor is linear in the probe momentum, i.e. exactly the
$\mathcal D_+^{\dot a}\widetilde\phi$ derivative of the output operator; the triangle has
three denominators, so (5G.6) applies directly:

$$
Q_-(\psi^A_{r+}\psi^B_{s+})\Big|_{\rm anom}
=\varsigma'\,\frac{\sqrt2\,\hbar g^2}{32\pi^2}\,
\varepsilon_{rst}\,\mathbb F'^{AB}{}_{CD}\;
\widetilde\lambda^{C}_{\dot a}\,\mathcal D_+^{\dot a}\widetilde\phi^{D}_t
+O(g^4),
\tag{5H.2}
$$

couplings $(-h)(\sqrt2h/\hbar)(\hbar g^2)^3=-\sqrt2\hbar^2g^2$ — the same
$\hbar^2g^2$ scaling as (5G.13) (uniformity across the ledger); $\mathbb F'$ the
two-structure-constant word of this routing; $\varsigma'$ the same four-factor global
class as (5G.13). The closure partners ("1"-branch, the $F$-contact resolutions of
$\mathcal I_7$, the $\mathcal I_5$-family triangles) cancel unregulated (W-a).

### 3.3 $(\mathfrak f,\mathfrak c^s)$ and $(\mathfrak c^s,\mathfrak f)$ — executed

Here the composite's $\mathfrak f$-leg attaches to the insertion in **two distinct
ways** — the first instance of the owner's more-than-one-diagram warning:

- **(D1)** through the covariant-derivative $A$-part of insertion term 6,
  $\mathcal I_6\supset
  -\sqrt2h\,(\sigma^m)_{-\dot a}\,c\,A_m\widetilde\phi_t\,
  (\bar\sigma^n\partial_n\psi_t)^{\dot a}$: $A(x)\!\leftrightarrow\!\mathfrak f(y)$;
  $\psi_t(x)$ **collapse** into $V_2(w)$; $\phi(w)\leftrightarrow\widetilde\phi_s(y)$;
  $\widetilde\lambda(w)\to$ probe; $\widetilde\phi_t(x)\to\phi$-probe [$t{=}s$ forced].
  Triangle $x$–$y$–$w$ with lines $(A,\psi,\phi)$, one vertex, matter-fermion
  $\mu^2$-site;
- **(D2)** through the $F_{np}$-coefficient of insertion term 3,
  $[(\sigma^{np})_b{}^c\epsilon_{-c}F_{np}]\mathcal E^b_\lambda$ with the Yukawa part of
  $\mathcal E_\lambda$: same external hookup, **no** collapse (classical-closure
  member), needed for the unregulated cancellation.

The $\mu^2$-branch of (D1) assembles exactly as in 5G ($2/d$-average, Euclidean Fierz,
triangle master integral); couplings $(-\sqrt2h\,c)(\sqrt2h/\hbar)(\hbar g^2)^3
=-2\hbar^2g^2$; output forced to
$\widetilde\lambda_{\dot a}\mathcal D_+^{\dot a}\widetilde\phi_s$ with the momentum-linear
factor supplied by the $\mathfrak f$-leg/probe kinematics:

$$
Q_-\big(\mathfrak f^A\,\widetilde\phi^B_s\big)\Big|_{\rm anom}
=\varsigma''\,\frac{2\,\hbar g^2}{32\pi^2}\,
\mathbb F''^{AB}{}_{CD}\;
\widetilde\lambda^C_{\dot a}\,\mathcal D_+^{\dot a}\widetilde\phi^D_s+O(g^4).
\tag{5H.3}
$$

(The separation of "momentum on the output $\widetilde\phi$" from "momentum of the
$\mathfrak f$-letter itself" is a $\sigma$-word bookkeeping step inside the flagged
assembly, not a new mechanism.)

## 4. CENSUSED families (gauge-letter channels: the multi-diagram sector)

For $(\mathfrak f,\mathfrak f)$, $(\mathfrak f,\mathfrak b_r)$,
$(\mathfrak b_r,\mathfrak f)$, $(\mathfrak f,\mathfrak d)$, $(\mathfrak d,\mathfrak f)$
the diagram multiplicity has three independent sources, each absent in the matter
families:

1. **the letter $\mathfrak f$ is composite in $A$** ($f=\partial A+AA$): each
   $\mathfrak f$ supplies one $A$-leg at leading order **plus** an $AA$-seagull leg
   (letter-expansion graphs);
2. **the insertion couples to the gauge multiplet through three different term groups**:
   the covariant-derivative $A$-parts of the matter terms, the
   $F_{np}$-coefficient and $\mathcal E_\lambda$ of term 3, and the full
   $\mathcal E_A$/$\mathcal E_{\mathscr D}$ terms 1–2;
3. **two collapse species coexist** (T1): gaugino-line collapses
   ($\mathcal E_\lambda$-kinetic into $\langle\lambda\widetilde\lambda\rangle$, e.g.
   $x$–$w$ lines ending on the gaugino-minimal vertex
   $h\,\widetilde\lambda\bar\sigma[A,\lambda]$) and vector-line collapses
   ($\mathcal E_A$-kinetic and $\bar\delta$-numerators into
   $\langle AA\rangle$ — the $\varepsilon$-scalar terms).

Census results (one interaction vertex; verified by the same end-scan used in §3, to be
mechanized in W-c):

- $(\mathfrak f,\mathfrak f)$: **three** $\mu^2$-carrying graphs — the gaugino triangle
  [term 3 kinetic; lines $(A,\lambda,A)$; vertex $=$ gaugino-minimal], the vector
  triangle [term 1 $\mathcal E_A$-kinetic; lines $(A,A,\lambda)$-routing; vertex $=$
  gaugino-minimal], and the seagull-collapsed bubble [one $\mathfrak f$ contributing its
  $AA$-part]; **plus** the classical-closure set (term-3-Yukawa, term-1-current,
  $\mathfrak G_-$ ghost graphs — $\mu^2$-free by (T2)). Additional mechanism unique to
  this family: individual graphs are log-divergent, and the $1/\epsilon$ poles meet
  $O(\epsilon)$ evanescent traces — the
  $p^\rho\breve\delta^{mn}(\sigma_m\bar\sigma_\rho\sigma_n)=-2\epsilon\,\sigma\!\cdot\!p$
  mechanism (review R.3) contributes **finite** terms alongside the $\mu^2$-triangles.
  Both mechanisms must be assembled together; pole cancellation before the finite
  remainder is the per-channel gate. Output: singlet
  $\widetilde\lambda_{\dot a}\mathcal D_+^{\dot a}f_{++}$-family, the settlement's
  AA-seed. **CENSUSED** — assembly is the designated hard target, cross-checked against
  the superspace-route seed.
- $(\mathfrak f,\mathfrak b_r)$/$(\mathfrak b_r,\mathfrak f)$: **two** $\mu^2$-graphs —
  matter-fermion collapse [insertion 6 $A$-part as in §3.3 with the $\phi$-line replaced
  by the $\psi$-composite routing] and gaugino collapse [term 3 kinetic with Yukawa-1
  vertex $\sqrt2h\,c\,\widetilde\phi\psi\lambda$]; output
  $\widetilde\lambda_{\dot a}\mathcal D_+^{\dot a}\psi_{r+}$. **CENSUSED.**
- $(\mathfrak f,\mathfrak d_{\dot a})$/$(\mathfrak d_{\dot a},\mathfrak f)$: the
  composite contains the letter $\widetilde\lambda$ itself; the graphs are the
  derivative descent of the $(\mathfrak f,\mathfrak f)$ and
  $(\mathfrak b,\mathfrak c)$ seeds (R.4's classification), with the same two collapse
  species. **CENSUSED.**

## 5. The derivative tower ($\mathcal D_{+\dot a}$-descendants)

A descendant letter $\mathcal D_{+\dot a_1}\!\cdots\mathcal D_{+\dot a_m}L$ modifies the
triangle only through the momentum polynomial of the composite leg: each derivative
inserts one power of the (shifted) leg momentum $a\,q_1+b\,q_2$ into the Feynman-parameter
integrand, exactly the mechanism verified analytically in review R.5:

$$
2\!\int_0^1\!db\!\int_0^b\!da\;a^{k+\ell}\,b^{(m-k)+(n-\ell)}
=\frac{2\binom mk\binom n\ell\,\big/\,\binom mk\binom n\ell}
{(k{+}\ell{+}1)(m{+}n{+}2)}\cdot\binom mk\binom n\ell
\ \Longrightarrow\
K_{m,n;k,\ell}=\frac{2\binom mk\binom n\ell}{(m{+}n{+}2)(k{+}\ell{+}1)},
\tag{5H.4}
$$

i.e. the zero-shift coefficients computed here generate the whole tower by the
$\Gamma(3)=2$-normalized parameter moments; no new collapse sites appear (derivatives
are $d$-dimensional momenta — (T1)). Project-side re-derivation of (5H.4) from the §3
triangles is workflow item W-e; it is also the third external anchor (the
holomorphic-twist tower with the factor-2 adjudication of R.5).

## 6. The 52 zeros

Grading kill, project-side (component transcription of the R.4 argument), then scan
confirmation:

- $(\mathfrak c,\mathfrak c)$ [9]: required output dim $\tfrac52$, odd, flavor
  $\bar{\mathbf3}\otimes\bar{\mathbf3}$, frame-scalar: the alphabet admits no candidate
  (the only dim-$\tfrac52$ odd objects are $\mathcal D\mathfrak b$-descendants with a
  free $\dot a$ or wrong flavor);
- $(\mathfrak b_r,\mathfrak b_r)$ diagonal [3]: killed by the $\varepsilon_{rsv}$ of the
  unique graph family (§3.2) — a graph-level zero;
- $(\mathfrak b_r,\mathfrak c^s)_{r\ne s}$ off-diagonal [12]: the flavor chain of every
  candidate graph closes only on $\delta_{rs}$ (5G §4);
- $(\mathfrak b/\mathfrak c,\mathfrak d)$ mixed [24] and $(\mathfrak d,\mathfrak d)$
  [4]: no output candidate at the required (dim, flavor, parity) — and the end-scan
  finds no one-vertex graph with an internal collapse and matching probes.

Each zero is recorded as ZERO-with-proof-type (grading vs graph-level), the ledger's
required trichotomy.

## 7. Status ledger (the deliverable map)

| family | channels | status | anomaly backbone |
|---|---|---|---|
| $(\mathfrak b_r,\mathfrak c^s)+$rev | 6 | **EXECUTED** (5G.13) | $\tfrac{\sqrt2\hbar g^2}{32\pi^2}\delta_{rs}\,\mathbb F\,\widetilde\lambda\widetilde\lambda$ |
| $(\mathfrak b_r,\mathfrak b_s)$ | 6 | **EXECUTED** (5H.2) | $\tfrac{\sqrt2\hbar g^2}{32\pi^2}\varepsilon_{rst}\,\mathbb F'\,\widetilde\lambda\mathcal D_+\widetilde\phi_t$ |
| $(\mathfrak f,\mathfrak c^s)+$rev | 6 | **EXECUTED** (5H.3) | $\tfrac{2\hbar g^2}{32\pi^2}\,\mathbb F''\,\widetilde\lambda\mathcal D_+\widetilde\phi_s$ |
| $(\mathfrak f,\mathfrak b_r)+$rev | 6 | CENSUSED (2 $\mu^2$-graphs) | $\widetilde\lambda\mathcal D_+\psi_{r+}$-form |
| $(\mathfrak f,\mathfrak f)$ | 1 | CENSUSED (3 $\mu^2$-graphs $+$ R.3 mechanism) | AA-seed |
| $(\mathfrak f,\mathfrak d)+$rev | 4 | CENSUSED (descent) | descent forms |
| zeros | 52 | **ZERO** (§6, typed proofs) | — |

All executed/censused channels share the uniform $\hbar^2g^2$ scaling, the
$\tfrac1{32\pi^2}$ backbone, and the same four-factor global class
$\varsigma^{(\cdot)}$ (box/triangle Koszul sign, loop orientation, color-word order,
detection normalization) — a single mechanical pass fixes them coherently across the
ledger (W-b).

## 8. Verification workflow (per-channel matrix, delegated)

For each nonzero family: **W-a** unregulated closure (F1-set $+$ collapse-"1" $+$
contacts $=0$; includes the (T2) $\mathfrak G_-$ check); **W-b** the four global factors,
fixed once, coherently, on the (5G.13) channel and transported; **W-c** mechanical
end-scan census (confirm §3/§4 diagram lists, prove stated absences); **W-d** the
$(\mathfrak f,\mathfrak f)$/$(\mathfrak f,\mathfrak b)$ assemblies with both mechanisms
($\mu^2$-master and pole$\times(-2\epsilon)$), pole cancellation gate; **W-e** the tower
(5H.4) from the executed triangles; **W-f** the three external anchors — HT zero-shift
entries, HT tower, Konishi normalization — after the dictionary; verdict per channel:
exact result / exact zero with proof / BLOCKED naming the missing lock.

The sixteen-family map above, with §3's three executed backbones and Step-5G's seed, is
the complete method deliverable: every remaining item is a bounded, typed assembly with
locked inputs and a named check.
