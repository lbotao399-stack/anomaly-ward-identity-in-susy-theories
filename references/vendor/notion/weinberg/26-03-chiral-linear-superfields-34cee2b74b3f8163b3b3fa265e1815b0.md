Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0 as of 2026-06-30T02:25:45.495Z:
<page url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f814e8d69d0e3182b91ec" title="第 26 章 超对称场论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"26.3 手征超场和线性超场"}
</properties>
<content>
我们在上一节发现, 一般超场中出现了 $`D`$ 和 $`\lambda`$ 这一点阻止了我们在满足物理要求的拉格朗日密度中使用这种超场.
那么假定我们考察这样的超场, 它满足
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81789bd3d37244960008">
	$$
	\lambda = D = 0 . \tag{26.3.1}
	$$
</synced_block>
这些条件是否受到超对称变换的保护? 根据方程(26.2.17)和(26.2.16), 如果 $`\lambda = 0`$ , 那么 $`D = 0`$ 的条件不变的, 但是要想 $`\lambda = 0`$ 的条件在超对称变换下不变则需要我们附加 $`\partial _ { \mu } V _ { \nu } - \partial _ { \nu } V _ { \mu } = 0`$ 的条件,这要求 $`V _ { \mu }`$ 是纯规范:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f815ab667da80eecb2eaa">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { \delta \lambda = \left( \frac { 1 } { 2 } \Big [ \partial _ { \mu } { \cal V } , \gamma ^ { \mu } \Big ] + \mathrm{i} \gamma _ { 5 } D \right) \alpha , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \delta D = \mathrm{i} \Big ( \bar { \alpha } \gamma _ { 5 } \not\!\partial\, \lambda \Big ) . } } \end{array} \tag{26.2.16-26.2.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8197ae8dee9f6f48571b">
	$$
	V _ { \mu } ( x ) = \partial _ { \mu } Z ( x ) . \tag{26.3.2}
	$$
</synced_block>
方程(26.2.15)表明, 有了 $`\lambda = 0`$ , 这个条件是被超对称变换保护的.
因此我们得到了一个退化的超场, 它满足约束(26.3.1)和(26.3.2), 它的分量场有如下的变换性质
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81789bd3d37244960008">
		$$
		\lambda = D = 0 . \tag{26.3.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8197ae8dee9f6f48571b">
		$$
		V _ { \mu } ( x ) = \partial _ { \mu } Z ( x ) . \tag{26.3.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8150b8b4d7b69d40d8ed">
	$$
	\begin{array} { r l } & { \delta C = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \omega \right) , } \\ & { \delta \omega = \left( - \mathrm{i} \gamma _ { 5 } \not\!\partial\, C - M + \mathrm{i} \gamma _ { 5 } N + \not\!\partial\, Z \right) \alpha , } \\ & { \delta M = - \Big ( \bar { \alpha } \not\!\partial\, \omega \Big ) , } \\ & { \delta N = \mathrm{i} \left( \bar { \alpha } \gamma _ { 5 } \not\!\partial\, \omega \right) , } \\ & { \delta Z = \left( \bar { \alpha } \omega \right) , } \end{array} \tag{26.3.4-26.3.6}
	$$
</synced_block>
与方程(26.1.21)比较, 我们看到这与26.1节通过直接方法构建的超多重态是相同的, 它们之间的对应是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f810ea7bec1cb3c00b45c">
		$$
		\begin{array} { l } { { \delta A = \bar { \alpha } \psi , \qquad \delta B = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \psi , } } \\ { { \qquad \delta \psi = \partial _ { \mu } ( A + \mathrm{i} \gamma _ { 5 } B ) \gamma ^ { \mu } \alpha + ( F - \mathrm{i} \gamma _ { 5 } G ) \alpha , } } \\ { { \qquad \delta F = \bar { \alpha } \gamma ^ { \mu } \partial _ { \mu } \psi , \qquad \delta G = - \mathrm{i} \bar { \alpha } \gamma _ { 5 } \gamma ^ { \mu } \partial _ { \mu } \psi . } } \end{array} \tag{26.1.21}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81af9b85f0543c55fb4f">
	$$
	C = A , \qquad \omega = - \mathrm{i} \gamma _ { 5 } \psi , \qquad M = G , \qquad N = - F , \qquad Z = B . \tag{26.3.8}
	$$
</synced_block>
满足条件(26.3.1)和(26.3.2)的超场被称作是手征的.\\\*
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81789bd3d37244960008">
		$$
		\lambda = D = 0 . \tag{26.3.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8197ae8dee9f6f48571b">
		$$
		V _ { \mu } ( x ) = \partial _ { \mu } Z ( x ) . \tag{26.3.2}
		$$
	</synced_block_reference>
</callout>
为了将手征超场 $`X ( x , \theta )`$ 与上一节的一般超场 $`S ( x , \theta )`$ 区分开来, 取代 $`C , M , N ,`$ $`Z`$ 和 $`\omega`$ , 我们用 $`A , B , F , G`$ 和 $`\psi`$ 表示它的分量.
通过在方程(26.2.10)中使用方程(26.3.1), (26.3.2)和(26.3.8), 我们发现一般手征超场的形式是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81789bd3d37244960008">
		$$
		\lambda = D = 0 . \tag{26.3.1}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8197ae8dee9f6f48571b">
		$$
		V _ { \mu } ( x ) = \partial _ { \mu } Z ( x ) . \tag{26.3.2}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81af9b85f0543c55fb4f">
		$$
		C = A , \qquad \omega = - \mathrm{i} \gamma _ { 5 } \psi , \qquad M = G , \qquad N = - F , \qquad Z = B . \tag{26.3.8}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81208604d4fff421664a">
	$$
	\begin{array} { l } { { \displaystyle { X ( x , \theta ) = A ( x ) - \left( \bar { \theta } \psi ( x ) \right) + \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) F ( x ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) G ( x ) } } } \\ { { \displaystyle { ~ + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } B ( x ) + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \gamma _ { 5 } \not\!\partial\, \psi ( x ) \Big ) } } } \\ { { \displaystyle { ~ - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box A ( x ) . } } } \end{array} \tag{26.3.9}
	$$
</synced_block>
(我们本也可以取 $`C = - B`$ , $`\omega = \psi`$ , $`M = - F`$ , $`N = - G`$ 和 $`Z = A`$ .
我们做(26.3.8)这种对应是因为,正如我们这里所看到的, 对于标量超场, 它们与 $`A`$ 和 $`F`$ 是标量而 $`B`$ 和 $`G`$ 是赝标量这个常见的约定是一致的.)
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81af9b85f0543c55fb4f">
		$$
		C = A , \qquad \omega = - \mathrm{i} \gamma _ { 5 } \psi , \qquad M = G , \qquad N = - F , \qquad Z = B . \tag{26.3.8}
		$$
	</synced_block_reference>
</callout>
手征超场(26.3.9)可以进一步分解成
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81208604d4fff421664a">
		$$
		\begin{array} { l } { { \displaystyle { X ( x , \theta ) = A ( x ) - \left( \bar { \theta } \psi ( x ) \right) + \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) F ( x ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) G ( x ) } } } \\ { { \displaystyle { ~ + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } B ( x ) + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \gamma _ { 5 } \not\!\partial\, \psi ( x ) \Big ) } } } \\ { { \displaystyle { ~ - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box A ( x ) . } } } \end{array} \tag{26.3.9}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f815889fcf9b073966a39">
	$$
	X ( x , \theta ) = \frac { 1 } { \sqrt { 2 } } \Big [ \Phi ( x , \theta ) + \tilde { \Phi } ( x , \theta ) \Big ] , \tag{26.3.10}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f819eaf3fe05cd968d43f">
	$$
	\begin{array} { l } { { \Phi ( x , \theta ) = \phi ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { L } ( x ) \Big ) + \mathcal{F} ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 + \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \phi ( x ) } } \\ { { \qquad - \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { L } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \phi ( x ) , } } \\ { { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { R } ( x ) \Big ) + \tilde { \mathcal{F} } ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 - \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \tilde { \phi } ( x ) } } \\ { { \qquad + \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { R } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \tilde { \phi } ( x ) , } } \end{array} \tag{26.3.11}
	$$
</synced_block>
它们的分量场定义成
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81f0a161ed7c4a2897b8">
	$$
	\phi \equiv { \frac { A + \mathrm{i} B } { \sqrt { 2 } } } , \qquad \psi _ { L } \equiv \biggl ( { \frac { 1 + \gamma _ { 5 } } { 2 } } \biggr ) \psi , \qquad \mathcal{F} \equiv { \frac { F - \mathrm{i} G } { \sqrt { 2 } } } , \tag{26.3.13}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81728ea4faa045d405a8">
	$$
	\tilde { \phi } \equiv { \frac { A - \mathrm{i} B } { \sqrt { 2 } } } , \qquad \psi _ { R } \equiv \biggl ( { \frac { 1 - \gamma _ { 5 } } { 2 } } \biggr ) \psi , \qquad \tilde { \mathcal{F} } \equiv { \frac { F + \mathrm{i} G } { \sqrt { 2 } } } , \tag{26.3.14}
	$$
</synced_block>
无论是 $`\Phi`$ 还在 $`\tilde { \Phi }`$ , 它们的分量场都构成了超对称代数的完整表示:
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81568065f84f9597622a">
	$$
	\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81e6ab2fd98971344748">
	$$
	\begin{array} { r l } & { \delta \psi _ { R } = \sqrt { 2 } \partial _ { \mu } \tilde { \phi } \gamma ^ { \mu } \alpha _ { L } + \sqrt { 2 } \tilde { \mathcal{F} } \alpha _ { R } , } \\ & { \delta \tilde { \mathcal{F} } = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \not\!\partial\, \psi _ { R } \Big ) , } \\ & { \delta \tilde { \phi } = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \psi _ { R } \Big ) , } \end{array} \tag{26.3.19, 26.3.20, 26.3.18}
	$$
</synced_block>
其中, 像往常一样,
$$
\alpha _ { L } = \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) \alpha , \alpha _ { R } = \left( \frac { 1 - \gamma _ { 5 } } { 2 } \right) \alpha ,
$$
对 $`\theta`$ 类似.
形如(26.3.11)和(26.3.12)的超场分别被称为是左手征和右手征的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f819eaf3fe05cd968d43f">
		$$
		\begin{array} { l } { { \Phi ( x , \theta ) = \phi ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { L } ( x ) \Big ) + \mathcal{F} ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 + \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \phi ( x ) } } \\ { { \qquad - \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { L } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \phi ( x ) , } } \\ { { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { R } ( x ) \Big ) + \tilde { \mathcal{F} } ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 - \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \tilde { \phi } ( x ) } } \\ { { \qquad + \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { R } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \tilde { \phi } ( x ) , } } \end{array} \tag{26.3.11}
		$$
	</synced_block_reference>
</callout>
在手征超场 $`X ( x , \theta )`$ 是实场的特殊情况下, 它的左手征和右手征部分 $`\Phi`$ 和 $`\tilde { \Phi }`$ 互为复共轭, 这使得 $`\tilde { \phi } = \phi ^ { * }`$ , $`\tilde { \mathcal{F} } = \mathcal{F} ^ { * }`$ , 以及 $`\psi`$ 是 Majorana 场.
然而, 如果我们不要求 $`X ( x , \theta )`$ 是实的, 那么 $`\Phi`$ 和 $`\tilde { \Phi }`$ 之间一般没有关系; 它们中的一个甚至有可能为零.
超场 $`\Phi`$ 的分量中含有两个复的玻色分量 $`\phi`$ 和 $`\mathcal{F}`$ ,或者说4个独立的实玻色分量,以及一个Ma-jorana 费米场 $`\psi`$ , 它有4个独立的费米分量.
这是上一节末尾推导的一般结果的又一例子, 即任何构成超对称代数表示的一组场必有相同数目的独立玻色分量和独立费米分量.
我们可以用方程(26.A.5), (26.A.17)和(26.A.18)重写方程(26.3.11)和(26.3.12)以阐明这些超场对 $`\theta _ { L }`$ 和 $`\theta _ { R }`$ 的依赖方式:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81cba5eded23c3d7723a">
		$$
		\begin{array} { r } { M ^ { \mathrm { T } } = \left\{ \begin{array} { l l } { + \mathcal{C} M \mathcal{C} ^ { - 1 } \quad } & { M = 1 , \ \gamma _ { 5 } \gamma _ { \mu } , \ \gamma _ { 5 } } \\ { - \mathcal{C} M \mathcal{C} ^ { - 1 } \quad } & { M = \gamma _ { \mu } , \ [ \gamma _ { \mu } , \gamma _ { \nu } ] } \end{array} \right. , } \end{array} \tag{26.A.5}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8168865bf41f3dacf374">
		$$
		s _ { \alpha } \left( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \right) = - ( \gamma _ { \mu } s ) _ { \alpha } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) . \tag{26.A.17}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81678701ee7b96af9b3b">
		$$
		\Bigl ( \bar { s } s \Bigr ) ^ { 2 } = - \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } , \qquad \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \mu } s \Bigr ) \Bigl ( \bar { s } \gamma _ { 5 } \gamma _ { \nu } s \Bigr ) = - \eta _ { \mu \nu } \Bigl ( \bar { s } \gamma _ { 5 } s \Bigr ) ^ { 2 } . \tag{26.A.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f819eaf3fe05cd968d43f">
		$$
		\begin{array} { l } { { \Phi ( x , \theta ) = \phi ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { L } ( x ) \Big ) + \mathcal{F} ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 + \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) + \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \phi ( x ) } } \\ { { \qquad - \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { L } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \phi ( x ) , } } \\ { { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x ) - \sqrt { 2 } \Big ( \bar { \theta } \psi _ { R } ( x ) \Big ) + \tilde { \mathcal{F} } ( x ) \bigg ( \bar { \theta } \bigg ( \frac { 1 - \gamma _ { 5 } } { 2 } \bigg ) \theta \bigg ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) \partial ^ { \mu } \tilde { \phi } ( x ) } } \\ { { \qquad + \frac { 1 } { \sqrt { 2 } } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Big ( \bar { \theta } \not\!\partial\, \psi _ { R } ( x ) \Big ) - \frac { 1 } { 8 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Box \tilde { \phi } ( x ) , } } \end{array} \tag{26.3.11}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81dab423c0265e13f79d">
	$$
	\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f810cb95ecbed092f76d7">
	$$
	\begin{array} { r } { x _ { \pm } ^ { \mu } \equiv x ^ { \mu } \pm \frac { 1 } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma ^ { \mu } \theta \Big ) = x ^ { \mu } \pm \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \gamma ^ { \mu } \theta _ { L } \Big ) . } \end{array} \tag{26.3.23}
	$$
</synced_block>
$`\phi ( x _ { + } )`$ 和 $`\tilde { \phi } ( \boldsymbol { x } _ { - } )`$ 对 $`x ^ { \mu } - x _ { \pm } ^ { \mu }`$ 的幂级数展开至于四次项, $`\psi _ { L , R } ( x _ { \pm } )`$ 的展开则止于线性项, 而 $`\mathcal{F} ( x _ { + } )`$ 和$`\tilde { \mathcal{F} } ( x _ { - } )`$ 的展开至于零阶项, 这是因为所有高阶项在方程(26.3.21)和(26.3.22)中的贡献都会包含三个或多个 $`\theta _ { L }`$ 或 $`\theta _ { R }`$ 因子, 因此为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81dab423c0265e13f79d">
		$$
		\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
		$$
	</synced_block_reference>
</callout>
由于相同的原因, 很容易看到, 任何只依赖于 $`\theta _ { L }`$ 和 $`x _ { + } ^ { \mu }`$ 但不额外依赖于 $`\theta _ { R }`$ 的超场必须取(26.3.21)的形式, 任何只依赖于 $`\theta _ { R }`$ 和 $`x _ { - } ^ { \mu }`$ 但不额外依赖于 $`\theta _ { L }`$ 的超场必须取(26.3.22)的形式.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81dab423c0265e13f79d">
		$$
		\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
		$$
	</synced_block_reference>
</callout>
我们已经看到, 一个超场是左手征还是右手征完全由这个超场允许依赖的量决定.
由此理解得出, 左手征超场(右手征超场)的任何函数, 而不是它们的复共轭或时空导数, 将是左(右)手征超场.
这也可以通过一个更加形式的方法证明.
因为 $`\Phi ( x , \theta )`$ 仅是通过 $`x _ { + }`$ 依赖于 $`\theta _ { R }`$ , 而 $`\tilde { \Phi } ( x , \theta )`$ 仅是通过 $`x _ { - }`$ 依赖于 $`\theta _ { L }`$ , 它们满足条件
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81d89c00ec93bb94b44c">
	$$
	{ \mathcal D } _ { R \alpha } \Phi = { \mathcal D } _ { L \alpha } \tilde { \Phi } = 0 , \tag{26.3.24}
	$$
</synced_block>
其中 $`\mathcal{D} _ { R }`$ 和 $`\mathcal{D} _ { L }`$ 分别是超导数(26.2.26)的左手征部分和右手征部分:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81228ecbee4906baf10a">
		$$
		\mathcal{D} \equiv - \frac { \partial } { \partial \bar { \theta } } - \gamma ^ { \mu } \theta \frac { \partial } { \partial x ^ { \mu } } , \tag{26.2.26}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8183b7c0cd8ddad60bee">
	$$
	\begin{array} { l } { { \displaystyle \mathcal{D} _ { R \alpha } \equiv \left[ \left( \frac { 1 - \gamma _ { 5 } } { 2 } \right) \mathcal{D} \right] _ { \alpha } = - \epsilon _ { \alpha \beta } \frac \partial { \partial \theta _ { R \beta } } - ( \gamma ^ { \mu } \theta _ { L } ) _ { \alpha } \frac \partial { \partial x ^ { \mu } } , } } \\ { { \displaystyle \mathcal{D} _ { L \alpha } \equiv \left[ \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) \mathcal{D} \right] _ { \alpha } = + \epsilon _ { \alpha \beta } \frac \partial { \partial \theta _ { L \beta } } - ( \gamma ^ { \mu } \theta _ { R } ) _ { \alpha } \frac \partial { \partial x ^ { \mu } } , } } \end{array} \tag{26.3.25-26.3.26}
	$$
</synced_block>
它们满足
$$
\mathcal{D} _ { R \alpha } x _ { + } ^ { \mu } = \mathcal{D} _ { L \alpha } x _ { - } ^ { \mu } = 0 .
$$
反之, 如果超场 $`\Phi`$ 满足 $`\mathcal{D} _ { R } \boldsymbol { \Phi } = 0`$ , 那么它是左手征的, 如果它满足 $`\mathcal{D} _ { L } \boldsymbol { \Phi } = 0`$ , 那么它是右手征的.
对于一组超场 $`\Phi _ { n }`$ , 如果它们都满足 $`\mathcal{D} _ { R } \boldsymbol { \Phi } _ { n } = 0`$ 或 $`\mathcal{D} _ { L } \boldsymbol { \Phi } _ { n } = 0`$ , 它们的任意函数 $`f ( \Phi )`$ 也将满足 $`\mathcal{D} _ { R } f ( \Phi ) = 0`$ 或 $`\mathcal{D} _ { L } f ( \Phi ) = 0`$ , 因此也分别是左手征和右手征的.
但是, 左手征超场和右手征超场的函数在一般情况下根本不是手征的.
左手征超场的表示(26.3.21)使得解出它们的乘积性质变得很容易.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81dab423c0265e13f79d">
		$$
		\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
		$$
	</synced_block_reference>
</callout>
例如, 如果 $`\Phi _ { 1 }`$ 和 $`\Phi _ { 2 }`$ 是两个左手征超场, 那么它们的乘积 $`\Phi = \Phi _ { 1 } \Phi _ { 2 }`$ 是左手征超场, 分量是
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81a28fc6ca49d397ab7e">
	$$
	\begin{array} { r l } & { \phi = \phi _ { 1 } \phi _ { 2 } \ : , } \\ & { \psi _ { L } = \phi _ { 1 } \psi _ { 2 L } + \phi _ { 2 } \psi _ { 1 L } \ : , } \\ & { \mathcal{F} = \phi _ { 1 } \mathcal{F} _ { 2 } + \phi _ { 2 } \mathcal{F} _ { 1 } - \left( \psi _ { 1 L } ^ { \mathrm { T } } \epsilon \psi _ { 2 L } \right) \ : . } \end{array} \tag{26.3.27-26.3.29}
	$$
</synced_block>
理论中出现了手征超场打开了构造超对称作用量的另一种可能性.
对变换规则(26.3.16)的观察表明, 左手征超场 $`\Phi`$ 的 $`\mathcal{F}`$ -项在超对称变换下的变化是一个导数项, 这使得对任何左手征超场的 $`\mathcal{F}`$ -项的积分是超对称的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81568065f84f9597622a">
		$$
		\begin{array} { r l } & { \delta \psi _ { L } = \sqrt { 2 } \partial _ { \mu } \phi \gamma ^ { \mu } \alpha _ { R } + \sqrt { 2 } \mathcal{F} \alpha _ { L } , } \\ & { \delta \mathcal{F} = \sqrt { 2 } \Big ( \overline { { \alpha _ { L } } } \not\!\partial\, \psi _ { L } \Big ) , } \\ & { \delta \phi = \sqrt { 2 } \Big ( \overline { { \alpha _ { R } } } \psi _ { L } \Big ) , } \end{array} \tag{26.3.15-26.3.17}
		$$
	</synced_block_reference>
</callout>
因此我们可以将超对称作用量构建为
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8185b369e09fb8d66190">
	$$
	I = \int \mathrm { d } ^ { 4 } x \left[ f \right] _ { \mathcal{F} } + \int \mathrm { d } ^ { 4 } x \left[ f \right] _ { \mathcal{F} } ^ { \ast } + \frac { 1 } { 2 } \int \mathrm { d } ^ { 4 } x \left[ K \right] _ { D } , \tag{26.3.30}
	$$
</synced_block>
其中 $`f`$ 和 $`K`$ 分别是左手征超场和一般实超场且是用基本超场构建的.
$`f`$ 和 $`K`$ 能够依赖于什么? 如果函数 $`f`$ 只依赖于左手征基本超场 $`\Phi _ { n }`$ 而不依赖与它们的右手征复共轭, 那么 $`f`$ 将是左手征的.
另一方面, 手征超场的超导数不是手征的, 所以我们不能随意地在 $`f`$ 中引入 $`\Phi _ { n }`$ 的超导数.
正确的是, 对于不是左手征的超场 $`S`$ (例如包含左手征超场的复共轭的超场), 一对右超导数作用在上面会给出左手征超场, 原因是独立的右超导数只有两个且互相反对易:
$$
\mathcal{D} _ { R \alpha } ( \mathcal{D} _ { R \beta } \mathcal{D} _ { R \gamma } S ) = 0 .
$$
然而, 对于任何以这种方式构建的函数 $`f`$ , 它的 $`\mathcal{F}`$ -项对作用量的贡献与其它某个复合超场的 $`D`$ 项对作用量的贡献相同.
由于 $`\mathcal{D}`$ 反对易, 通过用两个 $`\mathcal{D} _ { R }`$ 作用在一般超场 $`S`$ 上的得到最一般左手征超场可以表示成 $`( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } ) S`$ .
如果超势中的一个左手征超场是这种形式, 由于每个 $`\mathcal{D} _ { R }`$ 湮灭超势中所有其它超场, 我们可以将整个超势写成 $`f = ( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } ) h`$ , 其中 $`h`$ 是另外一个超场.
现在
$$
\begin{array} { r } { \left( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } \right) \left( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \right) = - 4 , } \end{array}
$$
所以, 除了对作用量没有贡献的时空导数外, $`( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } ) h`$ 是 $`- ( { \theta } _ { R } ^ { \mathrm { T } } { \epsilon } { \theta } _ { R } ) / 4`$ 在 $`h`$ 中的系数.
但是, 再一次地, 除时空导数外, $`[ f ] _ { \mathcal{F} }`$ 是 $`( \theta _ { L } ^ { \mathrm { { T } } } \epsilon \theta _ { L } )`$ 在 $`f`$ 中的系数, 所以 $`[ ( \mathcal{D} _ { R } ^ { \mathrm { T } } \epsilon \mathcal{D} _ { R } ) h ] _ { \mathcal{F} }`$ 等于 $`- ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } ) ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } ) / 4`$ $`= - ( \bar { \theta } \gamma _ { 5 } \theta ) ^ { 2 } / 4`$ 在 $`h`$ 中的系数, 因此
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f819f9c1adf812ce93c65">
	$$
	\int \mathrm { d } ^ { 4 } x \left[ ( { \mathcal{D} } _ { R } ^ { \mathrm { T } } \epsilon { \mathcal{D} } _ { R } ) h \right] _ { { \mathcal{F} } } = 2 \int \mathrm { d } ^ { 4 } x [ h ] _ { D } . \tag{26.3.31}
	$$
</synced_block>
因此, 对于那些依赖于形式为 $`\mathcal{D} _ { R \beta } \mathcal{D} _ { R \gamma } S`$ 的左手征超场的项, 我们不需要把这些项的贡献计入 $`f`$ ——任何这样的项将会被纳入所有可能的 $`D`$ -项中.
当 $`f`$ 被表示成仅是基本手征超场而非它们的超导数或时空导数的函数时, 它被称为超势.
与之相反, 实标量函数 $`K`$ 一般既是左手征手征超场 $`\Phi _ { n }`$ 和它们的复共轭 $`\Phi _ { n } ^ { * }`$ 的函数, 也是它们的超导数和时空导数的函数, 它被称为Kähler势.
(任何右手征超场都是某个左手征超场的复共轭, 所以这里假定 $`K`$ 只依赖于左手征超场和它们的复共轭是不失一般性的.) 然而, 以这种方式获得的 $`K`$ 并不都给出不同的作用量.
例如, 手征超场没有 $`D`$ -项, 所以如果两个 $`K`$ 只相差一个手征超场, 那么它们对作用量的贡献是相同的.
通过在超空间中部分积分, 我们也可以在不改变作用量的情况下改变 $`K`$ 的形式.
对于任意超场的超导数 $`\mathcal{D} _ { \alpha } S`$ , 因为
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81b9b6e9f04b1815700e">
	$$
	\int \mathrm { d } ^ { 4 } x \left[ \mathcal{D} _ { \alpha } S \right] _ { D } = 0 , \tag{26.3.32}
	$$
</synced_block>
所以它的 $`D`$ -项对作用量无贡献.
为了看到这点, 回忆起
$$
\mathcal{D} _ { \alpha } S = \Big ( \gamma _ { 5 } \epsilon \Big ) _ { \alpha \beta } \frac { \partial S } { \partial \theta _ { \beta } } - ( \gamma ^ { \mu } \theta ) _ { \alpha } \frac { \partial S } { \partial x ^ { \mu } } .
$$
由于 $`S`$ 最多是 $`\theta`$ 的四次多项式, $`\mathcal{D} _ { \alpha } S`$ 中的第一项最多是 $`\theta`$ 的三次多项式, 因此它的 $`D`$ -项只要非零就必是一个导数, 而第二项也是一个时空导数, 所以它的 $`D`$ -项也是时空导数, 因此 $`\mathcal{D} _ { \alpha } S`$ 中的第一项和第二项对方程(26.3.32)中的积分都没有贡献.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81b9b6e9f04b1815700e">
		$$
		\int \mathrm { d } ^ { 4 } x \left[ \mathcal{D} _ { \alpha } S \right] _ { D } = 0 , \tag{26.3.32}
		$$
	</synced_block_reference>
</callout>
另外, 超导数的作用满足分配率, 所以从方程(26.3.32)可以得出, 我们可以在超空间做分部积分: 对于任何两个玻色超场 $`S _ { 1 }`$ 和 $`S _ { 2 }`$ ,
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81b9b6e9f04b1815700e">
		$$
		\int \mathrm { d } ^ { 4 } x \left[ \mathcal{D} _ { \alpha } S \right] _ { D } = 0 , \tag{26.3.32}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f812494dbfb2d44a29a70">
	$$
	\int \mathrm { d } ^ { 4 } x [ S _ { 1 } \mathcal{D} _ { \alpha } S _ { 2 } ] _ { D } = - \int \mathrm { d } ^ { 4 } x [ S _ { 2 } \mathcal{D} _ { \alpha } S _ { 1 } ] _ { D } . \tag{26.3.33}
	$$
</synced_block>
在26.4节和26.8节, 我们将会细致考察 $`f`$ 和 $`K`$ 只依赖基本超场但不依赖它们的超导数或普通导数的情况.
我们在上一节看到, 在宇称守恒的理论中, 空间反演算符在一般标量超场上的效应是对它的变换做变换 $`x ^ { \mu } \to ( \Lambda _ { P } ) ^ { \mu } {} _ { \nu } x ^ { \nu }`$ 和 $`\theta \to - \mathrm{i} \beta \theta`$ , 然后再乘上可能的相位 $`\eta`$ .
在这些变换下, 方程(26.3.21)和(26.3.22)中的变量 $`x _ { \pm } ^ { \mu }`$ 的变化是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81dab423c0265e13f79d">
		$$
		\begin{array} { r l } & { \Phi ( x , \theta ) = \phi ( x _ { + } ) - \sqrt { 2 } \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \psi _ { L } ( x _ { + } ) \Big ) + \mathcal{F} ( x _ { + } ) \Big ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } \Big ) , } \\ & { \tilde { \Phi } ( x , \theta ) = \tilde { \phi } ( x _ { - } ) + \sqrt { 2 } \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \psi _ { R } ( x _ { - } ) \Big ) - \tilde { \mathcal{F} } ( x _ { - } ) \Big ( \theta _ { R } ^ { \mathrm { T } } \epsilon \theta _ { R } \Big ) , } \end{array} \tag{26.3.21-26.3.22}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f817baf8ecb04f7b04f28">
	$$
	x _ { \pm } ^ { \mu } \to ( \Lambda _ { P } x ) ^ { \mu } \pm { \textstyle \frac { 1 } { 2 } } \Bigl ( \bar { \theta } \beta \gamma _ { 5 } \gamma ^ { \mu } \beta \theta \Bigr ) = ( \Lambda _ { P } x _ { \mp } ) ^ { \mu } , \tag{26.3.34}
	$$
</synced_block>
以及 $`\theta _ { L } \to - \mathrm{i} \beta \theta _ { R }`$ 和 $`\theta _ { R } \to - \mathrm{i} \beta \theta _ { L }`$ .
因此空间反演将左手征超场变到右手征超场, 并将右手征超场变到左手征超场.
分量场中包含相同粒子的产生湮灭算符且这些粒子也被左手征超场 $`\Phi`$ 产生湮灭的唯一右手征超场是 $`\tilde { \Phi } \propto \Phi ^ { * }`$ , 所以 $`\mathsf { P } ^ { - 1 } \Phi \mathsf { P }`$ 必须正比于 $`\Phi ^ { * }`$ .
通过对 $`\Phi`$ 的相位做合适的选择, 我么可以重新整理这一变换规则使其变成
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81a2b79ac4420b0fdf68">
	$$
	\mathsf { P } ^ { - 1 } \Phi ( x , \theta ) \mathsf { P } = \Phi ^ { * } ( \Lambda _ { P } x , - \mathrm{i} \beta \theta ) . \tag{26.3.35}
	$$
</synced_block>
以分量场的形式, 这个变换是
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8108a418db9e9e4630f7">
	$$
	\begin{array} { r l } & { \mathsf { P } ^ { - 1 } \phi ( x ) \mathsf { P } = \phi ^ { * } \bigl ( \Lambda _ { P } x \bigr ) , } \\ & { \mathsf { P } ^ { - 1 } \psi _ { L } ( x ) \mathsf { P } = - \mathrm{i} \epsilon \gamma _ { 5 } \beta \psi _ { L } ^ { * } \bigl ( \Lambda _ { P } x \bigr ) , } \\ & { \mathsf { P } ^ { - 1 } \mathcal{F} ( x ) \mathsf { P } = \mathcal{F} ^ { * } ( \Lambda _ { P } x ) . } \end{array} \tag{26.3.36}
	$$
</synced_block>
还有另一种可能的对称性类型, 称为 $`R`$ -对称性, 它在26.5节将要讨论的一些超对称自发破缺模型中十分重要, 也会在 27.6 节被用来证明不可重整定理.
正如在 25.2 节中所提及的, 在简单 $`N = 1`$ 超对称理论中, $`R`$ -对称性就是在 $`U ( 1 )`$ 变换下的不变性, 在这个变换下, 生成元的左手分量(在25.2节记做 $`{ \mathcal{Q} } _ { a }`$ )携带不为零的量子数, 例如 $`-1`$ , 而它们的共轭, 超对称生成元的右手分量携带相反的量子数 $`+ 1`$ .
对方程(26.2.2)的观察表明, $`\theta`$ 超空间坐标在 $`R`$ -变换下的性质是不平庸的:$`\theta _ { L }`$ 携带 $`R`$ 量子数 $`+ 1`$ , 而正比于 $`\theta _ { L } ^ { * }`$ 的 $`\theta _ { R }`$ 携带 $`R`$ 量子数 $`-1`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f812e8a66c9b63a4d3331">
		$$
		\mathcal{Q} \equiv - \frac { \partial } { \partial \bar { \theta } } + \gamma ^ { \mu } \theta \frac { \partial } { \partial x ^ { \mu } } , \tag{26.2.2}
		$$
	</synced_block_reference>
</callout>
另外, 整个超场可以被赋予一个 $`R`$ -量子数.
如果我们给左手征超场 $`\Phi`$ 赋予 $`R`$ 量子数 $`R _ { \Phi }`$ , 那么它的标量分量 $`\phi`$ 会有相同的 $`R`$ 量子数, 左手征旋量分量 $`\psi _ { L }`$ 有 $`R _ { \psi } = R _ { \Phi } - 1`$ , 辅助场 $`\mathcal{F}`$ 有 $`R _ { \mathcal{F} } = R _ { \Phi } - 2`$ .
特别地, 为了使超势项 $`\textstyle \int \mathrm { d } ^ { 4 } x [ f ] _ { \mathcal{F} }`$ 是$`R`$ 守恒的,超势本身必须有 $`R _ { f } = + 2`$ ,所以如果 $`f`$ 依赖单个左手征超场 $`\Phi`$ ,那么它必须正比于 $`\Phi ^ { 2 / R _ { \Phi } }`$ 将其写成另一种形式, 如果 $`f ( \Phi )`$ 是正比于 $`\Phi ^ { 2 }`$ 的纯质量项, 那么我们必须选 $`R _ { \Phi } = + 1`$ , 而如果 $`f ( \Phi )`$ 是正比于 $`\Phi ^ { 3 }`$ 的纯相互作用项, 那么我们必须选 $`R _ { \Phi } = 2 / 3`$ .
另一方面, 对方程(26.2.10)的观察表明, 超场的 $`D`$ -项和超场的 $`R`$ 值相同, 所以为了使作用量中的 $`\int \mathrm { d } ^ { 4 } x \left[ K \right] _ { D }`$ 项c是 $`R`$ 守恒的, 唯一需要的是 $`K`$ 有 $`R = 0`$ , 而无论我们给 $`\Phi`$ 赋予什么样的 $`R`$ 值, 只要 $`K`$ 中的每一项拥有个数相同的 $`\Phi`$ 因子和 $`\Phi ^ { * }`$ 因子, $`K`$ 就满足要求.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81a5ae59cc8919a6be32">
		$$
		\begin{array} { l } { { S ( x , \theta ) = C ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \omega ( x ) \Big ) - \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) M ( x ) - \frac { 1 } { 2 } \Big ( \bar { \theta } \theta \Big ) N ( x ) } } \\ { { \qquad + \frac { \mathrm{i} } { 2 } \Big ( \bar { \theta } \gamma _ { 5 } \gamma _ { \mu } \theta \Big ) V ^ { \mu } ( x ) - \mathrm{i} \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) \Bigg ( \bar { \theta } \bigg [ \lambda ( x ) + \frac { 1 } { 2 } \not\!\partial\, \omega ( x ) \bigg ] \Bigg ) } } \\ { { \qquad - \frac { 1 } { 4 } \Big ( \bar { \theta } \gamma _ { 5 } \theta \Big ) ^ { 2 } \Bigg ( D ( x ) + \frac { 1 } { 2 } \Box C ( x ) \Bigg ) . } } \end{array} \tag{26.2.10}
		$$
	</synced_block_reference>
</callout>
当然, 为什么作用量应该遵循 $`R`$ -对称性, 亦或 $`R`$ -对称性为什么没有自发破缺, 这些现象并没有普遍的原因.
\\\* \\\* \\\*
还存在其它约束超场使其产生其他类型的场超多重态的方式.
其中较常见的是线性超场.
为了掌握这类超场的定义条件, 我们注意到, 如果 $`S`$ 是一般超场, 那么我们可以构建手征超场
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f816490acdd36871f2fe9">
	$$
	S ^ { \prime } \equiv \frac { 1 } { 4 } \Big ( \bar { \mathcal{D} } \mathcal{D} \Big ) S . \tag{26.3.37}
	$$
</synced_block>
这是手征超场是因为它可以写成左手征超场 $`\frac { 1 } { 4 } \big ( \bar { \mathcal{D} } _ { L } \mathcal{D} _ { L } \big ) S`$ 和左手征超场 $`\begin{array} { r l } { \frac { 1 } { 4 } \big ( \bar { \mathcal{D} } _ { R } \mathcal{D} _ { R } \big ) S } & { { } } \end{array}`$ 的和.
用 $`S`$ 的分量, 它的分量可以写成
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8185bef9d08e130abe9a">
	$$
	\begin{array} { l } { { C ^ { \prime } = N , } } \\ { { \omega ^ { \prime } = \lambda + \not\!\partial\, \omega , } } \\ { { M ^ { \prime } = - \partial _ { \mu } V ^ { \mu } , } } \\ { { N ^ { \prime } = D + \Box C , } } \\ { { V _ { \mu } ^ { \prime } = - \partial _ { \mu } M , } } \\ { { \lambda ^ { \prime } = D ^ { \prime } = 0 . } } \end{array} \tag{26.3.39-26.3.42}
	$$
</synced_block>
如果以这种方式定义的超场 $`S ^ { \prime }`$ 为零
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f81fc838fd0730e9af007">
	$$
	\left( \bar { \mathcal D } \mathcal D \right) \boldsymbol S = \boldsymbol 0 , \tag{26.3.44}
	$$
</synced_block>
或者用它的分量表示
<synced_block url="https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0#34cee2b74b3f8137afdbc9aa4ba36142">
	$$
	N = M = \partial _ { \mu } V ^ { \mu } = 0 , \qquad \lambda = - \not\!\partial\, \omega , \qquad D = - \Box C , \tag{26.3.45}
	$$
</synced_block>
那么多重态 $`S`$ 就被称作是线性的.
这种构造留下了四个独立的玻色场—— $`C`$ 和使得条件 $`\partial _ { \mu } V ^ { \mu } =`$ 0得以满足的 $`V ^ { \mu }`$ 的三个分量, 以及四个独立的费米场—— Majorana 4 -旋量 $`\omega`$ 的四个分量.
我们将会在26.6节看到, 那里定义的流超场的 $`V _ { \mu }`$ -项是与对称变换相联系的守恒流, 这个超场是线性超场.
</content>
</page>
