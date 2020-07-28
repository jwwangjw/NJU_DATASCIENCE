### 题目描述

给定一颗二叉树，分别实现按层和 ZigZag 打印二叉树。
ZigZag遍历: 意思是第一层从左到右遍历，第二层从右到左遍历，依次类推。


### 输入描述

```
第一行输入两个整数 n 和 root，n 表示二叉树的总节点个数，root 表示二叉树的根节点。
以下 n 行每行三个整数 fa，lch，rch，表示 fa 的左儿子为 lch，右儿子为 rch。(如果 lch 为 0 则表示 fa 没有左儿子，rch同理)
```
### 输出描述

```
先输出按层打印，再输出按ZigZag打印。
```

### 测试样例
#### 样例1:输入-输出-解释

```
8 1
1 2 3
2 4 0
4 0 0
3 5 6
5 7 8
6 0 0
7 0 0
8 0 0
```
```
Level 1 : 1
Level 2 : 2 3
Level 3 : 4 5 6
Level 4 : 7 8
Level 1 from left to right: 1
Level 2 from right to left: 3 2
Level 3 from left to right: 4 5 6
Level 4 from right to left: 8 7
```
```
无
```

### 题目来源  
`nowcoder.com`