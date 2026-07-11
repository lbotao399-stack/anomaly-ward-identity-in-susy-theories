# 00 3+1d SUSY QFT — Convention Lock

## Step 3C. Gauge vector representation

### 3C.1 Frames and bridge order

$$
R\in\{L,E\},
\qquad
\kappa_L:=2i,
\qquad
\kappa_E:=-2,
\qquad
u_R:=\frac4{\kappa_R},
\qquad
\rho_R:=\frac4{\kappa_R^2}.
\tag{3C.1}
$$

Thus

$$
(u_L,\rho_L)=(-2i,-1),
\qquad
(u_E,\rho_E)=(-2,+1).
\tag{3C.2}
$$

The three gauge frames are denoted by

$$
\mathsf V:=\text{gauge-vector frame},
\qquad
\mathsf C:=\text{gauge-chiral frame},
\qquad
\mathsf A:=\text{gauge-antichiral frame}.
\tag{3C.3}
$$

They are distinct from the Step-2A coordinate choice:

$$
\boxed{
\text{supersymmetry chiral coordinates }(y_R,\vartheta)
\ne
\text{gauge-chiral frame }\mathsf C
\ne
\text{gauge-vector frame }\mathsf V.}
\tag{3C.4}
$$

Define

$$
\begin{gathered}
G^{\rm loc}
:=\left\{e^{i\alpha^AT_A}:\alpha^A\in\mathbb R
\text{ in the chosen connected chart}\right\},\\
G_{\mathbb C}^{\rm loc}
:=\left\{e^{i\alpha^AT_A}:\alpha^A\in\mathbb C
\text{ in the chosen connected chart}\right\},\\
h_R:=e^{i\Lambda_R},
\qquad
\widetilde h_R:=e^{i\widetilde\Lambda_R},
\qquad
\bar D_{R\dot a}\Lambda_R=0,
\qquad
D_{Ra}\widetilde\Lambda_R=0,\\
h_R,\widetilde h_R,k_R,
\mathcal B_R,\widetilde{\mathcal B}_R
\in G_{\mathbb C}^{\rm loc}.
\end{gathered}
\tag{3C.5}
$$

Introduce two frame bridges and retain the Step-3A relative bridge:

$$
\boxed{
\mathcal B_R,
\qquad
\widetilde{\mathcal B}_R,
\qquad
\mathcal E_R
:=\widetilde{\mathcal B}_R\mathcal B_R
=e^{\mathcal V_R}.}
\tag{3C.6}
$$

Their finite transformations are

$$
\boxed{
\mathcal B_R'
=k_R\mathcal B_Rh_R^{-1},
\qquad
\widetilde{\mathcal B}_R'
=\widetilde h_R\widetilde{\mathcal B}_Rk_R^{-1}.}
\tag{3C.7}
$$

Hence

$$
\begin{aligned}
\mathcal E_R'
&=\widetilde{\mathcal B}_R'\mathcal B_R'\\
&=\widetilde h_R\widetilde{\mathcal B}_R
k_R^{-1}k_R\mathcal B_Rh_R^{-1}\\
&=\boxed{\widetilde h_R\mathcal E_Rh_R^{-1}},
\end{aligned}
\tag{3C.8}
$$

which is exactly (3A.32), with

$$
\widetilde h_L=\bar h_L,
\qquad
\widetilde\Lambda_L=\bar\Lambda_L.
\tag{3C.9}
$$

Lorentzian formal reality is

$$
\boxed{
\widetilde{\mathcal B}_L
=\mathcal B_L^{\ddagger_L},
\qquad
k_L^{\ddagger_L}=k_L^{-1},
\qquad
h_L^{\ddagger_L}=\widetilde h_L^{-1},
\qquad
k_L\in G^{\rm loc}.}
\tag{3C.10}
$$

Therefore

$$
\mathcal E_L
=\mathcal B_L^{\ddagger_L}\mathcal B_L,
\qquad
\mathcal E_L^{\ddagger_L}=\mathcal E_L.
\tag{3C.11}
$$

Intrinsic Euclidean superspace instead imposes

$$
\boxed{
(\mathcal B_E,\widetilde{\mathcal B}_E),
\quad
(h_E,\widetilde h_E),
\quad
k_E
\text{ are independent complexified data}.}
\tag{3C.12}
$$

### 3C.2 Complete covariant-derivative system

Let

$$
\mathfrak A=(a,\dot a,M),
\qquad
|a|=|\dot a|=1,
\qquad
|M|=0,
\qquad
D_{R\mathfrak A}:=(D_{Ra},\bar D_{R\dot a},\partial_{RM}),
\tag{3C.13}
$$

and reserve (A,B,C) for adjoint gauge indices.  The flat algebra is

$$
[D_{R\mathfrak A},D_{R\mathfrak B}\}
=T^R_{\mathfrak A\mathfrak B}{}^{\mathfrak C}
D_{R\mathfrak C},
\qquad
T^R_{a\dot b}{}^M
=T^R_{\dot b a}{}^M
=\kappa_R(\sigma_R^M)_{a\dot b},
\qquad
T^R_{\mathfrak A\mathfrak B}{}^{\mathfrak C}=0
\text{ otherwise}.
\tag{3C.14}
$$

Define

$$
\boldsymbol\nabla^{\mathsf V}_{R\mathfrak A}
:=D_{R\mathfrak A}
-i\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak A},
\tag{3C.15}
$$

$$
[\boldsymbol\nabla^{\mathsf V}_{R\mathfrak A},
\boldsymbol\nabla^{\mathsf V}_{R\mathfrak B}\}
=T^R_{\mathfrak A\mathfrak B}{}^{\mathfrak C}
\boldsymbol\nabla^{\mathsf V}_{R\mathfrak C}
-i\boldsymbol{\mathcal F}^{\mathsf V}_{R\mathfrak A\mathfrak B}.
\tag{3C.16}
$$

Direct expansion gives

$$
\boxed{
\begin{aligned}
\boldsymbol{\mathcal F}^{\mathsf V}_{R\mathfrak A\mathfrak B}
={}&D_{R\mathfrak A}\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak B}
-(-1)^{|\mathfrak A||\mathfrak B|}
D_{R\mathfrak B}\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak A}\\
&-i[\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak A},
\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak B}\}
-T^R_{\mathfrak A\mathfrak B}{}^{\mathfrak C}
\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak C}.
\end{aligned}}
\tag{3C.17}
$$

From

$$
(\boldsymbol\nabla^{\mathsf V}_{R\mathfrak A})'
=k_R\boldsymbol\nabla^{\mathsf V}_{R\mathfrak A}k_R^{-1},
\tag{3C.18}
$$

one obtains

$$
\boxed{
(\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak A})'
=k_R\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak A}k_R^{-1}
-i(D_{R\mathfrak A}k_R)k_R^{-1},}
\tag{3C.19}
$$

because

$$
k_RD_{R\mathfrak A}k_R^{-1}
=D_{R\mathfrak A}-(D_{R\mathfrak A}k_R)k_R^{-1}.
\tag{3C.20}
$$

The constraints are

$$
\boxed{
\boldsymbol{\mathcal F}^{\mathsf V}_{Rab}=0,
\qquad
\boldsymbol{\mathcal F}^{\mathsf V}_{R\dot a\dot b}=0,
\qquad
\boldsymbol{\mathcal F}^{\mathsf V}_{Ra\dot b}=0.}
\tag{3C.21}
$$

The first two are representation-preserving.  Their local solutions are

$$
\boxed{
\begin{aligned}
\boldsymbol\nabla^{\mathsf V}_{Ra}
&=\widetilde{\mathcal B}_R^{-1}
\circ D_{Ra}\circ\widetilde{\mathcal B}_R,\\
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
&=\mathcal B_R\circ\bar D_{R\dot a}
\circ\mathcal B_R^{-1},\\
\{\boldsymbol\nabla^{\mathsf V}_{Ra},
\boldsymbol\nabla^{\mathsf V}_{Rb}\}
&=\widetilde{\mathcal B}_R^{-1}
\{D_{Ra},D_{Rb}\}
\widetilde{\mathcal B}_R=0,\\
\{\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a},
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot b}\}
&=\mathcal B_R
\{\bar D_{R\dot a},\bar D_{R\dot b}\}
\mathcal B_R^{-1}=0.
\end{aligned}}
\tag{3C.22}
$$

The conventional mixed constraint defines the vector derivative:

$$
\boxed{
\boldsymbol{\mathcal D}^{\mathsf V}_{RM}
:=\boldsymbol\nabla^{\mathsf V}_{RM}
=\partial_{RM}
-i\boldsymbol{\mathcal A}^{\mathsf V}_{RM},
\qquad
\{\boldsymbol\nabla^{\mathsf V}_{Ra},
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot b}\}
=\kappa_R(\sigma_R^M)_{a\dot b}
\boldsymbol{\mathcal D}^{\mathsf V}_{RM}.}
\tag{3C.23}
$$

Equations (3C.5), (3C.7), and (3C.22) give

$$
(\boldsymbol\nabla^{\mathsf V}_{Ra})'
=k_R\boldsymbol\nabla^{\mathsf V}_{Ra}k_R^{-1},
\qquad
(\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a})'
=k_R\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}k_R^{-1}.
\tag{3C.24}
$$

### 3C.3 Chiral and antichiral similarities

The gauge-chiral frame is

$$
\boxed{
\begin{aligned}
\nabla^{\mathsf C}_{Ra}
&:=\mathcal B_R^{-1}
\boldsymbol\nabla^{\mathsf V}_{Ra}\mathcal B_R
=\mathcal E_R^{-1}\circ D_{Ra}\circ\mathcal E_R,\\
\bar\nabla^{\mathsf C}_{R\dot a}
&:=\mathcal B_R^{-1}
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}\mathcal B_R
=\bar D_{R\dot a},\\
\mathcal D^{\mathsf C}_{RM}
&:=\mathcal B_R^{-1}
\boldsymbol{\mathcal D}^{\mathsf V}_{RM}\mathcal B_R,\\
\nabla^{\mathsf C}_{R\mathfrak A}
&:=\left(
\nabla^{\mathsf C}_{Ra},
\bar\nabla^{\mathsf C}_{R\dot a},
\mathcal D^{\mathsf C}_{RM}
\right).
\end{aligned}}
\tag{3C.25}
$$

The first equality follows without commuting any factor:

$$
\begin{aligned}
\mathcal B_R^{-1}
\widetilde{\mathcal B}_R^{-1}
\circ D_{Ra}\circ
\widetilde{\mathcal B}_R\mathcal B_R
&=(\widetilde{\mathcal B}_R\mathcal B_R)^{-1}
\circ D_{Ra}\circ
(\widetilde{\mathcal B}_R\mathcal B_R)\\
&=\mathcal E_R^{-1}\circ D_{Ra}\circ\mathcal E_R.
\end{aligned}
\tag{3C.26}
$$

The gauge-antichiral frame is

$$
\boxed{
\begin{aligned}
\nabla^{\mathsf A}_{Ra}
&:=\widetilde{\mathcal B}_R
\boldsymbol\nabla^{\mathsf V}_{Ra}
\widetilde{\mathcal B}_R^{-1}
=D_{Ra},\\
\bar\nabla^{\mathsf A}_{R\dot a}
&:=\widetilde{\mathcal B}_R
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\widetilde{\mathcal B}_R^{-1}
=\mathcal E_R\circ\bar D_{R\dot a}
\circ\mathcal E_R^{-1}
=\bar D_{R\dot a}+\widetilde\Gamma^{\mathsf A}_{R\dot a},\\
\widetilde\Gamma^{\mathsf A}_{R\dot a}
&:=\mathcal E_R(\bar D_{R\dot a}\mathcal E_R^{-1}),\\
(\bar\nabla^{\mathsf A}_{R\dot a})^{\rm row}X
&:=\bar D_{R\dot a}X
-(-1)^{|X|}X\widetilde\Gamma^{\mathsf A}_{R\dot a},\\
\mathcal D^{\mathsf A}_{RM}
&:=\widetilde{\mathcal B}_R
\boldsymbol{\mathcal D}^{\mathsf V}_{RM}
\widetilde{\mathcal B}_R^{-1},\\
\nabla^{\mathsf A}_{R\mathfrak A}
&:=\left(
\nabla^{\mathsf A}_{Ra},
\bar\nabla^{\mathsf A}_{R\dot a},
\mathcal D^{\mathsf A}_{RM}
\right).
\end{aligned}}
\tag{3C.27}
$$

Consequently

$$
\boxed{
\nabla^{\mathsf A}_{R\mathfrak A}
=\mathcal E_R
\nabla^{\mathsf C}_{R\mathfrak A}
\mathcal E_R^{-1}.}
\tag{3C.28}
$$

A local symmetric bridge gauge is

$$
\boxed{
\begin{gathered}
h_R=\widetilde h_R=\mathbf1,
\qquad
k_R:=e^{\mathcal V_R/2}\mathcal B_R^{-1},\\
\mathcal B_R'
=k_R\mathcal B_R=e^{\mathcal V_R/2},\\
\widetilde{\mathcal B}_R'
=\widetilde{\mathcal B}_Rk_R^{-1}
=\widetilde{\mathcal B}_R\mathcal B_Re^{-\mathcal V_R/2}
=e^{\mathcal V_R}e^{-\mathcal V_R/2}
=e^{\mathcal V_R/2},\\
\mathcal B_R'
=\widetilde{\mathcal B}_R'
=e^{\mathcal V_R/2},
\qquad
\mathcal E_R=e^{\mathcal V_R/2}e^{\mathcal V_R/2}
=e^{\mathcal V_R},\\
k_L^{\ddagger_L}
=(\mathcal B_L^{\ddagger_L})^{-1}e^{\mathcal V_L/2}
=\mathcal B_Le^{-\mathcal V_L}e^{\mathcal V_L/2}
=\mathcal B_Le^{-\mathcal V_L/2}
=k_L^{-1},\\
\mathcal B_L^{\ddagger_L}\mathcal B_L=e^{\mathcal V_L}.
\end{gathered}}
\tag{3C.29}
$$

For

$$
e^{\mathcal V_R'}
=\widetilde h_Re^{\mathcal V_R}h_R^{-1},
\tag{3C.30}
$$

the compensating vector-frame transformation preserving (3C.29) is

$$
\boxed{
k_R(\Lambda_R,\widetilde\Lambda_R)
=e^{\mathcal V_R'/2}h_Re^{-\mathcal V_R/2},
\qquad
k_R^{-1}
=e^{-\mathcal V_R/2}\widetilde h_R^{-1}
e^{\mathcal V_R'/2}.}
\tag{3C.31}
$$

For (R=L), (3C.10) implies

$$
k_L(\Lambda_L,\bar\Lambda_L)^{\ddagger_L}
=k_L(\Lambda_L,\bar\Lambda_L)^{-1}.
\tag{3C.32}
$$

### 3C.4 Field strengths and graded Jacobi identities

Define the gauge-vector-frame strengths by transport from the accepted
Step-3A projectors:

$$
\boxed{
\begin{aligned}
\boldsymbol{\mathcal W}^{\mathsf V}_{Ra}
&:=\mathcal B_R\mathcal W^{\mathsf C}_{Ra}\mathcal B_R^{-1},\\
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot a}
&:=\widetilde{\mathcal B}_R^{-1}
\widetilde{\mathcal W}^{\mathsf A}_{R\dot a}
\widetilde{\mathcal B}_R,
\end{aligned}}
\tag{3C.33}
$$

where

$$
\boxed{
\begin{aligned}
\mathcal W^{\mathsf C}_{Ra}
&=-\frac18\bar D_R^2
\left[\mathcal E_R^{-1}(D_{Ra}\mathcal E_R)\right],\\
\widetilde{\mathcal W}^{\mathsf A}_{R\dot a}
&=+\frac18D_R^2
\left[\mathcal E_R(\bar D_{R\dot a}\mathcal E_R^{-1})\right].
\end{aligned}}
\tag{3C.34}
$$

Thus

$$
\boxed{
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb}=0,
\qquad
\boldsymbol\nabla^{\mathsf V}_{Ra}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b}=0.}
\tag{3C.35}
$$

Write

$$
\begin{gathered}
\partial_{Ra\dot b}
:=(\sigma_R^M)_{a\dot b}\partial_{RM},\\
\boldsymbol{\mathcal D}^{\mathsf V}_{Ra\dot b}
:=(\sigma_R^M)_{a\dot b}
\boldsymbol{\mathcal D}^{\mathsf V}_{RM},
\qquad
\mathcal D^{\mathsf C}_{Ra\dot b}
:=(\sigma_R^M)_{a\dot b}\mathcal D^{\mathsf C}_{RM}
=\mathcal B_R^{-1}
\boldsymbol{\mathcal D}^{\mathsf V}_{Ra\dot b}
\mathcal B_R.
\end{gathered}
\tag{3C.36}
$$

In the gauge-chiral frame,

$$
\mathcal D^{\mathsf C}_{Rb\dot b}
=\partial_{Rb\dot b}
+\kappa_R^{-1}\bar D_{R\dot b}\Gamma^{\mathsf C}_{Rb},
\qquad
\Gamma^{\mathsf C}_{Rb}:=\mathcal E_R^{-1}(D_{Rb}\mathcal E_R).
\tag{3C.37}
$$

Using

$$
\bar D_{R\dot a}\bar D_{R\dot b}
=-\frac12\epsilon_{\dot a\dot b}\bar D_R^2,
\tag{3C.38}
$$

one obtains

$$
\begin{aligned}
[\bar\nabla^{\mathsf C}_{R\dot a},
\mathcal D^{\mathsf C}_{Rb\dot b}]
&=-\frac1{2\kappa_R}\epsilon_{\dot a\dot b}
\bar D_R^2\Gamma^{\mathsf C}_{Rb}\\
&=\frac4{\kappa_R}\epsilon_{\dot a\dot b}
\mathcal W^{\mathsf C}_{Rb}.
\end{aligned}
\tag{3C.39}
$$

Similarity transport and the antichiral calculation give

$$
\begin{gathered}
D_{Ra}D_{Rb}=+\frac12\epsilon_{ab}D_R^2,
\qquad
\mathcal D^{\mathsf A}_{Rb\dot b}
=\partial_{Rb\dot b}
+\kappa_R^{-1}D_{Rb}\widetilde\Gamma^{\mathsf A}_{R\dot b},\\
{}[\nabla^{\mathsf A}_{Ra},
\mathcal D^{\mathsf A}_{Rb\dot b}]
=\frac1{2\kappa_R}\epsilon_{ab}
D_R^2\widetilde\Gamma^{\mathsf A}_{R\dot b}
=\frac4{\kappa_R}\epsilon_{ab}
\widetilde{\mathcal W}^{\mathsf A}_{R\dot b}.
\end{gathered}
\tag{3C.39a}
$$

$$
\boxed{
\begin{aligned}
[\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a},
\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b}]
&=u_R\epsilon_{\dot a\dot b}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb},\\
{}[\boldsymbol\nabla^{\mathsf V}_{Ra},
\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b}]
&=u_R\epsilon_{ab}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b}.
\end{aligned}}
\tag{3C.40}
$$

The graded Jacobi identity gives

$$
\begin{aligned}
0={}&
[\boldsymbol\nabla^{\mathsf V}_{Ra},
[\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a},
\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b}]]\\
&-[\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a},
[\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b},
\boldsymbol\nabla^{\mathsf V}_{Ra}]]\\
&+[\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b},
\{\boldsymbol\nabla^{\mathsf V}_{Ra},
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}\}]\\
={}&u_R\epsilon_{\dot a\dot b}
\boldsymbol\nabla^{\mathsf V}_{Ra}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb}
+u_R\epsilon_{ab}
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b}\\
&-\kappa_R
{}[\boldsymbol{\mathcal D}^{\mathsf V}_{Ra\dot a},
\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b}].
\end{aligned}
\tag{3C.41}
$$

so that

$$
\begin{aligned}
\frac{u_R}{\kappa_R}
&=\frac4{\kappa_R^2}=\rho_R,\\
{}[\boldsymbol{\mathcal D}^{\mathsf V}_{Ra\dot a},
\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b}]
={}&\rho_R\epsilon_{\dot a\dot b}
\boldsymbol\nabla^{\mathsf V}_{Ra}\boldsymbol{\mathcal W}^{\mathsf V}_{Rb}\\
&+\rho_R\epsilon_{ab}
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b}.
\end{aligned}
\tag{3C.42}
$$

Antisymmetry under
((a\dot a)\leftrightarrow(b\dot b)) yields

$$
\begin{gathered}
0=\epsilon_{\dot a\dot b}
\left(
\boldsymbol\nabla^{\mathsf V}_{Ra}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb}
-\boldsymbol\nabla^{\mathsf V}_{Rb}
\boldsymbol{\mathcal W}^{\mathsf V}_{Ra}
\right)\\
\qquad
+\epsilon_{ab}
\left(
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b}
-\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot b}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot a}
\right),\\
M_{ab}:=\boldsymbol\nabla^{\mathsf V}_{Ra}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb},
\qquad
N_{\dot a\dot b}:=
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b},\\
M_{ab}-M_{ba}=\epsilon_{ab}M^c{}_c,
\qquad
N_{\dot a\dot b}-N_{\dot b\dot a}
=\epsilon_{\dot a\dot b}N^{\dot c}{}_{\dot c},\\
\boxed{
\boldsymbol\nabla_R^{\mathsf V a}
\boldsymbol{\mathcal W}^{\mathsf V}_{Ra}
+\bar{\boldsymbol\nabla}_R^{\mathsf V\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot a}=0.}
\end{gathered}
\tag{3C.43}
$$

Using (3C.43), (3C.42) becomes

$$
\boxed{
\begin{aligned}
\boldsymbol\nabla^{\mathsf V}_{Ra}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb}
&=\boldsymbol\nabla^{\mathsf V}_{R(a}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb)}
+\frac12\epsilon_{ab}
\boldsymbol\nabla_R^{\mathsf V c}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rc},\\
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b}
&=\bar{\boldsymbol\nabla}^{\mathsf V}_{R(\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b)}
+\frac12\epsilon_{\dot a\dot b}
\bar{\boldsymbol\nabla}_R^{\mathsf V\dot c}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot c},\\
{}[\boldsymbol{\mathcal D}^{\mathsf V}_{Ra\dot a},
\boldsymbol{\mathcal D}^{\mathsf V}_{Rb\dot b}]
={}&\rho_R\epsilon_{\dot a\dot b}
\boldsymbol\nabla^{\mathsf V}_{R(a}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb)}\\
&+\rho_R\epsilon_{ab}
\bar{\boldsymbol\nabla}^{\mathsf V}_{R(\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b)}.
\end{aligned}}
\tag{3C.44}
$$

Equations (3C.23), (3C.35), (3C.40), (3C.43), and
(3C.44) give explicitly

$$
\begin{array}{c|cc}
&L&E\\ \hline
\{\boldsymbol\nabla_a^{\mathsf V},\bar{\boldsymbol\nabla}_{\dot b}^{\mathsf V}\}
&2i\boldsymbol{\mathcal D}_{a\dot b}^{\mathsf V}
&-2\boldsymbol{\mathcal D}_{a\dot b}^{\mathsf V}\\
{}[\bar{\boldsymbol\nabla}_{\dot a}^{\mathsf V},
\boldsymbol{\mathcal D}_{b\dot b}^{\mathsf V}]
&-2i\epsilon_{\dot a\dot b}\boldsymbol{\mathcal W}_b^{\mathsf V}
&-2\epsilon_{\dot a\dot b}\boldsymbol{\mathcal W}_b^{\mathsf V}\\
{}[\boldsymbol\nabla_a^{\mathsf V},
\boldsymbol{\mathcal D}_{b\dot b}^{\mathsf V}]
&-2i\epsilon_{ab}\widetilde{\boldsymbol{\mathcal W}}_{\dot b}^{\mathsf V}
&-2\epsilon_{ab}\widetilde{\boldsymbol{\mathcal W}}_{\dot b}^{\mathsf V}
\end{array}.
\tag{3C.45}
$$

Lorentzian reality and Euclidean independence are

$$
\boxed{
\begin{gathered}
(\boldsymbol\nabla^{\mathsf V}_{La})^{\ddagger_L}
=-\bar{\boldsymbol\nabla}^{\mathsf V}_{L\dot a},
\qquad
(\boldsymbol{\mathcal W}^{\mathsf V}_{La})^{\ddagger_L}
=\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{L\dot a},\\
(\boldsymbol{\mathcal A}^{\mathsf V}_{La})^{\ddagger_L}
=\boldsymbol{\mathcal A}^{\mathsf V}_{L\dot a},
\qquad
(\boldsymbol{\mathcal A}^{\mathsf V}_{L\mu})^{\ddagger_L}
=\boldsymbol{\mathcal A}^{\mathsf V}_{L\mu},
\qquad
(\boldsymbol{\mathcal D}^{\mathsf V}_{L\mu})^{\ddagger_L}
=-\boldsymbol{\mathcal D}^{\mathsf V}_{L\mu}.
\end{gathered}}
\tag{3C.46}
$$

$$
\boxed{
(\boldsymbol{\mathcal W}^{\mathsf V}_E,
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_E),
\qquad
(\boldsymbol{\mathcal A}^{\mathsf V}_{Ea},
\boldsymbol{\mathcal A}^{\mathsf V}_{E\dot a})
\text{ are independent before the Euclidean contour}.}
\tag{3C.47}
$$

### 3C.5 Matter fields and action equivalence

Let

$$
\boldsymbol\Phi_R^{\mathsf V}{}'=k_R\boldsymbol\Phi_R^{\mathsf V},
\qquad
\widetilde{\boldsymbol\Phi}_R^{\mathsf V}{}'
=\widetilde{\boldsymbol\Phi}_R^{\mathsf V}k_R^{-1},
\tag{3C.48}
$$

with covariant chirality

$$
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
\boldsymbol\Phi_R^{\mathsf V}=0,
\qquad
(\boldsymbol\nabla^{\mathsf V}_{Ra})^{\rm row}
\widetilde{\boldsymbol\Phi}_R^{\mathsf V}=0.
\tag{3C.49}
$$

For

$$
\boldsymbol\nabla^{\mathsf V}_{R\mathfrak A}
=D_{R\mathfrak A}+\boldsymbol\Gamma^{\mathsf V}_{R\mathfrak A},
\qquad
\boldsymbol\Gamma^{\mathsf V}_{R\mathfrak A}
=\left(\boldsymbol\Gamma^{\mathsf V}_{R\mathfrak A}\right)^AT_A,
\tag{3C.50}
$$

the graded row action is

$$
\boxed{
(\boldsymbol\nabla^{\mathsf V}_{R\mathfrak A})^{\rm row}X
:=D_{R\mathfrak A}X
-(-1)^{|\mathfrak A||X|}
X\boldsymbol\Gamma^{\mathsf V}_{R\mathfrak A}.}
\tag{3C.51}
$$

Define the Step-3A fields by

$$
\boxed{
\Phi_R:=\mathcal B_R^{-1}\boldsymbol\Phi_R^{\mathsf V},
\qquad
\widetilde\Phi_R
:=\widetilde{\boldsymbol\Phi}_R^{\mathsf V}
\widetilde{\mathcal B}_R^{-1}.}
\tag{3C.52}
$$

Then

$$
\bar D_{R\dot a}\Phi_R=0,
\qquad
D_{Ra}\widetilde\Phi_R=0,
\tag{3C.53}
$$

and

$$
\begin{aligned}
\Phi_R'&=h_R\Phi_R,
&\widetilde\Phi_R'
&=\widetilde\Phi_R\widetilde h_R^{-1},\\
(\boldsymbol\Phi_L^{\mathsf V})^{\ddagger_L}
&=(\mathcal B_L\Phi_L)^{\ddagger_L}
=\widetilde\Phi_L\mathcal B_L^{\ddagger_L}
=\widetilde\Phi_L\widetilde{\mathcal B}_L
=\widetilde{\boldsymbol\Phi}_L^{\mathsf V},\\
(\boldsymbol\Phi_E^{\mathsf V},
\widetilde{\boldsymbol\Phi}_E^{\mathsf V})
&\text{ are independent before the Euclidean contour}.
\end{aligned}
\tag{3C.54}
$$

The canonical full-superspace density satisfies

$$
\boxed{
\begin{aligned}
\widetilde{\boldsymbol\Phi}_R^{\mathsf V}
\boldsymbol\Phi_R^{\mathsf V}
&=(\widetilde\Phi_R\widetilde{\mathcal B}_R)
(\mathcal B_R\Phi_R)\\
&=\widetilde\Phi_R\mathcal E_R\Phi_R.
\end{aligned}}
\tag{3C.55}
$$

For the general Step-3A Kähler density define

$$
\boxed{
\begin{aligned}
\mathscr K_R^{\mathsf V}
(\widetilde{\boldsymbol\Phi}^{\mathsf V},
\boldsymbol\Phi^{\mathsf V};
\widetilde{\mathcal B},\mathcal B)
:={}&\mathscr K_{g,R}
(\widetilde{\boldsymbol\Phi}^{\mathsf V}
\widetilde{\mathcal B}^{-1},
\mathcal B^{-1}\boldsymbol\Phi^{\mathsf V},
\widetilde{\mathcal B}\mathcal B).
\end{aligned}}
\tag{3C.56}
$$

Thus

$$
[\mathscr K_R^{\mathsf V}]_D
=[\mathscr K_{g,R}(\widetilde\Phi_R,\Phi_R,\mathcal E_R)]_D.
\tag{3C.57}
$$

Equations (3A.70) and (3A.71) imply, along every complexified gauge
orbit,

$$
\begin{gathered}
\frac d{dt}\mathscr U(e^{it\alpha^AT_A}\Phi)
=\alpha^AX_A^I\partial_I\mathscr U=0,\\
\widetilde X_{A,I}
:=-i\widetilde\Phi_J(T_A)^J{}_I,
\qquad
\widetilde\partial^I
:=\frac{\partial}{\partial\widetilde\Phi_I},\\
\frac d{dt}
\widetilde{\mathscr U}
(\widetilde\Phi e^{-it\alpha^AT_A})
=\alpha^A\widetilde X_{A,I}
\widetilde\partial^I\widetilde{\mathscr U}=0.
\end{gathered}
\tag{3C.58}
$$

$$
\begin{aligned}
\frac d{dt}
\left[
f_{AB}(e^{it\alpha^CT_C}\Phi)
(\operatorname{Ad}_{e^{it\alpha^CT_C}}W)^{Aa}
(\operatorname{Ad}_{e^{it\alpha^CT_C}}W)^B_a
\right]
={}&\alpha^C
\left[
X_C^I\partial_If_{AB}
-c_{CA}{}^Df_{DB}
-c_{CB}{}^Df_{AD}
\right]W^{Aa}W_a^B\\
={}&0,\\[4pt]
\frac d{dt}
\left[
\widetilde f_{AB}
(\widetilde\Phi e^{-it\alpha^CT_C})
(\operatorname{Ad}_{e^{it\alpha^CT_C}}\widetilde W)^A_{\dot a}
(\operatorname{Ad}_{e^{it\alpha^CT_C}}\widetilde W)^{B\dot a}
\right]
={}&\alpha^C
\left[
\widetilde X_{C,I}\widetilde\partial^I\widetilde f_{AB}
-c_{CA}{}^D\widetilde f_{DB}
-c_{CB}{}^D\widetilde f_{AD}
\right]
\widetilde W^A_{\dot a}\widetilde W^{B\dot a}\\
={}&0.
\end{aligned}
\tag{3C.59}
$$

Use the same holomorphic functions on vector-frame arguments:

$$
\boxed{
\begin{aligned}
\mathscr U_R^{\mathsf V}(X)&:=\mathscr U_R(X),
&f^{\mathsf V}_{R,AB}(X)&:=f_{R,AB}(X),\\
\widetilde{\mathscr U}_R^{\mathsf V}(\widetilde X)
&:=\widetilde{\mathscr U}_R(\widetilde X),
&\widetilde f^{\mathsf V}_{R,AB}(\widetilde X)
&:=\widetilde f_{R,AB}(\widetilde X),\\[2pt]
\mathscr U_R^{\mathsf V}(\boldsymbol\Phi_R^{\mathsf V})
&=\mathscr U_R(\Phi_R),
&\widetilde{\mathscr U}_R^{\mathsf V}
(\widetilde{\boldsymbol\Phi}_R^{\mathsf V})
&=\widetilde{\mathscr U}_R(\widetilde\Phi_R),\\
f^{\mathsf V}_{R,AB}(\boldsymbol\Phi_R^{\mathsf V})
(\boldsymbol{\mathcal W}_R^{\mathsf V})^{Aa}
(\boldsymbol{\mathcal W}_{Ra}^{\mathsf V})^B
&=f_{R,AB}(\Phi_R)
(\mathcal W_R^{\mathsf C})^{Aa}(\mathcal W_{Ra}^{\mathsf C})^B,\\
\widetilde f^{\mathsf V}_{R,AB}
(\widetilde{\boldsymbol\Phi}_R^{\mathsf V})
(\widetilde{\boldsymbol{\mathcal W}}_{R\dot a}^{\mathsf V})^A
(\widetilde{\boldsymbol{\mathcal W}}_R^{\mathsf V\dot a})^B
&=\widetilde f_{R,AB}(\widetilde\Phi_R)
(\widetilde{\mathcal W}_{R\dot a}^{\mathsf A})^A
(\widetilde{\mathcal W}_R^{\mathsf A\dot a})^B.
\end{aligned}}
\tag{3C.60}
$$

The flat Step-3A projectors apply because

$$
\begin{aligned}
\mathcal I_R^{\mathsf V}
&:=f^{\mathsf V}_{R,AB}
(\boldsymbol{\mathcal W}^{\mathsf V}_R)^{Aa}
(\boldsymbol{\mathcal W}^{\mathsf V}_{Ra})^B,\\
\widetilde{\mathcal I}_R^{\mathsf V}
&:=\widetilde f^{\mathsf V}_{R,AB}
(\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot a})^A
(\widetilde{\boldsymbol{\mathcal W}}_R^{\mathsf V\dot a})^B,\\
\bar D_{R\dot a}
\mathscr U_R^{\mathsf V}(\boldsymbol\Phi_R^{\mathsf V})
&=i(\boldsymbol\Gamma^{\mathsf V}_{R\dot a})^A
X_A^I\partial_I\mathscr U_R=0,\\
\bar D_{R\dot a}\mathcal I_R^{\mathsf V}
&=i(\boldsymbol\Gamma^{\mathsf V}_{R\dot a})^C
\left[
X_C^I\partial_If_{R,AB}
-c_{CA}{}^Df_{R,DB}
-c_{CB}{}^Df_{R,AD}
\right]
(\boldsymbol{\mathcal W}^{\mathsf V}_R)^{Aa}
(\boldsymbol{\mathcal W}^{\mathsf V}_{Ra})^B=0,\\
D_{Ra}\widetilde{\mathscr U}_R^{\mathsf V}
(\widetilde{\boldsymbol\Phi}_R^{\mathsf V})
&=i(\boldsymbol\Gamma^{\mathsf V}_{Ra})^A
\widetilde X_{A,I}\widetilde\partial^I
\widetilde{\mathscr U}_R=0,\\
D_{Ra}\widetilde{\mathcal I}_R^{\mathsf V}
&=i(\boldsymbol\Gamma^{\mathsf V}_{Ra})^C
\left[
\widetilde X_{C,I}\widetilde\partial^I\widetilde f_{R,AB}
-c_{CA}{}^D\widetilde f_{R,DB}
-c_{CB}{}^D\widetilde f_{R,AD}
\right]
(\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot a})^A
(\widetilde{\boldsymbol{\mathcal W}}_R^{\mathsf V\dot a})^B=0.
\end{aligned}
\tag{3C.60a}
$$

In particular,

$$
\operatorname{tr}
(\boldsymbol{\mathcal W}_R^{\mathsf V a}
\boldsymbol{\mathcal W}_{Ra}^{\mathsf V})
=\operatorname{tr}
(\mathcal W_R^{\mathsf C a}\mathcal W_{Ra}^{\mathsf C}).
\tag{3C.61}
$$

Set

$$
\varsigma_L:=+1,
\qquad
\varsigma_E:=-1,
\qquad
\xi_Ac_{BC}{}^A=0,
\qquad
\mathcal V_R:=\log(\widetilde{\mathcal B}_R\mathcal B_R),
\qquad
\xi_A(\log(\widetilde{\mathcal B}_R\mathcal B_R))^A
=\xi_A\mathcal V_R^A.
\tag{3C.62}
$$

The complete two-derivative vector-frame action is

$$
\boxed{
\begin{aligned}
S_R^{\mathsf V}=\varsigma_R\int d^4x_R\Big\{&
[\mathscr K_R^{\mathsf V}]_D
+[\mathscr U_R^{\mathsf V}(\boldsymbol\Phi_R^{\mathsf V})]_F
+[\widetilde{\mathscr U}_R^{\mathsf V}
(\widetilde{\boldsymbol\Phi}_R^{\mathsf V})]_{\widetilde F}\\
&+\frac14
[\mathcal I_R^{\mathsf V}]_F\\
&+\frac14
[\widetilde{\mathcal I}_R^{\mathsf V}]_{\widetilde F}\\
&+\xi_A[(\log(\widetilde{\mathcal B}_R\mathcal B_R))^A]_D
\Big\}.
\end{aligned}}
\tag{3C.63}
$$

Term by term,

$$
\boxed{S_R^{\mathsf V}=S_R^{\mathsf C},}
\tag{3C.64}
$$

where (S_L^{\mathsf C}) is (3A.67) and (S_E^{\mathsf C}) is (3A.93).

### 3C.6 Covariant components

Define vector-frame matter components by

$$
\boxed{
\begin{aligned}
\boldsymbol\phi_R^{\mathsf V}
&:=\boldsymbol\Phi_R^{\mathsf V}|,\\
\boldsymbol\psi_{Ra}^{\mathsf V}
&:=\frac1{\sqrt2}
\boldsymbol\nabla^{\mathsf V}_{Ra}\boldsymbol\Phi_R^{\mathsf V}|,\\
\boldsymbol F_R^{\mathsf V}
&:=-\frac14(\boldsymbol\nabla_R^{\mathsf V})^2
\boldsymbol\Phi_R^{\mathsf V}|,\\
(\boldsymbol\nabla_R^{\mathsf V})^2
&:=\boldsymbol\nabla_R^{\mathsf V a}
\boldsymbol\nabla^{\mathsf V}_{Ra}.
\end{aligned}}
\tag{3C.65}
$$

and

$$
\boxed{
\begin{aligned}
\widetilde{\boldsymbol\phi}_R^{\mathsf V}
&:=\widetilde{\boldsymbol\Phi}_R^{\mathsf V}|,\\
\widetilde{\boldsymbol\psi}_{R\dot a}^{\mathsf V}
&:=\frac1{\sqrt2}
(\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a})^{\rm row}
\widetilde{\boldsymbol\Phi}_R^{\mathsf V}|,\\
\widetilde{\boldsymbol F}_R^{\mathsf V}
&:=-\frac14
((\bar{\boldsymbol\nabla}_R^{\mathsf V})^{\rm row})^2
\widetilde{\boldsymbol\Phi}_R^{\mathsf V}|,\\
((\bar{\boldsymbol\nabla}_R^{\mathsf V})^{\rm row})^2
&:=(\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a})^{\rm row}
(\bar{\boldsymbol\nabla}_R^{\mathsf V\dot a})^{\rm row},
\qquad
\text{rightmost acts first}.
\end{aligned}}
\tag{3C.66}
$$

Define the covariant chiral-frame and antichiral-frame projections and
the bridge bottoms:

$$
\boxed{
\begin{gathered}
(\phi_R^{\mathsf C},\psi_{Ra}^{\mathsf C},F_R^{\mathsf C})
:=\left(
\Phi_R|,
\frac1{\sqrt2}\nabla^{\mathsf C}_{Ra}\Phi_R|,
-\frac14(\nabla_R^{\mathsf C})^2\Phi_R|
\right),\\
(\nabla_R^{\mathsf C})^2
:=\nabla_R^{\mathsf C a}\nabla^{\mathsf C}_{Ra},\\
(\widetilde\phi_R^{\mathsf A},
\widetilde\psi_{R\dot a}^{\mathsf A},
\widetilde F_R^{\mathsf A})
:=\left(
\widetilde\Phi_R|,
\frac1{\sqrt2}(\bar\nabla^{\mathsf A}_{R\dot a})^{\rm row}
\widetilde\Phi_R|,
-\frac14((\bar\nabla_R^{\mathsf A})^{\rm row})^2
\widetilde\Phi_R|
\right),\\
((\bar\nabla_R^{\mathsf A})^{\rm row})^2
:=(\bar\nabla^{\mathsf A}_{R\dot a})^{\rm row}
(\bar\nabla_R^{\mathsf A\dot a})^{\rm row},
\qquad
\text{rightmost acts first},\\
b_R:=\mathcal B_R|,
\qquad
\widetilde b_R:=\widetilde{\mathcal B}_R|.
\end{gathered}}
\tag{3C.67}
$$

similarity covariance gives

$$
\boxed{
\begin{gathered}
\boldsymbol\nabla^{\mathsf V}_{Ra}(\mathcal B_R\Phi_R)
=\mathcal B_R\nabla^{\mathsf C}_{Ra}\Phi_R,
\qquad
(\boldsymbol\nabla_R^{\mathsf V})^2(\mathcal B_R\Phi_R)
=\mathcal B_R(\nabla_R^{\mathsf C})^2\Phi_R,\\
(\boldsymbol\phi_R^{\mathsf V},
\boldsymbol\psi_R^{\mathsf V},
\boldsymbol F_R^{\mathsf V})
=b_R(\phi_R^{\mathsf C},\psi_R^{\mathsf C},F_R^{\mathsf C}).
\end{gathered}}
\tag{3C.68}
$$

$$
\boxed{
\begin{gathered}
((\bar{\boldsymbol\nabla}_{R\dot a}^{\mathsf V})^{\rm row}
(\widetilde\Phi_R\widetilde{\mathcal B}_R))
=((\bar\nabla_{R\dot a}^{\mathsf A})^{\rm row}
\widetilde\Phi_R)\widetilde{\mathcal B}_R,\\
(((\bar{\boldsymbol\nabla}_R^{\mathsf V})^{\rm row})^2
(\widetilde\Phi_R\widetilde{\mathcal B}_R))
=(((\bar\nabla_R^{\mathsf A})^{\rm row})^2
\widetilde\Phi_R)\widetilde{\mathcal B}_R,\\
(\widetilde{\boldsymbol\phi}_R^{\mathsf V},
\widetilde{\boldsymbol\psi}_R^{\mathsf V},
\widetilde{\boldsymbol F}_R^{\mathsf V})
=(\widetilde\phi_R^{\mathsf A},
\widetilde\psi_R^{\mathsf A},
\widetilde F_R^{\mathsf A})\widetilde b_R.
\end{gathered}}
\tag{3C.69}
$$

The vector-multiplet projections are

$$
\boxed{
\begin{aligned}
\boldsymbol\lambda_{Ra}^{\mathsf V}
&:=i\boldsymbol{\mathcal W}_{Ra}^{\mathsf V}|,\\
\widetilde{\boldsymbol\lambda}_{R\dot a}^{\mathsf V}
&:=-i\widetilde{\boldsymbol{\mathcal W}}_{R\dot a}^{\mathsf V}|,\\
\boldsymbol{\mathscr D}_R^{\mathsf V}
&:=-\frac12\boldsymbol\nabla_R^{\mathsf V a}
\boldsymbol{\mathcal W}_{Ra}^{\mathsf V}|\\
&=+\frac12\bar{\boldsymbol\nabla}_R^{\mathsf V\dot a}
\widetilde{\boldsymbol{\mathcal W}}_{R\dot a}^{\mathsf V}|,\\
\boldsymbol F_{RMN}^{\mathsf V}
&:=\boldsymbol{\mathcal F}^{\mathsf V}_{RMN}|,
\qquad
[\boldsymbol{\mathcal D}_{RM}^{\mathsf V},
\boldsymbol{\mathcal D}_{RN}^{\mathsf V}]
=-i\boldsymbol{\mathcal F}^{\mathsf V}_{RMN},\\
\mathcal F^{\mathsf C}_{R\mathfrak A\mathfrak B}
&:=\mathcal B_R^{-1}
\boldsymbol{\mathcal F}^{\mathsf V}_{R\mathfrak A\mathfrak B}
\mathcal B_R,
\qquad
\boldsymbol{\mathcal F}^{\mathsf V}_{R\mathfrak A\mathfrak B}
=\mathcal B_R
\mathcal F^{\mathsf C}_{R\mathfrak A\mathfrak B}
\mathcal B_R^{-1}.
\end{aligned}}
\tag{3C.70}
$$

In the symmetric bridge and Wess--Zumino gauge,

$$
\mathcal B_R|=\widetilde{\mathcal B}_R|=\mathbf1,
\qquad
\begin{gathered}
D_{Ra}\mathcal B_R|=
D_R^2\mathcal B_R|=
\bar D_{R\dot a}\mathcal B_R|=
\bar D_R^2\mathcal B_R|=0,\\
D_{Ra}\widetilde{\mathcal B}_R|=
D_R^2\widetilde{\mathcal B}_R|=
\bar D_{R\dot a}\widetilde{\mathcal B}_R|=
\bar D_R^2\widetilde{\mathcal B}_R|=0,\\
\Gamma^{\mathsf C}_{Ra}|=D_R^a\Gamma^{\mathsf C}_{Ra}|=0,
\qquad
\widetilde\Gamma^{\mathsf A}_{R\dot a}|=
\bar D_R^{\dot a}\widetilde\Gamma^{\mathsf A}_{R\dot a}|=0.
\end{gathered}
\tag{3C.71}
$$

Therefore

$$
\boxed{
\begin{gathered}
(\boldsymbol\phi_R^{\mathsf V},
\boldsymbol\psi_R^{\mathsf V},
\boldsymbol F_R^{\mathsf V})
=(\phi_R^{\mathsf C},\psi_R^{\mathsf C},F_R^{\mathsf C})
=(\phi_R,\psi_R,F_R),\\
(\widetilde{\boldsymbol\phi}_R^{\mathsf V},
\widetilde{\boldsymbol\psi}_R^{\mathsf V},
\widetilde{\boldsymbol F}_R^{\mathsf V})
=(\widetilde\phi_R^{\mathsf A},
\widetilde\psi_R^{\mathsf A},
\widetilde F_R^{\mathsf A})
=(\widetilde\phi_R,\widetilde\psi_R,\widetilde F_R),\\
(\boldsymbol\lambda_R^{\mathsf V},
\widetilde{\boldsymbol\lambda}_R^{\mathsf V},
\boldsymbol{\mathscr D}_R^{\mathsf V},
\boldsymbol F^{\mathsf V}_{RMN})
=(\lambda_R,\widetilde\lambda_R,
\mathscr D_R,F_{RMN}).
\end{gathered}}
\tag{3C.72}
$$

Thus the Step-3B component action is unchanged off shell.

### 3C.7 Wick transport

The bridge Wick map is defined by

$$
\boxed{
\begin{gathered}
\mathcal B_E:=\mathcal B_L|_{\rm Wick},
\qquad
\widetilde{\mathcal B}_E
:=\widetilde{\mathcal B}_L|_{\rm Wick},
\qquad
\mathcal E_E
=\widetilde{\mathcal B}_E\mathcal B_E,\\
\boldsymbol\nabla_E^{\mathsf V}
:=\boldsymbol\nabla_L^{\mathsf V}|_{\rm Wick},
\qquad
\bar{\boldsymbol\nabla}_E^{\mathsf V}
:=\bar{\boldsymbol\nabla}_L^{\mathsf V}|_{\rm Wick},\\
\boldsymbol{\mathcal W}_E^{\mathsf V}
:=\boldsymbol{\mathcal W}_L^{\mathsf V}|_{\rm Wick},
\qquad
\widetilde{\boldsymbol{\mathcal W}}_E^{\mathsf V}
:=\widetilde{\boldsymbol{\mathcal W}}_L^{\mathsf V}|_{\rm Wick}.
\end{gathered}}
\tag{3C.73}
$$

On the Wick image of the Lorentzian symmetric frame,

$$
\mathcal B_E=\widetilde{\mathcal B}_E
=e^{\mathcal V_E/2}.
\tag{3C.74}
$$

Equation (3C.74) is a contour and frame choice.  It is not an intrinsic
Euclidean adjoint relation.  Together with

$$
\boldsymbol{\mathcal D}^{\mathsf V}_{L0}
=i\boldsymbol{\mathcal D}^{\mathsf V}_{E4},
\qquad
\boldsymbol{\mathcal D}^{\mathsf V}_{Li}
=\boldsymbol{\mathcal D}^{\mathsf V}_{Ei},
\qquad
(\sigma_L^\mu\boldsymbol{\mathcal D}^{\mathsf V}_{L\mu})
=i\sigma_E^m\boldsymbol{\mathcal D}^{\mathsf V}_{Em},
\tag{3C.75}
$$

the Lorentz algebra (3C.44) maps exactly to its Euclidean counterpart
because

$$
\begin{aligned}
i\kappa_L&=i(2i)=-2=\kappa_E,
\qquad
\frac{u_L}{i}=\frac{-2i}{i}=-2=u_E,
\qquad
-\rho_L=-(-1)=+1=\rho_E,\\
\mathcal X_{R;a\dot a,b\dot b}
&:=\epsilon_{\dot a\dot b}
\boldsymbol\nabla^{\mathsf V}_{R(a}
\boldsymbol{\mathcal W}^{\mathsf V}_{Rb)}
+\epsilon_{ab}
\bar{\boldsymbol\nabla}^{\mathsf V}_{R(\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{R\dot b)},\\
{}[i\boldsymbol{\mathcal D}^{\mathsf V}_{Ea\dot a},
i\boldsymbol{\mathcal D}^{\mathsf V}_{Eb\dot b}]
&=-[\boldsymbol{\mathcal D}^{\mathsf V}_{Ea\dot a},
\boldsymbol{\mathcal D}^{\mathsf V}_{Eb\dot b}],\\
\rho_L\mathcal X_{L;a\dot a,b\dot b}|_{\rm Wick}
&=-\mathcal X_{E;a\dot a,b\dot b}
=-\rho_E\mathcal X_{E;a\dot a,b\dot b},\\
\boldsymbol{\mathfrak J}_R^{\mathsf V}
&:=\Big([\mathscr K_R^{\mathsf V}]_D,
[\mathscr U_R^{\mathsf V}(\boldsymbol\Phi_R^{\mathsf V})]_F,
[\widetilde{\mathscr U}_R^{\mathsf V}
(\widetilde{\boldsymbol\Phi}_R^{\mathsf V})]_{\widetilde F},\\
&\quad\frac14[\mathcal I_R^{\mathsf V}]_F,
\frac14[\widetilde{\mathcal I}_R^{\mathsf V}]_{\widetilde F},
\xi_A[\mathcal V_R^A]_D\Big),\\
\boldsymbol{\mathfrak J}_E^{\mathsf V}
&=\boldsymbol{\mathfrak J}_L^{\mathsf V}|_{\rm Wick},\\
\mathcal L_R^{\mathsf V}
&:=\varsigma_R\sum_{j=1}^{6}(\boldsymbol{\mathfrak J}_R^{\mathsf V})_j,
\qquad
\mathcal L_E^{\mathsf V}
&=\varsigma_E\sum_{j=1}^{6}(\boldsymbol{\mathfrak J}_E^{\mathsf V})_j
=-\mathcal L_L^{\mathsf V}|_{\rm Wick}.
\end{aligned}
\tag{3C.76}
$$

### 3C.8 Source-to-Project dictionary

The admitted source ranges are

$$
\begin{array}{c|c}
\text{source PDF pages}&\text{source equations}\\ \hline
177\text{--}180&(4.2.30)\text{--}(4.2.47)\\
182\text{--}186&(4.2.53)\text{--}(4.2.78)\\
187\text{--}188&(4.2.79)\text{--}(4.2.91)\\
190&(4.3.1),(4.3.2),(4.3.4)
\end{array}.
\tag{3C.77}
$$

The bridge dictionary is

$$
\boxed{
\begin{array}{c|c}
\text{Gates--Grisaru--Rocek--Siegel}&\text{Project}\\ \hline
e^{\Omega}&\widetilde{\mathcal B}_L\\
e^{\bar\Omega}&\mathcal B_L\\
e^V=e^{\Omega}e^{\bar\Omega}
&\mathcal E_L=\widetilde{\mathcal B}_L\mathcal B_L
=e^{\mathcal V_L}\\
e^{iK}&k_L\\
e^{i\Lambda}&h_L\\
e^{i\bar\Lambda}&\widetilde h_L\\
\Phi_0&\Phi_L\\
\Phi_{\rm vector}&\boldsymbol\Phi_L^{\mathsf V}
\end{array}.}
\tag{3C.78}
$$

The source field-strength definition in (4.2.45) is not used to fix a
Project coefficient.  The Project coefficients are fixed independently
by (3A.51)--(3A.55):

$$
\boxed{
\mathcal W_{Ra}^{\mathsf C}
=-\frac18\bar D_R^2
[\mathcal E_R^{-1}(D_{Ra}\mathcal E_R)],
\qquad
\widetilde{\mathcal W}_{R\dot a}^{\mathsf A}
=+\frac18D_R^2
[\mathcal E_R(\bar D_{R\dot a}\mathcal E_R^{-1})].}
\tag{3C.79}
$$

The source coordinate-similarity object (U) in (4.2.38)--(4.2.42)
has no gauge-bridge identification:

$$
U_{\rm source}
\longleftrightarrow
\text{Step-2A coordinate representation change},
\qquad
(\Omega,\bar\Omega,V)_{\rm source}
\longleftrightarrow
\text{Step-3C gauge-frame change}.
\tag{3C.80}
$$

The source equations (4.2.27)--(4.2.29), (4.2.48), and (4.3.3) are not
inputs to this contract.

### 3C.9 Verification surface

The exact verifier checks

$$
\begin{gathered}
\mathcal E_R=\widetilde{\mathcal B}_R\mathcal B_R,
\qquad
\mathcal E_R'=\widetilde h_R\mathcal E_Rh_R^{-1},\\
\mathcal B_R^{-1}\boldsymbol\nabla_R^{\mathsf V}\mathcal B_R
=\nabla_R^{\mathsf C},
\qquad
\widetilde{\mathcal B}_R\boldsymbol\nabla_R^{\mathsf V}
\widetilde{\mathcal B}_R^{-1}
=\nabla_R^{\mathsf A},\\
\widetilde{\boldsymbol\Phi}_R^{\mathsf V}\boldsymbol\Phi_R^{\mathsf V}
=\widetilde\Phi_R\mathcal E_R\Phi_R,
\qquad
\operatorname{tr}(\boldsymbol{\mathcal W}_R^{\mathsf V})^2
=\operatorname{tr}(\mathcal W_R^{\mathsf C})^2,\\
(\kappa_L,u_L,\rho_L)=(2i,-2i,-1),
\qquad
(\kappa_E,u_E,\rho_E)=(-2,-2,+1).
\end{gathered}
\tag{3C.81}
$$
