#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct PROG {
    int n;
    short F[1600][1600], tv[5000], tn[5000], ter, head[1650], tot;

    short cter[1650];

#define TR(a, b, c) ((*p)[a][b][c])

    void Link(int u, int v) {
        cter[u]++;
        cter[v]++;
        tv[++ter] = v;
        tn[ter] = head[u];
        head[u] = ter;
        tv[++ter] = u;
        tn[ter] = head[v];
        head[v] = ter;
    }

    void Init() {
        short(*p)[4][20][40];
        p = (short(*)[4][20][40]) new short[4 * 20 * 40];
        scanf("%d", &n);
        for (int i = 0; i < 4; i++)
            for (int j = 1; j <= n; j++)
                for (int k = 1; k <= (2 * j - 1); k++) tot++, scanf("%hd", &((*p)[i][j][k]));
        for (int id = 0; id < 4; id++)
            for (int j = 1; j <= n; j++)
                for (int k = 2; k <= (2 * j - 1); k++)
                    if (!(k % 2))
                        Link(TR(id, j, k), TR(id, j, k - 1)), Link(TR(id, j, k), TR(id, j, k + 1)),
                            Link(TR(id, j, k), TR(id, j - 1, k - 1));
        for (int i = 1; i <= n; i++) {
            Link(TR(0, n, 2 * i - 1), TR(3, n - i + 1, 1));          // AD
            Link(TR(0, i, 2 * i - 1), TR(1, i, 1));                  // AB
            Link(TR(0, i, 1), TR(2, i, 2 * i - 1));                  // AC
            Link(TR(1, n, 2 * i - 1), TR(3, i, 2 * i - 1));          // BD
            Link(TR(1, i, 2 * i - 1), TR(2, i, 1));                  // BC
            Link(TR(2, n, 2 * i - 1), TR(3, n, 2 * n - 2 * i + 1));  // CD
        }
        delete[] p;
    }

    int getCon(int id, int r) {
        static int ans;
        ans = head[id];
        while (r) ans = tn[ans], r--;
        return tv[ans];
    }

    int getPo(int id, int id2) {
        static int ans, now;
        ans = 0, now = head[id];
        while (tv[now] != id2) ans++, now = tn[now];
        return ans;
    }

    int solve(int id, int range)  // id ~ range range < id:left else right
    {
        // cout<<id<<' '<<p<<' '<<range<<endl;
        if (F[id][range])
            return F[id][range];
        int now, ans = 0, lmax = 0, rmax = 0;
        now = head[id];
        for (int i = 0; now && i < 3; i++, now = tn[now]) {
            if (range < tv[now] && tv[now] < id)
                lmax = max(lmax, solve(tv[now], id) + solve(tv[now], range) + 1);
            if (id < tv[now] && tv[now] < range)
                rmax = max(rmax, solve(tv[now], id) + solve(tv[now], range) + 1);
        }
        if (id > range)
            ans = lmax;
        else
            ans = rmax;
        F[id][range] = ans;
        return ans;
    }

    int getAns(int id) {
        int ans = solve(id, 0) + solve(id, 4 * n * n + 1) + 1;
        return ans;
    }

    int main(void) {
        ter = 1;
        Init();
        int ans = 0;
        for (int i = 1; i < tot; i++) ans = max(ans, getAns(i));
        cout << ans << endl;
        return 0;
    }
} TEST;
int res = TEST.main();
int main(){};