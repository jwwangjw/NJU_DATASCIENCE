import math
s = input()
nums = []
for i in s:
    if i.isdigit():
        nums.append(int(i))
n = len(nums)-2
k, t = nums[n], nums[n+1]
for j in range(1,n):
    for i in range(max(0, j-k), j):
        if math.fabs(nums[j]-nums[i]) <= t:
            print('true')
            break
    else:
        continue
    break
else:
    print('false')