def count(x, y):
    if visited[x][y] == 0:
        if single[x][y] == '1':
            visited[x][y] = 1
            if y != len(visited[x])-1:
                count(x, y+1)
            if x != len(visited)-1:
                count(x+1, y)
            if y != 0:
                count(x, y-1)
            if x != 0:
                count(x-1, y)
        else:
            return
    else:
        return


a = input()
t = a.split(" ")
top = []
for i in range(3):
    top.append(int(t[i]))
graph = []
for i in range(top[0]):
    graph.append([])
    a = input()
    for j in range(top[1]):
        graph[i] = list(a)
for i in range(top[2]):
    ans = 0
    a = input()
    wi = []
    t = a.split(" ")
    for j in range(4):
        wi.append(int(t[j]))
    single = []
    for k in range(0, wi[2]-wi[0]+1):
        single.append([])    # wi[0]-1, wi[2]
        for l in range(0, wi[3]-wi[1]+1):
            single[k].append(graph[wi[0]-1+k][wi[1]-1+l])
    visited = []
    for k in range(0, wi[2] - wi[0] + 1):
        visited.append([])
        for l in range(0, wi[3] - wi[1] + 1):
            visited[k].append(0)
    for k in range(0, wi[2] - wi[0] + 1):
        for l in range(0, wi[3] - wi[1] + 1):
            if visited[k][l] == 0:
                count(k, l)
                ans = ans + 1
    numOfZero = 0
    for k in range(0, wi[2] - wi[0] + 1):
        for l in range(0, wi[3] - wi[1] + 1):
            if single[k][l] == '0':
                numOfZero = numOfZero + 1
    print(ans-numOfZero)






