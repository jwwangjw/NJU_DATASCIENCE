import collections
matrix=[]
k=0
try:
    while True:
        temp=input()
        if temp.isnumeric():
            k=int(temp)
        else:
            if temp[0] != " ":
                temp = temp[1:]
            if temp[-1] == "," or temp[-1] == "]":
                temp = temp[:-1]
            matrix.append(eval(temp))
except EOFError:
    pass
def bfs(matrix):
    dir=[(0,1),(0,-1),(1,0),(-1,0)]
    row=len(matrix)
    col=len(matrix[0])
    used=[]
    queue = collections.deque()
    queue.append((0, 0, 0))
    used.append((0,0,0))
    distance=0
    while len(queue)>0:
        distance+=1
        size=len(queue)
        for i in range(size):
            point=queue.popleft()
            x=point[0]
            y=point[1]
            z=point[2]
            if x==row-1 and y==col-1:
                return distance-1
            for j in range(4):
                newX=x+dir[j][0]
                newY=y+dir[j][1]
                newZ=z
                if newX<0 or newX>=row or newY<0 or newY>=col:
                    continue
                if matrix[newX][newY]==1:
                    if z<k:
                        newZ+=1
                    else:
                        continue
                if (newX,newY,newZ) not in used:
                    queue.append((newX,newY,newZ))
                    used.append((newX,newY,newZ))
    return -1
print(bfs(matrix))