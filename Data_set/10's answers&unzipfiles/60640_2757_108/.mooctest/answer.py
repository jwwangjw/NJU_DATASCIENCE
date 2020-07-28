#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;
namespace tools {
    bool digit (int ch) { return (ch <= '9' and ch >= '0');}
    inline int in () {
        int x = 0, ch = getchar(), base = 1;
        while (!digit(ch)) { base = (ch == '-')? -1: 1; ch = getchar();}
        while (digit(ch)) { x = x*10+ch-'0'; ch = getchar();}
        return x*base;
    }
    template <class T> inline void smax (T& x, T y) { x = max(x, y);}
    template <class T> inline void smin (T& x, T y) { x = min(x, y);}
    inline void print (int x) { printf("debug:%d\n", x);}
}
using namespace tools;

const int N = 710, M = 45;
struct Big {
    int l, t[M];
} Zero;
int n, root = 1;
int sz[N], ac[N][N]; 
long long tag[M];
Big f[N][N];
int nxt[N<<1], to[N<<1], head[N], index_edge;
inline void add (int u, int v) {
    int i = ++index_edge;
    nxt[i] = head[u]; to[i] = v; head[u] = i;
}

int Mod (int x) {
    return (x-1000*(x/1000));
}
void printBig (Big x) {
    for (int i = x.l; i; --i) {
        if (i == x.l) printf("%d", x.t[i]);
        else printf("%d%d%d", x.t[i]/100, (x.t[i]/10)%10, x.t[i]%10);
    }
    puts("");
}

void Spread (Big& x) {
    for (int i = 1; i <= x.l; ++i) {
        x.t[i] = Mod(tag[i]);
        tag[i+1] += tag[i]/1000;
        if (i == x.l and tag[i+1]) x.l++;
    }
}
Big MBig (Big x, Big y) {
    memset(tag, 0, sizeof(tag));
    int Maxl = 0;
    for (int j = 1; j <= y.l; ++j) {
        for (int i = 1; i <= x.l; ++i) {
            int tmp = y.t[j]*x.t[i];
            int l = i+j-1;
            while (tmp) {
                tag[l] += Mod(tmp);
                tmp /= 1000;
                smax(Maxl, l); l++;
            }
        }
    }
    x.l = Maxl;
    Spread(x); return x;
}
Big Max (Big x, Big y) {
    if (x.l != y.l) return (x.l > y.l)? x: y;
    for (int i = x.l; i; --i) {
        if (x.t[i] == y.t[i]) continue;
        return (x.t[i] > y.t[i])? x: y;
    }
    return x;
}
void GetAns (int x, int fa) {
    sz[x]++;
    f[x][0] = f[x][1] = Zero;
    ac[x][0] = ac[x][1] = true;

    for (int i = head[x]; i; i = nxt[i]) {
        int e = to[i];
        if (e == fa) continue;
        GetAns(e, x);
        sz[x] += sz[e];
        for (int l = sz[x]; l; --l) {
            for (int k = 0; k <= sz[e]; ++k) {
                if (l-k <= 0) break;
                if (!ac[x][l-k] or !ac[e][k]) continue;
                f[x][l] = Max(f[x][l], MBig(f[x][l-k], f[e][k]));
                ac[x][l] = true;
            }
        }
    }
    for (int i = 1; i <= sz[x]; ++i) {
        if (!ac[x][i]) continue;
        Big New = Zero; New.t[1] = i;
        f[x][0] = Max(f[x][0], MBig(f[x][i], New));
    }
}
void work () {
    GetAns(root, 0);
    printBig(f[root][0]);
}
void prepare () {
    Zero.l = 1; Zero.t[1] = 1;
    n = in();
    for (int i = 1; i < n; ++i) {
        int u = in(), v = in();
        add(u, v); add(v, u);
    }
    work();
}

int main () {
    prepare();
}