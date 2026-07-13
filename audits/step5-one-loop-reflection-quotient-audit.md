# Step 5 one-loop reflection / physical quotient verification

## 0. Definitions

$$
X^A:=(\nabla_+\mathcal W_+)^A,\qquad |X|=0,
\qquad Y^{A\dot a}:=\mathcal D_+{}^{\dot a}X^A,\qquad |Y|=0.
$$

$$
\mathcal D_+{}^{\dot a}:=
\epsilon^{\dot a\dot b}\mathcal D_{+\dot b},\qquad
|\mathcal D_{a\dot a}|=0.
$$

$$
F_{ABDE}:=c_{ACD}c_{BCE},\qquad
S^{DE}:=\widetilde{\mathcal W}_{\dot a}^D Y^{E\dot a}.
$$

## 1. Dotted variance

$$
\epsilon^{\dot1\dot2}=+1,\qquad
\epsilon_{\dot1\dot2}=-1,\qquad
Y^{\dot a}=\epsilon^{\dot a\dot b}Y_{\dot b}.
$$

For $W_{\dot a}=(w_1,w_2)$ and $Y_{\dot a}=(y_1,y_2)$,

$$
\begin{aligned}
W_{\dot a}Y^{\dot a}&=w_1y_2-w_2y_1,\\
Y^{\dot a}W_{\dot a}&=w_1y_2-w_2y_1,\\
Y_{\dot a}W^{\dot a}&=y_1w_2-y_2w_1
=-(w_1y_2-w_2y_1).
\end{aligned}
$$

The locked lower `TildeW` port is retained as `DOWN` in GraphIR and
in every scheduled numerator factor.
The $D$-algebra token is $ip_{a\dot b}$; its covariant completion is
$\mathcal D_{a\dot b}$.  The legacy symbol
$\nabla_+{}^{\dot a}X$ is type-invalid because $\nabla_+$ is an
undotted odd spinor derivative and has no dotted output.

## 2. Local two-letter quotient

$$
\begin{aligned}
\nabla_-(X^AX^B)
&=(\nabla_-X^A)X^B+X^A(\nabla_-X^B)\\
&=(\nabla_-X^A)X^B+(\nabla_-X^B)X^A\\
&=\nabla_-(X^BX^A).
\end{aligned}
$$

$$
\mathscr I^{AB}=\mathscr I^{BA},\qquad
\mathscr I\in\operatorname{Sym}^2(\operatorname{Adj}).
$$

$$
|\mathscr I|=|\nabla_-|+2|X|=1,\qquad
|J_{(AB)}|=1,\qquad |J_{(AB)}\mathscr I^{AB}|=0.
$$

The GraphIR source field is typed `FERMION`; the coupled insertion vertex is even.

In momentum space the exact exchange is $(A,p_1)\leftrightarrow(B,p_2)$.

## 3. Reflected orientation

Both GraphIR orientations have

$$
\operatorname{Ord}(v_I,v_{\widetilde W},v_W)
=(I,\widetilde W,W),\qquad
\operatorname{Word}_{\rm ext}=(\widetilde W,W).
$$

$$
|v_{J\mathscr I}|=|v_{\widetilde W}|=|v_W|=0,\qquad |V|=0.
$$

Therefore

$$
s_{\rm ref}^{\rm fixed\ vertex\ order}=+1.
$$

The reflected audit records the external subword permutation

$$
(\widetilde W,W)\longmapsto(W,\widetilde W)
\longmapsto-(\widetilde W,W),
$$

and separately records the odd quantum-word permutation.

The complete cubic blocks are

$$
B_{\widetilde W}=\widetilde W\,Q_{\bar D},\qquad
B_W=W\,Q_D,\qquad
|\widetilde W|=|Q_{\bar D}|=|W|=|Q_D|=1,
$$

so $|B_{\widetilde W}|=|B_W|=0$.  Full block reflection gives

$$
(W,Q_D,\widetilde W,Q_{\bar D})
\longmapsto
(\widetilde W,Q_{\bar D},W,Q_D):
\qquad (-1)^4=+1.
$$

Separating the same permutation gives

$$
s_{\rm ext}=(-1)^1=-1,\qquad
s_{\rm quantum}=(-1)^1=-1,\qquad
s_{\rm full}=s_{\rm ext}s_{\rm quantum}=+1.
$$

The specialized compiler retains both sub-signs and uses their product.

## 4. Color swap and projection

Let $s_{\rm ref}=s$. Then

$$
\mathscr O_s^{AB}=F_{ABDE}(S^{DE}+sS^{ED}).
$$

Using $F_{BADE}=F_{ABED}$ and then $D\leftrightarrow E$ gives

$$
\mathscr O_s^{BA}=F_{ABDE}(S^{ED}+sS^{DE})=s\mathscr O_s^{AB}.
$$

Rejected external-only sign:

$$
s=-1:\qquad
\mathscr O_-^{BA}=-\mathscr O_-^{AB},\qquad
P_{\rm Sym^2}\mathscr O_-=0.
$$

Fixed ordered-GraphIR sign:

$$
s=+1:\qquad
\boxed{
\mathscr O_+^{AB}=c_{ACD}c_{BCE}
\left[
\widetilde{\mathcal W}_{\dot a}^D
\mathcal D_+{}^{\dot a}X^E
+(\mathcal D_+{}^{\dot a}X^D)
\widetilde{\mathcal W}_{\dot a}^E
\right]},
\qquad \mathscr O_+^{BA}=\mathscr O_+^{AB}.
$$

## 5. Verdict

$$
\boxed{\texttt{PASS\_REFLECTION\_SOURCE\_DERIVATIVE\_TYPE\_GATES}}.
$$

- `TYPED_CONTACT_REPLAY_AFTER_REPAIR`: OPEN.
- `anomaly coefficient`: INVALIDATED_NOT_PROPAGATED.

Exact checks: 26/26; loop coefficient not evaluated.
