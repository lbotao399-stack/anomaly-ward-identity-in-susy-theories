Here is the result of "view" for the Page with URL https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a as of 2026-04-27T17:19:31.832Z:
<page url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a">
<ancestor-path>
<parent-page url="https://app.notion.com/p/a7bfa00c3bf745b393bdba34b5dbfa3f" title="Part III Spin One"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"95. Supersymmetry"}
</properties>
<content>
Supersymmetry is a continuous symmetry that mixes up bosonic and fermionic degrees of freedom. A supersymmetric theory (in four space-time dimensions) has a set of supercharges $`Q _ { a A }`$ , where $`a`$ is a left-handed spinor index, and $`A`$ is an internal index that runs from 1 to $`\mathcal { N }`$ , where the allowed values of $`\mathcal { N }`$ are 1, 2, and 4. The supercharges can be obtained as integrals over $`d ^ { 3 } x`$ of the time component of a supercurrent. The supercurrent is found via the Noether procedure, once we have identified the set of supersymmetry transformations that leaves the action invariant.
The supercharges $`Q _ { a A }`$ and their hermitian conjugates $`Q _ { \dot { a } A } ^ { \dagger }`$ , together with the generators of the Poincar´e group $`P ^ { \mu }`$ and $`M ^ { \mu \nu }`$ , obey a supersymmetry algebra
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#a1f9b6200ee84d33a6b537311e157021">
	$$
	\begin{array} { r l } & { [ Q _ { a A } , P ^ { \mu } ] = 0 , } \\& { [ Q _ { a A } ^ { \dagger } , P ^ { \mu } ] = 0 , } \\& { [ Q _ { a A } , M ^ { \mu \nu } ] = ( { S } _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } ^ { c } Q _ { c A } , } \\& { [ Q _ { a A } ^ { \dagger } , M ^ { \mu \nu } ] = ( { S } _ { \mathrm { R } } ^ { \mu \nu } ) _ { a } ^ { \dot { c } } Q _ { \dot { c } A } ^ { \dagger } , } \\& { \{ Q _ { a A } , Q _ { b B } \} = Z _ { A B } \varepsilon _ { a b } , } \\& { \{ Q _ { a A } , Q _ { i B } ^ { \dagger } \} = - 2 \delta _ { A B } \sigma _ { a i } ^ { \mu } P _ { \mu } . } \end{array} \tag{95.1-95.5}
	$$
</synced_block>
Eqs. (95.1) and (95.2) simply say that the supercharges are conserved, and eqs. (95.3) and (95.4) simply say that their spinor indices are indeed spinor indices. In eq. (95.5), $`Z _ { A B } = - Z _ { B A }`$ must commute with $`Q _ { a A }`$ , $`P ^ { \mu }`$ , and $`M ^ { \mu \nu }`$ , and so represents a central charge in the supersymmetry algebra. We will be concerned only with the case of $`{ \mathcal N } = 1`$ supersymmetry: the index $`A`$ then takes on only one value (and so can be dropped), and $`Z _ { A B } = 0`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#adfbce3ee207484db30a7769fbbdbbac">
		$$
		\begin{array} { r l } & { [ Q _ { a A } , P ^ { \mu } ] = 0 , } \\& { [ Q _ { a A } ^ { \dagger } , P ^ { \mu } ] = 0 , } \\& { [ Q _ { a A } , M ^ { \mu \nu } ] = ( { S } _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } ^ { c } Q _ { c A } , } \\& { [ Q _ { a A } ^ { \dagger } , M ^ { \mu \nu } ] = ( { S } _ { \mathrm { R } } ^ { \mu \nu } ) _ { a } ^ { \dot { c } } Q _ { \dot { c } A } ^ { \dagger } , } \\& { \{ Q _ { a A } , Q _ { b B } \} = Z _ { A B } \varepsilon _ { a b } , } \\& { \{ Q _ { a A } , Q _ { i B } ^ { \dagger } \} = - 2 \delta _ { A B } \sigma _ { a i } ^ { \mu } P _ { \mu } . } \end{array} \tag{95.1-95.5}
		$$
	</synced_block>
</callout>
$`\mathcal { N } = 1`$ supersymmetric theories are most easily formulated in superspace, where we augment the usual space-time coordinate $`x ^ { \mu }`$ with an anticommuting left-handed spinor coordinate $`\theta _ { a }`$ and its right-handed complex conjugate $`\theta _ { \dot { a } } ^ { * }`$ . We define superfields $`\Phi ( x , \theta , \theta ^ { * } )`$ that are functions of all these coordinates.
The energy-momentum vector generates translations of the usual spacetime coordinate $`x ^ { \mu }`$ in the usual way,
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f76cd2dd8cb549c598a56fe27efec9cb">
	$$
	\left[ \Phi ( x , \theta , \theta ^ { * } ) , P ^ { \mu } \right] = - i \partial ^ { \mu } \Phi ( x , \theta , \theta ^ { * } ) . \tag{95.7}
	$$
</synced_block>
By analogy, we would expect
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#dc1aff6f8c0c4cc3ac1a4ba027f8d841">
	$$
	\begin{array} { l } { { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { a } \right] = - i \mathcal { Q } _ { a } \Phi ( x , \theta , \theta ^ { * } ) , } } \\{ { \ } } \\{ { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { \dot { a } } ^ { \dagger } \right] = - i \mathcal { Q } _ { \dot { a } } ^ { * } \Phi ( x , \theta , \theta ^ { * } ) , } } \end{array} \tag{95.8-95.9}
	$$
</synced_block>
where $`\mathcal { Q } _ { a }`$ and $`\mathcal { Q } _ { \dot { a } } ^ { \ast }`$ are appropriate differential operators. To figure out what they should be, we first introduce the anticommuting derivatives $`\partial _ { a } \equiv \partial / \partial \theta ^ { a }`$ and $`\partial _ { \dot { a } } ^ { * } \equiv \partial / \partial \theta ^ { * \dot { a } }`$ , which obey $`\partial _ { a } \theta ^ { c } = \delta _ { a } { } ^ { c }`$ and $`\partial _ { \dot { a } } ^ { * } \theta ^ { * \dot { c } } = \delta _ { \dot { a } } { } ^ { \dot { c } }`$ . Note, however, that complex conjugation should reverse the order of a product of Grassmann variables, in order to maintain consistency with hermitian conjugation. Then we have $`\delta _ { a } { } ^ { c } = ( \partial _ { a } \theta ^ { c } ) ^ { * } = \theta ^ { * } { } ^ { \dot { c } } ( \partial _ { a } ) ^ { * } = - ( \partial _ { a } ) ^ { * } \theta ^ { * } { } ^ { \dot { c } }`$ , which implies
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#48c03e579a4543b6a7295c5ea6e402c1">
	$$
	\left( \partial _ { a } \right) ^ { * } = - \partial _ { \dot { a } } ^ { * } . \tag{95.10, 95.8}
	$$
</synced_block>
Thus, our first guess for the differential operators in eqs. (95.8) and (95.9) is $`\mathcal { Q } _ { a } = \partial _ { a }`$ and $`\mathcal { Q } _ { \dot { a } } ^ { * } = - \partial _ { \dot { a } } ^ { * }`$ . However, this choice is inconsistent with $`\{ Q _ { a } , Q _ { \dot { a } } ^ { \dagger } \} = - 2 \sigma _ { a \dot { a } } ^ { \mu } P _ { \mu }`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#b960538ec7a84f88a1f2f2189f7a4f67">
		$$
		\begin{array} { l } { { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { a } \right] = - i \mathcal { Q } _ { a } \Phi ( x , \theta , \theta ^ { * } ) , } } \\{ { \ } } \\{ { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { \dot { a } } ^ { \dagger } \right] = - i \mathcal { Q } _ { \dot { a } } ^ { * } \Phi ( x , \theta , \theta ^ { * } ) , } } \end{array} \tag{95.8-95.9}
		$$
	</synced_block>
</callout>
An alternative that avoids this pitfall is
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#736232711d68493dab01bbac2b4d20a6">
	$$
	\begin{array} { r } { \mathcal { Q } _ { a } = + \partial _ { a } + i \sigma _ { a \dot { c } } ^ { \mu } \theta ^ { * \dot { c } } \partial _ { \mu } , } \\{ \mathcal { Q } _ { \dot { a } } ^ { * } = - \partial _ { \dot { a } } ^ { * } - i \theta ^ { c } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } . } \end{array} \tag{95.11-95.12}
	$$
</synced_block>
These obey the anticommutation relations
$$
\left\{ \mathcal { Q } _ { a } , \mathcal { Q } _ { b } \right\} = \left\{ \mathcal { Q } _ { \dot { a } } ^ { * } , \mathcal { Q } _ { \dot { b } } ^ { * } \right\} = 0 ,
$$
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#7919e968869b4171b80165b1376b9b14">
	$$
	\{ { \mathcal { Q } } _ { a } , { \mathcal { Q } } _ { \dot { a } } ^ { * } \} = - 2 i \sigma _ { a \dot { a } } ^ { \mu } \partial _ { \mu } . \tag{95.13-95.14}
	$$
</synced_block>
It is straightforward to check that eqs. (95.5)–(95.12) are now mutually compatible. In particular, the Jacobi identity
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#0a7d8f0f166242a2ae807306ddfa63ad">
		$$
		\begin{array} { r l } & { [ Q _ { a A } , P ^ { \mu } ] = 0 , } \\& { [ Q _ { a A } ^ { \dagger } , P ^ { \mu } ] = 0 , } \\& { [ Q _ { a A } , M ^ { \mu \nu } ] = ( { S } _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } ^ { c } Q _ { c A } , } \\& { [ Q _ { a A } ^ { \dagger } , M ^ { \mu \nu } ] = ( { S } _ { \mathrm { R } } ^ { \mu \nu } ) _ { a } ^ { \dot { c } } Q _ { \dot { c } A } ^ { \dagger } , } \\& { \{ Q _ { a A } , Q _ { b B } \} = Z _ { A B } \varepsilon _ { a b } , } \\& { \{ Q _ { a A } , Q _ { i B } ^ { \dagger } \} = - 2 \delta _ { A B } \sigma _ { a i } ^ { \mu } P _ { \mu } . } \end{array} \tag{95.1-95.5}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#5f247a79384d417cb1ec77f47b157a19">
		$$
		\begin{array} { r } { \mathcal { Q } _ { a } = + \partial _ { a } + i \sigma _ { a \dot { c } } ^ { \mu } \theta ^ { * \dot { c } } \partial _ { \mu } , } \\{ \mathcal { Q } _ { \dot { a } } ^ { * } = - \partial _ { \dot { a } } ^ { * } - i \theta ^ { c } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } . } \end{array} \tag{95.11-95.12}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#c2071b5f8bfd497c862c27991c93a478">
	$$
	\{ [ \Phi , Q ] , Q ^ { \dagger } \} + \{ [ \Phi , Q ^ { \dagger } ] , Q \} - [ \Phi , \{ Q , Q ^ { \dagger } \} ] = 0 \tag{95.15}
	$$
</synced_block>
is satisfied.
Next we introduce the supercovariant derivatives
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#76e3176fa657446c8444bd35744325ad">
	$$
	\begin{array} { r } { \mathcal { D } _ { a } = + \partial _ { a } - i \sigma _ { a \dot { c } } ^ { \mu } \theta ^ { * \dot { c } } \partial _ { \mu } , } \\{ } \\{ \mathcal { D } _ { \dot { a } } ^ { * } = - \partial _ { \dot { a } } ^ { * } + i \theta ^ { c } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } . } \end{array} \tag{95.16-95.17}
	$$
</synced_block>
These obey
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#76e06fc7d1eb4066bc43c1259117799a">
	$$
	\left\{ \mathcal { D } _ { a } , \mathcal { D } _ { b } \right\} = \left\{ \mathcal { D } _ { \dot { a } } ^ { * } , \mathcal { D } _ { \dot { b } } ^ { * } \right\} = 0 , \tag{95.18}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#8f9200be7141437c964e2c0b54d7f88c">
	$$
	\{ { \mathcal D } _ { a } , { \mathcal D } _ { \dot { a } } ^ { * } \} = 2 i \sigma _ { a \dot { a } } ^ { \mu } \partial _ { \mu } , \tag{95.19}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#364e828eb3074e9ca7777da6f646b314">
	$$
	\{ { \mathcal D } _ { a } , { \mathcal Q } _ { b } \} = \{ { \mathcal D } _ { a } , { \mathcal Q } _ { b } ^ { * } \} = \{ { \mathcal D } _ { \dot { a } } ^ { * } , { \mathcal Q } _ { b } \} = \{ { \mathcal D } _ { \dot { a } } ^ { * } , { \mathcal Q } _ { \dot { b } } ^ { * } \} = 0 . \tag{95.20}
	$$
</synced_block>
Because of eq. (95.20), we could impose the condition $`\mathcal { D } _ { a } \Phi = 0`$ or $`\mathcal { D } _ { \dot { a } } ^ { * } \Phi = 0`$ on a superfield, and this condition would be preserved by the supersymmetry transformations of eqs. (95.8) and (95.9). A superfield that obeys
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#b0c70851133340fbb105a05d3757448a">
		$$
		\{ { \mathcal D } _ { a } , { \mathcal Q } _ { b } \} = \{ { \mathcal D } _ { a } , { \mathcal Q } _ { b } ^ { * } \} = \{ { \mathcal D } _ { \dot { a } } ^ { * } , { \mathcal Q } _ { b } \} = \{ { \mathcal D } _ { \dot { a } } ^ { * } , { \mathcal Q } _ { \dot { b } } ^ { * } \} = 0 . \tag{95.20}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#2cfdae89067a403e832c76510e08eadc">
		$$
		\begin{array} { l } { { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { a } \right] = - i \mathcal { Q } _ { a } \Phi ( x , \theta , \theta ^ { * } ) , } } \\{ { \ } } \\{ { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { \dot { a } } ^ { \dagger } \right] = - i \mathcal { Q } _ { \dot { a } } ^ { * } \Phi ( x , \theta , \theta ^ { * } ) , } } \end{array} \tag{95.8-95.9}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#3c7e0487c6904737a731d04c74d7836d">
	$$
	\mathcal { D } _ { \dot { a } } ^ { * } \Phi ( x , \theta , \theta ^ { * } ) = 0 \tag{95.21}
	$$
</synced_block>
is a left-handed chiral superfield. Its hermitian conjugate $`\Phi ^ { \dag } ( x , \theta , \theta ^ { \ast } )`$ obeys
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#6cc981f79f034b4aa8b726dbb188f8c6">
	$$
	{ \mathcal D } _ { a } \Phi ^ { \dagger } ( x , \theta , \theta ^ { * } ) = 0 , \tag{95.22}
	$$
</synced_block>
and is a right-handed chiral superfield.
We can solve eq. (95.21) by introducing
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f439757d02de4b688a308800c8ccaa1c">
		$$
		\mathcal { D } _ { \dot { a } } ^ { * } \Phi ( x , \theta , \theta ^ { * } ) = 0 \tag{95.21}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#a7d2f60954474b5e9d23f18285fdad26">
	$$
	y ^ { \mu } = x ^ { \mu } - i \theta ^ { c } \sigma _ { c \dot { c } } ^ { \mu } \theta ^ { * \dot { c } } , \tag{95.23}
	$$
</synced_block>
and noting that
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#45323156853449f5bc4ca562c866f4ba">
	$$
	{ \mathcal D } _ { \dot { a } } ^ { * } \theta _ { a } = 0 \quad \mathrm { a n d } \quad { \mathcal D } _ { \dot { a } } ^ { * } y ^ { \mu } = 0 . \tag{95.24}
	$$
</synced_block>
(When verifying $`\mathcal { D } _ { \dot { a } } ^ { * } y ^ { \mu } = 0`$ , remember that there is a minus sign from pulling the $`\partial _ { \dot { a } } ^ { \ast }`$ through $`\theta ^ { c }`$ .) Thus, any superfield $`\Phi ( \boldsymbol { y } , \theta )`$ that is a function of $`y`$ and $`\theta`$ only is a left-handed chiral superfield.
We can expand $`\Phi ( \boldsymbol { y } , \theta )`$ in powers of $`\theta`$ ; because $`\theta`$ is an anticommuting variable with a two-valued index, we have $`\theta _ { a } \theta _ { b } \theta _ { c } = 0`$ , and so the expansion terminates after the quadratic term. We thus have
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#e31e502f41e84d33b6227013b1df2bb6">
	$$
	\Phi ( y , \theta ) = A ( y ) + \sqrt { 2 } \theta \psi ( y ) + \theta \theta F ( y ) , \tag{95.25}
	$$
</synced_block>
where $`A ( y )`$ and $`F ( y )`$ are complex scalar fields, $`\psi _ { a } ( y )`$ is a left-handed Weyl field, and we have used our standard index-suppression conventions: $`\theta \psi =`$ $`\theta ^ { a } \psi _ { a }`$ and $`\theta \theta = \theta ^ { a } \theta _ { a }`$ . The factor of root-two is conventional.
We can now substitute in eq. (95.23), and continue to expand in powers of $`\theta`$ and $`\theta ^ { * }`$ . Making use of the spinor identities
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#88cfca82b9e245c5af00330a5cc4683c">
		$$
		y ^ { \mu } = x ^ { \mu } - i \theta ^ { c } \sigma _ { c \dot { c } } ^ { \mu } \theta ^ { * \dot { c } } , \tag{95.23}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#cf9b7e26713c4a58b79ecdab083199bc">
	$$
	\begin{array} { l l } { { \theta _ { a } \theta _ { b } = + { \frac { 1 } { 2 } } \theta \theta \varepsilon _ { a b } ~ , ~ } } & { { ~ \theta ^ { a } \theta ^ { b } = - { \frac { 1 } { 2 } } \theta \theta \varepsilon ^ { a b } ~ , } } \\{ { { } } } & { { { } } } \\{ { \theta _ { \dot { a } } ^ { * } \theta _ { \dot { b } } ^ { * } = - { \frac { 1 } { 2 } } \theta ^ { * } \theta ^ { * } \varepsilon _ { \dot { a } \dot { b } } ~ , ~ } } & { { ~ \theta ^ { * \dot { a } } \theta ^ { * \dot { b } } = + { \frac { 1 } { 2 } } \theta ^ { * } \theta ^ { * } \varepsilon ^ { \dot { a } \dot { b } } ~ , } } \end{array} \tag{95.26-95.27}
	$$
</synced_block>
where $`\theta \theta = \theta ^ { a } \theta _ { a }`$ and $`\theta ^ { * } \theta ^ { * } = ( \theta \theta ) ^ { * } = \theta _ { \dot { a } } ^ { * } \theta ^ { * \dot { a } }`$ , along with the Fierz identity
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#4ffb20e70e0447cc99a147fdbe351cac">
	$$
	\begin{array} { r } { ( \theta \sigma ^ { \mu } \theta ^ { * } ) ( \theta \sigma ^ { \nu } \theta ^ { * } ) = - \frac { 1 } { 2 } \theta \theta \theta ^ { * } \theta ^ { * } g ^ { \mu \nu } , } \end{array} \tag{95.28}
	$$
</synced_block>
we find
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#5faeda48caa74e809743d273496986a0">
	$$
	\begin{array} { l } { { \Phi ( x , \theta , \theta ^ { * } ) = A ( x ) + \sqrt { 2 } \theta \psi ( x ) + \theta \theta F ( x ) - i ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } A ( x ) } } \\{ { - \frac { 1 } { \sqrt { 2 } } i \theta \theta \theta ^ { * } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi ( x ) + \frac { 1 } { 4 } \theta \theta \theta ^ { * } \theta ^ { * } \partial ^ { 2 } A ( x ) . } } \end{array} \tag{95.29}
	$$
</synced_block>
Let us investigate the properties of a left-handed chiral superfield under a supersymmetry transformation, given by eqs. (95.8) and (95.9). It is easiest to use the $`y`$ and $`\theta`$ coordinates, since
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#c31da0981c9b4eca8aca33dd0cb78082">
		$$
		\begin{array} { l } { { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { a } \right] = - i \mathcal { Q } _ { a } \Phi ( x , \theta , \theta ^ { * } ) , } } \\{ { \ } } \\{ { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { \dot { a } } ^ { \dagger } \right] = - i \mathcal { Q } _ { \dot { a } } ^ { * } \Phi ( x , \theta , \theta ^ { * } ) , } } \end{array} \tag{95.8-95.9}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#b1be6a1e0ac9423f8fbb5dc25675bfa1">
	$$
	\begin{array} { l l } { { { \mathcal { Q } } _ { a } \theta ^ { b } = \delta _ { a } { } ^ { b } , \quad } } & { { { \mathcal { Q } } _ { a } y ^ { \mu } = 0 , } } \\{ { { } } } & { { { } } } \\{ { { \mathcal { Q } } _ { \dot { a } } ^ { * } \theta ^ { b } = 0 , \quad } } & { { { \mathcal { Q } } _ { \dot { a } } ^ { * } y ^ { \mu } = - 2 i \theta ^ { c } \sigma _ { c \dot { a } } ^ { \mu } . } } \end{array} \tag{95.30}
	$$
</synced_block>
We thus have
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#b79c858b89b742c9b855813b174018a7">
	$$
	\begin{array} { l } { { \mathcal { Q } _ { a } \Phi ( y , \theta ) = \partial _ { a } \Phi ( y , \theta ) } } \\{ { { } } } \\{ { { } = \sqrt { 2 } \psi _ { a } ( y ) + 2 \theta _ { a } F ( y ) , } } \\{ { { } } } \\{ { \mathcal { Q } _ { \dot { a } } ^ { \ast } \Phi ( y , \theta ) = - 2 i \theta ^ { c } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } \Phi ( y , \theta ) } } \\{ { { } } } \\{ { { } = - 2 i \theta ^ { c } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } A ( y ) + i \sqrt { 2 } \theta \theta \partial _ { \mu } \psi ^ { c } ( y ) \sigma _ { c \dot { a } } ^ { \mu } , } } \end{array} \tag{95.31-95.32}
	$$
</synced_block>
where $`\partial _ { \mu }`$ is with respect to $`y`$ ; we used eq. (95.26) to get the last line. We can now find the supersymmetry transformations of the component fields $`A`$ , $`\psi`$ , and $`F`$ by matching powers of $`\theta`$ on each side of eqs. (95.8) and (95.9). Remembering that the $`Q`$ and $`Q ^ { \dagger }`$ operators anticommute with $`\theta`$ and $`\theta ^ { * }`$ , we get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#9d8a30b1def04d2187994a6fb6912704">
		$$
		\begin{array} { l l } { { \theta _ { a } \theta _ { b } = + { \frac { 1 } { 2 } } \theta \theta \varepsilon _ { a b } ~ , ~ } } & { { ~ \theta ^ { a } \theta ^ { b } = - { \frac { 1 } { 2 } } \theta \theta \varepsilon ^ { a b } ~ , } } \\{ { { } } } & { { { } } } \\{ { \theta _ { \dot { a } } ^ { * } \theta _ { \dot { b } } ^ { * } = - { \frac { 1 } { 2 } } \theta ^ { * } \theta ^ { * } \varepsilon _ { \dot { a } \dot { b } } ~ , ~ } } & { { ~ \theta ^ { * \dot { a } } \theta ^ { * \dot { b } } = + { \frac { 1 } { 2 } } \theta ^ { * } \theta ^ { * } \varepsilon ^ { \dot { a } \dot { b } } ~ , } } \end{array} \tag{95.26-95.27}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#5ee6588654744399b0c9c36f2e1f7989">
		$$
		\begin{array} { l } { { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { a } \right] = - i \mathcal { Q } _ { a } \Phi ( x , \theta , \theta ^ { * } ) , } } \\{ { \ } } \\{ { \left[ \Phi ( x , \theta , \theta ^ { * } ) , Q _ { \dot { a } } ^ { \dagger } \right] = - i \mathcal { Q } _ { \dot { a } } ^ { * } \Phi ( x , \theta , \theta ^ { * } ) , } } \end{array} \tag{95.8-95.9}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f6896490c6724092a6c53d6e91696d1f">
	$$
	\begin{array} { c c c } { { { } [ A , Q _ { a } ] = - i \sqrt { 2 } \psi _ { a } ~ , ~ } } & { { { } } } & { { [ A , Q _ { \dot { a } } ^ { \dagger } ] = 0 ~ , } } \\{ { { } \{ \psi _ { c } , Q _ { a } \} = - i \sqrt { 2 } \varepsilon _ { a c } F ~ , ~ } } & { { { } } } & { { \{ \psi _ { c } , Q _ { \dot { a } } ^ { \dagger } \} = - \sqrt { 2 } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } A ~ , } } \\{ { { } } } & { { { } } } & { { { { } [ F , Q _ { a } ] = 0 ~ , ~ } } } \end{array} \tag{95.33-95.35}
	$$
</synced_block>
where all component fields have space-time argument $`y`$ . However, $`y`$ is arbitrary, and so we are free to replace it with $`x`$ .
Eq. (95.35) is the most important: it tells us that the supersymmetry transformation of the $`F`$ field is a total derivative. Therefore, $`\textstyle \int d ^ { 4 } x F ( x )`$ is invariant under a supersymmetry transformation, and hence could be a term in the action of a supersymmetric theory.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#93182da2221040998788f12d9bf0157c">
		$$
		\begin{array} { c c c } { { { } [ A , Q _ { a } ] = - i \sqrt { 2 } \psi _ { a } ~ , ~ } } & { { { } } } & { { [ A , Q _ { \dot { a } } ^ { \dagger } ] = 0 ~ , } } \\{ { { } \{ \psi _ { c } , Q _ { a } \} = - i \sqrt { 2 } \varepsilon _ { a c } F ~ , ~ } } & { { { } } } & { { \{ \psi _ { c } , Q _ { \dot { a } } ^ { \dagger } \} = - \sqrt { 2 } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } A ~ , } } \\{ { { } } } & { { { } } } & { { { { } [ F , Q _ { a } ] = 0 ~ , ~ } } } \end{array} \tag{95.33-95.35}
		$$
	</synced_block>
</callout>
The product of two left-handed chiral superfields is another left-handed chiral superfield; this is obvious from eq. (95.25), and the fact that the $`\theta`$ expansion always terminates with the quadratic term. For two chiral superfields $`\Phi _ { 1 } ( y , \theta )`$ and $`\Phi _ { 2 } ( y , \theta )`$ , we have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#8f14acfc266c4e13904ca53bef6a7f7a">
		$$
		\Phi ( y , \theta ) = A ( y ) + \sqrt { 2 } \theta \psi ( y ) + \theta \theta F ( y ) , \tag{95.25}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#8047b65cf4ef44c591a24a1c5bb98eb7">
	$$
	\Phi _ { 1 } \Phi _ { 2 } = A _ { 1 } A _ { 2 } + \sqrt { 2 } \theta ( A _ { 1 } \psi _ { 2 } + A _ { 2 } \psi _ { 1 } ) + \theta \theta ( A _ { 1 } F _ { 2 } + A _ { 2 } F _ { 1 } - \psi _ { 1 } \psi _ { 2 } ) . \tag{95.36}
	$$
</synced_block>
More generally, given a set of left-handed chiral superfields $`\Phi _ { i }`$ , we can consider a function of them $`W ( \Phi )`$ ; this function is itself a left-handed chiral superfield. Its $`F ^ { \prime }`$ term (the coefficient of $`\theta \theta`$ ) is
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#9af45129829a4ecbbcfb355ceebd1558">
	$$
	W ( \Phi ) { \Big | } _ { F } = { \frac { \partial W ( A ) } { \partial A _ { i } } } F _ { i } - { \frac { 1 } { 2 } } { \frac { \partial ^ { 2 } W ( A ) } { \partial A _ { i } \partial A _ { j } } } \psi _ { i } \psi _ { j } , \tag{95.37}
	$$
</synced_block>
where repeated indices are summed. The space-time integral of this term (like the space-time integral of any $`F ^ { \prime }`$ term) is invariant under supersymmetry, and hence could be a term in the action of a supersymmetric theory. In this case, the function $`W ( \Phi )`$ is called the superpotential.
We still need kinetic terms. To get them, we first investigate the properties of a vector superfield. A vector superfield $`V ( x , \theta , \theta ^ { * } )`$ is hermitian,
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f8826921220741c7a0d252650a4f0d00">
	$$
	[ V ( x , \theta , \theta ^ { * } ) ] ^ { \dag } = V ( x , \theta , \theta ^ { * } ) , \tag{95.38}
	$$
</synced_block>
but is not subject to any other constraint. Its component expansion is
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#1c9ff031481b402ebb297b4b119449bb">
	$$
	\begin{array} { l } { { V ( x , \theta , \theta ^ { * } ) = C ( x ) + \theta \chi ( x ) + \theta ^ { * } \chi ^ { \dagger } ( x ) + \theta \theta M ( x ) + \theta ^ { * } \theta ^ { * } M ^ { \dagger } ( x ) } } \\{ { \ ~ + \theta \sigma ^ { \mu } \theta ^ { * } v _ { \mu } ( x ) + \theta \theta \theta ^ { * } \lambda ^ { \dagger } ( x ) + \theta ^ { * } \theta ^ { * } \theta \lambda ( x ) } } \\{ { \ ~ + \frac { 1 } { 2 } \theta \theta \theta ^ { * } \theta ^ { * } D ( x ) ~ , } } \end{array} \tag{95.39}
	$$
</synced_block>
where $`C`$ and $`D`$ are real scalar fields, $`M`$ is a complex scalar field, $`\chi`$ and $`\lambda`$ are left-handed Weyl fields, and $`v _ { \mu }`$ is a real vector field.
Following the analysis that led to eq. (95.35), we find
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f568d7f4d765482c8e1089febc408a3b">
		$$
		\begin{array} { c c c } { { { } [ A , Q _ { a } ] = - i \sqrt { 2 } \psi _ { a } ~ , ~ } } & { { { } } } & { { [ A , Q _ { \dot { a } } ^ { \dagger } ] = 0 ~ , } } \\{ { { } \{ \psi _ { c } , Q _ { a } \} = - i \sqrt { 2 } \varepsilon _ { a c } F ~ , ~ } } & { { { } } } & { { \{ \psi _ { c } , Q _ { \dot { a } } ^ { \dagger } \} = - \sqrt { 2 } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } A ~ , } } \\{ { { } } } & { { { } } } & { { { { } [ F , Q _ { a } ] = 0 ~ , ~ } } } \end{array} \tag{95.33-95.35}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#076c5bd8a2d7424dbe28e2521c59ccff">
	$$
	[ { \cal D } , Q _ { a } ] = - \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger \dot { c } } , \qquad [ { \cal D } , Q _ { \dot { a } } ^ { \dagger } ] = + \partial _ { \mu } \lambda ^ { c } \sigma _ { c \dot { a } } ^ { \mu } . \tag{95.40}
	$$
</synced_block>
We see that the supersymmetry transformation of the $`D`$ component of a vector superfield is a total derivative. Therefore, $`\int d ^ { 4 } x D ( x )`$ is invariant under a supersymmetry transformation, and hence could be a term in the action of a supersymmetric theory.
Consider the product of a left-handed chiral superfield $`\Phi ( x , \theta , \theta ^ { * } )`$ , as given by eq. (95.29), and its hermitian conjugate
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#c6e2407f13fd412b99fefa27dfa5cc22">
		$$
		\begin{array} { l } { { \Phi ( x , \theta , \theta ^ { * } ) = A ( x ) + \sqrt { 2 } \theta \psi ( x ) + \theta \theta F ( x ) - i ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } A ( x ) } } \\{ { - \frac { 1 } { \sqrt { 2 } } i \theta \theta \theta ^ { * } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi ( x ) + \frac { 1 } { 4 } \theta \theta \theta ^ { * } \theta ^ { * } \partial ^ { 2 } A ( x ) . } } \end{array} \tag{95.29}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#d82ee53c10e343d09f9753eabfc7251b">
	$$
	\begin{array} { r } { \Phi ^ { \dagger } ( x , \theta , \theta ^ { * } ) = A ( x ) + \sqrt { 2 } \theta ^ { * } \psi ^ { \dagger } ( x ) + \theta ^ { * } \theta ^ { * } F ^ { \dagger } ( x ) + i ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } A ^ { \dagger } ( x ) } \\{ + \frac { 1 } { \sqrt { 2 } } i \theta ^ { * } \theta ^ { * } \partial _ { \mu } \psi ^ { \dagger } ( x ) \bar { \sigma } ^ { \mu } \theta + \frac { 1 } { 4 } \theta \theta \theta ^ { * } \theta ^ { * } \partial ^ { 2 } A ^ { \dagger } ( x ) \ . \qquad ( \mathfrak { g } ^ { * } \theta ^ { * } \nabla ^ { 2 } A ^ { \dagger } ( x ) ) } \end{array} \tag{95.41}
	$$
</synced_block>
The product $`\Phi ^ { \dag } \Phi`$ is obviously hermitian, and so is a vector superfield. After considerable use of eqs. (95.26)–(95.28), we find that the $`D`$ term (the coefficient of $`\theta \theta \theta ^ { * } \theta ^ { * }`$ ) of this vector superfield is
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#2376e2daf3764853894a68439eba235a">
		$$
		\begin{array} { l l } { { \theta _ { a } \theta _ { b } = + { \frac { 1 } { 2 } } \theta \theta \varepsilon _ { a b } ~ , ~ } } & { { ~ \theta ^ { a } \theta ^ { b } = - { \frac { 1 } { 2 } } \theta \theta \varepsilon ^ { a b } ~ , } } \\{ { { } } } & { { { } } } \\{ { \theta _ { \dot { a } } ^ { * } \theta _ { \dot { b } } ^ { * } = - { \frac { 1 } { 2 } } \theta ^ { * } \theta ^ { * } \varepsilon _ { \dot { a } \dot { b } } ~ , ~ } } & { { ~ \theta ^ { * \dot { a } } \theta ^ { * \dot { b } } = + { \frac { 1 } { 2 } } \theta ^ { * } \theta ^ { * } \varepsilon ^ { \dot { a } \dot { b } } ~ , } } \end{array} \tag{95.26-95.27}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#b80f4c09cc73437ab5ef66821534854e">
		$$
		\begin{array} { r } { ( \theta \sigma ^ { \mu } \theta ^ { * } ) ( \theta \sigma ^ { \nu } \theta ^ { * } ) = - \frac { 1 } { 2 } \theta \theta \theta ^ { * } \theta ^ { * } g ^ { \mu \nu } , } \end{array} \tag{95.28}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#8f6e5c5a35a04bf69ec0ecc427f9976d">
	$$
	\begin{array} { l } { { \Phi ^ { \dag } \Phi \Big \vert _ { D } = - \frac { 1 } { 2 } \partial ^ { \mu } A ^ { \dag } \partial _ { \mu } A + \frac { 1 } { 4 } A \partial ^ { 2 } A ^ { \dag } + \frac { 1 } { 4 } A ^ { \dag } \partial ^ { 2 } A } } \\{ { \qquad + \frac { 1 } { 2 } i \psi ^ { \dag } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi - \frac { 1 } { 2 } i \partial _ { \mu } \psi ^ { \dag } \bar { \sigma } ^ { \mu } \psi } } \\{ { \qquad + F ^ { \dag } F . } } \end{array} \tag{95.42}
	$$
</synced_block>
The space-time integral of this term (like the space-time integral of any $`\mathcal { D }`$ term) is invariant under supersymmetry, and hence could be a term in the action of a supersymmetric theory. After some integrations by parts, and dropping total divergences, we find
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#0d8607adddb645c5864da4fb5bac6041">
	$$
	\Phi ^ { \dagger } \Phi \Bigr | _ { D } = - \partial ^ { \mu } A ^ { \dagger } \partial _ { \mu } A + i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi + F ^ { \dagger } F . \tag{95.43}
	$$
</synced_block>
We see that we have standard kinetic terms for the complex scalar field $`A`$ and the left-handed Weyl field $`\psi`$ . We also have a term with no derivatives for the complex scalar field $`F`$ . The $`F`$ field is therefore called an auxiliary field.
If we consider a set of left-handed chiral superfields $`\Phi _ { i }`$ , we get a hermitian, supersymmetric action if we take as the lagrangian
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#cd9cb61d376d4791889e21dbafba54d2">
	$$
	\mathcal { L } = \left. \Phi _ { i } ^ { \dagger } \Phi _ { i } \right| _ { D } + \left. \left( W ( \Phi ) \right| _ { F } + \mathrm { h . c . } \right) , \tag{95.44}
	$$
</synced_block>
where the index in the first term is summed. Since $`F _ { i }`$ appears only quadratically and without derivatives, we can easily perform the path integral over it. The result is equivalent to solving the classical equation of motion for $`F _ { i } ^ { \prime }`$ ,
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#3f68ce08ce6b4eebb30e36ca7049edb4">
	$$
	\frac { \partial \mathcal { L } } { \partial F _ { i } } = F _ { i } ^ { \dagger } + \frac { \partial W ( A ) } { \partial A _ { i } } = 0 , \tag{95.45}
	$$
</synced_block>
and substituting the solution back into the lagrangian; the result is
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#21074353aad540dfbc091b8a0676ae4e">
	$$
	\begin{array} { l } { \displaystyle { \mathcal { L } = - \partial ^ { \mu } A _ { i } ^ { \dagger } \partial _ { \mu } A _ { i } + i \psi _ { i } ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi _ { i } } } \\{ \displaystyle \quad - \left| \frac { \partial W ( A ) } { \partial A _ { i } } \right| ^ { 2 } - \frac { 1 } { 2 } \biggl [ \frac { \partial ^ { 2 } W ( A ) } { \partial A _ { i } \partial A _ { j } } \psi _ { i } \psi _ { j } + \mathrm { h . c . } \biggr ] \ : , } \end{array} \tag{95.46}
	$$
</synced_block>
where the indices are summed in each term.
As an example, let us consider a single left-handed chiral superfield, with superpotential
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#b2a5eb43f32d4bc6bc0527f7cfd5a7c9">
	$$
	\begin{array} { r } { W ( A ) = \frac { 1 } { 2 } m A ^ { 2 } + \frac { 1 } { 6 } g A ^ { 3 } . } \end{array} \tag{95.47}
	$$
</synced_block>
This is the Wess–Zumino model. The scalar potential is
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#c925bf4172c54e6cad66f102a7135c44">
	$$
	\begin{array} { r l } & { V ( A ) = | \partial W / \partial A | ^ { 2 } } \\& { \qquad = m ^ { 2 } A ^ { \dagger } A + \frac { 1 } { 2 } g m ( A ^ { \dagger } A ^ { 2 } + A ^ { \dagger 2 } A ) + \frac { 1 } { 4 } g ^ { 2 } ( A ^ { \dagger } A ) ^ { 2 } . } \end{array} \tag{95.48}
	$$
</synced_block>
We see that the scalar has mass $`m`$ . The last term in eq. (95.46) becomes
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#78e2fc38ba704194a292f4a6aa9e158c">
		$$
		\begin{array} { l } { \displaystyle { \mathcal { L } = - \partial ^ { \mu } A _ { i } ^ { \dagger } \partial _ { \mu } A _ { i } + i \psi _ { i } ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi _ { i } } } \\{ \displaystyle \quad - \left| \frac { \partial W ( A ) } { \partial A _ { i } } \right| ^ { 2 } - \frac { 1 } { 2 } \biggl [ \frac { \partial ^ { 2 } W ( A ) } { \partial A _ { i } \partial A _ { j } } \psi _ { i } \psi _ { j } + \mathrm { h . c . } \biggr ] \ : , } \end{array} \tag{95.46}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#964944295e12429e99c5f3a92031790e">
	$$
	\begin{array} { r } { \mathcal { L } _ { \mathrm { m a s s + Y u k } } = - \frac { 1 } { 2 } m \psi \psi - \frac { 1 } { 2 } g A \psi \psi + \mathrm { h . c . } . } \end{array} \tag{95.46, 95.49}
	$$
</synced_block>
We see that the fermion also has mass $`m`$ , and a Yukawa interaction with the scalar. The Yukawa couping is related (by supersymmetry) to the cubic and quartic self-interactions of the scalar.
Next we would like to introduce gauge fields. Recall that the vector superfield $`V ( x , \theta , \theta ^ { * } )`$ has among its components a real vector field $`v _ { \mu } ( x )`$ that could be identified as an abelian gauge field. (Later we will add an adjoint index to the superfield in order to get a nonabelian gauge field.)
We need to generalize the notion of a gauge transformation to superfields. We begin by noting that if $`\Xi`$ is a left-handed chiral superfield, then $`i ( \Xi ^ { \dagger } - \Xi )`$ is a vector superfield. We then define a supergauge transformation
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#32b7bd62dc2846088e202bfafa816623">
	$$
	V V + i ( \Xi ^ { \dagger } - \Xi ) . \tag{95.50}
	$$
</synced_block>
We will attempt to construct actions that are invariant under eq. (95.50). Following the pattern of eqs. (95.29) and (95.41), we write
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#280d5ef20c414539ace02bcb0e64dd33">
		$$
		V V + i ( \Xi ^ { \dagger } - \Xi ) . \tag{95.50}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#58b92548ffcf4992a1dfd145a47e2684">
		$$
		\begin{array} { l } { { \Phi ( x , \theta , \theta ^ { * } ) = A ( x ) + \sqrt { 2 } \theta \psi ( x ) + \theta \theta F ( x ) - i ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } A ( x ) } } \\{ { - \frac { 1 } { \sqrt { 2 } } i \theta \theta \theta ^ { * } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi ( x ) + \frac { 1 } { 4 } \theta \theta \theta ^ { * } \theta ^ { * } \partial ^ { 2 } A ( x ) . } } \end{array} \tag{95.29}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#0896c95414734f039b1fe59e5818415f">
		$$
		\begin{array} { r } { \Phi ^ { \dagger } ( x , \theta , \theta ^ { * } ) = A ( x ) + \sqrt { 2 } \theta ^ { * } \psi ^ { \dagger } ( x ) + \theta ^ { * } \theta ^ { * } F ^ { \dagger } ( x ) + i ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } A ^ { \dagger } ( x ) } \\{ + \frac { 1 } { \sqrt { 2 } } i \theta ^ { * } \theta ^ { * } \partial _ { \mu } \psi ^ { \dagger } ( x ) \bar { \sigma } ^ { \mu } \theta + \frac { 1 } { 4 } \theta \theta \theta ^ { * } \theta ^ { * } \partial ^ { 2 } A ^ { \dagger } ( x ) \ . \qquad ( \mathfrak { g } ^ { * } \theta ^ { * } \nabla ^ { 2 } A ^ { \dagger } ( x ) ) } \end{array} \tag{95.41}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#8ce0137df84e44bb968c196bb2c44c71">
	$$
	\begin{array} { c } { { \Xi ( x , \theta , \theta ^ { * } ) = { \cal B } ( x ) + \theta \xi ( x ) + \theta \theta { \cal G } ( x ) } } \\{ { { } } } \\{ { - i ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } { \cal B } ( x ) + \ldots ~ , } } \\{ { { } } } \\{ { \Xi ^ { \dag } ( x , \theta , \theta ^ { * } ) = { \cal B } ^ { \dag } ( x ) + \theta ^ { * } \xi ^ { \dag } ( x ) + \theta ^ { * } \theta ^ { * } { \cal G } ^ { \dag } ( x ) } } \\{ { { } } } \\{ { + i ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } { \cal B } ^ { \dag } ( x ) + \ldots ~ . } } \end{array} \tag{95.51}
	$$
</synced_block>
If we set $`B = { \textstyle { \frac { 1 } { 2 } } } ( b + i a )`$ , where $`a`$ and $`b`$ are real scalar fields, we find
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#936c39c2a1be4244a1e50a383f8e46c4">
	$$
	i ( \Xi ^ { \dagger } - \Xi ) = a - i \theta \xi + i \theta ^ { * } \xi ^ { \dagger } - i \theta \theta G + i \theta ^ { * } \theta ^ { * } G ^ { \dagger } - ( \theta \sigma ^ { \mu } \theta ^ { * } ) \partial _ { \mu } b + \ldots . \tag{95.52, 95.53, 95.50}
	$$
</synced_block>
From eq. (95.39), we see that the supergauge transformation of eq. (95.50) results in
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#e18641cb071f46f9aa4eec26dbfaef9d">
		$$
		\begin{array} { l } { { V ( x , \theta , \theta ^ { * } ) = C ( x ) + \theta \chi ( x ) + \theta ^ { * } \chi ^ { \dagger } ( x ) + \theta \theta M ( x ) + \theta ^ { * } \theta ^ { * } M ^ { \dagger } ( x ) } } \\{ { \ ~ + \theta \sigma ^ { \mu } \theta ^ { * } v _ { \mu } ( x ) + \theta \theta \theta ^ { * } \lambda ^ { \dagger } ( x ) + \theta ^ { * } \theta ^ { * } \theta \lambda ( x ) } } \\{ { \ ~ + \frac { 1 } { 2 } \theta \theta \theta ^ { * } \theta ^ { * } D ( x ) ~ , } } \end{array} \tag{95.39}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#d22c69a6251f4dc9bb6ec9085b9af9ce">
		$$
		V V + i ( \Xi ^ { \dagger } - \Xi ) . \tag{95.50}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#1803bf83ef57435eb800e412efbe13a6">
	$$
	\begin{array} { c } { { C C + a ~ , } } \\{ { \chi \chi - i \xi ~ , } } \\{ { M M - i G ~ , } } \\{ { v _ { \mu } v _ { \mu } - \partial _ { \mu } b ~ . } } \end{array} \tag{95.54}
	$$
</synced_block>
The last of these is the usual abelian gauge transformation. The first three allow us to gauge away the $`C`$ , $`\chi`$ , and $`M`$ components of a vector superfield. That is, we can make a supergauge transformation with $`a = - C`$ , $`\xi = - i \chi`$ and $`G = - i M`$ ; in this gauge, known as Wess–Zumino gauge, the vector superfield becomes
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#98e6c044880f43b6a039cebae887d03c">
	$$
	\begin{array} { r } { V = ( \theta \sigma ^ { \mu } \theta ^ { * } ) v _ { \mu } + \theta \theta \theta ^ { * } \lambda ^ { \dagger } + \theta ^ { * } \theta ^ { * } \theta \lambda + \frac { 1 } { 2 } \theta \theta \theta ^ { * } \theta ^ { * } D ~ . } \end{array} \tag{95.55}
	$$
</synced_block>
Note that we still have the freedom to make the supergauge transformation of eq. (95.50) with $`\begin{array} { r } { B ( x ) = \frac { 1 } { 2 } b ( x ) } \end{array}`$ , and that this still implements the ordinary abelian gauge transformation of eq. (95.54).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#1a617eb6b2324228910ce74247f8e40b">
		$$
		V V + i ( \Xi ^ { \dagger } - \Xi ) . \tag{95.50}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#e758ad9ea4b5474095b03aa2a6b0718c">
		$$
		\begin{array} { c } { { C C + a ~ , } } \\{ { \chi \chi - i \xi ~ , } } \\{ { M M - i G ~ , } } \\{ { v _ { \mu } v _ { \mu } - \partial _ { \mu } b ~ . } } \end{array} \tag{95.54}
		$$
	</synced_block>
</callout>
Now consider a left-handed chiral superfield $`\Phi`$ that has charge $`+ 1`$ under a $`\mathrm { U } ( 1 )`$ gauge group. We take the kinetic term for $`\Phi`$ to be
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#88623cb52da945d28e5fed2bdf872f5b">
	$$
	\mathcal { L } _ { \mathrm { k i n } } = \Phi ^ { \dagger } e ^ { - 2 g V } \Phi \Big | _ { D } ~ , \tag{95.56}
	$$
</synced_block>
where $`g`$ is the gauge coupling. The vector superfield $`\Phi ^ { \dagger } e ^ { - 2 g V } \Phi`$ is clearly invariant under the supergauge transformation
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#e9fcbe638d4645448add480ef1ebb40c">
	$$
	\begin{array} { l } { { \Phi e ^ { - 2 i g \Xi } \Phi ~ , } } \\{ { { } } } \\{ { \Phi ^ { \dag } \Phi ^ { \dag } e ^ { + 2 i g \Xi ^ { \dag } } ~ , } } \\{ { { } } } \\{ { V V + i ( \Xi ^ { \dag } - \Xi ) ~ . } } \end{array} \tag{95.57-95.59}
	$$
</synced_block>
Let us evaluate eq. (95.56) in Wess–Zumino gauge, where we have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#fec7891c8557428cb61d7e2165bb0d0f">
		$$
		\mathcal { L } _ { \mathrm { k i n } } = \Phi ^ { \dagger } e ^ { - 2 g V } \Phi \Big | _ { D } ~ , \tag{95.56}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#a864bdd656b24962956d429e890e2c4e">
	$$
	\begin{array} { l } { { { \cal V } ^ { 2 } = - { \frac { 1 } { 2 } } \theta \theta \theta ^ { * } \theta ^ { * } v ^ { \mu } v _ { \mu } , } } \\{ { } } \\{ { { \cal V } ^ { 3 } = 0 . } } \end{array} \tag{95.60-95.61}
	$$
</synced_block>
The exponential factor in eq. (95.56) becomes
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#89ae5e14919948c99e3f125a25eafb61">
		$$
		\mathcal { L } _ { \mathrm { k i n } } = \Phi ^ { \dagger } e ^ { - 2 g V } \Phi \Big | _ { D } ~ , \tag{95.56}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#9600226bc58c47a1b221df343b7e87f5">
	$$
	\begin{array} { c } { { e ^ { - 2 g V } = 1 - 2 g ( \theta \sigma ^ { \mu } \theta ^ { * } ) v _ { \mu } - 2 g \theta \theta \theta ^ { * } \lambda ^ { \dagger } - 2 g \theta ^ { * } \theta ^ { * } \theta \lambda } } \\{ { - \theta \theta \theta ^ { * } \theta ^ { * } ( g D + g ^ { 2 } v ^ { \mu } v _ { \mu } ) . } } \end{array} \tag{95.62}
	$$
</synced_block>
The relevant terms in $`\Phi ^ { \dag } \Phi`$ are
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#3ed8580b8bf147d2bc30523e34670c6b">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { \Phi ^ { \dagger } \Phi = A ^ { \dagger } A + \sqrt { 2 } \theta ^ { * } \psi ^ { \dagger } A + \sqrt { 2 } \theta \psi A ^ { \dagger } } } \\{ { } } & { { } } & { { + ( \theta \sigma ^ { \mu } \theta ^ { * } ) ( \psi ^ { \dagger } \bar { \sigma } _ { \mu } \psi - i A ^ { \dagger } \partial _ { \mu } A + i A \partial _ { \mu } A ^ { \dagger } ) } } \\{ { } } & { { } } & { { + . . . + \theta \theta \theta ^ { * } \theta ^ { * } ( \Phi ^ { \dagger } \Phi ) _ { D } , } } \end{array} \tag{95.63}
	$$
</synced_block>
where we used $`2 ( \theta ^ { * } \psi ^ { \dagger } ) ( \theta \psi ) = ( \theta \sigma ^ { \mu } \theta ^ { * } ) ( \psi ^ { \dagger } \bar { \sigma } _ { \mu } \psi )`$ to get the first term in the second line, and $`( \Phi ^ { \dagger } \Phi ) _ { D }`$ is given by eq. (95.42).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#922703cd3f0d4f9e81c379ec445d5790">
		$$
		\begin{array} { l } { { \Phi ^ { \dag } \Phi \Big \vert _ { D } = - \frac { 1 } { 2 } \partial ^ { \mu } A ^ { \dag } \partial _ { \mu } A + \frac { 1 } { 4 } A \partial ^ { 2 } A ^ { \dag } + \frac { 1 } { 4 } A ^ { \dag } \partial ^ { 2 } A } } \\{ { \qquad + \frac { 1 } { 2 } i \psi ^ { \dag } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi - \frac { 1 } { 2 } i \partial _ { \mu } \psi ^ { \dag } \bar { \sigma } ^ { \mu } \psi } } \\{ { \qquad + F ^ { \dag } F . } } \end{array} \tag{95.42}
		$$
	</synced_block>
</callout>
Combining eqs. (95.62) and (95.63), taking the $`D`$ term, and performing the same integrations by parts that led to eq. (95.43), we find
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#556001515caa44e4a0a956109b7e1752">
		$$
		\begin{array} { c } { { e ^ { - 2 g V } = 1 - 2 g ( \theta \sigma ^ { \mu } \theta ^ { * } ) v _ { \mu } - 2 g \theta \theta \theta ^ { * } \lambda ^ { \dagger } - 2 g \theta ^ { * } \theta ^ { * } \theta \lambda } } \\{ { - \theta \theta \theta ^ { * } \theta ^ { * } ( g D + g ^ { 2 } v ^ { \mu } v _ { \mu } ) . } } \end{array} \tag{95.62}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#6eaaedaaf0674a16a6e6453753e98373">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { \Phi ^ { \dagger } \Phi = A ^ { \dagger } A + \sqrt { 2 } \theta ^ { * } \psi ^ { \dagger } A + \sqrt { 2 } \theta \psi A ^ { \dagger } } } \\{ { } } & { { } } & { { + ( \theta \sigma ^ { \mu } \theta ^ { * } ) ( \psi ^ { \dagger } \bar { \sigma } _ { \mu } \psi - i A ^ { \dagger } \partial _ { \mu } A + i A \partial _ { \mu } A ^ { \dagger } ) } } \\{ { } } & { { } } & { { + . . . + \theta \theta \theta ^ { * } \theta ^ { * } ( \Phi ^ { \dagger } \Phi ) _ { D } , } } \end{array} \tag{95.63}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#589a6236af52417aa18d18200bcafd7d">
		$$
		\Phi ^ { \dagger } \Phi \Bigr | _ { D } = - \partial ^ { \mu } A ^ { \dagger } \partial _ { \mu } A + i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi + F ^ { \dagger } F . \tag{95.43}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#12cbfd050f354cadb8fb58cc3d437352">
	$$
	\begin{array} { l } { { \Phi ^ { \dagger } e ^ { - 2 g V } \Phi \Bigr | _ { D } = - ( D ^ { \mu } A ) ^ { \dagger } D _ { \mu } A + i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } D _ { \mu } \psi + F ^ { \dagger } F } } \\{ { + \sqrt { 2 } g \psi ^ { \dagger } \lambda ^ { \dagger } A + \sqrt { 2 } g A ^ { \dagger } \lambda \psi - g A ^ { \dagger } D A , } } \end{array} \tag{95.64}
	$$
</synced_block>
where $`D _ { \mu } = { \partial } _ { \mu } - i g v _ { \mu }`$ is the usual gauge covariant derivative acting on a field of charge $`+ 1`$ .
We still need a kinetic term for the vector superfield. To get it, we first introduce a superfield that carries a left-handed spinor index,
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#c6d28cc41d3645788980358c5d3ddd48">
	$$
	W _ { a } \equiv { \textstyle \frac { 1 } { 4 } } { \cal D } _ { \dot { a } } ^ { * } { \cal D } ^ { * { \dot { a } } } { \cal { D } } _ { a } V ~ . \tag{95.65}
	$$
</synced_block>
Since the two components of $`{ \mathcal { D } } ^ { * }`$ anticommute, we have $`\mathcal { D } _ { \dot { a } } ^ { * } \mathcal { D } _ { \dot { b } } ^ { * } \mathcal { D } _ { \dot { c } } ^ { * } = 0`$ . Thus $`W _ { a }`$ obeys $`\mathcal { D } _ { \dot { a } } ^ { * } W _ { a } = 0`$ , and is therefore a left-handed chiral superfield. Furthermore, $`W _ { a }`$ is invariant under the supergauge transformation of eq. (95.50). To see this, we first note that $`\mathcal { D } _ { \dot { a } } ^ { * } \mathcal { D } ^ { * \dot { a } } \mathcal { D } _ { a }`$ annihilates $`\Xi ^ { \dagger }`$ (because $`\mathcal { D } _ { a }`$ does). Then, we use eq. (95.19) to write
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#d2b35937781f4f3d9f5462ed80b2cdfc">
		$$
		V V + i ( \Xi ^ { \dagger } - \Xi ) . \tag{95.50}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#cab0b60042474bb7b2278257c86c3be1">
		$$
		\{ { \mathcal D } _ { a } , { \mathcal D } _ { \dot { a } } ^ { * } \} = 2 i \sigma _ { a \dot { a } } ^ { \mu } \partial _ { \mu } , \tag{95.19}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#b565078f5b744a07b1510a4c9688b1bc">
	$$
	{ \mathcal { D } } _ { \dot { a } } ^ { * } { \mathcal { D } } ^ { * { \dot { a } } } { \mathcal { D } } _ { a } = - ( { \mathcal { D } } _ { \dot { a } } ^ { * } { \mathcal { D } } _ { a } + 2 i \sigma _ { a { \dot { a } } } ^ { \mu } \partial _ { \mu } ) { \mathcal { D } } ^ { * { \dot { a } } } ~ . \tag{95.66}
	$$
</synced_block>
Thus, $`\mathcal { D } _ { \dot { a } } ^ { * } \mathcal { D } ^ { * \dot { a } } \mathcal { D } _ { a }`$ also annihilates $`\Xi`$ (because $`\mathbf { \nabla } \mathcal { D } ^ { * \dot { a } }`$ does). Therefore, $`W _ { a }`$ is invariant under eq. (95.50).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#24c356da0c414183931a21792ad6843a">
		$$
		V V + i ( \Xi ^ { \dagger } - \Xi ) . \tag{95.50}
		$$
	</synced_block>
</callout>
Since $`W _ { a }`$ is a left-handed chiral superfield, it has an expansion in the form of eq. (95.25). To find the component fields of $`W _ { a }`$ , we set $`x = y + i \theta \sigma ^ { \mu } \theta ^ { * }`$ in eq. (95.55), and expand in $`\theta`$ and $`\theta ^ { * }`$ . The result is
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#ef55cd3c4c1742f2be46ec6cd00e56c2">
		$$
		\Phi ( y , \theta ) = A ( y ) + \sqrt { 2 } \theta \psi ( y ) + \theta \theta F ( y ) , \tag{95.25}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#d958e20d966c4dc6ac0072dfc2f6dccd">
		$$
		\begin{array} { r } { V = ( \theta \sigma ^ { \mu } \theta ^ { * } ) v _ { \mu } + \theta \theta \theta ^ { * } \lambda ^ { \dagger } + \theta ^ { * } \theta ^ { * } \theta \lambda + \frac { 1 } { 2 } \theta \theta \theta ^ { * } \theta ^ { * } D ~ . } \end{array} \tag{95.55}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f381ff604a91471b98dbe9a0614a43e9">
	$$
	V = ( \theta \sigma ^ { \mu } \theta ^ { \ast } ) v _ { \mu } + \theta \theta \theta ^ { \ast } \lambda ^ { \dagger } + \theta ^ { \ast } \theta ^ { \ast } \theta \lambda + { \textstyle { \frac { 1 } { 2 } } } \theta \theta \theta ^ { \ast } \theta ^ { \ast } ( D - i \partial ^ { \mu } v _ { \mu } ) , \tag{95.67}
	$$
</synced_block>
where all component fields have space-time argument $`y`$ . From eq. (95.24), we see that $`\mathcal { D } _ { \dot { a } } ^ { * } = - \dot { o } _ { \dot { a } } ^ { * }`$ when it acts on a function of $`y`$ , $`\theta`$ , and $`\theta ^ { * }`$ . We also have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#da26654f42aa48c18ed52a306201de92">
		$$
		{ \mathcal D } _ { \dot { a } } ^ { * } \theta _ { a } = 0 \quad \mathrm { a n d } \quad { \mathcal D } _ { \dot { a } } ^ { * } y ^ { \mu } = 0 . \tag{95.24}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#79ae523d3bb849ccb66760ab8a2655bf">
	$$
	\mathcal { D } _ { a } = ( \mathcal { D } _ { a } \theta ^ { c } ) \partial _ { c } + ( \mathcal { D } _ { a } \theta ^ { * \dot { c } } ) \partial _ { \dot { c } } ^ { * } + ( \mathcal { D } _ { a } y ^ { \mu } ) \partial _ { \mu } = \partial _ { a } + 0 - 2 i \sigma _ { a \dot { a } } ^ { \mu } \theta ^ { * \dot { a } } \partial _ { \mu } , \tag{95.68}
	$$
</synced_block>
where $`\partial _ { \mu }`$ is with respect to $`y`$ . Using eq. (95.68), we find
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f4cad27b77ca4a3e8faaa56406d874c4">
		$$
		\mathcal { D } _ { a } = ( \mathcal { D } _ { a } \theta ^ { c } ) \partial _ { c } + ( \mathcal { D } _ { a } \theta ^ { * \dot { c } } ) \partial _ { \dot { c } } ^ { * } + ( \mathcal { D } _ { a } y ^ { \mu } ) \partial _ { \mu } = \partial _ { a } + 0 - 2 i \sigma _ { a \dot { a } } ^ { \mu } \theta ^ { * \dot { a } } \partial _ { \mu } , \tag{95.68}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#36a5c41d1ad94c1996debb110135ab5c">
	$$
	\begin{array} { c } { { { \mathcal D } _ { a } V = \theta ^ { * } \theta ^ { * } \Big [ \lambda _ { a } + \theta _ { a } ( D - i \partial \cdot v ) - i ( \sigma ^ { \mu } \bar { \sigma } ^ { \nu } \theta ) _ { a } \partial _ { \mu } v _ { \nu } + i \theta \theta ( \sigma ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger } ) _ { a } \Big ] } } \\{ { + \dots . } } \end{array} \tag{95.69}
	$$
</synced_block>
When we act on $`D _ { a } V`$ with $`\mathcal { D } _ { \dot { a } } ^ { * } \mathcal { D } ^ { * \dot { a } } = \partial _ { \dot { a } } ^ { * } \partial ^ { * \dot { a } }`$ to get $`W _ { a }`$ , only the coefficient of $`\theta ^ { * } \theta ^ { * }`$ survives. Since $`\partial _ { \dot { a } } ^ { * } \partial ^ { * \dot { a } } ( \theta ^ { * } \theta ^ { * } ) = 4`$ , we find
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f33f26fa30f4468cac7b77bd3e153451">
	$$
	W _ { a } = \lambda _ { a } + \theta _ { a } ( D - i \partial \cdot v ) - i ( \sigma ^ { \mu } \bar { \sigma } ^ { \nu } \theta ) _ { a } \partial _ { \mu } v _ { \nu } + i \theta \theta ( \sigma ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger } ) _ { a } . \tag{95.70}
	$$
</synced_block>
We can simplify eq. (95.70) by using the identity
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#0e70466a03ee4b15bd4e915c31e92159">
		$$
		W _ { a } = \lambda _ { a } + \theta _ { a } ( D - i \partial \cdot v ) - i ( \sigma ^ { \mu } \bar { \sigma } ^ { \nu } \theta ) _ { a } \partial _ { \mu } v _ { \nu } + i \theta \theta ( \sigma ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger } ) _ { a } . \tag{95.70}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#8ec6b899be474a71af65a416b6917c6f">
	$$
	( \sigma ^ { \mu } \bar { \sigma } ^ { \nu } ) _ { a } { } ^ { b } = - g ^ { \mu \nu } \delta _ { a } { } ^ { c } - 2 i ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) _ { a } { } ^ { b } \ . \tag{95.71}
	$$
</synced_block>
Remembering that $`S _ { \mathrm { { L } } } ^ { \mu \nu }`$ is antisymmetric on $`\mu \nu`$ , and defining the field strength
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#a09bf73e3a284d5abf52aa93775758ba">
	$$
	F _ { \mu \nu } \equiv \partial _ { \mu } v _ { \nu } - \partial _ { \nu } v _ { \mu } , \tag{95.72}
	$$
</synced_block>
we get
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#964263c036cb4fdc9a8fe29bd3c5ca3e">
	$$
	W _ { a } = \lambda _ { a } + \theta _ { a } D - ( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { } ^ { c } \theta _ { c } F _ { \mu \nu } + i \theta \theta \sigma _ { a \dot { a } } ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger \dot { a } } \ . \tag{95.73}
	$$
</synced_block>
We see that $`W _ { a }`$ involves the vector field $`v _ { \mu }`$ only through its gauge-invariant field strength $`F _ { \mu \nu }`$ . Since $`W _ { a }`$ is supergauge invariant, this is to be expected.
Next, consider the $`F`$ term of $`W ^ { a } W _ { a }`$ . This term is Lorentz invariant, and its space-time integral (like the space-time integral of any $`F ^ { \prime }`$ term) is invariant under supersymmetry, and hence could be a term in the action of a supersymmetric theory. Working out the components, we find
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#f26f626273384f16934b0b7ca486b3c6">
	$$
	\left. W ^ { a } W _ { a } \right| _ { F } = 2 i \lambda ^ { a } \sigma _ { a \dot { a } } ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger \dot { a } } - { \textstyle \frac { 1 } { 2 } } \mathrm { T r } ( S _ { \mathrm { L } } ^ { \mu \nu } S _ { \mathrm { L } } ^ { \rho \sigma } ) F _ { \mu \nu } F _ { \rho \sigma } + { \cal D } ^ { 2 } , \tag{95.74}
	$$
</synced_block>
where $`\mathrm { T r } ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } S _ { \mathrm { \scriptscriptstyle L } } ^ { \rho o } ) = ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) _ { a } { } ^ { c } ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \rho o } ) _ { c } { } ^ { a }`$ . To get the spin matrices into this form, we used the fact that $`( S _ { \mathrm { L } } ^ { \mu \nu } ) _ { a c }`$ is symmetric on $`a c`$ . Now we use the identity
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#9e9a0f35c2554333b0747a75e17a6fdc">
	$$
	\begin{array} { r } { \operatorname{Tr} ( S _ { \mathrm { { L } } } ^ { \mu \nu } S _ { \mathrm { { L } } } ^ { \rho \sigma } ) = \frac { 1 } { 2 } ( g ^ { \mu \rho } g ^ { \nu \sigma } - g ^ { \mu \sigma } g ^ { \nu \rho } ) - \frac { 1 } { 2 } i \varepsilon ^ { \mu \nu \rho \sigma } } \end{array} \tag{95.75}
	$$
</synced_block>
to get
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#73286879638545ffb28e0324aa271311">
	$$
	\left. W ^ { a } W _ { a } \right| _ { F } = 2 i \lambda ^ { a } \sigma _ { a \dot { a } } ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger \dot { a } } - { \textstyle \frac { 1 } { 2 } } F ^ { \mu \nu } F _ { \mu \nu } - { \textstyle \frac { 1 } { 2 } } i \tilde { F } ^ { \mu \nu } F _ { \mu \nu } + { \cal D } ^ { 2 } , \tag{95.76}
	$$
</synced_block>
where $`\begin{array} { r } { \tilde { F } ^ { \mu \nu } = \frac { 1 } { 2 } \varepsilon ^ { \mu \nu \rho \sigma } F _ { \rho \sigma } } \end{array}`$ . We can now identify the kinetic term for the vector superfield as
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#17c4bef0ecb747daac5c353e67919dad">
	$$
	\begin{array} { r } { \mathcal { L } _ { \mathrm { k i n } } = \frac { 1 } { 4 } W ^ { a } W _ { a } \Big | _ { F } + \mathrm { h . c . } ~ } \\{ = i \lambda ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \lambda - \frac { 1 } { 4 } F ^ { \mu \nu } F _ { \mu \nu } + \frac { 1 } { 2 } D ^ { 2 } . } \end{array} \tag{95.77}
	$$
</synced_block>
We integrated by parts and dropped total divergences to get the second line. We see that we have the standard kinetic terms for the gauge field $`v _ { \mu }`$ and the gaugino field $`\lambda`$ , while $`D`$ is an auxiliary field.
All of this generalizes in a straightforward way to the nonabelian case. We define a matrix-valued vector superfield $`V = V ^ { a } T _ { \mathrm { { R } } } ^ { a }`$ , and a matrix-valued chiral superfield $`\Xi = \Xi ^ { a } T _ { \mathrm { { R } } } ^ { a }`$ , where $`a`$ is an adjoint group index. A chiral superfield $`\Phi`$ in the representation R still transforms according to eqs. (95.57)
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#c08300b99ba846e28130d785d81079fe">
		$$
		\begin{array} { l } { { \Phi e ^ { - 2 i g \Xi } \Phi ~ , } } \\{ { { } } } \\{ { \Phi ^ { \dag } \Phi ^ { \dag } e ^ { + 2 i g \Xi ^ { \dag } } ~ , } } \\{ { { } } } \\{ { V V + i ( \Xi ^ { \dag } - \Xi ) ~ . } } \end{array} \tag{95.57-95.59}
		$$
	</synced_block>
</callout>
and (95.58), but for the vector field we have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#d9ae13e484404260a2f7b7663023234d">
		$$
		\begin{array} { l } { { \Phi e ^ { - 2 i g \Xi } \Phi ~ , } } \\{ { { } } } \\{ { \Phi ^ { \dag } \Phi ^ { \dag } e ^ { + 2 i g \Xi ^ { \dag } } ~ , } } \\{ { { } } } \\{ { V V + i ( \Xi ^ { \dag } - \Xi ) ~ . } } \end{array} \tag{95.57-95.59}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#6b59292bb48540179315effa3f4c063c">
	$$
	e ^ { - 2 g V } \to e ^ { - 2 i g \Xi ^ { \dag } } e ^ { - 2 g V } e ^ { + 2 i g \Xi } ; \tag{95.78}
	$$
</synced_block>
this reduces to eq. (95.59) in the abelian case.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#34e72643a7b149c7826db27e1a0d2a1c">
		$$
		\begin{array} { l } { { \Phi e ^ { - 2 i g \Xi } \Phi ~ , } } \\{ { { } } } \\{ { \Phi ^ { \dag } \Phi ^ { \dag } e ^ { + 2 i g \Xi ^ { \dag } } ~ , } } \\{ { { } } } \\{ { V V + i ( \Xi ^ { \dag } - \Xi ) ~ . } } \end{array} \tag{95.57-95.59}
		$$
	</synced_block>
</callout>
The field-strength superfield is now
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#24ad5a60fe734a83b90a8c5238124508">
	$$
	\begin{array} { r } { W _ { a } = - \frac { 1 } { 8 g } { \mathcal D } _ { \dot { a } } ^ { * } { \mathcal D } ^ { * \dot { a } } e ^ { + 2 g V } { \mathcal D } _ { a } e ^ { - 2 g V } . } \end{array} \tag{95.79}
	$$
</synced_block>
Under a supergauge transformation,
<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#d9e9b182757d4755b44af6fe543d9b23">
	$$
	W _ { a } e ^ { - 2 i g \Xi } W _ { a } e ^ { + 2 i g \Xi } . \tag{95.80}
	$$
</synced_block>
Eq. (95.73) still holds, but the derivative that acts on $`\lambda ^ { \dagger }`$ is now the gauge covariant derivative for the adjoint representation, and $`F ^ { \mu \nu }`$ now includes the usual nonabelian commutator term. These changes also apply to eq. (95.77), where we must also trace over the group indices and (for proper normalization) divide by the index $`T ( \mathrm { R } )`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#e33a2bea6eff4c3a9859ecf483c2ae57">
		$$
		W _ { a } = \lambda _ { a } + \theta _ { a } D - ( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { } ^ { c } \theta _ { c } F _ { \mu \nu } + i \theta \theta \sigma _ { a \dot { a } } ^ { \mu } \partial _ { \mu } \lambda ^ { \dagger \dot { a } } \ . \tag{95.73}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#c1e3be1a60234be993c050b58590324b">
		$$
		\begin{array} { r } { \mathcal { L } _ { \mathrm { k i n } } = \frac { 1 } { 4 } W ^ { a } W _ { a } \Big | _ { F } + \mathrm { h . c . } ~ } \\{ = i \lambda ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \lambda - \frac { 1 } { 4 } F ^ { \mu \nu } F _ { \mu \nu } + \frac { 1 } { 2 } D ^ { 2 } . } \end{array} \tag{95.77}
		$$
	</synced_block>
</callout>
Reference notes
Introductions to supersymmetry can be found in Martin, Siegel, Weinberg III, and Wess & Bagger.
## Problems
### 95.1
Use eq. (95.6) to show that the hamiltonian is positive semidefinite, and that a state with zero energy must be annihilated by all the supercharges.
### 95.2
Supersymmetry is spontaneously broken if the ground state $`| 0 \rangle`$ is not annihilated by all the supercharges. a) Use the first of eqs. (95.34) to show that supersymmetry is spontaneously broken if $`\langle 0 | F | 0 \rangle \neq 0`$ . b) Compute $`\{ \lambda _ { a } , Q _ { b } \}`$ . Use the result to show that supersymmetry is spontaneously broken if $`\langle 0 | D | 0 \rangle \ne 0`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a#6af1706c805d469bb8364e131c286671">
		$$
		\begin{array} { c c c } { { { } [ A , Q _ { a } ] = - i \sqrt { 2 } \psi _ { a } ~ , ~ } } & { { { } } } & { { [ A , Q _ { \dot { a } } ^ { \dagger } ] = 0 ~ , } } \\{ { { } \{ \psi _ { c } , Q _ { a } \} = - i \sqrt { 2 } \varepsilon _ { a c } F ~ , ~ } } & { { { } } } & { { \{ \psi _ { c } , Q _ { \dot { a } } ^ { \dagger } \} = - \sqrt { 2 } \sigma _ { c \dot { a } } ^ { \mu } \partial _ { \mu } A ~ , } } \\{ { { } } } & { { { } } } & { { { { } [ F , Q _ { a } ] = 0 ~ , ~ } } } \end{array} \tag{95.33-95.35}
		$$
	</synced_block>
</callout>
### 95.3
Consider a supersymmetric theory with three chiral superfields $`A`$ , $`B`$ , and $`C`$ , and a superpotential $`W = m B C + \kappa A ( C ^ { 2 } - v ^ { 2 } )`$ , where $`m`$ and $`v`$ are parameters with dimensions of mass, and $`\kappa`$ is a dimensionless coupling constant. This is the $`O`$ ’Raifeartaigh model. a) Show that one or more $`F ^ { \prime }`$ components is nonzero at the minimum of the potential, and hence that supersymmetry is spontaneously broken. b) Show that the potential is minimized along a line in field space, and find the masses of the particles at an arbitrary point on this line. You should find that there is a massless Goldstone fermion or goldstino that is related by supersymmetry to the linear combination of $`F`$ fields that gets a nonzero vacuum expectation value.
### 95.4
Supersymmetric quantum electrodynamics. Consider a supersymmetric U(1) gauge theory with chiral superfields $`\Phi`$ and $`\overline { { \Phi } }`$ with charges $`+ 1`$ and $`^ { - 1 }`$ , respectively. Here the bar over the $`\Phi`$ in the field $`\overline { { \Phi } }`$ is part of the name of the field, and does not denote any sort of conjugation. We include a gauge-invariant superpotential $`W = m \overline { { \Phi } } \Phi`$ . a) Work out the lagrangian in terms of the component fields. b) Eliminate the auxiliary fields $`F ^ { \dagger }`$ , $`\overline { F }`$ , and $`D`$ .
### 95.5
In a supersymmetric gauge theory with a $`\mathrm { U } ( 1 )`$ factor, we can add a Fayet– Illiopoulos term $`\mathcal { L } _ { \mathrm { F I } } = e \xi D`$ to the lagrangian, where $`D`$ is the auxiliary field for the U(1) gauge field, and $`\xi`$ is a parameter with dimensions of mass-squared.
a) Explain why adding this term preserves supersymmetry. Explain why the corresponding gauge field cannot be nonabelian.<br>b) Add this term to the SQED lagrangian that you found in problem 94.4, and eliminate the auxiliary fields.<br>c) Minimize the resulting potential. Show that supersymmetry is spontaneously broken if $`\xi`$ is in a certain range.
### 95.6
$`R`$ symmetry. Given a supersymmetric gauge theory (abelian or nonabelian), consider a global $`\mathrm { U } ( 1 )`$ transformation that changes the phase of the gaugino fields, $`\lambda _ { a } \to e ^ { - \imath \alpha } \lambda _ { a }`$ ; we say that the gauginos have $`R`$ charge $`+ 1`$ .
a) If $`R`$ symmetry is to be a good symmetry of the lagrangian, what relation must hold between the $`R`$ charges of the scalar and fermion components of a chiral superfield that couples to the gauge fields? b) In addition, what conditions must be placed on the superpotential? c) Identify the $`R`$ symmetry, if any, of supersymmetric quantum electrodynamics.
</content>
</page>
