Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88 as of 2026-06-30T03:55:32.535Z:
<page url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.1 手征超场的规范不变作用量"}
</properties>
<content>
考虑一组保持超对称性生成元 $`Q`$ 不变的阿贝尔或非阿贝尔规范变换.
(简单超对称性只有一个Majorana旋量超对称性生成元, 对于任何半单规范群, 它只能构成这个群的平庸表示.) 同一个超多重态中的各个分量场在这种规范变换下必须以相同的方式变换.
特别地, 对于一个左手征超场, 我们有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f819b8a10e077207d8cf8">
	$$
	\begin{array}{l}
\displaystyle \phi^n(x)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x)\bigr)\bigr]^n{}_m\phi^m(x),\\
\displaystyle \psi^n_L(x)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x)\bigr)\bigr]^n{}_m\psi^m_L(x),\\
\displaystyle \mathcal F^n(x)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x)\bigr)\bigr]^n{}_m\mathcal F^m(x).
\end{array}\tag{27.1.1}
	$$
</synced_block>
其中 $`t _ { A }`$ 是代表规范代数生成元的厄米矩阵, $`\Lambda ^ { A } ( x )`$ 是 $`x ^ { \mu }`$ 的实函数, 参数化了一个有限大的规范变换.
(我们对规范变换函数使用的符号约定几乎与15.1节相同, 不同之处只有, 为了避免与Dirac指标产生混淆, 取代 $`\alpha , \beta`$ 等, 我们用字母 $`A , B`$ 等来标记规范生成元和规范变换参量.)
左手征超场(26.3.11)包含一些分量场的导数, 所以它的变换要比方程(27.1.1)复杂.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f819b8a10e077207d8cf8">
		$$
		\begin{array}{l}
\displaystyle \phi^n(x)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x)\bigr)\bigr]^n{}_m\phi^m(x),\\
\displaystyle \psi^n_L(x)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x)\bigr)\bigr]^n{}_m\psi^m_L(x),\\
\displaystyle \mathcal F^n(x)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x)\bigr)\bigr]^n{}_m\mathcal F^m(x).
\end{array}\tag{27.1.1}
		$$
	</synced_block_reference>
</callout>
然而, 方程(26.3.21)表明, 如果用 $`\theta _ { L }`$ 和方程(26.3.23)定义的变量 $`x _ { + }`$ 表示超场, 那么超场中就没有导数.
因此它有变换规则
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f819189d2e31f920550fc">
	$$
	\Phi^n(x,\theta)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x_+)\bigr)\bigr]^n{}_m\Phi^m(x,\theta).\tag{27.1.2}
	$$
</synced_block>
如果作用量中的一项只依赖左手征超场而不依赖左手征超场的导数或者复共轭,例如方程(26.3.30)中的 $`\textstyle \int \mathrm { d } ^ { 4 } x [ f ( \Phi ) ] _ { \mathcal{F} }`$ , 那么只要它在 $`\Lambda ^ { A } ( x )`$ 与 $`x ^ { \mu }`$ 无关的整体规范变换下不变, 那么它(和它的复共轭)在定域规范变换下不变.
在手征超场的可重整理论中引入规范场的需求仅来源于既包含 $`\Phi^n`$ 又包含 $`\Phi^\dagger_n`$ 的 $`D`$-项.
因为矩阵 $`t _ { A }`$ 是厄米的, 所以方程(27.1.2)的厄米伴是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f819189d2e31f920550fc">
		$$
		\Phi^n(x,\theta)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x_+)\bigr)\bigr]^n{}_m\Phi^m(x,\theta).\tag{27.1.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81df9e57d6bbbaf40f11">
	$$
	\Phi^\dagger_n(x,\theta)\to \Phi^\dagger_m(x,\theta)\bigl[\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\bigr]^m{}_n.\tag{27.1.3}
	$$
</synced_block>
要不是 $`\Lambda ^ { A } ( x _ { + } ) ^ { * } = \Lambda ^ { A } ( x _ { - } )`$ 和 $`\Lambda ^ { A } ( x _ { + } )`$ 之间有差异, 这几乎就是说 $`\Phi ^ { \dagger }`$ 变换遵循的规范群表示与 $`\Phi`$ 构成的表示逆步, 以及对于 $`\Phi`$ 和 $`\Phi ^ { \dagger }`$ 的任意函数, 只要它在整体规范变换下不变, 那么它就在定域
规范变换下不变.
由于 $`x _ { + }`$ 和 $`x _ { - }`$ 不同, 我们必须引入有如下变换性质的规范联络矩阵 $`\Gamma _ { n m } ( x , \theta )`$ ,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
	$$
	\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
	$$
</synced_block>
这样, 通过给 $`\Phi ^ { \dagger }`$ 右乘 $`\Gamma`$ , 我们就获得了有如下变换性质的超场
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81a39d65c1044c754551">
	$$
	\bigl[\Phi^\dagger(x,\theta)\Gamma(x,\theta)\bigr]_n\to \bigl[\Phi^\dagger(x,\theta)\Gamma(x,\theta)\bigr]_m\bigl[\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr)\bigr]^m{}_n.\tag{27.1.5}
	$$
</synced_block>
这使得任何用 $`\Phi`$ 和 $`\Phi ^ { \dagger } \Gamma`$ (不包含它们的导数或复共轭)构建的整体规格不变函数同时也是定域规范不变的.
一个显然的例子是 26.4 节中构建的拉格朗日量中 $`D`$ -项的规范不变版本 $`( \Phi ^ { \dag } \Gamma \Phi ) _ { D }`$ .
任何像方程(27.1.4)那样变换的 $`\Gamma ( x , \theta )`$ 都能让我们构建手征超场的规范不变拉格朗日量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
		$$
	</synced_block_reference>
</callout>
选择不是唯一的; 如果 $`\Gamma`$ 像方程(27.1.4)那样变换, 我们给它右乘一个有如下变换性质的左手征超场 $`\Upsilon _ { L }`$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
		$$
	</synced_block_reference>
</callout>
$$
\Upsilon_L(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)\bigr)\Upsilon_L(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr),
$$
那么我们就得到了一个也满足方程(27.1.4)的新规范联络.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
		$$
	</synced_block_reference>
</callout>
一种简化方式是把 $`\Gamma ( x , \theta )`$ 取成厄米的:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f8167a208c09120c4aef8">
	$$
	\Gamma ^ { \dagger } ( x , \theta ) = \Gamma ( x , \theta ) . \tag{27.1.6}
	$$
</synced_block>
这总是可能的: 如果存在任何满足方程(27.1.4)的 $`\Gamma ( x , \theta )`$ , 那么通过取方程(27.1.4)的厄米伴, 我们可以很容易地看到 $`\Gamma ^ { \dagger } ( x , \theta )`$ 的变换方式与 $`\Gamma ( x , \theta )`$ 相同, 所以, 如果 $`\Gamma ( x , \theta )`$ 不是厄米的, 我们就可以用它的厄米部分 $`( \Gamma + \Gamma ^ { \dagger } ) / 2`$ 替换它(如果这部分为零, 那么就用反厄米部分 $`( \Gamma - \Gamma ^ { \dagger } ) / 2 \mathrm{i}`$ 替换它.)另一个有重要物理意义的简化是将 $`\Gamma ( x , \theta )`$ 表示成那些规范变换性质不依赖于超场 $`\Phi ( x , \theta )`$ 所属的规范代数特定表示 $`t _ { A }`$ 的场, 这使得对于按照规范群的任意表示变换的手征超场, 这些场可以被用来构造一个合适的 $`\Gamma ( x , \theta )`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
		$$
	</synced_block_reference>
</callout>
对于这个目的, 回忆起Baker-Hausdorff公式是有用的, 这一公式表述了, 对于任意矩阵 $`a`$ 和 $`b`$ ,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81639d29ea4b0e142e07">
	$$
	\begin{array} { r } { \mathrm{e} ^ { a } \mathrm{e} ^ { b } = \exp \left( a + b + \frac { 1 } { 2 } [ a , b ] + \frac { 1 } { 1 2 } [ a , [ a , b ] ] + \frac { 1 } { 1 2 } [ b , [ b , a ] ] + \cdots \right) , } \end{array} \tag{27.1.7}
	$$
</synced_block>
其中“· · · ”表示可以被写为 $`a`$ 和 $`b`$ 的多重对易子的高阶项, 其中的二阶项和三阶项已经显式地写出来.
由此得出, 对于一个Lie代数的任意表示, 我们有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81c4b1d9e40d4779c8f3">
	$$
	\exp \Bigl ( a ^ { A } t _ { A } \Bigr ) \exp \Bigl ( b ^ { A } t _ { A } \Bigr ) = \exp \Bigl ( f ^ { A } ( a , b ) t _ { A } \Bigr ) , \tag{27.1.8}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81c5b0fadc1fccdeba04">
	$$
	\begin{array} { l } { { f ^ { A } ( a , b ) = a ^ { A } + b ^ { A } + { \frac { 1 } { 2 } } \mathrm{i} C ^ { A } { } _ { B C } a ^ { B } b ^ { C } - { \frac { 1 } { 1 2 } } C ^ { A } { } _ { B C } C ^ { C } { } _ { D E } a ^ { B } a ^ { D } b ^ { E } } } \\ { { \mathrm { } - { \frac { 1 } { 1 2 } } C ^ { A } { } _ { B C } C ^ { C } { } _ { D E } b ^ { B } b ^ { D } a ^ { E } + \cdots , } } \end{array} \tag{27.1.9}
	$$
</synced_block>
它通过结构常数 $`C ^ { A } { } _ { B C }`$ 依赖于这个 Lie 代数, 结构常数像往常一样定义成
$$
[ t _ { B } , t _ { C } ] = \mathrm{i} C ^ { A } { } _ { B C } t _ { A } ,
$$
但是它不依赖由 $`t _ { A }`$ 构成的特定表示.
我们将取 $`\Gamma ( x , \theta )`$ 为如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f813082f7cda768cfc371">
	$$
	\Gamma ( x , \theta ) = \exp \left( - 2 t _ { A } V ^ { A } ( x , \theta ) \right) , \tag{27.1.10}
	$$
</synced_block>
其中 $`V ^ { A } ( x , \theta )`$ 是一组实超场(这使得 $`\Gamma`$ 是厄米的), 它们不依赖由 $`t _ { A }`$ 构成的规范代数表示.
注意到超对称规范理论有一个额外的对称性, 它使我们能够进一步做一个重要的简化.
如果 $`\Phi`$ 和 $`\Phi ^ { \dagger } \Gamma`$ 在整体规范变换下不变, 那么它不仅自动在定域规范变换下不变, 同时也在一个更大的扩充规范变换
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81068ac6c75fc398e24f">
	$$
	\Phi^n_L(x,\theta)\to \bigl[\exp\bigl(\mathrm{i}t_A\Omega^A(x,\theta)\bigr)\bigr]^n{}_m\Phi^m_L(x,\theta).\tag{27.1.11}
	$$
</synced_block>
和
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81d0a062f562ed48d849">
	$$
	\Gamma(x,\theta)\to \exp\bigl(-\mathrm{i}t_A\Omega^A(x,\theta)\bigr)\Gamma(x,\theta)\exp\bigl(+\mathrm{i}t_A\Omega^A(x,\theta)^*\bigr).\tag{27.1.12}
	$$
</synced_block>
下不变, 其中 $`\Omega ^ { A } ( x , \theta )`$ 是一个任意的左手征超场——即, $`\theta _ { L }`$ 和 $`x _ { + }`$ 的一个任意函数.
在这个变换下,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81e2aaf6fb19a10c5a0b">
	$$
	V^A(x,\theta)\to V^A(x,\theta)+\frac{\mathrm{i}}{2}\bigl[\Omega^A(x,\theta)-\Omega^A(x,\theta)^*\bigr]+\cdots.\tag{27.1.13}
	$$
</synced_block>
其中“· · ·”代表的项来自方程(27.1.7)中的对易子, 它们是规范耦合常数的一阶项或高阶项.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81639d29ea4b0e142e07">
		$$
		\begin{array} { r } { \mathrm{e} ^ { a } \mathrm{e} ^ { b } = \exp \left( a + b + \frac { 1 } { 2 } [ a , b ] + \frac { 1 } { 1 2 } [ a , [ a , b ] ] + \frac { 1 } { 1 2 } [ b , [ b , a ] ] + \cdots \right) , } \end{array} \tag{27.1.7}
		$$
	</synced_block_reference>
</callout>
作为一个一般的左手征超场, $`\Omega`$ 可以写成(26.3.11)的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81069cbfcfe23b6b40a3">
	$$
	\begin{array}{l}
\Omega^A(x,\theta)=W^A(x)-\sqrt2\left(\bar\theta\frac{1+\gamma_5}{2}w^A(x)\right)+\mathcal W^A(x)\left(\bar\theta\frac{1+\gamma_5}{2}\theta\right)\\
\qquad+\frac12(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu W^A(x)-\frac1{\sqrt2}(\bar\theta\gamma_5\theta)\left(\bar\theta\not\partial\frac{1+\gamma_5}{2}w^A(x)\right)\\
\qquad-\frac18(\bar\theta\gamma_5\theta)^2\Box W^A(x).
\end{array}\tag{27.1.14}
	$$
</synced_block>
其中 $`W ^ { A } ( x )`$ 和 $`\mathcal{W} ( x )`$ 是 $`x ^ { \mu }`$ 的任意复函数, 并且我们引入了 Majorana 旋量 $`w ^ { A } ( x )`$ , 定义它成使得超场的左手旋量部分是 $`{ \textstyle \frac { 1 } { 2 } } ( 1 + \gamma _ { 5 } ) w ^ { A } ( x )`$ .
利用 Majorana 双线性型的复共轭性质(26.A.21), 方程(27.1.14)的复共轭给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81069cbfcfe23b6b40a3">
		$$
		\begin{array}{l}
\Omega^A(x,\theta)=W^A(x)-\sqrt2\left(\bar\theta\frac{1+\gamma_5}{2}w^A(x)\right)+\mathcal W^A(x)\left(\bar\theta\frac{1+\gamma_5}{2}\theta\right)\\
\qquad+\frac12(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu W^A(x)-\frac1{\sqrt2}(\bar\theta\gamma_5\theta)\left(\bar\theta\not\partial\frac{1+\gamma_5}{2}w^A(x)\right)\\
\qquad-\frac18(\bar\theta\gamma_5\theta)^2\Box W^A(x).
\end{array}\tag{27.1.14}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f811789a0c32c59439a4f">
	$$
	\begin{array}{l}
\Omega^A(x,\theta)^*=W^{A*}(x)-\sqrt2\left(\bar\theta\frac{1-\gamma_5}{2}w^A(x)\right)+\mathcal W^{A*}(x)\left(\bar\theta\frac{1-\gamma_5}{2}\theta\right)\\
\qquad-\frac12(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu W^{A*}(x)+\frac1{\sqrt2}(\bar\theta\gamma_5\theta)\left(\bar\theta\not\partial\frac{1+\gamma_5}{2}w^A(x)\right)\\
\qquad-\frac18(\bar\theta\gamma_5\theta)^2\Box W^{A*}(x).
\end{array}\tag{27.1.15}
	$$
</synced_block>
我们像方程(26.2.10)中那样将实超场 $`V ^ { A } ( x , \theta )`$ 写成分量场的形式:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81f387aadeed15593619">
	$$
	\begin{array}{l}
V^A(x,\theta)=C^A(x)-\mathrm{i}(\bar\theta\gamma_5\omega^A(x))-\frac{\mathrm{i}}2(\bar\theta\gamma_5\theta)M^A(x)-\frac12(\bar\theta\theta)N^A(x)\\
\qquad+\frac{\mathrm{i}}2(\bar\theta\gamma_5\gamma^\mu\theta)V_\mu{}^A(x)-\mathrm{i}(\bar\theta\gamma_5\theta)\left(\bar\theta\left[\lambda^A(x)+\frac12\not\partial\omega^A(x)\right]\right)\\
\qquad-\frac14(\bar\theta\gamma_5\theta)^2\left(D^A(x)+\frac12\Box C^A(x)\right).
\end{array}\tag{27.1.16}
	$$
</synced_block>
其中 $`C ^ { A } ( x ) , M ^ { A } ( x ) , N ^ { A } ( x )`$ 和 $`V _ { \mu } {} ^ { A } ( x )`$ 都是实的, 而 $`\omega ^ { A } ( x )`$ 和 $`\lambda ^ { A } ( x )`$ 则都是 Majorana 旋量.
在方程(27.1.13)中使用方程(27.1.14)—(27.1.16), 我们发现规范超场的分量场进行如下的扩充规范变换
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81e2aaf6fb19a10c5a0b">
		$$
		V^A(x,\theta)\to V^A(x,\theta)+\frac{\mathrm{i}}{2}\bigl[\Omega^A(x,\theta)-\Omega^A(x,\theta)^*\bigr]+\cdots.\tag{27.1.13}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81069cbfcfe23b6b40a3">
		$$
		\begin{array}{l}
\Omega^A(x,\theta)=W^A(x)-\sqrt2\left(\bar\theta\frac{1+\gamma_5}{2}w^A(x)\right)+\mathcal W^A(x)\left(\bar\theta\frac{1+\gamma_5}{2}\theta\right)\\
\qquad+\frac12(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu W^A(x)-\frac1{\sqrt2}(\bar\theta\gamma_5\theta)\left(\bar\theta\not\partial\frac{1+\gamma_5}{2}w^A(x)\right)\\
\qquad-\frac18(\bar\theta\gamma_5\theta)^2\Box W^A(x).
\end{array}\tag{27.1.14}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81f387aadeed15593619">
		$$
		\begin{array}{l}
V^A(x,\theta)=C^A(x)-\mathrm{i}(\bar\theta\gamma_5\omega^A(x))-\frac{\mathrm{i}}2(\bar\theta\gamma_5\theta)M^A(x)-\frac12(\bar\theta\theta)N^A(x)\\
\qquad+\frac{\mathrm{i}}2(\bar\theta\gamma_5\gamma^\mu\theta)V_\mu{}^A(x)-\mathrm{i}(\bar\theta\gamma_5\theta)\left(\bar\theta\left[\lambda^A(x)+\frac12\not\partial\omega^A(x)\right]\right)\\
\qquad-\frac14(\bar\theta\gamma_5\theta)^2\left(D^A(x)+\frac12\Box C^A(x)\right).
\end{array}\tag{27.1.16}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f815fb109d2acba06f849">
	$$
	\begin{array}{rl}
C^A(x)&\to C^A(x)-\operatorname{Im}W^A(x)+\cdots,\\
\omega^A(x)&\to \omega^A(x)+\frac1{\sqrt2}w^A(x)+\cdots,\\
V_\mu{}^A(x)&\to V_\mu{}^A(x)+\partial_\mu\operatorname{Re}W^A(x)+\cdots,\\
M^A(x)&\to M^A(x)-\operatorname{Re}\mathcal W^A(x)+\cdots,\\
N^A(x)&\to N^A(x)+\operatorname{Im}\mathcal W^A(x)+\cdots,\\
\lambda^A(x)&\to \lambda^A(x)+\cdots,\\
D^A(x)&\to D^A(x)+\cdots.
\end{array}\tag{27.1.17}
	$$
</synced_block>
其中“· · ·”依旧表示由方程(27.1.9)中的结构常数产生的项, 因此这些项正比于一个或多个耦合常数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81c5b0fadc1fccdeba04">
		$$
		\begin{array} { l } { { f ^ { A } ( a , b ) = a ^ { A } + b ^ { A } + { \frac { 1 } { 2 } } \mathrm{i} C ^ { A } { } _ { B C } a ^ { B } b ^ { C } - { \frac { 1 } { 1 2 } } C ^ { A } { } _ { B C } C ^ { C } { } _ { D E } a ^ { B } a ^ { D } b ^ { E } } } \\ { { \mathrm { } - { \frac { 1 } { 1 2 } } C ^ { A } { } _ { B C } C ^ { C } { } _ { D E } b ^ { B } b ^ { D } a ^ { E } + \cdots , } } \end{array} \tag{27.1.9}
		$$
	</synced_block_reference>
</callout>
我们可以使用这样的扩充规范变换将规范超场变成一种方便的形式, 称为 Wess-Zumino规范,在这个规范下
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81b29aeaf1725ad341c3">
	$$
	C ^ { A } ( x ) = \omega ^ { A } ( x ) = M ^ { A } ( x ) = N ^ { A } ( x ) = 0 , \tag{27.1.18}
	$$
</synced_block>
进而使得
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81d9a055f89733ec170f">
	$$
	\begin{array} { l } { { V ^ { A } ( x , \theta ) = \displaystyle \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta \Big ) V _ { \mu } {} ^ { A } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \lambda ^ { A } ( x ) \Big ) } } \\ { { { } } } \\ { { + \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } D ^ { A } ( x ) . } } \end{array} \tag{27.1.19}
	$$
</synced_block>
为了在耦合常数的零阶实现这点, 只需令 $`\operatorname{Im} { \cal W } ^ { A } ( x ) = C ^ { A } ( x )`$ , $`w ^ { A } ( x ) = - \sqrt { 2 } \omega ^ { A } ( x )`$ 以及 $`\mathcal{W} ^ { A } ( x ) =`$ $`M ^ { A } ( x ) - \mathrm{i} N ^ { A } ( x )`$ .
对于阿贝尔规范理论, 结构常数为零, 我们的任务就结束了.
对于非阿贝尔规范理论, 就得给 $`\operatorname{Im} W ^ { A } ( x )`$ , $`w ^ { A } ( x )`$ 和 $`\mathcal{W} ^ { A } ( x )`$ 加上规范耦合常数的一阶项来抵消零阶项的对易子产生的项, 然后给 $`\operatorname{Im} W ^ { A } ( x )`$ , $`w ^ { A } ( x )`$ 和 $`\mathcal{W} ^ { A } ( x )`$ 加上规范耦合常数的二阶项来抵消零阶项和一阶项的对易子产生的项, 以此类推.
计算 $`\operatorname{Im} W ^ { A } ( x )`$ , $`w ^ { A } ( x )`$ 和 $`\mathcal{W} ^ { A } ( x )`$ 级数展开中的项使得在耦合常数的所有阶都满足规范条件(27.1.18)并不容易, 但没必要这么做——重要的是这样做是可行的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81b29aeaf1725ad341c3">
		$$
		C ^ { A } ( x ) = \omega ^ { A } ( x ) = M ^ { A } ( x ) = N ^ { A } ( x ) = 0 , \tag{27.1.18}
		$$
	</synced_block_reference>
</callout>
对变换规则(26.2.11)—(26.2.14)的观察表明, 除非 $`V _ { \mu } {} ^ { A } = \lambda ^ { A } = 0`$ , 否则 Wess-Zumino 规范条件(27.1.18)在超对称变换下不是不变的, 另外, 除非 $`D ^ { A } = 0`$ , 否则条件 $`\lambda ^ { A } = 0`$ 不是超对称的, 在这种情况下, 整个超场为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81b29aeaf1725ad341c3">
		$$
		C ^ { A } ( x ) = \omega ^ { A } ( x ) = M ^ { A } ( x ) = N ^ { A } ( x ) = 0 , \tag{27.1.18}
		$$
	</synced_block_reference>
</callout>
一旦我们采取了Wess-Zumino规范, 那么在一般的扩充规范变换或超对称下, 作用量都不再是不变的, 但是, 在做一个超对称变换后, 这使我们脱离了Wess-Zumino规范,然后在接上合适的扩充规范变换使得我们回到Wess-Zumino规范, 作用量在这样的组合变换下是不变的.
(我们会在 27.8 节明确地探究这点.) 正如我们现在将要看到的, 在保持Wess-Zumino规范的普通规范变换(27.1.2)—(27.1.4)下, 作用量也是不变的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f819189d2e31f920550fc">
		$$
		\Phi^n(x,\theta)\to \bigl[\exp\bigl(\mathrm{i}t_A\Lambda^A(x_+)\bigr)\bigr]^n{}_m\Phi^m(x,\theta).\tag{27.1.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
		$$
	</synced_block_reference>
</callout>
当规范超场满足Wess-Zumino 规范条件(27.1.18)后, 推导它在普通的无限小规范变换下的行为变得相对容易.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81b29aeaf1725ad341c3">
		$$
		C ^ { A } ( x ) = \omega ^ { A } ( x ) = M ^ { A } ( x ) = N ^ { A } ( x ) = 0 , \tag{27.1.18}
		$$
	</synced_block_reference>
</callout>
在这种情况下, $`\Omega ^ { A } ( x _ { + } )`$ 是形如(26.3.11)的左手征超场, 但是没有 $`\psi _ { L }`$ -分量和 $`\mathcal{F}`$ -分量, 并且 $`\phi`$ -分量由实无限小函数 $`\Lambda ^ { A } ( x )`$ 给出:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81f88b67e68cfa9f1133">
	$$
	\Omega^A(x_+)=\Lambda^A(x)+\frac12(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu\Lambda^A(x)-\frac18(\bar\theta\gamma_5\theta)^2\Box\Lambda^A(x).\tag{27.1.20}
	$$
</synced_block>
为了计算变换规则(27.1.4)中的指数乘积, 我们使用 Baker-Hausdorff 公式的如下版本:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f8198b4e5ff63a9ca9163">
	$$
	\exp ( a ) \exp ( X ) \exp ( b ) = \exp \Bigl [ X + L _ { X } \cdot ( b - a ) + ( L _ { X } \coth L _ { X } ) \cdot ( b + a ) + \cdots \Bigr ] \ , \tag{27.1.21}
	$$
</synced_block>
其中 $`a , b`$ 和 $`X`$ 是任意矩阵, $`L _ { X }`$ 是算符
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81808ff5f1f5a6ab7d59">
	$$
	\begin{array} { r } { L _ { X } \cdot f = \frac { 1 } { 2 } [ X , f ] , } \end{array} \tag{27.1.22}
	$$
</synced_block>
而这里的“· · · ”代表 $`a`$ 和(或) $`b`$ 的二阶项和高阶项.
在我们的情况中有
$$
\begin{array}{l}
b+a=2t_A\operatorname{Im}\Lambda^A(x_+)=-\mathrm{i}(\bar\theta\gamma_5\gamma_\mu\theta)t_A\partial^\mu\Lambda^A(x),\\
b-a=-2\mathrm{i}t_A\operatorname{Re}\Lambda^A(x_+)=-2\mathrm{i}t_A\left[\Lambda^A(x)-\frac18(\bar\theta\gamma_5\theta)^2\Box\Lambda^A(x)\right],\\
X=-2t_AV^A(x,\theta)=-2t_A\left[\frac12(\bar\theta\gamma_5\gamma^\mu\theta)V_\mu{}^A(x)-\mathrm{i}(\bar\theta\gamma_5\theta)(\bar\theta\lambda^A(x))-\frac14(\bar\theta\gamma_5\theta)^2D^A(x)\right].
\end{array}
$$
现在, $`X`$ 中的每一项包含至少一个 $`\theta _ { L }`$ 因子和至少一个 $`\theta _ { R }`$ 因子, 而 $`a + b`$ 则只有一个 $`\theta _ { L }`$ 因子和一个 $`\theta _ { R }`$ 因子, 所以我们可以扔掉 $`L _ { X } \coth L _ { X }`$ 中 $`L _ { X }`$ 的任何二阶或更高阶项.
由于 $`L _ { X } \coth L _ { X }`$ 是 $`L _ { X }`$ 的偶函数, 这意味着我们可以将它本身换成它关于 $`L _ { X }`$ 的零阶项, 而这一项就是1. 另外, 我们可以扔掉 $`b - a`$ 中正比于 $`( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 }`$ 的项, 这是因为当 $`L _ { X }`$ 作用在该项上时, 这一项至少会产生 3 个 $`\theta _ { L }`$ 或 $`\theta _ { R }`$ 因子.
因此方程(27.1.21)右边的指数变量可以被换成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f8198b4e5ff63a9ca9163">
		$$
		\exp ( a ) \exp ( X ) \exp ( b ) = \exp \Bigl [ X + L _ { X } \cdot ( b - a ) + ( L _ { X } \coth L _ { X } ) \cdot ( b + a ) + \cdots \Bigr ] \ , \tag{27.1.21}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array}{l}
X+\frac12[X,b-a]+b+a=-2t_A\left[V^A(x,\theta)+C^A{}_{BC}V^B(x,\theta)\Lambda^C(x)\right.\\
\left.\qquad\qquad\qquad\qquad\qquad+\frac{\mathrm{i}}2(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu\Lambda^A(x)\right].
\end{array}
$$
因此对于无限小规范变换, 变换规则(27.1.4)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81bdad38f03acca38eb2">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Lambda^A(x_+)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Lambda^A(x_+)\bigr).\tag{27.1.4}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81929950f1a724a7da55">
	$$
	V^A(x,\theta)\to V^A(x,\theta)+C^A{}_{BC}V^B(x,\theta)\Lambda^C(x)+\frac{\mathrm{i}}2(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu\Lambda^A(x).\tag{27.1.23}
	$$
</synced_block>
值得注意的是, 在普通的规范变换下, Wess-Zumino规范下的规范超场依旧会处在Wess-Zumino规范下.
用方程(27.1.19)中的分量场表示, 方程(27.1.23)是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81d9a055f89733ec170f">
		$$
		\begin{array} { l } { { V ^ { A } ( x , \theta ) = \displaystyle \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta \Big ) V _ { \mu } {} ^ { A } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \lambda ^ { A } ( x ) \Big ) } } \\ { { { } } } \\ { { + \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } D ^ { A } ( x ) . } } \end{array} \tag{27.1.19}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81929950f1a724a7da55">
		$$
		V^A(x,\theta)\to V^A(x,\theta)+C^A{}_{BC}V^B(x,\theta)\Lambda^C(x)+\frac{\mathrm{i}}2(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu\Lambda^A(x).\tag{27.1.23}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81cfb70bfe5cf4fc0433">
	$$
	\begin{array}{l}
V_\mu{}^A(x)\to C^A{}_{BC}V_\mu{}^B(x)\Lambda^C(x)+\partial_\mu\Lambda^A(x),\\
\lambda^A(x)\to C^A{}_{BC}\lambda^B(x)\Lambda^C(x),\\
D^A(x)\to C^A{}_{BC}D^B(x)\Lambda^C(x).
\end{array}\tag{27.1.24-27.1.26}
	$$
</synced_block>
我们可以认为方程(27.1.24)是规范场通常的 Yang-Mills 规范变换规则(15.1.9), 而方程(27.1.25)和(27.1.26)告诉我们场 $`\lambda ^ { A } ( x )`$ 和 $`D ^ { A } ( x )`$ 像规范群伴随表示下的“物质”场那样变换.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81cfb70bfe5cf4fc0433">
		$$
		\begin{array}{l}
V_\mu{}^A(x)\to C^A{}_{BC}V_\mu{}^B(x)\Lambda^C(x)+\partial_\mu\Lambda^A(x),\\
\lambda^A(x)\to C^A{}_{BC}\lambda^B(x)\Lambda^C(x),\\
D^A(x)\to C^A{}_{BC}D^B(x)\Lambda^C(x).
\end{array}\tag{27.1.24-27.1.26}
		$$
	</synced_block_reference>
</callout>
Majorana 旋量$`\lambda ^ { A }`$ 被称为规范微子场, 而实标量 $`D ^ { A }`$ 将会变成另一组辅助场.
接下来我们必须要计算构建手征超场的规范不变函数时需要的矩阵Γ.
由于所有含有超过4个 $`\theta`$ 因子的项为零, 在Wess-Zumino规范下, 指数展开非常简单:
$$
\begin{array} { l } { { \Gamma ( x , \theta ) = \displaystyle \exp \Bigl ( - 2 t _ { A } V ^ { A } ( x , \theta ) \Bigr ) } } \\ { { { } } } \\ { { { } = 1 - \mathrm{i} \Bigl ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta \Bigr ) t _ { A } V _ { \mu } {} ^ { A } ( x ) } } \\ { { { } ~ - \displaystyle \frac { 1 } { 2 } \Bigl ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta \Bigr ) \Bigl ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \nu } \theta \Bigr ) t _ { A } t _ { B } V _ { \mu } {} ^ { A } ( x ) V _ { \nu } {} ^ { B } ( x ) } } \\ { { { } ~ + 2 \mathrm{i} \Bigl ( \bar { \theta } \gamma _ { 5 } \theta \Bigr ) t _ { A } \Bigl ( \bar { \theta } \lambda ^ { A } ( x ) \Bigr ) + \displaystyle \frac { 1 } { 2 } \Bigl ( \bar { \theta } \gamma _ { 5 } \theta \Bigr ) ^ { 2 } t _ { A } D ^ { A } ( x ) . } } \end{array}
$$
通过给矩阵 $`\Gamma`$ 右乘一个形如(26.3.11)的左手征超场的列矢量:
$$
\begin{array}{l}
\Phi^n(x,\theta)=\phi^n(x)-\sqrt2\bigl(\bar\theta\psi^n_L(x)\bigr)+\mathcal F^n(x)\left(\bar\theta\frac{1+\gamma_5}{2}\theta\right)\\
\qquad+\frac12(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu\phi^n(x)-\frac1{\sqrt2}(\bar\theta\gamma_5\theta)\bigl(\bar\theta\not\partial\psi^n_L(x)\bigr)\\
\qquad-\frac18(\bar\theta\gamma_5\gamma_\mu\theta)^2\Box\phi^n(x).
\end{array}
$$
再左乘列矢量
$$
\begin{array}{l}
\Phi^\dagger_n(x,\theta)=\phi^\dagger_n(x)-\sqrt2\bigl(\bar\psi_{Ln}(x)\theta\bigr)+\mathcal F^\dagger_n(x)\left(\bar\theta\frac{1-\gamma_5}{2}\theta\right)\\
\qquad-\frac12(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu\phi^\dagger_n(x)-\frac1{\sqrt2}(\bar\theta\gamma_5\theta)\partial_\mu\bigl(\bar\psi_{Ln}(x)\gamma^\mu\theta\bigr)\\
\qquad-\frac18(\bar\theta\gamma_5\gamma_\mu\theta)^2\Box\phi^\dagger_n(x).
\end{array}
$$
我们可以构建一个规范不变的密度.
这个乘积中 $`\theta`$ 的4阶项是
$$
\begin{aligned}
[\Phi^\dagger\Gamma\Phi]_{\theta^4}
&=-\frac18(\bar\theta\gamma_5\gamma_\mu\theta)^2\left\{[\phi^\dagger\Box\phi]+[(\Box\phi^\dagger)\phi]\right\}\\
&\quad+(\bar\theta\gamma_5\gamma_\mu\theta)\left\{[(\bar\psi_L\theta)(\bar\theta\gamma^\mu\partial_\mu\psi_L)]+[((\partial_\mu\bar\psi_L)\gamma^\mu\theta)(\bar\theta\psi_L)]\right\}\\
&\quad+\frac14(\bar\theta(1-\gamma_5)\theta)(\bar\theta(1+\gamma_5)\theta)[\mathcal F^\dagger\mathcal F]
-\frac14(\bar\theta\gamma_5\gamma^\mu\theta)(\bar\theta\gamma_5\gamma^\nu\theta)[\partial_\mu\phi^\dagger\partial_\nu\phi]\\
&\quad-\frac{\mathrm{i}}2(\bar\theta\gamma_5\gamma^\mu\theta)(\bar\theta\gamma_5\gamma^\nu\theta) V_\mu{}^A\left\{[\phi^\dagger t_A\partial_\nu\phi]-[(\partial_\nu\phi^\dagger)t_A\phi]\right\}\\
&\quad-\frac12(\bar\theta\gamma_5\gamma^\mu\theta)(\bar\theta\gamma_5\gamma^\nu\theta) V_\mu{}^A V_\nu{}^B[\phi^\dagger t_A t_B\phi]\\
&\quad-2\mathrm{i}(\bar\theta\gamma_5\gamma^\mu\theta) V_\mu{}^A[(\bar\psi_L\theta)t_A(\bar\theta\psi_L)]
-2\mathrm{i}\sqrt2(\bar\theta\gamma_5\theta)[(\bar\psi_L\theta)t_A(\bar\theta\lambda^A)\phi].
\end{aligned}
$$
$$
\begin{array} { l } { { \displaystyle - 2 \mathrm{i} \sqrt 2 \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big [ \phi ^ { \dagger } \left( \overline { { { \lambda ^ { A } } } } \theta \right) t _ { A } \left( \bar { \theta } \psi _ { L } \right) \Big ] } } \\ { { \displaystyle + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } D ^ { A } \Big [ \phi ^ { \dagger } t _ { A } \phi \Big ] , } } \end{array}
$$
其中我们用方括号表示味指标 $`n , m`$ 的标量积, 并继续用圆括号表示Dirac指标的标量积.
同26.4节一样, 我们可以使用恒等式(26.A.17)—(26.A.19)把对 $`\theta`$ 的所有依赖写成总因子 $`( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 }`$ 的形式:
$$
\begin{aligned}
[\Phi^\dagger\Gamma\Phi]_{\theta^4}
&=(\bar\theta\gamma_5\theta)^2\Bigl\{-\frac18[\phi^\dagger\Box\phi]-\frac18[(\Box\phi^\dagger)\phi]
+\frac14[(\bar\psi_L\gamma^\mu\partial_\mu\psi_L)]-\frac14[((\partial_\mu\bar\psi_L)\gamma^\mu\psi_L)]\\
&\qquad-\frac12[\mathcal F^\dagger\mathcal F]+\frac14[\partial_\mu\phi^\dagger\partial^\mu\phi]
+\frac{\mathrm{i}}2V_\mu{}^A[\phi^\dagger t_A\partial^\mu\phi]-\frac{\mathrm{i}}2V_\mu{}^A[(\partial^\mu\phi^\dagger)t_A\phi]\\
&\qquad+\frac12V_\mu{}^AV^{B\mu}[\phi^\dagger t_At_B\phi]-\frac{\mathrm{i}}2V_\mu{}^A[(\bar\psi_L\gamma^\mu t_A\psi_L)]
-\frac{\mathrm{i}}{\sqrt2}[(\bar\psi_Lt_A\lambda^A)\phi]\\
&\qquad+\frac{\mathrm{i}}{\sqrt2}[\phi^\dagger(\bar\lambda^At_A\psi_L)]+\frac12D^A[\phi^\dagger t_A\phi]\Bigr\}.
\end{aligned}
$$
$`D`$ -项是 $`- \textstyle { \frac { 1 } { 4 } } ( { \bar { \theta } } \gamma _ { 5 } \theta ) ^ { 2 }`$ 的系数减去 $`\frac { 1 } { 2 }`$ □ 作用在与 $`\theta`$ 无关的项上, $`[ \Phi ^ { \dagger } \Gamma \Phi ]`$ 中与 $`\theta`$ 无关的项是 $`[ \phi ^ { \dagger } \phi ]`$ , 所以
$$
\begin{aligned}
[\Phi^\dagger\Gamma\Phi]_D
&=-2[\partial_\mu\phi^\dagger\partial^\mu\phi]-[(\bar\psi_L\gamma^\mu\partial_\mu\psi_L)]+[((\partial_\mu\bar\psi_L)\gamma^\mu\psi_L)]+2[\mathcal F^\dagger\mathcal F]\\
&\quad-2\mathrm{i}V_\mu{}^A[\phi^\dagger t_A\partial^\mu\phi]+2\mathrm{i}V_\mu{}^A[(\partial^\mu\phi^\dagger)t_A\phi]
-2V_\mu{}^AV^{B\mu}[\phi^\dagger t_At_B\phi]\\
&\quad+2\mathrm{i}V_\mu{}^A[(\bar\psi_L\gamma^\mu t_A\psi_L)]
+2\mathrm{i}\sqrt2[(\bar\psi_Lt_A\lambda^A)\phi]-2\mathrm{i}\sqrt2[\phi^\dagger(\bar\lambda^At_A\psi_L)]\\
&\quad-2D^A[\phi^\dagger t_A\phi].
\end{aligned}
$$
为了看到这是规范不变的, 我们注意到它可以写成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81208a08d9c871455713">
	$$
	\begin{array} { r l } { \displaystyle \frac { 1 } { 2 } \Big [ \Phi ^ { \dagger } \Gamma \Phi \Big ] _ { D } = - \Big [ ( D _ { \mu } \phi ) ^ { \dagger } D ^ { \mu } \phi \Big ] } & { } \\ { \displaystyle - \frac { 1 } { 2 } \Big [ \Big ( \overline { { \psi _ { L } } } \gamma ^ { \mu } D _ { \mu } \psi _ { L } \Big ) \Big ] + \frac { 1 } { 2 } \Big [ \Big ( \overline { { ( D _ { \mu } \psi _ { L } ) } } \gamma ^ { \mu } \psi _ { L } \Big ) \Big ] + \Big [ \mathcal{F} ^ { \dagger } \mathcal{F} \Big ] } & { } \\ { \displaystyle + \mathrm{i} \sqrt { 2 } \Big [ \Big ( \overline { { \psi _ { L } } } t _ { A } \lambda ^ { A } \Big ) \phi \Big ] - \mathrm{i} \sqrt { 2 } \Big [ \phi ^ { \dagger } \Big ( \overline { { \lambda ^ { A } } } t _ { A } \psi _ { L } \Big ) \Big ] } & { } \\ { \displaystyle - D ^ { A } \Big [ \phi ^ { \dagger } t _ { A } \phi \Big ] , } \end{array} \tag{27.1.27}
	$$
</synced_block>
其中 $`D _ { \mu }`$ 是规范不变导数(15.1.10):
<synced_block url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81dab4d9f6e289c12e08">
	$$
	{ \cal D } _ { \mu } \psi _ { L } \equiv \partial _ { \mu } \psi _ { L } - \mathrm{i} t _ { A } V _ { \mu } {} ^ { A } \psi _ { L } , \qquad { \cal D } _ { \mu } \phi \equiv \partial _ { \mu } \phi - \mathrm{i} t _ { A } V _ { \mu } {} ^ { A } \phi . \tag{27.1.28}
	$$
</synced_block>
因此, 方程(27.1.27)现在是左手征超场的标量分量和旋量分量一个合适的规范不变动能拉格朗日量, 再加上规范微子场与手征超场的标量分量和旋量分量的Yukawa耦合以及包含辅助场 $`\mathcal F^n`$ 和 $`D^A`$ 的项.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88#34cee2b74b3f81208a08d9c871455713">
		$$
		\begin{array} { r l } { \displaystyle \frac { 1 } { 2 } \Big [ \Phi ^ { \dagger } \Gamma \Phi \Big ] _ { D } = - \Big [ ( D _ { \mu } \phi ) ^ { \dagger } D ^ { \mu } \phi \Big ] } & { } \\ { \displaystyle - \frac { 1 } { 2 } \Big [ \Big ( \overline { { \psi _ { L } } } \gamma ^ { \mu } D _ { \mu } \psi _ { L } \Big ) \Big ] + \frac { 1 } { 2 } \Big [ \Big ( \overline { { ( D _ { \mu } \psi _ { L } ) } } \gamma ^ { \mu } \psi _ { L } \Big ) \Big ] + \Big [ \mathcal{F} ^ { \dagger } \mathcal{F} \Big ] } & { } \\ { \displaystyle + \mathrm{i} \sqrt { 2 } \Big [ \Big ( \overline { { \psi _ { L } } } t _ { A } \lambda ^ { A } \Big ) \phi \Big ] - \mathrm{i} \sqrt { 2 } \Big [ \phi ^ { \dagger } \Big ( \overline { { \lambda ^ { A } } } t _ { A } \psi _ { L } \Big ) \Big ] } & { } \\ { \displaystyle - D ^ { A } \Big [ \phi ^ { \dagger } t _ { A } \phi \Big ] , } \end{array} \tag{27.1.27}
		$$
	</synced_block_reference>
</callout>
</content>
</page>
