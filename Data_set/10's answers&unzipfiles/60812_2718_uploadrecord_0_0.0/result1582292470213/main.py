s = input()
pairs = [{int(i[0]), int(i[2])} for i in input()[2:-2].split('],[')]
union = []
n = len(pairs)
label = [True for i in range(n)]
for i in range(n-1):
    temp = set()
    for j in range(i+1, n):
        if len(pairs[i] & pairs[j]) != 0:
            temp.add(j)
    union.append(temp)
union.append(set())
group = []
for i in range(n-1):
    if label[i]:
        while len(union[i]) != 0:
            temp = set()
            for j in union[i]:
                label[j] = False
                pairs[i] |= pairs[j]
                temp |= union[j]
            union[i] = temp
        group.append(pairs[i])
if label[n-1]:
    group.append(pairs[n-1])
sd = {}
for i in group:
    temp = []
    for j in i:
        temp.append(s[j])
    temp.sort()
    i = sorted(i)
    for j in range(len(i)):
        sd[i[j]] = temp[j]
for i in range(len(s)):
    if i in sd.keys():
        print(sd[i], end='')
    else:
        print(s[i], end='')