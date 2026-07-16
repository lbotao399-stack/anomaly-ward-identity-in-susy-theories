# AB/BA G1 provenance first-error exact audit

Status: `PASS_G1_FIRST_ERROR_IS_PURE_DIVERGENCE_MISREPORTED_AS_PHYSICAL_TWO`.

## 1. Source-selected DRED orbit

Let

$$
X=\langle D,B_1\rangle,
\qquad
Y=B_1(P^{\dot a}D_{\dot a}),
\qquad
T_{DB}=P^{\dot a}(D_{\dot a}B_1)=X+Y.
$$

The exact selected rows are

$$
A=\frac43p+\frac23q,
\qquad
B=\frac23p+\frac43q,
$$

therefore

$$
A+B=2p+2q=2X+2Y=2T_{DB}.
$$

For a general raw vector $(a,b)$,

$$
aX+bY=(a-b)X+bT_{DB},
$$

so

$$
\begin{pmatrix}c_{\rm pair}\\c_{T}\end{pmatrix}
=
\begin{pmatrix}1&-1\\0&1\end{pmatrix}
\begin{pmatrix}2\\2\end{pmatrix}
=
\begin{pmatrix}0\\2\end{pmatrix}.
$$

Hence

$$
\boxed{(2,2)_{(p,q)}=2T_{DB},\qquad c_{\rm pair}=0.}
$$

The same result follows at $q=-p$:

$$
A=\frac43-\frac23=\frac23,
\qquad
B=\frac23-\frac43=-\frac23,
\qquad
A+B=0.
$$

## 2. Rejected generic lift

The later full-word reconstruction gives

$$
F_{\rm generic}=-\frac76p-\frac43q.
$$

Its restriction is

$$
F_{\rm generic}\big|_{q=-p}
=-\frac76+\frac43
=\frac{-7+8}{6}
=\frac16.
$$

The direct one-variable replay gives

$$
F_{\rm direct}=-\frac32+1=-\frac12.
$$

Thus

$$
\frac16-\left(-\frac12\right)
=\frac16+\frac36
=\frac46
=\frac23\ne0.
$$

This lift remains `BLOCKED_RAW_GRAPH_Q_DATA_MISSING` and cannot replace the
selected orbit.

## 3. First error

The unified audit itself records

$$
(2,2)_{(p,q)}\longmapsto(0,2)_{({\rm pair},T_{DB})},
$$

but its final status calls the same row a physical G1 factor two.  The first
invalid step is therefore

$$
\boxed{2T_{DB}\not\longrightarrow 2\langle D,B_1\rangle.}
$$

G1 and G3 do not form a common physical factor-two mismatch.
