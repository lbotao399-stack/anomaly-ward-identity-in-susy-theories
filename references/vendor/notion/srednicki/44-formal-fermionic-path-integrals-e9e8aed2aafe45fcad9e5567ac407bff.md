Here is the result of "view" for the Page with URL https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff as of 2026-04-27T10:13:14.980Z:
<page url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"44. Formal development of fermionic path integrals"}
</properties>
<content>
Prerequisite: 43
In section 43, we formally defined the fermionic path integral for a free Dirac field $`\Psi`$ via
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#d13c3b5ab9c64dd98ee3a920aef8550f">
	$$
	\begin{array} { l } { { Z _ { 0 } ( \overline { { { \eta } } } , \eta ) = \displaystyle \int { \mathcal D } \Psi { \mathcal D } \overline { { { \Psi } } } \exp \Biggl [ i \int d ^ { 4 } x \overline { { { \Psi } } } ( i \partial / - m ) \Psi + \overline { { { \eta } } } \Psi + \overline { { { \Psi } } } \eta \Biggl ] } } \\{ { \displaystyle \qquad = \exp \Biggl [ i \int d ^ { 4 } x d ^ { 4 } y \overline { { { \eta } } } ( x ) S ( x - y ) \eta ( y ) \Biggr ] , } } \end{array} \tag{44.1}
	$$
</synced_block>
where the Feynman propagator $`S ( x - y )`$ is the inverse of the Dirac wave operator:
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#2abdab2f8ddd45c9b4d5f201849ed4d2">
	$$
	( - i \partial / _ { x } + m ) S ( x - y ) = \delta ^ { 4 } ( x - y ) . \tag{44.2}
	$$
</synced_block>
We would like to find a mathematical framework that allows us to derive this formula, rather than postulating it by analogy.
Consider a set of anticommuting numbers or Grassmann variables $`\psi _ { i }`$ that obey
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#eb178ae995bf45b78537ebb6290a7536">
	$$
	\{ \psi _ { i } , \psi _ { j } \} = 0 , \tag{44.3}
	$$
</synced_block>
where $`i = 1 , \ldots , n`$ . Let us begin with the very simplest case of $`n = 1`$ , and thus a single anticommuting number $`\psi`$ that obeys $`\psi ^ { 2 } = 0`$ . We can define a function $`f ( \psi )`$ of such an object via a Taylor expansion; because $`\psi ^ { 2 } = 0`$ , this expansion ends with the second term:
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#0f5ee52bb0f84155ba675d47ba509a9a">
	$$
	f ( \psi ) = a + \psi b . \tag{44.4}
	$$
</synced_block>
The reason for writing the coefficient $`b`$ to the right of the variable $`\psi`$ will become clear in a moment.
Next we would like to define the derivative of $`f ( \psi )`$ with respect to $`\psi`$ . Before we can do so, we must decide if $`f ( \psi )`$ itself is to be commuting or anticommuting; generally we will be interested in functions that are themselves commuting. In this case, $`a`$ in eq. (44.4) should be treated as an ordinary commuting number, but $`b`$ should be treated as an anticommuting number: $`\{ b , b \} = \{ b , \psi \} = 0`$ . In this case, $`f ( \psi ) = a + \psi b = a - b \psi`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#dcb058732a354351b41c29be05867fa6">
		$$
		f ( \psi ) = a + \psi b . \tag{44.4}
		$$
	</synced_block>
</callout>
Now we can define two kinds of derivatives. The left derivative of $`f ( \psi )`$ with respect to $`\psi`$ is given by the coefficient of $`\psi`$ when $`f ( \psi )`$ is written with the $`\psi`$ always on the far left:
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#6c0872b274ac4976a211d96cb4271c29">
	$$
	\partial _ { \psi } f ( \psi ) = + b \ . \tag{44.5}
	$$
</synced_block>
Similarly, the right derivative of $`f ( \psi )`$ with respect to $`\psi`$ is given by the coefficient of $`\psi`$ when $`f ( \psi )`$ is written with the $`\psi`$ always on the far right:
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#425a6bdb85714ff5b90ee720992ae98d">
	$$
	f ( \psi ) \overleftarrow { \partial } _ { \psi } = - b . \tag{44.6}
	$$
</synced_block>
Generally, when we write a derivative with respect to a Grassmann variable, we mean the left derivative. However, in section 37, when we wrote the canonical momentum for a fermionic field $`\psi`$ as $`\pi = \partial \mathcal { L } / \partial ( \partial _ { 0 } \psi )`$ , we actually meant the right derivative. (This is a standard, though rarely stated, convention.) Correspondingly, we wrote the hamiltonian density as $`\mathcal { H } = \pi \partial _ { 0 } \psi - \mathcal { L }`$ , with $`\partial _ { 0 } \psi`$ to the right of $`\pi`$ .
Finally, we would like to define a definite integral, analogous to integrating a real variable $`x`$ from minus to plus infinity. The key features of such an integral over $`x`$ (when it converges) are linearity,
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#21008af9ad6e4ebcbd1e55aec4528755">
	$$
	\int _ { - \infty } ^ { + \infty } d x c f ( x ) = c \int _ { - \infty } ^ { + \infty } d x f ( x ) \ , \tag{44.7}
	$$
</synced_block>
and invariance under shifts of the dependent variable $`x`$ by a constant:
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#b46fe14794df4eeea2eaa977caa5fd6a">
	$$
	\int _ { - \infty } ^ { + \infty } d x f ( x + a ) = \int _ { - \infty } ^ { + \infty } d x f ( x ) . \tag{44.8}
	$$
</synced_block>
Up to an overall numerical factor that is the same for every $`f ( \psi )`$ , the only possible nontrivial definition of $`\textstyle { \int d \psi f ( \psi ) }`$ that is both linear and shift invariant is
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#34694c8f350842abb59dfbc6661484d6">
	$$
	\int d \psi f ( \psi ) = b . \tag{44.9}
	$$
</synced_block>
Now let us generalize this to $`n > 1`$ . We have
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#674b694580f84c38b34e77e70e387d60">
	$$
	\begin{array} { r } { f ( \psi ) = a + \psi _ { i } b _ { i } + \frac 1 2 \psi _ { i _ { 1 } } \psi _ { i _ { 2 } } c _ { i _ { 1 } i _ { 2 } } + \ldots + \frac 1 { n ! } \psi _ { i _ { 1 } } \ldots \psi _ { i _ { n } } d _ { i _ { 1 } \ldots i _ { n } } \ , } \end{array} \tag{44.10}
	$$
</synced_block>
where the indices are implicitly summed. Here we have written the coefficients to the right of the variables to facilitate left-differentiation. These coefficients are completely antisymmetric on exchange of any two indices. The left derivative of $`f ( \psi )`$ with respect to $`\psi _ { j }`$ is
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#db4b52c0526748c7a3aea5d6ac5022a7">
	$$
	\begin{array} { r } { \frac { \partial } { \partial \psi _ { j } } f ( \psi ) = b _ { j } + \psi _ { i } c _ { j i } + . . . + \frac { 1 } { ( n - 1 ) ! } \psi _ { i _ { 2 } } \ldots \psi _ { i _ { n } } d _ { j i _ { 2 } \ldots i _ { n } } . } \end{array} \tag{44.11}
	$$
</synced_block>
Next we would like to find a linear, shift-invariant definition of the integral of $`f ( \psi )`$ . Note that the antisymmetry of the coefficients implies that
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#60fd2bb7ce6b472fa28b84096e787c63">
	$$
	d _ { i _ { 1 } \dots i _ { n } } = d \varepsilon _ { i _ { 1 } \dots i _ { n } } , \tag{44.12}
	$$
</synced_block>
where $`d`$ is just a number (ordinary if $`f`$ is commuting and $`n`$ is even, Grassmann if $`f`$ is commuting and $`n`$ is odd, etc.), and $`\varepsilon _ { i _ { 1 } \ldots i _ { n } }`$ is the completely antisymmetric Levi-Civita symbol with $`\varepsilon _ { 1 \ldots n } = + 1`$ . This number $`d`$ is a candidate (in fact, up to an overall numerical factor, the only candidate!) for the integral of $`f ( \psi )`$ :
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#751120d55a3f462495f275408cdcfa82">
	$$
	\int d ^ { n } \psi f ( \psi ) = d . \tag{44.13}
	$$
</synced_block>
Although eq. (44.13) really tells us everything we need to know about $`\int d ^ { n } \psi`$ , we can, if we like, write $`d ^ { n } \psi = d \psi _ { n } \ldots d \psi _ { 1 }`$ (note the backwards ordering), and treat the individual differentials as anticommuting: $`\{ d \psi _ { i } , d \psi _ { j } \} = 0`$ , $`\{ d \psi _ { i } , \psi _ { j } \} = 0`$ . Then we take $`\int d \psi _ { i } = 0`$ and $`\textstyle { \int { d \psi _ { i } \psi _ { j } } = \delta _ { i j } }`$ as our basic formulae, and use them to derive eq. (44.13).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#3ee888552ed64f969542c7c579ed738e">
		$$
		\int d ^ { n } \psi f ( \psi ) = d . \tag{44.13}
		$$
	</synced_block>
</callout>
Let us work out some consequences of eq. (44.13). Consider what happens if we make a linear change of variable,
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#e500c694268b49d7956b7eefc9e9f5b1">
		$$
		\int d ^ { n } \psi f ( \psi ) = d . \tag{44.13}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#c85a133a0153452e9d5aad7ee26ff32a">
	$$
	\psi _ { i } = J _ { i j } \psi _ { j } ^ { \prime } , \tag{44.14}
	$$
</synced_block>
where $`J _ { j i }`$ is a matrix of commuting numbers (and therefore can be written on either the left or right of $`\psi _ { j } ^ { \prime }`$ ). We now have
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#4e4dbd709c36433e9e0f877a13a0dc6c">
	$$
	\begin{array} { r } { f ( \psi ) = a + \ldots + \frac { 1 } { n ! } ( J _ { i _ { 1 } j _ { 1 } } \psi _ { j _ { 1 } } ^ { \prime } ) \ldots ( J _ { i _ { n } j _ { n } } \psi _ { j _ { n } } ^ { \prime } ) \varepsilon _ { i _ { 1 } \ldots i _ { n } } d . } \end{array} \tag{44.15}
	$$
</synced_block>
Next we use
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#3ef003d7087942ddaa8100d4fc251278">
	$$
	\varepsilon _ { i _ { 1 } \ldots i _ { n } } J _ { i _ { 1 } j _ { 1 } } \ldots J _ { i _ { n } j _ { n } } = ( \operatorname * { d e t } J ) \varepsilon _ { j _ { 1 } \ldots j _ { n } } \ , \tag{44.16}
	$$
</synced_block>
which holds for any $`n \times n`$ matrix $`J`$ , to get
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#ff51ea5e982a4ef1a1e06c51d2892449">
	$$
	\begin{array} { r } { f ( \psi ) = a + \ldots + \frac { 1 } { n ! } \psi _ { i _ { 1 } } ^ { \prime } \ldots \psi _ { i _ { n } } ^ { \prime } \varepsilon _ { i _ { 1 } \ldots i _ { n } } ( \operatorname* { d e t } J ) d . } \end{array} \tag{44.17}
	$$
</synced_block>
If we now integrate $`f ( \psi )`$ over $`d ^ { n } \psi ^ { \prime }`$ , eq. (44.13) tells us that the result is $`( \operatorname* { d e t } J ) d`$ . Thus,
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#c6c4b5093fd1429bbc3a1afbc5bccfe0">
		$$
		\int d ^ { n } \psi f ( \psi ) = d . \tag{44.13}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#a147c77023e7422a8044971b436a0332">
	$$
	\int d ^ { n } \psi f ( \psi ) = ( \operatorname * { d e t } J ) ^ { - 1 } \int d ^ { n } \psi ^ { \prime } f ( \psi ) . \tag{44.18}
	$$
</synced_block>
Recall that, for integrals over commuting real numbers $`x _ { i }`$ with $`x _ { i } = J _ { i j } x _ { j } ^ { \prime }`$ , we have instead
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#b04dc24815a747cd8525deaea4a777c5">
	$$
	\int d ^ { n } x f ( x ) = ( \operatorname * { d e t } J ) ^ { + 1 } \int d ^ { n } x ^ { \prime } f ( x ) . \tag{44.19}
	$$
</synced_block>
Note the opposite sign on the power of the determinant.
Now consider a quadratic form $`\psi ^ { \mathrm { T } } M \psi = \psi _ { i } M _ { i j } \psi _ { j }`$ , where $`M`$ is an antisymmetric matrix of commuting numbers (possibly complex). Let us evaluate the gaussian integral $`\begin{array} { r } { \int d ^ { n } \psi \exp \bigl ( \frac 1 2 \psi ^ { \mathrm { T } } M \psi \bigr ) } \end{array}`$ . For example, for $`n = 2`$ , we have
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#b9a26840ebff4828a816f64802ffee10">
	$$
	M = \left( \begin{array} { c c } { { 0 } } & { { + m } } \\{ { } } & { { } } \\{ { - m } } & { { 0 } } \end{array} \right) , \tag{44.20}
	$$
</synced_block>
and $`{ \psi } ^ { \mathrm { T } } M { \psi } = 2 m { \psi } _ { 1 } { \psi } _ { 2 }`$ . Thus $`\mathrm { e x p } ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { { r } } } M \psi ) = 1 + m \psi _ { 1 } \psi _ { 2 }`$ , and so
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#b4230ae987d747a68d4d9e7945d20b47">
	$$
	\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { { T } } } M \psi ) = m . \tag{44.21}
	$$
</synced_block>
For larger $`n`$ , we use the fact that a complex antisymmetric matrix can be brought to a block-diagonal form via
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#9a54fcd0486547468a39a1837ef8d2cd">
	$$
	U ^ { \mathrm { T } } M U = \left( \begin{array} { c c c c } { { 0 } } & { { + m _ { 1 } } } & { { } } & { { } } \\{ { - m _ { 1 } } } & { { 0 } } & { { } } & { { } } \\{ { } } & { { } } & { { } } & { { . } } \end{array} \right) , \tag{44.22}
	$$
</synced_block>
where $`U`$ is a unitary matrix, and each $`m _ { I }`$ is real and positive. (If $`n`$ is odd there is a final row and column of all zeros; from here on, we assume $`n`$ is even.) We can now let $`\psi _ { i } = U _ { i j } \psi _ { j } ^ { \prime }`$ ; then, we have
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#44e4f88d2ee044ef8cd485b77ed460b4">
	$$
	\int d ^ { n } \psi \exp ( \frac { 1 } { 2 } \psi ^ { \mathrm { r } } M \psi ) = ( \operatorname * { d e t } U ) ^ { - 1 } \prod _ { I = 1 } ^ { n / 2 } \int d ^ { 2 } \psi _ { I } \exp ( \frac { 1 } { 2 } \psi ^ { \mathrm { r } } M _ { I } \psi ) ~ , \tag{44.23}
	$$
</synced_block>
where $`M _ { I }`$ represents one of the $`2 \times 2`$ blocks in eq. (44.22). Each of these two-dimensional integrals can be evaluated using eq. (44.21), and so
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#b65c499c54eb44d38634ced9d32158a8">
		$$
		U ^ { \mathrm { T } } M U = \left( \begin{array} { c c c c } { { 0 } } & { { + m _ { 1 } } } & { { } } & { { } } \\{ { - m _ { 1 } } } & { { 0 } } & { { } } & { { } } \\{ { } } & { { } } & { { } } & { { . } } \end{array} \right) , \tag{44.22}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#056b8d99056f4c44b47dc312a5ffa4bc">
		$$
		\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { { T } } } M \psi ) = m . \tag{44.21}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#663b7c5a485d4b26bee071b9a2bd1ec8">
	$$
	\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi ) = ( \operatorname * { d e t } U ) ^ { - 1 } \prod _ { I = 1 } ^ { n / 2 } m _ { I } . \tag{44.24}
	$$
</synced_block>
Taking the determinant of eq. (44.22), we get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#81c2440dce6e441c95460be889868220">
		$$
		U ^ { \mathrm { T } } M U = \left( \begin{array} { c c c c } { { 0 } } & { { + m _ { 1 } } } & { { } } & { { } } \\{ { - m _ { 1 } } } & { { 0 } } & { { } } & { { } } \\{ { } } & { { } } & { { } } & { { . } } \end{array} \right) , \tag{44.22}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#c5d67bec25f64e668398903a1e2049f2">
	$$
	( \operatorname * { d e t } U ) ^ { 2 } ( \operatorname * { d e t } M ) = \prod _ { I = 1 } ^ { n / 2 } m _ { I } ^ { 2 } . \tag{44.25}
	$$
</synced_block>
We can therefore rewrite the right-hand side of eq. (44.24) as
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#22d1fedc494245bc9682c7b82ef30a66">
		$$
		\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi ) = ( \operatorname * { d e t } U ) ^ { - 1 } \prod _ { I = 1 } ^ { n / 2 } m _ { I } . \tag{44.24}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#c064c3b3b4494f7eaef6f40f74f04299">
	$$
	\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi ) = ( \operatorname * { d e t } M ) ^ { 1 / 2 } . \tag{44.26}
	$$
</synced_block>
In this form, there is a sign ambiguity associated with the square root; it is resolved by eq. (44.24). However, the overall sign (more generally, any overall numerical factor) will never be of concern to us, so we can use eq. (44.26) without worrying about the correct branch of the square root.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#0b0200db3c0c4a6aac346da6880ef268">
		$$
		\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi ) = ( \operatorname * { d e t } U ) ^ { - 1 } \prod _ { I = 1 } ^ { n / 2 } m _ { I } . \tag{44.24}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#fde18b0790cc4f668fbd643a9eb047ba">
		$$
		\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi ) = ( \operatorname * { d e t } M ) ^ { 1 / 2 } . \tag{44.26}
		$$
	</synced_block>
</callout>
It is instructive to compare eq. (44.26) with the corresponding gaussian integral for commuting real numbers,
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#5582d0a4ecb74bc9b4e9223e28207398">
		$$
		\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi ) = ( \operatorname * { d e t } M ) ^ { 1 / 2 } . \tag{44.26}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#5e04733cf2374fb1b9cc2d54ee129868">
	$$
	\int d ^ { n } x \exp ( - \textstyle { \frac { 1 } { 2 } } x ^ { \mathrm { { r } } } M x ) = ( 2 \pi ) ^ { n / 2 } ( \operatorname * { d e t } M ) ^ { - 1 / 2 } . \tag{44.26-44.27}
	$$
</synced_block>
Here $`M`$ is a complex symmetric matrix. Again, note the opposite sign on the power of the determinant.
Now let us introduce the notion of complex Grassmann variables via
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#c3780885002b4fb2b1ec5b524960cdde">
	$$
	\begin{array} { l } { { \chi \equiv \frac { 1 } { \sqrt { 2 } } ( \psi _ { 1 } + i \psi _ { 2 } ) \ , } } \\{ { { } } } \\{ { \bar { \chi } \equiv \frac { 1 } { \sqrt { 2 } } ( \psi _ { 1 } - i \psi _ { 2 } ) \ . } } \end{array} \tag{44.28}
	$$
</synced_block>
We can invert this to get
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#3b3491b68e4d41e6ab6d3667e0e0452b">
	$$
	\begin{array} { r } { \left( \begin{array} { c } { \psi _ { 1 } } \\{ \psi _ { 2 } } \end{array} \right) = \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c c } { 1 } & { 1 } \\{ i } & { - i } \end{array} \right) \left( \begin{array} { c } { \bar { \chi } } \\{ \chi } \end{array} \right) . } \end{array} \tag{44.29}
	$$
</synced_block>
The determinant of this transformation matrix is $`- i`$ , and so
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#fb857ee9e21f454d927c1083e358a213">
	$$
	d ^ { 2 } \psi = d \psi _ { 2 } d \psi _ { 1 } = ( - i ) ^ { - 1 } d \chi d \bar { \chi } . \tag{44.30}
	$$
</synced_block>
Also, $`\psi _ { 1 } \psi _ { 2 } = - i \bar { \chi } \chi`$ . Thus we have
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#25e5660af94e447c8c0daf2bb67f528f">
	$$
	\int d \chi d \bar { \chi } \bar { \chi } \chi = ( - i ) ( - i ) ^ { - 1 } \int d \psi _ { 2 } d \psi _ { 1 } \psi _ { 1 } \psi _ { 2 } = 1 . \tag{44.31}
	$$
</synced_block>
Thus, if we have a function
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#9f829663881a4f6298029ccae683b97c">
	$$
	f ( \chi , \bar { \chi } ) = a + \chi b + \bar { \chi } c + \bar { \chi } \chi d , \tag{44.32}
	$$
</synced_block>
its integral is
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#565e41b83eb94e2698e9bfa7e0f115b9">
	$$
	\int d \chi d \bar { \chi } f ( \chi , \bar { \chi } ) = d . \tag{44.33}
	$$
</synced_block>
In particular,
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#b100053761a541fa9ce4bd16f48108c2">
	$$
	\int d \chi d \bar { \chi } \exp ( m \bar { \chi } \chi ) = m . \tag{44.34}
	$$
</synced_block>
Let us now consider $`n`$ complex Grassmann variables $`\chi _ { i }`$ and their complex conjugates, $`\chi _ { i }`$ . We define
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#5cbf239cfa6a4007bc9021ed0a82a3b4">
	$$
	d ^ { n } \chi d ^ { n } \bar { \chi } \equiv d \chi _ { n } d \bar { \chi } _ { n } \ldots d \chi _ { 1 } d \bar { \chi } _ { 1 } \ . \tag{44.35}
	$$
</synced_block>
Then under a change of variable, $`\chi _ { i } = J _ { i j } \chi _ { j } ^ { \prime }`$ and $`\bar { \chi } _ { i } = K _ { i j } \bar { \chi } _ { j } ^ { \prime }`$ , we have
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#98417c9142694d8eb14aaa9ba1c627a2">
	$$
	d ^ { n } \chi d ^ { n } \bar { \chi } = ( \operatorname * { d e t } J ) ^ { - 1 } ( \operatorname * { d e t } K ) ^ { - 1 } d ^ { n } \chi ^ { \prime } d ^ { n } \bar { \chi } ^ { \prime } . \tag{44.36}
	$$
</synced_block>
Note that we need not require $`K _ { i j } = J _ { i j } ^ { * }`$ , because, as far as the integral is concerned, it is does not matter whether or not $`\chi _ { i }`$ is the complex conjugate of $`\chi _ { i }`$ .
We now have enough information to evaluate $`\textstyle \int d ^ { n } \chi d ^ { n } \bar { \chi } \exp ( \chi ^ { \dagger } M \chi )`$ , where $`M`$ is a general complex matrix. We make the change of variable $`\chi = U \chi ^ { \prime }`$ and $`\chi ^ { \dagger } = \chi ^ { \prime \dagger } V`$ , where $`U`$ and $`V`$ are unitary matrices with the property that $`V M U`$ is diagonal with positive real entries $`m _ { i }`$ . Then we get
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#2ca5b9be25954e8ba32a1e6e2ec6244b">
	$$
	\begin{array} { l } { { { \displaystyle \int d ^ { n } \chi d ^ { n } \bar { \chi } \exp ( \chi ^ { \dagger } M \chi ) = ( \operatorname * { d e t } U ) ^ { - 1 } ( \operatorname * { d e t } V ) ^ { - 1 } \prod _ { i = 1 } ^ { n } \int d \chi _ { i } d \bar { \chi } _ { i } \exp ( m _ { i } \bar { \chi } _ { i } \chi _ { i } ) } ~ } } \\{ { ~ } } \\{ { { } = ( \operatorname * { d e t } U ) ^ { - 1 } ( \operatorname * { d e t } V ) ^ { - 1 } \prod _ { i = 1 } ^ { n } m _ { i } } } \\{ { ~ } } \\{ { { } = \operatorname * { d e t } M ~ . } } \end{array} \tag{44.37}
	$$
</synced_block>
This can be compared to the analogous integral for commuting complex variables $`z _ { i } = ( x _ { i } + i y _ { i } ) / \sqrt { 2 }`$ and $`\bar { z } = ( x _ { i } - i y _ { i } ) / \sqrt { 2 }`$ , with $`d ^ { n } z d ^ { n } \bar { z } = d ^ { n } x d ^ { n } y`$ , namely
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#972ffa3561f04cc3a2973982b71a81e5">
	$$
	\int d ^ { n } z d ^ { n } \bar { z } \exp ( - z ^ { \dagger } M z ) = ( 2 \pi ) ^ { n } ( \operatorname * { d e t } M ) ^ { - 1 } . \tag{44.38}
	$$
</synced_block>
We can now generalize eqs. (44.26) and (44.37) by shifting the integration variables, and using shift invariance of the integrals. Thus, by making the replacement $`\psi \psi - M ^ { - 1 } \eta`$ in eq. (44.26), we get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#7f4715857d494166adb29af9c587f36a">
		$$
		\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi ) = ( \operatorname * { d e t } M ) ^ { 1 / 2 } . \tag{44.26}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#c623a6c48e6e4d23a8490b6f36e90c64">
		$$
		\begin{array} { l } { { { \displaystyle \int d ^ { n } \chi d ^ { n } \bar { \chi } \exp ( \chi ^ { \dagger } M \chi ) = ( \operatorname * { d e t } U ) ^ { - 1 } ( \operatorname * { d e t } V ) ^ { - 1 } \prod _ { i = 1 } ^ { n } \int d \chi _ { i } d \bar { \chi } _ { i } \exp ( m _ { i } \bar { \chi } _ { i } \chi _ { i } ) } ~ } } \\{ { ~ } } \\{ { { } = ( \operatorname * { d e t } U ) ^ { - 1 } ( \operatorname * { d e t } V ) ^ { - 1 } \prod _ { i = 1 } ^ { n } m _ { i } } } \\{ { ~ } } \\{ { { } = \operatorname * { d e t } M ~ . } } \end{array} \tag{44.37}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#21c5662416904dbabde2c8e241cfc8d4">
	$$
	\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi + \eta ^ { \mathrm { \scriptscriptstyle T } } \psi ) = ( \operatorname * { d e t } M ) ^ { 1 / 2 } \exp ( \textstyle { \frac { 1 } { 2 } } \eta ^ { \mathrm { \scriptscriptstyle T } } M ^ { - 1 } \eta ) . \tag{44.39}
	$$
</synced_block>
(In verifying this, remember that $`M`$ and its inverse are both antisymmetric.) Similarly, by making the replacements $`\chi \to \chi - M ^ { - 1 } \eta`$ and $`\chi ^ { \dagger }`$ $`\chi ^ { \dagger } - \eta ^ { \dagger } M ^ { - 1 }`$ in eq. (44.37), we get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#3f8c5824cbba4b8d858a180eee03789b">
		$$
		\begin{array} { l } { { { \displaystyle \int d ^ { n } \chi d ^ { n } \bar { \chi } \exp ( \chi ^ { \dagger } M \chi ) = ( \operatorname * { d e t } U ) ^ { - 1 } ( \operatorname * { d e t } V ) ^ { - 1 } \prod _ { i = 1 } ^ { n } \int d \chi _ { i } d \bar { \chi } _ { i } \exp ( m _ { i } \bar { \chi } _ { i } \chi _ { i } ) } ~ } } \\{ { ~ } } \\{ { { } = ( \operatorname * { d e t } U ) ^ { - 1 } ( \operatorname * { d e t } V ) ^ { - 1 } \prod _ { i = 1 } ^ { n } m _ { i } } } \\{ { ~ } } \\{ { { } = \operatorname * { d e t } M ~ . } } \end{array} \tag{44.37}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#067833223ef5490bbbd54b5a1d4e71f5">
	$$
	\int d ^ { n } \chi d ^ { n } \bar { \chi } \exp ( \chi ^ { \dagger } M \chi + \eta ^ { \dagger } \chi + \chi ^ { \dagger } \eta ) = ( \operatorname * { d e t } M ) \exp ( - \eta ^ { \dagger } M ^ { - 1 } \eta ) . \tag{44.40}
	$$
</synced_block>
We can now see that eq. (44.1) is simply a particular case of eq. (44.40), with the index on the complex Grassmann variable generalized to include both the ordinary spin index $`\alpha`$ and the continuous space-time argument $`x`$ of the field $`\Psi _ { \alpha } ( x )`$ . Similarly, eq. (43.21) for the path integral for a free Majorana field is simply a particular case of eq. (44.39). In both cases, the determinant factors are constants (that is, independent of the fields and sources) that we simply absorb into the overall normalization of the path integral. We will meet determinants that cannot be so neatly absorbed in sections 53 and 71.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#6b67465af7aa4407a3e605f1fef7127f">
		$$
		\begin{array} { l } { { Z _ { 0 } ( \overline { { { \eta } } } , \eta ) = \displaystyle \int { \mathcal D } \Psi { \mathcal D } \overline { { { \Psi } } } \exp \Biggl [ i \int d ^ { 4 } x \overline { { { \Psi } } } ( i \partial / - m ) \Psi + \overline { { { \eta } } } \Psi + \overline { { { \Psi } } } \eta \Biggl ] } } \\{ { \displaystyle \qquad = \exp \Biggl [ i \int d ^ { 4 } x d ^ { 4 } y \overline { { { \eta } } } ( x ) S ( x - y ) \eta ( y ) \Biggr ] , } } \end{array} \tag{44.1}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#b6de70ba6b104614b97fb496a7e1e6f0">
		$$
		\int d ^ { n } \chi d ^ { n } \bar { \chi } \exp ( \chi ^ { \dagger } M \chi + \eta ^ { \dagger } \chi + \chi ^ { \dagger } \eta ) = ( \operatorname * { d e t } M ) \exp ( - \eta ^ { \dagger } M ^ { - 1 } \eta ) . \tag{44.40}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#89bfd4dc3e0946469951b8b83122f1e2">
		<unknown url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#8043b6f8ec804a27b6dab31e411851fc"/>
	</synced_block>
	<synced_block url="https://app.notion.com/p/e9e8aed2aafe45fcad9e5567ac407bff#9b0c0f789ec8490584e47eb90f8b1608">
		$$
		\int d ^ { n } \psi \exp ( \textstyle { \frac { 1 } { 2 } } \psi ^ { \mathrm { \scriptscriptstyle T } } M \psi + \eta ^ { \mathrm { \scriptscriptstyle T } } \psi ) = ( \operatorname * { d e t } M ) ^ { 1 / 2 } \exp ( \textstyle { \frac { 1 } { 2 } } \eta ^ { \mathrm { \scriptscriptstyle T } } M ^ { - 1 } \eta ) . \tag{44.39}
		$$
	</synced_block>
</callout>
</content>
</page>
