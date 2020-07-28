"""
2.19
只出现一次的数字
运用list.count可以计算数组中元素出现的次数
"""
import re
# 运用正则，使用多个元素拆分字符串
data = re.split(r"[\[\],]", input())
# 首尾为空，删去，就能够得到数据数组
del data[0]
del data[-1]
for c in data:
    num = data.count(c)
    if num == 1:
        print(int(c))
        break
