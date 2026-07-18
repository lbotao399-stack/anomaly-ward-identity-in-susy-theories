Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd as of 2026-07-17T18:15:43.593Z:
<page url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.5 树级重求和中的超对称破缺"}
</properties>
<content>
我们在上一节看到, 如果 Fayet-Iliopoulos 常数 $`\xi^A`$ 全为零并且方程 $`\partial f(\phi)/\partial\phi^n=0`$ 存在一组解, 那么这些方程也会有规范超场的 $`D`$-分量全为零的解, 进而使得超对称是没有破缺的.
由此得出, 在规范超场和手征超场的可重整理论中, 超对称性在树级近似下能够自发破缺只有两种(互不排斥的)方式: **超势 **$`f(\phi)`$** 可以被取成使得所有方程 **$`\partial f(\phi)/\partial\phi^n=0`$** 没有解, 或者, 对于有 **$`U(1)`$** 因子的规范群, 作用量中含有 Fayet-Iliopoulos 项**.
我们在 26.5 节已经看到 $`\phi`$ 的任何值都不会使 $`\partial f(\phi)/\partial\phi^n=0`$ 是如何发生的.
当手征超场与规范超场相互作用时, 那个讨论也不需要做出任何改变, 所以我们转向另一可能性: Fayet-Iliopoulos项产生的超对称性自发破缺.
由于这只对有 $`U ( 1 )`$ 因子的规范群才会发生, 最简单的情况是只有一个 $`U ( 1 )`$ 规范群的理论.
**正如在 22.4 节讨论过的, 为了避免 **$`U ( 1 ) - U ( 1 ) - U ( 1 )`$** 反常和 **$`U ( 1 )`$** -引力-引力反常, 所有左手征超场的 **$`U ( 1 )`$** 量子数之和以及它们的立方和必须为零.**
我们将考虑最简单的可能性: 两个左手征超场 $`\Phi _ { \pm }`$ , 带有 $`U ( 1 )`$ 量子数 $`\pm e`$ .
(这是量子电动力学的超对称版, 两个超场的旋量分量 $`\psi _ { - L }`$ 和 $`\psi _ { + L }`$ 提供了电子场及其电荷共轭场的左手部分.) 
在一个可重整理论中, 最一般的 $`U ( 1 )`$ -不变超势就是 $`f ( \Phi ) = m \Phi _ { + } \Phi _ { - }`$ .
那么标量势(27.4.9)对于这些超场的标量分量 $`\phi _ { \pm }`$ 是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f814d862dec14dffeb88d">
		$$
									V(\phi)=\frac{\partial f^*(\phi^*)}{\partial\phi_n^*}\frac{\partial f(\phi)}{\partial\phi^n}
+\frac12(\xi_A+\phi_n^*(t_A)^n{}_m\phi^m)(\xi^A+\phi_l^*(t^A)^l{}_k\phi^k).\tag{27.4.9}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81188a9de335ca6c9530">
	$$
	V ( \phi _ { + } , \phi _ { - } ) = m ^ { 2 } | \phi _ { + } | ^ { 2 } + m ^ { 2 } | \phi _ { - } | ^ { 2 } + \left( \xi + e ^ { 2 } | \phi _ { + } | ^ { 2 } - e ^ { 2 } | \phi _ { - } | ^ { 2 } \right) ^ { 2 } . \tag{27.5.1}
	$$
</synced_block>
除非 Fayet-Iliopoulos 常数 $`\xi`$ 为零, 否则明显不可能找到 $`V = 0`$ 的超对称真空.
当 $`\xi > m ^ { 2 } / 2 e ^ { 2 }`$ 或$`\xi ~ < ~ - m ^ { 2 } / 2 e ^ { 2 }`$ 时, 势(27.5.1)在 $`\phi _ { + } ~ = ~ 0`$ 和 $`| \phi _ { - } | ^ { 2 } = ( 2 e ^ { 2 } \xi - m ^ { 2 } ) / 2 e ^ { 4 }`$ 或者在 $`\phi _ { - } ~ = ~ 0`$ 和 $`| \phi _ { + } | ^ { 2 } =`$ $`( - 2 e ^ { 2 } \xi - m ^ { 2 } ) / 2 e ^ { 4 }`$ 处有最小值, 这使得 $`U ( 1 )`$ 对称性是伴随超对称性破缺的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81188a9de335ca6c9530">
		$$
		V ( \phi _ { + } , \phi _ { - } ) = m ^ { 2 } | \phi _ { + } | ^ { 2 } + m ^ { 2 } | \phi _ { - } | ^ { 2 } + \left( \xi + e ^ { 2 } | \phi _ { + } | ^ { 2 } - e ^ { 2 } | \phi _ { - } | ^ { 2 } \right) ^ { 2 } . \tag{27.5.1}
		$$
	</synced_block_reference>
</callout>
当 $`| \xi | < m ^ { 2 } / 2 e ^ { 2 }`$ 时, 势能的最小值处在 $`\phi _ { + } = \phi _ { - } = 0`$ , 所以这里的规范对称性没有破缺.
超对称性可能的破缺与规范对称性可能的破缺之间一般没有必然的联系.
无论超对称性是通过这里讨论的 Fayet-Iliopoulos 机制亦或是 26.5 节的 O’Raifeartaigh 机制亦或是二者的结合体自发破缺, 超对称都在树级近似质量中留有余影.
对于规范超场和手征超场的一般可重整超对称理论, 对它们的拉格朗日量(27.4.8)的观察表明, 这个理论中的超对称自发破缺对27.4节计算的质量产生了相应的修正.
## 自旋 0 质量
如果 $`\mathcal F`$-项 $`\mathcal F^n=-(\partial f(\phi)/\partial\phi^n)^*`$ 在势能的最小值点 $`\phi_0`$ 处不为零, 那么除了方程(27.4.15)中列出的那些项, 势能中 $`\varphi^n\equiv\phi^n-\phi_0^n`$ 的二阶项有额外的项:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8118bc22c29b60a609f7">
		$$
							\begin{aligned}
V_{\mathrm{quad}}(\phi)
&=\varphi_n^*(\mathcal M^\dagger\mathcal M)^n{}_m\varphi^m
+\varphi_n^*(t_A\phi_0)^n(t^A\phi_0)_m^*\varphi^m\\
&\quad+\frac12(t_A\phi_0)_n^*(t^A\phi_0)_m^*\varphi^n\varphi^m
+\frac12\varphi_n^*\varphi_m^*(t_A\phi_0)^n(t^A\phi_0)^m.
\end{aligned}\tag{27.4.15}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
V_{\mathrm{quad}}
&=\varphi_n^*(\mathcal M^*\mathcal M)^n{}_m\varphi^m
+(t_A\phi_0)^n\varphi_n^*(t^A\phi_0)_m^*\varphi^m\\
&\quad+\frac12(t_A\phi_0)_n^*\varphi^n(t^A\phi_0)_m^*\varphi^m
+\frac12(t_A\phi_0)^n\varphi_n^*(t^A\phi_0)^m\varphi_m^*\\
&\quad+\frac12\mathcal N_{nm}\varphi^n\varphi^m+\frac12\mathcal N^{nm*}\varphi_n^*\varphi_m^*
+D^A_0(t_A)^n{}_m\varphi_n^*\varphi^m.
\end{aligned}\tag{27.5.2}
$$
其中 $`\mathcal{M}`$ 依旧是复对称矩阵(26.4.11):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#d8787cc4ba7f4998840cbb124f54bfb8">
		$$
		\mathcal{M} _ { n m } \equiv \left. f _ { n m } ( \phi ) \right| _ { \phi = \phi _ { 0 } } . \tag{26.4.11}
		$$
	</synced_block_reference>
</callout>
$$
\mathcal M_{nm}\equiv\left(\frac{\partial^2f(\phi)}{\partial\phi^n\partial\phi^m}\right)_{\phi=\phi_0},
$$
$`\mathcal{N} _ { n m }`$ 是新元素
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8103abbadc44c2b1e43f">
	$$
	\mathcal N_{nm}\equiv-\mathcal F_0^\ell\left(\frac{\partial^3f(\phi)}{\partial\phi^n\partial\phi^m\partial\phi^\ell}\right)_{\phi=\phi_0}.\tag{27.5.3}
	$$
</synced_block>
而 $`\mathcal F_0`$ 和 $`D^A_0`$ 依旧是手征标量超场和规范超场在势能最小值点处的 $`\mathcal F`$-项和 $`D`$-项:
$$
\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0},\qquad D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m.
$$
如果我们势能的二次部分(27.5.2)写成(27.4.16)的形式:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81cd896fd61c1fdf5521">
		$$
							V_{\mathrm{quad}}=\frac12
\begin{bmatrix}\varphi\\ \varphi^*\end{bmatrix}^{\dagger}
M_0^2
\begin{bmatrix}\varphi\\ \varphi^*\end{bmatrix}.\tag{27.4.16}
		$$
	</synced_block_reference>
</callout>
那么取代方程(27.4.17), 我们现在有标量质量矩阵
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81839e90cb371e3a20e7">
		$$
										M_0^2=\begin{bmatrix}
\mathcal M^*\mathcal M+(t_A\phi_0)(t^A\phi_0)^\dagger & (t_A\phi_0)(t^A\phi_0)^{\mathrm T}\\
(t_A\phi_0)^*(t^A\phi_0)^\dagger & \mathcal M^*\mathcal M+(t_A\phi_0)^*(t^A\phi_0)^{\mathrm T}
\end{bmatrix}.\tag{27.4.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f811d8b8ef88ae6f20082">
	$$
			M_0^2=\begin{bmatrix}
\mathcal M^*\mathcal M+\mathcal A+D^A_0t_A & \mathcal B+\mathcal N^*\\
\mathcal B^*+\mathcal N & \mathcal M\mathcal M^*+\mathcal A^*+D^A_0t_A^{\mathrm T}
\end{bmatrix}.\tag{27.5.4}
	$$
</synced_block>
其中
$$
\mathcal{A} \equiv ( t _ { A } \phi _ { 0 } ) ( t ^ { A } \phi _ { 0 } ) ^ { \dagger } , \qquad \mathcal{B} \equiv ( t _ { A } \phi _ { 0 } ) ( t ^ { A } \phi _ { 0 } ) ^ { \mathrm { T } } .
$$
# 自旋 $`1 / 2`$ 质量
费米子质量矩阵 $`M`$ 在这里依旧由方程(27.4.30)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f819abf34cad914d5b3ef">
		$$
		M_{nm}=\mathcal M_{nm},\qquad M_{nA}=M_{An}=\mathrm i\sqrt2\,((t_A\phi_0)_n)^*,\qquad M_{AB}=0.\tag{27.4.30}
		$$
	</synced_block_reference>
</callout>
$$
M _ { n m } = \mathcal{M} _ { n m } , M _ { n A } = M _ { A n } = \mathrm{i} \sqrt { 2 } ( t _ { A } \phi _ { 0 } ) _ { n } ^ { * } , M _ { A B } = 0 .
$$
然而, 取代方程(27.4.19), 规范不变性条件(27.4.18)现在给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81a1b998c5255c573d32">
		$$
		\mathcal M_{nm}(t_A\phi_0)^m=0.\tag{27.4.19}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8193bf58e495760c424a">
		$$
										\frac{\partial^2 f(\phi)}{\partial\phi^n\partial\phi^m}(t_A\phi)^m
+\frac{\partial f(\phi)}{\partial\phi^m}(t_A)^m{}_n=0.\tag{27.4.18}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8108a803ef4ab3c5c62e">
	$$
	\mathcal M_{nm}(t_A\phi_0)^m=\mathcal F^m_0(t_A)_{mn}.\tag{27.5.5}
	$$
</synced_block>
因此本征值是费米子质量平方的厄米正定矩阵是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81e39cf9c6f33b215fc1">
	$$
	\begin{array} { l } { { ( M ^ { \dagger } M ) _ { n } {} ^ { m } = ( { \mathcal M } ^ { \dagger } { \mathcal M } ) _ { n } {} ^ { m } + 2 ( t _ { A } \phi _ { 0 } ) _ { n } ( t ^ { A } \phi _ { 0 } ) ^ { m * } , } } \\ { { \displaystyle ( M ^ { \dagger } M ) _ { A B } = 2 ( \phi _ { 0 } ^ { \dagger } t _ { B } t _ { A } \phi _ { 0 } ) , } } \\ { { \displaystyle ( M ^ { \dagger } M ) _ { A } {} ^ { n } = \left[ ( M ^ { \dagger } M ) ^ { n } {} _ { A } \right] ^ { * } = \mathrm{i} \sqrt { 2 } { \mathcal F } _ { m 0 } ( t _ { A } ) ^ { m } {} _ { n } . } } \end{array} \tag{27.5.6}
	$$
</synced_block>
# 自旋1质量
矢量玻色子的质量平方依旧由矩阵(27.4.36)的本征值给出:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8186a425e368c38de064">
		$$
		(\mu^2)_{AB}=\phi_0^\dagger\{t_B,t_A\}\phi_0.\tag{27.4.36}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81f9baa7f80f122366bb">
	$$
	( \mu ^ { 2 } ) _ { A B } = \left( \phi _ { 0 } ^ { \dagger } \{ t _ { B } , t _ { A } \} \phi _ { 0 } \right) . \tag{27.5.7}
	$$
</synced_block>
除了方程(27.5.4)中的 $`D`$ -项有一个例外外,质量平方矩阵的变化都在它们的非对角元部分.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f811d8b8ef88ae6f20082">
		$$
				M_0^2=\begin{bmatrix}
\mathcal M^*\mathcal M+\mathcal A+D^A_0t_A & \mathcal B+\mathcal N^*\\
\mathcal B^*+\mathcal N & \mathcal M\mathcal M^*+\mathcal A^*+D^A_0t_A^{\mathrm T}
\end{bmatrix}.\tag{27.5.4}
		$$
	</synced_block_reference>
</callout>
因此, 方程(27.5.4), (27.5.6) 和 (27.5.7) 对这些矩阵的迹给出了特别简单的结果: 对于自旋 0
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f811d8b8ef88ae6f20082">
		$$
				M_0^2=\begin{bmatrix}
\mathcal M^*\mathcal M+\mathcal A+D^A_0t_A & \mathcal B+\mathcal N^*\\
\mathcal B^*+\mathcal N & \mathcal M\mathcal M^*+\mathcal A^*+D^A_0t_A^{\mathrm T}
\end{bmatrix}.\tag{27.5.4}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81e39cf9c6f33b215fc1">
		$$
		\begin{array} { l } { { ( M ^ { \dagger } M ) _ { n } {} ^ { m } = ( { \mathcal M } ^ { \dagger } { \mathcal M } ) _ { n } {} ^ { m } + 2 ( t _ { A } \phi _ { 0 } ) _ { n } ( t ^ { A } \phi _ { 0 } ) ^ { m * } , } } \\ { { \displaystyle ( M ^ { \dagger } M ) _ { A B } = 2 ( \phi _ { 0 } ^ { \dagger } t _ { B } t _ { A } \phi _ { 0 } ) , } } \\ { { \displaystyle ( M ^ { \dagger } M ) _ { A } {} ^ { n } = \left[ ( M ^ { \dagger } M ) ^ { n } {} _ { A } \right] ^ { * } = \mathrm{i} \sqrt { 2 } { \mathcal F } _ { m 0 } ( t _ { A } ) ^ { m } {} _ { n } . } } \end{array} \tag{27.5.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81f9baa7f80f122366bb">
		$$
		( \mu ^ { 2 } ) _ { A B } = \left( \phi _ { 0 } ^ { \dagger } \{ t _ { B } , t _ { A } \} \phi _ { 0 } \right) . \tag{27.5.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f812aafc5fa0a98220066">
	$$
	\operatorname{Tr} M _ { 0 } ^ { 2 } = 2 \operatorname{Tr} ( \mathcal{M} ^ { * } \mathcal{M} ) + \operatorname{Tr} \mu ^ { 2 } + 2 D _ { A 0 } \operatorname{Tr} t ^ { A } \tag{27.5.8}
	$$
</synced_block>
以及对于自旋 $`1 / 2`$
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81bf96d9ecbc31e6da78">
	$$
	\operatorname{Tr} ( M ^ { \dagger } M ) = \operatorname{Tr} ( \mathcal{M} ^ { * } \mathcal{M} ) + 2 \operatorname{Tr} \mu ^ { 2 } . \tag{27.5.9}
	$$
</synced_block>
<span color="yellow_bg">由于迹是本征值的和, 我们从此获得了一个质量求和规则:</span>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81ac8686e30cdc914fd8">
	$$
		\sum_{\mathrm{spin}\,0}m^2-2\sum_{\mathrm{spin}\,1/2}m^2+3\sum_{\mathrm{spin}\,1}m^2
=-2\sum_A D_{A0}\operatorname{Tr}t^A.\tag{27.5.10}
	$$
</synced_block>
除非 $`t _ { A }`$ 是 $`U ( 1 )`$ 生成元, 否则 $`t _ { A }`$ 的迹自动为零, 并且, 正如22.4节所提及的, 为了避免引力贡献一个会破坏 $`U ( 1 )`$ 流守恒的反常, $`U ( 1 )`$ 规范生成元的迹(当取遍所有左手费米子时)也必须为零.
因此(27.5.10)给出了更简单的结果\[4\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- S. Ferrara, L. Girardello, and F. Palumbo, Phys. Rev. D20, 403 (1979). 这篇文章重印于 Supersymmetry, 参考文献\[1\]. P. Fayet 给出了这个求和规则的特殊情况, Phys. Lett. 84B,416 (1979)
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8152b42ce99cadb07d86">
	$$
	\sum_{\mathrm{spin}\,0}m^2-2\sum_{\mathrm{spin}\,1/2}m^2+3\sum_{\mathrm{spin}\,1}m^2=0.\tag{27.5.11}
	$$
</synced_block>
当然, 电荷, 色荷, 重子数和轻子数守恒没有被破坏使得质量矩阵没有矩阵元来连接这些量子数取不同值的粒子, 所以所有这些结果对每组守恒的量子数分别成立.
<span color="yellow_bg">在标准模型的最小超对称扩张中, 求和规则(27.5.11)通常为超对称在树级近似下自发破缺的模型提供了反对的证据.</span>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8152b42ce99cadb07d86">
		$$
		\sum_{\mathrm{spin}\,0}m^2-2\sum_{\mathrm{spin}\,1/2}m^2+3\sum_{\mathrm{spin}\,1}m^2=0.\tag{27.5.11}
		$$
	</synced_block_reference>
</callout>
我们会在28.3节连同其它讨论来讨论这点.
<empty-block/>
正如已经在26.5节观察到的(将在29.1节和29.2节进行更普遍的而讨论), 超对称形的自发破缺必然要求存**在无质量费米子, 戈德斯通微子.**
对于树级近似下的可重整理论, 戈德斯通微子场 $`g`$ 出现在手征超场和规范超场的旋量分量 $`\psi^n`$ 和 $`\lambda^A`$ 中, 系数是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f816fb6c5fb4e0e527eb6">
	$$
	\psi _ { n L } = \mathrm{i} \sqrt { 2 } \mathcal{F} _ { n 0 } g _ { L } + \cdots \ , \qquad \lambda _ { A L } = D _ { A 0 } g _ { L } + \cdots \ , \tag{27.5.12}
	$$
</synced_block>
其中省略号代表与质量明确非零的旋量场相关的项.
为了验证这点, 我们必须证明 $`(\mathrm i\sqrt2\mathcal F^n_0,D^A_0)`$ 是费米子质量平方矩阵 $`M^\dagger M`$ 本征值为零的本征矢量.
为此, 我们将需要使用势(27.4.9)在 $`\phi=\phi_0`$ 处稳定这一条件:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f814d862dec14dffeb88d">
		$$
									V(\phi)=\frac{\partial f^*(\phi^*)}{\partial\phi_n^*}\frac{\partial f(\phi)}{\partial\phi^n}
+\frac12(\xi_A+\phi_n^*(t_A)^n{}_m\phi^m)(\xi^A+\phi_l^*(t^A)^l{}_k\phi^k).\tag{27.4.9}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f818ca795f2298857b31a">
	$$
	0 = \left. \frac { \partial V } { \partial \phi _ { n } } \right| _ { \phi = \phi _ { 0 } } = - \mathcal{M} _ { n } {} ^ { m } \mathcal{F} _ { m 0 } + D _ { A 0 } ( \phi _ { 0 } ^ { \dagger } t ^ { A } ) _ { n } . \tag{27.5.13}
	$$
</synced_block>
我们同时需要规范不变性条件(27.4.12), 它在 $`\phi = \phi _ { 0 }`$ 处是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8127a95bcf4984121d7a">
		$$
		\frac{\partial f(\phi)}{\partial\phi^m}(t_A)^m{}_n\phi^n=0.\tag{27.4.12}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f811b8b96d9f5b84c4d83">
	$$
	\mathcal{F} ^ { n } {} _ { 0 } \left( t _ { A } \phi _ { 0 } \right) _ { n } = 0 . \tag{27.5.14}
	$$
</synced_block>
这样, 结合方程(27.5.13)和(27.5.14)与方程(27.5.5)和(27.5.6)就给出了
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f818ca795f2298857b31a">
		$$
		0 = \left. \frac { \partial V } { \partial \phi _ { n } } \right| _ { \phi = \phi _ { 0 } } = - \mathcal{M} _ { n } {} ^ { m } \mathcal{F} _ { m 0 } + D _ { A 0 } ( \phi _ { 0 } ^ { \dagger } t ^ { A } ) _ { n } . \tag{27.5.13}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f811b8b96d9f5b84c4d83">
		$$
		\mathcal{F} ^ { n } {} _ { 0 } \left( t _ { A } \phi _ { 0 } \right) _ { n } = 0 . \tag{27.5.14}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f8108a803ef4ab3c5c62e">
		$$
		\mathcal M_{nm}(t_A\phi_0)^m=\mathcal F^m_0(t_A)_{mn}.\tag{27.5.5}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81e39cf9c6f33b215fc1">
		$$
		\begin{array} { l } { { ( M ^ { \dagger } M ) _ { n } {} ^ { m } = ( { \mathcal M } ^ { \dagger } { \mathcal M } ) _ { n } {} ^ { m } + 2 ( t _ { A } \phi _ { 0 } ) _ { n } ( t ^ { A } \phi _ { 0 } ) ^ { m * } , } } \\ { { \displaystyle ( M ^ { \dagger } M ) _ { A B } = 2 ( \phi _ { 0 } ^ { \dagger } t _ { B } t _ { A } \phi _ { 0 } ) , } } \\ { { \displaystyle ( M ^ { \dagger } M ) _ { A } {} ^ { n } = \left[ ( M ^ { \dagger } M ) ^ { n } {} _ { A } \right] ^ { * } = \mathrm{i} \sqrt { 2 } { \mathcal F } _ { m 0 } ( t _ { A } ) ^ { m } {} _ { n } . } } \end{array} \tag{27.5.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81959e37cec5e36d340a">
	$$
	\mathrm{i} \sqrt { 2 } ( M ^ { \dagger } M ) _ { n } {} ^ { m } { \mathcal F } _ { m 0 } = \mathrm{i} \sqrt { 2 } D _ { A } ( t ^ { A } { \mathcal F } _ { 0 } ^ { * } ) _ { n } = - ( M ^ { \dagger } M ) _ { n } {} ^ { A } D _ { A 0 } \tag{27.5.15}
	$$
</synced_block>
和
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f81b0bad4e26a9d953e68">
	$$
	\mathrm{i} \sqrt { 2 } ( M ^ { \dagger } M ) _ { A } {} ^ { m } \mathcal{F} _ { m 0 } = - 2 \mathcal{F} _ { n 0 } \left( t _ { A } \right) ^ { n } {} _ { m } \mathcal{F} ^ { m } {} _ { 0 } = - ( M ^ { \dagger } M ) _ { A } {} ^ { B } D _ { B 0 } . \tag{27.5.16}
	$$
</synced_block>
即,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81539884dcb60a7200cd#34cee2b74b3f815987f2dea8572ac7a1">
	$$
	M ^ { \dagger } M \left( \begin{array} { c } { { \mathrm{i} \sqrt { 2 } \mathcal{F} _ { 0 } } } \\ { { D _ { 0 } } } \end{array} \right) = 0 , \tag{27.5.17}
	$$
</synced_block>
而这正是所要证明的.
<empty-block/>
</content>
</page>
