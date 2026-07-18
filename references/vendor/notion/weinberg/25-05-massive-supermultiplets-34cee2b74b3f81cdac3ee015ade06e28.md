Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81cdac3ee015ade06e28 as of 2026-07-17T04:03:50.432Z:
<page url="https://app.notion.com/p/34cee2b74b3f81cdac3ee015ade06e28">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f815fb0b0e5db189e0b88" title="第 25 章 超对称代数"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"25.5 有质量粒子的超多重态"}
</properties>
<content>
尽管已知的夸克, 轻子和规范玻色子和它们的超对称伴在超对称破缺可以被忽视的能标处可以被视为是无质量的, 但对于其它粒子, 包括统一强相互作用和电弱相互作用的理论要求的质量很大的额外规范玻色子, 这不一定是成立的.
<details>
<summary>Typed Weinberg dictionary — Srednicki spinor-index grammar（no field mapping）</summary>
	本 fold 只恢复 massive-supermultiplet/BPS formulas 的 spinor type。Clebsch-Gordan arguments 中的 a,b=±1/2 仍是 numerical weights；r,s,... 仍是 Weinberg internal labels。
	$$
	\mathcal Q^{\dot a}{}_{r}:=\mathcal Q^{W,\rm src}_{ar},\qquad (\mathcal Q^\dagger)^a{}_{r}:=\mathcal Q^{W,\rm src\,*}_{ar}.
	$$
	$$
	a=\operatorname{wt}(\dot a),\qquad \mathcal Q^{\dot\pm}:=\mathcal Q^{\dot a}\big|_{a=\pm1/2},\qquad (\mathcal Q^\dagger)^\pm:=(\mathcal Q^\dagger)^a\big|_{a=\pm1/2}.
	$$
	$$
	\mathcal B^{\dot a}{}_{r}:=\mathcal Q^{\dot a}{}_{r}-(e_W)^{\dot a}{}_{b}U_r{}^s(\mathcal Q^\dagger)^b{}_{s}.
	$$
</details>
另外, 自Wess-Zumino模型起, 对于研究超对称理论,有质量粒子的理论就已经是个很有用的测试情况.
因此对我们来说, 简要地考察未破缺超对称对有质量粒子的意义将是值得的.
就像在上一节, 通过用算符 $`\mathcal{Q} _ { a r }`$ 和 $`{ \mathcal{Q} } _ { a r } ^ { * }`$ 作用超多重态中的任何一个单粒子态, 我们获得了超多重态中的各种单粒子态, 并且所有这些态有相同的 4 -动量.
不同于零质量的情况, 当质量 $`M \ >`$ 0 时, 我们现在可以取静止粒子的 4 -动量, 其中 $`i = { 1 , 2 , 3 }`$ 的 $`p ^ { i } = 0`$ 且 $`p ^ { 0 } = M`$ .
在这个参考系下,我们有
$$
\sigma _ { \mu } p ^ { \mu } = M \sigma _ { 0 } = M \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) ~ . \tag{25.5.1}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			(\sigma_{W,\mu})^{\dot a b}p^\mu
=M(\sigma_{W,0})^{\dot a b}
=M\begin{pmatrix}1&0\\0&1\end{pmatrix}^{\dot a b}.
	$$
</callout>
因此, 作用在有这一 4 -动量的超多重态中的任何态 $`| \ \rangle`$ 上, 反对易关系(25.2.7)给出
$$
\{ \mathcal{Q} _ { a r } , \mathcal{Q} _ { b s } ^ { * } \} | \rangle = 2 M \delta _ { a b } \delta _ { r s } | \rangle . \tag{25.5.2}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\{\mathcal Q^{\dot a}{}_{r},(\mathcal Q^\dagger)^b{}_{s}\}|\,\rangle
=2M(\sigma_{W,0})^{\dot a b}\delta_{rs}|\,\rangle.
	$$
</callout>
与零质量的情况相反, 这里没有哪个 $`\mathcal{Q} _ { a r }`$ 或 $`{ \mathcal{Q} } _ { a r } ^ { * }`$ 的分量可以在整个多重态上为零, 所以我们有两组上升和下降算符: $`\mathcal{Q} _ { ( 1 / 2 ) r }`$ 和 $`\mathcal{Q} _ { ( - 1 / 2 ) r } ^ { * }`$ 均将自旋 3 -分量降低 $`1 / 2`$ , 而 $`\mathcal{Q} _ { ( - 1 / 2 ) r }`$ 和 $`{ \mathcal{Q} } _ { ( 1 / 2 ) r } ^ { * }`$ 均将自旋 3 -分量提高 $`1 / 2`$ .
然而, 我们将会看到, 对于扩充超对称性, $`Q`$ 和 $`Q ^ { * }`$ 的特定线性组合有可能为零.
我们将首先考察简单超对称的情况.
通过使用超对称代数(25.2.31)和(25.2.32), 我们将证明一般的有质量超多重态由一个自旋 $`j + 1 / 2`$ 的粒子, 一对自旋 $`j`$ 的粒子和一个自旋 $`j - 1 / 2`$ 的粒子构成.
当宇称守恒时, 自旋为 $`j \pm 1 / 2`$ 的两个粒子拥有相同的内禀宇称, 由某个相位 $`\eta`$ 给定, 而两个自旋 $`j`$ 的粒子分别有宇称 $`+ \mathrm{i} \eta`$ 和−iη.
这里的 $`j`$ 是大于零的整数或半整数.
同时还存在坍缩超多重态,它由两个自旋零的粒子一个自旋 $`1 / 2`$ 的粒子构成.
当宇称守恒时, 自旋零的粒子有宇称 $`\mathrm{i} \eta`$ 和 $`- \mathrm{i} \eta`$ ,其中 $`\eta`$ 是自旋 $`1 / 2`$ 粒子的宇称.
下面是证明.
我们首先证明任何超多重态将包含至少一个自旋多重态 $`| j , \sigma \rangle`$ , 其中自旋3 -分量 $`\sigma`$ 以一为步长从 $`- j`$ 取到 $`+ j`$ , 它有特殊性质, 对于所有这样的 $`\sigma`$ 和 $`a = \pm 1 / 2`$ ,
$$
\mathcal{Q} _ { a } | j , \sigma \rangle = 0 . \tag{25.5.3}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\mathcal Q^{\dot a}|j,\sigma\rangle=0,
\qquad a=\operatorname{wt}(\dot a)=\pm\frac12.
	$$
</callout>
从这个超多重态中的任何非零态 $`| \psi \rangle`$ 出发, 我们可以定义非零态
$$
| \psi ^ { \prime } \rangle \equiv \left\{ \begin{array} { l l } { { ( 2 M ) ^ { - 1 / 2 } \mathcal{Q} _ { 1 / 2 } | \psi \rangle } } & { { \qquad \mathcal{Q} _ { 1 / 2 } | \psi \rangle \ne 0 } } \\ { { | \psi \rangle } } & { { \qquad \mathcal{Q} _ { 1 / 2 } | \psi \rangle = 0 } } \end{array} \right. ,
$$
和
$$
| \psi ^ { \prime \prime } \rangle \equiv \left\{ \begin{array} { l l } { { ( 2 M ) ^ { - 1 / 2 } \mathcal{Q} _ { - 1 / 2 } | \psi ^ { \prime } \rangle } } & { { \qquad \mathcal{Q} _ { - 1 / 2 } | \psi ^ { \prime } \rangle \neq 0 } } \\ { { | \psi ^ { \prime } \rangle } } & { { \qquad \mathcal{Q} _ { - 1 / 2 } | \psi ^ { \prime } \rangle = 0 } } \end{array} \right. .
$$
由于 $`\mathcal{Q} _ { a }`$ 反对易, $`\mathcal{Q} _ { 1 / 2 } | \psi ^ { \prime } \rangle = 0`$ , 因此对于 $`a \ = \ \pm 1 / 2`$ 有 $`\mathcal{Q} _ { a } | \psi ^ { \prime \prime } \rangle ~ = ~ 0 ~`$ .
如果任何态 $`| \psi ^ { \prime \prime } \rangle`$ 满足条件 $`\mathcal{Q} _ { a } \vert \psi ^ { \prime \prime } = 0`$ , 那么对于表示任意空间旋转的幺正表示 $`U ( R )`$ , $`U ( R ) | \psi ^ { \prime \prime } \rangle`$ 也满足这个条件.
由此得出满足这个条件态可以被分解进完整的自旋多重态 $`| j , \sigma \rangle`$ , 它满足条件(25.5.3)
现在集中在任何一个满足方程(25.5.3)的自旋多重态上, 对它进行归一化使得
$$
\langle j , \sigma ^ { \prime } | j , \sigma \rangle = \delta _ { \sigma ^ { \prime } \sigma } . \tag{25.5.4}
$$
当 $`j > 0`$ 时, 通过用自旋 $`1 / 2`$ 算符\* $`{ \mathcal{Q} } _ { a } ^ { * }`$ 作用这些态, 我们可以构造出自旋 $`j \pm 1 / 2`$ 的态:
<callout color="gray_bg">
	Footnote: The component $`\mathcal Q_a`$ transforms like a field annihilating a spin-$`1/2`$ particle with spin component $`a`$; its Hermitian conjugate transforms like the corresponding creation operator and hence like the particle state itself.
</callout>
$$
| j \pm 1 / 2 , \sigma \rangle = \frac { 1 } { \sqrt { 2 M } } C _ { \frac { 1 } { 2 } j } \Bigl ( j \pm 1 / 2 , \sigma ; a , \sigma - a \Bigr ) \mathcal{Q} _ { a } ^ { * } | j , \sigma - a \rangle , \tag{25.5.5}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			|j\!\pm\!\tfrac12,\sigma\rangle
=\frac1{\sqrt{2M}}C_{\frac12j}(j\!\pm\!\tfrac12,\sigma;a,\sigma-a)
(\mathcal Q^\dagger)^a|j,\sigma-a\rangle.
	$$
</callout>
其中 $`C _ { j j ^ { \prime } } ( j ^ { \prime \prime } , \sigma ^ { \prime \prime } ; \sigma , \sigma ^ { \prime } )`$ 是传统的 Clebsch-Gordan 系数, 它将 3 -分量为 $`\sigma`$ 和 $`\sigma ^ { \prime }`$ 的自旋 $`j`$ 和 $`j ^ { \prime \prime }`$ 耦合成3 -分量为 $`\sigma ^ { \prime \prime }`$ 的自旋 $`j ^ { \prime \prime }`$ .
利用方程(25.5.2)—(25.5.5)和 Clebsch-Gordan 系数的正交性, 我们可以证明这些态的归一化是正确的:
$$
\langle j \pm 1 / 2 , \sigma | j \pm 1 / 2 , \sigma ^ { \prime } \rangle = \delta _ { \sigma \sigma ^ { \prime } } , \qquad \langle j \pm 1 / 2 , \sigma | j \mp 1 / 2 , \sigma ^ { \prime } \rangle = 0 , \tag{25.5.6}
$$
所以态 $`| j \pm 1 / 2 , \sigma \rangle`$ 中的任何一个都不能为零.
唯一的例外是 $`j = 0`$ , 这时显然是由于不存在态 $`| j -`$ $`1 / 2 , \sigma \rangle`$ .
我们也可以通过作用两个 $`\mathcal{Q} ^ { \ast }`$ 在 $`| j , \sigma \rangle`$ 上获得其它态.
由于每个 $`{ \mathcal{Q} } _ { a } ^ { * }`$ 与它自身反对易, 唯一这样的非零态是通过作用算符 $`\mathcal{Q} _ { 1 / 2 } ^ { * } \mathcal{Q} _ { - 1 / 2 } ^ { * } = - \mathcal{Q} _ { - 1 / 2 } ^ { * } \mathcal{Q} _ { 1 / 2 } ^ { * }`$ 形成的.
这个算符可以写成 $`\frac { 1 } { 2 } e _ { a b } \mathcal{Q} _ { a } ^ { * } \mathcal{Q} _ { b } ^ { * }`$ ,这表明它是一个旋转不变量, 所以这给出了第二个自旋为 $`j`$ 的自旋多重态:
$$
| j , \sigma \rangle ^ { \flat } = \frac { 1 } { 2 M } \mathcal{Q} _ { \frac { 1 } { 2 } } ^ { * } \mathcal{Q} _ { - \frac { 1 } { 2 } } ^ { * } | j , \sigma \rangle , \tag{25.5.7}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			|j,\sigma\rangle^\flat
=\frac1{2M}(\mathcal Q^\dagger)^+(\mathcal Q^\dagger)^-|j,\sigma\rangle.
	$$
</callout>
它与 $`| j , \sigma \rangle`$ 不同是因为, 取代方程(25.5.3), 我们有
$$
\mathcal{Q} _ { a } ^ { * } | j , \sigma \rangle ^ { \flat } = 0 . \tag{25.5.8}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
	(\mathcal Q^\dagger)^a|j,\sigma\rangle^\flat=0.
	$$
</callout>
再次使用方程(25.5.2)—(25.5.4), 我们发现它们也是归一化态:
$$
{} ^ { \flat } \langle j , \sigma ^ { \prime } | j , \sigma \rangle ^ { \flat } = \delta _ { \sigma ^ { \prime } \sigma } , \qquad \langle j , \sigma ^ { \prime } | j , \sigma \rangle ^ { \flat } = 0 . \tag{25.5.9}
$$
那么很容易证明迄今为止构造的态构成了超对称代数的一个完整表示.
Clebsch-Gordan系数的正交性使得我们可以将方程(25.5.5)重写成
$$
\mathcal{Q} _ { a } ^ { * } | j , \sigma \rangle
= \sqrt { 2 M } C _ { \frac { 1 } { 2 } j } \Bigl ( j + \frac { 1 } { 2 } , \sigma + a ; a , \sigma \Bigr )
| j + \frac { 1 } { 2 } , \sigma + a \rangle
+ \sqrt { 2 M } C _ { \frac { 1 } { 2 } j } \Bigl ( j - \frac { 1 } { 2 } , \sigma + a ; a , \sigma \Bigr )
| j - \frac { 1 } { 2 } , \sigma + a \rangle . \tag{25.5.10}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\begin{aligned}
(\mathcal Q^\dagger)^a|j,\sigma\rangle
&=\sqrt{2M}\,C_{\frac12j}(j+\tfrac12,\sigma+a;a,\sigma)
|j+\tfrac12,\sigma+a\rangle\\
&\quad+\sqrt{2M}\,C_{\frac12j}(j-\tfrac12,\sigma+a;a,\sigma)
|j-\tfrac12,\sigma+a\rangle.
\end{aligned}
	$$
</callout>
另外, 方程(25.5.2)表明, 对于超对重态中的任何态 $`| \rangle`$ ,
$$
\left[ \mathcal{Q} _ { a } , \mathcal{Q} _ { \frac { 1 } { 2 } } ^ { * } \mathcal{Q} _ { - \frac { 1 } { 2 } } ^ { * } \right] | \rangle
= 2 M e _ { a }{}^{ b } \mathcal{Q} _ { b } ^ { * } | \rangle . \tag{25.5.11}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			[\mathcal Q^{\dot a},(\mathcal Q^\dagger)^+(\mathcal Q^\dagger)^-]|\,\rangle
=2M(e_W)^{\dot a}{}_{b}(\mathcal Q^\dagger)^b|\,\rangle.
	$$
</callout>
所以方程(25.5.7)和(25.5.3)给出
$$
\begin{aligned}
\mathcal{Q} _ { a } | j , \sigma \rangle ^ { \flat }
&= e _ { a }{}^{ b } \mathcal{Q} _ { b } ^ { * } | j , \sigma \rangle \\
&= \sqrt { 2 M } e _ { a }{}^{ b } C _ { \frac { 1 } { 2 } j } \Bigl ( j + \frac { 1 } { 2 } , \sigma + b ; b , \sigma \Bigr )
| j + \frac { 1 } { 2 } , \sigma + b \rangle \\
&\quad + \sqrt { 2 M } e _ { a }{}^{ b } C _ { \frac { 1 } { 2 } j } \Bigl ( j - \frac { 1 } { 2 } , \sigma + b ; b , \sigma \Bigr )
| j - \frac { 1 } { 2 } , \sigma + b \rangle .
\end{aligned} \tag{25.5.12}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\begin{aligned}
\mathcal Q^{\dot a}|j,\sigma\rangle^\flat
&=(e_W)^{\dot a}{}_{b}(\mathcal Q^\dagger)^b|j,\sigma\rangle\\
&=\sqrt{2M}(e_W)^{\dot a}{}_{b}C_{\frac12j}(j+\tfrac12,\sigma+b;b,\sigma)|j+\tfrac12,\sigma+b\rangle\\
&\quad+\sqrt{2M}(e_W)^{\dot a}{}_{b}C_{\frac12j}(j-\tfrac12,\sigma+b;b,\sigma)|j-\tfrac12,\sigma+b\rangle.
\end{aligned}
	$$
</callout>
从方程(25.5.2), (25.5.3)和(25.5.5)中我们得出
$$
\mathcal{Q} _ { a } | j \pm \frac { 1 } { 2 } , \sigma \rangle
= \sqrt { 2 M } C _ { \frac { 1 } { 2 } j } \Bigl ( j \pm \frac { 1 } { 2 } , \sigma ; a , \sigma - a \Bigr )
| j , \sigma - a \rangle . \tag{25.5.13}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\mathcal Q^{\dot a}|j\!\pm\!\tfrac12,\sigma\rangle
=\sqrt{2M}\,C_{\frac12j}(j\!\pm\!\tfrac12,\sigma;a,\sigma-a)
|j,\sigma-a\rangle,
\qquad a=\operatorname{wt}(\dot a).
	$$
</callout>
而方程(25.5.5), (25.2.31)和(25.5.7)给出
$$
\mathcal{Q} _ { a } ^ { * } | j \pm \frac { 1 } { 2 } , \sigma \rangle
= \sqrt { 2 M } e _ { a }{}^{ b } C _ { \frac { 1 } { 2 } j } \Bigl ( j \pm \frac { 1 } { 2 } , \sigma ; b , \sigma - b \Bigr )
| j , \sigma - b \rangle ^ { \flat } . \tag{25.5.14}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			(\mathcal Q^\dagger)^a|j\!\pm\!\tfrac12,\sigma\rangle
=\sqrt{2M}(e_W)^a{}_{b}C_{\frac12j}(j\!\pm\!\tfrac12,\sigma;b,\sigma-b)
|j,\sigma-b\rangle^\flat.
	$$
</callout>
方程(25.5.3), (25.5.8), (25.5.10)和(25.5.12)—(25.5.14)给出了 $`\mathcal{Q}`$ 和 $`\mathcal{Q} ^ { \ast }`$ 在这个超多重态中的所有态上的作用.
对于 $`j = 0`$ 我们有坍缩超多重态: 方程(25.5.3), (25.5.8), (25.5.10)和(25.5.12)—(25.5.14)变成
$$
\begin{array} { l l }
\mathcal{Q} _ { a } | 0 , 0 \rangle = 0 ,&
\mathcal{Q} _ { a } ^ { * } | 0 , 0 \rangle ^ { \flat } = 0 ,\\
\mathcal{Q} _ { a } ^ { * } | 0 , 0 \rangle = \sqrt { 2 M } | \frac { 1 } { 2 } , a \rangle ,&
\mathcal{Q} _ { a } | 0 , 0 \rangle ^ { \flat } = \sqrt { 2 M } e _ { a }{}^{ b } | \frac { 1 } { 2 } , b \rangle ,\\
\mathcal{Q} _ { a } | \frac { 1 } { 2 } , b \rangle = \sqrt { 2 M } \delta _ { a b } | 0 , 0 \rangle ,&
\mathcal{Q} _ { a } ^ { * } | \frac { 1 } { 2 } , b \rangle = \sqrt { 2 M } e _ { a b } | 0 , 0 \rangle ^ { \flat } .
\end{array} \tag{25.5.15}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\begin{array}{ll}
\mathcal Q^{\dot a}|0,0\rangle=0,
&(\mathcal Q^\dagger)^a|0,0\rangle^\flat=0,\\
(\mathcal Q^\dagger)^a|0,0\rangle=\sqrt{2M}|\tfrac12,a\rangle,
&\mathcal Q^{\dot a}|0,0\rangle^\flat=\sqrt{2M}(e_W)^{\dot a}{}_{b}|\tfrac12,b\rangle,\\
\mathcal Q^{\dot a}|\tfrac12,b\rangle=\sqrt{2M}(\sigma_{W,0})^{\dot a}{}_{b}|0,0\rangle,
&(\mathcal Q^\dagger)^a|\tfrac12,b\rangle=\sqrt{2M}(e_W)^{ab}|0,0\rangle^\flat.
\end{array}
	$$
</callout>
现在假定宇称是守恒的.
回忆, 我们可以选择超对称算符的相位使得宇称算符在这些生成元上的作用由方程(25.3.13)给定.
那么 $`{ \mathcal{Q} } _ { a } ^ { * }`$ 作用在 $`\mathsf { P } | j , \sigma \rangle`$ 是态 $`\mathsf { P } \mathcal{Q} _ { a } | j , \sigma \rangle`$ 的线性组合, 它们为零, 又由于 $`\mathsf { P } | j , \sigma \rangle`$ 和 $`| j , \sigma \rangle`$ 有着相同的选择性质, 它必须正比于它
$$
\mathsf { P } | j , \sigma \rangle = - \eta | j , \sigma \rangle ^ { \flat } . \tag{25.5.16}
$$
由于 P 是幺正的, $`\eta`$ 是满足 $`| \eta | = 1`$ 的相位因子.
对应的讨论表明 $`\mathsf { P } | j , \sigma \rangle ^ { \flat }`$ 正比于 $`| j , \sigma`$ .
为了找到比例系数, 我们注意到
$$
\begin{array} { l } { { \mathsf { P } | j , \sigma \rangle = ( 2 M ) ^ { - 1 } \mathsf { P } \mathcal{Q} _ { \frac { 1 } { 2 } } ^ { * } \mathcal{Q} _ { - \frac { 1 } { 2 } } ^ { * } | j , \sigma \rangle = - \eta ( 2 M ) ^ { - 1 } \mathcal{Q} _ { - \frac { 1 } { 2 } } \mathcal{Q} _ { \frac { 1 } { 2 } } | j , \sigma \rangle ^ { \flat } } } \\ { { \qquad = - \eta ( 2 M ) ^ { - 2 } \mathcal{Q} _ { - \frac { 1 } { 2 } } \mathcal{Q} _ { \frac { 1 } { 2 } } \mathcal{Q} _ { \frac { 1 } { 2 } } ^ { * } \mathcal{Q} _ { - \frac { 1 } { 2 } } ^ { * } | j , \sigma \rangle = - \eta | j , \sigma \rangle . } } \end{array}
$$
这样我们就可以定义自旋 $`j`$ 的态
$$
| j , \sigma \rangle _ { \pm } \equiv \frac { 1 } { \sqrt { 2 } } \left( | j , \sigma \rangle \pm \mathrm { i } | j , \sigma \rangle ^ { \flat } \right) . \tag{25.5.17}
$$
它们有确定的宇称
$$
\mathsf { P } | j , \sigma \rangle _ { \pm } = \pm \mathrm { i } \eta | j , \sigma \rangle _ { \pm } . \tag{25.5.18}
$$
最后, 用宇称算符作用方程(25.5.5)并使用方程(25.3.13)和(25.5.16), 给出
$$
{ \mathsf { P } } \left| j \pm 1 / 2 , \sigma \right\rangle = - { \frac { \eta } { \sqrt { 2 M } } } C _ { \frac { 1 } { 2 } j } \left( j \pm 1 / 2 , \sigma ; a , \sigma - a \right) e _ { a }{}^{ b } \mathcal{Q} _ { b } \left| j , \sigma - a \right\rangle ^ { \flat } .
$$
那么方程(25.5.12)和 Clebsch-Gordan 系数的正交性给出
$$
\mathsf { P } | j \pm \frac { 1 } { 2 } , \sigma \rangle = \eta | j \pm \frac { 1 } { 2 } , \sigma \rangle . \tag{25.5.19}
$$
这正是所要证明的.
我们现在简单地提一下有 $`N`$ 个超对称生成元的扩充超对称性的情况.
正如上一节提及的, 对于任何中心荷, 不可能存在有非零本征值的无质量粒子.
我们可以更进一步并证明中心荷算符的本征值为任何超多重态的质量提供了一个下界.
由于中心荷 $`Z _ { r s }`$ 和 $`Z _ { r s } ^ { * }`$ 彼此对易且与 $`P _ { \mu }`$ 对易,单粒子态可以选择成所有中心荷和 $`P _ { \mu }`$ 的共同本征态, 又因为中心荷与 $`\mathcal{Q} _ { a r }`$ 和 $`{ \mathcal{Q} } _ { a r } ^ { * }`$ 对易, 超多重态中的所有态拥有相同的本征值.
为了推导出将超多重态的质量 $`M`$ 与中心荷在这个多重态上的本征值关联起来的不等式, 我们使用反对易关系(25.2.7)和(25.2.8)写下
$$
\left\{
\mathcal{Q} _ { a r } - e _ { a }{}^{ b } U _ { r }{}^{ s } \mathcal{Q} _ { b s } ^ { * } ,
\mathcal{Q} _ { a r } ^ { * } - e _ { a }{}^{ c } U _ { r }{}^{ t * } \mathcal{Q} _ { c t }
\right\}
= 8 N P ^ { 0 } - 2 \operatorname { Tr } \left( Z U ^ { \dagger } + U Z ^ { \dagger } \right) . \tag{25.5.20}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
			\begin{aligned}
\mathcal B^{\dot a}{}_{r}
&:=\mathcal Q^{\dot a}{}_{r}-(e_W)^{\dot a}{}_{b}U_r{}^s(\mathcal Q^\dagger)^b{}_{s},\\
(\sigma_W^0)_{a\dot a}\{\mathcal B^{\dot a}{}_{r},(\mathcal B^\dagger)^a{}_{r}\}
&=8NP^0-2\operatorname{Tr}(ZU^\dagger+UZ^\dagger).
\end{aligned}
	$$
</callout>
其中 $`U _ { r }{}^{ s }`$ 是一任意的 $`N \times N`$ 幺正矩阵.
左边是正定算符, 通过让它作用在静止的超多重态上, 我们发现
$$
M \ge \frac { 1 } { 4 N } \operatorname { Tr } \left( Z U ^ { \dagger } + U Z ^ { \dagger } \right) , \tag{25.5.21}
$$
其中 $`Z _ { r s }`$ 现在是指质量为 $`M`$ 的超多重态的中心荷值.
极分解定理告诉我们任何方阵 $`Z`$ 可以写成$`H V`$ , 其中 $`H`$ 是正定厄米矩阵而 $`V`$ 是幺正的.
通过令 $`U = V`$ , 我们可以获得一个有用的不等式(事实上是最理想的), 在这一情况下, 方程(25.5.21)变成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cdac3ee015ade06e28#dd2110537b544133a2a4636780d9d49f">
	$$
			M \ge \frac { 1 } { 2 N } \operatorname { Tr } H
= \frac { 1 } { 2 N } \operatorname { Tr } \sqrt { Z ^ { \dagger } Z } . \tag{25.5.22}
	$$
</synced_block>
类比 23.3 节中讨论的 Bogomol’nyi-Prasad-Sommerfeld 磁单极构形, 在那里质量等于一般单极子质量下界的态被称为 $`B P S`$ 态, $`M`$ 等于这个不等式所允许的最小值的态被称为 $`B P S`$ 态.
事实上,这不只是个类比; 我们将会在27.9节看到, 在有扩充超对称性的理论中, 单极子质量的下界是下界(25.5.22)的一个特殊情况.
从方程(25.5.22)的推导中可以看到, 对于 BPS 超多重态, 当算符 $`\mathcal{Q} _ { a r } - e _ { a }{}^{ b } U _ { r }{}^{ s } \mathcal{Q} _ { b s } ^ { * }`$ 作用在这个超多重态中的任何态上时, 它给出零, 所以只有 $`N`$ 个独立的螺旋度下降算符 $`\mathcal{Q} _ { ( 1 / 2 ) r }`$ 和 $`N`$ 个独立的螺旋度上升算符 $`\mathcal{Q} _ { ( - 1 / 2 ) r }`$ , 和无质量超多重态的情况相同.
这给出的超多重态要比一般情况下超多重态要小.
例如, 对于 $`N = 2`$ 超对称性, 中心荷由一个复数给定\*\*
$$
Z = \begin{pmatrix} 0 & Z _ { 1 2 } \\ - Z _ { 1 2 } & 0 \end{pmatrix} . \tag{25.5.23}
$$
<callout color="gray_bg">
	Footnote: 在一些关于 $`N = 2`$ supersymmetry 的文章中, 那里的中心荷 $`Z`$ 是这里的 $`Z / ( 2 \sqrt { 2 } )`$.
</callout>
不等式(25.5.22)在这里是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81cdac3ee015ade06e28#26b82a4da9c2490fabb0059e56c8f602">
	$$
	M \ge | Z _ { 1 2 } | / 2 . \tag{25.5.24}
	$$
</synced_block>
当 $`M = | Z _ { 1 2 } | / 2`$ 时, 有质量粒子超多重态的螺旋度列表与无质量的相同: 有规范超多重态, 它们由一个自旋 1的粒子, 一个自旋 $`1 / 2`$ 的 $`S U ( 2 ) R`$ -对称性双重态以及一个自旋 0 的粒子构成(另一个螺旋度为零的态属于自旋1粒子), 还有极多重态, 它们由一个自旋 $`1 / 2`$ 的粒子和一个自旋0的 $`S U ( 2 )`$ $`R`$ -对称性二重态构成.
为了与在 $`M > | Z _ { 1 2 } | / 2`$ 时遇到的较长的超多重态相区分, 它们有时被称为“短”超多重态.
## 习题
1. 找到一组 $`2 \times 2`$ 矩阵, 使得它们构成既包含费米生成元又包含玻色生成元的阶化Lie代数.
2. 沿用 Haag, Lopuszanski 和 Sohnius 的方法, 推导出 $`2 + 1`$ 维时空中最一般对称超代数的形式.(提示: 在将 $`2 + 1`$ 维时空中的 Lorentz 群生成元标记成 $`A ^ { 1 } = - \mathrm{i} J ^ { 1 0 }`$ , $`A ^ { 2 } = - \mathrm{i} J ^ { 2 0 }`$ 和 $`A ^ { 3 } = J ^ { 1 2 }`$ 后, Poincaré 代数的对易关系是 $`[ A ^ { i } , A ^ { j } ] = \mathrm{i} \epsilon ^ { i j }{}_{ k } A ^ { k }`$, 所以 $`2 + 1`$ 维时空中的齐次 Lorentz 群的表示只用一个整数或半整数指标 $`A`$ 标记.) 在这里假定 Coleman-Mandula 定理成立的条件是满足的.
3. 假定没有螺旋度大于 $`+ 3 / 2`$ 或小于 $`- 3 / 2`$ 的无质量粒子.
找到 $`N = 6`$ 扩充超对称性和(使用CPT对称性) $`N = 5`$ 扩充超对称性的最一般的无质量粒子超多重态.
对这两个扩充超对称性, 你发现的这两个超多重态之间的差异说明了什么?
4. 对于扩充 $`N = 2`$ 超对称性短超多重态中的粒子, 它们可能的宇称是什么?
## 参考文献
\[1\] R. Haag, J. T. Lopuszanski, and M. Sohnius, Nucl.
Phys.
B88, 257 (1975).
这篇文章重印于 Supersymmetry, S. Ferrara 编辑(North Holland/World Scientific, Amsterdam/Singapore, 1987).
\[2\] B. Zumino, Nucl.
Phys.
B89, 535 (1975).
这篇文章重印于Supersymmetry, 参考文献\[1\].
<callout color="gray_bg">
	- R. Haag, J. T. Lopuszanski, and M. Sohnius, Nucl. Phys. B88, 257 (1975). 这篇文章重印于 Supersymmetry, S. Ferrara 编辑(North Holland/World Scientific, Amsterdam/Singapore, 1987)
</callout>
\[3\] M. T. Grisaru and H. N. Pendleton, Phys.
Lett. 67B, 323 (1977).
</content>
</page>
