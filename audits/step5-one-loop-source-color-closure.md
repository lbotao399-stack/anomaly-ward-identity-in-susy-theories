# Step 5 odd local source and color-quotient closure

## 1. Background Chevalley--Eilenberg lift

$$
M:=\operatorname{Sym}^2(\operatorname{Adj}),
\qquad
\mathscr I\in\Pi M,
\qquad
J\in\Pi M^\vee,
\qquad
|\Gamma|=|\mathscr I|=|J|=1.
$$

$$
\rho_2(t)
=\rho_{\rm ad}(t)\otimes\mathbf1
+\mathbf1\otimes\rho_{\rm ad}(t),
\qquad
\Gamma:=c^a\rho_2(t_a).
$$

$$
\boxed{
s_{\rm B}\Gamma=\Gamma^2,
\qquad
s_{\rm B}\mathscr I=\Gamma\mathscr I,
\qquad
s_{\rm B}J=J\Gamma.}
$$

$$
\begin{aligned}
s_{\rm B}^2\mathscr I
&=(s_{\rm B}\Gamma)\mathscr I
-\Gamma(s_{\rm B}\mathscr I)\\
&=\Gamma^2\mathscr I-\Gamma^2\mathscr I=0,\\
s_{\rm B}^2J
&=(s_{\rm B}J)\Gamma-J(s_{\rm B}\Gamma)\\
&=J\Gamma^2-J\Gamma^2=0,\\
s_{\rm B}(J\mathscr I)
&=(s_{\rm B}J)\mathscr I-J(s_{\rm B}\mathscr I)\\
&=J\Gamma\mathscr I-J\Gamma\mathscr I=0.
\end{aligned}
$$

## 2. Local source jets

$$
\mathcal D\mathscr I:=d\mathscr I+A\mathscr I,
\qquad
\mathcal D^\vee J:=dJ-JA,
$$

$$
s_{\rm B}A=-d\Gamma+\Gamma A-A\Gamma.
$$

$$
\begin{aligned}
s_{\rm B}(\mathcal D\mathscr I)
&=d(\Gamma\mathscr I)
+(-d\Gamma+\Gamma A-A\Gamma)\mathscr I
+A\Gamma\mathscr I\\
&=(d\Gamma)\mathscr I+\Gamma d\mathscr I
-(d\Gamma)\mathscr I+\Gamma A\mathscr I
-A\Gamma\mathscr I+A\Gamma\mathscr I\\
&=\Gamma(d\mathscr I+A\mathscr I)
=\Gamma\mathcal D\mathscr I,
\end{aligned}
$$

$$
\begin{aligned}
s_{\rm B}(\mathcal D^\vee J)
&=d(J\Gamma)-(J\Gamma)A
+J(-d\Gamma+\Gamma A-A\Gamma)\\
&=(dJ)\Gamma+Jd\Gamma-J\Gamma A
-Jd\Gamma+J\Gamma A-JA\Gamma\\
&=(dJ-JA)\Gamma
=(\mathcal D^\vee J)\Gamma.
\end{aligned}
$$

Hence every iterated covariant source jet closes by induction.

For the local-source (W\widetilde W\nabla\mathcal D) block, use

$$
\mathcal B_{\rm loc}
=(C_{\rm on\,W},C_{\rm split},S_{\mathcal D J}).
$$

Integrated source IBP and the pointwise antichiral EOM give

$$
C_{\rm on\,W}+C_{\rm split}+S_{\mathcal D J}=0,
$$

$$
C_{\rm split}
=\mathcal D_a{}^{\dot a}\widetilde{\mathcal W}_{\dot a}
=-\frac12\nabla_a\overline{\mathcal E}=0.
$$

$$
R_{\rm loc}
=\begin{pmatrix}
1&1&1\\
0&1&0
\end{pmatrix},
\qquad
\operatorname{rank}R_{\rm loc}=2,
$$

$$
\operatorname{rref}R_{\rm loc}
=\begin{pmatrix}
1&0&1\\
0&1&0
\end{pmatrix}.
$$

$$
\boxed{
\dim(\mathcal B_{\rm loc}/\operatorname{row}R_{\rm loc})=1,
\qquad
C_{\rm split}=0,
\qquad
S_{\mathcal D J}=-C_{\rm on\,W}.}
$$

The source momentum is retained:

$$
p_J+p_W+p_{\widetilde W}=0,
\qquad
p_J\ne0.
$$

## 3. Color quotient

Let (C:=\operatorname{Adj}\otimes\operatorname{Adj}) and

$$
M:=C/\Lambda^2(\operatorname{Adj})
=\operatorname{Sym}^2(\operatorname{Adj}).
$$

The surviving ordered-port jet is

$$
\iota_M:M\longrightarrow M\oplus M,
\qquad
\iota_M(m)=(m,-m).
$$

Define

$$
\pi_1:M\oplus M\longrightarrow M,
\qquad
\pi_1(u,v)=u.
$$

Then

$$
\boxed{
\pi_1\iota_M=\operatorname{id}_M,
\qquad
\ker\iota_M=0.}
$$

More generally, this proof survives every color relation quotient
(q:C\to C/R) applied to the source and separately to both output copies.

It does not survive an arbitrary larger target quotient.  For

$$
M=\mathbb Q,
\qquad
\iota_M(1)=(1,-1),
$$

quotienting the target by (\operatorname{span}(1,-1)) sends the jet to zero.

## 4. Boundary

$$
\boxed{
\text{background-CE odd source and local jets}=\texttt{PASS},
\qquad
\text{color }\operatorname{Sym}^2\text{ quotient}=\texttt{PASS}.}
$$

$$
\boxed{
\text{full quantum BV Slavnov source complex}
=\texttt{FAIL\_CLOSED}.}
$$

Step 3D defines the ordinary linear source as inert under
(\mathbf s_{R,\nu}^{\rm all}).  The Step-5 composite-source antifields,
source partners, and the linearized Slavnov mixing matrix are not defined.
Background covariance therefore does not determine the full source-linear
BV cohomology.  No loop coefficient is accepted.

## 5. Status patches for the aggregate audits

$$
\begin{array}{c|c}
\text{gate}&\text{replacement status}\\ \hline
G5&
\texttt{PASS\_BACKGROUND\_CE\_SOURCE\_JETS;
FULL\_BV\_ST\_FAIL\_CLOSED}\\
G9\text{ color}&
\texttt{PASS\_SPLIT\_MONOMORPHISM}\\
G9\text{ local }W\widetilde W\nabla\mathcal D&
\texttt{PASS\_RANK2\_QUOTIENT\_DIM1}\\
\ker\bar\ell_2=0&
\texttt{NOT\_ESTABLISHED\_BY\_THIS\_CERTIFICATE}
\end{array}
$$

The theorem status remains conditional.  Its source-BV and DRED gates remain
separate from the closed color quotient.
