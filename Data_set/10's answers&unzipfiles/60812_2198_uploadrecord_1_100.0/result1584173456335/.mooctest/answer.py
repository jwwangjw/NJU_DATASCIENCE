#include <bits/stdc++.h>
using namespace std;
const int maxn = 5e5 + 5;
const int mx = 20;
inline int read() {
    char c = getchar();
    int t = 0, f = 1;
    while (!isdigit(c)) {
        if (c == '-')
            f = -1;
        c = getchar();
    }
    while (isdigit(c)) {
        t = (t << 3) + (t << 1) + (c ^ 48);
        c = getchar();
    }
    return t * f;
}
int n, w[maxn], x[maxn], y[maxn], sa[maxn], rk[maxn], h[maxn], t[maxn], m = 300, c[maxn * mx][2];
char s[maxn];
void get() {
    for (int i = 1; i <= n; i++) t[x[i] = s[i]]++;
    for (int i = 1; i <= m; i++) t[i] += t[i - 1];
    for (int i = n; i >= 1; i--) sa[t[x[i]]--] = i;
    for (int k = 1; k <= n; k <<= 1) {
        int num = 0;
        for (int i = n - k + 1; i <= n; i++) y[++num] = i;
        for (int i = 1; i <= n; i++)
            if (sa[i] > k)
                y[++num] = sa[i] - k;
        memset(t, 0, sizeof(t));
        for (int i = 1; i <= n; i++) t[x[i]]++;
        for (int i = 1; i <= m; i++) t[i] += t[i - 1];
        for (int i = n; i >= 1; i--) {
            sa[t[x[y[i]]]--] = y[i];
            y[i] = 0;
        }
        swap(x, y);
        x[sa[1]] = 1;
        num = 1;
        for (int i = 2; i <= n; i++)
            x[sa[i]] = (y[sa[i]] == y[sa[i - 1]]) && (y[sa[i] + k] == y[sa[i - 1] + k]) ? num : ++num;
        if (num == n)
            break;
        m = num;
    }
    for (int i = 1; i <= n; i++) rk[sa[i]] = i;
    int k = 0;
    for (int i = 1; i <= n; i++) {
        // if(rk[i]==1)continue;
        if (k)
            k--;
        int j = sa[rk[i] - 1];
        while (s[i + k] == s[j + k] && i + k <= n && j + k <= n) k++;
        h[rk[i]] = k;
    }
}
int sz[maxn], f[maxn], rt[maxn], cnt;
inline int find(int x) { return f[x] == x ? f[x] : f[x] = find(f[x]); }
int build(int x) {
    int rt = ++cnt, now = rt;
    for (int i = mx; i >= 0; i--) {
        c[now][(x >> i) & 1] = ++cnt, now = cnt;
    }
    return rt;
}
typedef pair<int, int> pii;
pii so[maxn];
int query(int x, int y, int z = 0) {
    int best = z;
    if (c[x][0]) {
        if (c[y][1])
            best = query(c[x][0], c[y][1], 2 * z + 1);
        else
            best = query(c[x][0], c[y][0], 2 * z);
    }
    if (c[x][1]) {
        if (c[y][0])
            best = max(best, query(c[x][1], c[y][0], 2 * z + 1));
        else
            best = max(best, query(c[x][1], c[y][1], 2 * z));
    }
    return best;
}
int ans;
void merge(int x, int y) {
    if (c[x][0]) {
        if (c[y][0])
            merge(c[x][0], c[y][0]);
        else
            c[y][0] = c[x][0];
    }
    if (c[x][1]) {
        if (c[y][1])
            merge(c[x][1], c[y][1]);
        else
            c[y][1] = c[x][1];
    }
}
int main() {
    n = read();
    scanf("%s", s + 1);
    for (int i = 1; i <= n; i++) w[i] = read();
    get();
    for (int i = 1; i <= n; i++) {
        sz[i] = 1, f[i] = i;
        rt[i] = build(w[sa[i]]);
    }
    for (int i = 2; i <= n; i++) {
        so[i - 1] = pii(n - h[i], i);
    }
    sort(so + 1, so + n);
    int ret = 0;
    for (int i = 1; i < n; i++) {
        int x = so[i].second, y = x - 1, z = n - so[i].first;
        x = find(x), y = find(y);
        if (sz[x] < sz[y])
            swap(x, y);
        int tmp = query(rt[y], rt[x]) + z;
        if (tmp > ans)
            ans = tmp;
        sz[x] += sz[y];
        merge(rt[y], rt[x]);
        f[y] = x;
    }
    printf("%d\n", ans);
    return 0;
}