Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958 as of 2026-06-30T03:19:37.433Z:
<page url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.8 一般 Kähler 势"}
</properties>
<content>
在几种情况下我们必须要考察有一般形式(26.3.30)的不可重整拉格朗日密度
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f8185b369e09fb8d66190">
		$$
		I = \int \mathrm { d } ^ { 4 } x \left[ f \right] _ { \mathcal{F} } + \int \mathrm { d } ^ { 4 } x \left[ f \right] _ { \mathcal{F} } ^ { \ast } + \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \left[ K \right] _ { D } , \tag{26.3.30}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f817d947ee01bc9c5ddbb">
	$$
	\begin{array} { r } { \mathcal{L} = 2 \operatorname{Re} \Big [ f ( \Phi ) \Big ] _ { \mathcal{F} } + \frac { 1 } { 2 } \Big [ K \big ( \Phi , \Phi ^ { * } \big ) \Big ] _ { D } , } \end{array} \tag{26.8.1}
	$$
</synced_block>
其中超势 $`f`$ 是左手征超场 $`\Phi^n`$ 的函数但不是它们导数的函数, 而 Kähler势 $`K`$ 是 $`\Phi^n`$ 和 $`\Phi^{*\,n}`$ 的函数但不是它们导数的函数.
在对称性排除掉任何可重整相互作用或者可重整相互作用碰巧都很小的有效场论中, 这样的情况会出现.
对于导数个数, 费米场个数和任何小耦合常数个数的某个组合, 利用值最小的拉格朗日量通常可以从树图算出低能的散射振幅.
在19.5节, 我们检验过这种没有可重整耦合的有效场论, 它包含核子和软 $`\pi`$ 子. 21.4节讨论的动力学破缺的规范场论提供了可重整耦合都很小的那类理论的例子.
在对称性不允许有超势或者超势由于某个原因非常小的超对称理论中, 这一情况也会出现.
当我们在29.5节考察阿贝尔规范超场和规范中性手征标量超场的 $`N = 2`$ 扩充超对称理论时, 我们会遇到这样的例子.
我们将会那里证明, 通过使用形如(26.8.1)的拉格朗日密度, 其中 $`f=0`$ 且 $`K`$ 仅是 $`\Phi^n`$ 和 $`\Phi^{*\,n}`$ 的函数而不是它们导数的函数, 树图生成了这类理论中的低能散射振幅.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f817d947ee01bc9c5ddbb">
		$$
		\begin{array} { r } { \mathcal{L} = 2 \operatorname{Re} \Big [ f ( \Phi ) \Big ] _ { \mathcal{F} } + \frac { 1 } { 2 } \Big [ K \big ( \Phi , \Phi ^ { * } \big ) \Big ] _ { D } , } \end{array} \tag{26.8.1}
		$$
	</synced_block_reference>
</callout>
在有效场论中, 如果一些标量场与潜在理论的基本能标处在同一量级, 即使所有其它场的值和所有能量得要小的多, 这是引入对 $`\Phi^n`$ 和 $`\Phi^{*\,n}`$ 依赖方式任意但不依赖它们导数的Kähler势是特别重要的.
例如, 非常有趣的, 它会与引力传递超对称破缺的理论相关联, 这将在31.6节进行讨论.
我们来考察如何将拉格朗日密度(26.8.1)表示成分量场.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f817d947ee01bc9c5ddbb">
		$$
		\begin{array} { r } { \mathcal{L} = 2 \operatorname{Re} \Big [ f ( \Phi ) \Big ] _ { \mathcal{F} } + \frac { 1 } { 2 } \Big [ K \big ( \Phi , \Phi ^ { * } \big ) \Big ] _ { D } , } \end{array} \tag{26.8.1}
		$$
	</synced_block_reference>
</callout>
在推导方程(26.4.4)时, 我们没有使用 $`f ( \Phi )`$ 是三次多项式的假定, 所以它依旧给出任意超势给拉格朗日量贡献的 $`\mathcal{F}`$ -项.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f81ed9178dcf6147e791a">
		$$
		\Big [ f ( \Phi ) \Big ] _ { \mathcal{F} } = - \frac { 1 } { 2 } \frac { \partial ^ { 2 } f ( \phi ) } { \partial \phi _ { n } \partial \phi _ { m } } \Big ( \bar { \psi } ^ { n } _ { L } \psi ^ { m } _ { L } \Big ) + \mathcal{F} ^ { n } \frac { \partial f ( \phi ) } { \partial \phi _ { n } } . \tag{26.4.4}
		$$
	</synced_block_reference>
</callout>
为了推导 $`D`$ -项, 我们注意到Kähler势中 $`\theta`$ 的四阶项是
$$
\begin{aligned}
K(\Phi,\Phi^*)_{\theta^4}
={}&-\frac18(\bar\theta\gamma_5\theta)^2
\left[
\frac{\partial K(\phi,\phi^*)}{\partial\phi_n}\Box\phi^n
+
\frac{\partial K(\phi,\phi^*)}{\partial\phi^*_n}\Box\phi^{*\,n}
\right]
\\
&+
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi^*_m}
(\bar\theta\gamma_5\theta)
\left[
(\bar\theta\psi^m_R)(\bar\theta\not\!\partial\,\psi^n_L)
-(\bar\theta\psi^n_L)(\bar\theta\not\!\partial\,\psi^m_R)
\right]
\\
&+2\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\theta_L^{\mathrm T}\epsilon\psi^n_L)
(\theta_L^{\mathrm T}\epsilon\psi^m_L)
(\theta_L^{\mathrm T}\epsilon\theta_L)^*\mathcal F^{*\,l}
\right]
\\
&+2\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\bar\theta\psi^m_L)(\bar\theta\psi^l_R)
(\bar\theta\gamma_5\gamma_\mu\theta)\partial^\mu\phi^n
\right]
\\
&+
\frac{\partial^4K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_k\partial\phi^*_l}
(\bar\theta\psi^n_L)(\bar\theta\psi^m_L)(\bar\theta\psi^l_R)(\bar\theta\psi^k_R)
\\
&-\frac14
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi^*_m}
\mathcal F^n\mathcal F^{*\,m}
(\bar\theta(1+\gamma_5)\theta)(\bar\theta(1-\gamma_5)\theta)
\\
&+\frac14(\bar\theta\gamma_5\gamma^\mu\theta)(\bar\theta\gamma_5\gamma^\nu\theta)
\left[
-\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi^*_m}
\partial_\mu\phi^n\partial_\nu\phi^{*\,m}
\right.
\\
&\hspace{5.3cm}\left.
+\frac12\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m}
\partial_\mu\phi^n\partial_\nu\phi^m
+\frac12\frac{\partial^2K(\phi,\phi^*)}{\partial\phi^*_n\partial\phi^*_m}
\partial_\mu\phi^{*\,n}\partial_\nu\phi^{*\,m}
\right].
\end{aligned}\tag{26.8.2}
$$
我们可以再次使用方程(26.A.18), (26.A.19)和方程(26.A.9)将这一展开中对 $`\theta`$ 的依赖写成一个总
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f81678701ee7b96af9b3b">
		$$
		\Bigl ( \bar { s } s \Bigr ) ^ { 2 } = - \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } , \qquad \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \Bigr ) \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \nu } s \Bigr ) = - \eta _ { \mu \nu } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } . \tag{26.A.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f81459208c3b78885c16b">
		$$
		\begin{array} { r } { ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } s \bar { s } = - \frac { 1 } { 4 } \gamma _ { 5 } ( \bar { s } \gamma _ { 5 } s ) ^ { 2 } . } \end{array} \tag{26.A.19}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f81ed90b4fd1a2f33b2df">
		$$
		\begin{array} { r } { s \bar { s } = - \frac { 1 } { 4 } ( \bar { s } s ) + \frac { 1 } { 4 } \gamma _ { 5 } \gamma _ { \mu } ( \bar { s } \gamma _ { 5 } \gamma ^ { \mu } s ) - \frac { 1 } { 4 } \gamma _ { 5 } \left( \bar { s } \gamma _ { 5 } s \right) . } \end{array} \tag{26.A.9}
		$$
	</synced_block_reference>
</callout>
因子 $`( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 }`$ , 并发现
$$
\begin{aligned}
K(\Phi,\Phi^*)_{\theta^4}
={}&\frac14(\bar\theta\gamma_5\theta)^2\Bigg\{
-\frac12\frac{\partial K(\phi,\phi^*)}{\partial\phi_n}\Box\phi^n
-\frac12\frac{\partial K(\phi,\phi^*)}{\partial\phi^*_n}\Box\phi^{*\,n}
\\
&+
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi^*_m}
\left[
(\bar\psi^m\not\!\partial\,\psi^n_L)
+(\bar\psi^n\not\!\partial\,\psi^m_R)
-2\mathcal F^n\mathcal F^{*\,m}
\right]
\\
&+2\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\bar\psi^n\psi^m_L)\mathcal F^{*\,l}
\right]
\\
&-2\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\bar\psi^m\gamma^\mu\psi^l_R)\partial_\mu\phi^n
\right]
\\
&-\frac12
\frac{\partial^4K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_k\partial\phi^*_l}
(\bar\psi^n\psi^m_L)(\bar\psi^k\psi^l_R)
\\
&+
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi^*_m}
\partial_\mu\phi^n\partial^\mu\phi^{*\,m}
-\frac12
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m}
\partial_\mu\phi^n\partial^\mu\phi^m
\\
&-\frac12
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi^*_n\partial\phi^*_m}
\partial_\mu\phi^{*\,n}\partial^\mu\phi^{*\,m}
\Bigg\}.
\end{aligned}\tag{26.8.3}
$$
为了使费米子动能项的实性质是显然的, 我们可以使用方程(26.A.21)写下
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f8158a2fdc1adcd361128">
		$$
		( \overline { { { s _ { 1 } } } } M s _ { 2 } ) ^ { * } = \left\{ \begin{array} { l l } { { + ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = 1 , \ \gamma _ { \mu } , \ [ \gamma _ { \mu } , \gamma _ { \nu } ] } } \\ { { - ( \overline { { { s _ { 1 } } } } M s _ { 2 } ) } } & { { \qquad M = \gamma _ { \mu } \gamma _ { 5 } , \ \gamma _ { 5 } } } \end{array} \right. . \tag{26.A.21}
		$$
	</synced_block_reference>
</callout>
$$
\left(\bar\psi^n\not\!\partial\,\psi^m_R\right)
=
\left(\bar\psi^n\not\!\partial\,\psi^m_L\right)^* .
$$
$`K ( \Phi , \Phi ^ { * } )`$ 的 $`D`$ -项是 $`- ( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 } / 4`$ 的系数减去达朗贝尔算符作用在 $`K ( \Phi , \Phi ^ { * } )`$ 中 $`\theta`$ 无关项上的结果的一半, 这一项就是 $`K ( \phi , \phi ^ { * } )`$ , 所以
$$
\begin{aligned}
\frac12\left[K(\Phi,\Phi^*)\right]_D
={}&\operatorname{Re}\,\mathcal G_{nm}\left[
-\frac12\left(\bar\psi^m\not\!\partial\,(1+\gamma_5)\psi^n\right)
+\mathcal F^n\mathcal F^{*\,m}
-\partial_\mu\phi^n\partial^\mu\phi^{*\,m}
\right]
\\
&-\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\bar\psi^n\psi^m_L)\mathcal F^{*\,l}
\right]
\\
&+\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\bar\psi^m\gamma^\mu\psi^l_R)\partial_\mu\phi^n
\right]
\\
&+\frac14
\frac{\partial^4K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l\partial\phi^*_k}
(\bar\psi^n\psi^m_L)(\bar\psi^k\psi^l_R).
\end{aligned}\tag{26.8.4}
$$
其中 $`\mathcal{G} ( \phi , \phi ^ { * } )`$ 是 Kähler 度规
<synced_block url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f81a38ee1ce8bf6e7c5e2">
	$$
	\mathcal G_{nm}(\phi,\phi^*)\equiv
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi^*_m}.
\tag{26.8.5}
	$$
</synced_block>
注意到方程(26.4.2)中的常矩阵 $`g _ { n m }`$ 在这里被换成了 Kähler 度规 $`\mathcal{G} _ { n m } ( \phi , \phi ^ { * } )`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f81ad8582ddc12fb36aa4">
		$$
		\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \Big [ K ( \Phi , \Phi ^ { * } ) \Big ] _ { D } = g _ { n m } \left[ - \partial _ { \mu } \phi ^ { * \, n } \partial ^ { \mu } \phi ^ { m } + \mathcal{F} ^ { * \, n } \mathcal{F} ^ { m } \right. } \\ { \displaystyle \left. - \frac { 1 } { 2 } \Big ( \overline { { \psi ^ { n } _ { L } } } \gamma ^ { \mu } \partial _ { \mu } \psi ^ { m } _ { L } \Big ) + \frac { 1 } { 2 } \Big ( ( \partial _ { \mu } \overline { { \psi ^ { n } _ { L } } } ) \gamma ^ { \mu } \psi ^ { m } _ { L } \Big ) \right] . } \end{array} \tag{26.4.2}
		$$
	</synced_block_reference>
</callout>
因为 Kähler 度规与场相关, 所以我们一般无法通过重新定义场使得它等于一个单位矩阵, 所以总的拉格朗日量必须
是如下的形式
$$
\begin{aligned}
\mathcal L
={}&\operatorname{Re}\,\mathcal G_{nm}\left[
-\frac12\left(\bar\psi^m\not\!\partial\,(1+\gamma_5)\psi^n\right)
+\mathcal F^n\mathcal F^{*\,m}
-\partial_\mu\phi^n\partial^\mu\phi^{*\,m}
\right]
\\
&-\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\bar\psi^n\psi^m_L)\mathcal F^{*\,l}
\right]
\\
&+\operatorname{Re}\!\left[
\frac{\partial^3K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l}
(\bar\psi^m\gamma^\mu\psi^l_R)\partial_\mu\phi^n
\right]
\\
&+\frac14
\frac{\partial^4K(\phi,\phi^*)}{\partial\phi_n\partial\phi_m\partial\phi^*_l\partial\phi^*_k}
(\bar\psi^n\psi^m_L)(\bar\psi^k\psi^l_R)
\\
&-\operatorname{Re}\!\left[
\frac{\partial^2f(\phi)}{\partial\phi_n\partial\phi_m}
(\bar\psi^n\psi^m_L)
\right]
+2\operatorname{Re}\!\left[\mathcal F^n\frac{\partial f(\phi)}{\partial\phi_n}\right].
\end{aligned}\tag{26.8.6}
$$
双线性型 $`(\bar\psi^m\not\!\partial\,\gamma_5\psi^n)`$ 是全导数, 因此如果 $`\mathcal G_{nm}`$ 是常数, 它可以被扔掉, 但对于一般的 Kähler 势则必须保留.
在27.4节的末尾, 这一结果会被推广以纳入规范超场.
就像在19.6节讨论的那样,整体对称群 $`G`$ 到子群 $`H`$ 的自发破缺蕴含了一组无质量Goldstone实玻色子, 其玻色场为 $`\pi^k`$ , 对于这组玻色子, 拉格朗日量中导数最小的项取如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f811fb7eeef31abe2c1d6">
	$$
	\mathcal{L} _ { G / H } = - G _ { k \ell } ( \pi ) \, \partial _ { \mu } \pi ^ { k } \, \partial ^ { \mu } \pi ^ { \ell } , \tag{26.8.7}
	$$
</synced_block>
其中 $`G _ { k \ell } ( \pi )`$ 是陪集空间 $`G / H`$ 的度规.
(拉格朗日密度属于这种一般形式的理论被称为非线性 $`\sigma`$ -模型.) 通过将复标量场 $`\phi^n`$ 写成它们的实部和虚部, 拉格朗日密度(26.8.6)中的 $`-\mathcal G_{nm}(\phi,\phi^*)\partial_\mu\phi^n\partial^\mu\phi^{*\,m}`$ 可以被写成(26.8.7)的形式, 但反过来一般不成立: 像 Goldstone玻色场 $`\pi^k`$ 这样的一组实坐标可以被解释成场 $`\phi^n`$ 这样的一组复坐标的实部和虚部, 并且这些坐标的度规定域地由方程(26.8.5)给定, 这个条件定义了所谓的Kähler 流形.\*\* 在通常的 $`G/H`$ 不是Kähler流形的情况下,不应该认为 $`G`$ 在自发破缺到 $`H`$ 的同时无法保持超对称性不破缺.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f811fb7eeef31abe2c1d6">
		$$
		\mathcal{L} _ { G / H } = - G _ { k \ell } ( \pi ) \, \partial _ { \mu } \pi ^ { k } \, \partial ^ { \mu } \pi ^ { \ell } , \tag{26.8.7}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f816280f7c5e18852c958#34cee2b74b3f81a38ee1ce8bf6e7c5e2">
		$$
		\mathcal G_{nm}(\phi,\phi^*)\equiv
\frac{\partial^2K(\phi,\phi^*)}{\partial\phi_n\partial\phi^*_m}.
\tag{26.8.5}
		$$
	</synced_block_reference>
</callout>
在这些情况中发生的是出现了额外的无质量玻色子, 它们和Goldstone玻色子合在一起确实形成了Kähler流形.
这是因为超势 $`f(\phi)`$ 依赖于 $`\phi`$ 但不依赖 $`\phi^*`$ , 所以, 如果整个拉格朗日量在整体对称群 $`G`$ 下不变, 那么超势自动在 $`G_{\mathbb C}`$ 下不变: 如果 $`G`$ 由变换 $`\exp(\mathrm{i}\theta^A t_A)`$ 构成, 其中 $`t_A`$ 是生成元而 $`\theta^A`$ 是任意实参量, 那么 $`G_{\mathbb C}`$ 由生成元相同但参量为任意复数 $`z^A`$ 的变换 $`\exp(\mathrm{i}z^A t_A)`$ 构成.
(例如, 如果 $`G`$ 是 $`U ( n )`$ , 那么 $`G _ { \mathbb { C } }`$ 就是 $`G L ( n , \mathbb { C } )`$ , 即所有非奇异复矩阵的群, 如果 $`G`$ 是 $`S U ( n )`$ , 那么 $`G _ { \mathbb { C } }`$ 是 $`S L ( n , \mathbb { C } )`$ , 即所有行列式为 1 的复矩阵的群.) 同理, 如果 $`f ( \phi )`$ 的某个驻点 $`\phi ^ { ( 0 ) }`$ 在 $`G`$ 的某个子群 $`H`$ 下保持不变, 那么它在 $`G _ { \mathbb { C } }`$ 的子群 $`H _ { \mathbb { C } } { - } H`$ 的复化群——下保持不变.
无论 $`G / H`$ 是不是
Kähler 流形, 复化陪集空间 $`G _ { \mathbb { C } } / H _ { \mathbb { C } }`$ 总是Kähler流形.
能得出这点的原因是, $`G_{\mathbb C}/H_{\mathbb C}`$ 是 $`\phi^n`$ 的平坦复空间的复子流形, 前者是Kähler流形, 而有一个定理保证了Kähler流形的复子流形也是Kähler流形.\[9\] 如果 $`G_{\mathbb C}/H_{\mathbb C}`$ 被 $`\phi^n(z)=[\exp(\mathrm{i}z^A t_A)\phi^{(0)}]^n`$ 的值参数化, 那么通过将它嵌入到 $`\phi^n`$ 的平坦复空间中就能获得度规, 通常通过线元 $`\mathrm d\phi^n\,\mathrm d\phi^*_{n}`$ 获得.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- P. Griffiths and J. Harris, Principles of Algebraic Geometry (Wiley, New York, 1978): 109.在此感谢 D. Freed告诉我这个一般定理的应用
</callout>
$`G _ { \mathbb { C } }`$ 确实不是整个拉格朗日量的对称性, 但是 $`G _ { \mathbb { C } }`$ 破缺到 $`H _ { \mathbb { C } }`$ 带出的Goldstone玻色子却是严格无质量的.
这是被 27.6 节的不可重整定理, 或者更简单地, 25.4 节的结果所保证的, 即无质量零自旋粒子必须与通过超对称变换相联系的粒子成对出现, 因此对于任何与超对称对易的整体对称群 $`G`$ , 它们在这个群下有相同的变换.
</content>
</page>
