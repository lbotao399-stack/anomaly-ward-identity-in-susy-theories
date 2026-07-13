# Step 5 one-loop pure-gauge covariant-jet census

## 0. Status

$$
\boxed{\texttt{PASS\_EXACT\_PARTIAL\_FAIL\_CLOSED}}
$$

$$
\boxed{
\dim \operatorname{Span}_{\mathrm{Spin}(4)}
\{W\widetilde W\nabla\mathcal D\}_{(3/2,0)}=1
}
$$

$$
\boxed{
\dim H^0_{\mathrm{loc}}(s\mid d)=1
\quad\text{is not proved.}
}
$$

The ordered open carrier $\mathcal C^{AB}_{\mathrm{Adj}\otimes\mathrm{Adj}}$ is not quotiented.

## 1. Typed letters

Here `r_f` is the temporary formal grading defined by this table.
The Project (U(1)_R) identification remains open.

$$
\begin{array}{c|c|c|c|c}
L&[L]&r_{\mathrm f}(L)&|L|&(j_L,j_R)\\ \hline
W_a&\frac32&+1&1&(\frac12,0)\\
\widetilde W_{\dot a}&\frac32&-1&1&(0,\frac12)\\
\nabla_a&\frac12&-1&1&(\frac12,0)\\
\bar\nabla_{\dot a}&\frac12&+1&1&(0,\frac12)\\
\mathcal D_{a\dot a}&1&0&0&(\frac12,\frac12)
\end{array}
$$

Target:

$$
[\mathcal O]=\frac92,
\qquad
r_{\mathrm f}(\mathcal O)=-1,
\qquad
|\mathcal O|=1,
\qquad
(j_L,j_R)=\left(\frac32,0\right).
$$

Set

$$
N=n_W+n_{\widetilde W}.
$$

The exact integer system is

$$
\begin{aligned}
3N+n_\nabla+n_{\bar\nabla}+2n_{\mathcal D}&=9,\\
n_W-n_{\widetilde W}-n_\nabla+n_{\bar\nabla}&=-1,\\
n_W+n_{\widetilde W}+n_\nabla+n_{\bar\nabla}&=1\pmod 2.
\end{aligned}
$$

## 2. Complete dimension-charge-parity census

Each row denotes

$$
(n_W,n_{\widetilde W};n_\nabla,n_{\bar\nabla},n_{\mathcal D}).
$$

$$
\begin{array}{c|l}
N&\text{all solutions}\\ \hline
0&(0,0;1,0,4),(0,0;2,1,3),(0,0;3,2,2),(0,0;4,3,1),(0,0;5,4,0)\\
1&(0,1;0,0,3),(0,1;1,1,2),(0,1;2,2,1),(0,1;3,3,0),\\
 & (1,0;2,0,2),(1,0;3,1,1),(1,0;4,2,0)\\
2&(0,2;0,1,1),(0,2;1,2,0),(1,1;1,0,1),(1,1;2,1,0),(2,0;3,0,0)\\
3&(1,2;0,0,0)
\end{array}
$$

$$
\boxed{
\#\mathcal S_0=5,\qquad
\#\mathcal S_1=7,\qquad
\#\mathcal S_2=5,\qquad
\#\mathcal S_3=1,\qquad
\sum_{N=0}^{3}\#\mathcal S_N=18.
}
$$

For $N\geq4$,

$$
2[\mathcal O]\geq 3N\geq12>9.
$$

Hence

$$
\boxed{N\geq4\ \text{is excluded}.}
$$

The completion theorem uses the quadratic filtration

$$
\mathcal F_{\geq2}:=\{\mathcal O:\operatorname{ord}_{W,\widetilde W}\mathcal O\geq2\}.
$$

Thus $N=0,1$ lie outside this filtered census. Their global absence is not asserted.

## 3. $N=3$

The integer system gives only

$$
W\widetilde W\widetilde W.
$$

Its left spin is

$$
j_L=\frac12.
$$

Its right decomposition is

$$
\frac12\otimes\frac12=0\oplus1.
$$

Therefore

$$
\operatorname{mult}_{(3/2,0)}
\left(W\widetilde W\widetilde W\right)=0.
$$

## 4. $N=2$: exact free ordered spin-word multiplicities

No statistics, color, IBP, EOM, or derivative commutator quotient is used in this table.

$$
\begin{array}{c|c}
\text{content}&\operatorname{mult}_{(3/2,0)}\\ \hline
WW\nabla^3&4\\
W\widetilde W\nabla^2\bar\nabla&1\\
W\widetilde W\nabla\mathcal D&1\\
\widetilde W\widetilde W\nabla\bar\nabla^2&0\\
\widetilde W\widetilde W\bar\nabla\mathcal D&0
\end{array}
$$

For $W\widetilde W\nabla\mathcal D$,

$$
\begin{aligned}
\left(\frac12\right)_L^{\otimes3}
&=\frac32\oplus2\left(\frac12\right),\\
\left(\frac12\right)_R^{\otimes2}
&=0\oplus1.
\end{aligned}
$$

Hence

$$
\boxed{
\operatorname{mult}_{(3/2,0)}
\left(W\widetilde W\nabla\mathcal D\right)=1.
}
$$

For $WW\nabla^3$,

$$
\left(\frac12\right)^{\otimes5}
=\frac52\oplus4\left(\frac32\right)\oplus5\left(\frac12\right).
$$

## 5. Mixed derivative reduction

The exact Euclidean relation is

$$
\boxed{
\{\nabla_a,\bar\nabla_{\dot c}\}
=-2\mathcal D_{a\dot c}.
}
$$

For a chiral terminal letter,

$$
\bar\nabla_{\dot c}W_d=0.
$$

Thus

$$
\begin{aligned}
\bar\nabla_{\dot c}\nabla_a\nabla_bW_d
&=-\nabla_a\bar\nabla_{\dot c}\nabla_bW_d
-2\mathcal D_{a\dot c}\nabla_bW_d\\
&=+\nabla_a\nabla_b\bar\nabla_{\dot c}W_d
+2\nabla_a\mathcal D_{b\dot c}W_d
-2\mathcal D_{a\dot c}\nabla_bW_d\\
&=2\nabla_a\mathcal D_{b\dot c}W_d
-2\mathcal D_{a\dot c}\nabla_bW_d,
\end{aligned}
$$

$$
\begin{aligned}
\nabla_a\bar\nabla_{\dot c}\nabla_bW_d
&=-\nabla_a\nabla_b\bar\nabla_{\dot c}W_d
-2\nabla_a\mathcal D_{b\dot c}W_d\\
&=-2\nabla_a\mathcal D_{b\dot c}W_d,
\end{aligned}
$$

$$
\nabla_a\nabla_b\bar\nabla_{\dot c}W_d=0.
$$

For an antichiral terminal letter,

$$
\nabla_a\widetilde W_{\dot d}=0,
$$

and

$$
\begin{aligned}
\nabla_a\nabla_b\bar\nabla_{\dot c}\widetilde W_{\dot d}
&=-\nabla_a\bar\nabla_{\dot c}\nabla_b\widetilde W_{\dot d}
-2\nabla_a\mathcal D_{b\dot c}\widetilde W_{\dot d}\\
&=-2\nabla_a\mathcal D_{b\dot c}\widetilde W_{\dot d},\\
\nabla_a\bar\nabla_{\dot c}\nabla_b\widetilde W_{\dot d}&=0,\\
\bar\nabla_{\dot c}\nabla_a\nabla_b\widetilde W_{\dot d}&=0.
\end{aligned}
$$

Therefore every local three-derivative terminal word lies in

$$
\operatorname{Span}\{\nabla\mathcal D,\mathcal D\nabla\}
+\operatorname{Span}\{\bar\nabla W,\nabla\widetilde W\}.
$$

No $\nabla$-$\mathcal D$ reordering has been performed.

For derivatives distributed across $W\widetilde W$, the complete graded Leibniz and covariant-IBP map remains open.

## 6. $WW\nabla^3$ local EOM reduction

Define

$$
E:=\nabla^aW_a.
$$

The locked identities are

$$
\nabla_a\nabla_b
=\frac12\epsilon_{ab}\nabla^2,
\qquad
\nabla_cE=-\frac12\nabla^2W_c.
$$

Hence

$$
\boxed{
\nabla_a\nabla_bW_c
=-\epsilon_{ab}\nabla_cE.
}
$$

Three labeled derivatives distributed over two field strengths give $2^3=8$ assignments. Every assignment contains a field carrying at least two derivatives.

For a $2+1$ distribution,

$$
(\nabla_a\nabla_bW_c)(\nabla_dW_e)
=-\epsilon_{ab}(\nabla_cE)(\nabla_dW_e).
$$

For a $3+0$ distribution,

$$
\begin{aligned}
(\nabla_a\nabla_b\nabla_dW_c)W_e
&=\nabla_a(\nabla_b\nabla_dW_c)W_e\\
&=-\epsilon_{bd}(\nabla_a\nabla_cE)W_e.
\end{aligned}
$$

The remaining six labeled assignments follow by changing the derivative labels and exchanging $W_1,W_2$. The generated artifact stores all eight rows.

Thus each direct derivative block belongs to the differential ideal generated by $E$.

The complete ordered product requires the exact graded Leibniz signs, covariant IBP, and the curvature children generated by derivative commutators. Consequently,

$$
\boxed{
\texttt{UNPROVED}:\qquad
WW\nabla^3=0\pmod{(E,\nabla E,\ldots)}
}
$$

is not yet certified for the full ordered source insertion.

## 7. Fail-closed theorem boundary

The exact certified statements are

$$
\begin{gathered}
N\geq4:\quad 0,\\
N=3:\quad \operatorname{mult}_{(3/2,0)}=0,\\
N=2:\quad
\operatorname{mult}_{(3/2,0)}
\left(W\widetilde W\nabla\mathcal D\right)=1,\\
\nabla^2\bar\nabla:\quad
\operatorname{Span}\{\nabla\mathcal D,\mathcal D\nabla\}
+\text{chirality ideal},\\
WW\nabla^3:\quad
\text{direct terminal blocks lie in the differential }E\text{-ideal}.
\end{gathered}
$$

The unresolved quotient is

$$
\frac{
\mathcal F_{\geq2}^{[9/2],r_{\mathrm f}=-1,(3/2,0),\mathrm{odd}}
\otimes\mathcal C^{AB}_{\mathrm{Adj}\otimes\mathrm{Adj}}
}{
\mathcal I_{\mathrm{Leibniz}}
+\mathcal I_{\mathrm{IBP}}
+\mathcal I_{[\nabla,\mathcal D]}
+\mathcal I_{\mathrm{color}}
+\mathcal I_{\mathrm{evanescent}}
+\mathcal I_{\mathrm{source/BRST}}
}.
$$

Therefore

$$
\boxed{
\operatorname{mult}_{\mathrm{spin}}=1
\centernot\Longrightarrow
\dim H^0_{\mathrm{loc}}(s\mid d)=1.
}
$$

$$
\boxed{
\texttt{OPEN}:\qquad
r_{\mathrm f}\longleftrightarrow U(1)_R^{\rm Project}.}
$$
