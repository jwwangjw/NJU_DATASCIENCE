def inorder(tree, node, answer, last):
    lch, rch = tree[node]
    if lch != 0:
        answer[inorder(tree, lch, answer, last)] = node
    else:
        answer[last] = node
    if rch != 0:
         return inorder(tree, rch, answer, node)
    return node


n, root = [int(i) for i in input().split(' ')]
tree = {i: [] for i in range(1, n+1)}
for i in range(n):
    fa, lch, rch = [int(i) for i in input().split(' ')]
    tree[fa] = [lch, rch]
if root != 0:
    answer = {}
    inorder(tree, root, answer, 0)
    node = int(input())
    if node in answer.keys():
        print(answer[node])
    else:
        print(0)