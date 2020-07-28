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
    # 单个数字符合单峰
    if l == 1:
        return 1
    # 判断是否为无相等的单调序列
    count_up = 0
    count_down = 0
    for i in range(0, l-1):
        if d[i] < d[i+1]:
            count_up += 1
        if d[i] > d[i+1]:
            count_down += 1
    # 单调递增或递减，符合单峰
    if count_up == l-1 or count_down == l-1:
        return 1
    # 在有相等的情况下，分别从左右两侧进行判断,应该是这样/-\，如果出现递减的情况，则返回false
    # 如果出现相等，break
    for i in range(0, l-1):
        if d[i] > d[i+1]:
            return 0
        if d[i] == d[i+1]:
            break
    for j in range(0, l-1):
        # python特性
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
data_int = []
# 注意这里要先转换为int型，才能够进行比较大小
for x in range(0, length):
    data_int.append(int(data[x]))
res = is_unimodal(length, data_int)
if res == 1:
    print("YES")
else:
    print("NO")
