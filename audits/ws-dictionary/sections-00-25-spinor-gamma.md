# Weinberg--Srednicki--Project audit: draft sections 0--25

## Source ledger

Citation `KEY:L1-L2` means the exact local line interval `L1-L2` in the registered snapshot below.  Each key fixes the Notion `page_id` and URL.

| Key | Local snapshot | Notion page_id | Notion URL |
|---|---|---|---|
| `W54` | `references/vendor/notion/weinberg/05-04-dirac-formalism-34cee2b74b3f8115a5a1fac623c31862.md` | `34cee2b7-4b3f-8115-a5a1-fac623c31862` | https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862 |
| `W261` | `references/vendor/notion/weinberg/26-01-direct-field-supermultiplets-34cee2b74b3f81efaf28fa4031d4303e.md` | `34cee2b7-4b3f-81ef-af28-fa4031d4303e` | https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e |
| `W26A` | `references/vendor/notion/weinberg/26-appendix-majorana-spinors-34cee2b74b3f81349f82dd4d257ba62c.md` | `34cee2b7-4b3f-8134-9f82-dd4d257ba62c` | https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c |
| `S34` | `references/vendor/notion/srednicki/34-left-right-spinor-fields-812622be5c2d466faeb4a613eabad116.md` | `812622be-5c2d-466f-aeb4-a613eabad116` | https://app.notion.com/p/812622be5c2d466faeb4a613eabad116 |
| `S35` | `references/vendor/notion/srednicki/35-spinor-indices-1da2841c4cda42669598313359e3d07d.md` | `1da2841c-4cda-4266-9583-13359e3d07d` | https://app.notion.com/p/1da2841c4cda42669598313359e3d07d |
| `S36` | `references/vendor/notion/srednicki/36-spinor-lagrangians-b41fbf43fd9247d280fe27cace58ea52.md` | `b41fbf43-fd92-47d2-80fe-27cace58ea52` | https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52 |
| `S38` | `references/vendor/notion/srednicki/38-spinor-technology-19f10ddaf77242df946f54f8c3f99be6.md` | `19f10dda-f772-42df-946f-54f8c3f99be6` | https://app.notion.com/p/19f10ddaf77242df946f54f8c3f99be6 |
| `S47` | `references/vendor/notion/srednicki/47-gamma-matrix-technology-22607397de1a4af2bc9610b320426208.md` | `22607397-de1a-4af2-bc96-10b320426208` | https://app.notion.com/p/22607397de1a4af2bc9610b320426208 |
| `S49` | `references/vendor/notion/srednicki/49-majorana-feynman-rules-1707531df3dd440bbd490a9e2b963de8.md` | `1707531d-f3dd-440b-bd49-0a9e2b963de8` | https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8 |
| `S95` | `references/vendor/notion/srednicki/95-supersymmetry-0151805c7e85457a9928fcfd0e83da2a.md` | `0151805c-7e85-457a-9928-fcfd0e83da2a` | https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a |

Project citations use:

| Key | Canonical contract |
|---|---|
| `P1` | `contracts/foundations/step-01-supersymmetry-commutator.md` |
| `P2A` | `contracts/foundations/step-02a-flat-superspace.md` |

No block labelled `Codex 补充`, translator replacement, or unattributed annotation is used below.

## Independent ledgers

### Weinberg ledger

$$
\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1),\qquad
\{\gamma_W^\mu,\gamma_W^\nu\}=2\eta^{\mu\nu}\mathbf1_4,
$$

$$
\gamma_W^0=-i\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\gamma_W^i=-i\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix},
$$

$$
\gamma_{5W}=-i\gamma_W^0\gamma_W^1\gamma_W^2\gamma_W^3
=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\beta_W=i\gamma_W^0=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Source: `W54:46-55`, `W54:238-250`, `W54:305-308`, `W54:354-365`, `W54:379-395`.

Weinberg's brackets in

$$
\gamma_W^{[\mu_1}\cdots\gamma_W^{\mu_r]}
$$

sum all signed permutations **without** the factor $1/r!$; the six-term expansion is explicit.  Source: `W54:156-180`.

### Srednicki ledger

$$
\sigma^\mu=(1,\boldsymbol\sigma),\qquad
\bar\sigma^\mu=(1,-\boldsymbol\sigma),
$$

$$
\gamma_S^\mu=\begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix},\qquad
\{\gamma_S^\mu,\gamma_S^\nu\}=-2g^{\mu\nu}\mathbf1_4,
$$

$$
\gamma_{5S}=i\gamma_S^0\gamma_S^1\gamma_S^2\gamma_S^3
=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\qquad
\beta_S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Source: `S35:20-29`, `S35:175-185`, `S36:71-92`, `S36:201-210`, `S36:441-468`.

### Canonical-project ledger

$$
\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1),\qquad
\epsilon^{0123}=+1,
$$

$$
\epsilon^{12}=\epsilon^{\dot1\dot2}=+1,\qquad
\epsilon_{12}=\epsilon_{\dot1\dot2}=-1,
$$

$$
\sigma_L^\mu=(1,\boldsymbol\sigma),\qquad
\bar\sigma_L^\mu=(1,-\boldsymbol\sigma),
$$

$$
\sigma_L^\mu\bar\sigma_L^\nu+\sigma_L^\nu\bar\sigma_L^\mu
=-2\eta^{\mu\nu}\mathbf1_2.
$$

Source: `P1:5-18`, `P1:21-49`, `P1:63-104`.

The canonical project has fixed no four-component $\gamma$, $\gamma_5$, $\beta$, charge-conjugation matrix, Dirac spinor, Majorana condition, four-component Fierz basis, or Dirac/Majorana Lagrangian.  Every such project entry below is therefore `PROJECT_UNFIXED`.

## Section audit

### 0. Symbols -- `CORRECTED`

The draft's unified Clifford parameter is correct:

$$
\kappa_W=+1,\qquad \kappa_S=-1,
\qquad
\{\gamma_\bullet^\mu,\gamma_\bullet^\nu\}
=2\kappa_\bullet\eta^{\mu\nu}\mathbf1_4.
$$

Source: Weinberg `W54:46-55`; Srednicki `S36:77-87`.

The global definition

$$
\gamma^{\mu_1\cdots\mu_r}
:=\gamma^{[\mu_1}\cdots\gamma^{\mu_r]},
\qquad [\cdots]\text{ contains }1/r!,
$$

is not Weinberg notation.  Define an audit-only normalized product

$$
\Gamma_\bullet^{\mu_1\cdots\mu_r}
:=\frac1{r!}\sum_{\pi\in S_r}\operatorname{sgn}(\pi)
\gamma_\bullet^{\mu_{\pi(1)}}\cdots\gamma_\bullet^{\mu_{\pi(r)}}.
$$

Then

$$
\gamma_W^{[\mu_1}\cdots\gamma_W^{\mu_r]}
=r!\,\Gamma_W^{\mu_1\cdots\mu_r}.
$$

Source: Weinberg `W54:156-180`.  The draft's $T^A$, $[X]_F$, $[X]_D$, $W_i$, and $W_{ij}$ are not claims in sections 0--25 and are `NOT_IN_SCOPE` here.  Project: four-component objects `PROJECT_UNFIXED`.

### 1. Metric and spacetime epsilon -- `VERIFIED`

For Srednicki, $\sigma^0=\bar\sigma^0=1$ and

$$
\sigma^0\bar\sigma^0+\sigma^0\bar\sigma^0
=2=-2g^{00}
$$

give $g^{00}=-1$.  For $i=1,2,3$,

$$
\bar\sigma^i=-\sigma^i,\qquad (\sigma^i)^2=1,
$$

so

$$
\sigma^i\bar\sigma^i+\sigma^i\bar\sigma^i=-2=-2g^{ii},
$$

hence $g^{ii}=+1$.  Source: `S35:20-29`, `S35:175-185`, `S36:77-86`.

For Weinberg, $(\gamma_W^0)^2=-1$, $(\gamma_W^i)^2=+1$, and $\{\gamma_W^\mu,\gamma_W^\nu\}=2\eta^{\mu\nu}$ give the same metric.  Source: `W54:46-55`, `W54:238-250`.

Both fix $\epsilon^{0123}=+1$: Weinberg `W54:292-308`; Srednicki `S47:151-164`.  Therefore

$$
\epsilon_{0123}
=\eta_{00}\eta_{11}\eta_{22}\eta_{33}\epsilon^{0123}
=(-1)(+1)(+1)(+1)(+1)=-1.
$$

Project: `P1:14-18` agrees exactly.

### 2. Pauli and sigma matrices -- `VERIFIED`

Srednicki fixes

$$
\sigma^\mu=(1,\boldsymbol\sigma),\qquad
\bar\sigma^\mu=(1,-\boldsymbol\sigma),
$$

and the two sigma anticommutators with coefficient $-2g^{\mu\nu}$.  Source: `S35:20-29`, `S35:175-185`, `S36:77-86`.

Weinberg uses the same three Pauli matrices inside his explicit chiral blocks.  Source: `W54:238-250`.

Project: `P1:63-104` is exactly the Srednicki two-component system.

### 3. Srednicki gamma matrices -- `VERIFIED`

$$
\gamma_S^\mu=\begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}.
$$

Then

$$
\{\gamma_S^\mu,\gamma_S^\nu\}
=\begin{pmatrix}
\sigma^\mu\bar\sigma^\nu+\sigma^\nu\bar\sigma^\mu&0\\
0&\bar\sigma^\mu\sigma^\nu+\bar\sigma^\nu\sigma^\mu
\end{pmatrix}
=-2\eta^{\mu\nu}\mathbf1_4.
$$

Source: `S36:71-87`.  Project: `PROJECT_UNFIXED`; the project has fixed only the $2\times2$ sigma system.

### 4. Weinberg gamma matrices -- `VERIFIED`

In the displayed chiral bases,

$$
\gamma_W^0=-i\begin{pmatrix}0&1\\1&0\end{pmatrix}
=-i\gamma_S^0,
$$

$$
\gamma_W^i=-i\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}
=-i\gamma_S^i.
$$

Thus

$$
\boxed{\gamma_W^\mu=-i\gamma_S^\mu},
$$

and

$$
\{\gamma_W^\mu,\gamma_W^\nu\}
=(-i)^2\{\gamma_S^\mu,\gamma_S^\nu\}
=-(-2\eta^{\mu\nu})
=2\eta^{\mu\nu}.
$$

Source: Weinberg `W54:238-250`; Srednicki `S36:71-87`.  This equality is basis-specific; an independent similarity transformation changes it.  Project: `PROJECT_UNFIXED`.

### 5. Gamma five -- `VERIFIED`

Weinberg: `W54:305-308`, `W54:354-365`.

Srednicki: `S36:441-468`.

Using $\gamma_W^\mu=-i\gamma_S^\mu$,

$$
\begin{aligned}
\gamma_{5W}
&=-i\gamma_W^0\gamma_W^1\gamma_W^2\gamma_W^3\\
&=-i(-i)^4\gamma_S^0\gamma_S^1\gamma_S^2\gamma_S^3\\
&=-i\gamma_S^0\gamma_S^1\gamma_S^2\gamma_S^3\\
&=-\gamma_{5S}.
\end{aligned}
$$

Therefore

$$
\gamma_{5W}=-\gamma_{5S},\qquad
\gamma_{5\bullet}^2=1,
\qquad \{\gamma_{5\bullet},\gamma_\bullet^\mu\}=0.
$$

Source for square and anticommutator: Weinberg `W54:324-345`; Srednicki `S47:13-18`.  Project: `PROJECT_UNFIXED`.

### 6. Chirality projectors -- `VERIFIED`

$$
P_\pm^W=\frac12(1\pm\gamma_{5W}),\qquad
P_L^S=\frac12(1-\gamma_{5S}),\qquad
P_R^S=\frac12(1+\gamma_{5S}).
$$

Hence

$$
P_+^W=\frac12(1-\gamma_{5S})=P_L^S,
\qquad
P_-^W=\frac12(1+\gamma_{5S})=P_R^S.
$$

Weinberg explicitly calls $\frac12(1+\gamma_{5W})s$ left-handed and $\frac12(1-\gamma_{5W})s$ right-handed.  Source: `W26A:134-140`.  Srednicki's projectors and blocks are explicit at `S36:441-460`.  Project: `PROJECT_UNFIXED`.

### 7. Beta and Hermiticity -- `CORRECTED`

Numerically, in the selected bases,

$$
\beta_W=i\gamma_W^0
=\gamma_S^0
=\beta_S
=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Source: Weinberg `W54:379-395`; Srednicki `S36:201-210`.

Srednicki explicitly warns that $\beta_S$ and $\gamma_S^0$ have different spinor-index structures despite their numerical equality.  Source: `S36:201-210`.  The draft must therefore replace “the same matrix” by “the same numerical block array in these bases.”

Weinberg gives

$$
\beta_W(\gamma_W^\mu)^\dagger\beta_W=-\gamma_W^\mu.
$$

Source: `W54:397-407`.  Srednicki gives

$$
\beta_S(\gamma_S^\mu)^\dagger\beta_S=+\gamma_S^\mu.
$$

Source: `S38:113-122`.  Since $\beta_\bullet^{-1}=\beta_\bullet$,

$$
(\gamma_\bullet^\mu)^\dagger
=-\kappa_\bullet\beta_\bullet\gamma_\bullet^\mu\beta_\bullet^{-1}.
$$

Project: `PROJECT_UNFIXED`.

### 8. Lorentz generators -- `VERIFIED`

Weinberg fixes

$$
\mathcal J_W^{\mu\nu}=-\frac{i}{4}[\gamma_W^\mu,\gamma_W^\nu]
$$

at `W54:52-56`.  Srednicki fixes

$$
S_S^{\mu\nu}=+\frac{i}{4}[\gamma_S^\mu,\gamma_S^\nu]
$$

at `S36:487-509`.  Therefore

$$
\begin{aligned}
\mathcal J_W^{\mu\nu}
&=-\frac{i}{4}(-i)^2[\gamma_S^\mu,\gamma_S^\nu]\\
&=+\frac{i}{4}[\gamma_S^\mu,\gamma_S^\nu]\\
&=S_S^{\mu\nu}.
\end{aligned}
$$

Srednicki's two-component blocks are

$$
(S_L^{\mu\nu})_a{}^b
=\frac{i}{4}(\sigma^\mu\bar\sigma^\nu-\sigma^\nu\bar\sigma^\mu)_a{}^b,
$$

$$
(S_R^{\mu\nu})^{\dot a}{}_{\dot b}
=-\frac{i}{4}(\bar\sigma^\mu\sigma^\nu-\bar\sigma^\nu\sigma^\mu)^{\dot a}{}_{\dot b}.
$$

Source: `S35:175-203`.  Project relation:

$$
S_L^{\mu\nu}=i\sigma_L^{\mu\nu},\qquad
S_R^{\mu\nu}=-i\bar\sigma_L^{\mu\nu},
$$

with project definitions at `P1:106-126`.  The project has not fixed a four-component generator.

### 9. Two-component epsilon -- `VERIFIED`

Srednicki fixes

$$
\epsilon^{12}=\epsilon^{\dot1\dot2}
=\epsilon_{21}=\epsilon_{\dot2\dot1}=+1,
$$

$$
\epsilon^{21}=\epsilon^{\dot2\dot1}
=\epsilon_{12}=\epsilon_{\dot1\dot2}=-1,
$$

and contracts the second epsilon index when raising or lowering.  Source: `S34:183-204`, `S35:12-18`.

The project is identical: `P1:21-44`.  Weinberg's Majorana appendix fixes the numerical two-component matrix

$$
e=i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

but the cited page does not give the complete two-component upper/lower-index rule.  Source: `W26A:13-22`.  Weinberg's full two-component variance dictionary is therefore `SOURCE_INSUFFICIENT` in the registered section set.

### 10. Grassmann contractions -- `VERIFIED`

Srednicki fixes

$$
\chi\psi=\chi^a\psi_a=\psi^a\chi_a=\psi\chi
$$

at `S35:213-252`.  His superspace identities are

$$
\theta_a\theta_b=\frac12\epsilon_{ab}\theta\theta,
\qquad
\theta^a\theta^b=-\frac12\epsilon^{ab}\theta\theta,
$$

$$
\theta^*_{\dot a}\theta^*_{\dot b}
=-\frac12\epsilon_{\dot a\dot b}\theta^*\theta^*,
\qquad
\theta^{*\dot a}\theta^{*\dot b}
=+\frac12\epsilon^{\dot a\dot b}\theta^*\theta^*,
$$

$$
(\theta\sigma^\mu\theta^*)(\theta\sigma^\nu\theta^*)
=-\frac12(\theta\theta)(\theta^*\theta^*)g^{\mu\nu}.
$$

Source: `S95:155-178`.  The sigma contraction is also explicit at `S35:31-54`.

Project agrees on scalar contractions: `P1:46-61`; on the sigma contraction: `P1:90-104`.  The project has not yet locked the quadratic superspace monomial identities, so that subset is `PROJECT_UNFIXED`.

### 11. Charge-conjugation matrix -- `CORRECTED`

Use $\mathcal C$ for the numerical charge-conjugation matrix.  Srednicki also uses $C$ for the unitary charge-conjugation operator, so the draft's bare $C$ conflates two objects.  Source for the operator/matrix distinction: `S36:300-322`.

In the displayed bases,

$$
\mathcal C_W=\mathcal C_S
=-i\begin{pmatrix}\sigma^2&0\\0&-\sigma^2\end{pmatrix}
=\begin{pmatrix}\epsilon_{ab}&0\\0&\epsilon^{\dot a\dot b}\end{pmatrix}.
$$

Source: Weinberg `W54:448-457`; Srednicki `S36:320-368`.

The sources give

$$
\mathcal C^T=\mathcal C^\dagger=\mathcal C^{-1}=-\mathcal C,
\qquad
\mathcal C^{-1}\gamma_\bullet^\mu\mathcal C
=-(\gamma_\bullet^\mu)^T.
$$

Source: Weinberg `W54:448-467`; Srednicki `S36:358-383`.  Hence

$$
\mathcal C^2=-1,\qquad \mathcal C^*=\mathcal C.
$$

Srednicki also fixes $\beta\mathcal C=-\mathcal C\beta$ at `S38:357-375`.  The remaining commutators follow by direct multiplication of the displayed blocks.  Project: `PROJECT_UNFIXED`.

### 12. Srednicki Dirac spinor -- `CORRECTED`

Replace the draft's matrix symbol $C$ by $\mathcal C$:

$$
\Psi_{D,S}=\begin{pmatrix}\chi_a\\\xi^{\dagger\dot a}\end{pmatrix},
\qquad
\bar\Psi_{D,S}=\Psi_{D,S}^\dagger\beta
=(\xi^a,\chi^\dagger_{\dot a}),
$$

$$
\Psi_{D,S}^{,c}:=\mathcal C\bar\Psi_{D,S}^{,T}
=\begin{pmatrix}\xi_a\\\chi^{\dagger\dot a}\end{pmatrix}.
$$

Source: `S36:169-210`, `S36:307-343`.  Formula content is verified; the draft's symbol is not source-faithful.  Project: `PROJECT_UNFIXED`.

### 13. Srednicki Majorana spinor -- `VERIFIED`

Srednicki's Majorana field is

$$
\Psi_{M,S}=\begin{pmatrix}\psi_a\\\psi^{\dagger\dot a}\end{pmatrix},
\qquad \Psi_{M,S}^{,c}=\Psi_{M,S}.
$$

Source: `S36:89-105`, `S36:386-422`.

Since

$$
\Psi_S=\mathcal C\bar\Psi_S^T
=\mathcal C\beta^T\Psi_S^*,
$$

and $\beta^T=\beta$, $\mathcal C^{-1}=-\mathcal C$, $\beta\mathcal C=-\mathcal C\beta$,

$$
\begin{aligned}
\Psi_S^*
&=\beta\mathcal C^{-1}\Psi_S\\
&=-\beta\mathcal C\Psi_S,
\end{aligned}
$$

while the same Majorana condition gives

$$
\bar\Psi_S=\Psi_S^T\mathcal C.
$$

Source inputs: `S36:358-422`, `S38:357-375`.  Project: `PROJECT_UNFIXED`.

### 14. Weinberg Majorana condition and phase -- `CORRECTED`

Weinberg fixes

$$
s^*=\beta\mathcal C s,
\qquad
\bar s=-s^T\mathcal C,
$$

because $\mathcal C=-\epsilon\gamma_5$ and $\bar s=s^T\epsilon\gamma_5$.  Source: `W26A:23-52`, `W26A:68-78`.

Let $\Psi_W=e^{i\phi}\Psi_S$.  Requiring the Weinberg condition from the Srednicki condition gives

$$
\begin{aligned}
\Psi_W^*
&=e^{-i\phi}\Psi_S^*
=-e^{-i\phi}\beta\mathcal C\Psi_S,\\
\beta\mathcal C\Psi_W
&=e^{i\phi}\beta\mathcal C\Psi_S.
\end{aligned}
$$

Thus

$$
-e^{-i\phi}=e^{i\phi},
\qquad e^{2i\phi}=-1,
\qquad e^{i\phi}=\pm i.
$$

The draft's choice

$$
\Psi_W=+i\Psi_S,
\qquad
\bar\Psi_W=-i\bar\Psi_S
$$

is valid, but it is one of two residual-sign choices, not a unique consequence.  Project: `PROJECT_UNFIXED`.

### 15. Dirac Lagrangian dictionary -- `SOURCE_INSUFFICIENT`

Srednicki explicitly fixes

$$
\mathcal L_{D,S}
=i\bar\Psi_S\gamma_S^\mu\partial_\mu\Psi_S
-m\bar\Psi_S\Psi_S.
$$

Source: `S36:264-274`.

If one defines the Weinberg Dirac normalization by

$$
\mathcal L_{D,W}
=-\bar\Psi_W\gamma_W^\mu\partial_\mu\Psi_W
-m\bar\Psi_W\Psi_W,
$$

then, with $\Psi_W=i\Psi_S$, $\bar\Psi_W=-i\bar\Psi_S$, and $\gamma_W=-i\gamma_S$,

$$
\begin{aligned}
-\bar\Psi_W\gamma_W^\mu\partial_\mu\Psi_W
&=-(-i)(-i)(i)\bar\Psi_S\gamma_S^\mu\partial_\mu\Psi_S\\
&=i\bar\Psi_S\gamma_S^\mu\partial_\mu\Psi_S,\\
-m\bar\Psi_W\Psi_W
&=-m(-i)(i)\bar\Psi_S\Psi_S\\
&=-m\bar\Psi_S\Psi_S.
\end{aligned}
$$

The registered Weinberg pages fix the corresponding Majorana sign and factor, but do not directly state this general Dirac-field Lagrangian.  The conversion is algebraically valid; exact Weinberg attribution is `SOURCE_INSUFFICIENT`.  Project: `PROJECT_UNFIXED`.

### 16. Majorana Lagrangian -- `VERIFIED`

Weinberg:

$$
\mathcal L_{M,W}
=-\frac12\bar\Psi_W\gamma_W^\mu\partial_\mu\Psi_W
-\frac12m\bar\Psi_W\Psi_W.
$$

Source: `W261:235-242`.

Srednicki:

$$
\mathcal L_{M,S}
=\frac{i}{2}\bar\Psi_S\gamma_S^\mu\partial_\mu\Psi_S
-\frac12m\bar\Psi_S\Psi_S.
$$

Source: `S36:394-437`.  The phase/gamma calculation in section 15 maps one into the other.  Project: `PROJECT_UNFIXED`.

### 17. Dirac spinor into two Weinberg-Majorana spinors -- `VERIFIED`

Define the antilinear involution

$$
R_W\Psi:=\beta\mathcal C\Psi^*.
$$

The Weinberg Majorana condition is $R_W\Psi=\Psi$ (`W26A:23-52`, `W26A:68-78`).  Set

$$
\Psi_1=\frac12(\Psi+R_W\Psi),
\qquad
\Psi_2=-\frac{i}{2}(\Psi-R_W\Psi).
$$

Using antilinearity and $R_W^2=1$,

$$
R_W\Psi_1=\Psi_1,
$$

$$
\begin{aligned}
R_W\Psi_2
&=+\frac{i}{2}(R_W\Psi-\Psi)\\
&=-\frac{i}{2}(\Psi-R_W\Psi)\\
&=\Psi_2,
\end{aligned}
$$

and

$$
\Psi_1+i\Psi_2
=\frac12(\Psi+R_W\Psi)+\frac12(\Psi-R_W\Psi)
=\Psi.
$$

Project: `PROJECT_UNFIXED`.

### 18. Bilinear dictionary -- `VERIFIED`

For the declared choice $\Psi_W=i\Psi_S$,

$$
\bar\Psi_W\Psi_W=(-i)(i)\bar\Psi_S\Psi_S
=\bar\Psi_S\Psi_S,
$$

$$
\bar\Psi_W\gamma_W^\mu\Psi_W
=(-i)(-i)(i)\bar\Psi_S\gamma_S^\mu\Psi_S
=-i\bar\Psi_S\gamma_S^\mu\Psi_S,
$$

$$
\bar\Psi_W\gamma_{5W}\Psi_W
=(-i)(-1)(i)\bar\Psi_S\gamma_{5S}\Psi_S
=-\bar\Psi_S\gamma_{5S}\Psi_S,
$$

$$
\bar\Psi_W\gamma_W^\mu\gamma_{5W}\Psi_W
=(-i)(-i)(-1)(i)
\bar\Psi_S\gamma_S^\mu\gamma_{5S}\Psi_S
=i\bar\Psi_S\gamma_S^\mu\gamma_{5S}\Psi_S,
$$

$$
\bar\Psi_W[\gamma_W^\mu,\gamma_W^\nu]\Psi_W
=(-i)(-1)(i)
\bar\Psi_S[\gamma_S^\mu,\gamma_S^\nu]\Psi_S
=-\bar\Psi_S[\gamma_S^\mu,\gamma_S^\nu]\Psi_S.
$$

Book inputs: Weinberg gamma/gamma-five at `W54:238-250`, `W54:305-365`; Srednicki at `S36:71-87`, `S36:441-468`; Majorana phase from section 14.  Project: `PROJECT_UNFIXED`.

### 19. Majorana bilinear exchange -- `VERIFIED`

Both systems have

$$
M^T=+\mathcal C M\mathcal C^{-1},
\quad M\in\{1,\gamma_5,\gamma_5\gamma^\mu\},
$$

$$
M^T=-\mathcal C M\mathcal C^{-1},
\quad M\in\{\gamma^\mu,[\gamma^\mu,\gamma^\nu]\}.
$$

Weinberg states these classes at `W26A:68-84`; Srednicki supplies $\mathcal C^{-1}\gamma^\mu\mathcal C=-(\gamma^\mu)^T$ and the complete matrix basis at `S36:370-383`, `S47:213-214`.

For Srednicki Majorana spinors, $\bar\chi=\chi^T\mathcal C$:

$$
\begin{aligned}
\bar\chi M\psi
&=\chi^T\mathcal C M\psi\\
&=-\psi^T(\mathcal C M)^T\chi\\
&=+\psi^T M^T\mathcal C\chi\\
&=\pm\psi^T\mathcal C M\chi\\
&=\pm\bar\psi M\chi.
\end{aligned}
$$

The Weinberg adjoint has an additional minus on both sides and gives the same exchange table.  In particular,

$$
\bar\psi\gamma^\mu\psi=0,
\qquad
\bar\psi[\gamma^\mu,\gamma^\nu]\psi=0.
$$

Weinberg states the complete result at `W26A:80-92`.  Project: `PROJECT_UNFIXED`.

### 20. Two gamma matrices -- `CORRECTED`

For the audit-only normalized product

$$
\Gamma^{\mu\nu}:=\frac12[\gamma^\mu,\gamma^\nu],
$$

the Clifford relation gives

$$
\begin{aligned}
\gamma^\mu\gamma^\nu
&=\frac12\{\gamma^\mu,\gamma^\nu\}
+\frac12[\gamma^\mu,\gamma^\nu]\\
&=\kappa\eta^{\mu\nu}+\Gamma^{\mu\nu}.
\end{aligned}
$$

Book Clifford sources: Weinberg `W54:46-55`; Srednicki `S47:13-18`.  In Weinberg's own bracket convention, the antisymmetric term is

$$
\frac12\gamma_W^{[\mu}\gamma_W^{\nu]},
$$

because his bracket lacks $1/2$ (`W54:156-180`).  Project: `PROJECT_UNFIXED`.

### 21. Three gamma matrices -- `CORRECTED`

With normalized $\Gamma^{\mu\nu\rho}$,

$$
\gamma^\mu\gamma^\nu\gamma^\rho
=\Gamma^{\mu\nu\rho}
+\kappa\left(
\eta^{\mu\nu}\gamma^\rho
-\eta^{\mu\rho}\gamma^\nu
+\eta^{\nu\rho}\gamma^\mu
\right).
$$

Equivalently,

$$
\gamma^\mu\Gamma^{\nu\rho}
=\Gamma^{\mu\nu\rho}
+\kappa\eta^{\mu\nu}\gamma^\rho
-\kappa\eta^{\mu\rho}\gamma^\nu.
$$

The identities follow by expanding all six permutations and using the book Clifford relations at Weinberg `W54:46-55` and Srednicki `S47:13-18`.  Weinberg's own three-index bracket equals $3!\Gamma_W^{\mu\nu\rho}$ by `W54:156-180`; the draft must not insert his raw bracket into the normalized formula.  Project: `PROJECT_UNFIXED`.

### 22. Contracted identities -- `VERIFIED`

From $\{\gamma^\mu,\gamma^\nu\}=2\kappa\eta^{\mu\nu}$,

$$
\gamma^\mu\gamma_\mu
=\frac12\{\gamma^\mu,\gamma_\mu\}
=d\kappa,
$$

$$
\begin{aligned}
\gamma^\mu\gamma^\nu\gamma_\mu
&=\gamma^\mu(-\gamma_\mu\gamma^\nu+2\kappa\delta_\mu{}^\nu)\\
&=-d\kappa\gamma^\nu+2\kappa\gamma^\nu\\
&=(2-d)\kappa\gamma^\nu,
\end{aligned}
$$

$$
\begin{aligned}
\gamma^\mu\gamma^\nu\gamma^\rho\gamma_\mu
&=-\gamma^\mu\gamma^\nu\gamma_\mu\gamma^\rho
+2\kappa\gamma^\rho\gamma^\nu\\
&=-(2-d)\kappa\gamma^\nu\gamma^\rho
+2\kappa(-\gamma^\nu\gamma^\rho+2\kappa\eta^{\nu\rho})\\
&=(d-4)\kappa\gamma^\nu\gamma^\rho+4\eta^{\nu\rho}.
\end{aligned}
$$

Srednicki independently gives the $\kappa=-1$ cases at `S47:165-185`.  Weinberg's Clifford input is `W54:46-55`.  Project: `PROJECT_UNFIXED`.

### 23. Trace identities -- `VERIFIED`

Srednicki gives

$$
\operatorname{tr}1=4,
\qquad
\operatorname{tr}(\text{odd number of }\gamma)=0,
$$

$$
\operatorname{tr}(\gamma_S^\mu\gamma_S^\nu)=-4\eta^{\mu\nu},
$$

$$
\operatorname{tr}(\gamma_S^\mu\gamma_S^\nu\gamma_S^\rho\gamma_S^\sigma)
=4(\eta^{\mu\nu}\eta^{\rho\sigma}
-\eta^{\mu\rho}\eta^{\nu\sigma}
+\eta^{\mu\sigma}\eta^{\nu\rho}),
$$

$$
\operatorname{tr}(\gamma_{5S}\gamma_S^\mu\gamma_S^\nu\gamma_S^\rho\gamma_S^\sigma)
=-4i\epsilon^{\mu\nu\rho\sigma}.
$$

Source: `S47:13-55`, `S47:90-116`, `S47:126-164`.

Under $\gamma_W=-i\gamma_S$ and $\gamma_{5W}=-\gamma_{5S}$,

$$
\operatorname{tr}(\gamma_W^\mu\gamma_W^\nu)
=(-i)^2(-4\eta^{\mu\nu})
=4\eta^{\mu\nu},
$$

$$
\operatorname{tr}(\gamma_{5W}\gamma_W^\mu\gamma_W^\nu\gamma_W^\rho\gamma_W^\sigma)
=(-1)(-i)^4(-4i\epsilon^{\mu\nu\rho\sigma})
=4i\epsilon^{\mu\nu\rho\sigma}.
$$

Thus the unified form is

$$
\operatorname{tr}(\gamma_{5\bullet}\gamma_\bullet^\mu\gamma_\bullet^\nu
\gamma_\bullet^\rho\gamma_\bullet^\sigma)
=4i\kappa_\bullet\epsilon^{\mu\nu\rho\sigma}.
$$

Project: `PROJECT_UNFIXED`.

### 24. Duality identities -- `CORRECTED`

Use normalized $\Gamma^{\mu_1\cdots\mu_r}$.  With

$$
\gamma_5=-i\kappa\gamma^0\gamma^1\gamma^2\gamma^3,
$$

the exact identities are

$$
\Gamma^{\mu\nu\rho}
=i\epsilon^{\mu\nu\rho\sigma}\gamma_5\gamma_\sigma,
$$

$$
\Gamma^{\mu\nu\rho\sigma}
=i\kappa\epsilon^{\mu\nu\rho\sigma}\gamma_5,
$$

$$
\gamma_5\Gamma^{\mu\nu}
=-\frac{i\kappa}{2}\epsilon^{\mu\nu\rho\sigma}\Gamma_{\rho\sigma}.
$$

For example,

$$
i\epsilon^{0123}\gamma_5\gamma_3
=i(-i\kappa)\gamma^0\gamma^1\gamma^2(\gamma^3)^2
=i(-i\kappa)(\kappa)\gamma^0\gamma^1\gamma^2
=\Gamma^{012}.
$$

Weinberg explicitly gives the unnormalized identities

$$
\gamma_W^{[\rho}\gamma_W^\sigma\gamma_W^{\tau]}
=3!i\epsilon^{\rho\sigma\tau\eta}\gamma_{5W}\gamma_{W\eta},
$$

$$
\gamma_W^{[\rho}\gamma_W^\sigma\gamma_W^\tau\gamma_W^{\eta]}
=4!i\epsilon^{\rho\sigma\tau\eta}\gamma_{5W}.
$$

Source: `W54:292-320`.  Srednicki fixes $\gamma_{5S}=i\gamma_S^0\gamma_S^1\gamma_S^2\gamma_S^3$ at `S47:126-130`.  The draft's phrase “if Weinberg uses unnormalized antisymmetrization” is false: Weinberg explicitly does so at `W54:156-180`.  Project: `PROJECT_UNFIXED`.

### 25. Majorana Fierz identity -- `CORRECTED`

Weinberg gives

$$
\begin{aligned}
s_\alpha s_\beta={}&
+\frac14(\epsilon\gamma_{5W})_{\alpha\beta}(\bar s s)
+\frac14(\gamma_{W\mu}\epsilon)_{\alpha\beta}
(\bar s\gamma_{5W}\gamma_W^\mu s)\\
&+\frac14\epsilon_{\alpha\beta}(\bar s\gamma_{5W}s).
\end{aligned}
$$

Source: `W26A:93-131`.

Because

$$
\mathcal C=-\epsilon\gamma_{5W},
\qquad
\epsilon\gamma_{5W}=-\mathcal C,
\qquad
\epsilon=-\gamma_{5W}\mathcal C,
\qquad
\gamma_{W\mu}\epsilon=\gamma_{5W}\gamma_{W\mu}\mathcal C,
$$

the Weinberg form is exactly

$$
\boxed{
\begin{aligned}
(s_W)_\alpha(s_W)_\beta={}&
-\frac14\mathcal C_{\alpha\beta}(\bar s_Ws_W)
-\frac14(\gamma_{5W}\mathcal C)_{\alpha\beta}
(\bar s_W\gamma_{5W}s_W)\\
&+\frac14(\gamma_{5W}\gamma_{W\mu}\mathcal C)_{\alpha\beta}
(\bar s_W\gamma_{5W}\gamma_W^\mu s_W).
\end{aligned}}
$$

This verifies the draft formula only as a **Weinberg-convention** identity.

Translate with $s_W=is_S$, $\bar s_W=-i\bar s_S$, $\gamma_W=-i\gamma_S$, $\gamma_{5W}=-\gamma_{5S}$.  The left side is

$$
(s_W)_\alpha(s_W)_\beta=- (s_S)_\alpha(s_S)_\beta.
$$

The three Weinberg right-side channels become respectively

$$
-\frac14\mathcal C_{\alpha\beta}(\bar s_Ss_S),
$$

$$
-\frac14(\gamma_{5S}\mathcal C)_{\alpha\beta}
(\bar s_S\gamma_{5S}s_S),
$$

$$
-\frac14(\gamma_{5S}\gamma_{S\mu}\mathcal C)_{\alpha\beta}
(\bar s_S\gamma_{5S}\gamma_S^\mu s_S).
$$

Multiplying the full equality by $-1$ gives the Srednicki-convention identity

$$
\boxed{
\begin{aligned}
(s_S)_\alpha(s_S)_\beta={}&
+\frac14\mathcal C_{\alpha\beta}(\bar s_Ss_S)
+\frac14(\gamma_{5S}\mathcal C)_{\alpha\beta}
(\bar s_S\gamma_{5S}s_S)\\
&+\frac14(\gamma_{5S}\gamma_{S\mu}\mathcal C)_{\alpha\beta}
(\bar s_S\gamma_{5S}\gamma_S^\mu s_S).
\end{aligned}}
$$

Srednicki source inputs for the Majorana convention and matrix basis: `S36:358-422`, `S47:213-214`; his Majorana bilinear normalization $\bar\Psi=\Psi^T\mathcal C$ is restated at `S49:13-18`.  The registered Srednicki pages do not print this exact component Fierz formula; its Srednicki form above is an explicit translation from the source-fixed Weinberg identity.

Project: `PROJECT_UNFIXED`.

## P0 findings

1. **P0 -- antisymmetrization:** the draft imposes normalized brackets globally, while Weinberg's brackets are explicitly unnormalized.  Uncorrected use changes ranks two, three, four by factors $2$, $6$, $24$.  Resolution: retain Weinberg raw brackets and use the separate normalized symbol $\Gamma^{\mu_1\cdots\mu_r}$.
2. **P0 -- Majorana Fierz:** the draft presents the Weinberg-sign Fierz formula as convention-free.  Under the required Majorana phase, all three Srednicki channel signs are positive.  Resolution: label and retain both boxed formulas in section 25.

## P1 findings

1. **P1 -- beta:** $\beta_S$ and $\gamma_S^0$ are numerically equal but have different spinor-index structures.  Resolution: never identify them as indexed tensors.
2. **P1 -- charge conjugation:** Srednicki's $C$ is a unitary operator; $\mathcal C$ is the numerical matrix.  Resolution: use $\mathcal C$ throughout the dictionary.
3. **P1 -- Majorana phase:** the book-to-book reality map fixes $e^{i\phi}=\pm i$, not a unique $+i$.  Resolution: declare $+i$ as the dictionary branch and record the residual common sign.
4. **P1 -- project column:** the canonical project has not fixed any four-component spinor system.  Resolution: all such entries remain `PROJECT_UNFIXED`; no Srednicki-style completion is silently promoted to canonical status.
5. **P1 -- Weinberg Dirac attribution:** the registered Weinberg pages fix the Majorana kinetic convention, not the general Dirac Lagrangian quoted in draft section 15.  Resolution: retain the algebraic conversion but mark exact attribution `SOURCE_INSUFFICIENT`.
