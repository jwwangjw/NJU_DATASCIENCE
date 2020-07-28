#include <bits/stdc++.h>
#define FI first
#define SE second
#define maxn 200005
#define MP make_pair
#define ull unsigned long long
#define mod 1000000009
using namespace std;
typedef pair<int, int> pi;
const ull p = 1234321237ull;
int pre[maxn], to[maxn], las[maxn], num[maxn], inc;
ull bas[2] = { 998244353ull, 19260817 };
void ins(int a, int b, int c) {
    pre[++inc] = las[a];
    las[a] = inc, to[inc] = b, num[inc] = c;
}
int sz[maxn], vis[maxn], Mn = 1e9, rt;
void getsz(int x, int f) {
    sz[x] = 1;
    for (int i = las[x]; i; i = pre[i]) {
        int y = to[i];
        if (y == f || vis[y])
            continue;
        getsz(y, x), sz[x] += sz[y];
    }
}
void getrt(int x, int f, int d) {
    int Mx = d - sz[x];
    for (int i = las[x]; i; i = pre[i]) {
        int y = to[i];
        if (y == f || vis[y])
            continue;
        getrt(y, x, d), Mx = max(Mx, sz[y]);
    }
    if (Mn > Mx)
        Mn = Mx, rt = x;
}
namespace AC {
int ch[maxn][2], fail[maxn], tot = 1;
queue<int> q;
int pre[maxn], to[maxn], las[maxn], inc;
void Init() {
    for (int i = 1; i <= tot; i++) ch[i][0] = ch[i][1] = 0;
    tot = 1;
}
void Build() {
    for (int c = 0; c < 2; c++)
        if (ch[1][c])
            q.push(ch[1][c]), fail[ch[1][c]] = 1;
        else
            ch[1][c] = 1;
    while (q.size()) {
        int x = q.front();
        q.pop();
        for (int c = 0; c < 2; c++)
            if (ch[x][c])
                q.push(ch[x][c]), fail[ch[x][c]] = ch[fail[x]][c];
            else
                ch[x][c] = ch[fail[x]][c];
    }
}
}  // namespace AC
struct prog {
    int fi, la, d;
};
prog pa[maxn][17], nw[17];  // first表示公差，second表示首项
ull Ha[maxn], IHa[maxn], pw[maxn];
int dep[maxn];
vector<int> id[maxn];
void AddTree(int x, int f, int now, int d) {
    memset(pa[x], 0, sizeof(pa[x]));
    dep[x] = d, id[now].push_back(x);
    int ty = -1;
    if (Ha[d] == IHa[d] && d) {
        prog &la = nw[nw[0].d];
        if (la.fi == la.la && nw[0].d)
            la.la = d, la.d = la.la - la.fi, ty = 0;
        else if (la.d == d - la.la)
            la.la = d, ty = 1;
        else
            nw[++nw[0].d] = (prog){ d, d, 0 }, ty = 2;
    }
    memcpy(pa[x], nw, sizeof(nw));
    for (int i = las[x]; i; i = pre[i]) {
        int y = to[i];
        if (y == f || vis[y])
            continue;
        int &t = AC::ch[now][num[i]];
        if (!t)
            t = ++AC::tot;
        IHa[d + 1] = (pw[d] * bas[num[i]] % mod + IHa[d]) % mod;
        Ha[d + 1] = (Ha[d] * p % mod + bas[num[i]]) % mod;
        AddTree(y, x, t, d + 1);
    }
    prog &la = nw[nw[0].d - (ty == 2)];
    if (ty == 0)
        la.la = la.fi, la.d = 0;
    if (ty == 1)
        la.la -= la.d;
    if (ty == 2)
        nw[0].d--;
}
vector<int> T[maxn];
vector<prog> Q[maxn];                               // clear!!!!
int stk[maxn], ptk[maxn], cc[maxn], cnt[5][5], tp;  // clear!!!!
long long GetQuery(int x, int ty) {
    long long ret = 0;
    stk[++tp] = dep[id[x][0]], ptk[tp] = x;

    if (x != 1 || (x == 1 && ty == -1)) {
        for (int i = 1; i <= 4; i++) cnt[i][stk[tp] % i] += id[x].size();
        cc[stk[tp]] += id[x].size();
    }

    for (int i = 0; i < id[x].size(); i++) {
        int tx = id[x][i];
        for (int j = 1; j <= pa[tx][0].d; j++) {
            prog &cur = pa[tx][j];
            if (!cur.d)
                ret += cc[stk[tp] - cur.fi];
            else if (cur.d <= 4) {
                int res = (stk[tp] - cur.fi) % cur.d;
                int l = lower_bound(stk + 1, stk + tp + 1, stk[tp] - cur.la) - stk;
                l -= (stk[l] >= stk[tp] - cur.la);
                int r = lower_bound(stk + 1, stk + tp + 1, stk[tp] - cur.fi) - stk;
                r -= (stk[r] != stk[tp] - cur.fi);
                if (l)
                    l = ptk[l], Q[l].push_back((prog){ res, -1, cur.d });
                r = ptk[r], Q[r].push_back((prog){ res, 1, cur.d });
            } else
                for (int t = cur.fi; t <= cur.la; t += cur.d) ret += cc[stk[tp] - t];
        }
    }

    for (int i = 0; i < T[x].size(); i++) ret += GetQuery(T[x][i], ty);

    for (int i = 0; i < Q[x].size(); i++) {
        prog &cur = Q[x][i];
        ret += 1ll * cnt[cur.d][cur.fi] * cur.la;
    }

    if (x != 1 || (x == 1 && ty == -1)) {
        for (int i = 1; i <= 4; i++) cnt[i][stk[tp] % i] -= id[x].size();
        cc[stk[tp]] -= id[x].size();
    }
    tp--;
    return ret;
}
long long ans = 0;
void Calc(int x, int w) {
    for (int i = 1; i <= AC::tot; i++) id[i].clear();
    AC::Init();
    if (w == -1)
        AddTree(x, 0, 1, 0);
    else {
        AC::ch[1][w] = ++AC::tot;
        Ha[1] = IHa[1] = bas[w];
        AddTree(x, 0, 2, 1);
    }
    AC::Build();
    for (int i = 1; i <= AC::tot; i++) T[i].clear(), Q[i].clear();
    for (int i = 2; i <= AC::tot; i++) T[AC::fail[i]].push_back(i);
    ans += (w != -1 ? -1 : 1) * GetQuery(1, w);
    for (int i = 1; i <= AC::tot; i++)
        ans += (w != -1 ? -1ll : 1ll) * (long long)id[i].size() * ((long long)id[i].size() - 1) / 2;
}
void DC(int x) {
    vis[x] = 1, Calc(x, -1);
    for (int i = las[x]; i; i = pre[i]) {
        int y = to[i];
        if (vis[y])
            continue;
        Calc(y, num[i]);
        Mn = 1e9, getsz(y, x), getrt(y, x, sz[y]), DC(rt);
    }
}
int n;
int main() {
    scanf("%d", &n);
    pw[0] = 1;
    for (int i = 1; i <= n; i++) pw[i] = pw[i - 1] * p % mod;
    for (int i = 1, u, v, c; i < n; i++) scanf("%d%d%d", &u, &v, &c), ins(u, v, c), ins(v, u, c);
    Mn = 1e9, getsz(1, 0), getrt(1, 0, n), DC(rt);
    printf("%lld\n", ans);
    return 0;
}