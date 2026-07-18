Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701 as of 2026-07-17T17:39:18.517Z:
<page url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.6 微扰无重整定理"}
</properties>
<content>
自一开始, 普通可重整量子场论中的数个发散就被发现在这些理论的超对称版中消失了.
<span color="yellow_bg">随着1975年对超图技术的发展, 证明一些辐射修正不仅有限并且在微扰论中消失了变得可行.</span>
超图将会在第30章进行细致的描述, 但实际上证明最重要的**无重整定理**(non-renormaliation theo-rem)并不需要它们.
这一节将会给出Seiberg\[6\]在1993发展的方法的一个版本, 这个方法将会展示如何从对对称性和解析性的简单考察中得到无重整定理.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- N. Seiberg, Phys. Lett. B318, 469 (1993)
</callout>
考察一个一般的有数个左手征超场 $`\Phi^n`$ 和(或)规范超场 $`V^A`$ 的可重整超对称规范理论.
我们在27.3 节提到过, 如果我们从 $`t _ { A }`$ 和 $`C _ { A B C }`$ 中移出因子 $`g`$ 转而把它放进规范超场中, 那么拉格朗日密度有如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81478d8cf11c8fe1fb35">
	$$
	\mathcal L=[\Phi^\dagger e^{-V}\Phi]_D+2\operatorname{Re}[f(\Phi)]_{\mathcal F}+\frac{1}{2g^2}\operatorname{Re}[\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]_{\mathcal F}.\tag{27.6.1}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\mathcal L
=
[\Phi^\dagger e^{-V}\Phi]_D
+2\operatorname{Re}[f(\Phi)]_{\mathcal F}
+\frac1{2g^2}
\operatorname{Re}\left[
\delta_{AB}
(W_{L,W}^{A})_\alpha(C_W)^{\alpha\beta}(W_{L,W}^{B})_\beta
\right]_{\mathcal F}.
	$$
</callout>
其中超势 $`f ( \Phi )`$ 是左手征超场规范不变的三次多项式.
(我们忽略了可能存在的 $`\theta`$ -项, 它在微扰论中没有任何效应.)
假定我们给圈图中环流的动量附加一个紫外截断 $`\lambda`$ .
**就像在12.4节讨论过的, 我们可以找到一个带有这个截断的定域“威尔逊型”有效拉格朗日量 **$`\mathcal{L} _ { \lambda }`$** , 对于动量低于 **$`\lambda`$** 的过程的 **$`S`$** -矩阵, 它会给出与原始拉格朗日密度相同的结果.**
有效拉格朗日密度的质量和耦合常数现在会依赖于 $`\lambda`$ , 而且有效拉格朗日量中通常会有无限多个耦合项, 即理论的对称性允许的所有可能的项.
然而在超对称理论中, 情况要简单的多.
无重整定理告诉我们, 只要截断**不破坏超对称性和规范不变性**, 直到微扰论的所有阶, 有效拉格朗日量将会有如下的结构
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81dc8ea2c7fc9217bd0a">
	$$
					\begin{aligned}
\mathcal L_\lambda
&=[\mathcal A_\lambda(\Phi,\Phi^\dagger,V,\mathcal D,\cdots)]_D+2\operatorname{Re}[f(\Phi)]_{\mathcal F}\\
&\quad+\frac{1}{2g_\lambda^2}\operatorname{Re}[\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]_{\mathcal F}.
\end{aligned}\tag{27.6.2}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
		\begin{aligned}
\mathcal L_\lambda
={}&[\mathcal A_\lambda]_D
+2\operatorname{Re}[f(\Phi)]_{\mathcal F}\\
&+\frac1{2g_\lambda^2}
\operatorname{Re}\left[
\delta_{AB}
(W_{L,W}^{A})_\alpha(C_W)^{\alpha\beta}(W_{L,W}^{B})_\beta
\right]_{\mathcal F}.
\end{aligned}
	$$
</callout>
其中 $`\mathcal{A} _ { \lambda }`$ 是一般的Lorentz不变且规范不变的函数; “ $`\mathcal D,\cdots`$ ”代表的项包含了对后继变量的超导数或时空导数; $`g _ { \lambda }`$ 是单圈有效规范耦合, 给出它的公式与单圈重整化规范耦合常数相同,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81b1a764cd3e77498fbd">
	$$
	g_\lambda^{-2}=\text{常数}-2b\ln\lambda.\tag{27.6.3}
	$$
</synced_block>
其中 $`b`$ 是 Gell-Mann–Low 函数 $`\beta ( g )`$ 中 $`g ^ { 3 }`$ 的系数, 我们在第18章讨论过.
这是只有一个规范耦合的单规范群的结果, 但是到单规范群和 $`U ( 1 )`$ 规范群直积的推广是平庸的.
**特别地, 注意到有效超势不仅在 **$`\lambda \to \infty`$** 的极限是有限的, 而且至少在微扰论中它不包含原先超势中没有的项, 并且它所包含的那些项的系数没有任何变化.**
为了证明这个定理, 我们将会把这个理论解释成<span color="yellow_bg">有额外两个外规范不变左手征超场的理论</span>的特殊情况, 这个理论的拉格朗日密度是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f816d9893dae6e32a084f">
	$$
	\mathcal L^\sharp=\frac12[\Phi^\dagger e^{-V}\Phi]_D+2\operatorname{Re}[Yf(\Phi)]_{\mathcal F}+\frac12\operatorname{Re}[X\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]_{\mathcal F}.\tag{27.6.4}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\mathcal L^\sharp
=
\frac12[\Phi^\dagger e^{-V}\Phi]_D
+2\operatorname{Re}[Yf(\Phi)]_{\mathcal F}
+\frac12\operatorname{Re}\left[
X\delta_{AB}
(W_{L,W}^{A})_\alpha(C_W)^{\alpha\beta}(W_{L,W}^{B})_\beta
\right]_{\mathcal F}.
	$$
</callout>
当 $`X`$ 和 $`Y`$ 的标量分量 $`x`$ 和 $`y`$ 被赋予值 $`x = 1 / g ^ { 2 }`$ 和 $`y = 1`$ 且它们的旋量分量和辅助分量被设为零时, 这个拉格朗日密度就与原始的拉格朗日密度相同.
由于假定了在截断处理中超对称性和规范不变性是被保护的, 有这些外超场的有效拉格朗日密度必须是一般超场的 $`D`$ -项与左手征超场的 $`\mathcal{F}`$ -项之和:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f8124b616ce3f3b5ebf47">
	$$
	\mathcal{L} _ { \lambda } ^ { \sharp } = \Big [ \mathcal{A} _ { \lambda } ( \Phi , \Phi ^ { \dagger } , V , X , X ^ { \dagger } , Y , Y ^ { \dagger } , \mathcal{D} , \cdots ) \Big ] _ { D } + 2 \operatorname{Re} \Big [ \mathcal{B} _ { \lambda } ( \Phi , W _ { L } , X , Y ) \Big ] _ { \mathcal{F} } , \tag{27.6.5}
	$$
</synced_block>
其中 $`\mathcal{A} _ { \lambda }`$ 和 $`\mathcal{B} _ { \lambda }`$ 均是写出变量的规范不变函数.
我们不在 $`\mathcal{F}`$ -项引入任何超导数或时空导数, 同26.3节一样, 这是因为包含任何左手征超场或它们共轭的导数的项可以重写为对 $`[ \mathcal{A} _ { \lambda } ] _ { D }`$ 的贡献.
(诚然, 方程(27.3.13)表明 $`W _ { L }`$ 本身是由两个 $`\mathcal{D} _ { R }`$ 作用在一个超场 $`\exp ( - 2 V ) \mathcal{D} _ { L } \exp ( 2 V )`$ 上给出的,但这个超场不是规范不变的, 而我们要求 $`\mathcal{A} _ { \lambda }`$ 是规范不变的.)
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f819b9f7fd99a7d1742a0">
		$$
								2t_AW^A_{L\alpha}(x,\theta)
\equiv-\epsilon_{\beta\gamma}\mathcal D_{R\beta}\mathcal D_{R\gamma}
\left[
\exp\!\bigl(+2t_BV^B(x,\theta)\bigr)
\mathcal D_{L\alpha}
\exp\!\bigl(-2t_CV^C(x,\theta)\bigr)
\right].\tag{27.3.13}
		$$
	</synced_block_reference>
</callout>
从拉格朗日密度(27.6.4)获得的两个对称性严格限制了 $`\mathcal{B} _ { \lambda }`$ 对 $`X`$ 和 $`Y`$ 的依赖性.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f816d9893dae6e32a084f">
		$$
		\mathcal L^\sharp=\frac12[\Phi^\dagger e^{-V}\Phi]_D+2\operatorname{Re}[Yf(\Phi)]_{\mathcal F}+\frac12\operatorname{Re}[X\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]_{\mathcal F}.\tag{27.6.4}
		$$
	</synced_block_reference>
</callout>
(这两个对称性都被非微扰效应破缺了, 这将会在第29章考虑.) 
第一个对称性是26.3节讨论的那种**微扰论性的 **$`U ( 1 ) R`$** -对称性**, 其中 $`\theta _ { L }`$ 和 $`\theta _ { R }`$ 被赋予 $`R`$ 值 $`+ 1`$ 和 $`{ - 1 }`$ , 超场 $`\Phi`$ , $`V`$ 和 $`X`$ 是 $`R`$ -中性的, 而 $`Y`$ 的 $`R`$ -值是 $`+ 2`$ .
(回忆, $`f _ { \mathcal{F} }`$ 是 $`f`$ 中 $`\theta _ { L } ^ { 2 }`$ 的系数, 所以为了使 $`f _ { \mathcal{F} }`$ 的 $`R`$ -值为 $`0`$ , 所以 $`f`$ 的 $`R`$ -值必须是 2.) 
因为 $`W _ { L }`$ 是由两个 $`\mathcal{D} _ { R }`$ 和一个 $`\mathcal{D} _ { L }`$ 作用在 $`R`$ -中性超场上给出的, 它的 $`R`$ -值是 $`+ 1`$ .
现在, $`R`$ -不变性要求 $`\mathcal{B} _ { \lambda }`$ 同超势一样有 $`R`$ -值 $`+ 2`$ .
它不能依赖于任何 $`R`$ 值为负的超场, 例如左手征超场的共轭, **因为它是全纯的**, 所以 $`\mathcal{B} _ { \lambda }`$ 只能是 $`Y`$ 的一阶或者是 $`W _ { L }`$ 的二阶, 而系数只能依赖于 $`R`$ -中性超场 $`\Phi`$ 和(或)$`X`$ :
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81569ae6decf5596331c">
	$$
	\mathcal B_\lambda(\Phi,W_L,X,Y)=Yf_\lambda(\Phi,X)+\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}h_{\lambda AB}(\Phi,X).\tag{27.6.6}
	$$
</synced_block>
(Lorentz 不变性要求 $`W _ { L }`$ 的旋量指标要与 $`\epsilon _ { \alpha \beta }`$ 收缩.) 
另一个对称性是** **$`X`$** 平移一个虚的数值常数,**$`X X + \mathrm{i} \xi`$** , 其中 **$`\xi`$** 是实数**.
它对拉格朗日密度(27.6.4)的改变正比于 $`\operatorname{Im}[\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]`$, 而正如我们在27.3节看到的, 这是时空导数, 因此在微扰论中没有效应.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f816d9893dae6e32a084f">
		$$
		\mathcal L^\sharp=\frac12[\Phi^\dagger e^{-V}\Phi]_D+2\operatorname{Re}[Yf(\Phi)]_{\mathcal F}+\frac12\operatorname{Re}[X\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]_{\mathcal F}.\tag{27.6.4}
		$$
	</synced_block_reference>
</callout>
<span color="yellow_bg">除了 </span>$`X`$<span color="yellow_bg"> 在原始拉格朗日密度出现的地方, 这个平移对称性使得 </span>$`X`$<span color="yellow_bg"> 无法出现在有效拉格朗日密度(27.6.5)的其它任何地方.</span>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f8124b616ce3f3b5ebf47">
		$$
		\mathcal{L} _ { \lambda } ^ { \sharp } = \Big [ \mathcal{A} _ { \lambda } ( \Phi , \Phi ^ { \dagger } , V , X , X ^ { \dagger } , Y , Y ^ { \dagger } , \mathcal{D} , \cdots ) \Big ] _ { D } + 2 \operatorname{Re} \Big [ \mathcal{B} _ { \lambda } ( \Phi , W _ { L } , X , Y ) \Big ] _ { \mathcal{F} } , \tag{27.6.5}
		$$
	</synced_block_reference>
</callout>
因此我们得出 $`f _ { \lambda }`$ 独立于 $`X`$ , 而 $`h _ { \lambda A B }`$ 由一个正比于 $`X \delta _ { A B }`$ 的 $`\Phi`$ -无关项和一个与 $`X`$ 独立的项构成.
即,
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81b99f81c5364125ba03">
	$$
	\mathcal B_\lambda(\Phi,W_L,X,Y)=Yf_\lambda(\Phi,X)+\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}\left[c_\lambda\delta_{AB}X+\ell_{\lambda AB}(\Phi)\right].\tag{27.6.7}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\mathcal B_\lambda
=
Yf_\lambda(\Phi,X)
+
(W_{L,W}^{A})_\alpha(C_W)^{\alpha\beta}(W_{L,W}^{B})_\beta
\left[c_\lambda\delta_{AB}X+\ell_{\lambda AB}(\Phi)\right].
	$$
</callout>
<span color="yellow_bg">其中 </span>$`c _ { \lambda }`$<span color="yellow_bg"> 是截断无关的实常数.</span>
引入外辅助超场 $`X`$ 和 $`Y`$ 的目的在于, 通过赋予它们合适的值, 我们可以使用弱耦合近似定出方程(27.6.7)中的系数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81b99f81c5364125ba03">
		$$
		\mathcal B_\lambda(\Phi,W_L,X,Y)=Yf_\lambda(\Phi,X)+\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}\left[c_\lambda\delta_{AB}X+\ell_{\lambda AB}(\Phi)\right].\tag{27.6.7}
		$$
	</synced_block_reference>
</callout>
如果我们令 $`X`$ 和 $`Y`$ 的旋量分量和辅助分量为零, 并令它们的标量分量**分别趋于无穷大和零**, 那么规范耦合常数将以 $`1 / \sqrt { x }`$ 的速率趋于零, 而从超势导出的所有Yukawa耦合和标量耦合将以 $`y`$ 的速率趋于零.
在这个极限下, 对(27.6.7)中正比于 $`Y`$ 的项有贡献的只有一个图,这个图有一个来自于 $`2 \operatorname{Re} [ Y f ( \Phi ) ] _ { \mathcal{F} }`$ 的单顶点, 所以
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81b99f81c5364125ba03">
		$$
		\mathcal B_\lambda(\Phi,W_L,X,Y)=Yf_\lambda(\Phi,X)+\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}\left[c_\lambda\delta_{AB}X+\ell_{\lambda AB}(\Phi)\right].\tag{27.6.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f8120912ccd24a4ac7b39">
	$$
	f _ { \lambda } ( \Phi ) = f ( \Phi ) . \tag{27.6.8}
	$$
</synced_block>
另外, 在 $`Y = 0`$ 时, 有一个守恒律要求 $`\mathcal{L} _ { \lambda } ^ { \sharp }`$ 中的所有项有相同数目的 $`\Phi`$ 和 $`\Phi ^ { \dagger }`$ , 又因为 $`\Phi ^ { \dagger }`$ 不能出现在 $`\ell _ { \lambda A B }`$ 中, 所以 $`\Phi`$ 也不能.
这样, 对于单群, 规范不变性就要求常数 $`\ell _ { \lambda A B }`$ 正比于 $`\delta _ { A B }`$ :
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f812598aad98821615f1d">
	$$
	\ell _ { \lambda A B } = \delta _ { A B } L _ { \lambda } . \tag{27.6.9}
	$$
</synced_block>
现在, 由于规范传播子趋于 $`1 / x`$ 而纯规范相互作用趋于 $`x`$ 且标量传播子与相互作用与 $`x`$ 无关, 在$`y = 0`$ 时, 对于有 $`V _ { W }`$ 个纯规范玻色则顶点, $`I _ { W }`$ 个规范玻色子内线以及任意多个标量-规范玻色子顶点和标量传播子的图, 这个图中 $`x`$ 的幂次是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f810b95f6f36f60d1c035">
	$$
	N _ { x } = V _ { W } - I _ { W } . \tag{27.6.10}
	$$
</synced_block>
圈的个数是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f811393cce3118851ef53">
	$$
	\mathcal L=I_W+I_\Phi-V_W-V_\Phi+1.\tag{27.6.11}
	$$
</synced_block>
其中 $`I _ { \Phi }`$ 是内 $`\Phi`$ 线的个数, $`V _ { \Phi }`$ 是 $`\Phi - V`$ 相互作用顶点的个数.
所有 $`\Phi { - } V`$ 顶点有两个 $`\Phi`$ 线与其相连, 所以当没有外 $`\Phi`$ 线时, $`I _ { \Phi }`$ 等于 $`V _ { \Phi }`$ , 因而在方程(27.6.11)中抵消了, 这使得方程(27.6.10)可以写成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f811393cce3118851ef53">
		$$
		\mathcal L=I_W+I_\Phi-V_W-V_\Phi+1.\tag{27.6.11}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f810b95f6f36f60d1c035">
		$$
		N _ { x } = V _ { W } - I _ { W } . \tag{27.6.10}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81beb018e96b372cc98a">
	$$
	N _ { x } = 1 - L . \tag{27.6.12}
	$$
</synced_block>
因此<span color="yellow_bg">树级近似正确地给出了 </span>$`X`$<span color="yellow_bg"> 在方程(27.6.7)中的系数 </span>$`c _ { \lambda }`$<span color="yellow_bg"> , </span>因而这个系数也就是它在原始拉格朗日量中的值, 即 $`c _ { \lambda } = 1`$ , 而 $`X`$ -无关项的系数 $`L _ { \lambda }`$ 仅由单圈图给定.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81b99f81c5364125ba03">
		$$
		\mathcal B_\lambda(\Phi,W_L,X,Y)=Yf_\lambda(\Phi,X)+\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}\left[c_\lambda\delta_{AB}X+\ell_{\lambda AB}(\Phi)\right].\tag{27.6.7}
		$$
	</synced_block_reference>
</callout>
综上, 我们有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f818b8921f045fb90fa0f">
	$$
	\begin{array} { l } { \displaystyle \mathcal{L} _ { \lambda } ^ { \sharp } = \Big [ \mathcal{A} _ { \lambda } ( \Phi , \Phi ^ { \dagger } , V , X , X ^ { \dagger } , Y , Y ^ { \dagger } , \mathcal{D} \cdots ) \Big ] _ { D } + 2 \operatorname{Re} \Big [ Y f ( \Phi ) \Big ] _ { \mathcal{F} } } \\ { \displaystyle \quad + \frac { 1 } { 2 } \operatorname{Re} \Bigg [ \Big ( X + L _ { \lambda } \Big ) \epsilon _ { \alpha \beta } W _ { A \alpha L } W _ { A \beta L } \Bigg ] _ { \mathcal{F} } , } \end{array} \tag{27.6.13}
	$$
</synced_block>
其中 $`L _ { \lambda }`$ 是单圈贡献.
令 $`Y \ = \ 1`$ 和 $`X \ = \ 1 / g ^ { 2 }`$ 就给出了方程(27.6.2), 其中 $`g _ { \lambda } ^ { - 2 } = g ^ { - 2 } + L _ { \lambda }`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81dc8ea2c7fc9217bd0a">
		$$
						\begin{aligned}
\mathcal L_\lambda
&=[\mathcal A_\lambda(\Phi,\Phi^\dagger,V,\mathcal D,\cdots)]_D+2\operatorname{Re}[f(\Phi)]_{\mathcal F}\\
&\quad+\frac{1}{2g_\lambda^2}\operatorname{Re}[\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]_{\mathcal F}.
\end{aligned}\tag{27.6.2}
		$$
	</synced_block_reference>
</callout>
正如18.3 中展示过的, 无论用何种重整化方案定义耦合 $`g _ { \lambda }`$ , 对 $`\lambda { \mathrm { d } } g _ { \lambda } / { \mathrm { d } } \lambda`$ 的领头阶贡献是 $`g _ { \lambda }`$ 的相同函数, 所以到单圈阶, 我们必须有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81ce866ae5d586e3df8c">
	$$
	\lambda { \mathrm d } g _ { \lambda } / { \mathrm d } \lambda = b g _ { \lambda } ^ { 3 } , \tag{27.6.14}
	$$
</synced_block>
其中 $`b`$ 与 Gell-Mann 和Low的重整化群方程中 $`g ^ { 3 }`$ 的系数相同.
解是方程(27.6.3), 完成了证明.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81b1a764cd3e77498fbd">
		$$
		g_\lambda^{-2}=\text{常数}-2b\ln\lambda.\tag{27.6.3}
		$$
	</synced_block_reference>
</callout>
<empty-block/>
在有一个 $`U ( 1 )`$ 规范超场 $`V _ { 1 }`$ 的理论中, 拉格朗日量可能会包含一个 Fayet–Iliopoulos 项(27.2.7):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81fcb6d0c3edb7d1a098">
		$$
		\mathcal{L} _ { \mathrm{FI} } = \xi D , \tag{27.2.7}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f810086e9c8d763bdfead">
	$$
	\mathcal{L} _ { \mathrm{FI} } = \xi \left[ V _ { 1 } \right] _ { D } . \tag{27.6.15}
	$$
</synced_block>
容易看到这种项的系数 $`\xi`$ 是没有重整化过的.\[7\] 
如果威尔逊型拉格朗日密度中的相应系数 $`\xi _ { \lambda }`$ 不依赖与规范耦合或者超势中的耦合, 那么当我们将原始拉格朗日量(27.6.1)替换成包含外超场 $`X`$ 和$`Y`$ 的拉格朗日量(27.6.4)时, 超对称性就会要求威尔逊型拉格朗日量中的这一项取如下的形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- 这最先是在超图形式理论中证明的, W. Fischler, H. P. Nilles, J. Polchinski, S. Raby, andL. Susskind, Phys. Rev. Lett. 47, 757 (1981). 这里给出的证明来自 M. Dine, 收录于 Fields,Strings, and Duality: TASI 96, C. Efthimiou and B. Greene 编辑(World Scientific, Singapore,1997
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f810bb4acfc70d8bda10d">
	$$
	\mathcal{L} _ { \mathrm{FI} \lambda } ^ { \sharp } = \Big [ \xi _ { \lambda } ( X , Y , X ^ { * } , Y ^ { * } ) V _ { 1 } \Big ] _ { D } , \tag{27.6.16}
	$$
</synced_block>
其中 $`\xi _ { \lambda }`$ 是一个以不平庸的方式依赖于 $`X`$ 和(或) $`Y`$ 和(或)它们的共轭的函数.
但这样的项**不会是规范不变的**, 这是因为, 根据方程(27.2.18), 规范变换会使 $`V _ { 1 }`$ 偏移一个手征超场 $`\mathrm{i} ( \Omega - \Omega ^ { * } ) / 2`$ , 而尽管一个手征超场的 $`D`$ -项为零, 如果 $`\xi _ { \lambda }`$ 依赖于其它超场, $`\mathrm{i} ( \Omega - \Omega ^ { * } ) / 2`$ 与 $`\xi _ { \lambda }`$ 的乘积对于一般的规范变换不是手征的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81daaac0d2a6f8a9f629">
		$$
		V(x,\theta)\to V(x,\theta)+\frac{\mathrm{i}}2[\Omega(x,\theta)-\Omega^*(x,\theta)].\tag{27.2.18}
		$$
	</synced_block_reference>
</callout>
确实有对 $`\xi _ { \lambda }`$ 有贡献且独立于所有耦合常数的图.
对于拉格朗日量(27.6.1), 在规范超场与手征物质相互左右的顶点没有规范耦合 $`g`$ 的因子, 但每个规范传播子有一个因子 $`g ^ { - 2 }`$ ,所以一个没有内规范线且没有手征超场自耦合的图将不会依赖于耦合常数.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81478d8cf11c8fe1fb35">
		$$
		\mathcal L=[\Phi^\dagger e^{-V}\Phi]_D+2\operatorname{Re}[f(\Phi)]_{\mathcal F}+\frac{1}{2g^2}\operatorname{Re}[\delta_{AB}\epsilon^{\alpha\beta}W^A_{\alpha L}W^B_{\beta L}]_{\mathcal F}.\tag{27.6.1}
		$$
	</synced_block_reference>
</callout>
这样的对 $`\xi _ { \lambda }`$ 有贡献的图只有那些单个外规范线与一个手征圈相连的图.
(参看图27.1).
![图 27.1 超对称性被标量场和它们的共轭之间的三线性耦合破缺的理论中二次发散的单圈图. 这些线均代表复标量场.](https://prod-files-secure.s3.us-west-2.amazonaws.com/d3aee2b7-4b3f-81c2-8179-00038068497b/e190cc42-a5b6-4379-8b8d-d22acbe7f07c/96f24e93b76057987fd3c6c38151367292b6543f8040bf2a8fbf2c6672dc0413.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSJ2STYL%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T010143Z&X-Amz-Expires=300&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0x9udcXs92grneLDzErlfQFvgvGoc1IRGVMC60fFHvAiEAr5jzpGMjQ1PwLp3rhfvt5kDu9lNPQ3XhY%2F300Iqu79kq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDNW9%2BFXoYb4L3GWVJCrcAwrb2TViuglFPnw4XVDUTQu4FFNVN7EiT7mMpIJ%2FYCHjYYdyZSaBuWtWYnuDx5OtgvCuo54HZ69HorrMZ9HEhgnIimWySFZ0YSnBTSljloQ9nzmFBo6A4mZH4LjEcCbkzqL%2BDCzjluK2qSSB2GAPcH7sAYXU4G4LkzET9l8oczOmOFtxwc2L8w0tuBIT53RxoKuf3KihSAlhHwkHd9WGp%2FBeYWD5yAXwDPoNqAhX5WmUrqKeWZZxq8DQYYLxiMjlOb4xpSRuDONXtxbEKtTH7rVruKrmAipK8BqH7hdbT9suzrgfKyG%2F9frZeXiBMCPlmu43M%2BkHqIjsAARWlgFZKZvbkM%2BnjT1VFsFM9kVrTOccxbbpgKukdWFUEvbJcgSgEO%2BCekgCFWpCD2sZfHjWmEfN1nT%2B7w94huKKoYXUljS8LUixH3Gc2%2BBNQVS6PpG8mCuJdig98Gw1wGVjE6fJflJCUHicYhLmd%2BlmZaWz7cLOrt35RWJxU714ZYL%2FFHXbYbKukcqh%2FWVtFd%2BvaO7XNZVeAgnLMdNMA7X6g7wHry0FYs2Y7w5QOYsq79BrZU2RtsM6HH7i3U%2BoZACccrm3U%2FMuub0Zq%2FHiwMSpb%2FkQmXikaEXWT6F0xQExIU1WMOmU69IGOqUBKZJ%2BS5cz0XBrc0uHHsw0VfqNAc0cjH4kiACJHBN5dTOQjr7zg6WdYRyLouhUMbnMyWxPY7iHy9LeZbQfoLubPvV3eCaTjR06JfL5QkszT6%2FtAHO%2BtYLBYVQ3HRxkRslFP7lz0h4yS2fxdu54WNTcQuC1NxIbI4i%2BL7f%2FrP167Ec3DPLEowdR6%2FIitnnPE6S9o6PuSZSfJfBEYAdGWvgYIIWE1clY&X-Amz-Signature=4e2099ca502ee251acf678619ae3cdfb14c6ad56f39e8c84554d040e9886232f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
所有这种图的贡献正比于所有手征超场的规范耦合之和——即, 正比于 $`U ( 1 )`$ 生成元的迹.
<span color="yellow_bg">但就像在22.4节讨论过的那样, (如果 </span>$`U ( 1 )`$<span color="yellow_bg"> 对称性是不破缺的,) 为了避免破坏 </span>$`U ( 1 )`$<span color="yellow_bg"> 流守恒的引力反常, 这个迹必须为零.</span>
这些定理的最重要应用是一个推论, 这个推论告诉我们, 如果没有 Fayet–Iliopoulos 项且如果超势 $`f ( \Phi )`$ 使得方程 $`\partial f ( \phi ) / \partial \phi _ { n } = 0`$ 有解, 那么超对称性在微扰论的任何有限阶都是不破缺的.
为了检验这点, 我们必须<span color="yellow_bg">检查 Lorentz 不变的场构形,</span> 在这种场构形中, $`\Phi^n`$ 只有常标量分量 $`\phi^n`$ 和常辅助分量 $`\mathcal F^n`$, 而矩阵规范超场 $`V`$ 中规范生成元 $`t_A`$ 的系数 $`V^A`$ (在 Wess-Zumino 规范下)只有辅助分量 $`D^A`$.
如果存在 $`\phi _ { n }`$ 的值使得 $`{ \mathcal{L} } _ { \lambda }`$ 中没有 $`\mathcal{F} _ { n }`$ 或 $`D _ { A }`$ 的一阶项, 这时当然就有 $`\mathcal F_n=D_A=0`$ 的平衡解, 那么超对称性就是不破缺的.
(在29.2节, 我们将看到这是超对称性不破缺的充分必要条件.) 
在没有 Fayet-Iliopoulos 项时, 如果对于所有的 $`A`$ 有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81e99823f91be3e76f14">
	$$
	\frac { \partial K _ { \lambda } ( \phi , \phi ^ { * } ) } { \partial \phi _ { n } ^ { * } } ( t _ { A } ) ^ { m } { } _ { n } \phi _ { m } ^ { * } = 0 \tag{27.6.17}
	$$
</synced_block>
闭对所有的 $`n`$ 有
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f818dbb24cf4fa5a0c7de">
	$$
	\frac { \partial f ( \phi ) } { \partial \phi _ { n } } = 0 , \tag{27.6.18}
	$$
</synced_block>
其中有效 Kähler势 $`K _ { \lambda } ( \phi , \phi ^ { * } )`$ 是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f8145b643e8b2b19b98f0">
	$$
	K _ { \lambda } ( \phi , \phi ^ { * } ) = \mathcal{A} _ { \lambda } ( \phi , \phi ^ { * } , 0 , 0 \cdots ) , \tag{27.6.19}
	$$
</synced_block>
$`\mathcal A_\lambda(\phi,\phi^*,0,0,\cdots)`$ 从 $`\mathcal A_\lambda`$ 中通过设规范超场和所有超势等于零获得的, 那么就将是这样的情况.
(在超导数被 Lorentz不变性要求为零后, $`\mathcal{A} _ { \lambda }`$ 对 $`V`$ 的唯一依赖是每个 $`\Phi ^ { \dagger }`$ 因子后面的因子 $`\exp ( - V )`$ .)
我们现在使用在27.4节用过的一个技巧.
如果方程(27.6.18)有任何解 $`\phi ^ { ( 0 ) }`$ , 那么规范对称性告诉我们存在这样一组连续的解, 即 $`\phi _ { n }`$ 被替换成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f818dbb24cf4fa5a0c7de">
		$$
		\frac { \partial f ( \phi ) } { \partial \phi _ { n } } = 0 , \tag{27.6.18}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f811fa3c2ce3ebd71e087">
	$$
	\phi _ { n } ( z ) = \Bigl [ \exp ( \mathrm{i} t _ { A } z ^ { A } ) \Bigr ] ^ { n } { } _ { m } \phi _ { m } ^ { ( 0 ) } , \tag{27.6.20}
	$$
</synced_block>
其中(既然 $`f`$ 只依赖于 $`\phi`$ 而不依赖于 $`\phi^*`$) $`z_A`$ 是任意一组复参量.
如果 $`K _ { \lambda } ( \phi , \phi ^ { * } )`$ 在曲面 $`\phi = \phi ( z )`$ 的任何一处有一个稳定点, 那么在那一点
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81afa696ed11292cd458">
	$$
	0 = \frac { \partial K _ { \lambda } ( \phi , \phi ^ { * } ) } { \partial \phi _ { n } } ( t _ { A } ) ^ { n } { } _ { m } \phi _ { m } \delta z ^ { A } - \frac { \partial K _ { \lambda } ( \phi , \phi ^ { * } ) } { \partial \phi _ { n } ^ { * } } ( t _ { A } ) ^ { m } { } _ { n } \phi _ { m } ^ { * } \delta z ^ { A * } . \tag{27.6.21}
	$$
</synced_block>
由于这对所有无限小的复 $`\delta z _ { A }`$ 都必须满足, $`\delta z _ { A }`$ 和 $`\delta z _ { A } ^ { * }`$ 的系数都必须为零, 所以方程(27.6.17)和方程(27.6.18)在这一点都是满足的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f81e99823f91be3e76f14">
		$$
		\frac { \partial K _ { \lambda } ( \phi , \phi ^ { * } ) } { \partial \phi _ { n } ^ { * } } ( t _ { A } ) ^ { m } { } _ { n } \phi _ { m } ^ { * } = 0 \tag{27.6.17}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81cb89ddd43057494701#34cee2b74b3f818dbb24cf4fa5a0c7de">
		$$
		\frac { \partial f ( \phi ) } { \partial \phi _ { n } } = 0 , \tag{27.6.18}
		$$
	</synced_block_reference>
</callout>
<span color="yellow_bg">**因此 **</span>$`K _ { \lambda } ( \phi , \phi ^ { * } )`$<span color="yellow_bg">** 在曲面 **</span>$`\phi = \phi ( z )`$<span color="yellow_bg">** 上有稳定点表明超对称性在微扰论的所有阶都是不破缺的.**</span>
零阶 Kähler势 $`\left( \phi ^ { \dagger } \phi \right)`$ 下有解且在 $`\phi\to\infty`$ 时趋于无穷, 所以它肯定在曲面 $`\phi=\phi(z)`$ 上有最小值点, 那么显然它在这个点上是稳定的.
如果这个最小值点没有平坦方向, 即 $`K _ { \lambda }`$ 在这个方向是常数, 那么对 Kähler势任何充分小的微扰会移动这个最小值点, 但是不会摧毁它.
Kähler 势在曲面 $`\phi = \phi ( z )`$ 上的最小值点有平坦方向: $`z _ { A }`$ 为实数的普通整体规范变换 $`\begin{array} { r } { \delta \phi = \mathrm{i} \delta z ^ { A } t _ { A } \phi } \end{array}`$ .
但它们同时是微扰 $`K _ { \lambda } ( \phi , \phi ^ { * } ) - ( \phi ^ { \dagger } , \phi )`$ 的平坦方向, 所以至少对于任何在有限范围内的微扰, $`K _ { \lambda }`$ 在曲面 $`\phi = \phi ( z )`$ 上仍然有一个定域最小值点, 因此对于 $`K _ { \lambda } ( \phi , \phi ^ { * } )`$ 中出现的任何耦合常数, 到这些耦合常数的所有阶, $`K _ { \lambda }`$ 在曲面 $`\phi = \phi ( z )`$ 上都有一个定域最小值点.
而正如我们看到的, 这是使得对于所有 $`n`$ 和 $`A`$ 都有 $`\mathcal{F} _ { n } = 0`$ 和 $`D _ { A } = 0`$ 的标量场值, 也就意味着超对称性是不破缺的.
<empty-block/>
<span color="yellow_bg">这些结果也可以被推广至不可重整理论.\[3\]</span>
	在这种理论中, 方程(27.6.1)中的第一项 $`[\Phi^\dagger e^{-V}\Phi]_D`$ 要被替换成 $`\Phi^\dagger`$, $`\Phi`$, $`V`$ 以及它们的超导数和时空导数的一个任意规范不变实标量函数的 $`D`$-项, 而方程(27.6.1)中的第二项和第三项要被换成 $`\Phi^n`$ 和 $`W_\alpha`$ 的任意一个整体规范不变标量函数 $`f(\Phi,W)`$ 的 $`\mathcal F`$-项.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- S. Weinberg, Phys. Rev. Lett. 80, 3702 (1998)
</callout>
业已证明, 到微扰论的所有阶, 除了 $`W`$ 二次项的单圈重整化外, 威尔逊型拉格朗日量的 $`\mathcal{F}`$ -项中出现的函数 $`f _ { \lambda } ( \Phi , W )`$ 与 $`f ( \Phi , W )`$ 相同.
<empty-block/>
</content>
</page>
