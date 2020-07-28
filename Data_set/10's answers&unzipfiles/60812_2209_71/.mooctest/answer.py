#include <bits/stdc++.h>
#define ls q << 1
#define rs q << 1 | 1
using namespace std;
const int N = 3e5 + 11;
const int inf = 0x3f3f3f3f;
char s[N], c[N];
int n, m, cnt, trie[N][26], ed[N], tr[N << 2];
int dep[N], f[N], g[N], v[N], fail[N];
queue<int> q;
void insert() {
    int now = 0, len = strlen(c + 1);
    for (int i = 1; i <= len; i++) {
        int num = c[i] - 'a';
        if (!trie[now][num])
            trie[now][num] = ++cnt;
        dep[trie[now][num]] = dep[now] + 1;
        now = trie[now][num];
    }
    ed[now] = 1;
}
void makefail() {
    for (int i = 0; i < 26; i++)
        if (trie[0][i])
            q.push(trie[0][i]);
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        if (ed[x])
            v[x] = dep[x];
        else
            v[x] = v[fail[x]];
        for (int i = 0; i < 26; i++) {
            if (trie[x][i])
                fail[trie[x][i]] = trie[fail[x]][i], q.push(trie[x][i]);
            else
                trie[x][i] = trie[fail[x]][i];
        }
    }
}
void update(int q) { tr[q] = min(tr[ls], tr[rs]); }
int query(int q, int l, int r, int L, int R) {
    if (l >= L && r <= R)
        return tr[q];
    int mid = l + r >> 1, re = inf;
    if (mid >= L)
        re = min(re, query(ls, l, mid, L, R));
    if (mid < R)
        re = min(re, query(rs, mid + 1, r, L, R));
    return re;
}
void modify(int q, int l, int r, int x, int v) {
    if (l == r)
        return tr[q] = v, void();
    int mid = l + r >> 1;
    if (mid >= x)
        modify(ls, l, mid, x, v);
    else
        modify(rs, mid + 1, r, x, v);
    update(q);
}
int read() {
    int x = 0, f = 1;
    char ch = getchar();
    while (!isdigit(ch)) {
        if (ch == '-')
            f = -f;
        ch = getchar();
    }
    while (isdigit(ch)) {
        x = x * 10 + ch - 48;
        ch = getchar();
    }
    return x * f;
}
signed main() {
    m = read();
    scanf("%s", s + 1);
    n = strlen(s + 1);
    for (int i = 1; i <= m; i++) {
        scanf("%s", c + 1);
        insert();
    }
    makefail();
    int now = 0;
    for (int i = 1; i <= n; i++) {
        int x = trie[now][s[i] - 'a'];
        g[i] = v[x];
        now = x;
    }
    memset(tr, 0x3f, sizeof(tr));
    for (int i = 1; i <= n; i++) {
        if (!g[i])
            f[i] = inf;
        else {
            if (g[i] == i)
                f[i] = 1;
            else
                f[i] = query(1, 1, n, i - g[i], i - 1) + 1;
        }
        modify(1, 1, n, i, f[i]);
    }
    printf("%d\n", f[n] >= inf ? -1 : f[n]);
    return 0;
}