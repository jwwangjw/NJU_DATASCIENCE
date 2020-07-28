#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;
const int inf = 1 << 30;
struct node {
    int ls, rs, sum;
} t[7000005];
struct qu {
    int s, t, l, r, len, id;
} q[100005];
char A[100005], B[100005];
int m, s[200005], rnk[400005], pos[200005], sa[200005], buc[200005], tmp[200005], ht[200005];
int sz = 0, root[200005], st[200005][18], log_2[200005], bz[100005][17];
pair<ull, int> vec[100005];
ull has[100005];
long long res[100005], sum[100005][17];
int read() {
    char c = getchar();
    int x = 0;
    while (c < '0' || c > '9') c = getchar();
    while (c >= '0' && c <= '9') {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x;
}
void bucsort(int n) {
    for (int i = 0; i <= m; ++i) buc[i] = 0;
    for (int i = 1; i <= n; ++i) ++buc[rnk[pos[i]]];
    for (int i = 1; i <= m; ++i) buc[i] += buc[i - 1];
    for (int i = n; i >= 1; i--) sa[buc[rnk[pos[i]]]--] = pos[i];
}
void build_SA(int n) {
    m = 27;
    for (int i = 1; i <= n; ++i) rnk[i] = s[i], pos[i] = i;
    bucsort(n);
    for (int k = 1; k <= n; k <<= 1) {
        int p = 0;
        for (int i = n - k + 1; i <= n; ++i) pos[++p] = i;
        for (int i = 1; i <= n; ++i)
            if (sa[i] > k)
                pos[++p] = sa[i] - k;
        bucsort(n);
        p = 1;
        tmp[sa[1]] = 1;
        for (int i = 2; i <= n; ++i) {
            if (rnk[sa[i]] == rnk[sa[i - 1]] && rnk[sa[i] + k] == rnk[sa[i - 1] + k])
                tmp[sa[i]] = p;
            else
                tmp[sa[i]] = ++p;
        }
        memcpy(rnk, tmp, sizeof(tmp));
        if (p == n)
            break;
        m = p;
    }
    int k = 0;
    for (int i = 1; i <= n; ++i) {
        if (k)
            --k;
        int j = sa[rnk[i] - 1];
        while (i + k <= n && j + k <= n && s[i + k] == s[j + k]) ++k;
        ht[rnk[i]] = k;
    }
    for (int i = 1; i <= n; ++i) log_2[i] = log(i) / log(2);
    for (int i = 1; i <= n; ++i) st[i][0] = ht[i];
    for (int j = 1; j <= 17; ++j) {
        for (int i = 1; i + (1 << j) - 1 <= n; ++i) {
            st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
        }
    }
}
int query(int l, int r) {
    int t = log_2[r - l + 1];
    return min(st[l][t], st[r - (1 << t) + 1][t]);
}
int findL(int x, int k) {
    int l = 1, r = x, mid;
    while (r - l > 2) {
        mid = (l + r) >> 1;
        if (query(mid, x) >= k)
            r = mid;
        else
            l = mid;
    }
    for (int i = r; i >= l; i--)
        if (ht[i] < k)
            return i;
    return 1;
}
int findR(int x, int k, int n) {
    int l = x, r = n, mid;
    while (r - l > 2) {
        mid = (l + r) >> 1;
        if (query(x, mid) >= k)
            l = mid;
        else
            r = mid;
    }
    for (int i = l; i <= r; ++i)
        if (ht[i] < k)
            return i;
    return n + 1;
}
int insert(int old, int x, int l, int r) {
    int now = ++sz;
    t[now] = t[old];
    ++t[now].sum;
    if (l == r)
        return now;
    int mid = (l + r) >> 1;
    if (x <= mid)
        t[now].ls = insert(t[old].ls, x, l, mid);
    else
        t[now].rs = insert(t[old].rs, x, mid + 1, r);
    return now;
}
int query(int oldl, int oldr, int x, int y, int l, int r) {
    if (y < l || r < x || t[oldr].sum == t[oldl].sum)
        return inf;
    if (l == r)
        return l;
    int mid = (l + r) >> 1;
    if (x <= l && r <= y) {
        if (t[t[oldr].ls].sum > t[t[oldl].ls].sum)
            return query(t[oldl].ls, t[oldr].ls, x, y, l, mid);
        else
            return query(t[oldl].rs, t[oldr].rs, x, y, mid + 1, r);
    }
    return min(query(t[oldl].ls, t[oldr].ls, x, y, l, mid), query(t[oldl].rs, t[oldr].rs, x, y, mid + 1, r));
}
bool cmp(qu x, qu y) { return x.len < y.len; }
int main() {
    //	freopen("cover4.in","r",stdin);
    //	freopen("cover4.ans","w",stdout);
    int n = read(), K = read();
    scanf("%s", A + 1);
    scanf("%s", B + 1);
    for (int i = 1; i <= n; ++i) s[i] = A[i] - 'a' + 1;
    s[n + 1] = 27;
    for (int i = n + 2; i <= 2 * n + 1; ++i) s[i] = B[i - n - 1] - 'a' + 1;
    build_SA(2 * n + 1);
    for (int i = 1; i <= 2 * n + 1; ++i) {
        if (sa[i] <= n)
            root[i] = insert(root[i - 1], sa[i], 1, n);
        else
            root[i] = root[i - 1];
    }
    int Q = read(), tot = 0;
    for (int i = 1; i <= Q; ++i) {
        int s = read(), t = read(), l = read(), r = read();
        if (r - l <= 50) {
            q[++tot].s = s;
            q[tot].t = t;
            q[tot].l = l;
            q[tot].r = r;
            q[tot].len = r - l;
            q[tot].id = i;
            continue;
        }
        int p = rnk[l + n + 1];
        int L = findL(p, r - l + 1) - 1, R = findR(p + 1, r - l + 1, 2 * n + 1) - 1;
        long long ans = 0;
        int tp = query(root[L], root[R], s, t, 1, n);
        while (tp + r - l <= t) {
            ans += K - tp;
            s = tp + r - l + 1;
            tp = query(root[L], root[R], s, t, 1, n);
        }
        res[i] = ans;
    }
    sort(q + 1, q + tot + 1, cmp);
    int j = 1;
    for (int i = 0; i <= min(50, n - 1); ++i) {
        int cnt = 0;
        for (int k = 1; k + i <= n; ++k)
            vec[++cnt] = make_pair(has[k] = has[k] * (ull)131 + (ull)A[k + i], k);
        if (j > tot || q[j].len != i)
            continue;
        sort(vec + 1, vec + cnt + 1);
        for (int k = 0; k <= 16; ++k) bz[n + 1][k] = n + 1;
        int l = 1;
        for (int k = 1; k <= cnt; ++k) {
            while (l <= cnt && vec[l].first == vec[k].first && vec[l].second - vec[k].second <= i) ++l;
            if (l <= cnt && vec[l].first == vec[k].first && vec[l].second - vec[k].second > i) {
                bz[vec[k].second][0] = vec[l].second;
            } else
                bz[vec[k].second][0] = n + 1;
            sum[vec[k].second][0] = K - vec[k].second;
        }
        for (int k = 1; k <= 16; ++k) {
            for (int u = 1; u <= n; ++u) {
                sum[u][k] = sum[u][k - 1] + sum[bz[u][k - 1]][k - 1];
                bz[u][k] = bz[bz[u][k - 1]][k - 1];
            }
        }
        while (j <= tot && q[j].len == i) {
            int l = q[j].l, r = q[j].r, s = q[j].s, t = q[j].t;
            int p = rnk[l + n + 1];
            int L = findL(p, r - l + 1) - 1, R = findR(p + 1, r - l + 1, 2 * n + 1) - 1;
            long long ans = 0;
            int tp = query(root[L], root[R], s, t, 1, n);
            if (tp != inf && tp + r - l <= t) {
                for (int k = 16; k >= 0; k--) {
                    if (bz[tp][k] + r - l <= t) {
                        ans += sum[tp][k];
                        tp = bz[tp][k];
                    }
                }
                ans += K - tp;
                res[q[j].id] = ans;
            }
            ++j;
        }
    }
    for (int i = 1; i <= Q; ++i) printf("%lld\n", res[i]);
    return 0;
}