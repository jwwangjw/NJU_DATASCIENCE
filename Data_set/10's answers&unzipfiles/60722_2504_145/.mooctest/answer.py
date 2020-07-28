points = eval(input())
distance = sorted([x[0]*x[0]+x[1]*x[1] for x in points])
result = []
for i in distance:
    for j in points:
        if j[0]*j[0]+j[1]*j[1] == i:
            result.append(j)
            points.remove(j)
print(result[:1])
