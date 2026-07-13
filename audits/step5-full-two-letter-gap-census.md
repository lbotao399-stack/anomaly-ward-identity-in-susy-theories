# Step 5 full two-letter gap census

Input:

- `contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md`
- `scripts/step5_graph_ir.py`
- `scripts/step5_vertex_grammar.py`
- `scripts/step5_project_composites.py`
- `scripts/step5_ww_seed.py`
- `scripts/verify_step5_propagators.py`
- `scripts/verify_step5_dred_integrals.py`

Checked displayed equation groups in §§5.9--5.11e: \(44\).

## Exact census

$$
X^A=(\nabla_+W_+)^A,
\qquad
Y_r^A=(\nabla_+\Phi_r)^A,
\qquad
Z_r^A=\widetilde\Phi_r^A,
\qquad
T_{\dot a}^A=\widetilde W_{\dot a}^A.
$$

$$
(n_X,n_Y,n_Z,n_T)=(1,3,3,2),
\qquad
N_{\rm family}=4^2=16,
\qquad
N_{\rm component}=(1+3+3+2)^2=81.
$$

$$
N_{\rm family}^{\rm implemented}=1,
\qquad
N_{\rm family}^{\rm open}=15,
\qquad
N_{\rm component}^{\rm open}=80.
$$

The four tree-zero families are

$$
(Z,Z),\ (Z,T),\ (T,Z),\ (T,T),
\qquad
N_{\rm component}^{\rm tree\ zero}=(3+2)^2=25.
$$

The eleven unimplemented nonzero families contain

$$
80-25=55
$$

component channels.  The family AST contains

$$
N_{\rm descendant\ terms}=32,
$$

while index resolution gives

$$
N_{\rm descendant\ terms}^{\rm component}=144.
$$

## Gap table

| id | type | location | claim | missing exact step | severity | status |
|---|---|---|---|---|---|---|
| G1 | G-ALG | (5.53w)--(5.53y), `metric_contact_children()` | the WW contact family has the required pole | expand all legal \(I_{(3)}\widetilde S_{(3)}\), \(I_{(4)}\), and collapsed terms into physical Wick graphs with coefficients, symmetry factors, derivative words, and routed integrands | P1 | OPEN |
| G2 | G-THM | `pole_ledger()` | ordinary WW terms cancel | replace result strings by a graph-driven equality of triangle, bubble, quartic, and collapsed integrands; verify finite/nonlocal and propagator-canceling terms, not only the UV metric pole | P1 | OPEN |
| G3 | G-DEF | `step5_project_composites.py` | the four-letter loop family is generated | implement \(Y_{r,(n)},Z_{r,(n)}\), expose the existing \(\widetilde W_{(n)}\) recursion as the \(T_{\dot a,(n)}\) letter, and generate every channel insertion \(I_{ij,(N)}\); current insertion grammar generates only \(I_{XX,(N)}\) | P1 | OPEN |
| G4 | G-PROJ | `step5_vertex_grammar.py` to `GraphIR` | action monomials define physical vertices | compile exact coefficient, derivative scope, color/flavor contraction, ordered ports, and background/quantum assignments into physical `GraphIR.Vertex` objects | P1 | OPEN |
| G5 | G-DEF | `verify_step5_propagators.py`, `PropagatorGrammar` | all admitted Green kernels are usable by the graph census | expose \(P_{VV}\), \(P_{\Phi_r\widetilde\Phi_s}\), its reverse orientation, color/flavor deltas, projectors, and typed-zero pairings as exact edge kernels | P1 | OPEN |
| G6 | G-ALG | `DAlgebraEngine`, `step5_ww_seed.py` | channel D-algebra is automated | implement anticommutators, nilpotence, chirality, \(D^2\bar D^2D^2\) collapse, edge momenta, external derivatives, and exact \(\mathbb Q(i)\) coefficients; the current eight rows are WW-hardcoded | P1 | OPEN |
| G7 | G-ALG | `verify_step5_dred_integrals.py` | the DRED reducer covers all channels | derive the numerator rank from each graph and dispatch the required tensor masters; retain \(p^2,q^2,(p+q)^2>0\) until UV/IR poles are separated; the current path covers the routed WW rank-two numerator | P1 | OPEN |
| G8 | G-SCOPE | §§5.5--5.8 versus §5.11 | the 16 tree channels are one-loop channels | filter the 27 action monomials through actual typed Wick kernels; prove absence when no connected one-loop graph exists | P1 | OPEN |
| G9 | G-THM | four tree-zero families | \(dZ=dT=0\) implies the renormalized products vanish | prove that regulator/contact mixing produces no local descendant in \(ZZ,ZT,TZ,TT\), or compute the induced mixing | P1 | OPEN |
| G10 | G-SCOPE | (5.54b) | primitive FP/NK absence is channel-independent | rerun the typed-port loop census for every physical insertion family | P2 | OPEN |
| G11 | G-DEF | full operator-mixing matrix | each local mixing coefficient is detected | specify a nondegenerate set of external 1PI probes and prove that it separates every same-quantum-number local operator | P1 | OPEN |
| G12 | G-THM | aggregate cutting identity | regularization and SD cutting differ only by the displayed metric | define both ordered operations \(R_\epsilon C_{\rm SD}\) and \(C_{\rm SD}R_\epsilon\), then derive their finite commutator on every parent orbit | P1 | OPEN |
| G13 | G-OP | explicit contact basis versus collapsed basis | both representations can be summed together | construct a bijective change of basis between explicit \(I_{(3)}S_{(3)}\), \(I_{(2)}S_{(4)}\), \(I_{(4)}\) graphs and collapsed/cut representatives before forming the orbit sum | P1 | OPEN |
| G14 | G-SCOPE | matter-channel graph census | one interaction sector determines the N=4 answer | include gauge kinetic, matter bridge, chiral cubic, and antichiral cubic sectors in every typed channel census; prove every omitted sector absent | P1 | OPEN |
| G15 | G-NORM | renormalized DRED operator basis | the finite remainder is scheme-independent without further data | fix the evanescent-operator basis, pole subtraction, finite-counterterm convention, open-color tensor-product basis, and multi-trace sector | P1 | OPEN |

## Highest-risk correction

The current WW data contain

$$
30\ I_{(3)}
+6\ \widetilde S_{(3)}
+180\ I_{(4)}
=216
$$

ordered port-basis terms.  They are correctly classified as
`ORDERED_PORT_BASIS_TERM_NOT_GRAPH`.  Therefore

$$
P_{\triangle}^{mn}-P_C^{mn}
=\frac{g^2}{128\pi^2\epsilon}
(\widehat\delta-\delta_{(4)})^{mn}
$$

is presently an aggregate Schwinger--Dyson identity.  It is not yet the
explicit basis-resolved statement

$$
\mathcal A_{\triangle}^{(4)}
+\mathcal A_{I_{(3)}\widetilde S_{(3)}}^{(4)}
+\mathcal A_{I_{(4)}}^{(4)}
+\mathcal A_{\rm collapsed}^{(4)}=0.
$$

Hence the \(g^2/(64\pi^2)\) WW coefficient is a derived aggregate-SD candidate,
not an accepted full Ward-identity coefficient.

The (16) aggregate metric contacts and the explicit
(I_{(3)}S_{(3)}), (I_{(2)}S_{(4)}), (I_{(4)}) families are not independent
summands until G13 is closed.  A collapsed/cut representative may encode the
same SD descendant as an explicit bubble.  Adding both bases without a
bijection would double count the contact orbit.

## Repair order

1. Choose one canonical WW contact basis and prove its bijection with every collapsed/cut representative.
2. Physicalize the WW \(I_{(3)}\widetilde S_{(3)}\), \(I_{(2)}S_{(4)}\), \(I_{(4)}\), and collapsed families.
3. Prove the complete ordinary triangle--bubble/contact equality and the ordered \(R_\epsilon,C_{\rm SD}\) commutator.
4. Compile the \(Y,Z\) letter expansions, bind the existing \(\widetilde W_{(n)}\) recursion to \(T\), and expose the chiral edge kernels.
5. Enumerate the eleven remaining nonzero families and close the renormalized zero-family argument.
6. Fix the external probes, evanescent/multi-trace scheme, and channelwise FP/NK census.

## Verification checks

### V1. Spin frame

Equations (5.1)--(5.3) already fix

$$
+\equiv1,
\qquad
-\equiv2,
\qquad
\epsilon^{+-}=1,
\qquad
\nabla^2=2\nabla_-\nabla_+.
$$

No spin-frame definition gap remains.

### V2. Tree hierarchy

The existing emitter gives exactly

$$
dX=-\nabla_+\mathcal G
-2i\nabla_+(\Phi_s\times Z_s),
$$

$$
dY_r=\frac12\widetilde{\mathcal C}_r
-\sqrt2\epsilon_{rst}(Z_s\times Z_t),
\qquad
dZ_r=dT_{\dot a}=0.
$$

The ordered Leibniz rule emits \(16\) families, \(32\) family terms, and four
exact tree-zero families.

### V2a. Universal letter-valence hierarchy

For any ordered pair \(O_{UV}=UV\), write

$$
U=\sum_{n\geq1}U_{(n)},
\qquad
V=\sum_{n\geq1}V_{(n)},
\qquad
O_{UV,(N)}=\sum_{r+s=N}U_{(r)}V_{(s)}.
$$

Therefore

$$
\begin{aligned}
O_{UV,(2)}&=U_{(1)}V_{(1)},\\
O_{UV,(3)}&=U_{(2)}V_{(1)}+U_{(1)}V_{(2)},\\
O_{UV,(4)}&=U_{(3)}V_{(1)}+U_{(2)}V_{(2)}+U_{(1)}V_{(3)}.
\end{aligned}
$$

Define the odd connection action on the ordered product by

$$
\Gamma_-\boldsymbol\cdot(UV)
:=[\Gamma_-,U]V+(-1)^{|U|}U[\Gamma_-,V].
$$

Then the complete insertion hierarchy through quartic valence is

$$
\begin{aligned}
I_{UV,(2)}&=D_-O_{UV,(2)},\\
I_{UV,(3)}&=D_-O_{UV,(3)}
+\Gamma_{-,(1)}\boldsymbol\cdot O_{UV,(2)},\\
I_{UV,(4)}&=D_-O_{UV,(4)}
+\Gamma_{-,(1)}\boldsymbol\cdot O_{UV,(3)}
+\Gamma_{-,(2)}\boldsymbol\cdot O_{UV,(2)}.
\end{aligned}
$$

This identity fixes the required hierarchy but not the missing Project
coefficients of \(Y_{(n)},Z_{(n)}\) or their channel compiler.  The
\(\widetilde W_{(n)}\) recursion already exists and must be bound to the
\(T_{(n)}\) letter interface.

### V2b. Maximal one-loop insertion valence

Let one insertion have valence \(n_I\), let \(N\) interaction vertices have
valences \(n_a\), let the connected graph have two external legs, \(E\)
internal edges, and one loop.  Half-edge counting and the Euler relation give

$$
n_I+\sum_{a=1}^{N}n_a=2E+2,
\qquad
1=E-(N+1)+1,
\qquad
E=N+1.
$$

Hence

$$
\boxed{
(n_I-2)+\sum_{a=1}^{N}(n_a-2)=2.}
$$

For genuine interaction vertices \(n_a\geq3\), the complete solutions are

$$
\begin{array}{c|c|c}
N&\text{valences}&\text{graph family}\\ \hline
2&(n_I,n_1,n_2)=(2,3,3)&I_{(2)}S_{(3)}S_{(3)}\\
1&(n_I,n_1)=(3,3)&I_{(3)}S_{(3)}\\
1&(n_I,n_1)=(2,4)&I_{(2)}S_{(4)}\\
0&n_I=4&I_{(4)}
\end{array}
$$

Therefore no primitive one-loop two-external graph contains \(I_{(n)}\) with
\(n\geq5\).  Quadratic counterterm insertions are a separate renormalization
sector.

### V2c. Aggregate Schwinger--Dyson cancellation

For every bosonic quantum coordinate \(q^i\),

$$
0=\int Dq\,
\frac{\vec\partial}{\partial q^i}
\left[A^i(q)e^{-S(q)/\hbar}\right]
=\left\langle\frac{\vec\partial A^i}{\partial q^i}\right\rangle
-\frac1\hbar
\left\langle A^i\frac{\vec\partial S}{\partial q^i}\right\rangle.
$$

With

$$
\frac{\vec\partial S}{\partial q^i}
=K_{ij}q^j
+\frac12S_{ijk}q^jq^k
+\frac1{3!}S_{ijkl}q^jq^kq^l+\cdots,
$$

the contraction

$$
K_{ij}G^{jk}=\delta_i{}^k
$$

cuts one parent edge.  The \(S_{ijk}\), \(S_{ijkl}\), and

$$
\frac{\vec\partial A^i}{\partial q^i}
$$

terms generate respectively the bubble, quartic, and insertion-contact
families.  This proves the aggregate cancellation theorem.  G1 remains open
because its graph-by-graph expansion and exact multiplicities have not been
evaluated.

### V2d. Bare all-valence zero channels

Covariant antichirality holds order by order:

$$
0=(\nabla_-Z_r)_{(n)}
=D_-Z_{r,(n)}
+\sum_{a+b=n}[\Gamma_{-,(a)},Z_{r,(b)}],
$$

$$
0=(\nabla_-T_{\dot\alpha})_{(n)}
=D_-T_{\dot\alpha,(n)}
+\sum_{a+b=n}[\Gamma_{-,(a)},T_{\dot\alpha,(b)}].
$$

Therefore, for every total valence \(N\),

$$
I_{ZT,(N)}^{AB}
=\sum_{a+b=N}
\left[
(\nabla_-Z_r)_{(a)}^AT_{\dot\beta,(b)}^B
+Z_{r,(a)}^A(\nabla_-T_{\dot\beta})_{(b)}^B
\right]
=0.
$$

The same calculation gives

$$
I_{ZZ,(N)}=I_{ZT,(N)}=I_{TZ,(N)}=I_{TT,(N)}=0.
$$

Thus the four bare insertion families generate no parent graph at any valence.
G9 is the remaining renormalized-mixing statement, not a bare-operator gap.

### V3. WW row normalization

$$
(-2g^2)^3
\left(-\frac{ih}{8}\right)
\left(\frac{ih}{8}\right)
=-\frac{g^2}{8},
$$

$$
\frac1{128}\,16\,(2i)(2i)=-\frac12,
$$

$$
\left(-\frac{g^2}{8}\right)
\left(-\frac12\right)=\frac{g^2}{16}.
$$

The normalization audit passes; G1 concerns the unexpanded contact orbit, not
the Project seed normalization.
