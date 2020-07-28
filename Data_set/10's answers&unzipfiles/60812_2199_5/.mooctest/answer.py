#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define N 880000
using namespace std;
struct node {
    int len, pos, fa, nxt[30];
} a[N];
struct node1 {
    int l, r;
} tree[N * 40];
int rt[N], cnt, ans, num, lst, top[N], f[N], n;
vector<int> son[N];
char t[N];
void modfiy(int &p, int l, int r, int x) {
    if (!p)
        p = ++cnt;
    if (l == r)
        return;
    int mid = (l + r) / 2;
    if (x <= mid)
        modfiy(tree[p].l, l, mid, x);
    else
        modfiy(tree[p].r, mid + 1, r, x);
}
int merge(int x, int y) {
    if (!x or !y)
        return x | y;
    int z = ++cnt;
    tree[z].l = merge(tree[x].l, tree[y].l);
    tree[z].r = merge(tree[x].r, tree[y].r);
    return z;
}
int query(int p, int l, int r, int ql, int qr) {
    if (!p)
        return 0;
    if (ql <= l and r <= qr)
        return 1;
    int mid = (l + r) / 2;
    if (ql <= mid and query(tree[p].l, l, mid, ql, qr))
        return 1;
    if (mid < qr and query(tree[p].r, mid + 1, r, ql, qr))
        return 1;
    return 0;
}
inline void add(int c, int pos) {
    int p = lst, newnode = ++num;
    lst = newnode;
    a[newnode].len = a[p].len + 1;
    a[newnode].pos = pos;
    while (p and !a[p].nxt[c]) a[p].nxt[c] = newnode, p = a[p].fa;
    if (!p)
        a[newnode].fa = 1;
    else {
        int q = a[p].nxt[c];
        if (a[p].len + 1 == a[q].len)
            a[newnode].fa = q;
        else {
            int cop = ++num;
            a[cop] = a[q];
            a[cop].len = a[p].len + 1;
            a[q].fa = a[newnode].fa = cop;
            while (p and a[p].nxt[c] == q) a[p].nxt[c] = cop, p = a[p].fa;
        }
    }
}
void dfs(int u, int fa) {
    if (fa == 1 or fa == 0) {
        top[u] = u;
        f[u] = 1;
    } else {
        //	printf("sam\n");
        int yu = query(rt[top[fa]], 1, n, a[u].pos - a[u].len + a[top[fa]].len, a[u].pos - 1);
        if (yu)
            f[u] = f[fa] + 1, top[u] = u;
        else
            f[u] = f[fa], top[u] = top[fa];
        ans = max(ans, f[u]);
    }
    for (int i = 0; i < son[u].size(); ++i) dfs(son[u][i], u);
}
void dfs1(int u, int fa) {
    for (int i = 0; i < son[u].size(); ++i) dfs1(son[u][i], u), rt[u] = merge(rt[u], rt[son[u][i]]);
}
int main() {
    //	freopen("a.in","r",stdin);
    scanf("%s", t + 1);
    n = strlen(t + 1);
    num = 1;
    lst = 1;
    for (int i = 1; i <= n; ++i) add(t[i] - 'a', i), modfiy(rt[lst], 1, n, i);
    for (int i = num; i >= 2; --i) {
        son[a[i].fa].push_back(i);
    }
    ans = 1;
    dfs1(1, 0);
    dfs(1, 0);
    printf("%d\n", ans);
    return 0;
}