n, m = map(int, input().split())
t = 1 << n
a = list(map(int, input().split()))
tree = [0] * (t*4)


def update(x, l, r, p, i, v):
    if i != -1 and (i < l or i > r):
        return
    if l == r:
        if i == -1:
            tree[x] = a[l-1]
        else:
            tree[x] = v
        return

    mid = (l + r) // 2
    lc = x * 2
    rc = lc + 1
    update(lc, l, mid, p-1, i, v)
    update(rc, mid+1, r, p-1, i, v)

    if p % 2:
        tree[x] = tree[lc] | tree[rc]
    else:
        tree[x] = tree[lc] ^ tree[rc]


update(1, 1, t, n, -1, 0)

while m:
    m -= 1
    k, v = map(int, input().split())
    update(1, 1, t, n, k, v)
    print(tree[1])
