#include <bits/stdc++.h>
#define lch ch[x][0]
#define rch ch[x][1]
#define now c[top].nxt[k]
using namespace std;
const int sz = 2e5 + 7;
int n, m;
int cnt, L, R;
int rt, lst, cur, top;
int f[sz], col[sz];
int pos[sz];
int mx[sz], ans[sz];
int ch[sz][2];
char s[sz];
struct node {
    int len, link, nxt[2];
} c[sz];
struct Que {
    int l, r, id;
    const bool operator<(const Que &p) const { return r < p.r; }
} q[sz];
void update(int x, int sum) {
    for (; x; x -= x & -x) mx[x] = max(mx[x], sum);
}
int query(int x) {
    int ret = 0;
    for (; x <= n; x += x & -x) ret = max(ret, mx[x]);
    return ret;
}
bool nroot(int x) { return ch[f[x]][0] == x || ch[f[x]][1] == x; }
int get(int x) { return ch[f[x]][1] == x; }
void pushdn(int x) {
    if (lch)
        col[lch] = col[x];
    if (rch)
        col[rch] = col[x];
}
void pushall(int x) {
    if (nroot(x))
        pushall(f[x]);
    pushdn(x);
}
void rotate(int x) {
    int y = f[x], z = f[y], k = get(x), w = ch[x][!k];
    if (nroot(y))
        ch[z][get(y)] = x;
    ch[x][!k] = y;
    ch[y][k] = w;
    if (w)
        f[w] = y;
    f[y] = x;
    f[x] = z;
}
void splay(int x) {
    pushall(x);
    for (int y; nroot(x); rotate(x))
        if (nroot(y = f[x]))
            rotate(get(x) ^ get(y) ? x : y);
}
void access(int x, int cc) {
    for (int y = 0; x; x = f[y = x]) {
        splay(x);
        update(col[x], c[x].len);
        col[x] = cc;
        rch = y;
    }
}
void insert(int k) {
    cur = ++cnt;
    c[cur].len = c[lst].len + 1;
    pos[c[cur].len] = cur;
    top = lst;
    lst = cur;
    for (; top && !now; top = c[top].link) now = cur;
    if (!top)
        return (void)(c[cur].link = rt);
    if (c[top].len + 1 == c[now].len)
        return (void)(c[cur].link = now);
    int p = ++cnt, np = now;
    c[p] = c[np];
    c[p].len = c[top].len + 1;
    c[np].link = c[cur].link = p;
    for (; top && now == np; top = c[top].link) now = p;
}
void build() {
    for (int i = cnt; i >= 2; i--) f[i] = c[i].link;
}
int main() {
    scanf("%d%d", &n, &m);
    scanf("%s", s + 1);
    rt = lst = ++cnt;
    for (int i = 1; i <= n; i++) insert(s[i] - '0');
    build();
    //	for(int i=1;i<=n;i++) printf("%d %d %d\n",i,pos[i],c[pos[i]].link);
    //	for(int i=1;i<=cnt;i++) printf("%d %d\n",i,c[i].len);
    for (int i = 1; i <= m; i++) {
        scanf("%d%d", &L, &R);
        q[i] = (Que){ L, R, i };
    }
    sort(q + 1, q + m + 1);
    //	for(int i=1;i<=m;i++) printf("%d %d\n",q[i].l,q[i].r);
    int tot = 0;
    for (int i = 1; i <= m; i++) {
        while (tot < q[i].r) {
            tot++;
            access(pos[tot], tot);
            //			for(int i=1;i<=cnt;i++) pushall(i),printf("%d ",col[i]);
            //			printf("\n");
        }
        ans[q[i].id] = query(q[i].l);
        //		for(int i=1;i<=n;i++) printf("%d ",mx[i]);
        //		printf("\n");
    }
    for (int i = 1; i <= m; i++) printf("%d\n", ans[i]);
}