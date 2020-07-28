#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
using namespace std;
inline int read() {
    int x = 0, fl = 1;
    char st = getchar();
    while (st < '0' || st > '9') {
        if (st == '-')
            fl = -1;
        st = getchar();
    }
    while (st >= '0' && st <= '9') x = x * 10 + st - '0', st = getchar();
    return x * fl;
}
const int N = 100005;
int n, m, M = 127, LOG[N];
char c[N];
int sa[N], rk[N], hei[N];
int fk[N], psk[N];
int tub[N];
int f[N][19];
inline int lcp(int l, int r) {
    l++;
    return min(f[l][LOG[r - l + 1]], f[r - (1 << LOG[r - l + 1]) + 1][LOG[r - l + 1]]);
}
inline void rsort() {
    for (int i = 1; i <= M; i++) tub[i] = 0;
    for (int i = 1; i <= n; i++) ++tub[fk[i]];
    for (int i = 1; i <= M; i++) tub[i] += tub[i - 1];
    for (int i = n; i >= 1; i--) sa[tub[fk[psk[i]]]--] = psk[i];
}
inline void SA() {
    for (int i = 1; i <= n; i++) fk[i] = c[i], psk[i] = i;
    rsort();
    for (int k = 1; k <= n; k <<= 1) {
        int cnt = 0;
        for (int i = n - k + 1; i <= n; i++) psk[++cnt] = i;
        for (int i = 1; i <= n; i++)
            if (sa[i] > k)
                psk[++cnt] = sa[i] - k;
        rsort();
        swap(fk, psk);
        fk[sa[1]] = 1;
        cnt = 1;
        for (int i = 2; i <= n; i++)
            fk[sa[i]] = (psk[sa[i]] == psk[sa[i - 1]] && psk[sa[i] + k] == psk[sa[i - 1] + k]) ? cnt : ++cnt;
        if (cnt == n)
            break;
        M = cnt;
    }
}
inline void get_hei() {
    int k = 0;
    for (int i = 1; i <= n; i++) rk[sa[i]] = i;
    for (int i = 1; i <= n; i++) {
        if (k)
            k--;
        int j = sa[rk[i] - 1];
        while (j + k <= n && i + k <= n && c[j + k] == c[i + k]) k++;
        hei[rk[i]] = k;
    }
}
int rt[N], tot;
struct ST {
    int ls, rs;
    int v;
} a[N * 25];
inline int insert(int now, int l, int r, int x) {
    int p = ++tot;
    a[p] = a[now];
    a[p].v++;
    if (l == r)
        return p;
    int mid = l + r >> 1;
    if (x <= mid)
        a[p].ls = insert(a[now].ls, l, mid, x);
    else
        a[p].rs = insert(a[now].rs, mid + 1, r, x);
    return p;
}
inline int ask(int p, int q, int l, int r, int L, int R) {
    if (L <= l && R >= r)
        return a[q].v - a[p].v;
    int mid = l + r >> 1;
    int res = 0;
    if (L <= mid)
        res += ask(a[p].ls, a[q].ls, l, mid, L, R);
    if (R > mid)
        res += ask(a[p].rs, a[q].rs, mid + 1, r, L, R);
    return res;
}
inline int check(int MID, int a, int b, int c) {
    int l = 1, r = rk[c];
    while (l < r) {
        int mid = l + r >> 1;
        if (lcp(mid, rk[c]) >= MID)
            r = mid;
        else
            l = mid + 1;
    }
    int hi = l;
    l = rk[c], r = n;
    while (l < r) {
        int mid = l + r + 1 >> 1;
        if (lcp(rk[c], mid) >= MID)
            l = mid;
        else
            r = mid - 1;
    }
    int low = l;
    return ask(rt[hi - 1], rt[low], 1, n, a, b - MID + 1);
}
inline int sol(int a, int b, int c, int d) {
    int l = 0, r = min(b - a + 1, d - c + 1);
    while (l < r) {
        int mid = l + r + 1 >> 1;
        if (check(mid, a, b, c))
            l = mid;
        else
            r = mid - 1;
    }
    return l;
}
int main() {
    //	freopen("1.in","r",stdin);
    //	freopen("1.out","w",stdout);
    n = read();
    m = read();
    scanf("%s", c + 1);
    SA();
    get_hei();
    LOG[1] = 0;
    for (int i = 2; i <= n; i++) LOG[i] = LOG[i >> 1] + 1;
    //	hei[1]=0x3f3f3f3f;
    memset(f, 0x3f, sizeof f);
    for (int i = 1; i <= n; i++) f[i][0] = hei[i];
    for (int j = 1; j <= LOG[n] + 1; j++)
        for (int i = 1; i + (1 << j) - 1 <= n; i++) f[i][j] = min(f[i][j - 1], f[i + (1 << j - 1)][j - 1]);
    rt[0] = 1;
    tot++;
    for (int i = 1; i <= n; i++) rt[i] = insert(rt[i - 1], 1, n, sa[i]);
    for (int i = 1; i <= m; i++) {
        int l1 = read(), r1 = read(), l2 = read(), r2 = read();
        printf("%d\n", sol(l1, r1, l2, r2));
    }
    return 0;
}