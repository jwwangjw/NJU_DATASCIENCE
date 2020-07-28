from collections import defaultdict
def maxmove(stones):
    visited = set()
    rows, cols = defaultdict(list), defaultdict(list)
    count = 0
    for i, j in stones:
        rows[i].append(j)
        cols[j].append(i)
    for i, j in stones:
        if (i, j) not in visited:
            count += 1
            dfs(stones,i, j,visited,rows, cols)
    return len(stones) - count


def dfs(stones,i, j,visited,rows, cols):
    visited.add((i, j))
    for y in rows[i]:
        if (i, y) not in visited:
            dfs(stones,i, y,visited,rows, cols)
    for x in cols[j]:
        if (x, j) not in visited:
            dfs(stones,x, j,visited,rows, cols)

inp = eval(input())
print(maxmove(inp))