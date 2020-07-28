#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#define MAXN 200101
struct Edge {
    int v, nx;
} e[MAXN << 1];
int st[MAXN], w[MAXN], top, head[MAXN], tim, ecnt, n, m, x[MAXN], y, p[MAXN], dfn[MAXN], low[MAXN], num[MAXN],
    cnt, ent[MAXN];
bool vis[MAXN];
std::vector<int> v[MAXN];
void add(int f, int t) {
    e[++ecnt] = (Edge){ t, head[f] };
    head[f] = ecnt;
}
void tarjan(int u) {
    dfn[u] = low[u] = ++tim;
    st[++top] = u;
    vis[u] = 1;
    for (int i = head[u]; i; i = e[i].nx) {
        int v = e[i].v;
        if (!dfn[v]) {
            tarjan(v);
            low[u] = std::min(low[u], low[v]);
        } else if (vis[v])
            low[u] = std::min(low[u], dfn[v]);
    }
    if (low[u] == dfn[u]) {
        cnt++;
        int v;
        do {
            v = st[top--];
            vis[v] = 0;
            num[v] = cnt;
            w[cnt] += p[v];
        } while (u != v);
    }
}
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &p[i]);
    }
    for (int i = 1; i <= n; i++) {
        scanf("%d", &x[i]);
        add(x[i], i);
    }
    for (int i = 1; i <= n; i++) {
        if (!dfn[i])
            tarjan(i);
    }
    for (int i = 1; i <= n; i++) {
        if (num[i] == num[x[i]])
            continue;
        v[num[x[i]]].push_back(num[i]);
        ent[num[i]]++;
        // printf("%d -> %d\n", num[x[i]], num[i]);
    }
    std::queue<int> q;
    for (int i = 1; i <= cnt; i++) {
        if (!ent[i])
            q.push(i);
    }
    // for (int i = 1; i <= cnt; i++) {
    //     printf("%d ", ent[i]);
    // }
    // puts("");
    // for (int i = 1; i <= n; i++) {
    // 	printf("%d ", num[i]);
    // }
    // puts("");
    // for (int i = 1; i <= cnt; i++) {
    // 	printf("%d ", w[i]);
    // }
    // puts("");
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = 0; i < (int)v[u].size(); i++) {
            int to = v[u][i];
            ent[to]--;
            // printf("%d ", to);
            w[to] = w[to] + w[u];
            if (!ent[to])
                q.push(to);
        }
        // puts("");
    }
    for (int i = 1; i <= n; i++) {
        printf("%d\n", w[num[i]]);
    }
    return 0;
}