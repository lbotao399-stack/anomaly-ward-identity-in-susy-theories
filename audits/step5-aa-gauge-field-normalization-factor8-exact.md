# Step 5 \(AA\) gauge-field normalization and factor-eight audit

Status: PASS_AA_GAUGE_COORDINATE_NORMALIZATION__OLD_V_UNIT_PROPAGATOR_OVERCOUNT_FACTOR8__FULL_DWORD_COEFFICIENT_OPEN.

Scope: target-blind normalization only. The original-\(V\) quadratic Hessian and all coordinate-rescaling factors are locked. The corrected external-\(W_+\) index projection is included. The complete directed \(D\)-word sign is not inferred.

## 1. Original-\(V\) Hessian and inverse

The locked conditional Fermi--Feynman quadratic action is

$$
S_{E,V}^{(2)}
=\frac h4\int d^8z\,V^A\kappa_{AB}\Box_E V^B
=\frac12\int d^8z\,V^AK_{E,AB}^VV^B,
$$

$$
h=g^{-2},
\qquad
\boxed{K_{E,AB}^V=\frac h2\kappa_{AB}\Box_E.}
$$

Therefore

$$
(K_E^V)^{-1\,AB}
=2g^2\kappa^{AB}\Box_E^{-1},
$$

$$
K_E^V(K_E^V)^{-1}
=\frac h2(2g^2)\Box_E\Box_E^{-1}
=hg^2
=1.
$$

Since \(\Box_E\mapsto-p^2\),

$$
\boxed{
\langle V^A(p,1)V^B(-p,2)\rangle
=-\frac{2\hbar g^2}{p^2}\kappa^{AB}\delta^4(\theta_1-\theta_2).}
$$

For

$$
u=\frac{V}{\sqrt2g},
\qquad
v=\frac{V}{2g}=\frac{u}{\sqrt2},
$$

one obtains

$$
\boxed{\langle uu\rangle=-\frac{\hbar}{p^2},}
$$

$$
\boxed{\langle vv\rangle=-\frac{\hbar}{2p^2}.}
$$

Thus \(u\) has the unit propagator and \(v\) does not.

## 2. Original-\(V\) cubic gauge action

The exact expansion

$$
e^{-V}D_ae^V
=D_aV+\frac12[D_aV,V]+O(V^3)
$$

gives

$$
\mathcal W_a^{(1)}
=-\frac18\bar D^2D_aV,
$$

$$
\mathcal W_a^{(2)}
=-\frac1{16}\bar D^2[D_aV,V].
$$

Using the two symmetric cross terms in

$$
\frac h4\int d^2\theta\,\mathcal W^a\mathcal W_a
$$

and

$$
\int d^2\theta\,X\bar D^2Y=-4\int d^4\theta\,XY,
$$

the Euclidean chiral cubic is

$$
\boxed{
S_{E,+,3}^{V}
=-\frac h8\int d^8z\,
\mathcal W^{a}[D_aV,V].}
$$

Define \(\mathcal W=gW_c\) and \(V=ax\). Then

$$
S_{E,+,3}^{x}
=-\frac{a^2}{8g}\int d^8z\,
W_c^{a}[D_ax,x].
$$

The labeled action-Hessian magnitudes are

$$
\boxed{
|H_V|=\frac1{8g},
\qquad
|H_u|=\frac g4,
\qquad
|H_v|=\frac g2.}
$$

The two labeled quantum-port assignments are already contained in

$$
\delta_1\delta_2[Dx,x]
=[Dx_1,x_2]+[Dx_2,x_1].
$$

Hence no additional polarization factor \(2\) remains.

## 3. Source Hessian

Let

$$
A_c=g^{-1}\nabla_+\mathcal W_+.
$$

At linear order,

$$
A_c^{(1)}
=-\frac1{8g}D_+\bar D^2D_+V.
$$

For \(V=ax\),

$$
K_x=-\frac a{8g}D_+\bar D^2D_+,
$$

$$
D_-K_x
=-\frac a{16g}D^2\bar D^2D_+.
$$

The marked-unmarked source coefficient is

$$
\left(-\frac a{16g}\right)
\left(-\frac a{8g}\right)
=\frac{a^2}{128g^2}.
$$

The closed endpoint and two mixed anticommutators give

$$
16\cdot2\cdot2=64.
$$

Therefore

$$
\boxed{
w_S(V)=\frac1{2g^2},
\qquad
w_S(u)=1,
\qquad
w_S(v)=2.}
$$

The WW value

$$
w_D=\frac1{32}\cdot16\cdot2\cdot2=2
$$

is exactly the \(v\)-coordinate source weight.

## 4. Taylor and Wick multiplicities

For the mixed chiral-antichiral interaction,

$$
\frac1{2!}
\left(S_{+,3}S_{-,3}+S_{-,3}S_{+,3}\right)
=S_{+,3}S_{-,3}.
$$

Thus

$$
w_{\mathrm{Taylor}}=1.
$$

For one fixed directed port-preserving contraction,

$$
w_{\mathrm{Wick}}=1.
$$

The Hessian already contains its two labeled quantum-port assignments:

$$
w_{\mathrm{polarization\ after\ Hessian}}=1.
$$

## 5. Coordinate invariance

Suppressing the common color tensor and \(D\)-word, the exponent-vertex/propagator/source core is

$$
\mathcal N_x
=w_S(x)|H_x|^2
\frac{\langle xx\rangle^3}{\hbar^2}.
$$

For original \(V\),

$$
\mathcal N_V
=\frac1{2g^2}
\left(\frac1{8g}\right)^2
\frac{(-2\hbar g^2)^3}{\hbar^2}
=-\frac{\hbar g^2}{16}.
$$

For \(u\),

$$
\mathcal N_u
=1\left(\frac g4\right)^2
\frac{(-\hbar)^3}{\hbar^2}
=-\frac{\hbar g^2}{16}.
$$

For \(v\),

$$
\mathcal N_v
=2\left(\frac g2\right)^2
\frac{(-\hbar/2)^3}{\hbar^2}
=-\frac{\hbar g^2}{16}.
$$

Equivalently, relative to \(u\),

$$
\frac{w_S(v)}{w_S(u)}=2,
\qquad
\frac{|H_v|^2}{|H_u|^2}=4,
\qquad
\frac{\langle vv\rangle^3}{\langle uu\rangle^3}=\frac18,
$$

$$
\boxed{2\cdot4\cdot\frac18=1.}
$$

## 6. Earliest factor-eight conflict

Step-5 WW lines 443--445 use

$$
w_D=2,
$$

and lines 456--458 use

$$
\left(+\frac{ig}{2}\right)
\left(-\frac{ig}{2}\right)
=\frac{g^2}{4}.
$$

Both are the correct \(v=V/(2g)\) values.

For the same coordinate,

$$
\langle vv\rangle^3
=\left(-\frac{\hbar}{2p^2}\right)^3.
$$

However, Step-5 WW line 464 begins its loop coefficient with

$$
w_{\mathrm{Wick}}\frac{g^2}{4}w_D
$$

and omits the three-line normalization

$$
\left(\frac12\right)^3=\frac18.
$$

Hence the first wrong numerical step is Step-5 WW line 464, not the \(g/2\) Hessian and not \(w_D=2\):

$$
\frac{\mathcal N_{v,\mathrm{unit\ propagator}}}
{\mathcal N_{v,\mathrm{correct}}}
=\frac{
2(g^2/4)(-\hbar)^3/\hbar^2
}{
2(g^2/4)(-\hbar/2)^3/\hbar^2
}
=8.
$$

Thus, with the same old $D$-word held fixed, the unit-$v$-propagator WW arithmetic is larger than its consistently normalized version by exactly $8$.  This comparison does not fix the final AA gauge magnitude, because the old $D_+$ endpoint is independently rejected and the corrected $-D_-$ word has two nonzero selected edges.

## 7. Corrected external-\(W_+\) index

The abstract chiral Hessian contains

$$
W^\gamma(D_{C\gamma}-D_{U\gamma}).
$$

With

$$
W^-=-W_+,
$$

and only external \(W_+\) nonzero,

$$
\boxed{
W^\gamma(D_{C\gamma}-D_{U\gamma})
=-W_+(D_{C-}-D_{U-}).}
$$

Thus the action derivative is \(-D_-\), and

$$
H_{W_+}
=-\frac{ig}{4}W_+(D_{C-}-D_{U-}),
$$

$$
\tau_EH_{W_+}
=+\frac{ig}{4\hbar}W_+(D_{C-}-D_{U-}).
$$

This changes the projected chiral-vertex sign relative to treating the external \(W_+\) as \(W^\gamma D_\gamma=W_+D_+\). It does not change

$$
|H_u|=\frac g4
$$

or the factor-eight result.

Therefore coordinate normalization fixes only the field-rescaling factors.  It fixes neither the final magnitude nor the directed sign.  The old signed $-\lambda_1/8$ row requires a fresh ordered $D$-word replay with the action derivative $-D_-$ and occurrence-matched rank-one cuts.

## 8. Evidence boundary

The original-\(V\) quadratic evidence is

$$
\text{step-05a-component-bv-brst-primitive-supergraph-grammar.md:1053--1077}.
$$

The conflicting WW arithmetic is

$$
\text{step-05-euclidean-n4-awi-one-loop.md:437--466}.
$$

No holomorphic-twist coefficient enters this audit.  No full AA gauge coefficient is assigned.
