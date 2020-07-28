#include <bits/stdc++.h>
using namespace std;
#define N 10005
queue<int> q;
vector<int> v[N];
int t, n, m, x, y, a[N], r[N], vis[N];
void dfs(int k, int fa) {
    if (vis[k])
        return;
    vis[k] = 1;
    if (r[k] > 2)
        a[++a[0]] = k;
    x++;
    for (int i = 0; i < v[k].size(); i++)
        if ((r[v[k][i]] > 1) && (v[k][i] != fa)) {
            if ((fa) || (!vis[v[k][i]]))
                y++;
            dfs(v[k][i], k);
        }
}
void calc(int k, int fa, int x, int s) {
    if (k == x) {
        a[++a[0]] = s;
        return;
    }
    for (int i = 0; i < v[k].size(); i++)
        if ((r[v[k][i]] > 1) && (v[k][i] != fa))
            calc(v[k][i], k, x, s + 1);
}
int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &m);
        memset(r, 0, sizeof(r));
        memset(vis, 0, sizeof(vis));
        for (int i = 1; i <= n; i++) v[i].clear();
        for (int i = 1; i <= m; i++) {
            scanf("%d%d", &x, &y);
            r[x]++;
            r[y]++;
            v[x].push_back(y);
            v[y].push_back(x);
        }
        for (int i = 1; i <= n; i++) {
            if (!r[i])
                vis[i] = 1;
            if (r[i] == 1)
                q.push(i);
        }
        while (!q.empty()) {
            int k = q.front();
            q.pop();
            vis[k] = 1;
            for (int i = 0; i < v[k].size(); i++)
                if (--r[v[k][i]] == 1)
                    q.push(v[k][i]);
        }
        bool flag = 0;
        for (int i = 1; i <= n; i++) {
            x = y = a[0] = 0;
            dfs(i, 0);
            if ((x == y) && (x % 2 == 0))
                continue;
            if ((a[0] < 2) || (x + 1 < y) || (x == y) && (x & 1)) {
                flag = 1;
                break;
            }
            x = a[1];
            y = a[2];
            a[0] = 0;
            calc(x, 0, y, 0);
            sort(a + 1, a + a[0] + 1);
            if ((a[1] & 1) || (a[2] & 1) || (a[3] & 1) || (a[2] > 2)) {
                flag = 1;
                break;
            }
        }
        if (flag)
            printf("NO\n");
        else
            printf("YES\n");
    }
}