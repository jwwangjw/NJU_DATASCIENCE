#include<bits/stdc++.h>
using namespace std;
// 离散化操作
#define id(x) (lower_bound(b+1,b+L+1,a[x])-b)
#define rid(x) (b[x])

const int MAXN = 100005;

struct Node {
    int l, r, sum;
}node[10000005];
int head[MAXN],cnt;

vector<int> G[MAXN];

int N, M, L, lastans;
int a[MAXN], b[MAXN];
int f[MAXN][19], dep[MAXN];

inline void build(Node &u, int l, int r) {
    u.sum = 0;
    if (l == r) return;
    int mid = (l + r) >> 1;
    build(node[u.l = ++cnt], l, mid);
    build(node[u.r = ++cnt], mid + 1, r);
}

inline void insert(Node c, Node &u, int l, int r, int p) {
    u.sum = c.sum + 1;
    if (l == r) return;
    int mid = (l + r) >> 1;
    if(p <= mid)
        insert(node[c.l], node[u.l = ++cnt], l, mid, p), u.r = c.r;
    else
        insert(node[c.r], node[u.r = ++cnt], mid+1, r, p), u.l = c.l;
}

inline void dfs(int u, int fa) {
    insert(node[head[fa]], node[head[u] = ++cnt], 1, L, id(u));
    f[u][0] = fa;
    dep[u] = dep[fa] + 1;
    for (register int i = 1; i <= 18; ++i)
        f[u][i] = f[f[u][i-1]][i-1];
    for (vector<int>::iterator it = G[u].begin(); it != G[u].end(); it++) {
        int v = *it;
        if (v == fa) continue;
        dfs(v, u);
    }
}

inline int Lca(int u, int v) {
    if (dep[u] < dep[v]) swap(u, v);
    for (register int i = 18; i >= 0; --i) {
        if (dep[f[u][i]] >= dep[v]) u = f[u][i];
    }
    if (u == v) return u;
    for (register int i = 18; i >= 0; --i) {
        if (f[u][i] != f[v][i])
            u = f[u][i], v = f[v][i];
    }
    return f[u][0];
}

inline int query(Node x, Node y, Node z, Node w, int l, int r, int k) {
    if (l == r) return l;
    int sum = node[x.l].sum + node[y.l].sum - node[z.l].sum - node[w.l].sum;
    int mid = (l + r) >> 1;
    if(sum >= k) return query(node[x.l], node[y.l], node[z.l], node[w.l], l, mid, k);
    return query(node[x.r], node[y.r], node[z.r], node[w.r], mid+1, r, k - sum);
}

inline int querypath(int u, int v, int k) {
    int lca = Lca(u, v);
    return rid(query(node[head[u]], node[head[v]], node[head[lca]], node[head[f[lca][0]]], 1, L, k));
}

int main() {
    scanf("%d%d", &N, &M);
    for (register int i = 1; i <= N; ++i)
        scanf("%d", &a[i]), b[i] = a[i];
    for (register int i = 1; i < N; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        G[u].push_back(v);
        G[v].push_back(u);
    }
    sort(b + 1, b + N + 1);
    L = unique(b + 1, b + N + 1) - (b + 1);
    build(node[head[0] = ++cnt], 1, L);
    dfs(1, 0);
    for (register int i = 1; i <= M; ++i) {
        int u, v, k;
        scanf("%d%d%d", &u, &v, &k);
        int nowans = querypath(u^lastans, v, k);
        printf("%d\n", nowans);
        lastans = nowans;
    }
}