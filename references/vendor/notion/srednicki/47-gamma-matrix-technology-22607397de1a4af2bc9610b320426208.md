Here is the result of "view" for the Page with URL https://app.notion.com/p/22607397de1a4af2bc9610b320426208 as of 2026-04-27T17:30:33.040Z:
<page url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208">
<ancestor-path>
<parent-page url="https://app.notion.com/p/f8967ce7283b4557b4cd9553bc6faae1" title="Part II Spin One Half"/>
<ancestor-2-page url="https://app.notion.com/p/34fee2b74b3f80adaaa4e3113787083b" title="Quantum field theory Srednicki"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"47. Gamma matrix technology"}
</properties>
<content>
Prerequisite: 36
In this section, we will learn some tricks for handling gamma matrices. We need the following information as a starting point:
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#8305df8687d248e2b3b2d46b4a1b4dc9">
	$$
	\begin{array} { c } { { \{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = - 2 g ^ { \mu \nu } , } } \\{ { { } } } \\{ { \gamma _ { 5 } ^ { 2 } = 1 , } } \\{ { { } } } \\{ { \{ \gamma ^ { \mu } , \gamma _ { 5 } \} = 0 , } } \\{ { { } } } \\{ { { \mathrm { T r } 1 = 4 . } } } \end{array} \tag{47.1-47.4}
	$$
</synced_block>
Now consider the trace of the product of $`n`$ gamma matrices. We have
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#bdcd58b498414da1b0939819bb8d5190">
	$$
	\begin{array} { l } { { \mathrm { T r } [ \gamma ^ { \mu _ { 1 } } \ldots \gamma ^ { \mu _ { n } } ] = \mathrm { T r } [ \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { 1 } } \gamma _ { 5 } ^ { 2 } \ldots \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { n } } ] } } \\{ { \ \qquad = \mathrm { T r } [ ( \gamma _ { 5 } \gamma ^ { \mu _ { 1 } } \gamma _ { 5 } ) \ldots ( \gamma _ { 5 } \gamma ^ { \mu _ { n } } \gamma _ { 5 } ) ] } } \\{ { \ \qquad = \mathrm { T r } [ ( - \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { 1 } } ) \ldots ( - \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { n } } ) ] } } \\{ { \ \qquad = ( - 1 ) ^ { n } \mathrm { T r } [ \gamma ^ { \mu _ { 1 } } \ldots \gamma ^ { \mu _ { n } } ] \ . } } \end{array} \tag{47.5}
	$$
</synced_block>
We used eq. (47.2) to get the first equality, the cyclic property of the trace for the second, eq. (47.3) for the third, and eq. (47.2) again for the fourth. If $`n`$ is odd, eq. (47.5) tells us that this trace is equal to minus itself, and must therefore be zero:
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#da6fac2b399d421c83afa69a18b5e950">
		$$
		\begin{array} { c } { { \{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = - 2 g ^ { \mu \nu } , } } \\{ { { } } } \\{ { \gamma _ { 5 } ^ { 2 } = 1 , } } \\{ { { } } } \\{ { \{ \gamma ^ { \mu } , \gamma _ { 5 } \} = 0 , } } \\{ { { } } } \\{ { { \mathrm { T r } 1 = 4 . } } } \end{array} \tag{47.1-47.4}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#8d8975272761454a82bb5c699fe73b23">
		$$
		\begin{array} { l } { { \mathrm { T r } [ \gamma ^ { \mu _ { 1 } } \ldots \gamma ^ { \mu _ { n } } ] = \mathrm { T r } [ \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { 1 } } \gamma _ { 5 } ^ { 2 } \ldots \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { n } } ] } } \\{ { \ \qquad = \mathrm { T r } [ ( \gamma _ { 5 } \gamma ^ { \mu _ { 1 } } \gamma _ { 5 } ) \ldots ( \gamma _ { 5 } \gamma ^ { \mu _ { n } } \gamma _ { 5 } ) ] } } \\{ { \ \qquad = \mathrm { T r } [ ( - \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { 1 } } ) \ldots ( - \gamma _ { 5 } ^ { 2 } \gamma ^ { \mu _ { n } } ) ] } } \\{ { \ \qquad = ( - 1 ) ^ { n } \mathrm { T r } [ \gamma ^ { \mu _ { 1 } } \ldots \gamma ^ { \mu _ { n } } ] \ . } } \end{array} \tag{47.5}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#e0378a14aaf945f4ba213f725538fc67">
	$$
	\mathrm { T r } [ \mathrm { o d d ~ n o . ~ o f } \gamma ^ { \mu } \mathrm { s } ] = 0 . \tag{47.6}
	$$
</synced_block>
Similarly,
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#35658165e567428aa75da62ad67eb78c">
	$$
	\mathrm { T r } [ \gamma _ { 5 } ( \mathrm { o d d ~ n o . ~ o f ~ } \gamma ^ { \mu } \mathrm { s } ) ] = 0 . \tag{47.7}
	$$
</synced_block>
Next, consider $`\operatorname { T r } ( \gamma ^ { \mu } \gamma ^ { \nu } ]`$ . We have
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#235d28a9db2040519cfe11599fb74f8c">
	$$
	{ \begin{array} { r l } & { \operatorname{Tr} [ \gamma ^ { \mu } \gamma ^ { \nu } ] = \operatorname{Tr} [ \gamma ^ { \nu } \gamma ^ { \mu } ] } \\& { \qquad = { \frac { 1 } { 2 } } \operatorname{Tr} [ \gamma ^ { \mu } \gamma ^ { \nu } + \gamma ^ { \nu } \gamma ^ { \mu } ] } \\& { \qquad = - g ^ { \mu \nu } \operatorname{Tr} 1 } \\& { \qquad = - 4 g ^ { \mu \nu } ~ . } \end{array} } \tag{47.8}
	$$
</synced_block>
The first equality follows from the cyclic property of the trace, the second averages the left- and right-hand sides of the first, the third uses eq. (47.1), and the fourth uses eq. (47.4).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#e49f983eb7e64805b52c23ad995ed2a8">
		$$
		\begin{array} { c } { { \{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = - 2 g ^ { \mu \nu } , } } \\{ { { } } } \\{ { \gamma _ { 5 } ^ { 2 } = 1 , } } \\{ { { } } } \\{ { \{ \gamma ^ { \mu } , \gamma _ { 5 } \} = 0 , } } \\{ { { } } } \\{ { { \mathrm { T r } 1 = 4 . } } } \end{array} \tag{47.1-47.4}
		$$
	</synced_block>
</callout>
A slightly nicer way of expressing eq. (47.8) is to introduce two arbitrary four-vectors $`a ^ { \mu }`$ and $`b ^ { \mu }`$ , and write
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#145a32fff2ee412e8a95fcea3e8d04c7">
		$$
		{ \begin{array} { r l } & { \operatorname{Tr} [ \gamma ^ { \mu } \gamma ^ { \nu } ] = \operatorname{Tr} [ \gamma ^ { \nu } \gamma ^ { \mu } ] } \\& { \qquad = { \frac { 1 } { 2 } } \operatorname{Tr} [ \gamma ^ { \mu } \gamma ^ { \nu } + \gamma ^ { \nu } \gamma ^ { \mu } ] } \\& { \qquad = - g ^ { \mu \nu } \operatorname{Tr} 1 } \\& { \qquad = - 4 g ^ { \mu \nu } ~ . } \end{array} } \tag{47.8}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#9615dd502d9e4c7b9f058f7ace97bee4">
	$$
	\mathrm { T r } [ \rlap / \mu \psi ] = - 4 ( a b ) ~ , \tag{47.9}
	$$
</synced_block>
where $`\phi = a _ { \mu } \gamma ^ { \mu }`$ , $`\psi = b _ { \mu } \gamma ^ { \mu }`$ , and $`( a b ) = a ^ { \mu } b _ { \mu }`$
Next consider $`\operatorname { T r } [ \# \not \emptyset \not \phi \not \|`$ . We evaluate this by moving $`\phi`$ to the right, using eq. (47.1), which is now more usefully written as
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#cfc8f55f0c6e44dba758d3c488b0af37">
		$$
		\begin{array} { c } { { \{ \gamma ^ { \mu } , \gamma ^ { \nu } \} = - 2 g ^ { \mu \nu } , } } \\{ { { } } } \\{ { \gamma _ { 5 } ^ { 2 } = 1 , } } \\{ { { } } } \\{ { \{ \gamma ^ { \mu } , \gamma _ { 5 } \} = 0 , } } \\{ { { } } } \\{ { { \mathrm { T r } 1 = 4 . } } } \end{array} \tag{47.1-47.4}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#e8cfd58471824c7b9a91c10174b472f0">
	$$
	\rlap / { a } \psi = - \rlap { / { a } } \psi - 2 ( a b ) ~ . \tag{47.10}
	$$
</synced_block>
Using this repeatedly, we have
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#0bb155ea960c44249b6fd65be984e96d">
	$$
	\begin{array} { r l } & { \mathrm { T r } [ \phi \not \theta \not \varphi \not \theta ] = - \mathrm { T r } [ \not \theta \not \varphi \not \theta \not \theta ] - 2 ( a b ) \mathrm { T r } [ \not \varphi \not \theta ] } \\& { \qquad = + \mathrm { T r } [ \not \theta \not \varphi \not \theta \not \theta ] + 2 ( a c ) \mathrm { T r } [ \not \theta \not \theta ] - 2 ( a b ) \mathrm { T r } [ \not \varphi \not \theta ] } \\& { \qquad = - \mathrm { T r } [ \not \theta \not \varphi \not \theta \not \theta ] - 2 ( a d ) \mathrm { T r } [ \not \theta \not \varphi ] + 2 ( a c ) \mathrm { T r } [ \not \theta \not \theta ] - 2 ( a b ) \mathrm { T r } [ \not \varphi \not \theta ] \ . } \end{array} \tag{47.11}
	$$
</synced_block>
Now we note that the first term on the right-hand side of the last line is, by the cyclic property of the trace, equal to minus the left-hand side. We can then move this term to the left-hand side to get
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#058e8b3c95054cb1bcc7ed466ebbc690">
	$$
	2 \operatorname{Tr} [ \phi \psi \phi \mathscr { A } ] = - 2 ( a d ) \operatorname{Tr} [ \beta \phi ] + 2 ( a c ) \operatorname{Tr} [ \beta \phi ] - 2 ( a b ) \operatorname{Tr} [ \phi \mathscr { A } ] . \tag{47.12}
	$$
</synced_block>
Finally, we evaluate each $`\operatorname { T r } [ \phi \phi ]`$ with eq. (47.9), and divide by two:
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#e01725d86d7e42af9cdb5828ef8a80f1">
		$$
		\mathrm { T r } [ \rlap / \mu \psi ] = - 4 ( a b ) ~ , \tag{47.9}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#b386f41747344782a49a332992448127">
	$$
	\mathrm { T r } [ \rlap / \mu \ r \psi \ne d ] = 4 \Big [ ( a d ) ( b c ) - ( a c ) ( b d ) + ( a b ) ( c d ) \Big ] ~ . \tag{47.13}
	$$
</synced_block>
This is our final result for this trace.
Clearly, we can use the same technique to evaluate the trace of the product of any even number of gamma matrices.
Next, let us consider traces that involve $`\gamma _ { 5 }`$ s and $`\gamma ^ { \mu }`$ s. Since $`\{ \gamma _ { 5 } , \gamma ^ { \mu } \} = 0`$ , we can always bring all the $`\gamma _ { 5 }`$ s together by moving them through the $`\gamma ^ { \mu }`$ s (generating minus signs as we go). Then, since $`\gamma _ { 5 } ^ { 2 } = 1`$ , we end up with either
one $`\gamma _ { 5 }`$ or none. So we need only consider $`\mathrm { T r } [ \gamma _ { 5 } \gamma ^ { \mu _ { 1 } } \ldots \gamma ^ { \mu _ { n } } ]`$ . And, according to eq. (47.7), we need only be concerned with even $`n`$ .
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#dc3863c6060747c5a22ade1a6b95ac7e">
		$$
		\mathrm { T r } [ \gamma _ { 5 } ( \mathrm { o d d ~ n o . ~ o f ~ } \gamma ^ { \mu } \mathrm { s } ) ] = 0 . \tag{47.7}
		$$
	</synced_block>
</callout>
Recall that an explicit formula for $`\gamma _ { 5 }`$ is
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#d4bbceb003514eddb8e6ced1ee72ef1a">
	$$
	\gamma _ { 5 } = i \gamma ^ { 0 } \gamma ^ { 1 } \gamma ^ { 2 } \gamma ^ { 3 } . \tag{47.14}
	$$
</synced_block>
Eq. (47.13) then implies
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#5b5058a0fc8e4108a2fb2e7513a5d7a2">
		$$
		\mathrm { T r } [ \rlap / \mu \ r \psi \ne d ] = 4 \Big [ ( a d ) ( b c ) - ( a c ) ( b d ) + ( a b ) ( c d ) \Big ] ~ . \tag{47.13}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#4915389798214e2e91cd5a825e0ebd5b">
	$$
	{ \mathrm { T r } } \gamma _ { 5 } = 0 ~ . \tag{47.15}
	$$
</synced_block>
Similarly, we can show that
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#be793726d2e9426ab6862919971fe827">
	$$
	\mathrm { T r } [ \gamma _ { 5 } \gamma ^ { \mu } \gamma ^ { \nu } ] = 0 \ . \tag{47.16}
	$$
</synced_block>
Finally, consider $`\operatorname { T r } [ \gamma _ { 5 } \gamma ^ { \mu } \gamma ^ { \nu } \gamma ^ { \rho } \gamma ^ { \sigma } ]`$ . The only way to get a nonzero result is to have the four vector indices take on four different values. If we consider the special case $`\operatorname { T r } [ \gamma _ { 5 } \gamma ^ { 3 } \gamma ^ { 2 } \gamma ^ { 1 } \gamma ^ { 0 } ]`$ , plug in eq. (47.14), and then use $`( \gamma ^ { i } ) ^ { 2 } = - 1`$ and $`( \gamma ^ { 0 } ) ^ { 2 } = 1`$ , we get $`i ( - 1 ) ^ { 3 } \operatorname { T r } 1 = - 4 i`$ , or equivalently
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#68808833c4ea4f319a96e98824ed8eef">
		$$
		\gamma _ { 5 } = i \gamma ^ { 0 } \gamma ^ { 1 } \gamma ^ { 2 } \gamma ^ { 3 } . \tag{47.14}
		$$
	</synced_block>
</callout>
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#2fb2caf21df949d1a3808f4cdbc5870d">
	$$
	\mathrm { T r } [ \gamma _ { 5 } \gamma ^ { \mu } \gamma ^ { \nu } \gamma ^ { \rho } \gamma ^ { \sigma } ] = - 4 i \varepsilon ^ { \mu \nu \rho \sigma } , \tag{47.17}
	$$
</synced_block>
where $`\varepsilon ^ { 0 1 2 3 } = \varepsilon ^ { 3 2 1 0 } = + 1`$
Another category of gamma matrix combinations that we will eventually encounter is $`\gamma ^ { \mu } \phi \ldots \gamma _ { \mu }`$ . The simplest of these is
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#0b48bb9c15c449d0b0bce8eb561040da">
	$$
	\begin{array} { c } { { \gamma ^ { \mu } \gamma _ { \mu } = g _ { \mu \nu } \gamma ^ { \mu } \gamma ^ { \nu } } } \\{ { { } } } \\{ { { } = \frac { 1 } { 2 } g _ { \mu \nu } \{ \gamma ^ { \mu } , \gamma ^ { \nu } \} } } \\{ { { } } } \\{ { { } = - g _ { \mu \nu } g ^ { \mu \nu } } } \\{ { { } } } \\{ { { } = - d . } } \end{array} \tag{47.18}
	$$
</synced_block>
To get the second equality, we used the fact that $`g _ { \mu \nu }`$ is symmetric, and so only the symmetric part of $`\gamma ^ { \mu } \gamma ^ { \nu }`$ contributes. In the last line, $`d`$ is the number of space-time dimensions. Of course, our entire spinor formalism has been built around $`d = 4`$ , but we will need formal results for $`d = 4 - \varepsilon`$ when we dimensionally regulate loop diagrams involving fermions.
We move on to evaluate
$$
\begin{array} { r c l } { { \gamma ^ { \mu } \phi \gamma _ { \mu } = \gamma ^ { \mu } ( - \gamma _ { \mu } \phi - 2 a _ { \mu } ) } } \\{ { } } & { { } } \\{ { } } & { { = - \gamma ^ { \mu } \gamma _ { \mu } \phi - 2 \phi } } \\{ { } } & { { } } & { { } } \\{ { } } & { { = ( d - 2 ) \phi ~ . } } \end{array}
$$
We continue with
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#5fddd24ce1e14b6eb07f5edf0d8838c6">
	$$
	\gamma ^ { \mu } \phi \psi \gamma _ { \mu } = 4 ( a b ) - ( d - 4 ) \phi \psi \tag{47.19-47.20}
	$$
</synced_block>
and
<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#2fdfac7406d043c9879be3293e9a30fd">
	$$
	\gamma ^ { \mu } \phi \psi \phi \gamma _ { \mu } = 2 \phi \psi \phi + ( d \mathrm { - } 4 ) \phi \psi \phi ; \tag{47.21}
	$$
</synced_block>
the derivations are left as an exercise.
## Problems
### 47.1
Verify eq. (47.16).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#8cb1cb65600a46009b58eed8d2a7fb7a">
		$$
		\mathrm { T r } [ \gamma _ { 5 } \gamma ^ { \mu } \gamma ^ { \nu } ] = 0 \ . \tag{47.16}
		$$
	</synced_block>
</callout>
### 47.2
Verify eqs. (47.20) and (47.21).
<callout color="gray_bg">
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#e9001c10c76c4913b4df1483e1313fac">
		$$
		\gamma ^ { \mu } \phi \psi \gamma _ { \mu } = 4 ( a b ) - ( d - 4 ) \phi \psi \tag{47.19-47.20}
		$$
	</synced_block>
	<synced_block url="https://app.notion.com/p/22607397de1a4af2bc9610b320426208#9cb0f2c08a0641939a22c588a165d9ae">
		$$
		\gamma ^ { \mu } \phi \psi \phi \gamma _ { \mu } = 2 \phi \psi \phi + ( d \mathrm { - } 4 ) \phi \psi \phi ; \tag{47.21}
		$$
	</synced_block>
</callout>
### 47.3
Show that the most general $`4 \times 4`$ matrix can be written as a linear combination (with complex coefficients) of $`1`$ , $`\gamma ^ { \mu }`$ , $`S ^ { \mu \nu }`$ , $`\gamma ^ { \mu } \gamma _ { 5 }`$ , and $`\gamma _ { 5 }`$ , where $`^ { 1 }`$ is the identity matrix and $`\begin{array} { r } { S ^ { \mu \nu } = \frac { i } { 4 } [ \gamma ^ { \mu } , \gamma ^ { \nu } ] } \end{array}`$ . Hint: if $`A`$ and $`B`$ are two different members of this set, prove linear independence by showing that $`\mathrm { T r } A ^ { \dagger } B = 0`$ vanishes. Then count.
</content>
</page>
