# Step 5 one-loop covariant-completion review — round 3 audit

Status: `EXTERNAL_GAP_REVIEW_AUDITED`

The response is gap review only.  No coefficient is imported.

## Admitted after independent Project derivation

$$
\mathscr I^{AB}=\mathscr I^{BA},
\qquad
P_{\operatorname{Sym}^2(\mathrm{Adj})}\mathscr O_- =0,
\qquad
\mathscr O_+\in\operatorname{Sym}^2(\mathrm{Adj}).
$$

The ordered ledger and the local source quotient are distinct:

$$
\Gamma^{A|B}(p_1,p_2)\in\mathrm{Adj}\otimes\mathrm{Adj},
$$

$$
\pi_{\mathrm{loc}}\Gamma^{AB}
=\frac12\left[
\Gamma^{A|B}(p_1,p_2)+\Gamma^{B|A}(p_2,p_1)
\right]
\in\operatorname{Sym}^2(\mathrm{Adj}).
$$

For the source port,

$$
|J|=1,
\qquad
\left|I=\frac{\vec\delta H}{\delta J}\right|=1,
\qquad
|JI|=0.
$$

The finite injectivity gate is

$$
\{v\in\ker C:Lv\in B_2\}=\operatorname{im}B.
$$

Its relation blocks must contain

$$
R_{\mathrm{IBP/source\ jets}},\quad
R_{\mathrm{placements}},\quad
R_{\mathrm{commutators}},\quad
R_{\mathrm{color}},\quad
R_{\mathrm{evanescent}},\quad
L_{\ell_2}.
$$

In particular,

$$
0=\int d^8z\left[
(\nabla_aJ)\mathcal O^a
+(-1)^{|J|}J\nabla_a\mathcal O^a
\right],
$$

$$
|J|=1
\quad\Longrightarrow\quad
\int d^8z\,J\nabla_a\mathcal O^a
=\int d^8z\,(\nabla_aJ)\mathcal O^a
$$

must be represented in the source-jet complex; source derivatives cannot be
discarded before the quotient is fixed.

## Resolved locally beyond the response

The response left the graph reflection sign uncomputed.  The Project replay
contains the full pre-D word and endpoint-transfer ledger:

$$
(W,Q_D,\widetilde W,Q_{\bar D})
\longmapsto
(\widetilde W,Q_{\bar D},W,Q_D),
\qquad
(-1)^4=+1.
$$

Equivalently, separating the two odd-subword permutations gives

$$
s_{\mathrm{ext}}=(-1)^1=-1,
\qquad
s_{\mathrm{quantum}}=(-1)^1=-1,
\qquad
s_{\mathrm{ref}}=s_{\mathrm{ext}}s_{\mathrm{quantum}}=+1.
$$

The reflected prefactor is recomputed factor by factor:

$$
(-1)_{\mathrm{ext}}(-1)_{\mathrm{quantum}}
\left(-\frac{ih}{8}\right)
\left(+\frac{ih}{8}\right)
(-2g^2)^3
=-\frac18h^2g^6
=-\frac18g^2,
\qquad hg^2=1.
$$

Therefore the accepted tensor word is

$$
\mathscr O_+^{AB}
=c_{ACD}c_{BCE}\left[
\widetilde W_{\dot a}^{D}\mathcal D_+{}^{\dot a}X^E
+(\mathcal D_+{}^{\dot a}X^D)\widetilde W_{\dot a}^{E}
\right],
$$

$$
\mathscr O_+^{BA}=\mathscr O_+^{AB}.
$$

## Rejected or still open

No physical \(U(1)_R\) value is imported.  The Project symbol \(r_{\mathrm f}\)
remains a formal grading.

The response does not prove the indexed relation matrix, the full
\(\mathcal N=4\) source/EOM complex, the chiral–vector frame bridge, or

$$
\ker\bar\ell_2=0.
$$

No contact-family pole, evanescent remainder, anomaly coefficient, or
one-loop exactness theorem is accepted from this response.
