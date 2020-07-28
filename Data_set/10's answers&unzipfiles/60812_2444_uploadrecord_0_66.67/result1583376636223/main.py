import math
s = input()
nums = []
for i in s:
    if i.isdigit():
        nums.append(int(i))
n = len(nums)-2
k, t = nums[n], nums[n+1]
for i in range(n-1):
    for j in range(1, n):
        if math.fabs(nums[j]-nums[i]) <= t:
            sub = 0
            for k in range(i+1, j-1):
                for l in range(k+1,j):
                    sub = max(sub, math.fabs(nums[l]-nums[k]))
            if sub <= k:
                print('true')
                break
    else:
        continue
    break
else:
    print('false')