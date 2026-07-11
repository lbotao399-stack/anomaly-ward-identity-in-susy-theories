Here is the result of "view" for the Page with URL https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8 as of 2026-04-27T17:30:23.141Z:
<page url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"33. Representations of the Lorentz group"}
</properties>
<content>
In section 2, we saw that we could define a unitary operator $`U ( \Lambda )`$ that implemented a Lorentz transformation on a scalar field $`\varphi ( x )`$ via
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#9d432d1c9ca548f2acd3792d6f4842e5">
	$$
	U ( \Lambda ) ^ { - 1 } \varphi ( x ) U ( \Lambda ) = \varphi ( \Lambda ^ { - 1 } x ) . \tag{33.1}
	$$
</synced_block>
As shown in section 2, this implies that the derivative of the field transforms as
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#45c1a8bb14fd43d599f463ad1ef698b7">
	$$
	U ( \Lambda ) ^ { - 1 } \partial ^ { \mu } \varphi ( x ) U ( \Lambda ) = { \Lambda ^ { \mu } } _ { \rho } \bar { \partial } ^ { \rho } \varphi ( \Lambda ^ { - 1 } x ) , \tag{33.2}
	$$
</synced_block>
where the bar on the derivative means that it is with respect to the argument $`\bar { x } = \Lambda ^ { - 1 } x`$ .
Eq. (33.2) suggests that we could define a vector field $`A ^ { \mu } ( x )`$ that would transform as
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#04950eef5dfa4297896fdb1a2ddc6cad">
		$$
		U ( \Lambda ) ^ { - 1 } \partial ^ { \mu } \varphi ( x ) U ( \Lambda ) = { \Lambda ^ { \mu } } _ { \rho } \bar { \partial } ^ { \rho } \varphi ( \Lambda ^ { - 1 } x ) , \tag{33.2}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#634a2873a2824a19bea0538c3eae9164">
	$$
	U ( \Lambda ) ^ { - 1 } A ^ { \rho } ( x ) U ( \Lambda ) = { \Lambda ^ { \mu } } _ { \rho } A ^ { \rho } ( \Lambda ^ { - 1 } x ) , \tag{33.3}
	$$
</synced_block>
or a tensor field $`B ^ { \mu \nu } ( x )`$ that would transform as
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#856762d80fbc4f2182861e8b9dd9c554">
	$$
	U ( \Lambda ) ^ { - 1 } B ^ { \mu \nu } ( x ) U ( \Lambda ) = { \Lambda ^ { \mu } } _ { \rho } { \Lambda ^ { \nu } } _ { \sigma } B ^ { \rho \sigma } ( \Lambda ^ { - 1 } x ) . \tag{33.4}
	$$
</synced_block>
Note that if $`B ^ { \mu \nu }`$ is either symmetric, $`B ^ { \mu \nu } ( x ) = B ^ { \nu \mu } ( x )`$ , or antisymmetric, $`B ^ { \mu \nu } ( x ) = - B ^ { \nu \mu } ( x )`$ , then the symmetry is preserved by the Lorentz transformation. Also, if we take the trace to get $`T ( x ) \equiv g _ { \mu \nu } B ^ { \mu \nu } ( x )`$ , then, using $`g _ { \mu \nu } \Lambda ^ { \mu } { } _ { \rho } \Lambda ^ { \nu } { } _ { \sigma } = g _ { \rho \sigma }`$ , we find that $`T ( x )`$ transforms like a scalar field,
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#b819da2759e54c05b098860b939f26ba">
	$$
	U ( \Lambda ) ^ { - 1 } T ( x ) U ( \Lambda ) = T ( \Lambda ^ { - 1 } x ) . \tag{33.5}
	$$
</synced_block>
Thus, given a tensor field $`B ^ { \mu \nu } ( x )`$ with no particular symmetry, we can write
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#a7cbca4bf1a94227abc943e0a5a82a87">
	$$
	B ^ { \mu \nu } ( x ) = A ^ { \mu \nu } ( x ) + S ^ { \mu \nu } ( x ) + \textstyle { \frac { 1 } { 4 } } g ^ { \mu \nu } T ( x ) , \tag{33.6}
	$$
</synced_block>
where $`A ^ { \mu \nu }`$ is antisymmetric ( $`A ^ { \mu \nu } = - A ^ { \nu \mu }`$ ) and $`S ^ { \mu \nu }`$ is symmetric ( $`S ^ { \mu \nu } =`$ $`S ^ { \nu \mu }`$ ) and traceless ( $`g _ { \mu \nu } S ^ { \mu \nu } = 0`$ ). The key point is that the fields $`A ^ { \mu \nu }`$ , $`S ^ { \mu \nu }`$ , and $`T`$ do not mix with each other under Lorentz transformations.
Is it possible to further break apart these fields into still smaller sets that do not mix under Lorentz transformations? How do we make this decomposition into irreducible representations of the Lorentz group for a field carrying $`n`$ vector indices? Are there any other kinds of indices we could consistently assign to a field? If so, how do these behave under a Lorentz transformation?
The answers to these questions are to be found in the theory of group representations. Let us see how this works for the Lorentz group (in four space-time dimensions).
Consider a field (not necessarily hermitian) that carries a generic Lorentz index, $`\varphi _ { A } ( x )`$ . Under a Lorentz transformation, we have
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#6d73e1bbd9cb46ffa70ff1917f9ca4d6">
	$$
	U ( \Lambda ) ^ { - 1 } \varphi _ { A } ( x ) U ( \Lambda ) = L _ { A } { } ^ { B } ( \Lambda ) \varphi _ { B } ( \Lambda ^ { - 1 } x ) , \tag{33.7}
	$$
</synced_block>
where $`{ L _ { A } } ^ { B } ( \Lambda )`$ is a matrix that depends on $`\Lambda`$ . These finite-dimensional matrices must obey the group composition rule
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#7e045202c2a0404ba0e3016e0510fbd3">
	$$
	{ \cal L } _ { A } { } ^ { B } ( \Lambda ^ { \prime } ) { \cal L } _ { B } { } ^ { C } ( \Lambda ) = { \cal L } _ { A } { } ^ { C } ( \Lambda ^ { \prime } \Lambda ) . \tag{33.8}
	$$
</synced_block>
We say that the matrices $`{ L _ { A } } ^ { B } ( \Lambda )`$ form a representation of the Lorentz group.
For an infinitesimal transformation $`\Lambda ^ { \mu } { } _ { \nu } = \delta ^ { \mu } { } _ { \nu } + \delta \omega ^ { \mu } { } _ { \nu }`$ , we can write
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#5be290fa21d1441dac83eec0ab9ecd48">
	$$
	\begin{array} { r } { U ( 1 + \delta \omega ) = I + \frac { i } { 2 } \delta \omega _ { \mu \nu } M ^ { \mu \nu } , } \end{array} \tag{33.9}
	$$
</synced_block>
where the operators $`M ^ { \mu \nu }`$ are the generators of the Lorentz group. As shown in section 2, the generators obey the commutation relations
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#728ab05bc9e9485a8544aabcb22e5a74">
	$$
	[ M ^ { \mu \nu } , M ^ { \rho \sigma } ] = i \Big ( g ^ { \mu \rho } M ^ { \nu \sigma } - ( \mu { } \nu ) \Big ) - ( \rho { } \sigma ) , \tag{33.10}
	$$
</synced_block>
which specify the Lie algebra of the Lorentz group.
We can identify the components of the angular momentum operator $`\bar { J }`$ as $`J _ { i } \equiv { \textstyle \frac { 1 } { 2 } } \varepsilon _ { i j k } M ^ { j k }`$ and the components of the boost operator $`\vec { K }`$ as $`K _ { i } \equiv M ^ { \ i 0 }`$ . We then find from eq. (33.10) that
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#1d72e0014c26427d8d3ef6a2e1b2ad12">
		$$
		[ M ^ { \mu \nu } , M ^ { \rho \sigma } ] = i \Big ( g ^ { \mu \rho } M ^ { \nu \sigma } - ( \mu { } \nu ) \Big ) - ( \rho { } \sigma ) , \tag{33.10}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#75c0f529d507492f938af3b487e5ca1b">
	$$
	\begin{array} { c } { { [ J _ { i } , J _ { j } ] = + i \varepsilon _ { i j k } J _ { k } \ , } } \\{ { { } } } \\{ { { } [ J _ { i } , K _ { j } ] = + i \varepsilon _ { i j k } K _ { k } \ , } } \\{ { { } } } \\{ { { } [ K _ { i } , K _ { j } ] = - i \varepsilon _ { i j k } J _ { k } \ . } } \end{array} \tag{33.11-33.12}
	$$
</synced_block>
For an infinitesimal transformation, we also have
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#165e459913434dec93000f166454f7b1">
	$$
	\begin{array} { r } { { L _ { A } } ^ { B } ( 1 + \delta \omega ) = { \delta _ { A } } ^ { B } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S ^ { \mu \nu } ) _ { A } { } ^ { B } \ , } \end{array} \tag{33.13-33.14}
	$$
</synced_block>
Eq. (33.7) then becomes
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#10bbda3ca90d4881854a9492787c4b5d">
		$$
		U ( \Lambda ) ^ { - 1 } \varphi _ { A } ( x ) U ( \Lambda ) = L _ { A } { } ^ { B } ( \Lambda ) \varphi _ { B } ( \Lambda ^ { - 1 } x ) , \tag{33.7}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#a4b584151683418bbef020581ce2d7a6">
	$$
	\lbrack \varphi _ { A } ( x ) , M ^ { \mu \nu } ] = { \mathcal L } ^ { \mu \nu } \varphi _ { A } ( x ) + ( S ^ { \mu \nu } ) _ { A } { } ^ { B } \varphi _ { B } ( x ) , \tag{33.15}
	$$
</synced_block>
where $`{ \mathcal { L } } ^ { \mu \nu } \equiv { \frac { 1 } { i } } ( x ^ { \mu } \partial ^ { \nu } - x ^ { \nu } \partial ^ { \mu } )`$ . Both the differential operators $`{ \mathcal { L } } ^ { \mu \nu }`$ and the representation matrices $`( S ^ { \mu \nu } ) _ { A } { } ^ { B }`$ must separately obey the same commutation relations as the generators themselves; see problems 2.8 and 2.9.
Our problem now is to find all possible sets of finite-dimensional matrices that obey eq. (33.10), or equivalently eqs. (33.11)–(33.13). Although the operators $`M ^ { \mu \nu }`$ must be hermitian, the matrices $`( S ^ { \mu \nu } ) _ { A } { } ^ { B }`$ need not be.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#1c8f8ee7e83e4d2db2939e31e2acf44e">
		$$
		[ M ^ { \mu \nu } , M ^ { \rho \sigma } ] = i \Big ( g ^ { \mu \rho } M ^ { \nu \sigma } - ( \mu { } \nu ) \Big ) - ( \rho { } \sigma ) , \tag{33.10}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#3fec6fabfeb542a99f6b7dbcdefc9968">
		$$
		\begin{array} { c } { { [ J _ { i } , J _ { j } ] = + i \varepsilon _ { i j k } J _ { k } \ , } } \\{ { { } } } \\{ { { } [ J _ { i } , K _ { j } ] = + i \varepsilon _ { i j k } K _ { k } \ , } } \\{ { { } } } \\{ { { } [ K _ { i } , K _ { j } ] = - i \varepsilon _ { i j k } J _ { k } \ . } } \end{array} \tag{33.11-33.12}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#903c0ff13d4c43ca9ff3737362ebce16">
		$$
		\begin{array} { r } { { L _ { A } } ^ { B } ( 1 + \delta \omega ) = { \delta _ { A } } ^ { B } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S ^ { \mu \nu } ) _ { A } { } ^ { B } \ , } \end{array} \tag{33.13-33.14}
		$$
	</synced_block>
</callout>
If we restrict our attention to eq. (33.11) alone, we know (from standard results in the quantum mechanics of angular momentum) that we can find three $`( 2 j + 1 ) \times ( 2 j + 1 )`$ hermitian matrices $`\mathcal { I } _ { 1 }`$ , $`\mathcal { I } _ { 2 }`$ , and $`\mathcal { I } _ { 3 }`$ that obey eq. (33.11), and that the eigenvalues of (say) $`\mathcal { I } _ { 3 }`$ are $`- j , - j { + } 1 , \ldots , + j`$ , where $`j`$ has the possible values $`0 , { \frac { 1 } { 2 } } , 1 , \ldots`$ We further know that these matrices constitute all of the inequivalent, irreducible representations of the Lie algebra of SO(3), the rotation group in three dimensions. Inequivalent means not related by a unitary transformation; irreducible means cannot be made block-diagonal by a unitary transformation. (The standard derivation assumes that the matrices are hermitian, but allowing nonhermitian matrices does not enlarge the set of solutions.) Also, when $`j`$ is a half integer, a rotation by $`2 \pi`$ results in an overall minus sign; these representations of the Lie algebra of $`\mathrm { S O ( 3 ) }`$ are therefore actually not representations of the group SO(3), since a $`2 \pi`$ rotation should be equivalent to no rotation. As we saw in section 24, the Lie algebra of SO(3) is the same as the Lie algebra of SU(2); the half-integer representations of this Lie algebra do qualify as representations of the group $`{ \mathrm { S U } } ( 2 )`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#d10186be9250431c8d09d12b8028a6c4">
		$$
		\begin{array} { c } { { [ J _ { i } , J _ { j } ] = + i \varepsilon _ { i j k } J _ { k } \ , } } \\{ { { } } } \\{ { { } [ J _ { i } , K _ { j } ] = + i \varepsilon _ { i j k } K _ { k } \ , } } \\{ { { } } } \\{ { { } [ K _ { i } , K _ { j } ] = - i \varepsilon _ { i j k } J _ { k } \ . } } \end{array} \tag{33.11-33.12}
		$$
	</synced_block>
</callout>
We would like to extend these conclusions to encompass the full set of eqs. (33.11)–(33.13). In order to do so, it is helpful to define some nonhermitian operators whose physical significance is obscure, but which simplify the commutation relations. These are
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#b3f1cab5e598402a9c050bcd004afc9a">
		$$
		\begin{array} { c } { { [ J _ { i } , J _ { j } ] = + i \varepsilon _ { i j k } J _ { k } \ , } } \\{ { { } } } \\{ { { } [ J _ { i } , K _ { j } ] = + i \varepsilon _ { i j k } K _ { k } \ , } } \\{ { { } } } \\{ { { } [ K _ { i } , K _ { j } ] = - i \varepsilon _ { i j k } J _ { k } \ . } } \end{array} \tag{33.11-33.12}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#5c946536d82a4417b3680091051a5868">
		$$
		\begin{array} { r } { { L _ { A } } ^ { B } ( 1 + \delta \omega ) = { \delta _ { A } } ^ { B } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S ^ { \mu \nu } ) _ { A } { } ^ { B } \ , } \end{array} \tag{33.13-33.14}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#6f8290e3d8da4de48f6366f74d63f7b0">
	$$
	\begin{array} { r } { N _ { i } \equiv \frac { 1 } { 2 } ( J _ { i } - i K _ { i } ) , } \\{ N _ { i } ^ { \dagger } \equiv \frac { 1 } { 2 } ( J _ { i } + i K _ { i } ) . } \end{array} \tag{33.16-33.17}
	$$
</synced_block>
In terms of $`N _ { i }`$ and $`N _ { i } ^ { \dagger }`$ , eqs. (33.11)–(33.13) become
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#8ada05d4048b40f180b4a7f9859caa30">
		$$
		\begin{array} { c } { { [ J _ { i } , J _ { j } ] = + i \varepsilon _ { i j k } J _ { k } \ , } } \\{ { { } } } \\{ { { } [ J _ { i } , K _ { j } ] = + i \varepsilon _ { i j k } K _ { k } \ , } } \\{ { { } } } \\{ { { } [ K _ { i } , K _ { j } ] = - i \varepsilon _ { i j k } J _ { k } \ . } } \end{array} \tag{33.11-33.12}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#37d40effe99d4e38abceca6e5e51fbd9">
		$$
		\begin{array} { r } { { L _ { A } } ^ { B } ( 1 + \delta \omega ) = { \delta _ { A } } ^ { B } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S ^ { \mu \nu } ) _ { A } { } ^ { B } \ , } \end{array} \tag{33.13-33.14}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#0da01c3b562146e086310e1e2008d4eb">
	$$
	\begin{array} { l } { { { [ } N _ { i } , N _ { j } ] = i \varepsilon _ { i j k } N _ { k } \mathrm { ~ , ~ } } } \\{ { { [ } N _ { i } ^ { \dagger } , N _ { j } ^ { \dagger } ] = i \varepsilon _ { i j k } N _ { k } ^ { \dagger } \mathrm { ~ , ~ } } } \\{ { { [ } N _ { i } , N _ { j } ^ { \dagger } ] = 0 \mathrm { ~ . ~ } } } \end{array} \tag{33.18-33.20}
	$$
</synced_block>
We see that we have two different SU(2) Lie algebras that are exchanged by hermitian conjugation. As we just discussed, a representation of the SU(2) Lie algebra is specified by an integer or half integer; we therefore conclude that a representation of the Lie algebra of the Lorentz group in four spacetime dimensions is specified by two integers or half-integers $`n`$ and $`n ^ { \prime }`$ .
We will label these representations as $`\left( 2 n \mathrm { + } 1 , 2 n ^ { \prime } \mathrm { + } 1 \right)`$ ; the number of components of a representation is then $`( 2 n + 1 ) ( 2 n ^ { \prime } + 1 )`$ . Different components within a representation can also be labeled by their angular momentum representations. To do this, we first note that, from eqs. (33.16) and (33.17), we have $`J _ { i } = N _ { i } + N _ { i } ^ { \dagger }`$ . Thus, deducing the allowed values of $`j`$ given $`n`$ and $`n ^ { \prime }`$ becomes a standard problem in the addition of angular momenta. The general result is that the allowed values of $`j`$ are $`| n - n ^ { \prime } | , | n - n ^ { \prime } | + 1 , \ldots , n + n ^ { \prime }`$ , and each of these values appears exactly once.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#9e913b5c065d420aab9b3d37abae540c">
		$$
		\begin{array} { r } { N _ { i } \equiv \frac { 1 } { 2 } ( J _ { i } - i K _ { i } ) , } \\{ N _ { i } ^ { \dagger } \equiv \frac { 1 } { 2 } ( J _ { i } + i K _ { i } ) . } \end{array} \tag{33.16-33.17}
		$$
	</synced_block>
</callout>
The four simplest and most often encountered representations are $`( 1 , 1 )`$ , $`( 2 , 1 )`$ , $`( 1 , 2 )`$ , and $`( 2 , 2 )`$ . These are given special names:
<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#ccde0790dc2444b4be2e34e42b9bc085">
	$$
	\begin{array} { l } { { ( 1 , 1 ) = s c a l a r \mathrm { o r } s i n g l e t } } \\{ { ( 2 , 1 ) = l e f t { - } h a n d e d s p i n o r } } \\{ { ( 1 , 2 ) = r i g h t { - } h a n d e d s p i n o r } } \\{ { ( 2 , 2 ) = v e c t o r . } } \end{array} \tag{33.21}
	$$
</synced_block>
It may seem a little surprising that $`( 2 , 2 )`$ is to be identified as the vector representation. To see that this must be the case, we first note that the vector representation is irreducible: all the components of a four-vector mix with each other under a general Lorentz transformation. Secondly, the vector representation has four components. The only candidate irreducible representations are $`( 4 , 1 )`$ , $`( 1 , 4 )`$ , and $`( 2 , 2 )`$ . The first two of these contain angular momenta $`\begin{array} { r } { j = \frac { 3 } { 2 } } \end{array}`$ only, whereas $`( 2 , 2 )`$ contains $`j = 0`$ and 1. This is just right for a four-vector, whose time component is a scalar under spatial rotations, and whose space components are a three-vector.
In order to gain a better understanding of what it means for $`( 2 , 2 )`$ to be the vector representation, we must first investigate the spinor representations $`( 1 , 2 )`$ and $`( 2 , 1 )`$ , which contain angular momenta $`\begin{array} { r } { j = \frac { 1 } { 2 } } \end{array}`$ only.
Reference notes
An extended treatment of representations of the Lorentz group in four dimensions can be found in Weinberg $`I ,`$ .
## Problems
### 33.1
Express $`A ^ { \mu \nu } ( x )`$ , $`S ^ { \mu \nu } ( x )`$ , and $`T ( x )`$ in terms of $`B ^ { \mu \nu } ( x )`$ .
### 33.2
Verify that eqs. (33.18)–(33.20) follow from eqs. (33.11)–(33.13).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#df947247681d4933877add64ebf71c37">
		$$
		\begin{array} { l } { { { [ } N _ { i } , N _ { j } ] = i \varepsilon _ { i j k } N _ { k } \mathrm { ~ , ~ } } } \\{ { { [ } N _ { i } ^ { \dagger } , N _ { j } ^ { \dagger } ] = i \varepsilon _ { i j k } N _ { k } ^ { \dagger } \mathrm { ~ , ~ } } } \\{ { { [ } N _ { i } , N _ { j } ^ { \dagger } ] = 0 \mathrm { ~ . ~ } } } \end{array} \tag{33.18-33.20}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#323f4e876d014893aed4a6958ac1da2b">
		$$
		\begin{array} { c } { { [ J _ { i } , J _ { j } ] = + i \varepsilon _ { i j k } J _ { k } \ , } } \\{ { { } } } \\{ { { } [ J _ { i } , K _ { j } ] = + i \varepsilon _ { i j k } K _ { k } \ , } } \\{ { { } } } \\{ { { } [ K _ { i } , K _ { j } ] = - i \varepsilon _ { i j k } J _ { k } \ . } } \end{array} \tag{33.11-33.12}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/019f6db67ebe48249715e9c33b64f6f8#6e5fd93d10e94dfc9c8cbc5d589a5dc0">
		$$
		\begin{array} { r } { { L _ { A } } ^ { B } ( 1 + \delta \omega ) = { \delta _ { A } } ^ { B } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S ^ { \mu \nu } ) _ { A } { } ^ { B } \ , } \end{array} \tag{33.13-33.14}
		$$
	</synced_block>
</callout>
</content>
</page>
