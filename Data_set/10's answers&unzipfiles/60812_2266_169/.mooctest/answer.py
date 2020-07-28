#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <queue>
#include <vector>
#include <deque>
#include <string>
#include <ctime>
#include <ext/rope>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/hash_policy.hpp>
#include <ext/pb_ds/trie_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;

template <typename T>
inline void read(T& a) {
    a = 0;
    T f = 1;
    char ch;
    while (!isdigit(ch = getchar()))
        if (ch == '-')
            f = -1;
    while (isdigit(ch)) a = (a << 3) + (a << 1) + (ch ^ '0'), ch = getchar();
    a *= f;
}

template <typename T>
inline void write(T x, char end_, int __st) {
    if (x < 0)
        x = -x, putchar('-');
    if (x > 9)
        write(x / 10, end_, __st + 1);
    putchar(x % 10 + '0');
    if (!__st)
        putchar(end_);
}

template <typename T>
inline void write(T x) {
    if (x < 0)
        x = -x, putchar('-');
    if (x > 9)
        write(x / 10);
    putchar(x % 10 + '0');
}

template <typename T>
inline void writeln(T x) {
    write(x);
    puts("");
}

template <typename T>
inline void write_with_alpha(T x, char end_) {
    write(x);
    putchar(end_);
}

namespace io {
#define gc() (iS == iT ? (iT = (iS = ibuff) + fread(ibuff, 1, SIZ, stdin), (iS == iT ? EOF : *iS++)) : *iS++)
const int SIZ = 1 << 21 | 1;
char *iS, *iT, ibuff[SIZ], obuff[SIZ], *oS = obuff, *oT = oS + SIZ - 1, fu[110], c;
int fr;
inline void ioout() {
    fwrite(obuff, 1, oS - obuff, stdout);
    oS = obuff;
}
template <class Type>
inline void ioread(Type& x) {
    x = 0;
    Type y = 1;
    for (c = gc(); (c > '9' || c < '0') && c != '-'; c = gc())
        ;
    c == '-' ? y = -1 : x = (c & 15);
    for (c = gc(); c >= '0' && c <= '9'; c = gc()) x = x * 10 + (c & 15);
    x *= y;
}
template <class Type>
inline void ioprint(Type x, char text = '\n') {
    if (x < 0)
        *oS++ = '-', x *= -1;
    if (x == 0)
        *oS++ = '0';
    while (x) fu[++fr] = x % 10 + '0', x /= 10;
    while (fr) *oS++ = fu[fr--];
    *oS++ = text;
    ioout();
}
inline void prints(char x[], char text = '\n') {
    for (register int i = 0; x[i]; ++i) *oS++ = x[i];
    *oS++ = text;
    ioout();
}
}  // namespace io

const int SIZE = 1e5 + 10;
const int MOD = 998244353;
set<int> st;
bool vis[2000010];
int indegree[SIZE];
int nexto[SIZE];
int top, P[2000010];

struct UndirectedGraphStoreStructor {
    int nex;
    int ver;
};

struct ThisProblemSSolveNodeItsLuoguP4323 {
    int Indx_;
    int head[SIZE];
    UndirectedGraphStoreStructor edge[SIZE << 1];
    int siz[SIZE], n;
    int Hash[SIZE], G[SIZE];

    inline void init(int t) {
        n = t;
        Indx_ = 0;
        memset(head + 1, 0, n * sizeof(int));
    }

    inline void add_edge(int x, int y) {
        edge[++Indx_].ver = y;
        edge[Indx_].nex = head[x];
        head[x] = Indx_;
    }

    inline void dfs_1(int x, int f) {
        siz[x] = 1;
        Hash[x] = 1;
        for (int i = head[x]; i; i = edge[i].nex) {
            int y = edge[i].ver;
            if (y == f)
                continue;
            dfs_1(y, x);
            siz[x] += siz[y];
            Hash[x] = (Hash[x] + 1ll * Hash[y] * P[siz[y]] % MOD) % MOD;
            //        printf("x = %d hash[x] = %d \n", x, Hash[x]);
        }
    }

    inline void dfs_2(int x, int f, int v) {
        G[x] = (Hash[x] + 1ll * v * P[n - siz[x]] % MOD) % MOD;
        //        printf("x = %d v = %d G = %d \n", x, v, G[x]);
        for (int i = head[x]; i; i = edge[i].nex) {
            int y = edge[i].ver;
            if (y == f)
                continue;
            dfs_2(y, x, (G[x] - 1ll * Hash[y] * P[siz[y]] % MOD + MOD) % MOD);
        }
    }
} t0, t1;

// inline void make_node(ThisProblemSSolveNodeItsLuoguP4323 &rhs, int t) {
//	rhs.n = t;
//	rhs.Indx_ = 0;
//	memset(rhs.head, 0, sizeof rhs.head);
//	memset(rhs._next, 0, sizeof rhs._next);
//	memset(rhs.ver, 0, sizeof rhs.ver);
//	memset(rhs.Hash, 0, sizeof rhs.Hash);
//	memset(rhs.siz, 0, sizeof rhs.siz);
//}

signed main() {
    int tmp_233 = 2000009;
    for (int i = 2; i <= tmp_233; ++i) {
        if (!vis[i])
            P[++top] = i;
        for (int j = 1; j <= top && i * P[j] <= tmp_233; ++j) {
            vis[i * P[j]] = 1;
            if (!(i % P[j]))
                break;
        }
    }
    int n;
    read(n);
    t0.init(n);
    t1.init(n + 1);
    //	make_node(t0, n);
    //	make_node(t1, n + 1);
    for (int i = 1; i < n; ++i) {
        int from, to;
        read(from);
        read(to);
        t0.add_edge(from, to);
        t0.add_edge(to, from);
    }
    for (int i = 1; i <= n; ++i) {
        int from, to;
        read(from);
        read(to);
        t1.add_edge(from, to);
        t1.add_edge(to, from);
        indegree[from]++;
        indegree[to]++;
        nexto[from] = to;
        nexto[to] = from;
    }

    t0.dfs_1(1, 0);
    t0.dfs_2(1, 0, 0);
    for (int i = 1; i <= n; ++i) st.insert(t0.G[i]);
    t1.dfs_1(1, 0);
    t1.dfs_2(1, 0, 0);

    for (int i = 1; i <= n + 1; ++i) {
        if (indegree[i] == 1) {
            int _______ = (t1.G[nexto[i]] - 2 + MOD) % MOD;
            if (st.find(_______) != st.end()) {
                write(i);
                return 0;
            }
        }
    }
    return 0;
}