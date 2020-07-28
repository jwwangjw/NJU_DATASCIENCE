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
    # 判断是否为单调序列,即 / 或者 \
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
    # 也有可能是先单调增再单调减/\，同时也包含了中间相等的部分
    judge = 1
    for i in range(count_up, l-1):
        if d[i] < d[i+1]:
            judge = 0
            break
    if judge == 1:
        return 1
    else:
        return 0


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

