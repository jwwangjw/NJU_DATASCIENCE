A=eval(input())
world=[]
flag=False
for i in range(len(A)):
    row = []
    for j in range(len(A)):
        row.append(False)
    world.append(row)
def DFS(i,j):
    global flag
    world[i][j]=False
    if i!=len(A)-1 and world[i+1][j]==True:
        DFS(i+1,j)
    if j!=len(A)-1 and world[i][j+1]==True:
        DFS(i,j+1)
    if i!=0 and world[i-1][j]==True:
        DFS(i-1,j)
    if j!=0 and world[i][j-1]==True:
        DFS(i,j-1)
    if i==len(A)-1 and j==len(A)-1:
        flag=True
m=A[0][0]
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j]>m:
            m=A[i][j]
for time in range(A[0][0],m+1):
    for i in range(len(A)):
        for j in range(len(A)):
            world[i][j]=False
            if A[i][j]<=time:
                world[i][j]=True
    DFS(0,0)
    if flag:
        break
print(time)



