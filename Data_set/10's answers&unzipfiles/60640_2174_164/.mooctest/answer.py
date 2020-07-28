#include <stdio.h>
#include <bits/stdc++.h>
#define f(a, b, c) for (register int a = (b); a <= (c); ++a)
#define ff(a, b, c) for (register int a = (b); a >= (c); --a)
#define ll long long
#define int long long
#define pc putchar
#define pe putchar('\n')
#define ps putchar(' ')
#define wer rd()
using namespace std;
char *p1, *p2, buf[1 << 20];
#define GC (p1 == p2 && (p1 = buf, p2 = buf + fread(buf, 1, 1 << 20, stdin), p1 == p2) ? 0 : (*(p1++)))
//#define GC getchar()
inline ll wer {
    ll ans;
    char t, k;
    while (((t = GC) != '-') && (t > '9' || t < '0'))
        ;
    k = (t == '-');
    ans = k ? 0 : (t - '0');
    while ((t = GC) >= '0' && t <= '9') ans = ans * 10 + t - '0';
    return k ? -ans : ans;
}
inline void wt(ll k) {
    if (k < 0)
        pc('-'), wt(-k);
    else {
        if (k < 10)
            pc('0' + k);
        else
            wt(k / 10), pc('0' + k % 10);
    }
    return;
}
int n, q;
struct edge {
    int x, y, in, out;
};
struct th {
    int x, y;
};
vector<th> qu;
int que;
set<pair<int, int> > s;
map<pair<int, int>, pair<int, int> > mp;
vector<edge> e[20];
vector<pair<int, int> > bian[800010];
void add(int i, int l, int r, int x, int y, pair<int, int> qwq) {
    if (r < x || y < l)
        return;
    if (x <= l && r <= y)
        bian[i].push_back(qwq);
    else {
        int mid = l + r >> 1;
        add(i << 1, l, mid, x, y, qwq);
        add(i << 1 | 1, mid + 1, r, x, y, qwq);
    }
    return;
}
int ans[400010];
int f[400010], si[400010];
int getf(int x) { return f[x] == x ? x : getf(f[x]); }
void getans(int i, int l, int r, int k) {
    vector<int> qwq;
    f(j, 0, (int)(bian[i].size()) - 1) {
        int f1 = getf(bian[i][j].first);
        int f2 = getf(bian[i][j].second);
        if (f1 != f2)
            if (si[f1] > si[f2]) {
                f[f2] = f1;
                si[f1] += si[f2];
                qwq.push_back(f2);
            } else {
                f[f1] = f2;
                si[f2] += si[f1];
                qwq.push_back(f1);
            }
    }
    if (l == r) {
        //		wt(l),pe;
        //		wt(qu[l].x),ps,wt(qu[l].y),pe;
        //		f(i,1,n)wt(f[i]),ps;pe;
        //		wt(getf(qu[l].x)),ps,wt(getf(qu[l].y)),ps;pe;
        if (getf(qu[l].x) == getf(qu[l].y))
            ans[l] = min(ans[l], k);

    } else {
        int mid = l + r >> 1;
        getans(i << 1, l, mid, k);
        getans(i << 1 | 1, mid + 1, r, k);
    }
    ff(j, (int)(qwq.size()) - 1, 0) {
        int fff = getf(qwq[j]);
        si[fff] -= si[qwq[j]];
        f[qwq[j]] = qwq[j];
    }
    return;
}

main() {
    //	freopen("30.in","r",stdin);
    //	freopen("30.out","w",stdout);
    n = wer, q = wer;
    f(i, 1, n) f[i] = i;
    fill(si + 1, si + 1 + n, 1);
    memset(ans, 0x3f, sizeof ans);
    qu.push_back(th{ 0, 0 });
    f(i, 1, q) {
        int ty = wer;
        if (ty == 0) {
            int x = wer + 1, y = wer + 1, v = wer;
            if (x > y)
                swap(x, y);
            s.insert(make_pair(x, y));
            mp[make_pair(x, y)] = make_pair(v, que + 1);
        } else if (ty == 1) {
            int x = wer + 1, y = wer + 1;
            if (x > y)
                swap(x, y);
            if (s.count(make_pair(x, y)))
                s.erase(s.find(make_pair(x, y))),
                    e[mp[make_pair(x, y)].first].push_back(edge{ x, y, mp[make_pair(x, y)].second, que });
        } else {
            que++;
            int x = wer + 1, y = wer + 1;
            if (x > y)
                swap(x, y);
            qu.push_back(th{ x, y });
        }
    }
    //    f(i,1,que)
    //    wt(qu[i].x),ps,wt(qu[i].y),pe;
    for (set<pair<int, int> >::iterator it = s.begin(); it != s.end(); it++) {
        e[mp[*it].first].push_back(edge{ (*it).first, (*it).second, mp[*it].second, que });
    }
    f(i, 0, 9) {
        //        wt(i),pe;
        f(j, 0, (int)(e[i].size()) - 1) {
            add(1, 1, que, e[i][j].in, e[i][j].out, make_pair(e[i][j].x, e[i][j].y));
        }
        getans(1, 1, que, i);
    }
    f(i, 1, que) wt(ans[i] >= 1e9 ? -1 : ans[i]), pe;
}