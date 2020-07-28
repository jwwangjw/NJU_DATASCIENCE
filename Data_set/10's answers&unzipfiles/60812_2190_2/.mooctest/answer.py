#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define re register
#define LL long long
#define MOD 998244353ll
#define MAXN 100005
using namespace std;
struct Edge {
    int to, nex;
    Edge(int _ = 0, int __ = 0) { to = _, nex = __; }
} e[MAXN << 1];
struct sta {
    int fa, len, ch[26];
    void cls() {
        fa = len = 0;
        memset(ch, 0, sizeof(ch));
    }
    sta() {
        memset(ch, 0, sizeof(ch));
        len = 0;
    }
} a[MAXN << 1];
char s[MAXN];
int n, k, cnt, las, tot, hd[MAXN << 1], v[MAXN << 1], t[MAXN];
int rd() {
    int x = 0, tp = 1;
    char c;
    c = getchar();
    while (c < '0' || c > '9') {
        if (c == '-')
            tp = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x * tp;
}
void adde(int x, int y) {
    e[++cnt] = Edge(y, hd[x]);
    hd[x] = cnt;
}
void add(int c) {
    int p = las;
    int np = las = ++tot;
    v[tot] = 1;
    a[np].len = a[p].len + 1;
    for (; (p && (!a[p].ch[c])); p = a[p].fa) a[p].ch[c] = np;
    if (!p)
        a[np].fa = 1;
    else {
        int q = a[p].ch[c];
        if (a[q].len == a[p].len + 1)
            a[np].fa = q;
        else {
            int nq = ++tot;
            a[nq] = a[q];
            a[nq].len = a[p].len + 1;
            a[q].fa = a[np].fa = nq;
            for (; (p && a[p].ch[c] == q); p = a[p].fa) a[p].ch[c] = nq;
        }
    }
}
int lowbit(int x) { return x & -x; }
void modify(int x, int v) {
    for (; x <= n; x += lowbit(x)) t[x] += v;
}
int ask(int x) {
    int res = 0;
    for (; x; x -= lowbit(x)) res += t[x];
    return res;
}
void dfs(int now) {
    for (int i = hd[now]; i; i = e[i].nex) {
        dfs(e[i].to);
        v[now] += v[e[i].to];
    }
    if (v[now] == k)
        modify(a[a[now].fa].len + 1, 1), modify(a[now].len + 1, -1);
}
int main() {
    // freopen("testdata.in","r",stdin);
    // freopen("shit.out","w",stdout);
    int x, y, z, T = rd();
    while (T--) {
        cnt = 0;
        tot = las = 1;
        memset(hd, 0, sizeof(hd));
        memset(v, 0, sizeof(v));
        memset(t, 0, sizeof(t));
        scanf("%s", s + 1);
        n = strlen(s + 1), k = rd();
        for (int i = 1; i <= 2 * n; i++) a[i].cls();
        for (int i = 1; i <= n; i++) add(s[i] - 'a');
        for (int i = 2; i <= tot; i++) {
            adde(a[i].fa, i);
        }
        dfs(1);
        int now, ans = -1, bes = 1;
        for (int i = 1; i <= n; i++) {
            now = ask(i);
            if (now >= bes)
                ans = i, bes = now;
        }
        printf("%d\n", ans);
    }
    // printf("%.2lf\n",(double)clock()/CLOCKS_PER_SEC);
    return 0;
}