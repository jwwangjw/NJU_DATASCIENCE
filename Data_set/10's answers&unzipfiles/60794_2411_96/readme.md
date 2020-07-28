### 题目描述
<p>在一个&nbsp;XY 坐标系中有一些点，我们用数组&nbsp;<code>coordinates</code>&nbsp;来分别记录它们的坐标，其中&nbsp;<code>coordinates[i] = [x, y]</code>&nbsp;表示横坐标为 <code>x</code>、纵坐标为 <code>y</code>&nbsp;的点。</p>

<p>请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 <code>true</code>，否则请返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img style="height: 336px; width: 336px;" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-2.jpg" alt=""></p>

<pre><strong>输入：</strong>coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
<strong>输出：</strong>True
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img style="height: 336px; width: 348px;" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-1.jpg" alt=""></strong></p>

<pre><strong>输入：</strong>coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
<strong>输出：</strong>False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;=&nbsp;coordinates.length &lt;= 1000</code></li>
	<li><code>coordinates[i].length == 2</code></li>
	<li><code>-10^4 &lt;=&nbsp;coordinates[i][0],&nbsp;coordinates[i][1] &lt;= 10^4</code></li>
	<li><code>coordinates</code>&nbsp;中不含重复的点</li>
</ul>
### 样例输入<br>
```
6
1,2
2,3
3,4
4,5
5,6
6,7
```
### 样例输出<br>
```
True
```
```
第一行N为N个点，接下来N行为每个点的坐标
```
### 题目来源  
`LeetCode`
