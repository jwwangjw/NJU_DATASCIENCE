#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int MAXN = 1e6 + 4;
int sa[MAXN], rk[MAXN], len;
int t1[MAXN], t2[MAXN], cc[MAXN];
bool cmp(int *y, int a, int b, int k) {
    int a1 = y[a], b1 = y[b];
    int a2 = ((a + k >= len) ? -1 : y[a + k]);
    int b2 = ((b + k >= len) ? -1 : y[b + k]);
    return a1 == b1 && a2 == b2;
}

void getsa(int *s, int m) {
    int *x = t1;
    int *y = t2;
    for (int i = 0; i < m; i++) cc[i] = 0;
    for (int i = 0; i < len; i++) {
        x[i] = s[i];
        ++cc[x[i]];
    }
    for (int i = 1; i < m; i++) cc[i] += cc[i - 1];
    for (int i = len - 1; i >= 0; i--) sa[--cc[x[i]]] = i;
    for (int k = 1; k < len; k <<= 1) {
        int p = 0;
        for (int i = len - k; i < len; i++) y[p++] = i;
        for (int i = 0; i < len; i++)
            if (sa[i] >= k)
                y[p++] = sa[i] - k;
        for (int i = 0; i < m; i++) cc[i] = 0;
        for (int i = 0; i < len; i++) ++cc[x[y[i]]];
        for (int i = 1; i < m; i++) cc[i] += cc[i - 1];
        for (int i = len - 1; i >= 0; i--) sa[--cc[x[y[i]]]] = y[i];
        swap(x, y);
        m = 1;
        x[sa[0]] = 0;
        for (int i = 1; i < len; i++) {
            if (cmp(y, sa[i - 1], sa[i], k)) {
                x[sa[i]] = m - 1;
            } else {
                x[sa[i]] = m++;
            }
        }
        if (m >= len)
            break;
    }
}

void init(int *s, int l, int m) {
    len = l;
    getsa(s, m);
}
char s[MAXN];
int ss[MAXN];
int main() {
    scanf("%s", s);
    int l = strlen(s);
    for (int i = 0; i < l; i++) ss[i] = s[i];
    init(ss, l, 255);
    for (int i = 0; i < l; i++) rk[sa[i]] = i;
    for (int i = 0; i < l; i++) {
        printf("%d", sa[i] + 1);
        if (i == l - 1)
            puts("");
        else
            printf(" ");
    }
    return 0;
}