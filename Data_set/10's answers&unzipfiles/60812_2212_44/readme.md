## 题目描述
给定数字x，您的任务是查找此数字是否为不足数字。如果由divisorsSum（x）表示的数字的所有除数的总和小于数字x的值的两倍，则将数字x称为不足数。这两个值之间的差异称为缺陷。 从数学上讲，如果满足以下条件，则该数字称为“deficiency”：

从数学上讲，如果满足以下条件，则该数字称为“不足”：

divisorsSum(x) < 2*x

deficiency = (2*x) - divisorsSum(x)
## 输入输出描述
Input: 21

Output: 1

除数分别为1、3、7和21。除数之和为32。该总和小于2 * 21或42。

Input: 12

Output: 0

Input: 17

Output: 1

## 样例输入
3

21

12

17
## 样例输出
1

0

1
## 题目来源
geeksforgeeks.org