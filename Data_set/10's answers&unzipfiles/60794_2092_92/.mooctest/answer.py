#include <iostream>
#include <cstdio>
using namespace std;
int read() {
    int xx = 0, fh = 1;
    char ch = getchar();
    while (ch > '9' || ch < '0') {
        if (ch == '-')
            fh = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        xx = xx * 10 + ch - '0';
        ch = getchar();
    }
    return fh == 1 ? xx : -xx;
}
void wt(int x) {
    if (x > 9)
        wt(x / 10);
    putchar(x % 10 + '0');
}
int n, m, num, head[200010];
struct node {
    int to;
    int nxt;
} ed[200010];
void add(int u, int v) {
    ++num;
    ed[num].to = v;
    ed[num].nxt = head[u];
    head[u] = num;
}
int sc[200010], ans = 0x7fffffff;
bool b[200010];
void dfs(int u, int t) {
    b[u] = 1;
    sc[u] = t;
    for (int i = head[u]; i; i = ed[i].nxt) {
        int v = ed[i].to;
        if (b[v] == 1) {
            ans = min(t - sc[v] + 1, ans);
            continue;
        }
        if (sc[v] != 0)
            continue;
        b[v] = 1;
        dfs(v, t + 1);
        b[v] = 0;
    }
    b[u] = 0;
}
int main() {
    n = read();
    for (int i = 1; i <= n; ++i) {
        int x = read();
        add(i, x);
    }
    for (int i = 1; i <= n; ++i)
        if (sc[i] == 0)
            dfs(i, 1);
    wt(ans);
    return 0;
}