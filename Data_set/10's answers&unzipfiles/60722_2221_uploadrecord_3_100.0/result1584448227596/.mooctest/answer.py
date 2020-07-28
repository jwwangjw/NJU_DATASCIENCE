#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#define MAXn 10002
#define MAXm 50002
using namespace std;
int n, m;
struct line {
    int next, to;
} edge[MAXm];
bool instack[MAXn];
int cnt, maxt, dfn[MAXn], low[MAXn], num[MAXn], outdegree[MAXn], numtime[MAXn];
stack<int> stk;
int head[MAXn], _cnt;
void add(int u, int v) {
    edge[_cnt].to = v;
    edge[_cnt].next = head[u];
    head[u] = _cnt;
    _cnt++;
}
void Tarjan(int nownode) {
    int u = nownode;
    dfn[u] = low[u] = ++cnt;
    stk.push(u);
    instack[u] = true;
    for (int i = head[u]; ~i; i = edge[i].next) {
        int v = edge[i].to;
        if (dfn[v] == 0) {
            Tarjan(v);
            low[u] = min(low[u], low[v]);
        } else if (instack[v])
            low[u] = min(low[u], dfn[v]);
    }
    if (dfn[u] == low[u]) {
        maxt++;
        int nextnode;
        do {
            nextnode = stk.top();
            instack[nextnode] = false;
            stk.pop();
            num[nextnode] = maxt, numtime[maxt]++;
        } while (nextnode != u);
    }
    return;
}
int main() {
    cin >> n >> m;
    memset(head, -1, sizeof(head));
    for (int i = 1; i <= m; i++) {
        int x, y;
        cin >> x >> y;
        add(x, y);
    }
    memset(instack, false, sizeof(instack));
    for (int i = 1; i <= n; i++)
        if (num[i] == 0)
            Tarjan(i);
    //	for(int i=1;i<=n;i++) cout<<i<<" ";
    //	cout<<endl;
    //	for(int i=1; i<=n; i++) cout<<low[i]<<" ";
    //	cout<<endl;
    //	for(int i=1; i<=n; i++) cout<<num[i]<<" ";
    //	cout<<endl;
    for (int u = 1; u <= n; u++)
        for (int i = head[u]; ~i; i = edge[i].next) {
            int v = edge[i].to;
            if (num[u] != num[v])
                outdegree[num[u]]++;
        }
    int ans = 0, _ans = 0;
    for (int i = 1; i <= maxt; i++)
        if (outdegree[i] == 0) {
            ans++;
            if (ans > 1) {
                _ans = 0;
                break;
            } else
                _ans = numtime[i];
        }
    cout << _ans << endl;
    return 0;
}
/*
7 11
1 2
2 3
2 5
2 4
3 5
3 7
7 5
5 6
6 7
4 1
4 5
*/