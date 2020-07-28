s = input()
pairs = [{int(i[0]), int(i[2])} for i in input()[2:-2].split('],[')]
n = len(pairs)
belong = [i for i in range(n)]
for i in range(n-1):
    if pairs[i] != 0:
        for j in range(i + 1, n):
            if pairs[j] == 0:
                while j != belong[j]:
                    j = belong[j]
            if len(pairs[i] & pairs[j]) != 0:
                pairs[i] |= pairs[j]
                belong[j] = i
                pairs[j] = 0
m = pairs.count(0)
for i in range(m):
    pairs.remove(0)
sd = {}
for i in pairs:
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
print()