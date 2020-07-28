#include <bits/stdc++.h>
using namespace std;
int num;
struct trie {
    int son[10], end = 0;
} a[1000001];
int main() {
    string s;
    int cnt = 0;
    while (cin >> s) {
        num++;
        memset(a, 0, sizeof(a));
        int n;
        cnt = 0;
        bool flag = 0;
        while (1) {
            int now = 0;
            for (int k = 1; k <= s.length(); k++) {
                if (a[now].son[s[k - 1] - '0']) {
                    now = a[now].son[s[k - 1] - '0'];
                } else {
                    a[now].son[s[k - 1] - '0'] = ++cnt;
                    now = cnt;
                }
                if (a[now].end == 1) {
                    flag = 1;
                }
                if (k == s.length()) {
                    for (int i = 0; i <= 9; i++) {
                        if (a[now].son[i])
                            flag = 1;
                    }
                    a[now].end = 1;
                }
            }
            cin >> s;
            if (s == "9")
                break;
        }
        if (flag) {
            printf("Set %d is not immediately decodable\n", num);
        } else {
            printf("Set %d is immediately decodable\n", num);
        }
    }
    return 0;
}