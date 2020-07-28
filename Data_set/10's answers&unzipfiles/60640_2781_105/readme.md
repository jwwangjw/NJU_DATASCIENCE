### 题目描述

给出一些数字串，判断是否有一个数字串是另一个串的前缀。

数字串只包含0，1，记每个数字串长度为l，则1≤l≤10。每组数据至少有2个数字串，至多有8个数字串。
### 输入描述

```
输入数据为多组数据，每组数据读到9时结束。
```
### 输出描述

```
对于每组数据，如果不存在一个数字串是另一个串的前缀，输出一行 Set t is immediately decodable ，否则输出一行 Set t is not immediately decodable ，其中t是这一组数据的组号。
```

### 测试样例
#### 样例1:输入-输出-解释

```
01
10
0010
0000
9
01
10
010
0000
9
```
```
Set 1 is immediately decodable
Set 2 is not immediately decodable
```
```
无
```

### 题目来源  
`loj.ac`