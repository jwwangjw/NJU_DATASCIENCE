## 题目描述
<p>求解一个给定的方程，将<code>x</code>以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量&nbsp;<code>x</code>&nbsp;和其对应系数。</p>

<p>如果方程没有解，请返回“No solution”。</p>

<p>如果方程有无限解，则返回“Infinite solutions”。</p>

<p>如果方程中只有一个解，要保证返回值&nbsp;<code>x</code>&nbsp;是一个整数。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> "x+5-3+x=6+x-2"
<strong>输出:</strong> "x=2"
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> "x=x"
<strong>输出:</strong> "Infinite solutions"
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> "2x=x"
<strong>输出:</strong> "x=0"
</pre>

<p><strong>示例 4:</strong></p>

<pre><strong>输入:</strong> "2x+3x-6x=x+2"
<strong>输出:</strong> "x=-1"
</pre>

<p><strong>示例 5:</strong></p>

<pre><strong>输入:</strong> "x=x+2"
<strong>输出:</strong> "No solution"
</pre>