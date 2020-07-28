matrix=[]
try:
    while True:
        matrix.append(list(map(int,input().split(" "))))
except EOFError:
    pass

dist=[[float("inf")]*len(matrix[0]) for line in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            dist[i][j]=0
        if i>0:
            dist[i][j]=min(dist[i][j],dist[i-1][j]+1)
        if j>0:
            dist[i][j]=min(dist[i][j],dist[i][j-1]+1)
for i in range(len(matrix)-1,-1,-1):
    for j in range(len(matrix[0])-1,-1,-1):
        if i<len(matrix)-1:
            dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
        if j<len(matrix[0])-1:
            dist[i][j]=min(dist[i][j],dist[i][j+1]+1)
for line in dist:
    print(*line)
