Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b as of 2026-06-30T02:39:14.279Z:
<page url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.4 手征超场的可重整理论"}
</properties>
<content>
我们现在将给出标量超场的一般可重整理论的细节.
这会为超对称的应用提供一些启发, 并且我们获得的理论将是第28章讨论的超对称标准模型的一部分.
正如在12.2节中所讨论的, 可重整理论的拉格朗日密度只能包含量纲(以动量或能量为单位,且有 $`\hbar = c = 1 ,`$ )小于或等于4的算符.
方程(26.2.6)表明 $`{ \mathcal{Q} } _ { \alpha }`$ 和随之的 $`\partial / \partial \theta _ { \alpha }`$ 拥有量纲 $`1 / 2`$ , 所以 $`{ \mathcal{D} } _ { \alpha }`$ 有量纲 $`+ 1 / 2`$ , 而 $`\theta _ { \alpha }`$ 有量纲 $`- 1 / 2`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f812a87f0d48dffd6bcba">
		$$
		\left\{ { \mathcal{Q} } _ { \alpha } , { \overline { { { \mathcal{Q} } } } } _ { \beta } \right\} = 2 \gamma _ { \alpha \beta } ^ { \mu } { \frac { \partial } { \partial x ^ { \mu } } } . \tag{26.2.6}
		$$
	</synced_block_reference>
</callout>
超场 $`S`$ 的 $`\mathcal{F}`$ -项和 $`D`$ -项分别是两个 $`\theta`$ 因子和四个 $`\theta`$ 因子的系数, 所以如果超场的量纲是 $`d ( S )`$ , 那么它的 $`\mathcal{F}`$ -项和 $`D`$ -项分别有量纲 $`d ( \mathcal{F} ^ { S } ) = d ( S ) + 1`$ 和$`d ( D ^ { S } ) = d ( S ) + 2 .`$ 因此在可重整理论中,方程(26.3.30)中的函数 $`f`$ 和 $`K`$ 分别由量纲最多为3和2的算符构成.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8185b369e09fb8d66190">
		$$
		I = \int \mathrm { d } ^ { 4 } x \left[ f \right] _ { \mathcal{F} } + \int \mathrm { d } ^ { 4 } x \left[ f \right] _ { \mathcal{F} } ^ { \ast } + \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \left[ K \right] _ { D } , \tag{26.3.30}
		$$
	</synced_block_reference>
</callout>
基本标量超场 $`\Phi _ { n }`$ 的量纲是基本标量场的量纲, 或者说 $`+ 1`$ , 所以, 为了使函数 $`f`$ 中每一项的量纲小于等于 3, 它能包含的 $`\Phi _ { n }`$ 因子个数和(或)导数 $`\partial / \partial x ^ { \mu }`$ 的个数和(或)成对旋量超导数 $`{ \mathcal{D} } _ { \alpha }`$ 的个数不超过 3. 我们在上一节讨论过, $`f`$ 中任何包含超导数的左手征项都可以被 $`K`$ 中的项替换, 所以可以忽略 $`f`$ 中的超导数.
方程(26.2.30)表明时空导数可以表示成超导数, 所以它们也可以被忽略掉.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81738a97d99db41eabd6">
		$$
		\Big \{ \mathcal{D} _ { \alpha } , \overline { { { \mathcal{D} } } } _ { \beta } \Big \} = - 2 \gamma _ { \alpha \beta } ^ { \mu } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.30}
		$$
	</synced_block_reference>
</callout>
(在任何情况下, Lorentz不变性可以排除掉只有一个时空导数的项, 而在可重整理论中, 有两个导数的项只能包含一个 $`\Phi _ { n }`$ 因子, 这些导数必须要作用在这个因子上, 所以这样的项对作用量无贡献.) 我们得出: $`f ( \Phi )`$ 最多是 $`\Phi _ { n }`$ 的三次多项式并且不含时空导数和超导数.
同样的量纲分析表明, 可重整理论中的 $`K`$ 最多是 $`\Phi _ { n }`$ 和 $`\Phi _ { n } ^ { * }`$ 的四次函数并且没有导数.
然而,$`K ( \Phi , \Phi ^ { * } )`$ 中任何只含 $`\Phi _ { n }`$ 或 $`\Phi _ { n } ^ { * }`$ 的项将是手征超场, 而手征超场从定义上就没有 $`D`$ -项, 所以 $`K ( \Phi , \Phi ^ { * } )`$ 中对 $`\big [ K \big ( \Phi , \Phi ^ { * } \big ) \big ] _ { D }`$ 有贡献的项只能是那些既包含 $`\Phi _ { n }`$ 又包含 $`\Phi _ { n } ^ { * }`$ 的项.
因此 $`K ( \Phi , \Phi ^ { * } )`$ 必须是如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8155abc3ff66d9999947">
	$$
	K ( \Phi , \Phi ^ { * } ) = g _ { n m } \Phi ^ { * \, n } \Phi ^ { m } , \tag{26.4.1}
	$$
</synced_block>
它的常系数 $`g _ { n m }`$ 构成厄米矩阵.
我们现在必须要分别计算 $`f ( \Phi )`$ 的 $`\mathcal{F}`$ -分量和 $`K ( \Phi , \Phi ^ { * } )`$ 的 $`D`$ -分量.
为了计算 $`K ( \Phi , \Phi ^ { * } )`$ 的 $`D`$ -分量, 我们注意到 $`\Phi _ { n } ^ { * } \Phi _ { m }`$ 中 $`\theta`$ 的四阶项是
$$
\begin{array} { l } { { \Bigl [ \Phi _ { n } ^ { * } \Phi _ { m } \Bigr ] _ { \theta ^ { 4 } } = - \frac { 1 } { 8 } \Bigl ( \bar { \theta } \gamma _ { 5 } \theta \Bigr ) ^ { 2 } \Bigl [ \phi _ { n } ^ { * } \Box \phi _ { m } + \Bigl ( \Box \phi _ { n } ^ { * } \Bigr ) \phi _ { m } \Bigr ] } } \\ { { { } ~ + \Bigl ( \bar { \theta } \gamma _ { 5 } \theta \Bigr ) \Bigl [ \Bigl ( \overline { { { \psi _ { n } } } } \theta \Bigr ) \Bigl ( \bar { \theta } \gamma ^ { \mu } \partial _ { \mu } \psi _ { m } \Bigr ) + \Bigl ( ( \partial _ { \mu } \overline { { { \psi _ { n } } } } ) \gamma ^ { \mu } \theta \Bigr ) \Bigl ( \bar { \theta } \psi _ { m } \Bigr ) \Bigr ] } } \\ { { { } ~ + \frac { 1 } { 4 } \mathcal{F} _ { n } ^ { * } \mathcal{F} _ { m } \Bigl ( \bar { \theta } ( 1 - \gamma _ { 5 } ) \theta \Bigr ) \Bigl ( \bar { \theta } ( 1 + \gamma _ { 5 } ) \theta \Bigr ) } } \\ { { { } ~ - \frac { 1 } { 4 } \partial ^ { \mu } \phi _ { n } ^ { * } \partial ^ { \nu } \phi _ { m } \Bigl ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Bigr ) \Bigl ( \bar { \theta } \gamma _ { 5 } \gamma _ { \nu } \theta \Bigr ) ~ . } } \end{array}
$$
(26.A.18)和(26.A.19)可以让我们把这一表达式对 $`\theta`$ 的依赖关系转换成一个总因子 $`( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 }`$ :
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81678701ee7b96af9b3b">
		$$
		\Bigl ( \bar { s } s \Bigr ) ^ { 2 } = - \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } , \qquad \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \Bigr ) \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \nu } s \Bigr ) = - \eta _ { \mu \nu } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } . \tag{26.A.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81459208c3b78885c16b">
		$$
		\begin{array} { r } { ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } s \bar { s } = - \frac { 1 } { 4 } \gamma _ { 5 } ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } . } \end{array} \tag{26.A.19}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { { \displaystyle \left[ \Phi _ { n } ^ { * } \Phi _ { m } \right] _ { \theta ^ { 4 } } = - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \left[ \frac { 1 } { 2 } \phi _ { n } ^ { * } \Box \phi _ { m } + \frac { 1 } { 2 } \Big ( \Box \phi _ { n } ^ { * } \Big ) \phi _ { m } - \left( \overline { { \psi _ { n } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { m } \right) \right. } } \\ { { \displaystyle \qquad \left. + \left( \big ( \partial _ { \mu } \overline { { \psi _ { n } } } \big ) \gamma ^ { \mu } \psi _ { m } \right) + 2 \mathcal{F} _ { n } ^ { * } \mathcal{F} _ { m } - \partial ^ { \mu } \phi _ { n } ^ { * } \partial _ { \mu } \phi _ { m } \right] . } } \end{array}
$$
一个超场的 $`D`$ -项是 $`- \frac { 1 } { 4 } ( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 }`$ 的系数减去 $`\frac { 1 } { 2 } \Box`$ 作用在与 $`\theta`$ 独立的项上, 后者对于 $`\Phi _ { n } ^ { * } \Phi _ { m }`$ 就是 $`\phi _ { n } ^ { * } \phi _ { m }`$ ,所以
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81ad8582ddc12fb36aa4">
	$$
	\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } = g _ { n m } \left[ - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi ^ { m } + \mathcal{F} ^ { * \, n } \mathcal{F} ^ { m } \right. } \\ { \displaystyle \left. - \frac { 1 } { 2 } \Big ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi ^ { m } _ { L } \Big ) + \frac { 1 } { 2 } \Big ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi ^ { m } _ { L } \Big ) \right] . } \end{array} \tag{26.4.2}
	$$
</synced_block>
如果我们将 $`\Phi _ { n }`$ 写成新超场 $`\Phi _ { m } ^ { \prime }`$ 的线性组合 $`\begin{array} { r } { N _ { n } {} ^ { m } \Phi _ { m } ^ { \prime } } \end{array}`$ , 那么表示成新的超场, $`K ( \Phi , \Phi ^ { * } )`$ 与原来的在形式上的差别只是 $`g _ { n m }`$ 被换成了 $`g _ { n m } ^ { \prime } = ( N ^ { \dagger } g N ) _ { n m }`$ .
为了使标量场和旋量场的动能项在符号上和量子对易关系以及反对易关系一致, 正如 12.5节所证明的, 厄米矩阵 $`g _ { n m }`$ 必须是正定的, 这意味着我们可以选择 $`N`$ 使得 $`g _ { n m } ^ { \prime } = \delta _ { n m }`$ .
扔掉撇号, (26.4.2)现在是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81ad8582ddc12fb36aa4">
		$$
		\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } = g _ { n m } \left[ - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi ^ { m } + \mathcal{F} ^ { * \, n } \mathcal{F} ^ { m } \right. } \\ { \displaystyle \left. - \frac { 1 } { 2 } \Big ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi ^ { m } _ { L } \Big ) + \frac { 1 } { 2 } \Big ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi ^ { m } _ { L } \Big ) \right] . } \end{array} \tag{26.4.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8186a92af502fab038b4">
	$$
	\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } + \mathcal{F} ^ { * \, n } \mathcal{F} _ { n } } \\ { \displaystyle \phantom { \frac { 1 } { 2 } \Big [ } - \frac { 1 } { 2 } \Big ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Big ) + \frac { 1 } { 2 } \Big ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Big ) . } \end{array} \tag{26.4.3}
	$$
</synced_block>
我们仍然可以用一个幺正变换重新定义超场而不改变方程(26.4.3)的形式, 我们不久之后就需要使用这个自由度.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8186a92af502fab038b4">
		$$
		\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } + \mathcal{F} ^ { * \, n } \mathcal{F} _ { n } } \\ { \displaystyle \phantom { \frac { 1 } { 2 } \Big [ } - \frac { 1 } { 2 } \Big ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Big ) + \frac { 1 } { 2 } \Big ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Big ) . } \end{array} \tag{26.4.3}
		$$
	</synced_block_reference>
</callout>
方程(26.4.3)中包含 $`\phi _ { n }`$ 和 $`\psi _ { n L }`$ 的项是传统归一化复标量场和 Majorana 旋量场的正确拉格朗日量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8186a92af502fab038b4">
		$$
		\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } + \mathcal{F} ^ { * \, n } \mathcal{F} _ { n } } \\ { \displaystyle \phantom { \frac { 1 } { 2 } \Big [ } - \frac { 1 } { 2 } \Big ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Big ) + \frac { 1 } { 2 } \Big ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Big ) . } \end{array} \tag{26.4.3}
		$$
	</synced_block_reference>
</callout>
在我们可以考虑质量项后, 我们会将费米子项写成更加熟悉的形式.
在计算 $`f ( \Phi )`$ 的 $`\mathcal{F}`$ -项时, 最方便的做法是使用超场表示(26.3.21), 然后挑出 $`\theta _ { L }`$ 的二阶项:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81dab423c0265e13f79d">
		$$
		\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r l } { \Bigl [ f \Bigl ( \Phi ( x , \theta ) \Bigr ) \Bigr ] _ { \theta _ { L } ^ { 2 } } = \Bigl ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi ^ { n } _ { L } ( x ) \Bigr ) \Bigl ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi ^ { m } _ { L } ( x ) \Bigr ) \frac { \partial ^ { 2 } f \Bigl ( \phi ( x ) \Bigr ) } { \partial \phi _ { n } ( x ) \partial \phi _ { m } ( x ) } } \\ { \displaystyle \quad } & { + \mathcal{F} ^ { n } ( x ) \frac { \partial f \Bigl ( \phi ( x ) \Bigr ) } { \partial \phi _ { n } ( x ) } \Bigl ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Bigr ) . } \end{array}
$$
(我们已经这里的 $`x _ { + }`$ 替换成了 $`x`$ , 这是因为当乘以一个有两个 $`\theta _ { L }`$ 因子的式子后, 方程(26.3.21)中的 $`( \theta _ { R } ^ { \mathrm { T } } \epsilon \gamma ^ { \mu } \theta _ { L } )`$ 项为零.) 通过使用方程(26.A.11), 右边第一项对 $`\theta`$ 的依赖关系可以写成标准形式\\\*
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81dab423c0265e13f79d">
		$$
		\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8169909ed8efbe45884c">
		$$
		\begin{array} { r } { s _ { \alpha } s _ { \beta } = \frac { 1 } { 4 } ( \epsilon \gamma _ { 5 } ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma _ { 5 } s ) + \frac { 1 } { 4 } ( \gamma _ { \mu } \epsilon ) _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon \gamma ^ { \mu } s ) + \frac { 1 } { 4 } \epsilon _ { \alpha \beta } ( s ^ { \mathrm { T } } \epsilon s ) . } \end{array} \tag{26.A.11}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { { \displaystyle \left( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { n L } \right) \left( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { m L } \right) = \left( \psi _ { n L } ^ { \mathrm { T } } \epsilon \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) \theta \right) \left( \theta ^ { \mathrm { T } } \epsilon \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) \psi _ { m L } \right) } } \\ { { \displaystyle \qquad = - \frac { 1 } { 2 } \Big ( \bar { \psi } _ { n L } \psi _ { m L } \Big ) \left( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \right) . } } \end{array}
$$
任何左手征超场的 $`\mathcal{F}`$ -项是 $`\mathcal{F}`$ -项是 $`( \theta _ { L } ^ { \mathrm { { T } } } \epsilon \theta _ { L } )`$ 的系数, 所以这里有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81ed9178dcf6147e791a">
	$$
	\Big [ f ( \Phi ) \Big ] _ { \mathcal{F} } = - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \Big ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Big ) + \mathcal{F} ^ { n } \frac { \partial f ( \phi ) } { \partial \phi _ { n } } . \tag{26.4.4}
	$$
</synced_block>
完整的拉格朗日密度是(26.4.3), (26.4.4)和(26.4.4)的复共轭这三项的和:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8186a92af502fab038b4">
		$$
		\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } + \mathcal{F} ^ { * \, n } \mathcal{F} _ { n } } \\ { \displaystyle \phantom { \frac { 1 } { 2 } \Big [ } - \frac { 1 } { 2 } \Big ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Big ) + \frac { 1 } { 2 } \Big ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Big ) . } \end{array} \tag{26.4.3}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81ed9178dcf6147e791a">
		$$
		\Big [ f ( \Phi ) \Big ] _ { \mathcal{F} } = - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \Big ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Big ) + \mathcal{F} ^ { n } \frac { \partial f ( \phi ) } { \partial \phi _ { n } } . \tag{26.4.4}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r l } & { \mathcal{L} = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } + \mathcal{F} ^ { * \, n } \mathcal{F} _ { n } } \\ & { \quad \quad - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ & { \quad \quad - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) - \frac { 1 } { 2 } \Biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \Biggr ) ^ { * } \Bigl ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Bigr ) ^ { * } } \\ & { \quad \quad + \mathcal{F} ^ { n } \frac { \partial f ( \phi ) } { \partial \phi _ { n } } + \mathcal{F} ^ { * \, n } \Bigl ( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \Bigr ) ^ { * } . } \end{array}
$$
辅助场 $`\mathcal{F} _ { n }`$ 在作用量中是二次型的形式并且二次项的系数是常数, 所以通过令 $`\mathcal{F} _ { n }`$ 等于拉格朗日密度(26.4.5)相对 $`\mathcal{F} _ { n }`$ 和 $`\mathcal{F} _ { n } ^ { * }`$ 是驻定的值:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8133ad40c525f6e4f60e">
	$$
	\mathcal{F} _ { n } = - \left( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right) ^ { * } , \tag{26.4.6}
	$$
</synced_block>
我们就可以消掉它们.
将上式代入方程(26.4.5)给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f810985c8c7f06ab5a250">
	$$
	\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) - \frac { 1 } { 2 } \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) ^ { * } } \\ { \displaystyle \qquad - \biggl ( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \biggr ) ^ { * } \frac { \partial f ( \phi ) } { \partial \phi ^ { n } } . } \end{array} \tag{26.4.7}
	$$
</synced_block>
因此标量场的势是 $`\begin{array} { r } { V ( \phi ) = \left( \partial f ( \phi ) / \partial \phi _ { n } \right) ^ { * } \partial f ( \phi ) / \partial \phi ^ { n } } \end{array}`$ .
当辅助场以这种方式被消除后, 在剩下的场 $`\psi _ { n L }`$ 和 $`\phi _ { n }`$ 的超对称变换(26.3.15)和(26.3.17)下
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
$$
\delta \psi _ { n L } = \sqrt 2 \partial _ { \mu } \phi _ { n } \gamma ^ { \mu } \alpha _ { R } - \sqrt 2 \biggl ( { \frac { \partial f ( \phi ) } { \partial \phi _ { n } } } \biggr ) ^ { * } \alpha _ { L } , \qquad \delta \phi _ { n } = \sqrt 2 \biggl ( { \overline { { \alpha _ { R } } } } \psi _ { n L } \biggr ) ,
$$
作用量不再是不变的.
原因是: 表达式(26.4.6)不在服从(26.3.16)给出的 $`\mathcal{F} _ { n }`$ 的变换规则 $`\delta \mathcal{F} _ { n } ~ =`$ $`\sqrt { 2 } ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { n L } )`$ , 而是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8133ad40c525f6e4f60e">
		$$
		\mathcal{F} _ { n } = - \left( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right) ^ { * } , \tag{26.4.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
$$
\delta \biggl ( - \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \biggr ) ^ { * } = - \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \delta \phi ^ { * \, m } = - \sqrt { 2 } \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \Bigl ( \overline { { \alpha _ { L } } } \psi ^ { m } _ { R } \Bigr ) .
$$
由于相同的原因, 在消掉辅助场后, $`\phi _ { n }`$ 和 $`\psi _ { n L }`$ 的超对称变换的对易子不再由超对称反对易关系给定, 事实上, 它们并没有形成封闭的Lie超代数.
但这并不与存在满足超对称反对易关系的量子力学算符 $`Q _ { \alpha }`$ 相矛盾.
这些算符生成了超对称变换, 也就是说, $`- \mathrm{i} ( \bar { \alpha } Q )`$ 与任何 Heisenberg 绘景量子场 $`\phi _ { n }`$ 或 $`\psi _ { n L }`$ 的对易子等于这个场在无限小参量为 $`\alpha`$ 的超对称变换下的变化.
当 $`\mathcal{F} _ { n }`$ 由方程(26.4.6) 给定后, $`- \mathrm{i} ( \bar { \alpha } Q )`$ 与 $`\mathcal{F} _ { n }`$ 的对易子由 $`\delta \mathcal{F} _ { n } = \sqrt { 2 } ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { n L } )`$ 给定, 这是因为, 在 Heisenberg 绘景下, 量子场 $`\psi _ { n L }`$ 满足从拉格朗日量(26.4.7)导出的场方程:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8133ad40c525f6e4f60e">
		$$
		\mathcal{F} _ { n } = - \left( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right) ^ { * } , \tag{26.4.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f810985c8c7f06ab5a250">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) - \frac { 1 } { 2 } \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) ^ { * } } \\ { \displaystyle \qquad - \biggl ( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \biggr ) ^ { * } \frac { \partial f ( \phi ) } { \partial \phi ^ { n } } . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
$$
\not\!\partial\, \psi _ { n L } = - \Biggl ( { \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } } \Biggr ) ^ { * } \psi ^ { m } _ { R } .
$$
同样的, 当把场方程考虑在内后, 量子场 $`\phi _ { n }`$ 和 $`\psi _ { n L }`$ 的超对称变换确实构成封闭的 Lie 超代数.
这样的代数通常被称作是在壳的.
标量场 $`\phi _ { n }`$ 的零阶期望值 $`\phi _ { n 0 }`$ 必须处在方程(26.4.7)最后一项的极大值点处.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f810985c8c7f06ab5a250">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) - \frac { 1 } { 2 } \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) ^ { * } } \\ { \displaystyle \qquad - \biggl ( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \biggr ) ^ { * } \frac { \partial f ( \phi ) } { \partial \phi ^ { n } } . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
由于这一项不是负的就是零, 时空独立的场值 $`\phi _ { n 0 }`$ 使得最大值为零, 这使得
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8175ad30c66dbd5d3947">
	$$
	\left. \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right| _ { \phi = \phi _ { 0 } } = 0 , \tag{26.4.8}
	$$
</synced_block>
当然前提是假定这个方程存在解.
方程(26.4.8)不仅使得方程(26.4.7)的最后一项取最大值——它也是超对称性不破缺的条件.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8175ad30c66dbd5d3947">
		$$
		\left. \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right| _ { \phi = \phi _ { 0 } } = 0 , \tag{26.4.8}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f810985c8c7f06ab5a250">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) - \frac { 1 } { 2 } \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) ^ { * } } \\ { \displaystyle \qquad - \biggl ( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \biggr ) ^ { * } \frac { \partial f ( \phi ) } { \partial \phi ^ { n } } . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
真空在超对称变换下不变这个要求使得任何场在超对称变换下的变分的真空期望值应该为零.
玻色场的变分是费米场, 它的真空期望值显然总是为零, 当方程(26.3.15)表明 $`\delta \psi _ { n L }`$ 的真空期望值正比于辅助场 $`\mathcal{F} _ { n }`$ 的真空期望值, 如果超对称性不破缺, 它因此必须为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
根据方程(26.4.6), 在零阶微扰论中, 这个条件要求方程(26.4.8)必须被满足.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8133ad40c525f6e4f60e">
		$$
		\mathcal{F} _ { n } = - \left( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right) ^ { * } , \tag{26.4.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8175ad30c66dbd5d3947">
		$$
		\left. \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right| _ { \phi = \phi _ { 0 } } = 0 , \tag{26.4.8}
		$$
	</synced_block_reference>
</callout>
在 27.6 节我们会看到, 如果方程(26.4.8)是被满足的, 那么超对称性直到微扰论的所有阶都是不破缺的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8175ad30c66dbd5d3947">
		$$
		\left. \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right| _ { \phi = \phi _ { 0 } } = 0 , \tag{26.4.8}
		$$
	</synced_block_reference>
</callout>
对于一个左手征标量场 $`\Phi`$ , 代数基本定理告诉我们多项式 $`\partial f ( \phi ) / \partial \phi`$ 总是在复平面上的某处至少有一个解.
当超场的个数不止一个时, 这是不一定的.
如果我们假定方程(26.4.8)存在一个解 $`\phi _ { n 0 }`$ , 通过令
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8175ad30c66dbd5d3947">
		$$
		\left. \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \right| _ { \phi = \phi _ { 0 } } = 0 , \tag{26.4.8}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81d3a84bfddc6604d7b4">
	$$
	\phi _ { n } = \phi _ { n 0 } + \varphi _ { n } , \tag{26.4.9}
	$$
</synced_block>
并对 $`\varphi _ { n }`$ 做幂级数展开, 我们可以计算出这个理论的物理自由度.
通过观察 $`\phi`$ 和 $`\psi`$ 的二阶项, 我们可以计算出这个理论中的粒子质量:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f815db30ed8eddb989c4f">
	$$
	\begin{array} { r l } { \mathcal{L} _ { 0 } = - \partial _ { \mu } \varphi ^ { * \, n } \partial ^ { \mu } \varphi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( \partial _ { \mu } \bigl ( \overline { { \psi ^ { n } _ { L } } } \bigr ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { - \displaystyle \frac { 1 } { 2 } \mathcal{M} _ { n m } \Bigl ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Bigr ) - \frac { 1 } { 2 } \mathcal{M} _ { n m } ^ { * } \Bigl ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Bigr ) ^ { * } } \\ { - \displaystyle \Bigl ( \mathcal{M} ^ { \dagger } \mathcal{M} \Bigr ) _ { m n } \varphi ^ { * \, m } \varphi ^ { n } , } \end{array} \tag{26.4.10}
	$$
</synced_block>
其中 $`\mathcal{M}`$ 是对称复矩阵
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81c59c4ef3f2f382197d">
	$$
	\mathcal{M} _ { m n } \equiv \left( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \right) _ { \phi = \phi _ { 0 } } . \tag{26.4.11}
	$$
</synced_block>
现在, 如果我们通过一个幺正变换重新定义这些场
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f819995f3c8df52d43841">
	$$
	\varphi _ { n } = \mathcal{U} _ { n } {} ^ { m } \varphi _ { m } ^ { \prime } , \qquad \psi _ { n L } = \mathcal{U} _ { n } {} ^ { m } \psi _ { m L } ^ { \prime } , \tag{26.4.12}
	$$
</synced_block>
自由场拉格朗日量(26.4.10)的形式不会因此改变, 但是要把 $`\mathcal{M}`$ 换成 $`{ \mathcal{M} } ^ { \prime }`$ , 其中
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f815db30ed8eddb989c4f">
		$$
		\begin{array} { r l } { \mathcal{L} _ { 0 } = - \partial _ { \mu } \varphi ^ { * \, n } \partial ^ { \mu } \varphi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( \partial _ { \mu } \bigl ( \overline { { \psi ^ { n } _ { L } } } \bigr ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { - \displaystyle \frac { 1 } { 2 } \mathcal{M} _ { n m } \Bigl ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Bigr ) - \frac { 1 } { 2 } \mathcal{M} _ { n m } ^ { * } \Bigl ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Bigr ) ^ { * } } \\ { - \displaystyle \Bigl ( \mathcal{M} ^ { \dagger } \mathcal{M} \Bigr ) _ { m n } \varphi ^ { * \, m } \varphi ^ { n } , } \end{array} \tag{26.4.10}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f816d8580d9f0a0359a8d">
	$$
	\mathcal{M} ^ { \prime } = \mathcal{U} ^ { \mathrm { T } } \mathcal{M} \mathcal{U} . \tag{26.4.13}
	$$
</synced_block>
根据矩阵代数的一个定理, 对于任何复对称矩阵 $`\mathcal{M}`$ , 总能找到一个幺正矩阵 $`\boldsymbol { \mathcal U }`$ 使得方程(26.4.13)定义的矩阵 $`{ \mathcal{M} } ^ { \prime }`$ 是对角矩阵且矩阵元为正实数 $`m _ { n }`$ ; below we write the corresponding diagonal symmetric mass tensor as $`m _ { n m }`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f816d8580d9f0a0359a8d">
		$$
		\mathcal{M} ^ { \prime } = \mathcal{U} ^ { \mathrm { T } } \mathcal{M} \mathcal{U} . \tag{26.4.13}
		$$
	</synced_block_reference>
</callout>
(为了将来的使用, 我们注意到 $`\mathcal{M} ^ { \prime \dagger } \mathcal{M} ^ { \prime } =`$ $`\mathcal{U} ^ { \dag } \mathcal{M} ^ { \dag } \mathcal{M} \mathcal{U}`$ , 所以 $`m _ { n } ^ { 2 }`$ 就是正定厄米矩阵 $`\mathcal{M} ^ { \dagger } \mathcal{M}`$ 的本征值.) 以这种方式重新定义场并扔掉撇号,拉格朗日量的二次部分现在是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f816f8280fc33553a6012">
	$$
	\begin{array} { l } { { \displaystyle { \mathcal{L} } _ { 0 } = - \partial _ { \mu } \varphi ^ { * \, n } \partial ^ { \mu } \varphi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { { \psi ^ { n } _ { L } } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( \partial _ { \mu } \bigl ( \overline { { { \psi ^ { n } _ { L } } } } \bigr ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } } \\ { { \displaystyle ~ - \frac { 1 } { 2 } m _ { n m } \Bigl ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Bigr ) - \frac { 1 } { 2 } m _ { n m } ^ { * } \Bigl ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Bigr ) ^ { * } } } \\ { { \displaystyle ~ - \Bigl ( m ^ { \dagger } m \Bigr ) _ { n } {} ^ { m } \varphi ^ { * \, n } \varphi _ { m } . } } \end{array} \tag{26.4.14}
	$$
</synced_block>
为了将费米子质量项变成更加熟悉的形式, 我们引入作为 Majorana 场定义的场 $`\psi _ { n } ( x )`$ , 它的左手分量是 $`\psi _ { n L } ( x )`$ .
那么利用 Majorana 双线性型的对称性质(26.A.7):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f812dbfd2df88f108bb3b">
		$$
		( \overline { { { s _ { 1 } } } } M s _ { 2 } ) = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = 1 , \gamma _ { 5 } \gamma _ { \mu } , \gamma _ { 5 } } } \\ { { - ( \overline { { { s _ { 2 } } } } M s _ { 1 } ) } } & { { \qquad M = \gamma _ { \mu } , [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \end{array} \right. . \tag{26.A.7}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { { \displaystyle - \frac { 1 } { 2 } \Big ( \overline { { { \psi _ { n L } } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Big ) + \frac { 1 } { 2 } \Big ( \partial _ { \mu } ( \overline { { { \psi _ { n L } } } } ) \gamma ^ { \mu } \psi _ { n L } \Big ) } } \\ { { \displaystyle \quad = - \frac { 1 } { 2 } \Big ( \overline { { { \psi _ { n } } } } \gamma ^ { \mu } \Big ( \frac { 1 + \gamma _ { 5 } } { 2 } \Big ) \partial _ { \mu } \psi _ { n } \Big ) + \frac { 1 } { 2 } \Big ( \partial _ { \mu } ( \overline { { { \psi _ { n } } } } ) \gamma ^ { \mu } \Big ( \frac { 1 + \gamma _ { 5 } } { 2 } \Big ) \psi _ { n } \Big ) } } \\ { { \displaystyle \quad = - \frac { 1 } { 2 } \Big ( \overline { { { \psi _ { n } } } } \gamma ^ { \mu } \Big ( \frac { 1 + \gamma _ { 5 } } { 2 } \Big ) \partial _ { \mu } \psi _ { n } \Big ) - \frac { 1 } { 2 } \Big ( \overline { { { \psi _ { n } } } } \gamma ^ { \mu } \Big ( \frac { 1 - \gamma _ { 5 } } { 2 } \Big ) \partial _ { \mu } \psi _ { n } \Big ) } } \\ { { \displaystyle \quad = - \frac { 1 } { 2 } \Big ( \overline { { { \psi _ { n } } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n } \Big ) , } } \end{array}
$$
而实性质(26.A.21)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8158a2fdc1adcd361128">
		$$
		( \overline { { { s _ { 1 } } } } M s _ { 2 } ) ^ { * } = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = 1 , \ \gamma _ { \mu } , \ [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \\ { { - ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = \gamma _ { \mu } \gamma _ { 5 } , \ \gamma _ { 5 } } } \end{array} \right. . \tag{26.A.21}
		$$
	</synced_block_reference>
</callout>
$$
\left( \bar { \psi } _ { n L } \psi _ { n L } \right) + \left( \bar { \psi } _ { n L } \psi _ { n L } \right) ^ { * } = 2 \operatorname{Re} \left( \overline { { \psi _ { n } } } \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) \psi _ { n } \right) = \left( \overline { { \psi _ { n } } } \psi _ { n } \right) .
$$
这样, 完整的二次拉格朗日量就是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81ea9a1ac67293b17046">
	$$
	\begin{array} { l } { { \displaystyle { \mathcal{L} } _ { 0 } = - \partial _ { \mu } \varphi ^ { * \, n } \partial ^ { \mu } \varphi _ { n } - \Bigl ( m ^ { \dagger } m \Bigr ) _ { n } {} ^ { m } \varphi ^ { * \, n } \varphi _ { m } } } \\ { { \displaystyle ~ - \frac { 1 } { 2 } \Big ( \overline { { { \psi ^ { n } } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n } \Big ) - \frac { 1 } { 2 } m _ { n m } \Big ( \overline { { { \psi ^ { n } } } } \psi ^ { m } \Big ) ~ . } } \end{array} \tag{26.4.15}
	$$
</synced_block>
费米子项前面有因子 $`1 / 2`$ 是因为它们是 Majorana 费米场, 而标量项前面没有因子 $`1 / 2`$ 是因为它们是复标量.
我们看到无自旋粒子和自旋 $`1 / 2`$ 粒子有相等的质量 $`m _ { n }`$ , 这正是该理论的未破缺超对称性所要求的.
拉格朗日密度中的相互作用部分 $`{ \mathcal{L} } ^ { \prime }`$ 由方程(26.4.7)中比 $`\varphi _ { n }`$ 和 $`\psi _ { n }`$ 的二阶项还要高阶的项给定.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f810985c8c7f06ab5a250">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) - \frac { 1 } { 2 } \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) ^ { * } } \\ { \displaystyle \qquad - \biggl ( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \biggr ) ^ { * } \frac { \partial f ( \phi ) } { \partial \phi ^ { n } } . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
由于超势 $`f ( \phi _ { 0 } + \varphi )`$ 被假定是三次多项式且在 $`\varphi _ { n } ~ = ~ 0`$ 处驻定, 而 $`\varphi`$ 的定义又使得二阶项是$`{ \begin{array} { l } { { \frac { 1 } { 2 } } m _ { n m } \varphi ^ { n } \varphi ^ { m } } \end{array} }`$ , 我们可以将超势(除了一个不重要的常数项以外的部分)写成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8192adc8c2c6c4f9d65a">
	$$
	f ( \phi _ { 0 } + \varphi ) = \frac { 1 } { 2 } m _ { n m } \varphi ^ { n } \varphi ^ { m } + \frac { 1 } { 6 } f _ { n m \ell } \varphi ^ { n } \varphi ^ { m } \varphi ^ { \ell } . \tag{26.4.16}
	$$
</synced_block>
在方程(26.4.7)中使用上式就给出了相互作用
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f810985c8c7f06ab5a250">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi _ { n } - \frac { 1 } { 2 } \Bigl ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n L } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi _ { n L } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) - \frac { 1 } { 2 } \biggl ( \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \biggr ) ^ { * } \left( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \right) ^ { * } } \\ { \displaystyle \qquad - \biggl ( \frac { \partial f ( \phi ) } { \partial \phi _ { n } } \biggr ) ^ { * } \frac { \partial f ( \phi ) } { \partial \phi ^ { n } } . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { { \displaystyle { \mathcal{L} } ^ { \prime } = - \frac { 1 } { 2 } f _ { n m \ell } \varphi ^ { n } \left( \overline { { { \psi ^ { m } } } } \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) \psi ^ { \ell } \right) } } \\ { { \displaystyle ~ - \frac { 1 } { 2 } f _ { n m \ell } ^ { * } \varphi ^ { * \, n } \left( \overline { { { \psi ^ { m } } } } \left( \frac { 1 - \gamma _ { 5 } } { 2 } \right) \psi ^ { \ell } \right) } } \\ { { \displaystyle ~ - \frac { 1 } { 2 } m ^ { * \, p } {} _ { n } f _ { p m \ell } \varphi ^ { * \, n } \varphi ^ { m } \varphi ^ { \ell } - \frac { 1 } { 2 } m ^ { p } {} _ { n } f _ { p m \ell } ^ { * } \varphi ^ { n } \varphi ^ { * \, m } \varphi ^ { * \, \ell } } } \\ { { \displaystyle ~ - \frac { 1 } { 4 } f ^ { * \, n } {} _ { p q } f _ { n m \ell } \varphi ^ { m } \varphi ^ { \ell } \varphi ^ { * \, p } \varphi ^ { * \, q } . } } \end{array}
$$
我们看到, 知道了质量 $`m _ { n }`$ 以及标量和费米子的 “Yukawa” 耦合 $`f _ { n m l }`$ 就足以定出无自旋场的所有三次项和四次自对偶耦合.
作为一个例子, 考察只有一个左手征超场的情况.
为了与前面的结果进行对比, 我们将方程(26.4.16)中的单个系数 $`f`$ 写成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8192adc8c2c6c4f9d65a">
		$$
		f ( \phi _ { 0 } + \varphi ) = \frac { 1 } { 2 } m _ { n m } \varphi ^ { n } \varphi ^ { m } + \frac { 1 } { 6 } f _ { n m \ell } \varphi ^ { n } \varphi ^ { m } \varphi ^ { \ell } . \tag{26.4.16}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81e28fb3d3bc3aa2d0a9">
	$$
	f \equiv 2 \sqrt { 2 } \mathrm{e} ^ { \mathrm{i} \alpha } \lambda , \tag{26.4.18}
	$$
</synced_block>
其中 $`\lambda`$ 是实的而 $`\alpha`$ 是某个实相位.
我们同时还会引入一对无自旋实场 $`A ( x )`$ 和 $`B ( x )`$ , 方法是将这里的单个复标量写成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81339dcdc4357a480206">
	$$
	\varphi \equiv \mathrm{e} ^ { - \mathrm{i} \alpha } \left( { \frac { A + \mathrm{i} B } { \sqrt { 2 } } } \right) . \tag{26.4.19}
	$$
</synced_block>
这样, 方程(26.4.15)和(26.4.17)就给出了整个拉格朗日密度
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81ea9a1ac67293b17046">
		$$
		\begin{array} { l } { { \displaystyle { \mathcal{L} } _ { 0 } = - \partial _ { \mu } \varphi ^ { * \, n } \partial ^ { \mu } \varphi _ { n } - \Bigl ( m ^ { \dagger } m \Bigr ) _ { n } {} ^ { m } \varphi ^ { * \, n } \varphi _ { m } } } \\ { { \displaystyle ~ - \frac { 1 } { 2 } \Big ( \overline { { { \psi ^ { n } } } } \gamma ^ { \mu } \partial _ { \mu } \psi _ { n } \Big ) - \frac { 1 } { 2 } m _ { n m } \Big ( \overline { { { \psi ^ { n } } } } \psi ^ { m } \Big ) ~ . } } \end{array} \tag{26.4.15}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f81ff80fee631e72db7c3">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { \mathcal{L} = - \frac { 1 } { 2 } \partial _ { \mu } A \partial ^ { \mu } A - \frac { 1 } { 2 } \partial _ { \mu } B \partial ^ { \mu } B - \frac { 1 } { 2 } m ^ { 2 } \left( A ^ { 2 } + B ^ { 2 } \right) } } \\ { { } } & { { } } & { { - \frac { 1 } { 2 } \Big ( \bar { \psi } \gamma ^ { \mu } \partial _ { \mu } \psi \Big ) - \frac { 1 } { 2 } m \left( \bar { \psi } \psi \right) } } \\ { { } } & { { } } & { { - \lambda A \left( \bar { \psi } \psi \right) - \mathrm{i} \lambda B \left( \bar { \psi } \gamma _ { 5 } \psi \right) } } \\ { { } } & { { } } & { { - m \lambda A \left( A ^ { 2 } + B ^ { 2 } \right) - \frac { 1 } { 2 } \lambda ^ { 2 } \left( A ^ { 2 } + B ^ { 2 } \right) ^ { 2 } . } } \end{array} \tag{26.4.20}
	$$
</synced_block>
它与Wess和Zumino最初发现的拉格朗日密度(24.2.9)是相同的.\[2\] 在这个简单情况中值得注意的是, 即使我们不假定宇称守恒再进行推导, 拉格朗日量现在在如下的空间反演变换下是不变的:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- J. Wess and B. Zumino, Nucl. Phys. B70, 13 (1974). 这篇文章重印于Supersymmetry, 参考文献\[1\]
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b#34cee2b74b3f8184bb9cdefd5cebe353">
	$$
	A ( x ) \to A ( \Lambda _ { P } x ) , \qquad B ( x ) \to - B ( \Lambda _ { P } x ) , \qquad \psi ( x ) \to \mathrm{i} \beta \psi ( \Lambda _ { P } x ) . \tag{26.4.21}
	$$
</synced_block>
宇称守恒作为“偶然”对称性出现是各种可重整规范理论熟悉的特征(参看 12.5 节和 18.7 节), 但是它不是涉及无自旋场的理论的特征, 所以这是超对称性在单个标量超场的可重整理论中的特殊结果.
</content>
</page>
