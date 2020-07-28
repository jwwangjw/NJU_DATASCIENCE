### 题目描述

有一个整数 n 用以 b 为底的 k 位数表示：

`n = a[1]*b^(k-1) + a[2]*b^(k-2) + ... + a[k-1]*b + a[k]`

例如, 如果 `b=17，k=3，a=[11, 15, 7]`，则  `n=11*17^2+15*17+7`

请判断 n 是奇数还是偶数。

### 输入描述

```
第一行为两个整数底数 b 和位数 k (2 ≤ b ≤ 100， 1 ≤ k ≤ 10^5)
第二行包含 k 个整数(0 ≤ ai ≤ b)
n 的表述不包含不必要的前导0. 即只有当 k = 1时，a₁ 等于 0
```

### 输出描述

```
若 n 为偶数，输出 even，否则输出 odd
```

### 测试样例

#### 样例1: 输入-输出

```
13 3
3 2 7
```

```
even
```

#### 样例2: 输入-输出

```
10 9
1 2 3 4 5 6 7 8 9
```

```
odd
```

#### 样例3: 输入-输出

```
99 5
32 92 85 74 4
```

```
odd
```

### 题目来源

CodeForces