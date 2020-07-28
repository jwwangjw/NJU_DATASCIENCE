a = input()
b = input()
if len(a) > len(b):
    a, b = b, a
res = 0
d = {}
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        temp = a[i:j]
        if temp in d.keys():
            d[temp][0] += 1
        else:
            d[temp] = [1, 0]
for i in range(len(b)):
    for j in range(i+1, len(b)+1):
        temp = b[i:j]
        if temp in d.keys():
            d[temp][1] += 1
for i, j in d.values():
    res += i*j
print(res, end='')