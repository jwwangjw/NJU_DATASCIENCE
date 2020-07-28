#include <bits/stdc++.h>
#define Re register
#define fo(i, a, b) for (Re int i = (a); i <= (b); ++i)
#define fd(i, a, b) for (Re int i = (a); i >= (b); --i)
#define edge(i, u) for (Re int i = head[u], v = e[i].v; i; i = e[i].nxt, v = e[i].v)
#define pb push_back
#define F first
#define S second
#define ll long long
#define inf 1000000007
#define mp std::make_pair
#define ls (u << 1)
#define rs (u << 1 | 1)
#define mod 1000000007
#define eps 1e-4
#define lowbit(x) (x & -x)
#define N 115
#define ull unsigned long long
int n;
std::map<ull, int> ch[N * N * 2];
int pre[N * N * 2], step[N * N * 2], x, cnt = 1, last = 1, sz[N * N * 2];
inline void ins(int x) {
    int p = last, np = ++cnt;
    last = cnt;
    step[np] = step[p] + 1;
    sz[np] = 1;
    while (p && !ch[p][x]) ch[p][x] = np, p = pre[p];
    if (!p)
        pre[np] = 1;
    else {
        int q = ch[p][x];
        if (step[q] == step[p] + 1)
            pre[np] = q;
        else {
            int nq = ++cnt;
            step[nq] = step[p] + 1;
            ch[nq] = ch[q];
            pre[nq] = pre[q];
            pre[q] = pre[np] = nq;
            while (ch[p][x] == q) ch[p][x] = nq, p = pre[p];
        }
    }
}
int m, g[N * N * 2], ans, c[N][N];
ull s[N], f[N][N], po[N];
char chh;
inline void init() {
    fo(i, 1, cnt) ch[i].clear(), step[i] = pre[i] = sz[i] = g[i] = 0;
    cnt = last = 1;
}
inline void dfs(int u) {
    g[u] = 1;
    for (std::map<ull, int>::iterator it = ch[u].begin(); it != ch[u].end(); ++it) {
        dfs(it->S);
        g[u] += g[it->S];
    }
}
int main() {
    scanf("%d %d", &n, &m);
    fo(i, 1, n) fo(j, 1, m) {
        chh = getchar();
        while (!isalpha(chh)) chh = getchar();
        c[i][j] = chh;
    }
    fo(i, 1, n) fo(j, 1, m) f[i][j] = (f[i - 1][j] * 131 + c[i][j]);
    po[0] = 1;
    fo(i, 1, n) po[i] = po[i - 1] * 131;
    fo(len, 1, n) {
        init();
        fo(l, 1, n) {
            last = 1;
            int i = l, j = l + len - 1;
            if (j > n)
                break;
            fo(k, 1, m) s[k] = (f[j][k] - f[i - 1][k] * po[j - i + 1]);
            fo(k, 1, m) ins(s[k]);
        }
        dfs(1);
        ans += g[1] - 1;
    }
    printf("%d", ans);
}