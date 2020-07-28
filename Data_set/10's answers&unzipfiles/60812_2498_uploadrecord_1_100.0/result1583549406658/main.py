nums = [int(i) for i in input()[1:-1].split(',')]
n = len(nums)
s = []
d = []
for i in range(n):
    if nums[i] % 2 == 0:
        s.append(nums[i])
    else:
        d.append(nums[i])
print('[', end='')
temp = n//2-1
for i in range(temp):
    print("{}, {}".format(s[i], d[i]), end=',')
print("{}, {}]".format(s[temp], d[temp]))