#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxl = 110, maxn = 10010;

int head[maxl], ver[maxn], nex[maxn], tot;
inline void addedge(int len, int id) {
    ver[tot] = id; nex[tot] = head[len]; head[len] = tot++;
}

char ch[maxn][maxl];
int split[maxn][26];
int len[maxn], ans[maxn], pre[maxn];
int mres = 0, maid = -1;

inline bool check(int x, int y) {
    for(int i = 0; i < 26; i++)
        if(split[x][i] < split[y][i])
            return false;
    return true;
}

void dp(int cur) {
    ans[cur] = 1;
    for(int i = head[len[cur]-1]; i != -1; i = nex[i])
        if(check(cur, ver[i])) {
            if(!ans[ver[i]]) dp(ver[i]);
            if(ans[ver[i]] + 1 > ans[cur]) ans[cur] = ans[ver[i]] + 1, pre[cur] = ver[i];
        }
    if(ans[cur] > mres) mres = ans[cur], maid = cur;
}

int stack[10010], st = 0;
int main() {
    int pc = -1;
    memset(head, -1, sizeof(head));
    memset(pre, -1, sizeof(pre));
    while(scanf("%s", ch[++pc]) == 1) {
        len[pc] = strlen(ch[pc]);
        for(int i = 0; i < len[pc]; i++)
            split[pc][ch[pc][i]-'a']++;
        addedge(len[pc], pc);
    }
    for(int i = 0; i <= pc; i++) {
        if(ans[i]) continue;
        dp(i);
    }
    printf("%d\n", mres);
    for(int i = maid; i != -1; i = pre[i])
        stack[st++] = i;
    for(int i = st - 1; i > -1; --i)
        printf("%s\n", ch[stack[i]]);
    return 0;
}