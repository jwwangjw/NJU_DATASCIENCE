### 题目描述

给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：


	每次转换只能改变一个字母。
	转换过程中的中间单词必须是字典中的单词。


说明:


	如果不存在这样的转换序列，返回一个空列表。
	所有单词具有相同的长度。
	所有单词只由小写字母组成。
	字典中不存在重复的单词。
	你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

### 输入描述

```
两个单词（beginWord 和 endWord）和一个字典 wordList
```
### 输出描述

```
所有从 beginWord 到 endWord 的最短转换序列
```

### 测试样例
#### 样例1: 输入-输出-解释
```
hit
cog
["hot","dot","dog","lot","log","cog"]
```
```
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```
### 题目来源  
`LeetCode`