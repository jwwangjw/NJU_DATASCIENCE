#include <bits/stdc++.h>
#define debug(x) cout << #x << " " << (x) << endl
using namespace std;
const int N = 200005;
template <class T>
void read(T &x) {
    int sgn = 1;
    char ch;
    x = 0;
    for (ch = getchar(); (ch < '0' || ch > '9') && ch != '-'; ch = getchar())
        ;
    if (ch == '-')
        ch = getchar(), sgn = -1;
    for (; '0' <= ch && ch <= '9'; ch = getchar()) x = x * 10 + ch - '0';
    x *= sgn;
}
template <class T>
void write(T x) {
    if (x < 0)
        putchar('-'), write(-x);
    else if (x < 10)
        putchar(x + '0');
    else
        write(x / 10), putchar(x % 10 + '0');
}
int n, s, m, s_min = 0, a[N], b[N], c[N];
struct edge {
    int to, nxt, id;
    bool vis;
} graph[N];
int head[N], cnt = 0, tot = 0;
bool vis[N];
vector<int> stk[N];
void addedge(int u, int v, int id) {
    edge x = { v, head[u], id, false };
    graph[head[u] = ++cnt] = x;
}
void dfs(int u) {
    vis[u] = true;
    for (; head[u];) {
        int i = head[u];
        head[u] = graph[i].nxt;
        if (!graph[i].vis) {
            graph[i].vis = true, dfs(graph[i].to);
            stk[tot].push_back(graph[i].id);
        }
    }
}
int main() {
    read(n), read(s);
    for (int i = 1; i <= n; i++) read(a[i]), c[i] = b[i] = a[i];
    sort(b + 1, b + n + 1), sort(c + 1, c + n + 1);
    m = unique(c + 1, c + n + 1) - c - 1;
    for (int i = 1; i <= m; i++) head[i] = 0, vis[i] = false;
    for (int i = 1; i <= n; i++) {
        int u = lower_bound(c + 1, c + m + 1, a[i]) - c, v = lower_bound(c + 1, c + m + 1, b[i]) - c;
        if (u != v)
            addedge(u, v, i);
    }
    for (int i = 1; i <= m; i++) {
        if (!vis[i] && head[i])
            tot++, dfs(i);
    }
    s_min = 0;
    for (int i = 1; i <= tot; i++) s_min += stk[i].size();
    if (s >= s_min) {
        int t = min(s - s_min, tot);
        if (t <= 1) {
            write(tot), putchar('\n');
            for (int i = 1; i <= tot; i++) {
                write(stk[i].size()), putchar('\n');
                for (int j = 0; j < stk[i].size(); j++) write(stk[i][j]), putchar(' ');
                putchar('\n');
            }
        } else {
            write(tot - t + 2), putchar('\n');
            write(t), putchar('\n');
            for (int i = t; i; i--) write(stk[i][0]), putchar(' ');
            int total = 0;
            for (int i = 1; i <= t; i++) total += stk[i].size();
            putchar('\n'), write(total), putchar('\n');
            for (int i = 1; i <= t; i++) {
                for (int j = 0; j < stk[i].size(); j++) write(stk[i][(j + 1) % stk[i].size()]), putchar(' ');
            }
            for (int i = tot; i > t; i--) {
                write(stk[i].size()), putchar('\n');
                for (int j = 0; j < stk[i].size(); j++) write(stk[i][j]), putchar(' ');
                putchar('\n');
            }
        }
    } else
        write(-1), putchar('\n');
    return 0;
}