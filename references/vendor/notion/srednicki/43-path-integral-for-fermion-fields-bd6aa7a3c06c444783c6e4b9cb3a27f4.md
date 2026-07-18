Here is the result of "view" for the Page with URL https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4 as of 2026-04-27T10:13:09.149Z:
<page url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"43. The path integral for fermion fields"}
</properties>
<content>
We would like to write down a path integral formula for the vacuumexpectation value of a time-ordered product of free Dirac or Majorana fields. Recall that for a real scalar field with
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#4fd80a01eaa8435da79847cbf7c2d747">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { { \mathcal L } _ { 0 } = - \frac 1 2 \partial ^ { \mu } \varphi \partial _ { \mu } \varphi - \frac 1 2 m ^ { 2 } \varphi ^ { 2 } } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { = - \frac 1 2 \varphi ( - \partial ^ { 2 } + m ^ { 2 } ) \varphi - \frac 1 2 \partial _ { \mu } ( \varphi \partial ^ { \mu } \varphi ) , } } \end{array} \tag{43.1}
	$$
</synced_block>
we have
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#3f6d107d0dde4759ac148c56b4f18af7">
	$$
	\langle 0 | \mathrm { T } \varphi ( x _ { 1 } ) \ldots | 0 \rangle = { \frac { 1 } { i } } { \frac { \delta } { \delta J ( x _ { 1 } ) } } \cdot \cdot \cdot Z _ { 0 } ( J ) \Big | _ { J = 0 } , \tag{43.2}
	$$
</synced_block>
where
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#07a7005608c041fe862d8a68eb52114b">
	$$
	Z _ { 0 } ( J ) = \int { \mathcal { D } } \varphi \exp \left[ i \int d ^ { 4 } x ( { \mathcal { L } } _ { 0 } + J \varphi ) \right] . \tag{43.3}
	$$
</synced_block>
In this formula, we use the epsilon trick (see section 6) of replacing $`m ^ { 2 }`$ with $`m ^ { 2 } - i \epsilon`$ to construct the vacuum as the initial and final state. Then we get
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#05e961cca1b34f348f754c1f3a296af2">
	$$
	{ \cal Z } _ { 0 } ( J ) = \exp \left[ \frac { i } { 2 } \int d ^ { 4 } x d ^ { 4 } y J ( x ) \Delta ( x - y ) J ( y ) \right] , \tag{43.4}
	$$
</synced_block>
where the Feynman propagator
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#24b6062e8be541178507d4cb930f818c">
	$$
	\Delta ( x - y ) = \int { \frac { d ^ { 4 } k } { ( 2 \pi ) ^ { 4 } } } { \frac { e ^ { i k ( x - y ) } } { k ^ { 2 } + m ^ { 2 } - i \epsilon } } \tag{43.5}
	$$
</synced_block>
is the inverse of the Klein–Gordon wave operator:
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#1b1c478ceea84c0eafb2a2cc10d850b0">
	$$
	( - \partial _ { x } ^ { 2 } + m ^ { 2 } ) \Delta ( x - y ) = \delta ^ { 4 } ( x - y ) . \tag{43.6}
	$$
</synced_block>
For a complex scalar field with
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#0ffe59ff83594050b0252dbc8dde5b1c">
	$$
	\begin{array} { l } { { \mathcal { L } _ { 0 } = - \partial ^ { \mu } \varphi ^ { \dagger } \partial _ { \mu } \varphi - m ^ { 2 } \varphi ^ { \dagger } \varphi } } \\{ { { } } } \\{ { { } = - \varphi ^ { \dagger } ( - \partial ^ { 2 } + m ^ { 2 } ) \varphi - \partial _ { \mu } ( \varphi ^ { \dagger } \partial ^ { \mu } \varphi ) , } } \end{array} \tag{43.7}
	$$
</synced_block>
we have instead
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#301ecf96e7424a649a11fda72cebcf89">
	$$
	) | \mathrm { T } \varphi ( x _ { 1 } ) \dots \varphi ^ { \dagger } ( y _ { 1 } ) \dots | 0 \rangle = { \frac { 1 } { i } } \frac { \delta } { \delta J ^ { \dagger } ( x _ { 1 } ) } \dots \cdot \frac { 1 } { i } \frac { \delta } { \delta J ( y _ { 1 } ) } \dots Z _ { 0 } ( J ^ { \dagger } , J ) \Big | _ { J = J ^ { \dagger } = 0 } \tag{43.8}
	$$
</synced_block>
where
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#a31d3570772e4d00a94bf096b2923184">
	$$
	\begin{array} { l } { { Z _ { 0 } ( J ^ { \dagger } , J ) = \displaystyle \int { \mathcal D } \varphi ^ { \dagger } { \mathcal D } \varphi ~ \exp \left[ i \int d ^ { 4 } x \left( { \mathcal L } _ { 0 } + J ^ { \dagger } \varphi + \varphi ^ { \dagger } J \right) \right] ~ } } \\{ { ~ = \exp \left[ i \displaystyle \int d ^ { 4 } x d ^ { 4 } y J ^ { \dagger } ( x ) \Delta ( x - y ) J ( y ) \right] . } } \end{array} \tag{43.9}
	$$
</synced_block>
We treat $`J`$ and $`J ^ { \dagger }`$ as independent variables when evaluating eq. (43.8).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#9123e9d8ad6e40a399f6555c594c315a">
		$$
		) | \mathrm { T } \varphi ( x _ { 1 } ) \dots \varphi ^ { \dagger } ( y _ { 1 } ) \dots | 0 \rangle = { \frac { 1 } { i } } \frac { \delta } { \delta J ^ { \dagger } ( x _ { 1 } ) } \dots \cdot \frac { 1 } { i } \frac { \delta } { \delta J ( y _ { 1 } ) } \dots Z _ { 0 } ( J ^ { \dagger } , J ) \Big | _ { J = J ^ { \dagger } = 0 } \tag{43.8}
		$$
	</synced_block>
</callout>
In the case of a fermion field, we should have something similar, except that we need to account for the extra minus signs from anticommutation. For this to work out, a functional derivative with respect to an anticommuting variable must itself be treated as anticommuting. Thus if we define an anticommuting source $`\eta ( x )`$ for a Dirac field, we can write
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#edb5cbfa3d834609becf6c97fdc37c16">
	$$
	\begin{array} { c } { { \displaystyle \frac { \delta } { \delta \eta ( x ) } \int d ^ { 4 } y \left[ \overline { { { \eta } } } ( y ) \Psi ( y ) + \overline { { { \Psi } } } ( y ) \eta ( y ) \right] = - \overline { { { \Psi } } } ( x ) , } } \\{ { \displaystyle \frac { \delta } { \delta \overline { { { \eta } } } ( x ) } \int d ^ { 4 } y \left[ \overline { { { \eta } } } ( y ) \Psi ( y ) + \overline { { { \Psi } } } ( y ) \eta ( y ) \right] = + \Psi ( x ) . } } \end{array} \tag{43.10-43.11}
	$$
</synced_block>
The minus sign in eq. (43.10) arises because the $`\delta / \delta \eta`$ must pass through $`\overline { { \Psi } }`$ before reaching $`\eta`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#d24e337687ab4164b52846b5bc38fcfa">
		$$
		\begin{array} { c } { { \displaystyle \frac { \delta } { \delta \eta ( x ) } \int d ^ { 4 } y \left[ \overline { { { \eta } } } ( y ) \Psi ( y ) + \overline { { { \Psi } } } ( y ) \eta ( y ) \right] = - \overline { { { \Psi } } } ( x ) , } } \\{ { \displaystyle \frac { \delta } { \delta \overline { { { \eta } } } ( x ) } \int d ^ { 4 } y \left[ \overline { { { \eta } } } ( y ) \Psi ( y ) + \overline { { { \Psi } } } ( y ) \eta ( y ) \right] = + \Psi ( x ) . } } \end{array} \tag{43.10-43.11}
		$$
	</synced_block>
</callout>
Thus, consider a free Dirac field with
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#754dbfaa9fb9461db7084b11fd4fc9dd">
	$$
	\begin{array} { c } { { { \mathcal { L } } _ { 0 } = i \overline { { { \Psi } } } \partial / \Psi - m \overline { { { \Psi } } } \Psi } } \\{ { } } \\{ { = - \overline { { { \Psi } } } ( - i \partial / + m ) \Psi . } } \end{array} \tag{43.12}
	$$
</synced_block>
A natural guess for the appropriate path-integral formula, based on analogy with eq. (43.9), is
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#f807d49a12ac4b4fab8759ef62568d03">
		$$
		\begin{array} { l } { { Z _ { 0 } ( J ^ { \dagger } , J ) = \displaystyle \int { \mathcal D } \varphi ^ { \dagger } { \mathcal D } \varphi ~ \exp \left[ i \int d ^ { 4 } x \left( { \mathcal L } _ { 0 } + J ^ { \dagger } \varphi + \varphi ^ { \dagger } J \right) \right] ~ } } \\{ { ~ = \exp \left[ i \displaystyle \int d ^ { 4 } x d ^ { 4 } y J ^ { \dagger } ( x ) \Delta ( x - y ) J ( y ) \right] . } } \end{array} \tag{43.9}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#f9536498883a4933a84dd49402135f32">
	$$
	\begin{array} { l } { { \langle 0 | \mathrm { T } \Psi _ { \alpha _ { 1 } } ( x _ { 1 } ) \dots \overline { { \Psi } } _ { \beta _ { 1 } } ( y _ { 1 } ) \dots | 0 \rangle } } \\{ { \mathrm { ~ } = \displaystyle \frac { 1 } { i } \left. \frac { \delta } { \delta \overline { { { \eta } } } _ { \alpha _ { 1 } } ( x _ { 1 } ) } \dotsi \frac { \delta } { \delta \eta _ { \beta _ { 1 } } ( y _ { 1 } ) } \dots Z _ { 0 } ( \overline { { { \eta } } } , \eta ) \right| _ { \eta = \overline { { { \eta } } } = 0 } , } } \end{array} \tag{43.13}
	$$
</synced_block>
where
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#89e4b81e0e0e4fe791f631e8ed2cfe1c">
	$$
	\begin{array} { l } { { \displaystyle Z _ { 0 } ( \overline { { { \eta } } } , \eta ) = \int { \mathcal D } \Psi { \mathcal D } \overline { { { \Psi } } } \exp \left[ i \int d ^ { 4 } x ( { \mathcal L } _ { 0 } + \overline { { { \eta } } } \Psi + \overline { { { \Psi } } } \eta ) \right] } } \\{ { \displaystyle \ = \exp \left[ i \int d ^ { 4 } x d ^ { 4 } y \overline { { { \eta } } } ( x ) S ( x - y ) \eta ( y ) \right] , } } \end{array} \tag{43.14}
	$$
</synced_block>
and the Feynman propagator
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#7f07a250d3f6433d94934de1c00bc045">
	$$
	S ( x - y ) = \int { \frac { d ^ { 4 } p } { ( 2 \pi ) ^ { 4 } } } { \frac { ( - p / + m ) e ^ { i p ( x - y ) } } { p ^ { 2 } + m ^ { 2 } - i \epsilon } } \tag{43.15}
	$$
</synced_block>
is the inverse of the Dirac wave operator:
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#348f25d859404757b3650374c0c73d4a">
	$$
	( - i \partial / _ { x } + m ) S ( x - y ) = \delta ^ { 4 } ( x - y ) . \tag{43.16}
	$$
</synced_block>
Note that each $`\delta / \delta \eta`$ in eq. (43.13) comes with a factor of $`i`$ rather than the usual $`1 / i`$ ; this reflects the extra minus sign of eq. (43.10). We treat $`\eta`$ and $`\overline { { \eta } }`$ as independent variables when evaluating eq. (43.13). It is straightforward to check (by working out a few examples) that eqs. (43.13)–(43.16) do indeed reproduce the result of section 42 for the vacuum expectation value of a time-ordered product of Dirac fields.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#97fd38db746040f68a89899077e159b2">
		$$
		\begin{array} { l } { { \langle 0 | \mathrm { T } \Psi _ { \alpha _ { 1 } } ( x _ { 1 } ) \dots \overline { { \Psi } } _ { \beta _ { 1 } } ( y _ { 1 } ) \dots | 0 \rangle } } \\{ { \mathrm { ~ } = \displaystyle \frac { 1 } { i } \left. \frac { \delta } { \delta \overline { { { \eta } } } _ { \alpha _ { 1 } } ( x _ { 1 } ) } \dotsi \frac { \delta } { \delta \eta _ { \beta _ { 1 } } ( y _ { 1 } ) } \dots Z _ { 0 } ( \overline { { { \eta } } } , \eta ) \right| _ { \eta = \overline { { { \eta } } } = 0 } , } } \end{array} \tag{43.13}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#e301d7c4a8f74e69a08a46722a971360">
		$$
		\begin{array} { c } { { \displaystyle \frac { \delta } { \delta \eta ( x ) } \int d ^ { 4 } y \left[ \overline { { { \eta } } } ( y ) \Psi ( y ) + \overline { { { \Psi } } } ( y ) \eta ( y ) \right] = - \overline { { { \Psi } } } ( x ) , } } \\{ { \displaystyle \frac { \delta } { \delta \overline { { { \eta } } } ( x ) } \int d ^ { 4 } y \left[ \overline { { { \eta } } } ( y ) \Psi ( y ) + \overline { { { \Psi } } } ( y ) \eta ( y ) \right] = + \Psi ( x ) . } } \end{array} \tag{43.10-43.11}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#4b926f2a2b1548e0abe7c20019178736">
		$$
		( - i \partial / _ { x } + m ) S ( x - y ) = \delta ^ { 4 } ( x - y ) . \tag{43.16}
		$$
	</synced_block>
</callout>
This is really all we need to know. Recall that, for a complex scalar field with interactions specified by $`\mathcal { L } _ { 1 } ( \varphi ^ { \dagger } , \varphi )`$ , we have
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#52ca292011c648ff8b820ac9d86efb49">
	$$
	Z ( J ^ { \dagger } , J ) \propto \exp \left[ i \int d ^ { 4 } x { \mathcal L } _ { 1 } \bigg ( \frac { 1 } { i } \frac { \delta } { \delta J ( x ) } , \frac { 1 } { i } \frac { \delta } { \delta J ^ { \dagger } ( x ) } \bigg ) \right] Z _ { 0 } ( J ^ { \dagger } , J ) , \tag{43.17}
	$$
</synced_block>
where the overall normalization is fixed by $`Z ( 0 , 0 ) = 1`$ . Thus, for a Dirac field with interactions specified by $`\mathcal { L } _ { 1 } ( \overline { { \Psi } } , \Psi )`$ , we have
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#0e30a5e19fd34014b67f9c56e687a049">
	$$
	Z ( \overline { { { \eta } } } , \eta ) \propto \exp \left[ i \int d ^ { 4 } x { \mathcal L } _ { 1 } \biggl ( i \frac { \delta } { \delta \eta ( x ) } , \frac { 1 } { i } \frac { \delta } { \delta \overline { { { \eta } } } ( x ) } \biggr ) \right] Z _ { 0 } ( \overline { { { \eta } } } , \eta ) , \tag{43.18}
	$$
</synced_block>
where again the overall normalization is fixed by $`Z ( 0 , 0 ) = 1`$ . Vacuum expectation values of time-ordered products of Dirac fields in an interacting theory will now be given by eq. (43.13), but with $`Z _ { 0 } ( \overline { { { \eta } } } , \eta )`$ replaced by $`Z ( \overline { { { \eta } } } , \eta ) .`$ . Then, just as for a scalar field, this will lead to a Feynman-diagram expansion for $`Z ( \overline { { { \eta } } } , \eta )`$ . There are two extra complications: we must keep track of the spinor indices, and we must keep track of the extra minus signs from anticommutation. Both tasks are straightforward; we will take them up in section 45.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#642108ab6f8d4dab8e9fbf348536a40a">
		$$
		\begin{array} { l } { { \langle 0 | \mathrm { T } \Psi _ { \alpha _ { 1 } } ( x _ { 1 } ) \dots \overline { { \Psi } } _ { \beta _ { 1 } } ( y _ { 1 } ) \dots | 0 \rangle } } \\{ { \mathrm { ~ } = \displaystyle \frac { 1 } { i } \left. \frac { \delta } { \delta \overline { { { \eta } } } _ { \alpha _ { 1 } } ( x _ { 1 } ) } \dotsi \frac { \delta } { \delta \eta _ { \beta _ { 1 } } ( y _ { 1 } ) } \dots Z _ { 0 } ( \overline { { { \eta } } } , \eta ) \right| _ { \eta = \overline { { { \eta } } } = 0 } , } } \end{array} \tag{43.13}
		$$
	</synced_block>
</callout>
Next, let us consider a Majorana field with
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#8c5ce77323fe4b788087ea7d0bbf4431">
	$$
	\begin{array} { r } { \mathcal { L } _ { 0 } = \frac { i } { 2 } \Psi ^ { \mathrm { T } } \mathcal { C } \partial \Psi - \frac { 1 } { 2 } m \Psi ^ { \mathrm { T } } \mathcal { C } \Psi } \\{ = - \frac { 1 } { 2 } \Psi ^ { \mathrm { T } } \mathcal { C } ( - i \partial \phi + m ) \Psi . } \end{array} \tag{43.19}
	$$
</synced_block>
A natural guess for the appropriate path-integral formula, based on analogy with eq. (43.2), is
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#92398d65cd38430d9baa58cd0f184ed1">
		$$
		\langle 0 | \mathrm { T } \varphi ( x _ { 1 } ) \ldots | 0 \rangle = { \frac { 1 } { i } } { \frac { \delta } { \delta J ( x _ { 1 } ) } } \cdot \cdot \cdot Z _ { 0 } ( J ) \Big | _ { J = 0 } , \tag{43.2}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#42c5652923a44b2d841af678c47c6639">
	$$
	\langle 0 | \mathrm { T } \Psi _ { \alpha _ { 1 } } ( x _ { 1 } ) \dots | 0 \rangle = { \frac { 1 } { i } } \frac { \delta } { \delta \eta _ { \alpha _ { 1 } } ( x _ { 1 } ) } \ \dots \ Z _ { 0 } ( \eta ) \Big | _ { \eta = 0 } \ , \tag{43.20}
	$$
</synced_block>
where
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#29728042a3b14752a5dee9b6cac05f1e">
	$$
	\begin{array} { l } { { \displaystyle Z _ { 0 } ( \eta ) = \int { \mathcal D } \Psi \ \exp \biggl [ i \int d ^ { 4 } x ( { \mathcal L } _ { 0 } + \eta ^ { \mathrm { T } } \Psi ) \biggr ] } } \\{ { \displaystyle = \exp \biggl [ - \frac i 2 \int d ^ { 4 } x d ^ { 4 } y \eta ^ { \mathrm { T } } ( x ) S ( x - y ) { \mathcal C } ^ { - 1 } \eta ( y ) \biggr ] . } } \end{array} \tag{43.21}
	$$
</synced_block>
The Feynman propagator $`S ( x - y ) { \mathcal { C } } ^ { - 1 }`$ is the inverse of the Majorana wave operator $`\mathcal { C } ( - i \partial ^ { \aa } + m )`$ :
<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#1b558e9d2abb4a4fb19b80186c3aad18">
	$$
	\mathcal C ( - i \partial / _ { x } + m ) S ( x - y ) \mathcal C ^ { - 1 } = \delta ^ { 4 } ( x - y ) . \tag{43.22}
	$$
</synced_block>
The extra minus sign in eq. (43.21), as compared with eq. (43.14), arises because all functional derivatives in eq. (43.20) are accompanied by $`1 / i`$ , rather than half by $`1 / i`$ and half by $`i`$ , as in eq. (43.13). It is now straightforward to check (by working out a few examples) that eqs. (43.20)–(43.22) do indeed reproduce the result of section 42 for the vacuum expectation value of a time-ordered product of Majorana fields.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#19bbe8f2e8ec4538bc68edd8a5e2187b">
		$$
		\begin{array} { l } { { \displaystyle Z _ { 0 } ( \eta ) = \int { \mathcal D } \Psi \ \exp \biggl [ i \int d ^ { 4 } x ( { \mathcal L } _ { 0 } + \eta ^ { \mathrm { T } } \Psi ) \biggr ] } } \\{ { \displaystyle = \exp \biggl [ - \frac i 2 \int d ^ { 4 } x d ^ { 4 } y \eta ^ { \mathrm { T } } ( x ) S ( x - y ) { \mathcal C } ^ { - 1 } \eta ( y ) \biggr ] . } } \end{array} \tag{43.21}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#2dc5e95e2101400ea55997611cd2497a">
		$$
		\begin{array} { l } { { \displaystyle Z _ { 0 } ( \overline { { { \eta } } } , \eta ) = \int { \mathcal D } \Psi { \mathcal D } \overline { { { \Psi } } } \exp \left[ i \int d ^ { 4 } x ( { \mathcal L } _ { 0 } + \overline { { { \eta } } } \Psi + \overline { { { \Psi } } } \eta ) \right] } } \\{ { \displaystyle \ = \exp \left[ i \int d ^ { 4 } x d ^ { 4 } y \overline { { { \eta } } } ( x ) S ( x - y ) \eta ( y ) \right] , } } \end{array} \tag{43.14}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#3d1c1e20d0194b1694dfc11bccd9a956">
		$$
		\langle 0 | \mathrm { T } \Psi _ { \alpha _ { 1 } } ( x _ { 1 } ) \dots | 0 \rangle = { \frac { 1 } { i } } \frac { \delta } { \delta \eta _ { \alpha _ { 1 } } ( x _ { 1 } ) } \ \dots \ Z _ { 0 } ( \eta ) \Big | _ { \eta = 0 } \ , \tag{43.20}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#fe670f6f21ed4e548d97d642782eda49">
		$$
		\begin{array} { l } { { \langle 0 | \mathrm { T } \Psi _ { \alpha _ { 1 } } ( x _ { 1 } ) \dots \overline { { \Psi } } _ { \beta _ { 1 } } ( y _ { 1 } ) \dots | 0 \rangle } } \\{ { \mathrm { ~ } = \displaystyle \frac { 1 } { i } \left. \frac { \delta } { \delta \overline { { { \eta } } } _ { \alpha _ { 1 } } ( x _ { 1 } ) } \dotsi \frac { \delta } { \delta \eta _ { \beta _ { 1 } } ( y _ { 1 } ) } \dots Z _ { 0 } ( \overline { { { \eta } } } , \eta ) \right| _ { \eta = \overline { { { \eta } } } = 0 } , } } \end{array} \tag{43.13}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/bd6aa7a3c06c444783c6e4b9cb3a27f4#d641d44d8c31490fac4bb27e0082f9d5">
		$$
		\mathcal C ( - i \partial / _ { x } + m ) S ( x - y ) \mathcal C ^ { - 1 } = \delta ^ { 4 } ( x - y ) . \tag{43.22}
		$$
	</synced_block>
</callout>
</content>
</page>
