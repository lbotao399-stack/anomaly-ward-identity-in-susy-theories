Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81edb24ed794dd04feb5 as of 2026-07-04T13:03:11.963Z:
<page url="https://app.notion.com/p/34cee2b74b3f81edb24ed794dd04feb5">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f815fb0b0e5db189e0b88" title="第 25 章 超对称代数"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"25.2 超对称代数"}
</properties>
<content>
考察一个对称性生成元与 $`S .`$ -矩阵对易的一般阶化Lie代数.
如果 $`Q`$ 是其中的一个费米对称性生成元, 那么 $`U ^ { - 1 } ( \Lambda ) Q U ( \Lambda )`$ 也是, 其中 $`U ( \Lambda )`$ 是任意齐次 Lorentz 变换 $`\Lambda ^ { \mu } { } _ { \nu }`$ 对应的量子力学算符.因此 $`U ^ { - 1 } ( \Lambda ) Q U ( \Lambda )`$ 是费米对称性生成元完备集的线性组合, 由此得出, 这组生成元必须构成齐次Lorentz 群的一个表示.
这样, 根据各个生成元所属的齐次Lorentz 群不可约表示就可以对它们进行分类.
正如 5.6 节所描述的, 对于任何一组构成齐次 Lorentz 群表示的算符, 我们可以通过给出这组算符与生成元 $`\mathbf{A}`$ 和 $`\mathbf{B}`$ 的对易关系来指定这个表示, 其中 $`\mathbf{A}`$ 和 $`\mathbf{B}`$ 定义成
$$
\begin{array} { r } { { \bf A } \equiv \frac { 1 } { 2 } \Big ( { \bf J } + \mathrm{i} { \bf K } \Big ) , \qquad { \bf B } \equiv \frac { 1 } { 2 } \Big ( { \bf J } - \mathrm{i} { \bf K } \Big ) , } \end{array} \tag{25.2.1}
$$
其中 $`\mathbf{J}`$ 和 $`\mathbf{K}`$ 分别是旋转和增速(boost)的厄米生成元.
A 和 $`\mathbf{B}`$ 满足对易关系
$$
[ A ^ { i } , A ^ { j } ] = \epsilon ^ { i j } { } _ { k } A ^ { k } , \qquad [ B ^ { i } , B ^ { j } ] = \epsilon ^ { i j } { } _ { k } B ^ { k } , \qquad [ A ^ { i } , B ^ { j } ] = 0 . \tag{25.2.2}
$$
其中 $`i , j , k`$ 取遍值 1, 2, 3, $`\epsilon ^ { i j k }`$ 全反对称, $`\epsilon ^ { 1 2 3 } = + 1`$ .
因此, 就像带有两个独立自旋的态一样齐次Lorentz 群的表示由一对整数或半整数 $`A`$ 和 $`B`$ 标记, 而表示中的元素由一对指标 $`a , b`$ 标记, 它们以1 为步长分别从 $`- A`$ 取到 $`A`$ 以及从 $`- B`$ 取到 $`B`$ .
更确切一些, 一组总数为 $`( 2 A + 1 ) ( 2 B + 1 )`$ 的算符 $`Q _ { a b } ^ { A B }`$ 构成了齐次 Lorentz 群的一个 $`( A , B )`$ 表示, 它们满足对易关系
$$
[ { \bf A } , Q _ { a b } ^ { A B } ] = - ( { \bf J } ^ { ( A ) } ) _ { a } { } ^ { a ^ { \prime } } Q _ { a ^ { \prime } b } ^ { A B } , \qquad [ { \bf B } , Q _ { a b } ^ { A B } ] = - ( { \bf J } ^ { ( B ) } ) _ { b } { } ^ { b ^ { \prime } } Q _ { a b ^ { \prime } } ^ { A B } . \tag{25.2.3}
$$
其中 $`\mathbf{J} ^ { ( j ) }`$ 是角动量为 $`j`$ 的自旋3 -矢矩阵:
$$
\left( J _ { 1 } ^ { ( j ) } \pm \mathrm{i} J _ { 2 } ^ { ( j ) } \right) _ { \sigma ^ { \prime } \sigma } = \delta _ { \sigma ^ { \prime } , \sigma \pm 1 } \sqrt { ( j \mp \sigma ) ( j \pm \sigma + 1 ) } , \qquad \left( J _ { 3 } ^ { ( j ) } \right) _ { \sigma ^ { \prime } \sigma } = \delta _ { \sigma ^ { \prime } \sigma } \sigma . \tag{25.2.4}
$$
从方程(25.2.4)得出\*
$$
- \left( \mathbf{J} ^ { ( j ) } \right) _ { \sigma ^ { \prime } , \sigma } ^ { * } = ( - 1 ) ^ { \sigma ^ { \prime } - \sigma } \Big ( \mathbf{J} ^ { ( j ) } \Big ) _ { - \sigma ^ { \prime } , - \sigma } . \tag{25.2.5}
$$
因此, 如果 $`Q _ { \sigma } ^ { j }`$ 是一组按照旋转群的自旋 $`j`$ 表示进行变换的算符, 那么 $`( - 1 ) ^ { j - \sigma } Q _ { - \sigma } ^ { j * }`$ 也是.
Footnote: 这里用星号表示算符的 Hermitian conjugate 或数的 complex conjugate. 对由这些共轭构成的矩阵, 用 dagger $`\dagger`$ 表示再转置.
另外, 方程(25.2.1)表明 $`\mathbf A ^ { * } = \mathbf B`$ .
通过对方程(25.2.3)取厄米共轭, 我们看到, 按照齐次Lorentz 群的 $`( A , B )`$ 表示进行变换的算符的厄米共轭 $`Q _ { a b } ^ { A B * }`$ 与按照 $`( B , A )`$ 表示进行变换的算符 $`\bar { Q } _ { b a } ^ { B A }`$ , 它们通过一个相似变换彼此关联:
$$
Q _ { a b } ^ { A B * } = ( - 1 ) ^ { A - a } ( - 1 ) ^ { B - b } \bar { Q } _ { - b , - a } ^ { B A } . \tag{25.2.6}
$$
<callout color="gray_bg">
	Codex 补充证明：方程(25.2.6)
	证明如下. 先把共轭算符重新定义为
	$$
	\bar { Q } _ { b a } ^ { B A } \equiv ( - 1 ) ^ { A + a } ( - 1 ) ^ { B + b } Q _ { - a , - b } ^ { A B * } .
	$$
	方程(25.2.1)给出 $`\mathbf A ^ { * } = \mathbf B`$, $`\mathbf B ^ { * } = \mathbf A`$. 对方程(25.2.3)取厄米共轭时使用 $`[ X , Y ] ^ { * } = - [ X ^ { * } , Y ^ { * } ]`$, 得到
	$$
	\begin{aligned}
[ { \bf B } , Q _ { a b } ^ { A B * } ]
&= ( { \bf J } ^ { ( A ) } ) _ { a } { } ^ { a ^ { \prime } * } Q _ { a ^ { \prime } b } ^ { A B * } ,\\
[ { \bf A } , Q _ { a b } ^ { A B * } ]
&= ( { \bf J } ^ { ( B ) } ) _ { b } { } ^ { b ^ { \prime } * } Q _ { a b ^ { \prime } } ^ { A B * } .
\end{aligned}
	$$
	于是对 $`\mathbf A`$ 有
	$$
	\begin{aligned}
[ { \bf A } , \bar { Q } _ { b a } ^ { B A } ]
&= ( - 1 ) ^ { A + a } ( - 1 ) ^ { B + b }
[ { \bf A } , Q _ { - a , - b } ^ { A B * } ]\\
&= ( - 1 ) ^ { A + a } ( - 1 ) ^ { B + b }
( { \bf J } ^ { ( B ) } ) _ { - b } { } ^ { - b ^ { \prime } * }
Q _ { - a , - b ^ { \prime } } ^ { A B * }\\
&= - ( { \bf J } ^ { ( B ) } ) _ { b } { } ^ { b ^ { \prime } }
( - 1 ) ^ { A + a } ( - 1 ) ^ { B + b ^ { \prime } }
Q _ { - a , - b ^ { \prime } } ^ { A B * }\\
&= - ( { \bf J } ^ { ( B ) } ) _ { b } { } ^ { b ^ { \prime } }
\bar { Q } _ { b ^ { \prime } a } ^ { B A } ,
\end{aligned}
	$$
	其中第三行正是方程(25.2.5)在自旋 $`B`$ 表示上的应用. 同样地, 对 $`\mathbf B`$ 有
	$$
	\begin{aligned}
[ { \bf B } , \bar { Q } _ { b a } ^ { B A } ]
&= ( - 1 ) ^ { A + a } ( - 1 ) ^ { B + b }
[ { \bf B } , Q _ { - a , - b } ^ { A B * } ]\\
&= ( - 1 ) ^ { A + a } ( - 1 ) ^ { B + b }
( { \bf J } ^ { ( A ) } ) _ { - a } { } ^ { - a ^ { \prime } * }
Q _ { - a ^ { \prime } , - b } ^ { A B * }\\
&= - ( { \bf J } ^ { ( A ) } ) _ { a } { } ^ { a ^ { \prime } }
( - 1 ) ^ { A + a ^ { \prime } } ( - 1 ) ^ { B + b }
Q _ { - a ^ { \prime } , - b } ^ { A B * }\\
&= - ( { \bf J } ^ { ( A ) } ) _ { a } { } ^ { a ^ { \prime } }
\bar { Q } _ { b a ^ { \prime } } ^ { B A } .
\end{aligned}
	$$
	这两个对易关系就是方程(25.2.3)中 $`( B , A )`$ 表示的定义, 第一指标 $`b`$ 由 $`\mathbf A`$ 按自旋 $`B`$ 作用, 第二指标 $`a`$ 由 $`\mathbf B`$ 按自旋 $`A`$ 作用. 将上面对 $`\bar Q`$ 的定义改写为 $`Q ^ { A B * }`$ 的形式, 就得到方程(25.2.6).
</callout>
Haag-Lopuszanski-Sohnius 定理\[1\]的部分表述是, 费米对称性生成元只能属于 $`( 0 , 1 / 2 )`$ 表示和$`( 1 / 2 , 0 )`$ 表示.
- R. Haag, J. T. Lopuszanski, and M. Sohnius, Nucl. Phys. B88, 257 (1975). 这篇文章重印于 Supersymmetry, S. Ferrara 编辑(North Holland/World Scientific, Amsterdam/Singapore, 1987)
我们已经看到 $`( 0 , 1 / 2 )`$ 算符或 $`( 1 / 2 , 0 )`$ 算符的厄米共轭分别是 $`( 1 / 2 , 0 )`$ 算符或 $`( 0 , 1 / 2 )`$ 算符的线性组合, 因此, 费米对称性算符的完备集可以分成 $`( 0 , 1 / 2 )`$ 生成元 $`\mathcal{Q} ^ { \dot a r }`$ (省略了表示 $`( 0 , 1 / 2 )`$ 的上标)和
它们的 $`( 1 / 2 , 0 )`$ 厄米共轭 $`\left( \mathcal{Q} ^ \dagger \right) ^ { a }{} _ { r }`$ , 其中 $`\dot a`$ 和 $`a`$ 分别是 dotted 与 undotted 2分量旋量指标, $`r`$ 用来区分Lorentz 变换性质相同的不同2分量生成元.\*\*
Footnote: 为了与本节后面将要引入的 4 分量 Dirac spinor 区分, 这里用手写体 $`\mathcal Q`$ 标记 Weyl spinor. 本译文在最终代数中使用 van der Waerden notation: $`(0,1/2)`$ 指标写成 dotted upper index, $`(1/2,0)`$ 共轭指标写成 undotted upper index; Weinberg 原文中的 $`a=\pm1/2`$ weight-label 写法只在 Clebsch-Gordan 计算中保留.
这个定理进一步表述了, 可以定义费米生成元使它们满足反对易关系
$$
\begin{array} { l } { { \{ \mathcal{Q} ^ { \dot a r } , \left( \mathcal{Q} ^ \dagger \right) ^ { b }{} _ { s } \} = - 2 \delta ^ { r }{} _ { s } \bar\sigma _ { \mu }{} ^ { \dot a b } P ^ { \mu } , } } \\ { { \{ \mathcal{Q} ^ { \dot a r } , \mathcal{Q} ^ { \dot b s } \} = \epsilon ^ { \dot a \dot b } Z ^ { r s } , } } \end{array} \tag{25.2.7-25.2.8}
$$
其中 $`P ^ { \mu }`$ 是4-动量算符, $`Z ^ { r s } = - Z ^ { s r }`$ 是玻色对称性生成元, $`\bar\sigma _ { \mu }{} ^ { \dot a b }`$ 和 $`\epsilon ^ { \dot a \dot b }`$ 是 $`2 \times 2`$ 矩阵(行与列用 $`+ 1 / 2 , - 1 / 2`$ 标记):
$$
\begin{array}{lll}\sigma _ { 1 } = \begin{pmatrix}0&1\\1&0\end{pmatrix},& \sigma _ { 2 } = \begin{pmatrix}0&-\mathrm{i}\\ \mathrm{i}&0\end{pmatrix},& \sigma _ { 3 } = \begin{pmatrix}1&0\\0&-1\end{pmatrix},\\ \sigma _ { 0 } = \begin{pmatrix}1&0\\0&1\end{pmatrix},& e = \begin{pmatrix}0&1\\-1&0\end{pmatrix}.&\end{array} \tag{25.2.9}
$$
最后, 费米对称性生成元与能量和动量对易:
$$
\left[ P _ { \mu } , \mathcal{Q} ^ { \dot a r } \right] = \left[ P _ { \mu } , \left( \mathcal{Q} ^ \dagger \right) ^ { a }{} _ { r } \right] = 0 , \tag{25.2.10}
$$
而 $`Z ^ { r s }`$ 和 $`Z ^ { * }{} _ { r s }`$ 是这个代数的一组中心荷, 也就是说
$$
\begin{array} { r l } & { 0 = \left[ Z ^ { r s } , \mathcal{Q} ^ { \dot a t } \right] = \left[ Z ^ { r s } , \left( \mathcal{Q} ^ \dagger \right) ^ { a }{} _ { t } \right] = \left[ Z ^ { r s } , Z ^ { t u } \right] = \left[ Z ^ { r s } , Z ^ { * }{} _ { t u } \right] } \\ & { \phantom { \frac { 1 } { 1 } } = \left[ Z ^ { * }{} _ { r s } , \mathcal{Q} ^ { \dot a t } \right] = \left[ Z ^ { * }{} _ { r s } , \left( \mathcal{Q} ^ \dagger \right) ^ { a }{} _ { t } \right] = \left[ Z ^ { * }{} _ { r s } , Z ^ { * }{} _ { t u } \right] . } \end{array} \tag{25.2.11}
$$
为了证明这些结果, 我们先来考察非零费米对称性生成元, 并要求它属于齐次Lorentz 群的某个 $`( A , B )`$ 不可约表示的, 这样它就可以记做 $`Q _ { a b } ^ { A B }`$ , 其中 $`a`$ 和 $`b`$ 以 1 为步长分别从 $`- A`$ 取到 $`+ A`$ 以及从 $`- B`$ 取到 $`B`$ .
正如前面提到的, 厄米共轭通过方程(25.2.6)与 $`( B , A )`$ 表示下的算符相关联, 所以这些算符的反对易子必须采取如下的形式
$$
\begin{aligned}
\{ Q _ { a b } ^ { A B } , Q _ { a ^ { \prime } b ^ { \prime } } ^ { A B * } \}
&= ( - 1 ) ^ { A - a ^ { \prime } } ( - 1 ) ^ { B - b ^ { \prime } }
C ^ { c }{} _ { a , - b ^ { \prime } } ( C ; A B )
C ^ { d }{} _ { b , - a ^ { \prime } } ( D ; B A )
X _ { c d } ^ { C D } .
\end{aligned} \tag{25.2.12}
$$
<callout color="gray_bg">
	Codex 补充证明：方程(25.2.12)
	证明如下. 右边对允许的 $`C,D,c,d`$ 作 Clebsch-Gordan decomposition 中的求和. 由方程(25.2.6),
	$$
	Q _ { a ^ { \prime } b ^ { \prime } } ^ { A B * }
= ( - 1 ) ^ { A - a ^ { \prime } } ( - 1 ) ^ { B - b ^ { \prime } }
\bar Q _ { - b ^ { \prime } , - a ^ { \prime } } ^ { B A } .
	$$
	因此
	$$
	\{ Q _ { a b } ^ { A B } , Q _ { a ^ { \prime } b ^ { \prime } } ^ { A B * } \}
= ( - 1 ) ^ { A - a ^ { \prime } } ( - 1 ) ^ { B - b ^ { \prime } }
\{ Q _ { a b } ^ { A B } , \bar Q _ { - b ^ { \prime } , - a ^ { \prime } } ^ { B A } \} .
	$$
	在 $`\mathbf A`$ 这一个 $`S U ( 2 )`$ 上, 两个可耦合的指标是 $`a`$ 和 $`- b ^ { \prime }`$, 它们分别属于自旋 $`A`$ 和自旋 $`B`$. 所以
	$$
	| A a \rangle | B , - b ^ { \prime } \rangle
= C ^ { c }{} _ { a , - b ^ { \prime } } ( C ; A B ) | C c \rangle .
	$$
	在 $`\mathbf B`$ 这一个 $`S U ( 2 )`$ 上, 两个可耦合的指标是 $`b`$ 和 $`- a ^ { \prime }`$, 它们分别属于自旋 $`B`$ 和自旋 $`A`$. 所以
	$$
	| B b \rangle | A , - a ^ { \prime } \rangle
= C ^ { d }{} _ { b , - a ^ { \prime } } ( D ; B A ) | D d \rangle .
	$$
	这里第二个 Clebsch-Gordan 系数写成 $`( D ; B A )`$, 是为了让输入权重下标 $`b , - a ^ { \prime }`$ 的顺序与第二个 $`S U ( 2 )`$ 因子的实际 tensor-product order 一致; 若改用 $`( D ; A B )`$ 顺序, 则需要标准交换相位, 这相当于重新定义 $`X _ { c d } ^ { C D }`$ 的相位约定.
	于是任意按 $`( A , B ) \otimes ( B , A )`$ 变换的玻色算符都可以在不可约张量基中展开为
	$$
	\{ Q _ { a b } ^ { A B } , \bar Q _ { - b ^ { \prime } , - a ^ { \prime } } ^ { B A } \}
= C ^ { c }{} _ { a , - b ^ { \prime } } ( C ; A B )
C ^ { d }{} _ { b , - a ^ { \prime } } ( D ; B A )
X _ { c d } ^ { C D } .
	$$
	再代回前面的相位因子, 就得到方程(25.2.12).
</callout>
其中 $`C ^ { \sigma }{} _ { a b } ( j ; A B )`$ 是通常的 Clebsch-Gordan 系数, 它耦合了自旋 $`A`$ 和自旋 $`B`$ 的权重 $`a,b`$ 以形成自旋 $`j`$ 的权重 $`\sigma`$ , $`X _ { c d } ^ { C D }`$ 是按照齐次Lorentz 群的 $`( C , D )`$ 表示变换的算符的 $`( c , d )`$ -分量.
利用 Clebsch-Gordan 系数从所周知的幺正性, 我们可以将算符 $`X _ { c d } ^ { C D }`$ 表示成这些反对易子:
$$
\begin{aligned}
X _ { c d } ^ { C D }
&= ( - 1 ) ^ { A - a ^ { \prime } } ( - 1 ) ^ { B - b ^ { \prime } }
C ^ { c }{} _ { a , - b ^ { \prime } } ( C ; A B )
C ^ { d }{} _ { b , - a ^ { \prime } } ( D ; B A )
\left\{ Q _ { a b } ^ { A B } , Q _ { a ^ { \prime } b ^ { \prime } } ^ { A B * } \right\} .
\end{aligned} \tag{25.2.13}
$$
这些算符不一定都非零.
但是, 当 $`j = \sigma = A + B`$ 和 $`j = - \sigma = A + B`$ 时, 不为零的 Clebsch-Gordan 系数 $`C ^ { \sigma }{} _ { a b } ( j ; A B )`$ 分别只有那些 $`a = A`$ , $`b = B`$ 的和 $`a = - A`$ , $`b = - B`$ 的, 而这些系数的值均为1, 所以通过在方程中取 $`C = D = c = - d = A + B`$ , 我们发现
$$
X _ { A + B , - A - B } ^ { A + B , A + B } = ( - 1 ) ^ { 2 B } \left\{ Q _ { A , - B } ^ { A B } , Q _ { A , - B } ^ { A B * } \right\} . \tag{25.2.14}
$$
除非 $`Q _ { A , - B } ^ { A B } = 0`$ , 否则这不可能为零, 而 $`Q _ { A , - B } ^ { A B } = 0`$ (通过取 $`Q _ { A , - B } ^ { A B }`$ 与“下降”算符 $`A ^ { 1 } - \mathrm{i} A ^ { 2 }`$ 和“上升”算符 $`B ^ { 1 } + \mathrm{i} B ^ { 2 }`$ 的对易子)又暗示了所有 $`Q _ { a b } ^ { A B }`$ 为零.
因此, 如果存在任何不为零的 $`( A , B )`$ 费米生成元, 那么它们与共轭的反对易子至少必须要包含属于表示 $`( A + B , A + B )`$ 的非零玻色对称性生成元.
现在, Coleman-Mandula定理告诉我们, 组成玻色对称性生成元的是平移的 $`( 1 / 2 , 1 / 2 )`$ 生成元 $`P _ { \mu }`$ , 固有 Lorentz 变换的 $`( 1 , 0 ) \oplus ( 0 , 1 )`$ 生成元 $`J _ { \mu \nu }`$ , 以及可有可无的内部对称性的 $`( 0 , 0 )`$ 生成元 $`T _ { A }`$ (回顾一下, $`N`$ 阶对称无迹张量按照表示 $`( N / 2 , N / 2 )`$ 变换, 2 阶反对称张量按照表示 $`( 1 , 0 ) \oplus ( 0 , 1 )`$ 变换, 而 Dirac场按照表示 $`( 1 / 2 , 0 ) \oplus ( 0 , 1 / 2 )`$ 变换.) 因此费米对称性生成元只能属于 $`A + B \le 1 / 2`$ 的$`( A , B )`$ 表示.
这些算符将玻色子变成费米子并将费米子变成玻色子, 所以它们不能是标量, 这样只剩下了 $`( 1 / 2 , 0 )`$ 表示和 $`( 0 , 1 / 2 )`$ 表示, 正是所要证明的.
用 $`\mathcal{Q} ^ { \dot a r }`$ 标记线性独立的 $`( 0 , 1 / 2 )`$ 费米生成元, 反对易子 $`\{ \mathcal{Q} ^ { \dot a r } , \left( \mathcal{Q} ^ \dagger \right) ^ { b }{} _ { s } \}`$ 属于表示 $`( 0 , 1 / 2 ) \times ( 1 / 2 , 0 ) = ( 1 / 2 , 1 / 2 )`$ , 因此它只能正比于 $`( 1 / 2 , 1 / 2 )`$ 玻色对称性生成元, 即动量 4 -矢 $`P _ { \mu }`$ .
Lorentz不变性表明这个关系的形式必须是
$$
\left\{ \mathcal{Q} ^ { \dot a r } , \left( \mathcal{Q} ^ \dagger \right) ^ { b }{} _ { s } \right\} = - 2 N ^ { r }{} _ { s } \bar\sigma _ { \mu }{} ^ { \dot a b } P ^ { \mu } , \tag{25.2.15}
$$
其中 $`N ^ { r }{} _ { s }`$ 是数值矩阵.
为了看到这点, 我们使用2.7节讨论的Lorentz 群(或者更准确些, 它的覆盖群)与二维幺模复矩阵群 $`S L ( 2 , C )`$ 之间的同构.
Lorentz 变换 $`\Lambda ^ { \mu } { } _ { \nu }`$ 在 $`( 0 , 1 / 2 )`$ 费米生成元上的作用效果是
$$
U ^ { - 1 } ( \Lambda ) \mathcal{Q} ^ { \dot a r } U ( \Lambda ) = \lambda ^ { \dot a }{} _ { \dot b } \mathcal{Q} ^ { \dot b r } . \tag{25.2.16}
$$
其中 $`\Lambda`$ 是
$$
\lambda ^ { \dot a }{} _ { \dot c } \bar\sigma _ { \rho }{} ^ { \dot c c } ( \lambda ^ { \dagger } ) _ { c }{} ^ { b } = \bar\sigma _ { \mu }{} ^ { \dot a b } \Lambda ^ { \mu }{} _ { \rho } \tag{25.2.17}
$$
定义的 Lorentz 变换.
我们可以验证方程(25.2.16)对 $`( 0 , 1 / 2 )`$ 算符是成立的, 方法是, 注意到对于无限小 Lorentz 变换 $`\Lambda ^ { \mu } { } _ { \nu } = \delta ^ { \mu } { } _ { \nu } + \omega ^ { \mu } { } _ { \nu }`$ , 其中 $`\omega _ { \mu \nu } = \omega _ { \nu \mu }`$ , 方程(25.2.17)对
$$
\begin{array} { r } { \lambda = 1 + \frac { 1 } { 2 } \Big [ \frac { 1 } { 2 } \mathrm{i} \epsilon ^ { i j } { } _ { k } \omega _ { i j } + \omega _ { k 0 } \Big ] \sigma ^ { k } } \end{array}
$$
是满足的, 而此时†
$$
\begin{array} { r } { U ( \Lambda ) = 1 + \frac { 1 } { 2 } \mathrm{i} \omega _ { \mu \nu } J ^ { \mu \nu } = 1 + \frac { 1 } { 2 } \mathrm{i} \epsilon ^ { i j } { } _ { k } \omega _ { i j } J ^ { k } - \mathrm{i} \omega _ { i 0 } K ^ { i } . } \end{array}
$$
(这里重复的拉丁指标 $`i , j , k`$ 使用 Einstein convention.) 在这一情况下, 通过 $`\omega _ { i j }`$ 和 $`\omega _ { i 0 }`$ 在方程(25.2.16)两边的系数相等, 我们发现
$$
[ J ^ { i } , { \mathcal Q } ^ { \dot a } ] = - \frac { 1 } { 2 } ( \sigma ^ { i } ) ^ { \dot a }{} _ { \dot b } { \mathcal Q } ^ { \dot b } , \qquad [ K ^ { i } , { \mathcal Q } ^ { \dot a } ] = - \frac { 1 } { 2 } \mathrm{i} ( \sigma ^ { i } ) ^ { \dot a }{} _ { \dot b } { \mathcal Q } ^ { \dot b } ,
$$
或者等价的
$$
[ B ^ { i } , { \mathcal Q } ^ { \dot a } ] = - { \textstyle \frac { 1 } { 2 } } ( \sigma ^ { i } ) ^ { \dot a }{} _ { \dot b } { \mathcal Q } ^ { \dot b } , \qquad [ A ^ { i } , { \mathcal Q } ^ { \dot a } ] = 0 ,
$$
这表明满足方程(25.2.16)的算符属于 $`( 0 , 1 / 2 )`$ 表示.
现在, $`\bar\sigma _ { \mu }{} ^ { \dot a b }`$ 构成了 $`2 \times 2`$ 矩阵的一个完备集, 所以我们可以将反对易子 $`\{ \mathcal{Q} ^ { \dot a r } , \left( \mathcal{Q} ^ \dagger \right) ^ { b }{} _ { s } \}`$ 写成 $`N ^ { \mu }{} ^ { r }{} _ { s } \bar\sigma _ { \mu }{} ^ { \dot a b }`$ 的形式, 其中 $`N ^ { \mu }`$ 是算符的某个矩阵.
<callout color="gray_bg">
	Codex 补充推导：$`N^\mu`$ 的 Lorentz 变换
	方程(25.2.16)和(25.2.17)表明这些算符是 4 -矢. 具体地, 比较 $`N ^ { \mu } \bar\sigma _ { \mu }{} ^ { \dot a b }`$ 的变换给出
	$$
	\begin{aligned}
\bigl ( U ^ { - 1 } ( \Lambda ) N ^ { \mu } U ( \Lambda ) \bigr ) \bar\sigma _ { \mu }{} ^ { \dot a b }
&= N ^ { \rho } \lambda ^ { \dot a }{} _ { \dot c } \bar\sigma _ { \rho }{} ^ { \dot c c } ( \lambda ^ { \dagger } ) _ { c }{} ^ { b } \\
&= N ^ { \rho } \bar\sigma _ { \mu }{} ^ { \dot a b } \Lambda ^ { \mu }{} _ { \rho } \\
&= \bigl ( \Lambda ^ { \mu }{} _ { \rho } N ^ { \rho } \bigr ) \bar\sigma _ { \mu }{} ^ { \dot a b } ,
\end{aligned}
	$$
	所以 $`U ^ { - 1 } ( \Lambda ) N ^ { \mu } U ( \Lambda ) = \Lambda ^ { \mu }{} _ { \nu } N ^ { \nu }`$ . 那么根据 Coleman-Mandula定理它们只能正比于玻色对称性算符中的唯一4 -矢, $`P ^ { \mu }`$ .
	令 $`N ^ { \mu }{} ^ { r }{} _ { s } = - 2 P ^ { \mu } N ^ { r }{} _ { s }`$ 就给出了方程(25.2.15).
</callout>
下面的 normalization 继续使用 translated spinor-index notation. 只有从方程(25.2.18)开始的 Clebsch-Gordan weight calculation 临时沿用 Weinberg 的 source-label notation: $`\mathcal Q _ { a r }`$ 表示同一个 $`(0,1/2)`$ generator, 对应翻译后记号 $`\mathcal Q ^ { \dot a r }`$, 而 $`\mathcal Q _ { a r } ^ *`$ 对应 $`\left( \mathcal Q ^ \dagger \right) ^ a{} _ r`$.
现在我们要对 $`\mathcal{Q} ^ { \dot a r }`$ 做一个线性变换使得它们的反对易子是(25.2.7)的形式.
为了这个目的, 我们需要构建厄米且正定的矩阵 $`N ^ { r }{} _ { s }`$ .
通过取方程(25.2.15)的厄米共轭我们可以立刻得出 $`N ^ { r }{} _ { s }`$ 是厄米的.
为了看到它是正定的, 回忆 $`\mathcal{Q} ^ { \dot a r }`$ 是被取成线性独立的. 写
$`P ^ { \dot a b } \equiv - \bar\sigma _ { \mu }{} ^ { \dot a b } P ^ { \mu }`$, 那么对于任何非零的线性组合
$`\mathcal{Q} \equiv d _ { \dot a } c _ { r } \mathcal{Q} ^ { \dot a r }`$ , 必存在某个 $`\mathcal{Q}`$ 湮灭不了的态 $`| \Psi \rangle`$ .
取方程(25.2.15)在这个态上的期望值, 这给出
$$
2 d _ { \dot a } \langle \Psi | P ^ { \dot a b } | \Psi \rangle d ^ { \dagger } _ { b } c _ { r } N ^ { r }{} _ { s } c ^ { \dagger }{} ^ { s }
= \langle \Psi | \{ \mathcal{Q} , \mathcal{Q} ^ { \dagger } \} | \Psi \rangle > 0 .
$$
<callout color="gray_bg">
	Codex 补充证明：positivity
	这里的 positivity 是 Hilbert-space norm positivity:
	$$
	\begin{aligned}
\langle \Psi | \{ \mathcal{Q} , \mathcal{Q} ^ { \dagger } \} | \Psi \rangle
&= \langle \Psi | \mathcal{Q} \mathcal{Q} ^ { \dagger } | \Psi \rangle
+ \langle \Psi | \mathcal{Q} ^ { \dagger } \mathcal{Q} | \Psi \rangle \\
&= \| \mathcal{Q} ^ { \dagger } | \Psi \rangle \| ^ { 2 }
+ \| \mathcal{Q} | \Psi \rangle \| ^ { 2 } .
\end{aligned}
	$$
	因为 $`\mathcal{Q}`$ 是非零线性组合, 可以取 $`|\Psi\rangle`$ 使 $`\mathcal{Q}|\Psi\rangle \neq 0`$, 所以右边严格大于零.
</callout>
由此可以立刻得出, 对于任何不全为零的 $`c _ { r }`$ , $`c _ { r } N ^ { r }{} _ { s } c ^ { \dagger }{} ^ { s }`$ 必不为零, 所以 $`N ^ { r }{} _ { s }`$ 不是正定的就是负定的.
在 $`- P ^ { \mu } P _ { \mu } \ge 0`$ 且 $`P ^ { 0 } > 0`$ 的物理态的空间上, 算符 $`d _ { \dot a } P ^ { \dot a b } d ^ { \dagger } _ { b }`$ 是正定的, 所以矩阵 $`N ^ { r }{} _ { s }`$ 也必须是正定的.††
现在我们可以定义新的费米生成元
$$
\mathcal{Q} ^ { \prime \dot a r } \equiv \left( N ^ { - 1 / 2 } \right) ^ { r }{} _ { s } \mathcal{Q} ^ { \dot a s } ,
$$
使得反对易子取如下的形式
$$
\left\{ { \mathcal{Q} } ^ { \prime \dot a r } , \left( { \mathcal{Q} } ^ { \prime \dagger } \right) ^ { b }{} _ { s } \right\} = - 2 \delta ^ { r }{} _ { s } \bar\sigma _ { \mu }{} ^ { \dot a b } P ^ { \mu } .
$$
从现在起, 我们将假定所有费米生成元都以这种方式定义并去掉撇号, 使得方程(25.2.7)成立.
接下来我们必须要证明 $`\mathcal{Q} ^ { \dot a r }`$ 与动量4 -矢 $`P _ { \mu }`$ 对易. 为了直接使用 Clebsch-Gordan weight components, 从下一式开始到方程(25.2.29)临时写回 Weinberg source-label notation.
$`P _ { \mu }`$ 这样的 $`( 1 / 2 , 1 / 2 )`$ 算符与 $`\mathcal{Q}`$ 这样的 $`( 0 , 1 / 2 )`$ 算符, 它们的对易子只能是 $`( 1 / 2 , 0 )`$ 算符或 $`( 1 / 2 , 1 )`$ 算符, 但是我们看到不存在 $`( 1 / 2 , 1 )`$ 对称性生成元,所以 $`P _ { \mu }`$ 与 $`\mathcal{Q}`$ 的对易子只能正比于 $`( 1 / 2 , 0 )`$ 对称性生成元 $`\mathcal{Q} ^ { \ast }`$ .
Lorentz不变性要求这个关系取如下的形式
$$
[ \mathcal { M } _ { a b } , \mathcal{Q} _ { c r } ] = e _ { a c } K _ { r }{}^{ s } \mathcal{Q} _ { b s } ^ { * } . \tag{25.2.18}
$$
其中 $`K`$ 是一数值矩阵, $`\mathcal{M}`$ 是算符矩阵
$$
\mathcal { M } \equiv \sigma _ { \mu } P ^ { \mu } . \tag{25.2.19}
$$
(矩阵 $`e _ { a c }`$ 是将两个自旋 $`1 / 2`$ 耦合成零自旋的 Clebsch-Gordan系数.) 由此可以直接得出
$$
\left[ \mathcal { M } _ { - \frac { 1 } { 2 } , - \frac { 1 } { 2 } } , \left[ \mathcal { M } _ { - \frac { 1 } { 2 } , - \frac { 1 } { 2 } } , \{ \mathcal{Q} _ { \frac { 1 } { 2 } r } , \mathcal{Q} _ { \frac { 1 } { 2 } s } ^ { * } \} \right] \right]
= - 4 \mathcal { M } _ { - \frac { 1 } { 2 } , - \frac { 1 } { 2 } } ( K K ^ { \dagger } ) _ { r s } . \tag{25.2.20}
$$
<callout color="gray_bg">
	Codex 补充计算：方程(25.2.20)
	这个 double commutator 的展开如下. 令 $`m=-1/2`$, $`p=+1/2`$, $`\mathcal M=\mathcal M_{mm}`$. 因为 $`e_{mp}=-1`$, 方程(25.2.18)给出
	$$
	\begin{aligned}
[ \mathcal M , \mathcal Q _ { p r } ]
&= - K _ { r }{}^{ t } \mathcal Q _ { m t } ^ { * } ,\\
[ \mathcal M , \mathcal Q _ { p s } ^ { * } ]
&= K _ { s }{}^{ u * } \mathcal Q _ { m u } ,\\
[ \mathcal M , \mathcal Q _ { m u } ]
&= [ \mathcal M , \mathcal Q _ { m t } ^ { * } ] = 0 .
\end{aligned}
	$$
	因此
	$$
	\begin{aligned}
[ \mathcal M , \{ \mathcal Q _ { p r } , \mathcal Q _ { p s } ^ { * } \} ]
&= \{ [ \mathcal M , \mathcal Q _ { p r } ] , \mathcal Q _ { p s } ^ { * } \}
+ \{ \mathcal Q _ { p r } , [ \mathcal M , \mathcal Q _ { p s } ^ { * } ] \} \\
&= - K _ { r }{}^{ t } \{ \mathcal Q _ { m t } ^ { * } , \mathcal Q _ { p s } ^ { * } \}
+ K _ { s }{}^{ u * } \{ \mathcal Q _ { p r } , \mathcal Q _ { m u } \} .
\end{aligned}
	$$
	再对 $`\mathcal M`$ 对易一次:
	$$
	\begin{aligned}
[ \mathcal M , [ \mathcal M , \{ \mathcal Q _ { p r } , \mathcal Q _ { p s } ^ { * } \} ] ]
&= - K _ { r }{}^{ t } K _ { s }{}^{ u * }
\{ \mathcal Q _ { m t } ^ { * } , \mathcal Q _ { m u } \}
- K _ { s }{}^{ u * } K _ { r }{}^{ t }
\{ \mathcal Q _ { m t } ^ { * } , \mathcal Q _ { m u } \} \\
&= - 2 K _ { r }{}^{ t } K _ { s }{}^{ u * }
\{ \mathcal Q _ { m t } ^ { * } , \mathcal Q _ { m u } \} \\
&= - 4 K _ { r }{}^{ t } K _ { s }{}^{ t * } \mathcal M _ { m m } \\
&= - 4 \mathcal M _ { m m } ( K K ^ { \dagger } ) _ { r s } .
\end{aligned}
	$$
	这里最后一步用了方程(25.2.7)的 $`a=b=m`$ 分量, 即 $`\{ \mathcal Q _ { m u } , \mathcal Q _ { m t } ^ { * } \}=2\delta_{ut}\mathcal M_{mm}`$.
</callout>
利用方程(25.2.7), 左边是多重对易子 $`\left[ P _ { \mu } , \left[ P _ { \nu } , P _ { \lambda } \right] \right]`$ 的线性组合, 所有这样的对易子都为零, 而 $`\mathcal{M} _ { - 1 / 2 - 1 / 2 }`$ 对于一般的动量不为零, 所以 $`K K ^ { \dagger } = 0`$ , 因此 $`K = 0`$ , 加上方程(25.2.18), 这表明 $`[ P _ { \mu } , \mathcal{Q} _ { a r } ] = 0`$ .
复共轭给出 $`[ P _ { \mu } , \mathcal{Q} _ { a r } ^ { * } ] = 0`$ .
现在我们可以着手处理两个 $`\mathcal{Q}`$ 的反对易子.
两个 $`( 0 , 1 / 2 )`$ 对称性算符的反对易子必须是 $`( 0 , 1 )`$ 对称性生成元和 $`( 0 , 0 )`$ 对称性生成元的线性组合.
Coleman-Mandula定理告诉我们唯一的 $`( 0 , 1 )`$ 对称性生成元是固有齐次 Lorentz 变换的生成元 $`J _ { \nu \lambda }`$ 的线性组合, 但由于 $`\mathcal{Q}`$ 与 $`P _ { \mu }`$ 对易, 继而它们的反对易子也与 $`P _ { \mu }`$ 对易, 而方程(2.4.13)告诉我们 $`J _ { \nu \lambda }`$ 的线性组合与 $`P _ { \mu }`$ 不对易.
这样就只剩下了 $`( 0 , 0 )`$ 算符, 它既与 $`P _ { \mu }`$ 对易又与 $`J _ { \nu \lambda }`$ 对易.
这样, Lorentz不变性就会要求 $`\mathcal{Q}`$ 之间的反对易子必须采取方程(25.2.8)的形式.
内部对称性生成元 $`Z _ { r s }`$ 关于 $`r`$ 和 $`s`$ 是反对称的, 这是因为整个表达式必须在 $`r`$ 与$`s`$ 和 $`a`$ 与 $`b`$ 的交换下是对称的, 而矩阵 $`e _ { a b }`$ 关于 $`a`$ 和 $`b`$ 是反对称的.
剩下来要证明的是 $`Z`$ 是中心荷.
从方程(25.2.8)和(25.2.10)立即可以得出
$$
[ P _ { \mu } , Z _ { r s } ] = 0 . \tag{25.2.21}
$$
接下来考察包含两个 $`\mathcal{Q}`$ 和一个 $`\mathcal{Q} ^ { \ast }`$ 的推广 Jacobi 恒等式(25.1.5):
$$
0 = [ \{ \mathcal{Q} _ { a r } , \mathcal{Q} _ { b s } \} , \mathcal{Q} _ { c t } ^ { * } ] + [ \{ \mathcal{Q} _ { b s } , \mathcal{Q} _ { c t } ^ { * } \} , \mathcal{Q} _ { a r } ] + [ \{ \mathcal{Q} _ { c t } ^ { * } , \mathcal{Q} _ { a r } \} , \mathcal{Q} _ { b s } ] .
$$
方程(25.2.7)和(25.2.10)表明第二项和第三项为零, 所以
$$
[ Z _ { r s } , \mathcal{Q} _ { c t } ^ { * } ] = 0 . \tag{25.2.22}
$$
最后, 考察一个 $`Z`$ , 一个 $`\mathcal{Q}`$ 和一个 $`\mathcal{Q} ^ { \ast }`$ 的推广 Jacobi 恒等式:
$$
0 = - [ Z _ { r s } , \{ \mathcal{Q} _ { a t } , \mathcal{Q} _ { b u } ^ { * } \} ] + \{ \mathcal{Q} _ { b u } ^ { * } , [ Z _ { r s } , \mathcal{Q} _ { a t } ] \} - \{ \mathcal{Q} _ { a t } , [ \mathcal{Q} _ { b u } ^ { * } , Z _ { r s } ] \} .
$$
第一项和第三项分别因为方程(25.2.21)和(25.2.22)为零, 所以我们只剩下了第二项
$$
\left\{ \mathcal{Q} _ { b u } ^ { * } , [ Z _ { r s } , \mathcal{Q} _ { a t } ] \right\} = 0 . \tag{25.2.23}
$$
现在, $`[ Z _ { r s } , \mathcal{Q} _ { a t } ]`$ 是 $`( 0 , 1 / 2 )`$ 对称性生成元, 所以它必须是 $`\mathcal{Q}`$ 的线性组合:
$$
[ Z _ { r s } , \mathcal{Q} _ { a t } ] = M _ { r s t }{}^{ u } \mathcal{Q} _ { a u } . \tag{25.2.24}
$$
那么对于所有 $`a , b , r , s , t`$ 和 $`u`$ , 方程(25.2.23)就变成
$$
( \sigma _ { \mu } ) _ { a b } P ^ { \mu } M _ { r s t u } = 0 .
$$
由于算符 $`( \sigma _ { \mu } ) _ { a b } P ^ { \mu }`$ 不为零, 我们得出 $`M _ { r s t u } = 0`$ , 这使得
$$
[ Z _ { r s } , \mathcal{Q} _ { a t } ] = 0 . \tag{25.2.25}
$$
利用反对易关系(25.2.8)和它的共轭, 再加上对易关系(25.2.22)和(25.2.25)与它们的共轭, 这给出
$$
[ Z _ { r s } , Z _ { t u } ] = [ Z _ { r s } , Z _ { t u } ^ { * } ] = [ Z _ { r s } ^ { * } , Z _ { t u } ^ { * } ] = 0 . \tag{25.2.26}
$$
这完成了方程(25.2.11)的证明, 有了这个也就证明了 Haag-Lopuszanski-Sohnius 定理.
当然, $`Z _ { r s }`$ 是超对称代数的中心荷这一点并不会排除还存在其它阿贝尔或非阿贝尔内部对称性的可能性.
设 $`T _ { A }`$ 张开了玻色内部对称性的整个 Lie 代数.
那么 $`[ T _ { A } , \mathcal{Q} _ { a r } ]`$ 就是 $`( 0 , 1 / 2 )`$ 算符, 所以它必须是 $`\mathcal{Q}`$ 的线性组合:
$$
[ T _ { A } , \mathcal{Q} _ { a r } ] = - ( t _ { A } ) _ { r }{}^{ s } \mathcal{Q} _ { a s } . \tag{25.2.27}
$$
从两个 $`T`$ 和一个 $`\mathcal{Q}`$ 的Jacobi恒等式, 我们可以得知 $`t _ { A }`$ 矩阵构成了内部对对称性代数的一个表示
$$
[ t _ { A } , t _ { B } ] = \mathrm { i } C _ { A B }{}^{ C } t _ { C } , \tag{25.2.28}
$$
其中系数 $`C _ { A B } { } ^ { C }`$ 是内部对称性代数的结构常数
$$
[ T _ { A } , T _ { B } ] = \mathrm { i } C _ { A B }{}^{ C } T _ { C } . \tag{25.2.29}
$$
这样, $`Z _ { r s }`$ 不仅是 $`\mathcal{Q}`$ , $`\mathcal{Q} ^ { \ast }`$ , $`P _ { \mu }`$ , $`Z`$ 和 $`Z ^ { \ast }`$ 构成的超代数的中心荷, 同时还是包含所有 $`T _ { A }`$ 的更大的超代数的中心荷.
为了看到这点, 从方程(25.2.27)和(25.2.8)中注意到
$$
[ { \cal T } _ { \cal A } , { \cal Z } _ { r s } ] = - ( t _ { \cal A } ) _ { r } { } ^ { r ^ { \prime } } { \cal Z } _ { r ^ { \prime } s } - ( t _ { \cal A } ) _ { s } { } ^ { s ^ { \prime } } { \cal Z } _ { r s ^ { \prime } } ,
$$
所以 $`Z _ { r s }`$ 构成了整个玻色对称性代数的一个不变阿贝尔子代数.
但是回顾 Coleman-Mandula 定理的证明, 我们发现内部玻色对称性的整个 Lie 代数, 在这里就是 $`T _ { A }`$ 张开的 Lie 代数, 它同构于一个紧致半单 Lie 代数和几个 $`U ( 1 )`$ 代数的直和.
这种 Lie 代数的不变阿贝尔子代数只有那些 $`U ( 1 )`$ 生成元张开的, 所以 $`Z _ { r s }`$ 必须是 $`U ( 1 )`$ 生成元, 因而与所有 $`T _ { A }`$ 对易.
即使 $`Z`$ 与所有对称性算符都对易, 它们也不只是个数; 它们是量子算符, 它们的值可能随着态的变化而变化.
事实上, 对于超对称真空态, 由于它被所有超对称性生成元湮灭, $`Z`$ 显然必须在这个态上取零值, 但是一般而言它们不需要为零.
在27.9节, 我们将看到如何在有扩充超对称性的规范理论中计算 $`Z`$ .
在没有中心荷的情况下, 超对称代数(25.2.7), (25.2.8)在内部对称群 $`U ( N )`$ 下不变
$$
\mathcal{Q} ^ { \dot a r } \mapsto V ^ { r }{} _ { s } \mathcal{Q} ^ { \dot a s } , \tag{25.2.30}
$$
其中 $`V ^ { r }{} _ { s }`$ 是 $`N \times N`$ 幺正(不一定幺模)矩阵.
这被称为 $`R`$ -对称性.
这个对称性可能是也可能不是一个好对称性, 如果它是, 那么它可能被反常破坏也可能自发破缺, 或者它就是自然的一个好对称性.
$`r , s`$ 等指标的取值 $`N > 1`$ 的超对称代数被称为 $`N`$ -扩充超对称性.
当只有一个 $`\mathcal{Q}`$ 时, $`Z ^ { r s } = - Z ^ { s r }`$ 的条件告诉我们 $`Z`$ 为零, 这给出了反对易关系的一个更加简单的形式
$$
\{ \mathcal{Q} ^ { \dot a } , \left( \mathcal{Q} ^ \dagger \right) ^ { b } \} = - 2 \bar\sigma _ { \mu }{} ^ { \dot a b } P ^ { \mu } , \tag{25.2.31}
$$
$$
\{ \mathcal{Q} ^ { \dot a } , \mathcal{Q} ^ { \dot b } \} = 0 . \tag{25.2.32}
$$
这种情况被称为简单超对称, 或者 $`N = 1`$ 超对称.
在这一情况下, $`R`$ -对称变换是 $`U ( 1 )`$ 相位变换
$$
\mathcal{Q} ^ { \dot a } \mapsto \exp ( \mathrm { i } \varphi ) \mathcal{Q} ^ { \dot a } . \tag{25.2.33}
$$
其中 $`\varphi`$ 是一个实相位.
为了多个目的, 将 $`( 0 , 1 / 2 )`$ 算符 $`\mathcal{Q} ^ { \dot a r }`$ 与 $`( 1 / 2 , 0 )`$ 共轭算符 $`\left( \mathcal{Q} ^ \dagger \right) ^ a{} _ r`$ 相结合写成 4 分量 Majorana 旋量生成元 $`Q _ { r \alpha }`$ 将是方便的. 令 $`\alpha`$ 的上半块是 undotted $`a`$, 下半块是 dotted $`\dot a`$. 因为 $`Q _ { r \alpha }`$ 是 lower Dirac spinor, 上半块必须先用 $`\epsilon _ { a b }`$ 降指标:
$`\left( \mathcal{Q} ^ \dagger \right) _ { a r } \equiv \epsilon _ { a b } \left( \mathcal{Q} ^ \dagger \right) ^ b{} _ r`$. 因此 $`Q`$ 定义成
$$
Q _ { r \alpha } \equiv \begin{pmatrix} \left( \mathcal{Q} ^ \dagger \right) _ { a r } \\ \mathcal{Q} ^ { \dot a r } \end{pmatrix} _ { \alpha } . \tag{25.2.34}
$$
也就是说, $`Q _ { r \alpha }`$ 是 lower spinor; 它的上半块是 $`(1/2,0)`$ Weyl conjugate 的 lowered form, 它的 Dirac adjoint $`\overline Q{}^\alpha`$ 是 upper spinor, defined as usual by $`Q^\dagger\beta`$ with the same internal label.
这是一个 Majorana 旋量, 也就是说
$$
Q _ { r } = \beta C Q _ { r } ^ { * } , \qquad C \equiv \epsilon \gamma _ { 5 } ,
$$
这里 $`\beta`$ 交换两个 Weyl blocks, 而 $`C`$ 是 spinor metric block. 带指标地说, 在 $`Q _ r ^ *`$ 自然携带的 Weyl 顺序 $`(\dot a , a)`$ 中,
$$
C = \epsilon \gamma _ { 5 }
= \begin{pmatrix} e&0\\0&-e\end{pmatrix}
= \begin{pmatrix}
\epsilon ^ { \dot a \dot b }&0\\
0&\epsilon _ { a b }
\end{pmatrix} _ { ( \dot a , a ) } .
$$
其中 $`\beta , \epsilon`$ 和 $`\gamma _ { 5 }`$ 是 $`4 \times 4`$ 矩阵, 它们可以写成 $`2 \times 2`$ 分块矩阵:
$$
\beta = \begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \epsilon = \begin{pmatrix}e&0\\0&e\end{pmatrix},\qquad \gamma _ { 5 } = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
(第 26 章的附录将会回顾 Majorana 旋量的性质.) 选择(25.2.34)的形式是为了与齐次 Lorentz 群通常的4分量Dirac表示的记法一致, 根据方程(5.4.4), 在这个表示中旋转和增速生成元按照方程(5.4.19)和(5.4.20)被表示成
$$
\mathcal { J } _ { i } = \frac { 1 } { 2 } \begin{pmatrix} \sigma _ { i } & 0 \\ 0 & \sigma _ { i } \end{pmatrix} , \qquad
\mathcal { K } _ { i } = - \frac { \mathrm { i } } { 2 } \begin{pmatrix} \sigma _ { i } & 0 \\ 0 & - \sigma _ { i } \end{pmatrix} . \tag{25.2.35}
$$
再加上方程(25.2.1), 这表明 $`\mathbf{A}`$ 和 $`\mathbf{B}`$ 分别只作用在Dirac旋量的前两个分量和后两个分量上, 这就是为什么我们将 $`( 0 , 1 / 2 )`$ 算符 $`\mathcal{Q} ^ { \dot a r }`$ 用作方程(25.2.34)的下分量而不是上分量
在这个 4 分量记法中, 简单超对称的基础反对易关系(25.2.31)和(25.2.32)写成
$$
\{ Q _ { \alpha } , \overline { Q }{} ^ { \beta } \}
= 2 \begin{pmatrix} 0 & - e ( - \bar\sigma _ { \mu } P ^ { \mu } ) ^ { \mathrm { T } } e \\ - \bar\sigma _ { \mu } P ^ { \mu } & 0 \end{pmatrix}
= + 2 \mathrm { i } P _ { \mu } ( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta } . \tag{25.2.36}
$$
本卷的前言部分回顾了我们使用了Dirac 矩阵的约定; 这里我们仅需要记起
$$
( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta }
= \mathrm { i } \begin{pmatrix}
0&\sigma ^ { \mu }{} _ { a \dot b }\\
\bar\sigma ^ { \mu }{} ^ { \dot a b }&0
\end{pmatrix} _ { \alpha }{} ^ { \beta } ,
\qquad
\sigma ^ { \mu }{} _ { a \dot a } = ( \mathbf 1 , \sigma ^ i ) _ { a \dot a } , \qquad
\bar\sigma ^ { \mu }{} ^ { \dot a a } = ( \mathbf 1 , - \sigma ^ i ) ^ { \dot a a } . \tag{25.2.37}
$$
这里 $`- \bar\sigma _ { \mu }{} ^ { \dot a a } P ^ { \mu } = P ^ 0 \mathbf 1 + P ^ i \sigma _ i`$. 另外使用方程(25.2.9)后的 $`e`$-matrix identities.
<callout color="gray_bg">
	Codex 补充计算：方程(25.2.36) 的 block-matrix check
	这里的 block-matrix equality 可直接检查. 由 $`P_0=-P^0`$, $`P_i=P^i`$, $`\bar\sigma^\mu=(\mathbf 1,-\sigma^i)`$, $`\sigma^\mu=(\mathbf 1,\sigma^i)`$ 以及上面的 $`e`$-identity,
	$$
	\begin{aligned}
- e ( - \bar\sigma _ { \mu } P ^ { \mu } ) ^ { \mathrm T } e
&= - P ^ { 0 } e \sigma _ { 0 } e
- P ^ { i } e ( \sigma _ { i } ) ^ { \mathrm T } e \\
&= P ^ { 0 } \sigma _ { 0 } - P ^ { i } \sigma _ { i } ,
\end{aligned}
	$$
	$$
	\begin{aligned}
+ 2 \mathrm i P _ { \mu } ( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta }
&= - 2 P _ { \mu }
\begin{pmatrix}
0&\sigma^\mu\\
\bar\sigma^\mu&0
\end{pmatrix} _ { \alpha }{} ^ { \beta } \\
&= 2
\begin{pmatrix}
0&P^0\sigma_0-P^i\sigma_i\\
P^0\sigma_0+P^i\sigma_i&0
\end{pmatrix} _ { \alpha }{} ^ { \beta } \\
&=2\begin{pmatrix}
0 & -e(-\bar\sigma_\mu P^\mu)^{\mathrm T}e\\
-\bar\sigma_\mu P^\mu & 0
\end{pmatrix} _ { \alpha }{} ^ { \beta } .
\end{aligned}
	$$
</callout>
在扩充超对称的情况下, 中心荷的出现会改变这个公式; 取代方程(25.2.36), 我们有
$$
\{ Q _ { r \alpha } , \overline { Q } _ { s }{} ^ { \beta } \}
= + 2 \mathrm { i } P _ { \mu } ( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta } \delta _ { r s }
+ \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) _ { \alpha }{} ^ { \beta } Z ^ { * }{} _ { s r }
+ \left( \frac { 1 - \gamma _ { 5 } } { 2 } \right) _ { \alpha }{} ^ { \beta } Z ^ { r s } . \tag{25.2.38}
$$
这里给出的分析针对的是时空维数为4的情况, 在第32章, 我们将对一般的时空维数以一种不太显式的形式重复这个分析.
在那里我们将会看到, 在高维时空中, 即使理论中有扩充的量使得可以构造出Coleman-Mandula定理允许范围以外的玻色对称性生成元, 超对称性生成元也总是属于高维Lorentz 群的基础旋量表示.
在无质量的理论中, 对于那些在共形对称性代数(24.B.34)—(24.B.35)下不变的理论, 存在两个额外的能够出现在超对称反对易关系右边的对称性生成元, $`D`$ 和 $`K _ { \mu }`$ .
这些新生成元分别拥有标量和矢量的 Lorentz 变换性质, 就像 $`Z ^ { r s }`$ 和 $`P _ { \mu }`$ , 所以和前面一样, 费米生成元必须属于 Lorentz代数的基础 $`( 1 / 2 , 0 )`$ 旋量表示, 而它的共轭必须属于 $`( 0 , 1 / 2 )`$ 表示.
同时, 根据所有这些元与伸缩生成元 $`D`$ 的对易关系对它们进行分类是方便的; 如果一个算符 $`X`$ 有
$$
[ X , D ] = - \mathrm { i } a X , \tag{25.2.39}
$$
那就称它有量纲 $`a`$ .
对方程(24.B.34)的观察表明玻色对称性生成元 $`J ^ { \mu \nu }`$ , $`P ^ { \mu }`$ , $`K ^ { \mu }`$ 和 $`D`$ 分别拥有量纲 0, $`+ 1`$ , $`- 1`$ 和0. 另外, 对于任何内部对称性的Lie群, 它的生成元的量纲为零.
量纲为 $`a`$ 的费米生成元与它的共轭的反对易子是量纲为 $`2 a`$ 的正定玻色算符, 又因为正定玻色对称性生成元只能是 $`P _ { \mu }`$ 分量和 $`K _ { \mu }`$ 分量的线性组合, 费米对称性算符只能有量纲 $`+ 1 / 2`$ 和 $`- 1 / 2`$ .
量纲 $`1 / 2`$ 的 $`( 0 , 1 / 2 )`$ 费米对称性算符和它们的共轭可以再次被装配成Majorana 旋量 $`Q _ { r \alpha }`$ , 并满足
$$
\{ Q _ { r \alpha } , \overline { Q } _ { s }{} ^ { \beta } \} = + 2 \mathrm { i } P _ { \mu } ( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta } \delta _ { r s } , \tag{25.2.40}
$$
$$
[ P _ { \mu } , Q _ { r \alpha } ] = 0 , \tag{25.2.41}
$$
$$
[ D , Q _ { r \alpha } ] = + \frac { \mathrm { i } } { 2 } Q _ { r \alpha } . \tag{25.2.42}
$$
(注意, 因为中心荷的量纲是 0 而不是 $`+ 1`$ , 这里是不允许存在中心荷的.) $`K _ { \mu }`$ 与 $`Q _ { r \alpha }`$ 的对易子是Majorana 费米对称性生成元 $`Q _ { r \alpha } ^ { \sharp }`$ 的线性组合, Lorentz不变性使得我们可以将它写成如下形式
$$
[ K ^ { \mu } , Q _ { r \alpha } ] = \mathrm { i } ( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta } Q _ { r \beta } ^ { \sharp } . \tag{25.2.43}
$$
(右边的一个任意因子已经被吸收进 $`Q _ { r \beta } ^ { \sharp }`$ 的定义中.
对右边的相位已经进行了选择, 使得 $`Q _ { r \beta } ^ { \sharp }`$ 满足 Majorana 旋量的标准实条件(26.A.2).) $`Q _ { r \beta } ^ { \sharp }`$ 的量纲是 $`+ 1 / 2 - 1 = - 1 / 2`$ , 所以
$$
[ D , Q _ { r \alpha } ^ { \sharp } ] = - \frac { \mathrm { i } } { 2 } Q _ { r \alpha } ^ { \sharp } . \tag{25.2.44}
$$
取方程(25.2.43)与 $`P ^ { \nu }`$ 的对易子并使用方程(24.B.34)给出的 $`K ^ { \mu }`$ 和 $`P ^ { \nu }`$ 的对易关系, 这给出
$$
[ P ^ { \nu } , Q _ { r \alpha } ^ { \sharp } ] = - \mathrm { i } ( \gamma ^ { \nu } ) _ { \alpha }{} ^ { \beta } Q _ { r \beta } . \tag{25.2.45}
$$
我们看到 $`Q`$ 与 $`Q ^ { \sharp }`$ 是相联系的.
通过取反对易关系(25.2.40)与 $`K _ { \mu }`$ 的对易子, 我们发现了 $`Q ^ { \sharp }`$ 与 $`Q`$ 的反对易子:
$$
\{ Q _ { r \alpha } ^ { \sharp } , \overline { Q } _ { s }{} ^ { \beta } \}
= + 2 \mathrm { i } D \delta _ { r s } \delta _ { \alpha }{} ^ { \beta }
- 2 J _ { \mu \nu } \delta _ { r s } \mathcal { J } ^ { \mu \nu } _ { \alpha }{} ^ { \beta }
+ O _ { r s } \delta _ { \alpha }{} ^ { \beta }
+ O _ { r s } ^ { \prime } ( \gamma _ { 5 } ) _ { \alpha }{} ^ { \beta } . \tag{25.2.46}
$$
其中 $`{ \mathcal{J} } ^ { \mu \nu } _ { \alpha }{} ^ { \beta } = - \mathrm{i} [ \gamma ^ { \mu } , \gamma ^ { \nu } ] _ { \alpha }{} ^ { \beta } / 4 , O _ { r s }`$ 和 $`O _ { r s } ^ { \prime }`$ 是量纲为零的 Lorentz不变算符, 并满足
$$
O _ { r s } = - O _ { s r } , \qquad O _ { r s } ^ { \prime } = + O _ { s r } ^ { \prime } . \tag{25.2.47}
$$
<callout color="gray_bg">
	Codex 补充证明：方程(25.2.46)—(25.2.47)
	令
	$$
	A _ { r s \alpha }{} ^ { \beta }
\equiv
\{ Q _ { r \alpha } ^ { \sharp } , \overline Q _ s{} ^ \beta \}.
	$$
	由于 $`Q^\sharp`$ 的 dimension 是 $`-1/2`$, 而 $`\overline Q`$ 的 dimension 是 $`+1/2`$, $`A`$ 是 dimension-zero bosonic operator. Lorentz covariance 只允许 dimension-zero scalar, antisymmetric tensor, and internal scalar pieces, 所以先写成
	$$
	A _ { r s \alpha }{} ^ { \beta }
= a D \delta _ { r s } \delta _ \alpha{} ^ \beta
+ b J _ { \mu \rho } \delta _ { r s } \mathcal J ^ { \mu \rho } _ \alpha{} ^ \beta
+ O _ { r s } \delta _ \alpha{} ^ \beta
+ O _ { r s } ^ \prime ( \gamma _ 5 ) _ \alpha{} ^ \beta .
	$$
	其中 $`a,b`$ 是数值常数, 而 $`O,O'`$ 与 $`P^\nu`$ 对易. 用方程(25.2.45)和(25.2.40)计算左边的 $`P^\nu`$-commutator:
	$$
	\begin{aligned}
[ P ^ \nu , A _ { r s \alpha }{} ^ \beta ]
&=
\{ [ P ^ \nu , Q _ { r \alpha } ^ \sharp ] , \overline Q _ s{} ^ \beta \}
+ \{ Q _ { r \alpha } ^ \sharp , [ P ^ \nu , \overline Q _ s{} ^ \beta ] \} \\
&=
- \mathrm i ( \gamma ^ \nu ) _ \alpha{} ^ \gamma
\{ Q _ { r \gamma } , \overline Q _ s{} ^ \beta \} \\
&=
- \mathrm i ( \gamma ^ \nu ) _ \alpha{} ^ \gamma
 \Bigl [ + 2 \mathrm i P _ \rho ( \gamma ^ \rho ) _ \gamma{} ^ \beta \delta _ { r s } \Bigr ] \\
&=
+2 P _ \rho
( \gamma ^ \nu \gamma ^ \rho ) _ \alpha{} ^ \beta \delta _ { r s } .
\end{aligned}
	$$
	现在对 ansatz 右边逐项计算. 当前 $`D`$-convention 是 $`[P^\nu,D]=-\mathrm i P^\nu`$, 并且方程(24.B.35)给出
	$$
	[ P ^ \nu , J _ { \mu \rho } ]
= - \mathrm i \delta _ \mu{} ^ \nu P _ \rho
+ \mathrm i \delta _ \rho{} ^ \nu P _ \mu .
	$$
	因此
	$$
	\begin{aligned}
[ P ^ \nu , A _ { r s \alpha }{} ^ \beta ]
&=
a [ P ^ \nu , D ] \delta _ { r s } \delta _ \alpha{} ^ \beta
+ b [ P ^ \nu , J _ { \mu \rho } ] \delta _ { r s } \mathcal J ^ { \mu \rho } _ \alpha{} ^ \beta \\
&=
- \mathrm i a P ^ \nu \delta _ { r s } \delta _ \alpha{} ^ \beta
+ b \Bigl (
- \mathrm i \delta _ \mu{} ^ \nu P _ \rho
+ \mathrm i \delta _ \rho{} ^ \nu P _ \mu
\Bigr ) \delta _ { r s } \mathcal J ^ { \mu \rho } _ \alpha{} ^ \beta \\
&=
- \mathrm i a P ^ \nu \delta _ { r s } \delta _ \alpha{} ^ \beta
- 2 \mathrm i b P _ \rho \delta _ { r s } \mathcal J ^ { \nu \rho } _ \alpha{} ^ \beta .
\end{aligned}
	$$
	又因为 $`\mathcal J ^ { \nu \rho } = - \mathrm i [ \gamma^\nu , \gamma^\rho ] /4`$ and $`\{ \gamma^\nu , \gamma^\rho \}=2\eta^{\nu\rho}`$, 上式变为
	$$
	\begin{aligned}
[ P ^ \nu , A _ { r s \alpha }{} ^ \beta ]
&=
\left[
- { \mathrm i a \over 2 }
\{ \gamma ^ \nu , \gamma ^ \rho \}
- { b \over 2 }
[ \gamma ^ \nu , \gamma ^ \rho ]
\right] _ \alpha{} ^ \beta
P _ \rho \delta _ { r s } .
\end{aligned}
	$$
	另一方面
	$$
	2\gamma^\nu\gamma^\rho
=
\{ \gamma^\nu,\gamma^\rho \}
+[ \gamma^\nu,\gamma^\rho ] .
	$$
	逐项比较 $`\{ \gamma^\nu,\gamma^\rho \}`$ and $`[ \gamma^\nu,\gamma^\rho ]`$ 的系数, 得到
	$$
	- { \mathrm i a \over 2 }=+1,\qquad
- { b \over 2 }=+1,
	$$
	也就是
	$$
	a=+2\mathrm i,\qquad b=-2.
	$$
	这给出方程(25.2.46)中的 $`+2\mathrm iD`$ and $`-2J_{\mu\nu}\mathcal J^{\mu\nu}`$ coefficients.
	最后看 $`O,O'`$ 的 $`r,s`$ symmetry. Dimension-zero internal generators act on the $`N`$ Weyl supercharges by a Hermitian $`U(N)`$ matrix. 将这个 matrix 写成 real and imaginary parts:
	$$
	u _ { r s } = R _ { r s } + \mathrm i H _ { r s },
\qquad
u ^ \dagger = u .
	$$
	Hermiticity gives
	$$
	R _ { r s } = - R _ { s r },
\qquad
H _ { r s } = H _ { s r } .
	$$
	在 Majorana basis 中, multiplication by $`\mathrm i`$ on the Weyl charge is represented by $`\gamma_5`$. 因而 internal scalar part decomposes as $`R_{rs}\delta_\alpha{}^\beta + H_{rs}(\gamma_5)_\alpha{}^\beta`$, which is exactly
	$$
	O _ { r s } = - O _ { s r },
\qquad
O _ { r s } ^ \prime = + O _ { s r } ^ \prime .
	$$
</callout>
取方程(25.2.43)与 $`K _ { \nu }`$ 的对易子并使用 $`[ K _ { \nu } , K _ { \mu } ] = 0`$ , 我们发现 $`( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta } [ K ^ { \nu } , Q _ { r \beta } ^ { \sharp } ]`$ 关于 $`\mu`$ 和 $`\nu`$ 是对称的, 在经过一些计算, 这告诉我们
$$
[ K ^ { \nu } , Q _ { r \beta } ^ { \sharp } ] = 0 . \tag{25.2.48}
$$
<callout color="gray_bg">
	Codex 补充证明：方程(25.2.48) 中的 $`Q^\sharp`$
	这里 $`Q^\sharp`$ 是必要的: 若写成 $`Q`$, 会与方程(25.2.43)矛盾. 具体计算为, 令 $`R^\nu_{r\beta}\equiv [K^\nu,Q^\sharp_{r\beta}]`$. 由 Jacobi identity,
	$$
	\begin{aligned}
0&=[K^\nu,[K^\mu,Q_{r\alpha}]]
-[K^\mu,[K^\nu,Q_{r\alpha}]]\\
&=\mathrm i(\gamma^\mu)_\alpha{}^\beta R^\nu_{r\beta}
-\mathrm i(\gamma^\nu)_\alpha{}^\beta R^\mu_{r\beta}.
\end{aligned}
	$$
	所以 $`(\gamma^\mu)_\alpha{}^\beta R^\nu_{r\beta}`$ 对 $`\mu,\nu`$ symmetric. 同时, 由 $`[K^\nu,D]=+\mathrm iK^\nu`$ 和 $`[Q^\sharp_{r\beta},D]=+\frac{\mathrm i}{2}Q^\sharp_{r\beta}`$,
	$$
	\begin{aligned}
[R^\nu_{r\beta},D]
&=[[K^\nu,Q^\sharp_{r\beta}],D]\\
&=[K^\nu,[Q^\sharp_{r\beta},D]]
-[Q^\sharp_{r\beta},[K^\nu,D]]\\
&=+\frac{\mathrm i}{2}[K^\nu,Q^\sharp_{r\beta}]
-\mathrm i[Q^\sharp_{r\beta},K^\nu]\\
&=+\frac{3\mathrm i}{2}R^\nu_{r\beta}.
\end{aligned}
	$$
	也就是说 $`R^\nu_{r\beta}`$ 的 dimension 是 $`-3/2`$. 前面已经证明 fermionic symmetry generator 只能有 dimension $`+1/2`$ 或 $`-1/2`$, 因而 $`R^\nu_{r\beta}=0`$.
</callout>
另外, 取方程(25.2.46)与 $`K _ { \nu }`$ 的对易子给出
$$
\{ Q _ { r \alpha } ^ { \sharp } , \overline { Q ^ { \sharp } } _ { s }{} ^ { \beta } \}
= - 2 \mathrm { i } K _ { \mu } ( \gamma ^ { \mu } ) _ { \alpha }{} ^ { \beta } \delta _ { r s } . \tag{25.2.49}
$$
最后, 取方程(25.2.46)与 $`Q _ { t \gamma }`$ 的对易子, 这会表明 $`O _ { r s }`$ 和 $`O _ { r s } ^ { \prime }`$ 的作用就像 $`R`$ -对称群 $`U ( N )`$ 的生成元,而 $`Q _ { r \alpha }`$ 的左边和右边分别按照表示 $`\mathbf{N}`$ 和 $`\bar { \bf N }`$ 变换, $`P _ { \mu }`$ , $`K _ { \mu }`$ 和 $`D`$ 都是 $`U ( N )`$ -不变量.
这些生成元彼此之间以及它们与其它生成元的 $`U ( N )`$ 对易关系, 再加上 $`J _ { \mu \nu }`$ 和 $`D`$ 与各种生成元的对易子, 这些合起来构成了超共形代数.
这个代数与普通的简单超对称或者 $`N`$ -扩充超对称之间的一个重要差异是, $`U ( N )`$ 对称性不再只是超对称代数的一个外自同构, 那时它可以是也可以不是作用量的一个对称性——现在它是超共形代数的一部分, 因此它必须是任何共形不变的超对称理论的一个对称性.
## 翻译后记号
本节正文最终采用以下 spinor-index translation. Weinberg 原文中用于 $`(0,1/2)`$ 的 source label $`\mathcal Q _ { a r }`$ 在最终代数中翻译为 dotted Weyl generator $`\mathcal Q ^ { \dot a r }`$, 它的 Hermitian conjugate $`\mathcal Q _ { a r } ^ *`$ 翻译为 undotted conjugate generator $`\left( \mathcal Q ^ \dagger \right) ^ a{} _ r`$. 因此 basic anticommutator 写成
$$
\{ \mathcal Q ^ { \dot a r } , \left( \mathcal Q ^ \dagger \right) ^ b{} _ s \}
= -2 \delta ^ r{} _ s \bar\sigma _ \mu{} ^ { \dot a b } P ^ \mu
\equiv 2\delta^r{}_s P^{\dot a b},
\qquad
P^{\dot a b}\equiv -\bar\sigma_\mu{}^{\dot a b}P^\mu .
$$
Spinor indices are raised and lowered by $`\epsilon`$. The component convention is
$$
\epsilon ^ { + - } = 1,\qquad
\epsilon _ { - + } = 1,\qquad
\epsilon ^ { \dot + \dot - } = 1,\qquad
\epsilon _ { \dot - \dot + } = 1 .
$$
Thus $`\epsilon ^ { - + } = -1`$, $`\epsilon _ { + - } = -1`$, and the same antisymmetry holds for dotted spinors.
这里 $`\dot a,\dot b`$ 是 $`(0,1/2)`$ dotted spinor index, $`a,b`$ 是 $`(1/2,0)`$ undotted spinor index. 2-component sigma matrices 的位置约定是
$$
\sigma ^ \mu{} _ { a \dot a } = ( \mathbf 1 , \sigma ^ 1 , \sigma ^ 2 , \sigma ^ 3 ) _ { a \dot a } ,
\qquad
\bar\sigma ^ \mu{} ^ { \dot a a } = ( \mathbf 1 , - \sigma ^ 1 , - \sigma ^ 2 , - \sigma ^ 3 ) ^ { \dot a a } .
$$
4-component Majorana generator and Dirac adjoint carry opposite spinor variance. The upper two-component conjugate $`\left( \mathcal Q ^ \dagger \right)^a{}_r`$ is first lowered by $`\epsilon _ { a b }`$ when inserted into $`Q_{r\alpha}`$:
$`\left( \mathcal Q ^ \dagger \right) _ { a r } = \epsilon _ { a b } \left( \mathcal Q ^ \dagger \right)^b{}_r`$. $`\overline Q_s{}^\beta`$ denotes the Dirac adjoint of $`Q_{s\alpha}`$, with the same internal label $`s`$.
$$
Q _ { r \alpha } =
\begin{pmatrix}
\left( \mathcal Q ^ \dagger \right) _ { a r }\\
\mathcal Q ^ { \dot a r }
\end{pmatrix} _ \alpha .
$$
For the Majorana condition, $`C=\epsilon\gamma_5`$. In the Weyl order $`(\dot a,a)`$ carried by the complex-conjugate column,
$$
C=
\begin{pmatrix}
\epsilon ^ { \dot a\dot b }&0\\
0&\epsilon _ { ab }
\end{pmatrix}
=
\begin{pmatrix}
e&0\\
0&-e
\end{pmatrix}.
$$
因此 contraction 应写成 $`Q _ { r \alpha }\overline Q _ s{} ^ \beta`$, 而 gamma matrix carries one lower and one upper Dirac index:
$$
( \gamma ^ \mu ) _ \alpha{} ^ \beta
= \mathrm i
\begin{pmatrix}
0&\sigma ^ \mu{} _ { a\dot b }\\
\bar\sigma ^ \mu{} ^ { \dot a b }&0
\end{pmatrix} _ \alpha{} ^ \beta .
$$
所以本节中所有 4-component anticommutators 使用 $`\overline Q{}^\beta`$ and $`(\gamma^\mu)_\alpha{}^\beta`$, not a lower-index $`\overline Q`$ and not a gamma matrix with two lower spinor indices. 只有方程(25.2.18)—(25.2.29)附近的证明保留 Weinberg 的 $`a=\pm1/2`$ source-label notation, 因为那里直接使用 Clebsch-Gordan weight components.
</content>
</page>
