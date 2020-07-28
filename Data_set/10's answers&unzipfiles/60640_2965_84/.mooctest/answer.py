#include <cstdio>
using namespace std;
int k, m, n, pos, a[200005], b[200005], c[200005];
char s[200005];
int main() {
    scanf("%d%d", &k, &m);
    scanf("%s", s);
    scanf("%d", &n);
    for (register int i = 1; i <= n; ++i) scanf("%d%d%d", &a[i], &b[i], &c[i]);
    for (register int i = 0; i < k; ++i) {
        pos = i;
        for (register int j = n; j >= 1; --j) {
            if (pos >= c[j] + b[j] - a[j])
                pos = pos - b[j] + a[j];
            else if (pos >= c[j])
                pos = pos - c[j] + a[j];
        }
        printf("%c", s[pos]);
    }
    return 0;
}