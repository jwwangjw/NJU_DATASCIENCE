### 题目描述

给出一个由 n 个整数组成的数组 a[1]，a[2]，…，a[n]。你可以选择任何非负整数 D，对每个 a[i] 可以进行三种操作： 

1. 使该数加上一个 D 即执行 ai = ai + D 

2. 使该数减去一个 D 即执行 ai = ai - D 

3. 不对该数字进行任何操作

运算后值 ai 可能变成负数。 你的目标是选择一个最小非负整数 D 使得每个 a[i] 经过上述操作的其中一种后，能够全部相等 。 

### 输入描述

```
第一行输入 n (1<=n<=100) 
第二行输入数组 a[i] (1<=a[i]<=100)
```

### 输出描述

```
输出一个数表示最小非负整数 D，如果不存在，输出 -1
```

### 测试样例

#### 样例1: 输入-输出

```
6
1 4 4 7 4 1
```

```
3
```

#### 样例2: 输入-输出

```
5
2 2 5 2 5
```

```
3
```

### 题目来源

CodeForces