### 题目描述

给定一棵 n 个节点的树，每个点有一个权值。有 m 个询问，每次给你 u,v,k，你需要回答 u xor last 和 v 这两个节点间第 k 小的点权。

其中 last 是上一个询问的答案，定义其初始为 0，即第一个询问的 u 是明文。

### 输入描述

```
第一行两个整数 n,m。

第二行有 n 个整数，其中第 i 个整数表示点 ii 的权值。

后面 n-1 行每行两个整数 x,y，表示点 x 到点 y 有一条边。

最后 m 行每行两个整数 u,v,k，表示一组询问。
```
### 输出描述

```
m 行，每行一个正整数表示每个询问的答案。
```

### 测试样例
#### 样例1:输入-输出-解释

```
8 5
105 2 9 3 8 5 7 7
1 2
1 3
1 4
3 5
3 6
3 7
4 8
2 5 1
0 5 2
10 5 3
11 5 4
110 8 2
```
```
2
8
9
105
7
```
```
无
```

### 题目来源  
`luogu.com.cn`