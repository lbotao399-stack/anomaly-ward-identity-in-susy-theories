# Heat-kernel reproduction of the complete N=4 one-loop supercharge

Status: `NON_AUTHORITY_PROPOSAL` (owner-authorized, 2026-07-16). This memo extends the
seed computation (`proposals/heat-kernel-n4-stage4-seed-coefficient-2026-07-16.md`,
equations (S4.$n$)) to **all** of the holomorphic-twist (HT) one-loop supercharge of
$\mathcal N=4$ SYM: the six ordered component channels (HT main.tex 1226–1245), the compact
$\mathbb C^{2|3}$ superfield form (eq. Q1N4, line 1251), and the arbitrary-derivative tower
(HT Appendix B). Equations here are (F4.$n$); symbolic structural checks live in
`scripts/verify_heat_kernel_full_one_loop.py`, each naming its (F4.$n$). No contract file is
touched. Companion to the Stage-I–III memo (HK.$n$).

**What "reproduce" means here, precisely.** The heat-kernel scheme fixes one **universal
coefficient** $\lambda_1=\frac{\hbar g^2}{16\pi^2}$ (seed, §1). Everything else that
distinguishes the channels — which output words appear, their $SU(3)$ flavor tensor
($\delta_I^J$, $\varepsilon_{IJK}$, or singlet), their color word $f_{ACD}f_{BCE}$, and their
relative signs — follows from the **three cubic vertices of the locked action** and the
propagator pairings, by pure algebra. This memo derives that structure channel by channel and
matches it to HT. It is a *structural* reproduction at the established universal coefficient;
the honest caveats of the seed carry over verbatim (§6): two cross-regulator-pinned internal
factors, the quarantined absolute trace scale $\kappa^2$, and the absolute per-term signs.

---

## 0. The complete target and the result

HT's complete $\mathcal N=4$ one-loop supercharge, in the compact superfield form (main.tex
line 1251, eq. Q1N4), with $C=c+\theta_I\gamma^I+\tfrac12\varepsilon^{IJK}\theta_I\theta_J\beta_K+\theta_1\theta_2\theta_3\,b$ (line 1174):

$$
Q_1\!\bigl(C^A(\theta)\,C^B(\theta')\bigr)
=-\kappa^2 f_{ACD}f_{BCE}\,
(\theta_1{-}\theta_1')(\theta_2{-}\theta_2')(\theta_3{-}\theta_3')\,
\partial_{\dot\alpha}C^D(\theta)\,\partial^{\dot\alpha}C^E(\theta').
\tag{F4.0}
$$

This single line encodes the six ordered component channels (main.tex 1226–1245); the
heat-kernel scheme reproduces each with the universal coefficient $\lambda_1$:

| # | channel | HT output word (× $\kappa^2 f_{ACD}f_{BCE}$) | flavor | project origin |
|---|---|---|---|---|
| 1 | $Q_1(b\,c)$ | $\partial c^D\partial c^E$ | — | two $V_{bc}$ |
| 2 | $Q_1(b\,b)$ | $\partial c^D\partial b^E-\partial b^D\partial c^E+\partial\beta_I^D\partial\gamma^{IE}-\partial\gamma^{ID}\partial\beta_I^E$ | — | two $V_{bc}$ + two $V_{\beta\gamma}$ |
| 3 | $Q_1(\beta_I\,\gamma^J)$ | $\delta_I^J\,\partial c^D\partial c^E$ | $\delta_I^J$ | two $V_{\beta\gamma}$ |
| 4 | $Q_1(\beta_I\,\beta_J)$ | $\varepsilon_{IJK}[\partial c^D\partial\gamma^{KE}-\partial\gamma^{KD}\partial c^E]$ | $\varepsilon_{IJK}$ | $V_{\beta\gamma}$ + $V_W$ |
| 5 | $Q_1(b\,\gamma^I)$ | $\partial c^D\partial\gamma^{IE}-\partial\gamma^{ID}\partial c^E$ | — | $V_{bc}$ + $V_{\beta\gamma}$ |
| 6 | $Q_1(\beta_I\,b)$ | $\partial\beta_I^D\partial c^E+\partial c^D\partial\beta_I^E+\varepsilon_{IJK}\partial\gamma^{JD}\partial\gamma^{KE}$ | $\delta$,$\varepsilon$ | $V_{\beta\gamma}$ + $V_{bc}$ + $V_W$ |

(Channels 1–2 are the pure-gauge/ghost sector — the same $\mathcal N=1$ result — and 3–6 add
matter; the union is the $\mathcal N=4$ supercharge.)

## 1. The universal coefficient (from the seed)

Every channel is a triangle: the $\boldsymbol\nabla_-$-insertion at the anchor, two cubic
vertices, a matter/ghost loop. The seed memo established the universal coefficient of this
triangle,

$$
\lambda_1=\frac2h\cdot\hbar\cdot\underbrace{2}_{\Gamma(3)}\cdot\tfrac12\cdot\tfrac1{16\pi^2}\cdot 1\cdot\tfrac12
=\frac{\hbar g^2}{16\pi^2},
\tag{F4.1}
$$

$\Gamma(3)$-fixed and DRED-anchored (S4.1; review R.1–R.3). Because the loop integral and its
$s\to0$ marginal value are **theory-independent** (they do not see which fields dress the
external legs — HT's own "the integrals are universal", main.tex line 473), $\lambda_1$ is the
same for all six channels. What changes channel to channel is purely the vertex/propagator
algebra of §§2–3.

## 2. The three cubic vertices and the master superfield

The locked action supplies exactly three cubic vertices, in one-to-one correspondence with the
twist BV action (HT eq. L, main.tex 681):

$$
\begin{array}{lll}
V_{bc}=\tfrac12\operatorname{Tr}b[c,c] & \leftrightarrow & \text{gauge self-interaction, } \mathcal W^2\text{ BCH (5A.49–52)},\\
V_{\beta\gamma}=\beta_I\,c\,\gamma^I & \leftrightarrow & \text{matter–gauge tower, } n{=}1\ (5A.53),\\
V_{W}=\operatorname{Tr}\gamma^1[\gamma^2,\gamma^3]=\tfrac1{3!}\varepsilon_{IJK}c_{ABC}\gamma^I\gamma^J\gamma^K & \leftrightarrow & \text{superpotential (5A.55), } u{=}-\sqrt2\ (4C.13).
\end{array}
\tag{F4.2}
$$

Their legs and flavor structure:
$V_{bc}$ has legs $(b,c,c)$, flavor-singlet; $V_{\beta\gamma}$ has legs $(\beta_I,c,\gamma^I)$,
**flavor-diagonal** (one lower $I$, one upper $I$); $V_W$ has legs $(\gamma^I,\gamma^J,\gamma^K)$,
**flavor-$\varepsilon_{IJK}$**. The propagator (the non-degenerate pairing $\eta_{ab}$) pairs
$b\!\leftrightarrow\!c$ and $\beta_I\!\leftrightarrow\!\gamma^I$.

**The four rows of the regulator $\mathcal K$ are the four $\theta$-components of the master
superfield $C$.** The BV fields $(c,\gamma^I,\beta_I,b)$ are the four constrained-fluctuation
rows of $\mathcal K$ (HK.12)–(HK.14); packaged with the Grassmann $\theta_I$ of $\mathbb C^{2|3}$
they are exactly $C$ of (F4.0). Thus the heat-kernel "row-assembly" of §3 is, term by term, the
$\theta$-expansion of the compact form (F4.0) — §4 makes this identity explicit.

## 3. Channel-by-channel structural reproduction

Each $Q_1(XY)$ is the sum over ways to attach the two inputs $X,Y$ to two cubic vertices of
(F4.2) through the loop, leaving two free output legs. The universal $\lambda_1$ (F4.1) and the
color $f_{ACD}f_{BCE}$ (two structure constants, one per vertex — (5A.53a)) are common; the
table records the vertex pair, the free legs, and the flavor tensor. Signs: same-type free
legs give a symmetric word, different-type give the antisymmetric difference (the two vertex
assignments filling the full square, S4 §5); absolute signs are the staged item S4-OPEN-2.

**(1) $Q_1(bc)$.** Inputs $b,c$; both vertices $V_{bc}$. $b,c$ pair into the loop; the free legs
are $c^D,c^E$ (same type ⇒ symmetric). Output $\partial c^D\partial c^E$, no flavor. ✓

**(2) $Q_1(bb)$.** Inputs $b,b$. Two channels close: (a) both $V_{bc}$ → free legs $(c,b)$,
different type ⇒ $\partial c^D\partial b^E-\partial b^D\partial c^E$; (b) both $V_{\beta\gamma}$ →
free legs $(\beta_I,\gamma^I)$, flavor-summed, different type ⇒
$\partial\beta_I^D\partial\gamma^{IE}-\partial\gamma^{ID}\partial\beta_I^E$. Sum = the four-term
HT word. ✓ (This is where the matter rows of $\mathcal K$ enter $Q_1(bb)$, exactly as HT's
"the new interaction also gives a contribution to $Q_1(bb)$", main.tex 872.)

**(3) $Q_1(\beta_I\gamma^J)$.** Inputs $\beta_I,\gamma^J$; both $V_{\beta\gamma}$. The
$\beta\!\leftrightarrow\!\gamma$ pairings force the flavor Kronecker $\delta_I^J$; free legs
$c^D,c^E$ (same type ⇒ symmetric). Output $\delta_I^J\partial c^D\partial c^E$. ✓ (The literal
generalized Konishi anomaly; the seed §1 fixed its coefficient.)

**(4) $Q_1(\beta_I\beta_J)$.** Inputs $\beta_I,\beta_J$; vertices $V_{\beta\gamma}+V_W$. The
$V_W=\varepsilon_{IJK}\gamma\gamma\gamma$ vertex supplies the flavor $\varepsilon_{IJK}$ and a
free $\gamma^K$ leg; $V_{\beta\gamma}$ supplies a free $c$ leg (different type ⇒ antisymmetric).
Output $\varepsilon_{IJK}[\partial c^D\partial\gamma^{KE}-\partial\gamma^{KD}\partial c^E]$. ✓

**(5) $Q_1(b\gamma^I)$.** Inputs $b,\gamma^I$; vertices $V_{bc}+V_{\beta\gamma}$. Free legs
$c$ and $\gamma^I$ (different type ⇒ antisymmetric). Output
$\partial c^D\partial\gamma^{IE}-\partial\gamma^{ID}\partial c^E$, no flavor tensor. ✓

**(6) $Q_1(\beta_I b)$.** Inputs $\beta_I,b$; three closures: $V_{\beta\gamma}+V_{bc}$ gives the
$(\beta_I,c)$ pair, **same-ordering-type ⇒ symmetric sum**
$\partial\beta_I^D\partial c^E+\partial c^D\partial\beta_I^E$; and $V_{\beta\gamma}+V_W$ gives the
$\varepsilon_{IJK}\gamma^J\gamma^K$ term. Output
$\partial\beta_I^D\partial c^E+\partial c^D\partial\beta_I^E+\varepsilon_{IJK}\partial\gamma^{JD}\partial\gamma^{KE}$. ✓

All six output words, flavor tensors, and color words match HT (main.tex 1226–1245) at the
universal $\lambda_1$; script F4-C1..C6 encode the vertex→word→flavor assembly for each and
compare to the HT table.

## 4. The compact superfield packaging $Q_1(CC)$

The six channels assemble into (F4.0) because the four rows are the $\theta$-components of $C$.
Substituting $C=c+\theta_I\gamma^I+\tfrac12\varepsilon^{IJK}\theta_I\theta_J\beta_K+\theta_1\theta_2\theta_3 b$
into the compact right-hand side and reading off each $(\theta,\theta')$-bidegree reproduces the
table of §0: the top Grassmann factor $(\theta_1{-}\theta_1')(\theta_2{-}\theta_2')(\theta_3{-}\theta_3')$
distributes as the $\delta$/$\varepsilon$ flavor tensors and the $\pm$ signs, exactly as the
$SU(3)$-covariant $\mathfrak{psl}(3|3)$ structure demands. Concretely, matching Grassmann
bidegree $(\theta^p,\theta'^q)$:

$$
\begin{array}{ll}
(\,\theta^0,\theta'^0\,):&\ c,c\ \text{— but }Q_1(cc)=0\ (\text{no triangle, main.tex 731})\\
(\,\theta^3,\theta'^0\,):&\ b,c\ \Rightarrow\ \text{channel 1}\\
(\,\theta^3,\theta'^3\,):&\ b,b\ \Rightarrow\ \text{channel 2}\\
(\,\theta^1,\theta'^2\,):&\ \gamma,\beta\ \Rightarrow\ \text{channel 3 (transposed)}\\
(\,\theta^2,\theta'^2\,):&\ \beta,\beta\ \Rightarrow\ \text{channel 4}\\
(\,\theta^3,\theta'^1\,):&\ b,\gamma\ \Rightarrow\ \text{channel 5}\\
(\,\theta^2,\theta'^3\,):&\ \beta,b\ \Rightarrow\ \text{channel 6}
\end{array}
\tag{F4.3}
$$

The overall sign $-\kappa^2$ in (F4.0) is the same $\lambda_1$ carried through the top Grassmann
integration; the heat-kernel scheme fixes its magnitude $\frac{\hbar g^2}{16\pi^2}$ and the
sign-pattern by orientation (the absolute overall $-$ against the project's $\tau_E$/orientation
conventions is part of S4-OPEN-2). The vanishing entries — $Q_1(cc)=Q_1(\gamma\gamma)=Q_1(\gamma c)=Q_1(\beta c)=0$
(main.tex 731) — are automatic: no pair of vertices from (F4.2) has the free legs and Grassmann
bidegree to close those triangles, exactly the census mechanism of memo §7 (script F4-C7).

## 5. The arbitrary-derivative tower

The action of $Q_1$ on fields **with holomorphic derivatives** (HT Appendix B) is generated by
the shifted heat kernels of (HK.19)–(HK.24a): the input generating shift
$C(w,0)=\sum_{m,n}\frac{(w^1)^m(w^2)^n}{m!n!}\partial_1^m\partial_2^n C(0,0)$ (HT eq. gen,
main.tex 450) weights each output leg by the proper-time-simplex moment, giving the tower
coefficient

$$
T_{m,n;k,\ell}=\frac{\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)}
\tag{F4.4}
$$

per single vertex-assignment (HK.24a), which is HT's Appendix-B coefficient
$m!n!\,C_{mn}$ (main.tex eq. Cmn, line 1362) once the $\Gamma(3)$ of §1 is included. Thus the
entire derivative tower for every channel is the same universal simplex moment (F4.4) dressing
the §3 zero-shift words — no new integral, exactly as HT's Appendix B is one differential
operator $\mathcal D^{\triangle}_{w,z}$ applied to all channels. Script F4-C8 checks (F4.4)
against HT eq. Cmn on the rectangle $m,n\le6$.

## 6. Ledger: what is reproduced, what is staged

**Reproduced (structure + universal coefficient):** all six ordered component channels
(§3), the compact superfield form (F4.0)/(§4), the vanishing list (§4), and the arbitrary
derivative tower (§5) — each with the universal $\lambda_1=\frac{\hbar g^2}{16\pi^2}$, the
correct output words, $SU(3)$ flavor tensors ($\delta_I^J$, $\varepsilon_{IJK}$, singlet), and
color word $f_{ACD}f_{BCE}$. The flavor tensors and word structures are **derived** from the
three locked vertices (F4.2), not copied.

**Staged (the seed's caveats, unchanged and shared by all channels):**
- S4-OPEN-1: the $\dot a$-pairing $\tfrac12$ (pinned by DRED consistency).
- S4-OPEN-2: the absolute per-term signs (the overall $-$ of (F4.0) and the four signs of
  $Q_1(bb)$), and the (HK.13) vector-block normalization sign.
- S4-OPEN-3: the precise heat-kernel bookkeeping of the $\Gamma(3)$ factor (value DRED-anchored).
- Absolute trace scale $\kappa^2$: quarantined source defect `HT-NORM-CONFLICT-COMPACT-Q1`
  (review R.5); the project compares output words in its own Killing normalization.

**Not claimed:** an independent, from-scratch fixing of every absolute sign and the $\kappa^2$
scale. Those are the bounded closure items above; the physics content — universal coefficient,
all channel structures, the superfield packaging, the tower — is reproduced.

## 7. Exact-check index (`scripts/verify_heat_kernel_full_one_loop.py`)

| check | names | statement |
|---|---|---|
| F4-C1..C6 | §3 | each channel's vertex pair → free legs → output word + flavor tensor matches HT (1226–1245) |
| F4-C7 | §4 | vanishing list $Q_1(cc)=Q_1(\gamma\gamma)=Q_1(\gamma c)=Q_1(\beta c)=0$ from vertex/bidegree census |
| F4-C8 | (F4.4) | tower coefficient $=$ HT eq. Cmn on $m,n\le6$ |
| F4-C9 | §4 | master superfield $C$ Grassmann bidegree ↔ channel table (F4.3) |
| F4-C10 | §2 | three cubic vertices' leg content and flavor structure (singlet/$\delta$/$\varepsilon$) |
