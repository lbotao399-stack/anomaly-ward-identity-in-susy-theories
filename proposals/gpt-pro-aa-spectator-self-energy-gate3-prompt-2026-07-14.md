# GPT Pro Gate 3: ordered AA spectator-source triangles and exact DRED cuts

Work in the conditional residual-free canonical Fermi--Feynman coordinate of the GitHub AWI repository.  This is now a standard one-loop supergraph calculation.  Do not reopen the gauge-slice/NK existence question and do not fit a coefficient to the holomorphic twist.

## Regulator and cutting rule

Use

$$
d=4-2\epsilon,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2=-\widetilde\ell^2.
$$

For every occurrence keep its selected inverse-kernel edge $e$ until the end:

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}=0,
$$

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
$$

$$
\int_\ell^{\rm DRED}\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

There is no additional graph-dependent $(4-d)$ factor.  A term is zero in the anomaly sector when its exact rank-two four-dimensional numerator is traceless, or when its full-$d$ parent and Schwinger contact cancel on the same edge.  Do not combine rows carrying different selected edges.

## Canonical rules

Use

$$
V=\sqrt2g\,u,
\qquad
\langle u^A(p,1)u^B(-p,2)\rangle
=-\frac{\hbar\kappa^{AB}}{p_d^2}\delta^4(\theta_1-\theta_2),
$$

$$
\langle\Phi_{c,r}^A(p,1)\widetilde\Phi_{c,s}^B(-p,2)\rangle
=\delta_{rs}\frac{\hbar\kappa^{AB}}{16p_d^2}
\bar D_1^2D_1^2\delta^4(\theta_1-\theta_2),
$$

$$
A_c^{(1)}=-\frac1{4\sqrt2}D_+\bar D^2D_+u,
$$

and the action vertices derived from the repository, in particular

$$
S_{m3}=-\sqrt2g\sum_{r=1}^3\int d^8z\,
\kappa_{AB}\widetilde\Phi_{c,r}^A
u^U(T_U)^B{}_C\Phi_{c,r}^C.
$$

For the gauge vertices use the exact chiral and antichiral cubic words, not a scalarized effective vertex.  Retain all endpoint terms of every derivative difference.  The common color reduction is

$$
\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E}
=\mathbb F^{AB}{}_{DE},
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

## Corrected structural census

The former 495-route census omitted a genuine one-loop incidence family.  The full marked census now has

$$
N_{\rm parent}=495+870=1365.
$$

For ordered $A__A$, the omitted family contains exactly 42 directed Wick routes:

$$
N_{AA}^{\rm spectator}=36\,TGG+6\,TMM.
$$

Its incidence is

$$
I_0(A_L,A_R):\quad A_L\text{ external spectator},
\qquad A_R\longrightarrow V_1,
$$

$$
V_1\mathrel{\substack{\longleftrightarrow\\[-2mm]\longleftrightarrow}}V_2,
\qquad
V_2\longrightarrow u_{\rm ext},
$$

plus the reflected source choice.  Here $V_1,V_2$ are either the two gauge cubic vertices or two same-flavor $\widetilde\Phi u\Phi$ vertices.  These are precisely the standard two-gauge-vertex and two-matter--gauge-vertex one-loop triangles.  With three internal edges and three vertices,

$$
E=3,
\qquad V=3,
\qquad L=E-V+1=1.
$$

The 36 gauge routes resolve the three position-labelled $u$ ports and both bridge bijections; the six matter routes are two source choices times three flavors.  Do not infer a multiplicity coefficient from these counts: derive the vertex polarization, Wick factor, Koszul sign and D-word for every orbit.

Separate the two mark types:

1. the marked letter is the quantum source edge and may select an inverse kernel;
2. the marked letter is the external spectator and has no internal selected edge unless product-rule transport creates one, which must be displayed.

Also check typed FP/ghost and auxiliary triangles.  Either include each admitted one-loop port route or prove it is absent before momentum integration.  A statement that ghosts do not couple to the composite source is insufficient if the source quantum $u$ can attach to a ghost--gauge vertex.

## First exact error in the former split-source VVV result

The older checker claimed $-\lambda_1/8$ by inserting `selected_square=-4`.  That inference is withdrawn.  The exact sparse Grassmann replay splits

$$
D_-A_1
=\underbrace{\sqrt2\,\bar r_e^2D_+u}_{\mathcal S_e}
+\underbrace{\frac{\sqrt2}{16}D_+\bar D^2D^2u}_{\mathcal L_e}.
$$

For both source marks, all four endpoint rows obey

$$
\mathcal G_{\mathcal S_e}=0,
\qquad
\mathcal G_{\rm full}=\mathcal G_{\mathcal L_e}.
$$

The surviving endpoint polynomials are

$$
\text{mark}_{01}:(0,+b_1W_{02},0,+b_0W_{02}),
$$

$$
\text{mark}_{02}:(0,-b_1W_{02},0,+b_0W_{02}),
\qquad
W_{02}=a_0b_2-b_0a_2.
$$

In the fixed Euclidean frame the old summed rank-two diagonal is

$$
(-2,+2,0,0),
\qquad
\operatorname{tr}_4C=0.
$$

Therefore one may not use

$$
4r_{+\dot\alpha}r_-{}^{\dot\alpha}=-4\bar r^2
$$

unless the two spinor factors in that row are proved to carry the same tagged momentum $r_e$.  Replay the transported longitudinal word and its neighbouring-edge contacts.  Decide target-blind whether the entire old split-source VVV orbit is zero or nonzero.

## Required calculation

Compute all three pieces separately:

$$
C_{AA}^{\rm gauge output}
=C_{\rm split\ source,TGG}
+C_{\rm spectator,TGG}
+C_{\rm spectator,TMM},
$$

including every Schwinger/contact descendant exactly once.  For each nonzero or cancelling occurrence print

$$
(\mathrm{id},\mathrm{family},\mathrm{mark},\mathrm{field\ loop},
\mathrm{ports},\mathrm{vertex/Wick/Koszul\ factor},
\mathrm{raw\ D\!\!-word},r_e,
\mathrm{full\!\!-d\ contact},
\mu_\ell^2\mathrm{\ remainder},
\mathrm{simplex\ moment},
\mathrm{normalized\ output}).
$$

Compute the reflected carrier independently.  End with the target-blind ordered vector

$$
(c_{D>A},c_{A>D})
$$

in $\lambda_1\mathbb F^{AB}{}_{DE}$ units.

Only after sealing that vector compare with the external holomorphic-twist row

$$
(c_{D>A},c_{A>D})_{\rm HT}=(+1,-1).
$$

If there is a mismatch, identify the first exact occurrence row where it arises; do not add a counterterm or a fitted multiplicity.
