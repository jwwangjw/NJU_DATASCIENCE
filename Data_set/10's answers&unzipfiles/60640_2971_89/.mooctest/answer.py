#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 5;
char s[maxn];
int sa[maxn], rk[maxn], tp[maxn], cnt[maxn];
int n, m;
void sort() {
    memset(cnt, 0, sizeof(int) * (m + 1));
    for (int i = 1; i <= n; ++i) ++cnt[rk[i]];
    for (int i = 1; i <= m; ++i) cnt[i] += cnt[i - 1];
    for (int i = n; i >= 1; --i) sa[cnt[rk[tp[i]]]--] = tp[i];
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cin >> (s + 1);
    n = strlen(s + 1);
    m = 'z';
    for (int i = 1; i <= n; ++i) rk[i] = s[i] - '0' + 1, tp[i] = i;
    sort();
    for (int w = 1, p = 0; p < n; m = p, w <<= 1) {
        p = 0;
        for (int i = n; i > n - w; --i) tp[++p] = i;
        for (int i = 1; i <= n; ++i)
            if (sa[i] > w)
                tp[++p] = sa[i] - w;
        sort();
        swap(tp, rk);
        rk[sa[1]] = p = 1;
        for (int i = 2; i <= n; ++i)
            rk[sa[i]] = (tp[sa[i - 1]] == tp[sa[i]] && tp[sa[i - 1] + w] == tp[sa[i] + w]) ? p : ++p;
    }
    for (int i = 1; i <= n; ++i) cout << sa[i] << ' ';
    return 0;
}