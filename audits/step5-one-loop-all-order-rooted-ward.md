# Step 5A all-order rooted one-loop Ward certificate

## 1. Rooted expansion

$$
H_B=H_0+\sum_{r\ge1}H_r,
\qquad
I_B=\sum_{s\ge0}I_s.
$$

$$
\left.
\frac{\vec{\delta}}{\delta J}
\frac12\operatorname{STr}\log(H_B+JI_B)
\right|_{J=0}
=\frac12\operatorname{STr}(G_BI_B),
\qquad
G_B=(H_0+H_+)^{-1}.
$$

$$
G_B
=G_0\sum_{k=0}^\infty(-H_+G_0)^k.
$$

$$
\Gamma_{\mathscr I}^{(1)}
=\frac12\sum_{k\ge0}(-1)^k
\operatorname{STr}\!\left[
I_sG_0H_{r_1}G_0\cdots H_{r_k}G_0
\right],
\qquad
s+\sum_{j=1}^kr_j=n.
$$

$$
N_{\rm family}(n)=2^n,
$$

For \(m=n-s\ge1\), the ordered positive compositions obey

$$
\sum_{k=1}^m\binom{m-1}{k-1}=2^{m-1}.
$$

Hence

$$
N_{\rm family}(n)
=1+\sum_{m=1}^n2^{m-1}
=2^n.
$$

$$
N_{\rm pol}(n)
=\sum_{s=0}^n\binom ns
\sum_{k=0}^{n-s}k!\,S(n-s,k).
$$

$$
\begin{array}{c|cc}
n&N_{\rm family}&N_{\rm pol}\\ \hline
0&1&1\\
1&2&2\\
2&4&6\\
3&8&26\\
4&16&150\\
5&32&1082\\
6&64&9366\\
\end{array}
$$

## 2. Topology

$$
k=2:\triangle,
\qquad
k=3:\Box,
\qquad
k=4:\text{pentagon}.
$$

$$
N_{\rm vertices}=N_{\rm propagators}=k+1.
$$

Multi-background \(I_s\) and \(H_r\) give tadpole, seagull, pinch, and contact
members of the same rooted cycle; they are not additional one-loop words.

## 3. Ward telescoping

$$
\delta H=[R,H],
\qquad
\delta G=-G(\delta H)G
=-GRH G+GHRG
=RG-GR
=[R,G].
$$

For \(|R|=0\),

$$
\begin{aligned}
\delta(M_1\cdots M_m)
&=\sum_{j=1}^m
M_1\cdots(RM_j-M_jR)\cdots M_m\\
&=R(M_1\cdots M_m)-(M_1\cdots M_m)R,
\end{aligned}
$$

$$
\operatorname{STr}\delta(M_1\cdots M_m)=0.
$$

The executable cyclic-word reduction passes through \(n=6\).

## 4. Measure trace

$$
\operatorname{Tr}_{\rm Adj}(\operatorname{ad}_\eta)
=\eta^Cc_{CA}{}^A
=\eta^C\kappa^{AB}c_{CAB}
=0.
$$

## 5. DRED cyclicity

For

$$
a^m=\widehat\delta^m{}_na^n,
\qquad
\ell^m=k^m+a^m,
$$

the Project loop domain is mapped to itself and

$$
\det\!\left(\frac{\partial\ell}{\partial k}\right)=1.
$$

Therefore

$$
\begin{aligned}
\int_kF(k+a)
&=\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}F(k+a)\\
&=\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}F(\ell)
=\int_\ell F(\ell).
\end{aligned}
$$

The boundary term is zero by the Project test-field condition

$$
\int d^dx\,\partial_{\widehat m}Y^{\widehat m}=0.
$$

Since \(|R|=0\), finite color-trace cyclicity, Berezin integration, and this
loop translation give

$$
\operatorname{STr}_{\rm DRED}[R,\mathcal M]=0.
$$

## 6. Boundary

$$
\text{rooted one-loop census}
=\texttt{PASS}.
$$

$$
\text{full covariant completion}
=\texttt{OPEN}:
\qquad
\begin{gathered}
\delta H=[R,H],
\qquad
\delta I=[R,I],\\
\ker\bar\ell_2=0.
\end{gathered}
$$

must still be certified in the Project source-completed complex.  No anomaly
coefficient is accepted.
