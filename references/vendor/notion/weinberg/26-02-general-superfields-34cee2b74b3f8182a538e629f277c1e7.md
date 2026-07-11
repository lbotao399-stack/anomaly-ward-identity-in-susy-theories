Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7 as of 2026-06-30T03:26:17.926Z:
<page url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.2 一般超场"}
</properties>
<content>
通过上一节阐述的直接技巧, 构造场超多重态是直接的, 但是为了构造超对称作用量, 我们还需要知道如何将场超多重态乘起来给出其它的超多重态.
使用Salam和Strathdee发明的一套形式理论可以省下大量的功夫, 在那个形式理论中, 任何超多重态中的场被整合进单个超场中.
就像 4 -动量算符 $`P _ { \mu }`$ 定义成普通时空坐标 $`x ^ { \mu }`$ 的平移生成元, 4 个超对称生成元 $`{ \mathcal{Q} } _ { a }`$ 和 $`{ \mathcal{Q} } _ { a } ^ { * }`$ 也可以视作 4 个费米 c -数超空间坐标的平移生成元, 这些坐标彼此反对易且与费米场反对易, 但与 $`x ^ { \mu }`$ 和所有玻色场对易.
我们的目的是构建Lorentz不变的拉格朗日密度, 所以采取25.2描述的4 -分量 Dirac形式体系将是方便的.
超对称生成元被合并进一个 4 -分量 Majorana 旋量 $`Q _ { \alpha }`$ , 相应地, 超空间坐标被合并进另一个4 -分量Majorana旋量 $`\theta _ { \alpha }`$ .
(本章附录会概述Majorana旋量的各种性质.) 超对称生成元有不为零的反对易子, 所以我们不能简单地将它们取成正比于超坐标平移算符 $`\partial / \partial \theta _ { \alpha }`$ .
相反, Salam 和 Strathdee 发现, 如果我们设超对称生成元 $`Q`$ 与任何玻色或费米超场 $`S ( x , \theta )`$ 的对易子或反对易子是
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8129b0c9c3df0fd704d3">
	$$
	[ Q , S \} = \mathrm{i} \mathcal{Q} S \ , \tag{26.2.1}
	$$
</synced_block>
其中 $`\mathcal{Q}`$ 是超空间微分算符
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812e8a66c9b63a4d3331">
	$$
	\mathcal{Q} \equiv - \frac { \partial } { \partial \bar { \theta } } + \gamma ^ { \mu } \theta \frac { \partial } { \partial x ^ { \mu } } , \tag{26.2.2}
	$$
</synced_block>
那么超空间代数就是被满足的.
(像往常一样, $`\bar { \theta } \equiv \theta ^ { \dagger } \beta`$ .
所有对费米c -数变量的导数都应被理解成左导数, 计算时在对它微分前要将这个变量移至任何表达式的左边.) 对于 Majorana 旋量 $`\bar { \theta } =`$ $`\theta ^ { \mathrm { T } } \gamma _ { 5 } \epsilon`$ , 其中 $`4 \times 4`$ 矩阵 $`\epsilon`$ 由方程(26.A.3)给定, 所以方程(26.2.1)可以写成更加明显的
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81bbbc98c735742008ab">
		$$
		\epsilon\equiv\begin{pmatrix}e&0\\0&e\end{pmatrix}.\tag{26.A.3}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8129b0c9c3df0fd704d3">
		$$
		[ Q , S \} = \mathrm{i} \mathcal{Q} S \ , \tag{26.2.1}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8135b711e264d4c39f77">
	$$
	\mathcal{Q} _ { \alpha } = ( \gamma _ { 5 } \epsilon ) _ { \alpha \gamma } \frac { \partial } { \partial \theta _ { \gamma } } + \gamma _ { \alpha \gamma } ^ { \mu } \theta _ { \gamma } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.3}
	$$
</synced_block>
同理,
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f814db710fb9c6be9df38">
	$$
	\overline { { \mathcal{Q} } } _ { \beta } = \mathcal{Q} _ { \gamma } \left( \gamma _ { 5 } \epsilon \right) _ { \gamma \beta } = \frac { \partial } { \partial \theta _ { \beta } } - ( \gamma _ { 5 } \epsilon \gamma ^ { \mu } ) _ { \beta \gamma } \theta _ { \gamma } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.4}
	$$
</synced_block>
直接计算可以给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81898af9dd307e84ccf5">
	$$
	\left\{ \mathcal{Q} _ { \alpha } , \overline { { { \mathcal{Q} } } } _ { \beta } \right\} = ( \gamma _ { 5 } \epsilon \gamma ^ { \mu } \gamma _ { 5 } \epsilon ) _ { \beta \alpha } \frac { \partial } { \partial x ^ { \mu } } + \gamma _ { \alpha \beta } ^ { \mu } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.5}
	$$
</synced_block>
但是方程(5.4.35)表明 $`\gamma _ { \mu } ^ { \mathrm { T } } = - \mathcal{C} \gamma _ { \mu } \mathcal{C} ^ { - 1 }`$ , 其中 $`\mathcal{C}`$ 是矩阵 $`\mathcal{C} = - \gamma _ { 5 } \epsilon`$ , 所以方程(26.2.5)右边的两项是相等的, 因此
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81898af9dd307e84ccf5">
		$$
		\left\{ \mathcal{Q} _ { \alpha } , \overline { { { \mathcal{Q} } } } _ { \beta } \right\} = ( \gamma _ { 5 } \epsilon \gamma ^ { \mu } \gamma _ { 5 } \epsilon ) _ { \beta \alpha } \frac { \partial } { \partial x ^ { \mu } } + \gamma _ { \alpha \beta } ^ { \mu } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.5}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812a87f0d48dffd6bcba">
	$$
	\left\{ { \mathcal{Q} } _ { \alpha } , { \overline { { { \mathcal{Q} } } } } _ { \beta } \right\} = 2 \gamma _ { \alpha \beta } ^ { \mu } { \frac { \partial } { \partial x ^ { \mu } } } . \tag{26.2.6}
	$$
</synced_block>
方程(26.2.6)和(26.2.1)再加上广义 Jacobi 恒等式(25.1.5)表明
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812a87f0d48dffd6bcba">
		$$
		\left\{ { \mathcal{Q} } _ { \alpha } , { \overline { { { \mathcal{Q} } } } } _ { \beta } \right\} = 2 \gamma _ { \alpha \beta } ^ { \mu } { \frac { \partial } { \partial x ^ { \mu } } } . \tag{26.2.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8129b0c9c3df0fd704d3">
		$$
		[ Q , S \} = \mathrm{i} \mathcal{Q} S \ , \tag{26.2.1}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f816696bddd8d41f2d088">
	$$
	[ \{ Q _ { \alpha } , \overline { { { Q } } } _ { \beta } \} , S ] = \{ \mathcal{Q} _ { \alpha } , \overline { { { \mathcal{Q} } } } _ { \beta } \} S = 2 \gamma _ { \alpha \beta } ^ { \mu } \partial _ { \mu } S = - 2 \mathrm{i} \gamma _ { \alpha \beta } ^ { \mu } [ P _ { \mu } , S ] , \tag{26.2.7}
	$$
</synced_block>
与反对易关系(25.2.36)一致.
将对易和反对易关系(26.2.1)表示成在无限小超对称变换下的变换规则通常会更加方便.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8129b0c9c3df0fd704d3">
		$$
		[ Q , S \} = \mathrm{i} \mathcal{Q} S \ , \tag{26.2.1}
		$$
	</synced_block_reference>
</callout>
结合方程(26.1.18), (26.2.1) 和(26.2.2)表明无限小 Majorana 旋量参量为 $`\alpha`$ 的超对称变换对超场 $`S ( x , \theta )`$ 的变换是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8144bfa7d9c89936ea83">
		$$
		\mathrm{i} \delta { \mathcal O } ( x ) \equiv \left[ \bar { \alpha } Q , { \mathcal O } ( x ) \right] . \tag{26.1.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8129b0c9c3df0fd704d3">
		$$
		[ Q , S \} = \mathrm{i} \mathcal{Q} S \ , \tag{26.2.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812e8a66c9b63a4d3331">
		$$
		\mathcal{Q} \equiv - \frac { \partial } { \partial \bar { \theta } } + \gamma ^ { \mu } \theta \frac { \partial } { \partial x ^ { \mu } } , \tag{26.2.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f813a9f50c4e82207602f">
	$$
	\delta S = \left( { \bar { \alpha } } { \mathcal{Q} } \right) S = - \left( { \bar { \alpha } } { \frac { \partial S } { \partial { \bar { \theta } } } } \right) + \left( { \bar { \alpha } } \gamma ^ { \mu } \theta \right) { \frac { \partial S } { \partial x ^ { \mu } } } . \tag{26.2.8}
	$$
</synced_block>
注意这里的 $`\partial / \partial { \bar { \theta } }`$ 作用在任何表达式的左边.
特别的, 当 $`M`$ 是矩阵 1, $`\gamma _ { 5 } \gamma _ { \mu }`$ 和 $`\gamma _ { 5 }`$ 的线性组合且使得 $`{ \bar { \theta } } M \theta`$ 不为零, 我们有 $`\bar { \theta } ^ { \prime } M \theta ^ { \prime \prime } = \bar { \theta } ^ { \prime \prime } M \theta ^ { \prime }`$ , 所以
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a4859ee182fc8c4658">
	$$
	\frac { \partial } { \partial \theta } ( \bar { \theta } M \theta ) = 2 M \theta . \tag{26.2.9}
	$$
</synced_block>
$`\theta`$ 的分量反对易, 所以对于它们的分量的任意乘积, 如果其中有两个相等, 这个乘积为零.
但是 $`\theta`$ 只有4 个分量, 所以对于 $`\theta`$ 的任何函数, 它的幂级数展开至于四次项.
更进一步, 本章附录将会证明, 两个 $`\theta`$ 的乘积正比于 $`( { \bar { \theta } } \theta )`$ , $`( \bar { \theta } \gamma _ { \mu } \gamma _ { 5 } \theta )`$ 和 $`( \bar { \theta } \gamma _ { 5 } \theta )`$ 的线性组合; 三个 $`\theta`$ 的乘积正比于 $`( { \bar { \theta } } \gamma _ { 5 } \theta ) \theta`$ ; 四个 $`\theta`$ 的乘积正比于 $`( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 }`$ .
因此 $`x ^ { \mu }`$ 和 $`\theta`$ 的最一般函数可以表示成
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a5ae59cc8919a6be32">
	$$
	\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
	$$
</synced_block>
(为了后面的方便, 我们分别从 $`\lambda ( x )`$ 和 $`D ( x )`$ 中分别分离出了 $`{ \scriptstyle { \frac { 1 } { 2 } } } \not\!\partial\, \omega`$ 和 $`{ \scriptstyle { \frac { 1 } { 2 } } } \Box C ( x )`$ .) 如果 $`S ( x , \theta )`$ 是标量, 那么 $`C ( x ) , M ( x ) , N ( x )`$ 和 $`D ( x )`$ 是标量(或赝标量)场; $`\omega ( x )`$ 和 $`\lambda ( x )`$ 是4 -分量旋量场; $`V ^ { \mu } ( x )`$ 是矢量场.
另外, 通过使用本章附录给出的 Majorana 场双线性积的实性质, 我们可以看到, 如果$`S ( x , \theta )`$ 是实的, 那么 $`C ( x )`$ , $`M ( x )`$ , $`N ( x )`$ , $`\scriptstyle V ^ { \mu } ( x )`$ 和 $`D ( x )`$ 都是实的, 而 $`\omega ( x )`$ 和 $`\lambda ( x )`$ 是满足相位约定 $`s ^ { * } = - \beta \epsilon \gamma _ { 5 } s`$ 的 Majorana 旋量.
现在我们必须解出方程(26.2.10)中的分量场的超对称变换性质.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
对展开(26.2.10)应用(26.2.8)和(26.2.9), 这给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f813a9f50c4e82207602f">
		$$
		\delta S = \left( { \bar { \alpha } } { \mathcal{Q} } \right) S = - \left( { \bar { \alpha } } { \frac { \partial S } { \partial { \bar { \theta } } } } \right) + \left( { \bar { \alpha } } \gamma ^ { \mu } \theta \right) { \frac { \partial S } { \partial x ^ { \mu } } } . \tag{26.2.8}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a4859ee182fc8c4658">
		$$
		\frac { \partial } { \partial \theta } ( \bar { \theta } M \theta ) = 2 M \theta . \tag{26.2.9}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
\delta S&=(\bar\alpha\gamma^\mu\theta)\frac{\partial C}{\partial x^\mu}
+\mathrm{i}(\bar\alpha\gamma_5\omega)-\mathrm{i}(\bar\alpha\gamma^\mu\theta)\left(\bar\theta\gamma_5\frac{\partial\omega}{\partial x^\mu}\right)\\
&\quad+\mathrm{i}(\bar\alpha\gamma_5\theta)M-\frac12(\bar\alpha\gamma^\mu\theta)(\bar\theta\gamma_5\theta)\frac{\partial M}{\partial x^\mu}\\
&\quad+(\bar\alpha\theta)N-\frac12(\bar\alpha\gamma^\mu\theta)(\bar\theta\theta)\frac{\partial N}{\partial x^\mu}\\
&\quad-\mathrm{i}(\bar\alpha\gamma_5\gamma_\nu\theta)V^\nu+\frac{\mathrm{i}}2(\bar\alpha\gamma^\mu\theta)(\bar\theta\gamma_5\gamma_\nu\theta)\frac{\partial V^\nu}{\partial x^\mu}\\
&\quad+2\mathrm{i}(\bar\alpha\gamma_5\theta)\left(\bar\theta\left[\lambda+\frac12\not\!\partial\omega\right]\right)
+\mathrm{i}(\bar\theta\gamma_5\theta)\left(\bar\alpha\left[\lambda+\frac12\not\!\partial\omega\right]\right)\\
&\quad-\mathrm{i}(\bar\alpha\gamma^\mu\theta)(\bar\theta\gamma_5\theta)\left(\bar\theta\partial_\mu\left[\lambda+\frac12\not\!\partial\omega\right]\right)
+(\bar\theta\gamma_5\theta)(\bar\alpha\gamma_5\theta)\left[D+\frac12\Box C\right].
\end{aligned}
$$
我们需要将每一项变成方程(26.2.10)的标准形式.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
对于这个目的, 我们注意到: 方程(26.A.9)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81ed90b4fd1a2f33b2df">
		$$
		\begin{array} { r } { s \bar { s } = - \frac { 1 } { 4 } ( \bar { s } s ) + \frac { 1 } { 4 } \gamma _ { 5 } \gamma _ { \mu } ( \bar { s } \gamma _ { 5 } \gamma ^ { \mu } s ) - \frac { 1 } { 4 } \gamma _ { 5 } \left( \bar { s } \gamma _ { 5 } s \right) . } \end{array} \tag{26.A.9}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r } { ( \bar { \alpha } \gamma ^ { \mu } \theta ) ( \bar { \theta } \gamma _ { 5 } \partial _ { \mu } \omega ) = - \frac { 1 } { 4 } ( \bar { \theta } \theta ) ( \bar { \alpha } \not\!\partial\, \gamma _ { 5 } \omega ) - \frac { 1 } { 4 } ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \nu } \theta ) ( \bar { \alpha } \not\!\partial\, \gamma _ { \nu } \omega ) - \frac { 1 } { 4 } ( \bar { \theta } \gamma _ { 5 } \theta ) ( \bar { \alpha } \not\!\partial\, \omega ) ; } \end{array}
$$
方程(26.A.16)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81ba90b3cb0dc40f0b4c">
		$$
		s _ { \alpha } \left( \bar { s } s \right) = - ( \gamma _ { 5 } s ) _ { \alpha } \left( \bar { s } \gamma _ { 5 } s \right) \tag{26.A.16}
		$$
	</synced_block_reference>
</callout>
$$
( \bar { \alpha } \gamma ^ { \mu } \theta ) ( \bar { \theta } \theta ) = - ( \bar { \alpha } \gamma ^ { \mu } \gamma _ { 5 } \theta ) ( \bar { \theta } \gamma _ { 5 } \theta ) ;
$$
方程(26.A.17)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8168865bf41f3dacf374">
		$$
		s _ { \alpha } \left( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \right) = - ( \gamma _ { \mu } s ) _ { \alpha } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) . \tag{26.A.17}
		$$
	</synced_block_reference>
</callout>
$$
( \bar { \alpha } \gamma ^ { \mu } \theta ) ( \bar { \theta } \gamma _ { 5 } \gamma _ { \nu } \theta ) = - ( \bar { \alpha } \gamma ^ { \mu } \gamma _ { \nu } \theta ) ( \bar { \theta } \gamma _ { 5 } \theta ) ;
$$
方程(26.A.9)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81ed90b4fd1a2f33b2df">
		$$
		\begin{array} { r } { s \bar { s } = - \frac { 1 } { 4 } ( \bar { s } s ) + \frac { 1 } { 4 } \gamma _ { 5 } \gamma _ { \mu } ( \bar { s } \gamma _ { 5 } \gamma ^ { \mu } s ) - \frac { 1 } { 4 } \gamma _ { 5 } \left( \bar { s } \gamma _ { 5 } s \right) . } \end{array} \tag{26.A.9}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r l } & { ( \bar { \alpha } \gamma _ { 5 } \theta ) ( \bar { \theta } [ \lambda + \frac { 1 } { 2 } \not\!\partial\, \omega ] ) = - \frac { 1 } { 4 } ( \bar { \theta } \theta ) ( \bar { \alpha } \gamma _ { 5 } [ \lambda + \frac { 1 } { 2 } \not\!\partial\, \omega ] ) + \frac { 1 } { 4 } ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta ) ( \bar { \alpha } \gamma _ { \mu } [ \lambda + \frac { 1 } { 2 } \not\!\partial\, \omega ] ) } \\ & { \quad \quad \quad \quad \quad \quad - \frac { 1 } { 4 } ( \bar { \theta } \gamma _ { 5 } \theta ) ( \bar { \alpha } [ \lambda + \frac { 1 } { 2 } \not\!\partial\, \omega ] ) ; } \end{array}
$$
方程(26.A.19)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81459208c3b78885c16b">
		$$
		\begin{array} { r } { ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } s \bar { s } = - \frac { 1 } { 4 } \gamma _ { 5 } ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } . } \end{array} \tag{26.A.19}
		$$
	</synced_block_reference>
</callout>
$$
( \bar { \alpha } \gamma ^ { \mu } \theta ) ( \bar { \theta } \gamma _ { 5 } \theta ) ( \bar { \theta } \partial _ { \mu } [ \lambda + { \textstyle \frac { 1 } { 2 } } \not\!\partial\, \omega ] ) = - { \textstyle \frac 1 4 } ( \bar { \alpha } \not\!\partial\, \gamma _ { 5 } [ \lambda + { \textstyle \frac { 1 } { 2 } } \not\!\partial\, \omega ] ) ( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 } .
$$
利用这些关系并按照 $`\theta`$ 因子数目递增的顺序重排这些项, 我们有
$$
\begin{array} { r l } & { \delta S = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega \right) + \left( \bar { \alpha } [ \not\!\partial\, C + \mathrm{i} \gamma _ { 5 } M + N - \mathrm{i} \gamma _ { 5 } \not\! V ] \theta \right) } \\ & { \qquad - \frac { 1 } { 2 } \mathrm{i} \left( \bar { \theta } \theta \right) \left( \bar { \alpha } \gamma _ { 5 } [ \lambda + \not\!\partial\, \omega ] \right) + \frac { 1 } { 2 } \mathrm{i} \left( \bar { \theta } \gamma _ { 5 } \theta \right) \left( \bar { \alpha } [ \lambda + \not\!\partial\, \omega ] \right) } \\ & { \qquad + \frac { 1 } { 2 } \mathrm{i} \left( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta \right) \left( \bar { \alpha } \gamma _ { \mu } \lambda \right) + \frac { 1 } { 2 } \mathrm{i} \left( \bar { \theta } \gamma _ { 5 } \gamma ^ { \nu } \theta \right) \left( \bar { \alpha } \partial _ { \nu } \omega \right) } \\ & { \qquad + \frac { 1 } { 2 } \left( \bar { \theta } \gamma _ { 5 } \theta \right) \left( \bar { \alpha } [ - \mathrm{i} \not\!\partial M - \gamma _ { 5 } \not\!\partial N - \mathrm{i} \not\!\partial\, \not\! V + \gamma _ { 5 } ( D + \frac { 1 } { 2 } \Box C ) ] \theta \right) } \\ & { \qquad - \frac { 1 } { 4 } \mathrm{i} \left( \bar { \theta } \gamma _ { 5 } \theta \right) ^ { 2 } \left( \bar { \alpha } \gamma _ { 5 } [ \not\!\partial\, \lambda + \frac { 1 } { 2 } \Box \omega ] \right) , } \end{array}
$$
或者, 利用对称性(26.A.7)
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812dbfd2df88f108bb3b">
		$$
		( \overline { { { s _ { 1 } } } } M s _ { 2 } ) = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = 1 , \gamma _ { 5 } \gamma _ { \mu } , \gamma _ { 5 } } } \\ { { - ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = \gamma _ { \mu } , [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \end{array} \right. . \tag{26.A.7}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r l } & { \delta S = \mathrm{i} ( \bar { \alpha } \gamma _ { 5 } \omega ) + ( \bar { \theta } [ - \not\!\partial\, C + \mathrm{i} \gamma _ { 5 } M + N - \mathrm{i} \gamma _ { 5 } \not\! V ] \alpha ) } \\ & { \qquad - \frac { 1 } { 2 } \mathrm{i} ( \bar { \theta } \theta ) ( \bar { \alpha } \gamma _ { 5 } [ \lambda + \not\!\partial\, \omega ] ) + \frac { 1 } { 2 } \mathrm{i} ( \bar { \theta } \gamma _ { 5 } \theta ) ( \bar { \alpha } [ \lambda + \not\!\partial\, \omega ] ) } \\ & { \qquad + \frac { 1 } { 2 } \mathrm{i} ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta ) ( \bar { \alpha } \gamma _ { \mu } \lambda ) + \frac { 1 } { 2 } \mathrm{i} ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \nu } \theta ) ( \bar { \alpha } \partial _ { \nu } \omega ) } \\ & { \qquad + \frac { 1 } { 2 } ( \bar { \theta } \gamma _ { 5 } \theta ) ( \bar { \theta } [ \mathrm{i} \not\!\partial M - \gamma _ { 5 } \not\!\partial N - \mathrm{i} \partial _ { \mu } \not\! V \gamma ^ { \mu } + \gamma _ { 5 } ( D + \frac { 1 } { 2 } \Box C ) ] \alpha ) } \\ & { \qquad - \frac { 1 } { 4 } \mathrm{i} ( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 } ( \bar { \alpha } \gamma _ { 5 } [ \not\!\partial\, \lambda + \frac { 1 } { 2 } \Box \omega ] ) . } \end{array}
$$
如果我们比较上式与展开(26.2.10)中 $`\theta`$ 的零阶, 一阶和二阶项, 我们发现变换规则:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81d98e3ffeb867240dab">
	$$
	\begin{array} { r l } & { \delta C = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega \right) , } \\ & { \delta \omega = \left( - \mathrm{i} \gamma _ { 5 } \partial C - M + \mathrm{i} \gamma _ { 5 } N + V \right) \alpha , } \\ & { \delta M = - \left( \bar { \alpha } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta N = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta V _ { \mu } = \left( \bar { \alpha } \gamma _ { \mu } \lambda \right) + \left( \bar { \alpha } \partial _ { \mu } \omega \right) . } \end{array} \tag{26.2.12-26.2.14}
	$$
</synced_block>
$`\theta`$ 的三阶项和四阶项给出
$$
\begin{array} { r l } & { \delta [ \lambda + \frac { 1 } { 2 } \not\!\partial\, \omega ] = \frac { 1 } { 2 } \Big [ - \not\!\partial\, M - \mathrm{i} \gamma _ { 5 } \not\!\partial\, N + \partial _ { \mu } \not\! V \gamma ^ { \mu } + \mathrm{i} \gamma _ { 5 } \Big ( D + \frac { 1 } { 2 } \Box C \Big ) \Big ] \alpha } \\ & { \delta [ D + \frac { 1 } { 2 } \Box C ] = \mathrm{i} \Big ( \bar { \alpha } \gamma _ { 5 } [ \not\!\partial\, \lambda + \frac { 1 } { 2 } \Box \omega ] \Big ) . } \end{array}
$$
结合后两个变换规则与 $`C`$ 和 $`\omega`$ 的变换规则(26.2.11)和(26.2.12), 这给出 $`\lambda`$ 和 $`D`$ 更加简单的变换规则:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81d98e3ffeb867240dab">
		$$
		\begin{array} { r l } & { \delta C = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega \right) , } \\ & { \delta \omega = \left( - \mathrm{i} \gamma _ { 5 } \partial C - M + \mathrm{i} \gamma _ { 5 } N + V \right) \alpha , } \\ & { \delta M = - \left( \bar { \alpha } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta N = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta V _ { \mu } = \left( \bar { \alpha } \gamma _ { \mu } \lambda \right) + \left( \bar { \alpha } \partial _ { \mu } \omega \right) . } \end{array} \tag{26.2.12-26.2.14}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f815ab667da80eecb2eaa">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { \delta \lambda = \left( \frac { 1 } { 2 } \Big [ \partial _ { \mu } { \cal V } , \gamma ^ { \mu } \Big ] + \mathrm{i} \gamma _ { 5 } D \right) \alpha , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \delta D = \mathrm{i} \Big ( \bar { \alpha } \gamma _ { 5 } \not\!\partial\, \lambda \Big ) . } } \end{array} \tag{26.2.16-26.2.17}
	$$
</synced_block>
在展开(26.2.10)中从 $`\lambda`$ 和 $`D`$ 中分离出 $`{ \scriptstyle { \frac { 1 } { 2 } } } \not\!\partial\, \omega`$ 和 $`\scriptstyle { \frac { 1 } { 2 } } \Box C`$ 正是为了实现这个简化.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
超场形式体系的关键就是简化了用超多重态制造其它超多重态这个任务.
给定两个都满足变换规则(26.2.8)的超场 $`S _ { 1 }`$ 和 $`S _ { 2 }`$ , 它们的乘积 $`S \equiv S _ { 1 } S _ { 2 }`$ 满足
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f813a9f50c4e82207602f">
		$$
		\delta S = \left( { \bar { \alpha } } { \mathcal{Q} } \right) S = - \left( { \bar { \alpha } } { \frac { \partial S } { \partial { \bar { \theta } } } } \right) + \left( { \bar { \alpha } } \gamma ^ { \mu } \theta \right) { \frac { \partial S } { \partial x ^ { \mu } } } . \tag{26.2.8}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8127837ffcbfbbf405e1">
	$$
	\begin{array} { r l } & { \delta S \equiv \left[ ( \bar { \alpha } Q ) , S _ { 1 } S _ { 2 } \right] = ( \delta S _ { 1 } ) S _ { 2 } + S _ { 1 } ( \delta S _ { 2 } ) } \\ & { \quad \quad = \Big ( ( \bar { \alpha } \mathcal{Q} ) S _ { 1 } \Big ) S _ { 2 } + S _ { 1 } \Big ( ( \bar { \alpha } \mathcal{Q} ) \Big ) S _ { 2 } = ( \bar { \alpha } \mathcal{Q} ) S , } \end{array} \tag{26.2.18}
	$$
</synced_block>
因此也是个超场.
利用方程(26.A.7), (26.A.16), (26.A.18)和(26.A.19)直接进行计算就给出了它的
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812dbfd2df88f108bb3b">
		$$
		( \overline { { { s _ { 1 } } } } M s _ { 2 } ) = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = 1 , \gamma _ { 5 } \gamma _ { \mu } , \gamma _ { 5 } } } \\ { { - ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = \gamma _ { \mu } , [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \end{array} \right. . \tag{26.A.7}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81ba90b3cb0dc40f0b4c">
		$$
		s _ { \alpha } \left( \bar { s } s \right) = - ( \gamma _ { 5 } s ) _ { \alpha } \left( \bar { s } \gamma _ { 5 } s \right) \tag{26.A.16}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81678701ee7b96af9b3b">
		$$
		\Bigl ( \bar { s } s \Bigr ) ^ { 2 } = - \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } , \qquad \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \Bigr ) \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \nu } s \Bigr ) = - \eta _ { \mu \nu } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } . \tag{26.A.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81459208c3b78885c16b">
		$$
		\begin{array} { r } { ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } s \bar { s } = - \frac { 1 } { 4 } \gamma _ { 5 } ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } . } \end{array} \tag{26.A.19}
		$$
	</synced_block_reference>
</callout>
分量场
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f811eb87ae4e8b22b7f1a">
	$$
	\begin{array} { r l } & { C = C _ { 1 } C _ { 2 } , } \\ & { \omega = C _ { 1 } \omega _ { 2 } + C _ { 2 } \omega _ { 1 } , } \\ & { M = C _ { 1 } M _ { 2 } + C _ { 2 } M _ { 1 } + \frac { 1 } { 2 } \mathbf{i} ( \overline { { \omega _ { 1 } } } \gamma _ { 5 } \omega _ { 2 } ) , } \\ & { N = C _ { 1 } N _ { 2 } + C _ { 2 } N _ { 1 } - \frac { 1 } { 2 } ( \overline { { \omega _ { 1 } } } \omega _ { 2 } ) , } \\ & { V ^ { \mu } = C _ { 1 } V _ { 2 } ^ { \mu } + C _ { 2 } V _ { 1 } ^ { \mu } - \frac { 1 } { 2 } \mathbf{i} ( \overline { { \omega _ { 1 } } } \gamma _ { 5 } \gamma ^ { \mu } \omega _ { 2 } ) , } \\ & { \lambda = C _ { 1 } \lambda _ { 2 } + C _ { 2 } \lambda _ { 1 } - \frac { 1 } { 2 } \gamma ^ { \mu } \omega _ { 1 } \partial _ { \mu } C _ { 2 } - \frac { 1 } { 2 } \gamma ^ { \mu } \omega _ { 2 } \partial _ { \mu } C _ { 1 } + \frac { 1 } { 2 } \mathbf{i} \dot { V } _ { 1 } \gamma _ { 5 } \omega _ { 2 } + \frac { 1 } { 2 } \mathbf{i} \dot { V } _ { 2 } \gamma _ { 5 } \omega _ { 1 } } \\ & { \quad + \frac { 1 } { 2 } ( N _ { 1 } - \mathrm{i} \gamma _ { 5 } M _ { 1 } ) \omega _ { 2 } + \frac { 1 } { 2 } ( N _ { 2 } - \mathrm{i} \gamma _ { 5 } M _ { 2 } ) \omega _ { 1 } , } \\ & { \quad \quad - \frac { 1 } { 2 } ( \overline { { V } } _ { 1 } - \mathrm{i} \gamma _ { 5 } \omega _ { 2 } ) \omega _ { 1 } - \frac { 1 } { 2 } \gamma \omega _ { 2 } ^ { 2 } \omega _ { 2 } , } \end{array} \tag{26.2.21-26.2.23}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8103987cebe8cff53688">
	$$
	D = - \partial _ { \mu } C _ { 1 } \partial ^ { \mu } C _ { 2 } + C _ { 1 } D _ { 2 } + C _ { 2 } D _ { 1 } + M _ { 1 } M _ { 2 } + N _ { 1 } N _ { 2 } \tag{26.2.24}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8146a520db0bd1246217">
	$$
	\begin{array} { r } { - \left( \overline { { \omega _ { 1 } } } [ \lambda _ { 2 } + \frac { 1 } { 2 } \not\!\partial\, \omega _ { 2 } ] \right) - \left( \overline { { \omega _ { 2 } } } [ \lambda _ { 1 } + \frac { 1 } { 2 } \not\!\partial\, \omega _ { 1 } ] \right) - V _ { 1 \mu } V _ { 2 } ^ { \mu } . } \end{array} \tag{26.2.25}
	$$
</synced_block>
超场的线性组合平庸地是超场, 在同等意义下, 超场的时空导数和复共轭也是超场.
但是给超场乘以 $`\theta`$ 的某个函数或者做相对于 $`\theta`$ 的微分一般不会给出超场.
(例如, $`\theta`$ 自身显然不是超场, 这是因为 $`\theta`$ 是费米 $`\mathrm { c }`$ -数因而与 $`\bar { \alpha } Q`$ 对易, 而 $`\mathcal{Q} \theta \neq 0 .`$ .) 然而, 有一种方式可以组合超场对 $`\theta`$ 的导数和它与因子 $`\theta`$ 的乘积, 使得确实产生另一个超场.
考察超空间微分算符 $`{ \mathcal{D} } _ { \alpha }`$ , 它定义成
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81228ecbee4906baf10a">
	$$
	\mathcal{D} \equiv - \frac { \partial } { \partial \bar { \theta } } - \gamma ^ { \mu } \theta \frac { \partial } { \partial x ^ { \mu } } , \tag{26.2.26}
	$$
</synced_block>
或者更加清楚些
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8164ac70d5b474269ce4">
	$$
	\mathcal{D} _ { \alpha } = ( \gamma _ { 5 } \epsilon ) _ { \alpha \gamma } \frac { \partial } { \partial \theta _ { \gamma } } - \gamma _ { \alpha \gamma } ^ { \mu } \theta _ { \gamma } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.27}
	$$
</synced_block>
$`\mathcal{D}`$ 和 $`\mathcal{Q}`$ 的定义的唯一差异是包含时空导数那一项的符号变了.
这个符号变化的结果是, 在 $`\mathcal{D} _ { \beta }`$ 和$`{ \mathcal{Q} } _ { \alpha }`$ 的反对易子中, 取代像方程(26.2.6)中那样获得相同的两项, 我们现在得到的项有相反的符号,这使得它们抵消:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812a87f0d48dffd6bcba">
		$$
		\left\{ { \mathcal{Q} } _ { \alpha } , { \overline { { { \mathcal{Q} } } } } _ { \beta } \right\} = 2 \gamma _ { \alpha \beta } ^ { \mu } { \frac { \partial } { \partial x ^ { \mu } } } . \tag{26.2.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a49bb7df5ad53ad484">
	$$
	\{ \mathcal{D} _ { \beta } , \mathcal{Q} _ { \alpha } \} = 0 . \tag{26.2.28}
	$$
</synced_block>
由于 $`\alpha`$ 是费米的, 可以得出 $`( \alpha \mathcal{Q} )`$ 与 $`\mathcal{D} _ { \beta }`$ 对易, 所以, 如果 $`S ( x , \theta )`$ 是超场, 那么
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f815285d3eb55979563d3">
	$$
	\delta \mathcal{D} _ { \beta } S \equiv - \mathrm{i} [ \bar { \alpha } Q , \mathcal{D} _ { \beta } S ] = - \mathrm{i} \mathcal{D} _ { \beta } [ ( \bar { \alpha } Q ) , S ] = \mathcal{D} _ { \beta } ( \bar { \alpha } \mathcal{Q} ) S = ( \bar { \alpha } \mathcal{Q} ) \mathcal{D} _ { \beta } S , \tag{26.2.29}
	$$
</synced_block>
这使得 $`\mathcal{D} _ { \beta } S`$ 也是个超场.
因此, 超场 $`S`$ 和它们的超导数 $`\mathcal{D} _ { \beta } S`$ , $`{ \mathcal{D} } _ { \beta } { \mathcal{D} } _ { \gamma } S`$ 等的任意多项式函数也是超场.
虽然不是必须的, 但在这里提一下, 在用超场构建超场是可以纳入它们的时空导数.
这是因为这些时空导数可以通过二阶超导数获得.
由于 $`\mathcal{D} _ { \beta }`$ 和 $`{ \mathcal{Q} } _ { \beta }`$ 的唯一差异是包含 $`\partial _ { \mu }`$ 那一项的符号, 除了一个符号变化外, $`\mathcal{D}`$ 的反对易子与 $`\mathcal{Q}`$ 的反对易子相同:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81738a97d99db41eabd6">
	$$
	\Big \{ \mathcal{D} _ { \alpha } , \overline { { { \mathcal{D} } } } _ { \beta } \Big \} = - 2 \gamma _ { \alpha \beta } ^ { \mu } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.30}
	$$
</synced_block>
现在, 我们来考察如何用超场构建超对称作用量.
首先不存在超对称拉格朗日密度这种东西,这是因为, 反对易关系(26.2.6)表明, 如果 $`\delta \mathcal{L} = 0`$ , 那么 $`\mathcal{L}`$ 必须是个常数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812a87f0d48dffd6bcba">
		$$
		\left\{ { \mathcal{Q} } _ { \alpha } , { \overline { { { \mathcal{Q} } } } } _ { \beta } \right\} = 2 \gamma _ { \alpha \beta } ^ { \mu } { \frac { \partial } { \partial x ^ { \mu } } } . \tag{26.2.6}
		$$
	</synced_block_reference>
</callout>
即使拉格朗日密度不是超对称的, 如果 $`\delta { \mathcal{L} } ( x )`$ 是导数项, 它就不会贡献 $`\delta \int \mathcal{L} \mathrm { d } ^ { 4 } x`$ , 那么作用量将仍然是超对称的.
一般而言, 拉格朗日密度可以写成一些项的和, 其中每一项是用基本超场和它们的超导数构建的超场的某个分量.
观察各个分量的变换规则(26.2.11)—(26.2.17)表明, 如果在一般超场上没有特殊条件, 这种超场在变分下是个导数的唯一分量是 $`D`$ -分量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f815ab667da80eecb2eaa">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { \delta \lambda = \left( \frac { 1 } { 2 } \Big [ \partial _ { \mu } { \cal V } , \gamma ^ { \mu } \Big ] + \mathrm{i} \gamma _ { 5 } D \right) \alpha , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \delta D = \mathrm{i} \Big ( \bar { \alpha } \gamma _ { 5 } \not\!\partial\, \lambda \Big ) . } } \end{array} \tag{26.2.16-26.2.17}
		$$
	</synced_block_reference>
</callout>
另外, 为了是任何超场的 $`D`$ -分量是个标量, 超场本身也必须是个标量.
因此, 除非在构建拉格朗日密度的各个超场上有特殊条件, 否则超对称作用量只能是对标量超场 $`\Lambda`$ 的 $`D`$ -项的积分:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81199c62e24848d8f6dc">
	$$
	I = \int \mathrm { d } ^ { 4 } x [ \Lambda ] _ { D } . \tag{26.2.31}
	$$
</synced_block>
然而, 事实上, 如果在构建作用量的超场上没有特殊条件, 那么这类作用量没有一个在物理上是令人满意的.
对于一般超场 $`S ( x , \theta )`$ , 唯一一种既是 $`S`$ 和 $`S ^ { * }`$ 的双线性, 对分量场的导数又不超过二阶的超对称动能作用量 $`I _ { 0 }`$ 是如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81bbb8e0dadd0523ae79">
	$$
	I _ { 0 } \propto \int \mathrm { d } ^ { 4 } x \left[ S ^ { * } S \right] _ { D } . \tag{26.2.32}
	$$
</synced_block>
我们从方程(26.2.25)中看到 $`S ^ { \ast } S`$ 有 $`D`$ -分量
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8146a520db0bd1246217">
		$$
		\begin{array} { r } { - \left( \overline { { \omega _ { 1 } } } [ \lambda _ { 2 } + \frac { 1 } { 2 } \not\!\partial\, \omega _ { 2 } ] \right) - \left( \overline { { \omega _ { 2 } } } [ \lambda _ { 1 } + \frac { 1 } { 2 } \not\!\partial\, \omega _ { 1 } ] \right) - V _ { 1 \mu } V _ { 2 } ^ { \mu } . } \end{array} \tag{26.2.25}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f812d9298e3af4ddccab9">
	$$
	\begin{array} { c } { { { \Big [ } S ^ { * } S { \Big ] } _ { D } = - \partial _ { \mu } C ^ { * } \partial ^ { \mu } C - { \textstyle \frac { 1 } { 2 } } \Big ( \bar { \omega } \gamma ^ { \mu } \partial _ { \mu } \omega \Big ) + { \textstyle \frac { 1 } { 2 } } \Big ( ( \partial _ { \mu } \bar { \omega } ) \gamma ^ { \mu } \omega \Big ) } } \\ { { { } } } \\ { { + C ^ { * } D + D ^ { * } C - \Big ( \bar { \omega } \lambda \Big ) + \Big ( \bar { \lambda } \omega \Big ) } } \\ { { { } } } \\ { { + M ^ { * } M + N ^ { * } N - V _ { \mu } ^ { * } V ^ { \mu } . } } \end{array} \tag{26.2.33}
	$$
</synced_block>
$`C`$ 和 $`\omega`$ 的二次项和期望中的一样看起来是自旋零和 $`1 / 2`$ 的无质量场的动能拉格朗日量; 最后三项是无害的; 但是包含 $`D`$ 和 $`\lambda`$ 的项在路径积分中有灾难性的结果, 它们会约束 $`C`$ 和 $`\omega`$ 为零.
幸运的是, 就像我们将在下一节看到的, 存在一些受约束的超场, 使得我们可以用它们构造出物理上合理的作用量.
引入这些受约束的超场同时也打开在作用量中构建超对称项的方法, 它们可以不是超场函数的 $`D`$ -分量.
如果宇称是守恒的, 那么超场的分量场的空间反演性质将通过超对称关联起来.
为了解出这个关系,我们对对易(反对易)关系(26.2.1)作用宇称算符P并使用超对称生成元的变换性质(25.3.16),这给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8129b0c9c3df0fd704d3">
		$$
		[ Q , S \} = \mathrm{i} \mathcal{Q} S \ , \tag{26.2.1}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f813c8c8ed733558dcbb9">
	$$
	\mathrm{i} \beta \Big [ Q , \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } \Big \} = \mathcal{Q} \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } . \tag{26.2.34}
	$$
</synced_block>
对于标量超场, 方程(26.2.34)的解是如下形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f813c8c8ed733558dcbb9">
		$$
		\mathrm{i} \beta \Big [ Q , \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } \Big \} = \mathcal{Q} \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } . \tag{26.2.34}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8126bddeead3c28f07ed">
	$$
	\mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } = \eta S ( \Lambda _ { P } x , - \mathrm{i} \beta \theta ) , \tag{26.2.35}
	$$
</synced_block>
其中 $`\eta`$ 是某个相位(超场的内禀宇称), $`\Lambda _ { P } x \equiv ( - \mathbf{x} , + x ^ { 0 } )`$ .
(为了验证方程(26.2.35)满足(26.2.34),注意到方程(26.2.35)给出的方程(26.2.34)的左边是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8126bddeead3c28f07ed">
		$$
		\mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } = \eta S ( \Lambda _ { P } x , - \mathrm{i} \beta \theta ) , \tag{26.2.35}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f813c8c8ed733558dcbb9">
		$$
		\mathrm{i} \beta \Big [ Q , \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } \Big \} = \mathcal{Q} \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } . \tag{26.2.34}
		$$
	</synced_block_reference>
</callout>
$$
\mathrm{i} \eta \beta \left( - \frac { \partial } { \partial ( - \mathrm{i} \beta \theta ) } + \gamma ^ { \mu } ( - \mathrm{i} \beta \theta ) \frac { \partial } { \partial ( \Lambda _ { P } x ) ^ { \mu } } \right) S ( \Lambda _ { P } x , \theta ) = \eta \mathcal{Q} S ( \Lambda _ { P } x , - \mathrm{i} \beta \theta ) ,
$$
与方程(26.2.35)给出的方程(26.2.34)的右边一致.) 在方程(26.2.35)中使用展开(26.2.10)就给出了
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8126bddeead3c28f07ed">
		$$
		\mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } = \eta S ( \Lambda _ { P } x , - \mathrm{i} \beta \theta ) , \tag{26.2.35}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f813c8c8ed733558dcbb9">
		$$
		\mathrm{i} \beta \Big [ Q , \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } \Big \} = \mathcal{Q} \mathsf { P } ^ { - 1 } S ( x , \theta ) \mathsf { P } . \tag{26.2.34}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
分量场的空间反演性质:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f8168a952eb821d23545d">
	$$
	\begin{array} { r l } & { \mathsf { P } ^ { - 1 } C ( x ) \mathsf { P } = \eta C ( \Lambda _ { P } x ) , } \\ & { \mathsf { P } ^ { - 1 } \boldsymbol { \omega } ( x ) \mathsf { P } = - \mathrm{i} \eta \beta \boldsymbol { \omega } ( \Lambda _ { P } x ) , } \\ & { \mathsf { P } ^ { - 1 } M ( x ) \mathsf { P } = - \eta M ( \Lambda _ { P } x ) , } \\ & { \mathsf { P } ^ { - 1 } N ( x ) \mathsf { P } = \eta N ( \Lambda _ { P } x ) , } \\ & { \mathsf { P } ^ { - 1 } V ^ { \mu } ( x ) \mathsf { P } = - \eta \left( \Lambda _ { P } \right) ^ { \mu } {} _ { \nu } V ^ { \nu } ( \Lambda _ { P } x ) , } \\ & { \mathsf { P } ^ { - 1 } \lambda ( x ) \mathsf { P } = \mathrm{i} \eta \beta \boldsymbol { \lambda } ( \Lambda _ { P } x ) , } \\ & { \mathsf { P } ^ { - 1 } D ( x ) \mathsf { P } = \eta D ( \Lambda _ { P } x ) . } \end{array} \tag{26.2.36}
	$$
</synced_block>
\\\* \\\* \\\*
一般实超场 $`S`$ 包含四个无自旋实场 $`C`$ , $`M`$ , $`N`$ 和 $`D`$ , 加上一个实 4 -矢场 $`V ^ { \mu }`$ , 总共有八个独立的玻色场分量.
相较而言, 存在两个 4 -分量 Majorana 旋量场 $`\omega`$ 和 $`\lambda`$ , 独立场分量的总个数也是八个.一般而言, 独立玻色场分量的个数和独立费米场分量的个数相等不仅对于本节研究的不约束一般超场是成立的, 对于通过对一般超场附加超对称约束获得的所有超场也是成立的, 下一节讨论的手征超场和其它受约束超场就是这样的例子.
为了在一般情况下看到这点, 假定我们有由 $`N _ { B }`$ 个线性独立实玻色场算符 $`b _ { n } ( x )`$ 和 $`N _ { F }`$ 个线性独立费米场算符 $`f _ { k } ( x )`$ 提供的超对称代数的表示.
我们将假定这些场仅满足不平庸的场方程, 这使得 $`b _ { n }`$ 或 $`f _ { k }`$ 的系数非零的线性组合不可能满足齐次线性场方程.
考察一个实超对称生成元 $`Q ( u )`$ ,定义为
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f818fa4b4cfa2ca5416d4">
	$$
	Q ( u ) \equiv \Big ( \bar { u } Q \Big ) = \Big ( \bar { Q } u \Big ) , \tag{26.2.37}
	$$
</synced_block>
其中 $`u`$ 是某个普通的数值 Majorana 旋量(不是反对易 c -数).
(对于扩充超对称, 取代 $`Q _ { \alpha }`$ , 我们将使用 $`Q _ { r \alpha }`$ 中的任何一个, 例如 $`Q _ { 1 \alpha }`$ .) 为了使 $`b _ { n }`$ 和 $`f _ { k }`$ 构成这个超对称代数的一个表示, 我们必须有
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f814a87e1f6a09ecaf221">
	$$
	\begin{array} { c } { { \displaystyle \left[ Q ( u ) , b _ { n } \right] = \mathrm{i} q _ { n } {} ^ { k } ( \partial ) f _ { k } \ : , } } \\ { { \displaystyle \left\{ Q ( u ) , f _ { k } \right\} = p _ { k } {} ^ { n } ( \partial ) b _ { n } \ : , } } \end{array} \tag{26.2.38-26.2.39}
	$$
</synced_block>
其中 $`q ( \partial )`$ 和 $`p ( \partial )`$ 是一些矩阵微分算符.
取方程(26.2.38)和 $`Q ( u )`$ 的对易子以及方程(26.2.39)和 $`Q ( u )`$ 的反对易子, 这给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f814a87e1f6a09ecaf221">
		$$
		\begin{array} { c } { { \displaystyle \left[ Q ( u ) , b _ { n } \right] = \mathrm{i} q _ { n } {} ^ { k } ( \partial ) f _ { k } \ : , } } \\ { { \displaystyle \left\{ Q ( u ) , f _ { k } \right\} = p _ { k } {} ^ { n } ( \partial ) b _ { n } \ : , } } \end{array} \tag{26.2.38-26.2.39}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f81759500f7ae06fea9c2">
	$$
	\begin{array} { l } { { { \displaystyle \left[ Q ^ { 2 } ( u ) , b _ { n } \right] = \mathrm{i} \Bigl ( q ( \partial ) p ( \partial ) \Bigr ) _ { n } {} ^ { m } b _ { m } } ~ , } } \\ { { { \displaystyle \left[ Q ^ { 2 } ( u ) , f _ { k } \right] = \mathrm{i} \Bigl ( p ( \partial ) q ( \partial ) \Bigr ) _ { k } {} ^ { \ell } f _ { \ell } } . } } \end{array} \tag{26.2.40-26.2.41}
	$$
</synced_block>
反对易关系(25.2.36)或(25.2.38)给出 $`Q ( u )`$ 的平方是 $`Q ^ { 2 } ( u ) = - \mathrm{i} P _ { \mu } \Big ( \bar { u } \gamma ^ { \mu } u \Big )`$ .
这样方阵 $`p ( \partial ) q ( \partial )`$ 和$`q ( \partial ) p ( \partial )`$ 必须非奇异, 原因是, 如果存在非零系数 $`c _ { n } ( \partial )`$ 或 $`d _ { k } ( \partial )`$ 使得 $`\begin{array} { r } { c ^ { n } ( \partial ) ( q ( \partial ) p ( \partial ) ) _ { n }{} ^ { m } = 0 } \end{array}`$ 或者 $`\begin{array} { r } { d ^ { k } ( \partial ) ( p ( \partial ) q ( \partial ) ) _ { k }{} ^ { \ell } = 0 } \end{array}`$ , 那么 $`b _ { n }`$ 或 $`f _ { k }`$ 将满足齐次线性场方程
$$
\Big ( \bar { u } \gamma ^ { \mu } u \Big ) \partial _ { \mu } c ^ { n } ( \partial ) b _ { n } = 0 \qquad \text { or } \qquad \Big ( \bar { u } \gamma ^ { \mu } u \Big ) \partial _ { \mu } d ^ { k } ( \partial ) f _ { k } = 0 ,
$$
而我们前面假定了这些场不满足这样的场方程, 二者矛盾.
为了使 $`q p`$ 不奇异, 我们必须有 $`N _ { F } \geq`$ $`N _ { B }`$ ,而为了使 $`p q`$ 不奇异,我们必须有 $`N _ { B } \geq N _ { F }`$ ,所以我们可以得出 $`N _ { B } = N _ { F }`$ .
另外,方程 $`q`$ 和 $`p`$ 必须都是不奇异的, 所以方程(26.2.38)的复共轭告诉我们 $`f ^ { * } = q ^ { * - 1 } q f`$ , 这使得独立费米场的个数是 $`N _ { F }`$ 而不是 $`2 N _ { F }`$ , 因而等于独立玻色场的个数 $`N _ { B }`$ , 这正是所要证明的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7#34cee2b74b3f814a87e1f6a09ecaf221">
		$$
		\begin{array} { c } { { \displaystyle \left[ Q ( u ) , b _ { n } \right] = \mathrm{i} q _ { n } {} ^ { k } ( \partial ) f _ { k } \ : , } } \\ { { \displaystyle \left\{ Q ( u ) , f _ { k } \right\} = p _ { k } {} ^ { n } ( \partial ) b _ { n } \ : , } } \end{array} \tag{26.2.38-26.2.39}
		$$
	</synced_block_reference>
</callout>
</content>
</page>
