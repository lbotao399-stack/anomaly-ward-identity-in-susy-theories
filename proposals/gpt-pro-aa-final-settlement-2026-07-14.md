# GPT Pro ordered-AA final settlement — 2026-07-14

Status: `NON_AUTHORITY_PRO_REVIEW`.

Chat: https://chatgpt.com/c/6a563e16-0d68-83e8-aaef-928c89fe0b6b

Prompt: `/Users/libotao/.codex/procodex/2026-07-14-awi-aa-pair-standard-feynman/final-prompt.md`

Prompt SHA-256: `1efd04011130a3f64f4e57e42bc58fc1d0aa576af8bc8e7eb68b7f0eaab1f90b`.

Elapsed: `10m47s`.

The following is the completed visible response exported from the rendered DOM, with TeX recovered from the page's MathML annotations. Interface labels such as `Pasted text` are retained.

Scope remains the ordered $A^AA^B$ insertion, with separate $G$- and $M$-triangle sectors and a DRED cutting defect. Pasted text

Define

$$
\mathcal O_G^{DE}
:=
D_{\dot\alpha}^DP^{\dot\alpha}A^E
-
(P_{\dot\alpha}A^D)D^{E\dot\alpha},
$$

$$
\mathcal O_M^{DE}
:=
\sum_{r=1}^{3}
\left[
\langle B_r^D,C_r^E\rangle
-
\langle C_r^D,B_r^E\rangle
\right].
$$

The settled equations are

$$
\boxed{
\Gamma_{AA,G}^{AB}
=
\frac{\lambda_1}{8}
\mathbb F^{AB}{}_{DE}\mathcal O_G^{DE}
}
$$

and

$$
\boxed{
K^P_{m,n;k,l}
=
\frac{2\binom mk\binom nl}
{(m+n+2)(k+l+1)}.
}
$$

The old/corrected gauge ratio is exactly

$$
\boxed{
\frac{\Gamma_{G,\mathrm{old}}}{\Gamma_{G,\mathrm{corrected}}}=8.
}
$$

---

# 1. BLOCKED_UNREDUCED_Q4S_MATTER_WORD

For one flavor and one arrow,

$$
D_0=k^2,
\qquad
D_1=(k-q)^2,
\qquad
D_2=(k-p-q)^2.
$$

Set

$$
P:=p+q,
\qquad
x:=1-a-b,
$$

$$
\ell:=k-aq-bP.
$$

Then

$$
xD_0+aD_1+bD_2
=
\ell^2+\Delta,
$$

with

$$
\boxed{
\Delta
=
xa\,q^2+xb\,P^2+ab\,p^2.
}
$$

Therefore

$$
\boxed{
\frac1{D_0D_1D_2}
=
2\int_{\substack{a,b\geq0\\a+b\leq1}}
da\,db\,
\frac1{(\ell^2+\Delta)^3}.
}
$$

An admissible unreduced Q4S numerator must first be obtained as an open-spinor Clifford word

$$
\mathscr N_M^{Q4S}(r_0,r_1,r_2)
$$

before any finite-dimensional identity such as

$$
\det(-i\sigma_E\cdot r)=-r^2,
$$

finite Weyl completeness, Fierz rearrangement, or $2\times2$ Cayley--Hamilton.

Only after that derivation may one define pointwise tensors by

$$
\mathscr N_M^{Q4S}(\ell+aq+bP,p,q)
=
\ell^m\ell^n
\mathcal R^{Q4S}_{mn}(a,b;p,q)
+
\mathcal R^{Q4S}_0(a,b;p,q)
+
\mathcal R^{Q4S}_{\mathrm{odd}},
$$

provided the unreduced word independently proves that all rank-four terms cancel.

The exact full integral would then be

$$
\Gamma_{M_r}^{Q4S,\rightarrow}
=
2\hbar g^2\mathbb F^{AB}{}_{DE}
\int_{\Delta_2}da\,db
\left[
\frac{\widehat\delta^{mn}}4
I_2(\Delta)
\mathcal R^{Q4S}_{mn}
+
I_3(\Delta)
\mathcal R^{Q4S}_0
\right],
$$

where

$$
I_2(\Delta)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell^2+\Delta)^2}
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\Delta^{-\epsilon},
$$

$$
I_3(\Delta)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell^2+\Delta)^3}
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\frac{\Gamma(1+\epsilon)}2
\Delta^{-1-\epsilon}.
$$

The supplied finite expression

$$
N_M^{\rm eff}
=
4\left[
\det(r_0)(r_{1+}\wedge r_{2+})
-
\det(r_1)(r_{0+}\wedge r_{2+})
\right]
$$

is already the image of an unknown Q4S word under a finite-spinor reduction map,

$$
\pi_{2\times2}
\left(
\mathscr N_M^{Q4S}
\right)
=
N_M^{\rm eff}.
$$

The inverse

$$
\pi_{2\times2}^{-1}
\left(
N_M^{\rm eff}
\right)
$$

is not defined by the supplied contract. Consequently neither

$$
\mathcal R^{Q4S}_{mn}(a,b;p,q)
$$

nor

$$
\mathcal R^{Q4S}_0(a,b;p,q)
$$

can be reconstructed pointwise.

The authoritative input supplies the coordinate-space matter action and the $n=1$ matter vertex, but not the unreduced open-spinor D-word. Pasted text It also explicitly leaves the DRED continuation unfixed. Pasted text

The minimal missing axiom is

$$
\boxed{
\left\{
\mathscr N_M^{Q4S}(r_0,r_1,r_2),
\quad
\tau_{Q4S}\text{ on all open Weyl/Clifford chains}
\right\},
}
$$

including a rule for contractions such as

$$
(\sigma^m)_{\alpha\dot\alpha}
(\bar\sigma_m)^{\dot\beta\beta}
$$

without invoking finite two-component completeness.

Therefore

$$
\boxed{\texttt{BLOCKED\_UNREDUCED\_Q4S\_MATTER\_WORD}.}
$$

The two established checks remain

$$
\boxed{
\Gamma_{AA,M}^{\rm finite\,2\times2}=0,
}
$$

$$
\boxed{
\left[
\Gamma_{AA,M}^{Q4S}
\right]_{\rm isolated\ rank\,2\ pole}
=
\frac{4\lambda_1}{3}
\mathbb F^{AB}{}_{DE}\mathcal O_M^{DE}.
}
$$

The second equation is not the full Q4S matter amplitude.

---

# 2. Graph occurrence census

## FP ghost

To enumerate FP graphs one needs

$$
S_{\rm FP},
\qquad
G_{\rm FP}
=
\left(
\frac{\delta^2S_{\rm FP}}
{\delta\bar c\,\delta c}
\right)^{-1},
$$

and the background/quantum vertices

$$
\frac{\delta^{n+2}S_{\rm FP}}
{\delta\bar c\,\delta c\,
\delta u^n},
\qquad
\frac{\delta^{n+2}S_{\rm FP}}
{\delta\bar c\,\delta c\,
\delta\mathbf V^n}.
$$

None is admitted. In a standard ghost-number-diagonal gauge, a ghost loop joined to the $AA$ source by two quantum-vector propagators has

$$
I=4,
\qquad
V=3,
\qquad
L=I-V+1=2,
$$

but the absence of mixed $u$-ghost propagators is itself gauge-fixing data.

$$
\boxed{\Gamma_{\rm FP}\ \text{is blocked, not set to zero}.}
$$

## Nielsen--Kallosh ghost

The required data are

$$
S_{\rm NK},
\qquad
G_{\rm NK}
=
\left(
\frac{\delta^2S_{\rm NK}}
{\delta b_{\rm NK}\delta b_{\rm NK}}
\right)^{-1},
$$

together with its background-dependent Hessian.

No NK branch, propagator, statistics convention, or background vertex is specified.

$$
\boxed{\Gamma_{\rm NK}\ \text{is blocked, not set to zero}.}
$$

## Gauge-fixing sector

A purely quadratic, background-independent functional would obey

$$
\frac{\delta^3S_{\rm gf}}
{\delta u\,\delta u\,\delta\mathbf V}
=
0,
\qquad
\frac{\delta^4S_{\rm gf}}
{\delta u\,\delta u\,
\delta\mathbf V\,\delta\mathbf V}
=
0,
$$

and would produce no interaction graph.

A background-covariant gauge can instead have

$$
\frac{\delta^3S_{\rm gf}}
{\delta u\,\delta u\,\delta\mathbf V}
\neq0
$$

and contribute one-loop source triangles or contact bubbles.

Because $S_{\rm gf}$ is not supplied,

$$
\boxed{\Gamma_{\rm gf}\ \text{is blocked}.}
$$

## Source-link completion

The omitted source terms are

$$
\mathcal S_{\rm link}
=
D_-\!\left(
A^{(2)}A^{(1)}
+
A^{(1)}A^{(2)}
\right)
+
[\Gamma_-^{(1)},A^{(1)}A^{(1)}].
$$

They contain three quantum vectors:

$$
\deg_u\mathcal S_{\rm link}=3.
$$

A complete one-loop census also requires the one-quantum/two-background vertices

$$
\widetilde\Phi_{\mathrm b}\,u\,\Phi_{\mathrm b},
\qquad
\mathbf W\,\widetilde{\mathbf W}\,u,
$$

their superspace D-words, and the composite-source normal-ordering rule. For example,

$$
\mathcal S_{\rm link}[u^3]
\,
V_{\widetilde\Phi_{\mathrm b}u\Phi_{\mathrm b}}[u]
$$

contains four quantum-vector legs and can form

$$
I=2,
\qquad
V=2,
\qquad
L=1.
$$

Thus odd-field counting does not exclude every source-link bubble.

$$
\boxed{\Gamma_{\rm source\ link}\ \text{is blocked}.}
$$

## One-loop counterterms

The most general same-letter local renormalization contains

$$
[AA]_R
=
[AA]_B
+
\hbar z_G\,\mathcal O_G
+
\hbar z_M\,\mathcal O_M
+
\cdots.
$$

These terms contribute at the same order as the one-loop graph:

$$
\delta\Gamma_{AA}^{(1)}
=
\hbar z_G\,\mathcal O_G
+
\hbar z_M\,\mathcal O_M.
$$

No subtraction scheme, renormalization conditions, or values of $z_G,z_M$ are supplied.

$$
\boxed{\delta\Gamma_{\rm ct}\ \text{is blocked}.}
$$

## Evanescent operator mixing

Let $E_\alpha$ be Q4S-evanescent operators satisfying

$$
E_\alpha
=
\epsilon
\left(
R_{\alpha G}\mathcal O_G
+
R_{\alpha M}\mathcal O_M
\right)
+
O(\epsilon^2).
$$

A pole counterterm gives the finite contribution

$$
\frac{\hbar Z_\alpha}{\epsilon}E_\alpha
\underset{\epsilon\to0}{\longrightarrow}
\hbar Z_\alpha
\left(
R_{\alpha G}\mathcal O_G
+
R_{\alpha M}\mathcal O_M
\right).
$$

The evanescent basis, mixing matrix, and finite projection prescription are absent.

$$
\boxed{\delta\Gamma_{\rm ev}\ \text{is blocked}.}
$$

Hence the complete occurrence census is not closed:

$$
\boxed{
\Gamma_{\rm auxiliary}
=
\Gamma_{\rm FP}
+
\Gamma_{\rm NK}
+
\Gamma_{\rm gf}
+
\Gamma_{\rm source\ link}
+
\delta\Gamma_{\rm ct}
+
\delta\Gamma_{\rm ev}
\quad\text{is undetermined}.
}
$$

---

# 3. BLOCKED_PROJECT_HT_COMPONENT_INTERTWINER

Introduce a general Project-to-HT component map:

$$
D_{\dot\alpha}^{P}
=
\alpha_D\,
\partial_{\dot\alpha}c^{HT},
$$

$$
(P_{\dot\alpha}A)^P
=
\alpha_A\,
\partial_{\dot\alpha}b^{HT},
$$

$$
(P_{\dot\alpha}B_r)^P
=
\alpha_B\,
\partial_{\dot\alpha}\beta_r^{HT},
$$

$$
(P_{\dot\alpha}C_r)^P
=
\alpha_C\,
\partial_{\dot\alpha}\gamma_r^{HT}.
$$

Then the mapped gauge and matter coefficients are

$$
c_G^{HT}
=
c_G^P\alpha_D\alpha_A,
$$

$$
c_M^{HT}
=
c_M^P\alpha_B\alpha_C.
$$

Equality of the HT gauge and matter structures requires

$$
\boxed{
\frac{c_M^P}{c_G^P}
\frac{\alpha_B\alpha_C}
{\alpha_D\alpha_A}
=
1.
}
$$

For the isolated rank-two matter pole,

$$
\frac{c_M^P}{c_G^P}
=
\frac{4\lambda_1/3}{\lambda_1/8}
=
\frac{32}{3}.
$$

Therefore a nonuniform component intertwiner would have to satisfy

$$
\boxed{
\frac{\alpha_B\alpha_C}
{\alpha_D\alpha_A}
=
\frac3{32}.
}
$$

No admitted Project component definitions determine

$$
\alpha_A,\quad
\alpha_D,\quad
\alpha_B,\quad
\alpha_C,
$$

including their phases, Berezin normalizations, parities, and component extraction points.

The displayed $b,c,\beta,\gamma$ dictionary occurs only in the source's `EXTERNAL_TARGET_ONLY` section; it is not derived from Project component definitions. Pasted text

The accepted derivative kernel

$$
K^P_{m,n;k,l}
=
2T^{HT}_{m,n;k,l}
$$

does not determine any $\alpha$-factor and cannot change

$$
\frac{c_M^P}{c_G^P}.
$$

Therefore

$$
\boxed{\texttt{BLOCKED\_PROJECT\_HT\_COMPONENT\_INTERTWINER}.}
$$

---

# 4. Full ordered $AA$ settlement

The presently determined decomposition is

$$
\boxed{
\Gamma_{AA,\mathrm{full}}^{AB}
=
\frac{\lambda_1}{8}
\mathbb F^{AB}{}_{DE}\mathcal O_G^{DE}
+
\Gamma_{AA,M,\mathrm{full}}^{AB,Q4S}
+
\Gamma_{\rm auxiliary}^{AB}.
}
$$

The only fixed part of the Q4S matter contribution is

$$
\boxed{
\left[
\Gamma_{AA,M,\mathrm{full}}^{AB,Q4S}
\right]_{\rm isolated\ rank\,2\ pole}
=
\frac{4\lambda_1}{3}
\mathbb F^{AB}{}_{DE}\mathcal O_M^{DE}.
}
$$

The finite $2\times2$ calculation gives

$$
\boxed{
\Gamma_{AA,M}^{AB,\mathrm{finite}\ 2\times2}=0,
}
$$

but it is not the full Q4S result.

| Settlement item | Status | Exact equation or blocker |
| --- | --- | --- |
| `GAUGE` | **ACCEPTED** | $\displaystyle \Gamma_{AA,G}^{AB}=\frac{\lambda_1}{8}\mathbb F^{AB}{}_{DE}\mathcal O_G^{DE}$, with old/corrected ratio $8$. |
| `MATTER_FULL_Q4S` | **BLOCKED** | $\displaystyle \pi_{2\times2}^{-1}(N_M^{\rm eff})$ is undefined; hence $\mathcal R^{Q4S}_{mn}(a,b;p,q)$ and $\mathcal R^{Q4S}_0(a,b;p,q)$ are unavailable. |
| `GRAPH_CENSUS` | **BLOCKED** | $\displaystyle S_{\rm FP},S_{\rm NK},S_{\rm gf},Z_{AA\to\mathcal O_i},\{E_\alpha,Z_{\alpha i}\}$ are not specified, and the one-loop source-link D-words are not evaluated. |
| `PROJECT_HT_MAP` | **BLOCKED** | $\displaystyle \frac{\alpha_B\alpha_C}{\alpha_D\alpha_A}$ is undetermined; the isolated rank-two term would require exactly $3/32$. |
| `FULL_AA_MATCH` | **BLOCKED** | $\displaystyle \Gamma_{AA,\mathrm{full}}=\frac{\lambda_1}{8}\mathbb F\mathcal O_G+\Gamma_{M,\mathrm{full}}^{Q4S}+\Gamma_{\rm auxiliary}$, with the last two terms unresolved. |
