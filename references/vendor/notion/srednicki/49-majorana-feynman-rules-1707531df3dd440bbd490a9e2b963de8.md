Here is the result of "view" for the Page with URL https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8 as of 2026-04-27T16:53:16.045Z:
<page url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"49. The Feynman rules for Majorana fields"}
</properties>
<content>
In this section we will deduce the Feynman rules for Yukawa theory, but with a Majorana field instead of a Dirac field. We can think of the particles associated with the Majorana field as massive neutrinos.
We have
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#8cae0d3d6a4945c4ba785fcb1ee5d1b2">
	$$
	\begin{array} { r } { \mathcal { L } _ { 1 } = \frac { 1 } { 2 } g \varphi \overline { { \Psi } } \Psi } \\{ = \frac { 1 } { 2 } g \varphi \Psi ^ { \mathrm { T } } \mathcal { C } \Psi \ , } \end{array} \tag{49.1}
	$$
</synced_block>
where $`\Psi`$ is a Majorana field (with mass $`m`$ ), $`\varphi`$ is a real scalar field (with mass $`M`$ ), and $`g`$ is a coupling constant. In this section, we will be concerned with tree-level processes only, and so we omit renormalizing $`Z`$ factors.
From section 41, we have the LSZ rules appropriate for a Majorana field,
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#af806f220d91469e98e08dac99df2beb">
	$$
	b _ { s } ^ { \dagger } ( { \bf p } ) _ { \mathrm { i n } } \longrightarrow - i \int d ^ { 4 } x e ^ { + i p x } { \overline { { v } } } _ { s } ( { \bf p } ) ( - i \emptyset + m ) \Psi ( x ) \tag{49.2}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#f7180983ca1b45449f2be6259f223064">
	$$
	= + i \int d ^ { 4 } x \Psi ^ { \mathrm { T } } ( x ) { \mathcal C } ( + i \overleftarrow { \partial } + m ) u _ { s } ( \mathbf { p } ) e ^ { + i p x } , \tag{49.3}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#2b14926341fc4e359fe7cf6329d121c8">
	$$
	b _ { s ^ { \prime } } ( { \bf p ^ { \prime } } ) _ { \mathrm { o u t } } \longrightarrow + i \int d ^ { 4 } x e ^ { - i p ^ { \prime } x } { \overline { { { u } } } } _ { s ^ { \prime } } ( { \bf p ^ { \prime } } ) ( - i \emptyset + m ) \Psi ( x ) , \tag{49.4}
	$$
</synced_block>
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#bc86f6cb75aa4ddf936462dff2db5896">
	$$
	= - i \int d ^ { 4 } x e ^ { - i p ^ { \prime } x } \Psi ^ { \mathrm { T } } ( x ) \mathcal { C } ( + i \overleftarrow { \partial } + m ) v _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) e ^ { - i p ^ { \prime } x } . \tag{49.5}
	$$
</synced_block>
Eq. (49.3) follows from eq. (49.2) by taking the transpose of the right-hand side, and using $`\overline { { v } } _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) ^ { \mathrm { r } } = - \mathcal { C } u _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } )`$ and $`( - i { \partial { \big / } } + m ) ^ { \mathrm { { r } } } = { \mathcal { C } } ( + i { \partial { \big / } } + m ) { \mathcal { C } } ^ { - 1 }`$ ; similarly, eq. (49.5) follows from eq. (49.4). Which form we use depends on convenience, and is best chosen on a diagram-by-diagram basis, as we will see shortly.
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#a5203de30d1844189c063b81f9c9887a">
		$$
		= + i \int d ^ { 4 } x \Psi ^ { \mathrm { T } } ( x ) { \mathcal C } ( + i \overleftarrow { \partial } + m ) u _ { s } ( \mathbf { p } ) e ^ { + i p x } , \tag{49.3}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#d65556f7d3e74a4f9aceeab552701cb9">
		$$
		b _ { s } ^ { \dagger } ( { \bf p } ) _ { \mathrm { i n } } \longrightarrow - i \int d ^ { 4 } x e ^ { + i p x } { \overline { { v } } } _ { s } ( { \bf p } ) ( - i \emptyset + m ) \Psi ( x ) \tag{49.2}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#0f2097259924474baca8855d82128470">
		$$
		= - i \int d ^ { 4 } x e ^ { - i p ^ { \prime } x } \Psi ^ { \mathrm { T } } ( x ) \mathcal { C } ( + i \overleftarrow { \partial } + m ) v _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) e ^ { - i p ^ { \prime } x } . \tag{49.5}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#409ea653a138413795681219694f2e69">
		$$
		b _ { s ^ { \prime } } ( { \bf p ^ { \prime } } ) _ { \mathrm { o u t } } \longrightarrow + i \int d ^ { 4 } x e ^ { - i p ^ { \prime } x } { \overline { { { u } } } } _ { s ^ { \prime } } ( { \bf p ^ { \prime } } ) ( - i \emptyset + m ) \Psi ( x ) , \tag{49.4}
		$$
	</synced_block>
</callout>
Eqs. (49.2)–(49.5) lead us to compute correlation functions containing $`\Psi`$ ’s, but not $`\overline { { \Psi } } \mathrm { s }`$ . In position space, this leads to Feynman rules where the fermion propagator is $`\begin{array} { r } { \frac { 1 } { i } S ( x - y ) { \mathcal C } ^ { - 1 } } \end{array}`$ , and the $`\varphi \Psi \Psi`$ vertex is $`i g \mathcal { C }`$ ; the factor of $`\begin{array} { l } { { \frac { 1 } { 2 } } } \end{array}`$ in $`\mathcal { L } _ { 1 }`$ is canceled by a symmetry factor of 2! that arises from having two identical $`\Psi`$ fields in $`\mathcal { L } _ { 1 }`$ . In a particular diagram, as we move along a fermion line, the $`{ \mathcal { C } } ^ { - 1 }`$ in the propagator will cancel against the $`\mathcal { C }`$ in the vertex, leaving over a final $`{ \mathcal { C } } ^ { - 1 }`$ at one end. This $`{ \mathcal { C } } ^ { - 1 }`$ can be canceled by a $`\mathcal { C }`$ from eq. (49.3) (for an incoming particle) or eq. (49.5) (for an outgoing particle). On the other hand, for the other end of the same line, we should use either eq. (49.2) (for an incoming particle) or eq. (49.4) (for an outgoing particle) to avoid introducing an extra $`c`$ at that end. In this way, we can avoid ever having explicit factors of $`\mathcal { C }`$ in our Feynman rules.1
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#ef93a91e3735425e9d9b15a6391c6298">
		$$
		b _ { s } ^ { \dagger } ( { \bf p } ) _ { \mathrm { i n } } \longrightarrow - i \int d ^ { 4 } x e ^ { + i p x } { \overline { { v } } } _ { s } ( { \bf p } ) ( - i \emptyset + m ) \Psi ( x ) \tag{49.2}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#76fbf73881e3456499ecae4f1e17467a">
		$$
		= - i \int d ^ { 4 } x e ^ { - i p ^ { \prime } x } \Psi ^ { \mathrm { T } } ( x ) \mathcal { C } ( + i \overleftarrow { \partial } + m ) v _ { s ^ { \prime } } ( \mathbf { p } ^ { \prime } ) e ^ { - i p ^ { \prime } x } . \tag{49.5}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#91e3489cf5bf434ba7c9572a887204fa">
		$$
		= + i \int d ^ { 4 } x \Psi ^ { \mathrm { T } } ( x ) { \mathcal C } ( + i \overleftarrow { \partial } + m ) u _ { s } ( \mathbf { p } ) e ^ { + i p x } , \tag{49.3}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#39505cd31e7241e5b418853ee947dbc6">
		$$
		b _ { s ^ { \prime } } ( { \bf p ^ { \prime } } ) _ { \mathrm { o u t } } \longrightarrow + i \int d ^ { 4 } x e ^ { - i p ^ { \prime } x } { \overline { { { u } } } } _ { s ^ { \prime } } ( { \bf p ^ { \prime } } ) ( - i \emptyset + m ) \Psi ( x ) , \tag{49.4}
		$$
	</synced_block>
</callout>
Using this approach, the Feynman rules for this theory are as follows.
The total number of incoming and outgoing neutrinos is always even; call this number $`2 n`$ . Draw $`n`$ solid lines. Connect them with internal dashed lines, using a vertex that joins one dashed and two solid lines. Also, attach an external dashed line for each incoming or outgoing scalar. In this way, draw all possible diagrams that are topologically inequivalent.<br><br>Draw arrows on each segment of each solid line; keep the arrow direction continuous along each line.<br><br>Label each external dashed line with the momentum of an incoming or outgoing scalar. If the particle is incoming, draw an arrow on the dashed line that points towards the vertex; If the particle is outgoing, draw an arrow on the dashed line that points away from the vertex.<br><br>Label each external solid line with the momentum of an incoming or outgoing neutrino, but include a minus sign with the momentum if (a) the particle is incoming and the arrow points away from the vertex, or (b) the particle is outgoing and the arrow points towards the vertex. Do this labeling of external lines in all possible inequivalent ways. Two diagrams are considered equivalent if they can be transformed into each other by reversing all the arrows on one or more fermion lines, and correspondingly changing the signs of the external momenta on each arrow-reversed line.<br><br>Assign each internal line its own four-momentum. Think of the four-momenta as flowing along the arrows, and conserve four-momentum at each vertex. For a tree diagram, this fixes the momenta on all the internal lines.<br><br>The value of a diagram consists of the following factors: for each incoming or outgoing scalar, 1; for each incoming neutrino labeled with $`+ p _ { i }`$ , $`u _ { s _ { i } } ( \mathbf { p } _ { i } )`$ ; for each incoming neutrino labeled with $`- p _ { i }`$ , $`\overline { { v } } _ { s _ { i } } ( \mathbf { p } _ { i } )`$ ; for each outgoing neutrino labeled with $`+ p _ { i } ^ { \prime }`$ , $`\overline { { u } } _ { s _ { i } ^ { \prime } } ( \mathbf { p } _ { i } ^ { \prime } )`$ ; $`\varphi \longrightarrow \nu \nu`$ for each outgoing neutrino labeled with $`- { p } _ { i } ^ { \prime }`$ , $`v _ { s _ { i } ^ { \prime } } ( \mathbf { p } _ { i } ^ { \prime } )`$ ; for each vertex, $`_ { i g }`$ ; for each internal scalar, $`- i / ( k ^ { 2 } + M ^ { 2 } - i \epsilon )`$ ; for each internal fermion, $`- i ( - p / + m ) / ( p ^ { 2 } + m ^ { 2 } - i \epsilon )`$ .<br><br>Spinor indices are contracted by starting at one end of a fermion line: specifically, the end that has the arrow pointing away from the vertex. The factor associated with the external line is either $`\scriptstyle { \overline { { u } } }`$ or $`\overline { { v } }`$ . Go along the complete fermion line, following the arrows backwards, and writing down (in order from left to right) the factors associated with the vertices and propagators that you encounter. The last factor is either a $`u`$ or a $`v`$ . Repeat this procedure for the other fermion lines, if any.<br><br>The overall sign of a tree diagram is determined by drawing all contributing diagrams in a standard form: all fermion lines horizontal, with their arrows pointing from left to right, and with the left endpoints labeled in the same fixed order (from top to bottom); if the ordering of the labels on the right endpoints of the fermion lines in a given diagram is an even (odd) permutation of an arbitrarily chosen fixed ordering, then the sign of that diagram is positive (negative). To compare two diagrams, it may be necessary to use the arrowreversing equivalence relation of rule no. 4; there is then an extra minus sign for each arrow-reversed line.
![Figure 49.1. Two equivalent diagrams for .](https://prod-files-secure.s3.us-west-2.amazonaws.com/d3aee2b7-4b3f-81c2-8179-00038068497b/22af9a74-827c-4a65-ae7a-4109ceb319f7/00b35044177ab6726fb2d4258e64d144f6c2345e0dc1e1405af87dcbda51cb4c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVCUSC2T%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T033820Z&X-Amz-Expires=300&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BhTJWGqMjjcSh6Uuhi1PSEPuWLtVwgt9KRbhlyTAZQAiEAiKnVTvXM0ztHblRAHzWTA6Bo%2B7qeiPwlYyzSypM0tTwqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXtzD239tLM5iI2ECrcA8UjZjJr06E8SOe7JaMw1%2FEZrSXzthplymKrSjh093a4LoEGnXcgVS353YJ8VnjOhGfpqkySHpHIKT%2FFwSR1BY0I%2B1aTg36Yf6%2FJLz%2F07IECG1ChykXMZHkdomgegJuHKNbbmOUicHVUHkFpD8FecrZBHTDXdjzfz1vvGbAKJ4yOm0Vtn1hSsvwolJhtU1PbrTbSxFncbQIBzXFdUnZHG3l%2F0k5EfLUEiLpoBBi07RdzbWHwf5Cmv%2BIeM5OMib8TIKw6LArfuNtU%2BnakC9ONLWBXeU0Y%2FXCQuXITkjZJY75bNaXhQpXspwdAB%2FwhPicBLcTZmBRcKMs7mHjz0eSWf9172qdYDhnOoPZo2nRos2KOMdozLkwTy8cHLOJwZc0cD6JXDq4uV%2F75SpsudGDdWEQ%2BuKL4%2Bht9YbpeTQkVEj04492XdedDVKjrrwJSac8RXGxViBUgbCVhEAP57EPDzhjEi77p3VcfmdJgfCN%2F6fSUT575uLdY89OXlv%2BheiIlU2adxTVb7qhsT%2FW3i3y82hV0q00zvZ0AJB8kGGimBxD3igb0O5AbhrqQ4ScrNfBxjJW5kpDuoxqKS6rqZPFLyYROxaas1Gng5YAPlVmJ74o3JWFQNCdusq3Bmn1nMLnJxtIGOqUBXCXS%2BTY%2BWIqNH8i5SbHHDFGHmV%2Ba9gv314%2F0zeyWRu79znL%2FjiC9Krwgh4Bv2X%2FbN2DOfsD0ziffO6ugN9mrSj8bMd3h7sVdepD2kdS652za4mUfLQBqJWip4hn61g%2FgzfwRkUgHuRJq4GZ2e2bRUXmv4xfVyxutUERKiYtMf89USsQakKfjQOxuLPERFQAvemvPEP7odVG%2FMJJUKkcEfQUGcQX4&X-Amz-Signature=5745041ae3c934370665c49f6a7ebc1528b08e1709a17a9fc5d15dfa71f964c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The value of $`i T`$ is given by a sum over the values of all these diagrams.
There are additional rules for counterterms and loops, but we will postpone those to section 51.
Let us look at the simplest process, $`\varphi \longrightarrow \nu \nu`$ . There are two possible diagrams for this, shown in fig. 49.1. However, according to rule no. 4, these two diagrams are equivalent, and we should keep only one of them. The first diagram yields $`i T _ { 1 } = i g \overline { { v } } _ { 2 } ^ { \prime } u _ { 1 } ^ { \prime }`$ and the second $`i T _ { 2 } = i g { \overline { { v } } } _ { 1 } ^ { \prime } u _ { 2 } ^ { \prime }`$ . Rule no. 8 then implies that we should have $`T _ { 1 } = - T _ { 2 }`$ . To check this, we note that (after dropping primes to simplify the notation)
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#978df452b09849f7886adc9d54849df0">
	$$
	\begin{array} { r l } & { \overline { { v } } _ { 1 } u _ { 2 } = [ \overline { { v } } _ { 1 } u _ { 2 } ] ^ { \mathrm { r } } } \\& { \qquad = u _ { 2 } ^ { \mathrm { r } } \overline { { v } } _ { 1 } ^ { \mathrm { r } } } \\& { \qquad = \overline { { v } } _ { 2 } \mathcal { C } ^ { - 1 } \mathcal { C } ^ { - 1 } u _ { 1 } } \\& { \qquad = - \overline { { v } } _ { 2 } u _ { 1 } ~ , } \end{array} \tag{49.6}
	$$
</synced_block>
as required.
![Figure 49.2. Diagrams for $`\nu \nu \longrightarrow \nu \nu`$ , corresponding to eq. (49.7).](https://prod-files-secure.s3.us-west-2.amazonaws.com/d3aee2b7-4b3f-81c2-8179-00038068497b/a144ac52-8f21-49b3-acd9-cf3e34835e27/f62afa00aadba2c11f69522f5fab8fa3c725fabd09f9fcf2616700634df0a7e4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVCUSC2T%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T033820Z&X-Amz-Expires=300&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BhTJWGqMjjcSh6Uuhi1PSEPuWLtVwgt9KRbhlyTAZQAiEAiKnVTvXM0ztHblRAHzWTA6Bo%2B7qeiPwlYyzSypM0tTwqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXtzD239tLM5iI2ECrcA8UjZjJr06E8SOe7JaMw1%2FEZrSXzthplymKrSjh093a4LoEGnXcgVS353YJ8VnjOhGfpqkySHpHIKT%2FFwSR1BY0I%2B1aTg36Yf6%2FJLz%2F07IECG1ChykXMZHkdomgegJuHKNbbmOUicHVUHkFpD8FecrZBHTDXdjzfz1vvGbAKJ4yOm0Vtn1hSsvwolJhtU1PbrTbSxFncbQIBzXFdUnZHG3l%2F0k5EfLUEiLpoBBi07RdzbWHwf5Cmv%2BIeM5OMib8TIKw6LArfuNtU%2BnakC9ONLWBXeU0Y%2FXCQuXITkjZJY75bNaXhQpXspwdAB%2FwhPicBLcTZmBRcKMs7mHjz0eSWf9172qdYDhnOoPZo2nRos2KOMdozLkwTy8cHLOJwZc0cD6JXDq4uV%2F75SpsudGDdWEQ%2BuKL4%2Bht9YbpeTQkVEj04492XdedDVKjrrwJSac8RXGxViBUgbCVhEAP57EPDzhjEi77p3VcfmdJgfCN%2F6fSUT575uLdY89OXlv%2BheiIlU2adxTVb7qhsT%2FW3i3y82hV0q00zvZ0AJB8kGGimBxD3igb0O5AbhrqQ4ScrNfBxjJW5kpDuoxqKS6rqZPFLyYROxaas1Gng5YAPlVmJ74o3JWFQNCdusq3Bmn1nMLnJxtIGOqUBXCXS%2BTY%2BWIqNH8i5SbHHDFGHmV%2Ba9gv314%2F0zeyWRu79znL%2FjiC9Krwgh4Bv2X%2FbN2DOfsD0ziffO6ugN9mrSj8bMd3h7sVdepD2kdS652za4mUfLQBqJWip4hn61g%2FgzfwRkUgHuRJq4GZ2e2bRUXmv4xfVyxutUERKiYtMf89USsQakKfjQOxuLPERFQAvemvPEP7odVG%2FMJJUKkcEfQUGcQX4&X-Amz-Signature=8b5f1df91b5194f48ec86531c2a8dbf5e08808db65b6d5481fbea3c2fbcdfb08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In general, for processes with a total of just two incoming and outgoing neutrinos, such as $`\nu \varphi \to \nu \varphi`$ or $`\nu \nu \longrightarrow \varphi \varphi`$ , these rules give (up to an irrelevant overall sign) the same result for $`i T`$ as we would get for the corresponding process in the Dirac case, $`e ^ { - } \varphi e ^ { - } \varphi`$ or $`e ^ { + } e ^ { - } \to \varphi \varphi`$ . (Note, however, that in the Dirac case, we have $`\mathcal { L } _ { 1 } = g \varphi \overline { { \Psi } } \Psi`$ , as compared with $`\begin{array} { r } { \mathcal { L } _ { 1 } = \frac { 1 } { 2 } g \varphi \overline { { \Psi } } \Psi } \end{array}`$ in the Majorana case.)
The differences between Dirac and Majorana fermions become more pronounced for $`\nu \nu \longrightarrow \nu \nu`$ . Now there are three inequivalent contributing diagrams, shown in fig. 49.2. The corresponding amplitude can be written as
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#6fead4ac07e24dad8a56d23b93fc1e45">
	$$
	\begin{array} { r } { i T = \frac { 1 } { i } ( i g ) ^ { 2 } \left[ \frac { ( \overline { { u } } _ { 1 } ^ { \prime } u _ { 1 } ) ( \overline { { u } } _ { 2 } ^ { \prime } u _ { 2 } ) } { - t + M ^ { 2 } } - \frac { ( \overline { { u } } _ { 2 } ^ { \prime } u _ { 1 } ) ( \overline { { u } } _ { 1 } ^ { \prime } u _ { 2 } ) } { - u + M ^ { 2 } } + \frac { ( \overline { { v } } _ { 2 } u _ { 1 } ) ( \overline { { u } } _ { 1 } ^ { \prime } v _ { 2 } ^ { \prime } ) } { - s + M ^ { 2 } } \right] , } \end{array} \tag{49.7}
	$$
</synced_block>
where $`s = - ( p _ { 1 } { + } p _ { 2 } ) ^ { 2 }`$ , $`t = - ( p _ { 1 } - p _ { 1 } ^ { \prime } ) ^ { 2 }`$ and $`u = - ( p _ { 1 } - p _ { 2 } ^ { \prime } ) ^ { 2 }`$ . After arbitrarily assigning the first diagram a plus sign, the minus sign of the second diagram follows from rule no. 8. To get the sign of the third diagram, we compare it with the first. To do so, we reverse the arrow direction on the lower line of the first diagram (which yields an extra minus sign), and then redraw it in standard form. Comparing this modified first diagram with the third diagram (and invoking rule no. 8) reveals a relative minus sign. Since the modified first diagram has a minus sign from the arrow reversal, we conclude that the third diagram has an overall plus sign.
After taking the absolute square of eq. (49.7), we can use relations like eq. (49.6) on a term-by-term basis to put everything into a form that allows the spin sums to be performed in the standard way. In fact, we have already done all the necessary work in the Dirac case. The $`s`$ - $`s`$ , s- $`t`$ , and $`t`$ - $`t`$ terms in $`\langle | \mathcal { T } | ^ { 2 } \rangle`$ for $`\nu \nu \longrightarrow \nu \nu`$ are the same as those for $`e ^ { + } e ^ { - } e ^ { + } e ^ { - }`$ , while the $`t`$ - $`t`$ , $`t`$ - $`u`$ , and $`u`$ - $`u`$ terms are the same as those for the crossing-related process $`e ^ { - } e ^ { - } e ^ { - } e ^ { - }`$ . Finally, the $`s`$ - $`u`$ terms can be obtained from the $`s`$ - $`t`$ terms via $`t u`$ , or equivalently from the $`t`$ - $`u`$ terms via $`t s`$ . Thus the
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#634bfd606e6e4a818f4d43ac938527a4">
		$$
		\begin{array} { r } { i T = \frac { 1 } { i } ( i g ) ^ { 2 } \left[ \frac { ( \overline { { u } } _ { 1 } ^ { \prime } u _ { 1 } ) ( \overline { { u } } _ { 2 } ^ { \prime } u _ { 2 } ) } { - t + M ^ { 2 } } - \frac { ( \overline { { u } } _ { 2 } ^ { \prime } u _ { 1 } ) ( \overline { { u } } _ { 1 } ^ { \prime } u _ { 2 } ) } { - u + M ^ { 2 } } + \frac { ( \overline { { v } } _ { 2 } u _ { 1 } ) ( \overline { { u } } _ { 1 } ^ { \prime } v _ { 2 } ^ { \prime } ) } { - s + M ^ { 2 } } \right] , } \end{array} \tag{49.7}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#2bdad0e8e4594acf85ffb7b4de08d880">
		$$
		\begin{array} { r l } & { \overline { { v } } _ { 1 } u _ { 2 } = [ \overline { { v } } _ { 1 } u _ { 2 } ] ^ { \mathrm { r } } } \\& { \qquad = u _ { 2 } ^ { \mathrm { r } } \overline { { v } } _ { 1 } ^ { \mathrm { r } } } \\& { \qquad = \overline { { v } } _ { 2 } \mathcal { C } ^ { - 1 } \mathcal { C } ^ { - 1 } u _ { 1 } } \\& { \qquad = - \overline { { v } } _ { 2 } u _ { 1 } ~ , } \end{array} \tag{49.6}
		$$
	</synced_block>
</callout>
result is
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#f7f7c8c1f8584bc7acc9bc84a2e2560a">
	$$
	\begin{array} { c } { { \langle | T | ^ { 2 } \rangle = g ^ { 4 } \Bigg [ \frac { ( s - 4 m ^ { 2 } ) ^ { 2 } } { ( M ^ { 2 } - s ) ^ { 2 } } + \frac { s t - 4 m ^ { 2 } u } { ( M ^ { 2 } - s ) ( M ^ { 2 } - t ) } } } \\{ { + \frac { ( t - 4 m ^ { 2 } ) ^ { 2 } } { ( M ^ { 2 } - t ) ^ { 2 } } + \frac { t u - 4 m ^ { 2 } s } { ( M ^ { 2 } - t ) ( M ^ { 2 } - u ) } } } \\{ { + \frac { ( u - 4 m ^ { 2 } ) ^ { 2 } } { ( M ^ { 2 } - u ) ^ { 2 } } + \frac { u s - 4 m ^ { 2 } t } { ( M ^ { 2 } - u ) ( M ^ { 2 } - s ) } \Bigg ] ~ , } } \end{array} \tag{49.8}
	$$
</synced_block>
which is neatly symmetric on permutations of $`s`$ , $`t`$ , and $`u`$ .
## Problems
### 49.1
Let $`\Psi`$ be a Dirac field (representing the electron and positron), $`X`$ be a Majorana field (representing the photino, the hypothetical supersymmetric partner of the photon, with mass $`m _ { \tilde { \gamma } }`$ ), and $`E _ { \mathrm { L } }`$ and $`E _ { \mathrm { R } }`$ be two different complex scalar fields (representing the two selectrons, the hypothetical supersymmetric partners of the left-handed electron and the right-handed electron, with masses $`M _ { \mathrm { L } }`$ , and $`M _ { \mathrm { R } }`$ ; note that the subscripts L and R are just part of their names, and do not signify anything about their Lorentz transformation properties). They interact via
<synced_block url="https://app.notion.com/p/1707531df3dd440bbd490a9e2b963de8#55841b48b742429fb085ed15bf2ca902">
	$$
	\mathcal { L } _ { 1 } = \sqrt { 2 } e E _ { \mathrm { L } } ^ { \dagger } \overline { { { X } } } P _ { \mathrm { L } } \Psi + \sqrt { 2 } e E _ { \mathrm { R } } ^ { \dagger } \overline { { { X } } } P _ { \mathrm { R } } \Psi + \mathrm { h . c . } \ , \tag{49.9}
	$$
</synced_block>
where $`\alpha = e ^ { 2 } / 4 \pi \simeq 1 / 1 3 7`$ is the fine-structure constant, and $`P _ { \mathrm { L , R } } =`$ $`\textstyle { \frac { 1 } { 2 } } ( 1 \mp \gamma _ { 5 } )`$ .
a) Write down the hermitian conjugate term explicitly.<br>b) Find the tree-level scattering amplitude for $`e ^ { + } e ^ { - } \to \tilde { \gamma } \tilde { \gamma }`$ . Hint: there are four contributing diagrams, two each in the $`t`$ and $`u`$ channels, with exchange of either $`E _ { \mathrm { L } }`$ or $`E _ { \mathrm { R } }`$ .<br>c) Compute the spin-averaged differential cross section for this process in the case that $`m _ { e }`$ (the electron mass) can be neglected, and $`| t | , | u | \ll M _ { \mathrm { L } } = M _ { \mathrm { R } }`$ . Express it as a function of $`s`$ and the center-of-mass scattering angle $`\theta`$ .
</content>
</page>
