# Step 4. Project--Srednicki--Weinberg extended-SYM dictionary

## D4.1 Source boundary

$$
P:=\text{Project},
\qquad
S:=\text{Srednicki},
\qquad
W:=\text{Weinberg}.
\tag{D4.1}
$$

The semantic authority is the audited Git contract
`contracts/dictionaries/weinberg-srednicki-project-notation-dictionary.md`;
its reference evidence is the Git-vendored snapshot set registered by
`references/weinberg-srednicki-notation-source-ledger.json`.

| label | Git snapshot | Notion page |
|---|---|---|
| `S95` | `references/vendor/notion/srednicki/95-supersymmetry-0151805c7e85457a9928fcfd0e83da2a.md` | `0151805c7e85457a9928fcfd0e83da2a` |
| `W27.1` | `references/vendor/notion/weinberg/27-01-gauge-invariant-chiral-action-34cee2b74b3f81b6b72bd47d34df4d88.md` | `34cee2b74b3f81b6b72bd47d34df4d88` |
| `W27.2` | `references/vendor/notion/weinberg/27-02-abelian-gauge-superfield-action-34cee2b74b3f8131b10edd7a1dad0172.md` | `34cee2b74b3f8131b10edd7a1dad0172` |
| `W27.3` | `references/vendor/notion/weinberg/27-03-general-gauge-superfield-action-34cee2b74b3f812f97c2d0aa902aba5d.md` | `34cee2b74b3f812f97c2d0aa902aba5d` |
| `W27.4` | `references/vendor/notion/weinberg/27-04-renormalizable-gauge-theory-34cee2b74b3f81949500f3f35884f580.md` | `34cee2b74b3f81949500f3f35884f580` |

`SOURCE_INSUFFICIENT` means that no registered Git snapshot fixes the
displayed rule.  `NOT_DEFINED_IN_SOURCE` is used only for intrinsic
Euclidean superspace, whose absence is established by the allowed
dictionary itself.

## D4.2 Gauge normalization

The exact source-backed bosonic map is

$$
t_A=gT_A,
\qquad
\widehat V^A=gV_S^A,
\qquad
\widehat\Omega^A=-2g\Xi^A,
\tag{D4.2}
$$

$$
\left(A_{P,\mu}^A,F_{P,\mu\nu}^A,\mathscr D_P^A\right)
:=\left(\widehat V_\mu^A,
\widehat f_{\mu\nu}^A,\widehat D^A\right),
\tag{D4.2a}
$$

and hence

$$
A_{P,\mu}^A=g v_{S,\mu}^A=g V_{c,\mu}^A,
\qquad
F_{P,\mu\nu}^A=gF_{S,\mu\nu}^A=gf_{c,\mu\nu}^A,
\qquad
\mathscr D_P^A=gD_S^A=gD_c^A.
\tag{D4.3}
$$

Sources: dictionary (D.9.3)--(D.9.11); `S95` lines 436--447,
506--511, 645--686; `W27.1` lines 141--165, 483--493;
`W27.3` lines 287--320.

The quadratic invariant-form dictionary is

$$
\kappa_{AB}^{P}
\longleftrightarrow\delta_{AB}^{S}
\longleftrightarrow\delta_{AB}^{W};
\tag{D4.3a}
$$

this is a basis translation, not a claim that every Project basis is
orthonormal.  The registered pages do not fix a typed map from the
Project Weyl gaugino to Weinberg's four-component Majorana gaugino, nor
the remaining Project--Srednicki two-component phase.  Therefore

$$
\widehat\lambda_{W,4c}^A=g\lambda_{c,4c}^A,
\tag{D4.3b}
$$

but

$$
\lambda_{P,a}
\longleftrightarrow(\lambda_c)_{\rm Weyl}:
\mathrm{SOURCE\_INSUFFICIENT},
\qquad
\lambda_{P,a}\longleftrightarrow\lambda_{S,a}:
\mathrm{SOURCE\_INSUFFICIENT}.
\tag{D4.4}
$$

## D4.3 Pure \(\mathcal N=1\) SYM

| rule | Project | Srednicki | Weinberg |
|---|---|---|---|
| Wess--Zumino representative | Step 3B; (4A.20)--(4A.23) | (D.9.1), `S95` lines 388--423 | (D.9.2), `W27.1` lines 208--218, 419--421 |
| Abelian field strength | Step 3A and (4A.22)--(4A.23) | (D.9.12)--(D.9.13), `S95` lines 512--518, 583--618 | (D.9.14)--(D.9.15), `W27.2` lines 193--199, 260--304 |
| non-Abelian field strength | Step 3A | (D.9.16)--(D.9.18), `S95` lines 645--686 | (D.9.19)--(D.9.20), `W27.3` lines 183--224 |
| Lorentzian superspace action | (4A.1), (4A.4) | gauge $F$-term in `S95` lines 638--686 | (D.9.28), `W27.4` lines 627--639 |
| Lorentzian component action | (4A.5)--(4A.9) | (D.9.26), `S95` lines 620--644 | (D.9.25), (D.9.27), `W27.2` lines 41--92; `W27.3` lines 157--171, 261--320 |
| $A_\mu,\lambda,\bar\lambda,\mathscr D$ transformations | (4A.22)--(4A.26) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| off-shell closure and gauge parameter | (4A.28)--(4A.32) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| localized $C,K,j=C-K$ | (4A.33)--(4A.42) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| current divergence | (4A.43)--(4A.48) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| Euclidean action, rules, current, contour | (4A.2), (4A.10)--(4A.11), (4A.27), (4A.49)--(4A.57) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |

The three source-native kinetic densities are

$$
\mathcal L_{P,L}^{(1)}
=\frac1{g^2}\operatorname{tr}_\kappa\left[
-\frac14F_P^2+i\bar\lambda_P\bar\sigma_L^\mu
\mathcal D_\mu\lambda_P+\frac12\mathscr D_P^2\right]
+\frac{\vartheta_{\rm YM}}{32\pi^2}
\kappa_{AB}F_{P,\mu\nu}^A
\widetilde F_P^{B\mu\nu},
\tag{D4.5}
$$

$$
\mathcal L_S^{(1)}
=-\frac14F_S^2+i\lambda_S^\dagger\bar\sigma^\mu
\mathcal D_\mu\lambda_S+\frac12D_S^2,
\tag{D4.6}
$$

$$
\mathcal L_{W,c}^{(1)}
=-\frac14f_c^2-\frac12\bar\lambda_c\not{\mathcal D}\lambda_c
+\frac12D_c^2.
\tag{D4.7}
$$

Weinberg's rescaled topological term is

$$
\mathcal L_{\vartheta,W}
=\frac{\vartheta_{\rm YM}}{32\pi^2}
\widehat f_{\mu\nu}^A
\widetilde{\widehat f}^{A\mu\nu}.
\tag{D4.7a}
$$

Source: dictionary (D.9.26a)--(D.9.27).  The corresponding Srednicki
theta-angle row is `SOURCE_INSUFFICIENT`.

Equations (D4.2)--(D4.3a) map the bosonic coefficients, including the
Weinberg theta term, exactly.  The fermion comparison stops at (D4.4).

## D4.4 Pure \(\mathcal N=2\) SYM

| rule | Project | Srednicki | Weinberg |
|---|---|---|---|
| \(\mathbb V\oplus\Phi_{\rm ad}\) field content | (4.16)--(4.21) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| Lorentzian \(\mathcal N=1\)-superspace action | (4B.1)--(4B.7) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| relative metric $q_{AB}=h\kappa_{AB}$ | (4B.2)--(4B.6) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| Lorentzian component action and auxiliary triplet | (4B.9)--(4B.15) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| manifest four transformations | (4B.20), (4B.20a), Step 4A | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| hidden four transformations and WZ compensator | (4B.21)--(4B.26) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| compact $SU(2)_R$ rules | (4B.27)--(4B.33) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| all-field off-shell closure | (4B.42)--(4B.46) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| $SU(2)_R$-doublet $C,K,j$ | (4B.47)--(4B.55) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| Euclidean action, transformations, currents | (4B.8), (4B.16)--(4B.19), (4B.34)--(4B.35), (4B.52a)--(4B.58) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |

Every $\mathcal N=2$ Srednicki/Weinberg row is
`SOURCE_INSUFFICIENT`; no book coefficient is admitted by this
dictionary.

## D4.5 Pure \(\mathcal N=4\) SYM

| rule | Project | Srednicki | Weinberg |
|---|---|---|---|
| \(\mathbb V\oplus\Phi_1\oplus\Phi_2\oplus\Phi_3\) | (4.23)--(4.32) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| Lorentzian \(\mathcal N=1\)-superspace action | (4C.1)--(4C.4), (4C.13) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| cubic coefficient $u=-\sqrt2$ | (4C.5)--(4C.13) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| off-shell \(\mathcal N=1\) component action | (4C.14)--(4C.18) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| on-shell $SU(4)_R$ action | (4C.20)--(4C.23), (4C.43) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| all sixteen component transformations | (4C.24)--(4C.28), (4C.44)--(4C.48) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| \(\mathcal N=1\)-superspace reconstruction | (4C.29)--(4C.35) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| bosonic and fermionic closure surface | (4C.36)--(4C.42), (4C.55)--(4C.58) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| $SU(4)_R$-fundamental $C,K,j$ | (4C.49)--(4C.52), (4C.59)--(4C.69) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| exact \(\rho\), Fierz, Jacobi reduction | (4C.70)--(4C.71) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |

Every $\mathcal N=4$ Srednicki/Weinberg row is
`SOURCE_INSUFFICIENT`; no book coefficient is admitted by this
dictionary.

## D4.6 Translation verdict

$$
\boxed{
\begin{array}{c|ccc}
&P&S&W\\ \hline
\mathcal N=1\text{ Lorentzian gauge action}&\mathrm{DERIVED}&\mathrm{DEFINED}&\mathrm{DEFINED}\\
\mathcal N=1\text{ exact component transforms/current}&\mathrm{DERIVED}&\mathrm{SOURCE\_INSUFFICIENT}&\mathrm{SOURCE\_INSUFFICIENT}\\
\mathcal N=2&\mathrm{DERIVED}&\mathrm{SOURCE\_INSUFFICIENT}&\mathrm{SOURCE\_INSUFFICIENT}\\
\mathcal N=4&\mathrm{DERIVED}&\mathrm{SOURCE\_INSUFFICIENT}&\mathrm{SOURCE\_INSUFFICIENT}\\
\text{intrinsic Euclidean superspace}&\mathrm{DERIVED}&\mathrm{NOT\_DEFINED\_IN\_SOURCE}&\mathrm{NOT\_DEFINED\_IN\_SOURCE}\\
\text{Euclidean components/currents}&\mathrm{DERIVED}&\mathrm{SOURCE\_INSUFFICIENT}&\mathrm{SOURCE\_INSUFFICIENT}
\end{array}.}
\tag{D4.8}
$$
