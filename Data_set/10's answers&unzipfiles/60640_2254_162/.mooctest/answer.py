#include <bits/stdc++.h>
using namespace std;
const int maxV = 5010;
const int maxE = 20100;
int n, m, x, y, tot = 0, color = 0, Index = 0, Last[maxV], dfn[maxV], low[maxV], lab[maxV], cnt[maxV],
                Stack[maxV];
bool vis[maxV], f[maxV][maxV];
struct recEdge {
    int pre, to;
} E[maxE];
void addEdge(int U, int V) {
    E[++tot].pre = Last[U];
    Last[U] = tot;
    E[tot].to = V;
}
void tarjan(int u, int fa) {
    low[u] = dfn[u] = ++tot;
    vis[Stack[++Index] = u] = 1;
    for (int ed = Last[u]; ed; ed = E[ed].pre) {
        int v = E[ed].to;
        if (v == fa) {
            continue;
        }
        if (!dfn[v]) {
            tarjan(v, u);
            low[u] = min(low[u], low[v]);
        } else {
            if (vis[v]) {
                low[u] = min(low[u], dfn[v]);
            }
        }
    }
    if (low[u] == dfn[u]) {
        color++;
        do {
            lab[Stack[Index]] = color;
            vis[Stack[Index--]] = 0;
        } while (u != Stack[Index + 1]);
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin >> n >> m;
    memset(Last, 0, sizeof(Last));
    memset(dfn, 0, sizeof(dfn));
    memset(low, 0, sizeof(low));
    memset(vis, 0, sizeof(vis));
    memset(lab, 0, sizeof(lab));
    memset(cnt, 0, sizeof(cnt));
    memset(f, 0, sizeof(f));
    for (int i = 1; i <= m; i++) {
        cin >> x >> y;
        if (f[x][y])
            continue;
        f[x][y] = f[y][x] = 1;
        addEdge(x, y);
        addEdge(y, x);
    }
    tot = 0;
    for (int i = 1; i <= n; i++)
        if (!dfn[i])
            tarjan(i, 0);
    for (int i = 1; i <= n; i++) {
        for (int ed = Last[i]; ed; ed = E[ed].pre) {
            if (lab[i] != lab[E[ed].to]) {
                cnt[lab[i]]++;
                cnt[lab[E[ed].to]]++;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= color; i++) {
        if (cnt[i] == 2)
            ans++;
    }
    cout << (ans + 1) / 2 << endl;
    return 0;
}