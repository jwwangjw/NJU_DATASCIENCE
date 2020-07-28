def getAdajacent(arr,p):
    n = len(arr)
    for i in range(n):
        if arr[p][i] == 1:
            return i
    return -1
def bfs(arr, p, v,node):
    queue,res = [],[]
    queue.append(p)
    res.append(node[p])
    v[p] = 1
    while queue:
        p = queue.pop(0)
        u = getAdajacent(arr,p)
        while u != -1:
            arr[p][u] = 0
            arr[u][p] = 0
            if v[u] == 0:
                queue.append(u)
                res.append(node[u])
                v[u] = 1
            u = getAdajacent(arr,p)
    print(*res)


if __name__ == '__main__':
    ucaseNum = int(input())
    for i in range(ucaseNum):
        n,p = input().strip().split(" ")
        node = input().strip().split(" ")
        arr = [list(map(int,input().strip().split(" ")[1:])) for i in range(int(n))]
        for j in range(len(node)):
            if node[j] == p:
                p = j
                break
        v = [0]*int(n)
        # for j in node:
        #     v[j] = 0
        bfs(arr,p,v,node)