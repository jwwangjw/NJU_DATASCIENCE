n, root = [int(i) for i in input().split(' ')]
tree = {}
templist = []
for i in range(n):
    fa, lch, rch = [int(i) for i in input().split(' ')]
    templist.append([fa, lch, rch])
    temp = [fa, True]
    if rch != 0:
        tree[rch] = temp
    if lch != 0:
        tree[lch] = temp
o1, o2 = [int(i) for i in input().split(' ')]
temp1, temp2 = o1, o2
temptree = tree.copy()
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
        subroot = temp[0]
        break
print(subroot)