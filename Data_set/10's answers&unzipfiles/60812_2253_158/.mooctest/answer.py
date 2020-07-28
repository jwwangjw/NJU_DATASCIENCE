#include <bits/stdc++.h>
#define R register
#define INF 0x7fffffff
#define rep(i, a, b) for (R int i = a; i <= b; ++i)
#define dwn(i, a, b) for (R int i = a; i >= b; --i)
#define go(i, u) for (R int i = head[u]; i; i = a[i].next)
using namespace std;

inline int read() {
    int res = 0, f = 1;
    char ch;
    while (!isdigit(ch = getchar()))
        if (ch == '-')
            f = -1;
    do {
        res = res * 10 + ch - '0';
    } while (isdigit(ch = getchar()));
    return res * f;
}

const int N = 50005, M = 255;

int n, m, num, block, lft[M], rht[M], bel[N];

int a[N], b[N];

inline void build() {
    n = read(), m = read(), block = sqrt(n), num = n / block;
    if (n % block)
        ++num;
    rep(i, 1, n) a[i] = read();
    rep(i, 1, n) bel[i] = (i - 1) / block + 1;
    rep(i, 1, num) lft[i] = (i - 1) * block + 1, rht[i] = i * block;
    rht[num] = n;
    rep(i, 1, num) {
        rep(j, lft[i], rht[i]) b[j] = a[j];
        sort(b + lft[i], b + rht[i] + 1);
    }
}

inline int op1(int key, int l, int r) {
    int ans = 0;
    if (bel[l] == bel[r]) {
        rep(i, l, r) ans += (a[i] < key);
        return ans + 1;
    }
    rep(i, l, rht[bel[l]]) ans += (a[i] < key);
    rep(i, bel[l] + 1, bel[r] - 1) {
        int pos = lower_bound(b + lft[i], b + rht[i] + 1, key) - b - lft[i];
        if (pos < 0)
            continue;
        ans += pos;
    }
    rep(i, lft[bel[r]], r) ans += (a[i] < key);
    return ans + 1;
}

inline int op2(int kth, int l, int r) {
    int ans = 0, ll = 0, rr = 1e8;
    if (bel[l] == bel[r]) {
        while (ll <= rr) {
            int mid = ll + rr >> 1, sum = 0;
            rep(i, l, r) sum += (a[i] <= mid);
            if (sum < kth)
                ll = mid + 1;
            else
                ans = mid, rr = mid - 1;
        }
        return ans;
    }
    while (ll <= rr) {
        int mid = ll + rr >> 1, sum = 0;
        rep(i, l, rht[bel[l]]) sum += (a[i] <= mid);
        rep(i, bel[l] + 1, bel[r] - 1) {
            int num = upper_bound(b + lft[i], b + rht[i] + 1, mid) - b - lft[i];
            if (num < 0)
                continue;
            sum += num;
        }
        rep(i, lft[bel[r]], r) sum += (a[i] <= mid);
        if (sum < kth)
            ll = mid + 1;
        else
            ans = mid, rr = mid - 1;
    }
    return ans;
}

inline void op3(int pos, int key) {
    a[pos] = key;
    rep(i, lft[bel[pos]], rht[bel[pos]]) b[i] = a[i];
    sort(b + lft[bel[pos]], b + rht[bel[pos]] + 1);
}

inline int op4(int key, int l, int r) {
    int ans = -INF;
    if (bel[l] == bel[r]) {
        rep(i, l, r) if (a[i] > ans && a[i] < key) ans = a[i];
        return ans;
    }
    rep(i, l, rht[bel[l]]) if (a[i] > ans && a[i] < key) ans = a[i];
    rep(i, bel[l] + 1, bel[r] - 1) {
        int pos = lower_bound(b + lft[i], b + rht[i] + 1, key) - b - 1;
        if (pos < lft[i])
            continue;
        ans = max(ans, b[pos]);
    }
    rep(i, lft[bel[r]], r) if (a[i] > ans && a[i] < key) ans = a[i];
    return ans;
}

inline int op5(int key, int l, int r) {
    int ans = INF;
    if (bel[l] == bel[r]) {
        rep(i, l, r) if (a[i] < ans && a[i] > key) ans = a[i];
        return ans;
    }
    rep(i, l, rht[bel[l]]) if (a[i] < ans && a[i] > key) ans = a[i];
    rep(i, bel[l] + 1, bel[r] - 1) {
        int pos = upper_bound(b + lft[i], b + rht[i] + 1, key) - b;
        if (pos > rht[i])
            continue;
        ans = min(ans, b[pos]);
    }
    rep(i, lft[bel[r]], r) if (a[i] < ans && a[i] > key) ans = a[i];
    return ans;
}

int main() {
    build();
    while (m--) {
        int op = read(), x = read(), y = read(), v;
        if (op == 1)
            v = read(), printf("%d\n", op1(v, x, y));
        else if (op == 2)
            v = read(), printf("%d\n", op2(v, x, y));
        else if (op == 3)
            op3(x, y);
        else if (op == 4)
            v = read(), printf("%d\n", op4(v, x, y));
        else
            v = read(), printf("%d\n", op5(v, x, y));
    }
    return 0;
}