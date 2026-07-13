# Step 5 one-loop covariant completion — Pro review round 4

Role: external gap reviewer only.  Do not supply or import an anomaly
coefficient.  Audit the following Project-side exact statements and identify
the smallest remaining proof obligation or an explicit counterexample.

## Fixed object

$$
\mathscr I^{AB}
=\nabla_-\!\left[
(\nabla_+W_+)^A(\nabla_+W_+)^B
\right],
\qquad
\mathscr I^{AB}=\mathscr I^{BA}.
$$

The physical local source lies in
\(\operatorname{Sym}^2(\operatorname{Adj})\).  The complete reflection replay
gives

$$
s_{\rm ext}=-1,\qquad
s_{\rm quantum}=-1,\qquad
s_{\rm reflected}=+1.
$$

Hence the type-compatible word is

$$
\mathscr O_+^{AB}
=c_{ACD}c_{BCE}\left[
\widetilde W_{\dot a}^{D}\mathcal D_+{}^{\dot a}X^E
+(\mathcal D_+{}^{\dot a}X^D)\widetilde W_{\dot a}^{E}
\right],
\qquad
X^E=(\nabla_+W_+)^E.
$$

## Exact one-loop rooted functional

In the fixed Step-5A vector frame and reference-flat measure,

$$
\Gamma_{\mathscr I}^{(1)}[\mathcal B]
=\frac12\operatorname{STr}_{\rm DRED}
\left(G_{\mathcal B}I_{\mathcal B}\right).
$$

With

$$
H_{\mathcal B}=H_0+\sum_{r\ge1}H_r,\qquad
I_{\mathcal B}=\sum_{s\ge0}I_s,
$$

the exact background-order-\(n\) family is

$$
\Gamma_{\mathscr I,n}^{(1)}
=\frac12
\sum_{\substack{k\ge0,\ s\ge0,\ r_j\ge1\\
s+r_1+\cdots+r_k=n}}
(-1)^k
\operatorname{STr}_{\rm DRED}
\left[I_sG_0H_{r_1}G_0\cdots H_{r_k}G_0\right]
+\mathrm{CT}_n.
$$

The exact counts are

$$
N_{\rm family}(n)=2^n,
$$

$$
N_{\rm pol}(n)
=\sum_{s=0}^n\binom ns
\sum_{k=0}^{n-s}k!\,S(n-s,k),
$$

$$
(N_{\rm pol}(2),N_{\rm pol}(3),N_{\rm pol}(4))
=(6,26,150).
$$

The complete quadratic seed is

$$
\begin{aligned}
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}\Big[&
+I_0G_0H_1[1]G_0H_1[2]G_0
+I_0G_0H_1[2]G_0H_1[1]G_0\\
&-I_0G_0H_2[1,2]G_0
-I_1[1]G_0H_1[2]G_0\\
&-I_1[2]G_0H_1[1]G_0
+I_2[1,2]G_0
\Big]+\mathrm{CT}_2.
\end{aligned}
$$

Thus the theorem datum is not the isolated triangle.

## Functional Ward certificate

The Project derives

$$
H'=RHR^{-1},\qquad
G'=RGR^{-1},\qquad
I'=RIR^{-1},
$$

$$
\operatorname{Tr}_{\rm Adj}(\operatorname{ad}_\eta)=0,
\qquad
\operatorname{STr}_{\rm DRED}[R,\mathcal M]=0.
$$

The second identity retains the DRED loop translation and vanishing boundary
term.  Therefore the rooted functional is background covariant.  A
vertex-by-vertex GraphIR Ward replay remains open.

## Fixed-quadratic-jet matrix

The pure-gauge target is

$$
[\mathscr O]=\frac92,\qquad
(j_L,j_R)=\left(\frac32,0\right),\qquad
|\mathscr O|=1,\qquad
r_{\rm f}(\mathscr O)=-1.
$$

The Project census has

$$
\#\mathcal S_N=(5,7,5,1),\qquad N=0,1,2,3.
$$

Exact local blocks already computed:

$$
M_{N0}\in\mathbb Q^{40\times40},
\qquad
\operatorname{rank}M_{N0}=40,
$$

$$
M_{N0,J}\in\mathbb Q^{320\times320},
\qquad
\operatorname{rank}M_{N0,J}=320,
$$

$$
M_{N1}\in\mathbb Q^{40\times40},
\qquad
\operatorname{rank}M_{N1}=40,
$$

$$
M_{WW\nabla^3}\in\mathbb Q^{64\times64},
\qquad
\operatorname{rank}M_{WW\nabla^3}=64.
$$

For all indexed \(N\!-\!D\) and \(B\!-\!D\) curvature children:

$$
N_{\rm source\ words}=1626,\qquad
N_{\rm events}=21600,\qquad
N_{\rm branches}=53412,
$$

$$
M_{\rm hw}\in\mathbb Q^{126\times4864},
\qquad
\operatorname{rank}M_{\rm hw}=126,
$$

$$
M_{\rm Spin(4)}\in\mathbb Q^{504\times19456},
\qquad
\operatorname{rank}M_{\rm Spin(4)}=504.
$$

All 330 component intertwiners pass epsilon invariance, and every full
Spin(4) rank equals four times its highest-weight rank.

The complete tensor-valued quadratic jet of the surviving
\(W\widetilde W\nabla\mathcal D\) carrier is

$$
\ell_2[\mathscr C_K]
=\begin{pmatrix}1\\-1\end{pmatrix}
\otimes K^{AB}{}_{CD},
\qquad
\operatorname{rank}\ell_2=1,
\qquad
\dim\ker\ell_2=0
$$

over the free symbolic source-color tensor module.  No scalar color rank-one
claim is made.

Still absent:

$$
M_{D-D\ {\rm pairing}},\qquad
M_{\rm source\text{-}BRST},\qquad
M_{\rm color\text{-}Sym^2Adj},\qquad
M_{\rm DRED\text{-}evanescent}.
$$

Therefore the Project still reports

$$
\ker\bar\ell_2=0
\quad\text{not certified}.
$$

## Chiral/vector frame boundary

Project Step 3C gives exact covariant-operator similarities through
\(\mathcal B,\widetilde{\mathcal B}\).  The old arbitrary \(2\times2\)
GL matrix is rejected as a Project frame certificate.  The current repair
separates:

$$
\text{covariant-operator similarity},
\qquad
\text{linearized quantum tangent map},
\qquad
\text{nonlinear background-split field redefinition},
\qquad
\text{its measure/Jacobian}.
$$

No cross-frame functional equality is claimed yet.  The fixed vector-frame
Step-5A theorem does not use that equality.

## Questions

1. Is the conditional implication

$$
\ker\bar\ell_2=0,\qquad
\ell_2[\mathcal A_{\rm loc}^{(1)}]
=C_2\ell_2[\mathscr O_\star]
\quad\Longrightarrow\quad
\mathcal A_{\rm loc}^{(1)}=C_2\mathscr O_\star
$$

sufficient to prove that every box/pentagon/higher-background sum is the
Taylor dressing of the complete quadratic seed?

2. Give an explicit indexed pure-gauge local counterexample, if one exists,
with the fixed dimension, spin, parity, formal grading, and symmetric source
channel, whose complete quadratic jet vanishes.  Check all Bianchi, EOM, IBP,
color, and source-jet relations.  If no counterexample is supplied, do not
claim injectivity.

3. Does injectivity over the free symbolic source-color tensor module remove
the need for a separate scalar color-rank computation?  State exactly which
color quotient is still required by the physical
\(\operatorname{Sym}^2(\operatorname{Adj})\) source.

4. In Project DRED, every routed external momentum lies in the
\(\widehat\delta\) subspace, while spinor algebra uses
\(\delta_{(4)}=\widehat\delta+\widetilde\delta\).  Classify all independent
evanescent local jet directions in this fixed target sector.  Do not replace
this by the scalar trace \(2\epsilon\) unless the index reduction proves that
no free evanescent tensor survives.

5. Derive the actual chiral/vector quantum tangent intertwiner from
\(\nabla^{\mathsf C}=\mathcal B^{-1}\nabla^{\mathsf V}\mathcal B\).  Separate
the exact endomorphism similarity from the nonlinear background-split
Jacobian.  State whether the latter blocks the fixed-vector-frame theorem or
only cross-frame equality.

6. Audit the statement

$$
C_2=C_\triangle
$$

as a separate quadratic contact-cancellation problem.  Covariance alone must
not be used to prove it.

Return a fail-closed answer.  Do not infer a numerical anomaly coefficient.
