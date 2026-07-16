# Step-5K memo — the triangle principle and the complete triangle census of the $(\mathfrak b,\mathfrak c)$ channel

Status: `NON_AUTHORITY_PROPOSAL`. Numbered items (5K.$n$).

Owner directive implemented (2026-07-16): *compute the one-loop triangle diagrams only;
boxes, pentagons, etc. are the dressing of the triangle that renders it gauge-covariant —
not a theorem, but very reasonable, exactly as for the ABJ anomaly.*

## 1. The triangle principle (recorded as a working principle, with its status)

> **(5K.P) Triangle principle.** The one-loop anomaly coefficient of every letter-pair
> channel is carried by the **triangle** diagrams (three internal lines; in the project
> formalism: the $\partial\!\cdot\!j_-$ insertion node $x$ + the letter-pair node $y$ +
> **one** interaction vertex $w$). Higher-polygon graphs (the boxes of 5G, pentagons, …)
> are the gauge-covariantization dressing of the triangle output
> ($\partial\to\mathcal D$, $\partial A\to F$), fixed by covariance, contributing no
> independent coefficient — the ABJ pattern (AVV fixes the coefficient; AVVV etc. follow
> from consistency).

Status: **owner-adopted working principle**, not a theorem; its consistency check is that
the triangle sum alone reproduces the HT table (which is itself a triangle computation —
HT's graphs are letter-pair + two cubic vertices, and the project's insertion node
internalizes one vertex, 5I.4c). This supersedes the box-vs-triangle irresolution of
5J E-ii: the boxes are reclassified as dressing; the 5G $\mu^2$-box computation is
reinterpreted as the covariantized descendant of the triangle, not an independent term.

## 2. Complete triangle census of $(\mathfrak b_r,\mathfrak c^s)\to\widetilde\lambda\widetilde\lambda$

External data: pair $(\psi^{A}_{r+}\widetilde\phi^{B}_s)(y)$; two amputated
$\widetilde\lambda$ outputs; one $V_2=-\sqrt2h\,c\,\phi\widetilde\psi\widetilde\lambda$
vertex at $w$. Scanning **all** terms of the insertion (5D.4) for (three-line, two-output)
closures — this census is larger than the 5F/5H lists and replaces them for this channel:

| # | insertion piece at $x$ | fields at $x$ | loop lines $(x\!-\!y,\,y\!-\!w,\,w\!-\!x)$ | flavor |
|---|---|---|---|---|
| T-a | $\mathcal I_6^{Y}$: $-\sqrt2(\sigma^m\mathcal D_m\widetilde\phi_t)_{-\dot a}\cdot(-\sqrt2h)c\,\phi_t\widetilde\lambda^{\dot a}$ | $\widetilde\phi_t(\partial),\phi_t,\widetilde\lambda$ | $(\phi\widetilde\phi,\ \psi\widetilde\psi,\ \widetilde\phi\phi)$ | $t{=}s$, $u{=}t$, $u{=}r\Rightarrow\delta_{rs}$ |
| T-b | $\mathcal I_2$: $+i\mathcal E_{\mathscr D}(\sigma^n\partial_n\widetilde\lambda)_-$, $C_0$-part $\propto h(\phi_t\times\widetilde\phi_t)$ | $\phi_t,\widetilde\phi_t,\widetilde\lambda(\partial)$ | same pattern | $\delta_{rs}$ |
| T-c | $\mathcal I_1$: $-\mathcal E_A^n(\sigma_n\widetilde\lambda)_-$, scalar-current part $\propto h(\mathcal D_n\widetilde\phi_t\times\phi_t+\dots)$ | $\widetilde\phi_t(\partial),\phi_t,\widetilde\lambda$ | same pattern | $\delta_{rs}$ |
| T-d | $\mathcal I_1$: fermion-current part $\propto h(\widetilde\psi_t\bar\sigma_n\times\psi_t)$ | $\widetilde\psi_t,\psi_t,\widetilde\lambda$ | $(\psi\widetilde\psi,\ \phi\widetilde\phi,\ \widetilde\psi\psi)$ | $\delta_{rs}$ |
| T-e | $\mathcal I_4$: $+\sqrt2\,\mathcal E_{\phi_t}\psi_{t-}$, Yukawa part $\mathcal E_\phi\supset-\sqrt2h\,c\,(\widetilde\psi_t\widetilde\lambda)$ | $\widetilde\psi_t,\widetilde\lambda,\psi_{t-}$ | $(\psi\widetilde\psi,\ \phi\widetilde\phi,\ \widetilde\psi\psi)$ | $\delta_{rs}$ |
| T-f | $\mathcal I_3$: $i\epsilon_{b-}\mathscr D\,\mathcal E_\lambda^b$, $\mathscr D$-contact$\times C_0$-vertex $\to$ eff. $(\phi\widetilde\phi)$, $\mathcal E_\lambda$-kinetic $\partial(\widetilde\lambda\bar\sigma)$ | $\phi,\widetilde\phi,\widetilde\lambda(\partial)$ | same as T-b | $\delta_{rs}$ |

Absences (proved by end-scan): all $\mathcal I_5$/$\mathcal I_7$ pieces dead-end on
$F$-contacts into $\widetilde F\widetilde\phi\widetilde\phi$ (no $\widetilde\lambda$
output) or produce **undotted** $\lambda$ outputs (wrong output species — those feed
other channels); $\mathcal I_6^{\rm kin}$/$\mathcal E_\phi^{\rm kin}$ pieces have only
one output at one vertex — they are the **box** seeds, reclassified as dressing by
(5K.P).

Structural facts, all six triangles: color word $=c\times c$ (one structure constant from
the insertion piece or its contact-resolved vertex, one from $V_2$) — the
$f_{ACD}f_{BCE}$ family; flavor chain closes on $\delta_{rs}$ in every case; outputs are
the two $\widetilde\lambda$'s, one at $x$ (carrying the insertion's frame projection
$(\sigma)_{-\dot a}$ or $\partial_-$-structure) and one at $w$ (carrying the vertex
$\epsilon^{\dot a\dot b}$).

## 3. Template integrand (T-a), all factors explicit

Momenta: all incoming; pair momentum $p$ at $y$, outputs $k_1$ (at $x$), $k_2$ (at $w$),
insertion balance $q$; loop $\ell$ on $x\!\to\!y$ ($\phi$-line), $\ell+p_\psi$ on
$y\!\to\!w$ ($\psi$-line), $\ell'$ on $w\!\to\!x$ ($\phi$-line). With the propagators
(5G.1) and vertex (5G.2):

$$
\mathcal T_a=
\underbrace{(+2h)\,c_{BAC}\,(\sigma^m)_{-\dot a}}_{\mathcal I_6^Y}
\underbrace{(i\ell'_m)}_{\mathcal D\widetilde\phi}
\cdot
\underbrace{\frac{\sqrt2h}{\hbar}c_{A''B''C''}\epsilon^{\dot b\dot c}}_{V_2}
\cdot
\frac{\hbar g^2}{\ell^2}\,
\frac{-i\hbar g^2(\sigma\!\cdot\!(\ell{+}p_\psi))_{+\dot b}}{(\ell{+}p_\psi)^2}\,
\frac{\hbar g^2}{\ell'^2}\;
\times\;(\text{color/flavor}\ \kappa\text{-transport};\ \text{Koszul sign})
\tag{5K.1}
$$

with the two $\widetilde\lambda$ output indices $(\dot a$ at $x$, $\dot c$ at $w)$, and
$\ell'=\ell-q_{\rm loop}$-routing fixed by the all-incoming assignment. Loop-momentum
numerator: **two** powers ($\ell'_m$ from the insertion derivative, $\ell$ from the
fermion line) — individually log-divergent; the divergences of T-a…T-f must cancel in the
sum (the channel's contact terms vanish, so the summed output is the finite local
anomaly); the DRED-sensitive step is the $\widehat\delta_{mn}\langle\ell_m\ell_n\rangle$
average against the four-dimensional Fierz, exactly the (5G.10) mechanism, now applied to
the **sum** of six numerators rather than one graph.

## 4. Evaluation scheme (the remaining computation, precisely bounded)

1. assemble the six numerators (5K.1)-style — each is (coupling)$\times$($\le2$ loop
   momenta)$\times$($\sigma$-chain with one $-$-frame projection and one
   $\epsilon^{\dot b\dot c}$);
2. sum; Feynman-parametrize the common $1/D^3$;
3. split $\langle\ell\ell\rangle$ into $\bar\delta$ and evanescent parts; the
   $1/\epsilon\times$evanescent finite terms and the $\mu^2$-master terms together give
   the local $\widetilde\lambda_{\dot a}\widetilde\lambda^{\dot a}$ vertex;
4. output: $c_3\cdot\delta_{rs}\,\mathbb F^{AB}{}_{DE}\,\widetilde\lambda\widetilde\lambda$
   with $c_3$ an exact rational $\times\frac1{32\pi^2}$;
5. verdict: compare $c_3$ (and then $c_4$, $c_5$ from the same six-piece scan of the
   $(\mathfrak b,\mathfrak b)$, $(\mathfrak f,\mathfrak c)$ channels) against
   HT T3/T4/T5 through the 5J dictionary ($\zeta_Q=\tfrac12$, unit $\Phi$-letters,
   $\zeta_b$ from W-J4).

Honest status: census **closed** under (5K.P) — six triangles, absences proved; the
template integrand is assembled; the six-numerator sum and its DRED evaluation (steps
2–4) are the next computation and are **not yet done**. No coefficient is claimed.

---

**Addendum (same day, after execution — see Step-5L).** Steps 2–3 of §4 are
superseded: the six triangles do **not** cancel divergences among themselves; each
cancels *identically at the integrand level* against the "1"-branch of its parent
insertion piece's SD collapse (pairing theorem (5L.1), machine-certified for the T-a
pair). The channel coefficient is carried by the $\mu^2$-branch of the unique
fermionic collapse site, which pinches to the three-denominator $\mu^2$-triangle
master ((5L.2)) — this is the precise realization of (5K.P). The evaluated
coefficient is $c_3=-\sqrt2$ in units $\hbar g^2/32\pi^2$ ((5L.4)).
