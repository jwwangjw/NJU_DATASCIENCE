### 题目描述
<p>给定一个仅包含数字&nbsp;<code>0-9</code>&nbsp;的字符串和一个目标值，在数字之间添加<strong>二元</strong>运算符（不是一元）<code>+</code>、<code>-</code>&nbsp;或&nbsp;<code>*</code>&nbsp;，返回所有能够得到目标值的表达式。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code><em>num</em> = </code>"123", <em>target</em> = 6
<strong>输出: </strong>["1+2+3", "1*2*3"] 
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code><em>num</em> = </code>"232", <em>target</em> = 8
<strong>输出: </strong>["2*3+2", "2+3*2"]</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> <code><em>num</em> = </code>"105", <em>target</em> = 5
<strong>输出: </strong>["1*0+5","10-5"]</pre>

<p><strong>示例&nbsp;4:</strong></p>

<pre><strong>输入:</strong> <code><em>num</em> = </code>"00", <em>target</em> = 0
<strong>输出: </strong>["0+0", "0-0", "0*0"]
</pre>

<p><strong>示例 5:</strong></p>

<pre><strong>输入:</strong> <code><em>num</em> = </code>"3456237490", <em>target</em> = 9191
<strong>输出: </strong>[]
</pre>
### 样例输入<br>
```
123
6
```
```
第一行为字符串类型
第二行为int类型
```
### 样例输出<br>
```
['1+2+3', '1*2*3']
```
### 题目来源  
`LeetCode`