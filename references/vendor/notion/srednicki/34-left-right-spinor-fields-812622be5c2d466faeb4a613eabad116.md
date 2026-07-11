Here is the result of "view" for the Page with URL https://app.notion.com/p/812622be5c2d466faeb4a613eabad116 as of 2026-04-27T16:52:45.853Z:
<page url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"34. Left- and right-handed spinor fields"}
</properties>
<content>
Consider a left-handed spinor field $`\psi _ { a } ( x )`$ , also known as a left-handed Weyl field, which is in the $`( 2 , 1 )`$ representation of the Lie algebra of the Lorentz group. Here the index $`a`$ is a left-handed spinor index that takes on two possible values. Under a Lorentz transformation, we have
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#ea0be8ddf48346618894c5d4edac57aa">
	$$
	U ( \Lambda ) ^ { - 1 } \psi _ { a } ( x ) U ( \Lambda ) = L _ { a } { } ^ { b } ( \Lambda ) \psi _ { b } ( \Lambda ^ { - 1 } x ) , \tag{34.1}
	$$
</synced_block>
where $`{ { L } _ { a } } ^ { b } ( \Lambda )`$ is a matrix in the $`( 2 , 1 )`$ representation. These matrices satisfy the group composition rule
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#864687d798dc4abf9faa2a6a3b166e3d">
	$$
	L _ { a } { } ^ { b } ( \Lambda ^ { \prime } ) L _ { b } { } ^ { c } ( \Lambda ) = L _ { a } { } ^ { c } ( \Lambda ^ { \prime } \Lambda ) . \tag{34.2}
	$$
</synced_block>
For an infinitesimal transformation $`\Lambda ^ { \mu } { } _ { \nu } = \delta ^ { \mu } { } _ { \nu } + \delta \omega ^ { \mu } { } _ { \nu }`$ , we can write
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#bb52327b3b764071a79237c3aaba5591">
	$$
	L _ { a } { } ^ { b } ( 1 + \delta \omega ) = \delta _ { a } { } ^ { b } + { \textstyle { \frac { i } { 2 } } } \delta \omega _ { \mu \nu } ( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { } ^ { b } , \tag{34.3}
	$$
</synced_block>
where $`( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { } ^ { b } = - ( S _ { \mathrm { { L } } } ^ { \nu \mu } ) _ { a } { } ^ { b }`$ is a set of $`2 \times 2`$ matrices that obey the same commutation relations as the generators $`M ^ { \mu \nu }`$ , namely
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#f1bd0569673041598eb90398edbecb6d">
	$$
	[ S _ { \mathrm { { L } } } ^ { \mu \nu } , S _ { \mathrm { { L } } } ^ { \rho \sigma } ] = i { \Big ( } g ^ { \mu \rho } S _ { \mathrm { { L } } } ^ { \nu \sigma } - ( \mu { } \nu ) { \Big ) } - ( \rho { } \sigma ) ~ . \tag{34.4}
	$$
</synced_block>
Using
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#107628feffdc4ca2bb992398dcfbd252">
	$$
	\begin{array} { r } { U ( 1 + \delta \omega ) = I + \frac { i } { 2 } \delta \omega _ { \mu \nu } M ^ { \mu \nu } , } \end{array} \tag{34.5}
	$$
</synced_block>
eq. (34.1) becomes
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#5484bea766d14a7a91e2a53c8115090b">
		$$
		U ( \Lambda ) ^ { - 1 } \psi _ { a } ( x ) U ( \Lambda ) = L _ { a } { } ^ { b } ( \Lambda ) \psi _ { b } ( \Lambda ^ { - 1 } x ) , \tag{34.1}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#1c8d9b4483cd4198b48e3465b2bda81e">
	$$
	[ \psi _ { a } ( x ) , M ^ { \mu \nu } ] = { \mathcal L } ^ { \mu \nu } \psi _ { a } ( x ) + ( S _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } { } ^ { b } \psi _ { b } ( x ) , \tag{34.6}
	$$
</synced_block>
where $`{ \mathcal { L } } ^ { \mu \nu } = { \textstyle { \frac { 1 } { i } } } ( x ^ { \mu } \partial ^ { \nu } - x ^ { \nu } \partial ^ { \mu } )`$ . The $`{ \mathcal { L } } ^ { \mu \nu }`$ term in eq. (34.6) would also be present for a scalar field, and is not the focus of our current interest; we will suppress it by evaluating the fields at the space-time origin, $`x ^ { \mu } = 0`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#49ccd28e679c453780fa6d7cb291b713">
		$$
		[ \psi _ { a } ( x ) , M ^ { \mu \nu } ] = { \mathcal L } ^ { \mu \nu } \psi _ { a } ( x ) + ( S _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } { } ^ { b } \psi _ { b } ( x ) , \tag{34.6}
		$$
	</synced_block>
</callout>
Recalling that $`M ^ { i j } = \varepsilon ^ { i j k } J _ { k }`$ , where $`J _ { k }`$ is the angular momentum operator, we have
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#03e7987b875f49de9c24e390123c3895">
	$$
	\varepsilon ^ { i j k } [ \psi _ { a } ( 0 ) , J _ { k } ] = ( S _ { \mathrm { \scriptscriptstyle L } } ^ { i j } ) _ { a } ^ { b } \psi _ { b } ( 0 ) . \tag{34.7}
	$$
</synced_block>
Recall that the $`( 2 , 1 )`$ representation of the Lorentz group includes angular momentum $`\begin{array} { r } { j = \frac { 1 } { 2 } } \end{array}`$ only. For a spin-one-half operator, the standard convention is that the matrix on the right-hand side of eq. (34.7) is $`\textstyle { \frac { 1 } { 2 } } \varepsilon ^ { i j k } \sigma _ { k }`$ , where we have suppressed the row index $`a`$ and the column index $`b`$ , and where $`\sigma _ { k }`$ is a Pauli matrix:
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#ec8fe0bbcead4ace99d0143ca686c400">
		$$
		\varepsilon ^ { i j k } [ \psi _ { a } ( 0 ) , J _ { k } ] = ( S _ { \mathrm { \scriptscriptstyle L } } ^ { i j } ) _ { a } ^ { b } \psi _ { b } ( 0 ) . \tag{34.7}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#9dbc4062002a46488cd68a54d09e0c01">
	$$
	\sigma _ { 1 } = { \binom { 0 } { 1 } } \ 1 ) , \quad \sigma _ { 2 } = { \binom { 0 } { i } } \ - i \quad \sigma _ { 3 } = { \binom { 1 } { 0 } } \ \cdot \ 0 \ \cdot \tag{34.8}
	$$
</synced_block>
We therefore conclude that
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#b117132b8f3d40a7bb37bd5a91e428c8">
	$$
	( S _ { \mathrm { \scriptscriptstyle L } } ^ { i j } ) _ { a } ^ { b } = { \textstyle \frac { 1 } { 2 } } \varepsilon ^ { i j k } \sigma _ { k } ~ . \tag{34.9}
	$$
</synced_block>
Thus, for example, setting $`i { = } 1`$ and $`j { = } 2`$ yields $`( S _ { \mathrm { { L } } } ^ { 1 2 } ) _ { a } { } ^ { b } = \textstyle { \frac { 1 } { 2 } } \varepsilon ^ { 1 2 k } \sigma _ { k } = \textstyle { \frac { 1 } { 2 } } \sigma _ { 3 }`$ , and so $`\big ( S _ { \mathrm { L } } ^ { 1 2 } \big ) _ { 1 } { } ^ { 1 } = + \frac { 1 } { 2 }`$ , $`\begin{array} { r } { ( S _ { \mathrm { L } } ^ { 1 2 } ) _ { 2 } { } ^ { 2 } = - \frac { 1 } { 2 } } \end{array}`$ , and $`( S _ { \mathrm { { L } } } ^ { 1 2 } ) _ { 1 } { } ^ { 2 } = ( S _ { \mathrm { { L } } } ^ { 1 2 } ) _ { 2 } { } ^ { 1 } = 0`$ .
Once we have the $`( 2 , 1 )`$ representation matrices for the angular momentum operator $`J _ { i }`$ , we can easily get them for the boost operator $`K _ { k } = M ^ { k 0 }`$ . This is because $`J _ { k } = N _ { k } + N _ { k } ^ { \dagger }`$ and $`K _ { k } = i ( N _ { k } - N _ { k } ^ { \dagger } )`$ , and, acting on a field in the $`( 2 , 1 )`$ representation, $`N _ { k } ^ { \dagger }`$ is zero. Therefore, the representation matrices for $`K _ { k }`$ are simply $`i`$ times those for $`J _ { k }`$ , and so
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#5c03c357ee13455fac2c72a4fdbee539">
	$$
	( { S _ { \mathrm { \tiny { L } } } } ^ { k 0 } ) _ { a } { } ^ { b } = { \textstyle { \frac { 1 } { 2 } } } i \sigma _ { k } \ . \tag{34.10}
	$$
</synced_block>
Now consider taking the hermitian conjugate of the left-handed spinor field $`\psi _ { a } ( x )`$ . Recall that hermitian conjugation swaps the two SU(2) Lie algebras that comprise the Lie algebra of the Lorentz group. Therefore, the hermitian conjugate of a field in the $`( 2 , 1 )`$ representation should be a field in the $`( 1 , 2 )`$ representation; such a field is called a right-handed spinor field or a right-handed Weyl field. We will distinguish the indices of the $`( 1 , 2 )`$ representation from those of the $`( 2 , 1 )`$ representation by putting dots over them. Thus, we write
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#0260f9ad864b4845a8315da13b1f4316">
	$$
	[ \psi _ { a } ( x ) ] ^ { \dagger } = \psi _ { \dot { a } } ^ { \dagger } ( x ) . \tag{34.11}
	$$
</synced_block>
Under a Lorentz transformation, we have
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#66cdeea494284550bce1114fbaf0abd4">
	$$
	U ( \Lambda ) ^ { - 1 } \psi _ { \dot { a } } ^ { \dagger } ( x ) U ( \Lambda ) = R _ { \dot { a } } { } ^ { \dot { b } } ( \Lambda ) \psi _ { \dot { b } } ^ { \dagger } ( \Lambda ^ { - 1 } x ) , \tag{34.12}
	$$
</synced_block>
where $`{ R _ { \dot { a } } } ^ { b } ( \Lambda )`$ is a matrix in the $`( 1 , 2 )`$ representation. These matrices satisfy the group composition rule
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#8a63bfe739f545d787b79bfdf22c05ae">
	$$
	R _ { \dot { a } } { } ^ { \dot { b } } ( \Lambda ^ { \prime } ) R _ { \dot { b } } { } ^ { \dot { c } } ( \Lambda ) = R _ { \dot { a } } { } ^ { \dot { c } } ( \Lambda ^ { \prime } \Lambda ) \ . \tag{34.13}
	$$
</synced_block>
For an infinitesimal transformation $`\Lambda ^ { \mu } { } _ { \nu } = \delta ^ { \mu } { } _ { \nu } + \delta \omega ^ { \mu } { } _ { \nu }`$ , we can write
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#f9e070cfa09047eeaa189191c509ff41">
	$$
	\begin{array} { r } { R _ { \dot { a } } ^ { \dot { b } } ( 1 + \delta \omega ) = \delta _ { \dot { a } } { } ^ { \dot { b } } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S _ { \mathrm { { R } } } ^ { \mu \nu } ) _ { \dot { a } } { } ^ { \dot { b } } \ , } \end{array} \tag{34.14}
	$$
</synced_block>
where $`( S _ { \mathrm { { R } } } ^ { \mu \nu } ) _ { \dot { a } } { } ^ { \dot { b } } = - ( S _ { \mathrm { { R } } } ^ { \nu \mu } ) _ { \dot { a } } { } ^ { \dot { b } }`$ is a set of $`2 \times 2`$ matrices that obey the same commutation relations as the generators $`M ^ { \mu \nu }`$ . We then have
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#1bb0fd45215c49ea8fadc77e66386203">
	$$
	[ \psi _ { \dot { a } } ^ { \dagger } ( 0 ) , M ^ { \mu \nu } ] = ( S _ { \mathrm { \scriptscriptstyle R } } ^ { \mu \nu } ) _ { \dot { a } } { } ^ { \dot { b } } \psi _ { \dot { b } } ^ { \dagger } ( 0 ) . \tag{34.15}
	$$
</synced_block>
Taking the hermitian conjugate of this equation, we get
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#041627ef3d72414ca2fffd7e9a50b163">
	$$
	[ M ^ { \mu \nu } , \psi _ { a } ( 0 ) ] = [ ( S _ { \mathrm { R } } ^ { \mu \nu } ) _ { \dot { a } } { } ^ { \dot { b } } ] ^ { * } \psi _ { b } ( 0 ) . \tag{34.16}
	$$
</synced_block>
Comparing this with eq. (34.6), we see that
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#5e87da6168f64d3694894f71ac6e0bc5">
		$$
		[ \psi _ { a } ( x ) , M ^ { \mu \nu } ] = { \mathcal L } ^ { \mu \nu } \psi _ { a } ( x ) + ( S _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } { } ^ { b } \psi _ { b } ( x ) , \tag{34.6}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#9562c6dc3bf84cfba28e0085f86ba2c8">
	$$
	( S _ { \mathrm { \scriptscriptstyle R } } ^ { \mu \nu } ) _ { \dot { a } } ^ { \dot { b } } = - [ ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) _ { a } ^ { \ b } ] ^ { * } \ . \tag{34.17}
	$$
</synced_block>
In the previous section, we examined the Lorentz-transformation properties of a field carrying two vector indices. To help us get better acquainted with the properties of spinor indices, let us now do the same for a field that carries two $`( 2 , 1 )`$ indices. Call this field $`C _ { a b } ( x )`$ . Under a Lorentz transformation, we have
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#25e6717308264aa0b9e7efbf408127d2">
	$$
	U ( \Lambda ) ^ { - 1 } C _ { a b } ( x ) U ( \Lambda ) = L _ { a } { } ^ { c } ( \Lambda ) L _ { b } { } ^ { d } ( \Lambda ) C _ { c d } ( \Lambda ^ { - 1 } x ) . \tag{34.18}
	$$
</synced_block>
The question we wish to address is whether or not the four components of $`C _ { a b }`$ can be grouped into smaller sets that do not mix with each other under Lorentz transformations.
To answer this question, recall from quantum mechanics that two spinone-half particles can be in a state of total spin zero, or total spin one. Furthermore, the single spin-zero state is the unique antisymmetric combination of the two spin-one-half states, and the three spin-one states are the three symmetric combinations of the two spin-one-half states. We can write this schematically as $`2 \otimes 2 = 1 _ { \mathrm { A } } \oplus 3 _ { \mathrm { S } }`$ , where we label the representation of $`{ \mathrm { S U } } ( 2 )`$ by the number of its components, and the subscripts S and A indicate whether that representation appears in the symmetric or antisymmetric combination of the two 2s. For the Lorentz group, the relevant relation is $`( 2 , 1 ) \otimes ( 2 , 1 ) = ( 1 , 1 ) _ { \mathrm { A } } \oplus ( 3 , 1 ) _ { \mathrm { S } }`$ . This implies that we should be
able to write
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#c7c63ee24b364e15b2031b627536f2bb">
	$$
	C _ { a b } ( x ) = \varepsilon _ { a b } D ( x ) + G _ { a b } ( x ) , \tag{34.19}
	$$
</synced_block>
where $`D ( x )`$ is a scalar field, $`\varepsilon _ { a b } = - \varepsilon _ { b a }`$ is an antisymmetric set of constants, and $`G _ { a b } ( x ) = G _ { b a } ( x )`$ . The symbol $`\varepsilon _ { a b }`$ is uniquely determined by its symmetry properties up to an overall constant; we will choose $`\varepsilon _ { 2 1 } = - \varepsilon _ { 1 2 } = + 1`$ .
Since $`D ( x )`$ is a Lorentz scalar, eq. (34.19) is consistent with eq. (34.18) only if
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#5733e46882584ba5834a535a2f69cb87">
		$$
		C _ { a b } ( x ) = \varepsilon _ { a b } D ( x ) + G _ { a b } ( x ) , \tag{34.19}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#b6150c6ce53743998d5c3eb256b587bb">
		$$
		U ( \Lambda ) ^ { - 1 } C _ { a b } ( x ) U ( \Lambda ) = L _ { a } { } ^ { c } ( \Lambda ) L _ { b } { } ^ { d } ( \Lambda ) C _ { c d } ( \Lambda ^ { - 1 } x ) . \tag{34.18}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#59008e301469467a9e157dc7ab9ed41a">
	$$
	{ \cal L } _ { a } ^ { c } ( \Lambda ) { \cal L } _ { b } ^ { d } ( \Lambda ) \varepsilon _ { c d } = \varepsilon _ { a b } . \tag{34.18, 34.20}
	$$
</synced_block>
This means that $`\varepsilon _ { a b }`$ is an invariant symbol of the Lorentz group: it does not change under a Lorentz transformation that acts on all of its indices. In this way, $`\varepsilon _ { a b }`$ is analogous to the metric $`g _ { \mu \nu }`$ , which is also an invariant symbol, since
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#1fb18eb6e643412cb7d701311c08013c">
	$$
	\Lambda _ { \mu } { } ^ { \rho } \Lambda _ { \nu } { } ^ { \sigma } g _ { \rho \sigma } = g _ { \mu \nu } \ . \tag{34.21}
	$$
</synced_block>
We use $`g _ { \mu \nu }`$ and its inverse $`g ^ { \mu \nu }`$ to raise and lower vector indices, and we can use $`\varepsilon _ { a b }`$ and and its inverse $`\varepsilon ^ { a b }`$ to raise and lower left-handed spinor indices. Here we define $`\varepsilon ^ { a b }`$ via
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#2101d8c698004f1baaf72f8e9394d1e4">
	$$
	\varepsilon ^ { 1 2 } = \varepsilon _ { 2 1 } = + 1 , \qquad \varepsilon ^ { 2 1 } = \varepsilon _ { 1 2 } = - 1 . \tag{34.22}
	$$
</synced_block>
With this definition, we have
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#c960ed40268d4a81a61e8d51668b94fb">
	$$
	\varepsilon _ { a b } \varepsilon ^ { b c } = \delta _ { a } { } ^ { c } \ , \qquad \varepsilon ^ { a b } \varepsilon _ { b c } = \delta _ { \ c } ^ { a } \ . \tag{34.23}
	$$
</synced_block>
We can then define
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#8acf2138d6ab48d0967e8e4954aeff65">
	$$
	\psi ^ { a } ( x ) \equiv \varepsilon ^ { a b } \psi _ { b } ( x ) . \tag{34.24}
	$$
</synced_block>
We also have (suppressing the space-time argument of the field)
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#ddc87ee258024f74a7903f39a1eb7cc8">
	$$
	\psi _ { a } = \varepsilon _ { a b } \psi ^ { b } = \varepsilon _ { a b } \varepsilon ^ { b c } \psi _ { c } = \delta _ { a } { } ^ { c } \psi _ { c } , \tag{34.25}
	$$
</synced_block>
as we would expect. However, the antisymmetry of $`\varepsilon ^ { a b }`$ means that we must be careful with minus signs; for example, eq. (34.24) can be written in various ways, such as
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#a768fb98acb2486b8668b97f1bfddd41">
		$$
		\psi ^ { a } ( x ) \equiv \varepsilon ^ { a b } \psi _ { b } ( x ) . \tag{34.24}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#2c0aa42ad96542a4b597cb7e7260f63d">
	$$
	\psi ^ { a } = \varepsilon ^ { a b } \psi _ { b } = - \varepsilon ^ { b a } \psi _ { b } = - \psi _ { b } \varepsilon ^ { b a } = \psi _ { b } \varepsilon ^ { a b } . \tag{34.26}
	$$
</synced_block>
We must also be careful about signs when we contract indices, since
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#9a938a6cbdd94ac58448b160ca22141e">
	$$
	\psi ^ { a } \chi _ { a } = \varepsilon ^ { a b } \psi _ { b } \chi _ { a } = - \varepsilon ^ { b a } \psi _ { b } \chi _ { a } = - \psi _ { b } \chi ^ { b } . \tag{34.27}
	$$
</synced_block>
In section 35, we will (mercifully) develop an index-free notation that automatically keeps track of these essential (but annoying) minus signs.
An exactly analogous discussion applies to the second $`{ \mathrm { S U } } ( 2 )`$ factor; from the group-theoretic relation $`( 1 , 2 ) \otimes ( 1 , 2 ) = ( 1 , 1 ) _ { \mathrm { A } } \oplus ( 1 , 3 ) _ { \mathrm { S } }`$ , we can deduce the existence of an invariant symbol $`\varepsilon _ { \dot { a } \dot { b } } = - \varepsilon _ { \dot { b } \dot { a } }`$ . We will normalize $`\varepsilon ^ { \dot { a } \dot { b } }`$ according to eq. (34.22). Then eqs. (34.23)–(34.27) hold if all the undotted indices are replaced by dotted indices.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#d33c920083014adf8224e1135ec6d3c7">
		$$
		\varepsilon ^ { 1 2 } = \varepsilon _ { 2 1 } = + 1 , \qquad \varepsilon ^ { 2 1 } = \varepsilon _ { 1 2 } = - 1 . \tag{34.22}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#013db345095a40adbd0f2e77c232a620">
		$$
		\varepsilon _ { a b } \varepsilon ^ { b c } = \delta _ { a } { } ^ { c } \ , \qquad \varepsilon ^ { a b } \varepsilon _ { b c } = \delta _ { \ c } ^ { a } \ . \tag{34.23}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#02a2cfa2ad274f719f20106b640fc8cc">
		$$
		\psi ^ { a } \chi _ { a } = \varepsilon ^ { a b } \psi _ { b } \chi _ { a } = - \varepsilon ^ { b a } \psi _ { b } \chi _ { a } = - \psi _ { b } \chi ^ { b } . \tag{34.27}
		$$
	</synced_block>
</callout>
Now consider a field carrying one undotted and one dotted index, $`A _ { a \dot { a } } ( x )`$ . Such a field is in the $`( 2 , 2 )`$ representation, and in section 33 we concluded that the $`( 2 , 2 )`$ representation was the vector representation. We would more naturally write a field in the vector representation as $`A ^ { \mu } ( x )`$ . There must, then, be a dictionary that gives us the components of $`A _ { a \dot { a } } ( x )`$ in terms of the components of $`A ^ { \mu } ( x )`$ ; we can write this as
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#02a7495b359b45738ce3e7b0450d39ef">
	$$
	A _ { a \dot { a } } ( x ) = \sigma _ { a \dot { a } } ^ { \mu } A _ { \mu } ( x ) , \tag{34.28}
	$$
</synced_block>
where $`\sigma _ { a \dot { a } } ^ { \mu }`$ is another invariant symbol. That such a symbol must exist can be deduced from the group-theoretic relation
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#6b168e87e53d4a7892935f09e2af91a7">
	$$
	( 2 , 1 ) \otimes ( 1 , 2 ) \otimes ( 2 , 2 ) = ( 1 , 1 ) \oplus \ldots . \tag{34.29}
	$$
</synced_block>
As we will see in section 35, it turns out to be consistent with our already established conventions for $`S _ { \mathrm { { L } } } ^ { \mu \nu }`$ and $`S _ { \mathrm { { R } } } ^ { \mu \nu }`$ to choose
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#4cd6cd14df914a3f95f06cb7765eaddd">
	$$
	\sigma _ { a \dot { a } } ^ { \mu } = \left( I , \vec { \sigma } \right) . \tag{34.30}
	$$
</synced_block>
Thus, for example, $`\sigma _ { \mathrm { 1 i } } ^ { 3 } = + 1`$ , σ 322˙ $`\sigma _ { 2 \dot { 2 } } ^ { 3 } = - 1`$ , σ3 $`\sigma _ { 1 \dot { 2 } } ^ { 3 } = \sigma _ { 2 \dot { 1 } } ^ { 3 } = 0`$ = σ 321˙
In general, whenever the product of a set of representations includes the singlet, there is a corresponding invariant symbol. For example, we can deduce the existence of $`g _ { \mu \nu } = g _ { \nu \mu }`$ from
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#16f8c369315c4ba79dbe96873a474d77">
	$$
	( 2 , 2 ) \otimes ( 2 , 2 ) = ( 1 , 1 ) _ { \mathrm { S } } \oplus ( 1 , 3 ) _ { \mathrm { A } } \oplus ( 3 , 1 ) _ { \mathrm { A } } \oplus ( 3 , 3 ) _ { \mathrm { S } } . \tag{34.31}
	$$
</synced_block>
Another invariant symbol, the Levi-Cevita symbol, follows from
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#86750919145d42b79b130f81bbf8c4ce">
	$$
	( 2 , 2 ) \otimes ( 2 , 2 ) \otimes ( 2 , 2 ) \otimes ( 2 , 2 ) = ( 1 , 1 ) _ { \mathrm { A } } \oplus \ldots , \tag{34.32}
	$$
</synced_block>
where the subscript A denotes the completely antisymmetric part. The LeviCivita symbol is $`\varepsilon ^ { \mu \nu \rho \sigma }`$ , which is antisymmetric on exchange of any pair of its indices, and is normalized via $`\varepsilon ^ { 0 1 2 3 } = + 1`$ . To see that $`\varepsilon ^ { \mu \nu \rho \sigma }`$ is invariant, we note that $`\Lambda ^ { \mu } { } _ { \alpha } \Lambda ^ { \nu } { } _ { \beta } \Lambda ^ { \rho } { } _ { \gamma } \Lambda ^ { \sigma } { } _ { \delta } \varepsilon ^ { \alpha \beta \gamma \delta }`$ is antisymmetric on exchange of any two of its uncontracted indices, and therefore must be proportional to $`\varepsilon ^ { \mu \nu \rho \sigma }`$ . The constant of proportionality works out to be $`\operatorname* { d e t } \Lambda`$ , which is $`+ 1`$ for a proper Lorentz transformation.
We are finally ready to answer a question we posed at the beginning of section 33. There we considered a field $`B ^ { \mu \nu } ( x )`$ carrying two vector indices,
and we decomposed it as
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#f95afdaf381c40cbbaace23d3a9fb6e4">
	$$
	B ^ { \mu \nu } ( x ) = A ^ { \mu \nu } ( x ) + S ^ { \mu \nu } ( x ) + \textstyle { \frac { 1 } { 4 } } g ^ { \mu \nu } T ( x ) , \tag{34.33}
	$$
</synced_block>
where $`A ^ { \mu \nu }`$ is antisymmetric ( $`A ^ { \mu \nu } = - A ^ { \nu \mu }`$ ) and $`S ^ { \mu \nu }`$ is symmetric ( $`S ^ { \mu \nu } =`$ $`S ^ { \nu \mu }`$ ) and traceless ( $`g _ { \mu \nu } S ^ { \mu \nu } = 0`$ ). We asked whether further decomposition into still smaller irreducible representations was possible. The answer to this question can be found in eq. (34.31). Obviously, $`T ( x )`$ corresponds to $`( 1 , 1 )`$ , and $`S ^ { \mu \nu } ( x )`$ to $`( 3 , 3 )`$ .1 But, according to eq. (34.31), the antisymmetric field $`A ^ { \mu \nu } ( x )`$ should correspond to $`( 3 , 1 ) \oplus ( 1 , 3 )`$ . A field in the $`( 3 , 1 )`$ representation carries a symmetric pair of left-handed (undotted) spinor indices; its hermitian conjugate is a field in the $`( 1 , 3 )`$ representation that carries a symmetric pair of right-handed (dotted) spinor indices. We should, then, be able to find a mapping, analogous to eq. (34.28), that gives $`A ^ { \mu \nu } ( x )`$ in terms of a field $`G _ { a b } ( x )`$ and its hermitian conjugate $`G _ { \dot { a } \dot { b } } ^ { \dagger } ( x )`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#096373f21a9149dc9e9720ae94351555">
		$$
		( 2 , 2 ) \otimes ( 2 , 2 ) = ( 1 , 1 ) _ { \mathrm { S } } \oplus ( 1 , 3 ) _ { \mathrm { A } } \oplus ( 3 , 1 ) _ { \mathrm { A } } \oplus ( 3 , 3 ) _ { \mathrm { S } } . \tag{34.31}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#5b0b16cd02b54e139c48365d405c88ac">
		$$
		A _ { a \dot { a } } ( x ) = \sigma _ { a \dot { a } } ^ { \mu } A _ { \mu } ( x ) , \tag{34.28}
		$$
	</synced_block>
</callout>
This mapping is provided by the generator matrices $`S _ { \mathrm { { L } } } ^ { \mu \nu }`$ and $`S _ { \mathrm { { R } } } ^ { \mu \nu }`$ . We first note that the Pauli matrices are traceless, and so eqs. (34.9) and (34.10) imply that $`( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { } ^ { a } = 0`$ . Using eq. (34.24), we can rewrite this as $`\varepsilon ^ { a b } ( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a b } = 0`$ . Since $`\varepsilon ^ { a b }`$ is antisymmetric, $`( S _ { \mathrm { L } } ^ { \mu \nu } ) _ { a b }`$ must be symmetric on exchange of its two spinor indices. An identical argument shows that $`( S _ { \mathrm { R } } ^ { \mu \nu } ) _ { \dot { a } \dot { b } }`$ must be symmetric on exchange of its two spinor indices. Furthermore, according to eqs. (34.9) and (34.10), we have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#3af7473de2924fa6a5940f71f0c21a8d">
		$$
		( S _ { \mathrm { \scriptscriptstyle L } } ^ { i j } ) _ { a } ^ { b } = { \textstyle \frac { 1 } { 2 } } \varepsilon ^ { i j k } \sigma _ { k } ~ . \tag{34.9}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#4759822c23204b46837b4905dc482437">
		$$
		( { S _ { \mathrm { \tiny { L } } } } ^ { k 0 } ) _ { a } { } ^ { b } = { \textstyle { \frac { 1 } { 2 } } } i \sigma _ { k } \ . \tag{34.10}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#a276e2dc270b4e54b64491d04599f7f7">
		$$
		\psi ^ { a } ( x ) \equiv \varepsilon ^ { a b } \psi _ { b } ( x ) . \tag{34.24}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#a5c3e4241ee748c4bdcf812bcb9e72db">
	$$
	( S _ { \mathrm { \scriptscriptstyle L } } ^ { 1 0 } ) _ { a } { } ^ { b } = - i ( S _ { \mathrm { \scriptscriptstyle L } } ^ { 2 3 } ) _ { a } { } ^ { b } . \tag{34.34}
	$$
</synced_block>
This can be written covariantly with the Levi-Cevita symbol as
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#f29ffd41e3ea42239d561688ebb8c538">
	$$
	( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) _ { a } { } ^ { b } = - { \textstyle \frac { i } { 2 } } \varepsilon ^ { \mu \nu \rho \sigma } ( S _ { \mathrm { \scriptscriptstyle L } \rho \sigma } ) _ { a } { } ^ { b } \ . \tag{34.35}
	$$
</synced_block>
Similarly,
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#2ed021fd2b74450eab3bcc0746f2595d">
	$$
	( S _ { \mathrm { \tiny ~ R } } ^ { \mu \nu } ) _ { \dot { a } } { } ^ { \dot { b } } = + { \textstyle \frac { i } { 2 } } \varepsilon ^ { \mu \nu \rho \sigma } ( S _ { \mathrm { \tiny ~ R } \rho \sigma } ) _ { \dot { a } } { } ^ { \dot { b } } \ . \tag{34.36, 34.35}
	$$
</synced_block>
Eq. (34.36) follows from taking the complex conjugate of eq. (34.35) and using eq. (34.17).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#70721bbd07e14019abfe7937d25bd575">
		$$
		( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) _ { a } { } ^ { b } = - { \textstyle \frac { i } { 2 } } \varepsilon ^ { \mu \nu \rho \sigma } ( S _ { \mathrm { \scriptscriptstyle L } \rho \sigma } ) _ { a } { } ^ { b } \ . \tag{34.35}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#cdd8f269be714f87b93c3e691fc34a15">
		$$
		( S _ { \mathrm { \scriptscriptstyle R } } ^ { \mu \nu } ) _ { \dot { a } } ^ { \dot { b } } = - [ ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) _ { a } ^ { \ b } ] ^ { * } \ . \tag{34.17}
		$$
	</synced_block>
</callout>
Now, given a field $`G _ { a b } ( x )`$ in the $`( 3 , 1 )`$ representation, we can map it into a self-dual antisymmetric tensor $`G ^ { \mu \nu } ( x )`$ via
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#e3b050d581194fd49000f934fba1fba7">
	$$
	G ^ { \mu \nu } ( x ) \equiv ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) ^ { a b } G _ { a b } ( x ) . \tag{34.37}
	$$
</synced_block>
By self-dual, we mean that $`G ^ { \mu \nu } ( x )`$ obeys
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#32cd1fc8a94d4c0f91ccbd299f8c4eec">
	$$
	\begin{array} { r } { G ^ { \mu \nu } ( x ) = - \frac { i } { 2 } \varepsilon ^ { \mu \nu \rho \sigma } G _ { \rho \sigma } ( x ) . } \end{array} \tag{34.38}
	$$
</synced_block>
Taking the hermitian conjugate of eq. (34.37), and using eq. (34.17), we get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#03efc081e2184e5bb2e4e83739bc3878">
		$$
		G ^ { \mu \nu } ( x ) \equiv ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) ^ { a b } G _ { a b } ( x ) . \tag{34.37}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#dd8cfc212d8a49e88ed256d1dc8df9dd">
		$$
		( S _ { \mathrm { \scriptscriptstyle R } } ^ { \mu \nu } ) _ { \dot { a } } ^ { \dot { b } } = - [ ( S _ { \mathrm { \scriptscriptstyle L } } ^ { \mu \nu } ) _ { a } ^ { \ b } ] ^ { * } \ . \tag{34.17}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#c55a1cd8ad794085b85485f7ffc95e6a">
	$$
	G ^ { \dagger \mu \nu } ( x ) = - ( S _ { \mathrm { \scriptscriptstyle R } } ^ { \mu \nu } ) ^ { { \dot { a } } { \dot { b } } } G _ { { \dot { a } } { \dot { b } } } ^ { \dagger } ( x ) , \tag{34.39}
	$$
</synced_block>
which is anti-self-dual,
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#d892f133079d418dbe52bdcfdf61e09d">
	$$
	G ^ { \dagger \mu \nu } ( x ) = + { \textstyle \frac { i } { 2 } } \varepsilon ^ { \mu \nu \rho \sigma } G _ { \rho \sigma } ^ { \dagger } ( x ) . \tag{34.40}
	$$
</synced_block>
Given a hermitian antisymmetric tensor field $`A ^ { \mu \nu } ( x )`$ , we can extract its self-dual and anti-self-dual parts via
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#856d3b8a69764f048dc4c31c08abf022">
	$$
	\begin{array} { r } { G ^ { \mu \nu } ( x ) = \frac { 1 } { 2 } A ^ { \mu \nu } ( x ) - \frac { i } { 4 } \varepsilon ^ { \mu \nu \rho \sigma } A _ { \rho \sigma } ( x ) , } \\{ G ^ { \dag \mu \nu } ( x ) = \frac { 1 } { 2 } A ^ { \mu \nu } ( x ) + \frac { i } { 4 } \varepsilon ^ { \mu \nu \rho \sigma } A _ { \rho \sigma } ( x ) . } \end{array} \tag{34.41-34.42}
	$$
</synced_block>
Then we have
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#22b8f9e6db4b42a6bc7301d6eda63364">
	$$
	A ^ { \mu \nu } ( x ) = G ^ { \mu \nu } ( x ) + G ^ { \dag \mu \nu } ( x ) . \tag{34.43}
	$$
</synced_block>
The field $`G ^ { \mu \nu } ( x )`$ is in the $`( 3 , 1 )`$ representation, and the field $`G ^ { \dagger \mu \nu } ( x )`$ is in the $`( 1 , 3 )`$ representation; these do not mix under Lorentz transformations.
## Problems
### 34.1
Verify that eq. (34.6) follows from eq. (34.1).
### 34.2
Verify that eqs. (34.9) and (34.10) obey eq. (34.4).
### 34.3
Show that the Levi-Cevita symbol obeys
<synced_block url="https://app.notion.com/p/812622be5c2d466faeb4a613eabad116#94abef8bb8544a6bbf79e836d84f1152">
	$$
	\begin{array} { r l } & { \varepsilon ^ { \mu \nu \rho \sigma } \varepsilon _ { \alpha \beta \gamma \sigma } = - \delta ^ { \mu } { } _ { \alpha } \delta ^ { \nu } { } _ { \beta } \delta ^ { \rho } { } _ { \gamma } - \delta ^ { \mu } { } _ { \beta } \delta ^ { \nu } { } _ { \gamma } \delta ^ { \rho } { } _ { \alpha } - \delta ^ { \mu } { } _ { \gamma } \delta ^ { \nu } { } _ { \alpha } \delta ^ { \rho } { } _ { \beta } } \\& { \phantom { \varepsilon ^ { \mu \nu \rho \sigma } } + \delta ^ { \mu } { } _ { \beta } \delta ^ { \nu } { } _ { \alpha } \delta ^ { \rho } { } _ { \gamma } + \delta ^ { \mu } { } _ { \alpha } \delta ^ { \nu } { } _ { \gamma } \delta ^ { \rho } { } _ { \beta } + \delta ^ { \mu } { } _ { \gamma } \delta ^ { \nu } { } _ { \beta } \delta ^ { \rho } { } _ { \alpha } \ : , } \\& { \varepsilon ^ { \mu \nu \rho \sigma } \varepsilon _ { \alpha \beta \rho \sigma } = - 2 ( \delta ^ { \mu } { } _ { \alpha } \delta ^ { \nu } { } _ { \beta } - \delta ^ { \mu } { } _ { \beta } \delta ^ { \nu } { } _ { \alpha } ) \ : , } \\& { \varepsilon ^ { \mu \nu \rho \sigma } \varepsilon _ { \alpha \nu \rho \sigma } = - 6 \delta ^ { \mu } { } _ { \alpha } \ : . } \end{array} \tag{34.44-34.46}
	$$
</synced_block>
### 34.4
Consider a field $`C ^ { a . . . c \dot { a } . . . \dot { c } } ( x )`$ , with $`N`$ undotted indices and $`M`$ dotted indices, that is furthermore symmetric on exchange of any pair of undotted indices, and also symmetric on exchange of any pair of dotted indices. Show that this field corresponds to a single irreducible representation $`( 2 n \mathrm { + } 1 , 2 n ^ { \prime } \mathrm { + } 1 )`$ of the Lorentz group, and identify $`n`$ and $`n ^ { \prime }`$ .
</content>
</page>
