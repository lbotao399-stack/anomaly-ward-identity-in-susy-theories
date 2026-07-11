Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580 as of 2026-06-30T05:44:29.481Z:
<page url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.4 含有手征超场的可重整规范理论"}
</properties>
<content>
我们现在将前三节装配的零件放在一起为与一般规范场相互作用的手征超场构造最一般的可重整作用量.
将(27.1.27), (27.2.7), (27.3.1)和方程(26.4.5)中的超势项加在一起给出拉格朗日密度
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81208a08d9c871455713">
		$$
		\begin{array} { r l } { \displaystyle \frac { 1 } { 2 } \Big [ \Phi ^ { \dagger } \Gamma \Phi \Big ] _ { D } = - \Big [ ( D _ { \mu } \phi ) ^ { \dagger } D ^ { \mu } \phi \Big ] } & { } \\ { \displaystyle - \frac { 1 } { 2 } \Big [ \Big ( \overline { { \psi _ { L } } } \gamma ^ { \mu } D _ { \mu } \psi _ { L } \Big ) \Big ] + \frac { 1 } { 2 } \Big [ \Big ( \overline { { ( D _ { \mu } \psi _ { L } ) } } \gamma ^ { \mu } \psi _ { L } \Big ) \Big ] + \Big [ \mathcal{F} ^ { \dagger } \mathcal{F} \Big ] } & { } \\ { \displaystyle + \mathrm{i} \sqrt { 2 } \Big [ \Big ( \overline { { \psi _ { L } } } t _ { A } \lambda ^ { A } \Big ) \phi \Big ] - \mathrm{i} \sqrt { 2 } \Big [ \phi ^ { \dagger } \Big ( \overline { { \lambda ^ { A } } } t _ { A } \psi _ { L } \Big ) \Big ] } & { } \\ { \displaystyle - D ^ { A } \Big [ \phi ^ { \dagger } t _ { A } \phi \Big ] , } \end{array} \tag{27.1.27}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81fcb6d0c3edb7d1a098">
		$$
		\mathcal{L} _ { \mathrm{FI} } = \xi D , \tag{27.2.7}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81c6869dcba3f32ad343">
		$$
		\mathcal L_{\mathrm{gauge}}
=-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac12D_AD^A.\tag{27.3.1}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
\mathcal L
&=\frac12\left[\Phi^\dagger\exp(-2t_AV^A)\Phi\right]_D
-\frac12\operatorname{Re}[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}
-\frac{g^2\theta}{16\pi^2}\operatorname{Im}[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}\\
&\quad-\xi_A[V^A]_D+2\operatorname{Re}[f]_{\mathcal F}\\
&=-(D_\mu\phi)_n^*(D^\mu\phi)^n-\frac12\bar\psi_n\gamma^\mu(D_\mu\psi)^n+\mathcal F_n^*\mathcal F^n\\
&\quad-\operatorname{Re}\left[\frac{\partial^2 f(\phi)}{\partial\phi^n\partial\phi^m}(\psi_L^{n\mathrm T}\epsilon\psi_L^m)\right]
+2\operatorname{Re}\left[\frac{\partial f(\phi)}{\partial\phi^n}\mathcal F^n\right]\\
&\quad-2\sqrt2\operatorname{Im}\left[(t_A)^n{}_m(\bar\psi_{nL}\lambda^A)\phi^m\right]
+2\sqrt2\operatorname{Im}\left[(t_A)^m{}_n(\bar\psi_R^n\lambda^A)\phi_m^*\right]\\
&\quad-\phi_n^*(t_A)^n{}_m\phi^mD^A-\xi_AD^A+\frac12D_AD^A\\
&\quad-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}-\frac12(\bar\lambda_A\not D\lambda^A)
+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.
\end{aligned}\tag{27.4.1}
$$
这里的 $`f(\phi)`$ 是超势, $`\phi^n`$ (不是 $`\phi_n^*`$) 的规范不变复函数, 而可重整性条件要求这是一个三次多项式; $`\xi^A`$ 是常数, 除非 $`t_A`$ 是 $`U(1)`$ 生成元, 否则规范不变性要求它为零; 规范协变导数是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8173b2d3f36b2c42b028">
	$$
	\begin{aligned}
D_\mu\psi_L&\equiv\partial_\mu\psi_L-\mathrm i t_AV_\mu{}^A\psi_L,\\
D_\mu\phi&\equiv\partial_\mu\phi-\mathrm i t_AV_\mu{}^A\phi,\\
(D_\mu\lambda)^A&=\partial_\mu\lambda^A+C^A{}_{BC}V_\mu{}^B\lambda^C.
\end{aligned}\tag{27.4.2-27.4.4}
	$$
</synced_block>
$`f^A{}_{\mu\nu}`$ 是规范协变的规范场强张量
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81ae8fcbe5b544c10e57">
	$$
	f^A{}_{\mu\nu}=\partial_\mu V_\nu{}^A-\partial_\nu V_\mu{}^A+C^A{}_{BC}V_\mu{}^BV_\nu{}^C.\tag{27.4.5}
	$$
</synced_block>
辅助场以二次型的方式进入拉格朗日量, 且二阶项的系数是与场无关的常数, 所以通过令辅助场等于使得拉格朗日密度稳定的值可以消除它们:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8105bd67c31055dfa635">
	$$
	\begin{aligned}
\mathcal F^n&=-\left(\frac{\partial f(\phi)}{\partial\phi^n}\right)^*,\\
D^A&=\xi^A+\phi_n^*(t^A)^n{}_m\phi^m.
\end{aligned}\tag{27.4.6-27.4.7}
	$$
</synced_block>
把它们代回方程(27.4.1), 拉格朗日密度变成
$$
\mathcal L=-(D_\mu\phi)_n^*(D^\mu\phi)^n
$$
$$
\begin{aligned}
\mathcal L
&=-(D_\mu\phi)_n^*(D^\mu\phi)^n
-\frac12\bar\psi_{nL}\gamma^\mu(D_\mu\psi_L)^n
+\frac12\overline{(D_\mu\psi_L)^n}\gamma^\mu\psi_{nL}\\
&\quad-\frac12\frac{\partial^2 f(\phi)}{\partial\phi^n\partial\phi^m}(\psi_L^{n\mathrm T}\epsilon\psi_L^m)
-\frac12\left(\frac{\partial^2 f(\phi)}{\partial\phi^n\partial\phi^m}\right)^*(\psi_L^{n\mathrm T}\epsilon\psi_L^m)^*\\
&\quad-\frac{\partial f^*(\phi^*)}{\partial\phi_n^*}\frac{\partial f(\phi)}{\partial\phi^n}
+\mathrm i\sqrt2(\bar\psi_{nL}(t_A)^n{}_m\lambda^A)\phi^m
-\mathrm i\sqrt2\phi_n^*(\bar\lambda_A(t_A)^n{}_m\psi_L^m)\\
&\quad-\frac12(\xi_A+\phi_n^*(t_A)^n{}_m\phi^m)(\xi^A+\phi_l^*(t^A)^l{}_k\phi^k)
-\frac14 f^A{}_{\mu\nu}f_A{}^{\mu\nu}
-\frac12(\bar\lambda_A\not D\lambda^A)\\
&\quad+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.
\end{aligned}\tag{27.4.8}
$$
Lorentz 不变性要求场 $`\psi_L^n`$, $`\lambda^A`$ 和 $`f^A{}_{\mu\nu}`$ 的真空期望值为零, $`\phi^n`$ 的树级真空期望值处在势
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f814d862dec14dffeb88d">
	$$
	V(\phi)=\frac{\partial f^*(\phi^*)}{\partial\phi_n^*}\frac{\partial f(\phi)}{\partial\phi^n}
+\frac12(\xi_A+\phi_n^*(t_A)^n{}_m\phi^m)(\xi^A+\phi_l^*(t^A)^l{}_k\phi^k).\tag{27.4.9}
	$$
</synced_block>
的最小值处.
这个势是正的, 所以如果存在场的一组值使得 $`V ( \phi )`$ 为零, 那么这组场值同时自动是势的一个最小值点.
为了使 $`V(\phi)`$ 在某个场值 $`\phi^n=\phi_0^n`$ 处为零, 充要条件是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
	$$
	\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
	$$
</synced_block>
和
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81719b81e55e9d64b822">
	$$
	D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m=0.\tag{27.4.11}
	$$
</synced_block>
由于方程(26.3.15)给出 $`\langle\delta\psi_L^n\rangle_{\mathrm{VAC}}=\sqrt2\langle\mathcal F^n\rangle_{\mathrm{VAC}}\alpha_L`$, 方程(26.2.16)给出 $`\langle\delta\lambda^A\rangle_{\mathrm{VAC}}=\mathrm i\langle D^A\rangle_{\mathrm{VAC}}\gamma_5\alpha`$, 这转而是超对称不自发破缺的充要条件.
这里值得强调一下, 超对称性的自发对称性破缺要比其他对称性更加困难.
对于作用量的绝大多数对称性, 将会存在场构形使得对称性是不破缺的且势是稳定的, 但是, 如果这些构形中没有一个是势的最小值点, 这个对称性还是会自发破缺的.
反过来, 任何超对称的场构形给出的势的值是零, 它必然要比任何非超对称构形的势的值要低, 所以任何超对称场构形的存在将会确保超对称是不破缺的.
我们将在27.6节看到的, 这个结论会超出本节使用的树级近似; 它不被微扰论中任何有限阶的修正影响.
看起来方程(27.4.10)和(27.4.11)给标量场附加了太多的条件以至于不给超势做一些精细调节(fine-tuning)就无法期待有解.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
		$$
		\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81719b81e55e9d64b822">
		$$
		D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m=0.\tag{27.4.11}
		$$
	</synced_block_reference>
</callout>
然而, 对于维度为 $`D`$ 的规范群, 对所有 $`A`$ 和 $`\phi`$ , 超势 $`f ( \phi )`$ 要满足 $`D`$ 个约束
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8127a95bcf4984121d7a">
	$$
	\frac{\partial f(\phi)}{\partial\phi^m}(t_A)^m{}_n\phi^n=0.\tag{27.4.12}
	$$
</synced_block>
因此, 如果 $`\phi`$ 有 $`N`$ 个独立分量, 那么独立条件(27.4.10)的个数是 $`N - D`$ , 而条件(27.4.11)的个数是 $`D`$ , 所以总共只有 $`N`$ 个条件.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
		$$
		\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81719b81e55e9d64b822">
		$$
		D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m=0.\tag{27.4.11}
		$$
	</synced_block_reference>
</callout>
条件的数目等于自由变量的个数, 因此对于一般的超势是很可能找到解的.
事实上, 找到解比找不到解更普遍些.
例如, 对于处在一个半单群的非平庸表示下的手征超场, 我们有 $`\xi^A=0`$, 而 $`f(\phi)`$ 不可能有 $`\phi^n`$ 的线性项, 所以方程(27.4.10)和(27.4.11)在 $`\phi_0^n=0`$ 时均是满足的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
		$$
		\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81719b81e55e9d64b822">
		$$
		D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m=0.\tag{27.4.11}
		$$
	</synced_block_reference>
</callout>
方程(27.4.10)和(27.4.11)可能有其它会破缺规范对称性的解, 但在这样的一个理论中, 超对称不会被破缺, 至少不会在树级近似下被破缺, 而我们将在 27.6 节看到, 它也不会在微扰论的任何阶被破缺.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
		$$
		\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81719b81e55e9d64b822">
		$$
		D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m=0.\tag{27.4.11}
		$$
	</synced_block_reference>
</callout>
更一般地, 很容易看到, 即使规范群有 $`U(1)`$ 因子且即使超势包含规范不变的超场, 假定 Fayet-Iliopoulos 常数 $`\xi^A`$ 都为零, 如果存在一组满足方程(27.4.10)的标量场值 $`\phi_0^n`$, 那么就存在另外一组满足方程(27.4.10)和(27.4.11)的标量场值.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
		$$
		\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81719b81e55e9d64b822">
		$$
		D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m=0.\tag{27.4.11}
		$$
	</synced_block_reference>
</callout>
为了证明这点, 我们注意到, 由于超势 $`f(\phi)`$ 不涉及 $`\phi^*`$, 它不仅在 $`\Lambda^A`$ 是实常数的普通规范变换 $`\phi\to\exp(\mathrm i\Lambda^At_A)\phi`$ 下不变, 而且也在 $`\Lambda^A`$ 是任意复数的变换下不变.
在所有这些变换下, 方程(27.4.10)中的 $`\mathcal F`$-项进行线性变换, 所以如果 $`\phi_0`$ 满足方程(27.4.10), 那么 $`\phi^\Lambda\equiv\exp(\mathrm i\Lambda^At_A)\phi_0`$ 也满足.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
		$$
		\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
		$$
	</synced_block_reference>
</callout>
另一方面, 标量积 $`[\phi^\dagger\phi]`$ 在 $`\Lambda^A`$ 是复数的变换下不是不变的, 但 $`[\phi^{\Lambda\dagger}\phi^\Lambda]`$ 对于复的 $`\Lambda^A`$ 依旧是正实的, 所以它下有界, 因此有一个最小值.
当 $`\xi^A=0`$ 时, $`[\phi^{\Lambda\dagger}\phi^\Lambda]`$ 在最小值处为零这个条件就是 $`\phi^\Lambda`$ 应该满足方程(27.4.11).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81719b81e55e9d64b822">
		$$
		D^A_0=\xi^A+\phi_{0n}^*(t^A)^n{}_m\phi_0^m=0.\tag{27.4.11}
		$$
	</synced_block_reference>
</callout>
我们由此看到, 当没有 Fayet-Ilioupoulous $`D`$ -项时, 规范理论中超对称破不破缺的问题完全就是超势是否允许方程(27.4.10)有解的问题.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a79cedc57b9df0f23a">
		$$
		\mathcal F^n_0=-\left[\frac{\partial f(\phi)}{\partial\phi^n}\right]^*_{\phi=\phi_0}=0.\tag{27.4.10}
		$$
	</synced_block_reference>
</callout>
相同的结论即使在不可重整理论中也是成立的.\[3\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- S. Weinberg, Phys. Rev. Lett. 80, 3702 (1998)
</callout>
现在我们假定存在一组值 $`\phi_0^n`$ 使得 $`V(\phi_0)=0`$, 使得超对称性是不破缺的.
描述自旋 0自由度的是偏移场
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81469caee4b349786279">
	$$
	\varphi^n=\phi^n-\phi_0^n.\tag{27.4.13}
	$$
</synced_block>
那么就存在 $`\varphi`$ 和规范场之间的交叉项, 来源于方程(27.4.1)中的第一项:
$$
2\operatorname{Im}\left[\partial_\mu\varphi^n\bigl((t_A\phi_0)_n\bigr)^*\right]V^{A\mu}.
$$
正如在21.1节中证明过的, 通过选取一个“幺正规范”总能消除这一项, 在这个规范下, $`\varphi^n`$ 满足一个条件使得这项为零:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8191970bfd34d4c62fb6">
	$$
	\operatorname{Im}\left[\varphi^n\bigl((t_A\phi_0)_n\bigr)^*\right]=0.\tag{27.4.14}
	$$
</synced_block>
这将会消除破缺规范对称性附带的Goldstone 玻色子.
现在, 在超对称性不破缺的前提下, 考虑到规范对称性可能自发破缺的可能性, 我们将解出这个理论中产生的自旋0, $`\frac { 1 } { 2 }`$ 和1粒子的质量.
自旋 0
因为 $`\partial f(\phi)/\partial\phi^n`$ 和 $`\xi^A+\phi_n^*(t^A)^n{}_m\phi^m`$ 必须在 $`\phi^n=\phi_0^n`$ 处都为零, $`V(\phi)`$ 中 $`\varphi^n\equiv\phi^n-\phi_0^n`$ 和(或) $`\varphi_n^*`$ 的二阶项是如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8118bc22c29b60a609f7">
	$$
	\begin{aligned}
V_{\mathrm{quad}}(\phi)
&=\varphi_n^*(\mathcal M^\dagger\mathcal M)^n{}_m\varphi^m
+\varphi_n^*(t_A\phi_0)^n(t^A\phi_0)_m^*\varphi^m\\
&\quad+\frac12(t_A\phi_0)_n^*(t^A\phi_0)_m^*\varphi^n\varphi^m
+\frac12\varphi_n^*\varphi_m^*(t_A\phi_0)^n(t^A\phi_0)^m.
\end{aligned}\tag{27.4.15}
	$$
</synced_block>
其中 $`\mathcal{M}`$ 是复对称矩阵(26.4.11):
$$
\mathcal M_{nm}\equiv\left(\frac{\partial^2f(\phi)}{\partial\phi^n\partial\phi^m}\right)_{\phi=\phi_0}.
$$
这可以写成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81cd896fd61c1fdf5521">
	$$
	V_{\mathrm{quad}}=\frac12
\begin{bmatrix}\varphi\\ \varphi^*\end{bmatrix}^{\dagger}
M_0^2
\begin{bmatrix}\varphi\\ \varphi^*\end{bmatrix}.\tag{27.4.16}
	$$
</synced_block>
其中 $`M _ { 0 } ^ { 2 }`$ 是分块矩阵
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81839e90cb371e3a20e7">
	$$
	M_0^2=\begin{bmatrix}
\mathcal M^*\mathcal M+(t_A\phi_0)(t^A\phi_0)^\dagger & (t_A\phi_0)(t^A\phi_0)^{\mathrm T}\\
(t_A\phi_0)^*(t^A\phi_0)^\dagger & \mathcal M^*\mathcal M+(t_A\phi_0)^*(t^A\phi_0)^{\mathrm T}
\end{bmatrix}.\tag{27.4.17}
	$$
</synced_block>
现在我们必须找到这个质量平方矩阵的本征值.
方程(27.4.12)对 $`\phi^n`$ 的微分给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8127a95bcf4984121d7a">
		$$
		\frac{\partial f(\phi)}{\partial\phi^m}(t_A)^m{}_n\phi^n=0.\tag{27.4.12}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8193bf58e495760c424a">
	$$
	\frac{\partial^2 f(\phi)}{\partial\phi^n\partial\phi^m}(t_A\phi)^m
+\frac{\partial f(\phi)}{\partial\phi^m}(t_A)^m{}_n=0.\tag{27.4.18}
	$$
</synced_block>
但正如我们已经看到的, $`\partial f(\phi)/\partial\phi^m`$ 在 $`\phi=\phi_0`$ 处为零, 所以通过在方程(27.4.18)中令 $`\phi`$ 取在该值处, 我们发现
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8193bf58e495760c424a">
		$$
		\frac{\partial^2 f(\phi)}{\partial\phi^n\partial\phi^m}(t_A\phi)^m
+\frac{\partial f(\phi)}{\partial\phi^m}(t_A)^m{}_n=0.\tag{27.4.18}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a1b998c5255c573d32">
	$$
	\mathcal M_{nm}(t_A\phi_0)^m=0.\tag{27.4.19}
	$$
</synced_block>
由此得出
$$
M_0^2\begin{bmatrix}t_B\phi_0\\ \pm(t_B\phi_0)^*\end{bmatrix}
=\left(\phi_0^\dagger[t_A t_B\pm t_Bt_A]\phi_0\right)
\begin{bmatrix}t_B\phi_0\\ \pm(t_B\phi_0)^*\end{bmatrix}.
$$
但 $`D^A`$ 在 $`\phi=\phi_0`$ 处为零以及 $`\xi^A`$ 的整体规范不变性告诉我们
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81fa8111d34ba0c5ed68">
	$$
	(\phi_0^\dagger[t_A,t_B]\phi_0)
=\mathrm i C_{AB}{}^C(\phi_0^\dagger t_C\phi_0)
=-\mathrm i(\phi_0^\dagger\phi_0)C_{ABC}\xi^C=0.\tag{27.4.20}
	$$
</synced_block>
因此矩阵(27.4.17)对每个规范对称性有一对本征矢量
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81839e90cb371e3a20e7">
		$$
		M_0^2=\begin{bmatrix}
\mathcal M^*\mathcal M+(t_A\phi_0)(t^A\phi_0)^\dagger & (t_A\phi_0)(t^A\phi_0)^{\mathrm T}\\
(t_A\phi_0)^*(t^A\phi_0)^\dagger & \mathcal M^*\mathcal M+(t_A\phi_0)^*(t^A\phi_0)^{\mathrm T}
\end{bmatrix}.\tag{27.4.17}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f815d9699f1c0967a9028">
	$$
	u=\begin{bmatrix}c^Bt_B\phi_0\\ c^B(t_B\phi_0)^*\end{bmatrix},\qquad
v=\begin{bmatrix}c^Bt_B\phi_0\\ -c^B(t_B\phi_0)^*\end{bmatrix}.\tag{27.4.21}
	$$
</synced_block>
对于每个本证矢量
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f816f9e7af520a56446fc">
	$$
	M _ { 0 } ^ { 2 } u = \mu ^ { 2 } u , \qquad M _ { 0 } ^ { 2 } v = 0 , \tag{27.4.22}
	$$
</synced_block>
其中 $`\mu^2`$ 和 $`c^A`$ 是如下本征值问题的实解\*
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f813da1afe328ede1e5a2">
	$$
	(\phi_0^\dagger\{t_A,t_B\}\phi_0)c^B=\mu^2c_A.\tag{27.4.23}
	$$
</synced_block>
这里有一个例外, 如果本征值 $`\mu^2`$ 为零, 那么 $`c^Bt_B\phi_0=0`$, 这使得本征值 $`u`$ 和 $`v`$ 都缺失了.
与本征矢 $`v`$ 相对应的是 Goldstone玻色子, 它们被幺正规范条件(27.4.14)从物理频谱中消除了.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8191970bfd34d4c62fb6">
		$$
		\operatorname{Im}\left[\varphi^n\bigl((t_A\phi_0)_n\bigr)^*\right]=0.\tag{27.4.14}
		$$
	</synced_block_reference>
</callout>
除了这些有质量的本征态外, 还存在另外一组与所有 $`u`$ 和 $`v`$ 都正交的本征态, 因此它们取如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81b7acbbdd300ce0f4e5">
	$$
	w _ { \pm } = \left[ \begin{array} { c } { { \zeta } } \\ { { \pm \zeta ^ { * } } } \end{array} \right] , \tag{27.4.24}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f813e91feeb237b9d4a02">
	$$
	((t_A\phi_0)_n)^*\zeta^n=0.\tag{27.4.25}
	$$
</synced_block>
方程(27.4.19)表明满足方程(27.4.25)的 $`\xi`$ 构成的空间在乘以厄米矩阵 $`\mathcal{M} ^ { \dagger } \mathcal{M}`$ 后是不变的, 所以这个空间由这个矩阵的本征矢张开, 满足
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a1b998c5255c573d32">
		$$
		\mathcal M_{nm}(t_A\phi_0)^m=0.\tag{27.4.19}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f813e91feeb237b9d4a02">
		$$
		((t_A\phi_0)_n)^*\zeta^n=0.\tag{27.4.25}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81d9bd6eed58b6d9564e">
	$$
	{ \mathcal{M} } ^ { \dagger } { \mathcal{M} } \zeta = m ^ { 2 } \zeta \tag{27.4.26}
	$$
</synced_block>
其中 $`m ^ { 2 }`$ 是一组正实的(或零)本征值.
方程(27.4.26)和它的复共轭加上方程(27.4.25)表明 $`w \pm`$ 是 $`M _ { 0 } ^ { 2 }`$ 本征值为 $`m ^ { 2 }`$ 的本征矢:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81d9bd6eed58b6d9564e">
		$$
		{ \mathcal{M} } ^ { \dagger } { \mathcal{M} } \zeta = m ^ { 2 } \zeta \tag{27.4.26}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f813e91feeb237b9d4a02">
		$$
		((t_A\phi_0)_n)^*\zeta^n=0.\tag{27.4.25}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81ddb83ceff3579bf296">
	$$
	M _ { 0 } ^ { 2 } w _ { \pm } = m ^ { 2 } w _ { \pm } . \tag{27.4.27}
	$$
</synced_block>
因此我们有两个满足方程(27.4.27)的质量为 $`m`$ 的自荷共轭无自旋玻色子, 以及对于每个非零质量$`\mu`$ 有一个满足方程(27.4.23)的自荷共轭无自旋玻色子.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81ddb83ceff3579bf296">
		$$
		M _ { 0 } ^ { 2 } w _ { \pm } = m ^ { 2 } w _ { \pm } . \tag{27.4.27}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f813da1afe328ede1e5a2">
		$$
		(\phi_0^\dagger\{t_A,t_B\}\phi_0)c^B=\mu^2c_A.\tag{27.4.23}
		$$
	</synced_block_reference>
</callout>
自旋 1/2
费米子的质量来源于方程(27.4.8)中的非导数项, 它们是费米子场 $`\psi^n`$ 和 $`\lambda^A`$ 的二阶项:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f811fb716cdee861766eb">
	$$
	\mathcal L_{1/2}=-\frac12\mathcal M_{nm}(\psi_L^{n\mathrm T}\epsilon\psi_L^m)
-\mathrm i\sqrt2\,((t_A\phi_0)_m)^*(\lambda_L^{A\mathrm T}\epsilon\psi_L^m)+\mathrm{H.c.}\tag{27.4.28}
	$$
</synced_block>
我们在 26.4 节看到, 对于一列 Majorana 旋量场 $`\chi`$ , 如果拉格朗日量中的费米子质量项写成了如下的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81499374dc93f2c44622">
	$$
	{ \mathcal L } _ { 1 / 2 } = - \frac { 1 } { 2 } \Bigl ( \chi _ { L } ^ { \mathrm { T } } \epsilon M \chi _ { L } \Bigr ) + \mathrm { H . c . } , \tag{27.4.29}
	$$
</synced_block>
那么费米子质量平方是厄米矩阵 $`M ^ { \dagger } M`$ 的本征值.
这里方程(27.4.28)给出的矩阵 $`M`$ 的矩阵元是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f811fb716cdee861766eb">
		$$
		\mathcal L_{1/2}=-\frac12\mathcal M_{nm}(\psi_L^{n\mathrm T}\epsilon\psi_L^m)
-\mathrm i\sqrt2\,((t_A\phi_0)_m)^*(\lambda_L^{A\mathrm T}\epsilon\psi_L^m)+\mathrm{H.c.}\tag{27.4.28}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f819abf34cad914d5b3ef">
	$$
	M_{nm}=\mathcal M_{nm},\qquad M_{nA}=M_{An}=\mathrm i\sqrt2\,((t_A\phi_0)_n)^*,\qquad M_{AB}=0.\tag{27.4.30}
	$$
</synced_block>
对于这组矩阵元, 利用方程(27.4.19)和(27.4.20),
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81a1b998c5255c573d32">
		$$
		\mathcal M_{nm}(t_A\phi_0)^m=0.\tag{27.4.19}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81fa8111d34ba0c5ed68">
		$$
		(\phi_0^\dagger[t_A,t_B]\phi_0)
=\mathrm i C_{AB}{}^C(\phi_0^\dagger t_C\phi_0)
=-\mathrm i(\phi_0^\dagger\phi_0)C_{ABC}\xi^C=0.\tag{27.4.20}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f819bb37fe729d9111001">
	$$
	\begin{aligned}
(M^\dagger M)_{nm}&=(\mathcal M^\dagger\mathcal M)_{nm}+2(t_A\phi_0)_n(t^A\phi_0)_m^*,\\
(M^\dagger M)_{nA}&=(M^\dagger M)_{An}=0,\\
(M^\dagger M)_{AB}&=2(\phi_0^\dagger t_Bt_A\phi_0)=(\phi_0^\dagger\{t_B,t_A\}\phi_0).
\end{aligned}\tag{27.4.31}
	$$
</synced_block>
矩阵(27.4.30)的本征矢有 3 类.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f819abf34cad914d5b3ef">
		$$
		M_{nm}=\mathcal M_{nm},\qquad M_{nA}=M_{An}=\mathrm i\sqrt2\,((t_A\phi_0)_n)^*,\qquad M_{AB}=0.\tag{27.4.30}
		$$
	</synced_block_reference>
</callout>
第一种的形式是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81059c29e0bf076dc2e0">
	$$
	z = \left[ { \zeta \atop 0 } \right] , \tag{27.4.32}
	$$
</synced_block>
本征值是 $`m^2`$, 其中 $`\zeta^n`$ 和 $`m^2`$ 是 $`\mathcal M^\dagger\mathcal M`$ 的任何本征矢量以及相应的本征值.
第二种的形式是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f811198cef6e6d1391ecd">
	$$
	g = { \left[ \begin{array} { l } { 0 } \\ { c } \end{array} \right] } \ , \tag{27.4.33}
	$$
</synced_block>
本征值是 $`\mu^2`$, 其中 $`c^B`$ 和 $`\mu^2`$ 是矩阵 $`(\phi_0^\dagger\{t_B,t_A\}\phi_0)`$ 的任何本征矢量和相应的本征值.
最后一种的形式是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81e09612d39f4976a2dc">
	$$
	h = \left[ \begin{array} { c } { { c ^ { B } t _ { B } \phi _ { 0 } } } \\ { { 0 } } \end{array} \right] \ , \tag{27.4.34}
	$$
</synced_block>
本征值是 $`\mu^2`$, 其中 $`c^B`$ 和 $`\mu^2`$ 依旧是矩阵 $`(\phi_0^\dagger\{t_B,t_A\}\phi_0)`$ 的任何本征矢量和相应的本征值.
唯一的例外是这个矩阵本征值为零的本征矢 $`c`$ 有 $`c^At_A\phi_0=0`$, 对应于未破缺的对称性, 这使得矢量(27.4.34)在这一情况下为零且我们只有本征矢(27.4.33).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81e09612d39f4976a2dc">
		$$
		h = \left[ \begin{array} { c } { { c ^ { B } t _ { B } \phi _ { 0 } } } \\ { { 0 } } \end{array} \right] \ , \tag{27.4.34}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f811198cef6e6d1391ecd">
		$$
		g = { \left[ \begin{array} { l } { 0 } \\ { c } \end{array} \right] } \ , \tag{27.4.33}
		$$
	</synced_block_reference>
</callout>
因此, 对于每个质量 $`m`$ 有一个满足方程(27.4.26)的 Majorana 费米子, 对于每个非零的质量 $`\mu`$ 有两个满足方程(27.4.22)的 Majorana 费米子, 对于每个未破缺的对称性有一个零质量的Majorana费米子.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81d9bd6eed58b6d9564e">
		$$
		{ \mathcal{M} } ^ { \dagger } { \mathcal{M} } \zeta = m ^ { 2 } \zeta \tag{27.4.26}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f816f9e7af520a56446fc">
		$$
		M _ { 0 } ^ { 2 } u = \mu ^ { 2 } u , \qquad M _ { 0 } ^ { 2 } v = 0 , \tag{27.4.22}
		$$
	</synced_block_reference>
</callout>
## 自旋 1
拉格朗日量中规范场的质量项来源于方程(27.4.1)的第一项中规范场 $`V_\mu{}^A`$ 的二阶项部分:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81dc8889e8579a29b9e4">
	$$
	\mathcal L_V=-(t_A\phi_0)_n^*(t_B\phi_0)^nV_\mu{}^AV^{B\mu}.\tag{27.4.35}
	$$
</synced_block>
由于场 $`V_\mu{}^A`$ 是实的, 它们的质量平方矩阵是方程(27.4.23)中的矩阵:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f813da1afe328ede1e5a2">
		$$
		(\phi_0^\dagger\{t_A,t_B\}\phi_0)c^B=\mu^2c_A.\tag{27.4.23}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8186a425e368c38de064">
	$$
	(\mu^2)_{AB}=\phi_0^\dagger\{t_B,t_A\}\phi_0.\tag{27.4.36}
	$$
</synced_block>
对于矩阵(27.4.36)的每个本征值 $`\mu ^ { 2 }`$ 有一个质量为 $`\mu`$ 的自旋 1 粒子.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8186a425e368c38de064">
		$$
		(\mu^2)_{AB}=\phi_0^\dagger\{t_B,t_A\}\phi_0.\tag{27.4.36}
		$$
	</synced_block_reference>
</callout>
将这些放在一起, 我们看到, 对于矩阵 $`\mathcal{M} ^ { \ast } \mathcal{M}`$ 的每个本征值 $`m ^ { 2 }`$ , 存在两个质量为 $`m`$ 的自荷共轭的无自旋粒子和一个质量为 $`m`$ 的 Majorana 费米子; 对于矩阵 $`\mu _ { A B } ^ { 2 }`$ 的每个非零本征值, 存在一个自荷共轭的无自旋玻色子, 两个 Majorana 费米子和一个自荷共轭的自旋1 玻色子, 质量均为 $`\mu`$ ;对于这个矩阵的每个非零本征值, 存在一个无质量的Majorana费米子和一个无质量的自荷共轭的自旋1玻色子.
每个零质量或非零质量的粒子多重态恰好与我们在25.4和25.5节直接用超对称代数发现的相同, 这并不奇怪.
稍微有点让人惊讶的是, 规范粒子和手征粒子的质量彼此不受影响.
由 $`( \mathcal{M} ^ { * } \mathcal{M} )`$ 的本征值给出的质量 $`m`$ 和有这些质量的粒子就是没有规范超场的手征超场理论中的那些粒子和质量, 而由矩阵 $`\mu _ { A B } ^ { 2 }`$ 的本征值给出的质量 $`\mu`$ 和有这些质量的粒子就是没有手征超场的规范超场理论中的那些粒子和质量.
为了在27.9节的使用,我们现在要用26.7节描述的方法来为超对称规范拉格朗日量(27.4.1)构建超对称流.
在之前使用的规范下, 一个无限小超对称变换对 $`V^A`$, $`\lambda^A`$ 和 $`D^A`$ 的改变是(27.3.4)—(27.3.6).
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8137a000c40bda1b2e19">
		$$
		\begin{aligned}
\delta V_\mu{}^A&=(\bar\alpha\gamma_\mu\lambda^A),\\
\delta\lambda^A&=\left(\frac14 f^A{}_{\mu\nu}[\gamma^\nu,\gamma^\mu]+\mathrm i\gamma_5D^A\right)\alpha,\\
\delta D^A&=\mathrm i(\bar\alpha\gamma_5\not\partial\lambda^A).
\end{aligned}\tag{27.3.4-27.3.6}
		$$
	</synced_block_reference>
</callout>
方程(26.7.2)给出了这些场的 Noether 超对称流, 将这些流与已经在方程(26.7.8)中给出的 $`\phi^n,\psi^n`$ 和 $`\mathcal F^n`$ 的流加在一起, 再把导数换成规范协变导数, 这样就给出了总的 Noether 超对称流:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f811babe3dc5b3e86a690">
	$$
	\begin{aligned}
N^\mu
&=f_A{}^{\mu\nu}\gamma_\nu\lambda^A-rac18f_{A\rho\sigma}[\gamma^\rho,\gamma^\sigma]\gamma^\mu\lambda^A-rac{\mathrm i}{2}D_A\gamma_5\gamma^\mu\lambda^A\\
&\quad+\frac1{\sqrt2}\Big[2(D^\mu\phi)_n^*\psi_L^n+2(D^\mu\phi)^n\psi_{nR}+(
ot D\phi)^n\gamma^\mu\psi_{nR}\\
&\qquad\qquad+(
ot D\phi)_n^*\gamma^\mu\psi_L^n-\mathcal F^n\gamma^\mu\psi_{nR}-\mathcal F_n^*\gamma^\mu\psi_L^n\Big].
\end{aligned}\tag{27.4.37}
	$$
</synced_block>
因为拉格朗日密度在超对称下不是不变的, 这不是超对称流; 诚然, 拉格朗日密度的变化是导数
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8169b91ac9cd731fac7d">
	$$
	\delta { \mathcal L } = \partial _ { \mu } \Big ( \bar { \alpha } K ^ { \mu } \Big ) , \tag{27.4.38}
	$$
</synced_block>
其中\\\* \\\*
$$
\begin{aligned}
K^\mu
&=\frac{\mathrm i}{2}\epsilon^{\rho\sigma\mu\nu}f_{A\rho\sigma}\gamma_\nu\gamma_5\lambda^A
+\frac18[\gamma^\rho,\gamma^\sigma]\gamma^\mu\lambda^A f_{A\rho\sigma}
+\frac{\mathrm i}{2}D_A\gamma_5\gamma^\mu\lambda^A\\
&\quad-\mathrm i(t_A)^n{}_m\gamma_5\gamma^\mu\lambda^A\phi_n^*\phi^m\\
&\quad+\frac1{\sqrt2}\gamma^\mu\Big[-(\not D\phi)^n\psi_{nR}-(\not D\phi)_n^*\psi_L^n+\mathcal F_n^*\psi_L^n+\mathcal F^n\psi_{nR}\\
&\qquad+2\frac{\partial f(\phi)}{\partial\phi^n}\psi_L^n+2\left(\frac{\partial f(\phi)}{\partial\phi^n}\right)^*\psi_{nR}\Big].
\end{aligned}\tag{27.4.39}
$$
前两项是用恒等式(27.2.5)导出的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f8198bb8cc4a6cadd48de">
		$$
		\left[ \gamma ^ { \mu } , \gamma ^ { \nu } \right] \gamma ^ { \rho } = - 2 \eta ^ { \mu \rho } \gamma ^ { \nu } + 2 \eta ^ { \nu \rho } \gamma ^ { \mu } - 2 \mathrm{i} \epsilon ^ { \mu \nu \rho \sigma } \gamma _ { \sigma } \gamma _ { 5 } . \tag{27.2.5}
		$$
	</synced_block_reference>
</callout>
再次使用同一个恒等式并使用方程(26.7.4)给出了总的超对称流:
$$
\begin{aligned}
S^\mu&=N^\mu+K^\mu\\
&=-\frac14f_{A\rho\sigma}[\gamma^\rho,\gamma^\sigma]\gamma^\mu\lambda^A
-\mathrm i(t_A)^n{}_m\gamma_5\gamma^\mu\lambda^A\phi_n^*\phi^m\\
&\quad+\frac1{\sqrt2}\Big[(\not D\phi)^n\gamma^\mu\psi_{nR}+(\not D\phi)_n^*\gamma^\mu\psi_L^n
+2\frac{\partial f(\phi)}{\partial\phi^n}\gamma^\mu\psi_L^n\\
&\qquad+2\left(\frac{\partial f(\phi)}{\partial\phi^n}\right)^*\gamma^\mu\psi_{nR}\Big].
\end{aligned}\tag{27.4.40}
$$
\\\*\\\*\\\*
在26.8节, 我们考虑了一类有超势 $`f(\Phi)`$ 和 Kähler 势 $`K(\Phi,\Phi^*)`$ 的超对称理论, 其中 $`f(\Phi)`$ 以任意的方式依赖于一组左手征超场 $`\Phi^n`$ 但与它们的导数无关, 而 $`K(\Phi,\Phi^*)`$ 以任意的方式依赖于 $`\Phi^n`$ 和 $`\Phi_n^*`$ 但与它们的导数无关.
我们可以将相同的考虑推广至规范理论, 其中拉格朗日量对手征超场的依赖性依旧只被超对称形限制, 但不引入新的超导数或时间导数.
这样, 可重整的拉格朗日密度就被替换成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81178992fc4ab2b3b067">
	$$
	\begin{aligned}
\mathcal L
&=\frac12\left[K\left(\Phi,\Phi^\dagger\exp(-2t_AV^A)\right)\right]_D+2\operatorname{Re}[f(\Phi)]_{\mathcal F}\\
&\quad-\frac12\operatorname{Re}\left[h_{AB}(\Phi)(W_L^{A\mathrm T}\epsilon W_L^B)\right]_{\mathcal F}.
\end{aligned}\tag{27.4.41}
	$$
</synced_block>
其中 $`h_{AB}(\Phi)`$ 是 $`\Phi^n`$ 的一个新函数, 但与 $`\Phi_n^*`$ 或导数无关.
手征规范超场和标量规范超场由展开(26.3.21)和(27.3.16)给出:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f813a8364fcffbd288c0c">
		$$
		W^A_L(x,\theta)=\lambda^A_L(x_+)+\frac12\gamma^\mu\gamma^\nu\theta_L f^A{}_{\mu\nu}(x_+)+(\theta_L^{\mathrm T}\epsilon\theta_L)\not D\lambda^A_R(x_+)-\mathrm i\theta_LD^A(x_+).\tag{27.3.16}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
W_L^A(x,\theta)&=\lambda_L^A(x_+)+\frac12\gamma^\mu\gamma^\nu\theta_L f^A{}_{\mu\nu}(x_+)+(\theta_L^{\mathrm T}\epsilon\theta_L)\not D\lambda_R^A(x_+)-\mathrm i\theta_LD^A(x_+),\\
\Phi^n(x,\theta)&=\phi^n(x_+)-\sqrt2(\theta_L^{\mathrm T}\epsilon\psi_L^n(x_+))+\mathcal F^n(x_+)(\theta_L^{\mathrm T}\epsilon\theta_L).
\end{aligned}
$$
其中 $`x_+^\mu`$ 是偏移坐标(26.3.23).
这样, $`h_{AB}(\Phi)(W_L^{A\mathrm T}\epsilon W_L^B)`$ 中 $`\theta_L`$ (与 $`\theta_R`$ 独立)的二阶项就是
$$
-\left[h_{AB}(\Phi)(W_L^{A\mathrm T}\epsilon W_L^B)\right]_{\theta_L^2}
=(\theta_L^{\mathrm T}\epsilon\theta_L)\left\{

\begin{aligned}
& (\lambda_L^{A\mathrm T}\epsilon\lambda_L^B)\left[\frac12(\psi_L^{n\mathrm T}\epsilon\psi_L^m)\frac{\partial^2h_{AB}(\phi)}{\partial\phi^n\partial\phi^m}-\mathcal F^n\frac{\partial h_{AB}(\phi)}{\partial\phi^n}\right]\\
&\quad+h_{AB}(\phi)\left[-(\bar\lambda^A\not D(1-\gamma_5)\lambda^B)-\frac12f^A{}_{\mu\nu}f^{B\mu\nu}+\frac{\mathrm i}{4}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f^{B\rho\sigma}+D^AD^B\right]\\
&\quad+\frac{\sqrt2}{2}\frac{\partial h_{AB}(\phi)}{\partial\phi^n}\left[-(\bar\lambda^B\gamma^\mu\gamma^\nu\psi_L^n)f^A{}_{\mu\nu}+2\mathrm i(\bar\lambda^B\psi_L^n)D^A\right]
\end{aligned}
\right\}.
$$
现在所有场被理解成在 $`x ^ { \mu }`$ 处计算而不是 $`x _ { + } ^ { \mu }`$ .
(右边的第一项和第二项分别取自方程 (26.4.4) 和(27.3.17).) 另外, 通过将 $`\theta _ { L \alpha } \theta _ { L \beta }`$ 写成 $`\frac { 1 } { 2 } \epsilon _ { \alpha \beta } ( \theta _ { L } ^ { \mathrm { T } } \epsilon \theta _ { L } )`$ , 右边第三项也可以表示成正比于 $`( \theta _ { L } ^ { \mathrm { { T } } } \epsilon \theta _ { L } )`$ :
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f815a8faafaca24f0e9c5">
		$$
		\begin{aligned}
-[W_{AL}^{\mathrm T}\epsilon W_L^A]_{\mathcal F}
&=-(\bar\lambda_A\not D(1-\gamma_5)\lambda^A)-\frac12 f^A{}_{\mu\nu}f_A{}^{\mu\nu}\\
&\quad+\frac{\mathrm i}{4}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}+D_AD^A.
\end{aligned}\tag{27.3.17}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
&(\theta_L^{\mathrm T}\epsilon\psi_L^n)\left[(\bar\lambda^B\gamma^\mu\gamma^\nu\theta_L)f^A{}_{\mu\nu}-2\mathrm i(\bar\lambda^B\theta_L)D^A\right]\\
&\qquad=\frac12(\theta_L^{\mathrm T}\epsilon\theta_L)\left[(\bar\lambda^B\gamma^\mu\gamma^\nu\psi_L^n)f^A{}_{\mu\nu}-2\mathrm i(\bar\lambda^B\psi_L^n)D^A\right].
\end{aligned}
$$
$`\mathcal F`$-项是 $`(\theta_L^{\mathrm T}\epsilon\theta_L)`$ 的系数, 所以
$$
-\left[h_{AB}(\Phi)(W_L^{A\mathrm T}\epsilon W_L^B)\right]_{\mathcal F}
=

\begin{aligned}
& (\lambda_L^{A\mathrm T}\epsilon\lambda_L^B)\left[\frac12(\psi_L^{n\mathrm T}\epsilon\psi_L^m)\frac{\partial^2h_{AB}(\phi)}{\partial\phi^n\partial\phi^m}-\mathcal F^n\frac{\partial h_{AB}(\phi)}{\partial\phi^n}\right]\\
&\quad+h_{AB}(\phi)\left[-(\bar\lambda^A\not D(1-\gamma_5)\lambda^B)-\frac12f^A{}_{\mu\nu}f^{B\mu\nu}+\frac{\mathrm i}{4}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f^{B\rho\sigma}+D^AD^B\right]\\
&\quad+\frac{\sqrt2}{2}\frac{\partial h_{AB}(\phi)}{\partial\phi^n}\left[-(\bar\lambda^B\gamma^\mu\gamma^\nu\psi_L^n)f^A{}_{\mu\nu}+2\mathrm i(\bar\lambda^B\psi_L^n)D^A\right]
\end{aligned}
$$
方程(27.4.41)中的另一项正是由拉格朗日密度(26.8.6)的规范不变版本给出.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580#34cee2b74b3f81178992fc4ab2b3b067">
		$$
		\begin{aligned}
\mathcal L
&=\frac12\left[K\left(\Phi,\Phi^\dagger\exp(-2t_AV^A)\right)\right]_D+2\operatorname{Re}[f(\Phi)]_{\mathcal F}\\
&\quad-\frac12\operatorname{Re}\left[h_{AB}(\Phi)(W_L^{A\mathrm T}\epsilon W_L^B)\right]_{\mathcal F}.
\end{aligned}\tag{27.4.41}
		$$
	</synced_block_reference>
</callout>
将这些放在一起就给
出了拉格朗日密度
$$
\begin{aligned}
\mathcal L
&=\operatorname{Re}\,\mathcal G_{nm}(\phi,\phi^*)\left[-\frac12(\bar\psi^m\not D(1+\gamma_5)\psi^n)+\mathcal F_n^*\mathcal F^m-D_\mu\phi^nD^\mu\phi_m^*\right]\\
&\quad-2\operatorname{Re}\left[\frac{\partial K(\phi,\phi^*)}{\partial\phi_i^*}D^A(\phi^*t_A)_i\right]\\
&\quad+\mathrm i\sqrt2\frac{\partial^2K(\phi,\phi^*)}{\partial\phi^i\partial\phi_j^*}\left[(t_A\phi)^i\bar\psi_j\lambda_R^A-(\phi^*t_A)_j\bar\psi^i\lambda_L^A\right]\\
&\quad-\operatorname{Re}\left[\frac{\partial^3K(\phi,\phi^*)}{\partial\phi^n\partial\phi^m\partial\phi_l^*}(\bar\psi^n\psi_L^m)\mathcal F_l^*\right]\\
&\quad+\operatorname{Re}\left[\frac{\partial^3K(\phi,\phi^*)}{\partial\phi^n\partial\phi^m\partial\phi_l^*}(\bar\psi^m\gamma^\mu\psi_{lR})D_\mu\phi^n\right]\\
&\quad+\frac14\frac{\partial^4K(\phi,\phi^*)}{\partial\phi^n\partial\phi^m\partial\phi_l^*\partial\phi_k^*}(\bar\psi^n\psi_L^m)(\bar\psi^k\psi_{lR})\\
&\quad-\operatorname{Re}\left[\frac{\partial^2f(\phi)}{\partial\phi^n\partial\phi^m}(\bar\psi^n\psi_L^m)\right]
+2\operatorname{Re}\left[\mathcal F^n\frac{\partial f(\phi)}{\partial\phi^n}\right]\\
&\quad+\frac14\operatorname{Re}\left[(\bar\lambda^A\lambda_L^B)(\bar\psi^n\psi_L^m)\frac{\partial^2h_{AB}(\phi)}{\partial\phi^n\partial\phi^m}\right]
-\frac12\operatorname{Re}\left[(\bar\lambda^A\lambda_L^B)\mathcal F^n\frac{\partial h_{AB}(\phi)}{\partial\phi^n}\right]\\
&\quad+\operatorname{Re}\left[h_{AB}(\phi)\left(-\bar\lambda^A\not D\lambda_R^B-\frac14f^A{}_{\mu\nu}f^{B\mu\nu}+\frac{\mathrm i}{8}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f^{B\rho\sigma}+\frac12D^AD^B\right)\right]\\
&\quad+\frac{\sqrt2}{4}\operatorname{Re}\left[\frac{\partial h_{AB}(\phi)}{\partial\phi^n}\left(-(\bar\lambda^B\gamma^\mu\gamma^\nu\psi_L^n)f^A{}_{\mu\nu}+2\mathrm i(\bar\lambda^B\psi_L^n)D^A\right)\right].
\end{aligned}\tag{27.4.42}
$$
这个结果的一个有趣特征是, 当超对称性被 $`\mathcal F^n`$ 的一个非零值破缺时, 在含有 $`\phi^n`$ 相关函数 $`h_{AB}(\phi)`$ 的理论中出现了规范微子质量.
在一些引力传递的超对称性破缺的理论中, 这个机制被用于生成规范微子质量, 这些将在31.7节进行讨论.
</content>
</page>
