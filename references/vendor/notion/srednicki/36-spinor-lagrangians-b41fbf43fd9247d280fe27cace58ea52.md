Here is the result of "view" for the Page with URL https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52 as of 2026-04-27T17:30:26.984Z:
<page url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"36. Lagrangians for spinor fields"}
</properties>
<content>
Suppose we have a left-handed spinor field $`\psi _ { a }`$ . We would like to find a suitable lagrangian for it. This lagrangian must be Lorentz invariant, and it must be hermitian. We would also like it to be quadratic in $`\psi`$ and its hermitian conjugate $`\psi _ { \dot { a } } ^ { \dagger }`$ , because this will lead to a linear equation of motion, with plane-wave solutions. We want plane-wave solutions because these describe free particles, the starting point for a theory of interacting particles.
Let us begin with terms with no derivatives. The only possibility is $`\psi \psi =`$ $`\psi ^ { a } \psi _ { a } = \varepsilon ^ { a b } \psi _ { b } \psi _ { a }`$ , plus its hermitian conjugate. Because of anticommutation of the fields ( $`\psi _ { b } \psi _ { a } = - \psi _ { a } \psi _ { b }`$ ), this expression does not vanish (as it would if the fields commuted), and so we can use it as a term in $`\mathcal { L }`$ .
Next we need a term with derivatives. The obvious choice is $`\partial ^ { \mu } \psi \partial _ { \mu } \psi`$ , plus its hermitian conjugate. This, however, yields a hamiltonian that is unbounded below, which is unacceptable. To get a bounded hamiltonian, the kinetic term must involve both $`\psi`$ and $`\psi ^ { \dagger }`$ . A candidate is $`i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi`$ . This not hermitian, but
$$
\begin{array} { l } { { ( i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi ) ^ { \dagger } = ( i \psi _ { \dot { a } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } \psi _ { c } ) ^ { \dagger } } } \\{ { { } } } \\{ { { } = - i \partial _ { \mu } \psi _ { \dot { c } } ^ { \dagger } ( \bar { \sigma } ^ { \mu a \dot { c } } ) ^ { * } \psi _ { a } } } \\{ { { } } } \\{ { { } = - i \partial _ { \mu } \psi _ { \dot { c } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { c } a } \psi _ { a } } } \\{ { { } } } \\{ { { } = i \psi _ { \dot { c } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { c } a } \partial _ { \mu } \psi _ { a } - i \partial _ { \mu } ( \psi _ { \dot { c } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { c } a } \psi _ { a } ) } } \\{ { { } } } \\{ { { } = i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi - i \partial _ { \mu } ( \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \psi ) \ . } } \end{array}
$$
In the third line, we used the hermiticity of the matrices $`\bar { \sigma } ^ { \mu } = ( I , - \vec { \sigma } )`$ . In the fourth line, we used $`- ( \partial A ) B = A \partial B - \partial ( A B )`$ . In the last line, the second term is a total divergence, and vanishes (with suitable boundary conditions
on the fields at infinity) when we integrate it over $`d ^ { 4 } x`$ to get the action $`S`$ .<br>Thus $`i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi`$ has the hermiticity properties necessary for a term in $`\mathcal { L }`$ .
Our complete lagrangian for $`\psi`$ is then
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#80dc07b2bebb4bffa431111d322bc695">
	$$
	\begin{array} { r } { \mathcal { L } = i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi - \frac { 1 } { 2 } m \psi \psi - \frac { 1 } { 2 } m ^ { * } \psi ^ { \dagger } \psi ^ { \dagger } , } \end{array} \tag{36.2}
	$$
</synced_block>
where $`m`$ is a complex parameter with dimensions of mass. The phase of $`m`$ is actually irrelevant: if $`m = | m | e ^ { i \alpha }`$ , we can set $`\psi = e ^ { - i \alpha / 2 } \bar { \psi }`$ in eq. (36.2); then we get a lagrangian for $`\tilde { \psi }`$ that is identical to eq. (36.2), but with $`m`$ replaced by $`| m |`$ . So we can, without loss of generality, take $`m`$ to be real and positive in the first place, and that is what we will do, setting $`m ^ { * } = m`$ in eq. (36.2).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#18e98c654cd84f32aaaba7b42d611a0c">
		$$
		\begin{array} { r } { \mathcal { L } = i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi - \frac { 1 } { 2 } m \psi \psi - \frac { 1 } { 2 } m ^ { * } \psi ^ { \dagger } \psi ^ { \dagger } , } \end{array} \tag{36.2}
		$$
	</synced_block>
</callout>
The equation of motion for $`\psi`$ is then
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#787c6a63b3694d7db58017bf5e17e3bc">
	$$
	0 = - { \frac { \delta S } { \delta \psi ^ { \dagger } } } = - i \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi + m \psi ^ { \dagger } . \tag{36.3}
	$$
</synced_block>
Restoring the spinor indices, this reads
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#320cb8796c8342f29d860eae17923b25">
	$$
	0 = - i \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } \psi _ { c } + m \psi ^ { \dagger \dot { a } } . \tag{36.4}
	$$
</synced_block>
Taking the hermitian conjugate (or, equivalently, computing $`- \delta S / \delta \psi`$ ), we get
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#2603ece15637425f888740f6c93af77b">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { 0 = + i ( \bar { \sigma } ^ { \mu a \dot { c } } ) ^ { * } \partial _ { \mu } \psi _ { \dot { c } } ^ { \dagger } + m \psi ^ { a } } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { = + i \bar { \sigma } ^ { \mu \dot { c } a } \partial _ { \mu } \psi _ { \dot { c } } ^ { \dagger } + m \psi ^ { a } } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { = - i \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \psi ^ { \dagger \dot { c } } + m \psi _ { a } . } } \end{array} \tag{36.5}
	$$
</synced_block>
In the second line, we used the hermiticity of the matrices $`\bar { \sigma } ^ { \mu } = ( I , - \vec { \sigma } )`$ . In the third, we lowered the undotted index, and switched $`\dot { c } _ { \dot { c } }`$ to $`\dot { c } ^ { \dot { c } }`$ , which gives an extra minus sign.
Eqs. (36.5) and (36.4) can be combined to read
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#2bf8dc1525454ec5b80f48eda2e026f5">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { 0 = + i ( \bar { \sigma } ^ { \mu a \dot { c } } ) ^ { * } \partial _ { \mu } \psi _ { \dot { c } } ^ { \dagger } + m \psi ^ { a } } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { = + i \bar { \sigma } ^ { \mu \dot { c } a } \partial _ { \mu } \psi _ { \dot { c } } ^ { \dagger } + m \psi ^ { a } } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { = - i \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \psi ^ { \dagger \dot { c } } + m \psi _ { a } . } } \end{array} \tag{36.5}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#137fb9c446ae45e3883bf5bba4d5f9b7">
		$$
		0 = - i \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } \psi _ { c } + m \psi ^ { \dagger \dot { a } } . \tag{36.4}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#97b66015ef2448168ee760eb1f9040d0">
	$$
	\left( \begin{array} { c c } { { m \delta _ { a } { } ^ { c } } } & { { - i \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } } } \\{ { - i \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } } } & { { m \delta ^ { \dot { a } } { } _ { \dot { c } } } } \end{array} \right) \left( \begin{array} { c } { { \psi _ { c } } } \\{ { \psi ^ { \dagger \dot { c } } } } \end{array} \right) = 0 . \tag{36.6}
	$$
</synced_block>
We can write this more compactly by introducing the $`4 \times 4`$ gamma matrices
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#619ee931db9a4424b2e34a85d30229c8">
	$$
	\gamma ^ { \mu } \equiv \left( \begin{array} { c c } { { 0 } } & { { \sigma _ { a \dot { c } } ^ { \mu } } } \\{ { \bar { \sigma } ^ { \mu \dot { a } c } } } & { { 0 } } \end{array} \right) . \tag{36.7}
	$$
</synced_block>
Using the sigma-matrix relations,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#74dc0115009a435b8a7f94a177e9b9b5">
	$$
	\begin{array} { l } { { ( \sigma ^ { \mu } \bar { \sigma } ^ { \nu } + \sigma ^ { \nu } \bar { \sigma } ^ { \mu } ) _ { a } { } ^ { c } = - 2 g ^ { \mu \nu } \delta _ { a } { } ^ { c } \ : , } } \\{ { { } } } \\{ { ( \bar { \sigma } ^ { \mu } \sigma ^ { \nu } + \bar { \sigma } ^ { \nu } \sigma ^ { \mu } ) ^ { \dot { a } } { } _ { \dot { c } } = - 2 g ^ { \mu \nu } \delta ^ { \dot { a } } { } _ { \dot { c } } \ : , } } \end{array} \tag{36.8}
	$$
</synced_block>
which are most easily derived from the numerical formulae $`\sigma _ { a \dot { a } } ^ { \mu } = \left( I , \vec { \sigma } \right)`$ and $`\bar { \sigma } ^ { \mu \dot { a } a } = ( I , - \vec { \sigma } )`$ , we see that the gamma matrices obey
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#17fb4617132f426aa3918a718c779d7a">
	$$
	\{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = - 2 g ^ { \mu \nu } , \tag{36.9}
	$$
</synced_block>
where $`\{ A , B \} \equiv A B + B A`$ denotes the anticommutator, and there is an understood $`4 \times 4`$ identity matrix on the right-hand side. We also introduce a four-component Majorana field
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#c0af6e2af153464d808ff4d22edc0740">
	$$
	\Psi \equiv \left( \begin{array} { c } { { \psi _ { c } } } \\{ { \psi ^ { \dagger \dot { c } } } } \end{array} \right) . \tag{36.10}
	$$
</synced_block>
Then eq. (36.6) becomes
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#25ef0df26a0743afb0857face2b00e5f">
		$$
		\left( \begin{array} { c c } { { m \delta _ { a } { } ^ { c } } } & { { - i \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } } } \\{ { - i \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } } } & { { m \delta ^ { \dot { a } } { } _ { \dot { c } } } } \end{array} \right) \left( \begin{array} { c } { { \psi _ { c } } } \\{ { \psi ^ { \dagger \dot { c } } } } \end{array} \right) = 0 . \tag{36.6}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f55f771ff23f437ca4ab1e032890a89e">
	$$
	( - i \gamma ^ { \mu } \partial _ { \mu } + m ) \Psi = 0 . \tag{36.11}
	$$
</synced_block>
This is the Dirac equation. We first encountered it in section 1, where the gamma matrices were given different names ( $`\beta = \gamma ^ { 0 }`$ and $`\alpha ^ { k } = \gamma ^ { 0 } \gamma ^ { k }`$ ). Also, in section 1 we were trying (and failing) to interpret $`\Psi`$ as a wave function, rather than as a quantum field.
Now consider a theory of two left-handed spinor fields with an SO(2) symmetry,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#73f06254756e4eda8adf4bad89051589">
	$$
	\begin{array} { r } { \mathcal { L } = i \psi _ { i } ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi _ { i } - \frac { 1 } { 2 } m \psi _ { i } \psi _ { i } - \frac { 1 } { 2 } m \psi _ { i } ^ { \dagger } \psi _ { i } ^ { \dagger } , } \end{array} \tag{36.12}
	$$
</synced_block>
where the spinor indices are suppressed and $`i = 1 , 2`$ is implicitly summed. As in the analogous case of two scalar fields discussed in sections 22 and 23, this lagrangian is invariant under the SO(2) transformation
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#99f6ddaea6da4135b068fc6d13463eda">
	$$
	\binom { \psi _ { 1 } } { \psi _ { 2 } } ( \begin{array} { c c } { { \cos \alpha } } & { { \sin \alpha } } \\{ { - \sin \alpha } } & { { \cos \alpha } } \end{array} ) ( \begin{array} { c c } { { \psi _ { 1 } } } \\{ { \psi _ { 2 } } } \end{array} ) . \tag{36.13}
	$$
</synced_block>
We can write the lagrangian so that the SO(2) symmetry appears as a U(1) symmetry instead; let
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#776f3d6005e0405cb0a1e169412455ad">
	$$
	\begin{array} { r } { \chi = \frac { 1 } { \sqrt { 2 } } ( \psi _ { 1 } + i \psi _ { 2 } ) , } \\{ \xi = \frac { 1 } { \sqrt { 2 } } ( \psi _ { 1 } - i \psi _ { 2 } ) . } \end{array} \tag{36.14-36.15}
	$$
</synced_block>
In terms of these fields, we have
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#ed65904a582845d2a9e5d200db28fa4a">
	$$
	{ \mathcal { L } } = i \chi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \chi + i \xi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \xi - m \chi \xi - m \xi ^ { \dagger } \chi ^ { \dagger } . \tag{36.16}
	$$
</synced_block>
Eq. (36.16) is invariant under the U(1) version of eq. (36.13),
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#0ef0305fb047425d83bba93f4d215bce">
		$$
		{ \mathcal { L } } = i \chi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \chi + i \xi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \xi - m \chi \xi - m \xi ^ { \dagger } \chi ^ { \dagger } . \tag{36.16}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#6dcfc7abb1eb4634820d00fb7d465f5b">
		$$
		\binom { \psi _ { 1 } } { \psi _ { 2 } } ( \begin{array} { c c } { { \cos \alpha } } & { { \sin \alpha } } \\{ { - \sin \alpha } } & { { \cos \alpha } } \end{array} ) ( \begin{array} { c c } { { \psi _ { 1 } } } \\{ { \psi _ { 2 } } } \end{array} ) . \tag{36.13}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#923822ddf5904dbebc48ed5dbc165a6e">
	$$
	\begin{array} { c } { { \chi e ^ { - i \alpha } \chi ~ , } } \\{ { \xi e ^ { + i \alpha } \xi ~ . } } \end{array} \tag{36.17}
	$$
</synced_block>
Next, let us derive the equations of motion that we get from eq. (36.16), following the same procedure that ultimately led to eq. (36.6). The result is
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f01feebd4b594d25a1e6373df7062158">
		$$
		{ \mathcal { L } } = i \chi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \chi + i \xi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \xi - m \chi \xi - m \xi ^ { \dagger } \chi ^ { \dagger } . \tag{36.16}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#9701738d2a7f47dfa0a426aa0ce4a055">
		$$
		\left( \begin{array} { c c } { { m \delta _ { a } { } ^ { c } } } & { { - i \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } } } \\{ { - i \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } } } & { { m \delta ^ { \dot { a } } { } _ { \dot { c } } } } \end{array} \right) \left( \begin{array} { c } { { \psi _ { c } } } \\{ { \psi ^ { \dagger \dot { c } } } } \end{array} \right) = 0 . \tag{36.6}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#0977119ae2564b33abe2978383af045f">
	$$
	\left( \begin{array} { c c } { { m \delta _ { a } { } ^ { c } } } & { { - i \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } } } \\{ { - i \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } } } & { { m \delta ^ { \dot { a } } { } _ { \dot { c } } } } \end{array} \right) \left( \begin{array} { c } { { \chi _ { c } } } \\{ { \xi ^ { \dagger \dot { c } } } } \end{array} \right) = 0 . \tag{36.18}
	$$
</synced_block>
We can now define a four-component Dirac field
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#cafc9cf724974bbc9946435b2fdd0dd6">
	$$
	\Psi \equiv \left( { \chi \atop \xi ^ { \dagger \dot { c } } } \right) , \tag{36.19}
	$$
</synced_block>
which obeys the Dirac equation, eq. (36.11). (We have annoyingly used the same symbol $`\Psi`$ to denote both a Majorana field and a Dirac field; these are different objects, and so we must always announce which is meant when we write $`\Psi`$ .)
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#1b862d4953194641a099cb79c86e3bcc">
		$$
		( - i \gamma ^ { \mu } \partial _ { \mu } + m ) \Psi = 0 . \tag{36.11}
		$$
	</synced_block>
</callout>
We can also write the lagrangian, eq. (36.16), in terms of the Dirac field $`\Psi`$ , eq. (36.19). First we take the hermitian conjugate of $`\Psi`$ to get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#a546f98a855b4857b8c5f812ab7b4d49">
		$$
		{ \mathcal { L } } = i \chi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \chi + i \xi ^ { \dagger } { \bar { \sigma } } ^ { \mu } \partial _ { \mu } \xi - m \chi \xi - m \xi ^ { \dagger } \chi ^ { \dagger } . \tag{36.16}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#dea5c326a1024cbebcef24f185005756">
		$$
		\Psi \equiv \left( { \chi \atop \xi ^ { \dagger \dot { c } } } \right) , \tag{36.19}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#cce7be09d9914f7bbe27e51187ddc69f">
	$$
	\Psi ^ { \dagger } = ( \chi _ { \dot { a } } ^ { \dagger } , \xi ^ { a } ) . \tag{36.20}
	$$
</synced_block>
Introduce the matrix
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#3774fa05d23244eaa95dfd8b69eb166f">
	$$
	\beta \equiv \left( \begin{array} { c c } { { 0 } } & { { \delta ^ { \dot { a } } { } _ { \dot { c } } } } \\{ { \delta _ { a } { } ^ { c } } } & { { 0 } } \end{array} \right) \ . \tag{36.21}
	$$
</synced_block>
Numerically, $`\beta = \gamma ^ { 0 }`$ . However, the spinor index structure of $`\beta`$ and $`\gamma ^ { 0 }`$ is different, and so we will distinguish them. Given $`\beta`$ , we define
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#8707ddd8bd244018bce7c5ad404ee207">
	$$
	\overline { { { \Psi } } } \equiv \Psi ^ { \dag } \beta = ( \xi ^ { a } , \chi _ { \dot { a } } ^ { \dag } ) . \tag{36.22}
	$$
</synced_block>
Then we have
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#771d0387778c40fdab181eec3dce90d4">
	$$
	\overline { { { \Psi } } } \Psi = \xi ^ { a } \chi _ { a } + \chi _ { \dot { a } } ^ { \dagger } \xi ^ { \dagger \dot { a } } \ . \tag{36.23}
	$$
</synced_block>
Also,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#44a630904e3f495f82b62edb4e7efea4">
	$$
	\overline { { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi = \xi ^ { a } \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \xi ^ { \dagger \dot { c } } + \chi _ { \dot { a } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } \chi _ { c } . \tag{36.24}
	$$
</synced_block>
Using $`A \partial B = - ( \partial A ) B + \partial ( A B )`$ , the first term on the right-hand side of eq. (36.24) can be rewritten as
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#4c94016c93a3454abfcd2dea945e80c7">
		$$
		\overline { { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi = \xi ^ { a } \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \xi ^ { \dagger \dot { c } } + \chi _ { \dot { a } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } \chi _ { c } . \tag{36.24}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#27610a01707f4bc1bed23cbd39511118">
	$$
	\xi ^ { a } \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \xi ^ { \dagger \dot { c } } = - ( \partial _ { \mu } \xi ^ { a } ) \sigma _ { a \dot { c } } ^ { \mu } \xi ^ { \dagger \dot { c } } + \partial _ { \mu } ( \xi ^ { a } \sigma _ { a \dot { c } } ^ { \mu } \xi ^ { \dagger \dot { c } } ) \ . \tag{36.25}
	$$
</synced_block>
Then the first term on the right-hand side of eq. (36.25) can be rewritten as
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#a5aa50bb659b4a6d8d9c5e1018f5e5e6">
		$$
		\xi ^ { a } \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \xi ^ { \dagger \dot { c } } = - ( \partial _ { \mu } \xi ^ { a } ) \sigma _ { a \dot { c } } ^ { \mu } \xi ^ { \dagger \dot { c } } + \partial _ { \mu } ( \xi ^ { a } \sigma _ { a \dot { c } } ^ { \mu } \xi ^ { \dagger \dot { c } } ) \ . \tag{36.25}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#c58b39fd81504275bc0dfce7924a6408">
	$$
	- ( \partial _ { \mu } \xi ^ { a } ) \sigma _ { a \dot { c } } ^ { \mu } \xi ^ { \dagger \dot { c } } = + \xi ^ { \dagger \dot { c } } \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \xi ^ { a } = + \xi _ { \dot { c } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { c } a } \partial _ { \mu } \xi _ { a } . \tag{36.26}
	$$
</synced_block>
Here we used anticommutation of the fields to get the first equality, and switched $`{ \dot { c } } _ { \ \dot { c } }`$ to $`\dot { c } ^ { c }`$ and $`\textit { a } ^ { a }`$ to $`{ \mathit { \Pi } } ^ { a } _ { a }`$ (thus generating two minus signs) to get the second. Combining eqs. (36.24)–(36.26), we get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#55d6f0e04448479f8ae7c90d81cbca2d">
		$$
		\overline { { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi = \xi ^ { a } \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \xi ^ { \dagger \dot { c } } + \chi _ { \dot { a } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { a } c } \partial _ { \mu } \chi _ { c } . \tag{36.24}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#336ec358efcc4a3b9f16234ef8257943">
		$$
		- ( \partial _ { \mu } \xi ^ { a } ) \sigma _ { a \dot { c } } ^ { \mu } \xi ^ { \dagger \dot { c } } = + \xi ^ { \dagger \dot { c } } \sigma _ { a \dot { c } } ^ { \mu } \partial _ { \mu } \xi ^ { a } = + \xi _ { \dot { c } } ^ { \dagger } \bar { \sigma } ^ { \mu \dot { c } a } \partial _ { \mu } \xi _ { a } . \tag{36.26}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#5d66074ab528488aa0f310e076aff842">
	$$
	\overline { { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi = \chi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \chi + \xi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \xi + \partial _ { \mu } ( \xi \sigma ^ { \mu } \xi ^ { \dagger } ) . \tag{36.27}
	$$
</synced_block>
Therefore, up to an irrelevant total divergence, we have
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#c812ef20afce46198437ea4978902d79">
	$$
	{ \mathcal { L } } = i { \overline { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi - m { \overline { { \Psi } } } \Psi ~ . \tag{36.28}
	$$
</synced_block>
This form of the lagrangian is invariant under the U(1) transformation
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#917c934bd7a34e85bcd6dd9050a2ea0c">
	$$
	\begin{array} { l } { { \Psi ( \vphantom { \frac { 1 } { \Psi } } ) \nonumber \Psi e ^ { - i \alpha } \Psi \ , } } \\{ { \overline { { { \Psi } } } e ^ { + i \alpha } \overline { { { \Psi } } } \ , } } \end{array} \tag{36.29}
	$$
</synced_block>
which, given eq. (36.19), is the same as eq. (36.17). The Noether current associated with this symmetry is
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#a6edcf4cf0c54ec1b5c837c5c3982651">
		$$
		\Psi \equiv \left( { \chi \atop \xi ^ { \dagger \dot { c } } } \right) , \tag{36.19}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#b5a4ebee0165499c88d71527eb188ec0">
		$$
		\begin{array} { c } { { \chi e ^ { - i \alpha } \chi ~ , } } \\{ { \xi e ^ { + i \alpha } \xi ~ . } } \end{array} \tag{36.17}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#6cf194b6a8e6475f958b229941ab22f6">
	$$
	j ^ { \mu } = \overline { { { \Psi } } } \gamma ^ { \mu } \Psi = \chi ^ { \dagger } \bar { \sigma } ^ { \mu } \chi - \xi ^ { \dagger } \bar { \sigma } ^ { \mu } \xi \ . \tag{36.30}
	$$
</synced_block>
In quantum electrodynamics, the electromagnetic current is $`e { \overline { { \Psi } } } \gamma ^ { \mu } \Psi`$ , where $`e`$ is the charge of the electron.
As in the case of a complex scalar field with a $`\mathrm { U } ( 1 )`$ symmetry, there is an additional discrete symmetry, called charge conjugation, that enlarges SO(2) to O(2). Charge conjugation simply exchanges $`\chi`$ and $`\xi`$ . We can define a unitary charge conjugation operator $`C`$ that implements this,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#0454e2da539247edb2ad1dd3b0f98469">
	$$
	\begin{array} { l } { { C ^ { - 1 } \chi _ { a } ( x ) C = \xi _ { a } ( x ) \ , } } \\{ { { } } } \\{ { C ^ { - 1 } \xi _ { a } ( x ) C = \chi _ { a } ( x ) \ , } } \end{array} \tag{36.31}
	$$
</synced_block>
where, for the sake of precision, we have restored the spinor index and spacetime argument. We then have $`C ^ { - 1 } { \mathcal { L } } ( x ) C = { \mathcal { L } } ( x )`$ .
To express eq. (36.31) in terms of the Dirac field, eq. (36.19), we first introduce the charge conjugation matrix
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#6618a132e3624039a011b120a881ff2f">
		$$
		\begin{array} { l } { { C ^ { - 1 } \chi _ { a } ( x ) C = \xi _ { a } ( x ) \ , } } \\{ { { } } } \\{ { C ^ { - 1 } \xi _ { a } ( x ) C = \chi _ { a } ( x ) \ , } } \end{array} \tag{36.31}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#8f19732ad47d48d6b39ae5d492a09217">
		$$
		\Psi \equiv \left( { \chi \atop \xi ^ { \dagger \dot { c } } } \right) , \tag{36.19}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#a937569f66a4498ab59959c92efdcf80">
	$$
	\mathcal { C } \equiv \left( \begin{array} { c c } { { \varepsilon _ { a c } } } & { { 0 } } \\{ { 0 } } & { { \varepsilon ^ { \dot { a } \dot { c } } } } \end{array} \right) . \tag{36.32}
	$$
</synced_block>
Next we notice that, if we take the transpose of $`\overline { { \Psi } }`$ , eq. (36.22), we get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#4743e892608b4e598102ac57cc2b5717">
		$$
		\overline { { { \Psi } } } \equiv \Psi ^ { \dag } \beta = ( \xi ^ { a } , \chi _ { \dot { a } } ^ { \dag } ) . \tag{36.22}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#c44f3b51db474182aaef4331fffea7e7">
	$$
	\overline { { { \Psi } } } ^ { \mathrm { \tiny { T } } } = \left( { \xi } _ { \lambda } ^ { a } \right) . \tag{36.33}
	$$
</synced_block>
Then, if we multiply by $`\mathcal { C }`$ , we get a field that we will call $`\Psi ^ { \mathrm { c } }`$ , the charge conjugate of $`\Psi`$ ,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#dec6828e6367423097309b514bf0c96b">
	$$
	\Psi ^ { \mathrm { c } } \equiv \mathcal { C } \overline { { { \Psi } } } ^ { \mathrm { r } } = \left( { \xi } _ { a } ^ { ~ } \atop \chi ^ { \dagger \dot { a } } \right) . \tag{36.34}
	$$
</synced_block>
We see that $`\Psi ^ { \mathrm { C } }`$ is the same as the original field $`\Psi`$ , eq. (36.19), except that the roles of $`\chi`$ and $`\xi`$ have been switched. We therefore have
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#7703e3a83cf84d4d9e97348e647ca67e">
		$$
		\Psi \equiv \left( { \chi \atop \xi ^ { \dagger \dot { c } } } \right) , \tag{36.19}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#9741df4f89e9445f89e1b97ecd168e47">
	$$
	C ^ { - 1 } \Psi ( x ) C = \Psi ^ { \mathrm { c } } ( x ) \tag{36.35}
	$$
</synced_block>
for a Dirac field.
The charge conjugation matrix has a number of useful properties. As a numerical matrix, it obeys
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#52e4f7579ee3422da7f3472448cd256b">
	$$
	\begin{array} { r } { \mathcal { C } ^ { \mathrm { T } } = \mathcal { C } ^ { \dagger } = \mathcal { C } ^ { - 1 } = - \mathcal { C } , } \end{array} \tag{36.36}
	$$
</synced_block>
and we can also write it as
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#ef65115309e649a3a7e1445a30c96b3e">
	$$
	\mathcal { C } = \left( \begin{array} { c c } { - \varepsilon ^ { a c } } & { 0 } \\{ 0 } & { - \varepsilon _ { \dot { a } \dot { c } } } \end{array} \right) . \tag{36.37}
	$$
</synced_block>
A result that we will need later is
$$
\begin{array} { c } { { \mathcal { C } ^ { - 1 } \gamma ^ { \mu } \mathcal { C } = \left( \begin{array} { c c } { { \varepsilon ^ { a b } } } & { { 0 } } \\{ { 0 } } & { { \varepsilon _ { \mathrm { a i } } \delta } } \end{array} \right) \left( \begin{array} { c c } { { 0 } } & { { \sigma _ { b \bar { c } } ^ { \mu } } } \\{ { \bar { \sigma } ^ { \mu b c } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c c } { { \varepsilon _ { c e } } } & { { 0 } } \\{ { 0 } } & { { \varepsilon ^ { \dot { \varepsilon } \dot { e } } } } \end{array} \right) } } \\{ { = \left( \begin{array} { c c } { { 0 } } & { { \varepsilon ^ { a b } \sigma _ { b \bar { c } } ^ { \mu } \bar { c } ^ { \dot { c } \dot { e } } } } \\{ { \varepsilon _ { \mathrm { a i } \bar { \sigma } } ^ { \mu b c } \bar { c } _ { c e } } } & { { 0 } } \end{array} \right) } } \\{ { = \left( \begin{array} { c c } { { 0 } } & { { - \bar { \sigma } ^ { \mu a \dot { e } } } } \\{ { - \sigma _ { \bar { a } e } ^ { \mu } } } & { { 0 } } \end{array} \right) . } } \end{array}
$$
The minus signs in the last line come from raising or lowering an index by contracting with the first (rather than the second) index of an $`\varepsilon`$ symbol. Comparing with
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#c3643f14ea114203b13127ebca9835af">
	$$
	\gamma ^ { \mu } = \left( \begin{array} { c c } { { 0 } } & { { \sigma _ { e \dot { a } } ^ { \mu } } } \\{ { \bar { \sigma } ^ { \mu \dot { e } a } } } & { { 0 } } \end{array} \right) , \tag{36.39}
	$$
</synced_block>
we see that
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#db25fb7c2dd24c9ea234b5948877b663">
	$$
	{ \mathcal C } ^ { - 1 } \gamma ^ { \mu } { \mathcal C } = - ( \gamma ^ { \mu } ) ^ { \mathrm { r } } . \tag{36.40}
	$$
</synced_block>
Now let us return to the Majorana field, eq. (36.10). It is obvious that a Majorana field is its own charge conjugate, that is, $`\Psi ^ { \mathrm { c } } = \Psi`$ . This condition is analogous to the condition $`\varphi ^ { \dagger } = \varphi`$ that is satisfied by a real scalar field. A Dirac field, with its U(1) symmetry, is analogous to a complex scalar field, while a Majorana field, which has no U(1) symmetry, is analogous to a real scalar field.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#bd64bc231fa144cfbd1ae3e14e8f68e3">
		$$
		\Psi \equiv \left( \begin{array} { c } { { \psi _ { c } } } \\{ { \psi ^ { \dagger \dot { c } } } } \end{array} \right) . \tag{36.10}
		$$
	</synced_block>
</callout>
We can write our original lagrangian for a single left-handed spinor field, eq. (36.2), in terms of a Majorana field, eq. (36.10), by retracing eqs. (36.20)– (36.28) with $`\chi \to \psi`$ and $`\xi \psi`$ . The result is
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#ef425d2af9e64c02ab9748d1e2fdc23c">
		$$
		\begin{array} { r } { \mathcal { L } = i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi - \frac { 1 } { 2 } m \psi \psi - \frac { 1 } { 2 } m ^ { * } \psi ^ { \dagger } \psi ^ { \dagger } , } \end{array} \tag{36.2}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#fad8642d5fd9441fa825d376c67b1815">
		$$
		\Psi \equiv \left( \begin{array} { c } { { \psi _ { c } } } \\{ { \psi ^ { \dagger \dot { c } } } } \end{array} \right) . \tag{36.10}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#fce0e324f285453abd5d87b606d52e8e">
		$$
		\Psi ^ { \dagger } = ( \chi _ { \dot { a } } ^ { \dagger } , \xi ^ { a } ) . \tag{36.20}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#7ba0b43c058043a3b8370d23f79a8a0b">
		$$
		{ \mathcal { L } } = i { \overline { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi - m { \overline { { \Psi } } } \Psi ~ . \tag{36.28}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#0fa007c1ccb64657b046897b1ef6542c">
	$$
	{ \mathcal { L } } = { \textstyle \frac { i } { 2 } } { \overline { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi - { \textstyle \frac { 1 } { 2 } } m { \overline { { \Psi } } } \Psi ~ . \tag{36.41}
	$$
</synced_block>
However, we cannot yet derive the equation of motion from eq. (36.41) because it does not yet incorporate the Majorana condition $`\Psi ^ { \mathrm { c } } = \Psi`$ . To remedy this, we use eq. (36.36) to write the Majorana condition $`\Psi = \mathcal { C } \overline { { \Psi } } ^ { \mathrm { T } }`$ as $`{ \overline { { \Psi } } } = \Psi ^ { \mathrm { T } } { \mathcal { C } }`$ . Then we can replace $`\overline { { \Psi } }`$ in eq. (36.41) by $`\Psi ^ { \mathrm { T } } { \mathcal { C } }`$ to get
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#7a3570e0bf8d44d8a2c31cc6474e713f">
		$$
		{ \mathcal { L } } = { \textstyle \frac { i } { 2 } } { \overline { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi - { \textstyle \frac { 1 } { 2 } } m { \overline { { \Psi } } } \Psi ~ . \tag{36.41}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#ee3db36f700c4cc9b4330f7e435923f4">
		$$
		\begin{array} { r } { \mathcal { C } ^ { \mathrm { T } } = \mathcal { C } ^ { \dagger } = \mathcal { C } ^ { - 1 } = - \mathcal { C } , } \end{array} \tag{36.36}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#2f259f1aaa3b48e1b29e9d82c3d9c609">
	$$
	\begin{array} { r } { { \mathcal { L } } = \frac { i } { 2 } \Psi ^ { \mathrm { T } } { \mathcal { C } } \gamma ^ { \mu } \partial _ { \mu } \Psi - \frac { 1 } { 2 } m \Psi ^ { \mathrm { T } } { \mathcal { C } } \Psi ~ . } \end{array} \tag{36.42}
	$$
</synced_block>
The equation of motion that follows from this lagrangian is once again the Dirac equation.
We can also recover the Weyl components of a Dirac or Majorana field by means of a suitable projection matrix. Define
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f0afe62c05ff46bcbd673ebda9b1d999">
	$$
	\gamma _ { 5 } \equiv \left( \begin{array} { c c } { { - \delta _ { a } { } ^ { c } } } & { { 0 } } \\{ { 0 } } & { { + \delta ^ { \dot { a } } { } _ { \dot { c } } } } \end{array} \right) \tag{36.43}
	$$
</synced_block>
where the subscript 5 is simply part of the traditional name of this matrix, rather than the value of some index. Then we can define left and right projection matrices
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#65c6858832aa49c4b82690a304f8524d">
	$$
	\begin{array} { c c } { { P _ { \mathrm { L } } \equiv \frac { 1 } { 2 } ( 1 - \gamma _ { 5 } ) = \left( \begin{array} { c c } { { \delta _ { a } ^ { ~ c } } } & { { 0 } } \\{ { 0 } } & { { 0 } } \end{array} \right) , } } \\{ { { } } } & { { { } } } \\{ { P _ { \mathrm { R } } \equiv \frac { 1 } { 2 } ( 1 + \gamma _ { 5 } ) = \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\{ { 0 } } & { { \delta ^ { \dot { a } } { } _ { \dot { c } } } } \end{array} \right) . } } \end{array} \tag{36.44}
	$$
</synced_block>
Thus we have, for a Dirac field,
$$
P _ { \mathrm { { L } } } \Psi = { \binom { \chi _ { c } } { 0 } } ,
$$
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#7909df7c9cdf49bdb9f4d1480503d997">
	$$
	P _ { \mathrm { R } } \Psi = { \binom { 0 } { \xi ^ { \dagger { \dot { c } } } } } . \tag{36.45}
	$$
</synced_block>
The matrix $`\gamma _ { 5 }`$ can also be expressed as
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#ac14a05bbdd34cd1bce0dc82efea2aff">
	$$
	\begin{array} { c } { { \gamma _ { 5 } = i \gamma ^ { 0 } \gamma ^ { 1 } \gamma ^ { 2 } \gamma ^ { 3 } } } \\{ { = - \frac { i } { 2 4 } \varepsilon _ { \mu \nu \rho \sigma } \gamma ^ { \mu } \gamma ^ { \nu } \gamma ^ { \rho } \gamma ^ { \sigma } , } } \end{array} \tag{36.46}
	$$
</synced_block>
where $`\varepsilon _ { 0 1 2 3 } = - 1`$ .
Finally, let us consider the behavior of a Dirac or Majorana field under a Lorentz transformation. Recall that left- and right-handed spinor fields transform according to
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#055c6163adf342bcbbead70358313928">
	$$
	\begin{array} { l } { { U ( \Lambda ) ^ { - 1 } \psi _ { a } ( x ) U ( \Lambda ) = L ( \Lambda ) _ { a } { } ^ { c } \psi _ { c } ( \Lambda ^ { - 1 } x ) , } } \\{ { { } } } \\{ { U ( \Lambda ) ^ { - 1 } \psi _ { \dot { a } } ^ { \dagger } ( x ) U ( \Lambda ) = R ( \Lambda ) _ { \dot { a } } { } ^ { \dot { c } } \psi _ { \dot { c } } ^ { \dagger } ( \Lambda ^ { - 1 } x ) , } } \end{array} \tag{36.47-36.48}
	$$
</synced_block>
where, for an infinitesimal transformation $`\Lambda ^ { \mu } { } _ { \nu } = \delta ^ { \mu } { } _ { \nu } + \delta \omega ^ { \mu } { } _ { \nu }`$ ,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#902f5d430f62425b88912d5582b44a41">
	$$
	\begin{array} { r } { L ( 1 + \delta \omega ) _ { a } { ^ c } = \delta _ { a } { ^ c } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { ^ c } , } \\{ } \\{ R ( 1 + \delta \omega ) _ { \dot { a } } { ^ \dot { c } } = \delta _ { \dot { a } } { ^ \dot { c } } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S _ { \mathrm { { R } } } ^ { \mu \nu } ) _ { \dot { a } } { ^ \dot { c } } , } \end{array} \tag{36.49-36.50}
	$$
</synced_block>
and where
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#55dcc50f1343490b8d506419a2c4378c">
	$$
	\begin{array} { r c l } { { ( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { } ^ { c } = + \frac { i } { 4 } \big ( \sigma ^ { \mu } \bar { \sigma } ^ { \nu } - \sigma ^ { \nu } \bar { \sigma } ^ { \mu } \big ) _ { a } { } ^ { c } \ , } } \\{ { } } & { { } } \\{ { ( S _ { \mathrm { { R } } } ^ { \mu \nu } ) _ { \dot { c } } ^ { \dot { a } } = - \frac { i } { 4 } \big ( \bar { \sigma } ^ { \mu } \sigma ^ { \nu } - \bar { \sigma } ^ { \nu } \sigma ^ { \mu } \big ) _ { \dot { c } } ^ { \dot { a } } \ . } } \end{array} \tag{36.51-36.52}
	$$
</synced_block>
From these formulae, and the definition of $`\gamma ^ { \mu }`$ , eq. (36.7), we can see that
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#bc3e5736a50849d6b07cc2c642cb371f">
		$$
		\gamma ^ { \mu } \equiv \left( \begin{array} { c c } { { 0 } } & { { \sigma _ { a \dot { c } } ^ { \mu } } } \\{ { \bar { \sigma } ^ { \mu \dot { a } c } } } & { { 0 } } \end{array} \right) . \tag{36.7}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#5b526b2e021945ac88fcfa05c371be20">
	$$
	\begin{array} { r } { \frac { i } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] = \left( \begin{array} { c c } { + ( S _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } { } ^ { c } } & { 0 } \\{ 0 } & { - ( S _ { \mathrm { R } } ^ { \mu \nu } ) ^ { \dot { a } } { } _ { \dot { c } } } \end{array} \right) \equiv S ^ { \mu \nu } . } \end{array} \tag{36.53}
	$$
</synced_block>
Then, for either a Dirac or Majorana field $`\Psi`$ , we can write
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#fa40d4dab22d40209cb59d43bf0120b6">
	$$
	U ( \Lambda ) ^ { - 1 } \Psi ( x ) U ( \Lambda ) = D ( \Lambda ) \Psi ( \Lambda ^ { - 1 } x ) , \tag{36.54}
	$$
</synced_block>
where, for an infinitesimal transformation, the $`4 \times 4`$ matrix $`D ( \Lambda )`$ is
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#fe95d82ef4fb40a49f27aed8afcba9f2">
	$$
	\begin{array} { r } { D ( 1 + \delta \omega ) = 1 + \frac { i } { 2 } \delta \omega _ { \mu \nu } S ^ { \mu \nu } , } \end{array} \tag{36.55, 36.53}
	$$
</synced_block>
with $`S ^ { \mu \nu }`$ given by eq. (36.53). The minus sign in front of $`S _ { \mathrm { { R } } } ^ { \mu \nu }`$ in eq. (36.53) is compensated by the switch from a $`{ \dot { c } } _ { \ \dot { c } }`$ contraction in eq. (36.50) to a $`\dot { c } ^ { \dot { c } }`$ contraction in eq. (36.54).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#fc64bad89ef74a4f9ed2a0a9161882a3">
		$$
		\begin{array} { r } { \frac { i } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] = \left( \begin{array} { c c } { + ( S _ { \mathrm { L } } ^ { \mu \nu } ) _ { a } { } ^ { c } } & { 0 } \\{ 0 } & { - ( S _ { \mathrm { R } } ^ { \mu \nu } ) ^ { \dot { a } } { } _ { \dot { c } } } \end{array} \right) \equiv S ^ { \mu \nu } . } \end{array} \tag{36.53}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f8402648b31c45798203e65768082d66">
		$$
		\begin{array} { r } { L ( 1 + \delta \omega ) _ { a } { ^ c } = \delta _ { a } { ^ c } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S _ { \mathrm { { L } } } ^ { \mu \nu } ) _ { a } { ^ c } , } \\{ } \\{ R ( 1 + \delta \omega ) _ { \dot { a } } { ^ \dot { c } } = \delta _ { \dot { a } } { ^ \dot { c } } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S _ { \mathrm { { R } } } ^ { \mu \nu } ) _ { \dot { a } } { ^ \dot { c } } , } \end{array} \tag{36.49-36.50}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f124310112754d82a7d6bfd6ca61f02a">
		$$
		U ( \Lambda ) ^ { - 1 } \Psi ( x ) U ( \Lambda ) = D ( \Lambda ) \Psi ( \Lambda ^ { - 1 } x ) , \tag{36.54}
		$$
	</synced_block>
</callout>
## Problems
### 36.1
Using the results of problem 2.9, show that, for a rotation by an angle $`\theta`$ about the $`z`$ axis, we have
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#5071318105454328beed7e238e6d97f3">
	$$
	D ( \Lambda ) = \exp ( - i \theta S ^ { 1 2 } ) , \tag{36.56}
	$$
</synced_block>
and that, for a boost by rapidity $`\eta`$ in the $`z`$ direction, we have
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#ddaeb8a9562d43438206e943d6aebe83">
	$$
	D ( \Lambda ) = \exp ( + i \eta S ^ { 3 0 } ) . \tag{36.57}
	$$
</synced_block>
### 36.2
Verify that eq. (36.46) is consistent with eq. (36.43).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#bf5db895db2e4146af170348a27c1c64">
		$$
		\begin{array} { c } { { \gamma _ { 5 } = i \gamma ^ { 0 } \gamma ^ { 1 } \gamma ^ { 2 } \gamma ^ { 3 } } } \\{ { = - \frac { i } { 2 4 } \varepsilon _ { \mu \nu \rho \sigma } \gamma ^ { \mu } \gamma ^ { \nu } \gamma ^ { \rho } \gamma ^ { \sigma } , } } \end{array} \tag{36.46}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#d839e15949e04b1a8f21b2bdbec38421">
		$$
		\gamma _ { 5 } \equiv \left( \begin{array} { c c } { { - \delta _ { a } { } ^ { c } } } & { { 0 } } \\{ { 0 } } & { { + \delta ^ { \dot { a } } { } _ { \dot { c } } } } \end{array} \right) \tag{36.43}
		$$
	</synced_block>
</callout>
### 36.3
a) Prove the Fierz identities
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#35d4f06826c24d478938359cac19f462">
	$$
	\begin{array} { l } { { ( \chi _ { 1 } ^ { \dagger } \bar { \sigma } ^ { \mu } \chi _ { 2 } ) ( \chi _ { 3 } ^ { \dagger } \bar { \sigma } _ { \mu } \chi _ { 4 } ) = - 2 ( \chi _ { 1 } ^ { \dagger } \chi _ { 3 } ^ { \dagger } ) ( \chi _ { 2 } \chi _ { 4 } ) \ : , } } \\{ { { } } } \\{ { ( \chi _ { 1 } ^ { \dagger } \bar { \sigma } ^ { \mu } \chi _ { 2 } ) ( \chi _ { 3 } ^ { \dagger } \bar { \sigma } _ { \mu } \chi _ { 4 } ) = ( \chi _ { 1 } ^ { \dagger } \bar { \sigma } ^ { \mu } \chi _ { 4 } ) ( \chi _ { 3 } ^ { \dagger } \bar { \sigma } _ { \mu } \chi _ { 2 } ) \ : . } } \end{array} \tag{36.58-36.59}
	$$
</synced_block>
b) Define the Dirac fields
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#bf94c9cb227b4e9396aea163ef01eb96">
	$$
	\Psi _ { i } \equiv \left( { \begin{array} { c } { { \chi _ { i } } } \\{ { \xi _ { i } ^ { \dagger } } } \end{array} } \right) , \qquad \Psi _ { i } ^ { \mathrm { c } } \equiv \left( { \begin{array} { c } { { \xi _ { i } } } \\{ { \chi _ { i } ^ { \dagger } } } \end{array} } \right) . \tag{36.60}
	$$
</synced_block>
Use eqs. (36.58) and (36.59) to prove the Dirac form of the Fierz identities,
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#0ffaa131c4bf47b2a904ce1fa295e60b">
		$$
		\begin{array} { l } { { ( \chi _ { 1 } ^ { \dagger } \bar { \sigma } ^ { \mu } \chi _ { 2 } ) ( \chi _ { 3 } ^ { \dagger } \bar { \sigma } _ { \mu } \chi _ { 4 } ) = - 2 ( \chi _ { 1 } ^ { \dagger } \chi _ { 3 } ^ { \dagger } ) ( \chi _ { 2 } \chi _ { 4 } ) \ : , } } \\{ { { } } } \\{ { ( \chi _ { 1 } ^ { \dagger } \bar { \sigma } ^ { \mu } \chi _ { 2 } ) ( \chi _ { 3 } ^ { \dagger } \bar { \sigma } _ { \mu } \chi _ { 4 } ) = ( \chi _ { 1 } ^ { \dagger } \bar { \sigma } ^ { \mu } \chi _ { 4 } ) ( \chi _ { 3 } ^ { \dagger } \bar { \sigma } _ { \mu } \chi _ { 2 } ) \ : . } } \end{array} \tag{36.58-36.59}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#46761ae95b5c4a009847ab64be0c7d6d">
	$$
	\begin{array} { r l } & { \bigl ( \overline { { \Psi } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) \bigl ( \overline { { \Psi } } _ { 3 } \gamma _ { \mu } P _ { \mathrm { L } } \Psi _ { 4 } \bigr ) = - 2 \bigl ( \overline { { \Psi } } _ { 1 } P _ { \mathrm { R } } \Psi _ { 3 } ^ { \mathrm { c } } \bigr ) \bigl ( \overline { { \Psi } } _ { 4 } ^ { \mathrm { c } } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) , } \\& { \bigl ( \overline { { \Psi } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) \bigl ( \overline { { \Psi } } _ { 3 } \gamma _ { \mu } P _ { \mathrm { L } } \Psi _ { 4 } \bigr ) = \bigl ( \overline { { \Psi } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 4 } \bigr ) \bigl ( \overline { { \Psi } } _ { 3 } \gamma _ { \mu } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) . } \end{array} \tag{36.61-36.62}
	$$
</synced_block>
c) By writing both sides out in terms of Weyl fields, show that
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#c7c7765b42654a2ca0656956ecd21281">
	$$
	\begin{array} { r c l } { { } } & { { } } & { { \overline { { { \Psi } } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { R } } \Psi _ { 2 } = - \overline { { { \Psi } } } _ { 2 } ^ { \mathrm { c } } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 1 } ^ { \mathrm { c } } , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \overline { { { \Psi } } } _ { 1 } P _ { \mathrm { L } } \Psi _ { 2 } = + \overline { { { \Psi } } } _ { 2 } ^ { \mathrm { c } } P _ { \mathrm { L } } \Psi _ { 1 } ^ { \mathrm { c } } , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \overline { { { \Psi } } } _ { 1 } P _ { \mathrm { R } } \Psi _ { 2 } = + \overline { { { \Psi } } } _ { 2 } ^ { \mathrm { c } } P _ { \mathrm { R } } \Psi _ { 1 } ^ { \mathrm { c } } . } } \end{array} \tag{36.63-36.65}
	$$
</synced_block>
Combining eqs. (36.63)–(36.65) with eqs. (36.61) and (36.62) yields more useful forms of the Fierz identities.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#1b1f51077d9f46019e5577a25362304d">
		$$
		\begin{array} { r c l } { { } } & { { } } & { { \overline { { { \Psi } } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { R } } \Psi _ { 2 } = - \overline { { { \Psi } } } _ { 2 } ^ { \mathrm { c } } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 1 } ^ { \mathrm { c } } , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \overline { { { \Psi } } } _ { 1 } P _ { \mathrm { L } } \Psi _ { 2 } = + \overline { { { \Psi } } } _ { 2 } ^ { \mathrm { c } } P _ { \mathrm { L } } \Psi _ { 1 } ^ { \mathrm { c } } , } } \\{ { } } & { { } } & { { } } \\{ { } } & { { } } & { { \overline { { { \Psi } } } _ { 1 } P _ { \mathrm { R } } \Psi _ { 2 } = + \overline { { { \Psi } } } _ { 2 } ^ { \mathrm { c } } P _ { \mathrm { R } } \Psi _ { 1 } ^ { \mathrm { c } } . } } \end{array} \tag{36.63-36.65}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#a12cd391a6b043f0ab95731a9b34cdeb">
		$$
		\begin{array} { r l } & { \bigl ( \overline { { \Psi } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) \bigl ( \overline { { \Psi } } _ { 3 } \gamma _ { \mu } P _ { \mathrm { L } } \Psi _ { 4 } \bigr ) = - 2 \bigl ( \overline { { \Psi } } _ { 1 } P _ { \mathrm { R } } \Psi _ { 3 } ^ { \mathrm { c } } \bigr ) \bigl ( \overline { { \Psi } } _ { 4 } ^ { \mathrm { c } } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) , } \\& { \bigl ( \overline { { \Psi } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) \bigl ( \overline { { \Psi } } _ { 3 } \gamma _ { \mu } P _ { \mathrm { L } } \Psi _ { 4 } \bigr ) = \bigl ( \overline { { \Psi } } _ { 1 } \gamma ^ { \mu } P _ { \mathrm { L } } \Psi _ { 4 } \bigr ) \bigl ( \overline { { \Psi } } _ { 3 } \gamma _ { \mu } P _ { \mathrm { L } } \Psi _ { 2 } \bigr ) . } \end{array} \tag{36.61-36.62}
		$$
	</synced_block>
</callout>
### 36.4
Consider a field $`\varphi _ { A } ( x )`$ in an unspecified representation of the Lorentz group, indexed by $`A`$ , that obeys
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#48ef5487def24e7698ec224974dfeef2">
	$$
	U ( \Lambda ) ^ { - 1 } \varphi _ { A } ( x ) U ( \Lambda ) = L _ { A } { } ^ { B } ( \Lambda ) \varphi _ { B } ( \Lambda ^ { - 1 } x ) . \tag{36.66}
	$$
</synced_block>
For an infinitesimal transformation,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#7d944643b91f4d4d891b27879411a53a">
	$$
	\begin{array} { r } { { L _ { A } } ^ { B } ( 1 + \delta \omega ) = { \delta _ { A } } ^ { B } + \frac { i } { 2 } \delta \omega _ { \mu \nu } ( S ^ { \mu \nu } ) _ { A } { } ^ { B } \ . } \end{array} \tag{36.67}
	$$
</synced_block>
a) Following the procedure of section 22, show that the energy-momentum tensor is
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#0f66366734b246398ae5f08cdf52ea2e">
	$$
	T ^ { \mu \nu } = g ^ { \mu \nu } { \mathcal { L } } - { \frac { \partial { \mathcal { L } } } { \partial ( \partial _ { \mu } \varphi _ { A } ) } } \partial ^ { \nu } \varphi _ { A } ~ . \tag{36.68}
	$$
</synced_block>
b) Show that the Noether current corresponding to a Lorentz transformation is
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#c9c7e4ae30a440ce9afbf19b819f4cab">
	$$
	\mathcal { M } ^ { \mu \nu \rho } = x ^ { \nu } T ^ { \mu \rho } - x ^ { \rho } T ^ { \mu \nu } + B ^ { \mu \nu \rho } , \tag{36.69}
	$$
</synced_block>
where
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#8082970fc0bb408faf6da7f5340a0f38">
	$$
	B ^ { \mu \nu \rho } \equiv - i \frac { \partial \mathcal { L } } { \partial ( \partial _ { \mu } \varphi _ { A } ) } ( S ^ { \nu \rho } ) _ { A } { } ^ { B } \varphi _ { B } \ . \tag{36.70}
	$$
</synced_block>
c) Use the conservation laws $`\partial _ { \mu } T ^ { \mu \nu } = 0`$ and $`\partial _ { \mu } { \mathcal { M } } ^ { \mu \nu \rho } = 0`$ to show that
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#46e344d29bf642d6a291c34fb456075b">
	$$
	T ^ { \nu \rho } - T ^ { \rho \nu } + \partial _ { \mu } B ^ { \mu \nu \rho } = 0 . \tag{36.71}
	$$
</synced_block>
d) Define the improved energy-momentum tensor or Belinfante tensor
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#7d70126c53de4ce39fb4bfa799a4aa96">
	$$
	\Theta ^ { \mu \nu } \equiv T ^ { \mu \nu } + { \textstyle \frac { 1 } { 2 } } \partial _ { \rho } \big ( B ^ { \rho \mu \nu } - B ^ { \mu \rho \nu } - B ^ { \nu \rho \mu } \big ) . \tag{36.72}
	$$
</synced_block>
Show that $`\Theta ^ { \mu \nu }`$ is symmetric: $`\Theta ^ { \mu \nu } = \Theta ^ { \nu \mu }`$ . Also show that $`\Theta ^ { \mu \nu }`$ is conserved, $`\partial _ { \mu } \Theta ^ { \mu \nu } = 0`$ , and that $`\begin{array} { r } { \int d ^ { 3 } x \Theta ^ { \upsilon \nu } = \int d ^ { 3 } x T ^ { \upsilon \nu } = P ^ { \nu } } \end{array}`$ , where $`P ^ { \nu }`$ is the energymomentum four-vector. (In general relativity, it is the Belinfante tensor that couples to gravity.)
e) Show that the improved tensor
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#33b4d70d67ae4c2090fe6ee553f05f48">
	$$
	\Xi ^ { \mu \nu \rho } \equiv x ^ { \nu } \Theta ^ { \mu \rho } - x ^ { \rho } \Theta ^ { \mu \nu } \tag{36.73}
	$$
</synced_block>
obeys $`\partial _ { \mu } \Xi ^ { \mu \nu \rho } = 0`$ , and that $`\begin{array} { r } { \int d ^ { 3 } x \Xi ^ { 0 \nu \rho } = \int d ^ { 3 } x \mathcal { M } ^ { 0 \nu \rho } = \mathcal { M } ^ { \nu \rho } } \end{array}`$ , where $`M ^ { \nu \rho }`$ are the Lorentz generators.
f) Compute $`\Theta ^ { \mu \nu }`$ for a left-handed Weyl field with $`\mathcal { L }`$ given by eq. (36.2), and for a Dirac field with $`\mathcal { L }`$ given by eq. (36.28).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#fc7f319441934d7b9c0dcb9bc4195532">
		$$
		\begin{array} { r } { \mathcal { L } = i \psi ^ { \dagger } \bar { \sigma } ^ { \mu } \partial _ { \mu } \psi - \frac { 1 } { 2 } m \psi \psi - \frac { 1 } { 2 } m ^ { * } \psi ^ { \dagger } \psi ^ { \dagger } , } \end{array} \tag{36.2}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f78b8dc60afc4264b70d4a868362e728">
		$$
		{ \mathcal { L } } = i { \overline { { \Psi } } } \gamma ^ { \mu } \partial _ { \mu } \Psi - m { \overline { { \Psi } } } \Psi ~ . \tag{36.28}
		$$
	</synced_block>
</callout>
### 36.5
Symmetries of fermion fields. (Prerequisite: 24.) Consider a theory with $`N`$ massless Weyl fields $`\psi _ { j }`$ ,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f22d69d9a19546489649fa41dc303af0">
	$$
	\mathcal { L } = i \psi _ { j } ^ { \dagger } \sigma ^ { \mu } \partial _ { \mu } \psi _ { j } \ , \tag{36.74}
	$$
</synced_block>
where the repeated index $`j`$ is summed. This lagrangian is clearly invariant under the $`\mathrm { U } ( N )`$ transformation,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#cd3d16d900c1447fb2f8ad2ea0ca4db8">
	$$
	\psi _ { j } U _ { j k } \psi _ { k } ~ , \tag{36.75}
	$$
</synced_block>
where $`U`$ is a unitary matrix. State the invariance group for the following cases:
a) $`N`$ Weyl fields with a common mass $`m`$ ,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#e770290427e2485d90b8d9320a43ee66">
	$$
	\begin{array} { r } { { \mathcal { L } } = i \psi _ { j } ^ { \dagger } \sigma ^ { \mu } \partial _ { \mu } \psi _ { j } - \frac { 1 } { 2 } m ( \psi _ { j } \psi _ { j } + \psi _ { j } ^ { \dagger } \psi _ { j } ^ { \dagger } ) . } \end{array} \tag{36.76}
	$$
</synced_block>
b) $`N`$ massless Majorana fields,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#ccf44a6889784600ac4ab4ba591223c8">
	$$
	\begin{array} { r } { \mathcal { L } = \frac { i } { 2 } \Psi _ { j } ^ { \mathrm { T } } \mathcal { C } \gamma ^ { \mu } \partial _ { \mu } \Psi _ { j } \ . } \end{array} \tag{36.77}
	$$
</synced_block>
c) $`N`$ Majorana fields with a common mass $`m`$ ,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#1ba0fd8c09cb46aaa5feacb7f92bffd1">
	$$
	\begin{array} { r } { \mathcal { L } = \frac { i } { 2 } \Psi _ { j } ^ { \mathrm { T } } \mathcal { C } \gamma ^ { \mu } \partial _ { \mu } \Psi _ { j } - \frac { 1 } { 2 } m \Psi _ { j } ^ { \mathrm { T } } \mathcal { C } \Psi _ { j } } \end{array} . \tag{36.78}
	$$
</synced_block>
d) $`N`$ massless Dirac fields,
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#d89b6bc53ad846c0b9f514c221cf811c">
	$$
	{ \mathcal { L } } = i { \overline { { \Psi } } } _ { j } \gamma ^ { \mu } \partial _ { \mu } \Psi _ { j } \ . \tag{36.79}
	$$
</synced_block>
e) $`N`$ Dirac fields with a common mass $`m`$
<synced_block url="https://app.notion.com/p/b41fbf43fd9247d280fe27cace58ea52#f20e502d80ca471c8eb5d755a0474bcd">
	$$
	{ \mathcal { L } } = i { \overline { { \Psi } } } _ { j } \gamma ^ { \mu } \partial _ { \mu } \Psi _ { j } - m { \overline { { \Psi } } } _ { j } \Psi _ { j } ~ . \tag{36.80}
	$$
</synced_block>
</content>
</page>
