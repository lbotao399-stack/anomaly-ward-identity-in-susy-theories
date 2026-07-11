Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81ea804ed1024d19375b as of 2026-07-04T08:55:19.391Z:
<page url="https://app.notion.com/p/34cee2b74b3f81ea804ed1024d19375b">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f815fb0b0e5db189e0b88" title="第 25 章 超对称代数"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"25.1 阶化 Lie 代数和阶化参量"}
</properties>
<content>
我们在2.2节看到了如何将任意连续对称变换写成Lie代数的形式, 这个Lie代数由线性独立的对称性生成元 $`t _ { a }`$ 生成, 并且生成元满足对易关系 $`[ t _ { a } , t _ { b } ] = \mathrm{i} C _ { a b } { } ^ { c } t _ { c }`$ .
以非常类似的方式, 用来表示超对称的生成元 $`t _ { a }`$ 构成了阶化Lie代数,\[2\] 这样的Lie代数表现为如下形式的对易关系和反对易关系
<callout color="gray_bg">
	- B. Zumino, Nucl. Phys. B89, 535 (1975). 这篇文章重印于Supersymmetry, 参考文献\[1\]
</callout>
$$
t _ { a } t _ { b } - ( - 1 ) ^ { \eta _ { a } \eta _ { b } } t _ { b } t _ { a } = \mathrm{i} C _ { a b } { } ^ { c } t _ { c } . \tag{25.1.1}
$$
(本节采用爱因斯坦求和约定.) 对于每个 $`a`$ , $`\eta _ { a }`$ 是 $`+ 1`$ 或 $`0`$ , 它是生成元 $`t _ { a }`$ 的阶数, 而 $`C _ { a b } { } ^ { c }`$ 是一组数值的结构常数.
$`\eta _ { a } = 1`$ 的生成元 $`t _ { a }`$ 被称为费米的; 其它那些 $`\eta _ { a } = 0`$ 的生成元则被称为玻色的.
对于玻色算符和玻色算符以及玻色算符和费米算符, 方程(25.1.1)提供了对易关系, 而对于费米算符和费米算符, 它则提供了反对易关系.
我们暂且先来看一下它对结构常数产生的影响, 在此之后再回到提出方程(25.1.1)的动机.
根据方程(25.1.1), 结构常数必须满足条件
$$
C _ { a b } { } ^ { c } = - ( - 1 ) ^ { \eta _ { a } \eta _ { b } } C _ { b a } { } ^ { c } . \tag{25.1.2}
$$
对于任何由场算符的泛函构成的算符, 两个玻色算符的乘积或者两个费米算符的乘积是玻色的,而一个费米算符与一个玻色算符的乘积是费米的, 这使得
$$
C _ { a b } { } ^ { c } = 0 \quad \text{unless}\quad \eta _ { c } = \eta _ { a } + \eta _ { b } \pmod { 2 } . \tag{25.1.3}
$$
另外, 对于任何以这种方式构建的算符, 玻色算符和费米算符的厄米伴分别是玻色的和费米的.
如果 $`t _ { a }`$ 是厄米算符, 那么结构常数满足实条件
$$
C _ { a b } { } ^ { c * } = - C _ { b a } { } ^ { c } . \tag{25.1.4}
$$
结构常数同时还满足一个非线性约束, 这个约束来自于超Jacobi恒等式
$$
\begin{array} { r } { ( - 1 ) ^ { \eta _ { c } \eta _ { a } } [ [ t _ { a } , t _ { b } \} , t _ { c } \} + ( - 1 ) ^ { \eta _ { a } \eta _ { b } } [ [ t _ { b } , t _ { c } \} , t _ { a } \} + ( - 1 ) ^ { \eta _ { b } \eta _ { c } } [ [ t _ { c } , t _ { a } \} , t _ { b } \} = 0 \ . \ } \end{array} \tag{25.1.5}
$$
这里的“ $`[ \cdots \}`$ ”类似于方程(25.1.1)左边出现的对易子/反对易子, 但在这里推广至任意的阶化算符$`O , O ^ { \prime } \cdots`$
$$
[ { \cal O } , { \cal O } ^ { \prime } \} \equiv { \cal O } { \cal O } ^ { \prime } - ( - 1 ) ^ { \eta ( { \cal O } ) \eta ( { \cal O } ^ { \prime } ) } { \cal O } ^ { \prime } { \cal O } = - ( - 1 ) ^ { \eta ( { \cal O } ) \eta ( { \cal O } ^ { \prime } ) } [ { \cal O } ^ { \prime } , { \cal O } \} , \tag{25.1.6}
$$
现在它被理解成, 生成元的任意乘积 $`O = t _ { a } t _ { b } t _ { c } \cdot \cdot .`$ 被赋予阶数 $`\eta ( O ) \equiv \eta _ { a } + \eta _ { b } + \eta _ { c } + \cdots ( \pmod { 2 } )`$ .
(为证明方程(25.1.5), 只需证明 $`t _ { a } t _ { b } t _ { c }`$ 和 $`t _ { a } t _ { c } t _ { b }`$ 的系数为零即可, 至于生成元的其它乘积, 方程(25.1.5)左边在轮换 $`a b c b c a c a b`$ 下的对称性会确保它们的系数为零.
$`t _ { a } t _ { b } t _ { c }`$ 在方程(25.1.5)中的系数是
$$
( - 1 ) ^ { \eta _ { c } \eta _ { a } } - ( - 1 ) ^ { \eta _ { a } \eta _ { b } } ( - 1 ) ^ { \eta _ { a } ( \eta _ { b } + \eta _ { c } ) } = 0 ,
$$
而 $`t _ { a } t _ { c } t _ { b }`$ 的系数是
$$
( - 1 ) ^ { \eta _ { a } \eta _ { b } } ( - 1 ) ^ { \eta _ { b } \eta _ { c } } ( - 1 ) ^ { \eta _ { a } ( \eta _ { b } + \eta _ { c } ) } - ( - 1 ) ^ { \eta _ { b } \eta _ { c } } ( - 1 ) ^ { \eta _ { c } \eta _ { a } } = 0 ,
$$
证毕.) 将方程(25.1.1)代入方程(25.1.5), 我们发现约束
$$
( - 1 ) ^ { \eta _ { c } \eta _ { a } } C _ { a b } { } ^ { d } C _ { d c } { } ^ { e } + ( - 1 ) ^ { \eta _ { a } \eta _ { b } } C _ { b c } { } ^ { d } C _ { d a } { } ^ { e } + ( - 1 ) ^ { \eta _ { b } \eta _ { c } } C _ { c a } { } ^ { d } C _ { d b } { } ^ { e } = 0 . \tag{25.1.7}
$$
当然, 在所有生成元都是玻色生成元的情况下, 方程(25.1.5)就是通常的 Jacobi 恒等式, 而方程 (25.1.7)就是结构常数之间通常的非线性约束(2.2.22).
方程(25.1.1)可以取作我们的出发点, 但是就像在 2.2节我们对普通 Lie 代数所做的那样, 我们可以赋予它一个动机, 这样它就不是出发点而是有限连续对称变换的一个必要特征.
与2.2节不同的是, 现在这些变换依赖于连续的阶参量.
一组阶化c -数参量可以视为“数”, 这些数既包含格拉斯曼参量(参看9.5节)也包含普通数, 它们满是算术的结合律和分配率, 但是不再满足简单的交换律,而是满足关系
$$
\alpha ^ { a } \beta ^ { b } = ( - 1 ) ^ { \eta _ { a } \eta _ { b } } \beta ^ { b } \alpha ^ { a } , \tag{25.1.8}
$$
其中 $`\alpha ^ { a }`$ , $`\beta ^ { a } , \cdots`$ 用来区分第 $`a`$ 个参量的不同值, 以矢量代数中的方法, 我们可以用 $`v ^ { a }`$ 和 $`u ^ { a }`$ 来标记两个不同实矢量的 $`a`$ -分量.
和以前一样, 第 $`a`$ 个阶化参量被赋予阶数 $`\eta _ { a }`$ , 当 $`\alpha ^ { a }`$ 分别是费米参量和玻色参量时, $`\eta _ { a }`$ 分别等于 $`+ 1`$ 和0. 即, 如果这些参量中有一个是玻色的, 那么它们就是对易的, 如果两个参量都是费米的, 那么它们就是反对易的.
阶化参量的乘积 $`\alpha ^ { a } \beta ^ { b } \gamma ^ { c } \cdots`$ 被赋予阶数 $`\eta _ { a } + \eta _ { b } +`$ $`\eta _ { c } + \cdots ( \pmod { 2 } )`$ ; 即, 如果这个乘积中包含奇数个费米参量, 那么它就是费米的, 否则就是玻色的.有了这个阶数, 很容易看到阶化参量的乘积满足的对易规则或反对易规则类似于方程(25.1.8).
考察这样的连续变换 $`T _ { \alpha }`$ , 在形式上它由阶化参量 $`\alpha ^ { a }`$ 的幂级数给出:
$$
T ( \alpha ) = 1 + \alpha ^ { a } t _ { a } + \alpha ^ { a } \alpha ^ { b } t _ { a b } + \cdots , \tag{25.1.9}
$$
其中 $`t _ { a }`$ , $`t _ { a b }`$ 等是一组与 $`\alpha`$ 无关的算符系数, 这时我们还没有假定它们要满足任何像方程(25.1.1)这样的代数关系.
由于参量 $`\alpha ^ { a }`$ 满足方程(25.1.8), 系数 $`t _ { a b \cdots }`$ 必须要满足对称/反对称条件, 例如
$$
t _ { a b } = ( - 1 ) ^ { \eta _ { a } \eta _ { b } } t _ { b a } . \tag{25.1.10}
$$
同时假定变换 $`T ( \beta )`$ 与任意阶化参量的任意值 $`\alpha ^ { a }`$ 对易, 这将会方便我们的讨论, 在这一情况下, (25.1.9)中的算符系数满足条件
$$
\alpha ^ { a } t _ { b } = ( - 1 ) ^ { \eta _ { a } \eta _ { b } } t _ { b } \alpha ^ { a } , \tag{25.1.11}
$$
$$
\alpha ^ { a } t _ { b c } = ( - 1 ) ^ { \eta _ { a } ( \eta _ { b } + \eta _ { c } ) } t _ { b c } \alpha ^ { a } . \tag{25.1.12}
$$
即, 在 $`t _ { a }`$ 和 $`t _ { b c }`$ 与阶化参量满足的对易关系和反对易关系中, 它们自身分别就像是阶数分别为 $`\eta _ { a }`$ 和 $`\eta _ { b } + \eta _ { c } \pmod { 2 }`$ 的阶化参量.
算符上的其它约束来自于 $`T ( \alpha )`$ 构成半群的要求; 即, 对于阶化参量取不同值 $`\alpha`$ 和 $`\beta`$ 时的 $`T`$ 算符, 它们的乘积也是一个 $`T`$ 算符
$$
T ( \alpha ) T ( \beta ) = T ( f ( \alpha , \beta ) ) . \tag{25.1.13}
$$
其中 $`f ^ { c } ( \alpha , \beta )`$ 本身是阶化参量的形式幂级数.
由于 $`T ( 0 ) T ( \beta ) = T ( \beta )`$ 以及 $`T ( \alpha ) T ( 0 ) = T ( \alpha )`$ , 我们必须有
$$
f ^ { c } ( 0 , \beta ) = \beta ^ { c } , \qquad f ^ { c } ( \alpha , 0 ) = \alpha ^ { c } . \tag{25.1.14}
$$
因此 $`f ( \alpha , \beta )`$ 的幂级数展开必须采取如下的形式
$$
f ^ { c } ( \alpha , \beta ) = \alpha ^ { c } + \beta ^ { c } + f _ { a b } { } ^ { c } \alpha ^ { a } \beta ^ { b } + \cdots . \tag{25.1.15}
$$
其中 $`f _ { a b } { } ^ { c }`$ 是一组普通常数(即, 玻色常数), 而“· · ·”代表阶化参量的三阶项或者更高阶项.
为了使$`f ^ { c } ( \alpha , \beta )`$ 是阶化参量, 方程(25.1.15)的每一项必须要有相同的阶数, 这意味着
$$
f _ { a b } { } ^ { c } = 0 \quad \text{unless} \quad \eta _ { c } = \eta _ { a } + \eta _ { b } \pmod { 2 } . \tag{25.1.16}
$$
将幂级数(25.1.9)和(25.1.15)代入乘积规则(25.1.13), 这给出
$$
\begin{array} { l } { { \displaystyle \left[ 1 + \alpha ^ { a } t _ { a } + \alpha ^ { a } \alpha ^ { b } t _ { a b } + \cdots \right] \left[ 1 + \beta ^ { a } t _ { a } + \beta ^ { a } \beta ^ { b } t _ { a b } + \cdots \right] } } \\ { { \displaystyle \quad = 1 + \left( \alpha ^ { c } + \beta ^ { c } + f _ { a b } { } ^ { c } \alpha ^ { a } \beta ^ { b } + \cdots \right) t _ { c } } } \\ { { \displaystyle \quad \quad + \left( \alpha ^ { c } + \beta ^ { c } + \cdots \right) \left( \alpha ^ { d } + \beta ^ { d } + \cdots \right) t _ { c d } + \cdots . } } \end{array}
$$
1, $`\alpha ^ { a } , \beta ^ { a } , \alpha ^ { a } \alpha ^ { b }`$ 和 $`\beta ^ { a } \beta ^ { b }`$ 的系数在方程两边自动匹配, 而要求 $`\alpha ^ { a } \beta ^ { b }`$ 的系数相等这个条件给出了不平庸的关系
$$
( - 1 ) ^ { \eta _ { a } \eta _ { b } } t _ { a } t _ { b }
= f _ { a b } { } ^ { c } t _ { c } + t _ { a b } + ( - 1 ) ^ { \eta _ { a } \eta _ { b } } t _ { b a }
= f _ { a b } { } ^ { c } t _ { c } + 2 t _ { a b } . \tag{25.1.17}
$$
(左边的符号因子来自于 $`t _ { a }`$ 和 $`\beta ^ { b }`$ 的交换.) 加上同一类的高阶关系, 如果我们知道生成元 $`t _ { a }`$ 和群组合函数 $`f ^ { a } ( \alpha , \beta )`$ , 这将使得我们可以计算出整个函数(25.1.9).
但为了使这个计算是可能的, $`t _ { a }`$ 必须要满足一个约束.
利用方程(25.1.10), 方程(25.1.17)与交换 $`a , b`$ 后的同一方程的差或和给出 Lie 超代数关系(25.1.1), 而结构常数给定为
$$
\mathrm{i} C _ { a b } { } ^ { c } = ( - 1 ) ^ { \eta _ { a } \eta _ { b } } f _ { a b } { } ^ { c } - f _ { b a } { } ^ { c } . \tag{25.1.18}
$$
另外, 从方程(25.1.16)和(25.1.18)就立即得出了方程(25.1.3).
对于反对易 $`\mathrm { c }`$ -数 $`\alpha`$ 的复共轭 $`\alpha ^ { * }`$ , 它的定义要使得 $`\alpha`$ 与任意算符 $`\mathcal{O}`$ 的乘积的厄米共轭是
$$
( \alpha \mathcal{O} ) ^ { * } = \mathcal{O} ^ { * } \alpha ^ { * } . \tag{25.1.19}
$$
由此得出c -数在复共轭下的行为与算符在厄米共轭下的行为相同:
$$
( \alpha \beta ) ^ { * } = \beta ^ { * } \alpha ^ { * } . \tag{25.1.20}
$$
并且 $`\alpha ^ { * }`$ 与 $`\alpha`$ 的阶数相同.
阶化Lie代数对物理的意义被时空对称性严格限制了.
我们现在转向对这些约束的考察.
</content>
</page>
