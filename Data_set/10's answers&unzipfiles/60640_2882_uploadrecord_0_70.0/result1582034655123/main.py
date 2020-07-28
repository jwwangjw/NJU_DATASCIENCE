"""
2.18
单峰数组
一个数组是单峰的（Unimodal），如果：
第一部分：严格递增
第二部分：连续常数
第三部分：严格递减
第一部分和第三部分允许没有
"""


def is_unimodal(l, d):
    i = 0
    j = 0
    # 分别从左右两侧进行判断，如果出现递减的情况，则返回false
    # 如果出现相等，break
    for i in range(0, l-1):
        if d[i] > d[i+1]:
            return 0
        if d[i] == d[i+1]:
            break
    for j in range(0, l-1):
        if d[-j - 1] > d[-j - 2]:
            return 0
        if d[-j-1] == d[-j-2]:
            break
    # 上面保证了一三部分，下面判断中间连续常数的部分
    for k in range(i, l-j-1):
        if d[k] != d[k+1]:
            return 0
    return 1


length = int(input())
data = input().split(" ")
res = is_unimodal(length, data)
if res == 1:
    print("YES")
else:
    print("NO")



