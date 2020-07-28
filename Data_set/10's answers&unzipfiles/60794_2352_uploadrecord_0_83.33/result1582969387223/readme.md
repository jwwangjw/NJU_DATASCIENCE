### 题目描述

Nuske 有一个 N行M列的方形网格。行从上到下编号为1到N，列从左到右编号为1到M。网格中的每个单元格都涂成蓝色或白色。如果S<sub>i,j</sub>=1，则第i行第j列的单元格为蓝色；如果S<sub>i,j</sub>=0，则单元格为白色。对于每对蓝色单元格a和b，最多存在一条每步移动到相邻（有公共边）的蓝色单元格，且不重复经过同一个单元格的，从a开始到达b的路径。

Nuske 永恒的对手 Phantom Thnook 向 Nuske 发出了Q次查询。第i次查询由四个整数x<sub>i,1</sub>，y<sub>i,1</sub>，x<sub>i,2</sub>，y<sub>i,2</sub>描述，表示询问：如果从网格中分离出第x<sub>i,1</sub>到x<sub>i,2</sub>行、第y<sub>i,1</sub>到y<sub>i,2</sub>列的部分，在该区域有几个由蓝色单元格组成的四联通块？

请你回答所有查询。

### 输入描述

```
输入从标准输入流按以下形式给出：
```
<p align="left">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E5%9B%9B%E8%81%94%E9%80%9A%E5%9D%97.png" alt="Sample"  width="200" height="200">
</p>

数据范围：
<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E5%9B%9B%E8%81%94%E9%80%9A%E5%9D%973.png" alt="Sample"  width="200" height="92">
</p>

### 输出描述

```
对于每个询问，输出一行一个整数表示该区域内由蓝色单元格组成的四联通块个数。
```

### 测试样例
#### 样例1:输入-输出-解释

```
3 4 4
1101
0110
1101
1 1 3 4
1 1 3 1
2 2 3 4
1 2 2 4
```
```
3
2
2
2
```
样例解释：

<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E5%9B%9B%E8%81%94%E9%80%9A%E5%9D%972.png" alt="Sample"  width="180" height="140">
</p>

第一次查询了整个网格。有三个蓝色单元格组成的四联通块，因此应该输出3。

第二次查询了红框内的区域。有两个蓝色单元格组成的四联通块，因此应该输出2。请注意，在原始网格中属于相同四联通块的单元格在查询中形可能属于不同的四联通块。

### 题目来源  
`AGC015`