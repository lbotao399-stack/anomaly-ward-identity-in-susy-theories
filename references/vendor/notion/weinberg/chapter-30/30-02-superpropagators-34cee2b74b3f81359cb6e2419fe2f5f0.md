Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0 as of 2026-06-30T07:35:57.810Z:
<page url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f81239f12c44eda7b664f" title="第 30 章 超图"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"30.2 超传播子"}
</properties>
<content>
通常情况下, 可以直接从作用量中场的二次部分直接获得传播子.
如果我们把复标量场 $`\phi _ { i }`$ (其中 $`i`$ 是包含时空坐标以及自旋和种类指标的混合指标)的二次部分写成如下形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f814aacedd28355fb3227">
	$$
	I_{\mathrm{quad}}[\phi]=-\phi^*_iD^i{}_j\phi^j.\tag{30.2.1}
	$$
</synced_block>
其中 $`D _ { i j }`$ 是厄米的, 那么就像 9.4节中解释的那样, 传播子就是 $`\Delta = D ^ { - 1 }`$ .
当对于某类矢量 $`\xi`$ , 作用量在(线性化)规范变换
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81c5afbac7bed5f9968d">
	$$
	\phi^i\to\phi^i+\xi^i.\tag{30.2.2}
	$$
</synced_block>
下不变时, 这就会出现问题.
在这个情况下, 我们有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81d19c28c4079ab1a1b0">
	$$
	D^i{}_j\xi^j=0.\tag{30.2.3}
	$$
</synced_block>
显然我们对“矩阵” $`D _ { i j }`$ 求逆.
在电动力学中, 产生这个问题是因为拉格朗日密度在规范变换 $`A _ { \mu } \to`$ $`A _ { \mu } + \partial _ { \mu } \Lambda`$ 下不变.
我们这里也有这个问题: 由于作用量实际上是 $`\mathcal{D} _ { R } ^ { 2 } S _ { n }`$ 而非 $`S _ { n }`$ 自身的泛函, 对于任何超场, 在变换
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f8109a508ec2e623117bf">
	$$
	S^n\to S^n+\mathcal D_R X^n.\tag{30.2.4}
	$$
</synced_block>
作用量是不变的.
在带电粒子的电动力学中, 因规范不变性引起的问题一般通过选择规范来解决, 例如通过15.5节描述的 Faddeev–Popov–de Witt 方法.
但这里在变换(30.2.2)下不变而引起的问题更像是光子的有效场论在能量低于产生带电粒子时的问题, 这时理论规范不变就是因为作用量只包含规范不变的场.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81c5afbac7bed5f9968d">
		$$
		\phi^i\to\phi^i+\xi^i.\tag{30.2.2}
		$$
	</synced_block_reference>
</callout>
在这种理论中有一个更加简单的做法.
除了 $`D _ { i j }`$ 本征值为零的本征矢 $`\xi _ { i }`$ (简单起见取在一个单一的方向上), 我们可以找到一组本征值 $`d _ { \nu } \neq 0`$ 的正交本征矢 $`u _ { \nu i }`$ :
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f8125a121d3df7c9a96b5">
	$$
	D^i{}_j u_\nu{}^j=d_\nu u_\nu{}^i,\qquad u^{*\nu}{}_i u_{\nu'}{}^i=\delta^\nu{}_{\nu'},\qquad u^{*\nu}{}_i\xi^i=0.\tag{30.2.5}
	$$
</synced_block>
我们可以引入一组新的积分变量 $`\phi ^ { \prime }`$ 和 $`\phi _ { \nu } ^ { \prime \prime }`$ :
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f8184a314e3cd621a8a14">
	$$
	\phi^i=\phi'\xi^i+\phi^{\prime\nu}u_\nu{}^i.\tag{30.2.6}
	$$
</synced_block>
在量子期望值的 Feynman图计算中所遇到的那类积分就可以写为
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81fcb13de77b95eb2887">
	$$
	\begin{aligned}
&\int\left[\prod_i d\phi^i\,d\phi_i^*\right]\exp\{iI_{\mathrm{quad}}[\phi]\}\phi^a\cdots\phi_b^*\cdots
=J\int d\phi'\,d\phi^{\prime *}\\
&\quad\times\int\left[\prod_\nu d\phi^{\prime\nu}\,d\phi_\nu^{\prime *}\right]
\exp\{-i\phi_\rho^{\prime *}d^\rho{}_\sigma\phi^{\prime\sigma}\}
\left[\phi'\xi^a+\phi^{\prime\nu}u_\nu{}^a\right]\cdots
\left[\phi'\xi^b+\phi^{\prime\lambda}u_\lambda{}^b\right]^*\cdots .
\tag{30.2.7}
\end{aligned}
	$$
</synced_block>
其中 $`\mathcal{J}`$ 是变换(30.2.6)的雅克比行列式.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f8184a314e3cd621a8a14">
		$$
		\phi^i=\phi'\xi^i+\phi^{\prime\nu}u_\nu{}^i.\tag{30.2.6}
		$$
	</synced_block_reference>
</callout>
因为 $`\phi ^ { \prime }`$ 和 $`\phi ^ { \prime * }`$ 没有出现在指数变量中, 所以对 $`\phi ^ { \prime }`$ 和 $`\phi ^ { \prime * }`$ 的积分显然不是合理定义的.
但如果作用量仅含规范不变量, 那么这不成问题, 这是因为这样 $`\phi _ { a } , \phi _ { b }`$ 等就会与“流” $`J _ { a } , J _ { b }`$ 等收缩, 其中流满足
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81d7bb49f34fe3c639a2">
	$$
	\xi^aJ_a=0.\tag{30.2.8}
	$$
</synced_block>
因此我们可以将方程(30.2.7)写成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81fcb13de77b95eb2887">
		$$
		\begin{aligned}
&\int\left[\prod_i d\phi^i\,d\phi_i^*\right]\exp\{iI_{\mathrm{quad}}[\phi]\}\phi^a\cdots\phi_b^*\cdots
=J\int d\phi'\,d\phi^{\prime *}\\
&\quad\times\int\left[\prod_\nu d\phi^{\prime\nu}\,d\phi_\nu^{\prime *}\right]
\exp\{-i\phi_\rho^{\prime *}d^\rho{}_\sigma\phi^{\prime\sigma}\}
\left[\phi'\xi^a+\phi^{\prime\nu}u_\nu{}^a\right]\cdots
\left[\phi'\xi^b+\phi^{\prime\lambda}u_\lambda{}^b\right]^*\cdots .
\tag{30.2.7}
\end{aligned}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f8110a1dacd1fffe5ca6f">
	$$
	\begin{aligned}
&\int\left[\prod_i d\phi^i\,d\phi_i^*\right]\exp\{iI_{\mathrm{quad}}[\phi]\}\phi^a\cdots\phi_b^*\cdots
=C\int\left[\prod_\nu d\phi^{\prime\nu}\,d\phi_\nu^{\prime *}\right]\\
&\quad\times\exp\{-i\phi_\rho^{\prime *}d^\rho{}_\sigma\phi^{\prime\sigma}\}
\left[\phi^{\prime\nu}u_\nu{}^a\right]\cdots\left[\phi^{\prime\lambda}u_\lambda{}^b\right]^*\cdots
+\xi\text{-terms}.
\tag{30.2.9}
\end{aligned}
	$$
</synced_block>
其中“ $`\xi`$ -项”是指正比一个或多个 $`\xi _ { a } , \xi _ { b }`$ 等因子的项, 这些项与满足方程(30.2.8)的 $`J`$ 收缩后为零, 而$`\mathcal{C}`$ 是无限大常数 $`\mathcal{J} \int \mathrm { d } \phi ^ { \prime }`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81d7bb49f34fe3c639a2">
		$$
		\xi^aJ_a=0.\tag{30.2.8}
		$$
	</synced_block_reference>
</callout>
这样, 对 $`\phi _ { \nu } ^ { \prime }`$ 的积分就给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81619dfdf34db952c4a7">
	$$
	\int\left[\prod_i d\phi^i\,d\phi_i^*\right]\exp\{iI_{\mathrm{quad}}[\phi]\}\phi^a\cdots\phi_b^*\cdots=\left[-i\Delta^a{}_b\right]\cdots\Big|_{\mathrm{pairings}}+\xi\text{-terms}.\tag{30.2.10}
	$$
</synced_block>
其中对配对(pairings)求和是指对 $`\phi`$ 的指标和 $`\phi ^ { * }`$ 的指标进行配对的所有方式求和, 而 $`\Delta _ { a b }`$ 是传播子
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81268853db0c0102a2ae">
	$$
	\Delta^a{}_b=u_\nu{}^a(d^{-1})^\nu{}_\rho u^{*\rho}{}_b.\tag{30.2.11}
	$$
</synced_block>
取代计算求和(30.2.11), 我们可以使用它的定义性质
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81268853db0c0102a2ae">
		$$
		\Delta^a{}_b=u_\nu{}^a(d^{-1})^\nu{}_\rho u^{*\rho}{}_b.\tag{30.2.11}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81e1931cc811757643d3">
	$$
	D^a{}_c\Delta^c{}_b=u_\nu{}^a u^{*\nu}{}_b\equiv\Pi^a{}_b.\tag{30.2.12}
	$$
</synced_block>
其中Π是投影到与 $`\xi`$ 正交的空间的算符:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81f9a226d3f77e6fe189">
	$$
	\Pi^a{}_c\Pi^c{}_b=\Pi^a{}_b,\qquad \Pi^a{}_b\xi^b=0.\tag{30.2.13}
	$$
</synced_block>
方程(30.2.12)的解仅在相差 $`\xi`$ -项意义下是唯一的, 但如果场 $`\phi _ { i }`$ 仅以规范不变组合的方式出现在作用量中, 那么它们就不会造成问题.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81e1931cc811757643d3">
		$$
		D^a{}_c\Delta^c{}_b=u_\nu{}^a u^{*\nu}{}_b\equiv\Pi^a{}_b.\tag{30.2.12}
		$$
	</synced_block_reference>
</callout>
例如, 在电动力学中, 我们可以将作用量的动能部分写成
$$
I_{\mathrm{quad}}[A]=-\frac14\int d^4x\,f_{\mu\nu}f^{\mu\nu}=\frac12\int d^4x\,A^\mu\left(\Box\delta_\mu{}^\nu-\partial_\mu\partial^\nu\right)A_\nu.
$$
微分算符 $`- \bigtriangledown \delta _ { \mu } { } ^ { \nu } + \partial ^ { \nu } \partial _ { \mu }`$ 不是可逆的, 因为它有一个本征值为零的本征矢, 形如 $`\xi ^ { \mu } = \partial ^ { \mu } \Lambda`$ .
投影到与这些矢量正交的空间的算符是
$$
\Pi_\mu{}^\nu(x,y)=\left[\delta_\mu{}^\nu-\partial_\mu\partial^\nu\Box^{-1}\right]\delta^4(x-y).
$$
其中 $`\square ^ { - 1 } \delta ^ { 4 } ( x - y )`$ 是方程 $`[ [ \Sigma ^ { - 1 } \delta ^ { 4 } ( x - y ) ] = \delta ^ { 4 } ( x - y )`$ 的任意解.
这个传播子的定义解是
$$
\left(-\Box\delta_\mu{}^\lambda+\partial_\mu\partial^\lambda\right)\Delta_\lambda{}^\nu(x,y)=\Pi_\mu{}^\nu(x,y).
$$
它有解
其中 $`\Delta _ { F } ( x - y )`$ 是通常的 Feynman 传播子(6.2.16), 满足 $`\sqcup \Delta _ { F } ( x - y ) = - \delta ^ { 4 } ( x - y )`$ .
(作用量中的 $`1 / 2`$ 因子没有出现在这里的传播子的定义方程中是因为 $`A _ { \mu }`$ 是实场.
而对于方程(6.2.16)中的Fourier 积分分母中的−iϵ, 9.2 节中的路径积分形式理论解释了它的起源.)
对方程(30.1.9)第一项的观察表明时实超场传播子的定义方程是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f8138a5b3eab7e3bac613">
		$$
		I[\mathcal D_R^2S]=-\frac14\int d^4x\int d^4\theta\,S^*_n\mathcal D_L^2\mathcal D_R^2S^n-\operatorname{Re}\int d^4x\int d^4\theta\,\tilde f(S).\tag{30.1.9}
		$$
	</synced_block_reference>
</callout>
$$
-\frac14\mathcal D_L^2\mathcal D_R^2(\Delta^S)^n{}_m(x,\theta;x',\theta')=\mathcal P\delta^4(x-x')\delta^4(\theta-\theta')\delta^n{}_m.\tag{30.2.14}
$$
其中 $`\mathcal{P}`$ 是超空间微分算符, 满足投影算符的条件
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81fbba96e902cbafcb8c">
	$$
	{ \mathcal P } ^ { 2 } = { \mathcal P } , \qquad { \mathcal P } { \mathcal D } _ { R } = 0 , \tag{30.2.14}
	$$
</synced_block>
而 $`\delta ^ { 4 } ( \theta - \theta ^ { \prime } )`$ 是方程(26.6.8)中引入的费米 $`\delta`$ -函数.
解是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81af9a6bd42702e76259">
	$$
	\mathcal{P} = \frac { - 1 } { 1 6 \bigsqcup } \mathcal{D} _ { L } ^ { 2 } \mathcal{D} _ { R } ^ { 2 } . \tag{30.2.15}
	$$
</synced_block>
(显然有 $`\mathcal { P D } _ { R } = 0`$ .
为了验证 $`\mathcal{P} ^ { 2 } = \mathcal{P}`$ , 我们需要使用(26.6.12), 它表明 $`\mathcal{D} _ { R } ^ { 2 } \mathcal{D} _ { L } ^ { 2 } \mathcal{D} _ { R } ^ { 2 } = - 1 6 \bigtriangledown \mathcal{D} _ { R } ^ { 2 } .`$ )方程(30.2.14)的解是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81fbba96e902cbafcb8c">
		$$
		{ \mathcal P } ^ { 2 } = { \mathcal P } , \qquad { \mathcal P } { \mathcal D } _ { R } = 0 , \tag{30.2.14}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f810bbf18e1fc8403b908">
	$$
	\begin{array} { l } { \displaystyle \Delta _ { n m } ^ { S } ( x , \theta ; x ^ { \prime } , \theta ^ { \prime } ) = - \frac { 1 } { 4 \boxdot } \delta ^ { 4 } ( x - x ^ { \prime } ) \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) \delta _ { n m } } \\ { = \frac { 1 } { 4 } \Delta _ { F } ( x - x ^ { \prime } ) \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) \delta _ { n m } + \mathcal{D} _ { R } \ – \overrightarrow { \mathrm { J } } { \mathbb J } . } \end{array} \tag{30.2.16}
	$$
</synced_block>
这是由势超场 $`S _ { m } ^ { * } ( x ^ { \prime } , \theta ^ { \prime } )`$ 产生而被势超场 $`S _ { n } ( x , \theta )`$ 湮灭的线的传播子, 这个传播子就是我们计算作用量(30.1.9)的超图时所要使用的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f8138a5b3eab7e3bac613">
		$$
		I[\mathcal D_R^2S]=-\frac14\int d^4x\int d^4\theta\,S^*_n\mathcal D_L^2\mathcal D_R^2S^n-\operatorname{Re}\int d^4x\int d^4\theta\,\tilde f(S).\tag{30.1.9}
		$$
	</synced_block_reference>
</callout>
为了与普通传播子相联系, 考虑由左手征超场 $`\Phi _ { m } ^ { * } ( x ^ { \prime } , \theta ^ { \prime } )`$ 产生而被左手征超场 $`\Phi _ { n } ( x , \theta )`$ 湮灭的线的传播子是有益的.
通过用 $`\mathcal{D} _ { R } ^ { 2 }`$ 作用 $`S _ { n } ( x , \theta )`$ 并用 $`\mathcal{D} _ { { R } } ^ { \prime 2 } =`$ $`\mathcal{D} _ { \ L } ^ { \prime 2 }`$ 作用 $`S _ { m } ^ { * } ( x ^ { \prime } , \theta ^ { \prime } )`$ 可以获得这些手征超场, 所以左手征超场的传播子是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81438502c852a8f105f4">
	$$
	\Delta _ { n m } ^ { \Phi } ( x , \theta ; x ^ { \prime } , \theta ^ { \prime } ) = \frac 1 4 \mathcal{D} _ { R } ^ { 2 } { \mathcal{D} _ { L } ^ { \prime } } ^ { 2 } \Delta _ { F } ( x - x ^ { \prime } ) \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) \delta _ { n m } . \tag{30.2.17}
	$$
</synced_block>
例如, 传播子中 $`\theta`$ 和 $`\theta ^ { \prime }`$ 的零阶项是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81ceabb6c85a95a5ec85">
	$$
	\biggl [ \Delta _ { n m } ^ { \Phi } ( x , \theta ; x ^ { \prime } , \theta ^ { \prime } ) \biggr ] _ { \theta = \theta ^ { \prime } = 0 } = { \frac { 1 } { 4 } } \biggl ( { \frac { \partial } { \partial \theta _ { R } } } \biggr ) ^ { 2 } \biggl ( { \frac { \partial } { \partial \theta _ { L } ^ { \prime } } } \biggr ) ^ { 2 } \Delta _ { F } ( x - x ^ { \prime } ) \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) \delta _ { n m } . \tag{30.2.18}
	$$
</synced_block>
为了计算它, 我们回忆起费米 $`\delta`$ -函数的方程(26.6.8):
<synced_block url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81beae06deb7f9417257">
	$$
	\delta ^ { 4 } ( \theta - \theta ^ { \prime } ) = \frac { 1 } { 4 } \Big ( ( \theta _ { L } - \theta _ { L } ^ { \prime } ) ^ { \mathrm { T } } \epsilon ( \theta _ { L } - \theta _ { L } ^ { \prime } ) \Big ) \Big ( ( \theta _ { R } - \theta _ { R } ^ { \prime } ) ^ { \mathrm { T } } \epsilon ( \theta _ { R } - \theta _ { R } ^ { \prime } ) \Big ) , \tag{30.2.19}
	$$
</synced_block>
从此我们发现 $`( \partial / \partial \theta _ { R } ) ^ { 2 } ( \partial / \partial \theta _ { L } ^ { \prime } ) ^ { 2 } \delta ( \theta - \theta ^ { \prime } ) = 4`$ .
方程(30.2.19)因此给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81359cb6e2419fe2f5f0#34cee2b74b3f81beae06deb7f9417257">
		$$
		\delta ^ { 4 } ( \theta - \theta ^ { \prime } ) = \frac { 1 } { 4 } \Big ( ( \theta _ { L } - \theta _ { L } ^ { \prime } ) ^ { \mathrm { T } } \epsilon ( \theta _ { L } - \theta _ { L } ^ { \prime } ) \Big ) \Big ( ( \theta _ { R } - \theta _ { R } ^ { \prime } ) ^ { \mathrm { T } } \epsilon ( \theta _ { R } - \theta _ { R } ^ { \prime } ) \Big ) , \tag{30.2.19}
		$$
	</synced_block_reference>
</callout>
$$
\left[(\Delta^\Phi)^n{}_m(x,\theta;x',\theta')\right]_{\theta=\theta'=0}=\Delta_F(x-x')\delta^n{}_m.\tag{30.2.20}
$$
这正是超场标量分量通常的传播子.
</content>
</page>
