# Notation spine — 3+1d SUSY QFT conventions through BV–BRST

Project 0. The shared formalism every other project imports and none redefines. Distilled
from the accepted contracts (`contracts/foundations/step-01…05a`, `contracts/dictionaries/`);
each block cites its locked tag. Columns $C/W/S$ = Project (canonical) / Weinberg / Srednicki.

Human-readable only. The machine consistency checks live in `../machine/`.

---

## 1. Indices, parity, epsilon (step-01 §1.1)

$$
\mu,\nu=0,1,2,3;\quad a,b=1,2;\quad \dot a,\dot b=\dot1,\dot2;\qquad
[A,B\}:=AB-(-1)^{|A||B|}BA
$$

$$
\eta=\operatorname{diag}(-1,+1,+1,+1),\quad \epsilon^{0123}=+1;\qquad
\epsilon^{12}=\epsilon^{\dot1\dot2}=+1,\ \epsilon_{12}=\epsilon_{\dot1\dot2}=-1
$$

$$
\psi^a=\epsilon^{ab}\psi_b,\quad \psi_a=\epsilon_{ab}\psi^b\qquad(\text{NW–SE convention})
$$

## 2. Sigma matrices, Clifford (dictionary D.2.4–D.2.6, §3)

$$
(\sigma^\mu)_{a\dot a}=(\mathbf1,\vec\sigma),\quad
(\bar\sigma^\mu)^{\dot aa}=(\mathbf1,-\vec\sigma)=\epsilon^{ab}\epsilon^{\dot a\dot b}(\sigma^\mu)_{b\dot b},\quad
\sigma^\mu\bar\sigma^\nu+\sigma^\nu\bar\sigma^\mu=-2\eta^{\mu\nu}\ (C{=}S)
$$

**Weyl ↔ Majorana / four-component:** translate through dictionary §3 (Clifford, Dirac and
Majorana fields, bilinears, Fierz) and §7 (superspace bridge). Never by symbol shape — the
$W$ column is four-component throughout.

## 3. Flat superspace and covariant derivatives (step-02a; dictionary §4, §7)

Coordinates $(x^\mu,\vartheta^a,\bar\vartheta^{\dot a})$. Supercharges and covariant
derivatives $D_a,\bar D_{\dot a}$ with
$\{D_a,\bar D_{\dot a}\}=-2i(\sigma^\mu)_{a\dot a}\partial_\mu$ (step-02a). Chiral coordinate
$y^\mu=x^\mu+i\vartheta\sigma^\mu\bar\vartheta$; the three representation surfaces (chiral /
vector / antichiral) are dictionary §7.1.

**θ-expansion (component form) of superfields** — chiral $\Phi=\phi+\sqrt2\vartheta\psi+
\vartheta\vartheta F$ in the chiral coordinate; vector $V$ in Wess–Zumino and full charts;
all locked in step-03b (component reconstruction) and step-05a §5A.5.

## 4. Representations (step-03c; step-05a §5A.6)

- **Chiral representation:** $D_a$ flat, $\bar D_{\dot a}$ gauge-dressed; $\bar\Phi\,e^V\Phi$.
- **Vector representation:** covariant $\boldsymbol\nabla_a=e^{-V}D_ae^{V}$ etc.; the
  representation the supergraph project computes in.
- Intertwiners between them: step-03c (gauge vector representation).

## 5. Gauge sector and field strengths (step-03a; 5A.33)

$$
[T_A,T_B]=ic_{AB}{}^CT_C,\quad c_{ABC}=c_{[ABC]},\quad h=g^{-2};\qquad
\mathcal W_a=-\tfrac18\bar D^2(e^{-V}D_ae^{V}),\ \ \widetilde{\mathcal W}_{\dot a}=+\tfrac18D^2(e^{V}\bar D_{\dot a}e^{-V})
$$

**Trap:** the Project field-strength normalization is $-\tfrac18$ (not the textbook
$-\tfrac14$); every downstream vertex/propagator factor is locked to it.

## 6. Extended SYM and N=4 packaging (step-04, 04a–04c)

$SU(3)\subset SU(4)_R$: chirals $\Phi_r$, $r=1,2,3$; fermions in $\mathbf4$
($\Lambda^4=\lambda$, $\Lambda^r=\psi_r$), scalars in $\mathbf6$
($\varphi^{r4}=\phi_r$, $\varphi^{rs}=\varepsilon^{rst}\widetilde\phi_t$). Superpotential
$\mathscr U_4=-\tfrac{\sqrt2}{6g^2}\varepsilon_{rst}c_{ABC}\Phi_r^A\Phi_s^B\Phi_t^C$ (4C.12–13).

## 7. BV–BRST formalism (step-03d; step-05a §5A.7–5A.8)

Minimal BV action, antibracket, classical master equation, QME recursion (5A.41–5A.42f);
FP ghosts $\mathfrak c,\widetilde{\mathfrak c}$, non-minimal doublets, gauge fermion
$\Psi_{\mathcal F,\mathcal Y}$ (5A.43–5A.48). The regulated path integral and its
Schwinger–Dyson identity are step-03d (3D.34).

## 8. Signatures: Lorentzian and Euclidean (step-05a §5A.2)

$$
R\in\{L,E\};\quad \eta_L=+1,\ \eta_E=-1;\quad \tau_L=i/\hbar,\ \tau_E=-1/\hbar
$$

**Euclidean lock:** $\Phi_r$ and $\widetilde\Phi_r$ are **independent** (no conjugation
relates them). Wick continuation is dictionary §6.3. Both signatures are built in parallel;
each project declares which it uses.

## 9. Superpropagators and loop saturation (5A.64–5A.74)

$$
\langle VV\rangle=-\frac{2\hbar g^2\kappa^{AB}}{p^2}\delta^4(\vartheta_{12}),\qquad
\langle\Phi\widetilde\Phi\rangle=+\frac{\hbar g^2\kappa^{AB}}{16p^2}\bar D_1^2D_1^2\delta^4(\vartheta_{12})
$$

$$
\delta\Phi/\delta\Phi'=\mathcal P_+\delta^8,\qquad
\delta^4(\vartheta_{12})D^2\bar D^2\delta^4(\vartheta_{12})=16\,\delta^4(\vartheta_{12})
$$

Projectors $\mathcal P_\pm=\tfrac{\bar D^2D^2}{16\Box}\,/\,\tfrac{D^2\bar D^2}{16\Box}$,
$\mathcal P_T=-\tfrac{D^a\bar D^2D_a}{8\Box}$, $\mathcal P_T+\mathcal P_++\mathcal P_-=1$.

## 10. Standing traps

1. $\mathcal W_a$ normalization $-\tfrac18$, not $-\tfrac14$.
2. Euclidean $\Phi/\widetilde\Phi$ independence — propagator orientation $\mathcal P_+$ vs
   $\mathcal P_-$ tracked per line, never by conjugation.
3. Half-superspace vertex → full-measure conversion costs one $-\tfrac14\bar D^2$ (or $D^2$).
4. Weinberg four-component ↔ two-component only via dictionary §3/§7.
5. Vector vs chiral representation: pick one per calculation; intertwine via step-03c.

## Source contracts (verbatim, hash-pinned)

`step-01, 02a, 02b, 02c` (superspace, superconformal) · `03a, 03b, 03c, 03d` (gauge action,
components, vector rep, BV–BRST) · `04, 04a, 04b, 04c` (extended SYM) · `05a` (BV–BRST +
Feynman-rule grammar) · `contracts/dictionaries/weinberg-srednicki-project-notation-dictionary.md`
(1559 lines, tags D.\*). During the split these remain under `contracts/`; Phase 2 relocates
them under `notation/` proper.
