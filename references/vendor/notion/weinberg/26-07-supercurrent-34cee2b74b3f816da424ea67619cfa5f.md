Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f as of 2026-07-17T04:15:20.084Z:
<page url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.7 超对称流"}
</properties>
<content>
同任何其它整体连续对称性一样, 超对称性会导致一个守恒流.\[5\] 
超对称流的守恒和对易性质是一些算符方程, 即使在超对称自发破缺的情况下, 这些算符方程也是成立的, 因此在第29章我们在非微扰的意义下考察超对称自发破缺的理论时是有用的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- J. Iliopoulos and B. Zumino, Nucl. Phys. B76, 310 (1974); S. Ferrara and B.Zumino, Nucl.Phys. B87, 207 (1975). 这些文章重印于Supersymmetry, 参考文献\[1\]
</callout>
另外, 超对称流与称为超流的超场的分量相关,\[6\] 这一点在第31章我们处理超引力时具有基础的重要性.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- 这一节沿用的是 S. Ferrara 和 B. Zumino 的方法, 参考文献\[5\]
</callout>
就像我们在7.3节看到的, 拉格朗日密度在无限小变换 $`\chi ^ { \ell } \to \chi ^ { \ell } + \epsilon \mathcal{F} ^ { \ell }`$ 下(其中 $`\chi ^ { \ell }`$ 是一般的正则或辅助玻色场或费米场, $`\mathcal{F} ^ { \ell }`$ 是正则场和辅助场的函数.)
有一个普通的整体对称性会导致一个守恒流
$$
J ^ { \mu } ( x ) \propto \frac { \partial \mathcal{L} ( x ) } { \partial ( \partial \chi ^ { \ell } ( x ) / \partial x ^ { \mu } ) } \mathcal{F} ^ { \ell } ( x ) ,
$$
它对于满足场方程的场是守恒的并生成了对称性, 也就是说正则对易关系给出
$$
\left[ \int \mathrm { d } ^ { 3 } x J ^ { 0 } ( x ) , \chi ^ { \ell } ( x ) \right] \propto \mathcal{F} ^ { \ell } ( y ) .
$$
由于两个原因, 超对称流的处理要稍微复杂一些.
一个原因是, 超对称性是作用量的对称性而不是拉格朗日密度或者拉格朗日量的对称性.
取而代之, 拉格朗日密度在无限小超对称变换下的变分是时空导数, 我们可以将其写成如下形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f810ca352de9521d2cfa0">
	$$
	\delta { \mathcal L } = \left( \bar { \alpha } \partial _ { \mu } K ^ { \mu } \right) , \tag{26.7.1}
	$$
</synced_block>
其中 $`K ^ { \mu }`$ 是 Majorana 旋量的 4 -矢.
结果是, 超对称流不是通常的 Noether 流.
Noether 流是
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f818e9351fec7544fad6a">
	$$
	\frac { \partial _ { R } \mathcal{L} } { \partial ( \partial _ { \mu } \chi ^ { \ell } ) } \delta \chi ^ { \ell } \equiv - \Big ( \bar { \alpha } N ^ { \mu } \Big ) \tag{26.7.2}
	$$
</synced_block>
定义的 Majorana 旋量的 4 -矢 $`N ^ { \mu }`$ , 它的散度由 Euler-Lagrange 方程给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8183bf43c1d48bf5df15">
	$$
	\begin{array} { l } { { \displaystyle \left( \bar { \alpha } \partial _ { \mu } N ^ { \mu } \right) = - \frac { \partial _ { R } { \mathcal{L} } } { \partial \chi ^ { \ell } } \delta \chi ^ { \ell } - \frac { \partial _ { R } { \mathcal{L} } } { \partial ( \partial _ { \mu } \chi ^ { \ell } ) } \partial _ { \mu } \delta \chi ^ { \ell } } } \\ { { \displaystyle ~ = - \delta { \mathcal{L} } . } } \end{array} \tag{26.7.3}
	$$
</synced_block>
(这里的 $`\partial _ { R }`$ 是右导数, 它定义成在微分之前将要微分的费米变量移至右边的.) 
相反, 我们必须要将超对称流定义成
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8100a5dcfeb7f796d407">
	$$
	S ^ { \mu } \equiv N ^ { \mu } + K ^ { \mu } , \tag{26.7.4}
	$$
</synced_block>
方程(26.7.1)和(26.7.3)告诉我们它是守恒的:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f810ca352de9521d2cfa0">
		$$
		\delta { \mathcal L } = \left( \bar { \alpha } \partial _ { \mu } K ^ { \mu } \right) , \tag{26.7.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8183bf43c1d48bf5df15">
		$$
		\begin{array} { l } { { \displaystyle \left( \bar { \alpha } \partial _ { \mu } N ^ { \mu } \right) = - \frac { \partial _ { R } { \mathcal{L} } } { \partial \chi ^ { \ell } } \delta \chi ^ { \ell } - \frac { \partial _ { R } { \mathcal{L} } } { \partial ( \partial _ { \mu } \chi ^ { \ell } ) } \partial _ { \mu } \delta \chi ^ { \ell } } } \\ { { \displaystyle ~ = - \delta { \mathcal{L} } . } } \end{array} \tag{26.7.3}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8185a898d3bc5725b99a">
	$$
	\partial _ { \mu } S ^ { \mu } = 0 . \tag{26.7.5}
	$$
</synced_block>
第二个复杂性是, 正则场 $`\chi ^ { \ell }`$ 在超对称变换下的变化 $`\delta \chi ^ { \ell }`$ 不仅是正则场的函数, 还是它们的正则共轭的函数.
例如, 方程(26.3.15)表明手征标量超场的 $`\psi`$ -分量的**变化包含 **$`\phi`$** -分量的时间导数.**
结果是, Noether 荷 $`\int \mathrm { d } ^ { 3 } x \ : N ^ { 0 }`$ 与一般正则场的对易子并不给出那个场的超对称变换.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
幸运的是,这一复杂性被第一个复杂性抵消了: 当 $`\textstyle \int \mathrm { d } ^ { 3 } x K ^ { 0 }`$ 和 $`\int \mathrm { d } ^ { 3 } x N ^ { 0 }`$ 与场的对易子被考虑在内时, 算符$`\int \mathrm { d } ^ { 3 } x \ : S ^ { 0 }`$ 确实生成了超对称变换, 也就是说
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8192a37cd8e28a8234ee">
	$$
	\left[ \int \mathrm { d } ^ { 3 } x \left( \bar { \alpha } S ^ { 0 } \right) , \chi ^ { \ell } \right] = \mathrm{i} \delta \chi ^ { \ell } , \tag{26.7.6}
	$$
</synced_block>
对于以这种方式构建的流, 这是一般结果.
例如, 考察依赖一组正则变量 $`q ^ { n }`$ 和它们时间导数 $`\dot { q } ^ { n }`$ 的拉格朗日量 $`L`$ (不是拉格朗日密度), 其中没有任何一类约束.
在量子场论中, 指标 $`n`$ 包含空间坐标以及离散自旋指标和种类指标, 且有 $`\begin{array} { r } { L = \int \mathrm { d } ^ { 3 } x \mathcal{L} } \end{array}`$ .
我们这里假定了拉格朗日密度在某个无限小变换 $`\delta`$ 下在相差一个时空导数的意义下不变, 这意味着 $`\delta L`$ 是某个泛函 $`F`$ 的时间导数.
即,
$$
{ \frac { \partial L } { \partial q ^ { n } } } \delta q ^ { n } + { \frac { \partial L } { \partial { \dot { q } } ^ { n } } } \delta { \dot { q } } ^ { n } = { \frac { \mathrm { d } } { \mathrm { d } t } } F .
$$
利用正则运动方程, 这可以写成守恒律 $`\dot { Q } = 0`$ , 其中守恒荷是
$$
Q = - \frac { \partial L } { \partial \dot { q } ^ { n } } \delta q ^ { n } + F .
$$
在我们这里的情况中, $`\begin{array} { r } { Q = \int \mathrm { d } ^ { 3 } x \left[ N ^ { 0 } + K ^ { 0 } \right] } \end{array}`$ .
我们假定通常的未约束对易关系
$$
\left[ \frac { \partial L } { \partial \dot { q } ^ { n } } , q ^ { m } \right] = - \mathrm{i} \delta _ { n } {} ^ { m } , \qquad \left[ q ^ { n } , q ^ { m } \right] = 0 ,
$$
并找到对易子
$$
\Big [ Q , q ^ { m } \Big ] = \mathrm{i} \delta q ^ { m } - \frac { \partial L } { \partial \dot { q } ^ { l } } \frac { \partial \delta q ^ { l } } { \partial \dot { q } ^ { n } } \left[ \dot { q } ^ { n } , q ^ { m } \right] + \frac { \partial F } { \partial \dot { q } ^ { n } } \left[ \dot { q } ^ { n } , q ^ { m } \right] .
$$
与方程(26.2.1)和(26.2.8)一致.
为了计算第二项和第三项, 我们注意到二阶时间导数 $`\ddot { q } ^ { n }`$ 以线性的方式出现在不变性条件中, 所以它们的系数必须互相匹配: 即使没使用运动方程, 我们也有
$$
\frac { \partial L } { \partial \dot { q } ^ { l } } \frac { \partial \delta q ^ { l } } { \partial \dot { q } ^ { n } } = \frac { \partial F } { \partial \dot { q } ^ { n } } .
$$
对易子中的第二项和第三项因此抵消了, 留给我们想要的结果
$$
\left[ Q , q ^ { m } \right] = \mathrm{i} \delta q ^ { m } .
$$
取时间导数也给出
$$
\left[ Q , \dot { q } ^ { m } \right] = \mathrm{i} \delta \dot { q } ^ { m } .
$$
这个结果已经被扩展到有约束的理论中了.\[7\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- X. Gràcia and J. Pons, J. Phys. A25, 6357 (1992). 在此感谢 J. Gomis 建议我使用比对 $`\ddot { q } ^ { n }`$ 系数的方程
</callout>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8129b0c9c3df0fd704d3">
		$$
		[ Q , S \} = \mathrm{i} \mathcal{Q} S \ , \tag{26.2.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f813a9f50c4e82207602f">
		$$
		\delta S = \left( { \bar { \alpha } } { \mathcal{Q} } \right) S = - \left( { \bar { \alpha } } { \frac { \partial S } { \partial { \bar { \theta } } } } \right) + \left( { \bar { \alpha } } \gamma ^ { \mu } \theta \right) { \frac { \partial S } { \partial x ^ { \mu } } } . \tag{26.2.8}
		$$
	</synced_block_reference>
</callout>
例如, 我们可以在左手征超场 $`\Phi ^ { n }`$ 的一般可重整理论中导出超对称流的显式公式, 这个公式可以用来检验它确实生成了超对称变换, 即方程(26.7.6).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8192a37cd8e28a8234ee">
		$$
		\left[ \int \mathrm { d } ^ { 3 } x \left( \bar { \alpha } S ^ { 0 } \right) , \chi ^ { \ell } \right] = \mathrm{i} \delta \chi ^ { \ell } , \tag{26.7.6}
		$$
	</synced_block_reference>
</callout>
这个理论的拉格朗日量(26.4.7)可以写成如下形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#197b2065da3e45b087689719e6ad1c23">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { \dagger } _ { n } \partial ^ { \mu } \phi ^ { n } - \frac { 1 } { 2 } \Bigl ( \bar { \psi } _ { L } {} _ { n } \gamma ^ { \mu } \partial _ { \mu } \psi _ { L } ^ { n } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \bar { \psi } _ { L } {} _ { n } ) \gamma ^ { \mu } \psi _ { L } ^ { n } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } f _ { n m } ( \phi ) \left( \bar { \psi } _ { R } {} ^ { n } \psi _ { L } ^ { m } \right) - \frac { 1 } { 2 } f ^ { \dagger n m } ( \phi ^ { \dagger } ) \left( \bar { \psi } _ { L } {} _ { n } \psi _ { R } {} _ { m } \right) } \\ { \displaystyle \qquad - f ^ { \dagger n } ( \phi ^ { \dagger } ) f _ { n } ( \phi ) . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81078183d4b142d0604d">
	$$
												\mathcal L=-\partial_\mu\phi ^ { \dagger } _ { n }\partial^\mu\phi^n
-\frac12\bar { \psi } _ { L } {} _ { n }\gamma^\mu\partial_\mu\psi _ { L } ^ { n }
-\frac12\bar { \psi } _ { R } {} ^ { n }\gamma^\mu\partial_\mu\psi _ { R } {} _ { n } . \tag{26.7.7}
	$$
</synced_block>
利用变换规则(26.3.15), (26.3.17), (26.3.18)和(26.3.20)(其中 $`\tilde { \phi } = \phi ^ { \dagger }`$ ), 方程(26.7.2)定义的 Noether流是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f818e9351fec7544fad6a">
		$$
		\frac { \partial _ { R } \mathcal{L} } { \partial ( \partial _ { \mu } \chi ^ { \ell } ) } \delta \chi ^ { \ell } \equiv - \Big ( \bar { \alpha } N ^ { \mu } \Big ) \tag{26.7.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8187afc6e0c859787372">
	$$
	\begin{array} { l } { { { \displaystyle N ^ { \mu } = \frac { 1 } { \sqrt 2 } \left[ 2 \left( \partial ^ { \mu } \phi ^ { \dagger } _ { n } \right) \psi _ { L } ^ { n } + 2 \left( \partial ^ { \mu } \phi ^ { n } \right) \psi _ { R } {} _ { n } + \left( \not\!\partial\, \phi ^ { n } \right) \gamma ^ { \mu } \psi _ { R } {} _ { n } + \left( \not\!\partial\, \phi ^ { \dagger } _ { n } \right) \gamma ^ { \mu } \psi _ { L } ^ { n } \right. } } } \\ { { { \displaystyle \left. - \mathcal{F} ^ { n } \gamma ^ { \mu } \psi _ { R } {} _ { n } - \mathcal{F} ^ { \dagger } _ { n } \gamma ^ { \mu } \psi _ { L } ^ { n } \right] . } } } \end{array} \tag{26.7.8}
	$$
</synced_block>
我们可以直接计算拉格朗日密度的变化, 另一种更简单的方法是, 注意到 $`D`$ -项和 $`\mathcal{F}`$ -项在超对称变换下分别由方程(26.2.17)和(26.3.16)给出.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f815ab667da80eecb2eaa">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { \delta \lambda = \left( \frac12\Big[\partial_\mu\not\!\mathcal V,\gamma^\mu\Big] + \mathrm{i} \gamma _ { 5 } D \right) \alpha =(-iS^{\mu\nu}V_{\mu\nu}+i\gamma_5 D)\alpha } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \delta D = \mathrm{i} \Big ( \bar { \alpha } \gamma _ { 5 } \not\!\partial\, \lambda \Big ) . } } \end{array} \tag{26.2.16-26.2.17}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
无论以哪种方法, 我们发现方程(26.7.1)中的流 $`K ^ { \mu }`$ 是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f810ca352de9521d2cfa0">
		$$
		\delta { \mathcal L } = \left( \bar { \alpha } \partial _ { \mu } K ^ { \mu } \right) , \tag{26.7.1}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81f3be20c7d716a3e177">
	$$
																							\begin{aligned}
K^\mu=\frac1{\sqrt2}\gamma^\mu\big[&-(\not\!\partial\phi^n)\psi _ { R } {} _ { n }
-(\not\!\partial\phi ^ { \dagger } _ { n })\psi _ { L } ^ { n }
+\mathcal F ^ { \dagger } _ { n }\psi _ { L } ^ { n }
+\mathcal F^n\psi _ { R } {} _ { n }\\
&+2f_n(\phi)\psi _ { L } ^ { n }
+2f^{\dagger n}(\phi^\dagger)\psi _ { R } {} _ { n }\big].
\end{aligned}\tag{26.7.9}
	$$
</synced_block>
将(26.7.8)和(26.7.9)加起来就给出了这类理论的超对称流
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8187afc6e0c859787372">
		$$
		\begin{array} { l } { { { \displaystyle N ^ { \mu } = \frac { 1 } { \sqrt 2 } \left[ 2 \left( \partial ^ { \mu } \phi ^ { \dagger } _ { n } \right) \psi _ { L } ^ { n } + 2 \left( \partial ^ { \mu } \phi ^ { n } \right) \psi _ { R } {} _ { n } + \left( \not\!\partial\, \phi ^ { n } \right) \gamma ^ { \mu } \psi _ { R } {} _ { n } + \left( \not\!\partial\, \phi ^ { \dagger } _ { n } \right) \gamma ^ { \mu } \psi _ { L } ^ { n } \right. } } } \\ { { { \displaystyle \left. - \mathcal{F} ^ { n } \gamma ^ { \mu } \psi _ { R } {} _ { n } - \mathcal{F} ^ { \dagger } _ { n } \gamma ^ { \mu } \psi _ { L } ^ { n } \right] . } } } \end{array} \tag{26.7.8}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81f3be20c7d716a3e177">
		$$
																								\begin{aligned}
K^\mu=\frac1{\sqrt2}\gamma^\mu\big[&-(\not\!\partial\phi^n)\psi _ { R } {} _ { n }
-(\not\!\partial\phi ^ { \dagger } _ { n })\psi _ { L } ^ { n }
+\mathcal F ^ { \dagger } _ { n }\psi _ { L } ^ { n }
+\mathcal F^n\psi _ { R } {} _ { n }\\
&+2f_n(\phi)\psi _ { L } ^ { n }
+2f^{\dagger n}(\phi^\dagger)\psi _ { R } {} _ { n }\big].
\end{aligned}\tag{26.7.9}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f817da994f13a0440c19e">
	$$
																																																																													S^\mu=\sqrt2\left[(\not\!\partial\phi^n)\gamma^\mu\psi _ { R } {} _ { n }
+(\not\!\partial\phi ^ { \dagger } _ { n })\gamma^\mu\psi _ { L } ^ { n }
+f_n(\phi)\gamma^\mu\psi _ { L } ^ { n }
+f^{\dagger n}(\phi^\dagger)\gamma^\mu\psi _ { R } {} _ { n }\right]. \tag{26.7.10}
	$$
</synced_block>
这样一来, 用正则对易关系和反对易关系证实 $`\int \mathrm { d } ^ { 3 } x \ : S ^ { 0 }`$ 满足对易关系(26.7.6)就是直接的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8192a37cd8e28a8234ee">
		$$
		\left[ \int \mathrm { d } ^ { 3 } x \left( \bar { \alpha } S ^ { 0 } \right) , \chi ^ { \ell } \right] = \mathrm{i} \delta \chi ^ { \ell } , \tag{26.7.6}
		$$
	</synced_block_reference>
</callout>
<empty-block/>
对称流有另外一种定义, 即按照物质作用量对定域对称变换的响应来定义, 当相应的对称性被“规范化”后, 这个定义特别有用, 而当我们在第31章转向超引力理论时, 超对称就会变成这样的情况.
在没有超引力场的情况下, 作用量在定域超对称变换下不是不变的.
如果我们做这样一个带有时空相关参量 $`\alpha ( x )`$ 的变换, 为了使得作用量的变化在 $`\alpha ( x )`$ 是常数时为零, 它必须(即使场方程没有被满足)采取如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cf9e59cd98729a1ffc">
	$$
	\delta I = - \int \mathrm { d } ^ { 4 } x \Big ( ( \partial _ { \mu } \bar { \alpha } ( x ) ) S ^ { \mu } ( x ) \Big ) , \tag{26.7.11}
	$$
</synced_block>
其中 $`S ^ { \mu } ( x )`$ 是Majorana旋量算符系数的4 -矢.
<span color="yellow_bg">由于在我们将整体超对称变换推广至定域变换后,一般情况下, 对于场 </span>$`\chi`$<span color="yellow_bg"> 在定域对称变换的变化 </span>$`\delta \chi`$<span color="yellow_bg"> , 我们可以让它以任意的方式依赖于 </span>$`\alpha ( x )`$<span color="yellow_bg"> 的导数,所以这并不唯一地定义 </span>$`S ^ { \mu } ( x )`$<span color="yellow_bg"> .</span>
然而, 有一种定义定域对称变换的方式保证了方程(26.7.11)中的系数 $`S ^ { \mu } ( x )`$ 与方程(26.7.4)定义的流相同, 而正如我们看到的, 后者生成了对称变换, 即方程(26.7.6).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cf9e59cd98729a1ffc">
		$$
		\delta I = - \int \mathrm { d } ^ { 4 } x \Big ( ( \partial _ { \mu } \bar { \alpha } ( x ) ) S ^ { \mu } ( x ) \Big ) , \tag{26.7.11}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8100a5dcfeb7f796d407">
		$$
		S ^ { \mu } \equiv N ^ { \mu } + K ^ { \mu } , \tag{26.7.4}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8192a37cd8e28a8234ee">
		$$
		\left[ \int \mathrm { d } ^ { 3 } x \left( \bar { \alpha } S ^ { 0 } \right) , \chi ^ { \ell } \right] = \mathrm{i} \delta \chi ^ { \ell } , \tag{26.7.6}
		$$
	</synced_block_reference>
</callout>
<span color="yellow_bg">方法是指定正则场或辅助场 </span>$`\chi ^ { \ell }`$<span color="yellow_bg"> 的超对称变换中不出现 </span>$`\alpha ( x )`$<span color="yellow_bg"> 的导数.</span>
例如, 对于左手征超场的分量, 变换规则(26.3.15)—(26.3.17)的定域版本是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81e69ad5f96aecfbbb7c">
	$$
	\begin{array} { r l } & { \delta \psi _ { L } ( x ) = \sqrt { 2 } \partial _ { \mu } \phi ( x ) \gamma ^ { \mu } \alpha _ { R } ( x ) + \sqrt { 2 } \mathcal{F} ( x ) \alpha _ { L } ( x ) , } \\ & { \delta \mathcal{F} ( x ) = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } ( x ) \partial \psi _ { L } ( x ) \Big ) , } \\ & { \delta \phi ( x ) = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } ( x ) \psi _ { L } ( x ) \Big ) . } \end{array} \tag{26.7.12-26.7.14}
	$$
</synced_block>
方程(26.3.21)表明超场可以表示成**它在 **$`x _ { + } ^ { \mu }`$** 没有导数的分量场**, 所以这个超场的变换规则可以表示成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81dab423c0265e13f79d">
		$$
		\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f812dbfb5c7a575436afe">
	$$
	\delta \Phi ( x , \theta ) = \Big ( \bar { \alpha } ( x _ { + } ) \mathcal{Q} \Big ) \Phi ( x , \theta ) , \tag{26.7.15}
	$$
</synced_block>
其中 $`\mathcal{Q}`$ 是算符(26.2.2).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f812e8a66c9b63a4d3331">
		$$
		\mathcal{Q} \equiv - \frac { \partial } { \partial \bar { \theta } } + \gamma ^ { \mu } \theta \frac { \partial } { \partial x ^ { \mu } } , \tag{26.2.2}
		$$
	</synced_block_reference>
</callout>
当定域对称变换以这种方式定义后, 它们诱导出的作用量的变化由两项组成.
首先, 尽管正则场在超对称变换下的变分不包含 $`\alpha ( x )`$ 的导数, 但是正则场导数的变分确实包含 $`\alpha ( x )`$ 的导数.
除了要将 $`\bar { \alpha }`$ 换成 $`\partial _ { \mu } \bar { \alpha }`$ , 它产生的拉格朗日密度的变化与方程(26.7.2)相同:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f818e9351fec7544fad6a">
		$$
		\frac { \partial _ { R } \mathcal{L} } { \partial ( \partial _ { \mu } \chi ^ { \ell } ) } \delta \chi ^ { \ell } \equiv - \Big ( \bar { \alpha } N ^ { \mu } \Big ) \tag{26.7.2}
		$$
	</synced_block_reference>
</callout>
$$
\delta _ { 1 } I = - \int \mathrm { d } ^ { 4 } x \Big ( [ \partial _ { \mu } \bar { \alpha } ( x ) ] N ^ { \mu } ( x ) \Big ) .
$$
作用量变化中的第二项源于如下的事实: 即使在不含 $`\alpha ( x )`$ 导数的那部分超对称变换下, 拉格朗日密度也不是不变的.
根据方程(26.7.1), 它产生的作用量的变化是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f810ca352de9521d2cfa0">
		$$
		\delta { \mathcal L } = \left( \bar { \alpha } \partial _ { \mu } K ^ { \mu } \right) , \tag{26.7.1}
		$$
	</synced_block_reference>
</callout>
$$
\delta _ { 2 } I = \int \mathrm { d } ^ { 4 } x \Bigl ( \bar { \alpha } ( x ) \partial _ { \mu } K ^ { \mu } ( x ) \Bigr ) = - \int \mathrm { d } ^ { 4 } x \Bigl ( \bigl ( \partial _ { \mu } \bar { \alpha } ( x ) \bigr ) K ^ { \mu } ( x ) \Bigr ) .
$$
将 $`\delta _ { 1 } I`$ 和 $`\delta _ { 2 } I`$ 加起来就给出作用量形式为(26.7.11)的总变化, 其中 $`S ^ { \mu } ( x )`$ 由方程(26.7.4)给出, 这正是所要证明的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cf9e59cd98729a1ffc">
		$$
		\delta I = - \int \mathrm { d } ^ { 4 } x \Big ( ( \partial _ { \mu } \bar { \alpha } ( x ) ) S ^ { \mu } ( x ) \Big ) , \tag{26.7.11}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8100a5dcfeb7f796d407">
		$$
		S ^ { \mu } \equiv N ^ { \mu } + K ^ { \mu } , \tag{26.7.4}
		$$
	</synced_block_reference>
</callout>
即使在这样指定分量场的变换性质后, 超对称流 $`S ^ { \mu } ( x )`$ 也没有被方程(26.7.11)唯一地指定, 这是因为我们总可以引入修正流
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cf9e59cd98729a1ffc">
		$$
		\delta I = - \int \mathrm { d } ^ { 4 } x \Big ( ( \partial _ { \mu } \bar { \alpha } ( x ) ) S ^ { \mu } ( x ) \Big ) , \tag{26.7.11}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8164958fed793be5bc6c">
	$$
	S _ { \mathrm{new} } ^ { \mu } = S ^ { \mu } + \partial _ { \nu } A ^ { \mu \nu } , \tag{26.7.16}
	$$
</synced_block>
其中 $`A ^ { \mu \nu } = - A ^ { \nu \mu }`$ 是Majorana旋量的任意反对称张量.
无论场方程是否被满足, $`\partial _ { \nu } A ^ { \mu \nu }`$ 这一项总是守恒的, 并且它的时间分量是空间导数, 所以 $`\begin{array} { r } { \int \mathrm { d } ^ { 3 } x S _ { \mathrm{new} } ^ { 0 } = \int \mathrm { d } ^ { 3 } x S ^ { 0 } } \end{array}`$ , 这使得方程(26.7.6)保持不变.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8192a37cd8e28a8234ee">
		$$
		\left[ \int \mathrm { d } ^ { 3 } x \left( \bar { \alpha } S ^ { 0 } \right) , \chi ^ { \ell } \right] = \mathrm{i} \delta \chi ^ { \ell } , \tag{26.7.6}
		$$
	</synced_block_reference>
</callout>
事实上 $`A ^ { \mu \nu }`$ 有一个特殊的选择使得 $`\gamma _ { \mu } S _ { \mathrm{new} } ^ { \mu }`$ 有这样的方便特征: 它衡量了理论对标度不变性的破坏程度.
通过使用从拉格朗日密度(26.4.7)导出的Dirac方程:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#197b2065da3e45b087689719e6ad1c23">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { \dagger } _ { n } \partial ^ { \mu } \phi ^ { n } - \frac { 1 } { 2 } \Bigl ( \bar { \psi } _ { L } {} _ { n } \gamma ^ { \mu } \partial _ { \mu } \psi _ { L } ^ { n } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \bar { \psi } _ { L } {} _ { n } ) \gamma ^ { \mu } \psi _ { L } ^ { n } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } f _ { n m } ( \phi ) \left( \bar { \psi } _ { R } {} ^ { n } \psi _ { L } ^ { m } \right) - \frac { 1 } { 2 } f ^ { \dagger n m } ( \phi ^ { \dagger } ) \left( \bar { \psi } _ { L } {} _ { n } \psi _ { R } {} _ { m } \right) } \\ { \displaystyle \qquad - f ^ { \dagger n } ( \phi ^ { \dagger } ) f _ { n } ( \phi ) . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81978272e85ea9141d49">
	$$
												\not\!\partial\psi _ { L } ^ { m }
=-f^{\dagger mn}(\phi^\dagger)\psi _ { R } {} _ { n },
\qquad
\not\!\partial\psi _ { R } {} _ { m }
=-f_{mn}(\phi)\psi _ { L } ^ { n }. \tag{26.7.17}
	$$
</synced_block>
直接计算给出
$$
\gamma_\mu S^\mu=-2\sqrt2\left\{
\not\!\partial\left(\phi^n\psi _ { R } {} _ { n }+\phi ^ { \dagger } _ { n }\psi _ { L } ^ { n }\right)
+(\phi^m f_{nm}-2f_n)\psi _ { L } ^ { n }
+(\phi ^ { \dagger } _ { m }f^{\dagger nm}-2f^{\dagger n})\psi _ { R } {} _ { n }
\right\}.
$$
<callout icon="💡" color="gray_bg">
	$$
												S^\mu=\sqrt2\left[(\not\!\partial\phi^n)\gamma^\mu\psi _ { R } {} _ { n }
+(\not\!\partial\phi ^ { \dagger } _ { n })\gamma^\mu\psi _ { L } ^ { n }
+f_n(\phi)\gamma^\mu\psi _ { L } ^ { n }
+f^{\dagger n}(\phi^\dagger)\gamma^\mu\psi _ { R } {} _ { n }\right]. \tag{26.7.10}
	$$
</callout>
通过引入方程(26.7.16)那样一般类型的修正超对称流, 我们可以消除掉第一项:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8164958fed793be5bc6c">
		$$
		S _ { \mathrm{new} } ^ { \mu } = S ^ { \mu } + \partial _ { \nu } A ^ { \mu \nu } , \tag{26.7.16}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f815dba68d17d44237801">
	$$
	S _ { \mathrm{new} } ^ { \mu } = S ^ { \mu } + \frac { \sqrt { 2 } } { 3 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] \partial _ { \nu } \Big ( \phi ^ { n } \psi _ { R } {} _ { n } + \phi ^ { \dagger } _ { n } \psi _ { L } ^ { n } \Big ) , \tag{26.7.18}
	$$
</synced_block>
使得
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81f4b958fd6ab8a7de30">
	$$
												\gamma_\mu S_{\mathrm{new}}^\mu
=-2\sqrt2\left[
(\phi^m f_{nm}-2f_n)\psi _ { L } ^ { n }
+(\phi ^ { \dagger } _ { m }f^{\dagger nm}-2f^{\dagger n})\psi _ { R } {} _ { n }
\right]. \tag{26.7.19}
	$$
</synced_block>
对于标度不变的拉格朗日密度, 即 $`f ( \Phi )`$ 是 $`\Phi ^ { n }`$ 的三阶齐次多项式的拉格朗日密度, 右边为零.
<empty-block/>
我们现在转向超对称流的超对称变换性质.
可以直接验证方程(26.7.18)和(26.7.10)给出的流与一个非手征实超场 $`\Theta _ { \mu }`$ 的 $`\omega`$ -分量 $`\omega _ { \mu } ^ { \Theta }`$ 有如下的关系
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f815dba68d17d44237801">
		$$
		S _ { \mathrm{new} } ^ { \mu } = S ^ { \mu } + \frac { \sqrt { 2 } } { 3 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] \partial _ { \nu } \Big ( \phi ^ { n } \psi _ { R } {} _ { n } + \phi ^ { \dagger } _ { n } \psi _ { L } ^ { n } \Big ) , \tag{26.7.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f817da994f13a0440c19e">
		$$
																																																																														S^\mu=\sqrt2\left[(\not\!\partial\phi^n)\gamma^\mu\psi _ { R } {} _ { n }
+(\not\!\partial\phi ^ { \dagger } _ { n })\gamma^\mu\psi _ { L } ^ { n }
+f_n(\phi)\gamma^\mu\psi _ { L } ^ { n }
+f^{\dagger n}(\phi^\dagger)\gamma^\mu\psi _ { R } {} _ { n }\right]. \tag{26.7.10}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81708b14d39b093e501a">
	$$
	S _ { \mathrm{new} } ^ { \mu } = - 2  { \Theta _\mu } + 2 \gamma ^ { \mu } \gamma ^ { \nu } \Theta _\mu  \tag{26.7.20}|_{\omega}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cead0be409310ceb93">
	$$
	\Theta _ { \mu } = \frac { \mathrm{i} } { 12 } \left[ 4 \Phi ^ { \dagger } _ { n } \partial _ { \mu } \Phi ^ { n } - 4 \Phi ^ { n } \partial _ { \mu } \Phi ^ { \dagger } _ { n } + \left( ( \bar { \mathcal{D} } \Phi ^ { \dagger } _ { n } ) \gamma _ { \mu } ( \mathcal{D} \Phi ^ { n } ) \right) \right] . \tag{26.7.21}
	$$
</synced_block>
\\\*\\\*这里我们引入一个将在第 31 章广泛使用的符号约定; 
延续方程(26.2.10), 任意超场 $`S ( x , \theta )`$ 的分量 $`\mathcal{O} ^ { S } , \omega ^ { S } , \ M ^ { S }`$ $`N ^ { S }`$ , $`V _ { \nu } ^ { S }`$ , $`\lambda ^ { S }`$ 和 $`D ^ { S }`$ 通过如下展开定义:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { { S ( x , \theta ) = C ^ { S } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ^ { S } ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ^ { S } ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ^ { S } ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \nu } \theta \Big ) V _ { \nu } ^ { S } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \Big [ \lambda ^ { S } ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ^ { S } ( x ) \Big ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg [ D ^ { S } ( x ) + \frac { 1 } { 2 } \Box C ^ { S } ( x ) \Bigg ] ~ . } } \end{array}
$$
<empty-block/>
超场 $`\Theta ^ { \mu }`$ 被称为超流.
超流服从的守恒律包含了超对称流的守恒以及其它很多守恒律.
为了推导它, 我们可以使用反对易关系(26.2.30)写下†
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81738a97d99db41eabd6">
		$$
		\Big \{ \mathcal{D} _ { \alpha } , \overline { { { \mathcal{D} } } } _ { \beta } \Big \} = - 2 \gamma _ { \alpha \beta } ^ { \mu } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.30}
		$$
	</synced_block_reference>
</callout>
$$
\left[
\mathcal D_R,
\left((\overline{\mathcal D})_L\mathcal D_L\right)
\right]
=
-4\,\gamma^\mu\partial_\mu\mathcal D_L .
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	† 要注意，$`(\overline{\mathcal D})_L`$ 和 $`(\overline{\mathcal D})_R`$ 是 covariant adjoint $`\overline{\mathcal D}`$ 的 left-handed 与 right-handed components；它们不是 $`\mathcal D_L`$ 和 $`\mathcal D_R`$ 各自的 covariant adjoints $`\overline{(\mathcal D_L)}`$ 和 $`\overline{(\mathcal D_R)}`$。
</callout>
加上手征条件 $`\mathcal{D} _ { R } \Phi ^ { n } = \mathcal{D} _ { L } \Phi ^ { \dagger } _ { n } = 0`$ , 这给出
$$
\gamma ^ { \mu } \mathcal{D} _ { L } \left[ \Phi ^ { \dagger } _ { n } \partial _ { \mu } \Phi ^ { n } - \Phi ^ { n } \partial _ { \mu } \Phi ^ { \dagger } _ { n } \right] = - \frac { 1 } { 4 } \Phi ^ { \dagger } _ { n } \mathcal{D} _ { R } \left( \bar { \mathcal{D} } _ { L } \mathcal{D} _ { L } \right) \Phi ^ { n } - ( \not\!\partial\, \Phi ^ { \dagger } _ { n } ) \mathcal{D} _ { L } \Phi ^ { n }
$$
和
$$
\gamma ^ { \mu } \mathcal{D} _ { L } \left( ( \bar { \mathcal{D} } \Phi ^ { \dagger } _ { n } ) \gamma _ { \mu } ( \mathcal{D} \Phi ^ { n } ) \right) = 4 \left( \not\!\partial\, \Phi ^ { \dagger } _ { n } \right) \mathcal{D} \Phi ^ { n } + 2 \mathcal{D} \Phi ^ { \dagger } _ { n } \left( \bar { \mathcal{D} } _ { L } \mathcal{D} _ { L } \right) \Phi ^ { n } ,
$$
使得超场(26.7.21)满足
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cead0be409310ceb93">
		$$
		\Theta _ { \mu } = \frac { \mathrm{i} } { 12 } \left[ 4 \Phi ^ { \dagger } _ { n } \partial _ { \mu } \Phi ^ { n } - 4 \Phi ^ { n } \partial _ { \mu } \Phi ^ { \dagger } _ { n } + \left( ( \bar { \mathcal{D} } \Phi ^ { \dagger } _ { n } ) \gamma _ { \mu } ( \mathcal{D} \Phi ^ { n } ) \right) \right] . \tag{26.7.21}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81c0a695c4d224abc4c3">
	$$
	\gamma _ { \mu } \mathcal{D} _ { L } \Theta ^ { \mu } = \textstyle { \frac { 1 } { 6 } } \mathrm{i} \bigl ( \mathcal{D} _ { R } \Phi ^ { \dagger } _ { n } \bigr ) \biggl ( \bar { \mathcal D } _ { L } \mathcal{D} _ { L } \biggr ) \Phi ^ { n } - \textstyle { \frac { 1 } { 12 } } \mathrm{i} \Phi ^ { \dagger } _ { n } \mathcal{D} _ { R } \Bigl ( \bar { \mathcal D } _ { L } \mathcal{D} _ { L } \Bigr ) \Phi ^ { n } . \tag{26.7.22}
	$$
</synced_block>
我们在26.6 节看到, 拉格朗日密度(26.4.7)的场方程可以表示成如下形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#197b2065da3e45b087689719e6ad1c23">
		$$
		\begin{array} { l } { \displaystyle \mathcal{L} = - \partial _ { \mu } \phi ^ { \dagger } _ { n } \partial ^ { \mu } \phi ^ { n } - \frac { 1 } { 2 } \Bigl ( \bar { \psi } _ { L } {} _ { n } \gamma ^ { \mu } \partial _ { \mu } \psi _ { L } ^ { n } \Bigr ) + \frac { 1 } { 2 } \Bigl ( ( \partial _ { \mu } \bar { \psi } _ { L } {} _ { n } ) \gamma ^ { \mu } \psi _ { L } ^ { n } \Bigr ) } \\ { \displaystyle \qquad - \frac { 1 } { 2 } f _ { n m } ( \phi ) \left( \bar { \psi } _ { R } {} ^ { n } \psi _ { L } ^ { m } \right) - \frac { 1 } { 2 } f ^ { \dagger n m } ( \phi ^ { \dagger } ) \left( \bar { \psi } _ { L } {} _ { n } \psi _ { R } {} _ { m } \right) } \\ { \displaystyle \qquad - f ^ { \dagger n } ( \phi ^ { \dagger } ) f _ { n } ( \phi ) . } \end{array} \tag{26.4.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f812c8f84ce07c14ef603">
	$$
												(\bar { \mathcal D } _L\mathcal D_L)\Phi^n
=-4f^{\dagger n}(\Phi^\dagger). \tag{26.7.23}
	$$
</synced_block>
在方程(26.7.22)中使用上式最后给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81c0a695c4d224abc4c3">
		$$
		\gamma _ { \mu } \mathcal{D} _ { L } \Theta ^ { \mu } = \textstyle { \frac { 1 } { 6 } } \mathrm{i} \bigl ( \mathcal{D} _ { R } \Phi ^ { \dagger } _ { n } \bigr ) \biggl ( \bar { \mathcal D } _ { L } \mathcal{D} _ { L } \biggr ) \Phi ^ { n } - \textstyle { \frac { 1 } { 12 } } \mathrm{i} \Phi ^ { \dagger } _ { n } \mathcal{D} _ { R } \Bigl ( \bar { \mathcal D } _ { L } \mathcal{D} _ { L } \Bigr ) \Phi ^ { n } . \tag{26.7.22}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81598603df5c5229074d">
	$$
																							\begin{aligned}
\gamma^\mu\mathcal D_L\Theta_\mu
&=-\frac{2i}{3}(\mathcal D_R\Phi ^ { \dagger } _ { n })f^{\dagger n}
+\frac{i}{3}\Phi ^ { \dagger } _ { n }\mathcal D_Rf^{\dagger n}\\
&=\frac{i}{3}\mathcal D_R\!\left[
\Phi ^ { \dagger } _ { n }f^{\dagger n}-3f^\dagger
\right].
\end{aligned}\tag{26.7.24}
	$$
</synced_block>
方程(26.7.24)的厄米共轭是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81598603df5c5229074d">
		$$
																								\begin{aligned}
\gamma^\mu\mathcal D_L\Theta_\mu
&=-\frac{2i}{3}(\mathcal D_R\Phi ^ { \dagger } _ { n })f^{\dagger n}
+\frac{i}{3}\Phi ^ { \dagger } _ { n }\mathcal D_Rf^{\dagger n}\\
&=\frac{i}{3}\mathcal D_R\!\left[
\Phi ^ { \dagger } _ { n }f^{\dagger n}-3f^\dagger
\right].
\end{aligned}\tag{26.7.24}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ee91cfd2d16deb2185">
	$$
												\gamma^\mu\mathcal D_R\Theta_\mu
=-\frac{i}{3}\mathcal D_L\left[\Phi^n f_n-3f\right]. \tag{26.7.25}
	$$
</synced_block>
这样, 它与方程(26.7.24)给出守恒流
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81598603df5c5229074d">
		$$
																								\begin{aligned}
\gamma^\mu\mathcal D_L\Theta_\mu
&=-\frac{2i}{3}(\mathcal D_R\Phi ^ { \dagger } _ { n })f^{\dagger n}
+\frac{i}{3}\Phi ^ { \dagger } _ { n }\mathcal D_Rf^{\dagger n}\\
&=\frac{i}{3}\mathcal D_R\!\left[
\Phi ^ { \dagger } _ { n }f^{\dagger n}-3f^\dagger
\right].
\end{aligned}\tag{26.7.24}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ef865dc5e544ad48c6">
	$$
	\gamma ^ { \mu } { \mathcal{D} } \Theta _ { \mu } = { \mathcal{D} } X , \tag{26.7.26}
	$$
</synced_block>
其中 $`X`$ 是一个实手征超场, 它在这类理论中(在相差一个额外的常数的意义下)给定为
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81a4814fcfd10e80d129">
	$$
	X=\frac23\operatorname{Im}\left[\Phi^n f_n-3f\right]. \tag{26.7.27}
	$$
</synced_block>
尽管这里仅对手征超场的可重整理论做了推导, 我们可以预期守恒律(26.7.27)在更一般的情况下也会成立, <span color="yellow_bg">当然, 由于它还包含其它守恒律, </span>$`X`$<span color="yellow_bg"> 不一定由方程(26.7.27)给出.</span>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81a4814fcfd10e80d129">
		$$
		X=\frac23\operatorname{Im}\left[\Phi^n f_n-3f\right]. \tag{26.7.27}
		$$
	</synced_block_reference>
</callout>
(31.4 节将会给出 $`X`$ 的一个推广公式.) 
为了推导这些关系, 我们必须用方程(26.2.10)将 $`\Theta _ { \mu }`$ 表示成 $`C _ { \mu } ^ { \Theta }`$ , $`\omega _ { \mu } ^ { \Theta }`$ 等分
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
量, 并用方程(26.3.9)将手征超场 $`X`$ 表示成 $`A ^ { X }`$ , $`\psi ^ { X }`$ 等分量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81208604d4fff421664a">
		$$
		\begin{array} { l } { { \displaystyle { X ( x , \theta ) = A ( x ) - \left( \bar { \theta } \psi ( x ) \right) + \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) F ( x ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) G ( x ) } } } \\ { { \displaystyle { ~ + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } B ( x ) + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \gamma _ { 5 } \not\!\partial\, \psi ( x ) \Big ) } } } \\ { { \displaystyle { ~ - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box A ( x ) . } } } \end{array} \tag{26.3.9}
		$$
	</synced_block_reference>
</callout>
在方程(26.A.9), (26.A.16) (26.A.17)和Dirac矩阵恒等式的帮助下
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ed90b4fd1a2f33b2df">
		$$
		\begin{array} { r } { s \bar { s } = - \frac { 1 } { 4 } ( \bar { s } s ) + \frac { 1 } { 4 } \gamma _ { 5 } \gamma _ { \mu } ( \bar { s } \gamma _ { 5 } \gamma ^ { \mu } s ) - \frac { 1 } { 4 } \gamma _ { 5 } \left( \bar { s } \gamma _ { 5 } s \right) . } \end{array} \tag{26.A.9}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ba90b3cb0dc40f0b4c">
		$$
		s _ { \alpha } \left( \bar { s } s \right) = - ( \gamma _ { 5 } s ) _ { \alpha } \left( \bar { s } \gamma _ { 5 } s \right) \tag{26.A.16}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8168865bf41f3dacf374">
		$$
		s _ { \alpha } \left( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \right) = - ( \gamma _ { \mu } s ) _ { \alpha } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) . \tag{26.A.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81e8bf6fdd5761a61c37">
	$$
	\begin{array} { r } { \left[ \gamma ^ { \rho } , \gamma ^ { \sigma } \right] = - \frac { 1 } { 2 } \mathrm{i} \epsilon ^ { \rho \sigma \mu \nu } \gamma _ { 5 } \left[ \gamma _ { \mu } , \gamma _ { \nu } \right] , } \end{array} \tag{26.7.28}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81f6a64fca1555cb2e40">
	$$
	\gamma ^ { \mu } \gamma ^ { \rho } \gamma ^ { \sigma } = \eta ^ { \mu \rho } \gamma ^ { \sigma } - \eta ^ { \mu \sigma } \gamma ^ { \rho } + \eta ^ { \sigma \rho } \gamma ^ { \mu } + \mathrm{i} \gamma _ { 5 } \epsilon ^ { \mu \sigma \rho \nu } \gamma _ { \nu } , \tag{26.7.29}
	$$
</synced_block>
我们可以将方程(26.7.26)两边展到如下各项上
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ef865dc5e544ad48c6">
		$$
		\gamma ^ { \mu } { \mathcal{D} } \Theta _ { \mu } = { \mathcal{D} } X , \tag{26.7.26}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r l } & { 1 , \ \theta , \ \gamma _ { 5 } \theta , \ \gamma ^ { \nu } \theta , \ \gamma _ { 5 } \gamma ^ { \nu } \theta , \ \gamma _ { 5 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] \theta , \ } \\ & { \left( \bar { \theta } \theta \right) , \ \left( \bar { \theta } \gamma _ { 5 } \theta \right) , \ \left( \bar { \theta } \gamma _ { 5 } \gamma _ { \nu } \theta \right) , \ } \\ & { \theta \left( \bar { \theta } \gamma _ { 5 } \theta \right) , \ \gamma _ { 5 } \theta \left( \bar { \theta } \gamma _ { 5 } \theta \right) , \ \gamma ^ { \nu } \theta \left( \bar { \theta } \gamma _ { 5 } \theta \right) , \ } \\ & { \gamma ^ { \nu } \gamma _ { 5 } \theta \left( \bar { \theta } \gamma _ { 5 } \theta \right) , \ [ \gamma ^ { \rho } , \gamma ^ { \sigma } ] \theta \left( \bar { \theta } \gamma _ { 5 } \theta \right) , \ \left( \bar { \theta } \gamma _ { 5 } \theta \right) ^ { 2 } . } \end{array}
$$
分别比对 $`1 , \theta , \gamma _ { 5 } \theta , \gamma ^ { \nu } \theta , \gamma _ { 5 } \gamma ^ { \nu } \theta , \gamma _ { 5 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] \theta`$ 的系数, 这给出结果††
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f814680abedfbebef8ffe">
	$$
								\begin{aligned}
\psi^X&=-\mathrm i\gamma_5\gamma^\mu\omega_\mu^\Theta,\\
F^X&=\partial^\mu C_\mu^\Theta,\\
G^X&=(V^\Theta)_\mu{}^\mu,\\
\partial_\mu A^X&=-N_\mu^\Theta,\\
\partial_\mu B^X&=M_\mu^\Theta,\\
0&=V_{\mu\nu}^\Theta-V_{\nu\mu}^\Theta
+\epsilon_{\mu\nu\rho\sigma}\partial^\sigma C^{\Theta\rho}.
\end{aligned}\tag{26.7.30--26.7.35}
	$$
</synced_block>
<callout icon="💡" color="gray_bg">
	$$
	X=\frac23\operatorname{Im}\left[\Phi^n f_n-3f\right]. \tag{26.7.27}
	$$
</callout>
比对 $`( { \bar { \theta } } \theta )`$ 或 $`( \bar { \theta } \gamma _ { 5 } \theta )`$ 的系数给出同一个结果:
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8182ac46e323e08aac04">
	$$
	0 = \gamma ^ { \mu } \lambda _ { \mu } ^ { \Theta } , \tag{26.7.36}
	$$
</synced_block>
比对 $`( \bar { \theta } \gamma _ { 5 } \gamma ^ { \nu } \theta )`$ 的系数给出结果
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8155b886efae0925b008">
	$$
	- \mathrm{i} \gamma _ { 5 } \left[ \gamma ^ { \nu } , \rlap / \partial \right] \psi ^ { X } = 2 \gamma ^ { \mu } \gamma ^ { \nu } \lambda _ { \mu } ^ { \Theta } + \gamma ^ { \mu } \left[ \gamma ^ { \nu } , \rlap / \partial \right] \omega _ { \mu } ^ { \Theta } \ . \tag{26.7.37}
	$$
</synced_block>
我们从方程(26.7.30), (26.7.36)和(26.7.37)获得了超对称流(26.7.20)的守恒:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8182ac46e323e08aac04">
		$$
		0 = \gamma ^ { \mu } \lambda _ { \mu } ^ { \Theta } , \tag{26.7.36}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8155b886efae0925b008">
		$$
		- \mathrm{i} \gamma _ { 5 } \left[ \gamma ^ { \nu } , \rlap / \partial \right] \psi ^ { X } = 2 \gamma ^ { \mu } \gamma ^ { \nu } \lambda _ { \mu } ^ { \Theta } + \gamma ^ { \mu } \left[ \gamma ^ { \nu } , \rlap / \partial \right] \omega _ { \mu } ^ { \Theta } \ . \tag{26.7.37}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81708b14d39b093e501a">
		$$
		S _ { \mathrm{new} } ^ { \mu } = - 2  { \Theta _\mu } + 2 \gamma ^ { \mu } \gamma ^ { \nu } \Theta _\mu  \tag{26.7.20}|_{\omega}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81669a5dec4e625fa2f8">
	$$
	0 = \partial _ { \mu } S _ { \mathrm{new} } ^ { \mu } = - 2 \partial ^ { \mu } \omega _ { \mu } ^ { \Theta } + 2 \not\!\partial\, \gamma ^ { \mu } \omega _ { \mu } ^ { \Theta } , \tag{26.7.38}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
																		0=
\partial_\mu(S_{W,\mathrm{new}}^\mu)_\alpha
=
-2\partial^\mu(\omega_{\mu,W}^{\Theta})_\alpha
+2(\gamma_W^\rho)_\alpha{}^\beta\partial_\rho
(\gamma_W^\mu)_\beta{}^\gamma
(\omega_{\mu,W}^{\Theta})_\gamma .
	$$
</callout>
以及 $`\lambda _ { \mu } ^ { \Theta }`$ 和 $`\omega _ { \mu } ^ { \Theta }`$ 之间的关系:
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8114b3affb355c7d9890">
	$$
	\lambda _ { \nu } ^ { \Theta } = - \not\!\partial\, \omega _ { \nu } ^ { \Theta } + \partial _ { \nu } \gamma ^ { \mu } \omega _ { \mu } ^ { \Theta } . \tag{26.7.39}
	$$
</synced_block>
比对 $`\theta ( \bar { \theta } \gamma _ { 5 } \theta )`$ 和 $`\gamma _ { 5 } \theta ( \bar { \theta } \gamma _ { 5 } \theta )`$ 的系数所给出的关系可以分别通过对方程(26.7.34)和(26.7.33)取散度获得.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f814680abedfbebef8ffe">
		$$
									\begin{aligned}
\psi^X&=-\mathrm i\gamma_5\gamma^\mu\omega_\mu^\Theta,\\
F^X&=\partial^\mu C_\mu^\Theta,\\
G^X&=(V^\Theta)_\mu{}^\mu,\\
\partial_\mu A^X&=-N_\mu^\Theta,\\
\partial_\mu B^X&=M_\mu^\Theta,\\
0&=V_{\mu\nu}^\Theta-V_{\nu\mu}^\Theta
+\epsilon_{\mu\nu\rho\sigma}\partial^\sigma C^{\Theta\rho}.
\end{aligned}\tag{26.7.30--26.7.35}
		$$
	</synced_block_reference>
</callout>
比对 $`\gamma ^ { \rho } \theta ( \bar { \theta } \gamma _ { 5 } \theta )`$ 的系数给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81d991d6d7fabafb22d3">
	$$
	\partial _ { \rho } G ^ { X } = \partial ^ { \mu } V _ { \mu \rho } ^ { \Theta } + \partial ^ { \mu } V _ { \rho \mu } ^ { \Theta } - \partial _ { \rho } V _ { \lambda } {} ^ { \Theta \lambda } , \tag{26.7.40}
	$$
</synced_block>
结合方程(26.7.32), 这给出守恒律
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8169a39bece8a35a14fc">
	$$
	\partial _ { \mu } T ^ { \mu \nu } = 0 , \tag{26.7.41}
	$$
</synced_block>
其中 $`T ^ { \mu \nu }`$ 是对称张量
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81c89596c7815f5ad12e">
	$$
	\begin{array} { r } { T _ { \mu \nu } \equiv - \frac { 1 } { 2 } V _ { \mu \nu } ^ { \Theta } - \frac { 1 } { 2 } V _ { \nu \mu } ^ { \Theta } + \eta _ { \mu \nu } V _ { \lambda } {} ^ { \Theta \lambda } . } \end{array} \tag{26.7.42}
	$$
</synced_block>
比对 $`\gamma ^ { \rho } \gamma _ { 5 } \theta ( \bar { \theta } \gamma _ { 5 } \theta )`$ 的系数给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81698e44cf442543a618">
	$$
	\partial _ { \mu } F ^ { X } = 2 D _ { \mu } ^ { \Theta } + \Box C _ { \mu } ^ { \Theta } + \epsilon _ { \rho \nu \sigma \mu } \partial ^ { \nu } V ^ { \Theta \rho \sigma } , \tag{26.7.43}
	$$
</synced_block>
结合方程(26.7.31)和(26.7.35), 这给出了 $`D _ { \mu } ^ { \Theta }`$ 和 $`C _ { \mu } ^ { \Theta }`$ 之间的一个关系:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f814680abedfbebef8ffe">
		$$
									\begin{aligned}
\psi^X&=-\mathrm i\gamma_5\gamma^\mu\omega_\mu^\Theta,\\
F^X&=\partial^\mu C_\mu^\Theta,\\
G^X&=(V^\Theta)_\mu{}^\mu,\\
\partial_\mu A^X&=-N_\mu^\Theta,\\
\partial_\mu B^X&=M_\mu^\Theta,\\
0&=V_{\mu\nu}^\Theta-V_{\nu\mu}^\Theta
+\epsilon_{\mu\nu\rho\sigma}\partial^\sigma C^{\Theta\rho}.
\end{aligned}\tag{26.7.30--26.7.35}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81668c24d819e51abe79">
	$$
	D _ { \mu } ^ { \Theta } = - \Box C _ { \mu } ^ { \Theta } + \partial _ { \mu } \partial ^ { \nu } C _ { \nu } ^ { \Theta } . \tag{26.7.44}
	$$
</synced_block>
比对 $`[ \gamma ^ { \rho } , \gamma ^ { \sigma } ] \theta ( \bar { \theta } \gamma _ { 5 } \theta )`$ 和 $`( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 }`$ 给出的结果可以分别从方程(26.7.34)以及方程(26.7.38)和(26.7.39)得出.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f814680abedfbebef8ffe">
		$$
									\begin{aligned}
\psi^X&=-\mathrm i\gamma_5\gamma^\mu\omega_\mu^\Theta,\\
F^X&=\partial^\mu C_\mu^\Theta,\\
G^X&=(V^\Theta)_\mu{}^\mu,\\
\partial_\mu A^X&=-N_\mu^\Theta,\\
\partial_\mu B^X&=M_\mu^\Theta,\\
0&=V_{\mu\nu}^\Theta-V_{\nu\mu}^\Theta
+\epsilon_{\mu\nu\rho\sigma}\partial^\sigma C^{\Theta\rho}.
\end{aligned}\tag{26.7.30--26.7.35}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81669a5dec4e625fa2f8">
		$$
		0 = \partial _ { \mu } S _ { \mathrm{new} } ^ { \mu } = - 2 \partial ^ { \mu } \omega _ { \mu } ^ { \Theta } + 2 \not\!\partial\, \gamma ^ { \mu } \omega _ { \mu } ^ { \Theta } , \tag{26.7.38}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8114b3affb355c7d9890">
		$$
		\lambda _ { \nu } ^ { \Theta } = - \not\!\partial\, \omega _ { \nu } ^ { \Theta } + \partial _ { \nu } \gamma ^ { \mu } \omega _ { \mu } ^ { \Theta } . \tag{26.7.39}
		$$
	</synced_block_reference>
</callout>
守恒的对称张量 $`T ^ { \mu \nu }`$ 可以被视为该系统的能动量张量.
<empty-block/>
为了验证这点,我们用方程(26.1.18)和(26.2.12)将 $`\omega _ { \mu } ^ { \Theta } ( x )`$ 在无限小参量为 $`\alpha`$ 的超对称变换下的变化写成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8144bfa7d9c89936ea83">
		$$
		\mathrm{i} \delta { \mathcal O } ( x ) \equiv \left[ \bar { \alpha } Q , { \mathcal O } ( x ) \right] . \tag{26.1.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81d98e3ffeb867240dab">
		$$
		\begin{array} { r l } & { \delta C = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega \right) , } \\ & { \delta \omega = \left( - \mathrm{i} \gamma _ { 5 } \partial C - M + \mathrm{i} \gamma _ { 5 } N + \not\!\mathcal V \right) \alpha , } \\ & { \delta M = - \left( \bar { \alpha } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta N = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta V _ { \mu } = \left( \bar { \alpha } \gamma _ { \mu } \lambda \right) + \left( \bar { \alpha } \partial _ { \mu } \omega \right) . } \end{array} \tag{26.2.11-26.2.15}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r l } & { \delta \omega _ { \mu } ^ { \Theta } = - \mathrm{i} \Bigl [ ( \bar { Q } \alpha ) , \omega _ { \mu } ^ { \Theta } \Bigr ] = + \mathrm{i} \Bigl [ \omega _ { \mu } ^ { \Theta } , ( \bar { Q } \alpha ) \Bigr ] } \\ & { \qquad = \Bigl ( - \mathrm{i} \gamma _ { 5 } \not\!\partial\, C _ { \mu } ^ { \Theta } - M _ { \mu } ^ { \Theta } + \mathrm{i} \gamma _ { 5 } N _ { \mu } ^ { \Theta } + \gamma ^ { \nu } V _ { \mu \nu } ^ { \Theta } \Bigr ) \alpha . } \end{array}
$$
方程(26.7.33)—(26.7.35)使得我们可以将其变成如下形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f814680abedfbebef8ffe">
		$$
									\begin{aligned}
\psi^X&=-\mathrm i\gamma_5\gamma^\mu\omega_\mu^\Theta,\\
F^X&=\partial^\mu C_\mu^\Theta,\\
G^X&=(V^\Theta)_\mu{}^\mu,\\
\partial_\mu A^X&=-N_\mu^\Theta,\\
\partial_\mu B^X&=M_\mu^\Theta,\\
0&=V_{\mu\nu}^\Theta-V_{\nu\mu}^\Theta
+\epsilon_{\mu\nu\rho\sigma}\partial^\sigma C^{\Theta\rho}.
\end{aligned}\tag{26.7.30--26.7.35}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { r } { \mathrm{i} \Bigl \{ \omega _ { \mu } ^ { \Theta } , \bar { Q } \Bigr \} = \frac { 1 } { 2 } \gamma ^ { \nu } ( V _ { \mu \nu } ^ { \Theta } + V _ { \nu \mu } ^ { \Theta } ) - \partial _ { \mu } \bigl ( B ^ { X } + \gamma _ { 5 } A ^ { X } \bigr ) - \mathrm{i} \gamma _ { 5 } \partial \mathcal{C} _ { \mu } ^ { \Theta } + \frac { 1 } { 2 } \epsilon _ { \mu \nu \kappa \sigma } \gamma ^ { \nu } \partial ^ { \kappa } C ^ { \Theta \sigma } . } \end{array}
$$
以流(26.7.20)和(26.7.42)的形式, 这是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81708b14d39b093e501a">
		$$
		S _ { \mathrm{new} } ^ { \mu } = - 2  { \Theta _\mu } + 2 \gamma ^ { \mu } \gamma ^ { \nu } \Theta _\mu  \tag{26.7.20}|_{\omega}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81c89596c7815f5ad12e">
		$$
		\begin{array} { r } { T _ { \mu \nu } \equiv - \frac { 1 } { 2 } V _ { \mu \nu } ^ { \Theta } - \frac { 1 } { 2 } V _ { \nu \mu } ^ { \Theta } + \eta _ { \mu \nu } V _ { \lambda } {} ^ { \Theta \lambda } . } \end{array} \tag{26.7.42}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8190b6f3f194f672be51">
	$$
	\begin{array} { c } { { \mathrm{i} \{ S _ { \mathrm{new} } ^ { \mu } , \bar { Q } \} = 2 \gamma _ { \nu } T ^ { \mu \nu } + 2 ( \partial ^ { \mu } - \gamma ^ { \mu } \not\!\partial\, ) ( B ^ { X } + \gamma _ { 5 } A ^ { X } ) - \epsilon ^ { \mu \nu \kappa \sigma } \gamma _ { \nu } \partial _ { \kappa } C _ { \sigma } ^ { \Theta } } } \\ { { { } } } \\ { { + 2 \mathrm{i} \gamma _ { 5 } \Big ( \not\!\partial\, C ^ { \Theta \mu } - \gamma ^ { \mu } \gamma ^ { \lambda } \not\!\partial\, C _ { \lambda } ^ { \Theta } - \frac { 1 } { 2 } \gamma ^ { \mu } [ \not\!\partial , \gamma ^ { \sigma } ] C _ { \sigma } ^ { \Theta } \Big ) . } } \end{array} \tag{26.7.45}
	$$
</synced_block>
当 $`\mu = 0`$ 时, 右边除了第一项以外的所有项都是空间导数, 所以它们在我们对空间做积分后为零,留下
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ca8169f30e9af40989">
	$$
	\mathrm{i} \left\{ \int \mathrm { d } ^ { 3 } x S _ { \mathrm{new} } ^ { 0 } , \bar { Q } \right\} = 2 \gamma _ { \nu } \int \mathrm { d } ^ { 3 } x T ^ { 0 \nu } . \tag{26.7.46}
	$$
</synced_block>
我们已经定义了超对称流 $`S _ { \mathrm{new} } ^ { \mu }`$ 以给出 $`\begin{array} { r } { \int \mathrm { d } ^ { 3 } x S _ { \mathrm{new} } ^ { 0 } = Q } \end{array}`$ , 所以基本反对易关系(25.2.36)告诉我们
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81c9b72ed067f78b5e68">
	$$
	\int \mathrm { d } ^ { 3 } x T ^ { 0 \nu } = P ^ { \nu } , \tag{26.7.47}
	$$
</synced_block>
加上守恒条件(26.7.41), 这使得我们可以将 $`T ^ { \mu \nu }`$ 等同为能动量张量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8169a39bece8a35a14fc">
		$$
		\partial _ { \mu } T ^ { \mu \nu } = 0 , \tag{26.7.41}
		$$
	</synced_block_reference>
</callout>
需要注意的是我们以这种方式构建的能动量张量是哪一个.
无论是直接从方程(26.7.21)出发,还是通过考察流(26.7.18)的超对称变换, 对于手征超场的可重整理论, 我们可以计算出能动量张量 $`T ^ { \mu \nu }`$ 是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cead0be409310ceb93">
		$$
		\Theta _ { \mu } = \frac { \mathrm{i} } { 12 } \left[ 4 \Phi ^ { \dagger } _ { n } \partial _ { \mu } \Phi ^ { n } - 4 \Phi ^ { n } \partial _ { \mu } \Phi ^ { \dagger } _ { n } + \left( ( \bar { \mathcal{D} } \Phi ^ { \dagger } _ { n } ) \gamma _ { \mu } ( \mathcal{D} \Phi ^ { n } ) \right) \right] . \tag{26.7.21}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f815dba68d17d44237801">
		$$
		S _ { \mathrm{new} } ^ { \mu } = S ^ { \mu } + \frac { \sqrt { 2 } } { 3 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] \partial _ { \nu } \Big ( \phi ^ { n } \psi _ { R } {} _ { n } + \phi ^ { \dagger } _ { n } \psi _ { L } ^ { n } \Big ) , \tag{26.7.18}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8143a0c8ce4861c69fe1">
	$$
																		\begin{aligned}
T^{\mu\nu}={}&
\partial^\mu\phi^{\dagger}_{n}\partial^\nu\phi^n
+\partial^\nu\phi^{\dagger}_{n}\partial^\mu\phi^n\\
&-\eta^{\mu\nu}\left[
\partial^\lambda\phi^{\dagger}_{n}\partial_\lambda\phi^n
+f^{\dagger n}(\phi^{\dagger})f_n(\phi)
\right]\\
&+\frac13\left(\eta^{\mu\nu}\Box-\partial^\mu\partial^\nu\right)
\left(\phi^{\dagger}_{n}\phi^n\right)\\
&-\frac14\left[
\bar\psi_L{}_{n}\gamma^\mu\partial^\nu\psi_L^n
-(\partial^\nu\bar\psi_L{}_{n})\gamma^\mu\psi_L^n
\right.\\
&\hspace{3.8em}\left.
+\bar\psi_L{}_{n}\gamma^\nu\partial^\mu\psi_L^n
-(\partial^\mu\bar\psi_L{}_{n})\gamma^\nu\psi_L^n
\right].
\end{aligned}\tag{26.7.48}
	$$
</synced_block>
这里已经显式写出 fermion terms；其 notation 与方程(26.4.7)中的 $`\psi_L^n`$ 和 $`\bar\psi_L{}_{n}`$ 一致。
<span color="yellow_bg">标量 improvement 项 </span>$`\frac13(\eta^{\mu\nu}\Box-\partial^\mu\partial^\nu)(\phi_n^{\dagger}\phi^n)`$<span color="yellow_bg"> 通过超对称变换与方程(26.7.18)的修正项相关。对于没有超势的无质量自由场理论，</span>$`\Box\phi^n=0`$<span color="yellow_bg">，该项使能动量张量无迹。</span>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f815dba68d17d44237801">
		$$
		S _ { \mathrm{new} } ^ { \mu } = S ^ { \mu } + \frac { \sqrt { 2 } } { 3 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] \partial _ { \nu } \Big ( \phi ^ { n } \psi _ { R } {} _ { n } + \phi ^ { \dagger } _ { n } \psi _ { L } ^ { n } \Big ) , \tag{26.7.18}
		$$
	</synced_block_reference>
</callout>
一个简单的计算表明, 更一般地, 对于 $`f ( \phi )`$ 是 $`\phi ^ { n }`$ 的三阶齐次多项式的标度不变理论, $`T ^ { \mu \nu }`$ 也是无迹的.
超对称性也在标度不变性的破坏和 $`R`$ 守恒之间附加了一个有趣的关系.
方程 (26.7.30) —(26.7.32)表明 $`\gamma _ { \mu } S _ { \mathrm{new} } ^ { \mu } = 6 \gamma _ { \mu } \omega ^ { \Theta \mu }`$ , $`\partial ^ { \mu } C _ { \mu } ^ { \Theta }`$ 和 $`T _ { \lambda } ^ { \lambda } = 2 V ^ { \Theta \mu } { } _ { \mu }`$ (它衡量了标度不变性的破坏)正比于手征超场 $`X`$ 的分量, 所以, 如果其中一个作为算符方程(即, 不只是某个特殊的场构形)为零, 那么它们全部为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f814680abedfbebef8ffe">
		$$
									\begin{aligned}
\psi^X&=-\mathrm i\gamma_5\gamma^\mu\omega_\mu^\Theta,\\
F^X&=\partial^\mu C_\mu^\Theta,\\
G^X&=(V^\Theta)_\mu{}^\mu,\\
\partial_\mu A^X&=-N_\mu^\Theta,\\
\partial_\mu B^X&=M_\mu^\Theta,\\
0&=V_{\mu\nu}^\Theta-V_{\nu\mu}^\Theta
+\epsilon_{\mu\nu\rho\sigma}\partial^\sigma C^{\Theta\rho}.
\end{aligned}\tag{26.7.30--26.7.35}
		$$
	</synced_block_reference>
</callout>
<span color="yellow_bg">在这一情况下, 我们可以</span><span color="yellow_bg">**证明 **</span>$`C ^ { \Theta \rho }`$<span color="yellow_bg">** 正比于 **</span>$`R`$<span color="yellow_bg">** 量子数的流.**</span>
为了看到这点, 注意到方程(26.2.11)给出
$$
\delta C _ { \sigma } ^ { \Theta } = \mathrm{i} \left[ C _ { \sigma } ^ { \Theta } , ( \bar { \alpha } Q ) \right] = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega _ { \sigma } ^ { \Theta } \right) ,
$$
这使得一般有
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f818aa0e8d222a001b34f">
	$$
	\left[ C _ { \sigma } ^ { \Theta } , Q \right] = \gamma _ { 5 } \omega _ { \sigma } ^ { \Theta } . \tag{26.7.49}
	$$
</synced_block>
我们已经看到, 如果 $`C _ { \sigma } ^ { \Theta }`$ 守恒, 那么 $`\gamma _ { \mu } S ^ { \mu } = 0`$ , 这使得方程(26.7.20)给出 $`S _ { \sigma } = - 2 \omega _ { \sigma } ^ { \Theta }`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81708b14d39b093e501a">
		$$
		S _ { \mathrm{new} } ^ { \mu } = - 2  { \Theta _\mu } + 2 \gamma ^ { \mu } \gamma ^ { \nu } \Theta _\mu  \tag{26.7.20}|_{\omega}
		$$
	</synced_block_reference>
</callout>
这样, 在方程(26.7.49)中令 $`\sigma = 0`$ 并对 $`\mathbf{x}`$ 积分就给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f818aa0e8d222a001b34f">
		$$
		\left[ C _ { \sigma } ^ { \Theta } , Q \right] = \gamma _ { 5 } \omega _ { \sigma } ^ { \Theta } . \tag{26.7.49}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8137ab8ac3aafea9ce79">
	$$
	\left[ \int \mathrm { d } ^ { 3 } x C ^ { \Theta 0 } , Q \right] = - { \textstyle \frac { 1 } { 2 } } \gamma _ { 5 } Q . \tag{26.7.50}
	$$
</synced_block>
因此我们可以引入流
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81f8be41e79e4f791bb5">
	$$
	{ \mathcal R } ^ { \mu } \equiv 2 C ^ { \Theta \mu } , \tag{26.7.51}
	$$
</synced_block>
这个流如果守恒, 那么它是量子数 $`\begin{array} { r } { \mathcal{R} \equiv \int \mathrm { d } ^ { 3 } x \mathcal{R} ^ { 0 } } \end{array}`$ 的流, 而 $`Q _ { L }`$ 和 $`Q _ { R }`$ 在这个量子数上分别湮灭值 $`+ 1`$ 和 $`- 1`$ .
由于 $`Q _ { L }`$ 和标量超场 $`\Phi`$ 的对易子包含 $`\partial \Phi / \partial \theta _ { L }`$ 项, 这意味着 $`\theta _ { L }`$ 携带 $`\mathcal{R}`$ 值 $`+ 1`$ , 与通常的定义一致.
如果一个理论中的超场 $`X`$ 为零, 或者等价地, $`T _ { \mu } ^ { \mu }`$ , $`\gamma _ { \mu } S ^ { \mu }`$ 和 $`\partial _ { \mu } \mathcal{R} ^ { \mu }`$ 全部为零, 那么这个理论就在一组扩展的超对称变换下不变, 即25.2节末尾描述的超共形代数生成的变换.
在标度不变的理论中, 各种超场携带的 $`\mathcal{R}`$ 量子数值被拉格朗日量的结构决定.
例如, 在手征标量超场的标度不变理论中, 超势必须是超场的三阶齐次多项式.
超势的 $`\mathcal{F}`$ -项正比于 $`\theta _ { L } ^ { 2 }`$ 的系数,它有 $`\mathcal{R}`$ 量子数 $`+ 2`$ , 所以超势 $`\mathcal{F}`$ -项的 $`\mathcal{R}`$ 量子数是超势本身的 $`\mathcal{R}`$ 量子数减二.
这样, $`\mathcal{R}`$ 不变性就要求我们赋予标量超场 $`\mathcal{R}`$ 量子数 $`+ 2 / 3`$ , 这使得超场的 $`\mathcal{R}`$ 量子数是 $`+ 2`$ , 而它的 $`\mathcal{F}`$ -项的 $`\mathcal{R}`$ 量子数是零.
即, 标量分量 $`\phi ^ { n }`$ 有 $`\mathcal{R} = 2 / 3`$ 而旋量分量 $`\psi _ { L } ^ { n }`$ (正比于 $`\theta _ { L }`$ 在超场中的系数)有 $`\mathcal{R} = - 1 / 3`$ .
这可以通过从这类理论的超流(26.7.21)的 $`C`$ -项计算出流 $`{ \mathcal{R} } ^ { \mu }`$ 证实:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81cead0be409310ceb93">
		$$
		\Theta _ { \mu } = \frac { \mathrm{i} } { 12 } \left[ 4 \Phi ^ { \dagger } _ { n } \partial _ { \mu } \Phi ^ { n } - 4 \Phi ^ { n } \partial _ { \mu } \Phi ^ { \dagger } _ { n } + \left( ( \bar { \mathcal{D} } \Phi ^ { \dagger } _ { n } ) \gamma _ { \mu } ( \mathcal{D} \Phi ^ { n } ) \right) \right] . \tag{26.7.21}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f819ca725fd167e663b69">
	$$
	\begin{array} { r } { \mathcal{R} _ { \mu } = \frac 2 3 \mathrm{i} \left[ \phi ^ { \dagger } \partial _ { \mu } \phi - \phi \partial _ { \mu } \phi ^ { \dagger } \right] - \frac 1 6 \mathrm{i} \left( \bar { \psi } \gamma _ { \mu } \gamma _ { 5 } \psi \right) . } \end{array} \tag{26.7.52}
	$$
</synced_block>
(因为 $`\psi`$ 是Majorana 旋量, 第二项包含一个额外的因子 $`1 / 2`$ .)
量子修正会引入对 $`\mathcal{R}`$ 不变性的破坏(通过Adler-Bell-Jackiw反常)和标度不变性的破坏(通过耦合常数的重整化群跑动), 但即使这些对称性被这些修正破坏了, 超对称性仍然会在这些对称性之间附加一个关系.\[7a\] 我们会在29.3节看到这样的一个例子.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- M. Grisaru, in Recent Developments in Gravitation - Gargèse 1978, M. Lévy and S. Deser 编辑(Plenum Press, New York, 1979): 577
</callout>
<empty-block/>
守恒条件(26.7.26)并不唯一地决定超流 $`\Theta ^ { \mu }`$ 或相应的手征超场 $`X`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ef865dc5e544ad48c6">
		$$
		\gamma ^ { \mu } { \mathcal{D} } \Theta _ { \mu } = { \mathcal{D} } X , \tag{26.7.26}
		$$
	</synced_block_reference>
</callout>
特别地, 我们可以给 $`\Theta ^ { \mu }`$ 加上一项
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8183a6ccde50408894c5">
	$$
	\Delta \Theta ^ { \mu } = \partial ^ { \mu } Y , \tag{26.7.53}
	$$
</synced_block>
其中 $`Y`$ 是任意的的手征超场.
那么方程(26.7.26)的左边就会有如下的变化
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ef865dc5e544ad48c6">
		$$
		\gamma ^ { \mu } { \mathcal{D} } \Theta _ { \mu } = { \mathcal{D} } X , \tag{26.7.26}
		$$
	</synced_block_reference>
</callout>
$$
\gamma _ { \mu } { \mathcal{D} } \Delta \Theta ^ { \mu } = \not\!\partial\, { \mathcal{D} } Y .
$$
对于左手征超场 $`Y _ { L }`$ , 手征条件 $`\mathcal{D} _ { R } Y _ { L } = 0`$ 和反对易关系(26.2.30)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81738a97d99db41eabd6">
		$$
		\Big \{ \mathcal{D} _ { \alpha } , \overline { { { \mathcal{D} } } } _ { \beta } \Big \} = - 2 \gamma _ { \alpha \beta } ^ { \mu } \frac { \partial } { \partial x ^ { \mu } } . \tag{26.2.30}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array} { l } { \displaystyle \not\!\partial\, \mathcal{D} _ { \alpha } Y = - \frac { 1 } { 2 } \Big [ \{ \mathcal{D} _ { L } , \bar { \mathcal{D} } _ { R } \} \mathcal{D} _ { R } \Big ] _ { \alpha } Y _ { L } } \\ { \displaystyle = - \frac { 1 } { 2 } \Bigg [ \mathcal{D} _ { L \alpha } \Big ( \bar { \mathcal{D} } _ { R } \mathcal{D} _ { R } \Big ) Y _ { L } + \bar { \mathcal{D} } _ { L } {} ^ { \beta } \mathcal{D} _ { R \alpha } \mathcal{D} _ { L \beta } Y _ { L } \Bigg ] . } \end{array}
$$
上面展开右边第二项的 $`\bar { \mathcal{D} } _ { L \beta }`$ 中的矩阵 $`\epsilon \gamma _ { 5 }`$ 可以移至最后一个算符 $`\mathcal{D} _ { L \beta }`$ , 这使得守恒条件和反对易关系给出
$$
\bar { \mathcal{D} } _ { L } {} ^ { \beta } \mathcal{D} _ { R \alpha } \mathcal{D} _ { L \beta } Y _ { L } = - \mathcal{D} _ { L } {} ^ { \beta } \mathcal{D} _ { R \alpha } \bar { \mathcal{D} } _ { L \beta } Y _ { L } = 2 ( \not\!\partial\,\not\!\partial\, ) _ { \alpha } Y _ { L } ,
$$
以及随之的
$$
\begin{array} { r } { \not\!\partial\, \mathcal{D} Y _ { L } = - \frac { 1 } { 2 } \Big [ \mathcal{D} \Big ( \bar { \mathcal{D} } \mathcal{D} \Big ) Y _ { L } + 2 \not\!\partial\, \mathcal{D} Y _ { L } \Big ] = - \frac { 1 } { 4 } \mathcal{D} \Big ( \bar { \mathcal{D} } \mathcal{D} \Big ) Y _ { L } . } \end{array}
$$
对于任何右手征超场可以用相同的方法推出相同的结果, 因此它对于左手征超场和右手征超场的任意和 $`Y`$ 也是成立的
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f817f8060f35ddae4e928">
	$$
	\begin{array} { r } { \gamma _ { \mu } \mathcal{D} \Delta \Theta ^ { \mu } = \not\!\partial\, \mathcal{D} Y = - \frac { 1 } { 4 } \mathcal{D} \Big ( \bar { \mathcal{D} } \mathcal{D} \Big ) Y . } \end{array} \tag{26.7.54}
	$$
</synced_block>
这与守恒条件(26.7.26)是同一形式, 而相应的手征超场 $`X`$ 多出了如下的手征超场
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81ef865dc5e544ad48c6">
		$$
		\gamma ^ { \mu } { \mathcal{D} } \Theta _ { \mu } = { \mathcal{D} } X , \tag{26.7.26}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f815b9806e7686e992ad7">
	$$
	\begin{array} { r } { \Delta X = - \frac { 1 } { 4 } \big ( \bar { \mathcal{D} } \mathcal{D} \big ) Y . } \end{array} \tag{26.7.55}
	$$
</synced_block>
很容易验证给 $`\Theta ^ { \mu }`$ 加上 $`\Delta \Theta ^ { \mu }`$ 对 $`T ^ { \mu 0 }`$ 和 $`S _ { \mathrm{new} } ^ { 0 }`$ 的改变仅是空间导数, 因此并不会改变能动量 4 -矢 $`P ^ { \mu }`$ 和超荷 $`Q`$ .
我们在26.6节看到, 任何手征超场 $`X`$ 都可以表示成 $`\boldsymbol { X } = ( \hat { \mathcal{D} } \boldsymbol { \mathcal{D} } ) \boldsymbol { S }`$ 的形式, 因此, 通过给 $`\Theta ^ { \mu }`$ 加上形如(26.7.55)且其中 $`Y = 4 S`$ 的一项, $`X`$ 可以被消掉.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f815b9806e7686e992ad7">
		$$
		\begin{array} { r } { \Delta X = - \frac { 1 } { 4 } \big ( \bar { \mathcal{D} } \mathcal{D} \big ) Y . } \end{array} \tag{26.7.55}
		$$
	</synced_block_reference>
</callout>
但一般而言, $`S`$ 和以这种方式构建的新 $`\Theta ^ { \mu }`$ 将不是定域的.
从我们在第22章对三角反常的经验而言, 这一情况并不陌生——我们在里那里看到, 尽管总能构造出加在拉格朗日密度上的项使得反常被抵消, <span color="yellow_bg">但这些项一般不是定域的, 因此必须从拉格朗日密度中排除出去</span>.
存在可以表示成 $`( { \bar { \mathcal{D} } } { \mathcal{D} } ) S`$ 且 $`S`$ 定域的手征超场, 因此, 如果它出现连带的手征超场 $`X`$ 中, 它可以通过给 $`\Theta ^ { \mu }`$ 加上形如(26.7.53)的定域项被抵消掉.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f8183a6ccde50408894c5">
		$$
		\Delta \Theta ^ { \mu } = \partial ^ { \mu } Y , \tag{26.7.53}
		$$
	</synced_block_reference>
</callout>
例如, 因为方程(26.6.15)和(26.6.16)表明 $`( \bar { \mathcal{D} } \mathcal{D} ) \operatorname{Re} ( k ^ { * } \Phi ) = 4 \operatorname{Re} ( k \partial f ( \Phi ) / \partial \Phi )`$ , 这样的项包括像 $`\operatorname{Re} ( k \partial f ( \Phi ) / \partial \Phi )`$ 这样的项, 其中 $`k`$ 是任意的复常数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f81be882bf1e8f4ef7578">
		$$
		\mathcal D_R^2K_n=-4f_n(\Phi). \tag{26.6.15}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816da424ea67619cfa5f#34cee2b74b3f813a87b4ee08015df3e2">
		$$
		\mathcal D_L^2K^{\dagger n}=4f^{\dagger n}(\Phi^\dagger). \tag{26.6.16}
		$$
	</synced_block_reference>
</callout>
但是一般而言, 这种方法对 $`X`$ 造成的变化是相当有限的.
<empty-block/>
</content>
</page>
