def height(tree, node):
    temp = tree[node]
    lh = rh = 0
    n = len(temp)
    if n == 2:
        rh = height(tree, temp[1])
    if n > 0:
        lh = height(tree, temp[0])
    return 1+max(lh, rh)


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