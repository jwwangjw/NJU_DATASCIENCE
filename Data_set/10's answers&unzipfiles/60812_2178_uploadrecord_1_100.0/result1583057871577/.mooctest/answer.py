#include <bits/stdc++.h>
using namespace std;
const int Max_N = 1e5;
int n, lst = 1, cnt = 1, Max[Max_N * 2 + 10] = {}, P[Max_N * 2 + 10] = {};
long long ans = 0;
map<int, int> t[Max_N * 2 + 10] = {};
inline void Add(int x) {
    int p = lst;
    int np = lst = ++cnt;
    Max[np] = Max[p] + 1;
    for (; p && !t[p][x]; t[p][x] = np, p = P[p])
        ;
    if (!p)
        P[np] = 1;
    else {
        int q = t[p][x];
        if (Max[q] == Max[p] + 1)
            P[np] = q;
        else {
            int nq = ++cnt;
            t[nq] = t[q];
            P[nq] = P[q];
            Max[nq] = Max[p] + 1;
            P[q] = P[np] = nq;
            for (; p && t[p][x] == q; t[p][x] = nq, p = P[p])
                ;
        }
    }
    ans += Max[np] - Max[P[np]];
}
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        int x;
        scanf("%d", &x);
        Add(x);
        printf("%lld\n", ans);
    }
    return 0;
}