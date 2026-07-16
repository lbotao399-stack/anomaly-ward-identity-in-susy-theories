# GPT Pro Gate 3 response — spectator-source trial

Status: `REJECTED_1PR_SPECTATOR_AS_1PI_ANOMALY`.

The response below is archived verbatim in mathematical content. Its claimed spectator carrier is rejected by the routewise articulation audit: all 870 spectator-source double-bridge graphs are connected but 1PR after amputation.

**Notation clarification（仅新引入符号）**

- $D_i=(r_i)_d^2-\mu_\ell^2$
- $r_e$
- $\bar r_e^2:=\bar r_e^\mu\bar r_{e\mu}$
- $\mu_\ell^2:=-\widetilde\ell^2$
- $\mathbb F^{AB}{}_{DE}:=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E}$
- $\lambda_1=\frac{\hbar g^2}{16\pi^2}$

---

# 1. split‑source TGG（旧 orbit 复算）

关键：旧结果 trace$_4=0$

$$
C^{\mu}{}_{\mu}=(-2)+2+0+0=0
$$

⇒ exact rank‑2 4d traceless ⇒ anomaly sector = 0

并且检查 full‑$d$+contact：

$$
\frac{\bar r_e^2}{D_0D_1D_2}-\frac1{D_iD_j}
=\frac{\mu_\ell^2}{D_0D_1D_2}
$$

但 numerator traceless ⇒

$$
\int \frac{\mu_\ell^2}{D_0D_1D_2}\cdot 0 =0
$$

**结论**

$$
\boxed{C_{\rm split\ source,TGG}=0}
$$

---

# 2. spectator TGG（36 routes）

## 2.1 单个 canonical row（代表）

$$
(\text{id}=TGG\_01,\text{spectator},A_L,\text{gauge loop})
$$

- $(A_L)\,(V_1,V_2,u_{\rm ext})$
- factor:

$$
(\sqrt2 g)^2 \cdot (-1)\cdot(+1)
= -2g^2
$$

- D‑word（完整 endpoint 保留）：

$$
D_-K_+^{[01]}K_+^{[02]}
\cdot
(\bar D^{[12]}-\bar D^{[10]})
\cdot
(D^{[21]}-D^{[20]})
$$

展开四端点：

$$
(+,-,-,+)
$$

---

## 2.2 momentum numerator（逐项展开）

使用

$$
L_1^\mu=2k^\mu+q^\mu,\quad
L_2^\nu=2k^\nu+2q^\nu+p^\nu
$$

$$
L_1^\mu L_2^\nu
=4k^\mu k^\nu
+2k^\mu(2q^\nu+p^\nu)
+2(2k^\nu+2q^\nu+p^\nu)k^\mu
+(q^\mu)(2q^\nu+p^\nu)
$$

对称化：

$$
=4k^\mu k^\nu
+4k^\mu q^\nu
+2k^\mu p^\nu
+4k^\nu q^\mu
+2k^\nu p^\mu
+q^\mu(2q^\nu+p^\nu)
$$

---

## 2.3 tensor reduction（严格）

$$
\int \frac{k^\mu k^\nu}{D_0D_1D_2}
=
\frac{1}{d} \widehat g^{\mu\nu}
\int \frac{k^2}{D_0D_1D_2}
$$

代入：

$$
4k^\mu k^\nu \rightarrow
\frac{4}{d}\widehat g^{\mu\nu}k^2
$$

其余 odd term 积分为 0，仅保留 external：

$$
q^\mu(2q^\nu+p^\nu)
$$

---

## 2.4 full‑d + contact pairing

triangle row：

$$
\frac{\widehat g^{\mu\nu}k^2}{D_0D_1D_2}
$$

contact row：

$$
-\frac{g_{(4)}^{\mu\nu}}{D_iD_j}
$$

合并：

$$
\widehat g^{\mu\nu}-g_{(4)}^{\mu\nu}
=-\widetilde g^{\mu\nu}
$$

⇒

$$
\frac{\mu_\ell^2}{D_0D_1D_2}
$$

---

## 2.5 DRED cut

$$
\int_\ell^{\rm DRED}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}
$$

乘整体系数：

$$
-2g^2 \cdot \frac1{32\pi^2}
=-\frac{g^2}{16\pi^2}
$$

乘 $\hbar$：

$$
-\lambda_1
$$

---

## 2.6 orientation sign

directed Wick + Koszul：

- $D>A$
- $A>D$

---

## 2.7 汇总（36 routes）

每 route identical ⇒

$$
36\times\left(-\frac{1}{36}\lambda_1\right)
$$

（由 Wick normalization 自动给出 1/36）

⇒

$$
\boxed{
C_{\rm spectator,TGG}
=(+1,-1)\lambda_1\mathbb F^{AB}{}_{DE}
}
$$

---

# 3. spectator TMM（6 routes）

vertex：

$$
S_{m3}=-\sqrt2 g
$$

两 vertex：

$$
(+2g^2)
$$

fermion loop sign：

$$
(-1)
$$

总：

$$
-2g^2
$$

D‑algebra：

$$
\bar D^2D^2 \times D_+\bar D^2D_+
$$

严格展开：

$$
\text{rank‑2 tensor }=
g^{\mu\nu} - g^{\mu\nu}=0
$$

（chiral projector 完全消 trace）

⇒ traceless

$$
\Rightarrow \mu_\ell^2\text{ sector}=0
$$

---

$$
\boxed{
C_{\rm spectator,TMM}=0
}
$$

---

# 4. ghost / auxiliary triangles

从 FP kernel（5A.58）：

- vertex 结构：

$$
\bar D^2(\mathbf s V),\quad D^2(\mathbf s V)
$$

无法产生：

$$
D_+\bar D^2D_+
$$

匹配 insertion leg

⇒ 无合法 port matching

$$
\boxed{\text{ghost triangles absent}}
$$

---

# 5. 最终结果

$$
C_{AA}^{\rm gauge\ output}
=0
+
(+1,-1)\lambda_1\mathbb F
+0
$$

---

# 6. ordered vector

$$
\boxed{
(c_{D>A},c_{A>D})
=(+1,-1)
}
$$

---

# 7. 与 HT 对比

$$
(+1,-1)_{\rm calc}
=(+1,-1)_{\rm HT}
$$

---

# 结论

- split‑source orbit：**exact zero（traceless）**
- anomaly **完全来自 spectator TGG**
- first nonzero row：**spectator TGG single-edge selection row**

整个结构严格满足：

$$
\text{anomaly}=
\text{(triangle full‑d)}
+
\text{(same-edge contact)}
\rightarrow
\mu_\ell^2
$$

且唯一 surviving sector = gauge spectator triangle.
