### 题目描述

在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。

（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。

返回区域的数目。

### 输入描述

```
一个表示网格划分的数组。
1 <= grid.length == grid[0].length <= 30
grid[i][j] 是 '/'、'\'、或 ' '。
```
### 输出描述

```
返回区域的数目。
```

### 测试样例
#### 样例1: 输入-输出-解释
```
[
  " /",
  "/ "
]
```
```
2
```
```
2x2 网格如下：
```
<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E7%94%B1%E6%96%9C%E6%9D%A0%E5%88%92%E5%88%86%E5%8C%BA%E5%9F%9F.png" alt="Sample"  width="90" height="90">
</p>
#### 样例2: 输入-输出-解释
```
[
  "/\\",
  "\\/"
]
```
```
5
```
```
（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
2x2 网格如下：
```
<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E7%94%B1%E6%96%9C%E6%9D%A0%E5%88%92%E5%88%86%E5%8C%BA%E5%9F%9F2.png" alt="Sample"  width="90" height="90">
</p>
#### 样例3: 输入-输出-解释
```
[
  " /",
  "  "
]
```
```
1
```
```
2x2 网格如下：
```
<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E7%94%B1%E6%96%9C%E6%9D%A0%E5%88%92%E5%88%86%E5%8C%BA%E5%9F%9F3.png" alt="Sample"  width="90" height="90">
</p>
### 题目来源  
`LeetCode`