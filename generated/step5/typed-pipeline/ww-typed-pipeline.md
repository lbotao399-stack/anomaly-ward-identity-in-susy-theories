# Step 5A — Typed WW supergraph pipeline

## Notation

$$
\mathbb K=\mathbb Q(i,\sqrt2),\qquad h_{\mathfrak N}=\texttt{e235bf689c01b9644e9b1dcffdc420a7060bb8f5ee6db8316cbbddcf73f3eb79}.
$$

## Compiler

$$
\mathfrak N\xrightarrow{C_G}\mathfrak G\xrightarrow{C_A}\mathfrak A\xrightarrow{C_D}\mathfrak D.
$$

## Graph census

### DIRECT

$$
N_{\rm typed}=8,\qquad N_{\rm admitted}=1,\qquad b_1=1.
$$

$$
(r_0,r_1,r_2)=(k,k+q,k+p+q),\qquad C_G=-\frac{1}{8}g^2.
$$

### REFLECTED

$$
N_{\rm typed}=8,\qquad N_{\rm admitted}=1,\qquad b_1=1.
$$

$$
(r_0,r_1,r_2)=(k,k+q,k+p+q),\qquad C_G=\frac{1}{8}g^2.
$$

## D-algebra status

$$
D^2\bar D^2D^2=-16p_{(4)}^2D^2\quad\Longrightarrow\quad\texttt{local projector job = PASS}.
$$

$$
\left.D\bar D\,W_{\rm ext}\right|_{\rm physical\ WW\ schedule}\quad\Longrightarrow\quad\texttt{PASS\_PHYSICAL\_16\_ROW\_PHASE\_SEQUENCE},
$$

$$
\texttt{scope}\prec\texttt{endpoint}\prec\texttt{IBP}\prec\texttt{normal\ order}\prec\texttt{projector}\prec\texttt{chirality}\prec\texttt{saturation}\prec\texttt{collapse}.
$$

## Specialized row-to-pole binding

$$
C_{G}^{\rm D}=-\frac{g^2}{8},\qquad C_{G}^{\rm R}=+\frac{g^2}{8},\qquad C_D=-\frac12,
$$

$$
C_{\rm row}^{\rm D}=+\frac{g^2}{16},\qquad C_{\rm row}^{\rm R}=-\frac{g^2}{16},
$$

$$
\operatorname{Pole}\!\left[\int\frac{d^d\ell}{(2\pi)^d}\frac{\ell^\mu\ell^\nu}{(\ell^2+\Delta)^3}\right]=\frac{1}{16\pi^2}\frac{\widehat\delta^{\mu\nu}}{4\epsilon},
$$

$$
\sum_{r=1}^{8}P_{r}^{\rm D}=+\frac{g^2}{128\pi^2\epsilon}\widehat\delta^{\mu\nu},\qquad \sum_{r=1}^{8}P_{r}^{\rm R}=-\frac{g^2}{128\pi^2\epsilon}\widehat\delta^{\mu\nu}.
$$

Status: \texttt{PASS\_SPECIALIZED\_16\_ROW\_DRED\_MASTER\_BINDING}; generic out-of-scope $D$-words still fail closed.

$$
\Gamma_{\rm anomaly}:\ \texttt{NOT\_ACCEPTED}.
$$
