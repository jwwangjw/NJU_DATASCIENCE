#include <bits/stdc++.h>
#define maxn 2005
#define rep(i, j, k) for (int i = (j); i <= (k); i++)
using namespace std;

int n, m, Q, s[maxn][maxn], s1[maxn][maxn], s2[maxn][maxn];
int cal(int a, int b, int c, int d, int s[maxn][maxn]) {
    return s[c][d] - s[a - 1][d] - s[c][b - 1] + s[a - 1][b - 1];
}
char ch[maxn];

int main() {
    scanf("%d%d%d", &n, &m, &Q);
    rep(i, 1, n) {
        scanf("%s", ch + 1);
        rep(j, 1, m) {
            s[i][j] = ch[j] - '0';
            if (s[i][j] && s[i - 1][j])
                s1[i][j]++;
            if (s[i][j] && s[i][j - 1])
                s2[i][j]++;
        }
    }
    rep(i, 1, n) rep(j, 1, m) s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1],
        s1[i][j] += s1[i - 1][j] + s1[i][j - 1] - s1[i - 1][j - 1],
        s2[i][j] += s2[i - 1][j] + s2[i][j - 1] - s2[i - 1][j - 1];
    for (int a, b, c, d; Q--;) {
        scanf("%d%d%d%d", &a, &b, &c, &d);
        printf("%d\n", cal(a, b, c, d, s) - cal(a + 1, b, c, d, s1) - cal(a, b + 1, c, d, s2));
    }
}