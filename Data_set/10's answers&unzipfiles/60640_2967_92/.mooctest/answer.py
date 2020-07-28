#include <bits/stdc++.h>
using namespace std;

const int N = 500010;
int n;
int las = 1, tot = 1;
string st[N];
int Max[N], sa[N], Min[N], tax[N];

struct Node {
    int fa, len, ch[27];
} stm[N];

void add(int c) {
    int p = las, np = las = ++tot;
    stm[np].len = stm[p].len + 1;
    for (; p && !stm[p].ch[c]; p = stm[p].fa) stm[p].ch[c] = np;
    if (!p)
        stm[np].fa = 1;
    else {
        int q = stm[p].ch[c];
        if (stm[q].len == stm[p].len + 1)
            stm[np].fa = q;
        else {
            int nq = ++tot;
            stm[nq] = stm[q];
            stm[q].fa = stm[np].fa = nq;
            stm[nq].len = stm[p].len + 1;
            for (; p && stm[p].ch[c] == q; p = stm[p].fa) stm[p].ch[c] = nq;
        }
    }
}

void insert(string s) {
    for (int i = 0; i < s.size(); ++i) add(s[i] - 'a');
}

void solve(int x) {
    int p = 1, len = 0;
    for (int i = 0; i < st[x].size(); ++i) {
        int c = st[x][i] - 'a';
        while (p && !stm[p].ch[c]) p = stm[p].fa, len = stm[p].len;
        if (p) {
            ++len;
            p = stm[p].ch[c];
            Max[p] = max(Max[p], len);
        } else
            p = 1, len = 0;
    }
    for (int i = tot; i > 0; --i) {
        int fa = stm[sa[i]].fa;
        Max[fa] = max(Max[fa], min(Max[sa[i]], stm[fa].len));
        Min[sa[i]] = min(Min[sa[i]], Max[sa[i]]);
    }
    memset(Max, 0, sizeof(Max));
}

void Sort() {
    for (int i = 1; i <= tot; ++i) ++tax[stm[i].len];
    for (int i = 1; i <= tot; ++i) tax[i] += tax[i - 1];
    for (int i = 1; i <= tot; ++i) sa[tax[stm[i].len]--] = i;
}

int main() {
    memset(Min, 0x3f, sizeof(Min));
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> st[i];
    insert(st[0]);
    Sort();
    for (int i = 1; i < n; ++i) solve(i);
    int ans = 0;
    for (int i = 1; i <= tot; ++i) {
        ans = max(ans, Min[i]);
    }
    cout << ans << endl;
    return 0;
}