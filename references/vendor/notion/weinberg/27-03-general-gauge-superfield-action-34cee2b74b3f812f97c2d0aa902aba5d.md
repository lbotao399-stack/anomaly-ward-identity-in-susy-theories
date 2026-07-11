Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d as of 2026-06-30T05:23:23.535Z:
<page url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.3 一般规范超场的规范不变作用量"}
</properties>
<content>
我们上一节对超对称阿贝尔规范理论的经验表明, 在一般的非阿贝尔规范理论中, 场 $`V _ { \mu } ^ { A } ( x )`$ ,$`\lambda ^ { A } ( x )`$ 和 $`D ^ { A } ( x )`$ 的动能拉格朗日量应该作为方程(27.2.6)的规范不变推广的一部分出现:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81b590ebdfbd4941313c">
		$$
		\mathcal L_{\mathrm{gauge}}=-\frac14 f_{\mu\nu}f^{\mu\nu}-\frac12(\bar\lambda\not\partial\lambda)+\frac12D^2.\tag{27.2.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c6869dcba3f32ad343">
	$$
	\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
	$$
</synced_block>
在这里结构常数写作 $`C_{ABC}`$；按照本文的 index convention，伴随场分量写作 $`V_\mu{}^A,\lambda^A,D^A`$，并用 Killing form 降指标后与 $`C_{ABC}`$ 或 $`t_A`$ 缩并。
另外, $`f^A{}_{\mu\nu}`$ 是规范协变的场强张量
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f813fa417eaaa9d93092a">
	$$
	f^A{}_{\mu\nu}
=\partial_\mu V_\nu{}^A-\partial_\nu V_\mu{}^A
+C^A{}_{BC}V_\mu{}^BV_\nu{}^C.\tag{27.3.2}
	$$
</synced_block>
$`D _ { \mu } \lambda`$ 是规范微子场的规范协变导数, 它在伴随表示下是
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c49cbdff2cb1912b6d">
	$$
	(D_\mu\lambda)^A=\partial_\mu\lambda^A+C^A{}_{BC}V_\mu{}^B\lambda^C.\tag{27.3.3}
	$$
</synced_block>
问题是: 方程(27.3.1)是否给出了一个超对称的作用量?
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c6869dcba3f32ad343">
		$$
		\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
		$$
	</synced_block_reference>
</callout>
由于拉格朗日密度(27.3.1)是明显规范不变的, 我们可以在任何方便的规范下检验这个作用量是否是超对称的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c6869dcba3f32ad343">
		$$
		\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
		$$
	</synced_block_reference>
</callout>
为了查明 $`\delta\mathcal L_{\mathrm{gauge}}`$ 是否在某个点 $`X^\mu`$ 是导数, 采取 Wess-Zumino 规范的一个特定版本, $`V^\mu{}^A(X)=0`$, 将是方便的.
那么在 $`X`$ 处, 分量场的变化由方程(26.2.15)—(26.2.17)取在 $`x =`$ $`X`$ 处给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f8137a000c40bda1b2e19">
	$$
	\begin{aligned}
\delta V_\mu{}^A&=(\bar\alpha\gamma_\mu\lambda^A),\\
\delta\lambda^A&=\left(\frac14 f^A{}_{\mu\nu}[\gamma^\nu,\gamma^\mu]+\mathrm i\gamma_5D^A\right)\alpha,\\
\delta D^A&=\mathrm i(\bar\alpha\gamma_5\not\partial\lambda^A).
\end{aligned}\tag{27.3.4-27.3.6}
	$$
</synced_block>
(我们必须在计算超对称变换下的变化之后, 而不是之前, 令这些表达式中的 $`x^\mu`$ 等于 $`X^\mu`$.) 另外, $`f^{A\mu\nu}`$ 中的非线性项关于 $`V`$ 是二次的, 因此它们在 $`x=X`$ 处的变分为零, 所以在 $`x=X`$ 处
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f8145903fc71ea4a5a113">
	$$
	\delta f^A{}_{\mu\nu}=(\bar\alpha(\gamma_\nu\partial_\mu-\gamma_\mu\partial_\nu)\lambda^A).\tag{27.3.7}
	$$
</synced_block>
除了一个例外, 方程(27.3.1)中的项和它们在超对称变换下的变换就是上节讨论的阿贝尔理论的数个副本(由 $`A`$ 标记), 因此给出了一个超对称的作用量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c6869dcba3f32ad343">
		$$
		\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
		$$
	</synced_block_reference>
</callout>
可能会扰乱这个作用量的超对称性的那个例外来源于规范微子的规范协变导数(27.3.3)的第二项:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c49cbdff2cb1912b6d">
		$$
		(D_\mu\lambda)^A=\partial_\mu\lambda^A+C^A{}_{BC}V_\mu{}^B\lambda^C.\tag{27.3.3}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81ffb31fd46bad78e4ee">
	$$
	\mathcal L_{\lambda\lambda V}=-\frac12 C_{ABC}(\bar\lambda^A V^B\lambda^C).\tag{27.3.8}
	$$
</synced_block>
它在 $`x = X`$ 处的变分是
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f8193967bd34abad3b11e">
	$$
	\delta\mathcal L_{\lambda\lambda V}
=-\frac12C_{ABC}(\bar\lambda^A(\delta V^B)\lambda^C)
=-\frac12C_{ABC}(\bar\lambda^A\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu\lambda^B).\tag{27.3.9}
	$$
</synced_block>
我们可以将右边双线性型的乘积写为两项的和
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f810ea5d0ce443bd7504e">
	$$
	(\bar\lambda^A\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu\lambda^B)=X^{ABC}+Y^{ABC}.\tag{27.3.10}
	$$
</synced_block>
其中
$$
\begin{aligned}
X^{ABC}&\equiv\frac14\Big[(\bar\lambda^A(1+\gamma_5)\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu(1+\gamma_5)\lambda^B)\\
&\qquad\qquad +(\bar\lambda^A(1-\gamma_5)\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu(1-\gamma_5)\lambda^B)\Big],\\
Y^{ABC}&\equiv\frac14\Big[(\bar\lambda^A(1+\gamma_5)\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu(1-\gamma_5)\lambda^B)\\
&\qquad\qquad +(\bar\lambda^A(1-\gamma_5)\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu(1+\gamma_5)\lambda^B)\Big].
\end{aligned}
$$
通过使用标准Fierz恒等式和旋量场的反对易子, 我们有
$$
\begin{aligned}
&(\bar\lambda^A(1\pm\gamma_5)\gamma_\mu\lambda^B)(\bar\alpha\gamma^\mu(1\pm\gamma_5)\lambda^C)
=(\bar\lambda^A(1\pm\gamma_5)\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu(1\pm\gamma_5)\lambda^B),\\
&(\bar\lambda^A(1\pm\gamma_5)\gamma_\mu\lambda^B)(\bar\alpha\gamma^\mu(1\mp\gamma_5)\lambda^C)
=(\bar\lambda^C(1\pm\gamma_5)\gamma_\mu\lambda^B)(\bar\alpha\gamma^\mu(1\mp\gamma_5)\lambda^A).
\end{aligned}
$$
(为了推导这些关系中的第一个, 我们注意到 $`[ ( 1 \pm \gamma _ { 5 } ) \gamma _ { \mu } ] _ { \alpha \gamma } [ ( 1 \pm \gamma _ { 5 } ) \gamma ^ { \mu } ] _ { \delta \beta }`$ 可以认为是一个依赖于 $`\delta`$ 和 $`\gamma`$ 的矩阵的矩阵元 $`\alpha \beta`$ , 因此可以展成 $`1 _ { \alpha \beta } , \gamma _ { \alpha \beta } ^ { \mu } , [ \gamma ^ { \mu } , \gamma ^ { \kappa } ] _ { \alpha \beta } , ( \gamma _ { 5 } \gamma ^ { \mu } ) _ { \alpha \beta }`$ 和 $`( \gamma _ { 5 } ) _ { \alpha \beta }`$ .
由于因子 $`( 1 \pm`$ $`\gamma _ { 5 } )`$ ), 展开中只有正比于 $`[ ( 1 \pm \gamma _ { 5 } ) \gamma ^ { \mu } ] _ { \alpha \beta }`$ 的项.
Lorentz不变性和以及另一个 $`1 \pm \gamma _ { 5 }`$ 因子的出现告诉我们这个展开采取如下的形式
$$
[ ( 1 \pm \gamma _ { 5 } ) \gamma _ { \mu } ] _ { \alpha \gamma } [ ( 1 \pm \gamma _ { 5 } ) \gamma ^ { \mu } ] _ { \delta \beta } = k [ ( 1 \pm \gamma _ { 5 } ) \gamma _ { \mu } ] _ { \alpha \beta } [ ( 1 \pm \gamma _ { 5 } ) \gamma ^ { \mu } ] _ { \delta \gamma } .
$$
为了确定比例常数 $`k`$ , 我们可以用 $`( \gamma _ { \nu } ) _ { \gamma \alpha }`$ 收缩两边, 并发现 $`k = - 1`$ .
这个负号被 $`\lambda^C`$ 和 $`\bar\alpha`$ 反对易产生的负号抵消了.
除了要使用 Majorana 双线性型的对称性质(26.A.7), 证明另一个 Fierz 恒等式的方法是相同的.) 因此 $`X^{ABC}`$ 关于 $`B`$ 和 $`C`$ 的交换是对称的, 而 $`Y^{ABC}`$ 关于 $`A`$ 和 $`B`$ 的交换是对称的. 由于 $`C_{ABC}`$ 是全反对称的, $`C_{ABC}X^{ABC}`$ 和 $`C_{ABC}Y^{ABC}`$ 对方程(27.3.9)没有贡献, 留给我们 $`\delta\mathcal L_{\lambda\lambda V}=0`$, 使得方程(27.3.1)给出的作用量是超对称的, 而这正是我们所要证明的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f8193967bd34abad3b11e">
		$$
		\delta\mathcal L_{\lambda\lambda V}
=-\frac12C_{ABC}(\bar\lambda^A(\delta V^B)\lambda^C)
=-\frac12C_{ABC}(\bar\lambda^A\gamma_\mu\lambda^C)(\bar\alpha\gamma^\mu\lambda^B).\tag{27.3.9}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c6869dcba3f32ad343">
		$$
		\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
		$$
	</synced_block_reference>
</callout>
通过找出那个拥有 $`f^A{}_{\mu\nu}`$, $`\lambda^A`$ 和 $`D^A`$ 作为分量场的超场, 我们可以理解为什么方程(27.3.1)给出了一个超对称作用量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c6869dcba3f32ad343">
		$$
		\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
		$$
	</synced_block_reference>
</callout>
回忆, 在一个推广的规范变换下, 矢量超场 $`V^A(x,\theta)`$ 有变换性质(27.1.12):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81d0a062f562ed48d849">
		$$
		\Gamma(x,\theta)\to \exp\bigl(-\mathrm{i}t_A\Omega^A(x,\theta)\bigr)\Gamma(x,\theta)\exp\bigl(+\mathrm{i}t_A\Omega^A(x,\theta)^*\bigr).\tag{27.1.12}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c1bc55ecca066630b9">
	$$
	\exp(-2t_AV^A(x,\theta))
\to\exp(-\mathrm i t_A\Omega^A(x,\theta))\exp(-2t_BV^B(x,\theta))\exp(+\mathrm i t_C\Omega^{C*}(x,\theta)).\tag{27.3.11}
	$$
</synced_block>
其中 $`\Omega^A(x,\theta)`$ 是一个一般的左手征超场.
因为 $`\Omega^{A*}\neq\Omega^A`$, 所以这不是一个规范协变的变换规则. 为了消除包含 $`\Omega^{A*}`$ 的因子, 我们注意到 $`\Omega^{A*}`$ 是右手征超场, 这使得 $`\mathcal D_{L\alpha}\Omega^{A*}=0`$, 因此
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81438406d033c24c0317">
	$$
	\begin{aligned}
&\exp(-2t_AV^A(x,\theta))\mathcal D_{L\alpha}\exp(+2t_BV^B(x,\theta))\\
&\to\exp(-\mathrm i t_A\Omega^A(x,\theta))\exp(-2t_BV^B(x,\theta))
\mathcal D_{L\alpha}\!
\left[\exp(+2t_CV^C(x,\theta))\exp(+\mathrm i t_D\Omega^{D*}(x,\theta))\right].
\end{aligned}\tag{27.3.12}
	$$
</synced_block>
因为左超导数 $`\mathcal D_{L\alpha}`$ 既作用在 $`\exp(+\mathrm i t_A\Omega^A(x,\theta))`$ 上又作用在 $`\exp(+2t_AV^A(x,\theta))`$ 上, 这仍然不是规范协变的.
如果我们沿用上一节讨论的阿贝尔理论的推导, 并定义旋量超场
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f819b9f7fd99a7d1742a0">
	$$
	2t_AW^A_{L\alpha}(x,\theta)
\equiv\epsilon^{\beta\gamma}\mathcal D_{R\beta}\mathcal D_{R\gamma}
\left[\exp(-2t_BV^B(x,\theta))\mathcal D_{L\alpha}\exp(+2t_CV^C(x,\theta))\right].\tag{27.3.13}
	$$
</synced_block>
这个因子可以被消掉.
因为任何三个 $`\mathcal D_R`$ 的乘积为零, $`W^A_{L\alpha}`$ 是左手征的
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f8146ab01f932503eb319">
	$$
	\mathcal{D} _ { R \beta } W _ { A L \alpha } ( x , \theta ) = 0 , \tag{27.3.14}
	$$
</synced_block>
又因为 $`\mathcal D_{R\beta}\mathcal D_{R\gamma}\mathcal D_{L\alpha}\Omega^A\propto\mathcal D_{R\delta}\Omega^A=0`$, 对于一个推广的规范变换
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f819c9a5bc2b79b7ca94a">
	$$
	t_AW^A_{L\alpha}(x,\theta)
\to\exp(-\mathrm i t_B\Omega^B(x,\theta))\,t_AW^A_{L\alpha}(x,\theta)\,\exp(+\mathrm i t_C\Omega^C(x,\theta)).\tag{27.3.15}
	$$
</synced_block>
所以 $`W^A_{L\alpha}`$ 在如上的意义下是规范协变的.
为了计算 $`x=X`$ 处的旋量场, 我们可以再次使用 Wess-Zumino 规范的 $`V^A(X)=0`$ 的版本, 在一个直接计算后, 我们发现在这个规范下
$$
W^A_L(x,\theta)=\lambda^A_L(X_+)+\frac12\gamma^\mu\gamma^\nu\theta_L\left(\partial_\mu V_\nu{}^A(X_+)-\partial_\nu V_\mu{}^A(X_+)\right)+(\theta_L^{\mathrm T}\epsilon\theta_L)\not\partial\lambda^A_R(X_+)-\mathrm i\theta_LD^A(X_+).
$$
由于 $`W^A_L`$ 是规范协变的, 在一个一般规范下, 它在一般的点上必须有值
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f813a8364fcffbd288c0c">
	$$
	W^A_L(x,\theta)=\lambda^A_L(x_+)+\frac12\gamma^\mu\gamma^\nu\theta_L f^A{}_{\mu\nu}(x_+)+(\theta_L^{\mathrm T}\epsilon\theta_L)\not D\lambda^A_R(x_+)-\mathrm i\theta_LD^A(x_+).\tag{27.3.16}
	$$
</synced_block>
由此, 我们可以用 $`W`$ 的双线性型构建一个 Lorentz不变且规范不变的 $`\mathcal{F}`$ -项
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f815a8faafaca24f0e9c5">
	$$
	\begin{aligned}
-[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}
&=-(\bar\lambda_A\not D(1-\gamma_5)\lambda^A)-\frac12 f^A{}_{\mu\nu}f_A{}^{\mu\nu}\\
&\quad+\frac{\mathrm i}{4}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}+D_AD^A.
\end{aligned}\tag{27.3.17}
	$$
</synced_block>
同上一节一样, 从这个 $`{ \mathcal F } .`$ -项的实部获得了规范不变拉格朗日量(27.3.1):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c6869dcba3f32ad343">
		$$
		\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f810da3cfc7a952a25037">
	$$
	-\frac12\operatorname{Re}[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}=\mathcal L_{\mathrm{gauge}}.\tag{27.3.18}
	$$
</synced_block>
虚部又怎么样呢? 它是
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81b2b32cf88be5a55346">
	$$
	-\operatorname{Im}[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}
=-\mathrm i(\bar\lambda_A\not D\gamma_5\lambda^A)+\frac14\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.\tag{27.3.19}
	$$
</synced_block>
方程(26.A.7)和结构常数的反对易性表明 $`(\bar\lambda_A\not D\gamma_5\lambda^A)=\frac12\partial_\mu(\bar\lambda_A\gamma^\mu\gamma_5\lambda^A)`$, 所以第一项是全导数, 而方程(23.5.4)告诉我们第二项也是全导数.
在阿贝尔规范理论中, 这意味着像(27.3.19)这样的项没有效应.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81b2b32cf88be5a55346">
		$$
		-\operatorname{Im}[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}
=-\mathrm i(\bar\lambda_A\not D\gamma_5\lambda^A)+\frac14\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.\tag{27.3.19}
		$$
	</synced_block_reference>
</callout>
而在非阿贝尔规范理论中, 就像在23.5节和23.6节中讨论的那样, 瞬子解得存在使得密度(27.3.19)对时空的积分可以不为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81b2b32cf88be5a55346">
		$$
		-\operatorname{Im}[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}
=-\mathrm i(\bar\lambda_A\not D\gamma_5\lambda^A)+\frac14\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.\tag{27.3.19}
		$$
	</synced_block_reference>
</callout>
因此, 我们必须考虑到拉格朗日密度可能有如下的新项
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81b0883af4382737b6a3">
	$$
	\mathcal L_\theta=-\frac{g^2\theta}{16\pi^2}\operatorname{Im}[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}.\tag{27.3.20}
	$$
</synced_block>
其中 $`\theta`$ 是一个新的实参量, $`g`$ 是规范耦合, 对于一个单规范群, 它可以方便地定义成: 如果 $`t_A,t_B`$ 和 $`t_C`$ 处在计算瞬子效应所使用的规范代数的“标准” $`SU(2)`$ 子代数中, 我们就有 $`C_{ABC}=g\epsilon_{ABC}`$.
在规范耦合的这个定义下, 方程(23.5.20)对于单规范群给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81309d9fd20d91ea42d2">
	$$
	\int \mathrm d^4x\,\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}=64\pi^2\nu/g^2.\tag{27.3.21}
	$$
</synced_block>
其中 $`\nu = 0 , \pm 1 , \pm 2 , \cdots`$ 是整数, 即缠绕数, 它表征了规范场构形的拓扑类.
因此对于缠绕数为 $`\nu`$ 的瞬子, 拉格朗日密度 $`\mathcal{L} _ { \theta }`$ 对路径积分贡献一个相位,
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81d89e8ac5628649bc16">
	$$
	\left[ \exp \Bigl ( \mathrm{i} \int \mathrm { d } ^ { 4 } x \mathcal{L} _ { \theta } \Bigr ) \right] _ { \nu } = \exp ( \mathrm{i} \nu \theta ) , \tag{27.3.22}
	$$
</synced_block>
所以 $`\mathcal{L} _ { \theta }`$ 关于 $`\theta`$ 是周期的, 周期为 $`2 \pi`$ .
规范场吸收进一个 $`g`$ 因子通常会比较方便, 这使得结构常数不依赖于 $`g`$ , 而规范场的拉格朗日密度则要乘以一个总因子 $`1 / g ^ { 2 }`$ .
在这个约定下, 规范场的完整拉格朗日密度可以用重新标度过的规范场和耦合常数表示成
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c890f7cc98ab5b5046">
	$$
	\mathcal L_{\mathrm{gauge}}+\mathcal L_\theta=-\operatorname{Re}\left[\frac{\tau}{8\pi\mathrm i}W_{AL}^{\mathrm T}\epsilon W_L^A\right]_{\mathcal F}.\tag{27.3.23}
	$$
</synced_block>
其中 $`\tau`$ 是复耦合常数
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81c3aa6efcd2d7e8c4b5">
	$$
	\tau \equiv \frac { 4 \pi \mathrm{i} } { g ^ { 2 } } + \frac { \theta } { 2 \pi } . \tag{27.3.24}
	$$
</synced_block>
根据方程(23.5.19), 缠绕数为 $`\nu`$ 的瞬子对路径积分的贡献被因子 $`\exp ( - 8 \pi ^ { 2 } | \nu | / g ^ { 2 } )`$ 压低了, 它与因子(27.3.22)合在一起产生了总因子
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f81d89e8ac5628649bc16">
		$$
		\left[ \exp \Bigl ( \mathrm{i} \int \mathrm { d } ^ { 4 } x \mathcal{L} _ { \theta } \Bigr ) \right] _ { \nu } = \exp ( \mathrm{i} \nu \theta ) , \tag{27.3.22}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d#34cee2b74b3f8144991ac35a3da82a65">
	$$
	\exp \left[ \mathrm{i} \nu \theta - \frac { 8 \pi ^ { 2 } | \nu | } { g ^ { 2 } } \right] = \left\{ \begin{array} { l l } { { \exp ( 2 \pi \mathrm{i} \nu \tau ) } } & { { \qquad \nu \geq 0 } } \\ { { \exp ( 2 \pi \mathrm{i} \nu \tau ^ { * } ) } } & { { \qquad \nu \leq 0 } } \end{array} . \right. \tag{27.3.25}
	$$
</synced_block>
</content>
</page>
