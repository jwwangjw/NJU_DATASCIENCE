n, root = [int(i) for i in input().split(' ')]
tree = {}
for i in range(n):
    fa, lch, rch = [int(i) for i in input().split(' ')]
    if rch != 0:
        tree[rch] = [fa, True]
    if lch != 0:
        tree[lch] = [fa, True]
o1, o2 = [int(i) for i in input().split(' ')]
while o1 != root:
    temp = tree[o1]
    temp[1] = False
    o1 = temp[0]
subroot = root
while o2 != root:
    temp = tree[o2]
    if temp[1]:
        temp[1] = False
        o2 = temp[0]
    else:
        subroot = o2
        break
print(subroot)