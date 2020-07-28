### 题目描述

众所周知，二叉查找树的形态和键值的插入顺序密切相关。准确的讲：1、空树中加入一个键值k，则变为只有一个结点的二叉查找树，此结点的键值即为k；2、在非空树中插入一个键值k，若k小于其根的键值，则在其左子树中插入k，否则在其右子树中插入k。

我们将一棵二叉查找树的键值插入序列称为树的生成序列，现给出一个生成序列，求与其生成同样二叉查找树的所有生成序列中字典序最小的那个，其中，字典序关系是指对两个长度同为n的生成序列，先比较第一个插入键值，再比较第二个，依此类推。


### 输入描述

```
第一行，一个整数，n，表示二叉查找树的结点个数。第二行，有n个正整数，k1到kn，表示生成序列，简单起见，k1~kn为一个1到n的排列。
```
### 输出描述

```
一行，n个正整数，为能够生成同样二叉查找数的所有生成序列中最小的。
```

### 测试样例
#### 样例1:输入-输出-解释

```
4
1 3 4 2
```
```
1 3 2 4
```
```
无
```

### 题目来源  
`luogu.com.cn`