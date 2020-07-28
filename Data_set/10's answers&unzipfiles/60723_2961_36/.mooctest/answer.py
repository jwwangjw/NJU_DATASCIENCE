#include <bits/stdc++.h>
#define rep(i, j, k) for (register int i = j; i <= k; ++i)
#define drep(i, j, k) for (register int i = j; i >= k; --i)
inline int read(){
    char ch = getchar(); int u = 0, f = 1;
    while (!isdigit(ch)) { if(ch == '-') f = -1; ch = getchar();}
    while (isdigit(ch)) { u = (u << 3) + (u << 1) + ch - 48; ch = getchar();}
    return u * f;
}
const int maxn = 1e6 + 10;
namespace SuffixArry{
    int tax[maxn], Rank[maxn], str[maxn], SA[maxn], tmp[maxn], n, m;
    char ch[maxn];
    inline void Init(){
        scanf("%s", ch + 1);
        n = strlen(ch + 1);
        rep (i, 1, n) str[i] = (int)ch[i];
        rep (i, n + 1, n << 1) str[i] = str[i - n];
        n <<= 1; //把字符串接到自己后面求后缀数组
    } 
    inline void radix_sort(int m){
        memset(tax, 0, sizeof(int) * (m + 1));
        rep (i, 1, n) tax[Rank[i]]++;
        rep (i, 2, m) tax[i] += tax[i - 1];
        drep (i, n, 1) SA[tax[Rank[tmp[i]]]--] = tmp[i];
    }
    inline bool cmp(int *f, int x, int y, int w){
        return f[x] == f[y] && (x + w > n ? -1 : f[x + w]) == (y + w > n ? -1 : f[y + w]); 
    }
    inline void build(){
        rep (i, 1 ,n) Rank[i] = str[i], tmp[i] = i;
        m = 1005;
        radix_sort(m);
        for (int p = 1, w = 1; p < n; m = p, w <<= 1){
            p = 0;
            rep (i, n - w + 1, n) tmp[++p] = i;
            rep (i, 1, n) SA[i] > w ? tmp[++p] = SA[i] - w: 0;
            radix_sort(m);
            rep (i, 1, n) tmp[i] = Rank[i];
            Rank[SA[1]] = p = 1;
            rep (i, 2, n) Rank[SA[i]] = cmp(tmp, SA[i], SA[i - 1], w) ? p : ++p;
        }
    }
    inline void Print(){
        rep (i, 1, n) if (SA[i] <= (n >> 1)) putchar(str[SA[i] + (n >> 1) - 1]); //如果开头在原串里面，就输出答案。
    }
}
int main(){
    SuffixArry :: Init();
    SuffixArry :: build();
    SuffixArry :: Print();
    return 0;
}