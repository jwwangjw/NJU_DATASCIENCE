### 题目描述

<p align="center">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E5%B0%8FY%E5%92%8C%E5%9C%B0%E9%93%81.png" alt="Sample"  width="800" height="325">
</p>

### 输入描述

```
请注意本题有多组输入数据。
输入数据的第一行是一个整数T，表示输入数据的组数。接下来依次给出每组数据。
对于每组数据，第一行是一个整数n，表示小Y经过的换乘站的数目。第二行为n个用空格隔开的整数，依次表示每个换乘站的可以换乘的线路编号。这些编号都在1到n之内。

数据范围：1≤T≤100,1≤n≤44
```
### 输出描述

```
对于每组输入数据，输出一行一个整数，表示除掉这n个换乘站之外，最少有几个换乘站。
```

### 测试样例
#### 样例1:输入-输出-解释

```
4
4
1 2 1 2
8
1 2 3 4 1 2 3 4
5
5 4 3 3 5
8
1 2 3 4 1 3 2 4
```
```
0
0
0
1
```
样例解释：

对于样例的前两组数据，一种可能的最优答案如下图所示。

<p align="center">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E5%B0%8FY%E5%92%8C%E5%9C%B0%E9%93%812.png" alt="Sample"  width="500" height="450">
</p>

### 题目来源  
`清华集训`