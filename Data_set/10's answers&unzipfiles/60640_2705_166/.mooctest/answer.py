from collections import defaultdict
def findRedundantConnection(edges):
    ind = {} #记录各节点的入度，用以寻找树根
    g = defaultdict(list) #存储各节点的子节点
    nodes = set() #存储所有节点
    for u, v in edges:
        ind.setdefault(u, 0)
        ind.setdefault(v, 0)
        ind[v] += 1
        g[u].append(v)
        nodes.add(u)
        nodes.add(v)

    while len(edges) > 0:
        u, v = edges.pop()
        ind[v] -= 1
        g[u].remove(v)
        r = []
        for k in ind:
            if ind[k] == 0:
                r.append(k)

        if len(r) == 1:
            rt = r[0] 
            visit = set()
            dfs(g, rt, visit)

            if len(visit) == len(nodes):
                return [u, v]
        g[u].append(v)
        ind[v] += 1

def dfs(graph, root, visited):
    if root not in visited:
        visited.add(root)
        for vertex in graph[root]:
            dfs(graph, vertex, visited)

inp = eval(input())
print(findRedundantConnection(inp))