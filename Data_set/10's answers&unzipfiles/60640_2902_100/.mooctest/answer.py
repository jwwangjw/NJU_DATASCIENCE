#include <bits/stdc++.h>
using namespace std;

namespace IO {
    #pragma GCC target("avx")
    #pragma GCC optimize("Og")
    #pragma GCC optimize("Ofast")

    template<class T>
    inline void read(T& x) {
        x = 0;
        char ch;
        while(ch < '0' || ch > '9') {
            ch = getchar();
        }
        while(ch >= '0' && ch <= '9') {
            x = x * 10 + ch - '0';
            ch = getchar();
        }
    }

    template<class T>
    inline void write(T x) {
        if(x > 9) write(x / 10);
        putchar(x % 10 + '0');
    }
};

using namespace IO;

const int N = 110;

int n;
char str[N][N];

int main() {
    read(n);
    for(int i = 1;i <= n/2;i++) {//1st 2nd
        for(int j = 1;j <= n/2 - i + 1;j++) {// 1st
            putchar('*');
        }
        for(int j = 1;j <= 2*i-1;j++) {//全输
            putchar('D');
        }
        for(int j = 1;j <= n/2 - i + 1;j++) {// 2nd
            putchar('*');
        }
        puts("");
    }
    for(int i = 1;i <= n;i++) putchar('D');puts("");
    for(int i = n/2;i >= 1;i--) {// 3rd 4th
        for(int j = 1;j <= n/2 - i + 1;j++) {// 3rd
            putchar('*');
        }
        for(int j = 1;j <= 2*i-1;j++) {//全输
            putchar('D');
        }
        for(int j = 1;j <= n/2 - i + 1;j++) {// 4th
            putchar('*');
        }
        puts("");
    }
    return 0;
}