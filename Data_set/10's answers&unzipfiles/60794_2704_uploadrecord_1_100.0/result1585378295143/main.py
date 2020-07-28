a = eval(input())
parent = []
for i in range(len(a)+1):
    parent.append(i)
res = []
for i in range(len(a)):
    x = a[i][0]
    y = a[i][1]
    while x != parent[x]:
        x = parent[x]
    while y != parent[y]:
        y = parent[y]
    if x == y:
        res.append(a[i])
    else:
        parent[x] = y
print(res[len(res)-1])