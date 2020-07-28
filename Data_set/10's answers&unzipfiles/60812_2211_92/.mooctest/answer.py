#pragma GCC optimize(2)
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2e6 + 50;
int trie[MAXN][26], nxt[MAXN][26], fa[MAXN], len[MAXN];
int id[MAXN], sz[MAXN], c[MAXN], a[MAXN], tot = 1;
char s[MAXN];
inline int Insert(int x, int p) {
    int np = ++tot;
    len[np] = len[p] + 1;
    sz[np] = 1;
    for (; p && !nxt[p][x]; p = fa[p]) nxt[p][x] = np;
    if (!p)
        fa[np] = 1;
    else {
        int q = nxt[p][x];
        if (len[p] + 1 == len[q])
            fa[np] = q;
        else {
            int nq = ++tot;
            len[nq] = len[p] + 1;
            memcpy(nxt[nq], nxt[q], sizeof(nxt[q]));
            fa[nq] = fa[q];
            fa[q] = fa[np] = nq;
            for (; nxt[p][x] == q; p = fa[p]) nxt[p][x] = nq;
        }
    }
    return np;
}
int main() {
    int n, Q;
    scanf("%d%d", &n, &Q);
    for (int i = 1; i <= n; i++) {
        char ch;
        int bel;
        scanf(" %c %d", &ch, &bel);
        trie[bel][ch - 'A'] = i;
    }
    queue<int> que;
    que.push(0);
    id[0] = 1;
    while (!que.empty()) {
        int u = que.front();
        que.pop();
        for (int i = 0; i < 26; i++) {
            if (trie[u][i]) {
                que.push(trie[u][i]);
                id[trie[u][i]] = Insert(i, id[u]);
            }
        }
    }
    for (int i = 1; i <= tot; i++) c[len[i]]++;
    for (int i = 1; i <= tot; i++) c[i] += c[i - 1];
    for (int i = tot; i; i--) a[c[len[i]]--] = i;
    for (int i = tot; i; i--) sz[fa[a[i]]] += sz[a[i]];
    while (Q--) {
        scanf("%s", s);
        int l = strlen(s), rt = 1;
        bool ok = true;
        for (int i = l - 1; i >= 0; i--) {
            if (!nxt[rt][s[i] - 'A']) {
                ok = false;
                break;
            }
            rt = nxt[rt][s[i] - 'A'];
        }
        printf("%d\n", ok ? sz[rt] : 0);
    }
    return 0;
}