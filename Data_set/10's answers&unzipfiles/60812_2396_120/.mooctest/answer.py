#include <bits/stdc++.h>
using namespace std;
#define min(a, b) (a) < (b) ? (a) : (b)

#define MAXN 100009
template <class T>
inline void read(T &x) {
    x = 0;
    bool f = 0;
    char c = getchar();
    for (; !isdigit(c); c = getchar())
        if (c == '-')
            f = 1;
    for (; isdigit(c); c = getchar()) x = (x << 3) + (x << 1) + (c ^ 48);
    if (f)
        x = -x;
}

struct Node {
    int pos, num;
    bool operator<(const Node &i) const {
        if (num != i.num)
            return num < i.num;
        return pos < i.pos;
    }
} a[MAXN];
int val[MAXN], rnd[MAXN], tag[MAXN], siz[MAXN], son[MAXN][2], minn[MAXN];
int rt, x, y, z, tot, n;
int v[MAXN];

int build(int x) {
    val[++tot] = x, minn[tot] = x, siz[tot] = 1;
    rnd[tot] = rand();
    return tot;
}
int update(int x) {
    siz[x] = siz[son[x][0]] + siz[son[x][1]] + 1;
    minn[x] = val[x];
    if (son[x][0])
        minn[x] = min(minn[x], minn[son[x][0]]);
    if (son[x][1])
        minn[x] = min(minn[x], minn[son[x][1]]);
}
void pushdown(int x) {
    if (!tag[x])
        return;
    swap(son[x][0], son[x][1]);
    if (son[x][0])
        tag[son[x][0]] ^= 1;
    if (son[x][1])
        tag[son[x][1]] ^= 1;
    tag[x] = 0;
}
int merge(int x, int y) {
    if (!x || !y)
        return x | y;
    if (rnd[x] < rnd[y]) {
        pushdown(x);
        son[x][1] = merge(son[x][1], y);
        update(x);
        return x;
    }

    pushdown(y);
    son[y][0] = merge(x, son[y][0]);
    update(y);
    return y;
}
void split(int now, int k, int &x, int &y) {
    if (!now) {
        x = y = 0;
        return;
    }

    pushdown(now);
    if (siz[son[now][0]] < k) {
        x = now;
        split(son[x][1], k - siz[son[x][0]] - 1, son[x][1], y);
    } else {
        y = now;
        split(son[y][0], k, x, son[y][0]);
    }
    update(now);
}
int getrk(int x) {
    int k = 1;
    while (1) {
        pushdown(x);
        if (son[x][0] && minn[son[x][0]] == minn[x])
            x = son[x][0];
        else if (son[x][1] && minn[son[x][1]] == minn[x])
            k += siz[son[x][0]] + 1, x = son[x][1];
        else
            return k + siz[son[x][0]];
    }
}

int main() {
    // freopen("sort1.in", "r", stdin);
    // freopen("sort.out", "w", stdout);
    read(n);
    for (int i = 1; i <= n; i++) {
        read(a[i].num), a[i].pos = i;
    }

    sort(a + 1, a + n + 1);
    for (int i = 1; i <= n; i++) v[a[i].pos] = i;

    for (int i = 1; i <= n; i++) rt = merge(rt, build(v[i]));

    for (int i = 1; i <= n; i++) {
        int k = getrk(rt);
        split(rt, k, x, y);
        split(x, k - 1, x, z);
        tag[x] ^= 1;
        rt = merge(x, y);
        printf("%d ", k + i - 1);
    }
    return 0;
}