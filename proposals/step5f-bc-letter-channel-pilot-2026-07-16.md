# Step-5F memo — the pilot channel of the component AWI: $Q_-(\psi_+^A\widetilde\phi^B)$ at one loop (Konishi-anomaly-like sector, Euclidean N=4)

Status: `NON_AUTHORITY_PROPOSAL`. Numbered equations (5F.$n$). Companions: Step-5C
(current and off-shell divergence), Step-5D (method), Step-5E (toolkit: collapse
identity, master integral, W4/W5 items — its Konishi-current channel is hereby demoted
to an optional warm-up; **this memo is the designated pilot**, per the owner's
correction of 2026-07-16).

Owner instructions implemented: *insert the divergence of the supersymmetry current as
one vertex, then bring in one interaction vertex, and obtain the one-loop result for
$Q_-(\psi_+^A\bar\phi^B)$ beyond the tree-level classical result. This sector is
Konishi-anomaly-like.*

---

## 0. The channel and why it is Konishi-like

The letter pair is $(\mathfrak b_r,\mathfrak c^s)=(\psi_{r+},\widetilde\phi_s)$ with
**open adjoint indices** $A,B$ — the $(B_r,C^s)$ family of the 81-channel ledger, expected
nonzero $\propto\delta_r^s$ (six ordered channels). The composite
$\psi_{r+}^A\widetilde\phi_s^B$ is a component of the flavor-Konishi superfield family
$\widetilde\Phi_s e^{\mathcal V}\Phi_r$; the quantum term produced below is the
supersymmetry-partner statement of the Konishi anomaly, with output in the gaugino
bilinear:

$$
\boxed{
Q_-\big(\psi_{r+}^A\,\widetilde\phi_s^B\big)
=\underbrace{-\sqrt2\,F_r^A\,\widetilde\phi_s^B}_{\text{tree (off-shell); on the aux
shell }-\varepsilon_{rtu}(\widetilde\phi_t\times\widetilde\phi_u)^A\widetilde\phi_s^B}
\;+\;\underbrace{\mathfrak c_{bc}\,\frac{\hbar}{32\pi^2}\,\delta_{rs}\,
\mathbb F^{AB}{}_{DE}\;\widetilde\lambda^D_{\dot a}\widetilde\lambda^{E\dot a}}_{\text{one
loop (anomaly), this memo}}\;+\;\dots}
\tag{5F.1}
$$

with $\mathbb F^{AB}{}_{DE}$ a color word built from two structure constants
($c_{ADC}c_{BEC}$-family; its precise combination is a W-item output, not an input).
Twisted-grading check: $[\mathfrak b]+[\mathfrak c]+[Q_-]=\tfrac32+1+\tfrac12=3
=[\widetilde\lambda\widetilde\lambda]$; flavor: $\mathbf 3\otimes\bar{\mathbf 3}\supset
\mathbf 1$ with the singlet forced ($\delta_r^s$) because the output carries no flavor.
In the holomorphic-twist dictionary (Step-5D (5D.2)) this is
$Q_1(\beta_r\gamma^s)\propto\delta_r^s\,\partial_{\dot a}c\,\partial^{\dot a}c$ — the
external target's Konishi-like entry.

## 1. The correlator that extracts (5F.1)

$$
\mathcal M^{AB;DE}_{rs;\dot c\dot d}
:=\Big\langle\;\partial_mj^m_{E,-}(x)\;\;
\big(\psi^A_{r+}\widetilde\phi^B_s\big)(y)\;\;
\widetilde\lambda^D_{\dot c}(u)\;\widetilde\lambda^E_{\dot d}(v)\;\Big\rangle_E ,
\tag{5F.2}
$$

connected, at the first nonvanishing order. Structural facts:

1. **The classical layer of this correlator vanishes.** The contact term of the Ward
   identity is $-\tau_E^{-1}\delta(x-y)\langle\delta_-(\psi_{r+}\widetilde\phi_s)(y)\,
   \widetilde\lambda\widetilde\lambda\rangle$ with
   $\delta_-(\psi_{r+}\widetilde\phi_s)=-\sqrt2F_r\widetilde\phi_s$
   ($\delta_-\widetilde\phi=0$, Step-5D (5D.3)); the tree correlator
   $\langle F\widetilde\phi\,\widetilde\lambda\widetilde\lambda\rangle$ has no tree
   graph. So — exactly as in the Step-5E pilot — whatever survives at one loop **is**
   the quantum term of (5F.1). The channel is self-cleaning.
2. The insertion is the locked EOM form (5D.4) of $\partial_mj^m_{E,-}$; every graph
   below is a Wick contraction of one typed term of (5D.4).

## 2. Graph census at one loop

External ends to absorb: one $\psi$-end at $y$ (needs a $\widetilde\psi$ partner), one
$\widetilde\phi$-end at $y$ (needs $\phi$), two $\widetilde\lambda$-ends at $u,v$ (each
needs $\lambda$ or an elementary $\widetilde\lambda$ in the insertion/vertex). Complete
families (absences to be re-proved mechanically, W3′):

**(F1) The one-interaction-vertex triangles — the owner's minimal graphs.** Two
variants, both using one matter Yukawa vertex
$-\sqrt2h\,c_{A'B'C'}\phi^{A'}_t\widetilde\psi^{B'}_t\widetilde\lambda^{C'}(w)$ from
(4C.42a):

- **(F1a)** insertion term 6 of (5D.4), Yukawa part of $\mathcal E_{\widetilde\psi_t}$:
  insertion fields
  $-\sqrt2(\sigma^m)_{-\dot a}(\mathcal D_m\widetilde\phi_t)\cdot
  \sqrt2h(\phi_t\times\widetilde\lambda^{\dot a})(x)$.
  Contractions: $\phi_t(x)\!\leftrightarrow\!\widetilde\phi_s(y)$ [$t=s$];
  $\widetilde\phi_t(x)\!\leftrightarrow\!\phi_{t'}(w)$ [$t'=t$];
  $\widetilde\psi_{t'}(w)\!\leftrightarrow\!\psi_{r+}(y)$ [$t'=r$];
  $\widetilde\lambda(x)\to u$, $\widetilde\lambda(w)\to v$.
  Triangle $x\!-\!y\!-\!w$; flavor chain forces $r=t'=t=s$: **$\delta_{rs}$ emerges
  from the graph, matching the census.**
- **(F1b)** insertion term 4 of (5D.4), Yukawa part of $\mathcal E_{\phi_t}$:
  insertion fields $\sqrt2\cdot\sqrt2h(\widetilde\psi_t\times\widetilde\lambda)
  \psi_{t-}(x)$.
  Contractions: $\widetilde\psi_t(x)\!\leftrightarrow\!\psi_{r+}(y)$ [$t=r$];
  $\psi_t(x)\!\leftrightarrow\!\widetilde\psi_{t'}(w)$ [$t'=t$];
  $\phi_{t'}(w)\!\leftrightarrow\!\widetilde\phi_s(y)$ [$t'=s$];
  $\widetilde\lambda(x)\to u$, $\widetilde\lambda(w)\to v$. Same triangle, same
  $\delta_{rs}$.

**(F2) The collapse family — insertion kinetic pieces, two Yukawa vertices.** The
kinetic parts of $\mathcal E_{\widetilde\psi}$/$\mathcal E_{\phi}$ in the same insertion
terms contract a full Dirac (resp. Klein–Gordon) operator into the adjacent internal
line: numerator $(\bar\sigma\cdot r)(\sigma\cdot\bar r)/r_d^2=1+\mu_\ell^2/r_d^2$
(Step-5E (5E.6)). The "$1$" collapses the line to a point and cancels, in the
unregulated theory, against the F1 triangles and the (vanishing) contacts — this is the
cutting-rule closure. Under DRED the $\mu_\ell^2/r_d^2$ remainder survives: the
**$\mu^2$-triangle** with one evanescent insertion, the anomaly source. Scalar-line
collapses are exact (Step-5E §3 family (b) argument) — only fermion-line collapses
contribute.

**(F3) Gauge-sector remainder $\mathfrak G_-$** (Step-5D (5D.5) item 2): graphs from the
$\mathcal E_A$, $\mathcal E_{\mathscr D}$, $\mathcal E_\lambda$ terms of (5D.4) and the
gauge-fixing/ghost sector. Charge/letter counting: to reach the external content
$(\psi\widetilde\phi;\widetilde\lambda\widetilde\lambda)$ these need at least two more
vertices at this loop order in Feynman gauge; typed and expected absent/higher-order —
**must be proved absent mechanically (W3′), not assumed**, since $\mathfrak G_-\ne0$ in
general for the SUSY current (unlike Konishi).

**(F4) Auxiliary-contact resolutions**: insertion pieces containing $F_t$ contract
through the contact $\langle F\widetilde F\rangle$ into the superpotential vertex,
reproducing composite-$F$ insertions; enumeration shows they cannot reach two external
$\widetilde\lambda$'s with $\le1$ interaction vertex (checked case by case: the
$(F,\widetilde\phi,\lambda)$- and $(F,\phi,\psi)$-type pieces all dead-end on a missing
$\phi$/$\widetilde\psi$ partner) — absence proof to be mechanized in W3′.

## 3. The regulated evaluation (assembly specification)

Momentum space, all incoming (5B.D3): insertion momentum $q$ at $x$, letter-pair
momentum $p$ at $y$, gaugino momenta $k_u,k_v$. One loop momentum $\ell$, DRED ledger of
Step-5D §5.

- Unregulated: $\sum_{\rm F1}+\sum_{\rm F2}\big|_{\text{collapse-}1}+\text{contacts}=0$
  — the exact classical closure of the Ward identity in this channel (everything
  cancels; W6′-a verifies).
- DRED: the surviving object is the $\mu^2$-triangle family,
  $$
  \mathcal M\big|_{\rm anom}
  =\mathcal N^{AB;DE}_{rs}\;
  T^{(\sigma)}_{-\dot c\dot d}(q,p,k)\;
  \int\!\frac{d^d\ell}{(2\pi)^d}
  \frac{\mu_\ell^2}{\ell_d^2(\ell{+}k_1)_d^2(\ell{+}k_1{+}k_2)_d^2}
  \;+\;\text{orientation/assignment images},
  \tag{5F.3}
  $$
  evaluated by the master integral (5E.8) $\to\frac1{32\pi^2}$, $\Delta$-independent
  $\Rightarrow$ the output is **local**: after amputating the two
  $\widetilde\lambda$-legs and the $y$-legs, a polynomial vertex — the operator
  statement (5F.1).
- The $\sigma$-word $T^{(\sigma)}$: four-dimensional chains from the insertion's
  $(\sigma^m)_{-\dot a}$, the loop $\sigma\cdot\bar r$ factors, and the Yukawa spinor
  contractions; the frame projection forces the output into
  $\widetilde\lambda_{\dot a}\widetilde\lambda^{\dot a}$ (dotted scalar) — the
  $\partial_{\dot a}c\,\partial^{\dot a}c$ structure. The color word: F1a gives
  $c_{ADC'}c_{BEC'}$-type after the $\kappa$-contractions of three propagators
  (exact combination = W6′-c output; this is the $\mathbb F^{AB}{}_{DE}$ object of the
  review's R.6-2 item, now derived rather than imported).

**Pass criterion P1′**: the assembled coefficient
$\mathfrak c_{bc}/(32\pi^2)\,\delta_{rs}\,\mathbb F$ matches, through the HT dictionary,
the external target's $Q_1(\beta_r\gamma^s)$ entry; and through the Konishi multiplet
relation, the classic Konishi-anomaly normalization. Two independent external sanity
anchors for one project-derived number.

## 4. Relation to the Step-5E toolkit and to the full program

Shared items (already specified there, unchanged): W2 (component rules), W4 (collapse
identity), W5 (master integral). New/modified items:

- **W3′** [(5F.2) census]: mechanical Wick enumeration of every (5D.4) term against the
  external set $\{(\psi_{r+}\widetilde\phi_s)(y),\widetilde\lambda(u),
  \widetilde\lambda(v)\}$ at $\le2$ vertices; confirm F1a/F1b as the only
  one-interaction-vertex graphs; prove F3/F4 absences at this order.
- **W6′** [(5F.3)→(5F.1)]: (a) verify the unregulated closure (collapse-"1" terms +
  F1 + contacts sum to zero — the strongest single check of the whole bookkeeping);
  (b) assemble the $\mu^2$-triangles: orientations, Koszul fermion-loop signs,
  Feynman-parameter $\Gamma(3)=2$; (c) contract color/flavor: output
  $\delta_{rs}\,\mathbb F^{AB}{}_{DE}$ explicit; (d) the $\sigma$-word reduction to
  $\widetilde\lambda_{\dot a}\widetilde\lambda^{\dot a}$ with the exact rational
  $\mathfrak c_{bc}$.
- **W9′** [P1′]: dictionary comparison (HT $Q_1(\beta\gamma)$ entry; Konishi literature
  value) — reference-level, post-derivation.

Promotion path on PASS: the same insertion + census machinery runs the remaining
letter channels; the $(\mathfrak f,\mathfrak f)$ seed (gauge sector, $\mathfrak G_-$
nontrivial) is the next target, now with the F2-collapse bookkeeping already validated
in a channel where $\mathfrak G_-$ is spectator.

## 5. Decisions and gaps

No new convention decision is required (the channel consumes 5B.D3, 5D.D4, 5E.D5 and
the DRED ledger). Gap surfaced for the settlement bookkeeping: the F3 absence proof at
this order is channel-specific; the general typed treatment of $\mathfrak G_-$ remains
the known open item of the method (Step-5D §4 item 2) and must be faced at the
$(\mathfrak f,\mathfrak f)$ seed.
