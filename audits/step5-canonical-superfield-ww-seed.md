# Canonical-superfield WW seed: conditional arithmetic audit

Authority: `00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.  HT target 与 imported candidate coefficient 未进入计算。

## 1. Notation

$$
\epsilon^{+-}=1,\qquad \epsilon_{+-}=-1,\qquad
D^+=D_-,\qquad D^-=-D_+,
$$

$$
D^2=2D_-D_+,\qquad
e^{ip\cdot x}:\ \partial_m\mapsto ip_m,\qquad
\mathsf p_{a\dot a}=-i(\sigma_E^m)_{a\dot a}p_m.
$$

因此

$$
\{D_a,\bar D_{\dot a}\}=2\mathsf p_{a\dot a}.
$$

## 2. Absorbed-to-canonical dictionary

$$
\boxed{\mathcal V_P=2g v,\qquad \mathcal W_P=gW_{\rm can}},
$$

$$
v=\frac{\mathcal V_P}{2g},\qquad
W_{\rm can}=\frac{\mathcal W_P}g.
$$

由

$$
e^{-X}De^X=DX+\frac12[DX,X]+O(X^3),\qquad X=2gv,
$$

得到

$$
W_{\rm can,a}=W_{(1)a}+gW_{(2)a}+O(g^2),
$$

$$
W_{(1)a}=-\frac14\bar D^2D_av,
\qquad
W_{(2)a}=-\frac14\bar D^2\llbracket D_av,v\rrbracket.
$$

## 3. Background Fermi--Feynman gauge

在 residual-free slice 锁定

$$
\mathcal F_+=-\frac14(\bar{\boldsymbol\nabla}_B)^2(2gv),
\qquad
\mathcal F_-=-\frac14(\boldsymbol\nabla_B)^2(2gv),
\qquad \alpha=1.
$$

Gauge action 与该 gauge-fermion Hessian 的和为

$$
S_0=\frac12\int d^dx\,d^4\theta\,
\kappa_{AB}v^A(-\partial^2)v^B.
$$

故

$$
K_{AB}(p)=\kappa_{AB}p^2,
\qquad
K_{AC}(p)\frac{\kappa^{CB}}{p^2}=\delta_A{}^B,
$$

$$
\boxed{
\langle v^A(p,\theta_1)v^B(-p,\theta_2)\rangle_0
=\hbar\frac{\kappa^{AB}}{p^2}
\delta^4(\theta_1-\theta_2)}.
$$

## 4. Two background field-strength vertices

Chiral action 的 cubic cross term：

$$
S_{(3),+}
=-\frac g2\int d^dx\,d^4\theta\,
\operatorname{tr}_\kappa
\left(W_{(1)}^a\llbracket D_av,v\rrbracket\right).
$$

Antichiral term：

$$
S_{(3),-}
=+\frac g2\int d^dx\,d^4\theta\,
\operatorname{tr}_\kappa
\left(\widetilde W_{(1)\dot a}
\llbracket\bar D^{\dot a}v,v\rrbracket\right).
$$

Ordered second variation 后，再乘 $e^{-S_{\rm int}/\hbar}$ 的 minus sign：

$$
\boxed{
\mathcal V_W
=-\frac{ig}2c_{UCE}W^{E\gamma}
(D_{C\gamma}-D_{U\gamma})},
$$

$$
\boxed{
\mathcal V_{\widetilde W}
=+\frac{ig}2c_{UCD}\widetilde W^D_{\dot\gamma}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma})}.
$$

因此

$$
\left(+\frac{ig}2\right)
\left(-\frac{ig}2\right)=\frac{g^2}4.
$$

## 5. Ordered source and Wick weight

$$
K_+=-\frac14D_+\bar D^2D_+,
$$

$$
\mathcal I_{(2)}^{AB}
=D_-\left[(K_+v^A)(K_+v^B)\right]
=(D_-K_+v^A)(K_+v^B)
+(K_+v^A)(D_-K_+v^B).
$$

Fixed orientation 中 action expansion 给出

$$
\frac1{2!}
\left(S_{\widetilde W}S_W+S_WS_{\widetilde W}\right)
=S_{\widetilde W}S_W.
$$

故

$$
\boxed{w_{\rm Wick}=\frac12(1+1)=1}.
$$

这两个 label assignments 不是两个 graph orientations。

## 6. Eight derivative-endpoint rows

The table records the endpoint-sign ledger.  Its signs remain conditional until a full noncommutative superspace integration-by-parts trace derives every transfer from one explicit $D$-word.

| id | $D_-$ placement | $\bar D$ endpoint | $D$ endpoint | raw sign | transfer sign | final sign | numerator |
|---|---:|---:|---:|---:|---:|---:|---|
| WW-DA-01 | A | r0 | r1 | -1 | -1 | 1 | `(r0)_(+ dotbeta) p^(dotbeta gamma) (r1)_(gamma dot-alpha)` |
| WW-DA-02 | A | r0 | r2 | 1 | 1 | 1 | `(r0)_(+ dotbeta) p^(dotbeta gamma) (r2)_(gamma dot-alpha)` |
| WW-DA-03 | A | r1 | r1 | 1 | 1 | 1 | `(r1)_(+ dotbeta) p^(dotbeta gamma) (r1)_(gamma dot-alpha)` |
| WW-DA-04 | A | r1 | r2 | -1 | -1 | 1 | `(r1)_(+ dotbeta) p^(dotbeta gamma) (r2)_(gamma dot-alpha)` |
| WW-DA-05 | B | r0 | r1 | -1 | -1 | 1 | `(r0)_(+ dotbeta) p^(dotbeta gamma) (r1)_(gamma dot-alpha)` |
| WW-DA-06 | B | r0 | r2 | 1 | 1 | 1 | `(r0)_(+ dotbeta) p^(dotbeta gamma) (r2)_(gamma dot-alpha)` |
| WW-DA-07 | B | r1 | r1 | 1 | 1 | 1 | `(r1)_(+ dotbeta) p^(dotbeta gamma) (r1)_(gamma dot-alpha)` |
| WW-DA-08 | B | r1 | r2 | -1 | -1 | 1 | `(r1)_(+ dotbeta) p^(dotbeta gamma) (r2)_(gamma dot-alpha)` |

每个 placement 的四项严格相加为

$$
\left[(r_0)_{+\dot\beta}+(r_1)_{+\dot\beta}\right]
\mathsf p^{\dot\beta\gamma}
\left[(r_1)_\gamma{}^{\dot\alpha}+(r_2)_\gamma{}^{\dot\alpha}\right].
$$

定义

$$
r_0=k,\qquad r_1=k+q,\qquad r_2=k+P,\qquad P=p+q,
$$

$$
L_1=r_0+r_1=2k+q,
\qquad
L_2=r_1+r_2=2k+p+2q.
$$

## 7. D-algebra weight

$$
D_-K_+=-\frac18D^2\bar D^2D_+,
$$

$$
\left(-\frac18\right)\left(-\frac14\right)=\frac1{32}.
$$

$$
[D^2\bar D^2\delta^4(\theta)]_{\theta=0}
=(D^2\theta^2)(\bar D^2\bar\theta^2)=(-4)(-4)=16.
$$

两个 mixed anticommutators 各给出 $2$：

$$
\boxed{w_{D\text{-alg}}=\frac1{32}\cdot16\cdot2\cdot2=2}.
$$

这里没有乘 Wick weight；$w_{\rm Wick}=1$ 已独立固定。

The two factors $2$ are arithmetic inputs in this checkpoint, not outputs of an explicit $D$-word rewrite engine:

$$
\boxed{\texttt{BLOCKED\_EXPLICIT\_WW\_D\_ALGEBRA\_WORD\_DERIVATION}}.
$$

## 8. Fixed-orientation preintegral

令

$$
\mathcal C^{AB}{}_{DE}
=\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}.
$$

再定义

$$
T_{\mu\rho\nu,+}{}^{\dot\alpha}
:=(\sigma_{E,\mu})_{+\dot\beta}
(\bar\sigma_{E,\rho})^{\dot\beta\gamma}
(\sigma_{E,\nu})_\gamma{}^{\dot\alpha},
\qquad
X^E(p):=D_+W_+^E(p),
$$

$$
\mathcal O_{A,\mu\nu}^{DE}
:=\widetilde W^D_{\dot\alpha}(q)\,p^\rho X^E(p)\,
T_{\mu\rho\nu,+}{}^{\dot\alpha}.
$$

下标 $A$ 表示 marked $D_-$ placement；$B$ placement 保持为另一 ordered descendant $\mathcal O_B$，不并入 $\mathcal O_A$ 的 multiplicity。

对一个 marked $D_-$ placement：

$$
\frac{g^2}4\times w_{\rm Wick}\times w_{D\text{-alg}}
=\frac{g^2}4\times1\times2=\frac{g^2}2.
$$

$$
\boxed{
\Gamma_{T,A}
=\frac{\hbar g^2}2\mathcal C^{AB}{}_{DE}
\mathcal O^{DE}_{A,\mu\nu}
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{L_1^\mu L_2^\nu}
{k^2(k+q)^2(k+P)^2}}.
$$

两个 $D_-$ placements 对应两个 ordered external descendants，不能作为额外 multiplicity 相加到同一个 coefficient。

## 9. UV pole

$$
\frac1{D_0D_1D_2}
=2\int_{x,y,z\ge0}dx\,dy\,dz\,
\delta(1-x-y-z)\frac1{(\ell^2+\Delta)^3},
$$

$$
\ell=k+yq+zP,
\qquad
\Delta=xyq^2+xzP^2+yzp^2.
$$

UV quadratic numerator 为 $4\ell^\mu\ell^\nu$，且

$$
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^\mu\ell^\nu}{(\ell^2+\Delta)^3}
=\frac{\widehat\delta^{\mu\nu}}d(J_2-\Delta J_3),
$$

$$
J_2
=\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\Delta^{-\epsilon},
\qquad
\operatorname{Res}_{\epsilon=0}J_2=\frac1{16\pi^2},
$$

$$
\operatorname{Res}_{\epsilon=0}(\Delta J_3)=0,
\qquad
\int dx\,dy\,dz\,\delta(1-x-y-z)=\frac12.
$$

因此 tensor residue multiplier 是

$$
2\times4\times\frac14\times\frac12=1,
$$

$$
\operatorname{Res}_{\epsilon=0}
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{L_1^\mu L_2^\nu}{D_0D_1D_2}
=\frac{\widehat\delta^{\mu\nu}}{16\pi^2}.
$$

最终

$$
\boxed{
\Gamma_{T,A}\Big|_{1/\epsilon}
=+\frac{\hbar g^2}{32\pi^2\epsilon}
\mathcal C^{AB}{}_{DE}
\mathcal O^{DE}_{A,\mu\nu}
\widehat\delta^{\mu\nu}}.
$$

## 10. Mutation audit

| mutation | status | changed invariants |
|---|---|---|
| MUTATE_V_DICTIONARY_2_TO_1 | PASS | dictionary_W_linear |
| MUTATE_KINETIC_HESSIAN_1_TO_2 | PASS | pole, preintegral |
| MUTATE_SYMMETRY_FACTOR_HALF_TO_ONE | PASS | pole, preintegral, wick_weight |
| MUTATE_LABEL_ASSIGNMENTS_2_TO_1 | PASS | pole, preintegral, wick_weight |
| MUTATE_CLOSED_LOOP_16_TO_8 | PASS | D_weight, pole, preintegral |
| MUTATE_MIXED_ANTICOMMUTATOR_2_TO_1 | PASS | D_weight, pole, preintegral |
| MUTATE_SIMPLEX_VOLUME_HALF_TO_ONE | PASS | pole, tensor_multiplier |
| MUTATE_TENSOR_ONE_QUARTER_TO_ONE_HALF | PASS | pole, tensor_multiplier |
| MUTATE_ONE_ENDPOINT_TRANSFER_SIGN | PASS | all_row_signs |

| invariant | status |
|---|---|
| dictionary_W_linear | PASS |
| propagator_inverse | PASS |
| vertex_product | PASS |
| wick_weight | PASS |
| row_count | PASS |
| all_row_signs | PASS |
| D_weight | PASS |
| tensor_multiplier | PASS |
| preintegral | PASS |
| pole | PASS |
| all_mutations_detected | PASS |

## 11. Boundary

本 audit 只检查 isolated WW parent-triangle 的 coefficient arithmetic、Wick weight、recorded $D$-algebra numerator weight 与 ordinary metric pole。Explicit $D$-word transfer derivation、contact/collapsed/link/ghost/counterterm cuts 及 $\widehat\delta-\delta_4$ remainder 不在此 seed artifact 中宣称完成。
