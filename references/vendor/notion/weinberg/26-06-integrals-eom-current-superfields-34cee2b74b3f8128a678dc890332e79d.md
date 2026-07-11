Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d as of 2026-06-30T02:47:32.565Z:
<page url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.6 超空间积分, 场方程和流超场"}
</properties>
<content>
我们用来构建拉格朗日密度的“ $`\mathcal{F}`$ -项”和“ $`D`$ -项可以表示为在超空间坐标 $`\theta _ { \alpha }`$ 上的积分.
最初由Berezin\[4\]给出的费米参量积分规则已经在9.5节推导过了.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- F. A. Berezin, The Method of Second Quantization (Academic Press, New York, 1966)
</callout>
简言之, 由于任何费米参量的平方为零, $`N`$ 个费米参量 $`\xi _ { n }`$ 的任何函数可以表示成
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81ae820ae7b5c90c897f">
	$$
	f ( \xi ) = \biggl ( \prod _ { n = 1 } ^ { N } \xi _ { n } \biggr ) c + \text { terms with fewer than } N \text { factors of } \xi . \tag{26.6.1}
	$$
</synced_block>
而它对 $`\xi`$ 的积分就定义成
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f816bacaaf23af85acc5d">
	$$
	\int \mathrm { d } ^ { N } \xi f ( \xi ) \equiv c . \tag{26.6.2}
	$$
</synced_block>
系数 $`c`$ 本身可以依赖其它未积分的c -数变量, 这些变量与我们要进行积分的 $`\xi`$ 反对易, 在这种情况下, 固定 $`c`$ 的定义就十分重要, 做法和方程(26.6.1)一样, 在积分之前把所有 $`\xi`$ 移至 $`c`$ 的左边.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81ae820ae7b5c90c897f">
		$$
		f ( \xi ) = \biggl ( \prod _ { n = 1 } ^ { N } \xi _ { n } \biggr ) c + \text { terms with fewer than } N \text { factors of } \xi . \tag{26.6.1}
		$$
	</synced_block_reference>
</callout>
在这个定义下, 对费米变量的积分是线性算符.
由于将变量 $`\xi _ { n }`$ 偏移成 $`\xi _ { n } + a _ { n }`$ 对乘积的影响只是那些 $`\xi`$ 因子较少的项, 它不影响积分的值
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81d7a6cad2adf50fc352">
	$$
	\int \mathrm { d } ^ { N } \xi f ( \xi + a ) = \int \mathrm { d } ^ { N } \xi f ( \xi ) , \tag{26.6.3}
	$$
</synced_block>
在这种意义下它类似于对实变量的积分.
另外, 作为方程(26.6.2)的特殊情况, 如果 $`N`$ 个费米参量的多项式的阶数 $`< N`$ , 那么对它的积分为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f816bacaaf23af85acc5d">
		$$
		\int \mathrm { d } ^ { N } \xi f ( \xi ) \equiv c . \tag{26.6.2}
		$$
	</synced_block_reference>
</callout>
在变量代换对积分的影响上, 对费米参量的积分和对玻色参量的积分非常不同: 对于玻色参量 $`x _ { n }`$ , 我们有 $`\mathrm { d } ^ { N } x ^ { \prime } = \mathrm{Det} ( \partial x ^ { \prime } / \partial x ) \mathrm { d } ^ { N } x`$ , 而对于费米参量
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81cab6f4eaf5ac6a3e29">
	$$
	\begin{array} { r } { \mathrm { d } ^ { N } \xi ^ { \prime } = [ \mathrm{Det} ( \partial \xi ^ { \prime } / \partial \xi ) ] ^ { - 1 } \mathrm { d } ^ { N } \xi . } \end{array} \tag{26.6.4}
	$$
</synced_block>
特别地, $`\mathrm { d } \xi`$ 的量纲与 $`\xi`$ 的量纲相反.
根据方程(26.2.10), 一般超场 $`S ( x , \theta )`$ (可能是基本的也可能是复合的)的 $`D`$ -项在相差一个导数的意义下等于 $`- ( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 } / 4 = - ( \theta ^ { \mathrm { T } } \epsilon \theta ) ^ { 2 } / 4`$ 的系数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
四个 $`\theta`$ 中的任何一个都可能是 $`\theta _ { 1 }`$ , 而每种可能性给出相等的贡献, 所以我们可以假定 $`\theta _ { 1 }`$ 是最左边的, 这样就挑出了一个因子4. 这样 $`\theta _ { 2 }`$ 必须是下一个最左边的.
剩下两个 $`\theta`$ 中任何一个都可能是 $`\theta _ { 3 }`$ , 每种可能性给出相同的贡献, 所以我们可以假定, $`\theta _ { 3 }`$ ,是左边第三个并挑出了因子2, 这样 $`\theta _ { 4 }`$ 必须在最右边.
即,
$$
\begin{array} { r } { - \frac { 1 } { 4 } ( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 } = - \frac { 1 } { 4 } \times 4 \times 2 \times \theta _ { 1 } \theta _ { 2 } \theta _ { 3 } \theta _ { 4 } , } \end{array}
$$
所以 $`\theta`$ 的这个函数的系数是 $`- 1 / 2`$ 乘以对 $`\mathrm { d } ^ { 4 } \theta`$ 的积分.
因为这在相差一个导数的意义下是 $`D`$ -项, 我们就有
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f816181ffc2150c485797">
	$$
	\int \mathrm { d } ^ { 4 } x [ S ] _ { D } = - \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta S ( x , \theta ) . \tag{26.6.5}
	$$
</synced_block>
以同样的方式, 利用方程(26.3.11), 我们发现对一般左手征超场 $`\Phi`$ (和前面一样, 可以是基本的也可以是复合的)的 $`\mathcal{F}`$ -项的时空积分可以表示为
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f819eaf3fe05cd968d43f">
		$$
		\begin{array} { l } { { \Phi ( x , \theta ) = \phi ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { L } ( x ) \Big ) + \mathcal{F} ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 + \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \phi ( x ) } } \\ { { \qquad - \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { L } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \phi ( x ) , } } \\ { { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { R } ( x ) \Big ) + \tilde { \mathcal{F} } ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 - \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \tilde { \phi } ( x ) } } \\ { { \qquad + \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { R } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \tilde { \phi } ( x ) , } } \end{array} \tag{26.3.11}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8194bc16c298b00801b5">
	$$
	\int \mathrm { d } ^ { 4 } x [ \Phi ] _ { \mathcal{F} } = \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 2 } \theta _ { L } \Phi ( x , \theta ) . \tag{26.6.6}
	$$
</synced_block>
既然我们现在要对 $`\theta`$ 积分, 引入 $`\delta`$ 函数是方便的, 它像往常一样被如下的条件定义: 对于任意函数 $`f ( \theta )`$ ,
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8106b6a9cda8c406d761">
	$$
	\int \mathrm { d } ^ { 4 } \theta ^ { \prime } \delta ^ { 4 } ( \theta ^ { \prime } - \theta ) f ( \theta ^ { \prime } ) = f ( \theta ) . \tag{26.6.7}
	$$
</synced_block>
根据方程(9.5.40),
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8102b689f89feca3db11">
	$$
	\begin{array} { l } { { \delta ^ { 4 } ( \theta ^ { \prime } - \theta ) = ( \theta _ { 1 } ^ { \prime } - \theta _ { 1 } ) ( \theta _ { 2 } ^ { \prime } - \theta _ { 2 } ) ( \theta _ { 3 } ^ { \prime } - \theta _ { 3 } ) ( \theta _ { 4 } ^ { \prime } - \theta _ { 4 } ) } } \\ { { \mathrm { = } \displaystyle \frac { 1 } { 4 } \Big [ \Big ( \theta _ { L } - \theta _ { L } ^ { \prime } \Big ) ^ { \mathrm { T } } \epsilon \Big ( \theta _ { L } - \theta _ { L } ^ { \prime } \Big ) \Big ] \Big [ \Big ( \theta _ { R } - \theta _ { R } ^ { \prime } \Big ) ^ { \mathrm { T } } \epsilon \Big ( \theta _ { R } - \theta _ { R } ^ { \prime } \Big ) \Big ] } } \end{array} \tag{26.6.8}
	$$
</synced_block>
是满足这个条件的.
将作用量表示成超空间上的积分使得推导超场形式的场方程变得容易.
例如, 考察一组左手征超场 $`\Phi _ { n }`$ 的作用量(左手征超场 $`\Phi _ { n }`$ 的一般可重整理论是它的一个特殊情况):
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f812fad00cec051e26db7">
	$$
	I = \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } + 2 \operatorname{Re} \int \mathrm { d } ^ { 4 } x [ f ( \Phi ) ] _ { \mathcal{F} } , \tag{26.6.9}
	$$
</synced_block>
其中 $`K`$ 是 $`\Phi _ { n }`$ 和 $`\Phi _ { n } ^ { * }`$ 的不带导数的任意函数, $`f`$ 是 $`\Phi _ { n }`$ 的任意函数同时也不含导数.
(写下这种形式的作用量并它表示成分量场的动机将在26.8节进行阐述.) 仅通过要求作用量对 $`\Phi`$ 的任意变分均是驻定, 我们无法导出正确的场方程, 这是因为 $`\Phi _ { n }`$ 是被左手征超场的要求 $`\mathcal{D} _ { R } \boldsymbol { \Phi } _ { n } = 0`$ 约束的.为了确保任意变分不会破坏这个条件, 我们要用到一个小技巧, 这个技巧在第30章推导超空间Feynman规则时也将是有用的.
我们将 $`\Phi _ { n }`$ 写成势超场 $`S _ { n } ( x , \theta )`$
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81a1a333deee6e0775b8">
	$$
	\Phi _ { n } = \mathcal{D} _ { R } ^ { 2 } S _ { n } , \tag{26.6.10}
	$$
</synced_block>
(利用方程(26.A.21))由此可以得出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8158a2fdc1adcd361128">
		$$
		( \overline { { { s _ { 1 } } } } M s _ { 2 } ) ^ { * } = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = 1 , \ \gamma _ { \mu } , \ [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \\ { { - ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = \gamma _ { \mu } \gamma _ { 5 } , \ \gamma _ { 5 } } } \end{array} \right. . \tag{26.A.21}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f818ba45ae983b2e2896e">
	$$
	\Phi _ { n } ^ { * } = - \mathcal{D} _ { L } ^ { 2 } S _ { n } ^ { * } , \tag{26.6.11}
	$$
</synced_block>
其中 $`\mathcal{D} _ { R } ^ { 2 }`$ 和 $`\mathcal{D} _ { L } ^ { 2 }`$ 分别是 $`\left( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } \right) = - ( \bar { \mathcal{D} } _ { R } \mathcal{D} _ { R } )`$ 和 $`\left( \mathcal{D} _ { L } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { L } \right) = \left( \bar { \mathcal{D} } _ { L } \mathcal{D} _ { L } \right)`$ 的简写.
为了看到总能找到满足方程(26.6.10)的解(不一定定域), 注意到, 对于任何左手征超场 $`\Phi _ { n }`$ ,
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81a1a333deee6e0775b8">
		$$
		\Phi _ { n } = \mathcal{D} _ { R } ^ { 2 } S _ { n } , \tag{26.6.10}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f811c8adcc28aeca356b0">
	$$
	\mathcal{D} _ { R } ^ { 2 } \mathcal{D} _ { L } ^ { 2 } \Phi _ { n } = - 16 \Box \Phi _ { n } , \tag{26.6.12}
	$$
</synced_block>
这使得
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8127a48ddb2aae9018ac">
	$$
	- 16 \Box S _ { n } = \mathcal{D} _ { L } ^ { 2 } \Phi _ { n } . \tag{26.6.13}
	$$
</synced_block>
的解满足方程(26.6.10).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81a1a333deee6e0775b8">
		$$
		\Phi _ { n } = \mathcal{D} _ { R } ^ { 2 } S _ { n } , \tag{26.6.10}
		$$
	</synced_block_reference>
</callout>
对于任何 $`S , \mathcal{D} _ { R } ^ { 2 } S`$ 是左手征的, 所以作用量相对 $`S _ { n }`$ 的任意变分必须是驻定的.
利用方程 (26.6.5),写成 $`S _ { n }`$ 和 $`S _ { n } ^ { * }`$ , 作用量可以表示成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f816181ffc2150c485797">
		$$
		\int \mathrm { d } ^ { 4 } x [ S ] _ { D } = - \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta S ( x , \theta ) . \tag{26.6.5}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f819384f5cb82d414e02c">
	$$
	I = - \frac { 1 } { 4 } \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta K ( - { \mathcal{D} } _ { L } ^ { 2 } S ^ { * } , { \mathcal{D} } _ { R } ^ { 2 } S ) + 2 \operatorname{Re} \int \mathrm { d } ^ { 4 } x \left[ f ( { \mathcal{D} } _ { R } ^ { 2 } S ) \right] _ { \mathcal{F} } . \tag{26.6.14}
	$$
</synced_block>
第一项在 $`S _ { n }`$ (而不是 $`S _ { n } ^ { * }`$)的无限小变化
$`\delta S _ { n }`$ 下的变分可以通过超空间中的分部积分简单地计算出来:
$$
\begin{array} { r l } & { \displaystyle - \delta \frac { 1 } { 4 } \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta K ( - \mathcal{D} _ { L } ^ { 2 } S ^ { * } , \mathcal{D} _ { R } ^ { 2 } S ) } \\ & { \displaystyle \quad = - \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta \delta S _ { n } \mathcal{D} _ { R } ^ { 2 } \frac { \delta K ( - \mathcal{D} _ { L } ^ { 2 } S ^ { * } , \mathcal{D} _ { R } ^ { 2 } S ) } { \delta \mathcal{D} _ { R } ^ { 2 } S _ { n } } . } \end{array}
$$
对于超势项中的积分在 $`S _ { n }`$ 的无限小变化 $`\delta S _ { n }`$ 下的变分, 方程(26.3.31)和(26.6.5)使得我们可以将其表示成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f819f9c1adf812ce93c65">
		$$
		\int \mathrm { d } ^ { 4 } x \left[ ( { \mathcal{D} } _ { R } ^ { \mathrm { T } } \epsilon { \mathcal{D} } _ { R } ) h \right] _ { { \mathcal{F} } } = 2 \int \mathrm { d } ^ { 4 } x [ h ] _ { D } . \tag{26.3.31}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f816181ffc2150c485797">
		$$
		\int \mathrm { d } ^ { 4 } x [ S ] _ { D } = - \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta S ( x , \theta ) . \tag{26.6.5}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { { \displaystyle \delta \int \mathrm { d } ^ { 4 } x [ f ( \mathcal{D} _ { R } ^ { 2 } S ) ] _ { \mathcal{F} } = \int \mathrm { d } ^ { 4 } x [ { \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } } | _ { \Phi = \mathcal{D} _ { R } ^ { 2 } S } \mathcal{D} _ { R } ^ { 2 } \delta S _ { n } ] _ { \mathcal{F} } } } \\ { { \displaystyle = \int \mathrm { d } ^ { 4 } x [ { \mathcal{D} _ { R } ^ { 2 } } ( { \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } } | _ { \Phi = \mathcal{D} _ { R } ^ { 2 } S } S _ { n } ) ] _ { \mathcal{F} } } } \\ { { \displaystyle = 2 \int \mathrm { d } ^ { 4 } x [ { \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } } | _ { \Phi = \mathcal{D} _ { R } ^ { 2 } S } S _ { n } ] _ { D } } } \\ { { \displaystyle = - \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta { \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } } \Bigr | _ { \Phi = \mathcal{D} _ { R } ^ { 2 } S } \delta S _ { n } . } } \end{array}
$$
这样, 方程(26.6.14)对 $`S _ { n }`$ 的任意变分是驻定的这一条件就是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f819384f5cb82d414e02c">
		$$
		I = - \frac { 1 } { 4 } \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta K ( - { \mathcal{D} } _ { L } ^ { 2 } S ^ { * } , { \mathcal{D} } _ { R } ^ { 2 } S ) + 2 \operatorname{Re} \int \mathrm { d } ^ { 4 } x \left[ f ( { \mathcal{D} } _ { R } ^ { 2 } S ) \right] _ { \mathcal{F} } . \tag{26.6.14}
		$$
	</synced_block_reference>
</callout>
$$
\mathcal{D} _ { R } ^ { 2 } \frac { \delta K ( - \mathcal{D} _ { L } ^ { 2 } S ^ { * } , \mathcal{D} _ { R } ^ { 2 } S ) } { \delta \mathcal{D} _ { R } ^ { 2 } S _ { n } } = - 4 \left. \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } \right| _ { \Phi = \mathcal{D} _ { R } ^ { 2 } S } ,
$$
或者表示成手征超场
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81be882bf1e8f4ef7578">
	$$
	\mathcal{D} _ { R } ^ { 2 } \frac { \delta K ( \Phi , \Phi ^ { * } ) } { \delta \Phi _ { n } } = - 4 \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } . \tag{26.6.15}
	$$
</synced_block>
复共轭给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f813a87b4ee08015df3e2">
	$$
	\mathcal{D} _ { L } ^ { 2 } \frac { \delta K ( \Phi , \Phi ^ { * } ) } { \delta \Phi _ { n } ^ { * } } = 4 \left( \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } \right) ^ { * } . \tag{26.6.16}
	$$
</synced_block>
可以很容易地验证这些方程的分量给出 $`\Phi _ { n } ^ { * }`$ 和 $`\Phi _ { n }`$ 分量的场方程.
例如, 回忆起 $`\mathcal{D} _ { R } ^ { 2 } ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } ) = - 4`$ ,$`\mathcal{D} _ { R } ^ { 2 } \Phi _ { n } ^ { * }`$ 中与 $`\theta`$ 无关的部分是 $`4 \mathcal{F} _ { n } ^ { * }`$ , 而 $`\partial f ( \Phi ) / \partial \Phi _ { n }`$ 中与 $`\theta`$ 无关的部分是 $`\partial f ( \phi ) / \partial \phi _ { n }`$ , 所以对于 $`K =`$ $`\Phi ^ { * n } \Phi _ { n }`$ , 方程(26.6.15)中与 $`\theta`$ 无关的部分给出关系 $`\mathcal{F} _ { n } ^ { * } = - \partial f ( \phi ) / \partial \phi _ { n }`$ , 这与方程(26.4.6)一致.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81be882bf1e8f4ef7578">
		$$
		\mathcal{D} _ { R } ^ { 2 } \frac { \delta K ( \Phi , \Phi ^ { * } ) } { \delta \Phi _ { n } } = - 4 \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } . \tag{26.6.15}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8133ad40c525f6e4f60e">
		$$
		\mathcal{F} _ { n } = - \left( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right) ^ { * } , \tag{26.4.6}
		$$
	</synced_block_reference>
</callout>
作为如何使用这一形式体系的一个例子, 我们来考察守恒流所属的那个超场.
假定作用量中的超势和Kähler势在如下的整体变换下不变
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8118a930dc99c151653d">
	$$
	\delta \Phi _ { n } = \mathrm{i} \epsilon \mathcal{T} _ { n } {} ^ { m } \Phi _ { m } , \qquad \delta \Phi _ { n } ^ { * } = - \mathrm{i} \epsilon \mathcal{T} ^ { m } {} _ { n } \Phi _ { m } ^ { * } , \tag{26.6.17}
	$$
</synced_block>
其中 $`\epsilon`$ 是实的无限小参量, $`\mathcal{T} _ { n m }`$ 是厄米矩阵, 它可能是相似变换矩阵的部分 Lie 代数.
由于超势只依赖 $`\Phi _ { n }`$ , 它自动在如下的扩充变换下不变
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f812b85ddc07e51acaeec">
	$$
	\delta \Phi _ { n } = \mathrm{i} \epsilon \Lambda \mathcal{T} _ { n } {} ^ { m } \Phi _ { m } , \qquad \delta \Phi _ { n } ^ { * } = - \mathrm{i} \epsilon \Lambda ^ { * } \mathcal{T} ^ { m } {} _ { n } \Phi _ { m } ^ { * } , \tag{26.6.18}
	$$
</synced_block>
其中 $`\Lambda ( x , \theta )`$ 是超场, 为了使 $`\delta \Phi _ { n }`$ 是左手征的, 它必须也取成左手征的.
另一方面, 因为 $`\Lambda \neq \Lambda ^ { * }`$ , 诸如Kähler势这样的其它项在这些变换下一般不是不变的.
因此, 对于一般的场, 作用量的变换必须取如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f812dafe1c36688fba8b5">
	$$
	\delta I = \mathrm{i} \epsilon \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta \left[ \Lambda - \Lambda ^ { \ast } \right] \mathcal{J} , \tag{26.6.19}
	$$
</synced_block>
其中 $`\mathcal{J} \left( x , \theta \right)`$ 是某个实超场, 称为流超场.
但是, 如果场方程是成立的, 那么作用量在超场的任何变分下都是驻定的, 所以积分(26.6.19)对于任何左手征超场 $`\Lambda ( x , \theta )`$ 都必须为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f812dafe1c36688fba8b5">
		$$
		\delta I = \mathrm{i} \epsilon \int \mathrm { d } ^ { 4 } x \int \mathrm { d } ^ { 4 } \theta \left[ \Lambda - \Lambda ^ { \ast } \right] \mathcal{J} , \tag{26.6.19}
		$$
	</synced_block_reference>
</callout>
任何这样的 $`\Lambda`$ 都可以写成 $`\Lambda = \mathcal{D} _ { R } ^ { 2 } S`$ , 所以这意味着流超场必须满足
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f810ea9a9fcb208fa4c8e">
	$$
	\mathcal{D} _ { R } ^ { 2 } \mathcal{J} = \mathcal{D} _ { L } ^ { 2 } \mathcal{J} = 0 . \tag{26.6.20}
	$$
</synced_block>
即, $`\mathcal{J}`$ 是线性超场.
正如我们在 26.3 节看到的, 这意味着它的分量满足
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81b2b76cc235553f4cc2">
	$$
	N ^ { \mathcal{J} } = M ^ { \mathcal{J} } = \partial ^ { \mu } V _ { \mu } {} ^ { \mathcal{J} } = 0 , \qquad \lambda ^ { \mathcal{J} } = - \not\!\partial\, \omega ^ { \mathcal{J} } , \qquad D ^ { \mathcal{J} } = - \Box C ^ { \mathcal{J} } . \tag{26.6.21}
	$$
</synced_block>
这使得我们可以将 $`V`$ -分量 $`V _ { \mu } {} ^ { \mathcal{J} }`$ 等同为与这个对称性相联系的守恒流.
对于特殊的作用量(26.6.9), 流超场采取如下的形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f812fad00cec051e26db7">
		$$
		I = \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } + 2 \operatorname{Re} \int \mathrm { d } ^ { 4 } x [ f ( \Phi ) ] _ { \mathcal{F} } , \tag{26.6.9}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81f1bf71fd8efd86f00b">
	$$
	\mathcal{J} = \frac { \partial K ( \Phi , \Phi ^ { * } ) } { \partial \Phi _ { n } } \mathcal{T} _ { n } {} ^ { m } \Phi _ { m } = \frac { \partial K ( \Phi , \Phi ^ { * } ) } { \partial \Phi _ { n } ^ { * } } \mathcal{T} ^ { m } {} _ { n } \Phi _ { m } ^ { * } . \tag{26.6.22}
	$$
</synced_block>
这两个式子相等就是在变换(26.6.17)下的对称性的结果.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8118a930dc99c151653d">
		$$
		\delta \Phi _ { n } = \mathrm{i} \epsilon \mathcal{T} _ { n } {} ^ { m } \Phi _ { m } , \qquad \delta \Phi _ { n } ^ { * } = - \mathrm{i} \epsilon \mathcal{T} ^ { m } {} _ { n } \Phi _ { m } ^ { * } , \tag{26.6.17}
		$$
	</synced_block_reference>
</callout>
那么, 利用场方程(26.6.15)
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f81be882bf1e8f4ef7578">
		$$
		\mathcal{D} _ { R } ^ { 2 } \frac { \delta K ( \Phi , \Phi ^ { * } ) } { \delta \Phi _ { n } } = - 4 \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } . \tag{26.6.15}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8193b31ef5777dd34baa">
	$$
	\mathcal{D} _ { R } ^ { 2 } \mathcal{J} = \biggl [ \mathcal{D} _ { R } ^ { 2 } \frac { \partial K ( \Phi , \Phi ^ { * } ) } { \partial \Phi _ { n } } \biggr ] \mathcal{T} _ { n } {} ^ { m } \Phi _ { m } = - 4 \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } \mathcal{T} _ { n } {} ^ { m } \Phi _ { m } . \tag{26.6.23}
	$$
</synced_block>
由于假定超势在变换(26.6.17)下不变, 这为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f8118a930dc99c151653d">
		$$
		\delta \Phi _ { n } = \mathrm{i} \epsilon \mathcal{T} _ { n } {} ^ { m } \Phi _ { m } , \qquad \delta \Phi _ { n } ^ { * } = - \mathrm{i} \epsilon \mathcal{T} ^ { m } {} _ { n } \Phi _ { m } ^ { * } , \tag{26.6.17}
		$$
	</synced_block_reference>
</callout>
以同样的方式, 利用 $`\mathcal{J}`$ 的第二个表达式以及场方程(26.6.16), 我们发现 $`\mathcal{D} _ { L } ^ { 2 } \mathcal{J} = 0`$ , 因此证实了守恒条件(26.6.20)
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f813a87b4ee08015df3e2">
		$$
		\mathcal{D} _ { L } ^ { 2 } \frac { \delta K ( \Phi , \Phi ^ { * } ) } { \delta \Phi _ { n } ^ { * } } = 4 \left( \frac { \partial f ( \Phi ) } { \partial \Phi _ { n } } \right) ^ { * } . \tag{26.6.16}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128a678dc890332e79d#34cee2b74b3f810ea9a9fcb208fa4c8e">
		$$
		\mathcal{D} _ { R } ^ { 2 } \mathcal{J} = \mathcal{D} _ { L } ^ { 2 } \mathcal{J} = 0 . \tag{26.6.20}
		$$
	</synced_block_reference>
</callout>
</content>
</page>
