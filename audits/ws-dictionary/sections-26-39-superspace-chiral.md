# Weinberg--Srednicki--Project audit: draft sections 26--39

## Source ledger

| Key | Local snapshot or contract | Notion page id | Notion URL |
|---|---|---|---|
| `W26.2` | `references/vendor/notion/weinberg/26-02-general-superfields-34cee2b74b3f8182a538e629f277c1e7.md` | `34cee2b74b3f8182a538e629f277c1e7` | https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7 |
| `W26.3` | `references/vendor/notion/weinberg/26-03-chiral-linear-superfields-34cee2b74b3f8163b3b3fa265e1815b0.md` | `34cee2b74b3f8163b3b3fa265e1815b0` | https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0 |
| `W26.4` | `references/vendor/notion/weinberg/26-04-renormalizable-chiral-theories-34cee2b74b3f81f6bba1c92f1c61727b.md` | `34cee2b74b3f81f6bba1c92f1c61727b` | https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b |
| `W26A` | `references/vendor/notion/weinberg/26-appendix-majorana-spinors-34cee2b74b3f81349f82dd4d257ba62c.md` | `34cee2b74b3f81349f82dd4d257ba62c` | https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c |
| `S36` | `references/vendor/notion/srednicki/36-spinor-lagrangians-b41fbf43fd9247d280fe27cace58ea52.md` | `b41fbf43fd9247d280fe27cace58ea52` | https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52 |
| `S95` | `references/vendor/notion/srednicki/95-supersymmetry-0151805c7e85457a9928fcfd0e83da2a.md` | `0151805c7e85457a9928fcfd0e83da2a` | https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a |
| `P2A` | `contracts/foundations/step-02a-flat-superspace.md` | -- | -- |

No labelled Codex supplement, translator replacement, or unattributed editorial block is used as author evidence.

## Independent ledgers

Weinberg:

$$
[Q_W,S\}=i\mathcal Q_WS,
\qquad
\mathcal Q_W=-\frac{\vec\partial}{\partial\bar\Theta_W}
+\gamma_W^\mu\Theta_W\partial_\mu,
$$

$$
\mathcal D_W=-\frac{\vec\partial}{\partial\bar\Theta_W}
-\gamma_W^\mu\Theta_W\partial_\mu.
$$

[`W26.2:18-72`] [`W26.2:355-394`]

Srednicki:

$$
\mathcal Q_{S,a}=\partial_a+i\sigma^\mu_{a\dot b}\theta^{*\dot b}\partial_\mu,
\qquad
\mathcal Q^*_{S,\dot a}=-\partial^*_{\dot a}-i\theta^b\sigma^\mu_{b\dot a}\partial_\mu,
$$

$$
\mathcal D_{S,a}=\partial_a-i\sigma^\mu_{a\dot b}\theta^{*\dot b}\partial_\mu,
\qquad
\mathcal D^*_{S,\dot a}=-\partial^*_{\dot a}+i\theta^b\sigma^\mu_{b\dot a}\partial_\mu.
$$

[`S95:27-107`]

Project:

$$
\mathsf P^L_\mu=-i\partial_\mu,
\qquad
\mathsf Q_C=-i\mathcal Q_S,
\qquad
D_C=\mathcal D_S.
$$

[`P2A:168-219`] [`P2A:240-398`]

### 26. Weinberg four-component notation -- `CORRECTED`

The draft's $P=i\partial$ merges Noether and coordinate representations. The source-closed statements are

$$
[P_\mu,S]=+i\partial_\mu S,
\qquad
\mathsf P_\mu=-i\partial_\mu,
\qquad
[\mathsf P_\mu+P_\mu,S]=0.
$$

[`W26.2:88-93`] [`P2A:168-219`]

The draft also replaces Weinberg's derivative $\vec\partial/\partial\bar\Theta$ by an unindexed $\partial/\partial\Theta$. The correct operators are those in the Weinberg ledger. [`W26.2:18-72`] [`W26.2:355-394`]

### 27. Srednicki two-component notation -- `CORRECTED`

$$
\{\mathcal Q_{S,a},\mathcal Q^*_{S,\dot b}\}
=-2i\sigma^\mu_{a\dot b}\partial_\mu,
\qquad
\{\mathcal D_{S,a},\mathcal D^*_{S,\dot b}\}
=+2i\sigma^\mu_{a\dot b}\partial_\mu.
$$

All same-chirality brackets vanish and every $\mathcal D_S$ anticommutes with every $\mathcal Q_S$. [`S95:54-107`] The correction is categorical: these are differential operators, not the Noether charges denoted by the same undecorated letters in the draft.

In the project primitive barred basis,

$$
\partial^*_{S,\dot a}=-\bar\partial_{C,\dot a},
\qquad
\mathsf Q_C=-i\mathcal Q_S,
\qquad
D_C=\mathcal D_S.
$$

[`P2A:30-85`] [`P2A:240-398`]

### 28. Superspace-coordinate bridge -- `CORRECTED`

Define

$$
\Theta_S^{(4)}:=\begin{pmatrix}\theta_a\\ \theta^{*\dot a}\end{pmatrix}.
$$

Srednicki directly defines the conjugate coordinates at [`S95:27-43`]. Applying his four-component matrix convention to the dictionary package, then comparing with Weinberg's Majorana coordinate, derives

$$
\Theta_W=e^{i\phi_\Theta}\Theta_S^{(4)},
\qquad
e^{2i\phi_\Theta}=-1,
\qquad
e^{i\phi_\Theta}=\pm i.
$$

[`W26A:23-78`] [`S36:358-422`]

The dictionary branch

$$
\Theta_W=-i\Theta_S^{(4)},
\qquad
\bar\Theta_W=+i\bar\Theta_S^{(4)}
$$

is valid, but the draft incorrectly presents it as the unique consequence of reality. The component branch $\Psi_W=+i\Psi_S$ is independent until the chiral expansion is matched.

### 29. Chiral constraint -- `VERIFIED`

$$
\mathcal D_{R,W}:=P_-^W\mathcal D_W,
\qquad
\mathcal D_{R,W}\Phi_W=0.
$$

[`W26.3:226-249`]

Since $P_-^W=P_R^S$,

$$
\mathcal D_{R,W}\Phi_W=0
\longleftrightarrow
\mathcal D^*_{S,\dot a}\Phi_S=0
\longleftrightarrow
\bar D_{C,\dot a}\Phi_C=0.
$$

[`S95:110-154`] [`P2A:352-398`]

### 30. Chiral coordinates -- `VERIFIED`

$$
x_{+,W}^\mu=x^\mu+\frac12\bar\Theta_W\gamma_{5W}\gamma_W^\mu\Theta_W.
$$

[`W26.3:196-205`]

With $\gamma_W=-i\gamma_S$, $\gamma_{5W}=-\gamma_{5S}$, and $\Theta_W=-i\Theta_S^{(4)}$,

$$
\bar\Theta_W\gamma_{5W}\gamma_W^\mu\Theta_W
=i\bar\Theta_S^{(4)}\gamma_{5S}\gamma_S^\mu\Theta_S^{(4)}.
$$

The explicit blocks give

$$
\bar\Theta_S^{(4)}\gamma_{5S}\gamma_S^\mu\Theta_S^{(4)}
=-\theta\sigma^\mu\theta^*+\theta^*\bar\sigma^\mu\theta
=-2\theta\sigma^\mu\theta^*.
$$

Therefore

$$
x_{+,W}^\mu=x^\mu-i\theta\sigma^\mu\theta^*=y_S^\mu=y_C^\mu.
$$

[`S95:135-161`] [`P2A:400-429`]

### 31. Weinberg chiral superfield -- `CORRECTED`

Weinberg gives

$$
\Phi_W=\phi(x_+)
-\sqrt2\Theta_{L,W}^{\mathrm T}\varepsilon_{4,W}\psi_{L,W}(x_+)
+\mathcal F_W(x_+)\Theta_{L,W}^{\mathrm T}\varepsilon_{4,W}\Theta_{L,W}.
$$

[`W26.3:196-205`]

The branch-complete component map is

$$
\phi_W=A_S,
\qquad
\psi_W=+i\begin{pmatrix}\psi_{S,a}\\ \psi_S^{\dagger\dot a}\end{pmatrix},
\qquad
\mathcal F_W=F_S,
$$

$$
-\Theta_{L,W}^{\mathrm T}\varepsilon_{4,W}\psi_{L,W}=\theta\psi_S,
\qquad
\Theta_{L,W}^{\mathrm T}\varepsilon_{4,W}\Theta_{L,W}=\theta^2.
$$

The draft's formulas are correct only after the two residual signs in sections 14 and 28 are declared jointly; this missing branch statement is the correction.

Srednicki component source: [`S95:155-161`].

### 32. Srednicki chiral expansion -- `VERIFIED`

$$
\Phi_S(y,\theta)=A(y)+\sqrt2\theta\psi(y)+\theta^2F(y),
$$

$$
\begin{aligned}
\Phi_S(x,\theta,\theta^*)={}&A+\sqrt2\theta\psi+\theta^2F
-i(\theta\sigma^\mu\theta^*)\partial_\mu A\\
&-\frac{i}{\sqrt2}\theta^2\theta^*\bar\sigma^\mu\partial_\mu\psi
+\frac14\theta^2\theta^{*2}\Box A.
\end{aligned}
$$

[`S95:155-185`]

The quartic coefficient follows from

$$
\frac12(-i)^2
(\theta\sigma^\mu\theta^*)(\theta\sigma^\nu\theta^*)
\partial_\mu\partial_\nu A
=\frac14\theta^2\theta^{*2}\Box A.
$$

### 33. Weinberg expansion at fixed x -- `VERIFIED`

Weinberg's source form is

$$
\begin{aligned}
\Phi_W={}&\phi-\sqrt2\bar\Theta_W\psi_{L,W}
+(\bar\Theta_WP_+^W\Theta_W)\mathcal F_W\\
&+\frac12(\bar\Theta_W\gamma_{5W}\gamma_W^\mu\Theta_W)\partial_\mu\phi\\
&-\frac1{\sqrt2}(\bar\Theta_W\gamma_{5W}\Theta_W)
(\bar\Theta_W\not\!\partial_W\psi_{L,W})
-\frac18(\bar\Theta_W\gamma_{5W}\Theta_W)^2\Box\phi.
\end{aligned}
$$

[`W26.3:129-165`]

The draft's cubic term uses

$$
+\frac1{\sqrt2}(\bar\Theta\gamma_5\Theta)
(\bar\Theta\gamma_5\not\!\partial\psi_L)
=-\frac1{\sqrt2}(\bar\Theta\gamma_5\Theta)
(\bar\Theta\not\!\partial\psi_L),
$$

because $\gamma_5\not\!\partial\psi_L=-\not\!\partial\psi_L$. Thus it is equivalent to the source.

Moreover,

$$
\bar\Theta_W\gamma_{5W}\Theta_W=\theta^2-\theta^{*2},
\qquad
(\bar\Theta_W\gamma_{5W}\Theta_W)^2=-2\theta^2\theta^{*2},
$$

so the last term is $+\frac14\theta^2\theta^{*2}\Box A$.

### 34. D-component conversion -- `CORRECTED`

$$
-\frac14(\bar\Theta_W\gamma_{5W}\Theta_W)^2
\left([X]^W_D+\frac12\Box C_X\right)
=\theta^2\theta^{*2}
\left(\frac12[X]^W_D+\frac14\Box C_X\right),
$$

For the same W/S-paired real scalar superfield, with matched lowest component $C_X$, the dictionary extends Srednicki's coefficient notation by

$$
X_S\supset\theta^2\theta^{*2}[X]^S_D.
$$

Therefore the pointwise relation is

$$
[X]^S_D=\frac12[X]^W_D+\frac14\Box C_X.
$$

Only after spacetime integration with a vanishing boundary term,

$$
\int d^4x\,[X]^S_D
=\frac12\int d^4x\,[X]^W_D.
$$

For a matched left-chiral superfield only,

$$
[\Phi]^W_{\mathcal F}=[\Phi]^S_F,
\qquad
\mathcal F_W=F_S.
$$

[`W26.2:135-142`] [`W26.3:196-205`] [`W26.3:275-300`] [`S95:155-161`] [`S95:253-279`] [`S95:293-321`]

The draft's additional raw-measure equalities are not needed for this component dictionary and are not certified from the cited source lines; they are removed.

### 35. Product of chiral superfields -- `VERIFIED`

$$
\begin{aligned}
\Phi_1\Phi_2={}&A_1A_2
+\sqrt2\theta(A_1\psi_2+A_2\psi_1)\\
&+\theta^2(A_1F_2+A_2F_1-\psi_1\psi_2).
\end{aligned}
$$

[`W26.3:252-265`] [`S95:233-250`]

The fermion sign is

$$
2(\theta\psi_1)(\theta\psi_2)
=-2\theta^a\theta^b\psi_{1a}\psi_{2b}
=-\theta^2\psi_1\psi_2.
$$

### 36. Superpotential notation -- `VERIFIED`

$$
f_W(\Phi)=W_S(\Phi).
$$

Weinberg names the holomorphic function $f$; Srednicki names it $W$. [`W26.3:275-304`] [`W26.4:132-151`] [`S95:246-252`]

### 37. General superspace action -- `CORRECTED`

Weinberg supports

$$
I_W=\int d^4x\left(\frac12[K]^W_D+[f]^W_{\mathcal F}+[f]^{W*}_{\mathcal F}\right).
$$

[`W26.3:275-304`]

Srednicki 95 supports only

$$
\mathcal L_S=[\Phi_i^\dagger\Phi_i]^S_D+[W(\Phi)]^S_F+\mathrm{h.c.}
$$

in the ungauged chiral sector. [`S95:280-335`]

The allowed Srednicki page does not directly state the draft's generic $[K(\Phi^\dagger,\Phi)]_D$. The corrected cross-system claim is at action level:

$$
\frac12\int d^4x\,[K]^W_D
=\int d^4x\,[K]^S_D,
$$

not the draft's pointwise equality. The generic Srednicki expression is a derived real-superfield action, not an author quotation.

### 38. Superpotential component expansion -- `VERIFIED`

$$
W(\Phi)=W(A)+W_i(\sqrt2\theta\psi_i+\theta^2F_i)
+\frac12W_{ij}(\sqrt2\theta\psi_i)(\sqrt2\theta\psi_j),
$$

$$
[W(\Phi)]_F=W_iF_i-\frac12W_{ij}\psi_i\psi_j.
$$

[`W26.4:132-151`] [`S95:246-252`]

### 39. Canonical Kahler term -- `CORRECTED`

The exact local coefficient is

$$
\begin{aligned}
[\Phi^\dagger\Phi]^S_D={}&
-\frac12\partial^\mu A^\dagger\partial_\mu A
+\frac14A\Box A^\dagger+\frac14A^\dagger\Box A\\
&+\frac i2\psi^\dagger\bar\sigma^\mu\partial_\mu\psi
-\frac i2(\partial_\mu\psi^\dagger)\bar\sigma^\mu\psi
+F^\dagger F.
\end{aligned}
$$

[`S95:280-335`]

After integration by parts, with a vanishing boundary term,

$$
\int d^4x\,[\Phi^\dagger\Phi]^S_D
=\int d^4x\left(
-\partial_\mu A^\dagger\partial^\mu A
+i\psi^\dagger\bar\sigma^\mu\partial_\mu\psi
+F^\dagger F\right).
$$

Weinberg's matching canonical term is $\frac12\int d^4x[K]^W_D$ with $K=\Phi_i^*\Phi_i$. [`W26.4:40-104`]

The auxiliary equations are

$$
F_i^\dagger=-W_i,
\qquad
F_i=-W_i^\dagger,
\qquad
V_F=W_i^\dagger W_i.
$$

[`W26.4:139-168`] [`S95:318-335`]

## P0/P1 findings

| severity | draft section | finding | resolution |
|---|---|---|---|
| P0 | 26 | Noether momentum and coordinate differential generator were identified. | Separated $[P,\Phi]=i\partial\Phi$ from $\mathsf P=-i\partial$. |
| P1 | 28, 31 | Reality fixes only $\pm i$, while the draft called each phase unique. | Declared the coordinate and component branches separately, then fixed them jointly through the chiral expansion. |
| P0 | 34 | The pointwise rule $[X]^W_D=2[X]^S_D$ omitted $\frac14\Box C_X$. | Replaced it by the exact local rule and retained the factor two only after spacetime integration. |
| P1 | 37 | A pointwise generic Kahler equality was inferred from action equivalence. | Replaced it by the integrated equality and separated derivation from author quotation. |
| P1 | 39 | The integrated-by-parts kinetic expression was labelled as the local $D$ coefficient. | Retained both the exact local coefficient and its integrated form. |
