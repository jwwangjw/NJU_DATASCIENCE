## 题目描述
<p>验证给定的字符串是否可以解释为十进制数字。</p>

<p>例如:</p>

<p><code>"0"</code>&nbsp;=&gt;&nbsp;<code>true</code><br>
<code>" 0.1 "</code>&nbsp;=&gt;&nbsp;<code>true</code><br>
<code>"abc"</code>&nbsp;=&gt;&nbsp;<code>false</code><br>
<code>"1 a"</code>&nbsp;=&gt;&nbsp;<code>false</code><br>
<code>"2e10"</code>&nbsp;=&gt;&nbsp;<code>true</code><br>
<code>" -90e3&nbsp; &nbsp;"</code>&nbsp;=&gt;&nbsp;<code>true</code><br>
<code>" 1e"</code>&nbsp;=&gt;&nbsp;<code>false</code><br>
<code>"e3"</code>&nbsp;=&gt;&nbsp;<code>false</code><br>
<code>" 6e-1"</code>&nbsp;=&gt;&nbsp;<code>true</code><br>
<code>" 99e2.5&nbsp;"</code>&nbsp;=&gt;&nbsp;<code>false</code><br>
<code>"53.5e93"</code>&nbsp;=&gt;&nbsp;<code>true</code><br>
<code>" --6 "</code>&nbsp;=&gt;&nbsp;<code>false</code><br>
<code>"-+3"</code>&nbsp;=&gt;&nbsp;<code>false</code><br>
<code>"95a54e53"</code>&nbsp;=&gt;&nbsp;<code>false</code></p>

<p><strong>说明:</strong>&nbsp;我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：</p>