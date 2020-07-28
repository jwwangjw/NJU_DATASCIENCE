#include <bits/stdc++.h>
#define mul 1000000007ull
#define N 1000005
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int n, m;
ull hsh[205][205], p[205];
char s[205][205];
int now;
ull t[20005], len, ans;
int sa[N], sa2[N], rnk[N], sum[N], key[N], height[N];
map<ull, int> mp;

inline bool check(int *num, int x, int y, int l) {
    return num[x] == num[y] && num[x+l] == num[y+l];
}

inline void suffix(int n, int m) {
    int i, j, p; int *_rnk = rnk, *_sa2 = sa2;
    for (i = 1; i <= m; i++) sum[i] = 0;
    for (i = 1; i <= n; i++) sum[_rnk[i]=t[i]]++;
    for (i = 2; i <= m; i++) sum[i] += sum[i-1];
    for (i = n; i >= 1; i--) sa[sum[_rnk[i]]--] = i;
    for (j = 1; j <= n; j <<= 1, m = p) {
        for (p = 0, i = n - j + 1; i <= n; i++) _sa2[++p] = i;
        for (i = 1; i <= n; i++) if (sa[i] > j) _sa2[++p] = sa[i] - j;
        for (i = 1; i <= n; i++) key[i] = _rnk[_sa2[i]];
        for (i = 1; i <= m; i++) sum[i] = 0;
        for (i = 1; i <= n; i++) sum[key[i]]++;
        for (i = 2; i <= m; i++) sum[i] += sum[i-1];
        for (i = n; i >= 1; i--) sa[sum[key[i]]--] = _sa2[i];
        for (swap(_rnk, _sa2), i = 2, p = 2, _rnk[sa[1]] = 1; i <= n; i++) {
            _rnk[sa[i]] = check(_sa2, sa[i-1], sa[i], j) ? p-1 : p++;
        }
    } 
    p = 0;
    for (i = 1; i <= n; i++) rnk[sa[i]] = i;
    for (i = 1; i <= n; i++) {
        if (p) p--; j = sa[rnk[i]-1];
        while (t[i+p] == t[j+p]) p++;
        height[rnk[i]] = p; 
    }
}


int main() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) scanf("%s", s[i]+1);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            hsh[i][j] = (hsh[i][j-1] * mul + s[i][j]-'A'+1);
        }
    }
    p[0] = 1;
    for (int i = 1; i <= 200; i++) {
        p[i] = p[i-1] * mul;
    }
    for (int l = 1; l <= m; l++) {
        len = 0; now = 0; mp.clear();
        for (int j = 1; j <= m - l + 1; j++) {
            for (int i = 1; i <= n; i++) {
                ull x = hsh[i][j+l-1] - hsh[i][j-1] * p[l];
                if (!mp[x]) mp[x] = ++now;
                t[++len] = mp[x];
            }
            t[++len] = ++now; 
        }
        now += 10;
        suffix(len, now); 
        ans += n * (n+1) / 2 * (m - l + 1);
        for (int i = 1; i <= len; i++) {
            ans -= height[i];
        }
    }
    printf("%lld", ans);
    return 0;
}