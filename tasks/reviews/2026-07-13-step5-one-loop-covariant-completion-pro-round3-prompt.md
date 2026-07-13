# Step 5 one-loop covariant-completion review — GPT Pro round 3 prompt

This round replaces the incorrect spin label in round 2.  It is an external
gap audit only.  No anomaly coefficient or known result may be imported.

Use the Project Euclidean algebra

$$
\epsilon^{+-}=1,
\qquad
\epsilon_{+-}=-1,
\qquad
\{\nabla_a,\nabla_b\}=0,
\qquad
\{\nabla_a,\bar\nabla_{\dot b}\}
=-2\mathcal D_{a\dot b}.
$$

Define

$$
X_{ab}:=\nabla_{(a}W_{b)},
\qquad
E:=\nabla^aW_a,
\qquad
T_{bcde}^{AB}:=X_{(bc}^AX_{de)}^B,
\qquad
U_{a;bcde}^{AB}:=\nabla_aT_{bcde}^{AB}.
$$

The exact Project certificates already give

$$
\nabla_{(a}X_{bc)}=0,
\qquad
H_{abcde}:=\nabla_{(a}T_{bcde)}=0,
$$

$$
t_{cde}:=\epsilon^{ab}U_{a;bcde},
\qquad
U_{-;++++}=-\frac45t_{+++},
$$

$$
E=\nabla_-W_+-\nabla_+W_-,
\qquad
\nabla_+E=-\nabla_-X_{++},
$$

$$
\mathscr I^{AB}
:=\nabla_-(X^AX^B)
=-(\nabla_+E^A)X^B-X^A(\nabla_+E^B).
$$

Define only the temporary formal grading

$$
r_{\mathrm f}(\nabla_a)=-1,
\qquad
r_{\mathrm f}(W_a)=+1,
\qquad
r_{\mathrm f}(\widetilde W_{\dot a})=-1,
\qquad
r_{\mathrm f}(\mathcal D_{a\dot a})=0.
$$

Its identification with the Project (U(1)_R) charge is open.  With this
grading, the chiral-constrained seed is in the
\(j_L=\tfrac32,j_R=0,r_{\mathrm f}=-1\) sector.  Its full-superspace source is

$$
S_J=\int d^8z\,J_{AB}\mathscr I^{AB},
\qquad
[J]=-\frac52,
\qquad
r_{\mathrm f}(J)=+1,
\qquad
|J|=1.
$$

There is now one hard sign/type conflict.  Set

$$
Y^A_{\dot a}:=\mathcal D_{+\dot a}X^A,
\qquad
Y^{A\dot a}:=\epsilon^{\dot a\dot b}Y^A_{\dot b},
\qquad
|Y|=0,
$$

and read the previously obtained local candidate literally:

$$
\mathscr O_-^{AB}
=c_{ACD}c_{BCE}
\left[
\widetilde W^D_{\dot a}Y^{E\dot a}
-Y^{D\dot a}\widetilde W^E_{\dot a}
\right].
$$

Because \(Y\) is even,

$$
Y^{D\dot a}\widetilde W^E_{\dot a}
=\widetilde W^E_{\dot a}Y^{D\dot a},
$$

so the literal bracket is antisymmetric in \(D,E\), and

$$
\mathscr O_-^{BA}=-\mathscr O_-^{AB}.
$$

An exact component witness is

$$
Y_{\dot a}=(a,b),
\qquad
\widetilde W_{\dot a}=(c,d),
\qquad
Y^{\dot a}=(b,-a),
$$

$$
Y^{\dot a}\widetilde W_{\dot a}
=bc-ad
=\widetilde W_{\dot a}Y^{\dot a},
$$

whereas \(Y_{\dot a}\widetilde W^{\dot a}=ad-bc\).  The upper--lower and
lower--upper contractions cannot be substituted for one another.

Please independently audit the following.

1. Recompute the literal dotted-index variance and the \(A\leftrightarrow B\)
   symmetry.  Do not change index height during field reordering.

2. The graph ledger uses ordered external slots \(A|B\) with separate
   momenta, whereas the coincident component product of the even fields
   satisfies \(X^AX^B=X^BX^A\).  Construct the exact momentum-and-color
   exchange map from the ordered ledger to the physical local source.  Decide
   whether the physical sector is
   \(\operatorname{Adj}\otimes\operatorname{Adj}\),
   \(\operatorname{Sym}^2(\operatorname{Adj})\), or an ordered point-split
   carrier followed by a finite contact quotient.  Do not guess.

3. Recompute the reflected-orientation sign from the original pre-\(D\)
   external word, every endpoint-transfer sign, the fact that
   \(|W|=|\widetilde W|=1\), and the final parity \(|X|=|Y|=0\).  Determine
   whether the physical completion requires the displayed minus combination
   or the plus combination

   $$
   c_{ACD}c_{BCE}
   \left[
   \widetilde W^D_{\dot a}Y^{E\dot a}
   +Y^{D\dot a}\widetilde W^E_{\dot a}
   \right].
   $$

4. Audit a pure-gauge injectivity proof for the fixed quadratic jet.  At
   dimension \(9/2\), \(r_{\mathrm f}=-1\), and
   \((j_L,j_R)=(3/2,0)\):
   - the complete free ordered census contains five field-strength-degree
     zero rows and seven degree-one rows; these must be eliminated in the
     BRST/EOM/IBP/color quotient before one may assert that a quadratic-jet
     kernel starts at degree three;
   - four field strengths are excluded by dimension;
   - three field strengths require \(W\widetilde W\widetilde W\), whose
     right-scalar contraction has \(j_L=1/2\);
   - the quadratic \(WW\nabla^3\) family should reduce to the EOM ideal using
     \(\nabla_bE=-\tfrac12\nabla^2W_b\);
   - the quadratic \(W\widetilde W\nabla\mathcal D\) tensor product contains
     the target Lorentz representation once.

   Identify every missing IBP, derivative-placement, commutator, color, and
   evanescent relation before claiming \(\ker\ell_2=0\).

5. State the corrected conditional theorem using only injectivity of
   \(\ell_2:H\to\mathcal T_2\).  A rank-one corollary may be stated only after
   the color/source channel is fixed.

6. Retain the exact Hessian/source census

$$
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}
\left[
+G_0I_0G_0H_1G_0H_1
-G_0I_0G_0H_2
-G_0I_1G_0H_1
+G_0I_2
\right]
+\mathrm{CT}_2,
$$

but do not use it to bypass the ordered-to-physical exchange sign.

7. The current graph schema labels the external port

$$
\operatorname{Source}[\nabla_-(XX)]
$$

as bosonic, while both the composite insertion and its dual source are odd:

$$
|\mathscr I|=1,
\qquad
|J|=1,
\qquad
|J\mathscr I|=0.
$$

Determine whether the GraphIR port is an inert insertion marker excluded from
the Koszul algebra, the odd source $J$, or the odd insertion $\mathscr I$.  If
it is either of the latter two, recompute the orientation signs with fermionic
typing; do not silently retain the bosonic declaration.

Return a formula-first audit.  No numerical coefficient is requested.
