# Step-6: the two-loop 日 (kite) supergraph for $\boldsymbol\nabla_-(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^A\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^B\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^C)$ — anomaly sector

Status: `NON_AUTHORITY_PROPOSAL` (exploratory two-loop seed, owner-authorized in the
2026-07-16/17 sessions: *"N=4 SYM 中，能有 2-loop 的修正必须是 3-letters operator …
纯 gauge sector 的 $\nabla_-(\nabla_+W_+^A\nabla_+W_+^B\nabla_+W_+^C)$，日字图 …
只 focus 在这一个图的 anomaly sector"*). Nothing here modifies the accepted one-loop
settlement. Numbered equations are (K3.$n$). Conventions, the DRED two-loop ledger
extension **[D3]**, the $\mu^2$-insertion lemma, and the length-2 vanishing baseline are
shared with the companion memo
`proposals/step6-two-loop-kite-aa-anomaly-memo-2026-07-16.md` (cited as **K.$n$**).

**External-target boundary.** The HT source (arXiv:2512.07771v2) prints no explicit
two-loop coefficient. Its sharp two-loop statements are: (i) the two-loop bracket
$Q_2=\tfrac1{3!}\{\mathcal I,\mathcal I,\mathcal I,\mathcal O\}$ is supported on the
unique two-loop Laman topology $K_4-e$ = 日 (`main.tex:539-561,648`); (ii)
$Q_1^2+\{Q_0,Q_2\}=0$ (`main.tex:220,398`); (iii) corrections on a length-$n$ word are
expected to truncate at $Q_{n-1}$ (`main.tex:222`) — so $Q_2$ is first allowed on
length-3 words, while the length-2 channel must vanish. The companion memo proves
the length-2 vanishing on this topology (single output letter, single external momentum
— kinematic theorem K §8, machine-enumerated). This memo tests that first allowed
channel: the pure-gauge length-3 word $A^AA^BA^C$,
$A=\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+$, on the 日 graph.  The mandatory CP1
calibration fails below, so no nonzero coefficient is inferred.

---

## 1. Conventions

All of K §1 (seed-audit frame (K.1), FF propagator (K.2), saturation F.6, DRED anchor
(K.3), two-loop evanescent ledger **[D3]**). Canonical dictionary $\mathcal V_P=2gv$,
$W_{(1)a}=-\tfrac14\bar D^2D_av$, $\widetilde W_{(1)\dot a}=-\tfrac14D^2\bar D_{\dot a}v$;
cubic vertices $S_{(3),\pm}$ of (K.7).

## 2. The word

$$
\mathcal I^{ABC}_{(3)}
=D_-\big[(K_+v^A)(K_+v^B)(K_+v^C)\big],
\qquad K_+=-\tfrac14D_+\bar D^2D_+,\qquad
D_-K_+=-\tfrac18D^2\bar D^2D_+,
\tag{K3.1}
$$

three $\boldsymbol\nabla_-$-placements $\mathfrak a,\mathfrak b,\mathfrak c$ (Leibniz on
three bosonic legs).  If $\mathcal B$ is a canonical $D A$ or $A D$ output bilinear,
$\mathcal B_{\rm can}=g^{-2}\mathcal B_P$.  Hence the exact project conversion is

$$
g^3\big[\hbar^2g^3\mathcal B_{\rm can}\big]
=g^3\big[\hbar^2g^3g^{-2}\mathcal B_P\big]
=\hbar^2g^4\mathcal B_P.
\tag{K3.1a}
$$

Quantum numbers of the insertion: dimension $\tfrac{13}2$, undotted charge
$+\tfrac52$, odd Grassmann parity. Two-letter output words consistent with this
bookkeeping and with a pure-gauge routing (output jets are $v$-jets only):

$$
\mathsf p^3\text{-dressed }\langle D,A\rangle\text{-family}:\quad
\dim=\tfrac32+2+3=\tfrac{13}2,\quad
\text{charge}=0+1+\tfrac32=\tfrac52\ \checkmark
\tag{K3.2}
$$

(the $\mathsf p^4\langle B,C\rangle$ matter family cannot appear on all-vector lines).
Because the two output letters carry **independent** momenta $q_1,q_2$, the length-2
kinematic vanishing theorem (K §8) does not apply:
$\epsilon^{\dot a\dot b}\mathsf p_{+\dot a}(q_1)\mathsf p_{+\dot b}(q_2)\neq0$.
This channel is where HT's expected truncation $Q_{n-1}$ first permits — and the
consistency condition $Q_1^2+\{Q_0,Q_2\}=0$ generically demands — a nonzero $Q_2$.

## 3. The graph

$K_4-e$ with the insertion at a degree-3 corner; the missing edge is
$X_a$–$X_b$; the 日 rectangle is $O,X_a,X_{\rm mid},X_b$ with middle bar $O$–$X_{\rm mid}$:

```
            q₁ ⇐ (output letter, X_a)          (output letter, X_b) ⇒ q₂
                     ╲                              ╱
                    X_a(θ₁)                  X_b(θ₂)      ← NO edge (K₄−e)
                     │   ╲                    ╱   │
              D₁, ℓ  │     ╲ D₄, q₁−ℓ  D₅, q₂−k ╱ │  D₂, k
                     │       ╲              ╱     │
                    O(θ₀) ─────── D₃ ────── X_mid(θ₃)
                            Q−ℓ−k  (middle bar)

   O = ∇₋(∇₊W₊ᴬ ∇₊W₊ᴮ ∇₊W₊ᶜ)(Q = q₁+q₂ incoming)
```

equivalently, as the 日 character: cycle $O$–$X_a$–$X_{\rm mid}$–$X_b$–$O$ with the
middle bar $O$–$X_{\rm mid}$; $O$ and $X_{\rm mid}$ have degree 3, $X_a$ and $X_b$
degree 2 (one uncontracted output leg each).

$$
\begin{aligned}
&L_1:O\!\to\!X_a\ (\ell),\quad
L_2:O\!\to\!X_b\ (k),\quad
L_3:O\!\to\!X_{\rm mid}\ (Q-\ell-k),\\
&L_4:X_{\rm mid}\!\to\!X_a\ (q_1-\ell),\quad
L_5:X_{\rm mid}\!\to\!X_b\ (q_2-k),\qquad Q:=q_1+q_2,\\[2pt]
&D_1=\ell^2,\quad D_2=k^2,\quad D_3=(Q-\ell-k)^2,\quad
D_4=(q_1-\ell)^2,\quad D_5=(q_2-k)^2 .
\end{aligned}
\tag{K3.3}
$$

TikZ (paper layer):

```tex
\begin{tikzpicture}[scale=1.5, every node/.style={font=\small}]
  \coordinate (O)  at (0,0);  \coordinate (M)  at (0,-1.6);
  \coordinate (Xa) at (-1.5,-0.8); \coordinate (Xb) at (1.5,-0.8);
  \draw (O)--(Xa) node[midway,above left] {$\ell$};
  \draw (O)--(Xb) node[midway,above right] {$k$};
  \draw (O)--(M)  node[midway,right] {$Q-\ell-k$};
  \draw (M)--(Xa) node[midway,below left] {$q_1-\ell$};
  \draw (M)--(Xb) node[midway,below right] {$q_2-k$};
  \draw[dashed] (Xa)--(-2.4,-0.8) node[left] {$q_1$};
  \draw[dashed] (Xb)--(2.4,-0.8) node[right] {$q_2$};
  \filldraw (O) circle (2.2pt) node[above] {$\mathcal O=\boldsymbol\nabla_-(A^AA^BA^C)$};
  \filldraw (M) circle (1.5pt) node[below] {$X_{\rm mid}$};
  \filldraw (Xa) circle (1.5pt) node[above left] {$X_a$};
  \filldraw (Xb) circle (1.5pt) node[above right] {$X_b$};
\end{tikzpicture}
```

## 4. The amplitude read off the graph

For $\chi_v=+1$ on $S_{(3),+}$ and $\chi_v=-1$ on $S_{(3),-}$, the AAA insertion and
three vertex factors give

$$
\left(-\frac18\right)\left(-\frac14\right)^2=-\frac1{128},
\qquad
\hbar^5\left(-\frac1\hbar\right)^3
\prod_{v=m,a,b}\left(-\chi_v\frac{ig}{2}\right)
\left(-\frac1{128}\right)
=\frac{i}{1024}\hbar^2g^3\chi_m\chi_a\chi_b.
\tag{K3.4a}
$$

Leaving each E-slot $-1/4$ inside its word gives (K3.4a).  Stripping all three E-slot
numbers gives

$$
\frac{i}{1024}\left(-\frac14\right)^3
=-\frac{i}{65536},
\qquad w_{\rm Wick}=\frac1{3!}(3!)=1.
\tag{K3.4b}
$$

Let $j\in\{1,2,3\}$ be the insertion line carrying $D_-K_+$ and define the stripped
insertion words

$$
\widehat I_e^{(j)}=
\begin{cases}
D^2\bar D^2D_+,&e=j,\\
D_+\bar D^2D_+,&e\ne j.
\end{cases}
\tag{K3.4c}
$$

At each cubic vertex, $\widehat{\mathscr V}_{v,\chi_v,\sigma_v}$ assigns the ordered
stripped slots

$$
\chi=+:\ (\bar D^2D^a,D_a,1),
\qquad
\chi=-:\ (D^2\bar D_{\dot a},\bar D^{\dot a},1)
\tag{K3.4d}
$$

to the two incident propagator deltas and the third incident object by
$\sigma_v\in S_3$.  For $\pi=(X,Y,Z)$ on $(L_1,L_2,L_3)$, set

$$
\mathcal T^{XYZ}{}_{DE}:=
\kappa^{XX'}\kappa^{YY'}\kappa^{ZZ'}\kappa^{MM'}\kappa^{NN'}
c_{Z'MN}c_{X'M'D}c_{Y'N'E}.
\tag{K3.4e}
$$

With $\Delta_e=\delta^4(\theta_{s(e)}-\theta_{t(e)})$ and
$K'=D_1D_2D_3D_4D_5$, the complete fully stripped pre-$D$ amplitude is

$$
\boxed{
\begin{aligned}
\Gamma_{\rm kite}^{ABC}[v^D(q_1),v^E(q_2)]
={}&-\frac{i}{65536}\hbar^2g^3
\sum_{\pi\in S_3(A,B,C)}\sum_{j=1}^{3}
\sum_{\vec\chi\in\{\pm1\}^3}\sum_{\vec\sigma\in S_3^3}
\chi_m\chi_a\chi_b(-1)^{\kappa(j,\vec\chi,\vec\sigma)}\\
&\times\prod_{v=m,a,b}\operatorname{sgn}(\sigma_v)\,
\mathcal T^{XYZ}{}_{DE}\,
\mu^{4\epsilon}\int\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}\frac1{K'}
\int d^4\theta_1d^4\theta_2d^4\theta_3\\
&\times\prod_{e=1}^{3}[\widehat I_e^{(j)}\Delta_e]\,
\widehat{\mathscr V}_{m,\chi_m,\sigma_m}
\widehat{\mathscr V}_{a,\chi_a,\sigma_a}
\widehat{\mathscr V}_{b,\chi_b,\sigma_b}.
\end{aligned}}
\tag{K3.4}
$$

The fixed order in (K3.4d) and the global Koszul sign are those of
(5A.61)–(5A.62).  The unpruned declared census is
$3\cdot3!\cdot2^3\cdot(3!)^3=31104$ assignments; CP1 blocks generation of their CP3
reduced rows.

Conditional operator-counting target: the insertion supplies $7$ $D$'s $+\,6$
$\bar D$'s and the vertices supply $6+6$.  If the two $\theta$-loops each absorb
$D^2\bar D^2$, if CP3 leaves exactly two output jets, and if two momentum factors are
consumed by tensor reduction, the candidate covariant remainder is the
$\mathsf p^3\langle D,A\rangle$ family of (K3.2).  CP1 does not prove these CP3
premises, so neither the number of surviving external factors nor basis completeness
is asserted here.

## 5. D-algebra: reduced result

The fast engine represents Grassmann monomials by bitmasks and coefficients by sparse
$\mathbb Q(i)$ polynomials.  It reproduces the five CP0 anchors

$$
\begin{gathered}
(D^2\theta^2)|=-4,\qquad(\bar D^2\bar\theta^2)|=-4,\qquad
[D^2\bar D^2\delta^4]|=16,\\
\delta_{01}^4D^2\bar D^2\delta_{01}^4=16\delta_{01}^4,\qquad
\delta_{01}^4[\#D<2,\#\bar D<2]\delta_{01}^4=0.
\end{gathered}
\tag{K3.5}
$$

Thus `CP0_ANCHORS_PASS`.  Separately, replay of the locked WW arithmetic ledger gives
$w_D=(-1/8)(-1/4)(16)(2)(2)=2$; this is
`WW_WD_ARITHMETIC_REPLAY_PASS`, not a completed explicit WW $D$-word proof.  CP1
requires the eight endpoint rows

$$
\begin{array}{c|cccccccc}
\mathrm{id}&01&02&03&04&05&06&07&08\\ \hline
D_-\text{ placement}&A&A&A&A&B&B&B&B\\
(\bar D,D)\text{ endpoints}&(r_0,r_1)&(r_0,r_2)&(r_1,r_1)&(r_1,r_2)&
(r_0,r_1)&(r_0,r_2)&(r_1,r_1)&(r_1,r_2)
\end{array},
\quad r_0=k,\quad r_1=k+q,\quad r_2=k+p+q,
\tag{K3.6}
$$

each proportional to

$$
S(r_i,r_j)^{\dot\alpha}
=(r_i)_{+\dot\beta}\,\mathsf p^{\dot\beta\gamma}(p)
(r_j)_\gamma{}^{\dot\alpha}.
\tag{K3.7}
$$

For WW-DA-01, the current prepotential implementation produces the raw component

$$
R_{\dot1,+}=2k_{01}
\big[k_{01}(p_{00}+q_{00})-k_{00}(p_{01}+q_{01})\big].
\tag{K3.8}
$$

At

$$
k_{00}=1,\quad k_{01}=2,\quad p_{00}=7,\quad p_{01}=3,\quad
q_{00}=11,\quad q_{01}=5,
$$

one obtains

$$
R_{\dot1,+}=2(2)[2(7+11)-1(3+5)]=112\ne0.
\tag{K3.9}
$$

This multiplies the unretained jet $\widetilde W_{\dot1}D_+W^+$.  A typed
$\Pi_X$ projection could remove it, but no such executable projection is supplied by
the locked seed; hence the value 112 proves only that the unprojected row is nonzero.
Even if it is projected out, the retained branch contains

$$
2k_{00}k_{01}k_{11}-2k_{01}^2k_{10}
=2k_{01}\det k=-2k_{01}k^2,
\tag{K3.10}
$$

with no external $p$, whereas every monomial of (K3.7) contains one $p$.  This can be
removed only by an occurrence-resolved contact quotient, which is also absent.  The exact
difference-monomial counts for rows 01--08 are

$$
(18690,23890,31110,34092,25466,20993,34498,27829),
\tag{K3.11}
$$

and the pre-quotient scalar-dictionary scan is false for
$z\in\{\tfrac12,-\tfrac12,\tfrac i2,-\tfrac i2\}$.  Because the typed projection and
occurrence-resolved contact extraction are missing, this diagnostic does not falsify
the authoritative seed; it states that the **current engine does not reproduce the
locked CP1 representative**.  The independent internal identity

$$
R_A+R_B=D_-T,\qquad R_A+R_B\ne-D_-T
\tag{K3.12}
$$

passes, so this is not an ordinary Leibniz error.  The first missing typed datum is the
source-ordered $D$-word together with its graded-IBP transfer, external
$\Pi_{\widetilde W\otimes X}$ projection, Bianchi/EOM/contact quotient, and momentum
phase dictionary.  Therefore

$$
\boxed{\mathrm{CP1}=\texttt{BLOCKED\_EXPLICIT\_WW\_D\_ALGEBRA\_WORD\_DERIVATION}},
\qquad
\boxed{\mathrm{CP2},\mathrm{CP3},\mathrm{CP4}=\mathrm{NOT\ RUN}}.
\tag{K3.13}
$$

Consequently there is no admissible CP3 reduced-row JSON or human row table to report;
no two-loop numerator was manufactured past the go/no-go gate.

## 6. Anomaly-sector identification

Per marked edge $e\in\{1,\dots,5\}$ the occurrence-wise cutting identity (K.9) splits
each four-dimensional square $\bar r_e^{\,2}$ over the $d$-dimensional $K':=D_1\cdots
D_5$ into contact rows (Schwinger–Dyson/EOM sector) plus the cutting failure
$\mu_{r_e}^2/K'$. With line momenta (K3.3) and strictly hatted externals,

$$
\mu_{L_1}^2=\mu_\ell^2,\quad
\mu_{L_2}^2=\mu_k^2,\quad
\mu_{L_4}^2=\mu_\ell^2,\quad
\mu_{L_5}^2=\mu_k^2,\quad
\mu_{L_3}^2=\mu_\ell^2+2\mu_{\ell k}+\mu_k^2 ,
\tag{K3.14}
$$

so the middle bar is the sole source of $\mu_{\ell k}$ **within this diagonal
line-square dictionary**.  Before CP3, it is not the sole possible source: a surviving
cross contraction obeys

$$
\bar\ell\!\cdot\!\bar k=\ell_d\!\cdot\!k_d+\mu_{\ell k}
\tag{K3.15}
$$

independently of $L_3^2$.
Set $x=\mu_\ell^2$, $y=\mu_k^2$, $z=\mu_{\ell k}$.  A bookkeeping envelope through
evanescent degree two is

$$
\Gamma^{\rm anom}_{\text{日}}
=\mu^{4\epsilon}\!\!\int\!\!\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}\,
\frac{N_x\,x+N_y\,y+N_z\,z+N_{x^2}x^2+N_{xy}xy+N_{y^2}y^2
+N_{xz}xz+N_{yz}yz+N_{z^2}z^2}{K'}
+(\text{contact daughters}),
\tag{K3.16}
$$

This is neither a proven maximal support nor a locality statement.  Finiteness and
locality require the missing CP3 rows, occurrence-resolved CP4 cuts, and a declared
two-loop subtraction/$R'$ scheme.

No coefficient or row count in (K3.16) is presently determined: occurrence-resolved
CP4 data are forbidden by (K3.13).  In particular,

$$
x(x+2z+y)=x^2+2xz+xy,
\qquad
(x+2z+y)^2=x^2+y^2+4z^2+2xy+4xz+4yz,
\tag{K3.17}
$$

so the shorter four-term ansatz is not closed before CP4.

## 7. The AAA-kite $\mu$-masters by Feynman parameters

The insertion lemma is

$$
L(n,\Delta)=
\epsilon\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(n-1-d/2)}{\Gamma(n)}\Delta^{d/2+1-n},
\tag{K3.18}
$$

and exact symbolic division by its defining $J_{n-1}-\Delta J_n$ expression gives
one for $n=2,3,4$.  Explicitly,

$$
\begin{aligned}
L(2,\Delta)&=\epsilon\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(-1+\epsilon)\Delta^{1-\epsilon},\\
L(3,\Delta)&=\frac{\Gamma(1+\epsilon)}{32\pi^2}
\left(\frac{4\pi\mu^2}{\Delta}\right)^\epsilon,\\
L(4,\Delta)&=\epsilon\frac{\mu^{2\epsilon}}{6(4\pi)^{2-\epsilon}}
\Gamma(1+\epsilon)\Delta^{-1-\epsilon},
\qquad L(3,\Delta)|_{\epsilon=0}=\frac1{32\pi^2}.
\end{aligned}
\tag{K3.19}
$$

Put $s_1=q_1^2$, $s_2=q_2^2$, $u_{12}=q_1\!\cdot q_2$ and introduce
$x_i\ge0$, $\sum_i x_i=1$.  Completing the two loop squares gives

$$
\begin{aligned}
A&=x_1+x_3+x_4,&B&=x_2+x_3+x_5,&C&=x_3,&U&=AB-C^2,\\
r_\ell&=x_3Q+x_4q_1,&r_k&=x_3Q+x_5q_2,&
H&=x_3Q^2+x_4s_1+x_5s_2,\\
F&=UH-Br_\ell^2-Ar_k^2+2Cr_\ell\!\cdot r_k\\
&=s_1x_1(x_2x_3+x_2x_4+x_3x_4+x_3x_5+x_4x_5)\\
&\quad+s_2x_2(x_1x_3+x_1x_5+x_3x_4+x_3x_5+x_4x_5)
+2u_{12}x_1x_2x_3.
\end{aligned}
\tag{K3.20}
$$

For the formal evanescent dimension $n=d-4=-2\epsilon$ and
$G=U^{-1}\left(\begin{smallmatrix}B&-C\\-C&A\end{smallmatrix}\right)$, Wick
contraction, after extracting $t^{-1}$ or $t^{-2}$, gives

$$
\begin{aligned}
\langle\mu_\ell^2\rangle&=\epsilon B/U,&
\langle\mu_k^2\rangle&=\epsilon A/U,&
\langle\mu_{\ell k}\rangle&=-\epsilon C/U,\\
\langle\mu_\ell^2\mu_k^2\rangle
&=(\epsilon^2AB-\epsilon C^2)/U^2,\\
\langle\mu_\ell^2\mu_{\ell k}\rangle
&=\epsilon(1-\epsilon)BC/U^2,\\
\langle\mu_{\ell k}^2\rangle
&=-\epsilon[AB+(1-2\epsilon)C^2]/(2U^2).
\end{aligned}
\tag{K3.21}
$$

Define the six SPEC-requested scalar probes

$$
(N_1,N_2,N_3,N_4,N_5,N_6)
:=\mu^{4\epsilon}\int\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}
\frac{(xy,xz,z^2,z,y,x)}{K'},
\quad x=\mu_\ell^2, y=\mu_k^2, z=\mu_{\ell k}.
\tag{K3.22}
$$

With $d\Omega_4=\prod_i dx_i\,\delta(1-\sum_i x_i)$ and

$$
\mathcal C_2=\frac{\mu^{4\epsilon}\Gamma(-1+2\epsilon)}{(4\pi)^d},
\qquad
\mathcal C_1=\frac{\mu^{4\epsilon}\Gamma(2\epsilon)}{(4\pi)^d},
$$

their exact parameter representations are

$$
\begin{aligned}
N_1&=\mathcal C_2\int d\Omega_4(\epsilon^2AB-\epsilon C^2)
\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}},\\
N_2&=\mathcal C_2\int d\Omega_4\epsilon(1-\epsilon)BC
\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}},\\
N_3&=-\frac\epsilon2\mathcal C_2\int d\Omega_4[AB+(1-2\epsilon)C^2]
\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}},\\
N_4&=-\epsilon\mathcal C_1\int d\Omega_4C
\frac{F^{-2\epsilon}}{U^{3-3\epsilon}},\\
N_5&=\epsilon\mathcal C_1\int d\Omega_4A
\frac{F^{-2\epsilon}}{U^{3-3\epsilon}},\\
N_6&=\epsilon\mathcal C_1\int d\Omega_4B
\frac{F^{-2\epsilon}}{U^{3-3\epsilon}}.
\end{aligned}
\tag{K3.23}
$$

This six-probe set is not CP4-closed.  The same degree-two envelope (K3.16) also
allows

$$
(N_{x^2},N_{y^2},N_{yz})
:=\mu^{4\epsilon}\int\frac{d^d\ell\,d^dk}{(2\pi)^{2d}}
\frac{(x^2,y^2,yz)}{K'},
\tag{K3.23a}
$$

whose coefficients and required denominator masks cannot be fixed before CP4.

The exact exchange
$(\ell,k,q_1,q_2)\leftrightarrow(k,\ell,q_2,q_1)$ requires

$$
N_1(s_1,s_2,u_{12})=N_1(s_2,s_1,u_{12}).
\tag{K3.24}
$$

Thus the former draft-master pair
$-s_1/(3072\pi^4)$ and $-s_2/(3072\pi^4)$ is impossible for $s_1\ne s_2$.  Its first
omitted term appears when the inner triangle is shifted by

$$
k=K+R,\qquad \widetilde R=-\eta\widetilde\ell,\qquad
\mu_k^2=\mu_K^2+\eta^2\mu_\ell^2-2\eta\mu_{\ell K}.
\tag{K3.25}
$$

The $\eta^2\mu_\ell^2$ term is even and cannot be discarded.  Joint Gaussian integration,
including both primary subgraph corners, gives

$$
\boxed{
\begin{aligned}
N_1|_{\epsilon=0}
&=-\frac{2(s_1+s_2)-u_{12}}{24576\pi^4},\\
N_2&=-\frac{s_2}{18432\pi^4}\frac1\epsilon+O(\epsilon^0),\\
N_3&=\frac{s_1+s_2}{12288\pi^4}\frac1\epsilon+O(\epsilon^0),\\
N_4|_{\epsilon=0}&=-\frac1{1024\pi^4},\\
N_5&=\frac1{1024\pi^4}\frac1\epsilon+O(\epsilon^0),\\
N_6&=\frac1{1024\pi^4}\frac1\epsilon+O(\epsilon^0).
\end{aligned}}
\tag{K3.26}
$$

The exact ingredients are

$$
\operatorname{Res}_{\epsilon=0}\int d\Omega_4AB
\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}}=\frac{s_1+s_2}{12},
\quad
\int d\Omega_4\frac{C}{U^3}=\frac12,
\quad
\int d\Omega_4\frac{C^2F}{U^5}
=\frac{s_1+s_2}{24}+\frac{u_{12}}{48}.
\tag{K3.27}
$$

At $(s_1,s_2,u_{12})=(1,2,0.3)$,

$$
N_1(0)=-\frac{19}{81920\pi^4}=-2.3810261577026656\times10^{-6}.
\tag{K3.28}
$$

The direct parameter checks are

| $\epsilon$ | $N_1$ | $N_2$ | $N_3$ | $N_4$ | $N_5$ | $N_6$ |
|---:|---:|---:|---:|---:|---:|---:|
| 0.03 | $-3.47\,10^{-6}$ | $-5.06\,10^{-5}$ | $1.15\,10^{-4}$ | $-1.19\,10^{-5}$ | $4.42\,10^{-4}$ | $4.25\,10^{-4}$ |
| 0.02 | $-3.06\,10^{-6}$ | $-6.85\,10^{-5}$ | $1.55\,10^{-4}$ | $-1.12\,10^{-5}$ | $6.04\,10^{-4}$ | $5.89\,10^{-4}$ |
| 0.01 | $-2.70\,10^{-6}$ | $-1.24\,10^{-4}$ | $2.79\,10^{-4}$ | $-1.06\,10^{-5}$ | $1.10\,10^{-3}$ | $1.09\,10^{-3}$ |

The generic finite parts of $N_2,N_3,N_5,N_6$, the parents
$N_{x^2},N_{y^2},N_{yz}$, all one-denominator daughters, and all hatted tensor
numerators are not accepted: CP4 supplies neither their required denominator masks
nor numerator words.  Their typed status is

$$
\boxed{\texttt{BLOCKED\_CP4\_NUMERATOR\_INVENTORY}}.
\tag{K3.29}
$$

## 8. Assembly: the final result

The six insertion-color assignments form a rank-five half-ladder sum, not the
length-two Casimir tensor:

$$
\boxed{
\mathscr C^{ABC}{}_{DE}:=
\sum_{\rho\in S_3(A,B,C)}
\kappa^{AA'}\kappa^{BB'}\kappa^{CC'}
c_{D\rho'_1M}\kappa^{MM'}c_{M'\rho'_2N}
\kappa^{NN'}c_{N'\rho'_3E}.}
\tag{K3.30}
$$

Here $(\rho'_1,\rho'_2,\rho'_3):=\rho(A',B',C')$.

It satisfies
$\mathscr C^{ABC}{}_{DE}=\mathscr C^{(ABC)}{}_{DE}$ and
$\mathscr C^{ABC}{}_{ED}=-\mathscr C^{ABC}{}_{DE}$.  For
$SU(N)$ with $\kappa_{AB}=\delta_{AB}/2$ and $c_{ABC}=f_{ABC}/2$,

$$
\boxed{
\mathscr C^{ABC}{}_{DE}
=4\sum_{\rho\in S_3(A,B,C)}
f_{D\rho_1M}f_{M\rho_2N}f_{N\rho_3E}.}
\tag{K3.31}
$$

For $SU(2)$,

$$
\mathscr C^{ABC}{}_{DE}
=-8\big(\delta_{AB}f_{DCE}+\delta_{AC}f_{DBE}+\delta_{BC}f_{DAE}\big),
\tag{K3.32}
$$

verified on all $3^5=243$ components with maximum difference zero.  An $Nc$ reduction
would change the tensor rank and is invalid.

Define

$$
p_{i\dot a}:=\mathsf p_{+\dot a}(q_i),
\qquad
b_{12}:=\epsilon^{\dot a\dot b}p_{1\dot a}p_{2\dot b}.
$$

Schouten reduction gives the minimal covariant output shell

$$
\begin{aligned}
\mathcal B_{DA,1}^{DE}&=b_{12}p_{1\dot a}D^{D\dot a}(q_1)A^E(q_2),&
\mathcal B_{DA,2}^{DE}&=b_{12}p_{2\dot a}D^{D\dot a}(q_1)A^E(q_2),\\
\mathcal B_{AD,1}^{DE}&=b_{12}A^D(q_1)p_{1\dot a}D^{E\dot a}(q_2),&
\mathcal B_{AD,2}^{DE}&=b_{12}A^D(q_1)p_{2\dot a}D^{E\dot a}(q_2).
\end{aligned}
\tag{K3.33}
$$

Every basis element has

$$
\dim=\frac32+2+3=\frac{13}{2},
\qquad q_+=0+1+\frac32=\frac52,
\qquad |\mathcal B|=1.
\tag{K3.34}
$$

For normalized masters $\widehat M_\alpha=(16\pi^2)^2M_\alpha$, a formal projection
onto the four candidate basis rows would use

$$
\mathfrak r_\beta
:=\operatorname{FP}_{\epsilon=0}
\sum_\alpha R_{\beta\alpha}(\epsilon)\widehat M_\alpha(\epsilon),
\qquad
\beta\in\{DA1,DA2,AD1,AD2\}.
\tag{K3.35}
$$

The only accepted assembly statement is therefore a `SPECIFIED_SHELL` with an
unclassified remainder:

$$
\boxed{
\begin{aligned}
\boldsymbol\nabla_-(A^AA^BA^C)
\Big|^{\rm anomaly}_{\hbar^2,g^4,\rm kite}
={}&\frac{\hbar^2g^4}{(16\pi^2)^2}
\mathscr C^{ABC}{}_{DE}
\sum_{\beta\in\{DA1,DA2,AD1,AD2\}}
\mathfrak r_\beta\mathcal B_\beta^{DE}\\
&+\mathcal R^{ABC}_{\rm CP3/CP4},
\end{aligned}}
\tag{K3.36}
$$

with

$$
\boxed{
\mathfrak r_\beta=
\texttt{BLOCKED\_CP1\_WORD\_DERIVATION}
\oplus\texttt{BLOCKED\_CP3\_REDUCED\_ROWS}
\oplus\texttt{BLOCKED\_CP4\_CUTTING\_LEDGER}
\oplus\texttt{BLOCKED\_TWO\_LOOP\_SUBTRACTION\_SCHEME}.}
\tag{K3.37}
$$

and

$$
\boxed{
\mathcal R^{ABC}_{\rm CP3/CP4}
=\texttt{BLOCKED\_UNTYPED\_ROW\_AND\_CONTACT\_INVENTORY}.}
\tag{K3.38}
$$

No rational anomaly coefficient and no claim “this isolated length-three graph is
nonzero” passes the recorded gates.

## 9. HT comparison

1. Topology: the audited graph is exactly the $K_4-e$ two-loop Laman support.
2. Truncation pattern: the companion single-momentum theorem gives the length-2 zero;
   length-3 is the first channel in which $Q_2$ is allowed, but (K3.37) does not prove
   that this isolated graph is nonzero.
3. The quantitative acceptance target for the **full** channel (all routings summed;
   outside this single-graph memo) is Wess–Zumino consistency
   $\{Q_0,Q_2\}=-Q_1^2$ evaluated on $A^AA^BA^C$ with the settlement's locked one-loop
   kernels on the right-hand side.  It is not imposed termwise on (K3.36).

## 10. Boundary and census

This memo computes one labeled graph (all-vector lines, three cubic BCH vertices,
insertion at a degree-3 corner). Same-order contributions deferred to a future full
census: ghost-line routings; quartic-vertex routings; matter/superpotential loops
(including matter/superpotential dressing of vector lines);
insertion-side nonlinear (BCH/connection) routings; normal-product/$\mathscr Z$
scheme terms. Scheme decisions **[D3]** (two-loop evanescent ledger) and **[D4]**
(canonical routing) are as in the companion memo §10.  No two-loop $R'$ forest or
evanescent normal-product scheme is fixed by the allowed inputs; this is an additional
blocker in (K3.37).

## 11. Verification artifacts

Equation-linked local checks:

| check | result |
|---|---:|
| `engine_A/calib0.py` | CP0 five anchors `PASS` |
| `fast_cp0_cp1_engine.py` | CP0 `PASS`; CP1 eight rows `FAIL`; expected exit 3 |
| `fast_cp1_minimal_trace.py` | WW-DA-01 first divergence and Koszul sign `PASS` |
| `cp5_master_check.py` | K.11, $U/F$, Wick reconstruction, symmetry, poles, finite masters: all `PASS` |
| `cp5_exact_parameter_check.wls` | $1/2$ and $(1/24,1/24,1/48)$ exact parameter integrals `PASS` |
| `cp6_color_rank5_check.py` | all 243 $SU(2)$ components `PASS`, maximum difference 0 |
| repository suite | 169 tests: 164 direct pass, 4 skipped, one sandbox multiprocessing error; isolated unsandboxed rerun `9/9 PASS` |

The generated machine receipts are
`generated/cp0_cp4_fast_gate_report.json`,
`generated/cp0_cp4_cp1_minimal_trace.json`, and
`generated/cp5_numeric_raw.csv`.  The exact derivation audits are
`cp0_cp4_gate_audit.md` and `cp5_master_derivation.md`.
The consolidated receipt is `cp0_cp7_verification.json`.
