# GPT Pro Gate-BB12: ordered \(B_1>B_2\) one-loop DRED anomaly

Do an independent, target-blind, occurrence-resolved standard Feynman supergraph calculation for the ordered pair

$$
B_1^A B_2^B,
\qquad
B_r:=g^{-1}\nabla_+\Phi_r,
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

Do not infer any coefficient from the holomorphic-twist answer.  Derive every sign and rational factor.  The final HT row is disclosed only in the last section for comparison.

## 1. Locked Euclidean/DRED conventions

$$
Z_E=\int\mathcal D\Xi\,e^{-S_E/\hbar+\mathscr J_E/\hbar},
\qquad
V=\sqrt2g\,u,
\qquad
\Phi_r=g\phi_r,
\qquad
\widetilde\Phi_r=g\widetilde\phi_r.
$$

$$
d=4-2\epsilon,
\qquad
g_d=\bar g+\widetilde g,
\qquad
\operatorname{tr}\bar g=4,
\qquad
\operatorname{tr}\widetilde g=d-4=-2\epsilon,
$$

$$
\mu_\ell^2:=\bar\ell^2-\ell_d^2=-\widetilde\ell^2.
$$

For every selected inverse-kernel edge \(e\), use the pointwise full-dimensional Schwinger--Dyson identity

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}=0,
$$

and only afterwards form

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

There is no graph-specific extra \((4-d)\) factor.  The scalar master is

$$
\lim_{\epsilon\to0}\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

For

$$
r_0=\ell,
\qquad
r_1=\ell-p,
\qquad
r_2=\ell-p-q,
$$

derive all rank-one moments from the Feynman simplex.  In particular, check rather than assume

$$
2\int_{\Sigma_2}r_0
=\frac23p+\frac13q.
$$

The exact superspace conventions are

$$
D^2=2D_-D_+,
\qquad
\bar D^2=2\bar D_{\dot+}\bar D_{\dot-},
\qquad
D^2\bar D^2D^2=16\bar\Box D^2,
$$

$$
\delta^4(\theta)=4\theta^+\theta^-\bar\theta^{\dot+}\bar\theta^{\dot-},
\qquad
\int d^4\theta\,\delta^4(\theta)=1.
$$

Whenever a pure-antichiral endpoint projector has been omitted from an internal line, restore its exact endpoint word

$$
D^2\theta^2=-4.
$$

## 2. Locked vertices and propagators

The physical leading insertion is

$$
\mathcal O_{B_1B_2}^{(0),AB}
=g^2(D_+\phi_1)^A(D_+\phi_2)^B.
$$

The ordered action derivatives and exponent factors are

$$
C_{M_r^{(1)}}=-\sqrt2g\,T_U,
\qquad
\tau_EC_{M_r^{(1)}}=+\frac{\sqrt2g}{\hbar}T_U,
$$

$$
C_{H_-}=+\sqrt2g\,\varepsilon_{rst}c_{ABC},
\qquad
\tau_EC_{H_-}=-\frac{\sqrt2g}{\hbar}\varepsilon_{rst}c_{ABC}.
$$

Use

$$
\langle u^Au^B\rangle_E
=-\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_{12}),
$$

$$
\langle\phi_r^A\widetilde\phi_s^B\rangle_E
=\delta_{rs}\frac{\hbar\kappa^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\theta_{12}),
$$

with reversed chiral-line orientation derived explicitly rather than identified by reflection.

The color tensor is kept in the ordered form

$$
\mathbb F^{AB}{}_{DE}
=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E}.
$$

## 3. Descendant before any cancellation

Because \(|B_1|=|B_2|=1\), first write

$$
\nabla_-(B_1B_2)
=(\nabla_-B_1)B_2-B_1(\nabla_-B_2),
$$

$$
\nabla_-B_r
=-2\mathscr E_{\widetilde r}
-\sqrt2\varepsilon_{rst}(C_s\times C_t),
$$

$$
\mathscr E_{\widetilde r}
=-\frac14\nabla^2\Phi_r
-\frac1{\sqrt2}\varepsilon_{rst}(C_s\times C_t).
$$

It is forbidden to simplify

$$
-2\mathscr E_{\widetilde r}
-\sqrt2\varepsilon_{rst}(C_s\times C_t)
\longrightarrow \frac12\nabla^2\Phi_r
$$

before the regulated occurrence census.  Keep separately:

1. the full-Euler kinetic/potential occurrence;
2. the explicit superpotential contact occurrence;
3. every transported neighboring inverse-kernel occurrence;
4. nonlinear insertion terms from

$$
B_{r,c}=D_+\phi_r
+g\sqrt2[X,\phi_r]+g^2[C,\phi_r]+O(g^3);
$$

5. any quartic, gauge-fixing, ghost, auxiliary, or Jacobian occurrence allowed at the same one-loop order.

An algebraic cancellation is admissible only after both terms have identical occurrence tags, identical regulated kernels, and a displayed pointwise full-\(d\) equality.

## 4. Complete directed parent inventory for \(B_1>B_2\)

The cubic parent census contains exactly these three directed routes:

$$
\begin{array}{c|c|c|c}
\text{route}&\text{left vertex}&\text{right vertex}&\text{topology}\\\hline
001&M_1[0,1]&M_2[0,1]&TMM\\
002&M_1[0,2]&H_-[1,0]&TMH\\
003&H_-[0,1]&M_2[0,2]&TMH
\end{array}
$$

For route 002 the ports are

$$
\begin{aligned}
&B_1\text{ source }\phi_1\to M_1.\widetilde\phi_1,\\
&M_1.\phi_1\to H_-.\widetilde\phi_1,\\
&B_2\text{ source }\phi_2\to H_-.\widetilde\phi_2,\\
&\text{external }u^D\text{ at }M_1,\qquad
\widetilde\phi_3^E\text{ at }H_-.
\end{aligned}
$$

Thus route 002 must be projected onto the two independent ordered carriers

$$
\langle D^D,C_3^E\rangle,
\qquad
\langle C_3^D,D^E\rangle,
$$

without quotienting by total derivatives or exchanging \(D,E\).  Route 003 must be recomputed with reversed ports and graded source order; do not infer it by reflection.

## 5. Local finite-Grassmann data to audit, not to trust

An unfinished independent sparse-Grassmann replay of route 002 found:

* the outer mark on the \(M_1\)-source \(B_1\) edge gives zero;
* the outer mark on the \(H_-\)-source \(B_2\) edge gives, before the omitted antichiral endpoint \(-4\),

$$
R_{\dot1}^{\rm raw}
=-1024\,r_{0,+\dot2}\det r_2,
\qquad
R_{\dot2}^{\rm raw}
=+1024\,r_{0,+\dot1}\det r_2;
$$

* after removing the selected square, the residual word is

$$
(-128r_{0,+\dot2},\,+128r_{0,+\dot1});
$$

* the primitive normalization before the \(D\)-word is tentatively

$$
g^2
\left(+\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left(\frac{\hbar}{16}\right)^3
=-\frac{\hbar g^4}{2048},
$$

before the exact flavor/color/Koszul sign;

* a probe

$$
u_{\dot a}=\theta^+\theta^-\bar\theta_{\dot a}
$$

satisfies

$$
D^2\bar D_{\dot a}u_{\dot a}\big|=-2,
$$

whereas the physical external map is

$$
D^2\bar D_{\dot a}u\big|
=-\frac{4\sqrt2}{g}D_{\dot a},
\qquad
C_3=g\widetilde\phi_3.
$$

Recompute all of these lines.  If any line fails, identify the first failed operator word and replace it with a complete expansion.

## 6. Required output

Produce a graph/occurrence table with one row for every parent, Euler term, explicit potential contact, nonlinear insertion, transported inverse edge, bubble, quartic, gauge-fixing/ghost, auxiliary, and Jacobian occurrence.  Every row must display:

$$
(\text{route id},\ \text{outer mark},\ \text{ports},\ \text{color/flavor},\ \text{raw }D\text{-word},\ r_e,
\ \text{full-}d\text{ SD contact},\ \mu_\ell^2\text{ remainder},\ \text{simplex moment},\ \text{normalized output}).
$$

Explicitly prove:

1. the exact-zero or nonzero status of route 001;
2. both outer marks of route 002;
3. both outer marks of independently routed route 003;
4. the \(-4\) endpoint factor;
5. the \(1/3,2/3\) rank-one weights;
6. the complete regulated Euler/potential/contact cancellation or remainder;
7. the exact final coefficient vector in the ordered basis

$$
\left(
\langle D^D,C_3^E\rangle,
\langle C_3^D,D^E\rangle
\right).
$$

Do not use \(\sim\), \(\approx\), ``proportional to'', an unexplained overall constant, or a target-fitted normalization.

## 7. Sealed comparison target

Only after the complete Feynman coefficient vector has been derived, compare it with the conditional HT row

$$
\Delta(B_1,B_2)
=-i\sqrt2
\left(
\langle D^D,C_3^E\rangle
-\langle C_3^D,D^E\rangle
\right)
$$

in units of \(\lambda_1\mathbb F^{AB}{}_{DE}\).  A mismatch must remain a mismatch with the first unresolved occurrence or normalization line named; it may not be removed by rescaling the answer.
