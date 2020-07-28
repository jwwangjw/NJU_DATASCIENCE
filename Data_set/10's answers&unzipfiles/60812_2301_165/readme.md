### 题目描述

字典树又称为前缀树或者Trie树，是处理字符串常用的数据结构。假设组成所有单词的字符仅是‘a’～‘z’，请实现字典树的结构，并包含以下四个主要的功能。void insert(String word)：添加word，可重复添加；void delete(String word)：删除word，如果word添加过多次，仅删除一次；boolean search(String word)：查询word是否在字典树中出现过(完整的出现过，前缀式不算)；int prefixNumber(String pre)：返回以字符串pre作为前缀的单词数量。现在给定一个m，表示有m次操作，每次操作都为以上四种操作之一。每次操作会给定一个整数op和一个字符串word，op代表一个操作码，如果op为1，则代表添加word，op为2则代表删除word，op为3则代表查询word是否在字典树中，op为4代表返回以word为前缀的单词数量（数据保证不会删除不存在的word）。


### 输入描述
输入包含多行，第一行一个整数m(1≤m≤10^5)，代表操作次数。接下来m行，每行包含一个整数op(1≤op≤4)，和一个字符串word(1≤length(word)≤20)。

### 输出描述

```
对于每次操作，如果op为3时，如果word在字典树中，请输出“YES”，否则输出“NO”；如果op为4时，请输出返回以word为前缀的单词数量，其它情况不输出。
```

### 测试样例
#### 样例1:输入-输出-解释

```
7
1 qwer
1 qwe
3 qwer
4 q
2 qwer
3 qwer
4 q
```
```
YES
2
NO
1
```
```
无
```

### 题目来源  
`nowcoder.com`