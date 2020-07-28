friends = eval(input())
cir = []
result = []
check = True
for x in range(len(friends)):
    cir.append([])
for i in range(len(friends)):
    for j in range(len(friends)):
        if friends[i][j] == 1:
            cir[i].append(j)
for e in range(len(cir)):
    for f in cir[:e] + cir[e + 1:]:
        if set(cir[e]).issubset(f):
            check = False
            if cir[e] == f and cir[e] not in result:
                result.append(cir[e])
    if check:
        result.append(cir[e])
    check = True
print(len(result))