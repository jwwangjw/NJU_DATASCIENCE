### 题目描述

Are you going to solve poisonous problems?
- Thanks a lot for today's poisonous problems.

What are you doing at the end of the world? Are you busy? Will you save us?

Ithea and Chtholly want to play a game in order to determine who will solve poisonous problems.
- Willem...

Lakhesh loves to make poisonous problems, so Nephren helps her run a cinema. We may call it No. 68 Cinema.
- I... I survived.

如题目背景所述，这是一道 PSP（Poisonous String Problem，毒瘤字符串题）。

对于一个正整数k，若任何一个1~n的排列均是某个字符集大小不超过k的字符串的后缀排名数组（后缀排名数组即后缀数组的逆排列，如果你不知道什么是后缀数组，可以自行搜索或参考Wiki 对后缀数组的介绍），
则称k对于n是毒瘤的。给定k，你需要找到一个最小的正整数n使k对于n不是毒瘤的，并且你需要给出1~n的一个排列，其不是任何一个字符集大小不超过k的字符串的后缀排名数组。如果有多个排列，输出字典序最小的，如果不存在这样的n和排列，输出 213。

### 输入描述

```
输入仅包含一个正整数k。

数据范围：对于所有数据，1≤k≤10^5。
```
### 输出描述

```
输出包含一至两行。
若无解，输出一行一个字符串 213。
若有解，第一行包含一个正整数n，之后一行n个空格隔开的正整数表示排列。
```

### 测试样例
#### 样例1:输入-输出-解释

```
1
```
```
2
1 2
```
```
字符集为1,长也为1的字符串a的后缀排名数组为1,包含了所有长为1的排列,所以k= 1对于n= 1毒瘤的。
字符集为1,长为2的唯一一个字符串aa的后缀排名数组为{2,1},故{1,2}不是任何字符集为1的字符串的后缀排名数组,所以k= 1对于n= 2不是毒瘤的,且{1,2}是此时唯一不是后缀排名数组的排列, 也是此时满足条件的字典序最小的排列。
```