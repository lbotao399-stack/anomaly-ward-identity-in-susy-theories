Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51 as of 2026-07-15T03:41:46.945Z:
<page url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.5 树级近似下的自发超对称性破缺"}
</properties>
<content>
我们在上一节看到, 在手征超场的可重整理论中, 如果方程(26.4.8)有解, 即, 如果存在场值 $`\phi _ { 0 }`$ 使得超势是驻定的:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#eb851fcd76b4495490623d180edd1c3d">
		$$
		\left. f _ { n } ( \phi ) \right| _ { \phi = \phi _ { 0 } } = 0 , \tag{26.4.8}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81b9b9fee2c87707acde">
	$$
	f _ { n } ( \phi _ { 0 } )=0 . \tag{26.5.1}
	$$
</synced_block>
那么超对称性(至少在树级近似下)是不破缺的.
这里独立变量的个数和方程的个数相等, 所以我们一般会期待方程(26.5.1)有解.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81b9b9fee2c87707acde">
		$$
		f _ { n } ( \phi _ { 0 } )=0 . \tag{26.5.1}
		$$
	</synced_block_reference>
</callout>
为了使超对称性在这些理论中自发破缺, 我们有必要给超势的形式附加一些限制.
为了看到该如何选择超势进而使得超对称性可以自发破缺, 我们将会考察O’Raifeartaigh给出的一类模型的推广.\[3\] 
假定超势是一组左手征超场 $`Y ^ { i }`$ 的线性组合, 且它的系数由第二组左手征超场 $`X ^ { n }`$ 的函数 $`f _ { i } ( X )`$ 给定:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- L. O’Raifeartaigh, Nucl. Phys. B96, 331 (1975). 这篇文章重印于Supersymmetry, 参考文献\[1\]
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81f8b74ac8a4b24898dd">
	$$
	f ( X , Y )=Y ^ { i } f _ { i } ( X ) . \tag{26.5.2}
	$$
</synced_block>
超对称性不被这些超场的标量分量值 $`x ^ { n }`$ 和 $`y ^ { i }`$ 破缺的条件是
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81669be0f5580661678b">
	$$
							\begin{aligned}
0&=\frac{\partial f(x,y)}{\partial y^i}=f_i(x),\\
0&=\frac{\partial f(x,y)}{\partial x^n}
=y^i\frac{\partial f_i(x)}{\partial x^n}.
\end{aligned}\tag{26.5.3-26.5.4}
	$$
</synced_block>
方程(26.5.4)总可以通过取 $`y ^ { i } = 0`$ 被解掉, 并且它对解方程(26.5.3)没有影响.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81669be0f5580661678b">
		$$
								\begin{aligned}
0&=\frac{\partial f(x,y)}{\partial y^i}=f_i(x),\\
0&=\frac{\partial f(x,y)}{\partial x^n}
=y^i\frac{\partial f_i(x)}{\partial x^n}.
\end{aligned}\tag{26.5.3-26.5.4}
		$$
	</synced_block_reference>
</callout>
另一方面, 如果超场 $`X ^ { n }`$ 的个数小于超场 $`Y ^ { i }`$ 的个数, 那么方程(26.5.3)在 $`x ^ { n }`$ 上附加的条件要多于变量, 所以如果没有精细调节, 找到解是不可能的, 这时超对称是破缺的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81669be0f5580661678b">
		$$
								\begin{aligned}
0&=\frac{\partial f(x,y)}{\partial y^i}=f_i(x),\\
0&=\frac{\partial f(x,y)}{\partial x^n}
=y^i\frac{\partial f_i(x)}{\partial x^n}.
\end{aligned}\tag{26.5.3-26.5.4}
		$$
	</synced_block_reference>
</callout>
初始假定(26.5.2)本身看上去似乎代表了精细调节的一个基本形式, 但是这一形式可以通过假定合适的 $`R`$ -对称性附加到超势上.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81f8b74ac8a4b24898dd">
		$$
		f ( X , Y )=Y ^ { i } f _ { i } ( X ) . \tag{26.5.2}
		$$
	</synced_block_reference>
</callout>
就像在26.3节讨论的, 在有 $`N = 1`$ 超对称性的理论中, $`R`$ -对称性是使得 $`\theta`$ 超空间坐标有不平庸变换性质的 $`U ( 1 )`$ 对称性.
如果我们假定一个 $`R`$ -对称性使得 $`\theta _ { L }`$ 携带量子数 $`+ 1`$ , 那么任何超势的 $`\mathcal{F}`$ -项的量子数等于这个超势本身的量子数减2, 所以 $`R`$ 不变性要求超势本身有 $`R = 2`$ .
因此, 在超场 $`Y ^ { i }`$ 和 $`X ^ { n }`$ 分别有 $`R`$ 量子数 $`+ 2`$ 和0时, 我们可以通过要求 $`R`$ 不变性来附加结构(26.5.2).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81f8b74ac8a4b24898dd">
		$$
		f ( X , Y )=Y ^ { i } f _ { i } ( X ) . \tag{26.5.2}
		$$
	</synced_block_reference>
</callout>
在这类模型中, 标量场有势
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81bc8144e14bbdb77652">
	$$
							\begin{aligned}
V(x,y)={}&f^{\dagger i}(x^\dagger)f_i(x)\\
&+\left(y ^ { \dagger } _ { i }
\frac{\partial f^{\dagger i}(x^\dagger)}{\partial x ^ { \dagger } _ { n }}\right)
\left(y^j\frac{\partial f_j(x)}{\partial x^n}\right).
\end{aligned}\tag{26.5.5}
	$$
</synced_block>
通过选择 $`x ^ { n }`$ 使得第一项最小, 我们总可以到达这个势的最小值; 无论这要求 $`x ^ { n }`$ 取什么值, 第二项总可以通过取 $`y ^ { i } = 0`$ 到达最小值.
无论超对称性是否自发破缺, 这些模型有一个独特的特征:在场的空间中总有一个方向使得势的极小值点是平坦的.
令 $`v_{ni}:=\left.\partial f_i(x)/\partial x^n\right|_{x=x_0}`$。则第二项对任意满足 $`v_{ni}y^i=0`$（对每个 $`n`$）的 $`y^i`$ 都为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81bc8144e14bbdb77652">
		$$
								\begin{aligned}
V(x,y)={}&f^{\dagger i}(x^\dagger)f_i(x)\\
&+\left(y ^ { \dagger } _ { i }
\frac{\partial f^{\dagger i}(x^\dagger)}{\partial x ^ { \dagger } _ { n }}\right)
\left(y^j\frac{\partial f_j(x)}{\partial x^n}\right).
\end{aligned}\tag{26.5.5}
		$$
	</synced_block_reference>
</callout>
矩阵 $`v_{ni}`$ 的秩至多为 $`N_X`$；若 $`N_Y>N_X`$，则 $`\dim\ker v\ge N_Y-N_X`$，所以至少有 $`N_Y-N_X`$ 个平坦方向.
对于任何沿着这些平坦方向的非零 $`y ^ { i } = y _ { 0 } ^ { i }`$ , **拉格朗日密度的 **$`R`$** -对称性是自发破缺**的, 与这个整体对称性破缺相联系的 Goldstone 玻色场 $`\phi`$ 对应于与 $`y ^ { i }`$ 中的 $`y _ { 0 } ^ { i }`$ 正比的项.
这类模型中最简单的一个例子是只有一个 $`X`$ 超场和两个 $`Y`$ 超场的情况.
可重整性要求系数函数 $`f _ { i } ( X )`$ 是 $`X`$ 的二次函数, 通过取合适的 $`Y ^ { i }`$ 的线性组合并对 $`X`$ 做偏移和重标度, 我们可以选择这些函数使得
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f818bbe97c90a1395b043">
	$$
	f _ { 1 } ( X ) = X - a , \qquad f _ { 2 } ( X ) = X ^ { 2 } , \tag{26.5.6}
	$$
</synced_block>
其中 $`a`$ 是任意常数.
除非超势被精细调节使得 $`a = 0`$ , 否则两个方程(26.5.1)显然不可能同时有解.势(26.5.5)在这里是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81b9b9fee2c87707acde">
		$$
		f _ { n } ( \phi _ { 0 } )=0 . \tag{26.5.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81bc8144e14bbdb77652">
		$$
								\begin{aligned}
V(x,y)={}&f^{\dagger i}(x^\dagger)f_i(x)\\
&+\left(y ^ { \dagger } _ { i }
\frac{\partial f^{\dagger i}(x^\dagger)}{\partial x ^ { \dagger } _ { n }}\right)
\left(y^j\frac{\partial f_j(x)}{\partial x^n}\right).
\end{aligned}\tag{26.5.5}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81d4aa0cfab90dca2609">
	$$
	V(x,y)=|x|^4+|x-a|^2+|y^1+2xy^2|^2 . \tag{26.5.7}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	No four-spinor index occurs; scalar/flavor indices are unchanged.
	$$
	V ( x , y ) = | x | ^ { 4 } + | x - a | ^ { 2 } + | y ^ { 1 } + 2 x y ^ { 2 } | ^ { 2 } . 
	$$
</callout>
前两项的和有唯一的整体最小值点 $`x _ { 0 }`$ .
这里的平坦方向是使得 $`y ^ { 1 } + 2 x _ { 0 } y ^ { 2 } = 0`$ 的方向.
当 $`a = 0`$ 时,我们有 $`x _ { 0 } = 0`$ , 势能的最小值就是沿着 $`y ^ { 1 } = 0`$ 而 $`y ^ { 2 }`$ 任意的那条线.
无论自发破缺的原因是什么, 这个现象总需要存在一个**无质量的自旋 **$`1 / 2`$** 粒子, 戈德斯通微子(goldstino),** 它是与普通整体对称性自发破缺相联系的Goldstone玻色子的类似物.
(在超引力理论中有一个例外, 我们会在31.3节讨论, 那里的超对称性是定域对称性, 戈**德斯通微子是作为有质量自旋 **$`3 / 2`$** 粒子的 **$`\pm 1 / 2`$** 螺旋度态出现的, 即引力微子的 **$`\pm 1 / 2`$** 螺旋度态**.) 
在手征超场的可重整理论中，scalar field 的 tree-level vacuum $`\phi_0^n`$ 必须极小化方程(26.4.7)中的势 $`V(\phi,\phi^\dagger)=f^{\dagger n}(\phi^\dagger)f_n(\phi)`$，所以
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#197b2065da3e45b087689719e6ad1c23">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { \dagger } _ { n } \partial ^ { \mu } \phi ^ { n } - \frac { 1 } { 2 } \Bigl ( \bar { \psi } _ { L } {} _ { n } \gamma ^ { \mu } \partial _ { \mu } \psi _ { L } ^ { n } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \bar { \psi } _ { L } {} _ { n } ) \gamma ^ { \mu } \psi _ { L } ^ { n } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } f _ { n m } ( \phi ) \left( \bar { \psi } _ { R } {} ^ { n } \psi _ { L } ^ { m } \right) - \frac { 1 } { 2 } f ^ { \dagger n m } ( \phi ^ { \dagger } ) \left( \bar { \psi } _ { L } {} _ { n } \psi _ { R } {} _ { m } \right) } \\ { \displaystyle \qquad - f ^ { \dagger n } ( \phi ^ { \dagger } ) f _ { n } ( \phi ) . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f812c9ff8ece0fc5ebdab">
	$$
	\mathcal M_{nm}\,f^{\dagger m}(\phi _ { 0 } ^ { \dagger })=0 . \tag{26.5.8}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81d08af1fa1ef89273a4">
	$$
	\mathcal M_{nm}:=f_{nm}(\phi _ { 0 }) . \tag{26.5.9}
	$$
</synced_block>
如果方程(26.5.1)不成立，则方程(26.5.8)说明 $`\mathcal M_{nm}`$ 有零模；由方程(26.4.10)，存在由 $`\psi_L^n`$ 与 $`\psi_R{}_n`$ 描述的无质量 spin-$`1/2`$ 线性组合.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81b9b9fee2c87707acde">
		$$
		f _ { n } ( \phi _ { 0 } )=0 . \tag{26.5.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f812c9ff8ece0fc5ebdab">
		$$
		\mathcal M_{nm}\,f^{\dagger m}(\phi _ { 0 } ^ { \dagger })=0 . \tag{26.5.8}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#6ea6a4c65c6540c2970fda18a0e2e387">
		$$
		\begin{array} { r l } { \mathcal{L} _ { 0 } = - \partial _ { \mu } \varphi ^ { \dagger } _ { n } \partial ^ { \mu } \varphi ^ { n } - \frac { 1 } { 2 } \Bigl ( \bar { \psi } _ { L } {} _ { n } \gamma ^ { \mu } \partial _ { \mu } \psi _ { L } ^ { n } \Bigr ) + \frac { 1 } { 2 } \Bigl ( \partial _ { \mu } \bigl ( \bar { \psi } _ { L } {} _ { n } \bigr ) \gamma ^ { \mu } \psi _ { L } ^ { n } \Bigr ) } \\ { - \displaystyle \frac { 1 } { 2 } \mathcal{M} _ { n m } \Bigl ( \bar { \psi } _ { R } {} ^ { n } \psi _ { L } ^ { m } \Bigr ) - \frac { 1 } { 2 } \mathcal{M} ^ { \dagger n m } \Bigl ( \bar { \psi } _ { L } {} _ { n } \psi _ { R } {} _ { m } \Bigr ) } \\ { - \displaystyle \Bigl ( \mathcal{M} ^ { \dagger } \mathcal{M} \Bigr ) ^ { m } {} _ { n } \varphi ^ { \dagger } _ { m } \varphi ^ { n } , } \end{array} \tag{26.4.10}
		$$
	</synced_block_reference>
</callout>
零.
例如, 对于方程(26.5.2)和(26.5.6)定义的模型, 矩阵 $`\mathcal{M}`$ 不为零的分量是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f81f8b74ac8a4b24898dd">
		$$
		f ( X , Y )=Y ^ { i } f _ { i } ( X ) . \tag{26.5.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f818bbe97c90a1395b043">
		$$
		f _ { 1 } ( X ) = X - a , \qquad f _ { 2 } ( X ) = X ^ { 2 } , \tag{26.5.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8128b81bd4c39137cb51#34cee2b74b3f8183b145e1b6b134dda3">
	$$
	\mathcal{M} _ { x y ^ { 1 } } = \mathcal{M} _ { y ^ { 1 } x } = 1 , \qquad \mathcal{M} _ { x y ^ { 2 } } = \mathcal{M} _ { y ^ { 2 } x } = 2 x _ { 0 } , \tag{26.5.10}
	$$
</synced_block>
所以这个矩阵有本征值 $`\pm 2 x _ { 0 }`$ 和0, 其中最后一个本征值对应戈德斯通微子模.
在第29章, 我们将在不使用微扰论的情况下证明超对称性自发破缺要求存在戈德斯通微子, 并在那里探索它们的性质.
<empty-block/>
</content>
</page>
