### 题目描述

给定一个含有 n 个数的序列 a_1,a_2...a_n需要支持两种操作：

Q l r k 表示查询下标在区间 [l,r] 中的第 k 小的数

C x y 表示将 a_x改为 y

### 输入描述

```
第一行两个正整数 n,m，表示序列长度与操作个数。
第二行 n 个整数，表示 a_1,a_2...a_n。
接下来 m 行，每行表示一个操作，都为上述两种中的一个。
```
### 输出描述

```
对于每一次询问，输出一行一个整数表示答案。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 3
3 2 1 4 7
Q 1 4 3
C 2 6
Q 2 5 3
```
```
3
6
```
```
无
```

### 题目来源  
`luogu.com.cn`