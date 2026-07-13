# Step 5A primitive two-background Hessian-family audit

## 1. Definitions

$$
\mathscr I^{AB}=\nabla_-\!\left(X^A X^B\right),
\qquad X^A=(\nabla_+W_+)^A,
\qquad |X|=0,
\qquad |\mathscr I|=|J|=1.
$$

$$
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}\!\left[
+G_0I_0G_0H_1G_0H_1
-G_0I_0G_0H_2
-G_0I_1G_0H_1
+G_0I_2
\right]+\mathrm{CT}_2.
$$

## 2. Exact Project branch counts

$$
\begin{array}{c|ccc}
\text{source block}&I_0&I_1&I_2\\ \hline
\#\text{ ordered branches}&4&60&720
\end{array}
$$

$$
N(I_0)=2\binom20(0!)\,(2!)=4,
$$

$$
N(I_1)=10\binom31(1!)\,(2!)=60,
$$

$$
N(I_2)=30\binom42(2!)\,(2!)=720.
$$

The integers 2, 10, and 30 are the exact Project composite-term counts

$$
|I_{(2)}|=2,
\qquad |I_{(3)}|=10,
\qquad |I_{(4)}|=30.
$$

The split is

$$
V_j=(V_{\mathrm B})_j+v_j.
$$

It changes no source coefficient.  Each ordered background/quantum assignment
has multiplicity one; the final factor of two enumerates the ordered bosonic
Hessian row/column occurrences.  No factorial is divided a second time.

$$
\begin{array}{c|cc}
\text{action block}&H_1&H_2\\ \hline
V\to V&24&144\\
\Phi_r\leftrightarrow\widetilde\Phi_r\ \text{for each }r&2&4\\
\mathrm{FP}\to\mathrm{FP}&\texttt{BLOCKED}&\texttt{BLOCKED}\\
\mathrm{NK}\to\mathrm{NK}&\texttt{BLOCKED}&\texttt{BLOCKED}
\end{array}
$$

$$
N(H_1^{VV})=4\binom31(1!)\,(2!)=24,
\qquad
N(H_2^{VV})=6\binom42(2!)\,(2!)=144.
$$

The factors 4 and 6 count the Project cubic and quartic gauge-action
monomials.  The action-monomial coefficient, derivative scope, and color word
remain attached to every branch.

The explicit FP vertices contain quantum prepotentials,

$$
N(Vc'c)=4,
\qquad
N(V^2c'c)=4.
$$

They are retained as `QUANTUM_INTERACTION_NOT_BACKGROUND_HESSIAN`.  The
background dependence lies in the unexpanded
$\bar\nabla_{\mathrm B}^{2}$ and $\nabla_{\mathrm B}^{2}$ operators;
hence the FP entries of $H_1$ and $H_2$ are
`BLOCKED_MISSING_PROJECT_BLOCK`.  The NK background Hessians have the same
status.

## 3. Surviving bare vector families

$$
\begin{array}{c|c|c|c|c}
\text{word}&\text{polarizations}&\text{topology}&L&\#\text{ branch paths}\\ \hline
+I_0H_1H_1&2&\triangle&1&2\cdot2304\\
-I_0H_2&1&\text{seagull bubble}&1&576\\
-I_1H_1&2&\text{insertion-contact bubble}&1&2\cdot1440\\
+I_2&1&\text{double-contact tadpole}&1&720\\
\mathrm{CT}_2&1&\text{local}&0&\text{coefficient blocked}
\end{array}
$$

$$
2(2304)+576+2(1440)+720=8784.
$$

The three different census levels are

$$
N_{\mathrm{typed\ block\ paths}}
=6^3+6^2+6^2+6
=216+36+36+6
=294,
$$

$$
N_{\mathrm{ordered\ vector\ branch\ paths}}=8784,
\qquad
N_{\mathrm{GraphIR}}=6+1_{\mathrm{CT}_2}=7.
$$

Neither 294 nor 8784 is a graph count.

Every bare non-vector path vanishes at its source block.  A source-completed
non-vector diagonal path remains `BLOCKED_MISSING_PROJECT_BLOCK`; it is not
promoted to a zero.

## 4. Typed repair readback

$$
|W_+|=1,
\qquad |\nabla_+|=1,
\qquad |X|=1+1=0,
$$

$$
|X^AX^B|=0,
\qquad |\nabla_-|=1,
\qquad |\mathscr I|=1,
\qquad |J|=1.
$$

$$
\operatorname{Statistics}(J)=\mathrm{FERMION},
\qquad
\operatorname{Var}(J_{AB})=(\mathrm{DOWN},\mathrm{DOWN}),
$$

$$
\operatorname{Var}(\widetilde W_{\dot a})=\mathrm{DOWN},
\qquad
s_{\mathrm{reflected}}=(-1)_{\mathrm{ext}}(-1)_{\mathrm{quantum}}=+1.
$$

The external covariant derivative is

$$
\mathcal D_{+\dot a}.
$$

The persisted notation, GraphIR, and reflected amplitude readbacks are
REPAIRED.

## 5. Acceptance boundary

$$
\text{triangle pole}
=\text{contact pole}
=\text{anomaly coefficient}
=\texttt{NOT ACCEPTED}.
$$
