Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e as of 2026-06-30T02:15:35.595Z:
<page url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.1 场超多重态的直接构造"}
</properties>
<content>
为了阐明场多重态的直接构造, 对于我们将要考察的场, 它湮灭掉的粒子属于25.5节讨论过的任意质量的最简超多重态: 两个无自旋的粒子和一个自旋 $`1 / 2`$ 的粒子.
我们在方程(25.5.15)中看到, 湮灭掉零自旋单粒子态 $`| 0 , 0 \rangle`$ 的是 $`\mathcal{Q} _ { a }`$ 而不是 $`{ \mathcal{Q} } _ { a } ^ { * }`$ , 所以我们预期从真空(它假设成被所有超对称生成元湮灭)中创造这一粒子的标量场 $`\phi ( x )`$ 与 $`\mathcal{Q} _ { a }`$ 对易而不是 $`{ \mathcal{Q} } _ { a } ^ { * }`$ .
即,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ba131c81d19a3c585">
	$$
	[ { \mathcal{Q} } _ { a } , \phi ( x ) ] = 0 , \tag{26.1.1}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81b79dffe2d5208cabe2">
	$$
	- \mathrm{i} e _ { a }{}^{ b } [ \mathcal{Q} _ { b } ^ { \ast } , \phi ( x ) ] \equiv \zeta _ { a } ( x ) \neq 0 . \tag{26.1.2}
	$$
</synced_block>
在这里引入 $`2 \times 2`$ 的反对称矩阵 $`e _ { a b }`$ (其中 $`e _ { 1 / 2 , - 1 / 2 } \equiv + 1 )`$ 是因为, 在齐次 Lorentz 群下按照 $`( 1 / 2 , 0 )`$ 表示变换的是 $`e _ { a }{}^{ b } \mathcal{Q} _ { b } ^ { * }`$ .
由此得出 $`\zeta _ { a } ( x )`$ 这个二分量旋量场也属于齐次 Lorentz 群的 $`( 1 / 2 , 0 )`$ 表示.
\\\*
从方程(26.1.1)—(26.1.2)和反对易关系(25.2.31)中, 我们发现
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ba131c81d19a3c585">
		$$
		[ { \mathcal{Q} } _ { a } , \phi ( x ) ] = 0 , \tag{26.1.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81b79dffe2d5208cabe2">
		$$
		- \mathrm{i} e _ { a }{}^{ b } [ \mathcal{Q} _ { b } ^ { \ast } , \phi ( x ) ] \equiv \zeta _ { a } ( x ) \neq 0 . \tag{26.1.2}
		$$
	</synced_block_reference>
</callout>
$$
\{ \mathcal{Q} _ { b } , \zeta _ { a } \} = - \mathrm{i} e _ { a }{}^{ c } [ \{ \mathcal{Q} _ { b } , \mathcal{Q} _ { c } ^ { * } \} , \phi ( x ) ] = 2 \mathrm{i} ( \sigma ^ { \mu } e ) _ { b a } [ P _ { \mu } , \phi ] ,
$$
因而
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f8157b79ae12925d65376">
	$$
	\{ { \mathcal Q } _ { b } , \zeta _ { a } ( x ) \} = - 2 ( \sigma ^ { \mu } e ) _ { b a } \partial _ { \mu } \phi ( x ) . \tag{26.1.3}
	$$
</synced_block>
另一方面, 方程(26.1.2)和反对易关系(25.2.32)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81b79dffe2d5208cabe2">
		$$
		- \mathrm{i} e _ { a }{}^{ b } [ \mathcal{Q} _ { b } ^ { \ast } , \phi ( x ) ] \equiv \zeta _ { a } ( x ) \neq 0 . \tag{26.1.2}
		$$
	</synced_block_reference>
</callout>
$$
- \mathrm{i} e _ { a }{}^{ c } \{ \mathcal Q _ { b } ^ { * } , \zeta _ { c } \} = \{ \mathcal Q _ { b } ^ { * } , [ \mathcal Q _ { a } ^ { * } , \phi ] \} = - \{ \mathcal Q _ { a } ^ { * } , [ \mathcal Q _ { b } ^ { * } , \phi ] \} = \mathrm{i} e _ { b }{}^{ c } \{ \mathcal Q _ { a } ^ { * } , \zeta _ { c } \} ,
$$
所以 $`e _ { a }{}^{ c } \{ \mathcal{Q} _ { b } ^ { * } , \zeta _ { c } \}`$ 是反对称的, 因而正比于 $`2 \times 2`$ 反对称矩阵 $`e _ { a b }`$ :
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f812d92e2e133934eaf5b">
	$$
	\mathrm{i} \{ \mathcal{Q} _ { b } ^ { \ast } , \zeta _ { a } ( x ) \} = 2 \delta _ { a b } { \mathcal F } ( x ) . \tag{26.1.4}
	$$
</synced_block>
Lorentz不变性要求系数 $`{ \mathcal{F} } ( x )`$ 是个标量场.
我们现在必须更进一步, 计算超对称生成元与 $`{ \mathcal{F} } ( x )`$ 的对易子.
利用方程(26.1.4), (26.1.2)和(25.2.32), 我们有
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f812d92e2e133934eaf5b">
		$$
		\mathrm{i} \{ \mathcal{Q} _ { b } ^ { \ast } , \zeta _ { a } ( x ) \} = 2 \delta _ { a b } { \mathcal F } ( x ) . \tag{26.1.4}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81b79dffe2d5208cabe2">
		$$
		- \mathrm{i} e _ { a }{}^{ b } [ \mathcal{Q} _ { b } ^ { \ast } , \phi ( x ) ] \equiv \zeta _ { a } ( x ) \neq 0 . \tag{26.1.2}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r } { \delta _ { a b } \left[ \mathcal Q _ { c } ^ { * } , \mathcal{F} \right] = \frac { 1 } { 2 } \mathrm{i} [ \mathcal Q _ { c } ^ { * } , \{ \mathcal Q _ { b } ^ { * } , \zeta _ { a } \} ] = \frac { 1 } { 2 } \mathrm{i} [ \{ \mathcal Q _ { c } ^ { * } , \zeta _ { a } \} , \mathcal Q _ { b } ^ { * } ] = - \delta _ { a c } [ \mathcal Q _ { b } ^ { * } , \mathcal{F} ] . } \end{array}
$$
取 $`a = b \neq c`$ , 我们发现这个对易子为零:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81448315cf2f8ce4253f">
	$$
	[ { \mathcal Q } _ { c } ^ { * } , \mathcal F ( x ) ] = 0 . \tag{26.1.5}
	$$
</synced_block>
最后, 利用方程(26.1.4), (25.2.31)和(26.1.3), 我们有
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f812d92e2e133934eaf5b">
		$$
		\mathrm{i} \{ \mathcal{Q} _ { b } ^ { \ast } , \zeta _ { a } ( x ) \} = 2 \delta _ { a b } { \mathcal F } ( x ) . \tag{26.1.4}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f8157b79ae12925d65376">
		$$
		\{ { \mathcal Q } _ { b } , \zeta _ { a } ( x ) \} = - 2 ( \sigma ^ { \mu } e ) _ { b a } \partial _ { \mu } \phi ( x ) . \tag{26.1.3}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { { \displaystyle \delta _ { a b } \left[ \mathcal{Q} _ { c } , \mathcal{F} \right] = \frac { 1 } { 2 } \mathrm{i} [ \mathcal{Q} _ { c } , \{ \mathcal{Q} _ { b } ^ { * } , \zeta _ { a } \} ] = \frac { 1 } { 2 } \mathrm{i} [ \{ \mathcal{Q} _ { c } , \mathcal{Q} _ { b } ^ { * } \} , \zeta _ { a } ] - \frac { 1 } { 2 } \mathrm{i} [ \mathcal{Q} _ { b } ^ { * } , \{ \mathcal{Q} _ { c } , \zeta _ { a } \} ] } } \\ { ~ } \\ { { \displaystyle ~ = - \sigma _ { c b } ^ { \mu } \partial _ { \mu } \zeta _ { a } + \mathrm{i} ( \sigma ^ { \mu } e ) _ { c a } \left[ \mathcal{Q} _ { b } ^ { * } , \partial _ { \mu } \phi \right] } } \\ { ~ } \\ { { \displaystyle ~ = - \sigma _ { c b } ^ { \mu } \partial _ { \mu } \zeta _ { a } + e _ { b }{}^{ d } \left( \sigma ^ { \mu } e \right) _ { c a } \partial _ { \mu } \zeta _ { d } } . } \end{array}
$$
与 $`\delta _ { a b }`$ 收缩, 这变成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81ea8b76c14b3ca9a9f7">
	$$
	\left[ \mathcal{Q} _ { c } , \mathcal{F} ( x ) \right] = - \sigma _ { c a } ^ { \mu } \partial _ { \mu } \zeta _ { a } ( x ) . \tag{26.1.6}
	$$
</synced_block>
方程(26.1.1)—(26.1.6)表明场 $`\phi ( x )`$ , $`\zeta _ { a } ( x )`$ 和 $`\mathcal{F} ( x )`$ 构成了超对称代数的一个完整表示.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ba131c81d19a3c585">
		$$
		[ { \mathcal{Q} } _ { a } , \phi ( x ) ] = 0 , \tag{26.1.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81ea8b76c14b3ca9a9f7">
		$$
		\left[ \mathcal{Q} _ { c } , \mathcal{F} ( x ) \right] = - \sigma _ { c a } ^ { \mu } \partial _ { \mu } \zeta _ { a } ( x ) . \tag{26.1.6}
		$$
	</synced_block_reference>
</callout>
这些场不是厄米的, 所以它们的复共轭构成了另一个超多重态:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f8198bf64c9e12f1e5630">
	$$
		\begin{array} { l }
{ { { [ } \mathcal Q _ { a } ^ { * } , \phi ^ { * } ( x ) { ] } = 0 , } } \\
{ { \displaystyle - { \mathrm{i} e _ { a }{}^{ b } [ \mathcal Q _ { b } , \phi ^ { * } ( x ) ] } = \zeta _ { a } ^ { * } ( x ) , } } \\
{ { \displaystyle \{ \mathcal Q _ { b } ^ { * } , \zeta _ { a } ^ { * } ( x ) \} = 2 ( e \sigma ^ { \mu } ) _ { a b } \partial _ { \mu } \phi ^ { * } ( x ) . } } \\
{ { \displaystyle - { \mathrm{i} \{ \mathcal Q _ { b } , \zeta _ { a } ^ { * } ( x ) \} = 2 \delta _ { a b } \mathcal{F} ^ { * } ( x ) } , } } \\
{ { \displaystyle { [ } \mathcal Q _ { c } , \mathcal{F} ^ { * } ( x ) { ] } = 0 , } } \\
{ { \displaystyle { [ } \mathcal Q _ { c } ^ { * } , \mathcal{F} ^ { * } ( x ) { ] } = \sigma _ { a c } ^ { \mu } \partial _ { \mu } \zeta _ { a } ^ { * } ( x ) . } }
\end{array} \tag{26.1.8-26.1.11}
	$$
</synced_block>
我们可以将这些对易关系和反对易关系表示成在一个超对称变换下的变换规则, 这个超对称变换使得任何玻色或费米场算符 $`{ \mathcal{O} } ( x )`$ 偏移一个无限小量
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81438de4d49aa9f2898d">
	$$
	\delta \mathcal{O} ( x ) \equiv \left[ \epsilon ^ { a * } \mathcal{Q} _ { a } + \epsilon ^ { a } \mathcal{Q} _ { a } ^ { * } , \mathcal{O} ( x ) \right] , \tag{26.1.13}
	$$
</synced_block>
其中 $`\epsilon _ { a }`$ 是无限小的费米 c -数旋量.
(因为 $`\epsilon _ { a }`$ 和 $`\boldsymbol { \epsilon } _ { a } ^ { * }`$ 与 $`\mathcal{Q} _ { a }`$ 和 $`{ \mathcal{Q} } _ { a } ^ { * }`$ 反对易, $`\epsilon ^ { a * } \mathcal{Q} _ { a } + \epsilon ^ { a } \mathcal{Q} _ { a } ^ { * }`$ 是反厄米的, 所
以方程(26.1.13)给出 $`( \delta \mathcal{Q} ) ^ { * } = \delta \mathcal{Q} ^ { * }`$ .) 对易和反对易规则(26.1.1)—(26.1.6)等价于变换规则
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81438de4d49aa9f2898d">
		$$
		\delta \mathcal{O} ( x ) \equiv \left[ \epsilon ^ { a * } \mathcal{Q} _ { a } + \epsilon ^ { a } \mathcal{Q} _ { a } ^ { * } , \mathcal{O} ( x ) \right] , \tag{26.1.13}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ba131c81d19a3c585">
		$$
		[ { \mathcal{Q} } _ { a } , \phi ( x ) ] = 0 , \tag{26.1.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81ea8b76c14b3ca9a9f7">
		$$
		\left[ \mathcal{Q} _ { c } , \mathcal{F} ( x ) \right] = - \sigma _ { c a } ^ { \mu } \partial _ { \mu } \zeta _ { a } ( x ) . \tag{26.1.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81b7b244c914fce91024">
	$$
	\begin{array} { l } { { \displaystyle \delta \phi ( x ) = - \mathrm{i} \epsilon ^ { a } e _ { a }{}^{ b } \zeta _ { b } ( x ) , } } \\ { { \displaystyle \delta \zeta _ { a } ( x ) = - 2 \epsilon ^ { b \ast } ( \sigma ^ { \mu } e ) _ { b a } \partial _ { \mu } \phi ( x ) - 2 \mathrm{i} \epsilon _ { a } \mathcal{F} ( x ) , } } \\ { { \displaystyle \delta \mathcal{F} ( x ) = - \epsilon ^ { b \ast } \sigma _ { b a } ^ { \mu } \partial _ { \mu } \zeta _ { a } ( x ) . } } \end{array} \tag{26.1.14-26.1.16}
	$$
</synced_block>
通过引入一个无限小的 Majorana\\\*\\\* 4-分量旋量变换参量
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f819e8a4cdc2022392f0e">
	$$
	\alpha \equiv - \mathrm{i} \left( { \epsilon } _ { a } \right) , \tag{26.1.17}
	$$
</synced_block>
这可以写成 Dirac 4 -分量的形式, 使得方程(26.1.13)变成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81438de4d49aa9f2898d">
		$$
		\delta \mathcal{O} ( x ) \equiv \left[ \epsilon ^ { a * } \mathcal{Q} _ { a } + \epsilon ^ { a } \mathcal{Q} _ { a } ^ { * } , \mathcal{O} ( x ) \right] , \tag{26.1.13}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f8144bfa7d9c89936ea83">
	$$
	\mathrm{i} \delta { \mathcal O } ( x ) \equiv \left[ \bar { \alpha } Q , { \mathcal O } ( x ) \right] . \tag{26.1.18}
	$$
</synced_block>
通过引入一组实玻色场 $`A , B , F`$ 和 $`G`$ , 以及一个 4 -分量 Majorana 旋量 $`\psi`$ , 变换规则(26.1.14)—(26.1.16)和它们的复共轭可以写成一个方便的协变形式, 这些实玻色场的定义是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81b7b244c914fce91024">
		$$
		\begin{array} { l } { { \displaystyle \delta \phi ( x ) = - \mathrm{i} \epsilon ^ { a } e _ { a }{}^{ b } \zeta _ { b } ( x ) , } } \\ { { \displaystyle \delta \zeta _ { a } ( x ) = - 2 \epsilon ^ { b \ast } ( \sigma ^ { \mu } e ) _ { b a } \partial _ { \mu } \phi ( x ) - 2 \mathrm{i} \epsilon _ { a } \mathcal{F} ( x ) , } } \\ { { \displaystyle \delta \mathcal{F} ( x ) = - \epsilon ^ { b \ast } \sigma _ { b a } ^ { \mu } \partial _ { \mu } \zeta _ { a } ( x ) . } } \end{array} \tag{26.1.14-26.1.16}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f8132b9fec1e34813d470">
	$$
	\frac { A + \mathrm{i} B } { \sqrt { 2 } } \equiv \phi , \qquad \frac { F - \mathrm{i} G } { \sqrt { 2 } } \equiv \mathcal{F} , \tag{26.1.19}
	$$
</synced_block>
$`\psi`$ 的定义是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f8141bb42ca4693f4b2d7">
	$$
	\psi \equiv \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c } { { \zeta _ { a } } } \\ { { - e _ { a }{}^{ b } \zeta _ { b } ^ { * } } } \end{array} \right) . \tag{26.1.20}
	$$
</synced_block>
我们同时回忆起 $`4 \times 4`$ Dirac 矩阵和 $`2 \times 2`$ 矩阵 $`\sigma _ { \mu }`$ 的关系是:
$$
\gamma _ { \mu } = { \binom { 0 } { \mathrm{i} \sigma _ { \mu } } } \quad { \begin{array} { c } { { - \mathrm{i} e \sigma _ { \mu } ^ { \mathrm { T } } e } } \\ { { 0 } } \end{array} } .
$$
变换规则现在采取如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ea7bec1cb3c00b45c">
	$$
	\begin{array} { l } { { \delta A = \bar { \alpha } \psi , \qquad \delta B = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \psi , } } \\ { { \qquad \delta \psi = \partial _ { \mu } ( A + \mathrm{i} \gamma _ { 5 } B ) \gamma ^ { \mu } \alpha + ( F - \mathrm{i} \gamma _ { 5 } G ) \alpha , } } \\ { { \qquad \delta F = \bar { \alpha } \gamma ^ { \mu } \partial _ { \mu } \psi , \qquad \delta G = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \gamma ^ { \mu } \partial _ { \mu } \psi . } } \end{array} \tag{26.1.21}
	$$
</synced_block>
\\\*\\\*在我们将要使用的相位约定下, Majorana 4 -分量旋量由2 -分量 $`( 1 / 2 , 0 )`$ 旋量 $`u _ { a }`$ 以
$$
\scriptstyle \left( { \begin{array} { l } { u } \\ { - e u ^ { * } } \end{array} } \right)
$$
的方式构成.
方程(26.1.17)符合这一定义, 这里 $`u = - \mathrm{i} \epsilon`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f819e8a4cdc2022392f0e">
		$$
		\alpha \equiv - \mathrm{i} \left( { \epsilon } _ { a } \right) , \tag{26.1.17}
		$$
	</synced_block_reference>
</callout>
等价地, Majorana 旋量可以由 2 -分量 $`( 0 , 1 / 2 )`$ 旋量 $`v _ { a }`$ 以
$$
\binom { e v ^ { * } } { v }
$$
的方式构成.
方程(25.2.34)提供了另外一个例子.
本章附录会细致地考察 Majorana 旋量的性质.
一个繁琐但直接的计算表明, 这个变换保持作用量
<synced_block url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f818eb0d3d72adf70e08c">
	$$
	\begin{array} { c } { { I = \displaystyle \int \mathrm { d } ^ { 4 } x \left\{ - \frac { 1 } { 2 } \partial _ { \mu } A \partial ^ { \mu } A - \frac { 1 } { 2 } \partial _ { \mu } B \partial ^ { \mu } B - \frac { 1 } { 2 } \bar { \psi } \gamma ^ { \mu } \partial _ { \mu } \psi \right. } } \\ { { \left. \qquad \frac { 1 } { 2 } ( F ^ { 2 } + G ^ { 2 } ) + m \left[ F A + G B - \frac { 1 } { 2 } \bar { \psi } \psi \right] \right. } } \\ { { \left. g \Bigl [ F ( A ^ { 2 } + B ^ { 2 } ) + 2 G A B - \bar { \psi } ( A + \mathrm{i} \gamma _ { 5 } B ) \psi \Bigr ] \right\} } } \end{array} \tag{26.1.22}
	$$
</synced_block>
不变.
方程(26.1.21)和(26.1.22)与变换规则(24.2.8)以及 Wess 和 Zumino 的原始工作中发现的拉格朗日密度(24.2.9)一致.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ea7bec1cb3c00b45c">
		$$
		\begin{array} { l } { { \delta A = \bar { \alpha } \psi , \qquad \delta B = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \psi , } } \\ { { \qquad \delta \psi = \partial _ { \mu } ( A + \mathrm{i} \gamma _ { 5 } B ) \gamma ^ { \mu } \alpha + ( F - \mathrm{i} \gamma _ { 5 } G ) \alpha , } } \\ { { \qquad \delta F = \bar { \alpha } \gamma ^ { \mu } \partial _ { \mu } \psi , \qquad \delta G = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \gamma ^ { \mu } \partial _ { \mu } \psi . } } \end{array} \tag{26.1.21}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f818eb0d3d72adf70e08c">
		$$
		\begin{array} { c } { { I = \displaystyle \int \mathrm { d } ^ { 4 } x \left\{ - \frac { 1 } { 2 } \partial _ { \mu } A \partial ^ { \mu } A - \frac { 1 } { 2 } \partial _ { \mu } B \partial ^ { \mu } B - \frac { 1 } { 2 } \bar { \psi } \gamma ^ { \mu } \partial _ { \mu } \psi \right. } } \\ { { \left. \qquad \frac { 1 } { 2 } ( F ^ { 2 } + G ^ { 2 } ) + m \left[ F A + G B - \frac { 1 } { 2 } \bar { \psi } \psi \right] \right. } } \\ { { \left. g \Bigl [ F ( A ^ { 2 } + B ^ { 2 } ) + 2 G A B - \bar { \psi } ( A + \mathrm{i} \gamma _ { 5 } B ) \psi \Bigr ] \right\} } } \end{array} \tag{26.1.22}
		$$
	</synced_block_reference>
</callout>
在接下来的三节, 我们将会探索检验方程(26.1.22)的超对称性和导出更一般的超对称理论的一个方便技巧.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f818eb0d3d72adf70e08c">
		$$
		\begin{array} { c } { { I = \displaystyle \int \mathrm { d } ^ { 4 } x \left\{ - \frac { 1 } { 2 } \partial _ { \mu } A \partial ^ { \mu } A - \frac { 1 } { 2 } \partial _ { \mu } B \partial ^ { \mu } B - \frac { 1 } { 2 } \bar { \psi } \gamma ^ { \mu } \partial _ { \mu } \psi \right. } } \\ { { \left. \qquad \frac { 1 } { 2 } ( F ^ { 2 } + G ^ { 2 } ) + m \left[ F A + G B - \frac { 1 } { 2 } \bar { \psi } \psi \right] \right. } } \\ { { \left. g \Bigl [ F ( A ^ { 2 } + B ^ { 2 } ) + 2 G A B - \bar { \psi } ( A + \mathrm{i} \gamma _ { 5 } B ) \psi \Bigr ] \right\} } } \end{array} \tag{26.1.22}
		$$
	</synced_block_reference>
</callout>
当费米场 $`\psi ( x )`$ 满足自由场 Dirac方程 $`( \gamma ^ { \mu } \partial _ { \mu } + m ) \psi = 0`$ 时, 这些变换规则表明 $`F + m A`$ 和 $`G +`$ $`m B`$ 是不变的, 因此与 $`\mathcal{Q} _ { a }`$ 和 $`{ \mathcal{Q} } _ { a } ^ { * }`$ 对易, 随之也与 $`P _ { \mu }`$ 对易.
这并不能证明 $`F = - m A`$ 和 $`G = - m B`$ ,但在不改变对易和反对易规则(26.1.1)—(26.1.6)或变换规则(26.1.21)的前提下, 我们可以通过分别减除掉常数 $`F + m A`$ 和 $`B + m G`$ 重新定义场 $`F`$ 和 $`G`$ , 使得新的场 $`F`$ 和 $`G`$ 由 $`F = - m A`$ 和 $`G =`$ $`- m B`$ 给定, 因而就有 $`\mathcal{F} = - m \phi ^ { * }`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ba131c81d19a3c585">
		$$
		[ { \mathcal{Q} } _ { a } , \phi ( x ) ] = 0 , \tag{26.1.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f81ea8b76c14b3ca9a9f7">
		$$
		\left[ \mathcal{Q} _ { c } , \mathcal{F} ( x ) \right] = - \sigma _ { c a } ^ { \mu } \partial _ { \mu } \zeta _ { a } ( x ) . \tag{26.1.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f810ea7bec1cb3c00b45c">
		$$
		\begin{array} { l } { { \delta A = \bar { \alpha } \psi , \qquad \delta B = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \psi , } } \\ { { \qquad \delta \psi = \partial _ { \mu } ( A + \mathrm{i} \gamma _ { 5 } B ) \gamma ^ { \mu } \alpha + ( F - \mathrm{i} \gamma _ { 5 } G ) \alpha , } } \\ { { \qquad \delta F = \bar { \alpha } \gamma ^ { \mu } \partial _ { \mu } \psi , \qquad \delta G = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \gamma ^ { \mu } \partial _ { \mu } \psi . } } \end{array} \tag{26.1.21}
		$$
	</synced_block_reference>
</callout>
在有相互作用时, 这是不成立的, 但即使是在有相互作用的情况下, $`{ \mathcal{F} } ( x )`$ , $`F ( x )`$ 和 $`G ( x )`$ 一般是辅助场, 就像作用量(26.1.22)的情况, 它们可以被超多重态的其它场表示.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81efaf28fa4031d4303e#34cee2b74b3f818eb0d3d72adf70e08c">
		$$
		\begin{array} { c } { { I = \displaystyle \int \mathrm { d } ^ { 4 } x \left\{ - \frac { 1 } { 2 } \partial _ { \mu } A \partial ^ { \mu } A - \frac { 1 } { 2 } \partial _ { \mu } B \partial ^ { \mu } B - \frac { 1 } { 2 } \bar { \psi } \gamma ^ { \mu } \partial _ { \mu } \psi \right. } } \\ { { \left. \qquad \frac { 1 } { 2 } ( F ^ { 2 } + G ^ { 2 } ) + m \left[ F A + G B - \frac { 1 } { 2 } \bar { \psi } \psi \right] \right. } } \\ { { \left. g \Bigl [ F ( A ^ { 2 } + B ^ { 2 } ) + 2 G A B - \bar { \psi } ( A + \mathrm{i} \gamma _ { 5 } B ) \psi \Bigr ] \right\} } } \end{array} \tag{26.1.22}
		$$
	</synced_block_reference>
</callout>
</content>
</page>
