// WAPER
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
#include <deque>
#include <bitset>
#include <map>
#include <set>
#define inf 1e9
#define eps 1e-6
#define N 15
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
inline ll read() {
    char ch = getchar();
    ll s = 0, w = 1;
    while (ch < '0' || ch > '9') {
        if (ch == '-')
            w = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        s = s * 10 + ch - '0';
        ch = getchar();
    }
    return s * w;
}
int n, a[1 << N], b[1 << N];
const int mod = 1e9 + 7;
int fac[N], ans;
int x[N], y[N];
inline int Z(int x) { return x >= mod ? x - mod : x; }
inline int check(int now) {
    int sum = 0;
    for (register int i = 1; i <= 1 << (n - (now + 1)); i++) {
        for (register int j = (i - 1) * (1 << (now + 1)) + 1; j < i * (1 << (now + 1)); j++) {
            if (a[j + 1] != a[j] + 1) {
                if (!sum)
                    x[now] = i;
                else
                    y[now] = i;
                sum++;
            }
        }
    }
    return sum;
}
inline int check() {
    for (register int i = 1; i <= (1 << n); i++)
        if (a[i] != i)
            return 0;
    return 1;
}
void dfs(int now, int chosen) {
    if (check()) {
        ans = ans + fac[chosen];
        return;
    }
    int p = check(now);
    //	cout<<"WTF:"<<now<<" "<<p<<" "<<x[now]<<" "<<y[now]<<endl;
    ////	for(register int i=1;i<=(1<<n);i++)cout<<a[i]<<" ";cout<<endl;
    //	cout<<endl;
    if (p >= 3 || now >= n)
        return;
    if (p == 1) {
        int d = (1 << now), p = (1 << (now + 1));
        //		cout<<"GG:"<<(x[now]-1)*p+1<<" "<<(x[now]-1)*p+d+1<<" "<<x[now]*p<<endl;
        for (register int i = (x[now] - 1) * p + 1, j = (x[now] - 1) * p + d + 1; j <= x[now] * p; i++, j++)
            swap(a[i], a[j]) /*,cout<<"EEE:"<<i<<" "<<j<<endl*/;
        dfs(now + 1, chosen + 1);
        for (register int i = (x[now] - 1) * p + 1, j = (x[now] - 1) * p + d + 1; j <= x[now] * p; i++, j++)
            swap(a[i], a[j]);
    } else if (p == 2) {
        int d = (1 << now), p = (1 << (now + 1));
        //		cout<<"c2:"<<(x[now]-1)*p+1<<" "<<(x[now]-1)*p+d<<" "<<(x[now]-1)*p+d+1<<"
        //"<<x[now]*p<<" "<<(y[now]-1)*p+1<<" "<<(y[now]-1)*p+d<<" "<<(y[now]-1)*p+d+1<<" "<<y[now]*p<<endl;
        for (register int i = (x[now] - 1) * p + 1, j = (x[now] - 1) * p + d + 1; j <= x[now] * p; i++, j++)
            swap(a[i], a[j]);
        dfs(now + 1, chosen + 1);
        for (register int i = (x[now] - 1) * p + 1, j = (x[now] - 1) * p + d + 1; j <= x[now] * p; i++, j++)
            swap(a[i], a[j]);

        for (register int i = (x[now] - 1) * p + 1, j = (y[now] - 1) * p + 1; i <= (x[now] - 1) * p + d;
             i++, j++)
            swap(a[i], a[j]);
        dfs(now + 1, chosen + 1);
        for (register int i = (x[now] - 1) * p + 1, j = (y[now] - 1) * p + 1; i <= (x[now] - 1) * p + d;
             i++, j++)
            swap(a[i], a[j]);

        for (register int i = (x[now] - 1) * p + 1, j = (y[now] - 1) * p + d + 1; j <= y[now] * p; i++, j++)
            swap(a[i], a[j]);
        dfs(now + 1, chosen + 1);
        for (register int i = (x[now] - 1) * p + 1, j = (y[now] - 1) * p + d + 1; j <= y[now] * p; i++, j++)
            swap(a[i], a[j]);

        for (register int i = (x[now] - 1) * p + d + 1, j = (y[now] - 1) * p + 1; i <= x[now] * p; i++, j++)
            swap(a[i], a[j]);
        dfs(now + 1, chosen + 1);
        for (register int i = (x[now] - 1) * p + d + 1, j = (y[now] - 1) * p + 1; i <= x[now] * p; i++, j++)
            swap(a[i], a[j]);

        for (register int i = (x[now] - 1) * p + d + 1, j = (y[now] - 1) * p + d + 1; i <= x[now] * p;
             i++, j++)
            swap(a[i], a[j]);
        dfs(now + 1, chosen + 1);
        for (register int i = (x[now] - 1) * p + d + 1, j = (y[now] - 1) * p + d + 1; i <= x[now] * p;
             i++, j++)
            swap(a[i], a[j]);

        for (register int i = (y[now] - 1) * p + 1, j = (y[now] - 1) * p + d + 1; j <= y[now] * p; i++, j++)
            swap(a[i], a[j]);
        dfs(now + 1, chosen + 1);
        for (register int i = (y[now] - 1) * p + 1, j = (y[now] - 1) * p + d + 1; j <= y[now] * p; i++, j++)
            swap(a[i], a[j]);
    }
    dfs(now + 1, chosen);
}
int main() {
    // freopen(".in","r",stdin);
    // freopen(".out","w",stdout);
    n = read();
    for (register int i = 1; i <= (1 << n); i++) a[i] = read();
    fac[0] = 1;
    for (register int i = 1; i <= n; i++) fac[i] = fac[i - 1] * i;
    dfs(0, 0);
    printf("%d\n", ans);
    return 0;
}
/*
2
1 3 2 4
*/