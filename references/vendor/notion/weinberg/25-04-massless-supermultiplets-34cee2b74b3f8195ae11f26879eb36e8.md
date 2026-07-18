Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8195ae11f26879eb36e8 as of 2026-07-11T21:20:30.479Z:
<page url="https://app.notion.com/p/34cee2b74b3f8195ae11f26879eb36e8">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f815fb0b0e5db189e0b88" title="第 25 章 超对称代数"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"25.4 无质量粒子的超多重态"}
</properties>
<content>
超对称要求已知的粒子在超对称代数的不可约表示下要伴随“超粒子”(sparticles): 伴随夸克和轻子的是玻色“标量夸克”(squarks)和“标量轻子”(sleptons), 伴随规范玻色子的是费米“规范微子”(gauginos).
<details>
<summary>Typed Weinberg dictionary — Srednicki spinor-index grammar（no field mapping）</summary>
	本 fold 只给 massless-supermultiplet 公式恢复 spinor type。a=±1/2 在 Clebsch-Gordan/helicity discussion 中仍是 numerical weight；带点符号显示相应 operator 属于 (0,1/2)。
	$$
	\mathcal Q^{\dot +}{}_{r}:=\mathcal Q^{\dot a}{}_{r}\big|_{a=+1/2},\qquad \mathcal Q^{\dot -}{}_{r}:=\mathcal Q^{\dot a}{}_{r}\big|_{a=-1/2}.
	$$
	$$
	(\mathcal Q^\dagger)^\pm{}_{r}:=(\mathcal Q^\dagger)^a{}_{r}\big|_{a=\pm1/2}.
	$$
</details>
所有这些粒子还都没有观测到, 所以超对称性肯定破缺, 而超粒子的质量几乎肯定要比电弱 $`S U ( 2 ) \times U ( 1 )`$ 规范群自发破缺产生的夸克质量, 轻子质量和规范玻色子质量大得多, 因此和超对称多重态内部分裂的大小处于同一量级.
因此, 在能标足够高时很有可能我们可以忽略掉超对称破缺和这些质量分裂, 此时我们也可以将已知的夸克, 轻子, 规范玻色子和它们的超对称伴视作是无质量的.
因此, 我们对无质量粒子的超对称多重态很感兴趣.
本节采用 25.2 的 translated spinor-index notation. 也就是说, $`(0,1/2)`$ generator 写作 $`\mathcal Q^{\dot a r}`$, 它的 Hermitian conjugate 写作 $`\left(\mathcal Q^\dagger\right)^a{}_r`$. 在 helicity ladder 中, $`\dot{+}`$ 和 $`\dot{-}`$ 分别表示 $`\dot a=\pm1/2`$, 而 $`+`$ 和 $`-`$ 表示 conjugate undotted component.
考察这样一个态, 它只包含一个无质量粒子且这个粒子属于某个超对重态.
通过用算符 $`\mathcal{Q}^{\dot a r}`$ 和(或) $`\left(\mathcal{Q}^\dagger\right)^a{}_r`$ 作用这个态, 我们可以获得同一超多重态中的其它态.
由于 $`\mathcal{Q}^{\dot a r}`$ 和 $`\left(\mathcal{Q}^\dagger\right)^a{}_r`$ 与 $`P _ { \mu }`$ 对易, 所有这些态有相同的4-动量值.
我们将在这些态的4 -动量是 $`p ^ { 1 } = p ^ { 2 } = 0`$ 且 $`p ^ { 3 } = p ^ { 0 } = E`$ 的 Lorentz 参考系下进行处理.
在4 -动量的这一选择下, 我们有
$$
- \bar\sigma _ { \mu } p ^ { \mu } = E ( \sigma _ { 0 } + \sigma _ { 3 } )
= 2 E \begin{pmatrix} 1&0\\0&0\end{pmatrix} . \tag{25.4.1}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
	(\sigma_{W,\mu})^{\dot a b}p^\mu
=E\bigl[(\sigma_{W,0})^{\dot a b}+(\sigma_{W,3})^{\dot a b}\bigr]
=2E\begin{pmatrix}1&0\\0&0\end{pmatrix}^{\dot a b}.
	$$
</callout>
除去因子 $`2 E`$ 来看, 这是到螺旋度为 $`+ 1 / 2`$ 的子空间上的投射矩阵.
因此, 反对易关系(25.2.7)表明, 对于有这种 4 -动量的超多重态, $`\{ \mathcal{Q}^{\dot{-} r} , \left(\mathcal{Q}^\dagger\right)^-{}_r \}`$ 作用在这个超多重态中的任何态上都给出零. 由正定性, $`\mathcal{Q}^{\dot{-} r}`$ 和 $`\left(\mathcal{Q}^\dagger\right)^-{}_r`$ 本身也在这个多重态上给出零.
因此我们只能通过用 $`\mathcal{Q}^{\dot{+} r}`$ 和 $`\left(\mathcal{Q}^\dagger\right)^+{}_r`$ 进行作用来构建这个超多重态中的态.
更进一步, 我们可以用 $`\mathcal{Q}`$ 的 $`J ^ { 3 }`$ 值来标记它们, 也就是说
$$
[ J ^ { 3 } , \mathcal{Q}^{\dot a r} ] = - a \mathcal{Q}^{\dot a r} , \tag{25.4.2}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
	[J^3,\mathcal Q^{\dot a}{}_{r}]
=-a\,\mathcal Q^{\dot a}{}_{r},
\qquad a=\operatorname{wt}(\dot a)=\pm\frac12.
	$$
</callout>
这里 $`a`$ 表示 dotted component $`\dot a`$ 的数值 $`+1/2`$ 或 $`-1/2`$. 所以 $`\mathcal{Q}^{\dot{+} r}`$ 和 $`\left(\mathcal{Q}^\dagger\right)^+{}_r`$ 分别将螺旋度减小和提高 $`1 / 2`$.
我们首先来考察简单超对称的情况.
考察一个最大螺旋度为 $`\lambda _ { \mathrm{max} }`$ 的超多重态, 用 $`\left| \lambda _ { \max } \right\rangle`$ 标记任何螺旋度为 $`\lambda _ { \mathrm{max} }`$ 的单粒子态, 并设它的4 -动量是 $`p ^ { \mu }`$ .
那么
$$
\left(\mathcal{Q}^\dagger\right)^+ | \lambda _ { \max } \rangle = 0 , \tag{25.4.3}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
	(\mathcal Q^\dagger)^+|\lambda_{\max}\rangle=0.
	$$
</callout>
用 $`\mathcal{Q}^{\dot{+}}`$ 作用这个态则给出螺旋度为 $`\lambda _ { \max } - 1 / 2`$ 的态 $`\left| \lambda _ { \max } - 1 / 2 \right\rangle`$ .
我们会将这个态定义成
$$
| \lambda _ { \mathrm{max} } - 1 / 2 \rangle \equiv ( 4 E ) ^ { - 1 / 2 } \mathcal{Q}^{\dot{+}} | \lambda _ { \mathrm{max} } \rangle . \tag{25.4.4}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
	|\lambda_{\max}-\tfrac12\rangle
\equiv(4E)^{-1/2}\mathcal Q^{\dot +}|\lambda_{\max}\rangle.
	$$
</callout>
加上方程(25.4.1)和(25.4.3), 基础反对易关系(25.2.7)表明这个态的归一化方式与 $`| \lambda _ { \mathrm{max} } \rangle`$ 相同
$$
\langle \lambda _ { \max } - 1 / 2 | \lambda _ { \max } - 1 / 2 \rangle = \langle \lambda _ { \max } | \lambda _ { \max } \rangle , \tag{25.4.5}
$$
特别地, 这个态不能为零.
方程(25.2.32)表明 $`\left(\mathcal{Q}^{\dot{+}}\right)^2 = 0`$ , 所以用 $`\mathcal{Q}^{\dot{+}}`$ 作用
$`\left| \lambda _ { \mathrm{max} } - 1 / 2 \right\rangle`$ 给出零:
$$
\mathcal{Q}^{\dot{+}} | \lambda _ { \mathrm{max} } - 1 / 2 \rangle = ( 4 E ) ^ { - 1 / 2 } \left(\mathcal{Q}^{\dot{+}}\right)^2 | \lambda _ { \mathrm{max} } \rangle = 0 . \tag{25.4.6}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
	\mathcal Q^{\dot +}|\lambda_{\max}-\tfrac12\rangle
=(4E)^{-1/2}(\mathcal Q^{\dot +})^2|\lambda_{\max}\rangle=0.
	$$
</callout>
另一方面, 用 $`\left(\mathcal{Q}^\dagger\right)^+`$ 作用这个态给出的是我们作为出发点的态.
即,
$$
\left(\mathcal{Q}^\dagger\right)^+ | \lambda _ { \max } - 1 / 2 \rangle = ( 4 E ) ^ { - 1 / 2 } \left(\mathcal{Q}^\dagger\right)^+ \mathcal{Q}^{\dot{+}} | \lambda _ { \max } \rangle = ( 4 E ) ^ { - 1 / 2 } \{ \left(\mathcal{Q}^\dagger\right)^+ , \mathcal{Q}^{\dot{+}} \} | \lambda _ { \max } \rangle ,
$$
这使得方程(25.4.1)和反对易关系(25.2.31)产生
$$
\left(\mathcal{Q}^\dagger\right)^+ | \lambda _ { \max } - 1 / 2 \rangle = ( 4 E ) ^ { 1 / 2 } | \lambda _ { \max } \rangle . \tag{25.4.7}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
	(\mathcal Q^\dagger)^+|\lambda_{\max}-\tfrac12\rangle
=(4E)^{1/2}|\lambda_{\max}\rangle.
	$$
</callout>
因此超多重态仅由两个态构成, 螺旋度分别是 $`\lambda _ { \mathrm{max} }`$ 和 $`\lambda _ { \max } - 1 / 2`$ .
在这两个态提供的基下, 算符 $`\mathcal{Q}^{\dot{+}}`$ 和 $`\left(\mathcal{Q}^\dagger\right)^+`$ 被表示成矩阵
$$
q _ { \frac { 1 } { 2 } } = \sqrt { 4 E } \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 1 } } & { { 0 } } \end{array} \right) \ , \qquad q _ { \frac { 1 } { 2 } } ^ { \dagger } = \sqrt { 4 E } \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \ , \tag{25.4.8}
$$
而算符 $`\mathcal{Q}^{\dot{-}}`$ 和 $`\left(\mathcal{Q}^\dagger\right)^-`$ 被表示成零.
值得强调的是, 在有简单超对称性的理论中, 这是唯一一种无质量超多重态.
不存在没有超对称伴的无质量粒子, 也不存在有多个超对称伴的无质量粒子.
当然, CPT 不变性暗示了, 对于每个螺旋度为 $`\lambda`$ 和 $`\lambda - 1 / 2`$ 的无质量粒子超多重态, 必存在一个螺旋度为 $`- \lambda + 1 / 2`$ 和 $`- \lambda`$ 的反多重态.特别地, 螺旋度为 $`+ 1 / 2`$ 和 $`- 1 / 2`$ 的无质量粒子和反粒子不是伴随着螺旋度为 $`+ 1`$ 和 $`- 1`$ 的无质量粒子和反粒子, 就是伴随着螺旋度均为零的无质量粒子和反粒子.
那么已知的夸克, 轻子和规范玻色子该如何填进这个图景中呢? 我们将假定超对称性生成元与 $`S U ( 3 ) \times S U ( 2 ) \times U ( 1 )`$ 规范群的生成元对易.\* 夸克和轻子所属的规范群表示与规范玻色子所属的规范群表示不同, 所以它们不可能处在同一个超多重态中.
Footnote: 在简单超对称性中, 由于 $`S U ( 3 ) \times S U ( 2 )`$ 这样的 semisimple Lie algebra 没有 nontrivial one-dimensional representation, 所以生成元 $`Q _ \alpha`$ 在任何情况下都必须与 $`S U ( 3 ) \times S U ( 2 )`$ 生成元对易.
由此我们不得不得到如下的结论:在 $`S U ( 2 ) \times U ( 1 )`$ 对称性破缺可以被忽略的高能极限下, 每种色和味的无质量夸克和轻子都伴随着色和味相同但螺旋度为零的无质量标量夸克和标量轻子成对出现在超多重态中, 而与无质量规范玻色子伴随的螺旋度为 $`\pm 1 / 2`$ 的无质量规范微子构成了 $`S U ( 3 ) \times S U ( 2 ) \times U ( 1 )`$ 的一个伴随表示.
由于存在引力, 我们知道除了标准模型的粒子以外还必须存在螺旋度为 $`\pm 2`$ 的粒子, 引力子.对于螺旋度为 $`\lambda`$ 的无质量粒子, 如果 $`| \lambda | > 1 / 2`$ , 那么在低动量时它必须与守恒量耦合.\*\* 螺旋度为 $`\pm 1`$ 的软无质量粒子可以与各种内部对称性的生成元耦合, 螺旋度为 $`\pm 3 / 2`$ 的软无质量粒子可以与超对称生成元 $`\mathcal{Q}^{\dot a r}`$ 和 $`\left(\mathcal{Q}^\dagger\right)^a{}_r`$ 耦合, 而螺旋度为 $`\pm 2`$ 的软粒子可以与一个守恒量耦合, 动量 4 -矢 $`P _ { \mu }`$ , 但是没有什么守恒量可以与 $`| \lambda | > 2`$ 的软粒子耦合.
Footnote: 整数螺旋度的情况在 13.1 节讨论过; 半整数螺旋度的讨论由 Grisaru 和 Pendleton 给出.\[3\]
由此我们得出, 引力子所处的超多重态不能含有螺旋度为 $`\pm 5 / 2`$ 的粒子, 所以它所处的超多重态必须含有螺旋度为 $`\pm 3 / 2`$ 的粒子, 这个粒子被称为引力微子(gravitino), 它与超对称性生成元自身耦合.
这个超多重态的场论被称为超引力, 我们将在第 31 章讨论.
现在我们来考察有 $`N`$ 个超对称生成元的扩充超对称性情况.
我们首先注意到, $`\mathcal{Q}^{\dot{-} r}`$ 作用在超多重态中的态(包含那些通过 $`\mathcal{Q}^{\dot{+} s}`$ 作用这个多重态的任何其它态获得的态)上时都给出零,所以 $`Z ^ { r s }`$ 也湮灭这个多重态的任何态.
在中心荷不在这个图景的前提下, 当超对称生成元 $`\mathcal{Q}^{\dot{+} r}`$ 作用在无质量粒子超多重态上时, 它们反对易, 所以用 $`n`$ 个这样的生成元作用拥有最大螺旋度 $`\lambda _ { \mathrm{max} }`$ 且动量为 $`p ^ { \mu }`$ 的单粒子态时, 我们会得到 $`\frac { N ! } { n ! ( N - n ) ! }`$ 个螺旋度为 $`\lambda _ { \max } - n / 2`$ 且动量相同的单粒子态, 这些单粒子态构成 $`S U ( N )`$ $`R`$-对称性(25.2.30)的一个 $`n`$ 阶反对称表示.
Footnote: $`U ( N )`$ $`R`$-对称性的 $`U ( 1 )`$ 部分通常会被 quantum anomaly 破坏掉.
能够给出一个非零态的最大 $`n`$ 值是 $`n = N`$ , 所以一个超多重态中的最小螺旋度是
$$
\lambda _ { \min } = \lambda _ { \max } - N / 2 . \tag{25.4.9}
$$
如果我们希望排除掉那些螺旋度 $`\lambda`$ 满足 $`| \lambda | > 2`$ 的无质量粒子, 那么 $`\lambda _ { \max } - \lambda _ { \min } \leq 4`$ , 所以只有那些 $`N \leq 8`$ 的扩充超对称性才是被允许的.
当 $`N \ = \ 8`$ 且 $`| \lambda | > 2`$ 的螺旋度被排除时, 只有一种可能的超多重态, 组成它的是: 螺旋度为 $`\pm 2`$ 的引力子各1个; 螺旋度为 $`\pm 3 / 2`$ 的引力微子各8个; 螺旋度为 $`\pm 1`$ 的规范玻色子各28个; 螺旋度为 $`\pm 1 / 2`$ 的费米子各56个; 以及70个螺旋度为零的玻色子.
对比 $`N = 7`$ 的情况, 依旧排除掉 $`| \lambda | > 2`$ 的螺旋度.
这里存在两个超多重态.
一个超多重态包含: 1个螺旋度为 $`+ 2`$ 的引力子; 7个螺旋度为 $`+ 3 / 2`$ 的引力微子; 21个螺旋度为 $`+ 1`$ 的规范玻色子;35个螺旋度为 $`+ 1 / 2`$ 的费米子; 35 个螺旋度为零的玻色子; 21 个螺旋度为 $`- 1 / 2`$ 的费米子; 7 个螺旋度为 $`- 1`$ 的规范玻色子; 以及1个螺旋度为 $`- 3 / 2`$ 的引力微子.
另一个是CPT-共轭的超多重态,它的所有螺旋度反号.
将这两个超多重态中的粒子数加一下, 我们有螺旋度为 $`\pm 2`$ 的引力子各1个;螺旋度为 $`\pm 3 / 2`$ 的引力微子各 $`7 + 1 = 8`$ 个; 螺旋度为 $`\pm 1`$ 的规范玻色子各 $`21 + 7 = 28`$ 个; 螺旋度为 $`\pm 1 / 2`$ 的费米子各 $`35 + 21 = 56`$ 个; 以及 $`35 + 35 = 70`$ 个螺旋度为零的玻色子.
因此 $`N =`$ 8和 $`N = 7`$ 的扩充超引力理论有精确相同的粒子内容, 它们实质上是等价的.
另一方面, 在 $`N \leq 6`$ 的扩充超引力理论中, 螺旋度为 $`\pm 3 / 2`$ 的引力微子分别只有 $`N`$ 个, 因此它们都是不同的.
当 $`N \leq 4`$ 时, 还存在整体超对称理论的可能性, 在这样的理论中, 超多重态没有引力子和引力微子.
对于整体 $`N = 4`$ 超对称性, 仅存在一个超多重态, 组成它的是: 螺旋度为 $`\pm 1`$ 的规范玻色子各1个; 螺旋度为 $`\pm 1 / 2`$ 的费米子各4个; 以及6个螺旋度为零的玻色子.
这等价于 $`N = 3`$ 的整体超对称理论, 它有两个超多重态: 一个超多重态有1个螺旋度为 $`+ 1`$ 的规范玻色子; 3个螺旋度为 $`+ 1 / 2`$ 的费米子; 3个螺旋度为零的玻色子; 以及1个螺旋度为 $`- 1 / 2`$ 的费米子; 而另一个CPT共轭的超多重态有相反的螺旋度.
将这两个 $`N = 3`$ 超多重态中螺旋度相同的粒子数加起来就给出了同 $`N = 4`$ 整体超对称性相同的粒子内容.
拥有 $`N = 4`$ 超对称性的规范场论拥有显著的性质, 这将在 27.9 节进行讨论.
对于 $`N = 2`$ 的扩充超对称, 除了那些通过CPT关联的超多重态外, 存在两种不同类型的超多重态.
一种是规范超多重态, 它们包含一个螺旋度为 $`+ 1`$ 的规范玻色子, 两个螺旋度为 $`+ 1 / 2`$ 的费米子, 并且这两个费米子构成了 $`S U ( 2 ) R`$ -对称性下的一个双重态, 以及一个螺旋度为零的玻色子,再加上螺旋度都反号的CPT-共轭超多重态.
每个规范超多重态和它的反多重态合起来包含了:螺旋度为 $`\pm 1`$ 的规范玻色子各 1 个, 螺旋度为 $`\pm 1 / 2`$ 的费米子双重态各一个, 以及两个螺旋度为零的 $`S U ( 2 )`$ 单态玻色子.
另一种是极多重态(hypermultiplet), 它们包含螺旋度 $`\pm 1 / 2`$ 的费米子各一个, 以及螺旋度为零的玻色子构成的 $`S U ( 2 )`$ 双重态, 再加上这种超多重态的CPT-共轭.
(在量子场论中, 极多重态不能是自身的反多重态, 若非如此, 螺旋度为零的粒子将会被两个实标量场描述,而它们是无法形成一个 $`S U ( 2 )`$ 多重态的.) 当然, 在真实世界中还必须存在引力子超多重态, 它包含一个螺旋度为 $`+ 2`$ 的引力子, 一个螺旋度为 $`+ 3 / 2`$ 的引力微子的 $`S U ( 2 )`$ 双重态, 以及一个螺旋度为 $`+ 1`$ 的规范玻色子, 再加上它们螺旋度相反的CPT-共轭.
我们将在27.9节构造 $`N = 2`$ 超对称规范理论, 并在29.5节以非微扰的方式探索它的性质.
在可达到的能标试图将扩充超对称性融入进粒子的真实理论时, 这些超多重态的粒子内容反映出了一个困难.
除了一种情况外, 在任何其它情况中, 螺旋度 $`+ 1 / 2`$ 的费米子和螺旋度 $`+ 1`$ 的规范玻色子同属一个超多重态.
规范玻色子属于规范群的伴随表示, 所以如果超对称生成在规范群下不变, 那么螺旋度 $`+ 1 / 2`$ 的费米子也必须属于伴随表示, 而这是一个实表示.
而已知的夸克和轻子所属的 $`S U ( 3 ) \times S U ( 2 ) \times U ( 1 )`$ 表示是手征的——即, 对于这样的表示, 螺旋度 $`+ 1 / 2`$ 的费米子属于一个复表示, 那么它们的CPT共轭, 螺旋度 $`- 1 / 2`$ 的费米子构建的表示肯定与这个表示不同, 二者是矛盾的.
唯一的例外是上面讨论的 $`N = 2`$ 极多重态, 在这种情况中, 螺旋度 $`+ 1 / 2`$ 的费米子不在规范玻色子所处的超多重态中.
但在这一情况中, 螺旋度为 $`+ 1 / 2`$ 和 $`- 1 / 2`$ 的粒子处在同一超多重态中, 因此在任何使得超对称生成元不变的规范变换下, 它们的变换必须相同.
它们可能属于这个规范群的一个复表示, 那么这个极多重态的CPT-共轭就属于复共轭表示, 这样一来, 各个螺旋度的费米子属于两个表示的和, 这是实的, 依旧与已知夸克和轻子的手征性相矛盾.
与之相反, 对于简单超对称性存在只包含螺旋度 $`+ 1 / 2`$ 和零的超多重态, 它们可能处在规范群的一个复表示中并与CPT-共轭超多重态构建的表示不同.
这里不存在与手征性相悖的矛盾.
由于这个原因, 将超对称在可实现的能标视为没有破缺的对称性的讨论大多集中在简单超对称性而非扩充超对称性上.
</content>
</page>
