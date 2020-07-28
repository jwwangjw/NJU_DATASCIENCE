"""
花园浇花
不能够重复，不能剩余
1.花园长度必须能够被选择的那一个水桶整除
2.浇花的时间最短
"""
import sys
# 先将一行数据作为字符串读取进来，再根据空格切片
line1 = input().split(" ")
line2 = input().split(" ")
bucket = int(line1[0])
length = int(line1[1])
time = 0
# min开始取整数最大值
min_time = sys.maxsize
for i in line2:
    per_hour = int(i)
    # 读取每小时长度，先判断能否整除，再判断是否比前一个小
    if length % per_hour == 0:
        time = length // per_hour
    if time < min_time:
        min_time = time
print(min_time)
