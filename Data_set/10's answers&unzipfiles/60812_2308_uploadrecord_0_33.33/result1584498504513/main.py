def inorder(tree, node, answer):
    lch, rch = tree[node]
    last = 0
    if lch != 0:
        last = inorder(tree, lch, answer)
    answer[last] = node
    if rch != 0:
         return inorder(tree, rch, answer)
    return node


n, root = [int(i) for i in input().split(' ')]
tree = {i: [] for i in range(1, n+1)}
for i in range(n):
    fa, lch, rch = [int(i) for i in input().split(' ')]
    tree[fa] = [lch, rch]
if root != 0:
    answer = {}
    inorder(tree, root, answer)
    print(answer[int(input())])