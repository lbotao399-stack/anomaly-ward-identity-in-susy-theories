# Weinberg--Srednicki dictionary audit: §§40--54

## 0. Symbols and evidence keys

Dictionary-only symbols:

$$
\begin{array}{c|c}
\text{symbol}&\text{meaning}\\ \hline
(V_c,\lambda_c,D_c,f_c)&\text{Weinberg canonically normalized gauge multiplet}\\
(\widehat V,\widehat\lambda,\widehat D,\widehat f)&\text{Weinberg rescaled gauge multiplet}\\
(V_S,\lambda_S,D_S,F_S)&\text{Srednicki canonically normalized gauge multiplet}\\
t_A&\text{Weinberg canonical-basis Hermitian generator}\\
T_A&\text{coupling-independent representation generator}\\
\epsilon_W&\text{Weinberg's four-component antisymmetric matrix}\\
\mathcal C_W&\text{Weinberg's charge-conjugation matrix}\\
\Xi&\text{Srednicki chiral supergauge parameter}\\
\Omega_c,\widehat\Omega&\text{Weinberg canonical/rescaled chiral parameters}
\end{array}
$$

`PROJECT_UNFIXED` means that Steps 1, 2A, and 2B do not define the object.  Step 2A only reserves $\nabla$ for a future gauge-covariant superspace derivative [P2A:403].

Every book citation below has the form `[key:first-last]`.  The key supplies the exact vendored page, Notion page id, and Notion URL; `first-last` supplies the local line anchor.

| key | vendored page | Notion page id | exact Notion URL |
|---|---|---|---|
| `S95` | `references/vendor/notion/srednicki/95-supersymmetry-0151805c7e85457a9928fcfd0e83da2a.md` | `0151805c-7e85-457a-9928-fcfd0e83da2a` | `https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a` |
| `W26.2` | `references/vendor/notion/weinberg/26-02-general-superfields-34cee2b74b3f8182a538e629f277c1e7.md` | `34cee2b7-4b3f-8182-a538-e629f277c1e7` | `https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7` |
| `W26A` | `references/vendor/notion/weinberg/26-appendix-majorana-spinors-34cee2b74b3f81349f82dd4d257ba62c.md` | `34cee2b7-4b3f-8134-9f82-dd4d257ba62c` | `https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c` |
| `W27.1` | `references/vendor/notion/weinberg/27-01-gauge-invariant-chiral-action-34cee2b74b3f81b6b72bd47d34df4d88.md` | `34cee2b7-4b3f-81b6-b72b-d47d34df4d88` | `https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88` |
| `W27.2` | `references/vendor/notion/weinberg/27-02-abelian-gauge-superfield-action-34cee2b74b3f8131b10edd7a1dad0172.md` | `34cee2b7-4b3f-8131-b10e-dd7a1dad0172` | `https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172` |
| `W27.3` | `references/vendor/notion/weinberg/27-03-general-gauge-superfield-action-34cee2b74b3f812f97c2d0aa902aba5d.md` | `34cee2b7-4b3f-812f-97c2-d0aa902aba5d` | `https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d` |
| `W27.4` | `references/vendor/notion/weinberg/27-04-renormalizable-gauge-theory-34cee2b74b3f81949500f3f35884f580.md` | `34cee2b7-4b3f-8194-9500-f3f35884f580` | `https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580` |

Project anchor:

| key | path |
|---|---|
| `P2A` | `contracts/foundations/step-02a-flat-superspace.md` |

The sentence at `W27.3:28` is editorial notation commentary and is not used as Weinberg evidence.

## 1. Independent source ledgers

### 1.1 Srednicki

$$
\begin{aligned}
V_S^{\rm WZ}
&=(\theta\sigma^\mu\theta^*)v_\mu
+\theta^2\theta^*\lambda^\dagger
+\theta^{*2}\theta\lambda
+\frac12\theta^2\theta^{*2}D,
\\
V_S&\longmapsto V_S+i(\Xi^\dagger-\Xi),
\\
\Phi&\longmapsto e^{-2ig\Xi}\Phi,
\\
\Phi^\dagger&\longmapsto\Phi^\dagger e^{2ig\Xi^\dagger},
\\
\mathcal L_{\rm matter}
&=\left.\Phi^\dagger e^{-2gV_S}\Phi\right|_D.
\end{aligned}
$$

[S95:363-445]

$$
W_{a,S}=\frac14\mathcal D^*_{\dot a}\mathcal D^{*\dot a}\mathcal D_aV_S,
$$

$$
W_{a,S}
=\lambda_a+\theta_aD
-(S_L^{\mu\nu})_a{}^b\theta_bF_{\mu\nu}
+i\theta^2\sigma^\mu_{a\dot a}\partial_\mu\lambda^{\dagger\dot a}.
$$

[S95:512-518] [S95:583-618]

$$
\left.\frac14W^aW_a\right|_F+\mathrm{h.c.}
=i\lambda^\dagger\bar\sigma^\mu\partial_\mu\lambda
-\frac14F^{\mu\nu}F_{\mu\nu}
+\frac12D^2.
$$

[S95:620-644]

For the nonabelian theory,

$$
\begin{aligned}
E_S&:=e^{-2gV_S},\\
E_S&\longmapsto e^{-2ig\Xi^\dagger}E_Se^{2ig\Xi},\\
W_{a,S}&=-\frac1{8g}\mathcal D^{*2}
\left(E_S^{-1}\mathcal D_aE_S\right),\\
W_{a,S}&\longmapsto e^{-2ig\Xi}W_{a,S}e^{2ig\Xi}.
\end{aligned}
$$

[S95:645-686]

### 1.2 Weinberg: canonical basis

Weinberg first uses

$$
\Gamma_c=e^{-2t_AV_c^A},
\qquad
\Phi\longmapsto e^{it_A\Omega_c^A}\Phi,
$$

$$
\Gamma_c\longmapsto
e^{-it_A\Omega_c^A}\Gamma_c e^{it_A\Omega_c^{A*}}.
$$

[W27.1:141-165]

The Wess--Zumino representative reconstructed from the general real superfield is

$$
V_c^{A,\rm WZ}
=\frac i2(\bar\Theta\gamma_5\gamma^\mu\Theta)V_{c,\mu}^A
-i(\bar\Theta\gamma_5\Theta)(\bar\Theta\lambda_c^A)
-\frac14(\bar\Theta\gamma_5\Theta)^2D_c^A.
$$

[W26.2:135-142] [W27.1:208-218] [W27.1:419-421]

The component normalization is canonical:

$$
\mathcal L_{c,\rm gauge}
=-\frac14f_{c,\mu\nu}^Af_c^{A\mu\nu}
-\frac12\bar\lambda_c^A\not{\mathcal D}\lambda_c^A
+\frac12D_c^AD_c^A.
$$

[W27.2:41-92] [W27.3:20-40]

### 1.3 Weinberg: rescaled basis

Weinberg later absorbs one factor of $g$ into the gauge field so that the structure constants no longer contain $g$ and the gauge kinetic action acquires $1/g^2$ [W27.3:287-320].  Define the entire rescaled real superfield by

$$
\widehat V:=gV_c.
$$

The Wess--Zumino expansion then fixes every component scaling:

$$
\widehat V_\mu=gV_{c,\mu},
\qquad
\widehat\lambda=g\lambda_c,
\qquad
\widehat D=gD_c,
\qquad
\widehat f_{\mu\nu}=gf_{c,\mu\nu}.
$$

Hence

$$
\mathcal L_{\widehat V,\rm gauge}
=-\frac1{4g^2}\widehat f^2
-\frac1{2g^2}\bar{\widehat\lambda}\not{\mathcal D}\widehat\lambda
+\frac1{2g^2}\widehat D^2.
$$

This rescaling is not the convention used in Weinberg's preceding equations (27.1.10)--(27.4.7).

### 1.4 Project

The canonical project fixes flat and superconformal superspace only.  It defines neither a vector superfield nor $W_a$, $g$, $T_A$, $D^A$, an $F$-projection, a $D$-projection, nor a gauge action.  Therefore every project entry in §§40--54 is `PROJECT_UNFIXED`. [P2A:403]

## 2. Audit of §§40--54

### §40. Srednicki Wess--Zumino gauge — VERIFIED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:2659-2681`.

The unconstrained vector superfield contains $C,\chi,M,v_\mu,\lambda,D$ [S95:253-265].  With

$$
a=-C,
\qquad
\xi=-i\chi,
\qquad
\mathcal G=-iM,
$$

the transformations in (95.54) give

$$
C'=0,
\qquad
\chi'=0,
\qquad
M'=0.
$$

The surviving terms are exactly

$$
V_S^{\rm WZ}
=(\theta\sigma^\mu\theta^*)v_\mu
+\theta^2\theta^*\lambda^\dagger
+\theta^{*2}\theta\lambda
+\frac12\theta^2\theta^{*2}D.
$$

[S95:388-423]

Project: `PROJECT_UNFIXED`.

### §41. Weinberg Wess--Zumino gauge — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:2682-2750`.

Set $C=\omega=M=N=0$ in Weinberg's general real superfield:

$$
\begin{aligned}
V_c^{\rm WZ}
&=\frac i2(\bar\Theta\gamma_5\gamma^\mu\Theta)V_{c,\mu}
-i(\bar\Theta\gamma_5\Theta)(\bar\Theta\lambda_c)
-\frac14(\bar\Theta\gamma_5\Theta)^2D_c.
\end{aligned}
$$

[W26.2:135-142]

The vendored rendering of (27.1.19) contains $+(\bar\Theta\gamma_5\Theta)^2D$ [W27.1:266-277].  That coefficient is inconsistent with both the defining general superfield [W27.1:208-218] and Weinberg's subsequent exponential:

$$
-2t_AV_c^A
\supset
-2t_A\left[-\frac14(\bar\Theta\gamma_5\Theta)^2D_c^A\right]
=+\frac12(\bar\Theta\gamma_5\Theta)^2t_AD_c^A,
$$

which is the coefficient displayed in $\Gamma_c$ [W27.1:419-421].  Thus the draft's $-1/4$ coefficient is correct; the isolated rendered (27.1.19) block is not used.

The proposed four-component gaugino rephasing in the draft is not fixed by §§26.2, 27.1, or Srednicki §95.  The gauge-source-closed statement is only

$$
\lambda_c\text{ is the Majorana component of }V_c,
\qquad
\lambda_S\text{ is the undotted Weyl component of }V_S.
$$

[W27.1:208-218] [S95:259-265]

No phase map is asserted here.  In particular, a gaugino rephasing cannot be declared action-invisible before the matter Yukawa terms are transformed.

Project: `PROJECT_UNFIXED`.

### §42. Srednicki Abelian transformations — VERIFIED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:2752-2803`.

For charge $q$, replace $g$ by $gq$ in the charge-one formulas [S95:436-447]:

$$
\Phi'=e^{-2igq\Xi}\Phi,
\qquad
\Phi^{\dagger\prime}=\Phi^\dagger e^{2igq\Xi^\dagger},
\qquad
V_S'=V_S+i(\Xi^\dagger-\Xi).
$$

Since the Abelian exponents commute,

$$
\begin{aligned}
\Phi^{\dagger\prime}e^{-2gqV_S'}\Phi'
&=\Phi^\dagger
e^{2igq\Xi^\dagger}
e^{-2gqV_S-2igq(\Xi^\dagger-\Xi)}
e^{-2igq\Xi}\Phi\\
&=\Phi^\dagger e^{-2gqV_S}\Phi.
\end{aligned}
$$

The matrix-valued nonabelian replacement $V_S=V_S^AT_R^A$ is defined in Srednicki's nonabelian paragraph [S95:645-666].

Project: `PROJECT_UNFIXED`.

### §43. Weinberg Abelian transformations — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:2805-2882`.

Weinberg's exact canonical formulas are

$$
V_c' =V_c+\frac i2(\Omega_c-\Omega_c^*),
\qquad
\Phi'=e^{it_A\Omega_c^A}\Phi.
$$

[W27.1:150-165] [W27.2:305-323]

The canonical kinetic terms fix $V_c=v_S$.  Equality of matter covariant derivatives then gives

$$
\partial_\mu-it_AV_{c,\mu}^A
=\partial_\mu-igT_Av_{S,\mu}^A,
$$

and therefore

$$
t_A=gT_A,
\qquad
V_c^A=V_S^A.
$$

[W27.1:483-493] [S95:506-511]

Equality of matter transformations gives

$$
e^{igT_A\Omega_c^A}=e^{-2igT_A\Xi^A},
\qquad
\boxed{\Omega_c^A=-2\Xi^A}.
$$

The vector transformation checks the same result:

$$
\frac i2(-2\Xi+2\Xi^\dagger)
=i(\Xi^\dagger-\Xi).
$$

Only after defining

$$
\widehat V=gV_c,
\qquad
T_A=\frac{t_A}{g},
\qquad
\widehat\Omega=g\Omega_c,
$$

does one obtain

$$
\boxed{\widehat V=gV_S},
\qquad
\boxed{\widehat\Omega=-2g\Xi}.
$$

Thus the draft's parameter dictionary is valid only in the hatted, rescaled basis; it is false for Weinberg's canonical equations (27.1.10)--(27.2.18).

Project: `PROJECT_UNFIXED`.

### §44. Gauge-coupling normalization — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:2884-3004`.

Both authors first display canonical gauge kinetic terms:

$$
\mathcal L_{W,c}=-\frac14f_c^2-\frac12\bar\lambda_c\not{\mathcal D}\lambda_c+\frac12D_c^2,
$$

$$
\mathcal L_S=-\frac14F_S^2+i\lambda_S^\dagger\bar\sigma^\mu\mathcal D_\mu\lambda_S+\frac12D_S^2.
$$

[W27.2:41-92] [S95:638-644]

Matching the matter exponential and covariant derivative gives the canonical map

$$
t_A=gT_A,
\qquad
V_c^A=V_S^A,
\qquad
f_c^A=F_S^A,
\qquad
D_c^A=D_S^A.
$$

The last equality follows from

$$
-D_c^A\phi^\dagger t_A\phi
=-gD_c^A\phi^\dagger T_A\phi
=-gD_S^A A^\dagger T_AA.
$$

[W27.1:483-493] [S95:506-511]

Weinberg's later rescaling [W27.3:287-320] yields

$$
\boxed{
\widehat V^A=gV_S^A,
\quad
\widehat f^A=gF_S^A,
\quad
\widehat D^A=gD_S^A,
\quad
\widehat\lambda^A=g\lambda_c^A.}
$$

Then

$$
-\frac1{4g^2}\widehat f^2
=-\frac1{4g^2}(gF_S)(gF_S)
=-\frac14F_S^2.
$$

The factor $g$ does not determine the four-component/two-component gaugino phase.  That phase is a separate spinor-dictionary datum.

Project: `PROJECT_UNFIXED`.

### §45. Srednicki Abelian field strength — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3006-3077`.

The Abelian definitions and expansion are correct:

$$
W_{a,S}=\frac14\mathcal D^{*2}\mathcal D_aV_S,
\qquad
\mathcal D^*_{\dot a}W_{b,S}=0,
$$

$$
W_{a,S}=\lambda_a+\theta_aD
-(S_L^{\mu\nu})_a{}^b\theta_bF_{\mu\nu}
+i\theta^2\sigma^\mu_{a\dot a}\partial_\mu\lambda^{\dagger\dot a}.
$$

[S95:512-518] [S95:583-618]

From

$$
\left.W^aW_a\right|_F
=2i\lambda^a\sigma^\mu_{a\dot a}\partial_\mu\lambda^{\dagger\dot a}
-\frac12F^2
-\frac i2\widetilde F^{\mu\nu}F_{\mu\nu}
+D^2,
$$

[S95:620-637]

one gets

$$
\begin{aligned}
\frac14\left(\left.W^aW_a\right|_F+\mathrm{h.c.}\right)
&=i\lambda^\dagger\bar\sigma^\mu\partial_\mu\lambda
-\frac14F^2
+\frac12D^2,
\end{aligned}
$$

because the topological term changes sign under Hermitian conjugation [S95:638-644].

The correction is scope: the Abelian coefficient is $1/4$.  The traced expression

$$
\frac1{4T(R)}\left.\operatorname{Tr}_R(W^aW_a)\right|_F+\mathrm{h.c.}
$$

is the nonabelian extension stated later [S95:674-686], not part of the Abelian definition.

Project: `PROJECT_UNFIXED`.

### §46. Weinberg Abelian field strength — VERIFIED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3079-3121`.

Weinberg defines

$$
W_{L\alpha}
=\frac i4(\mathcal D_R^{\mathrm T}\epsilon_W\mathcal D_R)
\mathcal D_{L\alpha}V_c.
$$

[W27.2:260-304]

His matrices satisfy

$$
\mathcal C_W=-\epsilon_W\gamma_5.
$$

[W26A:29-40] [W26A:74-78]

Therefore

$$
\gamma_5\mathcal D_R=-\mathcal D_R
\quad\Longrightarrow\quad
\mathcal D_R^{\mathrm T}\mathcal C_W\mathcal D_R
=\mathcal D_R^{\mathrm T}\epsilon_W\mathcal D_R,
$$

while

$$
\gamma_5\Theta_L=+\Theta_L
\quad\Longrightarrow\quad
-\Theta_L^{\mathrm T}\mathcal C_W\Theta_L
=+\Theta_L^{\mathrm T}\epsilon_W\Theta_L.
$$

[W26A:135-140]

Thus the draft's use of $\mathcal C_W$ is exactly equivalent to Weinberg's $\epsilon_W$, and its expansion is

$$
\begin{aligned}
W_L
&=\lambda_L(x_+)
+\frac12\gamma^\mu\gamma^\nu\Theta_L f_{c,\mu\nu}(x_+)
-i\Theta_LD_c(x_+)\\
&\quad
-(\Theta_L^{\mathrm T}\mathcal C_W\Theta_L)
\not\!\partial\lambda_R(x_+).
\end{aligned}
$$

[W27.2:193-199]

Project: `PROJECT_UNFIXED`.

### §47. Srednicki nonabelian field strength — VERIFIED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3123-3167`.

The exact source formulas are [S95:645-685]

$$
E_S=e^{-2gV_S}
\longmapsto
e^{-2ig\Xi^\dagger}E_Se^{2ig\Xi},
$$

$$
W_{a,S}
=-\frac1{8g}\mathcal D^{*2}
\left(e^{2gV_S}\mathcal D_ae^{-2gV_S}\right),
$$

$$
W_{a,S}\longmapsto e^{-2ig\Xi}W_{a,S}e^{2ig\Xi}.
$$

Set

$$
U:=e^{-2ig\Xi},
\qquad
\bar U:=e^{-2ig\Xi^\dagger},
\qquad
E_S':=\bar U E_SU^{-1}.
$$

Since $\mathcal D_a\bar U=0$,

$$
\begin{aligned}
E_S'^{-1}\mathcal D_aE_S'
&=UE_S^{-1}\bar U^{-1}\mathcal D_a(\bar U E_SU^{-1})\\
&=U(E_S^{-1}\mathcal D_aE_S)U^{-1}+U\mathcal D_aU^{-1}.
\end{aligned}
$$

Chirality gives

$$
\mathcal D^{*2}(U\mathcal D_aU^{-1})=0,
\qquad
\mathcal D^{*2}\!\left[U(E_S^{-1}\mathcal D_aE_S)U^{-1}\right]
=U\mathcal D^{*2}(E_S^{-1}\mathcal D_aE_S)U^{-1},
$$

and hence the displayed adjoint transformation follows.

The coefficient and sign follow from the Abelian limit.  Write the exact exponential expansion as

$$
e^{2gV_S}\mathcal D_ae^{-2gV_S}
=-2g\mathcal D_aV_S+R_{2,a},
$$

where every monomial in $R_{2,a}$ contains at least two factors from $V_S,\mathcal D_aV_S$.  Hence at Abelian linear order

$$
-\frac1{8g}\mathcal D^{*2}(-2g\mathcal D_aV_S)
=\frac14\mathcal D^{*2}\mathcal D_aV_S,
$$

which is precisely (95.65) [S95:512-518].

Project: `PROJECT_UNFIXED`.

### §48. Weinberg nonabelian field strength — FALSE

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3169-3240`.

The draft's isolated formula

$$
\frac i4(\mathcal D_R^{\mathrm T}\mathcal C_W\mathcal D_R)
e^{-V}\mathcal D_Le^V
$$

is not Weinberg's nonabelian definition.  Weinberg defines the generator-valued field strength by

$$
\boxed{
2t_AW^A_{L\alpha}
=\epsilon_W^{\beta\gamma}\mathcal D_{R\beta}\mathcal D_{R\gamma}
\left[e^{-2t_BV_c^B}\mathcal D_{L\alpha}e^{2t_CV_c^C}\right].}
$$

[W27.3:183-209]

It transforms as

$$
t_AW_L^A
\longmapsto
e^{-it_B\Omega_c^B}(t_AW_L^A)e^{it_C\Omega_c^C}.
$$

[W27.3:211-224]

The factors $2t_A$ and the exponentials $e^{\mp2t_AV^A}$ are indispensable.  In the Abelian limit,

$$
e^{-2tV_c}\mathcal D_Le^{2tV_c}
=2t\mathcal D_LV_c+R_{2,L},
$$

so both sides contain the same factor $2t$ and reduce to Weinberg's Abelian (27.2.17) [W27.2:299-304].

The covariance statement in the draft is correct; the displayed defining formula is false.

Project: `PROJECT_UNFIXED`.

### §49. Matter coupled to a vector multiplet — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3242-3315`.

Srednicki's charge-one expression is

$$
\left.\Phi^\dagger e^{-2gV_S}\Phi\right|_D.
$$

[S95:436-447]

In Wess--Zumino gauge,

$$
V_S^2=-\frac12\theta^2\theta^{*2}v^\mu v_\mu,
\qquad
V_S^3=0,
$$

and therefore

$$
\begin{aligned}
e^{-2gV_S}
&=1-2gV_S+\frac{(-2gV_S)^2}{2}\\
&=1-2g(\theta\sigma^\mu\theta^*)v_\mu
-2g\theta^2\theta^*\lambda^\dagger
-2g\theta^{*2}\theta\lambda\\
&\quad-\theta^2\theta^{*2}(gD+g^2v^2).
\end{aligned}
$$

[S95:448-473]

Multiplication by $\Phi^\dagger\Phi$ gives

$$
\begin{aligned}
\left.\Phi^\dagger e^{-2gV_S}\Phi\right|_D
&=-(\mathcal D^\mu A)^*\mathcal D_\mu A
+i\psi^\dagger\bar\sigma^\mu\mathcal D_\mu\psi
+F^\dagger F\\
&\quad+\sqrt2g\psi^\dagger\lambda^\dagger A
+\sqrt2gA^\dagger\lambda\psi
-gA^\dagger DA,
\end{aligned}
$$

$$
\mathcal D_\mu=\partial_\mu-igv_\mu.
$$

[S95:474-511]

The representation-valued version follows from $V_S=V_S^AT_R^A$ [S95:645-666].

Weinberg's canonical expression is not obtained by inserting $V_c=gV_S$.  It is

$$
\frac12\left[\Phi^\dagger e^{-2t_AV_c^A}\Phi\right]_D,
$$

with

$$
t_A=gT_A,
\qquad
V_c^A=V_S^A.
$$

[W27.1:141-147] [W27.1:483-493]

Equivalently, in the rescaled basis,

$$
\frac12\left[\Phi^\dagger e^{-2T_A\widehat V^A}\Phi\right]_D,
\qquad
\widehat V^A=gV_S^A.
$$

The draft omitted the simultaneous generator replacement $t_A=gT_A$.

Project: `PROJECT_UNFIXED`.

### §50. Weinberg full gauge action — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3317-3387`.

Weinberg's source-backed general action is

$$
\boxed{
\mathcal L
=\frac12\left[K\!\left(\Phi,\Phi^\dagger e^{-2t_AV_c^A}\right)\right]_D
+2\operatorname{Re}[f(\Phi)]_{\mathcal F}
-\frac12\operatorname{Re}
\left[h_{AB}(\Phi)W_L^{A\mathrm T}\epsilon_WW_L^B\right]_{\mathcal F}.}
$$

[W27.4:627-639]

For one constant gauge coupling,

$$
\mathcal L_{\rm gauge}+\mathcal L_\theta
=-\operatorname{Re}
\left[\frac{\tau}{8\pi i}W_{AL}^{\mathrm T}\epsilon_WW_L^A\right]_{\mathcal F},
\qquad
\tau=\frac{4\pi i}{g^2}+\frac{\theta}{2\pi}.
$$

[W27.3:287-320]

Thus, when written as a chiral term plus its complex conjugate,

$$
-\operatorname{Re}\left[\frac{\tau}{8\pi i}X\right]
=-\frac12\left[
\frac{\tau}{8\pi i}X
+\left(\frac{\tau}{8\pi i}X\right)^*
\right].
$$

The chiral coefficient is $-\tau/(16\pi i)$, not $+\tau/(16\pi i)$ as in the draft.  Equivalently,

$$
h_{AB}=\frac{\tau}{4\pi i}\delta_{AB}
$$

inside Weinberg's $-\frac12\operatorname{Re}[h_{AB}W^AW^B]_{\mathcal F}$ convention.

In the rescaled basis the component gauge terms are

$$
\boxed{
\mathcal L_{\widehat V}
=-\frac1{4g^2}\widehat f_{\mu\nu}^A\widehat f^{A\mu\nu}
-\frac1{2g^2}\bar{\widehat\lambda}^A\not{\mathcal D}\widehat\lambda^A
+\frac1{2g^2}\widehat D^A\widehat D^A
+\frac{\theta}{32\pi^2}\widehat f_{\mu\nu}^A\widetilde{\widehat f}^{A\mu\nu}.}
$$

The $1/g^2$ form must not be combined with the canonical $V_c$ without the hats.

Project: `PROJECT_UNFIXED`.

### §51. Srednicki full action — SOURCE_INSUFFICIENT

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3389-3431`.

The allowed Srednicki page supports the following pieces:

$$
\left.\Phi^\dagger e^{-2gV_S}\Phi\right|_D,
\qquad
\left.W(\Phi)\right|_F+\mathrm{h.c.},
\qquad
\frac1{4T(R)}\left.\operatorname{Tr}_R(W^aW_a)\right|_F+\mathrm{h.c.}
$$

[S95:246-252] [S95:436-447] [S95:638-686]

It does not define, in the allowed source set,

$$
K(\Phi^\dagger e^{-2gV},\Phi),
\qquad
f_{AB}(\Phi)W^{A\alpha}W^B_\alpha.
$$

Therefore the draft's generic Kähler potential and field-dependent gauge kinetic function cannot be attributed to Srednicki §95.  The notation map $f_W(\Phi)=W_S(\Phi)$ is supported only as the names of the two authors' superpotentials [W27.4:34-51] [S95:246-252].

Project: `PROJECT_UNFIXED`.

### §52. Topological term under canonical normalization — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3433-3463`.

Weinberg gives

$$
-\operatorname{Im}[W_{AL}^{\mathrm T}\epsilon_WW_L^A]_{\mathcal F}
=-i\bar\lambda_A\not{\mathcal D}\gamma_5\lambda^A
+\frac14\epsilon_{\mu\nu\rho\sigma}f_c^{A\mu\nu}f_c^{A\rho\sigma},
$$

$$
\mathcal L_\theta
=-\frac{g^2\theta}{16\pi^2}
\operatorname{Im}[W_{AL}^{\mathrm T}\epsilon_WW_L^A]_{\mathcal F}.
$$

[W27.3:261-299]

Since

$$
\widetilde f_c^{\mu\nu}:=\frac12\epsilon^{\mu\nu\rho\sigma}f_{c,\rho\sigma},
\qquad
\epsilon_{\mu\nu\rho\sigma}f_c^{\mu\nu}f_c^{\rho\sigma}
=2f_{c,\mu\nu}\widetilde f_c^{\mu\nu},
$$

the bosonic canonical term is

$$
\mathcal L_{\theta,c}
=\frac{g^2\theta}{32\pi^2}f_{c,\mu\nu}^A\widetilde f_c^{A\mu\nu}.
$$

With $\widehat f=gf_c$,

$$
\frac{\theta}{32\pi^2}\widehat f\widetilde{\widehat f}
=\frac{\theta}{32\pi^2}(gf_c)(g\widetilde f_c)
=\frac{g^2\theta}{32\pi^2}f_c\widetilde f_c.
$$

The draft's algebra is correct only after $f_W$ is identified as the hatted, rescaled field strength.  Srednicki §95 does not state a $\theta$-angle normalization, so no Srednicki author claim is made beyond $f_c=F_S$ from canonical matching.

Project: `PROJECT_UNFIXED`.

### §53. Canonical component action in representations — SOURCE_INSUFFICIENT

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3465-3531`.

Srednicki §95 explicitly supplies the charge-one Abelian matter action [S95:506-511], the Abelian gauge action [S95:638-644], and states that the nonabelian theory uses a matrix vector superfield, an adjoint covariant derivative, a commutator contribution to $F_{\mu\nu}$, a trace, and $1/T(R)$ [S95:645-686].

The page does not state the group-algebra convention needed to decide between the candidate component formulas

$$
(\mathcal D_\mu\lambda)^A
=\partial_\mu\lambda^A+gf^{ABC}v_\mu^B\lambda^C,
$$

$$
F_{\mu\nu}^A
=\partial_\mu v_\nu^A-\partial_\nu v_\mu^A
+gf^{ABC}v_\mu^Bv_\nu^C.
$$

Consequently the complete representation-valued component action in the draft cannot be certified from the allowed Srednicki source.  Weinberg's independently fixed version is (27.4.1)--(27.4.5) [W27.4:34-66], but it uses $t_A,C^A{}_{BC}$ and cannot be attributed to Srednicki.

Project: `PROJECT_UNFIXED`.

### §54. Elimination of auxiliary fields — CORRECTED

Candidate: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3533-3632`.

For complex auxiliary fields,

$$
\mathcal L_F
=F_i^\dagger F_i+W_iF_i+W_i^\dagger F_i^\dagger,
\qquad
W_i:=\frac{\partial W}{\partial A_i}.
$$

Treating $F_i$ and $F_i^\dagger$ as independent variables gives

$$
\frac{\partial\mathcal L_F}{\partial F_i}
=F_i^\dagger+W_i=0,
\qquad
F_i^\dagger=-W_i,
$$

$$
\frac{\partial\mathcal L_F}{\partial F_i^\dagger}
=F_i+W_i^\dagger=0,
\qquad
F_i=-W_i^\dagger.
$$

Hence

$$
\mathcal L_F\big|_{\rm EOM}
=-W_i^\dagger W_i,
\qquad
V_F=W_i^\dagger W_i.
$$

[S95:246-252] [S95:318-335]

For the canonical Srednicki gauge basis with no Fayet--Iliopoulos term,

$$
\mathcal L_D
=\frac12D^AD^A-gJ^AD^A,
\qquad
J^A:=\sum_iA_i^\dagger T^AA_i.
$$

[S95:506-511] [S95:638-686]

Therefore

$$
\frac{\partial\mathcal L_D}{\partial D^A}
=D^A-gJ^A=0,
\qquad
D^A=gJ^A,
$$

and

$$
\begin{aligned}
\mathcal L_D\big|_{\rm EOM}
&=\frac12g^2J^AJ^A-g^2J^AJ^A\\
&=-\frac12g^2J^AJ^A,
\end{aligned}
$$

$$
V_D=\frac12g^2J^AJ^A.
$$

Weinberg includes the possible Abelian Fayet--Iliopoulos constant:

$$
\mathcal L_D
=\frac12D_AD^A-(\xi_A+\phi^\dagger t_A\phi)D^A,
$$

$$
D^A=\xi^A+\phi^\dagger t^A\phi.
$$

[W27.4:34-75]

Thus the draft result is correct only for $\xi^A=0$ and $t_A=gT_A$.  In that scope,

$$
V=W_i^\dagger W_i
+\frac{g^2}{2}
\left(\sum_iA_i^\dagger T^AA_i\right)
\left(\sum_jA_j^\dagger T^AA_j\right).
$$

Project: `PROJECT_UNFIXED`.

## 3. Downstream gauge rows in the compact table and algorithm

Candidate rows: `references/vendor/drafts/weinberg-srednicki-dictionary-draft.txt:3633-3767`.

The source-closed replacement is

$$
\begin{array}{c|c|c}
\text{object}&\text{Weinberg canonical}&\text{Weinberg rescaled}\\ \hline
\text{generator}&t_A=gT_A&T_A\\
\text{prepotential coefficient}&V_c^A=V_S^A&\widehat V^A=gV_S^A\\
\text{gauge boson}&V_{c,\mu}^A=v_{S,\mu}^A&\widehat V_\mu^A=gv_{S,\mu}^A\\
\text{field strength}&f_c^A=F_S^A&\widehat f^A=gF_S^A\\
\text{auxiliary}&D_c^A=D_S^A&\widehat D^A=gD_S^A\\
\text{Abelian parameter}&\Omega_c=-2\Xi&\widehat\Omega=-2g\Xi
\end{array}
$$

[W27.1:141-165] [W27.1:483-493] [W27.3:287-320] [S95:436-447] [S95:638-686]

The row $W_{L,W}\leftrightarrow W_{a,S}$ records representation type only.  Their defining differential expressions are not related by replacing a single symbol: the complete maps of $\mathcal D$, chirality projectors, $\epsilon_W/\mathcal C_W$, exponent orientation, generators, and gauge parameters are required [W27.2:260-304] [W27.3:183-224] [S95:512-518] [S95:645-685].

## 4. P0/P1 findings

| severity | location | finding | resolution |
|---|---|---|---|
| P0 | §§43, 44, 49, 50, 52; compact table | Weinberg canonical and rescaled gauge bases were merged. | Split $(t_A,V_c,\Omega_c)$ from $(T_A,\widehat V,\widehat\Omega)$; derived both maps. |
| P0 | §48 | The proposed Weinberg nonabelian $W_L$ omitted $2t_A$ and used the wrong exponential normalization. | Replaced by exact (27.3.13) and checked its Abelian limit. |
| P0 | §41 / vendored (27.1.19) | The isolated rendered $D$ coefficient conflicts with the defining real superfield and the subsequent exponential. | Fixed $-\frac14(\bar\Theta\gamma_5\Theta)^2D$ from (26.2.10) and the expansion of $\Gamma$. |
| P0 | §§51, 53 | Generic Kähler/gauge-kinetic and complete representation component formulas were attributed to Srednicki without support in allowed §95. | Marked `SOURCE_INSUFFICIENT`; retained only source-backed pieces. |
| P1 | §45 | Abelian and traced nonabelian kinetic normalizations were placed in one formula. | Separated $1/4$ from $1/[4T(R)]$. |
| P1 | §46 | $\epsilon_W$ and $\mathcal C_W$ were used without the chirality-dependent conversion. | Derived $\mathcal C_W=-\epsilon_W\gamma_5$ separately on $R$ derivatives and $L$ coordinates. |
| P1 | §§40--54 | The project column was implicitly treated as if gauge conventions existed. | Marked every entry `PROJECT_UNFIXED`; Step 2A only reserves $\nabla$. |
