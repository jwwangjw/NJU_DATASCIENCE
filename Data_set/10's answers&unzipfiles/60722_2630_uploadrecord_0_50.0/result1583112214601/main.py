A=eval(input())
world=[]
for i in range(len(A)):
    row = []
    for j in range(len(A)):
        row.append(False)
    world.append(row)
def DFS(i,j,time):
    if i==len(A)-1 and j!=len(A)-1:
        if A[i][j+1]<=time:
            world[i][j+1]=True
            DFS(i,j+1,time)
        else:
            return
    elif i!=len(A)-1 and j==len(A)-1:
        if A[i+1][j]<=time:
            world[i+1][j] = True
            DFS(i+1,j,time)
        else:
            return
    elif i!=len(A)-1 and j!=len(A)-1:
        if A[i][j+1]<=time:
            world[i][j+1]=True
            DFS(i,j+1,time)
        if A[i+1][j]<=time:
            world[i+1][j]=True
            DFS(i+1,j,time)
        return
m=A[0][0]
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j]>m:
            m=A[i][j]
for time in range(A[0][0],m+1):
    DFS(0,0,time)
    if world[len(A)-1][len(A)-1]:
        break
print(time)



