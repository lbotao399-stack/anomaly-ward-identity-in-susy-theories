# Step 5 AA gauge full-versus-selected trace audit

Status: `AA_GAUGE_GLOBAL_TRACE_NOT_EQUAL_TO_EDGE_TAGGED_CUT`.

No holomorphic-twist coefficient enters this audit.

Use

$$
r_0=\ell,
\qquad
r_2=\ell+P,
\qquad
b_0=b,
\qquad
b_2=b+B,
$$

and

$$
\det r_0=-\bar\ell^2,
\qquad
\det r_2=-\overline{(\ell+P)}^2.
$$

The corrected selected rows sum to

$$
G_{\mathcal S}
=2b_2\det r_0+2b_0\det r_2
=-2(b+B)\bar\ell^2-2b\overline{(\ell+P)}^2.
$$

The longitudinal rows give

$$
G_{\mathcal L}=-2d(a b_2-b a_2),
$$

and therefore

$$
G_{\rm full}
=2b\left[a_2(d+d_2)-b_2(c+c_2)\right].
$$

For a degree-three polynomial $N_3(\ell)$ and a degree-two polynomial $N_2(\ell)$ in four loop components, define their scalar harmonic projections by

$$
\Pi_{\rm sc}N_3
:=\frac{\bar\ell^2}{12}\Delta_\ell N_3,
\qquad
\Pi_{\rm sc}N_2
:=\frac{\bar\ell^2}{8}\Delta_\ell N_2.
$$

Exact differentiation gives

$$
\Pi_{\mathrm{sc}}G_{\mathcal S}^{(3)}=-4b\bar\ell^2,
\qquad
\Pi_{\mathrm{sc}}G_{\mathcal S}^{(2)}=-3B\bar\ell^2,
$$

$$
\Pi_{\mathrm{sc}}G_{\rm full}^{(3)}=-4b\bar\ell^2,
\qquad
\Pi_{\mathrm{sc}}G_{\rm full}^{(2)}=-2B\bar\ell^2,
$$

$$
\boxed{
\Pi_{\mathrm{sc}}G_{\mathcal L}^{(3)}=0,
\qquad
\Pi_{\mathrm{sc}}G_{\mathcal L}^{(2)}=+B\bar\ell^2.}
$$

The occurrence-tagged selected cutting defect remains

$$
G_{\mathcal S}^{\rm anom}
=-2(b_2+b_0)\mu_\ell^2
=-2(2b+B)\mu_\ell^2.
$$

Thus a global four-dimensional trace projection cannot replace the selected-edge Schwinger subtraction.  The first unresolved equality remains.

Blocker: `MISSING_ROWWISE_LONGITUDINAL_TO_CONTACT_EDGE_MAP`.

$$
\boxed{\texttt{MISSING\_ROWWISE\_LONGITUDINAL\_TO\_CONTACT\_EDGE\_MAP}.}
$$

Verification:

```text
python scripts/step5_aa_gauge_full_vs_selected_trace_exact_audit.py
```
