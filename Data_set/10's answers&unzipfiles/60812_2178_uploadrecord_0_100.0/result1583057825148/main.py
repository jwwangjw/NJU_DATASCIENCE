n = int(input())
nums = input().split(' ')
res = 0
s = []
for i in range(n):
    for j in range(0, i+1):
        temp = nums[j:i+1]
        if temp not in s:
            s.append(temp)
            res += 1
    print(res)