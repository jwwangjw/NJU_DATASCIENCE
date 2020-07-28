def inorderprint(tree: list, p: list):
    n = len(tree)
    if n == 3:
        inorderprint(tree[1], p)
        p.append(tree[0])
        inorderprint(tree[2], p)
    elif n == 1:
        p.append(tree[0])


s = input()
ctree = tree = []
st = []
for i in s:
    if i != '#':
        ctree.append(i)
        ctree.append([])
        st.append(ctree)
        ctree = ctree[1]
    else:
        ctree = st.pop()
        while len(ctree) == 3:
            if len(st) == 0:
                break
            ctree = st.pop()
        else:
            ctree.append([])
            st.append(ctree)
            ctree = ctree[2]
            continue
        break
p = []
inorderprint(tree, p)
if p == []:
    tree.append([])
    inorderprint(tree, p)
for i in p:
    print(i, end=' ')