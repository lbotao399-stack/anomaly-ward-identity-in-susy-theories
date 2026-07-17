# Independent analytic-input audit for the two-loop 日/kite supergraph

Auditor: independent worker (no engine built; hand re-derivation only).
Scope: SPEC §§1–4 analytic inputs, re-derived from the locked sources
(5A.2), (5A.33)–(5A.34), (5A.49)–(5A.53), (5A.61)–(5A.63) in
`contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md`,
the seed audit `audits/step5-canonical-superfield-ww-seed.md` §§1–8, and the F-block
memo `proposals/step5b-euclidean-feynman-rules-memo-2026-07-16.md` (F.1–F.6).
Equations numbered (V.n).

## 0. Conventions used (all quoted, none altered)

$$
\epsilon^{+-}=1,\ \epsilon_{+-}=-1,\ D^+=D_-,\ D^-=-D_+,\qquad
D^2:=2D_-D_+,\qquad \{D_a,\bar D_{\dot a}\}=2\mathsf p_{a\dot a},
\tag{V.1}
$$

$$
\eta_E=-1,\quad \tau_E=-\tfrac1\hbar,\quad h:=g^{-2},\quad
f_{AB}=h\kappa_{AB}+i\mathfrak k_{AB}\ \ (\mathfrak k_{AB}=0\text{ assumed, see R5}),
\quad \mathcal V_P=2gv,\ \mathcal W_P=gW_{\rm can}.
\tag{V.2}
$$

Berezin: $\int d^4\theta\,\delta^4(\theta)=1$, $\delta^4(\theta)=\theta^2\bar\theta^2$;
measure conversion $\int_{E,+}(-\tfrac14\bar D^2)X=\int d^dx\,d^4\theta\,X$, i.e.
$\int_{E,+}\bar D^2X=-4\int_8 X$ (F-memo §3 rule 2), mirror for $\int_{E,-}$.
Consistency check of the anchors with (V.1): $\theta^2:=\theta^a\theta_a=2\theta_-\theta_+
=-2\theta^+\theta^-$, so $D^2\theta^2=2D_-D_+(-2\theta^+\theta^-)=2\cdot(-2)=(-4)$ ✓ —
the level-0 anchor pins the $\theta^2$ orientation and hence the Berezin orientation
(no residual freedom there; see R6).

## 1. Cubic vertices from the locked 5A.52 gauge word

### 1.1 BCH letters

From (5A.49) with $a_{00}=1$, $a_{10}=-\tfrac12$, $a_{01}=+\tfrac12$ and from (5A.50)
with $\tilde a_{00}=-1$, $\tilde a_{10}=-\tfrac12$, $\tilde a_{01}=+\tfrac12$
(both verified against the integral representations (5A.51)):

$$
\Gamma_a=D_a\mathcal V+\tfrac12\llbracket D_a\mathcal V,\mathcal V\rrbracket+O(\mathcal V^3),
\qquad
\widetilde\Gamma_{\dot a}=-\bar D_{\dot a}\mathcal V
+\tfrac12\llbracket \bar D_{\dot a}\mathcal V,\mathcal V\rrbracket+O(\mathcal V^3),
\tag{V.3}
$$

with $\llbracket X,Y\rrbracket:=XY-YX$. With (5A.33) and $\mathcal V=2gv$:

$$
\mathcal W_a=g\,W_{(1)a}+g^2W_{(2)a}+O(g^3),\qquad
W_{(1)a}=-\tfrac14\bar D^2D_av,\qquad
W_{(2)a}=-\tfrac14\bar D^2\llbracket D_av,v\rrbracket,
\tag{V.4}
$$

$$
\widetilde{\mathcal W}_{\dot a}=g\,\widetilde W_{(1)\dot a}+g^2\widetilde W_{(2)\dot a}+O(g^3),
\qquad
\widetilde W_{(1)\dot a}=-\tfrac14D^2\bar D_{\dot a}v,\qquad
\widetilde W_{(2)\dot a}=+\tfrac14D^2\llbracket\bar D_{\dot a}v,v\rrbracket .
\tag{V.5}
$$

(V.4) reproduces seed §2 exactly; (V.5) verifies the SPEC §1 sign claim for
$\widetilde W_{(1)\dot a}$ (item (3) of this audit): the linear term of
$\widetilde\Gamma$ is $-\bar D_{\dot a}\mathcal V$, and $+\tfrac18\cdot(-1)\cdot 2g=-\tfrac g4$,
so $\widetilde W_{(1)\dot a}=-\tfrac14D^2\bar D_{\dot a}v$. **Confirmed.**
Note the relative sign flip in $W_{(2)}$ vs $\widetilde W_{(2)}$; it is the sole origin
of the opposite overall signs of $S_{(3),\pm}$.

### 1.2 Direct derivation from the 5A.52 word, p+q+r+s=1

Chiral sector. The four unit-order terms of $S^{\rm g}_{E,+}$ carry
$\eta_E(-1)^{p+r}f_{AB}/(256\cdot2)$; combining $(1,0,0,0)+(0,1,0,0)$ (A-side) and
$(0,0,1,0)+(0,0,0,1)$ (B-side),

$$
S_{(3),+}
=\frac{\eta_E f_{AB}}{512}
\Big\{[\bar D^2\llbracket D^a\mathcal V,\mathcal V\rrbracket]^A[\bar D^2D_a\mathcal V]^B
+[\bar D^2D^a\mathcal V]^A[\bar D^2\llbracket D_a\mathcal V,\mathcal V\rrbracket]^B\Big\}_{\int_{E,+}}.
\tag{V.6}
$$

For Grassmann-odd blocks $X,Y$: $X^aY_a=Y^aX_a$ and $X^aY_a=-X_aY^a$ (checked from
(V.1)); with $f_{AB}=h\kappa_{AB}$ symmetric the two terms are equal:

$$
S_{(3),+}=-\frac{h}{256}\,\kappa_{AB}\int_{E,+}
[\bar D^2\llbracket D^a\mathcal V,\mathcal V\rrbracket]^A[\bar D^2D_a\mathcal V]^B .
\tag{V.7}
$$

Insert $\mathcal V=2gv$ ($(2g)^3h=8g$), use
$[\bar D^2 X][\bar D^2D_av]=\bar D^2\big(X\,[\bar D^2D_av]\big)$ (the second block is
$\bar D$-annihilated) and $\int_{E,+}\bar D^2(\cdot)=-4\int_8(\cdot)$, then
$[\bar D^2D_av]=-4W_{(1)a}$:

$$
S_{(3),+}=+\frac g8\kappa_{AB}\int_8\llbracket D^av,v\rrbracket^A[\bar D^2D_av]^B
=-\frac g2\kappa_{AB}\int_8\llbracket D^av,v\rrbracket^A W_{(1)a}^B
=-\frac g2\int d^dx\,d^4\theta\,{\rm tr}_\kappa\!\big(W_{(1)}^a\llbracket D_av,v\rrbracket\big).
\tag{V.8}
$$

Antichiral sector. The unit-order coefficient is $\eta_E(-1)^{q+s}/512$; now the
A-side combination is $D^2(\mathcal V\bar D_{\dot a}\mathcal V-\bar D_{\dot a}\mathcal V\,\mathcal V)
=-D^2\llbracket\bar D_{\dot a}\mathcal V,\mathcal V\rrbracket$, producing one extra $(-1)$
relative to (V.7):

$$
S_{(3),-}=+\frac{h}{256}\kappa_{AB}\int_{E,-}
[D^2\llbracket\bar D_{\dot a}\mathcal V,\mathcal V\rrbracket]^A[D^2\bar D^{\dot a}\mathcal V]^B
\;\Longrightarrow\;
S_{(3),-}=+\frac g2\int d^dx\,d^4\theta\,
{\rm tr}_\kappa\!\big(\widetilde W_{(1)\dot a}\llbracket\bar D^{\dot a}v,v\rrbracket\big).
\tag{V.9}
$$

Both (V.8) and (V.9) were independently re-derived a second way from the (5A.34)
cross terms $2\,\eta_E\tfrac14 h\,\mathcal W^{(1)}\mathcal W^{(2)}$ using (V.4)–(V.5);
the two routes agree. **SPEC §2 trace forms confirmed, including the relative sign.**

### 1.3 Adjoint-component form, coefficient, i's, c-index order

With $[T_A,T_B]=ic_{AB}{}^CT_C$, ${\rm tr}_\kappa(T_AT_B)=\kappa_{AB}$:
$\llbracket D_av,v\rrbracket=ic_{CU}{}^E(D_av^C)v^U\,T_E$, so

$$
S_{(3),+}=-\frac{ig}2\,c_{CUE}\int d^dx\,d^4\theta\,
(-\tfrac14\bar D^2D^av^E)(D_av^C)\,v^U,
\qquad
S_{(3),-}=+\frac{ig}2\,c_{CUE}\int d^dx\,d^4\theta\,
(-\tfrac14 D^2\bar D_{\dot a}v^E)(\bar D^{\dot a}v^C)\,v^U .
\tag{V.10}
$$

**Coefficient $\mp$/$\pm(ig/2)$: confirmed. Single factor of $i$ per vertex (from the
color commutator): confirmed. c-index order $c_{CUE}$ (C-slot, U-slot, E-slot):
confirmed, matching SPEC §2 lines exactly.**

### 1.4 The boxed seed vertices and the $(-1/\hbar)$ claim

Ordered second variation of (V.10) w.r.t. $v^{C},v^{U}$ (two slot assignments,
$v$ bosonic, no Koszul sign) gives the raw Hessian vertex
$+\tfrac{ig}2c_{UCE}W^{E\gamma}(D_{C\gamma}-D_{U\gamma})$; multiplying by the
**sign** of $\tau_E=-1/\hbar$ (the seed's "再乘 $e^{-S_{\rm int}/\hbar}$ 的 minus sign"):

$$
\mathcal V_W=-\frac{ig}2c_{UCE}W^{E\gamma}(D_{C\gamma}-D_{U\gamma}),
\qquad
\mathcal V_{\widetilde W}=+\frac{ig}2c_{UCD}\widetilde W^D_{\dot\gamma}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}),
\tag{V.11}
$$

exactly the seed §4 boxes. **Finding: the boxes include the $(-1)$ of $\tau_E$ but
NOT the $\hbar^{-1}$.** The $\hbar^{-1}$ per vertex must still be counted in the
graph-weight ledger (5A.63). The SPEC's own sentence ("already include that minus
sign") is accurate; the shorthand "includes the $(-1/\hbar)$ factor" is imprecise —
including $\hbar^{-1}$ twice would break the seed's $\hbar$-count
($\hbar^3\cdot\hbar^{-2}=\hbar^1$ in $\Gamma_{T,A}$, which is correct as locked).
Wick weight $w_{\rm Wick}=1$ (1/n! vs n! vertex assignments): mechanism confirmed
as in seed §5.

## 2. Insertion operators (SPEC §3)

$$
K_+:=-\tfrac14D_+\bar D^2D_+
\;=\;\text{(canonical) }D_+W_{(1)+}\ \text{applied to }v,
\tag{V.12}
$$

consistent with $A_P=\nabla_+\mathcal W_+=g\,D_+W_{{\rm can},+}+O(g^2)$, hence
$\nabla_-(A^AA^B)_P=g^2\,\mathcal I^{AB}_{(2)}+O(g^3)$ as stated in SPEC §3.

$$
D_-K_+=-\tfrac14\,D_-D_+\,\bar D^2D_+
=-\tfrac14\big(\tfrac12D^2\big)\bar D^2D_+
=\boxed{-\tfrac18D^2\bar D^2D_+}\,,
\tag{V.13}
$$

using only $D^2=2D_-D_+\Rightarrow D_-D_+=\tfrac12D^2$. **Confirmed.**
$K_+v$ carries four $D$'s acting on bosonic $v$, hence is bosonic; Leibniz gives
exactly the two terms of SPEC §3 with no relative Koszul sign:

$$
\mathcal I^{AB}_{(2)}=D_-\big[(K_+v^A)(K_+v^B)\big]
=\underbrace{(-\tfrac18D^2\bar D^2D_+v^A)(-\tfrac14D_+\bar D^2D_+v^B)}_{\mathfrak a}
+\underbrace{(-\tfrac14D_+\bar D^2D_+v^A)(-\tfrac18D^2\bar D^2D_+v^B)}_{\mathfrak b}.
\tag{V.14}
$$

Numeric insertion-leg product (either term): $(-\tfrac18)(-\tfrac14)=+\tfrac1{32}$,
the $1/32$ of the seed's $w_D$ chain. Note $\mathcal I_{(2)}$ is Grassmann-odd
(free lower index $-$); its fixed left position relative to the vertex product is
part of the definition (relevant for Koszul bookkeeping in the engine).

## 3. $\widetilde W_{(1)\dot a}$ sign (SPEC item (3))

Done in (V.5): $\widetilde{\mathcal W}_{\dot a}=+\tfrac18D^2(e^{\mathcal V}\bar D_{\dot a}
e^{-\mathcal V})$ (5A.33), linear term $e^{\mathcal V}\bar D_{\dot a}e^{-\mathcal V}
=-\bar D_{\dot a}\mathcal V+\dots$ (5A.50/5A.51), $\mathcal V=2gv$:

$$
\widetilde{\mathcal W}_{(1)\dot a}=+\tfrac18D^2(-2g\,\bar D_{\dot a}v)
=g\big(-\tfrac14D^2\bar D_{\dot a}v\big)
\;\Rightarrow\;
\boxed{\widetilde W_{(1)\dot a}=-\tfrac14D^2\bar D_{\dot a}v}.
\tag{V.15}
$$

**SPEC §1 sign confirmed.**

## 4. Assembled pre-D-algebra kite amplitude and prefactor ledger (SPEC §4)

Structural definition (correlator form; canonical fields; Wick weight 1;
fixed labeled topology):

$$
\Gamma^{AB;G}_{日}(p)
=\sum_{\chi_1,\chi_2,\chi_3\in\{\pm\}}
\Big\langle\,
\mathcal I^{AB}_{(2)}(\theta_0;q_{\rm ins}=-p)\,
\Big(-\tfrac1\hbar\Big)^{\!3}
S_{(3),\chi_1}(\theta_1)\,S_{(3),\chi_2}(\theta_2)\,S_{(3),\chi_3}(\theta_3)\,
v^G(p)\Big\rangle_{0,\ \text{日 contractions}} .
\tag{V.16}
$$

Fully explicit master formula. Write $\Delta_e:=\delta^4(\theta_{s(e)}-\theta_{t(e)})$
for the five lines $L_1(O\!\to\!X_1,\ell)$, $L_2(O\!\to\!X_2,p-\ell)$,
$L_3(X_1\!\to\!X_2,k)$, $L_4(X_1\!\to\!X_3,\ell-k)$, $L_5(X_2\!\to\!X_3,p-\ell+k)$;
$D_1\cdots D_5=\ell^2(p-\ell)^2k^2(\ell-k)^2(p-\ell+k)^2$. Then

$$
\boxed{
\begin{aligned}
\Gamma^{AB;G}_{日}(p)
={}&-\frac{i}{256}\,\hbar^2g^3
\sum_{t\in\{\mathfrak a,\mathfrak b\}}\ \sum_{\vec\chi\in\{\pm\}^3}\chi_1\chi_2\chi_3
\sum_{\sigma=(\sigma_1,\sigma_2,\sigma_3)}(-1)^{\kappa(t,\vec\chi,\sigma)}\;
\Big[\kappa^{\,\uparrow}\,c_{C_1U_1E_1}c_{C_2U_2E_2}c_{C_3U_3E_3}\Big]^{AB;G}_{\sigma}\\
&\times\mu^{4\epsilon}\!\int\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}\;
\frac{1}{\ell^2\,(p-\ell)^2\,k^2\,(\ell-k)^2\,(p-\ell+k)^2}\\
&\times\int d^4\theta_1 d^4\theta_2 d^4\theta_3\;
\Big[\mathcal O^{(1)}_t\Delta_1\Big]\Big[\mathcal O^{(2)}_t\Delta_2\Big]
\prod_{i=1}^{3}\Big[P^{E,\chi_i}_{\sigma_i}\,P^{C,\chi_i}_{\sigma_i}\,
P^{U}_{\sigma_i}\Big]_{\theta_i}\;
\Big[\text{jet}_{\sigma_3}\,v^G(p,\theta_3)\Big],
\end{aligned}}
\tag{V.17}
$$

with all ingredients defined as:

- Insertion words at the $\theta_0$ ends of $L_1,L_2$ ($q_{\rm ins}=-p$ incoming at O):
  term $\mathfrak a$: $\mathcal O^{(1)}_{\mathfrak a}=-\tfrac18D^2\bar D^2D_+$ on $L_1$
  (color $A$), $\mathcal O^{(2)}_{\mathfrak a}=-\tfrac14D_+\bar D^2D_+$ on $L_2$
  (color $B$); term $\mathfrak b$: the two operator words exchanged (colors stay
  $A$ on $L_1$, $B$ on $L_2$). Their numeric $(-\tfrac18)(-\tfrac14)=\tfrac1{32}$ is
  kept inside the words here.
- Vertex slot words at $\theta_i$, per chirality: $\chi_i=+$:
  $P^{E,+}=-\tfrac14\bar D^2D^{a_i}$, $P^{C,+}=D_{a_i}$, $P^{U}=1$;
  $\chi_i=-$: $P^{E,-}=-\tfrac14D^2\bar D_{\dot a_i}$, $P^{C,-}=\bar D^{\dot a_i}$,
  $P^{U}=1$; spinor index $a_i$ (or $\dot a_i$) contracted within vertex $i$.
  $\sigma_i$ = assignment of $\{E,C,U\}$ to the three incident legs of $X_i$
  ($X_1$: $\{L_1,L_3,L_4\}$; $X_2$: $\{L_2,L_3,L_5\}$; $X_3$: $\{L_4,L_5,\text{ext}\}$);
  the word acts on that leg's $\Delta_e$ at $\theta_i$, or dresses the external
  $v^G(p,\theta_3)$ (the "jet$_{\sigma_3}$") when the slot is the external leg.
- Color: $[\kappa^{\uparrow}ccc]^{AB;G}_\sigma$ = the three $c$'s with slot labels
  distributed by $\sigma$, free $A$ on the O-end of $L_1$, free $B$ on the O-end of
  $L_2$, free $G$ on the external slot, every internal line contracting its two end
  labels with $\kappa^{XY}$ ($\kappa^{AB}$ per propagator).
- $(-1)^{\kappa(t,\vec\chi,\sigma)}$ = exact Koszul sign of the ordered
  differentiation/contraction (5A.61)–(5A.62), including moves of the odd words
  ($\mathcal O^{(1)}$, $P^{E,\pm}P^{C,\pm}$ pairs) past each other — engine-level,
  left symbolic here.
- Loop integrals not performed; $\theta_0$ not integrated; the $\theta_0$-jet content
  emerges after the three Berezin integrations.

Prefactor bookkeeping, factored (SPEC §4 format):

$$
\underbrace{\hbar^5}_{\text{5 props}}\times
\underbrace{\Big(-\tfrac1\hbar\Big)^3}_{\text{3 vertices}}\times
\underbrace{\prod_{i=1}^3\big(-\chi_i\tfrac{ig}2\big)}_{S\text{-coefficients}}\times
\underbrace{\big(-\tfrac18\big)\big(-\tfrac14\big)}_{\text{insertion legs}}
=\hbar^2\cdot\Big(\!-\frac{i}{256}\Big)\chi_1\chi_2\chi_3\,g^3 ,
\tag{V.18}
$$

which is the prefactor displayed in (V.17) (the E-slot $-\tfrac14$'s and insertion
numerics are kept inside the operator words there; if instead all three E-slots sit
on internal lines and one strips all numerics from the words, the fully lumped
constant is $-\tfrac i{256}\cdot(-\tfrac14)^3\cdot\chi_1\chi_2\chi_3
=+\tfrac{i}{16384}\chi_1\chi_2\chi_3$ times bare words $D^2\bar D^2D_+$,
$D_+\bar D^2D_+$, $\bar D^2D^a$, $D^2\bar D_{\dot a}$).
Overall order $\hbar^2g^3$ canonical ✓ (SPEC §4); project conversion:
$\times g^2$ from $\nabla_-(A^AA^B)_P=g^2\mathcal I_{(2)}$, output-jet dictionary
factor per external canonical letter — giving the SPEC's stated order
$\hbar^2g^4$ in project letters (see D4 below on the $1/2g$ nuance for a bare-$v$ jet).

One-loop calibration of the same ledger (must and does reproduce the locked seed):
2 vertices $(\chi=+,-)$: $\prod(-\chi_i\tfrac{ig}2)\to(+\tfrac{ig}2)(-\tfrac{ig}2)
=\tfrac{g^2}4$; $\hbar^3\cdot\hbar^{-2}\cdot\tfrac{g^2}4\cdot\tfrac1{32}\cdot16\cdot2\cdot2
=\tfrac{\hbar g^2}2$ = seed §8 $\Gamma_{T,A}$ prefactor. **Ledger validated.**

## 5. Discrepancies / findings

- **D1 (no discrepancy).** SPEC §2 vertices: coefficients $\mp(ig/2)$, one $i$ per
  vertex, $c_{CUE}$ order, $-\tfrac14$ E-slot words, trace forms and the relative
  $+/-$ sign — all re-derived from (5A.49)–(5A.52) + dictionary; exact match.
- **D2 (precision).** The seed's boxed $\mathcal V_W,\mathcal V_{\widetilde W}$ include
  the $(-1)$ of $\tau_E=-1/\hbar$ but **not** the $\hbar^{-1}$; the $\hbar^{-1}$ per
  vertex is counted separately in (5A.63)/(V.18). SPEC's wording ("include that minus
  sign") is correct; the task-level paraphrase "includes the $(-1/\hbar)$ factor" would
  be wrong if taken literally.
- **D3 (tension outside the operative frame, flag only).** The conditional layer
  (5A.74)/(F.4) gives $\langle\mathcal V\mathcal V\rangle=-2\hbar g^2\kappa^{AB}/p^2\,
  \delta^4(\theta_{12})$, while the locked seed §3 canonical propagator
  $\langle vv\rangle=+\hbar\kappa^{AB}/p^2\,\delta^4(\theta_{12})$ maps under
  $\mathcal V_P=2gv$ to $\langle\mathcal V\mathcal V\rangle=+4\hbar g^2\kappa^{AB}/p^2$:
  a factor $(-2)$ mismatch (equivalently seed §3's
  $S_0=\tfrac12\int\kappa v(-\partial^2)v$ vs (5A.67) $\tfrac h4\int V\Box_E V$ differ by
  $-\tfrac12$ under the dictionary). The kite computation is unaffected because SPEC §1
  locks the seed form and all kite inputs are canonical, and the (5A.67)–(5A.74) block
  is explicitly `conditional`; but the two layers cannot both be exact as written and
  this should be settled before any result is re-expressed through (5A.74).
- **D4 (minor SPEC wording).** SPEC §3's conversion rule "one factor $g$ per canonical
  output letter on the RHS" fits $W$-type letters ($\mathcal W_P=gW_{\rm can}$); the
  kite's uncontracted **bare-$v$** leg converts with $v=\mathcal V_P/(2g)$, i.e. a
  factor $1/(2g)$, not $g$. Order $\hbar^2g^4$ is unchanged; the rational factor
  ($\tfrac12$) bookkeeping should be fixed when quoting project-normalized totals.
- **D5 (no discrepancy).** $D_-K_+=-\tfrac18D^2\bar D^2D_+$ and
  $\widetilde W_{(1)\dot a}=-\tfrac14D^2\bar D_{\dot a}v$: both confirmed, (V.13), (V.15).

## 6. Residual convention items NOT pinned by the calibration gates

- **R1 — global overall-sign dictionary.** The simultaneous flip
  $D_a\to-D_a,\ \bar D_{\dot a}\to-\bar D_{\dot a}$ preserves every level-0 anchor
  ($D^2,\bar D^2,\{D,\bar D\}$ all bilinear) and maps the amplitude to $\pm$ itself
  depending on the (odd) total number of explicit $D$'s ($\mathcal I_{(2)}$ is odd).
  Level 1 catches it only if the external-letter symbols ($\widetilde W_{\dot a}$,
  $X=D_+W_+$) are NOT simultaneously re-derived in the flipped realization; the SPEC
  itself licenses passing "up to an overall sign/isomorphic relabeling" with a
  documented dictionary. Hence the absolute sign of $\Gamma_日$ relative to the
  project frame is pinned only by that documentation discipline, not by the gates.
- **R2 — the seed transfer-sign ledger is conditional.** The eight endpoint signs of
  seed §6 and the two $\times2$ mixed-anticommutator factors of §7 are recorded
  arithmetic inputs (`BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION`). Level 1 pins
  conformity with that ledger, not its correctness. An honest D-algebra engine may
  legitimately disagree with a row sign; per SPEC preamble this must be reported, not
  silently matched.
- **R3 — dotted-sector mirror details.** "Mirror for dotted" fixes the raising rule
  only as a pair statement; the anchors pin $\bar D^2$ and $\bar\theta^2$ jointly
  (through $(\bar D^2\bar\theta^2)|=-4$ and the saturation identities), but the split
  of $\bar D^2$ into an ordered product $2\bar D_{?}\bar D_{?}$ and the sign in
  $\bar D^{\dot\pm}=\pm\bar D_{\dot\mp}$ are exercised at level 1 only through the
  specific contractions of the seed's 8 rows. Single-$\bar D$ jet signs at two loops
  (output jets $\bar D_{\dot a}$-words, and cross-engine row-level comparisons) rest on
  a convention choice that the gates constrain but do not uniquely fix; only
  consistently-used choices give gate-equal totals.
- **R4 — per-line momentum-direction convention.** The realization
  $\{D_a,\bar D_{\dot a}\}=2\mathsf p_{a\dot a}(q)$ with "$q$ INTO the point" needs a
  global orientation rule (which end of each line sees $+q$). Level 1 validates one
  triangle orientation; the kite's five-line orientation is fixed by SPEC declaration,
  and level 2 (relabeling invariance) tests only internal consistency, not the
  declaration itself. The configuration "external leg on a cubic vertex sharing two
  internal lines with the insertion-adjacent loop" is exercised at one loop only
  through the $Y_2$ analog; the $X_3$-end conventions are otherwise new.
- **R5 — $\mathfrak k_{AB}=0$.** The seed/SPEC vertices use $f_{AB}=h\kappa_{AB}$;
  the topological term $i\mathfrak k_{AB}$ of (5A.2) is silently dropped and no gate
  tests it. This is a theory/scheme restriction that should be recorded as such.
- **R6 — (pinned, recorded for completeness).** Berezin orientation and $\theta^2$
  convention are NOT residual: $(D^2\theta^2)|=-4$ with $D^2=2D_-D_+$ forces
  $\theta^2=\theta^a\theta_a$, and $\int d^4\theta\,\delta^4(\theta)=1$ with
  $\delta^4=\theta^2\bar\theta^2$ then fixes the measure. Similarly the ordering of
  the two insertion-leg operators inside $\mathcal I_{(2)}$ is pinned by the seed §5
  definition (leg-1 word left of leg-2 word).
