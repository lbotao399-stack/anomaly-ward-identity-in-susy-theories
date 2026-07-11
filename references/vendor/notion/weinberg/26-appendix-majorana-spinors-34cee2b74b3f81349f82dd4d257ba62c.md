Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c as of 2026-06-30T03:26:17.933Z:
<page url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"附录 Majorana 旋量"}
</properties>
<content>
这个附录总结了一些处理超场时需要的 Majorana 旋量的代数性质.
考察像 $`Q`$ 或 $`\theta`$ 这样的 4 分量费米 Majorana 旋量 $`s`$ , 它可以表示成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81209c97deeb25f708ee">
	$$
	s = { \binom { e \varsigma ^ { * } } { \varsigma } } \ , \tag{26.A.1}
	$$
</synced_block>
其中ς 是某个2 分量旋量而 $`e`$ 是 $`2 \times 2`$ 矩阵
$$
e \equiv \left( \begin{array} { l l } { { 0 } } & { { 1 } } \\ { { - 1 } } & { { 0 } } \end{array} \right) = \mathrm{i} \sigma _ { 2 } .
$$
这样的旋量与它的复共轭的关系是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81bd92f2ff8d2a1a6247">
	$$
	s^*=\begin{pmatrix}0&e\\-e&0\end{pmatrix}s=-\beta\gamma_5\epsilon s.\tag{26.A.2}
	$$
</synced_block>
其中 $`\epsilon`$ 是 $`4 \times 4`$ 矩阵
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81bbbc98c735742008ab">
	$$
	\epsilon\equiv\begin{pmatrix}e&0\\0&e\end{pmatrix}.\tag{26.A.3}
	$$
</synced_block>
而 $`\gamma _ { 5 }`$ 和 $`\beta`$ 同往常一样是 $`4 \times 4`$ 矩阵
$$
\gamma_5=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\beta=\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$
其中1和0在这里被理解成 $`2 \times 2`$ 子矩阵.
取方程(26.A.2)的转置然后从右边乘上 $`\beta`$ 就给出了等价公式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81bd92f2ff8d2a1a6247">
		$$
		s^*=\begin{pmatrix}0&e\\-e&0\end{pmatrix}s=-\beta\gamma_5\epsilon s.\tag{26.A.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81969212fcbfb070c778">
	$$
	\bar { s } \equiv s ^ { \dagger } \beta = s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } . \tag{26.A.4}
	$$
</synced_block>
旋量分量的反对易系限制了能够从Majorana旋量中构造出的协变量的种类.
为了看到这点,首先考察双线性协变量的对称性质将是方便的, 而它们自身也是有趣的.
对于一对Majorana旋量 $`s _ { 1 }`$ 和 $`s _ { 2 }`$ 以及任意 $`4 \times 4`$ 数值矩阵 $`M`$ , 方程(26.A.4)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81969212fcbfb070c778">
		$$
		\bar { s } \equiv s ^ { \dagger } \beta = s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } . \tag{26.A.4}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r } { \overline { { s _ { 1 } } } M s _ { 2 } = s _ { 1 \alpha } s _ { 2 \beta } ( \epsilon \gamma _ { 5 } M ) _ { \alpha \beta } = - s _ { 2 \alpha } s _ { 1 \beta } ( \epsilon \gamma _ { 5 } M ) _ { \beta \alpha } } \\ { = + s _ { 2 \alpha } s _ { 1 \beta } ( M ^ { \mathrm { T } } \epsilon \gamma _ { 5 } ) _ { \alpha \beta } = \overline { { s _ { 2 } } } ( \epsilon \gamma _ { 5 } ) ^ { - 1 } M ^ { \mathrm { T } } \epsilon \gamma _ { 5 } s _ { 1 } , } \end{array}
$$
其中第二个等号后面的负号是因为这些旋量的费米性.
我们在5.4节发现, 从Dirac矩阵构造出来的16个协变矩阵满足
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81cba5eded23c3d7723a">
	$$
	\begin{array} { r } { M ^ { \mathrm { T } } = \left\{ \begin{array} { l l } { + \mathcal{C} M \mathcal{C} ^ { - 1 } \quad } & { M = 1 , \ \gamma _ { 5 } \gamma _ { \mu } , \ \gamma _ { 5 } } \\ { - \mathcal{C} M \mathcal{C} ^ { - 1 } \quad } & { M = \gamma _ { \mu } , \ [ \gamma _ { \mu } , \gamma _ { \nu } ] } \end{array} \right. , } \end{array} \tag{26.A.5}
	$$
</synced_block>
其中 $`\mathcal{C}`$ 是矩阵
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f814aa72be32ce105ca87">
	$$
	\begin{array} { r } { \mathcal{C} = \gamma _ { 2 } \beta = - \epsilon \gamma _ { 5 } = \left( \begin{array} { l l } { - e } & { 0 } \\ { 0 } & { e } \end{array} \right) . } \end{array} \tag{26.A.6}
	$$
</synced_block>
从它得出
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f812dbfd2df88f108bb3b">
	$$
	( \overline { { { s _ { 1 } } } } M s _ { 2 } ) = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = 1 , \gamma _ { 5 } \gamma _ { \mu } , \gamma _ { 5 } } } \\ { { - ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = \gamma _ { \mu } , [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \end{array} \right. . \tag{26.A.7}
	$$
</synced_block>
特别地, 令 $`s _ { 1 } = s _ { 2 } = s`$ , 我们发现
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81e99923e7e18f38ecb0">
	$$
	\bar { s } \gamma _ { \mu } s = \bar { s } \left[ \gamma _ { \mu } , \gamma _ { \nu } \right] s = 0 , \tag{26.A.8}
	$$
</synced_block>
所以从单个 Majorana 旋量 $`s`$ 构造出来的双线性协变量只有 $`\bar { s } s`$ , $`\bar { s } \gamma _ { 5 } \gamma _ { \mu } s`$ 和 $`\bar { s } \gamma _ { 5 } s`$ .
在考察最一般超场的形式时, 我们需要两个或多个 Majorana 旋量乘积的表达式.
对于两个旋量, 我们回忆起任何 $`4 { \times } 4`$ 矩阵都可以表示成 16 个协变矩阵 $`1 , \gamma _ { \mu } , [ \gamma _ { \mu } , \gamma _ { \nu } ] , \gamma _ { 5 } \gamma _ { \mu } , \gamma _ { 5 }`$ 的和.
Lorentz 不变性告诉我们, 对于矩阵 $`s _ { \alpha } \bar { s } _ { \beta }`$ , 这个表达式必须采取如下的形式
$$
\begin{array} { c } { { s \overline { { { s } } } = k _ { S } \left( \overline { { { s } } } s \right) + k _ { V } \gamma _ { \mu } \left( \overline { { { s } } } \gamma ^ { \mu } s \right) + k _ { T } \left[ \gamma _ { \mu } , \gamma _ { \nu } \right] \left( \overline { { { s } } } \left[ \gamma ^ { \mu } , \gamma ^ { \nu } \right] s \right) } } \\ { { { } } } \\ { { + k _ { A } \gamma _ { 5 } \gamma _ { \mu } \left( \overline { { { s } } } \gamma _ { 5 } \gamma ^ { \mu } s \right) + k _ { P } \gamma _ { 5 } \left( \overline { { { s } } } \gamma _ { 5 } s \right) , } } \end{array}
$$
其中这些 $`k`$ 是需要决定的常数.
方程(26.A.8)表明我们可以取 $`k _ { V } = k _ { T } = 0`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81e99923e7e18f38ecb0">
		$$
		\bar { s } \gamma _ { \mu } s = \bar { s } \left[ \gamma _ { \mu } , \gamma _ { \nu } \right] s = 0 , \tag{26.A.8}
		$$
	</synced_block_reference>
</callout>
通过从右边乘上 1,$`\gamma _ { 5 } \gamma ^ { \mu }`$ 和 $`\gamma _ { 5 }`$ 然后在取迹, 我们可以计算出剩下的系数, 这个方法给出 $`k _ { S } = - 1 / 4`$ , $`k _ { A } = + 1 / 4`$ 和 $`k _ { P } =`$ $`- 1 / 4`$ .
以这种方法, 我们发现
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81ed90b4fd1a2f33b2df">
	$$
	\begin{array} { r } { s \bar { s } = - \frac { 1 } { 4 } ( \bar { s } s ) + \frac { 1 } { 4 } \gamma _ { 5 } \gamma _ { \mu } ( \bar { s } \gamma _ { 5 } \gamma ^ { \mu } s ) - \frac { 1 } { 4 } \gamma _ { 5 } \left( \bar { s } \gamma _ { 5 } s \right) . } \end{array} \tag{26.A.9}
	$$
</synced_block>
通过给右边乘上 $`- \epsilon \gamma _ { 5 }`$ 并使用方程(26.A.4), 我们可以将其变成如下形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81969212fcbfb070c778">
		$$
		\bar { s } \equiv s ^ { \dagger } \beta = s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } . \tag{26.A.4}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81f18556cfce5b7fe611">
	$$
	s _ { \alpha } s _ { \beta } = { \textstyle { \frac { 1 } { 4 } } } ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( \bar { s } s ) + { \textstyle { \frac { 1 } { 4 } } } ( \gamma _ { \mu } \epsilon ) _ { \alpha \beta } ( \bar { s } \gamma _ { 5 } \gamma ^ { \mu } s ) + { \textstyle { \frac { 1 } { 4 } } } \epsilon _ { \alpha \beta } ( \bar { s } \gamma _ { 5 } s ) , \tag{26.A.10}
	$$
</synced_block>
或者, 等价地,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8169909ed8efbe45884c">
	$$
	\begin{array} { r } { s _ { \alpha } s _ { \beta } = \frac { 1 } { 4 } ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } s ) + \frac { 1 } { 4 } ( \gamma _ { \mu } \epsilon ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma ^ { \mu } s ) + \frac { 1 } { 4 } \epsilon _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon s ) . } \end{array} \tag{26.A.11}
	$$
</synced_block>
现在, 考察 Majorana 旋量 $`s`$ 的 3 个分量的乘积 $`s _ { \alpha } s _ { \beta } s _ { \gamma }`$ .
我们可以把 $`s`$ 分成左手部分和右手部分
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8173ab9beb667a71dce3">
	$$
	\begin{array} { c c c c } { { s = s _ { L } + s _ { R } , } } & { { } } & { { s _ { L } = \textstyle { \frac { 1 } { 2 } } ( 1 + \gamma _ { 5 } ) s , \ : \ : \ : } } & { { s _ { R } = \textstyle { \frac { 1 } { 2 } } ( 1 - \gamma _ { 5 } ) s . } } \end{array} \tag{26.A.12}
	$$
</synced_block>
$`s _ { L }`$ 和 $`s _ { R }`$ 都只有两个独立分量, 又因为任何费米 $`\mathrm { c }`$ -数的平方为零, 所以对于所有 $`\alpha , ~ \beta`$ 和 $`\gamma`$ , 我们有 $`s _ { L \alpha } s _ { L \beta } s _ { L \gamma } = 0`$ 和 $`s _ { R \alpha } s _ { R \beta } s _ { R \gamma } = 0`$ , 因此
$$
s _ { \alpha } s _ { \beta } s _ { \gamma } = s _ { L \alpha } s _ { L \beta } s _ { L \gamma } + s _ { L \alpha } s _ { R \beta } s _ { L \gamma } + s _ { R \alpha } s _ { L \beta } s _ { L \gamma } + L R ,
$$
其中“ $`L { } R`$ ”表示对前面的项交换 $`L`$ 和 $`R`$ 指标后的和.
为了计算这个表达式, 我们给方程(26.A.11)乘上合适的因子 $`( 1 + \gamma _ { 5 } ) / 2`$ , 并发现
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8169909ed8efbe45884c">
		$$
		\begin{array} { r } { s _ { \alpha } s _ { \beta } = \frac { 1 } { 4 } ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } s ) + \frac { 1 } { 4 } ( \gamma _ { \mu } \epsilon ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma ^ { \mu } s ) + \frac { 1 } { 4 } \epsilon _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon s ) . } \end{array} \tag{26.A.11}
		$$
	</synced_block_reference>
</callout>
$$
s _ { L \alpha } s _ { L \beta } = { \textstyle { \frac { 1 } { 4 } } } [ \epsilon ( 1 + \gamma _ { 5 } ) ] _ { \alpha \beta } \left( s _ { L } ^ { \mathrm { T } } \epsilon s _ { L } \right) .
$$
如果我们现在给它乘上 $`s _ { R \gamma }`$ , 由于 $`( s _ { R } ^ { \mathrm { T } } \epsilon s _ { R } ) s _ { R \gamma } = 0`$ , 我们可以扔掉双线性型 $`( s _ { L } ^ { \mathrm { T } } \epsilon s _ { L } )`$ 中旋量上的指标 $`L`$ :
$$
\begin{array} { r } { s _ { L \alpha } s _ { L \beta } s _ { R \gamma } = \frac { 1 } { 4 } [ \epsilon ( 1 + \gamma _ { 5 } ) ] _ { \alpha \beta } \left( s ^ { \mathrm { T } } \epsilon s \right) s _ { R \gamma } . } \end{array}
$$
相同的讨论也给出
$$
\begin{array} { r } { s _ { R \alpha } s _ { L \beta } s _ { L \gamma } = \frac { 1 } { 4 } [ \epsilon ( 1 - \gamma _ { 5 } ) ] _ { \alpha \beta } \left( s ^ { \mathrm { T } } \epsilon s \right) s _ { L \gamma } . } \end{array}
$$
对这个两个表达式求和, 再将结果中的 $`\gamma`$ 换成 $`\alpha`$ 或 $`\beta`$ , 把所有这些加起来最后给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f817a890ec37a7eb1c7fb">
	$$
	\begin{array} { r l } & { s _ { \alpha } s _ { \beta } s _ { \gamma } = \frac { 1 } { 4 } \Big ( s ^ { \mathrm { T } } \epsilon s \Big ) \Big [ \epsilon _ { \alpha \beta } s _ { \gamma } - ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( \gamma _ { 5 } s ) _ { \gamma } - \epsilon _ { \alpha \gamma } s _ { \beta } } \\ & { \qquad + ( \epsilon \gamma _ { 5 } ) _ { \alpha \gamma } ( \gamma _ { 5 } s ) _ { \beta } + \epsilon _ { \beta \gamma } s _ { \alpha } - ( \epsilon \gamma _ { 5 } ) _ { \beta \gamma } ( \gamma _ { 5 } s ) _ { \alpha } \Big ] . } \end{array} \tag{26.A.13}
	$$
</synced_block>
为了计算 4 个Majorana 旋量分量的乘积, 我们注意到 $`( s ^ { \mathrm { T } } \epsilon s )`$ 只包含两个 $`s _ { L }`$ 的项或两个 $`s _ { R }`$ 的项, 所以
$$
(s^{\mathrm T}\epsilon s)s_\gamma s_\delta
=(s^{\mathrm T}\epsilon s)\left[s_{R\gamma}s_{R\delta}+s_{L\gamma}s_{L\delta}\right].
$$
利用方程(26.A.11)计算方括号中的和, 并注意到
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8169909ed8efbe45884c">
		$$
		\begin{array} { r } { s _ { \alpha } s _ { \beta } = \frac { 1 } { 4 } ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } s ) + \frac { 1 } { 4 } ( \gamma _ { \mu } \epsilon ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma ^ { \mu } s ) + \frac { 1 } { 4 } \epsilon _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon s ) . } \end{array} \tag{26.A.11}
		$$
	</synced_block_reference>
</callout>
$$
( s ^ { \mathrm { T } } \epsilon s ) ( s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } s ) = ( s _ { L } ^ { \mathrm { T } } \epsilon s _ { L } ) ( s _ { R } ^ { \mathrm { T } } \epsilon s _ { R } ) - ( s _ { R } ^ { \mathrm { T } } \epsilon s _ { R } ) ( s _ { L } ^ { \mathrm { T } } \epsilon s _ { L } ) = 0 ,
$$
我们发现
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8118bb87d6470bbf977a">
	$$
	\begin{array} { r } { ( s ^ { \mathrm { T } } \epsilon s ) s _ { \gamma } s _ { \delta } = \frac { 1 } { 4 } \epsilon _ { \gamma \delta } ( s ^ { \mathrm { T } } \epsilon s ) ^ { 2 } . } \end{array} \tag{26.A.14}
	$$
</synced_block>
因此给方程(26.A.13)乘上 $`s _ { \delta }`$ 就给出结果
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f817a890ec37a7eb1c7fb">
		$$
		\begin{array} { r l } & { s _ { \alpha } s _ { \beta } s _ { \gamma } = \frac { 1 } { 4 } \Big ( s ^ { \mathrm { T } } \epsilon s \Big ) \Big [ \epsilon _ { \alpha \beta } s _ { \gamma } - ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( \gamma _ { 5 } s ) _ { \gamma } - \epsilon _ { \alpha \gamma } s _ { \beta } } \\ & { \qquad + ( \epsilon \gamma _ { 5 } ) _ { \alpha \gamma } ( \gamma _ { 5 } s ) _ { \beta } + \epsilon _ { \beta \gamma } s _ { \alpha } - ( \epsilon \gamma _ { 5 } ) _ { \beta \gamma } ( \gamma _ { 5 } s ) _ { \alpha } \Big ] . } \end{array} \tag{26.A.13}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f815fb256ef5c55643f36">
	$$
	\begin{array} { r } { s _ { \alpha } s _ { \beta } s _ { \gamma } s _ { \delta } = \frac { 1 } { 1 6 } \Big ( s ^ { \mathrm { T } } \epsilon s \Big ) ^ { 2 } \Big [ \epsilon _ { \alpha \beta } \epsilon _ { \gamma \delta } - \big ( \epsilon \gamma _ { 5 } \big ) _ { \alpha \beta } \big ( \epsilon \gamma _ { 5 } \big ) _ { \gamma \delta } - \epsilon _ { \alpha \gamma } \epsilon _ { \beta \delta } } \\ { + \big ( \epsilon \gamma _ { 5 } \big ) _ { \alpha \gamma } \big ( \epsilon \gamma _ { 5 } \big ) _ { \beta \delta } + \epsilon _ { \beta \gamma } \epsilon _ { \alpha \delta } - \big ( \epsilon \gamma _ { 5 } \big ) _ { \beta \gamma } \big ( \epsilon \gamma _ { 5 } \big ) _ { \alpha \delta } \Big ] \ . } \end{array} \tag{26.A.15}
	$$
</synced_block>
五个 $`s`$ 分量的任意乘积都为零, 所以这样就列完了 Majorana 旋量分量的乘积公式.
我们可以用这些公式推导一些在处理超场时有用的加法关系.
通过用 $`( \epsilon \gamma _ { 5 } ) _ { \beta \gamma }`$ 和 $`( \epsilon \gamma _ { \mu } ) _ { \beta \gamma }`$ 收缩方程(26.A.13), 我们发现
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f817a890ec37a7eb1c7fb">
		$$
		\begin{array} { r l } & { s _ { \alpha } s _ { \beta } s _ { \gamma } = \frac { 1 } { 4 } \Big ( s ^ { \mathrm { T } } \epsilon s \Big ) \Big [ \epsilon _ { \alpha \beta } s _ { \gamma } - ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( \gamma _ { 5 } s ) _ { \gamma } - \epsilon _ { \alpha \gamma } s _ { \beta } } \\ & { \qquad + ( \epsilon \gamma _ { 5 } ) _ { \alpha \gamma } ( \gamma _ { 5 } s ) _ { \beta } + \epsilon _ { \beta \gamma } s _ { \alpha } - ( \epsilon \gamma _ { 5 } ) _ { \beta \gamma } ( \gamma _ { 5 } s ) _ { \alpha } \Big ] . } \end{array} \tag{26.A.13}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81ba90b3cb0dc40f0b4c">
	$$
	s _ { \alpha } \left( \bar { s } s \right) = - ( \gamma _ { 5 } s ) _ { \alpha } \left( \bar { s } \gamma _ { 5 } s \right) \tag{26.A.16}
	$$
</synced_block>
和
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8168865bf41f3dacf374">
	$$
	s _ { \alpha } \left( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \right) = - ( \gamma _ { \mu } s ) _ { \alpha } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) . \tag{26.A.17}
	$$
</synced_block>
我们可以从方程(26.A.16)和(26.A.17)导出“Fierz”恒等式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81ba90b3cb0dc40f0b4c">
		$$
		s _ { \alpha } \left( \bar { s } s \right) = - ( \gamma _ { 5 } s ) _ { \alpha } \left( \bar { s } \gamma _ { 5 } s \right) \tag{26.A.16}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8168865bf41f3dacf374">
		$$
		s _ { \alpha } \left( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \right) = - ( \gamma _ { \mu } s ) _ { \alpha } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) . \tag{26.A.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81678701ee7b96af9b3b">
	$$
	\Bigl ( \bar { s } s \Bigr ) ^ { 2 } = - \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } , \qquad \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \Bigr ) \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \nu } s \Bigr ) = - \eta _ { \mu \nu } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } . \tag{26.A.18}
	$$
</synced_block>
另外, 方程(26.A.14)可以写成协变形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8118bb87d6470bbf977a">
		$$
		\begin{array} { r } { ( s ^ { \mathrm { T } } \epsilon s ) s _ { \gamma } s _ { \delta } = \frac { 1 } { 4 } \epsilon _ { \gamma \delta } ( s ^ { \mathrm { T } } \epsilon s ) ^ { 2 } . } \end{array} \tag{26.A.14}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81459208c3b78885c16b">
	$$
	\begin{array} { r } { ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } s \bar { s } = - \frac { 1 } { 4 } \gamma _ { 5 } ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } . } \end{array} \tag{26.A.19}
	$$
</synced_block>
标明Majorana旋量双线性积的实性质也将是有用的.
对于任何一对满足相位约定(26.A.1)的Majorana 旋量 $`s _ { 1 }`$ 和 $`s _ { 2 }`$ , 方程(26.A.2)和(26.A.4)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81209c97deeb25f708ee">
		$$
		s = { \binom { e \varsigma ^ { * } } { \varsigma } } \ , \tag{26.A.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81bd92f2ff8d2a1a6247">
		$$
		s^*=\begin{pmatrix}0&e\\-e&0\end{pmatrix}s=-\beta\gamma_5\epsilon s.\tag{26.A.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81969212fcbfb070c778">
		$$
		\bar { s } \equiv s ^ { \dagger } \beta = s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } . \tag{26.A.4}
		$$
	</synced_block_reference>
</callout>
$$
( \overline { { { s _ { 1 } } } } M s _ { 2 } ) ^ { * } = - ( s _ { 1 } ^ { \dag } \epsilon \gamma _ { 5 } M ^ { * } s _ { 2 } ^ { * } ) = ( \overline { { { s _ { 1 } } } } \beta \epsilon \gamma _ { 5 } M ^ { * } \beta \epsilon \gamma _ { 5 } s _ { 2 } ) .
$$
(中间表达式的负号来自于我们撤销了 $`s _ { 1 }`$ 和 $`s _ { 2 }`$ 的交换, 这会在我们取复共轭时发生.) 但是方程(5.4.40)和(26.A.6)给出 $`\beta \epsilon \gamma _ { 5 } \gamma _ { \mu } ^ { * } \beta \epsilon \gamma _ { 5 } = \gamma _ { \mu }`$ , 所以
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f814aa72be32ce105ca87">
		$$
		\begin{array} { r } { \mathcal{C} = \gamma _ { 2 } \beta = - \epsilon \gamma _ { 5 } = \left( \begin{array} { l l } { - e } & { 0 } \\ { 0 } & { e } \end{array} \right) . } \end{array} \tag{26.A.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f811b8c83fb1a2f139be1">
	$$
	\beta \epsilon \gamma _ { 5 } M ^ { * } \beta \epsilon \gamma _ { 5 } = \left\{ \begin{array} { l l } { { + M \qquad } } & { { M = 1 , \gamma _ { \mu } , [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \\ { { - M \qquad } } & { { M = \gamma _ { \mu } \gamma _ { 5 } , \gamma _ { 5 } } } \end{array} \right. , \tag{26.A.20}
	$$
</synced_block>
因此
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8158a2fdc1adcd361128">
	$$
	( \overline { { { s _ { 1 } } } } M s _ { 2 } ) ^ { * } = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = 1 , \ \gamma _ { \mu } , \ [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \\ { { - ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = \gamma _ { \mu } \gamma _ { 5 } , \ \gamma _ { 5 } } } \end{array} \right. . \tag{26.A.21}
	$$
</synced_block>
最后我们提一下, 任何旋量 $`u`$ 都可以写成一对 Majorana 旋量 $`s_\pm`$
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f8126acd2c7e1bae669cc">
	$$
	u = s _ { + } + \mathrm{i} s _ { - } , \tag{26.A.22}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81718ac8e47eb8fe99ad">
	$$
	s _ { + } \equiv \frac { 1 } { 2 } \Big ( u - \beta \epsilon \gamma _ { 5 } u ^ { * } \Big ) , \qquad s _ { - } \equiv \frac { 1 } { 2 \mathrm{i} } \Big ( u + \beta \epsilon \gamma _ { 5 } u ^ { * } \Big ) . \tag{26.A.23}
	$$
</synced_block>
为了验证 $`s _ { \pm }`$ 是满足方程(26.A.2)的 Majorana 旋量, 只需回忆起 $`\beta \epsilon \gamma _ { 5 }`$ 是实的, 以及 $`( \beta \epsilon \gamma _ { 5 } ) ^ { 2 } = 1`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81bd92f2ff8d2a1a6247">
		$$
		s^*=\begin{pmatrix}0&e\\-e&0\end{pmatrix}s=-\beta\gamma_5\epsilon s.\tag{26.A.2}
		$$
	</synced_block_reference>
</callout>
## 习题
1. 在 $`N = 2`$ 超对称的情况下, 利用 26.1 节的直接技巧, 找到只有一个 Majorana 旋量场和两个复标量场的有质量场超多重态的超对称变换规则.
2. 计算时间反演超场
$$
\mathsf { T } ^ { - 1 } S ( x , \theta ) \mathsf { T }
$$
的分量场, 将它们写成超场 $`S ( x , \theta )`$ 的分量场的形式.
对于左手征超场的时间反演, 我们得到了哪类超场? 对于线性超场又是什么?
1. 考察单个左手征超场 $`\Phi`$ 的 $`N = 1`$ 超对称理论.
在超场的符号约定下,列出所有包含 $`\Phi`$ 和(或) $`\Phi ^ { * }`$ 且量纲为5的可以加到拉格朗日密度上的项.
1. 考察三个左手征超场 $`\Phi^1`$ , $`\Phi^2`$ 和 $`\Phi^3`$ 的理论, 它有通常的动能项, 以及超势
$$
f(\Phi^1,\Phi^2,\Phi^3)=\Phi^1(\Phi^3)^2+\Phi^2\left((\Phi^3)^2+a\right),
$$
其中 $`a`$ 是一个非零实常数.
证明这是一个超对称自发破缺的理论.
找到势能的最小值.
将戈德斯通微子的场表示成 $`\Phi^1`$ , $`\Phi^2`$ 和 $`\Phi^3`$ 的费米分量.
1. 对于作用量(26.6.9), 找到流超场的所有分量, 将它们写成左手征超场 $`\Phi`$ 的分量, 超势 $`f`$ 的导数以及 Kähler 势 $`K`$ 的形式.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f812fad00cec051e26db7">
		$$
		I = \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } + 2 \operatorname{Re} \int \mathrm { d } ^ { 4 } x [ f ( \Phi ) ] _ { \mathcal{F} } , \tag{26.6.9}
		$$
	</synced_block_reference>
</callout>
1. 验证方程(26.7.18)和(26.7.10)给出的超对称流与超场(26.7.21)的 $`\omega`$ -分量通过方程(26.7.20)相关联.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f815dba68d17d44237801">
		$$
		S _ { \mathrm{new} } ^ { \mu } = S ^ { \mu } + \frac { \sqrt { 2 } } { 3 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] \partial _ { \nu } \Big ( \phi _ { n } \psi ^ { n } _ { R } + \phi ^ { * \, n } \psi _ { n L } \Big ) , \tag{26.7.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f817da994f13a0440c19e">
		$$
		S ^ { \mu } = \sqrt { 2 } \left[ ( \not\!\partial\, \phi _ { n } ) \gamma ^ { \mu } \psi ^ { n } _ { R } + ( \not\!\partial\, \phi ^ { * \, n } ) \gamma ^ { \mu } \psi _ { n L } + \left( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right) \gamma ^ { \mu } \psi _ { n L } + \left( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right) ^ { * } \gamma ^ { \mu } \psi ^ { n } _ { R } \right] . \tag{26.7.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81cead0be409310ceb93">
		$$
		\Theta _ { \mu } = \frac { \mathrm{i} } { 12 } \left[ 4 \Phi ^ { * \, n } \partial _ { \mu } \Phi _ { n } - 4 \Phi _ { n } \partial _ { \mu } \Phi ^ { * \, n } + \left( ( \bar { \mathcal{D} } \Phi ^ { * \, n } ) \gamma _ { \mu } ( \mathcal{D} \Phi _ { n } ) \right) \right] . \tag{26.7.21}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81349f82dd4d257ba62c#34cee2b74b3f81708b14d39b093e501a">
		$$
		S _ { \mathrm{new} } ^ { \mu } = - 2 \omega ^ { \ominus \mu } + 2 \gamma ^ { \mu } \gamma ^ { \nu } \omega _ { \nu } ^ { \ominus } , \tag{26.7.20}
		$$
	</synced_block_reference>
</callout>
</content>
</page>
