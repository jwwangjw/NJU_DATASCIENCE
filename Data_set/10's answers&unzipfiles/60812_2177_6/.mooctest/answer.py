#include <bits/stdc++.h>
using namespace std;
int main() {
    int k, a[200000];
    scanf("%d", &k);
    int n = k + 1;
    printf("%d\n", n);
    a[n] = n;
    for (int i = n - 2; i > 0; i -= 2) a[i] = a[i + 2] - 1;
    for (int i = n - 1; i > 0; i -= 2) a[i] = a[i + 2] + 1;
    for (int i = 1; i <= n; i++) printf("%d ", a[i]);
}