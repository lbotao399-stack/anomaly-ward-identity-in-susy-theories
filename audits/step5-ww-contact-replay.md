# Step 5 WW quadratic contact/cut replay

## 0. Notation

$$
X:=\nabla_+W_+,\qquad
\mathscr I^{AB}:=\nabla_-(X^AX^B),\qquad
\tau^{mn}:=\widetilde\delta^{mn}-\frac\epsilon2\delta_{(4)}^{mn},\qquad
\delta_{(4)mn}\tau^{mn}=0.
$$

## 1. Hessian and physical contact families

$$
\begin{aligned}
Q_{\rm Hess}^{(2)}={}&
-\frac12\operatorname{STr}_{\rm DRED}(I_0G_0H_2G_0)
-\frac12\operatorname{STr}_{\rm DRED}(I_1[p_1]G_0H_1[p_2]G_0)\\
&-\frac12\operatorname{STr}_{\rm DRED}(I_1[p_2]G_0H_1[p_1]G_0)
+\frac12\operatorname{STr}_{\rm DRED}(I_2G_0),\\
Q_{\rm cut}^{(2)}={}&
\sum_{o\in\{\mathrm D,\mathrm R\}}
\sum_{t=1}^{8}\sum_{e\in\{e_0,e_1,e_2\}}
C_{o,t,e}\operatorname{Collapse}_e(\Gamma_{\triangle,o,t}),\\
Q_{\rm phys}^{(2)}={}&Q_{\rm Hess}^{(2)}+Q_{\rm cut}^{(2)}+\mathrm{CT}_2.
\end{aligned}
$$

This is a regrouping, not an additional contribution:

$$
Q_{\rm cut}^{(2)}=\mathcal R_{\rm cut}Q_{\triangle}^{\rm bare},
\qquad
Q_{\triangle}^{\rm irr}
=(1-\mathcal R_{\rm cut})Q_{\triangle}^{\rm bare},
$$

$$
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm irr}+Q_{\rm phys}^{(2)},
\qquad
\mathcal R_{\rm cut}=\texttt{NOT\_CONSTRUCTED}.
$$

$$
N_{\rm collapse\ bindings}=48,\qquad
N_{\rm unique\ cut\ GraphIR}=6,\qquad
C_{o,t,e}=\texttt{OPEN},\qquad
C_{\mathrm{CT}_2}=\texttt{OPEN}.
$$

The following numbers are branch-path input literals, not graph counts:

$$
(B_{I_0H_2},B_{I_1H_1;p_1p_2},B_{I_1H_1;p_2p_1},B_{I_2})
=(576,1440,1440,720),\qquad
B_r=\texttt{NOT\_GENERATED}.
$$

## 2. Single-sign transport

$$
e^{-S_3/\hbar}=1-\frac{S_3}{\hbar}+\frac{S_3^2}{2\hbar^2}+\cdots,
\qquad C_{\rm Wick}(I_1,S_3)=-1.
$$

$$
C_{\rm Wick}(I_1,S_3)=C_{\rm Hess}(I_1,H_1)
=\texttt{NOT\_DERIVED}.
$$

$$
C_{\rm row}\neq
C_{\rm Wick}\,C_{\rm Neumann}\,C_{\rm stripped};
\qquad
\text{exactly one representation sign is used.}
$$

## 3. Projector census

$$
X_{(1)}=-\frac18D_+\bar D^2D_+V,\qquad
\widetilde W_{(1)\dot a}=-\frac18D^2\bar D_{\dot a}V.
$$

$$
N_{X,\rm local}=96,\qquad
N_{\widetilde W,\rm local}=120,\qquad
N_{\rm both,local}=32,\qquad
N_{\rm shared}=328.
$$

$$
\Pi_{X\widetilde W}H_2=\texttt{NOT\_DERIVED},\qquad
\Pi_{X\widetilde W}I_2=\texttt{NOT\_DERIVED}.
$$

## 4. Conditional I4 statement

$$
\left[
P(k,p_1,p_2)\in\mathbb Q[k,p_1,p_2]
\ \land\
\mathrm{Den}(k)=k^2
\right]
\Longrightarrow
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}\frac{P(k,p_1,p_2)}{k^2}=0.
$$

$$
N_{I_4,\rm conditional\ zero}=180,\qquad
N_{I_4,\rm certified\ zero}=0.
$$

The edge-tagged locality-to-polynomial implication is open.

## 5. Color and automorphism scope

$$
N_{\rm compiled\ incidence\ rows}=360+180=540,
\qquad
\mathcal C_{\rm red}
:=\left[\sum_r C_rT_r^{AB}{}_{DE}\right]
\Big/(\text{Jacobi},\text{antisymmetry},\kappa\text{-invariance}),
$$

$$
\operatorname{status}\!\left(\mathcal C_{\rm red}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED}.
$$

$$
|\operatorname{Aut}_{\mathfrak N}|_{\rm assigned}=1,\qquad
\operatorname{status}\!\left(
|\operatorname{Aut}_{\rm physical}|\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},\qquad
\operatorname{status}\!\left(\text{Taylor/Wick factorial matching proved}\right)
=\texttt{NOT\_COMPUTED}.
$$

## 6. Boundary

$$
\operatorname{status}\!\left(Q_{\rm phys,pole}^{(2)}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},\qquad
\operatorname{status}\!\left(Q_{\tau,\rm pole}^{(2)}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},\qquad
\operatorname{status}\!\left(C_{\rm anomaly}\text{ accepted}\right)
=\texttt{NOT\_ACCEPTED}.
$$

Schema invariants: 19 checked, 0 failed.  They certify serialization and fail-closed scope only.
