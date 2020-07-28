#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
int n, m, p, l, r, ans;
int a[N], sum[N << 2], tag[N << 2];
struct number {
    int opt, l, r;
} num[N];

void build(int k, int l, int r, int v) {
    if (l == r) {
        sum[k] = (a[l] >= v);
        tag[k] = -1;
        return;
    }
    int mid = l + r >> 1;
    build(k << 1, l, mid, v);
    build(k << 1 | 1, mid + 1, r, v);
    sum[k] = sum[k << 1] + sum[k << 1 | 1];
    tag[k] = -1;
}

inline void pushdown(int k, int l, int r) {
    if (tag[k] == -1)
        return;
    tag[k << 1] = tag[k << 1 | 1] = tag[k];
    int mid = l + r >> 1;
    sum[k << 1] = (mid - l + 1) * tag[k];
    sum[k << 1 | 1] = (r - (mid + 1) + 1) * tag[k];
    tag[k] = -1;
}

void change(int k, int l, int r, int qx, int qy, int v) {
    if (qx > qy)
        return;
    if (qx <= l && r <= qy) {
        sum[k] = (r - l + 1) * v;
        tag[k] = v;
        return;
    }
    pushdown(k, l, r);
    int mid = l + r >> 1;
    if (qx <= mid)
        change(k << 1, l, mid, qx, qy, v);
    if (mid < qy)
        change(k << 1 | 1, mid + 1, r, qx, qy, v);
    sum[k] = sum[k << 1] + sum[k << 1 | 1];
}

int query(int k, int l, int r, int qx, int qy) {
    if (qx <= l && r <= qy)
        return sum[k];
    pushdown(k, l, r);
    int ans = 0;
    int mid = l + r >> 1;
    if (qx <= mid)
        ans += query(k << 1, l, mid, qx, qy);
    if (mid < qy)
        ans += query(k << 1 | 1, mid + 1, r, qx, qy);
    return ans;
}

int query2(int k, int l, int r, int pos) {
    if (l == pos && pos == r)
        return sum[k];
    pushdown(k, l, r);
    int mid = l + r >> 1;
    if (pos <= mid)
        return query2(k << 1, l, mid, pos);
    else
        return query2(k << 1 | 1, mid + 1, r, pos);
}

inline bool jay(int mid) {
    build(1, 1, n, mid);
    for (register int i = 1; i <= m; ++i) {
        int cnt = query(1, 1, n, num[i].l, num[i].r);
        if (!num[i].opt) {
            change(1, 1, n, num[i].r - cnt + 1, num[i].r, 1);
            change(1, 1, n, num[i].l, num[i].r - cnt, 0);
        } else {
            change(1, 1, n, num[i].l, num[i].l + cnt - 1, 1);
            change(1, 1, n, num[i].l + cnt, num[i].r, 0);
        }
    }
    if (query2(1, 1, n, p))
        return true;
    else
        return false;
}

int main() {
    scanf("%d%d", &n, &m);
    for (register int i = 1; i <= n; ++i) scanf("%d", &a[i]);
    for (register int i = 1; i <= m; ++i) scanf("%d%d%d", &num[i].opt, &num[i].l, &num[i].r);
    scanf("%d", &p);
    l = 1;
    r = n;
    while (l <= r) {
        int mid = l + r >> 1;
        if (jay(mid))
            ans = mid, l = mid + 1;
        else
            r = mid - 1;
    }
    printf("%d\n", ans);
    return 0;
}