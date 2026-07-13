# Step 5A cubic open-$\tau$ projection feasibility

## 0. Status

$$
\boxed{
\mathsf{C}_{\tau,3}
=\texttt{BLOCKED\_MISSING\_COMPLETE\_N3\_PROJECT\_GRAMMAR}
}
$$

$$
\mathcal A_{\tau,3}^{\rm pre}
=\Gamma_{\tau,3}^{\rm pole}
=\texttt{NOT\ COMPUTED}.
$$

## 1. Target

$$
\mathscr E_{abc}^{AB}
=K^{AB}{}_{C[DE]}
\tau_{(ab|\dot c\dot d|}
W_{c)}^C
\widetilde W^{D\dot c}
\widetilde W^{E\dot d},
$$

$$
K^{AB}{}_{C[DE]}
=\delta^A{}_C c_{DE}{}^B
+\delta^B{}_C c_{DE}{}^A.
$$

$$
N_{\tau,N=3}=1,
\qquad
N_{\mathrm{physical},N=3}=0.
$$

$$
K^{00}{}_{0[DE]}B^{DE}=4B^{12}\ne0.
$$

The fields are $W,\widetilde W$; $\tau$ is a DRED coefficient spurion, not a
new background field.

$$
\mathscr E_\tau\in\mathcal V_{\rm DRED,raw}^{\rm CE},
\qquad
q_{4d}(\tau)=0,
\qquad
q_{4d}(\mathscr E_\tau)=0.
$$

## 2. Complete rooted census

$$
\Gamma_{J,3}^{(1)}
=\frac12
\sum_{s+\sum_jr_j=3}
(-1)^k\operatorname{STr}
\left[I_sG_0H_{r_1}G_0\cdots H_{r_k}G_0\right]
+\mathrm{CT}_3.
$$

$$
N_{\rm family}=8,
\qquad
N_{\rm polarized}=26.
$$

$$
\begin{array}{c|c|c|c|c|c}
\text{family}&N_{\rm pol}&k&\text{coefficient}&N_{\rm branch}&\text{gate}\\ \hline
I0\,H3&1&1&-\frac12&\texttt{BLOCKED}&\texttt{MISSING\ }H3\\
I0\,H1\,H2&3&2&+\frac12&41472&\texttt{KERNEL\ READY}\\
I0\,H2\,H1&3&2&+\frac12&41472&\texttt{KERNEL\ READY}\\
I0\,H1\,H1\,H1&6&3&-\frac12&331776&\texttt{KERNEL\ READY}\\
I1\,H2&3&1&-\frac12&25920&\texttt{KERNEL\ READY}\\
I1\,H1\,H1&6&2&+\frac12&207360&\texttt{KERNEL\ READY}\\
I2\,H1&3&1&-\frac12&51840&\texttt{KERNEL\ READY}\\
I3&1&0&+\frac12&\texttt{BLOCKED}&\texttt{MISSING\ }I3\\
\end{array}
$$

$$
N_{\rm kernel\ ready\ rows}=24,
\qquad
N_{\rm kernel\ blocked\ rows}=2,
$$

$$
N_{\rm available\ vector\ branch\ paths}
=699840.
$$

## 3. Missing kernels

$$
N(H_1^{VV})=24,
\qquad
N(H_2^{VV})=144,
\qquad
N(H_3^{VV})=\texttt{BLOCKED}.
$$

$$
\deg_V(\Gamma,W,\widetilde\Gamma,\widetilde W)\in\{1,2,3\},
\qquad
[V^5]S_{\rm gauge}=\texttt{ABSENT\ FROM\ GRAMMAR}.
$$

$$
N(I_0)=4,
\qquad
N(I_1)=60,
\qquad
N(I_2)=720,
\qquad
N(I_3)=\texttt{BLOCKED}.
$$

$$
I_3
=\left[V_{\rm B}^3v^2\right]
\nabla_-\left(X^AX^B\right)
=I_{(5)}[V_{\rm B}^3,v,v],
$$

$$
I_{(5)}=\texttt{ABSENT\ FROM\ GRAMMAR}.
$$

## 4. Missing projection

$$
P_\tau:
\mathcal A_{J,3}
\longrightarrow
K^{AB}{}_{C[DE]}
\tau_{(ab|\dot c\dot d|}
W_{c)}^C\widetilde W^{D\dot c}\widetilde W^{E\dot d}
$$

is not an executable Project map.

$$
\texttt{tau\ token}=0,
\qquad
\texttt{rank-five\ color\ projector}=0,
\qquad
\texttt{n=3\ pinch\ orbit}=0.
$$

The scheduled compiler requires

$$
N_{\rm vertex}=N_{\rm edge}=3,
$$

so it rejects the $k=3$ box and every $n=3$ contact topology.

## 5. Counterterm boundary

$$
\Gamma_{J,3}^{\rm ren}
=\Gamma_{J,3}^{\rm loop}+\mathrm{CT}_3.
$$

$$
\Gamma_{J,3}^{\rm loop,pole}
\text{ does not require }\mathrm{CT}_3,
\qquad
\Gamma_{J,3}^{\rm ren}
\text{ requires }\mathrm{CT}_3.
$$

$$
\mathrm{CT}_3=\texttt{UNRESOLVED}.
$$

## 6. Exact checks

$$
1+3+3+6+3+6+3+1=26.
$$

$$
\begin{aligned}
N_{\rm available}
={}&3(4\cdot24\cdot144)
+3(4\cdot144\cdot24)
+6(4\cdot24^3)\\
&+3(60\cdot144)
+6(60\cdot24^2)
+3(720\cdot24)\\
={}&41472+41472+331776+25920+207360+51840\\
={}&699840.
\end{aligned}
$$

## 7. Gap table

$$
\begin{array}{c|c|c|c}
\text{gap}&\text{type}&\text{missing object}&\text{severity}\\ \hline
G1&\mathrm{G\!\!-DEF}&H_3&P0\\
G2&\mathrm{G\!\!-DEF}&I_3&P0\\
G3&\mathrm{G\!\!-PROJ}&P_\tau\ \text{and }P_K&P0\\
G4&\mathrm{G\!\!-OP}&26\ \mathrm{GraphIRs}\ \text{and pinch orbit}&P0\\
G5&\mathrm{G\!\!-PROJ}&\text{open-rank DRED pole reducer}&P0\\
G6&\mathrm{G\!\!-NORM}&\mathrm{CT}_3&P1
\end{array}
$$

## 8. Result

$$
\boxed{
\mathsf C_{\tau,3}^{\rm raw\ DRED}
=\texttt{NOT\ DERIVED},
\qquad
q_{4d}(\mathscr E_\tau)=0.
}
$$
