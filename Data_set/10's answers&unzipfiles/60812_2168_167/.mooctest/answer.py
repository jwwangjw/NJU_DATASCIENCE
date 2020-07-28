#include <bits/stdc++.h>
#define mset(a, b) memset(a, b, sizeof(a))
#define rg register
using namespace std;
typedef long long LL;
const int N = 505;
const int M = N * N;
const LL INF = 1e13;

template <typename T>
inline void read(T &AKNOI) {
    T x = 0, flag = 1;
    char ch = getchar();
    while (!isdigit(ch)) {
        if (ch == '-')
            flag = -1;
        ch = getchar();
    }
    while (isdigit(ch)) {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    AKNOI = flag * x;
}

int n, m;
int pre[N], vis[N], bel[N], ID, EID;
LL in[N];

struct Edge {
    int u, v;
    LL w;
    Edge() {}
    Edge(int _u, int _v, LL _w) : u(_u), v(_v), w(_w) {}
} e[M];

void init() {
    read(n);
    read(m);
    for (int i = 1; i <= m; ++i) {
        read(e[i].u);
        read(e[i].v);
        read(e[i].w);
    }
    for (int i = 1; i <= n; ++i) {
        e[++m] = Edge(0, i, INF);
    }
}

void solve() {
    LL ans = 0;
    while (871) {
        for (int i = 1; i <= n; ++i) {
            in[i] = INF << 1;
            vis[i] = bel[i] = 0;
        }
        ID = EID = 0;
        for (int i = 1; i <= m; ++i) {
            if (e[i].w < in[e[i].v]) {
                in[e[i].v] = e[i].w;
                pre[e[i].v] = e[i].u;
            }
        }
        for (int i = 1; i <= n; ++i) {
            ans += in[i];
            int u;
            for (u = i; u && vis[u] != i && !bel[u]; u = pre[u]) {
                vis[u] = i;
            }
            if (u && !bel[u]) {
                bel[u] = ++ID;
                for (int v = pre[u]; v != u; v = pre[v]) {
                    bel[v] = ID;
                }
            }
        }
        if (!ID)
            break;
        for (int i = 1; i <= n; ++i) {
            if (!bel[i])
                bel[i] = ++ID;
        }
        for (int i = 1; i <= m; ++i) {
            if (bel[e[i].u] != bel[e[i].v]) {
                e[++EID] = Edge(bel[e[i].u], bel[e[i].v], e[i].w - in[e[i].v]);
            }
        }
        n = ID;
        m = EID;
    }
    printf("%lld\n", (ans >= (INF << 1)) ? -1 : ans - INF);
}

int main() {
    init();
    solve();
    return 0;
}