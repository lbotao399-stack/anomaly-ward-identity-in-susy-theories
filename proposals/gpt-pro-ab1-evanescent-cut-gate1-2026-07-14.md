# GPT Pro Gate 1 — evanescent cutting failure

- date: 2026-07-14
- status: NON_AUTHORITY_PRO_REVIEW
- gate: initial
- authority: none; every material claim requires Project-side adjudication
- prompt: `/Users/libotao/.codex/procodex/awi-evanescent-cut-gate1.md`
- local authority pin: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`

The audit concerns only the ordered one-loop triangle/cut defect, defined as the difference between regulated loop contraction and four-dimensional spin-algebra cutting. Pasted text

## A. Evanescent split and sign

Introduce a distinct physical four-dimensional projector $\bar g^{mn}$ and a $d$-dimensional integration metric $g_d^{mn}$:

$$
g_d^{mn}=\bar g^{mn}+\widetilde g^{mn},
$$

$$
\bar g^m{}_m=4,
\qquad
\widetilde g^m{}_m=d-4=-2\epsilon,
\qquad
\bar g\widetilde g=0.
$$

Define

$$
\bar\ell^{\,2}:=\bar g_{mn}\ell^m\ell^n,
\qquad
\widetilde\ell^{\,2}:=\widetilde g_{mn}\ell^m\ell^n,
\qquad
\ell_d^2:=g_{d,mn}\ell^m\ell^n.
$$

Then exactly

$$
\boxed{
\ell_d^2=\bar\ell^{\,2}+\widetilde\ell^{\,2}
}
$$

and therefore

$$
\boxed{
\widetilde\ell^{\,2}
=
\ell_d^2-\bar\ell^{\,2}.
}
$$

Hence the object with $d-4$ trace is

$$
\boxed{
\widetilde\ell^{\,2}
=
\ell_d^2-\bar\ell^{\,2}.
}
$$

The numerator appearing in triangle-minus-cut is its negative:

$$
\boxed{
\mu_\varepsilon^2
:=
\bar\ell^{\,2}-\ell_d^2
=
-\widetilde\ell^{\,2}.
}
$$

Thus the proposed definition

$$
\widehat\ell^{\,2}
=
\bar\ell^{\,2}-\ell_d^2
$$

is algebraically usable, but it has effective trace $4-d$, not $d-4$. If $\widehat\ell^{\,2}$ is intended to mean the genuine $d-4$ component, its sign must be reversed:

$$
\boxed{
\widehat\ell^{\,2}_{d-4}
=
\ell_d^2-\bar\ell^{\,2},
\qquad
\mu_\varepsilon^2
=
-\widehat\ell^{\,2}_{d-4}.
}
$$

### Compatibility with the frozen DRED convention

The previously frozen convention was

$$
\delta_4^{mn}
=
\widehat\delta^{mn}
+
\breve\delta^{mn},
\qquad
\widehat\delta^m{}_m=d,
\qquad
\breve\delta^m{}_m=4-d,
$$

$$
\ell^m=\widehat\delta^m{}_n\ell^n,
\qquad
\breve\delta^m{}_n\ell^n=0.
$$

Under that convention,

$$
\delta_{4,mn}\ell^m\ell^n
=
\widehat\delta_{mn}\ell^m\ell^n
=
\ell_d^2.
$$

Therefore, if

$$
\bar\ell^{\,2}
:=
\delta_{4,mn}\ell^m\ell^n,
$$

then

$$
\boxed{
\bar\ell^{\,2}-\ell_d^2=0.
}
$$

This is also the defining inverse-propagator property of consistent DRED: the $d$-dimensional momentum space is embedded as a subspace of Q4S so that the Q4S slash operator remains the inverse of the $d$-dimensional propagator. ar5iv

Therefore the nonzero scalar mechanism requires one additional regulator axiom:

$$
\boxed{
\text{The finite superspace }\sigma\text{-word contracts with a distinct }
\bar g^{mn},
\quad
g_d=\bar g+\widetilde g.
}
$$

It does not follow from the earlier frozen split by itself; that continuation was explicitly left unfixed. Pasted text

---

## B. Exact triangle-minus-cut algebra

Let the three internal denominators be

$$
D_i=r_{i,d}^{\,2},
\qquad
r_i=k+Q_i,
$$

with all $Q_i$ physical four-dimensional external momenta. Shift $k$ so that

$$
Q_0=0,
\qquad
r_0=k.
$$

Let $\mathcal P_\Gamma$ denote the complete source, vertex, propagator-sign, Wick, color, flavor and orientation factor, and let $\mathcal O_\Gamma$ denote the residual external operator.

Suppose the D-word selects

$$
N_D=\bar r_0^{\,2}.
$$

The triangle is

$$
\mathcal T_0
=
\mathcal P_\Gamma\mathcal O_\Gamma
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}
\frac{\bar r_0^{\,2}}{D_0D_1D_2}.
$$

Define the algebraic SD cut so that the orbit contains

$\mathcal T_0-\mathcal C_0$:

$$
\mathcal C_0
=
\mathcal P_\Gamma\mathcal O_\Gamma
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}
\frac1{D_1D_2}.
$$

Insert

$$
\frac1{D_1D_2}
=
\frac{D_0}{D_0D_1D_2}.
$$

Then, before integration,

$$
\mathcal T_0-\mathcal C_0
=
\mathcal P_\Gamma\mathcal O_\Gamma
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}
\frac{\bar r_0^{\,2}-r_{0,d}^{\,2}}
{D_0D_1D_2}.
$$

Thus

$$
\boxed{
\mathcal T_0-\mathcal C_0
=
\mathcal P_\Gamma\mathcal O_\Gamma
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}
\frac{\mu_\varepsilon^2(r_0)}
{D_0D_1D_2}.
}
$$

If one makes the incorrect replacement

$$
\bar r_0^{\,2}\longrightarrow r_{0,d}^{\,2},
$$

then

$$
\boxed{
\mathcal T_0-\mathcal C_0=0
}
$$

identically at the integrand level.

### Feynman parameters

Write

$$
D_0=k^2,
\qquad
D_1=(k+Q_1)^2,
\qquad
D_2=(k+Q_2)^2.
$$

Set

$$
x:=1-y-z,
\qquad
y\geq0,
\qquad
z\geq0,
\qquad
y+z\leq1.
$$

Then

$$
\frac1{D_0D_1D_2}
=
2
\int_0^1dy
\int_0^{1-y}dz\,
\frac1{(\ell_d^2+\Delta)^3},
$$

where

$$
\ell
=
k+yQ_1+zQ_2,
$$

$$
\boxed{
\Delta
=
xy\,Q_1^2
+
xz\,Q_2^2
+
yz\,(Q_1-Q_2)^2.
}
$$

Let

$$
s:=yQ_1+zQ_2.
$$

Since $s$ is physical four-dimensional,

$$
\bar s^{\,2}=s_d^2,
\qquad
\bar\ell\cdot s=\ell_d\cdot s.
$$

Consequently,

$$
\begin{aligned}
\mu_\varepsilon^2(k)
&=
\overline{(\ell-s)}^{\,2}
-
(\ell-s)_d^2
\\
&=
\bar\ell^{\,2}
-2\bar\ell\cdot s
+\bar s^{\,2}
-\ell_d^2
+2\ell_d\cdot s
-s_d^2
\\
&=
\bar\ell^{\,2}-\ell_d^2
\\
&=
\mu_\varepsilon^2(\ell).
\end{aligned}
$$

Therefore

$$
\mathcal T_0-\mathcal C_0
=
2\mathcal P_\Gamma\mathcal O_\Gamma
\int_{\Sigma_2}dy\,dz\,
J_\varepsilon(\Delta),
$$

with

$$
J_\varepsilon(\Delta)
:=
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\varepsilon^2(\ell)}
{(\ell_d^2+\Delta)^3}.
$$

### Evanescent tensor reduction

Rotational invariance in the regulated $d$-space gives

$$
\int d^d\ell\,
\ell^m\ell^nF(\ell_d^2)
=
\frac{g_d^{mn}}d
\int d^d\ell\,
\ell_d^2F(\ell_d^2).
$$

Hence

$$
\begin{aligned}
\int d^d\ell\,
\mu_\varepsilon^2F
&=
-\widetilde g_{mn}
\int d^d\ell\,
\ell^m\ell^nF
\\
&=
-\frac{\widetilde g_{mn}g_d^{mn}}d
\int d^d\ell\,
\ell_d^2F
\\
&=
-\frac{d-4}{d}
\int d^d\ell\,
\ell_d^2F
\\
&=
\frac{4-d}{d}
\int d^d\ell\,
\ell_d^2F.
\end{aligned}
$$

Thus

$$
J_\varepsilon(\Delta)
=
\frac{4-d}{d}
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell_d^2}{(\ell_d^2+\Delta)^3}.
$$

Use the exact integration-by-parts identity

$$
0
=
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\partial}{\partial\ell^m}
\left[
\frac{\ell^m}{(\ell_d^2+\Delta)^2}
\right].
$$

Expanding,

$$
0
=
d
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell_d^2+\Delta)^2}
-
4
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell_d^2}{(\ell_d^2+\Delta)^3}.
$$

Therefore

$$
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell_d^2}{(\ell_d^2+\Delta)^3}
=
\frac d4 I_2(\Delta),
$$

where

$$
I_2(\Delta)
:=
\mu_{\mathrm R}^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell_d^2+\Delta)^2}.
$$

Hence

$$
J_\varepsilon(\Delta)
=
\frac{4-d}{4}I_2(\Delta).
$$

The scalar integral is

$$
I_2(\Delta)
=
\frac{\mu_{\mathrm R}^{2\epsilon}}
{(4\pi)^{d/2}}
\Gamma\!\left(2-\frac d2\right)
\Delta^{d/2-2}.
$$

For

$$
d=4-2\epsilon,
$$

this becomes

$$
I_2(\Delta)
=
\frac{\mu_{\mathrm R}^{2\epsilon}\Gamma(\epsilon)}
{(4\pi)^{2-\epsilon}}
\Delta^{-\epsilon}.
$$

Thus

$$
\begin{aligned}
\mathcal T_0-\mathcal C_0
&=
2\mathcal P_\Gamma\mathcal O_\Gamma
\int_{\Sigma_2}dy\,dz\,
\frac{4-d}{4}
\frac{\mu_{\mathrm R}^{2\epsilon}\Gamma(\epsilon)}
{(4\pi)^{2-\epsilon}}
\Delta^{-\epsilon}
\\
&=
\mathcal P_\Gamma\mathcal O_\Gamma
(4-d)
\frac{\mu_{\mathrm R}^{2\epsilon}\Gamma(\epsilon)}
{2(4\pi)^{2-\epsilon}}
\int_{\Sigma_2}dy\,dz\,\Delta^{-\epsilon}.
\end{aligned}
$$

Define exactly the frozen scalar unit

$$
A_\epsilon
:=
\frac{\mu_{\mathrm R}^{2\epsilon}\Gamma(\epsilon)}
{2(4\pi)^{2-\epsilon}}
\int_{\Sigma_2}dy\,dz\,\Delta^{-\epsilon}.
$$

Therefore

$$
\boxed{
\mathcal T_0-\mathcal C_0
=
\mathcal P_\Gamma\mathcal O_\Gamma
(4-d)A_\epsilon.
}
$$

Since

$$
\int_{\Sigma_2}dy\,dz
=
\int_0^1dy\int_0^{1-y}dz
=
\frac12,
$$

and

$$
\Gamma(\epsilon)=\frac1\epsilon-\gamma_E+O(\epsilon),
$$

one obtains

$$
A_\epsilon
=
\frac1{64\pi^2\epsilon}+O(1).
$$

Using

$$
4-d=2\epsilon,
$$

gives

$$
\boxed{
\lim_{\epsilon\to0}(4-d)A_\epsilon
=
\frac1{32\pi^2}.
}
$$

Hence the universal unit-square result is

$$
\boxed{
\lim_{\epsilon\to0}
(\mathcal T_0-\mathcal C_0)
=
\frac{\mathcal P_\Gamma\mathcal O_\Gamma}{32\pi^2}.
}
$$

With the genuine $d-4$ square instead,

$$
\widetilde\ell^{\,2}
=
\ell_d^2-\bar\ell^{\,2},
$$

the sign is reversed:

$$
\boxed{
2
\int_{\Sigma_2}dy\,dz
\int_\ell
\frac{\widetilde\ell^{\,2}}
{(\ell_d^2+\Delta)^3}
=
-\frac1{32\pi^2}.
}
$$

---

## C. No independent graph-specific $4-d$

Suppose the D-word of graph $\Gamma$ produces

$$
N_D^\Gamma
=
a_\Gamma\bar r_s^{\,2}\mathcal O_\Gamma,
$$

where $a_\Gamma$ is the exact D-algebra coefficient.

Then

$$
\Gamma_{\Gamma,T}-\Gamma_{\Gamma,C}
=
\mathcal P_\Gamma a_\Gamma\mathcal O_\Gamma
(4-d)A_\epsilon.
$$

The factor $4-d$ has already arisen from

$$
-\widetilde g_{mn}g_d^{mn}
=
4-d.
$$

Therefore an additional manually inserted graph factor $4-d$ would give

$$
(4-d)^2A_\epsilon
=
4\epsilon^2
\left[
\frac1{64\pi^2\epsilon}+O(1)
\right],
$$

and hence

$$
\lim_{\epsilon\to0}(4-d)^2A_\epsilon=0.
$$

The reusable rule is therefore

$$
\boxed{
\bar r_s^{\,2}\text{ triangle}
-
r_{s,d}^{\,2}\text{ SD cut}
\quad\longrightarrow\quad
\frac1{32\pi^2}
}
$$

for a unit selected square, conditional on the projector algebra of Section A.

All graph dependence remains in

$$
\boxed{
\mathcal P_\Gamma a_\Gamma\mathcal O_\Gamma,
}
$$

including:

$$
\mathcal P_\Gamma
=
(\text{source sign})
(\text{vertex factors})
(\text{propagator signs})
(\text{Wick multiplicity})
(\text{color})
(\text{flavor})
(\text{arrow/orientation}).
$$

If the D-word leaves additional loop momentum,

$$
N_D^\Gamma
=
\bar r_s^{\,2}R_\Gamma(\ell,p,q),
\qquad
\deg_\ell R_\Gamma>0,
$$

then the exact difference remains

$$
\Gamma_{\Gamma,T}-\Gamma_{\Gamma,C}
=
\mathcal P_\Gamma
\int_k
\frac{\mu_\varepsilon^2(r_s)R_\Gamma}
{D_0D_1D_2},
$$

but the scalar number $1/(32\pi^2)$ alone is no longer sufficient; the additional tensor moments must be evaluated.

---

## D. Missing contact in a complete SD orbit

The inverse-Hessian identity gives a concrete obstruction.

Let

$$
G:=H^{-1},
$$

and let two background/source variations produce

$$
M_1^{(1)}:=\delta_1H,
\qquad
M_1^{(2)}:=\delta_2H,
\qquad
M_2^{(12)}:=\delta_2\delta_1H.
$$

First variation:

$$
\delta_1G
=
-GM_1^{(1)}G.
$$

Second variation:

$$
\begin{aligned}
\delta_2\delta_1G
&=
-\delta_2
\left(
GM_1^{(1)}G
\right)
\\
&=
-(\delta_2G)M_1^{(1)}G
-GM_2^{(12)}G
-GM_1^{(1)}(\delta_2G)
\\
&=
GM_1^{(2)}GM_1^{(1)}G
-GM_2^{(12)}G
+GM_1^{(1)}GM_1^{(2)}G.
\end{aligned}
$$

Therefore the complete second-order orbit contains

$$
\boxed{
GM_1^{(2)}GM_1^{(1)}G
+
GM_1^{(1)}GM_1^{(2)}G
-
GM_2^{(12)}G.
}
$$

The first two terms are the two directed $M_1M_1$ parents. The third term is an independent $M_2$ seagull/contact.

Thus the parent

$$
G_2=(I[u,\phi_1],M_1,M_1)
$$

is not a complete SD orbit by itself. Its concrete missing Hessian contact is

$$
\boxed{
G_{3,2}
=
(I[u,\phi_1],M_2,H_{\rm antichiral}).
}
$$

The scalar replacement

$$
\bar r_s^{\,2}-r_{s,d}^{\,2}
$$

computes only the line-cut defect inside the $M_1M_1$ parent. It does not prove

$$
G_{3,2}=0.
$$

That graph must separately satisfy one of:

$$
\boxed{
N_{G_{3,2}}=0,
}
$$

$$
\boxed{
\int_k
\frac{N_{G_{3,2}}}{\prod_jD_j}=0,
}
$$

or

$$
\boxed{
G_{3,2}
+
\text{another explicit contact}=0.
}
$$

If the source insertion itself depends on the two varied backgrounds, there are further source-link terms:

$$
\begin{aligned}
\delta_2\delta_1(IG)
&=
(\delta_2\delta_1I)G
+
(\delta_1I)(\delta_2G)
+
(\delta_2I)(\delta_1G)
+
I(\delta_2\delta_1G).
\end{aligned}
$$

These terms provide the structural location for an $M_3$/outer-source parent such as $G_{3,3}$. They are not generated by the evanescent-square integral.

---

## Claim table

| Audit claim | Result | Exact statement |
| $\bar\ell^{\,2}-\ell_d^2$ is the $d-4$ square | Rejected as named | $\widetilde\ell^{\,2}=\ell_d^2-\bar\ell^{\,2}$ has trace $d-4$; $\mu_\varepsilon^2=\bar\ell^{\,2}-\ell_d^2=-\widetilde\ell^{\,2}$ has effective trace $4-d$. |
| The integrand-level triangle-minus-cut mechanism is valid | Conditional | $\mathcal T-\mathcal C=\mathcal P_\Gamma\mathcal O_\Gamma\int\mu_\varepsilon^2/(D_0D_1D_2)$, provided a distinct finite-$4$ projector $\bar g$ is added. |
| The mechanism follows from the frozen Q4S/QDS split | Rejected | With $\delta_4=\widehat\delta+\breve\delta$ and $\breve\delta\ell=0$, $\delta_4(\ell,\ell)=\ell_d^2$, so the scalar difference is zero. |
| A separate graph-specific $4-d$ is required | Rejected | $\int\mu_\varepsilon^2F=(4-d)d^{-1}\int\ell_d^2F$; the trace factor is already inside the loop integral. |
| Universal scalar unit | Accepted conditionally | $\displaystyle 2\int_{\Sigma_2}\!\!dy\,dz\int_\ell\frac{\mu_\varepsilon^2}{(\ell_d^2+\Delta)^3}=\frac1{32\pi^2}$. |
| The scalar mechanism closes the full SD orbit | Rejected | $\delta_2\delta_1G=GM_1^{(2)}GM_1^{(1)}G+GM_1^{(1)}GM_1^{(2)}G-GM_2^{(12)}G$; the $M_2$ contact must be evaluated separately. |
