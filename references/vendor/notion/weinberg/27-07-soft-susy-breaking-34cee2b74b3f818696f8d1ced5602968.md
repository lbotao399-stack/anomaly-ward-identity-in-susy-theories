Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968 as of 2026-07-17T17:48:09.949Z:
<page url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.7 超对称软破缺"}
</properties>
<content>
我们会在下一章看到, 即使超对称性是作用量的一个精确对称性, **超对称性在高能的自发破缺会在描述低能物理的有效作用量中产生违反超对称守恒的**<span color="yellow_bg">**超可重整项**</span>**.**
这些超可重整项可以解释在可到达能量处没有观测到超对称性的现象.
在这一节, 我们将考虑由这种破坏超对称性的超可重整项产生的辐射修正, 这部分是为了看到这是否为标准模型的超对称版本中引入或排除这种项提供了一个判据.
超对称性破缺的迹象是一般超场的 $`D`$ -项或手征超场的 $`\mathcal{F}`$ -项有期望值.
拉格朗日密度中破缺超对称性的任何算符 $`\epsilon \mathcal{O}`$ 都可以以超对称的形式写成一个 $`D`$ -项
<synced_block url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f819ca737ecb6a95239e2">
	$$
	\epsilon { \mathcal O } = \Big [ Z S \Big ] _ { D } , \tag{27.7.1}
	$$
</synced_block>
**其中 **$`S`$** 是非手征超场, 它的 **$`C`$** -项是 **$`\mathcal{O}`$** , 而 **$`Z`$** 是非手征外超场, 它唯一不为零的分量是 **$`[ Z ] _ { D } = \epsilon`$** .**
部分但不是全部破坏对称性的算符 $`\epsilon \mathcal{O}`$ 也可以写成 $`\mathcal{F}`$ -项,
<synced_block url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f81d5b52ffebb3460d91a">
	$$
	\epsilon\mathcal O=\bigl[\Omega O\bigr]_{\mathcal F}.\tag{27.7.2}
	$$
</synced_block>
或者它们的共轭, 其中 $`O`$ 是 $`\mathcal{F}`$ -项是 $`\mathcal{O}`$ 的左手征超场, 而 $`\Omega`$ 是外左手征超场, 它唯一不为零的分量是 $`[ \Omega ] _ { \mathcal{F} } = \epsilon`$ .
<empty-block/>
对于有效拉格朗日量中一个会出现的给定修正, 通过计算**以超对称的方式构造这个修正所需要的 **$`Z`$** 或 **$`\Omega`$** 的幂次, 我们可以数出 **$`\epsilon`$** 的阶数.**
对于可以写成(27.7.2)和(27.7.1)的形式的那些相互作用, 我们会发现这些相互作用产生的修正有数个有趣的限制.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f81d5b52ffebb3460d91a">
		$$
		\epsilon\mathcal O=\bigl[\Omega O\bigr]_{\mathcal F}.\tag{27.7.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f819ca737ecb6a95239e2">
		$$
		\epsilon { \mathcal O } = \Big [ Z S \Big ] _ { D } , \tag{27.7.1}
		$$
	</synced_block_reference>
</callout>
根据上一节的结果, $`\mathcal{F}`$ -项没有辐射修正, 所以所有对威尔逊型拉格朗日量的破缺超对称的辐射修正必须采取 $`D`$ -项的形式.
这个定理并不阻止任何给定算符出现在威尔逊型拉格朗日量中,这是因为, 即使一个算符 $`\epsilon \Delta \mathcal{L}`$ 无法表示成 $`[ Z \Lambda ] _ { D }`$ 的形式, 其中 $`\Lambda`$ 是 $`C`$ -项为 $`\Delta \mathcal{L}`$ 的一般超场, 但$`\epsilon ^ { 2 } \Delta \mathcal{L}`$ 依旧能表示成
<synced_block url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f81a1b95ff43d9b7d62a0">
	$$
	\epsilon ^ { 2 } \Delta \mathcal{L} = 2 \Big [ \Omega ^ { * } \Omega \Lambda \Big ] _ { D } . \tag{27.7.3}
	$$
</synced_block>
<span color="yellow_bg">但并非所有的算符是由 </span>$`\Omega`$<span color="yellow_bg"> 或 </span>$`\Omega ^ { * }`$<span color="yellow_bg"> 的一阶辐射修正产生的.</span>
特别地, 如果一个函数仅是左手征超场 $`\Phi`$ 的 $`\phi`$ 项的函数, 而不是 $`\phi ^ { * }`$ 的函数, 那么它无法写为对 $`\Omega`$ 是线性的超场的 $`D`$ -项.
(注意, $`[ \Omega h ( \Phi ) ] _ { D }`$ 是一个导数, 而 $`[ \Omega ^ { * } h ( \Phi ) ] _ { D } = 2 [ \Phi ] _ { \mathcal{F} } \partial h ( \phi ) / \partial \phi`$ 不只是 $`\phi`$ 的函数.) 
我们由此得出威尔逊型拉格朗日量中只依赖于 $`\phi`$ 的超对称型破缺项无法由对形如(27.7.2)的超对称破缺相互作用是一阶的辐射修正产生.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f81d5b52ffebb3460d91a">
		$$
		\epsilon\mathcal O=\bigl[\Omega O\bigr]_{\mathcal F}.\tag{27.7.2}
		$$
	</synced_block_reference>
</callout>
这个结果是重要的, 因为绝大多数发散的辐射修正是**超可重整耦合的最低阶.**
更精确些, 对于一个量纲(按能量的幂次)为 $`\mathcal{D}`$ 的相互作用, 它的系数的量纲是 $`4 - \mathcal{D}`$ , 所以对一个量纲为 $`d`$ 的相互作用, 量纲分析表明一组量纲为 $`d _ { 1 }`$ , $`d _ { 2 }`$ 等的相互作用对这个相互作用的系数的贡献至多包含紫外截断的
<synced_block url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f81a1baead4879b3cf0b3">
	$$
	p = 4 - d - ( 4 - d _ { 1 } ) - ( 4 - d _ { 2 } ) - \cdots \tag{27.7.4}
	$$
</synced_block>
次方, 因此在 $`p < 0`$ 是有限的.
(这个讨论忽略了子积分中可能存在的紫外发散; 关于这个问题的全面处理, 参考文献\[8\].) 
超可重整相互作用是“软”的, 也就是说, 它们会**减少它们出现的图的发散度.**
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- 破坏某个整体对称性的超可重整项不会对可重整相互作用的系数引入无限大的对称性破缺辐射修正的细致证明是由 K. Symanzik 给出的, 收录于Cargése Lectures in Physics, Vol. 5,D. Bessis 编辑(Gordon and Breach, New York, 1972). 这在卷 I 第 507 页的脚注中简要讨论过
</callout>
特别地, 在一个所有相互作用都有 $`d _ { i } \leq 4`$ 且 $`d _ { i } = 4`$ 的严格可重整相互作用是超对称的可重整理论中, 对 $`d = 4`$ 的相互作用一个或多个超可重整相互作用对这个相互作用的系数的贡献总会有 $`p < 0`$ , 所以即使它们不是超对称的,<span color="yellow_bg">** 超可重整相互作用不会对超对称 **</span>$`d = 4`$<span color="yellow_bg">** 相互作用的系数产生破缺超对称且紫外发散的修正.**</span>
<empty-block/>
另一方面, 这种力量中或许会有对超可重整相互作用本身的发散辐射修正.\[9\] 
最麻烦的情况是二次(或更高次)发散, 如果在某个很高的能量标度 $`M _ { X }`$ 处截断, 那么为了保证超对称性在能量低于 $`M _ { X }`$ 是一个好的近似对称性, 这种发散会要求对裸耦合常数的精细调节.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- L. Girardello and M. T. Grisaru, Nucl. Phys. B194, 65 (1982), 重印于 Supersymmetry, 参考文献\[1\]; K. Harada and N. Sakai, Prob. Theor. Phys. 67, 67 (1982)
</callout>
根据方程(27.7.4), 在所有 $`d _ { i } = 4`$ 的相互作用都是超对称的理论中, 仅当辐射修正包含一个量纲 $`d _ { 1 } \geq 2 + d`$ 的超可重整超对称性破缺的相互作用插入时, 它们才能产生量纲为 $`d`$ 的二次发散或高次发散( $`p\geq2`$ )的超对称性破缺算符.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f81a1baead4879b3cf0b3">
		$$
		p = 4 - d - ( 4 - d _ { 1 } ) - ( 4 - d _ { 2 } ) - \cdots \tag{27.7.4}
		$$
	</synced_block_reference>
</callout>
这使得要么 $`d = 0`$ 且 $`d _ { 1 } \geq 2`$ , 要么 $`d = 1`$ 且 $`d _ { 1 } = 3`$ , 前者仅在我们计算宇宙常数时出现, 而后者仅在我们计算一个标量线消失于真空中的蝌蚪图时才会出现.
<span color="yellow_bg">对所有已知的理论, 宇宙常数都会产生精细调节的问题,\[10\] 我们这里不会进一步考虑.</span>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- 关于综述, 参看 S. Weinberg, Rev. Mod. Phys. 61, 1-23 (1989)
</callout>
蝌蚪图代表 $`\phi`$ 或 $`\phi ^ { * }`$ 线性的算符, 而我们已经看到, 对于可以写成(27.7.2)的超对称破缺相互作用, 直到它的第一阶都无法产生蝌蚪图.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f818696f8d1ced5602968#34cee2b74b3f81d5b52ffebb3460d91a">
		$$
		\epsilon\mathcal O=\bigl[\Omega O\bigr]_{\mathcal F}.\tag{27.7.2}
		$$
	</synced_block_reference>
</callout>
**因此这种超可重整相互作用是“软的”, 也就是说它们无法引入二次或高次发散.**
连同 $`d \leq 2`$ 的超可重整相互作用, 其中包括 $`\phi`$ 和 $`\phi ^ { * }`$ 的任意二次多项式, 超对称破缺相互作用在如下的意义是软的: 包含可以表示成 $`\phi ^ { 3 } = [ \Omega \Phi ^ { 3 } ] _ { \mathcal{F} }`$ 的 $`\phi`$ 的三阶项, 以及类似的 $`\phi ^ { * }`$ 的三阶项, 还有可以写成 $`[ \Omega \epsilon _ { \alpha \beta } W ^ { \alpha } W ^ { \beta } ] _ { \mathcal{F} }`$ 的 $`d = 3`$ 的规范微子质量项, 但不包含 $`\phi ^ { 2 } \phi ^ { * }`$ 或 $`\phi(\phi^*)^2`$ 这样的项, 这样的项一般会产生二次发散的蝌蚪图.\[9\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- L. Girardello and M. T. Grisaru, Nucl. Phys. B194, 65 (1982), 重印于 Supersymmetry, 参考文献\[1\]; K. Harada and N. Sakai, Prob. Theor. Phys. 67, 67 (1982)
</callout>
然而, 蝌蚪图只能伴随对所有精确对称性都是中性的标量场产生.
在没有这种标量场的理论中, 例如下一章要讨论超对称标准模型, <span color="yellow_bg">所有超可重整相互作用都可以被视为是软的.</span>
</content>
</page>
