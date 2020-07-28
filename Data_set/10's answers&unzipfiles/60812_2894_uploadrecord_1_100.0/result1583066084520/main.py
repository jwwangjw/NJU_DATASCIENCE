n = int(input())
s = input()
res = label = 0
for i in s:
    if i == 'V':
        label += 1
    elif label != 0:
        if label > 2:
            res += 2
        else:
            res += 1
        label = 0
if label > 1:
    res += 1
print(res,end='')