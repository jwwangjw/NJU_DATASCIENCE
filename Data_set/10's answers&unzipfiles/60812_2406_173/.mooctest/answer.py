/*Program from Luvwgyx*/
#include <cstdio>
#include <cstring>
#include <algorithm>
#define int long long
using namespace std;
const int inf = 1e9;
const int maxn = 1e5 + 10;
int n, tot, cnt, mx, a[maxn], lst[maxn], pre[maxn], nxt[maxn];
int read() {
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9') {
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    return x * f;
}
void print(int x) {
    if (x < 0)
        putchar('-'), x = -x;
    if (x > 9)
        print(x / 10);
    putchar(x % 10 + '0');
}
void write(int x) {
    print(x);
    puts("");
}
struct Binary_Index_Tree {
    int tree[maxn];
    void change(int x, int v) {
        for (; x <= n; x += (x & (-x))) tree[x] += v;
    }
    int query(int x) {
        int ret = 0;
        for (; x; x -= (x & (-x))) ret += tree[x];
        return ret;
    }
} t;
int root[maxn], tree[20 * maxn], ls[20 * maxn], rs[20 * maxn];
struct Chairman_Tree {
    void change(int &k, int pre, int l, int r, int x) {
        k = ++cnt;
        ls[k] = ls[pre];
        rs[k] = rs[pre];
        tree[k] = tree[pre] + 1;
        if (l == r)
            return;
        int mid = (l + r) >> 1;
        if (x <= mid)
            change(ls[k], ls[pre], l, mid, x);
        else
            change(rs[k], rs[pre], mid + 1, r, x);
    }
    int query(int k1, int k2, int l, int r, int x, int y) {
        if (x > y)
            return 0;
        if (x <= l && r <= y)
            return tree[k1] - tree[k2];
        int mid = (l + r) >> 1, ret = 0;
        if (x <= mid)
            ret += query(ls[k1], ls[k2], l, mid, x, y);
        if (mid < y)
            ret += query(rs[k1], rs[k2], mid + 1, r, x, y);
        return ret;
    }
} T;
int get(int l, int r) {
    int ret = 0;
    if (a[l] < a[r])
        ret++;
    else if (a[l] > a[r])
        ret--;
    ret += T.query(root[r - 1], root[l], 1, n, a[l] + 1, n);
    ret += T.query(root[r - 1], root[l], 1, n, 1, a[r] - 1);
    ret -= T.query(root[r - 1], root[l], 1, n, 1, a[l] - 1);
    ret -= T.query(root[r - 1], root[l], 1, n, a[r] + 1, n);
    return -ret;
}
void calc(int l, int r, int L, int R) {
    if (l > r)
        return;
    int mid = (l + r) >> 1, pos = 0, ret = -inf;
    for (int i = L; i <= R; i++) {
        if (pre[mid] == nxt[i])
            continue;
        int tmp = get(pre[mid], nxt[i]);
        if (tmp >= ret)
            ret = tmp, pos = i;
    }
    mx = max(mx, ret);
    calc(l, mid - 1, L, pos);
    calc(mid + 1, r, pos, R);
}
signed main() {
    n = read();
    int ans = 0;
    for (int i = 1; i <= n; i++) a[i] = read(), lst[++tot] = a[i];
    sort(lst + 1, lst + tot + 1);
    tot = unique(lst + 1, lst + tot + 1) - lst - 1;
    for (int i = 1; i <= n; i++) a[i] = lower_bound(lst + 1, lst + tot + 1, a[i]) - lst;
    for (int i = n; i >= 1; i--) ans += t.query(a[i] - 1), t.change(a[i], 1);
    pre[++pre[0]] = 1;
    nxt[++nxt[0]] = n;
    for (int i = 1; i <= n; i++)
        if (a[i] > a[pre[pre[0]]])
            pre[++pre[0]] = i;
    for (int i = n; i >= 1; i--)
        if (a[i] < a[nxt[nxt[0]]])
            nxt[++nxt[0]] = i;
    for (int i = 1; i <= n; i++) T.change(root[i], root[i - 1], 1, n, a[i]);
    reverse(nxt + 1, nxt + nxt[0] + 1);
    // for(int i=1;i<=pre[0];i++)printf("%lld ",pre[i]);puts("");
    // for(int i=1;i<=nxt[0];i++)printf("%lld ",nxt[i]);puts("");
    // write(ans);
    mx = -inf;
    calc(1, pre[0], 1, nxt[0]);
    ans -= mx;
    write(ans);
    return 0;
}