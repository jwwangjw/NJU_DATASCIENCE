#include <bits/stdc++.h>
using namespace std;

inline int get() {
    int x = 0, f = 1;
    char c = getchar();
    while (!isdigit(c)) {
        if (c == '-')
            f = -1;
        c = getchar();
    }
    while (isdigit(c)) {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x * f;
}

const int N = 1e5 + 5;
int n, q;

namespace Splay_Tree {
int val[N], rev[N], fa[N], ch[N][2], size[N], rt;

inline bool chk(int x) { return ch[fa[x]][1] == x; }

inline void pushup(int u) { size[u] = size[ch[u][1]] + size[ch[u][0]] + 1; }

inline void build(int l, int r, int f) {
    int mid = (l + r) >> 1;
    if (l == r)
        val[mid] = (l == 1 || l == n + 2) ? 0 : (l - 1), rev[mid] = 0, size[mid] = 1;
    if (l < mid)
        build(l, mid - 1, mid);
    if (r > mid)
        build(mid + 1, r, mid);
    val[mid] = (mid == 1 || mid == n + 2) ? 0 : (mid - 1), fa[mid] = f;
    ch[f][mid > f] = mid;
    pushup(mid);
}

inline void pushdown(int x) {
    if (rev[x]) {
        swap(ch[x][0], ch[x][1]);
        rev[ch[x][0]] ^= 1, rev[ch[x][1]] ^= 1;
        rev[x] = 0;
    }
}

inline void rotate(int x) {
    pushdown(x);
    int y = fa[x], z = fa[y], k = chk(x), s = ch[x][k ^ 1];
    ch[y][k] = s, fa[s] = y;
    ch[z][chk(y)] = x, fa[x] = z;
    ch[x][k ^ 1] = y, fa[y] = x;
    pushup(y), pushup(x);
}

inline void splay(int x, int k) {
    while (fa[x] != k) {
        if (fa[fa[x]] != k) {
            if (chk(x) == chk(fa[x]))
                rotate(fa[x]);
            else
                rotate(x);
        }
        rotate(x);
    }
    if (!k)
        rt = x;
}

inline int find(int rk) {
    int x = rt;
    while (x) {
        pushdown(x);
        if (ch[x][0] && size[ch[x][0]] >= rk)
            x = ch[x][0];
        else if (ch[x][1] && size[ch[x][0]] + 1 < rk)
            rk -= size[ch[x][0]] + 1, x = ch[x][1];
        else
            return x;
    }
}

inline int split(int l, int r) {
    int x = find(l - 1), y = find(r + 1);
    splay(x, 0), splay(y, x);
    return ch[y][0];
}

inline void reverse(int l, int r) {
    int x = split(l, r);
    rev[x] ^= 1;
}

inline void output(int u) {
    pushdown(u);
    if (ch[u][0])
        output(ch[u][0]);
    if (u == 1 || u == n + 2)
        ;
    else
        printf("%d ", val[u]);
    if (ch[u][1])
        output(ch[u][1]);
}
}  // namespace Splay_Tree

int main() {
    n = get(), q = get();
    Splay_Tree::build(1, n + 2, 0);
    Splay_Tree::rt = (n + 3) >> 1;
    while (q--) {
        int l = get() + 1, r = get() + 1;
        Splay_Tree::reverse(l, r);
    }
    Splay_Tree::output(Splay_Tree::rt);
    return 0;
}