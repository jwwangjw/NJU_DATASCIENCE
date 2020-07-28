#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <ctime>
using namespace std;
const int maxn = 500100;
struct sides {
    int a, b;
    long long w;
    bool operator<(const sides &a) const { return w < a.w; }
} s[maxn];
int n, m, L;
int v[maxn];
namespace force1 {
int par[maxn];
int num[maxn] = { 0 };
int getr(int x) {
    if (x == par[x])
        return x;
    return par[x] = getr(par[x]);
}
long long ans = 0;
void merge(int ra, int rb, long long w) {
    ans += w * num[ra] * num[rb];
    par[ra] = rb;
    num[rb] += num[ra];
}
void force1() {
    sort(s + 1, s + m + 1);
    for (int i = 1; i <= n; i++) {
        par[i] = i;
        num[i] = 1;
    }
    for (int i = 1; i <= m; i++) {
        int ra = getr(s[i].a), rb = getr(s[i].b);
        if (ra != rb) {
            // cout << s[i].a << " " << s[i].b << " " << ra << " " << rb << " " << s[i].w << endl;
            merge(ra, rb, s[i].w);
            // cout << ans << endl;
        }
    }
    cout << ans << endl;
}
}  // namespace force1
namespace force2 {
int par[maxn], num[maxn][55] = { 0 }, h[maxn][55] = { 0 };
int getr(int x) {
    if (x == par[x])
        return x;
    return par[x] = getr(par[x]);
}
long long ans = 0;
void merge(int ra, int rb, long long w) {
    // for(int i = 1; i <= 11; i ++)
    // cout << num[ra][i] << " " << h[ra][i] << " " << num[rb][i] << " " << h[rb][i] << endl;
    for (int i = 1; i + L <= 51; i++)
        ans +=
            w * num[ra][i] * (h[rb][51] - h[rb][i + L - 1]) + w * num[rb][i] * (h[ra][51] - h[ra][i + L - 1]);
    par[ra] = rb;
    for (int i = 1; i <= 51; i++) {
        num[rb][i] += num[ra][i];
        h[rb][i] = h[rb][i - 1] + num[rb][i];
    }
    // for(int i = 1; i <= 11; i ++)
    // cout << num[rb][i] << " " << h[rb][i] << endl;
}
void force2() {
    sort(s + 1, s + m + 1);
    for (int i = 1; i <= n; i++) {
        par[i] = i;
        num[i][v[i]] = 1;
        for (int j = v[i]; j <= 51; j++) h[i][j] = 1;
    }
    for (int i = 1; i <= m; i++) {
        int ra = getr(s[i].a), rb = getr(s[i].b);
        if (ra != rb) {
            // cout << s[i].a << " " << s[i].b << " " << ra << " " << rb << " " << s[i].w << endl;
            merge(ra, rb, s[i].w);
            // cout << ans << endl;
        }
    }
    cout << ans << endl;
}
}  // namespace force2
namespace force3 {
typedef struct node {
    int v, t, h;
    node *lch, *rch;
    node(int v) : v(v), t(1), h(rand()), lch(0), rch(0) {}
} * pnode;
int par[maxn];
pnode root[maxn];
int getr(int x) {
    if (x == par[x])
        return x;
    return par[x] = getr(par[x]);
}
long long ans = 0;
int gett(pnode r) {
    if (!r)
        return 0;
    return r->t;
}
int ask(pnode r, int x, bool asd) {
    if (!r)
        return 0;
    if (!asd) {
        if (r->v > x)
            return ask(r->lch, x, asd);
        else
            return ask(r->rch, x, asd) + gett(r->lch) + 1;
    }
    if (asd) {
        if (r->v >= x)
            return ask(r->lch, x, asd) + gett(r->rch) + 1;
        else
            return ask(r->rch, x, asd);
    }
}
void update(pnode r) { r->t = gett(r->lch) + gett(r->rch) + 1; }
void insert(pnode &r, int x) {
    if (!r) {
        r = new node(x);
        return;
    }
    if (x < r->v) {
        insert(r->lch, x);
        if (r->lch->h > r->h) {
            pnode tmp = r->lch;
            r->lch = tmp->rch;
            update(r);
            tmp->rch = r;
            r = tmp;
            update(r);
        }
    } else {
        insert(r->rch, x);
        if (r->rch->h > r->h) {
            pnode tmp = r->rch;
            r->rch = tmp->lch;
            update(r);
            tmp->lch = r;
            r = tmp;
            update(r);
        }
    }
    update(r);
}
void get(pnode r, pnode rr, long long w) {
    if (!r)
        return;
    if (r->v > L)
        ans += ask(rr, r->v - L, 0) * w;
    ans += ask(rr, r->v + L, 1) * w;
    get(r->lch, rr, w);
    get(r->rch, rr, w);
}
void INS(pnode r, pnode &rr) {
    if (!r)
        return;
    INS(r->lch, rr);
    INS(r->rch, rr);
    insert(rr, r->v);
}
void merge(int ra, int rb, long long w) {
    if (gett(root[ra]) > gett(root[rb]))
        swap(ra, rb);
    // cout << "ra = " << ra << "  rb =  " << rb << " " << "   ra.t = " << root[ra]->t << "    rb.t =  " <<
    // root[rb]->t << endl;
    get(root[ra], root[rb], w);
    INS(root[ra], root[rb]);
    par[ra] = rb;
}
void force3() {
    sort(s + 1, s + m + 1);
    for (int i = 1; i <= n; i++) {
        par[i] = i;
        root[i] = new node(v[i]);
    }
    for (int i = 1; i <= m; i++) {
        int ra = getr(s[i].a), rb = getr(s[i].b);
        if (ra != rb) {
            // cout << s[i].a << " " << s[i].b << " " << ra << " " << rb << " " << s[i].w << endl;
            merge(ra, rb, s[i].w);
            // cout << ans << endl;
        }
    }
    cout << ans << endl;
}
}  // namespace force3
int main() {
    // freopen("graph.in", "r", stdin);
    // freopen("graph.out", "w", stdout);
    std::ios::sync_with_stdio(false);
    cin >> n >> m >> L;
    bool asd = 0;
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
        v[i]++;
        if (v[i] > 51)
            asd = 1;
    }
    for (int i = 1; i <= m; i++) cin >> s[i].a >> s[i].b >> s[i].w;

    if (L == 0)
        force1::force1();
    else if (!asd)
        force2::force2();
    else
        force3::force3();

    // force3::force3();
    return 0;
}
/*
4 5 2
6 4 5 2
1 2 8
2 3 7
2 4 8
1 3 2
1 4 1
*/