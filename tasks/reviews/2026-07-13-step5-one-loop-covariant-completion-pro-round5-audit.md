# GPT Pro round 5 independent audit

Status: `ACCEPTED_AS_GAP_REVIEW__NO_COEFFICIENT_IMPORTED`

## 1. Physical and DRED complexes

Let

$$
q_{4d}:\mathcal C_{\rm DRED}\longrightarrow\mathcal C_{4d},
\qquad
\mathcal E_{\rm ev}:=\ker q_{4d}.
$$

The required commuting squares are

$$
q_{4d,2}\ell_2^{\rm DRED}
=\ell_2^{4d}q_{4d},
\qquad
q_{4d}d_{\rm CE}=d_{\rm CE}q_{4d}.
$$

The Project certificate already fixes the genuine projector algebra

$$
\delta_{(4)}=\widehat\delta+\widetilde\delta,
\qquad
\widehat\delta\widetilde\delta=0,
\qquad
\widetilde\delta^2=\widetilde\delta,
\qquad
\operatorname{tr}\widetilde\delta=2\epsilon,
$$

$$
\tau:=\widetilde\delta-\frac\epsilon2\delta_{(4)},
\qquad
\delta_{(4)mn}\tau^{mn}=0,
\qquad
\tau_{mn}\tau^{mn}=2\epsilon-\epsilon^2.
$$

Thus the explicit word proves

$$
0\ne\mathscr E\in
\ker\ell_2^{\rm DRED,raw}\cap\mathcal E_{\rm ev}.
$$

It does not prove

$$
[\mathscr E]_{\rm EOM/IBP/BV}\ne0.
$$

The additional renormalized gate is

$$
q_{4d}\operatorname{Loc}_{\rm UV}^{\rm DRED}
=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\quad\texttt{NOT\_PROVED},
$$

because

$$
\frac1\epsilon(\epsilon\mathscr O)=\mathscr O.
$$

## 2. Minimal physical-4d matrix certificate

Let

$$
A:P\longrightarrow T,
\qquad
R_T:U_T\longrightarrow T,
\qquad
Q_T:T\longrightarrow T_{\rm nf}.
$$

The terminal presentation must satisfy

$$
Q_TR_T=0,
\qquad
\operatorname{rank}Q_T+\operatorname{rank}R_T=\dim T,
$$

so that

$$
\ker Q_T=\operatorname{im}R_T.
$$

With closure matrix (D), exact/boundary matrix (B), and quadratic jet
(J_2), choose columns of (K) spanning

$$
\ker
\begin{pmatrix}
Q_CD\\
Q_2J_2
\end{pmatrix}.
$$

Injectivity requires an exact factorization

$$
K=BX+N_PY,
\qquad
\operatorname{im}N_P=\ker(Q_TA),
$$

or, on a genuine cohomology basis (U), an exact left inverse

$$
L(Q_2J_2U)=\mathbf1.
$$

The existing (4866) event coordinates do not define (P).  Therefore

$$
\operatorname{status}\!\left(\ker\bar\ell_2^{4d}=0\right)
=\texttt{FAIL\_CLOSED\_MISSING\_TRUE\_PARENT\_INCIDENCE}.
$$

## 3. Strongest theorem

The valid implication is

$$
\ker\bar\ell_2^{4d}=0,
\qquad
\bar\ell_2^{4d}
\left([\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}]
-C_{2,{\rm reg}}[\mathscr O_\star]\right)=0,
$$

$$
\Longrightarrow
\qquad
[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}]
=C_{2,{\rm reg}}[\mathscr O_\star],
\qquad
\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\Gamma_{\mathscr I,{\rm ren,DRED}}^{(1),{\rm reg}}.
$$

Neither premise is presently complete.  The rooted identity proves only

$$
\Gamma_{\mathscr I,\rm root}^{(1)}
=\frac12\operatorname{STr}_{\rm DRED}(G_BI_B),
\qquad
\delta_R\Gamma_{\mathscr I,\rm root}^{(1)}=0,
$$

for the registered fixed-vector Gaussian sectors.

It does not prove

$$
\Gamma_{\mathscr I,n}^{(1),{\rm nonlocal,reg}}
=C_{2,{\rm reg}}\mathscr O_{\star,n},
\qquad
\Gamma_{\mathscr I}^{(\ell)}=0\quad(\ell\ge2).
$$

## 4. Added P0 gates

$$
\begin{array}{c|c}
\text{gate}&\text{status}\\ \hline
\text{evanescent ideal stable under all relations}&\texttt{OPEN}\\
\text{subtraction descends to physical quotient}&\texttt{OPEN}\\
\text{complete six-row quadratic post-projector pole}&\texttt{OPEN}\\
\text{one source-dependent counterterm functional }\mathrm{CT}[B,J]
&\texttt{OPEN}\\
\text{full source BV--Slavnov complex}&\texttt{OPEN}\\
\text{nonexceptional UV/IR separation or }R^*&\texttt{OPEN}\\
\text{all source-coupled fluctuating sectors}&\texttt{OPEN}\\
\text{nonlinear vector/chiral frame measure bridge}&\texttt{OPEN}
\end{array}
$$

For the full \(\mathcal N=4\) claim, the last-but-one row includes gauge,
chiral-matter, FP, and NK carriers.  Pure-gauge fixed-vector closure alone is
not the full \(\mathcal N=4\) rooted functional.

## 5. Verdict

$$
\boxed{
\texttt{ROOTED\_WARD\_PROVED\_IN\_REGISTERED\_FRAME},
\quad
\texttt{UNIQUE\_COVARIANT\_DRESSING\_NOT\_PROVED},
\quad
\texttt{ANOMALY\_COEFFICIENT\_NOT\_ACCEPTED}.}
$$
