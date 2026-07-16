# GPT Pro Gate 12 response — original versus full measure

Status: `NON_AUTHORITY_PRO_REVIEW`.

## 1. Measure conversion

GPT Pro used the ordered (H)-endpoint basis in which

$$
D_H^2=2D_{H-}D_{H+},
\qquad
D_H^2\theta_H^2=-4.
$$

For

$$
Y=Y_0+\theta_{H+}Y_++\theta_{H-}Y_-+
\theta_{H+}\theta_{H-}Y_{+-},
$$

the endpoint projection gives

$$
D_H^2Y\big|_{\theta_H=0}=-2Y_{+-},
\qquad
\int d^2\theta_H,Y=\frac12Y_{+-},
$$

and therefore

$$
\int d^2\theta_H,Y
=-\frac14D_H^2Y\big|_{\theta_H=0}.
$$

If (D_{Ha}X=0), the two graded Leibniz signs cancel and

$$
D_H^2(XY)=X D_H^2Y.
$$

Hence

$$
\boxed{
\int d^2\bar\theta_H,X D_H^2Y\big|_{\theta_H=0}
=-4\int d^4\theta_H,XY.}
$$

Thus antichiral-to-full conversion removes one already present terminal
(D_H^2) and multiplies the word by (-4).  It does not multiply by
(-2).

## 2. Two adjacent-line presentations

For the (S-H) and (M-H) delta kernels,

$$
(D_S+D_H)\delta_{SH}=0,
\qquad
(D_M+D_H)\delta_{MH}=0,
$$

so the even square satisfies

$$
D_S^2\delta_{SH}=D_H^2\delta_{SH},
\qquad
D_M^2\delta_{MH}=D_H^2\delta_{MH}.
$$

Removing the terminal (D_H^2) from either the (S-H) projector or the
(M-H) projector gives

$$
W_F^{SH}(\sigma)=W_O(\sigma)=W_F^{MH}(\sigma),
\qquad
\sigma\in\{D_-\mathcal A,D_-\mathcal B\}.
$$

The two choices are presentations of one graph.  If both are retained in an
implementation, only the presentation average is legal:

$$
\frac12\left(W_F^{SH}(\sigma)+W_F^{MH}(\sigma)\right)=W_O(\sigma).
$$

## 3. Raw top coefficient

Let Ξ be the coefficient left after deleting one terminal (D_H^2).  The
direct original-measure replay gives

$$
[-2\Xi]_{\rm top}=32768W,
\qquad
[\Xi]_{\rm top}=-16384W.
$$

The full-measure word is (-4W), hence

$$
[-4W]_{\rm top}=-4(-16384W)=65536W.
$$

Therefore

$$
32768\longrightarrow65536,
$$

and the two measures give the same magnitude:

$$
c_O=32768\left(\frac14\right)_M\left(\frac12\right)_{\bar H}=4096,
$$

$$
c_F=65536\left(\frac14\right)_M\left(\frac14\right)_H=4096.
$$

At polynomial level, for either adjacent choice (j\in\{SH,MH\}),

$$
N_O^{(j)}(y,z;L)
=\frac12(-2)\Xi_j(y,z;L)
=-\Xi_j(y,z;L),
$$

$$
N_F^{(j)}(y,z;L)
=\frac14(-4)\Xi_j(y,z;L)
=-\Xi_j(y,z;L).
$$

Consequently

$$
N_O^{(j)}(y,z;L)-N_F^{(j)}(y,z;L)=0
$$

coefficientwise for arbitrary (y,z,L), including
((y,z)=(0,0)) and ((1/3,1/3)).

## 4. Supertrace cycles

The two nonzero block cycles are

$$
\mathcal C_1
=\operatorname{STr}(GM_2GH_-GI_{\phi_1u}),
\qquad
\mathcal C_2
=\operatorname{STr}(GH_-GM_2GI_{u\phi_1}).
$$

The mixed source Hessian and the two distinguishable action vertices give

$$
\mathcal C_2=\mathcal C_1,
\qquad
\frac12(\mathcal C_1+\mathcal C_2)=\mathcal C_1.
$$

The first false equality in the rejected route is

$$
\frac12(\mathcal C_1+\mathcal C_2)
\longrightarrow\frac12\mathcal C_1.
$$

It deletes the second nonzero cycle while retaining the outer (1/2).
Equivalently, a full-measure raw top of (32768) has replaced the required
(-4) conversion by (-2).

## 5. Verdict

$$
\boxed{c_{G_3}=4096.}
$$

$$
32768\left(\frac14\right)\left(\frac12\right)
=65536\left(\frac14\right)\left(\frac14\right)
=4096.
$$
