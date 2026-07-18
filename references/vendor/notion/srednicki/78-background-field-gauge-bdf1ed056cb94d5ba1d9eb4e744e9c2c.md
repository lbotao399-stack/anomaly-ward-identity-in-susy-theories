Here is the result of "view" for the Page with URL https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c as of 2026-04-27T16:55:44.997Z:
<page url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c">
<ancestor-path>
<parent-page url="https://app.notion.com/p/a7bfa00c3bf745b393bdba34b5dbfa3f" title="Part III Spin One"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"78. Background field gauge"}
</properties>
<content>
Prerequisite: 73
In the section, we will introduce a clever choice of gauge, background field gauge, that greatly simplifies the calculation of the beta function for Yang– Mills theory, especially at the one-loop level.
We begin with the lagrangian for Yang–Mills theory,
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#a0ba68e993b4470f92cc28ab710efec6">
	$$
	\begin{array} { r } { \mathcal { L } _ { \mathrm { Y M } } = - \frac { 1 } { 4 } F ^ { a \mu \nu } F _ { \mu \nu } ^ { a } , } \end{array} \tag{78.1}
	$$
</synced_block>
where the field strength is
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#f1e2ea06baec4e8d90d3e78ccb2a56c6">
	$$
	F _ { \mu \nu } ^ { a } = \partial _ { \mu } A _ { \nu } ^ { a } - \partial _ { \nu } A _ { \mu } ^ { a } + g f ^ { a b c } A _ { \mu } ^ { b } A _ { \nu } ^ { c } . \tag{78.2}
	$$
</synced_block>
To evaluate the path integral, we must choose a gauge. As we saw in section 71, one large class of gauges corresponds to choosing a gauge-fixing function $`G ^ { a } ( x )`$ , and adding $`{ \mathcal { L } } _ { \mathrm { g f } } + { \mathcal { L } } _ { \mathrm { g h } }`$ to $`{ \mathcal { L } } _ { \mathrm { v M } }`$ , where
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#1611dd06a6e149e8a2ad4311db6c220c">
	$$
	\begin{array} { l } { { \mathcal { L } _ { \mathrm { g f } } = - \frac { 1 } { 2 } \xi ^ { - 1 } G ^ { a } G ^ { a } , } } \\{ { \displaystyle } } \\{ { \mathcal { L } _ { \mathrm { g h } } = \bar { c } ^ { a } \frac { \partial G ^ { a } } { \partial A _ { \mu } ^ { b } } D _ { \mu } ^ { b c } c ^ { c } . } } \end{array} \tag{78.3-78.4}
	$$
</synced_block>
Here $`D _ { \mu } ^ { b c } = \delta ^ { b c } \partial _ { \mu } - i g ( T _ { \mathrm { { A } } } ^ { a } ) ^ { b c } A _ { \mu } ^ { a } = \delta ^ { b c } \partial _ { \mu } + g f ^ { b a c } A _ { \mu } ^ { a }`$ is the covariant derivative in the adjoint representation, and $`c`$ and $`c`$ are the ghost and antighost fields. The notation $`\partial G ^ { a } / \partial A _ { \mu } ^ { b }`$ means that any derivatives that act on $`A _ { \mu } ^ { b }`$ in $`G ^ { a }`$ now act to the right in eq. (78.4).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#d14b48cf1133494cac608bb5ed5bc947">
		$$
		\begin{array} { l } { { \mathcal { L } _ { \mathrm { g f } } = - \frac { 1 } { 2 } \xi ^ { - 1 } G ^ { a } G ^ { a } , } } \\{ { \displaystyle } } \\{ { \mathcal { L } _ { \mathrm { g h } } = \bar { c } ^ { a } \frac { \partial G ^ { a } } { \partial A _ { \mu } ^ { b } } D _ { \mu } ^ { b c } c ^ { c } . } } \end{array} \tag{78.3-78.4}
		$$
	</synced_block>
</callout>
We get $`R _ { \xi }`$ gauge by choosing $`G ^ { a } = \partial ^ { \mu } A _ { \mu } ^ { a }`$ . To get background field gauge, we first introduce a fixed, classical background field $`A _ { \mu } ^ { a } ( x )`$ , and the corresponding background covariant derivative,
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#1ef5fe2641f240d6a97a62e15f891fcc">
	$$
	\bar { \cal D } _ { \mu } \equiv \partial _ { \mu } - i g T _ { \mathrm { \scriptscriptstyle A } } ^ { a } \bar { A } _ { \mu } ^ { a } . \tag{78.5}
	$$
</synced_block>
Then we choose
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#ed21ad3b26c64305b2e571838d03184b">
	$$
	G ^ { a } = ( \bar { D } ^ { \mu } ) ^ { a b } ( A { - } \bar { A } ) _ { \mu } ^ { b } . \tag{78.6}
	$$
</synced_block>
The ghost lagrangian becomes $`{ \mathcal { L } } _ { \mathrm { g h } } = { \bar { c } } ^ { a } D ^ { \mu a b } D _ { \mu } ^ { b c } c ^ { c }`$ , or, after an integration by parts,
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#566a08fde7034da19370e25cae3b03e5">
	$$
	{ \mathcal { L } } _ { \mathrm { g h } } = - ( { \bar { D } } ^ { \mu } { \bar { c } } ) ^ { a } ( D _ { \mu } c ) ^ { a } , \tag{78.7}
	$$
</synced_block>
where $`( D ^ { \mu } { \bar { c } } ) ^ { a } = D ^ { \mu a b } { \bar { c } } ^ { b }`$ and $`( D _ { \mu } c ) ^ { a } = D _ { \mu } ^ { a c } c ^ { c }`$
Under an infinitesimal gauge transformation, the change in the fields is
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#bc4780a4c505456d8077d2ae7fab6fe7">
	$$
	\begin{array} { c } { { \delta _ { \mathrm { G } } A _ { \mu } ^ { a } ( x ) = - D _ { \mu } ^ { a c } \theta ^ { c } ( x ) \ , } } \\{ { { } } } \\{ { \delta _ { \mathrm { G } } c ^ { b } ( x ) = - i g \theta ^ { a } ( x ) ( T _ { \mathrm { A } } ^ { a } ) ^ { b c } c ^ { c } ( x ) \ , } } \\{ { { } } } \\{ { \delta _ { \mathrm { G } } \bar { A } _ { \mu } ^ { a } ( x ) = 0 \ . } } \end{array} \tag{78.8-78.10}
	$$
</synced_block>
The antighost $`c`$ transforms in the same way as $`c`$ (since the adjoint representation is real). The background field $`A`$ is fixed, and so does not change under a gauge transformation. Of course, this means that $`{ \mathcal { L } } _ { \mathrm { g f } }`$ and $`{ \mathcal { L } } _ { \mathrm { g h } }`$ are not gauge invariant; their role is to fix the gauge.
We can, however, define a background field gauge transformation, under which only the background field transforms,
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#aa88daecae9e43b89048090f32e1dc3f">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { \delta _ { \scriptscriptstyle \mathrm { B G } } \bar { A } _ { \mu } ^ { a } ( x ) = - \bar { D } _ { \mu } ^ { a c } \theta ^ { c } ( x ) , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \delta _ { \scriptscriptstyle \mathrm { B G } } A _ { \mu } ^ { a } ( x ) = 0 , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \delta _ { \scriptscriptstyle \mathrm { B G } } c ^ { b } ( x ) = 0 . } } \end{array} \tag{78.11-78.13}
	$$
</synced_block>
Obviously, $`\mathcal { L } _ { \mathrm { Y M } }`$ is invariant under this transformation (since it does not involve the background field at all), but $`{ \mathcal { L } } _ { \mathrm { g f } }`$ and $`{ \mathcal { L } } _ { \mathrm { g h } }`$ are not. However, $`{ \mathcal { L } } _ { \mathrm { g f } }`$ and $`{ \mathcal { L } } _ { \mathrm { g h } }`$ are invariant under the combined transformation $`\delta _ { \mathrm { G + B G } }`$ . For $`{ \mathcal { L } } _ { \mathrm { g h } }`$ , as given by eq. (78.7), this follows immediately from the fact that $`D _ { \mu }`$ and $`D _ { \mu }`$ have the same transformation property under the combined transformation, and that using covariant derivatives with all group indices contracted always yields a gauge-invariant expression.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#4cccd44a1729494bb451181e6553cbf6">
		$$
		{ \mathcal { L } } _ { \mathrm { g h } } = - ( { \bar { D } } ^ { \mu } { \bar { c } } ) ^ { a } ( D _ { \mu } c ) ^ { a } , \tag{78.7}
		$$
	</synced_block>
</callout>
To use this argument on $`{ \mathcal { L } } _ { \mathrm { g f } }`$ , as given by eqs. (78.3) and (78.6), we need to show that $`( A - A ) _ { \mu } ^ { a }`$ transforms under the combined transformation in the same way as does an ordinary field in the adjoint representation, such as the ghost field in eq. (78.9). To show this, we write
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#8ddb45b85f4545c69ecbb14083675de4">
		$$
		\begin{array} { l } { { \mathcal { L } _ { \mathrm { g f } } = - \frac { 1 } { 2 } \xi ^ { - 1 } G ^ { a } G ^ { a } , } } \\{ { \displaystyle } } \\{ { \mathcal { L } _ { \mathrm { g h } } = \bar { c } ^ { a } \frac { \partial G ^ { a } } { \partial A _ { \mu } ^ { b } } D _ { \mu } ^ { b c } c ^ { c } . } } \end{array} \tag{78.3-78.4}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#7120aec96d444ff1ae2d1b2a558794f3">
		$$
		G ^ { a } = ( \bar { D } ^ { \mu } ) ^ { a b } ( A { - } \bar { A } ) _ { \mu } ^ { b } . \tag{78.6}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#99580bb294fe4f0d8252c7b12069a049">
		$$
		\begin{array} { c } { { \delta _ { \mathrm { G } } A _ { \mu } ^ { a } ( x ) = - D _ { \mu } ^ { a c } \theta ^ { c } ( x ) \ , } } \\{ { { } } } \\{ { \delta _ { \mathrm { G } } c ^ { b } ( x ) = - i g \theta ^ { a } ( x ) ( T _ { \mathrm { A } } ^ { a } ) ^ { b c } c ^ { c } ( x ) \ , } } \\{ { { } } } \\{ { \delta _ { \mathrm { G } } \bar { A } _ { \mu } ^ { a } ( x ) = 0 \ . } } \end{array} \tag{78.8-78.10}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#ae0cdc30776042d5af5c5afa60de5244">
	$$
	\begin{array} { r c l } { { \delta _ { \mathrm { G + B G } } ( A - \bar { A } ) _ { \mu } ^ { b } = - ( D - \bar { D } ) _ { \mu } ^ { b a } \theta ^ { a } } } \\{ { } } & { { } } \\{ { } } & { { } } & { { = + i g ( A - \bar { A } ) _ { \mu } ^ { c } ( T _ { \mathrm { A } } ^ { c } ) ^ { b a } \theta ^ { a } } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { = - i g \theta ^ { a } ( T _ { \mathrm { A } } ^ { a } ) ^ { b c } ( A - \bar { A } ) _ { \mu } ^ { c } . } } \end{array} \tag{78.14}
	$$
</synced_block>
We used the complete antisymmetry of $`( T _ { \mathrm { A } } ^ { c } ) ^ { b a } = - i f ^ { c b a }`$ to get the last line. We see that $`( A - A ) _ { \mu } ^ { a }`$ transforms like an ordinary field in the adjoint representation, and so any expression that involves only covariant derivatives (either $`D _ { \mu }`$ or $`\boldsymbol { D } _ { \mu }`$ ) acting on this field, with all group indices contracted, is invariant under the combined transformation.
Therefore, the complete lagrangian, $`{ \mathcal { L } } = { \mathcal { L } } _ { \mathrm { Y M } } + { \mathcal { L } } _ { \mathrm { g f } } + { \mathcal { L } } _ { \mathrm { g h } }`$ , is invariant under the combined transformation.
Now consider constructing the quantum action $`\Gamma ( A , c , \bar { c } ; A )`$ . Recall from section 21 that the quantum action can be expressed as the sum of all 1PI diagrams, with the external propagators replaced by the corresponding fields. In a gauge theory, the quantum action is in general not gauge invariant, because we had to fix a gauge in order to carry out the path integral. The quantum action thus depends on the choice of gauge, and hence (in the case of background field gauge) on the background field $`A`$ . This is why we have written $`A`$ as an argument of $`\Gamma`$ , but separated by a semicolon to indicate its special role.
An important property of the quantum action is that it inherits all linear symmetries of the classical action; see problem 21.2. In the present case, these symmetries include the combined gauge transformation $`\delta _ { \mathrm { G + B G } }`$ . Therefore, the quantum action is also invariant under the combined transformation. The quantum action takes its simplest form if we set the external field $`A`$ equal to the background field $`A`$ . Then, $`\Gamma ( A , c , \bar { c } ; A )`$ is invariant under a gauge transformation of the form
$$
\delta _ { \mathrm { G + B G } } \bar { A } _ { \mu } ^ { a } ( x ) = - \bar { D } _ { \mu } ^ { a c } \theta ^ { c } ( x ) ,
$$
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#97284644d3834ca3861ef626cc2dd3c8">
	$$
	\delta _ { \tt G + B G } c ^ { b } ( x ) = - i g \theta ^ { a } ( x ) ( T _ { \mathrm { { a } } } ^ { a } ) ^ { b c } c ^ { c } ( x ) . \tag{78.15-78.16}
	$$
</synced_block>
This is now simply an ordinary gauge transformation, with $`A`$ as the gauge field.
The quantum action can be expressed as the classical action, plus loop corrections. For $`A = A`$ , we have
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#f30d4b27f5ad4969b2729159bf5b531c">
	$$
	\Gamma ( \bar { A } , c , \bar { c } ; \bar { A } ) = \int d ^ { 4 } x \left[ - { \textstyle \frac { 1 } { 4 } } \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } - ( \bar { D } ^ { \mu } \bar { c } ) ^ { a } ( \bar { D } _ { \mu } c ) ^ { a } \right] + \ldots , \tag{78.17}
	$$
</synced_block>
where the ellipses stand for the loop corrections. Note that $`{ \mathcal { L } } _ { \mathrm { g f } }`$ has disappeared \[because we set $`A = A`$ in eq. (78.6)\], and $`{ \mathcal { L } } _ { \mathrm { g h } }`$ has the form of a kinetic term for a complex scalar field in the adjoint representation. This term is therefore manifestly gauge invariant, as is the $`F F`$ term.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#5dd2b5ceca414ec9a048fddb019a68cc">
		$$
		G ^ { a } = ( \bar { D } ^ { \mu } ) ^ { a b } ( A { - } \bar { A } ) _ { \mu } ^ { b } . \tag{78.6}
		$$
	</synced_block>
</callout>
The gauge invariance of the quantum action has an important consequence for the loop corrections. In background field gauge, the renormalizing
$`Z`$ factors must respect the gauge invariance of the quantum action. Therefore, using the notation of section 73, we must have
$$
Z _ { 1 } = Z _ { 2 } ,
$$
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#c9845f5d0c4f4d958ee1829d52bafdce">
	$$
	Z _ { 1 ^ { \prime } } = Z _ { 2 ^ { \prime } } \ , \tag{78.18}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#d43f69588d024269ae9aacd4b211268a">
	$$
	Z _ { 3 } = Z _ { 3 g } = Z _ { 4 g } . \tag{78.19-78.20}
	$$
</synced_block>
Thus the relation between the bare and renormalized gauge couplings becomes
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#dde06c23616e443e9a9c797dbb080fd1">
	$$
	g _ { 0 } ^ { 2 } = Z _ { 3 } ^ { - 1 } g ^ { 2 } \tilde { \mu } ^ { \varepsilon } . \tag{78.21}
	$$
</synced_block>
This relation now involves only $`Z _ { 3 }`$ . We can therefore compute the beta function from $`Z _ { 3 }`$ alone. This is the major advantage of background field gauge.
To compute the loop corrections, we need to evaluate 1PI diagrams in background field gauge with the external propagators removed and replaced with external fields; the external gauge field should be set equal to the background field. The easiest way to do this is to set
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#714d86bb3dae445899d027b1c3cf7c62">
	$$
	A = \bar { A } + A \tag{78.22}
	$$
</synced_block>
at the beginning, and to write the path integral in terms of $`\mathcal { A }`$ . Then the $`\mathcal { A }`$ field appears only on internal lines, and the $`A`$ field only on external lines. The gauge-fixing term now reads
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#e4db208546524526ba253f774a080a53">
	$$
	\begin{array} { r } { \mathcal { L } _ { \mathrm { g f } } = - \frac { 1 } { 2 } \xi ^ { - 1 } ( \bar { D } ^ { \mu } \mathcal { A } _ { \mu } ) ^ { a } ( \bar { D } ^ { \nu } \mathcal { A } _ { \nu } ) ^ { a } \ , } \end{array} \tag{78.23}
	$$
</synced_block>
and the ghost term is given by eq. (78.7).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#9cdeda83603b4d4d8927cb795a8d4b05">
		$$
		{ \mathcal { L } } _ { \mathrm { g h } } = - ( { \bar { D } } ^ { \mu } { \bar { c } } ) ^ { a } ( D _ { \mu } c ) ^ { a } , \tag{78.7}
		$$
	</synced_block>
</callout>
The Feynman rules that follow from $`\mathcal { L } _ { \mathrm { Y M } } + \mathcal { L } _ { \mathrm { g f } } + \mathcal { L } _ { \mathrm { g h } }`$ are closely related to those we found in $`R _ { \xi }`$ gauge in section 72. The ghost and gluon propagators are the same, and vertices involving all internal lines are also the same. But if one or more gluon lines are external, then there are additional contributions to the vertices from $`{ \mathcal { L } } _ { \mathrm { g f } }`$ and $`{ \mathcal { L } } _ { \mathrm { g h } }`$ . We leave the details to problem 78.1.
Further simplifications arise at the one-loop level. Using eq. (78.22) in eq. (78.2), we find
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#6d48080e84fd4cbf99fc60a6b0f80ecd">
		$$
		A = \bar { A } + A \tag{78.22}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#66fb00afebaa485a9d7cdf02e011eba1">
		$$
		F _ { \mu \nu } ^ { a } = \partial _ { \mu } A _ { \nu } ^ { a } - \partial _ { \nu } A _ { \mu } ^ { a } + g f ^ { a b c } A _ { \mu } ^ { b } A _ { \nu } ^ { c } . \tag{78.2}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#1608d6aa7ce64204b3af47d59b4afd55">
	$$
	\begin{array} { c } { { F _ { \mu \nu } ^ { a } = \partial _ { \mu } \bar { A } _ { \nu } ^ { a } - \partial _ { \nu } \bar { A } _ { \mu } ^ { a } + g f ^ { a b c } \bar { A } _ { \mu } ^ { b } \bar { A } _ { \nu } ^ { c } } } \\{ { + \partial _ { \mu } { A } _ { \nu } ^ { a } - \partial _ { \nu } { A } _ { \mu } ^ { a } + g f ^ { a b c } ( \bar { A } _ { \mu } ^ { b } { A } _ { \nu } ^ { c } + { A } _ { \mu } ^ { b } \bar { A } _ { \nu } ^ { c } ) + g f ^ { a b c } { A } _ { \mu } ^ { b } { A } _ { \nu } ^ { c } } } \\{ { } } \\{ { = \bar { F } _ { \mu \nu } ^ { a } + ( \bar { D } _ { \mu } { A } _ { \nu } ) ^ { a } - ( \bar { D } _ { \nu } { A } _ { \mu } ) ^ { a } + g f ^ { a b c } { A } _ { \mu } ^ { b } { A } _ { \nu } ^ { c } . } } \end{array} \tag{78.22, 78.24}
	$$
</synced_block>
We then have
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#eae464b78fbc454d92f3c24d3cfb7cac">
	$$
	\begin{array} { l } { { { \mathcal { L } } _ { \mathrm { Y M } } = - \frac { 1 } { 4 } \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } - \frac { 1 } { 2 } ( \bar { D } ^ { \mu } \mathcal { A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \mu } \mathcal { A } _ { \nu } ) ^ { a } + \frac { 1 } { 2 } ( \bar { D } ^ { \mu } \mathcal { A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \nu } \mathcal { A } _ { \mu } ) ^ { a } } } \\{ { \qquad - \frac { 1 } { 2 } g f ^ { a b c } \bar { F } ^ { a \mu \nu } \mathcal { A } _ { \mu } ^ { b } \mathcal { A } _ { \nu } ^ { c } + \dots , } } \end{array} \tag{78.25}
	$$
</synced_block>
where the ellipses stand for terms that are linear, cubic, or quartic in $`\mathcal { A }`$ . Vertices arising from terms linear in $`\mathcal { A }`$ cannot appear in a 1PI diagram, and the cubic and quartic vertices do not appear in the one-loop contribution to the $`A`$ propagator.
The last term on the first line of eq. (78.25) can be usefully manipulated with some dummy-index relabelings and integrations by parts; we have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#b00b0eb5e4bf4956b40641b21d79dd61">
		$$
		\begin{array} { l } { { { \mathcal { L } } _ { \mathrm { Y M } } = - \frac { 1 } { 4 } \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } - \frac { 1 } { 2 } ( \bar { D } ^ { \mu } \mathcal { A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \mu } \mathcal { A } _ { \nu } ) ^ { a } + \frac { 1 } { 2 } ( \bar { D } ^ { \mu } \mathcal { A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \nu } \mathcal { A } _ { \mu } ) ^ { a } } } \\{ { \qquad - \frac { 1 } { 2 } g f ^ { a b c } \bar { F } ^ { a \mu \nu } \mathcal { A } _ { \mu } ^ { b } \mathcal { A } _ { \nu } ^ { c } + \dots , } } \end{array} \tag{78.25}
		$$
	</synced_block>
</callout>
$$
\begin{array} { l } { { ( \bar { D } ^ { \mu } \mathcal { A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \nu } \mathcal { A } _ { \mu } ) ^ { a } = ( \bar { D } ^ { \nu } \mathcal { A } _ { \mu } ) ^ { c } ( \bar { D } ^ { \mu } \mathcal { A } _ { \nu } ) ^ { c } } } \\{ { \ } } \\{ { \ } } \\{ { \qquad = - \mathcal { A } _ { \mu } ^ { b } ( \bar { D } ^ { \nu } \bar { D } ^ { \mu } ) ^ { b c } \mathcal { A } _ { \nu } ^ { c } } } \\{ { \ } } \\{ { \qquad = - \mathcal { A } _ { \mu } ^ { b } ( \bar { D } ^ { \mu } \bar { D } ^ { \nu } - [ \bar { D } ^ { \mu } , \bar { D } ^ { \nu } ] ) ^ { b c } \mathcal { A } _ { \nu } ^ { c } } } \\{ { \ } } \\{ { \ } } \\{ { \qquad = - \mathcal { A } _ { \mu } ^ { b } ( \bar { D } ^ { \mu } \bar { D } ^ { \nu } ) ^ { b c } \mathcal { A } _ { \nu } ^ { c } - i g ( T _ { \mathrm { a } } ^ { a } ) ^ { b c } \bar { F } ^ { a \mu \nu } \mathcal { A } _ { \mu } ^ { b } \mathcal { A } _ { \nu } ^ { c } } } \\{ { \ } } \\{ { \qquad = + ( \bar { D } ^ { \mu } \mathcal { A } _ { \mu } ) ^ { c } ( \bar { D } ^ { \nu } \mathcal { A } _ { \nu } ) ^ { c } - g f ^ { a b c } \bar { F } ^ { a \mu \nu } \mathcal { A } _ { \mu } ^ { b } \mathcal { A } _ { \nu } ^ { c } \ . } } \end{array}
$$
Now the first term on the right-hand side of eq. (78.26) has the same form as the gauge-fixing term. If we choose $`\xi = 1`$ , these two terms will cancel.
Setting $`\xi = 1`$ , and including a renormalizing factor of $`Z _ { 3 }`$ , the terms of interest in the complete lagrangian become
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#6d44e8c53a3d4a8eb1da36a3c18bdd14">
	$$
	\begin{array} { c } { { { \mathcal L = - \frac 1 4 Z _ { 3 } \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } - \frac 1 2 Z _ { 3 } ( \bar { D } ^ { \mu } { \mathcal A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \mu } { \mathcal A } _ { \nu } ) ^ { a } - ( \bar { D } ^ { \mu } \bar { c } ) ^ { a } ( \bar { D } _ { \mu } c ) ^ { a } } } } \\{ { - Z _ { 3 } g f ^ { a b c } \bar { F } ^ { a \mu \nu } { \mathcal A } _ { \mu } ^ { b } { \mathcal A } _ { \nu } ^ { c } . } } \end{array} \tag{78.27}
	$$
</synced_block>
In the ghost term, we have replaced $`D _ { \mu }`$ with $`\bar { D } _ { \mu }`$ ; the vertex corresponding to the dropped $`\mathcal { A }`$ term does not appear in the one-loop contribution to the $`A`$ propagator. Also, we can rescale $`\mathcal { A }`$ to absorb $`Z _ { 3 }`$ in all terms except the first; since $`\mathcal { A }`$ never appears on an external line, its normalization is irrelevant, and always cancels among propagators and vertices. (The same is true of the ghost field.)
The one-loop diagrams that contribute to the $`A`$ propagator are shown in fig. 78.1. The dashed lines in the first two diagrams represent either the $`\mathcal { A }`$ field or the ghost fields. In either case, the second diagram vanishes, because it is proportional to $`\int d ^ { 4 } \ell / \ell ^ { 2 }`$ , which is zero after dimensional regularization.
Note that the ghost term in eq. (78.27) has the form of a kinetic term for a complex scalar field in the adjoint representation. In problem 73.1, we found the contribution of a complex scalar field in a representation $`\mathrm { R } _ { \mathrm { c s } }`$ to
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#dafd58cdb00f48749e7b5a1fc5143c4e">
		$$
		\begin{array} { c } { { { \mathcal L = - \frac 1 4 Z _ { 3 } \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } - \frac 1 2 Z _ { 3 } ( \bar { D } ^ { \mu } { \mathcal A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \mu } { \mathcal A } _ { \nu } ) ^ { a } - ( \bar { D } ^ { \mu } \bar { c } ) ^ { a } ( \bar { D } _ { \mu } c ) ^ { a } } } } \\{ { - Z _ { 3 } g f ^ { a b c } \bar { F } ^ { a \mu \nu } { \mathcal A } _ { \mu } ^ { b } { \mathcal A } _ { \nu } ^ { c } . } } \end{array} \tag{78.27}
		$$
	</synced_block>
</callout>
![Figure 78.1. The one-loop contributions to the $`A`$ propagator in background field gauge; the dashed lines can be either ghosts or internal $`\boldsymbol { A }`$ gauge fields. The dots denote the $`F A A`$ vertex.](https://prod-files-secure.s3.us-west-2.amazonaws.com/d3aee2b7-4b3f-81c2-8179-00038068497b/03991ed5-7c35-4052-96c7-be68a245b8f1/0aa879d690d655982f208e90f95ee7f6d2c246cc327295118cc1ec2f6bb6f2d8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4IDZHGO%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T010203Z&X-Amz-Expires=300&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCInpSdorcMvR8mbz41yMsMGjWNvz7POXhaIGOSJ%2BQf0gIhAN1inPp9RZGnKFKu95D%2FYmfu70lY9an%2FczHbm74nVhP3Kv8DCGkQABoMNjM3NDIzMTgzODA1IgzYLeWjoFTF4ScvoLYq3AOQfhbW1VA2aaU4lSGSlw%2FP4ra1N4SKuBIUHOzMxBUatysSfq6F0rd%2BW2gVXMDgjBXWxTUEMoMuSP2W4cZS7cbR8qIb%2BjX13kZtffNRYvPosEpf3rApwmrQE%2BIjE5Vd4k7FsGez%2BF98gBUcvDQYlppLKrqstyDs9EE5gnQ7kgM73%2B9%2F0ydNoggW17%2FUDy9ApLIj8qPcDw9khU0XROIwSmrZTf%2FhF22ssV7Y5VQ%2FRUC%2BTzCU7WC7Z3Vo4Kb3Do%2BRZv4%2FCqGW9FVapQL7n991vDmh9E7WO2Q6S7v386gblEAZ0%2BcmrNE00rLiLptABLnOU%2FNxY7S7G5oBvNxri%2FV%2F4aEEctYeRS1TB%2Fsfg2%2FM5I%2B1tJYoYscTnsszGe7%2FjYvLyt4bdate3281j5dFRTIyJUp7CQ%2FDyOl%2FiYIZr2DrX%2FqTpSEYl81eS%2F56lwt2r7zZ9jNI0jjRLw1d599BS0nt%2BQo4VIo9RhyqnbYG9M0Oz%2BOUmOKnB2BzSlE3u1eh4S9aYyBipepsu9aWeE9kyKC4ElMFTFSW8HhDSMAN5AZQOJDvnNb0Y4VZLULkCt6iu1M01JKmUvFPW5NYBIge8uLyu8O3iKJGbtMBkykDwYM8spbsJoZtJJzie6rROefvmDD2juvSBjqkAdfDQ%2BUZel2sqiT1OlD8RQD6oFys51TKro2PAyQXp4bHxdjxpv97JCNQE6l4yx7qgXWHvS5F0XHMDv4lToiKm77XO24E1ZiXGAbVOelIgICK%2BhRDmdw%2BfPyJaGZycar50WFdX8CaoGGA1Ajsu6PC2lYSunb5GhRfoXsUSxmDzyaAbWciNscr4F3jLgJudxc77ESEgSanbR1lc1PqiPmR1EjVx5N8&X-Amz-Signature=643fd99c30e83b42f7f6d618cf3855aa0adb6c0dec0ca858f82c11c1fc857f22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
$`\Pi ( k ^ { 2 } )`$ is
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#3731b3bc4fe9418380f99c0e45845aa2">
	$$
	\Pi _ { \mathrm { c s } } ( k ^ { 2 } ) = - \frac { g ^ { 2 } } { 2 4 \pi ^ { 2 } } T ( \mathrm { R } _ { \mathrm { c s } } ) \frac { 1 } { \varepsilon } + \mathrm { f n i t e } . \tag{78.28}
	$$
</synced_block>
The ghost contribution is minus this, with $`\mathrm { R } _ { \mathrm { C S } } \longrightarrow \mathrm { A }`$ . (The minus sign is from the closed ghost loop.) Thus we have
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#e653987276f34410aa288b974c29e5dd">
	$$
	\Pi _ { \mathrm { g h } } ( k ^ { 2 } ) = + \frac { g ^ { 2 } } { 2 4 \pi ^ { 2 } } T ( { \mathrm A } ) \frac { 1 } { \varepsilon } + \mathrm { f i n i t e } + O ( g ^ { 4 } ) . \tag{78.29}
	$$
</synced_block>
For reference we recall that the counterterm contribution is
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#7f887b8ae3fe41d2b8403d539d82c93c">
	$$
	\Pi _ { \mathrm { c t } } ( k ^ { 2 } ) = - ( Z _ { 3 } - 1 ) . \tag{78.30}
	$$
</synced_block>
Next we consider the diagrams with $`\mathcal { A }`$ fields in the loop. If the $`F A A`$ interaction term was absent, the calculation would again be a familiar one; the $`D \mathcal { A } D \mathcal { A }`$ term in eq. (78.27) has the form of a kinetic term for a real scalar field that carries an extra index $`\nu`$ . That this index is a Lorentz vector index is immaterial for the diagrammatic calculation; the index is simply summed around the loop, yielding an extra factor of $`d = 4`$ . There is also an extra factor of one-half (relative to the case of a complex scalar) because $`\mathcal { A }`$ is real rather than complex. (Equivalently, the diagram has a symmetry factor of $`S = 2`$ from exchange of the top and bottom internal propagators when they do not carry charge arrows.) We thus have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#6aab97c6701b464cbf3f942dd08cd55d">
		$$
		\begin{array} { c } { { { \mathcal L = - \frac 1 4 Z _ { 3 } \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } - \frac 1 2 Z _ { 3 } ( \bar { D } ^ { \mu } { \mathcal A } ^ { \nu } ) ^ { a } ( \bar { D } _ { \mu } { \mathcal A } _ { \nu } ) ^ { a } - ( \bar { D } ^ { \mu } \bar { c } ) ^ { a } ( \bar { D } _ { \mu } c ) ^ { a } } } } \\{ { - Z _ { 3 } g f ^ { a b c } \bar { F } ^ { a \mu \nu } { \mathcal A } _ { \mu } ^ { b } { \mathcal A } _ { \nu } ^ { c } . } } \end{array} \tag{78.27}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#eb7dadf330e2480d9972399ecc7605fe">
	$$
	\Pi _ { \bar { \cal D } A \bar { \cal D } A } ( k ^ { 2 } ) = - \frac { g ^ { 2 } } { 1 2 \pi ^ { 2 } } T ( \mathrm { A } ) \frac { 1 } { \varepsilon } + \mathrm { f i n i t e } + O ( g ^ { 4 } ) . \tag{78.31}
	$$
</synced_block>
If we now include the $`F A A`$ interaction, we can think of $`F _ { \mu \nu } ^ { a }`$ as a constant external field. We can then draw the third diagram of fig. 78.1, where each dot denotes a vertex factor of $`- 2 i g f ^ { a b c } F _ { \mu \nu } ^ { a }`$ . This vacuum diagram has a symmetry factor of $`S = 2 \times 2`$ : one factor of two for exchanging the top and bottom propagators, and one for exchanging the left- and right-hand sources.
Its contribution to the quantum action is
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#88feef9d8b2c43fe97b58d343281858e">
	$$
	\begin{array} { r l r } { { \bar { \bar { F } } A A / V T = \frac { 1 } { 4 } ( - 2 i g f ^ { a c d } \bar { F } _ { \mu \nu } ^ { a } ) ( - 2 i g f ^ { b e g } \bar { F } _ { \rho \sigma } ^ { b } ) ( \frac { 1 } { i } ) ^ { 2 } \tilde { \mu } ^ { \mathcal { E } } \int \frac { d ^ { d } \ell } { ( 2 \pi ) ^ { d } } \frac { g _ { \mu \rho } \delta _ { c e } } { \ell ^ { 2 } } \frac { g _ { \nu \sigma } \delta _ { i } } { \ell ^ { 2 } } } } \\& { } & { = g ^ { 2 } T ( \mathrm { A } ) \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } ( \frac { i } { 8 \pi ^ { 2 } \varepsilon } + \mathrm { f n i t e } ) , \ ~ \ ~ \ ~ ( 7 8 . } \end{array} \tag{78.32}
	$$
</synced_block>
where $`V T`$ is the volume of space-time. Comparing this with the tree-level lagrangian $`- { \textstyle { \frac { 1 } { 4 } } } Z _ { 3 } { \bar { F } } { \bar { F } }`$ , and recalling eq. (78.30), we see that eq. (78.32) is equivalent to a contribution to $`\Pi ( k ^ { 2 } )`$ of
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#12524a6cf34a4dc3bff68d0d57f43e85">
		$$
		\Pi _ { \mathrm { c t } } ( k ^ { 2 } ) = - ( Z _ { 3 } - 1 ) . \tag{78.30}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#412321391d904da6be8a4f92a7faf2dc">
		$$
		\begin{array} { r l r } { { \bar { \bar { F } } A A / V T = \frac { 1 } { 4 } ( - 2 i g f ^ { a c d } \bar { F } _ { \mu \nu } ^ { a } ) ( - 2 i g f ^ { b e g } \bar { F } _ { \rho \sigma } ^ { b } ) ( \frac { 1 } { i } ) ^ { 2 } \tilde { \mu } ^ { \mathcal { E } } \int \frac { d ^ { d } \ell } { ( 2 \pi ) ^ { d } } \frac { g _ { \mu \rho } \delta _ { c e } } { \ell ^ { 2 } } \frac { g _ { \nu \sigma } \delta _ { i } } { \ell ^ { 2 } } } } \\& { } & { = g ^ { 2 } T ( \mathrm { A } ) \bar { F } ^ { a \mu \nu } \bar { F } _ { \mu \nu } ^ { a } ( \frac { i } { 8 \pi ^ { 2 } \varepsilon } + \mathrm { f n i t e } ) , \ ~ \ ~ \ ~ ( 7 8 . } \end{array} \tag{78.32}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#5a9d4ca58bcf4774bc54701e395b01d7">
	$$
	\Pi _ { \bar { \cal F } A \mathcal { A } } ( k ^ { 2 } ) = + \frac { g ^ { 2 } } { 2 \pi ^ { 2 } } T ( \mathrm { A } ) \frac { 1 } { \varepsilon } + \mathrm { f i n i t e } . \tag{78.32-78.33}
	$$
</synced_block>
There is also a one-loop diagram with one $`D \mathcal { A } D \mathcal { A }`$ vertex and one $`F A A`$ vertex; however, contracting the vector indices on the $`\mathcal { A }`$ fields around the loop leads to a factor of $`F ^ { \mu \nu } g _ { \mu \nu } = 0`$ . Similarly, a one-loop diagram with a single $`F A A`$ vertex vanishes.
We could also couple the gauge field to a Dirac fermion in the representation $`\mathrm { R } _ { \mathrm { D F } }`$ , and a complex scalar in the representation $`\mathrm { R } _ { \mathrm { C S } }`$ . The corresponding contributions to $`\Pi ( k ^ { 2 } )`$ were computed in section 73, and are given by eq. (78.28) and
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#5ded927b902d4ff4b0a22cf08125112a">
		$$
		\Pi _ { \mathrm { c s } } ( k ^ { 2 } ) = - \frac { g ^ { 2 } } { 2 4 \pi ^ { 2 } } T ( \mathrm { R } _ { \mathrm { c s } } ) \frac { 1 } { \varepsilon } + \mathrm { f n i t e } . \tag{78.28}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#6759519bc3a343ab998a0a94df371c34">
	$$
	\Pi _ { \scriptscriptstyle \mathrm { D F } } ( k ^ { 2 } ) = - \frac { g ^ { 2 } } { 6 \pi ^ { 2 } } T ( \mathrm { R } _ { \scriptscriptstyle \mathrm { D F } } ) \frac { 1 } { \varepsilon } + \mathrm { f i n i t e } . \tag{78.34}
	$$
</synced_block>
Adding up eqs. (78.28)–(78.31), (78.33), and (78.34), we find that finiteness of $`\Pi ( k ^ { 2 } )`$ requires
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#716659ec1d9141929620fcdb1ad04435">
		$$
		\Pi _ { \mathrm { c s } } ( k ^ { 2 } ) = - \frac { g ^ { 2 } } { 2 4 \pi ^ { 2 } } T ( \mathrm { R } _ { \mathrm { c s } } ) \frac { 1 } { \varepsilon } + \mathrm { f n i t e } . \tag{78.28}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#1da79903a4bb46a48a0df0b625b7b60b">
		$$
		\Pi _ { \bar { \cal D } A \bar { \cal D } A } ( k ^ { 2 } ) = - \frac { g ^ { 2 } } { 1 2 \pi ^ { 2 } } T ( \mathrm { A } ) \frac { 1 } { \varepsilon } + \mathrm { f i n i t e } + O ( g ^ { 4 } ) . \tag{78.31}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#ad500f6bb1ba48009c347ce08a5315e2">
		$$
		\Pi _ { \bar { \cal F } A \mathcal { A } } ( k ^ { 2 } ) = + \frac { g ^ { 2 } } { 2 \pi ^ { 2 } } T ( \mathrm { A } ) \frac { 1 } { \varepsilon } + \mathrm { f i n i t e } . \tag{78.32-78.33}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#bb3a4dd7f0224fd5b2891146267f3fdd">
		$$
		\Pi _ { \scriptscriptstyle \mathrm { D F } } ( k ^ { 2 } ) = - \frac { g ^ { 2 } } { 6 \pi ^ { 2 } } T ( \mathrm { R } _ { \scriptscriptstyle \mathrm { D F } } ) \frac { 1 } { \varepsilon } + \mathrm { f i n i t e } . \tag{78.34}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#f53b1debc54842e2b4aa5c4165600973">
	$$
	Z _ { 3 } = 1 + \frac { g ^ { 2 } } { 2 4 \pi ^ { 2 } } \Big [ \Big ( + 1 - 2 + 1 2 \Big ) T ( \mathrm { A } ) - 4 T ( \mathrm { R } _ { \mathrm { D F } } ) - T ( \mathrm { R } _ { \mathrm { c s } } ) \Big ] \frac { 1 } { \varepsilon } + { \cal O } ( g ^ { 4 } ) \tag{78.35}
	$$
</synced_block>
in the $`\mathrm { \overline { { M S } } }`$ renormalization scheme.
The analysis of section 28 now results in a beta function of
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#6a1170a8c0fb4da0b90de71ef0735056">
	$$
	\beta ( g ) = - \frac { g ^ { 3 } } { 4 8 \pi ^ { 2 } } \Big [ 1 1 T ( \mathrm { A } ) - 4 T ( \mathrm { R } _ { \mathrm { D F } } ) - T ( \mathrm { R } _ { \mathrm { C s } } ) \Big ] + O ( g ^ { 5 } ) \ . \tag{78.36}
	$$
</synced_block>
A Majorana fermion or a Weyl fermion makes half the contribution of a Dirac fermion in the same representation; a real scalar field makes half the contribution of a complex scalar field. (Majorana fermions and real scalars must be in real representations of the gauge group.)
In quantum chromodynamics, the gauge group is $`\mathrm { S U } ( 3 )`$ , and there are $`{ n _ { \mathrm { F } } } = 6`$ flavors of quarks (which are Dirac fermions) in the fundamental representation. We therefore have $`T ( A ) = 3`$ , $`\begin{array} { r } { T ( \mathrm { R } _ { \mathrm { D F } } ) = \frac { 1 } { 2 } n _ { \mathrm { F } } } \end{array}`$ , and $`T ( \mathrm { R } _ { \mathrm { c s } } ) = 0`$ ;
therefore
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#b48ed97a25d649ae8218e1fdabc08b02">
	$$
	\beta ( g ) = - \frac { g ^ { 3 } } { 1 6 \pi ^ { 2 } } \Big ( 1 1 - { \textstyle \frac { 2 } { 3 } } n _ { \mathrm { F } } \Big ) + O ( g ^ { 5 } ) ~ . \tag{78.37}
	$$
</synced_block>
We see that the beta function is negative for $`{ n _ { \mathrm { F } } \leq 1 6 }`$ , and so QCD is asymptotically free.
## Problems
### 78.1
Compute the tree-level vertex factors in background field gauge for all vertices that connect one or more external gluons with two or more internal lines (ghost or gluon).
### 78.2
Our one-loop corrections can be interpreted as functional determinants. Define
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#887c8567c86647f3840e3990730f0463">
	$$
	\begin{array} { r } { \Pi _ { \mathrm { R } , ( a , b ) } \equiv { \bar { D } } ^ { 2 } + g T _ { \mathrm { R } } ^ { a } { \bar { F } } _ { \mu \nu } ^ { a } S _ { ( a , b ) } ^ { \mu \nu } , } \end{array} \tag{78.38}
	$$
</synced_block>
where $`\bar { D } _ { \mu } = \partial _ { \mu } - i g ( T _ { \mathrm { R } } ^ { a } ) \bar { A } _ { \mu } ^ { a }`$ is the background-covariant derivative in the representation R, implicitly multiplied by the identity matrix for the $`( a , b )`$ representation of the Lorentz group, and S µ ν are the Lorentz generators for that representation; in particular,
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#0d518b7ef1b94c439210fe922785aa13">
	$$
	\begin{array} { c } { { S _ { ( 1 , 1 ) } ^ { \mu \nu } = 0 , } } \\{ { { } } } \\{ { S _ { ( 2 , 1 ) \oplus ( 1 , 2 ) } ^ { \mu \nu } = \frac { i } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] , } } \\{ { { } } } \\{ { { } ( S _ { ( 2 , 2 ) } ^ { \mu \nu } ) _ { \alpha \beta } = - i ( \delta ^ { \mu } { } _ { \alpha } \delta ^ { \nu } { } _ { \beta } - \delta ^ { \nu } { } _ { \alpha } \delta ^ { \mu } { } _ { \beta } ) . } } \end{array} \tag{78.39-78.41}
	$$
</synced_block>
Show that the one-loop contribution to the terms in the quantum action that do not depend on the ghost fields is given by
<synced_block url="https://app.notion.com/p/bdf1ed056cb94d5ba1d9eb4e744e9c2c#6088d072b78646f992d5cc5675f51cdf">
	$$
	\begin{array} { r l } { \exp i \Gamma _ { 1 - \mathrm { l o o p } } ( \bar { A } , 0 , 0 ; \bar { A } ) \propto ( \operatorname* { d e t } \pmb { \Pi } _ { \mathrm { A } , ( 1 , 1 ) } ) ^ { + 1 } } & { } \\{ \times ( \operatorname* { d e t } \pmb { \Pi } _ { \mathrm { A } , ( 2 , 2 ) } ) ^ { - 1 / 2 } } & { } \\{ \times ( \operatorname* { d e t } \pmb { \Pi } _ { \mathrm { R } _ { \mathrm { D F } } , ( 2 , 1 ) \oplus ( 1 , 2 ) } ) ^ { + 1 / 2 } } & { } \\{ \times ( \operatorname* { d e t } \pmb { \Pi } _ { \mathrm { R } _ { \mathrm { C S } } , ( 1 , 1 ) } ) ^ { - 1 } \ . } \end{array} \tag{78.42}
	$$
</synced_block>
Verify that this expression agrees with the diagrammatic analysis in this section.
</content>
</page>
