Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44 as of 2026-06-30T07:38:19.313Z:
<page url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f81239f12c44eda7b664f" title="第 30 章 超图"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"30.3 用超图进行计算"}
</properties>
<content>
我们现在来考虑如果用上一节的结果来计算一组经典势超场 $`S _ { n } ( x , \theta )`$ 及其伴随场的量子有效作用量 $`\Gamma ( S , S ^ { * } )`$ .
沿用16.1节中所讨论的处理方法, 有效作用量可以定义成所有单粒子不可约连通超图的求和, 其中组成单粒子不可约连通超图的顶点直接与内线和外线相连.
对于每条始于或终于一个顶点被 $`x`$ 和 $`\theta`$ 所标记的 $`n`$ 型外线, 我们分别引入一个 c -数因子 $`S _ { n } ( x , \theta )`$ 或 $`S _ { n } ^ { * } ( x , \theta )`$ (但没有传播子).
一个被 $`x , \theta`$ 标记且与 $`N`$ 条入线或出线相连的顶点, 设这 $`N`$ 条线被记为 $`n _ { 1 } , n _ { 2 } , \cdots , n _ { N }`$ ,这个顶点所产生的项就是 i 分别乘以超势 $`\tilde { f } ( \boldsymbol { S } )`$ 中 $`S _ { 1 } S _ { 2 } \cdots S _ { N }`$ 项的系数或该系数的复共轭.
任何一个从 $`x , \theta`$ 标记的顶点出发而进入被 $`x ^ { \prime } , \theta ^ { \prime }`$ 标记的顶点会产生一个传播子, 由方程(30.2.10)和(30.2.17)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f81619dfdf34db952c4a7">
		$$
		\int\left[\prod_i d\phi^i\,d\phi_i^*\right]\exp\{iI_{\mathrm{quad}}[\phi]\}\phi^a\cdots\phi_b^*\cdots=\left[-i\Delta^a{}_b\right]\cdots\Big|_{\mathrm{pairings}}+\xi\text{-terms}.\tag{30.2.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f81438502c852a8f105f4">
		$$
		\Delta _ { n m } ^ { \Phi } ( x , \theta ; x ^ { \prime } , \theta ^ { \prime } ) = \frac 1 4 \mathcal{D} _ { R } ^ { 2 } { \mathcal{D} _ { L } ^ { \prime } } ^ { 2 } \Delta _ { F } ( x - x ^ { \prime } ) \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) \delta _ { n m } . \tag{30.2.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f8173a7c4fbfa58005040">
	$$
	- \frac { \mathrm{i} } { 4 } \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) \Delta _ { F } ( x - x ^ { \prime } ) . \tag{30.3.1}
	$$
</synced_block>
另外, 方程(30.1.7)表明, 超导数 $`\mathcal{D} _ { R } ^ { 2 }`$ 作用在除了进入任意顶点的一条内线或外线以外的所有传播子或者外线的 $`S`$ 因子上, 而超导数 $`\mathcal{D} _ { L } ^ { 2 }`$ 作用在除了进入任意顶点的一条内线或外线以外的所有传播子或者外线的 $`S`$ 因子上.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f81c781ece238f8d78936">
		$$
		f(\mathcal D_R^2S)=\mathcal D_R^2\tilde f(S).\tag{30.1.7}
		$$
	</synced_block_reference>
</callout>
对这些因子的乘积要积掉所有 $`x`$ 和 $`\theta`$ ; 量子有效作用量就是对所有单粒子不可约图做这样的积分并求和.
通过在超空间中分部积分, 与任何一个传播子(例如, 连接被 $`x , \theta`$ 和 $`x ^ { \prime } , \theta ^ { \prime }`$ 标记的顶点)伴随的算符 $`\mathcal{D} _ { L } ^ { 2 }`$ 和(或) $`\mathcal{D} _ { R } ^ { 2 }`$ 可以被挪到其它传播子或外线因子上.
这使得这个内线贡献的因子正比于 $`\delta ^ { 4 } ( \theta -`$ $`\theta ^ { \prime }`$ ).
对 $`\theta ^ { \prime }`$ 的积分就消掉了这个 $`\delta`$ 函数, 并把其它所有的 $`\theta ^ { \prime }`$ 换成 $`\theta`$ .
(在数条内线连接同一对顶点的情况下, 我们可以使用费米 $`\delta`$ 函数的性质 $`[ \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) ] ^ { 2 } = 0 .`$ ) 以这种方法继续下去, 我们最终会得到一个 4 维 $`\theta`$ 积分, 而所有的 $`\mathcal{D}`$ 作用在外线因子 $`S _ { n }`$ 和 $`S _ { m } ^ { * }`$ 上.
即, 尽管一般不在空间坐标上定域,但 $`\Gamma [ S , S ^ { * } ]`$ 在费米坐标上是定域的.
在“规范”变换(30.2.4)下的不变性控制了这个泛函的结构.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f8109a508ec2e623117bf">
		$$
		S^n\to S^n+\mathcal D_R X^n.\tag{30.2.4}
		$$
	</synced_block_reference>
</callout>
这告诉我们每个外线因子 $`S _ { n }`$ 或 $`S _ { n } ^ { * }`$ 上分别要作用算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ , 但会有两个例外.
这两个例外是, 外线都为入线或出线的项, 其中除了一个外线因子 $`S _ { n }`$ 或 $`S _ { n } ^ { * }`$ 外, 其它所有外线因子都要分别用 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 作用且没有其它超导数.
这样的项尽管不能表示成对仅由 $`\Phi _ { n }`$ 和(或) $`\Phi _ { n } ^ { * }`$ 构成的函数的4 -维 $`\theta`$ 积分, 它在变换(30.2.4)下仍然是不变的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f8109a508ec2e623117bf">
		$$
		S^n\to S^n+\mathcal D_R X^n.\tag{30.2.4}
		$$
	</synced_block_reference>
</callout>
这是因为, 这种振幅在这个变换下的改变仅来自于外线因子 $`S _ { n }`$ 或 $`S _ { n } ^ { * }`$ 中不被算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 所作用的那部分的变化, 如果我们用分部积分将其它 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 算符中的一个挪到这个改变上, 那么这个改变就被消掉了.
正如我们在 30.1节看到的, 这样的项在 $`\Gamma [ S , S ^ { * } ]`$ 是 $`\Phi _ { n }`$ 或 $`\Phi _ { n } ^ { * }`$ 的泛函的 $`\mathcal{F}`$ -项, 因此会对超势或者它的复共轭有一修正.
除了这些例外外, $`\Gamma [ S , S ^ { * } ]`$ 中的每一项都可以写为对仅是 $`\Phi _ { n }`$ 和(或) $`\Phi _ { n } ^ { * }`$ 的泛函的 4 维 $`\theta`$ -积分, 因此对有效作用量的 $`D`$ -项部分有一修正.
另外注意到, 如果作用量中的一项中除了一个外线因子 $`S _ { n }`$ 或 $`S _ { n } ^ { * }`$ 外都分别被 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 作用,且被额外的 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 算符作用(例如 $`\mathcal{D} _ { R } ^ { 2 } \mathcal{D} _ { L } ^ { 2 } \mathcal{D} _ { R } ^ { 2 } S _ { n }`$ 或 $`\mathcal{D} _ { L } ^ { 2 } \mathcal{D} _ { R } ^ { 2 } \mathcal{D} _ { L } ^ { 2 } S _ { n } ^ { * }`$ 这样的组合), 那么这样的项也可以通过分部积分写成一个额外的 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 算符作用在先前未微分的外线因子 $`S _ { n }`$ 或 $`S _ { n } ^ { * }`$ 上.
这样的项因此可以表示成对仅是 $`\Phi _ { n }`$ 和(或) $`\Phi _ { n } ^ { * }`$ 的泛函的4 维 $`\theta`$ -积分, 因而可以对作用量的 $`D`$ -项部分有其它修正.
$`\Gamma [ S , S ^ { * } ]`$ 中唯一无法用这种方式写的项是有 $`E`$ 条入外线且只有 $`E - 1`$ 个算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 作用在 $`S _ { n }`$ 外线因子上, 或者 $`E ^ { * }`$ 条出外线e且只有 $`E ^ { * } - 1`$ 个算符 $`\mathcal{D} _ { L } ^ { 2 }`$ 作用在 $`S _ { n } ^ { * }`$ 外线因子上.
因此通过计数超图对 $`\Gamma [ S , S ^ { * } ]`$ 中相应的项贡献的算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 的个数, 我们可以分辨出超图是否对超势或它的共轭有贡献.
我们来计数这些超导数.
考虑如下的连通超图: $`V _ { n }`$ 个有 $`n`$ 条线进入的顶点; $`V _ { n } ^ { * }`$ 个有 $`n`$ 条线离开的顶点; $`I`$ 条内线; $`E`$ 条入外线; 以及 $`E ^ { * }`$ 条出外线.
这些数之间有关系
<synced_block url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f812ebae2f188a29e2dfb">
	$$
	I+E=V^n n_n,\qquad I+E^*=V^{*n}n_n.\tag{30.3.2}
	$$
</synced_block>
那么算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 或 $`\mathcal{D} _ { L } ^ { 2 }`$ 的总数就是
<synced_block url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f812b9f47f26d82473fe7">
	$$
	N_R=V^n(n-\mathbf1)_n=I+E-V=L+V^*+E-1.\tag{30.3.3}
	$$
</synced_block>
和
<synced_block url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f81f6be74e1eeb92ca748">
	$$
	N_L=V^{*n}(n-\mathbf1)_n=I+E^*-V^*=L+V+E^*-1.\tag{30.3.4}
	$$
</synced_block>
其中 $`\textstyle V = \sum _ { n } V _ { n }`$ 是线进入的顶点的总数; $`\begin{array} { r } { V ^ { * } = \sum _ { n } V _ { n } ^ { * } } \end{array}`$ 是线离开的顶点的总数; 而 $`L = I - V -`$ $`V ^ { * } + 1`$ 是圈的个数.
我们看到任何有圈的图有 $`N _ { R } \geq E`$ 和 $`N _ { L } \geq E ^ { * }`$ , 使得算符 $`\mathcal{D} _ { R } ^ { 2 }`$ 的个数足以将所有 $`S _ { n }`$ 转换成 $`\Phi _ { n } = \mathcal{D} _ { R } ^ { 2 } S _ { n }`$ 或它的导数, 以及算符 $`\mathcal{D} _ { L } ^ { 2 }`$ 的个数足以将所有 $`S _ { n } ^ { * }`$ 转换成 $`\Phi _ { n } ^ { * } = \mathcal{D} _ { L } ^ { 2 } S _ { n } ^ { * }`$ 或它的导数.
因此, 任何有圈的图产生的贡献总会正比于左手征超场 $`\Phi _ { n }`$ 及其伴随场的泛函的4维 $`\theta`$ -积分——换句话说, $`D`$ -项.
想要获得对 $`\mathcal{F}`$ 项或其共轭的贡献的唯一方法是分别只有 $`N _ { R } = E - 1`$ 个 $`\mathcal{D} _ { R } ^ { 2 }`$ 算法或只有 $`N _ { L } =`$ $`E ^ { * } - 1`$ 个 $`\mathcal{D} _ { L } ^ { 2 }`$ 算符.
根据方程(30.3.3)和(30.3.4), 这样的图将分别有 $`L \ = \ 0`$ 和 $`V ^ { * } ~ = ~ 0`$ 或 $`L \ =`$ 0和 $`V ~ = ~ 0`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f812b9f47f26d82473fe7">
		$$
		N_R=V^n(n-\mathbf1)_n=I+E-V=L+V^*+E-1.\tag{30.3.3}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f81f6be74e1eeb92ca748">
		$$
		N_L=V^{*n}(n-\mathbf1)_n=I+E^*-V^*=L+V+E^*-1.\tag{30.3.4}
		$$
	</synced_block_reference>
</callout>
换句话说, 由于我们只考虑单粒子不可约图, 我们只能从只有入线的顶点获得 $`\mathcal{F}`$ -项, 且只能从只有出线的顶点获得 $`\mathcal{F}`$ -项的伴随.
这个贡献正是原始超势中的被积 $`\mathcal{F}`$ -项, 或它的伴随.
因此我们再次看到: 直到微扰论的任意阶, 都不存在 $`\mathcal{F}`$ 项有限或无限的重正化.
## 习题
1. 利用方程(30.2.18)计算手征超场的旋量分量和辅助分量的传播子.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f817499daf036a9bdca44#34cee2b74b3f81ceabb6c85a95a5ec85">
		$$
		\biggl [ \Delta _ { n m } ^ { \Phi } ( x , \theta ; x ^ { \prime } , \theta ^ { \prime } ) \biggr ] _ { \theta = \theta ^ { \prime } = 0 } = { \frac { 1 } { 4 } } \biggl ( { \frac { \partial } { \partial \theta _ { R } } } \biggr ) ^ { 2 } \biggl ( { \frac { \partial } { \partial \theta _ { L } ^ { \prime } } } \biggr ) ^ { 2 } \Delta _ { F } ( x - x ^ { \prime } ) \delta ^ { 4 } ( \theta - \theta ^ { \prime } ) \delta _ { n m } . \tag{30.2.18}
		$$
	</synced_block_reference>
</callout>
2. 考虑单个手征超场 $`\Phi`$ 的超对称理论, 它有拉格朗日密度
$$
\mathcal{L} = \frac { 1 } { 2 } \Big [ \Phi ^ { * } \Phi \Big ] _ { D } + 2 \operatorname{Re} \Big ( g [ \Phi ^ { 3 } ] _ { \mathcal{F} } \Big ) ,
$$
其中 $`g`$ 是任意复常数.
利用超图形式体系计算量子有效作用量的单圈贡献.
将答案表示成对坐标及单个格拉斯曼坐标 $`\theta`$ 的积分.
3. 对于动能项是(27.3.18)的超对称阿贝尔规范理论, 规范超场 $`V ( x , \theta )`$ 的超传播子是什么?
</content>
</page>
