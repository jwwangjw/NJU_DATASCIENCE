temp = input().split('"')
s = temp[1]
t = temp[3]
d = {}
for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for i in t:
    if i in d.keys():
        if d[i] == 1:
            del d[i]
        else:
            d[i] -= 1
    else:
        print('false')
        break
else:
    if len(d) != 0:
        print('false')
    else:
        print('true')