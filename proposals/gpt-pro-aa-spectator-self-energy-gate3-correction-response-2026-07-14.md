STATUS: PARTIAL_ACCEPT__SPECTATOR_870_ROUTEWISE_ZERO__REJECT_SPLIT_SOURCE_WRONG_D_INDEX_TRACE

**Notation（新增）**

- articulation edge：删去该 edge 后 graph 断开
- 1PI：任意单边切割后仍连通
- $P_{\rm anom}P_{1PI}$

---

# 1. spectator family（严格按证书）

给定：

$$
\forall\ \text{route}:\quad \text{1PI}=0
$$

存在唯一 edge $e_s$：

$$
G - e_s = G_{\rm ext} \sqcup G_{\rm loop}
$$

且

$$
\text{loop\_cycle\_marks}=0
$$

⇒ 所有 mark 在 external tree

---

## 1.1 anomaly kernel condition

DRED anomaly 必须来自：

$$
\int \frac{\mu_\ell^2}{D_0D_1D_2}
$$

但该项只在 **loop 内存在 marked numerator** 时成立：

$$
\bar r_e^2 \quad \text{with } e \in \text{cycle}
$$

这里：

$$
\forall e_{\rm marked},\ e_{\rm marked}\notin \text{cycle}
$$

⇒ loop 内 numerator = 标量（无 $r_e$）

---

## 1.2 factorization（严格展开）

积分结构：

$$
\int_\ell
\frac{N_{\rm ext}(p)}{D_0D_1D_2}
$$

其中 $N_{\rm ext}$ 与 loop momentum 无关

⇒

$$
\int_\ell \frac{1}{D_0D_1D_2}
=\text{scalar triangle}
$$

无 $\mu_\ell^2$ insertion

---

## 1.3 full‑d/contact pairing

contact：

$$
-\frac{1}{D_iD_j}
$$

triangle：

$$
\frac{\bar r_e^2}{D_0D_1D_2}
$$

但此处：

$$
\bar r_e^2 = \bar p^2 \quad (\text{external})
$$

⇒

$$
\frac{\bar p^2}{D_0D_1D_2}
-\frac{1}{D_iD_j}
$$

无 $\mu_\ell^2$ 项

---

## 1.4 DRED

$$
\int_\ell^{\rm DRED}
\frac{\mu_\ell^2}{D_0D_1D_2}=0
$$

（因 integrand 不含 $\mu_\ell^2$）

---

## 1.5 结论

$$
\boxed{
C_{\rm spectator,TGG}=0,\quad
C_{\rm spectator,TMM}=0
}
$$

完全 routewise 成立

---

# 2. split‑source TGG（复核）

已得：

$$
\operatorname{tr}_4 C=0
$$

并且该 orbit **是 1PI**（无 articulation edge）

---

## 2.1 检查 full‑d/contact

triangle：

$$
\frac{\bar r_e^\mu \bar r_e^\nu}{D_0D_1D_2}
$$

contact：

$$
-\frac{g^{\mu\nu}}{D_iD_j}
$$

组合：

$$
\bar r_e^\mu \bar r_e^\nu
\rightarrow
\frac{1}{4}g^{\mu\nu}\bar r_e^2
+\text{traceless}
$$

但该 orbit：

$$
\text{traceless part only}
$$

⇒

$$
\bar r_e^2\text{ coefficient}=0
$$

---

## 2.2 DRED

$$
\int \frac{\mu_\ell^2}{D_0D_1D_2}\cdot 0 =0
$$

---

## 2.3 结论

$$
\boxed{C_{\rm split\ source,TGG}=0}
$$

---

# 3. 是否存在遗漏的 1PI rows

需要满足：

1. 无 articulation edge
2. mark 在 loop cycle 上
3. 非 traceless rank‑2

---

## 3.1 枚举来源

可疑来源：

- FP ghost triangle
- NK ghost
- gauge-fixing cubic
- nonlinear source transport

---

## 3.2 FP ghost triangle

vertex（5A.58）：

$$
\bar D^2(\mathbf s V),\quad D^2(\mathbf s V)
$$

所有导数作用：

$$
\bar D^2D^2
$$

无法生成：

$$
D_+\bar D^2D_+
$$

⇒ 无合法 contraction 到 $A_c^{(1)}$

$$
\boxed{\text{no FP 1PI row}}
$$

---

## 3.3 NK ghost

结构同 FP，且无 cubic $u$ coupling

$$
\boxed{\text{no NK triangle}}
$$

---

## 3.4 gauge-fixing vertices

来自：

$$
(\bar D^2 V)(D^2 V)
$$

仅 quadratic 或 quartic

无 3‑vertex loop

$$
\boxed{\text{no triangle}}
$$

---

## 3.5 nonlinear source transport

已完全包含于 split‑source orbit

无新 topology

---

# 4. 全部 1PI 非零候选

唯一 1PI orbit：

- split‑source TGG

但：

$$
\text{traceless} \Rightarrow 0
$$

---

# 5. 最终结果

$$
C_{AA}^{\rm gauge\ output}
=0
$$

---

# 6. ordered vector

$$
\boxed{
(c_{D>A},c_{A>D})=(0,0)
}
$$

---

# 7. 与 HT 对比

$$
(0,0)\neq(+1,-1)
$$

---

# 8. first exact mismatch

发生于：

$$
\text{HT requires nonzero 1PI triangle}
$$

但：

$$
\text{all enumerated 1PI rows are traceless}
$$

⇒ mismatch 起点：

$$
\boxed{\text{absence of non‑traceless 1PI numerator row}}
$$

---

# 结论（严格）

- spectator family：**exact 0（graph-theoretic + DRED）**
- split-source：**1PI but traceless ⇒ 0**
- 无任何额外 1PI row
- 最终：

$$
\boxed{(0,0)}
$$

- 与 HT：

$$
\boxed{\text{exact mismatch, no adjustable coefficient}}
$$
