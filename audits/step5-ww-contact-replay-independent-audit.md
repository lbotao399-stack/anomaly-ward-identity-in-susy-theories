# Step 5 WW contact replay: independent audit

## 0. Scope and notation

Checked files:

$$
\begin{gathered}
\texttt{scripts/step5\_ww\_contact\_replay.py},\qquad
\texttt{generated/step5/contact-replay/ww-contact-replay.json},\\
\texttt{audits/step5-ww-contact-replay.md},\qquad
\texttt{audits/step5-ww-contact-replay-verification.json},\\
\texttt{tests/test\_step5\_ww\_contact\_replay.py},\qquad
\texttt{contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md}.
\end{gathered}
$$

Notation:

$$
H[B]=H_0+H_1[B]+H_2[B,B]+\cdots,qquad
I[B]=I_0+I_1[B]+I_2[B,B]+\cdots,qquad
G[B]=H[B]^{-1}.
$$

The audit checked eleven equation/claim groups.  Verdict:

$$
\boxed{
\texttt{FAIL\_CLOSED\_PHYSICAL\_CONTACT\_FAMILY};\qquad
\Gamma_{C,\mathrm{pole}}=\texttt{NOT\_COMPUTED};\qquad
C_{\mathrm{anomaly}}=\texttt{NOT\_ACCEPTED}.}
$$

The artifact is a reproducible partial census.  It is not a completed contact
amplitude.

## 1. Exact functional expansion

For homogeneous Taylor coefficients and even total kernels,

$$
\begin{aligned}
G^{[0]}&=G_0,\\
G^{[1]}&=-G_0H_1G_0,\\
G^{[2]}&=G_0H_1G_0H_1G_0-G_0H_2G_0,
\end{aligned}
$$

because

$$
\begin{aligned}
&(H_0+H_1+H_2)
\left(G_0-G_0H_1G_0+G_0H_1G_0H_1G_0-G_0H_2G_0\right)\\
&=H_0G_0
-H_0G_0H_1G_0+H_1G_0\\
&\quad
+H_0G_0H_1G_0H_1G_0-H_1G_0H_1G_0
-H_0G_0H_2G_0+H_2G_0\\
&=\mathbf 1.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
\left[\frac12\operatorname{STr}(GI)\right]_{B^2}
=\frac12\operatorname{STr}\Big(&
G_0H_1G_0H_1G_0I_0-G_0H_2G_0I_0\\
&-G_0H_1G_0I_1+G_0I_2\Big).
\end{aligned}
$$

Cyclicity gives the script's four signs:

$$
\begin{aligned}
\operatorname{STr}(G_0H_1G_0H_1G_0I_0)
&=\operatorname{STr}(G_0I_0G_0H_1G_0H_1),\\
\operatorname{STr}(G_0H_2G_0I_0)
&=\operatorname{STr}(I_0G_0H_2G_0),\\
\operatorname{STr}(G_0H_1G_0I_1)
&=\operatorname{STr}(I_1G_0H_1G_0).
\end{aligned}
$$

This sign check is conditional on

$$
H_r=[B^r]H[B],\qquad I_r=[B^r]I[B],\qquad
|J\mathscr I|=|H_r|=|I_r|=0.
$$

These coefficient and parity definitions are not supplied locally by the
replay.  The functional word is structurally correct; its normalization is not
certified.

## 2. Hessian contacts and cut contacts

The replay constructs

$$
\begin{aligned}
Q_{\mathrm{Hess}}^{(2)}={}&
-\frac12\operatorname{STr}(I_0G_0H_2G_0)\\
&-\frac12\operatorname{STr}(I_1[p_1]G_0H_1[p_2]G_0)\\
&-\frac12\operatorname{STr}(I_1[p_2]G_0H_1[p_1]G_0)
+\frac12\operatorname{STr}(I_2G_0).
\end{aligned}
$$

The Project contract also requires the collapsed triangle children.  Their
coefficient-bearing sum is

$$
Q_{\mathrm{cut}}^{(2)}
=\sum_{o\in\{\mathrm D,\mathrm R\}}
\sum_{t=1}^{8}\sum_{e\in\{e_0,e_1,e_2\}}
C_{o,t,e}\,\operatorname{Collapse}_{e}(\Gamma_{\triangle,o,t}).
$$

Hence the physical renormalized contact/cut family is

$$
\boxed{
Q_{\mathrm{phys}}^{(2)}
=Q_{\mathrm{Hess}}^{(2)}+Q_{\mathrm{cut}}^{(2)}+\mathrm{CT}_2.}
$$

This is a regrouping, not an additional term.  With

$$
Q_{\mathrm{cut}}^{(2)}
=\mathcal R_{\mathrm{cut}}Q_{\triangle}^{\mathrm{bare}},
\qquad
Q_{\triangle}^{\mathrm{irr}}
=(1-\mathcal R_{\mathrm{cut}})Q_{\triangle}^{\mathrm{bare}},
$$

one must use

$$
\Gamma_{\mathscr I,2}^{(1)}
=Q_{\triangle}^{\mathrm{irr}}+Q_{\mathrm{phys}}^{(2)},
$$

not \(Q_{\triangle}^{\mathrm{bare}}+Q_{\mathrm{phys}}^{(2)}\).  The present
artifact does not construct \(\mathcal R_{\mathrm{cut}}\).

The artifact stores forty-eight collapse bindings but sets

$$
C_{o,t,e}=\texttt{NOT\_PERFORMED\_REQUIRES\_EDGE\_COLLAPSE\_D\_ALGEBRA}
$$

and omits $Q_{\mathrm{cut}}^{(2)}$ from
`complete_Q_contact`.  Therefore `complete_Q_contact` is complete only as the
four-term Hessian Taylor word plus $\mathrm{CT}_2$; it is not the complete
physical contact/cut orbit.

## 3. Exact count taxonomy

The independently reproducible counts are

$$
\begin{aligned}
N_{I_3S_3}^{\mathrm{labeled}}
&=30\cdot6\cdot2=360,\\
N_{I_4}^{\mathrm{unlabeled\ BQ\ assignment}}
&=30\binom42=180,\\
N_{\mathrm{collapse\ binding}}
&=2\cdot8\cdot3=48,\\
N_{\mathrm{collapse\ GraphIR}}^{\mathrm{unique}}
&=6.
\end{aligned}
$$

The JSON has five topology-level Hessian/contact GraphIR objects:

$$
\{I_0H_2,\ I_1[p_1]H_1[p_2],\ I_1[p_2]H_1[p_1],\ I_2,\ \mathrm{CT}_2\}.
$$

The numbers

$$
576,\qquad1440,\qquad1440,\qquad720
$$

are stored as `ordered_vector_branch_paths`.  They are literals in the replay;
the replay neither constructs that many GraphIR objects nor derives the
functional-Hessian multiplicities.  Consequently

$$
N_{I_0H_2}=576,qquad N_{I_1H_1}=1440,qquad N_{I_2}=720
$$

in the rendered audit cannot be read as graph counts.  The certified statement
is only

$$
(N_{\rm branch}^{I_0H_2},N_{\rm branch}^{I_1H_1;p_1p_2},
N_{\rm branch}^{I_1H_1;p_2p_1},N_{\rm branch}^{I_2})
=(576,1440,1440,720),
$$

with the branch-generation proof still absent.

## 4. Sign and normalization ledger

The Euclidean Wick expansion gives one sign:

$$
e^{-S_3/\hbar}=1-\frac{S_3}{\hbar}+\frac{S_3^2}{2\hbar^2}+\cdots,qquad
-\frac1\hbar\langle I_1S_3\rangle_{0,c}.
$$

The same sign appears in the Hessian representation:

$$
-\frac12\operatorname{STr}(I_1G_0H_1G_0),qquad H_1=S_3^{(2)}.
$$

They are two encodings of one contraction, not two multiplicative signs.  The
replay stores both

$$
\texttt{action\_expansion\_factor}=-1,qquad
\texttt{neumann\_sign}=-1,
$$

but supplies no transport equation identifying them.  Before numerical row
assembly one must prove

$$
C_{\rm Wick}(I_1,S_3)
=C_{\rm Hess}(I_1,H_1),
$$

including the supertrace factor $1/2$, the two labeled Wick pairings, the
functional derivatives in $H_1=S_3^{(2)}$, and all Koszul signs.  Multiplying
the two stored minus signs would give an incorrect plus sign.

## 5. $I_4$ scaleless statement

If every $I_4$ row has exactly one massless loop denominator and a polynomial
numerator,

$$
P(k,p_1,p_2)=\sum_{\alpha,\beta,\gamma}
c_{\alpha\beta\gamma}k^{\alpha}p_1^{\beta}p_2^{\gamma},
$$

then

$$
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{P(k,p_1,p_2)}{k^2}
=\sum_{\alpha,\beta,\gamma}
c_{\alpha\beta\gamma}p_1^{\beta}p_2^{\gamma}
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{k^{\alpha}}{k^2}=0.
$$

The full DRED integral is then zero.  It does not determine the ordinary UV
pole:

$$
I_{\rm scaleless}=I_{\rm UV}+I_{\rm IR}=0,qquad
I_{\rm UV}=-I_{\rm IR},qquad
I_{\rm UV}\ \texttt{NOT\_DETERMINED}.
$$

The replay correctly leaves the UV/IR split open.  Its proof of the premise is
insufficient: `local_AST_gives_polynomial_momentum_numerator` is computed only
from

$$
\operatorname{Ops}(\mathrm{AST})\subseteq
\texttt{SUPPORTED\_COLOR\_OPERATORS},
$$

while the same operator whitelist is already required by the AST compiler.
No edge-tagged $D$-algebra trace proves, row by row, the absence of an inverse
projector or an additional loop denominator.  Thus

$$
N_{I_4,\mathrm{DRED\ zero}}=180
$$

is conditional on a missing locality-to-polynomial lemma; the ordinary UV pole
remains correctly fail-closed.

## 6. Color tensors

For each retained $I_3S_3$ or $I_4$ row, the compiler produces

$$
T_r^{AB}{}_{DE}
=\prod_{u}c_{a_ub_u}{}^{d_u}
\prod_v\kappa_{e_vf_v}
\prod_w\kappa^{g_wh_w}
\prod_x\delta_{i_x}{}^{j_x}.
$$

The following incidence statements pass:

$$
\begin{gathered}
N_{\rm compiled}=360+180=540,\\
\{\mathrm{id}_{\rm color}^{I_3S_3}\}
=\{\mathrm{id}_{\rm scalar}^{I_3S_3}\},\qquad
\{\mathrm{id}_{\rm color}^{I_4}\}
=\{\mathrm{id}_{\rm scalar}^{I_4}\},\\
N_{\rm free}(A,B;D,E)=(2;2),\qquad
N_{\rm unmatched\ dummy}=0.
\end{gathered}
$$

The physical color reduction is not performed:

$$
\sum_{r=1}^{360}C_rT_r^{AB}{}_{DE}
\xrightarrow[
\kappa\text{-invariance}
]{c_{AB}{}^C=-c_{BA}{}^C,\ \mathrm{Jacobi}}
C_{\rm phys}\,c_{ACD}c_{BCE}
\quad\texttt{NOT\_COMPUTED}.
$$

Moreover, the 540 tensors exclude $I_0H_2$, collapsed children, and
$\mathrm{CT}_2$.  The reported number 102 is the number of syntactic SHA
classes, not the dimension of the Lie-identity quotient:

$$
102=|\mathcal C_{\rm syntactic}/\mathrm{SHA}|,qquad
\dim\frac{\mathcal C}
{\langle\text{antisymmetry},\text{Jacobi},\kappa\text{-invariance}\rangle}
=\texttt{NOT\_COMPUTED}.
$$

The scalar/color split also deletes every `kappa^-1` token without checking

$$
N_{\kappa^{-1}}(C_{\rm input})=N_{\rm internal\ propagators}.
$$

Thus `OPEN_CONTACT_002` is closed only for index incidence in the 540-row
subset; it is open for the complete physical color coefficient.

## 7. Gap table

| gap | type | location | claim | missing exact check | severity |
|---|---|---|---|---|---|
| G1 | G-SCOPE | `build_complete_contact_hessian_family`, `build_collapsed_certificate` | `complete_Q_contact` is complete | Add $Q_{\rm cut}^{(2)}$ with all $C_{o,t,e}$; include it in the pole sum | P1 |
| G2 | G-DEF | `build_payload`, complete quadratic family | the four Hessian words have fixed normalization | Define $H_r=[B^r]H$, $I_r=[B^r]I$, their factorial convention, parity, and the quadratic insertion prefactor | P1 |
| G3 | G-SIGN | `build_projection_and_coefficients`, `complete_Q_contact.terms` | $C_{\exp}=-1$ and `neumann_sign=-1` are both usable factors | Prove the Wick-to-Hessian transport and use the unique minus sign once | P1 |
| G4 | G-NORM | branch-count fields and rendered $N_{I_0H_2},N_{I_1H_1},N_{I_2}$ | 576, 1440, 1440, 720 are graph counts | Generate branch objects, quotient identical functional derivatives, and distinguish branches, Wick rows, topology GraphIR, and physical graphs | P1 |
| G5 | G-ALG | `build_i0_h2_certificate` | six intrinsic $S_4$ terms determine the full $H_2$ contribution | Construct the actual background/quantum Hessian, its color tensors, projector $D$-algebra, and routed integrand | P1 |
| G6 | G-THM | `build_tadpole_certificate` | all 180 $I_4$ rows have polynomial numerator over $k^2$ | Prove the locality-to-polynomial lemma on the edge-tagged $D$-algebra output for every row | P1 |
| G7 | G-IDX | `build_color_records` | `PASS_EXPLICIT_C_KAPPA_DELTA_TENSORS` closes color | Reduce the coefficient-weighted tensor sum; include $I_0H_2$, cut children, and $\mathrm{CT}_2$; check metric-token multiplicity | P1 |
| G8 | G-NORM | `build_automorphism_certificate` | all contact automorphism orders equal one | Compute the stabilizer of each contact GraphIR and match it to Taylor/Wick factorials; the current contact value is assigned as the constant 1 | P1 |
| G9 | G-DEF | `normal_order_policy` | absence of an AST `NormalOrder` node proves raw-composite self-contractions | State the bare composite renormalization prescription in the Project contract; Grassmann normal order is not Wick normal order | P2 |
| G10 | G-THM | `exact_checks`, tests, verification JSON | 19/19 establishes a scoped calculation PASS | Replace literal/status equality tests by independent coefficient, sign, stabilizer, color-reduction, and integral checks | P1 |

## 8. Tautological PASS surface

The following checks compare values to literals assigned by the same builder:

$$
\begin{gathered}
\texttt{I0H2\_not\_falsely\_removed\_by\_intrinsic\_chirality},\quad
\texttt{complete\_contact\_has\_five\_required\_terms},\\
\texttt{complete\_contact\_branch\_counts\_exact},\quad
\texttt{Euclidean\_action\_factor\_minus\_one},\\
\texttt{all\_contact\_automorphisms\_order\_one},\quad
\texttt{resolved\_open\_partition\_exact},\quad
\texttt{remaining\_gates\_fail\_closed},\\
\texttt{tau\_channel\_retained},\quad
\texttt{no\_contact\_pole\_or\_anomaly\_coefficient},\quad
\texttt{no\_external\_results}.
\end{gathered}
$$

`kappa_metric_not_left_in_scalar_coefficient` is also circular because
`without_kappa_placeholder` deletes all such tokens before the check.
`all_I4_raw_self_contractions_admitted_and_scaleless` inherits the unproved
polynomial predicate.  These checks protect schema and fail-closed boundaries;
they do not prove a contact amplitude.

## 9. Independent spot checks

### Check A: functional signs

$$
(H_0+H_1+H_2)^{-1}\Big|_{B^2}
=G_0H_1G_0H_1G_0-G_0H_2G_0.
$$

Result:

$$
\texttt{PASS\_CONDITIONAL\_ON\_TAYLOR\_AND\_PARITY\_DEFINITIONS}.
$$

### Check B: row/color bijections

Direct JSON readback gives

$$
\begin{aligned}
\operatorname{sort}(\mathrm{id}_{\rm color}^{I_3S_3})
&=\operatorname{sort}(\mathrm{id}_{\rm scalar}^{I_3S_3}),\\
\operatorname{sort}(\mathrm{id}_{\rm color}^{I_4})
&=\operatorname{sort}(\mathrm{id}_{\rm scalar}^{I_4}),
\end{aligned}
$$

with unique IDs in both sets.  Result:

$$
\texttt{PASS\_ROW\_INCIDENCE};\qquad
\texttt{PHYSICAL\_COLOR\_REDUCTION\_OPEN}.
$$

### Check C: deterministic execution

Targeted execution gives

$$
N_{\rm tests}=9,qquad N_{\rm failed}=0,qquad
N_{\rm exact\ checks}=19,qquad N_{\rm failed\ checks}=0.
$$

Result:

$$
\texttt{PASS\_BYTE\_REPRODUCIBILITY};\qquad
\texttt{FAIL\_CLOSED\_PHYSICAL\_COEFFICIENT}.
$$

## 10. Repair order

$$
\boxed{
\mathrm{G2}\prec\mathrm{G3}\prec\mathrm{G5}\prec\mathrm{G8}
\prec\mathrm{G7}\prec\mathrm{G6}\prec\mathrm{G1}\prec\mathrm{G10}.}
$$
