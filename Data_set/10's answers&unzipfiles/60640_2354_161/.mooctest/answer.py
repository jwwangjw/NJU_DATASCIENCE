// ===================================
//   author: M_sea
//   website: http://m-sea-blog.com/
// ===================================
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#define re register
using namespace std;
typedef long long ll;

inline ll read() {
    ll X = 0, w = 1;
    char c = getchar();
    while (c < '0' || c > '9') {
        if (c == '-')
            w = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') X = X * 10 + c - '0', c = getchar();
    return X * w;
}

const int N = 1000 + 10;
const int mod = 1e9 + 7;
inline int qpow(int a, ll b) {
    int c = 1;
    for (; b; b >>= 1, a = 1ll * a * a % mod)
        if (b & 1)
            c = 1ll * c * a % mod;
    return c;
}

int n, m;
ll k;
char s[N][N];

struct Matrix {
    int s[2][2];
    Matrix() { s[0][0] = s[0][1] = s[1][0] = s[1][1] = 0; }
    int* operator[](int i) { return s[i]; }
} M;
Matrix operator*(Matrix a, Matrix b) {
    Matrix c;
    for (re int i = 0; i < 2; ++i)
        for (re int k = 0; k < 2; ++k)
            for (re int j = 0; j < 2; ++j) c[i][j] = (c[i][j] + 1ll * a[i][k] * b[k][j]) % mod;
    return c;
}
inline Matrix qpow(Matrix a, ll b) {
    Matrix c;
    c[0][0] = c[1][1] = 1;
    for (; b; b >>= 1, a = a * a)
        if (b & 1)
            c = c * a;
    return c;
}

int main() {
    n = read(), m = read(), k = read();
    for (re int i = 1; i <= n; ++i) scanf("%s", s[i] + 1);
    int ud = 0, lr = 0, c = 0, ud_ = 0, lr_ = 0;
    for (re int i = 1; i <= m; ++i)
        if (s[1][i] == '#' && s[n][i] == '#')
            ++ud;
    for (re int i = 1; i <= n; ++i)
        if (s[i][1] == '#' && s[i][m] == '#')
            ++lr;
    for (re int i = 1; i <= n; ++i)
        for (re int j = 1; j <= m; ++j)
            if (s[i][j] == '#')
                ++c;
    for (re int i = 1; i < n; ++i)
        for (re int j = 1; j <= m; ++j)
            if (s[i][j] == '#' && s[i + 1][j] == '#')
                ++ud_;
    for (re int i = 1; i <= n; ++i)
        for (re int j = 1; j < m; ++j)
            if (s[i][j] == '#' && s[i][j + 1] == '#')
                ++lr_;
    if (ud && lr)
        puts("1");
    else if (!ud && !lr)
        printf("%d\n", qpow(c, k - 1));
    else if (ud) {
        M[0][0] = c, M[0][1] = ud_, M[1][0] = 0, M[1][1] = ud;
        M = qpow(M, k - 1);
        printf("%d\n", (M[0][0] - M[0][1] + mod) % mod);
    } else {
        M[0][0] = c, M[0][1] = lr_, M[1][0] = 0, M[1][1] = lr;
        M = qpow(M, k - 1);
        printf("%d\n", (M[0][0] - M[0][1] + mod) % mod);
    }
    return 0;
}