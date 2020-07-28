#include <bits/stdc++.h>

#define For(i, _l, _r) for (int i = (_l), i##r = (_r); i <= (i##r); ++i)
#define Lop(i, _l, _r) for (int i = (_l), i##r = (_r); i >= (i##r); --i)
#define Rep(i, _l, _r) for (int i = (_l); i; i = (_r))
#define debug(...) fprintf(stderr, __VA_ARGS__)

template <typename T>
T max(T x, T y) {
    return (x > y) ? x : y;
}
template <typename T>
T min(T x, T y) {
    return (x < y) ? x : y;
}
template <typename T>
bool chkmax(T &x, T y) {
    return (x >= y) ? 0 : (x = y, 1);
}
template <typename T>
bool chkmin(T &x, T y) {
    return (x <= y) ? 0 : (x = y, 1);
}

namespace Input_Ouput {
static const int len = 1 << 20 | 1;
char buffer[len], *S, *T;

char get_char() {
    if (S == T)
        T = (S = buffer) + fread(buffer, 1, len, stdin);
    return (S == T) ? EOF : *(S++);
}
}  // namespace Input_Ouput

#define getchar() Input_Ouput ::get_char()

template <typename T>
T read(T &in) {
    in = 0;
    char ch;
    T f = 1;
    while (!isdigit(ch = getchar()))
        if (ch == '-')
            f = -1;
    while (isdigit(ch)) in = in * 10 + ch - '0', ch = getchar();
    return in *= f;
}

typedef unsigned long long ull;
static const int base = 131;
static const int max1 = 1000000 + 11;
static const int max2 = 2000000 + 11;
static const int max3 = 4000000 + 11;

int n, m;
int l1, l2, l3, r1, r2, r3;

bool vis[max1];
int str[max2], fail[max2], RL[max3];
int S[max1], T[max1], __S[max1], __T[max1];
int k1[max1], k2[max1];
ull hS[max1], hT[max1], powb[max1];

void hash(int *S, ull *T) {
    T[0] = 0;
    For(i, 1, n) T[i] = T[i - 1] * base + S[i];
}

ull GetHash(ull *a, int l, int r) { return a[r] - a[l - 1] * powb[r - l + 1]; }

void kmp(int *__S, int *fail) {
    For(i, 0, n - 1) str[i] = __S[i + 1], fail[i] = 0;

    int k = 0;
    For(i, 1, n - 1) {
        while (k && str[i] != str[k]) k = fail[k - 1];
        if (str[i] == str[k])
            ++k;
        fail[i] = k;
    }

    Lop(i, n, 2) fail[i] = fail[i - 1];
}

void kmp(int *__S, int *__T, int *__fail) {
    int m = 0;
    For(i, 1, n) str[m++] = __T[i];
    str[m++] = 0;
    For(i, 1, n) str[m++] = __S[i];
    memset(fail, 0, sizeof(int) * m);

    int k = 0;
    For(i, 1, m - 1) {
        while (k && str[i] != str[k]) k = fail[k - 1];
        if (str[i] == str[k])
            ++k;
        fail[i] = k;
    }

    For(i, 1, n) __fail[i] = fail[n + i];
}

bool checkABC() {
    For(i, 1, n) if (S[i] != T[i]) return 0;
    l1 = r1 = 1, l2 = r2 = 2, l3 = 3, r3 = n;
    return 1;
}

bool checkACB() {
    memset(vis, 0, sizeof(bool) * (n + 1)), vis[0] = 1;

    kmp(__S, __T, k1), kmp(__T, k2);

    int p = 1;
    while (S[p] == T[p]) ++p;
    --p;

    Lop(i, min(n - 2, p), 1) {
        int k = k1[n - i];
        while (!vis[k]) {
            vis[k] = 1;
            if (GetHash(hS, i + k + 1, n) == GetHash(hT, i + 1, n - k)) {
                l1 = 1, r1 = i;
                l3 = i + 1, r3 = l3 + k - 1;
                l2 = r3 + 1, r2 = n;
                return 1;
            }
            k = k2[k];
        }
    }
    return 0;
}

bool checkBAC() {
    memset(vis, 0, sizeof(bool) * (n + 1)), vis[0] = 1;

    kmp(S, T, k1), kmp(T, k2);

    int p = n;
    while (S[p] == T[p]) --p;
    ++p;

    For(i, max(3, p), n) {
        int k = k1[i - 1];
        while (!vis[k]) {
            vis[k] = 1;
            if (GetHash(hS, 1, i - 1 - k) == GetHash(hT, k + 1, i - 1)) {
                l2 = 1, r2 = i - 1 - k;
                l1 = r2 + 1, r1 = i - 1;
                l3 = i, r3 = n;
                return 1;
            }
            k = k2[k];
        }
    }
    return 0;
}

bool checkBCA() {
    For(i, 1, n - 2) if (GetHash(hS, 1, i) == GetHash(hT, n - i + 1, n) &&
                         GetHash(hS, i + 1, n) == GetHash(hT, 1, n - i)) {
        l1 = i + 1, r1 = i + 1;
        l2 = r1 + 1, r2 = n;
        l3 = 1, r3 = i;
        return 1;
    }
    return 0;
}

bool checkCAB() {
    For(i, 1, n - 1) {
        if (GetHash(hS, 1, i) == GetHash(hT, n - i + 1, n) &&
            GetHash(hS, i + 1, n) == GetHash(hT, 1, n - i)) {
            l1 = i + 1, r1 = n;
            l2 = r2 = 1;
            l3 = r2 + 1, r3 = l1 - 1;
            return 1;
        }
    }
    return 0;
}

bool checkCBA() {
    static int S[max3], f[max3];

    int m = 0;
    For(i, 1, n) str[++m] = T[n - i + 1], str[++m] = ::S[i];

    int temp_m = m;

    m = 0;
    S[0] = -2, S[++m] = -1;
    For(i, 1, temp_m) S[++m] = str[i], S[++m] = -1;
    S[m + 1] = -3;

    int mx = 0, pos = 0;
    For(i, 1, m) {
        if (i < mx)
            RL[i] = min(mx - i + 1, RL[2 * pos - i]);
        else
            RL[i] = 1;

        while (S[i - RL[i]] == S[i + RL[i]]) ++RL[i];

        if (chkmax(mx, i + RL[i] - 1))
            pos = i;
    }

    static bool v[max3];
    static int is[max3];

    memset(is, 0, sizeof(int) * (m + 1));
    memset(v, 0, sizeof(bool) * (m + 1));

    For(i, 1, m) if (i & 1) if (i + RL[i] - 1 == m) v[i - RL[i] + 1] = 1;

    int last = 0;
    Lop(i, m, 1) if (i & 1) {
        if (last && RL[(i + last) >> 1] >= ((last - i) >> 1) + 1)
            is[i] = (last - i) >> 2;
        if (v[i])
            last = i;
    }

    memset(f, 0, sizeof(int) * (m + 1));
    For(i, 1, m) if (i & 1) chkmax(f[i - RL[i] + 1], i);

    For(i, 3, m) if (i & 1) chkmax(f[i], f[i - 2]);
    For(i, 1, m) if (i & 1 && f[i]) {
        int w = f[i] + f[i] - i;
        if (w > m)
            continue;
        if (RL[(w + m) >> 1] >= ((m - w) >> 1) + 1)
            is[i] = (f[i] - i) >> 1;
    }

    For(i, 3, m) if (i & 1) {
        if (RL[i] == i) {
            if (is[(i << 1) - 1]) {
                l3 = 1, r3 = i >> 1;
                l2 = r3 + 1, r2 = l2 + is[(i << 1) - 1] - 1;
                l1 = r2 + 1, r1 = n;
                return 1;
            }
        }
    }

    return 0;
}

void print() {
    puts("YES");
    printf("%d %d\n", l1, r1);
    printf("%d %d\n", l2, r2);
    printf("%d %d\n", l3, r3);
}

void Main() {
    static int id = 0;

    l1 = r1 = l2 = r2 = l3 = r3 = 0;

    read(n), read(m);
    For(i, 1, n) __T[n - i + 1] = read(T[i]);
    For(i, 1, n) __S[n - i + 1] = read(S[i]);

    hash(S, hS), hash(T, hT);

    if (checkABC())
        print();
    else if (checkACB())
        print();
    else if (checkBAC())
        print();
    else if (checkBCA())
        print();
    else if (checkCAB())
        print();
    else if (checkCBA())
        print();
    else
        puts("NO");
}

int main() {
    powb[0] = 1;
    For(i, 1, 1000000) powb[i] = powb[i - 1] * base;

    int T;
    read(T);

    while (T--) Main();

    return 0;
}