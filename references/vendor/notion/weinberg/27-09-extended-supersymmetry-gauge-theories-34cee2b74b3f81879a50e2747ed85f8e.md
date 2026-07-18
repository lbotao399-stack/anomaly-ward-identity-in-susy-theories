Here is the result of "view" for the Page with URL https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e as of 2026-07-17T18:57:32.593Z:
<page url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e">
<ancestor-path>
<parent-page url="https://app.notion.com/p/34cee2b74b3f811990e7cea413acedf0" title="第 27 章 超对称规范理论"/>
<ancestor-2-page url="https://app.notion.com/p/310ee2b74b3f8065a3acdbdac27f3b2b" title="量子场论 温伯格"/>
<ancestor-3-page url="https://app.notion.com/p/2fcee2b74b3f80b09e21c456470e4811" title="Theoretical Physics"/>
</ancestor-path>
<properties>
{"title":"27.9 带有扩充超对称性的规范理论"}
</properties>
<content>
因为25.4节讨论过的粒子多重态的非手征性, <span color="yellow_bg">**带有未破缺扩充超对称性的理论被认为不是标准模型的真实扩张的好候选者.**</span>
然而, 由于带有扩充超对称性的规范理论为使用强有力的数学工具解决动力学问题提供了范例, 它们在这里值得考虑一下.
为构造有 $`N = 2`$ 扩充超对称性的拉格朗日量已经提出了数个特殊的形式体系,\[12\] 但幸运的是, 我们可以用已有的工具获得它.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- 首例有 $`N = 2`$ 扩充超对称性的规范理论是 P. Fayet 给出的, Nucl. Phys. B113, 135 (1976);重印于 Supersymmetry, 参考文献\[1\]. 
	- 这里给出的方法与 P. Fayet 的类似. R. Grimm, M.Sohnius 和 J. Scherk 随后给出了超场形式体系, Nucl. Phys. B113, 77 (1977). 
	- 四维时空中的 $`N = 2`$ 和 $`N = 4`$ 超对称规范理论可以通过对高维时空的简单超对称
</callout>
任何带有 $`N \ = \ 2`$ 超对称性的理论同时也有 $`N \ = \ 1`$ 超对称性, 所以它的拉格朗日量必然是本章已经考虑过的拉格朗日量的一个特殊情况.
为了给25.4节和 25.5 节构造的某组 $`N = 2`$ 粒子超多重态构造一个有 $`N = 2`$ 超对称性的拉格朗日量, <span color="yellow_bg">我们只需写下带有 </span>$`N = 1`$<span color="yellow_bg"> 超对称性的最一般拉格朗日量, 要求它的 </span>$`N = 1`$<span color="yellow_bg"> 超多重态包含 </span>$`N = 2`$<span color="yellow_bg"> 超多重态中粒子的场, 然后给这个拉格朗日量附加一个离散的 </span>$`R`$<span color="yellow_bg"> -对称性: 在 </span>$`N = 2`$<span color="yellow_bg"> 超多重态的不同分量上进行不同作用的对称性.</span>
这样拉格朗日量在第二个超对称性也是不变的, 它的超多重态是通过用 $`R`$ -对称性作用在普通 $`N = 1`$ 的超多重态上给出的.
选择离散 $`R`$ -对称性使得
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81b1a6c2cd72d51c86cc">
	$$
	Q_1\to Q_2,\qquad Q_2\to-Q_1.\tag{27.9.1}
	$$
</synced_block>
将是方便的.
如果中心荷是零, 那么超对称代数在一个 $`S U ( 2 ) R`$ -对称群将是不变的, 这个对称群把变换(27.9.1)当做一个有限元 $`\exp ( \frac{1}{2}\mathrm{i} \pi  \tau _ { 2 } )=i\tau_2`$ , 但就我们的目的而言, 离散对称性是足够的, 所以我们无需假定中性荷为零.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81b1a6c2cd72d51c86cc">
		$$
		Q_1\to Q_2,\qquad Q_2\to-Q_1.\tag{27.9.1}
		$$
	</synced_block_reference>
</callout>
事实上, 我们用这个方法构造的拉格朗日量最后将会有一个 $`S U ( 2 )`$ 对称性,而不只是在离散变换(27.9.1)下的对称性.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81b1a6c2cd72d51c86cc">
		$$
		Q_1\to Q_2,\qquad Q_2\to-Q_1.\tag{27.9.1}
		$$
	</synced_block_reference>
</callout>
对于一般规范群的规范玻色子, 连同 $`N \ = \ 2`$ 扩充对称性要求的超对称伙伴, 我们先来考虑它们的可重整理论.
我们在25.4节看到, 在有 $`N \ = \ 2`$ 整体超对称性的理论中, 一个无质量玻色子所属的多重态必须同时含有螺旋度 $`\pm 1 / 2`$ 的无质量费米子各一对以及一对无自旋玻色子, <span color="yellow_bg">前者在 </span>$`S U ( 2 ) R`$<span color="yellow_bg"> -对称性按照双重态变换而后者则是 </span>$`S U ( 2 )`$<span color="yellow_bg"> 单态.</span>
既然 $`N = 2`$ 对称性包含 $`N = 1`$ 对称性, 这个理论的可重整拉格朗日量必然是一般可重整拉格朗日密度(27.4.1)的特殊情况.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#b10bcbaa697a464493ce186b420c124b">
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
	</synced_block_reference>
</callout>
这个特殊情况的一个特征是, 由于规范玻色子属于规范群的伴随表示, 所以费米场和标量也必须属于这个伴随表示.
为了构建含有正确粒子的场的 $`N = 2`$ 的超多重态, 对每个 $`N = 1`$ 规范多重态 $`V_\mu{}^A`$ , $`\lambda^A`$ , $`D^A`$ , 我们必须有一个 $`N = 1`$ 手征超场 $`\Phi^A`$ , 它的分量场是 $`\phi^A`$ , $`\psi^A`$ , $`\mathcal{F}^A`$ (其中 $`\psi^A`$ 是 Majorana 费米子而 $`\phi^A`$ 和 $`\mathcal{F}^A`$ 均是复的).
我们在变换
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f818d90e3ffee23f42a6e">
	$$
	\psi^A\to\lambda^A,\qquad \lambda^A\to-\psi^A\tag{27.9.2}
	$$
</synced_block>
(所有其它场不变)下附加一个离散 $`R`$ -对称性, 这是因为这是变换(27.9.1)的效应.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81b1a6c2cd72d51c86cc">
		$$
		Q_1\to Q_2,\qquad Q_2\to-Q_1.\tag{27.9.1}
		$$
	</synced_block_reference>
</callout>
由于超势给出的 $`\psi^A`$ 的相互作用或质量项是没有 $`\lambda^A`$ 的, 超势必须为零.
拉格朗日量(27.4.1)因此取如下的特殊形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#b10bcbaa697a464493ce186b420c124b">
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
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#aa908f9cb87547248f1e277d9e2e3411">
	$$
	\begin{aligned}
\mathcal L={}&-(D_\mu\phi)^*_A(D^\mu\phi)^A-\frac12\bar{\psi}_A(\not\!D\psi)^A+\mathcal F^*_A\mathcal F^A\\
&-2\sqrt2\operatorname{Re}\,C_{ABC}(\lambda_L^{A\mathrm T}\epsilon\psi_L^C)\phi^{*B}
+\mathrm i\,C_{ABC}\phi^{*B}\phi^C D^A-\xi_A D^A+\frac12D_A D^A\\
&-\frac14 f^A_{\mu\nu}f_A{}^{\mu\nu}-\frac12\bar{\lambda}_A(\not\!D\lambda)^A
+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.
\tag{27.9.3}
\end{aligned}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
												\lambda_L^{A\mathrm T}\!\cdot\psi_L^C
:=
(\lambda_{L,W}^{A})_\alpha(C_W)^{\alpha\beta}
(\psi_{L,W}^{C})_\beta .
	$$
</callout>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f815abb06e86f4d38337e">
	$$
												\begin{aligned}
(D_\mu\psi)^A&=\partial_\mu\psi^A+C_{BC}{}^A V_\mu{}^B\psi^C,\\
(D_\mu\lambda)^A&=\partial_\mu\lambda^A+C_{BC}{}^A V_\mu{}^B\lambda^C,\\
(D_\mu\phi)^A&=\partial_\mu\phi^A+C_{BC}{}^A V_\mu{}^B\phi^C.
\end{aligned}\tag{27.9.4-27.9.6}
	$$
</synced_block>
以及
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f813fb6e1d22b2a2a4d14">
	$$
	f^A_{\mu\nu}=\partial_\mu V_\nu{}^A-\partial_\nu V_\mu{}^A+C_{BC}{}^A V_\mu{}^B V_\nu{}^C.\tag{27.9.7}
	$$
</synced_block>
(回忆在伴随表示下 $`(t_A)_B{}^C=-\mathrm{i}C_{AB}{}^C`$ , 其中 $`C_{ABC}`$ 是实结构常数, 同往常一样在本书中定义成包含规范耦合因子, 并取在使得它自身全反对称的基上.) 
因为拉格朗日密度(27.9.3)是方程(27.4.1)的一个特殊情况, 因此它有多重态为 $`\phi^A`$ , $`\psi^A`$ , $`\mathcal{F}^A`$ 和 $`V_\mu{}^A`$ , $`\lambda^A`$ , $`D^A`$ 的 $`N = 1`$ 超对称性, 并且<span color="yellow_bg">**它还有一个旋转 **</span>$`\psi^A`$<span color="yellow_bg">** 和 **</span>$`\lambda^A`$<span color="yellow_bg">** 的 **</span>$`S U (2)`$<span color="yellow_bg">** 对称性**</span>, 其中包含在有限 $`S U (2)`$ 变换(27.9.2)下的不变性, 所以它还有第二个独立的 $`N = 1`$ 超对称性, 多重态为 $`\phi^A`$ , $`\lambda^A`$ , $`\mathcal{F}^A`$ 和 $`V_\mu{}^A`$ , $`-\psi^A`$ , $`D^A`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#b10bcbaa697a464493ce186b420c124b">
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
	</synced_block_reference>
</callout>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f818d90e3ffee23f42a6e">
		$$
		\psi^A\to\lambda^A,\qquad \lambda^A\to-\psi^A\tag{27.9.2}
		$$
	</synced_block_reference>
</callout>
因此它满足 $`N = 2`$ 超对称性附加的条件.
我们可以通过让辅助场等于使得拉格朗日密度(27.9.3)稳定的值来消除它们:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81f38e67df7621a98d6d">
	$$
	\mathcal F^A=0,\qquad D^A=-\mathrm i\,C^A{}_{BC}\phi^{*B}\phi^C.\tag{27.9.8}
	$$
</synced_block>
(我们现在假定 Fayet–Iliopoulos 常数 $`\xi _ { A }`$ 全为零.) 
将这些值代回方程(27.9.3)将给出一个等价的拉格朗日密度
$$
\begin{aligned}
\mathcal L={}&-(D_\mu\phi)^*_A(D^\mu\phi)^A-\frac12\bar{\psi}_A(\not\!D\psi)^A\\
&+\sqrt2\,C_{ABC}\biggl(\bar{\psi}^B\frac{1-\gamma_5}{2}\lambda^A\biggr)\phi^C
-\sqrt2\,C_{ABC}\biggl(\bar{\lambda}^A\frac{1+\gamma_5}{2}\psi^C\biggr)\phi^{*B}-V(\phi,\phi^*)\\
&-\frac14 f^A_{\mu\nu}f_A{}^{\mu\nu}-\frac12\bar{\lambda}_A(\not\!D\lambda)^A
+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.
\tag{27.9.9}
\end{aligned}
$$
其中势是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8146967ce47c462b8250">
	$$
												V(\phi,\phi^*)=-\frac12\left(C_{ABC}\phi^{*B}\phi^C\right)^2
=2\left(C_{ABC}\operatorname{Re}\phi^B\operatorname{Im}\phi^C\right)^2.\tag{27.9.10}
	$$
</synced_block>
这个势有一个等于零的最小值, 这个最小值不仅能通过对任何一组 $`\phi`$ 令 $`\phi^A=0`$ 得到, 也可以通过要求 $`C_{ABC}\phi^{*B}\phi^C=0`$ 对每个 $`A`$ 成立得到, 或者换一种说法, 令
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f816b8648c65d7e90a046">
	$$
	[t\cdot\operatorname{Re}\phi,t\cdot\operatorname{Im}\phi]=0,\qquad t\cdot v\equiv t_Av^A.\tag{27.9.11}
	$$
</synced_block>
即, 当这些标量场的值使得所有生成元 $`t \cdot \operatorname{Re} \phi`$ 和 $`t \cdot \operatorname{Im} \phi`$ 属于整个规范代数的一个Cartan子代数时, 即所有生成元彼此都对易的子代数, 势取它的最小值.
尽管所有这样的 $`\phi`$ 值都给出零势, 因而也就给出了不破缺的 $`N = 2`$ 对称性, 它们在物理上是不等价的, 例如对于破缺规范对称性附带的规范玻色子, 它们会赋予这些玻色子不同的质量.
扩充超对称性的显著特征之一是, 超对称代数在任何态中的<span color="yellow_bg">中心荷可以用那个态中与玻色场耦合的“荷”计算出来</span>.\[13\] 
进行这个计算的最简单方法是使用扩充超对称流 $`S _ { r } ^ { \mu } ( x )`$ 在普通 $`N = 1`$ 超对称性下的变换性质计算反对易子 $`\{ Q _ { 1 \alpha } , S _ { r \beta } ^ { \mu } ( x ) \}`$ , 其中 $`r = 2 , 3 , \cdots , N`$ .
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- E. Witten and D. Olive, Phys. Lett. 78B, 97 (1978). 另见 H. Osborn, Phys. Lett. 83B, 321(1979)
</callout>
这样我们就能从这个反对易子中计算出中心荷
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f817d903afefc049e12ca">
	$$
	\{ Q _ { 1 \alpha } , Q _ { r \beta } \} = \int \mathrm { d } ^ { 3 } x \left\{ Q _ { 1 \alpha } , S _ { r \beta } ^ { 0 } ( x ) \right\} . \tag{27.9.12}
	$$
</synced_block>
<span color="yellow_bg">右边的被积函数最后表现为一个对时空坐标的导数, 但如果态中有在 </span>$`\mathbf x\to\infty`$<span color="yellow_bg"> 时不快速为零的场,那么这个积分不会为零.</span>
为了细致地看到这是如何运作的, 我们来考虑**有一个 **$`S U ( 2 )`$** 规范对称性**和一个 $`N = 2`$ 规范超多重态但没有额外物质超多重态的 $`N = 2`$ 超对称性.
这里的拉格朗日量由方程(27.9.3)给出, 其中 $`A , B`$ 和 $`C`$ 在1, 2, 3中取值, 并且
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#aa908f9cb87547248f1e277d9e2e3411">
		$$
		\begin{aligned}
\mathcal L={}&-(D_\mu\phi)^*_A(D^\mu\phi)^A-\frac12\bar{\psi}_A(\not\!D\psi)^A+\mathcal F^*_A\mathcal F^A\\
&-2\sqrt2\operatorname{Re}\,C_{ABC}(\lambda_L^{A\mathrm T}\epsilon\psi_L^C)\phi^{*B}
+\mathrm i\,C_{ABC}\phi^{*B}\phi^C D^A-\xi_A D^A+\frac12D_A D^A\\
&-\frac14 f^A_{\mu\nu}f_A{}^{\mu\nu}-\frac12\bar{\lambda}_A(\not\!D\lambda)^A
+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.
\tag{27.9.3}
\end{aligned}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f819d99c0d924b4333bd1">
	$$
	C _ { A B } {} ^ { C } = e \epsilon _ { A B } {} ^ { C } , \xi _ { A } = 0 . \tag{27.9.13}
	$$
</synced_block>
(这里的耦合常数被记做 $`e`$ 是因为它是与**未破缺 **$`U ( 1 )`$** 规范对称性**的无质量规范场相互作用的荷.)
通常的 $`N = 1`$ 超对称流(现在用一个下标1进行区分)由方程(27.4.40)给出
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#fbbbdeb5172347bf8b7b3db0e3756e93">
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
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81f4961fdc34da950811">
	$$
												\begin{aligned}
S_1^\mu={}&-\frac14 f^A_{\rho\sigma}[\gamma^\rho,\gamma^\sigma]\gamma^\mu\lambda^A
-e\,\epsilon_{ABC}\gamma_5\gamma^\mu\lambda^A\phi^{*B}\phi^C\\
&+\frac1{\sqrt2}\left[(\not\!D\phi)_A\gamma^\mu\psi_R^A+(\not\!D\phi^*)_A\gamma^\mu\psi_L^A\right].
\end{aligned}\tag{27.9.14}
	$$
</synced_block>
我们可以通过上面使用的有限 $`S U (2) R`$ -对称性作用 $`S_1^\mu`$ 来计算第二个超对称流, 简单地归结为做替换 $`\psi^A\to\lambda^A`$ , $`\lambda^A\to-\psi^A`$ .
这给出
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8101baf4ec239b5d98f6">
	$$
												\begin{aligned}
S_2^\mu={}&\frac14 f^A_{\rho\sigma}[\gamma^\rho,\gamma^\sigma]\gamma^\mu\psi^A
+e\,\epsilon_{ABC}\gamma_5\gamma^\mu\psi^A\phi^{*B}\phi^C\\
&+\frac1{\sqrt2}\left[(\not\!D\phi)_A\gamma^\mu\lambda_R^A+(\not\!D\phi^*)_A\gamma^\mu\lambda_L^A\right].
\end{aligned}\tag{27.9.15}
	$$
</synced_block>
对我们的目的而言(并且也简单一些), 仅计算这个流的右手部分在一个 $`N = 1`$ 超对称变换下的变化将是足够的.
令辅助场等于它们的平衡值
$$
\mathcal F^A=0,\qquad D^A=-\mathrm i e\,\epsilon^A{}_{BC}\phi^{*B}\phi^C,
$$
我们发现
$$
\begin{aligned}
\delta S_{2R}^\mu={}&\frac{\sqrt2}{4}f^A_{\rho\sigma}[\gamma^\rho,\gamma^\sigma]\gamma^\mu(\not\!D\phi)_A\alpha_R
-\sqrt2 e\,\epsilon^A{}_{BC}\gamma^\mu(\not\!D\phi)_A\alpha_R\phi^{*B}\phi^C\\
&-\frac{\sqrt2}{4}f^A_{\rho\sigma}(\not\!D\phi)_A\gamma^\mu[\gamma^\rho,\gamma^\sigma]\alpha_R
-\sqrt2 e\,\epsilon^A{}_{BC}\phi^{*B}\phi^C(\not\!D\phi)_A\gamma^\mu\alpha_R+\cdots.
\end{aligned}
$$
其中省略号代表费米场的双线性项, 因为我们这里感兴趣的是长程玻色场的效应, 所以并不关心它们.
通过使用Dirac反对易关系和恒等式
$$
\left[ \gamma ^ { \rho } , \gamma ^ { \sigma } \right] \left[ \gamma ^ { \mu } , \gamma ^ { \nu } \right] + \left[ \gamma ^ { \mu } , \gamma ^ { \nu } \right] \left[ \gamma ^ { \rho } , \gamma ^ { \sigma } \right] = - 8 \eta ^ { \mu \rho } \eta ^ { \nu \sigma } + 8 \eta ^ { \sigma \mu } \eta ^ { \rho \nu } + 8 \mathrm{i} \epsilon ^ { \mu \nu \rho \sigma } \gamma _ { 5 }
$$
我们可以组合这些项并发现
$$
\begin{aligned}
\delta S_{2R}^\mu={}&-2\sqrt2\,f^{A\mu\nu}(D_\nu\phi)_A\alpha_R
-\mathrm i\sqrt2\,\epsilon^{\mu\nu\rho\sigma}f^A_{\rho\sigma}(D_\nu\phi)_A\alpha_R\\
&-2\sqrt2 e\,\epsilon^A{}_{BC}\phi^{*B}\phi^C(D^\mu\phi)_A\alpha_R+\cdots.
\end{aligned}
$$
为了将这个写成一个导数, 我们需要方程(15.3.6), (15.3.7)和(15.3.9)给出的 Yang–Mills 场方程:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81a99731e4665a409cb2">
		$$
		D _ { \mu } F _ { \alpha } { } ^ { \mu \nu } = - J _ { \alpha } { } ^ { \nu } \ , \tag{15.3.6}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f812e948af902922b59bd">
		$$
		J _ { \alpha } { } ^ { \nu } \equiv - \mathrm{i} \frac { \partial \mathcal{L} _ { M } } { \partial D _ { \nu } \psi } t _ { \alpha } \psi \ . \tag{15.3.7}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81cb9eb3c5deddb2585b">
		$$
		D _ { \mu } F _ { \alpha \nu \lambda } + D _ { \nu } F _ { \alpha \lambda \mu } + D _ { \lambda } F _ { \alpha \mu \nu } = 0 ~ , \tag{15.3.9}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
\mathcal D_\nu f^{A\mu\nu}=\mathcal J^{A\mu}
&=e\,\epsilon^A{}_{BC}\left((D^\mu\phi)^{*B}\phi^C-\phi^{*B}(D^\mu\phi)^C\right),\\
\epsilon_{\mu\nu\rho\sigma}(D^\nu f^{\rho\sigma})^A&=0.
\end{aligned}
$$
它们使得我们可以将 $`\delta S _ { 2 R } ^ { \mu }`$ 写成一个全导数
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8161af34d33144bb4f70">
	$$
	\delta S _ { 2 R } ^ { \mu } = D _ { \nu } X ^ { \mu \nu } \alpha _ { R } , \tag{27.9.16}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81c2a2d0e9184e0a6adc">
	$$
	X ^ { \mu \nu } = - 2 \sqrt { 2 } f _ { A } ^ { \mu \nu } \phi ^ { A } - \mathrm{i} \sqrt { 2 } \epsilon ^ { \mu \nu \rho \sigma } f _ { A \rho \sigma } \phi ^ { A } + \cdots , \tag{27.9.17}
	$$
</synced_block>
省略号依旧代表包含费米场的无关项.
方程(26.1.18)使得我们可以将方程(27.9.16)写成一个反对易关系
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8144bfa7d9c89936ea83">
		$$
		\mathrm{i} \delta { \mathcal O } ( x ) \equiv \left[ \bar { \alpha } Q , { \mathcal O } ( x ) \right] . \tag{26.1.18}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8161af34d33144bb4f70">
		$$
		\delta S _ { 2 R } ^ { \mu } = D _ { \nu } X ^ { \mu \nu } \alpha _ { R } , \tag{27.9.16}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81f2a8bef4e8b2215061">
	$$
	\Bigl \{ Q _ { R \alpha } , S _ { R \beta } ^ { \mu } \Bigr \} = \mathrm{i} \Bigl [ \epsilon \biggl ( \frac { 1 - \gamma _ { 5 } } { 2 } \biggr ) \Bigr ] _ { \alpha \beta } D _ { \nu } X ^ { \mu \nu } . \tag{27.9.18}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
												P_{R,W}:=\frac{1-\gamma_{5W}}2,
\qquad
(C_WP_{R,W})_{\alpha\beta}
:=
(C_W)_{\alpha\gamma}(P_{R,W})^\gamma{}_{\beta},
	$$
	$$
												\{(Q_{R,W})_\alpha,(S_{R,W}^{\mu})_\beta\}
=
\mathrm i(C_WP_{R,W})_{\alpha\beta}D_\nu X^{\mu\nu}.
	$$
</callout>
由于 $`X ^ { \mu \nu }`$ 是规范不变量, 它的规范协变导数与它的普通导数相同.
另外, $`X ^ { \mu \nu }`$ 是反对称的, 所以 $`D _ { \nu } X ^ { 0 \nu } = \partial _ { i } X ^ { 0 i }`$ .
从方程(27.9.12)和(27.9.16), 我们最后有
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f817d903afefc049e12ca">
		$$
		\{ Q _ { 1 \alpha } , Q _ { r \beta } \} = \int \mathrm { d } ^ { 3 } x \left\{ Q _ { 1 \alpha } , S _ { r \beta } ^ { 0 } ( x ) \right\} . \tag{27.9.12}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8161af34d33144bb4f70">
		$$
		\delta S _ { 2 R } ^ { \mu } = D _ { \nu } X ^ { \mu \nu } \alpha _ { R } , \tag{27.9.16}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f816e8c04fed7206a1caa">
	$$
	\Big \{ Q _ { R \alpha } , Q _ { R \beta } \Big \} = \mathrm{i} \bigg [ \epsilon \bigg ( \frac { 1 - \gamma _ { 5 } } { 2 } \bigg ) \bigg ] _ { \alpha \beta } \int \mathrm { d } S _ { i } X ^ { 0 i } , \tag{27.9.19}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
												\{(Q_{R,W})_\alpha,(Q_{R,W})_\beta\}
=
\mathrm i(C_WP_{R,W})_{\alpha\beta}
\int \mathrm dS_i\,X^{0i},
\qquad
P_{R,W}=\frac{1-\gamma_{5W}}2 .
	$$
</callout>
积分取在一个包裹所考察系统的大闭曲面, 而面积微分 dS 取成曲面的法向.
与方程(25.2.38)比较给出了中心荷
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#a108433b7d114ba6bd3162a3489c9fd7">
		$$
																								\{ Q _ { r } , \overline { Q } _ { s } \}
= - 2 \mathrm { i } P _ { \mu } \gamma ^ { \mu } \delta _ { r s }
+ \left( \frac { 1 + \gamma _ { 5 } } { 2 } \right) Z _ { s r } ^ { * }
+ \left( \frac { 1 - \gamma _ { 5 } } { 2 } \right) Z _ { r s } . \tag{25.2.38}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f818d9d6dc984f26a7bf2">
	$$
	Z _ { 1 2 } = - \mathrm{i} \int \mathrm { d } S _ { i } X ^ { 0 i } . \tag{27.9.20}
	$$
</synced_block>
如果我们选择的规范中 $`\phi^A`$ (几乎处处)只有不为零的常分量 $`\phi^3\equiv v`$ , 那么
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81e7aa64c502d5caf0f2">
	$$
	f _ { A } ^ { 0 i } \phi ^ { A } = - v E ^ { i } , \qquad \frac { 1 } { 2 } \epsilon ^ { 0 i \rho \sigma } f _ { A \rho \sigma } \phi ^ { A } = v B ^ { i } , \tag{27.9.21}
	$$
</synced_block>
其中 $`\mathbf{E}`$ 和 $`\mathbf{B}`$ 是与 $`S U ( 2 )`$ 规范群的未破缺 $`U ( 1 )`$ 子群相联系的电场和磁场.
因此中心荷(27.9.20)在这里是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f818d9d6dc984f26a7bf2">
		$$
		Z _ { 1 2 } = - \mathrm{i} \int \mathrm { d } S _ { i } X ^ { 0 i } . \tag{27.9.20}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f819990a3c7e1f41ce594">
	$$
	Z _ { 1 2 } = 2 \sqrt { 2 } v \left[ \mathrm{i} q - \mathcal{M} \right] , \tag{27.9.22}
	$$
</synced_block>
其中 $`q`$ 和 $`\mathcal{M}`$ 是电荷和磁单极距, 定义成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81d5bb35d0b2f6ed2c41">
	$$
	q = \int \mathrm { d } S _ { i } E ^ { i } , \qquad { \mathcal{M} } = \int \mathrm { d } S _ { i } B ^ { i } . \tag{27.9.23}
	$$
</synced_block>
就像在 23.3 节讨论过的, **这个理论, 其中 **$`S U ( 2 )`$** 规范对称性被一个 **$`S U ( 2 )`$** 三重态标量的期望值自发破缺, 确实有磁单极子.**
将27.4节的结果应用到拉格朗日密度(27.9.3)上表明, 在 $`S U ( 2 )`$ 规范对称性自发破缺之后, 这个理论将会包含电荷为 $`\pm e`$ , 磁单极距为零, 树级近似质量 $`M = { \sqrt { 2 } } | e v |`$ 的基本粒子.
特别地, 对电荷的每一个符号, 有一个自旋 1 的粒子, 两个自旋 $`1 / 2`$ 的, 以及一个自旋 0 的.
这里获得结果的一个显著后果是, 假定 $`v`$ 这个量为中心荷由方程(27.9.22)定义的, 那么质量值 $`\sqrt { 2 } | e v |`$ 是精确的, 不受辐射修正或非微扰效应的影响.\[13\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- E. Witten and D. Olive, Phys. Lett. 78B, 97 (1978). 另见 H. Osborn, Phys. Lett. 83B, 321(1979)
</callout>
为了看到这点, 注意到对电荷的每个符号, 有质量单粒子态是“短” $`N \ = \ 2`$ 超多重态, 而正如 25.5 节末尾证明过的, 它们的质量抵达下界(25.5.24):
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#26b82a4da9c2490fabb0059e56c8f602">
		$$
		M \ge | Z _ { 1 2 } | / 2 . \tag{25.5.24}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8145bd63dae6db5173ff">
	$$
	M = | Z _ { 1 2 } | / 2 . \tag{27.9.24}
	$$
</synced_block>
即使我们不相信树级近似给出粒子质量的精确值, 但我们也无法期待对这个近似的修正会把这个短多重态变成有更多态且质量更大的完整多重态, 所以我们可以确信方程(27.9.24)是精确成立的.对于电荷 $`q = \pm e`$ 且磁单极距为零的粒子, 方程(27.9.20)给出 $`Z _ { 1 2 } = \pm 2 \sqrt { 2 } \mathrm{i} v e`$ , 所以方程(27.9.24)告诉我们它们的质量是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8145bd63dae6db5173ff">
		$$
		M = | Z _ { 1 2 } | / 2 . \tag{27.9.24}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f818d9d6dc984f26a7bf2">
		$$
		Z _ { 1 2 } = - \mathrm{i} \int \mathrm { d } S _ { i } X ^ { 0 i } . \tag{27.9.20}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81c2855fee92debbe339">
	$$
	M = \sqrt { 2 } | e v | . \tag{27.9.25}
	$$
</synced_block>
这是在树级近似下发现的结果, 但现在我们看到它是精确的.
23.3节描述的半经典计算表明这个理论中的电中性磁单极子有磁单极强度
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8112afb9f419487522d4">
	$$
	\mathcal{M} = \frac { 4 \pi \nu } { e } , \tag{27.9.26}
	$$
</synced_block>
其中 $`\nu`$ 是缠绕数, 一个正整数或负整数.
因此中心荷的公式(27.9.22)加上不等式(25.2.24)给出了单极子质量上的下界
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f819990a3c7e1f41ce594">
		$$
		Z _ { 1 2 } = 2 \sqrt { 2 } v \left[ \mathrm{i} q - \mathcal{M} \right] , \tag{27.9.22}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#997fbd23d0684e688ef3ee8bfbdc4395">
		$$
		[ Z _ { r s } , \mathcal{Q} _ { a t } ] = M _ { r s t }{}^{ u } \mathcal{Q} _ { a u } . \tag{25.2.24}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f816aa1f4d8c1b16ae440">
	$$
	M \geq \frac { 4 \pi \sqrt { 2 } \left| \nu v \right| } { \left| e \right| } . \tag{27.9.27}
	$$
</synced_block>
有趣的是, 这与 23.3 节推导过的单极子能量上的 Bogomol’nyi 下界\[13\]相同.† 事实上, 23.3 节描述过的 $`\nu = 1`$ 的单极子解处在这个下界上.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- E. Witten and D. Olive, Phys. Lett. 78B, 97 (1978). 另见 H. Osborn, Phys. Lett. 83B, 321(1979)
</callout>
更一般地, 这个理论的“双荷子”,\[15\] 即既有电荷又有磁矩的粒子, 有质量\[16\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- D. Zwanziger, Phys. Rev. 176, 1480 (1968); J. Schwinger, Phys. Rev. 144, 1087 (1966); 173, 1536 (1968); B. Julia and A. Zee, Phys. Rev. D11, 2227 (1974); F. A. Bais and J. R. Primack, Phys. Rev. D13, 819 (1975). (在卷 II 第一次印刷的版本中, 第 23 章中错误地
	- M. K. Prasad and C. M. Sommerfield, Phys. Rev. Lett. 35, 760 (1975); E. B. Bogomol’nyi, 参考文献\[14\]; S. Coleman, S. Parke, A. Neveu, and C. M. Sommerfield, Phys. Rev. D15, 544 (1977)
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81a5873bc11bdafde286">
	$$
	M = 2 | v | \sqrt { q ^ { 2 } + \mathcal{M} ^ { 2 } } , \tag{27.9.28}
	$$
</synced_block>
这依旧是方程(25.5.24)和(27.9.20)所允许的最小值.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#26b82a4da9c2490fabb0059e56c8f602">
		$$
		M \ge | Z _ { 1 2 } | / 2 . \tag{25.5.24}
		$$
	</synced_block_reference>
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f818d9d6dc984f26a7bf2">
		$$
		Z _ { 1 2 } = - \mathrm{i} \int \mathrm { d } S _ { i } X ^ { 0 i } . \tag{27.9.20}
		$$
	</synced_block_reference>
</callout>
诚然, 这个理论中所有已知的粒子均有在半经典极限下由方程(27.9.28)给出的质量.\[17\]
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- C. Montonen 和 D. Olive 注意到了这一点, Phys. Lett. 72B, 117 (1977). 证明质量没有单圈 修正的是, A. D’Adda, R. Horsley, and P. Di Vecchia, Phys. Lett. 76B, 298 (1978)
</callout>
现在回到一般的 $`N = 2`$ 规范理论, 我们也可以在拉格朗日量中引入额外的“物质”场.
简单起见, 我们限制在有质量的“短”多重态(中心荷 $`\mathcal{Z}`$ 使不等式(25.5.24)的等号成立)上, 每个多重态由一个自旋 $`1 / 2`$ 的费米子和自旋 0 粒子的一个 $`S U ( 2 )`$ 双态再加上可区分的反粒子构成.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#26b82a4da9c2490fabb0059e56c8f602">
		$$
		M \ge | Z _ { 1 2 } | / 2 . \tag{25.5.24}
		$$
	</synced_block_reference>
</callout>
这个自旋组成与 $`N = 1`$ 超对称性下成对左手征标量超场 $`\Phi^{\prime n}`$ 和 $`\Phi^{\prime\prime n}`$ 加上其右手征共轭的自旋组成相同, 后者中的复标量场分量 $`\phi^{\prime n}`$ 和 $`\phi^{\prime\prime n}`$ 与它们的共轭形成了成对的 $`S U (2)`$ 双态, 而旋量场都是 $`S U (2)`$ 单态.
(我们使用撇号和双撇号来区分这些超场和 $`\Phi^A`$ 以及它们的分量和 $`\Phi^A`$ 的分量.) 如果其中一些极多重态 $`\Phi^{\prime n}`$ 和 $`\Phi^{\prime\prime n}`$ 在规范群下是中性的, 那么就允许有如下形式的超势:††
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8132891ff234b437fe4a">
	$$
	f(\Phi,\Phi',\Phi'')=\frac12(s_A)_{nm}\Phi^{\prime n}\Phi^{\prime\prime m}\Phi^A+\frac12\mu_{nm}\Phi^{\prime n}\Phi^{\prime\prime m}.\tag{27.9.29}
	$$
</synced_block>
这样我们就必须给拉格朗日密度(27.9.3)加上这些极多重态的拉格朗日密度, 它由方程(27.4.1)右
边的前八项给出, 并得到总的拉格朗日密度
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#b10bcbaa697a464493ce186b420c124b">
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
	</synced_block_reference>
</callout>
$$
\begin{aligned}
\mathcal L={}&-(D_\mu\phi')^*_n(D^\mu\phi')^n-(D_\mu\phi'')^*_n(D^\mu\phi'')^n-(D_\mu\phi)^*_A(D^\mu\phi)^A\\
&-\frac12\bar{\psi}'_n(\not\!D\psi')^n-\frac12\bar{\psi}''_n(\not\!D\psi'')^n-\frac12\bar{\psi}_A(\not\!D\psi)^A-\frac12\bar{\lambda}_A(\not\!D\lambda)^A\\
&+\mathcal F_n^{\prime *}\mathcal F^{\prime n}+\mathcal F_n^{\prime\prime *}\mathcal F^{\prime\prime n}+\mathcal F_A^*\mathcal F^A\\
&-\operatorname{Re}(s_A)_{nm}\phi^A(\psi_L^{\prime n\mathrm T}\epsilon\psi_L^{\prime\prime m})
-2\sqrt2\operatorname{Re}C_{ABC}(\lambda_L^{A\mathrm T}\epsilon\psi_L^C)\phi^{*B}\\
&-\operatorname{Re}(s_A)_{nm}\phi^{\prime n}(\psi_L^{\prime\prime m\mathrm T}\epsilon\psi_L^A)
-\operatorname{Re}(s_A)_{nm}\phi^{\prime\prime m}(\psi_L^{\prime n\mathrm T}\epsilon\psi_L^A)\\
&+2\sqrt2\operatorname{Im}(t'_A)^m{}_n(\psi_L^{\prime n\mathrm T}\epsilon\lambda_L^A)\phi_m^{\prime *}
+2\sqrt2\operatorname{Im}(t''_A)^m{}_n(\psi_L^{\prime\prime n\mathrm T}\epsilon\lambda_L^A)\phi_m^{\prime\prime *}\\
&+\operatorname{Re}(s_A)_{nm}\phi^A\phi^{\prime n}\mathcal F^{\prime\prime m}
+\operatorname{Re}(s_A)_{nm}\phi^A\phi^{\prime\prime m}\mathcal F^{\prime n}
+\operatorname{Re}(s_A)_{nm}\phi^{\prime n}\phi^{\prime\prime m}\mathcal F^A\\
&+\operatorname{Re}\mu_{nm}\phi^{\prime n}\mathcal F^{\prime\prime m}+\operatorname{Re}\mu_{nm}\phi^{\prime\prime m}\mathcal F^{\prime n}
-\operatorname{Re}\mu_{nm}(\psi_L^{\prime n\mathrm T}\epsilon\psi_L^{\prime\prime m})\\
&-(t'_A)^n{}_m\phi_n^{\prime *}\phi^{\prime m}D^A-(t''_A)^n{}_m\phi_n^{\prime\prime *}\phi^{\prime\prime m}D^A
+\mathrm i\,C_{ABC}\phi^{*B}\phi^C D^A-\xi_A D^A+\frac12D_A D^A\\
&-\frac14 f^A_{\mu\nu}f_A{}^{\mu\nu}+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.
\tag{27.9.30}
\end{aligned}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	Every left-chiral spinor bilinear in this equation is read as
	$$
												X_L^{\mathrm T}\!\cdot Y_L
:=
(X_{L,W})_\alpha(C_W)^{\alpha\beta}(Y_{L,W})_\beta .
	$$
</callout>
其中 $`(t'_A)^n{}_m`$ 和 $`(t''_A)^n{}_m`$ 分别代表左手征标量超场 $`\Phi^{\prime n}`$ 和 $`\Phi^{\prime\prime n}`$ 上的规范群的矩阵(包含耦合常数因子). 费米子和标量之间的 Yukawa 耦合在变换
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8131a7b8ec390745a23c">
	$$
																							\lambda_L^A\to-\psi_L^A,\qquad \psi_L^A\to+\lambda_L^A,\qquad
\phi^{\prime\prime n}\to-\phi^{\prime *}_n,\qquad \phi^{\prime n}\to\phi^{\prime\prime *}_n.\tag{27.9.31}
	$$
</synced_block>
下有一个离散的 $`R`$ -对称性, 如果假定
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f815f8edbd5ba496bf0eb">
	$$
	s_A=-2\sqrt2\,\mathrm i\,t_A^{\prime\mathrm T}=+2\sqrt2\,\mathrm i\,t_A^{\prime\prime}.\tag{27.9.32}
	$$
</synced_block>
(特别地, 注意到方程(27.9.32)要求 $`\Phi^{\prime n}`$ 和 $`\Phi^{\prime\prime n}`$ 构成的规范群表示互为复共轭.) 除了包含辅助场的那些项, 这同时也是拉格朗日密度(27.9.30)中所有其它项的一个对称性.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f815f8edbd5ba496bf0eb">
		$$
		s_A=-2\sqrt2\,\mathrm i\,t_A^{\prime\mathrm T}=+2\sqrt2\,\mathrm i\,t_A^{\prime\prime}.\tag{27.9.32}
		$$
	</synced_block_reference>
</callout>
将变换(27.9.31)下的对称性推广至辅助场是不可能的, 但是对称性会在消掉辅助场后出现.‡ 在令 $`D^A`$ , $`\mathcal F^{\prime n}`$ 和 $`\mathcal F^{\prime\prime n}`$ 等于使得拉格朗日量稳定的值, 并组合 $`D`$ -项和 $`\mathcal F`$ -项后, 拉格朗日密度(其中
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8131a7b8ec390745a23c">
		$$
																								\lambda_L^A\to-\psi_L^A,\qquad \psi_L^A\to+\lambda_L^A,\qquad
\phi^{\prime\prime n}\to-\phi^{\prime *}_n,\qquad \phi^{\prime n}\to\phi^{\prime\prime *}_n.\tag{27.9.31}
		$$
	</synced_block_reference>
</callout>
$`s_A`$ 和 $`t''_A`$ 由方程(27.9.32)给定而 $`\xi_A`$ 取为零)取如下的形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f815f8edbd5ba496bf0eb">
		$$
		s_A=-2\sqrt2\,\mathrm i\,t_A^{\prime\mathrm T}=+2\sqrt2\,\mathrm i\,t_A^{\prime\prime}.\tag{27.9.32}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
\mathcal L={}&-(D_\mu\phi')^*_n(D^\mu\phi')^n-(D_\mu\phi'')^*_n(D^\mu\phi'')^n-(D_\mu\phi)^*_A(D^\mu\phi)^A\\
&-\frac12\bar{\psi}'_n(\not\!D\psi')^n-\frac12\bar{\psi}''_n(\not\!D\psi'')^n-\frac12\bar{\psi}_A(\not\!D\psi)^A-\frac12\bar{\lambda}_A(\not\!D\lambda)^A\\
&-2\sqrt2\operatorname{Im}(t'_A)^m{}_n\phi^A(\psi_L^{\prime n\mathrm T}\epsilon\psi_L^{\prime\prime m})
-2\sqrt2\operatorname{Re}C_{ABC}(\lambda_L^{A\mathrm T}\epsilon\psi_L^C)\phi^{*B}\\
&-2\sqrt2\operatorname{Im}(t'_A)^m{}_n\phi^{\prime n}(\psi_L^{\prime\prime m\mathrm T}\epsilon\psi_L^A)
-2\sqrt2\operatorname{Im}(t'_A)^m{}_n\phi^{\prime\prime m}(\psi_L^{\prime n\mathrm T}\epsilon\psi_L^A)\\
&+2\sqrt2\operatorname{Im}(t'_A)^m{}_n(\psi_L^{\prime n\mathrm T}\epsilon\lambda_L^A)\phi_m^{\prime *}
-2\sqrt2\operatorname{Im}(t'_A)^n{}_m(\psi_L^{\prime\prime n\mathrm T}\epsilon\lambda_L^A)\phi_m^{\prime\prime *}\\
&-\frac14 f^A_{\mu\nu}f_A{}^{\mu\nu}+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}\\
&-\{t'_A,t'_B\}^n{}_m\phi^A\phi^{*B}(\phi_n^{\prime *}\phi^{\prime m}+\phi^{\prime\prime n}\phi_m^{\prime\prime *})
-\frac12\left[(t'_A)^n{}_m(\phi_n^{\prime *}\phi^{\prime m}-\phi^{\prime\prime n}\phi_m^{\prime\prime *})\right]^2\\
&+\frac12C_{ABC}C_{ADE}\phi^{*B}\phi^C\phi^{*D}\phi^E
-2\left|(t'_A)^n{}_m\phi^{\prime m}\phi^{\prime\prime n}\right|^2\\
&-4\operatorname{Re}(t'_A\mu)^n{}_m\phi_n^{\prime *}\phi^{\prime m}
-4\operatorname{Re}(\mu t'_A)^n{}_m\phi^{\prime\prime n}\phi_m^{\prime\prime *}\\
&-2(\mu^\dagger\mu)^n{}_m\phi_n^{\prime *}\phi^{\prime m}
-2(\mu\mu^\dagger)^n{}_m\phi^{\prime\prime n}\phi_m^{\prime\prime *}.
\tag{27.9.33}
\end{aligned}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	Every left-chiral spinor bilinear in this equation is read as
	$$
												X_L^{\mathrm T}\!\cdot Y_L
:=
(X_{L,W})_\alpha(C_W)^{\alpha\beta}(Y_{L,W})_\beta .
	$$
</callout>
右边的后五行来自于方程(27.9.30)中包含辅助场的那些项, 现在给定
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f810f9fe8dd25e0cbf84f">
	$$
	[t'_A,\mu]=[\mu^\dagger,\mu]=0.\tag{27.9.34}
	$$
</synced_block>
它们在离散变换(27.9.31)下也将是不变的.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8131a7b8ec390745a23c">
		$$
																								\lambda_L^A\to-\psi_L^A,\qquad \psi_L^A\to+\lambda_L^A,\qquad
\phi^{\prime\prime n}\to-\phi^{\prime *}_n,\qquad \phi^{\prime n}\to\phi^{\prime\prime *}_n.\tag{27.9.31}
		$$
	</synced_block_reference>
</callout>
<empty-block/>
<empty-block/>
我们现在可以更进一步并考虑 $`N = 4`$ 扩充整体超对称性的情况.(正如25.4节评述的, $`N=3`$ 超对称与 $`N=4`$ 超对称性相同)
 $`N = 4`$ 超对称性的无质量多重态中不含引力子或引力微子的只能由一个螺旋度为1的粒子, 一个螺旋度 $`1 / 2`$ 粒子的 $`S U ( 4 )`$ 四重态, 以及一个零螺旋度粒子的$`S U ( 4 )`$ 六重态, 加上与它们螺旋度相反的CPT共轭构成.
对规范群的每个生成元 $`t _ { A }`$ 都有这样一个超多重态.
这些粒子可以被分组成 $`N = 2`$ 超对称性的超多重态: 对每个 $`t _ { A }`$ 有一个规范超多重态, 这个规范多重态的CPT共轭, 以及两个极多重态, 规范多重态由螺旋度为1的一个粒子, 螺旋度为 $`\pm 1 / 2`$ 的两个粒子和螺旋度为0的一个粒子构成, CPT共轭则由螺旋度相反的粒子构成, 而每个极多重态由两个螺旋度各为 $`\pm 1 / 2`$ 的粒子和两个零螺旋度的粒子构成.
$`N = 2`$ 规范超场由一个 $`N = 1`$ 规范超场 $`V^A`$ 和一个左手征标量超场 $`\Phi^A`$ 以及它们的复共轭构成, 而两个 $`N = 2`$ 的极多重态由两个另外的左手征标量超场 $`\Phi^{\prime A}`$ 和 $`\Phi^{\prime\prime A}`$ 以及它们的复共轭构成.
由于 $`N = 4`$ 超对称性包含 $`N = 2`$ 超对称性, 在消掉 $`N = 1`$ 超对称性的辅助场后, 它的拉格朗日密度必然是方程(27.9.33)的一个特殊情况, 只不过指标 $`n`$ , $`m`$ 等现在在伴随表示的指标 $`A`$ , $`B`$ , $`C`$ 中取值.
另外, 超势(27.9.29)中的系数 $`\mu_{nm}`$ 在这里必须为零, 否则方程(27.9.33)将会包含费米场 $`\psi^{\prime A}`$ 和 $`\psi^{\prime\prime A}`$ 的二次项, 但它们的 $`N = 4`$ 超对称伙伴 $`\lambda^A`$ 和 $`\psi^A`$ 没有这样的项.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8132891ff234b437fe4a">
		$$
		f(\Phi,\Phi',\Phi'')=\frac12(s_A)_{nm}\Phi^{\prime n}\Phi^{\prime\prime m}\Phi^A+\frac12\mu_{nm}\Phi^{\prime n}\Phi^{\prime\prime m}.\tag{27.9.29}
		$$
	</synced_block_reference>
</callout>
再令 $`(t'_A)_B{}^C`$ 等于伴随表示中的生成元 $`-\mathrm i C_{AB}{}^C`$ , 我们发现拉格朗日密度必须取如下的形式
$$
\begin{aligned}
\mathcal L={}&-(D_\mu\phi')^*_A(D^\mu\phi')^A-(D_\mu\phi'')^*_A(D^\mu\phi'')^A-(D_\mu\phi)^*_A(D^\mu\phi)^A\\
&-\frac12\bar{\psi}'_A(\not\!D\psi')^A-\frac12\bar{\psi}''_A(\not\!D\psi'')^A-\frac12\bar{\psi}_A(\not\!D\psi)^A-\frac12\bar{\lambda}_A(\not\!D\lambda)^A\\
&-2\sqrt2\operatorname{Re}C_{ABC}\phi^A(\psi_L^{\prime B\mathrm T}\epsilon\psi_L^{\prime\prime C})
-2\sqrt2\operatorname{Re}C_{ABC}(\lambda_L^{A\mathrm T}\epsilon\psi_L^C)\phi^{*B}\\
&-2\sqrt2\operatorname{Re}C_{ABC}\phi^{\prime B}(\psi_L^{\prime\prime C\mathrm T}\epsilon\psi_L^A)
-2\sqrt2\operatorname{Re}C_{ABC}\phi^{\prime\prime C}(\psi_L^{\prime B\mathrm T}\epsilon\psi_L^A)\\
&+2\sqrt2\operatorname{Re}C_{ABC}(\psi_L^{\prime B\mathrm T}\epsilon\lambda_L^A)\phi^{\prime *C}
+2\sqrt2\operatorname{Re}C_{ABC}(\psi_L^{\prime\prime B\mathrm T}\epsilon\lambda_L^A)\phi^{\prime\prime *C}\\
&-\frac14 f^A_{\mu\nu}f_A{}^{\mu\nu}+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}-V.
\tag{27.9.35}
\end{aligned}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	Every left-chiral spinor bilinear in this equation is read as
	$$
												X_L^{\mathrm T}\!\cdot Y_L
:=
(X_{L,W})_\alpha(C_W)^{\alpha\beta}(Y_{L,W})_\beta .
	$$
</callout>
其中势是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81e59d12cee320be144a">
	$$
																							\begin{aligned}
V={}&C_{ADE}C_{BCE}(\phi^A\phi^{*B}+\phi^B\phi^{*A})(\phi^{\prime C}\phi^{\prime *D}+\phi^{\prime\prime *C}\phi^{\prime\prime D})\\
&+\frac12\left|C_{ABC}(\phi^{\prime *B}\phi^{\prime C}-\phi^{\prime\prime B}\phi^{\prime\prime *C})\right|^2
-\frac12 C_{ABC}C_{ADE}\phi^{*B}\phi^C\phi^{*D}\phi^E\\
&+2\left|C_{ABC}\phi^{\prime B}\phi^{\prime\prime C}\right|^2.
\tag{27.9.36}
\end{aligned}
	$$
</synced_block>
不需要进一步的约束, 这个拉格朗日量就有 $`S U ( 4 ) R`$ -对称性, 这暗示了它在 $`N = 4`$ 超对称性下是不变的.
为了看到这点, 我们需要用Jacobi恒等式将方程(27.9.36)右边第二行中的交叉项写成如下形式
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81e59d12cee320be144a">
		$$
																								\begin{aligned}
V={}&C_{ADE}C_{BCE}(\phi^A\phi^{*B}+\phi^B\phi^{*A})(\phi^{\prime C}\phi^{\prime *D}+\phi^{\prime\prime *C}\phi^{\prime\prime D})\\
&+\frac12\left|C_{ABC}(\phi^{\prime *B}\phi^{\prime C}-\phi^{\prime\prime B}\phi^{\prime\prime *C})\right|^2
-\frac12 C_{ABC}C_{ADE}\phi^{*B}\phi^C\phi^{*D}\phi^E\\
&+2\left|C_{ABC}\phi^{\prime B}\phi^{\prime\prime C}\right|^2.
\tag{27.9.36}
\end{aligned}
		$$
	</synced_block_reference>
</callout>
$$
\begin{aligned}
C_{ABC}C_{ADE}\phi^{\prime *B}\phi^{\prime C}\phi^{\prime\prime *D}\phi^{\prime\prime E}
={}&-C_{ABC}C_{ADE}\phi^{\prime *B}\phi^{\prime D}\phi^{\prime\prime *E}\phi^{\prime\prime C}\\
&-C_{ABC}C_{ADE}\phi^{\prime *B}\phi^{\prime E}\phi^{\prime\prime *C}\phi^{\prime\prime D}.
\end{aligned}
$$
这使得我们可以将势写成对标量和它们的共轭对称的形式
$$
\begin{aligned}
V={}&\left|C_{ABC}\phi^{*B}\phi^{\prime C}\right|^2+
\left|C_{ABC}\phi^{*B}\phi^{\prime\prime *C}\right|^2+
\left|C_{ABC}\phi^B\phi^{\prime C}\right|^2+
\left|C_{ABC}\phi^B\phi^{\prime\prime *C}\right|^2\\
&+\left|C_{ABC}\phi^{\prime *B}\phi^{\prime\prime C}\right|^2+
\left|C_{ABC}\phi^{\prime B}\phi^{\prime\prime C}\right|^2+
\frac12\left|C_{ABC}\phi^{\prime B}\phi^{\prime *C}\right|^2\\
&+\frac12\left|C_{ABC}\phi^{\prime\prime B}\phi^{\prime\prime *C}\right|^2+
\frac12\left|C_{ABC}\phi^B\phi^{*C}\right|^2.
\tag{27.9.37}
\end{aligned}
$$
现在, 为了显现 $`S U ( 4 )`$ 对称性, 我们引入场的 $`S U ( 4 )`$ 记法.
我们把左手费米场组装成一个 $`S U ( 4 )`$ 矢量:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81ad8090c2a5803f3725">
	$$
												\psi_L^{1A}\equiv\psi_L^A,\qquad \psi_L^{2A}\equiv\lambda_L^A,\qquad
\psi_L^{3A}\equiv\psi_L^{\prime A},\qquad \psi_L^{4A}\equiv\psi_L^{\prime\prime A}.\tag{27.9.38}
	$$
</synced_block>
为了使拉格朗日密度中的费米子动能项是 $`S U ( 4 )`$ -不变的, 我们必须把右手费米场组装成一个逆变矢量:
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8115bed5c2a2260f8b75">
	$$
												\psi_{R\,1}^A\equiv\psi_R^A,\qquad \psi_{R\,2}^A\equiv\lambda_R^A,\qquad
\psi_{R\,3}^A\equiv\psi_R^{\prime A},\qquad \psi_{R\,4}^A\equiv\psi_R^{\prime\prime A}.\tag{27.9.39}
	$$
</synced_block>
这样, 费米场上的 Majorana 条件就取 $`S U ( 4 )`$ -不变的形式
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81958644d25890681818">
	$$
	(\psi_L^{iA})^*=-\beta\epsilon\psi_{R\,i}^A.\tag{27.9.40}
	$$
</synced_block>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
												\bigl((\psi_{L,W}^{iA})_\alpha\bigr)^*
=
-(\beta_W)_\alpha{}^\rho
(C_W)_{\rho\beta}
(\psi_{R\,i,W}^{A})_\beta .
	$$
</callout>
其中指标 $`i , j`$ 等在 $`1 , 2 , 3 , 4`$ 中取值.
为了使费米场和标量场之间的 Yukawa 耦合是 $`S U ( 4 )`$ 不变的,我们必须给标量赋予反对称 $`S U ( 4 )`$ 张量的变换性质
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8195b20fc39709f77afa">
	$$
												\begin{array}{lll}
\phi^{12,A}\equiv\phi^{*A},&\phi^{13,A}\equiv\phi^{\prime\prime A},&\phi^{14,A}\equiv-\phi^{\prime A},\\
\phi^{23,A}\equiv-\phi^{\prime *A},&\phi^{24,A}\equiv-\phi^{\prime\prime *A},&\phi^{34,A}\equiv\phi^A.
\end{array}\tag{27.9.41}
	$$
</synced_block>
这同时还服从一个 $`S U ( 4 )`$ -不变的实条件
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f811d8c7ed6c3f650d102">
	$$
	(\phi^{ij,A})^*=\frac12\epsilon_{ijkl}\phi^{kl,A}.\tag{27.9.42}
	$$
</synced_block>
这样, 整个拉格朗日密度(27.9.35)就可以写成一个显然 $`S U ( 4 )`$ -不变的形式
$$
\begin{aligned}
\mathcal L={}&-\frac12(D_\mu\phi^{ij})^*_A(D^\mu\phi^{ij})^A
-\frac12\psi_L^{iA\mathrm T}\epsilon(\not\!D\psi_R)_{iA}
+\frac12\psi_{R\,i}^{A\mathrm T}\epsilon(\not\!D\psi_L)^i{}_A\\
&-\sqrt2\operatorname{Re}C_{ABC}\phi^{ij,A}(\psi_{L\,i}^{B\mathrm T}\epsilon\psi_{L\,j}^C)-V\\
&-\frac14 f^A_{\mu\nu}f_A{}^{\mu\nu}+\frac{g^2\theta}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}.
\tag{27.9.43}
\end{aligned}
$$
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**Weinberg quantities · Srednicki index grammar（no rephasing）**
	$$
											\begin{aligned}
\psi_L^{iA\mathrm T}\!\cdot(\not\!D\psi_R)_{iA}
&:=
(\psi_{L,W}^{iA})_\alpha(C_W)^{\alpha\beta}
(\not\!D\psi_{R,W})_{iA,\beta},\\
\psi_{R\,i}^{A\mathrm T}\!\cdot(\not\!D\psi_L)^i{}_A
&:=
-(\psi_{R\,i,W}^{A})_\alpha(C_W)^{\alpha\beta}
(\not\!D\psi_{L,W})^i{}_{A,\beta},\\
\psi_{L\,i}^{B\mathrm T}\!\cdot\psi_{L\,j}^{C}
&:=
(\psi_{L\,i,W}^{B})_\alpha(C_W)^{\alpha\beta}
(\psi_{L\,j,W}^{C})_\beta .
\end{aligned}
	$$
</callout>
其中势是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f816f8140d7607a3c1efb">
	$$
	V=\frac18\left|C_{ABC}\phi^{B\,ij}\phi^{C\,kl}\right|^2.\tag{27.9.44}
	$$
</synced_block>
这个势有一个为零的最小值, 这使得这个理论中的超对称性是不破缺的.
当生成元 $`t_A\phi^{Aij}`$ 全部彼此对易时, 势能到达这个最小值.
当 $`\theta`$ 角为零时, 无论是 $`N = 2`$ 还是 $`N = 4`$ 的超对称性, 只有一个单规范群的规范理论只有一个耦合常数, 规范耦合常数 $`g`$ .
由于这些理论有 $`N = 1`$ 规范对称性, 它们享有 27.6 节讨论过的性质,在微扰论的高阶中, 无穷大只出现在对这个耦合的单圈修正中.‡‡ 
那么到微扰论的所有阶, 重整化群方程 $`\mu \mathrm { d } g / \mathrm { d } \mu = \beta ( g )`$ 中的函数 $`\beta ( g )`$ 就由单圈公式(18.7.2)加上因出现标量场的合适修正给出:
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8167aebdd17eeb61c070">
		$$
		\beta ( g ) = - \frac { g ^ { 3 } } { 4 \pi ^ { 2 } } \left( \frac { 1 1 } { 1 2 } C _ { 1 } - \frac { 1 } { 3 } C _ { 2 } \right) + O ( g ^ { 5 } ) ~ . \tag{18.7.2}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81429df8f2ea7235dadd">
	$$
	\beta(g)=-\frac{g^3}{4\pi^2}\left(\frac{11}{12}C_1-\frac16C_2^f-\frac1{12}C_2^s\right).\tag{27.9.45}
	$$
</synced_block>
其中
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81b49ceed16548514c0d">
	$$
												\begin{aligned}
C_{AB}{}^C C^{AB}{}_D&=g^2C_1\delta^C{}_D,\\
\left[\operatorname{Tr}(t_Ct_D)\right]_{\text{Majorana fermions}}&=g^2C_2^f\delta_{CD},\\
\left[\operatorname{Tr}(t_Ct_D)\right]_{\text{complex scalars}}&=g^2C_2^s\delta_{CD}.
\end{aligned}\tag{27.9.46-27.9.47}
	$$
</synced_block>
在有 $`N = 2`$ 超对称性的一般理论中, 我们有两个处在伴随表示下的 Majorana 费米子 $`\lambda^A`$ 和 $`\psi^A`$ 以及 $`H`$ 对 Majorana 费米子 $`\psi^{\prime n}`$ 和 $`\psi^{\prime\prime n}`$ , 它们的左手和右手部分处在生成元为 $`t'_A`$ 或 $`-t_A^{\prime\mathrm T}`$ 的表示中, 所以
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f819a9088ff77c45a98c8">
	$$
	C_2^f=2C_1+2HC_2'.\tag{27.9.48}
	$$
</synced_block>
其中 $`C _ { 2 } ^ { \prime }`$ 被定义成
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81cb8d7ce77e0c27e45e">
	$$
	\operatorname{Tr}t'_Ct'_D=g^2C'_2\delta_{CD}.\tag{27.9.49}
	$$
</synced_block>
另外, 我们有一个处在伴随表示下的复标量 $`\phi^A`$ 和 $`H`$ 对处在生成元为 $`t'_A`$ 或 $`-t_A^{\prime\mathrm T}`$ 的表示下的 $`\phi^{\prime n}`$ 和 $`\phi^{\prime\prime n}`$ , 所以
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81feaa15c350a87b20a6">
	$$
	C_2^s=C_1+2HC'_2.\tag{27.9.50}
	$$
</synced_block>
因此 $`\beta`$ 函数(27.9.45)是
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81429df8f2ea7235dadd">
		$$
		\beta(g)=-\frac{g^3}{4\pi^2}\left(\frac{11}{12}C_1-\frac16C_2^f-\frac1{12}C_2^s\right).\tag{27.9.45}
		$$
	</synced_block_reference>
</callout>
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f812c8d75f9b76ad81f3e">
	$$
	\beta(g)=-\frac{g^2}{8\pi^2}(C_1-HC'_2).\tag{27.9.51}
	$$
</synced_block>
$`N = 4`$ 超对称性就是 $`H = 1`$ 对 $`N = 2`$ 极多重态处在伴随表示下的特殊情况, 即有 $`C _ { 2 } ^ { \prime } = C _ { 1 }`$ , 所以这一情况下的 $`\beta`$ 函数为零.
<span color="yellow_bg">因此这是一个根本没有重整化的有限理论.\[19\]</span>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- 证明 $`N = 4`$ 理论有限性的是, M. F. Sohnius and P. C. West, Nucl. Phys. B100, 245 (1981); P. S. Howe, K. S. Stelle, and P. Townsend, Nucl. Phys. B214, 519 (1983); S. Mandelstam, Nucl. Phys. B213, 149 (1983); L. Brink, O. Lindgren, and B. E. W. Nilsso
</callout>
<empty-block/>
有 $`N = 4`$ 超对称性的规范理论有另外一个显著性质, 称为对偶.
这最早是 Montonen和Olive对单规范群自发破缺到 $`U ( 1 )`$ 电磁规范群的纯玻色理论做出的猜想.
他们注意到, 对于电荷 $`q=ne`$ 且磁单极距 $`\mathcal M=4\pi m/e`$ ( $`n`$ 和 $`m`$ 是符号任意的整数)的粒子, (23.3节描述过的那类)半经典计算给出的粒子质量是
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f8124b539df7a27d9a4d8">
	$$
	M=\sqrt2\left|v\left(ne+\frac{4\pi\mathrm i m}{e}\right)\right|.\tag{27.9.52}
	$$
</synced_block>
它在变换
<synced_block url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81bfb13ac96148c89b95">
	$$
	m\to n,\qquad n\to-m,\qquad e\leftrightarrow\frac{4\pi}{e}.\tag{27.9.53}
	$$
</synced_block>
下是不变的.
以此为基础, 他们认为一个有弱规范耦合 $`e`$ 的理论完全等于一个有强规范耦合 $`4 \pi / e`$ 的理论.
纯玻色理论或 $`N = 1`$ 和 $`N = 2`$ 扩充超对称理论的最简单版本实际上都没有这个性质;\[20\]
首先, 破缺规范对称性的有质量带电荷矢量玻色子有自旋1, 而所有磁单极子和双荷子有自旋 $`1 / 2`$ 或 0. (我们将在 29.5 节看到, $`N = 2`$ 的理论确实有一类更加巧妙的对偶性质.) 
但对于 $`N = 4`$ 超对称性, 单极子态构成了有一个自旋1粒子, 4自旋 $`1 / 2`$ 粒子和两个自旋0粒子的多重态, 就像基本粒子一样.\[20\] 
$`N = 4`$ 超对称规范理论在电量子数和磁量子数以及 $`e`$ 和 $`4 \pi / e`$ 交换下不变这一点已有证据.\[21\]
 强耦合理论和弱耦合理论的等价性已经变成弦论中日趋重要的课题, 但这超出本书的讨论范围.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	- H. Osborn, 参考文献\[13\]
	- A. Sen, Phys. Lett. B329, 217 (1994); C. Vafa and E. Witten, Nucl. Phys. B431, 3 (1994); L. Girardello, A. Giveon, M. Porrati, and A. Zaffaroni, Phys. Lett. B334, 331 (1994)
</callout>
## 习题
**1.** 到规范耦合常数的第二阶, 计算出使用变换(27.1.12)将规范超场 $`V ^ { A }`$ 变到 Wess-Zumino 规范下所需要的超场 $`\Omega ^ { A }`$ 的分量.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f81d0a062f562ed48d849">
		$$
		\Gamma(x,\theta)\to \exp\bigl(+\mathrm{i}t_A\Omega^A(x,\theta)^*\bigr)\Gamma(x,\theta)\exp\bigl(-\mathrm{i}t_A\Omega^A(x,\theta)\bigr).\tag{27.1.12}
		$$
	</synced_block_reference>
</callout>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**解 1.**
	记所有量均为 representation matrices：
	$$
							C=t_AC^A,\quad \omega=t_A\omega^A,\quad M=t_AM^A,\quad N=t_AN^A,\quad
\Omega=t_A\Omega^A .
	$$
	每增加一个 commutator 就增加一阶规范耦合；取剩余普通规范自由度为 $`\operatorname{Re}W=0`$。
	令
	$$
							V_L:=V\big|_{\theta_R=0}=C-\frac{\mathrm i}{2}Q,\qquad
Q:=2\mathrm i(V_L-C).
	$$
	由一般实超场的分量展开，
	$$
	Q\big|_{\theta=0}=0,\qquad q_Q=-\sqrt2\,\omega,\qquad F_Q=M-\mathrm iN.
	$$
	Wess–Zumino 条件等价于
	$$
							\Gamma'\big|_{\theta_R=0}=1,\qquad
\Gamma'\big|_{\theta_L=0}=1.
	$$
	在 $`\theta_R=0`$ 上，$`\Omega^*=W^*=-\mathrm iC`$，故
	$$
							1=e^C e^{-2V_L}e^{-\mathrm i\Omega},
\qquad
e^{-\mathrm i\Omega}=e^{2V_L}e^{-C},
\qquad
\Omega=\mathrm i\log\!\left(e^{2V_L}e^{-C}\right).
	$$
	取 $`S:=V_L-C=-\mathrm iQ/2`$。Baker–Campbell–Hausdorff expansion 给出
	$$
							\begin{aligned}
\log\!\left(e^{2(C+S)}e^{-C}\right)
={}&C+2S+[C,S]+\frac12[C,[C,S]]\\
&+\frac13[S,[C,S]]+O(g^3),
\end{aligned}
	$$
	从而
	$$
							\boxed{\;
\Omega=\mathrm iC+Q+\frac12[C,Q]
+\frac14[C,[C,Q]]
-\frac{\mathrm i}{12}[Q,[C,Q]]
+O(g^3)\; }.
	$$
	对两个左手征超场 $`A=(a,\psi_A,F_A)`$、$`B=(b,\psi_B,F_B)`$，
	$$
	F_{AB}=aF_B+F_Ab-\psi_{AL}^{\mathrm T}\epsilon\psi_{BL}.
	$$
	逐分量读取上式即得
	$$
							\boxed{\begin{aligned}
W={}&\mathrm iC,\\
w={}&-\sqrt2\left(
\omega+\frac12[C,\omega]+\frac14[C,[C,\omega]]
\right)+O(g^3),\\
\mathcal W={}&M-\mathrm iN+\frac12[C,M-\mathrm iN]
+\frac14[C,[C,M-\mathrm iN]]\\
&+\frac{\mathrm i}{6}\left\{
\omega_L^{\mathrm T}\epsilon[C,\omega_L]
-[C,\omega_L]^{\mathrm T}\epsilon\omega_L
\right\}+O(g^3).
\end{aligned}}
	$$
	代回可直接得到
	$$
	C'=\omega'=M'=N'=0,
	$$
	而 $`V_\mu,\lambda,D`$ 保留；这正是 Wess–Zumino gauge。
</callout>
**2.** 证明满足条件(27.2.20)的最一般手征线性超场 $`W_\alpha`$ 拥有满足齐次 Maxwell 方程 $`\epsilon^{\mu\nu\rho\sigma}\partial_\rho f_{\mu\nu}=0`$ 的分量 $`f_{\mu\nu}`$.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f810b8ddfe083aa93bebe">
		$$
		\epsilon _ { \alpha \beta } { \mathcal D } _ { L \alpha } W _ { L \beta } = \epsilon _ { \alpha \beta } { \mathcal D } _ { R \alpha } W _ { R \beta } . \tag{27.2.20}
		$$
	</synced_block_reference>
</callout>
方程(27.2.20)给 $`W_\alpha`$ 的其它分量附加的条件是什么?
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	<synced_block_reference url="https://app.notion.com/p/34cee2b74b3f81879a50e2747ed85f8e#34cee2b74b3f810b8ddfe083aa93bebe">
		$$
		\epsilon _ { \alpha \beta } { \mathcal D } _ { L \alpha } W _ { L \beta } = \epsilon _ { \alpha \beta } { \mathcal D } _ { R \alpha } W _ { R \beta } . \tag{27.2.20}
		$$
	</synced_block_reference>
</callout>
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**解 2.**
	记
	$$
						\theta_L^2:=\theta_L^{\mathrm T}\epsilon\theta_L,\qquad
\theta_R^2:=\theta_R^{\mathrm T}\epsilon\theta_R .
	$$
	最一般的 chiral spinor superfield 可写为
	$$
						\begin{aligned}
W_{L\alpha}={}&\lambda_{L\alpha}(x_+)
+\left[-\mathrm i d_L\delta_\alpha{}^\beta
+\frac14[\gamma^\mu,\gamma^\nu]_\alpha{}^\beta
h^L_{\mu\nu}\right]\theta_{L\beta}
+\theta_L^2\rho_{R\alpha}(x_+),\\
W_{R\alpha}={}&\lambda_{R\alpha}(x_-)
+\left[+\mathrm i d_R\delta_\alpha{}^\beta
+\frac14[\gamma^\mu,\gamma^\nu]_\alpha{}^\beta
h^R_{\mu\nu}\right]\theta_{R\beta}
-\theta_R^2\rho_{L\alpha}(x_-).
\end{aligned}
	$$
	这里 $`h^L,h^R`$ 分别是同一个 two-form 在左右手旋量上可见的 Hodge projections；等价地定义实张量 $`f_{\mu\nu}`$ 使
	$$
						h^L_{\mu\nu}\gamma^{\mu\nu}P_L
=f_{\mu\nu}\gamma^{\mu\nu}P_L,\qquad
h^R_{\mu\nu}\gamma^{\mu\nu}P_R
=f_{\mu\nu}\gamma^{\mu\nu}P_R .
	$$
	令
	$$
						\Delta:=\epsilon_{\alpha\beta}\mathcal D_{L\alpha}W_{L\beta}
-\epsilon_{\alpha\beta}\mathcal D_{R\alpha}W_{R\beta}.
	$$
	把超导数逐次作用在一般展开上，各独立 Grassmann monomial 的系数为
	$$
						\begin{aligned}
[\Delta]_1&=-2\mathrm i(d_L-d_R),\\
[\Delta]_{\theta_L}
&=2\theta_L^{\mathrm T}\epsilon
\left(\rho_R-\not\!\partial\lambda_R\right),\\
[\Delta]_{\theta_R}
&=-2\theta_R^{\mathrm T}\epsilon
\left(\rho_L-\not\!\partial\lambda_L\right),\\
[\Delta]_{\theta_R\theta_L}
&=2\mathrm i
(\theta_R^{\mathrm T}\epsilon\gamma_\sigma\theta_L)
\epsilon^{\rho\mu\nu\sigma}\partial_\rho f_{\mu\nu}.
\end{aligned}
	$$
	所以 $`\Delta=0`$ 分别给出
	$$
						\boxed{\begin{gathered}
d_L=d_R=:D,\qquad D^*=D,\\
\rho_R=\not\!\partial\lambda_R,\qquad
\rho_L=\not\!\partial\lambda_L,\\
f_{\mu\nu}^*=f_{\mu\nu},\qquad
\epsilon^{\mu\nu\rho\sigma}\partial_\rho f_{\mu\nu}=0.
\end{gathered}}
	$$
	最后一式就是 homogeneous Maxwell equation。由 Poincaré lemma，在任意 contractible patch，
	$$
	f_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu .
	$$
	因此最一般解恰为
	$$
						\boxed{\begin{aligned}
W_L={}&\lambda_L(x_+)
+\frac12\gamma^\mu\gamma^\nu\theta_L f_{\mu\nu}(x_+)
-\mathrm i\theta_LD(x_+)
+\theta_L^2\not\!\partial\lambda_R(x_+),\\
W_R={}&\lambda_R(x_-)
+\frac12\gamma^\mu\gamma^\nu\theta_R f_{\mu\nu}(x_-)
+\mathrm i\theta_RD(x_-)
-\theta_R^2\not\!\partial\lambda_L(x_-).
\end{aligned}}
	$$
	这里没有推出 $`\partial_\mu f^{\mu\nu}=0`$、$`\not\!\partial\lambda=0`$ 或 $`D=0`$；这些是 off-shell Bianchi constraints，不是 equations of motion。
</callout>
**3.** 考虑有一个 $`S U ( 2 )`$ 规范群和一个手征超场的一般可重整 $`N = 1`$ 超对称规范理论, 其中手征超场属于 $`S U ( 2 )`$ 的3 -矢表示.
这个理论最一般的超势是什么? 清楚地构造出整个理论的拉格朗日密度.
消掉辅助场.
证明这个理论中的超对称性是不破缺的.
这个理论中粒子的质量是什么?
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**解 3.**
	取
	$$
					C_{ABC}=g\epsilon_{ABC},\qquad
(t_A)_B{}^C=-\mathrm i\,C_{AB}{}^C .
	$$
	一般 renormalizable holomorphic superpotential 为
	$$
					f=c+\ell_A\Phi^A+\frac12\mu_{AB}\Phi^A\Phi^B
+\frac16y_{ABC}\Phi^A\Phi^B\Phi^C .
	$$
	Gauge invariance 逐项给出
	$$
	\ell_A=0,\qquad \mu_{AB}=m\delta_{AB}.
	$$
	因为 chiral superfields 彼此交换，$`y_{ABC}`$ 只取全对称部分；而 $`SU(2)`$ 的三阶 invariant tensor 只有全反对称的 $`\epsilon_{ABC}`$，故
	$$
	\epsilon_{ABC}\Phi^A\Phi^B\Phi^C=0,\qquad y_{ABC}=0.
	$$
	所以
	$$
	\boxed{\,f(\Phi)=c+\frac m2\Phi_A\Phi_A\, }.
	$$
	完整 off-shell Lagrangian density 是
	$$
					\boxed{\begin{aligned}
\mathcal L={}&-(D_\mu\phi)^*_A(D^\mu\phi)^A
-\frac12\bar\psi_A(\not\!D\psi)^A+\mathcal F_A^*\mathcal F^A\\
&-2\sqrt2\,\operatorname{Re}\!\left[
C_{ABC}(\lambda_L^{A\mathrm T}\epsilon\psi_L^C)\phi^{*B}\right]
+\mathrm iC_{ABC}\phi^{*B}\phi^C D^A+\frac12D_AD^A\\
&-\frac14f^A_{\mu\nu}f_A{}^{\mu\nu}
-\frac12\bar\lambda_A(\not\!D\lambda)^A
+\frac{g^2\vartheta}{64\pi^2}
\epsilon_{\mu\nu\rho\sigma}f^{A\mu\nu}f_A{}^{\rho\sigma}\\
&+\left[m\mathcal F_A\phi_A
-\frac m2(\psi_{LA}^{\mathrm T}\epsilon\psi_{LA})
+\mathrm{H.c.}\right].
\end{aligned}}
	$$
	其中
	$$
					(D_\mu X)^A=\partial_\mu X^A+g\epsilon_{BC}{}^A V_\mu^B X^C,\qquad
f^A_{\mu\nu}=\partial_\mu V_\nu^A-\partial_\nu V_\mu^A
+g\epsilon_{BC}{}^A V_\mu^B V_\nu^C .
	$$
	辅助场方程逐项为
	$$
					\frac{\partial\mathcal L}{\partial\mathcal F_A^*}
=\mathcal F_A+m^*\phi_A^*=0,\qquad
\frac{\partial\mathcal L}{\partial D_A}
=D_A+\mathrm ig\epsilon_{ABC}\phi_B^*\phi_C=0,
	$$
	故
	$$
					\boxed{\mathcal F_A=-m^*\phi_A^*,\qquad
D_A=-\mathrm ig\epsilon_{ABC}\phi_B^*\phi_C .}
	$$
	消元后的 scalar potential 为
	$$
					\begin{aligned}
V&=|m|^2\phi_A^*\phi_A+\frac12D_AD_A\\
&=|m|^2\phi^\dagger\phi
+\frac{g^2}{2}\left[(\phi^\dagger\phi)^2-|\phi\!\cdot\!\phi|^2\right].
\end{aligned}
	$$
	写 $`\phi=u+\mathrm iv`$，其中 $`u,v\in\mathbb R^3`$，则
	$$
					(\phi^\dagger\phi)^2-|\phi\!\cdot\!\phi|^2
=4\left[u^2v^2-(u\!\cdot\!v)^2\right]
=4|u\times v|^2,
	$$
	因此
	$$
	\boxed{V=|m|^2(u^2+v^2)+2g^2|u\times v|^2\geq0.}
	$$
	$`\phi=0`$ 时 $`\mathcal F_A=D_A=V=0`$，故至少存在一个 supersymmetric vacuum，超对称性不破缺。
	若 $`m\neq0`$，唯一真空是 $`\phi_0=0`$，$`SU(2)`$ 不破缺：
	$$
					\begin{array}{c|c}
\text{fields}&\text{mass}\\ \hline
\phi^A,\ \psi^A&|m|\\
V_\mu^A,\ \lambda^A&0
\end{array}
	$$
	若 $`m=0`$，零势条件是 $`u\times v=0`$。模去 gauge transformations 后
	$$
	\phi_0=(0,0,z),\qquad z\in\mathbb C,\qquad z\sim-z .
	$$
	当 $`z\neq0`$ 时 $`SU(2)\to U(1)`$。令
	$$
	\mu:=\sqrt2\,g|z|.
	$$
	由标量动能项和 Yukawa matrix 分别得到
	$$
					\begin{gathered}
m(V_\mu^1)=m(V_\mu^2)=\mu,\qquad m(V_\mu^3)=0,\\
m(H_1)=m(H_2)=\mu,\qquad G_1,G_2\ \text{被 }V_\mu^{1,2}\text{ 吸收},\qquad
m(\phi^3)=0,\\
M_F^\dagger M_F
=\mu^2\operatorname{diag}(1,1,0,1,1,0)
\quad\text{on }(\psi^1,\psi^2,\psi^3,\lambda^1,\lambda^2,\lambda^3).
\end{gathered}
	$$
	所以 $`\psi^{1,2},\lambda^{1,2}`$ 的四个 massive spinor modes 质量均为 $`\mu`$，而 $`\psi^3,\lambda^3`$ 无质量；$`z=0`$ 时全部场无质量。
</callout>
**4.** 将27.5节描述过的量子电动力学超对称版中的规范微子场和费米场表示成戈德斯通微子场以及其它有明确质量的旋量场?
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**解 4.**
	令 $`\pm q`$ 是进入 $`D`$ 项和 Yukawa coupling 的实际 $`U(1)`$ 生成元本征值；本节印刷式(27.5.1)的记号对应 $`q=e^2`$。先采用与(27.4.9)、(27.5.12)一致的 canonical normalization：
	$$
				V=m^2(|\phi_+|^2+|\phi_-|^2)
+\frac12\left[\xi+q(|\phi_+|^2-|\phi_-|^2)\right]^2,
\qquad m>0 .
	$$
	当 $`|\xi|\leq m^2/q`$ 时，$`\phi_+=\phi_-=0`$，费米子质量矩阵为
	$$
				M_F\big|_{(\psi_+,\psi_-,\lambda)}
=\begin{pmatrix}0&m&0\\m&0&0\\0&0&0\end{pmatrix}.
	$$
	若 $`\xi\neq0`$，定义
	$$
				g_L=\lambda_L,\qquad
\chi_{1L}=\frac{\psi_{+L}+\psi_{-L}}{\sqrt2},\qquad
\chi_{2L}=\frac{\mathrm i(\psi_{+L}-\psi_{-L})}{\sqrt2}.
	$$
	则
	$$
	m_g=0,\qquad m_{\chi_1}=m_{\chi_2}=m,
	$$
	并且
	$$
				\psi_{+L}=\frac{\chi_{1L}-\mathrm i\chi_{2L}}{\sqrt2},\qquad
\psi_{-L}=\frac{\chi_{1L}+\mathrm i\chi_{2L}}{\sqrt2},\qquad
\lambda_L=g_L.
	$$
	在 $`\xi=0`$ 时同一质量分解成立，但 supersymmetry 没有破缺，$`\lambda`$ 不是 Goldstino。
	当 $`|\xi|>m^2/q`$ 时，令
	$$
				s:=\operatorname{sgn}\xi,\qquad
\Phi_c:=\Phi_{-s},\qquad \Phi_n:=\Phi_s .
	$$
	取 $`\phi_c=v>0,\ \phi_n=0`$，则
	$$
				v^2=\frac{q|\xi|-m^2}{q^2},\qquad
\mathcal F_{n0}=-mv,\qquad
\mathcal F_{c0}=0,\qquad
D_0=s\frac{m^2}{q}.
	$$
	再记
	$$
				a:=\sqrt2\,qv,\qquad
M_H:=\sqrt{m^2+a^2}=\sqrt{2q|\xi|-m^2},\qquad
\widetilde\lambda_L:=\mathrm i s\,\lambda_L .
	$$
	采用与 Goldstino identity (27.5.12) 相容的相对 Yukawa sign，质量矩阵为
	$$
				M_F\big|_{(\psi_n,\psi_c,\widetilde\lambda)}
=\begin{pmatrix}
0&m&0\\
m&0&a\\
0&a&0
\end{pmatrix}.
	$$
	定义
	$$
				\begin{aligned}
g_L&=\frac{-a\psi_{nL}+m\widetilde\lambda_L}{M_H},\\
h_L&=\frac{m\psi_{nL}+a\widetilde\lambda_L}{M_H},\\
\chi_{1L}&=\frac{h_L+\psi_{cL}}{\sqrt2},\qquad
\chi_{2L}=\frac{\mathrm i(h_L-\psi_{cL})}{\sqrt2}.
\end{aligned}
	$$
	直接相乘得到
	$$
				M_F
\begin{pmatrix}-a\\0\\m\end{pmatrix}=0,\qquad
M_Fh_L=M_H\psi_{cL},\qquad
M_F\psi_{cL}=M_Hh_L,
	$$
	因此
	$$
	U^{\mathrm T}M_FU=\operatorname{diag}(0,M_H,M_H).
	$$
	所求原场的展开为
	$$
				\boxed{\begin{aligned}
\psi_{nL}
&=-\frac a{M_H}g_L
+\frac m{\sqrt2M_H}(\chi_{1L}-\mathrm i\chi_{2L}),\\
\psi_{cL}
&=\frac{\chi_{1L}+\mathrm i\chi_{2L}}{\sqrt2},\\
\lambda_L
&=-\mathrm i s\left[
\frac m{M_H}g_L
+\frac a{\sqrt2M_H}(\chi_{1L}-\mathrm i\chi_{2L})
\right].
\end{aligned}}
	$$
	而
	$$
				\left(\mathrm i\sqrt2\,\mathcal F_{n0},\ \mathrm i sD_0\right)
=\frac{\mathrm im}{q}(-a,m),
	$$
	正是零本征矢量方向，故 $`g`$ 是 normalized Goldstino，$`\chi_1,\chi_2`$ 的质量均为 $`M_H`$。
	**Normalization/sign audit.** 印刷式(27.5.1)缺少与(27.4.9)一致的 $`1/2`$。若逐字采用它，则
	$$
				|\xi|_{\mathrm c}=\frac{m^2}{2q},\qquad
v^2=\frac{2q|\xi|-m^2}{2q^2},\qquad
M_H=\sqrt{2q|\xi|},
	$$
	但此时(27.5.12)中的 $`\lambda`$ 系数必须由 $`D_0`$ 改为 $`2D_0`$ 才能成为零模。另有
	$$
	M_{nA}=-\mathrm i\sqrt2\,((t_A\phi_0)_n)^*
	$$
	才与(27.5.12)的 $`+\mathrm i\sqrt2\,\mathcal F_{n0}`$ 同时相容；印刷式(27.4.30)的 $`+\mathrm i`$ 与它相反。以上主解采用彼此一致的(27.4.9)、(27.5.12) convention。
</callout>
**5.** 考虑有一个 $`S U ( 3 )`$ 规范对称性但没有极多重态的可重整 $`N = 2`$ 超对称理论.
使得势为零的标量场的值是什么? 对这些标量不为零的值, 无质量规范场是什么? 计算出中心荷, 并用与这些无质量玻色场耦合的量表示它.
<callout icon="https://upload.wikimedia.org/wikipedia/commons/c/ca/1x1.png" color="gray_bg">
	**解 5.**
	取
	$$
			T^a=\frac{\lambda^a}{2},\qquad
[T^a,T^b]=\mathrm if^{abc}T^c,\qquad
C^{abc}=gf^{abc},\qquad
\Phi_\infty:=\phi_aT^a .
	$$
	纯 $`N=2`$ theory 的势为
	$$
			V=2g^2\sum_a
\left(f^{abc}\operatorname{Re}\phi_b\operatorname{Im}\phi_c\right)^2 .
	$$
	因此
	$$
			V=0
\iff[\operatorname{Re}\Phi_\infty,\operatorname{Im}\Phi_\infty]=0
\iff[\Phi_\infty,\Phi_\infty^\dagger]=0 .
	$$
	两个 commuting Hermitian matrices 可同时对角化，故每个真空均 gauge-equivalent 于
	$$
			\boxed{\;
\Phi_\infty=a_3T^3+a_8T^8
=\operatorname{diag}(v_1,v_2,v_3),\qquad
v_1+v_2+v_3=0\; }
	$$
	其中
	$$
			v_1=\frac{a_3}{2}+\frac{a_8}{2\sqrt3},\qquad
v_2=-\frac{a_3}{2}+\frac{a_8}{2\sqrt3},\qquad
v_3=-\frac{a_8}{\sqrt3},
	$$
	且 $`(a_3,a_8)\in\mathbb C^2`$ 模 Weyl group $`S_3`$。
	在 $`(T^3,T^8)`$ basis 中，三个正根为
	$$
			\alpha_{12}=(1,0),\qquad
\alpha_{23}=\left(-\frac12,\frac{\sqrt3}{2}\right),\qquad
\alpha_{13}=\left(\frac12,\frac{\sqrt3}{2}\right).
	$$
	根方向 gauge boson 的质量由标量动能项给出：
	$$
			\boxed{\;M_{W_\alpha}=\sqrt2\,g\,|\alpha\!\cdot\!a|
=\sqrt2\,g\,|v_i-v_j|\; }.
	$$
	因此 massless gauge fields 分类为
	$$
			\begin{array}{c|c|c}
\text{locus}&\text{additional massless fields}&\text{unbroken group}\\ \hline
\alpha\!\cdot\!a\neq0\ \forall\alpha&A_\mu^3,A_\mu^8&U(1)_3\times U(1)_8\\
a_3=0&A_\mu^{1},A_\mu^{2}&SU(2)_{12}\times U(1)\\
a_3=\sqrt3a_8&A_\mu^{6},A_\mu^{7}&SU(2)_{23}\times U(1)\\
a_3=-\sqrt3a_8&A_\mu^{4},A_\mu^{5}&SU(2)_{13}\times U(1)\\
a_3=a_8=0&A_\mu^1,\ldots,A_\mu^8&SU(3)
\end{array}
	$$
	每一行还包含相应的 Cartan gauge fields。
	在 generic vacuum，定义与两个无质量 Abelian gauge fields 耦合的 electric/magnetic charges
	$$
			q_I:=\oint_{S_\infty^2}\mathrm dS_i\,E_I^i,\qquad
\mathcal M_I:=\oint_{S_\infty^2}\mathrm dS_i\,B_I^i,
\qquad I=3,8 .
	$$
	把(27.9.17)的 surface term 分别投影到两个 Cartan directions，得到
	$$
			\boxed{\;
Z_{12}=2\sqrt2\sum_{I=3,8}a_I
\left(\mathrm iq_I-\mathcal M_I\right)
=2\sqrt2\,\boldsymbol a\!\cdot\!
(\mathrm i\boldsymbol q-\boldsymbol{\mathcal M})\; }.
	$$
	于是
	$$
			M_{\mathrm{BPS}}=\frac{|Z_{12}|}{2}
=\sqrt2\,\left|
\boldsymbol a\!\cdot\!
(\mathrm i\boldsymbol q-\boldsymbol{\mathcal M})
\right|.
	$$
	对根 $`\alpha`$ 的 $`W`$ boson，
	$$
			\boldsymbol q=\pm g\alpha,\qquad
\boldsymbol{\mathcal M}=0,
	$$
	所以
	$$
			M_{\mathrm{BPS}}=\sqrt2\,g|\alpha\!\cdot\!a|
=M_{W_\alpha}.
	$$
	若取 simple roots $`\alpha_i`$，完整 charge lattice 可写为
	$$
			\boldsymbol q=g\sum_i n_e^i\alpha_i,\qquad
\boldsymbol{\mathcal M}=\frac{4\pi}{g}
\sum_i n_m^i\alpha_i^\vee,
	$$
	从而
	$$
			Z_{12}=2\sqrt2\sum_i
(\boldsymbol a\!\cdot\!\alpha_i)
\left(\mathrm ig\,n_e^i-\frac{4\pi}{g}n_m^i\right).
	$$
	在 $`SU(2)\times U(1)`$ enhancement wall 上，$`\alpha\!\cdot\!a=0`$ 的非 Abelian charges 对 $`Z_{12}`$ 的贡献为零；原点处 $`Z_{12}=0`$。
	这里 electric sign 采用印刷式(27.9.22)的 convention。若逐字把(27.9.20)、(27.9.21)代入，则 electric term 符号相反；两者由 $`q_I\mapsto-q_I`$，即反转 $`E_I^i`$ 的定义联系。
</callout>
<empty-block/>
</content>
</page>
