# GPT Pro Gate 3: AA full polarized cubic vertex and induced Schwinger contacts

Work target-blind. Gate 2Y is only a proof of the fixed-external-field-strength-slot Hessian. It is not the full third functional derivative of the cubic action.

## Locked mechanism

$$
g_d=\bar g+\widetilde g,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2=-\widetilde\ell^2,
$$

$$
\frac{r_{e,d}^2}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}=0,
$$

$$
\frac{\bar r_e^2}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

There is no independent graph-specific factor $4-d$.

## Exact component counterexample to Gate 2Y

Use

$$
p=e_0,
\qquad q=e_1,
\qquad \varepsilon=e_3,
\qquad
r_0=\ell,quad r_1=\ell-q,quad r_2=\ell-p-q,
$$

with external $A$ at momentum $p$, external $D$ at momentum $q$, and dotted index $\dot\alpha=0$.  The source is the corrected

$$
W^\gamma D_\gamma\big|_{W_+}=-W_+D_-.
$$

The exact finite Grassmann/color component engine directly differentiates every cubic word of (5A.52) with three independently labeled fields. At

$$
\ell=(2,-1,1,3)
$$

it gives, for the physical $(-,+)$ action chirality,

$$
N_{\rm full}=6-\frac{19}{2}i,
\qquad
N_{\rm fixed\ field\ strength}=-5.
$$

Thus the two expressions are not related by a multiplicity.  The fixed-field-strength calculation includes only the 16 raw rows where the external background occupies the linear field-strength slot.  It omits the 32 rows where the external background occupies either

1. the differentiated entry of $[D u,u]$ or $[\bar D u,u]$;
2. the undifferentiated entry of that commutator.

For the two occurrence-resolved source tags,

$$
T_0=I0\_DminusA1[A]*A1[B],
\qquad
T_2=I0\_A1[A]*DminusA1[B],
$$

the same exact replay gives

$$
N_{\rm full,0}=34-8i,
\qquad
N_{\rm full,2}=-28-\frac32i,
$$

whereas the selected pieces factor edgewise:

$$
N_{S,0}=\bar r_0^2R_0,
\qquad
N_{S,2}=\bar r_2^2R_2,
$$

$$
R_0(\ell)=
-\frac12+2i
+\left(1-\frac32i\right)\ell_0
+\left(-\frac12-2i\right)\ell_1
-\frac i2\ell_2-\frac i2\ell_3,
$$

$$
R_2(\ell)=
\frac i2
+\left(-1-\frac i2\right)\ell_0
+\frac12\ell_1
-\frac i2\ell_2-\frac i2\ell_3.
$$

At the displayed loop momentum,

$$
N_{S,0}=30-15i,
\qquad
N_{S,2}=-\frac{75}{2}(1+i).
$$

Define exact longitudinal remainders

$$
L_e:=N_{\rm full,e}-\bar r_e^2R_e.
$$

The induced derivative-of-action contact must be constructed on the same occurrence and edge:

$$
C_{e,d}:=-L_e-r_{e,d}^2R_e.
$$

Then the required row identity is

$$
N_{\rm full,e}+C_{e,d}
=(\bar r_e^2-r_{e,d}^2)R_e
=\mu_\ell^2R_e.
$$

The contact is not an independently evaluated source bubble, and an affine two-denominator contact is not zero.

## Immediate correction from an independent held-out loop

The two displayed affine formulas for $R_0,R_2$ were fitted from five loop
samples and are **retracted as identities**.  The independent exact sample

$$
\ell=(3,2,-2,1)
$$

gives

$$
N_{S,0}=-9+27i,
\qquad
N_{S,2}=-40+70i,
$$

which does not obey those affine fits.  Therefore a source tag $T_0$ or $T_2$
alone is not a complete edge-occurrence label after the two missing action
placement families are restored.  Each raw action placement must also carry
its own collapsed edge $e_j$.  Do not divide the aggregate $T_0$ sum by
$\bar r_0^2$, or the aggregate $T_2$ sum by $\bar r_2^2$.  The actual object
to prove is the raw-row decomposition

$$
N_{S,j}=Q_j\bar r_{e_j}^{,2},
\qquad
C_{j,d}=-L_j-Q_jr_{e_j,d}^{,2},
$$

$$
N_{{\rm full},j}+C_{j,d}=Q_j\mu_\ell^2.
$$

## Required exact replay

1. Expand the chiral and antichiral cubic actions into the three external-position families: linear field-strength slot, differentiated commutator slot, undifferentiated commutator slot. Give every rational coefficient and sign. Sum the three families and reproduce the exact full component values above. Explicitly show why Gate 2Y proved only the first family.

2. For each combined source/action occurrence, calculate the full, selected, and longitudinal numerators. Use the held-out sample to reject the aggregate affine fit, then derive the true raw-row quotients $Q_j$ and collapsed edges $e_j$. No aggregate harmonic trace may replace occurrence tagging.

3. Construct the induced contacts $C_{0,d},C_{2,d}$ directly from the Schwinger-Dyson derivative of the same full action. Prove row by row that replacing $\bar r_e^2$ by $r_{e,d}^2$ makes parent plus contact exactly zero and that the only DRED remainder is $\mu_\ell^2R_e$.

4. Integrate the affine quotients with

$$
\langle\ell\rangle=\frac{p+2q}{3}
$$

for the locked routing, keeping every typed ordered structure distinct. Include all action, source, propagator, color, Wick, and reflection factors exactly once.

5. Derive the reflected orientation independently from ordered functional derivatives. Do not infer its sign from a single fixed $SU(2)$ color component. Give the complete target-blind ordered AA coefficient vector. Only after that compare with the holomorphic-twist result and locate the first remaining mismatch, if any.

Forbidden: replacing the full polarized vertex by fixed-$W$, multiplying by 72, deleting affine contacts, using a global four-dimensional tensor trace as the cut, or inserting the target coefficient.
