Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862 as of 2026-06-28T04:42:01.925Z:
<page url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f8140bf34e882f5601e5d" title="第 5 章 量子场与反粒子"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"5.4 Dirac 形式体系"}
</properties>
<content>
在齐次Lorentz 群的所有表示中, 有一个表示在物理中扮演了特殊的角色.
正如我们在 1.1 节中看到的, 这个表示被Dirac引入到电子的理论中,\[3\] 但是像通常一样, 数学家在这之前就已经知道它了,\[4\] 这是因为它为任意维旋转群或Lorentz 群(实际上是它们的覆盖群——见2.7 节)的两大类表示中的一类提供了基.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- P. A. M. Dirac, Proc. Roy. Soc. (London) A117, 610 (1928)
	- E. Cartan, Bull. Soc. Math. France 41, 53 (1913)
</callout>
从我们在这里所遵循的观点看, 齐次Lorentz 群的表示决定了按照该群变换的量子场的结构和性质, 所以, 按照它首次出现在数学中的方式, 而不是按照 Dirac 引入的方式, 来描述Dirac形式体系对于我们来说更加自然.
对于齐次 Lorentz 群的一个表示, 我们通常是指一组满足群乘积法则的矩阵 $`D ( \Lambda )`$
$$
{ \cal D } ( \bar { \Lambda } ) { \cal D } ( \Lambda ) = { \cal D } ( \bar { \Lambda } \Lambda ) .
$$
就像处理幺正算符 $`U ( \Lambda )`$ 那样, 我们可以通过考察无限小情形来研究这些矩阵的性质,
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81859381fa447c07dd20">
	$$
	\Lambda ^ { \mu } {} _ { \nu } = \delta ^ { \mu } {} _ { \nu } + \omega ^ { \mu } {} _ { \nu } , \tag{5.4.1}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f814ea1bfd32315d63b4b">
	$$
	\omega _ { \mu \nu } = - \omega _ { \nu \mu } , \tag{5.4.2}
	$$
</synced_block>
这时
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8195948dece02ee2a794">
	$$
	D ( \Lambda ) = 1 + \frac { \mathrm{i} } { 2 } \omega _ { \mu \nu } \mathcal{J} ^ { \mu \nu } \tag{5.4.3}
	$$
</synced_block>
其中 $`\mathcal{J} ^ { \mu \nu } = - \mathcal{J} ^ { \nu \mu }`$ 是一组满足对易关系(2.4.12)的矩阵:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8196a9e7e97652806c6c">
	$$
	\mathrm{i} [ { \mathcal{J} } ^ { \mu \nu } , { \mathcal{J} } ^ { \rho \sigma } ] = \eta ^ { \nu \rho } { \mathcal{J} } ^ { \mu \sigma } - \eta ^ { \mu \rho } { \mathcal{J} } ^ { \nu \sigma } - \eta ^ { \sigma \mu } { \mathcal{J} } ^ { \rho \nu } + \eta ^ { \sigma \nu } { \mathcal{J} } ^ { \rho \mu } . \tag{5.4.4}
	$$
</synced_block>
为了找到这样一组矩阵, 假定我们先构造出了满足如下反对易关系的矩阵 $`\gamma ^ { \mu }`$
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81db9df2f3fa3fe83007">
	$$
	\{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = 2 \eta ^ { \mu \nu } \tag{5.4.5}
	$$
</synced_block>
并试定义
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81759537f78b1ca8ac49">
	$$
	{ \mathcal J } ^ { \mu \nu } = - \frac { \mathrm{i} } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] , \tag{5.4.6}
	$$
</synced_block>
利用方程(5.4.5)不难证明
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81db9df2f3fa3fe83007">
		$$
		\{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = 2 \eta ^ { \mu \nu } \tag{5.4.5}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f819284e1fccf55c0270a">
	$$
	\left[ { \mathcal{J} } ^ { \mu \nu } , \gamma ^ { \rho } \right] = - \mathrm{i} \gamma ^ { \mu } \eta ^ { \nu \rho } + \mathrm{i} \gamma ^ { \nu } \eta ^ { \mu \rho } \tag{5.4.7}
	$$
</synced_block>
由此我们不难看出方程(5.4.6)确实满足期望的对易关系(5.4.4).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81759537f78b1ca8ac49">
		$$
		{ \mathcal J } ^ { \mu \nu } = - \frac { \mathrm{i} } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] , \tag{5.4.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8196a9e7e97652806c6c">
		$$
		\mathrm{i} [ { \mathcal{J} } ^ { \mu \nu } , { \mathcal{J} } ^ { \rho \sigma } ] = \eta ^ { \nu \rho } { \mathcal{J} } ^ { \mu \sigma } - \eta ^ { \mu \rho } { \mathcal{J} } ^ { \nu \sigma } - \eta ^ { \sigma \mu } { \mathcal{J} } ^ { \rho \nu } + \eta ^ { \sigma \nu } { \mathcal{J} } ^ { \rho \mu } . \tag{5.4.4}
		$$
	</synced_block_reference>
</callout>
我们进一步假定矩阵 $`\gamma _ { \mu }`$ 是不可约的; 即, 不存在在所有这些矩阵下不变的真子空间.
否则, 我们可以选择更小的一组场分量, 它像方程(5.4.3)和(5.4.6)中那样变换, 并有一组不可约的 $`\gamma _ { \mu }`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8195948dece02ee2a794">
		$$
		D ( \Lambda ) = 1 + \frac { \mathrm{i} } { 2 } \omega _ { \mu \nu } \mathcal{J} ^ { \mu \nu } \tag{5.4.3}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81759537f78b1ca8ac49">
		$$
		{ \mathcal J } ^ { \mu \nu } = - \frac { \mathrm{i} } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] , \tag{5.4.6}
		$$
	</synced_block_reference>
</callout>
任何一组满足类似方程(5.4.5)(或者它的欧几里得类比, 也就是将 $`\eta _ { \mu \nu }`$ 替换成克罗内克 $`\delta`$ -符号)的关系的矩阵, 被称为 Clifford (克利福德)代数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81db9df2f3fa3fe83007">
		$$
		\{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = 2 \eta ^ { \mu \nu } \tag{5.4.5}
		$$
	</synced_block_reference>
</callout>
齐次 Lorentz 群(或者, 更精确些, 它的覆盖群)的这个特殊表示的数学重要性源于如下事实(见5.6节): Lorentz 群最一般的不可约表示要么是张量, 要么是按照方程(5.4.3)和(5.4.6)变换的旋量, 要么是一个张量和一个旋量的直积.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8195948dece02ee2a794">
		$$
		D ( \Lambda ) = 1 + \frac { \mathrm{i} } { 2 } \omega _ { \mu \nu } \mathcal{J} ^ { \mu \nu } \tag{5.4.3}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81759537f78b1ca8ac49">
		$$
		{ \mathcal J } ^ { \mu \nu } = - \frac { \mathrm{i} } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] , \tag{5.4.6}
		$$
	</synced_block_reference>
</callout>
对易关系(5.4.7)可以被总结为: $`\gamma ^ { \rho }`$ 是矢量, 也就是说方程(5.4.3)满足
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f819284e1fccf55c0270a">
		$$
		\left[ { \mathcal{J} } ^ { \mu \nu } , \gamma ^ { \rho } \right] = - \mathrm{i} \gamma ^ { \mu } \eta ^ { \nu \rho } + \mathrm{i} \gamma ^ { \nu } \eta ^ { \mu \rho } \tag{5.4.7}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8195948dece02ee2a794">
		$$
		D ( \Lambda ) = 1 + \frac { \mathrm{i} } { 2 } \omega _ { \mu \nu } \mathcal{J} ^ { \mu \nu } \tag{5.4.3}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81439005d02fbe504625">
	$$
	D ( \Lambda ) \gamma ^ { \rho } D ^ { - 1 } ( \Lambda ) = \Lambda ^ { \rho } {} _ { \sigma } \gamma ^ { \sigma } . \tag{5.4.8}
	$$
</synced_block>
在同样的意义下, 单位矩阵就是标量
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81aa8f45c49bc6bb8758">
	$$
	D ( \Lambda ) { \bf 1 } D ^ { - 1 } ( \Lambda ) = { \bf 1 } \tag{5.4.9}
	$$
</synced_block>
而方程(5.4.4)表明 $`\mathcal{J} ^ { \rho \sigma }`$ 是反对称张量
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8196a9e7e97652806c6c">
		$$
		\mathrm{i} [ { \mathcal{J} } ^ { \mu \nu } , { \mathcal{J} } ^ { \rho \sigma } ] = \eta ^ { \nu \rho } { \mathcal{J} } ^ { \mu \sigma } - \eta ^ { \mu \rho } { \mathcal{J} } ^ { \nu \sigma } - \eta ^ { \sigma \mu } { \mathcal{J} } ^ { \rho \nu } + \eta ^ { \sigma \nu } { \mathcal{J} } ^ { \rho \mu } . \tag{5.4.4}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8199952cee7011c12dc4">
	$$
	D ( \Lambda ) { \mathcal J } ^ { \rho \sigma } D ^ { - 1 } ( \Lambda ) = \Lambda ^ { \rho } {} _ { \mu } \Lambda ^ { \sigma } {} _ { \nu } { \mathcal J } ^ { \mu \nu } . \tag{5.4.10}
	$$
</synced_block>
用矩阵 $`\gamma ^ { \mu }`$ 可以构造出其它全反对称张量
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f812c8d4ec631ffc7e158">
	$$
	\mathcal{A} ^ { \rho \sigma \tau } \equiv \gamma ^ { [ \rho } \gamma ^ { \sigma } \gamma ^ { \tau ] } , \tag{5.4.11}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8112a248ca22912bf9a9">
	$$
	\mathcal{P} ^ { \rho \sigma \tau \eta } = \gamma ^ { [ \rho } \gamma ^ { \sigma } \gamma ^ { \tau } \gamma ^ { \eta ] } . \tag{5.4.12}
	$$
</synced_block>
这里的中括号是标准记法, 表明我们对括号内指标的所有置换求和, 而对求和中偶置换和奇置换要分别加上正号和负号.
例如, 方程(5.4.11)是下式的简单记法
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f812c8d4ec631ffc7e158">
		$$
		\mathcal{A} ^ { \rho \sigma \tau } \equiv \gamma ^ { [ \rho } \gamma ^ { \sigma } \gamma ^ { \tau ] } , \tag{5.4.11}
		$$
	</synced_block_reference>
</callout>
$$
\mathcal{A} ^ { \rho \sigma \tau } \equiv \gamma ^ { \rho } \gamma ^ { \sigma } \gamma ^ { \tau } - \gamma ^ { \rho } \gamma ^ { \tau } \gamma ^ { \sigma } - \gamma ^ { \sigma } \gamma ^ { \rho } \gamma ^ { \tau }
$$
$$
+ \gamma ^ { \tau } \gamma ^ { \rho } \gamma ^ { \sigma } + \gamma ^ { \sigma } \gamma ^ { \tau } \gamma ^ { \rho } - \gamma ^ { \tau } \gamma ^ { \sigma } \gamma ^ { \rho } .
$$
通过重复使用方程(5.4.5), 我们可以将 $`\gamma`$ 的任何乘积写成 $`\gamma`$ 的反对称乘积乘以度规张量乘积的和,所以对于用Dirac矩阵构造出的任何矩阵集合, 全反对称张量构成了一个完全基.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81db9df2f3fa3fe83007">
		$$
		\{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = 2 \eta ^ { \mu \nu } \tag{5.4.5}
		$$
	</synced_block_reference>
</callout>
这个形式体系自动包含了一个宇称变换, 通常取为
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81ca964dc5d2dfda1488">
	$$
	\beta \equiv \mathrm{i} \gamma ^ { 0 } . \tag{5.4.13}
	$$
</synced_block>
作用在Dirac矩阵上给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f812ba387f99c871ffb11">
	$$
	\beta \gamma ^ { i } \beta ^ { - 1 } = - \gamma ^ { i } , \qquad \beta \gamma ^ { 0 } \beta ^ { - 1 } = + \gamma ^ { 0 } . \tag{5.4.14}
	$$
</synced_block>
(我们这里的指标使 $`\mu`$ 取遍值 $`0 , 1 , 2 , \cdots .`$ 作用在 $`\gamma`$ 矩阵的任意乘积上, 取决于乘积中带空间指标的 $`\gamma`$ 是偶数个还是奇数个, 相同的相似变换仅产生正号或负号.
特别地,
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81aa8b39f7db589ba7bd">
	$$
	\beta \mathcal{J} ^ { i j } \beta ^ { - 1 } = \mathcal{J} ^ { i j } , \tag{5.4.15}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81d5a9d1cddf77393d86">
	$$
	\beta \mathcal{J} ^ { i 0 } \beta ^ { - 1 } = - \mathcal{J} ^ { i 0 } . \tag{5.4.16}
	$$
</synced_block>
迄今为止, 本节中的一切结果适用于任何时空维数以及任意“度规” $`\eta _ { \mu \nu }`$ .
然而, 四维时空有一特征, 即全反对称张量的指标不能超过4个, 所以张量序列 $`1 , \gamma ^ { \rho } , \mathcal{J} ^ { \rho \sigma } , \mathcal{A} ^ { \rho \sigma \tau } , \cdots`$ 终结于张量(5.4.12).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8112a248ca22912bf9a9">
		$$
		\mathcal{P} ^ { \rho \sigma \tau \eta } = \gamma ^ { [ \rho } \gamma ^ { \sigma } \gamma ^ { \tau } \gamma ^ { \eta ] } . \tag{5.4.12}
		$$
	</synced_block_reference>
</callout>
进一步, 这些张量在Lorentz 变换和(或)宇称变换下的变换并不相同, 所以它们是完全线性独立的.\\\* 这些张量的线性独立分量的数目是: 1有1个, $`\gamma ^ { \rho }`$ 有4个, $`\mathcal{J} ^ { \rho \sigma }`$ 有6个, $`\mathcal{A} ^ { \rho \sigma \tau }`$ 有4个,$`\mathcal{P} ^ { \mu \nu \rho \sigma }`$ 有1个, 总共是16个独立分量.
(普遍规则是, 对于 $`d`$ -维中带有 $`n`$ 个指标的全反对称张量, 其独立分量的数目等于二项式系数 $`d ! / n ! ( d - n ) !`$ ) 独立的 $`\nu \times \nu`$ 矩阵最多有 $`\nu ^ { 2 }`$ 个, 所以它们必须至少有 $`{ \sqrt { 1 6 } } = 4`$ 行和4列.
维数最小的Dirac矩阵必须是不可约的; 如果可约, 在这些矩阵下不变的子空间将构成维数更低的表示.
因此我们将 $`\gamma`$ 矩阵取为 $`4 \times 4`$ 矩阵.
(更普遍地, 若时空维数是任意偶数 $`d`$ , 那么可以建立有 $`0 , 1 , \cdots , d`$ 个指标的反对称张量, 它们包含的独立分量个数总共为
$$
\sum _ { n = 0 } ^ { d } \frac { d ! } { n ! ( d - n ) ! } = 2 ^ { d } ,
$$
所以 $`\gamma`$ -矩阵至少必须有 $`2 ^ { d / 2 }`$ 个行和列.
在奇数维空间或时空中, $`n`$ 秩和 $`d - n`$ 秩的全反对称张量通过如下条件线性相关\\\*\\\*
$$
\gamma ^ { [ \mu _ { 1 } } \gamma ^ { \mu _ { 2 } } \cdots \gamma ^ { \mu _ { r } ] } \propto \epsilon ^ { \mu _ { 1 } \mu _ { 2 } \cdots \mu _ { d } } \gamma _ { [ \mu _ { r + 1 } } \gamma _ { \mu _ { r + 2 } } \cdots \gamma _ { \mu _ { d } ] } ,
$$
其中 $`r = 0 , 1 , 2 , \cdots , d - 1`$ , $`\epsilon ^ { \mu _ { 1 } \mu _ { 2 } \cdots \mu _ { d } }`$ 全反对称, 左边在 $`r = 0`$ 时取为单位矩阵.
在这些条件下, 仅有 $`2 ^ { d - 1 }`$ 个独立张量, 这要求 $`\gamma`$ -矩阵的最低维数为 $`2 ^ { ( d - 1 ) / 2 }`$ .)
现在回到 4 维时空, 我们将选择一组显式的 $`4 \times 4`$ 的 $`\gamma`$ -矩阵.
一个非常方便的选择是
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81799efac77079e97d8b">
	$$
	\gamma ^ { 0 } = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { { \bf 1 } } } \\ { { { \bf 1 } } } & { { 0 } } \end{array} \right] \ : , \qquad \gamma = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { \sigma } } \\ { { - \sigma } } & { { 0 } } \end{array} \right] \ : , \tag{5.4.17}
	$$
</synced_block>
其中1是 $`2 \times 2`$ 单位矩阵, 而 $`\sigma`$ 的分量是通常的Pauli矩阵
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8191ab89fd514f6805f8">
	$$
	\sigma _ { 1 } = \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) , \quad \sigma _ { 2 } = \left( \begin{array} { c c } { { 0 } } & { { - \mathrm{i} } } \\ { { \mathrm{i} } } & { { 0 } } \end{array} \right) , \quad \sigma _ { 3 } = \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } \end{array} \right) . \tag{5.4.18}
	$$
</synced_block>
( $`( \sigma _ { i }`$ 就是三维中的 $`2 \times 2`$ 的 $`\gamma`$ -矩阵.) 可以证明,\[5\] 任何其它一组不可约的 $`\gamma`$ -矩阵与此只相差一个相似变换.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- 可参看 J. M. Jauch and F. Rohrlich, The Theory of Photons and Electrons (Addison-Wesley, Cambridge, MA 1955): Appendix A2; H. Georgi, Lie Algebras in Particle Physics (BenjaminCummings, Reading, MA, 1982): pp. 15, 198. 原始文献是 I. Schur, Sitz. Pr
</callout>
从方程(5.4.17)中, 我们可以简单地计算出 Lorentz 群生成元(5.4.6):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81799efac77079e97d8b">
		$$
		\gamma ^ { 0 } = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { { \bf 1 } } } \\ { { { \bf 1 } } } & { { 0 } } \end{array} \right] \ : , \qquad \gamma = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { \sigma } } \\ { { - \sigma } } & { { 0 } } \end{array} \right] \ : , \tag{5.4.17}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81759537f78b1ca8ac49">
		$$
		{ \mathcal J } ^ { \mu \nu } = - \frac { \mathrm{i} } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] , \tag{5.4.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81b18b98ca1d454a2a8b">
	$$
	\mathcal{J} ^ { i j } = \frac { 1 } { 2 } \epsilon _ { i j k } \left[ \begin{array} { c c } { \sigma _ { k } } & { 0 } \\ { 0 } & { \sigma _ { k } } \end{array} \right] \tag{5.4.19}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8115a72fc4e2fe64bae6">
	$$
	\mathcal{J} ^ { i 0 } = + \frac { \mathrm{i} } { 2 } \left[ \begin{array} { c c } { \sigma _ { i } } & { 0 } \\ { 0 } & { - \sigma _ { i } } \end{array} \right] . \tag{5.4.20}
	$$
</synced_block>
(其中, $`\epsilon _ { i j k }`$ 是三维中的全反对称张量, $`\epsilon _ { 1 2 3 } \equiv + 1 .`$ .) 我们注意到它们是分块对角的, 所以Dirac 矩阵固有正时Lorentz 群提供了一个可约表示, 即两个不可约表示的直和, 这两个表示分别有 $`{ \mathcal{J} } ^ { i j } =`$ $`\pm \mathrm{i} \epsilon _ { i j k } \mathcal{J} ^ { k 0 }`$ .
将全反对称张量(5.4.11)和(5.4.12)写成一种更简单的形式将更加方便.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f812c8d4ec631ffc7e158">
		$$
		\mathcal{A} ^ { \rho \sigma \tau } \equiv \gamma ^ { [ \rho } \gamma ^ { \sigma } \gamma ^ { \tau ] } , \tag{5.4.11}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8112a248ca22912bf9a9">
		$$
		\mathcal{P} ^ { \rho \sigma \tau \eta } = \gamma ^ { [ \rho } \gamma ^ { \sigma } \gamma ^ { \tau } \gamma ^ { \eta ] } . \tag{5.4.12}
		$$
	</synced_block_reference>
</callout>
矩阵(5.4.12)是全反对称矩阵, 因而正比于赝张量 $`\epsilon ^ { \rho \sigma \tau \eta }`$ , 这个赝张量被定义为一个全反对称量, 有 $`\epsilon ^ { 0 1 2 3 } = + 1`$ .令 $`\rho , \sigma , \tau , \eta`$ 分别等于 $`0 , 1 , 2 , 3`$ , 我们看到
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8112a248ca22912bf9a9">
		$$
		\mathcal{P} ^ { \rho \sigma \tau \eta } = \gamma ^ { [ \rho } \gamma ^ { \sigma } \gamma ^ { \tau } \gamma ^ { \eta ] } . \tag{5.4.12}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8198a24ee0ad2079417b">
	$$
	\mathcal{P} ^ { \rho \sigma \tau \eta } = 4 ! \mathrm{i} \epsilon ^ { \rho \sigma \tau \eta } \gamma _ { 5 } , \tag{5.4.21}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8193a6eedd2284a2ec4c">
	$$
	\gamma _ { 5 } \equiv - \mathrm{i} \gamma ^ { 0 } \gamma ^ { 1 } \gamma ^ { 2 } \gamma ^ { 3 } . \tag{5.4.22}
	$$
</synced_block>
矩阵 $`\gamma _ { 5 }`$ 是赝标量, 也就是说
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f817ebb95cbd89b13105b">
	$$
	\begin{array} { r } { \left[ \mathcal{J} ^ { \rho \sigma } , \gamma _ { 5 } \right] = 0 , } \\ { \beta \gamma _ { 5 } \beta ^ { - 1 } = - \gamma _ { 5 } . } \end{array} \tag{5.4.23-5.4.24}
	$$
</synced_block>
类似地, $`\mathcal{A} ^ { \rho \sigma \tau }`$ 必须正比于 $`\epsilon ^ { \rho \sigma \tau \eta }`$ 与某个矩阵 $`\mathcal{A} _ { \eta }`$ 的收缩, 令 $`\rho , \sigma , \tau`$ 依次等于 $`0 , 1 , 2`$ 或 $`0 , 1 , 3`$ 或 $`0 , 2 , 3`$ 或 1, 2, 3, 我们发现
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f814c8bf9cdc73d743be4">
	$$
	\mathcal{A} ^ { \rho \sigma \tau } = 3 ! \mathrm{i} \epsilon ^ { \rho \sigma \tau \eta } \gamma _ { 5 } \gamma _ { \eta } . \tag{5.4.25}
	$$
</synced_block>
因此, 16 个独立的 $`4 \times 4`$ 矩阵可以取为标量1, 矢量 $`\gamma ^ { \rho }`$ , 反对称张量 $`\mathcal{J} ^ { \rho \sigma }`$ , “轴”矢量 $`\gamma _ { 5 } \gamma _ { \eta }`$ 以及赝标量 $`\gamma _ { 5 }`$ .
很容易看到矩阵 $`\gamma _ { 5 }`$ 的平方等于1
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81879704ce04cf23afd4">
	$$
	{ \gamma } _ { 5 } { \bf \Psi } ^ { 2 } = { \bf 1 } \tag{5.4.26}
	$$
</synced_block>
并与所有 $`\gamma ^ { \mu }`$ 反对易
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81a08edec3cedcdf2c44">
	$$
	\left\{ \gamma _ { 5 } , \gamma ^ { \mu } \right\} = 0 . \tag{5.4.27}
	$$
</synced_block>
记成 $`\gamma _ { 5 }`$ 是非常恰当的, 因为反对易关系(5.4.26)和(5.4.27), 再加上方程(5.4.5), 它们合在一起表明了 $`\gamma ^ { 0 } , \gamma ^ { 1 } , \gamma ^ { 2 } , \gamma ^ { 3 } , \gamma _ { 5 }`$ 给出了五维时空中的 Clifford 代数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81879704ce04cf23afd4">
		$$
		{ \gamma } _ { 5 } { \bf \Psi } ^ { 2 } = { \bf 1 } \tag{5.4.26}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81a08edec3cedcdf2c44">
		$$
		\left\{ \gamma _ { 5 } , \gamma ^ { \mu } \right\} = 0 . \tag{5.4.27}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81db9df2f3fa3fe83007">
		$$
		\{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = 2 \eta ^ { \mu \nu } \tag{5.4.5}
		$$
	</synced_block_reference>
</callout>
对于 $`\gamma`$ -矩阵的特定 $`4 \times 4`$ 表示(5.4.17), 矩阵 $`\gamma _ { 5 }`$ 是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81799efac77079e97d8b">
		$$
		\gamma ^ { 0 } = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { { \bf 1 } } } \\ { { { \bf 1 } } } & { { 0 } } \end{array} \right] \ : , \qquad \gamma = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { \sigma } } \\ { { - \sigma } } & { { 0 } } \end{array} \right] \ : , \tag{5.4.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8164856dff058e53cfc9">
	$$
	\gamma _ { 5 } = \left[ \begin{array} { c c } { { { \bf 1 } } } & { { 0 } } \\ { { 0 } } & { { - { \bf 1 } } } \end{array} \right] . \tag{5.4.28}
	$$
</synced_block>
这个表示是方便的, 因为它将 $`\mathcal{J} ^ { \rho \sigma }`$ 和 $`\gamma _ { 5 }`$ 简化成了分块对角形式.
我们将会看到, 这使它在 $`v`$ $`c`$ 的极端相对论极限下处理粒子时非常有用.
(但这不是1.1节中Dirac最初引入的表示, 这是因为 Dirac 关注的是原子中的电子, 那里 $`v \ll c ,`$ , 而在这种情况下, 将 $`\gamma ^ { 0 }`$ 而非 $`\gamma _ { 5 }`$ 取成对角形式将更加方便.)
我们这里构造的齐次Lorentz 群的表示不是幺正的, 这是因为生成元 $`\mathcal{J} ^ { \rho \sigma }`$ 无法全部表示成厄米矩阵.
特别地, 在表示(5.4.17)中, $`\mathcal{J} ^ { i j }`$ 是厄米的, 但 $`\mathcal{J} ^ { i 0 }`$ 是反厄米的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81799efac77079e97d8b">
		$$
		\gamma ^ { 0 } = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { { \bf 1 } } } \\ { { { \bf 1 } } } & { { 0 } } \end{array} \right] \ : , \qquad \gamma = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { \sigma } } \\ { { - \sigma } } & { { 0 } } \end{array} \right] \ : , \tag{5.4.17}
		$$
	</synced_block_reference>
</callout>
通过引入方程(5.4.13)中的矩阵 $`\beta \equiv i \gamma ^ { 0 }`$ , 这种实条件可以非常方便地写成明显 Lorentz 不变的形式, $`\beta`$ 在表示(5.4.17)中的形式为
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81ca964dc5d2dfda1488">
		$$
		\beta \equiv \mathrm{i} \gamma ^ { 0 } . \tag{5.4.13}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81799efac77079e97d8b">
		$$
		\gamma ^ { 0 } = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { { \bf 1 } } } \\ { { { \bf 1 } } } & { { 0 } } \end{array} \right] \ : , \qquad \gamma = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { \sigma } } \\ { { - \sigma } } & { { 0 } } \end{array} \right] \ : , \tag{5.4.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f816ea695d9df3b505fe7">
	$$
	\beta = \left[ \begin{array} { l l } { 0 } & { \mathbf { 1 } } \\ { \mathbf { 1 } } & { 0 } \end{array} \right] . \tag{5.4.29}
	$$
</synced_block>
观察方程(5.4.17), 它给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81799efac77079e97d8b">
		$$
		\gamma ^ { 0 } = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { { \bf 1 } } } \\ { { { \bf 1 } } } & { { 0 } } \end{array} \right] \ : , \qquad \gamma = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { \sigma } } \\ { { - \sigma } } & { { 0 } } \end{array} \right] \ : , \tag{5.4.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81ffb793e75175349b9b">
	$$
	\beta \gamma ^ { \mu \dagger } \beta = - \gamma ^ { \mu } \tag{5.4.30}
	$$
</synced_block>
从而有
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81cc9191d12a1d54791b">
	$$
	\beta \mathcal{J} ^ { \rho \sigma \dagger } \beta = \mathcal{J} ^ { \rho \sigma } . \tag{5.4.31}
	$$
</synced_block>
因此, 尽管不幺正, 但矩阵 $`D ( \Lambda )`$ 满足赝幺正关系
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81da8fffe69fb896bea6">
	$$
	\beta D ( \Lambda ) ^ { \dagger } \beta = D ( \Lambda ) ^ { - 1 } . \tag{5.4.32}
	$$
</synced_block>
另外, $`\gamma _ { 5 }`$ 厄米且与 $`\beta`$ 反对易, 所以
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81f4acd7c9e14d179fd2">
	$$
	\beta \gamma _ { 5 } ^ { \dagger } \beta = - \gamma _ { 5 } \tag{5.4.33}
	$$
</synced_block>
由此得出
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81f085e9ed66dfdb8316">
	$$
	\beta ( \gamma _ { 5 } \gamma _ { \mu } ) ^ { \dagger } \beta = - \gamma _ { 5 } \gamma _ { \mu } . \tag{5.4.34}
	$$
</synced_block>
Dirac 矩阵及其相关矩阵还有重要的对称性质.
观察方程(5.4.17)和(5.4.18), 可以看出 $`\gamma _ { \mu }`$ 对 $`\mu =`$ $`0 , 2`$ 对称, 对 $`\mu = 1 , 3`$ 反对称, 所以
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81799efac77079e97d8b">
		$$
		\gamma ^ { 0 } = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { { \bf 1 } } } \\ { { { \bf 1 } } } & { { 0 } } \end{array} \right] \ : , \qquad \gamma = - \mathrm{i} \left[ \begin{array} { c c } { { 0 } } & { { \sigma } } \\ { { - \sigma } } & { { 0 } } \end{array} \right] \ : , \tag{5.4.17}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f8191ab89fd514f6805f8">
		$$
		\sigma _ { 1 } = \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) , \quad \sigma _ { 2 } = \left( \begin{array} { c c } { { 0 } } & { { - \mathrm{i} } } \\ { { \mathrm{i} } } & { { 0 } } \end{array} \right) , \quad \sigma _ { 3 } = \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } \end{array} \right) . \tag{5.4.18}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81019db3c1ef2d9685ae">
	$$
	\gamma _ { \mu } ^ { \mathrm { T } } = - \mathcal{C} \gamma _ { \mu } \mathcal{C} ^ { - 1 } , \tag{5.4.35}
	$$
</synced_block>
其中 $`_ \mathrm { T }`$ 表示转置, 并且
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f810caf78cdae0d031ba4">
	$$
	\mathcal{C} \equiv \gamma _ { 2 } \beta = - \mathrm{i} \left[ \begin{array} { c c } { { \sigma _ { 2 } } } & { { 0 } } \\ { { 0 } } & { { - \sigma _ { 2 } } } \end{array} \right] . \tag{5.4.36}
	$$
</synced_block>
由此立即得出
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81fe97e4c09e63dcc756">
	$$
	{ \mathcal J } _ { \mu \nu } ^ { \mathrm { T } } = - { \mathcal C } { \mathcal J } _ { \mu \nu } { \mathcal C } ^ { - 1 } , \tag{5.4.37}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f819d9a59dc4d41d39be7">
	$$
	\gamma _ { 5 } ^ { \mathrm { T } } = + \mathcal{C} \gamma _ { 5 } \mathcal{C} ^ { - 1 } , \tag{5.4.38}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81f3a5b9dc0526d1aa92">
	$$
	\left( \gamma _ { 5 } \gamma _ { \mu } \right) ^ { \mathrm { T } } = + \mathcal{C} \gamma _ { 5 } \gamma _ { \mu } \mathcal{C} ^ { - 1 } . \tag{5.4.39}
	$$
</synced_block>
我们在下一节考察不同流的荷共轭性质时, 这些符号将会体现出它们的重要性.
当然, 我们可以结合转置和共轭以获得Dirac矩阵及相关矩阵的复共轭:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81fba0ced0934490b1fa">
	$$
	\gamma _ { \mu } ^ { \ast } = \beta \mathcal{C} \gamma _ { \mu } \mathcal{C} ^ { - 1 } \beta , \tag{5.4.40}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81638615d3560c85e373">
	$$
	\mathcal{J} _ { \mu \nu } ^ { * } = - \beta \mathcal{C} \mathcal{J} _ { \mu \nu } \mathcal{C} ^ { - 1 } \beta , \tag{5.4.41}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f81c78544ee2a27235025">
	$$
	\gamma _ { 5 } ^ { \ast } = - \beta \mathcal{C} \gamma _ { 5 } \mathcal{C} ^ { - 1 } \beta , \tag{5.4.42}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8115a5a1fac623c31862#34cee2b74b3f817eba52f1d8e3a61cfb">
	$$
	( \gamma _ { 5 } \gamma _ { \mu } ) ^ { * } = - \beta \mathcal{C} \gamma _ { 5 } \gamma _ { \mu } \mathcal{C} ^ { - 1 } \beta . \tag{5.4.43}
	$$
</synced_block>
</content>
</page>
