a = list(input())
b = []
d = {}
for i in range(len(a)):
    if a[i] == "":
        continue
    b.append(a[i])
    num = 1
    for j in range(i+1, len(a)):
        if a[i] == a[j] and a[j] != "":
            b.append(a[j])
            a[j] = ""
            num = num + 1
    d[a[i]] = num
key = list(dict.keys(d))
v = list(dict.values(d))
ans = []
for i in range(len(v)):
    x = list.index(v, max(v))
    for j in range(max(v)):
        ans.append(key[x])
    v[x] = -1
print("".join(ans))