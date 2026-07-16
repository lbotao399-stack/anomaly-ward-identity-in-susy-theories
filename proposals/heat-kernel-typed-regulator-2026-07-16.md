# Typed heat-kernel regulator on the N=4 fluctuation complex

Status: `NON_AUTHORITY_PROPOSAL` (owner-authorized continuation, 2026-07-16). This memo
attacks the first two blockers recorded in
`audits/heat-kernel-ordered-simplex-verification.json`
(`BLOCKED_HEAT_KERNEL_TYPED_REGULATOR_AND_COEFFICIENT_DERIVATION`) and in §7 of the bounded
lemma memo `proposals/heat-kernel-n4-one-loop-memo-2026-07-16.md`:

> (1) that the Hessian maps back to its own domain without a field-space supermetric;
> (2) that one blockwise formula defines a single regulator in the presence of off-diagonal
> mixing; (3) that $K_2$ or higher differential insertions vanish.

Non-claims (1)–(2) are discharged here by an explicit construction; non-claim (3) is
addressed at the enumeration level: the complete list of same-order $K_2$ blocks is derived
from the locked action and the exact two-term second-order Duhamel formula (the bounded
memo's (HK.17)) is verified symbolically; the *evaluation* of the enumerated blocks and the
distributional tower extraction remain open and are stated precisely in §7. Equations are
(TR.$n$); checks in `scripts/verify_heat_kernel_typed_regulator.py`, each naming its (TR.$n$).
No contract file is touched. The accepted Project coefficient remains that of
`contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`; nothing here modifies it.

---

## 1. The fluctuation complex

Around a background configuration of the (D1)-slice gauge-fixed locked action
$S_E$ ((5A.34) with $\eta_E=-1$, gauge fixing (5A.44)–(5A.48), ghosts (5A.60), NK branch
(D2)), the constrained fluctuation complex is the graded direct sum

$$
E:=E_V\;\oplus\;\bigoplus_{r=1}^3 E_+^{(r)}\;\oplus\;\bigoplus_{r=1}^3 E_-^{(r)}
\;\oplus\;E_{\rm gh},
\qquad
\begin{array}{l}
E_V=\{\delta\mathcal V\}\ (\text{unconstrained, even}),\\
E_+^{(r)}=\{\delta\boldsymbol\Phi_r:\ \bar{\boldsymbol\nabla}\delta\boldsymbol\Phi_r=0\}\ (\text{even}),\\
E_-^{(r)}=\{\delta\widetilde{\boldsymbol\Phi}_r:\ \boldsymbol\nabla\delta\widetilde{\boldsymbol\Phi}_r=0\}\ (\text{even}),\\
E_{\rm gh}=\{\delta\mathfrak c,\delta\widetilde{\mathfrak c},
\delta\mathfrak c',\delta\widetilde{\mathfrak c}'\}\ (\text{odd, chiral/antichiral per (5A.35)/(5A.43)}).
\end{array}
\tag{TR.1}
$$

The second variation $S''[v]$ is, as the audit correctly insists, a graded symmetric
**two-form** on $E$ (a map $E\to E^\vee$), not an endomorphism: $e^{-sS''}$ is ill-typed.

## 2. The field-space supermetric

Define the ultralocal, background-independent, graded-symmetric pairing $G:E\to E^\vee$,
sector by sector, using the constrained identity kernels (5A.72) and the Killing form
$\kappa_{AB}$ (4C.1):

$$
\begin{aligned}
G_V(\delta\mathcal V_1,\delta\mathcal V_2)
&:=\frac h2\,\kappa_{AB}\int_{E,8}\delta\mathcal V_1^A\,\delta\mathcal V_2^B,\\
G_+\bigl(\delta\boldsymbol\Phi_1,\delta\boldsymbol\Phi_2\bigr)
&:=\frac h4\,\kappa_{AB}\int_{E,+}\delta\boldsymbol\Phi_1^A\,\delta\boldsymbol\Phi_2^B,
\qquad
G_-\bigl(\delta\widetilde{\boldsymbol\Phi}_1,\delta\widetilde{\boldsymbol\Phi}_2\bigr)
:=\frac h4\,\kappa_{AB}\int_{E,-}\delta\widetilde{\boldsymbol\Phi}_1^A\,
\delta\widetilde{\boldsymbol\Phi}_2^B,\\
G_{\rm gh}
&:=\text{the ghost-doublet pairing }
\tfrac i4\kappa_{AB}\bigl[\textstyle\int_{E,+}\delta\mathfrak c'\,\delta\widetilde{\mathfrak c}
-\int_{E,-}\delta\widetilde{\mathfrak c}'\,\delta\mathfrak c\bigr]\ \text{(off-diagonal on the
doublets, per the (5A.60) kinetic pairing)} .
\end{aligned}
\tag{TR.2}
$$

**Properties (each proved or checked):**

1. **Well-defined on the constrained spaces.** $G_\pm$ integrates a product of two
   covariantly (anti)chiral superfields over the (anti)chiral cycle $\int_{E,\pm}$ (3D.4);
   no conjugation is used — admissible on the Euclidean cycle where tilded and untilded
   fields are independent (4C.53)/(5A.2). In Euclidean signature $G$ is a complex
   bilinear pairing, not an inner product; **positivity is neither claimed nor needed** —
   only invertibility enters the construction (script TR-C1 exhibits the finite-mode
   Gram matrix and its inverse on the projected space).
2. **Non-degeneracy.** On the finite-$\nu$ cylindrical spaces (3D.14), the Gram matrix of
   $G_\pm$ in a $P_{\nu,\pm}$-projected basis is invertible: the kernel of the pairing is
   exactly the complement of the projected space, on which no fluctuation lives
   ((3D.20)–(3D.21)); similarly for $G_V$ and the ghost doublet pairing (TR-C1).
3. **Ultralocality and background independence.** $G$ contains no derivatives and no
   background fields: it commutes with the background-order grading of §5 and contributes
   a field-independent Berezinian to the (3D.18) density under (3D.22) — recorded, not
   dropped: this is the $\boldsymbol\varpi$-side bookkeeping of the scheme, and its
   field-independence is what keeps normalized correlators unaffected (same mechanism as
   decision (D2)).
4. **Scheme status.** $G$ is a declared regulator datum, on the same footing as the DRED
   ledger of the accepted contract: two admissible $G$'s differ by a field-independent,
   invertible, ultralocal factor, and the induced change of $e^{-s\mathcal K}$ is a
   reparametrization of the scheme whose effect on the $s\to0$ local remainder is a
   finite local counterterm — the standard scheme ambiguity, to be fixed against the
   Ward identities exactly as the accepted contract fixes its scheme.

## 3. The typed regulator

$$
\boxed{\;
\mathcal K:=G^{-1}\,S''[v]\;:\;E\longrightarrow E\;}
\tag{TR.3}
$$

is now a well-typed even endomorphism-valued differential operator, **including all
off-diagonal (mixing) blocks**: $G^{-1}$ is block-diagonal (TR.2), so the block
$(\mathcal K)_{ab}=(G_{aa})^{-1}(S'')_{ab}$ maps $E_b\to E_a$ for every pair of sectors —
this is the discharge of audit non-claim (2): a *single* formula, (TR.3), defines the
regulator on the full complex with mixing.

**Explicit blocks** (matter sector shown; $\mathcal V$/ghost rows analogous, script TR-C2
verifies the type bookkeeping of every block):

$$
\mathcal K\big|_{E_+^{(r)}\oplus E_-^{(r)}}
=\begin{pmatrix}
\dfrac{4}{h}\,\sqrt2h\,\varepsilon_{rst}c\,\boldsymbol\Phi_t\cdot
&\ \ \bar{\boldsymbol\nabla}^2\text{-block}\\[6pt]
\boldsymbol\nabla^2\text{-block}
&\ \ \dfrac{4}{h}\,\sqrt2h\,\varepsilon_{rst}c\,\widetilde{\boldsymbol\Phi}_t\cdot
\end{pmatrix},
\qquad
\begin{array}{l}
(\mathcal K)_{+-}=G_+^{-1}(S'')_{\Phi\widetilde\Phi}
=-\bar{\boldsymbol\nabla}^2\ (\text{up to the } G\text{-weights}),\\[4pt]
(\mathcal K)_{++}=G_+^{-1}(S'')_{\Phi\Phi}
=\text{multiplication by } \tfrac{4}{h}\,\mathscr U''\ (\text{chiral}\to\text{chiral}),
\end{array}
\tag{TR.4}
$$

with the $G$-weights of (TR.2) chosen so that the **free square is the same Laplacian on
every sector**:

$$
\bigl(\mathcal K^2\bigr)\big|_{\rm free,\,chiral}
=\Bigl(\frac{4}{h}\cdot\frac h4\Bigr)^2\,
\frac1{16}\,\bar{\boldsymbol\nabla}^2\boldsymbol\nabla^2\Big|_{\rm free}\cdot(-16/\!\cdot\!)
\;\longrightarrow\;
-\Box_E\,\mathcal P_+ ,
\qquad
\mathcal K\big|_{\rm free,\,V}=-\Box_E ,
\tag{TR.5}
$$

by (5A.64)–(5A.65) and (F.3)/(5A.68); the exact weight arithmetic — including the sign
that the audit flagged as never stated — is fixed in script TR-C3 and displayed there as
an explicit table (sector, $G$-weight, free operator, sign). The **even generator** used in
$e^{-s(\cdot)}$ is

$$
\mathcal K_{\rm ev}:=
\begin{cases}
\mathcal K^2 & \text{matter and ghost sectors (first order in }\Box\text{-counting)},\\
\mathcal K & \text{vector sector (already the Laplacian)},
\end{cases}
\tag{TR.6}
$$

which is the (HK.13)-style block convention, now derived from a single typed object (TR.3)
rather than posited blockwise.

## 4. The exact second-order Duhamel structure (audit (HK.17)), verified

Organize $\mathcal K_{\rm ev}(g)=K_0+gK_1+g^2K_2$ by background-letter order $g$ (the
number of external letters an insertion emits). The bounded memo's (HK.17) is the exact
statement

$$
[g^2]\,e^{-s\mathcal K_{\rm ev}(g)}
=-\int_0^s\!dt\;e^{-(s-t)K_0}\,K_2\,e^{-tK_0}
\;+\;\int_{0<t_1<t_2<s}\!\!\!dt_1dt_2\;
e^{-(s-t_2)K_0}\,K_1\,e^{-(t_2-t_1)K_0}\,K_1\,e^{-t_1K_0},
\tag{TR.7}
$$

and script TR-C4 verifies it **as an operator identity** order-by-order in $s$ (to
$O(s^4)$) with non-commuting symbols — both terms, both signs. Any coefficient derivation
in this scheme must therefore evaluate **both** lines; retaining only two labeled $K_1$
insertions (the removed draft's error) is not admissible.

## 5. Complete same-order block enumeration

Every interaction of the locked gauge-fixed action lands in exactly one $K_1$ or $K_2$
block. The census (script TR-C5 checks it is exhaustive against the vertex list
(5A.49)–(5A.60) and closed under the $\mathcal K^2$ squaring):

**$K_1$ blocks (one emitted letter each):**

| # | block | origin | emitted letter |
|---|---|---|---|
| 1 | $\widetilde{\boldsymbol{\mathcal W}}{}^{\dot a}\bar{\boldsymbol\nabla}_{\dot a}$-connection (antichiral box) | (3C.23)/(3C.40) in $\mathcal K^2|_{--}$ | $D_{\dot a}$ |
| 2 | $\boldsymbol{\mathcal W}^{a}\boldsymbol\nabla_{a}$-connection (chiral box) | same, $\mathcal K^2|_{++}$ | $\boldsymbol{\mathcal W}_a$ |
| 3 | $(\bar{\boldsymbol\nabla}\widetilde{\boldsymbol{\mathcal W}})$, $(\boldsymbol\nabla\boldsymbol{\mathcal W})$ divergence terms | Bianchi-paired partners of 1–2 | $D$, $\mathcal W$ descendants |
| 4 | superpotential mixing $M_{rs}\propto\varepsilon c\boldsymbol\Phi$, $\widetilde M{}_{rs}\propto\varepsilon c\widetilde{\boldsymbol\Phi}$ | (TR.4) diagonal blocks | $B$-, $C$-letters |
| 5 | $\mathcal V$–matter mixing, $n{=}1$ tower | (5A.53) one-background | matter letters |
| 6 | ghost–gauge words, linear | (5A.57)–(5A.59) $B_1$-terms | ghost letters |

**$K_2$ blocks (two emitted letters each — the audit's seagull list):**

| # | block | origin |
|---|---|---|
| S1 | matter seagull $\frac h2\widetilde{\boldsymbol\Phi}\,(\mathrm{ad}\mathcal V)^2\boldsymbol\Phi$, $n{=}2$ | (5A.53)/(5A.54) |
| S2 | connection-square $\Gamma\Gamma$-terms of the covariant boxes | squaring (TR.4) kinetic blocks; (3C.15)–(3C.23) |
| S3 | $M\widetilde M$, $\widetilde MM$ products | $\mathcal K^2$ cross-terms of block 4 |
| S4 | gauge-sector two-background words of the $\mathcal W^2$ BCH expansion | (5A.49)–(5A.52) quadratic-in-background |
| S5 | ghost words, quadratic ($B_2$-Bernoulli terms) | (5A.57)–(5A.59) |
| S6 | gauge-fixing/NK background dependence | (5A.44)–(5A.48); field-independent on the (D1) slice, contributes only to the subtracted $g^0$ sector — the one $K_2$ entry that *is* shown inert, by (D2) |

Rows S1–S5 are **not** claimed to vanish; they are the same-order contributions that the
removed draft ignored and that a coefficient derivation must evaluate under the Grassmann
selection rule. Their coincident-point evaluation is open item (O2) of §7.

## 6. Grading admissibility of the enumerated blocks (structure only)

For each output word of the accepted Step-5 channels, the blocks that can contribute are
constrained by (i) the Grassmann selection rule ($D^2\bar D^2$ saturation, (F.6)/(5A.65)),
(ii) $SU(3)$ flavor, (iii) the letter gradings. Script TR-C6 tabulates, for the Konishi
output word $D_{\dot a}D^{\dot a}$: admissible $= \{1{\times}1\ \text{(two connection
insertions)},\ S1,\ S2\}$; inadmissible $=\{4{\times}4\ (\text{flavor}),\ S3\
(\text{flavor}),\ S6\ (\text{(D2) inert})\}$. This is an admissibility census, **not** an
evaluation: whether S1 and S2 cancel, combine covariantly into
$\widetilde{\boldsymbol{\mathcal W}}{}^2$ (as gauge covariance of the assembled square
suggests and as the classic component Konishi–Shizuya computation realizes), or contribute
independently, is exactly open item (O2).

## 7. Boundary of this memo, and the remaining blockers

**Discharged here:** audit non-claims (1) and (2) — the supermetric (TR.2) and the single
typed formula (TR.3) with all mixing blocks; the exact two-term Duhamel structure (TR.7)
verified as an operator identity; the complete same-order block census (§5) with an
admissibility table (§6).

**Open, stated precisely (the remaining content of the BLOCKED status):**

- **(O1) Distributional tower extraction.** The local $w$-tower must be obtained as
  distributional coefficients at $w=0$ of the regulated kernel (the bounded memo's (HK.15)
  point), e.g. by pairing with $\partial_w^{(m,n)}\delta(w)$ test functions *before* the
  $s\to0$ limit; the single-ordering moments (HK.18)–(HK.19) then arise from the bridge
  means (HK.13) — a statement to be proved, not assumed.
- **(O2) Block evaluation.** Coincident-point evaluation of the §6-admissible blocks
  (two-connection, S1, S2 for the Konishi word), including the dotted pairing, color word,
  orientation sign, and the ordered-vertex calculation that would or would not supply the
  second-ordering factor — per the bounded memo §5, a factor two may be added **only**
  after that ordered calculation is done.
- **(O3) Assembly.** The $\hbar$/EOM normalization chain and the comparison against the
  accepted contract's coefficient, channel by channel, with the 29/52 census re-derived
  from the typed blocks rather than asserted.

Until (O1)–(O3) close, the full heat-kernel reconstruction remains
`BLOCKED_HEAT_KERNEL_TYPED_REGULATOR_AND_COEFFICIENT_DERIVATION` **minus** its typed-regulator
half: the blocker's remaining content is the coefficient derivation (O1)–(O3).

## 8. Exact-check index (`scripts/verify_heat_kernel_typed_regulator.py`)

| check | names | statement |
|---|---|---|
| TR-C1 | (TR.2) | finite-mode Gram matrices of $G_V,G_\pm,G_{\rm gh}$ on projected bases are invertible (bilinear, no positivity claim) |
| TR-C2 | (TR.3)–(TR.4) | type bookkeeping: every block of $G^{-1}S''$ maps $E_b\to E_a$ (source/target table closes) |
| TR-C3 | (TR.5)–(TR.6) | $G$-weight arithmetic: free $\mathcal K_{\rm ev}=-\Box$ on every sector, sign table explicit |
| TR-C4 | (TR.7) | two-term second-order Duhamel verified as operator identity to $O(s^4)$, non-commuting symbols |
| TR-C5 | §5 | block census exhaustive against (5A.49)–(5A.60) and closed under squaring |
| TR-C6 | §6 | admissibility table for the Konishi output word (flavor/Grassmann/grading) |
