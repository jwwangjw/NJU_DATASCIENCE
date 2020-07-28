#include <bits/stdc++.h>

using namespace std;

const int lim = 1e6 + 10;
char str[lim], pat[lim];
int fa[lim];
inline void kmp(char *pat, int len, int *fa) {
    int k, i = 0;
    fa[0] = k = -1;
    while (i < len) {
        while (k >= 0 && pat[i] != pat[k]) k = fa[k];
        fa[++i] = ++k;
    }
}

int main(void) {
    scanf("%s%s", str, pat);
    int slen = strlen(str), plen = strlen(pat);
    int ans = 0;
    kmp(pat, plen, fa);
    for (int i = 0, k = 0; i < slen; ++i) {
        while (k >= 0 && pat[k] != str[i]) k = fa[k];
        if (++k == plen) {
            ++ans;
            k = fa[k];
        }
    }
    printf("%d", ans);
    return 0;
}