#include <bits/stdc++.h>
using namespace std;

const int maxn = 45;

int n, ans, cnt, A[maxn], l[maxn], r[maxn], lst[maxn];

struct bit {
    int v[maxn];

    void clear(int n) { memset(v + 1, 0, sizeof(int) * n); }
    void add(int x, int a) {
        for (int i = x; i <= n; i += i & (-i)) v[i] += a;
    }
    int sum(int x) {
        int res = 0;
        for (int i = x; i; i -= i & (-i)) res += v[i];
        return res;
    }
    int qry(int l, int r) { return sum(r) - sum(l - 1); }

} up, dwn;

void dfs(int k, int sum) {
    if (sum >= ans)
        return;
    if (k > cnt)
        return ans = sum, void();
    up.add(r[k], 1);
    dfs(k + 1, sum + min(up.qry(l[k], r[k] - 1), up.qry(r[k] + 1, n) + dwn.qry(l[k] + 1, n)));
    up.add(r[k], -1);
    dwn.add(r[k], 1);
    dfs(k + 1, sum + min(dwn.qry(l[k], r[k] - 1), dwn.qry(r[k] + 1, n) + up.qry(l[k] + 1, n)));
    dwn.add(r[k], -1);
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        up.clear(n);
        dwn.clear(n);
        memset(lst + 1, 0, sizeof(int) * n);
        cnt = 0;
        for (int i = 1; i <= n; ++i) scanf("%d", &A[i]);
        for (int i = n; i >= 1; --i) lst[A[i]] ? r[++cnt] = lst[A[i]], l[cnt] = i : lst[A[i]] = i;
        reverse(l + 1, l + cnt + 1);
        reverse(r + 1, r + cnt + 1);

        ans = 1e9;
        dfs(1, 0);
        printf("%d\n", ans);
    }

    return 0;
}