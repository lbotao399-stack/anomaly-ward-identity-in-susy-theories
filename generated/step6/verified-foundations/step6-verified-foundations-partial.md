# Step 6 — verified foundations: partial mirror

$$
\mathrm{DocumentStatus}=\texttt{UNMERGED\_PROPOSAL}.
$$

## 1. Notation

$$
I_m:=\text{insertion of total valence }m,
\qquad
S_r:=\text{action vertex of valence }r,
\qquad
n_r:=N(S_r).
$$

$$
n_I:=\text{insertion valence},
\qquad
N_{\mathrm{int}}:=\text{number of internal edges},
\qquad
E:=2,
\qquad
V:=1+\sum_{r\geq3}n_r.
$$

$$
K:=\text{UV-pole projector},
\qquad
R'(G):=\Phi(G)+\sum_{\gamma\subsetneq G}C(\gamma)\Phi(G/\gamma),
\qquad
L_P:=\log\frac{4\pi\mu^2}{(p_1+p_2)^2}-\gamma_E.
$$

$$
\Phi(G):=\text{bare amplitude of }G,
\qquad
C(\gamma):=\text{local counterterm of }\gamma,
\qquad
w_j:=\frac{\text{signed decorated occurrence}}{|\operatorname{Aut}G_j|}.
$$

$$
m:=|\mathcal W_D|,
\qquad
|F|\in\{0,1\}:=\text{payload parity},
\qquad
N_{\mathrm{coeff}}:=\text{odd-coefficient crossings},
\qquad
N_{\mathrm{endpoint}}:=\text{endpoint transfers}.
$$

## 2. Two-loop valence closure

$$
n_I+\sum_{r\geq3}rn_r=2N_{\mathrm{int}}+E
=2N_{\mathrm{int}}+2.
$$

$$
L=N_{\mathrm{int}}-V+1=2
\quad\Longrightarrow\quad
N_{\mathrm{int}}=2+\sum_{r\geq3}n_r.
$$

$$
n_I+\sum_{r\geq3}rn_r
=2\left(2+\sum_{r\geq3}n_r\right)+2
\quad\Longrightarrow\quad
\boxed{(n_I-2)+\sum_{r\geq3}(r-2)n_r=4}.
$$

$$
\mathcal F_{L=2}=\left\{I_2S_3^4,\;I_2S_3^2S_4,\;I_2S_3S_5,\;I_2S_4^2,\;I_2S_6,\;I_3S_3^3,\;I_3S_3S_4,\;I_3S_5,\;I_4S_3^2,\;I_4S_4,\;I_5S_3,\;I_6\right\},
\qquad
|\mathcal F_{L=2}|=12.
$$

$$
\forall F\in\mathcal F_{L=2}:\qquad
F=\texttt{VALENCE\_NOT\_GRAPH},
\qquad
F\notin\mathrm{GraphIR}.
$$

$$
F=\texttt{VALENCE\_NOT\_GRAPH}
\quad\not\Longrightarrow\quad
N_{\mathrm{instantiated\ GraphIR}}(F)=0.
$$

## 3. Background-labelled K4-e parents

$$
\begin{aligned}
G_{1}&=\texttt{G6\_DIRECT\_K4ME\_I2\_S3SQ\_S4},&(H_1,H_2)&=(A,C),&|\operatorname{Aut}G_{1}|&=1,&w_{1}&=-1 \\
G_{2}&=\texttt{G6\_DIRECT\_K4ME\_I2\_S3SQ\_S4\_P1S4\_P2S3},&(H_1,H_2)&=(C,A),&|\operatorname{Aut}G_{2}|&=1,&w_{2}&=-1 \\
G_{3}&=\texttt{G6\_DIRECT\_K4ME\_I2\_S3SQ\_S4\_B2\_ON\_S4},&(H_1,H_2)&=(C,C),&|\operatorname{Aut}G_{3}|&=2,&w_{3}&=-\frac{1}{2} \\
G_{4}&=\texttt{G6\_DIRECT\_K4ME\_I3\_S3CUBED},&(H_1,H_2)&=(A,B),&|\operatorname{Aut}G_{4}|&=1,&w_{4}&=-1 \\
G_{5}&=\texttt{G6\_DIRECT\_K4ME\_I3\_S3CUBED\_P1S3\_P2I},&(H_1,H_2)&=(A,I),&|\operatorname{Aut}G_{5}|&=2,&w_{5}&=-\frac{1}{2} \\
G_{6}&=\texttt{G6\_DIRECT\_K4ME\_I3\_S3CUBED\_P1I\_P2S3},&(H_1,H_2)&=(I,A),&|\operatorname{Aut}G_{6}|&=2,&w_{6}&=-\frac{1}{2}
\end{aligned}
$$

$$
N_{K_4-e}=6,
\qquad
(w_1,w_2,w_3,w_4,w_5,w_6)=\left(-1,-1,-\frac12,-1,-\frac12,-\frac12\right).
$$

## 4. Restricted-three evaluator; six-parent boundary

$$
\mathcal U_6:=\bigoplus_{j=1}^6\mathfrak A(G_j),
\qquad
N_{\mathrm{structural}}=3,
\qquad
N_{\mathrm{fail\mbox{-}closed}}=3,
\qquad
N_{\mathrm{bounded\ materialized}}=3.
$$

$$
\mathcal U_{\mathrm{old}}=\left\{\texttt{G6\_DIRECT\_K4ME\_I2\_S3SQ\_S4},\;\texttt{G6\_DIRECT\_K4ME\_I2\_S3SQ\_S4\_B2\_ON\_S4},\;\texttt{G6\_DIRECT\_K4ME\_I3\_S3CUBED}\right\},
\qquad
\mathcal U_{\mathrm{new}}=\left\{\texttt{G6\_DIRECT\_K4ME\_I2\_S3SQ\_S4\_P1S4\_P2S3},\;\texttt{G6\_DIRECT\_K4ME\_I3\_S3CUBED\_P1S3\_P2I},\;\texttt{G6\_DIRECT\_K4ME\_I3\_S3CUBED\_P1I\_P2S3}\right\}.
$$

$$
\mathrm{Parents}_{\mathrm{evaluated}}=\frac36,
\qquad
\mathrm{Sectors}_{\mathrm{completed}}=\frac{40}{40},
\qquad
\mathrm{Status}_{\mathrm{restricted\ three}}
=\texttt{PASS\_SECTOR\_SHARDED\_RESTRICTED\_THREE\_EVALUATION}.
$$

$$
N_{\mathrm{input\ sparse\ rows}}=351\,069,
\qquad
N_{\mathrm{output\ sparse\ rows}}=55\,518,
\qquad
N_{\mathrm{output\ terms}}=350\,945.
$$

$$
\mathrm{GlobalDAGRegistryConstructed}=\texttt{FALSE},
\qquad
\mathrm{PolyExteriorSemanticExpansion}=\texttt{NOT\_RUN}.
$$

$$
\mathrm{RestrictedThreeResult}
\not\Longrightarrow
\mathrm{Full}\;K_4-e,
\qquad
\mathrm{RestrictedThreeResult}
\not\Longrightarrow
Q_2(bb).
$$

$$
\mathrm{SixParentSemanticUnion}
=\texttt{OPEN: FAIL\_CLOSED\_NEW3\_DALGEBRA\_OPEN\_AXIS\_EVALUATOR\_ABSENT}.
$$

## 5. Direct B2 overall-K certificate

$$
G_{B_2}=\texttt{G6\_DIRECT\_K4ME\_I2\_S3SQ\_S4\_B2\_ON\_S4},
\qquad
P+p_1+p_2=0,
\qquad
P=-p_1-p_2.
$$

$$
K R'(G_{B_2})
\in
\bigl(\mathrm{source}_{Q(i)}A_0^2h^3\bigr)
\left[
\epsilon^{-2}\mathcal M_{-2,0}
+\epsilon^{-1}L_P\mathcal M_{-1,1}
+\epsilon^{-1}\mathcal M_{-1,0}
\right].
$$

$$
N(\mathcal M_{-2,0})=3\,035\,883,
\qquad
N(\mathcal M_{-1,1})=0,
\qquad
N(\mathcal M_{-1,0})=5\,334\,947.
$$

$$
\boxed{\left[K R'(G_{B_2})\right]_{\epsilon^{-1}L_P}=0}.
$$

$$
N_{\mathrm{source\ rows}}=483\,685,
\quad
N_{\mathrm{forest\ events}}=1\,206\,389,
\quad
N_{\mathrm{forest\ templates}}=320\,327,
\quad
N_{\mathrm{overall\mbox{-}K\ templates}}=583.
$$

## 6. Full gate census

$$
N_V=273,
\qquad
N_{V,\mathrm{self\mbox{-}loop}}=178,
\qquad
N_{V\setminus K_4-e}=267,
\qquad
N_{\mathrm{FP}}=10,
\qquad
N_{\mathrm{matter}}=12.
$$

$$
\left.\mathrm{NK}\right|_{\mathrm{reference\mbox{-}flat\ fixed\ gauge}}
=\texttt{PROVED\_ABSENT\_AT\_THIS\_ORDER},
\qquad
\mathrm{FullVector+FP+MatterCompletion}=\texttt{OPEN}.
$$

## 7. Measure-tagged convolution

$$
N_{\Delta/\mathrm{order}}=256,
\qquad
N_{\mathrm{raw\ histories}}=216,
\qquad
N_{\mathrm{source\ rows}}=6,
\qquad
N_{\mathrm{unaggregated\ pairs}}=768.
$$

$$
\mathrm{PreAggregationRawReplaySeedWithBareDeltaIdentity}
=\texttt{RESOLVED: PASS\_EXACT\_REPLAY\_SEED}.
$$

$$
\mathrm{MeasureTaggedDeltaConvolutionBeforeContactAggregation}
=\texttt{OPEN: MISSING\_TYPE}.
$$

## 8. Primitive-contact provenance

$$
N_{\mathrm{stored\ contacts}}=608,
\qquad
N_{\mathrm{complete\ pre\mbox{-}distribution\ provenance}}=0,
\qquad
N_{\mathrm{unaggregated\ pairs}}=768.
$$

$$
\mathrm{ProvenanceMap}_{768\to608}=\texttt{FAIL\_CLOSED},
\qquad
\mathrm{MeasureTaggedDeltaConvolutionBeforeContactAggregation}
=\texttt{OPEN: MISSING\_TYPE}.
$$

## 9. Odd-word transfer sign

$$
N=m+\binom{m}{2}+m|F|+N_{\mathrm{coeff}}+N_{\mathrm{endpoint}},
\qquad
\boxed{s=(-1)^N}.
$$

$$
|F|\in\{0,1\},
\qquad
0\leq m\leq6,
\qquad
N_{\mathrm{exhaustive}}=10\,922,
\qquad
\mathrm{Status}=\texttt{PASS}.
$$

$$
|F|\in\{0,1\},
\qquad
0\leq m\leq16,
\qquad
N_{\mathrm{boundary}}=2(17)=34.
$$

## 10. Frozen full-orbit Schwinger–Dyson snapshot

$$
\mathrm{Snapshot}=\texttt{FROZEN\_FULL\_ORBIT\_AUDIT},
\qquad
\mathrm{NewestPerCutFrontier}=\texttt{NOT\_REPRESENTED\_HERE}.
$$

$$
N_{\mathrm{oriented\ columns}}=96,
\qquad
N_{\mathrm{resolved\ physical\ coefficients}}=0,
\qquad
\dim M_C=\dim M_E=22\times134.
$$

$$
\mathrm{PhysicalSDCoefficients}=\texttt{OPEN: BLOCKED\_TYPED\_LOCAL\_AST\_CLOSURE}.
$$

$$
\begin{aligned}
\tau_{1}&=\texttt{MISSING\_TYPE::EdgeCollapsedProjectKernelNormalForm} \\
\tau_{2}&=\texttt{MISSING\_TYPE::GroupedEVIntoI2I3OrderedPortNormalForm} \\
\tau_{3}&=\texttt{MISSING\_TYPE::HigherValenceOrderedEulerOccurrenceNormalForm} \\
\tau_{4}&=\texttt{MISSING\_TYPE::InheritedContactVertexAST}
\end{aligned}
$$

## 11. Covariant descent and coefficient boundary

$$
\mathrm{AutomaticSourceMapDescent}=\texttt{OPEN},
\qquad
\mathrm{CovariantProjection}=\texttt{OPEN},
\qquad
\mathrm{Covariant}\;X\otimes X=\texttt{NOT\_INFERRED}.
$$

$$
R=\texttt{INCOMPLETE},
\qquad
\mathrm{ParentUnion}=\texttt{INCOMPLETE},
\qquad
\boxed{C_{\mathrm{AWI}}^{(2)}=\texttt{UNCOMPUTED}}.
$$
