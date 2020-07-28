Coordinate=eval(input())
area=0
for i in range(len(Coordinate)):
    for j in range(len(Coordinate[i])):
        if Coordinate[i][j]!=0:
            area+=1
for i in range(len(Coordinate)):
    area+=max(Coordinate[i])
for i in range(len(Coordinate)):
    A=[]
    for j in range(len(Coordinate[0])):
        A.append(Coordinate[j][i])
    area+=max(A)
print(area)