Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc as of 2026-07-17T17:53:26.963Z:
<page url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.8 另一种方法: 规范不变的超对称变换"}
</properties>
<content>
迄今为止讨论的超对称变换规则包含普通的时空导数但不包含规范不变导数让人有些不安.
例如, 在一个 $`U ( 1 )`$ 规范理论中, 手征标量超场分量场的变换规则由方程(26.3.15)—(26.3.17)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f811d9036cae1f992209f">
	$$
					\begin{aligned}
\delta\psi_L&=\sqrt2\,\partial_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\delta\mathcal F&=\sqrt2(\bar\alpha_L\not\partial\psi_L),\\
\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.1}
	$$
</synced_block>
有的人或许会觉得, 在携带 $`U ( 1 )`$ 荷 $`q`$ 的手征超场的变换中, 方程(27.8.1)中的普通时空导数应该被换成规范协变导数, 以 $`U ( 1 )`$ 规范场 $`V _ { \mu }`$ 表示就是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f811d9036cae1f992209f">
		$$
						\begin{aligned}
\delta\psi_L&=\sqrt2\,\partial_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\delta\mathcal F&=\sqrt2(\bar\alpha_L\not\partial\psi_L),\\
\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.1}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81449fa6d32c5163d370">
	$$
	D _ { \mu } = \partial _ { \mu } - \mathrm{i} q V _ { \mu } . \tag{27.8.2}
	$$
</synced_block>
当手征超场的变换是这种规范不变的超对称变换时, 对于只包含物理和辅助场 $`V _ { \mu }`$ , $`\lambda`$ 和 $`D`$ 的规范超多重态, 我们仍旧尝试将它的超对称变换规则写成:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81bbb63ee5e1368efbcb">
	$$
					\begin{aligned}
\tilde\delta\mathcal V_\mu&=(\bar\alpha\gamma_\mu\lambda),\\
\tilde\delta\lambda&=\mathrm iD\gamma_5\alpha+\frac12[\partial_\mu\not\!\mathcal V,\gamma^\mu]\alpha,\\
\tilde\delta D&=\mathrm i(\bar\alpha\gamma_5\not\partial\lambda).
\end{aligned}\tag{27.8.3}
	$$
</synced_block>
其中出现的是普通导数是因为规范超场不携带 $`U ( 1 )`$ 荷.
这并不行得通.
<span color="yellow_bg">这些变换的代数不封闭: 两个修正超对称变换的对易子不是玻色对称变换, 例如时空平移和规范变换, 的线性组合.</span>
由此得出, 为手征超场和规范超场构造在这些修正超对称变换下不变的拉格朗日量是不可能的, 这是因为, 如果存在这样的拉格朗日量, 那么它也必须在这些变换的对易子在不变, 这使得这些对易子必须是拉格朗日量的玻色对称性.
在1973 年, de Wit 和 Freedman\[11\]证明了通过修正手征超场的超对称变换性质可以使得超对称代数封闭, 方法是不仅把普通导数换成规范协变导数, 同时在 $`\mathcal{F}`$ -分量的变换中加入额外一项,使得对于 $`U ( 1 )`$ 规范理论, 修正超对称变换规则是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- B. de Wit and D. Z. Freedman, Phys. Rev. D12, 2286 (1975). 这篇文章重印于 Supersymmetry, 参考文献\[1\]
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81bd942dfd97600b501a">
	$$
					\begin{aligned}
\tilde\delta\psi_L&=\sqrt2\,D_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\tilde\delta\mathcal F&=\sqrt2(\bar\alpha_L\not D\psi_L)-2\mathrm iq\phi(\bar\alpha_L\lambda_R),\\
\tilde\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.4}
	$$
</synced_block>
在做了这个改变后, 他们还能够构造出在变换(27.8.3)—(27.8.4)下不变的拉格朗日量, 而这个拉格朗日量正是我们在27.1节和27.2节发现的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81bbb63ee5e1368efbcb">
		$$
						\begin{aligned}
\tilde\delta\mathcal V_\mu&=(\bar\alpha\gamma_\mu\lambda),\\
\tilde\delta\lambda&=\mathrm iD\gamma_5\alpha+\frac12[\partial_\mu\not\!\mathcal V,\gamma^\mu]\alpha,\\
\tilde\delta D&=\mathrm i(\bar\alpha\gamma_5\not\partial\lambda).
\end{aligned}\tag{27.8.3}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81bd942dfd97600b501a">
		$$
						\begin{aligned}
\tilde\delta\psi_L&=\sqrt2\,D_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\tilde\delta\mathcal F&=\sqrt2(\bar\alpha_L\not D\psi_L)-2\mathrm iq\phi(\bar\alpha_L\lambda_R),\\
\tilde\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.4}
		$$
	</synced_block_reference>
</callout>
继续使用传统的变换规则(27.8.1)并没有什么错, 所以我们并不需要用de Wit–Freedman形式体系处理超对称规范理论.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f811d9036cae1f992209f">
		$$
						\begin{aligned}
\delta\psi_L&=\sqrt2\,\partial_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\delta\mathcal F&=\sqrt2(\bar\alpha_L\not\partial\psi_L),\\
\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.1}
		$$
	</synced_block_reference>
</callout>
然而, 这个体系本身是有益的, 因为传统体系在超引力理论中的相应版本非常繁琐.
就像在第 31章描述的, 在推导超引力理论中物理上感兴趣的结果时主要使用的形式体系跟随的是de Wit和Freedman那样的方法, 即超对称变换规则包含的是协变导数而不是普通导数, 而不是基于类似(27.8.1)这样的传统超对称变换.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f811d9036cae1f992209f">
		$$
						\begin{aligned}
\delta\psi_L&=\sqrt2\,\partial_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\delta\mathcal F&=\sqrt2(\bar\alpha_L\not\partial\psi_L),\\
\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.1}
		$$
	</synced_block_reference>
</callout>
因此在相对简单的 $`U ( 1 )`$ 规范理论的框架下理解de Wit–Freedman形式体系和传统方法之间的关系是有益的, 特别是解释 $`\mathcal{F}`$ 的变换规则中额外那一项的起源.
在写下不包含规范超场 $`V`$ 的分量 $`C , M ,`$ $`N`$ 或 $`\omega`$ 的超对称变换(27.8.3)时, <span color="yellow_bg">de Wit 和 Freedman隐含地采用了 27.1 节讨论的Wess–Zumino规范.</span>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81bbb63ee5e1368efbcb">
		$$
						\begin{aligned}
\tilde\delta\mathcal V_\mu&=(\bar\alpha\gamma_\mu\lambda),\\
\tilde\delta\lambda&=\mathrm iD\gamma_5\alpha+\frac12[\partial_\mu\not\!\mathcal V,\gamma^\mu]\alpha,\\
\tilde\delta D&=\mathrm i(\bar\alpha\gamma_5\not\partial\lambda).
\end{aligned}\tag{27.8.3}
		$$
	</synced_block_reference>
</callout>
但是Wess–Zumino规范的选择既不在传统超对称变换(26.2.11)—(26.2.17)下不变, 也不在扩充规范变换(27.1.17)下不变, 所以一旦我们采用了这个规范, 两个对称性都失去了.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81d98e3ffeb867240dab">
		$$
		\begin{array} { r l } & { \delta C = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega \right) , } \\ & { \delta \omega = \left( - \mathrm{i} \gamma _ { 5 } \partial C - M + \mathrm{i} \gamma _ { 5 } N + \not\!\mathcal V \right) \alpha , } \\ & { \delta M = - \left( \bar { \alpha } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta N = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta V _ { \mu } = \left( \bar { \alpha } \gamma _ { \mu } \lambda \right) + \left( \bar { \alpha } \partial _ { \mu } \omega \right) . } \end{array} \tag{26.2.11-26.2.15}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f815ab667da80eecb2eaa">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { \delta \lambda = \left( \frac12\Big[\partial_\mu\not\!\mathcal V,\gamma^\mu\Big] + \mathrm{i} \gamma _ { 5 } D \right) \alpha =(-iS^{\mu\nu}V_{\mu\nu}+i\gamma_5 D)\alpha } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \delta D = \mathrm{i} \Big ( \bar { \alpha } \gamma _ { 5 } \not\!\partial\, \lambda \Big ) . } } \end{array} \tag{26.2.16-26.2.17}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f815fb109d2acba06f849">
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
	</synced_block_reference>
</callout>
然而, 我们可以定义一个组合变换, 它作用在Wess-Zumino规范中的场上, 由一个传统的超对称变换加上一个规范变换, 使得我们再次回到Wess-Zumino规范.
<span color="yellow_bg">这就是 de Wit–Freedman 变换 </span>$`\tilde\delta`$<span color="yellow_bg">.\*</span>
以这种方法构造 de Wit–Freedman变换时, 注意到对于一个满足Wess-Zumino规范条件 $`C=M=N=\omega=0`$ 的规范超场, 变换规则(26.2.11)—(26.2.14)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81d98e3ffeb867240dab">
		$$
		\begin{array} { r l } & { \delta C = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega \right) , } \\ & { \delta \omega = \left( - \mathrm{i} \gamma _ { 5 } \partial C - M + \mathrm{i} \gamma _ { 5 } N + \not\!\mathcal V \right) \alpha , } \\ & { \delta M = - \left( \bar { \alpha } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta N = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } [ \lambda + \not\!\partial\, \omega ] \right) , } \\ & { \delta V _ { \mu } = \left( \bar { \alpha } \gamma _ { \mu } \lambda \right) + \left( \bar { \alpha } \partial _ { \mu } \omega \right) . } \end{array} \tag{26.2.11-26.2.15}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f8129b107e4904b2f8be3">
	$$
			\delta C=0,\qquad \delta\omega=\not\!\mathcal V\,\alpha,\qquad
\delta M=-(\bar\alpha\lambda),\qquad
\delta N=\mathrm i(\bar\alpha\gamma_5\lambda).\tag{27.8.5}
	$$
</synced_block>
根据方程(27.1.17), 通过进行一个无限小扩充规范变换(27.1.13):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f815fb109d2acba06f849">
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
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81e2aaf6fb19a10c5a0b">
		$$
		V^A(x,\theta)\to V^A(x,\theta)+\frac{\mathrm{i}}{2}\bigl[\Omega^A(x,\theta)-\Omega^A(x,\theta)^*\bigr]+\frac{i}{2}[\Omega^\dagger+\Omega,V]+\cdots.\tag{27.1.13}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f8172a5abcb47c7a259f8">
	$$
	V \to V + \frac { \mathrm{i} } { 2 } \biggl [ \Omega - \Omega ^ { * } \biggr ] \ , \tag{27.8.6}
	$$
</synced_block>
其中 $`\Omega`$ 是分量为
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81c898fdfe189b6ea75d">
	$$
			\phi^\Omega=0,\qquad
\psi_L^\Omega=-\sqrt2\,\not\!\mathcal V\,\alpha_R,\qquad
\mathcal F^\Omega=-\bigl(\bar\alpha(1-\gamma_5)\lambda\bigr).\tag{27.8.7}
	$$
</synced_block>
的左手征超场, 我们能够回到Wess–Zumino规范.
<empty-block/>
根据方程(27.1.11), 这个扩充规范变换在荷为 $`q`$ 的手征超场上诱导出了变换
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81068ac6c75fc398e24f">
		$$
		\Phi^n_L(x,\theta)\to \bigl[\exp\bigl(\mathrm{i}t_A\Omega^A(x,\theta)\bigr)\bigr]^n{}_m\Phi^m_L(x,\theta).\tag{27.1.11}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81cba0c7faf3e6a9d4a1">
	$$
	\delta ^ { \prime } \Phi = \mathrm{i} q \Omega \Phi . \tag{27.8.8}
	$$
</synced_block>
利用乘法规则(26.3.27)—(26.3.29), $`\Phi`$ 的分量的变换是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81a28fc6ca49d397ab7e">
		$$
		\begin{array} { r l } & { \phi = \phi^1 \phi^2 \ : , } \\ & { \psi _ { L } = \phi^1 \psi_L^2 + \phi^2 \psi_L^1 \ : , } \\ & { \mathcal{F} = \phi^1 \mathcal F^2 + \phi^2 \mathcal F^1 - \left( (\psi_L^1)^{\mathrm T} \epsilon \psi_L^2 \right) \ : . } \end{array} \tag{26.3.27-26.3.29}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f818f966bd72caf809e01">
	$$
			\begin{aligned}
\delta'\psi_L&=-\mathrm i\sqrt2\,q\phi\,\not\!\mathcal V\,\alpha_R,\\
\delta'\mathcal F&=-2\mathrm iq\phi(\bar\alpha_L\lambda_R)
-\mathrm i\sqrt2\,q(\bar\alpha_L\not\!\mathcal V\,\psi_L),\\
\delta'\phi&=0.
\end{aligned}\tag{27.8.9}
	$$
</synced_block>
将这个加在方程(27.8.1)上并与方程(27.8.4)比较表明de Wit–Freedman变换确实是一个传统超对称变换与相应扩充规范变换(27.8.8)的组合:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f811d9036cae1f992209f">
		$$
						\begin{aligned}
\delta\psi_L&=\sqrt2\,\partial_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\delta\mathcal F&=\sqrt2(\bar\alpha_L\not\partial\psi_L),\\
\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81bd942dfd97600b501a">
		$$
						\begin{aligned}
\tilde\delta\psi_L&=\sqrt2\,D_\mu\phi\,\gamma^\mu\alpha_R+\sqrt2\mathcal F\alpha_L,\\
\tilde\delta\mathcal F&=\sqrt2(\bar\alpha_L\not D\psi_L)-2\mathrm iq\phi(\bar\alpha_L\lambda_R),\\
\tilde\delta\phi&=\sqrt2(\bar\alpha_R\psi_L).
\end{aligned}\tag{27.8.4}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f81cba0c7faf3e6a9d4a1">
		$$
		\delta ^ { \prime } \Phi = \mathrm{i} q \Omega \Phi . \tag{27.8.8}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8122a5bbe9e798dd4afc#34cee2b74b3f815aa2a4cac26fd62deb">
	$$
	\tilde { \delta } \Phi = \delta \Phi + \delta ^ { \prime } \Phi . \tag{27.8.10}
	$$
</synced_block>
</content>
</page>
