Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489 as of 2026-06-30T07:31:17.106Z:
<page url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f81239f12c44eda7b664f" title="第 30 章 超图"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"30.1 势超场"}
</properties>
<content>
考虑左手征超场 $`\Phi _ { n } ( x , \theta )`$ 及其复共轭的理论, 但简单起见没有规范超场.
所有分量场编时乘积的真空期望值可以从这些超场编时乘积的真空期望值计算出来.
我们可以尝试用路径积分
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f81649da4d2a10ec7cfbb">
	$$
	\begin{aligned}
\big\langle T\{\Phi^{n_1}(x_1,\theta_1),\Phi^{n_2}(x_2,\theta_2),\cdots\}\big\rangle
={}&\int\left[\prod_{n,x,\theta}d\Phi^n(x,\theta)\right]\exp\{iI[\Phi]\}\\
&\times\Phi^{n_1}(x_1,\theta_1)\Phi^{n_2}(x_2,\theta_2)\cdots .
\tag{30.1.1}
\end{aligned}
	$$
</synced_block>
来计算它们, 其中 $`I [ \Phi ]`$ 是作用量
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f8157be45d87a0a6cae5c">
	$$
	I[\Phi]=\frac12\int d^4x\left[\Phi^*_n(x,\theta)\Phi^n(x,\theta)\right]_D+2\operatorname{Re}\int d^4x\left[f(\Phi)\right]_{\mathcal F}.\tag{30.1.2}
	$$
</synced_block>
(同方程(26.4.3)中一样, 在第一项中引入因子 $`1 / 2`$ 是为了使 $`\Phi`$ 的分量场是按惯例归一化的.) 但我们不能简单地从方程(30.1.1)中读出Feynman规则, 这是因为对超场 $`\Phi _ { n }`$ 的泛函积分要被约束以满足左手征条件 $`\mathcal{D} _ { R } \boldsymbol { \Phi } _ { n } = 0`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f81649da4d2a10ec7cfbb">
		$$
		\begin{aligned}
\big\langle T\{\Phi^{n_1}(x_1,\theta_1),\Phi^{n_2}(x_2,\theta_2),\cdots\}\big\rangle
={}&\int\left[\prod_{n,x,\theta}d\Phi^n(x,\theta)\right]\exp\{iI[\Phi]\}\\
&\times\Phi^{n_1}(x_1,\theta_1)\Phi^{n_2}(x_2,\theta_2)\cdots .
\tag{30.1.1}
\end{aligned}
		$$
	</synced_block_reference>
</callout>
这类似于电动力学中的问题.
正如在12.3节中所讨论的, 当能量低于电子质量时, 软光子之间的相互作用可以被如下的有效拉格朗日量描述:
$$
I [ f ] = - \frac { 1 } { 4 } \int \mathrm { d } ^ { 4 } x \left[ f _ { \mu \nu } f ^ { \mu \nu } + c _ { 1 } \biggl ( f _ { \mu \nu } f ^ { \mu \nu } \biggr ) ^ { 2 } + c _ { 2 } \biggl ( \epsilon _ { \mu \nu \rho \sigma } f ^ { \mu \nu } f ^ { \rho \sigma } \biggr ) ^ { 2 } \right] .
$$
但是, 如果不考虑路径积分被齐次 Maxwell 方程
$$
\partial _ { \mu } f _ { \nu \rho } + \partial _ { \nu } f _ { \rho \mu } + \partial _ { \rho } f _ { \mu \nu } = 0
$$
所约束这个事实, 我们无法从这个作用量中读出 Feynman 规则.
众所周知, 我们处理这个约束的方式是引入一个 4 -矢势 $`A _ { \mu }`$ , 满足 $`f _ { \mu \nu } = \partial _ { \mu } A _ { \nu } - \partial _ { \nu } A _ { \mu }`$ , 这使得这个约束自动满足, 然后对 $`A _ { \mu } ( x )`$ 积分而非 $`f _ { \mu \nu } ( x )`$ .
以相同的方法, 我们可以采用在26.6节就用来推导超场场方程的那个技巧, 并引入非手征实超场 $`S _ { n } ( x , \theta )`$ , 满足
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f8145bca1efe4bfbd6179">
	$$
	\Phi^n=\mathcal D_R^2S^n.\tag{30.1.3}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f8132823dfcf4db585653">
	$$
	\mathcal{D} _ { R } ^ { 2 } \equiv \epsilon ^ { \alpha \beta } \mathcal{D} _ { R \alpha } \mathcal{D} _ { R \beta } , \tag{30.1.4}
	$$
</synced_block>
这使得 $`\Phi _ { n }`$ 自动满足左手征约束, $`\mathcal{D} _ { R \alpha } \Phi _ { n } = 0`$ .
取代方程(30.1.1), 我们有路径积分公式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f81649da4d2a10ec7cfbb">
		$$
		\begin{aligned}
\big\langle T\{\Phi^{n_1}(x_1,\theta_1),\Phi^{n_2}(x_2,\theta_2),\cdots\}\big\rangle
={}&\int\left[\prod_{n,x,\theta}d\Phi^n(x,\theta)\right]\exp\{iI[\Phi]\}\\
&\times\Phi^{n_1}(x_1,\theta_1)\Phi^{n_2}(x_2,\theta_2)\cdots .
\tag{30.1.1}
\end{aligned}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f816fad3ad660c1431160">
	$$
	\begin{aligned}
T\{\Phi^{n_1}(x_1,\theta_1),\Phi^{n_2}(x_2,\theta_2),\cdots\}
={}&\int\left[\prod_{n,x,\theta}dS^n(x,\theta)\right]\exp\{iI[\mathcal D_R^2S]\}\\
&\times\mathcal D_R^2S^{n_1}(x_1,\theta_1)\mathcal D_R^2S^{n_2}(x_2,\theta_2)\cdots .
\tag{30.1.5}
\end{aligned}
	$$
</synced_block>
当用 $`S _ { n }`$ 表示作用量(30.1.2)后, 我们回忆起超导数的 $`D`$ -项对作用量没有贡献, 所以我们可以将方程(30.1.2)第一项中作用在 $`S _ { n } ^ { * }`$ 上的算符 $`( \mathcal{D} _ { R } ^ { 2 } ) ^ { * } = \mathcal{D} _ { L } ^ { 2 }`$ 移到 $`S _ { n }`$ 上, 这给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f8157be45d87a0a6cae5c">
		$$
		I[\Phi]=\frac12\int d^4x\left[\Phi^*_n(x,\theta)\Phi^n(x,\theta)\right]_D+2\operatorname{Re}\int d^4x\left[f(\Phi)\right]_{\mathcal F}.\tag{30.1.2}
		$$
	</synced_block_reference>
</callout>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f8157be45d87a0a6cae5c">
		$$
		I[\Phi]=\frac12\int d^4x\left[\Phi^*_n(x,\theta)\Phi^n(x,\theta)\right]_D+2\operatorname{Re}\int d^4x\left[f(\Phi)\right]_{\mathcal F}.\tag{30.1.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f81f39414f74f72c0603e">
	$$
	I[\mathcal D_R^2S]=\frac12\int d^4x\left[S^*_n\mathcal D_L^2\mathcal D_R^2S^n\right]_D+2\operatorname{Re}\int d^4x\left[f(\mathcal D_R^2S)\right]_{\mathcal F}.\tag{30.1.6}
	$$
</synced_block>
由于 $`\mathcal{D} _ { R }`$ 作用在 $`\mathcal{D} _ { R } ^ { 2 } S`$ 上给出零, 对于 $`f ( \mathcal{D} _ { R } ^ { 2 } S )`$ 的任何一项中的一个 $`\mathcal{D} _ { R } ^ { 2 } S`$ 因子, 我们可以将其中的算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 提出来使之作用在外面.
以这种方法, 我们可以写下
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f81c781ece238f8d78936">
	$$
	f(\mathcal D_R^2S)=\mathcal D_R^2\tilde f(S).\tag{30.1.7}
	$$
</synced_block>
其中 $`\tilde { f } ( \boldsymbol { S } )`$ 是通过将 $`f ( \mathcal{D} _ { R } ^ { 2 } S )`$ 中的每一项略掉任何一个算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 获得的.
例如, 当超场只有一种时,如果 $`\begin{array} { r } { f ( \Phi ) = \sum _ { r } c _ { r } \Phi ^ { r } } \end{array}`$ , 那么
$$
\tilde f(S)=c_rS\left(\mathcal D_R^2S\right)^{r-1}.
$$
利用方程(30.1.6), (30.1.7)和(26.3.31), 我们可以将整个作用量写成 $`D`$ -项的形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f81f39414f74f72c0603e">
		$$
		I[\mathcal D_R^2S]=\frac12\int d^4x\left[S^*_n\mathcal D_L^2\mathcal D_R^2S^n\right]_D+2\operatorname{Re}\int d^4x\left[f(\mathcal D_R^2S)\right]_{\mathcal F}.\tag{30.1.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f81c781ece238f8d78936">
		$$
		f(\mathcal D_R^2S)=\mathcal D_R^2\tilde f(S).\tag{30.1.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f817abcb1ff1092871ce0">
	$$
	I[\mathcal D_R^2S]=\frac12\int d^4x\left[S^*_n\mathcal D_L^2\mathcal D_R^2S^n\right]_D+2\operatorname{Re}\int d^4x\left[\tilde f(S)\right]_{\mathcal F}.\tag{30.1.8}
	$$
</synced_block>
方程(26.6.5)表明这也可以写成一个超空间积分:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a114ff6b4b910489#34cee2b74b3f8138a5b3eab7e3bac613">
	$$
	I[\mathcal D_R^2S]=-\frac14\int d^4x\int d^4\theta\,S^*_n\mathcal D_L^2\mathcal D_R^2S^n-\operatorname{Re}\int d^4x\int d^4\theta\,\tilde f(S).\tag{30.1.9}
	$$
</synced_block>
在超图体系的路径积分推导中, 我们将使用这个作用量.
</content>
</page>
