### 题目描述
<p>给定只含&nbsp;<code>"I"</code>（增大）或 <code>"D"</code>（减小）的字符串&nbsp;<code>S</code>&nbsp;，令&nbsp;<code>N = S.length</code>。</p>

<p>返回&nbsp;<code>[0, 1, ..., N]</code>&nbsp;的任意排列&nbsp;<code>A</code>&nbsp;使得对于所有&nbsp;<code>i = 0,&nbsp;..., N-1</code>，都有：</p>

<ul>
	<li>如果&nbsp;<code>S[i] == "I"</code>，那么&nbsp;<code>A[i] &lt; A[i+1]</code></li>
	<li>如果&nbsp;<code>S[i] == "D"</code>，那么&nbsp;<code>A[i] &gt; A[i+1]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输出：</strong>"IDID"
<strong>输出：</strong>[0,4,1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输出：</strong>"III"
<strong>输出：</strong>[0,1,2,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输出：</strong>"DDI"
<strong>输出：</strong>[3,2,0,1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 1000</code></li>
	<li><code>S</code> 只包含字符&nbsp;<code>"I"</code>&nbsp;或&nbsp;<code>"D"</code>。</li>
</ol>
### 样例输入<br>
```
IDID
```
### 样例输出<br>
```
[0,4,1,3,2]
```
### 题目来源  
`LeetCode`
