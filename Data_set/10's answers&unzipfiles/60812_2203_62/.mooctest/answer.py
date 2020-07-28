#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <map>
#define mp make_pair
#define pb push_back
#define pii pair<int, int>
#define link(x) for (edge *j = h[x]; j; j = j->next)
#define inc(i, l, r) for (int i = l; i <= r; i++)
#define dec(i, r, l) for (int i = r; i >= l; i--)
const int MAXN = 6e5 + 10;
const double eps = 1e-8;
const int mod = 1e9 + 7;
#define ll long long
using namespace std;
struct edge {
    int t, v;
    edge *next;
} e[MAXN << 1], *h[MAXN], *o = e;
void add(int x, int y, int vul) {
    o->t = y;
    o->v = vul;
    o->next = h[x];
    h[x] = o++;
}
ll read() {
    ll x = 0, f = 1;
    char ch = getchar();
    while (!isdigit(ch)) {
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
    return x * f;
}
ll base;
ll ksm(ll a, ll b) {
    ll ans = 1;
    while (b) {
        if (b & 1)
            ans = ans * a % mod;
        a = a * a % mod;
        b = b >> 1;
    }
    return ans;
}

int t1[MAXN], t2[MAXN];
int sa1[MAXN], txt[MAXN], td[MAXN], rank1[MAXN], Rank1[MAXN], sa2[MAXN], Rank2[MAXN];
bool cmp(int f[], int p1, int p2, int w) { return f[p1] == f[p2] && f[p1 + w] == f[p2 + w]; }
void Sa(char str[], int sa[], int rank2[]) {
    int len = strlen(str);
    int m = 128;
    int *td = t1;
    int *rank1 = t2;
    inc(i, 0, m - 1) txt[i] = 0;
    inc(i, 0, len - 1) rank1[i] = str[i], txt[str[i]]++;
    inc(i, 1, m - 1) txt[i] += txt[i - 1];
    dec(i, len - 1, 0) sa[--txt[str[i]]] = i;
    for (int k = 1; k <= len; k <<= 1) {
        int p = 0;
        inc(i, len - k, len - 1) td[p++] = i;
        inc(i, 0, len - 1) if (sa[i] >= k) td[p++] = sa[i] - k;
        inc(i, 0, m - 1) txt[i] = 0;
        inc(i, 0, len - 1) txt[rank1[i]]++;
        inc(i, 1, m - 1) txt[i] += txt[i - 1];
        dec(i, len - 1, 0) sa[--txt[rank1[td[i]]]] = td[i];
        swap(td, rank1);
        rank1[sa[0]] = 0;
        p = 1;
        inc(i, 1, len - 1) rank1[sa[i]] = cmp(td, sa[i], sa[i - 1], k) ? p - 1 : p++;
        if (p >= len)
            break;
        m = p;
    }
    inc(i, 0, len - 1) rank2[sa[i]] = i;
}
int h1[MAXN], h2[MAXN], H[MAXN], sz;
char s1[MAXN], s2[MAXN];
int dp2[MAXN][21], ma[MAXN], dp1[MAXN][21];
void hh(char str[], int h[], int rank2[], int sa[]) {
    int len = strlen(str);
    inc(i, 0, len - 1) h[i] = 0;
    memset(H, 0, sizeof(H));
    inc(i, 0, len - 1) {
        if (!rank2[i])
            continue;
        int t = sa[rank2[i] - 1];
        int w = i;
        int k = 0;
        if (!i || H[i - 1] <= 1)
            k = 0;
        else
            k = H[i - 1] - 1, t += k, w += k;
        while (t < len && w < len) {
            if (str[t] == str[w])
                k++;
            else
                break;
            t++;
            w++;
        }
        H[i] = k;
        h[rank2[i]] = k;
    }
}
void St1(int n) {
    for (int i = 1; i <= n; i++) dp1[i][0] = h1[i];
    for (int j = 1; j <= 20; j++) {
        for (int i = 1; i + (1 << j) <= n + 1; i++) {
            dp1[i][j] = min(dp1[i][j - 1], dp1[i + (1 << (j - 1))][j - 1]);
        }
    }
}
void St2(int n) {
    for (int i = 1; i <= n; i++) dp2[i][0] = h2[i];
    for (int j = 1; j <= 20; j++) {
        for (int i = 1; i + (1 << j) <= n + 1; i++) {
            dp2[i][j] = min(dp2[i][j - 1], dp2[i + (1 << (j - 1))][j - 1]);
        }
    }
}

int lcp1(int l, int r) {
    if (l > r)
        swap(l, r);
    l++;
    int k = ma[r - l + 1];
    return min(dp1[l][k], dp1[r - (1 << k) + 1][k]);
}
int lcp2(int l, int r) {
    if (l > r)
        swap(l, r);
    l++;
    int k = ma[r - l + 1];
    return min(dp2[l][k], dp2[r - (1 << k) + 1][k]);
}
char str[MAXN];
int n;
ll sum1[MAXN], sum2[MAXN];
int sum3[MAXN];
int get_id(int x) { return x & (-x); }
void update1(int x, ll y) {
    for (int i = x; i <= n; i += get_id(i)) sum1[i] += y, sum1[i] %= mod;
}
void update2(int x, ll y) {
    for (int i = x; i <= n; i += get_id(i)) sum2[i] += y, sum2[i] %= mod;
}
void update3(int x, int y) {
    for (int i = x; i <= n; i += get_id(i)) sum3[i] += y;
}
ll query1(int x) {
    ll ans = 0;
    for (int i = x; i > 0; i -= get_id(i)) ans += sum1[i], ans %= mod;
    return ans;
}
ll query2(int x) {
    ll ans = 0;
    for (int i = x; i > 0; i -= get_id(i)) ans += sum2[i], ans %= mod;
    return ans;
}
int query3(int x) {
    int ans = 0;
    for (int i = x; i > 0; i -= get_id(i)) ans += sum3[i];
    return ans;
}
ll sum[MAXN];
ll check(int i) {
    return ((query1(i) * (i - 1) % mod + base * query3(i) % mod * (i - 1) % mod * (i - 1) % mod) % mod +
            query2(i)) %
           mod;
}
void modify(int lx, int rx, int l, bool k) {
    ll t4 = (l + base - (lx - 1));
    if (t4 < 0)
        t4 += mod;
    if (!k)
        t4 = mod - t4;
    update1(lx + 1, t4);
    update1(rx + 2, mod - t4);
    ll t = (1ll * (lx - 1) * (lx - 1) % mod * base % mod - 1ll * (l + base) * (lx - 1) % mod + mod) % mod;
    if (!k)
        t = mod - t;
    update2(lx + 1, t);
    update2(rx + 2, mod - t);
    int t1 = 1;
    if (!k)
        t1 = -1;
    update3(lx + 1, t1);
    update3(rx + 2, -t1);
}
int main() {
    ma[1] = 0;
    base = ksm(2, mod - 2);
    inc(i, 2, MAXN - 1) ma[i] = ma[i / 2] + 1;
    scanf("%s", str);
    int len = strlen(str);
    n = len;
    str[len] = '$';
    str[len + 1] = '\0';
    Sa(str, sa1, Rank1);
    hh(str, h1, Rank1, sa1);
    St1(len);
    reverse(str, str + len);
    Sa(str, sa2, Rank2);
    hh(str, h2, Rank2, sa2);
    St2(len);
    inc(l, 1, len) {
        for (int i = 0; i + l < len; i += l) {
            int t1 = min(l, lcp1(Rank1[i], Rank1[i + l]));
            int t2 = min(l, lcp2(Rank2[len - 1 - i], Rank2[len - 1 - i - l]));
            if (t1 + t2 - 1 < l)
                continue;
            if (i + 2 * l - t2 + 1 >= len)
                continue;
            int t3 = lcp1(Rank1[i + l - t2 + 1], Rank1[i + 2 * l - t2 + 1]);
            if (t3 == 0)
                continue;
            int lx = i + 2 * l - t2 + 1;
            int rx = lx + t3 - 1;
            modify(lx, rx, l, 1);
            int t4 = t1 + t2 - l;
            if (lx + t4 <= rx)
                modify(lx + t4, rx, l, 0);
        }
    }
    inc(i, 1, len) {
        sum[i] = ((query1(i) * (i - 1) % mod + base * query3(i) % mod * (i - 1) % mod * (i - 1) % mod) % mod +
                  query2(i)) %
                 mod;
        sum[i] += sum[i - 1];
        sum[i] %= mod;
        printf("%lld\n", sum[i]);
    }
    return 0;
}