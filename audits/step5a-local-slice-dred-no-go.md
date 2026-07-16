# Step 5A local-slice and DRED no-go audit

Status: NO_GO_WITHIN_FINITE_LOCAL_TRIVIAL_PAIR_NORMAL_FORM__DRED_LEDGER_LOCKABLE_SEPARATELY

Authority: UNTRACKED_PROPOSAL_NOT_PROJECT_AUTHORITY

## 1. Definitions

$$
F:=(-\bar D_E^2V/4,-D_E^2V/4),\qquad
\mathcal A_E:=
\begin{pmatrix}
0&-\bar D_E^2/4\\
-D_E^2/4&0
\end{pmatrix},\qquad
\mathcal A_E^2=\Box_E\mathbf1,\qquad
H:=\frac h2\mathcal A_E.
$$

On the residual complement,

$$
H^{-1}=2g^2\frac{\mathcal A_E}{\Box_E}
=\mathcal Y_{E,\mathrm{FF}}.
$$

## 2. Naive localizer

Add

$$
\mathbf s_E\rho=w,\qquad \mathbf s_Ew=0,\qquad
\operatorname{gh}(\rho,w)=(-1,0),\qquad [\rho]=[w]=1.
$$

Then

$$
\mathcal Y_{\mathrm{loc}}
=\begin{pmatrix}0&\mathbf1\\\mathbf1&-H\end{pmatrix},
\qquad
\mathcal Y_{\mathrm{loc}}^{-1}
=\begin{pmatrix}H&\mathbf1\\\mathbf1&0\end{pmatrix}.
$$

$$
\frac12(F,0)\mathcal Y_{\mathrm{loc}}^{-1}\binom F0
=\frac12FHF.
$$

But

$$
\Psi_{\mathrm{loc}}^{(2)}
=\langle\mathfrak c',F\rangle
-\frac12\langle\mathfrak c',w\rangle
-\frac12\langle\rho,\mathfrak n\rangle
+\frac12\langle\rho,Hw\rangle
$$

gives

$$
\mathbf s_E\Psi_{\mathrm{loc}}^{(2)}
=\langle\mathfrak n,F\rangle
-\langle\mathfrak c',\mathbf s_EF\rangle
-\langle w,\mathfrak n\rangle
+\frac12\langle w,Hw\rangle.
$$

There is no \(\rho\) term. The auxiliary FP row has rank zero, the odd
integral is unsaturated, and Step 3D.74 fails.

## 3. Proper finite completion

Every completion in the audited normal-form class has the residual-complement form

$$
\Psi_E^{(2)}
=\langle u_0,F\rangle+\langle u_a,G\rangle
-\frac12\left\langle(u_0,u_a),
\mathcal Y\binom{v_0}{v_a}\right\rangle,
\qquad
G=KX+BF,
\qquad
\mathbf s_EX=\eta,
\qquad
\mathbf s_E\eta=0.
$$

The ghost Hessian is

$$
-\left\langle(u_0,u_a),
\begin{pmatrix}
\mathcal M&0\\
B\mathcal M&K
\end{pmatrix}
\binom c\eta
\right\rangle.
$$

Properness requires \(\mathcal M\) and \(K\) to be bijective.
Set \(Z:=\mathcal Y^{-1}\). Integrating multipliers and the proper
auxiliary coordinate gives

$$
H_{\mathrm{eff}}
=Z_{00}-Z_{0a}Z_{aa}^{-1}Z_{a0}.
$$

The ordered factorization is

$$
Z=
\begin{pmatrix}\mathbf1&Z_{0a}Z_{aa}^{-1}\\0&\mathbf1\end{pmatrix}
\begin{pmatrix}H_{\mathrm{eff}}&0\\0&Z_{aa}\end{pmatrix}
\begin{pmatrix}\mathbf1&0\\Z_{aa}^{-1}Z_{a0}&\mathbf1\end{pmatrix}.
$$

Thus

$$
\boxed{\mathcal Y_{00}=H_{\mathrm{eff}}^{-1}}.
$$

The target \(H_{\mathrm{eff}}=H\) forces

$$
\boxed{
\mathcal Y_{00}=H^{-1}
=2g^2\frac{\mathcal A_E}{\Box_E}
=\mathcal Y_{E,\mathrm{FF}}}.
$$

This is Step 5A.79. Within the audited normal-form class, a completion with
bijective residual FP blocks and invertible \(Z_{aa}\) reproduces the same
nonlocal primary block.

## 4. Nielsen--Kallosh

The naive block obeys \(\mathbf s_E\mathcal Y_{\mathrm{loc}}=0\), but
its auxiliary FP row has rank zero. A completion in the audited normal-form class forces
\(\mathcal Y_{00}=\mathcal Y_{E,\mathrm{FF}}\). Therefore no Step
3D.95b NK branch is selected for the target Fermi--Feynman Hessian.

## 5. DRED momentum ledger proposal

$$
d:=4-2\epsilon,\qquad
\delta_4^{mn}=\widehat\delta^{mn}+\breve\delta^{mn},
\qquad
\operatorname{tr}\widehat\delta=d,
\qquad
\operatorname{tr}\breve\delta=2\epsilon.
$$

$$
\widehat\delta^2=\widehat\delta,
\qquad
\breve\delta^2=\breve\delta,
\qquad
\widehat\delta\breve\delta=0.
$$

$$
X(x)=\int\frac{d^dp}{(2\pi)^d}e^{ip\cdot x}X(p),
\qquad
\partial_m\mapsto ip_m,
\qquad
\Box_E\mapsto-\widehat p^2,
\qquad
\widehat\delta^m{}_np^n=p^m,
\qquad
\breve\delta^m{}_np^n=0.
$$

$$
\int_{\widehat k}
:=\mu^{2\epsilon}\int\frac{d^d\widehat k}{(2\pi)^d},
\qquad
\widehat k^2
:=\widehat\delta_{mn}\widehat k^m\widehat k^n.
$$

Every vertex is all-incoming. The spinor algebra is four-dimensional:

$$
\sigma_E^m\bar\sigma_E^n+\sigma_E^n\bar\sigma_E^m
=2\delta_4^{mn}\mathbf1.
$$

$$
\operatorname*{Res}_{\epsilon=0}
\int_{\widehat\ell}
\frac{\widehat\ell^m\widehat\ell^n}
{(\widehat\ell^2+\Delta)^3}
=\frac{\widehat\delta^{mn}}{64\pi^2}.
$$

$$
\operatorname*{Res}_{\epsilon=0}
\int_{\widehat\ell}
\frac{(2\widehat\ell+\cdots)^m(2\widehat\ell+\cdots)^n}
{D_0D_1D_2}
=\frac{\widehat\delta^{mn}}{16\pi^2}.
$$

The cut contact carries \(\delta_4^{mn}\), so

$$
\boxed{
\widehat\delta^{mn}-\delta_4^{mn}
=-\breve\delta^{mn}}.
$$

The conditional propagators are

$$
\langle V^A(p,\vartheta_1)V^B(p',\vartheta_2)\rangle_E
=-(2\pi)^d\delta^d(p+p')
\frac{2\hbar g^2\kappa^{AB}}{\widehat p^2}
\delta^4(\vartheta_1-\vartheta_2),
$$

$$
\langle\Phi^A(p,1)\widetilde\Phi^B(p',2)\rangle_E
=(2\pi)^d\delta^d(p+p')
\frac{\hbar g^2\kappa^{AB}}{16\widehat p^2}
\bar D_1^2D_1^2\delta^4(\vartheta_1-\vartheta_2).
$$

They remain conditional because the local proper slice is absent.

## 6. Exact checks

| check | result |
|---|---|
| step5a_A_square | PASS |
| step5a_nonlocality | PASS |
| step3d_locality | PASS |
| step3d_proper_hessian | PASS |
| step3d_nk_branch | PASS |
| naive_block_identity | PASS |
| proper_completion_schur_identity | PASS |
| dred_trace_split | PASS |
