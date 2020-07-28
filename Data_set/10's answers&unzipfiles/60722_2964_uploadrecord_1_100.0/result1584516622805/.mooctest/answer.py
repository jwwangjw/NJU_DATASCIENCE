#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;
int n, i, j, len[205], ans, sum[10];
char s[205][100005];
void dfs(int x, int y, int k) {
    if (k + abs((len[j] - y) - (len[i] - x)) >= ans)
        return;
    while (x <= len[i] && y <= len[j] && s[i][x] == s[j][y]) x++, y++;
    if (x == len[i] + 1 && y == len[j] + 1) {
        ans = min(ans, k);
        return;
    }
    if (x <= len[i])
        dfs(x + 1, y, k + 1);
    if (y <= len[j])
        dfs(x, y + 1, k + 1);
    if (x <= len[i] && y <= len[j])
        dfs(x + 1, y + 1, k + 1);
}
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%s", s[i] + 1), len[i] = strlen(s[i] + 1);
    for (i = 1; i <= n; i++)
        for (j = i + 1; j <= n; j++) {
            ans = 9;
            dfs(1, 1, 0);
            sum[ans]++;
        }
    for (int i = 1; i <= 8; i++) printf("%d ", sum[i]);
}