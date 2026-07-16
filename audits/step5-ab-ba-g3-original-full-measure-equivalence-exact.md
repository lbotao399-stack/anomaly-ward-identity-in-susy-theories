# G3 original/full measure equivalence exact audit

Status: PASS_G3_ORIGINAL_FULL_MEASURE_EQUIVALENCE__CONVERSION_MAGNITUDE_FOUR__TWO_SUPERTRACE_CYCLES_CANCEL_HALF__C_G3_4096.

No HT coefficient or desired output is used.

## 1. Measure coefficient

The sparse engine orders the H-vertex generators as

$$
(\theta_{H+},\theta_{H-},
\bar\theta_{H\dot +},\bar\theta_{H\dot -}),
$$

and uses

$$
D_H^2=2D_{H-}D_{H+}.
$$

Direct left differentiation gives

$$
D_{H+}(\theta_{H+}\theta_{H-})=\theta_{H-},
$$

$$
D_{H-}D_{H+}(\theta_{H+}\theta_{H-})=1,
$$

$$
D_H^2(\theta_{H+}\theta_{H-})=2.
$$

The canonical monomial maps are

$$
\int d^2\bar\theta_H\,
\bar\theta_{H\dot +}\bar\theta_{H\dot -}
=\frac12,
$$

$$
\int d^4\theta_H\,
\theta_{H+}\theta_{H-}
\bar\theta_{H\dot +}\bar\theta_{H\dot -}
=\frac14.
$$

Therefore

$$
\frac12\cdot2=1,
$$

$$
4\cdot\frac14=1,
$$

and

$$
\boxed{
\int d^2\bar\theta_H\,
(D_H^2K)\big|_{\theta_H=0}
=4\int d^4\theta_H\,K.
}
$$

The ordered-H orientation with coefficient $-4$ has

$$
\Xi_{\mathrm{ordered}\ H}=-\Xi_{\mathrm{engine}},
$$

so

$$
(-4)\Xi_{\mathrm{ordered}\ H}
=(-4)(-\Xi_{\mathrm{engine}})
=4\Xi_{\mathrm{engine}}.
$$

Thus only the intermediate orientation sign differs.

## 2. Coefficientwise Grassmann equality

Define

$$
\mathcal A=D_+\bar D^2D_+\delta_{SM},
$$

$$
\mathcal B=D_+\bar D^2D^2\delta_{SH},
$$

$$
\mathcal P_{MH}=\bar D_M^2D_M^2\delta_{MH}.
$$

For

$$
\sigma\in\{D_-\mathcal A,D_-\mathcal B\},
$$

let $N_O$ use $d^2\bar\theta_H$.  Let $N_F^{MH}$ delete the
terminal $D_M^2$ from $\mathcal P_{MH}$, and let $N_F^{SH}$ delete the
terminal $D_S^2$ from the S-H projector.  Multiplying either deleted word
by the conversion coefficient gives

$$
N_O-N_F^{MH}=0,
$$

$$
N_O-N_F^{SH}=0.
$$

Both equalities hold coefficientwise in every remaining M-vertex
Grassmann monomial, with arbitrary loop components, at

$$
(y,z)=(0,0),
$$

and

$$
(y,z)=\left(\frac13,\frac13\right).
$$

The JSON artifact stores every nonzero coefficient and both zero
difference dictionaries.

## 3. Raw metric chain

The two original raw top coefficients are

$$
c_{O,A}^{\mathrm{raw}}=32768(1-z),
$$

$$
c_{O,B}^{\mathrm{raw}}=32768z.
$$

Deleting either terminal $D_H^2$ gives

$$
c_{\Xi,A}^{\mathrm{raw}}=16384(1-z),
$$

$$
c_{\Xi,B}^{\mathrm{raw}}=16384z.
$$

The full-measure conversion gives

$$
c_{F,A}^{\mathrm{raw}}
=4\cdot16384(1-z)
=65536(1-z),
$$

$$
c_{F,B}^{\mathrm{raw}}
=4\cdot16384z
=65536z.
$$

Hence

$$
32768\left(\frac14\right)_M
\left(\frac12\right)_{\bar H}
=4096,
$$

$$
65536\left(\frac14\right)_M
\left(\frac14\right)_H
=4096.
$$

The rejected coefficient $2$ gives

$$
2\cdot16384
\left(\frac14\right)_M
\left(\frac14\right)_H
=2048.
$$

The marked simplex moments are

$$
w_A=\frac23,
\qquad
w_B=\frac13,
\qquad
w_A+w_B=1.
$$

## 4. Supertrace cycles

In the basis

$$
(u,\phi_1,\widetilde\phi_1,\phi_s,\widetilde\phi_s),
$$

the exhaustive oriented-block census has $16$ candidates and exactly two
nonzero cycles:

$$
\mathcal C_1
=\operatorname{STr}
(G M_2 G H_- G I_{\phi_1u}),
$$

$$
\mathcal C_2
=\operatorname{STr}
(G H_- G M_2 G I_{u\phi_1}).
$$

The reverse even Hessian blocks give

$$
\mathcal C_1
=G_uG_1G_sI_0M_2H_-,
$$

$$
\mathcal C_2
=G_uG_1G_sI_0M_2H_-.
$$

Therefore

$$
\frac12(\mathcal C_1+\mathcal C_2)
=\frac12(2\mathcal C_1)
=\mathcal C_1.
$$

The rejected route first uses

$$
\boxed{
\frac12(\mathcal C_1+\mathcal C_2)
\longrightarrow
\frac12\mathcal C_1.
}
$$

Equivalently, its full-measure ledger replaces $4$ by $2$.  These are the
same missing factor, not two independent halves.

$$
\boxed{c_{G_3}=4096.}
$$

Checks: 53/53 PASS.
