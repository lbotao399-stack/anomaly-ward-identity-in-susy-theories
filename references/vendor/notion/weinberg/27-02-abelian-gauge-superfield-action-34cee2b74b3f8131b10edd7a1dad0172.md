Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172 as of 2026-06-30T05:01:53.202Z:
<page url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.2 阿贝尔规范超场的规范不变作用量"}
</properties>
<content>
我们现在要考虑如何给包含规范场 $`V _ { \mu } ^ { A }`$ 的规范超场 $`V ^ { A } ( x , \theta )`$ 构建一个规范不变的超对称作用量.
为了启发这个构造, 我们将首先考虑单个阿贝尔规范场(扔掉下标 $`A`$ )的情况, 然后在下一节回到一般情况.
在量子电动力学这样的阿贝尔规范场论中, 用 $`V _ { \mu } ( x )`$ 构造的规范不变场是熟悉的场强张量
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f818690d0ca47926c608f">
	$$
	f _ { \mu \nu } ( x ) = \partial _ { \mu } V _ { \nu } ( x ) - \partial _ { \nu } V _ { \mu } ( x ) . \tag{27.2.1}
	$$
</synced_block>
那么, $`f _ { \mu \nu } ( x )`$ 的超对称变换规则就由 $`V _ { \mu } ( x )`$ 的变换规则(26.2.15)给定为
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81859478efeae75f3cf4">
	$$
	\delta f _ { \mu \nu } = \Bigl ( \bar { \alpha } ( \partial _ { \mu } \gamma _ { \nu } - \partial _ { \nu } \gamma _ { \mu } ) \lambda \Bigr ) \ . \tag{27.2.2}
	$$
</synced_block>
方程(26.2.16)给出了 $`\lambda ( x )`$ ,的变换规则
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81629015e25bed8c2462">
	$$
	\begin{array} { r } { \delta \lambda = \Bigl ( - { \frac { 1 } { 4 } } f _ { \mu \nu } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] + \mathrm{i} \gamma _ { 5 } D \Bigr ) \alpha , } \end{array} \tag{27.2.3}
	$$
</synced_block>
而方程(26.2.17)给出了 $`D ( x )`$ 的变换规则:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81eaa49ede4186784e03">
	$$
	\delta D=\mathrm{i}(\bar\alpha\gamma_5\not\partial\lambda).\tag{27.2.4}
	$$
</synced_block>
其中没有一个依赖于超场 $`V ^ { A } ( x , \theta )`$ 是否被取在了Wess-Zumino 规范中.
我们看到场 $`f _ { \mu \nu } ( x )`$ , $`\lambda ( x )`$ 和 $`D ( x )`$ 构成了完备的超对称多重态.
给这个超多重态中的场构造一个合适的动能拉格朗日密度并不困难.
这些场的 Lorentz不变, 宇称守恒, 规范不变且量纲为 4 的函数只能是 $`f_{\mu\nu}f^{\mu\nu}`$, $`\bar\lambda\not\partial\lambda`$ 和 $`D^2`$.
通过取 $`f _ { \mu \nu } f ^ { \mu \nu }`$ 的系数为 $`- { \frac { 1 } { 4 } }`$ , 我们可以使 $`V ^ { \mu }`$ 是按习惯归一化的矢量场, 所以我们暂且可以将动能拉格朗日密度取成
$$
\mathcal L_{\mathrm{gauge}}=-\frac14 f_{\mu\nu}f^{\mu\nu}-c_\lambda(\bar\lambda\not\partial\lambda)-c_DD^2,
$$
其中系数 $`c_\lambda`$ 和 $`c_D`$ 由 $`\textstyle \int \mathcal L_{\mathrm{gauge}}\,\mathrm d^4x`$ 是超对称的这一条件决定.
利用方程(27.2.2)—(27.2.4), 无限小超对称变换对拉格朗日中的算符的改变是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81859478efeae75f3cf4">
		$$
		\delta f _ { \mu \nu } = \Bigl ( \bar { \alpha } ( \partial _ { \mu } \gamma _ { \nu } - \partial _ { \nu } \gamma _ { \mu } ) \lambda \Bigr ) \ . \tag{27.2.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81eaa49ede4186784e03">
		$$
		\delta D=\mathrm{i}(\bar\alpha\gamma_5\not\partial\lambda).\tag{27.2.4}
		$$
	</synced_block_reference>
</callout>
$$
\begin{array}{l}
\delta(f_{\mu\nu}f^{\mu\nu})=2f^{\mu\nu}\bigl(\bar\alpha(\gamma_\nu\partial_\mu-\gamma_\mu\partial_\nu)\lambda\bigr),\\
\delta(\bar\lambda\not\partial\lambda)=2\bigl(\bar\alpha[\frac14 f_{\mu\nu}[\gamma^\mu,\gamma^\nu]+\mathrm{i}\gamma_5D]\not\partial\lambda\bigr),\\
\delta D^2=2\mathrm{i}D(\bar\alpha\gamma_5\not\partial\lambda).
\end{array}
$$
其中我们扔掉了对作用量变分无贡献的导数项.
为了看到这些项是如何抵消的, 需要使用 $`\gamma`$ -矩阵的恒等式\\\*
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8198bb8cc4a6cadd48de">
	$$
	\left[ \gamma ^ { \mu } , \gamma ^ { \nu } \right] \gamma ^ { \rho } = - 2 \eta ^ { \mu \rho } \gamma ^ { \nu } + 2 \eta ^ { \nu \rho } \gamma ^ { \mu } - 2 \mathrm{i} \epsilon ^ { \mu \nu \rho \sigma } \gamma _ { \sigma } \gamma _ { 5 } . \tag{27.2.5}
	$$
</synced_block>
$`- \mathrm{i} \epsilon ^ { \mu \nu \rho \sigma } f _ { \mu \nu } ( \bar { \alpha } \gamma _ { \sigma } \gamma _ { 5 } \partial _ { \rho } \lambda )`$ 分部积分产生的贡献正比于 $`\epsilon ^ { \mu \nu \rho \sigma } \partial _ { \rho } f _ { \mu \nu }`$ , 这一项由于 $`f _ { \mu \nu }`$ 的形式(27.2.1)为零, 所以 $`- \mathrm{i} \epsilon ^ { \mu \nu \rho \sigma } f _ { \mu \nu } ( \bar { \alpha } \gamma _ { \sigma } \gamma _ { 5 } \partial _ { \rho } \lambda )`$ 这一项对 $`\int \mathrm { d } ^ { 4 } x \delta \mathcal{L}`$ 没有贡献.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f818690d0ca47926c608f">
		$$
		f _ { \mu \nu } ( x ) = \partial _ { \mu } V _ { \nu } ( x ) - \partial _ { \nu } V _ { \mu } ( x ) . \tag{27.2.1}
		$$
	</synced_block_reference>
</callout>
这样一来, 这个恒等式使得我们能够将 $`\lambda`$ -项的变分重写成
$$
\delta(\bar\lambda\not\partial\lambda)=-f^{\mu\nu}\bigl(\bar\alpha(\gamma_\nu\partial_\mu-\gamma_\mu\partial_\nu)\lambda\bigr)+2\mathrm{i}D(\bar\alpha\gamma_5\not\partial\lambda).
$$
抵消正比 $`f ^ { \mu \nu } \lambda`$ 的项要求 $`c _ { \lambda } = 1 / 2`$ , 而抵消正比于 $`D \lambda`$ 的项要求 $`c _ { D } = - c _ { \lambda }`$ , 所以超对称拉格朗日密度采取如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81b590ebdfbd4941313c">
	$$
	\mathcal L_{\mathrm{gauge}}=-\frac14 f_{\mu\nu}f^{\mu\nu}-\frac12(\bar\lambda\not\partial\lambda)+\frac12D^2.\tag{27.2.6}
	$$
</synced_block>
这表明, 在场 $`V ^ { \mu }`$ 正则归一化的情况下, 通过变换规则(27.2.2)和(27.2.3)与 $`V ^ { \mu }`$ 相关联的场 $`\lambda`$ 也是正则归一化的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81859478efeae75f3cf4">
		$$
		\delta f _ { \mu \nu } = \Bigl ( \bar { \alpha } ( \partial _ { \mu } \gamma _ { \nu } - \partial _ { \nu } \gamma _ { \mu } ) \lambda \Bigr ) \ . \tag{27.2.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81629015e25bed8c2462">
		$$
		\begin{array} { r } { \delta \lambda = \Bigl ( - { \frac { 1 } { 4 } } f _ { \mu \nu } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] + \mathrm{i} \gamma _ { 5 } D \Bigr ) \alpha , } \end{array} \tag{27.2.3}
		$$
	</synced_block_reference>
</callout>
另外, 阿贝尔规范理论还有一个可重整项, 称为 Fayet-Iliopoulous 项:\[2\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- P. Fayet and J Iliopoulos, Phys. Lett. 51B, 461 (1974). 这篇文章重印于 Supersymmetry, 参考文献\[1\]
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81fcb6d0c3edb7d1a098">
	$$
	\mathcal{L} _ { \mathrm{FI} } = \xi D , \tag{27.2.7}
	$$
</synced_block>
其中 $`\xi`$ 是任意常数.
通过方程(27.2.4)可以证明这一项在超对称变换下的变分是导数, 这使得它产生了作用量中另外一个超对称项.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81eaa49ede4186784e03">
		$$
		\delta D=\mathrm{i}(\bar\alpha\gamma_5\not\partial\lambda).\tag{27.2.4}
		$$
	</synced_block_reference>
</callout>
正如我们将在 27.5 节看到的, 这种项的出现为超对称的自发破缺提供了一个机制.
哪类超场是以 $`f _ { \mu \nu }`$ , $`\lambda`$ 和 $`D`$ 为分量场, 提这个问题是有益的, 这一方面是因为是其自身, 另一方面是它可以作为工具来构建包含这些场的超对称相互作用.
有些出人意料的是, 结果是旋量超场 $`W _ { \alpha } ( x )`$ , 它的分量场(在方程(26.2.10)的符号约定下)是
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8100a0face58aa747880">
	$$
	\begin{array}{rl}
C_{(\alpha)}(x)&=\lambda_\alpha(x),\\
\omega_{(\alpha)\beta}(x)&=\frac{\mathrm{i}}2(\gamma^\mu\gamma^\nu\epsilon)_{\alpha\beta}f_{\mu\nu}(x)+(\gamma_5\epsilon)_{\alpha\beta}D(x),\\
V_{(\alpha)\mu}(x)&=-\mathrm{i}\partial_\mu(\gamma_5\lambda(x))_\alpha,\\
M_{(\alpha)}(x)&=-\mathrm{i}(\not\partial\gamma_5\lambda(x))_\alpha,
\qquad N_{(\alpha)}(x)=-(\not\partial\lambda(x))_\alpha,\\
\lambda_{(\alpha)\beta}(x)&=D_{(\alpha)}(x)=0.
\end{array}\tag{27.2.8}
	$$
</synced_block>
(把这些分量场的下标 $`\alpha`$ 放在括号里面是为了强调它标记的是整个超场.) 可以直接用方程(27.2.2)(27.2.4)验证方程(27.2.8)给出的超场分量确实像方程(26.2.11)—(26.2.17)那样中变换.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81859478efeae75f3cf4">
		$$
		\delta f _ { \mu \nu } = \Bigl ( \bar { \alpha } ( \partial _ { \mu } \gamma _ { \nu } - \partial _ { \nu } \gamma _ { \mu } ) \lambda \Bigr ) \ . \tag{27.2.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81eaa49ede4186784e03">
		$$
		\delta D=\mathrm{i}(\bar\alpha\gamma_5\not\partial\lambda).\tag{27.2.4}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8100a0face58aa747880">
		$$
		\begin{array}{rl}
C_{(\alpha)}(x)&=\lambda_\alpha(x),\\
\omega_{(\alpha)\beta}(x)&=\frac{\mathrm{i}}2(\gamma^\mu\gamma^\nu\epsilon)_{\alpha\beta}f_{\mu\nu}(x)+(\gamma_5\epsilon)_{\alpha\beta}D(x),\\
V_{(\alpha)\mu}(x)&=-\mathrm{i}\partial_\mu(\gamma_5\lambda(x))_\alpha,\\
M_{(\alpha)}(x)&=-\mathrm{i}(\not\partial\gamma_5\lambda(x))_\alpha,
\qquad N_{(\alpha)}(x)=-(\not\partial\lambda(x))_\alpha,\\
\lambda_{(\alpha)\beta}(x)&=D_{(\alpha)}(x)=0.
\end{array}\tag{27.2.8}
		$$
	</synced_block_reference>
</callout>
将分量场(27.2.8)代入方程(26.2.10)并使用方程(26.A.5), 我们发现超场 $`W _ { \alpha }`$ 采取如下的形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8100a0face58aa747880">
		$$
		\begin{array}{rl}
C_{(\alpha)}(x)&=\lambda_\alpha(x),\\
\omega_{(\alpha)\beta}(x)&=\frac{\mathrm{i}}2(\gamma^\mu\gamma^\nu\epsilon)_{\alpha\beta}f_{\mu\nu}(x)+(\gamma_5\epsilon)_{\alpha\beta}D(x),\\
V_{(\alpha)\mu}(x)&=-\mathrm{i}\partial_\mu(\gamma_5\lambda(x))_\alpha,\\
M_{(\alpha)}(x)&=-\mathrm{i}(\not\partial\gamma_5\lambda(x))_\alpha,
\qquad N_{(\alpha)}(x)=-(\not\partial\lambda(x))_\alpha,\\
\lambda_{(\alpha)\beta}(x)&=D_{(\alpha)}(x)=0.
\end{array}\tag{27.2.8}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
W_\alpha(x,\theta)=\Bigl[&\lambda(x)+\frac12\gamma^\mu\gamma^\nu\theta f_{\mu\nu}(x)-\mathrm{i}\gamma_5\theta D(x)-\frac12(\theta^{\mathrm T}\epsilon\theta)\not\partial\gamma_5\lambda(x)\\
&+\frac12(\theta^{\mathrm T}\epsilon\gamma_5\theta)\not\partial\lambda(x)+\frac12(\theta^{\mathrm T}\epsilon\gamma^\mu\theta)\gamma_5\partial_\mu\lambda(x)\\
&-\frac14(\theta^{\mathrm T}\epsilon\theta)\gamma_5\gamma^\mu\gamma^\nu\gamma^\sigma\theta\partial_\sigma f_{\mu\nu}(x)
+\frac{\mathrm{i}}2(\theta^{\mathrm T}\epsilon\theta)\gamma^\sigma\theta\partial_\sigma D(x)\\
&-\frac18(\theta^{\mathrm T}\epsilon\theta)^2\Box\lambda(x)\Bigr]_\alpha.\tag{27.2.9}
\end{aligned}
$$
就像我们在 26.3节证明过的, 像这样没有 $`\lambda`$ -分量和 $`D`$ -分量的超场是手征的——即, 它是左手征超场和右手征超场的和
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8112b9fac173c3276e95">
	$$
	W ( x , \theta ) = W _ { L } ( x , \theta ) + W _ { R } ( x , \theta ) . \tag{27.2.10}
	$$
</synced_block>
这里的左手征超场和右手征超场分别是 $`W`$ 在 $`\gamma _ { 5 } = + 1`$ 的超空间和在 $`\gamma _ { 5 } = - 1`$ 的超空间上的投影:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8107b076d6cec06d14ee">
	$$
	\begin{array} { r l } & { W _ { L } ( x , \theta ) = \frac { 1 } { 2 } ( 1 + \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { L } ( x _ { + } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { L } f _ { \mu \nu } ( x _ { + } ) + \left( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \right) \partial \lambda _ { R } ( x _ { + } ) - \mathrm{i} \theta _ { L } D ( x _ { + } ) , } \\ & { W _ { R } ( x , \theta ) = \frac { 1 } { 2 } ( 1 - \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { R } ( x _ { - } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { R } f _ { \mu \nu } ( x _ { - } ) - \left( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \right) \partial \lambda _ { L } ( x _ { - } ) - \mathrm{i} \theta _ { R } D ( x _ { - } ) , } \end{array} \tag{27.2.11-27.2.12}
	$$
</synced_block>
其中 $`x _ { \pm } ^ { \mu }`$ 由方程(26.3.23)给出.
正如我们在26.3节看到的, 我们可以用一个左手征超场的任意函数的 $`\mathcal{F}`$ -项和它的厄米共轭来构建合适的拉格朗日密度.
左手征超场(27.2.11)的最简单标量函数是 $`W_L^{\mathrm T}\epsilon W_L`$.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8107b076d6cec06d14ee">
		$$
		\begin{array} { r l } & { W _ { L } ( x , \theta ) = \frac { 1 } { 2 } ( 1 + \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { L } ( x _ { + } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { L } f _ { \mu \nu } ( x _ { + } ) + \left( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \right) \partial \lambda _ { R } ( x _ { + } ) - \mathrm{i} \theta _ { L } D ( x _ { + } ) , } \\ & { W _ { R } ( x , \theta ) = \frac { 1 } { 2 } ( 1 - \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { R } ( x _ { - } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { R } f _ { \mu \nu } ( x _ { - } ) - \left( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \right) \partial \lambda _ { L } ( x _ { - } ) - \mathrm{i} \theta _ { R } D ( x _ { - } ) , } \end{array} \tag{27.2.11-27.2.12}
		$$
	</synced_block_reference>
</callout>
为了计算 $`\mathcal F`$-项, 我们注意到, 当表示成 $`\theta_L`$ 和 $`x_+`$ 的函数时, $`W_L^{\mathrm T}\epsilon W_L`$ 中 $`\theta_L`$ 的二阶项是
$$
\begin{aligned}
-[W_L^{\mathrm T}\epsilon W_L]_{\theta_L^2}
&=(\theta_L^{\mathrm T}\epsilon\theta_L)\left[-2(\lambda_L^{\mathrm T}(x)\epsilon\not\partial\lambda_R(x))+D^2(x)\right]\\
&\quad+\frac1{16}\bigl(\bar\theta_L[\gamma^\mu,\gamma^\nu][\gamma^\rho,\gamma^\sigma]\theta_L\bigr)f_{\mu\nu}(x)f_{\rho\sigma}(x).
\end{aligned}
$$
(场变量取成了 $`x ^ { \mu }`$ 而不是 $`x _ { + } ^ { \mu }`$ 是因为差产生的项至少包含 3 个 $`\theta _ { L }`$ 的因子, 因此为零.) $`\left( \bar { s } [ \gamma _ { \mu } , \gamma _ { \nu } ] s \right)`$ 和$`( \bar { s } [ \gamma _ { \mu } , \gamma _ { \nu } ] \gamma _ { 5 } s )`$ 对于任何 Majorana 旋量 $`s`$ 都为零这个性质, 再加上 Lorentz不变性告诉我们, 双线性型 $`( \overline { { { \theta _ { L } } } } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] [ \gamma ^ { \rho } , \gamma ^ { \sigma } ] ) \theta _ { L }`$ 必须正比于 $`( \overline { { { \theta _ { L } } } } \theta _ { L } ) ( \eta ^ { \mu \rho } \eta ^ { \nu \sigma } - \eta ^ { \mu \sigma } \eta ^ { \nu \rho } )`$ 和 $`( \overline { { { \theta _ { L } } } } \theta _ { L } ) \epsilon ^ { \mu \nu \rho \sigma }`$ 的线性组合.
通过给 $`\mu \nu \rho \sigma`$ 赋值1212或1230, 我们可以找到系数, 并且以这种方式, 我们发现
$$
\left( \overline { { { \theta _ { L } } } } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] [ \gamma ^ { \rho } , \gamma ^ { \sigma } ] \theta _ { L } \right) = 4 \left( \overline { { { \theta _ { L } } } } \theta _ { L } \right) \left[ - \eta ^ { \mu \rho } \eta ^ { \nu \sigma } + \eta ^ { \mu \sigma } \eta ^ { \nu \rho } + \mathrm{i} \epsilon ^ { \mu \nu \rho \sigma } \right] .
$$
$`\mathcal{F}`$ -项是 $`( \overline { { \theta _ { L } } } \theta _ { L } )`$ 的系数, 所以
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f817fb6c9d22e2797d50e">
	$$
	-[W_L^{\mathrm T}\epsilon W_L]_{\mathcal F}=-2(\bar\lambda_R\not\partial\lambda_R)-\frac12f_{\mu\nu}f^{\mu\nu}+\frac{\mathrm{i}}4\epsilon^{\mu\nu\rho\sigma}f_{\mu\nu}f_{\rho\sigma}+D^2.\tag{27.2.13}
	$$
</synced_block>
方程(26.A.1)表明 $`(\bar\lambda\not\partial\lambda)`$ 是实的, 而 $`(\bar\lambda\not\partial\gamma_5\lambda)`$ 是虚的, 所以方程(27.2.13)给出了规范场和规范微子场的拉格朗日量(27.2.6).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f817fb6c9d22e2797d50e">
		$$
		-[W_L^{\mathrm T}\epsilon W_L]_{\mathcal F}=-2(\bar\lambda_R\not\partial\lambda_R)-\frac12f_{\mu\nu}f^{\mu\nu}+\frac{\mathrm{i}}4\epsilon^{\mu\nu\rho\sigma}f_{\mu\nu}f_{\rho\sigma}+D^2.\tag{27.2.13}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81b590ebdfbd4941313c">
		$$
		\mathcal L_{\mathrm{gauge}}=-\frac14 f_{\mu\nu}f^{\mu\nu}-\frac12(\bar\lambda\not\partial\lambda)+\frac12D^2.\tag{27.2.6}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81f996e3dab4b948b18e">
	$$
	-\frac12\operatorname{Re}[W_L^{\mathrm T}\epsilon W_L]_{\mathcal F}=-\frac12(\bar\lambda\not\partial\lambda)-\frac14f_{\mu\nu}f^{\mu\nu}+\frac12D^2.\tag{27.2.14}
	$$
</synced_block>
在下一节, 虚部的物理意义会在更普遍的背景下进行讨论.
推导旋量超场的形式有另一种方法, 而这个方法在非阿贝尔规范理论中推导规范超场的分量时提供了一个更加方便的方法.
一个繁琐但直接的计算表明规范不变超场(27.2.9)可以用规范超场(27.1.16)表示成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81f387aadeed15593619">
		$$
		\begin{array}{l}
V^A(x,\theta)=C^A(x)-\mathrm{i}(\bar\theta\gamma_5\omega^A(x))-\frac{\mathrm{i}}2(\bar\theta\gamma_5\theta)M^A(x)-\frac12(\bar\theta\theta)N^A(x)\\
\qquad+\frac{\mathrm{i}}2(\bar\theta\gamma_5\gamma^\mu\theta)V_\mu{}^A(x)-\mathrm{i}(\bar\theta\gamma_5\theta)\left(\bar\theta\left[\lambda^A(x)+\frac12\not\partial\omega^A(x)\right]\right)\\
\qquad-\frac14(\bar\theta\gamma_5\theta)^2\left(D^A(x)+\frac12\Box C^A(x)\right).
\end{array}\tag{27.1.16}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814493b2fcfed4e962ef">
	$$
	W _ { \alpha } ( x , \theta ) = \frac { \mathrm{i} } { 4 } \Big ( \mathcal{D} ^ { \mathrm { T } } \epsilon \mathcal{D} \Big ) \mathcal{D} _ { \alpha } V ( x , \theta ) , \tag{27.2.15}
	$$
</synced_block>
其中 $`{ \mathcal{D} } _ { \alpha }`$ 是方程(26.2.26)中引入的超导数:
$$
\mathcal{D} _ { \alpha } \equiv ( \gamma _ { 5 } \epsilon ) _ { \alpha \beta } \frac { \partial } { \partial \theta _ { \beta } } - ( \gamma ^ { \mu } \theta ) _ { \alpha } \frac { \partial } { \partial x ^ { \mu } } = - \frac { \partial } { \partial \bar { \theta } _ { \alpha } } - ( \gamma ^ { \mu } \theta ) _ { \alpha } \frac { \partial } { \partial x ^ { \mu } } .
$$
得到这个结果(除了归一化因子)的一个方法是注意到函数(27.2.15)拥有称为规范不变手征旋量超场的所需性质.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814493b2fcfed4e962ef">
		$$
		W _ { \alpha } ( x , \theta ) = \frac { \mathrm{i} } { 4 } \Big ( \mathcal{D} ^ { \mathrm { T } } \epsilon \mathcal{D} \Big ) \mathcal{D} _ { \alpha } V ( x , \theta ) , \tag{27.2.15}
		$$
	</synced_block_reference>
</callout>
首先, 注意到方程(27.2.15)是一个超场, 这是因为它是通过用超导数作用在超场 $`V`$ 上形成的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814493b2fcfed4e962ef">
		$$
		W _ { \alpha } ( x , \theta ) = \frac { \mathrm{i} } { 4 } \Big ( \mathcal{D} ^ { \mathrm { T } } \epsilon \mathcal{D} \Big ) \mathcal{D} _ { \alpha } V ( x , \theta ) , \tag{27.2.15}
		$$
	</synced_block_reference>
</callout>
另外, 从 $`\mathcal{D}`$ 的反对易可以得出任意三个或多个 $`\mathcal{D} _ { L }`$ 的乘积或者任意三个或多个 $`\mathcal{D} _ { R }`$ 的乘积为零, 这使得
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81dd8ea5dddb8f025b22">
	$$
	(\mathcal D^{\mathrm T}\epsilon\mathcal D)\mathcal D=(\mathcal D_L^{\mathrm T}\epsilon\mathcal D_L)\mathcal D_R+(\mathcal D_R^{\mathrm T}\epsilon\mathcal D_R)\mathcal D_L.\tag{27.2.16}
	$$
</synced_block>
因为 $`\mathcal D _ { L } ( \mathcal D _ { L } ^ { \mathrm { T } } \epsilon \mathcal D _ { L } ) = \mathcal D _ { R } ( \mathcal D _ { R } ^ { \mathrm { T } } \epsilon \mathcal D _ { R } ) = 0`$ , 超场(27.2.15)是手征的, 且有
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814493b2fcfed4e962ef">
		$$
		W _ { \alpha } ( x , \theta ) = \frac { \mathrm{i} } { 4 } \Big ( \mathcal{D} ^ { \mathrm { T } } \epsilon \mathcal{D} \Big ) \mathcal{D} _ { \alpha } V ( x , \theta ) , \tag{27.2.15}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814698f5d9207df466f4">
	$$
	W_{L\alpha}(x,\theta)=\frac{\mathrm{i}}4(\mathcal D_R^{\mathrm T}\epsilon\mathcal D_R)\mathcal D_{L\alpha}V(x,\theta),\qquad
W_{R\alpha}(x,\theta)=\frac{\mathrm{i}}4(\mathcal D_L^{\mathrm T}\epsilon\mathcal D_L)\mathcal D_{R\alpha}V(x,\theta).\tag{27.2.17}
	$$
</synced_block>
最后, 我们可以证明(27.2.15)在推广的规范变换(27.1.13)下不变, 对于单个阿贝尔规范场, 这个规范变换就是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814493b2fcfed4e962ef">
		$$
		W _ { \alpha } ( x , \theta ) = \frac { \mathrm{i} } { 4 } \Big ( \mathcal{D} ^ { \mathrm { T } } \epsilon \mathcal{D} \Big ) \mathcal{D} _ { \alpha } V ( x , \theta ) , \tag{27.2.15}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81e2aaf6fb19a10c5a0b">
		$$
		V^A(x,\theta)\to V^A(x,\theta)+\frac{\mathrm{i}}{2}\bigl[\Omega^A(x,\theta)-\Omega^A(x,\theta)^*\bigr]+\cdots.\tag{27.1.13}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f81daaac0d2a6f8a9f629">
	$$
	V(x,\theta)\to V(x,\theta)+\frac{\mathrm{i}}2[\Omega(x,\theta)-\Omega^*(x,\theta)].\tag{27.2.18}
	$$
</synced_block>
其中 $`\Omega ( x , \theta )`$ 是一个任意的左手征超场.
由于 $`\mathcal{D} _ { L } \Omega ^ { * } = 0`$ , $`W _ { L \alpha }`$ 的变化正比于 $`( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } ) \mathcal{D} _ { L \alpha } \Omega`$ .
但是 $`\mathcal{D} _ { R } \Omega = 0`$ 且
$$
\bigl[(\mathcal D_R^{\mathrm T}\epsilon\mathcal D_R),\mathcal D_{L\alpha}\bigr]=-2\bigl[(1+\gamma_5)\not\partial\mathcal D_R\bigr]_\alpha,
$$
所以 $`W _ { L \alpha }`$ 的变化为零.
类似的讨论表明 $`W _ { R \alpha }`$ 也是规范不变的.
(通过使用这一规范不变性质将$`V ( x , \theta )`$ 变到 Wess-Zumino 规范下, 验证方程(27.2.15)的工作量被极大地简化.)
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814493b2fcfed4e962ef">
		$$
		W _ { \alpha } ( x , \theta ) = \frac { \mathrm{i} } { 4 } \Big ( \mathcal{D} ^ { \mathrm { T } } \epsilon \mathcal{D} \Big ) \mathcal{D} _ { \alpha } V ( x , \theta ) , \tag{27.2.15}
		$$
	</synced_block_reference>
</callout>
手征超场(27.2.11)和(27.2.12)显然不是左手征超场和右手征超场的最一般形式.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8107b076d6cec06d14ee">
		$$
		\begin{array} { r l } & { W _ { L } ( x , \theta ) = \frac { 1 } { 2 } ( 1 + \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { L } ( x _ { + } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { L } f _ { \mu \nu } ( x _ { + } ) + \left( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \right) \partial \lambda _ { R } ( x _ { + } ) - \mathrm{i} \theta _ { L } D ( x _ { + } ) , } \\ & { W _ { R } ( x , \theta ) = \frac { 1 } { 2 } ( 1 - \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { R } ( x _ { - } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { R } f _ { \mu \nu } ( x _ { - } ) - \left( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \right) \partial \lambda _ { L } ( x _ { - } ) - \mathrm{i} \theta _ { R } D ( x _ { - } ) , } \end{array} \tag{27.2.11-27.2.12}
		$$
	</synced_block_reference>
</callout>
为了把这些超场满足的约束变成明显超对称的形式, 我们通过使用反对易关系(26.2.30)注意到
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f815196fcdde6956d8511">
	$$
	\begin{array} { r l } & { \epsilon _ { \alpha \beta } \mathcal{D} _ { L \alpha } \Big ( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } \Big ) \mathcal{D} _ { L \beta } = - 2 \mathcal{D} _ { R \alpha } \mathcal{D} _ { L \beta } \Big ( \epsilon ( 1 + \gamma _ { 5 } ) \frac { \partial } { \partial t } \Big ) _ { \beta \alpha } + \Big ( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } \Big ) \Big ( \mathcal{D} _ { L } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { L } \Big ) } \\ & { \quad \quad \quad \quad = \epsilon _ { \alpha \beta } \mathcal{D} _ { R \alpha } \Big ( \mathcal{D} _ { L } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { L } \Big ) \mathcal{D} _ { R \beta } ~ . } \end{array} \tag{27.2.19}
	$$
</synced_block>
那么从方程(27.2.17)得出 $`W _ { L }`$ 和 $`W _ { R }`$ 通过如下的约束相关联:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f814698f5d9207df466f4">
		$$
		W_{L\alpha}(x,\theta)=\frac{\mathrm{i}}4(\mathcal D_R^{\mathrm T}\epsilon\mathcal D_R)\mathcal D_{L\alpha}V(x,\theta),\qquad
W_{R\alpha}(x,\theta)=\frac{\mathrm{i}}4(\mathcal D_L^{\mathrm T}\epsilon\mathcal D_L)\mathcal D_{R\alpha}V(x,\theta).\tag{27.2.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f810b8ddfe083aa93bebe">
	$$
	\epsilon _ { \alpha \beta } { \mathcal D } _ { L \alpha } W _ { L \beta } = \epsilon _ { \alpha \beta } { \mathcal D } _ { R \alpha } W _ { R \beta } . \tag{27.2.20}
	$$
</synced_block>
可以直接证明满足方程(27.2.20)的最一般手征旋量超场是(27.2.11)和(27.2.12)的形式, 且其中的$`f _ { \mu \nu }`$ 满足 “Bianchi” 恒等式 $`\epsilon ^ { \mu \nu \rho \sigma } \partial _ { \rho } f _ { \mu \nu } = 0`$ 的约束.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f810b8ddfe083aa93bebe">
		$$
		\epsilon _ { \alpha \beta } { \mathcal D } _ { L \alpha } W _ { L \beta } = \epsilon _ { \alpha \beta } { \mathcal D } _ { R \alpha } W _ { R \beta } . \tag{27.2.20}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172#34cee2b74b3f8107b076d6cec06d14ee">
		$$
		\begin{array} { r l } & { W _ { L } ( x , \theta ) = \frac { 1 } { 2 } ( 1 + \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { L } ( x _ { + } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { L } f _ { \mu \nu } ( x _ { + } ) + \left( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \right) \partial \lambda _ { R } ( x _ { + } ) - \mathrm{i} \theta _ { L } D ( x _ { + } ) , } \\ & { W _ { R } ( x , \theta ) = \frac { 1 } { 2 } ( 1 - \gamma _ { 5 } ) W ( x , \theta ) } \\ & { \qquad = \lambda _ { R } ( x _ { - } ) + \frac { 1 } { 2 } \gamma ^ { \mu } \gamma ^ { \nu } \theta _ { R } f _ { \mu \nu } ( x _ { - } ) - \left( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \right) \partial \lambda _ { L } ( x _ { - } ) - \mathrm{i} \theta _ { R } D ( x _ { - } ) , } \end{array} \tag{27.2.11-27.2.12}
		$$
	</synced_block_reference>
</callout>
</content>
</page>
