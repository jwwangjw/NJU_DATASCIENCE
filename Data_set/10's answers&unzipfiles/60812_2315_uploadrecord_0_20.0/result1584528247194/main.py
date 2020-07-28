def height(tree, node):
    temp = tree[node]
    if temp:
        return 1+max(height(tree, temp[0]), height(tree, temp[1]))
    return 1


n = int(input())
tree = {i: [] for i in range(n)}
retree = {i: -1 for i in range(n)}
for i in range(n-1):
    f, s = [int(i) for i in input().split(' ')]
    tree[f].append(s)
    retree[s] = f
root = 0
for i, j in retree.items():
    if j == -1:
        root = i
        break
print(height(tree, root))