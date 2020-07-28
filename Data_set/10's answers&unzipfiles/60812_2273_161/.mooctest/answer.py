// just4test
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 30009;
const int MAXK = 500009;
const int MAXNK = 26000000;

int n, k, fa[MAXN], a[MAXN], v[MAXN], sum[MAXN];
int F[MAXNK], G[MAXNK];
int L, R, Que[MAXK], QueV[MAXK];
int deg[MAXN], Node[MAXN];

char buf[30];

void Init() {
    gets(buf);
    sscanf(buf, "%d%d", &n, &k);
    for (int i = 0; i <= n + 1; i++) deg[i] = 0;
    for (int i = 1; i <= n; i++) {
        gets(buf);
        sscanf(buf, "%d%d%d", &fa[i], &a[i], &v[i]);
        if (i > 1)
            deg[fa[i]]++;
    }
    for (int i = 1; i <= n + 1; i++) deg[i] += deg[i - 1];
    for (int i = 2; i <= n; i++) Node[deg[fa[i]]--] = i;
    for (int i = 1; i <= n; i++) deg[i] = deg[i + 1];
}

void PutF(int x, int i, int val) { F[x * (k + 1) + i] = val; }
int GetF(int x, int i) { return F[x * (k + 1) + i]; }
void RefreshF(int x, int i, int val) { PutF(x, i, max(GetF(x, i), val)); }

void PutG(int x, int i, int val) { G[x * (k + 1) + i] = val; }
int GetG(int x, int i) { return G[x * (k + 1) + i]; }
void RefreshG(int x, int i, int val) { PutG(x, i, max(GetG(x, i), val)); }

void MultiFoldBagF(int x, int y, int ti, int val) {
    PutF(y, 0, 0);
    if (ti == 0) {
        for (int i = 1; i <= k; i++) PutF(y, i, GetF(x, i));
        return;
    }
    Que[L = R = 1] = QueV[1] = 0;
    for (int i = 1, v = val; i <= k; i++, v += val) {
        if (Que[L] < i - ti)
            L++;
        PutF(y, i, max(GetF(x, i), QueV[L] + v));
        int tmp = GetF(x, i) - v;
        while (L <= R && tmp > QueV[R]) R--;
        Que[++R] = i;
        QueV[R] = tmp;
    }
}

void MultiFoldBagG(int x, int y, int ti, int val) {
    Que[L = R = 1] = QueV[1] = 0;
    for (int i = 1, v = val; i <= k; i++, v += val) {
        if (Que[L] < i - ti)
            L++;
        RefreshG(y, i, QueV[L] + v);
        int tmp = GetG(x, i) - v;
        while (L <= R && tmp > QueV[R]) R--;
        Que[++R] = i;
        QueV[R] = tmp;
    }
}

void DPF(int fx, int x) {
    sum[x] = sum[fx] + v[x];
    MultiFoldBagF(fx, x, a[x] - 1, v[x]);
    for (int o = deg[x - 1] + 1; o <= deg[x]; o++) {
        int y = Node[o];
        DPF(x, y);
        for (int i = 1; i <= k; i++) RefreshF(x, i, GetF(y, i - 1) + v[y]);
    }
}

void DPG(int fx, int x) {
    for (int i = 0; i <= k; i++) PutG(x, i, GetG(fx, i));
    for (int o = deg[x]; o > deg[x - 1]; o--) {
        int y = Node[o];
        DPG(x, y);
        MultiFoldBagG(y, x, a[y], v[y]);
    }
}

void Solve() {
    sum[0] = 0;
    for (int i = 0; i <= k; i++) PutF(0, i, 0);
    DPF(0, 1);
    for (int i = 0; i <= k; i++) PutG(0, i, 0);
    DPG(0, 1);
    int ans = 0;
    for (int i = 1; i <= n; i++)
        if (deg[i] == deg[i - 1])
            for (int j = 0; j <= k; j++) ans = max(ans, GetF(i, j) + GetG(i, k - j) + sum[i]);
    cout << ans << "\n";
}

int main() {
    int Test;
    gets(buf);
    sscanf(buf, "%d", &Test);
    for (int i = 1; i <= Test; i++) {
        Init();
        Solve();
    }
}