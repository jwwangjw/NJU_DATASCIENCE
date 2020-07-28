s = input()
t = input()
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
        print('False')
        break
else:
    if len(d) != 0:
        print('False')
    else:
        print('True')