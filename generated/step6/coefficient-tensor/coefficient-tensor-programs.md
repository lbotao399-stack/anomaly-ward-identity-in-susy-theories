# Step 6 coefficient-space TensorProgramIR

Status: `PASS_LOCAL_TENSOR_PROGRAMS_GLOBAL_CONTRACTION_BLOCKED`.

## Coefficient metric

$$
M_{st}:=[e_s e_t]_{D},\qquad
\sum_tM_{st}(M^{-1})_{tu}=\delta_{su},
$$

$$
\Delta^4(\theta-\theta')=-4\prod_{i=0}^{3}(\theta_i-\theta'_i)
=\sum_{s,t}(M^{-1})_{st}e_s(\theta)e_t(\theta').
$$

$$
\langle v_s(r)v_t(-r)\rangle
=\hbar\frac{-2g^2}{r^2}(-1)^{|s|}(M^{-1})_{st}.
$$

`identity_16` is the operator identity; it is not `M_inverse`.

$$
V=\sum_{s=0}^{15}v_s e_s,\qquad |v_s|=\deg(e_s)\pmod 2,
$$

$$
(v_s e_s)(v_t e_t)=(-1)^{|v_t|\deg(e_s)}v_sv_t e_se_t.
$$

$$
H_{st}=(-1)^{|s||t|}M_{st},\qquad
(H^{-1})_{st}=(-1)^{|s|}(M^{-1})_{st}
\quad(M^{-1}_{st}\ne0).
$$

$$
[Y,Z]^C=i\,c[A,B,C]Y^A Z^B:
\quad\text{superspace AST}=Y^A Z^B,
$$

The `i` is already contained in the exact Q(i) grammar coefficient.

## Exact local compilation

- grammar terms: `22`
- oriented parents: `6`
- local TensorProgram references: `1048`
- materialization: `FACTORIZED_AST_REQUESTED_BASIS_EVALUATOR_ONLY`

## Fixtures

- `I2` `[0, 0]`: recursive=expanded, type `Exterior`, nonzero `True`
- `S3_PLUS` `[0, 0, 15]`: recursive=expanded, type `Poly`, nonzero `True`
- `S3_MINUS` `[0, 0, 15]`: recursive=expanded, type `Poly`, nonzero `True`
- `S4_PLUS` `[0, 0, 0, 15]`: recursive=expanded, type `Poly`, nonzero `True`

## Boundary

$$
\text{five-edge contraction}=\texttt{BLOCKED\_NOT\_PERFORMED},\qquad
C_{2\text{-loop}}=\varnothing.
$$

Audit: `21/21` checks pass.
