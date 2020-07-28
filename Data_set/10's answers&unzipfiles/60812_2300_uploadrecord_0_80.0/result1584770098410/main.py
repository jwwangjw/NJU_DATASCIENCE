def inorderprint(tree: list):
    n = len(tree)
    if n == 3:
        inorderprint(tree[1])
        print(tree[0], end=' ')
        inorderprint(tree[2])
    elif n == 1:
        print(tree[0], end=' ')


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
inorderprint(tree)