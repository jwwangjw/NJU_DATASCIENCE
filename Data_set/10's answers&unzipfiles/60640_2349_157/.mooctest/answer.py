#include <bits/stdc++.h>
#define rep(i, a, b) for (int i(a), i##_END(b); i <= i##_END; i++)
#define drep(i, a, b) for (int i(a), i##_END(b); i >= i##_END; i--)
using namespace std;
const int maxn = 800010, maxm = 2400010;
typedef long long ll;
const double pi = acos(-1);

struct Edge {
    int i, y, rig;
    double ang;
    Edge() {}
    Edge(int i, int y, double ang) : i(i), y(y), ang(ang) { rig = 0; }
};
int n, m, K, X[maxn], Y[maxn], cnt, mxe[maxn], begnd, vis[maxn], ontree[maxm], rig[maxm];
int head[maxn], ver[maxm], Next[maxm], tot, pp[maxn], we[maxm];
pair<int, int> rev[maxm];
ll w[maxn], sz[maxn], szq[maxn];
vector<Edge> e[maxn];
set<pair<int, int> > added;
bool operator<(Edge u, Edge v) { return u.ang < v.ang; }

inline int read() {
    int res = 0, f = 1;
    char c = getchar();
    while (c != '-' && (c < '0' || c > '9')) c = getchar();
    if (c == '-')
        f = -1, c = getchar();
    while (c >= '0' && c <= '9') res = (res << 3) + (res << 1) + c - '0', c = getchar();
    return f * res;
}

inline ll getS(int i, int j, int k) {
    ll dx1 = X[j] - X[i], dx2 = X[k] - X[i];
    ll dy1 = Y[j] - Y[i], dy2 = Y[k] - Y[i];
    return -(dx1 * dy2 - dx2 * dy1);
}
void getblock(int x, int las) {
    int i = rev[las].second;
    i = (i + 1) % e[x].size();
    int y = e[x][i].y;
    if (y == begnd)
        cnt++;
    else
        getblock(y, e[x][i].i ^ 1), w[cnt] += getS(begnd, x, y);
    e[x][i].rig = cnt;
}
inline void add(int x, int y) { ver[++tot] = y, Next[tot] = head[x], head[x] = tot; }
void dfs(int x) {
    vis[x] = 1;
    sz[x] = w[x];
    szq[x] = w[x] * w[x];
    for (int i = head[x]; i; i = Next[i])
        if (!vis[ver[i]]) {
            ontree[we[i]] = 1, dfs(ver[i]);
            sz[x] += sz[ver[i]], szq[x] += szq[ver[i]];
        }
}
ll gcd(ll x, ll y) { return x ? gcd(y % x, x) : y; }
inline int Find(int x, ll dy, ll dx) {
    double ang = atan2(dy, dx);
    int l = 0, r = e[x].size() - 1;
    while (l < r) {
        int mid = (l + r) >> 1;
        if (ang > e[x][mid].ang)
            l = mid + 1;
        else
            r = mid;
    }
    int res = -1;
    rep(i, max(0, l - 2),
        min((int)e[x].size() - 1, l + 2)) if (X[x] + dx == X[e[x][i].y] && Y[x] + dy == Y[e[x][i].y]) res = i;
    assert(res >= 0);
    return res;
}

int main() {
    // freopen("mine8.in", "r", stdin);
    // freopen("mine.out", "w", stdout);
    n = read();
    m = read();
    K = read();
    rep(i, 1, n) X[i] = read(), Y[i] = read();
    rep(i, 1, m) {
        int u = read(), v = read();
        double ang = atan2(1.0 * (Y[v] - Y[u]), 1.0 * (X[v] - X[u]));
        e[u].push_back(Edge(i * 2, v, ang));
        if (ang > 0)
            ang -= pi;
        else
            ang += pi;
        e[v].push_back(Edge(i * 2 + 1, u, ang));
    }
    rep(i, 1, n) sort(e[i].begin(), e[i].end());
    rep(i, 1, n) rep(j, 0, e[i].size() - 1) rev[e[i][j].i] = make_pair(i, j);
    rep(i, 1, n) {
        rep(j, 0, e[i].size() - 1) if (!e[i][j].rig) {
            begnd = i;
            getblock(e[i][j].y, e[i][j].i ^ 1);
            e[i][j].rig = cnt;
        }
    }
    // rep(i, 1, cnt) cout << w[i] << endl;
    // rep(i, 1, n) rep(j, 0, e[i].size() - 1) cout << i << ' ' << e[i][j].y << ' ' << e[i][j].rig << endl;
    rep(i, 1, m) {
        pair<int, int> x = rev[i * 2], y = rev[i * 2 + 1];
        int u = e[x.first][x.second].rig, v = e[y.first][y.second].rig;
        rig[i * 2] = u;
        rig[i * 2 + 1] = v;
        if (added.count(make_pair(u, v)))
            continue;
        ;
        add(u, v);
        we[tot] = i * 2 + 1;
        add(v, u);
        we[tot] = i * 2;
        added.insert(make_pair(u, v));
        added.insert(make_pair(v, u));
    }
    int rt = 0;
    rep(i, 1, cnt) if (w[i] < 0) {
        rt = i;
        break;
    }
    w[rt] = 0;
    dfs(rt);
    // cout << szq[rt] << endl;
    // rep(i, 1, m) {
    // if(ontree[i * 2]) cout << rig[i * 2 + 1] << ' ' << rig[i * 2] << endl;
    // if(ontree[i * 2 + 1]) cout << rig[i * 2] << ' ' << rig[i * 2 + 1] << endl;
    //}
    ll lastans = 0;
    while (K--) {
        int d = (read() + lastans) % n + 1;
        rep(i, 0, d - 1) pp[i] = (read() + lastans) % n + 1;
        ll zi = 0, mu = 0;
        // rep(i, 0, d - 1) cout << pp[i] << ' '; cout << endl;
        rep(i, 0, d - 1) {
            int x = pp[i], y = pp[(i + 1) % d];
            int ID = e[x][Find(x, Y[y] - Y[x], X[y] - X[x])].i;
            if (ontree[ID])
                zi -= szq[rig[ID]], mu -= sz[rig[ID]];
            if (ontree[ID ^ 1])
                zi += szq[rig[ID ^ 1]], mu += sz[rig[ID ^ 1]];
        }
        mu *= 2;
        ll dd = gcd(zi, mu);
        // cout << zi << ' ' << mu << ' ' << dd << endl;
        zi /= dd;
        mu /= dd;
        lastans = zi;
        printf("%lld %lld\n", zi, mu);
    }
    return 0;
}