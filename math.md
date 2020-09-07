機械学習のための<br>関数解析学の基礎

2020-08-29

---

### 目的
- 関数解析学をまとめる
- 機械学習を見通しよく理解することを目的とする
- 集合，線形代数，微分積分（特に，ルベーグ積分），確率論の基礎を過程する

---

### 記号の約束
- $\mathbb{Q}$，$\mathbb{R}$，$\mathbb{C}$を有理数，実数，複素数とする．
- $V$をベクトル空間とする．
- $\mathcal{B}$をバナッハ空間とする．
- $\mathcal{H}$をヒルベルト空間とする．

---

### 内積

**[Def]**<br>
実線形空間$V$の任意の2元$f,g$に対して一つの実数(複素線形空間の場合，複素数)を対応させる関数$\langle f,g \rangle$が次の条件を満たすとき，
関数$\langle \cdot, \cdot \rangle: V \times V \rightarrow \mathbb{R}$を内積と定義する．
1. $\langle g, f \rangle = \langle f, g \rangle$
1. $\langle af+bg, h \rangle = a\langle f, h \rangle + b\langle g, h \rangle$
1. $\langle f, f \rangle \geq 0$かつ等号が成立するのは$f=0$の場合に限る．

内積が定義された線形空間を内積空間という．
内積空間にはノルムを定義することができる．
内積空間の任意の元$f$に対して
$$
||f|| = \sqrt{\langle f, f \rangle}
$$
と定義するとき，これを内積から自然に導かれるノルムという．
内積空間は$||f||$に関してノルム空間になる．

---

### ヒルベルト空間
**[Def]**<br>
完備な内積空間をヒルベルト空間という．

このスライドでは，ヒルベルト空間のうち可分なもののみを対象として考える．

---

### 部分空間

---

### 直交

---

### 有界線形汎関数

---

### リースの表現定理
**[Thm]**

---

### ニューラルネットワークの普遍性定理

[Cybenko, George. "Approximation by superpositions of a sigmoidal function." Mathematics of control, signals and systems 2.4 (1989): 303-314.][cybenko]

**[Def]** sigmoidal関数<br>
関数$\sigma:\mathbb{R} \rightarrow \mathbb{R}$が次の条件をみたすとき，sigmoidal関数と定義する．

$$
  \sigma \rightarrow
    \begin{cases}
      1 & (t \rightarrow +\infty) \\\\
      0 & (t \rightarrow -\infty)
    \end{cases}
$$

**[Thm]** 普遍性定理<br>
$\sigma:\mathbb{R} \rightarrow \mathbb{R}$を連続なsigmoidal関数とすると，
$$
  G(x) = \sum^N\_{j=1} \alpha\_j \sigma(\langle x,y\_j \rangle + \theta\_j)
$$
という形をした$X$上の関数全体の集合$C(X)$で稠密になる．

すなわち，任意の$f \in C(X)$と任意の正数$\epsilon$に対して，上の形で表現される関数$G$を適当にとれば，
$$
  \forall x \in X,|f(x)-G(x)|< \epsilon
$$
が成立する．ここで$\alpha\_j \in \mathbb{R}, y\_j \in \mathbb{R}^n$であり，$\langle x,y \rangle$は内積である．

[鈴木先生のスライド][taiji2]より概説を引用

---

### ガウス過程回帰

---


### 再生核ヒルベルト空間（RKHS）

---

### 再生核の定義

---

### RKHSにおけるガウス過程回帰の理解

---

### 参考資料
- [「集合と位相」をなぜ学ぶのか ― 数学の基礎として根づくまでの歴史　(藤田博司)][fujita]
- [固有値問題30講　(志賀浩二)][shiga1]
- [ルベーグ積分30講　(志賀浩二)][shiga2]
- [測度・確率・ルベーグ積分 応用への最短コース　(原啓介)][hara]
- [工学のための関数解析　(山田功)][yamada]
- [工学系の関数解析　(小川英光)][ogawa]
- [深層学習の数理　大阪大学集中講義　(鈴木大慈)][taiji1]
- [深層学習の数理：カーネル法，スパース推定との接点　(鈴木大慈)][taiji2]

[cybenko]:https://link.springer.com/article/10.1007/BF02551274
[fujita]:https://gihyo.jp/book/2018/978-4-7741-9612-1
[shiga1]:https://www.asakura.co.jp/books/isbn/978-4-254-11485-0/
[shiga2]:https://www.asakura.co.jp/books/isbn/978-4-254-11484-3/
[hara]:https://bookclub.kodansha.co.jp/product?item=0000149472
[yamada]:https://www.saiensu.co.jp/search/?isbn=978-4-901683-62-3&y=2009
[ogawa]:https://www.morikita.co.jp/books/book/445
[taiji1]:https://www.slideshare.net/trinmu/ss-161240890
[taiji2]:https://www.slideshare.net/trinmu/ss-237399755
