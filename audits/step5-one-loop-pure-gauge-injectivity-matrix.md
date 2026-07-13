# Step 5 pure-gauge fixed-quadratic-jet injectivity matrix

## 0. Typed target

$$
[\mathscr O]=\frac92,
\qquad
(j_L,j_R)=\left(\frac32,0\right),
\qquad
|\mathscr O|=1,
\qquad
r_\mathrm f(\mathscr O)=-1.
$$

Here $r_\mathrm f$ is only the formal letter grading.  The physical Project
$U(1)_R$ binding is not used.

$$
\{\nabla_a,\bar\nabla_{\dot b}\}
=-2\mathcal D_{a\dot b},
$$

$$
[\nabla_a,\mathcal D_{b\dot b}]
=-2\epsilon_{ab}\widetilde{\mathcal W}_{\dot b},
\qquad
[\bar\nabla_{\dot a},\mathcal D_{b\dot b}]
=-2\epsilon_{\dot a\dot b}\mathcal W_b.
$$

## 1. Degree zero

$$
\nabla_{\mathfrak A}1
=\partial_{\mathfrak A}1+[\Gamma_{\mathfrak A},1]=0.
$$

The target basis has

$$
5\cdot8=40
$$

components.  Its identity-relation matrix has

$$
\operatorname{rank}M_0=40,
\qquad
\dim(\mathcal V_0/\operatorname{row}M_0)=0.
$$

For the elementary ordered derivatives

$$
S_k:=\int(\delta_k\cdots\delta_1J)
(\delta_{k+1}\cdots\delta_L1),
$$

$$
S_k+(-1)^{|\delta_{k+1}||J_k|}S_{k+1}=0,
\qquad
S_L=\int(\delta_L\cdots\delta_1J)1=0.
$$

The exact stepwise source-IBP chains have

$$
\operatorname{rank}M_{0,J}=320,
\qquad
\dim(\mathcal V_{0,J}/\operatorname{row}M_{0,J})=0.
$$

## 2. Degree one

$$
\nabla^2\mathcal W_a=-2\nabla_a\mathcal E,
\qquad
\mathcal E:=\nabla^b\mathcal W_b,
$$

$$
\mathcal D_a{}^{\dot a}\widetilde{\mathcal W}_{\dot a}
=-\frac12\nabla_a
\left(\bar\nabla^{\dot a}
\widetilde{\mathcal W}_{\dot a}\right).
$$

The seven skeletons contain

$$
2+2+2+2+4+4+4
=20
$$

target-spin components.  With one EOM carrier per component,

$$
\operatorname{rank}M_1
=40,
\qquad
\dim(\mathcal V_1/\operatorname{row}M_1)=0.
$$

Normal ordering covers

$$
N_{\rm words}=104
$$

distinct derivative words.  Every $[\nabla,\mathcal D]$ or
$[\bar\nabla,\mathcal D]$ child is stored with filtration tag
$N\geq2$.

### 2.1 Indexed child matrix

$$
P_j=\prod_{j'\ne j}
\frac{C_2-j'(j'+1)\mathbf1}
{j(j+1)-j'(j'+1)}.
$$

For all labeled $[\nabla,\mathcal D]$ and
$[\bar\nabla,\mathcal D]$ events,

$$
N_{\rm input}=1626,
\qquad
N_{\rm event}=21600,
\qquad
N_{\rm branch}=53412.
$$

$$
M_{ND,BD}\in
\operatorname{Mat}_{126\times4864}(\mathbb Q),
\qquad
\operatorname{rank}M_{ND,BD}=126,
\qquad
\dim\ker M_{ND,BD}=4738.
$$

$$
M_{ND,BD}^{\rm full}\in
\operatorname{Mat}_{504\times19456}(\mathbb Q),
\qquad
\operatorname{rank}M_{ND,BD}^{\rm full}=504,
\qquad
\dim\ker M_{ND,BD}^{\rm full}=18952.
$$

$$
\rho_E=1,
\qquad
[\mathcal D_{a\dot a},\mathcal D_{b\dot b}]
=\epsilon_{\dot a\dot b}\nabla_{(a}\mathcal W_{b)}
+\epsilon_{ab}\bar\nabla_{(\dot a}
\widetilde{\mathcal W}_{\dot b)}.
$$

The eight symmetrization/endpoint branches give

$$
M_{DD}^{\rm hw}
=\begin{pmatrix}0&1\\0&-1\end{pmatrix},
\qquad
\operatorname{rank}M_{DD}^{\rm hw}=1,
\qquad
\ker M_{DD}^{\rm hw}
=\operatorname{span}_\mathbb Q
\left\{\begin{pmatrix}1\\0\end{pmatrix}\right\}.
$$

$$
M_{DD}^{\rm full}\in
\operatorname{Mat}_{8\times8}(\mathbb Q),
\qquad
\operatorname{rank}M_{DD}^{\rm full}=4,
\qquad
\dim\ker M_{DD}^{\rm full}=4.
$$

This kernel belongs only to the local $[\mathcal D,\mathcal D]$ child map.
For the complete indexed child map,

$$
M_{1\to2}=\begin{pmatrix}M_{ND,BD}&M_{DD}\end{pmatrix}
\in\operatorname{Mat}_{126\times4866}(\mathbb Q),
$$

$$
\operatorname{rank}M_{1\to2}=126,
\qquad
\dim\ker M_{1\to2}=4740,
$$

$$
M_{1\to2}^{\rm full}
\in\operatorname{Mat}_{504\times19464}(\mathbb Q),
\qquad
\operatorname{rank}M_{1\to2}^{\rm full}=504,
\qquad
\dim\ker M_{1\to2}^{\rm full}=18960.
$$

Thus

$$
\operatorname{im}M_{1\to2}=\mathcal V_2^{\rm indexed},
\qquad
\ker M_{1\to2}\ne0.
$$

This is exact target coverage; it is not filtered-quotient injectivity.

## 3. Degree two

$$
\begin{array}{c|ccccc}
&WW\nabla^3&W\widetilde W\nabla^2\bar\nabla
&W\widetilde W\nabla\mathcal D
&\widetilde W^2\nabla\bar\nabla^2
&\widetilde W^2\bar\nabla\mathcal D\\ \hline
\operatorname{mult}_{(3/2,0)}&4&1&1&0&0
\end{array}
$$

### 3.1 $WW\nabla^3$

The weight-$m_L=3/2$ projector is

$$
P_{3/2}=I_5-\frac15\mathbf1\mathbf1^T,
\qquad
P_{3/2}^2=P_{3/2},
\qquad
\operatorname{rank}P_{3/2}=4.
$$

The $2^3=8$ graded-Leibniz placements obey

$$
\nabla_a\nabla_b\mathcal W_c
=-\epsilon_{ab}\nabla_c\mathcal E.
$$

For four spin copies the placement-plus-EOM matrix has

$$
\operatorname{rank}M_{WW}=
64,
\qquad
\dim(\mathcal V_{WW}/\operatorname{row}M_{WW})=0.
$$

### 3.2 $W\widetilde W\nabla^2\bar\nabla$

For the ordered word $\nabla_a\nabla_b\bar\nabla_{\dot c}$,
the eight placements reduce to

$$
\begin{aligned}
M_4&=-E,\\
M_5&=2C_{ba},\\
M_6&=-2C_{ab},\\
M_7&=-4H_{W\widetilde W^2},
\end{aligned}
$$

with $M_0=M_1=M_2=M_3=0$.  Since

$$
P_{\rm sym}
=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
P_{\rm sym}
\begin{pmatrix}2\\-2\end{pmatrix}
=\begin{pmatrix}0\\0\end{pmatrix},
$$

the target-spin projection contains only EOM and the $N=3$ child.

### 3.3 $W\widetilde W\nabla\mathcal D$

For $\nabla_a\mathcal D_{b\dot b}(W\widetilde W)$,

$$
\begin{array}{c|ccc}
&C_{W}&C_{\rm split}&H_{W\widetilde W^2}\\ \hline
P_0&1&0&-2\\
P_1&0&0&0\\
P_2&0&1&0\\
P_3&0&0&2
\end{array}.
$$

Thus

$$
\sum_{i=0}^3P_i=C_W+C_{\rm split},
\qquad
-2H_{W\widetilde W^2}+2H_{W\widetilde W^2}=0.
$$

IBP alone gives

$$
C_W+C_{\rm split}=0,
\qquad
\dim\mathcal Q_{\rm IBP,const}=1,
$$

For a local source,

$$
C_W+C_{\rm split}+S_{\mathcal D J}=0,
\qquad
\dim\mathcal Q_{\rm IBP,local}=2.
$$

The antichiral EOM gives

$$
C_{\rm split}
=\mathcal D_a{}^{\dot a}
\widetilde{\mathcal W}_{\dot a}
=-\frac12\nabla_a\bar{\mathcal E}=0.
$$

Hence

$$
\dim\mathcal Q_{\rm EOM+IBP,const}=0,
\qquad
\dim\mathcal Q_{\rm EOM+IBP,local}=1,
$$

$$
S_{\mathcal D J}=-C_W.
$$

Let the source-color tensor remain free:

$$
\mathscr C_K
=J_{AB}K^{AB}{}_{CD}
\widetilde{\mathcal W}^C_{\dot a}
\mathcal D_+{}^{\dot a}
\nabla_+\mathcal W_+^D.
$$

Its complete ordered quadratic jet is

$$
\ell_2[\mathscr C_K]
=
\begin{pmatrix}1\\-1\end{pmatrix}
\otimes K^{AB}{}_{CD},
$$

$$
\operatorname{rank}\ell_2=1,
\qquad
\dim\ker\ell_2=0
$$

over the free symbolic tensor module.  No scalar rank-one color claim is made.

Let $M$ be any quotient module of the source-color tensor module.  Define

$$
\iota_M:M\longrightarrow M\oplus M,
\qquad
\iota_M(m)=(m,-m),
$$

$$
\pi_1:M\oplus M\longrightarrow M,
\qquad
\pi_1(x,y)=x.
$$

Then

$$
\pi_1\circ\iota_M=\operatorname{id}_M,
\qquad
\ker\iota_M=0.
$$

Hence the same color quotient on the source and both ordered output copies
does not create a kernel.

## 4. Higher degree

$$
N=3:\quad W\widetilde W^2,
\qquad
\operatorname{mult}_{(3/2,0)}=
0.
$$

$$
N\geq4:\quad 2[\mathscr O]\geq3N\geq12>9.
$$

## 5. Filtered assembly

$$
\dim\mathcal V_0=40,
\qquad
\dim\mathcal V_1=20,
\qquad
\dim\mathcal V_2^{\rm indexed}=126,
\qquad
\dim\mathcal V_3=0.
$$

The existing canonical degree-two blocks contain

$$
4\cdot8+1\cdot8+1\cdot4=44
$$

placement coordinates.  Therefore the following exact incidence maps remain
unconstructed:

$$
C_1\in\operatorname{Mat}_{4866\times20}(\mathbb Q),
\qquad
R_2^{\rm indexed}:\mathcal V_2^{\rm indexed}
\longrightarrow\mathcal R_{\rm EOM/IBP/N3}.
$$

The exact $C_1$ basis sizes are

$$
\begin{array}{c|rrrrrrr}
\text{skeleton}
&T D^3&TN\bar N D^2&TN^2\bar N^2D&TN^3\bar N^3
&WN^2D^2&WN^3\bar N D&WN^4\bar N^2\\ \hline
\dim\mathcal V_1^{\rm abstract}&2&2&2&2&4&4&4\\
N_{\rm ordered\ records}&1&20&116&684&20&114&672\\
\dim\mathcal V_1^{\rm indexed}&2&40&232&1368&80&456&2688
\end{array}.
$$

$$
2+2+2+2+4+4+4=20,
$$

$$
2+40+232+1368+80+456+2688=4866.
$$

The $126$ columns of $R_2^{\rm indexed}$ are

$$
\left\{(p,\mu):
p\in\mathcal P_2^{\rm ordered},
\ 1\leq\mu\leq
\operatorname{mult}_{(3/2,0)}(p)}\right\},
$$

$$
|\mathcal P_2^{\rm ordered}|=83,
\qquad
\sum_{p\in\mathcal P_2^{\rm ordered}}
\operatorname{mult}_{(3/2,0)}(p)=126.
$$

For the local source basis $e_{x,y}$, where $x$ is the $\nabla$ endpoint
and $y$ is the $\mathcal D$ endpoint,

$$
e_{J,y}-e_{F_1,y}+e_{F_2,y}=0,
\qquad
y\in\{J,F_1,F_2\},
$$

$$
e_{x,J}+e_{x,F_1}+e_{x,F_2}=0,
\qquad
x\in\{J,F_1,F_2\}.
$$

Together with

$$
C_{\rm split}=0,
\qquad
S_{\mathcal D J}=-C_W,
\qquad
p=p_1+p_2.
$$

The event ledger contains curvature-child summands but not the terminal
normal-order, indexed EOM/source, or quadratic-boundary rows.  It therefore
does not define $C_1$ or $R_2^{\rm indexed}$.

The minimal missing Project type data are

$$
\boxed{
\texttt{STEP5\_SOURCE\_BRST\_COMPLEX},
\qquad
\texttt{STEP5\_ELL2\_CODOMAIN\_BOUNDARIES}.
}
$$

No additional local spinor-algebra identity is required after these types are
fixed.

Thus

$$
M_{\rm filtered}=
M_{N0\oplus N1\oplus N2\oplus N3}
\quad\text{is not assembled},
$$

$$
\dim\ker\left(
\ell_2:\mathcal V/\operatorname{row}M_{\rm filtered}
\longrightarrow\mathcal J_2
\right)
\quad\text{is not computed}.
$$

## 6. Fail-closed verdict

The missing exact matrices are

$$
\boxed{
\begin{gathered}
\mathsf{M_FILTERED_N0_N1_N2_N3_TOTAL},
\mathsf{M_SOURCE_BRST_COMPLETE},
\mathsf{M_DRED_EVANESCENT_JETS}.
\end{gathered}
}
$$

Hence

$$
\boxed{
\ker\ell_2=0
\quad\text{is not certified for the full Project quotient.}
}
$$

$$
\boxed{
\texttt{PASS\_EXACT\_LOCAL\_FAIL\_CLOSED\_GLOBAL}
\qquad
56/56.
}
$$
