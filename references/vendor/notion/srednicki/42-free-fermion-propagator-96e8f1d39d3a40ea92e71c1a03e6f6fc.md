Here is the result of "view" for the Page with URL https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc as of 2026-04-27T16:53:05.125Z:
<page url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"42. The free fermion propagator"}
</properties>
<content>
Consider a free Dirac field
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#04c56614ba4144d5b9a611a10c430e57">
	$$
	\begin{array} { l } { { \displaystyle \Psi ( x ) = \sum _ { s = \pm } \int \widetilde { d p } \left[ b _ { s } ( { \bf p } ) u _ { s } ( { \bf p } ) e ^ { i p x } + d _ { s } ^ { \dagger } ( { \bf p } ) v _ { s } ( { \bf p } ) e ^ { - i p x } \right] } , } \\{ { \displaystyle \overline { { \Psi } } ( y ) = \sum _ { s ^ { \prime } = \pm } \int \widetilde { d p } ^ { \prime } \left[ b _ { s ^ { \prime } } ^ { \dagger } ( { \bf p } ^ { \prime } ) \overline { { { u } } } _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) e ^ { - i p ^ { \prime } y } + d _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) \overline { { { v } } } _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) e ^ { i p ^ { \prime } y } \right] } , } \end{array} \tag{42.1-42.2}
	$$
</synced_block>
where
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#cf24aa171a234eb49d32f1c7b5d452a0">
	$$
	b _ { s } ( { \bf p } ) | 0 \rangle = d _ { s } ( { \bf p } ) | 0 \rangle = 0 , \tag{42.3}
	$$
</synced_block>
and
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#f1f0ad11fec04c809bea9f89a89c1e52">
	$$
	\begin{array} { r l } & { \{ b _ { s } ( \mathbf { p } ) , b _ { s ^ { \prime } } ^ { \dagger } ( \mathbf { p ^ { \prime } } ) \} = ( 2 \pi ) ^ { 3 } \delta ^ { 3 } ( \mathbf { p - p ^ { \prime } } ) 2 \omega \delta _ { s s ^ { \prime } } \ , } \\& { \{ d _ { s } ( \mathbf { p } ) , d _ { s ^ { \prime } } ^ { \dagger } ( \mathbf { p ^ { \prime } } ) \} = ( 2 \pi ) ^ { 3 } \delta ^ { 3 } ( \mathbf { p - p ^ { \prime } } ) 2 \omega \delta _ { s s ^ { \prime } } \ , } \end{array} \tag{42.4-42.5}
	$$
</synced_block>
and all the other possible anticommutators between $`b`$ and $`d`$ operators (and their hermitian conjugates) vanish.
We wish to compute the Feynman propagator
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#88a42af1cf0d4d7283938e106db8aa9b">
	$$
	S ( x - y ) _ { \alpha \beta } \equiv i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle , \tag{42.6}
	$$
</synced_block>
where T denotes the time-ordered product,
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#c41b1bd9e1644937896bd1e1300712f7">
	$$
	{ \mathrm { T } } \Psi _ { \alpha } ( x ) { \overline { { \Psi } } } _ { \beta } ( y ) \equiv \theta ( x ^ { 0 } - y ^ { 0 } ) \Psi _ { \alpha } ( x ) { \overline { { \Psi } } } _ { \beta } ( y ) - \theta ( y ^ { 0 } - x ^ { 0 } ) { \overline { { \Psi } } } _ { \beta } ( y ) \Psi _ { \alpha } ( x ) , \tag{42.7}
	$$
</synced_block>
and $`\theta ( t )`$ is the unit step function. Note the minus sign in the second term;<br>this is needed because $`\Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) = - \overline { { { \Psi } } } _ { \beta } ( y ) \Psi _ { \alpha } ( x )`$ when $`x ^ { 0 } \neq y ^ { 0 }`$ .
We can now compute $`\langle 0 | \Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle`$ and $`\langle 0 | \overline { { \Psi } } _ { \beta } ( y ) \Psi _ { \alpha } ( x ) | 0 \rangle`$ by inserting eqs. (42.1) and (42.2), and then using eqs. (42.3)–(42.5). We get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#3a6daa704b884cc1810e0d5b34d4a5aa">
		$$
		\begin{array} { l } { { \displaystyle \Psi ( x ) = \sum _ { s = \pm } \int \widetilde { d p } \left[ b _ { s } ( { \bf p } ) u _ { s } ( { \bf p } ) e ^ { i p x } + d _ { s } ^ { \dagger } ( { \bf p } ) v _ { s } ( { \bf p } ) e ^ { - i p x } \right] } , } \\{ { \displaystyle \overline { { \Psi } } ( y ) = \sum _ { s ^ { \prime } = \pm } \int \widetilde { d p } ^ { \prime } \left[ b _ { s ^ { \prime } } ^ { \dagger } ( { \bf p } ^ { \prime } ) \overline { { { u } } } _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) e ^ { - i p ^ { \prime } y } + d _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) \overline { { { v } } } _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) e ^ { i p ^ { \prime } y } \right] } , } \end{array} \tag{42.1-42.2}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#122d5ff5b4b24f20aabbcf7abbaaffc9">
		$$
		b _ { s } ( { \bf p } ) | 0 \rangle = d _ { s } ( { \bf p } ) | 0 \rangle = 0 , \tag{42.3}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#4c5313e95dbf415399a26c11aff61f36">
		$$
		\begin{array} { r l } & { \{ b _ { s } ( \mathbf { p } ) , b _ { s ^ { \prime } } ^ { \dagger } ( \mathbf { p ^ { \prime } } ) \} = ( 2 \pi ) ^ { 3 } \delta ^ { 3 } ( \mathbf { p - p ^ { \prime } } ) 2 \omega \delta _ { s s ^ { \prime } } \ , } \\& { \{ d _ { s } ( \mathbf { p } ) , d _ { s ^ { \prime } } ^ { \dagger } ( \mathbf { p ^ { \prime } } ) \} = ( 2 \pi ) ^ { 3 } \delta ^ { 3 } ( \mathbf { p - p ^ { \prime } } ) 2 \omega \delta _ { s s ^ { \prime } } \ , } \end{array} \tag{42.4-42.5}
		$$
	</synced_block>
</callout>
$$
\begin{array} { l } { { \langle 0 | \Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle } } \\{ { \ } } \\{ { \displaystyle \quad = \sum _ { s , s ^ { \prime } } \int \widetilde { d p } \widetilde { d p } ^ { \prime } e ^ { i p x } e ^ { - i p ^ { \prime } y } u _ { s } ( \mathbf { p } ) _ { \alpha } \overline { { { u } } } _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) _ { \beta } \langle 0 | b _ { s } ( \mathbf { p } ) b _ { s ^ { \prime } } ^ { \dagger } ( \mathbf { p } ^ { \prime } ) | 0 \rangle } } \\{ { \ } } \\{ { \displaystyle \quad = \sum _ { s , s ^ { \prime } } \int \widetilde { d p } \widetilde { d p } ^ { \prime } e ^ { i p x } e ^ { - i p ^ { \prime } y } u _ { s } ( \mathbf { p } ) _ { \alpha } \overline { { { u } } } _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) _ { \beta } \left( 2 \pi \right) ^ { 3 } \delta ^ { 3 } ( \mathbf { p } - \mathbf { p } ^ { \prime } ) 2 \omega \delta _ { s s ^ { \prime } } } } \\{ { \ } } \\{ { \displaystyle \quad = \sum _ { s } \int \widetilde { d p } e ^ { i p ( x - y ) } u _ { s } ( \mathbf { p } ) _ { \alpha } \overline { { { u } } } _ { s } ( \mathbf { p } ) _ { \beta } } } \\{ { \ } } \\{ { \displaystyle \quad = \int \widetilde { d p } e ^ { i p ( x - y ) } \left( - j + m \right) _ { \alpha \beta } . } } \end{array}
$$
To get the last line, we used a result from section 38. Similarly,
$$
\begin{array} { r l r } { { \langle 0 | \widetilde { \Psi } _ { \beta } ( y ) \Psi _ { \alpha } ( x ) | 0 \rangle } } \\& { } & { = \sum _ { s , s ^ { \prime } } \widetilde { \int { d p } } \widetilde { d p } ^ { \prime } e ^ { - i p x } e ^ { i p ^ { \prime } y } v _ { s } ( \mathbf { p } ) _ { \alpha } \overline { { v } } _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) _ { \beta } \langle 0 | d _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) d _ { s } ^ { \dagger } ( \mathbf { p } ) | 0 \rangle } \\& { } & { = \sum _ { s , s ^ { \prime } } \widetilde { \int { d p } } \widetilde { d p } ^ { \prime } e ^ { - i p x } e ^ { i p ^ { \prime } y } v _ { s } ( \mathbf { p } ) _ { \alpha } \overline { { v } } _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) _ { \beta } \langle 2 \pi \rangle ^ { 3 } \delta ^ { 3 } ( \mathbf { p } - \mathbf { p } ^ { \prime } ) 2 \omega \delta _ { s s ^ { \prime } } } \\& { } & { = \displaystyle \sum _ { s } \int \widetilde { d p } e ^ { - i p ( x - y ) } v _ { s } ( \mathbf { p } ) _ { \alpha } \overline { { v } } _ { s } ( \mathbf { p } ) _ { \beta } } \\& { } & { = \displaystyle \int \widetilde { d p } e ^ { - i p ( x - y ) } ( - p / - m ) _ { \alpha \beta } . } \end{array}
$$
We can combine eqs. (42.8) and (42.9) into a compact formula for the timeordered product by means of the identity
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#7e62ac8c6257470ebb2ffcc783149717">
	$$
	\begin{array} { l } { { \displaystyle \int \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } \frac { e ^ { i p ( x - y ) } f ( p ) } { p ^ { 2 } + m ^ { 2 } - i \epsilon } = i \theta ( x ^ { 0 } - y ^ { 0 } ) \int \widetilde { d p } e ^ { i p ( x - y ) } f ( p ) \ ~ } } \\{ { \displaystyle ~ + i \theta ( y ^ { 0 } - x ^ { 0 } ) \int \widetilde { d p } e ^ { - i p ( x - y ) } f ( - p ) ~ , } } \end{array} \tag{42.10}
	$$
</synced_block>
where $`f ( \boldsymbol p )`$ is a polynomial in $`p`$ ; the derivation of eq. (42.10) was sketched in section 8. We get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#10dd671cb70649d197342dd0122d94b1">
		$$
		\begin{array} { l } { { \displaystyle \int \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } \frac { e ^ { i p ( x - y ) } f ( p ) } { p ^ { 2 } + m ^ { 2 } - i \epsilon } = i \theta ( x ^ { 0 } - y ^ { 0 } ) \int \widetilde { d p } e ^ { i p ( x - y ) } f ( p ) \ ~ } } \\{ { \displaystyle ~ + i \theta ( y ^ { 0 } - x ^ { 0 } ) \int \widetilde { d p } e ^ { - i p ( x - y ) } f ( - p ) ~ , } } \end{array} \tag{42.10}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#2b0967e8dd5d4a00a533ea1c506b3829">
	$$
	\langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) { \overline { { \Psi } } } _ { \beta } ( y ) | 0 \rangle = { \frac { 1 } { i } } \int { \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } } e ^ { i p ( x - y ) } { \frac { ( - p / + m ) _ { \alpha \beta } } { p ^ { 2 } + m ^ { 2 } - i \epsilon } } , \tag{42.10-42.11}
	$$
</synced_block>
and so
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#fab1af681fd342b1983b69eb65218d2e">
	$$
	S ( x - y ) _ { \alpha \beta } = \int \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } e ^ { i p ( x - y ) } \frac { ( - p / + m ) _ { \alpha \beta } } { p ^ { 2 } + m ^ { 2 } - i \epsilon } . \tag{42.12}
	$$
</synced_block>
Note that $`S ( x - y )`$ is a Green’s function for the Dirac wave operator:
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#b794929191304b92ad43927c3a34a77f">
	$$
	( - i \partial / _ { x } + m ) _ { \alpha \beta } S ( x - y ) _ { \beta \gamma } = \int \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } e ^ { i p ( x - y ) } \frac { ( p / + m ) _ { \alpha \beta } ( - p / + m ) _ { \beta \gamma } } { p ^ { 2 } + m ^ { 2 } - i \epsilon } \tag{42.13}
	$$
</synced_block>
Similarly,
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#30f061cb36064ecf835ae5205a79f6fd">
	$$
	\begin{array} { l } { { S ( x - y ) _ { \alpha \beta } ( + i \overleftarrow { \partial _ { y } } + m ) _ { \beta \gamma } = \displaystyle \int \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } e ^ { i p ( x - y ) } \frac { ( - p / + m ) _ { \alpha \beta } ( p / + m ) _ { \beta \gamma } } { p ^ { 2 } + m ^ { 2 } - i \epsilon } } } \\{ { \mathrm { ~ } = \displaystyle \int \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } e ^ { i p ( x - y ) } \frac { ( p ^ { 2 } + m ^ { 2 } ) \delta _ { \alpha \gamma } } { p ^ { 2 } + m ^ { 2 } - i \epsilon } } } \\{ { \mathrm { ~ } = \delta ^ { 4 } ( x - y ) \delta _ { \alpha \gamma } . } } \end{array} \tag{42.14}
	$$
</synced_block>
We can also consider $`\langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \Psi _ { \beta } ( y ) | 0 \rangle`$ and $`\langle 0 | \mathrm { T } \overline { { \Psi } } _ { \alpha } ( x ) \overline { { \Psi } } _ { \beta } ( y ) | 0 \rangle`$ , but it is easy to see that now there is no way to pair up a $`b`$ with a $`b ^ { \dagger }`$ or a $`d`$ with a $`d ^ { \dagger }`$ , and so
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#9ac97235d0d44d3b8cfd04d738c4496a">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \Psi _ { \beta } ( y ) | 0 \rangle = 0 , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \langle 0 | \mathrm { T } \overline { { { \Psi } } } _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle = 0 . } } \end{array} \tag{42.15-42.16}
	$$
</synced_block>
Next, consider a Majorana field
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#13ac4d75bbe0423bbdcdb2b06fce6330">
	$$
	\begin{array} { l } { { \displaystyle \Psi ( x ) = \sum _ { s = \pm } \int \widetilde { d p } \left[ b _ { s } ( { \bf p } ) u _ { s } ( { \bf p } ) e ^ { i p x } + b _ { s } ^ { \dagger } ( { \bf p } ) v _ { s } ( { \bf p } ) e ^ { - i p x } \right] } , } \\{ { \displaystyle \overline { { \Psi } } ( y ) = \sum _ { s ^ { \prime } = \pm } \int \widetilde { d p } ^ { \prime } \left[ b _ { s ^ { \prime } } ^ { \dagger } ( { \bf p } ^ { \prime } ) \overline { { { u } } } _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) e ^ { - i p ^ { \prime } y } + b _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) \overline { { { v } } } _ { s ^ { \prime } } ( { \bf p } ^ { \prime } ) e ^ { i p ^ { \prime } y } \right] . } } \end{array} \tag{42.17-42.18}
	$$
</synced_block>
It is easy to see that $`\langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle`$ is the same as it is in the Dirac case; the only difference in the calculation is that we would have $`b`$ and $`b ^ { \dagger }`$ in place of $`d`$ and $`d ^ { \dagger }`$ in the second line of eq. (42.9), and this does not change the final result. Thus,
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#7fb97eb2dd194763821f68f06351e043">
	$$
	i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) { \overline { { \Psi } } } _ { \beta } ( y ) | 0 \rangle = S ( x - y ) _ { \alpha \beta } , \tag{42.19}
	$$
</synced_block>
where $`S ( x - y )`$ is given by eq. (42.12).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#f2eb1c32150149afa800c287c8948c00">
		$$
		S ( x - y ) _ { \alpha \beta } = \int \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } e ^ { i p ( x - y ) } \frac { ( - p / + m ) _ { \alpha \beta } } { p ^ { 2 } + m ^ { 2 } - i \epsilon } . \tag{42.12}
		$$
	</synced_block>
</callout>
However, eqs. (42.15) and (42.16) no longer hold for a Majorana field. Instead, the Majorana condition $`{ \overline { { \Psi } } } = \Psi ^ { \mathrm { T } } { \mathcal { C } }`$ , which can be rewritten as
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#ddaff114be7841d5966807e7cda85d9c">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \Psi _ { \beta } ( y ) | 0 \rangle = 0 , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \langle 0 | \mathrm { T } \overline { { { \Psi } } } _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle = 0 . } } \end{array} \tag{42.15-42.16}
		$$
	</synced_block>
</callout>
$`\Psi ^ { \mathrm { T } } = \overline { { \Psi } } \mathcal { C } ^ { - 1 }`$ , implies
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#32926be4e0ce4fc992462df4e2045076">
	$$
	\begin{array} { c } { { i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \Psi _ { \beta } ( y ) | 0 \rangle = i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \gamma } ( y ) | 0 \rangle ( \mathcal { C } ^ { - 1 } ) _ { \gamma \beta } } } \\{ { { } } } \\{ { { } = [ S ( x - y ) \mathcal { C } ^ { - 1 } ] _ { \alpha \beta } . } } \end{array} \tag{42.20}
	$$
</synced_block>
Similarly, using $`{ \mathcal { C } } ^ { \mathrm { T } } = { \mathcal { C } } ^ { - 1 }`$ , we can write the Majorana condition as $`\overline { { \Psi } } ^ { \mathrm { T } } =`$ $`\mathcal { C } ^ { - 1 } \Psi`$ , and so
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#8e59c02cb40e443093ce162607b02594">
	$$
	\begin{array} { c } { { i \langle 0 | \mathrm { T } \overline { { { \Psi } } } _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle = i ( \mathcal { C } ^ { - 1 } ) _ { \alpha \gamma } \langle 0 | \mathrm { T } \Psi _ { \gamma } ( x ) \overline { { { \Psi } } } _ { \beta } ( y ) | 0 \rangle } } \\{ { { } } } \\{ { { } = [ \mathcal { C } ^ { - 1 } S ( x - y ) ] _ { \alpha \beta } . } } \end{array} \tag{42.21, 42.20}
	$$
</synced_block>
Of course, $`{ \mathcal { C } } ^ { - 1 } = - { \mathcal { C } }`$ , but it will prove more convenient to leave eqs. (42.20) and (42.21) as they are.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#ad0b0478da12458b8eef88a0819d416f">
		$$
		\begin{array} { c } { { i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \Psi _ { \beta } ( y ) | 0 \rangle = i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \gamma } ( y ) | 0 \rangle ( \mathcal { C } ^ { - 1 } ) _ { \gamma \beta } } } \\{ { { } } } \\{ { { } = [ S ( x - y ) \mathcal { C } ^ { - 1 } ] _ { \alpha \beta } . } } \end{array} \tag{42.20}
		$$
	</synced_block>
</callout>
We can also consider the vacuum expectation value of a time-ordered product of more than two fields. In the Dirac case, we must have an equal number of $`\Psi \mathrm { s }`$ and $`\overline { { \Psi } }`$ s to get a nonzero result; and then, the $`\Psi`$ s and $`\overline { { \Psi } }`$ s must pair up to form propagators. There is an extra minus sign if the ordering of the fields in their pairs is an odd permutation of the original ordering. For example,
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#be2ae877b9ec47719ba6b1330fecc230">
	$$
	\begin{array} { r } { i ^ { 2 } \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \overline { { \Psi } } _ { \beta } ( y ) \Psi _ { \gamma } ( z ) \overline { { \Psi } } _ { \delta } ( w ) | 0 \rangle = + S ( x - y ) _ { \alpha \beta } S ( z - w ) _ { \gamma \delta } } \\{ - S ( x - w ) _ { \alpha \delta } S ( z - y ) _ { \gamma \beta } . } \end{array} \tag{42.22}
	$$
</synced_block>
In the Majorana case, we may as well let all the fields be $`\Psi`$ s (since we can always replace a $`\overline { { \Psi } }`$ with $`\Psi ^ { \mathrm { T } } { \mathcal { C } }`$ ). Then we must pair them up in all possible ways. There is an extra minus sign if the ordering of the fields in their pairs is an odd permutation of the original ordering. For example,
$$
\begin{array} { r } { ^ { 2 } \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \Psi _ { \beta } ( y ) \Psi _ { \gamma } ( z ) \Psi _ { \delta } ( w ) | 0 \rangle = + [ S ( x - y ) \mathcal { C } ^ { - 1 } ] _ { \alpha \beta } [ S ( z - w ) \mathcal { C } ^ { - 1 } ] _ { \gamma \delta } } \\{ - [ S ( x - z ) \mathcal { C } ^ { - 1 } ] _ { \alpha \gamma } [ S ( y - w ) \mathcal { C } ^ { - 1 } ] _ { \beta \delta } } \\{ + [ S ( x - w ) \mathcal { C } ^ { - 1 } ] _ { \alpha \delta } [ S ( y - z ) \mathcal { C } ^ { - 1 } ] _ { \beta \gamma } } \end{array}
$$
Note that the ordering within a pair does not matter, since
<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#ad73b1ee46e841f1b9b102c7cd16204c">
	$$
	[ S ( x - y ) \mathcal { C } ^ { - 1 } ] _ { \alpha \beta } = - [ S ( y - x ) \mathcal { C } ^ { - 1 } ] _ { \beta \alpha } . \tag{42.23-42.24}
	$$
</synced_block>
This follows from anticommutation of the fields and eq. (42.20).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#6517acc25a8b47ef8bfdaf9306fecd00">
		$$
		\begin{array} { c } { { i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \Psi _ { \beta } ( y ) | 0 \rangle = i \langle 0 | \mathrm { T } \Psi _ { \alpha } ( x ) \overline { { { \Psi } } } _ { \gamma } ( y ) | 0 \rangle ( \mathcal { C } ^ { - 1 } ) _ { \gamma \beta } } } \\{ { { } } } \\{ { { } = [ S ( x - y ) \mathcal { C } ^ { - 1 } ] _ { \alpha \beta } . } } \end{array} \tag{42.20}
		$$
	</synced_block>
</callout>
## Problems
### 42.1
Prove eq. (42.24) directly, using properties of the $`c`$ matrix.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/96e8f1d39d3a40ea92e71c1a03e6f6fc#764fd75274004e02a93c90eb431649e9">
		$$
		[ S ( x - y ) \mathcal { C } ^ { - 1 } ] _ { \alpha \beta } = - [ S ( y - x ) \mathcal { C } ^ { - 1 } ] _ { \beta \alpha } . \tag{42.23-42.24}
		$$
	</synced_block>
</callout>
</content>
</page>
