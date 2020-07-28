#include <bits/stdc++.h>
using namespace std;
#define S 2000005
int fi[S], len[S], c[26][S], f[S], pc = 1, lst = 1, mx[S], k, q[S], t, h = 1, can[S];
long long ans;
char s[S], o[S];
void insert(int C) {
    int p = lst, np = lst = ++pc, q, nq;
    len[np] = fi[np] = len[p] + 1;
    for (; p && !c[C][p]; p = f[p]) c[C][p] = np;
    if (!p) {
        f[np] = 1;
        return;
    }
    q = c[C][p];
    if (len[q] == len[p] + 1) {
        f[np] = q;
        return;
    }
    len[nq = ++pc] = len[p] + 1;
    fi[nq] = fi[q];
    for (int i = 0; i < 26; ++i) c[i][nq] = c[i][q];
    f[nq] = f[q];
    f[q] = f[np] = nq;
    for (; c[C][p] == q; p = f[p]) c[C][p] = nq;
}
int l[S], to[S], ec, fir[S];
void dfs(int p) {
    for (int i = fir[p]; i; i = l[i]) dfs(to[i]), mx[p] = max(mx[p], mx[to[i]]);
    mx[p] = max(mx[p], can[fi[p]]);
    ans += max(0, min(len[p], mx[p]) - len[f[p]]);
}
int main() {  // freopen("1.in","r",stdin);
    scanf("%s%s%d", s + 1, o + 1, &k);
    t = k + 1;
    for (int i = 1; s[i]; ++i) {
        insert(s[i] - 'a');
        if (o[i] ^ 49)
            q[++t] = i, h++;
        can[i] = i - q[h];
    }
    for (int i = 2; i <= pc; ++i) l[++ec] = fir[f[i]], fir[f[i]] = ec, to[ec] = i;
    dfs(1);
    cout << ans << endl;
}